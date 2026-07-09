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
import {
  coincideKeyword,
  evaluarRuta,
  KEYWORDS_ACCION_CLIENTES,
  KEYWORDS_VIABILIDAD_ECONOMICA,
  normalizarTexto,
  type EvaluacionCobertura,
  type Familia,
} from "../readiness";
import { MAX_COSECHA, MAX_COSECHA_PRIORIDAD, SECCION_ECONOMICA_TITULO, TEXTO_FAMILIA_FALTANTE } from "./constants";
import { dominioPermitido, type Grafo } from "./graph";
import type { PrioridadDeclarada } from "./interprete";
import { tokensCosecha } from "./tokens";
import { cerraduraAritmetica, numerosDeMaterial, numerosDeclarados, verificarNumerosHuerfanos } from "../verificadorHuerfanos";

export { SECCION_ECONOMICA_TITULO };

export interface MaterialNodo {
  id: string;
  concepto: string;
  pasos: string[];
  entregable: string;
  es_viabilidad_economica: boolean;
}

export function aMaterial(nid: string, graph: Grafo, families: Record<string, Familia>): MaterialNodo {
  const n = graph[nid];
  return {
    id: nid,
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

export const MARCADOR_AUTODECLARACION = "===JSON===";

/** Port de _parsear_autodeclaracion: separa el markdown del bloque final
 * ===JSON=== (Fase 2.8). Si el delimitador falta, devuelve (raw completo,
 * null). Si el delimitador SI aparece pero el JSON es invalido (Hotfix
 * v2.2.1: la causa real es un ===JSON=== cortado por max_tokens), devuelve
 * el cuerpo YA SEPARADO (sin el marcador ni el JSON roto) en vez de raw
 * completo -- de lo contrario el usuario veria el marcador y el JSON
 * truncado colgando al final de su plan. En ambos casos
 * autodeclaracion=null, y finalizarPlan() cae al respaldo por encabezados
 * (ver familiasDesdeEncabezados). Contrato compacto desde Hotfix v2.2.1:
 * solo familias_tratadas -- se elimino "secciones" (nunca se leia, era
 * puro peso extra en la cola que se cortaba primero al agotar max_tokens). */
/** Fase 3.1: 'etapas' mapea el numero de Etapa (tal como aparece en el
 * markdown, "1", "2", ...) a los node_ids de material_principal/
 * material_de_apoyo cuyo contenido real el redactor uso en esa etapa --
 * ver verificarProcedenciaEtapas. */
export interface AutodeclaracionPlan {
  familias_tratadas?: string[];
  etapas?: Record<string, string[]>;
}

export function parsearAutodeclaracion(raw: string): {
  cuerpo: string;
  autodeclaracion: AutodeclaracionPlan | null;
} {
  const idx = raw.lastIndexOf(MARCADOR_AUTODECLARACION);
  if (idx === -1) return { cuerpo: raw.trim(), autodeclaracion: null };
  const cuerpo = raw.slice(0, idx).trim();
  const bloque = raw.slice(idx + MARCADOR_AUTODECLARACION.length);
  try {
    const data = parsearJson<AutodeclaracionPlan>(bloque);
    return { cuerpo, autodeclaracion: data };
  } catch {
    return { cuerpo, autodeclaracion: null };
  }
}

/**
 * Envuelve un callback de deltas de streaming para que NUNCA reenvie el
 * marcador ===JSON=== ni lo que venga despues -- ese bloque es la
 * autodeclaracion de cobertura (regla 11 de SYSTEM_PLAN), uso interno
 * para finalizarPlan()/parsearAutodeclaracion, jamas contenido para
 * mostrarle a quien esta viendo el plan generarse en vivo.
 *
 * Bug real encontrado en una sesion en vivo (probar.ts): el CLI de Python
 * nunca tuvo este problema porque llama a Claude de forma bloqueante y
 * separa cuerpo/autodeclaracion ANTES de imprimir nada; la web SI
 * streamea el texto crudo del modelo turno a turno segun llega, asi que
 * sin este filtro, el marcador y el JSON de una linea quedan visibles en
 * el stream que ve el usuario (el plan YA GUARDADO en Supabase siempre
 * fue correcto -- finalizarPlan() ya lo parseaba bien -- el bug era
 * puramente de lo que se mostraba en vivo).
 *
 * Mantiene un buffer interno de a lo sumo
 * MARCADOR_AUTODECLARACION.length-1 caracteres sin enviar, por si el
 * marcador llega repartido entre dos chunks consecutivos del stream --
 * por eso expone finalizar(): si el stream termina SIN que el marcador
 * haya aparecido nunca (respuesta malformada, sin la autodeclaracion
 * mandatada), ese ultimo resto pendiente debe liberarse igual en vez de
 * perderse en silencio.
 */
export interface FiltroDeltaAutodeclaracion {
  onChunk: (chunk: string) => void;
  /** Llamar despues de que el stream termine (stream.finalMessage()) para
   * liberar cualquier resto en buffer si el marcador nunca aparecio. */
  finalizar: () => void;
}

export function filtrarDeltaAntesDeAutodeclaracion(onDeltaSeguro: (texto: string) => void): FiltroDeltaAutodeclaracion {
  let acumulado = "";
  let enviado = 0;
  let marcadorEncontrado = false;
  return {
    onChunk(chunk: string) {
      if (marcadorEncontrado) return;
      acumulado += chunk;
      const idx = acumulado.indexOf(MARCADOR_AUTODECLARACION);
      if (idx !== -1) {
        if (idx > enviado) onDeltaSeguro(acumulado.slice(enviado, idx));
        marcadorEncontrado = true;
        enviado = acumulado.length;
        return;
      }
      const limiteSeguro = Math.max(enviado, acumulado.length - (MARCADOR_AUTODECLARACION.length - 1));
      if (limiteSeguro > enviado) {
        onDeltaSeguro(acumulado.slice(enviado, limiteSeguro));
        enviado = limiteSeguro;
      }
    },
    finalizar() {
      if (marcadorEncontrado) return;
      if (acumulado.length > enviado) {
        onDeltaSeguro(acumulado.slice(enviado));
        enviado = acumulado.length;
      }
    },
  };
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
export function evaluacionDesdeAutodeclaracion(autodeclaracion: AutodeclaracionPlan | null): CoberturaPlan {
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

/**
 * Respaldo deterministico (Hotfix v2.2.1) cuando la autodeclaracion de la
 * regla 11 falta o no parsea (causa raiz real: un ===JSON=== cortado por
 * max_tokens en una sesion en vivo). A diferencia del respaldo anterior
 * (evaluarRuta sobre ruta+cosechaIds), esto NO mira los tags de families
 * del material de ENTRADA -- el redactor puede omitir parte de
 * materialDeApoyo si "no encaja con claridad en ninguna etapa" (regla 2),
 * asi que un tag de entrada no garantiza que la familia realmente quedo
 * cubierta en la SALIDA. En vez de eso, escanea los encabezados REALES
 * del markdown ya generado con las mismas palabras clave de readiness.ts.
 * viabilidad_economica ademas se confirma por la presencia exacta de la
 * seccion fija de sostenibilidad (regla 4), la misma senal que ya usa
 * corregirCoherenciaCobertura.
 */
export function familiasDesdeEncabezados(cuerpo: string): CoberturaPlan {
  const encabezados = cuerpo
    .split("\n")
    .filter((linea) => linea.trim().startsWith("#"))
    .join(" ");
  const textoEncabezados = normalizarTexto(encabezados);
  const tieneAccion = coincideKeyword(textoEncabezados, KEYWORDS_ACCION_CLIENTES);
  const tieneViabilidad =
    cuerpo.includes(SECCION_ECONOMICA_TITULO) || coincideKeyword(textoEncabezados, KEYWORDS_VIABILIDAD_ECONOMICA);
  const faltantes = (["accion_clientes", "viabilidad_economica"] as const)
    .filter((f) => (f === "accion_clientes" ? !tieneAccion : !tieneViabilidad))
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

/** Fase 3.1 (caja de vidrio): el redactor autodeclara, por etapa
 * numerada, que node_ids de materialPrincipal/materialDeApoyo uso
 * realmente (campo 'etapas' del contrato de FORMATO DE SALIDA). Verifica
 * deterministicamente que cada id declarado pertenezca al material que
 * de verdad se le entrego (ruta + cosecha) -- si el modelo inventa un id
 * que nunca vino en el payload, es una alucinacion de procedencia, y se
 * registra 'procedencia_invalida' para revision humana (no bloquea el
 * plan: la seccion ya se escribio, esto es observabilidad, no un
 * guardian que aborte). Port exacto de _verificar_procedencia_etapas. */
export function verificarProcedenciaEtapas(
  autodeclaracion: AutodeclaracionPlan | null,
  ruta: string[],
  cosechaIds: string[],
  registrarEvento?: (evento: Record<string, unknown>) => void
): void {
  const etapas = autodeclaracion?.etapas;
  if (!etapas || typeof etapas !== "object" || Object.keys(etapas).length === 0) return;
  const materialValido = new Set([...ruta, ...cosechaIds]);
  for (const [etapa, ids] of Object.entries(etapas)) {
    if (!Array.isArray(ids)) continue;
    const invalidos = ids.filter((nid) => !materialValido.has(nid));
    if (invalidos.length > 0) {
      registrarEvento?.({ tipo: "procedencia_invalida", etapa, ids_invalidos: invalidos });
    }
  }
}

/** Fase 3.1: la seccion financiera del plan (desde el encabezado fijo
 * SECCION_ECONOMICA_TITULO hasta el proximo encabezado o el final), para
 * acotar el verificador de numeros huerfanos a la parte del plan que
 * realmente habla de dinero. Port exacto de _extraer_seccion_economica. */
export function extraerSeccionEconomica(cuerpo: string): string {
  const idx = cuerpo.indexOf(SECCION_ECONOMICA_TITULO);
  if (idx === -1) return "";
  const lineas = cuerpo.slice(idx).split("\n");
  let fin = lineas.length;
  for (let i = 1; i < lineas.length; i++) {
    if (lineas[i].trim().startsWith("#")) {
      fin = i;
      break;
    }
  }
  return lineas.slice(0, fin).join("\n");
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
  registrarEvento?: (evento: Record<string, unknown>) => void,
  numerosProyecto?: unknown
): ResultadoEnsamblado {
  const { cosechaIds, materialPrincipal, materialDeApoyo, tieneMaterialEconomico, payload } = preparacion;

  let cuerpo: string;
  let autodeclaracion: AutodeclaracionPlan | null = null;
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
    // Hotfix v2.2.1: ver familiasDesdeEncabezados -- jamas se degrada la
    // etiqueta solo porque el JSON de cola se corto.
    evaluacionCobertura = familiasDesdeEncabezados(cuerpo);
    registrarEvento?.({ tipo: "autodeclaracion_fallida" });
  }
  evaluacionCobertura = corregirCoherenciaCobertura(evaluacionCobertura, cuerpo, tieneMaterialEconomico, registrarEvento);
  verificarProcedenciaEtapas(autodeclaracion, ruta, cosechaIds, registrarEvento);

  // Fase 3.1 (caja de vidrio): igual que en el reporte, pero acotado a la
  // seccion financiera del plan -- el redactor no corre calculadora.ts,
  // asi que el conjunto permitido es lo declarado por el usuario mas lo
  // que el propio material del grafo ya menciona.
  const seccionEconomica = extraerSeccionEconomica(cuerpo);
  if (seccionEconomica) {
    const textosMaterial = [...materialPrincipal, ...materialDeApoyo].flatMap((m) => [...m.pasos, m.entregable]);
    const numerosPermitidosPlan = cerraduraAritmetica(
      new Set([...numerosDeclarados(numerosProyecto), ...numerosDeMaterial(textosMaterial)])
    );
    verificarNumerosHuerfanos(seccionEconomica, numerosPermitidosPlan, registrarEvento);
  }

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
