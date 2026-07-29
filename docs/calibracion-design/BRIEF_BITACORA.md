# Brief de diseño — La bitácora del cliente (página en vivo)

**Qué es:** la historia completa del viaje de una idea, del inicio al cierre,
contada como línea de tiempo. Existe como **documento** (.md/PDF en el panel de
Tus documentos) y ahora como **PÁGINA en vivo** que el usuario ve antes de
imprimir.
**Estado actual (primera versión funcional):**
`web/examples/gate-canon/bitapage_pagina.png` (la página).
**Cómo se entra:** la tarjeta "Mi bitácora" con su botón "Ver mi bitácora" vive
como **primer punto del aside** (arriba a la derecha) en las páginas de
DESARROLLO: el plan (`bitaentry_plan.png`), Manos a la Obra (`bitaentry_manos.png`)
y los mundos. NO vive en el panel de documentos (ese solo descarga .md/PDF).
**Componentes:** `web/app/ui/Bitacora.tsx` (página), `web/app/ui/DocumentoPapel.tsx`
(versión impresa/PDF). El texto sale de `lib/bitacoraCliente.ts` (una sola verdad).

## Qué hay que diseñar

Volver **bella** la página (hoy es correcta pero básica). Encabezado, la barra
de tiempo, los nodos, el ritmo visual. También cómo se lee impresa (PDF).

## Anatomía actual (respetarla, embellecerla)

- **Encabezado:** eyebrow "TU HISTORIA" + título **"Mi bitácora de mi viaje"** +
  el nombre de la idea entre comillas + el rango de fechas. Botones "Descargar
  .md" e "Imprimir / PDF".
- **Línea de tiempo:** una **barra vertical continua** con un **punto por cada
  timestamp/actividad**. Cada **día** abre su encabezado con un **aro** sobre la
  barra; cada **entrada** es un **punto lleno** con su texto (y la hora, solo en
  los días con 2+ entradas). La barra pasa por el **centro** de los puntos.

## Lo que la bitácora narra (para calibrar el ritmo/jerarquía)

Cada decisión del usuario, en voz de persona: encendiste la chispa, ordenaste la
idea, exploraste, recibiste el plan, sellaste tu línea base, elegiste tu modo,
calculaste Tus Números, cambiaste el estado de una tarea (empezar/en
proceso/hecha/retirar con motivo/reactivar), moviste fechas (con cascada:
"y las N siguientes, X días después"), anotaste algo, trabajaste tus mundos
(explorar/diagnóstico/comprar/completar), y realizaste/reabriste tu idea.

**Idea para Design:** los distintos tipos de evento podrían tener un matiz o
icono que ayude a escanear (hito de fase vs acción diaria vs cierre), SIN meter
mecánica interna ni romper la voz. Es opcional; la vara la pone Design.

## Restricciones

- **Tema oscuro**, tokens de `web/app/tokens.css`. Azul para la barra/nodos;
  verde solo para el cierre/celebración si se quiere marcar el final.
- **La barra debe atravesar el centro de los puntos** (fue un reclamo explícito
  del fundador; ver `riel_v3.png` para el patrón correcto de la versión impresa).
- **Sin guiones largos**; **sin jerga ni nodos/grafos**; los motivos del usuario
  van entre comillas, tal cual los escribió.
- **Dos viewports** (1240 y 380).
- **Confidencialidad y honestidad:** solo eventos que son historia del usuario
  (lista blanca); lo no registrado no se inventa.

## La versión impresa (PDF)

Sale de `DocumentoPapel` (tokens de papel: superficies claras, tinta oscura,
identidad conservada). Abre con "# La historia de [idea]" + rango, y la secuencia
por día. Design puede proponer cómo se ve en papel (misma alma, medio distinto).

Entrega esperada: mockups de la PÁGINA (1240 y 380) y, si se anima, del PDF,
listos para que Claude Code los implemente.
