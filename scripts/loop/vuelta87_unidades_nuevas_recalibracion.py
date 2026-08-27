# -*- coding: utf-8 -*-
"""vuelta87_unidades_nuevas_recalibracion.py . TAREA 2.a de la vuelta 87.

POR QUE NACE (acta de la vuelta 86, seccion 4.2 y adjudicacion 5.3): el
reporte de la vuelta 86 escribio en prosa suelta "cosa que no ha pasado en
las TRES ultimas vueltas" sobre las unidades nuevas que cada recalibracion
podria abrir en la bolsa filtrada. La frase salio CIERTA (el auditor la
midio: V83->V84, V84->V85 y V85->V86 dan las tres CERO), pero se publico SIN
LA LINEA que la sostiene (EJECUTOR.md regla 1). El dato SI vive en fichero
(los docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V*.jsonl estan commiteados todos),
asi que la salida barata no es callar la frase: es tallarla.

QUE MIDE: dado el fichero de la bolsa filtrada de HOY y el de la vuelta
ANTERIOR (ambos con filas {"madre": ..., "hijo": ...} como minimo), cuenta
cuantos pares (madre, hijo) de la bolsa de HOY NO estaban en la bolsa
ANTERIOR. Si son pocos (10 o menos), los nombra uno por uno.

USO:
  python scripts/loop/vuelta87_unidades_nuevas_recalibracion.py <bolsa_hoy> <bolsa_anterior>

SALIDA: una linea "UNIDADES NUEVAS EN LA BOLSA DE HOY QUE NO ESTABAN EN LA
BOLSA ANTERIOR: N" y, si N <= 10, la lista de pares nombrados.

CASO OBLIGATORIO (vuelta 87): corrido sobre
docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V86.jsonl (hoy) contra
docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V85.jsonl (anterior) tiene que dar
CERO, que es lo que el auditor midio a mano en la vuelta 86
(docs/loop/_auditor_v86_nuevas_por_vuelta.txt).

CASO ROJO INVENTADO: corrido sobre una COPIA de una bolsa a la que se le
anadio una fila que la bolsa anterior no tenia, tiene que dar un numero
distinto de cero y nombrar esa fila. El caso rojo se corre SOLO sobre copias,
nunca sobre los ficheros reales.
"""
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]


def cargar_pares(ruta):
    filas = [json.loads(l) for l in Path(ruta).read_text(encoding="utf-8").splitlines() if l.strip()]
    return [(f["madre"], f["hijo"]) for f in filas], len(filas)


def unidades_nuevas(ruta_hoy, ruta_anterior):
    pares_hoy, n_hoy = cargar_pares(ruta_hoy)
    pares_ant, n_ant = cargar_pares(ruta_anterior)
    set_ant = set(pares_ant)
    nuevas = [p for p in pares_hoy if p not in set_ant]
    return nuevas, n_hoy, n_ant


def main():
    if len(sys.argv) != 3:
        raise SystemExit("USO: vuelta87_unidades_nuevas_recalibracion.py <bolsa_hoy> <bolsa_anterior>")
    ruta_hoy, ruta_anterior = sys.argv[1], sys.argv[2]
    nuevas, n_hoy, n_ant = unidades_nuevas(ruta_hoy, ruta_anterior)
    print("BOLSA DE HOY (%s): %d filas" % (ruta_hoy, n_hoy))
    print("BOLSA ANTERIOR (%s): %d filas" % (ruta_anterior, n_ant))
    print("UNIDADES NUEVAS EN LA BOLSA DE HOY QUE NO ESTABAN EN LA BOLSA ANTERIOR: %d" % len(nuevas))
    if 0 < len(nuevas) <= 10:
        for madre, hijo in nuevas:
            print("  %s -> %s" % (madre, hijo))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
