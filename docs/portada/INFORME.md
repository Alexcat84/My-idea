# Portada: la masa (rama `portada-particula`)

La muestra híbrida aprobada, llevada a la portada real: una masa líquida
oscura (raymarching) que se disgrega en partículas, forma una figura
(foco, lente, brújula, escalera, casa) y vuelve a fundirse. Ciclo, figuras,
paleta y encuadre salen de `particula-hibrida-my-idea.html`; el respaldo de
solo partículas sale de `particula-my-idea.html`.

**No se funde nada:** el merge lo decide el fundador después de verlo en
su teléfono.

## Qué cambió en el hero

- El lema y su animación desaparecen. El título queda como `<h1>` oculto a
  la vista (solo lectores de pantalla y buscadores):
  "My Idea: transforma tu creatividad en acción".
- **Comenzar gratis** se mantiene, discreto, en el borde inferior.
- Se retiran el campo de estrellas y el wordmark de partículas del hero.
- La masa queda centrada en los dos ejes y dimensionada sobre el **lado
  menor** del hero (80 %), sin recortarse nunca en el borde.
- Fuera del hero, un solo cambio: el tipeo simulado de "Cómo funciona" se
  aisló en su propio componente. Antes re-renderizaba la landing entera
  cada 55 ms y en móvil se comía el hilo principal (ver "Rendimiento").

## Dónde vive el código

`web/app/ui/portada/`

| Archivo | Qué hace |
|---|---|
| `HeroMasa.tsx` | Decide el nivel y monta el motor tras la primera pintura (evento `load` + reposo del hilo). Pausa con la pestaña oculta y con el hero fuera de pantalla. No importa three.js. |
| `masa/anfitrion.ts` | Lado del hilo principal: transfiere el lienzo como `OffscreenCanvas` a un worker; si el navegador no puede, corre el motor en el hilo principal. |
| `masa/trabajador.ts` | El worker: crea el contexto WebGL2, detecta GPU por software y corre el motor. |
| `masa/motor.ts` | El motor three.js (niveles alto, medio, bajo). Sin DOM. |
| `masa/glsl.ts` | Los shaders: líquido, composición, partículas, acabado y respaldo. |
| `masa/respaldo.ts` | Respaldo de solo partículas en WebGL1 crudo, sin three.js. |
| `masa/ciclo.ts`, `encuadre.ts`, `calidad.ts`, `figuras.ts` | Lógica pura: ciclo, encuadre, niveles y figuras. |
| `public/portada/masa-reposo.webp` | La imagen fija (19 KB), renderizada del propio motor en reposo. |

### El material

- **Líquido.** Una piel sobre una esfera con fbm y deformación de dominio en
  dos escalas: una ondulación lenta y grande, y un temblor fino y rápido.
  Iluminación física aproximada: fresnel de Schlick con dispersión por
  canal en el borde, dos luces (clave ceniza y contraluz violeta), reflejo
  de un entorno procedural oscuro, oclusión ambiental por SDF y un brillo
  interior tenue que respira. El aura es analítica y el borde lleva
  antialias. Núcleo oscuro, borde ceniza y violeta.
- **Partículas.** Nacen en la piel, viajan con ruido de rizo (el rotacional
  de un potencial de ruido simplex, así que el flujo no tiene fuentes ni
  sumideros), dejan estelas cortas y forman la figura con bordes nítidos.
  De regreso se apagan al tocar la superficie mientras la masa vuelve a
  crecer, sin corte visible. La masa oculta a las partículas que quedan
  detrás de ella.
- **Acabado.** Bloom suave (three.js `UnrealBloomPass`), grano de película
  proporcional a la luz y viñeta que solo oscurece. El negro del núcleo
  sigue en negro.

### Niveles de calidad

| Nivel | Cuándo | Líquido | Partículas |
|---|---|---|---|
| alto | escritorio | 72 pasos, 3 octavas, AO de 4 muestras, 0,75 de resolución, bloom | 14 000, rizo de 2 pasos |
| medio | móvil | 44 pasos, 2 octavas, AO de 2 muestras, 0,6 de resolución, bloom | 7 000, rizo de 1 paso |
| bajo | equipo débil o tras una caída | 30 pasos, sin AO, 0,42 de resolución, sin bloom | 4 000 |
| particulas | sin WebGL2, GPU por software o bajo que no se sostiene | — | 5 000 a 11 000 (respaldo WebGL1) |
| fija | sin WebGL, o partículas que no se sostienen | imagen quieta | — |

Adaptativo: tras 0,7 s de calentamiento se mide la mediana de fps durante
2,6 s. Si no alcanza el mínimo del nivel (45, 38, 28 y 24 fps) baja un
nivel y vuelve a medir. `prefers-reduced-motion` muestra el líquido quieto
en un solo fotograma.

Para verificar: `?masa=alto|medio|bajo|particulas|fija` fuerza un nivel
(sin adaptar) y `?masa-t=<segundos>` congela el ciclo en ese instante.

### Guardas contra el fallo de las muestras (dos cosas con el mismo nombre)

- ESLint, solo para `ui/portada`: `no-shadow`, `no-redeclare`,
  `no-use-before-define` y `no-var`. En el desarrollo atrapó tres casos
  reales.
- `masa/glsl.test.ts` revisa el texto de cada shader. Falla si un nombre
  global se repite, si una variable local tapa un global o una función, si
  un nombre choca con GLSL o con lo que three.js antepone (como `normal`),
  o si un shader no declara exactamente los uniformes que el motor le da.
  El motor tipa sus uniformes con esas mismas listas, así que TypeScript
  exige que estén todos.

## Verificación en navegador real

Los scripts están en `docs/portada/verificacion/` y se corren desde la raíz
del repo con el servidor levantado, por ejemplo
`node docs/portada/verificacion/capturar.mjs http://localhost:3000 salida`.
Usan Playwright con Chromium sobre la GPU real (ANGLE/D3D11, Intel Iris Xe).

### Capturas (`capturas/`, build de producción)

Tres anchos (390, 768 y 1440) por tres momentos del ciclo (reposo, mitad de
la disgregación y figura formada), más un mosaico con las otras cuatro
figuras, el respaldo de partículas, el nivel bajo y el modo sin movimiento.
También está la imagen del nivel fijo.

Geometría medida sobre los píxeles de cada captura, con el botón oculto
para medir. Es la caja de lo que brilla, como fracción del lado menor del
hero. El desvío es la distancia entre el centro de esa caja y el centro del
hero:

| Ancho | Momento | Nivel | Caja (ancho × alto) | Desvío del centro | Toca el borde |
|---|---|---|---|---|---|
| 390 | reposo | medio | 0,79 × 0,79 | 3 / 7 px | no |
| 390 | disgregación | medio | 0,96 × 0,93 | 1 / 5 px | no |
| 390 | figura (foco) | medio | 0,72 × 0,80 | 0 / 2 px | no |
| 768 | reposo | medio | 0,80 × 0,79 | 4 / 13 px | no |
| 768 | disgregación | medio | 0,97 × 0,95 | 5 / 4 px | no |
| 768 | figura (foco) | medio | 0,72 × 0,80 | 1 / 2 px | no |
| 1440 | reposo | alto | 0,80 × 0,83 | 8 / 10 px | no |
| 1440 | disgregación | alto | 0,97 × 0,97 | 9 / 8 px | no |
| 1440 | figura (foco) | alto | 0,73 × 0,81 | 1 / 2 px | no |

La figura formada mide el 80 % del lado menor y queda centrada a ±2 px. La
masa en reposo es orgánica: 79 % a 83 %, con un desvío de pocos píxeles
según hacia dónde se abulta. En vuelo las partículas llegan al 97 % sin
tocar el borde.

**Consola: sin errores ni avisos** (página y workers) en los tres anchos,
las cinco figuras, los niveles y el modo sin movimiento. La única
excepción: con GPU por software (SwiftShader) Chrome emite su propio aviso
de rendimiento del controlador, "GPU stall due to ReadPixels", al componer
el lienzo. No es un error de shader ni de JavaScript.

### Cuadros por segundo

| Perfil | Nivel elegido | fps (mediana, 5 s) |
|---|---|---|
| Escritorio 1440 × 900 (Intel Iris Xe) | alto | 60 |
| Móvil 390 × 844, dpr 3, CPU ×4 | medio | 60 |
| Móvil, fases congeladas (reposo, disgregación, figura, regreso) | medio | 60 en todas |

Cadena adaptativa comprobada:

- Escritorio con GPU por software: arranca directo en `particulas` (60 fps).
- Sin WebGL: `fija`.
- Con el motor en el hilo principal y CPU ×20: bajó alto → medio → bajo →
  partículas, y se quedó ahí a 30 fps.
- Con el worker, el estrangulamiento de CPU del hilo principal ya no afecta
  al motor: se sostiene en alto.

### Peso

Medido en el navegador, en bytes (gzip entre paréntesis):

| | Antes (`main`) | Después |
|---|---|---|
| JS inicial de la portada | PESO_BASE | 806 480 (220 502) |
| Diferido, motor de líquido (three.js + motor + worker) | — | 592 738 (151 632) |
| Diferido, respaldo de partículas | — | 26 067 (10 120) |
| Diferido, imagen fija | — | 19 314 |

three.js y el motor nunca entran en el bundle inicial. Se descargan después
del evento `load`, en reposo y dentro del worker. Un equipo que cae a
partículas o a la imagen fija no descarga three.js.

### Lighthouse (rendimiento, local, build de producción)

Medianas de 3 corridas antes y de 5 (móvil) o 3 (escritorio) después:

| | Puntuación | LCP | TBT | FCP | Speed Index | CLS |
|---|---|---|---|---|---|---|
| Móvil antes | 72 | 6,70 s | 216 ms | 1,66 s | 2,44 s | 0 |
| Móvil después | **77** | 6,62 s | 59 ms | 1,51 s | 1,57 s | 0 |
| Escritorio antes | 97 | 1,26 s | 18 ms | 0,41 s | 0,77 s | 0 |
| Escritorio después | **97** | 1,23 s | 0 ms | 0,37 s | 0,41 s | 0 |

En esas corridas el Chrome de Lighthouse cargó el motor completo (el
líquido, en el worker). El LCP móvil de 6,6 s ya estaba antes y no es de la
masa: el elemento LCP es un enlace del nav o del botón y lo retrasa la
simulación de red con el JS de la página.

Cómo se llegó ahí:

1. Una primera versión en el hilo principal bajó el móvil a 64. Dos causas
   medidas: la compilación de los shaders en ANGLE/D3D terminaba en el
   primer dibujo y bloqueaba el hilo 0,5 a 1,1 s, y crear el contexto
   WebGL2 costaba 126 a 168 ms.
2. El primer arreglo precompila todo y hace el primer dibujo por etapas,
   esperando a la GPU con una valla que no bloquea.
3. El arreglo de fondo mueve el motor a un worker con `OffscreenCanvas`.

## Pendiente o a decidir

- `app/layout.tsx` sigue cargando la fuente Instrument Serif, que solo usaba
  el lema. Quitarla ahorra una descarga de fuente en cada página, pero toca
  el layout global. Queda a decisión del fundador.
- Los fps de móvil se midieron con perfil emulado (viewport, dpr y CPU ×4)
  sobre la GPU de este equipo. La prueba de verdad es el teléfono del
  fundador; el nivel elegido y las caídas quedan en los atributos
  `data-nivel`, `data-fps` y `data-descartes` del contenedor
  `.portada-masa`.
