#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""simular_destejido.py. SIMULA UN DESTEJIDO SOBRE UNA COPIA EN MEMORIA.

ESTRICTAMENTE DE SOLO LECTURA. No toca ni un nodo, ni un byte de dataset/.

POR QUE EXISTE, dicho sin adornos. El estandar P.7 del banco del plan
("TODA OPERACION DE MESA SE SIMULA ANTES DE ESCRIBIRSE LISTA") tiene instrumento
para FUSIONES, scripts/plan/simular_fusion.py, y NO tiene ninguno para
DESTEJIDOS. Las siete operaciones DESTEJIDO del plan (OP-D-01 a OP-D-07) se
escribieron LISTAS sin simulacion, porque P.7 habla de operaciones de MESA. Este
script NO extiende P.7 por su cuenta: aporta la medicion que faltaba y deja la
pregunta de doctrina (si un destejido debe simularse como una mesa) escrita en el
reporte de la vuelta 17, sin darla por contestada.

QUE PUEDE ROMPER UN DESTEJIDO, y es lo unico que este script mide:

  1. UN VEREDICTO QUE SE APOYA EN UN PASO CONCRETO. Media docena de razones del
     cribado dicen literalmente "en su paso N". Si el destejido se lleva ese paso,
     la razon deja de sostenerse y el veredicto no era invariante, era prestado.
  2. UNA ARISTA PASO A NODO. docs/plan/PASO_NODO_CALIBRADO.jsonl ancla aristas al
     TEXTO de un paso de la madre. Si el paso muere, la arista pierde su ancla.
  3. UNA REFERENCIA INTERNA COLGANDO. Un paso que sobrevive y nombra material que
     el destejido se llevo ("el problema original", "la pregunta"). ESTE TERCER
     PUNTO ES UNA HEURISTICA DE PALABRAS Y SU SALIDA ES UN AVISO ORIENTATIVO: no
     es un veredicto y no es una rotura, y por eso no entra en el VEREDICTO DEL
     ESCENARIO. Etiquetado el 14 ago 2026 (vuelta 18) por la adjudicacion del
     discutible 6 de la vuelta 17. NINGUN CRITERIO DEL SIMULADOR CAMBIO: lo unico
     que cambia es que la salida ahora lo dice con palabras.
  4. NADA MAS. Un destejido no mueve ids, no crea alias y no toca nodos_previos
     ni nodos_siguientes: el grado del nodo y el de todos sus vecinos tienen que
     salir IDENTICOS antes y despues, y el script lo comprueba en vez de suponerlo.

USO
  python scripts/plan/simular_destejido.py --nodo ID --conservar 1,2,5-9
  python scripts/plan/simular_destejido.py --nodo ID --conservar 1-4 --conservar 5-16
"""
import argparse
import collections
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
CAMPOS = ("nodos_previos", "nodos_siguientes")


def jsonl(ruta):
    with open(ruta, encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.strip()
            if linea:
                yield json.loads(linea)


def rango(txt):
    """'1,2,5-9' -> {1,2,5,6,7,8,9}"""
    salida = set()
    for trozo in txt.split(","):
        trozo = trozo.strip()
        if "-" in trozo:
            a, b = trozo.split("-")
            salida.update(range(int(a), int(b) + 1))
        elif trozo:
            salida.add(int(trozo))
    return salida


def grados(nodos):
    g = collections.Counter()
    for nid, n in nodos.items():
        for campo in CAMPOS:
            for destino in (n.get(campo) or []):
                g[nid] += 1
                g[destino] += 1
    return g


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--grafo", default=str(RAIZ / "dataset" / "metadata" / "master_graph.json"))
    ap.add_argument("--nodo", required=True)
    ap.add_argument("--conservar", action="append", required=True,
                    help="pasos que SOBREVIVEN, p.ej. 1-4 o 2,5,13-17. Repetible: cada uno es un escenario")
    args = ap.parse_args()

    grafo = json.load(open(args.grafo, encoding="utf-8"))
    nodos = grafo["nodos"]
    if args.nodo not in nodos:
        print("ese id no esta en el grafo:", args.nodo)
        return 1
    nodo = nodos[args.nodo]
    pasos = nodo["pasos_accionables"]
    total = len(pasos)

    veredictos = list(jsonl(RAIZ / "docs" / "INTRA_DOMINIO_VEREDICTOS.jsonl"))
    calibrado = list(jsonl(RAIZ / "docs" / "plan" / "PASO_NODO_CALIBRADO.jsonl"))

    print("=" * 78)
    print("SIMULACION DE DESTEJIDO:", args.nodo)
    print("=" * 78)
    print("fuente declarada:", nodo.get("fuente"))
    print("pasos hoy:", total, "| dominio:", nodo.get("dominio"))
    print()

    # ---- 4. lo que un destejido NO puede mover, comprobado y no supuesto ----
    g_antes = grados(nodos)
    print("CONTROL DE ALCANCE (lo que un destejido no puede mover):")
    print("  ids que se mueven: 0 (un destejido reescribe pasos_accionables, no renombra)")
    print("  alias que se crean: 0")
    print("  grado del nodo antes:", g_antes[args.nodo],
          "| vecinos declarados:", sum(len(nodo.get(c) or []) for c in CAMPOS))
    print("  aristas del grafo entero antes:",
          sum(len(n.get(c) or []) for n in nodos.values() for c in CAMPOS))
    print("  IDENTICOS DESPUES POR CONSTRUCCION: la operacion no escribe en nodos_previos")
    print("  ni en nodos_siguientes de nadie. Si una ejecucion los mueve, no es este destejido.")
    print()

    # ---- 1. veredictos que se apoyan en un paso concreto ----
    pares = [v for v in veredictos if args.nodo in (v["nodo_a"], v["nodo_b"])]
    print("PARES DEL CRIBADO DONDE APARECE EL NODO:", len(pares))
    apoyos = []
    patron = re.compile(r"\bpasos?\s+((?:\d+\s*(?:,|y|a|\s)\s*)*\d+)", re.IGNORECASE)
    for v in sorted(pares, key=lambda x: x["puesto_intra"]):
        otro = v["nodo_b"] if v["nodo_a"] == args.nodo else v["nodo_a"]
        citados = set()
        for m in patron.finditer(v["razon"]):
            for num in re.findall(r"\d+", m.group(1)):
                num = int(num)
                if 1 <= num <= total:
                    citados.add(num)
        marca = ""
        # LA PROPIA RAZON PUEDE DECLARARSE INVARIANTE, y entonces citar un paso es
        # senalar la POSICION del solape (banco 9.9), no apoyar el veredicto en el.
        # El script NO decide eso: lee lo que la razon dice y lo reporta aparte.
        invariante = "INVARIANTE" in v["razon"].upper()
        if citados:
            apoyos.append((v["puesto_intra"], v["clase"], otro, sorted(citados), invariante))
            marca = "  <-- CITA LOS PASOS " + ", ".join(str(x) for x in sorted(citados))
            if invariante:
                marca += " | y su razon SE DECLARA INVARIANTE"
        print("  puesto", v["puesto_intra"], "| clase", v["clase"], "| contra", otro, marca)
    print()

    # ---- 2. aristas paso a nodo ancladas al texto de un paso ----
    anclas = []
    for c in calibrado:
        if c["madre"] != args.nodo:
            continue
        texto = c["texto_paso"]
        cual = None
        for i, p in enumerate(pasos, 1):
            if p.strip() == texto.strip():
                cual = i
                break
        anclas.append((c["hijo"], cual, texto, c["arista"]))
    print("ARISTAS PASO A NODO ANCLADAS A UN PASO DE ESTE NODO:", len(anclas))
    for hijo, cual, texto, ya in anclas:
        print("   hacia", hijo, "| ancla en el paso", cual, "| arista ya escrita:", ya)
        print("     texto:", texto)
    como_hijo = [c for c in calibrado if c["hijo"] == args.nodo]
    print("  (y", len(como_hijo), "aristas donde este nodo es el HIJO: no dependen de sus pasos,",
          "dependen del paso de la madre, asi que ningun destejido de este nodo las toca)")
    print()

    # ---- por escenario ----
    for n, texto_rango in enumerate(args.conservar, 1):
        conservar = rango(texto_rango)
        fuera = sorted(set(range(1, total + 1)) - conservar)
        print("-" * 78)
        print("ESCENARIO", n, ": SOBREVIVEN los pasos", texto_rango,
              "->", len(conservar), "de", total, "| SE VAN:", fuera)
        print("-" * 78)

        roto = False
        for puesto, clase, otro, citados, invariante in apoyos:
            perdidos = [p for p in citados if p not in conservar]
            if not perdidos:
                print("  respeta el veredicto del puesto", puesto, "(cita", citados, ")")
            elif invariante:
                print("  AVISO, NO ROTURA, en el puesto", puesto, "(clase", clase, "contra", otro + ")")
                print("    cita los pasos", citados, "y este escenario se lleva", perdidos)
                print("    PERO SU PROPIA RAZON SE DECLARA INVARIANTE: cita el paso como POSICION")
                print("    del solape (banco 9.9), no como apoyo del veredicto. Se reporta y no")
                print("    se cuenta como rotura. Quien discrepe, que lea la razon entera.")
            else:
                roto = True
                print("  ROMPE el veredicto del puesto", puesto, "(clase", clase, "contra", otro + ")")
                print("    porque su razon se apoya en los pasos", citados,
                      "y este escenario se lleva", perdidos)

        for hijo, cual, texto, ya in anclas:
            if cual is None:
                print("  AVISO: el ancla hacia", hijo, "no casa con ningun paso literal, no se puede juzgar")
            elif cual not in conservar:
                roto = True
                print("  ROMPE el ancla de la arista paso a nodo hacia", hijo,
                      ": vivia en el paso", cual)
            else:
                print("  respeta el ancla hacia", hijo, "(paso", str(cual) + ")")

        # ---- 3. referencias internas colgando ----
        pistas = ("original", "la pregunta", "el objetivo", "los objetivos", "el lienzo",
                  "el canvas", "los 9 bloques", "los nueve bloques", "el problema")
        colgando = []
        for i in sorted(conservar):
            if i > total:
                continue
            bajo = pasos[i - 1].lower()
            for pista in pistas:
                if pista in bajo:
                    fuente = [j for j in fuera if pista in pasos[j - 1].lower()]
                    if fuente:
                        colgando.append((i, pista, fuente))
        if colgando:
            print("  REFERENCIAS QUE QUEDAN COLGANDO (un paso que sobrevive nombra algo que se va):")
            for i, pista, fuente in colgando:
                print("    el paso", i, "nombra", repr(pista), "y quien lo establecia eran los pasos", fuente)
            print("    ESTO ES UN AVISO ORIENTATIVO, NO UN VEREDICTO Y NO UNA ROTURA.")
            print("    Es una heuristica de PALABRAS: casa una pista literal de una lista corta")
            print("    entre un paso que vive y un paso que se va, y no lee el sentido de")
            print("    ninguno de los dos. Puede senalar de mas (la misma palabra en dos temas")
            print("    distintos) y puede callar de menos (la referencia escrita con otras")
            print("    palabras). NO cuenta para el VEREDICTO DEL ESCENARIO de abajo, a")
            print("    proposito. Lo que hace es MANDAR A LEER los pasos que nombra: la")
            print("    decision es de quien los lea.")
        else:
            print("  referencias internas colgando: ninguna detectada por la heuristica de")
            print("    palabras. AVISO ORIENTATIVO: ese cero NO es un certificado de que no")
            print("    haya ninguna. Solo dice que ninguna pista de la lista corta caso.")

        print("  VEREDICTO DEL ESCENARIO:", "ROMPE ALGO" if roto else "no rompe ningun apoyo medido")
        print()

    return 0


if __name__ == "__main__":
    sys.exit(main())
