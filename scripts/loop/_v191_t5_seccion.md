### TAREA 5. LA MARCA CONTRA LA DIFICULTAD MEDIDA. CERRADA: LAS TRES CIFRAS ESTAN, Y NO ALCANZAN PARA CONCLUIR.

**NO SE ESCRIBIO NI UNA FILA DEL ARCHIVO.**
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y cierra en **disco 4054129 bytes | LF
4054129 bytes**, con `sha256` disco y `sha256` LF iguales en `0a77b5a35a962621`,
medido dentro del propio instrumento al entrar y al salir. Instrumento:
`scripts/loop/vuelta191_tarea5_marca_contra_dificultad.py`; salida:
`docs/loop/SALIDA_V191_T5_MARCA_CONTRA_DIFICULTAD.txt`
(disco 12555 bytes | LF 12555 bytes).

**(a) EL UNIVERSO SE DECLARA ANTES DE CONTAR, Y LAS DOS REGLAS ESTAN EN EL
CODIGO, NO EN LA PROSA.** Un universo elegido despues de ver el resultado no
sirve:

- **REGLA 1, LOS CANDIDATOS:** ficheros `.txt` y `.md` de `docs/loop/` cuyo
  NOMBRE contiene `COTEJO`. Son **43**, nombrados uno a uno en el bloque `B`.
- **REGLA 2, LA LEGIBILIDAD:** entra el que traiga al menos una linea con un
  numero **y** la palabra `DISCREPA` **como palabra entera** (no casa con
  `DISCREPAN` ni con `DISCREPANCIAS`), cuyo primer numero sea un puesto que
  existe en el archivo.

**Y LA REGLA DE NOMBRE TAMBIEN SE AUDITA, PARA QUE LA ELECCION DEL CANDIDATO SE
PUEDA DISCUTIR:** el bloque `C` publica los **10** ficheros de `docs/loop/` que
dicen `DISCREPA` y que la regla 1 deja fuera (`ACTA_AUDITOR.md` con 29
apariciones, cuatro destapes de ciega, y cinco sueltos). **No entran**: la regla
es la que es y no se ensancha despues de mirar.

**LOS QUE ENTRAN SON SEIS DE CUARENTA Y TRES**, y van con su cuenta:

| fichero | discrepantes | coincidentes |
|---|---:|---:|
| `SALIDA_V190_T4_COTEJO.txt` | 10 | 20 |
| `SALIDA_V191_T2_COTEJO.txt` | 7 | 23 |
| `_auditor_v155_cotejo_t3.txt` | 1 | 0 |
| `_auditor_v182_cotejo_ciega.txt` | 6 | 24 |
| `_auditor_v189b_cotejo.txt` | 6 | 0 |
| `_auditor_v191_cotejo_ciega.txt` | 9 | 21 |

**LOS 37 QUE QUEDAN FUERA VAN NOMBRADOS UNO A UNO** en el bloque `D`, con su
motivo. **Y aqui esta lo que hay que decir en voz alta:** entre los que caen
estan `_auditor_v183_cotejo_ciega.txt`, `_auditor_v184_cotejo_ciega.txt` y
`_auditor_v190_cotejo_ciega.txt`, que **SI son cotejos de ciega de verdad**. No
entran porque **esta casa tiene al menos seis formatos distintos de cotejo** y
ninguna regla unica los lee a todos: la 183 escribe `PUESTO 375 | yo D | archivo
B`, la 184 escribe `DISCREPAN: 1 -> [660]`, la 190 escribe `DISCREPAN: 2 [1645,
2967]`. **Eso es exactamente lo que "no legibles con una regla unica" significa**,
y ensanchar la regla hasta que los coja seria elegir el universo despues de ver
el resultado. **0 lineas con `DISCREPA` fueron rechazadas por no ser un puesto.**

**(b) LAS TRES CIFRAS, JUNTAS Y NO SUELTAS:**

| | cifra |
|---|---:|
| **1.** puestos que han TUMBADO alguna vez a un lector | **30** |
| **2.** de esos, los que llevan `DISCUTIBLE MARCADO` | **6** (2656, 2830, 2832, 2909, 3063, 3182) |
| **3.** tasa de la marca en el archivo entero | **427 de 3.388 = 12,60 por ciento** |

**LOS TREINTA, NOMBRADOS:** 33, 199, 201, 648, 716, 871, 872, 904, 963, 1012,
1201, 1366, 1369, 1612, 1812, 1813, 1842, 2422, 2423, 2464, 2656, 2830, 2832,
2909, 3063, 3067, 3086, 3087, 3182, 3183.

**LA COMPARACION, QUE ES PARA LO QUE SIRVEN LAS TRES:** tasa de la marca entre
los que tumban **20,00 por ciento**, tasa en el archivo entero **12,60 por
ciento**, **diferencia +7,40 puntos**.

**Y EL DENOMINADOR NO SE INVENTA.** La misma regla recupera **69** coincidentes,
o sea **96** puestos leidos en total, **pero dos de los seis ficheros solo listan
las discrepancias** (`_auditor_v155_cotejo_t3.txt` y `_auditor_v189b_cotejo.txt`),
asi que "cuantos se leyeron" NO sale de esta regla. **Se dice en vez de
estimarse.**

**(c) NO ALCANZA PARA CONCLUIR, Y ESO ES UN RESULTADO Y SE ESCRIBE COMO TAL.**
Treinta puestos son el **0,89 por ciento** del archivo. Con 30 casos una
diferencia de tasas no distingue una tendencia de un accidente de muestreo, y
**esta medicion no afirma ninguna**. El propio instrumento lo escribe en su bloque
`G` y **la frase esta en el codigo, con su umbral, antes de conocer el
resultado**.

**Y HAY QUE DECIR ALGO MAS, PORQUE ES LO CONTRARIO DE LO QUE SE ESPERABA.** El
acta 191 midio sobre SUS treinta que **ocho tumbaron a dos lectores y CERO
llevaban la marca**, y de ahi salio la sospecha de que la marca y la dificultad
no se tocan. **Ensanchado el universo a lo que se puede leer del repo, la cuenta
apunta al otro lado**: 6 de 30, un 20 por ciento contra el 12,60 del archivo. **Y
la relectura al doble de la TAREA 2 de esta misma vuelta apunta igual**: el unico
puesto que me tumbo FUERA de mis dudosos, el 2832, **SI lleva la marca**.

**NINGUNA DE LAS DOS DIRECCIONES SE SOSTIENE CON ESTAS CIFRAS**, y lo honesto es
publicar las dos y el tamano. **Lo que esta vuelta deja no es una conclusion: es
el UNIVERSO, la REGLA y las TRES CIFRAS**, para que la vuelta que quiera concluir
sepa de donde parte y para que la primera cosa que haga sea **hacer legibles con
una regla unica los tres cotejos de ciega que hoy no lo son**.

**(d) NI UNA FILA DEL ARCHIVO ESCRITA**, y `git diff --numstat -- dataset/` en
**0 filas**. Ponerle la marca a ocho razones sobre una muestra de treinta seria
editar datos publicados, y el encargo lo prohibe con esas palabras.
