### TAREA 5. MI REPORTE, Y LA GUARDA QUE ME FALTO EN LA 214

**LA CAIDA QUE REMEDIA ESTA TAREA ES MIA Y ES LA UNICA QUE ACUMULA**, y va
registrada entera en la TAREA 1.b con la linea del acta donde vive. Aqui va el
remedio, que son **DOS MITADES Y NO UNA**, y la segunda es la que importa.

#### 5.a. LA PRIMERA MITAD: LA CONSOLA SE SELLA DESDE DENTRO DEL INSTRUMENTO

**El ciclo imprime su consola por `stdout` y en la 214 nadie la redirigio.** El
encargo dice *"redirigela"*, y **acordarse de redirigir es exactamente lo que
esta casa lleva vueltas demostrando que no funciona**: por eso no la redirijo
desde fuera, **la escribe el propio instrumento**.

`scripts/loop/_v215_ciclo_gate0.py` duplica su salida con un `Tee`, la sigue
imprimiendo por pantalla, y **la escribe en el nombre exacto que el compositor
busca**, compuesto del numero de vuelta que sale del nombre del fichero y del
lado que llega por argumento. **Y si el fichero saliera de CERO BYTES, el propio
ciclo sale en rojo**, porque una salida sellada de cero bytes no cuenta como
hecha (`EJECUTOR.md` 1).

**MEDIDO:** `docs/loop/SALIDA_V215_CICLO_GATE0_APERTURA_CONSOLA.txt` existe, mide **912 bytes**, y publica **PEOR
EXITCODE DE LOS OCHO: 0**. **El lado CIERRE se sella igual al cerrar la
vuelta, y sus dos filas van en la seccion 3.1.**

#### 5.b. LA SEGUNDA MITAD, Y ES LA QUE IMPORTA: EL COMPOSITOR REVIENTA

**Lo que el acta 214 senala no es la celda vacia: es que mi compositor
ESCRIBIERA UNA FILA EN BLANCO Y SIGUIERA.** Eso es degradacion silenciosa, que es
lo que el banco 9 prohibe.

**LA DIFERENCIA NO ES UNA PROMESA, ES CODIGO, Y SE LEE DE LOS DOS FICHEROS:**

- El de la 214, **scripts/loop/_v214_cierre_texto.py linea 78: filas_gate.append("| **%s** | (sin fichero de consola) | | |" % lado)**
- El mio: **no tiene esa rama**. `fila_de_gate()` devuelve `(None, motivo)` y
  quien la llama **acumula el fallo duro y sale con exitcode 1 sin escribir una
  sola linea del cuerpo**.

**LA PRUEBA DE MUTACION, QUE VA DELANTE Y NO DETRAS** (`docs/loop/SALIDA_V215_T5_MUTANTES.txt`). Se muta **la
entrada de la funcion pura**, no el repo: ningun fichero se toca, ni se borra, ni
se renombra.

**FILAS ARMADAS: 4. FILAS QUE DEBERIA HABER: 4.**

| caso | que se le da a la guarda | da fila | se esperaba | veredicto |
|---|---|---|---|---|
| **LITERAL DE LA VUELTA 214** | LITERAL DE LA VUELTA 214 | NO | NO | **CALZA** |
| **B** | EL FICHERO EXISTE PERO NO TRAE NI UNA LINEA CON EXITCODE | NO | NO | **CALZA** |
| **C** | TRAE EXITCODES PERO NO SU PEOR EXITCODE | NO | NO | **CALZA** |
| **D** | LA CONSOLA DE VERDAD DE ESTA VUELTA, QUE TIENE QUE DAR FILA | SI | SI | **CALZA** |

**Y LA CIFRA QUE DE VERDAD MIDE EL REMEDIO, PORQUE UNA FILA CON CELDAS VACIAS
SIGUE SIENDO UNA FILA:** **CIFRA casos malos que AUN ASI producen una fila:
0** (se exige 0). **CIFRA casos malos que revientan CON SU MOTIVO
ESCRITO: 3 de 3**, porque reventar sin decir por que es la otra
mitad de la misma enfermedad.

**EL CASO `A` ES EL DE LA 214 LITERAL:** fichero que no existe. **Hoy no da fila,
da un rojo con su motivo.**

**Y ESTO NO FABRICA MAQUINARIA**, que es lo que la moratoria protege: el
compositor de cierre **se escribe cada vuelta de todas formas**, lleva prefijo de
guion bajo, **muere con la vuelta** y no entra en ninguna nomina. **Lo unico que
cambia es que falle ruidoso.**

**LA GUARDA NO SE QUEDO EN EL CIERRE:** los compositores de las TAREAS 3 y 4
llevan la misma negativa a rellenar, y **la de la TAREA 3 me mordio de verdad**
en su primera corrida (su lector de las cuatro clases del marcador devolvia
vacio, y **no escribio nada**).

#### 5.c. LA SECCION 9 CIERRA CON LA BATERIA CORRIDA, NO CON HUECO

**Esta es su vuelta y la bateria corrio.** La seccion 9 la talla
`scripts/loop/cerrar_reporte.py` con la salida compuesta de los once tramos
dentro, y **no lleva hueco declarado**, porque no hay hueco que declarar.

**LO QUE SI LLEVA, Y NO ES LO MISMO QUE UN HUECO:** los once tramos salen en
**exitcode 1**, y eso va dicho en la seccion 5 como **PARADA 2**, con su
contradiccion nombrada y sin que yo elija cual de las dos reglas cede. **Una
bateria corrida con su rojo dicho no es una bateria sin correr.**
