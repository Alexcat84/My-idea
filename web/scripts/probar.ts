// Fase 3.0.1: cliente interactivo de terminal para probar el cerebro web
// "de verdad" sin esperar a que exista una UI (item 11 de Fase 3.0,
// todavia pendiente a proposito). Mismo mecanismo de autenticacion real
// que web/scripts/vuelo.ts (dev user + cookie-jar de @supabase/ssr), pero
// aqui las respuestas las escribe la persona que corre el script, no un
// guion fijo -- lo mas parecido a "usar la web" que hay sin abrir un
// navegador.
//
// Uso: con `pnpm dev` corriendo en otra terminal (puerto 3000),
//   pnpm probar
// (o: npx tsx scripts/probar.ts)
// Costo real: cada opcion del menu hace llamadas reales a Anthropic
// (Haiku/Sonnet) y, en la entrevista completa, a Voyage AI.
import readline from "node:readline/promises";
import { autenticarComoDevUser, BASE_URL, cargarEnvRaiz, consumirSSE, getJson, postJson } from "./_shared/http";

cargarEnvRaiz();

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

async function preguntar(prompt: string): Promise<string> {
  const r = await rl.question(prompt);
  return r.trim();
}

async function flujoOrganizer(cookie: string) {
  const texto = await preguntar("\nCuéntame tu idea, o en qué punto estás con ella:\n> ");
  console.log("\n(pensando...)\n");
  const r = await postJson(cookie, "/api/organizer", { texto });
  console.log(r.markdown);
  console.log(`\n(costo: $${Number(r.costo_usd).toFixed(4)}, proyecto: ${r.project_id})`);
}

async function flujoEntrevista(cookie: string) {
  const texto = await preguntar("\nCuéntame tu idea, o en qué punto estás con ella:\n> ");
  console.log("\n(pensando...)\n");
  let r = await postJson(cookie, "/api/session/start", { texto });
  const sessionId = String(r.session_id);
  console.log(`(proyecto: ${r.project_id})`);

  while (r.tipo === "pregunta") {
    const nodosNuevos = (r.nodos_nuevos as Array<{ titulo: string; modo: string }> | undefined) ?? [];
    for (const n of nodosNuevos) {
      if (n.modo !== "conversado") console.log(`  (cubierto en silencio: ${n.titulo})`);
    }
    const respuesta = await preguntar(`\n${r.pregunta}\n> `);
    console.log("\n(pensando...)\n");
    r = await postJson(cookie, `/api/session/${sessionId}/turn`, { respuesta });
  }

  if (r.tipo === "salio") {
    console.log("\nHasta pronto.");
    return;
  }
  if (r.tipo === "error_temporal") {
    console.log("\n(hubo un problema de red/presupuesto; intenta de nuevo mas tarde)");
    return;
  }

  console.log(`\n(${r.tipo === "listo_para_plan" ? "listo para generar tu plan" : r.tipo})`);
  const generar = await preguntar("\n¿Generar tu plan ahora? (s/n)\n> ");
  if (generar.toLowerCase() !== "s") return;

  console.log("\nEnsamblando tu plan...\n");
  const resPlan = await fetch(`${BASE_URL}/api/session/${sessionId}/plan`, {
    method: "POST",
    headers: { Cookie: cookie },
  });
  if (!resPlan.ok) {
    console.error(`\n(fallo al generar el plan: HTTP ${resPlan.status})`);
    return;
  }
  await consumirSSE(resPlan, ({ evento, data }) => {
    if (evento === "delta") {
      process.stdout.write((data as { texto: string }).texto);
    } else if (evento === "aviso") {
      console.log(`\n[aviso] ${(data as { mensaje: string }).mensaje}`);
    } else if (evento === "error") {
      console.error(`\n[error] ${JSON.stringify(data)}`);
    } else if (evento === "done") {
      const d = data as { costo_usd: number };
      console.log(`\n\n(costo total de la sesion: $${d.costo_usd.toFixed(4)})`);
    }
  });
}

async function flujoListarProyectos(cookie: string) {
  const r = await getJson(cookie, "/api/projects");
  const proyectos = (r.proyectos as Array<Record<string, unknown>>) ?? [];
  if (proyectos.length === 0) {
    console.log("\nNo tienes proyectos todavía.");
    return;
  }
  console.log("");
  proyectos.forEach((p, i) => {
    console.log(`${i + 1}. [${p.fase_actual}] ${p.titulo ?? "(sin título)"} — ${p.id}`);
  });
}

async function flujoReporte(cookie: string) {
  const projectId = await preguntar("\nID del proyecto (pégalo completo, usa la opción 3 para verlos):\n> ");
  let r = await postJson(cookie, `/api/project/${projectId}/report`, {});
  while (r.tipo === "pregunta") {
    const respuesta = await preguntar(`\n${r.pregunta}\n> `);
    r = await postJson(cookie, `/api/project/${projectId}/report`, { respuesta });
  }
  console.log("\n" + r.contenido);
  console.log(`\n(costo: $${Number(r.costo_usd).toFixed(4)})`);
}

async function menuPrincipal(cookie: string) {
  while (true) {
    console.log("\n" + "=".repeat(60));
    console.log("  MY IDEA — cliente interactivo de la web (Fase 3.0)");
    console.log("=".repeat(60));
    console.log("1. Organizador rápido (una idea, sin entrevista)");
    console.log("2. Nueva entrevista completa (con plan al final)");
    console.log("3. Ver mis proyectos");
    console.log("4. Generar reporte de sostenibilidad de un proyecto");
    console.log("Q. Salir");
    const opcion = await preguntar("\n> ");
    if (opcion.toLowerCase() === "q") break;
    try {
      if (opcion === "1") await flujoOrganizer(cookie);
      else if (opcion === "2") await flujoEntrevista(cookie);
      else if (opcion === "3") await flujoListarProyectos(cookie);
      else if (opcion === "4") await flujoReporte(cookie);
      else console.log("Opción no reconocida.");
    } catch (e) {
      console.error("\nError:", e instanceof Error ? e.message : e);
    }
  }
}

async function main() {
  console.log(`Conectando a ${BASE_URL} y autenticando...`);
  const cookie = await autenticarComoDevUser();
  console.log("Listo.");
  await menuPrincipal(cookie);
  rl.close();
  process.exit(0);
}

main().catch((e) => {
  // Ctrl+D / EOF inesperado en el stdin cierra readline a mitad de una
  // pregunta -- salida limpia en vez de un stack trace, igual de espiritu
  // que SesionInterrumpida en el CLI de Python (leer_entrada).
  if (e instanceof Error && (e as NodeJS.ErrnoException).code === "ERR_USE_AFTER_CLOSE") {
    console.log("\n\nSesión interrumpida. Hasta pronto.");
    process.exit(0);
  }
  console.error("\nError inesperado:", e instanceof Error ? e.stack : e);
  process.exit(1);
});
