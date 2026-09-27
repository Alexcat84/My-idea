/**
 * Los avisos de un nodo en la tarjeta de pregunta (app/ui/TarjetaPregunta.tsx), decision del fundador del
 * 26 sep 2026 (saneamiento del dataset, tanda 1, puntos 3 y 4; docs/POLITICA_MARCO_PAIS.md):
 *   - clase B: el ejemplo es de un pais y la clase existe en casi todos;
 *   - clase C: nodo-frontera, aplica a quien opera o vende en ese pais;
 *   - vigencia: el nodo depende de una norma, un plazo, una cifra con fecha o una institucion. REGLA ESTRICTA
 *     (fundador, 26 sep 2026): el cliente nunca ve el titulo de un libro ni un autor como fuente; el aviso dice
 *     solo el ano ("Esta informacion puede haber cambiado desde [ano]").
 * Los paises llevan sus dos formas por idioma ("desde" y "en"), porque en varios idiomas la preposicion
 * se funde con el articulo (des Etats-Unis, aux Etats-Unis). Un pais nuevo en dataset/metadata/jurisdiccion.json
 * necesita su entrada aqui en los once idiomas (lo exige web/lib/engine/avisos.test.ts).
 */
import type { PorIdioma } from "../config";

type Pais = { desde: string; en: string };

const es = {
  claseB: "Ejemplo de {{desde}}: busca el equivalente en tu país.",
  claseC: "Aplica si operas o vendes en {{en}}.",
  vigencia: "Esta información puede haber cambiado desde {{anio}}: verifica la norma vigente en tu país.",
  vigenciaSinAnio: "Esta información puede haber cambiado: verifica la norma vigente en tu país.",
  paises: {
    US: { desde: "Estados Unidos", en: "Estados Unidos" } as Pais,
    EU: { desde: "la Unión Europea", en: "la Unión Europea" } as Pais,
    CA: { desde: "Canadá", en: "Canadá" } as Pais,
    GB: { desde: "el Reino Unido", en: "el Reino Unido" } as Pais,
    FR: { desde: "Francia", en: "Francia" } as Pais,
    MX: { desde: "México", en: "México" } as Pais,
    ES: { desde: "España", en: "España" } as Pais,
    CO: { desde: "Colombia", en: "Colombia" } as Pais,
    AR: { desde: "Argentina", en: "Argentina" } as Pais,
  },
};

const en: typeof es = {
  claseB: "Example from {{desde}}: look for the equivalent in your country.",
  claseC: "Applies if you operate or sell in {{en}}.",
  vigencia: "This information may have changed since {{anio}}: check the rules in force in your country.",
  vigenciaSinAnio: "This information may have changed: check the rules in force in your country.",
  paises: {
    US: { desde: "the United States", en: "the United States" },
    EU: { desde: "the European Union", en: "the European Union" },
    CA: { desde: "Canada", en: "Canada" },
    GB: { desde: "the United Kingdom", en: "the United Kingdom" },
    FR: { desde: "France", en: "France" },
    MX: { desde: "Mexico", en: "Mexico" },
    ES: { desde: "Spain", en: "Spain" },
    CO: { desde: "Colombia", en: "Colombia" },
    AR: { desde: "Argentina", en: "Argentina" },
  },
};

const fr: typeof es = {
  claseB: "Exemple {{desde}} : cherche l'équivalent dans ton pays.",
  claseC: "S'applique si tu opères ou vends {{en}}.",
  vigencia: "Cette information a pu changer depuis {{anio}} : vérifie la réglementation en vigueur dans ton pays.",
  vigenciaSinAnio: "Cette information a pu changer : vérifie la réglementation en vigueur dans ton pays.",
  paises: {
    US: { desde: "des États-Unis", en: "aux États-Unis" },
    EU: { desde: "de l'Union européenne", en: "dans l'Union européenne" },
    CA: { desde: "du Canada", en: "au Canada" },
    GB: { desde: "du Royaume-Uni", en: "au Royaume-Uni" },
    FR: { desde: "de France", en: "en France" },
    MX: { desde: "du Mexique", en: "au Mexique" },
    ES: { desde: "d'Espagne", en: "en Espagne" },
    CO: { desde: "de Colombie", en: "en Colombie" },
    AR: { desde: "d'Argentine", en: "en Argentine" },
  },
};

const pt: typeof es = {
  claseB: "Exemplo {{desde}}: procure o equivalente no seu país.",
  claseC: "Aplica-se se você opera ou vende {{en}}.",
  vigencia: "Esta informação pode ter mudado desde {{anio}}: verifique a norma vigente no seu país.",
  vigenciaSinAnio: "Esta informação pode ter mudado: verifique a norma vigente no seu país.",
  paises: {
    US: { desde: "dos Estados Unidos", en: "nos Estados Unidos" },
    EU: { desde: "da União Europeia", en: "na União Europeia" },
    CA: { desde: "do Canadá", en: "no Canadá" },
    GB: { desde: "do Reino Unido", en: "no Reino Unido" },
    FR: { desde: "da França", en: "na França" },
    MX: { desde: "do México", en: "no México" },
    ES: { desde: "da Espanha", en: "na Espanha" },
    CO: { desde: "da Colômbia", en: "na Colômbia" },
    AR: { desde: "da Argentina", en: "na Argentina" },
  },
};

const de: typeof es = {
  claseB: "Beispiel aus {{desde}}: Such die Entsprechung in deinem Land.",
  claseC: "Gilt, wenn du {{en}} tätig bist oder verkaufst.",
  vigencia: "Diese Information kann sich seit {{anio}} geändert haben: Prüf die in deinem Land geltende Regelung.",
  vigenciaSinAnio: "Diese Information kann sich geändert haben: Prüf die in deinem Land geltende Regelung.",
  paises: {
    US: { desde: "den USA", en: "in den USA" },
    EU: { desde: "der Europäischen Union", en: "in der Europäischen Union" },
    CA: { desde: "Kanada", en: "in Kanada" },
    GB: { desde: "dem Vereinigten Königreich", en: "im Vereinigten Königreich" },
    FR: { desde: "Frankreich", en: "in Frankreich" },
    MX: { desde: "Mexiko", en: "in Mexiko" },
    ES: { desde: "Spanien", en: "in Spanien" },
    CO: { desde: "Kolumbien", en: "in Kolumbien" },
    AR: { desde: "Argentinien", en: "in Argentinien" },
  },
};

const it: typeof es = {
  claseB: "Esempio {{desde}}: cerca l'equivalente nel tuo paese.",
  claseC: "Si applica se operi o vendi {{en}}.",
  vigencia: "Questa informazione potrebbe essere cambiata dal {{anio}}: verifica la norma in vigore nel tuo paese.",
  vigenciaSinAnio: "Questa informazione potrebbe essere cambiata: verifica la norma in vigore nel tuo paese.",
  paises: {
    US: { desde: "degli Stati Uniti", en: "negli Stati Uniti" },
    EU: { desde: "dell'Unione europea", en: "nell'Unione europea" },
    CA: { desde: "del Canada", en: "in Canada" },
    GB: { desde: "del Regno Unito", en: "nel Regno Unito" },
    FR: { desde: "della Francia", en: "in Francia" },
    MX: { desde: "del Messico", en: "in Messico" },
    ES: { desde: "della Spagna", en: "in Spagna" },
    CO: { desde: "della Colombia", en: "in Colombia" },
    AR: { desde: "dell'Argentina", en: "in Argentina" },
  },
};

const ja: typeof es = {
  claseB: "{{desde}}の例です。あなたの国で相当するものを探してください。",
  claseC: "{{en}}で事業を行う、または販売する場合に適用されます。",
  vigencia: "この情報は{{anio}}年以降に変わっている可能性があります：あなたの国の現行の規則を確認してください。",
  vigenciaSinAnio: "この情報は変わっている可能性があります：あなたの国の現行の規則を確認してください。",
  paises: {
    US: { desde: "米国", en: "米国" },
    EU: { desde: "欧州連合", en: "欧州連合" },
    CA: { desde: "カナダ", en: "カナダ" },
    GB: { desde: "英国", en: "英国" },
    FR: { desde: "フランス", en: "フランス" },
    MX: { desde: "メキシコ", en: "メキシコ" },
    ES: { desde: "スペイン", en: "スペイン" },
    CO: { desde: "コロンビア", en: "コロンビア" },
    AR: { desde: "アルゼンチン", en: "アルゼンチン" },
  },
};

const zh: typeof es = {
  claseB: "这是{{desde}}的例子：请在你所在的国家查找对应的规定。",
  claseC: "适用于在{{en}}经营或销售的情况。",
  vigencia: "此信息自{{anio}}年以来可能已有变化：请核实你所在国家现行的规定。",
  vigenciaSinAnio: "此信息可能已有变化：请核实你所在国家现行的规定。",
  paises: {
    US: { desde: "美国", en: "美国" },
    EU: { desde: "欧盟", en: "欧盟" },
    CA: { desde: "加拿大", en: "加拿大" },
    GB: { desde: "英国", en: "英国" },
    FR: { desde: "法国", en: "法国" },
    MX: { desde: "墨西哥", en: "墨西哥" },
    ES: { desde: "西班牙", en: "西班牙" },
    CO: { desde: "哥伦比亚", en: "哥伦比亚" },
    AR: { desde: "阿根廷", en: "阿根廷" },
  },
};

const ko: typeof es = {
  claseB: "{{desde}}의 사례예요. 자신의 나라에서 이에 해당하는 것을 찾아보세요.",
  claseC: "{{en}}에서 사업하거나 판매한다면 적용돼요.",
  vigencia: "이 정보는 {{anio}}년 이후 바뀌었을 수 있어요. 자신의 나라에서 현재 유효한 규정을 확인하세요.",
  vigenciaSinAnio: "이 정보는 바뀌었을 수 있어요. 자신의 나라에서 현재 유효한 규정을 확인하세요.",
  paises: {
    US: { desde: "미국", en: "미국" },
    EU: { desde: "유럽연합", en: "유럽연합" },
    CA: { desde: "캐나다", en: "캐나다" },
    GB: { desde: "영국", en: "영국" },
    FR: { desde: "프랑스", en: "프랑스" },
    MX: { desde: "멕시코", en: "멕시코" },
    ES: { desde: "스페인", en: "스페인" },
    CO: { desde: "콜롬비아", en: "콜롬비아" },
    AR: { desde: "아르헨티나", en: "아르헨티나" },
  },
};

const ar: typeof es = {
  claseB: "مثال من {{desde}}: ابحثوا عن المقابل في بلدكم.",
  claseC: "ينطبق إذا كنتم تعملون أو تبيعون في {{en}}.",
  vigencia: "ربما تغيّرت هذه المعلومات منذ {{anio}}: تحقّقوا من القواعد السارية في بلدكم.",
  vigenciaSinAnio: "ربما تغيّرت هذه المعلومات: تحقّقوا من القواعد السارية في بلدكم.",
  paises: {
    US: { desde: "الولايات المتحدة", en: "الولايات المتحدة" },
    EU: { desde: "الاتحاد الأوروبي", en: "الاتحاد الأوروبي" },
    CA: { desde: "كندا", en: "كندا" },
    GB: { desde: "المملكة المتحدة", en: "المملكة المتحدة" },
    FR: { desde: "فرنسا", en: "فرنسا" },
    MX: { desde: "المكسيك", en: "المكسيك" },
    ES: { desde: "إسبانيا", en: "إسبانيا" },
    CO: { desde: "كولومبيا", en: "كولومبيا" },
    AR: { desde: "الأرجنتين", en: "الأرجنتين" },
  },
};

const hi: typeof es = {
  claseB: "{{desde}} का उदाहरण: अपने देश में इसका समकक्ष खोजिए।",
  claseC: "{{en}} में काम करने या बेचने पर लागू होता है।",
  vigencia: "यह जानकारी {{anio}} के बाद बदल गई हो सकती है: अपने देश में लागू नियम की जाँच कीजिए।",
  vigenciaSinAnio: "यह जानकारी बदल गई हो सकती है: अपने देश में लागू नियम की जाँच कीजिए।",
  paises: {
    US: { desde: "संयुक्त राज्य अमेरिका", en: "संयुक्त राज्य अमेरिका" },
    EU: { desde: "यूरोपीय संघ", en: "यूरोपीय संघ" },
    CA: { desde: "कनाडा", en: "कनाडा" },
    GB: { desde: "यूनाइटेड किंगडम", en: "यूनाइटेड किंगडम" },
    FR: { desde: "फ़्रांस", en: "फ़्रांस" },
    MX: { desde: "मेक्सिको", en: "मेक्सिको" },
    ES: { desde: "स्पेन", en: "स्पेन" },
    CO: { desde: "कोलंबिया", en: "कोलंबिया" },
    AR: { desde: "अर्जेंटीना", en: "अर्जेंटीना" },
  },
};

export const AVISO_NODO: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
export type CodigoPais = keyof typeof es.paises;
