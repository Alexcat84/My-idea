# -*- coding: utf-8 -*-
# ROTULO titulo especie=PROCEDENCIA cita=vuelta:71 fuente=docs/loop/ACTA_AUDITOR.md prueba="ACTA DE LA VUELTA 71 DEL AUDITOR" corte=2026-08-26 motivo="el titulo nombra la VUELTA 71 porque es la vuelta cuyo reanclaje fabrico el ancla duplicada que este instrumento depura; el fichero es de la vuelta 72 y por eso el numero no calza con su propia vuelta a proposito"
"""vuelta72_ancla_duplicada.py . DEPURA EL ANCLA DUPLICADA QUE EL REANCLAJE DE LA
VUELTA 71 DEJO EN scripts/rumbos/banco_rumbos.json, Y COMPRUEBA POR MAQUINA QUE
NINGUN OTRO RUMBO DEL FICHERO QUEDO IGUAL.

TAREA 1 del encargo de la vuelta 72, adjudicacion 7 del acta 71. NADA DEL GRAFO
SE TOCA: ni un nodo, ni un veredicto, ni el marcador.

QUE PASO, MEDIDO POR EL AUDITOR EN EL ACTA 71 Y RE MEDIDO AQUI. El reanclaje de
la vuelta 71 (el que corre entre la fusion y run_phase1 para que ninguna
referencia del banco de rumbos apunte a un nodo deprecado) reescribio UNA
referencia del rumbo nucleo_le_sirve_a_todo_el_mundo. El ancla vieja y la nueva
resolvian AL MISMO destino vivo, asi que la lista `ancla` de ese rumbo quedo con
segmentos_de_clientes_problema_necesidad DOS VECES. No es un dato malo: es un
dato repetido, que es lo que este instrumento quita.

QUIEN FABRICA LIMPIA, Y ESA ES LA LETRA. P.16 por extension de su principio: la
vuelta que fabrica la duplicada es la que la retira, en el mismo carril en que
P.16 manda limpiar las aristas duplicadas que una fusion fabrica. Aqui la
duplicada no la fabrico una fusion sino un reanclaje, y por eso va por extension
del principio y no por la letra literal de P.16, que habla de aristas del grafo.

LO QUE SE MIDE Y SE PUBLICA, porque una busqueda negativa no se puede citar
(regla 9 de EJECUTOR.md): NO basta con depurar el rumbo que el acta nombra. Este
instrumento barre LOS RUMBOS ENTEROS del fichero, cuenta cuantos traen alguna
ancla repetida, los nombra uno a uno, y publica la cifra ANTES y DESPUES. Si el
acta hubiera nombrado uno y hubiera dos, se veria aqui.

EL ORDEN SE CONSERVA. La depuracion es de PRIMERA APARICION: se conserva el
primer ejemplar de cada id en el orden en que ya estaba y se quitan los
repetidos posteriores. Ningun ancla cambia de sitio ni se reordena la lista.

LAS GUARDAS, y ninguna tiene rama por defecto:
  1. si el fichero no trae la lista de rumbos, es ROJO y no se escribe nada;
  2. si NO hay ninguna ancla repetida, no se escribe nada (idempotente): el
     instrumento re corrido sobre su propio resultado dice YA DEPURADO;
  3. tras escribir se re-lee el fichero entero: MISMO numero de rumbos, MISMAS
     claves en todos ellos, CERO anclas repetidas, y ningun rumbo distinto del
     depurado cambia ni un byte;
  4. el conjunto de ids de cada ancla se conserva: depurar quita repeticiones,
     nunca destinos.

DE ESCRITURA SOLO SOBRE scripts/rumbos/banco_rumbos.json.

Uso: python scripts/loop/vuelta72_ancla_duplicada.py [--escribir]
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BANCO = os.path.join(RAIZ, "scripts", "rumbos", "banco_rumbos.json")
NL = chr(10)

CAMPO = "ancla"
# EL RUMBO QUE EL ACTA 71 NOMBRA. No se usa para BUSCAR (el barrido es del
# fichero entero); se usa para COTEJAR que lo medido y lo dicho coinciden.
RUMBO_DEL_ACTA = "nucleo_le_sirve_a_todo_el_mundo"


def repetidas(lista):
    """Devuelve {id: veces} de los que aparecen mas de una vez."""
    cuenta = {}
    for x in lista:
        cuenta[x] = cuenta.get(x, 0) + 1
    return {k: v for k, v in cuenta.items() if v > 1}


def depurar(lista):
    """Primera aparicion gana. El orden NO se toca."""
    vistos = set()
    fuera = []
    for x in lista:
        if x in vistos:
            continue
        vistos.add(x)
        fuera.append(x)
    return fuera


def censo(rumbos):
    """Los rumbos con alguna ancla repetida, nombrados. Del fichero ENTERO."""
    fuera = []
    for r in rumbos:
        rep = repetidas(r.get(CAMPO) or [])
        if rep:
            fuera.append((r.get("id"), rep, list(r.get(CAMPO) or [])))
    return fuera


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--escribir", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("DEPURACION DEL ANCLA DUPLICADA DEL BANCO DE RUMBOS (vuelta 72, acta 71 adj. 7)")
    print("=" * 78)

    crudo_antes = io.open(BANCO, encoding="utf-8").read()
    d = json.loads(crudo_antes)
    rumbos = d.get("rumbos")
    if not isinstance(rumbos, list):
        print("ROJO: el fichero no trae una lista de rumbos. PARADA.")
        return 1
    print()
    print("  rumbos leidos del fichero : %d" % len(rumbos))
    claves_antes = {r.get("id"): sorted(r.keys()) for r in rumbos}
    print("  anclas totales (con repeticiones) : %d"
          % sum(len(r.get(CAMPO) or []) for r in rumbos))

    # EL BARRIDO DEL FICHERO ENTERO, que es lo que el encargo manda publicar.
    antes = censo(rumbos)
    print()
    print("  --- CENSO DE ANCLAS REPETIDAS, SOBRE LOS %d RUMBOS ---" % len(rumbos))
    print("     rumbos con alguna ancla repetida : %d" % len(antes))
    for rid, rep, lista in antes:
        print("       %s -> %s" % (rid, rep))
        print("          ancla entera: %s" % lista)

    # EL COTEJO CON LO QUE EL ACTA DICE. No decide nada; DECLARA si calza.
    nombrados = [rid for rid, _, _ in antes]
    print()
    print("  el acta 71 nombra : %s" % RUMBO_DEL_ACTA)
    print("  lo medido nombra  : %s" % (nombrados if nombrados else "ninguno"))
    print("  calza exactamente : %s" % ("SI" if nombrados == [RUMBO_DEL_ACTA] else "NO"))

    # GUARDA 2: idempotencia.
    if not antes:
        print()
        print("YA DEPURADO: cero anclas repetidas en los %d rumbos. No se escribe nada."
              % len(rumbos))
        return 0

    quitadas = sum(sum(v - 1 for v in rep.values()) for _, rep, _ in antes)
    print()
    print("  la depuracion quita %d entrada(s) repetida(s) y CERO destinos" % quitadas)
    if not a.escribir:
        print()
        print("  SIMULACION (sin --escribir): no se toca el fichero.")
        print("FIN")
        return 0

    destinos_antes = {r.get("id"): set(r.get(CAMPO) or []) for r in rumbos}
    otros_antes = {r.get("id"): json.dumps(r, sort_keys=True, ensure_ascii=False)
                   for r in rumbos if r.get("id") not in nombrados}
    for r in rumbos:
        if r.get("id") in nombrados:
            r[CAMPO] = depurar(r.get(CAMPO) or [])

    with io.open(BANCO, "w", encoding="utf-8", newline=NL) as fh:
        json.dump(d, fh, ensure_ascii=False, indent=2)
        fh.write(NL)

    # GUARDA 3 y 4: se re-lee entero.
    print()
    print("GUARDAS TRAS ESCRIBIR")
    d2 = json.loads(io.open(BANCO, encoding="utf-8").read())
    rumbos2 = d2.get("rumbos")
    print("  rumbos antes %d, despues %d" % (len(rumbos), len(rumbos2)))
    claves_despues = {r.get("id"): sorted(r.keys()) for r in rumbos2}
    iguales = claves_antes == claves_despues
    print("  las claves de los %d rumbos son las MISMAS : %s"
          % (len(rumbos2), "OK" if iguales else "ROJO"))
    despues = censo(rumbos2)
    print("  rumbos con alguna ancla repetida, DESPUES  : %d %s"
          % (len(despues), "OK" if not despues else [x[0] for x in despues]))
    destinos_despues = {r.get("id"): set(r.get(CAMPO) or []) for r in rumbos2}
    mismos = destinos_antes == destinos_despues
    print("  el CONJUNTO de destinos de cada ancla es el MISMO : %s"
          % ("OK" if mismos else "ROJO"))
    otros_despues = {r.get("id"): json.dumps(r, sort_keys=True, ensure_ascii=False)
                     for r in rumbos2 if r.get("id") not in nombrados}
    movidos = [k for k in otros_antes if otros_antes[k] != otros_despues.get(k)]
    print("  otros rumbos movidos : %d %s" % (len(movidos), "OK" if not movidos else movidos))
    for rid, _, lista in antes:
        nuevo = [r for r in rumbos2 if r.get("id") == rid][0][CAMPO]
        print("  %s : %d anclas antes, %d despues -> %s"
              % (rid, len(lista), len(nuevo), nuevo))

    ok = (iguales and not despues and mismos and not movidos
          and len(rumbos) == len(rumbos2))
    print()
    print("VERDE" if ok else "ROJO")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
