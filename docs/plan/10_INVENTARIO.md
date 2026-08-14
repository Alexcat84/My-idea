# FASE 10: EL INVENTARIO NAVEGABLE

**La vista humana de `INVENTARIO.jsonl`.** Una entrada por **sujeto**: dominio,
racimo, acto, familia de ids, figura y defecto.

> **AQUI NO SE MIDE NADA NUEVO. Es consolidacion de lo ya escrito**, y **todo lo
> que se copia lleva su fecha de corte**. Lo que no existe todavia **se escribe
> como HUECO NOMBRADO, no se rellena.**

~~**FECHA DE CORTE DE TODO EL INVENTARIO: 11 ago 2026, cribado al puesto 2.117 de
3.388.**~~ Se recomputa entero con el disparador de `08_VERIFICACION`.

> ## AVISO QUE GOBIERNA ESTE DOCUMENTO ENTERO, puesto el 14 ago 2026 (vuelta 17)
>
> **ESTA VISTA HUMANA ESTA AL CORTE 2.117 Y SU ARCHIVO FUENTE YA NO.** Adjudicacion del
> discutible 3 de la vuelta 16 (`docs/loop/ACTA_AUDITOR.md` VUELTA 16 seccion 3, y punto 3 de
> `docs/loop/paradas/2026-08-14-credito-vuelta-16.md`).
>
> **LA TABLA NO SE REGENERA AQUI, A PROPOSITO:** la regla de arriba dice que este documento se
> recomputa ENTERO con el disparador de `08_VERIFICACION`, y regenerarlo es un trabajo de esa
> escala, no de esta vuelta. **Lo que se le pone es el aviso, no la cifra nueva en el sitio de la
> vieja.** Nada se borra: todas las cifras del 2.117 siguen escritas y legibles debajo.
>
> **LO QUE HAY QUE SABER ANTES DE LEER UNA SOLA FILA, medido en esta vuelta con
> `scripts/loop/vuelta17_acto_que_crecio.py` y `scripts/loop/vuelta17_marcar_221_superadas.py`
> sobre `docs/plan/INVENTARIO.jsonl` (corte de la medicion: 14 ago 2026, sobre el cribado cerrado
> en 3.388 de 3.388):**
>
> | | esta vista dice (corte 2.117, 11 ago 2026) | el archivo fuente tiene hoy (corte 3.388, 13 ago 2026) |
> |---|---:|---:|
> | filas de tipo `acto` | **221** | **556**, que son **221 SUPERADAS** mas **335 VIGENTES** |
> | filas totales | **336** | **671** |
> | los otros cinco tipos | 53 familias, 20 figuras, 19 defectos, 13 racimos, 10 dominios | **identicos, no se movieron** |
>
> **LAS 221 FILAS VIEJAS DEL ARCHIVO FUENTE YA ESTAN MARCADAS UNA A UNA** como `SUPERADA POR EL
> CORTE 3.388`, **cada una con el puntero a su sucesora vigente** (nombre mas `fecha_corte`
> 2026-08-13), en su campo `estado` y en su campo `nota`. **Ninguna se borro y ninguna cambio de
> `fecha_corte`.**
>
> **QUE SE PUEDE Y QUE NO SE PUEDE SACAR DE ESTE DOCUMENTO MIENTRAS EL AVISO ESTE PUESTO:**
>
> | se puede | NO se puede |
> |---|---|
> | leerlo como **el retrato del catalogo al puesto 2.117**, que es lo que fue y sigue siendo cierto de aquel corte | leer ninguna de sus cifras **como el estado de hoy** |
> | usar sus **razonamientos, formas, fronteras y huecos nombrados**, que no caducaron | citar su **conteo de actos, su total, ni su reparto por tamano** sin decir que son del 2.117 |
>
> **EL TOTAL DE HOY ES 671 Y NO ES UNA CORRECCION DEL 336: es otro corte.** El 336 sigue siendo la
> cifra correcta del 11 ago 2026 y no se toca.
>
> **UNA LINEA MAS AL AVISO, 14 ago 2026 (vuelta 18), adjudicacion del pendiente de doctrina 1 de la
> vuelta 17 (`docs/loop/ACTA_AUDITOR.md` VUELTA 17 seccion 4): LA FRASE "SIN PARES PENDIENTES: NO
> PUEDE CRECER" DE LAS NOTAS DE ACTO MIDE LOS PARES INTERNOS DEL ACTO, Y SOLO ESOS.** Una componente
> **tambien crece cuando entra un nodo de FUERA por una A nueva**, y eso la formula no lo ve.
> **Medido en esta vuelta con `scripts/loop/vuelta18_medir.py` sobre `docs/plan/INVENTARIO.jsonl` y
> `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`: 280 de las 335 notas de acto vigentes llevan esa frase**, y
> **el ejemplar que la desmiente es `gestion_terminacion_franquiciado`**: su entrada del corte 2.117
> decia "tamano 2. Sin pares pendientes: no puede crecer" con **1 de 1 pares leidos, 0 en cola y 0
> fuera de cola**, y hoy tiene **TRES miembros**, porque entro `perdida_control_operativo` **por la A
> del puesto 2190**, que es un par que la formula no contaba porque el tercer nodo estaba fuera.
>
> **LAS 335 NOTAS NO SE REESCRIBEN HOY, a proposito, por la misma razon que la tabla:** el arreglo es
> la regeneracion entera y esa la dispara `08_VERIFICACION`. **QUIEN REGENERE EL INVENTARIO ESCRIBE
> "SIN PARES INTERNOS PENDIENTES: NO PUEDE CRECER POR DENTRO."**

---

## EL VOLUMEN

| tipo | entradas |
|---|---:|
| **dominio** | **10** |
| **racimo** | **13** |
| **acto** | ~~**221**~~ **221 al corte 2.117. Ver el AVISO: hoy el archivo fuente tiene 556 filas de tipo `acto`, 221 superadas mas 335 vigentes** |
| **familia_de_ids** | **53** |
| **figura** | **20** |
| **defecto** | **19** |
| **TOTAL** | ~~**336**~~ **336 al corte 2.117. Ver el AVISO: hoy el archivo fuente tiene 671 filas** |

> **Las cifras tachadas de esta tabla NO estan mal: son del corte 2.117 y siguen siendo correctas
> de ese corte** (banco 9.21, la cifra vieja no se actualiza sola y no se borra). **Lo que esta
> mal es leerlas como el estado de hoy.** Las tres filas que no llevan tachado (`familia_de_ids`,
> `figura`, `defecto`) y las dos de arriba (`dominio`, `racimo`) **se remidieron en la vuelta 17 y
> siguen identicas en el archivo fuente**, por eso no llevan aviso.

---

## POR DOMINIO

**Diez dominios vivos. Seis han pasado por el cribado intra, CINCO estan cerrados,
y CUATRO no han entrado nunca.**

| dominio | nodos vivos | pares leidos | A | tasa | estado |
|---|---:|---:|---:|---:|---|
| **compras** | 46 | 155 | 1 | 0,6% | CERRADO |
| **core** | 1618 | 1.445 | 344 | 23,8% | CERRADO |
| **entrega** | 47 | 171 | 2 | 1,2% | CERRADO |
| **environmental** | 289 | 170 | 29 | 17,1% | CERRADO |
| **exportacion** | 141 | 130 | 15 | 11,5% | CERRADO |
| **franquicias** | 195 | 46 | 9 | 19,6% | **abierto y bajando** |
| `health_safety` | 283 | 0 | 0 | | **SIN CRIBAR** |
| `quality` | 792 | 0 | 0 | | **SIN CRIBAR** |
| `risk_management` | 55 | 0 | 0 | | **SIN CRIBAR** |
| `seguridad_digital` | 55 | 0 | 0 | | **SIN CRIBAR** |

> **HUECO NOMBRADO, y es el mayor del inventario: CUATRO DOMINIOS NO HAN ENTRADO
> AL CRIBADO INTRA.** `quality` (792 nodos), `health_safety` (283),
> `risk_management` (55) y `seguridad_digital` (55). **Son 1.185 nodos vivos, un
> tercio del catalogo, sobre los que este inventario no dice nada.**

> **Y la tasa de `franquicias` NO se puede leer como esta:** el dominio esta
> abierto, y por el banco 9.27 **la cola del dominio se agota por dentro**. El
> 19,6% de hoy **va a bajar**, como bajo `exportacion` de 36,0% a 11,5%.

---

## LOS ACTOS

**Un ACTO es una componente conexa de la relacion gemelo** (banco 9.24): si A
repite con B y B con C, los tres se deciden juntos.

> **TODA ESTA SECCION ESTA AL CORTE 2.117 Y NO SE REGENERA AQUI. Ver el AVISO de la cabecera.**
> **Las cifras de hoy, remedidas en la vuelta 17 (14 ago 2026) sobre las 335 filas vigentes de
> `docs/plan/INVENTARIO.jsonl`, van al lado de cada cifra vieja y no en su lugar.**

| | ~~corte 2.117~~ | **corte 3.388, vigente** |
|---|---:|---:|
| **actos** | ~~**221**~~ | **335** |
| nodos implicados | ~~**576**~~ | **854** |
| **CERRADOS**, listos para fundir | ~~**173**~~ | **280** |
| **ABIERTOS**, esperan al recomputo | ~~**48**~~ | **55** |

**POR TAMANO:**

| miembros | ~~actos al 2.117~~ | **actos al 3.388, vigente** |
|---:|---:|---:|
| 2 | ~~154~~ | **244** |
| 3 | ~~39~~ | **56** |
| 4 | ~~12~~ | **16** |
| 5 | ~~7~~ | **7** |
| 6 | ~~4~~ | **5** |
| 7 | ~~2~~ | **2** |
| 8 | ~~1~~ | **1** |
| 9 | ~~1~~ | **1** |
| 10 | ~~ninguno~~ | **1** |
| 13 | ~~1~~ | **1** |
| 15 | ~~ninguno~~ | **1** |

> **LAS DOS COLUMNAS SON CORRECTAS, cada una de su corte, y por eso conviven.** La columna
> vigente se midio en esta vuelta contando las 335 filas de `fecha_corte` 2026-08-13 por el largo
> de su campo `miembros` y por la palabra CERRADO u ABIERTO de su campo `estado`; suma 335 en las
> dos particiones (280 mas 55, y la columna por tamano).
>
> **UNA DIFERENCIA DE ETIQUETA QUE APARECE AL REMEDIR Y SE DECLARA EN VEZ DE CUADRARSE:** contando
> las 221 filas viejas por la palabra de su campo `estado`, salen **173 CERRADOS, 47 ABIERTOS y
> UNA que no dice ninguna de las dos**, el acto de la junta asesora, cuyo `estado` dice *"repite,
> DECISION TOMADA por `OP-M-04`"*. **La fila de arriba dice 48 abiertos porque cuenta a esa entre
> los abiertos.** No es una caida de nadie ni mueve ninguna decision: **173 mas 47 mas 1 son los
> mismos 221**, y la del `OP-M-04` no esperaba al recomputo, esperaba a una mesa que ya la
> resolvio. Se deja escrito para que quien recompute esta vista con `08_VERIFICACION` sepa que
> ese 48 es una etiqueta y no un conteo distinto.

**LOS SEIS MAYORES, y CUATRO no se funden aqui:**

| miembros | el acto | donde se resuelve |
|---:|---|---|
| **13** | puertas y portafolio | **`OP-M-01`**, mesa |
| **9** | customer discovery | **`OP-M-05`**, mesa |
| **8** | build, measure, learn | fusion |
| **7** | customer validation | **`OP-M-05`**, mesa |
| **7** | el brainstorming | **`OP-D-04`**, destejido con decision de fuente |
| **6** | cuatro empatados | pruebas A/B en `OP-D-03`; los otros tres, fusion |

> **Cuando un acto es grande, casi nunca es una fusion limpia.** Los de 13, 9 y 7
> llegaron a serlo **porque el catalogo trato el mismo programa de varias
> maneras**, y eso es una decision de forma.

> **AVISO SOBRE ESTA TABLA EN CONCRETO, vuelta 17: ~~el acto mayor del catalogo tiene 13
> miembros~~ ya no.** Remedido sobre las 335 filas vigentes (corte 3.388): **el mayor tiene
> QUINCE**, `cultura_de_seguridad_interpretivista_funcionalista`, y hay otro de **DIEZ**,
> `causas_comunes_vs_especiales`. **Los dos estan ABIERTOS y los dos cuelgan solo de `OP-U-02`:
> no aparecen en esta tabla porque no existian al corte 2.117, no porque se hayan omitido.** El
> resto de la tabla sigue calzando en su corte. **No se regenera aqui** (disparador de
> `08_VERIFICACION`): se avisa.

---

## LOS RACIMOS, con su forma medida

**Trece racimos con nombre.** La forma **no** es una etiqueta permanente: **es lo
que se sabe con la cobertura que tiene.**

| racimo | forma | cobertura | estado |
|---|---|---|---|
| **el efectivo contra la ganancia** | PURO | 3 de 3 | sano, forma cerrada |
| **la ecuacion de valor** | MEZCLADO | 10 de 10 | repite, forma cerrada |
| **el sales roadmap** | MEZCLADO | 10 de 15 | repite, cobertura INCOMPLETA |
| **la competencia entre inversores** | SUB-PURO | 7 de 10 | repite, DEGRADADO y RECONCILIADO el 11 ago 2026, cobertura INCOMPLETA |
| **la junta asesora** | MEZCLADO | 6 de 6 | en mesa, forma cerrada |
| **los cuadrantes de mercado** | MEZCLADO | 15 de 15 | repite, forma cerrada |
| **build, measure, learn** | SUB-PURO | 9 de 28 | repite, cobertura INCOMPLETA |
| **el compromiso contado tres veces** | PURO | 3 de 3 | sano, forma cerrada |
| **la seleccion de canal** | MEZCLADO | 10 de 10 | repite, forma cerrada |
| **la supervision de la IA** | PARTIDO 5 mas 4 mas 1 | ~~14 de 45 al puesto 1517~~ **18 de 45 al corte 3.388 (vuelta 15)** | en mesa, particion PROVISIONAL |
| **la mesa unida de puertas y portafolio** | DOS MITADES con frontera declarada, y una sola fusion dentro | ~~49 de 136~~ **54 de 136 (vuelta 16)** | MESA ADJUDICADA el 12 ago 2026: LAS DOS MITADES QUEDAN, con frontera adoptada |
| **el racimo del pivote** | SIETE NODOS A TRES: dos puertas y el acto al que las dos llevan | 13 de 21 | MESA ADJUDICADA el 12 ago 2026: DOS PUERTAS MAS UN ACTO |
| **la serie de Coleman** | MEZCLADO | 45 de 378 | MESA ADJUDICADA el 12 ago 2026, siete operaciones hijas |

> **TRES SUB-PUROS CAYERON EL 11 ago 2026 al cerrarse su cobertura**: los
> cuadrantes, la ecuacion de valor y el bloque humano de la IA. **Los tres pasaron
> a MEZCLADO en cuanto se termino de leerlos**, y por la razon que el banco ya
> tenia escrita: **el sub-puro es una promesa, no un resultado.**

**LOS DOS HUECOS SE CERRARON EL 11 ago 2026.** El **racimo del pivote** y la
**serie de Coleman** ya tienen nomina por id, medida con el contador mas el barrido
de las A y escrita en su bloque de apertura de `06_MESAS`.

| nomina | miembros | cobertura | lo que trae a su mesa |
|---|---:|---|---|
| **el racimo del pivote** | **7** | **13 de 21**, MEZCLADO | **las cuatro A no hacen un acto, hacen TRES**, cosidos entre si por **seis dudosos** |
| **la serie de Coleman** | **27** *(19 programa, 8 medios)* | **38 de 351**, MEZCLADO | **la fase 3 YA recibio el tratamiento que la mesa debate**: `fase_affirm_buyers_remorse` lleva tres alias dentro |

**Y LA CIFRA QUE PEDIA RE MEDIRSE SE RE MIDIO, Y BAJO**: *la competencia entre
inversores* se declaro **PURA con 4 miembros y 6 pares al puesto 1030**; la
componente medida al puesto 2.117 tiene **5 miembros y 10 pares**, con **7 leidos y
los 7 en A**. **DEGRADA a SUB-PURO, cobertura 7 de 10.** El quinto miembro,
`tecnica_anclaje_negociacion`, entro por una A **posterior a la declaracion** (el
puesto 878), y **los tres pares que faltan son suyos y estan fuera de cola.**

> **La degradacion no desmiente ninguna lectura: los siete pares leidos siguen
> siendo siete A.** Dice otra cosa, y es la que vale: **la forma se declaro sobre
> una componente que todavia iba a crecer.**

**Y LA DEGRADACION QUEDO RECONCILIADA EL MISMO DIA, que es lo que la cierra.** Ese
quinto miembro **ya se habia mirado y ya se habia dejado fuera con motivo escrito**
en el puesto **878**, el primer uso del barrido de las A: *su objeto es como
negociar terminos y no como generar competencia entre inversores*. **La exclusion no
se borra**, y ademas explica por que el racimo se declaro con cuatro.

**Manda la admision de hoy por tres razones que se suman**, y ninguna es *porque es
mas nueva*:

| | |
|---|---|
| **1** | el propio archivo, en el puesto **1295** y por tanto **despues** de la exclusion y de la declaracion de puro, escribe que ese nodo **tiene una A vigente y ES GEMELO** de `construccion_de_leverage` |
| **2** | **las dos decisiones no hablan del mismo objeto**: la del 878 decide el **TEMA** del racimo; la de hoy decide el **ACTO**, que por el banco 9.24 es el cierre transitivo de la relacion gemelo **y no admite gusto** |
| **3** | **la forma publicada se calculo sobre el ACTO**, no sobre el tema: *puro, cuatro miembros, seis pares* es una cuenta de componente conexa, y por el banco 9.17 **manda la medicion** |

> **LO QUE DE VERDAD PASO: se declaro una forma de ACTO sobre una nomina de TEMA.**
> Mientras el quinto no tuvo A, las dos coincidian. **Desde el puesto 878 dejaron de
> coincidir, y la etiqueta se quedo con la cuenta vieja.**

> **Y EL DESEMPATE VA EN LOS DOS SENTIDOS.** Si los tres pares fuera de cola salen
> **A**, vuelve a PURO con cinco. Si salen **D**, el quinto sale del acto y vuelve a
> PURO con cuatro, **o sea gana la exclusion del 878**. **Tres lecturas lo
> resuelven**, y por eso las dos decisiones se quedan con su fecha y ninguna se
> tacha.

La correccion para el banco de la sesion A esta en `CORRECCIONES_A_APLICAR.md`,
**correccion 6**, con la reconciliacion entera dentro.

---

## LAS FAMILIAS DE IDS

**53 familias sobre 125 nodos vivos**, medidas con el criterio de la DECISION 4:
sufijo numerico, particulas, orden de palabras y sinonimo.

| miembros | familias |
|---:|---:|
| 5 | 2 |
| 4 | 2 |
| 3 | 9 |
| 2 | 40 |

**LAS CUATRO MAYORES:**

| familia | ids |
|---|---|
| `accion_correctiva` | `accion_correctiva`, `accion_correctiva_2`, `accion_correctiva_4`, `accion_correctiva_5`, `accion_correctiva_6` |
| `consejo_calidad` | `consejo_calidad`, `consejo_calidad_2`, `consejo_de_calidad`, `consejo_de_calidad_2`, `consejo_de_calidad_3` |
| `definiciones_operacionales` | `definiciones_operacionales`, `definiciones_operacionales_2`, `definiciones_operacionales_3`, `definiciones_operacionales_4` |
| `make_certain_programa` | `make_certain_programa`, `programa_make_certain`, `programa_make_certain_2`, `programa_make_certain_3` |

> **Todas se resuelven por `OP-S-09`, con continua o repite y fusion con alias.**
> La excepcion escrita se mantiene: **la transdominio y el `_2` de propiedad
> intelectual van por renombre, no por fusion**, porque en los dos el contenido
> esta sano.

---

## LAS FIGURAS

**Doce figuras de lectura con doctrina escrita.** No son defectos: **son formas que
el catalogo produce y que hay que saber distinguir.**

| figura | ejemplares | que es |
|---|---|---|
| **SUBCONJUNTO ESTRICTO** | 23 ejemplares | los pasos del corto viven dentro del largo y lo unico propio cabe en una linea |
| **LA VARA EN LOS DOS SENTIDOS (9.22)** | 2 polos, 3 ejemplares del primero y 2 del segundo | procedimiento en los dos: sanos, ENLACE MUTUO. Linea en los dos: repiten, fusion |
| **ESTRELLA (9.23)** | 9 ejemplares | un centro que repite con dos periferios que entre si son sanos. La septima es INVERTIDA: el centro es el corto |
| **TRIANGULO ABIERTO** | 2 ejemplares | tres nodos del mismo tema y los TRES pares en D: la fuente partio el tema en tres cortes reales |
| **EL ESQUELETO COMPARTIDO** | 3 ejemplares | misma forma de pasos, contenido distinto en cada uno. Es el contrario del subconjunto estricto |
| **LAS DOS ADUANAS** | 5 ejemplares | lo que el destino exige contra lo que el pais propio prohibe. Contra la regla ajena hay recurso, contra la propia no |
| **LA BIFURCACION** | 2 ejemplares | un nodo declara en su primer paso que NO es el otro |
| **LOS DOS PARES QUE NO SE CRUZAN** | 1 ejemplar | dos parejas gemelas cuyos cruces salen D: la duplicacion esta dentro de cada pareja |
| **LA FIRMA POSICIONAL DEL INJERTO (P.2)** | 67 nodos candidatos, 43 confirmados | el orden dentro del campo fuente lleva informacion: el segundo libro es lo pegado |
| **LA A DE BLOQUE (P.4)** | 1 ejemplar y 1 contraejemplo | la repeticion vive entre el bloque injertado y el otro nodo entero. Destejido mas fusion parcial, nunca fusion de enteros |
| **LA COLA DEL DOMINIO SE AGOTA POR DENTRO (9.27)** | 3 dominios medidos | la tasa de A cae dentro de cada dominio: un dominio a medio leer no describe al dominio |
| **EL PASO DE OFICIO** | medio dominio exportacion | una linea generica que abre media docena de nodos y por si sola no decide ninguna clase |
| **frontera de disposicion** | 5 ejemplares | Dos nodos que mandan LO CONTRARIO sobre el MISMO gesto, los dos con razon dentro de su doctrina. No es defecto y no se funde: se declara y los dos se quedan. LOS TRES EJEMPLARES: la FRONTERA INTRA LIBRO del puesto 877 (Founder's Dilemmas contra si mismo: autoridad clara contra estructura colegiada); la FRONTERA DE MOMENTO del 221 (Rackham no presionar el cierre contra Weinberg pedir un si o un no), probada por seis lados; y la FRONTERA DE LA DECISION DE PIVOTAR del 1298 (el punto brillante de Ries mas Traction contra decidir rapido y sin miedo de Blank), declarada el 12 ago 2026. LA TERCERA ES LA PRIMERA QUE QUEDA REPARTIDA EN DOS NODOS DISTINTOS del mismo racimo, entre una puerta y el acto que le sigue, lo que la hace mas facil de perder: los dos lados ya no estan uno al lado del otro. UNA FRONTERA SE PIERDE POR PODA, NO POR FUSION. AMPLIADO EL 12 ago 2026 CON DOS MAS, y las dos de clase distinta a las tres primeras. LA CUARTA, la frontera de los dos niveles, NO ES UNA CONTRADICCION SINO UNA DISTINCION, y es la primera que EL CATALOGO ESCRIBIO SOLO: gestion_portafolio_dos_niveles la lleva dentro de sus pasos, estrategicas contra tacticas y complementarias no sustitutivas, y es madre de las dos mitades tres veces (LD-35, LD-43, LD-51). LA QUINTA, discovery contra validation, es la MAS PROBADA DEL PLAN: quince pares leidos entre los dos actos y LOS QUINCE D, con el 445 y el 1477 citados, uno pregunta y el otro cobra. Ninguna de las dos necesitaba adjudicacion: necesitaba REGISTRO, porque el riesgo no es decidirlas mal sino perderlas por descuido en una fusion futura. |
| **el nombre que esconde** | 3 ejemplares | TRES VECES el contador dejo fuera a un miembro real porque su NOMBRE no llevaba la palabra del tema, y las tres veces lo cazo el segundo instrumento. (1) el sexto de los cuadrantes de mercado; (2) seis_medios_comunicacion_cliente, la cabeza de la serie de medios de Coleman, levantada por el veredicto 948; (3) decision_factory_mentality, miembro 17 de la mesa unida, levantado por las A de los puestos 1499 y 583, y que se llama Haz menos proyectos pero hazlos bien. EL FALLO ES EL MISMO: el nombre no dice algo falso, CALLA LO QUE EL NODO HACE. SE CITA COMO HISTORIA Y NO COMO RECOMENDACION: el estandar de los dos instrumentos ya estaba en el banco 9.20 antes de los tres casos. Lo que anaden no es la regla: es la cuenta de lo que habria costado no tenerla, tres nominas mal en tres mesas distintas. |
| **nodo puente** | 3 ejemplares, uno de ellos con TODAS sus lecturas hechas | UN NODO PUENTE es el que tiene A con dos nodos que entre si son D. La componente que forma puede ser UNA familia o DOS pegadas por el, y EL CIERRE TRANSITIVO NO LO DISTINGUE: las junta igual. REGLA DE DETECCION, y es la unica que hay: SOLO SE VE MIRANDO LA COMPONENTE ENTERA, leyendo un par jamas. ES LA MITAD DIAGNOSTICA DE P.5. TRES EJEMPLARES en dos dias. (1) sistema_gates_go_kill, A con gestion_de_portafolio_gates_go_kill (488) y con requisitos_gates_con_dientes (801), que son D entre si (LD-44); LD-58 lo cerro HACIA LA UNION y la anomalia se movio al propio LD-44. (2) filosofia_customer_validation con earlyvangelists_ventas_tempranas (1096), que es D con otros tres del acto; se resuelve releyendo contra el superviviente. (3) customer_validation Y filosofia_customer_validation a la vez, los dos A con customer_validation_sell_phase (781 y 245), que es D con introduccion_validacion_clientes (LD-59); AQUI YA NO QUEDA LECTURA QUE DESEMPATE y se funde solo el triangulo cerrado. EL TERCERO ENSENA QUE UN PUENTE PUEDE SER DOBLE: dos nodos haciendo de puente sobre el mismo par, y entonces la componente no tiene un punto debil, tiene una COSTURA. TRES SALIDAS Y NINGUNA ES FUNDIR A CIEGAS: leer el par que falta, releer contra el superviviente, o fundir solo el subconjunto cerrado y enlazar el resto. AMPLIADO EL 12 ago 2026 con las seis lecturas del acto de seis. EL PRIMER EJEMPLAR CAMBIO DE DUENO Y DE FORMA: el puente ya no es sistema_gates_go_kill, es gestion_de_portafolio_gates_go_kill, y ahora es EL EJEMPLAR MAS PURO QUE HA DADO EL PLAN porque no le falta ninguna lectura. Los quince pares del acto estan leidos: DOCE A y TRES D, y las tres D salen de ese nodo. La particion medida es CINCO MAS UNO: una camarilla de cinco con diez pares de diez leidos y los diez en A, la unica completamente cerrada por lectura de todo el plan, mas un nodo con DOS A y TRES D contra ella. Y EL PATRON NO ES ACCIDENTE: repite con LOS DOS NODOS MAS GENERALES, los que describen el gate como concepto, y sale sano contra LOS TRES QUE DESCRIBEN SU ANATOMIA. Repite con la IDEA de puerta y no con su ANATOMIA, que es lo que un nodo de portafolio necesita de una puerta. RESUELTA COMO DOCTRINA EL 12 ago 2026 CON P.12: EL CIERRE TRANSITIVO CONVOCA, LA LECTURA DECIDE. El 9.24 define el universo del acto, no la membresia de la fusion; con el acto leido entero mandan los veredictos directos; y el nodo mixto SE JUZGA CON LA VARA CONTRA EL SUPERVIVIENTE: si comparte la idea en lineas, continua con enlace mas poda del solape; si comparte procedimiento, entra. NI TRANSITIVIDAD AUTOMATICA NI MAYORIA, porque contar A contra D parece objetivo y no lee nada. EL SEXTO DE GATES quedo fuera y enlazado, con sus dos A COBRADAS EN LA PODA y sus tres D como motivo de que viva. |
| **la camarilla cerrada por lectura** | 1 ejemplar | CINCO nodos, DIEZ pares posibles, LOS DIEZ LEIDOS Y LOS DIEZ EN A. Es la UNICA componente de todo el plan sin un solo par pendiente y sin una sola excepcion. POR QUE IMPORTA TENERLA NOMBRADA: es la unica fusion del plan que no necesita lectura de acto por P.5, porque su acto YA esta leido entero. En todas las demas, P.5 es una condicion; aqui es un hecho. SE LLEGO A ELLA POR ENCARGO Y NO POR SUERTE: cinco de sus diez pares se leyeron el 12 ago 2026 como lectura dirigida, precisamente para cerrarla. ADJUDICADA EL 12 ago 2026. SUPERVIVIENTE sistema_gates_go_kill, por P.8 EN ORDEN y con las dos vias apuntando al mismo nodo: el CONTENIDO, porque el veredicto 801 mide TRES piezas propias suyas contra DOS de requisitos_gates_con_dientes sobre un eje que se repite entero; y el CABLEADO, 9 contra 7, 5, 5 y 4. Diez perdidas viajan, recomputadas sobre la nomina final. |
| **la perdida que cambia de dueno** | 15 reclasificadas | UNA PERDIDA SE DECLARA CONTRA UN PAR Y SE COBRA CONTRA UNA NOMINA. Cuando la nomina cambia, toda perdida listada se recomprueba y la que viva dentro se reclasifica con su dueno. PASADA CORRIDA EL 12 ago 2026 SOBRE LAS QUINCE FUSIONES CON PERDIDAS: 15 reclasificadas de 47. TRES CLASES: VIAJA, la pieza no esta en ningun nodo vivo de la nomina; VIVE DENTRO, ya esta en el superviviente o en otro que sobrevive, y se tacha; YA NO APLICA, era de un nodo que dejo de entrar en la fusion y se la queda. POR QUE IMPORTA Y NO ES BUROCRACIA: una perdida falsa OBLIGA A INJERTAR EN EL SUPERVIVIENTE ALGO QUE YA ESTA, y asi es como se fabrica una repeticion nueva el dia de la pasada. La operacion que limpia seria la que ensucia. DOS PERDIDAS APARECIERON QUE NADIE HABIA LISTADO, y las levanto el mismo recomputo: los ENTREGABLES de la camarilla de cinco, que el superviviente no tiene y tres de los que mueren si, y LAS DOS ADVERTENCIAS de gates_go_kill_decision_points, que por P.11 son linea para la vara y perdida para la fusion. |
| **cobrar una A sin fundir** | 1 ejemplar | PLANTILLA PARA TODO NODO MIXTO QUE P.12 DEJE FUERA DE UNA FUSION. Una A es un dato y no una orden: dice que hay un bloque que repite, no que los nodos sean el mismo nodo. TRES PASOS: (1) el enlace, una arista de la madre al hijo en una sola direccion; (2) la poda del solape, el bloque que la A senala deja de reformular y pasa a citar la arista; (3) lo propio se queda, porque es el motivo de que el nodo viva. NO ES UNA FUSION A MEDIAS: una fusion resuelve la repeticion BORRANDO UN NODO y esta la resuelve BORRANDO UN BLOQUE. El resultado por el lado que importa es el mismo, la instruccion deja de estar dos veces, y se conserva lo que la fusion habria arrastrado. EL COSTE DE NO HACERLO ES DOBLE: el catalogo se queda con el bloque repetido Y sin la arista, que es el estado en que la mesa unida encontro sus dos mitades. |
| **el superviviente es de la nomina, no del nodo** | 1 ejemplar | UNA FUSION QUE CRECE RE MIDE TAMBIEN A SU SUPERVIVIENTE. P.13 recomprueba las perdidas al cambiar la nomina; el corolario recomprueba al superviviente, porque se elige por P.8 CONTRA LOS QUE ESTABAN. EJEMPLAR: el trio de gates elegia requisitos_gates_con_dientes porque contenia a los otros dos; como camarilla de cinco gana sistema_gates_go_kill, porque el veredicto 801 mide tres piezas propias suyas contra dos. NINGUNA LECTURA CAMBIO: cambio la nomina, y con ella el ganador. No se hereda el superviviente de la operacion pequena. |
| **el forastero por cableado** | 2 ejemplares | UN NODO ENTRA A UNA NOMINA POR EL NOMBRE Y SE QUEDA FUERA POR TODO LO DEMAS: sus lecturas contra la nomina salen sanas y sus aristas apuntan a otro vecindario. DOS EJEMPLARES. (1) tacticas_cierre_ventas, llamado durante mucho tiempo el octavo miembro del racimo del cierre: seis lecturas, una sola contra miembros del cierre y sale D, y su unica A es con un nodo que no es del cierre. Tiene su propio acto de dos. (2) incentivos_no_monetarios_advocacy, en la serie de Coleman por fuente y por nombre: CUATRO lecturas contra la serie y LAS CUATRO D (LD-28, LD-30, LD-31 y su cruce), y sus dos aristas van a equity_crowdfunding_terminos y a coeficiente_viral, o sea al mundo del crecimiento viral. COMO SE DETECTA: cuando una nomina se cierra por lectura, el forastero es el miembro que sale sano contra TODOS los demas. Y el cableado lo confirma sin ambiguedad: no comparte ni un vecino con el resto. POR QUE IMPORTA: un forastero no es un error del catalogo, es un error de la NOMINA. El nodo esta bien; lo que esta mal es la lista donde se le puso, y mientras siga ahi TODA FORMA que se calcule sobre esa nomina sale peor de lo que es. |

---

## LOS DEFECTOS, por clase y con su cuenta

| defecto | cuantos | estado | operaciones |
|---|---:|---|---|
| **aristas duplicadas tras resolucion** | 1056 | reparado en el plan | `OP-S-12`, `OP-C-05` |
| **aristas que faltan** | 477 | pendiente, BOLSA RECALIBRADA y tasa MEDIDA | `OP-E-01`, `OP-E-03` |
| **jerarquias nombradas y sin cablear** | 293 | reparado en el plan | `OP-E-06`, `OP-E-07` |
| **grafias no canonicas del campo fuente** | 129 | reparado en el plan | `OP-S-11` |
| **alias huerfanos** | 77 | reparado en el plan | `OP-S-08` |
| **marco de un solo pais** | 73 | reparado en el plan | `OP-S-10` |
| **gemelos que el cribado no ve** | 73 | pendiente, se recoge por DIFERENCIA CONTRA LA COLA | `OP-E-03` |
| **injertos de fuente** | 67 | reparado en el plan | `OP-F-01`, `OP-F-02`, `OP-F-03` y mas |
| **costuras internas confirmadas** | 46 | pendiente | `OP-D-01`, `OP-D-02`, `OP-D-03` y mas |
| **auto-aristas via alias** | 27 | reparado en el plan | `OP-S-07`, `OP-C-04` |
| **accesos al grafo sin resolver** | 20 | reparado en el plan | `OP-C-01`, `OP-C-02`, `OP-C-03` |
| **pares que una fusion reabre** | 7 | pendiente, con disparador escrito en 08_VERIFICACION | `OP-U-02` |
| **campos sucios** | 6 | reparado en el plan | `OP-S-06` |
| **herramientas muertas** | 6 | reparado en el plan | `OP-S-04`, `OP-S-05` |
| **error de dejar pasar** | 4,2%, banda 0,7 a 20,2 | MEDIDO el 12 ago 2026, un volteo propuesto a la sesion A | `OP-U-02` |
| **Incoterms sin version** | 3 | reparado en el plan | `OP-S-02` |
| **portal caducado export.gov** | 3 | reparado en el plan | `OP-S-03` |
| **racimos con miembro de otro dominio** | 3 | pendiente | `OP-E-02` |
| **tratado extinto en id y titulo** | 1 | reparado en el plan | `OP-S-01` |

> **13 de los 19 ya tienen operacion LISTA en el plan.** Los 6 pendientes son: **costuras internas confirmadas** (46), **aristas que faltan** (477), **racimos con miembro de otro dominio** (3), **gemelos que el cribado no ve** (73), **pares que una fusion reabre** (7), **error de dejar pasar** (4,2%, banda 0,7 a 20,2).

> **Y el mas nuevo de todos es el ultimo de esa lista: los GEMELOS QUE EL CRIBADO NO
> VE.** Aparecio el 11 ago 2026 leyendo la bolsa calibrada, **no se busco**, y son
> unos 73 pares con banda de 36 a 135. **Seis de los siete ejemplares medidos estan
> en `quality`, que no ha entrado nunca al cribado.**

> **LA BOLSA DE LAS ARISTAS QUE FALTAN BAJO DE 624 A 477** con la senal del verbo, y
> su tasa dejo de ser proyeccion: **32 sanas, 7 gemelos y 7 basura en 46 lecturas
> pineadas**. **Con su limite escrito al lado, que es la cifra que nadie debe
> soltar: la senal del verbo SOLO OPINA CUANDO CONOCE LAS DOS FAMILIAS DE ACCION, y
> sobre los 477 las conoce en 104, el 21,8%.** Los 477 no son una bolsa filtrada del
> todo: **son una bolsa filtrada en el quinto de sitios donde el instrumento tenia
> con que comparar.**

---

## LAS FUENTES, ya normalizadas

**55 libros canonicos** detras de **129 grafias distintas**. La normalizacion es
`OP-S-11` y **es prerrequisito de la aduana**.

| | |
|---|---:|
| nodos vivos | **3.521** |
| grafias distintas en primera posicion | **129** |
| **libros canonicos** | **55** |
| nodos con **mas de un libro** | **67** |
| **libros que aparecen en segunda posicion** | **6** |

**LOS SEIS QUE APORTAN INJERTOS, y los otros 49 no aportan ninguno:**

| libro | 1a o unica | **2a o posterior** |
|---|---:|---:|
| Essentials of Supply Chain Management, Hugos | 107 | **21** |
| Never Lose a Customer Again, Coleman | 68 | **15** |
| The Hard Thing About Hard Things, Horowitz | 88 | **14** |
| Traction, Weinberg | 67 | **13** |
| SPIN Selling, Rackham | 47 | **4** |
| Co-Intelligence, Mollick | 47 | **3** |

> **Los 43 de Coleman, Horowitz, Weinberg y Rackham se leyeron el 11 ago 2026 y
> salieron 43 de 43 CONFIRMADOS**, con cero arrastre. **Los 21 de Hugos ya estaban
> adjudicados y los 3 de Mollick tambien.**

---

## COMO SE LEE ESTE INVENTARIO

| si busca | mire |
|---|---|
| **que hay en un dominio** | la tabla por dominio, y **compruebe si esta cribado**: cuatro no lo estan |
| **si un nodo repite** | `INVENTARIO.jsonl`, entradas de tipo `acto`, campo `miembros`, **y de las dos familias de filas SOLO las 335 con `fecha_corte` 2026-08-13**. Las 221 con `fecha_corte` 2026-08-11 llevan `SUPERADA POR EL CORTE 3.388` al frente de su `estado` y el puntero a su sucesora en su `nota`: **estan para auditar, no para contestar** |
| **si una forma es firme** | el campo `cobertura`. **Toda forma con cobertura incompleta es PROVISIONAL** (banco 9.26) |
| **quien toca un sujeto** | el campo `operaciones` de su entrada |
| **cuando caduca lo que lee** | el campo `fecha_corte`, **fila por fila y no en bloque**. ~~**todo el inventario es del 11 ago 2026**~~ **YA NO ES CIERTO del archivo al que esta misma tabla manda**: `INVENTARIO.jsonl` tiene hoy DOS cortes conviviendo, 336 filas del 11 ago 2026 (corte 2.117) y 335 filas del 13 ago 2026 (corte 3.388). **ESTE DOCUMENTO si es entero del 11 ago 2026** |

> **LA ADVERTENCIA QUE GOBIERNA TODO EL DOCUMENTO: este inventario describe UN
> CATALOGO A DOS TERCIOS DE LEER.** 2.117 pares de 3.388, y cuatro dominios sin
> entrar. **Lo que dice es cierto; lo que no dice es la mayoria.**

> **Y LA SEGUNDA ADVERTENCIA, puesta el 14 ago 2026 (vuelta 17), que no deroga la primera sino
> que la fecha:** la de arriba sigue describiendo bien **este documento**, que es del corte 2.117.
> **Pero el cribado se cerro en 3.388 de 3.388 el 13 ago 2026, y el archivo fuente ya lo refleja
> y este documento no.** O sea que hoy **la advertencia de arriba es el estado de la VISTA, no el
> del catalogo**. Ver el AVISO de la cabecera. **Cuando `08_VERIFICACION` dispare la regeneracion
> de este documento, esta segunda advertencia se cae sola y la primera hay que reescribirla con
> el corte nuevo, no borrarla.**

