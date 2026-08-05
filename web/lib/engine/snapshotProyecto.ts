/**
 * snapshotProyecto.ts — Campaña "Mundos de protección", P1: el SNAPSHOT.
 *
 * Un mundo de protección (Riesgos, HSEQ, Seguridad Digital) no evalúa una idea
 * contada de nuevo: evalúa **las actividades reales** del plan vigente del
 * núcleo. Este módulo arma ese retrato y lo deja listo para viajar como contexto
 * de la entrevista y del diagnóstico.
 *
 * LECTURA PURA, y es la regla que más importa (BANCO §7.1, "el enlace jamás es
 * fusión"): aquí no se escribe NADA. El módulo no toca Supabase, no muta lo que
 * recibe y no tiene efectos. Un mundo lee el núcleo y nunca lo escribe; el
 * snapshot viaja con la sesión y muere con ella. Lo único que sobrevive son los
 * enlaces, que nacen en P2.
 *
 * QUÉ ES "VIGENTE" (adjudicado por el fundador y el auditor): las actividades
 * del **ciclo vigente** del núcleo (el plan de núcleo más reciente),
 * **incluyendo las ya hechas** —con su estado marcado, porque lo que el usuario
 * ya cerró también genera riesgos y explica dónde está parado— y **excluyendo
 * las retiradas** (`no_aplica`): sobre lo que el usuario descartó a propósito no
 * se levanta ninguna protección.
 */
import { esActivo, type Banda, type ChecklistEstado } from "../dbContract";

/** Una actividad del núcleo tal como la ve un mundo de protección. */
export interface ActividadSnapshot {
  /** Índice estable dentro del snapshot (1..N). Es la referencia que usa el
   * enlazador de P2: mandar los uuid costaría ~36 caracteres por actividad
   * (más de mil en un plan normal) sin darle nada al modelo. El mapa índice→id
   * se queda en el servidor, que es donde se necesita. */
  indice: number;
  id: string;
  titulo: string;
  etapa: number;
  estado: ChecklistEstado;
  fecha_base: string | null;
  banda: Banda | null;
}

export interface SnapshotNucleo {
  actividades: ActividadSnapshot[];
  estado_vivo: string | null;
}

/** Lo mínimo que necesita una fila del checklist para entrar al snapshot. */
export interface FilaChecklistSnapshot {
  id: string;
  texto: string;
  etapa: number;
  orden: number;
  estado: ChecklistEstado;
  fecha_base?: string | null;
  banda?: Banda | null;
}

/** El estado en palabras de persona. Mapa propio a propósito: este módulo es del
 * motor y no puede depender de un componente de pantalla. */
const ESTADO_EN_PALABRAS: Record<ChecklistEstado, string> = {
  pendiente: "sin empezar",
  empezado: "apenas empezada",
  en_proceso: "en proceso",
  hecho: "hecha",
  no_aplica: "retirada",
};

/**
 * Arma el snapshot desde las filas del checklist del ciclo vigente del núcleo.
 * PURO: ordena, filtra las retiradas y numera. No muta la entrada.
 */
export function armarSnapshot(
  filas: FilaChecklistSnapshot[],
  estadoVivo: string | null = null
): SnapshotNucleo {
  const vivas = filas
    .filter((f) => esActivo(f.estado))
    .slice()
    .sort((a, b) => a.etapa - b.etapa || a.orden - b.orden);
  return {
    actividades: vivas.map((f, i) => ({
      indice: i + 1,
      id: f.id,
      titulo: f.texto,
      etapa: f.etapa,
      estado: f.estado,
      fecha_base: f.fecha_base ?? null,
      banda: f.banda ?? null,
    })),
    estado_vivo: estadoVivo,
  };
}

/** La fecha en formato corto para el contexto ("14 ago"). Sin año: el snapshot
 * es de un plan en curso y el año solo gastaría tokens. */
function fechaCorta(iso: string): string {
  const d = new Date(iso);
  if (Number.isNaN(d.getTime())) return "";
  const MESES = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"];
  return `${d.getDate()} ${MESES[d.getMonth()]}`;
}

/**
 * El snapshot como texto compacto, listo para inyectar en un prompt. Una línea
 * por actividad, con su índice para que el enlazador pueda apuntar a ella.
 * No lleva el uuid (ver `ActividadSnapshot.indice`) ni el año de las fechas: en
 * un contexto que viaja en cada llamada, cada carácter se paga.
 */
export function snapshotComoTexto(s: SnapshotNucleo): string {
  if (s.actividades.length === 0) return "";
  const lineas = s.actividades.map((a) => {
    const partes = [`#${a.indice}`, `E${a.etapa}`, a.titulo, ESTADO_EN_PALABRAS[a.estado]];
    if (a.fecha_base) partes.push(fechaCorta(a.fecha_base));
    if (a.banda) partes.push(a.banda);
    return partes.join(" · ");
  });
  return ["Actividades vigentes del plan de la persona:", ...lineas].join("\n");
}

/**
 * Tope declarado del snapshot en tokens aproximados. Un plan real (5 etapas, 31
 * actividades) ronda los 600; el tope deja aire para un plan grande sin permitir
 * que un caso raro infle cada llamada de la entrevista. Si un día se supera, es
 * mejor enterarse por un test que por la factura.
 */
export const TOPE_TOKENS_SNAPSHOT = 1200;

/** Estimación de tokens por caracteres (~4 por token en español). Sirve para
 * medir el snapshot en los tests y para decidir si hay que recortarlo, no para
 * facturar: la cuenta real la lleva costmeter con el uso que devuelve la API. */
export function tokensAprox(texto: string): number {
  return Math.ceil(texto.length / 4);
}
