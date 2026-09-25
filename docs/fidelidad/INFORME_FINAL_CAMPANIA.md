NINGUN CONTRARIO CONOCIDO QUEDA EN PRODUCCION

# CAMPANIA DE FIDELIDAD TOTAL: INFORME FINAL

## Estado del catalogo, solo con lo probado

> **Los 15311 pasos accionables vivos del catalogo de My Idea se leyeron a ciegas contra su fuente, cada uno por al menos dos lectores independientes salvo 3 que quedaron OPERATIVOS con una sola lectura; los 101 que la contradecian y los 227 que afirmaban algo que la fuente no respalda tienen su correccion declarada en produccion, con cita literal, y un script lo comprueba contra main (0 y 0 sin corregir). Los demas campos que llegan a la IA o a la pantalla (resumen, entregable, condiciones, titulo y etiqueta) de los 3169 nodos vivos se leyeron tambien a ciegas contra su fuente, buscando solo contrarios y anadidos de cifra, plazo o norma: los 78 hallados tienen su correccion declarada en produccion (0 sin corregir). No esta demostrado que no quede ningun error sin detectar, y en esos campos no se buscaron anadidos practicos.**

Mandato del fundador: nunca le diremos a un cliente lo contrario de lo que dice su fuente. Busqueda en la rama fidelidad-total; correccion en la rama correcciones-fidelidad, llevada a main por avance rapido en las tandas fidelidad-t1 a fidelidad-t15. Todo con claude-opus-5-5; los agentes solo leyeron, clasificaron, verificaron y propusieron; la sesion escribio cada fichero e hizo cada commit. Este informe incluye lo hecho por las decisiones del fundador recogidas el 24 sep 2026 (secciones 8 a 10; fechadas 27 sep por error, vale la fecha del commit: docs/PENDIENTES.md seccion 0).

## 1. Cobertura, comprobada por script

**15311 pasos vivos, 15311 con veredicto, 0 sin veredicto, 0 duplicados, 0 que no existan** (campania/COBERTURA_FINAL.json).

**Cada paso vivo tiene al menos dos lecturas ciegas independientes contra su libro, salvo 3 pasos que el lector de la campania leyo OPERATIVO y que por un caso de borde del flujo no pasaron al verificador (OPERATIVO no se corrige): `amortizacion_y_periodo_de_gracia` p4, `eliminar_metas_numericas_gerencia` p1 y `eliminar_cuotas_numericas_trabajadores` p2.** Los no FIEL: lector y verificador ciego, y arbitro si no coincidian. Los FIEL: los muestreados en la campania por el verificador; todos los demas, por la segunda pasada ciega de la decision 5 (2763 de seguridad y salud y de legal y dinero, y su ampliacion a los 6186 del resto).

## 2. Censo por clase

| clase | campania | ahora | que se hizo |
|---|---:|---:|---|
| FIEL | 10693 | 9849 | nada |
| OPERATIVO | 4301 | 5134 | **no se toca** (decision del fundador 2: los OPERATIVOS se quedan) |
| ANADIDO | 224 | 227 | por regla: cifra, plazo, norma o materia legal, quitado o sustituido por el libro; practico, "Sugerencia de My Idea: ..." |
| CONTRARIO | 93 | 101 | **todos corregidos** con la version fiel, con su cita |

Lo que cambio despues de la campania:

| fuente | de | a | pasos |
|---|---|---|---:|
| ampliacion | FIEL | ANADIDO | 1 |
| ampliacion | FIEL | CONTRARIO | 2 |
| ampliacion | FIEL | OPERATIVO | 556 |
| arbitraje excepciones | OPERATIVO | ANADIDO | 2 |
| arbitraje excepciones | OPERATIVO | CONTRARIO | 1 |
| segunda pasada | FIEL | CONTRARIO | 5 |
| segunda pasada | FIEL | OPERATIVO | 280 |

**Los CONTRARIOS, comprobado por script contra main:** 101 CONTRARIOS conocidos (los del registro, los del muestreo, el del arbitraje de las excepciones y los de la segunda pasada y su ampliacion); **0 sin corregir** (scratchpad censo_final2.py).

## 3. Lo medido del metodo

- **Trampas en la campania:** 532 de 532 cazadas por los lectores y 532 de 532 por los verificadores ciegos; 32 de 32 en el tramo 1 calibrado.
- **Trampas en la segunda pasada:** lectores 100 de 100, verificadores 100 de 100; en la ampliacion, lectores 223 de 224 y verificadores 224 de 224.
  El lector del lote Q027 no cazo una trampa en dos lecturas (la leyo OPERATIVO; su verificador si la cazo). Por eso un verificador ciego extra releyo los 79 FIEL no muestreados de ese lote con sus 4 trampas dentro: 4 de 4, ningun ANADIDO ni CONTRARIO, 15 OPERATIVO (campania/p3/VERIFICADOR_EXTRA_Q027.json).
- **Desacuerdos lector frente a verificador:** 656 en la campania, 124 en la segunda pasada y 191 en la ampliacion; todos arbitrados releyendo el libro.
- **Lo que encontro la segunda lectura de los FIEL:** 7 CONTRARIOS y 1 ANADIDO en 8949 pasos (0,08 por ciento), todos corregidos. Los CONTRARIOS escondidos eran sutiles: un plazo alargado ("cada semana o dos" frente a "every week or so"), un criterio estrechado ("negocios fallidos" frente a "con o sin exito"), una consecuencia invertida ("bajos costos" de la sobrecapacidad frente a "higher costs").
- **Limites, dichos:** las trampas las escribe el mismo modelo que las caza; un solo arbitro por desacuerdo; la frontera FIEL y OPERATIVO es blanda (la segunda lectura paso 836 FIEL a OPERATIVO), la que importa es la de ANADIDO y CONTRARIO; las guias de empaque escaneadas con columnas mezcladas no permiten cita literal contigua (seccion 7). "Ningun contrario conocido" es verdad; que no quede ninguno sin detectar no esta demostrado, pero cada paso, salvo esos 3 OPERATIVOS, ya lo leyeron dos lectores ciegos distintos.

## 4. Tandas en produccion (main, avance rapido, con Gate 0 entero y las dos suites en verde)

| tanda | commit | correcciones | de ellas CONTRARIO | sugerencias de My Idea | nodos |
|---|---|---:|---:|---:|---:|
| fidelidad-t1 | 8808bf61 | 11 | 9 | 0 | 7 |
| fidelidad-t2 | c5182833 | 10 | 10 | 0 | 6 |
| fidelidad-t3 | a6015754 | 55 | 0 | 23 | 39 |
| fidelidad-t4 | fe8a88ee | 38 | 18 | 11 | 32 |
| fidelidad-t5 | 8f12a32e | 64 | 17 | 25 | 43 |
| fidelidad-t6 | 5ce22234 | 23 | 9 | 9 | 20 |
| fidelidad-t7 | f868f1ca | 51 | 22 | 15 | 33 |
| fidelidad-t8 | 8f4e7467 | 65 | 24 | 24 | 50 |
| fidelidad-t9 | 7f911164 | 76 | 11 | 41 | 48 |
| fidelidad-t10 | c855e9f4 | 4 | 1 | 3 | 4 |
| fidelidad-t11 | 7263d971 | 6 | 6 | 0 | 5 |
| fidelidad-t12 | f7705aee | 3 | 2 | 1 | 3 |
| fidelidad-t13 | ffccb770 | 3 | 0 | 3 | 2 |
| fidelidad-t14 | c94ae62f | 2 | 0 | 0 | 1 |
| fidelidad-t15 | ec162016 | 76 | 54 | 0 | 72 |
| **total** | | **487** | **183** | **155** | |

Cada correccion vive en el campo `correcciones` de su nodo con el texto viejo, el nuevo, la cita literal (libro, lineas, frase) y la decision (docs/fidelidad/tandas/ en main). Las cuentas de CONTRARIO incluyen los datos repetidos en el resumen o el entregable del mismo nodo.

## 5. Censo por libro

| libro | pasos | FIEL | OPERATIVO | ANADIDO | CONTRARIO |
|---|---:|---:|---:|---:|---:|
| Juran's Quality Handbook_ The C - Joseph A. Defeo | 2297 | 1652 | 625 | 13 | 7 |
| The Green to Gold Business Play - Daniel C. Esty | 933 | 645 | 283 | 1 | 4 |
| The Startup Owner's Manual - Blank, Steve | 864 | 731 | 119 | 10 | 4 |
| Franchise Your Business - Mark Siebert | 828 | 567 | 249 | 5 | 7 |
| Winning at New Products - Robert G. Cooper | 759 | 631 | 114 | 10 | 4 |
| Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev | 702 | 353 | 336 | 6 | 7 |
| A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) | 665 | 470 | 188 | 2 | 5 |
| Venture Deals - Brad Feld | 585 | 357 | 213 | 8 | 7 |
| Essentials of Supply Chain Management - Michael H. Hugos | 535 | 353 | 173 | 7 | 2 |
| The Founder's Dilemmas - Wasserman, Noam | 486 | 248 | 229 | 9 | 0 |
| The Hard Thing About Hard Things - Ben Horowitz | 452 | 265 | 171 | 11 | 5 |
| The Field Guide to Understandin - Dekker, Sidney | 424 | 256 | 159 | 8 | 1 |
| Quality is free _ the art of making quality certain -- Philip B_ Crosb | 406 | 270 | 128 | 3 | 5 |
| Managing the Risks of Organizat - Reason, J. T_ | 403 | 159 | 237 | 6 | 1 |
| The Lean Startup - Eric Ries | 352 | 252 | 93 | 5 | 2 |
| Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe | 348 | 193 | 143 | 10 | 2 |
| Traction - Gabriel Weinberg | 343 | 251 | 85 | 3 | 4 |
| Never Lose a Customer Again - Joey Coleman | 341 | 203 | 130 | 6 | 2 |
| Change by Design, Revised and U - Tim Brown | 335 | 185 | 145 | 2 | 3 |
| Assembling Tomorrow: A Guide to Designing a Thriving Future | 295 | 83 | 203 | 8 | 1 |
| A Project Manager's Book of Forms - Cynthia Stackpole Snyder | 283 | 254 | 29 | 0 | 0 |
| Business Model Generation - Osterwalder, Alexander | 243 | 181 | 54 | 7 | 1 |
| SMALL_BUSINESS | 238 | 166 | 60 | 10 | 2 |
| Cradle to Cradle - Michael Braungart | 229 | 100 | 127 | 1 | 1 |
| Value Proposition Design | 200 | 166 | 34 | 0 | 0 |
| SPIN Selling - Neil Rackham | 175 | 110 | 60 | 3 | 2 |
| Co-Intelligence_ Living and Wor - Ethan Mollick | 173 | 43 | 117 | 11 | 2 |
| The Art of Thought - Wallas, Graham | 154 | 56 | 93 | 4 | 1 |
| Edwards et al., Managing Project Risks | 123 | 29 | 84 | 8 | 2 |
| NIST SP 1318: Protecting CUI (SP 800-171 r3) - Small Business Primer | 115 | 98 | 15 | 2 | 0 |
| Diana L. Lindstrom, Procurement Project Management Success (J. Ross, 2 | 114 | 36 | 69 | 7 | 2 |
| The field guide to human-centered design | 90 | 68 | 20 | 2 | 0 |
| Chris Voss, Rompe la barrera del no | 86 | 34 | 44 | 2 | 6 |
| OSHA3885 | 84 | 70 | 10 | 4 | 0 |
| Rushton, Croucher y Baker, The Handbook of Logistics and Distribution  | 63 | 11 | 46 | 6 | 0 |
| DeMarco y Lister, Waltzing with Bears | 55 | 13 | 34 | 5 | 3 |
| NIST SP 1314: Risk Management Framework - Small Enterprise Quick Start | 45 | 38 | 7 | 0 | 0 |
| Guia de empaque para envios (FedEx) | 44 | 17 | 22 | 2 | 3 |
| Businessperson's Guide to Federal Warranty Law | 40 | 22 | 17 | 1 | 0 |
| Hubbard, The Failure of Risk Management | 40 | 8 | 30 | 0 | 2 |
| Sharon Cullinane, E-Logistics, Cap. 8 (B2C e-commerce y fulfilment) | 38 | 0 | 35 | 3 | 0 |
| OSHA3886 | 37 | 31 | 6 | 0 | 0 |
| NIST SP 1300: Cybersecurity Framework 2.0 - Small Business Quick-Start | 35 | 32 | 3 | 0 | 0 |
| Cybersecurity for Small Business: Understanding the NIST Cybersecurity | 28 | 22 | 6 | 0 | 0 |
| Getting Started with the NIST Privacy Framework: A Guide for Small and | 28 | 21 | 7 | 0 | 0 |
| Max Muller, Essentials of Inventory Management | 25 | 12 | 11 | 2 | 0 |
| ISTA 3P, Protocolo de ensayo de empaque para paqueteria | 24 | 8 | 12 | 3 | 1 |
| The Startup Owner's Manual - Blank, Steve / Never Lose a Customer Agai | 23 | 13 | 10 | 0 | 0 |
| Guia visual de empaque | 20 | 6 | 11 | 3 | 0 |
| DHL Express, Guia de empaque | 15 | 5 | 9 | 1 | 0 |
| The Founder's Dilemmas - Wasserman, Noam / The Hard Thing About Hard T | 15 | 10 | 5 | 0 | 0 |
| Requisitos de empaque de los couriers | 14 | 3 | 8 | 3 | 0 |
| Venture Deals - Brad Feld / The Founder's Dilemmas - Wasserman, Noam | 14 | 10 | 4 | 0 | 0 |
| The Startup Owner's Manual - Blank, Steve / The Lean Startup - Eric Ri | 8 | 7 | 1 | 0 | 0 |
| The Startup Owner's Manual - Blank, Steve / Traction - Gabriel Weinber | 8 | 8 | 0 | 0 | 0 |
| The Lean Startup - Eric Ries / The Hard Thing About Hard Things - Ben  | 7 | 6 | 1 | 0 | 0 |
| The Art of Thought - Graham Wallas | 6 | 3 | 2 | 1 | 0 |
| The Startup Owner's Manual - Blank, Steve / Never Lose a Customer Agai | 6 | 3 | 3 | 0 | 0 |
| Guia de empaque para transporte | 5 | 2 | 2 | 1 | 0 |
| Síntesis de tono de DeMarco y Lister, Waltzing with Bears (nodo ancla  | 4 | 3 | 0 | 1 | 0 |
| Síntesis del método aplicado al emprendedor individual (riesgo de rota | 4 | 0 | 3 | 1 | 0 |

## 6. CENSO DE OPERATIVOS

**5134 pasos OPERATIVOS** (33.5 por ciento del catalogo): concretan lo que su libro dice, en su misma direccion y sin datos nuevos. Decision del fundador 2: se quedan. Por libro, de mas a menos:

| libro | OPERATIVOS | de sus pasos |
|---|---:|---:|
| Juran's Quality Handbook_ The C - Joseph A. Defeo | 625 | 27% |
| Out of the Crisis, Reissue - Deming, W. Edwards; Cahill, Kev | 336 | 48% |
| The Green to Gold Business Play - Daniel C. Esty | 283 | 30% |
| Franchise Your Business - Mark Siebert | 249 | 30% |
| Managing the Risks of Organizat - Reason, J. T_ | 237 | 59% |
| The Founder's Dilemmas - Wasserman, Noam | 229 | 47% |
| Venture Deals - Brad Feld | 213 | 36% |
| Assembling Tomorrow: A Guide to Designing a Thriving Future | 203 | 69% |
| A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition) | 188 | 28% |
| Essentials of Supply Chain Management - Michael H. Hugos | 173 | 32% |
| The Hard Thing About Hard Things - Ben Horowitz | 171 | 38% |
| The Field Guide to Understandin - Dekker, Sidney | 159 | 38% |
| Change by Design, Revised and U - Tim Brown | 145 | 43% |
| Financial Intelligence for Entrepreneurs - Berman, Karen; Knight, Joe | 143 | 41% |
| Never Lose a Customer Again - Joey Coleman | 130 | 38% |
| Quality is free _ the art of making quality certain -- Philip B_ Crosb | 128 | 32% |
| Cradle to Cradle - Michael Braungart | 127 | 55% |
| The Startup Owner's Manual - Blank, Steve | 119 | 14% |
| Co-Intelligence_ Living and Wor - Ethan Mollick | 117 | 68% |
| Winning at New Products - Robert G. Cooper | 114 | 15% |
| The Art of Thought - Wallas, Graham | 93 | 60% |
| The Lean Startup - Eric Ries | 93 | 26% |
| Traction - Gabriel Weinberg | 85 | 25% |
| Edwards et al., Managing Project Risks | 84 | 68% |
| Diana L. Lindstrom, Procurement Project Management Success (J. Ross, 2 | 69 | 61% |
| SMALL_BUSINESS | 60 | 25% |
| SPIN Selling - Neil Rackham | 60 | 34% |
| Business Model Generation - Osterwalder, Alexander | 54 | 22% |
| Rushton, Croucher y Baker, The Handbook of Logistics and Distribution  | 46 | 73% |
| Chris Voss, Rompe la barrera del no | 44 | 51% |
| Sharon Cullinane, E-Logistics, Cap. 8 (B2C e-commerce y fulfilment) | 35 | 92% |
| DeMarco y Lister, Waltzing with Bears | 34 | 62% |
| Value Proposition Design | 34 | 17% |
| Hubbard, The Failure of Risk Management | 30 | 75% |
| A Project Manager's Book of Forms - Cynthia Stackpole Snyder | 29 | 10% |
| Guia de empaque para envios (FedEx) | 22 | 50% |
| The field guide to human-centered design | 20 | 22% |
| Businessperson's Guide to Federal Warranty Law | 17 | 42% |
| NIST SP 1318: Protecting CUI (SP 800-171 r3) - Small Business Primer | 15 | 13% |
| ISTA 3P, Protocolo de ensayo de empaque para paqueteria | 12 | 50% |
| Guia visual de empaque | 11 | 55% |
| Max Muller, Essentials of Inventory Management | 11 | 44% |
| OSHA3885 | 10 | 12% |
| The Startup Owner's Manual - Blank, Steve / Never Lose a Customer Agai | 10 | 43% |
| DHL Express, Guia de empaque | 9 | 60% |
| Requisitos de empaque de los couriers | 8 | 57% |
| Getting Started with the NIST Privacy Framework: A Guide for Small and | 7 | 25% |
| NIST SP 1314: Risk Management Framework - Small Enterprise Quick Start | 7 | 16% |
| Cybersecurity for Small Business: Understanding the NIST Cybersecurity | 6 | 21% |
| OSHA3886 | 6 | 16% |
| The Founder's Dilemmas - Wasserman, Noam / The Hard Thing About Hard T | 5 | 33% |
| Venture Deals - Brad Feld / The Founder's Dilemmas - Wasserman, Noam | 4 | 29% |
| NIST SP 1300: Cybersecurity Framework 2.0 - Small Business Quick-Start | 3 | 9% |
| Síntesis del método aplicado al emprendedor individual (riesgo de rota | 3 | 75% |
| The Startup Owner's Manual - Blank, Steve / Never Lose a Customer Agai | 3 | 50% |
| Guia de empaque para transporte | 2 | 40% |
| The Art of Thought - Graham Wallas | 2 | 33% |
| The Lean Startup - Eric Ries / The Hard Thing About Hard Things - Ben  | 1 | 14% |
| The Startup Owner's Manual - Blank, Steve / The Lean Startup - Eric Ri | 1 | 12% |

## 7. EXCEPCIONES

Ver docs/fidelidad/EXCEPCIONES.md. Ninguna es un CONTRARIO sin corregir.

## 8. Decisiones del fundador recogidas el 24 sep 2026, una por una

1. **Textos derivados.** Se buscaron los textos anteriores de las 120 correcciones de CONTRARIO y las 125 de cifra, plazo o norma en la cache de preguntas y en todo fichero derivado. Ninguna pregunta contiene un texto viejo; pero el generador lee los 400 primeros caracteres del resumen, asi que las preguntas cuyo resumen se corrigio dentro de ese tramo se **retiraron de la cache: 75** (docs/fidelidad/PREGUNTAS_RETIRADAS.json en main, con la pregunta, sus candidatos y la correccion que la invalida). Caen a la generica que la sesion adapta en vivo. El master_graph lleva el campo `correcciones` con los textos viejos, pero ningun codigo de web/ lo lee ni lo manda a un prompt. 7 textos viejos siguen identicos en nodos deprecados, que la app no ofrece y que resuelven al superviviente corregido.
2. **OPERATIVOS: se quedan.** Lista de atribuciones a autor para la sesion de idiomas: docs/fidelidad/ATRIBUCIONES_A_AUTOR.md en main (el codigo de web/ no atribuye nada ni lee el campo fuente; los nombres de autor viven dentro del texto de 241 nodos, con fichero y linea).
3. **EXCEPCIONES.** Las 4 con desacuerdo, a un arbitro con el libro (campania/ARBITRAJE_EXCEPCIONES.json): 1 CONTRARIO y 3 ANADIDOS practicos, corregidos en fidelidad-t10. Las 3 guias escaneadas: el fundador reconvierte los PDF y los pasara; pendientes (EXCEPCIONES.md, seccion B).
4. **Criterios ratificados:** quitar el dominio en los 3 pasos; el prefijo "Sugerencia de My Idea:"; la voz de la casa solo si el significado no cambia, con registro y cita.
5. **Segunda pasada ciega dirigida:** 2763 FIEL de seguridad y salud y de legal y dinero dieron 5 CONTRARIOS (fidelidad-t11); por la regla, se amplio al resto de los FIEL (6186), que dio 2 CONTRARIOS y 1 ANADIDO (fidelidad-t12). Registro: campania/p2/ y campania/p3/.
6. **Documentacion:** docs/fidelidad/ de esta rama y el informe del muestreo se fusionan a main como archivo.
7. **Sesion con credencial:** 52 nodos a re-embeber (el indice embebe titulo, resumen y condiciones, no los pasos) y 75 preguntas a regenerar; listas exactas en docs/fidelidad/credencial/ de main (LISTAS.md con la razon de cada una).

## 9. Segundas decisiones del fundador, recogidas el 24 sep 2026

1. **Ratificados** los textos que la sesion ajusto (EXCEPCIONES.md, seccion C).
2. **Atribuciones:** los nombres de autor dentro del texto de los nodos se quedan; no hay cambio de interfaz pendiente.
3. **Pagina del auditor externo** actualizada con estas cifras.
4. **Guias escaneadas:** el fundador reextrajo los PDF linea por linea con coordenadas. La infografia se identifico como la de UPS por el encabezado de su extraccion; la de DHL se comparo con la version oficial descargada (23/07/2026 frente a la local del 25/02/2026: mismo texto salvo un parrafo nuevo sobre "black foil"; la frase citada identica). Las dos ya tienen cita literal: 3 ANADIDOS practicos a "Sugerencia de My Idea:" en fidelidad-t13. Al comprobar por script que cada ANADIDO del censo tuviera su correccion aparecio uno sin corregir: `creacion_option_pool` p2, una excepcion del bloque B1 que se habia perdido (la cita no se reconocio por unas comillas tipograficas y nunca paso a EXCEPCIONES.md). Corregido en fidelidad-t14, junto con una cifra cambiada en su resumen ("hasta 20%" frente a "averaged 20%").
5. **Sesion con credencial:** pendiente de que el fundador diga "clave cargada"; listas exactas en docs/fidelidad/credencial/ de main (52 nodos a re-embeber y 75 preguntas a regenerar tras fidelidad-t14).
6. **Frase de estado:** al principio de este informe.

## 10. La pasada sobre los campos que llegan a la IA o a la pantalla

Decision del fundador (recogida el 24 sep): medir que campos llegan a la IA o a la pantalla (docs/fidelidad/CAMPOS_QUE_LLEGAN.md en main) y, si alguno aparte de los pasos llega, leerlo contra la fuente con el mismo metodo calibrado, buscando solo CONTRARIOS y ANADIDOS de cifra, plazo o norma. Llegan el resumen, el entregable, las condiciones de activacion, el titulo y la etiqueta de cara.

- **Cobertura:** 3169 nodos vivos, una fila por nodo con sus cinco campos, en 71 lotes.
- **Trampas:** 284 nodos trampa con un error sembrado; lectores 283, verificadores 282. La trampa de R013 (un plazo de 12 meses anadido en una condicion) se escapo a cuatro lecturas: lector, relectura, verificador y un verificador ciego extra, que releyo los nodos limpios no muestreados de ese lote sin encontrar nada en los reales.
- **Desacuerdos arbitrados:** 22.
- **Hallazgos:** 78 en 72 nodos: 43 resumen CONTRARIO, 13 entregable ANADIDO, 7 entregable CONTRARIO, 7 condiciones ANADIDO, 4 condiciones CONTRARIO, 3 resumen ANADIDO, 1 etiqueta CONTRARIO. Corregidos en fidelidad-t15 (76 correcciones), cada uno con su cita literal; 0 sin corregir.
- **Textos derivados:** 50 preguntas de la cache retiradas (nacieron de un resumen o de las condiciones de un candidato ahora corregidos) y 2 puertas del mundo entrega restauradas por la guarda AUD-09 H13, sin el dato corregido. Segunda sesion con credencial pendiente: listas en docs/fidelidad/credencial/ de main.
- **Registro:** campania/campos/ (VEREDICTOS_CAMPOS.jsonl, RESUMEN.json, VERIFICADOR_EXTRA_R013.json y el rastro de cada lote).
