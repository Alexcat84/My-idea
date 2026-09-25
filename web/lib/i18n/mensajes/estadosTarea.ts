/** SelectorEstado: las etiquetas de cara de los cinco estados de una tarea y el menú para elegirlos.
 * Las CLAVES de `etiquetas` son los valores de la base (checklist_items.estado): no se traducen. */
import type { PorIdioma } from "../config";

const es = {
  etiquetas: {
    pendiente: "sin empezar",
    empezado: "apenas empezada",
    en_proceso: "en proceso",
    hecho: "hecha",
    no_aplica: "no aplica",
  },
  /** title del disparador: "Estado: hecha · tocar para elegir" */
  tituloDisparador: "Estado: {{estado}} · tocar para elegir",
  /** aria-label del disparador: "hecha. Tocar para elegir el estado" */
  ariaDisparador: "{{estado}}. Tocar para elegir el estado",
  cerrarMenu: "Cerrar el menú de estado",
  comoVa: "¿Cómo va esta tarea?",
  porQueNoAplica: "¿Por qué no aplica?",
  paraTuMemoria: "Para tu propia memoria. Puedes dejarlo en blanco.",
  placeholderMotivo: "No corre para esta idea porque…",
  retirarTarea: "Retirar tarea",
  volver: "volver",
};

const en: typeof es = {
  etiquetas: {
    pendiente: "not started",
    empezado: "just started",
    en_proceso: "in progress",
    hecho: "done",
    no_aplica: "doesn't apply",
  },
  tituloDisparador: "Status: {{estado}} · tap to choose",
  ariaDisparador: "{{estado}}. Tap to choose the status",
  cerrarMenu: "Close the status menu",
  comoVa: "How's this task going?",
  porQueNoAplica: "Why doesn't it apply?",
  paraTuMemoria: "Just for your own memory. You can leave it blank.",
  placeholderMotivo: "It doesn't apply to this idea because…",
  retirarTarea: "Set task aside",
  volver: "back",
};

const fr: typeof es = {
  etiquetas: {
    pendiente: "pas commencée",
    empezado: "tout juste commencée",
    en_proceso: "en cours",
    hecho: "faite",
    no_aplica: "ne s'applique pas",
  },
  tituloDisparador: "Statut : {{estado}} · touche pour choisir",
  ariaDisparador: "{{estado}}. Touche pour choisir le statut",
  cerrarMenu: "Fermer le menu de statut",
  comoVa: "Où en est cette tâche?",
  porQueNoAplica: "Pourquoi ne s'applique-t-elle pas?",
  paraTuMemoria: "Juste pour toi, pour t'en souvenir. Tu peux laisser ce champ vide.",
  placeholderMotivo: "Elle ne s'applique pas à cette idée parce que…",
  retirarTarea: "Mettre la tâche de côté",
  volver: "retour",
};

const pt: typeof es = {
  etiquetas: {
    pendiente: "não iniciada",
    empezado: "recém-iniciada",
    en_proceso: "em andamento",
    hecho: "feita",
    no_aplica: "não se aplica",
  },
  tituloDisparador: "Status: {{estado}} · toque para escolher",
  ariaDisparador: "{{estado}}. Toque para escolher o status",
  cerrarMenu: "Fechar o menu de status",
  comoVa: "Como está indo esta tarefa?",
  porQueNoAplica: "Por que não se aplica?",
  paraTuMemoria: "Para sua própria memória. Pode deixar em branco.",
  placeholderMotivo: "Não se aplica a esta ideia porque…",
  retirarTarea: "Deixar a tarefa de lado",
  volver: "voltar",
};

const de: typeof es = {
  etiquetas: {
    pendiente: "nicht begonnen",
    empezado: "gerade begonnen",
    en_proceso: "in Arbeit",
    hecho: "erledigt",
    no_aplica: "trifft nicht zu",
  },
  tituloDisparador: "Status: {{estado}} · zum Auswählen tippen",
  ariaDisparador: "{{estado}}. Tippen, um den Status zu wählen",
  cerrarMenu: "Statusmenü schließen",
  comoVa: "Wie läuft diese Aufgabe?",
  porQueNoAplica: "Warum trifft sie nicht zu?",
  paraTuMemoria: "Nur für dich, zur Erinnerung. Du kannst es leer lassen.",
  placeholderMotivo: "Passt nicht zu dieser Idee, weil…",
  retirarTarea: "Aufgabe zurückstellen",
  volver: "zurück",
};

const it: typeof es = {
  etiquetas: {
    pendiente: "non iniziata",
    empezado: "appena iniziata",
    en_proceso: "in corso",
    hecho: "fatta",
    no_aplica: "non si applica",
  },
  tituloDisparador: "Stato: {{estado}} · tocca per scegliere",
  ariaDisparador: "{{estado}}. Tocca per scegliere lo stato",
  cerrarMenu: "Chiudi il menu dello stato",
  comoVa: "Come va questa attività?",
  porQueNoAplica: "Perché non si applica?",
  paraTuMemoria: "Solo per la tua memoria. Puoi lasciarlo vuoto.",
  placeholderMotivo: "Non fa per questa idea perché…",
  retirarTarea: "Metti da parte l'attività",
  volver: "indietro",
};

const ja: typeof es = {
  etiquetas: {
    pendiente: "未着手",
    empezado: "着手したばかり",
    en_proceso: "進行中",
    hecho: "完了",
    no_aplica: "対象外",
  },
  tituloDisparador: "状態：{{estado}} · タップして選択",
  ariaDisparador: "{{estado}}。タップして状態を選択",
  cerrarMenu: "状態メニューを閉じる",
  comoVa: "このタスクの状況はどうですか？",
  porQueNoAplica: "なぜ対象外ですか？",
  paraTuMemoria: "自分の記録用です。空欄のままでもかまいません。",
  placeholderMotivo: "このアイデアに当てはまらない理由は…",
  retirarTarea: "タスクを外す",
  volver: "戻る",
};

const zh: typeof es = {
  etiquetas: {
    pendiente: "未开始",
    empezado: "刚开始",
    en_proceso: "进行中",
    hecho: "已完成",
    no_aplica: "不适用",
  },
  tituloDisparador: "状态：{{estado}} · 点击选择",
  ariaDisparador: "{{estado}}。点击选择状态",
  cerrarMenu: "关闭状态菜单",
  comoVa: "这项任务进展如何？",
  porQueNoAplica: "为什么不适用？",
  paraTuMemoria: "只是留给你自己备忘。可以不填。",
  placeholderMotivo: "它不适合这个想法，因为…",
  retirarTarea: "搁置任务",
  volver: "返回",
};

const ko: typeof es = {
  etiquetas: {
    pendiente: "시작 전",
    empezado: "막 시작함",
    en_proceso: "진행 중",
    hecho: "완료",
    no_aplica: "해당 없음",
  },
  tituloDisparador: "상태: {{estado}} · 눌러서 선택",
  ariaDisparador: "{{estado}}. 눌러서 상태 선택",
  cerrarMenu: "상태 메뉴 닫기",
  comoVa: "이 할 일은 어떻게 되고 있나요?",
  porQueNoAplica: "해당 없는 이유는 뭔가요?",
  paraTuMemoria: "나중에 떠올리기 위한 나만의 메모예요. 비워 둬도 괜찮아요.",
  placeholderMotivo: "이 아이디어에 해당하지 않는 이유는…",
  retirarTarea: "할 일 제외하기",
  volver: "돌아가기",
};

const ar: typeof es = {
  etiquetas: {
    pendiente: "لم تبدأ",
    empezado: "بدأت للتو",
    en_proceso: "قيد التنفيذ",
    hecho: "منجزة",
    no_aplica: "لا تنطبق",
  },
  tituloDisparador: "الحالة: {{estado}} · اضغطوا للاختيار",
  ariaDisparador: "{{estado}}. اضغطوا لاختيار الحالة",
  cerrarMenu: "إغلاق قائمة الحالة",
  comoVa: "كيف تسير هذه المهمة؟",
  porQueNoAplica: "لماذا لا تنطبق؟",
  paraTuMemoria: "لذاكرتكم أنتم فقط. يمكنكم تركه فارغًا.",
  placeholderMotivo: "لا تنطبق على هذه الفكرة لأن…",
  retirarTarea: "استبعاد المهمة",
  volver: "رجوع",
};

const hi: typeof es = {
  etiquetas: {
    pendiente: "शुरू नहीं हुआ",
    empezado: "अभी शुरू हुआ",
    en_proceso: "प्रगति पर",
    hecho: "पूरा",
    no_aplica: "लागू नहीं",
  },
  tituloDisparador: "स्थिति: {{estado}} · चुनने के लिए टैप करें",
  ariaDisparador: "{{estado}}। स्थिति चुनने के लिए टैप करें",
  cerrarMenu: "स्थिति वाला मेन्यू बंद करें",
  comoVa: "यह काम कैसा चल रहा है?",
  porQueNoAplica: "यह लागू क्यों नहीं होता?",
  paraTuMemoria: "सिर्फ़ आपकी अपनी याद के लिए। चाहें तो खाली छोड़ दें।",
  placeholderMotivo: "यह इस विचार पर लागू नहीं होता, क्योंकि…",
  retirarTarea: "काम अलग रखें",
  volver: "वापस",
};

export const ESTADOS_TAREA: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
