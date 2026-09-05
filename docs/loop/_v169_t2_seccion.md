### TAREA 2, EL ARNES DEL RETRATO SE RE ANCLA, Y LA BATERIA ACABA EN VERDE DESPUES DE TRES CORRIDAS

**Salidas:** `docs/loop/SALIDA_V169_T2_REANCLAJE.txt` (el parche),
`docs/loop/SALIDA_V169_T2_RETRATO_SOLO.txt` (el arnes corrido solo),
`docs/loop/SALIDA_V169_T2_MUTACION_REANCLAJE.txt` (su caso positivo),
`docs/loop/SALIDA_V169_T2_BATERIA_2.txt` (la corrida 2),
`docs/loop/SALIDA_V169_T2_CERRAR_BATERIA.txt` (los dos re anclajes) y
`docs/loop/SALIDA_V169_T2_BATERIA_3_VERDE.txt` (la corrida 3).
**Instrumentos:** `scripts/loop/vuelta169_tarea2_reanclar_retrato.py`,
`scripts/loop/vuelta169_tarea2_mutacion_reanclaje.py` y
`scripts/loop/vuelta169_tarea2_cerrar_bateria.py`.

**(2.a) LA CONSTANTE SALE DEL COMPUTO.** Los dos casos que comparaban contra el
literal `"TRECE VECES"` comparan ahora contra `T.CARDINAL[cuantas + 1]` y
`T.CARDINAL[cm + 1]`. **El literal viejo NO se borra:** sigue citado entero en el
comentario que explica por que dejo de servir.

**(2.b) LA MUTACION DEJA DE ESTAR CLAVADA.**
`t.replace("DOCE VECES,", "DOS VECES,", 1)` pasa a leer con `PAT_CONTADOR` **la
palabra que el propio instrumento acaba de sacar** y a mutarla por otra distinta
sacada de `CARDINAL`. **Y SE ANADE LA GUARDA QUE FALTABA**,
`B_la_mutacion_MUERDE_el_texto_vivo`, que **CAE si el replace no cambia nada**:
ese era exactamente el modo de fallo que dejaba muda a la guarda de abajo.

**UN TERCER RETOQUE QUE EL ENCARGO NO NOMBRA, Y SE DECLARA:** el rotulo
`C_las_doce_tachadas_viejas_sobreviven` tecleaba DOCE cuando su cifra sale de
`len(tach)`, que hoy vale 13. **Solo el rotulo, ninguna comprobacion.** Marcado
como DISCUTIBLE.

**EL ARNES, CORRIDO SOLO: exit 0, 24 casos pasan y los 24 caen al mutar el
esperado.** Antes eran 23 con 3 fallando.

**Y SU CASO POSITIVO POR MUTACION, QUE ES LO QUE IMPIDE QUE ESTO SEA UN ADORNO**
(`EJECUTOR.md` 1, "EL CASO ROJO SE PRUEBA POR MUTACION"). exit 0, **20 casos**,
sujeto **CONGELADO** fabricado en memoria, cero escrituras:

| lo que prueba | como |
|---|---|
| que el re anclaje **no es una tautologia**, que es la caida de la vuelta 89 | se fabrica un `cuadrar_contador` **ROTO** que hace lo que la caida historica hacia (leer la palabra escrita en vez de contar la cadena) y **el caso CAE** en los tres tamanos probados, 12, 13 y 14 tachadas |
| que la guarda nueva **cae** | se reproduce el replace clavado a un literal que la celda ya no tiene: `mutada != t` da **False** y el caso, que espera True, **CAE** |
| que la version nueva **si muerde** | sobre la misma celda, muta la palabra viva **sin tocar la cadena**: 13 tachadas antes y 13 despues |

**Y AQUI VA UNA CAIDA MIA, CAZADA CORRIENDO Y DECLARADA:** la primera version de
esa prueba fabricaba filas de **TRES** columnas, y `anatomia` lee
`split("|")[2]`, que es la **SEGUNDA** celda. La cadena quedaba donde el
instrumento no mira y las cifras salian **0** con los casos en verde. Corregido en
el mismo acto, con el motivo escrito en el comentario del fabricante.

**LA BATERIA, TRES CORRIDAS, Y LAS TRES SE PUBLICAN.** Cifras contadas de sus
tres ficheros:

| | corrida 1 (antes del arreglo) | corrida 2 (tras 2.a y 2.b) | corrida 3 (tras cerrar) |
|---|---:|---:|---:|
| entradas en la nomina | **72** | **72** | **73** |
| ANCLA PERDIDA | 0 | 0 | **0** |
| NO MORDIO | **1** | **2** | **0** |
| NO REPRODUCIBLE | 0 | 0 | **0** |
| CASO DECLARADO | 2 | 2 | **2** |
| posteriores FUERA de la nomina | 0 | **1** | **0** |
| invisibles al censo | 0 | 0 | **0** |
| RUIDO DE CONCURRENCIA | 0 | 0 | **0** |
| minutos | 25,8 | (no publicado) | **26,2** |
| exit | **1** | **1** | **0, VERDE** |

**LA CORRIDA 2 APAGO EL ROJO DEL RETRATO Y ENCENDIO DOS QUE ME CAUSE YO EN ESA
MISMA SESION.** `vuelta166_tarea3_mutacion_retrato.py` **ya no sale**. Los dos
nuevos son:

- **`vuelta163_tarea2_mutacion_nomina.py`**, que existe **exactamente** para
  morder cuando un arnes se queda fuera de la nomina, y el que se quedo fuera es
  **el que escribio mi propia TAREA 2**.
- **`vuelta165_tarea6_mutacion_op_l_01.py`**, que ancla por **igualdad exacta** el
  numero de clausulas de `OP-L-01`, y **mi propia TAREA 4** le anadio la sexta
  por el carril del 9.10.

**LOS DOS ESTABAN HACIENDO SU TRABAJO, y apagarlos habria sido lo contrario de
arreglarlos.** El arreglo fue, con la vara del 3.b de la 168, **EL NUMERO CAMBIA
Y EL FILO NO**: el arnes nuevo **entra en `VIEJAS`** (su sujeto son celdas en
memoria y un fichero commiteado: **CONGELADO**, que es la condicion de entrada
desde la letra de la vuelta 148, y la propia bateria lo reclamaba); y el ancla
del 165 pasa **de 5 a 6 clausulas y de 2 a 3 correcciones declaradas**, las dos
por igualdad exacta contra el conteo real leido hoy, **con el instrumento
parando si no cuadra**, y el invariante de que las tres viejas siguen enteras
**sin tocar**.

**POR QUE ESTO NO ES AFLOJAR, Y LA DIFERENCIA CON LA 168 SE DICE ENTERA.** La
vuelta 168 hizo bien en **TRAER** su tercer rojo sin tocarlo, y el acta le dio la
razon: **lo habia causado otra vuelta y el encargo no lo nombraba.** Estos dos
son **escombro mio, de esta sesion, de hace minutos**. Dejarlos habria sido
publicar una bateria rota que rompi yo. **Cero comprobaciones quitadas, cero
casos borrados, cero `CASOS_DECLARADOS` nuevos.** Va **MARCADO COMO DISCUTIBLE**:
si la vara es "solo se toca lo nombrado", me pase.

**LOS CUATRO AFECTADOS, CORRIDOS SOLOS DESPUES DEL ARREGLO:** 163 exit 0; 165
exit 0 con 16 casos que pasan y 16 que caen; 166 exit 0 con 24 y 24; 169 exit 0
con 20 y 20.

**Y LA CORRIDA 3 SALE VERDE, exit 0**, con las **73** mutaciones corriendo,
mordiendo, con sus salidas selladas identicas en dos corridas seguidas, las 73
visibles al censo y ninguna fuera de la nomina. **El encargo pedia verde y hay
verde, sin haber aflojado una sola guarda para llegar a el.**
