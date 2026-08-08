# -*- coding: utf-8 -*-
"""El libro mayor de costos: docs/COSTOS.jsonl.

POR QUE EXISTE. Al cerrar el ciclo del censo (ago 2026) el fundador pidio el
costo total y no se pudo certificar: cada corrida imprimia lo suyo por pantalla
y lo escribia en un informe que la corrida siguiente PISABA. Al final quedaba la
ultima tanda de cada script y nada mas. La suma tenia que salir de la memoria
del chat, que es exactamente el tipo de numero que este proyecto no acepta.

LA POLITICA QUE LO ORDENA: "un numero honesto con su limite declarado vale mas
que uno redondo de memoria."

El libro es de APENDICE: una linea por corrida, JSONL, nunca se reescribe. Una
corrida que no anota no existio, y por eso anotar no puede tumbar la corrida:
si el disco falla, el trabajo ya esta hecho y el aviso va por pantalla.
"""
import json
import os
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
LIBRO = BASE / "docs" / "COSTOS.jsonl"


def anotar(pack, operacion, costo_usd, **extra):
    """Apendiza una corrida al libro. Devuelve la linea escrita, o None si fallo.

    pack: el pack sobre el que se corrio (o None si la corrida es de catalogo).
    operacion: que se hizo ('consolidacion', 're-voz', 'extraccion'...).
    costo_usd: lo que costo esa corrida, ya calculado por quien llama.
    extra: lo que el que llama quiera dejar dicho (nodos, tokens, lote...).
    """
    linea = {
        "fecha": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "pack": pack,
        "operacion": operacion,
        "costo_usd": round(float(costo_usd), 4),
    }
    linea.update(extra)
    try:
        LIBRO.parent.mkdir(parents=True, exist_ok=True)
        with open(LIBRO, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(linea, ensure_ascii=False) + "\n")
    except OSError as e:
        # Anotar jamas tumba la corrida: el trabajo ya se hizo y ya se pago.
        print(f"  [AVISO] no se pudo anotar en el libro mayor: {e}")
        return None
    return linea


def pack_del_lote(ruta):
    """Deduce el pack de una ruta packs/<pack>/poda/<archivo>."""
    partes = Path(ruta).resolve().parts
    if "packs" in partes:
        i = partes.index("packs")
        if i + 1 < len(partes):
            return partes[i + 1]
    return None


def leer(desde=None):
    """Devuelve las corridas anotadas. desde: prefijo ISO ('2026-08')."""
    if not LIBRO.exists():
        return []
    filas = []
    for linea in LIBRO.read_text(encoding="utf-8").splitlines():
        linea = linea.strip()
        if not linea:
            continue
        fila = json.loads(linea)
        if desde and not str(fila.get("fecha", "")).startswith(desde):
            continue
        filas.append(fila)
    return filas


def total(filas=None):
    """La suma de TODO lo anotado, parciales incluidos. Se declara como tal."""
    filas = leer() if filas is None else filas
    return round(sum(float(f.get("costo_usd") or 0) for f in filas), 2)


def total_certificable(filas=None):
    """LA CIFRA QUE SE PUEDE DEFENDER: solo las corridas que se anotaron solas,
    sin las rescatadas del ciclo viejo. Es la que se lleva a un cierre.

    La distincion es el libro entero: un total que suma filas rescatadas suena
    exacto y no lo es. Un numero honesto con su limite declarado vale mas que
    uno redondo de memoria."""
    filas = leer() if filas is None else filas
    return round(sum(float(f.get("costo_usd") or 0) for f in filas if not f.get("parcial")), 2)


def main():
    filas = leer()
    if not filas:
        print("El libro esta vacio.")
        return
    por_pack = {}
    for f in filas:
        clave = (f.get("pack") or "(catalogo)", f.get("operacion"))
        por_pack[clave] = por_pack.get(clave, 0) + float(f.get("costo_usd") or 0)
    for (pack, op), c in sorted(por_pack.items()):
        print(f"  {pack:<16} {op:<16} ${c:.2f}")
    parciales = [f for f in filas if f.get("parcial")]
    print(f"\n  {len(filas)} corridas anotadas. TOTAL ${total(filas):.2f}")
    print(f"  CERTIFICABLE (sin las rescatadas): ${total_certificable(filas):.2f} "
          f"de {len(filas) - len(parciales)} corridas que se anotaron solas.")
    if parciales:
        print(f"  Las otras {len(parciales)} van marcadas parcial: rescatadas de "
              f"informes que se pisaban, y son la ULTIMA corrida de su script "
              f"sobre ese pack, no el total.")


if __name__ == "__main__":
    main()
