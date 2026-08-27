# REPORTE DE LA VUELTA 95 (EJECUTOR)

Rama `pasada-unica`. Fase III, fase 04 ENLACES, modo de ejecucion continua.
Sobrescribe el reporte de la vuelta 94. Apertura: HEAD `325f537c5fe7676882eb7e0c50df54e8c5751430`,
sellado con `git rev-parse HEAD` ANTES de la primera operacion
(`docs/loop/SALIDA_V95_HEAD_APERTURA.txt`), commit del acta de la vuelta 94
DEL AUDITOR. Cierre recomputado AL CIERRE, sobre el arbol final (HEAD `220c07a18f3395a9e75222a2e1cee0262141a3b9`).

**ESTA VUELTA EJECUTA EL ENCARGO DE LA VUELTA 95** (`docs/loop/PROMPT_SIGUIENTE.md`,
que ejecuta el acta de la vuelta 94, `ACTA_AUDITOR.md` lineas 32888 a 33354):
la TAREA 2 (BLOQUEANTE, la escalada de codigo) nace el tallador
`tallar_barrido_cifras.py` y se repara la fila de identidad de
`tallar_cabecera_reporte.py`; la TAREA 1 deja los cuatro registros en
`docs/PENDIENTES.md`; la TAREA 3 reconstruye el cribado de cita de linea y
lee las 18 filas del grupo C (11 quedan, 4 a relectura conjunta, 3 ya
resueltas sin releer, CERO retiradas); la TAREA 4 hace las tres de higiene;
la TAREA 5 se para deliberadamente, sin intentarla, con su razon escrita.
**Ninguna caida de clase ni de cifra publicada esta vuelta. La racha de
reporte, que el acta 94 subio a DOS DE TRES, vuelve a CERO** (ninguna caida
de reporte se detecto en esta vuelta, ni en discutibles ni fuera de ellos).

## CABECERA TALLADA (--fase04 --vuelta 95), pegada entera

Comando: `python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 95`.
Salida completa en `docs/loop/SALIDA_V95_CABECERA_TALLADA.txt`, **EXIT 0**.
Antes del commit de cierre, `--comparar docs/loop/REPORTE.md` se corre otra
vez sobre este mismo fichero ya escrito (seccion "LA COMPARACION FINAL", mas
abajo).

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.188 / 665 | **3.853 / 3.188 / 665** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 9.190 / 9.169 / 18.359 / 9.813 | **9.190 / 9.169 / 18.359 / 9.813** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+0 / +0 / +0 / +0** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 1 fila(s): `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **1 fila(s): `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `325f537c` (ACTA DE LA VUELTA 94 DEL AUDITOR, leido de git log), HEAD real de apertura `325f537c` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, commit del acta `325f537c` (ACTA DE LA VUELTA 94 DEL AUDITOR, leido de git log), HEAD real de apertura `325f537c` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE** |

**LA FILA DE IDENTIDAD YA NO ES UN LITERAL** (TAREA 2.b de esta vuelta): la
celda "sellado antes de la 1.a operacion" sale ahora de
`procedencia_sello_apertura()`, que busca en `git log --diff-filter=A` el
commit que anade `SALIDA_V95_HEAD_APERTURA.txt` y compara su padre contra el
hash sellado. Esta vuelta es el primer caso REAL que la ejercita (el sello
si se escribio antes de la primera operacion), y el resultado calza con los
dos casos obligatorios probados en la TAREA 2.b (ver abajo).

**CERO ARISTAS SE MOVIERON**: ninguna tarea de esta vuelta toco `dataset/`
ni `web/`. Las celdas de apertura son copia literal de las de cierre de la
vuelta 94, por el CRITERIO NUEVO de la adjudicacion 2.2 del acta de la
vuelta 94: `git diff --stat a4c89ab6 325f537c -- dataset/ web/lib/assets/
scripts/` da CERO lineas (los tres arboles son byte identicos), verificado
en esta vuelta con `git rev-parse <commit>:<ruta>` sobre los tres commits y
las tres rutas (ver commit `220c07a1`). El cierre se RECOMPUTO igual, con
corrida propia completa: motor (25/25), Gate 0 (OK), aristas (identicas), web
(80/1030+3), tsc (limpio), desfase (identico). `git diff --stat` de
`dataset/` y `web/lib/assets/` contra el commit de apertura, corrido DESPUES
de todas las mediciones de cierre, da CERO lineas.

**MANEJO PROPIO DECLARADO, sin dato movido:** la primera corrida de
`scripts/run_phase1.py` para medir el cierre se hizo SIN `--reaplico-curaduria`
y dejo `dataset/metadata/master_graph.json` con un diff transitorio (72
etiquetas de "cara" recompiladas a su forma sin curar). Se completo el ciclo
de tres (`etiquetas_de_cara.py --aplicar`, `sync_assets_web.py`) y se
verifico `git diff --stat -- dataset/ web/lib/assets/` VACIO antes de seguir
con cualquier otra medicion. No quedo ningun cambio sin commitear ni ningun
dato movido por el descuido.

## TAREA 1: LOS CUATRO REGISTROS

Escritos en `docs/PENDIENTES.md`, seccion "VUELTA 95, TAREA 1": (a) la caida
de reporte del "8 aciertos" con su medicion re confirmada (14 filas, 11 y 3,
`docs/loop/SALIDA_V95_TAREA1A_COMPOSICION_V94.txt`) y la CORRECCION
DECLARADA con la cifra real de la TAREA 2.a (18 aciertos, 9 con salvedad, 9
sin); (b) las cuatro adjudicaciones del acta 94 (2.1 a 2.4) con sus lineas;
(c) el cribado de cita de linea (grupo A 57, B 9, C 18) con los cuatro
caidos y el 1083 confirmado, los cinco en C; (d) la caida propia del
auditor (`_auditor_v93_grafo.py`), registrada con el mismo trato que las del
ejecutor.

## TAREA 2 (BLOQUEANTE): LA OPERACION DE CODIGO DE LA ESCALADA

**(a) `scripts/loop/tallar_barrido_cifras.py`, nace.** Corre el barrido el
mismo (no lee la salida de texto de un barrido ajeno) y talla composicion
por fichero mas con/sin salvedad dentro de una ventana de 200 caracteres.
Probado por mutacion sobre `tiene_salvedad()` (la unica pieza de juicio) en
`scripts/loop/vuelta95_tarea2a_prueba_mutacion_barrido.py`: VERDE, entrada
normal True, entrada mutada (misma cadena sin la frase de salvedad) False.
Corrido sobre el barrido rehecho de la vuelta 94 (mismas raices y patrones,
`docs/plan,docs/BANCO_DE_TEXTOS.md` y `85 ESCRITA,87 con direccion,cifra
vigente`): **18 aciertos totales** (por ocurrencia del patron, no por linea
de grep), **14 en `04_ENLACES.md`, 3 en `OPERACIONES.jsonl`, 1 en
`03_FUSIONES.md`; 9 con salvedad, 9 sin**
(`docs/loop/SALIDA_V95_TAREA2A_BARRIDO_TALLADO.txt`). CORRECCION DECLARADA
del "8 aciertos... 7 mas 1" en `docs/PENDIENTES.md`, sin borrar la frase
vieja. DISCUTIBLE: el conteo por ocurrencia (no por linea) y la inclusion de
`OPERACIONES.jsonl` son decisiones de diseno declaradas en el docstring del
instrumento.

**(b) `tallar_cabecera_reporte.py`, la fila de identidad reparada.** Ya no
imprime el literal incondicional "(sellado por el ejecutor antes de la 1.a
operacion)": `procedencia_sello_apertura()` busca con `git log
--diff-filter=A` el commit que anade `SALIDA_V<N>_HEAD_APERTURA.txt` y
compara su padre contra el hash sellado. Los dos casos obligatorios calzan
exacto: vuelta 93 (`docs/loop/SALIDA_V95_TAREA2B_CASO_V93.txt`) da "sellado
antes de la 1.a operacion" (padre de `f73adb67` es `85a250be`, el mismo
sello); vuelta 94 (`docs/loop/SALIDA_V95_TAREA2B_CASO_V94.txt`) da "sello
RECONSTRUIDO DESPUES (commit a4c89ab6)" (padre de `a4c89ab6` es `4c22a083`,
NO `267365c8`). Las cabeceras ya publicadas de las vueltas 92 a 94 NO se
retocan.

## TAREA 3: EL CRIBADO DE CITA DE LINEA, RECONSTRUIDO, Y LA LECTURA DEL GRUPO C

**(a)** `scripts/loop/vuelta95_tarea3a_cribado_cita_de_linea.py` reconstruye
con codigo propio (no el del auditor) el cribado sobre las 84 filas de
`OP_E_07_DIRECCION_V94.jsonl`. Primer intento (patrones mas estrechos): 56/8/20,
DISTINTO del acta. Con dos ajustes linguisticos declarados (numero escrito
en "dice N lineas"; prefijo en vez de palabra exacta para "enumera"/"enuncia")
la reconstruccion da **57/9/18, IDENTICO al acta de la vuelta 94**, misma
enumeracion de B y C (`docs/loop/SALIDA_V95_TAREA3A_CRIBADO.txt`).

**(b) a (f)** `scripts/loop/vuelta95_tarea3_lectura_grupo_c.py` lee las 18
filas del grupo C, pasos primero y razon despues, misma mecanica que el
1009/1281/1992
(`docs/loop/SALIDA_V95_TAREA3_LECTURA_GRUPO_C.txt`). Tres ya resueltos sin
releer (1083 confirmado; 1191 por mandato explicito del encargo; 1886 por el
acta de la vuelta 93, `ACTA_AUDITOR.md` linea 32695). De las 15 restantes:

- **QUEDAN (11): 896, 909, 910, 940, 983, 993, 1020, 1057, 1086, 1196,
  1220.** Todos anclan a UN paso, fase o linea concreta de un nodo que el
  otro desarrolla entero (formula canonica del banco 9.6.2, `BANCO_DE_TEXTOS.md`
  lineas 1737 a 1793: "UNA LINEA QUE TARDA VARIOS PASOS EN EJECUTARSE...
  ES UN PROCEDIMIENTO NOMBRADO EN UNA LINEA"); el 1220 ademas dice
  literalmente "es la MADRE".
- **RELECTURA CONJUNTA, duda genuina (4): 886, 890, 947, 1844.** Los cuatro
  comparan una clase entera de un nodo contra lo que el otro "no tiene" o
  "asume", sin anclar a un paso, fase o linea unica y numerada: el mismo
  patron que hizo salir al 1098, 1009, 1281 y 1992. NO resueltos solo.

**CERO ARISTAS RETIRADAS esta tarea**: resultado legitimo y explicito del
encargo ("cada una se decide por su razon", "el grupo C no es una lista de
condenados"), no falta de trabajo.

**DISCUTIBLE marcado:** mi primer barrido de este mismo grupo, con un
criterio mas estricto (exigir la palabra literal "madre"), habria dado ONCE
candidatos a SALIR en vez de cuatro. Me aparte de ese criterio porque
contradecia la advertencia explicita del encargo y porque el precedente de
la vuelta 93 sobre el 1886 ya usaba el ancla-a-un-paso (no la palabra
literal) como prueba suficiente. Traigo la duda entera en vez de resolverla
sola.

## TAREA 4: LAS TRES DE HIGIENE

**(a)** `04_ENLACES.md` fila 11: intervalo cerrado ("desde la vuelta 93
hasta la vuelta 94"), remite a la fila 12 con la cifra vigente actual (82
ESCRITA + 2 YA_ESTABA). **(b)** `vuelta91_tarea4_direccion_ope07.py`, entrada
1992: anotado "SUPERADO por la TAREA 3 de la vuelta 94", sin borrar el
comentario original. **(c)** recuperado el ensayo de agosto pisado (387
filas, commit `88b3f7c6`) a `docs/plan/DIFERENCIA_CONTRA_COLA_ENSAYO_AGOSTO.jsonl`,
con la decision documentada en `diferencia_contra_cola.py`.

**El SyntaxWarning citado NO se reproduce**, discrepancia declarada
(EJECUTOR.md regla 2, "EL INSTRUMENTO MANDA"): corri
`scripts/loop/vuelta94_tarea4_reparar_marca_hijo.py` fresco por tres vias
(import con `warnings.filterwarnings('error', ...)`, `compile()` sobre el
fuente, `python -W always::SyntaxWarning`) y ninguna produce advertencia. El
fichero tiene un solo commit en toda su historia (`d1d88d1a`) y ese commit
YA trae `r"""` en su docstring principal. No se toco el fichero.

## TAREA 5: PARADA DELIBERADA

Las tareas 1 a 4 cerraron en verde. Lei la nota de `OP-E-03` en
`OPERACIONES.jsonl`: la lectura pendiente es el juicio COMPLETO A/B/C/D del
banco 9.6.1 mas direccion (9.6.2) para pares NUEVOS, no la pregunta mas
estrecha de la TAREA 3 (si una razon YA ESCRITA nombra la madre). Abrir 40
pares nuevos con ese juicio completo, en la misma vuelta y despues de cuatro
tareas ya densas, es la lectura apurada que "no adivines" prohibe. Parada
registrada en `docs/PENDIENTES.md` con lo que queda listo para la vuelta que
la tome (verificacion de cinco puntos y bolsa vigente de 183 filas, ya
escritas).

## EL MARCADOR Y LA TASA POR DOMINIO

**NO SE TOCAN esta vuelta** (ninguna tarea llego a mover una clase D ni un
veredicto del cribado intra-dominio): el marcador vigente sigue siendo el de
la vuelta 94, **A 551 / B 72 / C 5 / D 2.760**, sin remedir (no hay
instrumento de esta vuelta que lo produzca; se cita el de la vuelta 94 por
identidad de arbol, mismo criterio de la cabecera). La tasa por dominio del
banco 9.27 tampoco se mueve: la lectura del grupo C de OP-E-07 es
DIRECCION, no cribado intra-dominio, y sus veredictos (11 quedan, 4 a
relectura, 3 ya resueltos) se cuentan aparte, como manda `OP-E-07.verificacion`.

## PENDIENTES DE DOCTRINA

Ninguno nuevo esta vuelta.

## RUTAS TOCADAS (commits `b0d8c4ae` a `220c07a1`)

`scripts/loop/tallar_barrido_cifras.py` (nace),
`scripts/loop/vuelta95_tarea2a_prueba_mutacion_barrido.py` (nace),
`scripts/loop/tallar_cabecera_reporte.py` (reparado),
`scripts/loop/vuelta95_tarea3a_cribado_cita_de_linea.py` (nace),
`scripts/loop/vuelta95_tarea3_lectura_grupo_c.py` (nace),
`scripts/loop/vuelta91_tarea4_direccion_ope07.py` (anotado),
`scripts/plan/diferencia_contra_cola.py` (docstring),
`docs/plan/04_ENLACES.md` (fila 11 cerrada),
`docs/plan/DIFERENCIA_CONTRA_COLA_ENSAYO_AGOSTO.jsonl` (nace, recuperado de
`88b3f7c6`), `docs/PENDIENTES.md` (cinco secciones nuevas), mas los
`docs/loop/SALIDA_V95_*` de apoyo. **CERO ficheros de `dataset/` o `web/`
tocados** (verificado por `git diff --stat` vacio, citado arriba).

## LA COMPARACION FINAL

`python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 95
--comparar docs/loop/REPORTE.md`, corrido DESPUES de escribir este fichero y
ANTES del commit de cierre; su salida se pega en el commit de cierre de
esta vuelta.

## LOS DISCUTIBLES MARCADOS, para la relectura ciega del auditor

1. **La cuenta del barrido nuevo (TAREA 2.a): 18 aciertos por OCURRENCIA del
   patron, no por linea de grep, y con `OPERACIONES.jsonl` incluido** (que
   la salida vieja de la vuelta 94 no mostraba, aunque el `grep -rn
   docs/plan/` original ya lo barria). Es una decision de diseno del
   instrumento nuevo, declarada en su docstring, pero cambia la unidad de
   medida frente a la practica de "contar lineas de grep" de las vueltas
   anteriores.
2. **Los 4 de RELECTURA CONJUNTA de la TAREA 3 (886, 890, 947, 1844)**: el
   criterio que uso (ancla a un paso/linea concreta, no la palabra literal
   "madre") es el mismo que el precedente del 1886 (acta 93), pero es MI
   aplicacion de ese criterio a 15 razones nuevas, y con un criterio mas
   estricto el resultado habria sido muy distinto (11 SALEN en vez de 4 a
   relectura). Traer la duda es la regla, pero el limite entre "duda
   genuina" y "aplicacion insuficientemente firme del criterio" es mio.
3. **El SyntaxWarning no reproducido (TAREA 4)**: declaro que no lo
   encuentro por tres vias distintas, pero no descarto una diferencia de
   entorno (version de Python, locale de Windows) que mi corrida no capture.
4. **La herencia de apertura por el criterio 2.2**: es la primera vez que
   una vuelta completa este ciclo (diff de tres rutas corrido y citado,
   cierre recomputado igual) desde que el criterio se escribio; si el
   criterio en si tiene un hueco no previsto, esta es la vuelta donde se
   veria primero.
