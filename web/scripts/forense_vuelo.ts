// Fase 4.0 — FORENSE DEL VUELO: un solo .md con ABSOLUTAMENTE TODO lo que
// dejó la última corrida de vuelo.ts. Dos fuentes que se complementan:
//
//   1. La TRANSCRIPCIÓN del vuelo (examples/fase3_0_vuelo_web.txt): las
//      preguntas que el motor hizo y las respuestas que se dieron, turno a
//      turno, más cada verificación y los costos reales. Es lo que se vio.
//   2. El FORENSE de cada proyecto que el vuelo creó (reusa construirInforme
//      de forense.ts, sin duplicarlo): el recorrido con el tipo de cada nodo,
//      la DECISIÓN de cada turno con su razonamiento, el score de la brújula
//      por candidato, los saltos con sus perdedores, la procedencia, el
//      veredicto del juez y los costos por componente. Es lo que el motor pensó.
//
// Lee Supabase con service-role (herramienta de operador, como salud.ts).
// CERO API: solo lee lo ya persistido.
//
// Uso: pnpm tsx scripts/forense_vuelo.ts
import { readFileSync, mkdirSync, writeFileSync, existsSync } from "node:fs";
import path from "node:path";
import { cargarEnvRaiz, ROOT } from "./_shared/http";
import { clienteAdmin, construirInforme } from "./forense";

cargarEnvRaiz();

interface FilaProyecto {
  id: string;
  titulo: string | null;
  entrada_original: string | null;
  created_at: string;
}

async function main() {
  const supabase = clienteAdmin();

  // La Parte 2 sale de la Parte 1, no de una ventana de tiempo que adivina:
  // vuelo.ts loguea el project_id de cada fase, asi que la transcripcion
  // DECLARA exactamente los proyectos de su corrida. Una ventana temporal no
  // sirve (dentro de un vuelo hay huecos de +10 min por la fase de macetas, y
  // entre dos corridas seguidas puede haber solo 1 min).
  const tx = path.join(ROOT, "examples", "fase3_0_vuelo_web.txt");
  if (!existsSync(tx)) throw new Error(`sin transcripcion en ${tx}; corre vuelo.ts primero`);
  const transcripcion = readFileSync(tx, "utf-8");
  const ids = [...new Set([...transcripcion.matchAll(/project_id: ([0-9a-f-]{36})/g)].map((m) => m[1]))];
  if (ids.length === 0) throw new Error("la transcripcion no declara ningun project_id");

  const { data, error } = await supabase
    .from("projects")
    .select("id, titulo, entrada_original, created_at")
    .in("id", ids)
    .order("created_at", { ascending: true });
  if (error) throw error;
  const proyectos = (data ?? []) as FilaProyecto[];
  if (proyectos.length === 0) throw new Error("los proyectos de la transcripcion ya no estan en la base");

  const L: string[] = [];
  L.push("# Forense del vuelo completo — My Idea");
  L.push("");
  L.push(
    "Todo lo que dejó la última corrida de `vuelo.ts`, en un solo documento: lo que el " +
      "usuario simulado vio (preguntas y respuestas, turno a turno) y lo que el motor pensó " +
      "(la decisión de cada turno, el score de la brújula, los saltos y sus candidatos perdedores, " +
      "la procedencia de cada plan, el veredicto del juez y los costos reales)."
  );
  L.push("");
  L.push(`- **Generado:** ${new Date().toISOString().slice(0, 16).replace("T", " ")}`);
  L.push("- **Alcance:** los proyectos que la propia transcripción declara (Parte 2 ⟷ Parte 1)");
  L.push(`- **Proyectos del vuelo:** ${proyectos.length}`);
  L.push("");
  L.push("## Índice");
  proyectos.forEach((p, i) => {
    const nombre = p.titulo ?? (p.entrada_original ?? p.id).slice(0, 70);
    L.push(`${i + 1}. ${nombre} — \`${p.id}\``);
  });
  L.push("");

  // ── Parte 1: la transcripción (lo que se vio) ──
  L.push("---");
  L.push("");
  L.push("# Parte 1 — Transcripción del vuelo (preguntas, respuestas y verificaciones)");
  L.push("");
  L.push("```text");
  L.push(transcripcion.trimEnd());
  L.push("```");
  L.push("");

  // ── Parte 2: el forense por proyecto (lo que el motor pensó) ──
  L.push("---");
  L.push("");
  L.push("# Parte 2 — Forense por proyecto (la caja de vidrio)");
  L.push("");
  for (const [i, p] of proyectos.entries()) {
    const nombre = p.titulo ?? (p.entrada_original ?? p.id).slice(0, 70);
    console.log(`  [${i + 1}/${proyectos.length}] ${nombre}`);
    L.push(`## ${i + 1}. ${nombre}`);
    L.push("");
    const informe = await construirInforme(supabase, p.id);
    // El informe trae su propio "# Forense de sesion — …": se degrada un nivel
    // para que el índice del documento combinado no se rompa.
    L.push(informe.replace(/^#/gm, "##").trimEnd());
    L.push("");
  }

  const outDir = path.join(ROOT, "examples", "forense");
  mkdirSync(outDir, { recursive: true });
  const sello = new Date().toISOString().slice(0, 10);
  const outPath = path.join(outDir, `vuelo_${sello}.md`);
  writeFileSync(outPath, L.join("\n") + "\n", "utf-8");
  console.log(`\nForense del vuelo escrito en ${outPath} (${L.length} lineas, ${proyectos.length} proyectos).`);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
