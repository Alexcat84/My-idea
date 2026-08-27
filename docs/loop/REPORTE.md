# REPORTE DE LA VUELTA 88 (EJECUTOR)

Rama `pasada-unica`. Fase III, EJECUCION, modo de ejecucion continua. Sobrescribe
el reporte de la vuelta 87. Apertura sellada ANTES de la primera operacion en
`docs/loop/SALIDA_V88_HEAD_APERTURA.txt`: `e6dc63a0` (el acta de la vuelta 87).
Cierre recomputado AL CIERRE. ESTA VUELTA NO ESCRIBIO NINGUNA ARISTA: el grafo
de cierre es identico, digito por digito, al de apertura.

## CABECERA TALLADA (--fase04 --vuelta 88), pegada entera

Comando: `python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 88`
Salida completa en `docs/loop/_v88_cabecera_tallada.txt`, EXIT 0.

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.188 / 665 | **3.853 / 3.188 / 665** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 8.996 / 8.975 / 17.971 / 9.619 | **8.996 / 8.975 / 17.971 / 9.619** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+0 / +0 / +0 / +0** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 2 fila(s): `juran_rcca_metodo -> diseno_implementacion_remedio`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **2 fila(s): `juran_rcca_metodo -> diseno_implementacion_remedio`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `e6dc63a0` (ACTA DE LA VUELTA 87 DEL AUDITOR, leido de git log), HEAD real de apertura `e6dc63a0` (sellado por el ejecutor antes de la 1.a operacion), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, commit del acta `e6dc63a0` (ACTA DE LA VUELTA 87 DEL AUDITOR, leido de git log), HEAD real de apertura `e6dc63a0` (sellado por el ejecutor antes de la 1.a operacion), arboles de `dataset/` IGUALES: VERDE** |

**LA CABECERA ES IDENTICA APERTURA CONTRA CIERRE EN TODAS LAS CELDAS SALVO LA
FILA DE ARISTAS MOVIDAS (+0/+0/+0/+0).** Es lo esperado: la TAREA 2 concluyo que
la clase de la unidad 117 SE SOSTIENE (no se revierte ninguna arista) y la
TAREA 5 es medicion pura (cero aristas de `OP-E-06` escritas). El sha256 del
`master_graph.json` es el mismo en apertura y en cierre
(`6ea239641964f43a76d179721f6e5fc40b0422bf5e1ea3785fd2ee3987f2cd9f`,
`docs/loop/_v88_apertura_sha_grafo.txt` y `docs/loop/_v88_cierre_sha_grafo.txt`),
verificado con `hashlib.sha256` en Python, no solo con el hash que imprime
`sync_assets_web.py`.

El ciclo de tres (Gate 0, `etiquetas_de_cara.py --aplicar`, `sync_assets_web.py`)
se corrio completo en la apertura y otra vez completo en el cierre; las 71
etiquetas que "cambian" en cada corrida de `etiquetas_de_cara.py` no mueven el
`master_graph.json` final (es idempotente sobre el arbol de hoy). **DISCUTIBLE
DE PROCEDIMIENTO, marcado para la relectura:** en un punto intermedio de la
apertura corri `run_phase1.py --reaplico-curaduria` una SEGUNDA vez, fuera de
ciclo, para "confirmar" el Gate 0; eso revirtio las 71 etiquetas (`git diff`
mostro 72 lineas cambiadas) porque `--reaplico-curaduria` y
`etiquetas_de_cara.py --aplicar` no conmutan. Lo detecte con `git status`, lo
revertí con `git checkout --` y rehice el ciclo completo desde cero
(Gate 0 -> etiquetas -> sync), verificado limpio. Ese error de manejo NUNCA
llego a commitearse (`git status --porcelain -- dataset/ web/lib/assets/` dio
cero lineas antes de cualquier commit de esta vuelta) pero lo declaro porque
por poco publico una cifra de apertura equivocada. Volvi a caer en el MISMO
error al medir el cierre (corri `run_phase1.py --reaplico-curaduria` solo, sin
etiquetas ni sync, como "paso 1 del cierre") y lo corregi de la misma manera
antes de tallar nada.

---

## TAREA 1: LOS REGISTROS DEL ACTA 87, SIN REMEDIR

### 1.1. Las dos caidas de reporte de la vuelta 87 (viven SOLO en `REPORTE.md`, no mueven dato)

Medidas por el auditor, acta de la vuelta 87, secciones 3.1 y 3.2. Se registran
aqui por su nombre, sin volver a medirlas:

1. **La cifra declarada irreproducible que si se reproduce.** El reporte de la
   vuelta 87 escribio que "esa cifra [192 de `OP-E-06`] no se puede reproducir
   con lo que hay en el repositorio hoy". El auditor la reprodujo en una linea
   desde `docs/plan/COSECHA_RAZONES_D.jsonl` (397 filas, 293 nuevos, 192 con
   otra senal, reparto por dominio identico al de la ficha). Es caida de
   REPORTE: la premisa (el script no imprime la cifra) es cierta, la
   conclusion (no se puede reproducir) es falsa, y sobre esa conclusion se
   apoyaba una PARADA.
2. **"LA TABLA, pegada entera" con dos celdas escritas a mano.** La fila de
   `OP-E-02` llevaba "(sin dependencias; ya HECHA desde antes)", un texto que
   la salida del instrumento no traia. Es CIERTO (medido en el campo `nota`),
   pero tapaba un `AMBIGUA` real del propio instrumento (que hoy arreglamos en
   la TAREA 3).

**Racha de REPORTE: pasa a UNO. La parada pide TRES.**

### 1.2. La caida de CLASE de la vuelta 87 (unidad 117): registrada como ABIERTA hasta la TAREA 2

El auditor discrepo en la clase de `juran_rcca_metodo ->
diseno_implementacion_remedio` (acta de la vuelta 87, seccion 2.1). Queda
registrada aqui como abierta y pendiente de la relectura conjunta, sin darla
por buena ni por caida (esa decision es la TAREA 2, mas abajo). **Racha de
CLASE O CIFRA PUBLICADA: UNO antes de la TAREA 2. La parada pide DOS.**

### 1.3. Las diez adjudicaciones de la seccion 6 del acta de la vuelta 87, citadas por numero, sin remedir

- **6.1**: el 117 va a relectura conjunta (resuelta en la TAREA 2 de este
  reporte).
- **6.2**: la tabla tallada se talla entera o no se llama tallada; si al
  ejecutor le falta una celda, se anade AL INSTRUMENTO; un `AMBIGUA` se
  declara, nunca se rellena a mano (aplicada en la TAREA 3).
- **6.3**: los tres defectos del instrumento de la TAREA 5 (vuelta 87) se
  arreglan, cada uno con su caso rojo (aplicada en la TAREA 3 de este
  reporte).
- **6.4**: la parada de `OP-E-06` se levanta, no es parada.
- **6.5**: la re-base de `OP-E-06` es tarea de medicion y va antes de su
  apertura (aplicada en la TAREA 5 de este reporte).
- **6.6**: el "192 con direccion explicita" de la ficha queda marcado como
  cifra heredada y no verificada, sin corregirse todavia; prohibido publicar
  "192" como si fueran 192 aristas seguras (respetado: la TAREA 5 publica 129
  como cifra re-basada, y deja el 192 viejo delante, sin borrar).
- **6.7**: la marca de discutible vale por lo que aparta, no por acertar el
  motivo.
- **6.8**: la vara de la cadena se publica con su veredicto, no solo con su
  columna (aplicada en la TAREA 2: la correccion en `04_ENLACES.md` explica
  POR QUE la cadena propia no mata, no solo contesta SI/NO).
- **6.9**: `OP-C-05` es una casilla "a verificar" y no se da por buena
  (resuelta en la TAREA 4 de este reporte: NO EXISTE como guarda).
- **6.10**: el horneado doble y la celda de unidades nuevas quedan
  ratificados (adjudicaciones 5.2 y 5.3 del acta 86); sin efecto en esta
  vuelta, que no toca el horneado de `OP-E-01`.

---

## TAREA 2: LA RELECTURA CONJUNTA DE LA UNIDAD 117 (BLOQUEANTE)

Commit propio: `970713d6`. Instrumento propio:
`scripts/loop/vuelta88_tarea2_relectura_117.py`, salida en
`docs/loop/SALIDA_V88_TAREA2_RELECTURA_117.txt`.

### 2.a. Las seis aristas del camino, verificadas contra el grafo

Las seis aristas del camino que el acta de la vuelta 87 publico
(`juran_rcca_metodo -> definicion_problema_moms_2 -> analisis_sintomas ->
formulacion_teorias_causa -> prueba_teorias_causa_raiz ->
evaluacion_alternativas_solucion -> diseno_implementacion_remedio`) **ESTAN
LAS SEIS**, verificadas hoy leyendo `dataset/nodos/*.json` directo (no el acta),
en las DOS vistas (`nodos_siguientes` del origen y `nodos_previos` del
destino), los siete nodos **vivos** (`deprecado` ausente o `false` en los
siete). NO HAY HALLAZGO en 2.a: el camino que el auditor midio existe tal
como lo describio.

### 2.b. La pregunta de la vara (adjudicacion 6.1 del acta 83): ¿es la cadena propia de la madre?

**MI RESPUESTA: NO LO ES.**

La vara, citada por su letra (banco 9.6.1, CAVEAT MEDIDO): la cadena cuenta
como cableado establecido (mata la arista) **"si los hijos estan encadenados
en el orden que la madre enumera"**; **"si estan sueltos alrededor de la
madre, se cuentan los radios"** (alcanzabilidad, no cadena), y contra la
alcanzabilidad la arista sigue faltando (huerfana).

De los cinco nodos del camino que preceden al hijo, CUATRO son pasos
literales de `juran_rcca_metodo` en su propio orden
(`definicion_problema_moms_2` su paso 1; `analisis_sintomas`,
`formulacion_teorias_causa` y `prueba_teorias_causa_raiz` los tres, su paso
2, leido de `pasos_accionables` y verificado con el instrumento). **UNO no lo
es**: `evaluacion_alternativas_solucion` no aparece en ninguno de los cuatro
pasos de la madre. Por la letra de 9.6.1 ese nodo esta "suelto alrededor de la
madre", y un camino con un tramo suelto no es la cadena que la madre enumera:
es alcanzabilidad.

**El precedente sostiene esta lectura.** El par 55 (discutido en la acta del
auditor de la vuelta 84, no en la 82 como el encargo de esta vuelta lo cito;
declaro la discrepancia de cita y no la resuelvo copiando: verifique la
ubicacion con `grep` sobre `docs/loop/ACTA_AUDITOR.md`, linea 26743)
sobrevivio como NO cadena propia por DOS motivos escritos juntos: la
direccion iba al reves, **Y** el camino pasaba "por dos nodos de gobernanza
que la madre no enumera". El segundo motivo, solo, es el que aplica al 117:
no hace falta que la direccion falle para que un nodo suelto rompa la
cadena. Los pares 66, 91 y 100 (cadena propia que si mata) no tienen ningun
nodo suelto en su camino: los dos nodos de cada uno de esos tres caminos son
pasos de la madre.

### 2.c. No aplica

La clase NO cae (ver 2.b): no hay recomputo de grafo, registro ni cifra
final.

### 2.d. La razon se reemite en los dos sitios donde vive

**LA CLASE SE SOSTIENE: `SE ESCRIBE` queda.** La razon se reemite, sin borrar
la vieja (correccion declarada):

- `docs/plan/04_ENLACES.md`, apartado `OP-E-01, CIERRE MEDIDO`: se anadio un
  bloque "CORRECCION DECLARADA (28 ago 2026, vuelta 88)" despues de la tabla
  de la cola final, explicando por que el camino NO es la cadena propia de la
  madre y citando los precedentes por numero.
- El campo `nota` de `OP-E-01` (`id_op` en `OPERACIONES.jsonl`), con un
  ADDENDUM fechado que resume el mismo hallazgo y remite a `04_ENLACES.md`
  para el detalle.

La cifra final de `OP-E-01` (220 / 99 / 121) **no cambia**: la arista ya
estaba escrita con la clase correcta, lo que cambiaba era la razon.

**DISCUTIBLE, marcado para la relectura ciega:** esta es una lectura fresca,
no una repeticion de un precedente identico. El nodo suelto
(`evaluacion_alternativas_solucion`) esta a UN salto del hijo, no en medio de
la cadena de pasos de la madre; alguien podria argumentar que un nodo suelto
"casi al final" pesa distinto que uno "en medio". Lo mido como el mismo caso
(9.6.1 no distingue posicion, solo si el nodo es o no un paso de la madre) y
lo marco discutible por si la vara dice otra cosa.

---

## TAREA 3: EL INSTRUMENTO DE LA TAREA 5 (VUELTA 87) ARREGLADO

Commit propio: `e6402ea2`. Sucesor declarado:
`scripts/loop/vuelta88_tarea3_arreglo_desbloqueo_fase04.py` (el de la vuelta
87 no se toca). Salida completa en
`docs/loop/SALIDA_V88_TAREA3_DESBLOQUEO_FASE04.txt`, pegada por referencia
(no se retallan aqui las diez filas: se citan los casos obligatorios).

**LOS TRES DEFECTOS, CADA UNO CON SU CAUSA MEDIDA:**

1. **(3.a) El respaldo por `nota` nunca disparaba de verdad.** La causa
   medida (no la que el docstring viejo insinuaba): `marca_positiva()` solo
   reconoce CABECERAS markdown (`^#+...`), y el campo `nota` es prosa sin
   cabeceras. Arreglo: `marca_positiva_prosa()`, sin anclaje a cabecera, que
   suma "queda HECHA" y "CIERRE POR DECLARACION" (idioma ya establecido en
   mas de quince notas de `OPERACIONES.jsonl`, verificado con `grep`) a
   "REGISTRO DE OPERACION HECHA". **CASO OBLIGATORIO:** `OP-E-02` sale
   `EJECUTADA`, citando su `nota` (`OPERACIONES.jsonl:nota`), y la tabla se
   regenero sin ninguna celda escrita a mano.
2. **(3.b) `ruta_fase("00_CODIGO")` no encontraba la pagina.** Vive en
   `FASE_0_CODIGO.md`, no en `00_CODIGO.md`. Arreglo: mapa de excepciones.
   **CASO OBLIGATORIO:** corri el lector sobre `OP-C-04` y `OP-C-05`: las dos
   `AMBIGUA`, y ahora es una `AMBIGUA` MEDIDA (el lector SI encuentra y lee su
   seccion en `FASE_0_CODIGO.md`, verificado con `secciones_de()`), no una
   `AMBIGUA` por fallo de ruta. Ninguna de las dos trae cabecera con
   `CERRADA/SELLADA/CIERRE` ni "REGISTRO DE OPERACION HECHA": las dos siguen
   en `LISTA` de verdad.
3. **(3.c) El docstring nombraba solo una ronda.** `OP-D-06` (ronda vieja,
   lectura de seccion entera) y `OP-D-01` (ronda nueva, ventana de
   proximidad) son los DOS ciertos, cada uno de su ronda. El docstring nuevo
   nombra los dos, sin borrar ninguno.
4. **(3.d) Caso rojo inventado.** `scripts/loop/vuelta88_tarea3_caso_rojo.py`:
   sobre una COPIA EN MEMORIA de `02_DESTEJIDOS.md` (nunca escrita a disco),
   con una marca negativa metida dentro de la ventana de proximidad de
   `OP-D-02` (que hoy sale `EJECUTADA`), el lector la voltea a `NO EJECUTADA`.
   Verificado: `git status --porcelain -- docs/plan/` vacio antes y despues
   (`docs/loop/SALIDA_V88_TAREA3_CASO_ROJO.txt`).

**Ninguno de los tres arreglos mueve la tabla de la vuelta 87**: verificado
que ninguna de las diez operaciones de la fase 04 depende de una operacion de
fase `00_CODIGO` (solo `OP-E-06` depende de las `OP-D-*`, todas de fase
`02_DESTEJIDOS`).

---

## TAREA 4: LA CASILLA DE `OP-C-05`, VERIFICADA

Sin commit propio (se commiteo junto con la TAREA 5, `dfe9650a`). Salida en
`docs/loop/SALIDA_V88_TAREA4_ARISTAS_DUPLICADAS.txt`.

**`OP-C-04` SI corre**, medido con mis propios ojos dentro de Gate 0 de esta
vuelta (`docs/loop/SALIDA_V88_GATE0_CMD1_APERTURA.txt`): "Ningun nodo VIVO se
cita a si mismo tras RESOLVER (auto-arista via alias)", valor 0.

**`OP-C-05` NO EXISTE COMO GUARDA. ESTE ES EL HALLAZGO Y VA AL FRENTE.** Busque
en `scripts/run_phase1.py` (los veinte `checks.append` de Gate 0, listados uno
por uno) y en `engine/test_gate_*.py`: ninguno implementa el pseudocodigo de
`OP-C-05` ("ninguna lista de aristas puede tener dos entradas que resuelvan al
mismo destino", `FASE_0_CODIGO.md` linea 141-150). Lo que SI existe es
`scripts/plan/aristas_duplicadas_tras_resolver.py`, un instrumento de SOLO
LECTURA (nunca falla, siempre exit 0, solo imprime un informe) que mide la
MISMA condicion subyacente. Corrido hoy: **935 entradas sobran en 711 nodos**
(476 en `nodos_previos`, 459 en `nodos_siguientes`; 932 son "el id nuevo mas su
alias", 3 son "dos alias del mismo destino"). Por la propia ficha de `OP-C-05`
esto es el estado ESPERADO ("esta guarda se enciende DESPUES del saneo final
[`OP-S-12`]... el grafo de hoy la falla 1.056 veces y eso no es una
regresion"): la cifra de hoy (935) no calza con la de la ficha (1.056) porque
el grafo cambio desde entonces, y lo declaro como diferencia esperada, no como
discrepancia a resolver.

**PENDIENTE DE DOCTRINA (no para hoy: la `verificacion` de `OP-E-06` exige
pasar por esta guarda "al terminar", y hoy no hay ninguna guarda que correr).**
La vuelta 89, cuando abra `OP-E-06` de verdad, va a necesitar decidir una de
dos cosas: (a) escribir la guarda de `OP-C-05` como codigo antes de escribir
la primera arista, o (b) verificar por otra via equivalente que ninguna arista
nueva crea una duplicada tras resolver. No lo decido yo hoy: lo traigo como
pregunta.

---

## TAREA 5: LA RE-BASE DE `OP-E-06`, MEDICION PURA, CERO ARISTAS

Commit: `dfe9650a`. Instrumento propio:
`scripts/loop/vuelta88_tarea5_rebase_ope06.py`. Salida completa en
`docs/loop/SALIDA_V88_TAREA5_REBASE_OPE06.txt`, bolsa re-basada en
`docs/plan/OP_E_06_REBASE_V88.jsonl` (129 filas). **NO SE ESCRIBIO NINGUNA
ARISTA: verificado, `git status --porcelain -- dataset/` vacio en todos los
commits de esta vuelta.**

### 5.a. Los 192 y los 101, tallados (no citados de la ficha)

De `docs/plan/COSECHA_RAZONES_D.jsonl` (397 filas): **293 `nuevo=true`**, de
los cuales **192 con senales distintas de `["continua por la vara"]`**
(candidatos `OP-E-06`) y **101 con exactamente esa senal** (candidatos
`OP-E-07`). Reparto por dominio de los 192, identico a la vara de contraste
del auditor: **core 146, entrega 15, environmental 15, exportacion 12,
franquicias 4.**

### 5.b. Los cuatro frentes del dedupe, sobre el grafo de hoy

| frente | contra que | quita |
|---|---|---:|
| 1 | bolsa `PASO_NODO_CALIBRADO.jsonl` (468 filas hoy, pares madre/hijo no dirigidos) | **0** |
| 2 | pares ya declarados en el campo `aristas_nuevas` de OTRAS operaciones (18 pares extraidos de `OPERACIONES.jsonl`) | **0** |
| 3 | cola de relectura post fusion (7 puestos: 707, 1096, 196, 253, 224, 591, 968) | **0** |
| 4 | pares con arista YA en el grafo de hoy, resolviendo por alias | **16** |

**Medicion de contraste sobre los 192 completos** (no solo el remanente):
ya tienen arista hoy (con alias) **16**; tocan un nodo DEPRECADO **36**; tocan
un id inexistente **0**. La vara del auditor (definicion ESTRICTA SIN ALIAS,
`docs/loop/_auditor_v87_frases_192.txt`) daba **6 / 36 / 0**. **DECLARO LA
DIFERENCIA DE DEFINICION, no la resuelvo copiando**: mi 16 usa resolucion de
alias en las dos puntas (como pide la letra de la `verificacion` de
`OP-E-06`, "resolviendo por alias"); la vara del auditor era deliberadamente
estricta sin alias, como el mismo declaro. El 36 (deprecados) y el 0
(inexistentes) SI calzan al digito con las dos definiciones.

**DISCUTIBLE, marcado para la relectura:** los 36 pares que tocan un nodo
deprecado NO se quitan de la bolsa re-basada (no es uno de los cuatro frentes
oficiales que la `verificacion` nombra). Los dejo dentro porque P.9 exige que
cada arista se escriba con el id RESUELTO al dia de su escritura, y eso ya
cubriria el caso de un endpoint deprecado con sucesor vivo; pero no verifique
uno por uno si los 36 tienen de verdad un sucesor vivo resoluble o si alguno
apunta a un nodo muerto sin alias. Puede que la vuelta 89 encuentre ahi un
quinto motivo de descarte.

### 5.c. La direccion se lee, los descartes se cuentan y se nombran

Con las palabras del acta de la vuelta 87 (madre, hijo, padre, desarrolla,
detalla, "en una linea", procedimiento, cuelga, enumera, menciona, nombra),
sobre los **176** pares que sobreviven a los cuatro frentes (192 menos los 16
del frente 4): **129 CON alguna palabra** (siguen en la bolsa), **47 SIN
ninguna** (se descartan, TODOS nombrados en
`docs/loop/SALIDA_V88_TAREA5_REBASE_OPE06.txt`, incluidos los 5 con la frase
literal "Ninguno enlaza al otro."). **DIFERENCIA DE ALCANCE DECLARADA** contra
la vara del auditor (140 CON / 52 SIN, medida sobre los 192 SIN pasar primero
por los frentes 1 a 4): la aritmetica calza (140 menos 129 = 11, 52 menos 47 =
5, y 11 + 5 = 16, exactamente los que el frente 4 ya habia quitado), asi que
no es una discrepancia: es medir la direccion en un punto distinto del
pipeline (despues del dedupe, no antes), y lo declaro para que no se lea como
un numero que no cuadra.

### 5.d. El resultado

**CIFRA VIEJA (ficha de `OP-E-06`, 12 ago 2026, se deja delante): 192.**
**CIFRA NUEVA (re-basada sobre el grafo de hoy, vuelta 88): 129**, escrita en
`docs/plan/OP_E_06_REBASE_V88.jsonl`. Es esta cifra, no la de la ficha, la que
la vuelta 89 usa para abrir `OP-E-06`.

---

## REPASO DEL ENCARGO, PUNTO POR PUNTO, CON LA VERDAD

- Commitear y pushear lo pendiente antes de tocar nada: **SI** (arbol limpio
  al abrir, verificado con `git status --short`).
- Sello del HEAD de apertura antes de la primera operacion: **SI**,
  `e6dc63a0`, y coincide con el commit del acta 87.
- TAREA 1, los tres registros: **SI**, seccion TAREA 1 de este reporte.
- TAREA 2, relectura conjunta, commit propio antes de cualquier otra cosa:
  **SI**, commit `970713d6`, antes de la TAREA 3.
- TAREA 3, los tres defectos con su caso rojo, commit propio: **SI**, commit
  `e6402ea2`.
- TAREA 4, `OP-C-05` verificada y declarada en verde o rojo: **SI**, ROJO (no
  existe como guarda), con su fichero de salida.
- TAREA 5, re-base medida, cero aristas: **SI**, las cuatro piezas, ninguna
  arista escrita.
- Cabecera tallada con `--fase04 --vuelta 88`, pegada entera: **SI**.
- `--comparar docs/loop/REPORTE.md` da CABECERA IDENTICA: **verificado
  DESPUES de escribir este reporte** (ver seccion siguiente).
- Cero guiones largos y medios: **SI**, verificado con una busqueda de esos
  dos caracteres sobre todos los ficheros nuevos de esta vuelta, cero
  coincidencias.
- Ninguna frase de "no se puede reproducir" ni de comparacion entre tandas
  sin abrir el fichero que la sostiene: **SI**, cada afirmacion de este
  reporte cita su fichero de salida.

---

## VERIFICACION FINAL: `--comparar` CONTRA ESTE REPORTE

Comando: `python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 88
--comparar docs/loop/REPORTE.md`. Corrido DESPUES de escribir este reporte y
ANTES del commit de cierre. Salida en
`docs/loop/SALIDA_V88_COMPARAR_FASE04.txt`: **9 filas cotejadas, 0 DISTINTAS,
0 ausentes. CABECERA IDENTICA AL TALLADOR, EXIT 0.**

---

## PENDIENTES DE DOCTRINA

1. **La guarda de `OP-C-05` no existe** (TAREA 4). La `verificacion` de
   `OP-E-06` la exige "al terminar". Antes de que la vuelta 89 escriba la
   primera arista de `OP-E-06`, hay que decidir si se escribe el codigo de la
   guarda o si se verifica por otra via equivalente.
2. **Los 36 pares de la bolsa re-basada que tocan un nodo deprecado** (TAREA
   5.b): no se decidio si necesitan un quinto frente de dedupe o si P.9 (id
   resuelto al escribir) ya los cubre. Traido como pregunta, no resuelto.

## DISCUTIBLES MARCADOS PARA LA RELECTURA CIEGA (antes de saber si acierto)

1. **TAREA 2.d**: la lectura de que `evaluacion_alternativas_solucion` (a un
   salto del hijo) rompe la cadena propia igual que si estuviera en medio.
2. **TAREA 2.b**: la cita del par 55 en el acta de la vuelta 84 y no en la 82
   como el encargo decia; declarado, no resuelto en contra del encargo.
3. **TAREA 5.b, frente 1**: interpretar "la bolsa de 477 de la fase 04" como
   el fichero `PASO_NODO_CALIBRADO.jsonl` en su estado VIVO de hoy (468
   filas), no como una foto historica de 477 filas que ya no existe tal cual.
4. **TAREA 5.b, frente 2**: interpretar "las aristas ya escritas en otras
   operaciones" como el campo `aristas_nuevas` DECLARADO (aunque la
   operacion no haya corrido), extraido por regex de `id -> id`; podria
   significar solo las YA EJECUTADAS, que front 4 ya cubriria por otra via.
5. **TAREA 5.b/5.c, orden del pipeline**: la direccion se leyo DESPUES de los
   cuatro frentes, no sobre los 192 completos como hizo el auditor; declarado
   en 5.c, pero es una decision de diseno mia y no una repeticion de un
   patron ya adjudicado.
6. **TAREA 4**: declarar que la guarda "no existe" en vez de que "existe pero
   yo no la encontre"; busque en `run_phase1.py` (los veinte checks
   listados) y en `engine/test_gate_*.py`, pero no revise CADA script de
   `scripts/plan/` uno por uno.
