# ACTA DEL AUDITOR DEL BUCLE (se apende por vuelta; nada se borra)

## VUELTA 1, 12 ago 2026. Auditor: Fable 5. Reporte auditado: checkpoint 2.600 (ejecutor Opus 4.8)

### 1. VERIFICACION, todo con comando propio

- **Hashes**: `f3c3750c` contiene el archivo en 2.600 lineas exactas
  (`git show f3c3750c:docs/INTRA_DOMINIO_VEREDICTOS.jsonl | wc -l` da 2600). El commit
  posterior `5834d869` toca exactamente las rutas declaradas: BANCO_DE_TEXTOS.md,
  REPORTE.md y .gitignore; docs/plan/ intacto, como manda el encargo. Arbol limpio en `bucle`.
- **Marcador recomputado** (python sobre el jsonl, conteo por clase): **A 522, B 89, C 7,
  D 1.982; n 2.600; cero huecos (set 1..2600 completo) y cero duplicados.** Coincide cifra
  a cifra con el reporte, incluido el tramo nuevo: 46 pares, 14 A y 32 D.
- **Tasa por dominio**: recomputada entera; las ocho filas coinciden con la tabla del
  reporte (quality 189 pares, 68 A, 36,0).
- **Vara por tramo de 25 en quality**: recomputada del archivo; los ocho tramos coinciden,
  incluido el 2.576-2.600 en 28,0 (7 de 25).
- **Correccion declarada de TAREA 1, verificada contra el archivo y el grafo**: el 2.453 es
  A con `sistema_estable_causas_comunes` ganando a `sistema_estable_responsabilidad_gerencial`;
  el 2.537 y el 2.572 son A de `mejora_del_sistema_responsabilidad_gerencial`. La firma de
  POR ELEGIR (gano una, perdio otra) es real. El cumulo por raiz medido en el grafo
  (patron causas_comunes / causas_especiales / sistema_estable / responsabilidad_gerencial /
  distincion_causas en quality) da **17 nodos**: "pasa de quince, no de cinco" verifica.
- **Familias citadas, verificadas**: auditoria de producto 3 de 3 todas D (2.433, 2.478,
  2.594); histograma 2.517 A; causas comunes gana 2.497, 2.501 y 2.577; fusiones mutuas
  12.a 2.552, 13.a 2.575, 14.a 2.597, todas A en el archivo.
- **Perdidas de nombre, re-verificadas contra el grafo** (manda la seccion 1 del protocolo):
  COC vive en el titulo de `plan_de_gestion_de_riesgos` (que muere en el 2.593) y no en el
  superviviente; el Teorema de Nelson vive en el titulo de
  `distincion_causas_especiales_comunes` (muere en el 2.577) y no en el superviviente; el
  diagrama causa-efecto vive en los pasos de `analisis_diagnostico_causa` (muere en el
  2.600) y no en el superviviente. Las tres perdidas declaradas son reales.

### 2. RELECTURA CIEGA de los once discutibles marcados

Metodo: imprimi PRIMERO titulo, resumen y pasos de los dos nodos de cada par desde
`master_graph.json`, adjudique mi clase, y SOLO DESPUES destape las razones escritas.
**Limite declarado del ciego**: la tabla de discutibles del reporte trae la clase del
ejecutor, asi que el ciego pleno es sobre la RAZON, no sobre la clase; adjudique desde el
texto de los nodos antes de leer razon alguna.

| puesto | mi clase ciega | ejecutor | ¿coincide? |
|---:|---|---|---|
| 2.558 | D (dos lecturas del instrumento, procedimientos propios en ambos) | D | si |
| 2.571 | A por contencion (manual y costos de mala calidad son detalle de paso compartido, no paso propio) | A | si |
| 2.575 | A por fusion mutua (incendios contra delegacion departamental, linea en los dos sentidos) | A fusion mutua | si |
| 2.579 | A (la replicacion de Shewhart es paso propio; el Act del otro cabe dentro) | A | si |
| 2.583 | D (el envoltorio de politica declara que haya programa; el otro ES el programa) | D | si |
| 2.590 | A por contencion (los cinco pasos de Deming caben en los diez de Juran) | A | si |
| 2.596 | D (el lazo diagnostico-remedio-medicion contra la caja de siete tecnicas; ninguno cabe en el otro) | D | si |
| 2.597 | A por fusion mutua (auditoria e indicadores contra contabilidad creativa y banca) | A fusion mutua | si |
| 2.598 | A por contencion (los cuatro de Juran caben en los cinco de Deming, que ademas trae reglas de patron y compuerta) | A | si |
| 2.599 | D (la frontera regulatoria contra el taller del estandar; el solape de comites no funde los actos) | D | si |
| 2.600 | A (el causa-efecto es herramienta del paso de teorizar, no acto aparte) | A | si |

**Resultado: 11 de 11 coinciden, cero discrepancias, y ninguna discrepancia fuera del
marcado. El credito de la tanda queda INTACTO.** Las razones escritas, destapadas despues,
citan pasos que existen en los nodos: ninguna razon inventa contenido.

En el filo comun (A por contencion o fusion mutua contra D en instrumentos del mismo
libro) el criterio que sostiene la tanda y que hago explicito: **linea propia es un paso
entero que el otro no tiene; un detalle dentro de un paso compartido no vuelve mutua la
fusion, se registra como perdida nombrada.** Es la lectura que ya practican 2.571 (perdidas
nombradas, no mutua) contra 2.575 y 2.597 (pasos enteros propios, mutua). Consistente con
la vara 9.6.1: pesar contenido, no contar lineas.

### 3. METRICA DE CREDITO acumulada

Saliente: 15 relecturas, 35 puestos, 4 caidas, todas dentro del marcado.
Esta vuelta: +1 relectura, +11 puestos, 0 caidas, todo dentro del marcado.
**Acumulado: 16 relecturas, 46 puestos, 4 caidas, TODAS dentro del marcado.**

### 4. ADJUDICACIONES

1. **PREGUNTA 1, la fecha (adjudicada, no pide doctrina nueva).** La regla escrita del
   11 ago ("toda glosa en prosa lleva el corte") ya da la llave: **EL ORDEN CANONICO DEL
   BANCO ES EL CORTE, NO LA FECHA DE CALENDARIO.** Por extension: (a) lo que se transcribe
   de un adjudicador anterior conserva la fecha con que ese adjudicador lo firmo (los
   vistos del saliente quedan "18 ago" y NO se retocan); (b) todo texto NUEVO se firma con
   el reloj real del sistema MAS su corte, como hizo el ejecutor con su correccion ("12 ago
   2026, corte 2.600"); (c) la aparente inversion (un 12 ago despues de un 18 ago) es
   inofensiva porque el corte ordena. Nada de lo ya escrito se corrige; el ejecutor
   registra la precision donde vive la regla del corte.
2. **PREGUNTA 2, la tasa de la quinta cara: es medicion, no adjudicacion.** Se encarga con
   universo definido (TAREA 1 del encargo). La cifra de cinco apariciones queda como cota,
   igual que el precedente adjudicado del 18 ago ("esa cifra es una cota inferior, no un
   censo").
3. **DISCUTIBLE DE INFRA, el .gitignore: BIEN, por extension del precedente escrito.**
   `scripts/rumbos/_ultima_corrida.json` ya estaba ignorado con la misma razon (runtime que
   cambia por corrida; la vara committeada es otra). `loop.log`, `ultimo_ejecutor.json` y
   `ultimo_auditor.json` son la misma especie. Reversible si el fundador quiere versionar
   el log; queda anotado aqui para su vista.
4. **CONTINUIDAD DE LA FUENTE DE CHECKPOINTS.** El protocolo del auditor nombra las
   ultimas secciones del INTRA_DOMINIO_INFORME.md como fuente de verdad de checkpoints, y
   el informe se quedo en el 2.500 (seccion 91) porque el encargo del saliente movio el
   reporte a docs/loop/REPORTE.md, que se reescribe por vuelta. Adjudico: **el checkpoint
   se apende TAMBIEN al informe como seccion compacta** (cifras y commit, sin repetir la
   prosa del reporte), para que la fuente no quede trunca. Va al encargo.

### 5. ERRORES PROPIOS DE ESTA VUELTA, declarados

- Al cruzar la figura COC lei primero el reporte y por un momento trate el 2.593 como
  posible discrepancia porque los ids (`evaluacion_gestion_riesgos` contra
  `plan_de_gestion_de_riesgos`) no suenan a COC; el titulo del nodo que muere si lo trae.
  Verifique antes de afirmar y no quedo afirmacion falsa, pero el reflejo de dudar del id
  sin abrir el nodo queda anotado como aviso a mi mismo.
- El ciego parcial sobre la clase (punto 2) se declara como limite del metodo, no se
  esconde.

### 6. VEREDICTO DE LA VUELTA

Reporte VERIFICADO en todas sus cifras; relectura ciega 11 de 11; correccion declarada
bien hecha y bien registrada (tachado sin borrar, leccion contada); cero pendientes de
doctrina nueva; ninguna condicion de parada. La fase I continua: encargo el cribado
2.601 a 2.700. Faltan 788 pares (quality 655, risk_management 106, seguridad_digital 27).

## VUELTA 2, 12 ago 2026. Auditor: Fable 5. Reporte auditado: checkpoint 2.700 (ejecutor Opus 4.8)

### 1. VERIFICACION, todo con comando propio

- **Hashes**: `a5d16eee` contiene el archivo en 2.700 lineas exactas
  (`git show a5d16eee:docs/INTRA_DOMINIO_VEREDICTOS.jsonl | wc -l` da 2700). El commit
  posterior `4353cbe2` toca exactamente informe y reporte. El diff completo de la vuelta
  (`git diff --stat a0db3a76..HEAD`) toca solo las seis rutas declaradas; **docs/plan/
  intacto** (diff vacio). Arbol limpio en `bucle`.
- **Marcador recomputado** (python sobre el jsonl): **A 544, B 89, C 7, D 2.060; n 2.700;
  cero huecos (set 1..2700 completo) y cero duplicados.** Coincide cifra a cifra. Tramo
  2.601-2.700: 22 A y 78 D; **la lista de las 22 A del reporte coincide puesto a puesto**
  con la recomputada del archivo.
- **Tasa por dominio**: recomputada entera; las ocho filas coinciden (quality 289 pares,
  90 A, 31,1).
- **Vara por tramo de 25 en quality (2.601-2.700)**: 24,0 / 28,0 / 28,0 / 8,0; los cuatro
  tramos coinciden, incluido el 8,0 del ultimo cuarto.
- **Discutibles inline**: 68 pares del tramo llevan DISCUTIBLE MARCADO en el jsonl, la
  cifra que el reporte declara como conjunto completo del marcado.
- **TAREA 1 verificada**: secciones 92 y 93 del informe existen y sus cifras calzan con lo
  ya verificado (vuelta 1) y con mi recomputo (corte 2.700); la precision del 9.21 es fiel
  al acta vuelta 1, con los puntos a, b y c y sin retocar lo escrito; la medicion del
  9.28.1 la re-corri con el comando declarado (`python scripts/barrido_quinta_cara.py
  2600`): **863 de 2.600 pares con candidato, core 623, quality 86 crudos**, reproducido.
  Los hechos falsables de la medicion verifican los tres: las cuatro apariciones dentro de
  la superficie (2.464, 2.477, 2.488, 2.548) aparecen en el barrido; el box plot del 2.517
  vive en el CUERPO de `histogramas_distribucion_frecuencias` (no en titulo ni id); el COC
  del 2.593 esta DELETREADO en el titulo de `plan_de_gestion_de_riesgos` (Concerns,
  Options, Consequences, sin sigla), invisible al regex. **Limite declarado**: el 56 de
  189 es curacion a mano que no reproduje entera; verifique el marco crudo (86 candidatos
  en quality, y 56 cabe en 86) y que el BANCO la firma como cota con su metodo, no como
  censo. Consistente con 9.28.
- **Señal del idioma sin aparicion nueva, verificada**: ninguna razon del tramo 2.601-2.700
  menciona denominacion perdida ni el 9.28; la cifra queda en cinco al corte 2.700.
- **Precision de la capacidad, verificada y afinada con el grafo**: contada por raiz la
  familia lleva **8 pares, los 8 D** (el 2.423, establecer contra establecimiento, tambien
  junta dos nodos de la raiz); el "7 de 7" del reporte cuenta la cobertura completa del
  nucleo de cuatro nodos (6 pares, C(4,2)) mas el 2.697. **SIN ACTO se sostiene sobre los
  8**; nada sustantivo cambia. La precision que el ejecutor declaro era exacta y esta linea
  la completa. Va al encargo como una linea del checkpoint 2.800.
- **Citas cruzadas de familia** que sostienen las transitividades del tramo, verificadas
  clase a clase contra el archivo: 2.425 D, 2.513 D, 2.469 A, 2.444 D, 2.455 D, 2.495 D,
  2.668 D, 2.602 D, 2.498 A, 2.502 D, 2.539 D, 2.422 D, 2.443 D, 2.508 D, 2.556 D,
  2.335 A. Las seis correcciones del barrido de familia (2.605, 2.609, 2.610, 2.614,
  2.652, 2.653 en D; 2.620 en A) estan en el archivo como el reporte las cuenta.

### 2. RELECTURA CIEGA de los quince discutibles fuertes

Metodo: imprimi PRIMERO titulo, resumen y pasos de los dos nodos de cada par desde
`master_graph.json`, adjudique mi clase, y SOLO DESPUES destape las razones escritas.
**Limite declarado del ciego**, el mismo de la vuelta 1: la tabla del reporte trae la
clase del ejecutor, asi que el ciego pleno es sobre la RAZON; adjudique desde el texto de
los nodos antes de leer razon alguna. Los quince estan dentro de los 68 marcados inline.

| puesto | mi clase ciega | ejecutor | ¿coincide? |
|---:|---|---|---|
| 2.686 | A (mismos cinco pasos, mismo eje: prueba, criterio, regla de decision, validacion con las partes) | A | si |
| 2.691 | D (crear el liderazgo estadistico central con su salvaguarda contra seleccionar roles y repartir el reporte; ninguno contiene al otro limpio) | D | si |
| 2.677 | D (el diagnostico sobre el proceso contra la postura gerencial: lemas, compromiso escrito, comunicar al trabajador) | D | si |
| 2.618 | A (los cinco pasos del breakthrough SON el DMAIC; contencion) | A | si |
| 2.641 | A (los accidentes calzan paso a paso como caso del general; el caso no es la casa) | A | si |
| 2.620 | A (los pasos del caso de la arruga calzan uno a uno con el general; repite y sobrevive el general) | A | si |
| 2.663 | A (el consejo que elige proyectos, da recursos y reconoce cabe entero en el ejecutivo; politicas y niveles son pasos extra del superviviente) | A | si |
| 2.670 | A (mismo consejo; carta constitutiva contra capacitacion y Pareto, en el peor caso mutua, la clase no cambia) | A | si |
| 2.673 | A (mismo segundo paso del diseño: identificar el elenco; clasificar contra listar tipos son manos, no actos) | A | si |
| 2.645 | A (el reporte cabe en analisis mas reporte; el formato de entrega es detalle, no paso propio) | A | si |
| 2.700 | D (el lazo probar-cambiar-verificar sobre proceso controlado contra el mapa del sistema y la postura de no culpar) | D | si |
| 2.678 | D (ficha de Expand y Sustain contra el mapa de cinco fases) | D | si |
| 2.693 | D (la hoja de necesidades es un paso del paraguas QFD; ficha contra mapa, como el 2.653) | D | si |
| 2.695 | D (el diseño de metodos es el paso 7 y 8 del plan de 16; paso contra proceso) | D | si |
| 2.679 | D (enrutar la accion al mecanismo correcto contra proteger al trabajador de la culpa del sistema) | D | si |

**Resultado: 15 de 15 coinciden, cero discrepancias, y ninguna discrepancia fuera del
marcado. El credito de la tanda queda INTACTO.** Las razones destapadas citan pasos que
existen en los nodos: ninguna razon inventa contenido, y sus citas de familia estan
verificadas en la seccion 1.

El filo dominante del tramo, hecho explicito y consistente con el criterio de la vuelta 1:
**en los cumulos del mismo autor, la contencion funde solo cuando el acto entero de uno
cabe en el otro (2.618, 2.645, 2.663); la ficha que despliega un paso del mapa NO se
subsume, es cara distinta (2.678, 2.693, 2.695); y el caso cuyos pasos calzan uno a uno
con el general repite (2.620, 2.641), pero el que trae un paso de creacion propio no
(2.691).** Es la vara 9.6.1 pesando contenido, con la figura 78.2 en las dos direcciones.

### 3. METRICA DE CREDITO acumulada

Saliente tras vuelta 1: 16 relecturas, 46 puestos, 4 caidas, todas dentro del marcado.
Esta vuelta: +1 relectura, +15 puestos, 0 caidas, todo dentro del marcado.
**Acumulado: 17 relecturas, 61 puestos, 4 caidas, TODAS dentro del marcado.**

### 4. ADJUDICACIONES

1. **PREGUNTA 1, el universo limpio de la quinta cara: adjudicada, procede como MEDICION
   por extension del 9.28, no pide doctrina nueva.** El 9.28 ya establece que el barrido
   es buscador de candidatos y que la denominacion vive tambien fuera de title+id; el box
   plot del 2.517 lo documenta en su propia carne. Por extension citable: el barrido del
   CUERPO (resumen y pasos), restringido a los dominios de nombre largo en castellano
   (fuera `core`, ingles por diseño), es la medicion limpia que la figura pide. Se encarga
   con universo definido, revision a mano y publicacion como cota con corte y comando,
   igual que el precedente de la vuelta 1 ("es medicion, no adjudicacion").
2. **PREGUNTA 2, el hub del Consejo de Calidad: no pide adjudicacion.** La cola trae los
   pares que faltan; la especie queda POR ELEGIR provisional hasta cerrar la cobertura del
   cumulo, como el propio reporte la deja ("anotado, no dictado"). Bien traido y bien
   dejado; el encargo prohibe adelantar pares.
3. **La precision de la capacidad: registrada.** La declaracion del ejecutor ("cerrada era
   sobre los seis pares que la cola habia traido") era exacta; mi conteo por raiz la
   completa (8 de 8, todas D, con el 2.423). Una linea al checkpoint 2.800; nada ya
   escrito se retoca.

### 5. ERRORES PROPIOS DE ESTA VUELTA, declarados

- Mi primer barrido de la familia de la capacidad uso un grep por raiz demasiado ancho y
  trajo nodos de otros dominios (capacidades del fundador, capacidades de mercado); lo
  corregi en el acto restringiendo al patron de la capacidad de proceso de quality antes
  de afirmar nada. El instrumento ancho queda anotado como aviso a mi mismo.
- Mi primer volcado de nodos para la ciega uso llaves equivocadas (`resumen`/`pasos` en
  vez de `resumen_teorico`/`pasos_accionables`) y salio vacio; lo corregi antes de
  adjudicar. Ningun veredicto se emitio con el instrumento roto.

### 6. VEREDICTO DE LA VUELTA

Reporte VERIFICADO en todas sus cifras, incluidas las citas cruzadas de familia y los
hechos falsables de la medicion de la quinta cara; relectura ciega 15 de 15; cero
pendientes de doctrina nueva; ninguna condicion de parada. La fase I continua: encargo la
medicion del universo limpio (adjudicada), la linea de precision de la capacidad y el
cribado 2.701 a 2.800. Faltan 688 pares (quality 555, risk_management 106,
seguridad_digital 27).

## VUELTA 3, 12 ago 2026. Auditor: Fable 5. Reporte auditado: checkpoint 2.800 (ejecutor Opus 4.8)

### 1. VERIFICACION, todo con comando propio

- **Hashes**: `0f4e7c42` contiene el archivo en 2.800 lineas exactas
  (`git show 0f4e7c42:docs/INTRA_DOMINIO_VEREDICTOS.jsonl` medido con Measure-Object da
  2800). El diff completo de la vuelta (`git diff --stat 4ceca13f..0f4e7c42`) toca solo
  las cinco rutas declaradas; **docs/plan/ intacto**. Arbol limpio en `bucle`.
- **Marcador recomputado** (python sobre el jsonl): **A 563, B 89, C 7, D 2.141; n 2.800;
  cero huecos (set 1..2800 completo) y cero duplicados.** Coincide cifra a cifra. Tramo
  2.701-2.800: 19 A y 81 D; **la lista de las 19 A del reporte coincide puesto a puesto**
  con la recomputada del archivo.
- **Tasa por dominio**: recomputada entera; las ocho filas coinciden (quality 389 pares,
  109 A, 28,0).
- **Vara por tramo de 25 en quality (2.701-2.800)**: 12,0 / 24,0 / 24,0 / 16,0; los
  cuatro tramos coinciden.
- **Discutibles inline**: los 100 pares del tramo llevan DISCUTIBLE MARCADO en el jsonl y
  22 llevan la marca "fuerte", como el reporte declara.
- **TAREA 1, el barrido del cuerpo, re-corrido con el comando declarado**
  (`python scripts/barrido_quinta_cara_cuerpo.py 2800 --dominio quality`) **y recomputado
  ademas con instrumento propio desde el grafo** (replique la logica del script en python
  directo, sin pasar por su salida impresa): **universo fuerte 234 de 389, reproducido
  por las dos vias.** Las seis parejas de aparicion (2.464, 2.477, 2.488, 2.517, 2.548,
  2.593) caen DENTRO del universo, verificado par a par con sus tokens (ZD, MBO, box
  plot, VOC deletreado en el 2.548, COC deletreado en el 2.593). **La cota titular 6 de
  234 = 2,6 por ciento VERIFICA, y la leccion (dos cotas acotan, no hay tasa unica
  limpia) queda en pie.**
- **DOS CIFRAS SECUNDARIAS DEL 9.28.1 NO REPRODUCEN, y van a correccion declarada:**
  1. **El 204** ("sin los fragmentos total, of, value"): con exactamente esos tres
     fragmentos mi recomputo da **209** (pares del universo cuya senal no se reduce a
     esos tokens). Barri sistematicamente conjuntos alternativos de fragmentos: ninguno
     natural da 204 (el unico que lo da exige excluir la sigla ZD, que es una de las
     cinco denominaciones y no puede excluirse). La tasa secundaria NO cambia: 6 de 209
     = 2,9 por ciento, la misma que el reporte publico con 204.
  2. **El "benchmarking en 59 pares fuertes"**: mi recomputo da **20 pares fuertes** con
     el token benchmarking (y por raiz benchmark* son 25 pares, 24 nodos, 89 menciones;
     ni sumando dominios no core sale 59, da 34). El ranking cualitativo (benchmarking
     al frente, luego sigma, pareto, lean) SI se sostiene; la cifra no.
  Ninguna de las dos toca la cota titular ni el marcador; la correccion procede con las
  reglas existentes (correccion declarada con su comando y recomputo, precedente de la
  vuelta 1 del ejecutor). Va al encargo como TAREA 1.
- **La capacidad en 10 de 10, verificada por raiz contra el archivo**: los diez pares de
  la raiz (2.412, 2.423, 2.454, 2.535, 2.569, 2.591, 2.636, 2.697, 2.751, 2.779) estan
  en el archivo, todos D; los dos nuevos entran via `capacidad_de_proceso_2`. SIN ACTO se
  sostiene; extiende sin reabrir, como declara el reporte.
- **Senal del idioma sin aparicion nueva, verificada**: las unicas razones del tramo que
  tocan denominaciones (2.740 Nelson, 2.776 COC) las tratan como YA declaradas (2.577 y
  2.593), con la reposicion encargada donde corresponde. Cinco denominaciones al corte
  2.800 verifica.
- **Contador de fusiones mutuas en diecisiete, consistente**: la 17.a fue el 2.666
  (reporte vuelta 2, verificado en git); ninguna razon del tramo declara mutua numerada
  nueva; las A del tramo con mutua en la razon son de gemelos ya en cumulo, que por la
  convencion de la vuelta 2 (solo los casos nuevos abren numero) no mueven el contador.
- **Citas de transitividad del reporte, verificadas clase a clase**: 2.590 A, 2.413 D
  (sostienen el 2.706); 2.618 A, 2.548 A (sostienen el 2.759); 2.630 A, 2.648 D
  (sostienen el 2.789); 2.562 A, 2.639 A (sostienen el discutible del 2.799); 2.652 D,
  2.653 D y 2.666 A tal como el reporte los cita.

### 2. RELECTURA CIEGA de treinta discutibles (los 22 fuertes inline mas los fuertes de la tabla del reporte)

Metodo: imprimi PRIMERO titulo, resumen y pasos de los dos nodos de cada par desde
`master_graph.json` (volcador propio que nunca imprime la razon), adjudique mi clase, y
SOLO DESPUES destape las razones escritas. **Limites declarados**: (a) como en las
vueltas 1 y 2, el ciego pleno es sobre la RAZON, no sobre la clase; (b) **el 2.727 quedo
CONTAMINADO**: lei su razon entera durante la verificacion de la senal del idioma, antes
de la ciega. Se adjudico igual, declarado como NO ciego, y coincide (A por contencion:
los pasos de errores_de_medicion caben todos en el MSA, que ademas trae Gauge R&R y la
comparacion 5,15 sigma). No cuenta en el resultado ciego.

| puesto | mi clase ciega | ejecutor | ¿coincide? |
|---:|---|---|---|
| 2.702 | D (mecanica del muestreo contra diseno economico del plan; curva OC y balance de costos son pasos propios) | D | si |
| 2.723 | D (patron general de adaptaciones sectoriales contra ficha de una norma; ficha contra mapa) | D | si |
| 2.724 | D (procedimiento de la carta sobre el sistema estable contra el alcance del sistema: seleccion, entrenamiento, simplificar) | D | si |
| 2.730 | D (evolucionar el control de aceptacion con ciclo de vida contra abandonarlo; posturas distintas pese a la tesis compartida) | D | si |
| 2.733 | D (declarar la politica medible contra el ciclo de RH que la refuerza) | D | si |
| 2.735 | D (el VA/NVA es la ficha del paso de clasificar del VSM; ficha contra mapa) | D | si |
| 2.736 | A (mismo acto: limites para distinguir comun de especial sobre personas y responder sin culpar; calza paso a paso) | A | si |
| 2.737 | A (los mismos cinco principios de Nakajo y Kume; el servicio es el caso del general y el general sobrevive) | A | si |
| 2.739 | D (diseno y medicion del programa contra entrega y monitoreo con la guia; facetas del Make Certain, la leccion del 2.652) | D | si |
| 2.741 | D (postura gerencial con lemas y compromiso escrito contra procedimiento del sistema estable) | D | si |
| 2.742 | A (el Select ES el proceso de nominacion y seleccion: nominar, criterios, priorizar, encargar; charter y secretaria son manos) | A | si |
| 2.747 | **A (mi ciega: contencion en el _5)** | **D** | **NO, dentro del marcado** |
| 2.756 | **A (mi ciega: mismo eje criterio mas validacion entre inspectores, como el 2.686)** | **D** | **NO, dentro del marcado** |
| 2.760 | A (gemelos del gobierno familiar: junta asesora primero, consejo familiar, master plan con consultor, independientes) | A | si |
| 2.761 | D (la ficha SMART despliega el paso de metas del establecer proyecto; ficha contra mapa) | D | si |
| 2.765 | D (definicion del aseguramiento contra la distincion vigilar/asegurar; actos distintos) | D | si |
| 2.766 | A (rastrear el origen con registros y responder al problema sin culpar; mismo acto que la politica) | A | si |
| 2.767 | D (abolir la inspeccion masiva al 100 por ciento contra abolir el muestreo de aceptacion por lotes; blancos distintos con tesis comun) | D | si |
| 2.768 | D (ejecucion con checklist, severidades y plazos contra revision independiente con visitas y metas numericas; dos facetas) | D | si |
| 2.773 | A (juicios independientes comparados graficamente para consistencia; el esquema del item 20 y el sin jerarquia son manos del mismo acto) | A | si |
| 2.780 | A (revision periodica formal del progreso de proyectos; el formato con ahorro neto es detalle, no acto propio) | A | si |
| 2.784 | D (argumento y filosofia del Quality is Free contra el instrumento COPQ con taxonomia y benchmarks) | D | si |
| 2.787 | A (separar lo tactico de lo estrategico en la funcion calidad y subirla a la planificacion; calza paso a paso) | A | si |
| 2.790 | D (el goal statement es la ficha del paso de metas; ficha contra mapa, hermano del 2.761) | D | si |
| 2.795 | D (advertencia contractual del AQL contra la taxonomia de indices para disenar planes) | D | si |
| 2.797 | D (auditar el sistema contra construir el manual; cada uno lleva al otro solo como paso menor) | D | si |
| 2.798 | D (Expand y Sustain contra Prepare; fase contra fase del mismo roadmap) | D | si |
| 2.799 | D (transferir e implementar los controles contra disenar el plan de control; actos distintos del cierre) | D | si |
| 2.800 | A (rastreo estadistico del problema sin culpar; mismo acto que la politica, via el cumulo de la distincion) | A | si |

**Resultado: 27 de 29 ciegos coinciden; DOS discrepancias mias (2.747 y 2.756), AMBAS
DENTRO del marcado (las dos llevan la marca fuerte inline). El credito de la tanda queda
INTACTO por la regla del marcado.** Al destapar las razones, las dos discrepancias se
resolvieron SIN correccion, a favor del ejecutor y por el criterio ya escrito en la
vuelta 1 (**linea propia es un paso entero que el otro no tiene; el paso entero propio
rompe la contencion**): en el 2.747, montar el foro de reuniones es paso entero de _4 y
el chart de accion con causa raiz es paso entero de _5, asi que ninguno cabe limpio en el
otro; en el 2.756, el metodo de prueba de la definicion general es paso entero de _2 y la
recategorizacion por tipo de defecto (abolir mayor/menor con supervisores) es paso entero
de _defectos. Mi lectura A pesaba el nucleo compartido (la trampa contra la que avisa el
2.652); la vara escrita pesa el paso entero. Cero caidas de clase; las razones destapadas
de los treinta citan pasos que existen en los nodos.

### 3. METRICA DE CREDITO acumulada

Saliente tras vuelta 2: 17 relecturas, 61 puestos, 4 caidas, todas dentro del marcado.
Esta vuelta: +1 relectura, +30 puestos (29 ciegos y el 2.727 declarado no ciego),
0 caidas, y las dos discrepancias del auditor DENTRO del marcado.
**Acumulado: 18 relecturas, 91 puestos, 4 caidas, TODAS dentro del marcado.**

### 4. ADJUDICACIONES

1. **Las dos cifras secundarias del 9.28.1 (204 y 59): correccion con regla existente,
   no doctrina nueva.** Son mediciones, y las mediciones se firman con su comando (regla
   del corte y el comando, 9.28.1; precedente "es medicion, no adjudicacion" de las
   vueltas 1 y 2). El texto publicado no trae el comando que las produjo y mi instrumento
   no las reproduce. Procede: el ejecutor re-corre con instrumento declarado y o bien
   publica el comando exacto que da 204 y 59, o bien corrige con tachado (sin borrar) a
   las cifras reproducibles, **209** y **20**, dejando el comando al lado. La cota
   titular (6 de 234 = 2,6 por ciento), la tasa secundaria (2,9 por ciento, que
   sobrevive identica con 209) y la leccion de las dos cotas NO se tocan.
2. **Los discutibles 2.747 y 2.756: adjudicados D, sin correccion**, por el criterio de
   la vuelta 1 citado arriba. Mi caso A queda registrado en la tabla como discrepancia
   ciega que no prospero.
3. **Preguntas 1 y 2 del reporte (cobertura del Consejo de Calidad, sub-cumulo de la
   responsabilidad gerencial): siguen abiertas y no piden adjudicacion.** La cola trae
   los pares; POR ELEGIR provisional en ambas, como el reporte las deja. Bien traido y
   bien dejado.
4. **La convencion del contador de mutuas, hecha explicita**: solo los CASOS NUEVOS de
   fusion mutua (superviviente POR ELEGIR fuera de cumulo ya contado) abren numero; las
   mutuas de gemelos que ya viven en un cumulo contado no mueven el contador. Es la
   practica de las vueltas 2 y 3, ahora escrita.

### 5. ERRORES PROPIOS DE ESTA VUELTA, declarados

- **Contamine la ciega del 2.727**: mi grep de la senal del idioma imprimio razones
  enteras y lei la del 2.727 antes de la relectura. Lo declare, lo adjudique como NO
  ciego (coincide con el ejecutor) y lo saque del resultado ciego. Aviso a mi mismo: en
  la fase de verificacion, volcar solo puesto y clase, nunca el campo razon, hasta
  terminar la ciega.
- **Mi primer conteo del universo del cuerpo dio 212 en vez de 234** porque parsee la
  salida impresa del script en lugar de recomputar desde el grafo; el instrumento
  textual perdia bloques. Lo descarte y recompute con la logica replicada sobre el grafo
  antes de afirmar nada: 234 reproducido. El instrumento roto queda anotado, ningun
  numero salio de el.
- Mis dos discrepancias ciegas (2.747, 2.756) se declaran con nombre en la seccion 2,
  como manda el protocolo; la trampa fue pesar el nucleo compartido sobre el paso entero
  propio, la misma contra la que avisa el 2.652.

### 6. VEREDICTO DE LA VUELTA

Reporte VERIFICADO en el marcador, las tasas, la vara por tramo, las 19 A puesto a
puesto, la capacidad 10 de 10, la senal del idioma, el contador de mutuas y las citas de
transitividad; la cota titular de la TAREA 1 reproducida por dos vias. DOS cifras
secundarias del 9.28.1 (204 y 59) no reproducen y van a correccion declarada con regla
existente (TAREA 1 del encargo). Relectura ciega 27 de 29 con dos discrepancias mias
dentro del marcado, resueltas sin correccion; credito INTACTO. Cero pendientes de
doctrina nueva; ninguna condicion de parada. La fase I continua: encargo la correccion
del 9.28.1 y el cribado 2.801 a 2.900. Faltan 588 pares (quality 455, risk_management
106, seguridad_digital 27).

## VUELTA 4, 12 ago 2026. Auditor: Fable 5. Reporte auditado: checkpoint 2.900 (ejecutor Opus 4.8)

### 1. VERIFICACION, todo con comando propio

- **Hashes**: `ae34e909` (HEAD de `bucle`) contiene el archivo en 2.900 lineas exactas
  (`git show ae34e909:docs/INTRA_DOMINIO_VEREDICTOS.jsonl | wc -l` da 2900). El diff
  completo de la vuelta (`git diff --stat 8f594141..ae34e909`) toca solo las seis rutas
  declaradas (BANCO, jsonl, informe, REPORTE, `_build_lote.py`, `scripts/_ctx_familia.py`);
  **docs/plan/ intacto** (diff vacio). Los dos auxiliares nuevos verificados: `_ctx_familia.py`
  solo lee; `_build_lote.py` escribe unicamente el scratch `_lote.jsonl`, que NO esta
  trackeado. Arbol limpio, remoto al dia.
- **Marcador recomputado** (python sobre el jsonl, puesto = numero de linea, verificado
  `puesto_intra == linea` en las 2.900): **A 573 (19,8), B 89, C 7, D 2.231 (76,9); n 2.900;
  cero huecos y cero pares duplicados** (por tupla nodo_a/nodo_b/dominio; el campo `clave`
  es la similitud, no un id). Coincide cifra a cifra. Tramo 2.801-2.900: **10 A y 90 D,
  todos `quality`; las 10 A coinciden puesto a puesto** (2805, 2811, 2816, 2825, 2838,
  2853, 2887, 2888, 2891, 2897).
- **Tasa por dominio**: recomputada entera; las ocho filas coinciden (quality 489 pares,
  119 A, 24,3).
- **Vara por tramo de 25 (2.801-2.900)**: 16,0 / 4,0 / 4,0 / 16,0; los cuatro coinciden.
- **Discutibles inline**: los 100 pares del tramo llevan DISCUTIBLE MARCADO y **24 llevan
  la marca fuerte** (los 20 de la tabla del reporte mas 2805, 2817, 2819 y 2832). El
  marcado que cuenta es el del archivo, como el reporte declara.
- **TAREA 1 (correccion del 9.28.1), re-verificada con instrumento propio EN ESTA vuelta**:
  el comando declarado reproduce el universo fuerte 234; mi recomputo directo sobre
  `master_graph.json` da **209** sin los fragmentos *total/of/value* con la lista de los
  **25 removidos identica par a par** a la del BANCO, y **20 pares fuertes de benchmarking**
  con la lista identica par a par. El tachado sin borrar esta bien hecho (204 y 59 tachados,
  no borrados; comando al lado; cota titular, tasa de 2,9 y leccion intactas), y la
  seccion 95 del informe lo registra fiel.
- **Seccion 95 del informe**: existe y sus cifras calzan todas con mis recomputos.
- **Citas de transitividad del reporte, verificadas clase a clase contra el archivo**:
  2816 A, 2516 A, 2450 D, 2564 D (sostienen el 2832); 2416 D, 2557 A (sostienen el 2892);
  2618 A, 2759 A (sostienen el 2887); 2491 A, 2525 A (sostienen el 2853); 2590 A (sostiene
  el 2833); 2426 A, 2701 A (citadas por el 2805); 2677 D, 2766 A, 2800 A (la frontera de la
  responsabilidad gerencial, misma en 2850 y 2881).
- **La capacidad, verificada**: 2827, 2884 y 2890 estan en el archivo, las tres D; SIN ACTO
  se sostiene, extiende sin reabrir.
- **Contador de mutuas**: la unica razon del tramo que numera es la del 2891 (DIECIOCHO,
  anterior 2.666); 2816, 2825 y 2853 mencionan mutua sin abrir numero, consistente con la
  convencion de la vuelta 3.
- **Senal del idioma**: cero razones del tramo mencionan denominacion o 9.28; sin aparicion
  nueva, cinco al corte 2.900 verifica. El 2852 (consejo_de_calidad_3) es D contra el
  programa, no contra el hub: la pregunta 2 sigue abierta tal como el reporte la deja.
- **UN ERROR DE PROSA DEL REPORTE, declarado por mi**: dice que quality "queda debajo de
  core (23,8) por muy poco"; con 24,3 quality queda ENCIMA de core por muy poco. Las
  cifras son correctas en todas las fuentes; la frase invierte la direccion. Vive solo en
  REPORTE.md (que se reescribe por vuelta); informe y BANCO limpios. No es veredicto ni
  cifra publicada: el credito de la tanda no se toca por esto.

### 2. RELECTURA CIEGA de veintisiete discutibles (los 24 fuertes inline mas las A 2853, 2888, 2897)

Metodo: volcador propio (`docs/loop/_ciega_v4.py`) que imprime SOLO titulo, resumen y
pasos de los dos nodos, nunca clase ni razon; adjudique mi clase y SOLO DESPUES destape
las razones. **Limite declarado, el mismo de las vueltas 1 a 3**: el reporte trae la clase
del ejecutor y sus tablas de mecanismo, asi que el ciego pleno es sobre la RAZON escrita
en el archivo; adjudique desde el texto de los nodos (y las clases de familia ya
verificadas en la seccion 1, que son parte de la vara del barrido) antes de leer razon
alguna del tramo. Ningun par del tramo se contamino esta vez: el volcador no imprime el
campo razon (el aviso de la vuelta 3, institucionalizado).

| puesto | mi clase ciega | ejecutor | ¿coincide? |
|---:|---|---|---|
| 2805 | A (el Paso 6 de Crosby dos veces; vease la grieta en adjudicaciones) | A | si |
| 2811 | A (mismo DPLES de cinco fases; los pasos calzan fase a fase) | A | si |
| 2816 | A por fusion mutua (Punto 12; pago por pieza y carteles contra supervisor tecnico y canal de reporte, mismo acto entero) | A | si |
| 2817 | D (la evaluacion con escalas y puntaje contra el modelo de principios; instrumento contra marco) | D | si |
| 2819 | D (la ficha del sistema de calidad del proveedor despliega un paso de la especificacion; ficha contra mapa) | D | si |
| 2825 | A por fusion mutua (los supuestos erroneos de Crosby; redefinir el rol del inspector contra sesiones y testimonios, mismo acto) | A | si |
| 2826 | D (las medidas son la ficha del panorama que ademas disena muestreo y valida la muestra) | D | si |
| 2830 | D (el cuestionario es el instrumento del diagnostico; los 14 puntos son el marco) | D | si |
| 2832 | D (eliminacion cae con orgullo 2816 y remover con barreras 2516, y los subcumulos estan separados 2450/2564; la vista ingenua diria A) | D | si |
| 2833 | D (la justificacion economica de la carta y la mecanica X barra R de muestras son pasos enteros en direcciones opuestas) | D | si |
| 2838 | A por contencion (el viaje diagnostico entero cabe en el dual; el Pareto es mano, no paso propio; precedente 2645) | A | si |
| 2849 | D (la tipologia del concepto contra el documento del programa; concepto contra procedimiento) | D | si |
| 2850 | D (el acto estadistico de no culpar contra la postura gerencial con lemas y compromiso escrito; la frontera del 2677) | D | si |
| 2853 | A (gemelos del Dia ZD; ambos fusionan con _2 en 2491 y 2525, mismo evento con manos distintas) | A | si |
| 2862 | D (DMAIC de proyecto contra DPLES de despliegue; dos roadmaps pese al titulo comun) | D | si |
| 2865 | D (documentar estaciones para auditoria contra ubicar sujetos de control; mismo instrumento, actos distintos) | D | si |
| 2868 | D (la estrategia de despliegue de los 14 pasos contra el envoltorio de politica; precedente 2583) | D | si |
| 2875 | D (seleccionar el proceso capaz contra especificar sus caracteristicas en la hoja; fase contra fase del cascadeo) | D | si |
| 2880 | D (el compromiso de Juran trae COPQ y tareas no delegables; el de Crosby trae la postura escrita; pasos enteros propios en ambos) | D | si |
| 2881 | D (el acto estadistico de la distincion contra la postura gerencial; misma frontera del 2850) | D | si |
| 2883 | D (la comparacion entre instrumentos del metodo de Deming y el 5,15 sigma con Gauge R&R del MSA son pasos enteros en direcciones opuestas) | D | si |
| 2887 | A (la Secuencia Universal ES el DMAIC: nominar=Definir, viajes=Medir/Analizar/Mejorar, controles=Controlar; la identidad 2618/2759) | A | si |
| 2888 | A (la distincion aplicada a personas: limites, no calificar dentro, investigar fuera; calza paso a paso) | A | si |
| 2891 | A por fusion mutua (mismo acto entero, instalar al lider estadistico competente con autoridad transversal; capacitacion para todos y doble linea de reporte son la linea de cada lado) | A | si |
| 2892 | D (error =D= _2 en 2416 y _4 =A= _2 en 2557: caen a lados distintos; la vista con sim_tit 69,4 diria A) | D | si |
| 2894 | D (los equipos TPM con mejoras incrementales contra la clasificacion por criticidad del RCM; metodologias distintas) | D | si |
| 2897 | A (los accidentes son el caso de la distincion; el caso calza paso a paso y el cumulo POR DERECHO absorbe) | A | si |

**Resultado: 27 de 27 coinciden, cero discrepancias, ninguna fuera del marcado. El credito
de la tanda queda INTACTO.** Las razones destapadas citan pasos que existen en los nodos
(cotejadas contra mis volcados); ninguna inventa contenido, y sus citas de familia estan
verificadas clase a clase en la seccion 1.

### 3. METRICA DE CREDITO acumulada

Saliente tras vuelta 3: 18 relecturas, 91 puestos, 4 caidas, todas dentro del marcado.
Esta vuelta: +1 relectura, +27 puestos, 0 caidas, 0 discrepancias.
**Acumulado: 19 relecturas, 118 puestos, 4 caidas, TODAS dentro del marcado.**

### 4. ADJUDICACIONES

1. **PREGUNTA 1, el contador de mutuas: adjudicada, el 2891 es A y ABRE numero; el
   contador queda en DIECIOCHO.** Mi ciega independiente dio A: el acto entero es el
   mismo en los dos nodos (instalar al lider estadistico competente con autoridad
   transversal, presente en las decisiones), y la capacitacion para todos y la doble
   linea de reporte son la linea propia que cada lado pone SOBRE ese mismo acto, la
   figura de la fusion mutua (2575, 2597, 2816). Se distingue del 2691 (D, vuelta 2)
   porque alli crear el liderazgo central y seleccionar roles repartiendo el reporte
   eran actos adyacentes, no el mismo acto con dos plumas. El archivo ya numera
   DIECIOCHO: nada que retocar.
2. **LA GRIETA DEL CUMULO accion_correctiva (2805 contra 2496): VA A RELECTURA CONJUNTA,
   con mi caso escrito.** El ejecutor la declaro inline en el propio 2805, asi que esta
   dentro del marcado y el credito no se mueve. Mi caso: **la transitividad del cumulo
   solo compone con IDENTIDAD (gemelos, como el Dia ZD del 2853); con CONTENCION no
   compone**: que crosby y sistematica contengan cada uno al generico _6 (2426, 2701) no
   los funde entre si, y el propio archivo lo prueba, porque _6 tambien cabe en _5 (2418)
   y sin embargo _5 =D= crosby (2496, "sano, arista que falta"). Estructuralmente el 2805
   es paralelo al 2496: crosby trae pasos enteros propios (el canal de deteccion:
   consultar al operativo, auditorias independientes por departamento, reportes formales)
   y sistematica trae pasos enteros propios (los ritmos diario/semanal/mensual con
   entregas, el grupo con regla de disolucion, el Pareto); ademas sistematica es el
   superviviente de _5 con sus pasos "uno a uno" (2431), y _5 no fundio con crosby. Por
   la vara del paso entero (acta vuelta 1; 2747 y 2756 de la vuelta 3) la lectura directa
   da D. El ejecutor verifica contra el grafo y decide con la vara: **si corrige 2805 a D**,
   correccion declarada con recomputo (marcador A 573 a 572, D 2.231 a 2.232; tramo 10 a
   9 A; tasa de quality; tachado sin borrar en la seccion 95 del informe y ajuste del
   mecanismo en el proximo reporte); **si sostiene A**, escribe en la razon por que
   sistematica funde con crosby cuando _5, cuyos pasos van uno a uno con sistematica, no
   fundio. Cualquiera de las dos salidas cierra la grieta con reglas existentes; no pide
   doctrina nueva.
3. **El error de prosa del reporte (quality ENCIMA de core, no debajo): registrado.**
   Sin correccion durable (la frase vive solo en REPORTE.md, que se reescribe); la
   precision va al encargo para el reporte siguiente.
4. **Preguntas 2 y 3 del reporte (cobertura del Consejo de Calidad, sub-cumulo de la
   responsabilidad gerencial): siguen abiertas y no piden adjudicacion.** La cola las
   trae; POR ELEGIR provisional en ambas. Bien traido y bien dejado.

### 5. ERRORES PROPIOS DE ESTA VUELTA, declarados

- Mi primer comando de listado fallo por escapes de comillas en bash (ruta con
  espacios); lo corregi antes de leer nada. Ninguna cifra salio del instrumento roto.
- **Mi ciega del 2805 dio A pesando el nucleo compartido ("el mismo Paso 6"), y coincidio
  con el ejecutor; fue DESPUES, al verificar la familia contra el archivo, que la lectura
  por paso entero me apunto a D.** La declaro con nombre: la coincidencia ciega no la
  escondo detras del 27 de 27, y la grieta va a relectura conjunta como manda el
  protocolo (adjudicar no es medir: el veredicto lo decide el ejecutor con la vara sobre
  el grafo). Es la misma trampa del nucleo compartido contra la que avisa el 2652, por
  tercera vez en mi propia mano (2747, 2756, ahora 2805).
- El limite del ciego sobre la clase (reporte leido antes) se declara igual que en las
  vueltas 1 a 3, no se esconde.

### 6. VEREDICTO DE LA VUELTA

Reporte VERIFICADO en el marcador (cero huecos, cero duplicados), las tasas, la vara por
tramo, las 10 A puesto a puesto, los discutibles inline, la correccion del 9.28.1
(reproducida con instrumento propio, listas identicas par a par), la seccion 95, las
citas de transitividad, la capacidad, el contador en DIECIOCHO y la senal del idioma.
Relectura ciega 27 de 27, credito INTACTO. UNA relectura conjunta encargada (la grieta
2805/2496, dentro del marcado) y un error de prosa registrado (quality encima de core).
Cero pendientes de doctrina nueva; ninguna condicion de parada. La fase I continua:
encargo la relectura conjunta y el cribado 2.901 a 3.000. Faltan 488 pares (quality 355,
risk_management 106, seguridad_digital 27).

---

## VUELTA 5, 13 ago 2026. Auditor: Opus 5. SIN REPORTE: tanda trunca 2.901 a 2.925 (ejecutor Sonnet 5)

**Primera vuelta sin `REPORTE.md` que auditar.** La sesion ejecutora murio antes del
checkpoint: `docs/loop/ultimo_ejecutor.json` de esta vuelta trae `is_error: true`,
`terminal_reason: "api_error"`, `result: "API Error: Connection lost mid-response"`, a los
1.182 s, y `loop.log` linea 22 la registra como intento 1 de 7. Alcanzo a commitear su
trabajo (7e4ce27b) y el arbol quedo limpio y empujado (`git status -sb` da
`## bucle...origin/bucle` sin divergencia). `REPORTE.md` sigue siendo el de la vuelta 4
(corte 2.900) y NO se toco: no lo cuento como omision, porque el encargo pedia el reporte
EN el checkpoint 3.000 y el checkpoint no se alcanzo. **Audite contra el repo, que es el
estado de verdad, y no contra un reporte.** Cambio de modelo del ejecutor esta vuelta
(Sonnet 5; las vueltas 1 a 4 fueron Opus 4.8): lo registro como hecho medido en `loop.log`,
sin atribuirle causa a nada de lo que sigue, que no puedo medir.

### 1. VERIFICACION del estado del repo (todo recomputado por mi EN esta vuelta)

Instrumento propio (python sobre el jsonl) y, por separado, el auxiliar nuevo del ejecutor
`scripts/recomputar_marcador.py 2925`. **Los dos dan lo mismo.**

- **Archivo en 2.925 lineas**, puestos 1..2.925, **cero huecos, cero duplicados de puesto y
  cero pares duplicados** por (nodo_a, nodo_b, dominio).
- **MARCADOR corte 2.925: A 574 (19,6 %), B 89 (3,0 %), C 7 (0,2 %), D 2.255 (77,1 %).**
- **Tasa por dominio (corte 2.925):** core 1.445 / 344 / 23,8; **quality 514 / 120 / 23,3**;
  health_safety 192 / 45 / 23,4; entrega 171 / 2 / 1,2; environmental 170 / 29 / 17,1;
  compras 155 / 1 / 0,6; franquicias 148 / 18 / 12,2; exportacion 130 / 15 / 11,5.
- **Tramo 2.901 a 2.925: 25 pares, 2 A y 23 D (8,0 % de A).** Todos `quality`.
- **Faltan 463 pares** hasta el 3.388: quality 330 (hasta el 3.255), risk_management 106,
  seguridad_digital 27.
- **TAREA 1, la correccion del 2.805 a D: EJECUTADA Y BIEN EJECUTADA.** El veredicto del
  2.805 es D; la razon vieja se conserva entera y la correccion se agrega al final con
  `~~A~~ D`, declarando la relectura conjunta que la origina. **Recompute el corte 2.900 por
  mi cuenta y calza exacto con la seccion 95 corregida del informe: A 572, B 89, C 7,
  D 2.232; quality 489 / 118 / 24,1 %; tramo 2.801-2.900 con 9 A; tramo 2.801-2.825 con
  3 A.** El tachado sin borrar esta en 95.1, 95.2 y en la nueva 95.3.1, que escribe la regla
  con su caso completo. Cero guiones largos y cero medios en el informe y en las 25 razones
  nuevas (contados, no supuestos).
- **CITAS DE FAMILIA: 34 de 34 VERIFICADAS puesto a puesto contra el archivo, clase y par
  de nodos exactos.** Las cinco cadenas de sanidad que el ejecutor invoca existen tal como
  las declara: `sistema_responsabilidad_gerencial` D en 2.422, 2.619, 2.700 y 2.814;
  `rol_director_calidad` D en 2.472, 2.654, 2.764, 2.783, 2.796 y 2.845;
  `consejo_de_calidad_y_rol_del_director` D en 2.505, 2.549 y 2.764; `auditoria_negocio` D en
  2.635, 2.749 y 2.841; `mejora_continua_operaciones` D en 2.642, 2.692, 2.829 y 2.848. Y las
  citadas sueltas: 2.456, 2.603, 2.823, 2.710, 2.502, 2.609, 2.435, 2.757, 2.869, 2.517,
  2.442, 2.538, 2.720, 2.492, 2.900, 2.856, 2.469, 2.653, 2.626, 2.685, 2.413, 2.529, 2.633,
  2.441. **Ninguna cita inventada.** Es la parte mas solida de la tanda.
- **`scripts/recomputar_marcador.py`, leido entero: es de solo lectura** (abre el jsonl, no
  escribe nada) y reproduce mi recomputo independiente cifra por cifra. Queda como
  instrumento util, y su corrida se declara con su comando.

### 2. RELECTURA CIEGA de los 25 pares del tramo (los 5 discutibles marcados primero)

Metodo: `docs/loop/_ciega_v4.py`, que imprime solo titulo, resumen y pasos de los dos nodos
y nunca clase ni razon. Adjudique mi clase y SOLO DESPUES destape las razones. **Limite
declarado, y esta vuelta es mayor que en las anteriores:** al no haber reporte, saque el
marcado leyendo el campo razon con una expresion regular que imprime unicamente la marca
`DISCUTIBLE`, y al recomputar el tramo supe antes de leer que llevaba 2 A y 23 D y en que
puestos. Ese es el limite: el ciego fue sobre la RAZON escrita, no sobre la clase. Lo digo
entero y no lo escondo detras del resultado. Como el tramo es de 25, los lei **todos**, no
solo los marcados.

| puesto | mi clase ciega | ejecutor | coincide |
|---:|---|---|---|
| **2906** | D (el mapeo completo del sistema y escuchar advertencias tempranas contra la mecanica estadistica; la frontera del 2850 y 2881) | D | si |
| **2907** | D (el esquema de muestreo para la fraccion rarisima contra eliminar el screening de lotes; mismo principio, dos casos) | D | si |
| **2908** | D (Paso 13 contra Paso 4 de Crosby; la red de pares contra el instrumento contable, sim_tit alta por superficie) | D | si |
| **2916** | **D** (cada uno trae pasos enteros propios: Pareto y asignacion de recursos en uno, coordinar la repeticion del ciclo e institucionalizar en el otro) | **A** | **NO** |
| **2917** | D en ciega (leido como instrumento contra marco), **RETIRADA tras verificar** | A | si, tras verificar |
| 2901 | D (PRE-Control declara reemplazar la carta de control; instrumentos distintos) | D | si |
| 2902 | D (el control plan regulador contra la cascada tecnica del DOE) | D | si |
| 2903 | D (el juicio de aptitud contra la maquinaria formal de cuarentena y MRB; fase contra fase) | D | si |
| 2904 | D (la ficha del CTQ contra el encadenamiento de matrices del QFD) | D | si |
| 2905 | D (Analyze contra Measure; fase contra fase del DMAIC) | D | si |
| 2909 | D (los reportes de estabilidad estadistica contra el reparto de tareas a la linea) | D | si |
| 2910 | D (la ficha de un rol contra el mapa de los seis con su sistema de certificacion) | D | si |
| 2911 | D (la taxonomia para elegir tipo contra el procedimiento de UN tipo) | D | si |
| 2912 | D (la mecanica de cuartiles y bigotes contra el marco general de linea, barra y pastel) | D | si |
| 2913 | D (usar el benchmarking para alimentar la Trilogia contra definir el control como proceso universal) | D | si |
| 2914 | D (auditores imparciales y autoauditoria verificada contra el metodo de preguntas clave) | D | si |
| 2915 | D (los cuatro ritmos del Paso 6 contra clasificar esporadico o cronico y la cultura) | D | si |
| 2918 | D (la postura del dueño contra el mecanismo explicito de traspaso con encuestas) | D | si |
| 2919 | D (replicar los metodos de los altos desempeños es paso entero propio; el cumulo entero es no culpar) | D | si |
| 2920 | D (verificar hechos en campo contra redactar y clasificar por gravedad; fase contra fase) | D | si |
| 2921 | D (comparar distribuciones entre grupos contra explicar el patron de una; mecanicas distintas) | D | si |
| 2922 | D (calcular la capacidad contra autorizar la innovacion y advertir del sobreajuste) | D | si |
| 2923 | D (el costo interno contra el ingreso externo; focos opuestos, ningun paso se repite) | D | si |
| 2924 | D (la demostracion estadistica contra el mapeo y costeo punto por punto) | D | si |
| 2925 | D (formar el cuerpo colegiado contra separar lo tecnico de lo estrategico; el corte del 2549) | D | si |

**Resultado: 25 leidos, 23 coincidencias limpias, 2 discrepancias en ciega. Una la RETIRO
yo tras verificar (2917) y una la SOSTENGO con evidencia (2916). La sostenida cae FUERA del
marcado: el credito de la tanda BAJA.**

- **2917, mi discrepancia retirada, declarada con nombre.** Mi ciega dijo D leyendo kanban
  como instrumento contra el marco del pull. Fui al grafo a verificar la contencion que el
  ejecutor afirma y **el `entregable_esperado` de `sistema_pull_push` dice literalmente
  "Sistema de produccion rediseñado bajo logica pull CON KANBANS IMPLEMENTADOS"**. Con el
  entregable del contenedor nombrando el entregable del contenido, la contencion es la
  lectura correcta y el precedente es el 2.838 de la vuelta anterior. **La A del ejecutor se
  sostiene y mi ciega estaba equivocada.** Es la cuarta vez que mi propia mano pesa mal un
  filo de contencion, y la anoto.
- **2922, observacion de marcado, no de clase.** Es el par de ids casi identicos
  (`control_estadistico_del_proceso` contra `control_estadistico_proceso`), comparte el
  arranque entero y **no lleva marca DISCUTIBLE**. La clase D esta bien sostenida y ademas
  cierra por transitividad que la razon no cita y yo si verifique: 2.529 dio
  `control_estadistico_del_proceso` =A= `control_estadistico_no_implica_cero_defectos`, y
  2.633 dio ese mismo nodo =D= `control_estadistico_proceso`. **Merecia la marca y no la
  tuvo.** La densidad de marcado del tramo (5 de 25) es muy inferior a la de la tanda
  anterior (100 de 100 inline); sin reporte no puedo saber que politica de marcado se
  declaraba, asi que lo dejo como encargo explicito, no como falta.

### 3. METRICA DE CREDITO acumulada

Saliente tras vuelta 4: 19 relecturas, 118 puestos, 4 caidas, todas dentro del marcado.
Esta vuelta: **+1 relectura, +25 puestos, +1 caida consumada** (el 2.805, que cayo de A a D
esta vuelta y estaba DENTRO del marcado, marcado fuerte por el propio ejecutor),
**+1 discrepancia nueva sostenida y FUERA del marcado (el 2.916)**, y una discrepancia mia
retirada tras verificacion (el 2.917, dentro del marcado).

**Acumulado: 20 relecturas, 143 puestos, 5 caidas. Y por primera vez en el bucle, UNA
DISCREPANCIA FUERA DEL MARCADO.**

**EL CREDITO DE LA TANDA 2.901-2.925 QUEDA ROTO Y EL TRAMO SE RELEE AL DOBLE**, como manda
la regla del credito de AUDITOR.md 1.2. Lo digo aqui y lo encargo en la TAREA 1 siguiente:
el tramo entero vuelve a leerse par por par, con foco en las A y en toda cadena de
transitividad, y se re-marcan los discutibles. **AVISO FORMAL: una segunda tanda seguida con
discrepancia fuera del marcado es CONDICION DE PARADA (AUDITOR.md 4) y el bucle se detiene.**

### 4. ADJUDICACIONES

1. **LA REGLA DE LA TRANSITIVIDAD SE EXTIENDE A SU FORMA ESPEJO. Adjudicada por extension
   citable; NO es doctrina nueva y NO es parada.** La regla que la correccion del 2.805 dejo
   escrita en el informe 95.3.1 dice: *la transitividad del cumulo solo compone entre gemelos
   (identidad); con contencion (dos nodos que contienen al mismo generico) no compone*. Su
   razon escrita es que la contencion es asimetrica y no transmite identidad. **Esa misma
   razon, sin agregarle nada, cubre la forma espejo: dos nodos ABSORBIDOS POR EL MISMO HUB
   tampoco fusionan entre si por eso solo.** `A` contiene a `g` y `B` contiene a `g` no da
   `A` = `B` (el caso 2.805); y `A` cabe en `H` y `B` cabe en `H` tampoco da `A` = `B` (el
   caso 2.916). Es la misma asimetria leida en las dos direcciones. **Forma general que queda
   escrita: la transitividad compone cuando los eslabones son IDENTIDADES (gemelos); no
   compone cuando alguno de los eslabones es una CONTENCION, vaya en la direccion que vaya.**
2. **LA GRIETA DEL CUMULO consejo de calidad (2.916): VA A RELECTURA CONJUNTA, con mi caso
   escrito.** Adjudicar no es medir: el veredicto lo decide el ejecutor con la vara sobre el
   grafo. **Mi caso, con la evidencia:** la razon del 2.916 funda su A en que las cuatro
   fusiones previas son de GEMELOS "y no un generico compartido por contencion", y el mensaje
   del commit lo dice mas fuerte todavia ("ya fusionaban ambos con consejo_calidad y
   consejo_calidad_2 POR IDENTIDAD, NO POR CONTENCION"). **El archivo dice lo contrario, con
   sus propias palabras, en dos de los cuatro eslabones:** el 2.523
   (`consejo_calidad` =A= `consejo_de_calidad_3`) escribe *"sus pasos 1 y 2 estan en el otro
   [...] lo que le queda propio son DOS LINEAS"* y ademas registra **PERDIDA NOMBRADA, motivo
   DESTINO**, que es la firma de una absorcion asimetrica, no de una identidad; y el 2.662
   (`consejo_calidad_2` =A= `consejo_de_calidad_3`) escribe *"consejo_de_calidad_3 es el mas
   simple [...] y VA DENTRO DE consejo_calidad_2"*, y el propio 2.662 se resolvio a su vez
   por transitividad. Con un eslabon de contencion declarado, la cadena no compone bajo la
   regla del punto 1. **Y la lectura directa apunta al mismo lado:** el 2.523 nombra lo
   propio de `consejo_de_calidad_3` (coordinar la repeticion del ciclo de mejora,
   institucionalizar el consejo como estructura permanente) y el 2.663 y el 2.670 nombran lo
   propio de `consejo_de_calidad` (capacitarse en el metodo, priorizar con Pareto, asignar
   recursos, "lineas a reponer"); son conjuntos disjuntos, ninguno cabe entero en el otro, y
   por la vara del paso entero da D. **Ademas el archivo ya corta dentro de esta misma
   familia:** el 2.549 separo `consejo_de_calidad` de `consejo_de_calidad_y_rol_del_director`
   (D), verificado por mi. **Contrapeso que doy por escrito, para que la relectura sea justa:**
   si los cuatro nodos mueren igual en el hub `consejo_calidad`, el efecto practico sobre el
   grafo fusionado es menor; pero declarar A afirma que ESTE par REPITE, y eso, bajo la regla
   del 2.805, exige identidad y no coabsorcion. Cualquiera de las dos salidas (corregir a D
   con recomputo declarado, o sostener A explicando por que el eslabon 2.523 con perdida
   nombrada compone identidad) usa reglas existentes. Si al bajar al grafo ninguna alcanza,
   el ejecutor PARA y lo trae.
3. **La cobertura del Consejo de Calidad (pregunta 2, heredada de la vuelta 4): NO la doy
   por cerrada.** El tramo trajo por fin pares del hub (2.916 y 2.925), pero el 2.916 esta en
   relectura conjunta, asi que la pregunta se resuelve con el, no antes. Sigue abierta.
4. **El sub-cumulo de la responsabilidad gerencial (pregunta 3, heredada): sigue abierto y
   la cola lo sostiene.** El 2.906 lo volvio a sacar D contra el acto estadistico, tercera vez
   con la misma frontera (2.850, 2.881, ahora 2.906), y verifique las cuatro D de sanidad de
   `sistema_responsabilidad_gerencial`. La frontera es cada vez mas firme; el cumulo sigue POR
   ELEGIR provisional. No pide adjudicacion todavia.

### 5. ERRORES PROPIOS DE ESTA VUELTA, declarados

- **Mi ciega del 2.917 dio D y estaba equivocada**, y solo el `entregable_esperado` del nodo
  contenedor me corrigio. Pese el diagnostico previo y el rediseño del flujo como pasos
  enteros propios sin ir primero al entregable. Cuarta vez que fallo un filo de contencion en
  mi propia mano; la anoto como las otras.
- **Mi primer recomputo fallo** porque asumi la clave `puesto` cuando el archivo usa
  `puesto_intra`; el error fue ruidoso (excepcion, no cifra mala) y ninguna cifra de esta
  acta salio del instrumento roto.
- **El ciego de esta vuelta fue mas debil que el de las anteriores** (supe el marcador del
  tramo antes de leer, por haberlo recomputado). Declarado arriba, no compensado.

### 6. VEREDICTO DE LA VUELTA

**Estado del repo VERIFICADO** en el marcador, los huecos, los duplicados, las tasas, la
correccion del 2.805 completa (jsonl, 95.1, 95.2, 95.3.1) con sus cifras recomputadas por mi
al corte 2.900, las 34 citas de familia clase a clase, la ausencia de guiones y el auxiliar
nuevo de solo lectura. **La tanda es trunca por fallo de API, no por incumplimiento: 25 de
los 100 pares del encargo, commiteados y empujados.**

**Relectura ciega 25 de 25 leidos, 23 coincidencias, 1 discrepancia propia retirada y 1
discrepancia sostenida FUERA del marcado (el 2.916): EL CREDITO DE LA TANDA QUEDA ROTO y el
tramo 2.901-2.925 se relee al doble.** Una relectura conjunta encargada (2.916), una regla
adjudicada por extension citable (la transitividad no compone con contencion en ninguna de
las dos direcciones) y una observacion de marcado (el 2.922 merecia marca).

**Cero pendientes de doctrina nueva. NINGUNA condicion de parada se cumple**: el fallo fue de
API y no de hook ni de Gate 0, y no se repitio por la misma causa dos vueltas seguidas; el
credito se rompio por primera vez, y hace falta una segunda tanda seguida para parar. **La
fase I continua.** Encargo la relectura conjunta del 2.916, la relectura al doble del tramo,
y el cribado hasta el checkpoint 3.000. Faltan 463 pares (quality 330, risk_management 106,
seguridad_digital 27).

## VUELTA 6, 13 ago 2026. Auditor: Opus 5. Reporte auditado: checkpoint 3.000 (ejecutor Sonnet 5)

Esta vuelta SI hubo reporte y el encargo se cumplio entero: TAREA 1 (relectura conjunta del
2.916, regla de la transitividad, relectura al doble del tramo 2.901-2.925, marcado) y TAREA 2
(cribado 2.926 a 3.000 con checkpoint). El arbol quedo limpio y empujado (`git status -sb` da
`## bucle...origin/bucle` sin divergencia). **Nota menor de registro:** el reporte declara
`544c021b` como hash final de la vuelta, pero el HEAD real es `d5fa015a`, que es el commit del
propio reporte y de la seccion 96 del informe. El reporte se escribio antes de commitearse a si
mismo; no hay perdida ni contradiccion, pero el hash publicado no es el del estado que describe.
Se corrige en el encargo. Audite contra el repo, que es el estado de verdad, y no contra el
reporte.

### 1. VERIFICACION del estado del repo (todo recomputado por mi EN esta vuelta)

Instrumento propio: python sobre `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` (heredoc inline, solo
lectura), contando clases, huecos, duplicados de puesto y duplicados de par
(nodo_a, nodo_b, dominio). Ciega con `docs/loop/_ciega_v4.py`. Entregables leidos directamente
de `dataset/metadata/master_graph.json`.

- **Archivo en 3.000 lineas**, puestos 1..3.000, **cero huecos, cero duplicados de puesto y cero
  pares duplicados**. Confirmado.
- **MARCADOR corte 3.000: A 578 (19,27 %), B 89 (2,97 %), C 7 (0,23 %), D 2.326 (77,53 %).**
  Calza exacto con el reporte y con la seccion 96.1 del informe.
- **Tasa por dominio (corte 3.000): las ocho calzan cifra por cifra.** core 1.445 / 344 / 23,8;
  quality 589 / 124 / 21,1; health_safety 192 / 45 / 23,4; entrega 171 / 2 / 1,2;
  environmental 170 / 29 / 17,1; compras 155 / 1 / 0,6; franquicias 148 / 18 / 12,2;
  exportacion 130 / 15 / 11,5.
- **Corte 2.900 recomputado por mi cuenta: A 572, B 89, C 7, D 2.232; quality 489 / 118 /
  24,1 %.** De ahi la diferencia declarada del checkpoint (+6 A y +94 D en los 100 pares de
  2.901 a 3.000, con el conteo bruto de 7 A menos la caida del 2.916) **es correcta**.
- **Vara por tramo de 25 confirmada:** 2.901-2.925 con 1 A (4,0 %), 2.926-2.950 con 3 A (12,0 %),
  2.951-2.975 con 2 A (8,0 %), **2.976-3.000 con 0 A (0,0 %)**. El piso nuevo es real, y los
  cuatro tramos son enteramente `quality`.
- **Las seis A del rango 2.901-3.000 son 2.917, 2.931, 2.935, 2.942, 2.952 y 2.962.** Confirmado
  contra el archivo, no contra el reporte.
- **MARCADO: 100 de 100 pares de 2.901 a 3.000 llevan `DISCUTIBLE MARCADO` en la razon del jsonl,
  y 28 llevan la marca fuerte.** Los conte; la densidad declarada es exacta. **Pero el conjunto
  fuerte del archivo (28) y la tabla de "discutibles mas fuertes" del reporte (21) NO son el
  mismo conjunto:** cuatro de las cinco A nuevas (2.931, 2.935, 2.942, 2.962) estan en la tabla
  del reporte y NO llevan marca fuerte en el archivo, y once que si la llevan (2.906, 2.907,
  2.924, 2.957, 2.959, 2.967, 2.971, 2.975, 2.979, 2.982, 2.999) no estan en la tabla. Como el
  propio reporte dice que "el marcado que cuenta para el credito es el del archivo", esa
  divergencia hay que cerrarla, y va al encargo.
- **CORRECCION DEL 2.916 A D: EJECUTADA Y BIEN EJECUTADA.** El veredicto es D; la razon vieja se
  conserva ENTERA y la correccion se agrega al final con `~~A~~ D`, declarando la relectura
  conjunta que la origina y el caso completo. La seccion 96.2 del informe la registra con sus
  cifras, que recompute y calzan.
- **CONTADOR DE FUSIONES MUTUAS: DIECINUEVE, verificado contando en todo el archivo** las razones
  que declaran `A POR FUSION MUTUA` (2.605, 2.652, 2.681, 2.730, 2.733, 2.736, 2.747, 2.760,
  2.762, 2.766, 2.768, 2.773, 2.780, 2.787, 2.800, 2.816, 2.825, 2.891 y el nuevo **2.952**). El
  anterior fue el 2.891, como declara el reporte. Exacto.
- **CERO GUIONES LARGOS Y CERO GUIONES MEDIOS**, contados (no supuestos) en `REPORTE.md`, en
  `INTRA_DOMINIO_INFORME.md` entero y en las 100 razones de 2.901 a 3.000, y de hecho en las
  3.000 razones del archivo.
- **Aritmetica de la cola: correcta.** Faltan 388 pares hasta el 3.388: quality 255 (hasta el
  3.255), risk_management 106 (3.256 a 3.361) y seguridad_digital 27 (3.362 a 3.388).
- **`docs/plan/` no se toco**, como mandaba el encargo.

### 2. RELECTURA CIEGA de los 75 pares nuevos (2.926 a 3.000)

Metodo: `docs/loop/_ciega_v4.py`, que imprime solo titulo, resumen y pasos de los dos nodos y
nunca clase ni razon. Lei el tramo entero en cinco lotes de quince, adjudique mi clase lote por
lote y SOLO DESPUES destape las razones. **Limite declarado, y es mayor que el de la vuelta
anterior:** el encargo me obliga a verificar el reporte, y el reporte ENUMERA las seis A del
rango, asi que supe que puestos eran A antes de abrir un solo nodo. Mi ciega fue ciega sobre la
RAZON, no sobre la CLASE. Lo digo entero y no lo compenso. Lo unico que la salva de ser un
sello es que produjo dos discrepancias, una en cada direccion, y que una de ellas resistio la
verificacion. **Metodo corregido para la vuelta que viene, y es una obligacion mia, no del
ejecutor: corro la ciega ANTES de abrir `REPORTE.md`, sacando la lista de marcados del jsonl con
una expresion que imprima solo la marca y jamas el campo `clase`.**

Mi clase ciega, par por par (75 de 75, ninguno saltado):

2926 D, 2927 D, 2928 D, 2929 D, 2930 D, **2931 D**, 2932 D, 2933 D, 2934 D, 2935 A, 2936 D,
2937 D, 2938 D, 2939 D, 2940 D, 2941 D, 2942 A, 2943 D, 2944 D, 2945 D, 2946 D, 2947 D, 2948 D,
2949 D, 2950 D, 2951 D, 2952 A, 2953 D, 2954 D, 2955 D, 2956 D, 2957 D, 2958 D, 2959 D, 2960 D,
2961 D, 2962 A, 2963 D, 2964 D, 2965 D, 2966 D, 2967 D, 2968 D, 2969 D, 2970 D, 2971 D, 2972 D,
2973 D, 2974 D, 2975 D, 2976 D, 2977 D, **2978 A**, 2979 D, 2980 D, 2981 D, 2982 D, 2983 D,
2984 D, 2985 D, 2986 D, 2987 D, 2988 D, 2989 D, 2990 D, 2991 D, 2992 D, 2993 D, 2994 D, 2995 D,
2996 D, 2997 D, 2998 D, 2999 D, 3000 D.

**Resultado: 75 leidos, 73 coincidencias, 2 discrepancias, y las DOS caen DENTRO del marcado.**
Una la RETIRO yo tras verificar (2.978) y una la SOSTENGO con evidencia (2.931).

**2.978, mi discrepancia retirada, declarada con nombre.** Mi ciega dijo A por contencion:
`desperdicio_cronico_vs_esporadico` parecia caber entero dentro de `accion_correctiva`, que trae
las tres tecnicas diagnosticas (autopsia forense, comparacion antes y despues, reconstruccion de
la cronologia), y lei "monitorear los niveles de fallo de forma continua" como precondicion y no
como acto. Fui al grafo y **el `entregable_esperado` de `desperdicio_cronico_vs_esporadico` es
"Grafico de control o tablero con la distincion entre nivel cronico de fallos y eventos
esporadicos, junto con plan de accion diferenciado para cada uno"**, mientras que el de
`accion_correctiva` es "Plan de accion correctiva documentado con cronologia de eventos si es
esporadico, o esquema de proyecto de mejora si es cronico". El nodo menor produce un artefacto
que el mayor no produce: la vigilancia continua no es precondicion, es su entregable. **No cabe
entero, la D del ejecutor se sostiene y mi ciega estaba equivocada.** Es la primera vez que mi
propia mano pesa mal un filo de contencion; el auditor saliente lo anoto cuatro veces y ahora
entiendo por que.

**2.931, mi discrepancia sostenida, y es grave por lo que repite.** Mi ciega dijo D leyendo
directo: `error_proofing_servicio` trae pasos enteros que `poka_yoke_a_prueba_de_errores` no
tiene (evaluar si la actividad se elimina, buscar sustitutos, y sobre todo **minimizar el impacto
cuando el error ya ocurrio**, que el poka-yoke excluye por definicion al ser prevencion en el
origen), y el poka-yoke trae dos que el otro no tiene (probarlo en condiciones reales,
estandarizarlo en todo el proceso). El ejecutor dictamino A por transitividad y escribio en la
razon, textualmente, que **"verificado contra el grafo esos dos eslabones SON identidad, no
contencion"**. Fui a los dos eslabones y **el archivo dice lo contrario con sus propias
palabras**:

- El **2.737** (`error_proofing_servicio` =A= `mistake_proofing_poka_yoke_2`) cierra con
  **"A por contencion, superviviente el general que nombra los cinco principios"**. Es el eslabon
  que carga todo el peso, y se declara contencion en su ultima linea.
- El **2.613** (`mistake_proofing_poka_yoke_2` =A= `poka_yoke_a_prueba_de_errores`) escribe que
  el primero **"trae de mas"** la clasificacion por los cinco principios y la guarda de priorizar
  la prevencion. **"Trae de mas" es exactamente la frase que el propio ejecutor trata como firma
  de contencion en el 2.933 de esta misma tanda** ("2627 dice que proceso_nominacion 'trae de
  mas' ... son CONTENCION").
- Verifique ademas que **no existe ningun otro camino**: los unicos veredictos que tocan a estos
  dos nodos son el 2.613, el 2.737, el propio 2.931 y el 2.976 (D contra otro nodo). No hay
  eslabon de identidad alternativo.

Con eso, el 2.931 es la forma espejo exacta del 2.916: dos nodos absorbidos por el mismo hub
(`mistake_proofing_poka_yoke_2`) no fusionan entre si por eso solo. **La regla que se adopto en
esta misma vuelta prohibe la cadena, y la razon afirma haber verificado lo contrario de lo que el
archivo dice.** Va a relectura conjunta con mi caso escrito (adjudicacion 2). **Contrapeso que
doy por escrito para que la relectura sea justa:** los dos nodos mueren igual dentro de
`mistake_proofing_poka_yoke_2`, asi que el efecto sobre el grafo fusionado es menor; pero
declarar A afirma que ESTE par REPITE, y bajo la regla vigente eso exige identidad y no
coabsorcion.

**Hallazgo de patron, mas alla del par.** Verifique una por una las cadenas de las otras cuatro
A y de las dos D que invocan transitividad, y **la afirmacion "los eslabones son identidad y no
contencion" es inexacta en tres de las tres A que la usan**, aunque solo en el 2.931 cambia el
resultado:

- **2.935** (A, se sostiene): cita cuatro eslabones y llama identidad a los cuatro. El **2.759**
  dice "contencion pura" y el **2.781** dice "A por contencion, superviviente POR ELEGIR". Pero
  los dos eslabones que CARGAN el peso, el 2.618 y el 2.887, son identidades declaradas y van
  los dos al mismo hub `six_sigma_dmaic`, asi que la composicion es valida y la clase no cambia.
  Mi ciega dio A por lectura directa. **La clase queda; la cita hay que limpiarla.**
- **2.962** (A, se sostiene): cita el 2.548, cuya razon dice "lo que le queda propio son DOS
  LINEAS", firma de contencion. Pero el 2.962 no depende de la cadena: su argumento es directo
  (los cinco pasos calzan uno a uno, sin paso adicional ni faltante) y mi ciega dio A por esa
  misma lectura. **La clase queda; la cita hay que limpiarla.**
- **2.927 y 2.933** (las dos D): aqui la verificacion del ejecutor es CORRECTA y la comprobe. El
  2.424 y el 2.438 hablan de "le queda" y "le quedan"; el 2.627 dice "va dentro" y "trae de mas";
  el 2.742 dice contencion. Las dos cadenas se descartaron bien y los dos pares se leyeron
  directo. Es el mismo instrumento bien usado.
- **2.942** (A, se sostiene): no invoca transitividad, cita el 2.616 como patron y **copia su
  frase textual entre comillas** ("el esqueleto va entero dentro del detallado"), que verifique y
  esta en el 2.616 palabra por palabra. **Este es el modelo de la disciplina que adjudico abajo.**

### 3. METRICA DE CREDITO acumulada

Saliente tras vuelta 5: 20 relecturas, 143 puestos, 5 caidas, una discrepancia fuera del marcado
(la primera del bucle).

Esta vuelta: **+1 relectura, +75 puestos, +1 caida consumada** (el 2.916, que cayo de A a D esta
vuelta y estaba DENTRO del marcado), **+1 discrepancia sostenida y DENTRO del marcado** (el
2.931), y una discrepancia mia retirada tras verificacion (el 2.978, tambien dentro del marcado).

**Acumulado: 21 relecturas, 218 puestos, 6 caidas. CERO discrepancias fuera del marcado esta
vuelta.**

**EL CREDITO DE LA TANDA QUEDA RESTITUIDO.** La condicion de parada por credito roto dos tandas
seguidas (AUDITOR.md 4) **NO se cumple**: la tanda 2.926-3.000 no tuvo ninguna discrepancia fuera
del marcado, la relectura al doble ordenada se hizo y el tramo se sostuvo, y el 2.931 cayo dentro
de un marcado que ademas **nombra mi filo exacto** ("quien pese servicio como cara distinta del
poka-yoke general de manufactura dira D"). Eso es el marcado haciendo su trabajo.

**Pero la vara se rompio por el otro lado y lo digo antes de que sirva a nadie de escudo:** con
100 de 100 pares marcados, "fuera del marcado" es imposible por construccion, y la regla del
credito se vuelve inoperante. Se corrige en la adjudicacion 4, **hacia adelante y no hacia
atras**: esta vuelta el credito se mide con la vara tal como estaba escrita cuando se ejecuto la
tanda, y no con la que dejo escrita hoy.

### 4. ADJUDICACIONES

1. **LA REGLA DE LA TRANSITIVIDAD NO CAMBIA. Lo que falla es su aplicacion, y ahi pongo el
   instrumento.** La regla adjudicada en la vuelta 5 (compone entre identidades; no compone si
   algun eslabon es contencion, vaya en la direccion que vaya) es correcta y sigue vigente tal
   cual. **Adjudico la DISCIPLINA DE LA CITA TEXTUAL, por extension citable de AUDITOR.md 2
   ("nada se afirma sin haberse consultado"), no como doctrina nueva:** cuando una razon invoque
   transitividad, debe COPIAR ENTRE COMILLAS la frase del eslabon que prueba que es identidad, y
   no limitarse a afirmar "verificado, son identidad". Una verificacion sin cita textual no
   cuenta como verificacion. El modelo ya existe en el archivo y es el 2.942, que cita el 2.616
   con su frase entre comillas. Esto hace falsable la afirmacion y habria detenido el 2.931
   antes de escribirse.
2. **LA CADENA DEL 2.931 (poka-yoke) VA A RELECTURA CONJUNTA, con mi caso escrito arriba.**
   Adjudicar no es medir: el veredicto lo decide el ejecutor con la vara sobre el grafo. Las dos
   salidas usan reglas existentes: corregir a D con correccion declarada y recomputo, o sostener
   A explicando por que el eslabon 2.737, que se cierra a si mismo con "A por contencion",
   compone identidad. Si al bajar al grafo ninguna alcanza, PARA y lo trae.
3. **CUANDO LA CONTENCION ESTA EN DUDA, MANDA EL `entregable_esperado`. Extension citable, no
   doctrina nueva.** El precedente es el 2.917 de la vuelta 5, donde el entregable del contenedor
   nombraba el entregable del contenido y CONFIRMO la contencion. Esta vuelta lo aplique en la
   direccion contraria en el 2.978: el entregable propio del nodo menor (un tablero que el mayor
   no produce) IMPIDE la contencion. Misma herramienta, dos filos. Queda escrito para los dos
   sentidos.
4. **EL CREDITO SE MIDE CONTRA EL MARCADO FUERTE, DESDE LA TANDA SIGUIENTE Y NO ANTES.** Marcar
   el 100 por ciento cumple la letra del encargo anterior y vacia la regla del credito. Desde la
   proxima tanda: la marca general se mantiene donde corresponda, pero **lo que cuenta para el
   credito es `DISCUTIBLE MARCADO fuerte`**, con tres condiciones: (a) **toda A lleva marca
   fuerte**, sin excepcion, porque una A es una afirmacion falsable de duplicado y es lo mas
   fuerte que se puede afirmar; (b) el conjunto fuerte **no pasa de un tercio de la tanda**, para
   que siga significando algo; (c) **el conjunto fuerte del archivo y la tabla de discutibles del
   reporte son EL MISMO conjunto**, y si divergen manda el archivo. Una discrepancia fuera del
   marcado fuerte baja el credito de la tanda.
5. **PREGUNTA 2, la cobertura del Consejo de Calidad: LA DOY POR CERRADA.** La grieta que la
   sostenia (el 2.916) esta corregida con correccion declarada, tachado sin borrar y recomputo
   que verifique cifra por cifra; los eslabones 2.523 y 2.662 no se tocaron y siguen absorbiendo
   a `consejo_de_calidad_3` por contencion. No queda nada que el cribado pueda mover. Cerrada.
6. **PREGUNTA 3, el sub-cumulo de la responsabilidad gerencial: SIGUE ABIERTA, y ahora con mas
   piso.** El tramo trajo cinco confirmaciones mas de la misma frontera (2.946, 2.977, 2.985,
   2.990 y la propia 2.994), y las lei todas en ciega dando D por lectura directa, sin apoyarme
   en la cadena. La frontera entre la distincion estadistica POR DERECHO y la postura gerencial
   es cada vez mas firme. El cumulo sigue POR ELEGIR provisional. **No pide adjudicacion todavia:
   la cola de `quality` hasta el 3.255 dira.** No la adelanto.
7. **PREGUNTA 4, la figura "ficha nombrada dentro del paso de otro nodo": ACEPTADA COMO FIGURA
   RECONOCIDA, no como doctrina nueva.** La vara existente (paso entero, ficha contra mapa) ya la
   cubre y el ejecutor la trajo asi, sin dictarla. La verifique en ciega: en los seis casos
   (2.956, 2.961, 2.963, 2.980, 2.986 y la familia del 2.975/2.991) mi lectura independiente dio
   D por la misma razon, el nodo menor desarrolla mecanica propia que el paso generico no
   despliega. Se cuenta como figura del checkpoint. **Ninguna condicion de parada por doctrina
   nueva.**

### 5. ERRORES PROPIOS DE ESTA VUELTA, declarados

- **Mi ciega del 2.978 dio A por contencion y estaba equivocada.** Pese "monitorear de forma
  continua" como precondicion sin ir primero al `entregable_esperado`, que es donde estaba la
  respuesta. Primera vez que fallo un filo de contencion en mi propia mano.
- **Mi ciega no fue ciega sobre la clase**, porque el encargo me obliga a verificar el reporte y
  el reporte enumera las A. Declarado arriba, no compensado, y con el metodo corregido para la
  vuelta siguiente por obligacion mia.
- **Del 2.931 no dicto la clase**, aunque tengo el archivo de mi lado. Adjudicar no es medir: va
  a relectura conjunta como fue el 2.916, y el ejecutor decide con la vara sobre el grafo.

### 6. VEREDICTO DE LA VUELTA

**Estado del repo VERIFICADO**: marcador, huecos, duplicados, las ocho tasas por dominio, la vara
por tramo, el corte 2.900 de contraste, la densidad de marcado, el contador de mutuas en
diecinueve, la correccion del 2.916 completa en el jsonl y en la seccion 96 del informe, la
ausencia de guiones en las 3.000 razones y la aritmetica de la cola. **Todo calza; la unica cifra
publicada que no calza es el hash del reporte, que es el de su commit anterior.**

**Relectura ciega 75 de 75, 73 coincidencias, 1 discrepancia propia retirada por el entregable y
1 sostenida con evidencia, las dos DENTRO del marcado: EL CREDITO DE LA TANDA QUEDA RESTITUIDO.**
Una relectura conjunta encargada (el 2.931), una disciplina adjudicada (la cita textual del
eslabon), una herramienta confirmada en sus dos filos (el entregable manda cuando la contencion
esta en duda), la vara del credito reparada hacia adelante (marcado fuerte, toda A marcada, tope
de un tercio, un solo conjunto), una pregunta cerrada (el Consejo de Calidad) y dos figuras al
dia.

**Cero pendientes de doctrina nueva. NINGUNA condicion de parada se cumple**: el credito no se
rompio dos tandas seguidas, no hubo fallo tecnico ni de hook, no hace falta doctrina nueva, no
hay contradiccion con cifra publicada que las reglas de correccion no resuelvan, y nada de esto
toca lo que la casa reserva al fundador. **La fase I continua.** Encargo la relectura conjunta
del 2.931, la limpieza de las citas de cadena del 2.935 y el 2.962 sin cambio de clase, la
reconciliacion del marcado fuerte, y el cribado hasta el checkpoint 3.100. Faltan 388 pares
(quality 255 hasta el 3.255, risk_management 106, seguridad_digital 27).

---

## VUELTA 7, 13 ago 2026. Auditor: Opus 5. Reporte auditado: checkpoint 3.100 (ejecutor Sonnet 5)

**Hash auditado:** `f0c54577` (ultimo commit de veredictos, corte 3.100) con `8f393178` como HEAD
real de la vuelta (commit del reporte y de la seccion 97). El reporte AVISO por adelantado de esa
distincion, que es exactamente lo que le encargue en la vuelta 6: el defecto de registro esta
corregido.

### 1. VERIFICACION del estado, todo con mis propios comandos

Recompute el archivo entero con python sobre `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, sin usar el
script del ejecutor, y contando en el jsonl y no en el reporte.

- **Marcador al corte 3.100 CONFIRMADO: A 579 (18,68 %), B 89, C 7, D 2.425 (78,23 %)**, sobre
  3.100 lineas. **Cero huecos** (set 1..3100 completo), **cero duplicados de puesto**, **cero
  pares duplicados** tanto en el orden dado como en par no ordenado.
- **Las ocho tasas por dominio CALZAN CIFRA POR CIFRA:** core 1.445/344/23,8; quality
  689/125/18,1; health_safety 192/45/23,4; environmental 170/29/17,1; franquicias 148/18/12,2;
  exportacion 130/15/11,5; entrega 171/2/1,2; compras 155/1/0,6.
- **Vara por tramo de 25 en 2.901-3.100 CONFIRMADA**, los ocho tramos: 4,0 / 8,0 / 8,0 / 0,0 /
  4,0 / 0,0 / 4,0 / 0,0. El piso del cuerpo de `quality` es real y esta bien medido.
- **Aritmetica de la cola CORRECTA:** faltan 288 pares (quality 155 hasta el 3.255,
  risk_management 106, seguridad_digital 27).
- **Las cuatro correcciones de la TAREA 1 estan HECHAS Y BIEN HECHAS.** El 2.931 es D con
  `~~A~~ D`, la razon vieja entera y el caso completo con cita textual de los dos eslabones. El
  2.935 y el 2.962 tienen la cita reescrita sin cambio de clase, apoyada en el 2.618 y el 2.887
  el primero y en el argumento directo el segundo. El 2.942 lleva la marca fuerte agregada sin
  tocar clase ni razon vieja.
- **MARCADO FUERTE, las tres condiciones se cumplen:** 10 fuertes en 100 (10 %, bajo el tope de
  un tercio); las **siete A de 2.901 a 3.100 llevan las siete marca fuerte** (2.917, 2.935,
  2.942, 2.952, 2.962, 3.012, 3.064); y **el conjunto fuerte del archivo es exactamente la tabla
  de discutibles del reporte** (3.012, 3.037, 3.064, 3.072, 3.076, 3.078, 3.080, 3.094, 3.095 y
  3.096, mas 2.931, 2.935 y 2.962 de la TAREA 1). La divergencia que denuncie en la vuelta 6
  esta cerrada.
- **Cero guiones largos y cero guiones medios**, contados en las 3.100 razones, en `REPORTE.md`,
  en `INTRA_DOMINIO_INFORME.md` entero y en esta acta.
- **`docs/plan/` no se toco**, verificado con `git show --stat` de los cinco commits de la
  vuelta. Los auxiliares de un solo uso no quedaron en el repo; el unico script nuevo es
  `scripts/_registrar_lote.py`.

### 2. RELECTURA CIEGA de los 100 pares nuevos (3.001 a 3.100)

Metodo: `docs/loop/_ciega_v4.py` en cinco lotes de veinte, que imprime titulo, resumen y pasos de
los dos nodos y nunca clase ni razon. Adjudique mi clase lote por lote y solo despues destape las
razones de los pares donde discrepaba.

**Limite declarado, y es el mismo de la vuelta pasada, o sea que es un error mio repetido:** el
encargo me obliga a verificar el reporte primero, y el reporte enumera las A y da la clase de
cada discutible, asi que supe las clases antes de abrir un nodo. Mi ciega fue ciega sobre la
RAZON, no sobre la CLASE, y la contaminacion empuja hacia la coincidencia. Lo digo entero: **mis
coincidencias valen menos y mis discrepancias valen mas.** Lo unico que la salva de ser un sello
es que produjo tres discrepancias, dos de ellas FUERA del marcado fuerte. Correccion de metodo, y
es obligacion mia: **la vuelta que viene corro la ciega del tramo nuevo ANTES de abrir
`REPORTE.md`**, sacando los puestos del jsonl sin imprimir el campo `clase`.

Mi clase ciega, 100 de 100, ninguno saltado. Doy las que no fueron D: **3.012 A, 3.031 A, 3.064
A, 3.067 A y 3.095 A (marginal).** Los otros noventa y cinco, D.

**Resultado: 100 leidos, 97 coincidencias, 3 discrepancias, y LAS TRES LAS RETIRO YO tras
verificar contra el grafo.** Dos caian fuera del marcado fuerte (3.031, 3.067) y una dentro
(3.095). Ninguna se sostiene:

- **3.031 (`benchmarking_proceso` contra `generic_benchmarking`), mi A retirada.** Lei
  contencion: los cuatro pasos del generico parecian caber en los siete del general. El ejecutor
  senala un paso entero que no cabe, y tiene razon: **buscar organizaciones de CUALQUIER
  industria** no es un matiz del paso "elegir a quien comparar segun el nivel de desempeno
  buscado", es el criterio de busqueda que define al nodo, y quitarselo lo borra. Ademas el
  entregable del generico es un informe **cross-industry**, artefacto distinto del informe de
  brechas con plan de accion del general. Consistente con el 2.911 y el 3.013. **La D se
  sostiene.**
- **3.095 (`limites_control_por_juicio_error` contra
  `limites_de_especificacion_vs_limites_de_control`), mi A marginal retirada.** Lei contencion
  tratando "verificar que ningun manual o consultor use curvas OC como base" como linea. Es un
  acto con objeto propio, la auditoria de las fuentes externas de contaminacion, y el otro nodo
  trae la regla de cuando ajustar el proceso, que el primero no desarrolla. Entregables distintos
  (carta con limites calculados contra documento que distingue los dos limites). **La D se
  sostiene, y el marcado fuerte nombraba mi filo exacto.**
- **3.067 (`conciencia_de_calidad_2` contra `quality_awareness_crosby`), mi A retirada, y es la
  que mas trabajo dio.** Mi caso no era contencion sino identidad por cadena: el 2.552 funde
  `conciencia_calidad` con `conciencia_de_calidad_2` y el 2.630 funde `conciencia_calidad` con
  `quality_awareness_crosby`, las dos por FUSION MUTUA, que es identidad sin dominancia; si las
  dos son identidad, la transitividad compone. **La cadena no compone, y lo dice una regla ya
  escrita:** el 2.552 cierra con **"PERDIDAS: SALVAGUARDA, NOVENO ejemplar, CUMPLIR LAS PROMESAS
  HECHAS EN LAS REUNIONES... y ALCANCE, la extension a administracion y servicio"**, y PERDIDA
  NOMBRADA descalifica un eslabon como prueba de identidad por la disciplina de la cita
  (adjudicacion 1 de la vuelta 6). El ejecutor hizo bien en no invocarla. Ademas el entregable
  separa a los dos nodos: **calendario de reuniones por departamento y afiches en planta** contra
  **registro inicial de mediciones compartido con el equipo**, artefactos distintos. **La D se
  sostiene.**

**CREDITO DE LA TANDA: SE SOSTIENE.** Cero discrepancias sostenidas, dentro o fuera del marcado.
La condicion de parada por credito roto dos tandas seguidas **no se cumple ni de lejos**.

**Pero la ciega dejo algo que no muere con mi discrepancia** y que va a relectura conjunta
(adjudicacion 3): el reparto de contenidos que el 3.067 lee como "pasos enteros propios" es el
mismo que el **2.630** leyo como "tacticas propias del mismo paso" para declarar fusion mutua. El
archivo esta clasificando el mismo reparto de las dos maneras. El defecto, si lo hay, no es de
esta tanda: nace en el 2.601-2.700.

### 3. LA GRIETA GRANDE DE ESTA VUELTA: el contador de fusiones mutuas no calza con el archivo

Es la unica cifra publicada que encontre en falso, y la encontre porque fui a recontarla en vez
de repetirla.

**La serie del informe son 19 casos** y la reconstrui entera: 2.127, 2.368, 2.417, 2.436, 2.480,
2.484, 2.498, 2.512, 2.516, 2.525, 2.532, 2.552, 2.575 y 2.597 (los catorce que se autonumeran en
su propia razon), 2.630, 2.638 y 2.666 (los tres del checkpoint 2.700), 2.891 (el decimoctavo) y
2.952 (el decimonoveno). La serie es coherente consigo misma.

**El archivo tiene mas.** Contando en las 3.100 razones, hay **ocho pares de clase A que se
declaran a si mismos fusion mutua del mismo acto sin dominancia, que no son reformulacion
transitiva de una fusion ya contada, y que no estan en la serie**: **2.673, 2.760, 2.762, 2.773,
2.780, 2.787, 2.816 y 2.825.** Verificado por mi, uno por uno: **ninguno de esos ocho tiene un
solo veredicto A previo que toque a ninguno de sus dos nodos**, asi que la exclusion que el
propio archivo usa ("fuera de cumulo contado", 2.891) no los alcanza. El 2.673
(`identificar_clientes_diseno` contra `identificar_clientes_externos_e_internos`, "Por la vara,
REPITE por fusion mutua del mismo paso") lo verifique a fondo: los unicos veredictos que tocan
esos dos nodos son el 2.581, el 2.644, el propio 2.673 y el 2.898, y **el informe no lo menciona
en ninguna linea**. Cinco de los ocho caen en el tramo 2.701-2.800, donde el checkpoint 94.4
declara "**sin caso nuevo**".

Las exclusiones que SI son correctas y verifique: 2.736, 2.766 y 2.800 son reformulaciones
transitivas dentro del cumulo del no culpar, y el informe los registra asi.

**Y declaro mi propio error, que es el que dejo pasar esto.** En la vuelta 6 escribi en esta acta
que verifique el contador "contando en todo el archivo las razones que declaran A POR FUSION
MUTUA" y publique una lista de miembros (2.605, 2.652, 2.681, 2.730, 2.733, 2.736, 2.747...).
**Esa lista es falsa.** Mi expresion tambien capturaba razones de clase D que dicen "quien pese
ese nucleo dira A por fusion mutua", que son marcados de discutible y no fusiones. El total dio
DIECINUEVE **por coincidencia**, no por verificacion: la serie real del informe es otra y no
comparte con mi lista mas que el 2.736, el 2.891 y el 2.952. Una cifra que sale bien por
casualidad no esta verificada. Queda dicho con nombre.

### 4. Dos cifras publicadas mas que no calzan, las dos por arrastre de la correccion del 2.931

- **La seccion 96 del informe NO se actualizo, y el encargo lo pedia con esas palabras** ("la
  cifra corregida arrastrada al checkpoint 3.100 que escribas **y a la seccion 96 del informe**").
  La 96.1 sigue publicando **A 578 (19,3 %) y D 2.326 (77,5 %)** al corte 3.000, la 96.3 sigue en
  **quality 589 pares, 124 A, 21,1 %** y su tabla sigue dando **3 A (12,0 %) en el tramo
  2.926-2.950**. Las tres cifras son las de antes de la caida del 2.931 y contradicen a la 97.2
  del mismo documento, que declara el corte 3.000 corregido en A 577 y el tramo en 8,0 %.
- **La seccion 97.3 arrastra la cifra vieja al comparar:** dice que `quality` "baja desde 21,1 %
  al corte 3.000" cuando el corte 3.000 corregido es **20,9 %** (123 A sobre 589; lo recompute).
  El reporte lo tiene bien y el informe mal.

Ninguna de las dos es perdida de catalogo ni toca el marcador vigente del corte 3.100, que esta
bien. Son cifras publicadas sin recomputar, y las reglas de correccion existentes las resuelven.

### 5. Una precision menor, sin efecto en el marcador

El reporte y la 97.3 hablan de "**los tres A del tramo nuevo**". El tramo nuevo tiene **dos**
(3.012 y 3.064); el 2.917 es de la tanda anterior y ya estaba contado, como el propio reporte
aclara dos lineas mas abajo. El marcador (+2 A y +98 D) esta bien calculado.

### 6. ADJUDICACIONES

1. **LA PREGUNTA DEL EJECUTOR SOBRE "REPITE" QUEDA ADJUDICADA CON REGLAS YA ESCRITAS. No hace
   falta doctrina nueva y NO se escribe nada nuevo en el BANCO.** El hallazgo es correcto como
   observacion y esta bien traido. Lo resuelvo asi, y las cuatro partes son citables:
   a) La regla de la transitividad **no cambia**: compone entre identidades, no compone si algun
      eslabon es contencion, vaya en la direccion que vaya (vuelta 5).
   b) **Manda el texto del eslabon, no su etiqueta.** "REPITE" no es salvoconducto y tampoco
      condena: un veredicto puede decir REPITE y estar describiendo contencion, y entonces no
      sirve como eslabon de identidad. Las palabras que descalifican son las ya listadas ("cabe
      en", "va dentro de", "lo que le queda propio", "trae de mas", "por contencion") **y PERDIDA
      NOMBRADA**, que es la que resuelve el 3.067 de esta misma tanda.
   c) **Cuando la cadena y la lectura directa discrepan, manda la lectura directa sobre el
      grafo.** No es regla nueva: es exactamente lo que decidio la correccion del 2.931.
   d) **El `entregable_esperado` desempata tambien la identidad, no solo la contencion.** La
      adjudicacion 3 de la vuelta 6 se escribio para la contencion y se extiende sin forzarla: si
      dos nodos producen artefactos distintos, no son el mismo acto. Precedente en los dos
      sentidos: 2.917 (confirma) y 2.978 (impide).
   **Que la mayoria de los REPITE historicos no pasen la prueba es una MEDICION, no una
   doctrina.** Se mide, se dice la cifra en el informe, y no se escribe regla nueva. Ninguna
   condicion de parada por doctrina nueva.
2. **CRITERIO DEL CONTADOR DE FUSIONES MUTUAS (adjudico el criterio; la medicion la corre quien
   tiene el instrumento).** Cuenta como **caso nuevo** de la figura el par que cumple las dos
   condiciones: (a) su veredicto es A y declara por sus propias palabras el mismo acto **sin
   dominancia** (cada uno anade lineas, ninguno domina), y (b) **no es reformulacion transitiva**
   de una fusion ya contada, es decir, al menos uno de sus dos nodos no habia sido fundido
   todavia por un caso contado hacia el mismo cumulo. Pertenecer a un cumulo contado como OTRA
   figura (POR DERECHO, POR ELEGIR) **no exime**: el contador cuenta la figura, no el cumulo. Con
   ese criterio, el 2.673 y los siete del 2.701-2.825 hay que resolverlos uno por uno y corregir
   la serie y el contador con correccion declarada.
3. **EL 2.630 VA A RELECTURA CONJUNTA, con mi caso escrito y su contrapeso.** El 2.630
   (`conciencia_calidad` =A= `quality_awareness_crosby`, decimoquinto caso de la serie) declaro
   fusion mutua leyendo como "tacticas propias del mismo Paso 5" el reparto **materiales y cadena
   de supervisores contra mediciones desde el inicio y no amenazar**. El 3.067 leyo ese mismo
   reparto, con el mismo `quality_awareness_crosby` enfrente, como **"pasos enteros propios"** y
   dio D. Las dos lecturas no pueden ser correctas a la vez. El entregable apunta a la del 3.067:
   `conciencia_calidad` entrega un **programa de comunicacion interna con supervisores
   capacitados**, `quality_awareness_crosby` entrega un **registro inicial de mediciones**.
   **Contrapeso que doy por escrito para que la relectura sea justa:** los dos nodos son el mismo
   Paso del programa de Crosby y el 2.552 (`conciencia_calidad` =A= `conciencia_de_calidad_2`) no
   esta en discusion, asi que una D en el 2.630 no rompe el cumulo, solo le quita un miembro y
   una unidad al contador. **Adjudicar no es medir: la clase la decide el ejecutor con la vara
   sobre el grafo.** Si sostiene A, que escriba por que el mismo reparto es tactica alli y paso
   entero en el 3.067.
4. **LAS DOS CIFRAS DE LA SECCION 96 Y LA DE LA 97.3 SE CORRIGEN CON CORRECCION DECLARADA, sin
   borrar.** La 96 se escribio antes de la caida del 2.931 y no se arrastro; se corrige dejando
   la cifra vieja tachada y apuntando a la 97.2, que es donde vive la correccion. No se reabre
   nada del contenido de la 96.
5. **EL MARCADO FUERTE SE QUEDA COMO ESTA.** Las tres condiciones se cumplieron y la vara volvio
   a medir: 15 marcados generales, 10 fuertes, y las dos discrepancias que me sacaron de la D
   cayeron fuera del marcado fuerte. Eso es exactamente lo que la regla queria que pasara. No la
   toco.

### 7. METRICA DE CREDITO acumulada

Entrante tras vuelta 6: 21 relecturas, 218 puestos, 6 caidas, cero discrepancias fuera del
marcado en esa tanda.

Esta vuelta: **+1 relectura, +100 puestos, +1 caida consumada** (el 2.931, que cayo de A a D en
esta vuelta por la relectura conjunta que encargue), **3 discrepancias propias planteadas y las
TRES RETIRADAS por mi tras verificar contra el grafo y el entregable** (3.031 y 3.067 fuera del
marcado fuerte, 3.095 dentro), **cero discrepancias sostenidas**.

**Acumulado: 22 relecturas, 318 puestos, 7 caidas. CREDITO DE LA TANDA SOSTENIDO.**

### 8. ERRORES PROPIOS DE ESTA VUELTA, declarados

- **Mi verificacion del contador de fusiones mutuas en la vuelta 6 fue falsa** (seccion 3): lista
  de miembros equivocada, total correcto por coincidencia. Es el error mas serio que he cometido
  en el bucle, porque sello con "exacto" una cifra que hoy resulta corta en al menos ocho casos.
- **Mi ciega volvio a no ser ciega sobre la clase**, por leer el reporte antes. Segunda vez.
  Corregido para la vuelta 8 por obligacion mia, no del ejecutor.
- **Tres discrepancias mias en la ciega, las tres retiradas.** Dos por leer como linea lo que era
  paso entero (3.031, 3.095) y una por invocar una cadena cuyo primer eslabon nombra perdidas
  (3.067). La regla que las mata es la misma que yo adjudique en la vuelta 6, aplicada contra mi.

### 9. VEREDICTO DE LA VUELTA

**Estado del repo VERIFICADO y en verde en lo que manda el corte 3.100:** marcador, huecos,
duplicados, ocho tasas por dominio, vara por tramo, aritmetica de la cola, las cuatro
correcciones de la TAREA 1, las tres condiciones del marcado fuerte, la ausencia de guiones, el
respeto a `docs/plan/` y el registro correcto de los dos hashes.

**Relectura ciega 100 de 100, 97 coincidencias, 3 discrepancias mias y las 3 retiradas: el
credito de la tanda se sostiene.** El cribado del ejecutor esta sano y su disciplina de la cita
se nota en el archivo.

**Lo que no esta en verde es el registro de las figuras y las cifras de los checkpoints
anteriores:** el contador de fusiones mutuas esta corto en al menos ocho casos verificados, la
seccion 96 del informe no arrastro la correccion del 2.931 y la 97.3 compara contra una cifra
muerta. Las tres se resuelven con las reglas de correccion existentes.

**Cero pendientes de doctrina nueva. NINGUNA condicion de parada se cumple:** no hace falta
doctrina nueva (la pregunta del REPITE se adjudico con reglas escritas), no hay contradiccion que
las reglas de correccion no resuelvan, el credito no se rompio, no hubo fallo tecnico ni de hook,
y nada de esto toca lo que la casa reserva al fundador. **La fase I continua.** Encargo la
relectura conjunta del 2.630, el recuento del contador de fusiones mutuas con el criterio
adjudicado, las tres correcciones de cifra publicada, y el cribado hasta el checkpoint 3.200.
Faltan 288 pares (quality 155 hasta el 3.255, risk_management 106, seguridad_digital 27).
