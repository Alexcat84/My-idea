/**
 * prompts.ts - Fase 3.0: los SYSTEM prompts de engine/prototipo_motor.py,
 * re-exportados byte a byte desde web/lib/assets/prompts.json.
 *
 * Por que via JSON y no retipeados como template literals: cualquier
 * transcripcion manual de miles de palabras arriesga una diferencia
 * invisible a simple vista (un espacio, una comilla tipografica, un
 * caracter de mas) que rompe el prompt caching sin dar ningun error --
 * el prefijo cacheado en Anthropic deja de coincidir byte a byte y cada
 * llamada se factura como si no hubiera cache. web/lib/assets/prompts.json
 * se genera con scripts/sync_assets_web.py leyendo las constantes
 * SYSTEM_* directamente del modulo Python, asi que la igualdad byte a
 * byte esta garantizada por construccion, no por revision manual.
 * prompts.test.ts verifica el checksum contra el manifest igual que los
 * demas assets sincronizados.
 *
 * Correr `python scripts/sync_assets_web.py` despues de CUALQUIER cambio
 * a un SYSTEM_* en prototipo_motor.py para mantener esto al dia.
 */
import promptsJson from "./assets/prompts.json";

interface PromptsShape {
  SYSTEM_CLASIFICACION: string;
  SYSTEM_PUERTA_AVANZADA: string;
  SYSTEM_INTERPRETE_MULTI: string;
  SYSTEM_PROFUNDIZAR: string;
  SYSTEM_PREGUNTA_DIRIGIDA: string;
  SYSTEM_PLAN: string;
  SYSTEM_ESTADO_VIVO: string;
  SYSTEM_JUEZ_SESION: string;
  SYSTEM_ORGANIZADOR: string;
  SYSTEM_REPORTE: string;
  SYSTEM_CLASIFICAR_OFERTA: string;
  SYSTEM_DIAGNOSTICO_MUNDO: string;
}

const prompts = promptsJson as PromptsShape;

export const SYSTEM_CLASIFICACION = prompts.SYSTEM_CLASIFICACION;
export const SYSTEM_PUERTA_AVANZADA = prompts.SYSTEM_PUERTA_AVANZADA;
export const SYSTEM_INTERPRETE_MULTI = prompts.SYSTEM_INTERPRETE_MULTI;
export const SYSTEM_PROFUNDIZAR = prompts.SYSTEM_PROFUNDIZAR;
export const SYSTEM_PREGUNTA_DIRIGIDA = prompts.SYSTEM_PREGUNTA_DIRIGIDA;
export const SYSTEM_PLAN = prompts.SYSTEM_PLAN;
export const SYSTEM_ESTADO_VIVO = prompts.SYSTEM_ESTADO_VIVO;
export const SYSTEM_JUEZ_SESION = prompts.SYSTEM_JUEZ_SESION;
export const SYSTEM_ORGANIZADOR = prompts.SYSTEM_ORGANIZADOR;
export const SYSTEM_REPORTE = prompts.SYSTEM_REPORTE;
export const SYSTEM_CLASIFICAR_OFERTA = prompts.SYSTEM_CLASIFICAR_OFERTA;
export const SYSTEM_DIAGNOSTICO_MUNDO = prompts.SYSTEM_DIAGNOSTICO_MUNDO;

/**
 * SYSTEM_ESTIMACION_BANDA — Scheduler Inteligente, estimador de esfuerzo.
 *
 * PROCEDENCIA: los CRITERIOS DE BANDA (S/M/L/XL + espera_externa) son EL PROMPT
 * VALIDADO EN F0 (spike de estimación, 97.2% exacta-o-adyacente a nivel ítem,
 * bendecido por el fundador). Este prompt NO viene del sync de Python (nació en
 * TS en F0): por eso es una const nativa aquí y no una clave de
 * assets/prompts.json. Los criterios de banda se conservan palabra por palabra
 * respecto de scripts/spike_estimacion.ts; lo ÚNICO que cambia es el
 * empaquetado: el spike estimaba UNA tarea y devolvía un objeto; producción
 * estima el LOTE de un plan en UNA llamada (tres corridas = mayoría-de-3) y
 * devuelve un ARRAY con el id de cada tarea. Editar los criterios de banda
 * exige re-correr el spike (`npm run spike -- items`) y re-medir la puerta.
 */
/**
 * SYSTEM_REFORMULADOR_PROTECCION — Mundos de protección (P2b): EL ANCLAJE.
 *
 * PROCEDENCIA: nace en TS y NO toca ningún prompt del motor. Se escribió así a
 * propósito: los doce SYSTEM_* de engine/prototipo_motor.py son GLOBALES y los
 * comparte toda entrevista del producto, el núcleo incluido; meterles el
 * snapshot habría cambiado entrevistas que esta campaña promete no tocar. Y las
 * preguntas de los turnos no las escribe un modelo: salen del caché del grafo.
 * Por eso esto es un reformulador que corre DESPUÉS, solo en los tres mundos de
 * protección.
 *
 * BARANDA (a), la que define la pieza: ANCLA, jamás cambia QUÉ se pregunta. La
 * pregunta del grafo trae una intención metodológica que costó construir; esto
 * solo la apunta a la actividad concreta de la persona. Si ninguna encaja, la
 * devuelve tal cual: forzar un anclaje sería peor que no anclar.
 */
export const SYSTEM_REFORMULADOR_PROTECCION = [
  "PROHIBIDO usar guiones largos o medios (— o –) en cualquier texto que escribas:",
  "usa comas, dos puntos o parentesis.",
  "",
  "Recibes UNA pregunta de una entrevista de proteccion (riesgos, seguridad y",
  "salud, o seguridad digital) y la lista numerada de las ACTIVIDADES REALES del",
  "plan de la persona.",
  "",
  "Tu unico trabajo es ANCLARLA: reformula la pregunta apuntandola a la actividad",
  "concreta del snapshot (su numero #N y su titulo), CONSERVANDO INTACTA su",
  "intencion metodologica. Lo que la pregunta busca averiguar no cambia; solo",
  "cambia que ahora habla de algo que la persona de verdad va a hacer.",
  "",
  "Si NINGUNA actividad aplica a esa pregunta, DEVUELVELA TAL CUAL, palabra por",
  "palabra. Forzar un anclaje que no existe es peor que no anclar.",
  "",
  "Reglas: UNA sola pregunta, en segunda persona, sin explicar teoria antes, sin",
  "comillas y sin JSON. Menciona la actividad por su titulo (puedes citar su #N).",
  "Responde SOLO el texto de la pregunta.",
].join("\n");

/**
 * SYSTEM_ENLACE_PROTECCION — Mundos de protección (P2): el ENLAZADOR.
 *
 * PROCEDENCIA: nace en TS, como el estimador (por eso es una const nativa y no
 * una clave de assets/prompts.json: no viene del sync de Python). Es una SEGUNDA
 * llamada, hermana de la estimación de F1: el plan del mundo ya está escrito y
 * el usuario ya lo vio; esto solo lo lee y dice qué protege a qué. La forma
 * (segunda llamada, no estructura dentro de la prosa) fue adjudicada por el
 * fundador y el auditor: la coincidencia de texto quedó rechazada con nombre,
 * porque adivinar no es enlazar.
 *
 * El vocabulario de severidad es CERRADO y viene del propio grafo (nodo "la
 * matriz de colores te engaña"): nada de puntajes. Lo que se salga del enum se
 * descarta en el validador, no se aproxima.
 */
export const SYSTEM_ENLACE_PROTECCION = [
  "Eres el enlazador de un plan de PROTECCIÓN (riesgos, seguridad y salud, o",
  "seguridad digital) que se aplica SOBRE las actividades reales de un plan de",
  "negocio de una persona sola.",
  "",
  "Recibes DOS listas numeradas:",
  "- ACTIVIDADES DEL NÚCLEO: lo que la persona va a hacer de verdad (#1, #2…).",
  "- RESPUESTAS DEL PLAN DE PROTECCIÓN: las acciones del plan nuevo (#1, #2…).",
  "",
  "Por CADA respuesta dices tres cosas:",
  "1. LA DETECCIÓN que la originó, en UNA frase corta y concreta, en palabras de",
  "   persona (ejemplo: 'depende de un solo proveedor').",
  "2. A QUÉ ACTIVIDAD del núcleo protege: el número de esa actividad. Si protege",
  "   al negocio entero y no a una actividad concreta, devuelve null.",
  "3. La SEVERIDAD en palabras, JAMÁS en números ni colores:",
  "   probabilidad: poco_probable | probable | muy_probable",
  "   dolor: poco | bastante | mucho",
  "",
  "Reglas duras:",
  "- El número de actividad tiene que existir en la lista que te di. Si dudas,",
  "  devuelve null: inventar un número es peor que decir que es del negocio entero.",
  "- PROHIBIDO devolver puntajes, porcentajes, colores o escalas numéricas de",
  "  riesgo. Una matriz de colores finge una precisión que no existe.",
  "- PROHIBIDO usar guiones largos o medios.",
  "",
  "Responde SOLO un array JSON, sin una palabra más, con EXACTAMENTE un objeto",
  "por respuesta, con esta forma EXACTA:",
  '[{"item_orden":1,"deteccion":"depende de un solo proveedor","protege_indice":3,"probabilidad":"probable","dolor":"mucho"}]',
].join("\n");

export const SYSTEM_ESTIMACION_BANDA = [
  "Eres un estimador de esfuerzo para un plan de negocio de una persona sola.",
  "Clasificas CADA tarea de una lista en una BANDA de esfuerzo, con RANGOS",
  "honestos, JAMÁS un número de horas.",
  "",
  "Bandas (elige EXACTAMENTE una por tarea):",
  "- S: cabe en una sentada de una hora o menos.",
  "- M: dos a cuatro horas.",
  "- L: una jornada completa de trabajo.",
  "- XL: varios días de trabajo.",
  "",
  "Además, por cada tarea: ¿DEPENDE de terceros y por eso arrastra tiempo de",
  "ESPERA (aunque el esfuerzo propio sea poco)? Ejemplo: 'envía correos y espera",
  "respuestas' es poco esfuerzo pero tiene espera externa. Devuelve espera_externa.",
  "",
  "Recibes un array JSON de tareas, cada una con su id y su texto. Responde SOLO",
  "un array JSON, sin una palabra más, con EXACTAMENTE un objeto por tarea, con",
  "esta forma EXACTA (respeta el id que te di):",
  '[{"id":0,"banda":"S","espera_externa":false},{"id":1,"banda":"XL","espera_externa":true}]',
  "PROHIBIDO devolver horas numéricas o cualquier texto fuera del array JSON.",
].join("\n");
