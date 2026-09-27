/** Borrar una idea desde su cinta en /ideas (app/ui/BorrarIdeaCinta.tsx). */
import type { PorIdioma } from "../config";

const es = {
  borrarla: "¿Borrarla?",
  si: "Sí",
  no: "No",
  ariaBorrar: "Borrar la idea {{nombre}}",
  tituloBorrar: "Borrar idea",
};

const en: typeof es = {
  borrarla: "Delete it?",
  si: "Yes",
  no: "No",
  ariaBorrar: "Delete the idea {{nombre}}",
  tituloBorrar: "Delete idea",
};

const fr: typeof es = {
  borrarla: "La supprimer?",
  si: "Oui",
  no: "Non",
  ariaBorrar: "Supprimer l'idée {{nombre}}",
  tituloBorrar: "Supprimer l'idée",
};

const pt: typeof es = {
  borrarla: "Excluir?",
  si: "Sim",
  no: "Não",
  ariaBorrar: "Excluir a ideia {{nombre}}",
  tituloBorrar: "Excluir ideia",
};

const de: typeof es = {
  borrarla: "Löschen?",
  si: "Ja",
  no: "Nein",
  ariaBorrar: "Die Idee {{nombre}} löschen",
  tituloBorrar: "Idee löschen",
};

const it: typeof es = {
  borrarla: "La elimini?",
  si: "Sì",
  no: "No",
  ariaBorrar: "Elimina l'idea {{nombre}}",
  tituloBorrar: "Elimina idea",
};

const ja: typeof es = {
  borrarla: "削除しますか？",
  si: "はい",
  no: "いいえ",
  ariaBorrar: "アイデア「{{nombre}}」を削除",
  tituloBorrar: "アイデアを削除",
};

const zh: typeof es = {
  borrarla: "要删除吗？",
  si: "是",
  no: "否",
  ariaBorrar: "删除想法“{{nombre}}”",
  tituloBorrar: "删除想法",
};

const ko: typeof es = {
  borrarla: "삭제할까요?",
  si: "네",
  no: "아니요",
  ariaBorrar: "{{nombre}} 아이디어 삭제",
  tituloBorrar: "아이디어 삭제",
};

const ar: typeof es = {
  borrarla: "حذفها؟",
  si: "نعم",
  no: "لا",
  ariaBorrar: "حذف الفكرة {{nombre}}",
  tituloBorrar: "حذف الفكرة",
};

const hi: typeof es = {
  borrarla: "इसे हटाएँ?",
  si: "हाँ",
  no: "नहीं",
  ariaBorrar: "{{nombre}} विचार हटाएँ",
  tituloBorrar: "विचार हटाएँ",
};

export const BORRAR_IDEA: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
