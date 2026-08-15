# PARA ALEXIS: PARADA DE DOCTRINA EN `OP-D-03` (vuelta 33, 15 ago 2026, auditor Fable 5)

## EL MOTIVO EN DOS FRASES

La vuelta 33 esta LIMPIA: verificada entera y al digito por corrida propia del
auditor, la relectura ciega coincide 7 de 7, la primera fusion del plan esta bien
hecha, y Gate 0, las tres suites y el verificador de mapas estan verdes. El bucle
se detiene porque quedaron DOS preguntas que ninguna pagina contesta y que
bloquean lo que sigue: **el cableado de los nodos deprecados** y **la
recalibracion del instrumento de costuras**.

## EL ESTADO EXACTO

- Rama `pasada-unica`, HEAD `d5058140` (reporte de la vuelta 33). FASE III en
  modo continuo, detenida en `OP-D-03` con **CERO nodos tocados**.
- Marcador **n 3.388, A 582, B 84, C 8, D 2.714**, cero huecos y cero
  duplicados, recomputado por el auditor desde el archivo con comando propio.
- Grafo **3.853 ficheros, 3.538 vivos, 315 deprecados**; enlaces 16.852.
  `OP-D-02` **FUNDIDA** (`voz_del_cliente_voc` absorbe a `enfoque_mercado_voc`)
  con nueve guardas verdes. Gate 0 re-corrido por el auditor con el ciclo entero:
  **OK y derivado byte igual al commiteado**; motor 24 de 24, web 1.030 pasadas,
  `tsc` cero lineas, todo por corrida propia.
- `OP-D-01` y `OP-D-02` hechas. **El unico rojo vivo es el caso positivo de la
  fusion TRAS Gate 0 (22 de 23)**, dejado en rojo A PROPOSITO, y es lo correcto:
  es el sintoma de la pregunta 1, no un defecto del trabajo.
- La conducta del ejecutor en esta vuelta fue ejemplar: la cifra esperada escrita
  ANTES de correr el instrumento las dos veces, las dos corridas publicadas en
  cada discrepancia, y el rojo publicado sin maquillar.

## LAS TRES DECISIONES QUE SE NECESITAN DE TI

**1. EL CABLEADO DEL DEPRECADO** (bloquea la estabilidad de TODA fusion futura, y
hay una ya ejecutada esperando). El absorbido conserva sus aristas y el
reciprocado de Gate 0 se las devuelve a los tres vivos que lo nombraban. Opciones:

- **a) El deprecado conserva su cableado como archivo y Gate 0 deja de reciprocar
  aristas que nacen en deprecados.** Cambio de codigo en la simetrizacion de fase
  0, con caso positivo en rojo y en verde; la prueba *ningun vivo nombra al
  absorbido* vuelve a poder ser verde y ESTABLE. Es la que menos miente: el
  deprecado es archivo, no participante. **RECOMENDACION DEL AUDITOR.**
- b) La redireccion reescribe tambien las listas del absorbido. Estable, pero
  pierde el cableado historico intacto que hace auditable la fusion.
- c) La guarda cambia de letra a *ningun vivo lo nombra SIN resolver por alias*.
  Convierte la deuda en norma; el grafo crudo queda con punteros a muertos.

**2. `costuras_internas.py`** (bloquea `OP-D-03` entero y deja a medias el apoyo
del movimiento 2 del acta 32). La senal de bloque devuelve 0,0 para todo nodo de
menos de seis pasos (`range(MIN_BLOQUE, n - MIN_BLOQUE + 1)` vacio con
`MIN_BLOQUE = 3`), y los DOS nodos de calibracion tienen CINCO pasos hoy porque
esta misma campana los destejio en vueltas anteriores. Hace falta decidir: quien
lo arregla, con que rango o `MIN_BLOQUE`, y **contra que nodos se recalibra** (los
del docstring ya no miden el 60,0 y 54,7 declarados: hoy dan 47,1 y 54,3 de
pareja). Con el arreglo van: la correccion declarada de la cifra del acta 32
(bloque 0,0 contra 44, que no mide lo que dice medir) con recomputo de ese apoyo,
y la cura del pendiente 3: **la puerta de calibracion tiene que valer tambien para
quien la importa** (`vuelta32_costura_opd01.py` importo las senales por debajo de
la puerta), sea moviendola a las senales o escribiendo la regla de que toda
importacion trae su baranda.

**3. LOS SIETE PARES INTERNOS DE `OP-D-03`**: se leen como dirigidas igual que los
tres de `OP-D-02`, y si ANTES o DESPUES del destejido. `P.5` dice despues; la
respuesta depende de la decision 2.

## LO QUE NO NECESITA DECISION (adjudicado por el auditor con letra citable)

- Los checkpoints cerrados NO se reescriben (CRITERIO del 14 ago: lo viejo se
  cita como contraste; el 9.10 es para tablas vigentes). Pendiente 4 cerrado.
- Los puentes de `OP-D-02` no necesitan operacion propia (`P.10` mas fase 04;
  LD-74 con su arista declarada). Pendiente 5 cerrado.
- Credito: racha de tandas en CERO. Una caida de REPORTE del ejecutor registrada
  (el conteo de commits del encabezado: son ocho con la apertura, no siete);
  caidas de reporte seguidas: DOS. A la tercera seguida, parada de patron.
- La ciega del auditor coincide 7 de 7 con las clases escritas (494 C por el
  9.22, 724/755/827 D, LD-72/73/74 D).

## COMO RETOMAR

1. Decide las tres preguntas y deja la decision escrita (como la del 15 ago en
   `docs/loop/paradas/`).
2. Copia el encargo de abajo a `docs/loop/PROMPT_SIGUIENTE.md`, ajustando los
   corchetes segun lo que decidas.
3. Relanza el bucle. La verificacion del auditor volvera a ser completa hasta que
   la guarda de `OP-D-03` quede verde, como manda el modo continuo.

## EL ENCARGO SIGUIENTE COMPLETO (borrador listo para copiar)

Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

TAREA 1, registros:
1.1. Leer el acta de la vuelta 33 del auditor y la decision del fundador;
registrar las dos por su fecha en los documentos que tocan.
1.2. Aplicar la decision 1 [si es la opcion a: quitar en la simetrizacion de fase
0 el reciprocado de aristas que nacen en nodos deprecados, con caso positivo en
rojo y en verde, Gate 0 y las tres suites; re-correr el caso positivo de OP-D-02 y
publicar el 23 de 23 estable; correccion declarada en el plan de la fusion y en el
pendiente de doctrina 1].
1.3. Aplicar la decision 2 [arreglo de costuras_internas.py segun la letra del
fundador; recalibracion declarada en el docstring con las cifras de hoy y sus
nodos; correccion declarada de la cifra del acta 32 (bloque 0,0 contra 44) con
recomputo del apoyo del movimiento 2 de OP-D-01; y la puerta de calibracion valida
tambien importada].
1.4. Escribir UNA VEZ el criterio de la arista que falta de la tanda 724/755/827
(se declara donde hay madre e hijo del 9.6.2; no se declara donde el solape es
linea contra linea) donde las tres razones lo compartan.

TAREA 2, el trabajo:
2.1. Re-correr costuras sobre los seis nodos de OP-D-03 con el instrumento
recalibrado; identificar las TRES costuras que el orden interno manda destejer;
ejecutar el destejido tal como esta escrito, con simulacion previa sobre copia en
memoria, plan sellado, tabla de perdidas y caso positivo antes y despues, y el
ciclo de Gate 0 con las suites.
2.2. [Segun la decision 3] leer los pares internos de OP-D-03 como dirigidas en el
momento que el fundador fije, sin mover n, con los nodos impresos ENTEROS antes de
decidir y las aristas buscadas en los dos sentidos.
2.3. Seguir el modo continuo por el orden del 00_INDICE, con las guardas
obligatorias de siempre por operacion.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice
una regla vigente, paras y lo traes. No adivines.
