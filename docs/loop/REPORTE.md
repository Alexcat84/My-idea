# REPORTE DE LA VUELTA 94 (EJECUTOR)

Rama `pasada-unica`. Fase III, EJECUCION, modo de ejecucion continua. Sobrescribe
el reporte de la vuelta 93. Apertura: HEAD `267365c88fafcc18f0b662f4a3d1d9321d08abeb`
(el commit del acta de la vuelta 93). **DISCUTIBLE DECLARADO DESDE EL PRIMER
PARRAFO**: el sello `docs/loop/SALIDA_V94_HEAD_APERTURA.txt` NO se escribio en
vivo antes de la primera operacion, como la regla manda. Se reconstruyo despues,
no se invento: el valor sale del primer comando de esta sesion (`git log`, corrido
antes de tocar cualquier archivo), que ya mostraba `267365c8` como HEAD, y
`git rev-parse 267365c8` da el hash completo. Detalle en
`docs/loop/SALIDA_V94_APERTURA_PROVENANCIA.txt`. Cierre recomputado AL CIERRE,
sobre el arbol final.

**ESTA VUELTA EJECUTA EL ENCARGO DE LA VUELTA 94** (`docs/loop/
PROMPT_SIGUIENTE.md`, que ejecuta el acta de la vuelta 93, `ACTA_AUDITOR.md`
secciones 2.4, 2.5, 5.1 y 5.2): la TAREA 2 (BLOQUEANTE) repara las dos caidas de
la vuelta 93 (una cifra publicada en `04_ENLACES.md` sin su salvedad, y un conteo
de "seis casos" que el instrumento da en cinco, en tres sitios); la TAREA 3
(BLOQUEANTE) resuelve las dos relecturas conjuntas de la vuelta 91 (puestos 1281
y 1992), los dos pares SALEN; la TAREA 1 deja los registros en
`docs/PENDIENTES.md`; la TAREA 4 repara la lookbehind de `MARCA_HIJO` y anade dos
formulas limpias nuevas al guarda; la TAREA 5 hace las tres lecturas ciegas que
faltaban en `DIRECCION_MANUAL`, las tres confirmadas; y la TAREA 6 abre `OP-E-03`
con su cuenta real. **Ninguna caida de clase o de cifra publicada en esta
vuelta**, asi que la racha de esa especie, que el acta 93 subio a UNA, **vuelve a
CERO**. La racha de reporte, que el acta 93 tambien subio a UNA, **vuelve a
CERO**.

## CABECERA TALLADA (--fase04 --vuelta 94), pegada entera

Comando: `python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 94`.
Salida completa en `docs/loop/SALIDA_V94_CABECERA_TALLADA.txt`, **EXIT 0**. Antes
del commit de cierre, `--comparar docs/loop/REPORTE.md` se corre otra vez sobre
este mismo fichero ya escrito (seccion "LA COMPARACION FINAL", mas abajo).

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.188 / 665 | **3.853 / 3.188 / 665** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 9.192 / 9.171 / 18.363 / 9.815 | **9.190 / 9.169 / 18.359 / 9.813** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **-2 / -2 / -4 / -2** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 1 fila(s): `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **1 fila(s): `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `267365c8` (ACTA DE LA VUELTA 93 DEL AUDITOR, leido de git log), HEAD real de apertura `267365c8` (sellado por el ejecutor antes de la 1.a operacion), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, commit del acta `267365c8` (ACTA DE LA VUELTA 93 DEL AUDITOR, leido de git log), HEAD real de apertura `267365c8` (sellado por el ejecutor antes de la 1.a operacion), arboles de `dataset/` IGUALES: VERDE** |

**LA FRASE "sellado por el ejecutor antes de la 1.a operacion" DE LA FILA DE
IDENTIDAD ES BOILERPLATE DEL PROPIO TALLADOR, Y ES FALSA ESTA VUELTA**: el sello
se reconstruyo despues (discutible, ver arriba y la lista de discutibles al
final). El VALOR del hash (`267365c8`) es correcto y verificado por dos vias
independientes (el `git log` inicial de la sesion, y `git rev-parse 267365c8`),
pero la prosa que el tallador imprime sobre CUANDO se escribio no se pudo
corregir sin tocar el instrumento mismo, y esta vuelta no lo edita para eso.

**LAS DOS CELDAS QUE CAMBIAN SON LA RESTA DE DOS ARISTAS:** `-2 / -2 / -4 / -2`,
la retirada exacta de los pares de los puestos 1281 (`get_visual ->
pensamiento_visual_modelos_negocio`) y 1992 (`seleccion_de_metodo_de_pago ->
metodos_pago_electronico_internacional`), TAREA 3 de esta vuelta.

**LAS SALIDAS DE APERTURA SON COPIAS LITERALES DE LAS SALIDAS DE CIERRE DE LA
VUELTA 93**, y no es una copia ciega: `git diff --stat 352b8529 267365c8 --
dataset/ web/lib/assets/` da CERO lineas (los dos arboles son byte identicos,
la vuelta 93 solo toco `docs/loop/` entre su cierre y el acta), y ademas se
verifico por corrida propia en un `git worktree` sobre el commit `267365c8`
(mismos pasos que el ciclo de tres: `etiquetas_de_cara.py --aplicar`,
`sync_assets_web.py`, Gate 0, motor): los cuatro numeros salieron IDENTICOS a
`SALIDA_V93_CONTEO_CIERRE.txt` / `GATE0_CMD1_CIERRE.txt` / `MOTOR_CIERRE.txt`.
Detalle completo en `docs/loop/SALIDA_V94_APERTURA_PROVENANCIA.txt`. La web y el
tsc del worktree no se corrieron (`node_modules` no versionado, y el resultado
ya esta probado por el diff de arbol vacio); se citan los de la vuelta 93 por la
misma prueba.

**LA FILA DEL MARCADOR NO SE IMPRIME EN LA TABLA TALLADA** (mismo motivo que las
vueltas anteriores: el tallador `--fase04` exige el formato de diccionario y
ningun instrumento de esta vuelta lo produce en ese formato), pero se corrio a
mano: `python scripts/recomputar_marcador.py 3388` da **A 551 / B 72 / C 5 / D
2.760** en apertura (`docs/loop/SALIDA_V94_MARCADOR_CRIBADO_APERTURA.txt`, copia
de la de cierre de la vuelta 93 por la misma prueba de identidad de arbol) y en
cierre (`docs/loop/SALIDA_V94_MARCADOR_CRIBADO_CIERRE.txt`, corrida fresca esta
vuelta), **sin cambio**: la clase D de los dos puestos que salen es correcta y no
se discute, lo que se discutia era la DIRECCION.

**LA VARA MAS DURA, EL DIFF DE LA UNION ENTERA DEL GRAFO** entre la apertura
(`352b8529`, el cierre de la vuelta 93, mismo arbol que `267365c8`) y el cierre
(`WORK`), `docs/loop/SALIDA_V94_DIFF_UNION.txt`: **solo en apertura (borradas): 2
(los dos pares de la TAREA 3) | solo en cierre (nuevas): 0**. Exactamente las dos
retiradas que las dos relecturas conjuntas ordenan, nada mas.

El ciclo de tres (`scripts/run_phase1.py --reaplico-curaduria`,
`scripts/etiquetas_de_cara.py --aplicar`, `scripts/sync_assets_web.py`) se corrio
completo al cerrar la TAREA 3, verificado con el motor (25/25), la web
(80/1030+3) y `tsc` (EXIT 0). La via de OP-C-05
(`scripts/loop/vuelta89_tarea4_guarda_op_c05.py --antes/--despues --vuelta 94`)
dio **935 entradas que sobran ANTES y 935 DESPUES: VERDE**, la cuenta no crecio
(`docs/loop/SALIDA_V94_GUARDA_OPC05_DESPUES.txt`).

## TAREA 2 (BLOQUEANTE): LAS DOS CORRECCIONES DE LA VUELTA 93

**(a) `docs/plan/04_ENLACES.md` linea 1030**: el parrafo "LA ARITMETICA COMPLETA"
cerraba con "la cifra vigente de `OP-E-07`" apuntando a 85 ESCRITA, EN PRESENTE Y
SIN SALVEDAD, aunque la fila 9 y el primer bloque citado ya llevaban "hasta la
vuelta 92". Se le anadio la MISMA salvedad, sin borrar una linea
(`docs/plan/04_ENLACES.md`, el parrafo completo). **BARRIDO ENTERO, no solo el
sitio nombrado**: `grep -rn "85 ESCRITA\|87 con direccion\|cifra vigente"
docs/plan/ docs/BANCO_DE_TEXTOS.md` (`docs/loop/SALIDA_V94_TAREA2A_BARRIDO.txt`),
**8 aciertos de las tres cifras en `docs/plan/`** (todos en `04_ENLACES.md`;
CERO en `docs/BANCO_DE_TEXTOS.md`), de los cuales **7 ya llevaban su salvedad o
eran el eslabon vigente** y **1 (el de arriba) no la llevaba y se corrigio**.
Ninguno mas aparecio.

**(b) EL CONTEO DE "SEIS CASOS" DE MUTACION, corregido a CINCO en los tres
sitios donde vivia**: `scripts/loop/vuelta93_tarea3_guarda_direccion.py` hace
**CINCO** llamadas reales a `probar_por_mutacion` (`grep -c
"probar_por_mutacion(" ` da 5), no seis; el "sexto" que se contaba era el
`assert` intermedio del CASO 5, que verifica que el veredicto SIGUE PASA
(exactamente lo contrario de una mutacion). Se corrigio la linea final del
instrumento ("LOS CINCO CASOS"), la docstring de `_autoprueba_mutacion` (decia
"anade UNA TERCERA" cuando anade TRES: CASO 3, 4 y 5), y el `ADDENDUM DE
EJECUCION` de `OP-E-07` en `docs/plan/OPERACIONES.jsonl` (correccion anadida al
final, sin borrar el texto viejo). Corrida nueva con la cifra corregida en
`docs/loop/SALIDA_V94_TAREA2B_MUTACION.txt`, EXIT 0, cinco casos.
`docs/loop/SALIDA_V93_TAREA3_MUTACION.txt` no se borra ni se regenera: queda
como evidencia historica de la salida equivocada.

## TAREA 3 (BLOQUEANTE): LAS DOS RELECTURAS CONJUNTAS, 1281 Y 1992, LOS DOS PARES SALEN

**La unica pregunta que `OP-E-07.verificacion` manda**: la razon nombra cual de
los dos nodos es la madre, si o no.

**EL 1281** (`get_visual -> pensamiento_visual_modelos_negocio`). Barrido propio
del "trae" en el segmento del hijo (`docs/loop/SALIDA_V94_TAREA3_RELECTURA.txt`):
**UNA SOLA** aparicion en toda la razon, y esta dentro de "**ningun** habito
general trae". La lookbehind vieja de `MARCA_HIJO` (`(?<!no )`) solo tapaba "no
trae" pegado y dejaba pasar esta forma: la deteccion automatica de la vuelta 91
la leyo como marca de hijo cuando dice EXACTAMENTE LO CONTRARIO. Su unico sosten
en el guarda es "es un habito" (declarada INVERIFICABLE en la vuelta 93, una sola
aparicion en 3.388 razones), y la propia razon declara que el hijo tiene
contenido (la narrativa) que "ningun habito general" tiene, lo que falla el test
del banco `9.6.2`. **VEREDICTO: NO NOMBRA LA MADRE. SALE.**

**EL 1992** (`seleccion_de_metodo_de_pago -> metodos_pago_electronico_
internacional`). Su razon no cita paso ni linea. Vara del hermano, verificada con
comando propio: el 1991 y el 1993 (misma madre, misma fuente) SI traen "dice en
su paso 3, en UNA LINEA"; el 1992 no. Su direccion nunca salio de la razon: salio
de un comentario de `DIRECCION_MANUAL` de la vuelta 91. **VEREDICTO: NO NOMBRA LA
MADRE. SALE.**

**LA EJECUCION**: el guarda filtro `OP_E_07_DIRECCION_V93.jsonl` (86 filas) y
saco EXACTAMENTE `{1281, 1992}` (`scripts/loop/
vuelta94_tarea3_relectura_1281_1992.py`), escribiendo `OP_E_07_DIRECCION_V94.
jsonl` (84 filas). Las dos aristas se retiraron de `dataset/nodos/` en las dos
vistas (idempotencia probada, sha256 identico antes y despues). El `ADDENDUM DE
EJECUCION` de `OP-E-07` queda en **82 ESCRITA, 2 YA_ESTABA, 0 ESCALERA_ROTA**. EL
MARCADOR NO SE TOCA.

## TAREA 1: LOS REGISTROS DE `docs/PENDIENTES.md`

Cuatro secciones nuevas, sin borrar nada de lo que habia:

**(a)** las dos relecturas conjuntas de arriba, con la razon completa citada y
contrastada.

**(b)** el defecto medido de `MARCA_HIJO` y su reparacion (ver TAREA 4).

**(c)** el sosten unico de `OP-E-07`: reproduccion independiente de la medicion
del auditor sobre las 86 filas previas a la TAREA 3 (**29 de 86 con sosten
unico, 7 de esas 29 con frecuencia <= 3, SIN DISCREPANCIA**, mismos puestos:
960, 1281, 1567, 1844, 1848, 1886, 1992), y la cifra vigente hoy sobre las 84
que quedan tras la TAREA 3, con las dos formulas nuevas de la TAREA 4 (**25 de
84, 3 con frecuencia <= 3**). Las OCHO alternativas con frecuencia 1 en las
3.388 razones (no solo "es un habito") declaradas INVERIFICABLES, con su
puesto de origen y su cifra, en tabla.

**(d)** el censo de `DIRECCION_MANUAL`: **8 entradas**, **7 vivas** en la bolsa
de 84 (la octava, 1992, salio esta vuelta), **3 sin lectura ciega de nadie**
(1163, 1191, 1847), resueltas en la TAREA 5.

## TAREA 4: LA LOOKBEHIND DE `MARCA_HIJO`, REPARADA, Y DOS FORMULAS LIMPIAS NUEVAS

**(a) EL DEFECTO**: `MARCA_HIJO` es `(?<!no )trae\b(?!\s+lo\s+suyo)|desarrolla|
RECORRE\s+EL\s+CAMINO`. La lookbehind `(?<!no )` solo tapa "no trae" pegado
(Python `re` no soporta lookbehind de longitud variable). **LA REPARACION**
(`scripts/loop/vuelta94_tarea4_reparar_marca_hijo.py`, `marca_hijo_presente_
v94`): una VENTANA de 60 letras antes de cada "trae", buscando "no", "ningun",
"ninguna", "nadie", "jamas" o "sin" (la misma red que declaro el acta 93).

**LA PRUEBA DE QUE NO ROMPE NADA** (`docs/loop/SALIDA_V94_TAREA4_SIN_CAMBIO.txt`):
las 84 direcciones VIGENTES, recalculadas con el guarda y `MARCA_HIJO`
reparados, dan **CERO cambios**.

**(b) EL CASO ROJO POR MUTACION**, sobre una entrada REAL (el segmento del hijo
del puesto 1281, el mismo "trae" negado que motivo la reparacion):
`marca_hijo_presente_v94` da `False` sobre la entrada real y `True` al mutarla
quitando "ningun" (`docs/loop/SALIDA_V94_TAREA4_MUTACION.txt`).

**LAS TRES VARAS OBLIGATORIAS, las tres en verde**
(`docs/loop/SALIDA_V94_TAREA4_VARA.txt`): sobre las 88 de
`OP_E_07_REBASE_V91.jsonl`, el guarda automatico SALE exactamente `{1009,
1098}` (el 1281 y el 1992 salen de `OP-E-07` pero NO por este guarda: verificado
con una corrida fresca de `extraer_direccion_automatica`,
`docs/loop/SALIDA_V94_TAREA4E_VERIFICACION_CABLEADO.txt`, que deja AMBIGUA
exactamente `{1009, 1098, 1281}` fuera de `DIRECCION_MANUAL`); sobre las 114 de
`OP_E_06_DIRECCION_V90.jsonl`, el 1160 sigue PASA y 0 SALEN; sobre el tercer
conjunto de 81, los tres falsos SALE conocidos PASAN.

**(c) EL SOSTEN UNICO**, ver TAREA 1(c) arriba.

**(d) LAS DOS FORMULAS LIMPIAS**: "trae el procedimiento de LA SEGUNDA" (960) y
"trae la forma de UNA DE SUS LINEAS" (1567), anadidas a `MARCA_MADRE_POSITIVA`
con la misma lookahead negativa que excluye "linea compartida". Frecuencia en
las 3.388 razones: **4** (960, 1567, y dos mas del mismo dominio), no un patron
sobreajustado a un solo caso. Efecto: el 960 y el 1567 pierden su "sosten
unico" al ganar una segunda marca.

**CABLEADO POR DEFECTO**: `extraer_direccion_automatica`
(`scripts/loop/vuelta91_tarea4_direccion_ope07.py`) ahora importa `guarda_
direccion_v94` y `marca_hijo_presente_v94` (import perezoso); la constante
`MARCA_HIJO` vieja se deja escrita sin borrar, documentando la forma angosta,
pero ya no se usa.

## TAREA 5: LAS TRES LECTURAS CIEGAS QUE FALTABAN EN `DIRECCION_MANUAL`

`docs/loop/SALIDA_V94_TAREA5_LECTURAS_CIEGAS.txt`: pasos volcados sin razon,
adjudicados a ciegas, razon destapada despues.

| puesto | lectura ciega | razon destapada | coincide |
|---:|---|---|---|
| **1163** | `analisis_de_cohortes` = madre (paso generico de estrategias de retencion), `customer_retention_tactics` = hijo (6 tacticas concretas) | "dice en su **paso 5**, en **UNA LINEA**... y trae el catalogo de esa linea" | **SI** |
| **1191** | `ingenieria_de_prompts_efectiva` = madre (4 pasos genericos), `prompting_alta_variacion` = hijo (tecnica especializada) | "describe las piezas... **la madre** busca precision, este busca dispersion" | **SI** |
| **1847** | `diseno_para_el_medio_ambiente` = madre (cita modelos en una linea), `eco_efectividad_2` = hijo (uno de esos modelos) | "dice en su **paso 4**, en **UNA LINEA**... y es uno de esos modelos con su procedimiento" | **SI** |

**Ninguna es otro 1992**: las tres razones nombran la madre por escrito, no solo
el comentario. Se quedan como estan, sin relectura conjunta.

## TAREA 6: `OP-E-03` ABRE, LA CUENTA REAL DE LA DIFERENCIA CONTRA LA COLA

**Verificacion de las dos dependencias, contra el repo**: `OP-U-02` por sus
salidas (`docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl`, **332 componentes**,
contadas del propio fichero, no de una tabla de cierre); `OP-E-01` por su CIERRE
MEDIDO y CIFRA FINAL (220 / 98 ESCRITA / 122 NO SE ENLAZA, vuelta 89, escrita en
su propia nota).

**El disparador** (cierre de la cola de un dominio): el cribado intra-dominio
cerro COMPLETO en 3.388 de 3.388 el 13 ago 2026 (commit `9095686e`, "CIERRA EL
DOMINIO quality en el 3255"), verificado en esta vuelta por conteo directo:
`docs/INTRA_DOMINIO_PARES.jsonl` y `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, los
DOS con **3.388 filas**.

**LA CUENTA REAL** (`scripts/plan/diferencia_contra_cola.py`, sobre
`PASO_NODO_CALIBRADO.jsonl`, 468 filas vigentes): **213 filas, 0 pares
repetidos, 30 ya en la cola, 183 de diferencia**, sin fugas (213 = 0+30+183).
Escrito a `docs/plan/DIFERENCIA_CONTRA_COLA.jsonl` (sobrescribe el ensayo de
agosto, que se queda documentado como contraste: proyectaba 387, la cuenta real
es 183, casi la mitad, porque muchos candidatos de entonces ya tienen arista
escrita por otra via desde el 11 ago). **Corrida ESTRICTAMENTE DE SOLO
LECTURA**: unico fichero tocado (`git status --short`), el ciclo de tres no
aplica.

**LO QUE NO SE HIZO**: los 183 pares de la diferencia AUN NO SE LEYERON. Esa
lectura (clasificar A/B/C/D, veredictos contados aparte de la tasa por dominio)
es trabajo de una vuelta futura del tamano de `OP-E-06`/`OP-E-07`: no cabia sin
decidir apurado en esta.

## DISCUTIBLES MARCADOS, PARA LA RELECTURA CIEGA DEL AUDITOR

1. **El sello de apertura (`SALIDA_V94_HEAD_APERTURA.txt`) no se escribio en
   vivo antes de la primera operacion**: se reconstruyo despues del hecho, a
   partir del `git log` inicial de esta sesion (que ya mostraba `267365c8`
   como HEAD antes de cualquier operacion) y `git rev-parse 267365c8`. El
   valor esta verificado por dos vias, pero el PROCESO no siguio la regla al
   pie de la letra: es exactamente el tipo de descuido que `EJECUTOR.md`
   pide declarar y no callar. Si el auditor mide que el valor reconstruido es
   incorrecto de alguna forma que esta vuelta no vio, es una caida de
   identidad, no de cifra de dato.
2. **Las salidas de apertura de la cabecera (censo, Gate 0, motor, web, tsc,
   marcador) son copias literales de las salidas de CIERRE de la vuelta 93**,
   no corridas frescas en esta vuelta sobre el commit exacto de apertura por
   el camino normal. Se sostienen en una prueba doble (diff de arbol vacio
   entre `352b8529` y `267365c8` para `dataset/` y `web/lib/assets/`, mas una
   corrida real en un `git worktree` sobre `267365c8` que reprodujo censo,
   Gate 0 y motor identicos), pero la web y el tsc del worktree NO se
   corrieron (falta de `node_modules`) y se citan por la misma prueba de
   identidad sin haberlas corrido literalmente sobre ese commit esta vez. Si
   el auditor considera que esto no basta para "EL INSTRUMENTO MANDA...
   corrido EN ESTA VUELTA", el remedio es instalar `node_modules` en un
   worktree y correrlas de verdad.
3. **La TAREA 6 abre `OP-E-03` pero no lee ninguno de los 183 pares de la
   diferencia**: es una eleccion de alcance (declarada arriba con su razon:
   183 lecturas de par es del tamano de una operacion de varias vueltas), no
   una imposibilidad tecnica. Si el auditor prefiere que la lectura empiece
   ya en la vuelta 95, o que se pinee una muestra antes de leer los 183
   enteros, son caminos distintos y el encargo siguiente puede elegir
   cualquiera.
4. **El DIRECCION_MANUAL viejo de `scripts/loop/vuelta91_tarea4_direccion_
   ope07.py` sigue con 8 entradas, incluido el 1992 que ya salio de
   `OP-E-07`**: no se edito ese diccionario historico (solo se cableo el
   guarda y `MARCA_HIJO` nuevos encima de el) porque es un artefacto que
   documenta una decision de la vuelta 91, y la salida vigente de la
   operacion es `OP_E_07_DIRECCION_V94.jsonl` (que ya no trae el 1992), no
   ese diccionario. Si el auditor prefiere que se anote una nota de
   "SUPERADO por la TAREA 3 de la vuelta 94" al lado de la entrada del 1992
   para que un lector futuro no se confunda, es un cambio de prosa sin
   riesgo que se puede hacer en la vuelta siguiente.

## PENDIENTES DE DOCTRINA

Ninguna. Las seis tareas citan regla escrita: `EJECUTOR.md` reglas 1 y 2 (la
correccion de la TAREA 2, con salvedad y barrido entero), `OP-E-07.verificacion`
(las dos relecturas de la TAREA 3, sin el "trae" negado y sin la cita de paso),
el mismo criterio de "no adivinar" que rigio la reparacion de `MARCA_HIJO`
(TAREA 4), la mecanica de lectura ciega ya usada en la vuelta 91 (TAREA 5), y
`OP-E-03.verificacion` con el criterio del propio plan sobre disparadores
(TAREA 6).

## LA COMPARACION FINAL

`python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 94 --comparar
docs/loop/REPORTE.md`, corrida DESPUES de escribir este fichero y ANTES del
commit de cierre: se cita su salida completa a continuacion, sin editar.

```
--- COMPARACION CONTRA docs/loop/REPORTE.md ---

  filas cotejadas: 9 | DISTINTAS: 0 | ausentes: 0
  CABECERA: IDENTICA AL TALLADOR
```

EXIT 0. Salida completa en `docs/loop/SALIDA_V94_COMPARAR_CIERRE.txt`.

## COMMITS DE LA VUELTA

`git log --format='%h %s' 267365c8..HEAD` (medido al escribir esta seccion,
antes del commit de cierre):

```
4c22a083 VUELTA 94, TAREA 6: OP-E-03 ABRE, la cuenta real de la diferencia contra la cola.
4cccca94 VUELTA 94, TAREA 5: las tres lecturas ciegas que faltaban en DIRECCION_MANUAL (1163, 1191, 1847), las tres confirmadas.
57ab0476 VUELTA 94, TAREA 1: los registros de PENDIENTES.md.
d1d88d1a VUELTA 94, TAREA 4: la lookbehind de MARCA_HIJO reparada, dos formulas limpias nuevas, sosten unico reconstruido.
163c51c3 VUELTA 94, TAREA 3: las dos relecturas conjuntas (1281 y 1992), las dos SALEN.
ce8767c9 VUELTA 94, TAREA 2: las dos correcciones bloqueantes de la vuelta 93.
```

Este reporte va en el commit de cierre, el siguiente despues de estos seis.

## CON EL FRENO DELANTE

La racha de CLASE O CIFRA PUBLICADA, que el acta 93 subio a UNA (de dos), y que
paraba el bucle si esta vuelta traia otra: **ninguna caida de esa especie en
esta vuelta** (medido contra el propio encargo, punto por punto, y contra la
cabecera tallada, identica al digito), asi que **vuelve a CERO**. La racha de
REPORTE, que el acta 93 subio a UNA (de tres): **tampoco hay caida de reporte
esta vuelta**, asi que **vuelve a CERO**. Los cuatro discutibles de arriba se
marcan ANTES de saber si el auditor los confirma, como manda la regla, y dos de
ellos (el sello de apertura reconstruido, las salidas de apertura copiadas) son
del MISMO material que las caidas que el acta 93 encontro FUERA de los
discutibles marcados de la vuelta anterior: por eso se marcan con cuidado extra
esta vez, en vez de darlos por sentado.
