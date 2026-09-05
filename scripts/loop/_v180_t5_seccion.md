### TAREA 5. EL BACKLOG DE `OP-L-02`, MEDIDO Y NO LEIDO

**NI UN PAR LEIDO, Y VA MEDIDO Y NO PROMETIDO.** El bloque `H)` del instrumento
publica lo que esta corrida NO hizo: **pares leidos 0, veredictos escritos 0,
filas anadidas al archivo 0, marcador tocado no, estado de fichas tocado no,
nodos tocados 0.**

**LA VARA DEL FUNDADOR, CORRIDA HOY**
(`scripts/loop/vuelta150_3_relectura_expediente.py --corte <HEAD>`) sigue dando
**cuatro fichas de trabajo real**: `OP-L-01`, `OP-L-02`, `OP-L-03` y `OP-I-01`,
mas dos CONSUMIDAS (`OP-M-02-MEDIOS` y `OP-M-02-ADMIT`, por `OP-U-01`). Publica
las dos cifras, **6 en LISTA sin prueba, de las cuales 4 son trabajo real**, y
**la cifra vieja no se poda**. Y se repite lo que el encargo manda: **la vara es
esa salida y nunca el campo `estado`**, que para `OP-L-02` dice `LISTA` con
`fecha_corte 2026-08-11`.

**EL INSTRUMENTO NUEVO ES HERMANO DEL QUE CERRO `OP-L-03`:**
`scripts/loop/backlog_l02_resuelto.py`, **nombre estable y sin numero de vuelta**,
solo lectura. Corre el instrumento viejo **por dentro** importando `leer_nominas()`
de `scripts/loop/vuelta169_tarea5_cobertura_op_l_02.py`, que parsea la constante
`NOMINAS_OP_L_02` de `scripts/vuelta16_generar_actos.mjs`. **Ninguno de los dos se
toca.**

**LOS PARES QUE DA EL INSTRUMENTO, Y LOS PARES REALES, LAS DOS COLUMNAS Y LA
VIEJA NO SE BORRA** (`banco 9.10`). Salida:
`docs/loop/SALIDA_V180_T5_BACKLOG_L02.txt`, exit **0**, corte
**HEAD `0d3073204d57`**:

| cifra | valor | se mueve dentro de una vuelta |
|---|---:|---|
| nominas que el instrumento da | **6** | no, sale de una constante sellada |
| **PARES QUE EL INSTRUMENTO DA** (la cifra vieja) | **66** | no, sale de la misma constante |
| pares DISUELTOS tras resolver | **17** | SI, con su corte |
| pares DISTINTOS tras resolver | **46** | SI, con su corte |
| pares que YA TIENEN VEREDICTO, por el par RESUELTO | **31** | SI, con su corte |
| pares con LECTURA DIRIGIDA escrita | **16** | SI, con su corte |
| **PARES REALES contra el archivo** (la definicion literal del encargo) | **15** | SI, con su corte |
| **PARES REALES contra las DOS sedes** (lo que queda de verdad) | **0** | SI, con su corte |

**POR QUE HAY DOS COLUMNAS DE REALES Y NO UNA, dicho antes de contar:**
`OP-L-03` tenia UNA sede de clase y `OP-L-02` tiene **DOS**. La definicion literal
del encargo (*"los que no estan ya en el archivo tras resolver a nodo vivo"*) da
**15**; esos quince **estan leidos**, pero como **LECTURA DIRIGIDA**, que por su
propia definicion no entra en la cola y no mueve el marcador. Contarlos como
trabajo pendiente seria mandar a releer lo ya leido; no contarlos escondería que
no estan en el archivo. **Van las dos, y sin las dos al lado la cifra enganaria en
un sentido o en el otro.**

**LOS DOS CAMINOS CALZAN EN LAS SEIS NOMINAS.** `6 de 6`, y `0` donde no calzan,
las dos cifras con su corte pegado. El instrumento cae en **exit 1** si alguna no
calza, nombrandola.

| nomina | miembros | vivos resolutor | vivos grafo | calzan | del instrumento | disueltos | con veredicto | con dirigida | REALES archivo | REALES dos sedes |
|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|
| `customer_validation_sales_roadmap` | 6 | 6 | 6 | SI | 15 | 0 | 10 | 5 | **5** | **0** |
| `clasificacion_mercados_cadena_suministro` | 6 | 1 | 1 | SI | 15 | 15 | 0 | 0 | **0** | **0** |
| `alineacion_etica_ia_negocio` | 5 | 5 | 5 | SI | 10 | 0 | 7 | 3 | **3** | **0** |
| `construccion_de_valor_percibido` | 5 | 5 | 5 | SI | 10 | 0 | 5 | 5 | **5** | **0** |
| `channels_hypothesis_physical` | 5 | 5 | 5 | SI | 10 | 0 | 8 | 2 | **2** | **0** |
| `formalizar_junta_asesora` | 4 | 2 | 2 | SI | 6 | 2 | 1 | 1 | **0** | **0** |

**EL REPARTO POR TRAMO, CON SU CORTE PEGADO**, y **el criterio se dice antes de
repartir**: una nomina esta YA MIRADA si alguno de sus pares tiene lectura
dirigida escrita, y SIN MIRAR si ninguno. No se teclea ninguna lista.

| tramo | nominas | pares del instrumento | reales contra el archivo | reales contra las dos sedes | corte |
|---|---:|---:|---:|---:|---|
| YA MIRADAS | **5** | **51** | **15** | **0** | HEAD `0d3073204d57` |
| SIN MIRAR | **1** | **15** | **0** | **0** | HEAD `0d3073204d57` |
| **todas** | **6** | **66** | **15** | **0** | HEAD `0d3073204d57` |

**LA UNICA NOMINA SIN MIRAR ES `clasificacion_mercados_cadena_suministro`, Y NO
HAY NADA QUE MIRAR EN ELLA:** sus **6 miembros escritos resuelven a UN SOLO nodo
vivo**, o sea que el acto **ya se fundio**, y sus 15 pares salen los quince como
disueltos. **Cero reales por las dos definiciones.**

**LA CIFRA VIEJA DE LA FICHA, CITADA COMO CONTRASTE Y NUNCA COMO FUENTE**
(`EJECUTOR.md` 2), leida de la propia ficha en la corrida: *"MEDIDO el 11 ago
2026: 205 pares fuera de cola, 11 leidos, 194 pendientes"*, `fecha_corte
2026-08-11`. **LA DISCREPANCIA SE DECLARA EN VEZ DE RESOLVERSE COPIANDO: son
universos distintos.** La ficha mide los pares **fuera de cola de todo el
dominio**; esta corrida mide **las seis nominas que la constante declara**. Las
dos son verdaderas y **no responden la misma pregunta**.

**EL INSTRUMENTO CAYO EN ROJO EN SU PRIMERA CORRIDA, Y LO CAZO SU PROPIA GUARDA
DE RESTAS.** La corrida roja queda guardada sin retocar en
`docs/loop/SALIDA_V180_T5_BACKLOG_L02_ANTES.txt` (exit **1**): decia
`LA RESTA: del instrumento 66, menos 17 disueltos, menos 31 con veredicto, quedan
18. Y los REALES contra el archivo medidos son 15. CALZA: NO`. **La causa es
exactamente la que `backlog_l03_resuelto.py` declara en su `medir_acto()`:** dos
parejas de miembros ESCRITAS distintas pueden resolver AL MISMO par, y entonces
hay UNA lectura que hacer y no dos. Aqui son **3 duplicados** que colapsan. La
resta pasa a **cuatro pasos** y cada uno se publica:

| paso | cuenta | calza |
|---|---|---|
| 1 | del instrumento **66**, menos **17** disueltos, quedan **49** escritos | |
| 2 | de esos 49 escritos, los **DISTINTOS** tras resolver son **46**, o sea **3** duplicados | |
| 3 | de los 46 distintos, **31** ya tienen veredicto y quedan **15** | **SI** |
| 4 | de esos 15 reales, **15** tienen ademas lectura dirigida y quedan **0** | **SI** |

**LOS CINCO PARES DE SALES ROADMAP, NOMBRADOS Y DEJADOS.**
`docs/plan/LECTURAS_DIRIGIDAS.md` los deja expresamente como decision revocable
del fundador y el punto 8 del acta 179 los sube. **Aqui no se tocan**, y se dice
de que fichero salen, `docs/plan/LD_SALES_ROADMAP.md`:

| par | clase | sede |
|---|---|---|
| `customer_validation_sales_roadmap` contra `estrategia_de_ventas` | D | `LD_SALES_ROADMAP.md` |
| `customer_validation_sales_roadmap` contra `sales_roadmap` | D | `LD_SALES_ROADMAP.md` |
| `estrategia_de_ventas` contra `hoja_de_ruta_de_ventas` | A | `LD_SALES_ROADMAP.md` |
| `estrategia_de_ventas` contra `refinar_sales_roadmap` | D | `LD_SALES_ROADMAP.md` |
| `estrategia_de_ventas` contra `sales_roadmap_vs_sales_force` | D | `LD_SALES_ROADMAP.md` |

**EL CASO POSITIVO POR MUTACION**
(`scripts/loop/vuelta180_tarea5_mutacion_backlog_l02.py`, salida
`docs/loop/SALIDA_V180_T5_MUTACION.txt`, exit **0**): **16 comprobaciones, 0
fallan**, todo el material fabricado (mapa de alias, grafo, veredictos y lecturas
dirigidas), **sin leer el archivo, ni el grafo, ni `docs/plan/`, ni `dataset/`**.

| caso | que prueba | resultado |
|---|---|---|
| A | una nomina que colapsa a un nodo da **cero** reales y seis disueltos | pasa |
| B | **la contraprueba**: quitando el alias, los seis pares vuelven | pasa |
| **C** | **el caso que mordio hoy**: dos parejas escritas que son un solo par se cuentan **una vez**, y `distintos = con veredicto + reales` | pasa |
| C, la mutacion | contar escritos da **5** donde los distintos son **3**: **CAE** | pasa |
| D | un par con veredicto no es real; sin el veredicto vuelve a serlo | pasa |
| E | un par con lectura dirigida es real **contra el archivo** y no **contra las dos sedes** | pasa |
| F | si el grafo y el resolutor discrepan, `calzan` sale `False`, y con los dos de acuerdo sale `True` | pasa |

**LA NOMINA CRECE DE 107 A 108** con
`vuelta180_tarea5_mutacion_backlog_l02.py`. Recontada al cerrar esta tarea: censo
**168**, nomina **108**, `168 - 108 = 60` y fuera de la nomina **60**;
`arneses_que_faltan()` **0**, invisibles **0**, sujetos sin congelar **0**. El
sello entero: **`108 (corte: HEAD 0d3073204d57, nomina contada en esta
corrida)`**. `backlog_l02_resuelto.py` **no entra**, por la vara de siempre: su
nombre no trae ninguna de las tres familias del censo.
