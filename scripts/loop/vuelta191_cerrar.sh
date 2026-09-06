#!/bin/sh
# vuelta191_cerrar.sh . EL CIERRE DEL REPORTE DE LA VUELTA 191, EN UNA SOLA ORDEN
# Y REPETIBLE.
#
# POR QUE EXISTE: `cerrar_reporte.py` lleva cuatro argumentos largos y dos de
# ellos son parrafos enteros (el veredicto y la atribucion del hueco). Tecleados
# a mano en cada intento, la orden NO SE PUEDE REPETIR IGUAL, y una orden que no
# se puede repetir no se puede auditar. Aqui queda escrita entera, con sus dos
# parrafos literales, y el auditor puede correrla tal cual.
#
# Y DESDE ESTA VUELTA, EL VEREDICTO VA SIN VESTIR: la guarda nueva de la TAREA 4
# (`veredicto_ya_viene_vestido`) CAE EN ROJO si el `--veredicto` llega con la
# etiqueta `EL VEREDICTO DE UNA LINEA:` o con los asteriscos ya puestos. El de la
# vuelta 190 los llevaba, y por eso su reporte salio con la etiqueta duplicada.
# ESTE NO LOS LLEVA, y esa es la prueba de que la guarda esta puesta y de que
# quien la escribio la cumple.
#
# LO QUE ESTE FICHERO NO HACE: no toca el reporte, no mide nada y no decide nada.
# Solo llama a `scripts/loop/cerrar_reporte.py` con sus argumentos.
#
# USO:
#   sh scripts/loop/vuelta191_cerrar.sh

set -e

VEREDICTO='LAS CINCO TAREAS CERRARON SIN MOVER UN SOLO VEREDICTO DEL ARCHIVO, QUE ABRE Y CIERRA EN 0a77b5a35a962621 POR LAS DOS CONVENCIONES. EL ACTA 191 ENTRA COMO R.53 Y EL REGISTRADOR APRENDIO A LEER UN CERO DE EN CONTRA SIN ROMPERSE Y A CONTAR CAIDAS QUE NO SE LLAMAN C.n; EL AL DOBLE DEL 3182 SE LEYO A CIEGAS CON 23 QUE COINCIDEN Y 7 QUE DISCREPAN, Y LA UNICA QUE CAE FUERA DE MIS DUDOSOS, EL 2832, LA TRAIGO ENTERA Y NO ME AUTO ENCARGO SU ESCALADA; LAS DOS CONVENCIONES DE LINEAS SE MIDIERON PRIMERO (12 EN ROJO) Y SE ARREGLARON DESPUES (0 EN ROJO) CON SU GUARDA APLICADA A QUIEN LA ESCRIBIO; cerrar_reporte.py YA CAE EN ROJO SI EL VEREDICTO LLEGA VESTIDO, Y LA MEDICION DESTAPA QUE EL REPORTE DE LA 188 TAMBIEN LO TRAIA, QUE ES LA PARADA QUE DECLARO; Y LA MARCA CONTRA LA DIFICULTAD TIENE SU UNIVERSO DECLARADO Y SUS TRES CIFRAS, Y NO ALCANZAN PARA CONCLUIR, QUE ES UN RESULTADO. LAS SEIS CAIDAS PROPIAS SON DE METODO Y NINGUNA LLEGO A PUBLICAR UNA CIFRA FALSA, INCLUIDA LA MAS GORDA: MI PROPIA PROSA PUBLICABA 22 CIFRAS DE BYTES SIN SU PAREJA Y EL CERRADOR SE NEGO A ESCRIBIR HASTA QUE LAS ARREGLE.'

ATRIBUCION='por AUDITOR.md 6.1, decision del fundador del 5 sep 2026, la bateria de mutaciones corre CADA CINCO VUELTAS en una vuelta propia que no lleva nada mas. La 189 la corrio ENTERA y sus diez tramos siguen sellados en disco. Por esa cadencia LA SIGUIENTE VUELTA DE BATERIA ES LA 194, y esta vuelta NO es de bateria: su encargo se lo dice con esas palabras y su sello de apertura lo escribe en la primera linea. Lo que esta vuelta SI hizo tocando el radio de la bateria es NO tocarla: la TAREA 3 comprobo contra verificar_mutaciones_viejas.VIEJAS, 127 entradas leidas del instrumento, que NINGUNO de los doce ficheros que arreglo esta en la nomina, y salto expresamente vuelta183_tarea1b_mutacion_atribucion.py, que si lo esta, porque cambiar lo que imprime habria movido una salida sellada que la 194 compara byte a byte. La nomina no se podo, que es la opcion c que el fundador RECHAZO el 5 sep 2026, y sigue en 127 entradas, asi que la 194 la encontrara completa.'

python scripts/loop/cerrar_reporte.py \
  --vuelta 191 \
  --cuerpo scripts/loop/_v191_cierre_texto.md \
  --tallador docs/loop/SALIDA_V191_TALLADOR_CABECERA.txt \
  --bateria docs/loop/SALIDA_V191_BATERIA.txt \
  --veredicto "$VEREDICTO" \
  --hueco-atribucion "$ATRIBUCION"
