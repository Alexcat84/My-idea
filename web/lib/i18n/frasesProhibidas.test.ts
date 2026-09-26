// i18n F6, D8: BANCO_DE_TEXTOS es el canon en español; en los otros idiomas, el
// catálogo; y las guardias de frases prohibidas corren sobre CADA idioma. Las
// reglas y sus equivalentes por idioma viven en frasesProhibidas.ts (cada una
// cita su sección del BANCO). Aquí: (1) toda regla decide los once idiomas, y
// un idioma sin equivalente lo justifica; (2) la guardia caza cada equivalente
// y deja pasar lo que el canon permite (casos escritos a mano); (3) ningún texto
// de ningún catálogo, en ningún idioma, ni ninguna etiqueta del riel, la rompe.
import { readdirSync, statSync } from "node:fs";
import path from "node:path";
import { pathToFileURL } from "node:url";
import { describe, expect, it } from "vitest";
import { pareceCatalogo } from "./auditor";
import { LOCALES, type Locale } from "./config";
import { faltasDeVoz, REGLAS_VOZ } from "./frasesProhibidas";
import { ETIQUETAS_RIEL } from "./etiquetasRiel";

const DIR = path.join(__dirname, "mensajes");

function archivos(dir: string): string[] {
  return readdirSync(dir).flatMap((n) => {
    const p = path.join(dir, n);
    return statSync(p).isDirectory() ? archivos(p) : p.endsWith(".ts") && !p.endsWith(".test.ts") ? [p] : [];
  });
}

/** Los ids de las reglas que rompe un texto (sin repetir). */
const rotas = (texto: string, idioma: Locale) => [...new Set(faltasDeVoz(texto, idioma).map((f) => f.regla))];

// Un ejemplo que DEBE caer, por regla y por idioma (null: el idioma no tiene
// equivalente y la regla lo justifica).
const CAEN: Record<string, Record<Locale, string | null>> = {
  tuteoSingular: {
    es: "Ustedes pueden empezar hoy",
    en: null,
    pt: "Vocês podem começar hoje",
    fr: "Vous pouvez commencer aujourd'hui",
    de: "Ihr Plan ist fertig, ich zeige ihn euch",
    it: "Voi potete iniziare oggi",
    ja: "皆さんのプランです",
    zh: "你们的计划好了",
    ko: "여러분의 계획이에요",
    ar: null,
    hi: "आप लोग आज शुरू कर सकते हैं",
  },
  reproche: {
    es: "Vas tarde con la etapa 2",
    en: "You're behind on stage 2",
    pt: "Você está atrasado na etapa 2",
    fr: "Tu es en retard sur l'étape 2",
    de: "Du bist im Rückstand",
    it: "Sei in ritardo con la tappa 2",
    ja: "ステージ2が遅れています",
    zh: "你落后了",
    ko: "2단계가 늦었어요",
    ar: "أنتم متأخرون في المرحلة 2",
    hi: "आप पीछे चल रहे हैं",
  },
  aMedias: {
    es: "la tarea quedó a medias",
    en: "the task is half-done",
    pt: "a tarefa ficou pela metade",
    fr: "la tâche est à moitié faite",
    de: "die Aufgabe ist halb fertig",
    it: "l'attività è fatta a metà",
    ja: "タスクが中途半端です",
    zh: "任务做了一半",
    ko: "할 일이 어중간해요",
    ar: "المهمة نصف منجزة",
    hi: "काम आधा-अधूरा है",
  },
  monedaTokens: {
    es: "Te quedan 3 tokens",
    en: "You have 3 tokens left",
    pt: "Restam 3 tokens",
    fr: "Il te reste 3 jetons",
    de: "Du hast noch 3 Token",
    it: "Ti restano 3 token",
    ja: "残り3トークン",
    zh: "剩余3个代币",
    ko: "토큰 3개 남았어요",
    ar: "تبقّى لكم 3 توكن",
    hi: "3 टोकन बचे हैं",
  },
  claimsNoUsar: {
    es: "Cero alucinación, garantizado",
    en: "Zero hallucination, guaranteed",
    pt: "Zero alucinação, garantido",
    fr: "Zéro hallucination, garanti",
    de: "Null Halluzination, garantiert",
    it: "Zero allucinazioni, garantito",
    ja: "ハルシネーションゼロを保証",
    zh: "零幻觉，有保障",
    ko: "환각 제로를 보장해요",
    ar: "صفر هلوسة، مضمون",
    hi: "शून्य मतिभ्रम, पक्का",
  },
  reemplazaConsultor: {
    es: "My Idea reemplaza a un consultor",
    en: "My Idea replaces a consultant",
    pt: "O My Idea substitui um consultor",
    fr: "My Idea remplace un consultant",
    de: "My Idea ersetzt einen Berater",
    it: "My Idea sostituisce un consulente",
    ja: "My Ideaはコンサルタントの代わりになります",
    zh: "My Idea可以取代顾问",
    ko: "My Idea는 컨설턴트를 대체해요",
    ar: "My Idea يحل محل المستشار",
    hi: "My Idea सलाहकार की जगह लेता है",
  },
  lenguajeMuerto: {
    es: "Explóralo gratis",
    en: "Explore it for free",
    pt: "Explore de graça",
    fr: "Explore-le gratuitement",
    de: "Kostenlos erkunden",
    it: "Esploralo gratis",
    ja: "無料で探求してみましょう",
    zh: "免费探索一下",
    ko: "무료로 탐색해 보세요",
    ar: "استكشفوه مجانًا",
    hi: "मुफ़्त में खोजें",
  },
};

// Lo que el canon PERMITE y que una guardia torpe cazaría (no debe caer).
const PASAN: [Locale, string][] = [
  ["es", "Exploraste gratis el mundo Calidad y Confianza."], // historia de la bitácora
  ["es", "No sustituye a un consultor humano."], // BANCO §4, la frontera dicha en negativo
  ["es", "tardías · 20%"], // el rótulo ámbar de las tardías es canon (BANCO §3)
  ["en", "late · 20%"],
  ["en", "My Idea doesn't replace a consultant."],
  ["fr", "My Idea ne remplace pas un consultant."],
  ["pt", "O My Idea não substitui um consultor."],
  ["it", "My Idea non sostituisce un consulente."],
  ["zh", "My Idea不能取代顾问。"],
  ["ko", "My Idea는 컨설턴트를 대체하지 않아요."],
  ["ar", "My Idea لا يحل محل المستشار."],
  ["ja", "ワールド「品質と信頼」を無料で探求しました。"],
  ["zh", "你免费探索了“质量与信任”世界。"],
  ["de", "Alles aus der Welt: ihr Fortschritt und ihr Logbuch."], // "ihr" posesivo, no el vosotros
  ["it", "la connessione si è interrotta a metà"], // "a metà" = a mitad de camino, no un estado
  ["en", "the connection dropped halfway through"],
  ["ar", "استكشفتم عالم الجودة مجانًا."], // plural de cortesía (D7), no un "ustedes"
  ["fr", "Garder le cap ou le changer"],
  ["es", "Etapa {{etapa}}: {{dias}} días"],
  ["pt", "Divida seu tempo pela metade"], // aritmética, no un estado de tarea
  ["de", "Wenn dein Projekt in den nächsten Zyklus geht, kannst du diese Welt erneut kostenlos erkunden."], // la frase viva
  ["de", "Wähle, wie ihr im Team entscheidet"], // plural del equipo que el usuario declaró (BANCO §3)
];

describe("guardias de frases por idioma (D8)", () => {
  it("toda regla decide los once idiomas; un idioma sin equivalente lo justifica", () => {
    for (const regla of REGLAS_VOZ) {
      expect(Object.keys(regla.porIdioma).sort(), regla.id).toEqual([...LOCALES].sort());
      expect(regla.origen, regla.id).toMatch(/BANCO|F3_CONVENCIONES|potenciadores/);
      for (const idioma of LOCALES)
        if (regla.porIdioma[idioma].length === 0)
          expect(regla.sinEquivalente[idioma]?.trim(), `${regla.id} [${idioma}] sin equivalente ni motivo`).toBeTruthy();
    }
  });

  it("las reglas de forma valen en todos los idiomas: raya, tres puntos, jerga cruda", () => {
    for (const idioma of LOCALES) {
      expect(rotas("explora — su plan", idioma)).toEqual(["raya"]);
      expect(rotas("entre 3–5 clientes", idioma)).toEqual(["raya"]);
      expect(rotas("Preparando...", idioma)).toEqual(["puntosSuspensivos"]);
      expect(rotas("Construye tu MVP", idioma)).toEqual(["jergaCruda"]);
      expect(rotas("stakeholders", idioma)).toEqual(["jergaCruda"]);
    }
  });

  it("¿ y ¡ solo en español", () => {
    expect(rotas("¿Seguro?", "es")).toEqual([]);
    for (const idioma of LOCALES.filter((l) => l !== "es")) expect(rotas("¿Sure?", idioma)).toEqual(["signosInvertidos"]);
  });

  it("cada equivalente cae en su idioma", () => {
    for (const [id, porIdioma] of Object.entries(CAEN)) {
      expect(REGLAS_VOZ.map((r) => r.id), id).toContain(id);
      for (const idioma of LOCALES) {
        const ejemplo = porIdioma[idioma];
        if (ejemplo === null) {
          expect(REGLAS_VOZ.find((r) => r.id === id)!.porIdioma[idioma], `${id} [${idioma}]`).toEqual([]);
          continue;
        }
        expect(rotas(ejemplo, idioma), `${id} [${idioma}] "${ejemplo}"`).toContain(id);
      }
    }
  });

  it("lo que el canon permite pasa", () => {
    for (const [idioma, texto] of PASAN) expect(rotas(texto, idioma), `[${idioma}] "${texto}"`).toEqual([]);
  });

  it("ningún texto de ningún catálogo, en ningún idioma, rompe una guardia", { timeout: 60_000 }, async () => {
    const hallazgos: string[] = [];
    for (const archivo of archivos(DIR)) {
      const mod = (await import(pathToFileURL(archivo).href)) as Record<string, unknown>;
      for (const [nombre, valor] of Object.entries(mod)) {
        if (!pareceCatalogo(valor)) continue;
        for (const [idioma, cat] of Object.entries(valor)) {
          const recorrer = (x: unknown, ruta: string) => {
            if (typeof x === "string") {
              const f = faltasDeVoz(x, idioma as Locale);
              if (f.length) hallazgos.push(`${path.basename(archivo)}:${nombre}[${idioma}]${ruta} ${JSON.stringify(f)}`);
            } else if (x && typeof x === "object") for (const [k, v] of Object.entries(x)) recorrer(v, `${ruta}.${k}`);
          };
          recorrer(cat, "");
        }
      }
    }
    expect(hallazgos).toEqual([]);
  });

  it("ninguna etiqueta del riel (D3), en ningún idioma, rompe una guardia", () => {
    const hallazgos: string[] = [];
    for (const [idioma, etiquetas] of Object.entries(ETIQUETAS_RIEL))
      for (const [nid, texto] of Object.entries(etiquetas as Record<string, string>)) {
        const f = faltasDeVoz(texto, idioma as Locale);
        if (f.length) hallazgos.push(`${idioma}:${nid} ${JSON.stringify(f)}`);
      }
    expect(hallazgos).toEqual([]);
  });
});
