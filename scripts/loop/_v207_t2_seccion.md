### TAREA 2. LA MESA `OP-L-01`, LEIDA CONTRA LOS TRES DOCUMENTOS QUE SU PROPIA FICHA NOMBRA

**LO QUE DEJO SELLADO, CON LAS DOS CONVENCIONES EN EL MISMO RENGLON:**

| salida sellada | bytes | exitcode |
|---|---|---:|
| `docs/loop/SALIDA_V207_T2_VARA.txt` | 6533 bytes en disco y 6533 normalizado a LF | 0 |
| `docs/loop/SALIDA_V207_T2_COTEJO.txt` | 10620 bytes en disco y 10620 normalizado a LF | 0 |

#### 2.a. LA VARA, ESCRITA Y SELLADA ANTES DE ABRIR NINGUN DOCUMENTO

**VA EN SU PROPIO COMMIT, `d7ab4545`, Y ESE ES EL PUNTO.** Una vara escrita
despues de mirar se acomoda a lo que se vio, y la unica forma de probar que la
mia no se acomodo es que exista en git ANTES del commit que abre los documentos.

**CATORCE PUNTOS, `V.1` A `V.14`, CADA UNO CON LA CITA LITERAL DEL CAMPO Y DEL
ELEMENTO DE LA FICHA DEL QUE SALE**, y **las catorce citas comprobadas VERBATIM
por el propio computo contra la ficha**: `CIFRA citas que NO aparecen verbatim: 0`.
Si una sola no hubiera aparecido, el computo caia en rojo y no sellaba nada.

**LA SEDE FINA ES `campo[indice]` Y NO UN NUMERO DE LINEA**, y se dice por que:
la ficha entera vive en **UNA sola linea** de `docs/plan/OPERACIONES.jsonl`, la
**41**. Decir *"linea 41"* catorce veces no localiza nada.

**LA FICHA, MEDIDA:** **18** campos, **4** elementos de `evidencia`, **6** de
`verificacion` de los cuales **4** son CORRECCIONES DECLARADAS, `fecha_corte`
**2026-08-11**, `depende_de` vacio (**0**) y `bloquea_a` vacio (**0**), que es
justo por lo que el encargo la elige primera de las cuatro.

**EL CAMPO `estado` SE LEE COMO DATO Y NO SE TOCA** (`AUDITOR.md` 0): dice
`LISTA`. No lo levante, no lo baje y no lo mire para decidir nada.

**Y EL REPARTO TAMBIEN SE SELLO ANTES DE MIRAR**, que es la mitad que suele
faltar: **10** puntos declarados documentales y **4** declarados NO documentales
con su motivo escrito. Si el cotejo hubiera querido mover un punto de un lado al
otro despues de ver los documentos, el sello lo delataria.

#### 2.b. EL COTEJO, PUNTO POR PUNTO, CON SU FICHERO Y SU LINEA

**LOS TRES DOCUMENTOS, REMEDIDOS POR MI Y NO COPIADOS DEL ENCARGO**, y los tres
calzan al digito con su contraste:

| documento | bytes | sha256 |
|---|---|---|
| `docs/plan/LECTURAS_DIRIGIDAS.md` | 214916 bytes en disco y 214916 normalizado a LF | sha256 disco `dda1cdd67042c733` y sha256 LF `dda1cdd67042c733` |
| `docs/INTRA_DOMINIO_INFORME.md` | 943970 bytes en disco y 943970 normalizado a LF | sha256 disco `c05b6bcd20188a9c` y sha256 LF `c05b6bcd20188a9c` |
| `docs/BANCO_DE_TEXTOS.md` | 182228 bytes en disco y 182228 normalizado a LF | sha256 disco `68557cd00a3124f4` y sha256 LF `68557cd00a3124f4` |

**LAS ONCE SE CUENTAN CON `CABECERA_LD` IMPORTADA Y NO CON UN PATRON MIO**, que
es la vara que esta campana ya usa y que el acta 203 cita por su nombre. Da
**27** cabeceras `LD` en el documento de hoy, de las cuales **11** son de la
tanda (`LD-01` a `LD-11`) y **16** son de fuera. **CIFRA de las once que el
patron NO encontro: 0.**

**LA TABLA DEL COTEJO. UNA FILA SIN CITA NO VALE:**

| punto | doc | veredicto | cita, con fichero y linea |
|---|---|---|---|
| `V.1` las once con su razon | LD | **CUBRE** | `LECTURAS_DIRIGIDAS.md:74` `## LAS ONCE, una por una`. Las 11 con veredicto leido de su cabecera y las 11 con prosa y linea de cita. **CIFRA sin razon: 0** |
| `V.2` seccion 52 con las parejas que el ejercicio no puede cerrar | INF | **CUBRE** | `INTRA_DOMINIO_INFORME.md:10055` `## 52. LAS PAREJAS QUE EL EJERCICIO NO PUEDE CERRAR`, lineas 10055 a 10111 |
| `V.3` la `TABLA VIVA DE LOS PUROS` | BAN | **A MEDIAS** | `BANCO_DE_TEXTOS.md:938` `#### TABLA VIVA DE LOS PUROS, al 14 ago 2026 (vigente al puesto 1157)`, 11 filas de racimo. **Existe, pero no lleva el efecto de esta mesa. Ver la `D.1`** |
| `V.4` la cifra 205 sobre 221 componentes | LD | **CUBRE** | `LECTURAS_DIRIGIDAS.md:17` y la cifra 205 en la linea **21**. **Iba sellado como NO documental y resulta que SI tiene sede documental. Ver la `D.2`** |
| `V.5` la tanda de once, 11 ago 2026 | LD | **CUBRE** | `LECTURAS_DIRIGIDAS.md:44` `## ESTA TANDA: ONCE LECTURAS`, y la fecha en la linea **17** |
| `V.6` misma vara, marcadas LECTURA DIRIGIDA | LD | **CUBRE** | `LECTURAS_DIRIGIDAS.md:10`, y la segunda mitad de la clausula en la **11** |
| `V.7` el saldo, 2 `A` y 9 `D` | LD | **CUBRE** | `LECTURAS_DIRIGIDAS.md:60` `## EL SALDO`. **Y su cifra calza con MI recuento de las cabeceras: 2 que empiezan por A y 9 que son D** |
| `V.8` las once nombradas una a una | LD | **CUBRE** | `LECTURAS_DIRIGIDAS.md:74`. **CIFRA con cabecera propia y veredicto: 11 de 11** |
| `V.9` la clase nueva `A DE BLOQUE` | LD | **CUBRE** | `LECTURAS_DIRIGIDAS.md:177`, la definicion entera; la clase se nombra en **4** lineas |
| `V.10` destejido mas fusion parcial | LD | **CUBRE** | `LECTURAS_DIRIGIDAS.md:180`, y se repite en la tabla de formas en la **296** |
| `V.11` la leccion del saldo, 9 de 11 sanas | LD | **CUBRE** | `LECTURAS_DIRIGIDAS.md:299`, con su motivo detras |
| `V.12` clausula 1 de verificacion | (LD) | **NO DOCUMENTAL** | sellado antes de mirar: es clausula contra `INTRA_DOMINIO_VEREDICTOS.jsonl`, que no es ninguno de los tres. Se busco igual y el literal aparece en `LECTURAS_DIRIGIDAS.md:1826` |
| `V.13` clausula 2 de verificacion | (LD) | **NO DOCUMENTAL** | sellado antes de mirar: es clausula contra el marcador del cribado. Se busco igual y aparece en `LECTURAS_DIRIGIDAS.md:11` |
| `V.14` clausula 3 de verificacion | (LD) | **NO DOCUMENTAL** | sellado antes de mirar: es clausula contra las nominas del inventario. Se busco igual y aparece en `LECTURAS_DIRIGIDAS.md:51` |

**LO QUE LA `V.2` MIDE ADEMAS, Y VA COMO DATO Y NO COMO REPROCHE:** de las once,
**8** tienen sus DOS identificadores dentro de la seccion 52 (`LD-04` a `LD-11`)
y **3** no (`LD-01`, `LD-02`, `LD-03`). **No es un fallo de la seccion:** esas
tres son las que la propia tanda clasifica como *cierran una nomina* y no salen
de esa lista, y el documento lo dice en su linea **51**.

#### 2.c. LA COBERTURA, MEDIDA Y NO NARRADA

| veredicto | cuantos | cuales |
|---|---:|---|
| **CUBRE** | **10** | `V.1`, `V.2`, `V.4`, `V.5`, `V.6`, `V.7`, `V.8`, `V.9`, `V.10`, `V.11` |
| **A MEDIAS** | **1** | `V.3` |
| **NO CUBRE** | **0** | (NINGUNO) |
| **NO DOCUMENTAL** | **3** | `V.12`, `V.13`, `V.14` |

**LA LISTA NOMINAL DE LOS QUE NO CUBREN: NINGUNO.**
**LA LISTA NOMINAL DE LOS QUE CUBREN A MEDIAS: `V.3`.**

**SOBRE LOS 10 PUNTOS DOCUMENTALES SELLADOS: 9 CUBREN, 1 a medias, 0 no cubren.**

**ESTA ES LA CIFRA QUE LA MESA LLEVABA DOS VUELTAS SIN TENER**, y es exactamente
lo que la vara del trabajo pendiente dice de si misma que no hace: *"Si cubre lo
que la ficha describe es LECTURA, y esta vara no la hace."*

#### 2.d. NO CIERRO LA FICHA. LO DEJO PROPUESTO

**PROPUESTA, Y NO ADJUDICACION:** con **0 puntos sin cubrir** y **1 a medias**,
`OP-L-01` **esta sustancialmente cubierta por los tres documentos que su propia
ficha nombra**, y **propongo cerrarla**. **Cerrar una ficha del plan es
adjudicacion del auditor y no mia**, asi que aqui se para.

**LO QUE FALTA PARA QUE SEA UN CIERRE LIMPIO, NOMBRADO Y NO EJECUTADO:** el unico
punto que no cubre entero es la `V.3`, y **no lo arreglo en esta vuelta**.
Arreglarlo seria reescribir dos filas de la `TABLA VIVA DE LOS PUROS` en
`docs/BANCO_DE_TEXTOS.md`, que es una sede sellada del banco, por el carril del
`9.10` y con su correccion declarada. **No cabe con sus guardas al lado de las
dos sub-tareas de esta vuelta, y una mesa a medias es peor que una mesa
pendiente.**

**NO SE TOCO EL CAMPO `estado`**, y no lo digo: lo mide el `sha256`.
`docs/plan/OPERACIONES.jsonl` sigue en **513043** bytes en disco y **513043**
normalizado a LF, sha256 disco `829c583eb779cab6` y sha256 LF `829c583eb779cab6`,
identicos a los de mi apertura. **`git diff --numstat` sobre `docs/plan/`,
`docs/BANCO_DE_TEXTOS.md` y `docs/INTRA_DOMINIO_INFORME.md` da 0 filas.**

#### 2.e. EL COMPUTO, CON PREFIJO DE GUION BAJO

`scripts/loop/_v207_t2_vara.py` y `scripts/loop/_v207_t2_cotejo.py`, los dos
**fuera del censo y fuera de la nomina**, que sigue congelada en **135**.
**NINGUN LECTOR NUEVO DE PROPOSITO GENERAL:** `CABECERA_LD` se IMPORTA de
`scripts/loop/vuelta165_tarea6_op_l_01.py` y la vara se IMPORTA del fichero
sellado. El resto es busqueda de literal que devuelve linea.
