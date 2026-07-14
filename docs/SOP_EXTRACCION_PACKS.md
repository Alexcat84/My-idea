# SOP — Extracción de nodos para packs (mundos temáticos)

Procedimiento versionado para construir un pack temático (un "mundo" premium)
a partir de libros fuente. **Esta es la vara real, reconciliada con el pipeline
del repo** (el validador `scripts/expansion/validar_esquema.py`), no un
documento genérico de chat.

> Reconciliación 2026-07-12 (pack risk_management): el documento de arranque
> de esa extracción tenía 3 erratas de esquema que el validador real habría
> rechazado. Este SOP las corrige. **Ante cualquier duda de esquema, manda el
> validador, no este texto.**

## Contexto del proyecto
My Idea es una app de guía emprendedora basada en un grafo de conocimiento
curado. Cada concepto es un "nodo" JSON. Los nodos se agrupan en dominios: el
"core" (el plan principal) y "packs" temáticos premium (mundos). Un pack nuevo
se extrae de varios libros y se destila en nodos.

## EL ESTÁNDAR DE NODO (obligatorio — la lista blanca del validador)
El validador `scripts/expansion/validar_esquema.py` define `CAMPOS_PERMITIDOS`
(lista blanca: cualquier campo fuera de ella hace RECHAZAR el nodo) y
`OBLIGATORIOS_NO_VACIOS`. El estándar es EXACTAMENTE:

```json
{
  "node_id": "identificador_ascii_minusculas_con_guiones_bajos",
  "fase_proyecto": "ideacion",
  "dominio": "nombre_del_pack",
  "titulo_concepto": "Nombre del Concepto en el Libro",
  "fuente": "Autor, Título, Cap. N (sección)",
  "resumen_teorico": "Párrafo de 80-150 palabras destilando el concepto en palabras propias, jamás copiando pasajes del libro. Lenguaje de consultor que le habla a un emprendedor, con acentos correctos del español.",
  "pasos_accionables": [
    "Paso 1 imperativo, concreto, hacible esta semana.",
    "Paso 2 imperativo."
  ],
  "entregable_esperado": "Una frase: el artefacto concreto que el emprendedor termina con en la mano.",
  "nodos_previos": ["Título del nodo del que se viene"],
  "nodos_siguientes": ["Título del nodo al que se avanza"],
  "condiciones_activacion": [
    "Situación concreta del emprendedor que activa este nodo",
    "Otra señal del usuario"
  ],
  "etiqueta_arbol": "Tu Etiqueta Corta"
}
```

### Diferencias clave frente a documentos de arranque viejos (NO repetir)
- **NO existe el campo `familia`.** No está en la lista blanca: incluirlo hace
  que el validador RECHACE el nodo (exit 1, "campo renegado").
- **`entregable_esperado` es OBLIGATORIO y no vacío.** Es un string: el
  artefacto concreto que el emprendedor obtiene (no una lista).
- **`fase_proyecto` solo admite las 4 del motor:** `ideacion`, `validacion`,
  `planificacion`, `ejecucion` (`FASES_VALIDAS`). NO existen "construccion",
  "operacion" ni "crecimiento".
- **`etiqueta_arbol` SÍ está permitido** (lista blanca) y es deseable; si no se
  escribe a mano, el pipeline lo genera (`scripts/generar_etiquetas_arbol.py`).
- **`ids_alias`** también está permitido (legado del saneamiento ascii); no se
  escribe a mano en la extracción.

### Reglas de cada campo
- **node_id**: `^[a-z0-9_]+$`, único en todo el universo (verificar contra
  `scripts/ids_existentes.txt`). El validador exige `node_id == nombre de
  archivo`. Si hay colisión, añadir sufijo del pack (p. ej. `_rm`).
- **fase_proyecto**: una de las 4 válidas. Si el índice narrativo usa más fases
  (p. ej. una historia de 5 etapas para el emprendedor), se MAPEA a las 4 del
  motor (ver "Mapeo de fases" abajo). La granularidad extra no le aporta nada a
  la brújula ni a la brecha, y añade fricción.
- **dominio**: la clave del pack (p. ej. `risk_management`), igual en todos.
- **titulo_concepto**: el nombre del concepto tal como el libro lo presenta.
- **fuente**: libro + capítulo/sección.
- **resumen_teorico**: 80-150 palabras, PALABRAS PROPIAS (nunca pasajes), con
  acentos correctos.
- **etiqueta_arbol**: máximo 6 palabras y 40 caracteres. Segunda persona o
  imperativo; cero anglicismos de manual ("risk register", "stakeholder"); cero
  nombres de autores. Titular de revista que le habla al emprendedor.
- **condiciones_activacion**: 2-4 situaciones concretas del emprendedor, en
  lenguaje llano.
- **pasos_accionables**: 3-6 pasos imperativos concretos, hacibles esta semana.
- **entregable_esperado**: el artefacto que queda al terminar los pasos.
- **nodos_siguientes / nodos_previos**: como TÍTULOS textuales por ahora (el
  pipeline los resuelve a IDs en una segunda pasada).

### Orden de campos
Espejar el orden del repo: `node_id, fase_proyecto, dominio, titulo_concepto,
fuente, resumen_teorico, pasos_accionables, entregable_esperado, nodos_previos,
nodos_siguientes, condiciones_activacion, etiqueta_arbol`. (El validador no
exige orden, pero la consistencia ayuda a la revisión.)

## Mapeo de fases (índice narrativo de 5 → 4 buckets del motor)
Si el índice organiza los conceptos en una narrativa de 5 etapas emprendedoras,
mapear a las 4 fases reales así (usado en risk_management):

| Narrativa del índice | fase_proyecto |
|---|---|
| Ideación | `ideacion` |
| Validación | `validacion` |
| Construcción | `planificacion` |
| Operación | `ejecucion` |
| Crecimiento | `ejecucion` |

## REGLAS DE EXTRACCIÓN (lecciones de olas previas)
1. DESTILAR conceptos, nunca copiar pasajes (libros con copyright: se extraen
   IDEAS y MÉTODOS en palabras propias).
2. Un concepto = un nodo. No agrupar 3 ideas ni fragmentar una en 5.
3. El TONO le habla a UNA persona que puede estar sola, sin equipo, sin jefe,
   empezando. Cero supuestos corporativos ("su organización", "el comité"). Si
   el libro habla en corporativo, traducir a emprendedor individual.
4. `pasos_accionables` CONCRETOS y hacibles esta semana, sin jerga.
5. `condiciones_activacion` describen la SITUACIÓN del emprendedor, no el
   capítulo del libro.
6. PROHIBIDOS los guiones largos y medios (— –) en cualquier texto. Usar coma,
   dos puntos o punto.
7. Los nodos de un pack NO duplican contenido de otros packs. Cada pack tiene su
   alcance; los dominios especializados se mencionan como categorías y se remite
   a sus mundos, jamás se duplica su contenido.
8. Destilar del TEXTO REAL de cada sección (verificar antes de construir), no de
   memoria.

## PROCESO (paso a paso)
1. **Preparar la vara**: generar `scripts/ids_existentes.txt` (todos los
   node_id de `dataset/nodos/*.json` + `packs/*/nodos/*.json`) para chequear
   colisiones. Tener los libros en texto.
2. **Índice temático consolidado** (40-80 conceptos genuinamente distintos,
   agrupados por fase narrativa; título, libro, capítulo, una línea de qué
   aporta). NO generar nodos aún: es para aprobación.
3. **Revisar y aprobar/ajustar** el índice (fusiones, recortes, añadidos).
4. **Generar los nodos en lotes** de 10-15, empezando por la primera fase y
   avanzando. Cada nodo destilado del texto real de su sección. Estándar de
   nodo AL PIE DE LA LETRA. `nodos_previos/siguientes` como títulos textuales.
5. **Validar cada lote con el validador REAL** entre lote y lote:
   `python scripts/expansion/validar_esquema.py <carpeta_de_nodos_individuales>`
   (exit 0 = limpio). Chequear además: node_id único vs. `ids_existentes.txt`,
   `etiqueta_arbol` <= 6 palabras/40 chars, cero guiones largos.
6. **Consolidar** todos los lotes en `packs/<pack>/nodos_crudos/<pack>_crudo.json`
   (array). La resolución de aristas, dedup, Gate 0, semillas y puentes los hace
   el pipeline existente, no la extracción.
