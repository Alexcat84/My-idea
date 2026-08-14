"""VUELTA 17. Marca las 221 entradas viejas de tipo `acto` de
docs/plan/INVENTARIO.jsonl como SUPERADAS POR EL CORTE 3.388, cada una con el
puntero a su sucesora. Adjudicacion del discutible 1 de la vuelta 16
(docs/loop/ACTA_AUDITOR.md VUELTA 16 seccion 3, punto 2 de la parada archivada).

QUE HACE Y QUE NO HACE
  - NO borra ninguna linea, ningun campo ni ningun texto viejo.
  - NO toca las 335 entradas nuevas ni las 115 de los otros cinco tipos.
  - NO anade claves: las 221 conservan exactamente el mismo esquema que las 335.
  - Escribe el marcador al FRENTE de `estado`, conservando el texto viejo
    palabra por palabra detras, y el puntero a la sucesora al FINAL de `nota`.

CONTROLES QUE TIENE QUE PASAR ANTES DE ESCRIBIR (si alguno falla, no escribe):
  1. 671 filas, 556 actos, 221 con corte 2026-08-11 y 335 con corte 2026-08-13.
  2. cada uno de los 221 tiene EXACTAMENTE UNA sucesora por superset.
  3. ninguna de las 221 lleva ya el marcador (el script es idempotente por
     negativa: si ya esta marcado, para y no lo marca dos veces).

Uso:
  python scripts/loop/vuelta17_marcar_221_superadas.py            (simulacro)
  python scripts/loop/vuelta17_marcar_221_superadas.py --escribir (escribe)
"""

import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
INVENTARIO = os.path.join(RAIZ, "docs", "plan", "INVENTARIO.jsonl")

MARCA = "SUPERADA POR EL CORTE 3.388 (vuelta 17, 14 ago 2026)"
VIEJO = "2026-08-11"
NUEVO = "2026-08-13"


def main():
    escribir = "--escribir" in sys.argv

    filas = []
    with open(INVENTARIO, encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.strip()
            if linea:
                filas.append(json.loads(linea))

    actos = [o for o in filas if o.get("tipo") == "acto"]
    viejos = [o for o in actos if o.get("fecha_corte") == VIEJO]
    nuevos = [o for o in actos if o.get("fecha_corte") == NUEVO]

    print("CONTROL 1, materia prima:", len(filas), "filas |", len(actos), "actos |",
          len(viejos), "viejos |", len(nuevos), "nuevos")
    assert len(filas) == 671 and len(actos) == 556, "el archivo no es el esperado"
    assert len(viejos) == 221 and len(nuevos) == 335, "el reparto por corte no es el esperado"

    ya = [o for o in viejos if MARCA in o.get("estado", "")]
    print("CONTROL 3, viejos ya marcados:", len(ya))
    assert not ya, "ya estaban marcadas: el script no marca dos veces"

    # sucesion por superset de miembros
    indice = [(frozenset(n["miembros"]), n) for n in nuevos]
    sin_sucesora, multiples, cambian_nombre, crecen = [], [], [], []
    parejas = {}
    for viejo in viejos:
        conjunto = frozenset(viejo["miembros"])
        cands = [n for cj, n in indice if conjunto <= cj]
        if len(cands) == 0:
            sin_sucesora.append(viejo["nombre"])
            continue
        if len(cands) > 1:
            multiples.append(viejo["nombre"])
        suc = cands[0]
        parejas[id(viejo)] = suc
        if suc["nombre"] != viejo["nombre"]:
            cambian_nombre.append((viejo["nombre"], suc["nombre"]))
        if len(suc["miembros"]) != len(viejo["miembros"]):
            crecen.append((viejo["nombre"], len(viejo["miembros"]), len(suc["miembros"])))

    print("CONTROL 2, sucesion: sin sucesora", len(sin_sucesora), sin_sucesora,
          "| con mas de una", len(multiples), multiples)
    print("  sucesoras que cambian de nombre:", len(cambian_nombre), cambian_nombre)
    print("  sucesoras de distinto tamano:", len(crecen), crecen)
    assert not sin_sucesora and not multiples, "la sucesion no es uno a uno"

    # el puntero necesita mas que el nombre si el nombre se repite entre cortes
    nombres_nuevos = [n["nombre"] for n in nuevos]
    print("  nombres distintos entre las 335 nuevas:", len(set(nombres_nuevos)), "de", len(nombres_nuevos))

    tocadas = 0
    for viejo in viejos:
        suc = parejas[id(viejo)]
        viejo["estado"] = (
            MARCA + ". El texto viejo de este campo, sin tocar: " + viejo["estado"]
        )
        viejo["nota"] = viejo["nota"] + (
            " " + MARCA + ", adjudicacion del discutible 1 de la vuelta 16. NADA SE BORRA: esta linea"
            " sigue entera y su fecha_corte sigue siendo " + VIEJO + ", el corte 2.117."
            " PUNTERO A SU SUCESORA VIGENTE: la entrada de tipo acto con nombre \""
            + suc["nombre"] + "\" y fecha_corte " + NUEVO + " (el corte 3.388), de "
            + str(len(suc["miembros"])) + " miembros."
            " PARA CONTESTAR SI UN NODO REPITE HOY SE LEE LA SUCESORA, NO ESTA:"
            " esta describe el catalogo a 2.117 pares de 3.388 leidos."
        )
        tocadas += 1

    print("MARCADAS:", tocadas)

    if not escribir:
        print("SIMULACRO: no se escribio nada. Vuelve a correr con --escribir.")
        return

    with open(INVENTARIO, "w", encoding="utf-8") as fh:
        for o in filas:
            fh.write(json.dumps(o, ensure_ascii=False) + "\n")
    print("ESCRITO en", INVENTARIO)


if __name__ == "__main__":
    main()
