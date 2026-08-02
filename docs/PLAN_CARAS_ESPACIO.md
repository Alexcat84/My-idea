# Plan — Las 3 caras de cada espacio (Plan · Manos a la obra · Tu avance)

Extensión de la campaña **"Espacios"** (Fase 1+2 ya en producción). Dentro de cada
pestaña-espacio (el core "Tu viaje" y cada mundo), un **selector segmentado** separa
el contenido en tres CARAS, para no apilar todo hacia abajo en un solo scroll.
Sin migraciones: todo sale de datos ya persistidos.

## 1. Objetivo y modelo

Cada espacio (una idea = un proyecto; el core + sus mundos) es un **expediente** con
tres caras, y se ve **una a la vez**:

| Cara | Qué muestra |
|---|---|
| **Plan** | el documento del plan del espacio (en un mundo, también su **diagnóstico**) |
| **Manos a la obra** | el checklist y su ejecución (la vista de hoy: rituales + tareas + cierre) |
| **Tu avance** | la **línea de hitos reales** del espacio: inicio → cada acción hecha → cierre |

Aplica al **core** ("Tu viaje") y a **cada mundo**. Un mundo **sin plan** (sin explorar
/ solo diagnóstico) **no** muestra el segmentado: conserva su flujo de explorar/comprar.

## 2. Decisiones cerradas (fundador)

1. **Selector SEGMENTADO** (no una segunda fila de pestañas-fichero, para no repetir):
   píldora con 3 celdas, indicador que se desliza, tema oscuro, un **icono por cara**.
   Es la versión de 3 opciones del switch de referencia que dio el fundador.
2. **Nombre de la 3.ª cara: "Tu avance".** Hallazgo: la línea de hitos de la Celebración
   **no tiene nombre de cara** hoy (interno "Timeline/hitos"); y **"Tu recorrido" ya
   está tomado** (el árbol de conceptos, "Construido con tu recorrido"). Por eso no se
   reusa ningún nombre y se elige "Tu avance" (palabra de persona, distinta).
3. **Aplica al core igual**, con su particularidad de inicio (Chispa → Claridad → Plan;
   el mundo arranca en su Diagnóstico → su Plan).

## 3. Reglas de la casa (no negociables)

- **Sin jerga:** nada de "timeline"/"Gantt" en la cara del usuario. Es **"Tu avance"**.
- **Ley de color:** el azul del indicador activo (piensa/estructura); el **verde**
  para hitos alcanzados y el cierre (ejecuta/celebra); el **gris** para hitos pendientes
  (lo que falta). Distinción por **forma** además de color. **Nunca rojo.**
- **"Tu avance" sale de DATOS REALES** (fechas persistidas), **cero invención, cero
  LLM, cero estadística** (las métricas viven en Análisis del proyecto; esto es la
  historia de hitos, no números).
- Acordeones colapsados por defecto (ya vigente).

## 4. Los datos por espacio (verificado contra el repo)

**Mundo** — todo disponible en el payload `mundos` de `/api/idea/[id]`:
`resumen_at` (diagnóstico), `plan.created_at` (su plan), sus **items completados**
(`completed_at`, ya scopeados por dominio vía `grupoVigente`), `completado_at` (cierre).
→ La línea del mundo se arma **sin datos nuevos**.

**Core** — parcialmente disponible en `ManosALaObra`:
- ✅ **Tu Plan**: `planCreatedAt` (ya es prop).
- ✅ **Acciones hechas**: los items del core con `completed_at` (ya en el checklist).
- ✅ **Realizada**: `realizada_at` (existe en `DetalleIdea.idea`, hoy no se pasa a
  `ManosALaObra`).
- ⚠️ **La Chispa** (`projects.created_at`) y **Claridad** (fecha del organizador) **no
  se exponen hoy** en `DetalleIdea`. Decisión del plan: **añadirlas** al payload de
  `/api/idea/[id]` (`idea.created_at`, `organizador.created_at`) y pasarlas a
  `ManosALaObra`. Alternativa mínima si se prefiere no tocar la ruta: el core arranca en
  "Tu Plan" (sin Chispa/Claridad). **Recomendación: exponerlas** (dos campos, sin
  migración) para que el core cuente su inicio completo.

Nota: `construirHitos` (analytics) **no etiqueta las acciones por dominio**, así que la
línea por espacio **no** se deriva de ahí: se arma de los **items ya scopeados** que
`ManosALaObra` tiene por dominio (`grupoVigente`). Sin tocar analytics.

## 5. Componentes

### Nuevo — `web/app/ui/SelectorCara.tsx` (segmentado, presentacional)
- Píldora `surface-2` con 3 celdas; indicador **accent** que se desliza (`translateX`
  por índice); texto blanco en la activa, `dim` en las demás; icono + nombre por celda.
- Props: `valor: Cara`, `onCambio(cara)`, `opciones: {id, nombre, icono}[]`.
- Accesible (`role="tablist"`/`aria-selected`), y responsive a 380 (no comprime).

### Nuevo — `web/lib/hitosEspacio.ts` (puro, testeable) + `.test.ts`
- `hitosDeEspacio(entrada) -> HitoEspacio[]`: dado el tipo de espacio (core|mundo), sus
  fechas de arranque/cierre y sus items completados, devuelve la lista **ordenada** de
  hitos con su estado (`alcanzado` | `pendiente`). Fuente única que comparten la UI y
  los tests (para que no envejezcan). Regla de partición: los hitos del core **no**
  incluyen mundos y viceversa (misma ley que `lib/espacios.ts`).

### Nuevo — `web/app/ui/LineaAvance.tsx` (la cara "Tu avance", presentacional)
- Lista vertical **sobria** (sin la animación de la Celebración grande, que es del
  proyecto): cada hito con su punto (verde=alcanzado / gris=pendiente), su etiqueta y su
  fecha humana. Consume `hitosDeEspacio`.

### Modificado — `web/app/ui/ManosALaObra.tsx` (ADITIVO, bajo riesgo)
- Estado local `cara: "plan" | "manos" | "avance"`, **default `"manos"`** (la ejecución
  es el uso principal; mínima disrupción). `useEffect` sobre `soloDominio` lo resetea al
  cambiar de espacio.
- Cuando el espacio **tiene plan** (core siempre; mundo solo si `plan_comprado`): render
  `<SelectorCara>` arriba + **una** cara:
  - `plan` → `PlanDocumento` (+ el diagnóstico del mundo).
  - `manos` → el bloque actual (rituales + checklist + cierre).
  - `avance` → `<LineaAvance>`.
- **Reemplaza** los acordeones "Tu plan"/"El plan de {mundo}"/"Tu diagnóstico" (MOD 3):
  ese contenido pasa a la cara **Plan**; se elimina la duplicación.
- Mundo **sin plan**: sin segmentado; el flujo de explorar/comprar de hoy, intacto.
- El gateo por `cara` es aditivo: la cara `manos` es el comportamiento actual.

### Modificado — `web/app/idea/[id]/IdeaView.tsx`
- Pasar a `ManosALaObra` lo que el **core "Tu avance"** necesita: `proyectoCreatedAt`
  (Chispa), `organizadorAt` (Claridad), `realizadaAt`. (Los del mundo ya viajan en
  `mundos`.)
- **Deep-link de la cara** (`?cara=plan|manos|avance`): recomendado, para volver a la
  misma cara y para que el gate capture cada una. (Puede empezar sin deep-link si el
  auditor prefiere alcance mínimo.)

### Modificado — `web/app/api/idea/[id]/route.ts`
- Exponer `idea.created_at` y `organizador.created_at` (dos campos; **sin migración**),
  para la Chispa y la Claridad del core. (Ver §4; opcional si se acepta el core sin
  esos dos hitos.)

## 6. Tests

- `hitosEspacio.test.ts` (a mano, fechas conocidas): la lista de hitos **exacta y
  ordenada** para un core y para un mundo sembrados; el core **no** trae hitos de mundo;
  un espacio sin cierre termina "en marcha"; una acción sin `completed_at` no aparece;
  partición (cada acción en su espacio).
- El segmentado y las caras son presentacionales; su selección se cubre con el estado y
  la regla "sin plan ⇒ sin segmentado".

## 7. Verificación (checkpoint)

- **tsc + suite completa + build** verdes.
- **Gate** (`gate_beta.ts`): ampliar la siembra del mundo (unlock + plan + checklist del
  dominio) y capturar **las 3 caras** del core y de un mundo, en dos viewports.
- **Vuelo de dinero**: sin cambio de contabilidad (esto no cobra); si la navegación del
  ciclo de mundo cambia de pasos, se actualiza.

## 8. Gobierno

- **BANCO §7.1** (decisión de la campaña): "cada espacio es un expediente de **tres
  caras** (Plan · Manos a la obra · Tu avance); 'Tu avance' son **hitos reales**, no
  estadística; 'Tu recorrido' queda reservado al árbol de conceptos".
- **Matriz de deltas del canon**: las 3 caras como "implementado, vara pendiente".
- **Brief a Design**: el segmentado + las 3 caras (con las capturas del gate).

## 9. Archivos

- **Nuevos:** `web/app/ui/SelectorCara.tsx`, `web/app/ui/LineaAvance.tsx`,
  `web/lib/hitosEspacio.ts` (+ `.test.ts`).
- **Modificados:** `web/app/ui/ManosALaObra.tsx`, `web/app/idea/[id]/IdeaView.tsx`,
  `web/app/api/idea/[id]/route.ts`, `web/scripts/gate_beta.ts`, `docs/BANCO_DE_TEXTOS.md`.
- **Sin migraciones** (todo sale de datos ya persistidos).

## 10. Riesgos y decisiones abiertas

- `ManosALaObra` es **código central de producción**; por eso el gateo por cara es
  **aditivo** (la cara `manos` = comportamiento actual), para minimizar riesgo de
  regresión.
- **Default de la cara:** `"manos"` (mínima disrupción). ¿O `"plan"` en la primera
  visita? Recomendación: `"manos"`, afinable.
- **Chispa/Claridad del core:** exponer dos campos en la ruta (recomendado) vs. arrancar
  el core en "Tu Plan" (alcance mínimo). Decisión del auditor/fundador.
- **Deep-link `?cara=`:** recomendado (gate + volver a la misma cara); puede diferirse.
