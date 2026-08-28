Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION, FASE 05 SANEO. RAMA pasada-unica.
MODO DE EJECUCION CONTINUA (AUDITOR.md seccion 3) y MODO AUSTERO
(AUDITOR.md seccion 6, EJECUTOR.md al final), con las guardas
obligatorias por operacion.

La decision del fundador que desbloquea esta vuelta esta en
docs/loop/paradas/2026-08-28-titulo-nafta-ops01-DECISION.md, y la parada
entera en docs/loop/paradas/2026-08-28-titulo-nafta-ops01.md. En resumen:
SALIDA B con texto exacto, el barrido NO entra a la campaña, y OP-S-01 se
declara CUMPLIDA CON REMISION. Visto tambien al encargo de codigo de la
seccion 6 de la parada, que es la TAREA 1 y va PRIMERA.

- TAREA 1, EL ARREGLO DE LA SECCION 6, Y VA ANTES DE TOCAR OP-S-01 O
  OP-S-09, que son las dos que mueven ids y que la atadura 1 pone detras
  de la fase 0. La via equivalente de OP-C-05 tiene su caso positivo
  ROTO: scripts/loop/vuelta89_tarea4_guarda_op_c05.py --caso-rojo se para
  siempre con "ROJO: dataset/ ya tenia cambios antes del caso rojo",
  porque su guarda de limpieza mira git status --porcelain -- dataset/,
  que SIEMPRE ve la M espuria de fin de linea. FICHERO NUEVO con la via
  equivalente cuya guarda de limpieza MIDE CONTENIDO: git diff --numstat
  -- dataset/ en CERO LINEAS, no estado. LA GUARDA VIEJA NO SE TOCA: el
  fichero de la vuelta 89 se queda como esta. Y EL CASO ROJO SE CORRE Y
  SE PEGA antes de dar la fase 0 por probada, porque la fila 0 del plan
  dice que una guarda que nunca fallo no esta probada y una guarda cuyo
  caso positivo no puede correr esta en ese mismo sitio. El caso rojo se
  prueba POR MUTACION sobre una variable que el codigo compute (EJECUTOR
  regla 1), no sobre un literal.
- TAREA 2, LOS REGISTROS DEL ACTA 118 en docs/PENDIENTES.md, incluida la
  CORRECCION DE ATRIBUCION que el auditor declara con treinta vueltas de
  retraso: su acta 88 escribio que la via equivalente de OP-C-05 "la
  autoriza la ficha misma" y ES FALSO, porque FASE_0_CODIGO.md no
  contiene las palabras "equivalente", "no crezca" ni "antes y despues";
  la via equivalente es una ADJUDICACION POR EXTENSION DEL AUDITOR y su
  cita correcta es EL ACTA 88 SECCION 5.4. La adjudicacion se sostiene;
  lo que se corrige es la atribucion, con correccion declarada y sin
  borrar el texto viejo.
  Y LA ANOTACION DEL BARRIDO en la ficha vigencia-del-marco-internacional
  de PENDIENTES.md, por la decision 2 del fundador: los CUATRO nodos
  vivos que nombran NAFTA y que NO entran a la campaña quedan anotados
  ahi como trabajo post campaña, por su id:
  certificado_de_origen_coo, documentacion_exportacion, regla_de_minimis
  y reglas_origen_sectoriales.
- TAREA 3, EJECUTAR EL RESTO DE OP-S-01 CON LA DECISION DELANTE.
  (3.1) EL TITULO. El titulo_concepto del superviviente
  certificado_de_origen_tratados_libre_comercio pasa al TEXTO EXACTO de
  la decision: Certificado de Origen y Tratados de Libre Comercio
  (T-MEC/USMCA, Rules of Origin, RVC). Por CORRECCION DECLARADA, sin
  borrar el texto viejo, y con EL CICLO DE GATE 0 Y LAS SUITES corridos
  despues. T-MEC va primero por la voz en espanol del producto y USMCA
  como sigla internacional buscable; CUSMA NO va al titulo y puede vivir
  en el cuerpo como denominacion alterna.
  (3.2) EL PUNTO 4 SE ACOTA por correccion declarada A LA NOMINA DE LA
  OPERACION, citando que el barrido global vive en la ficha
  vigencia-del-marco-internacional. No se reescribe el punto: se acota su
  alcance y se dice por que, con la decision citada.
  (3.3) LA OPERACION SE DECLARA CUMPLIDA CON REMISION EN SU NOTA: su acto
  material lo consumio la fase 03 en la vuelta 57 (commit a1d7269d, 20
  ago 2026), y el punto 4 queda remitido a la ficha por la decision del
  fundador.
  (3.4) Y DESPUES OP-S-02 EN ADELANTE, en MODO CONTINUO y AUSTERO, con
  las guardas completas por operacion.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
