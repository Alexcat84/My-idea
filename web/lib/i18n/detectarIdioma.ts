/**
 * El idioma de la IDEA (i18n F5, DISENO §3.3 y §5). Es distinto del de la
 * interfaz: se detecta del texto original, se guarda en `projects.idioma`
 * (migración 046) y manda en todo lo que escribe la IA y en los documentos de
 * ese proyecto (D2).
 *
 * Cómo, como en el I Ching: primero el ALFABETO (el que tiene más letras gana);
 * si es el latino, las PALABRAS VACÍAS de cada idioma (más una señal por las
 * letras que solo usa uno); en empate o sin señal, el idioma de la interfaz.
 *
 * Añadido del fundador (25 sep 2026): también se reconocen idiomas FUERA de
 * los once. La IA responde en ellos (sabe hacerlo); la interfaz y lo que
 * escribe el código sin IA caen al idioma de la interfaz (`idiomaDePlantilla`).
 * El código que se guarda es el ISO 639-1.
 */
import { esActivo, type ActiveLocale } from "./config";

export interface IdiomaDetectado {
  /** ISO 639-1 del idioma de la idea (puede estar fuera de los once). */
  codigo: string;
  /** true = no hubo señal suficiente y se tomó el de la interfaz. */
  porDefecto: boolean;
}

/** Alfabetos que deciden solos (sin palabras vacías). */
const ALFABETO_PROPIO: [RegExp, string][] = [
  [/\p{Script=Devanagari}/u, "hi"],
  [/\p{Script=Greek}/u, "el"],
  [/\p{Script=Hebrew}/u, "he"],
  [/\p{Script=Thai}/u, "th"],
  [/\p{Script=Bengali}/u, "bn"],
  [/\p{Script=Tamil}/u, "ta"],
  [/\p{Script=Telugu}/u, "te"],
  [/\p{Script=Gujarati}/u, "gu"],
  [/\p{Script=Gurmukhi}/u, "pa"],
  [/\p{Script=Kannada}/u, "kn"],
  [/\p{Script=Malayalam}/u, "ml"],
  [/\p{Script=Georgian}/u, "ka"],
  [/\p{Script=Armenian}/u, "hy"],
  [/\p{Script=Ethiopic}/u, "am"],
  [/\p{Script=Khmer}/u, "km"],
  [/\p{Script=Lao}/u, "lo"],
  [/\p{Script=Myanmar}/u, "my"],
  [/\p{Script=Sinhala}/u, "si"],
];

const LATINA = /\p{Script=Latin}/u;
const ARABE = /\p{Script=Arabic}/u;
const CIRILICA = /\p{Script=Cyrillic}/u;
const HANGUL = /\p{Script=Hangul}/u;
const KANA = /[\p{Script=Hiragana}\p{Script=Katakana}]/u;
const HAN = /\p{Script=Han}/u;

/** Letras del urdu y del persa dentro del alfabeto árabe (el urdu primero:
 * también usa las del persa). */
const LETRAS_URDU = /[ٹڈڑںے]/u;
const LETRAS_PERSA = /[پچژگ]/u;
/** Letras del ucraniano que el ruso no tiene. */
const LETRAS_UCRANIANO = /[іїєґІЇЄҐ]/u;

/** Las palabras vacías de los idiomas de alfabeto latino que se reconocen. Las
 * listas evitan a propósito las palabras que chocan entre idiomas sin decir
 * nada (el "de" del neerlandés, el "i" del polaco). */
const VACIAS: Record<string, readonly string[]> = {
  es: ["de", "la", "que", "el", "en", "y", "los", "las", "del", "se", "por", "un", "una", "con", "para", "es", "mi", "mis", "quiero", "al", "lo", "como", "más", "pero", "su", "sus", "yo", "tengo", "este", "esta", "porque", "muy", "sin", "también", "me", "hay", "no", "nuestro", "nuestra", "donde", "cuando"],
  pt: ["de", "da", "do", "das", "dos", "que", "em", "um", "uma", "para", "com", "os", "as", "não", "é", "e", "na", "no", "por", "mais", "se", "eu", "quero", "meu", "minha", "nosso", "nossa", "também", "mas", "como", "isso", "esse", "essa", "você", "ao"],
  fr: ["je", "veux", "du", "dans", "mon", "ma", "mes", "le", "la", "les", "de", "des", "et", "un", "une", "en", "que", "qui", "pour", "avec", "sur", "est", "pas", "ce", "cette", "au", "aux", "mais", "nous", "vous", "aussi", "notre", "très", "sont"],
  en: ["i", "the", "to", "and", "a", "of", "in", "my", "want", "is", "it", "for", "that", "with", "on", "this", "we", "be", "have", "our", "would", "like", "an", "are", "but", "not"],
  de: ["ich", "möchte", "in", "meinem", "meine", "mein", "meiner", "der", "die", "das", "und", "ist", "zu", "den", "dem", "mit", "von", "für", "auf", "nicht", "ein", "eine", "einen", "im", "es", "wir", "will", "auch", "sich", "unsere", "unser"],
  it: ["voglio", "nel", "nella", "mio", "mia", "miei", "il", "di", "che", "e", "la", "per", "un", "una", "con", "non", "sono", "del", "della", "gli", "anche", "questo", "questa", "vorrei", "come", "ma", "si", "lo"],
  nl: ["ik", "wil", "in", "mijn", "het", "een", "van", "dat", "voor", "met", "niet", "op", "te", "zijn", "wij", "we", "ook", "onze", "ons", "graag"],
  pl: ["chcę", "w", "z", "na", "się", "nie", "jest", "że", "moja", "mojej", "mój", "moim", "jak", "dla", "od", "ale", "oraz", "chciałbym", "chciałabym", "także"],
  tr: ["ve", "bu", "bir", "için", "istiyorum", "ile", "çok", "gibi", "ama", "daha", "olarak", "benim", "bana", "şey"],
  vi: ["tôi", "muốn", "ở", "của", "và", "là", "có", "không", "một", "các", "những", "cho", "với", "được", "này", "trong", "người", "để"],
  id: ["saya", "ingin", "dan", "yang", "untuk", "dengan", "ini", "itu", "ke", "dari", "tidak", "akan", "kami", "kita", "aku", "mau", "bisa", "ada", "di"],
  ro: ["vreau", "să", "și", "în", "pe", "cu", "care", "pentru", "mea", "meu", "nu", "este", "eu", "sunt", "acest", "această", "aș"],
  sv: ["jag", "vill", "och", "att", "det", "är", "som", "på", "med", "för", "min", "mitt", "mina", "inte", "av", "har", "också"],
};

const CONJUNTOS: Record<string, Set<string>> = Object.fromEntries(
  Object.entries(VACIAS).map(([codigo, palabras]) => [codigo, new Set(palabras.map((p) => p.normalize("NFC")))])
);

/** Letras que solo usa un idioma: suman un punto (una vez por texto). Sobre la
 * forma NFD, para ver el cuerno del vietnamita dentro de "ở". */
const SENAL_DE_LETRA: [RegExp, string][] = [
  [/[ñ¿¡]/u, "es"],
  [/[ãõ]/u, "pt"],
  [/ß/u, "de"],
  [/œ/u, "fr"],
  [/[łąęśźżń]/u, "pl"],
  [/[ğşı]/u, "tr"],
  [/[̛đ]/u, "vi"],
  [/[ășț]/u, "ro"],
];

function contar(texto: string, re: RegExp): number {
  let n = 0;
  for (const c of texto) if (re.test(c)) n++;
  return n;
}

function porLaInterfaz(interfaz: ActiveLocale): IdiomaDetectado {
  return { codigo: interfaz, porDefecto: true };
}

function latino(texto: string, interfaz: ActiveLocale): IdiomaDetectado {
  const minusculas = texto.normalize("NFC").toLocaleLowerCase();
  const palabras = minusculas.match(/[\p{L}\p{M}]+/gu) ?? [];
  const puntos: Record<string, number> = {};
  for (const [codigo, conjunto] of Object.entries(CONJUNTOS)) {
    let n = 0;
    for (const p of palabras) if (conjunto.has(p)) n++;
    if (n > 0) puntos[codigo] = n;
  }
  const descompuesto = minusculas.normalize("NFD");
  for (const [re, codigo] of SENAL_DE_LETRA) {
    if (re.test(minusculas) || re.test(descompuesto)) puntos[codigo] = (puntos[codigo] ?? 0) + 1;
  }
  const maximo = Math.max(0, ...Object.values(puntos));
  if (maximo === 0) return porLaInterfaz(interfaz);
  const empatados = Object.keys(puntos).filter((c) => puntos[c] === maximo);
  if (empatados.length === 1) return { codigo: empatados[0], porDefecto: false };
  // En empate no se adivina: gana la interfaz si está entre los empatados.
  if (empatados.includes(interfaz)) return { codigo: interfaz, porDefecto: false };
  return porLaInterfaz(interfaz);
}

export function detectarIdioma(texto: string, interfaz: ActiveLocale): IdiomaDetectado {
  const t = (texto ?? "").normalize("NFC");
  const cuentas: [string, number][] = [
    ["latino", contar(t, LATINA)],
    ["arabe", contar(t, ARABE)],
    ["cirilico", contar(t, CIRILICA)],
    ["cjk", contar(t, HANGUL) + contar(t, KANA) + contar(t, HAN)],
    ...ALFABETO_PROPIO.map(([re, codigo]): [string, number] => [codigo, contar(t, re)]),
  ];
  const [ganador, letras] = cuentas.reduce((a, b) => (b[1] > a[1] ? b : a));
  if (letras === 0) return porLaInterfaz(interfaz);

  switch (ganador) {
    case "latino":
      return latino(t, interfaz);
    case "arabe":
      return { codigo: LETRAS_URDU.test(t) ? "ur" : LETRAS_PERSA.test(t) ? "fa" : "ar", porDefecto: false };
    case "cirilico":
      return { codigo: LETRAS_UCRANIANO.test(t) ? "uk" : "ru", porDefecto: false };
    case "cjk": {
      const hangul = contar(t, HANGUL);
      const kana = contar(t, KANA);
      const codigo = hangul > 0 && hangul >= kana ? "ko" : kana > 0 ? "ja" : "zh";
      return { codigo, porDefecto: false };
    }
    default:
      return { codigo: ganador, porDefecto: false };
  }
}

/** El idioma en que escribe el código SIN IA (plantillas, marcadores, avisos)
 * para un proyecto: el suyo si es de los once; si no, el de la interfaz. */
export function idiomaDePlantilla(codigo: string | null | undefined, interfaz: ActiveLocale): ActiveLocale {
  return esActivo(codigo) ? codigo : interfaz;
}

const CODIGO_VALIDO = /^[a-z]{2,3}$/;

/** El idioma guardado de un proyecto. Uno de antes de F5 (sin la columna, o
 * NULL) es español: la app solo hablaba español. */
export function idiomaDelProyecto(proyecto: { idioma?: string | null }): string {
  const x = proyecto.idioma;
  return typeof x === "string" && CODIGO_VALIDO.test(x) ? x : "es";
}

/** Cada idioma reconocido, nombrado en español (el prompt está en español) y
 * en su propia escritura, para la regla de IDIOMA DE SALIDA. */
const NOMBRE_PARA_IA: Record<string, string> = {
  es: "español",
  en: "inglés (English)",
  pt: "portugués de Brasil (português)",
  fr: "francés neutro, válido para Quebec (français)",
  de: "alemán (Deutsch)",
  it: "italiano (italiano)",
  ja: "japonés (日本語)",
  zh: "chino simplificado (简体中文)",
  ko: "coreano (한국어)",
  ar: "árabe estándar moderno (العربية)",
  hi: "hindi (हिन्दी)",
  ru: "ruso (русский)",
  uk: "ucraniano (українська)",
  el: "griego (ελληνικά)",
  he: "hebreo (עברית)",
  th: "tailandés (ไทย)",
  fa: "persa (فارسی)",
  ur: "urdu (اردو)",
  bn: "bengalí (বাংলা)",
  ta: "tamil (தமிழ்)",
  te: "telugu (తెలుగు)",
  gu: "guyaratí (ગુજરાતી)",
  pa: "panyabí (ਪੰਜਾਬੀ)",
  kn: "canarés (ಕನ್ನಡ)",
  ml: "malayalam (മലയാളം)",
  ka: "georgiano (ქართული)",
  hy: "armenio (հայերեն)",
  am: "amárico (አማርኛ)",
  km: "jemer (ខ្មែរ)",
  lo: "lao (ລາວ)",
  my: "birmano (မြန်မာ)",
  si: "cingalés (සිංහල)",
  nl: "neerlandés (Nederlands)",
  pl: "polaco (polski)",
  tr: "turco (Türkçe)",
  vi: "vietnamita (Tiếng Việt)",
  id: "indonesio (Bahasa Indonesia)",
  ro: "rumano (română)",
  sv: "sueco (svenska)",
};

export function nombreIdiomaParaIA(codigo: string): string {
  return NOMBRE_PARA_IA[codigo] ?? `el idioma de código ISO «${codigo}»`;
}
