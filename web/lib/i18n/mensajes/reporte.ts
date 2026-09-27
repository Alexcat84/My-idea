/** El reporte de Tus Números (lib/engine/reporte.ts): las preguntas de la
 * mini-entrevista (con {{u}} = la unidad de venta del usuario), el reporte del
 * guardián GIGO y el respaldo sin IA. Los "## ", "- " y "> " son estructura
 * markdown del documento. */
import type { PorIdioma } from "../config";

const es = {
  /** la unidad de venta cuando el usuario no dio ninguna (va dentro de las preguntas) */
  unidadPorOmision: "unidad",
  preguntas: {
    servicio: {
      costo_materiales_unidad:
        "¿Cuánto te cuesta directamente cada {{u}} (insumos, materiales que uses, etc.)? Un número aproximado sirve; si no tienes, responde 0.",
      horas_por_unidad: "¿Cuántas horas de trabajo te toma cada {{u}}?",
      valor_hora: "¿En cuánto valoras tu hora de trabajo (lo que sientes que deberías ganar por hora)?",
      precio_tentativo: "¿A qué precio cobras (o cobrarías) cada {{u}}?",
      capacidad_semanal: "En una semana normal, ¿cuántas veces puedes atender? Cuenta cada {{u}} como una vez.",
      costos_fijos_mensuales: "¿Tienes costos fijos mensuales (renta, herramientas, etc.)? Si sí, ¿cuánto suman al mes?",
    },
    digital: {
      costos_fijos_mensuales:
        "¿Cuánto gastas al mes en costos fijos de infraestructura (hosting, APIs, herramientas, suscripciones)?",
      costo_materiales_unidad:
        "¿Tienes algún costo variable por cada {{u}} (por ejemplo, costo de API por uso)? Si es prácticamente cero, responde 0.",
      precio_tentativo: "¿A qué precio o ingreso promedio vendes (o venderías) cada {{u}}?",
      unidades_vendidas: "Contando por {{u}}, ¿cuánto tienes hoy, o cuál sería una meta mensual realista?",
    },
    productoFisico: {
      costo_materiales_unidad: "¿Cuánto gastas en materiales por {{u}}, más o menos? Un número aproximado sirve.",
      horas_por_unidad: "¿Cuántas horas de trabajo te toma cada {{u}}, de principio a fin?",
      valor_hora: "¿En cuánto valoras tu hora de trabajo (lo que sientes que deberías ganar por hora)?",
      precio_tentativo: "¿A qué precio venderías (o vendes) cada {{u}}?",
      capacidad_semanal: "En una semana normal, ¿cuánto puedes producir, contando por {{u}}?",
      costos_fijos_mensuales: "¿Tienes costos fijos mensuales (renta, herramientas, etc.)? Si sí, ¿cuánto suman al mes?",
    },
  },
  tusNumerosHoy: "## Tus números hoy",
  gigo: {
    algoNoCuadra: "Antes de calcular nada, encontré algo que no cuadra en estos números:",
    noVoyACalcular:
      "No voy a calcular margen ni punto de equilibrio con estos datos: el resultado sería una cifra que suena precisa pero está mal, y eso es peor que no tener el cálculo. Prefiero decírtelo con honestidad.",
    losNumerosQueDiste: "## Los números que diste",
    losQueTeFaltanComo: "## Los números que te faltan (y cómo conseguirlos)",
    revisa:
      "Revisa si alguno de los números de arriba está en una unidad distinta a la que esperaba el reporte (por ejemplo, un gasto mensual anotado como costo por unidad, o un plazo en meses anotado como horas), corrígelo, y vuelve a generar el reporte con la cifra corregida.",
  },
  offline: {
    costo: "- Costo por unidad: {{valor}}",
    margen: "- Margen por unidad: {{valor}} ({{porcentaje}}%)",
    equilibrio: "- Punto de equilibrio: {{valor}} unidades/mes",
    techo: "- Techo de ingreso mensual: {{ingreso}} ({{unidades}} unidades/mes)",
    losQueTeFaltan: "## Los números que te faltan",
  },
};

const en: typeof es = {
  /** la unidad de venta cuando el usuario no dio ninguna (va dentro de las preguntas) */
  unidadPorOmision: "unit",
  preguntas: {
    servicio: {
      costo_materiales_unidad:
        "How much does each {{u}} cost you directly (supplies, materials you use, etc.)? A rough number is fine; if you don't have one, answer 0.",
      horas_por_unidad: "How many hours of work does each {{u}} take you?",
      valor_hora: "How much is an hour of your work worth to you (what you feel you should earn per hour)?",
      precio_tentativo: "What price do you charge (or would you charge) for each {{u}}?",
      capacidad_semanal: "In a normal week, how many can you take on, counting each {{u}}?",
      costos_fijos_mensuales: "Do you have monthly fixed costs (rent, tools, etc.)? If so, how much do they add up to per month?",
    },
    digital: {
      costos_fijos_mensuales:
        "How much do you spend each month on fixed infrastructure costs (hosting, APIs, tools, subscriptions)?",
      costo_materiales_unidad:
        "Do you have any variable cost for each {{u}} (for example, API cost per use)? If it's practically zero, answer 0.",
      precio_tentativo: "At what price or average revenue do you sell (or would you sell) each {{u}}?",
      unidades_vendidas: "How many do you have today, counting each {{u}}, or what would be a realistic monthly goal?",
    },
    productoFisico: {
      costo_materiales_unidad: "Roughly how much do you spend on materials for each {{u}}? A rough number is fine.",
      horas_por_unidad: "How many hours of work does each {{u}} take you, from start to finish?",
      valor_hora: "How much is an hour of your work worth to you (what you feel you should earn per hour)?",
      precio_tentativo: "What price would you sell (or do you sell) each {{u}} for?",
      capacidad_semanal: "In a normal week, how many can you make, counting each {{u}}?",
      costos_fijos_mensuales: "Do you have monthly fixed costs (rent, tools, etc.)? If so, how much do they add up to per month?",
    },
  },
  tusNumerosHoy: "## Your numbers today",
  gigo: {
    algoNoCuadra: "Before calculating anything, I found something in these numbers that doesn't add up:",
    noVoyACalcular:
      "I'm not going to calculate margin or break-even point with these numbers: the result would be a figure that sounds precise but is wrong, and that's worse than having no calculation at all. I'd rather tell you honestly.",
    losNumerosQueDiste: "## The numbers you gave",
    losQueTeFaltanComo: "## The numbers you're missing (and how to get them)",
    revisa:
      "Check whether any of the numbers above is in a different unit than the report expected (for example, a monthly expense entered as a cost per unit, or a timeframe in months entered as hours), correct it, and generate the report again with the corrected figure.",
  },
  offline: {
    costo: "- Cost per unit: {{valor}}",
    margen: "- Margin per unit: {{valor}} ({{porcentaje}}%)",
    equilibrio: "- Break-even point: {{valor}} units/month",
    techo: "- Monthly revenue ceiling: {{ingreso}} ({{unidades}} units/month)",
    losQueTeFaltan: "## The numbers you're missing",
  },
};

const fr: typeof es = {
  unidadPorOmision: "unité",
  preguntas: {
    servicio: {
      costo_materiales_unidad: "Combien te coûte directement chaque {{u}} (fournitures, matériel utilisé, etc.)? Un chiffre approximatif suffit; si tu n'en as pas, réponds 0.",
      horas_por_unidad: "Combien d'heures de travail te prend chaque {{u}}?",
      valor_hora: "Combien vaut une heure de ton travail (ce que tu estimes devoir gagner à l'heure)?",
      precio_tentativo: "À quel prix factures-tu (ou facturerais-tu) chaque {{u}}?",
      capacidad_semanal: "Dans une semaine normale, quelle quantité peux-tu prendre en charge (à compter par {{u}})?",
      costos_fijos_mensuales: "As-tu des coûts fixes mensuels (loyer, outils, etc.)? Si oui, combien font-ils par mois?",
    },
    digital: {
      costos_fijos_mensuales: "Combien dépenses-tu par mois en coûts fixes d'infrastructure (hébergement, API, outils, abonnements)?",
      costo_materiales_unidad: "As-tu un coût variable pour chaque {{u}} (par exemple, un coût d'API à l'utilisation)? S'il est pratiquement nul, réponds 0.",
      precio_tentativo: "À quel prix, ou pour quel revenu moyen, vends-tu (ou vendrais-tu) chaque {{u}}?",
      unidades_vendidas: "Combien d'unités as-tu aujourd'hui (à compter par {{u}}), ou quel serait un objectif mensuel réaliste?",
    },
    productoFisico: {
      costo_materiales_unidad: "Combien dépenses-tu en matériaux pour chaque {{u}}, à peu près? Un chiffre approximatif suffit.",
      horas_por_unidad: "Combien d'heures de travail te prend chaque {{u}}, du début à la fin?",
      valor_hora: "Combien vaut une heure de ton travail (ce que tu estimes devoir gagner à l'heure)?",
      precio_tentativo: "À quel prix vendrais-tu (ou vends-tu) chaque {{u}}?",
      capacidad_semanal: "Dans une semaine normale, quelle quantité peux-tu produire (à compter par {{u}})?",
      costos_fijos_mensuales: "As-tu des coûts fixes mensuels (loyer, outils, etc.)? Si oui, combien font-ils par mois?",
    },
  },
  tusNumerosHoy: "## Tes chiffres aujourd'hui",
  gigo: {
    algoNoCuadra: "Avant de calculer quoi que ce soit, j'ai trouvé quelque chose qui ne colle pas dans ces chiffres :",
    noVoyACalcular: "Je ne vais pas calculer de marge ni de seuil de rentabilité avec ces données : le résultat serait un chiffre qui a l'air précis mais qui est faux, et c'est pire que de ne pas avoir de calcul du tout. Je préfère te le dire honnêtement.",
    losNumerosQueDiste: "## Les chiffres que tu as donnés",
    losQueTeFaltanComo: "## Les chiffres qui te manquent (et comment les obtenir)",
    revisa: "Vérifie si l'un des chiffres ci-dessus est dans une autre unité que celle attendue par le rapport (par exemple, une dépense mensuelle inscrite comme coût par unité, ou un délai en mois inscrit en heures), corrige-le et génère de nouveau le rapport avec le chiffre corrigé.",
  },
  offline: {
    costo: "- Coût par unité : {{valor}}",
    margen: "- Marge par unité : {{valor}} ({{porcentaje}} %)",
    equilibrio: "- Seuil de rentabilité : {{valor}} unités/mois",
    techo: "- Plafond de revenu mensuel : {{ingreso}} ({{unidades}} unités/mois)",
    losQueTeFaltan: "## Les chiffres qui te manquent",
  },
};

const pt: typeof es = {
  unidadPorOmision: "unidade",
  preguntas: {
    servicio: {
      costo_materiales_unidad: "Quanto custa diretamente para você cada {{u}} (insumos, materiais que usa etc.)? Um número aproximado serve; se não tiver, responda 0.",
      horas_por_unidad: "Quantas horas de trabalho você leva em cada {{u}}?",
      valor_hora: "Quanto vale sua hora de trabalho para você (o que sente que deveria ganhar por hora)?",
      precio_tentativo: "Por qual preço você cobra (ou cobraria) cada {{u}}?",
      capacidad_semanal: "Em uma semana normal, quantas vezes você consegue atender, contando cada {{u}}?",
      costos_fijos_mensuales: "Você tem custos fixos mensais (aluguel, ferramentas etc.)? Se tiver, quanto eles somam por mês?",
    },
    digital: {
      costos_fijos_mensuales: "Quanto você gasta por mês com custos fixos de infraestrutura (hospedagem, APIs, ferramentas, assinaturas)?",
      costo_materiales_unidad: "Você tem algum custo variável por cada {{u}} (por exemplo, custo de API por uso)? Se for praticamente zero, responda 0.",
      precio_tentativo: "Por qual preço ou receita média você vende (ou venderia) cada {{u}}?",
      unidades_vendidas: "Quantas você tem hoje, contando cada {{u}}, ou qual seria uma meta mensal realista?",
    },
    productoFisico: {
      costo_materiales_unidad: "Quanto você gasta em materiais por {{u}}, mais ou menos? Um número aproximado serve.",
      horas_por_unidad: "Quantas horas de trabalho você leva em cada {{u}}, do início ao fim?",
      valor_hora: "Quanto vale sua hora de trabalho para você (o que sente que deveria ganhar por hora)?",
      precio_tentativo: "Por qual preço você venderia (ou vende) cada {{u}}?",
      capacidad_semanal: "Em uma semana normal, quantas você consegue produzir, contando cada {{u}}?",
      costos_fijos_mensuales: "Você tem custos fixos mensais (aluguel, ferramentas etc.)? Se tiver, quanto eles somam por mês?",
    },
  },
  tusNumerosHoy: "## Seus números hoje",
  gigo: {
    algoNoCuadra: "Antes de calcular qualquer coisa, encontrei algo que não fecha nestes números:",
    noVoyACalcular: "Não vou calcular margem nem ponto de equilíbrio com estes dados: o resultado seria um número que parece preciso, mas está errado, e isso é pior do que não ter o cálculo. Prefiro ser honesto com você.",
    losNumerosQueDiste: "## Os números que você informou",
    losQueTeFaltanComo: "## Os números que faltam (e como consegui-los)",
    revisa: "Verifique se algum dos números acima está em uma unidade diferente da que o relatório esperava (por exemplo, um gasto mensal anotado como custo por unidade, ou um prazo em meses anotado como horas), corrija e gere o relatório de novo com o número corrigido.",
  },
  offline: {
    costo: "- Custo por unidade: {{valor}}",
    margen: "- Margem por unidade: {{valor}} ({{porcentaje}}%)",
    equilibrio: "- Ponto de equilíbrio: {{valor}} unidades/mês",
    techo: "- Teto de receita mensal: {{ingreso}} ({{unidades}} unidades/mês)",
    losQueTeFaltan: "## Os números que faltam",
  },
};

const de: typeof es = {
  unidadPorOmision: "Einheit",
  preguntas: {
    servicio: {
      costo_materiales_unidad: "Wie hoch sind deine direkten Kosten pro {{u}} (Verbrauchsmaterial, Material, das du einsetzt, usw.)? Eine ungefähre Zahl reicht; wenn du keine hast, antworte 0.",
      horas_por_unidad: "Wie viele Arbeitsstunden brauchst du pro {{u}}?",
      valor_hora: "Wie viel ist dir eine Stunde deiner Arbeit wert (was du deiner Meinung nach pro Stunde verdienen solltest)?",
      precio_tentativo: "Welchen Preis verlangst du (oder würdest du verlangen) pro {{u}}?",
      capacidad_semanal: "Wie viele kannst du in einer normalen Woche übernehmen (gezählt pro {{u}})?",
      costos_fijos_mensuales: "Hast du monatliche Fixkosten (Miete, Werkzeuge usw.)? Wenn ja, wie viel kommt im Monat zusammen?",
    },
    digital: {
      costos_fijos_mensuales: "Wie viel gibst du im Monat für feste Infrastrukturkosten aus (Hosting, APIs, Werkzeuge, Abos)?",
      costo_materiales_unidad: "Hast du variable Kosten pro {{u}} (zum Beispiel API-Kosten pro Nutzung)? Wenn sie praktisch null sind, antworte 0.",
      precio_tentativo: "Welchen Preis oder durchschnittlichen Erlös erzielst du (oder würdest du erzielen) pro {{u}}?",
      unidades_vendidas: "Wie viele hast du heute (gezählt pro {{u}}), oder was wäre ein realistisches Monatsziel?",
    },
    productoFisico: {
      costo_materiales_unidad: "Wie viel gibst du ungefähr für Material pro {{u}} aus? Eine ungefähre Zahl reicht.",
      horas_por_unidad: "Wie viele Arbeitsstunden brauchst du pro {{u}}, von Anfang bis Ende?",
      valor_hora: "Wie viel ist dir eine Stunde deiner Arbeit wert (was du deiner Meinung nach pro Stunde verdienen solltest)?",
      precio_tentativo: "Welchen Preis würdest du pro {{u}} verlangen (oder verlangst du schon)?",
      capacidad_semanal: "Wie viele kannst du in einer normalen Woche herstellen (gezählt pro {{u}})?",
      costos_fijos_mensuales: "Hast du monatliche Fixkosten (Miete, Werkzeuge usw.)? Wenn ja, wie viel kommt im Monat zusammen?",
    },
  },
  tusNumerosHoy: "## Deine Zahlen heute",
  gigo: {
    algoNoCuadra: "Bevor ich irgendetwas berechne: Mir ist in diesen Zahlen etwas aufgefallen, das nicht zusammenpasst:",
    noVoyACalcular: "Mit diesen Daten berechne ich weder Marge noch Gewinnschwelle: Das Ergebnis wäre eine Zahl, die genau klingt, aber falsch ist, und das ist schlimmer, als gar keine Berechnung zu haben. Ich sage es dir lieber ehrlich.",
    losNumerosQueDiste: "## Die Zahlen, die du angegeben hast",
    losQueTeFaltanComo: "## Die Zahlen, die dir fehlen (und wie du sie bekommst)",
    revisa: "Prüf, ob eine der Zahlen oben in einer anderen Einheit steht, als der Bericht erwartet hat (zum Beispiel eine monatliche Ausgabe, die als Kosten pro Einheit eingetragen ist, oder ein Zeitraum in Monaten, der als Stunden eingetragen ist), korrigiere sie und erstelle den Bericht mit der korrigierten Zahl neu.",
  },
  offline: {
    costo: "- Kosten pro Einheit: {{valor}}",
    margen: "- Marge pro Einheit: {{valor}} ({{porcentaje}} %)",
    equilibrio: "- Gewinnschwelle: {{valor}} Einheiten/Monat",
    techo: "- Monatliche Umsatzobergrenze: {{ingreso}} ({{unidades}} Einheiten/Monat)",
    losQueTeFaltan: "## Die Zahlen, die dir fehlen",
  },
};

const it: typeof es = {
  unidadPorOmision: "unità",
  preguntas: {
    servicio: {
      costo_materiales_unidad: "Quanto ti costa direttamente ogni {{u}} (forniture, materiali che usi, ecc.)? Basta un numero approssimativo; se non ne hai, rispondi 0.",
      horas_por_unidad: "Quante ore di lavoro ti richiede ogni {{u}}?",
      valor_hora: "Quanto vale per te un'ora del tuo lavoro (quello che senti di dover guadagnare all'ora)?",
      precio_tentativo: "A che prezzo fai pagare (o faresti pagare) ogni {{u}}?",
      capacidad_semanal: "In una settimana normale, quante volte riesci a offrire il tuo servizio? Conta ogni {{u}} come una volta.",
      costos_fijos_mensuales: "Hai costi fissi mensili (affitto, strumenti, ecc.)? Se sì, a quanto ammontano al mese?",
    },
    digital: {
      costos_fijos_mensuales: "Quanto spendi al mese in costi fissi di infrastruttura (hosting, API, strumenti, abbonamenti)?",
      costo_materiales_unidad: "Hai qualche costo variabile per ogni {{u}} (per esempio, il costo delle API per utilizzo)? Se è praticamente zero, rispondi 0.",
      precio_tentativo: "A che prezzo, o con che ricavo medio, vendi (o venderesti) ogni {{u}}?",
      unidades_vendidas: "Contando ogni {{u}}, a quanto arrivi oggi? Oppure, quale sarebbe un obiettivo mensile realistico?",
    },
    productoFisico: {
      costo_materiales_unidad: "Quanto spendi in materiali per ogni {{u}}, più o meno? Basta un numero approssimativo.",
      horas_por_unidad: "Quante ore di lavoro ti richiede ogni {{u}}, dall'inizio alla fine?",
      valor_hora: "Quanto vale per te un'ora del tuo lavoro (quello che senti di dover guadagnare all'ora)?",
      precio_tentativo: "A che prezzo venderesti (o vendi) ogni {{u}}?",
      capacidad_semanal: "In una settimana normale, quante unità riesci a produrre? Conta ogni {{u}} come una.",
      costos_fijos_mensuales: "Hai costi fissi mensili (affitto, strumenti, ecc.)? Se sì, a quanto ammontano al mese?",
    },
  },
  tusNumerosHoy: "## I tuoi numeri oggi",
  gigo: {
    algoNoCuadra: "Prima di calcolare qualsiasi cosa, ho trovato qualcosa che non torna in questi numeri:",
    noVoyACalcular: "Non calcolerò margine né punto di pareggio con questi dati: il risultato sarebbe una cifra che sembra precisa ma è sbagliata, ed è peggio che non avere il calcolo. Preferisco dirtelo con onestà.",
    losNumerosQueDiste: "## I numeri che hai dato",
    losQueTeFaltanComo: "## I numeri che ti mancano (e come ottenerli)",
    revisa: "Controlla se qualcuno dei numeri qui sopra è in un'unità diversa da quella che si aspettava il resoconto (per esempio, una spesa mensile inserita come costo per unità, o una durata in mesi inserita come ore), correggilo e genera di nuovo il resoconto con la cifra corretta.",
  },
  offline: {
    costo: "- Costo per unità: {{valor}}",
    margen: "- Margine per unità: {{valor}} ({{porcentaje}}%)",
    equilibrio: "- Punto di pareggio: {{valor}} unità/mese",
    techo: "- Tetto di ricavi mensili: {{ingreso}} ({{unidades}} unità/mese)",
    losQueTeFaltan: "## I numeri che ti mancano",
  },
};

const ja: typeof es = {
  unidadPorOmision: "個",
  preguntas: {
    servicio: {
      costo_materiales_unidad: "1{{u}}あたり、直接かかる費用はいくらですか（消耗品、使う材料など）？おおよその数字で大丈夫です。なければ0と答えてください。",
      horas_por_unidad: "1{{u}}あたり、何時間の作業がかかりますか？",
      valor_hora: "ご自身の1時間の仕事に、どれくらいの価値をつけますか（1時間あたりこれくらいは稼ぐべきだと感じる金額）？",
      precio_tentativo: "1{{u}}あたり、いくらで請求していますか（または、請求するつもりですか）？",
      capacidad_semanal: "普段の1週間で、何{{u}}くらい対応できますか？",
      costos_fijos_mensuales: "毎月の固定費（家賃、ツールなど）はありますか？あれば、月にいくらになりますか？",
    },
    digital: {
      costos_fijos_mensuales: "インフラの固定費（ホスティング、API、ツール、サブスクリプション）に、毎月いくら使っていますか？",
      costo_materiales_unidad: "1{{u}}あたりにかかる変動費はありますか（たとえば、利用ごとのAPI費用）？ほぼゼロなら0と答えてください。",
      precio_tentativo: "1{{u}}あたり、いくらの価格または平均収入で販売していますか（または、販売するつもりですか）？",
      unidades_vendidas: "今、何{{u}}くらいありますか？または、現実的な月間目標はどれくらいですか？",
    },
    productoFisico: {
      costo_materiales_unidad: "1{{u}}あたり、材料費はおおよそいくらかかりますか？おおよその数字で大丈夫です。",
      horas_por_unidad: "1{{u}}あたり、始めから終わりまで何時間の作業がかかりますか？",
      valor_hora: "ご自身の1時間の仕事に、どれくらいの価値をつけますか（1時間あたりこれくらいは稼ぐべきだと感じる金額）？",
      precio_tentativo: "1{{u}}あたり、いくらで販売しますか（または、販売していますか）？",
      capacidad_semanal: "普段の1週間で、何{{u}}くらい作れますか？",
      costos_fijos_mensuales: "毎月の固定費（家賃、ツールなど）はありますか？あれば、月にいくらになりますか？",
    },
  },
  tusNumerosHoy: "## 今のあなたの数字",
  gigo: {
    algoNoCuadra: "計算する前に、この数字の中に辻褄の合わないところを見つけました：",
    noVoyACalcular: "このデータでは、利益も損益分岐点も計算しません。正確そうに見えて実は間違っている数字になってしまい、それは計算がないよりも悪いからです。正直にお伝えしたいと思います。",
    losNumerosQueDiste: "## 入力した数字",
    losQueTeFaltanComo: "## 足りない数字（と、その集め方）",
    revisa: "上の数字のどれかが、レポートの想定と違う単位になっていないか確認してください（たとえば、月々の支出を1個あたりのコストとして入れている、月単位の期間を時間として入れている、など）。見つけたら修正して、正しい数字でレポートをもう一度作成してください。",
  },
  offline: {
    costo: "- 1個あたりのコスト：{{valor}}",
    margen: "- 1個あたりの利益：{{valor}}（{{porcentaje}}%）",
    equilibrio: "- 損益分岐点：{{valor}}個/月",
    techo: "- 月間売上の上限：{{ingreso}}（{{unidades}}個/月）",
    losQueTeFaltan: "## 足りない数字",
  },
};

const zh: typeof es = {
  unidadPorOmision: "单位",
  preguntas: {
    servicio: {
      costo_materiales_unidad: "每{{u}}直接花你多少钱（耗材、用到的材料等）？给个大概数字就行；如果没有，就回答0。",
      horas_por_unidad: "每{{u}}要花你多少小时的工作？",
      valor_hora: "你觉得自己一小时的工作值多少钱（你认为每小时应该赚多少）？",
      precio_tentativo: "每{{u}}你收（或打算收）多少钱？",
      capacidad_semanal: "在正常的一周里，你能接待多少（按{{u}}计）？",
      costos_fijos_mensuales: "你每月有固定成本吗（房租、工具等）？如果有，每月一共多少？",
    },
    digital: {
      costos_fijos_mensuales: "你每月在基础设施的固定成本上花多少钱（服务器托管、API、工具、订阅）？",
      costo_materiales_unidad: "每{{u}}有没有变动成本（比如按使用量计的API费用）？如果几乎为零，就回答0。",
      precio_tentativo: "每{{u}}你卖（或打算卖）多少钱，或者平均收入是多少？",
      unidades_vendidas: "你现在有多少（按{{u}}计），或者一个现实的月度目标是多少？",
    },
    productoFisico: {
      costo_materiales_unidad: "每{{u}}你大概要花多少材料费？给个大概数字就行。",
      horas_por_unidad: "每{{u}}从头到尾要花你多少小时的工作？",
      valor_hora: "你觉得自己一小时的工作值多少钱（你认为每小时应该赚多少）？",
      precio_tentativo: "每{{u}}你会卖（或现在卖）多少钱？",
      capacidad_semanal: "在正常的一周里，你能生产多少（按{{u}}计）？",
      costos_fijos_mensuales: "你每月有固定成本吗（房租、工具等）？如果有，每月一共多少？",
    },
  },
  tusNumerosHoy: "## 你今天的数字",
  gigo: {
    algoNoCuadra: "在计算之前，我发现这些数字里有地方对不上：",
    noVoyACalcular: "我不会用这些数据计算利润或盈亏平衡点：算出来的数字听起来很精确，其实是错的，这比没有计算更糟。我宁愿老实告诉你。",
    losNumerosQueDiste: "## 你提供的数字",
    losQueTeFaltanComo: "## 你还缺的数字（以及怎么得到它们）",
    revisa: "检查一下上面的数字里，有没有哪个用的单位和报告预期的不一样（比如把每月的开支填成了每单位的成本，或把以月计的期限填成了小时），改正它，再用改好的数字重新生成报告。",
  },
  offline: {
    costo: "- 每单位成本：{{valor}}",
    margen: "- 每单位利润：{{valor}}（{{porcentaje}}%）",
    equilibrio: "- 盈亏平衡点：{{valor}}单位/月",
    techo: "- 月收入上限：{{ingreso}}（{{unidades}}单位/月）",
    losQueTeFaltan: "## 你还缺的数字",
  },
};

const ko: typeof es = {
  unidadPorOmision: "개",
  preguntas: {
    servicio: {
      costo_materiales_unidad: "{{u}}당 직접 드는 비용은 얼마인가요(소모품, 사용하는 재료 등)? 대략적인 숫자면 충분해요. 없다면 0이라고 답해 주세요.",
      horas_por_unidad: "{{u}}당 작업 시간이 몇 시간 걸리나요?",
      valor_hora: "내 작업 1시간의 가치를 얼마로 보나요(시간당 이 정도는 벌어야 한다고 느끼는 금액)?",
      precio_tentativo: "{{u}}당 얼마를 받나요(또는 받을 건가요)?",
      capacidad_semanal: "평범한 한 주에 맡을 수 있는 {{u}} 수는 얼마인가요?",
      costos_fijos_mensuales: "매달 나가는 고정비(임대료, 도구 등)가 있나요? 있다면 한 달에 모두 얼마인가요?",
    },
    digital: {
      costos_fijos_mensuales: "인프라 고정비(호스팅, API, 도구, 구독)로 한 달에 얼마를 쓰나요?",
      costo_materiales_unidad: "{{u}}당 드는 변동비가 있나요(예: 사용량에 따른 API 비용)? 거의 0이라면 0이라고 답해 주세요.",
      precio_tentativo: "{{u}}당 가격이나 평균 수입은 얼마인가요(또는 얼마로 팔 건가요)?",
      unidades_vendidas: "지금 {{u}} 수는 얼마인가요? 아니면 현실적인 월 목표는 얼마인가요?",
    },
    productoFisico: {
      costo_materiales_unidad: "{{u}}당 재료비가 대략 얼마나 드나요? 대략적인 숫자면 충분해요.",
      horas_por_unidad: "{{u}}당 처음부터 끝까지 작업 시간이 몇 시간 걸리나요?",
      valor_hora: "내 작업 1시간의 가치를 얼마로 보나요(시간당 이 정도는 벌어야 한다고 느끼는 금액)?",
      precio_tentativo: "{{u}}당 얼마에 팔 건가요(또는 팔고 있나요)?",
      capacidad_semanal: "평범한 한 주에 만들 수 있는 {{u}} 수는 얼마인가요?",
      costos_fijos_mensuales: "매달 나가는 고정비(임대료, 도구 등)가 있나요? 있다면 한 달에 모두 얼마인가요?",
    },
  },
  tusNumerosHoy: "## 지금 나의 숫자",
  gigo: {
    algoNoCuadra: "계산하기 전에, 이 숫자들에서 맞지 않는 부분을 발견했어요:",
    noVoyACalcular: "이 데이터로는 마진도 손익분기점도 계산하지 않을게요. 정확해 보이지만 틀린 숫자가 나올 텐데, 그건 계산이 없는 것보다 더 나빠요. 솔직하게 말씀드리는 편이 나아요.",
    losNumerosQueDiste: "## 입력한 숫자",
    losQueTeFaltanComo: "## 아직 없는 숫자(와 구하는 방법)",
    revisa: "위 숫자 중에 리포트가 예상한 것과 다른 단위로 적힌 게 있는지 확인해 주세요(예: 월 지출을 단위당 비용으로 적었거나, 개월 단위 기간을 시간으로 적은 경우). 고친 뒤 수정한 수치로 리포트를 다시 만들어 주세요.",
  },
  offline: {
    costo: "- 단위당 비용: {{valor}}",
    margen: "- 단위당 마진: {{valor}}({{porcentaje}}%)",
    equilibrio: "- 손익분기점: 월 {{valor}}개",
    techo: "- 월 수입 상한: {{ingreso}}(월 {{unidades}}개)",
    losQueTeFaltan: "## 아직 없는 숫자",
  },
};

const ar: typeof es = {
  unidadPorOmision: "وحدة",
  preguntas: {
    servicio: {
      costo_materiales_unidad: "كم تكلّفكم كل {{u}} بشكل مباشر (المستلزمات، والمواد التي تستخدمونها، إلخ)؟ يكفي رقم تقريبي؛ وإن لم يكن لديكم، فأجيبوا 0.",
      horas_por_unidad: "كم ساعة عمل تستغرق منكم كل {{u}}؟",
      valor_hora: "كم تقدّرون قيمة ساعة عملكم (ما تشعرون أنكم يجب أن تكسبوه في الساعة)؟",
      precio_tentativo: "بأي سعر تتقاضون (أو ستتقاضون) مقابل كل {{u}}؟",
      capacidad_semanal: "كم {{u}} تستطيعون تقديمها في أسبوع عادي؟",
      costos_fijos_mensuales: "هل لديكم تكاليف ثابتة شهرية (الإيجار، والأدوات، إلخ)؟ إن كان الجواب نعم، فكم مجموعها في الشهر؟",
    },
    digital: {
      costos_fijos_mensuales: "كم تنفقون شهريًا على التكاليف الثابتة للبنية التحتية (الاستضافة، وواجهات API، والأدوات، والاشتراكات)؟",
      costo_materiales_unidad: "هل لديكم تكلفة متغيرة عن كل {{u}} (مثل تكلفة API لكل استخدام)؟ إن كانت شبه معدومة، فأجيبوا 0.",
      precio_tentativo: "بأي سعر أو بأي متوسط إيراد تبيعون (أو ستبيعون) كل {{u}}؟",
      unidades_vendidas: "كم {{u}} لديكم اليوم، أو ما الهدف الشهري الواقعي؟",
    },
    productoFisico: {
      costo_materiales_unidad: "كم تنفقون تقريبًا على المواد لكل {{u}}؟ يكفي رقم تقريبي.",
      horas_por_unidad: "كم ساعة عمل تستغرق منكم كل {{u}}، من البداية إلى النهاية؟",
      valor_hora: "كم تقدّرون قيمة ساعة عملكم (ما تشعرون أنكم يجب أن تكسبوه في الساعة)؟",
      precio_tentativo: "بأي سعر ستبيعون (أو تبيعون) كل {{u}}؟",
      capacidad_semanal: "كم {{u}} تستطيعون إنتاجها في أسبوع عادي؟",
      costos_fijos_mensuales: "هل لديكم تكاليف ثابتة شهرية (الإيجار، والأدوات، إلخ)؟ إن كان الجواب نعم، فكم مجموعها في الشهر؟",
    },
  },
  tusNumerosHoy: "## أرقامكم اليوم",
  gigo: {
    algoNoCuadra: "قبل أن أحسب أي شيء، وجدت في هذه الأرقام ما لا يستقيم:",
    noVoyACalcular: "لن أحسب هامش الربح ولا نقطة التعادل بهذه البيانات: فالنتيجة ستكون رقمًا يبدو دقيقًا لكنه خاطئ، وهذا أسوأ من عدم وجود الحساب أصلًا. أفضّل أن أصارحكم بذلك.",
    losNumerosQueDiste: "## الأرقام التي قدّمتموها",
    losQueTeFaltanComo: "## الأرقام التي تنقصكم (وكيف تحصلون عليها)",
    revisa: "تحقّقوا مما إذا كان أحد الأرقام أعلاه بوحدة غير التي توقّعها التقرير (مثلًا، مصروف شهري سُجّل كتكلفة للوحدة، أو مدة بالأشهر سُجّلت كساعات)، وصحّحوه، ثم أعيدوا إنشاء التقرير بالرقم المصحَّح.",
  },
  offline: {
    costo: "- التكلفة للوحدة: {{valor}}",
    margen: "- هامش الربح للوحدة: {{valor}} ({{porcentaje}}%)",
    equilibrio: "- نقطة التعادل (وحدات في الشهر): {{valor}}",
    techo: "- سقف الإيراد الشهري: {{ingreso}} (وحدات في الشهر: {{unidades}})",
    losQueTeFaltan: "## الأرقام التي تنقصكم",
  },
};

const hi: typeof es = {
  unidadPorOmision: "यूनिट",
  preguntas: {
    servicio: {
      costo_materiales_unidad: "हर {{u}} पर आपका सीधा खर्च कितना आता है (सामग्री, इस्तेमाल होने वाला सामान, वगैरह)? मोटा-मोटा अंदाज़ा भी चलेगा; अगर कोई खर्च नहीं है, तो 0 लिखें।",
      horas_por_unidad: "हर {{u}} में आपके काम के कितने घंटे लगते हैं?",
      valor_hora: "आपके काम के एक घंटे की कीमत कितनी है (आपको लगता है कि आपको प्रति घंटा कितना कमाना चाहिए)?",
      precio_tentativo: "हर {{u}} के लिए आपकी कीमत कितनी है (या कितनी होगी)?",
      capacidad_semanal: "एक सामान्य हफ़्ते में कितनी बार {{u}} संभाला जा सकता है?",
      costos_fijos_mensuales: "क्या हर महीने आपकी कुछ स्थिर लागतें हैं (किराया, औज़ार, वगैरह)? अगर हाँ, तो महीने में कुल कितनी होती हैं?",
    },
    digital: {
      costos_fijos_mensuales: "इंफ्रास्ट्रक्चर की स्थिर लागतों (होस्टिंग, API, टूल्स, सब्सक्रिप्शन) पर हर महीने आपका कितना खर्च होता है?",
      costo_materiales_unidad: "क्या हर {{u}} पर आपकी कोई बदलती लागत है (जैसे, हर इस्तेमाल पर API का खर्च)? अगर यह लगभग शून्य है, तो 0 लिखें।",
      precio_tentativo: "हर {{u}} की कीमत या औसत कमाई कितनी है (या कितनी होगी)?",
      unidades_vendidas: "आज आपके पास कितने {{u}} हैं, या हर महीने के लिए कौन-सा लक्ष्य व्यावहारिक होगा?",
    },
    productoFisico: {
      costo_materiales_unidad: "हर {{u}} की सामग्री पर लगभग कितना खर्च आता है? मोटा-मोटा अंदाज़ा भी चलेगा।",
      horas_por_unidad: "हर {{u}} को शुरू से आख़िर तक बनाने में आपके काम के कितने घंटे लगते हैं?",
      valor_hora: "आपके काम के एक घंटे की कीमत कितनी है (आपको लगता है कि आपको प्रति घंटा कितना कमाना चाहिए)?",
      precio_tentativo: "हर {{u}} की बिक्री कीमत कितनी होगी (या अभी कितनी है)?",
      capacidad_semanal: "एक सामान्य हफ़्ते में कितने {{u}} बन सकते हैं?",
      costos_fijos_mensuales: "क्या हर महीने आपकी कुछ स्थिर लागतें हैं (किराया, औज़ार, वगैरह)? अगर हाँ, तो महीने में कुल कितनी होती हैं?",
    },
  },
  tusNumerosHoy: "## आज आपके आंकड़े",
  gigo: {
    algoNoCuadra: "कुछ भी गणना करने से पहले, मुझे इन संख्याओं में कुछ ऐसा मिला जो मेल नहीं खाता:",
    noVoyACalcular: "इन आंकड़ों से मार्जिन या ब्रेक-ईवन बिंदु की गणना नहीं की जाएगी: नतीजा एक ऐसी संख्या होती जो सटीक लगती पर गलत होती, और यह कोई गणना न होने से भी बुरा है। इसलिए आपको ईमानदारी से बताना बेहतर है।",
    losNumerosQueDiste: "## आपके दिए हुए आंकड़े",
    losQueTeFaltanComo: "## जो आंकड़े अभी बाकी हैं (और उन्हें कैसे जुटाएँ)",
    revisa: "देखें कि ऊपर की कोई संख्या उस इकाई से अलग इकाई में तो नहीं है जिसकी रिपोर्ट को उम्मीद थी (जैसे, हर महीने का कोई खर्च जिसे प्रति यूनिट लागत के रूप में लिखा गया हो, या महीनों की कोई अवधि जिसे घंटों के रूप में लिखा गया हो)। उसे सुधारें, और सुधारी हुई संख्या के साथ रिपोर्ट फिर से बनाएँ।",
  },
  offline: {
    costo: "- प्रति यूनिट लागत: {{valor}}",
    margen: "- प्रति यूनिट मार्जिन: {{valor}} ({{porcentaje}}%)",
    equilibrio: "- ब्रेक-ईवन बिंदु: {{valor}} यूनिट/महीना",
    techo: "- हर महीने की अधिकतम कमाई: {{ingreso}} ({{unidades}} यूनिट/महीना)",
    losQueTeFaltan: "## जो आंकड़े अभी बाकी हैं",
  },
};

export const REPORTE: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
