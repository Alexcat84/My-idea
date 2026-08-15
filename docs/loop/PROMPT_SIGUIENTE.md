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
1.4. Correr scripts/loop/verificar_mapas_destejido.py sobre las tablas vigentes tras la
correccion de 1.1 y citar su salida verde en el reporte.

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
