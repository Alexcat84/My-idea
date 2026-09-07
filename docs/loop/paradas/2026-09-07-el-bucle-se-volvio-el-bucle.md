# PARADA DEL BUCLE. VUELTA 198, auditor Opus 5 (7 sep 2026)

**EL BUCLE SE DETIENE Y `PROMPT_SIGUIENTE.md` QUEDA VACIO.** La condicion es la
primera de `AUDITOR.md` 4, **doctrina NUEVA necesaria**, por **dos caminos
independientes**, y ninguno de los dos lo puede escribir el bucle porque los dos
tocan reglas tuyas.

**Lo primero, para que no se lea como una parada por avería: la vuelta 197 esta
BIEN. La verifique entera y no encontre ni una sola cifra falsa suya.** Gate 0,
las tres suites, el marcador, las once selladas medidas en bytes, el cotejo de sus
240 pares recomputado por mi desde cero: **todo reproduce**. Se para por lo que
esta escrito, no por lo que salio mal.

---

## 1. POR QUE SE PARA

### `A` EL TOPE DE 80 LINEAS DEL MODO AUSTERO, Y LAS TRES CIFRAS QUE PEDISTE

Es la `P.1` del reporte de la 197 y la `4.6` del acta 197, que encargo las tres
medidas **para que decidieras sobre cifras y no sobre una queja**. Las cifras ya
estan, y **las recompute yo importando el instrumento**:

| vara | que cuenta | `REPORTE.md` de la 197 | el de la 196 |
|---|---|---:|---:|
| **V1 total** | `count(NL)` / `len(split(NL))` | **686 / 687** | **588 / 589** |
| **V2 escrita a mano** | total menos las piezas TALLADAS | **658** | **562** |
| **V3 estrecha** | V2 menos lo que otra regla obliga | **408** | **267** |

**Ni siquiera la vara mas favorable entra: 408 contra 80 son 5,1 veces el tope.**
Y lo que empuja el reporte por encima **no es prosa de acompanamiento**: son la
cabecera tallada, la tabla de tareas, la seccion 4 y la seccion 9, **piezas que
otras guardas exigen**. Las tres salidas posibles **son tuyas y ninguna mia**:
subir el tope, medirlo por la vara estrecha, o recortar de verdad lo que hoy es
obligatorio. **Adjudicar cualquiera seria el bucle reescribiendo una regla tuya.**

### `B` LA SERIE QUE DOBLA SOLA, QUE VA POR 480 Y NO SE DETIENE SOLA

La regla del credito (`AUDITOR.md` 1.2) manda releer el tramo **al doble** cuando
una discrepancia cae **fuera de los discutibles marcados**. La serie medida va
**30, 60, 120, 240, y la vuelta 198 tendria que leer 480 pares**.

**La causa la medi yo, y no es que se lea mal:**

- de los **240** pares de la ultima tanda, **31 llevan el literal `DISCUTIBLE
  MARCADO`**, y **CERO de los 177 que estan por debajo del puesto 2662**;
- **16 de las 25 discrepancias** cayeron en ese tramo, donde quedar *fuera del
  marcado* **es una propiedad del tramo y no un juicio sobre la lectura**.

O sea: **mientras se relea el archivo por debajo del 2662, el credito baja casi
siempre y el tramo se dobla casi siempre.** Eso ya lo levanto el acta 197 como su
hallazgo `5.2` y lo dejo publicado sin resolver. **Yo no lo resuelvo tampoco:
cambiar la regla del credito es doctrina tuya.** Lo que si hago es decir la
consecuencia con su cifra delante: **la vuelta siguiente gastaria su turno entero
en 480 pares de un tramo que ya no discrimina.**

---

## 2. LO QUE ADEMAS TIENES QUE VER, Y ES LO QUE MAS PESA

### `C` DOS REMEDIOS ESCRITOS LLEVAN APAGADOS DESDE LA 197, Y ME LO HICIERON A MI

**Medido, no sospechado:** `docs/loop/SALIDA_V198_GUARDA_MUERTA.txt`, **10 casos,
10 verdes**, con escenario de control al lado.

Desde que la TAREA 2.b de la vuelta 197 dejo `docs/loop/_TURNO_DEL_AUDITOR.json`
con `vivo.abierto: false`, **ningun proceso vuelve a abrir el turno**, porque
`sellar()` no toca ese campo y la unica linea que lo reabre esta en la rama del
fichero **inexistente**. Consecuencia, en dos mitades:

1. **la bitacora deja de acumular entre procesos**, y con eso `sellar()` **ya no
   puede caer en rojo** aunque el turno haya tocado `git log`, `git status` o
   `REPORTE.md`. Ese es el remedio de la **vuelta 193**;
2. **`leer_reporte()` sin `vuelta` no mira el disco y deja pasar**. Ese es el
   remedio de la **vuelta 197**, y el orden que `AUDITOR.md` escribe es
   `leer_reporte()` a secas.

**Yo selle por el CLI, llame a `leer_reporte()` como la doctrina manda, y el modulo
me entrego el reporte con las tablas de discrepancias de mi propio sujeto, sin un
solo rojo.** Los 49 casos de mutacion de la 197 salen verdes porque prueban la
guarda **con la `vuelta` en la mano y sobre un turno que no venia cerrado**; la
sede real la llama **sin `vuelta` y sobre un turno cerrado**.

**No es una caida de cifra de nadie por la letra de hoy, y por eso dejo escrita una
pregunta que NO contesto yo:** el 5 sep decidiste que **una ruta que promete prueba
sobre un vacio cuenta como cifra publicada**. **Una guarda que se publica como
mordiendo y no muerde engana igual, o mas.** Si quieres que cuente, hay que
escribirlo, y no lo escribo yo porque **ademas moveria una racha a mi favor**.

**UN ALCANCE QUE DIGO YO:** `docs/loop/_TURNO_DEL_AUDITOR.json` esta en `.gitignore`,
asi que **es estado local de esta copia de trabajo**. En un clon nuevo no existe y las
dos guardas si muerden. **No rebaja el agujero** (el bucle corre siempre aqui, y aqui
el fichero existe y esta cerrado desde la 197), pero **la reparacion hay que probarla
sobre un turno CERRADO**: en una maquina limpia sale verde sin haber medido nada.

### `D` LA CAMPANA NO SE ESTA MOVIENDO, Y SON COMMITS, NO UNA IMPRESION

| que | ultimo movimiento | cuanto hace |
|---|---|---|
| `docs/plan/OPERACIONES.jsonl` | `28c5a5dc`, 4 sep 2026 | **293 commits**, y desde entonces corrieron las vueltas **170 a 197** |
| `dataset/` | `a34328b2`, vuelta **148**, 2 sep 2026 | **489 commits** |
| `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` | `b8c2b5cc`, vuelta **187** | **una fila** |

La vara del trabajo pendiente, corrida por mi hoy
(`scripts/loop/vuelta150_3_relectura_expediente.py --corte HEAD`, exit 0), dice lo
mismo que lleva vueltas diciendo: **71 fichas, 37 que no calzan, 6 en LISTA sin
ninguna prueba, 4 de trabajo real, y `OP-L-02` sin documento que medir.**

**Lo digo sin adorno y sin proponerte nada, porque el alcance de la campana es
tuyo: veintiocho vueltas seguidas de guardas sobre guardas con el plan quieto.**
Cada vuelta reciente escribe arneses que vigilan los arneses de la anterior, y la
nomina de la bateria **crece sin techo por regla propia** (135 entradas hoy). El
trabajo del bucle se volvio **el bucle**.

---

## 3. EL ESTADO EXACTO, MEDIDO HOY

- **rama** `pasada-unica`, **HEAD** `ca8e7ba9` al empezar mi turno. **Fase III.**
- **marcador**, por `AP.marcador()` y sellado en
  `docs/loop/SALIDA_MARCADOR_AUDITOR_V198.json`: **3388 filas; A 551, B 72, C 5,
  D 2760**, **0 huecos y 0 duplicados**. El cribado esta **completo en 3.388**.
- **Gate 0**: **26 controles en OK, 0 en rojo**. **motor 25/25. tsc exitcode 0.
  web 82 ficheros y 1040 tests, todos pasando.**
- **censo** 3853 nodos, 3169 vivos, 684 deprecados. **aristas** 8780 / 8740.
- `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`: **4054129 bytes**, `sha256`
  `0a77b5a35a962621`. **No se movio en la vuelta 197.**
- **serie de registros**: 51 entradas, **siguiente libre `R.60`**, 0 colisiones,
  0 huecos. El acta 198 **todavia no esta registrada**: la registra la vuelta que
  reanude.
- **proxima vuelta de bateria: la 199**, por la cadencia de cinco desde la 194.
- **nada quedo a medias**: `dataset/`, `web/` y `engine/` cierran con **0 filas**
  de `git diff --numstat` tras correr yo el ciclo entero de Gate 0.

---

## 4. LO QUE NECESITO DE TI

**Cuatro decisiones. Las dos primeras desbloquean el bucle; las otras dos lo
enderezan.**

1. **EL TOPE DE 80 LINEAS.** Subirlo (y a cuanto), medirlo por la vara estrecha,
   o recortar lo que hoy es obligatorio. **Con las tres cifras del punto `A`
   delante.**
2. **LA SERIE QUE DOBLA.** Tres formas, y la tercera es la que yo elegiria si
   fuera mia: (a) dejarla como esta y leer 480; (b) que una discrepancia en un
   tramo **sin marcado** no cuente como *fuera del marcado*, porque ahi la
   comparacion no existe; (c) poner un techo a la serie y que el exceso se
   declare en vez de doblarse. **Cualquiera de las tres es una linea tuya.**
3. **LA GUARDA QUE PROMETE PROTECCION Y NO MUERDE**, del punto `C`: ¿cuenta como
   **cifra publicada** igual que la ruta que promete prueba?
4. **EL ALCANCE**, del punto `D`: si el bucle sigue puliendo sus propias guardas o
   vuelve al plan. **Es tuya entera y no la sugiero.**

---

## 5. COMO RETOMAR

**Contesta los cuatro puntos en un fichero de decision** (el patron de la casa:
`docs/loop/paradas/2026-09-XX-<asunto>-DECISION.md`) **y relanza.** El encargo de
la vuelta que reanude **ya esta decidido y no hace falta que lo pienses tu**: lo
adjudique yo y lo dejo escrito aqui para que la parada no se lo lleve por delante.

**TAREA 1, BLOQUEANTE Y DE CODIGO: LAS DOS GUARDAS APAGADAS DEL PUNTO `C`.**
Sobre `scripts/loop/apertura_del_auditor.py`, que **no se clona**: (a) que un turno
nuevo **reabra** el turno al sellar, o que `_cargar_turno()` no deje el fichero
marcado como cerrado para siempre; (b) que `leer_reporte()` **mire el sello en
disco tambien sin `vuelta`**, que es como la doctrina manda llamarla. **Cada mitad
con su caso rojo que MUERDA**, y el arnes tiene que fallar **sin** el remedio y
pasar **con** el, corriendo en **procesos distintos** y sobre un turno **cerrado**,
que es donde los 49 casos de la 197 no miraban.
**Mi arnes ya esta escrito y corrido:** `scripts/loop/_auditor_v198_guarda_muerta.py`.

**TAREA 2, BLOQUEANTE Y CON FECHA: EL ARNES QUE BORRA LA SEDE DEL TURNO.**
`scripts/loop/vuelta182_tarea2_mutacion_apertura_auditor.py` llama a
`AP.olvidar_todo()` **seis veces** contra el modulo real **sin redirigir
`AP.RUTA_DEL_TURNO`**, asi que **borra `docs/loop/_TURNO_DEL_AUDITOR.json` cada vez
que corre**. Es la `P.2` del reporte de la 197 y la adjudique a favor de repararlo:
**no es podar una guarda, es aplicarle la misma leccion que la 193 le aplico a
`olvidar_todo()` y la 194 al arnes de la 192**. **Tiene fecha porque la 199 es
vuelta de bateria** y la bateria corre esa nomina entera.

**TAREA 3: LOS EJEMPLARES DEL BANCO SALEN DEL UNIVERSO DE LAS CIEGAS.** Es la
`P.3` del reporte, adjudicada por mi **por extension de la `4.4` del acta 197**: el
banco nombra sus ejemplares **con puesto y clase**, y la doctrina que se manda citar
**entrega la respuesta**. Le paso al ejecutor con el `1077` y **me paso a mi con el
`165`**. La lista se **computa del banco**, no se teclea, y entra en
`aislador_de_ciega.py` por el carril `--excluir` que ya existe.

**Y una cosa que NO esta encargada y que solo tu puedes soltar:** la nomina de la
bateria **no se poda sin ti**, y hoy son 135 entradas que se corren dos veces cada
cinco vueltas.

---

## 6. MI PROPIA CAIDA, PARA QUE NO TE LA CUENTE OTRO

**Corri `git log` y `git status` en la terminal ANTES de sellar**, con `AUDITOR.md`
ya leido. La bitacora no los vio porque no pasaron por el modulo, **asi que mi sello
salio verde igual**: la guarda no puede impedirlo y la regla dice que hacerlo es una
decision, no un descuido. **Lo que vi fueron asuntos de commit y el sujeto no se
quemo por ahi** (lo quemo el reporte, por el agujero del punto `C`), pero la caida
es mia y esta en el acta con su nombre. **Y hay una segunda:** teclee dos cifras en
mi propio fichero de clases (dije 60 puestos y son 59, y un reparto que no era el
que sale de contarlos). **Las cazo mi propio cotejo y quedan escritas sin borrar lo
viejo.**

**Todo lo de arriba esta en `docs/loop/ACTA_AUDITOR.md`, acta de la vuelta 198,
lineas 69636 en adelante.**
