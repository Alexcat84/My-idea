### DECISION 3.a. La fase de cada nodo, por lectura y en un registro incremental

> La FASE de cada nodo se asigna por lectura contra el criterio de fases que My-idea ya usa
> (cita el documento), y se guarda en un registro por id (fases_mundo11.jsonl) para que sea
> INCREMENTAL. Ciega de 20 nodos al azar con semilla escrita al terminar.

**El criterio citado.** `docs/SOP_EXTRACCION_PACKS.md`, linea 52: *`fase_proyecto` solo admite
las 4 del motor: `ideacion`, `validacion`, `planificacion`, `ejecucion`*; y lineas 88 a 100,
*Mapeo de fases*: Ideacion a `ideacion`, Validacion a `validacion`, Construccion a
`planificacion`, Operacion y Crecimiento a `ejecucion`. El motor usa la fase como **la etapa
del proyecto en la que la persona necesita ese procedimiento** (`engine/prototipo_motor.py`,
`candidatos_seguimiento`, y `web/lib/engine/evaluacionBrecha.ts`, `ORDEN_FASES`: puntuan mas
los nodos de la fase actual del proyecto y de la siguiente).

**La vara, escrita ANTES de leer y aplicada a un mundo de equipo:**

| fase | cuando la lleva un nodo del mundo 11 |
|---|---|
| `ideacion` | decide si la gestion o el equipo es su camino, o se conoce a si misma, ANTES de sostener un equipo |
| `validacion` | prueba con evidencia real si algo funciona (se mide, ensaya, diagnostica o contrasta) antes de comprometerse |
| `planificacion` | monta la estructura antes de usarla: proceso, sistema, plan, tarjeta, calendario o formato (la Construccion del SOP) |
| `ejecucion` | corre el equipo en el dia a dia o lo hace crecer: conversacion, reunion, decision o gesto en curso (Operacion y Crecimiento) |
- **`entregable_esperado` es OBLIGATORIO y no vacío.** Es un string: el
  artefacto concreto que el emprendedor obtiene (no una lista).
- **`fase_proyecto` solo admite las 4 del motor:** `ideacion`, `validacion`,
  `planificacion`, `ejecucion` (`FASES_VALIDAS`). NO existen "construccion",

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

