# -*- coding: utf-8 -*-
"""verificar_mapas_destejido.py

Nace de la parada de credito de la vuelta 32 (docs/loop/ACTA_AUDITOR.md): dos
tandas seguidas cayeron por una celda tecleada a mano en una tabla de prosa de
docs/plan/ que ningun instrumento validaba (el nombre "investigar" en la
vuelta 31; el origen 16 en el grupo equivocado en la vuelta 32). Las dos son
la misma especie. Este instrumento la cierra para las tablas de mapa de
movimiento de docs/plan/02_DESTEJIDOS.md, con dos varas:

1. TODO NUMERO DE ORIGEN CITADO EN EL MOTIVO DE UNA FILA TIENE QUE
   PERTENECER AL GRUPO DE ORIGENES DE ESA MISMA FILA.
   Ejemplar que lo trajo: la fila del paso 6 de OP-D-01 (origenes 8, 14, 17,
   22) cita en su motivo "los pasos 14 y 16 traen la cadencia", y el 16 vive
   en el grupo de la fila del paso 2 (2, 6, 11, 15, 16, 19). Las dos filas no
   pueden ser verdad a la vez.

2. DONDE EXISTE EL PLAN SELLADO JSON DE LA MISMA OPERACION, LA PARTICION DE
   LA TABLA (origenes por fila) TIENE QUE SER IGUAL, CELDA A CELDA, A LA
   PARTICION DEL JSON (nodos[].grupos_pasos[].origenes). Las dos fuentes
   describen el mismo reparto; si difieren, una de las dos esta mal escrita.

USO:
  python scripts/loop/verificar_mapas_destejido.py
  python scripts/loop/verificar_mapas_destejido.py --md RUTA.md
  python scripts/loop/verificar_mapas_destejido.py --json docs/loop/PLAN_V32_OPD01_EMBLEMA.json

Repetible: --json se puede pasar varias veces, una por plan sellado.
SALIDA: cada discrepancia nombra la TABLA, la FILA (el paso destino), su
LINEA en el archivo, y el numero exacto que la causa. Exit 0 sin
discrepancias, exit 1 con discrepancias.

LIMITE DECLARADO, para que nadie lo use como prueba de lo que no mide: el
barrido del motivo por numeros citados es LEXICO (busca "paso" o "pasos"
seguido de digitos hasta el primer separador que no sea numero, coma, "y" o
espacio), no semantico. Si un motivo cita el paso de OTRO nodo (por ejemplo
"el paso 3 del donante") con un numero que por coincidencia SI esta en el
grupo local, el chequeo pasa aunque el numero no se refiera a un origen de
esta fila. Es una guarda mecanica contra el error medido dos veces (una
celda que contradice su propio motivo), no un lector de espanol.
"""
import argparse
import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent
DESTEJIDOS_PATH = BASE / "docs" / "plan" / "02_DESTEJIDOS.md"

RE_TABLA_HEADER = re.compile(
    r"\|\s*paso del resultado\s*\|\s*de qu[eé] or[ií]genes sale\s*\|", re.IGNORECASE
)
RE_FILA = re.compile(r"^\|\s*\*{0,2}(\d+)\*{0,2}\s*\|\s*([^|]+?)\s*\|\s*(.+?)\s*\|\s*$")
RE_NUM = re.compile(r"\d+")
RE_PASO_CITA = re.compile(r"\bpasos?\b([^.]*)", re.IGNORECASE)
RE_FRAGMENTO_NUMS = re.compile(r"^([\d,\sy]+)")


def extraer_tablas(texto):
    """Devuelve una lista de tablas de mapa de movimiento halladas en el texto.

    Cada tabla es {"titulo", "linea_header", "filas": [...]}
    Cada fila es {"paso", "origenes" (lista int), "motivo" (texto), "linea"}.
    """
    lineas = texto.splitlines()
    tablas = []
    titulo_actual = "(sin titulo de seccion)"
    i = 0
    while i < len(lineas):
        linea = lineas[i]
        if linea.lstrip().startswith("#"):
            titulo_actual = linea.lstrip("#").strip()
        if RE_TABLA_HEADER.search(linea):
            filas = []
            j = i + 2  # salta la fila de header y la de separador ---
            while j < len(lineas) and lineas[j].strip().startswith("|"):
                m = RE_FILA.match(lineas[j])
                if m:
                    paso = int(m.group(1))
                    origenes = [int(x) for x in RE_NUM.findall(m.group(2))]
                    motivo = m.group(3)
                    filas.append(
                        {"paso": paso, "origenes": origenes, "motivo": motivo, "linea": j + 1}
                    )
                j += 1
            tablas.append({"titulo": titulo_actual, "linea_header": i + 1, "filas": filas})
            i = j
            continue
        i += 1
    return tablas


def numeros_citados_en_motivo(motivo):
    """Numeros que el motivo cita junto a 'paso'/'pasos', hasta el primer
    separador que no sea digito, coma, 'y' o espacio."""
    numeros = set()
    for m in RE_PASO_CITA.finditer(motivo):
        fragmento = m.group(1).strip()
        m2 = RE_FRAGMENTO_NUMS.match(fragmento)
        if m2:
            numeros.update(int(n) for n in RE_NUM.findall(m2.group(1)))
    return numeros


def verificar_motivo_contra_grupo(tabla):
    discrepancias = []
    for fila in tabla["filas"]:
        origenes = set(fila["origenes"])
        citados = numeros_citados_en_motivo(fila["motivo"])
        for n in sorted(citados - origenes):
            discrepancias.append(
                {
                    "tipo": "MOTIVO AJENO",
                    "tabla": tabla["titulo"],
                    "fila_paso": fila["paso"],
                    "linea": fila["linea"],
                    "numero_ajeno": n,
                    "origenes_de_la_fila": sorted(origenes),
                }
            )
    return discrepancias


def cargar_grupos_json(ruta_json):
    d = json.loads(Path(ruta_json).read_text(encoding="utf-8"))
    grupos = []
    for nodo in d.get("nodos", []):
        for g in nodo.get("grupos_pasos", []):
            grupos.append(sorted(g["origenes"]))
    return grupos


def verificar_tabla_contra_json(tabla, ruta_json):
    grupos_md = [sorted(f["origenes"]) for f in tabla["filas"]]
    grupos_json = cargar_grupos_json(ruta_json)
    if grupos_md == grupos_json:
        return []
    return [
        {
            "tipo": "PARTICION DISTINTA",
            "tabla": tabla["titulo"],
            "json": str(ruta_json),
            "particion_md": grupos_md,
            "particion_json": grupos_json,
        }
    ]


def imprimir(d):
    if d["tipo"] == "MOTIVO AJENO":
        print(
            f"[MOTIVO AJENO] tabla '{d['tabla']}', fila del paso {d['fila_paso']} "
            f"(linea {d['linea']}): el motivo cita el origen {d['numero_ajeno']}, "
            f"que NO esta en el grupo de esta fila {d['origenes_de_la_fila']}."
        )
    else:
        print(
            f"[PARTICION DISTINTA] tabla '{d['tabla']}' contra {d['json']}: "
            f"tabla={d['particion_md']} json={d['particion_json']}"
        )


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--md", default=str(DESTEJIDOS_PATH), help="ruta al markdown con las tablas de mapa")
    ap.add_argument(
        "--json", action="append", default=[], dest="jsons",
        help="plan sellado a comparar celda a celda contra las tablas (repetible)",
    )
    args = ap.parse_args()

    texto = Path(args.md).read_text(encoding="utf-8")
    tablas = extraer_tablas(texto)

    if not tablas:
        print(f"AVISO: cero tablas de mapa de movimiento encontradas en {args.md}")

    todas = []
    for tabla in tablas:
        todas.extend(verificar_motivo_contra_grupo(tabla))
        for ruta_json in args.jsons:
            todas.extend(verificar_tabla_contra_json(tabla, ruta_json))

    for d in todas:
        imprimir(d)

    total_filas = sum(len(t["filas"]) for t in tablas)
    print(f"\n{len(tablas)} tabla(s), {total_filas} fila(s), {len(todas)} discrepancia(s).")
    if todas:
        print("VERIFICADOR DE MAPAS DE DESTEJIDO: FALLIDO")
        return 1
    print("VERIFICADOR DE MAPAS DE DESTEJIDO: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
