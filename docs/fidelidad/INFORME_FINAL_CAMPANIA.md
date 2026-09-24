NINGUN CONTRARIO CONOCIDO QUEDA EN PRODUCCION

# CAMPANIA DE FIDELIDAD TOTAL: INFORME FINAL

Mandato del fundador: nunca le diremos a un cliente lo contrario de lo que dice su fuente. Busqueda en la rama fidelidad-total; correccion en la rama correcciones-fidelidad, llevada a main por avance rapido en las tandas fidelidad-t1 a fidelidad-t9. Todo con claude-opus-5-5; los agentes solo leyeron, clasificaron, verificaron y propusieron; la sesion escribio cada fichero e hizo cada commit.

## 1. Cobertura, comprobada por script

**15311 pasos vivos, 15311 con veredicto, 0 sin veredicto, 0 duplicados, 0 que no existan** (docs/fidelidad/campania/COBERTURA_FINAL.json). Fuentes del registro: el tramo 1 calibrado (VEREDICTOS_TRAMO1.jsonl, 827 pasos) y la campania (c2/VEREDICTOS_CAMPANIA.jsonl, 14484 pasos, 133 lotes, que incluyen Reason y Assembling Tomorrow releidos enteros).

## 2. Censo por clase

| clase | pasos | que se hizo |
|---|---:|---|
| FIEL | 10693 | nada |
| OPERATIVO | 4301 | **no se toca**; su politica la decide el fundador con esta cifra delante (seccion 6) |
| ANADIDO | 224 | por regla: cifra, plazo, norma o materia legal, quitado o sustituido por el libro; practico, "Sugerencia de My Idea: ..."; lo que la regla no resolvio limpio, a EXCEPCIONES |
| CONTRARIO | 93 | **todos corregidos** con la version fiel del verificador (o del arbitro), con su cita |

**Los CONTRARIOS, comprobado por script contra main:** cada uno de los 93 CONTRARIOS conocidos (los del registro mas los 5 del muestreo) tiene en su nodo una correccion declarada de ese paso (scratchpad contrarios_en_produccion.py: 93 de 93, 0 sin corregir).

## 3. Lo medido del metodo

- **Trampas:** 532 de 532 cazadas por los lectores y 532 de 532 por los verificadores ciegos en la campania; 32 de 32 en el tramo 1. Ningun lote tuvo que releerse.
- **Desacuerdos lector frente a verificador:** 656, todos arbitrados releyendo el libro.
- **FIEL releidos a ciegas:** 1731; 141 eran OPERATIVO y **1 era CONTRARIO** (cazado y corregido). Tasa de CONTRARIO escondido entre los FIEL: 0,06 por ciento, intervalo de Wilson al 95 por ciento de 0,01 a 0,33. **Lo que eso significa, dicho claro:** entre los unos 8960 pasos FIEL que no se muestrearon puede quedar del orden de 5 CONTRARIOS no detectados (cota superior al 95 por ciento: unos 30). "Ningun contrario conocido" es verdad; "ningun contrario" no esta demostrado.
- **Limites:** las trampas las escribe el mismo modelo que las caza; un solo arbitro por desacuerdo; las guias de empaque escaneadas con columnas mezcladas no permiten cita literal contigua.

## 4. Tandas en produccion (main, avance rapido, con Gate 0 entero y las dos suites en verde)

| tanda | correcciones | de ellas CONTRARIO | sugerencias de My Idea | nodos |
|---|---:|---:|---:|---:|
| fidelidad-t1 | 11 | 9 | 0 | 7 |
| fidelidad-t2 | 10 | 10 | 0 | 6 |
| fidelidad-t3 | 55 | 0 | 23 | 39 |
| fidelidad-t4 | 38 | 18 | 11 | 32 |
| fidelidad-t5 | 64 | 17 | 25 | 43 |
| fidelidad-t6 | 23 | 9 | 9 | 20 |
| fidelidad-t7 | 51 | 22 | 15 | 33 |
| fidelidad-t8 | 65 | 24 | 24 | 50 |
| fidelidad-t9 | 76 | 11 | 41 | 48 |
| **total** | **393** | **120** | **148** | |

Cada correccion vive en el campo `correcciones` de su nodo con el texto viejo, el nuevo, la cita literal (libro, lineas, frase) y la decision (rama correcciones-fidelidad, docs/fidelidad/tandas/). Las cuentas de CONTRARIO de la tabla incluyen los datos repetidos en el resumen o el entregable del mismo nodo.

## 5. Censo por libro

| libro | pasos | FIEL | OPERATIVO | ANADIDO | CONTRARIO |
|---|---:|---:|---:|---:|---:|
| Juran's Quality Handbook_ The C - Joseph A. Defeo | 2297 | 1791 | 486 | 13 | 7 |
| The Green to Gold Business Play - Daniel C. Esty | 933 | 686 | 242 | 1 | 4 |
| The Startup Owner's Manual - Blank, Steve | 864 | 749 | 101 | 10 | 4 |
| Franchise Your Business - Mark Siebert | 828 | 618 | 201 | 5 | 4 |
| Winning at New Products - Robert G. Cooper | 759 | 652 | 93 | 10 | 4 |
| Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev | 702 | 440 | 250 | 5 | 7 |
| A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) | 665 | 483 | 175 | 2 | 5 |
| Venture Deals - Brad Feld | 585 | 386 | 185 | 8 | 6 |
| Essentials of Supply Chain Management - Michael H. Hugos | 535 | 373 | 154 | 7 | 1 |
| The Founder's Dilemmas - Wasserman, Noam | 486 | 283 | 194 | 9 | 0 |
| The Hard Thing About Hard Things - Ben Horowitz | 452 | 291 | 145 | 11 | 5 |
| The Field Guide to Understandin - Dekker, Sidney | 424 | 298 | 117 | 8 | 1 |
| Quality is free _ the art of making quality certain -- Philip B_ Crosb | 406 | 294 | 104 | 3 | 5 |
| Managing the Risks of Organizat - Reason, J. T_ | 403 | 184 | 214 | 4 | 1 |
| The Lean Startup - Eric Ries | 352 | 276 | 70 | 5 | 1 |
| Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe | 348 | 215 | 121 | 10 | 2 |
| Traction - Gabriel Weinberg | 343 | 261 | 75 | 3 | 4 |
| Never Lose a Customer Again - Joey Coleman | 341 | 215 | 118 | 6 | 2 |
| Change by Design, Revised and U - Tim Brown | 335 | 203 | 127 | 2 | 3 |
| Assembling Tomorrow: A Guide to Designing a Thriving Future | 295 | 124 | 163 | 8 | 0 |
| A Project Manager's Book of Forms - Cynthia Stackpole Snyder | 283 | 259 | 24 | 0 | 0 |
| Business Model Generation - Osterwalder, Alexander | 243 | 186 | 49 | 7 | 1 |
| SMALL_BUSINESS | 238 | 197 | 29 | 10 | 2 |
| Cradle to Cradle - Michael Braungart | 229 | 117 | 110 | 1 | 1 |
| Value Proposition Design | 200 | 172 | 28 | 0 | 0 |
| SPIN Selling - Neil Rackham | 175 | 113 | 57 | 3 | 2 |
| Co-Intelligence_ Living and Wor - Ethan Mollick | 173 | 52 | 108 | 11 | 2 |
| The Art of Thought - Wallas, Graham | 154 | 66 | 83 | 4 | 1 |
| Edwards et al., Managing Project Risks | 123 | 35 | 78 | 8 | 2 |
| NIST SP 1318: Protecting CUI (SP 800-171 r3) - Small Business Primer | 115 | 100 | 13 | 2 | 0 |
| Diana L. Lindstrom, Procurement Project Management Success (J. Ross, 2 | 114 | 40 | 65 | 7 | 2 |
| The field guide to human-centered design | 90 | 69 | 19 | 2 | 0 |
| Chris Voss, Rompe la barrera del no | 86 | 35 | 43 | 2 | 6 |
| OSHA3885 | 84 | 74 | 6 | 4 | 0 |
| Rushton, Croucher y Baker, The Handbook of Logistics and Distribution  | 63 | 21 | 36 | 6 | 0 |
| DeMarco y Lister, Waltzing with Bears | 55 | 15 | 33 | 5 | 2 |
| NIST SP 1314: Risk Management Framework - Small Enterprise Quick Start | 45 | 38 | 7 | 0 | 0 |
| Guia de empaque para envios (FedEx) | 44 | 24 | 15 | 2 | 3 |
| Businessperson's Guide to Federal Warranty Law | 40 | 23 | 16 | 1 | 0 |
| Hubbard, The Failure of Risk Management | 40 | 12 | 26 | 0 | 2 |
| Sharon Cullinane, E-Logistics, Cap. 8 (B2C e-commerce y fulfilment) | 38 | 0 | 35 | 3 | 0 |
| OSHA3886 | 37 | 33 | 4 | 0 | 0 |
| NIST SP 1300: Cybersecurity Framework 2.0 - Small Business Quick-Start | 35 | 32 | 3 | 0 | 0 |
| Cybersecurity for Small Business: Understanding the NIST Cybersecurity | 28 | 22 | 6 | 0 | 0 |
| Getting Started with the NIST Privacy Framework: A Guide for Small and | 28 | 24 | 4 | 0 | 0 |
| Max Muller, Essentials of Inventory Management | 25 | 13 | 10 | 2 | 0 |
| ISTA 3P, Protocolo de ensayo de empaque para paqueteria | 24 | 9 | 11 | 3 | 1 |
| The Startup Owner's Manual - Blank, Steve / Never Lose a Customer Agai | 23 | 15 | 8 | 0 | 0 |
| Guia visual de empaque | 20 | 8 | 9 | 3 | 0 |
| DHL Express, Guia de empaque | 15 | 8 | 6 | 1 | 0 |
| The Founder's Dilemmas - Wasserman, Noam / The Hard Thing About Hard T | 15 | 11 | 4 | 0 | 0 |
| Requisitos de empaque de los couriers | 14 | 6 | 5 | 3 | 0 |
| Venture Deals - Brad Feld / The Founder's Dilemmas - Wasserman, Noam | 14 | 10 | 4 | 0 | 0 |
| The Startup Owner's Manual - Blank, Steve / The Lean Startup - Eric Ri | 8 | 7 | 1 | 0 | 0 |
| The Startup Owner's Manual - Blank, Steve / Traction - Gabriel Weinber | 8 | 8 | 0 | 0 | 0 |
| The Lean Startup - Eric Ries / The Hard Thing About Hard Things - Ben  | 7 | 6 | 1 | 0 | 0 |
| The Art of Thought - Graham Wallas | 6 | 3 | 2 | 1 | 0 |
| The Startup Owner's Manual - Blank, Steve / Never Lose a Customer Agai | 6 | 3 | 3 | 0 | 0 |
| Guia de empaque para transporte | 5 | 2 | 2 | 1 | 0 |
| Síntesis de tono de DeMarco y Lister, Waltzing with Bears (nodo ancla  | 4 | 3 | 0 | 1 | 0 |
| Síntesis del método aplicado al emprendedor individual (riesgo de rota | 4 | 0 | 3 | 1 | 0 |

## 6. CENSO DE OPERATIVOS, para la decision del fundador

**4301 pasos OPERATIVOS** (28.1 por ciento del catalogo): concretan lo que su libro dice, en su misma direccion y sin datos nuevos. No se toco ninguno. Por libro, de mas a menos:

| libro | OPERATIVOS | de sus pasos |
|---|---:|---:|
| Juran's Quality Handbook_ The C - Joseph A. Defeo | 486 | 21% |
| Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev | 250 | 36% |
| The Green to Gold Business Play - Daniel C. Esty | 242 | 26% |
| Managing the Risks of Organizat - Reason, J. T_ | 214 | 53% |
| Franchise Your Business - Mark Siebert | 201 | 24% |
| The Founder's Dilemmas - Wasserman, Noam | 194 | 40% |
| Venture Deals - Brad Feld | 185 | 32% |
| A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) | 175 | 26% |
| Assembling Tomorrow: A Guide to Designing a Thriving Future | 163 | 55% |
| Essentials of Supply Chain Management - Michael H. Hugos | 154 | 29% |
| The Hard Thing About Hard Things - Ben Horowitz | 145 | 32% |
| Change by Design, Revised and U - Tim Brown | 127 | 38% |
| Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe | 121 | 35% |
| Never Lose a Customer Again - Joey Coleman | 118 | 35% |
| The Field Guide to Understandin - Dekker, Sidney | 117 | 28% |
| Cradle to Cradle - Michael Braungart | 110 | 48% |
| Co-Intelligence_ Living and Wor - Ethan Mollick | 108 | 62% |
| Quality is free _ the art of making quality certain -- Philip B_ Crosb | 104 | 26% |
| The Startup Owner's Manual - Blank, Steve | 101 | 12% |
| Winning at New Products - Robert G. Cooper | 93 | 12% |
| The Art of Thought - Wallas, Graham | 83 | 54% |
| Edwards et al., Managing Project Risks | 78 | 63% |
| Traction - Gabriel Weinberg | 75 | 22% |
| The Lean Startup - Eric Ries | 70 | 20% |
| Diana L. Lindstrom, Procurement Project Management Success (J. Ross, 2 | 65 | 57% |
| SPIN Selling - Neil Rackham | 57 | 33% |
| Business Model Generation - Osterwalder, Alexander | 49 | 20% |
| Chris Voss, Rompe la barrera del no | 43 | 50% |
| Rushton, Croucher y Baker, The Handbook of Logistics and Distribution  | 36 | 57% |
| Sharon Cullinane, E-Logistics, Cap. 8 (B2C e-commerce y fulfilment) | 35 | 92% |
| DeMarco y Lister, Waltzing with Bears | 33 | 60% |
| SMALL_BUSINESS | 29 | 12% |
| Value Proposition Design | 28 | 14% |
| Hubbard, The Failure of Risk Management | 26 | 65% |
| A Project Manager's Book of Forms - Cynthia Stackpole Snyder | 24 | 8% |
| The field guide to human-centered design | 19 | 21% |
| Businessperson's Guide to Federal Warranty Law | 16 | 40% |
| Guia de empaque para envios (FedEx) | 15 | 34% |
| NIST SP 1318: Protecting CUI (SP 800-171 r3) - Small Business Primer | 13 | 11% |
| ISTA 3P, Protocolo de ensayo de empaque para paqueteria | 11 | 46% |
| Max Muller, Essentials of Inventory Management | 10 | 40% |
| Guia visual de empaque | 9 | 45% |
| The Startup Owner's Manual - Blank, Steve / Never Lose a Customer Agai | 8 | 35% |
| NIST SP 1314: Risk Management Framework - Small Enterprise Quick Start | 7 | 16% |
| Cybersecurity for Small Business: Understanding the NIST Cybersecurity | 6 | 21% |
| DHL Express, Guia de empaque | 6 | 40% |
| OSHA3885 | 6 | 7% |
| Requisitos de empaque de los couriers | 5 | 36% |
| Getting Started with the NIST Privacy Framework: A Guide for Small and | 4 | 14% |
| OSHA3886 | 4 | 11% |
| The Founder's Dilemmas - Wasserman, Noam / The Hard Thing About Hard T | 4 | 27% |
| Venture Deals - Brad Feld / The Founder's Dilemmas - Wasserman, Noam | 4 | 29% |
| NIST SP 1300: Cybersecurity Framework 2.0 - Small Business Quick-Start | 3 | 9% |
| Síntesis del método aplicado al emprendedor individual (riesgo de rota | 3 | 75% |
| The Startup Owner's Manual - Blank, Steve / Never Lose a Customer Agai | 3 | 50% |
| Guia de empaque para transporte | 2 | 40% |
| The Art of Thought - Graham Wallas | 2 | 33% |
| The Lean Startup - Eric Ries / The Hard Thing About Hard Things - Ben  | 1 | 14% |
| The Startup Owner's Manual - Blank, Steve / The Lean Startup - Eric Ri | 1 | 12% |

## 7. EXCEPCIONES para el fundador

Ver docs/fidelidad/EXCEPCIONES.md: lo que la regla no resolvio limpio, sin corregir. Ninguna es un CONTRARIO.

## 8. Pendiente para la integracion del mundo 11

Anotado en docs/PENDIENTES.md seccion 0a (en main): re-embeber los nodos corregidos y regenerar su cache de preguntas en la sesion con credencial; y, al sincronizar puente-forja con main, regenerar los derivados del grafo en vez de fusionarlos a mano.
