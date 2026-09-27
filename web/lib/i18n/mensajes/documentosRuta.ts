/** GET /api/project/[id]/documentos: títulos, nombres de archivo y textos que la ruta arma para los documentos. */
import type { PorIdioma } from "../config";

const es = {
  noEncontrado: "documento no encontrado",
  noPudimosLeerRegistro: "no pudimos leer tu registro; intenta de nuevo en un momento",
  tituloReporte: "Reporte de {{mundo}}",
  tituloRegistro: "Registro de {{mundo}}",
  encabezadoRegistro: "> {{nombre}} · Registro de {{mundo}} · {{fecha}}",
  tituloBitacora: "Tu bitácora",
  archivoBitacora: "Tu bitácora",
  tituloAnalisis: "Análisis del proyecto",
  archivoAnalisis: "Análisis del proyecto",
  tituloExpediente: "Expediente completo",
  hitoRealizado: "Realizado",
  loQuePendiente: {
    one: "Queda {{n}} acción por delante. Nada se borró: sigue en tu expediente.",
    other: "Quedan {{n}} acciones por delante. Nada se borró: siguen en tu expediente.",
  },
  loQuePendienteConRetiradas: {
    one: "Queda {{n}} acción por delante y {{retiradas}} que retiraste con su motivo. Nada se borró: siguen en tu expediente.",
    other: "Quedan {{n}} acciones por delante y {{retiradas}} que retiraste con su motivo. Nada se borró: siguen en tu expediente.",
  },
};

const en: typeof es = {
  noEncontrado: "document not found",
  noPudimosLeerRegistro: "we couldn't read your register; try again in a moment",
  tituloReporte: "{{mundo}} report",
  tituloRegistro: "{{mundo}} register",
  encabezadoRegistro: "> {{nombre}} · {{mundo}} register · {{fecha}}",
  tituloBitacora: "Your Logbook",
  archivoBitacora: "Your Logbook",
  tituloAnalisis: "Project analysis",
  archivoAnalisis: "Project analysis",
  tituloExpediente: "Full Record",
  hitoRealizado: "Achieved",
  loQuePendiente: {
    one: "{{n}} action is still ahead. Nothing was deleted: it's still in your Full Record.",
    other: "{{n}} actions are still ahead. Nothing was deleted: they're still in your Full Record.",
  },
  loQuePendienteConRetiradas: {
    one: "{{n}} action is still ahead, plus {{retiradas}} you set aside with your reason. Nothing was deleted: they're still in your Full Record.",
    other: "{{n}} actions are still ahead, plus {{retiradas}} you set aside with your reason. Nothing was deleted: they're still in your Full Record.",
  },
};

const fr: typeof es = {
  noEncontrado: "document introuvable",
  noPudimosLeerRegistro: "nous n'avons pas pu lire ton registre; réessaie dans un moment",
  tituloReporte: "Rapport de {{mundo}}",
  tituloRegistro: "Registre de {{mundo}}",
  encabezadoRegistro: "> {{nombre}} · Registre de {{mundo}} · {{fecha}}",
  tituloBitacora: "Ton journal de bord",
  archivoBitacora: "Ton journal de bord",
  tituloAnalisis: "Analyse du projet",
  archivoAnalisis: "Analyse du projet",
  tituloExpediente: "Dossier complet",
  hitoRealizado: "Réalisé",
  loQuePendiente: {
    one: "Il reste {{n}} action à venir. Rien n'a été supprimé : elle est toujours dans ton dossier.",
    other: "Il reste {{n}} actions à venir. Rien n'a été supprimé : elles sont toujours dans ton dossier.",
  },
  loQuePendienteConRetiradas: {
    one: "Il reste {{n}} action à venir, plus celles que tu as mises de côté avec leur motif ({{retiradas}}). Rien n'a été supprimé : tout est toujours dans ton dossier.",
    other: "Il reste {{n}} actions à venir, plus celles que tu as mises de côté avec leur motif ({{retiradas}}). Rien n'a été supprimé : tout est toujours dans ton dossier.",
  },
};

const pt: typeof es = {
  noEncontrado: "documento não encontrado",
  noPudimosLeerRegistro: "não conseguimos ler seu registro; tente de novo daqui a pouco",
  tituloReporte: "Relatório de {{mundo}}",
  tituloRegistro: "Registro de {{mundo}}",
  encabezadoRegistro: "> {{nombre}} · Registro de {{mundo}} · {{fecha}}",
  tituloBitacora: "Seu diário de bordo",
  archivoBitacora: "Seu diario de bordo",
  tituloAnalisis: "Análise do projeto",
  archivoAnalisis: "Análise do projeto",
  tituloExpediente: "Dossiê completo",
  hitoRealizado: "Realizado",
  loQuePendiente: {
    one: "Ainda há {{n}} ação pela frente. Nada foi apagado: ela continua no seu dossiê.",
    other: "Ainda há {{n}} ações pela frente. Nada foi apagado: elas continuam no seu dossiê.",
  },
  loQuePendienteConRetiradas: {
    one: "Ainda há {{n}} ação pela frente e {{retiradas}} que você deixou de lado com o seu motivo. Nada foi apagado: tudo continua no seu dossiê.",
    other: "Ainda há {{n}} ações pela frente e {{retiradas}} que você deixou de lado com o seu motivo. Nada foi apagado: tudo continua no seu dossiê.",
  },
};

const de: typeof es = {
  noEncontrado: "Dokument nicht gefunden",
  noPudimosLeerRegistro: "wir konnten dein Register nicht lesen; versuch es gleich noch einmal",
  tituloReporte: "Bericht zu {{mundo}}",
  tituloRegistro: "Register für {{mundo}}",
  encabezadoRegistro: "> {{nombre}} · Register für {{mundo}} · {{fecha}}",
  tituloBitacora: "Dein Logbuch",
  archivoBitacora: "Dein Logbuch",
  tituloAnalisis: "Projektanalyse",
  archivoAnalisis: "Projektanalyse",
  tituloExpediente: "Vollständiges Dossier",
  hitoRealizado: "Verwirklicht",
  loQuePendiente: {
    one: "Vor dir liegt noch {{n}} Schritt. Nichts wurde gelöscht: Er steht weiter in deinem Dossier.",
    other: "Vor dir liegen noch {{n}} Schritte. Nichts wurde gelöscht: Sie stehen weiter in deinem Dossier.",
  },
  loQuePendienteConRetiradas: {
    one: "Vor dir liegt noch {{n}} Schritt, dazu {{retiradas}}, die du mit Begründung zurückgestellt hast. Nichts wurde gelöscht: Alles steht weiter in deinem Dossier.",
    other: "Vor dir liegen noch {{n}} Schritte, dazu {{retiradas}}, die du mit Begründung zurückgestellt hast. Nichts wurde gelöscht: Alles steht weiter in deinem Dossier.",
  },
};

const it: typeof es = {
  noEncontrado: "documento non trovato",
  noPudimosLeerRegistro: "non siamo riusciti a leggere il tuo registro; riprova tra un momento",
  tituloReporte: "Resoconto di {{mundo}}",
  tituloRegistro: "Registro di {{mundo}}",
  encabezadoRegistro: "> {{nombre}} · Registro di {{mundo}} · {{fecha}}",
  tituloBitacora: "Il tuo diario di bordo",
  archivoBitacora: "Il tuo diario di bordo",
  tituloAnalisis: "Analisi del progetto",
  archivoAnalisis: "Analisi del progetto",
  tituloExpediente: "Fascicolo completo",
  hitoRealizado: "Realizzato",
  loQuePendiente: {
    one: "Resta {{n}} azione da fare. Non è stato cancellato niente: è ancora nel tuo fascicolo.",
    other: "Restano {{n}} azioni da fare. Non è stato cancellato niente: sono ancora nel tuo fascicolo.",
  },
  loQuePendienteConRetiradas: {
    one: "Resta {{n}} azione da fare, più {{retiradas}} che hai messo da parte spiegando il perché. Non è stato cancellato niente: sono ancora nel tuo fascicolo.",
    other: "Restano {{n}} azioni da fare, più {{retiradas}} che hai messo da parte spiegando il perché. Non è stato cancellato niente: sono ancora nel tuo fascicolo.",
  },
};

const ja: typeof es = {
  noEncontrado: "ドキュメントが見つかりません",
  noPudimosLeerRegistro: "記録簿を読み込めませんでした。少ししてから、もう一度お試しください",
  tituloReporte: "{{mundo}}のレポート",
  tituloRegistro: "{{mundo}}の記録簿",
  encabezadoRegistro: "> {{nombre}} · {{mundo}}の記録簿 · {{fecha}}",
  tituloBitacora: "活動ログ",
  archivoBitacora: "活動ログ",
  tituloAnalisis: "プロジェクトの分析",
  archivoAnalisis: "プロジェクトの分析",
  tituloExpediente: "全記録",
  hitoRealizado: "実現",
  loQuePendiente: {
    one: "この先のアクションが{{n}}件残っています。何も消えていません。全記録にそのまま残っています。",
    other: "この先のアクションが{{n}}件残っています。何も消えていません。全記録にそのまま残っています。",
  },
  loQuePendienteConRetiradas: {
    one: "この先のアクションが{{n}}件と、理由を添えて外したものが{{retiradas}}件あります。何も消えていません。全記録にそのまま残っています。",
    other: "この先のアクションが{{n}}件と、理由を添えて外したものが{{retiradas}}件あります。何も消えていません。全記録にそのまま残っています。",
  },
};

const zh: typeof es = {
  noEncontrado: "未找到文档",
  noPudimosLeerRegistro: "没能读取你的登记册，请稍后再试",
  tituloReporte: "{{mundo}}报告",
  tituloRegistro: "{{mundo}}登记册",
  encabezadoRegistro: "> {{nombre}} · {{mundo}}登记册 · {{fecha}}",
  tituloBitacora: "你的日志",
  archivoBitacora: "你的日志",
  tituloAnalisis: "项目分析",
  archivoAnalisis: "项目分析",
  tituloExpediente: "完整档案",
  hitoRealizado: "已实现",
  loQuePendiente: {
    one: "还有{{n}}项行动待完成。什么都没有删除：它们都还在你的完整档案里。",
    other: "还有{{n}}项行动待完成。什么都没有删除：它们都还在你的完整档案里。",
  },
  loQuePendienteConRetiradas: {
    one: "还有{{n}}项行动待完成，另有{{retiradas}}项已由你说明理由后搁置。什么都没有删除：它们都还在你的完整档案里。",
    other: "还有{{n}}项行动待完成，另有{{retiradas}}项已由你说明理由后搁置。什么都没有删除：它们都还在你的完整档案里。",
  },
};

const ko: typeof es = {
  noEncontrado: "문서를 찾을 수 없어요",
  noPudimosLeerRegistro: "등록부를 읽지 못했어요. 잠시 후 다시 시도해 주세요",
  tituloReporte: "{{mundo}} 리포트",
  tituloRegistro: "{{mundo}} 등록부",
  encabezadoRegistro: "> {{nombre}} · {{mundo}} 등록부 · {{fecha}}",
  tituloBitacora: "나의 기록장",
  archivoBitacora: "나의 기록장",
  tituloAnalisis: "프로젝트 분석",
  archivoAnalisis: "프로젝트 분석",
  tituloExpediente: "전체 자료",
  hitoRealizado: "실현",
  loQuePendiente: {
    one: "앞으로 남은 실행 항목이 {{n}}개예요. 지워진 건 없어요. 전체 자료에 그대로 남아 있어요.",
    other: "앞으로 남은 실행 항목이 {{n}}개예요. 지워진 건 없어요. 전체 자료에 그대로 남아 있어요.",
  },
  loQuePendienteConRetiradas: {
    one: "앞으로 남은 실행 항목 {{n}}개와, 이유를 적고 제외한 항목 {{retiradas}}개가 있어요. 지워진 건 없어요. 전체 자료에 그대로 남아 있어요.",
    other: "앞으로 남은 실행 항목 {{n}}개와, 이유를 적고 제외한 항목 {{retiradas}}개가 있어요. 지워진 건 없어요. 전체 자료에 그대로 남아 있어요.",
  },
};

const ar: typeof es = {
  noEncontrado: "المستند غير موجود",
  noPudimosLeerRegistro: "لم نتمكّن من قراءة سجلّكم؛ حاولوا مجددًا بعد لحظة",
  tituloReporte: "تقرير {{mundo}}",
  tituloRegistro: "سجل {{mundo}}",
  encabezadoRegistro: "> {{nombre}} · سجل {{mundo}} · {{fecha}}",
  tituloBitacora: "سجلّ رحلتكم",
  archivoBitacora: "سجل رحلتكم",
  tituloAnalisis: "تحليل المشروع",
  archivoAnalisis: "تحليل المشروع",
  tituloExpediente: "الملف الكامل",
  hitoRealizado: "تحقّق",
  loQuePendiente: {
    one: "يبقى أمامكم {{n}} إجراء. لم يُحذف شيء: ما زال في ملفكم الكامل.",
    other: "الإجراءات الباقية أمامكم: {{n}}. لم يُحذف شيء: ما زالت في ملفكم الكامل.",
  },
  loQuePendienteConRetiradas: {
    one: "يبقى أمامكم {{n}} إجراء، والمستبعدة مع سببها: {{retiradas}}. لم يُحذف شيء: كلها ما زالت في ملفكم الكامل.",
    other: "الإجراءات الباقية أمامكم: {{n}}، والمستبعدة مع سببها: {{retiradas}}. لم يُحذف شيء: كلها ما زالت في ملفكم الكامل.",
  },
};

const hi: typeof es = {
  noEncontrado: "दस्तावेज़ नहीं मिला",
  noPudimosLeerRegistro: "हम आपका रजिस्टर नहीं पढ़ पाए; थोड़ी देर में फिर कोशिश करें",
  tituloReporte: "{{mundo}} की रिपोर्ट",
  tituloRegistro: "{{mundo}} रजिस्टर",
  encabezadoRegistro: "> {{nombre}} · {{mundo}} रजिस्टर · {{fecha}}",
  tituloBitacora: "आपकी लॉगबुक",
  archivoBitacora: "आपकी लॉगबुक",
  tituloAnalisis: "परियोजना का विश्लेषण",
  archivoAnalisis: "परियोजना का विश्लेषण",
  tituloExpediente: "पूरा ब्यौरा",
  hitoRealizado: "साकार",
  loQuePendiente: {
    one: "{{n}} कदम अभी बाकी है। कुछ भी हटाया नहीं गया: सब आपके पूरे ब्यौरे में है।",
    other: "{{n}} कदम अभी बाकी हैं। कुछ भी हटाया नहीं गया: सब आपके पूरे ब्यौरे में है।",
  },
  loQuePendienteConRetiradas: {
    one: "{{n}} कदम अभी बाकी है, और {{retiradas}} को आपने वजह बताकर अलग रखा है। कुछ भी हटाया नहीं गया: सब आपके पूरे ब्यौरे में है।",
    other: "{{n}} कदम अभी बाकी हैं, और {{retiradas}} को आपने वजह बताकर अलग रखा है। कुछ भी हटाया नहीं गया: सब आपके पूरे ब्यौरे में है।",
  },
};

export const DOCUMENTOS_RUTA: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
