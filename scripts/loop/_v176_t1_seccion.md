### TAREA 1. LA BATERIA ENTERA, EN TRAMOS, CON SU GUARDA DE COMMIT

**LA SALIDA UNICA, MEDIDA ANTES DE NOMBRARLA EN NINGUN SITIO** (`EJECUTOR.md` 1,
LA RUTA QUE PROMETE PRUEBA ES CIFRA): `docs/loop/SALIDA_V176_BATERIA.txt`,
**60197 bytes**. **Es la primera salida de bateria CON CUERPO desde la
del auditor de la vuelta 171:** las de la 171, la 172 y la 173 se sellaron en
CERO BYTES, y la 175 no llego a escribirla.

**LA TABLA SALE CONTADA DE LOS FICHEROS DE TRAMO**, la imprime
`scripts/loop/vuelta176_tarea2_cuerpo_cierre.py` y ninguna celda se teclea:

| tramo | fichero | bytes | lineas | entradas | minutos | exit |
|---:|---|---:|---:|---:|---:|---:|
| 1 | `SALIDA_V176_BATERIA_TRAMO_1.txt` | 7883 | 108 | 10 | 1.5 | 0 |
| 2 | `SALIDA_V176_BATERIA_TRAMO_2.txt` | 6090 | 102 | 10 | 2.6 | 0 |
| 3 | `SALIDA_V176_BATERIA_TRAMO_3.txt` | 6138 | 102 | 10 | 3.9 | 0 |
| 4 | `SALIDA_V176_BATERIA_TRAMO_4.txt` | 6177 | 102 | 10 | 15.9 | 0 |
| 5 | `SALIDA_V176_BATERIA_TRAMO_5.txt` | 6166 | 102 | 10 | 2.0 | 0 |
| 6 | `SALIDA_V176_BATERIA_TRAMO_6.txt` | 5782 | 103 | 10 | 1.6 | 1 |
| 7 | `SALIDA_V176_BATERIA_TRAMO_7.txt` | 6155 | 102 | 10 | 1.5 | 0 |
| 8 | `SALIDA_V176_BATERIA_TRAMO_8.txt` | 6180 | 102 | 10 | 1.8 | 0 |
| 9 | `SALIDA_V176_BATERIA_TRAMO_9.txt` | 5616 | 94 | 8 | 1.1 | 0 |
| **union** | `SALIDA_V176_BATERIA.txt` | **60197** |  | **88** | **31.9** |  |

**LA COBERTURA SE LEYO DE LAS SALIDAS Y NO SE RECALCULO DEL REPARTO**, que es la
diferencia entre comprobar y preguntarle al reparto por el reparto: los tramos
dicen haber corrido **88 entradas**, con **0 de la nomina sin correr, 0
ajenas y 0 repetidas** (`docs/loop/SALIDA_V176_T1E_COMPOSICION.txt`). **Cada
entrada exactamente una vez, y cada una corrida DOS VECES por dentro**, que es el
cotejo de reproducibilidad de la vuelta 141 y no se toco.

**EL VEREDICTO DE LOS 9 TRAMOS, CONTADO DE SUS FICHEROS:** ANCLA
PERDIDA **0**, NO REPRODUCIBLE **0**, RUIDO DE
CONCURRENCIA **0**, CASO DECLARADO **2**, NO MORDIO
**1**. **Ese NO MORDIO es la PARADA de la seccion 4 y se trae sin
arreglar.**

**LA GUARDA DEL COMMIT (1.a) NACIO Y MORDIO.**
`scripts/loop/guarda_commit_dataset.py`, nombre estable y sin numero de vuelta.
Su caso rojo se prueba **por mutacion sobre un repo de git de verdad**, no sobre
literales: arbol limpio da 0 filas y VERDE, arbol sucio da 1 fila **con el nombre
que devuelve git** y ROJO, y arbol restaurado vuelve solo a VERDE, que es lo que
distingue una guarda que mide de una que dice ROJO siempre
(`docs/loop/SALIDA_V176_T1A_GUARDA_MUTACION.txt`, 3 de 3).

**LA RESTAURACION AL ENTRAR (1.b) NO HIZO FALTA NI UNA VEZ, Y ESO TAMBIEN SE
MIDE.** La guarda corrio **al entrar y al salir de cada tramo**, o sea
**9 y 9 veces**, y **todas dio cero filas**. Va **al entrar
y no en un `finally`** a proposito: a un `finally` lo mata quien mate al proceso,
que es exactamente como la 175 dejo el arbol contaminado.

**EL RELOJ REAL, SUMADO DE LOS TRAMOS: 31.9 minutos**, contra la
estimacion de entre 29 y 37,8 que se publico ANTES de correr en
`docs/loop/SALIDA_V176_T1C_REPARTO.txt`.
