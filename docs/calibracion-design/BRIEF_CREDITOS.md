# Brief de diseño — Créditos (centro de saldo + recarga de un consumible)

Rediseñamos la pantalla **`/creditos`**. Es un **centro de saldo prepago**: el
usuario ve **cuánto le queda**, **suma créditos** cuando quiere, y entiende
**en qué se gastan** — con calidad de alta industria en modo oscuro y nuestra
identidad de color. Pedimos **2–3 OPCIONES**.

> **Esta es la v2 del brief — corrige la primera ronda.** La opción 2a fue por
> buen camino en UNA cosa: separó *recargar* de *valor*, que es el patrón
> correcto de un consumible. Pero tuvo tres fallos que esta versión ataca de
> raíz, y son la razón del reencargo:
>
> 1. **Afirmaciones falsas.** La sección de beneficios quitó TODAS las cifras y
>    presentó como "lo que recibes" cosas que **cuestan créditos**. Ejemplo real:
>    *recalcular tu plan / poner tu proyecto al día NO es gratis* — es un
>    **seguimiento, y cuesta 5**. Un consumible se vende con **transparencia de
>    costo**, no escondiéndolo. Ver "Honestidad: gratis / incluido / cuesta".
> 2. **Jerga técnica.** Aparecieron "Gantt", etc. El fundador **combate** ese
>    idioma: el usuario jamás ve términos de manual. Ver "Sin jerga (obligatorio)".
> 3. **Demasiado simple.** El resultado quedó plano. La riqueza NO viene de
>    inventar listas de beneficios: viene del **oficio** (jerarquía, el saldo como
>    héroe, el catálogo de costos como una pieza bella y honesta). Ver "Qué diseñar".

## El modelo: un CONSUMIBLE, no una suscripción (esto lo cambia todo)

El error de la primera ronda nació de tratar esto como una **página de precios de
SaaS** (Linear, Stripe, Vercel: niveles con listas de features). **No es eso.** Es
una **billetera de créditos prepago y fungibles**: el usuario compra una cantidad
y la gasta **en el orden y en lo que él decida**. El patrón correcto tiene tres
piezas, y las tres importan:

1. **Tu saldo** (lo que tienes ahora) — el héroe.
2. **Sumar créditos** — tarjetas de **cantidad**, no de "nivel". Mínimas: nombre,
   cantidad, precio, botón. Una sola señal social ("el más elegido"). **No** llevan
   lista de features (eso es lenguaje de suscripción y fue el origen del error).
3. **En qué se gastan tus créditos** — el **catálogo transparente de costos**. Es
   la pieza de CONFIANZA del modelo (y la que 2a borró). Aquí se ve, sin mentir,
   qué es gratis, qué viene incluido con el plan, y qué cuesta cada acción.

**Referencias correctas (por su MODELO, no las de suscripción):**
- **Créditos prepago de API** — la **consola de Anthropic** y la de **OpenAI**:
  saldo grande arriba, "añadir créditos" simple, y una tabla de tarifas por acción
  **radicalmente transparente**. Ese es el tono: confianza por transparencia.
- **RevenueCat — Virtual Currency** (la pasarela que usaremos): billetera fungible,
  paquetes de recarga.
- **Tiendas de moneda virtual** (Game UI Database → "Currency Store / IAP"): buena
  referencia de *cómo se ve comprar una cantidad de una moneda*. **PERO** ellos usan
  **bonos por volumen** ("paga 375k, llévate 325k gratis"): nosotros **NO**. Nuestro
  catálogo es **congruente y honesto** — cada pack ES un viaje real, sin trucos. Esa
  honestidad es la marca; no la copiemos, superémosla.

## Para quién y dónde

- **Pantalla `/creditos`**, con su propio menú (separada de Potenciadores). Es donde
  vive TODO lo del dinero.
- **Usuario:** alguien que trabaja su idea y necesita ver de un vistazo cuánto le
  queda, cuánto sumar, y en qué se irá — **sin fricción ni jerga**. Móvil primero
  (380) y escritorio (1240).
- **Estado beta:** la compra con dinero está **DORMIDA** (las pasarelas llegan
  después); el saldo se siembra a mano. El diseño se ve "comprable" (botón
  **Comprar** normal), con un aviso **sobrio** de que la compra se abre pronto — sin
  cartel de "cerrado" ni "beta" gritando.

## Reglas de la casa (no negociables)

- **Modo oscuro**, tokens de la casa (`--surface`, `--surface-2/3`, `--border`
  hairline, `--text`, `--text-dim`, `--accent` azul, `--done` verde). **Hairlines,
  no cajas pesadas**; sombra solo en capas flotantes.
- **Ley de color:** el **azul piensa/estructura**, el **verde ejecuta y celebra**,
  el **ámbar guarda** (dato, no regaño), el **gris es lo que falta**. **Nunca rojo.**
  El color lleva sentido, no adorna.
- **Sin guiones largos** (— –) en copy visible. Cifras en `tabular-nums`.
- **Copy de dinero:** respeta `docs/BANCO_DE_TEXTOS.md` (§6.1: ninguna afirmación de
  dinero sin respaldo). Nada de promesas de retorno.
- **Autocontenido:** sin CDNs ni assets externos; iconos SVG en línea; UTF-8; HTML.

## Honestidad: gratis / incluido / cuesta (el corazón de esta v2)

Todo lo que se muestre cae en **exactamente una** de tres cubetas. Nunca se cruzan.
Esta es la corrección central: **jamás presentar algo que cuesta como si viniera
incluido o gratis.**

**① GRATIS — sin costo (SOLO estas dos, y nada más lleva la palabra "gratis"):**
- **La Claridad** — tu idea ordenada. Sin cuenta, sin tarjeta.
- **El diagnóstico de un mundo** — su primer vistazo.

**② INCLUIDO en tu plan — viene con Tu Plan (10), no se cobra aparte:**
- **Tus Números** — el tablero de tu idea; corregir cifras y volver a calcular,
  cuando quieras.
- **Registrar tu avance** y tus notas.
- **Tus documentos** (en .md y PDF) y **tu bitácora**.

**③ CUESTA créditos — cada uso baja tu saldo (el precio se ve, sin esconderlo):**
- **Tu Plan** (La Exploración): **10**.
- **Un seguimiento de tu viaje**: **5**. ⚠️ *Poner tu plan al día / recalcular
  desde donde estás ES un seguimiento → cuesta 5. NO es gratis ni "incluido".*
- **El plan de un mundo**: **5**.
- **El seguimiento de un mundo**: **5**.

Regla de una línea que resume todo: **"Tu plan: 10 créditos. Todo lo demás: 5. La
Claridad y los diagnósticos: gratis."** Los créditos son **fungibles**: se narra por
lo que **"alcanza para"**, jamás como derechos cerrados ("incluye 3 seguimientos"
implicaría un contador de bundle que no existe).

## Sin jerga (obligatorio)

El usuario **jamás** ve términos de manual (regla dura del BANCO §7.1, "etiquetas de
cara"). Si una palabra huele a software o a consultoría, se traduce por su **función**
en palabras de persona:

| jerga (NO usar) | cómo se dice en casa |
|---|---|
| Gantt | tus fechas de un vistazo · el mapa de tus fechas |
| checklist | tus tareas · tu lista de pasos |
| línea base | tus fechas de referencia · el punto de partida |
| cascada | acomodar las fechas que siguen |
| dashboard | tu tablero |
| token / créditos del motor | crédito |
| KPI | indicadores |
| preview | el primer vistazo · el diagnóstico |
| recalcular (a secas) | poner tu plan al día |

(El diccionario completo vive en `docs/BANCO_DE_TEXTOS.md` §7.1. Ante la duda:
¿lo diría un emprendedor que nunca estudió administración? Si no, se traduce.)

## Los datos exactos (leídos de `lib/precios.ts`, jamás hardcodear)

**Las 4 recargas — catálogo congruente (cada pack = un viaje real):**

| Pack | Créditos | Precio | Alcanza para |
| --- | --- | --- | --- |
| **Recarga** | 5 | **$4.99** | un seguimiento o un mundo suelto |
| **Básico** | 10 | **$9.99** | tu plan completo (con Tus Números dentro) |
| **Premium** | 15 | **$14.99** | tu plan y tu primer seguimiento — **el más elegido** |
| **Profesional** | 30 | **$29.99** | el viaje entero de una idea |

El "alcanza para" es el **puente honesto** entre la cantidad y el viaje (una moneda
fungible necesita ese ancla). Va **sutil** — una línea de apoyo, no una lista de
features. Puede vivir en la card o en el catálogo de costos; tú decides dónde queda
más limpio, pero **debe existir**.

**El saldo (cabecera):** número grande + la promesa honesta ya vigente: *"Se
verifica tu saldo al inicio de cada acción y se descuenta a la entrega. Si algo
falla a mitad, no se cobra nada."* (se puede reformular, no perder).

## Qué diseñar (pedimos 2–3 OPCIONES)

Contra lo "simplista": la riqueza viene del **oficio**, no de inventar contenido.
Cada opción, coherente en 1240 y 380, con estas tres piezas:

1. **Tu saldo (el héroe).** El número manda; la promesa de "no se cobra si algo
   falla" con peso de compromiso, no de nota al pie. Trabájalo: es lo primero que
   el usuario quiere ver.
2. **Sumar créditos — 4 recargas mínimas.** Nombre, cantidad, precio, **Comprar**.
   Una sola señal social: **Premium** "el más elegido" (anillo/acento/degradado
   sutil, azul). **Color por paquete SIN romper la ley:** proponnos cómo dar
   identidad a los cuatro (acento en progresión tenue→pleno, o matiz muy sutil)
   cuidando que el verde no lea "compra celebrada" ni el ámbar "alerta". **No**
   listas de features en las cards.
3. **En qué se gastan tus créditos — el catálogo de costos como pieza BELLA.** Esta
   es la que sube el listón (y la que 2a borró). Agrúpalo por las **tres cubetas**
   (gratis / incluido con tu plan / cuesta), cada línea con su estado claro: lo
   gratis en verde, lo incluido como "ya tuyo", el costo con su cifra sin esconderla.
   Que se lea de un vistazo y transmita **confianza por transparencia** (el tono de
   la consola de Anthropic/OpenAI). Aquí el usuario entiende su billetera y elige
   cantidad por SUS prioridades — sin que le digamos qué comprar.

Opcional (si suma sin recargar): un micro-explicador **"cómo funcionan tus
créditos"** (son tuyos, no caducan, los gastas en el orden que quieras).

**Qué NO hacer:** nada de "1 crédito = 1 dólar"; nada de tarjetas de recarga con
listas de features (es lenguaje de suscripción); **nunca** presentar lo que cuesta
(seguimientos, mundos) como beneficio incluido o gratis; nada de jerga (Gantt,
checklist, línea base…); nada de bonos por volumen ni "descuentos ocultos"; nada de
cobro mensual (es prepago consumible).

## Entrega esperada

- **HTML autocontenido** por opción (modo oscuro), en **1240 y 380**, con
  `tokens_creditos.md` (valores usados) y un `notas.md` corto por opción (la idea y
  el manejo del color).
- Nombres claros (`creditos_opcion_a_1240.html`, `..._380.html`, …).
- Sin CDNs ni assets externos; iconos SVG en línea; UTF-8.

Referencia del **estado actual** (el punto de partida, no el objetivo):
`creditos_estado_actual.html` (en esta carpeta). Cuando elijas dirección, Claude
Code la implementa leyendo de `precios.ts` (cero números hardcodeados) y respetando
el BANCO.
