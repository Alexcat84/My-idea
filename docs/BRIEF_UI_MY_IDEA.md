# BRIEF DE DISEÑO UI — "My Idea" (Fases 3.2 y 3.3)
Fuente: visión del fundador (transcripción de voz, 2026-07-08), estructurada por Fable.
Regla madre: la web NO es un chat. Es un espacio de trabajo de ideas con su propio
lenguaje visual. Cero parentesco con la UI del I Ching.

## 1. IDENTIDAD
- Nombre del producto: **My Idea**. La unidad de trabajo se llama **idea** en toda la
  UI (jamás "proyecto" de cara al usuario; "project" queda solo en la DB).
- **Modo oscuro único** (no hay modo claro en beta). Paleta ACTUALIZADA (2026-07-09,
  referencia elegida por el fundador: Frame.io V4 — negro cinematográfico, un solo
  acento azul eléctrico; reemplaza la provisional ámbar del brief original):

  ```css
  --bg: #000000;               /* fondo base: negro verdadero */
  --surface: #101013;          /* cintas, tarjetas, acordeones */
  --surface-2: #17171B;        /* hover / elevación segunda */
  --border: rgba(255,255,255,0.08);  /* hairlines, no bordes gruesos */
  --text: #F5F6F8;             /* títulos y texto primario */
  --text-dim: #A6A7AD;         /* secundario, metadatos, labels */
  --accent: #4D7CFE;           /* azul eléctrico: acciones, progreso, focus ring */
  --accent-soft: rgba(77,124,254,0.14); /* fondos de estado activo */
  --done: #3FB950;             /* checklist Hecho */
  --warn: #E3B341;             /* avisos suaves (GIGO en palabras de persona) */
  --radius: 12px; --radius-lg: 16px;
  --motion: 180ms cubic-bezier(0.2, 0.8, 0.2, 1);
  ```

  Cinco reglas de lenguaje visual (Frame, no solo pintado como Frame):
  (1) el color vive en el contenido, no en el chrome: interfaz monocroma, el acento
  solo en acciones/progreso/estados; (2) hairlines de 1px translúcido, jamás bordes
  gruesos ni sombras dramáticas; (3) jerarquía por tamaño y peso tipográfico, no por
  colores de título; (4) layout de riel (árbol punteado) + panel de contenido en la
  vista de idea; (5) movimiento mantecoso y breve (180ms ease-out) en acordeones,
  hover de cintas y encendido de nodos.

  La arquitectura de tokens (CSS variables) vive en UN solo archivo
  (`web/app/tokens.css`) y debe permitir cambiar la paleta editando solo ese archivo.
- Tipografía: sans limpia (Inter o similar), generosa en interlineado; los planes
  se leen como documento, no como terminal.

## 2. MAPA DE PANTALLAS (Fase 3.2 = base de beta)

### 2.1 Login
Magic link. Pantalla mínima: logo, campo email, frase de producto. Allowlist de
beta con mensaje amable al no invitado.

### 2.2 Home: "Mis ideas" (las cintas)
- Lista vertical de **cintas** (bandas horizontales full-width, esquinas suaves):
  una por idea. Cada cinta: nombre de la idea (primeras palabras o título editable),
  fecha de última actividad, mini-estado (Organizada / En entrevista / Con plan /
  En seguimiento), y micro-indicador de progreso del checklist si existe.
- Botón primario flotante o superior: **"Nueva idea"**.
- Click en cinta → vista de la idea (2.4). Vacío elegante si no hay ideas aún.

### 2.3 Captura de idea (el momento sagrado)
- Pantalla limpia: un solo campo grande multilínea ("Cuéntame tu idea, o en qué
  punto estás con ella") + **botón de micrófono**.
- Voz: Web Speech API (SpeechRecognition) cuando el navegador la soporte
  (Chrome/Edge/Android); transcripción en vivo dentro del campo, editable antes
  de enviar. Fallback limpio a solo-texto donde no exista (Firefox): el micrófono
  no aparece, sin error. (Whisper/API de transcripción = backlog 3.4, no beta.)
- Enviar → arranca el organizador gratuito (una idea nueva SIEMPRE pasa primero
  por el organizador: es el gancho freemium).

### 2.4 Vista de idea: generación con "árbol que piensa"
REGLA DE ORO: la animación es VERDAD, no teatro. Cada elemento visual mapea a un
evento real del motor (la caja de vidrio alimenta la UI).
- Mientras genera: en el lado izquierdo crece una **línea punteada vertical** que
  se bifurca en nodos/puntos; cada punto se enciende cuando llega el evento real:
  para el organizador, cada sección detectada en el stream ("En una frase",
  "Lo que ya tienes claro", "Supuestos", "Áreas del plan"); para la entrevista,
  cada nodo real de la ruta (label del nodo, con los silenciosos apareciendo
  atenuados con su marca "cubierto por lo que contaste"); para el plan, cada
  etapa del SSE al llegar su encabezado. Texto de estado tipo "generando: <label>".
- Resultado del organizador: **acordeones** (cintas desplegables), una por sección.
  Cerradas por defecto salvo "En una frase". Debajo, el CTA según estado de tokens:
  con tokens → "Continuar el desarrollo de mi idea"; sin tokens → "Ver planes"
  (en beta: stub de cortesía, sin pagos reales).

### 2.5 Entrevista (no-chat)
- **Una pregunta a la vez, como tarjeta**: la pregunta arriba (con el título del
  concepto como cintillo pequeño), campo de respuesta + micrófono debajo, botón
  enviar. Nada de burbujas ni historial de chat en pantalla principal.
- A la izquierda persiste el árbol punteado creciendo con la ruta real (los saltos
  con una marca sutil distinta). Un acordeón "recorrido" permite releer preguntas
  y respuestas previas sin convertir la pantalla en chat.
- El motor NUNCA re-pregunta la idea inicial (ya la conoce): así funciona ya.
- La oferta de "¿seguimos o plan ya?" y el botón permanente "Generar mi plan"
  se muestran como acciones claras, no como texto en conversación.

### 2.6 Plan
- Streamea con el árbol marcando etapas; al terminar se re-renderiza como
  **documento acordeón**: título + intro abiertos; cada Etapa = acordeón con sus
  pasos numerados; "Esta semana" destacado dentro de cada etapa con el acento;
  la sección de sostenibilidad al final; etiqueta (inicial/completo) visible
  discreta; botón de descarga .md.
- Bajo el plan: tarjeta **"Reporte de números"** (corre la mini-entrevista de
  tipo de oferta en tarjetas iguales a 2.5, y muestra el reporte en acordeones).

## 3. FASE 3.3 — EL BUCLE DE CHECKLIST (el alma del seguimiento)
La innovación central del fundador. Convierte --seguir en un ritual sin fricción.
- **Derivación**: al guardarse un plan, el backend deriva determinísticamente un
  checklist: un ítem por cada "Esta semana" y por cada paso numerado de etapa
  (id estable: plan_id + etapa + índice; texto = el imperativo del paso).
  Guardado en tabla nueva `checklist_items` (project_id, plan_id, dominio='core',
  etapa, orden, texto, estado, nota, updated_at). Migración + dbContract.
- **Estados por ítem (4, discretos)**: Pendiente / Empezado / A medias / Hecho.
  UI: la cinta de la idea muestra el checklist agrupado por etapa (acordeones),
  cada ítem con selector de estado de un toque y campo de nota opcional.
- **Volver a la idea (seguimiento)**: al pulsar "Continuar mi idea", NO hay campo
  de texto libre primero. Aparece: (1) el checklist para actualizar estados,
  (2) "Detalles adicionales" (texto/voz opcional), (3) "¿Hacia dónde quieres
  profundizar?" con opción explícita **"No estoy seguro"**.
- **Composición determinística**: el backend construye el mensaje de seguimiento
  para el motor a partir de {estados del checklist agrupados, notas, detalles,
  enfoque}, en texto estructurado y compacto. El MOTOR NO CAMBIA: recibe ese
  texto como el "qué ha pasado" de siempre + estado_vivo. El compresor de
  estado_vivo puede citar el resumen del checklist (frase, no tabla).
- Cada nuevo plan de seguimiento genera SU checklist (misma tabla, nuevo plan_id);
  la vista de la idea muestra la cronología: planes como hitos, checklists por
  fase, hasta "idea cerrada" (estado que el usuario puede marcar).

## 4. ADD-ONS (mundos HSEQ) — SOLO FACHADA EN BETA
- En la vista de idea, tres tarjetas con candado y sus nombres de cara al usuario:
  **"Calidad y Confianza"**, **"Seguridad y Personas"**, **"Ambiente y Futuro"**,
  con una línea de promesa cada una desde un `packs_catalog.json` estático
  (NUNCA leyendo nodos). Click → "Disponible próximamente" + registro del click
  (telemetría de demanda: oro para priorizar el lanzamiento del primer pack).
- Diseño acordado para su activación real (v1.3, post-beta), respondiendo la
  pregunta del fundador sobre sincronización: **un solo almacén de checklist**
  (`checklist_items.dominio` distingue core/pack). Al activarse un pack en una
  idea: (1) corre una *evaluación de brecha* automática que lee estado_vivo +
  numeros + estados del checklist core (jamás re-pregunta lo sabido), (2) entra
  al grafo del dominio por la semilla afín a la fase actual, (3) sus planes
  derivan ítems con dominio propio en la MISMA tabla. Como todos leen y escriben
  el mismo almacén, "que se actualicen solos" es propiedad de la arquitectura
  (una fuente de verdad, vistas filtradas por dominio), no un trabajo de sync.

## 5. FUERA DE BETA (backlog 3.4+, registrado, no construir)
Pagos reales de tokens (Stripe), activación real de packs, transcripción Whisper,
edición del título de idea con IA, exportar PDF, modo claro, paleta final del
sitio de referencia del fundador, marcar "idea cerrada" con celebración.

## 6. CRITERIOS DE CIERRE FASE 3.2 (base) y 3.3 (bucle)
- 3.2: flujo completo Nueva idea → organizador con árbol real → entrevista en
  tarjetas → plan acordeón → reporte, en Vercel preview con allowlist, mobile-first
  (mínimo 380px), voz funcionando en Chrome/Android con fallback correcto,
  vuelo.ts extendido con verificación de que los eventos del árbol corresponden
  1:1 a la ruta persistida.
- 3.3: derivación de checklist verificada contra un plan real (ítems = pasos),
  ciclo completo seguir-con-checklist en vivo, y el mensaje compuesto visible
  en la bitácora de la sesión (auditable).
- Ambas: suites verdes en clon limpio; la certificación final sigue siendo la
  sesión real del fundador VÍA UI en el preview.
