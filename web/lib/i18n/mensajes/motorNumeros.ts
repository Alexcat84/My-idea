/** Los textos que arman para la pantalla los módulos deterministas de Tus Números:
 * calculadora.ts (notas y guardián GIGO), palancas.ts, tableroNumeros.ts y numerosVivo.ts. */
import type { PorIdioma } from "../config";

const es = {
  calculadora: {
    equilibrioSinMargenRango:
      "el margen por unidad no es positivo en todo el rango; no hay punto de equilibrio posible así",
    equilibrioSinMargen: "el margen por unidad no es positivo; no hay punto de equilibrio posible con estos números",
    gigoMargen:
      "con estos números el margen por unidad es {{pct}}%, muy por debajo de -100%: lo más probable es que alguna cifra esté en la unidad equivocada (por ejemplo, un presupuesto mensual leído como costo por unidad, o un plazo en meses leído como horas), no que cada venta pierda esa cantidad de dinero",
    gigoPrecio:
      "el precio declarado es menos del 5% del costo unitario calculado: revisa si el precio y el costo están expresados en la misma unidad (por pieza, por mes, etc.)",
  },
  palancas: {
    volumenBloqueado:
      "Con el margen en rojo, el volumen agranda la pérdida. Primero arregla el margen; cuando esté en verde, aquí va cuántas unidades al mes necesitas para tu meta.",
  },
  escenarios: {
    sinFijos: "falta tu gasto fijo del mes",
    pesimista: "Pesimista",
    tuRitmo: "Tu ritmo de hoy",
    capacidadPlena: "A capacidad plena",
    alMes: "{{n}} al mes",
    /** Las filas de adopción (producto digital), por su nivel (el nivel es el DATO). */
    adopcion: {
      "50%": "mitad de tu meta",
      "100%": "tu meta",
      "200%": "el doble",
    },
  },
  vivo: {
    topeRenarracion:
      "Por hoy llegamos al límite de relecturas. Tus números y tus cambios quedan guardados, el recálculo sigue disponible sin límite, y mañana puedes pedir una relectura nueva.",
    cicloPositivo: "Tu dinero tarda unos {{d}} días en volver a tu bolsillo desde que pagas los materiales.",
    cicloCero: "Tu dinero vuelve el mismo día: cobras justo cuando pagas.",
    cicloNegativo: "Cobras antes de pagar: tu caja trabaja a favor, con unos {{d}} días de holgura.",
    unidadPorDefecto: "unidad",
    datos:
      "Aún me faltan cifras para darte el panorama: cuando completes lo que falta, aquí verás con claridad si cada {{u}} te deja ganancia.",
    perdidaAcento: "{{monto}} más de lo que cobras",
    perdida:
      "Hoy, cada {{u}} que vendes te cuesta {{acento}}: no es problema de vender más, es que el precio todavía no cubre lo que te cuesta hacerla.",
    ajusteAcento: "{{monto}} por {{u}}",
    ajustePct: " ({{pct}}%)",
    ajuste:
      "Cada {{u}} te deja {{acento}}{{pct}}: ya es ganancia, pero un margen delgado, así que conviene reforzarlo antes de crecer.",
    sanoAcento: "{{monto}} limpios",
    sanoCola:
      ", y con vender {{equilibrio}} al mes ya cubres tus {{fijos}} de gasto fijo: de ahí en adelante, cada {{u}} es ganancia",
    sano: "Cada {{u}} te deja {{acento}}{{cola}}.",
  },
};

const en: typeof es = {
  calculadora: {
    equilibrioSinMargenRango:
      "the margin per unit isn't positive across the whole range; there's no possible break-even point like this",
    equilibrioSinMargen: "the margin per unit isn't positive; there's no possible break-even point with these numbers",
    gigoMargen:
      "with these numbers the margin per unit is {{pct}}%, far below -100%: most likely some figure is in the wrong unit (for example, a monthly budget read as a cost per unit, or a timeframe in months read as hours), not that each sale loses that much money",
    gigoPrecio:
      "the price you entered is less than 5% of the calculated unit cost: check that the price and the cost are in the same unit (per piece, per month, etc.)",
  },
  palancas: {
    volumenBloqueado:
      "With your margin in the red, more volume only makes the loss bigger. Fix the margin first; once it's in the green, this is where you'll see how many units a month you need for your goal.",
  },
  escenarios: {
    sinFijos: "your monthly fixed costs are missing",
    pesimista: "Pessimistic",
    tuRitmo: "Your current pace",
    capacidadPlena: "At full capacity",
    alMes: "{{n}} a month",
    adopcion: {
      "50%": "half your goal",
      "100%": "your goal",
      "200%": "double your goal",
    },
  },
  vivo: {
    topeRenarracion:
      "That's the limit for fresh readings today. Your numbers and your changes are saved, recalculating is still unlimited, and tomorrow you can ask for a new reading.",
    cicloPositivo: "Your money takes about {{d}} days to come back to your pocket from the moment you pay for materials.",
    cicloCero: "Your money comes back the same day: you get paid right when you pay.",
    cicloNegativo: "You get paid before you pay: your cash works in your favor, with about {{d}} days of breathing room.",
    unidadPorDefecto: "unit",
    datos:
      "I'm still missing some figures to give you the full picture: once you fill in what's missing, you'll see clearly here whether each {{u}} leaves you a profit.",
    perdidaAcento: "{{monto}} more than you charge",
    perdida:
      "Right now, each {{u}} you sell costs you {{acento}}: the problem isn't selling more, it's that your price doesn't yet cover what it costs you to make it.",
    ajusteAcento: "{{monto}} per {{u}}",
    ajustePct: " ({{pct}}%)",
    ajuste:
      "Each {{u}} leaves you {{acento}}{{pct}}: that's already profit, but a thin margin, so it's worth strengthening before you grow.",
    sanoAcento: "{{monto}} clear",
    sanoCola:
      ", and selling {{equilibrio}} a month already covers your {{fijos}} in fixed costs: from there on, every {{u}} is profit",
    sano: "Each {{u}} leaves you {{acento}}{{cola}}.",
  },
};

const fr: typeof es = {
  calculadora: {
    equilibrioSinMargenRango: "la marge par unité n'est pas positive sur toute la plage; aucun seuil de rentabilité n'est possible ainsi",
    equilibrioSinMargen: "la marge par unité n'est pas positive; aucun seuil de rentabilité n'est possible avec ces chiffres",
    gigoMargen: "avec ces chiffres, la marge par unité est de {{pct}} %, bien en dessous de -100 % : le plus probable, c'est qu'un chiffre soit dans la mauvaise unité (par exemple, un budget mensuel lu comme un coût par unité, ou un délai en mois lu comme des heures), et non que chaque vente fasse perdre autant d'argent",
    gigoPrecio: "le prix indiqué est inférieur à 5 % du coût unitaire calculé : vérifie si le prix et le coût sont exprimés dans la même unité (par pièce, par mois, etc.)",
  },
  palancas: {
    volumenBloqueado: "Avec la marge dans le rouge, le volume ne fait que grossir la perte. Corrige d'abord la marge; quand elle sera dans le vert, tu verras ici combien d'unités par mois il te faut pour atteindre ton objectif.",
  },
  escenarios: {
    sinFijos: "il manque tes coûts fixes du mois",
    pesimista: "Pessimiste",
    tuRitmo: "Ton rythme actuel",
    capacidadPlena: "À pleine capacité",
    alMes: "{{n}} par mois",
    adopcion: {
      "50%": "la moitié de ton objectif",
      "100%": "ton objectif",
      "200%": "le double",
    },
  },
  vivo: {
    topeRenarracion: "Pour aujourd'hui, on a atteint la limite de nouvelles lectures. Tes chiffres et tes changements sont enregistrés, le recalcul reste disponible sans limite, et demain tu pourras demander une nouvelle lecture.",
    cicloPositivo: "Ton argent met environ {{d}} jours à revenir dans tes poches à partir du moment où tu paies les matériaux.",
    cicloCero: "Ton argent revient le jour même : tu encaisses au moment où tu paies.",
    cicloNegativo: "Tu encaisses avant de payer : ta trésorerie travaille pour toi, avec environ {{d}} jours d'avance.",
    unidadPorDefecto: "unité",
    datos: "Il me manque encore des chiffres pour te donner une vue d'ensemble : quand tu auras complété ce qui manque, tu verras clairement ici si chaque {{u}} te laisse un profit.",
    perdidaAcento: "{{monto}} de plus que ton prix",
    perdida: "Aujourd'hui, chaque {{u}} que tu vends te coûte {{acento}} : le problème n'est pas de vendre plus, c'est que ton prix ne couvre pas encore ce qu'il t'en coûte pour produire.",
    ajusteAcento: "{{monto}} par {{u}}",
    ajustePct: " ({{pct}} %)",
    ajuste: "Chaque {{u}} te laisse {{acento}}{{pct}} : c'est déjà du profit, mais une marge mince, alors mieux vaut la renforcer avant de grandir.",
    sanoAcento: "{{monto}} net",
    sanoCola: ", et en vendant {{equilibrio}} par mois, tu couvres déjà tes {{fijos}} de coûts fixes : à partir de là, chaque {{u}} est du profit",
    sano: "Chaque {{u}} te laisse {{acento}}{{cola}}.",
  },
};

const pt: typeof es = {
  calculadora: {
    equilibrioSinMargenRango: "a margem por unidade não é positiva em toda a faixa; assim não há ponto de equilíbrio possível",
    equilibrioSinMargen: "a margem por unidade não é positiva; não há ponto de equilíbrio possível com estes números",
    gigoMargen: "com estes números a margem por unidade é {{pct}}%, muito abaixo de -100%: o mais provável é que algum valor esteja na unidade errada (por exemplo, um orçamento mensal lido como custo por unidade, ou um prazo em meses lido como horas), e não que cada venda perca essa quantia de dinheiro",
    gigoPrecio: "o preço informado é menos de 5% do custo unitário calculado: confira se o preço e o custo estão na mesma unidade (por peça, por mês etc.)",
  },
  palancas: {
    volumenBloqueado: "Com a margem no vermelho, o volume aumenta o prejuízo. Primeiro acerte a margem; quando ela estiver no verde, aqui aparece quantas unidades por mês você precisa para chegar à sua meta.",
  },
  escenarios: {
    sinFijos: "falta o seu gasto fixo do mês",
    pesimista: "Pessimista",
    tuRitmo: "Seu ritmo de hoje",
    capacidadPlena: "Com capacidade total",
    alMes: "{{n}} por mês",
    adopcion: {
      "50%": "metade da sua meta",
      "100%": "sua meta",
      "200%": "o dobro",
    },
  },
  vivo: {
    topeRenarracion: "Por hoje chegamos ao limite de releituras. Seus números e suas alterações ficam salvos, o recálculo continua disponível sem limite e amanhã você pode pedir uma nova releitura.",
    cicloPositivo: "Seu dinheiro leva uns {{d}} dias para voltar ao seu bolso desde que você paga os materiais.",
    cicloCero: "Seu dinheiro volta no mesmo dia: você recebe exatamente quando paga.",
    cicloNegativo: "Você recebe antes de pagar: seu caixa trabalha a seu favor, com uns {{d}} dias de folga.",
    unidadPorDefecto: "unidade",
    datos: "Ainda faltam valores para eu te dar o panorama: quando você completar o que falta, vai ver aqui com clareza se cada {{u}} dá lucro.",
    perdidaAcento: "{{monto}} a mais do que você cobra",
    perdida: "Hoje, cada {{u}} que você vende te custa {{acento}}: o problema não é vender mais, é que o preço ainda não cobre o que você gasta para produzir.",
    ajusteAcento: "{{monto}} por {{u}}",
    ajustePct: " ({{pct}}%)",
    ajuste: "Cada {{u}} rende {{acento}}{{pct}}: já é lucro, mas com margem apertada, então vale reforçá-la antes de crescer.",
    sanoAcento: "{{monto}} líquidos",
    sanoCola: ", e vendendo {{equilibrio}} por mês você já cobre seus {{fijos}} de gasto fixo: daí em diante, cada {{u}} é lucro",
    sano: "Cada {{u}} rende {{acento}}{{cola}}.",
  },
};

const de: typeof es = {
  calculadora: {
    equilibrioSinMargenRango: "die Marge pro Einheit ist nicht im ganzen Bereich positiv; so ist keine Gewinnschwelle möglich",
    equilibrioSinMargen: "die Marge pro Einheit ist nicht positiv; mit diesen Zahlen ist keine Gewinnschwelle möglich",
    gigoMargen: "mit diesen Zahlen liegt die Marge pro Einheit bei {{pct}} %, weit unter -100 %: Höchstwahrscheinlich steht eine Zahl in der falschen Einheit (zum Beispiel ein Monatsbudget, das als Kosten pro Einheit gelesen wurde, oder eine Frist in Monaten, die als Stunden gelesen wurde), und nicht jeder Verkauf verliert wirklich so viel Geld",
    gigoPrecio: "der angegebene Preis liegt unter 5 % der berechneten Stückkosten: Prüf, ob Preis und Kosten in derselben Einheit angegeben sind (pro Stück, pro Monat usw.)",
  },
  palancas: {
    volumenBloqueado: "Solange die Marge im Minus ist, vergrößert mehr Menge nur den Verlust. Bring zuerst die Marge in Ordnung; sobald sie im Plus ist, siehst du hier, wie viele Einheiten du im Monat für dein Ziel brauchst.",
  },
  escenarios: {
    sinFijos: "deine monatlichen Fixkosten fehlen",
    pesimista: "Pessimistisch",
    tuRitmo: "Dein heutiges Tempo",
    capacidadPlena: "Bei voller Auslastung",
    alMes: "{{n}} im Monat",
    adopcion: {
      "50%": "die Hälfte deines Ziels",
      "100%": "dein Ziel",
      "200%": "das Doppelte",
    },
  },
  vivo: {
    topeRenarracion: "Für heute ist die Grenze für neue Einschätzungen erreicht. Deine Zahlen und Änderungen sind gespeichert, neu berechnen kannst du weiterhin ohne Limit, und morgen kannst du wieder eine neue Einschätzung anfordern.",
    cicloPositivo: "Ab dem Moment, in dem du das Material bezahlst, dauert es etwa {{d}} Tage, bis dein Geld wieder in deiner Tasche ist.",
    cicloCero: "Dein Geld kommt am selben Tag zurück: Du kassierst genau dann, wenn du bezahlst.",
    cicloNegativo: "Du kassierst, bevor du bezahlst: Deine Kasse arbeitet für dich, mit etwa {{d}} Tagen Luft.",
    unidadPorDefecto: "Stück",
    datos: "Mir fehlen noch ein paar Zahlen für das Gesamtbild: Sobald du den Rest ergänzt, siehst du hier klar, ob dir pro {{u}} ein Gewinn bleibt.",
    perdidaAcento: "{{monto}} mehr, als du dafür bekommst",
    perdida: "Im Moment kostet dich die Herstellung pro {{u}} {{acento}}: Mehr zu verkaufen löst das nicht, dein Preis deckt einfach noch nicht deine Kosten.",
    ajusteAcento: "{{monto}} pro {{u}}",
    ajustePct: " ({{pct}} %)",
    ajuste: "Bei jedem Verkauf bleiben dir {{acento}}{{pct}}: Das ist schon Gewinn, aber eine dünne Marge pro {{u}}. Stärke sie lieber, bevor du wächst.",
    sanoAcento: "{{monto}} übrig",
    sanoCola: ", und mit {{equilibrio}} Verkäufen im Monat deckst du schon deine {{fijos}} Fixkosten: Ab da ist die Marge pro {{u}} reiner Gewinn",
    sano: "Pro {{u}} bleiben dir {{acento}}{{cola}}.",
  },
};

const it: typeof es = {
  calculadora: {
    equilibrioSinMargenRango: "il margine per unità non è positivo in tutto l'intervallo; così non esiste un punto di pareggio possibile",
    equilibrioSinMargen: "il margine per unità non è positivo; con questi numeri non esiste un punto di pareggio possibile",
    gigoMargen: "con questi numeri il margine per unità è {{pct}}%, molto al di sotto di -100%: con ogni probabilità qualche cifra è nell'unità sbagliata (per esempio, un budget mensile letto come costo per unità, o una durata in mesi letta come ore), non che ogni vendita perda davvero tutti quei soldi",
    gigoPrecio: "il prezzo indicato è meno del 5% del costo unitario calcolato: controlla che prezzo e costo siano espressi nella stessa unità (al pezzo, al mese, ecc.)",
  },
  palancas: {
    volumenBloqueado: "Con il margine in rosso, più volume ingrandisce solo la perdita. Prima sistema il margine; quando sarà in verde, qui vedrai quante unità al mese ti servono per il tuo obiettivo.",
  },
  escenarios: {
    sinFijos: "mancano i tuoi costi fissi mensili",
    pesimista: "Pessimista",
    tuRitmo: "Il tuo ritmo di oggi",
    capacidadPlena: "A piena capacità",
    alMes: "{{n}} al mese",
    adopcion: {
      "50%": "metà del tuo obiettivo",
      "100%": "il tuo obiettivo",
      "200%": "il doppio",
    },
  },
  vivo: {
    topeRenarracion: "Per oggi abbiamo raggiunto il limite di riletture. I tuoi numeri e le tue modifiche restano salvati, il ricalcolo resta disponibile senza limiti, e domani potrai chiedere una nuova rilettura.",
    cicloPositivo: "I tuoi soldi impiegano circa {{d}} giorni a tornarti in tasca da quando paghi i materiali.",
    cicloCero: "I tuoi soldi tornano lo stesso giorno: incassi proprio quando paghi.",
    cicloNegativo: "Incassi prima di pagare: la tua cassa lavora a tuo favore, con circa {{d}} giorni di respiro.",
    unidadPorDefecto: "unità",
    datos: "Mi mancano ancora alcune cifre per darti il quadro completo: quando avrai inserito quelle che mancano, qui vedrai chiaramente se ogni {{u}} ti lascia un guadagno.",
    perdidaAcento: "{{monto}} in più di quanto incassi",
    perdida: "Oggi ogni {{u}} che vendi ti costa {{acento}}: il problema non è vendere di più, è che il prezzo non copre ancora quello che ti costa produrla.",
    ajusteAcento: "{{monto}} per {{u}}",
    ajustePct: " ({{pct}}%)",
    ajuste: "Ogni {{u}} ti lascia {{acento}}{{pct}}: è già un guadagno, ma il margine è sottile, quindi conviene rafforzarlo prima di crescere.",
    sanoAcento: "{{monto}} netti",
    sanoCola: ", e vendendone {{equilibrio}} al mese copri già i tuoi {{fijos}} di costi fissi: da lì in poi, ogni {{u}} è guadagno",
    sano: "Ogni {{u}} ti lascia {{acento}}{{cola}}.",
  },
};

const ja: typeof es = {
  calculadora: {
    equilibrioSinMargenRango: "範囲全体で1個あたりの利益がプラスになっていないため、このままでは損益分岐点を出せません",
    equilibrioSinMargen: "1個あたりの利益がプラスになっていないため、この数字では損益分岐点を出せません",
    gigoMargen: "この数字だと1個あたりの利益は{{pct}}%で、-100%を大きく下回っています。売るたびにそれだけ損をしているというより、どこかの数字の単位が違っている可能性が高いです（たとえば、月の予算を1個あたりのコストとして読んでいる、月単位の期間を時間として読んでいる、など）",
    gigoPrecio: "入力された価格が、計算した1個あたりのコストの5%未満です。価格とコストが同じ単位（1個あたり、1か月あたりなど）になっているか確認してください",
  },
  palancas: {
    volumenBloqueado: "利益がマイナスのうちは、売る量を増やすほど損失が大きくなります。まずは利益を立て直しましょう。プラスになったら、目標に必要な月の販売数をここでお見せします。",
  },
  escenarios: {
    sinFijos: "月の固定費が未入力です",
    pesimista: "悲観的",
    tuRitmo: "今のペース",
    capacidadPlena: "フル稼働",
    alMes: "月{{n}}",
    adopcion: {
      "50%": "目標の半分",
      "100%": "目標どおり",
      "200%": "目標の2倍",
    },
  },
  vivo: {
    topeRenarracion: "今日の読み解きは上限に達しました。数字と変更内容は保存されていて、再計算は引き続き無制限です。明日になれば、新しい読み解きを頼めます。",
    cicloPositivo: "材料費を支払ってから、そのお金が手元に戻るまで約{{d}}日かかります。",
    cicloCero: "お金はその日のうちに戻ります。支払うのと同じタイミングで入金があるからです。",
    cicloNegativo: "支払いより先に入金があるので、資金繰りが味方してくれます。約{{d}}日の余裕があります。",
    unidadPorDefecto: "個",
    datos: "全体像をお伝えするには、まだいくつか数字が足りません。足りない分を入力すると、1{{u}}ごとに利益が出ているかどうかが、ここではっきりわかります。",
    perdidaAcento: "売値より{{monto}}多い",
    perdida: "今は、1{{u}}売るたびに{{acento}}費用がかかっています。売る数の問題ではなく、価格がまだ作るのにかかる費用をまかなえていないのです。",
    ajusteAcento: "1{{u}}あたり{{monto}}",
    ajustePct: "（{{pct}}%）",
    ajuste: "{{acento}}{{pct}}が手元に残ります。すでに利益は出ていますが幅が薄いので、事業を広げる前に1{{u}}あたりの利益を厚くしておきましょう。",
    sanoAcento: "{{monto}}の利益",
    sanoCola: "。月の販売数が{{equilibrio}}に届けば{{fijos}}の固定費をまかなえ、そこから先は1{{u}}売るたびに利益が積み上がります",
    sano: "1{{u}}ごとに{{acento}}が残ります{{cola}}。",
  },
};

const zh: typeof es = {
  calculadora: {
    equilibrioSinMargenRango: "在整个区间内，每件利润都不是正数；这样不可能达到盈亏平衡点",
    equilibrioSinMargen: "每件利润不是正数；按这些数字不可能达到盈亏平衡点",
    gigoMargen: "按这些数字，每件利润率为{{pct}}%，远低于-100%：最可能的情况是某个数字的单位填错了（比如把月度预算当成了单件成本，或把以月计的周期当成了小时），而不是每卖一件都会亏这么多钱",
    gigoPrecio: "填写的价格还不到计算出的单件成本的5%：请检查价格和成本是否用的是同一个单位（按件、按月等）",
  },
  palancas: {
    volumenBloqueado: "利润为负时，卖得越多，亏得越多。先把利润调好；等它转为正数，这里会告诉你每月要卖多少件才能达到目标。",
  },
  escenarios: {
    sinFijos: "缺少你每月的固定成本",
    pesimista: "悲观",
    tuRitmo: "按你目前的节奏",
    capacidadPlena: "满负荷",
    alMes: "每月{{n}}",
    adopcion: {
      "50%": "目标的一半",
      "100%": "你的目标",
      "200%": "目标的两倍",
    },
  },
  vivo: {
    topeRenarracion: "今天的重新解读次数已经用完。你的数字和修改都已保存，重新计算依然不限次数，明天你可以再要一次新的解读。",
    cicloPositivo: "从你支付材料费算起，大约{{d}}天后，钱才会回到你的口袋。",
    cicloCero: "你的钱当天就能回来：收款和付款在同一天。",
    cicloNegativo: "你先收款、后付款：现金流对你有利，大约有{{d}}天的余地。",
    unidadPorDefecto: "件",
    datos: "我还缺一些数字，没法给你完整的全貌：等你补齐缺少的部分，就能在这里清楚看到每{{u}}能不能给你带来利润。",
    perdidaAcento: "比售价高出{{monto}}",
    perdida: "目前，你每卖出一{{u}}，成本都{{acento}}：问题不在于卖得不够多，而在于价格还不够覆盖做它的成本。",
    ajusteAcento: "每{{u}}赚{{monto}}",
    ajustePct: "（{{pct}}%）",
    ajuste: "你卖出的每一{{u}}都在盈利：{{acento}}{{pct}}。不过利润偏薄，扩大规模之前，最好先把它做厚一些。",
    sanoAcento: "净赚{{monto}}",
    sanoCola: "，而且每月销量只要达到{{equilibrio}}，就能覆盖你{{fijos}}的固定成本：从那以后，每多卖一{{u}}都是利润",
    sano: "每{{u}}{{acento}}{{cola}}。",
  },
};

const ko: typeof es = {
  calculadora: {
    equilibrioSinMargenRango: "범위 전체에서 단위당 마진이 양수가 아니에요. 이대로는 손익분기점이 나올 수 없어요",
    equilibrioSinMargen: "단위당 마진이 양수가 아니에요. 이 숫자로는 손익분기점이 나올 수 없어요",
    gigoMargen: "이 숫자로 계산하면 단위당 마진이 {{pct}}%로, -100%보다 훨씬 낮아요. 판매할 때마다 정말 그만큼 손해를 본다기보다는, 어떤 수치가 잘못된 단위로 들어갔을 가능성이 커요(예를 들어 월 예산을 단위당 비용으로, 개월 단위 기간을 시간으로 읽은 경우)",
    gigoPrecio: "입력한 가격이 계산된 단위당 원가의 5%도 안 돼요. 가격과 비용이 같은 단위(개당, 월당 등)로 적혀 있는지 확인해 주세요",
  },
  palancas: {
    volumenBloqueado: "마진이 적자인 상태에서는 판매량이 늘수록 손실도 커져요. 먼저 마진을 바로잡아 주세요. 흑자가 되면 목표에 필요한 월 판매량을 여기서 보여 드릴게요.",
  },
  escenarios: {
    sinFijos: "월 고정비가 빠져 있어요",
    pesimista: "비관적",
    tuRitmo: "지금 속도",
    capacidadPlena: "최대 생산량일 때",
    alMes: "월 {{n}}",
    adopcion: {
      "50%": "목표의 절반",
      "100%": "목표치",
      "200%": "목표의 두 배",
    },
  },
  vivo: {
    topeRenarracion: "오늘 새 해설을 받을 수 있는 한도에 도달했어요. 숫자와 변경 사항은 저장돼 있고, 재계산은 계속 무제한으로 할 수 있어요. 내일 다시 새 해설을 요청할 수 있어요.",
    cicloPositivo: "재료비를 낸 뒤 돈이 다시 주머니로 돌아오기까지 약 {{d}}일이 걸려요.",
    cicloCero: "돈이 같은 날 돌아와요. 돈을 내는 바로 그때 대금을 받아요.",
    cicloNegativo: "돈을 내기 전에 먼저 받아요. 현금 흐름이 유리하게 돌아가고, 약 {{d}}일의 여유가 있어요.",
    unidadPorDefecto: "개",
    datos: "전체 그림을 보여 드리기엔 아직 수치가 부족해요. 빠진 부분을 채우면 {{u}}당 이익이 남는지 여기서 한눈에 볼 수 있어요.",
    perdidaAcento: "받는 가격보다 {{monto}} 더",
    perdida: "지금은 팔 때마다 {{u}}당 {{acento}} 들어요. 더 많이 파는 게 문제가 아니라, 가격이 아직 만드는 데 드는 비용을 감당하지 못하는 거예요.",
    ajusteAcento: "{{u}}당 {{monto}}",
    ajustePct: " ({{pct}}%)",
    ajuste: "지금은 {{acento}}{{pct}} 남아요. 이미 이익이지만 마진이 얇으니, 사업을 키우기 전에 {{u}}당 남는 몫부터 늘려 두는 게 좋아요.",
    sanoAcento: "순수하게 {{monto}}",
    sanoCola: ". 한 달에 {{equilibrio}}개만 팔아도 고정비({{fijos}})를 모두 감당할 수 있고, 그다음부터는 {{u}}당 마진이 고스란히 이익이에요",
    sano: "{{u}}당 {{acento}} 남아요{{cola}}.",
  },
};

const ar: typeof es = {
  calculadora: {
    equilibrioSinMargenRango: "هامش الربح لكل وحدة ليس موجبًا في النطاق كله؛ لا توجد نقطة تعادل ممكنة على هذا النحو",
    equilibrioSinMargen: "هامش الربح لكل وحدة ليس موجبًا؛ لا توجد نقطة تعادل ممكنة بهذه الأرقام",
    gigoMargen: "بهذه الأرقام يبلغ هامش الربح لكل وحدة {{pct}}%، أي أدنى بكثير من -100%: الأرجح أن رقمًا ما مُدخل بوحدة خاطئة (مثلًا ميزانية شهرية قُرئت كتكلفة للوحدة، أو مدة بالأشهر قُرئت كساعات)، لا أن كل عملية بيع تخسر هذا القدر من المال",
    gigoPrecio: "السعر المُعلَن أقل من 5% من تكلفة الوحدة المحسوبة: تحقّقوا من أن السعر والتكلفة محسوبان بالوحدة نفسها (للقطعة، للشهر، إلخ)",
  },
  palancas: {
    volumenBloqueado: "ما دام هامش الربح في الأحمر، فزيادة حجم المبيعات تكبّر الخسارة. أصلحوا هامش الربح أولًا؛ وحين يصبح في الأخضر، سترون هنا كم وحدة تحتاجونها شهريًا لبلوغ هدفكم.",
  },
  escenarios: {
    sinFijos: "تنقص تكاليفكم الثابتة الشهرية",
    pesimista: "متشائم",
    tuRitmo: "وتيرتكم اليوم",
    capacidadPlena: "بالطاقة الكاملة",
    alMes: "{{n}} في الشهر",
    adopcion: {
      "50%": "نصف هدفكم",
      "100%": "هدفكم",
      "200%": "ضعف هدفكم",
    },
  },
  vivo: {
    topeRenarracion: "بلغنا لهذا اليوم حدّ القراءات الجديدة. أرقامكم وتغييراتكم محفوظة، وإعادة الحساب ما زالت متاحة بلا حدود، وغدًا يمكنكم طلب قراءة جديدة.",
    cicloPositivo: "عدد الأيام التي يحتاجها مالكم ليعود إلى جيبكم منذ أن تدفعوا ثمن المواد: نحو {{d}}.",
    cicloCero: "يعود مالكم في اليوم نفسه: تقبضون في اللحظة التي تدفعون فيها.",
    cicloNegativo: "تقبضون قبل أن تدفعوا: سيولتكم تعمل لصالحكم، والهامش بالأيام نحو {{d}}.",
    unidadPorDefecto: "وحدة",
    datos: "ما زالت تنقصني أرقام لأرسم لكم الصورة كاملة: حين تكملون الناقص، سترون هنا بوضوح إن كنتم تربحون من كل {{u}}.",
    perdidaAcento: "{{monto}} أكثر مما تتقاضونه",
    perdida: "اليوم، بيع كل {{u}} يكلّفكم {{acento}}: المشكلة ليست في أن تبيعوا أكثر، بل في أن السعر لا يغطي بعدُ تكلفة الصنع.",
    ajusteAcento: "{{monto}} لكل {{u}}",
    ajustePct: " ({{pct}}%)",
    ajuste: "يبقى لكم من كل {{u}} {{acento}}{{pct}}: هذا ربح بالفعل، لكنه هامش رفيع، لذا يحسن تقويته قبل أن تكبروا.",
    sanoAcento: "{{monto}} صافيًا",
    sanoCola: "، وببيع {{equilibrio}} في الشهر تغطّون بالفعل تكاليفكم الثابتة ({{fijos}}): ومن بعدها، كل {{u}} ربح خالص",
    sano: "يبقى لكم من كل {{u}} {{acento}}{{cola}}.",
  },
};

const hi: typeof es = {
  calculadora: {
    equilibrioSinMargenRango: "पूरी रेंज में प्रति यूनिट मार्जिन शून्य से ऊपर नहीं है; ऐसे में ब्रेक-ईवन बिंदु मुमकिन नहीं",
    equilibrioSinMargen: "प्रति यूनिट मार्जिन शून्य से ऊपर नहीं है; इन आंकड़ों के साथ ब्रेक-ईवन बिंदु मुमकिन नहीं",
    gigoMargen: "इन आंकड़ों के साथ प्रति यूनिट मार्जिन {{pct}}% है, जो -100% से बहुत नीचे है: सबसे ज़्यादा संभावना यह है कि कोई आंकड़ा गलत इकाई में है (जैसे, महीने का बजट प्रति यूनिट लागत की तरह पढ़ा गया, या महीनों में दी गई अवधि घंटों की तरह पढ़ी गई), न कि हर बिक्री में इतना पैसा डूब रहा है",
    gigoPrecio: "बताई गई कीमत गणना की गई प्रति यूनिट लागत के 5% से भी कम है: देखें कि कीमत और लागत एक ही इकाई में हैं या नहीं (प्रति नग, प्रति महीना, आदि)",
  },
  palancas: {
    volumenBloqueado: "मार्जिन लाल निशान में हो, तो ज़्यादा बिक्री घाटे को और बड़ा करती है। पहले मार्जिन ठीक करें; जब वह हरे निशान में आ जाए, तो यहाँ दिखेगा कि अपने लक्ष्य के लिए आपको हर महीने कितनी यूनिट चाहिए।",
  },
  escenarios: {
    sinFijos: "आपकी महीने की स्थिर लागत अभी नहीं भरी गई",
    pesimista: "निराशावादी",
    tuRitmo: "आपकी आज की गति",
    capacidadPlena: "पूरी क्षमता पर",
    alMes: "हर महीने {{n}}",
    adopcion: {
      "50%": "आपके लक्ष्य का आधा",
      "100%": "आपका लक्ष्य",
      "200%": "लक्ष्य का दोगुना",
    },
  },
  vivo: {
    topeRenarracion: "आज के लिए नई व्याख्याओं की सीमा पूरी हो गई। आपके आंकड़े और बदलाव सहेजे हुए हैं, दोबारा गणना बिना किसी सीमा के चालू है, और कल फिर नई व्याख्या माँगी जा सकती है।",
    cicloPositivo: "सामान का भुगतान करने से लेकर पैसा वापस आपकी जेब में आने तक करीब {{d}} दिन लगते हैं।",
    cicloCero: "आपका पैसा उसी दिन लौट आता है: जिस दिन भुगतान करना होता है, उसी दिन आपको पैसे मिल जाते हैं।",
    cicloNegativo: "आपको भुगतान करने से पहले ही पैसे मिल जाते हैं: आपकी नकदी आपके पक्ष में काम करती है, करीब {{d}} दिन की गुंजाइश के साथ।",
    unidadPorDefecto: "यूनिट",
    datos: "पूरी तस्वीर दिखाने के लिए मुझे अभी कुछ आंकड़े और चाहिए: बाकी जानकारी भरते ही यहाँ साफ़ दिखेगा कि हर {{u}} से आपको मुनाफ़ा होता है या नहीं।",
    perdidaAcento: "आपकी कीमत से {{monto}} ज़्यादा",
    perdida: "आज हर {{u}} पर आपकी लागत {{acento}} बैठती है: समस्या कम बिक्री की नहीं है, बात यह है कि आपकी कीमत अभी उसे बनाने का खर्च भी पूरा नहीं करती।",
    ajusteAcento: "{{monto}} प्रति {{u}}",
    ajustePct: " ({{pct}}%)",
    ajuste: "आपका मार्जिन {{acento}}{{pct}} है: हर {{u}} पर मुनाफ़ा तो है, पर पतला है, इसलिए बढ़ने से पहले इसे मज़बूत करना बेहतर है।",
    sanoAcento: "{{monto}} का साफ़ मुनाफ़ा",
    sanoCola: ", और हर महीने {{equilibrio}} बेचते ही आपकी {{fijos}} की स्थिर लागत निकल आती है: उसके बाद हर {{u}} मुनाफ़ा ही है",
    sano: "हर {{u}} पर आपको {{acento}} मिलता है{{cola}}।",
  },
};

export const MOTOR_NUMEROS: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
