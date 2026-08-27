# -*- coding: utf-8 -*-
"""vuelta95_tarea3a_cribado_cita_de_linea.py . VUELTA 95, TAREA 3(a): RECONSTRUYE
CON CODIGO PROPIO el cribado de "cita de linea" que el acta de la vuelta 94
publico (docs/loop/ACTA_AUDITOR.md lineas 33309 a 33336,
docs/loop/_auditor_v94_cita_de_linea.txt), sobre las 84 filas vigentes de
docs/plan/OP_E_07_DIRECCION_V94.jsonl. EJECUTOR.md regla 2, "EL INSTRUMENTO
MANDA": esta corrida es la fuente; el acta se cita como CONTRASTE.

LA PREGUNTA: para cada par, su RAZON completa (docs/INTRA_DOMINIO_VEREDICTOS.jsonl,
cruzada por puesto == puesto_intra) cita un PASO NUMERADO o una LINEA EXPLICITA
(grupo A), o al menos trae FORMA DE INDICE sin cita de linea (grupo B), o
NINGUNA de las dos (grupo C)?

PATRONES, los mismos que el acta describe en prosa (linea 33313-33315),
escritos aqui como regex propia y no copiada del fichero del auditor:
  GRUPO A: "paso N", "en una/dos/tres/media linea(s)", "dice N lineas",
  "primera/segunda/tercera linea", "una de sus lineas", "entre sus pasos".
  GRUPO B (solo si A no caso): "es el indice", "enumera", "enuncia".
  GRUPO C: ninguno de los dos.
Sin distincion de acentos ("linea" o "línea") ni de mayusculas.

MECANICA DE ROJO: si una fila de OP_E_07_DIRECCION_V94.jsonl no tiene su
`puesto_intra` correspondiente en INTRA_DOMINIO_VEREDICTOS.jsonl, o si el total
de filas clasificadas no es 84, ROJO y no se imprime nada.

USO:
  python scripts/loop/vuelta95_tarea3a_cribado_cita_de_linea.py
"""
import io
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PLAN = os.path.join(RAIZ, "docs", "plan")
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
ENTRADA = os.path.join(PLAN, "OP_E_07_DIRECCION_V94.jsonl")

PATRONES_A = [
    re.compile(r"\bpaso\s+\d+\b", re.IGNORECASE),
    re.compile(r"\ben\s+(una|dos|tres|media)\s+l[ií]neas?\b", re.IGNORECASE),
    # "dice N lineas": N puede ser digito o numero escrito (el 960 dice "tres lineas").
    re.compile(r"\bdice\s+(\d+|un|una|dos|tres|cuatro|cinco|seis|siete|ocho)\s+l[ií]neas?\b", re.IGNORECASE),
    re.compile(r"\b(primera|segunda|tercera)\s+l[ií]nea\b", re.IGNORECASE),
    re.compile(r"\buna\s+de\s+sus\s+l[ií]neas\b", re.IGNORECASE),
    re.compile(r"\bentre\s+sus\s+pasos\b", re.IGNORECASE),
]
PATRONES_B = [
    re.compile(r"\bes\s+el\s+[ií]ndice\b", re.IGNORECASE),
    # prefijo, no palabra exacta: cubre conjugaciones (enumera, enumeran,
    # enumerar) y (enuncia, enuncian, enunciar), como el 1778 ("se enuncian").
    re.compile(r"\benumera\w*\b", re.IGNORECASE),
    re.compile(r"\benuncia\w*\b", re.IGNORECASE),
]


def clasifica_razon(razon):
    """LA UNICA PIEZA DE JUICIO: dado el texto de la razon, devuelve 'A', 'B'
    o 'C'. Grupo A si CUALQUIER patron de PATRONES_A casa; si no, grupo B si
    CUALQUIER patron de PATRONES_B casa; si no, grupo C."""
    if any(p.search(razon) for p in PATRONES_A):
        return "A"
    if any(p.search(razon) for p in PATRONES_B):
        return "B"
    return "C"


def cargar_jsonl(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def main():
    filas = cargar_jsonl(ENTRADA)
    veredictos = {int(v["puesto_intra"]): v for v in cargar_jsonl(VEREDICTOS)}

    fallos = []
    grupos = {"A": [], "B": [], "C": []}
    for fila in filas:
        puesto = fila["puesto"]
        v = veredictos.get(puesto)
        if v is None:
            fallos.append("puesto %s no tiene puesto_intra en %s" % (puesto, VEREDICTOS))
            continue
        clase = clasifica_razon(v["razon"])
        grupos[clase].append(puesto)

    if fallos:
        print("ROJO, %d cosa(s) no se pudieron leer y NO SE TALLA NADA:" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1

    total = len(grupos["A"]) + len(grupos["B"]) + len(grupos["C"])
    if total != 84:
        print("ROJO: el total clasificado es %d, no 84 (filas vigentes de %s). NO SE TALLA NADA."
              % (total, os.path.basename(ENTRADA)))
        return 1

    print("=" * 90)
    print("CRIBADO DE CITA DE LINEA, RECONSTRUIDO CON CODIGO PROPIO (vuelta 95, TAREA 3.a)")
    print("Fuente: %s (%d filas), razones de %s" % (os.path.basename(ENTRADA), len(filas), os.path.basename(VEREDICTOS)))
    print("=" * 90)
    print()
    print("| grupo | cuantas |")
    print("|---|---:|")
    print("| A, citan paso numerado o linea explicita | %d |" % len(grupos["A"]))
    print("| B, no citan linea pero traen forma de indice | %d |" % len(grupos["B"]))
    print("| C, ni una ni otra | %d |" % len(grupos["C"]))
    print()
    print("ENUMERACION grupo B (%d): %s" % (len(grupos["B"]), ", ".join(str(p) for p in sorted(grupos["B"]))))
    print("ENUMERACION grupo C (%d): %s" % (len(grupos["C"]), ", ".join(str(p) for p in sorted(grupos["C"]))))
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
