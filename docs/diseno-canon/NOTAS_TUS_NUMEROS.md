# NOTAS DE DECISIONES, pantalla nueva: Tus Números

Complemento de `NOTAS_DE_DECISIONES.md`. Esta pantalla convierte "Tus Números"
de una tarjeta de texto en la réplica financiera del Análisis del Proyecto:
misma familia visual, mismo peso, misma honestidad de espejo.

Archivo: `14_tus_numeros.html`. Cuatro `data-screen-label`, únicos y disjuntos
(ninguno prefijo de otro):
  - Tus Numeros perdida desktop
  - Tus Numeros perdida movil 380
  - Tus Numeros sano desktop
  - Tus Numeros sano movil 380

## La decisión de fondo: el ámbar tiene un segundo empleo canónico

La regla dice ámbar solo para el guardián de datos y las tardías. Aquí se
extiende, con el mismo espíritu: el ámbar también dice PÉRDIDA. Es el mismo
principio (espejo sin regaño), y por eso JAMÁS se usa rojo para el número
negativo. Un margen negativo no es una falta que reprochar, es un dato que
mostrar. Verde para el margen sano, azul para "faltan datos". Queda registrado
para que la implementacion no meta un rojo "porque es una pérdida".

## Dos estados, a propósito: el producto no solo da malas noticias

- Estado PÉRDIDA (velas de soya: cuesta 42, se vende a 38, margen menos 4). Es
  el caso que justifica la pantalla: hace visible el hueco.
- Estado SANO (kits de huerto: cuesta 180, se vende a 350, margen 170). Prueba
  que la misma pantalla celebra cuando toca, sin cambiar de gramática.
Entregar solo el estado malo habria dado un producto que solo regana.

## Seccion por seccion

1. Header + veredicto en UNA frase, con su color. La frase lleva el número clave
   coloreado (menos 4 en ámbar, 170 en verde) y explica el porqué en lenguaje de
   persona, no de contador. En pérdida deja claro que el problema es el precio,
   no el esfuerzo: desactiva de entrada la lectura de "vende más".

2. Tiles: costo por unidad, precio, margen por pieza, punto de equilibrio.
   Números grandes, labels dim, pie de contexto. El margen negativo va en ámbar;
   el sano en verde. En pérdida el punto de equilibrio dice "No hay" (con margen
   negativo no existe), en vez de un número falso o un infinito frio.

3. La barra de la verdad: costo y precio como dos barras horizontales CSS
   comparadas. En pérdida la barra de costo es la larga (ámbar) y sobresale de la
   de precio: ese sobrante es la pérdida, y se nombra. En sano se invierte: la de
   precio es la larga (verde) y la de costo llega a la mitad; el hueco es el
   margen. La misma figura cuenta las dos historias con solo cambiar cual barra
   es más larga.

4. Las palancas (el corazon nuevo): "Tres caminos para que estos números
   funcionen". Cada palanca es una tarjeta con su número YA calculado (subir a
   58, bajar a 24, vender 24) y un stepper visual del margen (carril + perno +
   marcas de "desde / hasta"). El stepper es estatico en el canon y se declara
   conceptual: interactivo después. Debajo, una frase que traduce el número a
   consecuencia ("a 58 tu margen pasa a más 16, cubres los 200 fijos con 13
   ventas").
   - Decisión honesta clave: en PÉRDIDA, la tercera palanca (vender más) NO se
     dibuja como una palanca más. Vender más con margen negativo agranda la
     pérdida. Se muestra en borde punteado, diciendo justo eso, y remite a
     arreglar primero el margen. Fingir que el volumen ayuda sería mentir con un
     gráfico bonito.
   - En SANO, la palanca de volumen si es valida y es la recomendada, con la meta
     de ganancia calculada.

5. Escenarios: tabla compacta con barras inline (pesimista, base, techo de
   capacidad). En pérdida las tres dan negativo (ámbar), que es la prueba visual
   de que el problema es estructural. En sano las tres son positivas y el techo
   lo pone el tiempo del fundador, dicho en la nota. En móvil la columna de barra
   se oculta y queda nombre + valor, para que la tabla no se rompa a 380.

6. Los números que te faltan: checklist de casillas, no párrafos. Lo que ya se
   tiene va con casilla verde marcada; lo pendiente con casilla azul vacia, cada
   una con su "porque importa" en una línea. Conecta con el guardián: son
   justamente los datos que, al entrar, cambian el resultado.

7. Guardián GIGO en su caja ámbar, como en Potenciadores. Aquí se personaliza:
   nombra que faltan el tiempo y el costo del puesto (pérdida) o el envío y la
   merma (sano), y advierte que el número real puede moverse. Cierra con la
   fórmula de siempre: no sustituye contabilidad ni asesoría fiscal.

## Reglas de entrega respetadas

- Un HTML autocontenido, abre por doble clic sin servidor, sin CDNs ni
  frameworks. Tokens en `:root`, clases semanticas en espanol, 2 espacios,
  comentarios de seccion, comentario indice de labels al inicio.
- Los cuatro frames en sus dos viewports (1240 y 380). Ni un frame sin su 380.
- Textos de prueba largos y feos (nombres de idea que truncan en el header, los
  "porque" de dos líneas). Cero guiones largos o medios.
- Barras, steppers y checklist son CSS y HTML puros: cero imagenes, cero libs.

## Lo que quedó conceptual (para implementacion)

- El stepper de cada palanca es estatico: dibuja el "desde" y el "hasta". La
  versión viva mueve el perno y recalcula el margen y la ganancia en tiempo real
  con la calculadora determinística (misma que hoy da los tiles). Todo el copy
  numerico ("más 16 por vela", "13 ventas", "2.880 al mes") sale de esa
  calculadora, no de la IA: el canon solo fija donde va cada número.
