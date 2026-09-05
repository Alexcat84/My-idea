# -*- coding: utf-8 -*-
r"""vuelta171_tarea5_censo_y_barrido.py . TAREA 5.b y 5.c DE LA VUELTA 171
(adjudicaciones 6.9 y 6.12 del acta 170).

LAS DOS SON BUSQUEDAS QUE NADIE HABIA CORRIDO, Y LAS DOS SE CORREN AQUI. La
regla que las obliga es `EJECUTOR.md` 9: **una busqueda negativa no se puede
citar**. El ejecutor de la vuelta 170 dijo que no encontro vocabulario cerrado
para el campo `forma` sin haberlo barrido, y ni el ni el auditor corrieron la
busqueda de los 8 pares.

5.b EL CENSO DEL CAMPO `forma` sobre las entradas de
`docs/plan/INVENTARIO.jsonl`, en TRES varas distintas para no depender de una
sola forma de mirar:
  (i)   LA CABEZA del campo: el primer token en mayusculas con el que abre cada
        `forma`, que es como la casa escribe la particion (`MEZCLADO`,
        `SUB-PURO`, `PARTIDO n mas m`, `PROVISIONAL`, ...);
  (ii)  TODO token en mayusculas de cuatro letras o mas que aparezca EN
        CUALQUIER SITIO del campo, con cuantas entradas lo usan;
  (iii) LA BUSQUEDA DE UNA NOMINA ESCRITA en las paginas de doctrina
        (`docs/BANCO_DE_TEXTOS.md` y `docs/plan/BANCO_DEL_PLAN.md`): si existe
        un vocabulario cerrado, esta escrito ahi; y si no, ESO es el hallazgo, y
        se dice con el comando corrido delante en vez de con un "no encontre".

5.c EL BARRIDO DE LOS 8 PARES SIN LEER de `la supervision de la IA` sobre las
fichas de `docs/plan/OPERACIONES.jsonl`, en los cuatro campos que el encargo
nombra (`nodos`, `preservar`, `eliminar`, `superviviente`). LOS 8 PARES NO SE
TECLEAN: se computan con el resolutor delante (`P.1`), igual que los computo la
vuelta 170, y se nombran uno a uno.

DE SOLO LECTURA. No escribe nada salvo su propia salida.

USO:  python scripts/loop/vuelta171_tarea5_censo_y_barrido.py
"""
import collections
import io
import itertools
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
INVENTARIO = os.path.join(RAIZ, "docs", "plan", "INVENTARIO.jsonl")
OPERACIONES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
PLAN = os.path.join(RAIZ, "docs", "plan")
BANCOS = [os.path.join(RAIZ, "docs", "BANCO_DE_TEXTOS.md"),
          os.path.join(RAIZ, "docs", "plan", "BANCO_DEL_PLAN.md")]
RACIMO = "la supervision de la IA"

PAT_LD = re.compile(
    r"^#{1,4}\s+`(LD-\d+)`\s*\.\s*`([a-z0-9_]+)`\s+contra\s+`([a-z0-9_]+)`\s*\.\s*\*\*([A-Z ]+)\*\*",
    re.M)
PAT_LD_TABLA = re.compile(
    r"^\|\s*\**`([a-z0-9_]+)`\**\s+contra\s+\**`([a-z0-9_]+)`\**\s*\|\s*\**([A-Z][A-Z ]*?)\**\s*\|\s*$",
    re.M)
PAT_MAY = re.compile(r"\b([A-ZÑÁÉÍÓÚ][A-ZÑÁÉÍÓÚ\-]{3,})\b")


def cargar(p):
    return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 171, TAREA 5.b y 5.c: EL CENSO DEL CAMPO forma Y EL BARRIDO DE")
    print("LOS 8 PARES, LAS DOS BUSQUEDAS CORRIDAS EN VEZ DE AFIRMADAS")
    print("=" * 78)
    print("")

    inv = cargar(INVENTARIO)
    print("A) EL UNIVERSO DEL CENSO, CONTADO")
    print("   CIFRA entradas de docs/plan/INVENTARIO.jsonl: %d" % len(inv))
    con_forma = [e for e in inv if (e.get("forma") or "").strip()]
    print("   CIFRA entradas con campo `forma` no vacio: %d" % len(con_forma))
    print("   CIFRA entradas con `forma` vacio o ausente: %d" % (len(inv) - len(con_forma)))
    print("")

    print("B) 5.b VARA (i): LA CABEZA DE CADA `forma`, o sea con que palabra abre")
    cabezas = collections.Counter()
    ejemplos = {}
    for e in con_forma:
        f = e["forma"].strip()
        m = re.match(r"^([A-ZÑÁÉÍÓÚ][A-ZÑÁÉÍÓÚ\-]*)", f)
        cab = m.group(1) if m else "(abre en minusculas: %s)" % f.split()[0]
        cabezas[cab] += 1
        ejemplos.setdefault(cab, e.get("nombre", "?"))
    print("   CIFRA cabezas distintas: %d" % len(cabezas))
    for cab, n in cabezas.most_common():
        print("      %-46s %4d entrada(s)   ej.: %s" % (cab, n, ejemplos[cab][:34]))
    print("")

    print("C) 5.b VARA (ii): TODO TOKEN EN MAYUSCULAS DE 4 LETRAS O MAS, EN")
    print("   CUALQUIER SITIO DEL CAMPO, CON CUANTAS ENTRADAS LO USAN")
    usos = collections.Counter()
    for e in con_forma:
        for tok in set(PAT_MAY.findall(e["forma"])):
            usos[tok] += 1
    print("   CIFRA tokens distintos: %d" % len(usos))
    for tok, n in usos.most_common():
        print("      %-24s %4d entrada(s)" % (tok, n))
    print("")

    print("D) 5.b VARA (iii): ¿HAY UNA NOMINA ESCRITA EN LAS PAGINAS DE DOCTRINA?")
    print("   La busqueda se CORRE y se publica su salida; no se dice 'no encontre'.")
    candidatas = [t for t, _n in usos.most_common()]
    for banco in BANCOS:
        rel = os.path.relpath(banco, RAIZ).replace(os.sep, "/")
        if not os.path.exists(banco):
            print("   %s -> NO EXISTE" % rel)
            continue
        texto = io.open(banco, encoding="utf-8").read()
        print("   %s -> %d bytes" % (rel, len(texto.encode("utf-8"))))
        for frase in ["vocabulario", "nomina de formas", "el campo `forma`",
                      "campo forma", "formas posibles", "valores de `forma`"]:
            print("      contiene %-22r -> %d vez(veces)" % (frase, texto.count(frase)))
        presentes = [t for t in candidatas if t in texto]
        print("      tokens del censo que aparecen en esta pagina: %d de %d -> %s"
              % (len(presentes), len(candidatas), ", ".join(presentes) or "ninguno"))
    print("")

    print("E) 5.b LA PALABRA `FUNDIDA`, LOCALIZADA UNA POR UNA")
    quien = [e.get("nombre") for e in con_forma if "FUNDIDA" in e["forma"]]
    print("   CIFRA entradas del inventario cuyo `forma` la usa: %d" % len(quien))
    for n in quien:
        print("      %s" % n)
    hallada_en_doctrina = []
    for banco in BANCOS:
        if os.path.exists(banco) and "FUNDIDA" in io.open(banco, encoding="utf-8").read():
            hallada_en_doctrina.append(os.path.relpath(banco, RAIZ).replace(os.sep, "/"))
    print("   paginas de doctrina donde aparece la palabra: %d (%s)"
          % (len(hallada_en_doctrina), ", ".join(hallada_en_doctrina) or "ninguna"))
    print("")

    # ------------------------------------------------------------------- 5.c
    print("F) 5.c EL RESOLUTOR Y LAS SEDES DE LECTURA, LEIDOS HOY (P.1)")
    G = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    ALIAS = dict((a, k) for k, v in G.items() for a in (v.get("ids_alias") or []))

    def res(x):
        visto = set()
        while x in ALIAS and x not in visto:
            visto.add(x)
            x = ALIAS[x]
        return x

    V = cargar(VEREDICTOS)
    cola = {}
    for r in V:
        cola[tuple(sorted((res(r["nodo_a"]), res(r["nodo_b"]))))] = (
            r["clase"], r["puesto_intra"])
    dirigidas = {}
    for nombre in sorted(os.listdir(PLAN)):
        if not nombre.endswith(".md"):
            continue
        texto = io.open(os.path.join(PLAN, nombre), encoding="utf-8").read()
        for ld, a, b, clase in PAT_LD.findall(texto):
            dirigidas[tuple(sorted((res(a), res(b))))] = (clase.strip().split()[0], ld)
        for a, b, clase in PAT_LD_TABLA.findall(texto):
            dirigidas[tuple(sorted((res(a), res(b))))] = (
                clase.strip().split()[0], "fila de tabla en %s" % nombre)
    print("   grafo: %d nodos, %d entradas de alias" % (len(G), len(ALIAS)))
    print("   cola: %d filas, %d pares distintos tras resolver" % (len(V), len(cola)))
    print("   pares dirigidos distintos tras resolver: %d" % len(dirigidas))
    print("")

    print("G) 5.c LOS 8 PARES, COMPUTADOS Y NO TECLEADOS")
    idx = [e for e in inv if e.get("nombre") == RACIMO]
    if len(idx) != 1:
        print("   ROJO: %r aparece %d veces en el inventario." % (RACIMO, len(idx)))
        return 1
    miembros = idx[0].get("miembros") or []
    vivos = sorted(set(res(x) for x in miembros))
    colapsos = [(x, res(x)) for x in miembros if res(x) != x]
    pares = [tuple(sorted(p)) for p in itertools.combinations(vivos, 2)]
    sin = [p for p in pares if p not in cola and p not in dirigidas]
    print("   miembros escritos: %d" % len(miembros))
    print("   vivos tras resolver: %d" % len(vivos))
    print("   colapsos: %d %s" % (len(colapsos),
                                  "; ".join("%s -> %s" % c for c in colapsos) or ""))
    print("   pares posibles entre los vivos: %d" % len(pares))
    print("   leidos (cola mas dirigidas): %d" % (len(pares) - len(sin)))
    print("   SIN VEREDICTO: %d" % len(sin))
    for i, (a, b) in enumerate(sin, 1):
        print("      %d. %s  contra  %s" % (i, a, b))
    print("")

    print("H) 5.c EL BARRIDO SOBRE LAS FICHAS, EN SUS CUATRO CAMPOS")
    print("   comando equivalente, escrito al lado como manda el encargo:")
    print("   python - <<  for ficha in OPERACIONES.jsonl:")
    print("                    universo = res(nodos) + res(preservar) + res(eliminar)")
    print("                               + res(superviviente)")
    print("                    si los DOS nodos del par estan en universo -> ACIERTO")
    ops = cargar(OPERACIONES)
    print("   CIFRA fichas de docs/plan/OPERACIONES.jsonl: %d" % len(ops))
    campos = ("nodos", "preservar", "eliminar", "superviviente")

    def universo(f):
        u = set()
        for c in campos:
            v = f.get(c)
            if isinstance(v, list):
                u |= set(res(x) for x in v if isinstance(x, str))
            elif isinstance(v, str) and v:
                u.add(res(v))
        return u

    universos = {f["id_op"]: universo(f) for f in ops}
    total_nodos = len(set().union(*universos.values())) if universos else 0
    print("   CIFRA nodos distintos que esos cuatro campos nombran, tras resolver: %d"
          % total_nodos)
    print("")
    print("   PAR A PAR, Y NINGUNO SE OMITE:")
    aciertos_par = 0
    sueltos_totales = collections.Counter()
    for i, (a, b) in enumerate(sin, 1):
        con_a = sorted(k for k, u in universos.items() if a in u)
        con_b = sorted(k for k, u in universos.items() if b in u)
        juntos = sorted(set(con_a) & set(con_b))
        print("   %d. %s  contra  %s" % (i, a, b))
        print("        fichas que nombran el PRIMERO:  %d %s"
              % (len(con_a), ", ".join(con_a) or "(ninguna)"))
        print("        fichas que nombran el SEGUNDO:  %d %s"
              % (len(con_b), ", ".join(con_b) or "(ninguna)"))
        print("        fichas que nombran LOS DOS:     %d %s"
              % (len(juntos), ", ".join(juntos) or "(ninguna)"))
        if juntos:
            aciertos_par += 1
        for n in (a, b):
            sueltos_totales[n] += len([k for k, u in universos.items() if n in u])
    print("")
    print("I) EL RESULTADO DEL BARRIDO, CONTADO")
    print("   CIFRA pares de los 8 recogidos ENTEROS por alguna ficha: %d" % aciertos_par)
    nodos_del_racimo = sorted(set([n for p in sin for n in p]))
    print("   CIFRA nodos distintos que aparecen en los 8 pares: %d" % len(nodos_del_racimo))
    nombrados = [n for n in nodos_del_racimo
                 if any(n in u for u in universos.values())]
    print("   CIFRA de esos nodos que alguna ficha nombra: %d" % len(nombrados))
    for n in nodos_del_racimo:
        fich = sorted(k for k, u in universos.items() if n in u)
        print("      %-44s %d ficha(s) %s"
              % (n, len(fich), ", ".join(fich) or "(ninguna)"))
    print("")
    print("   LA CONCLUSION QUE LA MEDICION SOSTIENE, Y NI UNA MAS: de los 8 pares,")
    print("   %d aparecen ENTEROS en alguna ficha de las 71." % aciertos_par)
    print("")
    return 0


if __name__ == "__main__":
    sys.exit(main())
