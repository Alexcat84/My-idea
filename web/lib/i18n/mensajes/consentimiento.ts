/**
 * El consentimiento legal versionado (corrección del fundador, 7 oct 2026, que retiró el modal): la línea que va junto
 * al botón en el primer envío de datos (app/ui/LineaConsentimiento.tsx, en /nueva y en La Exploración), la línea y
 * los enlaces de /login, el aviso de cookies del pie (app/ui/AvisoCookies.tsx) y los mensajes del servidor
 * (/api/cuenta/consentimiento y la guarda de lib/legal/aceptacionServidor.ts). Lo ve toda identidad que envía datos,
 * también la invisible. Los enlaces llevan a las páginas legales, que se leen en el idioma de la persona si su
 * traducción está publicada y, si no, en español.
 */
import type { PorIdioma } from "../config";

const es = {
  envio: {
    linea: "Al continuar, aceptas los <terminos>Términos</terminos> y la <privacidad>Política de Privacidad</privacidad>",
    lineaNueva:
      "Actualizamos los <terminos>Términos</terminos> y la <privacidad>Política de Privacidad</privacidad>. Al continuar, aceptas la versión nueva",
    aceptarYGenerar: "Aceptar y generar",
    aceptarYSeguir: "Aceptar y seguir",
    guardando: "Guardando tu aceptación…",
    errorGuardar: "No pudimos guardar tu aceptación, así que no enviamos nada. Inténtalo de nuevo.",
    versionCambio:
      "Los Términos o la Política de Privacidad cambiaron mientras escribías. Recarga la página para ver la versión nueva.",
  },
  login: {
    enlaces: "<terminos>Términos</terminos> · <privacidad>Privacidad</privacidad>",
    linea: "Al continuar, aceptas los <terminos>Términos</terminos> y la <privacidad>Política de Privacidad</privacidad>",
  },
  cookies: {
    aviso: "Solo usamos cookies necesarias para que la app funcione y para recordar tu idioma. <cookies>Más información</cookies>",
  },
  servidor: {
    sinIdentidad: "No pudimos reconocer tu sesión. Recarga la página e inténtalo de nuevo.",
    cuerpoInvalido: "No entendimos la petición. Inténtalo de nuevo.",
    noLeido: "No pudimos comprobar tu aceptación de los Términos y la Privacidad. Inténtalo de nuevo en un momento.",
    noGuardado: "No pudimos guardar tu aceptación, así que todavía no cuenta. Inténtalo de nuevo.",
    versionVieja: "Los textos cambiaron mientras los leías. Recarga la página para ver la versión nueva.",
    requerida: "Antes de generar, acepta los Términos y la Política de Privacidad.",
    requeridaNueva: "Actualizamos los Términos y la Política de Privacidad. Acepta la versión nueva para continuar.",
  },
};

const en: typeof es = {
  envio: {
    linea: "By continuing, you accept the <terminos>Terms</terminos> and the <privacidad>Privacy Policy</privacidad>",
    lineaNueva:
      "We updated the <terminos>Terms</terminos> and the <privacidad>Privacy Policy</privacidad>. By continuing, you accept the new version",
    aceptarYGenerar: "Accept and generate",
    aceptarYSeguir: "Accept and continue",
    guardando: "Saving your acceptance…",
    errorGuardar: "We couldn't save your acceptance, so nothing was sent. Please try again.",
    versionCambio: "The Terms or the Privacy Policy changed while you were writing. Reload the page to see the new version.",
  },
  login: {
    enlaces: "<terminos>Terms</terminos> · <privacidad>Privacy</privacidad>",
    linea: "By continuing, you accept the <terminos>Terms</terminos> and the <privacidad>Privacy Policy</privacidad>",
  },
  cookies: {
    aviso: "We only use cookies the app needs to work and to remember your language. <cookies>Learn more</cookies>",
  },
  servidor: {
    sinIdentidad: "We couldn't recognize your session. Reload the page and try again.",
    cuerpoInvalido: "We didn't understand the request. Please try again.",
    noLeido: "We couldn't check your acceptance of the Terms and the Privacy Policy. Please try again in a moment.",
    noGuardado: "We couldn't save your acceptance, so it doesn't count yet. Please try again.",
    versionVieja: "The texts changed while you were reading them. Reload the page to see the new version.",
    requerida: "Before generating, accept the Terms and the Privacy Policy.",
    requeridaNueva: "We updated the Terms and the Privacy Policy. Accept the new version to continue.",
  },
};

const pt: typeof es = {
  envio: {
    linea: "Ao continuar, você aceita os <terminos>Termos</terminos> e a <privacidad>Política de Privacidade</privacidad>",
    lineaNueva:
      "Atualizamos os <terminos>Termos</terminos> e a <privacidad>Política de Privacidade</privacidad>. Ao continuar, você aceita a nova versão",
    aceptarYGenerar: "Aceitar e gerar",
    aceptarYSeguir: "Aceitar e continuar",
    guardando: "Salvando a sua aceitação…",
    errorGuardar: "Não conseguimos salvar a sua aceitação, então nada foi enviado. Tente novamente.",
    versionCambio:
      "Os Termos ou a Política de Privacidade mudaram enquanto você escrevia. Recarregue a página para ver a nova versão.",
  },
  login: {
    enlaces: "<terminos>Termos</terminos> · <privacidad>Privacidade</privacidad>",
    linea: "Ao continuar, você aceita os <terminos>Termos</terminos> e a <privacidad>Política de Privacidade</privacidad>",
  },
  cookies: {
    aviso: "Usamos apenas os cookies necessários para o app funcionar e para lembrar o seu idioma. <cookies>Saiba mais</cookies>",
  },
  servidor: {
    sinIdentidad: "Não conseguimos reconhecer a sua sessão. Recarregue a página e tente novamente.",
    cuerpoInvalido: "Não entendemos o pedido. Tente novamente.",
    noLeido: "Não conseguimos verificar a sua aceitação dos Termos e da Privacidade. Tente novamente em instantes.",
    noGuardado: "Não conseguimos salvar a sua aceitação, então ela ainda não vale. Tente novamente.",
    versionVieja: "Os textos mudaram enquanto você os lia. Recarregue a página para ver a nova versão.",
    requerida: "Antes de gerar, aceite os Termos e a Política de Privacidade.",
    requeridaNueva: "Atualizamos os Termos e a Política de Privacidade. Aceite a nova versão para continuar.",
  },
};

const fr: typeof es = {
  envio: {
    linea:
      "En continuant, tu acceptes les <terminos>Conditions</terminos> et la <privacidad>Politique de confidentialité</privacidad>",
    lineaNueva:
      "Nous avons mis à jour les <terminos>Conditions</terminos> et la <privacidad>Politique de confidentialité</privacidad>. En continuant, tu acceptes la nouvelle version",
    aceptarYGenerar: "Accepter et générer",
    aceptarYSeguir: "Accepter et continuer",
    guardando: "Enregistrement de ton acceptation…",
    errorGuardar: "Nous n'avons pas pu enregistrer ton acceptation, donc rien n'a été envoyé. Réessaie.",
    versionCambio:
      "Les Conditions ou la Politique de confidentialité ont changé pendant que tu écrivais. Recharge la page pour voir la nouvelle version.",
  },
  login: {
    enlaces: "<terminos>Conditions</terminos> · <privacidad>Confidentialité</privacidad>",
    linea:
      "En continuant, tu acceptes les <terminos>Conditions</terminos> et la <privacidad>Politique de confidentialité</privacidad>",
  },
  cookies: {
    aviso:
      "Nous utilisons seulement les témoins nécessaires au fonctionnement de l'application et pour retenir ta langue. <cookies>En savoir plus</cookies>",
  },
  servidor: {
    sinIdentidad: "Nous n'avons pas pu reconnaître ta session. Recharge la page et réessaie.",
    cuerpoInvalido: "Nous n'avons pas compris la demande. Réessaie.",
    noLeido: "Nous n'avons pas pu vérifier ton acceptation des Conditions et de la Confidentialité. Réessaie dans un instant.",
    noGuardado: "Nous n'avons pas pu enregistrer ton acceptation, elle ne compte donc pas encore. Réessaie.",
    versionVieja: "Les textes ont changé pendant que tu les lisais. Recharge la page pour voir la nouvelle version.",
    requerida: "Avant de générer, accepte les Conditions et la Politique de confidentialité.",
    requeridaNueva: "Nous avons mis à jour les Conditions et la Politique de confidentialité. Accepte la nouvelle version pour continuer.",
  },
};

const de: typeof es = {
  envio: {
    linea:
      "Wenn du fortfährst, akzeptierst du die <terminos>Nutzungsbedingungen</terminos> und die <privacidad>Datenschutzerklärung</privacidad>",
    lineaNueva:
      "Wir haben die <terminos>Nutzungsbedingungen</terminos> und die <privacidad>Datenschutzerklärung</privacidad> aktualisiert. Wenn du fortfährst, akzeptierst du die neue Version",
    aceptarYGenerar: "Akzeptieren und erstellen",
    aceptarYSeguir: "Akzeptieren und weiter",
    guardando: "Deine Zustimmung wird gespeichert…",
    errorGuardar: "Wir konnten deine Zustimmung nicht speichern, deshalb wurde nichts gesendet. Versuch es noch einmal.",
    versionCambio:
      "Die Nutzungsbedingungen oder die Datenschutzerklärung haben sich geändert, während du geschrieben hast. Lade die Seite neu, um die neue Version zu sehen.",
  },
  login: {
    enlaces: "<terminos>Nutzungsbedingungen</terminos> · <privacidad>Datenschutz</privacidad>",
    linea:
      "Wenn du fortfährst, akzeptierst du die <terminos>Nutzungsbedingungen</terminos> und die <privacidad>Datenschutzerklärung</privacidad>",
  },
  cookies: {
    aviso:
      "Wir verwenden nur Cookies, die die App zum Funktionieren braucht und die sich deine Sprache merken. <cookies>Mehr erfahren</cookies>",
  },
  servidor: {
    sinIdentidad: "Wir konnten deine Sitzung nicht erkennen. Lade die Seite neu und versuch es noch einmal.",
    cuerpoInvalido: "Wir haben die Anfrage nicht verstanden. Versuch es noch einmal.",
    noLeido: "Wir konnten deine Zustimmung zu den Nutzungsbedingungen und zum Datenschutz nicht prüfen. Versuch es gleich noch einmal.",
    noGuardado: "Wir konnten deine Zustimmung nicht speichern, deshalb zählt sie noch nicht. Versuch es noch einmal.",
    versionVieja: "Die Texte haben sich geändert, während du sie gelesen hast. Lade die Seite neu, um die neue Version zu sehen.",
    requerida: "Bevor du etwas erstellen lässt, akzeptiere die Nutzungsbedingungen und die Datenschutzerklärung.",
    requeridaNueva:
      "Wir haben die Nutzungsbedingungen und die Datenschutzerklärung aktualisiert. Akzeptiere die neue Version, um fortzufahren.",
  },
};

const it: typeof es = {
  envio: {
    linea: "Continuando, accetti i <terminos>Termini</terminos> e l'<privacidad>Informativa sulla privacy</privacidad>",
    lineaNueva:
      "Abbiamo aggiornato i <terminos>Termini</terminos> e l'<privacidad>Informativa sulla privacy</privacidad>. Continuando, accetti la nuova versione",
    aceptarYGenerar: "Accetta e genera",
    aceptarYSeguir: "Accetta e continua",
    guardando: "Salvataggio della tua accettazione…",
    errorGuardar: "Non siamo riusciti a salvare la tua accettazione, quindi non abbiamo inviato nulla. Riprova.",
    versionCambio:
      "I Termini o l'Informativa sulla privacy sono cambiati mentre scrivevi. Ricarica la pagina per vedere la nuova versione.",
  },
  login: {
    enlaces: "<terminos>Termini</terminos> · <privacidad>Privacy</privacidad>",
    linea: "Continuando, accetti i <terminos>Termini</terminos> e l'<privacidad>Informativa sulla privacy</privacidad>",
  },
  cookies: {
    aviso: "Usiamo solo i cookie necessari al funzionamento dell'app e per ricordare la tua lingua. <cookies>Scopri di più</cookies>",
  },
  servidor: {
    sinIdentidad: "Non siamo riusciti a riconoscere la tua sessione. Ricarica la pagina e riprova.",
    cuerpoInvalido: "Non abbiamo capito la richiesta. Riprova.",
    noLeido: "Non siamo riusciti a verificare la tua accettazione dei Termini e della Privacy. Riprova tra un momento.",
    noGuardado: "Non siamo riusciti a salvare la tua accettazione, quindi non vale ancora. Riprova.",
    versionVieja: "I testi sono cambiati mentre li leggevi. Ricarica la pagina per vedere la nuova versione.",
    requerida: "Prima di generare, accetta i Termini e l'Informativa sulla privacy.",
    requeridaNueva: "Abbiamo aggiornato i Termini e l'Informativa sulla privacy. Accetta la nuova versione per continuare.",
  },
};

const ja: typeof es = {
  envio: {
    linea: "続行すると、<terminos>利用規約</terminos>と<privacidad>プライバシーポリシー</privacidad>に同意したことになります",
    lineaNueva:
      "<terminos>利用規約</terminos>と<privacidad>プライバシーポリシー</privacidad>を更新しました。続行すると、新しいバージョンに同意したことになります",
    aceptarYGenerar: "同意して作成する",
    aceptarYSeguir: "同意して続ける",
    guardando: "同意を保存しています…",
    errorGuardar: "同意を保存できなかったため、何も送信していません。もう一度お試しください。",
    versionCambio: "入力中に利用規約またはプライバシーポリシーが変更されました。ページを再読み込みして新しいバージョンをご確認ください。",
  },
  login: {
    enlaces: "<terminos>利用規約</terminos> · <privacidad>プライバシー</privacidad>",
    linea: "続行すると、<terminos>利用規約</terminos>と<privacidad>プライバシーポリシー</privacidad>に同意したことになります",
  },
  cookies: {
    aviso: "アプリを動かすためと、表示言語を覚えておくために必要なCookieだけを使っています。<cookies>詳しく見る</cookies>",
  },
  servidor: {
    sinIdentidad: "セッションを確認できませんでした。ページを再読み込みして、もう一度お試しください。",
    cuerpoInvalido: "リクエストを理解できませんでした。もう一度お試しください。",
    noLeido: "利用規約とプライバシーポリシーへの同意を確認できませんでした。少し待ってからもう一度お試しください。",
    noGuardado: "同意を保存できなかったため、まだ有効になっていません。もう一度お試しください。",
    versionVieja: "お読みいただいている間に内容が変わりました。ページを再読み込みして新しいバージョンをご確認ください。",
    requerida: "作成する前に、利用規約とプライバシーポリシーに同意してください。",
    requeridaNueva: "利用規約とプライバシーポリシーを更新しました。続けるには新しいバージョンに同意してください。",
  },
};

const zh: typeof es = {
  envio: {
    linea: "继续即表示你接受<terminos>使用条款</terminos>和<privacidad>隐私政策</privacidad>",
    lineaNueva: "我们更新了<terminos>使用条款</terminos>和<privacidad>隐私政策</privacidad>。继续即表示你接受新版本",
    aceptarYGenerar: "接受并生成",
    aceptarYSeguir: "接受并继续",
    guardando: "正在保存你的同意…",
    errorGuardar: "我们没能保存你的同意，所以什么都没有发送。请再试一次。",
    versionCambio: "你输入期间，使用条款或隐私政策有了变化。请刷新页面查看新版本。",
  },
  login: {
    enlaces: "<terminos>条款</terminos> · <privacidad>隐私</privacidad>",
    linea: "继续即表示你接受<terminos>使用条款</terminos>和<privacidad>隐私政策</privacidad>",
  },
  cookies: {
    aviso: "我们只使用应用运行和记住你的语言所必需的 Cookie。<cookies>了解更多</cookies>",
  },
  servidor: {
    sinIdentidad: "我们没能识别你的会话。请刷新页面后再试一次。",
    cuerpoInvalido: "我们没能理解这个请求。请再试一次。",
    noLeido: "我们没能确认你是否已同意使用条款和隐私政策。请稍后再试。",
    noGuardado: "我们没能保存你的同意，所以暂时还未生效。请再试一次。",
    versionVieja: "你阅读期间文本有了变化。请刷新页面查看新版本。",
    requerida: "生成之前，请接受使用条款和隐私政策。",
    requeridaNueva: "我们更新了使用条款和隐私政策。接受新版本后即可继续。",
  },
};

const ko: typeof es = {
  envio: {
    linea: "계속하면 <terminos>이용약관</terminos>과 <privacidad>개인정보 처리방침</privacidad>에 동의하게 돼요",
    lineaNueva:
      "<terminos>이용약관</terminos>과 <privacidad>개인정보 처리방침</privacidad>을 업데이트했어요. 계속하면 새 버전에 동의하게 돼요",
    aceptarYGenerar: "동의하고 만들기",
    aceptarYSeguir: "동의하고 계속하기",
    guardando: "동의를 저장하는 중…",
    errorGuardar: "동의를 저장하지 못해서 아무것도 보내지 않았어요. 다시 시도해 주세요.",
    versionCambio: "작성하는 동안 이용약관이나 개인정보 처리방침이 바뀌었어요. 페이지를 새로고침해서 새 버전을 확인해 주세요.",
  },
  login: {
    enlaces: "<terminos>이용약관</terminos> · <privacidad>개인정보</privacidad>",
    linea: "계속하면 <terminos>이용약관</terminos>과 <privacidad>개인정보 처리방침</privacidad>에 동의하게 돼요",
  },
  cookies: {
    aviso: "앱이 작동하고 언어를 기억하는 데 필요한 쿠키만 사용해요. <cookies>자세히 보기</cookies>",
  },
  servidor: {
    sinIdentidad: "세션을 확인하지 못했어요. 페이지를 새로고침하고 다시 시도해 주세요.",
    cuerpoInvalido: "요청을 이해하지 못했어요. 다시 시도해 주세요.",
    noLeido: "이용약관과 개인정보 처리방침 동의 여부를 확인하지 못했어요. 잠시 후 다시 시도해 주세요.",
    noGuardado: "동의를 저장하지 못해서 아직 반영되지 않았어요. 다시 시도해 주세요.",
    versionVieja: "읽는 동안 내용이 바뀌었어요. 페이지를 새로고침해서 새 버전을 확인해 주세요.",
    requerida: "만들기 전에 이용약관과 개인정보 처리방침에 동의해 주세요.",
    requeridaNueva: "이용약관과 개인정보 처리방침을 업데이트했어요. 계속하려면 새 버전에 동의해 주세요.",
  },
};

const ar: typeof es = {
  envio: {
    linea: "بالمتابعة، توافقون على <terminos>الشروط</terminos> و<privacidad>سياسة الخصوصية</privacidad>",
    lineaNueva:
      "حدّثنا <terminos>الشروط</terminos> و<privacidad>سياسة الخصوصية</privacidad>. بالمتابعة، توافقون على النسخة الجديدة",
    aceptarYGenerar: "أوافق وأنشئ",
    aceptarYSeguir: "أوافق وأتابع",
    guardando: "جارٍ حفظ موافقتكم…",
    errorGuardar: "لم نتمكن من حفظ موافقتكم، لذلك لم نرسل شيئًا. حاولوا مرة أخرى.",
    versionCambio: "تغيّرت الشروط أو سياسة الخصوصية أثناء كتابتكم. أعيدوا تحميل الصفحة لتروا النسخة الجديدة.",
  },
  login: {
    enlaces: "<terminos>الشروط</terminos> · <privacidad>الخصوصية</privacidad>",
    linea: "بالمتابعة، توافقون على <terminos>الشروط</terminos> و<privacidad>سياسة الخصوصية</privacidad>",
  },
  cookies: {
    aviso: "نستخدم فقط ملفات تعريف الارتباط اللازمة لعمل التطبيق ولتذكّر لغتكم. <cookies>مزيد من المعلومات</cookies>",
  },
  servidor: {
    sinIdentidad: "لم نتمكن من التعرّف على جلستكم. أعيدوا تحميل الصفحة وحاولوا مرة أخرى.",
    cuerpoInvalido: "لم نفهم الطلب. حاولوا مرة أخرى.",
    noLeido: "لم نتمكن من التحقق من موافقتكم على الشروط وسياسة الخصوصية. حاولوا مرة أخرى بعد قليل.",
    noGuardado: "لم نتمكن من حفظ موافقتكم، لذلك لا تُحتسب بعد. حاولوا مرة أخرى.",
    versionVieja: "تغيّرت النصوص أثناء قراءتكم لها. أعيدوا تحميل الصفحة لتروا النسخة الجديدة.",
    requerida: "قبل الإنشاء، وافقوا على الشروط وسياسة الخصوصية.",
    requeridaNueva: "حدّثنا الشروط وسياسة الخصوصية. وافقوا على النسخة الجديدة للمتابعة.",
  },
};

const hi: typeof es = {
  envio: {
    linea: "आगे बढ़कर आप <terminos>शर्तें</terminos> और <privacidad>गोपनीयता नीति</privacidad> स्वीकार करते हैं",
    lineaNueva:
      "हमने <terminos>शर्तें</terminos> और <privacidad>गोपनीयता नीति</privacidad> अपडेट की हैं। आगे बढ़कर आप नया संस्करण स्वीकार करते हैं",
    aceptarYGenerar: "स्वीकार करें और बनाएँ",
    aceptarYSeguir: "स्वीकार करें और आगे बढ़ें",
    guardando: "आपकी स्वीकृति सहेजी जा रही है…",
    errorGuardar: "हम आपकी स्वीकृति सहेज नहीं पाए, इसलिए कुछ भी नहीं भेजा गया। फिर से कोशिश करें।",
    versionCambio: "आपके लिखते समय शर्तें या गोपनीयता नीति बदल गईं। नया संस्करण देखने के लिए पेज फिर से लोड करें।",
  },
  login: {
    enlaces: "<terminos>शर्तें</terminos> · <privacidad>गोपनीयता</privacidad>",
    linea: "आगे बढ़कर आप <terminos>शर्तें</terminos> और <privacidad>गोपनीयता नीति</privacidad> स्वीकार करते हैं",
  },
  cookies: {
    aviso: "हम केवल वही कुकीज़ इस्तेमाल करते हैं जो ऐप चलाने और आपकी भाषा याद रखने के लिए ज़रूरी हैं। <cookies>और जानें</cookies>",
  },
  servidor: {
    sinIdentidad: "हम आपका सत्र पहचान नहीं पाए। पेज फिर से लोड करें और दोबारा कोशिश करें।",
    cuerpoInvalido: "हम अनुरोध समझ नहीं पाए। फिर से कोशिश करें।",
    noLeido: "हम शर्तों और गोपनीयता नीति की आपकी स्वीकृति जाँच नहीं पाए। थोड़ी देर बाद फिर से कोशिश करें।",
    noGuardado: "हम आपकी स्वीकृति सहेज नहीं पाए, इसलिए वह अभी मान्य नहीं है। फिर से कोशिश करें।",
    versionVieja: "आपके पढ़ते समय पाठ बदल गए। नया संस्करण देखने के लिए पेज फिर से लोड करें।",
    requerida: "बनाने से पहले, शर्तें और गोपनीयता नीति स्वीकार करें।",
    requeridaNueva: "हमने शर्तें और गोपनीयता नीति अपडेट की हैं। आगे बढ़ने के लिए नया संस्करण स्वीकार करें।",
  },
};

export const CONSENTIMIENTO: PorIdioma<typeof es> = { es, en, pt, fr, de, it, ja, zh, ko, ar, hi };
