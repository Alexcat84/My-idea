### TAREA 5. EL COTEJO QUE NO CONVIERTE `"no"` EN `si`. **CERRADA EN VERDE.**

**LA CAIDA, CONFIRMADA CORRIENDOLA Y NO LEYENDOLA.** `bool("no")` en Python es
`True`, y eso se imprime dentro de la propia mutacion en vez de afirmarse.
`cuerpo_del_cotejo()` hacia `bool(du)`, y el docstring del formato especifica esa
columna como *"`en dudosos` . `si` o `no`"*: **la forma que el formato invita a
usar era justo la que reventaba.**

**a) `en_dudosos` SE NORMALIZA O CAE.** `normalizar_en_dudosos()` admite el
booleano de verdad, `0`/`1`, y las formas literales `si`/`sí`/`true`/`1` y
`no`/`false`/`0`, con la caja y los espacios normalizados **y nada mas**.
**Cualquier otra cosa levanta `EnDudososIlegible`**, que es una excepcion con
nombre propio y con la causa medida escrita en su docstring. Es la misma vara que
el caso `G` de la mutacion ya le aplicaba a `veredicto_de`: **lo raro sale a la
vista en vez de resolverse en silencio.**

**b) LA GUARDA DE `escribir_cotejo()` YA NO MIRA SOLO EL DENOMINADOR, Y SE DICE
POR QUE.** Sobre el fichero del auditor, **con las dos discrepancias de fuera
silenciadas, el denominador calzaba PERFECTAMENTE y la guarda daba VERDE**: un
denominador correcto sobre una columna falsa sigue siendo un verde falso. Ahora la
guarda **relee la columna `en dudosos` del disco y la coteja contra la que se le
paso**, normalizada, y publica tres cifras nuevas: puestos torcidos al escribir,
puestos que no volvieron del disco, y el reparto `si`/`no` del fichero. **Si algo
no calza, CAE y nombra los puestos.**

**c) EL CASO POSITIVO POR MUTACION, Y CORRE LOS DOS CAMINOS.** En
`docs/loop/SALIDA_V192_T5_MUTACION_FORMATO_COTEJO.txt` (4881 bytes, **VEREDICTO:
VERDE**), bloque `H`. Se fabrica un cotejo con `no` **en texto** en el puesto que
DISCREPA:

- **camino de hoy**: dudosos **1**, DENTRO `[]`, **FUERA `[2]`**;
- **camino viejo**, corrido aqui y no citado: `bool()` sobre `['si', 'no', 'no']`
  da **`[True, True, True]`**, o sea marca los TRES como dudosos y la discrepancia
  le sale DENTRO. **LA MUTACION CAE.**
- Mas la mutacion de los valores raros: `'quiza'`, `''`, `None`, `7` y `[]`
  **LEVANTAN**; `'SI '` y `'No'` **si se leen**, porque la caja y los espacios son
  lo unico que se normaliza.
- Mas la mutacion de que `cuerpo_del_cotejo()` **entero** cae si una fila trae un
  valor ilegible, **en vez de escribir un fichero con la columna inventada**.

**d) EL COTEJO DEL AUDITOR, RE ESCRITO CON EL INSTRUMENTO ARREGLADO.**
`scripts/loop/vuelta193_tarea5d_rehacer_cotejo_auditor.py`, salida en
`docs/loop/SALIDA_V193_T5D_REHACER_COTEJO.txt` (2463 bytes) y fichero en
`docs/loop/SALIDA_V193_T5D_COTEJO_AUDITOR_REHECHO.txt`. **Se le pasa `en dudosos`
COMO TEXTO a proposito**, que es el camino que reventaba. **Su fichero no se
toca.**

| | obtenido | lo que el auditor publica a mano | |
|---|---:|---:|---|
| cotejados | 30 | 30 | **CALZA** |
| coinciden | 25 | 25 | **CALZA** |
| discrepan | 5 | 5 | **CALZA** |
| DENTRO de sus dudosos | `965, 1068, 1814` | `965, 1068, 1814` | **CALZA** |
| FUERA de sus dudosos | `1804, 2833` | `1804, 2833` | **CALZA** |

**Y LA MEDICION QUE SEPARA LOS DOS CAMINOS, SOBRE SUS 30 FILAS DE VERDAD:** el
camino viejo lee **`si` en 30 de 30** (el fichero trae 13 `si` y 17 `no`) y publica
**0 discrepancias FUERA**; el de hoy publica **2** (`1804`, `2833`). **La regla de
parada de `AUDITOR.md` 1.2 cuelga de esa cifra, asi que el camino viejo publicaba
un VERDE donde habia una escalada.**

**e) `cotejo_de_ciega.py` NACIO EN LA 192 Y TODAVIA NO HA ENTRADO EN LA NOMINA.**
El carril `--reproduccion` de la TAREA 2, corrido en esta vuelta, mide que **los
arneses que el censo RECLAMA son cuatro** y **ninguno de ellos es este fichero**.
**Tocarlo ahora es ANTES de que entre, y eso es a favor y no en contra:** entrara
ya con el `bool(du)` arreglado, con su guarda ensanchada y con su mutacion
cubriendo la columna. **Lo digo aqui para que no se lea como que le meti mano a
una entrada de la nomina.**

**Y EL CORTE VIEJO NO SE BORRA:** queda en
`docs/loop/SALIDA_V192_T5_MUTACION_FORMATO_COTEJO_CORTE_192.txt`, con su nombre y
su vuelta.
