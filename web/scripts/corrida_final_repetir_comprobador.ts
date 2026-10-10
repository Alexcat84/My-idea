/**
 * Repite el comprobador paso contra nodo (punto 3, decision del fundador, 10 oct 2026) sobre las entradas que guardo
 * corrida_final_redactar_planes.ts --comprobador (A_previo/<plan>.md y A_previo/<plan>.json), sin volver a redactar.
 * Cada llamada reserva su peor caso antes de lanzarse (lib/presupuestoGuion.ts).
 *
 * Uso (desde web/, con el .env raiz): npx tsx scripts/corrida_final_repetir_comprobador.ts --dir <salida> [--tope 0.2]
 */
import { readdirSync, readFileSync, writeFileSync } from "node:fs";
import path from "node:path";
import Anthropic from "@anthropic-ai/sdk";
import { comprobarPasos, pasosDelPlan } from "../lib/engine/comprobadorPasos";
import { costoAcumuladoUsd, usoVacio } from "../lib/costmeter";
import { Presupuesto, reservaDeLlamada, TopeAlcanzado } from "../lib/presupuestoGuion";
import { SYSTEM_COMPROBADOR_PASOS } from "../lib/prompts";

const arg = (n: string) => {
  const i = process.argv.indexOf(n);
  return i >= 0 ? process.argv[i + 1] ?? null : null;
};

async function main() {
  const dir = arg("--dir");
  if (!dir) throw new Error("uso: --dir <salida> [--tope 0.2]");
  const presupuesto = new Presupuesto(Number(arg("--tope") ?? 0.2));
  const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });
  const previo = path.join(dir, "A_previo");
  const informe: Array<Record<string, unknown>> = [];
  for (const f of readdirSync(previo).filter((x) => x.endsWith(".json"))) {
    const id = f.replace(/\.json$/, "");
    const markdown = readFileSync(path.join(previo, `${id}.md`), "utf8");
    const entrada = JSON.parse(readFileSync(path.join(previo, f), "utf8"));
    let reserva: number;
    try {
      reserva = presupuesto.reservar(reservaDeLlamada(JSON.stringify(entrada.nodos).length + markdown.length + SYSTEM_COMPROBADOR_PASOS.length, 6000, [2, 10]));
    } catch (e) {
      if (!(e instanceof TopeAlcanzado)) throw e;
      console.log(`TOPE: ${e.message}`);
      break;
    }
    const r = await comprobarPasos(client, { markdown, pasosCitados: entrada.pasosCitados, nodos: entrada.nodos }, usoVacio(), { presupuestoUsd: 5 });
    const costo = costoAcumuladoUsd(r.acumulado);
    presupuesto.cerrar(reserva, costo);
    const pasos = pasosDelPlan(markdown);
    console.log(`${id}: ${r.juzgados} juzgados, quitados ${r.quitados.join(", ") || "ninguno"}, ignorados ${r.ignorados}${r.revision ? ", REVISION" : ""}${r.fallo ? `, FALLO ${r.fallo}` : ""} | $${costo.toFixed(4)}`);
    for (const p of r.propuestas) console.log(`   ${p.clave} [${p.nodo}] paso: «${pasos.get(p.clave)?.texto ?? "?"}» | tema: «${p.el_tema_dice}» | ${p.motivo ?? ""}`);
    informe.push({ plan_id: id, juzgados: r.juzgados, quitados: r.quitados, ignorados: r.ignorados, revision: r.revision, fallo: r.fallo, propuestas: r.propuestas, costo });
  }
  writeFileSync(path.join(dir, "repeticion_comprobador.json"), JSON.stringify({ gastado_usd: presupuesto.gastado, planes: informe }, null, 2), "utf8");
  console.log(`LISTO: gastado $${presupuesto.gastado.toFixed(4)}`);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
