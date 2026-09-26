/**
 * Guardias de frases por idioma (i18n F6, D8). BANCO_DE_TEXTOS es el canon en
 * español; en los otros idiomas manda el catálogo, y las guardias de frases
 * prohibidas corren sobre cada uno. Aquí vive la lista, regla por regla, con
 * su origen en el BANCO y su equivalente en cada uno de los once idiomas:
 *   - las reglas de FORMA (la raya, los tres puntos, la jerga cruda) valen igual
 *     en todos;
 *   - las reglas de LENGUA (el reproche, el plural, los claims) llevan una
 *     traducción fiel del español del BANCO por idioma.
 * Un idioma sin equivalente (p. ej. el "ustedes" en inglés) lo declara con su
 * motivo en `sinEquivalente`: la prueba exige que toda regla decida los once.
 *
 * La corre frasesProhibidas.test.ts sobre todos los catálogos de `mensajes/`
 * en todos los idiomas y sobre las etiquetas del riel (D3). Si una traducción
 * rompe una guardia, se corrige ESA traducción, nunca el español.
 */
import type { Locale } from "./config";

export type ReglaVoz = {
  id: string;
  /** De dónde sale la regla (sección del BANCO o convención). */
  origen: string;
  /** Qué prohíbe, en una línea. */
  que: string;
  /** Los patrones que la rompen, en cada idioma (vacío: sin equivalente). */
  porIdioma: Record<Locale, readonly RegExp[]>;
  /** Por qué un idioma no tiene equivalente (obligatorio si su lista va vacía). */
  sinEquivalente: Readonly<Record<string, string>>;
};

/** Un patrón entre límites de palabra que entiende acentos y otras escrituras
 * latinas (el `\b` de JS solo ve ASCII). Sin distinguir mayúsculas. */
const palabra = (s: string) => new RegExp(`(?<!\\p{L})(?:${s})(?!\\p{L})`, "iu");

const LOS_ONCE = <T>(x: T): Record<Locale, T> => ({ es: x, en: x, pt: x, fr: x, de: x, it: x, ja: x, zh: x, ko: x, ar: x, hi: x });

/** La jerga cruda en su forma original (se cuela igual en cualquier idioma). */
const JERGA_LATINA = palabra("MVPs?|pivot(?:e|es|s|ar|ear|ing)?|earlyvangelists?|stakeholders?|build[- ]measure[- ]learn");
const TOKENS_LATINO = palabra("tokens?");
const AP = "['’]"; // apóstrofo recto o tipográfico

export const REGLAS_VOZ: readonly ReglaVoz[] = [
  {
    id: "raya",
    origen: "BANCO §3: cero guiones largos o medios",
    que: "— y – en el texto (coma, dos puntos o punto)",
    porIdioma: LOS_ONCE([/[—–]/u]),
    sinEquivalente: {},
  },
  {
    id: "puntosSuspensivos",
    origen: "F3_CONVENCIONES (la voz): puntos suspensivos con el carácter …",
    que: "tres puntos seguidos en vez de …",
    porIdioma: LOS_ONCE([/\.\.\./]),
    sinEquivalente: {},
  },
  {
    id: "signosInvertidos",
    origen: "F3_CONVENCIONES (la voz): nada de ¿ ni ¡ fuera del español",
    que: "¿ o ¡ en un idioma que no es el español",
    porIdioma: { ...LOS_ONCE([/[¿¡]/u]), es: [] },
    sinEquivalente: { es: "son la puntuación propia del español" },
  },
  {
    id: "jergaCruda",
    origen: "BANCO §3: cero jerga de manual (MVP, pivot, earlyvangelists, stakeholder, Build-Measure-Learn)",
    que: "la jerga de manual cruda, en su forma original o transliterada",
    porIdioma: {
      ...LOS_ONCE([JERGA_LATINA]),
      ja: [JERGA_LATINA, /ピボット|ステークホルダー|アーリーエバンジェリスト/u],
      ko: [JERGA_LATINA, /피벗|스테이크홀더|얼리\s?(?:밴|반)젤리스트/u],
      ar: [JERGA_LATINA, /بيفوت|ستيك\s?هولدر/u],
      hi: [JERGA_LATINA, /एमवीपी|पिवट|स्टेकहोल्डर/u],
    },
    sinEquivalente: {},
  },
  {
    id: "monedaTokens",
    origen: "BANCO §3: la moneda son créditos, jamás \"tokens\"",
    que: "llamar \"tokens\" a los créditos",
    porIdioma: {
      ...LOS_ONCE([TOKENS_LATINO]),
      fr: [TOKENS_LATINO, palabra("jetons?")],
      ja: [TOKENS_LATINO, /トークン/u],
      zh: [TOKENS_LATINO, /代币|令牌/u],
      ko: [TOKENS_LATINO, /토큰/u],
      ar: [TOKENS_LATINO, /توكن/u],
      hi: [TOKENS_LATINO, /टोकन/u],
    },
    sinEquivalente: {},
  },
  {
    id: "tuteoSingular",
    origen: "BANCO §3: tuteo singular, le habla a UNA persona (y el registro de DISENO §6 / D7)",
    que: "tratar al usuario en plural (el \"ustedes\") o, en francés, italiano y alemán, salir del tuteo",
    porIdioma: {
      es: [palabra("ustedes|vosotr[oa]s")],
      en: [],
      pt: [palabra("vocês|vós")],
      fr: [palabra("vous|votre|vos")],
      de: [palabra("euch|euer|eure[mnrs]?")],
      it: [palabra("voi|vostr[oaie]")],
      ja: [/皆さん|皆様|あなたたち|あなた方/u],
      zh: [/你们/u],
      ko: [/여러분/u],
      ar: [],
      hi: [/आप लोग|आप सब/u],
    },
    sinEquivalente: {
      en: "\"you\" no distingue singular de plural: no hay forma que prohibir",
      ar: "D7: el plural de cortesía (أنتم، ـكم) ES la forma neutra canónica en árabe, no un \"ustedes\"",
    },
  },
  {
    id: "reproche",
    origen: "BANCO §3 (espejo, jamás regaño) y §5 (notificaciones): prohibido \"vas tarde\", \"te atrasaste\", \"no cumpliste\", \"deberías haber\", \"estás atrasado\"",
    que: "reprocharle al usuario su ritmo o sus fechas",
    porIdioma: {
      es: [palabra("vas tarde|te atrasaste|no cumpliste|deber[ií]as haber|est[aá]s atrasad[oa]|vas atrasad[oa]")],
      en: [palabra(`you${AP}re (?:late|behind)|you are (?:late|behind)|you fell behind|you(?:${AP}ve| have) fallen behind|you didn${AP}t (?:meet|keep|finish)|you failed to|you should have`)],
      pt: [palabra("você está atrasad[oa]|você se atrasou|você não cumpriu|você deveria ter")],
      fr: [palabra(`tu es en retard|tu as pris du retard|tu n${AP}as pas (?:respecté|tenu)|tu aurais dû`)],
      de: [palabra("du bist (?:spät dran|zu spät|im verzug|im rückstand|hinterher)|du hast dich verspätet|du hättest")],
      it: [palabra("sei in ritardo|sei indietro|ti sei attardat[oa]|non hai rispettato|avresti dovuto")],
      ja: [/遅れています|遅れました|遅れてしまいました|守れませんでした|(?:す|する)べきでした/u],
      zh: [/你落后了|你迟到了|你拖延了|你没有完成|你本应|你本该|你早该/u],
      ko: [/늦었어요|뒤처졌어요|지키지 못했어요|했어야 (?:했어요|해요)/u],
      ar: [/أنتم متأخرون|تأخرتم|لم تلتزموا|كان عليكم أن|كان ينبغي عليكم/u],
      hi: [/आप पीछे (?:चल रहे )?हैं|आप पिछड़ गए|आपने पूरा नहीं किया|आपको .{0,30}चाहिए था/u],
    },
    sinEquivalente: {},
  },
  {
    id: "aMedias",
    origen: "BANCO §3: vocabulario de los estados de tarea, \"en proceso\" (nunca \"a medias\")",
    que: "llamar \"a medias\" a una tarea en proceso",
    porIdioma: {
      es: [palabra("a medias")],
      en: [palabra("half[- ](?:done|finished|baked)")],
      pt: [palabra("(?:ficou|feit[oa]|deixad[oa]) pela metade|meio feit[oa]")], // "divida seu tempo pela metade" es aritmética
      fr: [palabra("à moitié (?:fait|faite|finie?|terminée?)")],
      de: [palabra("halb fertig|halbfertig|halb erledigt")],
      it: [palabra("fatt[oa] a metà|lasciat[oa] a metà")],
      ja: [/中途半端/u],
      zh: [/做了一半|半途而废|半拉子/u],
      ko: [/어중간|하다 만/u],
      ar: [/نصف منجز/u],
      hi: [/आधा[- ]अधूरा/u],
    },
    sinEquivalente: {},
  },
  {
    id: "claimsNoUsar",
    origen: "BANCO §6: \"Cero alucinación\" NO USAR ASÍ (decirlo entero o no decirlo)",
    que: "el claim recortado de \"cero alucinación\"",
    porIdioma: {
      es: [palabra("cero alucinaci(?:ón|ones)")],
      en: [palabra("zero hallucinations?|no hallucinations")],
      pt: [palabra("zero alucinaç(?:ão|ões)")],
      fr: [palabra("zéro hallucinations?|aucune hallucination")],
      de: [palabra("null halluzination(?:en)?|keine halluzinationen")],
      it: [palabra("zero allucinazion[ei]|nessuna allucinazione")],
      ja: [/ハルシネーションゼロ|幻覚ゼロ/u],
      zh: [/零幻觉/u],
      ko: [/환각 제로/u],
      ar: [/صفر هلوسة/u],
      hi: [/शून्य मतिभ्रम/u],
    },
    sinEquivalente: {},
  },
  {
    id: "reemplazaConsultor",
    origen: "BANCO §6: \"Reemplaza a un consultor\" NO USAR (ver §4: no sustituye a un consultor humano)",
    que: "afirmar que My Idea reemplaza a un consultor (la frontera dicha en negativo sí vale)",
    porIdioma: {
      es: [/(?<!no )(?:reemplaza|sustituye) a (?:un|tu) consultor/iu],
      en: [new RegExp(`(?<!(?:not|n${AP}t|never) )replaces? (?:a|your) consultant|(?<!(?:not|n${AP}t) )(?:a )?replacement for (?:a|your) consultant`, "iu")],
      pt: [/(?<!não )substitui (?:um|seu|o seu) consultor/iu],
      fr: [/(?<!ne )remplace (?:un|ton) consultant/iu],
      de: [/ersetzt (?:einen|deinen) Berater|ersetzt (?:eine|deine) Beraterin/iu],
      it: [/(?<!non )sostituisce (?:un|il tuo) consulente/iu],
      ja: [/コンサルタントの代わりになります|コンサルタントに取って代わ|コンサルタントは不要/u],
      zh: [/(?<!不|不能|无法|不会|并不)(?:取代|替代)(?:你的)?顾问/u],
      ko: [/컨설턴트를 대체(?:해요|합니다|한다|할 수 있)/u],
      ar: [/(?<!لا )(?:يحل|تحل) محل (?:ال)?مستشار/u],
      hi: [/सलाहकार की जगह ले(?:ता|ती|ते) है/u],
    },
    sinEquivalente: {},
  },
  {
    id: "lenguajeMuerto",
    origen: "app/potenciadores/page.test.ts y BANCO §5: el precio va al frente; murieron \"Explóralo gratis\" y \"Se paga por uso\"",
    que: "las invitaciones muertas a explorar gratis o pagar por uso",
    porIdioma: {
      es: [palabra("expl[oó]ral[oa] gratis|se paga por uso")],
      en: [palabra("explore it (?:for )?free|pay per use|pay as you go")],
      pt: [palabra("explore(?:-o)? (?:de graça|grátis|gratuitamente)|pague pelo uso|paga-se pelo uso")],
      fr: [palabra(`explore-le (?:gratuitement|gratis)|paiement à l${AP}utilisation`)],
      // el infinitivo tras "kannst du … erneut" es la frase viva ("podrás explorarlo
      // de nuevo gratis"); la muerta es la invitación suelta, al inicio.
      de: [/(?:^|[.:!?]\s+)kostenlos erkunden|erkunde (?:sie|es|ihn) kostenlos|bezahlung nach nutzung/iu],
      it: [palabra("esploral[oa] (?:gratis|gratuitamente)|si paga a consumo|paghi a consumo")],
      ja: [/無料で探求してみ|無料で探ってみ|従量課金/u],
      zh: [/免费探索一下|免费探索吧|按使用付费|按量付费/u],
      ko: [/무료로 탐색해 보세요|무료로 둘러보세요|사용한 만큼 (?:결제|지불)/u],
      ar: [/استكشفوه مجان|استكشفوها مجان|الدفع حسب الاستخدام|ادفعوا حسب الاستخدام/u],
      hi: [/मुफ़?्त में (?:खोजें|देखें)|जितना इस्तेमाल,? उतना भुगतान/u],
    },
    sinEquivalente: {},
  },
];

export type FaltaVoz = { regla: string; texto: string };

/** Las faltas de voz de un texto en su idioma. Los {{marcadores}} y las
 * <etiquetas> propias no son texto: se quitan antes de mirar. */
export function faltasDeVoz(texto: string, idioma: Locale): FaltaVoz[] {
  const t = texto.replace(/\{\{\w+\}\}/g, " ").replace(/<\/?[a-zA-Z]\w*\s*\/?>/g, " ");
  const faltas: FaltaVoz[] = [];
  for (const regla of REGLAS_VOZ)
    for (const patron of regla.porIdioma[idioma] ?? []) {
      const m = t.match(patron);
      if (m) faltas.push({ regla: regla.id, texto: m[0] });
    }
  return faltas;
}
