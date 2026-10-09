/**
 * COSTES_MODELOS.md de la corrida final (decision del fundador, 8 oct 2026): de esta medicion depende el modelo a usar
 * (Sonnet 5.5 / 4.6, Haiku 5.5 / 4.5). No llama a la IA ni a la base: lee los volcados de coste de
 * docs/corrida_final/<fecha>/ (solo numeros, sin textos) y escribe el informe.
 *
 * El coste por modelo se calcula con costoLlamadaUsd de lib/costmeter.ts: los mismos precios y multiplicadores de
 * cache que cobra la app.
 *
 * Uso (desde web/):
 *   npx tsx scripts/corrida_final_costes_modelos.ts ../docs/corrida_final/2026-10-08
 */
import { readFileSync, writeFileSync, existsSync } from "node:fs";
import path from "node:path";
import { costoLlamadaUsd, PRECIOS } from "../lib/costmeter";

type UsoModelo = { in: number; out: number; llamadas: number; cache_read: number; cache_write: number; cache_write_1h?: number };
type Llamada = {
  componente?: string | null;
  modelo?: string;
  model?: string;
  in?: number;
  out?: number;
  cache_read?: number;
  cache_write?: number;
  cache_write_1h?: number;
  usd?: number;
};
type Sesion = {
  id: string;
  tipo: string;
  dominio: string;
  costo_usd: number | null;
  costo_desglose: Record<string, number> | null;
  uso: Record<string, UsoModelo> | null;
  llamadas?: Llamada[] | null;
  presupuesto_excedido: boolean | null;
};
type Volcado = { nota: string; ventana: { desde: string; hasta: string }; sesiones: Sesion[] };

const dir = process.argv[2];
if (!dir) throw new Error("uso: <carpeta de la corrida>");
const leer = (f: string): Volcado | null => (existsSync(path.join(dir, f)) ? (JSON.parse(readFileSync(path.join(dir, f), "utf8")) as Volcado) : null);

const CORRIDAS: Array<{ clave: string; titulo: string; archivo: string }> = [
  { clave: "base", titulo: "Vuelo 27 sep (Sonnet 4.6 + Haiku 4.5)", archivo: "base_vuelo_2026-09-27.json" },
  { clave: "coherencia", titulo: "Coherencia 8 oct (5.5, antes del arreglo del anclaje)", archivo: "costes_coherencia.json" },
  { clave: "vuelo1", titulo: "Vuelo 8 oct, intento 1 (paro en 2i)", archivo: "costes_vuelo.json" },
  { clave: "vuelo2", titulo: "Vuelo 8 oct, intento 2 (paro en 2j)", archivo: "costes_vuelo_intento2.json" },
  { clave: "vuelo3", titulo: "Vuelo 8 oct, intento 3 (paro en 2f, sin creditos)", archivo: "costes_vuelo_intento3.json" },
  { clave: "vuelofinal", titulo: "Vuelo FINAL validado (intento 10 + fases 3 y 4)", archivo: "costes_vuelo_final.json" },
];

const usd = (n: number, d = 4) => `$${n.toFixed(d)}`;
const num = (n: number) => Math.round(n).toLocaleString("es");
const sum = (xs: number[]) => xs.reduce((a, b) => a + b, 0);
function pct(xs: number[], p: number): number {
  if (xs.length === 0) return 0;
  const s = [...xs].sort((a, b) => a - b);
  return s[Math.min(s.length - 1, Math.ceil((p / 100) * s.length) - 1)];
}
const costoSesion = (s: Sesion) => s.costo_usd ?? sum(Object.values(s.costo_desglose ?? {}));
const costoModelo = (m: string, u: UsoModelo) => costoLlamadaUsd(m, u.in, u.out, u.cache_read, u.cache_write, u.cache_write_1h ?? 0);

const out: string[] = [];
const L = (s = "") => out.push(s);

const datos = CORRIDAS.map((c) => ({ ...c, v: leer(c.archivo) })).filter((c) => c.v);

L("# Costes por modelo: la corrida final contra el vuelo del 27 de septiembre");
L();
L("## La cifra oficial: la consola del fundador");
L();
L("El coste oficial de la corrida es el que marca la consola de Anthropic del fundador, no la suma de `costo_usd`:");
L();
L("| | USD | Hora (UTC) |");
L("|---|---:|---|");
L(`| Saldo inicial de referencia | 19,67 | 8 oct 2026, 01:05 |`);
L(`| Saldo final | ${process.env.SALDO_FINAL_USD ?? "pendiente (lo anota el fundador)"} | ${process.env.SALDO_FINAL_HORA ?? ""} |`);
L(`| Coste oficial de la corrida | ${process.env.SALDO_FINAL_USD ? (19.67 - Number(process.env.SALDO_FINAL_USD.replace(",", "."))).toFixed(2).replace(".", ",") : "pendiente"} | |`);
L();
L("La consola incluye todo lo que corrió con la clave en el día (la caché de preguntas, sus jueces, las neutrales, la");
L("coherencia, cada intento del vuelo y la medición del anclaje). `costo_usd` de la app queda solo como DESGLOSE por pieza");
L("y por modelo, que es lo que decide qué modelo usa cada pieza.");
L();
L("## El desglose");
L();
L("De esta medición depende qué modelo usa cada pieza de la app. Todo sale de los volcados de coste de esta carpeta");
L("(solo números, sin textos de usuario). El coste por modelo se recalcula con `costoLlamadaUsd` de `web/lib/costmeter.ts`:");
L("los mismos precios y multiplicadores de caché que usa la app para cobrar.");
L();
L("Precios por millón de tokens (entrada / salida), tal como están en `PRECIOS`:");
L();
L("| Modelo | Entrada | Salida |");
L("|---|---:|---:|");
for (const [m, [pin, pout]] of Object.entries(PRECIOS)) L(`| ${m} | ${usd(pin, 2)} | ${usd(pout, 2)} |`);
L();

L("## 1. Resumen por corrida");
L();
L("| Corrida | Sesiones | Total | Media por sesión | p50 | p95 | Máxima |");
L("|---|---:|---:|---:|---:|---:|---:|");
for (const c of datos) {
  const cs = c.v!.sesiones.map(costoSesion);
  L(`| ${c.titulo} | ${cs.length} | ${usd(sum(cs))} | ${usd(sum(cs) / Math.max(1, cs.length))} | ${usd(pct(cs, 50))} | ${usd(pct(cs, 95))} | ${usd(Math.max(0, ...cs))} |`);
}
L();
L("Las corridas no tienen la misma mezcla de sesiones (cuántos seguimientos, qué mundos, cuántos turnos), así que el");
L("total no se compara a ciegas: la comparación más justa es por pieza (sección 3) y por llamada (sección 4).");
L();

L("## 2. Por modelo");
L();
for (const c of datos) {
  const porModelo = new Map<string, UsoModelo>();
  for (const s of c.v!.sesiones)
    for (const [m, u] of Object.entries(s.uso ?? {})) {
      const a = porModelo.get(m) ?? { in: 0, out: 0, llamadas: 0, cache_read: 0, cache_write: 0, cache_write_1h: 0 };
      porModelo.set(m, {
        in: a.in + u.in, out: a.out + u.out, llamadas: a.llamadas + (u.llamadas ?? 0), cache_read: a.cache_read + u.cache_read,
        cache_write: a.cache_write + u.cache_write, cache_write_1h: (a.cache_write_1h ?? 0) + (u.cache_write_1h ?? 0),
      });
    }
  if (porModelo.size === 0) continue;
  L(`### ${c.titulo}`);
  L();
  L("| Modelo | Llamadas | Entrada | Salida | Caché leída | Caché escrita 5 min | Caché escrita 1 h | Coste | Coste por llamada |");
  L("|---|---:|---:|---:|---:|---:|---:|---:|---:|");
  for (const [m, u] of porModelo) {
    const k = costoModelo(m, u);
    L(`| ${m} | ${num(u.llamadas)} | ${num(u.in)} | ${num(u.out)} | ${num(u.cache_read)} | ${num(u.cache_write)} | ${num(u.cache_write_1h ?? 0)} | ${usd(k)} | ${usd(k / Math.max(1, u.llamadas), 5)} |`);
  }
  L();
}

L("## 3. Por pieza (componente)");
L();
const componentes = new Set<string>();
for (const c of datos) for (const s of c.v!.sesiones) for (const k of Object.keys(s.costo_desglose ?? {})) componentes.add(k);
L(`| Pieza | ${datos.map((c) => c.titulo).join(" | ")} |`);
L(`|---|${datos.map(() => "---:").join("|")}|`);
for (const comp of [...componentes].sort()) {
  const celdas = datos.map((c) => {
    const vals = c.v!.sesiones.map((s) => s.costo_desglose?.[comp]).filter((x): x is number => typeof x === "number");
    return vals.length ? `${usd(sum(vals))} (${vals.length} ses.)` : "";
  });
  L(`| ${comp} | ${celdas.join(" | ")} |`);
}
L();

L("## 4. Por llamada (pieza × modelo)");
L();
L("El registro llamada por llamada existe desde la corrida con los modelos 5.5. Media por llamada:");
L();
for (const c of datos) {
  const filas = new Map<string, { n: number; usd: number; in: number; out: number; cr: number }>();
  for (const s of c.v!.sesiones)
    for (const l of s.llamadas ?? []) {
      const clave = `${l.componente ?? "(sin pieza)"} · ${l.modelo ?? l.model ?? "?"}`;
      const a = filas.get(clave) ?? { n: 0, usd: 0, in: 0, out: 0, cr: 0 };
      filas.set(clave, { n: a.n + 1, usd: a.usd + (l.usd ?? 0), in: a.in + (l.in ?? 0), out: a.out + (l.out ?? 0), cr: a.cr + (l.cache_read ?? 0) });
    }
  if (filas.size === 0) continue;
  L(`### ${c.titulo}`);
  L();
  L("| Pieza · modelo | Llamadas | Coste por llamada | Entrada media | Salida media | Caché leída media |");
  L("|---|---:|---:|---:|---:|---:|");
  for (const [k, f] of [...filas].sort((a, b) => b[1].usd - a[1].usd))
    L(`| ${k} | ${f.n} | ${usd(f.usd / f.n, 5)} | ${num(f.in / f.n)} | ${num(f.out / f.n)} | ${num(f.cr / f.n)} |`);
  L();
}

L("## 5. Por sesión y por espacio");
L();
for (const c of datos) {
  const grupos = new Map<string, number[]>();
  for (const s of c.v!.sesiones) {
    const k = `${s.tipo} · ${s.dominio}`;
    grupos.set(k, [...(grupos.get(k) ?? []), costoSesion(s)]);
  }
  L(`### ${c.titulo}`);
  L();
  L("| Tipo · espacio | Sesiones | Media | Máxima |");
  L("|---|---:|---:|---:|");
  for (const [k, xs] of [...grupos].sort()) L(`| ${k} | ${xs.length} | ${usd(sum(xs) / xs.length)} | ${usd(Math.max(...xs))} |`);
  L();
}

L("## 6. Caché");
L();
L("Lo que costaría la caché leída si se pagara como entrada normal, contra lo que costó de verdad:");
L();
L("| Corrida | Modelo | Caché leída | Pagado por leerla | Habría costado sin caché | Ahorro |");
L("|---|---|---:|---:|---:|---:|");
for (const c of datos) {
  const porModelo = new Map<string, number>();
  for (const s of c.v!.sesiones) for (const [m, u] of Object.entries(s.uso ?? {})) porModelo.set(m, (porModelo.get(m) ?? 0) + u.cache_read);
  for (const [m, cr] of porModelo) {
    if (!cr) continue;
    const pagado = costoLlamadaUsd(m, 0, 0, cr, 0, 0);
    const lleno = costoLlamadaUsd(m, cr, 0, 0, 0, 0);
    L(`| ${c.titulo} | ${m} | ${num(cr)} | ${usd(pagado)} | ${usd(lleno)} | ${usd(lleno - pagado)} |`);
  }
}
L();
const medicion = existsSync(path.join(dir, "medicion_cache_anclaje.txt")) ? readFileSync(path.join(dir, "medicion_cache_anclaje.txt"), "utf8").trim() : null;
if (medicion) {
  L("### El hallazgo del anclaje de protección");
  L();
  L("En la coherencia, el anclaje de los mundos de protección fue la pieza más cara: la foto del proyecto y la ficha de");
  L("cada turno viajaban juntas en el bloque con caché de 1 hora, así que el bloque se reescribía (a 2× la entrada) en");
  L("cada turno. Arreglo (main 0908caa7a): solo la parte fija va en caché; la ficha viaja aparte, sin caché. Medido con la");
  L("misma sesión real antes y después:");
  L();
  L("```");
  L(medicion);
  L("```");
  L();
}

L("## 7. El tope por sesión");
L();
L("Visto del fundador (8 oct 2026): USD 1,00 por defecto en el código; al alcanzarlo la entrevista se cierra ordenada y el");
L("plan que arranca se termina entero (margen de USD 0,50). Sesiones que habrían tocado cada valor:");
L();
L("| Corrida | Sesiones | > 0,35 | > 1,00 | Máxima |");
L("|---|---:|---:|---:|---:|");
for (const c of datos) {
  const cs = c.v!.sesiones.map(costoSesion);
  L(`| ${c.titulo} | ${cs.length} | ${cs.filter((x) => x > 0.35).length} | ${cs.filter((x) => x > 1).length} | ${usd(Math.max(0, ...cs))} |`);
}
L();

L("## 8. La consulta de costo_usd");
L();
L("Para repetir las cuentas en el SQL Editor de Supabase (cambia la ventana):");
L();
L("```sql");
L("select tipo, dominio, count(*) as sesiones, round(sum(costo_usd)::numeric, 4) as total_usd,");
L("       round(avg(costo_usd)::numeric, 4) as media_usd, round(max(costo_usd)::numeric, 4) as maxima_usd");
L("from sessions");
L("where user_id = '4a05a687-fc7e-4427-8eaf-cc1cc1644678'");
L("  and created_at >= '2026-10-08T13:02:00Z' and created_at < '2026-10-09T00:00:00Z'");
L("group by tipo, dominio");
L("order by tipo, dominio;");
L("```");
L();

writeFileSync(path.join(dir, "COSTES_MODELOS.md"), out.join("\n") + "\n");
console.log(`COSTES_MODELOS.md escrito (${datos.length} corridas)`);
