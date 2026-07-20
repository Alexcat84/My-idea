# Notas de decisiones — Lote 3: la beta viva

El criterio pantalla por pantalla. Formato de siempre: qué se decidió, por qué,
y qué NO se dibujó (propuestas que la app aún no hace, ley 5).

## 15 · Login por código

- **Sin nav.** La puerta no navega: solo marca, subtítulo y el formulario. El
  avatar N se mantiene como firma de la casa.
- **Paso B con 6 cajas** en vez de un campo con tracking: cada dígito tiene su
  casa, la caja activa lleva anillo azul. El código llega por correo; el CTA es
  "Entrar" y la salida única es "Pedir otro código o cambiar de correo".
- **No invitado va en AZUL informativo**, no ámbar: no es un error del usuario
  ni una pérdida, es una puerta que aún no se abre. Copy espejo: se sugiere
  confirmar el correo con quien invitó, sin culpa.
- **Código vencido va en ÁMBAR**: algo no funcionó y hay que decirlo. Espejo,
  nunca rojo; el CTA repara ("Pedirme un código nuevo").
- Correos de prueba largos y feos, como manda el formato.
- **No dibujado (propuesta):** la bienvenida de los 20 créditos de cortesía
  merece una línea en el primer aterrizaje en /ideas ("Tienes 20 créditos de
  cortesía para explorar"), no un modal. La app hoy no la muestra; queda como
  propuesta.

## 16 · La fila de potenciadores (4 estados)

- El estado vive en el **chip superior derecho** de la tarjeta; el footer dice
  el precio vivo. Ningún tachado, ningún "gratis en beta", ningún candado.
- Los 5 chips: "Se abre con tu plan" (gris hairline, pre-plan), "Explóralo
  gratis" (azul contorno), "Listo para tu plan" (azul lleno: es el único estado
  que pide acción del usuario y por eso el único chip sólido), "Activo · n/m"
  (verde contorno + barra de progreso verde: ejecución), "Completado" (verde
  con check: forma además de color).
- Frame 1 muestra la fila pre-plan (todos bloqueados); frame 2 la fila con el
  plan generado, donde los otros 4 estados conviven de verdad.
- El footer del activo cambia a progreso ("Plan activo · 2 de 9 acciones
  hechas") y el del completado a "Cerrado por ti · su checklist te espera
  igual" (§2.1 del banco: lo pendiente es testigo, no deuda).

## 17 · El escaparate del mundo

- El diagnóstico persistido con **borde azul** (es material del motor pensando)
  y la identidad del mundo en teal (borde izquierdo de la cabecera).
- **Sello híbrido** en el eyebrow: "hace un momento" recién generado, "ayer
  18:40" después (el frame móvil muestra la segunda cara a propósito).
- Tres secciones fijas con la prosa real del producto: Lo que encontré / Lo que
  un plan te estructuraría / Veredicto.
- CTA con el precio vivo y la ley de cobro visible: "3 créditos · se descuentan
  a la entrega". Debajo, la garantía de persistencia: el preview no se vuelve a
  pagar.

## 18 · La compuerta de Tus Números

- Una sola tarjeta con borde azul: activar es pedirle al motor que piense.
- **La ley se dice completa antes de cobrar, dentro de la tarjeta**: "Se activa
  una vez por idea. Después, corregir cifras y recalcular es gratis, siempre."
  más la garantía de cobro a la entrega. No hay letra chica.
- El copy de la promesa suma la credencial: "Los números los calcula código,
  no la IA" (claim verificable del banco §6).

## 19 · Tus Números, el tablero vivo

- **El sello "Tus números de HOY"** vive bajo el veredicto, con la fecha del
  último cálculo y la puerta "Corregir mis cifras · gratis" al lado. La palabra
  "gratis" viaja SIEMPRE pegada a corregir: es la ley de la compuerta cumplida.
- **Versiones anteriores**: una fila por versión con fecha híbrida, punto de
  color del veredicto, la palabra del veredicto y el margen con su color. La
  historia no se reescribe: el recálculo agrega, no reemplaza.
- **Modo lectura**: banda azul arriba ("Estás viendo tus números del 18 de
  julio, 08:25" + "Volver a hoy"). Sin sello HOY, sin enlace de corregir, y los
  textos en pasado ("ese día cobrabas $150"). El pasado se visita, no se edita.
  La caja de faltantes lo dice de frente: "Esta es una foto: para corregir
  cifras, vuelve a hoy."
- **Tu ciclo de caja**: el número grande (50 días) más una sola frase en
  palabras de persona. Sin desglose contable: eso es del recolector.
- **El recolector**: formulario de una columna (dos en desktop donde los pares
  son naturales), pre-llenado con las cifras vigentes, preguntas en palabras de
  persona ("¿Cuánto te cuesta hacer cada kit?"). El bloque "Tu ciclo de caja"
  es opcional y lo dice; cada campo de días lleva su porqué en una línea
  ("cobrar tarde aprieta tu caja"). CTA azul "Recalcular mis números · gratis"
  y la garantía de versiones debajo.
- El 14 del canon 2.0 (pérdida/sano) sigue siendo la vara de los veredictos;
  este 19 lo extiende, no lo reemplaza.

## 20 · El chip de saldo y el 402

- **El chip**: pill discreta, borde azul, junto a Potenciadores. Es la puerta
  al centro de créditos. Tres caras: azul con saldo (20, 3, da igual: el chip
  informa, no presiona), gris en cero. **Jamás parpadea ni cambia a ámbar**: la
  conversación del saldo ocurre donde ocurre la acción, no en el header.
- En móvil el chip **sobrevive fuera del menú**: saldo visible siempre.
- **El 402 va en AZUL, no ámbar.** El criterio: el ámbar es de los datos del
  negocio del usuario (pérdida, tardías, GIGO); quedarse sin créditos es un
  hecho del sistema con una puerta al frente. Nada se perdió y nadie hizo nada
  mal: informar y abrir la puerta es trabajo del azul.
- Anatomía fija del 402: **el hecho** con las dos cifras ("Te quedan 2
  créditos; esto cuesta 3."), **la garantía** ("Tu trabajo queda guardado tal
  como está", más la del contexto: el diagnóstico no caduca), y **la puerta**
  ("Ver mis créditos" primario, "Volver a mi plan" fantasma). El CTA original
  queda apagado, no desaparece: el usuario ve qué iba a pasar.

## 21 · La landing con sesión

- Sin sesión: "Iniciar sesión" (link) + "Comenzar" (botón azul). Con sesión:
  **"Mis ideas"** como botón fantasma, único elemento del nav: la landing deja
  de vender cuando ya te tiene.
- **La puerta del que regresa sin sesión** (el hueco que señala el encargo):
  una línea discreta bajo el CTA del hero: "¿Ya tienes ideas aquí? Inicia
  sesión y sigue donde ibas."
- **Propuesta (no existe en la app):** con sesión viva, una tarjeta de regreso
  bajo el hero con la última idea y su etapa ("Sigue donde ibas · Velas
  artesanales de soya · Tu Plan, listo"). Dibujada como propuesta a evaluar;
  si no se adopta, el botón "Mis ideas" del nav basta.

## 22 · El riel de redacción

- Tres estados de nodo, y solo tres: **escrita** (punto azul lleno + "escrita"),
  **escribiéndose** (anillo azul girando + "escribiéndose ahora"), **por
  escribir** (punto hueco y "Etapa N · por escribir": el título NO se inventa,
  aparece cuando existe; fallar ruidoso antes que mentir calladito).
- La línea del riel se pinta azul solo hasta donde hay etapas escritas.
- La tarjeta central muestra la prosa llegando con **cursor vivo** y la
  promesa de libertad: "Puedes quedarte a mirar o volver luego: tu plan te
  espera terminado."
- En el stepper superior, la etapa 4 lleva el anillo girando en lugar del
  punto: "Tu Plan · escribiéndose".
- En 380 el riel se pliega a la barra "Recorrido (2 de 5)" como en el canon 04.

## 07 · Potenciadores y Créditos (actualización, PILA 2)

- Saldo real: 20 con la etiqueta verde "cortesía de bienvenida" (verde: es un
  regalo entregado, no una promesa).
- Nueva tabla **"Lo que cuesta cada cosa"**: refleja precios.ts (5 / 3 / 2 / 2 /
  2 / 0), con la línea de "Registrar tu avance · Gratis, siempre" cerrando la
  tabla. Corrige de paso la errata del 2.0 (el seguimiento core cuesta 2, no
  es gratis).
- Los packs conservan su estructura con "$ —" por definir.
- La fila usa el modelo del preview (los 4 estados completos viven en el 16);
  la tarjeta de Tus Números dice su ley en el footer: "Una vez por idea ·
  corregir y recalcular: gratis".
