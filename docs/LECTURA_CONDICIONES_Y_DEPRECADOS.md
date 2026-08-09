# Dos entregas de lectura — cero cambios, con el código en la mano

---

# (a) ¿Cómo se usan HOY las `condiciones_activacion`?

## La respuesta corta

**No son compuerta. Nunca.** Ningún camino del motor excluye un nodo porque su
condición no se cumpla. **La única compuerta es `esOfrecible`**: existe, no está
deprecado, dominio desbloqueado. Y esas tres cosas no miran el campo.

Lo que sí hacen las condiciones es **pesar**, de dos maneras distintas.

## Lo que hacen, sitio por sitio

### 1. Puntaje léxico, +1 por palabra compartida — cuatro sitios

| dónde | qué decide |
|---|---|
| `interprete.ts:241` (`elegirPorAfinidad`) | el respaldo tier-2: cuando el modelo falla dos veces, se elige el candidato con más palabras en común |
| `reeleccionPuerta.ts:67` (`afinidad`) | qué puerta le queda a un mundo cuando el intérprete descartó la actual |
| `planRedactor.ts:117` y `:137` | qué nodos se cosechan para el plan |
| `puertaAvanzada.ts:51` | qué candidato abre una sesión de seguimiento |

En los cuatro el texto puntuado es `titulo + condiciones_activacion` (y a veces
los primeros 300 caracteres del resumen). **Suma, no filtra.** Un nodo cuya
condición no encaja simplemente puntúa más bajo; si es el único candidato, se
ofrece igual.

### 2. Material para el modelo — `resumenNodo`

`graph.ts:238` mete **las dos primeras condiciones** de cada nodo en el resumen
que viaja al intérprete (`interprete.ts:315, 316, 340`) y a la puerta avanzada.
El modelo las **lee** y elige con ellas delante. Es la vía más cercana a una
compuerta, y es blanda: el prompt no le ordena descartar por condición.

### 3. **Y ya están embebidas en el índice semántico** ← corrección a la hipótesis

`scripts/build_semantic_index_voyage.py:56-62`:

```python
def texto_nodo(n):
    partes = [
        n.get("titulo_concepto", ""),
        n.get("resumen_teorico", ""),
        " ".join(n.get("condiciones_activacion", []) or []),
    ]
```

**Las condiciones ya forman parte del texto que se embebe.** La hipótesis del
auditor para el frente de recuperación —*"embeber también las
condiciones_activacion, es dato que ya existe y sería un spike barato"*— parte
de una premisa falsa: **ya están dentro**, y los tres rumbos rebeldes fallan con
ellas incluidas.

Eso no mata la intuición, la reorienta: si el campo escrito como situación ya
está en la mezcla y no basta, el spike que queda es **embeberlo aparte y
consultarlo aparte** (dos índices, o un campo con peso propio), no *añadirlo*.
Lo anoto en la ficha del frente y no lo diseño.

## Qué significa para la política de escala

**Es segura, con una advertencia.**

Segura porque la condición honesta que le pusimos a los nodos corporativos
—*"Si tu negocio ya tiene varias personas o áreas trabajando en esto"*— hace
justo lo que la política quiere: **pesa** hacia quien la cumple, tanto en el
puntaje léxico como en el índice semántico, y el modelo la lee antes de elegir.
Un artesano solo no la va a mencionar en sus palabras, así que esos nodos
puntúan bajo para él.

La advertencia: **no es un muro**. Si el catálogo se quedara sin candidatos
mejores, un nodo corporativo se le ofrecerá igual a quien trabaja solo. Hoy eso
es improbable —3.511 nodos activos y el núcleo cubre bien— pero conviene
decirlo: la política se apoya en un peso, no en una puerta.

**Si algún día se quiere que sea puerta**, el sitio existe y es uno solo:
`esOfrecible`. Está escrito para eso, y su docstring ya lo dice: *"Si mañana
hace falta una condición nueva para ofrecer un nodo, se escribe AQUÍ o no se
escribe"*.

---

# (b) Todo lo deprecado de selección — 10 nodos

De los **324 deprecados**, **314 son fusiones** (tienen sucesor que los reclama
por `ids_alias`). Solo **10 se retiraron de la selección** sin fusionarse. Ésos
son los que la política nueva puede tocar.

**Ninguno se revierte hasta tu palabra.**

## Clase 1 — PROGRAMA O FIGURA DE UN SOLO PAÍS (8)

Motivo original: *"los programas de tu estado no significan nada donde no hay
estados con programa"*.

| nodo | qué es | recomendación |
|---|---|---|
| `programas_estatales_locales_financiamiento_exportacion` | programas de financiamiento de **estados y ciudades de EE.UU.** | **VUELVE** con *"si exportas desde Estados Unidos"* |
| `asistencia_agencias_minoritarias_mbda` | agencia federal para empresas de minorías | **VUELVE** con *"si operas en Estados Unidos"* |
| `planes_estatales_osha` | los 22 planes estatales de OSHA | **VUELVE** con *"si tu negocio está en Estados Unidos"* |
| `programas_cooperativos_osha` | VPP, alianzas, asociaciones estratégicas | **VUELVE**, misma condición |
| `programa_consulta_osha_onsite` | consultoría gratuita de OSHA para pymes | **VUELVE**, misma condición |
| `recursos_educativos_osha` | materiales gratuitos de OSHA | **VUELVE**, misma condición |
| `recursos_niosh` | agencia de investigación del CDC | **VUELVE**, misma condición |
| `sbrefa_cumplimiento` | ley de 1996 que ayuda a pymes con OSHA | **VUELVE**, misma condición |

**Los ocho son reversibles bajo la política nueva**, y con la misma maquinaria
que ya corrió once veces con Magnuson-Moss: condición explícita y excluyente al
frente. Seis de los ocho son **servicios gratuitos del gobierno estadounidense**
para pequeñas empresas — es contenido útil de verdad para quien está allí, y
retirarlo fue una decisión de proporción, no de calidad.

**Un matiz que traigo, no decido**: `recursos_educativos_osha` y
`programa_consulta_osha_onsite` ya estaban **re-vozados a la voz de la casa**
antes de deprecarse (*"OSHA pone a tu disposición, sin costo…"*). Vuelven casi
listos.

## Clase 2 — ESCALA (2)

| nodo | qué es | recomendación |
|---|---|---|
| `equipo_mejora_calidad_2` | el grupo de personas que llevan la calidad a cada área | **VUELVE** con condición honesta de escala. Es exactamente el caso que la política nueva describe: si el lector tiene equipo, la respuesta con equipo es la correcta |
| `involucramiento_sindical_calidad` | cómo trabajar con el sindicato en un programa de calidad | **VUELVE** con *"si tu negocio tiene personal sindicalizado"*. Y es más que escala: es una **realidad legal** en buena parte del mundo, no una rareza corporativa |

## El detalle que hay que decidir con esto

Estos 10 tienen **`deprecado: true` y ningún `ids_alias` que los reclame**.
Revertirlos es quitar esa marca y darles su condición. Pero hay dos cosas que
mirar antes, y por eso **no toco nada**:

1. **El nodo-fantasma al revés.** Al deprecar los tres programas de OSHA se
   descubrió que dejaban 5 nodos activos sin entrada, y hubo que re-anclar. Al
   revertirlos, esas aristas vuelven a existir: **Gate 0 lo verificará**, pero
   conviene saber que el grafo se mueve.
2. **`involucramiento_sindical`** (sin sufijo) es un deprecado cuya cadena
   termina en `involucramiento_sindical_calidad`. Si el segundo revive, el
   primero resuelve a un nodo activo otra vez — que es lo correcto, y es el
   resolutor de la historia haciendo su trabajo sin que nadie lo toque.

**Costo estimado de la reversión completa**: 10 nodos × re-voz con condición
≈ **$0,25**, más Gate 0, re-embebido y rumbos.
