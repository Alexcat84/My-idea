# Ciega del auditor, vuelta 62: imprime los pasos y condiciones de los DOS
# miembros de cada acto elegido, leidos del arbol de APERTURA (d9fd6a54),
# SIN tocar los planes sellados. La adjudicacion se hace mirando esto y
# SOLO DESPUES se destapa el motivo del plan.
import io, json, subprocess, sys

sys.stdout.reconfigure(encoding="utf-8")

raw = subprocess.run(
    ["git", "show", "d9fd6a54:dataset/metadata/master_graph.json"],
    capture_output=True).stdout
nodos = json.loads(raw.decode("utf-8"))["nodos"]

ACTOS = {
    1: ("administracion_sin_miedo", "gestion_miedo_reportes"),
    2: ("contacto_con_el_cliente", "contacto_con_el_cliente_2"),
    5: ("gobierno_corporativo_juntas_directivas", "planificacion_gobierno_organizaciones_familiares"),
    8: ("revision_progreso", "revision_progreso_breakthrough"),
    9: ("gestion_estrategica_de_calidad_sqm", "rol_tactico_estrategico_oficina"),
    12: ("cinco_suposiciones_erroneas_calidad", "concepto_supuestos_erroneos_sobre_calidad"),
    18: ("control_del_proceso_del_proveedor", "planificacion_tecnologica_conjunta"),
    20: ("getting_started_maintenance", "mantenimiento_sistema_cui"),
}

for num in sorted(ACTOS):
    a, b = ACTOS[num]
    print("=" * 90)
    print("ACTO %d" % num)
    for nid in (a, b):
        n = nodos[nid]
        print("-" * 90)
        print("nodo: %s" % nid)
        print("titulo: %s" % n.get("titulo_concepto"))
        print("siguientes: %d | previos: %d" % (len(n.get("nodos_siguientes", [])),
                                                len(n.get("nodos_previos", []))))
        print("condiciones (%d):" % len(n.get("condiciones_activacion", [])))
        for c in n.get("condiciones_activacion", []):
            print("   * %s" % c)
        print("pasos (%d):" % len(n.get("pasos_accionables", [])))
        for p in n.get("pasos_accionables", []):
            print("   %s" % p)
    print()
