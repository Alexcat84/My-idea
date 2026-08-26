# -*- coding: utf-8 -*-
"""tramo_al_cierre.py . LO QUE QUEDA DE UN TRAMO, MEDIDO SOBRE EL GRAFO DEL DIA.

NOMBRE ESTABLE Y SIN NUMERO DE VUELTA NI DE TRAMO, por la misma vara del acta 58
(pregunta 4) con la que nacieron tallar_cabecera_reporte.py, dossier_del_tramo.py
y generar_plan_del_lote.py: el tramo entra por --tramo, la vuelta por --vuelta y
el reparto por lotes por --lotes. Este fichero no se clona cada vuelta.

POR QUE NACE (26 ago 2026, vuelta 70). La tabla de LO QUE QUEDA DEL TRAMO se
venia publicando desde una sonda escrita dentro de la vuelta y no quedaba en el
arbol: buscada hoy con grep sobre scripts/, la cabecera EL TRAMO UNICO DE OP-U-02
AL CIERRE no aparece en ningun instrumento. Una cifra que se publica en cada
vuelta y cuyo instrumento no queda en el arbol no se puede re-correr contra otro
corte, que es exactamente lo que la regla 2 del EJECUTOR pide poder hacer, y es
el mismo motivo por el que nacio vuelta51_censo_colisiones.py.

QUE MIDE, Y QUE NO. MIDE sobre dataset/nodos: cuantos miembros de cada acto
siguen VIVOS, cual es el superviviente cuando el acto esta fundido, y cuantos
actos y nodos quedan en pie. NO decide nada: el reparto por lotes y la lista de
los DECLARADOS Y NO FUNDIDOS son HISTORIA y entran por argumento, porque no se
pueden medir sobre el grafo (un acto declarado tiene todos sus miembros vivos,
igual que uno sin tocar). Cada uno se imprime con la etiqueta de que entro por
argumento, para que nadie lo lea como medicion.

UN ACTO ESTA FUNDIDO si le queda UN solo miembro vivo o ninguno; esta ABIERTO si
le quedan DOS o mas. Esa es toda la aritmetica y se dice entera.

DE SOLO LECTURA. No escribe nada.

Uso:
  python scripts/loop/tramo_al_cierre.py --tramo docs/loop/TRAMO_UNICO_OPU02_V64.jsonl
      --vuelta 70 --lotes "A:65,B:66,C:67,D:68,E:69,F:70"
      --declarados 1,5,10,11,12,13,14,15,17,20,21,23,24,27
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")


def vivo(nid):
    ruta = os.path.join(NODOS, nid + ".json")
    if not os.path.exists(ruta):
        return None
    d = json.load(io.open(ruta, encoding="utf-8"))
    return not bool(d.get("deprecado") or d.get("deprecated"))


def cuenta_pasos(nid):
    d = json.load(io.open(os.path.join(NODOS, nid + ".json"), encoding="utf-8"))
    return len(d.get("pasos_accionables") or []), len(d.get("condiciones_activacion") or [])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tramo", required=True)
    ap.add_argument("--vuelta", type=int, required=True)
    ap.add_argument("--declarados", default="",
                    help="ordenes de los actos DECLARADOS Y NO FUNDIDOS. ENTRA POR "
                         "ARGUMENTO porque no se puede medir: un declarado tiene todos "
                         "sus miembros vivos igual que uno sin tocar")
    ap.add_argument("--clave-orden", default="orden_universo")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    ruta = os.path.join(RAIZ, a.tramo.replace("/", os.sep))
    filas = [json.loads(l) for l in io.open(ruta, encoding="utf-8") if l.strip()]
    declarados = set(int(x) for x in a.declarados.split(",") if x.strip())

    print("=" * 78)
    print("LO QUE QUEDA DEL TRAMO AL CIERRE DE LA VUELTA %d" % a.vuelta)
    print("  fichero fijado : %s" % a.tramo)
    print("  MEDIDO sobre dataset/nodos en esta corrida; el reparto por lotes y la")
    print("  lista de DECLARADOS son HISTORIA y entran por argumento, no se miden.")
    print("=" * 78)
    print()

    abiertos, fundidos, nodos_abiertos = [], [], 0
    detalle = []
    for r in filas:
        o = int(r[a.clave_orden])
        M = r["miembros"]
        vivos = [m for m in M if vivo(m)]
        if len(vivos) <= 1:
            fundidos.append(o)
            detalle.append((o, "FUNDIDO", vivos[0] if vivos else "", len(M), len(vivos),
                            r.get("duenos_cualquier_operacion") or []))
        else:
            abiertos.append(o)
            nodos_abiertos += len(vivos)
            detalle.append((o, "DECLARADO" if o in declarados else "ABIERTO", "", len(M), len(vivos),
                            r.get("duenos_cualquier_operacion") or []))

    print("  actos del tramo (filas del fichero fijado) : %d" % len(filas))
    print("  actos FUNDIDOS, medido (1 o 0 miembros vivos): %d" % len(fundidos))
    print("     %s" % sorted(fundidos))
    print("  actos con DOS O MAS miembros vivos           : %d" % len(abiertos))
    print("  de esos, DECLARADOS Y NO FUNDIDOS (argumento): %d" % len(declarados & set(abiertos)))
    print("     %s" % sorted(declarados & set(abiertos)))
    quedan = [o for o in abiertos if o not in declarados]
    nodos_quedan = sum(d[4] for d in detalle if d[0] in quedan)
    print()
    print("  QUEDAN SIN DESTINO: %d actos y %d nodos" % (len(quedan), nodos_quedan))
    print("     %s" % quedan)
    con_dueno = [d[0] for d in detalle if d[0] in quedan and d[5]]
    print("  de los que quedan, CON DUENO medido: %d %s" % (len(con_dueno), con_dueno))
    for o in con_dueno:
        d = [x for x in detalle if x[0] == o][0]
        print("     acto %-3d duenos_cualquier_operacion = %s" % (o, d[5]))
    if quedan:
        print("  el siguiente del prefijo: acto %d" % quedan[0])
    print()
    print("  LOS ACTOS FUNDIDOS, CON SU SUPERVIVIENTE VIVO Y SU TAMANO DE HOY:")
    for o, estado, sup, n, nv, du in detalle:
        if estado != "FUNDIDO" or not sup:
            continue
        p, c = cuenta_pasos(sup)
        print("     acto %-3d %-52s pasos %-3d condiciones %d" % (o, sup, p, c))
    print()
    print("  LOS QUE QUEDAN, UNO A UNO:")
    for o, estado, sup, n, nv, du in detalle:
        if o not in quedan:
            continue
        print("     acto %-3d miembros %d, vivos %d, duenos %s" % (o, n, nv, du or "[]"))
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    sys.exit(main())
