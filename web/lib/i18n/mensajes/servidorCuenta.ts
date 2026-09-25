/** Mensajes de las rutas de cuenta y acceso: app/api/auth/** (registrar,
 * entrar, reset, reenviar), app/api/cuenta/eliminar y los comunes que
 * comparten con las rutas del doble factor (app/api/cuenta/2fa/**). */
import type { PorIdioma } from "../config";

const es = {
  comun: {
    cuerpoInvalido: "cuerpo inválido",
    necesitasCuenta: "necesitas tu cuenta para esto",
    algoSeAtoro: "algo se atoró; intenta de nuevo",
    algoSeAtoroMomento: "algo se atoró de nuestro lado; intenta de nuevo en un momento",
    correoInvalido: "escribe un correo válido",
  },
  entrar: {
    faltanDatos: "escribe tu correo y tu contraseña",
    sinConfirmar: "Aún no confirmaste tu correo. Revisa tu bandeja (y el spam) o pide un enlace nuevo.",
    credencialesMalas: "Correo o contraseña incorrectos.",
  },
  registrar: {
    demasiadosIntentos: "Demasiados intentos por ahora. Espera unos minutos y vuelve a intentar.",
    noPudimosCrear: "no pudimos crear tu cuenta; intenta de nuevo en un momento",
  },
  eliminar: {
    escribeEliminar: 'Para borrar tu cuenta escribe la palabra "{{palabra}}" tal cual.',
    seguridadSinConfirmar:
      "No pude confirmar la seguridad de tu cuenta, así que no borré nada. Intenta de nuevo en un momento.",
    noPudeBorrarTodo: "No pude borrar todos tus datos, así que tu cuenta sigue igual. Intenta de nuevo en un momento.",
  },
};

const en: typeof es = {
  comun: {
    cuerpoInvalido: "invalid body",
    necesitasCuenta: "you need your account for this",
    algoSeAtoro: "something got stuck; try again",
    algoSeAtoroMomento: "something got stuck on our end; try again in a moment",
    correoInvalido: "enter a valid email",
  },
  entrar: {
    faltanDatos: "enter your email and password",
    sinConfirmar: "You haven't confirmed your email yet. Check your inbox (and your spam) or request a new link.",
    credencialesMalas: "Incorrect email or password.",
  },
  registrar: {
    demasiadosIntentos: "Too many attempts for now. Wait a few minutes and try again.",
    noPudimosCrear: "we couldn't create your account; try again in a moment",
  },
  eliminar: {
    escribeEliminar: 'To delete your account, type the word "{{palabra}}" exactly as shown.',
    seguridadSinConfirmar:
      "I couldn't verify your account's security, so I didn't delete anything. Try again in a moment.",
    noPudeBorrarTodo: "I couldn't delete all your data, so your account is unchanged. Try again in a moment.",
  },
};

const fr: typeof es = {
  comun: {
    cuerpoInvalido: "corps de requête invalide",
    necesitasCuenta: "il te faut ton compte pour ça",
    algoSeAtoro: "quelque chose a coincé; réessaie",
    algoSeAtoroMomento: "quelque chose a coincé de notre côté; réessaie dans un moment",
    correoInvalido: "écris une adresse courriel valide",
  },
  entrar: {
    faltanDatos: "écris ton courriel et ton mot de passe",
    sinConfirmar: "Tu n'as pas encore confirmé ton courriel. Vérifie ta boîte de réception (et tes courriels indésirables) ou demande un nouveau lien.",
    credencialesMalas: "Courriel ou mot de passe incorrect.",
  },
  registrar: {
    demasiadosIntentos: "Trop de tentatives pour l'instant. Attends quelques minutes et réessaie.",
    noPudimosCrear: "nous n'avons pas pu créer ton compte; réessaie dans un moment",
  },
  eliminar: {
    escribeEliminar: "Pour supprimer ton compte, écris le mot « {{palabra}} » tel quel.",
    seguridadSinConfirmar: "Je n'ai pas pu confirmer la sécurité de ton compte, alors je n'ai rien supprimé. Réessaie dans un moment.",
    noPudeBorrarTodo: "Je n'ai pas pu supprimer toutes tes données, alors ton compte reste tel quel. Réessaie dans un moment.",
  },
};

const pt: typeof es = {
  comun: {
    cuerpoInvalido: "corpo inválido",
    necesitasCuenta: "você precisa da sua conta para isso",
    algoSeAtoro: "algo travou; tente de novo",
    algoSeAtoroMomento: "algo travou do nosso lado; tente de novo daqui a pouco",
    correoInvalido: "digite um e-mail válido",
  },
  entrar: {
    faltanDatos: "digite seu e-mail e sua senha",
    sinConfirmar: "Você ainda não confirmou seu e-mail. Confira sua caixa de entrada (e o spam) ou peça um novo link.",
    credencialesMalas: "E-mail ou senha incorretos.",
  },
  registrar: {
    demasiadosIntentos: "Muitas tentativas por enquanto. Espere alguns minutos e tente de novo.",
    noPudimosCrear: "não conseguimos criar sua conta; tente de novo daqui a pouco",
  },
  eliminar: {
    escribeEliminar: "Para excluir sua conta, digite a palavra \"{{palabra}}\" exatamente assim.",
    seguridadSinConfirmar: "Não consegui confirmar a segurança da sua conta, então não apaguei nada. Tente de novo daqui a pouco.",
    noPudeBorrarTodo: "Não consegui apagar todos os seus dados, então sua conta continua igual. Tente de novo daqui a pouco.",
  },
};

const de: typeof es = {
  comun: {
    cuerpoInvalido: "ungültiger Anfrageinhalt",
    necesitasCuenta: "dafür brauchst du dein Konto",
    algoSeAtoro: "etwas hat gehakt; versuch es noch einmal",
    algoSeAtoroMomento: "bei uns hat etwas gehakt; versuch es gleich noch einmal",
    correoInvalido: "gib eine gültige E-Mail-Adresse ein",
  },
  entrar: {
    faltanDatos: "gib deine E-Mail-Adresse und dein Passwort ein",
    sinConfirmar: "Du hast deine E-Mail-Adresse noch nicht bestätigt. Schau in dein Postfach (auch in den Spam-Ordner) oder fordere einen neuen Link an.",
    credencialesMalas: "E-Mail-Adresse oder Passwort ist falsch.",
  },
  registrar: {
    demasiadosIntentos: "Gerade zu viele Versuche. Warte ein paar Minuten und versuch es dann noch einmal.",
    noPudimosCrear: "wir konnten dein Konto nicht erstellen; versuch es gleich noch einmal",
  },
  eliminar: {
    escribeEliminar: "Um dein Konto zu löschen, tippe das Wort „{{palabra}}“ genau so ein.",
    seguridadSinConfirmar: "Ich konnte die Sicherheit deines Kontos nicht bestätigen, deshalb habe ich nichts gelöscht. Versuch es gleich noch einmal.",
    noPudeBorrarTodo: "Ich konnte nicht alle deine Daten löschen, deshalb bleibt dein Konto unverändert. Versuch es gleich noch einmal.",
  },
};

const it: typeof es = {
  comun: {
    cuerpoInvalido: "corpo della richiesta non valido",
    necesitasCuenta: "per questo ti serve il tuo account",
    algoSeAtoro: "qualcosa si è inceppato; riprova",
    algoSeAtoroMomento: "qualcosa si è inceppato da parte nostra; riprova tra un momento",
    correoInvalido: "scrivi un'email valida",
  },
  entrar: {
    faltanDatos: "scrivi la tua email e la tua password",
    sinConfirmar: "Non hai ancora confermato la tua email. Controlla la posta in arrivo (e lo spam) o chiedi un nuovo link.",
    credencialesMalas: "Email o password errate.",
  },
  registrar: {
    demasiadosIntentos: "Troppi tentativi per ora. Aspetta qualche minuto e riprova.",
    noPudimosCrear: "non siamo riusciti a creare il tuo account; riprova tra un momento",
  },
  eliminar: {
    escribeEliminar: "Per eliminare il tuo account scrivi la parola \"{{palabra}}\" esattamente così.",
    seguridadSinConfirmar: "Non ho potuto confermare la sicurezza del tuo account, quindi non ho cancellato niente. Riprova tra un momento.",
    noPudeBorrarTodo: "Non ho potuto cancellare tutti i tuoi dati, quindi il tuo account è rimasto com'era. Riprova tra un momento.",
  },
};

const ja: typeof es = {
  comun: {
    cuerpoInvalido: "リクエストの内容が正しくありません",
    necesitasCuenta: "これにはアカウントが必要です",
    algoSeAtoro: "うまく処理できませんでした。もう一度お試しください",
    algoSeAtoroMomento: "こちらで問題が起きました。少ししてから、もう一度お試しください",
    correoInvalido: "有効なメールアドレスを入力してください",
  },
  entrar: {
    faltanDatos: "メールアドレスとパスワードを入力してください",
    sinConfirmar: "メールアドレスの確認がまだ済んでいません。受信トレイ（迷惑メールフォルダも）を確認するか、新しいリンクをリクエストしてください。",
    credencialesMalas: "メールアドレスまたはパスワードが正しくありません。",
  },
  registrar: {
    demasiadosIntentos: "試行回数が多すぎます。数分待ってから、もう一度お試しください。",
    noPudimosCrear: "アカウントを作成できませんでした。少ししてから、もう一度お試しください",
  },
  eliminar: {
    escribeEliminar: "アカウントを削除するには、「{{palabra}}」とそのまま入力してください。",
    seguridadSinConfirmar: "アカウントのセキュリティを確認できなかったため、何も削除していません。少ししてから、もう一度お試しください。",
    noPudeBorrarTodo: "データをすべて削除できなかったため、アカウントはそのままです。少ししてから、もう一度お試しください。",
  },
};

const zh: typeof es = {
  comun: {
    cuerpoInvalido: "请求体无效",
    necesitasCuenta: "这需要登录你的账户",
    algoSeAtoro: "出了点问题，请重试",
    algoSeAtoroMomento: "我们这边出了点问题，请稍后再试",
    correoInvalido: "请输入有效的邮箱",
  },
  entrar: {
    faltanDatos: "请输入你的邮箱和密码",
    sinConfirmar: "你还没确认邮箱。请查看收件箱（以及垃圾邮件），或重新申请一个链接。",
    credencialesMalas: "邮箱或密码不正确。",
  },
  registrar: {
    demasiadosIntentos: "尝试次数太多了。请等几分钟再试。",
    noPudimosCrear: "没能创建你的账户，请稍后再试",
  },
  eliminar: {
    escribeEliminar: "要删除你的账户，请原样输入“{{palabra}}”。",
    seguridadSinConfirmar: "我没能确认你账户的安全状态，所以什么都没删。请稍后再试。",
    noPudeBorrarTodo: "我没能删除你的全部数据，所以你的账户保持原样。请稍后再试。",
  },
};

const ko: typeof es = {
  comun: {
    cuerpoInvalido: "잘못된 요청 본문",
    necesitasCuenta: "이 작업에는 계정이 필요해요",
    algoSeAtoro: "문제가 생겼어요. 다시 시도해 주세요",
    algoSeAtoroMomento: "저희 쪽에서 문제가 생겼어요. 잠시 후 다시 시도해 주세요",
    correoInvalido: "올바른 이메일 주소를 입력해 주세요",
  },
  entrar: {
    faltanDatos: "이메일과 비밀번호를 입력해 주세요",
    sinConfirmar: "아직 이메일 인증을 하지 않았어요. 받은편지함(스팸함도)을 확인하거나 새 링크를 요청해 주세요.",
    credencialesMalas: "이메일 또는 비밀번호가 올바르지 않아요.",
  },
  registrar: {
    demasiadosIntentos: "시도 횟수가 너무 많아요. 몇 분 기다렸다가 다시 시도해 주세요.",
    noPudimosCrear: "계정을 만들지 못했어요. 잠시 후 다시 시도해 주세요",
  },
  eliminar: {
    escribeEliminar: "계정을 삭제하려면 “{{palabra}}”라고 그대로 입력하세요.",
    seguridadSinConfirmar: "계정 보안을 확인하지 못해서 아무것도 삭제하지 않았어요. 잠시 후 다시 시도해 주세요.",
    noPudeBorrarTodo: "데이터를 모두 삭제하지 못해서 계정은 그대로예요. 잠시 후 다시 시도해 주세요.",
  },
};

const ar: typeof es = {
  comun: {
    cuerpoInvalido: "محتوى الطلب غير صالح",
    necesitasCuenta: "تحتاجون إلى حسابكم لهذا",
    algoSeAtoro: "تعثّر شيء ما؛ حاولوا مجددًا",
    algoSeAtoroMomento: "تعثّر شيء ما من جهتنا؛ حاولوا مجددًا بعد لحظة",
    correoInvalido: "اكتبوا بريدًا إلكترونيًا صالحًا",
  },
  entrar: {
    faltanDatos: "اكتبوا بريدكم الإلكتروني وكلمة المرور",
    sinConfirmar: "لم تؤكّدوا بريدكم الإلكتروني بعد. راجعوا صندوق الوارد (والرسائل غير المرغوب فيها) أو اطلبوا رابطًا جديدًا.",
    credencialesMalas: "البريد الإلكتروني أو كلمة المرور غير صحيحة.",
  },
  registrar: {
    demasiadosIntentos: "محاولات كثيرة جدًا في الوقت الحالي. انتظروا بضع دقائق ثم حاولوا مجددًا.",
    noPudimosCrear: "لم نتمكّن من إنشاء حسابكم؛ حاولوا مجددًا بعد لحظة",
  },
  eliminar: {
    escribeEliminar: "لحذف حسابكم، اكتبوا الكلمة «{{palabra}}» كما هي تمامًا.",
    seguridadSinConfirmar: "لم أتمكّن من التحقق من أمان حسابكم، لذا لم أحذف شيئًا. حاولوا مجددًا بعد لحظة.",
    noPudeBorrarTodo: "لم أتمكّن من حذف كل بياناتكم، لذا بقي حسابكم كما هو. حاولوا مجددًا بعد لحظة.",
  },
};

const hi: typeof es = {
  comun: {
    cuerpoInvalido: "अमान्य अनुरोध",
    necesitasCuenta: "इसके लिए आपको अपना खाता चाहिए",
    algoSeAtoro: "कुछ अटक गया; फिर से कोशिश करें",
    algoSeAtoroMomento: "हमारी तरफ़ कुछ अटक गया; थोड़ी देर में फिर कोशिश करें",
    correoInvalido: "सही ईमेल लिखें",
  },
  entrar: {
    faltanDatos: "अपना ईमेल और पासवर्ड लिखें",
    sinConfirmar: "आपने अभी तक अपने ईमेल की पुष्टि नहीं की है। अपना इनबॉक्स (और स्पैम भी) देखें या नया लिंक माँगें।",
    credencialesMalas: "ईमेल या पासवर्ड गलत है।",
  },
  registrar: {
    demasiadosIntentos: "अभी बहुत ज़्यादा कोशिशें हो गई हैं। कुछ मिनट रुकें और फिर कोशिश करें।",
    noPudimosCrear: "हम आपका खाता नहीं बना पाए; थोड़ी देर में फिर कोशिश करें",
  },
  eliminar: {
    escribeEliminar: "अपना खाता हटाने के लिए \"{{palabra}}\" शब्द ठीक वैसा ही लिखें।",
    seguridadSinConfirmar: "आपके खाते की सुरक्षा की पुष्टि नहीं हो सकी, इसलिए कुछ भी नहीं हटाया गया। थोड़ी देर में फिर कोशिश करें।",
    noPudeBorrarTodo: "आपका सारा डेटा नहीं हटाया जा सका, इसलिए आपका खाता पहले जैसा ही है। थोड़ी देर में फिर कोशिश करें।",
  },
};

export const SERVIDOR_CUENTA: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
