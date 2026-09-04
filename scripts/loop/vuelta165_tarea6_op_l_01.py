# -*- coding: utf-8 -*-
r"""vuelta165_tarea6_op_l_01.py . TAREA 6 de la vuelta 165: SE ABRE EL ULTIMO
TRAMO DE LA FASE III POR `OP-L-01` (adjudicacion 6.10 del acta 164).

QUE HACE, Y NO HACE NADA MAS. Lee la ficha ENTERA de `OP-L-01` de
`docs/plan/OPERACIONES.jsonl` con su linea, y comprueba sus TRES clausulas de
verificacion CONTRA EL ARCHIVO DE HOY. NO cambia el estado de la operacion, NO
toca un nodo y NO escribe en el plan: esta es una operacion de tipo `MESA` cuya
ficha declara `nodos`, `preservar`, `eliminar` y `aristas_nuevas` VACIOS, y eso
se comprueba aqui antes que nada, que es la simulacion previa.

EL RESOLUTOR VA DELANTE DE TODO CONTEO (`P.1`, y `EJECUTOR.md` 9). Comparar ids
literalmente no mide lo que parece: un id vivo y un alias suyo son el mismo nodo
escrito de dos maneras. El mapa de alias se construye de `dataset/nodos/*.json`
(`ids_alias`), y la clausula 1 se mide DOS VECES, literal y resuelta, para que se
vea que la resolucion no cambia el veredicto en vez de afirmarlo.

LO QUE ESTE INSTRUMENTO ESPERA ENCONTRAR Y NO ARREGLA. La clausula 2 dice *"el
marcador del cribado no se mueve: sigue en 2.117"* y su `fecha_corte` es del
11 ago 2026, ANTERIOR al cierre del cribado. Este instrumento MIDE el marcador de
hoy y publica la diferencia; NO decide como leer la clausula. Si no se puede leer
sin estrechar ni ensanchar, eso es PARADA y sale como PARADA.

SU CASO POSITIVO POR MUTACION es `vuelta165_tarea6_mutacion_op_l_01.py`.

USO:  python scripts/loop/vuelta165_tarea6_op_l_01.py
"""
import io
import itertools
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPERACIONES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
LECTURAS = os.path.join(RAIZ, "docs", "plan", "LECTURAS_DIRIGIDAS.md")
INVENTARIO = os.path.join(RAIZ, "docs", "plan", "INVENTARIO.jsonl")
NODOS = os.path.join(RAIZ, "dataset", "nodos")

CABECERA_LD = re.compile(
    r"^### `(LD-\d+)` \. `([^`]+)` contra `([^`]+)` \. \*\*([^*]+)\*\*", re.M)


def ficha(id_op):
    for i, l in enumerate(io.open(OPERACIONES, encoding="utf-8"), 1):
        l = l.strip()
        if not l:
            continue
        d = json.loads(l)
        if d.get("id_op") == id_op:
            return i, d
    raise SystemExit("ROJO: no existe la ficha %s" % id_op)


def mapa_de_alias():
    """EL RESOLUTOR (`P.1`). Devuelve (mapa alias -> destino, cifra de nodos)."""
    mapa = {}
    n = 0
    for f in sorted(os.listdir(NODOS)):
        if not f.endswith(".json"):
            continue
        n += 1
        d = json.load(io.open(os.path.join(NODOS, f), encoding="utf-8"))
        for a in (d.get("ids_alias") or []):
            mapa[a] = d["node_id"]
    return mapa, n


def resolver(mapa, x):
    visto = set()
    while x in mapa and x not in visto:
        visto.add(x)
        x = mapa[x]
    return x


def las_once():
    txt = io.open(LECTURAS, encoding="utf-8").read()
    return [(m.group(1), m.group(2), m.group(3), m.group(4))
            for m in CABECERA_LD.finditer(txt)]


def veredictos():
    filas = []
    for l in io.open(VEREDICTOS, encoding="utf-8"):
        l = l.strip()
        if l:
            filas.append(json.loads(l))
    return filas


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 165, TAREA 6: OP-L-01 CONTRA EL ARCHIVO DE HOY")
    print("=" * 78)
    print("")

    linea, d = ficha("OP-L-01")
    print("A) LA FICHA ENTERA, LEIDA HOY")
    print("   docs/plan/OPERACIONES.jsonl:%d" % linea)
    for k in ("id_op", "fase", "tipo", "orden", "estado", "fecha_corte"):
        print("   %-16s %s" % (k + ":", d.get(k)))
    for k in ("depende_de", "bloquea_a", "nodos", "preservar", "eliminar",
              "aristas_nuevas"):
        print("   %-16s %s (CIFRA %d)" % (k + ":", d.get(k), len(d.get(k) or [])))
    print("   verificacion, sus %d clausulas:" % len(d.get("verificacion") or []))
    for i, c in enumerate(d.get("verificacion") or [], 1):
        print("      %d. %s" % (i, c))
    print("   evidencia, sus %d entradas:" % len(d.get("evidencia") or []))
    for e in (d.get("evidencia") or []):
        print("      . %s" % e)
    print("   adjudicacion: %s" % d.get("adjudicacion"))
    print("")

    print("B) LA SIMULACION PREVIA: QUE ESCRIBIRIA ESTA OPERACION")
    escribiria = sum(len(d.get(k) or []) for k in
                     ("nodos", "preservar", "eliminar", "aristas_nuevas"))
    print("   CIFRA elementos que la ficha declara para escribir: %d" % escribiria)
    print("   CIFRA dependencias declaradas: %d" % len(d.get("depende_de") or []))
    print("   VEREDICTO DE LA SIMULACION: es una operacion de VERIFICACION PURA.")
    print("   No mueve un nodo, no mueve una arista y no toca el grafo. Lo unico")
    print("   que puede cambiar es su propio campo `estado`, y solo si sus tres")
    print("   clausulas se cumplen.")
    if escribiria != 0:
        print("   PARADA: la ficha declara escrituras y esta vuelta esta en MODO")
        print("   DE CIERRE para los nodos. No se toca nada.")
        return 1
    print("")

    mapa, n_nodos = mapa_de_alias()
    print("C) EL RESOLUTOR, DELANTE DE TODO CONTEO (P.1)")
    print("   CIFRA ficheros de nodo leidos: %d" % n_nodos)
    print("   CIFRA alias en el mapa: %d" % len(mapa))
    print("")

    once = las_once()
    V = veredictos()
    print("D) CLAUSULA 1: 'ninguna de las once aparece en")
    print("   INTRA_DOMINIO_VEREDICTOS.jsonl: viven solo aqui'")
    print("   CIFRA cabeceras LD leidas de LECTURAS_DIRIGIDAS.md: %d" % len(once))
    print("   CIFRA filas de docs/INTRA_DOMINIO_VEREDICTOS.jsonl: %d" % len(V))
    literal = set()
    resuelto = set()
    for f in V:
        a, b = f.get("nodo_a"), f.get("nodo_b")
        literal.add(frozenset((a, b)))
        resuelto.add(frozenset((resolver(mapa, a), resolver(mapa, b))))
    print("   CIFRA pares distintos, comparacion LITERAL: %d" % len(literal))
    print("   CIFRA pares distintos, comparacion RESUELTA: %d" % len(resuelto))
    dentro_lit, dentro_res = [], []
    for ld, a, b, clase in once:
        ra, rb = resolver(mapa, a), resolver(mapa, b)
        el = frozenset((a, b)) in literal
        er = frozenset((ra, rb)) in resuelto
        if el:
            dentro_lit.append(ld)
        if er:
            dentro_res.append(ld)
        print("      %-7s %-40s %-40s literal=%-3s resuelto=%-3s"
              % (ld, a, b, "SI" if el else "NO", "SI" if er else "NO"))
        if (ra, rb) != (a, b):
            print("              el resolutor mueve: %s -> %s | %s -> %s"
                  % (a, ra, b, rb))
    print("   CIFRA de las once que APARECEN, comparacion literal: %d" % len(dentro_lit))
    print("   CIFRA de las once que APARECEN, comparacion resuelta: %d" % len(dentro_res))
    c1 = (len(dentro_res) == 0)
    print("   CLAUSULA 1: %s" % ("SE CUMPLE" if c1 else "NO SE CUMPLE"))
    print("")

    print("E) CLAUSULA 2: 'el marcador del cribado no se mueve: sigue en 2.117'")
    print("   LA LETRA, COPIADA DE LA FICHA: %r" % (d.get("verificacion") or [None, None])[1])
    print("   LA FECHA DE CORTE DE LA FICHA: %s" % d.get("fecha_corte"))
    marcador_hoy = len(V)
    print("   CIFRA marcador del cribado HOY (filas del fichero): %d" % marcador_hoy)
    esperado = 2117
    print("   CIFRA que la clausula escribe: %d" % esperado)
    print("   CIFRA diferencia: %d" % (marcador_hoy - esperado))
    print("")
    print("   LAS DOS LECTURAS POSIBLES, Y NINGUNA SE ELIGE AQUI:")
    print("   (a) LITERAL, 'el marcador vale 2.117 hoy': NO se cumple, y no puede")
    print("       cumplirse, porque el cribado cerro en %d con su corte publicado."
          % marcador_hoy)
    print("   (b) DE EFECTO, 'esta operacion no mueve el marcador': se cumpliria,")
    print("       porque la simulacion de la seccion B da CERO escrituras. Pero")
    print("       para leerla asi hay que DESCARTAR el numeral '2.117' de la")
    print("       propia clausula, y eso es ESTRECHARLA.")
    print("   VEREDICTO: la clausula NO se puede leer sin estrechar ni ensanchar.")
    print("   ESO ES PARADA (EJECUTOR.md 5), y no se improvisa una lectura.")
    c2 = None
    print("")

    print("F) CLAUSULA 3: 'cada nomina afectada se re-mide con su cobertura al")
    print("   lado (banco 9.26)'")
    txt = io.open(LECTURAS, encoding="utf-8").read()
    tabla = re.search(r"## QUE NOMINAS Y QUE FORMAS CAMBIAN(.+?)\n---", txt, re.S)
    nombres = []
    if tabla:
        for l in tabla.group(1).split("\n"):
            m = re.match(r"^\|\s*\*\*(.+?)\*\*\s*\|", l)
            if m:
                nombres.append(m.group(1).replace("`", "").strip())
    print("   CIFRA nominas que la tabla de LECTURAS_DIRIGIDAS.md nombra: %d"
          % len(nombres))
    inv = []
    for l in io.open(INVENTARIO, encoding="utf-8"):
        l = l.strip()
        if l:
            inv.append(json.loads(l))
    print("   CIFRA filas de docs/plan/INVENTARIO.jsonl: %d" % len(inv))
    medidas, sin_mapeo = [], []
    for nom in nombres:
        cand = [x for x in inv
                if nom.lower() in (x.get("nombre") or "").lower()
                or (x.get("nombre") or "").lower().endswith(nom.lower())]
        cand = [x for x in cand if x.get("miembros")]
        if not cand:
            sin_mapeo.append(nom)
            print("      %-40s SIN ENTRADA CON MIEMBROS en el inventario" % nom)
            continue
        x = cand[0]
        miembros = [resolver(mapa, m) for m in x["miembros"]]
        posibles = list(itertools.combinations(sorted(set(miembros)), 2))
        leidos = [p for p in posibles if frozenset(p) in resuelto]
        ld_de_la_nomina = [ld for ld, a, b, _c in once
                           if resolver(mapa, a) in miembros
                           and resolver(mapa, b) in miembros]
        cubiertos = set(frozenset(p) for p in leidos)
        for ld, a, b, _c in once:
            ra, rb = resolver(mapa, a), resolver(mapa, b)
            if ra in miembros and rb in miembros:
                cubiertos.add(frozenset((ra, rb)))
        print("      %-40s -> inventario '%s' (%s)"
              % (nom, x["nombre"], x["tipo"]))
        print("          CIFRA miembros: %d | posibles: %d | leidos en el cribado: %d"
              % (len(set(miembros)), len(posibles), len(leidos)))
        print("          CIFRA lecturas dirigidas de esta tanda dentro: %d (%s)"
              % (len(ld_de_la_nomina), ", ".join(ld_de_la_nomina) or "ninguna"))
        print("          COBERTURA RE MEDIDA HOY (banco 9.26): %d de %d"
              % (len(cubiertos), len(posibles)))
        print("          cobertura que el inventario declara: %s"
              % str(x.get("cobertura"))[:70])
        medidas.append((nom, len(cubiertos), len(posibles), x.get("cobertura")))
    print("   CIFRA nominas RE MEDIDAS: %d" % len(medidas))
    print("   CIFRA nominas SIN ENTRADA MAPEABLE en el inventario: %d" % len(sin_mapeo))
    c3 = (len(sin_mapeo) == 0)
    print("   CLAUSULA 3: %s" % ("SE CUMPLE" if c3 else "NO SE PUEDE CUMPLIR ENTERA"))
    if sin_mapeo:
        print("   Y SE DICE POR QUE, SIN ADIVINAR: la clausula dice 'cada nomina")
        print("   afectada' y NO nombra cuales ni donde viven. Las que el")
        print("   inventario nombra con sus miembros se re miden arriba; las")
        print("   otras %d solo existen como prosa, y elegirles una entrada del"
              % len(sin_mapeo))
        print("   inventario seria DECIDIR, no medir.")
    print("")

    print("G) EL VEREDICTO DE LA OPERACION")
    print("   clausula 1: %s" % ("SE CUMPLE" if c1 else "NO SE CUMPLE"))
    print("   clausula 2: PARADA (no se puede leer sin estrechar ni ensanchar)")
    print("   clausula 3: %s" % ("SE CUMPLE" if c3 else "SE CUMPLE SOLO EN PARTE"))
    print("")
    print("   OP-L-01 NO SE CIERRA Y SU ESTADO NO SE TOCA: sigue en %r."
          % d.get("estado"))
    print("   UNA OPERACION CUYO TEXTO NO ALCANZA PARA EJECUTARSE SIN DECIDIR ES")
    print("   PARADA, NO UNA IMPROVISACION.")
    print("")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
