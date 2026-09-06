### TAREA 4. LA GUARDA DEL VEREDICTO DUPLICADO. CERRADA EN VERDE, Y CON UNA PARADA DECLARADA.

**LA CAUSA ESTABA MEDIDA Y ESTA VUELTA LA CIERRA.** `cerrar_reporte.py` componia
`"**EL VEREDICTO DE UNA LINEA: %s**"` con lo que le pasaran, **sin mirar si ya
venia puesto**, y la salida sellada de la 190 prueba que le pasaron un veredicto
que ya traia la etiqueta y sus asteriscos. Resultado: la linea 50 del reporte de
la 190 dice `**EL VEREDICTO DE UNA LINEA: **EL VEREDICTO DE UNA LINEA: LAS CINCO
TAREAS...`.

**(a) LA GUARDA, Y FALLA RUIDOSO.** `veredicto_ya_viene_vestido()` es PURA, mira
tres cosas literales y ninguna por parecido: que el `--veredicto` traiga dentro la
etiqueta, que empiece por `**`, y que termine por `**`. Corre en el bloque
**`A.1`** de `main()`, **antes de tocar nada**, y sus motivos van a `rojos`, que es
lo que impide que se escriba. **Cada motivo dice QUE RECIBIO y QUE ESPERABA**,
comprobado por el arnes. **No se limpia en silencio**, y el porque va escrito en
el propio docstring: limpiar en silencio es la otra mitad de la misma enfermedad,
porque el que la paso de mas no se enteraria nunca.

**Y SE ARREGLO LA MITAD QUE NADIE PEDIA PERO QUE HACE QUE LA GUARDA VALGA:** la
etiqueta estaba **tecleada tres veces** en el fichero (la comprobacion de estado,
la composicion final y ahora la guarda). Ahora hay **una constante**,
`ETIQUETA_VEREDICTO`, y las tres la usan. **Una guarda que vigila un literal
distinto del que se compone no vigila nada.**

**(b) EL CASO POSITIVO POR MUTACION: VERDE, 0 casos que caen y 0 mutaciones que no
cayeron**, en
`docs/loop/SALIDA_V191_T4_MUTACION_VEREDICTO.txt`
(disco 6072 bytes | LF 6072 bytes). **Dos
carriles, y ninguno sustituye al otro:**

- **EL CARRIL DE LA FUNCION PURA.** Un veredicto limpio dispara **0** motivos; con
  la etiqueta dentro, **1**; con etiqueta y asteriscos como el de la 190, **3**;
  solo con asteriscos, **2**. Y las dos mutaciones corridas: pedirle al limpio que
  dispare **CAE**, y pedirle 0 al vestido **CAE**. **Una guarda que muerde a los
  limpios no sirve, y eso se prueba en vez de decirse.**
- **EL EJEMPLAR DE VERDAD, LEIDO Y NO TECLEADO.** El veredicto que la 190 le paso
  se saca de `docs/loop/SALIDA_V190_CERRAR_REPORTE.txt` con un patron sobre su
  propia linea `el veredicto, tal como se paso:`. **La guarda lo tumba con 2
  motivos.** Si el fichero no estuviera, el bloque se declara SIN CORRER en vez de
  fabricar un ejemplar que se apruebe solo.
- **EL CARRIL DE LA MUTACION DE VERDAD, QUE ES EL QUE EL ENCARGO PIDE.** Se copia
  `cerrar_reporte.py` a un temporal y **se le QUITA la guarda** con un reemplazo
  literal, exigiendo que el trozo `rojos.extend(motivos_vestido)` aparezca
  **exactamente una vez**. Medido: **1 en la de verdad y 0 en la mutada**, y la
  mutada compila. **Lo que eso prueba y ni una palabra mas:** la version mutilada
  seguiria midiendo el veredicto y publicando sus motivos, **pero no los sumaria a
  `rojos`, o sea que cerraria el reporte igual**. Que es exactamente lo que hacia
  antes de hoy.
- **LA CAIDA REPRODUCIDA SIN TOCAR EL REPORTE:** componer con un veredicto que ya
  traia la etiqueta da **2** apariciones, que es la linea 50 de la 190.

**(c) EL REPORTE DE LA 190 NO SE REESCRIBE.** Esta cerrado y archivado byte a
byte (disco 68540 bytes | LF 68540 bytes, con `sha256` disco y `sha256` LF
iguales en `7a74fc3ccd11b769`), y **su etiqueta doble se queda
donde esta con esta explicacion al lado**. Lo que se arregla es que no vuelva a
pasar.

**PARADA. Y VA AQUI PORQUE ES UNA CIFRA PUBLICADA CON SU CORTE QUE MI MEDICION DE
HOY CONTRADICE.** El acta 191 dice en su `5.2`, literal: *"Los cinco reportes
anteriores (186 a 189) la traen UNA sola vez, o sea que no es herencia"*. **Medido
hoy fichero a fichero**, en el bloque `H.5` del sello de apertura y otra vez en el
bloque `E` del arnes de esta tarea:

| fichero | apariciones de `EL VEREDICTO DE UNA LINEA:` |
|---|---:|
| `REPORTE_V185.md` | 1 |
| `REPORTE_V186.md` | 1 |
| `REPORTE_V187.md` | 1 |
| **`REPORTE_V188.md`** | **2** |
| `REPORTE_V189.md` | 1 |
| `REPORTE_V190.md` | 2 |

**`REPORTE_V188.md` la trae DOS veces, en su linea 56.** O sea que **NO es nueva
de la vuelta 190 y SI hay herencia**: paso al menos dos veces y el cerrador la
dejo pasar las dos. **Lo declaro y no lo arreglo yo** (`EJECUTOR.md` 5), y no
reescribo el reporte de la 188, que esta cerrado. **La adjudicacion de la `5.2` no
cambia por esto**, porque el defecto y su remedio son los mismos; lo que cambia es
**cuantas veces mordio antes de que se cazara**, y eso le importa a quien lleve la
cuenta de las rachas.
