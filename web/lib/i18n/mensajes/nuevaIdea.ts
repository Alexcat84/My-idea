/** /nueva: La Chispa, la espera del organizador y sus errores (app/nueva/page.tsx).
 * La tarjeta del resultado vive en claridad.ts. */
import type { PorIdioma } from "../config";

const es = {
  errores: {
    conexionCortadaRef:
      "La conexión se cortó antes de terminar. Tu texto sigue aquí; intenta de nuevo (referencia {{id}}).",
    sinId: "sin id",
    atorado: "algo se atoró; intenta de nuevo",
    cortadaAMedioCamino: "la conexión se cortó a medio camino; tu texto sigue aquí, intenta de nuevo",
    tardando: "esto está tardando más de lo normal; tu texto sigue aquí, intenta de nuevo",
    sinConexion: "no pudimos conectar; revisa tu internet e intenta de nuevo",
  },
  irAMisIdeas: "Ir a mis ideas",
  organizando: "Organizando tu idea…",
  etiquetaChispa: "Nueva idea · La Chispa",
  cuentameTuIdea: "Cuéntame tu idea",
  subtitulo: "Escríbela o díctala tal como la tienes en mente. Ese es todo el requisito.",
  placeholder: "Quiero vender café de especialidad a domicilio en mi barrio…",
  intentarDeNuevo: "Intentar de nuevo",
  sinPlantillas: "Sin plantillas ni formularios. Solo tu idea, en tus palabras.",
  continuar: "Continuar",
};

const en: typeof es = {
  errores: {
    conexionCortadaRef:
      "The connection dropped before we could finish. Your text is still here; try again (reference {{id}}).",
    sinId: "no id",
    atorado: "something got stuck; try again",
    cortadaAMedioCamino: "the connection dropped halfway through; your text is still here, try again",
    tardando: "this is taking longer than usual; your text is still here, try again",
    sinConexion: "we couldn't connect; check your internet connection and try again",
  },
  irAMisIdeas: "Go to my ideas",
  organizando: "Organizing your idea…",
  etiquetaChispa: "New idea · The Spark",
  cuentameTuIdea: "Tell me your idea",
  subtitulo: "Type it or dictate it just as you have it in mind. That's all it takes.",
  placeholder: "I want to deliver specialty coffee to homes in my neighborhood…",
  intentarDeNuevo: "Try again",
  sinPlantillas: "No templates or forms. Just your idea, in your own words.",
  continuar: "Continue",
};

const fr: typeof es = {
  errores: {
    conexionCortadaRef: "La connexion a été coupée avant la fin. Ton texte est toujours ici; réessaie (référence {{id}}).",
    sinId: "sans id",
    atorado: "quelque chose a coincé; réessaie",
    cortadaAMedioCamino: "la connexion a été coupée en cours de route; ton texte est toujours ici, réessaie",
    tardando: "ça prend plus de temps que d'habitude; ton texte est toujours ici, réessaie",
    sinConexion: "nous n'avons pas pu nous connecter; vérifie ta connexion Internet et réessaie",
  },
  irAMisIdeas: "Aller à mes idées",
  organizando: "J'organise ton idée…",
  etiquetaChispa: "Nouvelle idée · L'Étincelle",
  cuentameTuIdea: "Raconte-moi ton idée",
  subtitulo: "Écris-la ou dicte-la telle que tu l'as en tête. C'est tout ce qu'il faut.",
  placeholder: "Je veux livrer du café de spécialité à domicile dans mon quartier…",
  intentarDeNuevo: "Réessayer",
  sinPlantillas: "Sans modèles ni formulaires. Juste ton idée, avec tes mots.",
  continuar: "Continuer",
};

const pt: typeof es = {
  errores: {
    conexionCortadaRef: "A conexão caiu antes de terminar. Seu texto continua aqui; tente de novo (referência {{id}}).",
    sinId: "sem id",
    atorado: "algo travou; tente de novo",
    cortadaAMedioCamino: "a conexão caiu no meio do caminho; seu texto continua aqui, tente de novo",
    tardando: "isto está demorando mais que o normal; seu texto continua aqui, tente de novo",
    sinConexion: "não conseguimos conectar; confira sua internet e tente de novo",
  },
  irAMisIdeas: "Ir para minhas ideias",
  organizando: "Organizando sua ideia…",
  etiquetaChispa: "Nova ideia · A Faísca",
  cuentameTuIdea: "Me conte sua ideia",
  subtitulo: "Escreva ou dite do jeito que ela está na sua cabeça. Só isso já basta.",
  placeholder: "Quero vender café especial com entrega em domicílio no meu bairro…",
  intentarDeNuevo: "Tentar de novo",
  sinPlantillas: "Sem modelos nem formulários. Só sua ideia, com suas palavras.",
  continuar: "Continuar",
};

const de: typeof es = {
  errores: {
    conexionCortadaRef: "Die Verbindung ist abgebrochen, bevor alles fertig war. Dein Text ist noch da; versuch es noch einmal (Referenz {{id}}).",
    sinId: "keine ID",
    atorado: "etwas hat gehakt; versuch es noch einmal",
    cortadaAMedioCamino: "die Verbindung ist mittendrin abgebrochen; dein Text ist noch da, versuch es noch einmal",
    tardando: "das dauert länger als üblich; dein Text ist noch da, versuch es noch einmal",
    sinConexion: "wir konnten keine Verbindung herstellen; prüf deine Internetverbindung und versuch es noch einmal",
  },
  irAMisIdeas: "Zu meinen Ideen",
  organizando: "Deine Idee wird geordnet…",
  etiquetaChispa: "Neue Idee · Der Funke",
  cuentameTuIdea: "Erzähl mir deine Idee",
  subtitulo: "Schreib oder diktiere sie so, wie du sie im Kopf hast. Mehr braucht es nicht.",
  placeholder: "Ich möchte in meinem Viertel Spezialitätenkaffee nach Hause liefern…",
  intentarDeNuevo: "Noch einmal versuchen",
  sinPlantillas: "Keine Vorlagen, keine Formulare. Nur deine Idee, in deinen Worten.",
  continuar: "Weiter",
};

const it: typeof es = {
  errores: {
    conexionCortadaRef: "La connessione si è interrotta prima della fine. Il tuo testo è ancora qui; riprova (riferimento {{id}}).",
    sinId: "senza id",
    atorado: "qualcosa si è inceppato; riprova",
    cortadaAMedioCamino: "la connessione si è interrotta a metà; il tuo testo è ancora qui, riprova",
    tardando: "ci sta mettendo più del solito; il tuo testo è ancora qui, riprova",
    sinConexion: "non siamo riusciti a connetterci; controlla la connessione e riprova",
  },
  irAMisIdeas: "Vai alle mie idee",
  organizando: "Sto organizzando la tua idea…",
  etiquetaChispa: "Nuova idea · La Scintilla",
  cuentameTuIdea: "Raccontami la tua idea",
  subtitulo: "Scrivila o dettala così come ce l'hai in mente. Non serve altro.",
  placeholder: "Voglio vendere caffè di specialità a domicilio nel mio quartiere…",
  intentarDeNuevo: "Riprova",
  sinPlantillas: "Niente modelli né moduli. Solo la tua idea, con parole tue.",
  continuar: "Continua",
};

const ja: typeof es = {
  errores: {
    conexionCortadaRef: "処理が終わる前に接続が切れました。入力した文章は残っています。もう一度お試しください（参照番号 {{id}}）。",
    sinId: "IDなし",
    atorado: "うまく処理できませんでした。もう一度お試しください",
    cortadaAMedioCamino: "途中で接続が切れました。入力した文章は残っているので、もう一度お試しください",
    tardando: "いつもより時間がかかっています。入力した文章は残っているので、もう一度お試しください",
    sinConexion: "接続できませんでした。インターネット接続を確認して、もう一度お試しください",
  },
  irAMisIdeas: "アイデア一覧へ",
  organizando: "アイデアを整理しています…",
  etiquetaChispa: "新しいアイデア · ひらめき",
  cuentameTuIdea: "アイデアを聞かせてください",
  subtitulo: "頭の中にあるまま、書くか話してください。必要なのはそれだけです。",
  placeholder: "近所でスペシャルティコーヒーの宅配をしたい…",
  intentarDeNuevo: "もう一度試す",
  sinPlantillas: "テンプレートもフォームもいりません。自分の言葉で、アイデアをそのまま。",
  continuar: "続ける",
};

const zh: typeof es = {
  errores: {
    conexionCortadaRef: "连接在完成前中断了。你的文字还在这里，请再试一次（参考编号 {{id}}）。",
    sinId: "无编号",
    atorado: "出了点状况，请再试一次",
    cortadaAMedioCamino: "连接中途断开了；你的文字还在这里，请再试一次",
    tardando: "这次比平时慢；你的文字还在这里，请再试一次",
    sinConexion: "没能连接上，请检查网络后再试一次",
  },
  irAMisIdeas: "前往我的想法",
  organizando: "正在整理你的想法…",
  etiquetaChispa: "新想法 · 灵光一闪",
  cuentameTuIdea: "告诉我你的想法",
  subtitulo: "按你脑子里的样子写下来，或者说出来。只需要这些。",
  placeholder: "我想在我住的小区做精品咖啡外送…",
  intentarDeNuevo: "再试一次",
  sinPlantillas: "没有模板，也没有表单。只有你的想法，用你自己的话。",
  continuar: "继续",
};

const ko: typeof es = {
  errores: {
    conexionCortadaRef: "끝나기 전에 연결이 끊겼어요. 쓰신 내용은 그대로 있으니 다시 시도해 주세요(참조 번호 {{id}}).",
    sinId: "ID 없음",
    atorado: "문제가 생겼어요. 다시 시도해 주세요",
    cortadaAMedioCamino: "도중에 연결이 끊겼어요. 쓰신 내용은 그대로 있으니 다시 시도해 주세요",
    tardando: "평소보다 오래 걸리고 있어요. 쓰신 내용은 그대로 있으니 다시 시도해 주세요",
    sinConexion: "연결하지 못했어요. 인터넷 연결을 확인하고 다시 시도해 주세요",
  },
  irAMisIdeas: "내 아이디어로 가기",
  organizando: "아이디어를 정리하는 중…",
  etiquetaChispa: "새 아이디어 · 불꽃",
  cuentameTuIdea: "아이디어를 들려주세요",
  subtitulo: "머릿속에 있는 그대로 쓰거나 말해 주세요. 그거면 충분해요.",
  placeholder: "우리 동네에 스페셜티 커피를 배달하고 싶어요…",
  intentarDeNuevo: "다시 시도",
  sinPlantillas: "템플릿도, 양식도 없어요. 내 말로 쓴 아이디어면 돼요.",
  continuar: "계속",
};

const ar: typeof es = {
  errores: {
    conexionCortadaRef: "انقطع الاتصال قبل أن ننتهي. نصّكم ما زال هنا؛ حاولوا مرة أخرى (المرجع {{id}}).",
    sinId: "بلا معرّف",
    atorado: "تعثّر شيء ما؛ حاولوا مرة أخرى",
    cortadaAMedioCamino: "انقطع الاتصال في منتصف الطريق؛ نصّكم ما زال هنا، حاولوا مرة أخرى",
    tardando: "يستغرق هذا وقتًا أطول من المعتاد؛ نصّكم ما زال هنا، حاولوا مرة أخرى",
    sinConexion: "تعذّر الاتصال؛ تحقّقوا من الإنترنت وحاولوا مرة أخرى",
  },
  irAMisIdeas: "الانتقال إلى أفكاري",
  organizando: "جارٍ ترتيب فكرتكم…",
  etiquetaChispa: "فكرة جديدة · الشرارة",
  cuentameTuIdea: "حدّثوني عن فكرتكم",
  subtitulo: "اكتبوها أو أملوها كما هي في أذهانكم. هذا كل المطلوب.",
  placeholder: "أريد بيع قهوة مختصة مع التوصيل إلى المنازل في حيّي…",
  intentarDeNuevo: "المحاولة مرة أخرى",
  sinPlantillas: "بلا قوالب ولا استمارات. فقط فكرتكم، بكلماتكم.",
  continuar: "متابعة",
};

const hi: typeof es = {
  errores: {
    conexionCortadaRef: "काम पूरा होने से पहले कनेक्शन टूट गया। आपका लिखा यहीं है; फिर से कोशिश करें (संदर्भ {{id}})।",
    sinId: "कोई id नहीं",
    atorado: "कुछ अटक गया; फिर से कोशिश करें",
    cortadaAMedioCamino: "कनेक्शन बीच में ही टूट गया; आपका लिखा यहीं है, फिर से कोशिश करें",
    tardando: "इसमें सामान्य से ज़्यादा समय लग रहा है; आपका लिखा यहीं है, फिर से कोशिश करें",
    sinConexion: "हम कनेक्ट नहीं कर पाए; अपना इंटरनेट जाँचें और फिर से कोशिश करें",
  },
  irAMisIdeas: "मेरे विचारों पर जाएँ",
  organizando: "आपका विचार व्यवस्थित हो रहा है…",
  etiquetaChispa: "नया विचार · चिंगारी",
  cuentameTuIdea: "मुझे अपना विचार बताइए",
  subtitulo: "इसे वैसे ही लिखें या बोलकर लिखवाएँ, जैसा आपके मन में है। बस इतना ही चाहिए।",
  placeholder: "मेरा विचार: अपने मोहल्ले में घर-घर स्पेशलिटी कॉफ़ी पहुँचाना…",
  intentarDeNuevo: "फिर से कोशिश करें",
  sinPlantillas: "न टेम्पलेट, न फ़ॉर्म। सिर्फ़ आपका विचार, आपके शब्दों में।",
  continuar: "आगे बढ़ें",
};

export const NUEVA_IDEA: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
