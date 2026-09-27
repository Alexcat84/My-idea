/** El acta de cierre en el informe markdown (lib/acta.ts: actaMarkdown). Los
 * "## ", "- " y "**" son estructura markdown y se conservan en cada idioma;
 * {{pct}} es " (NN%)" o vacío. */
import type { PorIdioma } from "../config";

const es = {
  titulo: "## Acta de cierre",
  cerradaEl: "- Cerrada el {{fecha}}",
  accionesAlCerrar: "- Acciones al cerrar: **{{hechas}} de {{total}}**{{pct}}",
  mundo: "- {{mundo}}: **{{hechas}} de {{total}}**{{pct}}, {{estado}}",
  completadoEl: "completado el {{fecha}}",
  abierto: "abierto",
  tituloPorQue: "### Por qué la cerraste aquí",
};

const en: typeof es = {
  titulo: "## Closing record",
  cerradaEl: "- Closed on {{fecha}}",
  accionesAlCerrar: "- Actions at close: **{{hechas}} of {{total}}**{{pct}}",
  mundo: "- {{mundo}}: **{{hechas}} of {{total}}**{{pct}}, {{estado}}",
  completadoEl: "completed on {{fecha}}",
  abierto: "open",
  tituloPorQue: "### Why you closed it here",
};

const fr: typeof es = {
  titulo: "## Bilan de clôture",
  cerradaEl: "- Fermée le {{fecha}}",
  accionesAlCerrar: "- Actions à la fermeture : **{{hechas}} sur {{total}}**{{pct}}",
  mundo: "- {{mundo}} : **{{hechas}} sur {{total}}**{{pct}}, {{estado}}",
  completadoEl: "terminé le {{fecha}}",
  abierto: "ouvert",
  tituloPorQue: "### Pourquoi tu l'as fermée ici",
};

const pt: typeof es = {
  titulo: "## Ata de encerramento",
  cerradaEl: "- Encerrada em {{fecha}}",
  accionesAlCerrar: "- Ações no encerramento: **{{hechas}} de {{total}}**{{pct}}",
  mundo: "- {{mundo}}: **{{hechas}} de {{total}}**{{pct}}, {{estado}}",
  completadoEl: "concluído em {{fecha}}",
  abierto: "aberto",
  tituloPorQue: "### Por que você a encerrou aqui",
};

const de: typeof es = {
  titulo: "## Abschlussprotokoll",
  cerradaEl: "- Abgeschlossen am {{fecha}}",
  accionesAlCerrar: "- Schritte beim Abschluss: **{{hechas}} von {{total}}**{{pct}}",
  mundo: "- {{mundo}}: **{{hechas}} von {{total}}**{{pct}}, {{estado}}",
  completadoEl: "abgeschlossen am {{fecha}}",
  abierto: "offen",
  tituloPorQue: "### Warum du sie hier abgeschlossen hast",
};

const it: typeof es = {
  titulo: "## Verbale di chiusura",
  cerradaEl: "- Chiusa il {{fecha}}",
  accionesAlCerrar: "- Azioni alla chiusura: **{{hechas}} su {{total}}**{{pct}}",
  mundo: "- {{mundo}}: **{{hechas}} su {{total}}**{{pct}}, {{estado}}",
  completadoEl: "completato il {{fecha}}",
  abierto: "aperto",
  tituloPorQue: "### Perché l'hai chiusa qui",
};

const ja: typeof es = {
  titulo: "## 完了記録",
  cerradaEl: "- 締めくくった日：{{fecha}}",
  accionesAlCerrar: "- 締めくくり時のアクション：**{{hechas}}/{{total}}**{{pct}}",
  mundo: "- {{mundo}}：**{{hechas}}/{{total}}**{{pct}}、{{estado}}",
  completadoEl: "{{fecha}}に完了",
  abierto: "未完了",
  tituloPorQue: "### ここで締めくくった理由",
};

const zh: typeof es = {
  titulo: "## 结项记录",
  cerradaEl: "- 收尾日期：{{fecha}}",
  accionesAlCerrar: "- 收尾时的行动：**已完成 {{hechas}}/{{total}}**{{pct}}",
  mundo: "- {{mundo}}：**已完成 {{hechas}}/{{total}}**{{pct}}，{{estado}}",
  completadoEl: "已于 {{fecha}} 完成",
  abierto: "进行中",
  tituloPorQue: "### 你为什么选择在这里收尾",
};

const ko: typeof es = {
  titulo: "## 마무리 기록",
  cerradaEl: "- 마무리한 날: {{fecha}}",
  accionesAlCerrar: "- 마무리 시점의 실행 항목: **{{total}}개 중 {{hechas}}개**{{pct}}",
  mundo: "- {{mundo}}: **{{total}}개 중 {{hechas}}개**{{pct}}, {{estado}}",
  completadoEl: "{{fecha}} 완료",
  abierto: "진행 중",
  tituloPorQue: "### 여기서 마무리한 이유",
};

const ar: typeof es = {
  titulo: "## محضر الإغلاق",
  cerradaEl: "- أُغلقت في {{fecha}}",
  accionesAlCerrar: "- الإجراءات عند الإغلاق: **{{hechas}} من {{total}}**{{pct}}",
  mundo: "- {{mundo}}: **{{hechas}} من {{total}}**{{pct}}، {{estado}}",
  completadoEl: "اكتمل في {{fecha}}",
  abierto: "مفتوح",
  tituloPorQue: "### لماذا أغلقتموها هنا",
};

const hi: typeof es = {
  titulo: "## समापन रिकॉर्ड",
  cerradaEl: "- {{fecha}} को बंद किया गया",
  accionesAlCerrar: "- बंद करते समय कदम: **{{total}} में से {{hechas}}**{{pct}}",
  mundo: "- {{mundo}}: **{{total}} में से {{hechas}}**{{pct}}, {{estado}}",
  completadoEl: "{{fecha}} को पूरी हुई",
  abierto: "खुली है",
  tituloPorQue: "### आपने इसे यहाँ क्यों बंद किया",
};

export const ACTA: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
