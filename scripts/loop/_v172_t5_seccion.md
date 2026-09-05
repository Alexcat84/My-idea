### TAREA 5. EL CIERRE DEL REPORTE DEJA DE SER UN PASO A MANO

**NACE `scripts/loop/cerrar_reporte.py`, DE NOMBRE ESTABLE Y SIN NUMERO DE
VUELTA** (adjudicacion 6.6 del acta 171), como sus hermanos
`paso0_archivar_anterior.py`, `tallar_cabecera_reporte.py`,
`archivar_reporte.py`, `serie_de_registros.py` y `aislador_de_ciega.py`, **para
que el proximo clon no lo pierda**. Su plano es
`vuelta171_tarea1b_cerrar_reporte_170.py`, que ya sabia hacer esto para un
reporte ajeno; lo que cambia es que aqui **esta parametrizado** y **cae en rojo**.

**LA CAUSA QUE LO PIDE ESTA MEDIDA Y NO SUPUESTA:** `vuelta171_cierre.py` **solo
mide**, escribe once ficheros `SALIDA_*` y **no toca `REPORTE.md` en ninguna
linea**. Cerrar el reporte era un paso a mano que venia despues, y **ahi cayeron
las dos ultimas vueltas**. El clon de esta vuelta, `vuelta172_cierre.py`, lo dice
en su propia cabecera para que nadie vuelva a confiarse.

**LO QUE HACE, EN UN SOLO ACTO:** pega la cabecera leyendola del fichero del
tallador (ninguna celda tecleada), anexa el cuerpo del cierre comprobando su
sha256, escribe la seccion 9 **con la salida de la bateria entera dentro**,
escribe el veredicto de una linea, y **relee del disco**.

**Y CAE EN ROJO SI AL TERMINAR FALTA CUALQUIERA DE LAS CUATRO PIEZAS:**

| pieza | que exige |
|---|---|
| **(1)** veredicto escrito | el *"SIN ESCRIBIR TODAVIA"* ya no esta y hay veredicto en su sitio |
| **(2)** cabecera pegada | el hueco *"PENDIENTE DE TALLAR"* ya no esta **y** todas las filas del tallador estan dentro, byte a byte |
| **(3)** secciones 3 a 9 | las siete existen |
| **(4)** bateria dentro de la 9 | la salida de la bateria de ESTA vuelta esta dentro de la seccion 9, entera y no vacia |

**LAS CUATRO VIVEN EN UNA FUNCION PURA, `piezas_que_faltan(texto, filas,
lineas)`, Y NO DENTRO DEL CUERPO QUE ESCRIBE.** El motivo es el mismo que en la
TAREA 2.a: **una guarda que no se puede llamar no se puede probar por
mutacion**.

**EL CASO POSITIVO POR MUTACION:**
`scripts/loop/vuelta172_tarea5_mutacion_cierre.py`, salida
`docs/loop/SALIDA_V172_T5_MUTACION_CIERRE.txt`, **exit 0**: **17 casos, 17
pasan, 17 caen al mutar el esperado**. Prueba exactamente lo que el encargo pide
y dos cosas mas:

- **se quita una pieza a una y la que falta sale NOMBRADA por su numero**;
- **los casos tramposos**: el hueco de la cabecera quitado **pero las filas sin
  pegar** sigue siendo falta de la **(2)**; una bateria **recortada** dentro de
  la seccion 9 sigue siendo falta de la **(4)**; una bateria de cero lineas y un
  tallador sin filas tambien;
- **el escenario real del principio**: un esqueleto recien tallado, que es lo que
  las vueltas 170 y 171 dejaron commiteado, **falla las cuatro**. Si este
  instrumento hubiera existido, **habria salido ROJO en vez de callar**.

**SUJETO CONGELADO:** todos los reportes de mentira son cadenas literales del
proceso, **cero lecturas de disco y cero escrituras**.

**Y ESTA VUELTA SE CIERRA CON EL, QUE ES LA UNICA FORMA DE SABER SI SIRVE.** Su
corrida y su veredicto viven en `docs/loop/SALIDA_V172_T5_CERRAR_REPORTE.txt`, y
si esa salida no existe es que el instrumento no llego a correr, cosa que
tambien se sabria leyendo este mismo reporte.

**LO QUE ESTE INSTRUMENTO NO HACE, Y VA DICHO PARA QUE NO SE LE PIDA:** no talla
la cabecera, no archiva, no corre la bateria y **no anexa tareas**. Recibe lo que
otros produjeron y lo monta; si algo falta lo dice en rojo **en vez de escribir
un reporte a medias**, que es la diferencia entera con las dos vueltas
anteriores.
