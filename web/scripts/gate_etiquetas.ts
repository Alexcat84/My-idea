/**
 * gate_etiquetas.ts — la vara de las ETIQUETAS DE CARA sobre el build real.
 *
 * El rescate de la primera idea de la beta mostró títulos de manual en la cara
 * del usuario ("Producto Mínimo Viable (MVP)", "Earlyvangelists", "VoC"). El
 * problema era de CABLEADO: los nodos ya tenían su etiqueta natural y la
 * pantalla leía el campo equivocado. Un test unitario no lo habría cazado,
 * porque el dato viajaba correcto hasta el último salto.
 *
 * Este gate siembra una sesión con los nodos MÁS técnicos del grafo (cero
 * llamadas al modelo: se escribe el estado directo) y mira lo que de verdad
 * llega: el JSON de la API, el texto en pantalla y los tooltips. Deja una
 * captura del riel para el ojo del fundador.
 *
 * Uso: pnpm dev en otra terminal, luego
 *   npx tsx scripts/gate_etiquetas.ts
 */
import { createClient } from "@supabase/supabase-js";
import { createServerClient } from "@supabase/ssr";
import { chromium } from "playwright";
import { autenticarComoDevUser, BASE_URL, cargarEnvRaiz } from "./_shared/http";

cargarEnvRaiz();

const RUTA_TECNICA = [
  "enfoque_mercado_voc",
  "customer_discovery_get_out_of_building",
  "earlyvangelists_identificacion",
  "mvp_catalogo_tecnicas",
  "business_model_canvas_vs_plan",
  "identificar_earlyvangelists",
];
const PROHIBIDAS = ["MVP", "Earlyvangelists", "VoC", "Canvas", "Business Model", "Customer Discovery"];

async function main() {
  const admin = createClient(process.env.NEXT_PUBLIC_SUPABASE_URL!, process.env.SUPABASE_SERVICE_ROLE_KEY!, {
    auth: { persistSession: false },
  });

  const jar = new Map<string, string>();
  const anon = createServerClient(process.env.NEXT_PUBLIC_SUPABASE_URL!, process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!, {
    cookies: {
      getAll: () => [...jar].map(([name, value]) => ({ name, value })),
      setAll: (cs) => cs.forEach((c) => jar.set(c.name, c.value)),
    },
  });
  const { data: sesion, error: eLogin } = await anon.auth.signInWithPassword({
    email: "dev@my-idea.local",
    password: process.env.VUELO_DEV_PASSWORD!,
  });
  if (eLogin || !sesion.user) throw eLogin ?? new Error("sin user");
  const userId = sesion.user.id;

  const { data: proy, error: eP } = await admin
    .from("projects")
    .insert({
      user_id: userId,
      entrada_original: "Quiero validar mi idea con clientes reales antes de construir nada.",
      titulo: "Prueba de etiquetas de cara",
      fase_actual: "validacion",
    })
    .select("id")
    .single();
  if (eP) throw eP;
  const projectId = proy.id as string;

  const estado = {
    recorrido: {
      ruta: RUTA_TECNICA,
      modos: ["conversado", "conversado", "silencioso", "conversado", "salto", "conversado"],
      perfilSesion: "",
      textoOriginal: "Quiero validar mi idea con clientes reales.",
      profundizarOfrecido: false,
      esSeguimiento: false,
      estadoVivoPrevio: null,
      nodosCubiertosPrevios: [],
      dominiosDesbloqueados: ["core"],
      dominioSesion: "core",
      puertasDescartadas: [],
      fallbackEvents: [],
      prioridadDeclarada: null,
      preguntaPendiente: "¿Con cuántas personas has hablado ya?",
      fase: "esperando_respuesta",
      sigamosDirigido: null,
    },
    acumulado: { llamadas: [], uso_por_componente: {}, costo_usd: 0 },
    turnos: [
      { pregunta: "¿Qué te frena hoy?", respuesta: "No sé si alguien pagaría.", en: new Date(0).toISOString() },
    ],
    ultimaPregunta: "¿Con cuántas personas has hablado ya?",
  };

  const { error: eS } = await admin.from("sessions").insert({
    project_id: projectId,
    user_id: userId,
    session_position: 1,
    tipo: "inicial",
    mensaje_entrada: "quiero validar mi idea",
    estado_recorrido: estado,
  });
  if (eS) throw eS;

  // ── El render ─────────────────────────────────────────────────────────────
  const cookie = await autenticarComoDevUser();
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ viewport: { width: 1280, height: 1100 } });
  await ctx.addCookies(
    cookie.split("; ").map((kv) => {
      const i = kv.indexOf("=");
      return { name: kv.slice(0, i), value: kv.slice(i + 1), domain: "localhost", path: "/" };
    })
  );
  const page = await ctx.newPage();
  await page.goto(`${BASE_URL}/idea/${projectId}`, { waitUntil: "networkidle" });
  await page.waitForTimeout(1500);

  // 1) Lo que la API manda (¿viaja el titulo tecnico por el cable?)
  const api = await (await fetch(`${BASE_URL}/api/idea/${projectId}`, { headers: { Cookie: cookie } })).text();
  const enApi = PROHIBIDAS.filter((p) => api.includes(p));
  console.log("API /api/idea:", enApi.length ? `FUGA -> ${enApi.join(", ")}` : "limpia");

  // 2) Lo que se ve en pantalla, incluidos los tooltips (title=)
  const textoVisible = await page.evaluate(() => document.body.innerText);
  const titles = await page.evaluate(() =>
    [...document.querySelectorAll("[title]")].map((e) => e.getAttribute("title") ?? "").join(" | ")
  );
  const enPantalla = PROHIBIDAS.filter((p) => textoVisible.includes(p));
  const enTooltips = PROHIBIDAS.filter((p) => titles.includes(p));
  console.log("Pantalla:", enPantalla.length ? `FUGA -> ${enPantalla.join(", ")}` : "limpia");
  console.log("Tooltips:", enTooltips.length ? `FUGA -> ${enTooltips.join(", ")}` : "limpia");
  console.log("tooltips vistos:", titles.slice(0, 200));

  const rielVisible = await page.evaluate(() =>
    [...document.querySelectorAll("li")].map((e) => (e as HTMLElement).innerText.split("\n")[0]).filter(Boolean).slice(0, 12)
  );
  console.log("riel:", JSON.stringify(rielVisible, null, 1));

  await page.screenshot({ path: "examples/capturas/gate_etiquetas_riel.png", fullPage: false });
  await browser.close();
  await admin.from("projects").delete().eq("id", projectId);
  console.log(
    enApi.length + enPantalla.length + enTooltips.length === 0
      ? "\nVEREDICTO: ninguna palabra tecnica llego al usuario."
      : "\nVEREDICTO: HAY FUGA."
  );
}

main();
