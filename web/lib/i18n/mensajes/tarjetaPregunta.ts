/** La tarjeta de pregunta de la entrevista (app/ui/TarjetaPregunta.tsx). */
import type { PorIdioma } from "../config";

const es = {
  placeholder: "Cuéntame con tus palabras…",
  responder: "Responder",
  pensando: "Pensando…",
};

const en: typeof es = {
  placeholder: "Tell me in your own words…",
  responder: "Answer",
  pensando: "Thinking…",
};

const fr: typeof es = {
  placeholder: "Raconte-moi avec tes mots…",
  responder: "Répondre",
  pensando: "Je réfléchis…",
};

const pt: typeof es = {
  placeholder: "Me conte com suas palavras…",
  responder: "Responder",
  pensando: "Pensando…",
};

const de: typeof es = {
  placeholder: "Erzähl es mir in deinen Worten…",
  responder: "Antworten",
  pensando: "Ich denke nach…",
};

const it: typeof es = {
  placeholder: "Raccontamelo con parole tue…",
  responder: "Rispondi",
  pensando: "Ci sto pensando…",
};

const ja: typeof es = {
  placeholder: "自分の言葉で教えてください…",
  responder: "回答する",
  pensando: "考えています…",
};

const zh: typeof es = {
  placeholder: "用你自己的话告诉我…",
  responder: "回答",
  pensando: "正在思考…",
};

const ko: typeof es = {
  placeholder: "내 말로 편하게 들려주세요…",
  responder: "답하기",
  pensando: "생각 중…",
};

const ar: typeof es = {
  placeholder: "حدّثوني بكلماتكم…",
  responder: "إرسال الإجابة",
  pensando: "جارٍ التفكير…",
};

const hi: typeof es = {
  placeholder: "अपने शब्दों में बताइए…",
  responder: "जवाब दें",
  pensando: "सोच जारी है…",
};

export const TARJETA_PREGUNTA: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
