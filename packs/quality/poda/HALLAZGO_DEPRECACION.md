# El paso 4 necesita un mecanismo que no existe

Paro antes de consolidar y lo explico, porque construirlo mal rompe la selección
en producción **sin que nada se queje**, que es la clase de avería que esta casa
persigue.

## Lo que pide el encargo

> deprecación-de-la-selección de los absorbidos (JAMÁS borrado: 165 vivieron en
> recorridos)

Es decir: el nodo absorbido **deja de ser elegible** pero **sigue existiendo**.

## Lo que hay hoy

La casa ya tiene una fusión, en `scripts/hseq/paso2_dedup.py --fusionar`. Hace
esto:

1. el superviviente absorbe `ids_alias` y `merged_originals`
2. hereda las aristas del absorbido
3. **borra el archivo del absorbido** (`borrar_nodo`)
4. redirige las referencias entrantes del dominio

O sea: **el mecanismo existente SÍ borra.** Es lo contrario de lo encargado.

Y hay un segundo problema, más silencioso: **nada en `web/` consume
`ids_alias`.** Lo verifiqué con búsqueda exhaustiva: solo lo leen scripts de
saneamiento (`paso1_ascii`, `paso3_4_aristas`, `tejer_ola1`). El motor no lo
mira. Así que un id absorbido:

- no resuelve en el grafo,
- y `etiquetaArbol()` (`lib/engine/graph.ts:74`) cae a su último recurso:
  `?? nid`, o sea **muestra el identificador crudo** en vez de un título.

No es un crash — el código es defensivo con `?.` en todas partes — pero es
exactamente "la historia se toca".

## Lo que además encontré por el camino

**32 nodos de `dataset/nodos/` ya llevan `merged_originals`**, un campo que
**el validador NO permite** (`CAMPOS_PERMITIDOS` no lo incluye). No revienta
nada porque `validar_esquema.py` se corre a mano sobre carpetas concretas y
nadie lo corre sobre `dataset/nodos/`. Es una inconsistencia dormida, de la
fusión HSEQ de la Fase 3.5. **No la toco**: la reporto.

## El diseño que propongo

Un campo nuevo y uno existente usado como fue pensado:

| campo | dónde | qué hace |
|---|---|---|
| `deprecado: true` | en el **absorbido** | lo saca de la SELECCIÓN, no del grafo |
| `ids_alias` | en el **superviviente** | ya está en la lista blanca; recoge los ids absorbidos |

El absorbido **conserva su archivo, su id, su título y su resumen**. Sigue
resolviendo, así que cualquier lectura histórica muestra su nombre de verdad.
Lo único que pierde es la elegibilidad.

**Lo que hay que tocar para que la deprecación signifique algo** (y esto es lo
que hace al paso 4 más grande de lo que parecía):

1. `scripts/expansion/validar_esquema.py`: `deprecado` entra en la lista blanca.
   Es un cambio de esquema y quiero tu palabra antes de hacerlo.
2. `scripts/build_semantic_index_voyage.py`: los deprecados no se embeben. Sin
   esto, el buscador semántico los sigue ofreciendo y la deprecación es
   decorativa.
3. La selección del motor (`lib/engine/`): los deprecados no se proponen. Hay
   que encontrar el punto único donde se filtran candidatos, o serán varios.
4. `scripts/run_phase1.py` (Gate 0): un deprecado no puede exigir alcance ni
   contar como huérfano, pero sus aristas **sí** deben seguir siendo válidas.
5. `engine/build_question_cache.py`: no gastar API en preguntas de deprecados.

## Por qué no lo hago y te pregunto

Tres de esos cinco puntos son **producción viva**: el índice semántico, la
selección del motor y el Gate 0. Un filtro puesto en el sitio equivocado no
falla: simplemente deja de ofrecer nodos, o los sigue ofreciendo, y en ambos
casos el síntoma aparece semanas después en el recorrido de alguien.

La alternativa es la que ya existe: **fusionar borrando** con `ids_alias`, y
aceptar que 89 ids salgan del grafo. Es menos trabajo y está probada, pero
contradice tu instrucción explícita.

**Las dos opciones, para tu palabra:**

- **(A) Deprecación de verdad.** Construir el mecanismo de los cinco puntos.
  Más trabajo, toca el validador y la selección, y es lo que pediste.
- **(B) Fusión con alias, como HSEQ.** Rápida y probada, pero 89 ids
  desaparecen del grafo y las lecturas históricas de esos nodos mostrarían el
  identificador crudo.

Mi recomendación es **(A)**, y con una condición: que el filtro de elegibilidad
viva en **un solo sitio** del motor, con su test, porque repartido en tres es
donde nace el fallo silencioso.

---

## Lo que sí quedó hecho

La poda del auditor está aplicada al índice:

- **66 clusters se funden**
- **`costo_de_mala_calidad_copq_2` excluido** del cluster 1 y conservado como
  nodo propio (definir el COPQ y medirlo son acciones distintas; su telemetría
  de *visto 8 · cosechado 7* lo confirma puerta viva). El cluster 1 queda con 6.
- Supervivientes por las reglas adoptadas: telemetría en 42, propuesto en 23,
  y el cluster 8 esperando tu ojo.
- Tres banderas anotadas para `re-voz-de-quality`, sin tocar: clusters **24**
  (frontera con Riesgos), **44** (puntajes Shingo) y **43 / 58** (voz
  corporativa).

**Cuentas: 66 supervivientes, 89 absorbidos. 896 − 89 = 807 nodos.** (Tu
estimado era ~808; la diferencia es exactamente el nodo que el auditor excluyó.)
