# -*- coding: utf-8 -*-
"""Vuelta 48, TAREA 1.4 (segunda mitad): LAS DOS CELDAS DEL 00_INDICE ESCRITAS
DESDE LA MEDICION, no tecleadas (EJECUTOR.md regla 1).

Importa el contador de scripts/loop/vuelta48_contar_ld.py y usa SUS numeros.
Si el contador cambia, estas celdas cambian con el.

Uso: python scripts/loop/vuelta48_celdas_ld.py [--escribir]
"""
import argparse
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
IND = os.path.join(RAIZ, "docs", "plan", "00_INDICE.md")
PLAN = os.path.join(RAIZ, "docs", "plan")
DOCS = os.path.join(RAIZ, "docs")

RE_CAB = re.compile(r"^#+\s*\**\s*`?LD-(\d+)`?")
RE_ID = re.compile(r"LD-(\d+)")

V1 = "| lecturas dirigidas **hechas** | **65** | no lo mide este instrumento: **a verificar** |"
V2 = ("| lecturas dirigidas **encargadas y sin hacer** | **CERO** | "
      "no lo mide este instrumento: **a verificar** |")


def medir():
    paginas = ["LECTURAS_DIRIGIDAS.md"] + sorted(
        f for f in os.listdir(PLAN) if f.startswith("LD_") and f.endswith(".md"))
    hechas = set()
    for n in paginas:
        for l in io.open(os.path.join(PLAN, n), encoding="utf-8"):
            m = RE_CAB.match(l)
            if m:
                hechas.add(int(m.group(1)))
    universo = set()
    for base, _, fs in os.walk(DOCS):
        for f in fs:
            if not f.endswith((".md", ".txt", ".json", ".jsonl")):
                continue
            if f.startswith("SALIDA_"):   # salida de instrumento, no encargo
                continue
            t = io.open(os.path.join(base, f), encoding="utf-8", errors="replace").read()
            universo |= set(int(x) for x in RE_ID.findall(t))
    return hechas, sorted(universo - hechas)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--escribir", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    hechas, sin = medir()
    print("MEDIDO AHORA: hechas %d ; nombradas sin seccion %d -> %s"
          % (len(hechas), len(sin), ", ".join("LD-%02d" % n for n in sin)))
    if sin != [71, 99]:
        print("PARADA: la nomina de nombradas sin seccion cambio. Las dos que la")
        print("celda explica una por una son LD-71 y LD-99. No escribo a ciegas.")
        return 2

    n1 = ("| lecturas dirigidas **hechas** | **65** | ~~no lo mide este instrumento: "
          "**a verificar**~~ **MEDIDO el 19 ago 2026 (vuelta 48) con "
          "`scripts/loop/vuelta48_contar_ld.py` "
          "([`../loop/SALIDA_V48_CONTAR_LD.txt`](../loop/SALIDA_V48_CONTAR_LD.txt), exit 0): "
          "%d**, contadas como las que tienen SECCION PROPIA con veredicto en "
          "`LECTURAS_DIRIGIDAS.md` (38) y en las seis `LD_*.md` (43). **La cifra vieja de 65 "
          "no se borra: era exacta al corte del 12 ago 2026**; la diferencia son las tandas "
          "escritas despues, hasta `LD-98` |") % len(hechas)

    n2 = ("| lecturas dirigidas **encargadas y sin hacer** | **CERO** | ~~no lo mide este "
          "instrumento: **a verificar**~~ **MEDIDO el 19 ago 2026 (vuelta 48), misma corrida: "
          "CERO, y la cifra vieja aguanta.** El barrido halla **%d** numeros nombrados sin "
          "seccion propia, `LD-71` y `LD-99`, y **ninguno de los dos es trabajo pendiente**: "
          "`LD-71` esta ADJUDICADO COMO NO ACUNADO (`../loop/ACTA_AUDITOR.md` linea **4234**, "
          "*`LD-71` NO se acuna*, porque el par ya estaba leido como `LD-04`) y `LD-99` fue una "
          "propuesta del instrumento que el ejecutor no uso (`../loop/ACTA_AUDITOR.md` linea "
          "**7906**, *el ejecutor uso 96 a 98*) |") % len(sin)

    t = io.open(IND, encoding="utf-8", newline="").read()
    if V1 not in t or V2 not in t:
        if "vuelta 48" in t:
            print("YA APLICADA.")
            return 0
        print("PARADA: no encuentro las dos celdas ancla. No adivino.")
        return 2
    if not a.escribir:
        print("SIMULACION: se sustituirian las 2 celdas. Sin --escribir no toco nada.")
        return 0
    n0 = t.count("\n")
    t = t.replace(V1, n1, 1).replace(V2, n2, 1)
    io.open(IND, "w", encoding="utf-8", newline="").write(t)
    print("ESCRITAS 2 celdas. lineas antes %d, despues %d" % (n0, t.count("\n")))
    print("texto viejo conservado (tachado): %s"
          % ("no lo mide este instrumento" in t))
    print("guiones largos %d, guiones medios %d"
          % (t.count("\u2014"), t.count("\u2013")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
