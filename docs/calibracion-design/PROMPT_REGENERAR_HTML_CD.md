Necesito que regeneres, desde tu sesión, unos entregables que ya diseñaste, pero en un formato que la implementación (Claude Code) pueda LEER e implementar fiel. El problema con los HTML actuales es que vienen con datos comprimidos e imágenes embebidas (base64/gzip), y no se pueden leer para extraer la estructura ni el CSS.

## El formato que necesito (lo más importante)

Para cada archivo, un **HTML autocontenido y HUMANAMENTE LEGIBLE**:

- **CSS inline en un `<style>` al inicio, SIN minificar** (indentado, con los tokens en `:root` arriba y comentarios por sección). Nada de CSS comprimido en una línea.
- **CERO imágenes embebidas / base64 / datos gzip.** Los iconos y los gráficos, como **SVG en línea** escrito a mano (paths legibles). Si algo usaba una imagen rasterizada, reemplázalo por SVG o por una caja con su medida.
- **Sin CDNs, sin fuentes externas, sin frameworks.** Fuentes del sistema. UTF-8.
- **Markup semántico y legible**, con clases en español y comentarios de sección, tal como tu convención de entrega.
- Que abra con doble clic, sin internet.

En resumen: el mismo diseño que ya hiciste, pero **en texto plano legible** (HTML + CSS a la vista), no empaquetado.

## Los archivos

### 1. La Celebración — el TIMELINE vertical (lo prioritario)
De **"09 - La Celebración"**, necesito sobre todo la **línea de tiempo vertical de hitos**: el eje, la barra azul→verde que desciende marcando el avance, los nodos sobre el eje, el nodo mayor (anillo) del cierre "Realizada", y las etiquetas/fechas de cada hito. Es la vara que voy a calcar para una pantalla nueva ("Tu avance": los hitos de cada espacio del proyecto, en versión estática/sobria).
- `09_la_celebracion_1240.html` (escritorio) y `09_la_celebracion_380.html` (móvil).
- Si prefieres, entrega SOLO el fragmento del timeline (su HTML + su CSS), con tal de que sea legible y completo.

### 2. PDF Expediente · interiores (las 4 páginas)
Las páginas interiores del Expediente que quedaron pendientes de aplicar (816px, carta):
- `tus_numeros_816.html` — la página de Tus Números.
- `un_mundo_816.html` — la página de un mundo (Riesgos Bajo Control).
- `resumen_816.html` — "Cómo te fue" / "Tu progreso hasta aquí".
- `secuencia_816.html` — "La secuencia de tu viaje" (la bitácora dentro del expediente).

## Reglas de la casa (recordatorio)
Modo oscuro en pantalla; el papel del PDF con su paleta de papel. Azul #4D7CFE (en papel #3B6BE8) para la acción; verde para lo cumplido y el cierre; ámbar avisa; gris lo que ya no se mueve. **Nunca rojo. Sin guiones largos. Sin jerga ni mecánica del motor.**

Con esos archivos en texto plano legible, Claude Code implementa "Tu avance" calcado del timeline de la Celebración y aplica los interiores del PDF Expediente.
