// Phase 3.7 — GATE DE CIERRE (C7): una sesión REAL completa vía la UI
// (no APIs directas): Chispa → Claridad → Exploración → espera del plan
// → Tu Plan → Manos a la Obra, capturando la app viva en cada pantalla y,
// al lado, el frame desktop del HTML canon correspondiente
// (docs/diseno-canon, autocontenidos: abren por file://).
// Salida: web/examples/gate-canon/NN_<pantalla>_{app|canon}.png.
// Diferencias visibles = fase abierta (el veredicto es del auditor/fundador).
//
// Uso: pnpm dev corriendo en :3000, luego npx tsx scripts/gate_canon.ts
// Costo real: 1 organizer + 1 entrevista + 1 plan (≈ lo de una sesión).
import { chromium, type Page } from "playwright";
import { mkdirSync } from "node:fs";
import path from "node:path";
import { pathToFileURL } from "node:url";
import { autenticarComoDevUser, BASE_URL, cargarEnvRaiz, ROOT } from "./_shared/http";

cargarEnvRaiz();

const OUT = path.join(ROOT, "web", "examples", "gate-canon");
const CANON = path.join(ROOT, "docs", "diseno-canon");

const IDEA =
  "Quiero vender kits de huerto urbano para balcones pequeños, con todo listo para sembrar y una guía simple; ya armé tres para amigos y me los pagaron.";

const RESPUESTAS = [
  "Ya vendí tres kits a amigos y los tres me pidieron otro para regalar; los armo yo misma en casa con macetas, sustrato y semillas que compro al por mayor.",
  "Cada kit me cuesta unos 180 en materiales y lo vendo a 350; tardo una tarde en armar cinco.",
  "Lo que más me preocupa es si alguien fuera de mis conocidos pagaría ese precio, todavía no he vendido a desconocidos.",
  "Puedo dedicarle unas 10 horas a la semana sin descuidar mi trabajo.",
  // Phase 3.7.2: cierres explícitos para que el intérprete proponga el
  // plan y aparezca LA OFERTA HONESTA (el estado nuevo que el gate debe ver)
  "Con eso me basta por ahora, creo que ya te conté lo importante.",
  "Ya no tengo más que agregar, quiero ver mi plan.",
  "De acuerdo, suficiente, armemos el plan.",
];

async function capturar(page: Page, archivo: string) {
  // animaciones del canon: planIn/railIn + el stepFill escalonado del
  // stepper (la última barra termina ~1.65s; 3s deja todo asentado)
  await page.waitForTimeout(3000);
  await page.screenshot({ path: path.join(OUT, archivo), fullPage: true });
  console.log(`  ${archivo}`);
}

async function capturarCanon(page: Page, htmlCanon: string, archivo: string) {
  await page.goto(pathToFileURL(path.join(CANON, htmlCanon)).href);
  await page.waitForTimeout(900);
  const frame = page.locator("[data-screen-label$='desktop']").first();
  await frame.screenshot({ path: path.join(OUT, archivo) });
  console.log(`  ${archivo} <- canon "${htmlCanon}"`);
}

async function main() {
  mkdirSync(OUT, { recursive: true });
  const cookie = await autenticarComoDevUser();
  const browser = await chromium.launch();
  const context = await browser.newContext({ viewport: { width: 1240, height: 900 }, deviceScaleFactor: 1 });
  const url = new URL(BASE_URL);
  await context.addCookies(
    cookie.split("; ").map((par) => {
      const i = par.indexOf("=");
      return { name: par.slice(0, i), value: par.slice(i + 1), domain: url.hostname, path: "/" };
    })
  );
  const app = await context.newPage();
  const canon = await context.newPage();

  // 01 La Chispa
  await app.goto(`${BASE_URL}/nueva`);
  await capturar(app, "01_chispa_app.png");
  await capturarCanon(canon, "02 - Etapa 1 - La Chispa.html", "01_chispa_canon.png");

  // 02 Claridad (organizer real por la UI)
  await app.fill("#idea", IDEA);
  await app.getByRole("button", { name: /organizar|continuar|empezar|listo/i }).first().click();
  await app.getByText("Esto entendí de tu idea", { exact: false }).waitFor({ timeout: 120000 });
  await capturar(app, "02_claridad_app.png");
  await capturarCanon(canon, "03 - Etapa 2 - Claridad.html", "02_claridad_canon.png");

  // 03 La Exploración (entrevista real por la UI)
  await app.getByRole("button", { name: "Explorar estas suposiciones" }).click();
  const hayOferta = async () =>
    (await app.getByText("Tu recorrido hasta aquí", { exact: false }).count()) +
      (await app.getByText("Suficiente para avanzar", { exact: false }).count()) >
    0;
  for (let i = 0; i < RESPUESTAS.length; i++) {
    // la oferta pudo llegar con la respuesta anterior: no hay textarea que llenar
    if (await hayOferta()) break;
    // textarea HABILITADO (mientras envía queda disabled en el DOM)
    const campo = app.locator("textarea:not([disabled])").first();
    await campo.waitFor({ timeout: 180000 });
    if (i === 2) await capturar(app, "03_exploracion_app.png"); // a mitad del riel
    await campo.fill(RESPUESTAS[i]);
    await app.getByRole("button", { name: "Enviar" }).click();
    // Phase 3.7.2: la siguiente pregunta (campo habilitado de nuevo) o LA
    // OFERTA HONESTA, lo que llegue primero.
    await Promise.race([
      app.locator("textarea:not([disabled])").first().waitFor({ timeout: 180000 }),
      app.getByText("Tu recorrido hasta aquí", { exact: false }).waitFor({ timeout: 180000 }),
      app.getByText("Suficiente para avanzar", { exact: false }).waitFor({ timeout: 180000 }),
    ]).catch(() => {});
    if (await hayOferta()) break;
  }
  await capturarCanon(canon, "04 - Etapa 3 - La Exploracion.html", "03_exploracion_canon.png");

  // Phase 3.7.2 — la oferta honesta: captura del estado nuevo si apareció
  if ((await app.getByText("Tu recorrido hasta aquí", { exact: false }).count()) > 0) {
    await capturar(app, "03b_oferta_honesta_app.png");
  }

  // 04 espera del plan + Tu Plan, pasando por la tarjeta intermedia
  // ("¿Algo más que quieras que tu plan tome en cuenta?") con contexto
  // real: ejercita el canal contexto_final -> redactor -> bitácora.
  const btnPlan = app.getByRole("button", { name: /Generar mi plan/i }).first();
  if ((await btnPlan.count()) > 0) await btnPlan.click();
  else await app.getByText("Generar mi plan con lo que ya conté").click();
  await app.getByText("¿Algo más que quieras", { exact: false }).waitFor({ timeout: 30000 });
  await app
    .locator("#contexto-final")
    .fill("Me importa que el plan asuma que solo puedo invertir 200 al mes al inicio.");
  await app.getByRole("button", { name: "Armar mi plan" }).click();
  await app.getByText("Tu Plan · en camino", { exact: false }).first().waitFor({ timeout: 30000 });
  await app.waitForTimeout(4000); // etapas encendiéndose por SSE
  await capturar(app, "04a_plan_en_camino_app.png");
  try {
    await app.getByRole("button", { name: "Pasar a Manos a la Obra" }).waitFor({ timeout: 240000 });
  } catch (e) {
    // diagnóstico del camino en-vivo: qué quedó en pantalla cuando el CTA
    // no apareció tras el done del SSE
    await app.screenshot({ path: path.join(OUT, "_debug_sin_cta.png"), fullPage: true });
    const cuerpo = ((await app.textContent("body")) ?? "").replace(/\s+/g, " ");
    console.log("SIN CTA. Pistas del DOM:");
    for (const clave of ["Pasar a Manos", "Generar mi plan", "Suficiente para avanzar", "Tu Plan · en camino", "Tu Plan · listo", "en curso", "algo se atoró", "conexión se cortó"]) {
      console.log(`  "${clave}" presente:`, cuerpo.includes(clave));
    }
    throw e;
  }
  await capturar(app, "04_tu_plan_app.png");
  await capturarCanon(canon, "05 - Etapa 4 - Tu Plan.html", "04_tu_plan_canon.png");

  // 05 Manos a la Obra POR LA PUERTA (el CTA, sin teclear URLs) + los 6 mundos
  await app.getByRole("button", { name: "Pasar a Manos a la Obra" }).click();
  await app.waitForURL(/vista=manos/, { timeout: 30000 });
  await capturar(app, "05_manos_app.png");
  await capturarCanon(canon, "06 - Etapa 5 - Manos a la Obra.html", "05_manos_canon.png");

  // verificación C0: los 6 mundos visibles en el flujo real
  const cuerpo = (await app.textContent("body")) ?? "";
  const mundos = ["Calidad y Confianza", "Seguridad y Personas", "Ambiente y Futuro", "Seguridad Digital", "Vender al Mundo", "Multiplica tu Negocio"];
  const visibles = mundos.filter((m) => cuerpo.includes(m));
  console.log(`\nmundos visibles en el flujo real: ${visibles.length}/6 (${visibles.join(", ")})`);
  if (visibles.length !== 6) {
    // la fila también vive bajo el plan en la vista default: verificar ahí
    await app.getByRole("button", { name: "← Ver el plan" }).click().catch(() => {});
    await app.waitForTimeout(1200);
    const cuerpo2 = (await app.textContent("body")) ?? "";
    const visibles2 = mundos.filter((m) => cuerpo2.includes(m));
    console.log(`mundos visibles bajo el plan (vista default): ${visibles2.length}/6`);
    if (visibles2.length !== 6) throw new Error("GATE ROJO: los 6 mundos no aparecen en el flujo real sin URLs");
  }

  // ── Fase 3.8: el sentido del tiempo (canon 09/10/11) desde la sesión real.
  // Requiere la migración 018 aplicada. Envuelto para no perder las capturas
  // anteriores si un selector necesita ajuste.
  try {
    // asegurar la vista Manos (por si el bloque de mundos volvió al plan)
    if (!/vista=manos/.test(app.url())) {
      await app.getByRole("button", { name: "Pasar a Manos a la Obra" }).click().catch(() => {});
      await app.waitForURL(/vista=manos/, { timeout: 30000 }).catch(() => {});
    }

    // 06 Modo del camino (vista A): la tarjeta de elección en la primera entrada
    await app.getByText("¿Cómo quieres llevar tu camino?", { exact: false }).waitFor({ timeout: 30000 });
    await capturar(app, "06_modo_app.png");
    await capturarCanon(canon, "10 - Modo y Fechas.html", "06_modo_canon.png");

    // elegir "Con fechas y recordatorios" → el ritual de la línea base (vista B)
    await app.getByRole("button", { name: /Con fechas y recordatorios/ }).click();
    await app.getByText("Ponle fechas a tu camino", { exact: false }).waitFor({ timeout: 30000 });
    await capturar(app, "07_baseline_app.png");
    await app.getByRole("button", { name: "Aceptar estas fechas" }).click();
    await app.waitForTimeout(1500);

    // marcar dos acciones como hechas (Hoy) para poblar el timeline real
    for (let i = 0; i < 2; i++) {
      const btn = app.getByRole("button", { name: "Marcar hecho" }).first();
      if ((await btn.count()) === 0) break;
      await btn.click();
      await app.getByRole("button", { name: "Hoy" }).first().click().catch(() => {});
      await app.waitForTimeout(800);
    }

    // 07 Análisis del proyecto (canon 11)
    await app.getByRole("button", { name: /Ver análisis del proyecto/ }).click();
    await app.getByText("Análisis de", { exact: false }).first().waitFor({ timeout: 30000 });
    await app.waitForTimeout(1500);
    await capturar(app, "08_analisis_app.png");
    await capturarCanon(canon, "11 - Analisis del Proyecto.html", "08_analisis_canon.png");
    await app.getByRole("button", { name: "← Volver" }).click().catch(() => {});
    await app.waitForTimeout(1000);

    // 08 La Celebración (canon 09) — variante con cumplimiento (modo fechas)
    await app.getByRole("button", { name: "Marcar como realizada" }).click();
    await app.getByRole("button", { name: /Sí, es un proyecto/ }).click();
    await app.getByText("Aquí acaba tu idea y nace tu proyecto", { exact: false }).waitFor({ timeout: 30000 });
    await app.waitForTimeout(8000); // la animación 6-8s asienta
    await capturar(app, "09_celebracion_cumplimiento_app.png");
    await capturarCanon(canon, "09 - La Celebracion.html", "09_celebracion_canon.png");

    // variante a-mi-ritmo: reabrir → pausar fechas → realizar de nuevo
    await app.getByRole("button", { name: /Reabrir esta idea/ }).click();
    await app.waitForTimeout(2000);
    await app.getByRole("button", { name: "Pausar" }).click().catch(() => {});
    await app.waitForTimeout(800);
    await app.getByRole("button", { name: "Marcar como realizada" }).click();
    await app.getByRole("button", { name: /Sí, es un proyecto/ }).click();
    await app.getByText("Aquí acaba tu idea y nace tu proyecto", { exact: false }).waitFor({ timeout: 30000 });
    await app.waitForTimeout(8000);
    await capturar(app, "09b_celebracion_ritmo_app.png");
  } catch (e) {
    console.log(`\n[Fase 3.8] captura incompleta (¿migración 018 aplicada?): ${e instanceof Error ? e.message : e}`);
  }

  await browser.close();
  console.log(`\nGATE: capturas lado a lado en ${OUT} — el veredicto visual es del fundador/auditor.`);
}

main();
