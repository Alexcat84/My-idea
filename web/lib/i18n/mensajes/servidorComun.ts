/** Mensajes compartidos del servidor: los que arman lib/mensajeServidor.ts,
 * lib/constants.ts, lib/rateLimit.ts, lib/creditos.ts, lib/seguridad.ts y
 * lib/identidad.ts, y que muchas rutas devuelven en `error`. */
import type { PorIdioma } from "../config";

const es = {
  /** lib/mensajeServidor.ts: el genérico, solo cuando el servidor no dio razón. */
  errorGenerico: "algo se atoró de nuestro lado; intenta de nuevo en un momento",
  /** lib/constants.ts */
  textoLargo: "Tu texto pasa de {{limite}} caracteres. Recórtalo un poco y seguimos.",
  ideaLarga: "Tu idea pasa de 12.000 caracteres. Recórtala un poco y seguimos.",
  adopcionPendiente:
    "Algunas ideas que escribiste antes de entrar todavía no llegan a tu cuenta. Lo reintento cada vez que entras; no se perdió nada.",
  /** lib/rateLimit.ts */
  limiteDiario:
    "Por hoy alcanzaste el límite de la beta ({{arranques}} al día). Tus ideas quedan guardadas. Vuelve mañana y seguimos donde quedamos.",
  arranques: { one: "{{n}} arranque", other: "{{n}} arranques" },
  fusible: "Estamos a capacidad por hoy; tus ideas te esperan mañana.",
  servicioNoDisponible: "Servicio temporalmente no disponible. No se te cobró nada; intenta de nuevo en unos minutos.",
  /** lib/creditos.ts: el 402 en palabras de persona. */
  saldoInsuficiente: "Te quedan {{creditos}}; esto cuesta {{costo}}. Tu trabajo queda guardado tal como está.",
  saldoInsuficienteConApartados:
    "Tienes {{creditos}} y {{apartados}} para un plan que tienes en curso; esto cuesta {{costo}}. Tu trabajo queda guardado tal como está.",
  creditos: { one: "{{n}} crédito", other: "{{n}} créditos" },
  apartados: { one: "{{n}} ya está apartado", other: "{{n}} ya están apartados" },
  /** lib/seguridad.ts: el 403 de frontera del segundo factor. */
  aviso2FA: "Tu cuenta tiene verificación en dos pasos. Confirma tu segundo factor y seguimos justo donde quedaste.",
  /** lib/identidad.ts: el 401 de frontera. */
  avisoLogin: "Para explorar tu idea necesitas tu cuenta. Entra con tu correo y seguimos justo donde quedaste.",
};

const en: typeof es = {
  errorGenerico: "something got stuck on our end; try again in a moment",
  textoLargo: "Your text is over {{limite}} characters. Trim it a little and we'll keep going.",
  ideaLarga: "Your idea is over 12,000 characters. Trim it a little and we'll keep going.",
  adopcionPendiente:
    "Some ideas you wrote before logging in haven't reached your account yet. I retry every time you log in; nothing was lost.",
  limiteDiario:
    "You've reached today's beta limit ({{arranques}} a day). Your ideas are saved. Come back tomorrow and we'll pick up where we left off.",
  arranques: { one: "{{n}} start", other: "{{n}} starts" },
  fusible: "We're at capacity for today; your ideas will be waiting for you tomorrow.",
  servicioNoDisponible: "Service temporarily unavailable. You weren't charged anything; please try again in a few minutes.",
  saldoInsuficiente: "You have {{creditos}} left; this costs {{costo}}. Your work is saved just as it is.",
  saldoInsuficienteConApartados:
    "You have {{creditos}}, and {{apartados}} for a plan you have in progress; this costs {{costo}}. Your work is saved just as it is.",
  creditos: { one: "{{n}} credit", other: "{{n}} credits" },
  apartados: { one: "{{n}} is already set aside", other: "{{n}} are already set aside" },
  aviso2FA: "Your account has two-step verification. Confirm your second factor and we'll pick up right where you left off.",
  avisoLogin: "To explore your idea, you need your account. Log in with your email and we'll pick up right where you left off.",
};

const fr: typeof es = {
  errorGenerico: "quelque chose a coincé de notre côté; réessaie dans un moment",
  textoLargo: "Ton texte dépasse {{limite}} caractères. Raccourcis-le un peu et on continue.",
  ideaLarga: "Ton idée dépasse 12 000 caractères. Raccourcis-la un peu et on continue.",
  adopcionPendiente: "Certaines idées que tu as écrites avant de te connecter ne sont pas encore arrivées dans ton compte. Je réessaie chaque fois que tu te connectes; rien n'est perdu.",
  limiteDiario: "Pour aujourd'hui, tu as atteint la limite de la bêta ({{arranques}} par jour). Tes idées sont enregistrées. Reviens demain et on reprendra là où tu en étais.",
  arranques: {
    one: "{{n}} démarrage",
    other: "{{n}} démarrages",
  },
  fusible: "Nous sommes à pleine capacité pour aujourd'hui; tes idées t'attendent demain.",
  servicioNoDisponible: "Service temporairement indisponible. Rien ne t'a été facturé; réessaie dans quelques minutes.",
  saldoInsuficiente: "Il te reste {{creditos}}; ceci coûte {{costo}}. Ton travail est enregistré tel quel.",
  saldoInsuficienteConApartados: "Tu as {{creditos}}, et {{apartados}} pour un plan en cours; ceci coûte {{costo}}. Ton travail est enregistré tel quel.",
  creditos: {
    one: "{{n}} crédit",
    other: "{{n}} crédits",
  },
  apartados: {
    one: "{{n}} est déjà réservé",
    other: "{{n}} sont déjà réservés",
  },
  aviso2FA: "Ton compte utilise la vérification en deux étapes. Confirme ta deuxième étape et on reprend exactement là où tu en étais.",
  avisoLogin: "Pour explorer ton idée, il te faut ton compte. Connecte-toi avec ton courriel et on reprend exactement là où tu en étais.",
};

const pt: typeof es = {
  errorGenerico: "algo travou do nosso lado; tente de novo daqui a pouco",
  textoLargo: "Seu texto passa de {{limite}} caracteres. Encurte um pouco e seguimos.",
  ideaLarga: "Sua ideia passa de 12.000 caracteres. Encurte um pouco e seguimos.",
  adopcionPendiente: "Algumas ideias que você escreveu antes de entrar ainda não chegaram à sua conta. Tento de novo toda vez que você entra; nada se perdeu.",
  limiteDiario: "Por hoje você chegou ao limite da versão beta ({{arranques}} por dia). Suas ideias ficam salvas. Volte amanhã e seguimos de onde paramos.",
  arranques: {
    one: "{{n}} início",
    other: "{{n}} inícios",
  },
  fusible: "Estamos no limite da capacidade por hoje; suas ideias esperam você amanhã.",
  servicioNoDisponible: "Serviço temporariamente indisponível. Nada foi cobrado de você; tente de novo em alguns minutos.",
  saldoInsuficiente: "Você ainda tem {{creditos}}; isto custa {{costo}}. Seu trabalho fica salvo do jeito que está.",
  saldoInsuficienteConApartados: "Você tem {{creditos}}, e {{apartados}} para um plano que está em andamento; isto custa {{costo}}. Seu trabalho fica salvo do jeito que está.",
  creditos: {
    one: "{{n}} crédito",
    other: "{{n}} créditos",
  },
  apartados: {
    one: "{{n}} já está reservado",
    other: "{{n}} já estão reservados",
  },
  aviso2FA: "Sua conta tem verificação em duas etapas. Confirme seu segundo fator e seguimos exatamente de onde você parou.",
  avisoLogin: "Para explorar sua ideia, você precisa da sua conta. Entre com seu e-mail e seguimos exatamente de onde você parou.",
};

const de: typeof es = {
  errorGenerico: "bei uns hat etwas gehakt; versuch es gleich noch einmal",
  textoLargo: "Dein Text ist länger als {{limite}} Zeichen. Kürz ihn ein bisschen, dann machen wir weiter.",
  ideaLarga: "Deine Idee ist länger als 12.000 Zeichen. Kürz sie ein bisschen, dann machen wir weiter.",
  adopcionPendiente: "Ein paar Ideen, die du vor der Anmeldung geschrieben hast, sind noch nicht in deinem Konto angekommen. Ich versuche es bei jeder Anmeldung erneut; nichts ist verloren.",
  limiteDiario: "Für heute hast du das Beta-Limit erreicht ({{arranques}} pro Tag). Deine Ideen sind gespeichert. Komm morgen wieder, dann machen wir da weiter, wo wir aufgehört haben.",
  arranques: {
    one: "{{n}} Start",
    other: "{{n}} Starts",
  },
  fusible: "Für heute sind wir ausgelastet; deine Ideen warten morgen auf dich.",
  servicioNoDisponible: "Dienst vorübergehend nicht verfügbar. Dir wurde nichts berechnet; versuch es in ein paar Minuten noch einmal.",
  saldoInsuficiente: "Du hast noch {{creditos}}; das hier kostet {{costo}}. Deine Arbeit bleibt genau so gespeichert, wie sie ist.",
  saldoInsuficienteConApartados: "Du hast {{creditos}}, und {{apartados}} für einen Plan, der gerade läuft; das hier kostet {{costo}}. Deine Arbeit bleibt genau so gespeichert, wie sie ist.",
  creditos: {
    one: "{{n}} Punkt",
    other: "{{n}} Punkte",
  },
  apartados: {
    one: "{{n}} ist schon reserviert",
    other: "{{n}} sind schon reserviert",
  },
  aviso2FA: "Dein Konto hat eine Bestätigung in zwei Schritten. Bestätige deinen zweiten Faktor, dann machen wir genau da weiter, wo du aufgehört hast.",
  avisoLogin: "Um deine Idee zu erkunden, brauchst du dein Konto. Melde dich mit deiner E-Mail-Adresse an, dann machen wir genau da weiter, wo du aufgehört hast.",
};

const it: typeof es = {
  errorGenerico: "qualcosa si è inceppato da parte nostra; riprova tra un momento",
  textoLargo: "Il tuo testo supera i {{limite}} caratteri. Accorcialo un po' e andiamo avanti.",
  ideaLarga: "La tua idea supera i 12.000 caratteri. Accorciala un po' e andiamo avanti.",
  adopcionPendiente: "Alcune idee che hai scritto prima di accedere non sono ancora arrivate al tuo account. Ci riprovo ogni volta che accedi; non è andato perso niente.",
  limiteDiario: "Per oggi hai raggiunto il limite della beta ({{arranques}} al giorno). Le tue idee restano salvate. Torna domani e riprendiamo da dove avevi lasciato.",
  arranques: {
    one: "{{n}} avvio",
    other: "{{n}} avvii",
  },
  fusible: "Per oggi siamo al completo; le tue idee ti aspettano domani.",
  servicioNoDisponible: "Servizio temporaneamente non disponibile. Non ti è stato addebitato nulla; riprova tra qualche minuto.",
  saldoInsuficiente: "Ti restano {{creditos}}; questo costa {{costo}}. Il tuo lavoro resta salvato così com'è.",
  saldoInsuficienteConApartados: "Hai {{creditos}}, e {{apartados}} per un piano che hai in corso; questo costa {{costo}}. Il tuo lavoro resta salvato così com'è.",
  creditos: {
    one: "{{n}} credito",
    other: "{{n}} crediti",
  },
  apartados: {
    one: "{{n}} è già accantonato",
    other: "{{n}} sono già accantonati",
  },
  aviso2FA: "Il tuo account ha la verifica in due passaggi. Conferma il tuo secondo fattore e riprendiamo esattamente da dove avevi lasciato.",
  avisoLogin: "Per esplorare la tua idea ti serve il tuo account. Accedi con la tua email e riprendiamo esattamente da dove avevi lasciato.",
};

const ja: typeof es = {
  errorGenerico: "こちらで問題が起きました。少ししてから、もう一度お試しください",
  textoLargo: "テキストが{{limite}}文字を超えています。少し短くしていただければ、続けられます。",
  ideaLarga: "アイデアが12,000文字を超えています。少し短くしていただければ、続けられます。",
  adopcionPendiente: "ログイン前に書いたアイデアのうち、まだアカウントに届いていないものがあります。ログインのたびに再試行しています。失われたものはありません。",
  limiteDiario: "今日のベータ版の上限（1日{{arranques}}）に達しました。アイデアは保存されています。明日また来ていただければ、続きから再開します。",
  arranques: {
    one: "{{n}}回",
    other: "{{n}}回",
  },
  fusible: "今日は利用が上限に達しています。アイデアは保存されているので、また明日お越しください。",
  servicioNoDisponible: "サービスは一時的に利用できません。料金は一切かかっていません。数分後にもう一度お試しください。",
  saldoInsuficiente: "残りは{{creditos}}で、これには{{costo}}必要です。作業内容はそのまま保存されています。",
  saldoInsuficienteConApartados: "残りは{{creditos}}です（進行中のプラン用に{{apartados}}）。これには{{costo}}必要です。作業内容はそのまま保存されています。",
  creditos: {
    one: "{{n}}ポイント",
    other: "{{n}}ポイント",
  },
  apartados: {
    one: "{{n}}ポイントを確保済み",
    other: "{{n}}ポイントを確保済み",
  },
  aviso2FA: "このアカウントでは2段階認証が有効です。2つ目の確認を済ませれば、中断したところからそのまま続けられます。",
  avisoLogin: "アイデアを探っていくには、アカウントが必要です。メールアドレスでログインすれば、中断したところからそのまま続けられます。",
};

const zh: typeof es = {
  errorGenerico: "我们这边出了点问题，请稍后再试",
  textoLargo: "你的文字超过了{{limite}}个字符。稍微删减一些，我们再继续。",
  ideaLarga: "你的想法超过了12,000个字符。稍微删减一些，我们再继续。",
  adopcionPendiente: "你登录前写下的一些想法还没同步到你的账户。每次你登录，我都会重试；什么都没丢。",
  limiteDiario: "你今天已达到测试版的上限（每天{{arranques}}）。你的想法都已保存。明天再来，我们从上次停下的地方继续。",
  arranques: {
    one: "{{n}}次启动",
    other: "{{n}}次启动",
  },
  fusible: "今天我们的容量已满；你的想法明天在这里等你。",
  servicioNoDisponible: "服务暂时不可用。没有向你收取任何费用；请几分钟后再试。",
  saldoInsuficiente: "你还剩{{creditos}}；这次需要{{costo}}。你的工作已原样保存。",
  saldoInsuficienteConApartados: "你有{{creditos}}，另有{{apartados}}给你进行中的一个计划；这次需要{{costo}}。你的工作已原样保存。",
  creditos: {
    one: "{{n}}点",
    other: "{{n}}点",
  },
  apartados: {
    one: "{{n}}点已预留",
    other: "{{n}}点已预留",
  },
  aviso2FA: "你的账户开启了两步验证。完成第二步验证后，我们就从你刚才停下的地方继续。",
  avisoLogin: "要探索你的想法，需要登录你的账户。用你的邮箱登录，我们就从你刚才停下的地方继续。",
};

const ko: typeof es = {
  errorGenerico: "저희 쪽에서 문제가 생겼어요. 잠시 후 다시 시도해 주세요",
  textoLargo: "글이 {{limite}}자를 넘었어요. 조금만 줄이면 계속할 수 있어요.",
  ideaLarga: "아이디어가 12,000자를 넘었어요. 조금만 줄이면 계속할 수 있어요.",
  adopcionPendiente: "로그인 전에 쓴 아이디어 중 일부가 아직 계정에 옮겨지지 않았어요. 로그인할 때마다 다시 시도하고 있어요. 잃어버린 건 없어요.",
  limiteDiario: "오늘 베타 이용 한도(하루 {{arranques}})에 도달했어요. 아이디어는 저장돼 있어요. 내일 다시 오면 멈춘 곳부터 이어 갈게요.",
  arranques: {
    one: "{{n}}회 시작",
    other: "{{n}}회 시작",
  },
  fusible: "오늘은 이용량이 가득 찼어요. 아이디어는 내일도 그대로 기다리고 있어요.",
  servicioNoDisponible: "서비스를 잠시 이용할 수 없어요. 요금은 전혀 청구되지 않았어요. 몇 분 뒤에 다시 시도해 주세요.",
  saldoInsuficiente: "지금 남은 건 {{creditos}}이고, 이 작업에는 {{costo}}크레딧이 필요해요. 작업은 지금 상태 그대로 저장돼 있어요.",
  saldoInsuficienteConApartados: "지금 쓸 수 있는 건 {{creditos}}이고, 진행 중인 계획을 위해 {{apartados}}. 이 작업에는 {{costo}}크레딧이 필요해요. 작업은 지금 상태 그대로 저장돼 있어요.",
  creditos: {
    one: "{{n}}크레딧",
    other: "{{n}}크레딧",
  },
  apartados: {
    one: "{{n}}크레딧은 이미 따로 떼어 두었어요",
    other: "{{n}}크레딧은 이미 따로 떼어 두었어요",
  },
  aviso2FA: "계정에 2단계 인증이 켜져 있어요. 두 번째 인증을 확인하면 멈춘 곳에서 바로 이어 갈게요.",
  avisoLogin: "아이디어를 탐색하려면 계정이 필요해요. 이메일로 로그인하면 멈춘 곳에서 바로 이어 갈게요.",
};

const ar: typeof es = {
  errorGenerico: "تعثّر شيء ما من جهتنا؛ حاولوا مجددًا بعد لحظة",
  textoLargo: "نصّكم يتجاوز الحد الأقصى للأحرف ({{limite}}). اختصروه قليلًا ونكمل.",
  ideaLarga: "فكرتكم تتجاوز 12,000 حرف. اختصروها قليلًا ونكمل.",
  adopcionPendiente: "بعض الأفكار التي كتبتموها قبل تسجيل الدخول لم تصل بعد إلى حسابكم. أعيد المحاولة في كل مرة تدخلون فيها؛ لم يضع شيء.",
  limiteDiario: "بلغتم لهذا اليوم حدّ النسخة التجريبية ({{arranques}} في اليوم). أفكاركم محفوظة. عودوا غدًا ونكمل من حيث توقفنا.",
  arranques: {
    one: "مرات البدء: {{n}}",
    other: "مرات البدء: {{n}}",
  },
  fusible: "بلغنا طاقتنا القصوى لهذا اليوم؛ أفكاركم بانتظاركم غدًا.",
  servicioNoDisponible: "الخدمة غير متاحة مؤقتًا. لم يُخصم منكم أي شيء؛ حاولوا مرة أخرى بعد بضع دقائق.",
  saldoInsuficiente: "رصيدكم المتبقي {{creditos}}، وتكلفة هذا {{costo}}. عملكم محفوظ كما هو.",
  saldoInsuficienteConApartados: "لديكم {{creditos}} ({{apartados}} لخطة قيد الإنجاز)، وتكلفة هذا {{costo}}. عملكم محفوظ كما هو.",
  creditos: {
    one: "{{n}} نقطة",
    other: "{{n}} من النقاط",
  },
  apartados: {
    one: "المحجوز منها بالفعل: {{n}}",
    other: "المحجوز منها بالفعل: {{n}}",
  },
  aviso2FA: "حسابكم محمي بالتحقق بخطوتين. أكّدوا الخطوة الثانية ونكمل تمامًا من حيث توقفتم.",
  avisoLogin: "لاستكشاف فكرتكم تحتاجون إلى حسابكم. ادخلوا ببريدكم الإلكتروني ونكمل تمامًا من حيث توقفتم.",
};

const hi: typeof es = {
  errorGenerico: "हमारी तरफ़ कुछ अटक गया; थोड़ी देर में फिर कोशिश करें",
  textoLargo: "आपका टेक्स्ट {{limite}} अक्षरों से ज़्यादा है। इसे थोड़ा छोटा करें, फिर आगे बढ़ते हैं।",
  ideaLarga: "आपका विचार 12,000 अक्षरों से ज़्यादा है। इसे थोड़ा छोटा करें, फिर आगे बढ़ते हैं।",
  adopcionPendiente: "लॉग इन से पहले लिखे आपके कुछ विचार अभी आपके खाते तक नहीं पहुँचे हैं। हर बार लॉग इन करने पर इन्हें फिर से लाने की कोशिश होती है; कुछ भी खोया नहीं है।",
  limiteDiario: "आज के लिए बीटा की सीमा पूरी हो गई है (दिन में {{arranques}})। आपके विचार सहेजे हुए हैं। कल लौटें, वहीं से आगे बढ़ेंगे जहाँ आपने छोड़ा था।",
  arranques: {
    one: "{{n}} शुरुआत",
    other: "{{n}} शुरुआतें",
  },
  fusible: "आज के लिए हमारी क्षमता पूरी हो गई है; आपके विचार कल आपका इंतज़ार करेंगे।",
  servicioNoDisponible: "सेवा अस्थायी रूप से उपलब्ध नहीं है। आपसे कुछ भी नहीं लिया गया; कुछ मिनट बाद फिर से कोशिश करें।",
  saldoInsuficiente: "आपका बैलेंस {{creditos}} है; इसके लिए {{costo}} क्रेडिट चाहिए। आपका काम जैसा है, वैसा ही सहेजा हुआ है।",
  saldoInsuficienteConApartados: "आपका बैलेंस {{creditos}} है, और आपकी चालू योजना के लिए {{apartados}}; इसके लिए {{costo}} क्रेडिट चाहिए। आपका काम जैसा है, वैसा ही सहेजा हुआ है।",
  creditos: {
    one: "{{n}} क्रेडिट",
    other: "{{n}} क्रेडिट",
  },
  apartados: {
    one: "{{n}} पहले से अलग रखा है",
    other: "{{n}} पहले से अलग रखे हैं",
  },
  aviso2FA: "आपके खाते में दो-चरणीय सत्यापन चालू है। दूसरे चरण की पुष्टि करें, फिर वहीं से आगे बढ़ते हैं जहाँ आपने छोड़ा था।",
  avisoLogin: "अपने विचार की पड़ताल के लिए आपको अपना खाता चाहिए। अपने ईमेल से लॉग इन करें, फिर वहीं से आगे बढ़ते हैं जहाँ आपने छोड़ा था।",
};

export const SERVIDOR_COMUN: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
