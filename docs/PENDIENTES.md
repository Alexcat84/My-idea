# Pendientes — My Idea

Lista viva de lo que queda por hacer. Se actualiza al cerrar o abrir frentes.
(Última actualización: agosto 2026.)

## 1. Campaña "Espacios" — Fase 3 restante (en cola)

**Plan detallado: `docs/PLAN_ESPACIOS_FASE3.md`** (propuesta pendiente del visto
del fundador y del auditor; enfoque Opción A "dentro de Tu avance", garantías de
fuente única / partición exacta / sin doble conteo, y las 5 tandas).

La Fase 1+2 y las 3 caras del espacio (Plan · Manos a la obra · Tu avance) ya
están en producción. Queda el resto de la Fase 3:

- **Documentos por espacio**: el plan y los seguimientos de cada espacio en .md/PDF,
  filtrados por dominio (del mismo texto del servidor).
- **Estadísticas por espacio**: dibujar `analyticsDeMundo` (ya calculado en
  `analytics.ts`) en el hub de cada mundo.
- **Etiquetas de espacio** (nombres de cara) en la bitácora y el expediente; **regla
  de ruido cero**: solo aparecen cuando el proyecto tiene ≥1 mundo.
- **Addendum — bitácora y reporte POR ESPACIO** como vistas filtradas de la fuente
  única ("una fuente, muchas lecturas": nunca registros paralelos). Partición EXACTA:
  cada entrada de la global aparece en exactamente una específica.
- **Análisis del proyecto sin doble conteo**: "Tu proyecto completo: core y N mundos";
  el avance de cada nivel es el suyo, el del proyecto es la suma declarada.

## 2. Claude Design (encargos)

- **Centro de créditos v4** (alta industria, modelo de consumible): brief y prompt v2
  listos (`docs/calibracion-design/BRIEF_CREDITOS.md`, `PROMPT_CREDITOS_CD.md`).
  Esperando opciones de CD.
- **Espacios** (pestañas-fichero + hub + caras): `docs/calibracion-design/BRIEF_ESPACIOS.md`
  listo, con el riesgo de los dos niveles de navegación explícito. Encargo a CD para
  calibrar la vara visual (incluida la cara "Tu avance").
- **PDF Expediente · interiores (DIFERIDO post-beta):** el diseño YA existe
  (`_entrega-claude-design/Entrega-desing 20260729/entrega2/pdf-expediente-interiores/`:
  Tus Números, un mundo, "Cómo te fue", "La secuencia de tu viaje"). **Cuando sea el
  momento: pedirle a CD regenerar esas 4 páginas en HTML LIMPIO (sin imágenes
  embebidas / blobs)** para poder implementarlas; las HTML entregadas están pesadas y
  no se pueden leer bien tal cual.

## 3. Verificación en vivo (necesita `pnpm dev` + Supabase real; la corre el fundador/auditor)

- **Vuelo de dinero** (`web/scripts/vuelo_beta.ts`): la contabilidad nueva del Catálogo
  congruente (siembra 30 → plan −10 → Tus Números 0 → mundo −5 → seguimiento −5 →
  seguimiento de mundo −5 = 5). **NO corrido en vivo.**
- **Gate** (`web/scripts/gate_beta.ts`): capturas de `/creditos`, del cambiador, del hub
  y de las **3 caras** de Espacios (dos viewports). La **siembra de un mundo con plan**
  en el gate es nueva y **no se corrió en vivo** → verificar el esquema al ejecutarlo.
- **Veredicto visual del fundador** sobre el conjunto de Espacios y sobre el centro de
  créditos (cuando pruebe en producción).
- **Auditoría**: Catálogo congruente y Espacios quedan en revisión del auditor.

## 4. Pasarelas y cuenta — ETAPA 3 (dormido a propósito)

- **Compra con dinero** (RevenueCat / Stripe / Play): la compra "se abre pronto"; el
  catálogo de packs muestra el estado deshabilitado hasta la ETAPA 3.
- **Siembra manual de créditos** (mientras): el fundador otorga créditos desde Supabase
  (`otorgar_creditos`, origen `siembra_beta`) — documentado en `docs/BETA_CUENTAS_README.md §2.f`.
- **2FA/TOTP + dominio de correo propio**: dormido (anclas listas).

## 5. Backlog / afinar

- **Ajustes visuales de Espacios** que salgan de la prueba del fundador (grosor del eje y
  tamaño de nodos de "Tu avance", cuánto se "levanta" la pestaña activa, el segmentado).
- **Píldora-humana** en las fechas: backlog post-beta (de la fidelidad al canon).
- La **decoración de papel** de los interiores del Expediente (ver §2, ligado al pedido a CD).
- **`cumplimiento-desglose-core-multiciclo`** (analytics): la fila "core" de
  `cumplimientoPorDominio` cuenta ítems de cualquier ciclo, mientras los tiles globales
  cuentan solo el plan baseline vigente. No es doble conteo; criterio distinto que puede
  no cuadrar con varios ciclos. Arreglo NO es de una línea (pasar el id del baseline a
  `cumplimientoPorDominio`). Nombrado en `docs/PLAN_ESPACIOS_FASE3.md §6`; **jamás
  arreglar "de paso"**.

## Hecho recientemente (para no reabrirlo por error)

- **Calendario**: modo con-fechas + recordatorios + `.ics` universal (webcal) EN PRODUCCIÓN.
  El **Google Calendar Nivel 1 se RETIRÓ** a favor del webcal universal (no reabrir).
- **Catálogo congruente** (precios 10/5, Tus Números incluido, beta sin cortesía): EN PRODUCCIÓN.
- **Espacios** Fase 1+2 + las 3 caras (Plan · Manos a la obra · Tu avance): EN PRODUCCIÓN.
