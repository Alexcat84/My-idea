/**
 * Paquetes del juez de fidelidad para la MEDICION BARATA (decision del fundador, corrida final, 8 oct 2026).
 *
 * Toma los paquetes del vuelo (tramo C) de cada plan redactado de nuevo, conserva EXACTOS sus nodos y su contexto (la
 * misma entrevista) y cambia solo la salida por la version A (solo reglas) o B (reglas + verificador). Planta las
 * trampas sin marca con el mismo metodo (plantarTrampas, 1 por cada 5 salidas), con una semilla fija por version
 * escrita antes de leer las salidas: A = 20261012, B = 20261013. No llama a la IA ni a la base.
 *
 * Uso (desde web/): npx tsx scripts/corrida_final_paquetes_ab.ts --paquetes-c <dir> --claves-c <claves.json> --medicion <dir> --salida <dir>
 */
import { mkdirSync, readFileSync, readdirSync, existsSync, writeFileSync } from "node:fs";
import path from "node:path";
import { plantarTrampas, type ClavePaquete, type PaqueteFidelidad, type SalidaReal } from "../lib/coherencia/juezFidelidad";

// Semillas por defecto de la primera medicion; --semilla-a/--semilla-b las cambian (escritas antes de leer las salidas).
const SEMILLAS = { A: 20261012, B: 20261013 };

const arg = (n: string) => {
  const i = process.argv.indexOf(n);
  return i >= 0 ? process.argv[i + 1] ?? null : null;
};

function main() {
  const dirC = arg("--paquetes-c");
  const clavesC = arg("--claves-c");
  const medicion = arg("--medicion");
  const salida = arg("--salida");
  if (!dirC || !clavesC || !medicion || !salida) throw new Error("faltan argumentos");
  if (arg("--semilla-a")) SEMILLAS.A = Number(arg("--semilla-a"));
  if (arg("--semilla-b")) SEMILLAS.B = Number(arg("--semilla-b"));
  const claves = (JSON.parse(readFileSync(clavesC, "utf8")) as { claves: ClavePaquete[] }).claves.filter((c) => c.origen === "real");
  const paquetesC = new Map<string, PaqueteFidelidad>(
    readdirSync(dirC).filter((f) => f.endsWith(".json")).map((f) => {
      const p = JSON.parse(readFileSync(path.join(dirC, f), "utf8")) as PaqueteFidelidad;
      return [p.paquete, p];
    })
  );
  for (const version of ["A", "B"] as const) {
    const salidas: SalidaReal[] = [];
    for (const c of claves) {
      const archivo = path.join(medicion, version, `${c.ref.plan_id}.md`);
      if (!existsSync(archivo)) continue;
      const original = paquetesC.get(c.paquete);
      if (!original) throw new Error(`no esta el paquete ${c.paquete} del tramo C`);
      const { paquete: _id, ...contenido } = original;
      salidas.push({ ref: c.ref, contenido: { ...contenido, salida: readFileSync(archivo, "utf8") } });
    }
    const { paquetes, claves: clavesV } = plantarTrampas(salidas, SEMILLAS[version]);
    const dirP = path.join(salida, `paquetes_${version}`);
    const dirK = path.join(salida, `claves_${version}`);
    mkdirSync(dirP, { recursive: true });
    mkdirSync(dirK, { recursive: true });
    for (const p of paquetes) writeFileSync(path.join(dirP, `${p.paquete}.json`), JSON.stringify(p, null, 2), "utf8");
    writeFileSync(path.join(dirK, "claves.json"), JSON.stringify({ version, semilla: SEMILLAS[version], salidas: salidas.length, claves: clavesV }, null, 2), "utf8");
    console.log(`version ${version}: ${salidas.length} salidas + ${paquetes.length - salidas.length} trampas = ${paquetes.length} paquetes`);
  }
}

main();
