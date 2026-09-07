### TAREA 3. LA DISCREPANCIA DE COMPONENTES, PERSEGUIDA Y DECLARADA

**LA NOMINA SELLADA SE CUENTA Y NO SE REESCRIBE.**
`docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl` mide **96361 bytes en disco y 96029
normalizado a LF**, `sha256` LF **95dca64dbce48d52**, y **332 lineas no vacias**.
No se abrio en modo escritura en ninguna linea, y el `numstat` de `docs/plan/`
sigue en **0 filas**. Todo lo de abajo sale de
`docs/loop/SALIDA_V204_T3_COMPONENTES.txt`.

#### EL PROTOCOLO DEL SELLO, Y LA PUERTA QUE NI SIQUIERA ESCRIBE

**MI PROPIA CAIDA, DECLARADA Y NO TAPADA (`C.1`).** El bloque `H.3` de mi sello
de apertura publico **VEREDICTO DE LA COMPROBACION PREVIA: NO ESCRIBE** sobre
`scripts/loop/vuelta169_tarea3_op_i_01.py`, y **eso es falso en lo que importa**.
Mi marca solo veia la escritura DIRECTA, que es **0 lineas**, y ese instrumento
escribe **POR SUBPROCESO**, en sus lineas 147 y 157, llamando a
`scripts/plan/recomputo_3388.py --salida`. **La cifra de 0 era cierta; la palabra
que le puse encima, no.** El texto viejo sigue entero en el sello de apertura y
no se borra.

**EL REMEDIO NO FUE ESCRIBIR Y RESTAURAR, SINO NO ESCRIBIR.** El propio
instrumento documenta en su linea 52 la variable de entorno
`V169_RECOMPUTO_SALIDA`, y por ahi se redirigio la salida a
`docs/loop/RECOMPUTO_V204_DIAGNOSTICO.jsonl`. **MEDIDO Y NO AFIRMADO:**
`docs/loop/RECOMPUTO_V169.jsonl` mide **15369 bytes en disco y 15322 normalizado
a LF**, `sha256` LF **e8a10f174df3c5fa**, **antes y despues de correr**, y
`git status --porcelain` sobre las dos sedes da **0 filas**. **No hizo falta
restaurar nada porque no se toco nada.**

**EL `PD.2` SE PUBLICA Y NO SE RESUELVE:** los dos tamanos de esa sede discrepan
por el CRLF que `git checkout` deja. La convencion de bytes sigue siendo del
fundador.

#### EL BLOQUE `E`, REPRODUCIDO HOY Y NO COPIADO DEL ENCARGO

El instrumento corrio con `exit 0` y su bloque `E` publica: **sellado 332 lineas
con 54 ABIERTO y 278 CERRADO**, **hoy 47 lineas con 21 ABIERTO y 26 CERRADO**, y
**su veredicto de reproduccion sale `False`**. Calza al digito con lo que el
encargo describe.

#### EL COTEJO CONJUNTO A CONJUNTO, CON EL RESOLUTOR DELANTE POR `P.1`

Con **3853 nodos vivos y 761 alias** en el resolutor, y con la clave de cada
componente formada por el conjunto de sus miembros YA RESUELTOS:

- **332 claves distintas en el sellado, 47 en la corrida de hoy.**
- **COMPONENTES DEL SELLADO QUE HOY NO ESTAN: 285.**
- **COMPONENTES DE HOY QUE NO ESTABAN EN EL SELLADO: 0.**
- **COMPONENTES QUE COINCIDEN EN LAS DOS: 47.**

**El conjunto de hoy es SUBCONJUNTO ESTRICTO del sellado.** Ninguna componente
nueva.

#### DE DONDE SALE LA DIFERENCIA: LA CAUSA, MEDIDA EN POSITIVO

| pregunta | medicion de hoy |
|---|---|
| ¿el universo cambio? | **106 commits** sobre `dataset/metadata/master_graph.json` y `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` desde el corte del sellado |
| ¿cuantas componentes selladas colapsaron? | **263 de 332** resuelven HOY a UN SOLO nodo |
| ¿algun miembro murio? | **0** componentes selladas tienen miembros que hoy no sean nodo vivo ni alias que lleve a uno |
| ¿el instrumento cambio? | **SI: 2 commits** sobre `scripts/plan/recomputo_3388.py` desde el corte, uno de ellos titulado *la A deja de perderse al agrupar* |
| ¿la fecha del corte? | **2026-08-19**, leida de `git log` sobre el propio fichero sellado |

**LO QUE EL COLAPSO NO EXPLICA, CONTADO EN VEZ DE PASADO POR ALTO:** de las
**285** que faltan, **263 son colapso puro** y **22 NO lo son**, porque todavia
tienen dos o mas nodos distintos tras resolver. De esas 22: **0 estan contenidas
en una componente de hoy, 0 solapan con ninguna, y 22 no tocan ninguna**;
**21 son de 2 nodos y 1 es de 3**. **Esas 22 no las explica la fusion, y no se
tapan.**

#### EL VEREDICTO SOBRE LA CAUSA, Y UNA CAIDA MIA MAS

**CAIDA `C.2`, CAZADA ANTES DE PUBLICARSE.** Mi primera redaccion de este
veredicto decia, **tecleada y no medida**, *el instrumento y el motor NO
cambiaron desde el corte del sellado, asi que la causa NO es el instrumento*, y
**mi propio bloque `D.3` la desmiente**. La frase vieja queda escrita en la
salida y no se borra.

**LO QUE LAS CIFRAS SOSTIENEN, Y SOLO ESO:** la causa mayor es **EL UNIVERSO**,
con 263 de 332 componentes fundidas a un solo nodo, que es exactamente lo que la
nota de la propia ficha ya describia. **EL INSTRUMENTO NO SE PUEDE DESCARTAR como
causa parcial**, porque cambio despues del corte; lo que si se puede decir con
cifra es que **un cambio de algoritmo que agrupara distinto habria producido
componentes NUEVAS, y hay 0**. **LA FECHA NO ES UNA CAUSA APARTE**, sino la
etiqueta de la primera.

**POR DONDE ME PODRIA EQUIVOCAR, DICHO ANTES DE SABERLO:** mi cuenta del cambio
de instrumento mide los dos ficheros **por su ruta y no su cadena de imports**;
mi definicion de colapso es **una** lectura y no la unica; y **no medi el grafo
del corte contra el de hoy nodo a nodo**, que es la corrida que cerraria la
pregunta y que el encargo no pedia.

#### NO HAY PARADA, Y NO HACE FALTA CODIGO

**NINGUNA CIFRA PUBLICADA ENVEJECIO POR ESTA MEDICION**, asi que **no se abre el
carril del banco `9.10`**: la nota de `OP-I-01` ya trae escritas las tres cifras
(332, 47 y su aritmetica) **cada una con su corte**, y la corrida de hoy las
reproduce. **No se para**, porque nada contradice una regla vigente ni una cifra
publicada con su corte. **Y no hace falta codigo**: la unica medicion que
quedaria pendiente, correr el motor sobre el grafo del corte viejo, **se nombra y
no se fabrica**, que es lo que la moratoria `6.3` manda.

**DISCUTIBLE `D.3`:** las **22 componentes que el colapso no explica** son el
candidato natural a una lectura propia. Son 21 pares y un trio, y **no tocan
ninguna componente de hoy**, lo que apunta a que su arista dejo de ser `A` en la
sede de veredictos y no a que sus nodos se fundieran. **No lo persigo mas: lo
mido, lo nombro y lo dejo.**
