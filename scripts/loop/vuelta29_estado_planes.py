"""Vuelta 29: mide que cortes de los planes sellados YA estan en el arbol y
cuales siguen pendientes. No escribe nada.

El encargo de la vuelta 29 cita "los cinco bloques nodo propio de OP-F-03
(PLAN_V27_OPF03_SISTEMAS.json y lo que falte de PLAN_V27_OPF03_CADENA.json)".
Este script mide, en vez de suponer: por cada corte de cada plan dice si el
origen todavia tiene los pasos que el plan espera sacar (PENDIENTE) o si ya no
los tiene (APLICADO), y cuenta los destinos de tipo nodo_propio.

Uso:
    python scripts/loop/vuelta29_estado_planes.py <plan.json> [<plan.json> ...]
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")


def nodo(nid):
    ruta = os.path.join(NODOS, nid + ".json")
    if not os.path.exists(ruta):
        return None
    with open(ruta, encoding="utf-8") as fh:
        return json.load(fh)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    for plan_path in sys.argv[1:]:
        plan = json.load(open(plan_path, encoding="utf-8"))
        cortes = plan.get("cortes") or plan.get("mudanzas") or []
        print("=" * 78)
        print("PLAN     : %s" % os.path.basename(plan_path))
        print("OPERACION: %s" % plan["operacion"])
        print("CORTES   : %d" % len(cortes))
        propios = 0
        pendientes = 0
        for c in cortes:
            origen = c.get("origen") or c.get("desde")
            dest = c["destino"]
            tipo = dest["tipo"]
            destino_id = dest.get("nodo") or (dest.get("nuevo") or {}).get("node_id")
            if tipo == "nodo_propio":
                propios += 1
            d = nodo(origen)
            if d is None:
                estado = "ORIGEN AUSENTE"
            else:
                hoy = len(d["pasos_accionables"])
                esperados = c.get("pasos_totales")
                salen = c["pasos_que_salen"]
                if esperados is None:
                    esperados = c.get("pasos_totales") or hoy
                if hoy == esperados:
                    estado = "PENDIENTE (origen con %d pasos, los %d esperados)" % (hoy, esperados)
                    pendientes += 1
                elif hoy == esperados - len(salen):
                    estado = "APLICADO   (origen con %d pasos, %d menos los %d que salieron)" % (
                        hoy, esperados, len(salen))
                else:
                    estado = "NO CUADRA  (origen con %d pasos; el plan esperaba %d y saca %d)" % (
                        hoy, esperados, len(salen))
            existe_destino = "existe" if (destino_id and nodo(destino_id)) else "NO EXISTE"
            print("  %-14s %-42s -> %-12s %-46s [%s]" % (
                "", origen, tipo, (destino_id or "?") + " (" + existe_destino + ")", estado))
        print("  RESUMEN: %d cortes, %d con destino nodo_propio, %d pendientes" % (
            len(cortes), propios, pendientes))
    return 0


if __name__ == "__main__":
    sys.exit(main())
