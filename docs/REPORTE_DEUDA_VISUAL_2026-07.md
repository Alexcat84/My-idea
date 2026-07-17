# REPORTE DE DEUDA VISUAL — app vs canon refrescado (jul 2026)

Primera corrida del gate contra el canon nuevo de Claude Design. Las 64 capturas
viven en `web/examples/gate-canon/`, en pares `NN_<pantalla>_{app|canon}[_380].png`.

**El veredicto visual es del fundador.** Este reporte solo ordena lo que el
instrumento produjo y anota lo que pude observar objetivamente, para que el corte
pre-beta vs. backlog se decida con la foto entera.

## Cómo leer las capturas

- `..._app.png` / `..._app_380.png` — la app viva HOY, en 1240 y 380.
- `..._canon.png` / `..._canon_380.png` — el frame del canon, al lado.
- `z_..._SOLOCANON*.png` — pantallas del canon nuevo que la app **aún no
  implementa** o que el flujo del gate no visita: se muestran solas, como
  objetivo. No son pares rotos.

## Clasificación

- **ROTA** — ilegible, desbordada o intocable con el dedo. (Ninguna encontrada
  en lo que inspeccioné: la app funciona; la deuda es de arquitectura y de
  ajuste, no de rotura.)
- **ESTRUCTURAL** — la app funciona pero el canon reorganiza la información de
  forma que cambia el layout (no es un ajuste de píxeles).
- **DIVERGENCIA DE FORMATO** — la app y el canon eligen representar el mismo dato
  distinto; hay que decidir cuál gana.
- **NUEVO** — el canon dibuja una pantalla/estado que la app no tiene.

---

## Lo que inspeccioné de cerca

### Manos a la Obra a 380 — ESTRUCTURAL (la deuda más grande)

Pares: `05_manos_app_380` vs `05_manos_canon_380`.

- La app son **3.394px de scroll**. El canon lo reorganiza a ~2.300px.
- **"Contar qué pasó" (la puerta al seguimiento) está en la app hasta el fondo**,
  a ~2.800px del pulgar. El canon la sube arriba del todo, con jerarquía. Es el
  corazón del replanteo: la acción principal no puede estar enterrada.
- El **selector de modo** ("¿Cómo quieres llevar tu camino?") ocupa un bloque
  enorme arriba en la app. El canon muestra el estado ya elegido, compacto
  ("Modo: a mi ritmo · cambiar"), y manda la elección completa a la pantalla 10.
- "Ver análisis" y "Ritmo" son secciones completas al fondo en la app; el canon
  las vuelve tarjetas **plegables**.

Veredicto sugerido: **pre-beta si la APK es prioridad** (es el viewport real del
teléfono), backlog si la web de escritorio manda primero. La decisión es tuya.

### Home / Mis ideas — DIVERGENCIA DE FORMATO (el timestamp)

Pares: `00_home_app` vs `00_home_canon`.

La lista, los rieles (ya conectados tras el fix) y los chips **calzan**. La
divergencia es el sello de fecha que implementé la ronda pasada:

- **La app** (mi `fechaSello`) es puramente absoluta: `hoy 08:14`, `ayer 21:26`,
  `14 jul`, `31 dic 2025`.
- **El canon** de Design es **híbrido**: usa relativo para lo muy reciente
  (`hace 21 min`, `hace 3 días`) y absoluto como ancla (`ayer 21:26`, `hoy
  08:14`, `el 12 de marzo`).
- Las realizadas también difieren: la app dice "realizada el 14 jul · N días de
  la chispa al proyecto"; el canon dice "Realizada **el 12 de marzo** · 24 de 31
  acciones hechas" (mes completo, y cuenta acciones en vez de días).

Hay que decidir: **¿adoptamos el híbrido de Design o el absoluto que puse?** Es
un cambio chico en `fechaSello` y en la pista de la cinta, en cuanto lo digas.

---

## Lo que el instrumento produjo, para tu veredicto pantalla por pantalla

Estos pares existen en la carpeta y esperan tu ojo. No los juzgo yo: el canon es
un rediseño, así que casi todos difieren de la app en algo, y decidir qué de eso
entra pre-beta es criterio de producto.

| Pantalla | Pares en la carpeta | Nota |
|---|---|---|
| Home | `00_home` | timestamp divergente (arriba) |
| La Chispa | `01_chispa` | cambió poco; probable calce |
| Claridad | `02_claridad` | distinción por forma (punto/rombo) |
| La Exploración | `03_exploracion` + oferta + plan en camino | el riel ya conecta |
| Tu Plan | `04_tu_plan` | "Activar · beta" en la fila |
| Manos a la Obra | `05_manos` | la deuda estructural (arriba) |
| Mundo activo | `10_mundo_activo` | mundo como subproyecto |
| Cierre de mundo | `10c_mundo_cierre` | el acta en miniatura |
| Modo (elección) | `06_modo` | |
| Ritual de fechas | `07_baseline` | |
| Análisis | `08_analisis` | fila "cumplimiento por mundo" |
| Celebración (cumplimiento) | `09_celebracion_cumplimiento` | |
| Celebración (a mi ritmo) | `09b_celebracion_ritmo` | ahora con par de 380 |

## NUEVO — pantallas del canon que la app no tiene (solo-canon)

Estas son objetivos, no pares. La app aún no las dibuja como el canon:

| Objetivo | Captura | Estado en la app |
|---|---|---|
| Potenciadores y Créditos | `z_potenciadores_SOLOCANON` | existe la fila con "Activar · beta"; falta la pantalla-centro |
| Cierre honesto (camino core) | `z_cierre_camino_SOLOCANON` | existe `CierreHonesto` en código; el estilo del canon es más cálido |
| Cierre honesto (mundo) | `z_cierre_mundo_SOLOCANON` | idem; **ojo**: el canon dice "devolvimos 3 créditos", pero en beta la activación es gratis (no hay créditos que devolver hasta la ETAPA 2) |
| Detalle de actividad | `z_detalle_actividad_SOLOCANON` | **no existe**: es la pantalla nueva que pediste ("Explorar actividad") |

## Recomendación de orden (mía; la decisión es tuya)

1. **El timestamp** — chico, y ya está a medias hecho: solo hay que decidir el
   formato (mi absoluto vs. el híbrido de Design).
2. **Manos a la Obra a 380** — la deuda estructural real, y la que más pesa para
   la APK.
3. **Detalle de actividad** — pantalla nueva que pediste; el canon ya la dibujó.
4. El resto, pantalla por pantalla, según tu veredicto sobre cada par.
