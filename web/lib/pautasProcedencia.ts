/**
 * LAS PAUTAS DE PROCEDENCIA, en un solo sitio (PROXIMOS_PASOS §6, punto 3; 7 oct 2026). Regla dura D1 de
 * docs/REGLAS_DE_LA_CASA.md: JAMÁS un usuario debe saber, ni poder intuir, de dónde provienen las respuestas de la
 * app; y D5: un método se nombra y se explica, nunca se atribuye.
 *
 * Antes vivían dentro de las pruebas (lib/procedencia.test.ts y engine/test_procedencia_nombres.py). Ahora:
 *  - lib/procedencia.test.ts importa de aquí el prefijo, la atribución genérica y las personas;
 *  - lib/guardasContenido.ts las vuelca a dataset/metadata/guardas_contenido.json (desde la versión 1.1.0), con sus
 *    fixtures `caza` y `no_caza`;
 *  - engine/test_procedencia_nombres.py lee del JSON las formas de nombre propio;
 *  - la forja copia el JSON y su aduana rechaza el candidato que las incumpla.
 * Si cambia una pauta, se sube VERSION_GUARDAS y se regenera el fichero.
 */

/** El prefijo de procedencia en los once idiomas (fundador, 30 sep 2026: el texto visible queda limpio). */
export const PREFIJO_PROCEDENCIA = /sugerencia de my idea|suggestion (?:from|de|by) my idea|my idea suggest|sugest[aã]o (?:da|de|do) my idea|vorschlag (?:von|aus) my idea|suggerimento (?:di|da) my idea|my idea(?:の提案|の提案|建议|의 제안| का सुझाव)|اقتراح my idea/i;

/**
 * Atribuir un consejo a estudios, investigaciones, expertos o la literatura insinúa un origen (D1). Se dice
 * directamente. Los patrones no muerden las instrucciones al usuario ("busca en la literatura", "según los datos
 * obtenidos", "no se ha probado con usuarios"): solo la atribución de un hecho.
 */
const VERBO_ES = "(?:muestra|muestran|demuestra|demuestran|demostr[oó]|demostraron|indica|indican|revela|revelan|sugiere|sugieren|confirma|confirman|ha mostrado|han mostrado|ha demostrado|han demostrado|encontr[oó]|encontraron|señala|señalan)";
export const ATRIBUCION_GENERICA: readonly RegExp[] = [
  // español
  new RegExp(`\\b(?:un|el|los|varios|algunos|diversos|numerosos|muchos) estudios? ${VERBO_ES}`, "i"),
  new RegExp(`\\b(?:la|las) investigaci(?:ón|on|ones) ${VERBO_ES}`, "i"),
  new RegExp(`\\b(?:la evidencia|la ciencia) ${VERBO_ES}`, "i"),
  /\bseg[uú]n (?:los |las |la |el |diversos |varios |algunos )?(?:expertos|especialistas|estudios|investigaciones|investigaci[oó]n|la literatura|investigadores|autores|analistas|estudios citados)/i,
  /\blos (?:expertos|especialistas|investigadores|analistas) (?:recomiendan|coinciden|sugieren|dicen|afirman|advierten|han encontrado|encontraron)/i,
  /\b(?:est[aá]|ha sido|se ha) (?:demostrado|comprobado) que/i,
  // los otros diez idiomas de la interfaz
  /\b(?:studies|research|evidence) (?:shows?|suggests?|has shown|have shown|proves?|indicates?)\b|\bexperts (?:recommend|agree|say)\b|\baccording to (?:studies|research|experts)\b/i,
  /\b(?:les études|la recherche) (?:montrent|montre|suggèrent|suggère)\b|\bselon (?:les experts|des études|les études)\b/i,
  /\b(?:estudos|a pesquisa) (?:mostram|mostra|sugerem|sugere)\b|\bsegundo (?:especialistas|estudos|os especialistas)\b/i,
  /\b(?:studien|die forschung) (?:zeigen|zeigt|belegen|belegt)\b|\blaut (?:studien|experten)\b|\bexperten empfehlen\b/i,
  /\b(?:gli studi|la ricerca) (?:mostrano|mostra|dimostrano|dimostra|suggeriscono)\b|\bsecondo (?:gli esperti|gli studi|studi)\b/i,
  /研究によると|研究では|専門家によると|研究表明|研究显示|专家建议|据研究|연구에 따르면|전문가들은|تُظهر الدراسات|تظهر الدراسات|وفقًا للدراسات|يقول الخبراء|अध्ययनों से पता|विशेषज्ञों के अनुसार|शोध बताता/,
];

/**
 * Regla de procedencia del fundador (1 oct 2026, D5): un método se nombra y se explica, pero nunca se atribuye
 * ("según Deming", "como decía Drucker", "Jane Jacobs demostró"), y si tiene nombre neutro se usa ese ("ciclo PDCA",
 * no "ciclo de Deming"). Una persona de la lista solo puede aparecer dentro de un nombre de método sin alternativa
 * neutra corriente.
 */
export const PERSONAS_COMO_FUENTE = /\b(Deming|Shewhart|Juran|Crosby|Taguchi|Heinrich|Drucker|Christensen|Geoffrey Moore|Jacobs|Goodall|Eames|Porter|Feigenbaum|Osterwalder|Fulton Suri|Kotter|Covey|Maslow|Eisenhower)\b/;
// Decisión del fundador (1 oct 2026, punto 1): un nombre de método con apellido NO es atribución. En lo que ve el
// cliente se prefiere el nombre neutro cuando existe (ciclo PDCA, trilogía de la calidad, las cuatro etapas del proceso
// creativo); si no existe, el nombre se queda. Estos son los que no tienen nombre neutro corriente.
export const METODO_SIN_NEUTRO = /diagramas? de Eames|(?:los )?14 puntos de Deming/gi;

/** Los campos de un nodo que se ven (la pauta de personas solo se aplica ahí; el título es material interno). */
export const CAMPOS_VISIBLES_NODO = ["etiqueta_arbol", "resumen_teorico", "entregable_esperado", "pasos_accionables", "condiciones_activacion"] as const;

/**
 * Las formas de autoría con nombre propio (medida 4 de procedencia, acta 15.3, 6 oct 2026): "Popularizada por Janine
 * Benyus", "El filósofo Don Ihde llama", "Basado en el modelo de Stewart Brand", "(ver NIST SP 800-60)". El verbo o la
 * frase de autoría no distingue mayúsculas, el NOMBRE sí: tiene que empezar en mayúscula. Por eso van en texto con el
 * modificador local `(?i:…)` (Python re y regex lo entienden; en JS hace falta Node 23 o más), no como RegExp: este
 * módulo se importa sin compilarlas. Un nombre de método que se explica sin atribuirlo no es procedencia (D5): las
 * formas exigen un verbo o una frase de autoría delante del nombre.
 */
const NOMBRE = "[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+";
export interface FormaNombrePropio {
  id: string;
  patron: string;
  flags: string;
  /** Campos donde la forma no se aplica, con su porqué. */
  no_aplica_en?: readonly string[];
  porque?: string;
}
export const FORMAS_NOMBRE_PROPIO: readonly FormaNombrePropio[] = [
  { id: "autoria", flags: "", patron: String.raw`(?i:\b(popularizad|desarrollad|propuest|cread|acuñad|ideado|ideada|formulad|introducid|difundid|planteado|planteada)[oa]s?\s+por)\s+` + NOMBRE },
  { id: "basado_en", flags: "", patron: String.raw`(?i:\bbasad[oa]s?\s+en\s+(el|la|los|las)\s+(modelo|trabajo|concepto|teor[ií]a|idea|enfoque|propuesta|an[eé]cdota)s?\s+de)\s+` + NOMBRE },
  {
    id: "segun_nombre",
    flags: "",
    patron: String.raw`(?i:\bseg[uú]n)\s+` + NOMBRE + String.raw`\s+` + NOMBRE,
    no_aplica_en: ["etiqueta_arbol"],
    porque: "las etiquetas van en mayúscula de rótulo (C30): \"Calidad Según Quien Juzga\" no nombra a nadie",
  },
  { id: "oficio_nombre", flags: "", patron: String.raw`(?i:\b(el|la)\s+(fil[oó]sof[oa]|psic[oó]log[oa]|soci[oó]log[oa]|economista|autora?|investigador[a]?|profesor[a]?|dise[nñ]ador[a]?|consultor[a]?))\s+` + NOMBRE },
  { id: "dijo_nombre", flags: "", patron: String.raw`(?i:\bcomo\s+(dijo|dec[ií]a|escribi[oó]|afirm[oó]|explic[oó]|aconsejaba))\s+` + NOMBRE },
  { id: "referencia", flags: "", patron: String.raw`\(\s*(?i:ver|v[eé]ase|cf\.?)\s+[A-Z]` },
];

export interface PatronDatos {
  id?: string;
  patron: string;
  flags: string;
  no_aplica_en?: readonly string[];
  porque?: string;
}
export interface PautaProcedencia {
  id: string;
  origen: string;
  que: string;
  /** Dónde se aplica en el catálogo (la prueba que la hace cumplir). */
  se_cumple_en: string;
  /** Qué textos barre. */
  textos: string;
  /** Los campos de un nodo a los que se aplica (el título del concepto es material interno y no entra). */
  campos_de_nodo: readonly string[];
  patrones: readonly PatronDatos[];
  /** Se quitan del texto ANTES de buscar los patrones (nombres de método sin alternativa neutra). */
  exentos?: readonly PatronDatos[];
  /** Fixtures: lo que DEBE cazar y lo que NO (BANCO §9: todo patrón nace con dos fixtures). */
  caza: readonly string[];
  no_caza: readonly string[];
}

const datos = (rx: RegExp): PatronDatos => ({ patron: rx.source, flags: rx.flags });

export const PAUTAS_PROCEDENCIA: readonly PautaProcedencia[] = [
  {
    id: "prefijoProcedencia",
    origen: "D1 (fundador, 30 sep 2026): ninguna etiqueta de procedencia; D4 (1 oct 2026): ningún texto lleva \"Sugerencia de My Idea\"",
    que: "el prefijo o la etiqueta de procedencia (\"Sugerencia de My Idea\"), en los once idiomas",
    se_cumple_en: "web/lib/procedencia.test.ts (sección 5)",
    textos: "todo texto de cara al cliente: interfaz, etiquetas, preguntas, prompts y los campos de los nodos",
    campos_de_nodo: CAMPOS_VISIBLES_NODO,
    patrones: [datos(PREFIJO_PROCEDENCIA)],
    caza: ["Sugerencia de My Idea: guarda el comprobante", "Suggestion from My Idea: keep the receipt", "Vorschlag von My Idea: bewahre den Beleg auf"],
    no_caza: ["Guarda el comprobante de cada venta", "My Idea te ayuda a ordenar tu plan"],
  },
  {
    id: "atribucionGenerica",
    origen: "D1 (fundador, 30 sep 2026) y D5 (1 oct 2026): \"los estudios muestran\" y similares se reescriben diciendo el consejo directamente",
    que: "atribuir lo que se dice a estudios, investigaciones, expertos, la evidencia o la literatura, en los once idiomas; no muerde las instrucciones al usuario ni las negaciones",
    se_cumple_en: "web/lib/procedencia.test.ts (sección 6)",
    textos: "todo texto de cara al cliente: interfaz, etiquetas, preguntas, prompts y los campos de los nodos",
    campos_de_nodo: CAMPOS_VISIBLES_NODO,
    patrones: ATRIBUCION_GENERICA.map(datos),
    caza: ["Los estudios muestran que escribir ayuda.", "La investigación sugiere que funciona.", "según diversos estudios (Rasmussen)", "Studies show it works.", "Selon les experts, c'est utile."],
    no_caza: ["Investigar la literatura sobre antropología cultural del país", "Confirmar el objetivo según los datos obtenidos", "Una estrategia que no se ha probado con usuarios reales", "aunque todavía no está probado que lo logren"],
  },
  {
    id: "metodoConPersona",
    origen: "D5 (fundador, 1 oct 2026): un método se nombra y se explica, nunca se atribuye, y con su nombre neutro si lo tiene; un nombre de método con apellido sin alternativa neutra corriente se queda",
    que: "una persona de la lista como fuente, o un método con persona que tiene nombre neutro (\"ciclo de Deming\" en vez de \"ciclo PDCA\")",
    se_cumple_en: "web/lib/procedencia.test.ts (sección 7)",
    textos: `los campos visibles de un nodo: ${CAMPOS_VISIBLES_NODO.join(", ")}`,
    campos_de_nodo: CAMPOS_VISIBLES_NODO,
    patrones: [datos(PERSONAS_COMO_FUENTE)],
    exentos: [datos(METODO_SIN_NEUTRO)],
    caza: ["Como decía Drucker, no hay nada tan inútil", "El ciclo de Deming tiene cuatro pasos", "Deja el Triángulo de Heinrich"],
    no_caza: ["Usa el diagrama de Eames para ver la intersección", "Aplica el ciclo PDCA", "Ordena tus causas con un diagrama de Pareto", "Repasa los 14 puntos de Deming con tu equipo"],
  },
  {
    id: "nombrePropio",
    origen: "D1 y D5; medida 4 de procedencia (acta 15.3, 6 oct 2026): ninguna persona u organización con nombre como fuente",
    que: "las formas de autoría con nombre propio: autoría (\"popularizada por X\"), \"basado en el modelo de X\", \"según X Y\", \"el filósofo X\", \"como dijo X\" y las referencias \"(ver X)\"",
    se_cumple_en: "engine/test_procedencia_nombres.py",
    textos: "los campos de cara de los nodos vivos (etiqueta, resumen, entregable, pasos y condiciones) y la pregunta base",
    campos_de_nodo: [...CAMPOS_VISIBLES_NODO, "pregunta"],
    patrones: FORMAS_NOMBRE_PROPIO,
    caza: ["Popularizada por Janine Benyus, la biomímesis propone", "Basado en el modelo de Stewart Brand, todo sistema", "El filósofo Don Ihde llama 'falacia del diseñador'", "documentar la categorización (ver NIST SP 800-60).", "como dijo George Box: 'todos los modelos'"],
    no_caza: ["Aplica el ciclo PDCA a tu proceso", "Usa el diagrama de Ishikawa para ordenar causas", "Si vendes en Estados Unidos, revisa la norma"],
  },
];
