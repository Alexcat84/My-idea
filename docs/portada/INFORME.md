# Portada: la masa (rama `portada-particula`)

La muestra híbrida aprobada, llevada a la portada real: una masa líquida
oscura (raymarching) que forma una figura (foco, lente, brújula, escalera,
casa) y vuelve a fundirse. Ciclo, figuras, paleta y encuadre salen de
`particula-hibrida-my-idea.html`. El respaldo de solo partículas, para
equipos débiles, sale de `particula-my-idea.html`.

**Decisiones del fundador posteriores al brief (23 sep):**

- Las figuras se forman con **la misma materia**, sin partículas: el
  líquido fluye, se estira y se vuelve la figura.
- La materia se mueve **más rápido** y de forma **más agresiva**.

Las partículas quedan solo en el respaldo para equipos que no sostienen el
líquido.

**No se funde nada:** el merge lo decide el fundador después de verlo en
su teléfono.

## Qué cambió en el hero

- El lema y su animación desaparecen. El título queda como `<h1>` oculto a
  la vista (solo lectores de pantalla y buscadores):
  "My Idea: transforma tu creatividad en acción".
- **Comenzar gratis** se mantiene, discreto, en el borde inferior.
- Se retiran el campo de estrellas y el wordmark de partículas del hero.
- La masa y las figuras quedan centradas en los dos ejes y dimensionadas
  sobre el **lado menor** del hero (80 %), sin recortarse nunca en el borde.
- Fuera del hero, un solo cambio: el tipeo simulado de "Cómo funciona" se
  aisló en su propio componente. Antes re-renderizaba la landing entera
  cada 55 ms y en móvil se comía el hilo principal.

## Dónde vive el código

`web/app/ui/portada/`

| Archivo | Qué hace |
|---|---|
| `HeroMasa.tsx` | Decide el nivel y monta el motor tras la primera pintura (evento `load` + reposo del hilo). Pausa con la pestaña oculta y con el hero fuera de pantalla. No importa three.js. |
| `masa/anfitrion.ts` | Lado del hilo principal: transfiere el lienzo como `OffscreenCanvas` a un worker; si el navegador no puede, corre el motor en el hilo principal. |
| `masa/trabajador.ts` | El worker: crea el contexto WebGL2, detecta GPU por software y corre el motor. |
| `masa/motor.ts` | El motor three.js (niveles alto, medio y bajo). Sin DOM. |
| `masa/glsl.ts` | Los shaders: la materia (masa y figura), composición, acabado y respaldo. |
| `masa/figuras.ts` | Los trazos de las cinco figuras y su campo de distancia con signo (transformada exacta de Felzenszwalb y Huttenlocher, suavizada). |
| `masa/respaldo.ts` | Respaldo de solo partículas en WebGL1 crudo, sin three.js. |
| `masa/ciclo.ts`, `encuadre.ts`, `calidad.ts` | Lógica pura: ciclo, encuadre y niveles. |
| `public/portada/masa-reposo.webp` | La imagen fija (24 KB), renderizada del propio motor en reposo. |

### La materia

**Masa.** Una piel sobre una esfera, con fbm y deformación de dominio en
dos escalas: una ondulación grande y un temblor fino y rápido. Su reloj va
×1,7 respecto de la muestra y la amplitud es mayor, para un movimiento más
vivo y agresivo, sin salir del 96 % del lado menor.

**Figura.** Cada trazo del icono se vuelve un tubo de líquido: un campo de
distancia en 2D (textura de 256 × 256) se extruye en 3D con sección
redonda. Un temblor corre también por los tubos.

**Transformación.** La superficie que se dibuja interpola entre la piel de
la masa y la figura. En el medio se estira y se retuerce con ruido extra,
así que aparecen lóbulos y a veces una gota que se desprende. La masa gira;
la figura formada mira de frente.

**Luz.** Fresnel de Schlick con dispersión por canal en el borde, dos luces
(clave ceniza y contraluz violeta), reflejo de un entorno procedural
oscuro, oclusión ambiental por SDF y un brillo interior tenue que respira.
El aura es analítica: alrededor de la masa, y en el plano de la figura
alrededor de sus tubos. El borde lleva antialias. Núcleo oscuro, borde
ceniza y violeta.

**Acabado.** Bloom suave (three.js `UnrealBloomPass`), grano de película
proporcional a la luz y viñeta que solo oscurece. El negro sigue en negro.

### Niveles de calidad

| Nivel | Cuándo | La materia |
|---|---|---|
| alto | escritorio | 80 pasos, 3 octavas, AO de 4 muestras, 0,75 de resolución, bloom |
| medio | móvil | 52 pasos, 2 octavas, AO de 2 muestras, 0,6 de resolución, bloom |
| bajo | equipo débil o tras una caída | 36 pasos, sin AO, 0,42 de resolución, sin bloom |
| particulas | sin WebGL2, GPU por software o bajo que no se sostiene | respaldo de partículas (WebGL1, sin three.js) |
| fija | sin WebGL, o partículas que no se sostienen | imagen quieta |

Adaptativo: tras 0,7 s de calentamiento se mide la mediana de fps durante
2,6 s. Si no alcanza el mínimo del nivel (45, 38, 28 y 24 fps) baja un
nivel y vuelve a medir. `prefers-reduced-motion` muestra la masa quieta en
un solo fotograma.

Para verificar: `?masa=alto|medio|bajo|particulas|fija` fuerza un nivel
(sin adaptar) y `?masa-t=<segundos>` congela el ciclo en ese instante.

### Guardas contra el fallo de las muestras (dos cosas con el mismo nombre)

- ESLint, solo para `ui/portada`: `no-shadow`, `no-redeclare`,
  `no-use-before-define` y `no-var`. En el desarrollo atrapó tres casos
  reales.
- `masa/glsl.test.ts` revisa el texto de cada shader. Falla si un nombre
  global se repite, si una variable local tapa un global o una función, si
  un nombre choca con GLSL o con lo que three.js antepone (como `uv` o
  `normal`), o si un shader no declara exactamente los uniformes que el
  motor le da. Atrapó un `uv` local en el shader de la figura. El motor
  tipa sus uniformes con esas mismas listas, así que TypeScript exige que
  estén todos.

## Verificación en navegador real

Los scripts están en `docs/portada/verificacion/` y se corren desde la raíz
del repo con el servidor levantado, por ejemplo
`node docs/portada/verificacion/capturar.mjs http://localhost:3000 salida`.
Usan Playwright con Chromium sobre la GPU real (ANGLE/D3D11, Intel Iris Xe).

### Capturas (`capturas/`, build de producción)

Tres anchos (390, 768 y 1440) por tres momentos del ciclo (reposo, mitad de
la transformación y figura formada), más un mosaico con las otras cuatro
figuras, el nivel bajo, el modo sin movimiento y el respaldo de
partículas. También está la imagen del nivel fijo.

Geometría medida sobre los píxeles de cada captura, con el botón oculto
para medir. Es la caja de lo que brilla, como fracción del lado menor del
hero. El desvío es la distancia entre el centro de esa caja y el centro del
hero:

| Ancho | Momento | Nivel | Caja (ancho × alto) | Desvío del centro | Toca el borde |
|---|---|---|---|---|---|
| 390 | reposo | medio | 0,78 × 0,77 | 2 / 2 px | no |
| 390 | transformación | medio | 0,67 × 0,77 | 10 / 2 px | no |
| 390 | figura (foco) | medio | 0,74 × 0,83 | 1 / 1 px | no |
| 768 | reposo | medio | 0,79 × 0,78 | 3 / 2 px | no |
| 768 | transformación | medio | 0,67 × 0,77 | 26 / 6 px | no |
| 768 | figura (foco) | medio | 0,74 × 0,82 | 1 / 1 px | no |
| 1440 | reposo | alto | 0,80 × 0,82 | 6 / 7 px | no |
| 1440 | transformación | alto | 0,70 × 0,80 | 21 / 12 px | no |
| 1440 | figura (foco) | alto | 0,74 × 0,82 | 1 / 1 px | no |

La figura formada mide el 80 % del lado menor (82 % con el grosor de los
tubos y su borde luminoso) y queda centrada a ±1 px. La masa es orgánica:
en reposo mide 77 % a 82 %. A mitad de la transformación se abulta hacia
un lado, y eso es lo que mueve el centro de su caja.

**Consola: sin errores ni avisos** (página y workers) en los tres anchos,
las cinco figuras, los niveles y el modo sin movimiento. La única
excepción: con GPU por software (SwiftShader) Chrome emite su propio aviso
de rendimiento del controlador, "GPU stall due to ReadPixels", al componer
el lienzo del respaldo. No es un error de shader ni de JavaScript.

### Cuadros por segundo

| Perfil | Nivel elegido | fps (mediana) |
|---|---|---|
| Escritorio 1440 × 900 (Intel Iris Xe), ciclo en marcha | alto | 60 |
| Escritorio, congelado en la transformación y en la figura | alto | 60 y 60 |
| Móvil 390 × 844, dpr 3, CPU ×4, ciclo en marcha | medio | 60 |
| Móvil, congelado en la transformación y en la figura | medio | 60 y 60 |

Cadena adaptativa comprobada:

- Escritorio con GPU por software: arranca directo en `particulas` (60 fps).
- Sin WebGL: `fija`.
- Con el motor en el hilo principal y CPU ×20: bajó alto → medio → bajo →
  partículas.
- Con el worker, el estrangulamiento de CPU del hilo principal no afecta al
  motor.

### Peso

Medido en el navegador, en bytes (gzip entre paréntesis):

| | Antes (`main`) | Después |
|---|---|---|
| JS inicial de la portada | 810 395 (221 468) | 806 398 (220 476), unos 4 KB menos |
| Diferido, motor de la materia (three.js + motor + worker) | — | 590 759 (151 522) |
| Diferido, respaldo de partículas | — | 24 626 (9 913) |
| Diferido, imagen fija | — | 24 204 |

three.js y el motor nunca entran en el bundle inicial. Se descargan después
del evento `load`, en reposo y dentro del worker. Un equipo que cae a
partículas o a la imagen fija no descarga three.js. Los campos de distancia
de las figuras se calculan en el worker y no pesan en la descarga.

### Lighthouse (rendimiento, local, build de producción)

Medianas de 3 corridas antes y de 5 (móvil) o 3 (escritorio) después:

| | Puntuación | LCP | TBT | FCP | Speed Index | CLS |
|---|---|---|---|---|---|---|
| Móvil antes | 72 | 6,70 s | 216 ms | 1,66 s | 2,44 s | 0 |
| Móvil después | **77** | 6,62 s | 54 ms | 1,51 s | 1,62 s | 0 |
| Escritorio antes | 97 | 1,26 s | 18 ms | 0,41 s | 0,77 s | 0 |
| Escritorio después | **97** | 1,23 s | 0 ms | 0,37 s | 0,41 s | 0 |

En esas corridas el Chrome de Lighthouse cargó el motor completo, en el
worker. El LCP móvil de 6,6 s ya estaba antes y no es de la masa: el
elemento LCP es un enlace del nav o del botón y lo retrasa la simulación de
red con el JS de la página.

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
