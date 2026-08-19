# -*- coding: utf-8 -*-
"""vuelta39_acto.py - LA PREGUNTA DE P.5 CONTESTADA, PARA CUALQUIER ACTO DEL PLAN.

ESTRICTAMENTE DE SOLO LECTURA. No funde nada, no toca un nodo, no escribe en el
archivo. Mide, imprime y deja el veredicto de si la fusion se puede ejecutar.

SUCESOR DECLARADO de scripts/loop/vuelta37_acto_opd04.py (EJECUTOR.md regla 2), y
lo que cambia va dicho: aquel traia los SIETE nodos y las TRECE lecturas dirigidas
de OP-D-04 ESCRITOS DENTRO DEL CODIGO, asi que servia para un acto y para ninguno
mas. Este LEE LA NOMINA de docs/plan/OPERACIONES.jsonl por el id de la operacion,
que es donde vive, y aborta si un par se queda sin clase en vez de inventarsela.
La aritmetica de los seis bloques es la misma y a proposito: cambiar la vara y el
sujeto en la misma corrida haria incomparables las dos medidas.

LO QUE MIDE, en este orden y con la regla que manda cada cosa:
  1. LOS PARES DEL ACTO CON SU CLASE, leidos del archivo de veredictos.
  2. EL DETECTOR DE NODOS PUENTE DE P.10: un nodo puente es el que tiene A con
     dos nodos que entre si son D. Si aparece, LA COMPONENTE NO SE FUNDE.
  3. LOS SUBCONJUNTOS CERRADOS: grupos con TODOS sus pares internos en A.
  4. LA ESPECIE DE 9.3.1 CON SU CORRECCION DEL 18 ago 2026: la prueba de ganador
     por derecho se hace UNICAMENTE sobre los pares A.
  5. EL CABLEADO DE P.8, resuelto por alias (P.1) y sin contarse a si mismo (9.14).
  6. LA RECIPROCIDAD ARISTA POR ARISTA entre los nodos del acto, que es lo que
     dice cuanto costaria cada eleccion de superviviente.

Uso: python scripts/loop/vuelta39_acto.py --op OP-D-05
"""
import io
import itertools
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
NODOS = os.path.join(RAIZ, "dataset", "nodos")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
CAMPOS = ("nodos_previos", "nodos_siguientes")
OPUESTO = {"nodos_previos": "nodos_siguientes", "nodos_siguientes": "nodos_previos"}

VERBOS_GANADOR = ("GANA ", "GANA.", " gana ", "SOBREVIVE", "sobrevive",
                  "superviviente es", "EL SUPERVIVIENTE")


def bloque(t):
    print("")
    print("=" * 78)
    print(t)
    print("=" * 78)


def cargar_grafo():
    with io.open(GRAFO, encoding="utf-8") as fh:
        g = json.load(fh)
    nodos = g.get("nodes") or g.get("nodos") or g
    if isinstance(nodos, dict):
        return nodos
    return dict((n.get("node_id") or n.get("id"), n) for n in nodos)


def resolver(nid, alias):
    visto, actual = set(), nid
    while actual in alias and actual not in visto:
        visto.add(actual)
        actual = alias[actual]
    return actual


def main():
    id_op = None
    argv = sys.argv[1:]
    for i, x in enumerate(argv):
        if x == "--op":
            id_op = argv[i + 1]
    if not id_op:
        sys.exit("hace falta --op <ID>")

    op = None
    for linea in io.open(OPS, encoding="utf-8-sig"):
        if not linea.strip():
            continue
        d = json.loads(linea)
        if d.get("id_op") == id_op:
            op = d
    if op is None:
        sys.exit("no existe la operacion %s" % id_op)

    NOM = list(op["nodos"])
    print("OPERACION : %s, %s, estado %s" % (id_op, op["tipo"], op["estado"]))
    print("NOMINA    : %d nodos, leidos de OPERACIONES.jsonl y no del codigo" % len(NOM))
    for n in NOM:
        print("   %s" % n)
    print("PARES POSIBLES: %d" % (len(NOM) * (len(NOM) - 1) // 2))

    bloque("0. GUARDA: LOS NODOS EXISTEN Y ESTAN VIVOS")
    G = {}
    for n in NOM:
        ruta = os.path.join(NODOS, n + ".json")
        if not os.path.exists(ruta):
            print("ABORTA: no existe dataset/nodos/%s.json" % n)
            return 1
        G[n] = json.load(io.open(ruta, encoding="utf-8"))
        print("  %-44s vivo=%-5s pasos=%-3d condiciones=%-3d fuente=%s"
              % (n, not G[n].get("deprecado"),
                 len(G[n].get("pasos_accionables") or []),
                 len(G[n].get("condiciones_activacion") or []), G[n].get("fuente")))
    if any(G[n].get("deprecado") for n in NOM):
        print("ABORTA: algun nodo de la nomina ya esta deprecado")
        return 1

    V = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
    por_par = {}
    for v in V:
        a, b = v.get("nodo_a"), v.get("nodo_b")
        if a and b:
            por_par[(a, b)] = por_par[(b, a)] = v

    bloque("1. LOS PARES DEL ACTO, CON SU CLASE Y SU FUENTE")
    clase, origen, razon = {}, {}, {}
    sin_clase = []
    for a, b in itertools.combinations(NOM, 2):
        v = por_par.get((a, b))
        if v is None:
            sin_clase.append((a, b))
            print("  ???  %-44s %-44s  SIN VEREDICTO EN EL ARCHIVO" % (a, b))
            continue
        clase[(a, b)] = clase[(b, a)] = v["clase"]
        origen[(a, b)] = origen[(b, a)] = "archivo, puesto %s" % v["puesto_intra"]
        razon[(a, b)] = razon[(b, a)] = v.get("razon") or ""
        print("  %-3s  %-44s %-44s  %s" % (v["clase"], a, b, origen[(a, b)]))
    if sin_clase:
        print("")
        print("ABORTA: %d par(es) sin clase. P.5 pide el acto LEIDO ENTERO antes de fundir."
              % len(sin_clase))
        return 1
    cuenta = {}
    for a, b in itertools.combinations(NOM, 2):
        cuenta[clase[(a, b)]] = cuenta.get(clase[(a, b)], 0) + 1
    print("")
    print("  %d de %d con clase. Reparto: %s"
          % (len(clase) // 2, len(NOM) * (len(NOM) - 1) // 2, cuenta))

    bloque("2. EL DETECTOR DE NODOS PUENTE (P.10)")
    print("Un nodo puente es el que tiene A con dos nodos que entre si son D.")
    print("")
    puentes = []
    for n in NOM:
        aes = [m for m in NOM if m != n and clase[(n, m)] == "A"]
        choques = [(x, y, clase[(x, y)]) for x, y in itertools.combinations(sorted(aes), 2)
                   if clase[(x, y)] != "A"]
        print("  %-44s A con %d: %s" % (n, len(aes), ", ".join(sorted(aes)) or "(ninguno)"))
        if choques:
            puentes.append(n)
            for x, y, c in choques:
                print("        PUENTE: %s contra %s da %s (%s)" % (x, y, c, origen[(x, y)]))
        else:
            print("        no es puente: sus A cierran triangulo entre si (o tiene menos de dos)")
    print("")
    print("  NODOS PUENTE: %d -> %s" % (len(puentes), puentes))

    bloque("3. LOS SUBCONJUNTOS CERRADOS: todos sus pares internos en A")
    cerrados = []
    for k in range(len(NOM), 1, -1):
        for grupo in itertools.combinations(NOM, k):
            if all(clase[(x, y)] == "A" for x, y in itertools.combinations(grupo, 2)):
                if not any(set(grupo) < set(g) for g in cerrados):
                    cerrados.append(grupo)
    print("  cerrados maximales encontrados: %d" % len(cerrados))
    for g in cerrados:
        print("     tamano %d: %s" % (len(g), ", ".join(g)))
        for x, y in itertools.combinations(g, 2):
            print("        %s con %s: %s (%s)" % (x, y, clase[(x, y)], origen[(x, y)]))
    if len(cerrados) == 1 and len(cerrados[0]) == len(NOM):
        print("")
        print("  EL ACTO ENTERO ES UN SUBCONJUNTO CERRADO: todos sus pares internos son A.")

    bloque("4. LA ESPECIE DE 9.3.1, SOBRE LOS PARES A UNICAMENTE")
    print("La correccion del 18 ago 2026: una D no es sobrevivir a un duelo, es que no")
    print("hubo duelo. La prueba se hace SOLO sobre los pares A.")
    print("")
    con_ganador = 0
    total_a = 0
    for a, b in itertools.combinations(NOM, 2):
        if clase[(a, b)] != "A":
            continue
        total_a += 1
        nombra = any(w in razon[(a, b)] for w in VERBOS_GANADOR)
        if nombra:
            con_ganador += 1
        print("  A  %-44s %-44s  nombra ganador: %s" % (a, b, "SI" if nombra else "NO"))
        print("       razon: %s" % (razon[(a, b)][:400] or "(vacia)"))
    print("")
    print("  pares A: %d.  Con ganador nombrado en su razon: %d." % (total_a, con_ganador))
    if total_a and con_ganador == 0:
        print("  NINGUN PAR A NOMBRA GANADOR: no hay GANADOR POR DERECHO posible, porque la")
        print("  prueba de 9.3.1 no tiene ni una victoria citable de la que tirar.")
        print("  LA ESPECIE ES POR ELEGIR, y la elige P.8 con lectura de contenido.")

    bloque("5. EL CABLEADO DE P.8, resuelto por alias y sin contarse a si mismo")
    grafo = cargar_grafo()
    alias = {}
    for nid, n in grafo.items():
        for al in (n.get("ids_alias") or []):
            alias[al] = nid
    entrantes = dict((n, 0) for n in NOM)
    for nid, n in grafo.items():
        if n.get("deprecado"):
            continue
        for campo in CAMPOS:
            for x in (n.get(campo) or []):
                r = resolver(x, alias)
                if r in entrantes and r != nid:
                    entrantes[r] += 1
    print("  %-44s %8s %8s %8s %8s" % ("nodo", "pasos", "previos", "siguien", "LO NOMBRAN"))
    for n in NOM:
        d = G[n]
        pre = len([x for x in (d.get("nodos_previos") or []) if resolver(x, alias) != n])
        sig = len([x for x in (d.get("nodos_siguientes") or []) if resolver(x, alias) != n])
        print("  %-44s %8d %8d %8d %8d"
              % (n, len(d.get("pasos_accionables") or []), pre, sig, entrantes[n]))

    bloque("6. LA RECIPROCIDAD ARISTA POR ARISTA, y es lo que dice cuanto cuesta cada eleccion")
    print("El ejecutor de fusiones DEPRECA al absorbido y redirige solo lo que lo NOMBRA")
    print("desde fuera. Las aristas que el absorbido declara y que el otro extremo NO")
    print("devuelve se quedan dentro de un nodo deprecado, o sea SE PIERDEN.")
    print("")
    for n in NOM:
        cojas = []
        for campo in CAMPOS:
            for x in (G[n].get(campo) or []):
                r = resolver(x, alias)
                if r == n:
                    continue
                vecino = grafo.get(r)
                if vecino is None:
                    cojas.append((campo, x, "el vecino no existe"))
                    continue
                devuelta = n in [resolver(y, alias) for y in (vecino.get(OPUESTO[campo]) or [])]
                if not devuelta:
                    cojas.append((campo, r, "el vecino NO la devuelve"))
        print("  %-44s aristas propias sin reciproco: %d" % (n, len(cojas)))
        for campo, r, motivo in cojas:
            print("       .%-18s %-40s %s" % (campo, r, motivo))
    print("")
    print("  LECTURA: elegir superviviente a X cuesta las aristas cojas de los OTROS, que")
    print("  son las que su fichero declara y nadie devuelve.")

    bloque("7. LO QUE LA OPERACION TIENE ESCRITO")
    for k in ("preservar", "verificacion", "evidencia", "adjudicacion", "superviviente"):
        print("  %s: %s" % (k, json.dumps(op.get(k), ensure_ascii=False)))
    print("  nota (%d caracteres):" % len(op.get("nota") or ""))
    print("    %s" % (op.get("nota") or ""))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
