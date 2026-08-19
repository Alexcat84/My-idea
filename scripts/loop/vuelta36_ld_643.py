# -*- coding: utf-8 -*-
"""vuelta36_ld_643.py - LA LECTURA DIRIGIDA DEL 643 POR P.5, MEDIDA ANTES DE LEERSE.

ESTRICTAMENTE DE SOLO LECTURA. No escribe en el archivo ni en un nodo.

SUCESOR DECLARADO de scripts/loop/vuelta34_leer_opd03.py, y lo que ANADE va dicho
(EJECUTOR.md regla 2): aquel imprime los seis nodos enteros y las aristas internas,
y eso se sigue usando tal cual (SALIDA_V36_NODOS_ENTEROS.txt). Este pone al lado
UNA MEDICION QUE AQUEL NO HACE: cuanto de cada nodo cabe en el otro.

POR QUE ESA MEDICION Y NO OTRA. Las cinco relecturas que esta misma vuelta volco
se decidieron con el criterio del 738 (la mecanica compartida no basta, el OBJETO
decide), y ese criterio lo escribio la vuelta 34, QUE NADIE HA AUDITADO. Apoyar
una sexta lectura en la misma vara heredada, y sola, seria encadenar seis
veredictos a un criterio sin auditar. ASI QUE EL 643 SE MIDE TAMBIEN CON UNA VARA
QUE NO DEPENDE DE ESE CRITERIO: la CONTENCION. Un par REPITE cuando el contenido
de uno vive dentro del otro; si cada lado conserva la mayoria de sus propios
pasos, ninguno contiene a nadie.

LA CORRESPONDENCIA PASO A PASO NO LA DECIDE ESTE SCRIPT: la decide el lector y se
declara aqui como dato de entrada, con el texto de los dos pasos impreso al lado
para que cualquiera pueda discutirla mirandola. Lo que el script hace es la
ARITMETICA de esa declaracion, imprimirla, y correr las guardas.

GUARDAS, escritas para caer:
  1. los dos nodos existen, estan VIVOS y tienen HOY los pasos que la lectura dice.
  2. el par sigue registrado en el archivo y sigue en la clase que la lectura espera.
  3. la arista se busca EN LOS DOS SENTIDOS contra el grafo compilado, con el
     RESOLUTOR DE ALIAS aplicado antes de comparar (P.1).
  4. ningun paso queda declarado como pareja de dos pasos distintos.

Uso: python scripts/loop/vuelta36_ld_643.py
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")

PUESTO = 643
A = "split_testing"
B = "test_ab_precio"
CLASE_ESPERADA = "A"
PASOS_ESPERADOS = {A: 4, B: 5}

# LA CORRESPONDENCIA DECLARADA POR EL LECTOR, paso de A contra paso de B.
# Solo se declara donde el gesto es el MISMO, no donde los dos hablan del mismo
# tema. Cada fila lleva el motivo por el que se declara o por el que no.
CORRESPONDENCIA = [
    (1, 1, "SI", "define las variaciones a testear contra definir las variantes a testear: "
                 "mismo verbo y mismo objeto gramatical, casi verbatim"),
    (2, None, "NO", "dividir el trafico EQUITATIVAMENTE entre control y challenge no tiene "
                    "pareja: el paso 2 del otro manda implementar en un canal real, que es "
                    "otra cosa"),
    (3, 4, "SI", "medir la conversion de cada variante, con metrica distinta (tasa del CTA "
                 "contra porcentaje de usuarios que prefieren) pero el mismo gesto"),
    (4, None, "NO", "asegurar significancia estadistica superior al 95 por ciento antes de "
                    "concluir NO existe en el otro nodo, en ningun paso"),
]
# Los pasos de B que ningun paso de A recoge, con su motivo.
B_SIN_PAREJA = [
    (2, "implementar el test en un canal real (sitio web, landing page): el otro nodo no "
        "nombra canal en ningun paso"),
    (3, "ejecutar MULTIPLES RONDAS para afinar el precio optimo: el otro nodo no itera, "
        "concluye una vez con la significancia en la mano"),
    (5, "seleccionar el precio o modelo validado con mayor conversion: el otro nodo NO "
        "tiene paso de quedarse con la ganadora, su cierre es el umbral estadistico"),
]


def leer(nid):
    ruta = os.path.join(NODOS, nid + ".json")
    if not os.path.exists(ruta):
        return None
    return json.load(io.open(ruta, encoding="utf-8"))


def main():
    print("=" * 78)
    print("LECTURA DIRIGIDA DEL PUESTO %d POR P.5: %s contra %s" % (PUESTO, A, B))
    print("=" * 78)

    print("\nGUARDA 1: los dos nodos, vivos y con los pasos de hoy")
    N = {}
    for nid in (A, B):
        d = leer(nid)
        if d is None:
            print("  ABORTA: no existe el fichero de %s" % nid)
            return 1
        N[nid] = d
        pasos = d.get("pasos_accionables") or []
        vivo = not d.get("deprecado")
        print("  %-16s vivo=%-5s pasos=%d (la lectura dice %d)  %s"
              % (nid, vivo, len(pasos), PASOS_ESPERADOS[nid],
                 "OK" if (vivo and len(pasos) == PASOS_ESPERADOS[nid]) else "ABORTA"))
        if not vivo or len(pasos) != PASOS_ESPERADOS[nid]:
            return 1

    print("\nGUARDA 2: el par en el archivo")
    V = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
    reg = None
    for v in V:
        if v["puesto_intra"] == PUESTO:
            reg = v
            break
    if reg is None:
        print("  ABORTA: el puesto %d no esta registrado" % PUESTO)
        return 1
    print("  puesto %d: %s contra %s, clase %s (la lectura espera %s)  %s"
          % (PUESTO, reg["nodo_a"], reg["nodo_b"], reg["clase"], CLASE_ESPERADA,
             "OK" if reg["clase"] == CLASE_ESPERADA else "ABORTA"))
    if reg["clase"] != CLASE_ESPERADA:
        return 1
    if {reg["nodo_a"], reg["nodo_b"]} != {A, B}:
        print("  ABORTA: el puesto %d no es el par que esta lectura cree" % PUESTO)
        return 1

    print("\nGUARDA 3: la arista, EN LOS DOS SENTIDOS y con el RESOLUTOR de P.1 aplicado")
    G = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    AL = {x: k for k, v in G.items() for x in (v.get("ids_alias") or [])}

    def res(x):
        s = set()
        while x in AL and x not in s:
            s.add(x)
            x = AL[x]
        return x

    ra, rb = res(A), res(B)
    print("  resueltos: %s -> %s   |   %s -> %s" % (A, ra, B, rb))
    hay = False
    for origen, destino in ((ra, rb), (rb, ra)):
        for campo in ("nodos_previos", "nodos_siguientes"):
            vecinos = [res(y) for y in (G.get(origen, {}).get(campo) or [])]
            marca = destino in vecinos
            print("    %-16s %-16s contiene a %-16s : %s"
                  % (origen, campo, destino, "SI" if marca else "no"))
            hay = hay or marca
    print("  ARISTA ENTRE LOS DOS: %s" % ("SI LA HAY" if hay else "NO HAY NINGUNA"))

    print("\nGUARDA 4: ningun paso declarado como pareja de dos")
    usados_b = [b for (_, b, si, _) in CORRESPONDENCIA if si == "SI"]
    if len(usados_b) != len(set(usados_b)):
        print("  ABORTA: un paso de %s esta declarado como pareja de dos pasos de %s" % (B, A))
        return 1
    print("  OK")

    pa = N[A]["pasos_accionables"]
    pb = N[B]["pasos_accionables"]

    print("\n" + "=" * 78)
    print("LA MEDICION DE CONTENCION, paso a paso y con el texto delante")
    print("=" * 78)
    print("\n--- LOS %d PASOS DE %s, uno por uno ---" % (len(pa), A))
    for i, (ia, ib, si, motivo) in enumerate(CORRESPONDENCIA, 1):
        print("  paso %d de %s: %s" % (ia, A, pa[ia - 1]))
        if si == "SI":
            print("     PAREJA: paso %d de %s: %s" % (ib, B, pb[ib - 1]))
        else:
            print("     SIN PAREJA")
        print("     motivo: %s" % motivo)
    print("\n--- LOS PASOS DE %s QUE NINGUN PASO DE %s RECOGE ---" % (B, A))
    for ib, motivo in B_SIN_PAREJA:
        print("  paso %d de %s: %s" % (ib, B, pb[ib - 1]))
        print("     motivo: %s" % motivo)

    comp_a = sum(1 for (_, _, si, _) in CORRESPONDENCIA if si == "SI")
    prop_a = len(pa) - comp_a
    comp_b = comp_a
    prop_b = len(pb) - comp_b
    print("\n" + "=" * 78)
    print("LA ARITMETICA DE LA DECLARACION, que es lo unico que calcula este script")
    print("=" * 78)
    print("  %-16s pasos %d | compartidos %d | PROPIOS %d (%.0f por ciento propio)"
          % (A, len(pa), comp_a, prop_a, 100.0 * prop_a / len(pa)))
    print("  %-16s pasos %d | compartidos %d | PROPIOS %d (%.0f por ciento propio)"
          % (B, len(pb), comp_b, prop_b, 100.0 * prop_b / len(pb)))
    print()
    print("  CONTIENE %s a %s? %s" % (A, B, "SI" if prop_b == 0 else "NO"))
    print("  CONTIENE %s a %s? %s" % (B, A, "SI" if prop_a == 0 else "NO"))
    print()
    print("  LA VARA DE CONTENCION, y no depende del criterio del 738: un par REPITE cuando")
    print("  el contenido de uno VIVE DENTRO del otro. Aqui NINGUNO contiene al otro y CADA")
    print("  LADO CONSERVA LA MAYORIA DE SUS PROPIOS PASOS. Eso no es repetir.")

    print("\n--- LOS ENTREGABLES, que el 9.6.2 dice que deciden mas rapido que los pasos ---")
    for nid in (A, B):
        print("  %-16s %s" % (nid, N[nid].get("entregable_esperado") or N[nid].get("entregable")))
    print("\n--- LAS CONDICIONES DE ACTIVACION ---")
    for nid in (A, B):
        for c in (N[nid].get("condiciones_activacion") or N[nid].get("condiciones") or []):
            print("  %-16s %s" % (nid, c))
    print("\n--- EL CABLEADO PROPIO DE CADA UNO (cuenta para la arista, criterio del 827) ---")
    for nid in (A, B):
        d = N[nid]
        print("  %-16s previos %d, siguientes %d, total %d"
              % (nid, len(d.get("nodos_previos") or []), len(d.get("nodos_siguientes") or []),
                 len(d.get("nodos_previos") or []) + len(d.get("nodos_siguientes") or [])))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
