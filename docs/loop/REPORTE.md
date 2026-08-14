# REPORTE del ejecutor del bucle, vuelta 12 (FASE II, SEGUNDA VUELTA: EL PLAN SE REESCRIBE AL 3.388)

**Sesion ejecutora (Sonnet 5). Fecha de reloj: 13 ago 2026. Rama activa: `bucle`.** MODO DE CIERRE:
cero reparaciones de nodos. **`dataset/` no se toco ni un byte.** La Fase III (mover nodos de
verdad, rama `pasada-unica`) sigue sin abrir.

## Hash y rutas

- **Hash final de esta vuelta:** `f1f267d4` (TAREA 2.B). Este reporte queda por encima.
- **Commits de la vuelta:**
  - `ec57d14b` TAREA 1: dos preguntas que el encargo declaro imposibles quedan medidas, y la
    adjudicacion 101.e queda registrada.
  - `5382943c` TAREA 2.A: el plan se reescribe al corte 3.388 (`OP-U-02` a LISTA, `OP-U-01`
    reescrita, 28 operaciones mas verificadas sin cambio).
  - `f1f267d4` TAREA 2.B: el paso 2 del recomputo, corrido por la via acotada de los 36.
- **Rutas tocadas:**
  - `docs/plan/RECOMPUTO_3388.md`: cinco correcciones declaradas (401/400, los 48, el 387, la
    autorizacion de `OP-U-02`, y el paso 2 completo), todas con tachado sin borrar.
  - `docs/INTRA_DOMINIO_INFORME.md`: seccion 101.e nueva (la adjudicacion del acto de quince de
    `health_safety`), con correccion del encabezado de "cuatro" a "cinco" adjudicaciones.
  - `docs/plan/OPERACIONES.jsonl`: dos lineas editadas, `OP-U-01` y `OP-U-02`. Las otras 67 lineas,
    sin tocar (verificado por diff: solo 2 de 69 lineas cambiaron).
  - `docs/loop/REPORTE.md`: este archivo, reescrito entero.

---

## TAREA 1: dos preguntas que el encargo declaro imposibles, medidas y registradas

### 1.a El 401 contra 400 A vigentes al 2.117

**VERIFICADO por el ejecutor con instrumento propio antes de escribir**, no solo transcrito del
acta del auditor. Comando: `git show c16a24f5:docs/INTRA_DOMINIO_VEREDICTOS.jsonl` (11 ago 2026,
2.117 lineas exactas) comparado clase a clase, linea a linea, contra las 2.117 primeras lineas del
archivo de hoy. **Resultado: UN solo cambio de clase, el puesto 2.078**
(`elaboracion_fdd`/`preparar_fdd`, `franquicias`), **D el 11 ago y A hoy**. El archivo viejo tiene
exactamente 400 A. **Correccion declarada en `docs/plan/RECOMPUTO_3388.md`**, con el texto viejo
tachado y sin borrar, citando el hash, el puesto y la frase del banco 9.21 ("cada cifra es correcta
en su corte").

### 1.b El mapeo de los 48 actos abiertos del 2.117

**Este es el hallazgo mas importante de la vuelta, porque el primer intento del ejecutor NO
reprodujo la cifra del auditor, y el encargo pedia exactamente eso: no escribir lo que no verifica.**

Primer intento: reconstruir el estado al corte 2.117 (veredictos truncados a 2.117 lineas, con el
2.078 forzado a D) usando el MISMO criterio simplificado que `scripts/plan/recomputo_3388.py` usa
para el corte 3.388 (un acto cierra si sus pares INTERNOS estan todos leidos). Resultado: **179
cerrados sobre 384 nodos, 42 abiertos sobre 192**. NO coincidia con la cifra publicada (173/371,
48/205). **Por la instruccion del encargo, no se escribio: se investigo la causa.**

**La causa:** el criterio simplificado de `recomputo_3388.py` es valido SOLO cuando la cola esta
agotada (como al corte 3.388, donde `INTRA_DOMINIO_PARES.jsonl` y `INTRA_DOMINIO_VEREDICTOS.jsonl`
tienen exactamente los mismos 3.388 pares). Al corte 2.117 la cola NO estaba agotada (quedaban
1.271 pares sin leer), y el criterio ORIGINAL de `OP-U-01` tiene una segunda condicion mas amplia,
escrita en su propia nota: "ningun miembro tiene un par PENDIENTE EN LA COLA", contra CUALQUIER
nodo, no solo contra otro miembro del acto. El script simplificado solo mira pares internos al
acto y por eso cerraba de mas.

**Corregido el instrumento** (comprobando, para cada miembro de cada componente, si tiene algun par
en la cola completa de 3.388 sin leer todavia, sin restringir a pares internos) y vuelto a correr:
**reproduce exacto la cifra publicada**: 221 componentes sobre 576 nodos, **173 cerrados sobre 371**
(149 de dos, 23 de tres, uno de cuatro), **48 abiertos sobre 205**, motivos **42 por par interno mas
6 por miembro pendiente**. Coincide cifra a cifra con el acta del auditor.

**Con esa membresia reconstruida, el mapeo contra el corte 3.388:**

| | cuantos |
|---|---:|
| CERRARON (mismos miembros, hoy CERRADO) | **5** |
| siguen abiertos, identicos, sin crecer | **42** |
| siguen abiertos y CRECIERON | **1** (`gestion_terminacion_franquiciado` con `terminacion_franquiciado_causas`, de 2 a 3) |

Los cinco que cerraron: `cinco_categorias_costos_franquicia`/`costos_preparacion_franquicia`/
`estimacion_inversion_inicial_franquiciador`; `estrategia_multicanal_expansion`/
`franquicia_mas_crecimiento_corporativo_hibrido`; `proceso_llamada_inicial_venta`/
`proceso_primera_llamada`; `sitio_web_captura_leads`/`sitio_web_franquicia`;
`comprender_definicion_legal_franquicia`/`marco_name_system_fee`.

Y **114 actos de hoy no contienen ni un nodo de un acto del 2.117**, de los cuales **102 nacieron
cerrados y 12 nacieron abiertos**. Las cuentas cierran: 173+5+102=**280**; 42+1+12=**55**.
Correccion declarada en `docs/plan/RECOMPUTO_3388.md`, texto viejo tachado sin borrar.

### 1.c Por que la diferencia de `OP-E-03` (387) no bajo

Leido `scripts/plan/diferencia_contra_cola.py`: compara los candidatos del barrido contra la UNION
de `INTRA_DOMINIO_PARES.jsonl` (la cola planificada) mas `INTRA_DOMINIO_VEREDICTOS.jsonl` (lo
leido). La primera esta completa en 3.388 desde el 9 ago 2026 (verificado, `git diff --stat
c442345a -- docs/INTRA_DOMINIO_PARES.jsonl` vacio). **Cerrar un dominio no mueve la cola
planificada: mueve el archivo leido, que ya estaba dentro de la union desde antes.** Por eso el 387
no podia bajar sin importar cuantos dominios cerraran. Registrado en `docs/plan/RECOMPUTO_3388.md`
con la frase de que la expectativa de baja fue error del auditor, no del ejecutor de la vuelta 11.

### 1.d La adjudicacion 101.e

Registrada en `docs/INTRA_DOMINIO_INFORME.md`: cuando el acto de quince de `health_safety` se
ejecute, el superviviente conserva el contraste de seis ejes de
`vieja_vision_vs_nueva_vision_seguridad` (el nodo repite cuatro veces y muere en las cuatro; su
tabla es catalogo). El encabezado de la seccion 101 se corrigio de "CUATRO" a "CINCO"
adjudicaciones, con correccion declarada.

### 1.3 Lo verificado y en verde, no se toco

El marcador entero al 3.388, las 583 A, las 335 componentes y sus miembros, los 280 CERRADOS y los
55 ABIERTOS, las cuatro comprobaciones, la tabla de `OP-E-03`, los cinco hubs de siete toques, los
once discutibles del tramo. Siguen aprobados `scripts/plan/recomputo_3388.py` y
`scripts/plan/diferencia_contra_cola.py` (con la salvedad, ahora escrita, de que su criterio de paso
4 es una simplificacion valida solo con la cola agotada).

---

## TAREA 2.A: el plan se reescribe al corte 3.388

### `OP-U-02`: DECISION PENDIENTE a LISTA

`fecha_corte` a `2026-08-13`. Evidencia reescrita con 335 componentes, 280/600, 55/254, citando la
verificacion del auditor (acta vuelta 11, adjudicacion 4.1, con la prueba de identidad conjunto a
conjunto). La linea vieja del corte 2.117 se conserva, sin borrar (banco 9.21).

### `OP-U-01`: cifras reescritas al corte 3.388

Cerrados de 173/371 a **280/600** (2: 244, 3: 32, 4: 4). Abiertos a **55/254**. Nota ampliada con
cuales de los 48 cerraron (los cinco de franquicias, nombrados arriba). Verificacion "NINGUN acto de
la lista de abiertos se ejecuta antes del recomputo" actualizada a la lista de 55, sin borrar la
referencia a los 48. La vieja cifra (173/371, corte 2.117) queda al lado con su fecha, sin borrar.

### Las 28 operaciones restantes, verificadas una por una, CERO CAMBIOS

**Instrumento propio**: para cada operacion (`OP-L-02`, `OP-M-01` a `OP-M-05` y sus 22 sub
operaciones, `OP-D-01` a `OP-D-06`), se tomo su nomina de nodos citada (`nodos`, resuelta por
alias), se calcularon los pares posibles entre ellos, y se contaron cuantos estaban leidos (y
cuantos en A) al corte 2.117 contra el corte 3.388.

| operacion | nodos | pares posibles | leidos 2.117 (A) | leidos 3.388 (A) | cambio |
|---|---:|---:|---|---|---|
| OP-D-01 | 2 | 1 | 1 (1) | 1 (1) | ninguno |
| OP-D-02 | 4 | 6 | 3 (3) | 3 (3) | ninguno |
| OP-D-03 | 6 | 15 | 8 (7) | 8 (7) | ninguno |
| OP-D-04 | 7 | 21 | 8 (7) | 8 (7) | ninguno |
| OP-D-05 | 3 | 3 | 3 (3) | 3 (3) | ninguno |
| OP-D-06 | 18 | 153 | 9 (9) | 9 (9) | ninguno |
| OP-M-01 | 17 | 136 | 23 (18) | 23 (18) | ninguno |
| OP-M-02 | 28 | 378 | 41 (10) | 41 (10) | ninguno |
| OP-M-03 (7 nodos, nomina en prosa) | 7 | 21 | 13 (4) | 13 (4) | ninguno |
| OP-M-04 | 4 | 6 | 5 (4) | 5 (4) | ninguno |
| OP-M-05 | 9 | 36 | 16 (12) | 16 (12) | ninguno |
| OP-M-02-PROG/MEDIOS/ASSESS/ADMIT/ACTIVATE/ACCLIMATE/ACCOMPLISH (7 sub) | 2 cada una | 1 cada una | 1 (1) cada una | 1 (1) cada una | ninguno |
| OP-M-03-I/II/III/ENLACES (4 sub) | 2 a 3 | 1 a 3 | igual | igual | ninguno |
| OP-M-01-FUSION/ESLABONES/SEXTO (3 sub) | 2 a 5 | 1 a 10 | igual | igual | ninguno |
| OP-M-05-INDICE/EDIFICIO/APERTURA (3 sub) | 3 cada una | 3 cada una | igual | igual | ninguno |

**CERO cambios en las 28.** Ningun veredicto nuevo entre el puesto 2.118 y el 3.388 toca las
nominas de estas operaciones: sus mesas y destejidos viven en `core` sobre racimos cuya cribado
interna ya estaba agotado al 2.117 (verificado en cada fila, no supuesto). Los numeros publicados
(120/136 posibles de `OP-M-01`, 378 de `OP-M-02`, 21 de `OP-M-03`) coinciden exacto con el
recomputo. **Se dejan sin tocar**, con su cifra confirmada aqui, tal como pide el encargo para las
que no cambian.

**`OP-L-02` no tiene nomina de nodos citada** (su universo son tres nominas de lecturas dirigidas
descritas en prosa: cuadrantes de mercado, ecuacion de valor, bloque humano de la IA). Razonamiento
en vez de recomputo directo: su evidencia (205 pares FUERA DE COLA) es por definicion un universo
que nunca entro a la cola intra-dominio, asi que avanzar el cribado de 2.117 a 3.388 no puede
tocarla estructuralmente (no hay pares fuera de cola que una cola distinta pueda leer). Queda sin
tocar con esa razon escrita, no con un recomputo directo: es el intento que se corrio, declarado
como pide la regla nueva.

### Comprobacion de integridad de `OPERACIONES.jsonl`

**69 operaciones antes y 69 despues** (`wc -l` y conteo de lineas JSON validas, iguales). **Cero
`id_op` duplicados.** **Cero `depende_de` apuntando a un id inexistente.** **Cero `bloquea_a`
apuntando a un id inexistente** (comprobacion extra, no pedida, barata). Comando: script python de
una linea sobre el archivo, cargando cada linea como JSON y comparando el conjunto de ids.

### Lo que NO se ejecuto

Ninguna operacion. `dataset/` no se toco. No se creo la rama `pasada-unica`.

---

## TAREA 2.B: el paso 2 del recomputo, por la via acotada

**Corrido, con correccion declarada en `docs/plan/RECOMPUTO_3388.md`.**

1. **Cruce de las 128 citas de `docs/COSTURAS_INTERNAS.jsonl` (resueltas por alias) contra los 854
   nodos con al menos una A.** Verificado: **interseccion de 36**, exacto contra la cifra del
   auditor.
2. **Para los 36, el veredicto ya escrito**, buscado en la tabla reconciliada de
   `docs/FICHA_SUBFUSION_GRADIENTE.md` (lineas 3651-3780, la que declara "cada una de las 128 citas
   leidas vive en exactamente una fila"). **Fraccion: 36 de 36 tienen veredicto escrito (0 sin
   veredicto), 15 CONFIRMADA, 21 FALSA.** Cada uno citado con su linea exacta en
   `docs/plan/RECOMPUTO_3388.md`.
3. **Los 15 CONFIRMADA son las curas acopladas, y ninguno es nuevo.** Diez tienen ejemplar numerado
   propio en la serie SANO POR DENTRO, GEMELO POR FUERA (CUARTO a DUODECIMO mas el DECIMOTERCERO Y
   CUARTO); dos son el precedente citado dentro de esa misma serie (`blueprint_de_experiencia` y
   `customer_journey_mapping`, puesto 341); tres estan en la tabla "TRES que el goteo no habia
   encontrado" (`brainstorming_divergente`, `future_scenarios_planning`,
   `plan_de_adquisicion_acquire`). **Cero se reescribieron: se citaron.**
4. **Verificacion cruzada barata: los 15 ya tienen dueno en `OP-D-01` a `OP-D-06`.** Cada uno de los
   15 aparece en la nomina de nodos de alguna de esas seis operaciones. El paso 2, corrido por la
   via acotada, confirma que los seis destejidos ya son exhaustivos sobre el universo de los 36: no
   abre ninguna cura acoplada que el plan no tuviera contemplada.

---

## MIDIENDO SIN ESCRIBIR EN EL PLAN (encargo para la vuelta siguiente)

**De las 55 componentes ABIERTAS al corte 3.388, TODAS (55 de 55) lo estan exclusivamente por pares
que nunca entraron a la cola** (`fuera_de_cola`). **Cero estan abiertas por "miembro con par
pendiente en la cola sin leer"** (`en_cola_sin_leer`), y cero por ambos motivos a la vez. Esto es
la consecuencia directa, medida y no solo deducida, de que la cola intra-dominio esta agotada al
3.388 (`INTRA_DOMINIO_PARES.jsonl` y `INTRA_DOMINIO_VEREDICTOS.jsonl` identicos): la segunda
condicion del criterio de `OP-U-01` es hoy trivialmente cierta para las 335 componentes, y la
unica via que deja algo abierto es la primera. Nada de esto se escribio en `docs/plan/`, tal como
pide el encargo: queda aqui para alimentar el encargo siguiente (probablemente `OP-L-02`, que es
exactamente el universo de "fuera de cola").

---

## LO QUE NO SE MIDIO ESTA VUELTA

- **La nomina completa de las 46 confirmadas (no solo las 36 con A) sigue sin estar escrita como
  lista en ningun sitio.** El paso 2 se cerro por la via acotada de los 36 (los que SI tienen A), que
  es lo que el encargo pedia; las 10 restantes de las 46 (las que no tienen A vigente, si las hay)
  no se buscaron, porque no eran parte de la via acotada.
- **El lote de cinco lecturas del sales roadmap, la cola de relectura post fusion, el criterio del
  forastero, las lecturas de acto entero de P.5, y las 387 filas de LECTURAS DIRIGIDAS**: fuera de
  esta vuelta por instruccion explicita del encargo, cada una con su orden propio.
- **Las 205 lecturas fuera de cola de `OP-L-02`** no se remidieron: su evidencia (205, 126, 79, 24,
  55) es estructuralmente inmune al corte del cribado intra-dominio (razonado arriba, seccion TAREA
  2.A), pero no se corrio un recomputo directo sobre sus tres nominas nombradas en prosa porque el
  encargo no las incluyo en la lista de operaciones a verificar mas alla de "OP-L-02" como bloque.
- **El pendiente de los 365 A ciegos anteriores al 2.127** sigue sin verificar, sin cambio esta
  vuelta.
- **La trampa del identificador** sigue sin censo sobre `core`, `environmental`, `exportacion`,
  `entrega` ni `compras`.

---

## DISCUTIBLES MARCADOS, para la relectura ciega del auditor

1. **La correccion del criterio de paso 4 para el corte viejo (TAREA 1.b) es la pieza mas fuerte de
   esta vuelta y la mas facil de auditar mal si el auditor no repite el mismo error que el ejecutor
   casi comete.** El criterio simplificado de `recomputo_3388.py` (solo pares internos al acto) da
   179/42, NO 173/48. Si el auditor recomputa el corte 2.117 con ese mismo script tal cual esta
   escrito hoy (sin el ajuste manual de "miembro con pendiente externo"), le va a dar 179/42 tambien,
   y podria leer eso como una discrepancia del ejecutor cuando es al reves: el ejecutor SI encontro
   el error y lo corrigio antes de publicar. **La verificacion del auditor tiene que usar el
   criterio de dos condiciones completo (miembro con CUALQUIER par pendiente, no solo interno), no
   el script tal cual esta commiteado.**
2. **`scripts/plan/recomputo_3388.py` queda con una limitacion no corregida esta vuelta**: su paso 4
   usa el criterio simplificado (valido solo con la cola agotada). Es correcto para el corte 3.388
   (su unico uso autorizado) pero seria enganoso si alguien lo usa para reconstruir un corte
   intermedio sin saber esto. No se toco el script esta vuelta porque MODO DE CIERRE no autoriza
   escribir instrumentos nuevos fuera de lo que el encargo pide, y el encargo no pidio arreglar el
   script, solo verificar la cifra. **Marcado para que quede escrito y no se pierda.**
3. **La reconstruccion del corte 2.117 fuerza el puesto 2.078 a D "a mano"** (no hay una forma
   automatica de re-derivar la clase historica salvo el commit `c16a24f5`, que ya se uso para eso).
   Es un solo puesto, verificado dos veces (TAREA 1.a y TAREA 1.b), pero es una intervencion manual
   sobre datos que vale la pena que el auditor recorra el mismo camino antes de dar por buena la
   cifra.
4. **La lista de "sin cambio" de las 28 operaciones (TAREA 2.A) se basa en comparar pares posibles
   entre la nomina de `nodos` citada por cada operacion, no en re-simular las fusiones ni releer las
   notas completas.** Si alguna operacion tiene una cifra publicada que depende de algo distinto de
   "cuantos pares entre estos nodos estan leidos" (por ejemplo, una cifra sobre nodos FUERA de la
   nomina citada, como el "72 pares cruzados" de `OP-M-01` contra el resto del racimo), ese tipo de
   cifra no quedo verificada por este metodo. Se declara el limite en vez de esconderlo.
5. **El hallazgo de la seccion "MIDIENDO SIN ESCRIBIR EN EL PLAN" (55 de 55 por fuera_de_cola) se
   deduce logicamente del aviso metodologico que el propio `docs/plan/RECOMPUTO_3388.md` ya
   declaraba** (la cola agotada hace trivial la segunda condicion). La medicion directa lo confirma
   sin sorpresas, pero vale la pena que el auditor la re-corra por su cuenta antes de darla por
   sentada para el encargo siguiente.
