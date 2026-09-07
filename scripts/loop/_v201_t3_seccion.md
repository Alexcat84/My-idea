### TAREA 3: `OP-L-02` MEDIDA CONTRA SU `verificacion`. TERMINA EN PARADA, Y LA PARADA ES LA MEDICION

**ADJUDICADA POR EL ACTA 199 EN SU `4.2`.** Comando corrido en esta vuelta, con su
salida sellada en `docs/loop/SALIDA_V201_T3_OP_L_02.txt` (**9199 bytes**):

```
python scripts/loop/_v201_t3_medir_op_l_02.py
```

**POR QUE SE MIDE CONTRA `verificacion` Y NO CONTRA `evidencia`, CONTADO AQUI Y
NO HEREDADO DEL ENCARGO:** la ficha vive en la **linea 42** de
`docs/plan/OPERACIONES.jsonl`, su `evidencia` tiene **1 solo elemento**
(*"MEDIDO el 11 ago 2026: 205 pares fuera de cola, 11 leidos, 194 pendientes"*) y
de ese elemento **0 nombran un fichero**. **Sin fichero nombrado no hay documento
que medir.**

**LA `verificacion` SE CITA POR LINEA, Y LA COORDENADA VA ENTERA.** La ficha es
**una linea de JSONL**, asi que la cita es **la linea 42 mas el indice del
elemento**, y las dos van juntas. **4 elementos**:

| coordenada | que pide, verbatim |
|---|---|
| linea 42, `verificacion[1]` | `las tres nominas afectadas quedan con cobertura COMPLETA y su forma reescrita` |
| linea 42, `verificacion[2]` | `el marcador del cribado no se mueve: sigue en 2.117` |
| linea 42, `verificacion[3]` | `cada grupo del backlog lleva su motivo escrito, no solo su cuenta` |
| linea 42, `verificacion[4]` | la CORRECCION DECLARADA de la vuelta 170 sobre la clausula 2, **1486 caracteres** |

**QUE SE PUEDE COMPROBAR HOY Y QUE NO, CLAUSULA A CLAUSULA:**

- **`verificacion[1]`: NO ALCANZA PARA EJECUTAR SIN DECIDIR.** Pide **dos** cosas,
  no una: **cobertura COMPLETA** y **forma reescrita**. Y el motivo es medido, no
  opinado: la clausula escribe el numeral **`tres`**, y el campo `nota` **de esta
  misma ficha** escribe el literal **`SEIS nominas`** **1 vez** y **`TRES
  nominas`** **1 vez**. Las dos frases estan en la misma ficha, hablan de las
  mismas nominas y dan numeros distintos. **Y ninguna de las dos las nombra por
  id:** los campos `nodos`, `preservar`, `eliminar` y `superviviente` de la ficha
  miden **0, 0, 0 y `None`**. **Elegir cuales son las tres afectadas es DECIDIR,
  no medir.**
- **`verificacion[2]`: SE PUEDE MEDIR EL MARCADOR, PERO NO ES CRITERIO DE HECHO.**
  Recontado hoy, linea a linea, de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`
  (**4054129 bytes en disco y 4054129 normalizados a LF**): **3388 filas**, **3388
  puestos distintos**, **maximo 3388**, **0 huecos**, y el reparto por clase **A
  551, B 72, C 5, D 2760**, que suma **3388**. **Este conteo NO pasa por el
  resolutor y se dice por que:** `P.1` lo manda para **todo conteo que toque ids**,
  y contar **puestos** no toca ninguno. Lo que la clausula pide es que **la
  operacion** no mueva el marcador, y eso solo se comprueba **corriendo la
  operacion**, que no se ha corrido. **El 3388 de hoy es un ESTADO, no el
  cumplimiento de la clausula**, y el `2.117` es **testigo y no condicion**, como
  ya dice la correccion declarada de la vuelta 170 que vive en esta misma lista.
- **`verificacion[3]`: SE COMPRUEBA HOY Y SALE CUMPLIDA.** Leido del campo `nota`
  de la propia ficha: **189 pares** de backlog en **4 grupos**, **126 esperan
  destejido**, **55 son resto sin mesa ni nomina**, **5 de sales roadmap con clase
  ya decidida** y **3 ya leidas en la primera tanda**. **La suma de los grupos da
  189 contra el total escrito 189 y CALZA**, y **los 4 de 4 llevan motivo
  escrito**.
- **`verificacion[4]`: NO ES CRITERIO.** Es la correccion por adicion de la
  clausula 2, y por eso no se mide como tal.

**LAS RUTAS QUE LA FICHA PROMETE COMO PRUEBA, MEDIDAS UNA A UNA** (`EJECUTOR.md`
1, LA RUTA QUE PROMETE PRUEBA ES CIFRA): **8 rutas distintas**, **8 vivas**, **0
inexistentes** y **0 de cero bytes**. Ninguna caida de cifra por ahi.

**LA CORRECCION DE MI PROPIO COMPUTO, DECLARADA Y NO TAPADA.** La primera version
del lector del backlog casaba `(\d+)\s+(.*)` contra cada trozo separado por coma,
y **el cuarto grupo de la `nota` empieza por `y 3 ya leidas...`**: el patron no
casaba, la cuenta salia 0, el motivo salia vacio, y este computo publicaba **`3 de
4 grupos con motivo`** y **`186 contra 189, NO CALZA`**. **La ficha estaba bien y
el lector estaba mal.** Se quita la conjuncion antes de leer la cifra, queda
escrito dentro del fichero, y **con el arreglo salen 4 de 4 y 189 contra 189**.

**Y LO QUE ESTA TAREA NO HIZO:** no movio ningun `estado` (la ficha entra y sale en
`LISTA`), no cerro la ficha, no adjudico ninguna clase, no toco ni un veredicto,
**no escribio una sola linea en `docs/plan/`** y no ejecuto la operacion.

> **PARADA `1` DE ESTA VUELTA, Y NO LA ARREGLO YO.** `OP-L-02` **no se puede
> ejecutar hoy sin decidir**, por su `verificacion[1]`: su propio texto da **tres**
> y **seis** para las mismas nominas y **no las nombra por id en ningun sitio**.
> `AUDITOR.md` 3 dice que una operacion cuyo texto no alcanza para ejecutarse sin
> decidir **es PARADA, no una improvisacion**. **No la improviso y no la declaro
> hecha.** Lo que hace falta para desbloquearla es una sola decision escrita:
> **cuales son las nominas afectadas, nombradas por id**, y si son **tres** o
> **seis**. **Esa decision no es mia.**
