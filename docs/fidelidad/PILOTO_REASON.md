PILOTO LISTO. Recall de CONTRARIOS: 17 de 17 (los 16 sinteticos y el conocido de prevalencia_omisiones, paso 2). Recall de ANADIDOS: 12 de 12 detectados; 10 de 12 con INFERIDO-ANADIDO como etiqueta principal (los otros 2 salen CONTRARIO con el dato inventado marcado, por la regla de que el contrario manda). Tres decisiones quedan para el fundador (seccion 1).

# Piloto de fidelidad total sobre Reason

Rama `fidelidad-total` de Alexcat84/My-idea, 25 sep 2026. Todo con `claude-opus-5-5`, las dos pasadas incluidas. `dataset/` no se ha tocado: todo vive en `docs/fidelidad/`. La campania completa NO se ha lanzado.

## 0. Las cifras en corto

| Medida | Valor |
|---|---|
| Nodos vivos del catalogo (no deprecados, puerta `esOfrecible` de `web/lib/engine/graph.ts` en main) | 3169 nodos, 15311 pasos, 61 valores de `fuente` |
| Pasos verificables hoy (texto .txt o .md del libro disponible) | 15311 de 15311 |
| Reason | 90 nodos vivos, 403 pasos |
| Recall de contrarios (intento final) | pasada 1: 17 de 17; pasada 2: 17 de 17 |
| Recall de anadidos (intento final) | pasada 1: 12 de 12; pasada 2: 12 de 12 con el dato detectado, 10 de 12 con la etiqueta principal |
| Tasa de marcado de la pasada 1 sobre los 403 pasos reales | 56,8 % con las dos marcas (solo contrarios: 33,5 %) |
| CONTRARIOS reales en Reason | 14 en el intento final; 17 en la union de dos corridas a ciegas; 8 en ambas |
| INFERIDO-ANADIDO reales en Reason | 24 en el intento final; 25 en la union; 13 en ambas |
| Coste medido del piloto entero (873 llamadas) | 149,41 USD |
| Coste por paso | 0,104 USD solo contrarios; 0,149 USD contrarios mas anadidos |
| Proyeccion de la campania (15311 pasos, 61 fuentes) | 2003,89 USD solo contrarios; 2691,90 USD contrarios mas anadidos |

## 1. Decisiones para el fundador

1. **La precedencia entre CONTRARIO y ANADIDO.** El encargo pide que la pasada 2 clasifique como INFERIDO-ANADIDO todos los anadidos sinteticos. En el intento final lo hace con 10 de 12. Los otros dos (A08 e A09) salen CONTRARIO con `tambien_anadido = true` y el dato inventado listado. No es un fallo de deteccion. Es la regla "los CONTRARIOS siguen siendo la prioridad absoluta": los dos sinteticos, ademas de inventar un dato, chocan con el libro. A08 organiza la medicion en cuatro factores y deja fuera dos de las seis dimensiones que el libro exige muestrear (L2750: "What matters is that a principled attempt is made to sample each of the six main dimensions"). A08 salio asi en las dos corridas: el generador fabrico un caso defectuoso. A09 queda en la frontera: salio ANADIDO en el intento 2 y CONTRARIO en el 3. Propongo mantener la precedencia (un paso asi se corrige por las dos cosas) y contar el recall de anadidos como "detectado". Si el fundador quiere la etiqueta principal estricta, hay que invertir la precedencia, y eso choca con su propia regla.
2. **Una corrida o dos de la pasada 2.** Hice la prueba entera dos veces, con dos mezclas a ciegas independientes (intentos 2 y 3). Los sinteticos salieron 17 de 17 las dos veces, pero los contrarios REALES variaron: 11 en una corrida, 14 en la otra, 8 en ambas y 17 en la union. Los 9 que salieron en una sola corrida son casos de frontera (matiz, condicion quitada, "solo" que excluye), no errores gruesos. La pasada 1 los marco en ambas. Lo que varia es el juicio final. Recomiendo pasar dos veces la pasada 2 sobre los pasos marcados "podria contradecir" (42,2 % en Reason) y unir los CONTRARIO, al menos en el tramo 1. Eso anade unos 0,076 USD por paso: tramo 1 (1230 pasos) unos 94 USD, catalogo entero unos 1170 USD. La decision es del fundador.
3. **La atribucion en la app (seccion 10).** La app NO muestra al usuario ni la fuente ni el autor de ningun nodo o paso, y el redactor del plan tiene prohibido nombrar autores. No hay "segun" ni "dice" que cambiar. Si algun dia se muestra la fuente, propongo la forma "Basado en (libro)" y nunca "segun (autor)". Queda como decision para el fundador; no he cambiado nada.

## 2. FASE 0: inventario y cobertura

Metodo (`herramientas/inventario.py`, salida `INVENTARIO_NODOS.jsonl` e `INVENTARIO_LIBROS.json`):

- **Nodo vivo**: `deprecado` no verdadero. Es la puerta `esOfrecible` de `web/lib/engine/graph.ts` en main (existe y no esta deprecado; el dominio depende del proyecto, no del nodo). En main hoy: 3853 nodos, 3169 vivos, 15311 pasos. El grafo de `web/lib/assets/` y el de `dataset/metadata/` tienen los mismos ids y los mismos pasos.
- **Libro**: el campo `fuente`. Siete nodos tienen fuente compuesta ("A | B"). Cuentan como verificables porque estan todos los textos. Dos nodos de Waltzing with Bears declaran ser "Sintesis de..." de la casa y se verifican contra el libro.
- **Carpetas miradas** (solo nombres, salvo el texto de un libro del catalogo): `I have an idea\books` y `\txt`, `OCR` (con `output`), `Downloads` (solo nombres de libros) y `forja-nodos\fuentes` (sin git). Todos los libros del catalogo tienen texto .txt o .md: **no hay ningun paso NO VERIFICABLE hoy**, y ningun libro depende solo de epub o pdf. Las copias epub y pdf existen para casi todos, pero no hacen falta.
- **Salvedades**: (a) "A Basic Guide to Exporting, 11th Edition": el txt es la edicion "Latest" del gobierno y hay que comprobar que es la misma antes de verificar ese libro. (b) Rushton: el texto completo solo esta en `Downloads\Supply chain`; en `txt\` hay solo un extracto. (c) "Requisitos de empaque de los couriers" apunta a una extraccion de la casa; las tres guias primarias (UPS, FedEx, DHL) tambien estan en txt. (d) Grove, Gerber y Marquet (la linea del arnes) aun no estan en main y no entran en este inventario.
- **Orden de riesgo**: tramo 1 seguridad y salud (Dekker, Reason, el manual OSHA de pequena empresa, OSHA3885, OSHA3886 y la guia FedEx, que trae mercancia peligrosa: baterias, UN 3373 y muestras clinicas); tramo 2 legal y dinero (inversion, socios, finanzas, franquicia, exportacion, garantias, ciberseguridad y privacidad NIST y FTC, riesgo de proyectos, compras y negociacion); tramo 3 el resto. Dentro de cada tramo, mas pasos primero.

### Cobertura (fase 0), en orden de riesgo

| Orden | Tramo | Libro (campo `fuente`) | Nodos vivos | Pasos | Verificables | NO verificables | Texto usado | Nota |
|---:|---|---|---:|---:|---:|---:|---|---|
| 1 | 1 | The Field Guide to Understandin - Dekker, Sidney | 102 | 424 | 424 | 0 | The Field Guide to Understandin - Dekker, Sidney;.txt |  |
| 2 | 1 | Managing the Risks of Organizat - Reason, J. T_ | 90 | 403 | 403 | 0 | Managing the Risks of Organizat - Reason, J. T_.txt |  |
| 3 | 1 | SMALL_BUSINESS | 46 | 238 | 238 | 0 | SMALL_BUSINESS.md | manual OSHA para pequena empresa |
| 4 | 1 | OSHA3885 | 15 | 84 | 84 | 0 | OSHA3885.md |  |
| 5 | 1 | Guia de empaque para envios (FedEx) | 9 | 44 | 44 | 0 | HowToPack_fxcom.txt | incluye mercancia peligrosa (baterias, UN 3373, muestras clinicas) |
| 6 | 1 | OSHA3886 | 7 | 37 | 37 | 0 | OSHA3886.md |  |
| 7 | 2 | Franchise Your Business - Mark Siebert | 182 | 828 | 828 | 0 | Franchise Your Business - Mark Siebert.txt |  |
| 8 | 2 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) | 131 | 665 | 665 | 0 | basic-guide-to-exporting_Latest_eg_main_086196.txt | el txt es la edicion 'Latest' del gobierno; comprobar que coincide con la 11.a |
| 9 | 2 | Venture Deals - Brad Feld | 131 | 585 | 585 | 0 | Venture Deals - Brad Feld.txt |  |
| 10 | 2 | The Founder's Dilemmas - Wasserman, Noam | 116 | 486 | 486 | 0 | The Founder's Dilemmas - Wasserman, Noam.txt |  |
| 11 | 2 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe | 76 | 348 | 348 | 0 | Financial Intelligence for Entr - Berman, Karen; Knight, Joe;.txt |  |
| 12 | 2 | Edwards et al., Managing Project Risks | 30 | 123 | 123 | 0 | Managing Project Risks - Peter J. Edwards.txt |  |
| 13 | 2 | NIST SP 1318: Protecting CUI (SP 800-171 r3) - Small Business Primer | 23 | 115 | 115 | 0 | NIST.SP.1318.txt |  |
| 14 | 2 | Diana L. Lindstrom, Procurement Project Management Success (J. Ross, 2014) | 23 | 114 | 114 | 0 | Diana L. Lindstrom - Procurement Project Management Success_ Achieving a Higher Level of Effectiveness-J. Ross Publishing (2014).txt | contratos de compra |
| 15 | 2 | Chris Voss, Rompe la barrera del no | 18 | 86 | 86 | 0 | Rompe la barrera del no_ 9 prin - Chris Voss.txt | negociacion |
| 16 | 2 | DeMarco y Lister, Waltzing with Bears | 15 | 63 | 63 | 0 | Waltzing with bears _ managing risk on software projects.txt |  |
| 17 | 2 | NIST SP 1314: Risk Management Framework - Small Enterprise Quick Start Guide | 11 | 45 | 45 | 0 | NIST.SP.1314.txt |  |
| 18 | 2 | Hubbard, The Failure of Risk Management | 10 | 40 | 40 | 0 | The Failure of Risk Management_ - Douglas W. Hubbard.txt |  |
| 19 | 2 | Businessperson's Guide to Federal Warranty Law | 11 | 40 | 40 | 0 | Businessperson's Guide to Federal Warranty Law.txt |  |
| 20 | 2 | NIST SP 1300: Cybersecurity Framework 2.0 - Small Business Quick-Start Guide | 6 | 35 | 35 | 0 | NIST.SP.1300.txt |  |
| 21 | 2 | Getting Started with the NIST Privacy Framework: A Guide for Small and Medium Businesses | 6 | 28 | 28 | 0 | Getting-Started-NIST-Privacy-Framework-Guide.txt |  |
| 22 | 2 | Cybersecurity for Small Business: Understanding the NIST Cybersecurity Framework (FTC) | 6 | 28 | 28 | 0 | cybersecurity_sb_nist-cyber-framework.txt |  |
| 23 | 2 | The Founder's Dilemmas - Wasserman, Noam | The Hard Thing About Hard Things - Ben Horowitz | 1 | 15 | 15 | 0 | The Founder's Dilemmas - Wasserman, Noam.txt; The Hard Thing About Hard Thing - Ben Horowitz.txt |  |
| 24 | 2 | Venture Deals - Brad Feld | The Founder's Dilemmas - Wasserman, Noam | 2 | 14 | 14 | 0 | Venture Deals - Brad Feld.txt; The Founder's Dilemmas - Wasserman, Noam.txt |  |
| 25 | 3 | Juran's Quality Handbook_ The C - Joseph A. Defeo | 459 | 2297 | 2297 | 0 | Juran's Quality Handbook_ The C - Joseph A. Defeo.txt |  |
| 26 | 3 | The Green to Gold Business Play - Daniel C. Esty | 209 | 933 | 933 | 0 | The Green to Gold Business Play - Daniel C. Esty.txt |  |
| 27 | 3 | The Startup Owner's Manual - Blank, Steve | 163 | 864 | 864 | 0 | The Startup Owner's Manual_ The - Blank, Steve.txt |  |
| 28 | 3 | Winning at New Products - Robert G. Cooper | 147 | 759 | 759 | 0 | Winning at New Products_ Creati - Robert G. Cooper.txt |  |
| 29 | 3 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev | 151 | 702 | 702 | 0 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev.txt |  |
| 30 | 3 | Essentials of Supply Chain Management - Michael H. Hugos | 95 | 535 | 535 | 0 | Essentials of Supply Chain Mana - Michael H. Hugos.txt |  |
| 31 | 3 | The Hard Thing About Hard Things - Ben Horowitz | 85 | 452 | 452 | 0 | The Hard Thing About Hard Thing - Ben Horowitz.txt |  |
| 32 | 3 | Quality is free _ the art of making quality certain -- Philip B_ Crosby | 82 | 406 | 406 | 0 | Quality is free _ the art of making quality certain -- Philip B_ Crosby.md |  |
| 33 | 3 | The Lean Startup - Eric Ries | 72 | 352 | 352 | 0 | The Lean Startup_ How Today's E - Eric Ries.txt |  |
| 34 | 3 | Traction - Gabriel Weinberg | 57 | 343 | 343 | 0 | Traction - Gabriel Weinberg.txt |  |
| 35 | 3 | Never Lose a Customer Again - Joey Coleman | 58 | 341 | 341 | 0 | Never Lose a Customer Again_ Tu - Joey Coleman.txt |  |
| 36 | 3 | Change by Design, Revised and U - Tim Brown | 73 | 335 | 335 | 0 | Change by Design, Revised and U - Tim Brown.txt |  |
| 37 | 3 | Assembling Tomorrow: A Guide to Designing a Thriving Future | 64 | 295 | 295 | 0 | Assembling Tomorrow_ A Guide to - Scott Doorley.txt |  |
| 38 | 3 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder | 61 | 283 | 283 | 0 | A Project Manager's Book of For - Cynthia Stackpole Snyder.txt |  |
| 39 | 3 | Business Model Generation - Osterwalder, Alexander | 48 | 243 | 243 | 0 | Business Model Generation_ A Ha - Osterwalder, Alexander.txt |  |
| 40 | 3 | Cradle to Cradle - Michael Braungart | 56 | 229 | 229 | 0 | Cradle to Cradle - Michael Braungart.txt |  |
| 41 | 3 | Value Proposition Design | 44 | 200 | 200 | 0 | Value Proposition Design - Smith, Alan, Osterwalder, Alexa.txt |  |
| 42 | 3 | SPIN Selling - Neil Rackham | 32 | 175 | 175 | 0 | SPIN Selling - Neil Rackham.txt |  |
| 43 | 3 | Co-Intelligence_ Living and Wor - Ethan Mollick | 39 | 173 | 173 | 0 | Co-Intelligence_ Living and Wor - Ethan Mollick.txt |  |
| 44 | 3 | The Art of Thought - Wallas, Graham | 40 | 160 | 160 | 0 | The Art of Thought - Wallas, Graham.txt |  |
| 45 | 3 | The field guide to human-centered design | 19 | 90 | 90 | 0 | The field guide to human-center - Unknown.txt |  |
| 46 | 3 | Rushton, Croucher y Baker, The Handbook of Logistics and Distribution Management | 14 | 63 | 63 | 0 | The Handbook of Logistics and D - Alan Rushton;Phil Croucher;Pete.txt | texto completo solo en Descargas; en txt/ hay un extracto |
| 47 | 3 | Sharon Cullinane, E-Logistics, Cap. 8 (B2C e-commerce y fulfilment) | 8 | 38 | 38 | 0 | E-logistics_Cap8_B2C_ecommerce_y_fulfilment.md | libro entero tambien en OCR/20260806 |
| 48 | 3 | Max Muller, Essentials of Inventory Management | 5 | 25 | 25 | 0 | Essentials of Inventory Managem - Max Muller.txt |  |
| 49 | 3 | ISTA 3P, Protocolo de ensayo de empaque para paqueteria | 5 | 24 | 24 | 0 | ISTA_3P_26-26_Overview.txt |  |
| 50 | 3 | The Startup Owner's Manual - Blank, Steve | Never Lose a Customer Again - Joey Coleman | Traction - Gabriel Weinberg | 1 | 23 | 23 | 0 | The Startup Owner's Manual_ The - Blank, Steve.txt; Never Lose a Customer Again_ Tu - Joey Coleman.txt; Traction - Gabriel Weinberg.txt |  |
| 51 | 3 | Guia visual de empaque | 4 | 20 | 20 | 0 | packaging_guide_infographic.txt |  |
| 52 | 3 | DHL Express, Guia de empaque | 3 | 15 | 15 | 0 | dhl_express_packing_guide_en.txt |  |
| 53 | 3 | Requisitos de empaque de los couriers | 3 | 14 | 14 | 0 | EXTRACCION_EMPAQUE_COURIERS.md | extraccion de la casa sobre las guias de UPS, FedEx y DHL; las tres primarias estan en txt |
| 54 | 3 | The Startup Owner's Manual - Blank, Steve | The Lean Startup - Eric Ries | 1 | 8 | 8 | 0 | The Startup Owner's Manual_ The - Blank, Steve.txt; The Lean Startup_ How Today's E - Eric Ries.txt |  |
| 55 | 3 | The Startup Owner's Manual - Blank, Steve | Traction - Gabriel Weinberg | 1 | 8 | 8 | 0 | The Startup Owner's Manual_ The - Blank, Steve.txt; Traction - Gabriel Weinberg.txt |  |
| 56 | 3 | The Lean Startup - Eric Ries | The Hard Thing About Hard Things - Ben Horowitz | 1 | 7 | 7 | 0 | The Lean Startup_ How Today's E - Eric Ries.txt; The Hard Thing About Hard Thing - Ben Horowitz.txt |  |
| 57 | 3 | The Startup Owner's Manual - Blank, Steve | Never Lose a Customer Again - Joey Coleman | 1 | 6 | 6 | 0 | The Startup Owner's Manual_ The - Blank, Steve.txt; Never Lose a Customer Again_ Tu - Joey Coleman.txt |  |
| 58 | 3 | Guia de empaque para transporte | 1 | 5 | 5 | 0 | Packaging_Guidelines.txt | guia de UPS |
| | | **Total** | **3169** | **15311** | **15311** | **0** | | |

## 3. Metodo de busqueda: medido y elegido

Troceado: el txt del fundador se parte en 493 fragmentos de unas 170 palabras con su linea (`Lnnn`), sin cruzar capitulos (10 capitulos detectados). Las notas quedan marcadas. El texto se sanea (raya a `--`) antes de todo. Los fragmentos viven fuera del repo, porque son el libro.

Se midieron cuatro metodos sin clave de Voyage. **Voyage queda SIN MEDIR** hasta que el fundador ponga la clave en una sesion con el delante. No la busque.

- **A, lexico solo**: BM25 propio con el titulo del nodo mas el paso, en espanol, contra el libro en ingles. Solo casa por cognados.
- **B, consultas traducidas mas lexico**: Opus 5.5 escribe 3 consultas en ingles por paso, en lotes barajados. BM25 por consulta, fusion RRF y la consulta del nodo con medio peso.
- **C, hibrido RRF**: B mas el ranking de A.
- **D, hibrido por turnos**: las mismas cinco listas de C, tomadas por turno rotatorio.

La vara: las lineas del pasaje de cada sintetico; L1943 y L2170 para el conocido; y 40 pasos reales al azar, con las lineas que Opus 5.5 senalo tras leer el libro entero numerado en una llamada. Acierto = algun fragmento recuperado contiene una linea de la vara (`MEDIDA_BUSQUEDA_i3.json`):

| Metodo | Sinteticos contrarios k=10 / k=20 | Anadidos k=10 / k=20 | Conocido k=20 | 40 reales k=10 / k=20 |
|---|---|---|---|---|
| A lexico solo | 14/16 / 14/16 | 8/12 / 9/12 | 1/1 | 28/40 / 30/40 |
| B traducidas + lexico | 14/16 / 15/16 | 12/12 / 12/12 | 1/1 | 38/40 / 40/40 |
| C hibrido RRF | 14/16 / 15/16 | 12/12 / 12/12 | 1/1 | 39/40 / 40/40 |
| **D hibrido por turnos** | 13/16 / **16/16** | 12/12 / **12/12** | **1/1** | 39/40 / **40/40** |

**Elegido: D con k = 20**. Es el unico que llega al 100 % de todas las varas. El lexico solo pierde un cuarto de los pasos reales. El sintetico que solo D recupera (S02, "despedir por un solo fallo") casa por el ranking en espanol y se perdia en la fusion RRF.

## 4. Las pasadas

Las dos con `claude -p --model claude-opus-5-5 --output-format json --tools "" --system-prompt ... --strict-mcp-config --no-session-persistence --max-turns 1`, desde un directorio de trabajo fuera de los repos, con como mucho 4 procesos a la vez y sin subagentes. La pasada 2 lleva `--effort high`; la pasada 1 usa el esfuerzo por defecto.

- **Declaracion de modelo.** Por la correccion del fundador ("hazlo siempre con opus 5.5"), las dos pasadas usan Opus 5.5. **Nunca se lanzo nada con claude-sonnet-5**, asi que no hubo nada que descartar. En las tres primeras etapas (generar sinteticos, traducir consultas, oro) el CLI hizo por su cuenta una llamada auxiliar a un modelo pequeno (claude-haiku-4-5), que aparece en el coste y no decidio nada. Desde la pasada 1 se apago (`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1`). Tambien se apago la cache de prompt, que cuesta el doble al escribirse y no se reutiliza. Cada llamada de las pasadas es solo Opus 5.5.
- **PASADA 1, alto recall**: lotes de 4 pasos barajados, con id opaco, nodo, resumen, paso y sus 20 fragmentos. Dos marcas independientes: `podria_contradecir` (cualquier indicio de choque, o fragmentos que no tratan el asunto; ante la duda, marca) y `dato_concreto` (numero, plazo, frecuencia, herramienta, norma o ley, rol o responsable). Cualquiera de las dos manda el paso a la pasada 2.
- **PASADA 2, a fondo**: un paso por llamada, con el nodo completo (titulo, resumen, entregable y los otros pasos), los capitulos ENTEROS donde caen sus mejores fragmentos (hasta 2), el resto de fragmentos y la sospecha de la pasada 1, avisando de que puede estar equivocada. Devuelve el veredicto, las lineas, una cita literal, los datos sin respaldo y el paso fiel.
- **Veredictos, definicion literal** (tambien en la cabecera de `VEREDICTOS_PASOS.jsonl`):
  - CONTRARIO: el nodo aconseja lo que su libro desaconseja o contradice. Prioridad absoluta.
  - INFERIDO-ANADIDO: "afirma algo concreto que el libro no respalda (una cifra, un plazo, una herramienta, un responsable, una norma, una frecuencia). SE CORRIGE en la tanda de correcciones."
  - INFERIDO-OPERATIVO: "concreta lo que el libro dice, en su misma direccion, sin datos nuevos. SE QUEDA."
  - FIEL: el libro dice lo que el paso aconseja.
  - Precedencia: CONTRARIO, luego INFERIDO-ANADIDO, luego INFERIDO-OPERATIVO. Un CONTRARIO que ademas inventa un dato lleva `tambien_anadido = true`.
  - La etiqueta de maquina es `INFERIDO-ANADIDO`, sin enie, por seguridad de codificacion.

## 5. Prueba de recall a ciegas: cada intento

Los sinteticos se generaron en llamadas aparte (`herramientas/sinteticos.py`) a partir de pasajes reales elegidos al azar. Se escribieron SOLO en `pruebas/SINTETICOS_REASON.jsonl`, marcados como sinteticos en cada registro. Son 16 CONTRARIOS (5 francos, 6 sutiles, 5 muy sutiles) y 12 ANADIDOS (2 cifras, 2 plazos, 2 herramientas, 2 normas, 2 roles y 2 libres). Cada uno va alojado en el nodo de Reason que mejor le cuadra, para que parezca un paso mas. Cada intento baraja reales y sinteticos bajo ids opacos nuevos (`mezclar.py`). La clave solo vive en `pruebas/CLAVE_CIEGA_iN.json`, que ningun prompt lee. El recall se mide despues, cruzando ids (`recall.py`).

| Intento | Metodo | Contrarios: pasada 1 / final | Conocido: pasada 1 / final | Anadidos: pasada 1 / final | Estado |
|---|---|---|---|---|---|
| 1 | Una marca (podria contradecir), 3 veredictos | 16/16 / sin pasada 2 | 1/1 / sin pasada 2 | no existian | SUPERADO por el anadido del fundador antes de la pasada 2. Tasa de marcado 33,5 %. |
| 2 | Dos marcas, 4 veredictos | 16/16 / **16/16** | 1/1 / **1/1** | 12/12 / **11/12** | SUPERADO: A08 salio CONTRARIO; el dato inventado (ISO 45001) estaba en la razon, pero no en `datos_sin_respaldo`, porque la instruccion lo pedia "solo si INFERIDO-ANADIDO". |
| 3 (final) | Ajuste: la pasada 2 lista SIEMPRE los datos sin respaldo y marca `tambien_anadido` en un CONTRARIO que ademas inventa. Mezcla a ciegas nueva, repetido entero. | 16/16 / **16/16** | 1/1 / **1/1** | 12/12 / **12/12 detectados; 10/12 etiqueta principal** | FINAL. A08 e A09: CONTRARIO con `tambien_anadido` (seccion 1, punto 1). |

Ajustes declarados, uno por intento: del 1 al 2, el anadido del fundador (dos marcas, cuatro veredictos, 12 anadidos sinteticos nuevos); del 2 al 3, los datos sin respaldo se listan siempre. La busqueda (D con k = 20), el troceado y los sinteticos no cambiaron. Las consultas traducidas se heredan por texto.

## 6. Contrarios encontrados en Reason

Los 17 de la union de las dos corridas a ciegas. "Ambos" = CONTRARIO en los intentos 2 y 3. La cita es la linea del txt del fundador. La cita y el paso fiel son los de la corrida que lo dio CONTRARIO (la 3 si lo dieron las dos).

| Nodo | Paso | Texto del paso | Intentos | Cita del libro | Lo que diria el paso fiel |
|---|---:|---|---|---|---|
| accidentes_individuales_vs_organizacionales | 1 | Clasificar los eventos de seguridad pasados de la organización según sean individuales u organizacionales antes de iniciar cualquier investigación. | ambos | L323, L244, L248, L194, L293: "Individual accidents can, and usually do, have organizational origins. [...] Although it is not always easy to draw a hard and fast line between individual and organizational accidents, this book argues that it is useful to treat them as distinct kinds of [...]" | Clasificar los eventos de seguridad pasados de la organización como individuales u organizacionales según lo que revele su investigación, remontando desde los actos inseguros hasta las condiciones del lugar de trabajo y los factores organizacionales, sin cerrar el análisis porque un evento parezca individual. |
| clasificacion_riesgos_por_dominio | 4 | Priorizar recursos de gestión de riesgo según el tipo de riesgo predominante en el dominio, no solo en lesiones personales | solo i3 (i2: INFERIDO-OPERATIVO) | L5639, L5781, L5905, L5907: "All domains must be assessed as at least ‘high’ in this regard. […] Effective risk management requires the application of different countermeasures targeted at different levels of the system at the same time--and all the time." | Repartir los recursos de gestión de riesgo entre los cuatro tipos de riesgo a la vez, ajustando el énfasis al balance propio del dominio, sin limitarse a las lesiones personales y sin relegar nunca las condiciones latentes, que son al menos altas en todos los dominios. |
| documentacion_mantenimiento_linea_base | 2 | Asegurar que toda tarea, sin importar su origen, incluya documentación completa y advertencias de seguridad. | ambos | L417, L419, L423, L451, L453: "The line and base environments thus require different kinds of planning and supportive work packs. In the case of line maintenance, the paperwork is generated just before the work is due to be done and is subject to change according to operational needs. The [...]" | Cuando una tarea de línea se traspase a personal de base, acompañarla de hojas de etapa escritas con el trabajo ya realizado y asegurar que quien la recibe disponga de las tarjetas de tarea, las advertencias del manual y un medio para firmar los trabajos de restitución. |
| efectos_recompensa_castigo | 2 | Evitar sanciones tardías desconectadas del momento del incidente | solo i3 (i2: INFERIDO-OPERATIVO) | L5067, L5077, L4765, L5063: "Delayed punishments have negative effects: they generally do not lead to improved behaviour and can induce resentment in both the punished and the could-be-punished. [...] But there are other factors that argue strongly in favour of punishing the few who [...]" | No recurrir al castigo diferido para corregir los actos inseguros ordinarios, pero sancionar, aunque sea tras la investigación, a los pocos autores de actos inseguros graves (imprudencia, negligencia, consumo de sustancias o reincidencia). |
| efectos_recompensa_castigo | 3 | Aplicar sanciones consistentes y visibles solo a casos de negligencia grave o reincidencia comprobada | ambos | L4765, L5063, L5061, L5077: "Both malevolent damage and the dangerous use of alcohol or drugs are wholly unacceptable and should receive very severe sanctions, possibly administered by the courts rather than the organization. Between ‘substance abuse with mitigation’ and ‘possible [...]" | Aplicar sanciones consistentes y visibles a los pocos actos inseguros graves (sabotaje, consumo de alcohol o drogas, incumplimiento temerario, imprudencia o negligencia reiteradas), juzgar con cuidado los casos de posible negligencia y tratar el resto como no culpable. |
| falla_sistemica_vs_error_individual | 4 | Documentar la cadena completa de decisiones organizacionales que condujeron al incidente | solo i2 (i3: INFERIDO-OPERATIVO) | L261, L263, L271, L273, L293: "Since time and causality are seamless, they have no natural breakpoints, only artificially imposed ones. … Both of these ends are best satisfied by limiting the scope of the analysis to those things over which the people involved--and most particularly the [...]" | Documentar las decisiones y los factores organizacionales que contribuyeron al incidente, remontándose desde las defensas fallidas y las condiciones locales, y limitando el alcance a aquello que los gestores del sistema pueden razonablemente controlar. |
| fijar_causa_ultimo_accidente_riesgo_siguiente | 3 | Establecer revisiones periódicas de reglas post-accidente para verificar su aplicabilidad universal | ambos | L1031, L1035, L1145: "regulators--just as much as system designers--cannot foresee all the possible scenarios of failure in complex, tightly-coupled and highly interactive systems such as nuclear power plants, and so cannot universally proscribe particular types of human response." | Revisar las reglas post-accidente para detectar los contextos operativos en que podrían resultar contraproducentes, asumiendo que no pueden anticipar todos los escenarios ni aplicarse universalmente. |
| gestion_falsas_alarmas | 3 | Establecer protocolos que impidan la desactivación unilateral de alarmas críticas sin verificación cruzada | solo i3 (i2: INFERIDO-ANADIDO) | L1085, L1095, L1141, L1145, L1035: "Measures designed to eliminate a conspicuous cause of some previous accident can contribute to the next one. […] cannot universally proscribe particular types of human response. What proved to be an error in the TMI event turned out to be a vital step at [...]" | Atacar la causa de la desconfianza eliminando las activaciones falsas de las alarmas críticas para que recuperen su credibilidad, en lugar de añadir procedimientos que prohíban de forma general una respuesta humana que en escenarios imprevistos podría ser la acertada. |
| ida_diagrama_influencia | 3 | Asignar razones de influencia (buena/mala) a cada factor mediante escalas graduadas de evidencia | solo i3 (i2: INFERIDO-OPERATIVO) | L3692, L3704, L3706, L3714, L3718: "The process begins with one of the ‘bottom influences’ (leaf nodes)--that is, a factor that has no external influences shown as impinging upon it. ... they are given a graded indicator scale that specifies the nature of the evidence to be taken into account." | Con la guía de un facilitador experto, asignar a cada factor hoja (sin influencias previas) una razón de influencia (buena/mala) mediante una escala graduada de evidencia; los factores con varias influencias se derivan después combinando evaluaciones condicionales. |
| ironias_de_la_automatizacion | 3 | Diseñar sistemas de monitoreo que compensen la baja capacidad humana de mantener vigilancia sostenida ante eventos raros. | ambos | L848, L856, L942, L1033, L1141: "In their efforts to compensate for the unreliability of human performance, the designers of automated control systems have unwittingly created opportunities for new error types that can be even more serious than those they were seeking to avoid." | Asumir que los operadores rinden mal vigilando durante largos periodos condiciones anómalas muy raras. En lugar de confiar en sistemas añadidos que compensen esa limitación, que pueden crear errores nuevos, más complejidad y falsas alarmas, invertir en el entrenamiento del operador. |
| limite_busqueda_causas_pendulo | 5 | Priorizar la calidad y disponibilidad de evidencia confiable al fijar los límites del análisis | ambos | L263, L271, L273, L5726: "Accident analysts, just like historians, are limited by their resources and by the availability of reliable evidence. [...] Both of these ends are best satisfied by limiting the scope of the analysis to those things over which [...] the system managers--might [...]" | Fijar los límites del análisis priorizando los factores que los gestores del sistema pueden razonablemente controlar, teniendo en cuenta que la cantidad y fiabilidad de la evidencia disminuyen con la distancia al suceso. |
| prevalencia_omisiones | 2 | Identificar en qué nivel cognitivo (planificación, almacenamiento, ejecución, monitoreo) ocurren las omisiones más frecuentes | ambos | L2170, L2250, L2259: "Even when the omission is one's own, the underlying mechanisms are not easy to establish, but when the omission is made by another person at some time in the past, the underlying reasons may be impossible to discover. The task analysis route, on the other [...]" | Analizar los pasos de cada procedimiento de mantenimiento para contar cuántos rasgos que provocan omisiones reúne cada uno (aislado funcionalmente, cerca del final, oculto a la vista, con múltiples elementos, con cambios recientes...), en lugar de intentar averiguar el mecanismo cognitivo de cada omisión pasada. |
| racional_mantenimiento_preventivo_correctivo | 2 | Calcular curvas de costo de mantenimiento preventivo vs correctivo para determinar el nivel óptimo | ambos | L2322, L2340, L2354, L2369: "Unfortunately, this orthodoxy presumes that all--or at least most--maintenance activities are essentially benign. But suppose preventive maintenance did not always prevent failure and that corrective maintenance did not always correct it." | Calcular las curvas de costo de mantenimiento preventivo y correctivo solo como punto de partida, y fijar el nivel de mantenimiento teniendo en cuenta además el riesgo de error humano que introduce cada intervención, sin tomar el mínimo de costo como nivel óptimo. |
| redes_de_seguridad_regulatoria | 4 | Diseñar redundancia real entre capas de control para evitar fallas simultáneas | solo i3 (i2: INFERIDO-OPERATIVO) | L1068, L1072, L1137, L4092, L4502: "Redundant defensive back-ups increase the interactive complexity of high-technology organizations and thus increase the likelihood of unforeseeable common-mode failures. ... human errors at the ‘sharp end’, in the maintenance sector and in the managerial [...]" | Identificar y corregir las causas sistémicas comunes (falta de recursos, presiones comerciales, inacción de la dirección) que pueden hacer fallar varias capas a la vez, sin confiar en que añadir redundancia lo evite, porque aumenta la complejidad y la opacidad del sistema. |
| reporte_casi_accidentes | 2 | Desarrollar una cultura de reporte sin represalias que incentive la notificación honesta | solo i2 (i3: FIEL) | L4765, L4798, L4824, L4987: "A ‘no-blame’ culture is neither feasible nor desirable. A small proportion of human unsafe acts are egregious (for example, substance abuse, reckless non-compliance, sabotage and so on) and warrant sanctions, severe ones in some cases." | Desarrollar una cultura justa de reporte que proteja a quienes informan de sanciones por lo que reportan, en la medida de lo practicable, y que deje claro dónde está la línea entre conductas aceptables e inaceptables (abuso de sustancias, incumplimiento temerario, sabotaje), que sí se sancionan. |
| self_regulation_deregulation_tradeoffs | 1 | Evaluar si la organización tiene la madurez para autorregularse | solo i2 (i3: INFERIDO-OPERATIVO) | L4429, L4308, L4431, L4435: "The long-term safety benefits of being forced to grapple with these enormously difficult--and still unresolved--sociotechnical issues are undoubtedly greater than any number of purely technical ‘fixes’. The process is more valuable than the product." | Asumir la elaboración y actualización del Safety Case como el ejercicio que obliga a la organización a comprender a fondo sus riesgos sociotécnicos, sin esperar a tener una madurez previa, porque el proceso vale más que el producto. |
| self_regulation_deregulation_tradeoffs | 4 | Balancear la reducción de carga regulatoria con el mantenimiento de la vigilancia efectiva | solo i3 (i2: INFERIDO-OPERATIVO) | L4060, L4182, L4418, L4523: "As elsewhere, the deregulation of the airline industry in 1978 has not made the regulators’ work any easier. ... Running in parallel with these moves towards deregulation, there has been--predictably--a steady erosion of the HSC/HSE’s budget." | Asegurar que el paso hacia la autorregulación se acompañe de legislación, recursos, formación y herramientas suficientes para que el regulador mantenga una vigilancia efectiva, sin tratar la reducción de la carga regulatoria como un objetivo en sí misma. |

## 7. Anadidos encontrados en Reason (INFERIDO-ANADIDO)

Los 25 de la union (24 en el intento final, 13 en ambos). Se corrigen en la tanda de correcciones. El detalle completo, con cita, razon y paso fiel, esta en `VEREDICTOS_PASOS.jsonl` y en `piloto_reason/pasada2_i3.json`.

| Nodo | Paso | Texto del paso | Intentos | Dato sin respaldo | Lineas |
|---|---:|---|---|---|---|
| accidentes_organizacionales_por_mantenimiento | 4 | Usar los casos como material de capacitación y sensibilización para personal técnico y gerencial | ambos | personal técnico y gerencial como destinatarios; uso de los casos como material de capacitación | L2369, L1840, L1934 |
| arbol_decision_culpabilidad | 6 | Clasificar el acto en: criminal, negligente, violación con o sin mitigación, o error inducido por el sistema | solo i3 (i2: INFERIDO-OPERATIVO) | categoría 'violación con o sin mitigación' (en el libro la mitigación califica el abuso de sustancias; las violaciones se dividen en posible violación [...] | L5043, L5053, L5055, L5057, L5063 |
| clasificacion_riesgos_por_dominio | 2 | Comparar el perfil de riesgo actual contra dominios similares usando referencias históricas | solo i3 (i2: INFERIDO-OPERATIVO) | referencias históricas como herramienta de comparación | L5603, L5605, L5611, L5639 |
| conflicto_de_objetivos_en_organismos_reguladores | 3 | Establecer canales de reporte independientes para el personal de seguridad | ambos | personal de seguridad (como destinatario específico de los canales independientes) | L4761, L4806, L4908 |
| costos_ocultos_accidentes_iceberg | 2 | Tener claro un análisis costo-beneficio de la inversión en prevención frente al costo potencial de un accidente mayor, antes de decidir | solo i3 (i2: INFERIDO-OPERATIVO) | análisis costo-beneficio (como herramienta formal); antes de decidir (como condición previa a la decisión) | L5894, L5834, L5892, L5907 |
| cultura_como_mecanismo_descentralizacion | 4 | Diseñar mecanismos de transmisión cultural (formación, mentoría) en lugar de solo reglas escritas | solo i3 (i2: INFERIDO-OPERATIVO) | mentoría | L5178, L5132, L5182, L5184, L5206 |
| cultura_de_seguridad_componentes | 4 | Tener claro y por escrito por que vale la pena invertir en estos cuatro pilares antes de decidir | ambos | justificacion 'por escrito' (documento previo de justificacion de la inversion); 'antes de decidir' como requisito previo a la decision de invertir | L4749, L4689, L2579, L4777, L4695 |
| cultura_flexible | 2 | Diseñar protocolos que permitan transferir autoridad a expertos técnicos durante emergencias | ambos | protocolos (formales) de transferencia de autoridad | L4769, L5164, L5174, L5178, L5208 |
| cultura_justa | 2 | Establecer una línea explícita entre errores humanos normales y actos verdaderamente negligentes o maliciosos, y dejarla por escrito | solo i3 (i2: INFERIDO-OPERATIVO) | dejarla por escrito | L4987, L4989, L5063 |
| cultura_justa | 3 | Capacitar a supervisores y gestores en la aplicación consistente de estos criterios | ambos | capacitación/formación como medio para lograr la aplicación consistente; supervisores y gestores como responsables de aplicar los criterios | L5085, L5057, L5266, L4989 |
| diseno_recordatorios_efectivos_2 | 1 | Identifica los pasos de tarea propensos a omisión revisando errores históricos | ambos | revision de errores historicos como metodo para identificar los pasos propensos a omision | L2170, L2250, L2127, L2259 |
| espacio_de_seguridad | 4 | Implementar navegación activa: monitoreo continuo en vez de reacción pasiva a accidentes | solo i3 (i2: INFERIDO-OPERATIVO) | monitoreo continuo | L2520, L2568, L2596, L2638, L2658 |
| fallas_activas_condiciones_latentes | 6 | Mantener un registro de condiciones latentes conocidas para monitorearlas de forma continua, no solo tras un accidente | solo i3 (i2: INFERIDO-OPERATIVO) | registro de condiciones latentes conocidas | L5775, L5781, L2598, L2658, L2767 |
| fallo_regulatorio_por_recursos_insuficientes | 2 | Comparar el ratio de personal de seguridad respecto al total de la organización con estándares del sector | ambos | comparación con estándares del sector como referencia | L3993, L4180, L4121 |
| fijar_causa_ultimo_accidente_riesgo_siguiente | 2 | Realizar análisis de sensibilidad sobre nuevas regulaciones en diferentes contextos operativos | ambos | análisis de sensibilidad | L1035, L1031 |
| gestion_falsas_alarmas | 3 | Establecer protocolos que impidan la desactivación unilateral de alarmas críticas sin verificación cruzada | solo i2 (i3: CONTRARIO) | protocolos que impidan la desactivación unilateral de alarmas; verificación cruzada obligatoria antes de desactivar | L1085, L1089, L1095, L1141, L1035 |
| modelo_queso_suizo | 3 | Diseñar mecanismos de monitoreo continuo de huecos en cada capa defensiva. | solo i3 (i2: INFERIDO-OPERATIVO) | monitoreo continuo; en cada capa defensiva | L2650, L2654, L2658 |
| normalizacion_de_la_desviacion | 4 | Establece puntos de control periódicos en tu calendario para cuestionar la aceptación acumulada de desviaciones | solo i3 (i2: INFERIDO-OPERATIVO) | en tu calendario | L3965, L3971, L4429, L4478 |
| normalizacion_de_la_desviacion | 6 | Busca una revisión externa, como un mentor o asesor, que contrarreste tu normalización interna | ambos | mentor | L4446, L3971, L4190, L4257, L4261 |
| planificacion_recuperacion_post_accidente | 4 | Probar (testear) el plan de recuperación mediante simulacros antes de que ocurra un evento real | solo i3 (i2: INFERIDO-OPERATIVO) | simulacros | L5894, L5896 |
| prevalencia_omisiones | 3 | Enfocar las intervenciones de mejora en los pasos con mayor tasa de omisión histórica | ambos | la tasa de omision historica por paso como criterio para elegir donde intervenir | L2250, L2170, L2866 |
| quality_control_vs_quality_assurance | 4 | Implementar auditorías aleatorias sobre el trabajo firmado como conforme | ambos | auditorías aleatorias (muestreo al azar como mecanismo de verificación) | L967, L971, L975, L3465 |
| riesgo_error_humano_en_mantenimiento | 3 | Priorizar el diseño de componentes que solo puedan instalarse correctamente (poka-yoke) | solo i3 (i2: INFERIDO-OPERATIVO) | poka-yoke | L2311, L1842, L2369 |
| riesgo_error_humano_en_mantenimiento | 4 | Explorar la eliminación de la necesidad de contacto humano directo mediante sistemas de autodiagnóstico | ambos | sistemas de autodiagnóstico | L2311, L2356, L2367 |
| safety_culture_engineering | 4 | Medir el compromiso mediante comunicación basada en confianza mutua y percepción compartida de importancia de la seguridad | ambos | usar la comunicacion basada en confianza mutua y la percepcion compartida como metodo o instrumento para medir el compromiso | L4730, L4734 |

## 8. Tasa de marcado y costes

- **Tasa de marcado de la pasada 1** sobre los 403 pasos reales: 56,8 % con las dos marcas (229 pasos). De ellos, 170 marcan "podria contradecir" (42,2 %), 109 marcan "dato concreto" y 59 van solo por el dato. Con la marca unica del intento 1 (solo contrarios), la tasa fue 33,5 %. La pasada 2 es el 69 % del coste por paso. Esta tasa es lo que decide el precio.
- **Veredicto final de los 403 pasos** (intento 3): FIEL 161, INFERIDO-OPERATIVO 204, INFERIDO-ANADIDO 24, CONTRARIO 14. Coinciden con el intento 2 en 348 de 403.
- **Turnos**: cada llamada es 1 turno (`--max-turns 1`). La pasada 1 hace 1 llamada por cada 4 pasos; la pasada 2, 1 llamada por paso marcado.

### Costes medidos del piloto (Opus 5.5 en todo)

| Etapa | Llamadas | USD | Turnos | Tiempo de API (min) | Pared con 4 a la vez (min) | Tokens entrada | Tokens salida |
|---|---:|---:|---:|---:|---:|---:|---:|
| Sinteticos (contrarios y anadidos) | 2 | 0.62 | 2 | 2.3 | 0.6 | 43,618 | 16,442 |
| Traduccion de consultas | 36 | 2.07 | 36 | 8.3 | 2.4 | 133,718 | 44,972 |
| Oro de busqueda (libro entero) | 1 | 1.62 | 1 | 0.5 | 0.1 | 178,909 | 3,225 |
| Pasada 1, intento 1 (una marca; superado) | 105 | 16.39 | 105 | 24.4 | 6.7 | 3,472,175 | 125,055 |
| Pasada 1, intento 2 (dos marcas; superado) | 108 | 18.06 | 108 | 32.2 | 8.6 | 3,599,952 | 182,935 |
| Pasada 2, intento 2 (superado) | 256 | 46.14 | 256 | 49.1 | 13.4 | 10,328,585 | 241,495 |
| Pasada 1, intento 3 (dos marcas; final) | 108 | 18.09 | 108 | 32.6 | 8.6 | 3,599,924 | 184,281 |
| Pasada 2, intento 3 (final) | 257 | 46.43 | 257 | 52.6 | 14.5 | 10,346,425 | 252,038 |
| **Total del piloto** | 873 | **149.41** | 873 | 202.0 | 54.9 | 31,703,306 | 1,050,443 |

### Coste por paso y por libro (Reason)

| Modo | Tasa de marcado (reales) | USD por paso | Turnos por paso | Segundos de pared por paso (4 a la vez) | USD Reason (403 pasos + prueba fija) | Horas de pared Reason |
|---|---:|---:|---:|---:|---:|---:|
| Solo contrarios | 33.5% | 0.104 | 0.67 | 2.4 | 49.07 | 0.32 |
| Contrarios mas anadidos | 56.8% | 0.149 | 0.90 | 3.4 | 67.18 | 0.43 |

Prueba de recall fija por libro (generar sinteticos y pasar 28 por las dos pasadas): 6.98 USD, 39 turnos.

La pared real observada en el piloto, con 4 procesos a la vez, fue de 8,5 min para la pasada 1 y de 14,4 min para la pasada 2, sobre los 431 pasos de la mezcla. Coincide con la estimacion (suma de duraciones entre 4).

## 9. Proyeccion de la campania completa, en orden de riesgo

Modelo, todo con cifras medidas en Reason:

- Por libro: `pasos x (traduccion + pasada 1 + tasa de marcado x pasada 2)`, mas una prueba de recall fija por libro (generar sinteticos y pasar 28 por las dos pasadas: 6,98 USD).
- "Solo contrarios" usa la pasada 1 y la tasa del intento 1; "contrarios mas anadidos", las del intento 3. La pasada 2 cuesta lo del intento 3 en los dos modos.
- Supuesto declarado: el coste por paso de Reason vale para los demas libros. La pasada 2 lleva capitulos enteros, y un libro con capitulos mas largos (Juran) costara mas por paso.
- No incluye la doble pasada 2 de la seccion 1, punto 2 (unos 0,076 USD mas por paso), ni la revision humana.

### Proyeccion: SOLO CONTRARIOS

| Orden | Tramo | Libro | Pasos | USD | Turnos | Horas de pared (4 a la vez) | USD acumulado |
|---:|---|---|---:|---:|---:|---:|---:|
| 1 | 1 | The Field Guide to Understandin - Dekker, Sidney | 424 | 51.26 | 323 | 0.33 | 51.26 |
| 2 | 1 | Managing the Risks of Organizat - Reason, J. T_ | 403 | 49.07 | 309 | 0.32 | 100.33 |
| 3 | 1 | SMALL_BUSINESS | 238 | 31.84 | 199 | 0.21 | 132.16 |
| 4 | 1 | OSHA3885 | 84 | 15.75 | 96 | 0.10 | 147.92 |
| 5 | 1 | Guia de empaque para envios (FedEx) | 44 | 11.58 | 69 | 0.08 | 159.50 |
| 6 | 1 | OSHA3886 | 37 | 10.85 | 64 | 0.07 | 170.34 |
| 7 | 2 | Franchise Your Business - Mark Siebert | 828 | 93.45 | 593 | 0.60 | 263.79 |
| 8 | 2 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) | 665 | 76.43 | 484 | 0.49 | 340.22 |
| 9 | 2 | Venture Deals - Brad Feld | 585 | 68.07 | 431 | 0.44 | 408.29 |
| 10 | 2 | The Founder's Dilemmas - Wasserman, Noam | 486 | 57.73 | 365 | 0.37 | 466.03 |
| 11 | 2 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe | 348 | 43.32 | 272 | 0.28 | 509.35 |
| 12 | 2 | Edwards et al., Managing Project Risks | 123 | 19.83 | 122 | 0.13 | 529.18 |
| 13 | 2 | NIST SP 1318: Protecting CUI (SP 800-171 r3) - Small Business Primer | 115 | 18.99 | 116 | 0.13 | 548.17 |
| 14 | 2 | Diana L. Lindstrom, Procurement Project Management Success (J. Ross, 2014) | 114 | 18.89 | 116 | 0.12 | 567.06 |
| 15 | 2 | Chris Voss, Rompe la barrera del no | 86 | 15.96 | 97 | 0.11 | 583.02 |
| 16 | 2 | DeMarco y Lister, Waltzing with Bears | 63 | 13.56 | 82 | 0.09 | 596.58 |
| 17 | 2 | NIST SP 1314: Risk Management Framework - Small Enterprise Quick Start Guide | 45 | 11.68 | 69 | 0.08 | 608.26 |
| 18 | 2 | Hubbard, The Failure of Risk Management | 40 | 11.16 | 66 | 0.07 | 619.42 |
| 19 | 2 | Businessperson's Guide to Federal Warranty Law | 40 | 11.16 | 66 | 0.07 | 630.58 |
| 20 | 2 | NIST SP 1300: Cybersecurity Framework 2.0 - Small Business Quick-Start Guide | 35 | 10.64 | 63 | 0.07 | 641.22 |
| 21 | 2 | Getting Started with the NIST Privacy Framework: A Guide for Small and Medium Bu | 28 | 9.91 | 58 | 0.07 | 651.13 |
| 22 | 2 | Cybersecurity for Small Business: Understanding the NIST Cybersecurity Framework | 28 | 9.91 | 58 | 0.07 | 661.03 |
| 23 | 2 | The Founder's Dilemmas - Wasserman, Noam | The Hard Thing About Hard Things - Be | 15 | 8.55 | 49 | 0.06 | 669.58 |
| 24 | 2 | Venture Deals - Brad Feld | The Founder's Dilemmas - Wasserman, Noam | 14 | 8.44 | 49 | 0.06 | 678.03 |
| 25 | 3 | Juran's Quality Handbook_ The C - Joseph A. Defeo | 2297 | 246.85 | 1576 | 1.59 | 924.88 |
| 26 | 3 | The Green to Gold Business Play - Daniel C. Esty | 933 | 104.41 | 664 | 0.68 | 1029.30 |
| 27 | 3 | The Startup Owner's Manual - Blank, Steve | 864 | 97.21 | 617 | 0.63 | 1126.50 |
| 28 | 3 | Winning at New Products - Robert G. Cooper | 759 | 86.24 | 547 | 0.56 | 1212.75 |
| 29 | 3 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev | 702 | 80.29 | 509 | 0.52 | 1293.04 |
| 30 | 3 | Essentials of Supply Chain Management - Michael H. Hugos | 535 | 62.85 | 397 | 0.41 | 1355.89 |
| 31 | 3 | The Hard Thing About Hard Things - Ben Horowitz | 452 | 54.18 | 342 | 0.35 | 1410.07 |
| 32 | 3 | Quality is free _ the art of making quality certain -- Philip B_ Crosby | 406 | 49.38 | 311 | 0.32 | 1459.45 |
| 33 | 3 | The Lean Startup - Eric Ries | 352 | 43.74 | 275 | 0.28 | 1503.20 |
| 34 | 3 | Traction - Gabriel Weinberg | 343 | 42.80 | 269 | 0.28 | 1546.00 |
| 35 | 3 | Never Lose a Customer Again - Joey Coleman | 341 | 42.59 | 268 | 0.28 | 1588.59 |
| 36 | 3 | Change by Design, Revised and U - Tim Brown | 335 | 41.97 | 264 | 0.27 | 1630.56 |
| 37 | 3 | Assembling Tomorrow: A Guide to Designing a Thriving Future | 295 | 37.79 | 237 | 0.25 | 1668.35 |
| 38 | 3 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder | 283 | 36.54 | 229 | 0.24 | 1704.88 |
| 39 | 3 | Business Model Generation - Osterwalder, Alexander | 243 | 32.36 | 202 | 0.21 | 1737.24 |
| 40 | 3 | Cradle to Cradle - Michael Braungart | 229 | 30.90 | 193 | 0.20 | 1768.14 |
| 41 | 3 | Value Proposition Design | 200 | 27.87 | 173 | 0.18 | 1796.00 |
| 42 | 3 | SPIN Selling - Neil Rackham | 175 | 25.26 | 156 | 0.17 | 1821.26 |
| 43 | 3 | Co-Intelligence_ Living and Wor - Ethan Mollick | 173 | 25.05 | 155 | 0.16 | 1846.31 |
| 44 | 3 | The Art of Thought - Wallas, Graham | 160 | 23.69 | 146 | 0.16 | 1870.00 |
| 45 | 3 | The field guide to human-centered design | 90 | 16.38 | 100 | 0.11 | 1886.38 |
| 46 | 3 | Rushton, Croucher y Baker, The Handbook of Logistics and Distribution Management | 63 | 13.56 | 82 | 0.09 | 1899.94 |
| 47 | 3 | Sharon Cullinane, E-Logistics, Cap. 8 (B2C e-commerce y fulfilment) | 38 | 10.95 | 65 | 0.07 | 1910.89 |
| 48 | 3 | Max Muller, Essentials of Inventory Management | 25 | 9.59 | 56 | 0.06 | 1920.49 |
| 49 | 3 | ISTA 3P, Protocolo de ensayo de empaque para paqueteria | 24 | 9.49 | 55 | 0.06 | 1929.98 |
| 50 | 3 | The Startup Owner's Manual - Blank, Steve | Never Lose a Customer Again - Joey C | 23 | 9.38 | 55 | 0.06 | 1939.36 |
| 51 | 3 | Guia visual de empaque | 20 | 9.07 | 53 | 0.06 | 1948.43 |
| 52 | 3 | DHL Express, Guia de empaque | 15 | 8.55 | 49 | 0.06 | 1956.98 |
| 53 | 3 | Requisitos de empaque de los couriers | 14 | 8.44 | 49 | 0.06 | 1965.43 |
| 54 | 3 | The Startup Owner's Manual - Blank, Steve | The Lean Startup - Eric Ries | 8 | 7.82 | 45 | 0.05 | 1973.24 |
| 55 | 3 | The Startup Owner's Manual - Blank, Steve | Traction - Gabriel Weinberg | 8 | 7.82 | 45 | 0.05 | 1981.06 |
| 56 | 3 | The Lean Startup - Eric Ries | The Hard Thing About Hard Things - Ben Horowitz | 7 | 7.71 | 44 | 0.05 | 1988.78 |
| 57 | 3 | The Startup Owner's Manual - Blank, Steve | Never Lose a Customer Again - Joey C | 6 | 7.61 | 43 | 0.05 | 1996.38 |
| 58 | 3 | Guia de empaque para transporte | 5 | 7.50 | 43 | 0.05 | 2003.89 |
| | | **Total** | **15311** | **2003.89** | **12528** | **13.1** | |

| Tramo | Pasos | USD | Horas de pared |
|---|---:|---:|---:|
| 1 seguridad y salud | 1230 | 170.34 | 1.1 |
| 2 legal y dinero | 3658 | 507.68 | 3.3 |
| 3 el resto | 10423 | 1325.86 | 8.6 |

### Proyeccion: CONTRARIOS MAS ANADIDOS

| Orden | Tramo | Libro | Pasos | USD | Turnos | Horas de pared (4 a la vez) | USD acumulado |
|---:|---|---|---:|---:|---:|---:|---:|
| 1 | 1 | The Field Guide to Understandin - Dekker, Sidney | 424 | 70.31 | 422 | 0.45 | 70.31 |
| 2 | 1 | Managing the Risks of Organizat - Reason, J. T_ | 403 | 67.18 | 403 | 0.43 | 137.49 |
| 3 | 1 | SMALL_BUSINESS | 238 | 42.53 | 254 | 0.28 | 180.02 |
| 4 | 1 | OSHA3885 | 84 | 19.53 | 115 | 0.13 | 199.55 |
| 5 | 1 | Guia de empaque para envios (FedEx) | 44 | 13.55 | 79 | 0.09 | 213.10 |
| 6 | 1 | OSHA3886 | 37 | 12.51 | 73 | 0.08 | 225.61 |
| 7 | 2 | Franchise Your Business - Mark Siebert | 828 | 130.66 | 786 | 0.84 | 356.27 |
| 8 | 2 | A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) | 665 | 106.31 | 639 | 0.69 | 462.58 |
| 9 | 2 | Venture Deals - Brad Feld | 585 | 94.36 | 567 | 0.61 | 556.94 |
| 10 | 2 | The Founder's Dilemmas - Wasserman, Noam | 486 | 79.57 | 478 | 0.51 | 636.51 |
| 11 | 2 | Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe | 348 | 58.96 | 353 | 0.38 | 695.47 |
| 12 | 2 | Edwards et al., Managing Project Risks | 123 | 25.35 | 150 | 0.17 | 720.83 |
| 13 | 2 | NIST SP 1318: Protecting CUI (SP 800-171 r3) - Small Business Primer | 115 | 24.16 | 143 | 0.16 | 744.99 |
| 14 | 2 | Diana L. Lindstrom, Procurement Project Management Success (J. Ross, 2014) | 114 | 24.01 | 142 | 0.16 | 769.00 |
| 15 | 2 | Chris Voss, Rompe la barrera del no | 86 | 19.83 | 117 | 0.13 | 788.83 |
| 16 | 2 | DeMarco y Lister, Waltzing with Bears | 63 | 16.39 | 96 | 0.11 | 805.22 |
| 17 | 2 | NIST SP 1314: Risk Management Framework - Small Enterprise Quick Start Guide | 45 | 13.70 | 80 | 0.09 | 818.92 |
| 18 | 2 | Hubbard, The Failure of Risk Management | 40 | 12.96 | 75 | 0.09 | 831.88 |
| 19 | 2 | Businessperson's Guide to Federal Warranty Law | 40 | 12.96 | 75 | 0.09 | 844.84 |
| 20 | 2 | NIST SP 1300: Cybersecurity Framework 2.0 - Small Business Quick-Start Guide | 35 | 12.21 | 71 | 0.08 | 857.05 |
| 21 | 2 | Getting Started with the NIST Privacy Framework: A Guide for Small and Medium Bu | 28 | 11.16 | 65 | 0.07 | 868.21 |
| 22 | 2 | Cybersecurity for Small Business: Understanding the NIST Cybersecurity Framework | 28 | 11.16 | 65 | 0.07 | 879.38 |
| 23 | 2 | The Founder's Dilemmas - Wasserman, Noam | The Hard Thing About Hard Things - Be | 15 | 9.22 | 53 | 0.06 | 888.60 |
| 24 | 2 | Venture Deals - Brad Feld | The Founder's Dilemmas - Wasserman, Noam | 14 | 9.07 | 52 | 0.06 | 897.67 |
| 25 | 3 | Juran's Quality Handbook_ The C - Joseph A. Defeo | 2297 | 350.07 | 2111 | 2.25 | 1247.74 |
| 26 | 3 | The Green to Gold Business Play - Daniel C. Esty | 933 | 146.34 | 881 | 0.94 | 1394.08 |
| 27 | 3 | The Startup Owner's Manual - Blank, Steve | 864 | 136.03 | 819 | 0.88 | 1530.12 |
| 28 | 3 | Winning at New Products - Robert G. Cooper | 759 | 120.35 | 724 | 0.78 | 1650.47 |
| 29 | 3 | Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev | 702 | 111.84 | 673 | 0.72 | 1762.30 |
| 30 | 3 | Essentials of Supply Chain Management - Michael H. Hugos | 535 | 86.89 | 522 | 0.56 | 1849.19 |
| 31 | 3 | The Hard Thing About Hard Things - Ben Horowitz | 452 | 74.50 | 447 | 0.48 | 1923.69 |
| 32 | 3 | Quality is free _ the art of making quality certain -- Philip B_ Crosby | 406 | 67.62 | 406 | 0.44 | 1991.31 |
| 33 | 3 | The Lean Startup - Eric Ries | 352 | 59.56 | 357 | 0.39 | 2050.87 |
| 34 | 3 | Traction - Gabriel Weinberg | 343 | 58.21 | 349 | 0.38 | 2109.09 |
| 35 | 3 | Never Lose a Customer Again - Joey Coleman | 341 | 57.92 | 347 | 0.37 | 2167.00 |
| 36 | 3 | Change by Design, Revised and U - Tim Brown | 335 | 57.02 | 342 | 0.37 | 2224.02 |
| 37 | 3 | Assembling Tomorrow: A Guide to Designing a Thriving Future | 295 | 51.04 | 305 | 0.33 | 2275.07 |
| 38 | 3 | A Project Manager's Book of Forms - Cynthia Stackpole Snyder | 283 | 49.25 | 295 | 0.32 | 2324.32 |
| 39 | 3 | Business Model Generation - Osterwalder, Alexander | 243 | 43.28 | 259 | 0.28 | 2367.60 |
| 40 | 3 | Cradle to Cradle - Michael Braungart | 229 | 41.19 | 246 | 0.27 | 2408.78 |
| 41 | 3 | Value Proposition Design | 200 | 36.86 | 220 | 0.24 | 2445.64 |
| 42 | 3 | SPIN Selling - Neil Rackham | 175 | 33.12 | 197 | 0.22 | 2478.76 |
| 43 | 3 | Co-Intelligence_ Living and Wor - Ethan Mollick | 173 | 32.82 | 195 | 0.21 | 2511.58 |
| 44 | 3 | The Art of Thought - Wallas, Graham | 160 | 30.88 | 184 | 0.20 | 2542.46 |
| 45 | 3 | The field guide to human-centered design | 90 | 20.43 | 121 | 0.13 | 2562.89 |
| 46 | 3 | Rushton, Croucher y Baker, The Handbook of Logistics and Distribution Management | 63 | 16.39 | 96 | 0.11 | 2579.28 |
| 47 | 3 | Sharon Cullinane, E-Logistics, Cap. 8 (B2C e-commerce y fulfilment) | 38 | 12.66 | 74 | 0.08 | 2591.94 |
| 48 | 3 | Max Muller, Essentials of Inventory Management | 25 | 10.72 | 62 | 0.07 | 2602.66 |
| 49 | 3 | ISTA 3P, Protocolo de ensayo de empaque para paqueteria | 24 | 10.57 | 61 | 0.07 | 2613.22 |
| 50 | 3 | The Startup Owner's Manual - Blank, Steve | Never Lose a Customer Again - Joey C | 23 | 10.42 | 60 | 0.07 | 2623.64 |
| 51 | 3 | Guia visual de empaque | 20 | 9.97 | 57 | 0.07 | 2633.61 |
| 52 | 3 | DHL Express, Guia de empaque | 15 | 9.22 | 53 | 0.06 | 2642.84 |
| 53 | 3 | Requisitos de empaque de los couriers | 14 | 9.07 | 52 | 0.06 | 2651.91 |
| 54 | 3 | The Startup Owner's Manual - Blank, Steve | The Lean Startup - Eric Ries | 8 | 8.18 | 47 | 0.06 | 2660.09 |
| 55 | 3 | The Startup Owner's Manual - Blank, Steve | Traction - Gabriel Weinberg | 8 | 8.18 | 47 | 0.06 | 2668.26 |
| 56 | 3 | The Lean Startup - Eric Ries | The Hard Thing About Hard Things - Ben Horowitz | 7 | 8.03 | 46 | 0.05 | 2676.29 |
| 57 | 3 | The Startup Owner's Manual - Blank, Steve | Never Lose a Customer Again - Joey C | 6 | 7.88 | 45 | 0.05 | 2684.17 |
| 58 | 3 | Guia de empaque para transporte | 5 | 7.73 | 44 | 0.05 | 2691.90 |
| | | **Total** | **15311** | **2691.90** | **16095** | **17.5** | |

| Tramo | Pasos | USD | Horas de pared |
|---|---:|---:|---:|
| 1 seguridad y salud | 1230 | 225.61 | 1.5 |
| 2 legal y dinero | 3658 | 672.06 | 4.4 |
| 3 el resto | 10423 | 1794.23 | 11.6 |

## 10. Atribucion en la app (punto 3 del anadido; solo lectura de `web/`)

Busque en `web/` todo sitio donde la fuente o el autor de un nodo o de un paso llegue al usuario:

- `web/lib/engine/graph.ts:24`: `fuente?: string;` esta declarado en el tipo `NodoGrafo`, y ningun codigo de `web/` lo lee (sin usos de `.fuente` de un nodo).
- `web/lib/engine/planRedactor.ts:79-88` (`aMaterial`): el material que recibe el redactor del plan es `id`, `concepto` (`titulo_concepto`), `pasos`, `entregable` y `es_viabilidad_economica`. La fuente no viaja.
- `web/lib/assets/prompts.json:7` (`SYSTEM_PLAN`, sincronizado desde `engine/prototipo_motor.py:1008`): la frase exacta es "Espanol comun, sin jerga sin explicar, sin autores, sin relleno motivacional. Todo debe salir del material recibido; no inventes tecnicas, cifras ni fuentes nuevas". El plan tiene prohibido nombrar autores.
- `web/app/ui/PlanDocumento.tsx:267` ("Construido con tu recorrido") y `web/app/idea/[id]/IdeaView.tsx:950` (`nodosFuente`): lo que se lista son las etiquetas de los nodos del recorrido (`etiqueta_arbol`), no libros ni autores.
- `web/lib/assets/packs_catalog.json` (nombre y promesa de cada mundo): no nombra libros ni autores.

Conclusion: la app no atribuye nada a un autor, ni en forma directa ("segun", "dice") ni indirecta. **No hay cambio que proponer hoy.** Si el fundador decide mostrar la fuente algun dia, la forma propuesta es "Basado en (titulo del libro)", nunca "segun (autor)" ni "(autor) dice". Asi no se le atribuye al autor un paso que es una concrecion de la casa (la mitad de los pasos de Reason son INFERIDO-OPERATIVO). Queda como decision del fundador; no he cambiado nada en `web/`.

## 11. Lo que no se hizo y sus limites

- **Voyage sin medir**: no hay clave en esta sesion.
- **La campania completa no se lanzo**: la aprueba el fundador con estas cifras delante.
- **La precision no esta medida contra un humano.** Los contrarios y anadidos de las secciones 6 y 7 son veredictos de Opus 5.5 con cita. Algunos son de frontera (seccion 1, punto 2), y conviene que el fundador lea al menos los 9 que salieron en una sola corrida antes de corregir.
- **Sinteticos y juez son del mismo modelo** (Opus 5.5 genero los sinteticos). La mezcla es ciega, pero un parecido de estilo entre generador y juez puede inflar el recall sintetico. El contrario conocido, escrito por el catalogo y no por el generador, tambien salio en todas las corridas.
- **El oro de busqueda de los reales** es una muestra de 40 pasos leidos por Opus sobre el libro entero, no una lectura humana.
- **La proyeccion extrapola** el coste por paso de Reason; cada libro pedira su prueba de recall propia.
- El intento 1 no llego a la pasada 2: lo supero el anadido del fundador.

## 12. Ficheros

- `docs/fidelidad/PILOTO_REASON.md`: este reporte.
- `docs/fidelidad/VEREDICTOS_PASOS.jsonl`: una linea por paso real de Reason (nodo, paso, veredicto, cita con lineas y texto, pasada que lo decidio, datos sin respaldo, paso fiel, veredicto del intento anterior), con una cabecera que trae las definiciones.
- `docs/fidelidad/INVENTARIO_NODOS.jsonl` e `INVENTARIO_LIBROS.json`: la fase 0.
- `docs/fidelidad/pruebas/`: los sinteticos (marcados como tales) y las claves ciegas de cada intento. Nunca en `dataset/`.
- `docs/fidelidad/piloto_reason/`: las mezclas, las consultas, el oro, las medidas de busqueda, las salidas de cada pasada y la respuesta cruda de cada llamada (`crudo/`), el coste de cada llamada (`COSTES_LLAMADAS.jsonl`), `RECALL_iN.json` y `ESTABILIDAD_i2_i3.json`.
- `docs/fidelidad/herramientas/`: `inventario.py`, `comun.py`, `sinteticos.py`, `mezclar.py`, `busqueda.py`, `pasadas.py`, `recall.py` y `tablas.py`. Los fragmentos del libro se regeneran desde el txt del fundador y no se commitean.
