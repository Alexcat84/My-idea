/** El dictado por voz: el botón del micrófono (CampoConVoz) y los motivos por los
 * que el dictado se apaga (lib/useSpeech.ts, mensajeErrorVoz). */
import type { PorIdioma } from "../config";

const es = {
  detenerDictado: "Detener dictado",
  dictarPorVoz: "Dictar por voz",
  errores: {
    sinPermiso:
      "Tu navegador no me dio permiso para usar el micrófono. Puedes escribir, o darle permiso en la configuración del navegador.",
    sinMicrofono: "No encontré un micrófono. Puedes escribir tu respuesta.",
    silencioLargo: "Apagué el micrófono porque dejé de oírte. Tócalo para seguir dictando.",
    cortado: "El dictado se cortó. Puedes volver a intentarlo o escribir.",
  },
};

const en: typeof es = {
  detenerDictado: "Stop dictating",
  dictarPorVoz: "Dictate with your voice",
  errores: {
    sinPermiso:
      "Your browser didn't give me permission to use the microphone. You can type instead, or allow it in your browser settings.",
    sinMicrofono: "I couldn't find a microphone. You can type your answer.",
    silencioLargo: "I turned off the microphone because I stopped hearing you. Tap it to keep dictating.",
    cortado: "Dictation cut out. You can try again or type instead.",
  },
};

const fr: typeof es = {
  detenerDictado: "Arrêter la dictée",
  dictarPorVoz: "Dicter à voix haute",
  errores: {
    sinPermiso: "Ton navigateur ne m'a pas donné la permission d'utiliser le micro. Tu peux écrire, ou l'autoriser dans les paramètres du navigateur.",
    sinMicrofono: "Je n'ai pas trouvé de micro. Tu peux écrire ta réponse.",
    silencioLargo: "J'ai éteint le micro parce que je ne t'entendais plus. Touche-le pour continuer à dicter.",
    cortado: "La dictée s'est interrompue. Tu peux réessayer ou écrire.",
  },
};

const pt: typeof es = {
  detenerDictado: "Parar ditado",
  dictarPorVoz: "Ditar por voz",
  errores: {
    sinPermiso: "Seu navegador não me deu permissão para usar o microfone. Você pode escrever ou dar permissão nas configurações do navegador.",
    sinMicrofono: "Não encontrei um microfone. Você pode escrever sua resposta.",
    silencioLargo: "Desliguei o microfone porque parei de ouvir você. Toque nele para continuar ditando.",
    cortado: "O ditado foi interrompido. Você pode tentar de novo ou escrever.",
  },
};

const de: typeof es = {
  detenerDictado: "Diktat beenden",
  dictarPorVoz: "Per Sprache diktieren",
  errores: {
    sinPermiso: "Dein Browser hat mir keinen Zugriff auf das Mikrofon erlaubt. Du kannst schreiben oder den Zugriff in den Browsereinstellungen erlauben.",
    sinMicrofono: "Ich habe kein Mikrofon gefunden. Du kannst deine Antwort schreiben.",
    silencioLargo: "Ich habe das Mikrofon ausgeschaltet, weil ich dich nicht mehr gehört habe. Tippe darauf, um weiter zu diktieren.",
    cortado: "Das Diktat wurde unterbrochen. Du kannst es noch einmal versuchen oder schreiben.",
  },
};

const it: typeof es = {
  detenerDictado: "Ferma la dettatura",
  dictarPorVoz: "Detta a voce",
  errores: {
    sinPermiso: "Il tuo browser non mi ha dato il permesso di usare il microfono. Puoi scrivere, oppure dargli il permesso nelle impostazioni del browser.",
    sinMicrofono: "Non ho trovato un microfono. Puoi scrivere la tua risposta.",
    silencioLargo: "Ho spento il microfono perché non ti sentivo più. Toccalo per continuare a dettare.",
    cortado: "La dettatura si è interrotta. Puoi riprovare o scrivere.",
  },
};

const ja: typeof es = {
  detenerDictado: "音声入力を停止",
  dictarPorVoz: "音声で入力",
  errores: {
    sinPermiso: "ブラウザからマイクの使用が許可されませんでした。文字で入力するか、ブラウザの設定でマイクを許可してください。",
    sinMicrofono: "マイクが見つかりませんでした。文字で入力できます。",
    silencioLargo: "声が聞こえなくなったので、マイクをオフにしました。続けるにはマイクをタップしてください。",
    cortado: "音声入力が途切れました。もう一度試すか、文字で入力してください。",
  },
};

const zh: typeof es = {
  detenerDictado: "停止语音输入",
  dictarPorVoz: "语音输入",
  errores: {
    sinPermiso: "你的浏览器没有允许我使用麦克风。你可以直接打字，或者在浏览器设置里开启权限。",
    sinMicrofono: "我没找到麦克风。你可以打字回答。",
    silencioLargo: "我听不到你的声音了，所以关掉了麦克风。点一下它可以继续说。",
    cortado: "语音输入中断了。你可以再试一次，或者直接打字。",
  },
};

const ko: typeof es = {
  detenerDictado: "받아쓰기 멈추기",
  dictarPorVoz: "음성으로 받아쓰기",
  errores: {
    sinPermiso: "브라우저에서 마이크 사용 권한을 받지 못했어요. 직접 입력하거나, 브라우저 설정에서 권한을 허용해 주세요.",
    sinMicrofono: "마이크를 찾지 못했어요. 답을 직접 입력해 주세요.",
    silencioLargo: "목소리가 들리지 않아서 마이크를 껐어요. 다시 누르면 받아쓰기를 이어 갈 수 있어요.",
    cortado: "받아쓰기가 끊겼어요. 다시 시도하거나 직접 입력해 주세요.",
  },
};

const ar: typeof es = {
  detenerDictado: "إيقاف الإملاء",
  dictarPorVoz: "الإملاء بالصوت",
  errores: {
    sinPermiso: "لم يمنحني متصفحكم إذنًا باستخدام الميكروفون. يمكنكم الكتابة، أو منح الإذن من إعدادات المتصفح.",
    sinMicrofono: "لم أجد ميكروفونًا. يمكنكم كتابة إجابتكم.",
    silencioLargo: "أطفأت الميكروفون لأنني لم أعد أسمعكم. اضغطوا عليه لمواصلة الإملاء.",
    cortado: "انقطع الإملاء. يمكنكم المحاولة مرة أخرى أو الكتابة.",
  },
};

const hi: typeof es = {
  detenerDictado: "बोलकर लिखवाना रोकें",
  dictarPorVoz: "बोलकर लिखवाएँ",
  errores: {
    sinPermiso: "आपके ब्राउज़र ने माइक्रोफ़ोन इस्तेमाल करने की अनुमति नहीं दी। चाहें तो लिखें, या ब्राउज़र की सेटिंग में अनुमति दें।",
    sinMicrofono: "कोई माइक्रोफ़ोन नहीं मिला। अपना जवाब लिखकर दें।",
    silencioLargo: "आपकी आवाज़ सुनाई देनी बंद हो गई, इसलिए मैंने माइक्रोफ़ोन बंद कर दिया। आगे बोलने के लिए उस पर टैप करें।",
    cortado: "बोलकर लिखवाना बीच में रुक गया। फिर से कोशिश करें या लिखें।",
  },
};

export const VOZ: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
