# REPORTE DE LA VUELTA 89 (EJECUTOR)

Rama `pasada-unica`. Fase III, EJECUCION, modo de ejecucion continua. Sobrescribe
el reporte de la vuelta 88. Apertura sellada ANTES de la primera operacion en
`docs/loop/SALIDA_V89_HEAD_APERTURA.txt`: `17a477acdd6edaeeffd2f28467cde69335d1607b`
(el acta de la vuelta 88). Cierre recomputado AL CIERRE. ESTA VUELTA SI ESCRIBIO:
la TAREA 2 revirtio la arista del par 117, y es la UNICA escritura de dataset de
la vuelta (TAREA 3 y TAREA 4 son medicion pura, cero aristas).

## CABECERA TALLADA (--fase04 --vuelta 89), pegada entera

Comando: `python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 89`
Salida completa en `docs/loop/_v89_cabecera_tallada.txt`, EXIT 0. Antes del commit
de cierre, `--comparar docs/loop/REPORTE.md` se corre otra vez sobre este mismo
fichero ya escrito (seccion de cierre del reporte, mas abajo).

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.188 / 665 | **3.853 / 3.188 / 665** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 8.996 / 8.975 / 17.971 / 9.619 | **8.995 / 8.974 / 17.969 / 9.618** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **-1 / -1 / -2 / -1** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 2 fila(s): `juran_rcca_metodo -> diseno_implementacion_remedio`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **1 fila(s): `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `17a477ac` (ACTA DE LA VUELTA 88 DEL AUDITOR, leido de git log), HEAD real de apertura `17a477ac` (sellado por el ejecutor antes de la 1.a operacion), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, commit del acta `17a477ac` (ACTA DE LA VUELTA 88 DEL AUDITOR, leido de git log), HEAD real de apertura `17a477ac` (sellado por el ejecutor antes de la 1.a operacion), arboles de `dataset/` IGUALES: VERDE** |

**LA UNICA CELDA QUE CAMBIA (fuera de la fila derivada "aristas movidas") ES LA
DE ARISTAS Y LA DEL DESFASE, Y ES LA CORRECCION, NO UNA DISCREPANCIA**, tal como el
encargo la predijo al digito: `-1 / -1 / -2 / -1` en las cuatro cifras de aristas
(8.996/8.995, 8.975/8.974, 17.971/17.969, 9.619/9.618, correspondiendo a UNA arista
quitada de las DOS vistas) y el desfase bajando de 2 filas a 1 (la fila del par
117 tenia `arista guardada=False | arista real hoy=True` y, al revertir, deja de
discrepar: la unica fila que queda es `ganar_comprension_del_cliente ->
dia_en_la_vida_del_cliente`, sin relacion con esta vuelta). **Mi corrida NO
discrepo en ningun digito contra lo que el encargo predijo**, asi que no hay
discrepancia que declarar en esta celda.

El sha256 del `master_graph.json` **cambia** (correctamente, porque la vuelta si
escribio): de `6ea239641964f43a76d179721f6e5fc40b0422bf5e1ea3785fd2ee3987f2cd9f`
(apertura, identico al cierre de la vuelta 88) a `1671895b2a6c...` (cierre de esta
vuelta, verificado identico en el commit de la TAREA 2 y en el arbol de trabajo al
medir el cierre: la vuelta no toco `dataset/` despues de la TAREA 2).

El ciclo de tres (Gate 0, `etiquetas_de_cara.py --aplicar`, `sync_assets_web.py`)
se corrio completo tres veces (apertura, tras la reversion de la TAREA 2, y
cierre), las tres veces detras de `run_phase1.py --reaplico-curaduria` corrido
SOLO primero (que revierte las 71 etiquetas, adjudicacion 5.6 del acta 88: "no se
corre solo, nunca"), verificado con `git status --porcelain -- dataset/
web/lib/assets/` en CERO despues del ciclo completo las tres veces. **NO CAI EN EL
ERROR DE MANEJO DE LA VUELTA 88** (correr `--reaplico-curaduria` solo y dejarlo
ahi): las tres veces complete el ciclo antes de seguir. Esta vez el paso
intermedio (`GATE0_CMD1` solo, con `master_graph.json` modificado) SI se sello
como fichero de la cabecera (`SALIDA_V89_GATE0_CMD1_APERTURA.txt` y
`..._CIERRE.txt`), porque es la salida que el tallador de la cabecera exige leer:
esa salida es del PRIMER comando del ciclo, no del ciclo completo, y el estado
que cuenta (`git status` en cero) es el de DESPUES de los tres comandos, medido
aparte y citado arriba.

---

## TAREA 1: LOS REGISTROS DEL ACTA 88, SIN REMEDIR

### 1.1. La caida de REPORTE de la vuelta 88 (vive SOLO en REPORTE.md, no mueve dato)

Medida por el auditor, acta de la vuelta 88, seccion 3. Se registra aqui por su
nombre, sin volver a medirla: **"los 36 pares que tocan un nodo deprecado NO se
quitan de la bolsa re-basada" es falso: son 17 de 129, no 36.** Los otros 19 ya
se habian caido por el frente 4 (arista ya escrita, alias canonico) o por el
filtro de direccion. La intencion del discutible 5.b del reporte de la vuelta 88
era cierta (no se aplico un quinto frente por deprecados); la frase no lo era.

**Racha de REPORTE: pasa a DOS SEGUIDAS (la 87 y la 88). La parada pide TRES.**

### 1.2. La caida de EXPEDIENTE de la vuelta 88 (docs/plan/, sin correr el BFS)

Medida por el auditor, acta de la vuelta 88, seccion 2.3. **"91: dos nodos, los
dos pasos", escrito en `docs/plan/04_ENLACES.md` linea 601 y en el campo `nota`
de `OP-E-01`, es incorrecto: el BFS de hoy da TRES intermedios**
(`validacion_sistema_medicion`, el paso 5 de la madre;
`autocontrol_y_controlabilidad`, el paso 6 de la madre; y
`autocontrol_planificacion_servicio`, que el acta 85 no nombra). **No suma a
ninguna racha por si sola**: es el mismo razonamiento de la clase del par 117 y
ya esta contado ahi (seccion 2.5 del acta 88). Se corrige en los DOS sitios donde
vive, en la TAREA 2 de esta vuelta (2.e mas abajo), sin borrar el texto del 28
ago.

### 1.3. Las diez adjudicaciones de la seccion 5 del acta 88, cada una por su numero

- **5.1** El par 117 se revierte, con recomputo completo y sin borrar nada.
  Ejecutada en la TAREA 2 de esta vuelta.
- **5.2** Lo que se escribe en `docs/plan/` se mide antes, y no es doctrina
  nueva: `AUDITOR.md` 1.1 y la adjudicacion 6.2 del acta 87 valen igual para una
  tabla tallada que para un precedente citado. Corregido en la TAREA 2.e (el "91:
  dos nodos" de `04_ENLACES.md` y del campo `nota`).
- **5.3** Los 36 deprecados quedan resueltos y no hace falta un quinto frente:
  con la semantica canonica de `resolverId`, los 36 resuelven a nodo vivo y CERO
  de los 192 tocan un deprecado tras resolver. P.9 los cubre. **CERRADO, no se
  reabre** (regla explicita del encargo de la 89, TAREA 4.d).
- **5.4** La guarda de `OP-C-05` no existe, el hallazgo es correcto y no es
  parada: se cumple por la via equivalente que la propia ficha de `OP-C-05`
  autoriza (correr `aristas_duplicadas_tras_resolver.py` antes y despues, sin
  crecer). Cableada en la TAREA 4 de esta vuelta.
- **5.5** La marca de discutible sigue valiendo por lo que aparta (6.7 del acta
  87, reafirmada) y no cubre lo que no nombra: las tres frases de la seccion 4.1
  cayeron fuera de los seis discutibles del ejecutor de la vuelta 88. Corregido
  en la TAREA 3 de esta vuelta (las tres salen, verificado con ROJO automatico si
  alguna no cayera).
- **5.6** El ciclo de tres se corre entero o no se corre: descriptiva, citando el
  canon de fallar ruidoso. Cumplida las tres veces en esta vuelta (ver la
  cabecera, arriba): NO se repitio el error de manejo.
- **5.7** La re-base se hace otra vez, y la direccion se lee leyendo: la lista de
  palabras (mia, del encargo de la 88) queda derogada como filtro unico.
  Ejecutada en la TAREA 3 de esta vuelta, con criterio nuevo escrito entero.
- **5.8** `OP-E-06` no abre en la vuelta 89: cumplida. Ni una arista de `OP-E-06`
  se escribio esta vuelta.
- **5.9** Los arreglos de la TAREA 3 de la vuelta 88 quedan ratificados, los
  tres: descriptiva, no exige accion de esta vuelta.
- **5.10** El sha256 del grafo se queda como vara de "cero aristas": descriptiva,
  y esta vuelta la usa al reves (el sha256 SI cambia, correctamente, porque la
  vuelta SI escribio una reversion).

### 1.4. Las cuatro caidas de procedimiento del auditor, seccion 7 del acta 88

1. **La cita del par 55**, escrita por el auditor en el acta 82 (encargo de la
   vuelta 88) cuando en realidad esta en el acta 84 (linea 26743). El ejecutor de
   la vuelta 88 la detecto y la declaro en vez de copiar.
2. **La vara del desfase mal definida** en la primera corrida del auditor: conto
   "pares de la bolsa CON arista en el grafo de hoy" (214) en vez de "campo
   `arista` guardado en la bolsa distinto del grafo" (2). Corregida leyendo el
   docstring del instrumento antes de publicar.
3. **El resolutor de alias deviante** del auditor: su primer frente 4 se detenia
   en el primer nodo vivo y dio 6; la semantica canonica de la casa (que camina
   la cadena entera) da 16, los mismos que el ejecutor de la vuelta 88 midio.
4. **La lista de palabras de direccion**, entregada por el auditor en el encargo
   de la 88 como "CRUDA, no canon": tiene el modo de fallo que motiva la TAREA 3
   de esta vuelta (premia la palabra suelta y no lee la oracion).

Las cuatro quedan en el expediente de esta vuelta por su numero, sin remedirlas:
son caidas del auditor, no del ejecutor, y el acta 88 ya las declaro con su
medicion.

---

## TAREA 2: LA REVERSION DEL PAR 117 (BLOQUEANTE, commit propio `43bafe47`)

**2.a** Arista `juran_rcca_metodo -> diseno_implementacion_remedio` quitada de
las DOS vistas: `nodos_siguientes` de `dataset/nodos/juran_rcca_metodo.json`
(de tres elementos a dos, se queda solo `definicion_problema_moms_2` y
`viaje_diagnostico_remedial`) y `nodos_previos` de
`dataset/nodos/diseno_implementacion_remedio.json` (de dos elementos a uno, se
queda solo `evaluacion_alternativas_solucion`). Nada mas se toco en esos dos
ficheros.

**2.b** Ciclo de tres corrido completo y en orden tres veces (ver cabecera):
`git status --porcelain -- dataset/ web/lib/assets/` en cero las tres veces
detras del ciclo completo. `run_phase1.py --reaplico-curaduria` se corrio solo
como primer paso de cada medicion (apertura y cierre), tal como la cabecera lo
exige, pero SIEMPRE seguido del ciclo completo antes de dar por buena la
medicion: nunca quedo a medias, nunca se commiteo a medias.

**2.c** `docs/plan/OP_E_01_DECIDIDAS.jsonl` rehorneado con
`scripts/loop/vuelta85_hornear_decididas.py` (sucesor declarado, no se toca,
descubre los tramos por patron): **220 filas, 98 ESCRITA, 122 NO SE ENLAZA**,
exactamente lo que el encargo predijo. Salida completa en
`docs/loop/SALIDA_V89_TAREA2_HORNEAR_OPE01.txt`: la fila `juran_rcca_metodo ->
diseno_implementacion_remedio` (tramo 12) sale **DEGRADADA** (`ESCRITA -> NO SE
ENLAZA`, "arista NO presente hoy en las dos vistas del grafo"), la unica
degradacion nueva de esta corrida.

**2.d** Guarda contra la bolsa V87 (`scripts/loop/vuelta83_guarda_decididas.py
--bolsa docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V87.jsonl`): **VERDE, TODA LA
BOLSA ESTA DECIDIDA**, con el indice 117 mostrando hoy `NO SE ENLAZA (tramo 12)`.
Salida completa en `docs/loop/SALIDA_V89_TAREA2_GUARDA_DECIDIDAS.txt`.

**2.e** La cifra final de `OP-E-01` reescrita en los DOS sitios donde vive, con
correccion declarada del 29 ago 2026 anadida ENCIMA del texto del 28 ago (nada
se borra):
- `docs/plan/04_ENLACES.md`, apartado `OP-E-01 CIERRE MEDIDO`: nuevo bloque
  "CORRECCION DECLARADA (29 ago 2026, vuelta 89)" con el motivo entero (no
  resumido) de la adjudicacion 5.1, la correccion del precedente del par 91 (son
  TRES intermedios, no dos, y no corrobora ninguna lectura), y la cifra vigente
  **220 / 98 ESCRITA / 122 NO SE ENLAZA**.
- El campo `nota` de `OP-E-01` en `docs/plan/OPERACIONES.jsonl`: ADDENDUM (29
  ago 2026, vuelta 89) con el mismo motivo (comprimido pero completo) y la misma
  cifra vigente, apuntando a `docs/plan/04_ENLACES.md` para el texto entero.

**2.f** La cabecera del cierre cambio, y es la correccion, no discrepancia (ver
tabla de arriba): aristas bajan a 8.995 / 8.974 / 17.969 / 9.618 (movidas -1 /
-1 / -2 / -1), el sha256 del grafo cambia, y **el desfase del calibrado de
cierre baja a 1 fila** (solo `ganar_comprension_del_cliente ->
dia_en_la_vida_del_cliente`), exactamente lo que el encargo predijo al digito.

Motor 25/25 y `tsc` en cero corridos despues de la reversion, antes de commitear
(no forman parte de la cabecera de apertura/cierre pero son la verificacion
minima de que la reversion no rompio nada). Commit propio `43bafe47`, pusheado
antes de tocar la TAREA 3.

---

## TAREA 3: LA SEGUNDA RE-BASE DE `OP-E-06`, AL DOBLE (commit `5ae40940`)

Instrumento propio, `scripts/loop/vuelta89_tarea3_rebase_ope06.py`, sucesor
declarado de `scripts/loop/vuelta88_tarea5_rebase_ope06.py` (que NO se toca).
Arranca de la bolsa de 129 de `docs/plan/OP_E_06_REBASE_V88.jsonl`, no de los
192 ni del grafo.

**3.a, el criterio nuevo** (la lista de palabras queda derogada como filtro
unico): **LA FRASE DICE QUIEN DESARROLLA A QUIEN, O NO LO DICE.** Escrito
entero en el docstring del instrumento. Una frase ENTRA cuando afirma, sobre el
par (`nodo_a`, `nodo_b`) que la fila declara, que uno de los dos elabora,
detalla, ejecuta o nombra en una linea (o pocas lineas) un contenido que el otro
trae completo (el patron mas comun de la bolsa: "`<NODO>` dice/nombra/despacha
en su paso N, EN UNA LINEA, `<contenido>`"). Una clausula "sin arista entre
ellos" o "no enlaza con ninguno" en la MISMA frase no descarta por si sola: solo
describe el estado de HOY (por eso el par es candidato), y convive con la
evidencia de contenido. Una frase NO ENTRA cuando su afirmacion nuclear es que
el par no tiene relacion de contenido entre si (aunque compartan un tercer nodo,
un padre o una vecindad comun) o cuando es un argumento metodologico sobre la
familia entera sin citar contenido propio del par ("Ninguno enlaza al otro",
"hermanos que no se conocen", "la madre no enlaza a ninguno/a de sus X", "dicen
casi lo mismo", "sin arista igual a DUPLICACION", "manda el contenido" sin
decirlo).

**3.b, las 129 frases leidas enteras, una por una** (no se muestreo, no se
delego a una expresion regular sola: la clasificacion fila por fila, con su
razon, esta escrita en el propio instrumento, `DECISIONES`, como el resultado de
esa lectura). Salida completa en `docs/loop/SALIDA_V89_TAREA3_REBASE_OPE06.txt`.
**Caen DOCE, todas nombradas con su par y su frase completa:**

| puesto | par | por que cae |
|---:|---|---|
| 455 | `customer_validation_sell_phase -> realizar_pruebas_pasa_no_pasa` | "Ninguno enlaza al otro... son hermanos que no se conocen": niega el enlace. De la caida 4.1 del acta 88. |
| 490 | `fit_problema_solucion -> product_market_fit` | "La madre enumera los tres tipos... y ninguno enlaza al otro": enumerar no es desarrollar. De la caida 4.1 del acta 88. |
| 522 | `metricas_cohortes -> retention_metrics` | "Ninguno enlaza al otro... misma vecindad de retencion": niega el enlace. De la caida 4.1 del acta 88. |
| 530 | `estrategia_de_innovacion_de_producto -> estrategia_de_innovacion_y_tecnologia` | "Lo unico que el segundo tiene es la palabra arenas": la propia frase declara que la evidencia es una palabra suelta, no contenido desarrollado. **DISCUTIBLE** |
| 581 | `cumplimiento_magnuson_moss -> prohibicion_tie_in_sales` | argumento metodologico citando el banco 9 (recomienda la arista por topologia) sin decir que nodo desarrolla contenido del otro. **DISCUTIBLE** |
| 650 | `diferenciacion_garantia_contrato_servicio -> prohibicion_tie_in_sales` | describe a los dos como hermanos bajo una madre comun, sin decir que uno desarrolle al otro. |
| 658 | `overlapping_stages_concurrent_execution -> reduccion_tiempo_de_mercado_velocidad` | figura CERO ENLAZADOS del banco, concluye "sin arista igual a DUPLICACION": no cita contenido del par. |
| 669 | `seis_herramientas_comunicacion_celebracion -> seis_medios_comunicacion_cliente` | "la madre no enlaza a ninguna de sus tres aplicaciones... huerfanos de camino": patron de familia, no del par. |
| 676 | `customer_discovery_overview -> verificar_product_market_fit` | "La madre no enlaza a ninguna de las tres": sin contenido del par. |
| 778 | `design_thinking_fundamentos -> triada_restricciones_diseno` | "cero enlazados... manda el contenido": remite al contenido sin decirlo. |
| 795 | `busqueda_cofundador_complementario -> circulos_busqueda_cofundadores` | "dos hijos que dicen casi lo mismo": sinonimia, no desarrollo. |
| 816 | `get_out_building_test_sell -> realizar_pruebas_pasa_no_pasa` | "la madre no enlaza a su hijo de paso": una linea, sin contenido. |

**Cifra nueva de la bolsa: 117 de 129** (129 - 12 = 117). Escrita a fichero
propio, `docs/plan/OP_E_06_REBASE_V89.jsonl` (117 filas). La bolsa V88 (129
filas, su propio fichero) NO se toca ni se sobrescribe: queda delante como la
primera re-base, tal como esta campaña corrige cifras.

**3.c, verificado: las TRES filas de la caida 4.1 del acta 88 (puestos 455, 490,
522) SALIERON las tres**, con un chequeo `ROJO` automatico en el propio
instrumento que habria detenido la escritura si alguna hubiera sobrevivido (no
se disparo: exit 0). El criterio nuevo NO las deja dentro: no hay hallazgo que
reportar en este punto.

**3.d, caso rojo obligatorio**, dos frases fabricadas sobre copia en memoria
(nunca tocan un fichero real):
1. Una frase que CONTIENE palabras de la lista vieja (`madre`, `cuelga`,
   `enumera`) y NIEGA el enlace ("...pero ninguno enlaza al otro: son ramas que
   no se tocan"): el filtro viejo la habria aceptado; el criterio nuevo da
   `NO_ENTRA`, como se espera.
2. Una frase SIN ninguna palabra de la lista vieja que SI dice quien desarrolla
   a quien ("...explica... con dos parrafos completos, exactamente lo mismo
   que... resume en una sola frase..."): el filtro viejo la habria rechazado; el
   criterio nuevo da `ENTRA`, como se espera.

Los dos casos se comportan como el criterio nuevo exige y como el filtro viejo
no habria dado. Salida completa en `docs/loop/SALIDA_V89_TAREA3_REBASE_OPE06.txt`
(seccion "TAREA 3.d").

**3.e** `OP_E_06_REBASE_V89.jsonl` es la cifra que la vuelta 90 usa para abrir
`OP-E-06`: **117**, no 129 ni 192.

**LOS TRES DISCUTIBLES DE ESTA TAREA, para la relectura ciega (marcados ANTES de
saber si acierto):**

1. **Puesto 530** (`estrategia_de_innovacion_de_producto ->
   estrategia_de_innovacion_y_tecnologia`), clasificado `NO_ENTRA`: mi lectura
   es que "lo unico que el segundo tiene es la palabra arenas" es una
   declaracion de evidencia DEBIL (una palabra compartida en una lista de seis),
   no un desarrollo de contenido. Una lectura contraria es defendible: "en UNA
   LINEA dentro de una lista de seis" SI seria, en otras filas de esta misma
   bolsa, el patron canonico de entrada.
2. **Puesto 581** (`cumplimiento_magnuson_moss -> prohibicion_tie_in_sales`),
   clasificado `NO_ENTRA`: mi lectura es que el argumento (citando el banco 9,
   "la madre sabe enlazar a sus hijos, la falta es omision del grafo") es
   METODOLOGICO y no cita contenido propio del par, asi que no dice quien
   desarrolla a quien. Una lectura contraria es defendible: el argumento SI
   sostiene, por inferencia, que la madre deberia enlazar al hijo, que es una
   forma de decir direccion sin usar las palabras "dice en" o "desarrolla".
3. **Puesto 932** (`cumplimiento_magnuson_moss -> mecanismo_resolucion_
   disputas`), clasificado `ENTRA`: mi lectura es que "nombra en DOS LINEAS a
   cuatro nodos hermanos" es el patron canonico de direccion (la madre nombra a
   sus hijos), aunque el fichero de origen esta truncado a 200 caracteres
   (defecto pre existente de `docs/plan/COSECHA_RAZONES_D.jsonl`, no introducido
   por esta vuelta) y no deja verificar si `mecanismo_resolucion_disputas` es
   literalmente uno de los cuatro nombrados ("el titulo, la divulgacion, la
   disponibilidad previa y la prohibicion de tie-in") o un quinto hermano no
   nombrado en ese fragmento. Lei a favor de la evidencia positiva escrita, no
   de la duda que el truncado deja abierta: es el unico de los tres discutibles
   donde la duda podria mover la fila HACIA AFUERA de la bolsa, no hacia
   adentro.

**HALLAZGO ADICIONAL, no pedido por el encargo pero medido de camino:** el
campo `frase` de `docs/plan/COSECHA_RAZONES_D.jsonl` esta truncado a **200
caracteres exactos** en varias filas (verificado: `len(frase) == 200` en las
filas que cortan a mitad de palabra, por ejemplo puestos 1134, 1149, 1995,
2023, 2082, 2106, 2038, entre otras). No es un defecto de esta vuelta ni de la
88: esta en el fichero de origen. No cambio ninguna de mis doce exclusiones (las
doce tienen su razon nuclear en la parte NO truncada de la frase), pero **queda
como PENDIENTE DE DOCTRINA** para quien relea las filas con texto cortado: si el
fundador quiere el texto completo, `COSECHA_RAZONES_D.jsonl` tendria que
regenerarse desde su fuente con el limite de caracteres ampliado o quitado. No
paro por esto: ninguna de mis doce decisiones depende del texto que falta.

---

## TAREA 4: LA VIA DE `OP-C-05`, CABLEADA Y PROBADA (commit `5ae40940`)

Instrumento propio, `scripts/loop/vuelta89_tarea4_guarda_op_c05.py`, con tres
modos.

**4.a** `--antes` y `--despues`: corren
`scripts/plan/aristas_duplicadas_tras_resolver.py` (de solo lectura, nunca
tocado) sobre `dataset/metadata/master_graph.json`, leen "entradas que SOBRAN" y
"nodos con al menos una duplicada" de su salida, y `--despues` compara contra el
sello que `--antes` dejo en `docs/loop/SALIDA_V<vuelta>_GUARDA_OPC05_ANTES.txt`:
si la cuenta CRECIO, `EXIT 1` (ROJO, "LA OPERACION PARA"); si no crecio, `EXIT
0` (VERDE). El nombre del sello lleva la vuelta, para que una vuelta no pise el
sello de otra.

Corrida hoy: `--antes` da **935 entradas que sobran, 711 nodos**
(`docs/loop/SALIDA_V89_TAREA4_GUARDA_ANTES_CORRIDA.txt`, sello en
`docs/loop/SALIDA_V89_GUARDA_OPC05_ANTES.txt`), y `--despues`, corrido
inmediatamente despues sin ninguna escritura entre medio, da **935 tambien: +0,
VERDE, EXIT 0** (`docs/loop/SALIDA_V89_TAREA4_GUARDA_DESPUES_CORRIDA.txt`): la
via funciona en el caso donde nada se escribio.

**4.b, caso rojo obligatorio**, sobre copia en memoria
(`docs/loop/SALIDA_V89_TAREA4_CASO_ROJO.txt`): `git status --porcelain --
dataset/` vacio ANTES; se carga el grafo de hoy en memoria, se fabrica una
entrada duplicada tras resolver en un nodo vivo elegido por el propio
instrumento (`ab_testing_optimizacion.nodos_siguientes` gana una segunda
entrada de `cohort_analysis_retencion`, quedando `[...] cohort_analysis_
retencion x2`); esa copia se escribe SOLO a un fichero temporal fuera del repo
(`tempfile.TemporaryDirectory`, nunca `dataset/`); el instrumento de solo
lectura corre sobre ese temporal y da **936 entradas que sobran** (935 + 1, el
duplicado fabricado); `git status --porcelain -- dataset/` vacio DESPUES. **La
cuenta fabricada (936) es mayor que la de hoy (935): exactamente la condicion
que `--despues` detecta como ROJO**, simulada y confirmada en la misma corrida.
`dataset/` nunca se toco: los dos `git status` salieron vacios.

**4.c** La cifra base de hoy, medida por el ejecutor y por el auditor al
digito: **935 entradas que sobran, en 711 nodos**. Es la linea base contra la
que la vuelta 90 mide con `--antes` propio (no reusa el sello de esta vuelta:
`--vuelta 90` escribe su propio fichero).

**4.d** El pendiente de doctrina 2 del reporte de la vuelta 88 (los 36
deprecados) sigue CERRADO por la adjudicacion 5.3: no se reabre.

---

## `OP-E-06` NO ABRE EN ESTA VUELTA (adjudicacion 5.8, cumplida)

Cero aristas de `OP-E-06` escritas. `docs/plan/OPERACIONES.jsonl` no se tocó en
el campo de `OP-E-06`. La vuelta 90 abre la operacion con la bolsa de **117**
(`docs/plan/OP_E_06_REBASE_V89.jsonl`) y la via de `OP-C-05` ya cableada
(`scripts/loop/vuelta89_tarea4_guarda_op_c05.py`).

---

## RUTAS TOCADAS ESTA VUELTA

Dataset (la unica escritura, TAREA 2):
- `dataset/nodos/juran_rcca_metodo.json`
- `dataset/nodos/diseno_implementacion_remedio.json`
- `dataset/metadata/master_graph.json` (compilado)
- `web/lib/assets/master_graph.json`, `web/lib/assets/manifest.json` (sync)

Expediente:
- `docs/plan/04_ENLACES.md` (correccion declarada 29 ago, TAREA 2.e)
- `docs/plan/OPERACIONES.jsonl` (addendum en el campo `nota` de `OP-E-01`)
- `docs/plan/OP_E_01_DECIDIDAS.jsonl` (rehorneado, 220/98/122)
- `docs/plan/OP_E_06_REBASE_V89.jsonl` (nuevo, 117 filas)

Instrumentos nuevos:
- `scripts/loop/vuelta89_tarea3_rebase_ope06.py`
- `scripts/loop/vuelta89_tarea4_guarda_op_c05.py`

Salidas de esta vuelta, todas en `docs/loop/`: `SALIDA_V89_HEAD_APERTURA.txt`,
`SALIDA_V89_GATE0_CMD1_APERTURA.txt`/`_CIERRE.txt`,
`SALIDA_V89_ETIQUETAS_APERTURA.txt`, `SALIDA_V89_SYNC_APERTURA.txt`,
`SALIDA_V89_CONTEO_APERTURA.txt`/`_CIERRE.txt`,
`SALIDA_V89_MOTOR_APERTURA.txt`/`_CIERRE.txt`,
`SALIDA_V89_WEB_APERTURA.txt`/`_CIERRE.txt`,
`SALIDA_V89_TSC_APERTURA.txt`/`_CIERRE.txt`,
`SALIDA_V89_DESFASE_CALIBRADO_APERTURA.txt`/`_CIERRE.txt`,
`SALIDA_V89_TAREA2_HORNEAR_OPE01.txt`, `SALIDA_V89_TAREA2_GUARDA_DECIDIDAS.txt`,
`SALIDA_V89_TAREA3_REBASE_OPE06.txt`,
`SALIDA_V89_TAREA4_GUARDA_ANTES_CORRIDA.txt`,
`SALIDA_V89_TAREA4_GUARDA_DESPUES_CORRIDA.txt`, `SALIDA_V89_TAREA4_CASO_ROJO.txt`,
`SALIDA_V89_GUARDA_OPC05_ANTES.txt`, `_v89_cabecera_tallada.txt`.

**Marcador del cribado, tasa por dominio, vara por tramo del cribado: NO
APLICAN a esta vuelta** (fase 04, no toca el cribado intra dominio; sin cambio
respecto de las vueltas 83 a 88). **Figuras y familias del banco: sin cambio,
no se toco doctrina.**

---

## CORRECCIONES DECLARADAS DE ESTA VUELTA (con su fecha de corte)

1. **29 ago 2026**, `docs/plan/04_ENLACES.md`, apartado `OP-E-01 CIERRE
   MEDIDO`: el par 117 pasa de `SE ESCRIBE` a `NO SE ENLAZA`; la cifra final
   pasa de 220/99/121 a 220/98/122; el precedente "91: dos nodos, los dos
   pasos" se corrige a TRES intermedios. Anadida encima del texto del 28 ago,
   que no se borra.
2. **29 ago 2026**, campo `nota` de `OP-E-01` en `docs/plan/OPERACIONES.jsonl`:
   mismo contenido, formato addendum, sin borrar el addendum del 28 ago.

---

## PENDIENTES DE DOCTRINA

1. **El truncado a 200 caracteres de `docs/plan/COSECHA_RAZONES_D.jsonl`**
   (seccion TAREA 3, hallazgo adicional): no bloqueo ninguna decision de esta
   vuelta, pero deja algunas frases de la bolsa re-basada sin su final (o su
   inicio, en las filas 2015, 2023, 2082). Si una vuelta futura necesita el
   texto completo (por ejemplo, para resolver el discutible del puesto 932 sin
   ambiguedad), el fichero tendria que regenerarse desde su fuente.

---

## REPASO DEL ENCARGO, PUNTO POR PUNTO, CON LA VERDAD

- Commitear y pushear lo pendiente antes de tocar nada: **SI**, `git status`
  daba limpio al abrir (verificado antes de sellar el HEAD).
- Sello de apertura antes de la primera operacion: **SI**,
  `SALIDA_V89_HEAD_APERTURA.txt` escrito antes de correr `run_phase1.py`.
- TAREA 1 (los cuatro registros): **SI**, seccion TAREA 1 de este reporte.
- TAREA 2 (reversion del 117, bloqueante, commit propio): **SI**, las seis
  subtareas (2.a a 2.f) completas, commit `43bafe47` pusheado antes de tocar la
  TAREA 3.
- TAREA 3 (segunda re-base de `OP-E-06`, al doble): **SI**, las 129 frases
  leidas enteras una por una, criterio nuevo escrito, las tres de (C)
  verificadas fuera, caso rojo con dos frases fabricadas, bolsa nueva a fichero
  propio (117).
- TAREA 4 (via de `OP-C-05`): **SI**, instrumento con `--antes`/`--despues`/
  `--caso-rojo`, caso rojo probado sobre copia en memoria, cifra base 935/711
  confirmada.
- `OP-E-06` no abre en esta vuelta: **SI**, cero aristas escritas de `OP-E-06`.
- Cabecera tallada con `--fase04 --vuelta 89`, pegada entera: **SI**, EXIT 0,
  cero fallos.
- Sello del HEAD de apertura dando el commit del acta 88: **SI**, `17a477ac`.
- Ningun precedente citado en `docs/plan/` sin la corrida que lo sostiene:
  **SI**: el precedente del par 91 que se corrige en la TAREA 2.e cita
  explicitamente el BFS del auditor (acta 88, seccion 2.3), no una corrida
  propia nueva (no hacia falta remedirlo: el auditor ya lo midio esta misma
  vuelta pasada y el encargo no pide repetirlo, solo corregir el texto).
- Ninguna afirmacion de composicion sin abrir el fichero y contar: **SI**, la
  cifra de la TAREA 3 (12 caen, 117 quedan) sale de contar
  `docs/plan/OP_E_06_REBASE_V89.jsonl` y las doce filas del instrumento, ambas
  citadas.
- Cero guiones largos y cero guiones medios: **SI**, verificado con `grep -P
  '[\x{2013}\x{2014}]'` sobre las LINEAS ANADIDAS de los 27 ficheros que la
  vuelta toco (no sobre el contenido preexistente de `master_graph.json`, que
  trae guiones de las fuentes de los libros desde antes de esta vuelta: 65
  ocurrencias ya en la apertura, verificado con `git show 17a477ac:...`, y CERO
  lineas anadidas por esta vuelta las traen). El hook de commit corrio las dos
  veces y paso las dos veces.

**LO UNICO QUE NO SE CORRIO FUE LO QUE EL ENCARGO EXPLICITAMENTE PROHIBIA**:
ninguna arista de `OP-E-06` se escribio.

---

## DISCUTIBLES DE ESTA VUELTA, PARA LA RELECTURA CIEGA (resumen)

Los tres de la TAREA 3 (puestos 530, 581 y 932 de la bolsa `OP-E-06`), con su
razon completa en la seccion de la TAREA 3. Ningun otro discutible: la TAREA 2
y la TAREA 4 son mediciones directas contra instrumentos que dieron
exactamente lo que el encargo predijo, sin lectura de por medio.
