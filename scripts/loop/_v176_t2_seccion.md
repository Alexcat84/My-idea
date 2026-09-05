### TAREA 2. ABRIR Y CERRAR ESTE MISMO REPORTE, EN LA MISMA VUELTA

**EL REPORTE SE ABRIO AL EMPEZAR Y CRECIO POR ANEXION**, y esta fila es prueba de
que llego al final. El esqueleto lo tallo
`scripts/loop/vuelta176_esqueleto_reporte.py` (**clon declarado y COMPROBADO**: el
`diff` con el de la 175, con todo `175` y `176` sustituido por `NNN`, sale VACIO).

**ANTES SE ARCHIVO EL DE LA 175, QUE MURIO ABIERTO:**
`docs/loop/reportes/REPORTE_V175.md`, **5953 bytes, 69 lineas, sha256 `10f1d838`**,
leido de git y no del arbol. **Un reporte que murio abierto es texto igual, y se
archiva igual.**

**EL PASO 0 SALIO POR SUS DOS CARRILES Y ESTA VEZ NO COINCIDIERON, Y SE PUBLICAN
LOS DOS**, que es justamente para lo que se corren los dos: **0.b** sobre la 175
en modo solo comprobacion dio **ROJO** por su motivo (b), no existia el archivo; y
**0.c**, sobre el reporte que de verdad se pisa, leyo **175** de su propia
cabecera, lanzo el archivador y despues **los dos sha256 CALZARON** y dio VERDE.
**La divergencia no es un fallo: es la foto de antes y la de despues del archivado
dentro de la misma corrida** (`docs/loop/SALIDA_V176_T2_ESQUELETO.txt`).

**LA RACHA DE `AUDITOR.md` 6.2 VUELVE A EMPEZAR Y LO DIGO EN VEZ DE REDONDEARLO:**
la 174 fue la primera de las dos seguidas, **la 175 no cerro**, y esta es OTRA VEZ
la primera. **La segunda tendra que ser la 177.**

**EL CUERPO DEL CIERRE TAMBIEN SE TALLA DESDE ESTA VUELTA.** Hasta ahora
`cerrar_reporte.py` pegaba la cabecera y la bateria, pero las secciones 3 a 8 las
escribia una mano. Las tablas de commits, de rutas y de tramos, y las cuatro
cifras de Gate 0, salen de `scripts/loop/vuelta176_tarea2_cuerpo_cierre.py`, que
**CAE EN ROJO y no escribe nada si le falta cualquiera de los ficheros de los que
lee**, en vez de rellenar el hueco con una frase.
