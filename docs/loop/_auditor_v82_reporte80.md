# REPORTE DE LA VUELTA 80 DEL EJECUTOR (modelo: Sonnet 5)

Sobrescribe el reporte de la vuelta 79. Cubre TAREA 1 (registros y correccion
declarada de la caida de reporte de la vuelta 79), TAREA 2 BLOQUEANTE (el
tallador `--fase04` gana la fila de identidad, commit de apertura leido de
git), TAREA 3 (las dos relecturas conjuntas D2 y D3 del acta 79), TAREA 4 (la
relectura al doble del tramo 5) y TAREA 5 (el tramo 6 de `OP-E-01`) del
encargo de `docs/loop/PROMPT_SIGUIENTE.md`, escrito tras la decision del
fundador en
`docs/loop/paradas/2026-08-26-racha-hash-apertura-DECISION.md`.

**LA CABECERA DE ABAJO ESTA TALLADA, NO TECLEADA, Y AHORA INCLUYE LA
IDENTIDAD**, con el instrumento extendido en la TAREA 2 de esta vuelta:

```
python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 80
```

Salida completa en `docs/loop/SALIDA_V80_TALLADOR_FASE04.txt`, pegada entera:

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.188 / 665 | **3.853 / 3.188 / 665** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 8.960 / 8.939 / 17.899 / 9.583 | **8.960 / 8.939 / 17.899 / 9.583** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit `bc9cde6f` (ACTA DE LA VUELTA 79 DEL AUDITOR, leido de git log) | **rama `pasada-unica`, commit `bc9cde6f` (ACTA DE LA VUELTA 79 DEL AUDITOR, leido de git log)** |

**Verificado con `--comparar` contra este mismo fichero antes del commit de
cierre** (regla 1 de `EJECUTOR.md`): `python scripts/loop/tallar_cabecera_reporte.py
--fase04 --vuelta 80 --comparar docs/loop/REPORTE.md` da **7 filas
cotejadas, 0 DISTINTAS, 0 ausentes, "CABECERA: IDENTICA AL TALLADOR"**
(corrida despues de pegar esta misma tabla, salida citada en la seccion 6).

**El marcador del cribado no aparece**: esta fase no lo toca, y el tallador
omite la fila cuando no hay `SALIDA_V80_MARCADOR_*` que citar. Sin cambio
real: el cribado sigue en A 551, B 72, C 5, D 2.760, n 3.388, medido la
ultima vez en `docs/loop/SALIDA_V79_MARCADOR_CIERRE.txt` (contraste, no
cifra nueva de esta vuelta).

**SE MANTIENE "LA TABLA SE CUENTA DE SU FICHERO"**: toda tabla o cifra de
este reporte cita el fichero de salida del que sale.

---

## 0. LO QUE CAMBIA COMO SE ESCRIBE ESTA VUELTA

La vuelta 79 cerro en **PARADA por racha de reporte en TRES tandas
seguidas** (77, 78, 79), documentada en
`docs/loop/paradas/2026-08-26-racha-hash-apertura-DECISION.md`. El fundador
decidio la **opcion (b) generalizada** el 26 ago 2026: el tallador gana la
**PROSA DE IDENTIDAD** (commit de apertura leido de git, nunca tecleado), y
la regla queda escrita en `EJECUTOR.md` como **LA IDENTIDAD SE LEE DE GIT**.
**Esta vuelta ejecuta esa decision como TAREA 2 BLOQUEANTE, la racha de
reporte vuelve a CERO al relanzar, y `OP-E-01` sigue con el tramo 6.**

**Cero caidas de clase y cero de cifra publicada en la vuelta 79** (acta 79,
seccion 7): esa racha sigue en cero, y sigue en cero al cierre de esta
vuelta (nada de lo hecho aqui movio un dato sin verificarlo por corrida
propia).

---

## 1. TAREA 1: LOS REGISTROS Y LA CORRECCION DECLARADA

### 1.1. La caida de reporte de la vuelta 79, registrada con su nombre

Medida y descrita en `docs/loop/ACTA_AUDITOR.md` (vuelta 79, seccion 4 y
seccion 5 punto "la caida de reporte"). Se registra aqui con su nombre, **sin
volver a medirla** (ya viene medida por el auditor, citado como fuente):

**UNA caida de reporte, FUERA del marcado (tercera tanda seguida, PARADA).**
El reporte de la vuelta 79, seccion 0, publico: *"Commit de apertura:
`43b02413` (acta de la vuelta 78, [...] verificado con `git rev-parse HEAD` y
`git rev-parse origin/pasada-unica`)."* **`43b02413` es el commit de la
TAREA 4 de esa misma vuelta 79**, escrito por el propio ejecutor a mitad del
trabajo; la apertura real es **`aea7cc81`**, el acta de la vuelta 78. El
arbol del hash publicado (8.948/8.927/17.875/9.571) contradice la propia
columna apertura del reporte (8.949/8.928/17.877/9.572, que es lo que mide
`aea7cc81`). **No mueve ningun dato**: es la especie barata, y fue la
tercera seguida.

### 1.2. Correccion declarada: la linea de REPORTE.md, con el texto viejo intacto delante

**Corregida directamente en `docs/loop/REPORTE.md` (commit `d2f6b524`), sin
reescribir el texto viejo**: la linea original ("Commit de apertura:
`43b02413`...") quedo intacta, y debajo se anadio la correccion declarada
nombrando el hash correcto (`aea7cc81`) y citando la fuente (acta 79,
seccion 4). Esta vuelta el reporte se reescribe entero (regla de
`AUDITOR.md`, "el reporte completo va en REPORTE.md, sobrescribe el
anterior"), asi que el rastro de esa correccion queda en el historial de
`git log -- docs/loop/REPORTE.md` en el commit `d2f6b524`, y aqui, en esta
seccion 1.2, con el texto viejo citado arriba en 1.1 sin borrarlo.

### 1.3. Las seis adjudicaciones del acta 79, registradas sin remedirlas

De la seccion 5 del acta 79 (cita como fuente, no se vuelve a medir):

1. **D1** (`uso_inadecuado_computadoras -> causas_comunes_vs_especiales`):
   **la arista se queda**, por cita de 9.6.2 y por medicion (el tercer nodo
   del racimo esta DEPRECADO, no hay duplicado sin detectar). **Cerrado.**
2. **D2** (`producto_mercado_fit_motores -> afinar_motor_crecimiento`): **no
   pasa la vara, va a RELECTURA CONJUNTA.** Es un radio sobre la cadena
   completa del framework de contabilidad de la innovacion. **Resuelta en la
   TAREA 3.1 de este reporte: se revierte.**
3. **D3** (`terminologia_clave_breakthrough -> analisis_sintomas`): **no pasa
   la vara, va a RELECTURA CONJUNTA.** El hijo caracteriza el sintoma; el
   paso manda diferenciarlo de la causa. **Resuelta en la TAREA 3.2 de este
   reporte: se revierte.**
4. **D4** (clase D del puesto 2324 leida como mandato de enlazar): **la
   arista se queda, y NO sienta precedente.** La clase D contesta la
   pregunta de la fusion, no la del enlace. **Cerrado.**
5. **Observacion tecnica de Gate 0**: **NO es un fallo y no queda
   pendiente.** El chequeo compara el snapshot previo al paso 6 por diseno
   declarado en `run_phase1.py`, y el motor cubre el estado en disco.
   **Cerrado.**
6. **VARA NUEVA DE LA CADENA, por cita y sin doctrina nueva**: antes de
   escribir una arista de la fase 04, medir si el hijo ya cuelga de la
   cadena de la madre en el orden que la madre enumera. **Puesta en
   operacion en la TAREA 5 de este reporte**
   (`scripts/loop/vuelta80_vara_cadena.py`).

---

## 2. TAREA 2 BLOQUEANTE: EL TALLADOR GANA LA PROSA DE IDENTIDAD

Disparada por la decision del fundador (opcion b generalizada), no por
decision propia. `scripts/loop/tallar_cabecera_reporte.py`, modo `--fase04`,
gana una fila mas: **el commit de apertura, leido de `git log` de la rama
actual** (leida de `git rev-parse --abbrev-ref HEAD`, nunca tecleada),
buscando el commit cuyo mensaje EMPIEZA por `"ACTA DE LA VUELTA <vuelta-1>
DEL AUDITOR"` (patron exacto que todo acta de auditor usa). **Si no hay
NINGUNO o hay MAS DE UNO, ROJO: jamas inventa un hash.**

**Mecanica de rojo, probada**: `python scripts/loop/tallar_cabecera_reporte.py
--fase04 --vuelta 999` cae en ROJO citando **33 celdas** no leidas (32 de las
seis filas de siempre, mas la nueva fila de identidad: *"git log de la rama
pasada-unica no trae ningun commit 'ACTA DE LA VUELTA 998 DEL AUDITOR'"*),
exit code 1, sin escribir tabla.

**CASO POSITIVO OBLIGATORIO contra la vuelta 79**, salida en
`docs/loop/SALIDA_V80_TAREA2_CASO_POSITIVO_V79.txt`: `python
scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 79` da como commit
de apertura **`aea7cc81`, NO `43b02413`**, exactamente lo que la caida de la
vuelta 79 debio publicar.

**`--comparar` probado dos veces, cotejando la fila de identidad como una
fila mas**: contra `docs/loop/REPORTE.md` tal como estaba (la fila no
existia todavia en su tabla, formato de dos columnas de prosa) dio
**AUSENTE**; contra una copia con el hash malo (`43b02413`) inyectado a mano
dio **DISTINTA, apertura y cierre**, citando fichero contra tallador
celda por celda, exit code 1. Los ficheros de prueba no quedan en el repo
(no siguen la convencion de nombre); el comando y su salida quedan citados
en el commit `038ebcd0` y aqui.

**Lo que la regla generalizada todavia no cubre, dicho y no callado** (regla
1 de `EJECUTOR.md`: *"si al construirlo ves que alguna de esas lineas
todavia queda fuera de lo tallado, la nombras"*): la **RAMA** se lee de git
como apoyo pero no es fila propia comparable (no hay una segunda rama contra
la que fallar); el **COMMIT DE CIERRE** y las **FECHAS** de apertura/cierre
quedan FUERA de este tallador, porque el commit de cierre de una vuelta no
existe todavia en el instante en que el tallador corre (el reporte que lo
citaria es, el mismo, parte de ese commit). Mientras el reporte necesite
nombrar el cierre, lo hace citando los commits de tarea ya creados (seccion
6 de este mismo reporte), no un hash unico de cierre.

**Usado en el propio reporte de esta vuelta**: la cabecera de la seccion "LA
CABECERA DE ABAJO ESTA TALLADA" arriba sale integra de `python
scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 80`
(`docs/loop/SALIDA_V80_TALLADOR_FASE04.txt`).

---

## 3. TAREA 3: LAS DOS RELECTURAS CONJUNTAS DE LA SECCION 5 DEL ACTA 79

### 3.1. `producto_mercado_fit_motores -> afinar_motor_crecimiento` (D2)

**Verificado contra el grafo esta vuelta** (`dataset/nodos/*.json`): el paso
4 de la madre (*"Usa la contabilidad de la innovacion..."*) nombra
literalmente `contabilidad_innovacion`, YA enlazado en `nodos_siguientes` de
la madre. `contabilidad_innovacion.nodos_siguientes` incluye
`establecer_linea_base_mvp` (*"Este es el primer paso..."*, por su propio
resumen). `establecer_linea_base_mvp.nodos_siguientes` es **exactamente**
`['afinar_motor_crecimiento']` (*"Es el segundo paso..."*). **La cadena
completa ya existia en el grafo de la apertura**, en el orden exacto que los
propios resumenes declaran: `producto_mercado_fit_motores ->
contabilidad_innovacion -> establecer_linea_base_mvp ->
afinar_motor_crecimiento`.

**DECISION: SE REVIERTE.** El caso del auditor (acta 79, seccion 2, D2) se
confirma contra el grafo campo a campo. Es el CAVEAT MEDIDO de la 9.6.1 ("la
familia ENCADENADA no se cuenta por radios [...] antes de contar, se mira la
FORMA"): `afinar_motor_crecimiento` NO es contenido huerfano de camino
(banco 9.6), esta a tres saltos por el camino que el propio paso 4 nombra.
Mismo error, mismo remedio, que la correccion declarada del primer ejemplar
de la 9.6 (`proceso_diseno_modelo_negocio_5_fases`).

### 3.2. `terminologia_clave_breakthrough -> analisis_sintomas` (D3)

**Verificado contra el grafo esta vuelta**: el paso 2 de la madre es literal:
*"Diferenciar sintomas de causas en cada problema detectado"*. Los cuatro
pasos del hijo (recolectar datos de ocurrencia, ubicar la falla con
diagramas de flujo, aplicar Pareto y estratificacion, documentar
frecuencia/severidad/tipo) **caracterizan el sintoma; ninguno lo DIFERENCIA
de la causa**. Los entregables no coinciden (madre: *"glosario de terminos
[...] y lista de teorias a probar"*; hijo: *"analisis documentado de
sintomas"*), que 9.6.2 declara la senal mas fiable que los pasos.

**DECISION: SE REVIERTE.** El caso del auditor (acta 79, seccion 2, D3) se
confirma contra el grafo. Por 9.6.2 (*"la vara tiene direccion"*), el hijo
PRECEDE la accion del paso, no la ejecuta.

### 3.3. Las dos reversiones, simetrizadas y recomputadas

Escrito en `scripts/loop/vuelta80_tarea3_relectura_conjunta.py`
(`docs/loop/SALIDA_V80_TAREA3_REVERSION.txt`): las dos quitadas de **las DOS
vistas a la vez**, con las cuatro comprobaciones ANTES/DESPUES dando
`True`/`False` exactas para las dos. Correccion declarada en
`docs/plan/04_ENLACES.md`, bajo `OP-E-01`, texto viejo intacto.

**Gate 0 el ciclo entero tras las dos reversiones**
(`docs/loop/SALIDA_V80_GATE0_CMD1_TRAS_TAREA3.txt`): OK, sin reaparicion.
Aristas: **8.958 / 8.937 / 17.895 / 9.581**
(`docs/loop/SALIDA_V80_CONTEO_TRAS_TAREA3.txt`), dos menos que la apertura
(8.960/8.939/17.899/9.583) en las cuatro cifras, como corresponde a dos
aristas quitadas de las dos vistas. Motor **25/25**
(`SALIDA_V80_MOTOR_TRAS_TAREA3.txt`), web **80/1.030/3**
(`SALIDA_V80_WEB_TRAS_TAREA3.txt`), tsc **limpio**
(`SALIDA_V80_TSC_TRAS_TAREA3.txt`).

---

## 4. TAREA 4: LA RELECTURA AL DOBLE DEL TRAMO 5 (12 ARISTAS), POR EL CREDITO REBAJADO

El credito de la tanda quedo rebajado porque la caida de reporte de la
vuelta 79 aparecio **FUERA de los discutibles marcados** (`AUDITOR.md`
seccion 1.2). El tramo 5 de `OP-E-01` (las 12 aristas de la vuelta 79) se
relee al doble, script
`scripts/loop/vuelta80_tarea4_relectura_doble_tramo5.py`, salida completa en
`docs/loop/SALIDA_V80_TAREA4_RELECTURA_DOBLE_TRAMO5.txt`:

**Barrido 1, contra `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, sin direccion:**

| | contado del fichero |
|---|---:|
| aristas del tramo 5 | 12 |
| **LEIDAS por el cribado** | **1** |
| clase A (de las leidas) | 0 |
| **A REVERTIR** | **0** |

La unica leida: `identificacion_evaluacion_peligros ->
investigacion_incidentes`, puesto 2324, clase D (ya adjudicada por el
auditor: *"ARISTA QUE FALTA"*).

**Barrido 2, contra la bolsa filtrada de la vuelta 79 (167 filas), buscando
la reciproca:**

| | contado del fichero |
|---|---:|
| de las 12, con reciproca propuesta en la bolsa y no leida | **0** |

**Resultado de la relectura al doble: cero reversiones.** Las 12 aristas del
tramo 5 se sostienen por esta vara de credito (las dos reversiones de la
TAREA 3, D2 y D3, no cuentan aqui: fueron adjudicadas por relectura conjunta
de discutibles marcados, no por esta vara).

---

## 5. TAREA 5: EL TRAMO 6 DE `OP-E-01`

Corrido porque TAREA 1 a 4 cerraron en verde (Gate 0 OK, motor 25/25, web
1.030/3, tsc limpio en cada tramo intermedio).

### 5.1. Bolsa recalibrada FRESCA, sobre el grafo ya movido por la TAREA 3

Corrida: `python scripts/plan/paso_contra_nodo_calibrado.py --umbral-titulo
72 --umbral-contencion 0.45 --min-tokens 4` (mismos umbrales, sobre el grafo
YA movido por las dos reversiones de la TAREA 3).
`docs/plan/PASO_NODO_CALIBRADO.jsonl` sellado antes y **restaurado despues**
de la corrida (`docs/loop/SALIDA_V80_CALIBRADO_FRESCO.txt`):

| | vuelta 79, tras el tramo 5 | **vuelta 80, esta vuelta** |
|---|---:|---:|
| candidatos brutos | 590 | **590** |
| bolsa reducida | 468 | **468** |
| **sin arista** | 259 | **249** |

**249, no 259: verificado por que.** El tramo 5 de la vuelta 79 escribio 12
aristas (quitandolas del pool de "sin arista": 259-12=247); la TAREA 3 de
esta vuelta revirtio 2 de esas 12 (D2 y D3), devolviendolas al pool
(247+2=249). **No es discrepancia: es el mismo fichero despues de los
movimientos que esta misma vuelta ordeno.**

### 5.2. Filtro `P.9.1` ensanchado, la guarda del par no dirigido Y LA VARA NUEVA DE LA CADENA

Script `scripts/loop/vuelta80_tramo6_filtrar.py`, salida en
`docs/loop/SALIDA_V80_TRAMO6_FILTRO_P91_GUARDA_CADENA.txt`:

| | contado del fichero |
|---|---:|
| candidatos sin arista | 249 |
| **apartados por P.9.1 ensanchado (operaciones + vara de los A)** | **92** |
| de esos, SOLO por operacion | 35 |
| de esos, con al menos un motivo de la vara de los A | 57 |
| **limpios tras P.9.1** | **157** |
| **parejas detectadas por la guarda del par no dirigido** | **0** |
| **CANDIDATOS (unidades de lectura) tras la guarda** | **157** |

Bolsa filtrada completa en `docs/plan/PASO_NODO_CALIBRADO_FILTRADO_V80.jsonl`
(157 filas, orden de archivo, sin sorteo). **LA VARA NUEVA DE LA CADENA**
(`scripts/loop/vuelta80_vara_cadena.py`, reusando la maquina de
`docs/loop/_auditor_v79_atajo.py`) se corrio sobre las 30 unidades de cabeza,
marcando cada una ALCANZABLE o no ANTES de leer, **sin apartar ninguna por
si sola** (el acta 79 lo dejo escrito: alcanzable no es lo mismo que
encadenado): de las 30, **15 tenian camino previo ya alcanzable**, y la
lectura de cada una verifico explicitamente si ese camino era la cadena
propia de la madre antes de decidir (seccion 5.3).

### 5.3. Lectura de las primeras 30 unidades, con el criterio adjudicado

Dossier completo en `docs/loop/SALIDA_V80_TRAMO6_DOSSIER30.txt`.

**VEINTE de las 30 unidades YA ESTABAN DECIDIDAS por vueltas anteriores de
esta misma campana** (reaparecen en la cabeza de la bolsa porque nunca se
escribieron, o porque se revirtieron hoy mismo, y siguen pasando el filtro
`P.9.1`): se citan sin re-derivar.

| # | par | decidido en |
|---:|---|---|
| 0 | `clasificacion_tipos_activos -> tipos_de_pasivos` | tramo 4, vuelta 78: gemelo estructural falso |
| 1 | `proceso_llamada_inicial_venta -> proceso_venta_franquicias` | tramo 4, vuelta 78: direccion inversa |
| 2 | `equipo_customer_development -> customer_development_team` | tramo 4, vuelta 78: veredicto B puesto 637 |
| 3 | `extraer_priorizar_hipotesis -> value_proposition_startup` | TAREA 3.1, vuelta 79: revertida |
| 4 | `preparacion_preguntas_problema_precall -> preguntas_situacion` | tramo 4, vuelta 78: hermanas SPIN |
| 5 | `timing_solicitud_referidos -> fase_adopt_ciclo_cliente` | tramo 4, vuelta 78: direccion al reves |
| 6 | `requisitos_numericos_calidad_lotes -> critica_acceptable_quality_level` | D5 disuelto, TAREA 1.3, vuelta 79 |
| 7 | `hipotesis_relacion_clientes_web -> mvp_alta_fidelidad` | tramo 5, vuelta 79: mismatch de fidelidad |
| 8 | `producto_mercado_fit_motores -> afinar_motor_crecimiento` | **TAREA 3.1 de ESTA vuelta: revertida (D2)** |
| 9 | `valor_intangible_sostenibilidad -> compromiso_cliente_sostenibilidad` | tramo 5, vuelta 79: tematico, no procedimiento |
| 10 | `analisis_valor -> customer_needs_spreadsheet` | tramo 5, vuelta 79: no toca costos |
| 11 | `posicionamiento_vs_competidores -> analisis_competencia_franquicias` | tramo 5, vuelta 79: veredicto D puesto 2097 |
| 12 | `organizacion_interna_exportacion -> estructura_plan_exportacion` | tramo 5, vuelta 79: coincidencia lexica |
| 13 | `errores_comunes_fundraising -> confidencialidad_nda_adquisicion` | tramo 5, vuelta 79: reglas opuestas |
| 14 | `mvp_catalogo_tecnicas -> mvp_tipo_video` | tramo 5, vuelta 79: veredicto D puesto 384 |
| 15 | `reporte_estado_miembro_equipo -> variance_analysis` | tramo 5, vuelta 79: no cabe en un paso |
| 16 | `terminologia_clave_breakthrough -> analisis_sintomas` | **TAREA 3.2 de ESTA vuelta: revertida (D3)** |
| 17 | `evaluacion_actitudes_empleados -> identificar_oportunidades_sostenibilidad` | tramo 5, vuelta 79: mismatch de objeto |
| 18 | `pre_control_estadistico -> limites_de_especificacion_vs_limites_de_control` | tramo 5, vuelta 79: contraste, no procedimiento |
| 19 | `posicionamiento_por_tipo_de_mercado -> resegmentacion_mercado_nicho_bajo_costo` | tramo 5, vuelta 79: paso previo, no la accion |

**Las 10 restantes son lectura fresca de esta vuelta.** Ninguna traia
veredicto propio salvo la marcada abajo:

| # | par (paso senalado) | alcanzable previo (vara de la cadena) | decision |
|---:|---|---|:---:|
| 20 | `control_calidad_operaciones_servicio -> descubrir_necesidades_del_cliente` (paso 1) | si, 6 saltos, incidental | **NO SE ENLAZA** |
| 21 | `el_riesgo_nunca_se_acaba_se_administra -> cuando_el_riesgo_se_vuelve_realidad` (paso 2) | si, 6 saltos, incidental | **NO SE ENLAZA** |
| 22 | `curva_caracteristica_operativa -> distribucion_binomial` (paso 2) | no | **SE ENLAZA** |
| 23 | `abolir_inspeccion_masiva -> eliminacion_inspeccion_masiva_por_control_estadistico` (paso 5) | no | **NO SE ENLAZA** (veredicto D, puesto 2560) |
| 24 | `recursos_apoyo_gubernamental_exportacion -> trabajo_con_bancos_comerciales` (paso 3) | no | **NO SE ENLAZA** |
| 25 | `definiciones_operacionales_de_calidad -> optimizacion_caracteristicas_diseno` (paso 1) | no | **NO SE ENLAZA** |
| 26 | `desarrollo_de_controles_de_proceso -> bucle_retroalimentacion_control` (paso 2) | no | **SE ENLAZA** |
| 27 | `descubrir_necesidades_del_cliente -> traduccion_necesidades_cliente` (paso 2, redirect a paso 6) | no (no es cadena propia) | **DISCUTIBLE, NO SE ENLAZA** |
| 28 | `qfd_matriz -> identificar_clientes_externos_e_internos` (paso 2) | si, en direccion inversa | **NO SE ENLAZA** (direccion equivocada) |
| 29 | `analisis_variacion_desempeno_servicio -> pre_control_estadistico` (paso 4) | no | **NO SE ENLAZA** |

**LA VARA NUEVA DE LA CADENA EN ACCION, EL CASO QUE LA JUSTIFICA:** el par 27
es el ejemplo exacto que la vara existe para atrapar: el calibrador senalo
el paso 2, pero el que calza de verdad es el paso 6 de la MISMA madre
(*"traducir las necesidades priorizadas al lenguaje tecnico"*, casi palabra
por palabra el proposito del hijo). **Es la misma especie de redirect de
paso que produjo D2**, revertida en la TAREA 3 de esta misma vuelta. La vara
de la cadena por si sola NO lo descarta (el camino existente pasa por
`customer_needs_spreadsheet`, que no es paso de esta madre, asi que no es
"cadena propia"), pero la lectura, con el error de D2 fresco, prefiere la
cautela: la familia ya tiene un camino establecido mas especifico
(`identificar_clientes_externos_e_internos -> customer_needs_spreadsheet ->
traduccion_necesidades_cliente`) para la misma transicion. **NO SE ESCRIBE**,
queda discutible para la relectura del auditor (seccion 5.5).

**LAS DOS ARISTAS SANAS ESCRITAS:**

1. `curva_caracteristica_operativa -> distribucion_binomial`: paso 2 nombra
   LITERALMENTE la distribucion binomial como uno de tres metodos
   (Poisson, binomial, hipergeometrica); el hijo ES el procedimiento
   completo de esa distribucion especifica. Madre conserva materia propia en
   los otros 4 pasos. Sin camino previo (huerfano de camino).
2. `desarrollo_de_controles_de_proceso -> bucle_retroalimentacion_control`:
   paso 2 es la linea literal ("disenar el bucle de retroalimentacion"); el
   hijo ES ese bucle completo, con procedimiento propio de 5 pasos. Madre
   conserva materia propia en los otros 5 pasos. Sin camino previo.

**LAS SIETE NO ESCRITAS, con razon**, escritas en
`scripts/loop/vuelta80_tramo6_escribir.py` y citadas en la tabla de arriba
(paso 20, 21, 23, 24, 25, 28, 29). **Y LA UNA DISCUTIBLE, tambien no
escrita** (paso 27).

**LA TABLA SE CUENTA DE SU FICHERO**, escritura en
`docs/loop/SALIDA_V80_TRAMO6_ESCRIBIR.txt`:

| clase | cuantos de las 10 frescas | que se hizo |
|---|---:|---|
| **JERARQUIA SANA (9.6.2)** | **2** | arista escrita en `nodos_siguientes` Y `nodos_previos` a la vez |
| **NO ESCRITOS, con razon** | **7** | sin arista, razon citada arriba |
| **DISCUTIBLE, no escrito por cautela** | **1** | sin arista, marcado para la relectura del auditor |

**Chequeo de escalera, exacto**, sobre las 2: **cero de 2**, verificado por
corrida independiente (`docs/loop/SALIDA_V80_TRAMO6_ESCALERA.txt`, "en
siguientes de madre: True" y "en previos de hijo: True" para las dos, cero
inversas).

**Gate 0 el ciclo entero, tras las 2 escrituras**
(`docs/loop/SALIDA_V80_GATE0_CMD1_TRAMO6.txt`, `_ETIQUETAS_`, `_SYNC_`): OK,
3.853/3.188/665, 0 auto-aristas, 0 duplicadas de titulo, 0 divergentes;
motor **25/25** (`SALIDA_V80_MOTOR_TRAMO6.txt`); web **80/1.030/3**
(`SALIDA_V80_WEB_TRAMO6.txt`); tsc **exitcode 0, cero lineas**
(`SALIDA_V80_TSC_TRAMO6.txt`). Aristas: **8.960/8.939/17.899/9.583**
(`SALIDA_V80_CONTEO_TRAMO6.txt`), que **vuelven al valor de la apertura de
esta vuelta**: menos 2 de la TAREA 3, mas 2 de este tramo, cero neto. **No es
casualidad sospechosa: es la aritmetica exacta de dos reversiones y dos
escrituras en la misma vuelta**, declarada para que no se lea como un
recomputo que no corrio.

### 5.4. `docs/plan/PASO_NODO_CALIBRADO.jsonl`, sellado y restaurado

Verificado con `git status --short` antes y despues de la corrida del
calibrador: **sin diferencia** tras `git checkout --
docs/plan/PASO_NODO_CALIBRADO.jsonl` (el fichero tracked vuelve exactamente
al commiteado en `2e040cb6`, vuelta 78). La bolsa filtrada de esta vuelta
(157 filas) SI queda commiteada, como en las vueltas anteriores.

### 5.5. Discutibles de la lectura, marcados AQUI antes de saber si aciertan

1. **`descubrir_necesidades_del_cliente -> traduccion_necesidades_cliente`,
   NO ESCRITA POR CAUTELA.** El paso que calza de verdad (paso 6, no el 2
   que senalo el calibrador) coincide casi palabra por palabra con el
   proposito del hijo, y la madre conserva materia propia de sobra en los
   otros cinco pasos: por contenido solo, pasaria 9.6.2. Se decidio NO
   escribir por ser la misma especie de redirect de paso que D2 (revertida
   hoy mismo en esta vuelta) y porque la familia ya tiene un camino
   establecido mas especifico
   (`identificar_clientes_externos_e_internos -> customer_needs_spreadsheet
   -> traduccion_necesidades_cliente`) para la misma transicion. **Vale que
   el auditor confirme si la cautela fue correcta o si fue demasiado
   conservadora**: a diferencia de D2, aqui NO hay una cadena propia de la
   madre que la vara nueva pueda nombrar (el camino existente pasa por un
   nodo que no es paso de esta madre), asi que el caso no es identico al de
   D2, solo de la misma FAMILIA de error.
2. **`curva_caracteristica_operativa -> distribucion_binomial`, ESCRITA.**
   El paso nombra TRES metodos (Poisson, binomial, hipergeometrica) y solo
   uno queda enlazado hoy. No es el mismo problema que D2 (no hay cadena
   previa, es huerfano de camino puro), pero merece que quede senalado por
   si una vuelta futura lee Poisson o hipergeometrica desde esta misma
   madre y hace falta revisar consistencia de patron (como el par
   `establecimiento_capacidad_proceso -> pruebas_destructivas /
   control_estadistico_de_procesos` del tramo 5, dos hijos legitimos para
   el mismo paso).

---

## 6. EL CIERRE, medido AL CIERRE

Commits de esta vuelta que cierran TAREA 1 a 5:
`d2f6b524` (TAREA 1), `038ebcd0` (TAREA 2), `c25403a0` (TAREA 3), `04c0e4c5`
(TAREA 4), `3d4800e0` (TAREA 5); este reporte se cierra en un commit
posterior que solo anade este mismo fichero.

La tabla de cabecera de la seccion 0 de arriba **es** la medicion de cierre
(columna derecha), tallada con `python scripts/loop/tallar_cabecera_reporte.py
--fase04 --vuelta 80` sobre `SALIDA_V80_*_CIERRE.txt` (copiados identicos de
`SALIDA_V80_*_TRAMO6.txt`, que es el estado final tras la TAREA 5, la ultima
operacion de codigo de esta vuelta; misma convencion que la vuelta 79).

**Verificacion `--comparar` de esta misma cabecera contra este fichero,
corrida DESPUES de pegar la tabla**, salida en
`docs/loop/SALIDA_V80_COMPARAR_CIERRE.txt`: `python
scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 80 --comparar
docs/loop/REPORTE.md` da **7 filas cotejadas, 0 DISTINTAS, 0 ausentes,
"CABECERA: IDENTICA AL TALLADOR"**.

Cifras adicionales que el tallador de fase04 no cubre, contadas de su
fichero:

| | medido con |
|---|---|
| aristas nuevas escritas esta vuelta | **2** (TAREA 5) |
| aristas revertidas esta vuelta | **2** (TAREA 3: D2 y D3) |
| pares leidos y no enlazados esta vuelta (tramo 6, con razon) | **7** |
| discutibles no escritos esta vuelta | **1** |
| pares ya decididos citados sin re-derivar | **20** |
| operaciones cerradas esta vuelta | 0 |
| correcciones declaradas esta vuelta | 2 (1.2 en `REPORTE.md`; la de la TAREA 3 en `docs/plan/04_ENLACES.md`, cubre D2 y D3 juntas) |
| bolsa de `OP-E-01` restante sin leer (filtrada por P.9.1 ensanchado + guarda, esta vuelta) | **127 de 157** (157 filtrados menos las 30 unidades leidas) |

---

## 7. LOS DISCUTIBLES MARCADOS, para la relectura ciega del auditor

Los dos discutibles de la seccion 5.5 (arriba): la cautela sobre
`descubrir_necesidades_del_cliente -> traduccion_necesidades_cliente` (no
escrita, redirect de paso de la misma familia de error que D2), y la
cobertura de un solo metodo (binomial) de los tres que
`curva_caracteristica_operativa` nombra en su paso 2.

---

## 8. PENDIENTES DE DOCTRINA

**Ninguno nuevo.** Las seis adjudicaciones del acta 79 (seccion 1.3 de este
reporte) se resolvieron todas por cita: cuatro cerradas directamente por el
auditor, dos (D2 y D3) resueltas en la TAREA 3 de esta vuelta con el caso
del auditor confirmado contra el grafo.

---

## 9. LO QUE QUEDA PENDIENTE PARA LA VUELTA SIGUIENTE

- Continuar `OP-E-01` con un TRAMO 7, recalibrando la bolsa antes de leer
  (regla EL INSTRUMENTO MANDA: no reusar
  `PASO_NODO_CALIBRADO_FILTRADO_V80.jsonl`, el grafo se movera otra vez con
  las 2 aristas de este tramo), con el filtro `P.9.1` ensanchado, la guarda
  del par no dirigido y la vara nueva de la cadena ya incorporadas de forma
  permanente al flujo de filtrado.
- Los dos discutibles de la seccion 5.5 esperan la relectura ciega del
  auditor, en especial si `descubrir_necesidades_del_cliente ->
  traduccion_necesidades_cliente` debio escribirse.
- `OP-E-02` sigue CERRADO (vuelta 76), sin cambio.
- `OP-E-03` sigue esperando a que `OP-E-01` termine entero.
- `OP-M-03-ENLACES`, `OP-E-04`, `OP-E-05`, `OP-M-01-ESLABONES` y
  `OP-M-01-SEXTO` siguen esperando a la fase 06 (remision escrita, no se
  tocan).
- `OP-E-06` y `OP-E-07` siguen libres de bloqueo de dependencia pero esperan
  su turno en el orden escrito.
- Las diez aristas de la fase 04 que la vara de los A sigue tocando (acta
  78, seccion 1.8; sin remedir esta vuelta) quedan como observacion, no como
  parada: ninguna operacion las condena hoy.
- Los 149 pares del grafo escritos en los dos sentidos y el desbalance
  644/623 entre las dos vistas (acta 79, seccion 3.2) siguen como
  observacion medida, sin remedir esta vuelta: no son de esta fase.

Commitea y pushea lo pendiente en la rama activa antes de tocar nada (esta
vuelta: hecho al cierre de cada tramo, y de nuevo al cierre de este mismo
reporte). Cero guiones largos y cero guiones medios. El hook corrio en cada
commit sin saltarse. No se adivino nada que no se pudiera medir.
