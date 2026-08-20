# -*- coding: utf-8 -*-
"""Vuelta 48: CUANTAS PUERTAS HAY DENTRO DEL LOTE DE `OP-U-01`.

ESTRICTAMENTE DE SOLO LECTURA.

CORRECCION DECLARADA, 20 ago 2026 (vuelta 52, TAREA 1.5 del encargo, que la
manda citando la adjudicacion de la pregunta 3 del acta de la vuelta 51). EL
TEXTO VIEJO VA DELANTE ENTERO, porque una correccion que tapa lo que corrige no
se puede auditar. Lo que este instrumento decia y hacia era esto:

    La pregunta que eso deja no es del acto 36: es de la operacion entera. Un
    nodo PROTEGIDO (semilla de entrada o extremo de puente aprobado) es una
    PUERTA por la que se entra a un mundo. Si muere, la puerta no abre. Este
    instrumento cuenta cuantos actos del lote tienen una puerta dentro, y
    separa los dos casos, que son muy distintos:

      a) UN SOLO miembro protegido: el acto SE SALVA si la lectura elige a ese
         nodo como superviviente. La regla de la pagina (sobrevive por
         CONTENIDO) puede apuntar al otro, y entonces hay choque y se declara.
      b) TODOS los miembros protegidos: NO HAY FUSION POSIBLE sin cerrar una
         puerta, porque alguien tiene que morir. Ese acto no se funde con las
         reglas escritas.

Y ESA DICOTOMIA NO ALCANZA. La vuelta 51 la rompio midiendo: los actos con
miembros `decision_cuando_fundar` mas `evaluacion_capacidades_fundador` mas
`tres_preguntas_carrera`, y `enfoque_paso_a_paso_investigacion_mercado` mas
`evaluacion_mercados_objetivo` mas `screening_mercados_potenciales`, tienen DOS
puertas cada uno y NINGUNO de sus supervivientes viables las deja vivas a las
dos. El instrumento los imprimia bajo el rotulo "SALVABLES (una sola puerta)"
IMPRIMIENDO DOS EN LA MISMA LINEA: el rotulo se desmentia a si mismo y la
salida seguia diciendo SALVABLE. Es la especie del canon 9 del banco (fallar
ruidoso, no mentir calladito): una guarda que tranquiliza sin mirar.

FALTABA EL TERCER CASO, y es el que se anade:

  c) ALGUNA PUERTA OBLIGADA A MORIR POR LA ESTRUCTURA DEL ACTO, CUALQUIERA SEA
     SU CUENTA.
     No es que todos los miembros sean puerta (caso b): es que NINGUNA eleccion
     de superviviente que la receta `P.12` permita deja vivas a todas las
     puertas del acto. El acto no se funde y queda DECLARADO IMPOSIBLE POR
     PUERTA.

     CORRECCION DE ROTULO DECLARADA, 20 ago 2026 (vuelta 53, TAREA 1.3 del
     encargo; adjudicacion del acta de la vuelta 52, pregunta 5 y seccion 3.2).
     EL TEXTO VIEJO VA DELANTE ENTERO, porque una correccion que tapa lo que
     corrige no se puede auditar. Este caso decia:

         c) MAS DE UNA PUERTA, CON ALGUNA OBLIGADA A MORIR POR LA ESTRUCTURA
            DEL ACTO.

     Y ESE ROTULO REPETIA EL SINTOMA EN VEZ DE DECIR LA VARA. La vara
     implementada abajo (un candidato es LIMPIO si ninguno de sus absorbidos es
     puerta; el acto es SALVABLE si tiene al menos un candidato limpio) NO
     CUENTA PUERTAS, y esta bien asi: la vuelta 52 encontro un tercer acto
     imposible por estructura con UNA SOLA puerta (calcular_peso_dimensional_
     antes_cotizar y hermanos), cuya unica puerta es el CENTRO de la estrella y
     por eso no puede sobrevivir. El listado imprimia "puertas (1)" justo
     debajo del rotulo que decia "mas de una". LA LETRA DEL SINTOMA NACE DEL
     ENCARGO 1.5 DE LA VUELTA 52, y su autor la declara suya en el acta 52,
     seccion 3.2: el ejecutor heredo esa letra, no la fabrico. La vara buena es
     la del acta 51, pregunta 3: un acto es IMPOSIBLE POR PUERTA cuando NINGUNA
     fusion posible respeta la guarda 1B.

LA VARA, escrita entera para poder discutirla, y no es nueva: es la de
`scripts/loop/vuelta50_supervivientes_viables.py`, que la saco del unico acto
ya resuelto (el del SPIN, vuelta 49), mas la guarda `1B` del encargo (ningun
absorbido puede ser semilla ni extremo de puente):

  - dado un superviviente S, PARTE A = {S} mas los miembros con arista `A`
    contra S; ABSORBIDOS = PARTE A menos S; MIXTOS = el resto.
  - si TODOS los pares internos del acto son `A` (FUSION PURA) el acto se funde
    entero: cualquier miembro puede ser S y ABSORBIDOS son todos los demas.
  - si el acto es MIXTO, S es VIABLE solo si la PARTE A es una clique `A` y
    queda al menos un mixto fuera.
  - un candidato S es LIMPIO si ninguno de sus ABSORBIDOS es puerta. Una puerta
    que se queda FUERA de la parte A (mixto) NO muere: sobrevive con su texto.
  - el acto es SALVABLE si tiene al menos un candidato LIMPIO. Si no lo tiene,
    es IMPOSIBLE POR PUERTA.

LAS DOS ETIQUETAS DE IMPOSIBLE SE SIGUEN IMPRIMIENDO POR SEPARADO aunque la
segunda contenga a la primera, porque las paginas ya citan la vieja por su
nombre: POR NOMINA (todos los miembros son puerta) y POR ESTRUCTURA (el caso c).

POR QUE EXISTE, y no es una idea: la primera corrida --ejecutar del tramo 1 de
la vuelta 48 depreco
investiga_con_fuentes_objetivas_antes_de_contactar_al_proveedor y GATE 0 SALIO
EN ROJO por DOS chequeos a la vez, porque ese nodo es SEMILLA DE ENTRADA del
mundo compras y ademas DESTINO DE UN PUENTE APROBADO. El dataset se restauro
con git checkout y el acto salio del lote.

Las fuentes de las puertas son las MISMAS que lee scripts/run_phase1.py en su
Gate 0. Las de las clases son docs/INTRA_DOMINIO_VEREDICTOS.jsonl resuelto por
el resolutor de la casa (`P.1`).

Uso: python scripts/loop/vuelta48_puertas_en_el_lote.py --nomina docs/loop/RECOMPUTO_V48_COMPONENTES.jsonl
"""
import argparse
import io
import itertools
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nomina", required=True)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    sem = set(json.load(io.open(os.path.join(RAIZ, "dataset", "metadata",
                                             "entry_seeds.json"),
                                encoding="utf-8")).get("seeds", []))
    n_core = len(sem)
    packs = os.path.join(RAIZ, "packs")
    for d in sorted(os.listdir(packs)):
        q = os.path.join(packs, d, "metadata", "entry_seeds.json")
        if os.path.exists(q):
            sem.update(json.load(io.open(q, encoding="utf-8")))
    pue = {}
    for d in sorted(os.listdir(packs)):
        q = os.path.join(packs, d, "metadata", "bridges_aprobados.json")
        if not os.path.exists(q):
            continue
        for x in json.load(io.open(q, encoding="utf-8")).get("aprobados", []):
            for extremo in ("core", "dominio"):
                if x.get(extremo):
                    pue.setdefault(x[extremo], set()).add(d)
    prot = sem | set(pue)

    # El resolutor de la casa (P.1), para poder leer la clase de cada par interno.
    todos = {}
    for nombre in sorted(os.listdir(NODOS)):
        if nombre.endswith(".json"):
            d = json.load(io.open(os.path.join(NODOS, nombre), encoding="utf-8"))
            todos[d["node_id"]] = d
    alias = {}
    for nid, d in todos.items():
        if not (d.get("deprecado") or d.get("deprecated")):
            for x in (d.get("ids_alias") or []):
                alias[x] = nid

    def res(x):
        visto = set()
        while x in alias and x not in visto:
            visto.add(x)
            x = alias[x]
        return x

    clases = {}
    for l in io.open(VER, encoding="utf-8"):
        if not l.strip():
            continue
        v = json.loads(l)
        clases.setdefault(frozenset((res(v["nodo_a"]), res(v["nodo_b"]))), set()).add(v["clase"])

    print("=" * 78)
    print("LAS PUERTAS DENTRO DEL LOTE DE OP-U-01")
    print("=" * 78)
    print("  semillas de entrada core                     : %d" % n_core)
    print("  semillas de entrada con las de los mundos    : %d" % len(sem))
    print("  nodos que son extremo de puente aprobado     : %d" % len(pue))
    print("  UNION, el universo PROTEGIDO                 : %d" % len(prot))

    R = [json.loads(l) for l in io.open(a.nomina, encoding="utf-8") if l.strip()]
    C = [r for r in R if r["estado"] == "CERRADO"]

    salvables, imp_nomina, imp_estructura, sin_receta = [], [], [], []
    for i, r in enumerate(C, 1):
        ms = list(r["miembros"])
        p = [x for x in ms if x in prot]
        if not p:
            continue

        es_a = {}
        for x, y in itertools.combinations(ms, 2):
            es_a[frozenset((x, y))] = "A" in (clases.get(frozenset((res(x), res(y)))) or set())
        pura = all(es_a.values())

        # Los candidatos a superviviente que la receta permite, con sus absorbidos.
        candidatos = []
        for s in ms:
            parte = [s] + [m for m in ms if m != s and es_a[frozenset((s, m))]]
            mixtos = [m for m in ms if m not in parte]
            if pura:
                candidatos.append((s, [m for m in ms if m != s], []))
                continue
            if not mixtos:
                continue  # no deja ningun mixto fuera: seria fusion entera
            if not all(es_a[frozenset(q)] for q in itertools.combinations(parte, 2)):
                continue  # la parte A no es clique
            candidatos.append((s, [m for m in parte if m != s], mixtos))

        limpios = [c for c in candidatos if not any(x in prot for x in c[1])]
        fila = (i, r, p, pura, candidatos, limpios)
        if not candidatos:
            sin_receta.append(fila)
        elif limpios:
            salvables.append(fila)
        elif len(p) == len(ms):
            imp_nomina.append(fila)
        else:
            imp_estructura.append(fila)

    total = len(salvables) + len(imp_nomina) + len(imp_estructura) + len(sin_receta)
    print()
    print("SOBRE LOS %d ACTOS CERRADOS:" % len(C))
    print("  actos con al menos una puerta dentro: %d" % total)
    print("    SALVABLES (hay al menos un superviviente que no absorbe ninguna puerta): %d"
          % len(salvables))
    print("    IMPOSIBLES POR NOMINA (todos sus miembros son puerta): %d" % len(imp_nomina))
    # CORRECCION DE ROTULO DECLARADA, 20 ago 2026 (vuelta 53, TAREA 1.3 del
    # encargo). EL TEXTO VIEJO VA DELANTE ENTERO: este parentesis decia
    # "(mas de una puerta, alguna obligada a morir)", que es el SINTOMA y no
    # la vara, y el listado de abajo imprime "puertas (1)" en uno de los tres.
    # El motivo entero esta en el caso c del docstring.
    print("    IMPOSIBLES POR ESTRUCTURA (alguna puerta obligada a morir por la"
          " estructura del acto, cualquiera sea su cuenta): %d"
          % len(imp_estructura))
    print("    SIN RECETA (ningun superviviente viable; no lo decide la puerta): %d"
          % len(sin_receta))

    def pinta(fila, con_candidatos):
        i, r, p, pura, candidatos, limpios = fila
        print("    acto %3d tam %d %-12s | puertas (%d): %s"
              % (i, r["tamano"], "FUSION PURA" if pura else "MIXTO", len(p), ", ".join(p)))
        print("               resto: %s"
              % (", ".join(x for x in r["miembros"] if x not in p) or "ninguno"))
        if not con_candidatos:
            return
        for s, absorbidos, mixtos in candidatos:
            marca = "LIMPIO" if not any(x in prot for x in absorbidos) else "CIERRA PUERTA"
            print("               S = %-46s %-13s absorbe: %s"
                  % (s, marca, ", ".join(absorbidos) or "nadie"))

    print()
    print("  LOS IMPOSIBLES POR NOMINA, uno por uno:")
    for fila in imp_nomina:
        pinta(fila, False)
    if not imp_nomina:
        print("    ninguno")

    print()
    print("  LOS IMPOSIBLES POR ESTRUCTURA, uno por uno y CON SUS CANDIDATOS:")
    for fila in imp_estructura:
        pinta(fila, True)
    if not imp_estructura:
        print("    ninguno")

    if sin_receta:
        print()
        print("  LOS SIN RECETA, uno por uno:")
        for fila in sin_receta:
            pinta(fila, False)

    print()
    print("  LOS SALVABLES, uno por uno (puerta que TIENE que sobrevivir):")
    for i, r, p, pura, candidatos, limpios in salvables:
        print("    acto %3d tam %d | puerta: %s" % (i, r["tamano"], ", ".join(p)))
        print("               resto: %s" % ", ".join(x for x in r["miembros"] if x not in p))
    print()
    print("LO QUE ESTO DEJA ESCRITO PARA LOS TRAMOS QUE VIENEN: la eleccion de")
    print("superviviente de esos %d actos NO es libre. La regla de la pagina dice" % total)
    print("que sobrevive por CONTENIDO; si el contenido apunta al que NO es puerta,")
    print("hay choque entre la vara de la fase y el Gate 0, y eso no lo resuelve")
    print("ninguna regla escrita hoy. Va como pregunta al auditor, no como decision.")
    print("Y LOS IMPOSIBLES POR ESTRUCTURA NO SON UN CHOQUE SINO UN CIERRE: ninguna")
    print("eleccion permitida los salva, asi que se DECLARAN y no se funden.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
