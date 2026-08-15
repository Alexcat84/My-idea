# PARA ALEXIS: PARADA DE CREDITO (15 ago 2026, vuelta 32, auditor Fable 5)

## EL MOTIVO, en dos lineas

**Dos tandas seguidas con caida de cifra publicada, y tu regla del 13 ago dice que eso es
PARADA sin pesar el dano.** La vuelta 31 tuvo el nombre `investigar` en la tabla de costuras;
la vuelta 32 tiene **el origen 16 en el grupo equivocado del mapa del emblema**. Las dos son
la misma especie: una celda tecleada a mano en una tabla de prosa de `docs/plan/` que ningun
instrumento valida.

## LA CAIDA DE ESTA VUELTA, con su evidencia

`docs/plan/02_DESTEJIDOS.md`, tabla del movimiento 1 de `OP-D-01`: la fila del paso **2**
lista los origenes **2, 6, 11, 15, 16, 19**, y la fila del paso **6** (origenes 8, 14, 17,
22) dice en su motivo *los pasos **14 y 16** traen la cadencia*. **Las dos filas no pueden
ser verdad a la vez.** El paso 16 viejo (*Desarrolla tu primera version de forma incremental,
en ciclos cortos e iterativos*) es cadencia pura: **pertenece al grupo del paso 6**. La misma
contradiccion vive en `docs/loop/PLAN_V32_OPD01_EMBLEMA.json` y en la seccion 4.1 del
reporte.

**Lo que NO mueve, medido por mi:** el texto del nodo esta BIEN tal como quedo; los
supervivientes no cambian; la cobertura sigue exacta 22 de 22; ninguna cifra del marcador se
toca. Es una celda de papel, pero tu regla cuenta tandas, no dano, y por eso paro.

**Hubo ademas UNA caida de reporte** (el motivo 2 de la parada de `OP-D-02` dice *DOS de los
tres pares A no nombran ganador* cuando medido hoy **ninguno de los tres** lo nombra; la
conclusion sale reforzada). No acumula para parada: van una seguida.

## EL ESTADO EXACTO

- Rama `pasada-unica`, reporte en `1736e1d7` (cierre del ejecutor `c0cc10b3`), mas el commit
  de esta acta. Cero merges, cero nodos tocados en la parada, el `.env` fuera del repo.
- Marcador **n 3.388, A 583, B 89, C 7, D 2.709**, cero huecos, verificado con el instrumento
  corrido hoy. Grafo **3.853 ficheros, 3.539 vivos, 314 deprecados**, enlaces 16.848.
- **FASE III:** fase 01 re-cerrada **14 de 14** (verificada con las dos corridas de saldo al
  digito); **`OP-D-01` ejecutada y verificada entera** (el 14vo por `P.19`, el emblema 22 a 6
  y 10 a 5, el pariente en 7 por la excepcion de clase); **`OP-D-02` parada con cero nodos
  tocados** y sus tres motivos reproducidos por mi medicion.
- **Guardas, todas por corrida propia:** Gate 0 OK con derivado byte igual, motor 24 de 24,
  web 1.030 pasadas y 3 saltadas, `tsc` cero lineas.
- La relectura ciega de los 15 discutibles del reporte: **coincido en los quince en el
  fondo**. El acta entera esta en `docs/loop/ACTA_AUDITOR.md`, vuelta 32.

## LO QUE ESTA VUELTA DEJA ADJUDICADO (con letra citable, para que no se pierda)

1. **Los tres pares internos que le faltan a `OP-D-02` los lee el ejecutor de la fusion, por
   `P.5`, como LECTURAS DIRIGIDAS** (`docs/plan/LECTURAS_DIRIGIDAS.md`: misma vara, formato
   LD, **no entran en la cola ni mueven su marcador**). El miedo de mover n de 3.388 lo
   resuelve esa letra: n no se toca. Precedente: el lote de sales roadmap del 14 ago.
2. **El carril de las tres clases releidas (494 a C, 592 a D, 830 a D) es el banco 9.10 como
   MECANISMO**, no como fase: volcar al archivo con *REESCRITA EL ... POR ...* y barrer las
   tablas derivadas en el mismo acto. La verificacion de la fase 02 lo exige (*los congelados
   se releen y salen de la lista*). El marcador quedaria A 582, B 87, C 8, D 2.711, n intacto.
3. **La nomina de `OP-D-02` queda en CUATRO** por `P.6` (la nomina de acto se computa por el
   cierre transitivo de las A). Los dos nodos del censo entran solo si una A los mete, y esa
   A pasa por el congelado 724, que espera al superviviente por el 9.4.

## LO QUE SE NECESITA DE TI

1. **Dar por vista la parada de credito** y decidir si el bucle rearranca (y con que cura del
   patron: las dos caidas de las dos tandas son celdas manuales en tablas de prosa; si
   quieres, una guarda de instrumento que valide mapas contra motivos es escribible, pero
   ordenarla es tu pluma).
2. **Visto a la correccion de la celda del 16** (texto viejo tachado, no borrado, en
   `02_DESTEJIDOS.md`, el plan sellado y donde el reporte la cita), que quedaria ordenada en
   el encargo de abajo.
3. **Visto a las tres adjudicaciones de arriba.** Son por letra citable, no doctrina nueva,
   pero la parada las deja en espera de tu ojo.

## COMO RETOMAR

Relanza el bucle copiando el encargo siguiente ENTERO (esta abajo) a
`docs/loop/PROMPT_SIGUIENTE.md`, que hoy queda vacio como manda la parada.

---

## EL ENCARGO SIGUIENTE PROPUESTO, completo

Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

TAREA 1, LOS REGISTROS.
1.1. La correccion de la celda del origen 16 (caida de cifra publicada del acta 32): en
`docs/plan/02_DESTEJIDOS.md` (tabla del movimiento 1) y en la seccion `grupos_pasos` de
`docs/loop/PLAN_V32_OPD01_EMBLEMA.json`, el origen 16 pasa del grupo del paso 2 al grupo del
paso 6, con el texto viejo tachado y no borrado y la correccion declarada con su fecha. El
texto del nodo NO se toca: la medicion del acta 32 confirma que esta bien tal como esta.
1.2. La correccion del motivo 2 de la parada de `OP-D-02` donde el reporte y
`SALIDA_V32_PARADA_OPD02.txt` dicen *dos de los tres*: la medicion del acta 32 da que
NINGUNO de los tres pares A nombra ganador. Se registra en `02_DESTEJIDOS.md` seccion
`OP-D-02` como correccion declarada; la nota de `OPERACIONES.jsonl` ya esta bien y no se
toca.
1.3. El volcado de las tres clases releidas, adjudicado en el acta 32 seccion 4.2: en
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, el 494 pasa de A a C (banco 9.22, tercer ejemplar,
enlace mutuo declarado para la fase 04), el 592 y el 830 pasan de B a D (arista que falta),
cada uno con su razon reescrita al estilo *REESCRITA EL ... POR ...* conservando la razon
vieja dentro. En el mismo acto, por el banco 9.10: barrer TODA tabla derivada que cite esos
tres puestos o el marcador viejo (A 583, B 89, C 7, D 2.709), recomputar el marcador con el
instrumento y publicar la salida. El marcador esperado es A 582, B 87, C 8, D 2.711 con n en
3.388: si el instrumento da otra cosa, PARAR y traerlo.

TAREA 2, EL TRABAJO: `OP-D-02` por su letra, con el carril adjudicado.
2.1. Leer los TRES pares internos que faltan (`enfoque_mercado_voc` contra
`homework_frontend_loading`; `homework_frontend_loading` contra `voz_del_cliente_voc`;
`voice_of_customer_homework` contra `voz_del_cliente_voc`) como LECTURAS DIRIGIDAS por `P.5`:
misma vara del cribado, nodos impresos ENTEROS antes de decidir, registro en
`docs/plan/LECTURAS_DIRIGIDAS.md` con numero LD nuevo y formato de la casa. NO entran en la
cola ni mueven n. Con 6 de 6 leidos, contestar por escrito la pregunta de `P.5`: el acto es
UNA familia o DOS.
2.2. Con el acto entero delante, fijar el superviviente: primero la prueba corregida del
banco 9.3.1 (gano todos los pares A que lo tocan, contando solo las A); si no hay ganador por
derecho, GANADOR POR ELEGIR por `P.8` sobre la nomina de cuatro, contenido primero y cableado
como desempate, con la eleccion y su porque escritos en la operacion como correccion
declarada del campo `superviviente`.
2.3. Ejecutar la fusion de `OP-D-02` tal como esta escrita, con su `preservar` integro (la
evaluacion preliminar de mercado, el analisis competitivo detallado, y probar los conceptos
con clientes reales antes del desarrollo formal), simulacion previa sobre copia en memoria,
plan sellado, tabla de seis motivos, caso positivo antes y despues, y el ciclo de Gate 0 con
las suites.
2.4. Releer 724, 755 y 827 contra el superviviente ya estable (banco 9.4) y volcarlos por el
mismo carril del 9.10 de la tarea 1.3, con su barrido en el mismo acto. GUARDA: si el 724
diera A (`voice_of_customer_estrategico` entraria al acto por `P.6`), PARAR y traerlo: una
fusion nueva sin operacion escrita no se improvisa.
2.5. Con `OP-D-01` y `OP-D-02` hechas y verificadas, seguir el modo continuo por el orden del
`00_INDICE` (`OP-D-03` en adelante), con las guardas obligatorias de siempre por operacion.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una regla
vigente, paras y lo traes. No adivines.
