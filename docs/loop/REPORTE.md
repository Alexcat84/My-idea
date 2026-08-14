# REPORTE, vuelta 16 del ejecutor (Sonnet 5)

**FASE II, RECOMPUTO. MODO DE CIERRE: cero reparaciones de nodos, cero operaciones ejecutadas, cero
pares nuevos leidos de la cola.** `dataset/` intacto. `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` intacto
(sigue en 3.388 lineas). La FASE III no se abre y la rama `pasada-unica` no se crea.

**Hash final: `afeb4933`** (push confirmado a `origin/bucle`). Commits de esta vuelta:
`b81919e9` (TAREA 1 puntos 1 a 3) y `afeb4933` (TAREA 1 punto 4 y TAREA 2).

**Rutas tocadas en la vuelta** (`git diff --stat d16c714b HEAD`): `docs/plan/10_INVENTARIO.md`,
`docs/plan/EXPEDIENTE_MESA_UNIDA.md`, `docs/plan/INVENTARIO.jsonl`, `docs/plan/LD_MESA_UNIDA.md`,
`docs/plan/LECTURAS_DIRIGIDAS.md`, `docs/plan/OPERACIONES.jsonl`, `docs/plan/RECOMPUTO_3388.md`, mas
cinco scripts nuevos de solo lectura en `scripts/` (`vuelta16_racimos.mjs`,
`vuelta16_buscar_actos.mjs`, `vuelta16_buscar_actos2.mjs`, `vuelta16_generar_actos.mjs`,
`vuelta16_operaciones_cruce.mjs`). Ninguna ruta en `dataset/`, ninguna en
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` (verificado con `git diff --name-only d16c714b HEAD --
dataset/ docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, vacio). Ninguna operacion se ejecuto, ninguna se creo.

---

## TAREA 1: tres correcciones y el tramo releido al doble (encargo de la vuelta 16)

### 1. La cobertura de los trece racimos, remedida entera con el instrumento corregido

**Instrumento nuevo (`scripts/vuelta16_racimos.mjs`), corregido segun el discutible que causo la caida
de la vuelta 15**: pares posibles de cada nomina vigente, cruzados contra `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`
(la cola) MAS las **65 lecturas dirigidas** de todo el plan (las 11 de la primera tanda de
`LECTURAS_DIRIGIDAS.md`, las 16 de la segunda tanda, las 4 de `LD_ADOPT_ADVOCATE.md`, las 26 de
`LD_MESA_UNIDA.md` y las 8 de `LD_CADENA.md` mas `LD_ACTO_DE_SEIS.md`), con dedupe por pareja de nodos
(no por id de lectura: `LD-62` repite a `LD-36` y `LD-65` repite a `LD-44`, se cuentan una vez) y sin
sumar dos veces una dirigida que ya esta en la cola.

**LA TABLA DE LOS TRECE:**

| racimo | nomina | posibles | cola | dirigidas nuevas | cobertura | clases | cambia |
|---|---:|---:|---:|---:|---:|---|---|
| el efectivo contra la ganancia | 3 | 3 | 3 | 0 | 3 de 3 | 3 A | no |
| la ecuacion de valor | 5 | 10 | 5 | 5 | 10 de 10 | 6 A, 4 D | no |
| el sales roadmap | 6 | 15 | 10 | 0 | 10 de 15 | 6 A, 4 D | no |
| la competencia entre inversores | 5 | 10 | 7 | 0 | 7 de 10 | 7 A | no |
| la junta asesora | 4 | 6 | 5 | 1 (`LD-01`) | 6 de 6 | 4 A, 2 D | no |
| los cuadrantes de mercado | 6 | 15 | 7 | 8 | 15 de 15 | 8 A, 7 D | no |
| build, measure, learn | 8 | 28 | 9 | 0 | 9 de 28 | 9 A | no |
| el compromiso contado tres veces | 3 | 3 | 3 | 0 | 3 de 3 | 3 A | no |
| la seleccion de canal | 5 | 10 | 8 | 2 (`LD-02`, `LD-03`) | 10 de 10 | 9 A, 1 D | no |
| la supervision de la IA | 10 | 45 | 15 | 3 | 18 de 45 | 8 A, 10 D | no (ya corregido en vuelta 15) |
| **la mesa unida de puertas y portafolio** | 17 | 136 | 23 | **31** | **54 de 136** | **23 A, 2 B, 2 C, 27 D** | **SI, de 49 a 54** |
| el racimo del pivote | 7 | 21 | 13 | 0 | 13 de 21 | 4 A, 6 B, 3 D | no |
| la serie de Coleman | 28 | 378 | 41 | 4 (`LD-28` a `LD-31`) | 45 de 378 | 10 A, 3 B, 32 D | no |

**RESULTADO: TRECE de trece racimos verifican identicos a como estaban ANTES de esta vuelta, salvo UNO.**
La unica que cambia es **la mesa unida, de 49 a 54 de 136** (23 en cola mas 31 dirigidas unicas, no 26).
**Las cinco dirigidas que faltaban son `LD-58`, `LD-60`, `LD-61`, `LD-63` y `LD-64`** (de
`LD_CADENA.md` y `LD_ACTO_DE_SEIS.md`, ejecutadas el mismo 12 ago 2026 que las 26 de
`LD_MESA_UNIDA.md` pero en otros dos archivos, y la busqueda de la vuelta 15 no las sumo). **Cuatro de
las cinco son A** (`LD-58`, `LD-60`, `LD-61`, `LD-64`); `LD-63` es D.

**LO QUE MEDI Y NO SE ME PIDIO AFIRMAR, con el dato:** las cuatro A nuevas son internas al lado de las
**puertas** (entre `gates_go_kill_decision_points`, `requisitos_gates_con_dientes`, `estructura_gates`,
`estructura_de_gates` y `sistema_gates_go_kill`); **ninguna cruza la frontera declarada.** Por eso:
**la forma "DOS MITADES con frontera declarada" NO se mueve, y la frase "UN SOLO NODO REPITE con las
puertas" (`gestion_de_portafolio_gates_go_kill`) TAMPOCO se mueve.** Las dos calzan con el dato nuevo, no
se dan por supuestas.

**ARRASTRADO CON TACHADO, sin borrar el 49, en los siete sitios vivos donde estaba escrito** (buscado con
`grep`, no supuesto): `docs/plan/INVENTARIO.jsonl` (entrada de racimo, campo `cobertura` y `nota`),
`docs/plan/10_INVENTARIO.md` (fila de la tabla de racimos), `docs/plan/OPERACIONES.jsonl` (nota de
`OP-M-01`), `docs/plan/RECOMPUTO_3388.md` (tabla de los trece de la vuelta 15 y su parrafo de
resultado), `docs/plan/EXPEDIENTE_MESA_UNIDA.md`, `docs/plan/LD_MESA_UNIDA.md` y
`docs/plan/LECTURAS_DIRIGIDAS.md` (cuarta tanda).

### 2. El bloque humano de la supervision de la IA, corregido a 5 A y 5 D

**Caida del auditor, no del ejecutor** (declarada por el mismo en `docs/loop/ACTA_AUDITOR.md` VUELTA 15
seccion 3). Remedido con instrumento propio sobre `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` (no copiado):
de los cinco nodos del bloque humano (`principio_humano_en_el_loop`, `human_in_the_loop_ia`,
`alineacion_etica_ia_negocio`, `mitigar_falling_asleep_wheel`, `riesgo_sobredependencia_ia`), **7 de los
10 pares posibles estan en cola**: `166` (A), `293` (A), `692` (A), `792` (A), `1.041` (A), `1.496` (D),
`1.541` (D). **Mas las tres dirigidas del bloque, las tres D.** **REPARTO REAL: 10 de 10, CINCO A Y CINCO
D, no siete y tres.** El conteo de diez pares sigue siendo correcto; solo el reparto de clases cambia.
No mueve la forma (sigue MEZCLADO) ni el 18 de 45 del racimo entero (verificado exacto en la seccion 1
de arriba, la unica cifra tocada del racimo entero fue en la vuelta 15).

**Corregido con tachado en los tres sitios vivos, sin borrar el 7A/3D:** `docs/plan/LECTURAS_DIRIGIDAS.md`
(la linea "iban 7 de 10" y la linea "NUEVA FORMA"), la nota de `OP-L-02` en `docs/plan/OPERACIONES.jsonl`,
y `docs/plan/RECOMPUTO_3388.md` (la seccion que cita el bonus de `OP-L-02` de la vuelta 13). En los tres
queda escrito que la caida es del auditor.

**Las otras dos nominas de la misma tanda NO se tocaron**, verificadas y correctas: cuadrantes 15 de 15
con 8 A y 7 D; ecuacion de valor 10 de 10 con 6 A y 4 D (ver tabla de la seccion 1).

### 3. La contradiccion de la nota de `OP-I-01` contra su propio punto 2.d, corregida

La nota de `OP-I-01` decia "los otros cinco sumandos NO dependen del corte del cribado", y el propio
punto 2.d de `RECOMPUTO_3388.md` (TAREA vuelta 15) dice que las **figuras SI dependen del corte**
(los ejemplares internos quedan PENDIENTES DE MEDICION). **No es caida: es etiqueta**, mismo precedente
que el acta VUELTA 4 usa para un error de prosa que no es cifra publicada ni veredicto (no mueve
credito). **Corregido con tachado en `docs/plan/OPERACIONES.jsonl`**: lo que no depende del corte es el
**CONTEO DE FILAS** de los cinco sumandos (53 familias, 19 defectos, 13 racimos, 20 figuras, 10
dominios); el **ESTADO INTERNO** de dos de ellos (los ejemplares de las figuras, el estado de fusion de
las familias) **SI depende del corte**, tal como el propio punto 2.d ya lo decia.

### 4. Registro de las cinco adjudicaciones de `ACTA_AUDITOR.md` VUELTA 15 seccion 6

Registradas cada una donde corresponde, con su cita, en `docs/plan/RECOMPUTO_3388.md` seccion "TAREA
(vuelta 16)": 1) cobertura mesa unida a 54/136; 2) bloque humano a 5A/5D; 3) regeneracion de actos
aprobada y ejecutada, ver TAREA 2; 4) tres cubetas de las 53 familias publicadas; 5) los ejemplares de
las veinte figuras registrados como el ultimo bloque grande de la FASE II (no se mide nada nuevo sobre
ellas esta vuelta).

---

## TAREA 2: la regeneracion de las entradas de tipo `acto`, ejecutada con las cinco condiciones

**Instrumentos**: `scripts/vuelta16_buscar_actos.mjs` y `..._buscar_actos2.mjs` (busqueda de citas),
`scripts/vuelta16_generar_actos.mjs` (generacion de las 335 entradas nuevas) y
`scripts/vuelta16_operaciones_cruce.mjs` (verificacion del metodo de cruce de `operaciones` contra los
221 viejos antes de aplicarlo). Los cuatro de solo lectura salvo la escritura final en
`docs/plan/INVENTARIO.jsonl`.

### a. La busqueda de los 221 nombres viejos por el repo

Barrido de TODO el repo (7.468 archivos): **221 de 221 aparecen**, trivialmente, porque cada `nombre` de
acto ES un id de nodo real y vive en `dataset/`, `packs/`, `engine/`, `web/` y en los jsonl mecanicos del
cribado. Ese barrido no distingue nada. **Barrido acotado a la capa narrativa de planeacion**
(`docs/plan/*.md`, `docs/loop/*.md`, `docs/BANCO_DE_TEXTOS.md`, `docs/plan/OPERACIONES.jsonl`, fuera
`INVENTARIO.jsonl` y los jsonl mecanicos): **81 de 221 citados**, casi todos dentro de la nomina `nodos`
de una operacion o de un expediente de mesa. **Ninguna de las 81 cita al ACTO como objeto de inventario
por su nombre compuesto: todas citan al nodo individual dentro de una nomina mas ancha.** Lista completa
con sitio y conteo en `scripts/_actos_citas_narrativa.json`. Ninguna cita se rompe porque ningun nodo se
borra ni cambia de id.

### b a f. El metodo, y un hallazgo que acota el alcance de (b) y (c)

**Los 221 actos viejos tienen, los 221, exactamente UN componente sucesor en el corte 3.388** (verificado
por contencion de conjuntos contra `RECOMPUTO_3388_COMPONENTES.jsonl`): ninguno se parte, porque las
aristas A solo se agregan. **220 son identicos en tamano; 1 crecio** (`construccion_de_leverage`, de 4 a
5, ya documentado). **Esto vacia la condicion (c) esta vuelta: cero entradas quedan "sin componente
sucesor".** Se declara medido, no se fuerza.

**De las 221 notas viejas, 220 son la MISMA formula mecanica** (22 notas distintas sobre 221 filas, 21 de
ellas puramente mecanicas). **La UNICA nota escrita a mano es la de `formalizar_junta_asesora`**, y viaja
intacta a su sucesora con el corte viejo (2026-08-11) al lado.

**Condicion (a), NADA SE BORRA: las 221 lineas viejas NO se tocan.** Se ANADEN 335 lineas nuevas (una por
componente del corte 3.388) en vez de sobrescribir: lectura mas literal de "no se borra ni una linea del
archivo" que la que proponia el plan original de la vuelta 15 (que planeaba borrar 221 y escribir 335).
**La condicion (a) deroga esa parte del plan viejo.**

**Condicion (d), verificada antes de usarla:** `nombre` = primer id alfabetico de `miembros` en las 221
viejas (221 de 221) y en las 335 nuevas (mismo orden en `RECOMPUTO_3388_COMPONENTES.jsonl`, 335 de 335).
Misma convencion, sin inventar ninguna.

**Condicion (e), nada inventado:** las 335 nuevas llevan la formula mecanica de cobertura mas una linea
de procedencia; las 114 sin antecesor llevan ademas "hueco nombrado, no rellenado"; solo la sucesora de
`formalizar_junta_asesora` lleva prosa, y es la vieja transplantada, no una nueva.

**Condicion (f):** campos mecanicos literales de `RECOMPUTO_3388_COMPONENTES.jsonl`. `operaciones` es el
cruce contra las 69 nominas de `OPERACIONES.jsonl`, **metodo verificado ANTES de aplicarse**:
reproduciendolo sobre los 221 viejos con su propia nomina vieja da **189 de 221 identicos**; las 32
diferencias tienen motivo medido (5 son los mismos cinco actos que cerraron entre el 2.117 y el 3.388 que
ya nombra la nota de `OP-U-01`; el resto son operaciones-hijas creadas despues de que la entrada vieja se
escribiera). **Metodo: union de a) cualquier operacion (de las 44 de 69 con `nodos` poblado) que comparta
al menos un miembro con el componente; b) `OP-U-01` si CERRADO u `OP-U-02` si ABIERTO (universales,
verificado sin excepcion contra las 221 viejas); c) `OP-L-03` si el componente esta en el backlog de 40
actos y 73 pares (recalculado con el metodo de `scripts/loop/backlog_l03_vuelta14.py`, da EXACTAMENTE 40
y 73, identico al adjudicado en la vuelta 14).**

### g. El archivo medido otra vez

| tipo | antes | despues |
|---|---:|---:|
| acto | 221 | **556** (221 viejos intactos mas 335 nuevos) |
| resto (dominio, racimo, familia, figura, defecto) | 115 | 115 |
| **TOTAL** | **336** | **671** |

**EL TOTAL REAL NO ES 450**, y no es por la condicion (c) (cero entradas superadas sin sucesor): es por
la condicion (a). El 450 de la vuelta 15 asumia REEMPLAZO; "nada se borra" lo prohibe. El archivo
ANADE, no sustituye. **323, 336 y 450 siguen escritos, el 671 se suma al lado, sin cuadrar el numero a la
fuerza.**

### h. Las tres cubetas de las 53 familias, sin leer nada

| cubeta | cuantas |
|---|---:|
| CONTENIDAS (un componente entero) | 23 |
| PARTIDAS (repartidas en componentes distintos) | 14 |
| SIN ARISTA A registrada al corte 3.388 | 16 |

Lista completa con nombre en `docs/plan/RECOMPUTO_3388.md` seccion "LAS TRES CUBETAS". **Esto ES el
estado, no la falta de estado.** Si alguna PARTIDA es de verdad dos familias: materia de mesa, no de
recomputo.

**Todo lo de TAREA 2 esta en una seccion nueva al final de `docs/plan/RECOMPUTO_3388.md`, sin reescribir
nada anterior, mas la nota de `OP-I-01` puesta al dia.**

---

## MARCADOR (confirmado, sin cambio: cero pares leidos esta vuelta)

**A 583 (17,2 %), B 89 (2,6 %), C 7 (0,2 %), D 2.709 (80,0 %); n 3.388; cero huecos, cero duplicados**
(sin recomputar esta vuelta: `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` no cambio de tamano, confirmado por
el diff vacio de la seccion de rutas).

**Vara por tramo: NO APLICA esta vuelta.** Cero pares nuevos leidos, cero operaciones ejecutadas.

---

## CORRECCIONES DECLARADAS, todas con tachado sin borrar

1. Cobertura de la mesa unida: 49 de 136 (tachado) a 54 de 136, en siete sitios vivos (ver TAREA 1.1).
2. Bloque humano de la IA: 7 A y 3 D (tachado) a 5 A y 5 D, en tres sitios vivos (ver TAREA 1.2).
3. Etiqueta de la nota de `OP-I-01`: "los cinco sumandos no dependen del corte" (tachado) a "el conteo de
   filas no depende, el estado interno de dos si" (ver TAREA 1.3).
4. Total del inventario: 450 (proyectado, TAREA vuelta 15) se mantiene escrito; se suma 671 (real, TAREA
   vuelta 16), sin reemplazarlo, con su motivo (regeneracion aditiva, no reemplazo).

## PENDIENTES DE DOCTRINA

**Ninguno nuevo esta vuelta.** Las correcciones cuelgan de banco 9.10, 9.21, 9.26, la regla de recomputo
de la FASE II, y el precedente "etiqueta mala no es caida" (acta VUELTA 4). La regeneracion cuelga de la
adjudicacion 6.3 del acta VUELTA 15 con sus cinco condiciones.

---

## DISCUTIBLES MARCADOS, para la relectura ciega del auditor

Marcados ANTES de saber si aciertan.

1. **La lectura de "nada se borra" como ADITIVA (335 lineas nuevas conviviendo con las 221 viejas) en vez
   de IN-PLACE (actualizar las 221 en su sitio con tachado, como el resto de este documento).** Las dos
   cumplen "no se borra texto"; elegi la mas literal ("no se borra ni una linea del archivo") y la mas
   auditable (diff de solo altas), pero duplica informacion: 556 filas de tipo `acto` describen 335
   componentes reales, y un conteo ingenuo de "cuantos actos hay" ahora depende de cual de las dos
   familias de filas se cuente. Si el auditor prefiere la lectura in-place, se revierte y se reescribe.
2. **El campo `operaciones` de las 335 nuevas hereda cualquier incompletud del campo `nodos` de las
   operaciones viejas**: no investigue operacion por operacion si su `nodos` esta completo, tome el
   campo tal cual esta escrito. El metodo se verifico reproduciendo el `operaciones` viejo (189 de 221
   identico, 32 con motivo medido), pero esa verificacion prueba que el metodo es CONSISTENTE con el
   campo viejo, no que el campo viejo este completo.
3. **`docs/plan/10_INVENTARIO.md` no se toco.** Su tabla de actos sigue en 221 al corte 2.117 (11 ago
   2026); con 556 actos vivos en el archivo fuente, queda desactualizada por partida doble (corte y
   cifra). Su propia regla dice que se recomputa entera con el disparador de `08_VERIFICACION`, y
   regenerarla entera es un trabajo de esa escala, no de esta TAREA. Se trae como pregunta.
4. **La medicion de si las cuatro A nuevas de la mesa unida mueven la forma o la nota "un solo nodo
   repite" se hizo con los mismos datos ya escritos en `LD_MESA_UNIDA.md` y `LD_ACTO_DE_SEIS.md` (los
   cinco nodos de la "camarilla de cinco" ya estaban documentados como un acto cerrado por lectura antes
   de esta vuelta); no lei ningun par nuevo para confirmarlo, solo cruce nominas.** Riesgo bajo (la
   frontera puertas/portafolio esta bien definida por nomina), pero declarado.
5. **El barrido de citas del punto (a) usa limite de palabra (`\b...\b`) sobre texto plano**, no un
   parser de jsonl/markdown; si algun archivo cita un `nombre` de acto dentro de una cadena mas larga sin
   separador de palabra (poco probable en ids con guion bajo, pero no verificado caracter por caracter en
   los 7.468 archivos), ese archivo no aparece en la lista de 81.
