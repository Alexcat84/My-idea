# -*- coding: utf-8 -*-
r"""vuelta96_tarea2_mesa_de_formula.py . VUELTA 96, TAREA 2: LA MESA DE FORMULA
de los pares 886, 890 y 947, tal como la decision 2 del fundador la escribe
(docs/loop/paradas/2026-08-27-racha-parentesis-DECISION.md).

QUE IMPRIME. LOS CINCO EJEMPLARES DE LA FORMULA, ENTEROS Y JUNTOS: el 1083
(CONFIRMADO), el 1009 (CAIDO, ya salio) y los tres vivos (886, 890, 947). De
cada uno: su puesto, su dominio, sus dos nodos RESUELTOS por el resolutor (P.1),
su razon COMPLETA sin recortar, y los `pasos_accionables` ENTEROS de los dos
nodos. Nada se resume: la mesa se sienta sobre el texto entero o no se sienta.

POR QUE LA MESA NO SE PUEDE EVITAR (acta 95, seccion 4.2, linea 33795): la
formula "trae un procedimiento que X no tiene" produjo el 1083 CONFIRMADO y el
1009 CAIDO. La MISMA formula, los dos resultados. Y el 886 es el hermano vivo
del 1009: mismo nodo hijo `fit_problema_solucion`, misma formula literal, madre
casi gemela.

EL RESOLUTOR (P.1, BANCO_DEL_PLAN.md linea 11): todo id que este instrumento
toque se resuelve antes de cruzarse, con la semantica de resolverId del motor
(camina la cadena de alias hasta el id final, sin ciclar). Se dice aqui porque
P.1 obliga a decir SIEMPRE si se resolvio.

MECANICA DE ROJO, y no se imprime nada si salta: (i) un puesto de los cinco sin
veredicto en docs/INTRA_DOMINIO_VEREDICTOS.jsonl; (ii) un nodo del par que, ya
resuelto, no existe en el grafo; (iii) un nodo sin `pasos_accionables`.
Probada por mutacion en scripts/loop/vuelta96_tarea2_prueba_mutacion.py.

USO:
  python scripts/loop/vuelta96_tarea2_mesa_de_formula.py
"""
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
ENTRADA = os.path.join(RAIZ, "docs", "plan", "OP_E_07_DIRECCION_V94.jsonl")

# Los cinco ejemplares de la formula. El estado NO es juicio de este
# instrumento: sale del expediente y se cita con su sitio.
LOS_CINCO = [
    (1083, "CONFIRMADO", "acta 95 seccion 3.3; su razon dice 'que LA MADRE no tiene'"),
    (1009, "CAIDO, YA SALIO", "docs/PENDIENTES.md, seccion de la vuelta 93"),
    (886, "VIVO, a mesa", "acta 95 seccion 4.2, hermano del 1009"),
    (890, "VIVO, a mesa", "acta 95 seccion 4.2"),
    (947, "VIVO, a mesa", "acta 95 seccion 4.2"),
]


def cargar_jsonl(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def construir_resolutor(nodos):
    """P.1: la semantica de resolverId del motor, camina la cadena de alias
    hasta el id final, sin ciclar."""
    alias = {a: k for k, v in nodos.items() for a in (v.get("ids_alias") or [])}

    def res(x):
        visto = set()
        while x in alias and x not in visto:
            visto.add(x)
            x = alias[x]
        return x
    return res


def reunir():
    nodos = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    res = construir_resolutor(nodos)
    ver = {int(v["puesto_intra"]): v for v in cargar_jsonl(VEREDICTOS)}
    direccion = {f["puesto"]: f for f in cargar_jsonl(ENTRADA)}

    fallos = []
    fichas = []
    for puesto, estado, sitio in LOS_CINCO:
        v = ver.get(puesto)
        if v is None:
            fallos.append("el puesto %s no tiene veredicto en INTRA_DOMINIO_VEREDICTOS.jsonl" % puesto)
            continue
        d = direccion.get(puesto)
        crudos = (v["nodo_a"], v["nodo_b"])
        resueltos = tuple(res(x) for x in crudos)
        for crudo, resuelto in zip(crudos, resueltos):
            if resuelto not in nodos:
                fallos.append("el puesto %s trae el nodo %r (resuelto %r) que no existe en el grafo"
                              % (puesto, crudo, resuelto))
                continue
            if not (nodos[resuelto].get("pasos_accionables") or []):
                fallos.append("el nodo %r (puesto %s) no tiene pasos_accionables" % (resuelto, puesto))
        fichas.append({
            "puesto": puesto, "estado": estado, "sitio": sitio,
            "dominio": v.get("dominio"), "clase": v.get("clase"),
            "crudos": crudos, "resueltos": resueltos,
            "razon": v["razon"],
            "madre_registrada": d["madre"] if d else None,
            "hijo_registrado": d["hijo"] if d else None,
            "nodos": nodos,
        })
    return fichas, fallos


def main():
    fichas, fallos = reunir()
    if fallos:
        print("ROJO, %d cosa(s) no cuadran y NO SE IMPRIME NADA:" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1

    print("=" * 90)
    print("LA MESA DE FORMULA: LOS CINCO EJEMPLARES, ENTEROS Y JUNTOS (vuelta 96, TAREA 2)")
    print("Ids RESUELTOS por el resolutor antes de cruzarse (P.1). Nada recortado.")
    print("=" * 90)

    for f in fichas:
        nodos = f["nodos"]
        print()
        print("#" * 90)
        print("PUESTO %s . %s . dominio %s . clase %s" % (f["puesto"], f["estado"], f["dominio"], f["clase"]))
        print("  sitio del estado: %s" % f["sitio"])
        print("  nodos crudos:    %s  |  %s" % f["crudos"])
        print("  nodos RESUELTOS: %s  |  %s" % f["resueltos"])
        if f["madre_registrada"]:
            print("  direccion registrada en OP_E_07_DIRECCION_V94.jsonl: madre=%s  hijo=%s"
                  % (f["madre_registrada"], f["hijo_registrado"]))
        else:
            print("  direccion registrada en OP_E_07_DIRECCION_V94.jsonl: NO ESTA (el par ya salio de la bolsa)")
        print("#" * 90)
        print()
        print("LA RAZON, ENTERA:")
        print("  " + f["razon"])
        print()
        for etiqueta, nid in zip(("NODO A", "NODO B"), f["resueltos"]):
            n = nodos[nid]
            pasos = n.get("pasos_accionables") or []
            print("%s . %s" % (etiqueta, nid))
            print("  titulo: %s" % n.get("titulo_concepto", "?"))
            print("  pasos_accionables (%d), ENTEROS:" % len(pasos))
            for i, paso in enumerate(pasos, 1):
                print("    %d. %s" % (i, paso))
            print()

    print("=" * 90)
    print("FIN. Cinco ejemplares impresos enteros. La VARA se escribe en el reporte,")
    print("no aqui: este instrumento imprime el material, no juzga.")
    print("=" * 90)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
