/** NotaRapida: el atajo de nota de cada actividad (Manos a la Obra y Calendario). */
import type { PorIdioma } from "../config";

const es = {
  verOEditar: "Ver o editar tu nota",
  anadir: "Añadir una nota",
  cerrarNota: "Cerrar la nota",
  tuNota: "Tu nota",
  placeholder: "Lo que necesites recordar…",
  guardar: "Guardar",
  cerrar: "cerrar",
  quitar: "quitar",
};

const en: typeof es = {
  verOEditar: "View or edit your note",
  anadir: "Add a note",
  cerrarNota: "Close the note",
  tuNota: "Your note",
  placeholder: "Anything you need to remember…",
  guardar: "Save",
  cerrar: "close",
  quitar: "remove",
};

const fr: typeof es = {
  verOEditar: "Voir ou modifier ta note",
  anadir: "Ajouter une note",
  cerrarNota: "Fermer la note",
  tuNota: "Ta note",
  placeholder: "Ce que tu veux retenir…",
  guardar: "Enregistrer",
  cerrar: "fermer",
  quitar: "effacer",
};

const pt: typeof es = {
  verOEditar: "Ver ou editar sua nota",
  anadir: "Adicionar uma nota",
  cerrarNota: "Fechar a nota",
  tuNota: "Sua nota",
  placeholder: "O que você precisar lembrar…",
  guardar: "Salvar",
  cerrar: "fechar",
  quitar: "remover",
};

const de: typeof es = {
  verOEditar: "Deine Notiz ansehen oder bearbeiten",
  anadir: "Notiz hinzufügen",
  cerrarNota: "Notiz schließen",
  tuNota: "Deine Notiz",
  placeholder: "Was du dir merken willst…",
  guardar: "Speichern",
  cerrar: "schließen",
  quitar: "entfernen",
};

const it: typeof es = {
  verOEditar: "Vedi o modifica la tua nota",
  anadir: "Aggiungi una nota",
  cerrarNota: "Chiudi la nota",
  tuNota: "La tua nota",
  placeholder: "Quello che ti serve ricordare…",
  guardar: "Salva",
  cerrar: "chiudi",
  quitar: "rimuovi",
};

const ja: typeof es = {
  verOEditar: "メモを見る・編集する",
  anadir: "メモを追加",
  cerrarNota: "メモを閉じる",
  tuNota: "メモ",
  placeholder: "覚えておきたいこと…",
  guardar: "保存",
  cerrar: "閉じる",
  quitar: "削除",
};

const zh: typeof es = {
  verOEditar: "查看或编辑你的笔记",
  anadir: "添加笔记",
  cerrarNota: "关闭笔记",
  tuNota: "你的笔记",
  placeholder: "你需要记住的事…",
  guardar: "保存",
  cerrar: "关闭",
  quitar: "移除",
};

const ko: typeof es = {
  verOEditar: "메모 보기 또는 수정",
  anadir: "메모 추가",
  cerrarNota: "메모 닫기",
  tuNota: "메모",
  placeholder: "기억해 둘 것…",
  guardar: "저장",
  cerrar: "닫기",
  quitar: "삭제",
};

const ar: typeof es = {
  verOEditar: "عرض ملاحظتكم أو تعديلها",
  anadir: "إضافة ملاحظة",
  cerrarNota: "إغلاق الملاحظة",
  tuNota: "ملاحظتكم",
  placeholder: "ما تحتاجون إلى تذكّره…",
  guardar: "حفظ",
  cerrar: "إغلاق",
  quitar: "إزالة",
};

const hi: typeof es = {
  verOEditar: "अपना नोट देखें या बदलें",
  anadir: "एक नोट जोड़ें",
  cerrarNota: "नोट बंद करें",
  tuNota: "आपका नोट",
  placeholder: "जो भी आपको याद रखना हो…",
  guardar: "सहेजें",
  cerrar: "बंद करें",
  quitar: "हटाएँ",
};

export const NOTA_RAPIDA: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
