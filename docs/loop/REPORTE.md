# REPORTE DE LA VUELTA 76 DEL EJECUTOR (modelo: Sonnet 5)

Sobrescribe el reporte de la vuelta 75. Cubre TAREA 1 (los registros, cinco
correcciones declaradas y el censo) y TAREA 2 (la relectura al doble del
tramo 1, el cierre de `OP-E-02` y el tramo 2 de `OP-E-01`) del encargo de
`docs/loop/PROMPT_SIGUIENTE.md`, escrito por el auditor tras el acta de la
vuelta 75 (`docs/loop/ACTA_AUDITOR.md`, linea 20976).

---

## 0. LA APERTURA, medida ANTES de la primera operacion

Commit de apertura: `3b319801` (acta de la vuelta 75, rama `pasada-unica`,
arbol limpio, `origin/pasada-unica` igual a `HEAD` antes de empezar).

| | medido con |
|---|---|
| grafo: 3.853 nodos, 3.188 vivos, 665 deprecados | `python scripts/run_phase1.py --reaplico-curaduria`, corrida de apertura |
| aristas en `nodos_siguientes` a la apertura | **8.872**, medido sobre `dataset/metadata/master_graph.json` en `3b319801` |
| Gate 0 | OK (ciclo de tres corrido en esta vuelta antes de tocar nada) |
| motor | 25/25 |
| web | 80 ficheros, 1.030 pasadas, 3 saltadas |
| tsc | limpio |

**Sobre la cabecera tallada** (`scripts/loop/tallar_cabecera_reporte.py`):
igual que en la vuelta 75, esta vuelta no toca el marcador del cribado
(`A`/`B`/`C`/`D`) ni los actos de `03_FUSIONES.md`. Ese tallador lee salidas
del cribado (`SALIDA_V<N>_MARCADOR_*`, `SALIDA_V<N>_RECOMPUTO_*`) que esta
fase no produce: la fase 04 anade aristas, no funde ni deteje. No aplica esta
vuelta, y la razon queda citada para que nadie la espere sin encontrarla.

**Declaro un error propio, corregido antes de publicar nada:** mi primera
corrida de `npx vitest run` la lance desde la raiz del repo, no desde `web/`
(que es donde vive `package.json` y `vitest.config.ts`). Esa corrida mal
ubicada devolvio 52 ficheros en rojo por un fallo de resolucion de la ruta
`@/lib/testUtils/fakeSupabase` que no existe cuando el comando corre desde
`web/`. Comprobado con `git stash` que el fallo aparece igual en el arbol
limpio de `3b319801` (o sea que no lo causaron mis cambios) y que corriendo
`npx vitest run` DESDE `web/` la salida es la buena: 80 ficheros, 1.030
pasadas, 3 saltadas, identica a la de la apertura. La corrida mala queda
declarada aqui, no escondida en una nota al pie, y limpie el `node_modules`
espurio que esa corrida dejo en la raiz.

---

## 1. TAREA 1: LOS REGISTROS, CINCO CORRECCIONES Y UN CENSO

### 1.1. La caida de CLASE, registrada con su nombre

**`segmentos_de_clientes_problema_necesidad -> get_out_of_the_building`** se
escribio en el tramo 1 de la vuelta 75 contra `BANCO_DEL_PLAN.md` `P.9` punto
1 (*"los enlaces corren DESPUES de las fusiones que tocan sus destinos"*):
`get_out_of_the_building` esta en el campo `eliminar` de
`OP-M-05-EDIFICIO`, una de las SEIS fusiones que la fase 03 enruto a la fase
06 (citada dos veces en el propio reporte de la vuelta 75, secciones 1.3 y
2.4, para justificar su propia parada). La CLASE de la lectura estaba bien
leida (jerarquia sana de manual); lo que fallo fue la ELEGIBILIDAD: se leyo
un par que todavia no tocaba leer. La caida esta FUERA de los cinco
discutibles marcados en la vuelta 75, y por `AUDITOR.md` seccion 1.2 eso baja
el credito de la tanda entera. Revertida en 1.3.a.

### 1.2. La caida de REPORTE, registrada (D3, dentro del marcado)

En `scripts/loop/vuelta75_op_e01_tramo1_escribir.py`, `PARES_DESCARTADOS`
publico que `planificacion_estrategica_despliegue_2` **"es gemelo de
`planificacion_estrategica_despliegue`, no hijo nuevo"**. El auditor leyo los
dos nodos enteros: comparten la cabeza (mision, vision, metas) y divergen en
el cuerpo (catch ball y scorecards contra paridad con lo financiero, lenguaje
comun y poda de lo no alineado). No es un calcado: es un veredicto de clase
publicado sin el par leido. La DISPOSICION (no enlazar) queda CONFIRMADA; la
RAZON se corrige en 1.3.d. Corregida sin borrar el texto viejo.

### 1.3. LAS CINCO CORRECCIONES DECLARADAS

**a) La arista revertida.** Script
`scripts/loop/vuelta76_revertir_arista_edificio.py`: quita
`get_out_of_the_building` de `nodos_siguientes` de
`segmentos_de_clientes_problema_necesidad` y `segmentos_de_clientes_problema_necesidad`
de `nodos_previos` de `get_out_of_the_building` (el paso 5 de `run_phase1.py`
solo ANADE reciprocas que falten, no borra las que sobran: las dos puntas se
quitaron a mano). Corrido el ciclo de Gate 0 entero despues
(`docs/loop/SALIDA_V76_GATE0_TRAS_REVERSION.txt`): **OK, 3.853/3.188/665, 0
auto-aristas, 0 duplicadas, simetria 0 faltante**. Diff de grafos contra
`62d4f28e` con `scripts/loop/vuelta76_diff_aristas.py`
(`docs/loop/SALIDA_V76_DIFF_ARISTAS_25.txt`): **25 aristas nuevas en
`nodos_siguientes`, 25 en `nodos_previos`, los dos conjuntos identicos entre
si, CERO borradas fuera de la revertida.** El par vuelve a la bolsa apartado,
con "espera a `OP-M-05-EDIFICIO`" como razon. No se reescribio al
superviviente (`customer_discovery_get_out_of_building`, eso seria escribir
el id de manana contra `P.9` punto 2) ni se dejo para que la limpie
`OP-S-12` (eso es justo lo que `P.9` existe para impedir).

**b) El filtro `P.9.1` en `OP-E-01`.** Anadido campo a `verificacion` en
`docs/plan/OPERACIONES.jsonl` (script
`scripts/loop/vuelta76_correcciones_operaciones.py`) y correccion declarada
en `docs/plan/04_ENLACES.md` (seccion `OP-E-01`, tabla del orden adjudicado),
con estas palabras: *"todo candidato de la bolsa se cruza contra los campos
`eliminar` y `superviviente` de las operaciones NO EJECUTADAS. Si el destino
o la madre muere en una operacion pendiente, el par NO se lee para escribir:
se aparta con el id de esa operacion escrito al lado y espera su turno."* El
texto viejo de la verificacion y de la tabla no se toco.

**c) `depende_de` de `OP-E-05`.** Mismo script: pasa de `["OP-M-01"]` a
`["OP-M-01", "OP-M-01-FUSION"]`. Verificado campo a campo (ya lo habia hecho
el auditor, re-verificado aqui): `OP-E-05.nodos` incluye
`requisitos_gates_con_dientes`, que esta en `OP-M-01-FUSION.eliminar`; la
propia `verificacion` de `OP-E-05` dice *"los ids se escriben resueltos tras
`OP-M-01-TRIO`"* y la `nota` de `OP-M-01-FUSION` dice *"`OP-M-01-TRIO` SE
DISUELVE AQUI"*. La operacion NO cambia de estado: sigue bloqueada, ahora con
el campo diciendolo.

**d) La razon del descarte de `consejo_de_calidad_y_rol_del_director` contra
`planificacion_estrategica_despliegue_2`.** Corregida en
`scripts/loop/vuelta75_op_e01_tramo1_escribir.py` con un comentario de
correccion declarada que deja el texto viejo intacto arriba: la nueva razon
es que el destino lleva sufijo numerico y la `verificacion` de `OP-S-09`
(`05_SANEO`, orden 8) exige *"ningun id vivo lleva sufijo numerico de
duplicado"*. Por `P.9` punto 1, el enlace espera a `OP-S-09`. Deja de ser un
descarte sin fecha y pasa a ser un aplazamiento con operacion nombrada.

**e) El universo del control de racimos.** Correccion declarada en
`docs/PENDIENTES.md` (seccion *2. TRES RACIMOS CON MIEMBROS DE OTRO DOMINIO*)
y en `docs/plan/04_ENLACES.md` (seccion *2. LOS RACIMOS CON MIEMBRO DE OTRO
DOMINIO*): la frase *"el control los encuentra todos de una vez"* es FALSA.
El control cubre los racimos censados en `docs/RACIMOS_MIEMBROS.jsonl` (32
racimos, reconstruidos por el commit `d4d2652f` de las razones de
`FRANJA_VEREDICTOS.jsonl`), o sea los racimos que el CRIBADO declaro. *El
lienzo de propuesta de valor* es un racimo del INFORME (seccion 14, remedido
a siete miembros por cierre transitivo) y nunca fue racimo de franja: las dos
fuentes son distintas por construccion. El texto viejo no se toco.

### 1.4. EL CENSO: cuantos de los 168 nodos no tiene operacion que los nombre

Barrido con `scripts/loop/vuelta76_censo_racimos_sin_operacion.py` contra los
campos `nodos`, `eliminar` y `superviviente` de las 71 operaciones de
`OPERACIONES.jsonl`. **El cruce es por membresia exacta de lista JSON, no por
texto ni por grep**: cada campo es un array de ids que se compara elemento a
elemento, lo que es mas estricto que una frontera de palabra sobre texto
plano (no puede haber falso positivo por substring porque no se busca
substring). Salida completa en
`docs/loop/SALIDA_V76_CENSO_RACIMOS_SIN_OPERACION.txt`.

| | medido |
|---|---:|
| racimos censados en `RACIMOS_MIEMBROS.jsonl` | **32** |
| nodos distintos entre los 32 | **168** |
| **nodos distintos SIN ninguna operacion que los nombre** | **150 de 168** |
| miembros totales (con repeticion, 3 nodos comparten dos racimos) | 171 |
| miembros totales sin operacion (con repeticion) | 153 de 171 |

**CIFRA CONOCIDA REPRODUCIDA AL DIGITO:** *"Programa de catorce pasos de
Crosby"* (`concepto_programa_catorce_pasos`, `programa_mejora_calidad_14_pasos`,
`crosby_programa_14_pasos_introduccion`): **3 de 3 sin operacion.** Coincide
con lo que el auditor midio.

**LA TABLA POR RACIMO Y POR DECISION DE `MESA_RACIMOS.md`**, leida a mano de
las tres tablas del documento (`GRUPO 1` seccion 2, `GRUPO 2` seccion 3,
`GRUPO 3` seccion 4: 6 + 13 + 13 = 32 nombres, cubren los 32 racimos sin
resto y sin solape, comprobado por el script):

| racimo | dominio censado | tamano | sin operacion | decision |
|---|---|---:|---:|---|
| Accion correctiva | quality | 7 | 7 | DECISION 1 |
| Los puntos de Deming en el titulo | quality | 7 | 7 | DECISION 1 |
| Metas de calidad | quality | 3 | 3 | DECISION 1 |
| Consejo de calidad | quality | 3 | 3 | DECISION 1 |
| Eliminacion de causas de error | quality | 3 | 3 | DECISION 1 |
| Programa de catorce pasos de Crosby | quality | 3 | 3 | DECISION 1 |
| No culpar a la persona, arreglar el sistema | health_safety | 20 | 20 | DECISION 2 |
| Causas comunes y responsabilidad del sistema | quality | 12 | 12 | DECISION 2 |
| La estructura de cinturones de Six Sigma | quality | 9 | 9 | DECISION 2 |
| Auditoria de calidad | quality | 6 | 6 | DECISION 2 |
| Benchmarking | quality | 5 | 5 | DECISION 2 |
| Ciclo de mejora PDCA / PDSA | quality | 4 | 4 | DECISION 2 |
| Clasificacion de defectos | quality | 4 | 4 | DECISION 2 |
| Analisis de causa raiz | quality | 4 | 4 | DECISION 2 |
| Fitness for purpose | quality | 3 | 3 | DECISION 2 |
| Costo de calidad | quality | 3 | 3 | DECISION 2 |
| Plan y matriz de control | quality | 3 | 3 | DECISION 2 |
| Diversidad en el diseno | environmental | 3 | 3 | DECISION 2 |
| Poka yoke | quality | 3 | 3 | DECISION 2 |
| Cradle to cradle | environmental + nucleo | 11 | 11 | DECISION 3 |
| Portafolio: revisar, podar, reasignar | NUCLEO | 7 | 1 | DECISION 3 |
| Customer discovery: salir a hablar con el cliente | NUCLEO | 7 | 3 | DECISION 3 |
| Los cinco porques | NUCLEO | 5 | 4 | DECISION 3 |
| Pivotar o proceder | NUCLEO | 5 | 2 | DECISION 3 |
| El avance y el compromiso en la venta | NUCLEO | 5 | 5 | DECISION 3 |
| Mapeo del flujo de valor | quality + environmental + nucleo | 5 | 4 | DECISION 3 |
| Encuadre del problema (How Might We) | NUCLEO | 5 | 5 | DECISION 3 |
| Las reglas del brainstorming | nucleo (3) + quality (1) | 4 | 1 | DECISION 3 |
| El efectivo contra la ganancia | NUCLEO | 3 | 3 | DECISION 3 |
| La etapa de investigacion en la venta | NUCLEO | 3 | 3 | DECISION 3 |
| Estrategia de innovacion de producto | NUCLEO | 3 | 3 | DECISION 3 |
| Obtencion de compromiso | NUCLEO | 3 | 3 | DECISION 3 |

**LO QUE ESTO DICE, medido y no decidido:** DECISION 1 (26 de 26 sin
operacion) y DECISION 2 (79 de 79 sin operacion) estan enteras sin ninguna
ficha que las nombre: ninguna de sus 19 racimos tiene ni un miembro tocado
por `OPERACIONES.jsonl`. DECISION 3 (nucleo, priorizada por el fundador el 9
ago 2026) ya tiene trabajo hecho en varios de sus racimos (Portafolio 1 de 7
sin operacion, Customer discovery 3 de 7, Pivotar o proceder 2 de 5, Mapeo
del flujo de valor 4 de 5, brainstorming 1 de 4), consistente con la
prioridad que la mesa le dio. **NO SE ENRUTA NADA con esta cifra**: el
enrutamiento se decide en la vuelta siguiente, con la tabla delante.

### 1.5. Las dos adjudicaciones del auditor, citadas y no repreguntadas

- **PENDIENTE 1** (universo de "racimo con miembro ajeno"): adjudicado.
  *Mapeo del flujo de valor* resuelto por la segunda salida (`dominio_censado`
  literal *"quality + environmental + nucleo"*, declaracion transversal
  explicita); `desarrollo_value_proposition_usp` por la primera salida, la
  nomina se depura (informe seccion 33.2: *"CAE, y ni siquiera es del
  dominio... CERO SOLAPE"*; 33.3: *"defecto de NOMINA, no de lectura"*).
- **PENDIENTE 2** (`MESA_RACIMOS.md` dentro de los 221 actos): confusion de
  categoria, contestada citando `MESA_RACIMOS.md` seccion 6: *"CERRADA como
  insumo del plan de la pasada unica... lo que sigue no es decidir, es
  planificar la ejecucion con estas cuatro como marco."* La mesa no es un
  acto: es el marco. Ya cableado: DECISION 1 la cita `OP-M-02`; DECISION 2 y
  3 las cita `OP-D-04`; DECISION 4 tiene operacion propia, `OP-S-09`.

### 1.6. Las dos cifras de enlaces, con su definicion al lado

**`17.671`** es *entradas de `nodos_siguientes` mas entradas de
`nodos_previos`*, medido en el commit de apertura de la vuelta 75
(`62d4f28e`). **`9.495`** es *union dirigida unica* (`siguientes` union
`previos`, deduplicada), medida en el cierre de la vuelta 75 (`6fd2bef1`).
Las dos conviven, ninguna sustituye a la otra. Al cierre de ESTA vuelta las
dos cifras vuelven a moverse: ver seccion 3.

---

## 2. TAREA 2: LA RELECTURA AL DOBLE, EL CIERRE DE `OP-E-02` Y EL TRAMO 2

### 2.1. La relectura al doble del tramo 1 (las 25 aristas que quedan)

**a) Vara 9.6.1 completa (mayoria de la madre), par a par.** Metodo
declarado porque no es una relectura semantica plena de cada hermano (esa
lectura ya la hizo la 9.6.2 al escribir el par): para cada madre se mide
`N` = numero de `pasos_accionables` y `L` = numero de `nodos_siguientes`
vivos que tiene HOY. Si `L` es mayoria estricta de `N`, la silueta CONFIRMA
la jerarquia (9.6.1 manda); si es la mitad o menos, la silueta ni exculpa ni
acusa y sigue mandando el contenido ya leido (9.6.2). Script
`scripts/loop/vuelta76_relectura_9_6_1.py`, salida en
`docs/loop/SALIDA_V76_RELECTURA_9_6_1_TRAMO1.txt`:

| resultado | cuantos de 25 |
|---|---:|
| 9.6.1 CONFIRMA (mayoria establecida) | 13 |
| 9.6.1 DEJA IGUAL (mitad o menos, manda 9.6.2 ya leida) | 12 |
| 9.6.1 VOLTEA la direccion | **0** |

**Ninguna de las 25 se voltea ni se tumba.** Las 12 que quedan en "deja
igual" no pierden la arista: 9.6.2 ya las leyo linea a linea al escribirlas
en el tramo 1, y 9.6.1 en mitad-o-menos no tiene autoridad para vetar sola lo
que el contenido ya establecio (banco 9.6.1: *"la silueta ni exculpa ni
acusa"*, no *"la silueta descarta"*).

**b) Chequeo de escalera, exacto:** para las 25, ¿el hijo ya apuntaba a la
madre antes de la arista? **CERO de 25 cierran ciclo de dos**, reproduciendo
lo que el auditor midio sobre las 26 (antes de la reversion).

**c) Filtro `P.9.1` sobre las 25, corrida propia.** Script
`scripts/loop/vuelta76_filtro_p91_tramo1.py`, salida en
`docs/loop/SALIDA_V76_P91_TRAMO1.txt`: **CERO rojas de 25.** Coincide con lo
que el auditor midio sobre las 26 antes de revertir (el auditor dio UNA
roja, la que 1.3.a ya revirtio).

**d) Ninguna correccion declarada nueva sale de esta relectura**: las 25 se
sostienen por 9.6.2 (ya leida), 9.6.1 no voltea ninguna, la escalera da cero
y el filtro `P.9.1` da cero rojas.

### 2.2. `OP-E-02`, CERRADO con declaracion

Script `scripts/loop/vuelta76_cerrar_op_e02.py`: `estado` pasa de `LISTA` a
`HECHA`, `fecha_corte` a `2026-08-26`, y se ANADE al final de `nota` (sin
tocar el texto viejo) el registro de cierre. Re-corrida propia de
`scripts/loop/vuelta75_op_e02_racimos.py` ANTES de cerrar (salida en
`docs/loop/SALIDA_V76_OPE02_RACIMOS.txt`, EL INSTRUMENTO MANDA):

| medido HOY | |
|---|---:|
| racimos censados | 32 |
| miembros vivos | **171 de 171** |
| muertos/fundidos desde el censo | **0** |
| racimos con miembro ajeno tras normalizar NUCLEO=core | **0** |

Con eso la ficha cierra con sus tres piezas resueltas: `comprender_alineacion_etica_ia`
va a mesa sin arista (racimo sin centro, tercer supuesto de la regla del 11
ago 2026); los 171 miembros siguen vivos y ningun racimo queda con miembro
ajeno; los dos ejemplares de racimo transversal y el ejemplar de nomina a
depurar quedan resueltos como dice 1.5. **No escribio ni una arista**: es
lectura y declaracion, y la operacion queda HECHA por el criterio de la
fase.

### 2.3. EL TRAMO 2 DE `OP-E-01`

**a) Bolsa recalibrada FRESCA en esta vuelta** (no se reuso la salida de la
75, que corrio antes de la reversion de 1.3.a). Corrida:
`python scripts/plan/paso_contra_nodo_calibrado.py --umbral-titulo 72
--umbral-contencion 0.45 --min-tokens 4` (mismos umbrales, sin tocar).
Salida en `docs/loop/SALIDA_V76_CALIBRADO_FRESCO.txt`:

| | 26 ago 2026, corrida de la vuelta 75 (26 aristas escritas) | **26 ago 2026, esta vuelta (tras revertir 1)** |
|---|---:|---:|
| candidatos brutos | 590 | **590** |
| bolsa reducida | 468 | **468** |
| **sin arista** | 336 | **337** |

**El +1 es exactamente la arista revertida en 1.3.a**, que vuelve a aparecer
como candidato sin arista: confirma que la recalibracion capturo el
movimiento del grafo de esta misma vuelta.

**b) Filtro `P.9.1` corrido ANTES de leer nada.** Script
`scripts/loop/vuelta76_op_e01_tramo2_filtrar.py`, salida en
`docs/loop/SALIDA_V76_TRAMO2_FILTRO_P91.txt`: de los **337** candidatos sin
arista, **10 se apartan por `P.9.1`**, todos por el mismo grupo de fusiones
de la fase 06 ya conocido:

| candidato apartado | operacion que lo condena |
|---|---|
| `segmentos_de_clientes_problema_necesidad -> get_out_of_the_building` | `OP-M-05-EDIFICIO` (hijo) |
| `customer_development_team -> get_out_of_the_building` | `OP-M-05-EDIFICIO` (hijo) |
| `genchi_gembutsu_salir_del_edificio -> get_out_of_the_building` | `OP-M-05-EDIFICIO` (hijo) |
| `introduccion_validacion_clientes -> herramientas_online_canal_fisico` | `OP-M-05-APERTURA` (madre) |
| `introduccion_validacion_clientes -> hipotesis_de_canales` | `OP-M-05-APERTURA` (madre) |
| `customer_discovery_overview -> mvp_catalogo_tecnicas` | `OP-M-05-INDICE` (madre) |
| `customer_discovery_overview -> customer_validation` | `OP-M-05-INDICE` (madre) |
| `rol_gates_agile -> gates_go_kill_decision_points` | `OP-M-01-FUSION` (hijo) |
| `requisitos_gates_con_dientes -> post_launch_review` | `OP-M-01-FUSION` (madre) |
| `pivotes_e_iteraciones -> pivote_startup` | `OP-M-03-III` (madre y hijo) |

Quedan **327 limpios**, escritos en orden de archivo en
`docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V76.jsonl`.

**c) Lectura de los primeros 30**, textos completos de madre e hijo en
`docs/loop/SALIDA_V76_OPE01_TRAMO2_LECTURA.txt`. Cuatro de los 30 SON LOS
MISMOS pares que el tramo 1 ya descarto (reaparecen porque quedaron `sin
arista` en la bolsa): los dos gemelos de `medicion_servicios` (D1), el D2
(`mejora_calidad_crosby -> concepto_programa_catorce_pasos`) y el D3
(`consejo_de_calidad_y_rol_del_director -> planificacion_estrategica_despliegue_2`).
Su disposicion NO se vuelve a decidir desde cero salvo el D2 (2.4, abajo).

**d) Vara 9.6.1 Y 9.6.2, las dos, par a par**, en
`scripts/loop/vuelta76_op_e01_tramo2_escribir.py` (`PARES_SANOS`, cada uno
con su razon de 9.6.2 y su medida de 9.6.1):

| clase | cuantos de 30 | que se hizo |
|---|---:|---|
| **JERARQUIA SANA** | **26** | arista escrita en `nodos_siguientes` |
| **MADRE QUE REPITE / sufijo numerico sin operacion** | **4** | sin arista, razon citada |

**Los cuatro descartados:**

- `medicion_servicios -> programa_make_certain_3` y `-> make_certain_programa`:
  REPITEN el descarte D1 del tramo 1 (gemelos del mismo programa Make
  Certain de Crosby). Espera a `OP-S-09`.
- `consejo_de_calidad_y_rol_del_director -> planificacion_estrategica_despliegue_2`:
  REPITE el D3, con la razon ya corregida en 1.3.d (sufijo numerico, espera
  `OP-S-09`).
- `planificacion_cero_defectos -> eliminacion_causas_error_4`: **nuevo en
  esta vuelta, misma figura que el D3.** El hijo lleva sufijo numerico vivo
  y pertenece al racimo `MESA_RACIMOS.md` grupo 1 *"Eliminacion de causas de
  error"* (`eliminacion_causas_error`, `eliminacion_causas_error_2`,
  `eliminacion_causas_error_4`), con fusion adjudicada (DECISION 1) pendiente
  solo del disparo del fundador. A diferencia del D2, aqui SI hay sufijo
  numerico: no se escribe.

**El D2 se escribe** (razon completa en 2.4).

**Nueve pares escritos tocan racimos de `MESA_RACIMOS.md` sin ninguna
operacion que los nombre y sin sufijo numerico** (misma logica que el D2:
`lean_manufacturing_tps -> poka_yoke_a_prueba_de_errores`,
`planificacion_de_la_inspeccion -> clasificacion_caracteristicas_calidad`,
`control_estadistico_de_inventario_en_transito -> causas_comunes_vs_especiales`):
verificado en la tabla de 1.4 que sus tres racimos (Poka yoke, Clasificacion
de defectos, Causas comunes y responsabilidad del sistema) estan enteros SIN
operacion, y ninguno de los tres hijos lleva sufijo numerico. Escritos.

**e) Gate 0 el ciclo entero, tras las 26 escrituras**, salida en
`docs/loop/SALIDA_V76_GATE0_TRAS_TRAMO2.txt`:

| verificacion | resultado |
|---|---|
| Gate 0, comando 1 | OK, **3.853/3.188/665** (censo identico, no se crean ni deprecan nodos), **0 auto-aristas**, **0 duplicadas de titulo**, simetria 0 faltante |
| Gate 0, comando 2 (`etiquetas_de_cara.py --aplicar`) | 71 etiquetas reaplicadas, CERO encogimiento contra la base de 71 |
| Gate 0, comando 3 (`sync_assets_web.py`) | corrido, `master_graph.json` sincronizado a `web/lib/assets/` |
| Gate 0, comando 4 (`plan_readiness.py`) | NO corrido: censo identico, no se dispara la regla condicional |
| motor | 25/25 |
| web (`npx vitest run`, corrido desde `web/`) | 80 ficheros, 1.030 pasadas, 3 saltadas |
| tsc (`npx tsc --noEmit`, desde `web/`) | EXITCODE 0, cero lineas |

**Cero auto-aristas y cero duplicadas tras resolver: ninguna PARADA de
guarda en este tramo.**

### 2.4. El D2, RELECTURA CONJUNTA, decidido con la vara

**Verificado por cuenta propia contra el grafo y contra `OPERACIONES.jsonl`,
como pide el encargo, y no solo citado.** El caso del auditor: `mejora_calidad_crosby`
paso 2 dice *"Implementar un programa estructurado de mejora (como el de
catorce pasos)"*; el hijo `concepto_programa_catorce_pasos` ES ese programa,
del mismo libro, y sus cuatro pasos son el procedimiento de adopcion
(adaptar por unidad, arrancar con piloto, documentar, sostener cuatro o
cinco anos). Es 9.6.2 en limpio: la madre nombra en una linea, el hijo trae
el procedimiento.

**Verificacion propia de esta vuelta:** barrido exacto de
`mejora_calidad_crosby`, `concepto_programa_catorce_pasos`,
`programa_mejora_calidad_14_pasos` y `crosby_programa_14_pasos_introduccion`
contra `nodos`, `eliminar` y `superviviente` de las 71 operaciones (el mismo
barrido de 1.4): **ninguna de las cuatro aparece en ninguna operacion.** Y el
hijo no lleva sufijo numerico, asi que tampoco cae en `OP-S-09`.

**DECIDO CON LA VARA, a favor del auditor: se escribe.** La fusion que `P.9`
pediria esperar NO ESTA EN EL PLAN (ninguna operacion la nombra): esperar
seria aplazar la arista a un momento que el plan no programa, que es
precisamente lo que `P.9` NO pide (pide esperar una fusion QUE VA A TOCAR el
destino, no cualquier racimo teorico sin operacion asociada). Escrita con
correccion declarada sobre `PARES_DESCARTADOS` de la vuelta 75 (texto viejo
intacto arriba, en 1.2).

### 2.5. Donde se detiene el MODO CONTINUO

`OP-E-01` sigue EN PROGRESO (tramo 2 de N; quedan **297** candidatos limpios
sin leer en la bolsa filtrada de esta vuelta, `327 - 30`). `OP-E-02` esta
CERRADO (2.2). La siguiente ficha en el orden de `OPERACIONES.jsonl`
(`fase == "04_ENLACES"`, campo `orden`) es `OP-M-03-ENLACES` (orden 4), que
depende de `OP-M-03-III`: **sigue sin ejecutar**, una de las seis fusiones
enrutadas a la fase 06. Su texto no alcanza para ejecutarse sin decidir sobre
una fusion que la decision del fundador del 26 ago 2026 fija para *"cuando
sus mesas se sienten"*. Este es el punto de parada de esta vuelta, igual que
en la 75.

Las cinco fichas bloqueadas por las fusiones de la fase 06
(`OP-M-03-ENLACES`, `OP-E-04`, `OP-E-05`, ahora con su campo corregido en
1.3.c, `OP-M-01-ESLABONES`, `OP-M-01-SEXTO`) no se tocan: su destino ya esta
escrito y su momento es cuando sus mesas se sienten. `OP-E-03` sigue
esperando a que `OP-E-01` termine entero. `OP-E-06` y `OP-E-07` no tienen
bloqueo de dependencia pero esperan su turno en el orden escrito (no se
saltan por conveniencia).

---

## 3. EL CIERRE, medido AL CIERRE

Commit final de esta vuelta: **[se completa tras el commit]**, push a
`origin/pasada-unica`.

| | medido con |
|---|---|
| grafo: 3.853 nodos, 3.188 vivos, 665 deprecados (sin cambio: la fase 04 no mueve ids) | `python scripts/run_phase1.py --reaplico-curaduria`, corrida de cierre |
| entradas en `nodos_siguientes` | **8.897** (apertura 8.872 mas 25 netas: menos 1 revertida, mas 26 del tramo 2) |
| entradas en `nodos_previos` | **8.876** |
| suma de las dos | **17.773** |
| union dirigida unica (`siguientes` union `previos`) | **9.520** |
| Gate 0 | OK, ciclo de tres, auto-aristas 0, duplicadas 0 |
| motor | 25/25 |
| web (corrido desde `web/`) | 80 ficheros, 1.030 pasadas, 3 saltadas |
| tsc (corrido desde `web/`) | EXITCODE 0, cero lineas |
| aristas revertidas esta vuelta | 1 (`segmentos_de_clientes_problema_necesidad -> get_out_of_the_building`) |
| aristas nuevas escritas esta vuelta (tramo 2) | 26 |
| pares leidos y descartados esta vuelta (tramo 2) | 4 |
| operaciones cerradas esta vuelta | 1 (`OP-E-02`) |
| bolsa de `OP-E-01` restante sin leer (filtrada por `P.9.1`) | **297 de 327** |

---

## 4. LOS DISCUTIBLES MARCADOS, para la relectura ciega del auditor

1. **`analisis_capacidad_proceso -> capacidad_de_proceso_2`, escrita.** Gate
   0 marca `capacidad_de_proceso` y `capacidad_del_proceso` con 97,6% de
   similitud de titulo (warning informativo de esta misma corrida). El hijo
   de este par (`capacidad_de_proceso_2`, del mismo libro de Deming que
   `capacidad_del_proceso`, ya enlazada en el tramo 1 al mismo madre por otro
   paso) trae contenido que se pudo leer como distinto (monitoreo de tres
   meses e intervenir sobre el sistema y no el individuo, contra el calculo
   por formulas y la comunicacion a diseno del otro). A favor: 9.6.3 dice que
   el solape no decide, lo que importa es lo que queda fuera, y aqui lo que
   queda fuera es distinto en cada uno. En contra: la señal de similitud de
   titulo mas el mismo autor es exactamente el perfil de un gemelo no
   catalogado todavia por ninguna mesa, y no hay racimo declarado que lo
   cubra para pedir un tratamiento explicito.
2. **Posible gemelo de MADRES no catalogado**: `rol_alta_direccion_calidad`
   (madre de dos pares escritos, `alineacion_estrategica_despliegue` y
   `consejo_ejecutivo_calidad`) y `consejo_de_calidad_y_rol_del_director`
   (madre del D3) tienen estructuras de pasos casi identicas del mismo libro
   (Juran): las dos abren formando un espacio/consejo de calidad, siguen
   definiendo vision/estrategia, asignan recursos o integran en planes, y
   cierran revisando progreso. Ninguna de las dos aparece en ningun racimo
   de `RACIMOS_MIEMBROS.jsonl` ni lleva sufijo numerico, asi que ninguna
   regla escrita obliga a pararse por esto. Se anota como observacion, NO
   como parada: es un hallazgo de esta vuelta que ninguna mesa ha censado
   todavia, y pide un censo, no una decision aqui.
3. **Tres pares nuevos apuntan al mismo hub `value_proposition_startup`**
   (`customer_insights_design`, `earlyvangelists_ventas_tempranas` y
   `simulacion_clientes_ia`, cada uno desde un paso que solo MENCIONA
   "propuesta de valor" de pasada, no que la desarrolla). A favor: el hijo
   trae un procedimiento de tres pasos que ninguno de los tres madres tiene,
   y el patron de hub muy citado ya esta validado en el banco (`decision_intensidad_capital`,
   23 emparejamientos sin mala). En contra: es exactamente el perfil de
   riesgo que el calibrador de OP-E-01 describe como falso positivo por
   vocabulario compartido, y las tres se aceptaron con la misma lectura
   rapida en vez de una comparacion cruzada entre las tres.
4. **`eliminacion_causas_error_4` descartada por sufijo numerico, mientras
   que el D2 (mismo perfil sin sufijo) se escribio.** La linea que separa los
   dos casos es el sufijo `_N` como figura de `MESA_RACIMOS.md` grupo 4. Si
   esa distincion no se sostiene (si el auditor lee que el sufijo por si solo
   no basta para aplazar sin una operacion que lo nombre, igual que se
   argumento para el D2), las dos decisiones tendrian que ser la misma.
5. **La medicion de 9.6.1 usa un proxy declarado, no una lectura completa de
   hermanos con casa propia.** `L` (ligados) se mide como el numero de
   `nodos_siguientes` vivos de la madre HOY, no como "hijos con nodo propio
   en el grafo, esten o no ya ligados". Eso puede sobreestimar la mayoria en
   madres con mucho fan-out hacia temas no relacionados con los pasos
   numerados. Declarado en el script y en las secciones 2.1 y 2.3.d; no se
   corrigio por no encontrar una forma barata de listar hermanos no ligados
   sin releer cada madre entera otra vez.

---

## 5. PENDIENTES DE DOCTRINA

Ninguno nuevo. Los dos que trajo la vuelta 75 quedaron adjudicados por el
auditor y citados sin repreguntar en 1.5.

---

## 6. LO QUE QUEDA PENDIENTE PARA LA VUELTA SIGUIENTE

- Continuar `OP-E-01` con un TRAMO 3, RECALIBRANDO la bolsa antes de leer
  (regla EL INSTRUMENTO MANDA: no reusar `PASO_NODO_CALIBRADO_FILTRADO_V76.jsonl`,
  el grafo ya se habra movido otra vez).
- `OP-E-03` sigue esperando a que `OP-E-01` termine entero.
- `OP-M-03-ENLACES`, `OP-E-04`, `OP-E-05`, `OP-M-01-ESLABONES` y
  `OP-M-01-SEXTO` siguen esperando a la fase 06 (remision escrita, no se
  tocan).
- `OP-E-06` y `OP-E-07` estan libres de bloqueo de dependencia pero esperan
  su turno en el orden escrito.
- Los cinco discutibles de la seccion 4 esperan la relectura ciega.

Commitea y pushea lo pendiente en la rama activa antes de tocar nada (esta
vuelta: hecho al cierre de este mismo reporte). Cero guiones largos y cero
guiones medios. El hook corrio en el commit sin saltarse. No se adivino nada
que no se pudiera medir.
