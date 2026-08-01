# Brief de diseño — Créditos (centro de manejo + compra, calidad de alta industria)

Rehacemos por completo la pantalla **`/creditos`** ("Tus créditos"). Hoy se ve
como una lista funcional; la queremos como un **centro de créditos de alta
industria**: un lugar donde el usuario **maneja su saldo** y **compra créditos**,
con la presentación pulida de las mejores páginas de precios en modo oscuro, pero
con **nuestra identidad de color**. Pedimos **2–3 OPCIONES** visuales.

> **La decisión que dispara el rediseño (fundador):** fuera el marco "**un
> crédito = un dólar, siempre**" y "los packs no esconden descuentos". No tiene
> lógica de cara al usuario: nadie compra "dólares disfrazados de créditos". Los
> paquetes deben presentarse por **VALOR / lo que logras con ellos**, como una
> página de precios profesional — no por una equivalencia unitaria.

## Para quién y dónde

- **Pantalla:** `/creditos`, con su propio menú (separada de Potenciadores: cada
  proceso en su carril). Es donde vive TODO lo del dinero.
- **Usuario:** alguien que ya trabaja su idea y necesita entender, de un vistazo,
  cuánto le queda, qué puede comprar, y qué cuesta cada cosa — sin fricción ni
  jerga. Móvil primero (380) y escritorio (1240).
- **Importante:** la **compra con dinero está DORMIDA** en la beta (las pasarelas
  llegan después); hoy el usuario trabaja con una **cortesía de bienvenida**. El
  diseño debe verse "comprable" pero contemplar el estado beta (los packs se ven,
  con un aviso sobrio de que la compra se abre pronto).

## Reglas de la casa (no negociables)

- **Modo oscuro**, tokens de la casa (`surface`, `surface-2/3`, `hairline`,
  `dim`, `ink`, `accent`). **Hairlines, no cajas pesadas**; sombra solo en capas
  flotantes.
- **Ley de color:** el **azul piensa/estructura**, el **verde ejecuta y celebra**,
  el **ámbar es el guardián**, el **gris es lo que falta**. **Nunca rojo.** Los
  colores llevan sentido; no se usan de adorno. (Ojo con esto al colorear los
  paquetes — ver "Qué diseñar", punto 2.)
- **Sin jerga ni mecánica interna** (nada de "tokens del motor", conteos internos,
  nombres técnicos). Palabras de persona.
- **Sin guiones largos** en el copy visible. Cifras en `tabular-nums`.
- **Copy de dinero:** respeta el `docs/BANCO_DE_TEXTOS.md` (§6 registro de claims
  y §6.1: ninguna afirmación de dinero sin respaldo). Nada de promesas de retorno.
- **Autocontenido:** sin CDNs, sin fuentes/imágenes externas, iconos SVG en línea,
  UTF-8. Entregar en HTML como las tandas anteriores.

## Qué datos YA existen (anclar el diseño, cero invención)

**Saldo / manejo (cabecera):**
- El **saldo** en créditos (número grande).
- La **cortesía de bienvenida** (etiqueta): con qué nació la cuenta.
- Regla honesta ya vigente: *"Se verifica tu saldo al inicio de cada acción y se
  descuenta a la entrega. Si algo falla a mitad, no se cobra nada."* (esto SÍ se
  queda, es un compromiso real; se puede reformular pero no perder).

**Los 3 paquetes de compra** (leídos de `lib/precios.ts` → `PACKS`, jamás
hardcodear números):

| Créditos | Precio | Lo que logras | Nota |
| --- | --- | --- | --- |
| 5  | **$4.99**  | tu plan completo | — |
| 15 | **$14.99** | el viaje completo de una idea | **el más elegido** (destacar) |
| 30 | **$29.99** | dos ideas trabajadas | — |

**Lo que cuesta cada cosa** (leído de `PRECIOS`, jamás hardcodear):

| Cosa | Costo |
| --- | --- |
| El organizador (Claridad) — tu idea ordenada | **Gratis, siempre** |
| La Exploración — la entrevista y tu plan completo | 5 |
| El plan de un mundo — *el preview (entrevista + diagnóstico) es gratis* | 3 |
| Seguimiento del viaje principal — recalcular tu plan desde donde estás | 2 |
| Seguimiento de un mundo — recalcular su checklist | 2 |
| Tus Números — *una vez por idea; corregir cifras y recalcular es gratis* | 2 |
| Registrar tu avance — marcar hecho, notas, progreso | **Gratis, siempre** |

## Referencias de la industria (el listón)

Modo oscuro, tipografía con jerarquía, un acento disciplinado. Buenos ejemplos
del patrón que buscamos (por su estructura, no para copiar): **Linear**, **Vercel**,
**Stripe**, **Raycast**, **Cursor**, **Framer**. Lo que hacen bien y queremos:

- **Tarjetas de nivel** claras, alineadas, con jerarquía de precio fuerte (el
  número manda) y una lista corta de "lo que incluye/logras".
- **Un nivel destacado** ("el más elegido") con anillo/acento y, a veces, un
  degradado sutil — sin gritar.
- **Aire generoso**, alineación impecable, acento usado con moderación (no todo
  colorido).
- **Un ancla de valor** honesta (qué logras), no una tabla de equivalencias.
- Una sección de "qué cuesta cada cosa" **legible de un vistazo** (no un muro).

## Qué diseñar (pedimos OPCIONES)

Danos **2–3 opciones** de la pantalla completa (cabecera + packs + costos), cada
una coherente en 1240 y 380. Ejes a explorar:

1. **Cabecera de manejo (saldo):** cómo presentar el saldo + la cortesía + la
   regla de "no se cobra si algo falla", con peso de "centro de cuenta", no de
   nota al pie. ¿Barra superior de resumen? ¿Tarjeta ancla a la izquierda?
2. **Los 3 packs como niveles, con COLOR POR PAQUETE — respetando la ley.** Aquí
   está el reto: queremos una **identidad de color por paquete**, pero sin romper
   el significado de los colores. Propón cómo resolverlo. Opciones que vemos:
   - un **acento por nivel en progresión** (tenue → pleno) manteniendo el azul
     como base y el destacado con el acento más fuerte; o
   - **matiz frío-a-cálido** muy sutil (el más grande, "dos ideas", con un matiz
     de crecimiento) cuidando que el verde no lea como "compra celebrada" ni el
     ámbar como "alerta". Tú tienes el criterio: enséñanos la forma correcta.
   - El **"más elegido"** debe ganar el ojo (anillo/acento/degradado sutil).
3. **"Lo que cuesta cada cosa":** la forma más clara y profesional de mostrar la
   tabla — que **lo gratis** (organizador, registrar avance) se lea como valor, y
   que **los mundos** se entiendan (qué es "el plan de un mundo", que su preview
   es gratis). ¿Filas con hairline? ¿Agrupado (viaje principal / mundos / extras)?
4. **El estado beta:** cómo mostrar que la compra "se abre pronto" sin matar el
   deseo (los packs se ven comprables; un aviso sobrio, no un cartel de "cerrado").

**Qué NO hacer:** nada de "1 crédito = 1 dólar", nada de "sin descuentos
ocultos", nada de tabla de equivalencias unitarias. Nada de suscripción recurrente
(el modelo es de **créditos consumibles**, se compran por paquete; presentación de
página de precios, sí; cobro mensual, no).

## Entrega esperada

- **HTML autocontenido** por opción (modo oscuro), en **1240 y 380**, con
  `tokens_creditos.md` (los valores que uses) y un `notas.md` corto por opción
  explicando la idea y el manejo del color.
- Nombres claros (`creditos_opcion_a_1240.html`, `..._380.html`, etc.).
- Sin CDNs ni assets externos; iconos SVG en línea; UTF-8.

Cuando elijas la dirección, yo la implemento en el front leyendo de `precios.ts`
(cero números hardcodeados) y respetando el BANCO.
