# Los dos sensores del panel de nodos — diseño, costo y recomendación

**Solo reporte.** No se instrumentó nada: la instrumentación se dispara con el
visto del fundador.

**Por qué corre el reloj:** la telemetría solo acumula desde que el sensor
existe. Un sensor que nace después del primer tester no puede contar lo que ese
tester hizo. La meta es que los dos estén vivos **antes** del primer tester.

---

## (b1) El ítem del checklist y su nodo de origen

### La pregunta era: ¿el redactor emite el mapa, o hace falta una pasada tipo-enlazador?

**Ya lo emite.** Y esto cambia el diseño entero, así que lo pongo primero.

Desde la Fase 3.1 (la caja de vidrio) el redactor **autodeclara** en su salida:

```ts
interface AutodeclaracionPlan {
  familias_tratadas?: string[];
  etapas?: Record<string, string[]>;   // "1" -> [node_id, node_id, ...]
}
```

Es decir: **por cada etapa numerada, qué node_ids usó realmente**. Y hay más:
`verificarProcedenciaEtapas()` ya comprueba de forma determinística que cada id
declarado pertenezca al material que se le entregó de verdad; si el modelo
inventa un id, se registra `procedencia_invalida`.

O sea que el trabajo caro —conseguir el mapa y saber que no está alucinado— **ya
está hecho y en producción**. Lo que falta es solo *persistirlo* al derivar el
checklist.

**No hace falta pasada tipo-enlazador. No hace falta llamada extra a la API.
El costo por plan es CERO.**

### Lo que falta, y su límite honesto

La autodeclaración es **por etapa**, no por ítem. Un ítem del checklist hereda
los nodos de **su etapa**, no "su" nodo exacto. Cuando una etapa usó tres nodos
y produjo cinco ítems, no se sabe cuál vino de cuál.

Dos caminos:

- **(1) Barato y honesto: guardar los nodos de la ETAPA.** Cero API, cero
  cambios al prompt. El sensor responde *"este ítem salió de una etapa que usó
  estos 3 nodos"*. Para la pregunta que el panel quiere contestar —*¿qué nodos
  producen ítems que la gente marca como hechos?*— eso sirve: agregado sobre
  cientos de planes, la señal se separa del ruido.
- **(2) Caro y exacto: pedir la autodeclaración por ítem.** Cambia el contrato
  de salida del redactor, alarga la cola (que es lo primero que se corta al
  agotar `max_tokens`, según su propio comentario) y arriesga la sección que ya
  funciona.

**Recomiendo (1).** El sensor perfecto que llega tarde vale menos que el bueno
que llega antes del primer tester. Y si algún día la agregación por etapa se
queda corta, la (2) se puede añadir encima sin deshacer nada.

### La migración

```sql
ALTER TABLE public.checklist_items
  ADD COLUMN nodos_origen text[];
```

**Nullable, sin default.** Los ítems que ya existen quedan en `NULL`, que se lee
como *"nació antes del sensor"* y no como *"no vino de ningún nodo"*. Esa
distinción importa: si se pusiera `'{}'` por defecto, los planes viejos
mentirían diciendo que no tuvieron origen.

`text[]` y no una tabla puente porque no hay nada que consultar *desde* el nodo
hacia el ítem: la pregunta siempre va del ítem hacia sus nodos, y el arreglo lo
resuelve sin un JOIN.

### Los tests

1. **Un plan con autodeclaración** guarda sus `nodos_origen` por ítem según la
   etapa de cada uno.
2. **Un plan SIN autodeclaración** (el modelo la omitió, que ya pasa hoy y cae
   al respaldo por encabezados) guarda `NULL`, no `'{}'`.
3. **Un id alucinado** que `verificarProcedenciaEtapas` marcó como inválido
   **no** se persiste: el sensor no puede guardar procedencia falsa.
4. **Contrato de esquema**: `dbContract.test.ts` verifica la columna contra la
   migración, como todas.

---

## (b2) La granularidad temporal de `project_nodes`

### Lo que hay hoy

```sql
CREATE TABLE public.project_nodes (
  id UUID PRIMARY KEY,
  project_id UUID NOT NULL REFERENCES projects,
  session_id UUID NOT NULL REFERENCES sessions,
  node_id TEXT NOT NULL,
  tipo TEXT NOT NULL CHECK (tipo IN ('conversado','silencioso','cosechado','salto')),
  created_at TIMESTAMPTZ DEFAULT NOW(),
  UNIQUE (project_id, node_id)
);
```

**`created_at` y `session_id` ya existen.** La pregunta del encargo —*¿basta
`created_at`/`session_id` nullable?*— tiene una respuesta mejor: ya están, y
`session_id` ya es NOT NULL, que es más fuerte.

### El límite real, y no es el que parecía

**`UNIQUE (project_id, node_id)`.** Un nodo cuenta **una sola vez por proyecto**.
Así que hoy se puede saber *cuándo se pisó por primera vez* y *en qué sesión*,
pero **no** si se volvió a pisar, ni cuántas veces, ni si el usuario volvió a él
en un ciclo posterior.

Y hay una consecuencia que conviene decir en voz alta: el insert de `db.ts` no
tiene `ON CONFLICT`. Un intento de re-insertar el mismo nodo **lanza excepción**.
Hoy no revienta porque el motor filtra los ya cubiertos antes de insertar, pero
esa protección vive en el código de llamada, no en el esquema.

### Qué haría falta para la granularidad completa

Quitar el `UNIQUE` y contar visitas. Pero ese índice **no es decorativo**: es lo
que hace que `nodosCubiertos()` devuelva un conjunto limpio, y ese conjunto se
usa como **lista de exclusión** del recorrido. Sin `UNIQUE`, cada consulta de
cobertura tendría que deduplicar, y el motor entero depende de eso.

### Mi recomendación: NO tocar el UNIQUE. Una tabla aparte.

```sql
CREATE TABLE public.node_visits (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  project_id uuid NOT NULL REFERENCES public.projects(id) ON DELETE CASCADE,
  session_id uuid NOT NULL REFERENCES public.sessions(id) ON DELETE CASCADE,
  node_id text NOT NULL,
  tipo text NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX node_visits_node_idx ON public.node_visits(node_id);
CREATE INDEX node_visits_project_idx ON public.node_visits(project_id);
-- SIN unique: aquí cada visita es una fila, y eso es el punto.
```

`project_nodes` se queda **exactamente como está** —es el estado, y el motor
depende de él— y `node_visits` es **el diario**. Estado y diario son cosas
distintas y mezclarlas fue lo que creó el límite.

**Coste de escritura:** un insert más por nodo cubierto, en el mismo camino que
ya inserta. Sin API, sin latencia perceptible.

**Lo que desbloquea, y que hoy es imposible:** cuántas veces se vuelve a un
nodo, en qué sesión, cuánto tarda alguien entre pisarlo y cosecharlo, y qué
nodos se visitan y **nunca** se cosechan — que es justo la señal que separa un
nodo útil de uno que estorba.

---

## Resumen para tu decisión

| | mecanismo | costo por plan | migración | riesgo |
|---|---|---|---|---|
| **b1** | reusar la autodeclaración que ya existe | **$0** | 1 columna `text[]` nullable | bajo: nada cambia en el prompt |
| **b2** | tabla `node_visits` aparte | **$0** | 1 tabla + 2 índices + RLS | bajo: `project_nodes` no se toca |

**Ambos sensores son de coste cero por plan.** Lo único que cuesta es una
migración que tú aplicas y el cableado, y ninguno de los dos toca el motor: b1
escribe en el mismo sitio donde ya se deriva el checklist, y b2 añade una
escritura al lado de la que ya existe.

**Mi recomendación es disparar los dos, y pronto.** No por su tamaño, que es
chico, sino porque **son los únicos dos pendientes que se degradan con el
calendario**: cada día sin ellos es un día de telemetría que no existirá nunca.
