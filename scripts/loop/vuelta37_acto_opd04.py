# -*- coding: utf-8 -*-
"""vuelta37_acto_opd04.py - LA PREGUNTA DE P.5 CONTESTADA Y EL PASO 3 DE OP-D-04 MEDIDO.

ESTRICTAMENTE DE SOLO LECTURA. No funde nada, no toca un nodo, no escribe en el
archivo. Mide, imprime y deja el veredicto de si la fusion se puede ejecutar.

SUCESOR DECLARADO de scripts/loop/vuelta32_acto_opd02.py y de
scripts/loop/vuelta33_acto_opd02.py. LO QUE CAMBIA VA DICHO (EJECUTOR.md regla 2):
aquellos median un acto de CUATRO nodos con SEIS pares posibles y leian la clase
del archivo; este mide uno de SIETE con VEINTIUNO, y por eso tiene que juntar DOS
fuentes de clase, el archivo (8 pares) y docs/plan/LECTURAS_DIRIGIDAS.md (13
pares, la decima tanda LD-83 a LD-95), porque una lectura dirigida NO entra en la
cola y NO existe en el archivo de veredictos. Las trece se declaran aqui como
dato de entrada con su LD al lado, y el instrumento ABORTA si alguna no esta
escrita en el fichero de lecturas dirigidas con esa misma clase en su cabecera.

LO QUE MIDE, en este orden y con la regla que manda cada cosa:
  1. LOS 21 PARES CON SU CLASE, juntando las dos fuentes.
  2. EL DETECTOR DE NODOS PUENTE DE P.10: un nodo puente es el que tiene A con
     dos nodos que entre si son D. P.10 dice que si aparece, LA COMPONENTE NO SE
     FUNDE hasta que ese triangulo se cierre, y que lo que NUNCA es salida es
     fundir la componente entera porque el cierre transitivo la junta.
  3. LOS SUBCONJUNTOS CERRADOS: los grupos de nodos en los que TODOS los pares
     internos son A. Es la tercera salida de P.10, fundir solo el cerrado y
     enlazar el resto.
  4. LA ESPECIE DE 9.3.1 CON SU CORRECCION DEL 18 ago 2026: la prueba de ganador
     por derecho se hace UNICAMENTE sobre los pares A, y pregunta si algun nodo
     gano todos los pares A que lo tocan. Un par cuya razon NO nombra ganador no
     da victoria a nadie: se cuenta como sin ganador y se dice.
  5. EL CABLEADO DE P.8 sobre la nomina entera, con el grado de cada nodo
     resuelto por alias (P.1) y sin contarse a si mismo (banco 9.14).
  6. EL RACIMO DECLARADO al que pertenecen tres de los siete, con su nomina
     entera leida de docs/RACIMOS_MIEMBROS.jsonl, para ver cuantos de sus
     miembros quedan FUERA del acto.

Uso: python scripts/loop/vuelta37_acto_opd04.py
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
LD = os.path.join(RAIZ, "docs", "plan", "LECTURAS_DIRIGIDAS.md")
RACIMOS = os.path.join(RAIZ, "docs", "RACIMOS_MIEMBROS.jsonl")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")

SIETE = [
    "brainstorming_divergente",
    "brainstorming_efectivo",
    "reglas_brainstorming",
    "generar_multiples_opciones",
    "construir_sobre_ideas_ajenas",
    "pensamiento_convergente_divergente",
    "design_attitude_vs_decision_attitude",
]

# Las TRECE lecturas dirigidas de esta vuelta, con su clase. Cada una se verifica
# contra su cabecera en docs/plan/LECTURAS_DIRIGIDAS.md antes de usarse.
DIRIGIDAS = {
    ("brainstorming_divergente", "construir_sobre_ideas_ajenas"): ("LD-83", "D"),
    ("brainstorming_divergente", "design_attitude_vs_decision_attitude"): ("LD-84", "D"),
    ("brainstorming_efectivo", "generar_multiples_opciones"): ("LD-85", "D"),
    ("brainstorming_efectivo", "pensamiento_convergente_divergente"): ("LD-86", "D"),
    ("brainstorming_efectivo", "design_attitude_vs_decision_attitude"): ("LD-87", "D"),
    ("reglas_brainstorming", "generar_multiples_opciones"): ("LD-88", "D"),
    ("reglas_brainstorming", "construir_sobre_ideas_ajenas"): ("LD-89", "D"),
    ("reglas_brainstorming", "pensamiento_convergente_divergente"): ("LD-90", "D"),
    ("reglas_brainstorming", "design_attitude_vs_decision_attitude"): ("LD-91", "D"),
    ("generar_multiples_opciones", "construir_sobre_ideas_ajenas"): ("LD-92", "D"),
    ("generar_multiples_opciones", "design_attitude_vs_decision_attitude"): ("LD-93", "A"),
    ("construir_sobre_ideas_ajenas", "pensamiento_convergente_divergente"): ("LD-94", "D"),
    ("construir_sobre_ideas_ajenas", "design_attitude_vs_decision_attitude"): ("LD-95", "D"),
}

# Palabras con las que una razon nombra a un ganador. Se busca el VERBO y no un
# substring suelto: la vuelta 33 recibio una caida por preguntar 'gana' in razon,
# porque 'gana' vive dentro de 'ganar' y una razon decia 'por ganar tiempo'.
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
    visto = set()
    actual = nid
    while actual in alias and actual not in visto:
        visto.add(actual)
        actual = alias[actual]
    return actual


def main():
    texto_ld = io.open(LD, encoding="utf-8").read()

    bloque("0. GUARDA: LAS TRECE DIRIGIDAS ESTAN ESCRITAS CON SU CLASE")
    for (a, b), (ld, clase) in sorted(DIRIGIDAS.items(), key=lambda x: x[1][0]):
        cabecera = "## `%s` . `%s` contra `%s` . **%s." % (ld, a, b, clase)
        ok = cabecera in texto_ld
        print("  %-6s %-3s %-38s contra %-38s escrita: %s"
              % (ld, clase, a, b, "SI" if ok else "NO"))
        if not ok:
            print("ABORTA: la cabecera de %s no esta literal en LECTURAS_DIRIGIDAS.md" % ld)
            print("        buscada: %s" % cabecera)
            return 1
    print("  las trece, con su clase, literales en el fichero.")

    V = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
    por_par = {}
    for v in V:
        a, b = v.get("nodo_a"), v.get("nodo_b")
        if a and b:
            por_par[(a, b)] = v
            por_par[(b, a)] = v

    bloque("1. LOS 21 PARES DEL ACTO, CON SU CLASE Y SU FUENTE")
    clase = {}
    origen = {}
    for a, b in itertools.combinations(SIETE, 2):
        v = por_par.get((a, b))
        if v is not None:
            clase[(a, b)] = clase[(b, a)] = v["clase"]
            origen[(a, b)] = origen[(b, a)] = "archivo, puesto %s" % v["puesto_intra"]
        elif (a, b) in DIRIGIDAS:
            ld, c = DIRIGIDAS[(a, b)]
            clase[(a, b)] = clase[(b, a)] = c
            origen[(a, b)] = origen[(b, a)] = "lectura dirigida %s" % ld
        elif (b, a) in DIRIGIDAS:
            ld, c = DIRIGIDAS[(b, a)]
            clase[(a, b)] = clase[(b, a)] = c
            origen[(a, b)] = origen[(b, a)] = "lectura dirigida %s" % ld
        else:
            print("ABORTA: el par %s contra %s no tiene clase por ninguna fuente" % (a, b))
            return 1
        print("  %-3s  %-38s %-38s  %s"
              % (clase[(a, b)], a, b, origen[(a, b)]))
    cuenta = {}
    for a, b in itertools.combinations(SIETE, 2):
        cuenta[clase[(a, b)]] = cuenta.get(clase[(a, b)], 0) + 1
    print("")
    print("  21 de 21 con clase. Reparto: %s" % cuenta)

    bloque("2. EL DETECTOR DE NODOS PUENTE (P.10)")
    print("Un nodo puente es el que tiene A con dos nodos que entre si son D.")
    print("")
    puentes = []
    for n in SIETE:
        aes = [m for m in SIETE if m != n and clase[(n, m)] == "A"]
        choques = []
        for x, y in itertools.combinations(sorted(aes), 2):
            if clase[(x, y)] != "A":
                choques.append((x, y, clase[(x, y)], origen[(x, y)]))
        print("  %-38s A con %d: %s" % (n, len(aes), ", ".join(sorted(aes)) or "(ninguno)"))
        if choques:
            puentes.append(n)
            for x, y, c, o in choques:
                print("        PUENTE: %s contra %s da %s (%s)" % (x, y, c, o))
        else:
            print("        no es puente: sus A cierran triangulo entre si (o tiene menos de dos)")
    print("")
    print("  NODOS PUENTE: %d -> %s" % (len(puentes), puentes))

    bloque("3. LOS SUBCONJUNTOS CERRADOS: todos sus pares internos en A")
    cerrados = []
    for k in range(len(SIETE), 1, -1):
        for grupo in itertools.combinations(SIETE, k):
            if all(clase[(x, y)] == "A" for x, y in itertools.combinations(grupo, 2)):
                if not any(set(grupo) < set(g) for g in cerrados):
                    cerrados.append(grupo)
    print("  cerrados maximales encontrados: %d" % len(cerrados))
    for g in cerrados:
        pares = ["%s(%s)" % (origen[(x, y)].split()[-1], clase[(x, y)])
                 for x, y in itertools.combinations(g, 2)]
        print("     tamano %d: %s" % (len(g), ", ".join(g)))
        print("        sus pares internos: %s" % ", ".join(pares))

    bloque("4. LA ESPECIE DE 9.3.1, SOBRE LOS PARES A UNICAMENTE")
    print("La correccion del 18 ago 2026 dice: una D no es sobrevivir a un duelo, es")
    print("que no hubo duelo. La prueba se hace SOLO sobre los pares A.")
    print("")
    con_ganador = 0
    for a, b in itertools.combinations(SIETE, 2):
        if clase[(a, b)] != "A":
            continue
        v = por_par.get((a, b))
        razon = (v["razon"] if v else "")
        nombra = any(w in razon for w in VERBOS_GANADOR)
        etiqueta = origen[(a, b)]
        if nombra:
            con_ganador += 1
        print("  A  %-38s %-38s  %-28s nombra ganador: %s"
              % (a, b, etiqueta, "SI" if nombra else "NO"))
    total_a = sum(1 for a, b in itertools.combinations(SIETE, 2) if clase[(a, b)] == "A")
    print("")
    print("  pares A: %d.  Con ganador nombrado en su razon: %d." % (total_a, con_ganador))
    if con_ganador == 0:
        print("  NINGUN PAR A NOMBRA GANADOR: no hay GANADOR POR DERECHO posible, porque")
        print("  la prueba de 9.3.1 (gano todos los pares A que lo tocan) no tiene ni una")
        print("  victoria citable de la que tirar. LA ESPECIE ES POR ELEGIR.")

    bloque("5. EL CABLEADO DE P.8, resuelto por alias y sin contarse a si mismo")
    grafo = cargar_grafo()
    alias = {}
    for nid, n in grafo.items():
        for al in (n.get("ids_alias") or []):
            alias[al] = nid
    entrantes = dict((n, 0) for n in SIETE)
    for nid, n in grafo.items():
        if n.get("deprecado"):
            continue
        for x in (n.get("nodos_siguientes") or []):
            r = resolver(x, alias)
            if r in entrantes and r != nid:
                entrantes[r] += 1
    print("  %-38s %8s %8s %8s" % ("nodo", "previos", "siguien", "entrant"))
    for n in SIETE:
        d = json.load(io.open(os.path.join(NODOS, n + ".json"), encoding="utf-8"))
        pre = len([x for x in (d.get("nodos_previos") or []) if resolver(x, alias) != n])
        sig = len([x for x in (d.get("nodos_siguientes") or []) if resolver(x, alias) != n])
        print("  %-38s %8d %8d %8d" % (n, pre, sig, entrantes[n]))

    bloque("6. EL RACIMO DECLARADO, con su nomina entera")
    for linea in io.open(RACIMOS, encoding="utf-8"):
        linea = linea.strip()
        if not linea:
            continue
        r = json.loads(linea)
        miembros = [m["node_id"] for m in r.get("miembros", [])]
        if set(miembros) & set(SIETE):
            dentro = sorted(set(miembros) & set(SIETE))
            fuera = sorted(set(miembros) - set(SIETE))
            print("  racimo: %s" % r["racimo"])
            print("     dominio censado : %s" % r.get("dominio_censado"))
            print("     miembros        : %d -> %s" % (len(miembros), miembros))
            print("     DENTRO del acto : %d -> %s" % (len(dentro), dentro))
            print("     FUERA del acto  : %d -> %s" % (len(fuera), fuera))

    bloque("7. LO QUE LA OPERACION TIENE ESCRITO")
    for linea in io.open(OPS, encoding="utf-8"):
        linea = linea.strip()
        if not linea:
            continue
        o = json.loads(linea)
        if o.get("id_op") == "OP-D-04":
            print("  superviviente : %r" % o.get("superviviente"))
            print("  eliminar      : %r" % o.get("eliminar"))
            print("  aristas_nuevas: %r" % o.get("aristas_nuevas"))
            print("  preservar:")
            for p in o.get("preservar", []):
                print("     - %s" % p)
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
