/**
 * planRedactor.ts - Fase 3.0: port de cosechar_vecindario, ensamblar_plan
 * (menos la llamada a Claude en si, que en la web es STREAMING y vive en
 * la ruta) y comprimir_estado_vivo, en prototipo_motor.py.
 *
 * Separacion deliberada de responsabilidades: este modulo es PURO (sin
 * llamadas a Claude) salvo comprimirEstadoVivo, que es una llamada
 * aislada corta (no streaming, 700 tokens). prepararPlan() arma el
 * payload que la ruta envia a Claude; finalizarPlan() toma el texto YA
 * obtenido (por streaming o por el respaldo offline si la llamada fallo)
 * y hace el resto: separar la autodeclaracion, decidir la etiqueta, el
 * post-validador mecanico de coherencia, y ensamblar el markdown final.
 * Mantenerlo puro hace que toda esta logica se pueda probar sin mockear
 * streaming.
 */
import type Anthropic from "@anthropic-ai/sdk";
import { llamarClaude, MODEL_HAIKU, type UsoAcumulado } from "../costmeter";
import { parsearJson } from "../parseJson";
import { SYSTEM_ESTADO_VIVO } from "../prompts";
import { evaluarRuta, type EvaluacionCobertura, type Familia } from "../readiness";
import { MAX_COSECHA, MAX_COSECHA_PRIORIDAD, SECCION_ECONOMICA_TITULO, TEXTO_FAMILIA_FALTANTE } from "./constants";
import { dominioPermitido, type Grafo } from "./graph";
import type { PrioridadDeclarada } from "./interprete";
import { tokensCosecha } from "./tokens";

export { SECCION_ECONOMICA_TITULO };

export interface MaterialNodo {
  concepto: string;
  pasos: string[];
  entregable: string;
  es_viabilidad_economica: boolean;
}

export function aMaterial(nid: string, graph: Grafo, families: Record<string, Familia>): MaterialNodo {
  const n = graph[nid];
  return {
    concepto: n.titulo_concepto,
    pasos: n.pasos_accionables ?? [],
    entregable: n.entregable_esperado ?? "",
    es_viabilidad_economica: (families[nid] ?? "general") === "viabilidad_economica",
  };
}

/** Port de cosechar_vecindario: expande desde la ruta hacia vecinos
 * adyacentes (sin preguntar nada), priorizados por familia faltante, fase
 * mayoritaria de la ruta, y afinidad de palabras clave con perfil_sesion.
 * Si hay prioridad_declarada, reserva hasta MAX_COSECHA_PRIORIDAD cupos
 * para nodos afines a esa prioridad ANTES del puntaje normal. */
export function cosecharVecindario(
  ruta: string[],
  graph: Grafo,
  families: Record<string, Familia>,
  evaluacion: Pick<EvaluacionCobertura, "tiene_accion_clientes" | "tiene_viabilidad_economica">,
  perfilSesion: string | null,
  prioridadDeclarada: PrioridadDeclarada | null = null,
  tope = MAX_COSECHA
): string[] {
  const rutaSet = new Set(ruta);
  const candidatos = new Set<string>();
  for (const nid of ruta) {
    const n = graph[nid];
    if (!n) continue;
    for (const vecino of [...(n.nodos_siguientes ?? []), ...(n.nodos_previos ?? [])]) {
      if (vecino in graph && !rutaSet.has(vecino) && dominioPermitido(vecino, graph)) {
        candidatos.add(vecino);
      }
    }
  }

  const fasesRuta = ruta.filter((nid) => nid in graph).map((nid) => graph[nid].fase_proyecto);
  let faseMayoritaria: string | undefined;
  if (fasesRuta.length > 0) {
    const conteo = new Map<string, number>();
    for (const f of fasesRuta) conteo.set(f, (conteo.get(f) ?? 0) + 1);
    faseMayoritaria = [...conteo.entries()].sort((a, b) => b[1] - a[1])[0][0];
  }

  const familiasFaltantes = new Set<string>();
  if (!evaluacion.tiene_accion_clientes) familiasFaltantes.add("accion_clientes");
  if (!evaluacion.tiene_viabilidad_economica) familiasFaltantes.add("viabilidad_economica");

  const perfilTokens = perfilSesion ? tokensCosecha(perfilSesion) : new Set<string>();

  const seleccionados: string[] = [];
  const candidatosRestantes = new Set(candidatos);

  const textoPrioridad = prioridadDeclarada?.texto ?? null;
  if (textoPrioridad) {
    const prioridadTokens = tokensCosecha(textoPrioridad);
    if (prioridadTokens.size > 0) {
      const afinidadPrioridad = (nid: string): number => {
        const n = graph[nid];
        const textoNodo =
          `${n.titulo_concepto ?? ""} ${(n.resumen_teorico ?? "").slice(0, 300)} ` +
          `${(n.condiciones_activacion ?? []).join(" ")}`;
        let c = 0;
        for (const t of tokensCosecha(textoNodo)) if (prioridadTokens.has(t)) c++;
        return c;
      };
      const reservados = [...candidatosRestantes]
        .filter((nid) => afinidadPrioridad(nid) > 0)
        .sort((a, b) => afinidadPrioridad(b) - afinidadPrioridad(a))
        .slice(0, MAX_COSECHA_PRIORIDAD);
      seleccionados.push(...reservados);
      for (const r of reservados) candidatosRestantes.delete(r);
    }
  }

  const puntaje = (nid: string): number => {
    const n = graph[nid];
    let p = 0;
    if (familiasFaltantes.has(families[nid] ?? "general")) p += 10;
    if (n.fase_proyecto === faseMayoritaria) p += 3;
    if (perfilTokens.size > 0) {
      const textoNodo = `${n.titulo_concepto ?? ""} ${(n.condiciones_activacion ?? []).join(" ")}`;
      let c = 0;
      for (const t of tokensCosecha(textoNodo)) if (perfilTokens.has(t)) c++;
      p += c;
    }
    return p;
  };

  const resto = [...candidatosRestantes].sort((a, b) => puntaje(b) - puntaje(a));
  seleccionados.push(...resto.slice(0, Math.max(0, tope - seleccionados.length)));
  return seleccionados.slice(0, tope);
}

export interface PayloadPlan {
  entrada_original: string;
  perfil_sesion: string | null;
  material_principal: MaterialNodo[];
  material_de_apoyo: MaterialNodo[];
  bloqueo_declarado: string | null;
  es_seguimiento?: true;
  estado_vivo_previo?: string | null;
}

export interface PreparacionPlan {
  payload: PayloadPlan;
  cosechaIds: string[];
  materialPrincipal: MaterialNodo[];
  materialDeApoyo: MaterialNodo[];
  tieneMaterialEconomico: boolean;
}

/** Arma todo lo que la ruta necesita ANTES de llamar a Claude: el
 * material principal (la ruta conversada), la cosecha del vecindario, y
 * el payload exacto que espera SYSTEM_PLAN. No llama a la API. */
export function prepararPlan(
  ruta: string[],
  graph: Grafo,
  families: Record<string, Familia>,
  textoOriginal: string,
  perfilSesion: string | null,
  prioridadDeclarada: PrioridadDeclarada | null,
  esSeguimiento: boolean,
  estadoVivoPrevio: string | null
): PreparacionPlan {
  const evaluacionRuta = evaluarRuta(ruta, families);
  const materialPrincipal = ruta.map((nid) => aMaterial(nid, graph, families));
  const cosechaIds = cosecharVecindario(ruta, graph, families, evaluacionRuta, perfilSesion, prioridadDeclarada);
  const materialDeApoyo = cosechaIds.map((nid) => aMaterial(nid, graph, families));
  const tieneMaterialEconomico = [...materialPrincipal, ...materialDeApoyo].some((m) => m.es_viabilidad_economica);

  const payload: PayloadPlan = {
    entrada_original: textoOriginal,
    perfil_sesion: perfilSesion,
    material_principal: materialPrincipal,
    material_de_apoyo: materialDeApoyo,
    bloqueo_declarado: prioridadDeclarada?.texto ?? null,
  };
  if (esSeguimiento) {
    payload.es_seguimiento = true;
    payload.estado_vivo_previo = estadoVivoPrevio;
  }

  return { payload, cosechaIds, materialPrincipal, materialDeApoyo, tieneMaterialEconomico };
}

/** Port de _parsear_autodeclaracion: separa el markdown del bloque final
 * ===JSON=== (Fase 2.8). Si el delimitador falta o el JSON es invalido,
 * devuelve (raw completo, null) -- "sin autodeclaracion". */
export function parsearAutodeclaracion(raw: string): {
  cuerpo: string;
  autodeclaracion: { familias_tratadas?: string[]; secciones?: string[] } | null;
} {
  const marcador = "===JSON===";
  const idx = raw.lastIndexOf(marcador);
  if (idx === -1) return { cuerpo: raw.trim(), autodeclaracion: null };
  const cuerpo = raw.slice(0, idx).trim();
  const bloque = raw.slice(idx + marcador.length);
  try {
    const data = parsearJson<{ familias_tratadas?: string[]; secciones?: string[] }>(bloque);
    return { cuerpo, autodeclaracion: data };
  } catch {
    return { cuerpo: raw.trim(), autodeclaracion: null };
  }
}

export interface CoberturaPlan {
  es_completa: boolean;
  tiene_accion_clientes: boolean;
  tiene_viabilidad_economica: boolean;
  familias_faltantes: string[];
}

/** Port de _evaluacion_desde_autodeclaracion: construye el mismo shape
 * que evaluarRuta, pero a partir de lo que el REDACTOR declaro que el
 * plan realmente trata -- la UNICA fuente para la etiqueta del plan y la
 * seccion "no cubre", coherente por construccion. */
export function evaluacionDesdeAutodeclaracion(
  autodeclaracion: { familias_tratadas?: string[] } | null
): CoberturaPlan {
  const tratadas = new Set(autodeclaracion?.familias_tratadas ?? []);
  const tieneAccion = tratadas.has("accion_clientes");
  const tieneViabilidad = tratadas.has("viabilidad_economica");
  const faltantes = ["accion_clientes", "viabilidad_economica"]
    .filter((f) => !tratadas.has(f))
    .map((f) => TEXTO_FAMILIA_FALTANTE[f]);
  return {
    es_completa: tieneAccion && tieneViabilidad,
    tiene_accion_clientes: tieneAccion,
    tiene_viabilidad_economica: tieneViabilidad,
    familias_faltantes: faltantes,
  };
}

/** Post-validador MECANICO (Motor v2.2) de la incoherencia etiqueta/
 * contenido: si el material ya traia un concepto de viabilidad economica
 * Y el redactor efectivamente escribio la seccion fija de sostenibilidad,
 * 'viabilidad_economica' NUNCA puede aparecer en "no cubre" -- sin
 * importar lo que el redactor autodeclaro. Ya no depende de que el
 * modelo lo declare bien: se verifica contra el propio markdown
 * generado, en codigo (3a reincidencia de este bug, ver AUD-06). */
export function corregirCoherenciaCobertura(
  evaluacionCobertura: CoberturaPlan,
  cuerpo: string,
  tieneMaterialEconomico: boolean,
  registrarEvento?: (evento: Record<string, unknown>) => void
): CoberturaPlan {
  const seccionPresente = tieneMaterialEconomico && cuerpo.includes(SECCION_ECONOMICA_TITULO);
  if (seccionPresente && !evaluacionCobertura.tiene_viabilidad_economica) {
    registrarEvento?.({ tipo: "coherencia_cobertura_corregida", familia: "viabilidad_economica" });
    return {
      ...evaluacionCobertura,
      tiene_viabilidad_economica: true,
      familias_faltantes: evaluacionCobertura.familias_faltantes.filter(
        (f) => f !== TEXTO_FAMILIA_FALTANTE.viabilidad_economica
      ),
      es_completa: evaluacionCobertura.tiene_accion_clientes,
    };
  }
  return evaluacionCobertura;
}

/** Port de _ensamblar_offline: respaldo sin IA (fallo de red/presupuesto
 * en la llamada al redactor) -- concatena el material sin narrar. */
export function ensamblarOffline(material: MaterialNodo[], perfilSesion: string | null, textoOriginal: string): string {
  const out: string[] = ["# Tu plan de accion", ""];
  if (textoOriginal || perfilSesion) {
    out.push("## Contexto");
    if (textoOriginal) out.push(`Punto de partida: ${textoOriginal}`);
    if (perfilSesion) out.push(`Lo que sabemos de tu idea: ${perfilSesion}`);
    out.push("");
  }
  material.forEach((m, i) => {
    out.push(`## Etapa ${i + 1}: ${m.concepto}`);
    m.pasos.forEach((p, j) => out.push(`  ${i + 1}.${j + 1} ${p}`));
    if (m.entregable) out.push(`  Punto de control: ${m.entregable}`);
    out.push("");
  });
  return out.join("\n");
}

export function extraerTitulo(planMd: string): string | null {
  for (const linea of planMd.split("\n")) {
    const t = linea.trim();
    if (t.startsWith("# ")) return t.slice(2).trim();
  }
  return null;
}

export interface ResultadoEnsamblado {
  markdown: string;
  cosechaIds: string[];
  evaluacionCobertura: CoberturaPlan;
}

/**
 * Toma el texto YA obtenido del redactor (rawTextoModelo=null si la
 * llamada a Claude fallo y se debe usar el respaldo offline) y hace todo
 * lo demas: separar la autodeclaracion, decidir la evaluacion de
 * cobertura, el post-validador mecanico, y ensamblar el markdown final
 * con su etiqueta y la seccion "no cubre".
 */
export function finalizarPlan(
  rawTextoModelo: string | null,
  preparacion: PreparacionPlan,
  ruta: string[],
  families: Record<string, Familia>,
  textoOriginal: string,
  registrarEvento?: (evento: Record<string, unknown>) => void
): ResultadoEnsamblado {
  const { cosechaIds, materialPrincipal, tieneMaterialEconomico, payload } = preparacion;

  let cuerpo: string;
  let autodeclaracion: { familias_tratadas?: string[] } | null = null;
  if (rawTextoModelo !== null) {
    const parsed = parsearAutodeclaracion(rawTextoModelo);
    cuerpo = parsed.cuerpo;
    autodeclaracion = parsed.autodeclaracion;
  } else {
    cuerpo = ensamblarOffline(materialPrincipal, payload.perfil_sesion, textoOriginal);
  }

  let evaluacionCobertura: CoberturaPlan;
  if (autodeclaracion !== null) {
    evaluacionCobertura = evaluacionDesdeAutodeclaracion(autodeclaracion);
  } else {
    evaluacionCobertura = evaluarRuta([...ruta, ...cosechaIds], families);
  }
  evaluacionCobertura = corregirCoherenciaCobertura(evaluacionCobertura, cuerpo, tieneMaterialEconomico, registrarEvento);

  const etiqueta = evaluacionCobertura.es_completa ? "Plan completo" : "Plan inicial";
  const totalConceptos = ruta.length + cosechaIds.length;
  const partes: string[] = [`_${etiqueta}_`, "", cuerpo];
  partes.push(
    "",
    "---",
    `_Este plan se alimento de ${totalConceptos} conceptos: ${ruta.length} de tu recorrido conversado ` +
      `y ${cosechaIds.length} del vecindario relacionado del grafo._`
  );
  if (!evaluacionCobertura.es_completa) {
    partes.push("", "## Lo que este plan aun no cubre", "");
    for (const f of evaluacionCobertura.familias_faltantes) partes.push(`- ${f}`);
    partes.push("", "Para profundizar, continua la conversacion en esta misma sesion.");
  }

  return { markdown: partes.join("\n"), cosechaIds, evaluacionCobertura };
}

/** Port de comprimir_estado_vivo: comprime estado_anterior + novedades de
 * la sesion en un estado_vivo nuevo de 300-500 tokens. Respaldo offline:
 * concatena sin comprimir. */
export async function comprimirEstadoVivo(
  client: Anthropic,
  estadoAnterior: string | null,
  perfilSesionNueva: string,
  conceptosNuevosTitulos: string[],
  acumulado: UsoAcumulado
): Promise<{ estadoVivo: string; acumulado: UsoAcumulado }> {
  try {
    const ctx = {
      estado_vivo_anterior: estadoAnterior,
      perfil_actualizado_esta_sesion: perfilSesionNueva,
      conceptos_nuevos_cubiertos: conceptosNuevosTitulos,
    };
    const r = await llamarClaude(client, SYSTEM_ESTADO_VIVO, JSON.stringify(ctx), MODEL_HAIKU, acumulado, {
      maxTokens: 700,
      componente: "estado_vivo",
    });
    return { estadoVivo: r.texto.trim(), acumulado: r.acumulado };
  } catch {
    const estadoVivo = estadoAnterior ? `${estadoAnterior}\n${perfilSesionNueva}`.trim() : perfilSesionNueva;
    return { estadoVivo, acumulado };
  }
}
