### TAREA 2: LA CORRECCION DECLARADA DE LA EVIDENCIA DE `OP-I-01`, EN SU SEDE

**ADJUDICADA POR EL ACTA 199 EN SU `4.1`. NO ES PARADA.** Comando corrido en esta
vuelta, con su salida sellada en
`docs/loop/SALIDA_V201_T2_CORRECCION_OP_I_01.txt`:

```
python scripts/loop/_v201_t2_correccion_op_i_01.py --escribir
```

**NINGUNA DE LAS DOS CIFRAS ESTA TECLEADA, Y CADA UNA VIAJA CON SU FECHA DE
CORTE** (banco `9.21`):

- **323 entradas, corte 2026-08-11.** No se busco a ojo: se **cita por linea**.
  Vive en la **linea 44** de `docs/plan/OPERACIONES.jsonl`, en el **elemento 1**
  de la lista `evidencia` de la ficha, verbatim `INVENTARIO.jsonl, 323 entradas`,
  y el `2026-08-11` es el `fecha_corte` de la propia ficha. El computo **cae en
  rojo si el 323 no esta en exactamente un elemento**, para que la cifra vieja no
  se elija a dedo. **El 323 aparece TAMBIEN en el campo `nota`**, y ese campo **no
  se toca**.
- **672 entradas, corte 2026-09-07.** Recontadas **en esta vuelta**, leyendo
  `docs/plan/INVENTARIO.jsonl` linea a linea y parseando cada una como JSON:
  **672 lineas no vacias**, **0 lineas que no son JSON valido**, y
  **584554 bytes en disco y 584554 normalizados a LF**.

**EL REPARTO POR TIPO, RECONTADO HOY Y NO COPIADO DE NINGUNA ACTA NI DEL ACTA
199.** Contado de `docs/loop/SALIDA_V201_T2_CORRECCION_OP_I_01.txt`:

| tipo | entradas, corte 2026-09-07 |
|---|---:|
| `acto` | 556 |
| `familia_de_ids` | 54 |
| `figura` | 20 |
| `defecto` | 19 |
| `racimo` | 13 |
| `dominio` | 10 |
| **suma** | **672** |

**LA SUMA DEL REPARTO CALZA CON LAS ENTRADAS: SI.** Y **el reparto viejo (221
actos, 53 familias de ids, 14 defectos, 13 racimos, 12 figuras y 10 dominios)
sigue escrito en el campo `nota` de la ficha y no se toca**, que es lo que
significa **el texto viejo entero y sin tachar**.

**LA CIFRA VIEJA NO ES UNA MENTIRA Y NO SE RETIRA.** Con su corte era cierta. **Lo
que envejecio es la evidencia**, y por eso la correccion entra **POR ADICION**,
como un **elemento mas de la misma lista `evidencia`** y **sin clave nueva de
esquema**: es la via que la ficha gemela `OP-L-01` uso en la vuelta 166 y que el
acta 71, seccion 6, adjudicacion 3, adjudico **CON LAS PALABRAS NO ES PARADA**.

**NINGUN CAMPO `estado` SE MOVIO, Y NO SE AFIRMA: SE MIDE CONTRA `HEAD`.** Salida
sellada en `docs/loop/SALIDA_V201_T2_GUARDA_ESTADO.txt`, que sale **VERDE**: **1
sola linea difiere** de las 71 y es la **44**; de esa ficha cambia **1 sola clave**
y es `evidencia`; el `estado` de `OP-I-01` entra y sale en `LISTA`; los **3
elementos viejos siguen identicos y en su orden** y ahora son **4**; y **0 de las
71 fichas** cambian su campo `estado`. `git diff --numstat` sobre `docs/plan/`
da **1 anadida y 1 borrada** en `docs/plan/OPERACIONES.jsonl`, que es lo que
`jsonl` da siempre al reescribir una linea. El fichero sale en
**499474 bytes en disco y 499474 normalizados a LF**, y antes de escribir media
498085 por disco y 498085 por LF. Tiene **71 lineas no vacias antes y despues** y
**0 lineas que no sean JSON valido**.

**UNA CORRECCION DE MI PROPIO COMPUTO, HECHA EN ESTA MISMA VUELTA Y DECLARADA EN
VEZ DE CALLADA.** En su primera version la guarda del 323 corria **delante** de la
de idempotencia, y la segunda corrida caia en **ROJO** diciendo *"el 323 no esta
en exactamente un elemento de `evidencia`"*. **Era cierto**, porque **la propia
correccion cita el 323 verbatim** y despues de escribirla hay **dos** elementos con
esa cifra. **No escribia nada, que es lo que se queria, pero lo decia por el motivo
equivocado**, y un instrumento que acierta por el motivo equivocado no vale. Se
reordeno, se dejo escrito dentro del fichero, y la segunda corrida esta sellada
aparte en `docs/loop/SALIDA_V201_T2_CORRECCION_OP_I_01_IDEM.txt`, que mide
**1390 bytes en disco y 1390 normalizados a LF**: **IDEMPOTENTE**, **4 elementos
de `evidencia` al entrar** y la ficha sin crecer ni un byte.
