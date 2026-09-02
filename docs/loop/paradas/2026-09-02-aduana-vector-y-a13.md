# PARA ALEXIS: EL BUCLE SE DETIENE EN LA PUERTA DE LA FASE 07 (2 sep 2026, vuelta 147, auditor Opus 5)

## EL MOTIVO, EN DOS FRASES

**La fase 07 ADUANA esta en la puerta de cerrarse y lo unico que le queda son DOS
preguntas que ninguna regla escrita cubre, y las dos son tuyas.** La primera la trae el
ejecutor: **la puerta semantica `A2.6` quedo cableada y bloquea a un candidato que no
tenga vector, pero en la linea de ensamblaje de hoy el vector no puede existir todavia
cuando el candidato se copia**. La segunda es mia y vence sola: **la mitad semantica de
`A1.3` sigue sin resolver, y mi propia acta 146 escribio que el dia que la fase 07
intentara cerrarse con esa mitad abierta eso seria PARADA de decision de fundador**. Ese
dia es hoy, porque `A2.6` era la otra razon por la que la fase no cerraba y ya esta
instalada.

**Ninguna otra condicion de parada se cumple.** Gate 0, motor, web, `tsc` y el hook estan
verdes hoy corridos por mi. **Y las dos rachas de credito bajan a CERO**, que es la mejor
noticia de la vuelta.

## EL ESTADO EXACTO

- Rama **`pasada-unica`**, HEAD **`8384155e`** (esta acta y este fichero van en el commit
  siguiente). Arbol limpio, `origin/pasada-unica` sin ahead ni behind.
- **Marcador del cribado, recomputado hoy por mi del fichero:** **A 551 / B 72 / C 5 /
  D 2.760**, n 3.388, `puesto_intra` de 1 a 3.388, **cero huecos y cero duplicados**.
- **Censo, con parser propio anclado en `node_id` sobre los diez refs de la vuelta:**
  **3.853 nodos, 3.169 vivos, 684 deprecados**. Aristas **9.234 / 9.211 / 18.445 /
  9.914**. **Los diez refs dan lo mismo sin una excepcion: la vuelta 147 no movio una sola
  flecha.**
- **TODO VERDE por corrida propia mia:** Gate 0 OK con su ciclo entero en orden
  (`run_phase1.py --reaplico-curaduria`, `etiquetas_de_cara.py --aplicar`,
  `sync_assets_web.py`, numstat VACIO), motor 25/25, web 80 passed (80) y 1.030 passed 3
  skipped (1.033), `tsc` EXIT 0 cero lineas, desfase del calibrado 4 filas sobre 468.
- **Operaciones:** 71 en total, **61 LISTA y 10 HECHA**, contadas por mi del fichero.
  **`OPERACIONES.jsonl` no se toco en toda la vuelta** y el campo `estado` sigue congelado
  desde la vuelta 139, como esta escrito.
- **Fase 07 ADUANA, contra la vara de codigo, corrida por mi:** **9 controles declarados /
  7 distintos / 8 instalados y mordiendo enteros / 1 instalado solo en su mitad mecanica
  (`A1.3`) / 0 no instalados.**
- **Fases cerradas hasta hoy:** 03 (CERRADA CON REMISION, vuelta 74), 04 (CERRADA CON
  REMISION, vuelta 118) y 05 (CERRADA CON REMISION, vuelta 136).
- **Lo que queda despues de la fase 07:** `OP-S-12` al final de la pasada por la atadura 2
  del indice, y la fase 08 entera. **La campana NO esta consumada y este fichero NO pide
  el merge.**

---

## PREGUNTA 1. QUE HACE LA ADUANA CON UN CANDIDATO QUE TODAVIA NO TIENE VECTOR

### Lo que hay hoy, medido por mi en el codigo y no leido de un reporte

`OP-A-02` manda, con todas sus letras: *"ningun nodo entra sin correr el indice contra su
dominio y el nucleo"*, y *"si algun vecino supera el umbral de la cola, LA INSERCION SE
BLOQUEA hasta que quien inserta escriba el veredicto continua-o-repite CITANDO EL ID DEL
VECINO"*. La vuelta 147 la cableo exactamente ahi: en `scripts/integrar_packs.py`, en el
`copy2` que copia cada nodo del pack a `dataset/nodos/`. **Lo verifique y funciona: seis
casos y los seis muerden, incluido el que la ficha pide literalmente (un clon que se
parece por encima del umbral no entra sin veredicto) y el que impide que la puerta sea un
muro (un nodo que no se parece a nadie entra sin veredicto).**

**Y aqui esta el nudo, y es circular por construccion, no por un orden mal puesto:**

| paso de la linea | que hace | consecuencia |
|---|---|---|
| **(a)** | copia el candidato a `dataset/nodos/` **y aqui esta la puerta** | el candidato todavia no esta en `master_graph.json` |
| **(e)** | `run_phase1.py` recompila `master_graph.json` **desde** `dataset/nodos/` | solo ahora el grafo conoce al candidato |
| **(d)** | `build_semantic_index_voyage.py` construye el indice **leyendo** `master_graph.json` | solo ahora existe el vector |

**El vector no puede existir antes de la copia porque se fabrica leyendo el grafo, y el
grafo solo conoce al candidato despues de la copia.** Reordenar los pasos que hoy existen
no rompe el circulo.

**Y hay un segundo muro:** el unico instrumento que fabrica vectores,
`scripts/build_semantic_index_voyage.py`, **exige `VOYAGE_API_KEY` del `.env` de la raiz**,
y ese `.env` esta fuera del repo mientras el bucle corre, por regla tuya. **El bucle no
puede ni siquiera probar la salida que consistiria en embeber al candidato aparte.**

**Hoy no muerde y eso esta medido:** `python scripts/integrar_packs.py --dry-run` dice que
**los nueve packs estan integrados y no hay ninguno pendiente**. La puerta esta cableada e
inerte sobre el arbol de hoy. **Pero el dia que llegue un pack de verdad,
`integrar_packs.py --ejecutar` no podra completarse.**

### Por que no lo adjudico yo

Busque una regla escrita que lo cubriera por extension citable, que es lo que `AUDITOR.md`
seccion 3 me manda intentar antes de traerte nada. **La unica doctrina escrita sobre ids
sin vector es tuya, del 14 ago 2026, opcion B estricta, en
`docs/plan/08_VERIFICACION.md`**, y dice literal que el rojo declarado vale *"EXCLUSIVAMENTE
PARA LOS IDS QUE LA PASADA ACABA DE CREAR"* y que *"CUALQUIER OTRO id en rojo en el chequeo
del indice es PARADA: no se declara, se trae"*. **Un candidato de pack no es un id que la
pasada cree, asi que tu propia regla apunta a la parada en vez de evitarla.**

### Los tres caminos, con su coste, y ninguno es mio

| camino | que costaria | que rompe |
|---|---|---|
| **1. Embeber al candidato aparte antes de insertarlo** | una llamada mas a Voyage por candidato, con la credencial que la casa reserva | nada del mecanismo: la puerta sigue bloqueando en la insercion, tal como la ficha manda. **Es el mas fiel a la ficha y el mas caro** |
| **2. Mover la puerta a despues del paso (d)** | nada de dinero | cambia *"la insercion se bloquea"* por *"la insercion se deshace"*: el nodo ya se copio, el grafo ya se recompilo y el indice ya se construyo cuando la aduana habla. **La aduana deja de ser una puerta y pasa a ser una revision posterior** |
| **3. Darle otra salida** (por ejemplo, que un candidato sin vector entre declarado, como el rojo declarado de la pasada) | nada de dinero | extiende una excepcion que tu escribiste **exclusivamente** para ids que la pasada crea. **Es doctrina nueva y solo tuya** |

**Mi lectura, y la doy como opinion y no como adjudicacion: el camino 1 es el unico que no
toca el mecanismo que ya adjudicaste.** El 2 es barato y defendible, pero convierte la
aduana en otra cosa. El 3 es el mas rapido y el que mas se parece a lo que esta campana
existe para impedir.

---

## PREGUNTA 2. LA MITAD SEMANTICA DE `A1.3`, Y ESTA FRONTERA LA ESCRIBI YO

La verificacion 3 de `OP-A-01` dice: *"Gate 0 rechaza un nodo cuyo segundo libro no aparece
en ningun paso"*. **Su mitad mecanica esta instalada y muerde** (el segundo libro contra la
nomina adjudicada). **Su mitad semantica no lo esta**, y en la vuelta 146 medi por que: la
lectura literal (buscar el titulo del segundo libro como texto dentro de
`pasos_accionables`) **dispara en 9 de 9**, o sea que rechazaria los ocho nodos ya
adjudicados enteros, porque ningun paso del catalogo nombra su libro.

**En mi acta 146, seccion 3.16, escribi la frontera con estas palabras:** *"el dia que la
fase 07 intente CERRARSE con esa mitad sin resolver, eso SI es PARADA de decision de
fundador, porque cerrar una fase con una verificacion inejecutable cambia el criterio de
HECHO"*. Y anadi que ese dia no habia llegado **porque la fase no cerraba por otra razon,
que era `A2.6`**.

**`A2.6` ya esta instalada y muerde.** La vara lo dice sola: *"LA FASE NO SE CIERRA CONTRA
ESTA VARA, y lo que le falta va nombrado: A1.3 (solo su mitad mecanica)"*. **Mi frontera
vence hoy, y correrla otra vuelta seria justo lo que escribi que no habia que hacer.**

**Lo que necesito de ti, y son tres opciones limpias:**

  1. **La verificacion 3 se lee cumplida con su mitad mecanica**, y se deja escrito en la
     ficha que la mitad semantica no es ejecutable con el catalogo que hay. La fase 07
     cierra.
  2. **La verificacion 3 se reescribe** en una forma que si sea ejecutable, y eso es
     cambiar el texto de una ficha del plan, que es tuyo.
  3. **La fase 07 no cierra** hasta que el catalogo permita la lectura semantica, y eso
     bloquea `OP-S-12` y la fase 08 detras.

---

## LO QUE PASO EN LA VUELTA 147, EN CUATRO LINEAS, PORQUE ES BUENA

**No encontre una sola cifra falsa.** Re-medi con instrumento propio todo lo que el reporte
publica (censo y aristas en diez refs, la truncacion por dos universos, la vara, el
marcador, los registros por prefijo, las guardas del cierre) **y todo reproduce al digito**.
**Las dos cifras que si estaban mal eran MIAS, de mi acta 146** (el "seis" de las coladas son
cinco, las "doce" lineas de calibracion son siete), **y el ejecutor las declaro en vez de
copiarlas, que es exactamente lo que la casa pide**. **Las dos rachas bajan a CERO:** cifra
publicada de uno a cero, reporte de tres a cero con la especie rota en dos. **La escalada de
la escalada que encargue como tarea bloqueante hizo su trabajo**, y lo probe yo: las tres
cadenas del barrido que fallo estaban muertas en el arbol de su propio commit y estan vivas
en el de hoy, asi que juzgar un sello contra el arbol de hoy lo resucita con las palabras que
se escribieron para enterrarlo.

## COMO RETOMAR

1. **Decide la PREGUNTA 1** (el candidato sin vector) y **la PREGUNTA 2** (la mitad semantica
   de `A1.3`). Con eso la fase 07 puede cerrar o queda con su destino escrito.
2. **Escribe tu decision** en `docs/loop/paradas/2026-09-02-aduana-vector-y-a13-DECISION.md`,
   como las anteriores, para que sea citable.
3. **Relanza el bucle.** El encargo de la vuelta 148 sera la aplicacion de tu decision mas la
   lista de seis puntos que deje medida en la **seccion 7 del acta 147**: la guarda de la
   nomina cerrada por el lado del commit (probe que es ciega al movimiento que llega ya
   commiteado), el camino POR CONJUNTO de la guarda de cifras, la unidad que le falta a la
   vara, la salida auditable del falso positivo de la guarda de ausencias, la letra de
   `VIEJAS`, y las CORRECCIONES 27 y 28 con mis dos cifras falsas corregidas por adicion.
4. **`docs/loop/PROMPT_SIGUIENTE.md` queda VACIO**, por la seccion 4 de `AUDITOR.md`.

**El merge de `pasada-unica` no se pide aqui y no se hace: la campana no esta consumada.**
