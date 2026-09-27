# Limpieza M11: evidencia (integracion del mundo 11, paso 3, 28 sep 2026)

Decisiones del fundador del 28 sep 2026 (voz de libro fuera, 471 resumenes nuevos, notas_extraccion interno).
Instrumento: `docs/saneamiento/instrumentos/M11_LIMPIEZA.md`. Tandas aplicables (en orden) sobre el pack importado:
`docs/saneamiento/tandas/m11-limpieza.json` (5452), `m11-glosario.json` (130), `m11-limites.json` (21).

- `redactor/lote_NN.json`: lo que escribio cada redactor (40 lotes, 12 nodos + 1 trampa).
- `verificador/salida_NN.json`: el juicio del verificador ciego por elemento. Sus entradas se regeneran con
  `herramientas/preparar_verificador.py NN` (semilla 20260929+NN); las entradas de los lotes con
  `herramientas/preparar_lotes.py` (semilla 20260928) sobre el pack importado con `scripts/importar_forja.py`.
- `arbitro/`: los casos FALLA reales y la decision del arbitro.
- `ajustes_orquestador.json`: los textos finales que el orquestador fijo sobre lo arbitrado, cada uno con su motivo
  (barandas de la casa, pase de matices).
- `matices/`: el pase de matices (resumenes de los lotes 01 a 31 y textos con experiencia de autor), lector + arbitro.
- `glosario/`: DECISIONES.md, propuestas, verificador y la resolucion del orquestador.
- `limites/`: el arbitro de los casos que los verificadores dejaron en OK senalados como dudosos.
- `muestra/`: la muestra ciega final (25 nodos, semilla escrita antes de sortear, 3 trampas sin marca).
- `claves/`: las claves de todas las trampas.
- Las lineas de los libros que llevaban las entradas se retiraron del repo (texto con derechos); quedan fichero y
  lineas como referencia.

FALLO DE METODO DECLARADO: las trampas del redactor, del verificador, del pase de matices y del glosario llevaban
nombre visible (trampa_NN, vtrampa_, mtrampa_, gtrampa_). Sus puntuaciones no prueban ceguera. Las trampas del
arbitro de limites y de la muestra final se plantaron sin marca, en ids reales: 1 de 1 y 3 de 3 cazadas.

## Auditoria completa y barrido (28 sep 2026, tras la muestra ciega que dio 57 defectos en 19 de 25 nodos)

Umbral del fundador fijado ANTES de medir (claves/umbral_y_semilla_auditoria.json): en la muestra ciega final, cero
invenciones y cero contrarios; matices, calcos y coherencia como maximo 1 por cada 5 nodos (lectura estricta: tambien
regionalismo, voz y ortografia dentro del tope). Todas las trampas sin marca y en ids reales.

- `auditoria/`: 19 auditores ciegos (471 nodos, reparto con semilla 20261005, `auditoria/repartir.py`), 24 trampas sin
  marca, 24 cazadas. 952 defectos marcados; 892 campos al arbitro: 842 corregidos (ANADIDO 382, VOZ 292, COHERENCIA 143,
  CONTRARIO 16, ORTOGRAFIA 9) y 50 que no se sostuvieron. Tanda `m11-auditoria` (842 en 372 nodos).
  Dos fallos del orquestador, corregidos y declarados: la primera version de las instrucciones daba "agresividad
  molesta" como nombre fijado (el pack usa "agresion odiosa"; los arbitros lo rechazaron); y el consolidador descartaba
  todo defecto del campo de una trampa, tambien los reales (3, arbitrados aparte en el lote X).
- `barrido/`: los calcos que la auditoria dejo repetidos ("a que se parece", "abastecer", "por delante" como up front,
  "que suban la voz", "ensenar mejora"); redactor, verificador ciego con 1 trampa sin marca (cazada). Tanda `m11-barrido` (37).
- La herramienta admite ahora CONTRARIO, ANADIDO y COHERENCIA sobre `titulo_concepto` (con su cita), con su caso en rojo
  primero en `engine/test_correcciones_mundo11.py`.
- Orden de las tandas sobre el pack importado: m11-limpieza, m11-glosario, m11-limites, m11-auditoria, m11-barrido.

## Muestra ciega final 1, segundo pase y barrido de "salida" (28 sep 2026)

- `muestra_final/`: 50 nodos con semilla 20261006, dos auditores ciegos (F1, F2), 4 trampas sin marca en ids reales,
  4 cazadas. El arbitro confirmo 23 defectos: 0 invenciones y 0 contrarios, 23 del resto (VOZ 11, ANADIDO de matiz 7,
  COHERENCIA 5) contra un tope de 10. Veredicto: NO CUMPLE (`claves/resultado_muestra_final_1.json`). Las 23
  correcciones van en la tanda `m11-muestra-final` (15 nodos).
- `pase2/`: segundo pase solo sobre las categorias que fallaron (matiz, calco, coherencia, regionalismo, voz,
  ortografia) en los 471 nodos, 24 auditores con reparto de semilla 20261008 y 28 trampas sin marca: 26 cazadas.
  FALLA DECLARADA: dos trampas de matiz no se cazaron (lotes 02 y 10, en pasos). Las trampas solo viven en la entrada del
  auditor, no en el pack; lo que prueban es que el auditor deja pasar parte de los matices, y eso es lo que mide la
  muestra final 2. 761 defectos marcados; 696 campos al arbitro: 673 corregidos (VOZ 429, ANADIDO 153, COHERENCIA 82,
  ORTOGRAFIA 6, CONTRARIO 3) y 23 que no se sostuvieron. Tanda `m11-pase2` (673 en 335 nodos).
- `salida/`: "salida" como calco de output pasa a "produccion" (operacion) o "resultado" (mando, unidad, proceso); se
  queda cuando va en par con "entrada". Verificador ciego con 1 trampa sin marca (cazada) y 1 falla real de concordancia
  resuelta con su propuesta. Tanda `m11-salida` (15 en 3 nodos).
- Reproducibilidad: las ocho tandas aplicadas en orden sobre el pack importado dan la copia limpia exacta (471 de 471
  nodos iguales). Guarda de voz de cliente: 0 faltas en 471 nodos.
- Orden de las tandas sobre el pack importado: m11-limpieza, m11-glosario, m11-limites, m11-auditoria, m11-barrido,
  m11-muestra-final, m11-pase2, m11-salida.
- La muestra ciega final 2 (semilla 20261009, escrita antes de sortear) se mide despues de este commit.
