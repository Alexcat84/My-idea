/**
 * El nombre y la promesa de cada mundo, por idioma (i18n F3; glosario en
 * DISENO §6). La fuente del español es web/lib/assets/packs_catalog.json: este
 * `es` es su COPIA y lib/catalogoMundos.test.ts falla si se separan. Las claves
 * son la `clave` de cada pack (el dominio): no se traducen.
 */
import type { PorIdioma } from "../config";

const es = {
  quality: { nombre: "Calidad y Confianza", promesa: "Que tu cliente confíe, vuelva y te recomiende." },
  health_safety: { nombre: "Seguridad y Personas", promesa: "Protege a tu gente y a tu negocio de su peor día." },
  environmental: { nombre: "Ambiente y Futuro", promesa: "Convierte lo sostenible en ventaja que se nota y se cobra." },
  seguridad_digital: { nombre: "Seguridad Digital", promesa: "Blinda tus datos, tus cuentas y la confianza de tus clientes." },
  exportacion: { nombre: "Vender al Mundo", promesa: "Lleva tu producto a clientes de otros países, con método." },
  franquicias: { nombre: "Multiplica tu Negocio", promesa: "Convierte tu negocio probado en muchos que funcionan igual." },
  risk_management: { nombre: "Riesgos Bajo Control", promesa: "Ve venir lo que puede fallar, y decide antes de que decida por ti." },
  compras: { nombre: "Tu Compra Correcta", promesa: "Compra lo que toca, al que toca, al precio que toca." },
  entrega: { nombre: "Del Taller a sus Manos", promesa: "Que llegue entero, a tiempo y sin sorpresas de costo." },
};

const en: typeof es = {
  quality: { nombre: "Quality & Trust", promesa: "Get your customers to trust you, come back and recommend you." },
  health_safety: { nombre: "Safety & People", promesa: "Protect your people and your business from their worst day." },
  environmental: { nombre: "Environment & Future", promesa: "Turn sustainability into an edge people notice and pay for." },
  seguridad_digital: { nombre: "Digital Security", promesa: "Lock down your data, your accounts and your customers' trust." },
  exportacion: { nombre: "Sell to the World", promesa: "Take your product to customers in other countries, with a method." },
  franquicias: { nombre: "Multiply Your Business", promesa: "Turn your proven business into many that work the same way." },
  risk_management: { nombre: "Risks Under Control", promesa: "See what could go wrong before it happens, and decide before it decides for you." },
  compras: { nombre: "The Right Purchase", promesa: "Buy the right thing, from the right supplier, at the right price." },
  entrega: { nombre: "From Workshop to Customer", promesa: "Make sure it arrives intact, on time and with no cost surprises." },
};

const fr: typeof es = {
  quality: {
    nombre: "Qualité et confiance",
    promesa: "Que ton client te fasse confiance, revienne et te recommande.",
  },
  health_safety: {
    nombre: "Sécurité et personnes",
    promesa: "Protège les tiens et ton entreprise de leur pire journée.",
  },
  environmental: {
    nombre: "Environnement et avenir",
    promesa: "Fais du durable un avantage qui se voit et qui se paie.",
  },
  seguridad_digital: {
    nombre: "Sécurité numérique",
    promesa: "Blinde tes données, tes comptes et la confiance de tes clients.",
  },
  exportacion: {
    nombre: "Vendre au monde",
    promesa: "Porte ton produit jusqu'aux clients d'autres pays, avec méthode.",
  },
  franquicias: {
    nombre: "Multiplie ton entreprise",
    promesa: "Transforme ton entreprise qui a fait ses preuves en plusieurs qui fonctionnent de la même façon.",
  },
  risk_management: {
    nombre: "Risques sous contrôle",
    promesa: "Vois venir ce qui peut mal tourner, et décide avant que ça décide pour toi.",
  },
  compras: {
    nombre: "Ton bon achat",
    promesa: "Achète ce qu'il faut, à qui il faut, au prix qu'il faut.",
  },
  entrega: {
    nombre: "De l'atelier à leurs mains",
    promesa: "Que ça arrive intact, à temps et sans mauvaise surprise sur les coûts.",
  },
};

const pt: typeof es = {
  quality: {
    nombre: "Qualidade e Confiança",
    promesa: "Que seu cliente confie, volte e recomende você.",
  },
  health_safety: {
    nombre: "Segurança e Pessoas",
    promesa: "Proteja sua gente e seu negócio do pior dia.",
  },
  environmental: {
    nombre: "Ambiente e Futuro",
    promesa: "Transforme a sustentabilidade em vantagem que se nota e se cobra.",
  },
  seguridad_digital: {
    nombre: "Segurança Digital",
    promesa: "Blinde seus dados, suas contas e a confiança dos seus clientes.",
  },
  exportacion: {
    nombre: "Vender para o Mundo",
    promesa: "Leve seu produto a clientes de outros países, com método.",
  },
  franquicias: {
    nombre: "Multiplique seu Negócio",
    promesa: "Transforme seu negócio comprovado em muitos que funcionam igual.",
  },
  risk_management: {
    nombre: "Riscos sob Controle",
    promesa: "Veja chegar o que pode dar errado e decida antes que isso decida por você.",
  },
  compras: {
    nombre: "Sua Compra Certa",
    promesa: "Compre o que é certo, de quem é certo, pelo preço certo.",
  },
  entrega: {
    nombre: "Da Oficina às Mãos Deles",
    promesa: "Que chegue inteiro, no prazo e sem surpresas de custo.",
  },
};

const de: typeof es = {
  quality: {
    nombre: "Qualität & Vertrauen",
    promesa: "Damit deine Kunden dir vertrauen, wiederkommen und dich weiterempfehlen.",
  },
  health_safety: {
    nombre: "Sicherheit & Menschen",
    promesa: "Schütze deine Leute und dein Geschäft vor ihrem schlimmsten Tag.",
  },
  environmental: {
    nombre: "Umwelt & Zukunft",
    promesa: "Mach Nachhaltigkeit zu einem Vorteil, den man sieht und für den man gern bezahlt.",
  },
  seguridad_digital: {
    nombre: "Digitale Sicherheit",
    promesa: "Sichere deine Daten, deine Konten und das Vertrauen deiner Kunden.",
  },
  exportacion: {
    nombre: "Weltweit verkaufen",
    promesa: "Bring dein Produkt zu Kunden in anderen Ländern, mit Methode.",
  },
  franquicias: {
    nombre: "Vervielfache dein Geschäft",
    promesa: "Mach aus deinem bewährten Geschäft viele, die genauso funktionieren.",
  },
  risk_management: {
    nombre: "Risiken im Griff",
    promesa: "Sieh kommen, was schiefgehen kann, und entscheide, bevor es für dich entscheidet.",
  },
  compras: {
    nombre: "Richtig einkaufen",
    promesa: "Kauf das Richtige, beim Richtigen, zum richtigen Preis.",
  },
  entrega: {
    nombre: "Von der Werkstatt in ihre Hände",
    promesa: "Damit es heil, pünktlich und ohne Kostenüberraschungen ankommt.",
  },
};

const it: typeof es = {
  quality: {
    nombre: "Qualità e Fiducia",
    promesa: "Fai sì che il tuo cliente si fidi, torni e ti consigli.",
  },
  health_safety: {
    nombre: "Sicurezza e Persone",
    promesa: "Proteggi la tua gente e la tua attività dal loro giorno peggiore.",
  },
  environmental: {
    nombre: "Ambiente e Futuro",
    promesa: "Trasforma la sostenibilità in un vantaggio che si nota e si fa pagare.",
  },
  seguridad_digital: {
    nombre: "Sicurezza Digitale",
    promesa: "Blinda i tuoi dati, i tuoi account e la fiducia dei tuoi clienti.",
  },
  exportacion: {
    nombre: "Vendere al Mondo",
    promesa: "Porta il tuo prodotto a clienti di altri paesi, con metodo.",
  },
  franquicias: {
    nombre: "Moltiplica la tua Attività",
    promesa: "Trasforma la tua attività collaudata in tante altre che funzionano allo stesso modo.",
  },
  risk_management: {
    nombre: "Rischi sotto Controllo",
    promesa: "Anticipa ciò che può andare storto, e decidi tu prima che siano gli imprevisti a decidere per te.",
  },
  compras: {
    nombre: "Il tuo Acquisto Giusto",
    promesa: "Compra la cosa giusta, dal fornitore giusto, al prezzo giusto.",
  },
  entrega: {
    nombre: "Dal Laboratorio alle loro Mani",
    promesa: "Fai in modo che arrivi integro, puntuale e senza sorprese sui costi.",
  },
};

const ja: typeof es = {
  quality: {
    nombre: "品質と信頼",
    promesa: "お客様に信頼され、また選ばれ、紹介してもらえるように。",
  },
  health_safety: {
    nombre: "安全と人",
    promesa: "仲間とビジネスを、最悪の一日から守りましょう。",
  },
  environmental: {
    nombre: "環境と未来",
    promesa: "サステナビリティを、目に見えて対価につながる強みに変えましょう。",
  },
  seguridad_digital: {
    nombre: "デジタルセキュリティ",
    promesa: "データ、アカウント、そしてお客様からの信頼を、しっかり守りましょう。",
  },
  exportacion: {
    nombre: "世界に売る",
    promesa: "確かな方法で、製品を海外のお客様へ届けましょう。",
  },
  franquicias: {
    nombre: "ビジネスを広げる",
    promesa: "実績のあるビジネスを、同じように回るたくさんの拠点へ広げましょう。",
  },
  risk_management: {
    nombre: "リスクを管理下に",
    promesa: "うまくいかない可能性を先読みして、それに決められてしまう前に、自分で決めましょう。",
  },
  compras: {
    nombre: "正しい仕入れ",
    promesa: "必要なものを、ふさわしい相手から、適正な価格で仕入れましょう。",
  },
  entrega: {
    nombre: "工房からお客様の手へ",
    promesa: "壊れずに、時間どおりに、想定外の費用なしで届くように。",
  },
};

const zh: typeof es = {
  quality: {
    nombre: "质量与信任",
    promesa: "让你的客户信任你、再回来，还把你推荐给别人。",
  },
  health_safety: {
    nombre: "安全与人",
    promesa: "保护你的人和你的生意，挺过最糟糕的那一天。",
  },
  environmental: {
    nombre: "环境与未来",
    promesa: "把可持续变成看得见、也能收钱的优势。",
  },
  seguridad_digital: {
    nombre: "数字安全",
    promesa: "守牢你的数据、你的账户，还有客户对你的信任。",
  },
  exportacion: {
    nombre: "卖向世界",
    promesa: "有方法地把你的产品卖给其他国家的客户。",
  },
  franquicias: {
    nombre: "让生意倍增",
    promesa: "把你已经验证过的生意，复制成许多同样运转的店。",
  },
  risk_management: {
    nombre: "风险可控",
    promesa: "提前看到可能出错的地方，在它替你做决定之前先做决定。",
  },
  compras: {
    nombre: "正确采购",
    promesa: "买对的东西，找对的供应商，付对的价钱。",
  },
  entrega: {
    nombre: "从作坊到客户手中",
    promesa: "完好无损、准时送达，成本上没有意外。",
  },
};

const ko: typeof es = {
  quality: {
    nombre: "품질과 신뢰",
    promesa: "고객이 믿고, 다시 찾고, 추천하도록.",
  },
  health_safety: {
    nombre: "안전과 사람",
    promesa: "최악의 날로부터 사람들과 사업을 지켜요.",
  },
  environmental: {
    nombre: "환경과 미래",
    promesa: "지속 가능성을 눈에 띄고 돈이 되는 강점으로 바꿔요.",
  },
  seguridad_digital: {
    nombre: "디지털 보안",
    promesa: "데이터와 계정, 고객의 신뢰를 단단히 지켜요.",
  },
  exportacion: {
    nombre: "세계로 팔기",
    promesa: "체계적인 방법으로 다른 나라의 고객에게 제품을 선보여요.",
  },
  franquicias: {
    nombre: "사업 확장",
    promesa: "검증된 사업을 똑같이 돌아가는 여러 곳으로 늘려요.",
  },
  risk_management: {
    nombre: "위험 관리",
    promesa: "잘못될 수 있는 일을 미리 내다보고, 그 일이 대신 정해 버리기 전에 먼저 결정해요.",
  },
  compras: {
    nombre: "올바른 구매",
    promesa: "필요한 것을, 알맞은 곳에서, 알맞은 가격에 사요.",
  },
  entrega: {
    nombre: "공방에서 고객의 손까지",
    promesa: "온전하게, 제때, 뜻밖의 비용 없이 도착하도록.",
  },
};

const ar: typeof es = {
  quality: {
    nombre: "الجودة والثقة",
    promesa: "أن يثق بكم عميلكم، ويعود، ويوصي بكم.",
  },
  health_safety: {
    nombre: "السلامة والناس",
    promesa: "احموا فريقكم وعملكم من أسوأ أيامهما.",
  },
  environmental: {
    nombre: "البيئة والمستقبل",
    promesa: "حوّلوا الاستدامة إلى ميزة تُلاحَظ ويُدفع مقابلها.",
  },
  seguridad_digital: {
    nombre: "الأمن الرقمي",
    promesa: "حصّنوا بياناتكم وحساباتكم وثقة عملائكم.",
  },
  exportacion: {
    nombre: "البيع للعالم",
    promesa: "خذوا منتجكم إلى عملاء في بلدان أخرى، بمنهج واضح.",
  },
  franquicias: {
    nombre: "ضاعف عملك",
    promesa: "حوّلوا عملكم المجرَّب إلى فروع كثيرة تعمل بالطريقة نفسها.",
  },
  risk_management: {
    nombre: "المخاطر تحت السيطرة",
    promesa: "توقّعوا ما قد يتعثّر، واحسموا قراركم قبل أن يُحسم عنكم.",
  },
  compras: {
    nombre: "شراؤكم الصحيح",
    promesa: "اشتروا ما يلزم، ممن يلزم، بالسعر الذي يلزم.",
  },
  entrega: {
    nombre: "من الورشة إلى أيديهم",
    promesa: "أن يصل سليمًا، وفي موعده، ودون مفاجآت في التكلفة.",
  },
};

const hi: typeof es = {
  quality: {
    nombre: "गुणवत्ता और भरोसा",
    promesa: "ताकि आपका ग्राहक आप पर भरोसा करे, लौटकर आए और दूसरों से आपकी सिफ़ारिश करे।",
  },
  health_safety: {
    nombre: "सुरक्षा और लोग",
    promesa: "अपने लोगों और अपने व्यवसाय को उनके सबसे बुरे दिन से बचाएँ।",
  },
  environmental: {
    nombre: "पर्यावरण और भविष्य",
    promesa: "टिकाऊपन को ऐसी बढ़त में बदलें जो दिखे भी और जिसकी कीमत भी मिले।",
  },
  seguridad_digital: {
    nombre: "डिजिटल सुरक्षा",
    promesa: "अपने डेटा, अपने खातों और अपने ग्राहकों के भरोसे को पूरी तरह सुरक्षित करें।",
  },
  exportacion: {
    nombre: "दुनिया को बेचना",
    promesa: "अपना प्रोडक्ट दूसरे देशों के ग्राहकों तक पहुँचाएँ, सही तरीके से।",
  },
  franquicias: {
    nombre: "अपना व्यवसाय बढ़ाएँ",
    promesa: "अपने आज़माए हुए व्यवसाय को ऐसे कई व्यवसायों में बदलें जो बिल्कुल वैसे ही चलें।",
  },
  risk_management: {
    nombre: "जोखिम नियंत्रण में",
    promesa: "जो गड़बड़ हो सकता है उसे पहले से भाँप लें, और इससे पहले कि वह आपके लिए फ़ैसला करे, आप खुद फ़ैसला करें।",
  },
  compras: {
    nombre: "आपकी सही खरीद",
    promesa: "सही चीज़ खरीदें, सही सप्लायर से, सही कीमत पर।",
  },
  entrega: {
    nombre: "कार्यशाला से उनके हाथों तक",
    promesa: "ताकि सामान सही-सलामत, समय पर और बिना किसी अचानक खर्च के पहुँचे।",
  },
};

export const MUNDOS_I18N: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
