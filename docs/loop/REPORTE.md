# REPORTE DE LA VUELTA 79 DEL EJECUTOR (modelo: Sonnet 5)

Sobrescribe el reporte de la vuelta 78. Cubre TAREA 1 (registros y correccion
declarada del criterio real de TAREA 3.2), TAREA 2 BLOQUEANTE (escalada
automatica del tallador a la fase 04), TAREA 3 (relectura conjunta de un
discutible y relectura al doble del tramo 4), TAREA 4 (la guarda del par no
dirigido) y TAREA 5 (el tramo 5 de `OP-E-01`) del encargo de
`docs/loop/PROMPT_SIGUIENTE.md`, escrito tras el acta de la vuelta 78
(`docs/loop/ACTA_AUDITOR.md`, desde la linea 22702).

**LA CABECERA DE ABAJO ESTA TALLADA, NO TECLEADA**, con el instrumento nuevo
de esta vuelta:

```
python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 79
```

Salida completa en `docs/loop/SALIDA_V79_TALLADOR_FASE04.txt`, pegada entera:

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.188 / 665 | **3.853 / 3.188 / 665** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 8.949 / 8.928 / 17.877 / 9.572 | **8.960 / 8.939 / 17.899 / 9.583** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |

**El marcador del cribado no aparece**: esta fase no lo toca, y el tallador
omite la fila cuando no hay `SALIDA_V79_MARCADOR_*` que citar (mecanica
explicita del modo `--fase04`, no un olvido). Sin cambio real de todos modos:
el cribado sigue en A 551, B 72, C 5, D 2.760, n 3.388, medido la ultima vez
en `docs/loop/SALIDA_V78_MARCADOR_CIERRE.txt` (contraste, no cifra nueva de
esta vuelta).

Commit de apertura: `43b02413` (acta de la vuelta 78, rama `pasada-unica`,
arbol limpio, `origin/pasada-unica` igual a `HEAD` antes de empezar la
primera tarea de codigo, verificado con `git rev-parse HEAD` y `git rev-parse
origin/pasada-unica`).

**CORRECCION DECLARADA (vuelta 80), texto viejo intacto arriba, sin
reescribirlo.** El texto de arriba esta MAL: `43b02413` es el commit de la
TAREA 4 de esta misma vuelta 79 (`git show --stat 43b02413` da los tres
ficheros de esa tarea), no la apertura. **El commit de apertura real es
`aea7cc81`** (acta de la vuelta 78 del auditor), que es exactamente lo que
mide la columna apertura de la propia tabla de este reporte (8.949 / 8.928 /
17.877 / 9.572). Caida de reporte con nombre, medida y adjudicada por el
auditor (`docs/loop/ACTA_AUDITOR.md`, vuelta 79, seccion 4 y seccion 5 punto
"la caida de reporte"): tercera tanda seguida, PARADA. Registrada sin
remedirse en `docs/loop/REPORTE.md` de la vuelta 80, TAREA 1.

**SE MANTIENE "LA TABLA SE CUENTA DE SU FICHERO"**: toda tabla o cifra de
este reporte cita el fichero de salida del que sale.

---

## 0. LO QUE CAMBIA COMO SE ESCRIBE ESTA VUELTA

La racha de caidas de reporte llego a **DOS TANDAS SEGUIDAS** (vueltas 77 y
78), que es el numero exacto que el fundador dejo escrito como gatillo de la
**ESCALADA AUTOMATICA de la opcion (b)**
(`docs/loop/paradas/2026-08-26-racha-tramo-mecanico-DECISION.md`, linea 183):
extender el tallador a la fase 04. Es la **TAREA 2 de este reporte, y fue
BLOQUEANTE**: no se leyo un solo candidato nuevo hasta que quedo verde. **La
parada de esta especie pide TRES tandas**: esta es la ultima vuelta antes de
esa parada si hubiera una tercera caida de reporte.

**Cero caidas de clase y cero de cifra publicada en la vuelta 78** (acta 78,
delantera): la racha de esa especie sigue en cero.

---

## 1. TAREA 1: LOS REGISTROS Y LA CORRECCION DECLARADA

### 1.1. La caida de reporte de la vuelta 78, registrada con su nombre

Medida y descrita en `docs/loop/ACTA_AUDITOR.md` (vuelta 78, seccion 3 D4 y
seccion 5 punto 4). Se registra aqui con su nombre, **sin volver a medirla**
(ya viene medida por el auditor, citado como fuente):

**UNA caida de reporte, DENTRO del marcado.** El reporte de la vuelta 78,
seccion 3.2, publico un criterio unico para las once aristas que la vara de
los veredictos A toca: *"si el extremo ESCRITO en la arista esta condenado
por una operacion sin ser su superviviente, la arista SE MUEVE; si el extremo
escrito ES el superviviente declarado, o si ninguna operacion condena al
extremo escrito, la arista SE QUEDA"*. La fila 11 de su propia tabla tiene el
hijo escrito sin ninguna operacion que lo condene, y por ese criterio debia
quedarse: se movio (revirtio). El criterio publicado no produce la decision
publicada, y no distingue la fila 11 de la 4 ni de la 6 (misma forma,
resultado distinto). **Las once disposiciones son correctas**; solo el
criterio publicado esta mal. Corregido en 1.2.

**Cero caidas de clase y cero de cifra publicada en la vuelta 78**: la racha
de esa especie sigue en cero (acta 78, delantera).

### 1.2. Correccion declarada: el criterio real de la TAREA 3.2, escrito donde se pueda auditar

**Verificado por corrida propia en esta vuelta** contra las fichas de
`docs/plan/OPERACIONES.jsonl` antes de escribir la correccion
(`docs/loop/SALIDA_V79_TAREA12_FICHAS.txt`):

```
OP-S-09       | tipo: RENOMBRE_CON_ALIAS | superviviente: None | eliminar: [] | nodos_len: 67
OP-M-05-APERTURA | tipo: FUSION DE MESA | superviviente: customer_validation | eliminar: ['filosofia_customer_validation', 'introduccion_validacion_clientes'] | nodos_len: 3
```

`OP-M-05-APERTURA` **es una FUSION con `superviviente` declarado**
(`customer_validation`) y `eliminar` de dos ids; `OP-S-09` **es un
RENOMBRE_CON_ALIAS con `superviviente` `null`**: confirma exactamente lo que
el docstring de `scripts/loop/vuelta78_tarea32_decision_once.py` ya
distinguia y el reporte de la vuelta 78 nunca publico.

**Texto viejo (reporte de la vuelta 78, seccion 3.2), citado sin
reescribir:** *"si el extremo ESCRITO en la arista (no su companero de A)
esta condenado por una operacion sin ser su superviviente, la arista SE
MUEVE; si el extremo escrito ES el superviviente declarado, o si ninguna
operacion condena al extremo escrito, la arista SE QUEDA con la razon
puesta."*

**CORRECCION DECLARADA (vuelta 79): el criterio real** vive ahora en
`docs/plan/04_ENLACES.md`, bajo las notas de `P.9.1` (correccion declarada
del 26 ago 2026, texto viejo intacto al lado): *"no es lo mismo que el
companero de A caiga en el `eliminar` de una FUSION que en los `nodos` de un
RENOMBRE_CON_ALIAS. Una fusion ya declara superviviente: si el extremo
escrito no es el condenado, el extremo escrito esta a salvo y la arista SE
QUEDA (filas 2, 3 y 4). Un renombre no mata a nadie y no declara ganador:
cual de los dos gemelos vivira sigue abierto, asi que la arista escrita sobre
cualquiera de los dos SE MUEVE y espera (fila 11). Y cuando el archivo remite
la familia a mesa, manda la mesa (fila 6, puesto 460)."* **Las once
disposiciones de la vuelta 78 no cambian**: solo se corrige el criterio
publicado.

### 1.3. Las cinco adjudicaciones del auditor, registradas sin remedirlas

De la seccion 5 del acta 78 (cita como fuente, no se vuelve a medir):

1. **D1** (`diferencia_iso9001_iso9004 -> trilogia_de_juran`): **la arista se
   queda**, por banco 9.6.2. Cerrado.
2. **D2** (`conformidad_comercio_internacional -> sistema_gestion_calidad`):
   **se queda**, por banco 9.6.2, con el lado flojo declarado. Cerrado.
3. **D3**: **no es sobre-conexion por termino generico**; tres de las cuatro
   se quedan; la cuarta (`extraer_priorizar_hipotesis ->
   value_proposition_startup`) fue a relectura conjunta. **Resuelta en la
   TAREA 3.1 de este reporte: se revierte.**
4. **D4**: **las once disposiciones se confirman una a una.** El criterio
   publicado se corrigio en 1.2.
5. **D5** (`requisitos_numericos_calidad_lotes ->
   critica_acceptable_quality_level`): **la abstencion se confirma y el
   PENDIENTE DE DOCTRINA queda DISUELTO por cita** de banco 9.6.2 (el hijo no
   ejecuta el paso de la madre: lo deroga) y banco 9.6.3 (procedimiento en
   los dos lados, par sano, caminos distintos). **No queda ninguna doctrina
   nueva pendiente por este par.** El pendiente que la seccion 7 del reporte
   de la vuelta 78 declaraba queda cerrado aqui, sin texto nuevo que
   inventar: es exactamente la cita del auditor.

---

## 2. TAREA 2 BLOQUEANTE: LA ESCALADA AUTOMATICA DEL TALLADOR A LA FASE 04

Disparada por la condicion escrita del fundador (racha de reporte en DOS),
no por decision propia. `scripts/loop/tallar_cabecera_reporte.py` ganó un
modo `--fase04` que talla la cabecera de la fase de ENLACES (apertura y
cierre por separado) leyendo `SALIDA_V<N>_GATE0_CMD1_*` (censo y las tres
comprobaciones de Gate 0), `SALIDA_V<N>_CONTEO_*` (las cuatro cifras de
aristas), `SALIDA_V<N>_MOTOR_*`, `SALIDA_V<N>_WEB_*`, `SALIDA_V<N>_TSC_*`, y
`SALIDA_V<N>_MARCADOR_*` **solo si la vuelta lo produce** (fila opcional, sin
la cual el tallador no cae en rojo).

**Mecanica de rojo, probada**: `python scripts/loop/tallar_cabecera_reporte.py
--fase04 --vuelta 999` (vuelta inexistente) cae en ROJO citando cada celda
que no se pudo leer, exit code 1, sin escribir tabla.

**`--comparar` funcional en fase04, probado con un sanity check propio**: se
tallo la cabecera de la vuelta 78 con `--fase04`, se pego en un fichero de
prueba, y `--comparar` contra si misma dio "CABECERA: IDENTICA AL TALLADOR"
(0 distintas, 0 ausentes); se inyecto una diferencia (`25/25` por `24/25` en
motor) y `--comparar` la nombro exacta: `DISTINTA | motor | apertura`, exit
code 1. El sanity check no se dejo en el repo (era un fichero temporal fuera
de convencion de nombre); el comando y su resultado quedan citados aqui para
que se puedan reproducir.

**CASO POSITIVO OBLIGATORIO con la vuelta 78**, script
`scripts/loop/vuelta79_tarea2_caso_positivo.py`, salida en
`docs/loop/SALIDA_V79_TAREA2_CASO_POSITIVO_TALLADOR.txt`: talla la cabecera
de la vuelta 78 con sus `SALIDA_V78_*` ya en el repo y coteja, **cifra por
cifra** (no por prosa: el reporte archivado en `0ea71f3a` teclea en dos
tablas de PROSA de dos columnas, no en la tabla limpia de tres columnas que
el tallador imprime, asi que `--comparar` no aplica aqui por choque de
FORMA, no de DATO; el script hace el cotejo de dato que el encargo pide,
leyendo el texto exacto del archivado). **Las 25 cifras cotejadas (censo,
las ocho de aristas, motor, web, tsc y Gate 0 en los dos lados, mas las
cinco del marcador de cierre) dan IGUALES.** Las unicas diferencias
literales de texto (p. ej. `"1.030 passed, 3 skipped (1.033)"` del tallador
contra `"1.030 pasadas, 3 saltadas"` del reporte viejo) son de PALABRA, no de
CIFRA: el tallador cita el instrumento en su idioma original (vitest en
ingles); el reporte viejo lo parafraseaba. Declarado, no oculto.

**Usado en el propio reporte de esta vuelta**: la cabecera de la seccion
"LA CABECERA DE ABAJO ESTA TALLADA" arriba sale integra de `python
scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 79`
(`docs/loop/SALIDA_V79_TALLADOR_FASE04.txt`).

**Gate 0 con su ciclo de tres, motor, web y tsc en verde ANTES de pasar a la
TAREA 3**: medido con la apertura de esta vuelta (seccion 5, columna
apertura), sin una sola operacion de codigo todavia.

---

## 3. TAREA 3: LA RELECTURA CONJUNTA Y LA RELECTURA AL DOBLE DEL TRAMO 4

### 3.1. Relectura conjunta: `extraer_priorizar_hipotesis -> value_proposition_startup`

**Verificado contra el grafo esta vuelta** (`dataset/nodos/*.json`): el paso
1 de la madre dice *"Lista todo lo que tiene que ser cierto sobre tu modelo
de negocio, tu propuesta de valor y tu cliente"*. **La accion del paso es
LISTAR**; la propuesta de valor es uno de los tres objetos que se listan, no
la accion. El resumen de la propia madre lo confirma sin ambiguedad: *"A
partir de tu mapa de propuesta de valor y tu modelo de negocio, identifica
todas las suposiciones..."*, es decir que la propuesta de valor es **insumo
previo** a este paso, no su resultado. El hijo (identificar problemas del
segmento, definir caracteristicas que los resuelven, verificar el encaje)
**no ejecuta "listar hipotesis": la precede.**

**DECISION: SE REVIERTE.** El caso del auditor (acta 78, seccion 3 D3) se
confirma contra el grafo. Contraste con la hermana que si pasa la vara en el
mismo hub, `etapa_build_business_case` (paso 1 *"Definir el mercado
objetivo, posicionamiento y propuesta de valor del producto"*): ahi la
accion del paso ES definir la propuesta de valor; aqui la accion es listar
hipotesis sobre tres objetos distintos. Reversion simetrizada en las dos
vistas (`scripts/loop/vuelta79_tarea31_relectura_conjunta.py`,
`docs/loop/SALIDA_V79_TAREA31_REVERSION.txt`), confirmada tras el ciclo de
Gate 0 que no reaparece (`docs/loop/SALIDA_V79_GATE0_CMD1_TRAS31.txt`).
Correccion declarada en `docs/plan/04_ENLACES.md`, bajo `OP-E-01`, texto
viejo intacto. **Las otras tres del mismo hub
(`actualizar_business_model_canvas_tuneup`, `etapa_build_business_case`,
`ventaja_competitiva_producto`) no se tocan**: ya fueron confirmadas en el
acta de la vuelta 78.

**TROPIEZO PROPIO declarado**: al verificar esta reversion corri Gate 0 CMD1
una segunda vez tras CMD2/CMD3 "para reverificar", reproduciendo el mismo
tropiezo de divergencia de `etiqueta_arbol` que la vuelta 78 documento
(`docs/loop/SALIDA_V79_TROPIEZO_CICLO_TRAS31.txt`). Corregido restaurando
los artefactos compilados con `git checkout` y corriendo el ciclo de tres
una vez cada comando, en orden, sin re-verificacion. **Leccion aplicada el
resto de esta vuelta**: el ciclo de tres se corre EXACTAMENTE una vez cada
comando; la confirmacion se lee del resultado de esa corrida o de `git
status`, nunca de una segunda corrida de CMD1.

### 3.2. Relectura al doble del tramo 4 (24 aristas), por el credito rebajado

El credito de la tanda quedo rebajado porque el hallazgo del par en dos
direcciones (TAREA 4 del encargo) aparecio fuera de los discutibles
marcados. Por `AUDITOR.md` seccion 1.2, el tramo 4 se releyo al doble, en
dos barridos (`scripts/loop/vuelta79_tarea32_relectura_doble_tramo4.py`,
salida completa en
`docs/loop/SALIDA_V79_TAREA32_RELECTURA_DOBLE_TRAMO4.txt`):

**Barrido 1, contra `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, sin direccion:**

| | contado del fichero |
|---|---:|
| aristas del tramo 4 | 24 |
| **LEIDAS por el cribado** | **1** |
| clase A (de las leidas) | 0 |
| **A REVERTIR** | **0** |

La unica leida: `sujetos_de_control -> key_process_product_characteristics`,
puesto 3205, clase D. **Declaracion sobre el numero, no discrepancia con el
auditor**: el encargo cita *"2 de las 30 leidas (3205 D y 637 B)"*, que es la
cifra correcta para el conjunto de **30** (24 escritas mas las 6 no
escritas del tramo 4): el puesto 637
(`equipo_customer_development -> customer_development_team`) pertenece a las
6 NO escritas, fuera de esta vara de 24. Sobre las 24 escritas
especificamente, que es lo que este punto pide cruzar, **1 de 24** es la
cifra que da la corrida.

**Barrido 2, contra la bolsa filtrada de 191 filas de la vuelta 78, buscando
la reciproca:**

| | contado del fichero |
|---|---:|
| de las 24, con reciproca propuesta en la bolsa y no leida | **1** |

La unica: `necesidades_reales_vs_declaradas -> descubrir_necesidades_del_cliente`
(fila 1 de 191), con su reciproca en la fila 46. **Coincide al digito con el
hallazgo del auditor** (acta 78, seccion 4). Ya esta adjudicada por el
auditor y no se toca: la arista se queda como esta escrita (banco 9.6.2, la
madre conserva materia propia que el hijo no toca).

**Resultado de la relectura al doble: cero reversiones. Las 24 aristas del
tramo 4 se sostienen** (menos la de la TAREA 3.1, que no forma parte de esta
vara: se revirtio por relectura conjunta de un discutible marcado, no por
esta vara de credito).

---

## 4. TAREA 4: LA GUARDA DEL PAR NO DIRIGIDO

Adjudicada por cita del banco 9.6.2 y de `AUDITOR.md` seccion 3, **sin
doctrina nueva**. El hallazgo del auditor (acta 78, seccion 4): la bolsa
filtrada de la vuelta 78 traia el mismo par dos veces, una en cada
direccion, y el campo `arista` del calibrador no tiene direccion, asi que
escribir un sentido resolvia el otro sin que nadie lo mirara.

**LA GUARDA**: antes de leer, la bolsa filtrada se agrupa por **par NO
DIRIGIDO**; cuando el mismo par aparece en las dos direcciones, las dos
filas se leen juntas y la direccion se decide con 9.6.2 explicitamente, con
la opcion descartada nombrada; la fila hermana no cuenta como candidato
aparte. Implementada en `scripts/loop/vuelta79_guarda_par_no_dirigido.py`.

**CASO POSITIVO OBLIGATORIO, con datos sinteticos**, salida en
`docs/loop/SALIDA_V79_TAREA4_GUARDA_CASO_POSITIVO.txt`: de 5 filas
sinteticas, agrupa el par `alfa<->beta` (propuesto en las dos direcciones)
como UNA pareja; deja suelto el candidato normal `gamma -> delta` (una sola
direccion); **y no produce falso positivo** con `epsilon -> zeta` y
`zeta -> eta` (comparten el nodo `zeta` pero con companeros distintos: NO
son el mismo par no dirigido, y la guarda los deja sueltos correctamente).
Candidatos tras la guarda: 4 (1 pareja + 3 sueltas), no 5. **Los cuatro
chequeos del caso positivo dan OK.**

Documentado en `docs/plan/04_ENLACES.md`, bajo las notas de `P.9.1`. **La
direccion de la fila 1 (`necesidades_reales_vs_declaradas ->
descubrir_necesidades_del_cliente`) ya esta adjudicada por el auditor y NO
se toca** (seccion 3.2 arriba).

**Corrida sobre la bolsa real de esta vuelta (TAREA 5): 0 parejas
detectadas** (`docs/loop/SALIDA_V79_TRAMO5_FILTRO_P91_GUARDA.txt`) — caso
normal, la guarda no rompe nada y confirma que no hay un segundo par en dos
direcciones esta vez.

---

## 5. TAREA 5: EL TRAMO 5 DE `OP-E-01`

Corrido porque TAREA 1 a 4 cerraron en verde (Gate 0 OK, motor 25/25, web
1.030/3, tsc limpio en cada tramo intermedio).

### 5.1. Bolsa recalibrada FRESCA

Corrida: `python scripts/plan/paso_contra_nodo_calibrado.py --umbral-titulo
72 --umbral-contencion 0.45 --min-tokens 4` (mismos umbrales, sobre el grafo
YA movido por 1.2 y 3.1). `docs/plan/PASO_NODO_CALIBRADO.jsonl` sellado
antes y **restaurado despues** de la corrida
(`docs/loop/SALIDA_V79_CALIBRADO_FRESCO.txt`):

| | vuelta 78, tras el tramo 4 (auditor, seccion 1.6 del acta) | **vuelta 79, esta vuelta** |
|---|---:|---:|
| candidatos brutos | 590 | **590** |
| bolsa reducida | 468 | **468** |
| **sin arista** | 258 | **259** |

**259, no 258: verificado por que.** La TAREA 3.1 de esta vuelta revirtio
`extraer_priorizar_hipotesis -> value_proposition_startup`, que SI esta en
la bolsa del calibrador: al revertirla, vuelve a "sin arista" (+1). 258 + 1
= 259. **No es discrepancia con el auditor: es el mismo fichero despues de
un movimiento que el propio encargo de esta vuelta ordeno** (TAREA 3.1).

### 5.2. Filtro `P.9.1` ensanchado MAS la guarda del par no dirigido

Script `scripts/loop/vuelta79_tramo5_filtrar.py`, salida en
`docs/loop/SALIDA_V79_TRAMO5_FILTRO_P91_GUARDA.txt`:

| | contado del fichero |
|---|---:|
| candidatos sin arista | 259 |
| **apartados por P.9.1 ensanchado (operaciones + vara de los A)** | **92** |
| de esos, SOLO por operacion | 35 |
| de esos, con al menos un motivo de la vara de los A | 57 |
| **limpios tras P.9.1** | **167** |
| **parejas detectadas por la guarda del par no dirigido** | **0** |
| **CANDIDATOS (unidades de lectura) tras la guarda** | **167** |

Bolsa filtrada completa en `docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V79.jsonl`
(167 filas, orden de archivo, sin sorteo).

### 5.3. Lectura de las primeras 30 unidades, con el criterio adjudicado

Dossier completo en `docs/loop/SALIDA_V79_TRAMO5_DOSSIER30.txt`.

**SIETE de las 30 unidades YA ESTABAN DECIDIDAS por vueltas anteriores de
esta misma campana** (reaparecen en la cabeza de la bolsa porque nunca se
escribieron y siguen pasando el filtro P.9.1): se citan sin re-derivar.

| # | par | decidido en |
|---:|---|---|
| 0 | `clasificacion_tipos_activos -> tipos_de_pasivos` | tramo 4, vuelta 78: gemelo estructural falso |
| 1 | `proceso_llamada_inicial_venta -> proceso_venta_franquicias` | tramo 4, vuelta 78: direccion inversa |
| 2 | `equipo_customer_development -> customer_development_team` | tramo 4, vuelta 78: veredicto B puesto 637, "sin arista entre ellos" |
| 3 | `extraer_priorizar_hipotesis -> value_proposition_startup` | TAREA 3.1 de esta vuelta: revertida |
| 4 | `preparacion_preguntas_problema_precall -> preguntas_situacion` | tramo 4, vuelta 78: hermanas SPIN, no madre-hijo |
| 5 | `timing_solicitud_referidos -> fase_adopt_ciclo_cliente` | tramo 4, vuelta 78: direccion de generalidad al reves |
| 6 | `requisitos_numericos_calidad_lotes -> critica_acceptable_quality_level` | D5 disuelto, TAREA 1.3 de esta vuelta: critica, no procedimiento |

**Las 23 restantes son lectura fresca de esta vuelta.** Tres tenian
veredicto propio del cribado, honrado como manda el criterio adjudicado
("veredicto del cribado PRIMERO"):

| puesto | par | clase | lo que dice el archivo | decision |
|---:|---|:---:|---|:---:|
| 2324 | `identificacion_evaluacion_peligros -> investigacion_incidentes` | D | *"Por la vara, CONTINUA. ARISTA QUE FALTA."* | **SE ENLAZA** |
| 2097 | `analisis_competencia_franquicias -> posicionamiento_vs_competidores` (mismo par, direccion inversa a la propuesta) | D | *"sin arista entre ellos... CONTINUA en los dos sentidos, banco 9.22: uno junta la municion, el otro dispara"* | **NO SE ENLAZA** |
| 384 | `mvp_catalogo_tecnicas -> mvp_tipo_video` | D | *"no hay arista entre estos dos, [...] la madre real es producto_minimo_viable"* | **NO SE ENLAZA** |

**El puesto 2324 es el hallazgo de la tanda**: un veredicto CLASE D cuya
propia razon dice explicitamente que la arista FALTA, es decir que la clase
D en este cribado no siempre significa "no se enlaza": hay que leer la
razon, no solo la letra. Los otros 20 se decidieron por 9.6.2 (contenido).

**LA TABLA SE CUENTA DE SU FICHERO**, escritura en
`docs/loop/SALIDA_V79_TRAMO5_ESCRIBIR.txt`:

| clase | cuantos de las 23 nuevas | que se hizo |
|---|---:|---|
| **JERARQUIA SANA (9.6.2)** | **12** | arista escrita en `nodos_siguientes` Y `nodos_previos` a la vez |
| **NO ESCRITOS, con razon** | **11** | sin arista, razon citada abajo |

**Chequeo de escalera, exacto**, sobre las 12: **cero de 12** (contado del
mismo fichero, seccion "ESCALERA ROTA: 0").

**Las 12 aristas sanas escritas:**

1. `uso_inadecuado_computadoras -> causas_comunes_vs_especiales`: paso 3 es
   la linea (aprender a distinguir causa comun de causa especial); el hijo
   ES ese procedimiento de deteccion (Deming) con 15 pasos propios.
2. `producto_mercado_fit_motores -> afinar_motor_crecimiento`: el calibrador
   senala el paso 1, pero el que calza es el paso 4 (usar la contabilidad de
   la innovacion para decidir pivote); el hijo ES el segundo paso de esa
   misma contabilidad de la innovacion, nombrado por su propio resumen.
3. `planificacion_inicial_calidad -> identificar_caracteristicas_metas_proceso`:
   paso 2 es la linea (identificar KPCs); el hijo ES ese procedimiento.
4. `establecimiento_capacidad_proceso -> pruebas_destructivas`: paso 5 es la
   linea (confirmar control estadistico mediante cartas de control); el
   hijo especializa esa confirmacion para el caso de pruebas que destruyen
   la muestra.
5. `certificacion_de_proveedores -> indice_cpk`: paso 3 es la linea (usar
   indices de capacidad de proceso en la certificacion); el hijo ES uno de
   esos indices con procedimiento propio.
6. `mitigacion_efecto_latigo -> precios_todos_los_dias_bajos`: paso 4 es la
   linea literal ("everyday low price"); el hijo ES esa politica.
7. `herramientas_analisis_causa_raiz -> estratificacion_datos`: paso 5
   nombra la estratificacion explicitamente; el hijo ES esa tecnica.
8. `identificacion_evaluacion_peligros -> investigacion_incidentes`:
   veredicto propio, puesto 2324, "ARISTA QUE FALTA" (arriba).
9. `establecimiento_capacidad_proceso -> control_estadistico_de_procesos`:
   mismo paso 5 que el par 4, hijo distinto: el metodo GENERAL de SPC (10
   pasos), frente al caso especializado de pruebas destructivas. Dos hijos
   legitimos para el mismo paso.
10. `testear_circulo_cuadrado_rectangulo -> validar_modelo_negocio_hechos`:
    paso 3 es la linea (validar el modelo de negocio completo, "rectangulo");
    el hijo ES el procedimiento de convertir el canvas en hechos.
11. `terminologia_clave_breakthrough -> analisis_sintomas`: paso 2 es la
    linea (diferenciar sintomas de causas); el hijo profundiza la
    caracterizacion de sintomas antes de inferir causas.
12. `mapa_de_canal_de_ventas -> validar_canal_distribucion`: paso 1 es la
    linea literal (validar un solo canal); el hijo ES ese procedimiento.

**Los once no escritos, con razon:**

- `hipotesis_relacion_clientes_web -> mvp_alta_fidelidad`: el paso senalado
  nombra MVP de BAJA fidelidad; el hijo propuesto es de ALTA fidelidad.
  Mismatch de fidelidad, ningun paso nombra la version alta.
- `valor_intangible_sostenibilidad -> compromiso_cliente_sostenibilidad`: el
  paso es sobre metricas de tracking; el hijo es una tactica especifica de
  campanas digitales. Tematico, no procedimiento del paso.
- `analisis_valor -> customer_needs_spreadsheet`: el paso exige relacionar
  COSTOS con necesidades; el hijo nunca toca costos, es otra herramienta
  (matriz cliente x necesidad de Quality by Design).
- `posicionamiento_vs_competidores -> analisis_competencia_franquicias`:
  veredicto propio, puesto 2097, "sin arista entre ellos" (arriba).
- `organizacion_interna_exportacion -> estructura_plan_exportacion`: el
  paso es sobre estructura de REPORTE organizacional; el hijo es la
  estructura de un DOCUMENTO. Coincidencia lexica, significados distintos.
- `errores_comunes_fundraising -> confidencialidad_nda_adquisicion`: reglas
  opuestas para escenarios distintos (VC vs M&A): contraste, no jerarquia.
- `mvp_catalogo_tecnicas -> mvp_tipo_video`: veredicto propio, puesto 384,
  "no hay arista entre estos dos" (arriba).
- `reporte_estado_miembro_equipo -> variance_analysis`: el hijo no cabe en
  un solo paso de la madre (abarca tres a la vez); posible relacion mas
  ancha o invertida.
- `evaluacion_actitudes_empleados -> identificar_oportunidades_sostenibilidad`:
  el paso es sobre reacciones internas de empleados; el hijo es analisis
  estrategico de mercado externo. Mismatch de objeto.
- `pre_control_estadistico -> limites_de_especificacion_vs_limites_de_control`:
  el hijo es una advertencia conceptual contra el TIPO de ajuste que
  Pre-Control practica: contraste, no procedimiento.
- `posicionamiento_por_tipo_de_mercado -> resegmentacion_mercado_nicho_bajo_costo`:
  el paso manda COMUNICAR; el hijo es el trabajo analitico previo a esa
  comunicacion (identificar, evaluar, definir, mapear). Misma especie que
  `extraer_priorizar_hipotesis` (TAREA 3.1): el paso nombra el resultado, el
  hijo hace el trabajo previo, no la accion mandada.

**Gate 0 el ciclo entero, tras las 12 escrituras**
(`docs/loop/SALIDA_V79_GATE0_CMD1_TRAMO5.txt`, `_CMD2_`, `_CMD3_`): OK,
3.853/3.188/665, 0 auto-aristas, 0 duplicadas de titulo, 0 divergentes;
motor **25/25** (`SALIDA_V79_MOTOR_TRAMO5.txt`); web **80/1.030/3**
(`SALIDA_V79_WEB_TRAMO5.txt`); tsc **exitcode 0, cero lineas**
(`SALIDA_V79_TSC_TRAMO5.txt`).

### 5.4. Discutibles de la lectura, marcados AQUI antes de saber si aciertan

1. **`uso_inadecuado_computadoras -> causas_comunes_vs_especiales`.** La
   madre ya tiene OTRO hijo del tramo 4 sobre el mismo paso 3 y el mismo
   concepto (`causas_especiales_y_comunes_variacion`, via Juran), y existe
   un TERCER nodo casi identico en el grafo
   (`causas_comunes_causas_especiales`, ya senalado por Gate 0 como
   similitud de titulo >=95 contra `causas_comunes_vs_especiales`). El par
   pasa 9.6.2 solo (cabe entero en el paso, madre conserva materia propia),
   pero la posible sobre-cobertura del mismo paso con un hijo casi-gemelo de
   uno ya escrito merece relectura: podria ser que uno de los tres nodos de
   "causas comunes/especiales" sea un duplicado no detectado que deberia
   fundirse en vez de acumular madres distintas.
2. **`producto_mercado_fit_motores -> afinar_motor_crecimiento`.** Escrita
   bajo el paso 4 (redireccion de paso, acta 77 D1), no el paso 1 que el
   calibrador senalo. El hijo cubre solo UNO de los tres pasos del framework
   de "contabilidad de la innovacion" que el paso 4 invoca en bloque
   (establecer linea base, afinar motor, pivotar o perseverar). Se escribe
   por el precedente de redireccion, pero la cobertura parcial vale
   relectura.
3. **`terminologia_clave_breakthrough -> analisis_sintomas`.** La accion
   literal del paso 2 es "diferenciar" sintomas de causas; el hijo no hace
   esa comparacion paso a paso, solo profundiza la caracterizacion del
   sintoma (frecuencia, severidad, tipo, ubicacion). Direccion floja, mismo
   patron que los discutibles de `iso9001/iso9004` y
   `conformidad_comercio_internacional` de la vuelta 78 (D1 y D2, ambos A
   FAVOR pero con el lado flojo declarado).
4. **`identificacion_evaluacion_peligros -> investigacion_incidentes`**,
   puesto 2324. Es la primera vez en esta campana que un veredicto **clase
   D** se lee como mandato de ENLAZAR (**"ARISTA QUE FALTA"**) en vez de
   como "no se enlaza". Vale que el auditor confirme que la lectura de la
   letra de clase contra el texto de la razon es correcta aqui, porque
   podria sentar un precedente sobre como se lee la clase D en general.

---

## 6. EL CIERRE, medido AL CIERRE

Commit de esta vuelta que cierra TAREA 1 a 5:
`2bbb0408` (TAREA 1 y 2), `07324da5` (TAREA 3), `43b02413` (TAREA 4),
`38ab7b37` (TAREA 5); este reporte se cierra en un commit posterior que solo
anade este mismo fichero.

La tabla de cabecera de la seccion 0 de arriba **es** la medicion de cierre
(columna derecha), tallada con `python scripts/loop/tallar_cabecera_reporte.py
--fase04 --vuelta 79` sobre `SALIDA_V79_*_CIERRE.txt`. Cifras adicionales que
el tallador de fase04 no cubre, contadas de su fichero:

| | medido con |
|---|---|
| aristas nuevas escritas esta vuelta | **12** (TAREA 5); **0** de TAREA 1 esta vuelta (TAREA 1 fue registro y correccion de texto, no arista) |
| aristas revertidas esta vuelta | **1** (TAREA 3.1: `extraer_priorizar_hipotesis -> value_proposition_startup`) |
| pares leidos y no enlazados esta vuelta (tramo 5, con razon) | **11** |
| pares ya decididos citados sin re-derivar | **7** |
| operaciones cerradas esta vuelta | 0 |
| correcciones declaradas esta vuelta | 3 (1.2, la de TAREA 3.1 en `04_ENLACES.md`, la guarda de TAREA 4) |
| bolsa de `OP-E-01` restante sin leer (filtrada por P.9.1 ensanchado + guarda, esta vuelta) | **137 de 167** (167 filtrados menos las 30 unidades leidas) |

Verificado con `python docs/loop/_auditor_v78_conteo.py HEAD WORK` que las
cifras de aristas de la cabecera coinciden con el arbol de trabajo tras el
cierre (`docs/loop/SALIDA_V79_CONTEO_CIERRE.txt`).

**OBSERVACION TECNICA, no bloqueante, declarada para que no se repita sin
aviso**: durante esta vuelta, correr `run_phase1.py` (Gate 0 CMD1) una
SEGUNDA vez despues de `etiquetas_de_cara.py`/`sync_assets_web.py` reprodujo
DOS VECES el mismo tropiezo de divergencia de `etiqueta_arbol` entre
`dataset/metadata/master_graph.json` y `web/lib/assets/master_graph.json`
(seccion 3.1 arriba, y de nuevo al intentar medir esta misma seccion de
cierre). **En al menos una de las dos veces, el propio chequeo interno de
Gate 0 ("Los dos master_graph dicen lo mismo") reporto 0 divergentes pese a
que `test_gate_alias.py::test_EL_CATALOGO_REAL_ESTA_LIMPIO` si detectaria la
divergencia real de contenido si se corriera en ese instante** (no se
corrio motor en ese instante exacto, asi que esto es una observacion sobre
el ORDEN de los datos en disco, no una caida confirmada por dos
instrumentos a la vez). No se investigo mas a fondo por no ser parte del
encargo; **se marca aqui como discutible tecnico** para que el auditor o una
vuelta futura decida si Gate 0 necesita el mismo chequeo que
`test_gate_alias.py` ya tiene.

---

## 7. LOS DISCUTIBLES MARCADOS, para la relectura ciega del auditor

Los cuatro discutibles de la seccion 5.4 (arriba): el posible near-duplicate
en `causas_comunes_vs_especiales`, la redireccion de paso parcial en
`afinar_motor_crecimiento`, la direccion floja en `analisis_sintomas`, y la
lectura de la clase D como mandato de enlazar en el puesto 2324. Mas la
observacion tecnica de la seccion 6 sobre el chequeo de divergencia de Gate
0.

---

## 8. PENDIENTES DE DOCTRINA

**Ninguno nuevo.** El pendiente que la vuelta 78 dejo abierto (D5,
`requisitos_numericos_calidad_lotes -> critica_acceptable_quality_level`)
quedo disuelto por cita en la TAREA 1.3 de este reporte (banco 9.6.2 y
9.6.3), sin doctrina nueva que escribir.

---

## 9. LO QUE QUEDA PENDIENTE PARA LA VUELTA SIGUIENTE

- Continuar `OP-E-01` con un TRAMO 6, recalibrando la bolsa antes de leer
  (regla EL INSTRUMENTO MANDA: no reusar
  `PASO_NODO_CALIBRADO_FILTRADO_V79.jsonl`, el grafo ya se habra movido otra
  vez con las 12 aristas de este tramo), y con la guarda del par no dirigido
  ya incorporada de forma permanente al flujo de filtrado.
- Los cuatro discutibles de la seccion 5.4 esperan la relectura ciega del
  auditor.
- La observacion tecnica de la seccion 6 (Gate 0 vs `test_gate_alias.py` en
  el chequeo de divergencia) espera decision: se investiga a fondo o se
  deja como esta.
- `OP-E-02` sigue CERRADO (vuelta 76), sin cambio.
- `OP-E-03` sigue esperando a que `OP-E-01` termine entero.
- `OP-M-03-ENLACES`, `OP-E-04`, `OP-E-05`, `OP-M-01-ESLABONES` y
  `OP-M-01-SEXTO` siguen esperando a la fase 06 (remision escrita, no se
  tocan).
- `OP-E-06` y `OP-E-07` siguen libres de bloqueo de dependencia pero esperan
  su turno en el orden escrito.
- Las diez aristas de la fase 04 que la vara de los A sigue tocando (acta
  78, seccion 1.8) quedan como observacion, no como parada: ninguna
  operacion las condena hoy.

Commitea y pushea lo pendiente en la rama activa antes de tocar nada (esta
vuelta: hecho al cierre de cada tramo, y de nuevo al cierre de este mismo
reporte). Cero guiones largos y cero guiones medios. El hook corrio en cada
commit sin saltarse. No se adivino nada que no se pudiera medir.
