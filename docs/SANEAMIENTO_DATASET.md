# SANEAMIENTO DEL DATASET: LA LISTA COMPLETA DE VERIFICACION (documento vivo)

*Mandato del fundador (26 sep 2026): **el dataset no se declara saneado hasta cumplir esta lista completa.**
Cada criterio lleva su instrumento, su estado (VERIFICADO, A MEDIAS, PENDIENTE) y su evidencia (commit, informe,
cifra). Las cifras sin fuente citada se midieron el 26 sep 2026 sobre `main` en `264fd82e`, solo lectura, con
scripts que no escriben. **Donde la evidencia no alcanza el estado que el mandato le da, la fila lo dice.***

Universo: **3.853** nodos en `dataset/nodos/`, **3.169 vivos** y **684 deprecados**. El mundo 11 vive fuera del
catalogo: **459 nodos** en la forja (`forja-nodos/dataset/nodos.jsonl`) y **20** en su bandeja (Marquet), sin
integrar todavia.

---

## ESTADO DE UN VISTAZO

| # | criterio | estado |
|---|---|---|
| 1 | Duplicados y fusiones | VERIFICADO |
| 2 | Pasos contra su libro | VERIFICADO |
| 3 | Etiquetas del riel contra su nodo, y su vigencia en las traducciones | VERIFICADO |
| 4 | Identificadores | VERIFICADO |
| 5 | Fuentes | VERIFICADO |
| 6 | Aristas por lectura | A MEDIAS (el mandato lo daba por VERIFICADO; ver la fila) |
| 7 | Indice semantico | A MEDIAS (el mandato lo daba por VERIFICADO; ver la fila) |
| 8 | Resumenes y entregables | A MEDIAS |
| 9 | Los 61 puentes al nucleo sin declarar | A MEDIAS |
| 10 | Vigencia de contenido legal, normativo, numerico y de enlaces | PENDIENTE (medido: 313 nodos) |
| 11 | Jurisdiccion (nodos propios de un pais) | PENDIENTE (medido: 110 sin clase) |
| 12 | Coherencia interna de cada nodo | PENDIENTE (medido: 25 incoherentes) |
| 13 | Aristas rancias tras las correcciones | PENDIENTE (medido: 1 por correccion, 149 de antes) |
| 14 | Titulos y condiciones de activacion contra su contenido | PENDIENTE (muestra: 0,0 y 0,3 por ciento) |
| 15 | Fase y dominio de cada nodo | PENDIENTE (muestra: fase 12,3 por ciento, dominio 0,7) |
| 16 | Ortografia y voz de la casa | PENDIENTE |
| 17 | Mundo 11 contra el catalogo (puerta semantica en la integracion) | PENDIENTE |

---

## VERIFICADOS

### 1. Duplicados y fusiones: VERIFICADO
- **Instrumento:** `scripts/censo_duplicacion.py`, `scripts/intra_dominio.py`, `scripts/gradiente_pares.py`; guardas de
  Gate 0 en `scripts/run_phase1.py` (auto-alias, alias con dos duenos, semillas deprecadas, titulos exactos
  duplicados); `engine/test_precedencia_superviviente.py`, `test_gate_alias.py`, `test_gate_deprecado_reciproco.py`.
- **Evidencia:** campania consumada con reparos listados, sello `673fdf4b` (`docs/loop/ACTA_INTEGRAL.md`, 335 de 335
  actos con destino). Medido hoy: 684 deprecados, los 684 resuelven a un superviviente vivo (671 directo, 13 por
  cadena); 761 alias en 562 nodos, 0 con dos duenos, 0 apuntando a un vivo.
- **Residuos a la vista (no bloquean el criterio, se listan):** 13 pares de titulos con similitud de 95 o mas que
  Gate 0 avisa (`docs/loop/SALIDA_integral_GATE0_CMD1_CIERRE_FINAL.txt`); 27 aristas de vivo a deprecado sin
  recablear al superviviente (AUD-09 B15), que se cuentan en el criterio 13.

### 2. Pasos contra su libro: VERIFICADO
- **Instrumento:** campania de fidelidad con lector, trampas, verificador ciego y arbitro;
  `scripts/fidelidad/aplicar_correcciones.py` y `engine/test_aplicar_correcciones_fidelidad.py`.
- **Evidencia:** `docs/fidelidad/INFORME_FINAL_CAMPANIA.md`: 15.311 pasos vivos, 15.311 con veredicto; hoy FIEL 9.849,
  OPERATIVO 5.134, ANADIDO 227, CONTRARIO 101, **0 CONTRARIOS sin corregir**; 487 correcciones en 354 nodos, 15
  tandas (`fidelidad-t1` `8808bf61` a `fidelidad-t15` `ec162016`).
- **Limite declarado:** no esta probado que no quede ningun error sin detectar.

### 3. Etiquetas del riel contra su nodo, y su vigencia en traducciones: VERIFICADO
- **Instrumento:** pasada con trampas y verificador ciego; guardas `engine/test_etiquetas_fidelidad.py`,
  `web/lib/etiquetasCara.test.ts`, `web/lib/i18n/etiquetasVigencia.test.ts` (huella sha-256 de la etiqueta en espanol).
- **Evidencia:** `docs/fidelidad/etiquetas/PASADA_ETIQUETAS.md`: 3.169 leidas, **41 corregidas** (commits `6871a11e`
  y `0f46772d`); trampas 79 de 80 y 78 de 79. Traducciones: 10 idiomas en `web/lib/i18n/etiquetas/`, 3.169 claves
  y 3.169 huellas cada uno, **0 rancias** contra la etiqueta viva, incluidas las 41 (`docs/i18n/F6_INFORME.md`).

### 4. Identificadores: VERIFICADO
- **Instrumento:** Gate 0 (nombres no ASCII, conteo del grafo contra disco, alias, autoaristas);
  `scripts/expansion/validar_esquema.py` (`^[a-z0-9_]+$`).
- **Evidencia:** Gate 0 OK (27 comprobaciones); 0 ids fuera de snake_case, 0 ficheros cuyo nombre difiera de su id.
- **Nota:** 48 ids vivos terminan en sufijo numerico (`_2`, `_3`), que la regla de My-idea admite y la de la forja
  (`forja-nodos/docs/REGLAS_DE_ID.md`) no. Afecta a la integracion del mundo 11, criterio 17.

### 5. Fuentes: VERIFICADO
- **Instrumento:** Gate 0 (fuente canonica, `scripts/loop/verificar_fuente_canonico.py`; nodos con mas de una fuente).
- **Evidencia:** los 3.169 vivos citan su libro (0 vacios, 61 libros distintos), 0 fallos contra la lista canonica,
  8 con mas de una fuente, 0 sin adjudicar.
- **Nota:** la fuente cita el libro, no la pagina; la cita literal con fichero y lineas existe solo en
  `correcciones[].cita` de los 354 nodos corregidos. `fuente` no llega ni a la IA ni a la pantalla
  (`docs/fidelidad/CAMPOS_QUE_LLEGAN.md`).

## A MEDIAS

### 6. Aristas por lectura: A MEDIAS
- **Por que no VERIFICADO:** lo verificado por lectura son las aristas NUEVAS y los pares bidireccionales (Gate 0
  OP-C-05: 154 pares, 154 con cita, 0 sin cita). La mayoria de las 9.914 aristas existentes no se valido una a una
  leyendo. Siguen abiertas 477 aristas que faltan (`docs/loop/ACTA_INTEGRAL.md`), 50 nodos del nucleo inalcanzables
  andando solo por el nucleo (AUD-09 M54) y 233 callejones sin salida (AUD-09 M55).

### 7. Indice semantico: A MEDIAS
- **Por que no VERIFICADO:** la cobertura esta completa (3.169 ids, 3.169 vectores, 0 vivos sin vector, 0 ids muertos;
  Gate 0), pero **52 nodos llevan el vector de su texto viejo** tras la tanda t15
  (`docs/fidelidad/credencial/nodos_a_reembeber.txt`), pendientes de la segunda sesion con credencial, que tambien
  regenera 52 preguntas retiradas (`docs/fidelidad/credencial/preguntas_a_regenerar.txt`).

### 8. Resumenes y entregables: A MEDIAS
- **La pasada de los campos que llegan a la IA TERMINO:** 3.169 nodos en 71 lotes; trampas 283 de 284 y 282 de 284;
  **78 hallazgos en 72 nodos** (resumen: 43 CONTRARIO y 3 ANADIDO; entregable: 7 CONTRARIO y 13 ANADIDO;
  condiciones: 4 CONTRARIO y 7 ANADIDO; etiqueta: 1 CONTRARIO; titulo: 0), **0 sin corregir**
  (`docs/fidelidad/campania/campos/RESUMEN.json`, tanda `fidelidad-t15` `ec162016`).
- **Por que A MEDIAS:** solo busco CONTRARIOS y ANADIDOS de cifra, plazo o norma; los anadidos practicos y la
  coherencia del resumen y del entregable con los pasos no se midieron (criterio 12).

### 9. Los 61 puentes al nucleo sin declarar: A MEDIAS
- **Evidencia:** AUD-09 M53 (`docs/audits/AUD-09-Recorrido_Completo_2026-09-23.md`) y la ficha
  `puentes-reanclados-sin-tejer` (`docs/PENDIENTES.md`). Reproducido hoy: 112 puentes aprobados, 151 aristas vivas de
  nucleo a mundo, **61 fuera de todo `bridges_aprobados`** (48 a quality, 7 a health_safety, 6 a environmental).
- **Falta:** tejer los puentes aprobados, una guarda que compare el fichero contra las aristas (hoy ninguna lo
  hace) y la ley de ancla en 2 (`scripts/integrar_packs.py` tolera 3).

## PENDIENTES

### 10. Vigencia de contenido legal, normativo, numerico y de enlaces: PENDIENTE
### 11. Jurisdiccion: PENDIENTE
- **La politica existe** ("marco contra pais", agosto 2026), repartida en adjudicaciones: `docs/PENDIENTES.md`
  (ficha `vigencia-del-marco-internacional`, doctrina de la clase), `packs/exportacion/poda/ADJUDICACION_MARCO_VS_PAIS.md`,
  `packs/_core/poda/REGULACION_EEUU_NUCLEO.md`, `packs/_core/poda/_frontera_eeuu.json`, `_reencuadre_clase.json`,
  `_cierre_ftc.json`, `_revive_pais.json`, `dataset/metadata/falsos_positivos_adjudicados.json`. **La clase no es un
  campo del nodo**: se lee en su texto (condicion de pais, formula de localizacion, puntero de vigencia).
- La regla "contratar, nomina y despido como metodo, nunca como norma" **no aparece escrita** en el repo.
- **Medicion en curso** (ver MEDICIONES).

### 12. Coherencia interna de cada nodo: PENDIENTE (medicion en curso)
### 13. Aristas rancias tras las correcciones: PENDIENTE (medicion en curso)
### 14. Titulos y condiciones de activacion contra su contenido: PENDIENTE (medicion en curso, muestra con semilla)
### 15. Fase y dominio de cada nodo: PENDIENTE (medicion en curso, muestra con semilla)
- Hoy, vivos por fase: ejecucion 1.333, planificacion 983, validacion 452, ideacion 401; por dominio: core 1.439,
  quality 692, environmental 265, health_safety 260, franquicias 182, exportacion 131, risk_management 55,
  seguridad_digital 52, entrega 47, compras 46.
### 16. Ortografia y voz de la casa: PENDIENTE
### 17. Mundo 11 contra el catalogo: PENDIENTE
- La puerta semantica de la integracion esta escrita y cableada (`docs/plan/07_ADUANA.md` OP-A-02, codigo
  `scripts/loop/aduana_semantica.py`, llamado desde `scripts/integrar_packs.py`) y pide vector de Voyage para cada
  candidato. El puente (`origin/puente-forja`, `e2fcc698`) se probo en seco con 338 nodos de la forja; hoy la forja
  tiene 459 mas 20 en bandeja.

---

## MEDICIONES (solo lectura, antes de corregir nada)

*Se rellena al cerrar cada medicion. Metodo calibrado: lector por lote con trampas sembradas, verificador ciego de
lo marcado mas una muestra de lo limpio, arbitro en los desacuerdos; todos los agentes en claude-opus-5-5.*

### Vigencia y jurisdiccion (pasada J, 26 sep 2026)
- **Instrumento:** criba lexica de solo lectura (`criba_lexica.py`) que marca candidatos, y lectura con agentes de
  **1.466 nodos**: los 1.224 marcados (catalogo y mundo 11) mas una **muestra ciega de 242 no marcados** (1 de cada
  10, semilla 20260926) para medir lo que la criba deja. 33 lotes, **99 trampas** (pais sin clase, norma o plazo
  datado, enlace o institucion): el lector cazo **97 de 99**, el verificador ciego **98 de 99**; 113 desacuerdos al
  arbitro. Clases segun la politica "marco contra pais".
- **Jurisdiccion, catalogo:** **222 nodos** con contenido propio de un pais: A 10, B 55, C 47 y **SIN CLASE 110**
  (EE.UU. 108, Union Europea 3, Canada 2, Reino Unido 2, Francia 1). Sin clase por mundo: exportacion 34,
  seguridad_digital 27, core 20, franquicias 11, health_safety 10, environmental 6, quality 2. La muestra ciega da
  un 1,2 por ciento de no marcados con pais sin clase: **unos 27 mas** fuera de la criba (estimacion).
  Ejemplos: `international_partner_search` (U.S. Commercial Service), `getting_started_risk_assessment` (CUI del
  gobierno de EE.UU.), `analisis_competencia_franquicias` (FDD), `autorregulacion_seguridad` (HSW Act 1974 del Reino
  Unido), `politica_compras_verdes` (Energy Star).
- **Programas de un gobierno:** 34 (SIN CLASE 21, C 9, B 4). **Cifra de mercado:** 7. **Empleo tratado como norma:** 2
  (`temas_legales_empleo`, empleo at-will; `clasificacion_consultores_empleados`).
- **Vigencia, catalogo:** **313 nodos** dependen de algo que caduca: norma 193, institucion 148, cifra datada 72,
  plazo legal 21, enlace 17, importe de mercado 7. La muestra ciega anade un 2,9 por ciento de no marcados con
  alguna dependencia (unos 63 mas, estimacion).
- **Mundo 11** (459 en la forja y 20 en su bandeja): casi limpio. 2 nodos con pais: `conducir_llamadas_referencia`
  (B, bien) y **`evitar_preguntas_ilegales_entrevista` SIN CLASE** (la lista de preguntas ilegales de EE.UU. impuesta a
  todos, y ademas contratar como norma). 9 con alguna dependencia, 3 con cifra de mercado (salarios en dolares de
  ejemplo).
- **Regresion por fidelidad, confirmada leyendo:** `programas_cooperativos_osha` y `reglas_de_origen_fta_2` quedaron
  **incoherentes** (condicion de solo EE.UU. y a la vez "o el equivalente en tu mercado"); `valuacion_409a` paso de
  nodo-frontera C a reencuadre B; `calculo_de_aranceles_importacion` es un reencuadre B coherente.
- **Cumplimiento de la politica:** **110 nodos vivos** (mas unos 27 estimados) con contenido propio de un pais sin
  ninguna de las tres clases.

### Muestra con semilla: titulos, condiciones, fase y dominio (pasada M, 26 sep 2026)
- **Instrumento:** muestra de **300 nodos vivos**, semilla escrita **20260927**, 6 lotes, 12 trampas (cazadas 12 de 12
  por el lector y 12 de 12 por el verificador); el verificador ciego releyo los 300; 8 desacuerdos al arbitro.
- **Tasas de error (IC 95 por ciento):** titulo **0,0** (0,0 a 1,3); condiciones **0,3** (0,1 a 1,9); dominio **0,7**
  (0,2 a 2,4); **fase 12,3** (9,1 a 16,5), unos 390 nodos del catalogo (290 a 520).
- **El error de fase es de dos fases:** de los marcados **validacion, el 46 por ciento** esta mal (26 de 56; casi
  todos son ejecucion o planificacion), y de ideacion el 24 por ciento (7 de 29); planificacion 1 por ciento y
  ejecucion 3 por ciento. Estimacion: unos 210 nodos mal marcados como validacion y unos 95 como ideacion.

### Aristas rancias tras las correcciones (pasada R, 26 sep 2026)
- **Instrumento:** las **2.212 aristas vivas** que tocan a los 354 nodos corregidos, cada una juzgada con el texto de
  hoy y las correcciones a la vista; 15 lotes, 30 aristas falsas de trampa (cazadas 29 de 30 y 29 de 30); 31
  desacuerdos al arbitro.
- **Resultado:** **1 arista rancia por la correccion** (`comunicacion_a_toda_la_empresa` hacia
  `confianza_mutua_fundadores`); **149 rancias de antes** (6,7 por ciento), en 139 pares distintos que tocan a 93
  nodos, que no vienen de la campania sino del origen (por ejemplo `identificacion_de_riesgos` hacia
  `distribucion_weibull`). Si la tasa se sostuviera en todo el grafo serian unas 660 de 9.914 (solo indicio: la
  muestra no es aleatoria).
- **Determinista:** **54 referencias de un vivo a un deprecado** en todo el catalogo (27 pares, AUD-09 B15).

### Coherencia interna (pasada K, 26 sep 2026)
- **Instrumento:** los **3.169 nodos vivos**, 46 lotes, **92 trampas** (un paso contra el resumen, un entregable ajeno):
  cazadas **92 de 92** por el lector y **92 de 92** por el verificador ciego; 16 desacuerdos al arbitro; muestra ciega de
  551 limpios, 4 cambiaron tras verificar.
- **Resultado:** **25 nodos incoherentes** (0,8 por ciento; con la muestra, unos 19 mas estimados): core 16, quality 4,
  health_safety 2, franquicias 2, compras 1. Por par de campos: resumen contra pasos 13, pasos contra pasos 5, pasos
  contra entregable 5, condiciones contra contenido 4, titulo contra pasos 3, resumen contra entregable 3. **6 de los
  25 son nodos corregidos por la campania de fidelidad** (a revisar como posible efecto de la correccion).
  Ejemplos: `test_rico_vs_rey` (el titulo pide diagnosticar tu motivacion; el resumen es la evaluacion que hace un
  inversor de otro), `channels_hypothesis_web_mobile` (un paso manda un solo canal y el siguiente repartir entre
  varios), `framework_caracteristicas_ventajas_beneficios` (el paso 2 prohibe lo que el paso 6 manda).

### Regresion de la campania de fidelidad sobre la politica de pais (medida determinista, 26 sep 2026)
- De las 487 correcciones, **17 tocaron 13 nodos con clase de pais** (por las listas de la politica o por su
  condicion de pais antes de la campania). **Ninguna quito** un reencuadre, una condicion de pais ni una mencion de pais.
- **4 anadieron la formula B** ("o la autoridad equivalente en tu mercado"): **2 en nodos-frontera de clase C**
  (`programas_cooperativos_osha` en `fidelidad-t3-44`, `valuacion_409a` en `fidelidad-t4-035`), que es una
  regresion (un nodo que solo aplica si operas en EE.UU. ahora ofrece un equivalente local); y 2 en nodos de
  exportacion de la lista de vigencia (`calculo_de_aranceles_importacion` `fidelidad-t4-007`,
  `reglas_de_origen_fta_2` `fidelidad-t4-011`), a leer. Se confirman leyendo en la pasada de jurisdiccion.

---

## PROPUESTA DE TRATAMIENTO (a la espera del visto del fundador; NADA se ha corregido)

| punto | tamano medido | propuesta |
|---|---|---|
| Jurisdiccion | 110 nodos sin clase (mas unos 27), 108 de EE.UU.; 34 programas de gobierno; 2 de empleo como norma | **Marcar, no reescribir:** una lista curada `dataset/metadata/jurisdiccion.json` (nodo, pais, clase A, B o C, condicion) y que la app lo diga en la tarjeta ("este nodo trata normas de EE.UU."). Reescribir solo lo incoherente. Unificar la letra de la politica en un solo documento, con la regla de empleo que hoy no esta escrita, para que el fundador la ratifique. Una guarda que falle si un nodo con contenido de pais no tiene clase. |
| Regresion por fidelidad | 2 nodos-frontera con la formula B (incoherentes); 1 que paso de C a B | Devolver a los 2 su clase C quitando la formula B, por el ciclo de correcciones declaradas; `valuacion_409a` lo decide el fundador (C o B). |
| Vigencia | 313 nodos (mas unos 63): norma 193, institucion 148, cifra datada 72, plazo legal 21, enlace 17, importe de mercado 7 | **Ficha de vigencia** por nodo (`dataset/metadata/vigencia.json`: tipo, fragmento, fecha de verificacion, revisar cada), y que la app muestre "verificado a fecha de". Los 17 enlaces, comprobados por un instrumento; las 72 cifras datadas, con su "a fecha de" o generalizadas; los 7 importes de mercado salen (regla de la cifra). |
| Coherencia interna | 25 nodos (mas unos 19) | Corregir contra el libro por el ciclo de la campania (lector, verificador, cita literal), empezando por los 6 corregidos por fidelidad. |
| Aristas rancias | 1 por correccion; 149 de antes (139 pares, 93 nodos); 54 referencias a deprecados | Quitar la 1; recablear las 54 al superviviente con un instrumento determinista y una guarda en Gate 0; las 149 abren la **pasada de aristas por lectura** del criterio 6 sobre las 9.914 (tasa medida de 6,7 por ciento en esta muestra). |
| Fase | 12,3 por ciento en la muestra (unos 390 nodos); validacion 46 por ciento y ideacion 24 | Pasada de fase con agentes, trampas y verificador sobre los 853 nodos marcados validacion o ideacion, y correccion declarada del campo `fase_proyecto` (mirar antes que la brujula y la brecha lo usan). |
| Titulos, condiciones y dominio | 0,0, 0,3 y 0,7 por ciento | Sin campania: corregir los 3 casos hallados (1 condicion, 2 dominios). |
| Mundo 11 | 1 nodo sin clase y con empleo como norma (`evitar_preguntas_ilegales_entrevista`); 3 cifras de mercado | Arreglarlos en la forja antes de la integracion (clase C o B, y contratar como metodo); la cifra de mercado sale. |
