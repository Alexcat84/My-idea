# PROMPT PARA CLAUDE DESIGN — El canon de la APK de My Idea

> Para el fundador: copia de aquí hacia abajo. Todo lo de arriba es contexto de
> este repo. La sección final ("Lo que NO debes hacer") es la que más importa:
> son los errores concretos que este proyecto ya pagó.

---

Necesito el **canon visual de la APK Android de My Idea**. Es un paquete de
mockups nuevo, hermano del que ya entregaste para la web (11 pantallas, que
sigue vigente y **no se toca**).

## 1. Qué es My Idea

Un espacio de trabajo donde una persona con una idea de negocio la convierte en
un plan y lo ejecuta. No es un chatbot: es **un árbol que piensa contigo**. El
usuario cuenta su idea en sus palabras (o la dicta), el sistema la entrevista, y
de esa conversación nace un plan con acciones concretas que después tacha en el
mundo real.

**El viaje son 5 etapas, y estos son sus únicos nombres válidos:**

1. **La Chispa** — cuenta tu idea
2. **Claridad** — el sistema te la devuelve organizada
3. **La Exploración** — la entrevista, con el árbol creciendo al lado
4. **Tu Plan** — el plan en etapas con su entregable
5. **Manos a la Obra** — el checklist que se ejecuta

Además hay **mundos** (paquetes que se activan con créditos: "Calidad y
Confianza", "Seguridad y Personas", "Riesgos Bajo Control"…). Un mundo es un
**subproyecto completo**: tiene su exploración, su plan, su checklist, su
seguimiento y su cierre propios, dentro del proyecto.

Frases del producto: *"Transforma tu creatividad en acción."* · *"De la chispa a
la realidad."* · *"Aquí acaba tu idea y nace tu proyecto."*

## 2. El encargo, y por qué existe

Hoy la APK no existe. El plan era envolver la web en un WebView. **El fundador
lo rechazó, como fundador y como cliente usuario: «eso no sirve, se satura».**
Envolver el scroll de la web y llamarlo app da una app que no se ve como una app.

El problema real, medido, no opinado:

- La web a 380px **no tiene navegación**: ni menú que se despliegue, ni barra
  inferior, ni nada colapsable.
- Todo es **un scroll único y larguísimo**: la pantalla "Manos a la Obra" a 380
  mide **~3.100px** de alto. El Análisis, ~1.700. El ritual de fechas, más.
- El header **trunca el nombre de la idea** ("Kits de hue…") para que quepan el
  breadcrumb y el stepper de 5 puntos.
- Todo lo que en escritorio vive en una **columna lateral** (el análisis, cerrar
  la idea, el ritmo, el ciclo de profundización) cae **al fondo de la página**,
  a 2.500px del pulgar.

**El encargo:** la APK **luce como APK**, aunque por dentro inyectemos la web.
Tendrá **componentes nativos**. Ya lo hicimos así en otro producto del mismo
fundador (una app de I Ching) y funcionó.

## 3. La frontera (esto es arquitectura, no estilo)

- **Nativo** = caparazón: navegación, barras del sistema, botón atrás, splash,
  permisos, compras, sesión.
- **Web inyectada** = el producto: la Chispa, el árbol, el plan, el checklist,
  los mundos.
- **Toda la inteligencia vive en el servidor.** El cliente no decide nada de
  negocio.

El caparazón nativo ya existe como patrón probado y aporta: botón atrás del
sistema, safe areas (notch y barra de gestos), barras del sistema edge-to-edge,
splash de app, pantallas nativas propias, y un puente para hablarse con la web.

**Tu trabajo es decidir, pantalla por pantalla, qué es caparazón y qué es
producto** — y dibujar los dos, marcando cuál es cuál.

## 4. Tokens (obligatorios, sin excepción)

| Token | Valor |
|---|---|
| Azul primario | `#4D7CFE` |
| Verde ejecución | `#3FB950` |
| Ámbar guardián | `#E0A64A` |
| Matiz de los mundos | `#3A9B8F` |
| Fondo base | `#0A0A0C` / `#000000` |
| Superficie 1 (tarjetas) | `#101013` |
| Superficie 2 (campos, hover) | `#17171B` / `#141419` |
| Texto | `#F5F6F8` |
| Texto dim | `#A6A7AD` |
| Hairline (bordes) | `rgba(255,255,255,0.08)` |

Tipografía: **Inter**.

**La regla de color, que es de significado y no de gusto: EL AZUL PIENSA, EL
VERDE EJECUTA.** Azul = exploración, planeación, posibilidad (etapas 1-4,
navegación, chips informativos, el anillo "pensando"). Verde = acción sobre el
mundo real (etapa 5, el progreso del checklist, "esta semana", los contadores
X/N). El ámbar es **solo** para el guardián de datos. El matiz de los mundos no
es ni azul ni verde: los mundos tienen tono propio.

**Los estados completados se distinguen también por FORMA** (check lleno, texto
tachado), nunca solo por color.

## 5. La voz

- Palabras de persona, jamás de máquina. El usuario nunca ve maquinaria.
- Nada de regaños. Si el usuario va tarde, el sistema **lo dice sin juzgar**: el
  tono es espejo, no látigo.
- **Sin cifras inventadas.** Si un mockup muestra un número, es del usuario.
- Cero jerga. "Manos a la Obra", no "En marcha". Nunca claves técnicas
  (`quality` es "Calidad y Confianza", siempre).

## 6. Las pantallas que necesito

**Todas a 380px de ancho** (el viewport real del teléfono), y donde tenga
sentido, su variante de tablet.

**Del caparazón nativo:**

1. **La navegación**. El problema central. ¿Qué reemplaza al header que trunca?
   ¿Barra inferior, drawer, ambas? ¿Dónde viven "Mis ideas", la idea actual, el
   Análisis, los mundos? El stepper de 5 puntos ocupa medio header a 380: ¿se
   queda, se colapsa, se mueve?
2. **Splash / arranque.**
3. **El paso entre pantallas** (cómo se siente que es una app y no un navegador).

**Del producto (la web inyectada), rediseñadas para el pulgar:**

4. **La Chispa** — el micrófono es la razón de ser de la APK: *"una idea nace en
   un preciso momento"*. Aquí no se degrada nunca.
5. **La Exploración** — hoy el árbol vive en una columna lateral que a 380 no
   cabe. ¿Dónde va?
6. **Tu Plan.**
7. **Manos a la Obra** — la peor: 3.100px de scroll. Etapas plegables, la acción
   de la semana, y **todo lo que hoy cae al fondo** (análisis, cerrar la idea,
   ritmo, "Contar qué pasó") necesita casa.
8. **La sección de un mundo activo**, dentro de Manos a la Obra: su checklist, su
   "Contar qué pasó", su cierre.
9. **La Celebración** — el timeline del viaje, con su pulso. Es el momento
   emocional del producto.

**Marca en cada pantalla qué es nativo y qué es web inyectada.**

## 7. Formato de entrega (esto es literal, y hay una razón)

Igual que el paquete de la web: **HTML autocontenido, que abra por `file://`**,
con cada vista dentro de un frame que lleve **`data-screen-label`**.

**Convención de las etiquetas, obligatoria:** el label termina en el viewport.

- `"Manos a la Obra mobile 380"`
- `"Navegacion nativa mobile 380"`

Y si una etiqueta es **prefijo** de otra, difieren desde el principio, no al
final (`"Plan mobile 380"` y `"Plan mobile 380 con mundo"` ya nos cruzaron un par
una vez).

**Por qué literal:** tenemos un instrumento automático que abre tu HTML, recorta
cada frame por su `data-screen-label` y lo pone **al lado de la app real** en la
misma medida. Tu entrega no es una referencia: **es la vara contra la que se mide
el código**. Si el label no calza, la comparación se cruza en silencio.

## 8. Lo que NO debes hacer (errores que este proyecto ya pagó)

- **No inventes números ni contenido de relleno.** Los mockups anteriores
  usaron ítems cortos y bonitos ("Habla con 5 cafeterías"); el producto real
  genera frases de tres líneas. **Diseña con textos largos y feos**, que son los
  de verdad. Si el diseño solo funciona con texto corto, no funciona.
- **No dejes ningún frame sin su variante 380.** El paquete de la web trae
  `mobile 380` en 10 de 11 pantallas, y el instrumento pasó **siete fases sin
  mirarlos**. Aprendimos la lección: *una vara que el instrumento no mira es
  decoración*.
- **No cambies los nombres de las 5 etapas ni los de los mundos.**
- **No rompas la regla del azul y el verde** para que algo "se vea mejor".
- **No diseñes un menú que necesite saber de negocio.** El caparazón navega; no
  decide.
- **No asumas que hay que mostrarlo todo.** El problema de hoy no es que falte
  información: es que sobra a la vez.

## 9. Qué te pido de vuelta, además del HTML

Una nota corta con **las decisiones que tomaste y por qué**: qué mandaste a
nativo y qué dejaste en la web, qué se colapsa, qué se fue a un segundo nivel, y
**qué recortaste**. Esa nota vale tanto como los frames: es lo que evita que la
implementación reinterprete tu criterio.
