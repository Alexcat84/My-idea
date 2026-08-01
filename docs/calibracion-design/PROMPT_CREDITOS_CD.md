Eres el director de diseño de "My Idea", una app en español para emprendedores. Rediseña la pantalla `/creditos`: un **centro de saldo prepago**. Entrégame **2–3 OPCIONES** en HTML autocontenido, modo oscuro, cada una en 1240 y 380 px.

## Qué NO es (el error a evitar)
Esto **no** es una página de precios de suscripción (nada de niveles con listas de features tipo Linear/Stripe). Es una **billetera de créditos prepago y fungibles**: el usuario compra una cantidad y la gasta en el orden y en lo que él decida. Tres errores de la ronda pasada, PROHIBIDOS:
1. Presentar como "lo que recibes" cosas que **cuestan** créditos. Ejemplo real: recalcular / poner tu plan al día NO es gratis — es un seguimiento y cuesta 5.
2. Jerga técnica (Gantt, checklist, línea base…). El usuario JAMÁS ve términos de manual.
3. Quedar plano / simplista.

## Las 3 piezas de la pantalla
1. **Tu saldo** (el héroe): número grande de créditos + la promesa honesta *"Se verifica tu saldo al inicio de cada acción y se descuenta a la entrega; si algo falla a mitad, no se cobra nada."*
2. **Sumar créditos**: 4 tarjetas de **cantidad** (no de "nivel"). Mínimas: nombre, cantidad, precio, botón **Comprar**. Una sola señal social: Premium "el más elegido". **Sin listas de features en las cards.**
3. **En qué se gastan tus créditos**: el catálogo de costos **transparente y bello** (la pieza de confianza). Agrupado en tres cubetas, sin mentir.

## Los datos exactos
Recargas (cada pack es un viaje real, sin bonos por volumen):
- **Recarga** · 5 créditos · $4.99 · alcanza para un seguimiento o un mundo suelto
- **Básico** · 10 · $9.99 · tu plan completo (con Tus Números dentro)
- **Premium** · 15 · $14.99 · tu plan y tu primer seguimiento — **el más elegido**
- **Profesional** · 30 · $29.99 · el viaje entero de una idea

Las tres cubetas (nunca se cruzan; jamás presentar lo que cuesta como gratis o incluido):
- **GRATIS** (solo estas dos): la Claridad (tu idea ordenada, sin cuenta) y el diagnóstico de un mundo (su primer vistazo).
- **INCLUIDO en tu plan** (viene con Tu Plan de 10, no se cobra aparte): Tus Números, registrar tu avance, tus documentos, tu bitácora.
- **CUESTA créditos** (cada uso baja el saldo): Tu Plan 10 · un seguimiento de tu viaje 5 (⚠️ recalcular/poner tu plan al día ES un seguimiento → 5) · el plan de un mundo 5 · el seguimiento de un mundo 5.

Regla de una línea que lo resume: **"Tu plan: 10 créditos. Todo lo demás: 5. La Claridad y los diagnósticos: gratis."** El "alcanza para" es el puente honesto entre la cantidad y el viaje: va sutil (una línea de apoyo), no una lista de features.

## Sin jerga (traduce por función)
Gantt → "tus fechas de un vistazo" · checklist → "tus tareas / tus pasos" · línea base → "tus fechas de referencia" · cascada → "acomodar las fechas que siguen" · preview → "el primer vistazo / el diagnóstico" · dashboard → "tu tablero". Ante la duda: ¿lo diría alguien que nunca estudió administración? Si no, se traduce.

## Reglas visuales
- **Modo oscuro.** Fondo negro; superficies gris muy oscuro (#101013 / #17171b); hairlines translúcidos de 1px (rgba(255,255,255,.08)), no cajas pesadas; texto casi blanco (#f5f6f8), secundario gris (#a6a7ad).
- **Ley de color (lleva sentido, no adorna):** acento **azul #4d7cfe** (piensa/estructura), **verde #3fb950** (ejecuta/celebra — úsalo para lo gratis), **ámbar #e0a64a** (guarda, dato, nunca regaño). **NUNCA rojo.**
- **Color por paquete SIN romper la ley:** da identidad a las 4 recargas (acento en progresión tenue→pleno, o matiz muy sutil) cuidando que el verde no lea "compra celebrada" ni el ámbar "alerta". Premium "el más elegido" gana el ojo con anillo/acento/degradado azul.
- **Sin guiones largos** (— –) en el copy. Cifras alineadas (tabular-nums).
- **Estado beta:** la compra está por abrir; botón **Comprar** normal + aviso sobrio "se abre pronto", sin cartel de "cerrado" ni "beta" gritando.

## El tono (referencias, descritas — no las copies, supéralas)
- La transparencia de la **consola de créditos de una API** (saldo grande arriba, recarga simple, tarifas por acción claras): **confianza por transparencia**. Ese es el tono del catálogo de costos.
- Una **tienda de moneda** (se ve comprar una cantidad de una moneda), **pero SIN** bonos por volumen ni descuentos ocultos: cada pack es un viaje real y honesto. Esa honestidad es la marca.

## Entrega
2–3 opciones en HTML autocontenido (sin CDNs ni assets externos, iconos SVG en línea, UTF-8), cada una coherente en 1240 y 380 px, con una nota corta de la idea y el manejo del color. La riqueza viene del **oficio** (jerarquía, aire, el saldo como héroe, el catálogo de costos como artefacto considerado), no de inventar contenido.
