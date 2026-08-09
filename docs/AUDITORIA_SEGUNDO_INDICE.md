# El segundo índice semántico: auditoría con paro

**Solo lectura. Cero código tocado, cero archivos movidos, cero regeneraciones.**
La decisión entre retirar el `.npz` con su código o meterlo bajo el mismo chequeo
la toma el fundador con el auditor.

---

## Los dos índices, lado a lado

| | `web/lib/assets/semantic_index.json` | `engine/semantic_index.npz` |
|---|---|---|
| vectores | **3.521** | **1.266** |
| dimensión | 512 | 384 |
| proveedor | **Voyage AI** (`voyage-4-lite`) | **sentence-transformers**, local |
| modelo | `voyage-4-lite` | `paraphrase-multilingual-MiniLM-L12-v2` |
| generador | `scripts/build_semantic_index_voyage.py` | `engine/build_semantic_index.py:23,43-44` |
| última escritura | **2026-08-08 20:51** (hoy) | **2026-07-08 17:40** (hace un mes) |
| lo consume | `web/lib/compass.ts`, `scripts/rumbos/prueba_rumbos.py`, `scripts/rumbos/puesto_de_blancos.py` | `engine/prototipo_motor.py:232, 1552-1560` |

**Los espacios no son comparables.** Proveedores distintos, modelos distintos y
dimensiones distintas: un vector de 384 de MiniLM y uno de 512 de Voyage no se
pueden medir con el mismo coseno ni mezclar. No es que uno esté desactualizado
respecto del otro: **son dos brújulas distintas**, y la del CLI apunta sobre un
mapa de hace un mes con dos tercios del territorio en blanco.

---

## (a) Qué caminos alcanzan hoy `buscar_afines` de `prototipo_motor.py`

`engine/prototipo_motor.py:1573` define la función. **La llaman exactamente dos
sitios, los dos dentro del mismo archivo**:

- **`prototipo_motor.py:1749`** — el salto semántico del bucle de entrevista:
  ofrece candidatos de salto con `min_score=MIN_SCORE_SALTO`.
- **`prototipo_motor.py:2007`** — la cosecha por familias faltantes,
  `buscar_afines(query, visitados, k=20, graph=graph)`.

**Ninguna ruta de la web lo alcanza.** Busqué `prototipo_motor` en `web/app`,
`web/lib` y `web/scripts`: las cinco apariciones son **comentarios de cabecera**
que documentan de qué función Python es port cada ruta
(`web/app/api/organizer/route.ts:3`, `follow/route.ts:3`, `report/route.ts:3`,
`session/start/route.ts:3`, `session/[id]/plan/route.ts:3`). **Cero imports,
cero invocaciones, cero `python engine/...`.** La web tiene su propio port en
`web/lib/compass.ts`, con Voyage.

**Ningún script de operación lo alcanza.** El único que importa
`prototipo_motor` fuera de `engine/` es `scripts/sync_assets_web.py:68`, y lo
hace **solo para leer las constantes `SYSTEM_*`** y exportarlas a
`prompts.json`. No toca la brújula.

**Conclusión de (a): `buscar_afines` del CLI solo se alcanza corriendo
`prototipo_motor.py` a mano.**

---

## (b) ¿Alguna de las 21 pruebas del motor ejercita ese índice?

**No. Ninguna carga la brújula de verdad.**

Diez de las 21 importan `prototipo_motor`, pero **ninguna** menciona
`_cargar_brujula` ni `semantic_index.npz`. La única que se acerca es
**`engine/test_salto_semantico.py`**, y hace lo contrario de ejercitarla:
**la sustituye entera** (`test_salto_semantico.py:23`):

```python
pm.buscar_afines = lambda texto, excluidos, k=5, min_score=0.0, con_score=False,
                          graph=None, dominios_desbloqueados=None: (
    [(candidato_salto, 0.9)] if con_score else [candidato_salto]
)
```

Y su propio docstring lo declara: *"sin llamadas reales a la API ni a la
brújula: monkeypatch de `pm.buscar_afines` para controlar exactamente qué
`saltos_posibles` se ofrecen"*.

**Está bien que lo haga**: ese test mide la validación del salto, no la
recuperación. Pero la respuesta a la pregunta es clara: **el `.npz` no lo
ejercita nadie, y por eso su desfase de 2.255 nodos no ha hecho caer ninguna
suite.** No es que la prueba mida sobre el universo equivocado: es que **no lo
mide en absoluto**.

---

## (c) Cuándo se generó y con qué

- **`.npz`**: `2026-07-08 17:40`, con `engine/build_semantic_index.py`
  (`sentence-transformers`, `paraphrase-multilingual-MiniLM-L12-v2`, local, sin
  API). Su propio docstring dice *"índice de embeddings de los 1265 nodos"*:
  **la cifra de su día**, que ya no es la de hoy.
- **`.json`**: `2026-08-08 20:51`, con `scripts/build_semantic_index_voyage.py`
  (Voyage, `input_type="document"`).

El `.npz` **no se regenera en ningún flujo**. `build_semantic_index.py` solo
aparece nombrado en documentación: el manual de comandos
(`docs/04_PROCESSES/PRO-02-Manual_de_Comandos_CLI.md:141`), una auditoría vieja,
y **la auditoría del motor de este ciclo, que ya lo había clasificado como
fósil** (`docs/AUDITORIA_MOTOR.md:61`). Ninguna línea de ensamblaje lo llama.

---

## Lo que esto significa, dicho sin adornos

**El desfase es real: 1.266 contra 3.521.** La brújula del CLI es ciega a
**2.255 nodos**, que son casi dos tercios del catálogo, y a **todo lo que este
ciclo tocó**: las fusiones, las 550 re-voces, los diez revividos, los dos mundos
nuevos.

**Pero no hay usuario expuesto.** Nadie llega a ese código salvo quien corra el
CLI a mano, y la web tiene su propia brújula con el índice al día. El riesgo no
es que un usuario reciba una mala respuesta: **es que alguien corra el CLI para
comprobar algo y se lleve una conclusión falsa**, creyendo que está midiendo el
motor cuando mide un mapa de hace un mes.

**Y el chequeo nuevo del Gate no lo cubre**, a propósito: mira
`web/lib/assets/semantic_index.json`, que es el que la web usa. Extenderlo al
`.npz` sería fácil, y sería la decisión equivocada si el `.npz` va a retirarse.

**Por eso paro aquí y no propongo una de las dos salidas como si fuera obvia.**
Las dos son defendibles:

- **Retirarlo con su código** cierra un fósil que ya nadie corre y que solo puede
  mentirle a quien lo use. Cuesta: se pierde la capacidad de correr el motor de
  CLI, que es donde vive el port original y de donde salen los prompts.
- **Meterlo bajo el mismo chequeo** lo mantiene vivo y honesto. Cuesta: hay que
  regenerarlo en cada cambio del catálogo, con una dependencia
  (`sentence-transformers`) que la línea de ensamblaje no usa para nada más.

**No borro, no regenero, no muevo nada.**
