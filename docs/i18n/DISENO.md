# My Idea multilingüe: diseño (F0)

**Fecha:** 26 sep 2026. **Rama:** `i18n`, desde `main` en `dc5f5e65`. **Estado:** F0 cerrada; el
fundador aprobó el glosario y las decisiones D1 a D9 (§7). F1 espera la clave de Voyage.

## 1. Lo que pide el fundador

- Idioma base **español**. Once idiomas, los de theoriginaliching: `es, en, pt, fr, de, it, ja, zh,
  ko, ar, hi`.
- **El grafo sigue en español** como fuente única: no se traduce ningún nodo. La IA responde en el
  idioma del usuario, apoyándose en los nodos en español.
- El usuario escribe o dicta en **cualquier idioma**: se detecta, se guarda el texto original tal
  cual, el proyecto recuerda su idioma y todo lo que la app le devuelve sale en ese idioma.
- Patrón theoriginaliching: preferencia en cookie, idioma del navegador solo en la primera visita
  (mapeado al soportado más cercano), y un auditor que falla si falta una clave en algún idioma.

## 2. Lo que hay hoy (el inventario)

**No existe ningún sistema de idiomas.** Ni librería, ni catálogo, ni detección. `<html lang="es">`
fijo (`app/layout.tsx`), dictado en `es-MX` (`lib/useSpeech.ts`), y ningún `Intl`: fechas, números y
dinero están escritos a mano en español (`lib/fechas.ts`, `money()` de `TusNumeros`, `pesos()` de
`numerosVivo`, el separador de miles es el punto).

| superficie | tamaño medido | dónde vive |
|---|---|---|
| Textos de pantalla (`app/**/*.tsx`) | ~1.050 cadenas distintas en 58 archivos (~1.180 con repetidas); al unir frases partidas por `<em>`/`<br>`, ~850 a 900 claves | los más grandes: `ManosALaObra` 161, `TusNumeros` 96, `Landing` 54, `Calendario` 63, `IdeaView` 53, `login` 48, `DetalleActividad` 45, `AnalisisPapel` 45, `creditos` 40 |
| Textos de `lib/` que llegan a pantalla | ~410 cadenas en ~40 archivos (sin contar prompts) | `bloqueRealidad` 54, `bitacoraCliente` 40, `expediente` 39, `readiness` 38, `reporte` 32, `engine/constants` 25, `analytics` 23, `hitosEspacio` 15 |
| Mensajes del servidor al usuario | ~100 distintos en 41 rutas, más ~15 constantes compartidas (`mensajeSaldoInsuficiente`, `mensajeLimite`, `MENSAJE_FUSIBLE`, `AVISO_LOGIN`, `AVISO_2FA`, `murallaSinPlan`, `MENSAJE_LECTURA_FALLIDA`, `AVISO_VERSION_BASICA`, `ERROR_GENERICO`...) | `cuenta/2fa/*` ~51, `documentos` 13, `session/[id]/plan` 13, `checklist` 10 a 15, `follow` 11 |
| Correos | **1 en código** (código de 2FA por correo, Resend por `fetch`); **3 plantillas de Supabase** (confirmar cuenta, reenviar, recuperar contraseña) configuradas en el tablero de Supabase, fuera del repo | `api/cuenta/2fa/email/enviar/route.ts` |
| Documentos (PDF) | No hay librería de PDF: el PDF es `window.print()` de los componentes de papel. Generadores en markdown ~220 cadenas; componentes de papel ~90 | `expediente.ts`, `reporte.ts`, `bitacoraCliente.ts`, `analytics.ts`, `acta.ts`, `registroProteccion.ts`, `AnalisisPapel`, `Descargas`, `GraficosAnalisis`, `GanttCumplimiento`, `ResumenPapel`, `BitacoraPapel`, `PlanDocumento` |
| Textos legales | **No existen.** Los enlaces "Privacidad" y "Términos" de la portada apuntan a `#`. Hay materia prima en BANCO §4, §5 y §7 (~1.000 palabras) | `app/ui/Landing.tsx` |
| SEO | 2 bloques de metadatos (layout y portada). Sin `generateMetadata`, OpenGraph, `robots`, `sitemap` ni `manifest` | `app/layout.tsx`, `app/page.tsx` |
| Calendario | `PRODID ...//ES`, "Etapa N · idea", "Tu viaje", "Calendario no encontrado."; los textos de las tareas vienen de la base (generados en español) | `lib/ics.ts`, `api/calendar/feed/[token]` |
| Prompts de la IA | 12 sincronizados desde `engine/prototipo_motor.py` a `web/lib/assets/prompts.json` + 3 nativos en `web/lib/prompts.ts`. **Ninguno pide responder en el idioma del usuario**; solo 4 fijan el español de forma explícita (`SYSTEM_PLAN` reglas 13 y 14, `SYSTEM_ESTADO_VIVO`, `SYSTEM_REPORTE`, `SYSTEM_DIAGNOSTICO_MUNDO`); los demás salen en español porque el prompt y el grafo lo están | ver §5 |
| Contenido del grafo que llega **sin pasar por la IA** | `etiqueta_arbol` en 3.169 nodos activos (~95 mil caracteres) en el riel y el cintillo; **3.569 preguntas** en `preguntas_cache.json` (~871 mil caracteres) que se muestran tal cual en la primera pregunta de un mundo, en la reelección de puerta y cuando el intérprete no adapta; 9 mundos (`nombre` y `promesa`) en `packs_catalog.json`; 65 semillas en `packs_entry_seeds.json` | ver decisión D3 |
| Guardias que fijan frases en español | ~83 archivos de prueba con ~395 aserciones de texto (el mayor: `expediente.test` 34, `bloqueRealidad.test` 34, `accesosResueltos.test` 20, `DetalleActividad.test` 19) | pasan a correr por idioma (F6) |

**Conteo para el catálogo:** ~1.300 a 1.450 claves de interfaz (pantalla + `lib` + servidor), cada
una en 11 idiomas: unas 15.000 cadenas. Aparte, el contenido (grafo, preguntas, planes) va por la IA
o por la decisión D3, no por el catálogo.

## 3. Arquitectura propuesta (calco del I Ching, con el español de base)

### 3.1 El catálogo
- **Sin librería** (igual que el I Ching, que prohíbe `next-intl` en su `CLAUDE.md`): un módulo
  propio `web/lib/i18n/` con `locales.ts` (`LOCALES = [es, en, pt, fr, de, it, ja, zh, ko, ar, hi]`,
  **`LOCALE_BASE = "es"`**), `interpolar()` para `{{clave}}`, y catálogos TypeScript por área
  (`mensajes/manos.ts`, `mensajes/numeros.ts`, `mensajes/servidor.ts`...), cada uno un
  `Record<Locale, T>` completo con su getter.
- **El tipo es el primer auditor:** si falta un idioma o una clave, no compila (el guardián de
  commit ya corre tsc).
- **El auditor** (`scripts/auditor_i18n.ts`, en la suite y en el guardián) cierra lo que el I Ching
  dejó abierto: prohíbe `Partial<Record<Locale`; exige las mismas claves en los 11 idiomas; exige los
  mismos `{{marcadores}}` en cada traducción; prohíbe cadenas vacías; exige que las marcas del
  glosario marcadas "no se traducen" aparezcan intactas; y exige que la lista `hreflang` sea igual a
  `LOCALES`.
- **Plurales y géneros** por funciones de formato con `Intl.PluralRules` (los "crédito/créditos" de
  hoy), no por concatenación.

### 3.2 Cómo se elige el idioma de la interfaz
- **La preferencia vive en la cookie** `myidea_idioma` (`path=/; max-age=1 año; samesite=lax`,
  legible por el cliente), como en el I Ching. **D9:** además, `?lang=xx` en la URL manda en esa
  visita y actualiza la cookie; los `hreflang` apuntan a esas variantes.
- **Primera visita:** `proxy.ts` (donde ya vive la identidad invisible), sin cookie, negocia el
  `Accept-Language` (orden por `q`, subetiqueta primaria: `pt-BR→pt`, `zh-TW→zh`, `fr-CA→fr`) y
  **cae al español** si no hay coincidencia. Después manda la cookie.
- Selector de idioma con cada nombre en su propia escritura ("日本語", "العربية"). Cambiar escribe la
  cookie, pone `lang`/`dir` en `<html>` y refresca.
- **Servidor:** las rutas leen la cookie para sus mensajes.

### 3.3 Dos idiomas distintos: el de la interfaz y el del proyecto
- **Idioma de interfaz:** preferencia del usuario (cookie). Manda en botones, menús y mensajes.
- **Idioma del proyecto:** se detecta del texto original de la idea y se guarda en el proyecto
  (columna nueva `projects.idioma`, migración en F5). Manda en todo lo que genera la IA y en los
  documentos de ese proyecto.
- Ver D2: qué pasa cuando no coinciden.

### 3.4 Formatos
- `web/lib/i18n/formato.ts`: fechas (`fechaHumana`, `fechaSello`, "hace N min"), números, porcentajes
  y dinero con `Intl.DateTimeFormat`, `Intl.NumberFormat` y `Intl.RelativeTimeFormat` por idioma. Se
  reescriben los ~49 usos de `lib/fechas.ts` y los `money()` / `pesos()` / `toFixed(1)` sobre esa base.
  En español el resultado debe salir idéntico al de hoy (prueba de F2).
- `zh` se etiqueta `zh-Hans`; `fr` neutral, válido para Quebec (sin giros exclusivos de Francia).

### 3.5 Escrituras especiales
- **Árabe:** `dir="rtl"` en `<html>` solo para `ar`. Hay 69 clases físicas de dirección en 24
  archivos (`ml-`, `mr-`, `pl-`, `pr-`, `left-`, `right-`, `text-left`, `rounded-l`...), que pasan a
  las lógicas de Tailwind 4 (`ms-`, `me-`, `ps-`, `pe-`, `start-`, `end-`, `text-start`); los
  gráficos (Gantt, línea de avance) se revisan uno por uno.
- **Tipografías:** Noto Sans JP, SC, KR y Devanagari con `next/font`, cargadas en el layout **solo**
  cuando la cookie elige ese idioma.

### 3.6 SEO
- Metadatos por idioma con `generateMetadata`. `hreflang` para los 11 más `x-default`. Ver D9 (con
  el idioma en cookie, el buscador solo ve el idioma por defecto).

## 4. Correos, documentos y textos legales
- **Correo de 2FA:** asunto y cuerpo desde el catálogo, en el idioma de la cookie.
- **Correos de Supabase:** ver D4.
- **Documentos:** los componentes de papel usan el catálogo como la pantalla. Los generadores de
  markdown (`expediente`, `acta`, `registro`, `bitácora`, informe) reciben el idioma **del proyecto**.
- **Legales:** ver D5.

## 5. La IA en el idioma del usuario (F5)
- **Detección:** como el I Ching (`detect-input-language.ts`): primero el alfabeto (árabe,
  devanagari, hangul, kana, han), luego palabras vacías en alfabeto latino, y en empate el idioma de
  la interfaz. El dictado arranca con el idioma de la interfaz; el texto dictado pasa por la misma
  detección.
- **Los prompts:** cada prompt que produce texto para el usuario gana una regla final,
  `IDIOMA DE SALIDA: responde solo en {idioma}; los nodos que recibes están en español, úsalos como
  fuente y exprésalos en {idioma}`, y las reglas que hoy dicen "español" pasan a "el idioma de
  salida". Los que producen JSON interno no cambian. Se editan en `engine/` y se sincronizan (la
  fase F5 es la que autoriza tocar `engine/`).
- **Lo que hoy se rompería:** los analizadores que leen encabezados en español de la salida de la
  IA (`checklist.ts` con `## Etapa N:` y `**Esta semana:**`, `planParser.ts`, el título de la
  sección económica, `previewMundos.ts`, las listas de palabras de `readiness.ts`, el detector de
  acentos). F5 cambia esos marcadores por **marcadores neutros** que la IA escribe siempre igual y la
  pantalla pinta en su idioma.
- **Generadores sin IA** que necesitan plantilla por idioma: `ensamblarOffline` (el plan básico),
  `reporteOffline`, `construirBloqueRealidad`, `componerMensajeSeguimiento`, `construirMarkdown` de la
  Claridad, `TEXTO_FAMILIA_FALTANTE`, `AVISO_VERSION_BASICA`, `decisionPorPalabras`.
- **El buscador:** Voyage `voyage-4-lite`, que es multilingüe. El índice (`semantic_index.json`) está
  hecho con el texto en español de los nodos; la consulta es el texto crudo del usuario. F1 mide si
  una idea en coreano recupera los mismos nodos que en español.

## 6. Glosario de marca (APROBADO por el fundador el 26 sep 2026, con sus ajustes; pendiente la revisión de naturalidad antes de F3)

**Reglas propuestas:**
- **"My Idea" no se traduce** en ningún idioma.
- Registro: el tú del español se mantiene donde el idioma lo admite en una app (`fr` tu, `de` du,
  `it` tu, `pt` você); `ja` cortés (です/ます), `ko` 해요체, `ar` árabe estándar moderno, `hi` आप.
- Las variantes: `pt` de Brasil, `zh` simplificado, `fr` neutral válido para Quebec.

### Las etapas (el paso a paso tiene seis hitos: las cinco etapas y Realizado)

| es | en | pt | fr | de | it | ja | zh | ko | ar | hi |
|---|---|---|---|---|---|---|---|---|---|---|
| La Chispa | The Spark | A Faísca | L'Étincelle | Der Funke | La Scintilla | ひらめき | 灵光一闪 | 불꽃 | الشرارة | चिंगारी |
| Claridad | Clarity | Clareza | Clarté | Klarheit | Chiarezza | 明確さ | 清晰 | 명확함 | الوضوح | स्पष्टता |
| La Exploración | Exploration | A Exploração | L'Exploration | Die Erkundung | L'Esplorazione | 探求 | 探索 | 탐색 | الاستكشاف | अन्वेषण |
| Tu Plan | Your Plan | Seu Plano | Ton plan | Dein Plan | Il tuo piano | あなたのプラン | 你的计划 | 나의 계획 | خطتكم | आपकी योजना |
| Manos a la Obra | Get to Work | Mãos à Obra | À l'ouvrage | Ans Werk | Al lavoro | 実行 | 动手做 | 실행하기 | إلى العمل | काम शुरू करें |
| Realizado | Achieved | Realizado | Réalisé | Verwirklicht | Realizzato | 実現 | 已实现 | 실현 | تحقّق | साकार |

### Los nueve mundos

| es | en | pt | fr | de | it | ja | zh | ko | ar | hi |
|---|---|---|---|---|---|---|---|---|---|---|
| Calidad y Confianza | Quality & Trust | Qualidade e Confiança | Qualité et confiance | Qualität & Vertrauen | Qualità e Fiducia | 品質と信頼 | 质量与信任 | 품질과 신뢰 | الجودة والثقة | गुणवत्ता और भरोसा |
| Seguridad y Personas | Safety & People | Segurança e Pessoas | Sécurité et personnes | Sicherheit & Menschen | Sicurezza e Persone | 安全と人 | 安全与人 | 안전과 사람 | السلامة والناس | सुरक्षा और लोग |
| Ambiente y Futuro | Environment & Future | Ambiente e Futuro | Environnement et avenir | Umwelt & Zukunft | Ambiente e Futuro | 環境と未来 | 环境与未来 | 환경과 미래 | البيئة والمستقبل | पर्यावरण और भविष्य |
| Seguridad Digital | Digital Security | Segurança Digital | Sécurité numérique | Digitale Sicherheit | Sicurezza Digitale | デジタルセキュリティ | 数字安全 | 디지털 보안 | الأمن الرقمي | डिजिटल सुरक्षा |
| Vender al Mundo | Sell to the World | Vender para o Mundo | Vendre au monde | Weltweit verkaufen | Vendere al Mondo | 世界に売る | 卖向世界 | 세계로 팔기 | البيع للعالم | दुनिया को बेचना |
| Multiplica tu Negocio | Multiply Your Business | Multiplique seu Negócio | Multiplie ton entreprise | Vervielfache dein Geschäft | Moltiplica la tua Attività | ビジネスを広げる | 让生意倍增 | 사업 확장 | ضاعف عملك | अपना व्यवसाय बढ़ाएँ |
| Riesgos Bajo Control | Risks Under Control | Riscos sob Controle | Risques sous contrôle | Risiken im Griff | Rischi sotto Controllo | リスクを管理下に | 风险可控 | 위험 관리 | المخاطر تحت السيطرة | जोखिम नियंत्रण में |
| Tu Compra Correcta | The Right Purchase | Sua Compra Certa | Ton bon achat | Richtig einkaufen | Il tuo Acquisto Giusto | 正しい仕入れ | 正确采购 | 올바른 구매 | شراؤكم الصحيح | आपकी सही खरीद |
| Del Taller a sus Manos | From Workshop to Customer | Da Oficina às Mãos Deles | De l'atelier à leurs mains | Von der Werkstatt in ihre Hände | Dal Laboratorio alle loro Mani | 工房からお客様の手へ | 从作坊到客户手中 | 공방에서 고객의 손까지 | من الورشة إلى أيديهم | कार्यशाला से उनके हाथों तक |

(El mundo 11, `primer_equipo`, está registrado en el Gate 0 pero aún no integrado en la app: su
nombre entra al glosario cuando se integre.)

### Conceptos propios

| es | en | pt | fr | de | it | ja | zh | ko | ar | hi |
|---|---|---|---|---|---|---|---|---|---|---|
| My Idea | My Idea | My Idea | My Idea | My Idea | My Idea | My Idea | My Idea | My Idea | My Idea | My Idea |
| Tus Números | Your Numbers | Seus Números | Tes chiffres | Deine Zahlen | I tuoi numeri | あなたの数字 | 你的数字 | 나의 숫자 | أرقامكم | आपके आंकड़े |
| Potencia tu idea | Power up your idea | Potencialize sua ideia | Propulse ton idée | Stärke deine Idee | Potenzia la tua idea | アイデアを強化 | 为你的想法赋能 | 아이디어 강화 | عزّزوا فكرتكم | अपने विचार को सशक्त करें |
| Ciclo de profundización | Deepening Cycle | Ciclo de aprofundamento | Cycle d'approfondissement | Vertiefungszyklus | Ciclo di approfondimento | 深掘りサイクル | 深化循环 | 심화 사이클 | دورة التعمّق | गहराई चक्र |
| Expediente | Full Record | Dossiê | Dossier | Dossier | Fascicolo | 全記録 | 完整档案 | 전체 자료 | الملف الكامل | पूरा ब्यौरा |
| Bitácora | Logbook | Diário de bordo | Journal de bord | Logbuch | Diario di bordo | 活動ログ | 日志 | 기록장 | سجلّ الرحلة | लॉगबुक |
| Cierre honesto | Honest Close | Encerramento honesto | Clôture honnête | Ehrlicher Abschluss | Chiusura onesta | 正直な締めくくり | 坦诚收尾 | 솔직한 마무리 | إغلاق صادق | ईमानदार समापन |
| Mundos | Worlds | Mundos | Mondes | Welten | Mondi | ワールド | 世界 | 월드 | العوالم | दुनियाएँ |
| Créditos | Credits | Créditos | Crédits | Guthaben | Crediti | ポイント | 点数 | 크레딧 | رصيد | क्रेडिट |
| Tu viaje (el núcleo) | Your Journey | Sua Jornada | Ton parcours | Deine Reise | Il tuo viaggio | あなたの旅 | 你的旅程 | 나의 여정 | رحلتكم | आपकी यात्रा |
| A mi ritmo | At my own pace | No meu ritmo | À mon rythme | In meinem Tempo | Al mio ritmo | 自分のペースで | 按我的节奏 | 내 속도대로 | على وتيرتي | अपनी गति से |
| Con fechas | With dates | Com datas | Avec des dates | Mit Terminen | Con date | 日付あり | 按日期 | 날짜와 함께 | مع مواعيد | तारीखों के साथ |

Los nombres de las recargas (Recarga, Básico, Premium, Profesional) y los cinco estados de una tarea
(pendiente, empezado, en proceso, hecho, no aplica) entran al catálogo como texto de interfaz, no
como marca: se traducen en F3 con el mismo glosario.

### Revisión de naturalidad (segundo modelo, 26 sep 2026)

Un segundo modelo revisó el glosario idioma por idioma. Los cuatro términos que fijó el fundador
no se tocaron.

**Aplicado (evidente):**
- de "Credits" → **"Guthaben"**: era la única entrada que dejaba la palabra en inglés; "Guthaben"
  es el término alemán para saldo prepago.
- ja "クレジット" → **"ポイント"**: クレジット se lee como tarjeta de crédito; las apps japonesas usan
  ポイント para saldo prepago.
- zh "灵感火花" → **"灵光一闪"**: el primero es un compuesto artificial; el segundo es la expresión
  establecida ("chispazo de inspiración").
- hi "दुनिया को बेचें" → **"दुनिया को बेचना"**: era la única entrada en imperativo; los nombres de
  mundo van en forma nominal.
- ar, todo el glosario: el posesivo e imperativo masculino singular (ـك) pasa al **plural neutro**
  (ـكم): خطتكم، أرقامكم، رحلتكم، شراؤكم الصحيح، عزّزوا فكرتكم. Es la regla D7: formas neutras primero.

**Discutible: APROBADO por el fundador el 26 sep 2026 tal como lo propuso el revisor** (ya aplicado
en las tablas):
- en "The Exploration" → "Exploration" (sin artículo, como "Clarity").
- fr "Ton achat juste" → "Ton bon achat" ("faire un bon achat" es la colocación natural).
- de "Gesamtakte" → "Dossier" ("Akte" suena a expediente burocrático).
- de "Gib deiner Idee Kraft" → "Stärke deine Idee" (más corto e idiomático).
- it "Mani all'opera" → "Al lavoro" (el revisor lo ve como calco del español).
- ja "明確化" → "明確さ" (cualidad y no proceso, como "Claridad").
- ko "전체 기록" → "전체 자료" (para no compartir raíz con "기록장", la bitácora).
- hi "काम पर" → "काम शुरू करें" (para que suene a llamada a la acción).

## 7. Decisiones del fundador (26 sep 2026)

- **D1. Glosario APROBADO** con cuatro ajustes, ya aplicados en §6: en inglés "Get to Work" (no
  "Hands On") y "From Workshop to Customer"; en francés "Propulse ton idée" (sin anglicismos: el
  mercado francés es Quebec); en alemán "Richtig einkaufen". **Antes de F3**, un segundo modelo
  revisa la naturalidad del glosario en cada idioma y lista lo que cambiaría: lo evidente se aplica,
  lo discutible sube al fundador.
- **D2. APROBADA.** La interfaz sigue la preferencia del usuario; el plan y los documentos siguen el
  idioma del proyecto.
- **D3. APROBADAS las dos.** Las etiquetas del riel van en una traducción **derivada** por idioma
  (archivos aparte, el grafo no se toca), y fuera del español las preguntas las adapta la IA. **El
  auditor exige etiqueta en cada idioma para todo nodo vivo**; al cambiar el grafo, se regeneran
  solo las que falten.
- **D4. SÍ al Send Email Hook** de Supabase, con Resend y el catálogo. Los pasos exactos de
  configuración en Supabase se entregan al fundador cuando llegue esa fase (F6).
- **D5. Textos legales:** borradores en español de Términos, Privacidad y Cookies para un negocio
  registrado en Quebec, Canadá, marcados **BORRADOR PENDIENTE DE REVISIÓN PROFESIONAL**, en
  `docs/legal/`, construidos sobre un **inventario de datos** (`docs/legal/INVENTARIO_DATOS.md`) y con
  la comprobación del **borrado real** de la cuenta. Los enlaces de la app **no** apuntan a ellos hasta
  que el fundador los apruebe. La versión francesa será obligatoria.
- **D6. APROBADA** la propuesta (formato por idioma con `Intl`, símbolo "$" por ahora). La moneda por
  proyecto es **función futura**, con su ficha en PENDIENTES.
- **D7. APROBADA:** `pt` de Brasil, `zh` simplificado, `fr` neutral válido para Quebec y el registro
  de §6. En árabe, **formas neutras primero**, y el masculino gramatical solo cuando no haya
  alternativa.
- **D8. APROBADA.** BANCO_DE_TEXTOS es el canon en español; en los otros idiomas, el catálogo; las
  guardias de frases prohibidas corren sobre cada uno.
- **D9. SÍ a `?lang=xx` en la URL**, con los `hreflang` apuntando a esas variantes (la cookie sigue
  siendo la preferencia; el parámetro manda sobre ella en esa visita y la actualiza).

## 8. Plan por fases

| fase | qué | toca | quién hace falta |
|---|---|---|---|
| F0 | este documento | solo `docs/` | glosario y decisiones: el fundador |
| F1 | 20 ideas × 11 idiomas contra `buscarAfines`; acuerdo por idioma con la versión en español (solape de los primeros 10 nodos); si alguno recupera mal, se mide también traducir la consulta al español antes de buscar | un script de medición, sin cambios en la app | el fundador con la clave de Voyage |
| F2 | `lib/i18n/`, auditor, cookie y negociación en `proxy.ts`, formatos con `Intl`, y **todos** los textos extraídos al catálogo en español; la app se ve idéntica (capturas antes y después) | `web/` | visto en la vista previa. **HECHA, pendiente del visto** (27 sep 2026): ver `F2_INFORME.md` |
| F3 | las otras 10 traducciones con el glosario; formatos por idioma | catálogos | visto |
| F4 | árabe RTL; tipografías CJK y devanagari solo al elegirlas; capturas de cada una | `web/` | visto |
| F5 | detección del idioma de la idea, `projects.idioma` (migración), prompts con idioma de salida, marcadores neutros en el plan, plantillas por idioma de los generadores sin IA, y D3; prueba: una idea en coreano y otra en árabe dan plan y respuestas en su idioma con los nodos correctos | `web/`, `engine/` (prompts), `supabase/` | visto; migración la aplica el fundador |
| F6 | correos (D4), documentos, legales (D5), SEO y `hreflang` (D9); auditor y guardias de frases por idioma | `web/` | visto |
