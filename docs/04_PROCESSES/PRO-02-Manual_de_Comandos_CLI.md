# PRO-02 — Manual de Comandos CLI: probar todas las facetas del motor

Guía práctica para probar `engine/prototipo_motor.py` por tu cuenta, cubriendo
cada modo. Todos los comandos se corren desde la raíz del repo. Todos hacen
llamadas reales a la API salvo que se indique lo contrario (tienen costo
real, en céntimos de dólar — ver "Presupuestos" al final).

---

## 1. Sesión nueva (modo por defecto)

```bash
python engine/prototipo_motor.py
```
Pide tu idea, clasifica la puerta de entrada, y arranca la entrevista
turno a turno. Guarda en Supabase (o en `engine/projects_local/` si no hay
credenciales configuradas). Al final imprime el `project_id` — anótalo
para usarlo en `--seguir`/`--reporte` después.

**Para no tocar Supabase mientras pruebas** (recomendado en pruebas
sueltas que no te interesa conservar):
```bash
python engine/prototipo_motor.py --offline
```
Persiste en JSON local (`engine/projects_local/`) en vez de Supabase.
Todo lo demás (llamadas a la API, lógica del motor) es idéntico.

## 2. Retomar una sesión interrumpida

Si cierras el proceso a mitad de una pregunta (`Ctrl+C`, `Ctrl+Z`+Enter en
Windows, o cerrar la terminal), el motor cae en "cierre elegante" e
imprime el comando exacto para retomar:
```bash
python engine/prototipo_motor.py --continuar SESSION_ID
```
`SESSION_ID` es el id de 8 caracteres que imprime el mensaje de cierre
(también queda guardado en `engine/sessions/{SESSION_ID}.json`, no
versionado). Desde el hotfix v2.1.2, la pregunta que estaba pendiente se
re-presenta primero — respondela como si nunca se hubiera cortado.

**Para forzar tú mismo un corte a mitad de sesión** (útil para probar el
cierre elegante): en vez de contestar en la terminal interactiva, corré
```bash
echo "tu respuesta" | python engine/prototipo_motor.py
```
El pipe cierra `stdin` después de esa línea, así que el motor recibe EOF
en la siguiente pregunta y se cierra solo, guardando el progreso.

## 3. Seguimiento de un proyecto existente

```bash
python engine/prototipo_motor.py --seguir PROJECT_ID
```
`PROJECT_ID` es el UUID largo que imprimió la sesión original (o el que
ves en la tabla `projects` de Supabase). Pregunta "qué ha pasado desde la
última vez", elige una puerta de entrada avanzada según tu respuesta y el
`estado_vivo` comprimido del proyecto, y sigue la entrevista desde ahí.

## 4. Organizador gratuito (sin entrevista)

```bash
python engine/prototipo_motor.py --gratis
```
Una sola llamada, sin preguntas — organiza tu idea cruda en un resumen
estructurado. Crea un proyecto nuevo igual que el modo completo (podés
seguirlo después con `--seguir`).

## 5. Reporte de Sostenibilidad (Motor v2.1)

```bash
python engine/prototipo_motor.py --reporte PROJECT_ID
```
Requiere un proyecto existente. Revisa qué campos numéricos ya se
declararon en conversaciones anteriores (`numeros_proyecto`), pregunta por
los que falten (hasta 6, determinístico, aceptás "no sé" sin que insista),
calcula todo con `calculadora.py` (cero LLM), y narra el resultado con una
sola llamada a Sonnet. Presupuesto propio: $0.10 (independiente del
presupuesto general de sesión). Guarda el `.md` en la raíz del repo
(`reporte_*.md`, gitignored) y, si hay Supabase, una fila en `plans`
etiquetada `reporte_numeros`.

**Para repetir la mini-entrevista completa sin escribir cada respuesta a
mano**, podés encolarlas con un heredoc:
```bash
python engine/prototipo_motor.py --reporte PROJECT_ID <<'EOF'
8
4
15
85
5
no se
EOF
```
(ese orden — materiales, horas, valor hora, precio, capacidad, costos
fijos — es el de `PREGUNTAS_NUMERICAS` en `prototipo_motor.py`; si algún
campo ya está declarado, esa pregunta no aparece y el heredoc se
desalinea, así que conviene primero correrlo sin heredoc para ver
exactamente cuáles preguntas quedan pendientes).

## 6. Combinaciones útiles

```bash
python engine/prototipo_motor.py --seguir PROJECT_ID --offline
python engine/prototipo_motor.py --continuar SESSION_ID --offline
python engine/prototipo_motor.py --reporte PROJECT_ID --offline
```
`--offline` combina con cualquier otro modo — fuerza JSON local sin
cambiar la lógica de conversación.

---

## 7. Mantenimiento del dataset (no es el motor conversacional)

```bash
python scripts/run_phase1.py
```
Gate 0: valida los 1266 nodos del grafo (enlaces rotos, dominio válido,
alcanzabilidad, duplicados, símetría de aristas). Correr después de
cualquier cambio a `dataset/nodos/`. Si termina con `GATE 0: OK` y no
había trabajo nuevo de simetrización, `dataset/metadata/phase1_run_log.json`
puede quedar sobrescrito con un log casi vacío — restaurarlo con
`git checkout HEAD -- dataset/metadata/phase1_run_log.json` si el diff de
`master_graph.json` no tiene el cambio que esperabas.

```bash
python engine/build_semantic_index.py
python engine/build_question_cache.py
```
Regeneran el índice semántico (embeddings locales, sin costo de API) y el
caché de preguntas (con costo de API, una llamada Haiku por nodo nuevo) —
correr después de agregar nodos al dataset. `build_question_cache.py`
acepta `--patch NODE_ID` para regenerar solo un nodo en vez de los 1266.

---

## Presupuestos y costos

- Sesión normal (nueva o `--seguir`): tope $0.30 (`PRESUPUESTO_SESION_USD`,
  configurable por variable de entorno). Al llegar al tope, el motor cae
  a un menú numerado de emergencia en vez de seguir llamando a la API.
- `--reporte`: tope propio $0.10, independiente del anterior.
- Costo real de cada corrida se imprime al final ("Costo real de la
  sesion (tokens)"), desglosado por componente (turnos, plan, estado_vivo,
  reporte).

Ver también [TST-01-Registro_de_Pruebas](../05_TESTING/TST-01-Registro_de_Pruebas.md)
para la suite de pruebas automatizadas (sin costo, mocks) que valida la
lógica interna sin necesidad de correr sesiones reales.
