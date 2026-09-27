# SANEAMIENTO DEL DATASET: LA LISTA COMPLETA DE VERIFICACION (documento vivo)

> **EL DATASET ESTA SANEADO PARA EL CLIENTE.**
>
> Nivel 1 cerrado por la decision del fundador del 27 sep 2026 ("dos niveles de saneamiento"): todos sus criterios
> verificados por su instrumento, con Gate 0 (alcanzabilidad 100 por ciento), el motor, vitest y tsc en verde. La unica
> pieza del nivel 1 que no depende de este trabajo es el criterio 7 (252 vectores y 66 preguntas de texto viejo, ahora
> 349 nodos), que por la misma decision espera a que el fundador diga "clave cargada": no toca ningun texto que vea el
> cliente, solo la busqueda semantica.
>
> **Nivel 2, mejora continua (no bloquea esta declaracion)**, cada uno con su ficha y su fecha en `docs/PENDIENTES.md`,
> seccion 0c:
> - `n2-aristas-por-lectura`: las aristas que ninguna pasada leyo todavia y las 477 que faltan;
> - `n2-vigencia-completa`: la campania completa de vigencia de los 305 nodos;
> - `n2-voz-de-la-casa`: la voz de la casa en los textos que ve el cliente;
> - `n2-muestra-anadidos-practicos`: una muestra de los anadidos practicos de resumenes y entregables, para decidir si
>   merecen campania.

*Mandato del fundador (26 sep 2026): **el dataset no se declara saneado hasta cumplir esta lista completa.**
Cada criterio lleva su instrumento, su estado (VERIFICADO, A MEDIAS, PENDIENTE) y su evidencia (commit, informe,
cifra). Las cifras sin fuente citada se midieron el 26 sep 2026 sobre `main` en `264fd82e`, solo lectura, con
scripts que no escriben. **Donde la evidencia no alcanza el estado que el mandato le da, la fila lo dice.***

Universo: **3.853** nodos en `dataset/nodos/`, **3.169 vivos** y **684 deprecados**. El mundo 11 vive fuera del
catalogo: **459 nodos** en la forja (`forja-nodos/dataset/nodos.jsonl`) y **20** en su bandeja (Marquet), sin
integrar todavia.

---

## ESTADO DE UN VISTAZO

| # | criterio | estado (cierre del nivel 1) |
|---|---|---|
| 1 | Duplicados y fusiones | VERIFICADO |
| 2 | Pasos contra su libro | VERIFICADO |
| 3 | Etiquetas del riel contra su nodo, y su vigencia en las traducciones | VERIFICADO |
| 4 | Identificadores | VERIFICADO |
| 5 | Fuentes | VERIFICADO (`fuentes_internas` completas; ningun libro ni autor llega al cliente) |
| 6 | Aristas | VERIFICADO PARA EL CLIENTE: ningun nodo del nucleo sin camino por el nucleo (eran 45); alcanzabilidad 100 por ciento; los 240 sin sucesor, cerrados por diseno. Nivel 2: la lectura de las aristas restantes y las 477 que faltan |
| 7 | Indice semantico | ESPERA "clave cargada": 349 nodos a re-embeber y 66 preguntas a regenerar |
| 8 | Resumenes y entregables | VERIFICADO PARA EL CLIENTE (contrarios y anadidos de cifra, plazo o norma: cero). Nivel 2: la muestra de anadidos practicos |
| 9 | Los 61 puentes al nucleo sin declarar | VERIFICADO (157 puentes en 9 mundos, todos tejidos, ley del ancla en 2, guarda) |
| 10 | Vigencia | VERIFICADO PARA EL CLIENTE: aviso sin libro en 305 nodos, 21 plazos verificados, enlaces rotos corregidos o retirados. Nivel 2: la campania completa |
| 11 | Jurisdiccion | VERIFICADO |
| 12 | Coherencia interna de cada nodo | VERIFICADO (segundo lector ciego sobre los 2.592 que leyo uno solo; los 4 hallados, corregidos contra su libro) |
| 13 | Aristas rancias tras las correcciones | VERIFICADO |
| 14 | Titulos y condiciones de activacion | VERIFICADO (condiciones leidas en los 3.169, frontera de pais primero; 114 corregidas) |
| 15 | Fase y dominio de cada nodo | VERIFICADO (fase leida en los 3.169; dominio leido en los 3.169 y los 35 que salian del nucleo decididos nodo por nodo) |
| 16 | Ortografia y voz de la casa | ORTOGRAFIA VERIFICADA (1.036 correcciones). Nivel 2: la voz de la casa |
| 17 | Mundo 11 contra el catalogo | En su integracion: la forja cerro y fundio (tag `forja-mundo-11`, 471 nodos en el pack) |
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

### 9. Los 61 puentes al nucleo sin declarar: VERIFICADO (ver TANDA 2 y las decisiones del 27 sep)
- **Evidencia:** AUD-09 M53 (`docs/audits/AUD-09-Recorrido_Completo_2026-09-23.md`) y la ficha
  `puentes-reanclados-sin-tejer` (`docs/PENDIENTES.md`). Reproducido hoy: 112 puentes aprobados, 151 aristas vivas de
  nucleo a mundo, **61 fuera de todo `bridges_aprobados`** (48 a quality, 7 a health_safety, 6 a environmental).
- **Falta:** tejer los puentes aprobados, una guarda que compare el fichero contra las aristas (hoy ninguna lo
  hace) y la ley de ancla en 2 (`scripts/integrar_packs.py` tolera 3).

## PENDIENTES

### 10. Vigencia de contenido legal, normativo, numerico y de enlaces: A MEDIAS (ver TANDA 1)
### 11. Jurisdiccion: VERIFICADO (ver TANDA 1)
- **La politica existe** ("marco contra pais", agosto 2026), repartida en adjudicaciones: `docs/PENDIENTES.md`
  (ficha `vigencia-del-marco-internacional`, doctrina de la clase), `packs/exportacion/poda/ADJUDICACION_MARCO_VS_PAIS.md`,
  `packs/_core/poda/REGULACION_EEUU_NUCLEO.md`, `packs/_core/poda/_frontera_eeuu.json`, `_reencuadre_clase.json`,
  `_cierre_ftc.json`, `_revive_pais.json`, `dataset/metadata/falsos_positivos_adjudicados.json`. **La clase no es un
  campo del nodo**: se lee en su texto (condicion de pais, formula de localizacion, puntero de vigencia).
- La regla "contratar, nomina y despido como metodo, nunca como norma" **no aparece escrita** en el repo.
- **Medicion en curso** (ver MEDICIONES).

### 12. Coherencia interna de cada nodo: A MEDIAS (ver pasada K y TANDA 1)
### 13. Aristas rancias tras las correcciones: VERIFICADO (ver TANDA 2)
### 14. Titulos y condiciones de activacion contra su contenido: A MEDIAS (ver pasada M y TANDA 2)
### 15. Fase y dominio de cada nodo: A MEDIAS (ver TANDA 2; las cifras de abajo son de antes)
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

*Instrumentos en `docs/saneamiento/instrumentos/` y resultados por nodo, con las claves de las trampas, en
`docs/saneamiento/resultados/` (J vigencia y jurisdiccion, K coherencia, M muestra, R aristas). Metodo calibrado: lector por lote con trampas sembradas, verificador ciego de
lo marcado mas una muestra de lo limpio, arbitro en los desacuerdos; todos los agentes en claude-opus-5-5.*

### Vigencia y jurisdiccion (pasada J, 26 sep 2026)
- **Instrumento:** criba lexica de solo lectura (`docs/saneamiento/instrumentos/criba_lexica.py`) que marca candidatos, y lectura con agentes de
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

---

## TANDA 1 (decision del fundador del 26 sep 2026): LO QUE PUEDE DANAR A UN CLIENTE. CERRADA

Todo por correccion declarada en el propio nodo (`scripts/fidelidad/aplicar_correcciones.py`, cada una con su cita),
Gate 0, `engine/run_all_tests.py` y vitest en verde. Tandas en `docs/saneamiento/tandas/`.

1. **Politica unica:** `docs/POLITICA_MARCO_PAIS.md`, las tres clases, la regla de la cifra, la regla del empleo (que no
   estaba escrita) y la reversion de agosto (programas de gobierno como clase C), ratificada por el fundador.
2. **Regresiones:** `saneamiento-t1-regresiones` (5 correcciones en 3 nodos): `programas_cooperativos_osha` y
   `reglas_de_origen_fta_2` vuelven a clase C (sin la formula B); `valuacion_409a` vuelve a clase C con la condicion "si tu
   empresa esta constituida en EE.UU. (por ejemplo, en Delaware para levantar capital alli)".
3. **Jurisdiccion:** `dataset/metadata/jurisdiccion.json`, **237 nodos con clase** (A 12, B 121, C 104; EE.UU. casi todos) y
   21 adjudicados sin pais con su motivo. Salen de la pasada J (clase medida) y de la pasada JC (clase declarada de los 110
   sin clase y de los **21 que la criba no vio**, encontrados entre 678 candidatos legales; trampas 32 de 32 y 32 de 32).
   **Solo se reescribio lo incoherente** en sentido estricto (clase C que prometia "el equivalente en tu mercado" o clase B
   atada a un solo pais): `saneamiento-t1-jurisdiccion`, 9 correcciones en 5 nodos. La tarjeta de la app lo dice en los once
   idiomas (`web/lib/engine/avisos.ts`, `web/lib/i18n/mensajes/avisoNodo.ts`, `app/ui/TarjetaPregunta.tsx`): B "Ejemplo de
   Estados Unidos: busca el equivalente en tu pais", C "Aplica si operas o vendes en Estados Unidos". **Guarda:**
   `engine/test_jurisdiccion.py`, ningun nodo con marca de pais sin clase (con caso negativo), y `web/lib/engine/avisos.test.ts`.
4. **Vigencia, primer paso:** `dataset/metadata/vigencia.json`, **305 nodos** con norma, plazo legal, cifra con fecha o
   institucion llevan en la tarjeta "Esta informacion puede haber cambiado desde [ano]: verifica la norma vigente en tu
   pais" (sin el libro: correccion urgente del 26 sep, abajo). El ano de cada libro se
   leyo en su propio fichero, con la linea que lo prueba y su seguridad (de 54 libros: 17 ALTA, 27 MEDIA, 10 BAJA; si no hay
   ano, el aviso lo omite). **Comprobador de enlaces:** `scripts/saneamiento/comprobar_enlaces.py` y su informe
   `docs/saneamiento/ENLACES.md` (24 enlaces: 14 vivos, 2 redirigen, 4 rotos, 4 no responden). **Los 21 plazos legales,
   verificados HOY contra la fuente oficial** con cita (37 plazos: 16 vigentes, 18 imprecisos, 1 desactualizado, 2 que no
   son plazo legal); corregidos por `saneamiento-t1-plazos`, 17 correcciones en 14 nodos (por ejemplo, las garantias GSM-102
   del USDA pasan de "hasta 3 anos" a 24 meses; las auditorias de seguimiento, de "cada seis meses" a "al menos una vez al
   ano"). El resto de la vigencia queda como campania posterior en `docs/PENDIENTES.md`.
5. **Coherencia:** los 25 contra su libro, empezando por los 6 corregidos por la fidelidad: lector con el libro, verificador
   ciego y arbitro, cada cita comprobada literal; `saneamiento-t1-coherencia`, **52 correcciones en los 25 nodos**. El titulo
   de `test_rico_vs_rey` no se toca (doctrina: el titulo vive con el libro y no se muestra); su etiqueta de cara, que tambien
   decia lo contrario, pasa a "Evalua si el Fundador Busca Control" (lista de fidelidad de etiquetas, en los once idiomas).
6. **Mundo 11:** el nodo sin clase (`evitar_preguntas_ilegales_entrevista`, contratar como metodo) y las 3 cifras de mercado
   se arreglan EN LA FORJA por su propio proceso antes de integrar: anotado en `docs/PENDIENTES.md`.

**Textos derivados:** ninguna pregunta en cache contenia el texto corregido (no se retiro ninguna); 24 nodos van a
re-embeber y 14 preguntas a regenerar en la proxima sesion con credencial (`docs/fidelidad/credencial/`, ahora 75 y 66).
**Aviso con titulo de libro:** salio a produccion como "Segun [libro], [ano]" y el fundador lo corrigio el mismo dia; ver la
seccion siguiente.

---

## CORRECCION URGENTE DEL FUNDADOR (26 sep 2026): NINGUN LIBRO NI AUTOR LLEGA AL CLIENTE. CERRADA

**Regla:** el cliente nunca ve el titulo de un libro ni un autor citado como fuente, ni en pantalla, ni en un documento, ni
en un correo, ni en una respuesta de la IA. Las fuentes viven solo en metadatos internos. Regla escrita en `AGENTS.md`
("Ningun libro ni autor llega al cliente; las fuentes son metadato interno"), que sustituye a "la etiqueta enamora, el
titulo respalda": ya no hay "detalle del nodo junto a su fuente" (esa vista nunca existio y el tooltip repetia la etiqueta).

1. **Hotfix del aviso** (9349df2c, en vivo): "Esta informacion puede haber cambiado desde [ano]: verifica la norma vigente
   en tu pais", en los once idiomas, sin libro. La prueba que lo exige estuvo en rojo primero (3.355 avisos nombraban un
   libro).
2. **El titulo no se pinta en ninguna parte:** la opcion de emergencia (error de la IA) y el plan sin IA nombraban el nodo
   por su `titulo_concepto`; ahora por su etiqueta. **Guarda:** `engine/test_fuentes_de_cara.py` barre 66.848 textos de
   cara al cliente (catalogos de la interfaz y de los correos en los once idiomas, etiquetas en diez idiomas, preguntas en
   cache, instrucciones de la IA, el codigo de la web y el texto de cada nodo vivo) contra la lista canonica de titulos
   (`dataset/metadata/fuentes_canonicas.json`, 67 formas de fuente, 53 libros). Un titulo que tambien es el nombre de un
   concepto del oficio (green to gold, quality is free, co-inteligencia, SPIN Selling) solo cuenta en su forma inequivoca.
3. **Las 252 menciones de autor en 241 nodos, clasificadas** (lector con 2 trampas por lote, 16 de 16; verificador ciego,
   10 de 11; arbitro en 25 desacuerdos). Menciones: **CITA 215** (sale), **CONCEPTO 61** y **ORGANIZACION 61** (se quedan).
   Por texto: **185 con alguna cita**, 60 solo con conceptos u organizaciones, 7 sin mencion real (falsos positivos de la
   busqueda). La cita salio por **correccion declarada** (veredicto nuevo ATRIBUCION de `aplicar_correcciones.py`, que
   declara la regla y los fragmentos que salen): `saneamiento-atribuciones`, **183 correcciones en 182 nodos** (178
   resumenes, 4 pasos y 1 resumen que citaba "Assembling Tomorrow", hallado por la guarda de titulos). Cada texto sin la
   cita se reviso contra el anterior (misma informacion, sin endurecer una opinion en un hecho): 149 bien a la primera, 33
   reescritos y confirmados por un segundo revisor ciego, 1 corregido por el confirmador. **3 titulos** citan a su autor
   ("(Juran)", "(Deming)", "Crosby"): no se tocan por doctrina y no se muestran. Ninguna pregunta en cache nombra un autor
   o un libro; los 176 nodos con resumen nuevo van a re-embeber (`docs/fidelidad/credencial/`, ahora 251).
4. **La IA:** solo `SYSTEM_PLAN` prohibia autores ("sin autores"). Ahora TODA llamada lleva el bloque fijo
   `REGLA_SIN_FUENTES` (`web/lib/reglaSinFuentes.ts`) despues del prompt cacheado (el cache no cambia). **Guarda:**
   `web/lib/reglaSinFuentes.test.ts` (la regla en toda llamada, y ninguna llamada arma su sistema por otro camino).

## DECISIONES DEL FUNDADOR (27 sep 2026): FUENTES COMPLETAS Y NADA INTERNO EN EL NAVEGADOR. CERRADA

1. y 4. **Fuentes completas por nodo:** `scripts/fuentes_internas.py` calcula, para cada nodo vivo, TODOS los libros de los
   que viene: el suyo y los de todo lo que absorbio por cualquier fusion y en cadena, sin limite (ids_alias y
   merged_originals de los nodos, merge_decisions, los mapas de alias de las capas y las referencias fantasma; la fuente de
   cada absorbido sale de su fichero, de su original, de la procedencia de su absorbedor o, para 38 que solo quedaban en el
   historial de git, de `dataset/metadata/fuentes_historicas.json`). Lo guarda en el campo interno `fuentes_internas` y en
   `docs/internos/INVENTARIO_FUENTES.md`. `fuente` no se toca. Resultado: 3.169 nodos vivos, **54 con mas de un libro**
   (hasta 4), 722 absorbedores de 1.165 ids; 333 ids absorbidos no tienen libro en ningun sitio (referencias que nunca
   fueron nodo) y se listan aparte. **Guarda:** `engine/test_fuentes_internas.py` (al dia, empieza por la fuente propia,
   cada libro en la lista canonica; caso negativo con una cadena de cuatro fusiones por cuatro vias).
2. **Nada interno llega al navegador.** Medido en rojo primero (`web/lib/assets/sinInternos.test.ts`): la copia del grafo
   en web/ llevaba `fuente`, `correcciones` con sus citas y `merged_originals` (8.336 claves internas); vigencia.json llevaba
   los libros con su fichero y su frase; y las instrucciones de la IA (prompts.json) iban en el paquete del navegador por
   DetalleActividad, estimacion.ts y prompts.ts. Arreglado por el ciclo de siempre: `scripts/sync_assets_web.py` escribe la
   VISTA WEB (sin fuente, fuentes_internas, correcciones ni merged_originals; vigencia solo con el ano; jurisdiccion solo con
   pais y clase) y `rangoDeBanda` vive en un modulo puro. El chequeo de gemelos del Gate 0 compara todo menos esas claves y
   falla si una aparece en la web. **Comprobado en un build de produccion:** los 44 ficheros que descarga el navegador no
   llevan ninguna clave interna, instruccion de la IA, texto de nodo ni titulo de libro.
3. **Repositorios a privado:** ninguna sesion en la nube esta a mitad de un trabajo (la unica en la nube, "Proyecto idiomas
   My Idea", esta ociosa).

---

## TANDA 2 (decision del fundador del 26 sep 2026): ARISTAS, FASE Y PUENTES. CERRADA

Todo por correccion declarada en el propio nodo, Gate 0 (alcanzabilidad 100 por ciento, 3.169 de 3.169),
`engine/run_all_tests.py` (32 de 32), vitest (2.017) y tsc en verde. Tandas en `docs/saneamiento/tandas/`, instrumentos en
`docs/saneamiento/instrumentos/`, resultados por nodo en `docs/saneamiento/resultados/` (E, F, P). Las aristas se corrigen
con `scripts/saneamiento/aplicar_aristas.py` (nuevo: QUITAR, TEJER o RECABLEAR, en las dos vistas de la arista y declarado
en los dos nodos); fase, dominio y coherencia con los veredictos nuevos FASE, DOMINIO y COHERENCIA de
`aplicar_correcciones.py`, que declaran su instrumento y su evidencia.

7. **Aristas** (`saneamiento-t2-aristas`, 190 operaciones en 241 nodos): salen la arista rancia por la correccion y las
   rancias de antes de la pasada R (135 pares sin disputa; de los 4 pares juzgados vigentes desde un extremo y rancios
   desde el otro, un arbitro dejo 3 y quito 1: 136 en total); las **54 referencias a deprecados** pasan a su
   superviviente. **Ningun nodo se queda sin camino:** 18 de esas aristas eran la unica entrada de 27 nodos; la pasada E
   (dos lectores ciegos entre 8 candidatos semanticos alcanzables, arbitro en 1) dio a cada uno un predecesor correcto
   (`saneamiento-t2-entradas`; uno sobre una lista ampliada de 20, y uno rehecho porque formaba un par de ida y vuelta).
8. **Fase** (`saneamiento-t2-fase`): pasada F sobre los **853 nodos** marcados validacion o ideacion, con la vara
   calibrada de la pasada M; 29 lotes, trampas 56 de 58 (lector) y 32 de 34 (verificador ciego), 41 desacuerdos al
   arbitro. **326 con la fase mal (38 por ciento)**, todas confirmadas por dos lectores o por el arbitro: validacion a
   ejecucion 136, ideacion a planificacion 72, validacion a planificacion 63, ideacion a ejecucion 48, y 7 entre ideacion
   y validacion. Hoy, vivos por fase: ejecucion 1.517, planificacion 1.118, ideacion 282, validacion 252. Las 20 puertas
   siguen 5 por fase (la unica semilla corregida, `decision_fundador_solo_vs_equipo`, ya estaba curada entre las de
   planificacion). Las 13 semillas de mundo con la fase corregida se alinearon en `packs_entry_seeds.json`, con prueba
   (`semillasDePack.test.ts`). Los 2 fallos de trampa: una trampa de fase bien puesta que los dos lectores marcaron
   (`evitar_uso_complacencia`, planificacion, fuera del universo) y una de fase mal que el lector no vio.
9. **Puentes** (`saneamiento-t2-puentes`, 71 operaciones; ficheros `packs/*/metadata/bridges_aprobados.json`):
   - **ley del ancla en 2** (`integrar_packs.py` toleraba 3): `reglas_gestion_riesgo_gambling` pierde su tercer puente;
   - **21 puentes aprobados tejidos** y 16 aristas viejas de mundo a mundo que el reanclaje reemplazaba, retiradas;
   - **7 aprobados que la pasada R juzgo rancios** (por ejemplo `sesgo_optimismo_fundador` hacia
     `prospecto_emprendedor_flaming`) pasan a `rechazados` con el motivo de R, en vez de volver a tejerse;
   - **las 61 aristas del nucleo a un mundo sin declarar**, leidas en la pasada P (lector con trampas, verificador ciego y
     arbitro; trampas 5 de 6 y 5 de 6): **21 PUENTE** se declaran en su fichero (con su score y su lectura), **40
     RETIRAR** salen (6 ya las habia quitado la pasada R);
   - **guarda** `engine/test_puentes_tejidos.py`: en cada mundo, aprobados igual a aristas vivas del nucleo al mundo, y
     ley del ancla; en rojo sobre main antes de la tanda (84 fallos), en verde despues (125 puentes en 9 mundos).
   - **3 casos de la muestra M:** `manufactura_celular` pasa de environmental a quality; las 2 condiciones de
     `regalos_estrategicos_personalizados` que contradecian el contenido se reescriben desde sus pasos.

**Para el fundador:**
- **Retenido (decidido el 27 sep: pasa a entrega, ver abajo):** `colaboracion_transporte_ctm` (la muestra M lo ve de entrega, no del nucleo). No se movio: es ancla de un
  puente aprobado a quality, 4 nodos del nucleo entran por el, y sacarlo del nucleo lo cierra tras el mundo de entrega.
  Es decision de producto: moverlo (y declarar sus puentes) o dejarlo en el nucleo.
- **Aviso:** el puente aprobado `gestion_de_conflictos_cofundadores` hacia `enfoque_situacional_vs_personal`
  (health_safety) fue la trampa que los dos lectores de la pasada P juzgaron RETIRAR; se queda como esta aprobado, pero la
  lectura dice que es debil.

**Textos derivados:** las 2 condiciones nuevas entran al vector: `regalos_estrategicos_personalizados` se suma a
`nodos_a_reembeber.txt` (252). Fase, dominio y aristas no cambian vectores ni preguntas en cache.

---

## DECISIONES DEL FUNDADOR (27 sep 2026, cierre de la tanda 2). CERRADA

1. **`colaboracion_transporte_ctm` pasa a entrega** (correccion declarada DOMINIO, `saneamiento-d27-dominio`). Pasada C
   (`docs/saneamiento/resultados/C`, dos lectores ciegos, acuerdo en los 6 bloques, sin arbitro):
   - su puente a calidad se reancla en `colaboracion_cadena_suministro` (ley del ancla intacta); la arista vieja de
     entrega a calidad sale;
   - `collaboration_enablers`, el unico nodo del nucleo que solo entraba por el, recibe como predecesor
     `coordinacion_colaboracion_cadena_suministro`;
   - de las 4 aristas del nucleo que le llegaban, 2 son puente a entrega y se declaran en su fichero
     (`collaboration_roadblocks`, `programacion_entregas_delivery_scheduling`) y 2 salen
     (`definicion_alineacion_cadena_suministro`, `outsourcing_cadena_suministro`).
2. **El puente `gestion_de_conflictos_cofundadores` hacia `enfoque_situacional_vs_personal` se rechaza** y su arista
   sale; el nodo conserva sus 2 entradas de su propio mundo (`ciclo_de_culpa_2`, `errores_como_consecuencia`).
3. Tanda `saneamiento-d27-aristas` (6 operaciones en 9 nodos). **Alcanzabilidad 100 por ciento** (3.169 de 3.169) en
   Gate 0; `collaboration_enablers` se alcanza andando solo por el nucleo. Gate 0, motor (32 de 32), vitest (2.017) y
   tsc en verde; 126 puentes aprobados en 9 mundos, todos tejidos.

## ESTADO FINAL DE LA TANDA 2: LO QUE FALTABA (superado: ver NIVEL 1 al final y la declaracion al principio)

Verificados: 1, 2, 3, 4, 5, 9, 11 y 13. **No se declara saneado todavia**: quedan nueve criterios, en este orden de
peso para el cliente.

| # | lo que falta | como se cierra |
|---|---|---|
| 15 | Fase de los 2.635 nodos de planificacion y ejecucion (unos 60 mal, por la muestra) y dominio en todo el catalogo (unos 20) | Pasada F con la misma vara sobre planificacion y ejecucion, y una pasada de dominio; correccion declarada |
| 14 | Condiciones de activacion en todo el catalogo (unas 10 mal, por la muestra) | Pasada completa de titulos y condiciones contra el contenido |
| 12 | Residuo de coherencia interna (unos 19 sin localizar) | Segunda pasada K sobre los nodos que la primera dio por coherentes |
| 8 | Anadidos practicos de resumenes y entregables sin medir | Pasada de anadidos contra el libro |
| 6 | Unas 4.900 aristas sin leer una a una; 477 que faltan; 45 nodos del nucleo inalcanzables solo por el nucleo; 240 sin sucesor | Pasada de aristas por lectura (tasa medida en R: 6,7 por ciento rancias); tejer las que faltan |
| 10 | Vigencia: fichas con fecha de verificacion, las normas, cifras e instituciones de los 305 nodos contra su fuente oficial, unos 63 sin marcar, 10 anos de libro BAJA, 4 enlaces rotos | Campania de vigencia |
| 16 | Ortografia y voz de la casa | Pasada de estilo |
| 7 | 252 vectores de texto viejo y 66 preguntas a regenerar | Sesion con credencial, cuando el fundador diga "clave cargada" |
| 17 | Mundo 11 contra el catalogo | En la integracion del mundo 11, por la aduana semantica, con sus libros en la lista canonica y sus fuentes internas |

---

## NIVEL 1 "SANEADO PARA EL CLIENTE" (decision del fundador del 27 sep 2026). CERRADO

Todo por correccion declarada en el propio nodo, instrumento y resultados por nodo en `docs/saneamiento/`; Gate 0
(alcanzabilidad 100 por ciento, 3.169 de 3.169), motor (32 de 32), vitest (2.017) y tsc en verde.

- **15. Fase y dominio (pasada Q, 3.169 nodos, vara calibrada de M, lector con trampas, verificador ciego y arbitro;
  trampas 206 de 212 y 205 de 208).** 65 fases corregidas en planificacion y ejecucion (validacion e ideacion ya las
  leyo la F). 50 dominios mal: 15 entre mundos o de vuelta al nucleo, aplicados; **los 35 que sacaban un nodo del
  nucleo, decididos NODO POR NODO** (decision del fundador) con la prueba "lo necesita cualquier emprendedor aunque nunca
  active ese mundo?" (pasada D, dos lectores ciegos y arbitro, trampas 4 de 4 y 4 de 4):
  - **1 se queda en el nucleo**, con su motivo: `criterios_seleccion_proveedores` ("casi cualquier emprendedor tiene que
    elegir proveedores, un gestor contable, un hosting, un fabricante o una agencia, y comparar con criterios ponderados
    es la forma general de hacerlo; el mundo de compras lo profundiza");
  - **34 se mueven a su mundo** (19 a entrega, 10 a compras, 2 a riesgos, 2 a calidad, 1 a seguridad digital), como
    `colaboracion_transporte_ctm` (pasada MV): de las 58 aristas del nucleo al mundo, 40 son puente (declaradas dentro de
    la ley del ancla) y 18 salen; 7 puentes que anclaban en un nodo movido a su mismo mundo quedan dentro del mundo; 7 se
    reanclan en el nucleo por lectura; 13 nodos del nucleo sin camino reciben un predecesor del nucleo y 5 nodos sin
    entrada, uno de su mismo mundo (pasada R2). Resultado: 157 puentes en 9 mundos, 0 nodos del nucleo sin camino por el
    nucleo, alcanzabilidad 100 por ciento. Hoy, vivos por mundo: core 1.410, quality 686, environmental 263,
    health_safety 258, franquicias 181, exportacion 130, entrega 67, risk_management 66, compras 55, seguridad_digital 53.
- **14. Condiciones de activacion (pasada Q):** 114 condiciones mal en 105 nodos (la muestra estimaba unas 10),
  reescritas desde el propio contenido del nodo (veredicto COHERENCIA); en los nodos-frontera de pais, la clase C con su
  condicion de operar alli y la B sin exigirla.
- **12. Coherencia (pasada K2):** segundo lector ciego sobre los 2.592 nodos que en K leyo uno solo, trampas 162 de 162
  y 162 de 162. **4 incoherentes** (se estimaban unos 19), corregidos contra su libro por dos lectores ciegos con el libro
  y un arbitro con cita literal: 10 correcciones en los 4 nodos.
- **6. Aristas:** los 45 nodos del nucleo inalcanzables andando solo por el nucleo, por 23 raices que recibieron un
  predecesor del nucleo (pasada N); hoy 0. **Los 240 nodos sin sucesor se CIERRAN como resueltos por diseno** (decision
  del fundador del 27 sep 2026): el motor les da salida, porque al llegar a un nodo sin sucesor ofrecible el recorrido
  pasa a `listo_para_plan`.
- **10. Enlaces rotos:** de los 8 que fallaban, revisados a mano, 4 no eran enlaces rotos (Half.com y `site:dominio.com`
  son ejemplo y marcador; NIST responde; USDA FAS solo rechaza a los robots) y 4 se corrigieron o retiraron
  (`saneamiento-n1-enlaces`, veredicto VIGENCIA).
- **16. Ortografia (pasada O):** 21.649 textos del dataset que ve el cliente (etiquetas, pasos, entregables) y las 3.519
  preguntas en cache; trampas plantadas 224 de 224; el segundo lector ciego en 1 de cada 5 lotes hallo 3 faltas que el
  primero no vio sobre 227 (1,3 por ciento). **1.036 correcciones**: 941 en pasos y entregables (veredicto ORTOGRAFIA),
  87 preguntas y 8 etiquetas (lista `etiquetas_de_cara_v1_ortografia.json`, con sus traducciones reselladas en los diez
  idiomas).
- **7.** Espera "clave cargada": 349 nodos a re-embeber (`docs/fidelidad/credencial/nodos_a_reembeber.txt`) y 66
  preguntas a regenerar.

