### TAREA 1. LOS REGISTROS. **CERRADA, Y CON UNA DISCREPANCIA DENTRO DEL ACTA QUE SE PUBLICA EN VEZ DE RESOLVERSE COPIANDO.**

**EL NUMERO DE LA ENTRADA NO SE TECLEA.** `scripts/loop/serie_de_registros.py`,
corrido en el bloque `G` de la apertura y otra vez dentro del registrador, da
**`R.56`** como siguiente libre sobre **47 entradas**, con **0 colisiones** y **0
huecos**. El encargo adelantaba `R.56` y **CALZA**, y esa palabra la escribe el
instrumento y no yo.

**LA ENTRADA ESCRITA:** `R.56` en `docs/PENDIENTES.md`. Contada de
`docs/loop/SALIDA_V194_T1A_REGISTRO_R56.txt`:
**10486 bytes en disco y 10486 bytes normalizado a LF**, **181 lineas** por
`count(NL)` y **182** por `split`, **0 guiones largos o medios**. La sede
`docs/PENDIENTES.md` pasa de **1029096 bytes** a **1039583 bytes**, y la entrada
se releyo del disco byte a byte.

**LA IDEMPOTENCIA NO SE AFIRMA: SE PROBO RE CORRIENDOLO**, con la sede medida en
bytes antes y despues. Segunda corrida:
`docs/loop/SALIDA_V194_T1A_RECORRIDO_SIN_ESCRIBIR.txt`
(12207 bytes en disco y 12207 bytes normalizado a LF), *"el acta
194 YA TIENE ENTRADA en la serie: 2 linea(s) la nombran. NO se escribe una entrada
nueva y NO se consume el numero R.57."* **docs/PENDIENTES.md sigue en 1039583
bytes**, la misma cifra por las dos medidas.

**LO QUE LA ENTRADA REGISTRA, TODO CONTADO DEL CUERPO ACOTADO DEL ACTA (lineas
68284 a 68708, 425 lineas) Y NADA DEL ENCARGO:**

| lo que se cuenta | del acta | cotejo |
|---|---:|---|
| adjudicaciones `4.1` a `4.10`, patron entrecomillado | 10 | el patron suelto da **0**, y las dos cifras se publican |
| discutibles `D.1` a `D.7`, todos A FAVOR | 7 | reparto por familia leido del titulo |
| preguntas `P.1`, `P.2` y `P.3`, contestadas por extension citable | 3 | |
| **`EN CONTRA`** | **0** | **CUARTA acta seguida**, y la guarda vieja de la 190 PARARIA aqui |
| hallazgos de la seccion 5 | 3 | los DOS lectores heredados dan **0** cada uno |
| discrepancias fuera del marcado, POR RESTA de la fila (5) menos los hallazgos (3) | 2 | la fila los cuenta juntos y su celda lo escribe |
| caidas propias del auditor, del CUERPO de la seccion 8 | **2** | **su fila de la tabla dice 1. NO CALZA** |
| caidas del ejecutor, de reporte | 1 | la fila nombra el hallazgo `5.2`, no una `C.n` |
| caidas del ejecutor, de metodo, con el rango expandido | 3 | `C.1` a `C.3`, y **CALZA** con su fila |
| actas sin entrada propia en la serie, tramo 173 a 193 | 8 | 173 a 180, y el encargo dice ocho: **CALZA** |

**LA DISCREPANCIA, DICHA ENTERA Y CON SUS DOS LINEAS.** El cuerpo de la seccion 8
del acta 194 (`## 8. MIS CAIDAS PROPIAS`, lineas 68646 a 68662) declara **DOS**
caidas propias del auditor, `C.1` en la linea 68648 y `C.2` en la 68654. **Su fila
de la tabla de credito, en la linea 68629, dice UNO** y solo nombra la `C.1`. **Las
dos lecturas son correctas: es el acta la que se contradice consigo misma.** Se
registra la del cuerpo, porque el encargo de esta vuelta dice literal *"cada cifra
se cuenta del cuerpo acotado del acta y no de aqui"* y ademas nombra **DOS**; y
**las dos cifras quedan publicadas en la entrada con su linea y su atribucion**.
**Es la misma especie que el propio hallazgo `5.2` del acta**, que levanta contra
el reporte de la 193 una seccion que dice cuatro donde el instrumento dice cinco.
**Lo registro y no lo adjudico: registrar no es adjudicar, y quien clasifica las
caidas del auditor es el auditor.** Va marcado como discutible abajo.

**Y NINGUNA GUARDA SE AFLOJO PARA PODER DECIRLO.** El registrador de la 193 PARABA
cuando el cuerpo y la fila no calzaban, y esa parada existia para cazar **un error
de lectura del propio registrador**. Aqui no hay error de lectura, asi que:

- **la parada por descuadre SIGUE ENTERA** para la fila del ejecutor de metodo,
  que es donde la lectura si podria fallar (3 claves del rango contra 3 de la
  fila, y CALZA);
- **la parada por especie no declarada SIGUE ENTERA**: la `C.1` sale **SIN
  ESPECIE** con el vocabulario de la 193 y el registrador PARARIA, asi que el
  vocabulario CRECE en una marca literal del acta, `ROMPER UN REMEDIO ESCRITO`, y
  **una caida muda sigue haciendo PARAR**;
- **y SE ANADE UNA GUARDA NUEVA**, `entrada_publica_las_dos()`: si hay descuadre y
  la entrada armada no lleva **las dos** cifras en su tabla de cotejo Y la frase
  que declara el descuadre, el registrador **cae en rojo y no escribe nada**. Una
  discrepancia callada seria peor que la parada que sustituye.

**LO QUE ESTE REGISTRADOR ESTRENA, Y POR QUE NO ERA OPCIONAL.** El acta 194 cambia
de forma en tres sitios y **los tres estaban medidos antes de escribir una linea
de la entrada**:

1. **los hallazgos son titulares `###` y no negritas**: `claves_de_adjudicacion` da
   **0** y `claves_entrecomilladas` da **0** sobre esta acta, y con cero el
   registrador PARARIA por no encontrar hallazgos que el acta si tiene. Se anade
   `hallazgos_en_titular()`, **lector ANADIDO y no ensanche**: los dos viejos
   siguen intactos y sus cifras se publican al lado;
2. **las caidas propias viven en la seccion 8 y no en la 6**, porque en el acta 194
   la 6 es PENDIENTES DE DOCTRINA. Se anade
   `caidas_propias_entrecomilladas()`, con **el rango por parametro**, para que el
   lector no suponga la seccion;
3. **la fila de puestos ya no dice `SOLAPE TOTAL`: dice `ONCE QUEMADOS`.** La nota
   heredada **no aparece** en esta acta (buscada y medida), y el registrador de la
   193 PARARIA por eso. **La vieja se conserva y se sigue buscando**: retirarla
   estrecharia el vocabulario a lo que el acta de hoy usa.

**LA FILA DE PUESTOS, REGISTRADA CON SU NOTA Y SUS TRES CIFRAS**, leidas de la
celda y no parafraseadas: **30 aislados**, **30 cotejados**, **once quemados por el
contexto de sesion y no por comando del auditor**, y **el cotejo limpio va sobre
19**. **El cotejo se publica dos veces**, sobre los 30 y sobre los 19. Un quemado
no es un solape: **el solape mide si dos lectores leen lo mismo; el quemado dice
que uno de los dos ya sabia lo que el otro habia dicho antes de leer.**

**EL CASO POSITIVO POR MUTACION, CORRIDO Y NO PROMETIDO:**
`docs/loop/SALIDA_V194_T1A_MUTACION_REGISTRADOR.txt`
(4074 bytes en disco y 4074 bytes normalizado a LF), **VEREDICTO:
VERDE**, con **27 casos, 27 pasan y 0 fallan**, cifra que ese mismo fichero
publica de si mismo en su linea `CIFRA casos` y que por eso `cerrar_reporte.py`
puede cotejar contra esta prosa. Cada trozo
nuevo es PURO y se corre sobre texto **fabricado**, con el valor esperado sacado de
como se fabrico y no de una constante igual a la obtenida. Las mutaciones que
importan, nombradas: **la misma entrada sin la frase que declara el descuadre CAE**;
**una entrada que publica una sola cifra CAE**; **una caida sin especie sigue
saliendo SIN ESPECIE con el vocabulario nuevo**; y **los dos lectores heredados
sobre el texto fabricado dan cero**, que es lo que prueba que el nuevo es un
anadido y no un ensanche.
