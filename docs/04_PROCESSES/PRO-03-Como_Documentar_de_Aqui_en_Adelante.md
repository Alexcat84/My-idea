# PRO-03 — Cómo documentar de aquí en adelante

Instrucciones fijas para mantener el QMS (`docs/`) coherente sin que se
vuelva a desordenar. Esto aplica a cualquiera que trabaje en el repo,
humano o agente.

---

## 1. Regla de nomenclatura

Todo documento formal vive en `docs/<categoria>/<PREFIJO>-<NN>-<Titulo_En_Snake_Case>.md`
y aparece indexado en [docs/00_MASTER_INDEX.md](../00_MASTER_INDEX.md) con
un enlace **relativo** (nunca `file:///` absoluto — no es portable a otra
máquina ni se renderiza en GitHub).

| Prefijo | Categoría | Carpeta |
|---|---|---|
| `STR` | Estrategia y visión | `docs/01_STRATEGY/` |
| `PLN` | Planificación / roadmap | `docs/02_PLANNING/` |
| `TEC` | Arquitectura técnica | `docs/03_TECHNICAL/` (aún vacía) |
| `PRO` | Procesos y operación (SOPs) | `docs/04_PROCESSES/` |
| `TST` | Pruebas y verificación | `docs/05_TESTING/` |
| `AUD` | Auditorías / cierres de fase | `docs/audits/` |

El número (`NN`) es secuencial dentro de su prefijo y **nunca se reutiliza
ni se borra**. Si un documento queda obsoleto, se le agrega una nota al
principio ("Superado por AUD-0X") en vez de eliminarlo — la trazabilidad
importa más que la prolijidad.

## 2. Cuándo crear cada tipo (y cuándo NO)

- **`AUD` — el que se crea con más frecuencia.** Un `AUD-XX` nuevo se
  escribe **al cerrar** una fase, un hotfix, o un hito real (cuando se
  aplica un tag de git, o el usuario declara algo "cerrado"/"certificado").
  No se crea uno por cada commit — se agrupa a la granularidad de fase
  (ver `AUD-01` a `AUD-04`: cada uno cubre varios commits relacionados).
  Estructura mínima: qué se planeó/motivó el cambio, qué se hizo (con
  commits), qué se verificó y con qué evidencia, estado final.
- **`TST`** — no se crea un `TST-XX` nuevo por cada test. Se **agrega una
  fila** a `TST-01` cada vez que se escribe o se mueve un archivo
  `test_*.py` real al repo (nunca se documenta un test que solo vive en un
  scratchpad de sesión — si no está commiteado, no cuenta como parte de la
  suite). Solo se justificaría un `TST-02` si el registro creciera tanto
  que conviniera separarlo por subsistema (ej. pruebas del motor vs.
  pruebas de un futuro backend web).
- **`PRO`** — se agrega un `PRO-XX` nuevo cuando se documenta un
  procedimiento operativo NUEVO y reusable (cómo desplegar, cómo rotar
  credenciales, cómo correr todo el sistema). No para una tarea puntual de
  una sola vez.
- **`PLN`** — se toca solo si cambia el roadmap completo del proyecto.
  `PLN-01` sigue vigente (Fases 0-4); no hace falta un `PLN-02` mientras el
  plan maestro no cambie de fondo.
- **`STR`** — se toca solo si cambia la visión u objetivo del proyecto en
  sí (raro, no confundir con progreso normal).

## 3. Flujo estándar después de cada iteración de trabajo

1. **Durante el trabajo** (mientras la fase/hotfix está abierta): el
   detalle turno-a-turno, transcripciones, hallazgos de auditoría en el
   momento, siguen viviendo en `examples/README.md` — es el registro
   "vivo" y narrativo, se actualiza con cada iteración, igual que hasta
   ahora.
2. **Al cerrar** (tag aplicado, o declarado terminado explícitamente):
   escribir el `AUD-XX` correspondiente resumiendo el mismo trabajo en
   formato cerrado/archivable (qué se planeó, qué se hizo, qué se
   verificó), y agregar su entrada a `docs/00_MASTER_INDEX.md`.
3. **Si se agregó o movió un `test_*.py`**: agregar su fila a `TST-01`
   antes de dar el trabajo por terminado — un test sin registrar es un
   test que se puede perder o duplicar sin que nadie lo note.
4. **Si se agregó un comando CLI, flag, o modo de operación nuevo**:
   actualizar `PRO-02` (el manual de comandos).
5. **Los planes/reportes que la app genera para usuarios reales** (no para
   el equipo) van a `engine/salidas/` — nunca a la raíz del repo. Esa
   carpeta está gitignored a propósito: es contenido de usuario final, no
   documentación del proyecto.
6. **Las migraciones SQL** siguen numeradas secuencialmente en
   `supabase/migrations/my_idea_0NN_*.sql`, referenciadas desde el
   `AUD-XX` que las originó — no tienen categoría `docs/` propia todavía
   (candidatas a `TEC` el día que esa carpeta deje de estar vacía).
7. **Todo test numérico nuevo en `calculadora.py`** sigue la regla ya
   fijada en `AGENTS.md` (`PRO-01`): el cálculo manual del escenario
   canónico se escribe en un comentario ANTES del assert — no se repite
   aquí, se referencia.

## 4. Checklist rápido al cerrar cualquier trabajo

- [ ] ¿Hay un test nuevo? → fila nueva en `TST-01`.
- [ ] ¿Hay un comando/flag nuevo? → actualizar `PRO-02`.
- [ ] ¿Se cierra una fase/hotfix/hito? → `AUD-XX` nuevo + entrada en
      `00_MASTER_INDEX.md`.
- [ ] ¿Hay una migración SQL nueva? → número secuencial, aplicada
      manualmente, referenciada desde su `AUD-XX`.
- [ ] ¿Generó la app algún `.md` de salida para un usuario? → debe estar en
      `engine/salidas/`, no en la raíz.
- [ ] ¿El índice maestro sigue teniendo enlaces relativos que resuelven a
      archivos reales? (se puede verificar con un `grep` simple de los
      links contra el filesystem, como se hizo al escribir este documento).
