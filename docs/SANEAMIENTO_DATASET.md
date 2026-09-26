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
| 10 | Vigencia de contenido legal, normativo, numerico y de enlaces | PENDIENTE (medicion en curso) |
| 11 | Jurisdiccion (nodos propios de un pais) | PENDIENTE (medicion en curso) |
| 12 | Coherencia interna de cada nodo | PENDIENTE (medicion en curso) |
| 13 | Aristas rancias tras las correcciones | PENDIENTE (medicion en curso) |
| 14 | Titulos y condiciones de activacion contra su contenido | PENDIENTE (medicion en curso) |
| 15 | Fase y dominio de cada nodo | PENDIENTE (medicion en curso) |
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

### Regresion de la campania de fidelidad sobre la politica de pais (medida determinista, 26 sep 2026)
- De las 487 correcciones, **17 tocaron 13 nodos con clase de pais** (por las listas de la politica o por su
  condicion de pais antes de la campania). **Ninguna quito** un reencuadre, una condicion de pais ni una mencion de pais.
- **4 anadieron la formula B** ("o la autoridad equivalente en tu mercado"): **2 en nodos-frontera de clase C**
  (`programas_cooperativos_osha` en `fidelidad-t3-44`, `valuacion_409a` en `fidelidad-t4-035`), que es una
  regresion (un nodo que solo aplica si operas en EE.UU. ahora ofrece un equivalente local); y 2 en nodos de
  exportacion de la lista de vigencia (`calculo_de_aranceles_importacion` `fidelidad-t4-007`,
  `reglas_de_origen_fta_2` `fidelidad-t4-011`), a leer. Se confirman leyendo en la pasada de jurisdiccion.
