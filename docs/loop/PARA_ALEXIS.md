# PARA ALEXIS. EL BUCLE SE DETIENE EN LA MITAD DE `OP-C-05`

**Escrito por el auditor de la vuelta 151 (2 sep 2026, Opus 5), tras auditar la vuelta 150.**
**`docs/loop/PROMPT_SIGUIENTE.md` queda VACIO.** El acta entera esta al final de
`docs/loop/ACTA_AUDITOR.md`, bajo la cabecera *ACTA DEL AUDITOR, VUELTA 151*.

---

## 1. EL MOTIVO, EN UNA PAGINA

`OP-C-05` es una guarda de **FASE 00 CODIGO**, la fase que el protocolo declara **primera y
bloqueante**. Tiene dos mitades. **La primera esta hecha, verificada y viva en Gate 0.** La
segunda **no se puede escribir sin que tu decidas**, y no por falta de ganas: porque su
propia ficha dice tres cosas que **no pueden ser ciertas a la vez**.

Las tres letras, tal como estan escritas hoy en `docs/plan/OPERACIONES.jsonl`:

| | la letra | de donde sale |
|---|---|---|
| **L1** | *"la guarda falla ante cualquier arista bidireccional SALVO las de la lista blanca"* | su `adjudicacion`, 12 ago 2026 |
| **L2** | *"el grafo saneado por `OP-S-12` pasa en verde"* | su `verificacion`, punto 2 |
| **L3** | *"cada entrada CITA SU LECTURA: una entrada sin su C del 9.22 detras no es una excepcion, es un agujero"* | su `adjudicacion` |

**Y ahora la medicion, hecha por el ejecutor y REPRODUCIDA por mi con instrumento propio**
(`docs/loop/_auditor_v151_opc05.py`, resolucion re escrita desde cero):

  - **153 pares bidireccionales entre nodos vivos en HEAD.**
  - **83 pares en el mergebase con `main` (`36b57d78`)**, o sea **antes de que esta campana
    empezara**. No es un estado que la pasada haya creado.
  - **La lista blanca escrita tiene DOS entradas**, los dos enlaces mutuos de `OP-E-05`.

De ahi salen las dos unicas salidas posibles, y **las dos chocan con una letra distinta de
la misma ficha**:

  - **Encender la guarda tal como esta escrita** pone Gate 0 en **rojo 153 veces sobre el
    grafo ya saneado**. Eso contradice **L2** de frente, y ademas contradice la
    **CORRECCION 14.d**, que dice literal: *"Si una retirada tocase una arista que ninguna
    operacion del plan propuso ni prohibe, esa retirada se para y se trae, no se ejecuta"*.
  - **Meter los 153 en la lista blanca** obliga a escribir **151 entradas sin una sola
    lectura detras**. Eso contradice **L3**, que es justo lo que la lista blanca vino a
    impedir.

**Busque una regla escrita que lo resolviera por extension y no la hay.** La mas cercana es
la **CORRECCION 14**, que refina la vara del banco 9.22 a un **test de lineas con dos
salidas** (dos lineas distintas = enlace mutuo y las dos viven; la misma linea = escalera y
la vuelta se retira). Pero su alcance escrito es *"cuando una fusion colapsa dos aristas
que eran de pares distintos"*, que es una especie mucho mas estrecha que este censo de 153.
**No cubre el caso, y forzarla seria doctrina nueva disfrazada de cita.**

**El ejecutor de la 150 hizo lo correcto: ejecuto la mitad que no pide decidir y trajo la
otra. Yo confirmo la parada y no la resuelvo.**

---

## 2. EL ESTADO EXACTO, MEDIDO HOY Y NO RECORDADO

  - **Rama:** `pasada-unica`. **HEAD:** `4444e1ca`. `origin/pasada-unica` sin ahead ni
    behind. Arbol limpio.
  - **Fase:** III, EJECUCION, modo continuo, regimen completo. **NO hay merge pedido ni
    hecho: el merge es tuyo y solo tuyo.**
  - **Censo:** **3.853 nodos / 3.169 vivos / 684 deprecados**. **Aristas:** `siguientes`
    8.780, `previos` 8.740, suma 17.520, union 9.914, **auto-aristas 0**. Medido por mi en
    cinco refs de la vuelta y **las cinco dan lo mismo**.
  - **Gate 0:** **25 comprobaciones, las 25 en OK, exit 0** (eran 24 antes de esta vuelta;
    la 25 es la primera mitad de `OP-C-05`).
  - **Suites:** motor **25/25**, web **80 ficheros / 1.030 pasadas / 3 saltadas**, `tsc`
    **exit 0 sin una linea**. Las tres corridas por mi hoy.
  - **Marcador del cribado, recomputado por mi desde el archivo:** **3.388 lineas, A 551,
    B 72, C 5, D 2.760**, sin huecos. Cerrado y sin tocar.
  - **Expediente:** **71 fichas, un solo esquema, 18 claves**. **60 en `LISTA`, 11 en
    `HECHA`.** `05_SANEO` cerrada **10 de 10**.
  - **Fase 08:** su **tabla por fase** quedo recorrida entera (VERDE 4 de 8, VERDE PARCIAL
    4 de 8, NO CUMPLE 0). Su **verificacion transversal** sigue abierta y **tres de sus
    cinco puntos piden la credencial del `.env`**, que esta fuera del repo.

---

## 3. LO QUE NECESITO DE TI

### PREGUNTA 1, LA QUE PARA EL BUCLE. `OP-C-05`: cual de las dos letras cede?

Te la traigo con las tres opciones que veo y **sin recomendar ninguna**, porque las tres
caen en lo que la casa te reserva.

  - **(a) LA GUARDA SE ACOTA A LO QUE LA PASADA ESCRIBE.** La mitad de bidireccionales solo
    vigila aristas **nacidas en esta campana**, y los 83 anteriores quedan fuera por ser
    estado previo. **Coste:** hay que escribir el criterio de "nacida en la campana" y
    dejarlo medible. **Gana:** L2 y L3 sobreviven intactas.
  - **(b) LA MITAD DE BIDIRECCIONALES NO SE ENCIENDE, Y SE DECLARA.** `OP-C-05` entrega
    solo su guarda de duplicadas tras resolver, que es la que hace permanente a `OP-S-12`,
    y la otra mitad queda registrada como **no ejecutable con la doctrina de hoy**.
    **Coste:** cambia lo que una operacion del plan entrega. **Gana:** nada se borra y nada
    se inventa.
  - **(c) LA LISTA BLANCA SE SUSTITUYE POR EL TEST DE LINEAS DE LA CORRECCION 14.** La
    guarda deja de preguntar *"esta en la lista?"* y pasa a exigir que **cada par
    bidireccional tenga su veredicto de lectura registrado**. **Coste:** son 153 pares por
    leer, y eso es trabajo de lectura de verdad, no mecanico. **Gana:** una sola doctrina
    para toda la campana.

**Si eliges, el bucle retoma solo. Si prefieres pensarlo, el bucle se queda parado y no se
pierde nada: todo lo verde de hoy esta commiteado.**

### PREGUNTA 2, SECUNDARIA Y DE REGLA. Una cifra falsa dentro del codigo de Gate 0, cuenta?

Encontre una cifra con la unidad cambiada: `SALIDA_V150_2C_SIETE_VERIFICACIONES.txt` y el
comentario de la guarda en `scripts/run_phase1.py` dicen **"307 nodos vivos"** donde lo
medido son **307 destinos sobre 255 nodos vivos**. La cifra **no vive en `REPORTE.md`, ni
en `docs/plan/`, ni en el banco**, que son los tres sitios que tu letra del 13 ago 2026
nombra para la especie CIFRA PUBLICADA. **Por la letra, no acumula para la parada, y asi la
registre.**

**Lo que traigo es la pregunta de regla:** una cifra dentro del **codigo de Gate 0** es mas
duradera que una del reporte, y hoy no tiene casillero. **Debe contar como cifra publicada
a partir de ahora?** No lo decido yo.

---

## 4. COMO SE RETOMA, Y QUE ENCUENTRA EL BUCLE HECHO

Con tu decision de la pregunta 1 escrita en `docs/loop/paradas/`, el proximo auditor abre
la vuelta siguiente con este orden, que dejo ya adjudicado en el acta 151 para que nadie lo
vuelva a discutir:

  1. **REPARAR LAS DOS VARAS QUE SE CUENTAN A SI MISMAS. ES LO PRIMERO Y ES BLOQUEANTE.**
     Lo encontre esta vuelta y esta medido: la pierna **P3** de la relectura del expediente
     y la fila **0 CODIGO** de la tabla por fase **cuentan el papeleo de la propia vuelta
     como prueba de que el trabajo se hizo**. Hoy, sin que nadie toque un nodo, sus
     **58/13/30/67** son **60/11/32/69**, y las dos fichas que el reporte declaro **sin
     ninguna prueba** (`OP-V-01` y `OP-L-01`) hoy tienen una: **el commit que dijo que no
     la tenian**. La reparacion es simple y esta escrita: **el reloj de git se congela en
     el commit anterior al de la propia vuelta**, y lo verifique yo, porque congelandolo
     **las siete cifras del reporte reproducen al digito**.
  2. **RECONTAR CON LA VARA ARREGLADA**, y publicar el recuento con su corte.
  3. **EL PASE DE `estado` DE LAS FICHAS CONGELADAS**, como **un solo acto del auditor con
     el conteo antes y despues** (esta reservado ahi desde el acta 139, 3.6). **Aviso
     medido:** el "30 congeladas en silencio" **no es un cardinal duro**, es una convencion
     que se mueve **entre 8 y 43** segun la lista de marcas que se use; lo medi con cuatro
     listas distintas.
  4. **LA CORRECCION DECLARADA DEL 307**, con la cifra vieja intacta y la unidad buena al
     lado.
  5. **LAS CUATRO FILAS VERDE PARCIAL** de la tabla por fase, cada una con lo que le falta
     nombrado: los **quince congelados de 02** sin vara escrita, la **atribucion** de la
     alteracion de pasos en 01, la confirmacion **por lectura** de 04 que la propia celda
     excluye, y los **dos supervivientes divergentes** de 03 que la CORRECCION 16 ya
     clasifica.

**Nada de esos cinco puntos pide credencial y nada decide lo que esta reservado.**

**Y despues de esos cinco queda el muro conocido y ya adjudicado (acta 149, 3.10): la fase
08 no cierra sin una sesion con credencial y contigo delante.** Eso no es un fallo del
bucle: es donde termina lo que un bucle puede hacer solo.

---

## 5. LO QUE LA VUELTA 150 DEJO HECHO, PARA QUE NO SE PIERDA

Lo verifique todo con instrumento propio y **no encontre una sola cifra falsa en su
reporte**:

  - **`OP-C-05`, primera mitad, VIVA EN GATE 0:** la guarda de duplicadas **tras resolver**.
    Es la que defiende las **925 entradas** que `OP-S-12` retiro en la vuelta 148. Su fuerza
    esta medida: sobre el grafo de justo antes de `OP-S-12`, una guarda literal habria dado
    **0 grupos** y esta da **888**. Su caso positivo tumba Gate 0 de verdad, con exit 1 y
    nombrando nodo, campo y destino.
  - **`OP-S-12` cerrada como se debe:** primero la **CORRECCION 30** (su verificacion pedia
    una bajada de 1.056 y bajo 925; el rastro de las **treinta versiones** del fichero
    fuente prueba que la cifra estaba **vencida**, no contradicha), y **despues** el estado
    a `HECHA`. `05_SANEO` queda 10 de 10.
  - **La trampa del ciclo de Gate 0 ya muerde sola.** Cuatro actas seguidas cayeron en el
    mismo falso rojo. Ahora, en los **tres** sitios donde aparece, el mensaje dice si es un
    rojo de verdad o un ciclo sin cerrar, y **nombra el comando que falta**. No afloja nada:
    el exit sigue siendo 1.
  - **El indice semantico, medido:** **3.521 ids, 3.169 vivos, 18 vivos sin vector, 370
    deprecados y CERO fantasmas**. Una sola corrida del constructor arregla los dos lados, y
    esa corrida es de la sesion con credencial.

**El merge de `pasada-unica` no se pide en esta pagina.** La campana no esta consumada.
