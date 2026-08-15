"""Vuelta 29: mide las costuras que los cortes de OP-F-04-WEI crearon dentro de
sus miembros receptores.

Encargo de la vuelta 29 (TAREA 1, punto 1), que nace de la omision de registro
adjudicada en el acta de la vuelta 28 (seccion 3, punto 2): el registro
"LA COLA TAMBIEN RECIBE LAS COSTURAS QUE UN REPARTO CREA" (docs/plan/08_VERIFICACION.md)
se escribio en la misma vuelta que ejecuto WEI, y las costuras de WEI no entraron.

Este script NO desteje y NO decide: MIDE. Por cada miembro receptor imprime los
pasos que tiene HOY y los que tenia ANTES del reparto (leidos del commit que el
invocante pase), para que la costura se declare con su medicion al lado.

Uso:
    python scripts/loop/vuelta29_costuras.py <commit_antes>
"""
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")

# Los cuatro miembros que recibieron bloque en OP-F-04-WEI, con el corte que los
# alcanzo. Se leen de docs/plan/01_FUENTES.md, seccion OP-F-04-WEI EJECUTADA EN
# PARTE, y de docs/loop/PLAN_V28_OPF04_WEI.json.
RECEPTORES = [
    ("fases_traccion_producto", "fit_problema_solucion", "pasos 4 a 6"),
    ("clasificacion_leads_abc", "sales_funnel_get_keep_grow", "pasos 5 a 9"),
    ("bullseye_framework", "plan_de_adquisicion_acquire", "pasos 8 a 12"),
    ("publicidad_offline_pruebas_locales", "earned_vs_paid_media", "pasos 5 a 8"),
    ("compromiso_linea_tiempo_cliente", "sales_funnel_get_keep_grow", "el paso 10"),
]


def hoy(nid):
    with open(os.path.join(NODOS, nid + ".json"), encoding="utf-8") as fh:
        return json.load(fh)


def antes(nid, commit):
    ruta = "dataset/nodos/%s.json" % nid
    crudo = subprocess.run(
        ["git", "show", "%s:%s" % (commit, ruta)],
        cwd=RAIZ, capture_output=True, check=True,
    ).stdout.decode("utf-8")
    return json.loads(crudo)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    commit = sys.argv[1]
    print("COMMIT ANTES DEL REPARTO: %s" % commit)
    print("MEDIDO HOY CONTRA: dataset/nodos/ del arbol de trabajo")
    print("=" * 78)
    for nid, donante, tramo in RECEPTORES:
        d_hoy = hoy(nid)
        d_ant = antes(nid, commit)
        p_hoy = d_hoy["pasos_accionables"]
        p_ant = d_ant["pasos_accionables"]
        print()
        print("MIEMBRO   : %s" % nid)
        print("DONANTE   : %s (%s)" % (donante, tramo))
        print("PASOS     : %d hoy, contra %d antes del reparto" % (len(p_hoy), len(p_ant)))
        print("FUENTE HOY: %s" % d_hoy.get("fuente"))
        print("-" * 78)
        print("  LOS QUE YA TENIA (los %d de antes):" % len(p_ant))
        for i, p in enumerate(p_ant, 1):
            print("    %2d. %s" % (i, p))
        print("  LOS QUE ENTRARON (%d):" % (len(p_hoy) - len(p_ant)))
        for i, p in enumerate(p_hoy[len(p_ant):], len(p_ant) + 1):
            print("    %2d. %s" % (i, p))
        print("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
