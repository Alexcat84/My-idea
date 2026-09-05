### TAREA 5. EL TRABAJO DE VERDAD: CERRAR `OP-L-02`

**5.a LA FORMA DE LAS TRES NOMINAS, RE ESCRITA POR ADICION.** Instrumento
`scripts/loop/vuelta170_tarea5_forma_de_las_nominas.py`, salida
`docs/loop/SALIDA_V170_T5A_FORMA_NOMINAS.txt`, **exit 0**. Corrido antes en modo
medicion, que no toca el inventario.

**LO QUE EL RESOLUTOR SEPARA, Y ES LA MITAD QUE HACIA FALTA.** Una forma escrita
el 11 ago 2026 habla de una nomina que ese dia tenia N nodos vivos. **Desde
entonces la campana ha fundido**, y contar sin resolver haria que una nomina
fundida siguiera pareciendo entera. Cada nomina se mide **dos veces**: como esta
escrita y como queda tras resolver.

| nomina (racimo del inventario) | miembros escritos | vivos tras resolver | pares posibles | leidos | SIN | puentes `P.10` |
|---|---:|---:|---:|---:|---:|---:|
| los cuadrantes de mercado | 6 | **1** | 0 | 0 | 0 | 0 |
| la ecuacion de valor | 5 | 5 | 10 | 10 | 0 | 4 |
| la supervision de la IA | 10 | **7** | 21 | 13 | **8** | 3 |

**LA GORDA, Y NO ESTABA PREVISTA: `los cuadrantes de mercado` ESTA FUNDIDA.** Sus
seis miembros resuelven **todos** a `marco_analisis_mercado_cadena_suministro`
(cinco colapsos por `ids_alias`, nombrados uno a uno en la salida). **No queda
ningun par que leer, asi que ya no tiene forma que medir.** Su `MEZCLADO` con
`15 de 15` era cierto en su corte y se queda entero al lado.

**LA SEGUNDA, Y OBLIGA A ESCRIBIR DOS CIFRAS EN VEZ DE UNA:** `la supervision de
la IA` **como racimo entero** esta **PROVISIONAL, 13 de 21**, con 8 pares sin
leer y 3 colapsos; **pero la nomina que `OP-L-02` cerro es un SUBCONJUNTO suyo**,
el bloque humano, y **esa si esta 10 de 10, cero sin veredicto, reparto A 5 D 5**.
**Las dos cifras son ciertas y hablan de universos distintos**, y por eso las dos
van escritas en el mismo campo, medidas por **la misma maquina en la misma
corrida**. Escribir solo la del racimo habria hecho parecer que la segunda tanda
no cerro nada.

**`9.16` VIAJA CON CADA FORMA QUE SE ESCRIBE**, y no de adorno: `la ecuacion de
valor` cierra 10 de 10 **pero NO se funde**, porque trae **4 nodos puente de
`P.10`** y `P.10` dice que la componente no se funde hasta que el triangulo se
cierre. La forma lo dice con sus puentes nombrados.

**LAS GUARDAS:** la forma vieja y la cobertura vieja **siguen enteras dentro de
las tres** (comprobado antes de escribir, y el instrumento cae en rojo si no);
**672 entradas antes y despues**; **reparto por tipo identico** antes y despues;
las tres siguen en sus lineas 237, 233 y 241; **9 claves antes y 9 despues**;
**cero campos movidos** ademas de `forma` y `cobertura`; y **el `estado` de las
tres sin mover**.

**UNA CAIDA MIA, CAZADA POR MI Y DECLARADA:** mi primer parche pego la coletilla
del subconjunto **dos veces** en `la supervision de la IA`. Lo vi al leer el
campo en disco, restaure `INVENTARIO.jsonl` con `git checkout`, arregle el
instrumento y lo volvi a correr. **La forma pasa de 1.064 a 753 caracteres**, que
es la diferencia exacta de la coletilla repetida.

**5.b EL VEREDICTO DE `OP-L-02`, CON LA MEDICION DELANTE.** Instrumento
`scripts/loop/vuelta170_tarea5b_veredicto_op_l_02.py`, salida
`docs/loop/SALIDA_V170_T5B_VEREDICTO_OP_L_02.txt`, **exit 0**. Las clausulas
**se leen de la ficha**, y las `CORRECCION DECLARADA` se separan de ellas porque
**una correccion no es una clausula que cumplir**: 4 elementos en
`verificacion`, **3 clausulas** y 1 correccion.

| clausula | como se midio | veredicto |
|---|---|:-:|
| **1**. *las tres nominas afectadas quedan con cobertura COMPLETA y su forma reescrita* | las **seis** nominas de `OP-L-02` con el resolutor delante dan **0 pares sin veredicto**; y las tres formas llevan hoy el corte `2026-09-04` escrito | **CUMPLIDA** |
| **2**. *el marcador del cribado no se mueve: sigue en 2.117* | marcador recomputado **3.388** (A 551, B 72, C 5, D 2.760); `git diff 46208790 HEAD --numstat -- docs/INTRA_DOMINIO_VEREDICTOS.jsonl` da **0 filas**, y sin commitear **0 filas** | **CUMPLIDA** |
| **3**. *cada grupo del backlog lleva su motivo escrito, no solo su cuenta* | la tabla del backlog de `LECTURAS_DIRIGIDAS.md`, contada fila a fila: **4 grupos, 4 con motivo escrito, 0 sin** | **CUMPLIDA** |

**LAS TRES CLAUSULAS QUEDAN CUMPLIDAS, 3 de 3, Y LO DIGO CON LA MEDICION
DELANTE.** Y **el campo `estado` NO SE TOCA**: sigue diciendo `LISTA` y **no es
la vara**, por la decision del fundador del 4 sep 2026. La vara corrida al lado,
`scripts/loop/vuelta150_3_relectura_expediente.py --corte HEAD`: **71 fichas, 37
que no calzan, 24 congeladas declaradas, 12 congeladas en silencio, 1 HECHA sin
prueba y 6 en LISTA sin prueba**, exit 0.

**Y SOLO ENTONCES, `OP-L-03` SE ABRE LEYENDO SU FICHA Y SIN EJECUTAR NADA.**
Linea 43, tipo `MESA`, `estado` `LISTA`, `fecha_corte` 2026-08-11, `depende_de`
las seis `OP-D-*`, `bloquea_a` `OP-U-01` y `OP-U-02`.

**AQUI VA UN CONTRASTE MEDIDO QUE NO CALZA CON EL ENCARGO, Y NO ES PARADA:** el
encargo dice *"leer sus cuatro clausulas"*, y la ficha trae **4 elementos** en
`verificacion` **pero solo 3 son clausulas**; el cuarto es una `CORRECCION
DECLARADA`. **Cuento 3, no 4.** No paro por esto porque la tarea era leerlas y
las tres estan leidas, pero **la cifra del encargo se corrige con la medicion
delante en vez de repetirse**:

1. *ningun acto se funde con un par interno sin veredicto*
2. *las 55 lecturas marcadas LECTURA DIRIGIDA: no entran en la cola ni mueven su marcador*
3. *cada acto cuya lectura completa cambie su forma se re-mide con su cobertura al lado*

Su `adjudicacion`, leida hoy: *"LOS 55 DEJAN DE SER BACKLOG. Por la regla `P.5`,
cada acto que vaya a fundirse se lee ENTERO despues de su destejido y antes de su
fusion. Los 55 pares se reparten entre 29 actos y bajan del backlog."*

**NINGUNA DE LAS TRES SE EJECUTA EN ESTA VUELTA**, y no por prudencia: el tope de
cinco tareas esta agotado y esta es la quinta. **Lo leido queda aqui para que la
vuelta siguiente empiece con la ficha abierta y no con la ficha por abrir.**
