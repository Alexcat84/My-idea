# -*- coding: utf-8 -*-
"""vuelta138_3_pieza_de_varios_duenos.py . MIDE UN HUECO DEL CONTRATO DE MARCAS
QUE APARECE AL SENTAR LA PRIMERA MESA DE LA FASE 06.

EL HUECO, dicho antes de medirlo. El contrato de marcas del ejecutor tiene TRES
destinos para una pieza del nodo que muere, y solo tres:
  APPEND            . viaja entera como paso nuevo del superviviente
  CUBIERTO:n        . ya lo dice el paso n DEL SUPERVIVIENTE
  CUBIERTO_COND:n   . ya lo dice la condicion n DEL SUPERVIVIENTE
  INCISO:n|trozo|nexo . se adosa al paso n DEL SUPERVIVIENTE
Los cuatro miran AL SUPERVIVIENTE, y los cuatro se validan contra el numero de
pasos que el superviviente tiene ANTES de la fusion (en
generar_plan_de_fusion_de_mesa.py: "1 <= k <= n_sup_pasos", con n_sup_pasos
medido del nodo sin tocar).

NO HAY NINGUN DESTINO QUE DIGA "ESTA PIEZA YA VIAJA EN ESTE MISMO ACTO, POR OTRO
ABSORBIDO". Con UN solo absorbido ese destino no hace falta y por eso nadie lo
echo de menos: las TRES fusiones de mesa que la campana ha ejecutado
(OP-M-02-PROG, OP-M-03-I y OP-M-03-II) tienen un absorbido cada una. Con dos o
mas, y con una pieza que el superviviente NO tiene y que DOS O MAS de los que
mueren SI, las tres salidas son las tres malas:
  APPEND en los dos     . el superviviente acaba con el mismo gesto dos veces;
  CUBIERTO:n en el otro . afirma del superviviente algo que el superviviente no
                          dice, que es exactamente la mentira callada que la
                          casa persigue;
  INCISO al paso nuevo  . lo prohibe la guarda del generador, porque el paso
                          nuevo todavia no existe cuando el plan se sella.

COMO SE MIDE, y se mide del texto de la ficha, no de una impresion: el campo
`preservar` de cada operacion nombra las piezas que VIAJAN, y muchas lineas dicen
de quien son NOMBRANDO EL ID del absorbido. Aqui se cuenta, para cada linea,
cuantos ids de absorbido de la PROPIA ficha aparecen EN LA LINEA ENTERA. Dos o mas
ids es una pieza que cae en el hueco.

LA PRIMERA VERSION DE ESTE FICHERO SOLO MIRABA LA CABEZA DE LAS LINEAS QUE
EMPIEZAN POR "VIAJA, de ", Y SUB-CONTABA. Corrida asi daba UNA sola pieza en el
hueco, la de OP-M-01-FUSION, y se dejaba fuera al menos la de OP-M-05-APERTURA
("de introduccion_validacion_clientes y filosofia_customer_validation: probar que
el proceso de venta SE REPITE..."), que no empieza por "VIAJA". Se corrige y se
declara: una busqueda negativa no se puede citar (EJECUTOR regla 9), y un cero que
sale de mirar donde no es, es peor que no medir.

Y EL LIMITE QUE QUEDA, DICHO EN VEZ DE CALLADO: hay lineas de `preservar` que
nombran a los duenos EN PROSA y no por id, como la de OP-M-05-INDICE ("LAS CUATRO
FASES ENUMERADAS del descubrimiento, que es lo que LOS DOS INDICES aportan y el
superviviente no lleva"). Ningun contador de ids las puede ver. Por eso este
fichero NO publica un cero para ellas: las saca en una lista aparte, SIN
CLASIFICAR POR ID, para que se lean con el ojo antes de fundir. El cero que este
instrumento puede sostener es "cero lineas que NOMBREN dos absorbidos", nunca
"cero piezas de varios duenos".

NO DECIDE NADA Y NO TOCA NADA. Mide, nombra y sale.

CASO ROJO, y es REAL, no fabricado: OP-M-01-FUSION tiene una linea de
`preservar` que dice literalmente "VIAJA, de requisitos_gates_con_dientes y
estructura_gates y estructura_de_gates: LOS ENTREGABLES CLAROS Y ESTANDARIZADOS
con sus plantillas. El superviviente NO los tiene y los tres que mueren si". La
propia ficha declara las dos mitades del hueco: TRES duenos y el superviviente
NO la tiene. La prueba de mutacion va sobre la cifra COMPUTADA `duenos`, no
sobre un literal: con --mutar-umbral se exige 1 dueno en vez de 2 y el reparto
de piezas cambia, lo que ensena que la cuenta sale del texto y no de una tabla
escrita a mano.

USO:
  python scripts/loop/vuelta138_3_pieza_de_varios_duenos.py
  python scripts/loop/vuelta138_3_pieza_de_varios_duenos.py --mutar-umbral
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPERACIONES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")

LAS_SEIS = ["OP-M-01-FUSION", "OP-M-02-ACCLIMATE", "OP-M-03-III",
            "OP-M-05-INDICE", "OP-M-05-EDIFICIO", "OP-M-05-APERTURA"]


def fichas():
    d = {}
    for l in io.open(OPERACIONES, encoding="utf-8"):
        if not l.strip():
            continue
        x = json.loads(l)
        d[x.get("id_op")] = x
    return d


def duenos_de_la_linea(linea, absorbidos):
    """Cuantos ABSORBIDOS de la ficha nombra la linea ENTERA, por su id."""
    return [ab for ab in absorbidos if ab in linea]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutar-umbral", dest="mutar", action="store_true",
                    help="exige 1 dueno en vez de 2: la cuenta tiene que cambiar")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    umbral = 1 if a.mutar else 2
    print("=" * 78)
    print("PIEZAS DE VARIOS DUENOS EN LAS SEIS FUSIONES DE LA FASE 06")
    print("  umbral de duenos para caer en el hueco: %d o mas" % umbral)
    if a.mutar:
        print("  MODO MUTACION: umbral bajado a 1. La cuenta TIENE QUE CAMBIAR.")
    print("=" * 78)

    F = fichas()
    total_en_el_hueco = 0
    por_op = []
    for id_op in LAS_SEIS:
        op = F.get(id_op)
        if op is None:
            print("  ROJO: %s no esta en OPERACIONES.jsonl" % id_op)
            return 1
        absorbidos = list(op.get("eliminar") or [])
        preservar = list(op.get("preservar") or [])
        print("")
        print("-" * 78)
        print("%s  | absorbidos %d | lineas de preservar %d"
              % (id_op, len(absorbidos), len(preservar)))
        en_el_hueco = 0
        sin_id = []
        for linea in preservar:
            d = duenos_de_la_linea(linea, absorbidos)
            if not d:
                sin_id.append(linea)
            if len(d) >= umbral:
                en_el_hueco += 1
                pieza = linea.split(":", 1)[1].strip() if ":" in linea else linea
                print("  PIEZA DE %d DUENO(S): %s" % (len(d), ", ".join(d)))
                print("      %s" % pieza[:150])
        if not preservar:
            print("  (la ficha no trae campo preservar)")
        print("  lineas que NOMBRAN %d o mas absorbidos: %d" % (umbral, en_el_hueco))
        if sin_id:
            print("  LINEAS SIN NINGUN ID DE ABSORBIDO, no clasificables por maquina,")
            print("  SE LEEN CON EL OJO ANTES DE FUNDIR (%d):" % len(sin_id))
            for l in sin_id:
                print("      %s" % l[:150])
        total_en_el_hueco += en_el_hueco
        por_op.append((id_op, len(absorbidos), len(preservar), en_el_hueco, len(sin_id)))

    print("")
    print("=" * 78)
    print("  %-20s %-11s %-10s %-13s %s"
          % ("OPERACION", "ABSORBIDOS", "PRESERVAR", "NOMBRAN 2+", "SIN ID (a leer)"))
    for id_op, na, npres, nh, ns in por_op:
        print("  %-20s %-11d %-10d %-13d %d" % (id_op, na, npres, nh, ns))
    print("")
    print("CIFRA lineas de preservar que nombran dos o mas absorbidos: %d lineas"
          % total_en_el_hueco)
    print("CIFRA lineas de preservar sin ningun id, que la maquina NO clasifica: %d lineas"
          % sum(ns for _, _, _, _, ns in por_op))
    bloqueadas = [o for o, _, _, nh, _ in por_op if nh]
    print("CIFRA operaciones con al menos una pieza en el hueco: %d grupos" % len(bloqueadas))
    print("  son: %s" % (", ".join(bloqueadas) if bloqueadas else "ninguna"))
    print("")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
