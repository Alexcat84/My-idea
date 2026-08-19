# -*- coding: utf-8 -*-
"""vuelta38_tabla_perdidas.py

IMPRIME la TABLA DE PERDIDAS de un plan sellado de fusion, en markdown, con las
tres clases de P.13 (VIAJA, VIVE DENTRO, YA NO APLICA) y el conteo al pie. NO
decide nada y NO escribe en ningun documento: imprime.

POR QUE EXISTE. Es el hermano de scripts/loop/vuelta33_tabla_mapa.py para la otra
tabla que una fusion publica. La regla es la misma (EJECUTOR.md regla 1, cuarto
renglon: LA TABLA SE IMPRIME, NO SE TECLEA) y el motivo tambien: las paradas de
credito de las vueltas 31 y 32 fueron por celdas tecleadas a mano en tablas de
prosa que ningun instrumento generaba. La tabla de perdidas de OP-D-02 se publico
en prosa y por eso no hizo falta; estas dos son de CATORCE y ONCE filas, y a esa
escala una celda a mano es una caida esperando.

LA CABECERA ES PROPIA A PROPOSITO: scripts/loop/verificar_mapas_destejido.py
reconoce las tablas de PARTICION por su cabecera "paso del resultado", y una tabla
de perdidas no es de particion (una pieza puede vivir dentro y no ir a ningun
destino). Con cabecera propia el verificador ni la mira, que es lo correcto.

USO:
  python scripts/loop/vuelta38_tabla_perdidas.py docs/loop/PLAN_V38_OPD04_TALLER.json
"""
import argparse
import json
import sys
from pathlib import Path

CABECERA = "| pieza | de que nodo | clase P.13 | a donde va | por que |"
SEPARADOR = "|---|---|:---:|---|---|"
ORDEN = {"VIAJA": 0, "VIVE DENTRO": 1, "YA NO APLICA": 2}


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("plan", help="ruta al plan sellado JSON")
    args = ap.parse_args()

    ruta = Path(args.plan)
    if not ruta.exists():
        print("NO EXISTE: %s" % args.plan)
        return 2
    d = json.loads(ruta.read_text(encoding="utf-8"))
    filas = d.get("tabla_perdidas_p13") or []
    if not filas:
        print("SIN TABLA DE PERDIDAS: %s" % args.plan)
        return 2

    desconocidas = [f["clase"] for f in filas if f["clase"] not in ORDEN]
    if desconocidas:
        print("CLASE FUERA DE P.13: %s" % sorted(set(desconocidas)))
        return 2

    print(CABECERA)
    print(SEPARADOR)
    for f in sorted(filas, key=lambda x: (ORDEN[x["clase"]], x["de"])):
        print("| %s | `%s` | **%s** | %s | %s |"
              % (f["pieza"], f["de"], f["clase"], f["destino"], f["motivo"]))
    print("")
    print("**%d piezas: %d `VIAJA`, %d `VIVE DENTRO`, %d `YA NO APLICA`.**"
          % (len(filas),
             sum(1 for f in filas if f["clase"] == "VIAJA"),
             sum(1 for f in filas if f["clase"] == "VIVE DENTRO"),
             sum(1 for f in filas if f["clase"] == "YA NO APLICA")))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
