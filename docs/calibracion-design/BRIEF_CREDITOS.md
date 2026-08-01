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

> **El principio comercial (ANÁLISIS §4, ya implementado):** lo que hoy decimos
> "**gratis para siempre**" (registrar el avance, los documentos, los recálculos)
> **NO se anuncia como gratis: se dice "incluido" con lo que ya compraste.** La
> única inclusión-de-producto real es **Tus Números dentro del plan** (el plan
> cuesta 10 e incluye Tus Números). El **seguimiento** NO va incluido: es un
> concepto aparte de 5 créditos —lo que hace congruente el catálogo (los packs
> ES un paquete real: Premium 15 = plan 10 + un seguimiento 5). Los créditos son
> **fungibles**; los packs se narran por lo que **"alcanza para"**.
>
> **Lo ÚNICO que se declara gratis: el primer vistazo** — el término ya existe en
> la app: **Claridad** (el organizador del viaje principal, sin cuenta) y **el
> diagnóstico** (el escaparate de un mundo: su entrevista + su diagnóstico). Nada
> más se nombra "gratis"; lo que no cobra pero ya compraste va **"incluido"**.

## Para quién y dónde

- **Pantalla:** `/creditos`, con su propio menú (separada de Potenciadores: cada
  proceso en su carril). Es donde vive TODO lo del dinero.
- **Usuario:** alguien que ya trabaja su idea y necesita entender, de un vistazo,
  cuánto le queda, qué puede comprar, y qué cuesta cada cosa — sin fricción ni
  jerga. Móvil primero (380) y escritorio (1240).
- **Importante:** la **compra con dinero está DORMIDA** en la beta (las pasarelas
  llegan después); ya NO hay cortesía automática, el usuario trabaja con créditos
  que el fundador le siembra a mano. El diseño debe verse "comprable" pero
  contemplar el estado beta (los packs se ven, con un aviso sobrio de que la
  compra se abre pronto).

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
- El saldo se siembra a mano en la beta (sin etiqueta de cortesía): el número es real.
- Regla honesta ya vigente: *"Se verifica tu saldo al inicio de cada acción y se
  descuenta a la entrega. Si algo falla a mitad, no se cobra nada."* (esto SÍ se
  queda, es un compromiso real; se puede reformular pero no perder).

**Los 4 packs — el catálogo congruente (ANÁLISIS §4, YA es ley)** (leídos de
`lib/precios.ts` → `PACKS`, jamás hardcodear números). Cada pack ES un paquete
real de trabajo (congruencia exacta), y se narra por lo que **"alcanza para"**,
nunca como derechos cerrados:

| Pack | Créditos | Precio | Alcanza para | Nota |
| --- | --- | --- | --- | --- |
| **Recarga** | 5 | **$4.99** | un seguimiento o un mundo suelto | — |
| **Básico** | 10 | **$9.99** | tu plan completo, con Tus Números incluidos | — |
| **Premium** | 15 | **$14.99** | tu plan y tu primer seguimiento | **el más elegido** (destacar) |
| **Profesional** | 30 | **$29.99** | el viaje entero de una idea | — |

**El primer vistazo — lo ÚNICO gratis** (nombres canónicos, ya en la app):

| Gratis | Qué es |
| --- | --- |
| **Claridad** (viaje principal) | tu idea ordenada: la frase, lo que tienes, lo que asumes. Sin cuenta. |
| **El diagnóstico** (un mundo) | el escaparate del mundo: su entrevista y su diagnóstico. |

**Lo que cuesta cada cosa** (leído de `PRECIOS`; la regla de una línea: *"tu plan
10, todo lo demás 5, la Claridad y los diagnósticos gratis"*):

| Cosa | Costo |
| --- | --- |
| **Tu Plan** (La Exploración) — incluye **Tus Números** | **10** |
| **Seguimiento** del viaje principal | **5** |
| **El plan de un mundo** (su diagnóstico ya fue gratis) | **5** |
| **Seguimiento** de un mundo | **5** |
| **Tus Números** | **incluido con tu plan** (0) |
| **Registrar** tu avance, documentos y bitácora | **incluido con tu paquete** |

> **Marco comercial (ANÁLISIS §4/§7/§8, ya implementado en el código):** los
> créditos son **fungibles** (una billetera). Los packs se narran por lo que
> **"alcanza para"**, JAMÁS como "incluye 3 seguimientos" (eso implicaría un
> contador de bundle que no existe). La palabra **"gratis"** se reserva a la
> Claridad y a los diagnósticos; lo que no cobra pero ya compraste se dice
> **"incluido"**. El único inclusión-de-producto real es **Tus Números dentro del
> plan**. Nada de "1 crédito = 1 dólar" en la cara del usuario.

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

1. **Cabecera de manejo (saldo):** cómo presentar el saldo + la regla de "no se
   cobra si algo falla", con peso de "centro de cuenta", no de nota al pie. (Ya
   NO hay "cortesía de bienvenida": la beta corre con precios reales.) ¿Barra
   superior de resumen? ¿Tarjeta ancla a la izquierda?
2. **Los 4 packs como niveles (Recarga · Básico · Premium ⭐ · Profesional), con
   COLOR POR PAQUETE — respetando la ley.** El reto: una **identidad de color por
   paquete** sin romper el significado de los colores. Opciones que vemos:
   - un **acento por nivel en progresión** (tenue → pleno) manteniendo el azul
     como base y el destacado con el acento más fuerte; o
   - **matiz frío-a-cálido** muy sutil (el más grande, "el viaje entero", con un
     matiz de crecimiento) cuidando que el verde no lea como "compra celebrada"
     ni el ámbar como "alerta". Tú tienes el criterio: enséñanos la forma correcta.
   - **Premium (el más elegido)** debe ganar el ojo (anillo/acento/degradado sutil).
   - Cada card lleva su narración **"alcanza para"** (fungible, no derechos cerrados).
3. **"Lo que cuesta cada cosa":** la forma más clara y profesional de la tabla.
   Que **Tu Plan (10)** se lea con **Tus Números DENTRO** (la única inclusión real);
   que **lo gratis** (Claridad · el diagnóstico) sea la puerta de entrada; que **lo
   incluido** (registrar, documentos, bitácora) se lea como valor ya tuyo. El
   **seguimiento y los mundos son 5 cada uno** — líneas honestas, NO "incluidas".
4. **El estado beta:** cómo mostrar que la compra "se abre pronto" sin matar el
   deseo (los packs se ven comprables; un aviso sobrio, no un cartel de "cerrado").

**Qué NO hacer:** nada de "1 crédito = 1 dólar", nada de "sin descuentos
ocultos", nada de tabla de equivalencias unitarias. **No anunciar "gratis para
siempre"** el registro / los documentos / los recálculos: van *incluidos* con lo
que ya compraste (lo único gratis: Claridad · el diagnóstico). El **seguimiento
NO es "incluido"**: es su propia línea de 5. No repartir el PLAN en varias filas
baratas (Tus Números va dentro). Nada de "incluye 3 seguimientos" (los créditos
son fungibles: se narra "alcanza para"). Nada de suscripción recurrente (el modelo
es de **créditos consumibles**; presentación de página de precios, sí; cobro
mensual, no).

## Entrega esperada

- **HTML autocontenido** por opción (modo oscuro), en **1240 y 380**, con
  `tokens_creditos.md` (los valores que uses) y un `notas.md` corto por opción
  explicando la idea y el manejo del color.
- Nombres claros (`creditos_opcion_a_1240.html`, `..._380.html`, etc.).
- Sin CDNs ni assets externos; iconos SVG en línea; UTF-8.

Cuando elijas la dirección, yo la implemento en el front leyendo de `precios.ts`
(cero números hardcodeados) y respetando el BANCO.
