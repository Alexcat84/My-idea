# PARA ALEXIS: EL BUCLE SE DETIENE POR RACHA DE CAIDAS DE REPORTE (26 ago 2026, vuelta 79, auditor Opus 5)

## EL MOTIVO, EN UNA FRASE

Tres vueltas seguidas (77, 78 y 79) con al menos una afirmacion equivocada en
el REPORTE, y la regla que tu mismo afinaste el 13 ago dice que tres de la
misma especie ya no son ruido sino patron de dictado suelto: **PARADA**.

**LO IMPORTANTE PRIMERO: LOS DATOS ESTAN VERDES.** Esta parada es de higiene
de dictado, no de integridad del catalogo. **CERO caidas de clase y CERO de
cifra publicada** en esta tanda, y esa racha sigue en cero. Todo lo que la
vuelta 79 toco lo verifique al digito por corrida propia: las 12 aristas
nuevas y sus reciprocas, la reversion en sus dos vistas, la escalera, el
censo, las tres suites, el marcador, la bolsa medida en dos puntos, el filtro
cotejado **fila a fila**, y el instrumento nuevo entero con sus tres varas mas
una diferencia que inyecte yo.

## LA CAIDA, EXACTA, EN CUATRO LINEAS

El reporte de la vuelta 79 publica en su seccion 0:

> *"Commit de apertura: `43b02413` (acta de la vuelta 78, [...] verificado con
> `git rev-parse HEAD` y `git rev-parse origin/pasada-unica`)."*

- **`43b02413` es el commit de la TAREA 4 de esa misma vuelta 79**, escrito
  por el propio ejecutor a mitad del trabajo. La apertura es **`aea7cc81`**,
  el acta de la vuelta 78.
- **El arbol del hash publicado contradice la propia tabla del reporte**: mide
  8.948 / 8.927 / 17.875 / 9.571, y la columna apertura publica
  8.949 / 8.928 / 17.877 / 9.572, que es lo que mide `aea7cc81`.
- **No mueve ningun dato.** La medicion de apertura es correcta; lo que esta
  mal es el nombre publicado al lado. Es la especie barata, y es la tercera
  seguida.

## LO QUE MAS TE INTERESA, Y ES NUEVO

**El remedio que elegiste el 26 ago 2026 funciona, y la caida entro por el
borde de su perimetro.**

La escalada automatica de la opcion (b) se disparo sola en la vuelta 78 y fue
la TAREA 2 BLOQUEANTE de la 79: `scripts/loop/tallar_cabecera_reporte.py`
gano un modo `--fase04`. **Lo probe entero yo mismo y sale bien por las tres
varas:**

| vara | resultado de MI corrida |
|---|---|
| tallar la vuelta 79 | tabla **identica celda por celda** a la cabecera del reporte |
| `--comparar docs/loop/REPORTE.md` | 6 filas cotejadas, **0 distintas, 0 ausentes** |
| ROJO con `--vuelta 999` | **32 celdas no leidas, no talla nada, exit 1** |
| **diferencia inyectada por mi** (`25/25` por `24/25`) | la nombra exacta: **DISTINTA, motor, apertura**, exit 1 |
| caso positivo contra la vuelta 78 | **las 25 cifras dan IGUALES** |

**Pero el tallador talla SEIS FILAS: censo, Gate 0, aristas, motor, web y
tsc.** La linea del commit de apertura **no es una de esas seis**: es prosa
suelta encima de la tabla, y siguio siendo una frase tecleada. **Ahi entro la
caida.** Es la tercera vez que la racha se rompe por algo que el instrumento
no cubria todavia: el `623` de la vuelta 56, el `13/12` de la 76, y ahora un
hash.

## EL ESTADO EXACTO

- Rama **`pasada-unica`**, HEAD de la vuelta 79 en **`3b97cf58`** (esta acta y
  este documento van encima). `origin/pasada-unica` igual a `HEAD` al empezar
  mi auditoria.
- **Censo: 3.853 nodos, 3.188 vivos, 665 deprecados.** Sin cambio.
- **Gate 0: OK** por corrida propia mia, con el ciclo de tres entero.
  Auto-aristas 0, duplicadas de titulo 0, alias con dos duenos 0, los dos
  `master_graph` con 0 divergentes, alcanzabilidad 100,0% (3.188 de 3.188, 85
  semillas), enlaces rotos 0.
- **Aristas: 8.960 `nodos_siguientes` / 8.939 `nodos_previos` / 17.899 suma /
  9.583 union**, cero auto-aristas y cero duplicadas dentro de una lista.
- **Suites: motor 25/25; web 80 ficheros, 1.030 pasadas y 3 saltadas; `tsc`
  exit 0 y cero lineas.** Las tres corridas por mi.
- **Marcador del cribado: A 551, B 72, C 5, D 2.760, n 3.388**, cero huecos y
  cero duplicados. La fase 04 no lo toca.
- **Fase: 04 ENLACES, abierta.** `OP-E-01` en curso: cinco tramos hechos,
  **114 aristas acumuladas de la fase 04** y **137 candidatos filtrados sin
  leer** del corte de esta vuelta (de 167 tras el filtro `P.9.1` ensanchado y
  la guarda del par no dirigido).
- **Plan: 71 operaciones, 70 LISTA y 1 HECHA** (`OP-E-02`, cerrada en la
  vuelta 76).
- **El merge a staging o a produccion sigue siendo tuyo y no del bucle.**

## LO QUE DEJO ADJUDICADO, PARA QUE NO SE PIERDA

De la relectura ciega de los cuatro discutibles marcados (acta completa en
`docs/loop/ACTA_AUDITOR.md`, vuelta 79):

- **DOS se cierran a favor y por cita**, sin doctrina nueva: el near-duplicate
  de "causas comunes y especiales" **no existe** (el tercer nodo esta
  DEPRECADO, lo medi), y la clase D del puesto 2324 **no sienta precedente**
  (la letra de clase contesta si el par se FUNDE, no si se ENLAZA; el enlace
  lo contesta el banco 9.6, que el propio veredicto cita por numero).
- **DOS van a relectura conjunta** y quedan pendientes de que el bucle se
  reanude:
  1. `producto_mercado_fit_motores -> afinar_motor_crecimiento`. **Es un radio
     sobre una cadena completa**: los tres pasos del framework de contabilidad
     de la innovacion ya cuelgan encadenados del nodo que el paso 4 nombra
     literalmente. Lo mata el CAVEAT MEDIDO del banco 9.6.1 (*"antes de
     contar, se mira la FORMA"*) y la definicion misma de la 9.6 (el contenido
     no era inalcanzable). Es el mismo error que la propia 9.6 ya se corrigio
     a si misma con `proceso_diseno_modelo_negocio_5_fases`.
  2. `terminologia_clave_breakthrough -> analisis_sintomas`. **El hijo
     caracteriza el sintoma; el paso manda diferenciarlo de la causa.** Es la
     misma especie que esta misma tanda revirtio en un caso y rechazo en otro.
- **La observacion tecnica sobre Gate 0 queda cerrada y NO es un fallo.** La
  reproduje sellando antes: tras una segunda corrida de `run_phase1.py` el
  Gate dice 0 divergentes y en disco hay 71. **Es diseno declarado en el
  codigo** (comparar el intermedio pondria el Gate en rojo siempre); el motor
  cubre el estado en disco y corre despues del ciclo. La disciplina que lo
  cierra ya esta escrita y aplicada: el ciclo de tres se corre exactamente una
  vez cada comando, en orden.
- **VARA NUEVA, por cita y sin doctrina nueva:** antes de escribir una arista
  de la fase 04, medir si el hijo **ya cuelga de la cadena de la madre**. La
  corri sobre las 12: cinco tenian camino previo, y **una** de ellas era la
  cadena de la propia familia (la del punto 1 de arriba).

## DOS OBSERVACIONES MEDIDAS QUE NO SON PARADA Y QUE NADIE HABIA CONTADO

1. **149 pares del grafo estan escritos en los DOS sentidos**
   (`a -> b` y `b -> a` en `nodos_siguientes`). **Son todos previos: la vuelta
   79 no anadio ni uno.** Es la version escrita en el grafo de la misma
   enfermedad que la guarda del par no dirigido ataca en la bolsa. No es de
   esta fase, pero queda medido y nombrado.
2. **644 aristas viven solo en `nodos_siguientes` y 623 solo en
   `nodos_previos`.** Iguales en la apertura y al cierre, o sea estado previo
   sin cambio. Lo digo porque la fase 04 escribe siempre en las dos vistas y
   conviene saber que el punto de partida no era simetrico.

## LO QUE NECESITO DE TI

**Una decision sobre la racha, y opcionalmente una sobre el remedio.** Las
opciones, con lo que cuesta cada una:

- **(a) Poner la racha a cero y seguir**, como el 26 ago. Barato e inmediato.
  El riesgo esta medido: es la tercera vez que pasa, y las tres veces la
  caida entro por un sitio que el instrumento no cubria.
- **(b) Ensanchar el perimetro del tallador a la prosa de identidad**, que es
  donde entro esta: que el modo `--fase04` talle tambien **la linea del commit
  de apertura**, leyendola de `git rev-parse` y del `git log` de la rama en
  vez de dejarla tecleada, y que `--comparar` la cotoje como una fila mas. Es
  el mismo remedio que ya elegiste dos veces, aplicado al borde por donde se
  escapo. Barato: el instrumento ya existe y funciona.
- **(c) Otra cosa**, si el patron te dice algo que a mi se me escapa: tres
  vueltas seguidas con una frase suelta cada una, siempre fuera de lo tallado,
  y siempre sin mover un dato.

**No hace falta que toques modelos por mi cuenta.** El ejecutor Sonnet 5 esta
haciendo el trabajo de lectura y de medicion bien: cero caidas de clase y cero
de cifra publicada en dos vueltas seguidas, el filtro sale fila a fila, y la
TAREA 2 bloqueante quedo bien construida y bien probada. Lo que falla es la
prosa que envuelve las cifras, no las cifras.

## COMO RETOMAR

1. Escribe tu decision al final de este mismo fichero, como en las paradas
   anteriores (`DECISION DEL FUNDADOR (fecha): ...`).
2. Relanza el bucle. El encargo de la vuelta de reanudacion, ya escrito para
   que se copie a `PROMPT_SIGUIENTE.md`:

- **TAREA 1, los registros y la correccion declarada.** (1.1) Registrar la
  caida de reporte de la vuelta 79 con su nombre: `43b02413` publicado como
  commit de apertura siendo el commit de la TAREA 4 de esa misma vuelta; la
  apertura es `aea7cc81`. **No se vuelve a medir: ya viene medida.** (1.2)
  Corregir la linea en `REPORTE.md` con el texto viejo delante y sin
  reescribirlo. (1.3) Registrar las seis adjudicaciones del acta 79 (seccion
  5), incluida la vara nueva de la cadena y el cierre de la observacion
  tecnica de Gate 0.
- **TAREA 2, el remedio que decidas**, si eliges la (b): que el tallador
  `--fase04` talle la linea del commit de apertura desde `git rev-parse` y
  `git log`, con su mecanica de ROJO y con `--comparar` cotejandola, y **caso
  positivo obligatorio** contra la vuelta 79 (debe salir `aea7cc81` y NO
  `43b02413`).
- **TAREA 3, las dos relecturas conjuntas** de la seccion 5 del acta 79, con
  mi caso escrito y verificado contra el grafo antes de decidir. Si se
  revierten, **quitando las dos vistas a la vez**, con correccion declarada y
  recomputo.
- **TAREA 4, la relectura al doble del tramo 5** por el credito rebajado
  (`AUDITOR.md` seccion 1.2, la caida cayo fuera del marcado): cruzar las 12
  aristas escritas contra `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` sin direccion,
  y contra la bolsa buscando la reciproca, las dos con tabla contada de su
  fichero.
- **TAREA 5, el tramo 6 de `OP-E-01`**, recalibrando la bolsa antes de leer
  (el grafo se movio con las 12 de esta vuelta), con el filtro `P.9.1`
  ensanchado, **la guarda del par no dirigido** y **la vara nueva de la
  cadena** corridas antes de leer nada.

`docs/loop/PROMPT_SIGUIENTE.md` queda **VACIO** como la parada manda.

## DONDE ESTA TODO

- Acta completa de la vuelta 79: `docs/loop/ACTA_AUDITOR.md`, desde la linea
  23340 (verificacion al digito, ciega de los cuatro discutibles,
  adjudicaciones, mis propios manejos y la metrica de credito).
- Mis ficheros de salida, commiteados al lado: `docs/loop/_auditor_v79_*`.
- El reporte que audite: `docs/loop/REPORTE.md`.
- La decision anterior sobre esta misma racha:
  `docs/loop/paradas/2026-08-26-racha-tramo-mecanico-DECISION.md`.
