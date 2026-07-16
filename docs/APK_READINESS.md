# PREPARACIÓN APK — Restricciones que My Idea respeta DESDE HOY

Propósito: que ninguna decisión de infraestructura o dependencia de la web de
hoy se convierta en sorpresa el día que nazca la APK (patrón WebView/TWA,
heredero del I Ching). Este documento se consulta **ANTES** de añadir
dependencias o de cambiar la arquitectura de auth, streaming, notificaciones o
pagos.

## 1. REGLAS DE GOOGLE PLAY CON FECHA (verificadas jul 2026, fuente oficial)

- **Target API**: apps nuevas y actualizaciones deben apuntar a **Android 16
  (API level 36) o superior** desde el 31 de agosto de 2026. My Idea APK nace
  como app nueva: API 36+ desde el día uno. (Fuente: Play Console Help,
  answer/11926878; el requisito sube cada agosto: re-verificar al construir.)
- **Verificación de desarrollador**: las apps deben estar registradas en Play
  Console (requisito de developer verification). La cuenta del fundador ya
  existe (I Ching); la APK de My Idea se registra al crearse.
- **User Data e IA de terceros** (anuncio 15 jul 2026): los requisitos de User
  Data aplican explícitamente a integraciones de IA de terceros; el
  desarrollador es responsable de uso limitado, divulgación y consentimiento.
  My Idea envía contenido del usuario a la API de Anthropic: la sección Data
  Safety de Play y la política de privacidad **DEBEN** declararlo. (Enlaza con
  `BANCO_DE_TEXTOS.md` §7.)
- **Content rating obligatorio**: Play no permite apps sin clasificar.
- **Billing**: dentro de la app de Play, las compras de créditos pasan por
  Google Play Billing (15-30%), vía RevenueCat. La web sigue con Stripe (vía
  RevenueCat). El ledger ya es agnóstico de pasarela por diseño: **NO romper eso**.
- Herramienta para el día APK: la skill open-source de Google que fundamenta
  LLMs en políticas de Play (`github.com/android/skills`,
  `play-policy-insights`): Claude Code se auto-audita contra políticas antes del
  submit.

## 2. DECISIONES YA TOMADAS QUE LA APK PRESUPONE (no re-litigar)

- **Toda la inteligencia vive en el servidor**; la web es una cara. La APK es
  OTRA cara de las mismas rutas API. Nada de lógica de negocio en el cliente.
- **Ledger de créditos agnóstico de pasarela** (migraciones 020-024): origen
  `'cortesia' | 'revenuecat'`; RevenueCat es el puente único hacia Stripe (web)
  y Play (móvil). Cualquier cambio al ledger conserva esta pluralidad.
- **Auth**: Supabase Auth con convivencia de proveedores. Magic link para la
  beta web; **"Continuar con Google" se añade como proveedor primario ANTES de
  la APK** (el magic link en WebView es fricción fea: saltar al correo y volver
  rompe el flujo).
- **Mobile-first 380px es ley del canon**: toda pantalla nueva se diseña y se
  gate-verifica también en 380 (el gate lo hace desde jul 2026, en sus dos
  viewports).
- **La APK NO es la web embebida y ya.** *(Decisión del fundador, 2026-07-16,
  revirtiendo la línea original de este § —"la APK renderiza exactamente esta
  web"— que venía del auditor.)* El veredicto, como fundador y como **cliente
  usuario**: **«eso no sirve, se satura»**. Envolver el scroll de la web en un
  WebView y llamarlo app da una app que no se ve como una app.

  **La APK sigue un diseño detallado propio y LUCE como APK, aunque inyectemos
  la web.** Tendrá **componentes nativos**. El precedente no es teórico: es el I
  Ching, donde este patrón "aplicó y quedó genial, con las variaciones
  correctas".

  Lo que eso NO cambia (sigue en pie, y es lo que hace posible lo anterior):
  toda la inteligencia vive en el servidor y la APK es **otra cara de las mismas
  rutas API**. El caparazón es nativo; el cerebro, no. Nada de lógica de negocio
  en el cliente.
- **La Chispa con micrófono es la razón de ser de la APK** ("una idea nace en un
  preciso momento"): la captura por voz jamás se degrada en móvil.

## 3. REGLAS DE INGENIERÍA DESDE HOY (compatibilidad WebView)

Lecciones pagadas en el I Ching, aplicadas de nacimiento:

- **SSE con heartbeat**: los streams (organizador, plan) ya usan SSE; los
  WebView y las radios móviles matan conexiones ociosas. Mantener heartbeats y
  reconexión tolerante (el retry de plan/organizador ya existe: conservarlo).
  Ninguna dependencia nueva de streaming sin probar en WebView.
- **APIs de navegador con fallback**: nada que dependa exclusivamente de APIs de
  escritorio. Antes de usar una API del navegador (portapapeles, share,
  fullscreen, notificaciones web, file picker), verificar soporte WebView o
  degradar con gracia. El micrófono (MediaRecorder/SpeechRecognition) es el caso
  crítico: en la APK puede requerir permiso nativo puenteado; aislar su uso en un
  módulo único reemplazable.
- **Cookies y sesión**: la sesión de Supabase debe sobrevivir dentro de un
  WebView (cookies first-party, sin depender de third-party cookies ni de popups
  OAuth que WebView bloquea: el login con Google en móvil usará el flujo nativo
  puenteado, patrón I Ching).
- **Deep links**: las rutas ya son limpias (`/idea/[id]`, `/nueva`). No
  introducir estado que viva solo en memoria del cliente para llegar a una
  pantalla: todo destino importante debe ser alcanzable por URL (la celebración,
  el análisis, el mundo). Regla ya cumplida: mantenerla.
- **Origin guard**: al nacer la APK, el backend valida el origen del WebView
  (patrón endurecido del I Ching, auditado allá). Las rutas de My Idea no asumen
  hoy nada que lo impida: conservar.
- **Notificaciones por capas**: email (beta) → web push (opt-in) → FCM (APK). El
  diseño de la 4.1-futura no debe acoplarse a un canal: el cron lee `fecha_base`
  y el canal es un adaptador. Nada de web-push-only.
- **Peso y rendimiento**: presupuesto de bundle vigilado (el WebView de un
  teléfono medio es el target real). Dependencias nuevas de UI se justifican;
  nada de librerías pesadas por conveniencia.
- **El sello de versión (v·hash) en el pie**: en la APK identifica qué build web
  sirve el WebView. Conservar siempre.

## 3-bis. EL CAPARAZÓN NATIVO (el patrón del I Ching, verificado en su código)

Esto no es una intención: es lo que `referencia/iching-app/apps/mobile` ya hace
en producción, y de ahí se porta. La APK es un **WebView dentro de un caparazón
nativo**, no un WebView a secas:

| Pieza | Qué aporta | Dónde vive en el I Ching |
|---|---|---|
| **Botón atrás del sistema** | Que "atrás" haga lo que el usuario espera y no cierre la app | `BackHandler` (`app/index.tsx`) |
| **Safe areas** | Que el notch y la barra de gestos no se coman la UI | `useSafeAreaInsets` |
| **Barras del sistema / edge-to-edge** | Que la app ocupe la pantalla como app, no como página | `SystemBars` (`react-native-edge-to-edge`), `StatusBar` |
| **Splash** | Arranque de app, no parpadeo de navegador | `expo-splash-screen` |
| **Pantallas NATIVAS propias** | Lo que en un WebView es fricción fea o directamente no funciona | `expo-router` `Stack`: `auth/`, `purchase-success` |
| **El puente** | La web y lo nativo se hablan | `injectedJavaScript` + `onMessage` (`WebViewMessageEvent`) |
| **Compras** | Play Billing de verdad | `react-native-purchases` (RevenueCat) |
| **Estado local + sync** | Que la app abra con contenido, sin esperar red | `AsyncStorage`, `src/db`, `src/sync/sync-service.ts` |

**La consecuencia de diseño, que es la que el fundador señaló:** la navegación
de My Idea a 380 hoy **no existe** — no hay menú que se despliegue, no hay nada
que se colapse, y todo es un scroll largo (la captura de Manos a la Obra a 380
mide ~3.100px y el header trunca el nombre de la idea). Eso hay que diseñarlo, y
la parte que sea **chrome de navegación** es candidata a ser **nativa**, no
inyectada. El diseño detallado de la APK es su propia entrega de canon: hasta que
exista, este § describe el patrón, no la pantalla.

**Regla que sí queda fijada:** la frontera. Nativo = caparazón, navegación,
permisos, compras, sesión. Web inyectada = el producto (la Chispa, el árbol, el
plan, el checklist, los mundos). Si una pieza necesita saber de negocio, vive en
el servidor y se pinta en la web.

## 4. CHECKLIST DEL DÍA APK (para no redescubrirlo)

0. **El diseño detallado de la APK** (su canon propio): qué es nativo y qué se
   inyecta, pantalla por pantalla. Es el prerequisito de todo lo demás — sin él
   la APK es la web envuelta, que es exactamente lo que el fundador rechazó.
1. Proyecto Android (WebView + caparazón nativo, patrón I Ching; **no** un TWA
   pelado), target API 36+ (re-verificar el nivel vigente ese agosto).
2. Play Integrity + origin guard (portar del I Ching).
3. Login con Google nativo puenteado a Supabase.
4. RevenueCat + Google Play Billing sobre el ledger existente (origen nuevo,
   cero cambios de esquema).
5. FCM para recordatorios (el adaptador de canal nuevo; el cron ya existirá).
6. Micrófono con permiso nativo (el módulo aislado del §3 se reemplaza).
7. Data Safety con divulgación de IA de terceros + política de privacidad
   enlazada + content rating.
8. Registro de la app en Play Console (developer verification).
9. La skill `play-policy-insights` corre sobre el proyecto antes del submit.
10. Los dos dev servers jamás comparten puerto con el I Ching (3000 vs 3100:
    lección vivida).

---

## 5. ESTADO REAL CONTRA ESTE DOCUMENTO (auditado 2026-07-15, contra `main` = `be54bea`)

Regla de la casa: **nada se afirma sin evidencia** (`archivo:línea` o resultado
real). Este documento declara varias reglas como "ya cumplida"; aquí queda
verificado cuáles lo están de verdad y cuál no, para que nadie herede una
tranquilidad falsa.

| Regla del §2/§3 | Estado | Evidencia |
|---|---|---|
| SSE con heartbeat | ✅ **Cumplida** | `organizer/stream/route.ts:97` y `session/[id]/plan/route.ts:179`: `": heartbeat\n\n"` cada `INTERVALO_HEARTBEAT_MS` (15s), con `Cache-Control: no-cache, no-transform` y `Connection: keep-alive`. El `no-transform` importa: evita que un proxy móvil buferee el stream. |
| Reconexión tolerante en streams | ✅ **Cumplida** | Retry con backoff en los dos únicos streams (Fase 4.0 / follow-up del stream del plan). |
| Micrófono aislado en un módulo único | ✅ **Cumplida** | `lib/useSpeech.ts` es el ÚNICO sitio que toca `SpeechRecognition`; su único consumidor es `app/ui/CampoConVoz.tsx`. El día del permiso nativo se reemplaza **un** archivo. |
| APIs de navegador con fallback | ✅ **Cumplida** | `useSpeech` expone `soportado`; `CampoConVoz.tsx:62` **no renderiza** el micrófono sin soporte (fallback limpio a solo-texto). Las únicas otras APIs son `matchMedia('prefers-reduced-motion')` en `Celebracion.tsx:57` y `Landing.tsx:83`, ambas con `?.` y ambas decorativas. Cero portapapeles, cero share, cero fullscreen, cero file picker, cero notificaciones web. |
| Deep links: todo destino alcanzable por URL | ✅ **Cumplida** | `IdeaView.tsx:114-116` lee `?vista=` para `manos`, `analisis` y `celebracion`, y `router.replace` la sella al navegar (`:407`, `:420`, `:435`). La sección de un mundo vive dentro de `?vista=manos`. |
| Sello de versión en el pie | ✅ **Cumplida** | `app/layout.tsx`. |
| Peso: sin librerías pesadas | ✅ **Cumplida** | 9 dependencias de producción: `next`, `react`, `react-dom`, `@supabase/ssr`, `@supabase/supabase-js`, `@anthropic-ai/sdk`, `react-markdown`, `rehype-sanitize`, `remark-gfm`. **Cero librerías de UI, de estado, de fechas, de gráficos o de streaming.** Nada aquí es hostil al WebView. |
| Ledger agnóstico de pasarela | ⏸️ **Diseñado, sin aplicar** | Migraciones 020-024, rama `cuentas-y-creditos`. La ETAPA 2 requiere autorización escrita del fundador. |
| **Mobile-first 380: se gate-verifica también en 380** | ❌ **NO cumplida — es el único hueco real** | Ver abajo. |

### 5.1 El hueco: el canon tiene la vara de 380 y el gate no la mira

El canon **sí** trae su frame `mobile 380` en **10 de las 11 pantallas** (solo el
07 Potenciadores no lo tiene):

```
01 Home            -> Mis ideas mobile 380
02 La Chispa       -> La Chispa mobile 380
03 Claridad        -> Claridad mobile 380
04 La Exploracion  -> 1a mobile 380 · 1a mobile 380 recorrido abierto
05 Tu Plan         -> Tu Plan mobile 380
06 Manos a la Obra -> Manos a la Obra mobile 380
07 Potenciadores   -> SIN frame mobile
08 Mundos Activos  -> Idea con mundo activo mobile 380
09 La Celebracion  -> La Celebracion mobile 380
10 Modo y Fechas   -> Eleccion de modo mobile 380 · Ritual de fechas mobile 380
11 Analisis        -> Analisis ambas capas mobile 380
```

Y `gate_canon.ts:118` abre **un solo contexto**:
`viewport: { width: 1240, height: 900 }`. **El gate nunca ha capturado la app a
380, ni una vez, en ninguna fase.** `capturarCanon` toma por defecto el primer
frame que termina en `"desktop"`; los frames de 380 del canon **nunca se han
mirado contra nada**.

Esto es exactamente el primer punto de `BANCO_DE_TEXTOS.md` §9: **una señal que
nadie lee no es una salvaguarda.** La vara existe, el diseñador la dibujó, y el
instrumento no la usa. "Mobile-first 380px es ley del canon" es verdad del
**canon** y mentira del **gate**.

Gravedad: **la APK renderiza esta web en un teléfono.** El 380 no es un extra de
la APK — es su viewport real. Todo lo que se ha declarado "fidelidad al canon
verificada" (Fase 3.7, la fidelidad cerrada, las 11 pantallas) se verificó
**solo en escritorio**.

## 6. VEREDICTO SOBRE DEPENDENCIAS

**Para compatibilidad de dependencias: no hay nada que hacer, y conviene que
quede escrito por qué.**

El árbol de producción son 9 paquetes y ninguno introduce una superficie que el
WebView castigue: no hay librería de streaming propia (SSE es del estándar), no
hay librería de estado, no hay date-picker de terceros (las fechas son
`<input type="date">` nativo — decisión de la 3.8, la "píldora-humana" quedó en
backlog), no hay gráficos (el Análisis y la Celebración se dibujan con CSS), y el
markdown se sanea con `rehype-sanitize`. `@anthropic-ai/sdk` **solo corre en el
servidor** (`runtime = "nodejs"` en las rutas): jamás viaja al WebView.

La regla que este documento aporta no es una tarea, es un **freno**: la próxima
vez que se quiera meter una librería de UI, de gráficos o de fechas "por
conveniencia", este §6 es el que dice que no.

**Lo que sí justifica trabajo no es una dependencia: es el §5.1.** El gate debe
capturar a 380 contra los frames de 380 del canon. Es barato (el gate ya corre;
es un segundo contexto de viewport y un `label` distinto en `capturarCanon`) y no
cuesta ni un token de LLM extra. Pero **cambia lo que el gate cuesta y produce, y
puede destapar deuda visual en 10 pantallas ya dadas por cerradas**: la decisión
de cuándo pagarlo es del fundador.
