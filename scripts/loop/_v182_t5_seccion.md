### TAREA 5. LA BATERIA DE LA 183, PREPARADA Y DECLARADA, Y NO CORRIDA

**`scripts/loop/vuelta183_bateria_por_tramos.py`** (**23.847 bytes en disco**),
**clon declarado** de `scripts/loop/vuelta176_bateria_por_tramos.py`, que es **el
precedente que la propia decision del fundador cita**. Cotejo del clon en
`docs/loop/SALIDA_V182_T5_COTEJO_CLON_BATERIA.txt` (**7.017 bytes**): **52
sentencias de codigo y 4 literales de texto**. **No sale vacio y no se dice que
salga**: el docstring entero cambia, el `TAMANO` cambia y el carril `--siguiente`
es nuevo.

**EL REPARTO, COMPUTADO Y NO TECLEADO** (`--plan`, salida en
`docs/loop/SALIDA_V182_T5_PLAN_BATERIA_183.txt`, **5.820 bytes**): **109 entradas
de nomina**, **tramo de 13**, **9 tramos**, y **la suma de las entradas de todos
los tramos es 109**, o sea que no se cae ni se repite ninguna. **Los nueve no son
un numero elegido: son los del precedente de la 176**, y el `TAMANO` es lo que se
ajusta para que salgan nueve, no al reves.

**LA ESTIMACION DEL RELOJ, DICHA COMO ESTIMACION Y NO COMO MEDICION**, con las
cifras del propio archivo: **entre 4,3 y 5,6 minutos por tramo** y **entre 36,0 y
46,9 minutos la nomina entera**. **La medicion de verdad la da cada tramo al
cerrarse.**

**EL CARRIL NUEVO `--siguiente` ES LA MITAD EN CODIGO DE "RETOMA EN EL TRAMO
SIGUIENTE".** El lanzador de la 176 ya era resumible de hecho, porque cada tramo
se corre con `--tramo N`; pero **saber cual tocaba era cosa de acordarse**, y
acordarse es lo que esta casa lleva vueltas demostrando que no funciona. Corrido
hoy (`docs/loop/SALIDA_V182_T5_SIGUIENTE_TRAMO.txt`, **1.178 bytes**): **9 tramos
del reparto, 0 con salida sellada, 9 faltan, EL SIGUIENTE ES EL TRAMO 1.**

> **Y UNA SALIDA SELLADA QUE MIDE CERO BYTES NO CUENTA COMO HECHA.** No es
> severidad: la bateria del ejecutor salio en **cero bytes tres vueltas seguidas**
> (171, 172 y 173) y esa es media causa del regimen entero de `AUDITOR.md` 6.1.
> Por la letra del 5 sep 2026, **una ruta que promete prueba y mide cero bytes es
> caida de cifra**.

**LO QUE ESTA VUELTA NO HACE CON ESTO, Y ES LO QUE SU ENCARGO MANDA:** *"Aqui solo
se deja preparada y declarada"*. Lo unico que se corrio de este fichero es
`--plan` y `--siguiente`, que **no tocan la nomina, no corren ningun arnes y no
escriben ninguna salida de bateria**. **No hay ninguna corrida de bateria en esta
vuelta**, y por eso la seccion 9 de este reporte cierra con su **hueco declarado y
medido**, que es lo que el regimen 6.1 manda para las vueltas intermedias.

**Y LA NOMINA CRECIO DENTRO DE ESTA MISMA VUELTA, con su corte al lado:** de
**108** a **109** entradas, por el arnes de la `P.1` que la TAREA 1.b remedio y
renombro. **La cifra de 109 es la de esta corrida de `--plan`, tomada al cierre y
no en la apertura**, porque la propia vuelta la movio.
