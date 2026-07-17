// Phase 3.7 — GATE DE CIERRE (C7): una sesión REAL completa vía la UI
// (no APIs directas): Chispa → Claridad → Exploración → espera del plan
// → Tu Plan → Manos a la Obra, capturando la app viva en cada pantalla y,
// al lado, el frame desktop del HTML canon correspondiente
// (docs/diseno-canon, autocontenidos: abren por file://).
// Salida: web/examples/gate-canon/NN_<pantalla>_{app|canon}.png.
// Diferencias visibles = fase abierta (el veredicto es del auditor/fundador).
//
// DOS VIEWPORTS, SIEMPRE (desde jul 2026): cada pantalla se captura a 1240 y
// a 380, contra el frame del canon que le corresponde. El canon trae su frame
// "mobile 380" en 10 de sus 11 pantallas y durante siete fases el gate solo
// miro el de escritorio: una vara que el instrumento no mira es decoracion
// (BANCO §9). La APK renderiza esta web EN UN TELEFONO: 380 no es un extra.
// Regla: toda pantalla futura se verifica en los DOS o su fase no cierra.
//
// Uso: pnpm dev corriendo en :3000, luego npx tsx scripts/gate_canon.ts
// Costo real: 1 organizer + 1 entrevista + 1 plan core + 1 ciclo de mundo
// (Fase 4.2: el canon 08 exige un mundo con checklist real). Las capturas de
// 380 anaden CERO tokens: es el mismo flujo, redimensionado.
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

/** Los dos viewports del gate. 380 es el ancho de canon del movil; 1240 el de
 * escritorio. */
const VP_ESCRITORIO = { width: 1240, height: 900 };
const VP_MOVIL = { width: 380, height: 844 };

async function capturar(page: Page, archivo: string, fullPage = true) {
  // animaciones del canon: planIn/railIn + el stepFill escalonado del
  // stepper (la última barra termina ~1.65s; 3s deja todo asentado)
  await page.waitForTimeout(3000);
  await page.screenshot({ path: path.join(OUT, archivo), fullPage });
  console.log(`  ${archivo}`);
}

/**
 * Captura la pantalla viva en LOS DOS viewports.
 *
 * Redimensiona la MISMA pagina a proposito, en vez de abrir un segundo contexto:
 * el estado de estas pantallas no vive en la URL (la entrevista a mitad de
 * camino es estado de React), asi que una segunda pestaña no podria reproducirlo
 * sin RE-CORRER el flujo -- y eso costaria tokens de verdad. Redimensionando, el
 * 380 sale gratis y, mejor aun, es EXACTAMENTE el mismo estado: si el par
 * escritorio/movil difiere, la diferencia es del layout y de nada mas.
 */
async function capturarApp(app: Page, base: string, fullPage = true) {
  await capturar(app, `${base}_app.png`, fullPage);
  await app.setViewportSize(VP_MOVIL);
  await capturar(app, `${base}_app_380.png`, fullPage);
  await app.setViewportSize(VP_ESCRITORIO);
  await app.waitForTimeout(500); // el reflow de vuelta asienta antes de seguir
}

/** yyyy-mm-dd local para llenar un <input type="date">. */
function fmtFechaLocal(d: Date): string {
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`;
}

/** Marca un ítem PENDIENTE como hecho HOY. Reglas del instrumento (cero
 * swallow, cero .first() ciego):
 *  - selecciona un ítem pendiente EXPLÍCITO (el último "Marcar hecho" del DOM),
 *    jamás un .first() que una recarga stale pueda reapuntar a un ítem ya hecho;
 *  - espera el botón "Hoy" y el PATCH real (waitForResponse);
 *  - CONFIRMA el completion por la aparición de un nuevo "hecho el ..." — no
 *    basta con que el prompt se abra (eso ya quita el botón) ni con que el
 *    PATCH responda: exige que el ítem quede hecho de verdad, o LANZA. */
async function marcarHechoHoy(app: Page) {
  const marcar = app.getByRole("button", { name: "Marcar hecho" });
  const hechos = app.getByText(/^hecho el /);
  await marcar.first().waitFor({ state: "visible", timeout: 15000 });
  const pendientes = await marcar.count();
  if (pendientes === 0) throw new Error("no quedan ítems pendientes para marcar hecho");
  const hechosAntes = await hechos.count();

  // El último pendiente del DOM: selección explícita, no un .first() ciego.
  await marcar.nth(pendientes - 1).click();
  const hoy = app.getByRole("button", { name: "Hoy", exact: true });
  await hoy.waitFor({ state: "visible", timeout: 8000 });
  const [resp] = await Promise.all([
    app.waitForResponse(
      (r) => r.url().includes("/checklist") && r.request().method() === "PATCH",
      { timeout: 15000 }
    ),
    hoy.click(),
  ]);
  if (!resp.ok()) throw new Error(`PATCH checklist falló al marcar hecho: HTTP ${resp.status()}`);

  // Settlement: exige un "hecho el ..." MÁS renderizado (completion real).
  const t0 = Date.now();
  while (Date.now() - t0 < 10000) {
    if ((await hechos.count()) > hechosAntes) return;
    await app.waitForTimeout(150);
  }
  throw new Error("no apareció un nuevo 'hecho el' tras el PATCH: el ítem no quedó hecho");
}

/** Garantiza la vista Manos a la Obra, POR LA PUERTA (el CTA, sin teclear
 * URLs). El gate navega mucho y varias ramas dejan la app en la vista del plan
 * (p.ej. el respaldo de la verificacion C0 de los 6 mundos, que hace clic en
 * "← Ver el plan"): quien necesite Manos, la pide con esto. */
async function asegurarManos(app: Page) {
  if (/vista=manos/.test(app.url())) return;
  const irManos = app.getByRole("button", { name: "Pasar a Manos a la Obra" }).first();
  await irManos.waitFor({ state: "visible", timeout: 15000 });
  await irManos.click();
  await app.waitForURL(/vista=manos/, { timeout: 30000 });
}

// label opcional: substring del data-screen-label a capturar. Sin él, el
// primer frame que termina en "desktop" (varios canon tienen varias vistas;
// p.ej. 10 tiene "Eleccion ... Desktop" y "Ritual ... desktop": hay que
// pedir el correcto o el par app-canon se cruza).
//
// `exacto` para cuando una etiqueta es PREFIJO de otra: el canon 04 tiene
// "1a mobile 380" y "1a mobile 380 recorrido abierto", y un substring se
// llevaria la que caiga primero en el DOM -- cruzando el par sin avisar.
async function capturarCanon(
  page: Page,
  htmlCanon: string,
  archivo: string,
  label?: string,
  exacto = false
) {
  await page.goto(pathToFileURL(path.join(CANON, htmlCanon)).href);
  await page.waitForTimeout(900);
  const sel = label
    ? exacto
      ? `[data-screen-label="${label}"]`
      : `[data-screen-label*="${label}"]`
    : "[data-screen-label$='desktop']";
  const frame = page.locator(sel).first();
  await frame.screenshot({ path: path.join(OUT, archivo) });
  console.log(`  ${archivo} <- canon "${htmlCanon}"${label ? ` [${label}]` : ""}`);
}

async function main() {
  mkdirSync(OUT, { recursive: true });
  const cookie = await autenticarComoDevUser();
  const browser = await chromium.launch();
  const context = await browser.newContext({ viewport: VP_ESCRITORIO, deviceScaleFactor: 1 });
  const url = new URL(BASE_URL);
  await context.addCookies(
    cookie.split("; ").map((par) => {
      const i = par.indexOf("=");
      return { name: par.slice(0, i), value: par.slice(i + 1), domain: url.hostname, path: "/" };
    })
  );
  const app = await context.newPage();
  const canon = await context.newPage();

  // 00 Home (canon 01). Hueco heredado: el gate nunca la habia capturado, en
  // NINGUN viewport, aunque el canon la trae en los dos.
  //
  // UNICA pantalla que se captura SIN fullPage, y por una razon de honestidad:
  // la cuenta del gate acumula CIENTOS de ideas de todos los vuelos, y su
  // fullPage salia 23.000px -- 31 veces el frame del canon. Eso medía
  // contaminacion del banco de pruebas, no diseno. El canon 01 es un frame de
  // UNA pantalla; la contaminacion vive toda bajo el pliegue. Pantalla contra
  // pantalla es la comparacion honesta, y ahi la cinta de idea SI es la vara.
  await app.goto(`${BASE_URL}/ideas`);
  await capturarApp(app, "00_home", false);
  await capturarCanon(canon, "01_home_mis_ideas.html", "00_home_canon.png", "Home Mis Ideas desktop", true);
  await capturarCanon(canon, "01_home_mis_ideas.html", "00_home_canon_380.png", "Home Mis Ideas movil 380", true);

  // 01 La Chispa
  await app.goto(`${BASE_URL}/nueva`);
  await capturarApp(app, "01_chispa");
  await capturarCanon(canon, "02_la_chispa.html", "01_chispa_canon.png", "La Chispa desktop", true);
  await capturarCanon(canon, "02_la_chispa.html", "01_chispa_canon_380.png", "La Chispa movil 380", true);

  // 02 Claridad (organizer real por la UI)
  await app.fill("#idea", IDEA);
  await app.getByRole("button", { name: /organizar|continuar|empezar|listo/i }).first().click();
  await app.getByText("Esto entendí de tu idea", { exact: false }).waitFor({ timeout: 120000 });
  await capturarApp(app, "02_claridad");
  await capturarCanon(canon, "03_claridad.html", "02_claridad_canon.png", "Claridad desktop", true);
  await capturarCanon(canon, "03_claridad.html", "02_claridad_canon_380.png", "Claridad movil 380", true);

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
    if (i === 2) await capturarApp(app, "03_exploracion"); // a mitad del riel
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
  await capturarCanon(canon, "04_la_exploracion.html", "03_exploracion_canon.png", "Exploracion desktop", true);
  // exacto: "Exploracion movil 380" convive con "Exploracion recorrido abierto
  // movil 380" en el mismo archivo; el match exacto evita cruzarlos.
  await capturarCanon(canon, "04_la_exploracion.html", "03_exploracion_canon_380.png", "Exploracion movil 380", true);

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
  await capturarApp(app, "04_tu_plan");
  await capturarCanon(canon, "05_tu_plan.html", "04_tu_plan_canon.png", "Tu Plan desktop", true);
  await capturarCanon(canon, "05_tu_plan.html", "04_tu_plan_canon_380.png", "Tu Plan movil 380", true);

  // 05 Manos a la Obra POR LA PUERTA (el CTA, sin teclear URLs) + los 6 mundos
  await app.getByRole("button", { name: "Pasar a Manos a la Obra" }).click();
  await app.waitForURL(/vista=manos/, { timeout: 30000 });

  // 06 Modo del camino (vista A): en la PRIMERA entrada a Manos el selector de
  // modo está a la vista, así que se captura aquí (antes vivía suelto más abajo).
  await app.getByText("¿Cómo quieres llevar tu camino?", { exact: false }).waitFor({ timeout: 30000 });
  await capturarApp(app, "06_modo");
  await capturarCanon(canon, "10_modo_y_fechas.html", "06_modo_canon.png", "Modo eleccion desktop", true);
  await capturarCanon(canon, "10_modo_y_fechas.html", "06_modo_canon_380.png", "Modo eleccion movil 380", true);

  // Fase 4.3.2: el canon de Manos muestra el estado ACTIVO (modo elegido,
  // compacto), no el selector de primera entrada. Se elige "a mi ritmo" para
  // capturar ESE estado -- y de paso deja el modo listo para el resto del flujo.
  await app.getByRole("button", { name: /A mi ritmo/ }).click();
  await app.getByText("Modo:", { exact: false }).first().waitFor({ timeout: 15000 });
  await capturarApp(app, "05_manos");
  await capturarCanon(canon, "06_manos_a_la_obra.html", "05_manos_canon.png", "Manos a la Obra desktop", true);
  await capturarCanon(canon, "06_manos_a_la_obra.html", "05_manos_canon_380.png", "Manos a la Obra movil 380", true);

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

  // ── Fase 4.2 (canon 08 "Mundos Activos"): la seccion de un mundo activo, con
  // lo que la fase le anadio -- su ritual "Contar que paso" y su cierre. Se
  // captura ANTES del bloque 3.8: aqui la idea aun esta abierta y la seccion del
  // mundo se ve en su estado natural, bajo el checklist core.
  //
  // El unlock va por API a proposito, y es la UNICA excepcion a la regla "por la
  // puerta, sin APIs": la activacion de un mundo NO tiene puerta en la UI
  // todavia (es pre-pagos; la tarjeta bloqueada solo registra interes). El resto
  // del camino -- explorar, plan, checklist -- va por la UI como todo lo demas.
  const idProyecto = app.url().match(/\/idea\/([0-9a-f-]{36})/)?.[1];
  if (!idProyecto) throw new Error(`GATE ROJO: no se pudo leer el id del proyecto de la URL: ${app.url()}`);
  const MUNDO_GATE = "quality"; // "Calidad y Confianza": el mundo del canon 08
  const resUnlock = await context.request.post(
    `${BASE_URL}/api/project/${idProyecto}/world/${MUNDO_GATE}/unlock`
  );
  if (!resUnlock.ok()) throw new Error(`GATE ROJO: el unlock del mundo respondio ${resUnlock.status()}`);
  await app.reload();
  // La verificacion C0 de arriba pudo dejarnos en la vista del plan (su rama de
  // respaldo hace clic en "← Ver el plan"): la seccion del mundo vive en Manos.
  await asegurarManos(app);

  const explorarMundo = app.getByRole("button", { name: "Explorar este mundo" }).first();
  await explorarMundo.waitFor({ state: "visible", timeout: 30000 });
  await explorarMundo.click();

  // La entrevista del mundo, por la UI: se responde hasta que ofrezca el plan.
  const RESPUESTAS_MUNDO = [
    "Los tres kits que vendi salieron bien, pero el sustrato me quedo disparejo entre uno y otro y me dio verguenza.",
    "No tengo ninguna forma de revisar que cada kit salga igual; lo hago a ojo.",
    "Quiero que quien lo compre sienta que compro algo serio, no un experimento.",
    "Con eso me basta por ahora, armemos el plan.",
  ];
  const hayOfertaMundo = async () =>
    (await app.getByText("Tu recorrido hasta aquí", { exact: false }).count()) +
      (await app.getByText("Suficiente para avanzar", { exact: false }).count()) >
    0;
  for (const respuesta of RESPUESTAS_MUNDO) {
    if (await hayOfertaMundo()) break;
    const campo = app.locator("textarea:not([disabled])").first();
    try {
      await campo.waitFor({ timeout: 120000 });
    } catch {
      // Sin campo Y sin oferta: el interprete SALIO del mundo (decision
      // 'salir'). apiSesion cierra la sesion y IdeaView solo hace
      // setPregunta(null): la pantalla se queda MUDA. Un timeout de 180s
      // esperando un textarea fantasma no dice nada de eso; esto si.
      await app.screenshot({ path: path.join(OUT, "_debug_mundo_mudo.png"), fullPage: true });
      const cuerpo = ((await app.textContent("body")) ?? "").replace(/\s+/g, " ");
      throw new Error(
        "GATE ROJO: la entrevista del mundo se quedo sin campo y sin oferta. El interprete " +
          "SALIO (busca decision 'salir' en sessions.decisiones de la sesion dominio=quality): " +
          "la sesion queda cerrada y el usuario -- que pago por explorar ESE mundo -- se queda " +
          "mirando una pantalla sin pregunta, sin plan y sin explicacion. Cuerpo: " +
          cuerpo.slice(0, 240)
      );
    }
    await campo.fill(respuesta);
    await app.getByRole("button", { name: "Enviar" }).click();
    await Promise.race([
      app.locator("textarea:not([disabled])").first().waitFor({ timeout: 180000 }),
      app.getByText("Tu recorrido hasta aquí", { exact: false }).waitFor({ timeout: 180000 }),
      app.getByText("Suficiente para avanzar", { exact: false }).waitFor({ timeout: 180000 }),
    ]).catch(() => {});
  }
  const btnPlanMundo = app.getByRole("button", { name: /Generar mi plan/i }).first();
  if ((await btnPlanMundo.count()) > 0) await btnPlanMundo.click();
  else await app.getByText("Generar mi plan con lo que ya conté").click();
  const contextoMundo = app.locator("#contexto-final");
  if ((await contextoMundo.count()) > 0) {
    await contextoMundo.fill("Trabajo sola y no quiero procesos que me quiten toda la tarde.");
    await app.getByRole("button", { name: "Armar mi plan" }).click();
  }
  const aObra = app.getByRole("button", { name: "Pasar a Manos a la Obra" }).first();
  await aObra.waitFor({ timeout: 240000 });
  await aObra.click();
  await app.waitForURL(/vista=manos/, { timeout: 30000 });

  // La seccion del mundo, ya con su checklist: es lo que el canon 08 muestra.
  await app.getByText("Calidad y Confianza", { exact: false }).first().waitFor({ timeout: 30000 });
  // TODO lo del mundo se pide DENTRO de su seccion. "Contar qué pasó" existe dos
  // veces en esta pantalla -- la del mundo y la del core, en el aside -- y el
  // aside va DESPUES en el DOM: un .last() ciego abre el ritual del CORE y el
  // gate captura la pantalla equivocada creyendo que capturo la buena.
  const seccionMundo = app.locator("section").filter({ hasText: "Calidad y Confianza" }).first();
  const cerrarMundo = seccionMundo.getByRole("button", { name: "Marcar este mundo como completado" });
  await cerrarMundo.waitFor({ state: "visible", timeout: 15000 });
  await capturarApp(app, "10_mundo_activo");
  await capturarCanon(canon, "08_mundos_activos.html", "10_mundo_activo_canon.png", "Mundo activo desktop", true);
  await capturarCanon(canon, "08_mundos_activos.html", "10_mundo_activo_canon_380.png", "Mundo activo movil 380", true);

  // El ritual del mundo y su cierre: los dos estados nuevos de la 4.2. No hay
  // par de canon para ellos (el 08 es anterior a esta fase): se capturan solos,
  // para que el fundador los vea en el mismo barrido.
  await seccionMundo.getByRole("button", { name: "Contar qué pasó" }).click();
  // La prueba de que se abrio el del MUNDO y no el del core: su encabezado lo
  // nombra. Si esto falla, la captura habria sido una mentira.
  await seccionMundo.getByText("Continuar Calidad y Confianza", { exact: false }).waitFor({ timeout: 15000 });
  await capturarApp(app, "10b_mundo_ritual");
  await seccionMundo.getByRole("button", { name: "Cerrar" }).click();

  await cerrarMundo.click();
  await seccionMundo
    .getByText("¿Diste Calidad y Confianza por terminado?", { exact: false })
    .waitFor({ timeout: 15000 });
  await capturarApp(app, "10c_mundo_cierre");
  await capturarCanon(canon, "08_mundos_activos.html", "10c_mundo_cierre_canon.png", "Mundo cierre desktop", true);
  await capturarCanon(canon, "08_mundos_activos.html", "10c_mundo_cierre_canon_380.png", "Mundo cierre movil 380", true);
  await seccionMundo.getByRole("button", { name: "Todavía no" }).click();

  // ── Fase 3.8: el sentido del tiempo (canon 09/10/11) desde la sesión real.
  // Requiere la migración 018 aplicada. CERO swallow: cada paso espera lo suyo
  // y LANZA si falla -- el gate es un instrumento permanente, no un adorno.

  // asegurar la vista Manos (el bloque de mundos pudo volver al plan default)
  await asegurarManos(app);

  // ── variante A-MI-RITMO: el modo ya es "a mi ritmo" (elegido y capturado como
  // pantalla 06 arriba). Se marca el avance SIN baseline (sin cumplimiento).
  for (let i = 0; i < 4; i++) await marcarHechoHoy(app); // completions reales, sin fechas base
  await app.getByRole("button", { name: "Marcar como realizada" }).click();
  await app.getByRole("button", { name: /Sí, es un proyecto/ }).click();
  await app.getByText("Aquí acaba tu idea y nace tu proyecto", { exact: false }).waitFor({ timeout: 30000 });
  await app.waitForTimeout(8000); // la animación 6-8s asienta
  await capturarApp(app, "09b_celebracion_ritmo");
  // Refresco jul 2026: el canon nuevo SÍ trae la variante a-mi-ritmo en 380
  // (el viejo solo la tenía en escritorio), así que ahora es un par vivo.
  await capturarCanon(canon, "09_la_celebracion.html", "09b_celebracion_ritmo_canon.png", "Celebracion a mi ritmo desktop", true);
  await capturarCanon(canon, "09_la_celebracion.html", "09b_celebracion_ritmo_canon_380.png", "Celebracion a mi ritmo movil 380", true);

  // reabrir para pasar a la variante con fechas
  const reabrir = app.getByRole("button", { name: /Reabrir esta idea/ });
  await reabrir.waitFor({ state: "visible", timeout: 15000 });
  await reabrir.click();

  // ── variante FECHAS: el interruptor "Activar/Pausar" se retiró (Fase 4.3.2).
  // Se cambia de modo reabriendo el selector con "cambiar" y eligiendo "Con
  // fechas y recordatorios". Sin fechas aún, el ritual de baseline se abre solo,
  // con las 3 clases de cumplimiento (tardía en ámbar, a tiempo, adelantadas).
  const cambiar = app.getByRole("button", { name: "cambiar" }).first();
  await cambiar.waitFor({ state: "visible", timeout: 30000 });
  await cambiar.click();
  await app.getByText("¿Cómo quieres llevar tu camino?", { exact: false }).waitFor({ timeout: 15000 });
  await app.getByRole("button", { name: /Con fechas y recordatorios/ }).click();
  await app.getByText("Ponle fechas a tu camino", { exact: false }).waitFor({ timeout: 30000 });

  // editar las dos primeras fechas (ítems ya hechos HOY): una al pasado (→
  // tardía) y otra a hoy (→ a tiempo); el resto quedan en su sugerida futura
  // (→ adelantadas). Las demás fechas base ancla del canon quedan intactas.
  const inputs = app.locator('input[type="date"]');
  await inputs.first().waitFor({ state: "visible", timeout: 10000 });
  await inputs.nth(0).fill(fmtFechaLocal(new Date(Date.now() - 21 * 86400000))); // 3 semanas atrás → tardía
  await inputs.nth(1).fill(fmtFechaLocal(new Date())); // hoy → a tiempo
  await capturarApp(app, "07_baseline");
  await capturarCanon(canon, "10_modo_y_fechas.html", "07_baseline_canon.png", "Modo fechas ritual desktop", true);
  await capturarCanon(canon, "10_modo_y_fechas.html", "07_baseline_canon_380.png", "Modo fechas ritual movil 380", true);

  const [respBase] = await Promise.all([
    app.waitForResponse((r) => r.url().includes("/baseline") && r.request().method() === "POST", { timeout: 15000 }),
    app.getByRole("button", { name: "Aceptar estas fechas" }).click(),
  ]);
  if (!respBase.ok()) throw new Error(`POST baseline falló: HTTP ${respBase.status()}`);
  // el checklist recarga y reaparecen los "Marcar hecho" de los pendientes
  await app.getByRole("button", { name: "Marcar hecho" }).first().waitFor({ timeout: 15000 });
  for (let i = 0; i < 2; i++) await marcarHechoHoy(app); // dos más → adelantadas

  // 08 Análisis del proyecto (canon 11) — ahora con cumplimiento poblado
  await app.getByRole("button", { name: /Ver análisis del proyecto/ }).click();
  await app.getByText("Análisis de", { exact: false }).first().waitFor({ timeout: 30000 });
  await app.waitForTimeout(1500);
  await capturarApp(app, "08_analisis");
  await capturarCanon(canon, "11_analisis_del_proyecto.html", "08_analisis_canon.png", "Analisis del Proyecto desktop", true);
  await capturarCanon(canon, "11_analisis_del_proyecto.html", "08_analisis_canon_380.png", "Analisis del Proyecto movil 380", true);
  const volver = app.getByRole("button", { name: "← Volver" }).first();
  await volver.waitFor({ state: "visible", timeout: 15000 });
  await volver.click();

  // 09 La Celebración (canon 09) — variante con cumplimiento (modo fechas)
  const marcarReal = app.getByRole("button", { name: "Marcar como realizada" }).first();
  await marcarReal.waitFor({ state: "visible", timeout: 15000 });
  await marcarReal.click();
  await app.getByRole("button", { name: /Sí, es un proyecto/ }).click();
  await app.getByText("Aquí acaba tu idea y nace tu proyecto", { exact: false }).waitFor({ timeout: 30000 });
  await app.waitForTimeout(8000);
  await capturarApp(app, "09_celebracion_cumplimiento");
  await capturarCanon(canon, "09_la_celebracion.html", "09_celebracion_canon.png", "Celebracion cumplimiento desktop", true);
  await capturarCanon(canon, "09_la_celebracion.html", "09_celebracion_canon_380.png", "Celebracion cumplimiento movil 380", true);

  // ── Refresco jul 2026: pantallas del canon nuevo que el FLUJO del gate no
  // visita (o que la app aun no implementa). Se capturan SOLO del canon, sin par
  // de app, para que el fundador vea el objetivo completo. Cuando la app las
  // tenga (o el flujo las alcance), se les cablea su captura de app y pasan a
  // ser un par vivo. Marcadas con "SOLO CANON" en su nombre para que no se
  // confundan con un par app-vs-canon roto.
  await capturarCanon(canon, "07_potenciadores_y_creditos.html", "z_potenciadores_SOLOCANON.png", "Potenciadores y Creditos desktop", true);
  await capturarCanon(canon, "07_potenciadores_y_creditos.html", "z_potenciadores_SOLOCANON_380.png", "Potenciadores y Creditos movil 380", true);
  await capturarCanon(canon, "12_el_cierre_honesto.html", "z_cierre_camino_SOLOCANON.png", "Cierre honesto camino desktop", true);
  await capturarCanon(canon, "12_el_cierre_honesto.html", "z_cierre_camino_SOLOCANON_380.png", "Cierre honesto camino movil 380", true);
  await capturarCanon(canon, "12_el_cierre_honesto.html", "z_cierre_mundo_SOLOCANON.png", "Cierre honesto mundo desktop", true);
  await capturarCanon(canon, "12_el_cierre_honesto.html", "z_cierre_mundo_SOLOCANON_380.png", "Cierre honesto mundo movil 380", true);
  await capturarCanon(canon, "13_detalle_de_actividad.html", "z_detalle_actividad_SOLOCANON.png", "Detalle de actividad desktop", true);
  await capturarCanon(canon, "13_detalle_de_actividad.html", "z_detalle_actividad_SOLOCANON_380.png", "Detalle de actividad movil 380", true);

  await browser.close();
  console.log(`\nGATE: capturas lado a lado en ${OUT} — el veredicto visual es del fundador/auditor.`);
}

main();
