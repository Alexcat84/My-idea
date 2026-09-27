/**
 * readiness.ts - Fase 3.0: port TypeScript de engine/plan_readiness.py.
 * Clasifica nodos en familias para el medidor de completitud (Fase 2.2).
 * Clasificacion por palabras clave (sin llamadas a la API), sobre
 * titulo_concepto + resumen_teorico, normalizados (sin acentos,
 * minusculas). En runtime, la web usa el node_families.json ya
 * precalculado (sincronizado por scripts/sync_assets_web.py) via
 * cargarFamilies() -- clasificarGrafo()/clasificarNodo() se conservan
 * para paridad y para poder reclasificar si el dataset cambia.
 */
import nodeFamiliesJson from "./assets/node_families.json";
import { textosFamiliaFaltante } from "./engine/constants";
import { LOCALE_BASE, type Locale } from "./i18n/config";

export const MIN_NODOS_COMPLETA = 5;

// Revisar/ajustar aqui. Coincidencia por substring sobre texto normalizado
// (sin acentos, minusculas) de titulo_concepto + resumen_teorico.
export const KEYWORDS_ACCION_CLIENTES = [
  "entrevista", "voz del cliente", "mvp", "producto minimo viable",
  "prueba de usuario", "pruebas de usuario", "testeo con usuario",
  "validacion con cliente", "desarrollo de clientes", "customer development",
  "customer discovery", "investigacion de usuario", "user research",
  "prototipo", "feedback de cliente", "retroalimentacion de cliente",
  "presentacion del problema", "descubrimiento de clientes",
  "investigacion etnografica", "observacion de campo",
];

export const KEYWORDS_VIABILIDAD_ECONOMICA = [
  "punto de equilibrio", "flujo de caja", "flujo de efectivo",
  "unit economics", "metricas financieras", "modelo de ingresos",
  "estructura de costos", "analisis financiero", "proyeccion financiera",
  "presupuesto operativo", "margen de contribucion", "burn rate", "runway",
  "break even", "break-even", "estado de resultados",
  "inteligencia financiera", "arte de las finanzas", "fuentes de financiamiento",
  "rentabilidad", "numeros del negocio", "precio de venta",
  "estrategia de precios", "modelo de precios",
];

/**
 * i18n F6: las MISMAS dos familias, con sus palabras en cada idioma, para leer
 * un PLAN (no el grafo). El grafo sigue en español (DISENO §1) y se clasifica
 * con las dos listas de arriba, que son las del español de aquí. El respaldo
 * por encabezados del plan (planRedactor.familiasDesdeEncabezados) lee
 * markdown escrito en el idioma de la idea: sin estas listas, fuera del
 * español perdía la familia en silencio.
 *
 * Mismo criterio que el español: frases de oficio, no palabras sueltas que
 * salgan en cualquier plan ("cliente" solo no basta, "entrevista" sí). Se
 * comparan normalizadas con normalizarParaPalabras (minúsculas, sin acentos,
 * sin signos de vocal del árabe ni nukta del hindi, álef unificado): aquí van
 * con su ortografía normal.
 */
export type PalabrasFamilias = Record<"accion_clientes" | "viabilidad_economica", readonly string[]>;

export const PALABRAS_FAMILIAS_PLAN: Record<Locale, PalabrasFamilias> = {
  es: { accion_clientes: KEYWORDS_ACCION_CLIENTES, viabilidad_economica: KEYWORDS_VIABILIDAD_ECONOMICA },
  en: {
    accion_clientes: [
      "interview", "voice of the customer", "mvp", "minimum viable product", "user test", "usability test",
      "customer validation", "validate with customers", "validate with real customers", "customer development",
      "customer discovery", "user research", "prototype", "customer feedback", "field observation", "ethnograph",
    ],
    viabilidad_economica: [
      "break-even", "break even", "cash flow", "unit economics", "financial metrics", "revenue model",
      "cost structure", "financial analysis", "financial projection", "financial forecast", "operating budget",
      "contribution margin", "burn rate", "runway", "income statement", "profitability", "funding sources",
      "sources of funding", "selling price", "sale price", "pricing strategy", "pricing model", "business numbers",
    ],
  },
  pt: {
    accion_clientes: [
      "entrevista", "voz do cliente", "mvp", "produto mínimo viável", "teste de usuário", "testes de usuário",
      "teste com usuários", "testes com usuários", "validação com clientes", "validar com clientes",
      "desenvolvimento de clientes", "descoberta de clientes", "pesquisa com usuários", "pesquisa de usuário",
      "protótipo", "feedback de clientes", "feedback do cliente", "observação de campo", "etnográf",
    ],
    viabilidad_economica: [
      "ponto de equilíbrio", "fluxo de caixa", "unit economics", "métricas financeiras", "modelo de receita",
      "estrutura de custos", "análise financeira", "projeção financeira", "orçamento operacional",
      "margem de contribuição", "burn rate", "runway", "break-even", "demonstração de resultados", "rentabilidade",
      "lucratividade", "fontes de financiamento", "preço de venda", "estratégia de preços", "precificação",
      "números do negócio",
    ],
  },
  fr: {
    accion_clientes: [
      "entretien", "entrevue", "voix du client", "mvp", "produit minimum viable", "produit minimal viable",
      "test utilisateur", "tests utilisateurs", "tests auprès des utilisateurs", "validation client",
      "valider auprès des clients", "développement client", "découverte client", "recherche utilisateur",
      "prototype", "rétroaction des clients", "retour client", "retours clients", "observation sur le terrain",
      "ethnograph",
    ],
    viabilidad_economica: [
      "seuil de rentabilité", "point mort", "flux de trésorerie", "unit economics", "indicateurs financiers",
      "modèle de revenus", "structure des coûts", "structure de coûts", "analyse financière",
      "projection financière", "prévisions financières", "budget d’exploitation", "budget d'exploitation",
      "marge sur coûts variables", "marge de contribution", "burn rate", "runway", "état des résultats",
      "compte de résultat", "rentabilité", "sources de financement", "prix de vente", "stratégie de prix",
      "stratégie de tarification", "modèle de tarification", "tarification",
    ],
  },
  de: {
    accion_clientes: [
      "interview", "kundengespräch", "stimme des kunden", "mvp", "minimal funktionsfähiges produkt", "nutzertest",
      "usability-test", "kundenvalidierung", "mit kunden validieren", "customer development", "kundenentwicklung",
      "customer discovery", "nutzerforschung", "user research", "prototyp", "kundenfeedback",
      "feedback von kunden", "feldbeobachtung", "ethnograf",
    ],
    viabilidad_economica: [
      "gewinnschwelle", "break-even", "break even", "cashflow", "cash-flow", "unit economics", "finanzkennzahlen",
      "erlösmodell", "umsatzmodell", "kostenstruktur", "finanzanalyse", "finanzprognose", "finanzplanung",
      "betriebsbudget", "deckungsbeitrag", "burn rate", "runway", "gewinn- und verlustrechnung", "rentabilität",
      "wirtschaftlichkeit", "finanzierungsquellen", "verkaufspreis", "preisstrategie", "preismodell",
      "preisgestaltung",
    ],
  },
  it: {
    accion_clientes: [
      "intervista", "interviste", "voce del cliente", "mvp", "prodotto minimo funzionante",
      "prodotto minimo praticabile", "test con gli utenti", "test con utenti", "test utente",
      "validazione con i clienti", "validare con i clienti", "customer development", "sviluppo dei clienti",
      "customer discovery", "scoperta dei clienti", "ricerca sugli utenti", "user research", "prototipo",
      "feedback dei clienti", "feedback del cliente", "osservazione sul campo", "etnograf",
    ],
    viabilidad_economica: [
      "punto di pareggio", "break-even", "break even", "flusso di cassa", "cash flow", "unit economics",
      "metriche finanziarie", "modello di ricavi", "struttura dei costi", "analisi finanziaria",
      "proiezione finanziaria", "budget operativo", "margine di contribuzione", "burn rate", "runway",
      "conto economico", "redditività", "fonti di finanziamento", "prezzo di vendita", "strategia di prezzo",
      "strategia dei prezzi", "modello di prezzo",
    ],
  },
  ja: {
    accion_clientes: [
      "インタビュー", "顧客の声", "お客様の声", "mvp", "実用最小限の製品", "ユーザーテスト", "ユーザー調査",
      "顧客検証", "顧客開発", "顧客発見", "プロトタイプ", "試作品", "顧客のフィードバック",
      "顧客からのフィードバック", "現場観察", "エスノグラフィ",
    ],
    viabilidad_economica: [
      "損益分岐点", "キャッシュフロー", "資金繰り", "ユニットエコノミクス", "財務指標", "収益モデル", "コスト構造",
      "財務分析", "財務予測", "収支計画", "運営予算", "限界利益", "貢献利益", "バーンレート", "ランウェイ",
      "損益計算書", "収益性", "資金調達", "販売価格", "価格戦略", "価格設定", "価格モデル",
    ],
  },
  zh: {
    accion_clientes: [
      "访谈", "采访", "客户之声", "用户之声", "mvp", "最小可行产品", "用户测试", "可用性测试", "客户验证",
      "客户开发", "客户发现", "用户研究", "原型", "客户反馈", "用户反馈", "实地观察", "民族志",
    ],
    viabilidad_economica: [
      "盈亏平衡", "现金流", "单位经济", "财务指标", "收入模式", "盈利模式", "成本结构", "财务分析", "财务预测",
      "运营预算", "边际贡献", "贡献毛利", "烧钱率", "资金跑道", "利润表", "损益表", "盈利能力", "融资来源",
      "资金来源", "销售价格", "定价策略", "定价模式",
    ],
  },
  ko: {
    accion_clientes: [
      "인터뷰", "고객의 목소리", "mvp", "최소 기능 제품", "최소 실행 가능 제품", "사용자 테스트", "사용성 테스트",
      "고객 검증", "고객 개발", "고객 발견", "사용자 조사", "사용자 리서치", "프로토타입", "시제품",
      "고객 피드백", "현장 관찰", "민족지",
    ],
    viabilidad_economica: [
      "손익분기", "현금 흐름", "현금흐름", "단위 경제성", "유닛 이코노믹스", "재무 지표", "수익 모델",
      "비용 구조", "재무 분석", "재무 예측", "운영 예산", "공헌 이익", "번 레이트", "런웨이", "손익계산서",
      "수익성", "자금 조달", "판매 가격", "가격 전략", "가격 책정", "가격 모델",
    ],
  },
  ar: {
    accion_clientes: [
      "مقابلة", "مقابلات", "صوت العميل", "mvp", "المنتج الأدنى القابل للتطبيق", "الحد الأدنى من المنتج",
      "اختبار المستخدم", "اختبار المستخدمين", "اختبار مع المستخدمين", "التحقق مع العملاء", "تطوير العملاء",
      "اكتشاف العملاء", "بحث المستخدمين", "أبحاث المستخدمين", "نموذج أولي", "النموذج الأولي",
      "ملاحظات العملاء", "آراء العملاء", "الملاحظة الميدانية",
    ],
    viabilidad_economica: [
      "نقطة التعادل", "التدفق النقدي", "التدفقات النقدية", "اقتصاديات الوحدة", "المؤشرات المالية",
      "مؤشرات مالية", "نموذج الإيرادات", "هيكل التكاليف", "التحليل المالي", "تحليل مالي",
      "التوقعات المالية", "توقعات مالية", "الميزانية التشغيلية", "هامش المساهمة", "معدل الحرق",
      "قائمة الدخل", "الربحية", "مصادر التمويل", "سعر البيع", "استراتيجية التسعير", "نموذج التسعير",
    ],
  },
  hi: {
    accion_clientes: [
      "इंटरव्यू", "साक्षात्कार", "ग्राहकों से बातचीत", "ग्राहक की आवाज़", "mvp", "न्यूनतम व्यवहार्य उत्पाद",
      "यूज़र टेस्ट", "उपयोगकर्ता परीक्षण", "ग्राहक सत्यापन", "कस्टमर डेवलपमेंट", "ग्राहक विकास", "ग्राहक खोज",
      "उपयोगकर्ता शोध", "प्रोटोटाइप", "ग्राहक फ़ीडबैक", "ग्राहकों की प्रतिक्रिया", "फ़ील्ड अवलोकन",
    ],
    viabilidad_economica: [
      "ब्रेक-ईवन", "ब्रेक ईवन", "नकदी प्रवाह", "कैश फ्लो", "यूनिट इकोनॉमिक्स", "वित्तीय संकेतक", "राजस्व मॉडल",
      "आय मॉडल", "लागत संरचना", "वित्तीय विश्लेषण", "वित्तीय अनुमान", "परिचालन बजट", "योगदान मार्जिन",
      "बर्न रेट", "रनवे", "आय विवरण", "लाभप्रदता", "फंडिंग के स्रोत", "वित्तपोषण के स्रोत", "बिक्री मूल्य",
      "मूल्य निर्धारण", "मूल्य रणनीति",
    ],
  },
};

/** Normaliza para comparar las palabras de un plan en cualquier idioma: la de
 * siempre (minúsculas, sin acentos latinos) más los signos de vocal y el
 * tatweel del árabe, el álef con hamza como álef, y el nukta del devanagari.
 * No reemplaza a normalizarTexto: el grafo se clasifica igual que en Python. */
export function normalizarParaPalabras(texto: string): string {
  return normalizarTexto(texto)
    .replace(/[ً-ٰٟـ]/g, "")
    .replace(/[آأإ]/g, "ا")
    .replace(/ى/g, "ي")
    .replace(/़/g, "");
}

export type Familia = "accion_clientes" | "viabilidad_economica" | "general";

interface NodoGrafo {
  titulo_concepto?: string;
  resumen_teorico?: string;
  [key: string]: unknown;
}

// Exportadas (Hotfix v2.2.1): planRedactor.ts las reusa para el respaldo
// de autodeclaracion basado en encabezados (familiasDesdeEncabezados),
// mismo criterio deterministico que clasificarNodo aplica a los nodos del
// grafo, aplicado ahora al markdown ya generado.
export function normalizarTexto(texto: string): string {
  // NFKD descompone "á" en "a" + U+0301 (acento combinante); el rango
  // ̀-ͯ (Combining Diacritical Marks) es el equivalente en JS
  // de filtrar por unicodedata.combining(c) != 0 en Python.
  return texto
    .toLowerCase()
    .normalize("NFKD")
    .replace(/[̀-ͯ]/g, "");
}

export function coincideKeyword(textoNormalizado: string, palabrasClave: string[]): boolean {
  return palabrasClave.some((p) => textoNormalizado.includes(p));
}

export function clasificarNodo(node: NodoGrafo): Familia {
  const texto = normalizarTexto(`${node.titulo_concepto ?? ""} ${node.resumen_teorico ?? ""}`);
  if (coincideKeyword(texto, KEYWORDS_ACCION_CLIENTES)) return "accion_clientes";
  if (coincideKeyword(texto, KEYWORDS_VIABILIDAD_ECONOMICA)) return "viabilidad_economica";
  return "general";
}

export function clasificarGrafo(graph: Record<string, NodoGrafo>): Record<string, Familia> {
  return Object.fromEntries(Object.entries(graph).map(([nid, n]) => [nid, clasificarNodo(n)]));
}

/** node_families.json ya sincronizado (Fase 3.0) -- equivalente a
 * cargar_families() cuando FAMILIES_PATH.exists() en Python. */
export function cargarFamilies(): Record<string, Familia> {
  return nodeFamiliesJson as Record<string, Familia>;
}

export interface EvaluacionCobertura {
  es_completa: boolean;
  tiene_accion_clientes: boolean;
  tiene_viabilidad_economica: boolean;
  num_nodos: number;
  familias_faltantes: string[];
}

/**
 * Evalua si una ruta esta lista para un plan completo (toca >=1 nodo de
 * accion_clientes y >=1 de viabilidad_economica, con al menos 5 nodos).
 */
export function evaluarRuta(
  ruta: string[],
  families: Record<string, Familia>,
  /** i18n: el idioma de los textos de lo que falta (el recorrido pasa el de la
   * interfaz; el plan, que es documento, queda en el base hasta F5). */
  idioma: Locale = LOCALE_BASE
): EvaluacionCobertura {
  const familiasEnRuta = new Set(ruta.map((nid) => families[nid] ?? "general"));
  const tieneAccion = familiasEnRuta.has("accion_clientes");
  const tieneViabilidad = familiasEnRuta.has("viabilidad_economica");
  const esCompleta = tieneAccion && tieneViabilidad && ruta.length >= MIN_NODOS_COMPLETA;
  const faltantes: string[] = [];
  // AUD-09 M33: los textos de la fuente única (constants.ts).
  const texto = textosFamiliaFaltante(idioma);
  if (!tieneAccion) faltantes.push(texto.accion_clientes);
  if (!tieneViabilidad) faltantes.push(texto.viabilidad_economica);
  if (ruta.length < MIN_NODOS_COMPLETA) faltantes.push(texto.profundidad);
  return {
    es_completa: esCompleta,
    tiene_accion_clientes: tieneAccion,
    tiene_viabilidad_economica: tieneViabilidad,
    num_nodos: ruta.length,
    familias_faltantes: faltantes,
  };
}
