/**
 * Las ETAPAS del plan validan con clientes, en los ONCE idiomas (decisiones del fundador, 9 oct 2026). Lo que no
 * depende del idioma: las etapas (finalizarPlan neutraliza los rotulos, asi que toda etapa llega como "## Etapa N:") y
 * la regla (en la misma frase, una accion de contacto o de prueba y un cliente; nunca la introduccion ni otra seccion).
 * Lo que si depende: las palabras. Por nodos ya se mira (coberturaContraEtapas) y no basto en los casos reales, porque
 * la autodeclaracion de las etapas no siempre trae los nodos de clientes.
 *
 * Como se compara: en espanol, palabras exactas (la lista medida en la segunda medicion A/B). En portugues, ingles,
 * frances, aleman e italiano, raices al inicio de palabra, sin acentos y en minusculas. En arabe, sin vocales cortas y
 * por subcadena. En japones, chino, coreano e hindi, por subcadena. Las formas de preguntarse a uno mismo no cuentan.
 */
import type { Locale } from "../i18n/config";

/** sinMarcas: quitar acentos y vocales cortas (latinas y arabe); en japones e hindi romperia las palabras. */
type Lista = { verbos: string[]; clientes: string[]; excluir?: string[]; modo: "exacto" | "raiz" | "subcadena"; sinMarcas: boolean };

const LISTAS: Record<Locale, Lista> = {
  es: {
    sinMarcas: true,
    modo: "exacto",
    verbos: [
      "habla", "hablar", "hablale", "hablales", "conversa", "conversar", "conversacion", "conversaciones", "entrevista",
      "entrevistar", "entrevistas", "preguntale", "preguntales", "preguntarle", "preguntarles", "pregunta a", "escucha",
      "escuchar", "observa", "observar", "entrega", "entregala", "entregalo", "entregar", "lanza", "lanzar", "lanzala",
      "prueba", "probar", "pruebala", "atiende", "atender", "muestra", "mostrar", "muestrale", "muestrales", "vende",
      "vender", "venderle", "venderles", "cobra", "cobrar", "cobrale", "cobrales", "preventa", "ofrece", "ofrecer",
      "ofrecele", "ofreceles",
    ],
    clientes: [
      "cliente", "clientes", "comprador", "compradores", "compradora", "compradoras", "usuario", "usuarios", "usuaria",
      "usuarias", "consumidor", "consumidores", "personas reales", "personas que podrian", "personas que llevan",
      "personas que intentan", "personas que usan", "personas que compran", "personas que tienen", "personas que sufren",
    ],
  },
  en: {
    sinMarcas: true,
    modo: "raiz",
    verbos: [
      "talk", "speak", "interview", "ask", "listen", "observe", "watch", "meet", "visit", "call", "survey", "hand",
      "deliver", "launch", "release", "ship", "test", "try", "pilot", "show", "demo", "present", "sell", "charge",
      "presell", "pre-sell", "preorder", "pre-order", "presale", "pre-sale", "offer",
    ],
    clientes: [
      "customer", "client", "buyer", "shopper", "user", "consumer", "real people", "people who would", "people who could",
      "people who might", "people who use", "people who buy", "people who keep", "people who try", "people who have",
      "people who already", "people who struggle",
    ],
    excluir: ["ask yourself", "ask yourselves"],
  },
  pt: {
    sinMarcas: true,
    modo: "raiz",
    verbos: [
      "convers", "fale com", "fala com", "falar com", "entrevist", "pergunt", "escut", "ouc", "observ", "visit", "lig",
      "entreg", "lanc", "test", "experiment", "mostr", "apresent", "vend", "cobr", "pre-venda", "prevenda", "ofere",
    ],
    clientes: ["client", "comprador", "usuari", "utilizador", "consumidor", "pessoas reais", "pessoas que"],
    excluir: ["pergunte-se", "pergunta-te", "pergunte a si", "pergunta a si"],
  },
  fr: {
    sinMarcas: true,
    modo: "raiz",
    verbos: [
      "parl", "discut", "convers", "interview", "entretien", "interroge", "demand", "ecout", "observ", "rencontr",
      "appel", "livr", "remet", "confi", "lanc", "test", "essai", "essay", "montr", "present", "vend", "factur",
      "prevente", "pre-vente", "propos", "offr",
    ],
    clientes: ["client", "acheteu", "utilisat", "consommat", "personnes reelles", "personnes qui", "gens qui"],
    excluir: ["demande-toi", "demandez-vous", "demande toi", "demandez vous"],
  },
  de: {
    sinMarcas: true,
    modo: "raiz",
    verbos: [
      "sprich", "sprech", "rede", "reden", "gesprach", "interview", "befrag", "frag", "hore", "horen", "zuhor",
      "beobacht", "besuch", "ruf", "ubergib", "ubergeb", "liefer", "start", "test", "probier", "zeig", "prasentier",
      "verkauf", "biet", "anbiet",
    ],
    clientes: ["kunde", "kundin", "kaufer", "nutzer", "benutzer", "anwender", "verbraucher", "echte menschen", "menschen, die", "menschen die"],
    excluir: ["frag dich", "fragen sie sich", "frage dich"],
  },
  it: {
    sinMarcas: true,
    modo: "raiz",
    verbos: [
      "parl", "convers", "intervist", "chied", "domand", "ascolt", "osserv", "incontr", "chiam", "consegn", "lanc",
      "test", "prov", "mostr", "present", "vend", "far pagare", "fai pagare", "prevendit", "offr", "propon",
    ],
    clientes: ["client", "acquirent", "utent", "utilizzator", "consumator", "persone reali", "persone che"],
    excluir: ["chiediti", "domandati", "chiedetevi", "chiedi a te stess"],
  },
  ja: {
    sinMarcas: false,
    modo: "subcadena",
    verbos: ["話", "聞", "インタビュー", "尋ね", "質問", "観察", "訪問", "渡", "届け", "発売", "リリース", "試", "テスト", "見せ", "紹介", "提案", "販売", "売"],
    clientes: ["顧客", "お客", "ユーザー", "利用者", "購入者", "買い手", "消費者"],
  },
  zh: {
    sinMarcas: false,
    modo: "subcadena",
    verbos: ["交谈", "聊", "访谈", "采访", "询问", "请教", "倾听", "观察", "拜访", "联系", "交给", "发布", "推出", "测试", "试用", "展示", "销售", "出售", "卖给", "预售", "收费", "提供给"],
    clientes: ["客户", "顾客", "买家", "用户", "消费者", "使用者"],
  },
  ko: {
    sinMarcas: false,
    modo: "subcadena",
    verbos: ["이야기", "대화", "인터뷰", "물어", "질문", "들어", "경청", "관찰", "만나", "방문", "전달", "출시", "테스트", "시험", "보여", "판매", "선판매", "제공"],
    clientes: ["고객", "손님", "사용자", "구매자", "소비자", "이용자"],
  },
  ar: {
    sinMarcas: true,
    modo: "subcadena",
    verbos: ["تحدث", "حاور", "حوار", "قابل", "مقابل", "اسأل", "سؤال", "استمع", "لاحظ", "راقب", "زر", "تواصل", "سلم", "أطلق", "اطلق", "اختبر", "جرب", "اعرض", "بيع", "قدم"],
    clientes: ["عملاء", "عميل", "زبائن", "زبون", "مستخدم", "مشتر", "مستهلك"],
  },
  hi: {
    sinMarcas: false,
    modo: "subcadena",
    verbos: ["बात", "साक्षात्कार", "इंटरव्यू", "पूछ", "सुन", "देख", "अवलोकन", "मिल", "सौंप", "लॉन्च", "परीक्षण", "टेस्ट", "आज़मा", "दिखा", "बेच", "बिक्री", "पेशकश"],
    clientes: ["ग्राहक", "उपयोगकर्ता", "यूज़र", "यूजर", "खरीदार", "उपभोक्ता"],
  },
};

const escapar = (x: string) => x.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
const sinMarcas = (s: string) => s.normalize("NFD").replace(/\p{Mn}/gu, "").normalize("NFC").toLowerCase();
const llano = (s: string) => s.normalize("NFC").toLowerCase();
const forma = (l: Lista) => (l.sinMarcas ? sinMarcas : llano);

function comparador(lista: Lista): (frase: string) => boolean {
  const f0 = forma(lista);
  const l = { ...lista, verbos: lista.verbos.map(f0), clientes: lista.clientes.map(f0) };
  if (l.modo === "subcadena") {
    return (f) => l.verbos.some((v) => f.includes(v)) && l.clientes.some((c) => f.includes(c));
  }
  const borde = "(?:^|[^\\p{L}\\p{N}])";
  const fin = l.modo === "exacto" ? "(?=$|[^\\p{L}\\p{N}])" : "";
  const re = (xs: string[]) => new RegExp(`${borde}(?:${xs.map(escapar).join("|")})${fin}`, "u");
  const verbo = re(l.verbos);
  const cliente = re(l.clientes);
  return (f) => verbo.test(f) && cliente.test(f);
}

const COMPARADORES = Object.fromEntries(Object.entries(LISTAS).map(([k, l]) => [k, comparador(l)])) as Record<Locale, (f: string) => boolean>;
const ENCABEZADO_ETAPA = /^#{2,4}\s*etapa\s+\d+\s*[:.-]?\s*/i;

/** Los idiomas con lista (todos los activos). */
export const IDIOMAS_VALIDACION_CLIENTES = Object.keys(LISTAS) as Locale[];

/** Las etapas del plan validan con clientes, leidas con la lista del espanol (base) y la del idioma del plan. */
export function validaConClientes(cuerpo: string, idiomas: Locale[]): boolean {
  const frases: string[] = [];
  let enEtapa = false;
  for (const linea of cuerpo.split("\n")) {
    const t = linea.trim();
    if (t.startsWith("#")) {
      enEtapa = ENCABEZADO_ETAPA.test(t);
      if (enEtapa) frases.push(t.replace(ENCABEZADO_ETAPA, ""));
      continue;
    }
    if (enEtapa && t) frases.push(t);
  }
  const cortar = (f: string) => f.split(/[.!?;。！？；؟।]+/);
  return [...new Set(idiomas)].some((idioma) => {
    const l = LISTAS[idioma];
    const comparar = COMPARADORES[idioma];
    if (!l || !comparar) return false;
    const partes = frases.flatMap((f) => cortar(forma(l)(f)));
    const fuera = (l.excluir ?? []).map(forma(l));
    return partes.some((p) => comparar(fuera.reduce((acc, x) => acc.split(x).join(" "), p)));
  });
}
