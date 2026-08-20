# REPORTE DE LA VUELTA 51 (20 ago 2026, ejecutor Opus 5)

**LA TAREA 1 ENTERA, cada una de sus tres correcciones tratada por SU ESPECIE. DE LA TAREA 2,
CUATRO ACTOS FUNDIDOS Y CINCO LECTURAS `P.12`. Y EL HALLAZGO DE LA VUELTA ME LO HIZO A MI MISMO
MI PROPIO INSTRUMENTO: la guarda que escribi para cumplir la cuenta de colisiones del encargo
MIRABA SOLO DENTRO DEL ACTO, dio el visto bueno a una fusion, y el censo del archivo entero
devolvio CINCO colisiones donde ella habia prometido TRES. El dataset se revirtio con `git
checkout`, el instrumento se reescribio para re-resolver los 3.388 veredictos, y los 25 mixtos
se re-midieron con la aritmetica buena antes de seguir.**

| | |
|---|---|
| **rama** | `pasada-unica` |
| **hash de apertura** | `6dcb01b9` (el acta de la vuelta 50), **arbol limpio y todo pusheado** |
| **commits de la vuelta** | **4**: `67bc64c3` (TAREA 1), `40b8eb80` (lote A), `a78c12e5` (lote B) y el del cierre |
| **arbol al cierre** | limpio tras el commit del cierre |

---

## 0. LA APERTURA, MEDIDA ANTES DE LA PRIMERA OPERACION (regla 1)

**Corrida ANTES de tocar nada**, con `python scripts/loop/vuelta31_estado.py APERTURA_V51`
([`SALIDA_V51_APERTURA.txt`](SALIDA_V51_APERTURA.txt)). **El arbol estaba limpio y todo pusheado
en `6dcb01b9`, asi que la regla 3 se cumplio por vacio, y se dice asi en vez de darla por
cumplida.**

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 571 / 77 / 8 / 2.732 | **566 / 77 / 8 / 2.737** |
| `n`, huecos, duplicados | 3.388 / 0 / 0 | **3.388 / 0 / 0** |
| tasa de `A` | 16,9 | **16,7** |
| grafo: ficheros / vivos / deprecados / enlaces | 3.853 / 3.498 / 355 / 16.986 | **3.853 / 3.492 / 361 / 17.011** |
| retrato: `A` crudas / colapsos / pares distintos | 571 / 49 / 522 | **566 / 57 / 509** |
| operaciones, estados, dependencias rotas | 71, todas `LISTA`, 0 | **71, todas `LISTA`, 0** |
| entradas del inventario | 672 | **672** |
| actos `CERRADOS` / `ABIERTOS` | 251 / 53 | **247 / 53** |
| nodos en `CERRADOS` / `ABIERTOS` | 532 / 240 | **518 / 240** |
| cola de costuras | 1.491 | **1.489** |
| duplicadas tras resolver (grupos) / auto-aristas | 1.002 / 0 | **1.001 / 0** |
| colisiones de clase vigentes | 0 | **0** |
| mixtos del tramo 1 pendientes de `P.12` | 25 | **21** |

**El cierre esta RECOMPUTADO al cierre** ([`SALIDA_V51_CIERRE.txt`](SALIDA_V51_CIERRE.txt),
[`SALIDA_V51_MARCADOR_CIERRE.txt`](SALIDA_V51_MARCADOR_CIERRE.txt),
[`SALIDA_V51_RECOMPUTO_CIERRE.txt`](SALIDA_V51_RECOMPUTO_CIERRE.txt),
[`SALIDA_V51_COLA_CIERRE.txt`](SALIDA_V51_COLA_CIERRE.txt)), **no copiado de la apertura.**

**Las cinco familias de libro no se mueven** (Weinberg 68/66, Horowitz 91/89, Hugos 111/111,
Coleman 74/72, Rackham 46/46). **Los dominios que se mueven son DOS**, medidos al cierre: `quality`
de `A 126` a `A 123` (14,9 a 14,6 por ciento) y `core` de `A 334` a `A 332` (23,1 a 23,0).

---

## 1. TAREA 1: LAS TRES CORRECCIONES, CADA UNA POR SU ESPECIE

**La regla que las separa es la que el acta de la vuelta 50 adjudico en su pregunta 5**, y esta
vuelta la aplico como criterio de clasificacion y no como formula
([`SALIDA_V51_CORRECCIONES_T1.txt`](SALIDA_V51_CORRECCIONES_T1.txt),
`scripts/loop/vuelta51_correcciones_tarea1.py`, cuatro sustituciones, todas idempotentes al
re-correrlas: [`SALIDA_V51_CORRECCIONES_T1_IDEMPOTENCIA.txt`](SALIDA_V51_CORRECCIONES_T1_IDEMPOTENCIA.txt)).

| | la especie | lo que se toco |
|---|---|---|
| **1.1** | **CIFRA QUE NACIO MAL**, no que envejecio | la fila *lecturas `P.12` encargadas y NO hechas* del registro de la vuelta 49: **25 tachado, 26 vigente**, con la salida que lo mide citada y el acta 50 como su relectura conjunta. **La fila hermana del registro de la vuelta 50, que dice 25 al cierre, NO se toco** |
| **1.2** | **ROTULO ENVEJECIDO**, la cifra se queda | la columna *numero en la vuelta 48 / hoy* de los cinco declarados: **el rotulo pasa a AL ABRIR LA VUELTA 50** y las cifras (7, 24, 26, 30, 31) quedan intactas, con nota de que al cierre eran 6, 23, 25, 29 y 30. **Misma vara al *hoy el acto 156* de los imposibles**, que al abrir la vuelta 51 es el **155** |
| **1.3** | **CORRECCION INCOMPLETA DE FORMA** | el checkpoint **ii** de la fila **528**: **525 tachado y 522 vigente en los DOS parentesis**, cadena de notas intacta |

**LA MEDICION QUE SOSTIENE 1.2, y no sale de ningun acta:** los cinco declarados eran **7, 24,
26, 30 y 31** al abrir la vuelta 50
([`SALIDA_V50_TRAMO1_POR_MIEMBROS.txt`](SALIDA_V50_TRAMO1_POR_MIEMBROS.txt)) y **6, 23, 25, 29 y
30** al cerrarla ([`SALIDA_V50_TRAMO1_CIERRE.txt`](SALIDA_V50_TRAMO1_CIERRE.txt)); al abrir la 51
seguian en **6, 23, 25, 29 y 30**
([`SALIDA_V51_TRAMO1_APERTURA.txt`](SALIDA_V51_TRAMO1_APERTURA.txt)). El segundo imposible por
puerta era el **156** al abrir la vuelta 50
([`SALIDA_V50_PUERTAS_EN_EL_LOTE.txt`](SALIDA_V50_PUERTAS_EN_EL_LOTE.txt)) y el **155** al abrir
la 51 ([`SALIDA_V51_PUERTAS_APERTURA.txt`](SALIDA_V51_PUERTAS_APERTURA.txt)).

### UN CUARTO SITIO DE LA MISMA ESPECIE, MEDIDO Y **NO TOCADO**

**El registro de la vuelta 49 tiene la misma especie de rotulo envejecido en su fila *los
declarados 29, 32 y 36 (hoy 26, 28 y 32)*.** Medido corriendo el instrumento de miembros contra
cuatro cortes distintos: **26, 28 y 32 es la numeracion de la APERTURA de la vuelta 49**; al
**cerrar** aquella vuelta ya eran **24, 26 y 30**
([`SALIDA_V51_TRAMO1_EN_CIERRE_V49.txt`](SALIDA_V51_TRAMO1_EN_CIERRE_V49.txt)) y al abrir la 51
son **23, 25 y 29**. **No se corrige porque el encargo scopeo la TAREA 1.2 al registro de la
vuelta 50 y el acta 50 hizo lo mismo.** Va como hallazgo y como pregunta, no como alcance
tomado por mi cuenta.

---

## 2. EL HALLAZGO DE LA VUELTA: **UNA FUSION NO SOLO CHOCA CONSIGO MISMA**

**El encargo pone una guarda de cuenta** (*una colision por cada `CONTINUA` sobre mixto CON
forma y CERO por cada `ENTRA`; una colision que no calce con esa cuenta te detiene*). Para poder
cumplirla ANTES de mover un nodo escribi `scripts/loop/vuelta51_colisiones_esperadas.py`. **Y la
primera version contaba las colisiones mirando SOLO LOS VEREDICTOS INTERNOS DEL ACTO.**

| | |
|---|---|
| que prometio | **TRES** colisiones para el lote A (los actos de la accion correctiva, del scorecard y del reparto de equity) |
| que salio | **CINCO**, medidas sobre el archivo entero tras ejecutar ([`SALIDA_V51_CENSO_COLISIONES_LOTE_A.txt`](SALIDA_V51_CENSO_COLISIONES_LOTE_A.txt), primera corrida) |
| las dos de mas | veredictos del absorbido `split_igual_vs_desigual` contra nodos de **FUERA del acto**: el **266** contra `reparto_inicial_equity` y el **246** contra `timing_equity_split`, que al resolver caian sobre los pares **754** y **688**, que el superviviente ya tenia leidos |

> **LA LECCION: absorber un nodo arrastra TODOS sus veredictos, tambien los que apuntan fuera del
> acto, y cada uno puede caer sobre un par que el superviviente ya tenia leido. Una guarda que
> solo mira dentro del acto TRANQUILIZA SIN MIRAR**, que es la misma especie de averia que la
> vuelta 50 encontro en el barrido `9.10`.

**QUE SE HIZO, y no fue seguir:** el dataset se revirtio entero con `git checkout -- dataset/`,
el censo confirmo la vuelta a **CERO** colisiones, el instrumento se reescribio para **simular el
mapa de alias y re-resolver LOS 3.388 VEREDICTOS**, y las 51 combinaciones de acto y superviviente
viable de los 25 mixtos se re-midieron
([`SALIDA_V51_COLISIONES_ESPERADAS.txt`](SALIDA_V51_COLISIONES_ESPERADAS.txt)).

| | combinaciones |
|---|---:|
| **CALZAN** con la cuenta del encargo | **46** |
| **NO CALZAN** (colisiones fuera del acto) | **5**, en cuatro actos: el del equity, el de los habitos, el del *value proposition canvas* (los dos viables) y el de los warrants |

### Y UNA FORMA DE CONTAR QUE ESTA VUELTA TUVO QUE FIJAR

**LA COLISION SE CUENTA POR PAR RESUELTO, NO POR VEREDICTO.** El par
`consejo_de_calidad` contra `consejo_de_calidad_3` lleva **TRES** veredictos dentro (**2523** `A`,
**2662** `A`, **2916** `D`) y es **UNA** colision: los dos `A` se voltean, el `D` se queda. **Con
esa forma de contar la cuenta del encargo calza; contando veredictos, no.** Es decision de lectura
y va marcada (**D9**).

---

## 3. LOS CUATRO ACTOS FUNDIDOS Y LAS CINCO LECTURAS `P.12`

**Las cinco salieron `CONTINUA`, y ninguna por descarte:** en las cinco el veredicto DIRECTO del
par mixto ya era `D` y ya traia escrito por que. **En el de los cofundadores el propio veredicto
escribe la palabra** (el **1058**: *por la vara del banco `9.6.1`, CONTINUA*).

| lote | superviviente | absorbe | el mixto, `CONTINUA` contra el | colision limpiada |
|---|---|---|---|---|
| **A** | `accion_correctiva_sistematica` | `accion_correctiva_5`, `accion_correctiva_6` | `accion_correctiva_crosby` (2805) | **2426** `A` a `D` |
| **A** | `scorecard_de_seleccion_de_proyectos` | `scoring_model_scorecard` (el centro) | `scorecards_criterios_gate` (1201) | **820** `A` a `D` |
| **B** | `consejo_de_calidad` | `consejo_calidad`, `consejo_calidad_2` | `consejo_de_calidad_3` (2916) | **2523** y **2662** `A` a `D` |
| **B** | `cofundar_con_amigos_familia_riesgos` | `riesgo_cofundadores_relacion_previa` (el centro) | `seleccion_relaciones_cofundadores` (1058) | **498** `A` a `D` |
| **detenido** | `criterios_equity_split` | (no se ejecuta) | `teoria_equidad_split_equity` (871), **lectura HECHA** | (ninguna: el acto no se funde) |

**Guardas, por acto y en los cuatro:** miembros vivos y nomina completa, **`1B`**, cobertura
exacta de indices sin olvidos, cero repetidos literales. **`1B` pasa CON CONTENIDO en el acto del
scorecard** (su puerta `scorecards_criterios_gate` es el mixto y sobrevive) y **por vacio** en los
otros tres. **Cero auto-aristas y cero duplicadas NUEVAS** en los dos lotes, con el pasivo
historico bajando de 1.002 a 1.001 grupos porque `P.16` limpia lo que la propia sustitucion toca.
**Los cinco campos que la operacion no redacta, intactos; los siete absorbidos con su texto
INTACTO.** **Censo tras cada limpieza: CERO colisiones vigentes**
([`SALIDA_V51_CENSO_COLISIONES_TRAS_P16.txt`](SALIDA_V51_CENSO_COLISIONES_TRAS_P16.txt),
[`SALIDA_V51_CENSO_COLISIONES_TRAS_P16_B.txt`](SALIDA_V51_CENSO_COLISIONES_TRAS_P16_B.txt)).

### EL CHOQUE DE LETRA CONTRA ARITMETICA, registrado con sus puestos

**El acta 50, pregunta 3, lo adjudico: MANDA LA ARITMETICA.** En el acto del consejo hay
**CINCO**: los puestos **2631**, **2663** y **2523** cierran con *Sobrevive `consejo_calidad`*, y
los **2670** y **2662** con *Sobrevive `consejo_calidad_2`*, **y ninguno de los dos es VIABLE**,
porque su parte `A` se lleva a los cuatro miembros y no deja ningun mixto fuera. **Los dos
nombrados mueren, ninguno absorbe el racimo.** En los otros tres actos ningun veredicto `A`
escribe la formula, y se dice en vez de darlo por supuesto.

### EL ACTO DETENIDO, con el acto escrito entero

**El del reparto de equity.** El contenido elige `criterios_equity_split` por el margen mas ancho
del tramo (**ocho pasos contra cuatro, tres condiciones contra dos, 1.134 caracteres de resumen
contra 586, cableado 20 contra 4**) y con ese superviviente la fusion fabrica **TRES** colisiones
para **UNA** `CONTINUA`. **El otro viable SI calza, pero elegirlo seria dejar que la aritmetica de
las colisiones decida el superviviente, y ninguna regla escrita lo permite.** Lectura `P.12`
hecha, plan escrito, y el acto va al auditor.

---

## 4. DOS ACTOS QUE BLOQUEA LA VARA DE LAS PUERTAS, Y EL INSTRUMENTO NO LO DICE

**Medido sobre la nomina re-medida tras el lote A**
([`SALIDA_V51_PUERTAS_TRAS_LOTE_A.txt`](SALIDA_V51_PUERTAS_TRAS_LOTE_A.txt)): los actos **9** y
**17** tienen **DOS puertas dentro cada uno** (`decision_cuando_fundar` mas
`evaluacion_capacidades_fundador`; `enfoque_paso_a_paso_investigacion_mercado` mas
`evaluacion_mercados_objetivo`) **y en los dos la puerta que hace de CENTRO de la estrella tiene
que morir con cualquiera de los supervivientes viables.** La guarda `1B` los rechaza.

> **EL HALLAZGO: `vuelta48_puertas_en_el_lote.py` LOS LLAMA SALVABLES.** Su dicotomia es SALVABLE
> (una sola puerta) contra IMPOSIBLE (todos los miembros son puerta). **Falta el tercer caso: MAS
> DE UNA PUERTA, con alguna obligada a morir por la estructura del acto.** No se repara aqui, que
> seria alcance: se declara y se trae.

---

## 5. EL BARRIDO `9.10` DEL CIERRE, CORRIDO DESPUES DEL ULTIMO MOVIMIENTO

**Con las cifras viejas DE HOY** (`--viejo 571,77,8,2732 --retrato 49,522`, mas los cinco puestos
corregidos), como manda la regla del aviso
([`SALIDA_V51_BARRIDO_910_CIERRE.txt`](SALIDA_V51_BARRIDO_910_CIERRE.txt)). **NUEVE celdas
corregidas** ([`SALIDA_V51_CORRECCIONES_910.txt`](SALIDA_V51_CORRECCIONES_910.txt)):

| la celda | decia | **medido al cierre** |
|---|---:|---:|
| `RECOMPUTO_3388.md` **246**, `A` crudas | 571 | **566** |
| **247**, colapsos a auto-arista | 49 | **57** |
| **248**, pares distintos del retrato | 522 | **509** |
| **528**, el checkpoint **ii** (los dos parentesis mas su nota) | 522 igual a 522 | **509 igual a 509, sigue OK** |
| **1079**, total de `A` de la tabla por dominio | 571 (16,9 %) | **566 (16,7 %)** |
| `INTRA_DOMINIO_INFORME.md` **100.1**, fila `A` | 571 (16,9 %) | **566 (16,7 %)** |
| **100.1**, fila `D` | 2.732 (80,6 %) | **2.737 (80,8 %)** |
| **100.1**, la nota de correccion | | **segunda nota adosada, sin reescribir la de la vuelta 50** |

### DOS FAMILIAS QUE EL BARRIDO SACO Y QUE **NO TOQUE**, con su cifra medida

**No son medicion: son adjudicacion, y por eso van como pregunta.**

1. **El apendice 95.1 de `INTRA_DOMINIO_INFORME.md`, MARCADOR (corte 2.900).** Publica
   `A 571, B 89, C 7, D 2.233`. **Medido hoy con `python scripts/recomputar_marcador.py 2900`**
   ([`SALIDA_V51_MARCADOR_2900_CIERRE.txt`](SALIDA_V51_MARCADOR_2900_CIERRE.txt)):
   **`A 554, B 77, C 8, D 2.261`**. **La duda no es la cifra.** O es una FOTO FECHADA de la vuelta
   4 (y entonces la cadena de tachados que vueltas posteriores le fueron aplicando a la `A` y a la
   `D` sobraba), o es una TABLA VIGENTE al corte 2.900 (y entonces lleva tiempo derivando, porque
   **se ha mantenido restando de la cifra anterior en vez de re-midiendo**, y por eso la `B` y la
   `C` se quedaron en las de la vuelta 4).
2. **Las dos tablas *EL MARCADOR ... AL CERRAR LA VUELTA* de `RECOMPUTO_3388.md`** (lineas 1790 y
   1837), que publican `575 / 83 / 8 / 2.722` bajo un encabezado que dice ***medido hoy***. Misma
   duda y **exactamente la misma especie del rotulo que la TAREA 1.2 de esta vuelta corrigio**.

---

## 6. GATE 0 Y LAS SUITES

**Corridos tras la TAREA 1, tras cada lote y otra vez al cierre. Todos exit 0.**

| que | como salio |
|---|---|
| **Gate 0**, ciclo de **TRES** comandos | `run_phase1 --reaplico-curaduria` con **`GATE 0: OK`**; `etiquetas_de_cara --aplicar` con **71** etiquetas; `sync_assets_web` con **6** assets |
| **suite del motor** | **25 de 25** |
| **suite web** | **80** ficheros, **1.030** pasadas y **3** saltadas |
| `tsc --noEmit` | **CERO** lineas |
| duplicadas / auto-aristas **NUEVAS** | **CERO** y **CERO** en los dos lotes |
| las cuatro comprobaciones de `08_VERIFICACION` | **TODAS OK** al cierre |
| **hook guardian** | verde en todos los commits |

---

## 7. CORRECCIONES DECLARADAS SOBRE MI PROPIO TRABAJO

1. **EL INSTRUMENTO DE COLISIONES ESPERADAS MIRABA SOLO DENTRO DEL ACTO** y por eso aprobo una
   fusion que fabricaba dos colisiones que el no veia. **Reescrito para re-resolver los 3.388
   veredictos, con el motivo entero escrito en su propio docstring**, y la fusion revertida.
2. **LA CELDA QUE ESCRIBI EN LA TAREA 1.1 NACIO PARTIDA EN DIEZ LINEAS Y ROMPIA LA FILA DE LA
   TABLA MARKDOWN.** Colapsada a una sola linea, que es la forma de las celdas corregidas de
   `RECOMPUTO_3388.md`, **y el instrumento se actualizo para que su re-corrida sea idempotente**
   en vez de dejar el fichero y el instrumento diciendo cosas distintas.
3. **MI PRIMERA VERSION DEL PREDICTOR LEIA EL CAMPO `puesto` Y EL CAMPO SE LLAMA `puesto_intra`**:
   imprimia `None` en todos los puestos citados. **Las clases salian bien y los puestos no**, que
   es la clase de fallo que se publica sin darse cuenta si nadie mira la columna.
4. **Ficheros tocados que el encargo no nombraba, declarados:** `docs/COSTURAS_INTERNAS.jsonl` y
   `docs/COSTURAS_INTERNAS_RESUMEN.md` (los reescribe `scripts/costuras_internas.py` al correrse),
   `docs/plan/ARISTAS_DUPLICADAS.jsonl` (lo reescribe el instrumento de duplicadas; el commit
   traia una version anterior al volteo del 305), `dataset/metadata/*` y `web/lib/assets/manifest.json`
   (los reescribe el ciclo de Gate 0). **Mismo alcance que las vueltas 48, 49 y 50.**

---

## 8. LOS DISCUTIBLES MARCADOS, para la relectura ciega

**Marcados ANTES de saber si acierto. Son ONCE.**

| # | el discutible | por que lo marco |
|---:|---|---|
| **D1** | **Ejecute 4 de 25 lecturas `P.12` y NO abri el tramo 2.** | Es el discutible mayor y es de alcance. Lo que consumio la vuelta fue el hallazgo del instrumento, la reversion y la re-medicion de las 51 combinaciones. **Si el auditor lee que la reversion sobraba y que las tres colisiones del equity se limpiaban bajo `P.16` y se seguia, esto es una caida de reparto y la marco yo** |
| **D2** | **Reverti con `git checkout` un acto YA EJECUTADO en vez de limpiar sus colisiones.** | `P.16` dice *quien fabrica limpia*, y yo podia haber limpiado. **Elegi detener porque el encargo lo manda con esas palabras y porque las dos colisiones de fuera caian sobre pares que NO lei como parte de `P.5`.** Un lector puede decir que revertir trabajo bueno es peor que leer dos pares mas |
| **D3** | **La politica de reparto de los lotes es mia:** parametro concreto de un gesto que el superviviente ya tiene, INCISO; gesto distinto, APPEND. | **Ninguna regla escrita la dice.** La saque de la figura del INCISO y del precedente `D4` de la vuelta 50. **De ella cuelgan siete INCISOS de esta vuelta** |
| **D4** | **En la accion correctiva elegi `accion_correctiva_sistematica` con el contenido EMPATADO en pasos y condiciones y el resumen a favor del otro** (672 contra 535). | Lo decidi con el veredicto DIRECTO del par (2431, *Sobrevive `accion_correctiva_sistematica`*), que es lo que `P.12` parte 2 manda. **Pero eso deja la vara del resumen contradicha, y la vara del resumen es la que la vuelta 50 uso para desempatar** |
| **D5** | **El paso 5 de `accion_correctiva_5` viaja de APPEND aunque el 2431 lo da por CUBIERTO.** | El 2431 lo mapea al paso 3 del elegido. **No es la misma escalada: una es de AUTORIDAD y la otra de CALENDARIO**, y el 2418 llama a esa escalada *lo unico del par que impide que un problema cronico se vuelva paisaje*. **Si el auditor lee que si estaba cubierto, ese paso sobra y duplica** |
| **D6** | **La procedencia del paso 1 de `accion_correctiva_6` (*mediante auditorias de calidad*) va de PERDIDA NOMBRADA y NO de INCISO.** | **Es la unica perdida declarada del lote A junto con el *otro indicador de productividad* del scorecard.** La deje ir porque el paso resultante no se leia limpio y porque el mixto vivo `accion_correctiva_crosby` manda auditorias independientes por departamento. **Un lector puede decir que una perdida nombrada sigue siendo una perdida** |
| **D7** | **En el consejo elegi `consejo_de_calidad` con DOS de las tres varas EN CONTRA** (una condicion contra dos, resumen 362 contra 427). | Me apoye en la vara de los PASOS (seis contra cuatro) y en que el veredicto directo 2916 cuenta **tres pasos enteros propios contra dos**. **Si el auditor lee que las varas se pesan todas juntas, el superviviente era el otro y las cuatro piezas del reparto estan al reves** |
| **D8** | **Adose CUATRO incisos sobre DOS pasos del consejo** (dos al paso 1 y dos al paso 6). | Ningun precedente apila dos incisos en el mismo paso. **Los dos pasos resultantes se leen limpios y estan impresos en la salida**, pero es una forma nueva |
| **D9** | **Conte la colision POR PAR RESUELTO y no por veredicto**, y eso es lo que hace que la cuenta del encargo calce en el acto del consejo. | Contando veredictos, ese acto habria dado **dos** colisiones para una `CONTINUA` **y me habria detenido**. **La decision de que es una colision la tome yo** |
| **D10** | **No corregi el rotulo *hoy* del registro de la vuelta 49** (los declarados 29, 32 y 36), aunque es la especie exacta que la TAREA 1.2 vino a corregir y la medi. | Lo deje por scope: el encargo y el acta scopearon la 1.2 al registro de la vuelta 50. **Si el auditor lee que la vara adjudicada es general, dejarlo vivo es la misma caida que corregi tres parrafos mas arriba** |
| **D11** | **No corregi el apendice 95.1 ni las dos tablas de `RECOMPUTO_3388.md`** que el barrido saco, y las traigo como pregunta con su cifra medida. | Es la decision mas comoda de las once y lo digo asi. **La alternativa era elegir yo si son fotos fechadas o tablas vigentes, y esa eleccion cambia si sus cifras se reescriben o se restauran** |

---

## 9. PENDIENTES DE DOCTRINA

1. **LA CUENTA DE COLISIONES DEL ENCARGO NO CUBRE LAS QUE CAEN FUERA DEL ACTO.** Medido: **cinco
   combinaciones de las 51** las fabrican. **La formula *una por `CONTINUA`* es exacta para la
   forma de la estrella con centro absorbido y no en general**, y hoy no hay regla que diga que
   hacer cuando el exceso aparece.
2. **LA VARA DE LAS PUERTAS TIENE DOS CATEGORIAS Y HACEN FALTA TRES.** SALVABLE, IMPOSIBLE, **y el
   caso de MAS DE UNA PUERTA con alguna obligada a morir**, que hoy se cuenta como SALVABLE y no
   lo es. **Afecta a dos actos del tramo 1.**
3. **LA CLASE `B` COMO PAR CONGELADO PARA LA MESA.** Cuatro de los 21 mixtos que quedan tienen su
   par mixto en `B`, y al menos uno (el **703**, el del S&OP) congela **una pregunta de politica**
   (*si el catalogo quiere un procedimiento con dos contextos o dos nodos*), no una condicion de
   texto. **`08_VERIFICACION` manda releer la `B` cuando el nodo cambia de texto, y `P.12` manda
   que la lectura decida; ninguna de las dos dice quien contesta una pregunta de politica.**
4. **HEREDADOS Y SIN CAMBIO HOY**: el INCISO para condiciones **sigue sin existir** en el
   instrumento; el esquema de `OPERACIONES.jsonl` **sigue sin distinguir ejecutada de pendiente**
   (71 en `LISTA`, medido hoy); y el campo `orden` de la fase 03 **sigue sin ser su criterio de
   orden**.

---

## 10. LO QUE ESTA VUELTA NO HIZO, DICHO EN VEZ DE CALLADO

1. **NO hizo 21 de las 25 lecturas `P.12` pendientes.** Cinco hechas, cuatro ejecutadas. **Es el
   incumplimiento mayor de la vuelta.**
2. **NO abrio el tramo 2** de 50 actos.
3. **NO toco los cinco declarados**, identificados por sus miembros. Al cerrar son los actos 4,
   21, 23, 27 y 28.
4. **NO ejecuto las cuatro aristas** de los `CONTINUA` ni la poda de sus solapes: son de la fase
   04 y quedan **declaradas** con id resuelto (`P.9`). **En el acto del equity la arista ya existia
   en los dos sentidos**, y por eso alli no habria arista que declarar sino solo poda.
5. **NO resolvio las 1.001 duplicadas** ni el alias durmiente `modelo_spin_2`: son de `OP-S-12`.
6. **NO corrigio** el apendice 95.1, ni las dos tablas *al cerrar la vuelta* de
   `RECOMPUTO_3388.md`, ni el rotulo del registro de la vuelta 49. **Las tres estan medidas y
   traidas.**
7. **NO reparo el instrumento de las puertas** para que reconozca el tercer caso.

---

## 11. LAS PREGUNTAS PARA EL AUDITOR

1. **La colision: se cuenta por PAR RESUELTO o por VEREDICTO?** (**D9**.) De la respuesta depende
   si el acto del consejo se podia fundir o me tenia que haber detenido.
2. **El acto detenido: detener era lo correcto, o `P.16` obligaba a limpiar las dos colisiones de
   fuera y seguir?** (**D1**, **D2**.) **Si la respuesta es limpiar, el acto esta escrito entero y
   sale en una corrida.**
3. **Los actos con DOS puertas: son IMPOSIBLES?** (Pendiente 2.) Y si lo son, **se repara el
   instrumento que hoy los llama SALVABLES?**
4. **El apendice 95.1 al corte 2.900: foto fechada o tabla vigente?** (**D11**.) Si es foto, hay
   una cadena de tachados que sobra; si es vigente, lleva tiempo derivando por mantenerse restando
   en vez de re-midiendo.
5. **Un par `B` que congela una pregunta de POLITICA: la contesta `P.12` o va a la mesa?**
   (Pendiente 3.) Afecta a cuatro de los 21 mixtos que quedan.
6. **A contenido empatado en las tres varas, desempata el resumen por cinco caracteres, o el
   empate va al auditor por `P.8` fila tres?** El acto de los regalos estrategicos queda en
   **433 contra 428** de resumen, con pasos, condiciones y cableado empatados. **No lo funde esta
   vuelta y por eso no es discutible sino pregunta.**
