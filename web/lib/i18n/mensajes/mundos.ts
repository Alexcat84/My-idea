/**
 * El nombre y la promesa de cada mundo, por idioma (i18n F3; glosario en
 * DISENO §6). La fuente del español es web/lib/assets/packs_catalog.json: este
 * `es` es su COPIA y lib/catalogoMundos.test.ts falla si se separan. Las claves
 * son la `clave` de cada pack (el dominio): no se traducen.
 */
import type { PorIdioma } from "../config";

const es = {
  quality: { nombre: "Calidad y Confianza", promesa: "Trabaja la calidad para que tu cliente confíe, vuelva y te recomiende." },
  health_safety: { nombre: "Seguridad y Personas", promesa: "Prepara a tu gente y a tu negocio para los riesgos de cada día." },
  environmental: { nombre: "Ambiente y Futuro", promesa: "Haz de lo sostenible una ventaja que tus clientes puedan ver." },
  seguridad_digital: { nombre: "Seguridad Digital", promesa: "Un plan para proteger tus datos, tus cuentas y la confianza de tus clientes." },
  exportacion: { nombre: "Vender al Mundo", promesa: "Lleva tu producto a clientes de otros países, con método." },
  franquicias: { nombre: "Multiplica tu Negocio", promesa: "Prepara tu negocio probado para replicarlo con el mismo estándar." },
  risk_management: { nombre: "Riesgos Bajo Control", promesa: "Anticipa lo que puede fallar y decide antes de que decida por ti." },
  compras: { nombre: "Tu Compra Correcta", promesa: "Elige con método qué comprar, a quién y a qué precio." },
  entrega: { nombre: "Del Taller a sus Manos", promesa: "Planea tus entregas para que lleguen enteras, a tiempo y con costos previstos." },
  primer_equipo: { nombre: "Primer Equipo", promesa: "Contrata bien, dirige mejor y haz crecer a tu gente." },
};

const en: typeof es = {
  quality: { nombre: "Quality & Trust", promesa: "Work on quality so your customers trust you, come back and recommend you." },
  health_safety: { nombre: "Safety & People", promesa: "Prepare your people and your business for everyday risks." },
  environmental: { nombre: "Environment & Future", promesa: "Make sustainability an advantage your customers can see." },
  seguridad_digital: { nombre: "Digital Security", promesa: "A plan to protect your data, your accounts and your customers' trust." },
  exportacion: { nombre: "Sell to the World", promesa: "Take your product to customers in other countries, with a method." },
  franquicias: { nombre: "Multiply Your Business", promesa: "Get your proven business ready to replicate to the same standard." },
  risk_management: { nombre: "Risks Under Control", promesa: "Anticipate what could go wrong and decide before it decides for you." },
  compras: { nombre: "The Right Purchase", promesa: "Decide methodically what to buy, from whom and at what price." },
  entrega: { nombre: "From Workshop to Customer", promesa: "Plan your deliveries so they arrive intact, on time and with predictable costs." },
  primer_equipo: { nombre: "First Team", promesa: "Hire well, lead better and help your people grow." },
};

const fr: typeof es = {
  quality: {
    nombre: "Qualité et confiance",
    promesa: "Travaille la qualité pour que ton client te fasse confiance, revienne et te recommande.",
  },
  health_safety: {
    nombre: "Sécurité et personnes",
    promesa: "Prépare ton équipe et ton entreprise aux risques du quotidien.",
  },
  environmental: {
    nombre: "Environnement et avenir",
    promesa: "Fais du durable un avantage visible pour tes clients.",
  },
  seguridad_digital: {
    nombre: "Sécurité numérique",
    promesa: "Un plan pour protéger tes données, tes comptes et la confiance de tes clients.",
  },
  exportacion: {
    nombre: "Vendre au monde",
    promesa: "Porte ton produit jusqu'aux clients d'autres pays, avec méthode.",
  },
  franquicias: {
    nombre: "Multiplie ton entreprise",
    promesa: "Prépare ton entreprise qui a fait ses preuves pour la reproduire avec la même exigence.",
  },
  risk_management: {
    nombre: "Risques sous contrôle",
    promesa: "Anticipe ce qui peut mal tourner et décide avant que ça décide pour toi.",
  },
  compras: {
    nombre: "Ton bon achat",
    promesa: "Choisis avec méthode quoi acheter, à qui et à quel prix.",
  },
  entrega: {
    nombre: "De l'atelier à leurs mains",
    promesa: "Planifie tes livraisons pour qu'elles arrivent intactes, à temps et avec des coûts prévus.",
  },
  primer_equipo: {
    nombre: "Première équipe",
    promesa: "Recrute bien, dirige mieux et fais grandir ton équipe.",
  },
};

const pt: typeof es = {
  quality: {
    nombre: "Qualidade e Confiança",
    promesa: "Trabalhe a qualidade para que seu cliente confie, volte e recomende você.",
  },
  health_safety: {
    nombre: "Segurança e Pessoas",
    promesa: "Prepare sua equipe e seu negócio para os riscos do dia a dia.",
  },
  environmental: {
    nombre: "Ambiente e Futuro",
    promesa: "Faça da sustentabilidade uma vantagem que seus clientes possam ver.",
  },
  seguridad_digital: {
    nombre: "Segurança Digital",
    promesa: "Um plano para proteger seus dados, suas contas e a confiança dos seus clientes.",
  },
  exportacion: {
    nombre: "Vender para o Mundo",
    promesa: "Leve seu produto a clientes de outros países, com método.",
  },
  franquicias: {
    nombre: "Multiplique seu Negócio",
    promesa: "Prepare seu negócio comprovado para replicá-lo com o mesmo padrão.",
  },
  risk_management: {
    nombre: "Riscos sob Controle",
    promesa: "Antecipe o que pode dar errado e decida antes que isso decida por você.",
  },
  compras: {
    nombre: "Sua Compra Certa",
    promesa: "Escolha com método o que comprar, de quem e por qual preço.",
  },
  entrega: {
    nombre: "Da Oficina às Mãos Deles",
    promesa: "Planeje suas entregas para que cheguem inteiras, no prazo e com custos previstos.",
  },
  primer_equipo: {
    nombre: "Primeira Equipe",
    promesa: "Contrate bem, lidere melhor e faça sua equipe crescer.",
  },
};

const de: typeof es = {
  quality: {
    nombre: "Qualität & Vertrauen",
    promesa: "Arbeite an deiner Qualität, damit deine Kunden dir vertrauen, wiederkommen und dich weiterempfehlen.",
  },
  health_safety: {
    nombre: "Sicherheit & Menschen",
    promesa: "Bereite deine Leute und dein Geschäft auf die Risiken des Alltags vor.",
  },
  environmental: {
    nombre: "Umwelt & Zukunft",
    promesa: "Mach Nachhaltigkeit zu einem Vorteil, den deine Kunden sehen.",
  },
  seguridad_digital: {
    nombre: "Digitale Sicherheit",
    promesa: "Ein Plan, um deine Daten, deine Konten und das Vertrauen deiner Kunden zu schützen.",
  },
  exportacion: {
    nombre: "Weltweit verkaufen",
    promesa: "Bring dein Produkt zu Kunden in anderen Ländern, mit Methode.",
  },
  franquicias: {
    nombre: "Vervielfache dein Geschäft",
    promesa: "Bereite dein bewährtes Geschäft darauf vor, es mit demselben Standard zu vervielfältigen.",
  },
  risk_management: {
    nombre: "Risiken im Griff",
    promesa: "Erkenne früh, was schiefgehen kann, und entscheide, bevor es für dich entscheidet.",
  },
  compras: {
    nombre: "Richtig einkaufen",
    promesa: "Entscheide mit Methode, was du kaufst, bei wem und zu welchem Preis.",
  },
  entrega: {
    nombre: "Von der Werkstatt in ihre Hände",
    promesa: "Plane deine Lieferungen so, dass sie heil, pünktlich und mit eingeplanten Kosten ankommen.",
  },
  primer_equipo: {
    nombre: "Erstes Team",
    promesa: "Stell gut ein, führe besser und lass deine Leute wachsen.",
  },
};

const it: typeof es = {
  quality: {
    nombre: "Qualità e Fiducia",
    promesa: "Cura la qualità perché il tuo cliente si fidi, torni e ti consigli.",
  },
  health_safety: {
    nombre: "Sicurezza e Persone",
    promesa: "Prepara la tua gente e la tua attività ai rischi di ogni giorno.",
  },
  environmental: {
    nombre: "Ambiente e Futuro",
    promesa: "Fai della sostenibilità un vantaggio che i tuoi clienti possano vedere.",
  },
  seguridad_digital: {
    nombre: "Sicurezza Digitale",
    promesa: "Un piano per proteggere i tuoi dati, i tuoi account e la fiducia dei tuoi clienti.",
  },
  exportacion: {
    nombre: "Vendere al Mondo",
    promesa: "Porta il tuo prodotto a clienti di altri paesi, con metodo.",
  },
  franquicias: {
    nombre: "Moltiplica la tua Attività",
    promesa: "Prepara la tua attività collaudata per replicarla con lo stesso standard.",
  },
  risk_management: {
    nombre: "Rischi sotto Controllo",
    promesa: "Anticipa ciò che può andare storto e decidi tu prima che siano gli imprevisti a decidere per te.",
  },
  compras: {
    nombre: "Il tuo Acquisto Giusto",
    promesa: "Scegli con metodo cosa comprare, da chi e a quale prezzo.",
  },
  entrega: {
    nombre: "Dal Laboratorio alle loro Mani",
    promesa: "Pianifica le tue consegne perché arrivino integre, puntuali e con costi previsti.",
  },
  primer_equipo: {
    nombre: "Prima Squadra",
    promesa: "Assumi bene, guida meglio e fai crescere la tua squadra.",
  },
};

const ja: typeof es = {
  quality: {
    nombre: "品質と信頼",
    promesa: "品質を磨いて、お客様に信頼され、また選ばれ、紹介してもらえるように。",
  },
  health_safety: {
    nombre: "安全と人",
    promesa: "日々の安全上のリスクに、仲間とビジネスで備えましょう。",
  },
  environmental: {
    nombre: "環境と未来",
    promesa: "サステナビリティを、お客様の目に見える強みにしましょう。",
  },
  seguridad_digital: {
    nombre: "デジタルセキュリティ",
    promesa: "データ、アカウント、そしてお客様からの信頼を守るための計画。",
  },
  exportacion: {
    nombre: "世界に売る",
    promesa: "確かな方法で、製品を海外のお客様へ届けましょう。",
  },
  franquicias: {
    nombre: "ビジネスを広げる",
    promesa: "実績のあるビジネスを、同じ水準で展開できるように準備しましょう。",
  },
  risk_management: {
    nombre: "リスクを管理下に",
    promesa: "うまくいかない可能性を先読みして、それに決められてしまう前に、自分で決めましょう。",
  },
  compras: {
    nombre: "正しい仕入れ",
    promesa: "何を、誰から、いくらで仕入れるか、筋道を立てて決めましょう。",
  },
  entrega: {
    nombre: "工房からお客様の手へ",
    promesa: "壊れずに、時間どおりに、見込んだ費用で届くよう、配送を計画しましょう。",
  },
  primer_equipo: {
    nombre: "はじめてのチーム",
    promesa: "よい人を採用し、よりよく導き、メンバーを育てる。",
  },
};

const zh: typeof es = {
  quality: {
    nombre: "质量与信任",
    promesa: "把质量做好，让客户信任你、再回来，还把你推荐给别人。",
  },
  health_safety: {
    nombre: "安全与人",
    promesa: "让你的团队和生意，为日常的安全风险做好准备。",
  },
  environmental: {
    nombre: "环境与未来",
    promesa: "把可持续变成客户看得见的优势。",
  },
  seguridad_digital: {
    nombre: "数字安全",
    promesa: "一份保护你的数据、账户和客户信任的计划。",
  },
  exportacion: {
    nombre: "卖向世界",
    promesa: "有方法地把你的产品卖给其他国家的客户。",
  },
  franquicias: {
    nombre: "让生意倍增",
    promesa: "为你已经验证过的生意做好准备，按同样的标准复制。",
  },
  risk_management: {
    nombre: "风险可控",
    promesa: "预判可能出错的地方，在它替你做决定之前先做决定。",
  },
  compras: {
    nombre: "正确采购",
    promesa: "有方法地决定买什么、向谁买、以什么价格买。",
  },
  entrega: {
    nombre: "从作坊到客户手中",
    promesa: "规划你的交付，让货物完好、准时送达，成本心中有数。",
  },
  primer_equipo: {
    nombre: "第一支团队",
    promesa: "招对人，带好队，让你的人成长。",
  },
};

const ko: typeof es = {
  quality: {
    nombre: "품질과 신뢰",
    promesa: "품질을 다듬어 고객이 믿고, 다시 찾고, 추천하도록.",
  },
  health_safety: {
    nombre: "안전과 사람",
    promesa: "사람들과 사업이 일상의 안전 위험에 대비하도록 준비해요.",
  },
  environmental: {
    nombre: "환경과 미래",
    promesa: "지속 가능성을 고객이 알아볼 수 있는 강점으로 만들어요.",
  },
  seguridad_digital: {
    nombre: "디지털 보안",
    promesa: "데이터와 계정, 고객의 신뢰를 지키기 위한 계획.",
  },
  exportacion: {
    nombre: "세계로 팔기",
    promesa: "체계적인 방법으로 다른 나라의 고객에게 제품을 선보여요.",
  },
  franquicias: {
    nombre: "사업 확장",
    promesa: "검증된 사업을 같은 기준으로 확장할 수 있도록 준비해요.",
  },
  risk_management: {
    nombre: "위험 관리",
    promesa: "잘못될 수 있는 일을 미리 내다보고, 그 일이 대신 정해 버리기 전에 먼저 결정해요.",
  },
  compras: {
    nombre: "올바른 구매",
    promesa: "무엇을, 누구에게서, 얼마에 살지 체계적으로 정해요.",
  },
  entrega: {
    nombre: "공방에서 고객의 손까지",
    promesa: "온전하게, 제때, 예상한 비용으로 도착하도록 배송을 계획해요.",
  },
  primer_equipo: {
    nombre: "첫 팀",
    promesa: "잘 뽑고, 더 잘 이끌고, 팀원이 성장하도록.",
  },
};

const ar: typeof es = {
  quality: {
    nombre: "الجودة والثقة",
    promesa: "اعملوا على الجودة ليثق بكم عميلكم، ويعود، ويوصي بكم.",
  },
  health_safety: {
    nombre: "السلامة والناس",
    promesa: "جهّزوا فريقكم وعملكم لمخاطر السلامة اليومية.",
  },
  environmental: {
    nombre: "البيئة والمستقبل",
    promesa: "اجعلوا الاستدامة ميزة يراها عملاؤكم.",
  },
  seguridad_digital: {
    nombre: "الأمن الرقمي",
    promesa: "خطة لحماية بياناتكم وحساباتكم وثقة عملائكم.",
  },
  exportacion: {
    nombre: "البيع للعالم",
    promesa: "خذوا منتجكم إلى عملاء في بلدان أخرى، بمنهج واضح.",
  },
  franquicias: {
    nombre: "ضاعف عملك",
    promesa: "جهّزوا عملكم المجرَّب ليُكرَّر بالمعيار نفسه.",
  },
  risk_management: {
    nombre: "المخاطر تحت السيطرة",
    promesa: "توقّعوا ما قد يتعثّر، واحسموا قراركم قبل أن يُحسم عنكم.",
  },
  compras: {
    nombre: "شراؤكم الصحيح",
    promesa: "اختاروا بمنهج ماذا تشترون، وممّن، وبأي سعر.",
  },
  entrega: {
    nombre: "من الورشة إلى أيديهم",
    promesa: "خطّطوا لتوصيلاتكم لتصل سليمة، وفي موعدها، وبتكاليف محسوبة مسبقًا.",
  },
  primer_equipo: {
    nombre: "فريقكم الأول",
    promesa: "وظّفوا جيدًا، وقودوا أفضل، وساعدوا فريقكم على النمو.",
  },
};

const hi: typeof es = {
  quality: {
    nombre: "गुणवत्ता और भरोसा",
    promesa: "गुणवत्ता पर काम करें, ताकि आपका ग्राहक आप पर भरोसा करे, लौटकर आए और दूसरों से आपकी सिफ़ारिश करे।",
  },
  health_safety: {
    nombre: "सुरक्षा और लोग",
    promesa: "अपने लोगों और अपने व्यवसाय को रोज़मर्रा के सुरक्षा जोखिमों के लिए तैयार करें।",
  },
  environmental: {
    nombre: "पर्यावरण और भविष्य",
    promesa: "टिकाऊपन को ऐसी बढ़त बनाएँ जो आपके ग्राहकों को दिखे।",
  },
  seguridad_digital: {
    nombre: "डिजिटल सुरक्षा",
    promesa: "अपने डेटा, अपने खातों और अपने ग्राहकों के भरोसे की सुरक्षा के लिए एक योजना।",
  },
  exportacion: {
    nombre: "दुनिया को बेचना",
    promesa: "अपना प्रोडक्ट दूसरे देशों के ग्राहकों तक पहुँचाएँ, सही तरीके से।",
  },
  franquicias: {
    nombre: "अपना व्यवसाय बढ़ाएँ",
    promesa: "अपने आज़माए हुए व्यवसाय को उसी मानक के साथ दोहराने के लिए तैयार करें।",
  },
  risk_management: {
    nombre: "जोखिम नियंत्रण में",
    promesa: "जो गड़बड़ हो सकता है उसे पहले से भाँप लें, और इससे पहले कि वह आपके लिए फ़ैसला करे, आप खुद फ़ैसला करें।",
  },
  compras: {
    nombre: "आपकी सही खरीद",
    promesa: "तरीके से तय करें कि क्या खरीदना है, किससे और किस कीमत पर।",
  },
  entrega: {
    nombre: "कार्यशाला से उनके हाथों तक",
    promesa: "अपनी डिलीवरी की योजना बनाएँ, ताकि सामान सही-सलामत, समय पर और पहले से आँकी गई लागत में पहुँचे।",
  },
  primer_equipo: {
    nombre: "आपकी पहली टीम",
    promesa: "सही लोगों को चुनें, बेहतर नेतृत्व करें और अपनी टीम को आगे बढ़ाएँ।",
  },
};

export const MUNDOS_I18N: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
