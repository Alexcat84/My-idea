/** El saldo de créditos: lib/textoSaldo.ts (chip del encabezado y barra de /creditos) y ui/ChipSaldo.tsx. */
import type { PorIdioma } from "../config";

const es = {
  creditos: { one: "{{n}} crédito", other: "{{n}} créditos" },
  reservados: { one: "{{n}} reservado para tu sesión en curso", other: "{{n}} reservados para tu sesión en curso" },
  tituloConReserva: "Disponible: {{saldo}} · {{reservados}}",
  tituloChip: "Tus créditos",
};

const en: typeof es = {
  creditos: { one: "{{n}} credit", other: "{{n}} credits" },
  reservados: { one: "{{n}} reserved for your current session", other: "{{n}} reserved for your current session" },
  tituloConReserva: "{{saldo}} available · {{reservados}}",
  tituloChip: "Your credits",
};

const fr: typeof es = {
  creditos: {
    one: "{{n}} crédit",
    other: "{{n}} crédits",
  },
  reservados: {
    one: "{{n}} réservé pour ta session en cours",
    other: "{{n}} réservés pour ta session en cours",
  },
  tituloConReserva: "Disponible : {{saldo}} · {{reservados}}",
  tituloChip: "Tes crédits",
};

const pt: typeof es = {
  creditos: {
    one: "{{n}} crédito",
    other: "{{n}} créditos",
  },
  reservados: {
    one: "{{n}} reservado para sua sessão em andamento",
    other: "{{n}} reservados para sua sessão em andamento",
  },
  tituloConReserva: "Disponível: {{saldo}} · {{reservados}}",
  tituloChip: "Seus créditos",
};

const de: typeof es = {
  creditos: {
    one: "{{n}} Punkt",
    other: "{{n}} Punkte",
  },
  reservados: {
    one: "{{n}} für deine laufende Sitzung reserviert",
    other: "{{n}} für deine laufende Sitzung reserviert",
  },
  tituloConReserva: "{{saldo}} verfügbar · {{reservados}}",
  tituloChip: "Dein Guthaben",
};

const it: typeof es = {
  creditos: {
    one: "{{n}} credito",
    other: "{{n}} crediti",
  },
  reservados: {
    one: "{{n}} riservato alla tua sessione in corso",
    other: "{{n}} riservati alla tua sessione in corso",
  },
  tituloConReserva: "Disponibile: {{saldo}} · {{reservados}}",
  tituloChip: "I tuoi crediti",
};

const ja: typeof es = {
  creditos: {
    one: "{{n}}ポイント",
    other: "{{n}}ポイント",
  },
  reservados: {
    one: "{{n}}ポイントは進行中のセッション用に確保済み",
    other: "{{n}}ポイントは進行中のセッション用に確保済み",
  },
  tituloConReserva: "利用可能 {{saldo}} · {{reservados}}",
  tituloChip: "ポイント残高",
};

const zh: typeof es = {
  creditos: {
    one: "{{n}}点",
    other: "{{n}}点",
  },
  reservados: {
    one: "{{n}}点已为你进行中的会话预留",
    other: "{{n}}点已为你进行中的会话预留",
  },
  tituloConReserva: "可用{{saldo}} · {{reservados}}",
  tituloChip: "你的点数",
};

const ko: typeof es = {
  creditos: {
    one: "{{n}}크레딧",
    other: "{{n}}크레딧",
  },
  reservados: {
    one: "진행 중인 세션에 {{n}}크레딧 예약됨",
    other: "진행 중인 세션에 {{n}}크레딧 예약됨",
  },
  tituloConReserva: "사용 가능 {{saldo}} · {{reservados}}",
  tituloChip: "나의 크레딧",
};

const ar: typeof es = {
  creditos: {
    one: "{{n}} نقطة",
    other: "{{n}} من النقاط",
  },
  reservados: {
    one: "المحجوز لجلستكم الحالية: {{n}}",
    other: "المحجوز لجلستكم الحالية: {{n}}",
  },
  tituloConReserva: "المتاح: {{saldo}} · {{reservados}}",
  tituloChip: "رصيدكم",
};

const hi: typeof es = {
  creditos: {
    one: "{{n}} क्रेडिट",
    other: "{{n}} क्रेडिट",
  },
  reservados: {
    one: "{{n}} आपके चालू सेशन के लिए रखा गया",
    other: "{{n}} आपके चालू सेशन के लिए रखे गए",
  },
  tituloConReserva: "उपलब्ध: {{saldo}} · {{reservados}}",
  tituloChip: "आपके क्रेडिट",
};

export const SALDO: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
