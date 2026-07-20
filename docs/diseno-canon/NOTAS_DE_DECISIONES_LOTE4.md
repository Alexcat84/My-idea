# Notas de decisiones, lote 4

Los porqués, pantalla por pantalla. Lo que no está aquí sigue la vara de los
lotes anteriores.

## 23 · El centro de cuenta

- **Una sola columna de tarjetas (max 760px), sin héroe.** /cuenta es una
  pantalla de administración, no de trabajo: se lee de arriba abajo en el
  orden del riesgo (quién eres, cómo te proteges, qué tienes, qué puedes
  perder). El borrado de cuenta va al final, siempre.
- **La verificación en dos pasos es el corazón** y por eso es la única tarjeta
  que muta (7 estados). Los otros bloques no cambian entre estados: menos
  ruido para QA visual y para el diff del canon.
- **Estados que las capturas no traían, diseñados por descripción:**
  - *Activada con correo*: mismo patrón que "activada con app", solo cambia el
    método tras el punto medio y la frase de qué pasará al entrar. Un patrón,
    dos métodos: nada nuevo que aprender.
  - *El candado (423)*: aviso ámbar de bloque (punto + texto), input y CTA
    dormidos. Se dice la espera en palabras y se promete que nada se pierde.
    Es fricción de seguridad, no castigo: espejo, jamás regaño.
  - *El código no coincide*: error inline en ámbar BAJO el input (el ojo ya
    está ahí), borde del campo en ámbar, y el botón sigue despierto porque
    reintentar es el camino. El aviso de bloque queda reservado al candado.
- **Borrar una idea: confirmación inline, no modal.** La pregunta completa
  ("¿Borrarla para siempre?") aparece en la propia fila con "Sí, borrar" en
  ámbar y "Cancelar" neutro. En 380 la confirmación baja a su propia línea
  debajo del nombre: el título de la idea nunca se tapa (la captura de la app
  muestra esa colisión; va en HALLAZGOS).
- **Borrar la cuenta: escribir ELIMINAR habilita el botón.** ELIMINAR va en
  mono ámbar tanto en la instrucción como en el campo: la confirmación es
  literal, se copia lo que se lee. El botón vive dormido (opacidad), nunca
  oculto: la salida existe y se ve.
- **Los créditos solo se asoman.** Decisión del fundador: el centro sigue en
  /potenciadores. Aquí, saldo en una frase y una puerta azul ("Ver mi centro
  de créditos"). Nada de packs ni precios en /cuenta.
- **El QR es utilería** dibujada en canvas (patrón determinístico con los tres
  buscadores): el mockup abre por file sin red y no promete un secreto real.

## 24 · El desafío del login

- **Misma puerta que el 15**: marca, subtítulo, sin nav. El desafío es la
  continuación del login, no otra pantalla; el usuario no debe sentir cambio
  de lugar.
- **Un solo campo centrado, no 6 cajitas.** Las cajitas del 15 celebran el
  código que te acaba de llegar por correo; aquí el código se copia de otra
  app y un campo único con letter-spacing es más rápido de pegar y de leer.
- **El botón Verificar nace dormido** (azul al 30%) y despierta con el código
  completo. El estado dormido usa el mismo azul: es el mismo botón esperando,
  no otro botón.
- **El alternador es un enlace, no un botón**: "No tengo mi código: usar uno
  de rescate" / "Volver al código normal". Cambiar de método es una salida
  lateral, no una acción principal.
- **La variante correo agrega "Reenviarme el código" como fantasma**: existe
  sin competir con Verificar.
- **El rescate va en mono de 12** con marcador XXXXXXXXXXXX (12, exactos: los
  códigos del 23 tienen 12). La promesa de un solo uso se repite aquí porque
  es el momento donde importa.

## 15 v2 · El login con Google

- **La puerta nueva no toca la vieja**: el correo y su CTA azul quedan
  intactos arriba; debajo, divisor hairline con "o" y el botón de Google
  (glifo oficial multicolor, borde hairline, fondo superficie 1). El azul
  sigue siendo del código: Google no compite en jerarquía.
- **El no invitado conserva el correo a la vista.** La app lo quitó; el canon
  lo mantiene porque el dato accionable es QUÉ correo no está en la lista
  (con Google también lo sabemos). La copy ahora dice que la lista es la
  misma para las dos puertas.
- **La nota al pie ahora nombra las dos puertas** sin alargarse: "con su
  código de un solo uso o con tu cuenta de Google. Sin contraseñas."

## 07 v3 · Potenciadores y Créditos

- **El "$ —" murió**: packs 5 · 15 · 30 a $4.99 / $14.99 / $29.99, cada uno
  con su frase de persona ("tu plan completo", "el viaje completo de una
  idea", "dos ideas trabajadas"). El 15 hereda el destacado azul y "el más
  elegido".
- **La ley comercial se narra con orgullo, no con letra chica**: banda propia
  a lo ancho del panel, "Un crédito es un dólar, siempre." en texto pleno,
  seguida del porqué (sin descuentos por volumen) y del cuándo (la compra con
  dinero se abre muy pronto).
- **Precio sin botón de compra**: la compra no está activa en beta, así que
  las tarjetas muestran precio y nada más. Ningún CTA fantasma que no lleve a
  ningún lado.
- **El resto de la pantalla no se tocó**: tabla "lo que cuesta cada cosa",
  fila de potenciadores y "Tus Números, por dentro" siguen tal cual el lote 3
  (la captura 07v3 sugiere derivas en la app; van en HALLAZGOS, no las adopto
  sin decisión).
