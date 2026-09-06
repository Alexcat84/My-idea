#!/bin/sh
# vuelta190_cerrar.sh . EL CIERRE DEL REPORTE DE LA VUELTA 190, EN UNA SOLA ORDEN
# Y REPETIBLE.
#
# POR QUE EXISTE, Y LA CAUSA ES DE ESTA MISMA VUELTA: `cerrar_reporte.py` lleva
# cuatro argumentos largos y dos de ellos son parrafos enteros (el veredicto y la
# atribucion del hueco). Tecleados a mano en cada intento, la orden NO SE PUEDE
# REPETIR IGUAL, y una orden que no se puede repetir no se puede auditar. Aqui
# queda escrita entera, con sus dos parrafos literales, y el auditor puede
# correrla tal cual.
#
# LO QUE ESTE FICHERO NO HACE: no toca el reporte, no mide nada y no decide nada.
# Solo llama a `scripts/loop/cerrar_reporte.py` con sus argumentos.
#
# USO:
#   sh scripts/loop/vuelta190_cerrar.sh

set -e

VEREDICTO='**EL VEREDICTO DE UNA LINEA: LAS CINCO TAREAS CERRARON Y VOLVIO EL TOPE DE CINCO, LA GUARDA DEL SUJETO CONGELADO ESTA DE VUELTA EN EL VEREDICTO Y ESA TAREA CIERRA EN ROJO POR DEUDA DECLARADA CON EXITCODE 2 SIN QUE SE AFLOJE NINGUNA GUARDA, EL EXITCODE DE LA BATERIA YA SEPARA EL ARNES CAIDO DE LA DEUDA Y LA BATERIA RESTAURA SOLA LAS SALIDAS SELLADAS AJENAS QUE PISA, LA RELECTURA AL DOBLE DEL TRAMO DEL 2422 SE HIZO CON 20 COINCIDENCIAS Y 10 DISCREPANCIAS DE LAS QUE UNA CAE FUERA DE MIS DUDOSOS Y LA TRAIGO ENTERA, Y LA SEDE DE OP-L-02 SE BUSCO SIN INVENTARLA: LAS TRES NOMINAS SI LA TIENEN Y LO QUE FALTA SE ELEVA.**'

ATRIBUCION='por AUDITOR.md 6.1, decision del fundador del 5 sep 2026, la bateria de mutaciones corre CADA CINCO VUELTAS en una vuelta propia que no lleva nada mas. La 189 la corrio ENTERA: sus diez tramos siguen sellados en disco y el bloque H.5 del sello de apertura de esta vuelta los remidio uno a uno, por las dos convenciones, en disco y normalizado a LF, antes de tocar nada. Por esa cadencia LA SIGUIENTE VUELTA DE BATERIA ES LA 194, y esta vuelta NO es de bateria: su encargo se lo dice con esas palabras. Lo que esta vuelta SI hizo sobre la bateria es arreglar su lanzador en la TAREA 3, sin correr ni un tramo: --plan y --siguiente son las dos unicas ordenes suyas que se invocaron y ninguna sella salida de tramo ni corre ningun arnes. La nomina cierra en 127 entradas, arneses_que_faltan() en 0, o sea que la 194 la encontrara completa.'

python scripts/loop/cerrar_reporte.py \
  --vuelta 190 \
  --cuerpo scripts/loop/_v190_cierre_texto.md \
  --tallador docs/loop/SALIDA_V190_TALLADOR_CABECERA.txt \
  --bateria docs/loop/SALIDA_V190_BATERIA.txt \
  --veredicto "$VEREDICTO" \
  --hueco-atribucion "$ATRIBUCION"
