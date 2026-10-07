/**
 * El consentimiento legal versionado (decisión del fundador, 7 oct 2026): el modal de app/ui/ConsentimientoLegal.tsx,
 * los enlaces de /login a los Términos y la Privacidad, y los mensajes de /api/cuenta/consentimiento. Solo lo ven las
 * cuentas reales, nunca la identidad invisible. Los textos legales existen en español y francés: los demás idiomas
 * lo dicen (`soloEsFr`).
 */
import type { PorIdioma } from "../config";

const es = {
  tituloPrimera: "Antes de seguir con tu cuenta",
  tituloNueva: "Actualizamos los Términos y la Privacidad",
  introPrimera:
    "Lee los <terminos>Términos de uso</terminos> y la <privacidad>Política de privacidad</privacidad> de My Idea. Para usar tu cuenta, necesitamos que los aceptes. Guardamos la versión que aceptas y su fecha.",
  introNueva:
    "Los textos cambiaron desde la última vez que los aceptaste. Lee los <terminos>Términos de uso</terminos> y la <privacidad>Política de privacidad</privacidad>, y acepta la versión nueva para seguir con tu cuenta.",
  soloEsFr: "Estos textos están disponibles en español y en francés.",
  version: "Versión del {{version}}",
  casilla: "Leí y acepto los Términos de uso y la Política de privacidad.",
  aceptar: "Aceptar y seguir",
  guardando: "Guardando…",
  salir: "Ahora no, salir de mi cuenta",
  borrar: "Prefiero borrar mi cuenta",
  errorGuardar: "No pudimos guardar tu aceptación, así que todavía no cuenta. Inténtalo de nuevo.",
  errorEstado: "No pudimos comprobar si ya aceptaste la versión vigente. Si quieres seguir con tu cuenta, acéptala aquí.",
  versionCambio: "Los textos cambiaron mientras los leías. Revisa la versión nueva y acéptala.",
  login: {
    enlaces: "<terminos>Términos</terminos> · <privacidad>Privacidad</privacidad>",
    aviso: "Al crear tu cuenta te pediremos que aceptes los Términos de uso y la Política de privacidad.",
  },
  servidor: {
    necesitasCuenta: "Para aceptar los Términos y la Privacidad necesitas entrar con tu cuenta.",
    cuerpoInvalido: "No entendimos la petición. Inténtalo de nuevo.",
    noLeido: "No pudimos comprobar tu aceptación de los Términos y la Privacidad. Inténtalo de nuevo en un momento.",
    noGuardado: "No pudimos guardar tu aceptación, así que todavía no cuenta. Inténtalo de nuevo.",
    versionVieja: "Los textos cambiaron mientras los leías. Revisa la versión nueva y acéptala.",
  },
};

const en: typeof es = {
  tituloPrimera: "Before you continue with your account",
  tituloNueva: "We updated the Terms and the Privacy policy",
  introPrimera:
    "Read the My Idea <terminos>Terms of use</terminos> and <privacidad>Privacy policy</privacidad>. To use your account, we need you to accept them. We keep the version you accept and its date.",
  introNueva:
    "The texts changed since you last accepted them. Read the <terminos>Terms of use</terminos> and the <privacidad>Privacy policy</privacidad>, and accept the new version to continue with your account.",
  soloEsFr: "These texts are available in Spanish and French.",
  version: "Version of {{version}}",
  casilla: "I have read and accept the Terms of use and the Privacy policy.",
  aceptar: "Accept and continue",
  guardando: "Saving…",
  salir: "Not now, log out of my account",
  borrar: "I'd rather delete my account",
  errorGuardar: "We couldn't save your acceptance, so it doesn't count yet. Please try again.",
  errorEstado: "We couldn't check whether you already accepted the current version. To continue with your account, accept it here.",
  versionCambio: "The texts changed while you were reading them. Review the new version and accept it.",
  login: {
    enlaces: "<terminos>Terms</terminos> · <privacidad>Privacy</privacidad>",
    aviso: "When you create your account, we'll ask you to accept the Terms of use and the Privacy policy.",
  },
  servidor: {
    necesitasCuenta: "To accept the Terms and the Privacy policy, you need to log in with your account.",
    cuerpoInvalido: "We didn't understand the request. Please try again.",
    noLeido: "We couldn't check your acceptance of the Terms and the Privacy policy. Please try again in a moment.",
    noGuardado: "We couldn't save your acceptance, so it doesn't count yet. Please try again.",
    versionVieja: "The texts changed while you were reading them. Review the new version and accept it.",
  },
};

const pt: typeof es = {
  tituloPrimera: "Antes de continuar com a sua conta",
  tituloNueva: "Atualizamos os Termos e a Privacidade",
  introPrimera:
    "Leia os <terminos>Termos de uso</terminos> e a <privacidad>Política de privacidade</privacidad> do My Idea. Para usar a sua conta, precisamos que você os aceite. Guardamos a versão que você aceita e a data.",
  introNueva:
    "Os textos mudaram desde a última vez que você os aceitou. Leia os <terminos>Termos de uso</terminos> e a <privacidad>Política de privacidade</privacidad> e aceite a nova versão para continuar com a sua conta.",
  soloEsFr: "Estes textos estão disponíveis em espanhol e em francês.",
  version: "Versão de {{version}}",
  casilla: "Li e aceito os Termos de uso e a Política de privacidade.",
  aceptar: "Aceitar e continuar",
  guardando: "Salvando…",
  salir: "Agora não, sair da minha conta",
  borrar: "Prefiro excluir minha conta",
  errorGuardar: "Não conseguimos salvar a sua aceitação, então ela ainda não vale. Tente de novo.",
  errorEstado: "Não conseguimos verificar se você já aceitou a versão vigente. Para continuar com a sua conta, aceite-a aqui.",
  versionCambio: "Os textos mudaram enquanto você os lia. Revise a nova versão e aceite-a.",
  login: {
    enlaces: "<terminos>Termos</terminos> · <privacidad>Privacidade</privacidad>",
    aviso: "Ao criar a sua conta, vamos pedir que você aceite os Termos de uso e a Política de privacidade.",
  },
  servidor: {
    necesitasCuenta: "Para aceitar os Termos e a Privacidade, você precisa entrar com a sua conta.",
    cuerpoInvalido: "Não entendemos o pedido. Tente de novo.",
    noLeido: "Não conseguimos verificar a sua aceitação dos Termos e da Privacidade. Tente de novo em um momento.",
    noGuardado: "Não conseguimos salvar a sua aceitação, então ela ainda não vale. Tente de novo.",
    versionVieja: "Os textos mudaram enquanto você os lia. Revise a nova versão e aceite-a.",
  },
};

const fr: typeof es = {
  tituloPrimera: "Avant de continuer avec ton compte",
  tituloNueva: "Nous avons mis à jour les Conditions et la Confidentialité",
  introPrimera:
    "Lis les <terminos>Conditions d'utilisation</terminos> et la <privacidad>Politique de confidentialité</privacidad> de My Idea. Pour utiliser ton compte, nous avons besoin que tu les acceptes. Nous conservons la version que tu acceptes et sa date.",
  introNueva:
    "Les textes ont changé depuis la dernière fois que tu les as acceptés. Lis les <terminos>Conditions d'utilisation</terminos> et la <privacidad>Politique de confidentialité</privacidad>, puis accepte la nouvelle version pour continuer avec ton compte.",
  soloEsFr: "Ces textes sont disponibles en espagnol et en français.",
  version: "Version du {{version}}",
  casilla: "J'ai lu et j'accepte les Conditions d'utilisation et la Politique de confidentialité.",
  aceptar: "Accepter et continuer",
  guardando: "Enregistrement…",
  salir: "Pas maintenant, me déconnecter de mon compte",
  borrar: "Je préfère supprimer mon compte",
  errorGuardar: "Nous n'avons pas pu enregistrer ton acceptation, elle ne compte donc pas encore. Réessaie.",
  errorEstado: "Nous n'avons pas pu vérifier si tu as déjà accepté la version en vigueur. Pour continuer avec ton compte, accepte-la ici.",
  versionCambio: "Les textes ont changé pendant que tu les lisais. Revois la nouvelle version et accepte-la.",
  login: {
    enlaces: "<terminos>Conditions</terminos> · <privacidad>Confidentialité</privacidad>",
    aviso: "À la création de ton compte, nous te demanderons d'accepter les Conditions d'utilisation et la Politique de confidentialité.",
  },
  servidor: {
    necesitasCuenta: "Pour accepter les Conditions et la Confidentialité, tu dois te connecter avec ton compte.",
    cuerpoInvalido: "Nous n'avons pas compris la demande. Réessaie.",
    noLeido: "Nous n'avons pas pu vérifier ton acceptation des Conditions et de la Confidentialité. Réessaie dans un instant.",
    noGuardado: "Nous n'avons pas pu enregistrer ton acceptation, elle ne compte donc pas encore. Réessaie.",
    versionVieja: "Les textes ont changé pendant que tu les lisais. Revois la nouvelle version et accepte-la.",
  },
};

const de: typeof es = {
  tituloPrimera: "Bevor du mit deinem Konto weitermachst",
  tituloNueva: "Wir haben die Nutzungsbedingungen und den Datenschutz aktualisiert",
  introPrimera:
    "Lies die <terminos>Nutzungsbedingungen</terminos> und die <privacidad>Datenschutzerklärung</privacidad> von My Idea. Damit du dein Konto nutzen kannst, musst du sie akzeptieren. Wir speichern die Version, die du akzeptierst, und ihr Datum.",
  introNueva:
    "Die Texte haben sich geändert, seit du sie zuletzt akzeptiert hast. Lies die <terminos>Nutzungsbedingungen</terminos> und die <privacidad>Datenschutzerklärung</privacidad> und akzeptiere die neue Version, um mit deinem Konto weiterzumachen.",
  soloEsFr: "Diese Texte gibt es auf Spanisch und Französisch.",
  version: "Version vom {{version}}",
  casilla: "Ich habe die Nutzungsbedingungen und die Datenschutzerklärung gelesen und akzeptiere sie.",
  aceptar: "Akzeptieren und weiter",
  guardando: "Wird gespeichert…",
  salir: "Jetzt nicht, von meinem Konto abmelden",
  borrar: "Ich möchte mein Konto lieber löschen",
  errorGuardar: "Wir konnten deine Zustimmung nicht speichern, deshalb zählt sie noch nicht. Versuch es noch einmal.",
  errorEstado: "Wir konnten nicht prüfen, ob du die aktuelle Version schon akzeptiert hast. Um mit deinem Konto weiterzumachen, akzeptiere sie hier.",
  versionCambio: "Die Texte haben sich geändert, während du sie gelesen hast. Sieh dir die neue Version an und akzeptiere sie.",
  login: {
    enlaces: "<terminos>Nutzungsbedingungen</terminos> · <privacidad>Datenschutz</privacidad>",
    aviso: "Wenn du dein Konto erstellst, bitten wir dich, die Nutzungsbedingungen und die Datenschutzerklärung zu akzeptieren.",
  },
  servidor: {
    necesitasCuenta: "Um die Nutzungsbedingungen und den Datenschutz zu akzeptieren, musst du dich mit deinem Konto anmelden.",
    cuerpoInvalido: "Wir haben die Anfrage nicht verstanden. Versuch es noch einmal.",
    noLeido: "Wir konnten deine Zustimmung zu den Nutzungsbedingungen und zum Datenschutz nicht prüfen. Versuch es gleich noch einmal.",
    noGuardado: "Wir konnten deine Zustimmung nicht speichern, deshalb zählt sie noch nicht. Versuch es noch einmal.",
    versionVieja: "Die Texte haben sich geändert, während du sie gelesen hast. Sieh dir die neue Version an und akzeptiere sie.",
  },
};

const it: typeof es = {
  tituloPrimera: "Prima di continuare con il tuo account",
  tituloNueva: "Abbiamo aggiornato i Termini e la Privacy",
  introPrimera:
    "Leggi i <terminos>Termini d'uso</terminos> e l'<privacidad>Informativa sulla privacy</privacidad> di My Idea. Per usare il tuo account, devi accettarli. Conserviamo la versione che accetti e la sua data.",
  introNueva:
    "I testi sono cambiati dall'ultima volta che li hai accettati. Leggi i <terminos>Termini d'uso</terminos> e l'<privacidad>Informativa sulla privacy</privacidad> e accetta la nuova versione per continuare con il tuo account.",
  soloEsFr: "Questi testi sono disponibili in spagnolo e in francese.",
  version: "Versione del {{version}}",
  casilla: "Ho letto e accetto i Termini d'uso e l'Informativa sulla privacy.",
  aceptar: "Accetta e continua",
  guardando: "Salvataggio…",
  salir: "Non ora, esci dal mio account",
  borrar: "Preferisco eliminare il mio account",
  errorGuardar: "Non siamo riusciti a salvare la tua accettazione, quindi non vale ancora. Riprova.",
  errorEstado: "Non siamo riusciti a verificare se hai già accettato la versione in vigore. Per continuare con il tuo account, accettala qui.",
  versionCambio: "I testi sono cambiati mentre li leggevi. Rivedi la nuova versione e accettala.",
  login: {
    enlaces: "<terminos>Termini</terminos> · <privacidad>Privacy</privacidad>",
    aviso: "Quando crei il tuo account, ti chiederemo di accettare i Termini d'uso e l'Informativa sulla privacy.",
  },
  servidor: {
    necesitasCuenta: "Per accettare i Termini e la Privacy devi accedere con il tuo account.",
    cuerpoInvalido: "Non abbiamo capito la richiesta. Riprova.",
    noLeido: "Non siamo riusciti a verificare la tua accettazione dei Termini e della Privacy. Riprova tra un momento.",
    noGuardado: "Non siamo riusciti a salvare la tua accettazione, quindi non vale ancora. Riprova.",
    versionVieja: "I testi sono cambiati mentre li leggevi. Rivedi la nuova versione e accettala.",
  },
};

const ja: typeof es = {
  tituloPrimera: "アカウントを続けて使う前に",
  tituloNueva: "利用規約とプライバシーポリシーを更新しました",
  introPrimera:
    "My Idea の<terminos>利用規約</terminos>と<privacidad>プライバシーポリシー</privacidad>をお読みください。アカウントを使うには、これらへの同意が必要です。同意したバージョンと日付を記録します。",
  introNueva:
    "前回の同意のあとで内容が変わりました。<terminos>利用規約</terminos>と<privacidad>プライバシーポリシー</privacidad>をお読みのうえ、新しいバージョンに同意するとアカウントを続けて使えます。",
  soloEsFr: "これらの文書はスペイン語とフランス語でご覧いただけます。",
  version: "{{version}} 版",
  casilla: "利用規約とプライバシーポリシーを読み、同意します。",
  aceptar: "同意して続ける",
  guardando: "保存しています…",
  salir: "今はしない（アカウントからログアウト）",
  borrar: "アカウントを削除したい",
  errorGuardar: "同意を保存できなかったため、まだ有効になっていません。もう一度お試しください。",
  errorEstado: "現在のバージョンにすでに同意しているか確認できませんでした。アカウントを続けて使うには、ここで同意してください。",
  versionCambio: "お読みいただいている間に内容が変わりました。新しいバージョンを確認して同意してください。",
  login: {
    enlaces: "<terminos>利用規約</terminos> · <privacidad>プライバシー</privacidad>",
    aviso: "アカウントを作成すると、利用規約とプライバシーポリシーへの同意をお願いします。",
  },
  servidor: {
    necesitasCuenta: "利用規約とプライバシーポリシーに同意するには、アカウントでログインしてください。",
    cuerpoInvalido: "リクエストを理解できませんでした。もう一度お試しください。",
    noLeido: "利用規約とプライバシーポリシーへの同意を確認できませんでした。少し待ってからもう一度お試しください。",
    noGuardado: "同意を保存できなかったため、まだ有効になっていません。もう一度お試しください。",
    versionVieja: "お読みいただいている間に内容が変わりました。新しいバージョンを確認して同意してください。",
  },
};

const zh: typeof es = {
  tituloPrimera: "继续使用你的账户之前",
  tituloNueva: "我们更新了使用条款和隐私政策",
  introPrimera:
    "请阅读 My Idea 的<terminos>使用条款</terminos>和<privacidad>隐私政策</privacidad>。要使用你的账户，需要你接受它们。我们会保存你接受的版本和日期。",
  introNueva:
    "自你上次接受以来，这些文本已有变化。请阅读<terminos>使用条款</terminos>和<privacidad>隐私政策</privacidad>，接受新版本后即可继续使用你的账户。",
  soloEsFr: "这些文本提供西班牙语和法语版本。",
  version: "{{version}} 版",
  casilla: "我已阅读并接受使用条款和隐私政策。",
  aceptar: "接受并继续",
  guardando: "正在保存…",
  salir: "暂不，退出我的账户",
  borrar: "我想删除我的账户",
  errorGuardar: "我们没能保存你的接受，所以它还不算数。请再试一次。",
  errorEstado: "我们没能确认你是否已接受现行版本。要继续使用你的账户，请在这里接受。",
  versionCambio: "你阅读期间文本有了变化。请查看新版本并接受。",
  login: {
    enlaces: "<terminos>条款</terminos> · <privacidad>隐私</privacidad>",
    aviso: "创建账户时，我们会请你接受使用条款和隐私政策。",
  },
  servidor: {
    necesitasCuenta: "要接受使用条款和隐私政策，你需要用你的账户登录。",
    cuerpoInvalido: "我们没能理解这个请求。请再试一次。",
    noLeido: "我们没能确认你对使用条款和隐私政策的接受。请稍后再试。",
    noGuardado: "我们没能保存你的接受，所以它还不算数。请再试一次。",
    versionVieja: "你阅读期间文本有了变化。请查看新版本并接受。",
  },
};

const ko: typeof es = {
  tituloPrimera: "계정을 계속 사용하기 전에",
  tituloNueva: "이용약관과 개인정보 처리방침을 업데이트했어요",
  introPrimera:
    "My Idea의 <terminos>이용약관</terminos>과 <privacidad>개인정보 처리방침</privacidad>을 읽어 주세요. 계정을 사용하려면 동의가 필요해요. 동의한 버전과 날짜를 기록해요.",
  introNueva:
    "마지막으로 동의한 뒤 내용이 바뀌었어요. <terminos>이용약관</terminos>과 <privacidad>개인정보 처리방침</privacidad>을 읽고 새 버전에 동의하면 계정을 계속 사용할 수 있어요.",
  soloEsFr: "이 문서는 스페인어와 프랑스어로 제공돼요.",
  version: "{{version}} 버전",
  casilla: "이용약관과 개인정보 처리방침을 읽었으며 동의해요.",
  aceptar: "동의하고 계속하기",
  guardando: "저장하는 중…",
  salir: "지금은 안 할래요, 계정에서 로그아웃",
  borrar: "계정을 삭제할래요",
  errorGuardar: "동의를 저장하지 못해서 아직 반영되지 않았어요. 다시 시도해 주세요.",
  errorEstado: "현재 버전에 이미 동의했는지 확인하지 못했어요. 계정을 계속 사용하려면 여기에서 동의해 주세요.",
  versionCambio: "읽는 동안 내용이 바뀌었어요. 새 버전을 확인하고 동의해 주세요.",
  login: {
    enlaces: "<terminos>이용약관</terminos> · <privacidad>개인정보</privacidad>",
    aviso: "계정을 만들면 이용약관과 개인정보 처리방침에 동의해 달라고 요청할 거예요.",
  },
  servidor: {
    necesitasCuenta: "이용약관과 개인정보 처리방침에 동의하려면 계정으로 로그인해야 해요.",
    cuerpoInvalido: "요청을 이해하지 못했어요. 다시 시도해 주세요.",
    noLeido: "이용약관과 개인정보 처리방침 동의 여부를 확인하지 못했어요. 잠시 후 다시 시도해 주세요.",
    noGuardado: "동의를 저장하지 못해서 아직 반영되지 않았어요. 다시 시도해 주세요.",
    versionVieja: "읽는 동안 내용이 바뀌었어요. 새 버전을 확인하고 동의해 주세요.",
  },
};

const ar: typeof es = {
  tituloPrimera: "قبل أن تتابع بحسابك",
  tituloNueva: "حدّثنا شروط الاستخدام وسياسة الخصوصية",
  introPrimera:
    "اقرأ <terminos>شروط الاستخدام</terminos> و<privacidad>سياسة الخصوصية</privacidad> الخاصة بـ My Idea. لكي تستخدم حسابك، نحتاج إلى موافقتك عليهما. نحفظ النسخة التي توافق عليها وتاريخها.",
  introNueva:
    "تغيّرت النصوص منذ آخر مرة وافقت عليها. اقرأ <terminos>شروط الاستخدام</terminos> و<privacidad>سياسة الخصوصية</privacidad>، ووافق على النسخة الجديدة لتتابع بحسابك.",
  soloEsFr: "هذه النصوص متاحة بالإسبانية والفرنسية.",
  version: "نسخة {{version}}",
  casilla: "قرأت شروط الاستخدام وسياسة الخصوصية وأوافق عليهما.",
  aceptar: "أوافق وأتابع",
  guardando: "جارٍ الحفظ…",
  salir: "ليس الآن، سجّل خروجي من حسابي",
  borrar: "أفضّل حذف حسابي",
  errorGuardar: "لم نتمكن من حفظ موافقتك، لذلك لا تُحتسب بعد. حاول مرة أخرى.",
  errorEstado: "لم نتمكن من التحقق مما إذا كنت قد وافقت على النسخة الحالية. لتتابع بحسابك، وافق عليها هنا.",
  versionCambio: "تغيّرت النصوص أثناء قراءتك لها. راجع النسخة الجديدة ووافق عليها.",
  login: {
    enlaces: "<terminos>الشروط</terminos> · <privacidad>الخصوصية</privacidad>",
    aviso: "عند إنشاء حسابك سنطلب منك الموافقة على شروط الاستخدام وسياسة الخصوصية.",
  },
  servidor: {
    necesitasCuenta: "لكي توافق على الشروط وسياسة الخصوصية، عليك تسجيل الدخول بحسابك.",
    cuerpoInvalido: "لم نفهم الطلب. حاول مرة أخرى.",
    noLeido: "لم نتمكن من التحقق من موافقتك على الشروط وسياسة الخصوصية. حاول مرة أخرى بعد قليل.",
    noGuardado: "لم نتمكن من حفظ موافقتك، لذلك لا تُحتسب بعد. حاول مرة أخرى.",
    versionVieja: "تغيّرت النصوص أثناء قراءتك لها. راجع النسخة الجديدة ووافق عليها.",
  },
};

const hi: typeof es = {
  tituloPrimera: "अपने खाते के साथ आगे बढ़ने से पहले",
  tituloNueva: "हमने उपयोग की शर्तें और गोपनीयता नीति अपडेट की हैं",
  introPrimera:
    "My Idea की <terminos>उपयोग की शर्तें</terminos> और <privacidad>गोपनीयता नीति</privacidad> पढ़ें। अपना खाता इस्तेमाल करने के लिए आपको इन्हें स्वीकार करना होगा। आप जो संस्करण स्वीकार करते हैं, हम उसे और उसकी तारीख को सहेजते हैं।",
  introNueva:
    "पिछली बार स्वीकार करने के बाद से ये पाठ बदल गए हैं। <terminos>उपयोग की शर्तें</terminos> और <privacidad>गोपनीयता नीति</privacidad> पढ़ें, और अपने खाते के साथ आगे बढ़ने के लिए नया संस्करण स्वीकार करें।",
  soloEsFr: "ये पाठ स्पेनिश और फ़्रेंच में उपलब्ध हैं।",
  version: "{{version}} का संस्करण",
  casilla: "मैंने उपयोग की शर्तें और गोपनीयता नीति पढ़ ली हैं और मैं उन्हें स्वीकार करता/करती हूँ।",
  aceptar: "स्वीकार करें और आगे बढ़ें",
  guardando: "सहेजा जा रहा है…",
  salir: "अभी नहीं, मेरे खाते से लॉग आउट करें",
  borrar: "मैं अपना खाता हटाना पसंद करूँगा/करूँगी",
  errorGuardar: "हम आपकी स्वीकृति सहेज नहीं पाए, इसलिए वह अभी मान्य नहीं है। फिर से कोशिश करें।",
  errorEstado: "हम जाँच नहीं पाए कि आपने मौजूदा संस्करण पहले ही स्वीकार किया है या नहीं। अपने खाते के साथ आगे बढ़ने के लिए उसे यहाँ स्वीकार करें।",
  versionCambio: "आपके पढ़ते समय पाठ बदल गए। नया संस्करण देखें और उसे स्वीकार करें।",
  login: {
    enlaces: "<terminos>शर्तें</terminos> · <privacidad>गोपनीयता</privacidad>",
    aviso: "खाता बनाते समय हम आपसे उपयोग की शर्तें और गोपनीयता नीति स्वीकार करने को कहेंगे।",
  },
  servidor: {
    necesitasCuenta: "शर्तें और गोपनीयता नीति स्वीकार करने के लिए आपको अपने खाते से लॉग इन करना होगा।",
    cuerpoInvalido: "हम अनुरोध समझ नहीं पाए। फिर से कोशिश करें।",
    noLeido: "हम शर्तों और गोपनीयता नीति की आपकी स्वीकृति जाँच नहीं पाए। थोड़ी देर बाद फिर से कोशिश करें।",
    noGuardado: "हम आपकी स्वीकृति सहेज नहीं पाए, इसलिए वह अभी मान्य नहीं है। फिर से कोशिश करें।",
    versionVieja: "आपके पढ़ते समय पाठ बदल गए। नया संस्करण देखें और उसे स्वीकार करें।",
  },
};

export const CONSENTIMIENTO: PorIdioma<typeof es> = { es, en, pt, fr, de, it, ja, zh, ko, ar, hi };
