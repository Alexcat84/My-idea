/**
 * Los temas citados como fuente (decision del fundador, 9 oct 2026, REDACTOR_CON_RESPALDO.md punto 1). La ultima
 * medicion sostuvo dos procedencias: «El material enseña que la seguridad funciona cuando la gente participa»
 * (M3A-f015-1) y «El material de este plan no cubre seguridad informática en detalle» (M3A-f003-3). La persona no sabe
 * que la IA recibe temas; lo que el plan dice lo dice la casa. El codigo, sin modelo:
 *  - «Según el material, X» y «El material enseña que X» quedan como «X» (en aleman no: la subordinada no es frase);
 *  - cualquier otra frase con un sujeto de fuente y un verbo de fuente se quita entera.
 * El material fisico no se toca: hace falta un verbo de fuente ("enseña", "recomienda", "no cubre"...), no basta la
 * palabra ("si el material se agrieta", "tu material sale caro"). En los once idiomas; se aplica la lista del espanol
 * y la del idioma del plan.
 */
import type { Locale } from "../i18n/config";

type Latina = {
  tipo: "latina";
  sujetos: string[];
  verbos: string[];
  /** "Según el material, X" */
  prefijos: string[];
  /** "El material enseña que X": el nexo; null si la subordinada no puede quedar como frase (aleman). */
  nexo: string | null;
};
type Otra = { tipo: "otra"; sujetos: string[]; marcadores: string[]; fin: RegExp; unir: string };

const LISTAS: Record<Locale, Latina | Otra> = {
  es: {
    tipo: "latina",
    sujetos: [
      "el material", "este material", "ese material", "nuestro material", "mi material", "el contenido de este plan",
      "los temas de este plan", "los temas", "estos temas", "el método base", "el temario", "la base de este plan",
    ],
    verbos: [
      "enseña", "enseñan", "dice", "dicen", "indica", "indican", "explica", "explican", "recomienda", "recomiendan",
      "sugiere", "sugieren", "propone", "proponen", "plantea", "plantean", "señala", "señalan", "advierte", "advierten",
      "no cubre", "no cubren", "solo cubre", "solo cubren", "no trae", "no traen", "no incluye", "no incluyen",
      "no aborda", "no abordan",
    ],
    prefijos: ["según", "de acuerdo con", "como enseña", "como enseñan", "como dice", "como dicen", "como indica", "como explica"],
    nexo: "que",
  },
  en: {
    tipo: "latina",
    sujetos: ["the material", "this material", "the content of this plan", "this plan's content", "the topics", "these topics", "the base method"],
    verbos: [
      "teaches", "teach", "says", "say", "recommends", "recommend", "suggests", "suggest", "indicates", "explains",
      "proposes", "does not cover", "doesn't cover", "do not cover", "don't cover", "only covers",
    ],
    prefijos: ["according to", "as"],
    nexo: "that",
  },
  pt: {
    tipo: "latina",
    sujetos: ["o material", "este material", "o conteúdo deste plano", "os temas deste plano", "os temas"],
    verbos: ["ensina", "ensinam", "diz", "dizem", "recomenda", "recomendam", "sugere", "sugerem", "indica", "explica", "não cobre", "não cobrem"],
    prefijos: ["segundo", "de acordo com", "conforme"],
    nexo: "que",
  },
  fr: {
    tipo: "latina",
    sujetos: ["le matériel", "ce matériel", "le contenu de ce plan", "le support", "les thèmes de ce plan", "les thèmes"],
    verbos: ["enseigne", "enseignent", "dit", "disent", "recommande", "recommandent", "suggère", "indique", "explique", "ne couvre pas", "ne couvrent pas"],
    prefijos: ["selon", "d'après"],
    nexo: "que",
  },
  de: {
    tipo: "latina",
    sujetos: ["das material", "dieses material", "der inhalt dieses plans", "die themen dieses plans", "die themen"],
    verbos: ["lehrt", "lehren", "sagt", "sagen", "empfiehlt", "empfehlen", "erklärt", "erklären", "deckt nicht", "behandelt nicht"],
    prefijos: ["laut", "gemäß"],
    nexo: null,
  },
  it: {
    tipo: "latina",
    sujetos: ["il materiale", "questo materiale", "il contenuto di questo piano", "i temi di questo piano", "i temi"],
    verbos: ["insegna", "insegnano", "dice", "dicono", "consiglia", "consigliano", "suggerisce", "indica", "spiega", "non copre", "non coprono"],
    prefijos: ["secondo", "in base a"],
    nexo: "che",
  },
  ja: { tipo: "otra", sujetos: ["資料", "教材", "この計画の内容"], marcadores: ["によると", "によれば", "が教える", "は教えて", "は示して", "扱っていません", "カバーしていません", "扱いません"], fin: /[^。！？]*[。！？]?/g, unir: "" },
  zh: { tipo: "otra", sujetos: ["资料", "教材", "本计划的内容"], marcadores: ["根据", "据", "指出", "告诉", "显示", "没有涵盖", "不涵盖", "建议"], fin: /[^。！？]*[。！？]?/g, unir: "" },
  ko: { tipo: "otra", sujetos: ["자료", "교재", "이 계획의 내용"], marcadores: ["따르면", "가르칩니다", "알려줍니다", "다루지 않습니다", "권장합니다"], fin: /[^.!?]*[.!?]?\s*/g, unir: "" },
  ar: { tipo: "otra", sujetos: ["لمادة", "لمحتوى", "هذه المواد"], marcadores: ["وفقًا", "وفقا", "حسب", "تعلّم", "تعلم", "تقول", "توصي", "لا تغطي"], fin: /[^.!?؟]*[.!?؟]?\s*/g, unir: "" },
  hi: { tipo: "otra", sujetos: ["सामग्री"], marcadores: ["के अनुसार", "बताती", "सिखाती", "कहती", "शामिल नहीं"], fin: /[^।!?]*[।!?]?\s*/g, unir: "" },
};

const escapar = (x: string) => x.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
const alternativa = (xs: string[]) => xs.map(escapar).sort((a, b) => b.length - a.length).join("|");
const mayuscula = (s: string) => s.replace(/^\s*(\p{L})/u, (_m, l: string) => l.toUpperCase());

/** Una frase latina: null si se quita, la frase (quiza reescrita) si se queda. */
function frasesLatinas(l: Latina): (frase: string) => string | null {
  const S = alternativa(l.sujetos);
  const V = alternativa(l.verbos);
  const P = alternativa(l.prefijos);
  const borde = "(?<![\\p{L}\\p{N}])";
  const fin = "(?![\\p{L}\\p{N}])";
  const conPrefijo = new RegExp(`^\\s*(?:${P})\\s+(?:${S})(?:\\s+(?:${V}))?\\s*,\\s*(.+)$`, "iu");
  const conNexo = l.nexo ? new RegExp(`^\\s*(?:${S})\\s+(?:${V})\\s*,?\\s+${escapar(l.nexo)}\\s+(.+)$`, "iu") : null;
  const fuente = new RegExp(`${borde}(?:${S})(?:\\s+\\p{L}+){0,4}\\s+(?:${V})${fin}`, "iu");
  return (frase) => {
    const m1 = conPrefijo.exec(frase);
    if (m1) return mayuscula(m1[1]);
    const m2 = conNexo?.exec(frase);
    if (m2) return mayuscula(m2[1]);
    return fuente.test(frase) ? null : frase;
  };
}

/** Quita o reescribe las frases que citan los temas como fuente. Devuelve el texto y cuántas frases cambió. */
export function quitarCitasDeFuente(texto: string, idiomas: Locale[]): { texto: string; cambios: number } {
  let cambios = 0;
  let actual = texto;
  for (const idioma of [...new Set(idiomas)]) {
    const l = LISTAS[idioma];
    if (!l) continue;
    actual = actual
      .split("\n")
      .map((linea) => {
        if (l.tipo === "latina") {
          const juzgar = frasesLatinas(l);
          const prefijo = linea.match(/^\s*(?:#+\s*|\d+\.\s+|[-*]\s+)?/)?.[0] ?? "";
          const cuerpo = linea.slice(prefijo.length);
          const frases = cuerpo.match(/[^.!?]+[.!?]+["»”)]*\s*|[^.!?]+$/g);
          if (!frases) return linea;
          const salida: string[] = [];
          for (const f of frases) {
            const r = juzgar(f.trim());
            if (r === null) cambios++;
            else {
              if (r !== f.trim()) cambios++;
              salida.push(r);
            }
          }
          return prefijo + salida.join(" ");
        }
        const frases = linea.match(l.fin)?.filter((f) => f.length > 0) ?? [];
        if (frases.length === 0) return linea;
        const quedan = frases.filter((f) => {
          const cita = l.sujetos.some((s) => f.includes(s)) && l.marcadores.some((m) => f.includes(m));
          if (cita) cambios++;
          return !cita;
        });
        return quedan.map((f) => f.trim()).join(l.unir === "" && idioma === "ko" ? " " : l.unir).trim();
      })
      .join("\n");
  }
  return { texto: actual, cambios };
}
