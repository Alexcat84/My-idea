/**
 * expediente.ts — Fase 4.6: los documentos que el usuario se lleva.
 *
 * El viaje tiene fases y cada fase deja un documento propio: el plan con el
 * que arrancaste, cada seguimiento que replanteó el camino, y al final el
 * expediente con TODO el desarrollo. Este módulo es PURO: arma el índice y el
 * markdown a partir de lo ya persistido, sin tocar Supabase ni el motor (una
 * descarga no cuesta créditos ni llama al LLM).
 *
 * Confidencialidad (BANCO §5, decisión del fundador): el expediente jamás
 * nombra nodos, grafos, conteos internos ni la mecánica del sistema. Narra el
 * viaje del usuario con lo que el usuario reconoce.
 *
 * Sin guiones largos en el texto generado: es copy visible.
 */
import { fechaHumanaConAno } from "./fechas";

/** Un ciclo del viaje: el plan original o cada seguimiento posterior. */
export interface CicloExpediente {
  planId: string;
  /** 'inicial' | 'completo' | 'seguimiento' */
  etiqueta: string;
  createdAt: string;
  contenidoMd: string;
}

export interface AccionExpediente {
  etapa: number;
  texto: string;
  /** 'pendiente' | 'hecho' | ... (dbContract CHECKLIST_ESTADO) */
  estado: string;
  completedAt: string | null;
  fechaBase: string | null;
}

export interface MundoExpediente {
  nombre: string;
  contenidoMd: string | null;
  completadoAt: string | null;
}

export interface DocumentoIndice {
  /** identificador estable que la UI manda de vuelta para pedir el contenido */
  clave: string;
  tipo: "ciclo" | "expediente";
  titulo: string;
  subtitulo: string;
  /** ISO; null solo si el documento no cuelga de una fecha concreta */
  fecha: string | null;
}

export interface DatosExpediente {
  nombre: string;
  entradaOriginal: string;
  creadaAt: string;
  realizadaAt: string | null;
  cierreMotivo: string | null;
  organizadorMd: string | null;
  ciclos: CicloExpediente[];
  acciones: AccionExpediente[];
  numerosMd: string | null;
  mundos: MundoExpediente[];
  /** el informe de analytics.ts, ya calculado por quien llama */
  informeMd: string | null;
  /** ISO del momento de la descarga (inyectable para tests deterministas) */
  generadoAt: string;
}

/** Clave del documento de un ciclo. La UI la trata como opaca. */
export const claveDeCiclo = (planId: string) => `ciclo:${planId}`;
export const CLAVE_EXPEDIENTE = "expediente";

/**
 * Baja de nivel los títulos de un markdown incrustado: un plan trae su propio
 * `# Título`, y al meterlo bajo un `## ` del expediente la jerarquía quedaría
 * al revés. Respeta los bloques de código cercados (``` y ~~~), donde un `#`
 * es un comentario y no un título.
 */
export function rebajarTitulos(md: string, niveles: number): string {
  if (niveles <= 0) return md;
  let dentroDeCodigo = false;
  let cerca = "";
  return md
    .split("\n")
    .map((linea) => {
      const apertura = /^\s{0,3}(`{3,}|~{3,})/.exec(linea);
      if (apertura) {
        const marca = apertura[1][0];
        if (!dentroDeCodigo) {
          dentroDeCodigo = true;
          cerca = marca;
        } else if (marca === cerca) {
          dentroDeCodigo = false;
        }
        return linea;
      }
      if (dentroDeCodigo) return linea;
      const titulo = /^(#{1,6})(\s)/.exec(linea);
      if (!titulo) return linea;
      // Markdown no pasa de h6: lo que ya está al fondo se queda donde está.
      const nuevo = Math.min(6, titulo[1].length + niveles);
      return "#".repeat(nuevo) + linea.slice(titulo[1].length);
    })
    .join("\n");
}

/**
 * Nombra cada ciclo como lo vive el usuario: el primero es "Tu Plan" y cada
 * uno posterior es un seguimiento numerado. El orden es cronológico, así que
 * la posición manda; la etiqueta de base de datos no se le enseña a nadie.
 */
export function titulosDeCiclos(ciclos: CicloExpediente[]): Array<{ ciclo: CicloExpediente; titulo: string; subtitulo: string }> {
  return ciclos.map((ciclo, i) => {
    if (i === 0) {
      return { ciclo, titulo: "Tu Plan", subtitulo: "El plan con el que arrancaste" };
    }
    return {
      ciclo,
      titulo: `Seguimiento ${i}`,
      subtitulo: "Lo que pasó y el plan recalculado",
    };
  });
}

/** El índice de descargas: un documento por fase del viaje, más el completo. */
export function indiceDeDocumentos(ciclos: CicloExpediente[], realizadaAt: string | null): DocumentoIndice[] {
  const docs: DocumentoIndice[] = titulosDeCiclos(ciclos).map(({ ciclo, titulo, subtitulo }) => ({
    clave: claveDeCiclo(ciclo.planId),
    tipo: "ciclo" as const,
    titulo,
    subtitulo,
    fecha: ciclo.createdAt,
  }));
  // El expediente existe desde el primer plan: antes de eso no hay desarrollo
  // que contar, y ofrecer una descarga vacía sería prometer de más.
  if (docs.length > 0) {
    docs.push({
      clave: CLAVE_EXPEDIENTE,
      tipo: "expediente",
      titulo: "Expediente completo",
      subtitulo: realizadaAt
        ? "Todo tu desarrollo, de la idea al cierre"
        : "Todo tu desarrollo hasta hoy, en un solo documento",
      fecha: realizadaAt,
    });
  }
  return docs;
}

/** El markdown de un ciclo suelto, con su portadilla. */
export function cicloMarkdown(nombre: string, titulo: string, ciclo: CicloExpediente): string {
  const l: string[] = [];
  l.push(`> ${nombre} · ${titulo} · ${fechaHumanaConAno(ciclo.createdAt)}`);
  l.push("");
  l.push(ciclo.contenidoMd.trim());
  l.push("");
  return l.join("\n");
}

function seccionAcciones(acciones: AccionExpediente[]): string[] {
  const l: string[] = [];
  const hechas = acciones.filter((a) => a.estado === "hecho");
  l.push(`Completaste **${hechas.length} de ${acciones.length}** acciones.`);
  l.push("");
  const etapas = [...new Set(acciones.map((a) => a.etapa))].sort((a, b) => a - b);
  for (const etapa of etapas) {
    l.push(`### Etapa ${etapa}`);
    l.push("");
    for (const a of acciones.filter((x) => x.etapa === etapa)) {
      const marca = a.estado === "hecho" ? "x" : " ";
      const cuando = a.completedAt
        ? ` · hecho el ${fechaHumanaConAno(a.completedAt)}`
        : a.fechaBase
          ? ` · previsto para el ${fechaHumanaConAno(a.fechaBase)}`
          : "";
      l.push(`- [${marca}] ${a.texto.replace(/\s+/g, " ").trim()}${cuando}`);
    }
    l.push("");
  }
  return l;
}

/**
 * El expediente completo: la idea como la escribiste, cada ciclo del plan en
 * orden, el registro de lo que hiciste y cuándo, tus números, los mundos que
 * trabajaste y, si la cerraste, cómo te fue.
 */
export function expedienteMarkdown(d: DatosExpediente): string {
  const l: string[] = [];

  l.push(`# ${d.nombre}`);
  l.push("");
  l.push(`> Expediente completo · generado el ${fechaHumanaConAno(d.generadoAt)}`);
  l.push("");
  l.push(`**Empezaste** el ${fechaHumanaConAno(d.creadaAt)}`);
  l.push("");
  l.push(
    d.realizadaAt
      ? `**Estado** Proyecto realizado el ${fechaHumanaConAno(d.realizadaAt)}`
      : "**Estado** En marcha"
  );
  l.push("");

  // Índice: un expediente largo se navega, no se lee de corrido.
  const secciones: string[] = ["Tu idea, tal como la escribiste"];
  if (d.organizadorMd) secciones.push("Tu idea, ordenada");
  const ciclos = titulosDeCiclos(d.ciclos);
  for (const c of ciclos) secciones.push(c.titulo);
  if (d.acciones.length) secciones.push("Lo que hiciste");
  if (d.numerosMd) secciones.push("Tus Números");
  for (const m of d.mundos) if (m.contenidoMd) secciones.push(m.nombre);
  if (d.informeMd) secciones.push("Cómo te fue");

  l.push("## Contenido");
  l.push("");
  for (const s of secciones) l.push(`- ${s}`);
  l.push("");
  l.push("---");
  l.push("");

  l.push("## Tu idea, tal como la escribiste");
  l.push("");
  l.push(d.entradaOriginal.trim());
  l.push("");

  if (d.organizadorMd) {
    l.push("## Tu idea, ordenada");
    l.push("");
    l.push(rebajarTitulos(d.organizadorMd.trim(), 2));
    l.push("");
  }

  for (const { ciclo, titulo } of ciclos) {
    l.push(`## ${titulo}`);
    l.push("");
    l.push(`_${fechaHumanaConAno(ciclo.createdAt)}_`);
    l.push("");
    l.push(rebajarTitulos(ciclo.contenidoMd.trim(), 2));
    l.push("");
  }

  if (d.acciones.length) {
    l.push("## Lo que hiciste");
    l.push("");
    l.push(...seccionAcciones(d.acciones));
  }

  if (d.numerosMd) {
    l.push("## Tus Números");
    l.push("");
    l.push(rebajarTitulos(d.numerosMd.trim(), 2));
    l.push("");
  }

  for (const m of d.mundos) {
    if (!m.contenidoMd) continue;
    l.push(`## ${m.nombre}`);
    l.push("");
    if (m.completadoAt) {
      l.push(`_Lo diste por terminado el ${fechaHumanaConAno(m.completadoAt)}_`);
      l.push("");
    }
    l.push(rebajarTitulos(m.contenidoMd.trim(), 2));
    l.push("");
  }

  if (d.informeMd) {
    l.push("## Cómo te fue");
    l.push("");
    l.push(rebajarTitulos(d.informeMd.trim(), 1));
    l.push("");
  }

  if (d.cierreMotivo) {
    l.push("## Por qué la cerraste aquí");
    l.push("");
    l.push(`> ${d.cierreMotivo.replace(/\s+/g, " ").trim()}`);
    l.push("");
  }

  return l.join("\n");
}

/** Nombre de archivo seguro para la descarga (sin extensión). */
export function nombreArchivo(nombreIdea: string, titulo: string): string {
  const limpio = (s: string) =>
    s
      .replace(/[^\p{L}\p{N} _-]/gu, "")
      .trim()
      .replace(/\s+/g, "-")
      .slice(0, 40);
  const base = limpio(nombreIdea) || "mi-idea";
  const sufijo = limpio(titulo) || "documento";
  return `${base}-${sufijo}`.toLowerCase();
}
