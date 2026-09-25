/** /potenciadores: app/potenciadores/page.tsx y ElegirPotenciador.tsx (solo la puerta y el foco; la parrilla vive en PotenciaTuIdea). */
import type { PorIdioma } from "../config";

const es = {
  misIdeas: "Mis ideas /",
  titulo: "Potenciar",
  ideaSinTitulo: "Idea sin título",
  elegirIdea: {
    titulo: "¿Qué idea quieres potenciar?",
    sinIdeas: "Los potenciadores se suman a una idea. Cuando tengas la primera, aquí podrás elegirla.",
    texto: "Elige una y te llevo a sus potenciadores.",
    pista: "Añádele un mundo o revisa sus potenciadores.",
  },
  elegirPotenciador: {
    error: "no pudimos cargar tu idea; intenta de nuevo en un momento",
    cargando: "Cargando tu idea…",
    cambiarIdea: "← Cambiar de idea",
    titulo: "¿Qué potenciador quieres usar?",
    texto: "Para <idea/>. Al aplicarlo queda agregado a tu idea, y sigues desde ahí.",
  },
};

const en: typeof es = {
  misIdeas: "My ideas /",
  titulo: "Power up",
  ideaSinTitulo: "Untitled idea",
  elegirIdea: {
    titulo: "Which idea do you want to power up?",
    sinIdeas: "Power-ups are added to an idea. Once you have your first one, you'll be able to pick it here.",
    texto: "Pick one and I'll take you to its power-ups.",
    pista: "Add a world to it or check out its power-ups.",
  },
  elegirPotenciador: {
    error: "we couldn't load your idea; try again in a moment",
    cargando: "Loading your idea…",
    cambiarIdea: "← Switch idea",
    titulo: "Which power-up do you want to use?",
    texto: "For <idea/>. Once you apply it, it's added to your idea and you pick up from there.",
  },
};

const fr: typeof es = {
  misIdeas: "Mes idées /",
  titulo: "Propulser",
  ideaSinTitulo: "Idée sans titre",
  elegirIdea: {
    titulo: "Quelle idée veux-tu propulser?",
    sinIdeas: "Les propulseurs s'ajoutent à une idée. Quand tu auras la première, tu pourras la choisir ici.",
    texto: "Choisis-en une et je t'emmène vers ses propulseurs.",
    pista: "Ajoute-lui un monde ou jette un œil à ses propulseurs.",
  },
  elegirPotenciador: {
    error: "nous n'avons pas pu charger ton idée; réessaie dans un instant",
    cargando: "Chargement de ton idée…",
    cambiarIdea: "← Changer d'idée",
    titulo: "Quel propulseur veux-tu utiliser?",
    texto: "Pour <idea/>. Une fois appliqué, il s'ajoute à ton idée, et tu continues à partir de là.",
  },
};

const pt: typeof es = {
  misIdeas: "Minhas ideias /",
  titulo: "Potencializar",
  ideaSinTitulo: "Ideia sem título",
  elegirIdea: {
    titulo: "Qual ideia você quer potencializar?",
    sinIdeas: "Os potencializadores se somam a uma ideia. Quando você tiver a primeira, vai poder escolhê-la aqui.",
    texto: "Escolha uma e eu levo você aos potencializadores dela.",
    pista: "Adicione um mundo a ela ou confira os potencializadores dela.",
  },
  elegirPotenciador: {
    error: "não conseguimos carregar sua ideia; tente de novo daqui a pouco",
    cargando: "Carregando sua ideia…",
    cambiarIdea: "← Trocar de ideia",
    titulo: "Qual potencializador você quer usar?",
    texto: "Para <idea/>. Ao aplicá-lo, ele fica adicionado à sua ideia, e você continua dali.",
  },
};

const de: typeof es = {
  misIdeas: "Meine Ideen /",
  titulo: "Stärken",
  ideaSinTitulo: "Idee ohne Titel",
  elegirIdea: {
    titulo: "Welche Idee möchtest du stärken?",
    sinIdeas: "Verstärker gehören immer zu einer Idee. Sobald du deine erste hast, kannst du sie hier auswählen.",
    texto: "Wähl eine aus, und ich bringe dich zu ihren Verstärkern.",
    pista: "Füge ihr eine Welt hinzu oder sieh dir ihre Verstärker an.",
  },
  elegirPotenciador: {
    error: "wir konnten deine Idee nicht laden; versuch es gleich noch einmal",
    cargando: "Deine Idee wird geladen…",
    cambiarIdea: "← Idee wechseln",
    titulo: "Welchen Verstärker möchtest du nutzen?",
    texto: "Für <idea/>. Sobald du ihn anwendest, gehört er zu deiner Idee, und du machst von dort aus weiter.",
  },
};

const it: typeof es = {
  misIdeas: "Le mie idee /",
  titulo: "Potenzia",
  ideaSinTitulo: "Idea senza titolo",
  elegirIdea: {
    titulo: "Quale idea vuoi potenziare?",
    sinIdeas: "I potenziatori si aggiungono a un'idea. Quando avrai la prima, qui potrai sceglierla.",
    texto: "Scegline una e ti porto ai suoi potenziatori.",
    pista: "Aggiungile un mondo o dai un'occhiata ai suoi potenziatori.",
  },
  elegirPotenciador: {
    error: "non siamo riusciti a caricare la tua idea; riprova tra un momento",
    cargando: "Sto caricando la tua idea…",
    cambiarIdea: "← Cambia idea",
    titulo: "Quale potenziatore vuoi usare?",
    texto: "Per <idea/>. Quando lo applichi, si aggiunge alla tua idea e riparti da lì.",
  },
};

const ja: typeof es = {
  misIdeas: "アイデア一覧 /",
  titulo: "強化する",
  ideaSinTitulo: "無題のアイデア",
  elegirIdea: {
    titulo: "どのアイデアを強化しますか？",
    sinIdeas: "強化オプションはアイデアに追加するものです。最初のアイデアができたら、ここで選べます。",
    texto: "ひとつ選ぶと、その強化オプションの画面に進みます。",
    pista: "ワールドを追加するか、強化オプションを確認しましょう。",
  },
  elegirPotenciador: {
    error: "アイデアを読み込めませんでした。少し待ってからもう一度お試しください",
    cargando: "アイデアを読み込んでいます…",
    cambiarIdea: "← アイデアを変更",
    titulo: "どの強化オプションを使いますか？",
    texto: "対象：<idea/>。適用するとアイデアに追加され、そこから続きを進められます。",
  },
};

const zh: typeof es = {
  misIdeas: "我的想法 /",
  titulo: "赋能",
  ideaSinTitulo: "未命名的想法",
  elegirIdea: {
    titulo: "你想为哪个想法赋能？",
    sinIdeas: "赋能工具要加在某个想法上。等你有了第一个想法，就能在这里选它。",
    texto: "选一个，我带你去看它的赋能工具。",
    pista: "为它添加一个世界，或查看它的赋能工具。",
  },
  elegirPotenciador: {
    error: "没能加载你的想法，请稍后再试",
    cargando: "正在加载你的想法…",
    cambiarIdea: "← 换一个想法",
    titulo: "你想使用哪个赋能工具？",
    texto: "用于 <idea/>。应用后它会加到你的想法上，你从那里继续。",
  },
};

const ko: typeof es = {
  misIdeas: "내 아이디어 /",
  titulo: "강화하기",
  ideaSinTitulo: "제목 없는 아이디어",
  elegirIdea: {
    titulo: "어떤 아이디어를 강화할까요?",
    sinIdeas: "강화 옵션은 아이디어에 더하는 거예요. 첫 아이디어가 생기면 여기서 고를 수 있어요.",
    texto: "하나를 고르면 그 아이디어의 강화 옵션으로 안내할게요.",
    pista: "월드를 더하거나 강화 옵션을 살펴보세요.",
  },
  elegirPotenciador: {
    error: "아이디어를 불러오지 못했어요. 잠시 후 다시 시도해 주세요",
    cargando: "아이디어를 불러오는 중…",
    cambiarIdea: "← 다른 아이디어 고르기",
    titulo: "어떤 강화 옵션을 쓸까요?",
    texto: "대상: <idea/>. 적용하면 아이디어에 더해지고, 거기서부터 이어 가면 돼요.",
  },
};

const ar: typeof es = {
  misIdeas: "أفكاري /",
  titulo: "تعزيز",
  ideaSinTitulo: "فكرة بلا عنوان",
  elegirIdea: {
    titulo: "أي فكرة تريدون تعزيزها؟",
    sinIdeas: "أدوات التعزيز تُضاف إلى فكرة. حين تكون لديكم أولى أفكاركم، ستتمكنون من اختيارها هنا.",
    texto: "اختاروا واحدة وسآخذكم إلى أدوات تعزيزها.",
    pista: "أضيفوا إليها عالمًا أو تفقّدوا أدوات تعزيزها.",
  },
  elegirPotenciador: {
    error: "تعذّر تحميل فكرتكم؛ حاولوا مرة أخرى بعد قليل",
    cargando: "جارٍ تحميل فكرتكم…",
    cambiarIdea: "→ تغيير الفكرة",
    titulo: "أي أداة تعزيز تريدون استخدامها؟",
    texto: "من أجل <idea/>. عند تطبيقها تُضاف إلى فكرتكم، وتتابعون من هناك.",
  },
};

const hi: typeof es = {
  misIdeas: "मेरे विचार /",
  titulo: "सशक्त करें",
  ideaSinTitulo: "बिना नाम का विचार",
  elegirIdea: {
    titulo: "किस विचार को सशक्त करना है?",
    sinIdeas: "सशक्त विकल्प किसी विचार में जोड़े जाते हैं। जब आपका पहला विचार होगा, उसे यहीं चुना जा सकेगा।",
    texto: "एक चुनें, और उसके सशक्त विकल्प आपके सामने होंगे।",
    pista: "इसमें कोई दुनिया जोड़ें या इसके सशक्त विकल्प देखें।",
  },
  elegirPotenciador: {
    error: "हम आपका विचार लोड नहीं कर पाए; थोड़ी देर में फिर से कोशिश करें",
    cargando: "आपका विचार लोड हो रहा है…",
    cambiarIdea: "← विचार बदलें",
    titulo: "कौन-सा सशक्त विकल्प इस्तेमाल करना है?",
    texto: "<idea/> के लिए। लागू करते ही यह आपके विचार में जुड़ जाएगा, और सफ़र वहीं से आगे चलेगा।",
  },
};

export const POTENCIADORES: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
