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

> **El principio comercial (2.ª decisión del fundador — clave):** lo que hoy
> decimos "**gratis para siempre**" (registrar el avance, el seguimiento) **NO se
> anuncia como gratis: se vende como parte de lo que INCLUYE la compra.** Al
> comprar el plan, compras tu plan **y** el seguimiento completo del desarrollo de
> tu idea, el acompañamiento hasta convertirla en proyecto y su cierre — porque
> eso es lo que la app hace de verdad. Lo mismo en cada mundo: incluye su
> seguimiento, igual que el viaje principal. Esto sostiene un precio mayor por
> entregable (el fundador subirá el costo en créditos del plan y de los mundos).
>
> **Lo ÚNICO que se declara gratis: el primer vistazo** — el término ya existe en
> la app: **Claridad** (el organizador del viaje principal, sin cuenta) y **el
> diagnóstico** (el escaparate de un mundo: su entrevista + su diagnóstico). Nada
> más se nombra "gratis"; todo lo demás va "incluido en tu compra".

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

**El primer vistazo — lo ÚNICO gratis** (nombres canónicos, ya en la app):

| Gratis | Qué es |
| --- | --- |
| **Claridad** (viaje principal) | tu idea ordenada: la frase, lo que tienes, lo que asumes. Sin cuenta. |
| **El diagnóstico** (un mundo) | el escaparate del mundo: su entrevista y su diagnóstico. |

**Lo que compras — y TODO lo que incluye** (leído de `PRECIOS`, jamás hardcodear;
los números están **en revisión al alza** — ver nota):

| Compra | Incluye | Costo (en revisión) |
| --- | --- | --- |
| **Tu Plan** (La Exploración) | tu plan completo · el seguimiento de tu idea hasta el cierre · el registro de tu avance · el acompañamiento hasta volverla proyecto | 5 → posible alza |
| **Un mundo** | el plan del mundo · su seguimiento hasta el cierre (igual que el viaje principal) | 3 → posible alza |
| **Tus Números** | el reporte de sostenibilidad de tu idea; corregir cifras y recalcular, incluido | 2 |

> **Nota de precios (fundador):** el seguimiento y el registro **dejan de ser
> líneas "gratis" sueltas** — se absorben en lo que incluye el plan / el mundo.
> Por eso el costo del plan y de los mundos **sube** (el mundo podría igualarse a
> **3** para estandarizar, ahora que incluye su seguimiento como el principal).
> Los números finales los fija el fundador y yo los pongo en `precios.ts`; el
> diseño solo debe dejar espacio para que el número cambie y para la lista de
> "incluye". **No** repartir el valor en varias filas baratas: **una compra, todo
> incluido**.

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
3. **"Qué incluye cada compra" (no "qué cuesta cada cosa"):** el eje del rediseño.
   Mostrar cada compra (Tu Plan, Un mundo, Tus Números) con **su lista de "incluye"**
   como valor visible — que se sienta un paquete completo (plan + seguimiento +
   acompañamiento a proyecto), no un cargo suelto. Aparte, sobrio, **el primer
   vistazo gratis** (Claridad · el diagnóstico) como puerta de entrada, no como
   "línea gratis" que abarate. Ojo: el número debe poder cambiar sin romper el
   layout, y la lista de "incluye" es la estrella (una compra, todo dentro).
4. **El estado beta:** cómo mostrar que la compra "se abre pronto" sin matar el
   deseo (los packs se ven comprables; un aviso sobrio, no un cartel de "cerrado").

**Qué NO hacer:** nada de "1 crédito = 1 dólar", nada de "sin descuentos
ocultos", nada de tabla de equivalencias unitarias. **No anunciar "gratis para
siempre"** el seguimiento ni el registro del avance: van *incluidos* en la compra,
no como líneas gratis que abaraten el valor (lo único gratis: el primer vistazo,
Claridad · el diagnóstico). No repartir una compra en varias filas baratas. Nada
de suscripción recurrente (el modelo es de **créditos consumibles**, se compran
por paquete; presentación de página de precios, sí; cobro mensual, no).

## Entrega esperada

- **HTML autocontenido** por opción (modo oscuro), en **1240 y 380**, con
  `tokens_creditos.md` (los valores que uses) y un `notas.md` corto por opción
  explicando la idea y el manejo del color.
- Nombres claros (`creditos_opcion_a_1240.html`, `..._380.html`, etc.).
- Sin CDNs ni assets externos; iconos SVG en línea; UTF-8.

Cuando elijas la dirección, yo la implemento en el front leyendo de `precios.ts`
(cero números hardcodeados) y respetando el BANCO.
