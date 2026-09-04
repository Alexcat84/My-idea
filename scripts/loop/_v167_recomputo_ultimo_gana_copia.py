#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""recomputo_3388.py . EL RECOMPUTO DE LA FASE II, LOS CUATRO PASOS EN ORDEN.

CORRECCION DECLARADA, 19 ago 2026 (vuelta 48), y el texto viejo se queda delante
porque una correccion que tapa lo que corrige no se puede auditar. Lo que este
docstring decia era:

    ESTRICTAMENTE DE SOLO LECTURA. No escribe ni un nodo, ni un veredicto, ni
    una operacion. Solo imprime y, si se pide, vuelca su propio jsonl de salida
    bajo docs/plan/.

Y NO ERA CIERTO: --salida traia un default apuntando a
docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl, asi que la corrida desnuda PISABA
ese fichero SELLADO sin pedir nada. Le paso a la vuelta 47 (332 lineas bajadas a
324, restauradas con git checkout; reporte de la vuelta 47, seccion 6). Es la
especie del canon 9 del banco (fallar ruidoso, no mentir calladito): un
instrumento que se anuncia de solo lectura y escribe NO DEJA SINTOMA.

LO QUE ES DE VERDAD, hoy: NO TOCA NI UN NODO, NI UN VEREDICTO, NI UNA OPERACION,
y ESCRIBE EXACTAMENTE UN FICHERO, el que se le nombre en --salida, que ahora es
OBLIGATORIO Y SIN DEFAULT. Sin --salida la corrida FALLA VISIBLE en vez de pisar
nada. Elegir donde escribe es de quien lo corre, no del instrumento.

Disparador cumplido: el cribado intra-dominio llego al puesto 3.388 (banco
9.21, OP-U-02). Es la UNICA recomputacion general del plan.

MODELADO SOBRE LO QUE YA EXISTE Y FUNCIONA:
  - scripts/plan/nominas.py: el comp() de componentes y el cobertura() con las
    formas PURO / SUB-PURO / MEZCLADO.
  - scripts/volcar_pares.py: el res() para resolver alias.

REGLA P.1 DEL BANCO DEL PLAN: todo conteo que toque ids pasa por el resolutor
antes de contar. Los cuatro pasos de aqui resuelven ANTES de contar; un
recomputo literal contaria los absorbidos como nodos vivos y no veria las
auto-aristas via alias.

EL ORDEN NO ES DE COMODIDAD: cada paso usa la salida del anterior
(08_VERIFICACION.md).

Uso:  python scripts/plan/recomputo_3388.py --salida docs/loop/RECOMPUTO_VXX.jsonl

      La forma sin --salida ya no existe: falla con codigo 2 y lo dice.
      Y la salida NO se apunta a docs/plan/ salvo que el encargo mande
      re-sellar la nomina: ese fichero esta sellado.
"""
import argparse
import collections
import io
import itertools
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]


def cargar(p):
    return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--grafo", default=str(RAIZ / "dataset" / "metadata" / "master_graph.json"))
    ap.add_argument("--veredictos", default=str(RAIZ / "docs" / "INTRA_DOMINIO_VEREDICTOS.jsonl"))
    ap.add_argument("--cola", default=str(RAIZ / "docs" / "INTRA_DOMINIO_PARES.jsonl"))
    ap.add_argument("--corte-viejo", type=int, default=2117,
                     help="corte de la medicion anterior (OP-U-01/OP-U-02), para separar edad de las A")
    # OBLIGATORIO Y SIN DEFAULT (vuelta 48, canon 9 del banco): el default viejo
    # apuntaba a la nomina SELLADA y la corrida desnuda la pisaba en silencio.
    ap.add_argument("--salida", required=True,
                     help="jsonl de componentes que este instrumento ESCRIBE. "
                          "Obligatorio: sin el, la corrida falla en vez de pisar "
                          "la nomina sellada de docs/plan/.")
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    G = json.load(io.open(args.grafo, encoding="utf-8"))["nodos"]
    ALIAS = {a: k for k, v in G.items() for a in (v.get("ids_alias") or [])}

    def res(x, visto=None):
        """EL RESOLUTOR, con la semantica de resolverId del motor: camina la
        cadena de alias hasta el id final, sin ciclar."""
        visto = visto or set()
        while x in ALIAS and x not in visto:
            visto.add(x)
            x = ALIAS[x]
        return x

    V = cargar(args.veredictos)
    P = cargar(args.cola)
    corte = max(r["puesto_intra"] for r in V)

    print("=" * 78)
    print("RECOMPUTO_3388.PY, corte %d, grafo %d nodos (%d deprecados)"
          % (corte, len(G), sum(1 for v in G.values() if v.get("deprecado"))))
    print("=" * 78)

    # ------------------------------------------------------------------
    # PASO 1: EL RETRATO DE LAS A
    # ------------------------------------------------------------------
    print()
    print("### PASO 1: EL RETRATO DE LAS A (resueltas por alias)")
    print()

    a_crudas = [r for r in V if r["clase"] == "A"]
    retrato = {}          # frozenset(resueltos) -> lista de veredictos que lo forman
    colapsos = []          # A que se vuelven auto-arista tras resolver
    for r in a_crudas:
        ra, rb = res(r["nodo_a"]), res(r["nodo_b"])
        if ra == rb:
            colapsos.append(r)
            continue
        key = frozenset((ra, rb))
        retrato.setdefault(key, []).append(r)

    print("A crudas en el archivo (clase == 'A'): %d" % len(a_crudas))
    print("de esas, colapsan a auto-arista tras resolver (mismo nodo vivo en los dos lados): %d"
          % len(colapsos))
    for r in colapsos:
        print("   puesto %d: %s <-> %s (resuelven al mismo id)" % (r["puesto_intra"], r["nodo_a"], r["nodo_b"]))
    print("PARES DISTINTOS EN EL RETRATO (tras resolver y deduplicar): %d" % len(retrato))
    multi = {k: v for k, v in retrato.items() if len(v) > 1}
    print("de esos, con mas de un veredicto crudo apuntando al mismo par resuelto: %d" % len(multi))
    for k, v in multi.items():
        print("   %s: puestos %s" % (sorted(k), [r["puesto_intra"] for r in v]))
    print("FECHA DE CORTE: puesto %d (archivo entero, banco 9.21)" % corte)

    # ------------------------------------------------------------------
    # PASO 2: EL BARRIDO DE CONFIRMADAS CONTRA LAS A
    # ------------------------------------------------------------------
    print()
    print("### PASO 2: EL BARRIDO DE CONFIRMADAS CONTRA LAS A")
    print()
    print("NO CORRIDO. Localizada la cifra (11 costuras confirmadas con pegado de Hugos, de 46")
    print("costuras confirmadas en total) en docs/plan/01_FUENTES.md linea 53 y linea 62, y en")
    print("docs/plan/CORRECCIONES_A_APLICAR.md lineas 169-174 (CORRECCION 4). NINGUNA de las dos")
    print("escribe la nomina como LISTA de nodos: las dos citan solo el numero 11 (contra el 21 de")
    print("la firma del injerto, que ese si esta escrito nodo por nodo). Busqueda adicional sobre")
    print("docs/ completo (grep 'costuras confirmadas', 'confirmadas de rebote'): docs/COSTURAS_")
    print("INTERNAS_RESUMEN.md secciones 6-7 y docs/FICHA_SUBFUSION_GRADIENTE.md solo repiten el")
    print("CONTEO de 46 (45 nucleo + 1 quality) sin nomina; docs/GRADIENTE_VEREDICTOS.md tiene una")
    print("familia distinta, 'costuras confirmadas DE REBOTE' (6 casos, nombrados, pero es otro")
    print("universo: verificaciones post-cirugia de la cola del gradiente, no la nomina de las 46")
    print("del cierre de costuras internas). SIN LISTA ESCRITA EN NINGUN SITIO: el paso 2 NO SE")
    print("CORRE. No se inventa ni se reconstruye de memoria.")

    # ------------------------------------------------------------------
    # PASO 3: EL CIERRE TRANSITIVO sobre el retrato del paso 1
    # ------------------------------------------------------------------
    print()
    print("### PASO 3: EL CIERRE TRANSITIVO (sobre el retrato del paso 1, no sobre el archivo crudo)")
    print()

    ady = collections.defaultdict(set)
    edge_puesto = {}
    for (ra, rb), vs in retrato.items():
        ady[ra].add(rb)
        ady[rb].add(ra)
        edge_puesto[frozenset((ra, rb))] = min(r["puesto_intra"] for r in vs)

    vistos = set()
    componentes = []
    for n in list(ady):
        if n in vistos:
            continue
        pila = [n]
        c = set()
        while pila:
            x = pila.pop()
            if x in c:
                continue
            c.add(x)
            pila.extend(ady[x] - c)
        vistos |= c
        componentes.append(c)

    tam = collections.Counter(len(c) for c in componentes)
    print("nodos con al menos una A (tras resolver): %d" % len(ady))
    print("componentes totales: %d" % len(componentes))
    print("tamano 1 (sueltos, imposible: todo nodo en ady tiene A, tamano minimo 2): %d" % tam.get(1, 0))
    print("distribucion de tamanos (>=2): %s" % dict(sorted((k, v) for k, v in tam.items() if k >= 2)))
    mayores = sorted((c for c in componentes if len(c) >= 2), key=lambda c: -len(c))
    print()
    print("COMPONENTES DE TAMANO >= 2, la mas grande primero:")
    for c in mayores:
        print("   tamano %2d: %s" % (len(c), ", ".join(sorted(c))))

    # ------------------------------------------------------------------
    # PASO 4: LAS NOMINAS Y LOS ACTOS, con cobertura al lado
    # ------------------------------------------------------------------
    print()
    print("### PASO 4: LAS NOMINAS Y LOS ACTOS (cobertura banco 9.26, CERRADO/ABIERTO como OP-U-01)")
    print()

    # CORRECCION DECLARADA, 4 sep 2026 (vuelta 167, TAREA 3; acta 166,
    # adjudicacion 6.5, por su hallazgo 4.2). El texto viejo se queda delante
    # porque una correccion que tapa lo que corrige no se puede auditar. Lo que
    # este bloque hacia era, literal:
    #
    #     leido = {}
    #     for r in V:
    #         ra, rb = res(r["nodo_a"]), res(r["nodo_b"])
    #         if ra == rb:
    #             continue
    #         leido[frozenset((ra, rb))] = r
    #
    # ULTIMO GANA POR PAR RESUELTO Y SIN MIRAR LA CLASE. Un par con varias filas
    # crudas se quedaba con la ULTIMA DEL FICHERO, asi que un par que SI tiene
    # una fila `A` pero cuya ultima fila es `B` o `D` dejaba de contar como
    # arista `A` interna de su componente. Y eso rompia la comprobacion ii, que
    # compara el retrato del PASO 1 (pares con AL MENOS UNA `A`) contra estas
    # aristas internas: el instrumento imprimia `149` contra `146` y su pie
    # decia `LAS CUATRO: AL MENOS UNA FALLA`. Los tres pares que se perdian van
    # medidos y nombrados uno por uno en
    # `docs/loop/SALIDA_V167_T3_MEDICION_PROPIA.txt`.
    #
    # LO QUE CAMBIA Y LO QUE NO, dicho antes de leerlo: la `A` GANA (si el par
    # ya tenia una fila `A` guardada, una fila posterior de otra clase NO la
    # pisa), y para todo lo demas se conserva el ultimo gana de siempre, para
    # que esta correccion no mueva ninguna otra cifra del PASO 4. NO SE ADJUDICA
    # CLASE A NADIE: la pertenencia al retrato ya la decidieron las lecturas del
    # cribado; esto solo deja de perderla al agrupar.
    leido = {}
    for r in V:
        ra, rb = res(r["nodo_a"]), res(r["nodo_b"])
        if ra == rb:
            continue
        leido[frozenset((ra, rb))] = r
    encola = set()
    for p in P:
        ra, rb = res(p["nodo_a"]), res(p["nodo_b"])
        if ra != rb:
            encola.add(frozenset((ra, rb)))

    filas = []
    cerrados = []
    abiertos = []
    total_aristas_internas = 0
    total_nodos_en_actos = 0
    dep_en_componente = []

    for c in mayores:
        nom = sorted(c)
        pos = len(nom) * (len(nom) - 1) // 2
        pares_posibles = list(itertools.combinations(nom, 2))
        ley = [p for p in pares_posibles if frozenset(p) in leido]
        col = [p for p in pares_posibles if frozenset(p) in encola and frozenset(p) not in leido]
        fue = [p for p in pares_posibles if frozenset(p) not in encola and frozenset(p) not in leido]
        cl = collections.Counter(leido[frozenset(p)]["clase"] for p in ley)
        aristas_internas = cl.get("A", 0)
        cerrado = (len(fue) == 0 and len(col) == 0)
        edades = [edge_puesto[frozenset((a, b))] for a, b in itertools.combinations(nom, 2)
                  if frozenset((a, b)) in edge_puesto]
        todo_viejo = all(e <= args.corte_viejo for e in edades)
        todo_nuevo = all(e > args.corte_viejo for e in edades)
        for n in nom:
            if G.get(n, {}).get("deprecado"):
                dep_en_componente.append(n)
        total_aristas_internas += aristas_internas
        total_nodos_en_actos += len(nom)
        fila = {
            "miembros": nom, "tamano": len(nom), "posibles": pos, "leidos": len(ley),
            "en_cola_sin_leer": len(col), "fuera_de_cola": len(fue),
            "clases_internas": dict(cl), "aristas_A_internas": aristas_internas,
            "estado": "CERRADO" if cerrado else "ABIERTO",
            "edad": "TODO ANTERIOR AL 2117" if todo_viejo else ("TODO POSTERIOR AL 2117" if todo_nuevo else "MIXTO"),
        }
        filas.append(fila)
        (cerrados if cerrado else abiertos).append(fila)
        print("   [%s] tamano %2d | posibles %3d | leidos %3d | en cola sin leer %d | fuera de cola %2d | "
              "clases internas %-22s | edad %s"
              % (fila["estado"][0], fila["tamano"], fila["posibles"], fila["leidos"], fila["en_cola_sin_leer"],
                 fila["fuera_de_cola"], dict(cl), fila["edad"]))

    with io.open(args.salida, "w", encoding="utf-8", newline="\n") as fh:
        for fila in filas:
            fh.write(json.dumps(fila, ensure_ascii=False) + "\n")

    print()
    print("RESUMEN PASO 4:")
    print("  actos (componentes >=2): %d" % len(filas))
    print("  CERRADOS: %d sobre %d nodos" % (len(cerrados), sum(f["tamano"] for f in cerrados)))
    print("  ABIERTOS: %d sobre %d nodos" % (len(abiertos), sum(f["tamano"] for f in abiertos)))
    tam_cerrados = collections.Counter(f["tamano"] for f in cerrados)
    print("  CERRADOS por tamano: %s" % dict(sorted(tam_cerrados.items())))
    tam_abiertos = collections.Counter(f["tamano"] for f in abiertos)
    print("  ABIERTOS por tamano: %s" % dict(sorted(tam_abiertos.items())))
    print()
    print("  edad de los actos (TODO ANTERIOR AL CORTE VIEJO / MIXTO / TODO POSTERIOR):")
    edad_c = collections.Counter(f["edad"] for f in filas)
    print("   ", dict(edad_c))
    print("   ABIERTOS por edad:", dict(collections.Counter(f["edad"] for f in abiertos)))
    print("   CERRADOS por edad:", dict(collections.Counter(f["edad"] for f in cerrados)))
    print("escrito: %s" % args.salida)

    # ------------------------------------------------------------------
    # LAS CUATRO COMPROBACIONES
    # ------------------------------------------------------------------
    print()
    print("### LAS CUATRO COMPROBACIONES (08_VERIFICACION.md)")
    print()
    i_ok = total_nodos_en_actos == sum(len(c) for c in mayores)
    print("i. nodos en actos (%d) == suma de tamanos de las componentes (%d): %s"
          % (total_nodos_en_actos, sum(len(c) for c in mayores), "OK" if i_ok else "FALLA"))

    ii_ok = total_aristas_internas == len(retrato)
    print("ii. A vigentes resueltas del retrato (%d) == suma de aristas A internas de las componentes (%d): %s"
          % (len(retrato), total_aristas_internas, "OK" if ii_ok else "FALLA"))

    iii_ok = all((f["en_cola_sin_leer"] == 0 and f["fuera_de_cola"] == 0) for f in cerrados)
    print("iii. todo acto CERRADO tiene sus pares internos leidos y ningun miembro con par pendiente: %s"
          % ("OK" if iii_ok else "FALLA"))

    iv_ok = len(dep_en_componente) == 0
    print("iv. ningun nodo deprecado aparece dentro de una componente: %s (%d encontrados: %s)"
          % ("OK" if iv_ok else "FALLA", len(dep_en_componente), dep_en_componente))

    print()
    print("LAS CUATRO: %s" % ("TODAS OK" if (i_ok and ii_ok and iii_ok and iv_ok) else "AL MENOS UNA FALLA"))


if __name__ == "__main__":
    main()
