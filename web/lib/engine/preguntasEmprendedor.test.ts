// LA GUARDA del contexto del emprendedor (decision del fundador del 28 sep 2026,
// tras el vuelo del mundo 11): ninguna pregunta en cache de Primer Equipo da por
// hecho que la persona tiene un jefe por encima, un departamento de recursos
// humanos o la estructura de una empresa grande. Puede nombrarlos en
// CONDICIONAL ("si tienes a alguien por encima..."), nunca como un hecho.
//
// "su jefe" no cuenta: en estas preguntas es el jefe del empleado, que es la
// propia persona. Los patrones son los de la medicion del 28 sep 2026 (14 de 347
// preguntas del mundo 11 los traian), afinados asi.
import { describe, expect, it } from "vitest";
import grafo from "../assets/master_graph.json";
import cache from "../assets/preguntas_cache.json";

const PATRONES: Array<[string, RegExp]> = [
  ["jefe propio", /\btu (propio )?jefe\b|\btus jefes\b|\btus? superior(es)?\b/i],
  ["recursos humanos", /recursos humanos|\bRR\.? ?HH\b/i],
  ["empresa grande", /\bequipo directivo\b|\bdirectivos\b|\borganigrama\b|\bdepartamentos?\b|\bdivisi[oó]n(es)?\b/i],
];
const CONDICIONAL = /\bsi (tienes|trabajas|hay|llegas|en tu caso|algun dia|alguna vez|cuentas con)\b/i;

function supuestos(): string[] {
  const nodos = (grafo as { nodos: Record<string, { dominio?: string; deprecado?: boolean }> }).nodos;
  const preguntas = cache as Record<string, { pregunta: string }>;
  const fuera: string[] = [];
  for (const [id, n] of Object.entries(nodos)) {
    if (n.dominio !== "primer_equipo" || n.deprecado || !preguntas[id]) continue;
    const p = preguntas[id].pregunta;
    if (CONDICIONAL.test(p)) continue;
    for (const [nombre, re] of PATRONES) if (re.test(p)) fuera.push(`${id} (${nombre})`);
  }
  return fuera.sort();
}

// BASES CONOCIDAS CON EL SUPUESTO. Ya no se regeneran: por el principio 2 del
// fundador (28 sep 2026, docs/REGLAS_DE_LA_CASA.md) las preguntas base se quedan
// exactamente como estan, y el adaptador (lib/engine/adaptadorPregunta.ts) las
// dice a la persona real; su salida segura es la neutral o la plantilla neutral,
// nunca la base. La lista solo puede ENCOGER: una pregunta NUEVA (--faltantes,
// que nace con la regla unica) que suponga un jefe hace fallar la guarda.
const BASES_CON_SUPUESTO = new Set<string>([
  "acordar_plan_conjunto_jefe",
  "aplicar_ejercicio_codigo_genetico_control",
  "construir_apoyo_equipo_directivo_metodo",
  "disenar_equipo_plan_anual",
  "eliminar_seguimiento_descendente_responsabilizar_dueno",
  "exigir_critica_jefe_reticente",
  "instalar_metodo_contratacion_empresa",
  "pasar_direccion_directa_indirecta",
  "responder_primer_aviso_renuncia_subordinado",
  "transitar_aprendiz_primeros_meses",
  "tratar_jefe_entrenador",
]);

describe("la guarda del contexto del emprendedor (mundo 11)", () => {
  it("la lista de bases conocidas solo encoge: cada una sigue con su supuesto o sale de la lista", () => {
    const siguen = new Set(supuestos().map((x) => x.split(" ")[0]));
    const yaSinSupuesto = [...BASES_CON_SUPUESTO].filter((id) => !siguen.has(id));
    expect(yaSinSupuesto, `ya sin el supuesto y todavia en la lista (sacalos): ${yaSinSupuesto.join(", ")}`).toEqual([]);
  });

  it("ninguna pregunta de Primer Equipo supone jefe, recursos humanos o empresa grande", () => {
    const nuevos = supuestos().filter((x) => !BASES_CON_SUPUESTO.has(x.split(" ")[0]));
    expect(nuevos, nuevos.join("\n")).toEqual([]);
  });
});
