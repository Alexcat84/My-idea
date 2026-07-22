// ETAPA 2 — EL VUELO DE DINERO (la verificacion mas seria del proyecto:
// es dinero + identidad). HTTP real contra `next dev` en :3000 + ledger real.
//
// LA CONTABILIDAD A MANO (regla AGENTS.md, aqui con creditos):
//   cortesia +20                       -> saldo 20
//   plan core            -5 (entrega)  -> saldo 15
//   Tus Numeros          -2 (activar)  -> saldo 13
//   plan de mundo        -3 (entrega; preview y diagnostico GRATIS) -> saldo 10
//   seguimiento core     -2 (entrega)  -> saldo  8   <- EXACTO
// verificada contra credit_transactions FILA POR FILA (delta, concepto,
// saldo_resultante). Despues: idempotencia en vivo (doble submit no descuenta
// dos veces), 402 limpio sin cobrar y sin perder trabajo, reembolso con su
// log, organizador anonimo + adopcion, y RLS en vivo (B no ve lo de A).
//
// Costo real: ~$0.35-0.50 (entrevistas + 3 planes + diagnostico). Es el
// precio de probar dinero de verdad.
//
// Uso: con `pnpm dev` en :3000,  npx tsx scripts/vuelo_beta.ts
import { createClient } from "@supabase/supabase-js";
import { createServerClient } from "@supabase/ssr";
import { BASE_URL, cargarEnvRaiz, consumirSSE } from "./_shared/http";

cargarEnvRaiz();
const admin = createClient(process.env.NEXT_PUBLIC_SUPABASE_URL!, process.env.SUPABASE_SERVICE_ROLE_KEY!);

let fallos = 0;
function check(nombre: string, cond: boolean, extra?: unknown) {
  console.log(`${cond ? "OK  " : "FALLO"}: ${nombre}${cond ? "" : `  -> ${JSON.stringify(extra)}`}`);
  if (!cond) fallos++;
}

/** Login por password con el MISMO mecanismo de cookies de las rutas reales. */
async function autenticarCon(email: string, password: string): Promise<string> {
  const jar = new Map<string, string>();
  const client = createServerClient(process.env.NEXT_PUBLIC_SUPABASE_URL!, process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!, {
    cookies: {
      getAll() {
        return [...jar.entries()].map(([name, value]) => ({ name, value }));
      },
      setAll(cookies) {
        for (const { name, value } of cookies) jar.set(name, value);
      },
    },
  });
  const { error } = await client.auth.signInWithPassword({ email, password });
  if (error) throw new Error(`login fallo (${email}): ${error.message}`);
  return [...jar.entries()].map(([k, v]) => `${k}=${v}`).join("; ");
}

async function crearUsuario(email: string): Promise<{ id: string; cookie: string; password: string }> {
  const password = crypto.randomUUID() + crypto.randomUUID();
  const { data, error } = await admin.auth.admin.createUser({ email, password, email_confirm: true });
  if (error) throw error;
  const cookie = await autenticarCon(email, password);
  return { id: data.user.id, cookie, password };
}

async function saldoDe(uid: string): Promise<number> {
  const { data } = await admin.from("credit_accounts").select("creditos_total").eq("user_id", uid).maybeSingle();
  return (data as { creditos_total: number } | null)?.creditos_total ?? 0;
}

async function transaccionesDe(uid: string) {
  const { data } = await admin
    .from("credit_transactions")
    .select("delta, saldo_resultante, tipo, concepto, idempotency_key")
    .eq("user_id", uid)
    .order("created_at", { ascending: true });
  return (data ?? []) as Array<{ delta: number; saldo_resultante: number; tipo: string; concepto: string | null; idempotency_key: string | null }>;
}

async function post(cookie: string, ruta: string, body: unknown = {}): Promise<{ status: number; json: Record<string, unknown> }> {
  const res = await fetch(`${BASE_URL}${ruta}`, {
    method: "POST",
    headers: { "Content-Type": "application/json", Cookie: cookie },
    body: JSON.stringify(body),
  });
  return { status: res.status, json: (await res.json().catch(() => ({}))) as Record<string, unknown> };
}

/** Corre N turnos y luego pide el plan por SSE (el boton es permanente). */
async function turnosYPlan(cookie: string, sessionId: string, respuestas: string[]): Promise<string> {
  for (const r of respuestas) {
    const t = await post(cookie, `/api/session/${sessionId}/turn`, { respuesta: r });
    if ((t.json.tipo as string) === "listo_para_plan" || (t.json.tipo as string) === "salio") break;
  }
  const res = await fetch(`${BASE_URL}/api/session/${sessionId}/plan`, {
    method: "POST",
    headers: { "Content-Type": "application/json", Cookie: cookie },
    body: JSON.stringify({}),
  });
  if (!res.ok) throw new Error(`plan ${sessionId} -> ${res.status}: ${await res.text()}`);
  let md = "";
  await consumirSSE(res, ({ evento, data }) => {
    if (evento === "done") md = (data as { markdown: string }).markdown;
    if (evento === "error") throw new Error(`plan SSE error: ${JSON.stringify(data)}`);
  });
  if (md.length < 100) throw new Error("el plan no llego");
  return md;
}

async function main() {
  // 0) 020-024 aplicadas: chequeo ruidoso antes de gastar API.
  const { error: err020 } = await admin.from("credit_accounts").select("user_id").limit(1);
  if (err020) {
    console.error("FALTAN LAS 020-024:", err020.message);
    process.exit(2);
  }

  const marca = Date.now();
  const emailA = `vuelo-beta-a-${marca}@pruebas.my-idea.local`;
  const emailB = `vuelo-beta-b-${marca}@pruebas.my-idea.local`;
  const emailInvisible = `visitante-${crypto.randomUUID()}@invitado.my-idea.local`;

  // ── 1) LA ALLOWLIST: el no invitado recibe palabras, no cuenta (registro
  // por correo+contraseña; magic-link/código murió por el límite de correos).
  const noInvitado = await post("", "/api/auth/registrar", {
    email: `nadie-${marca}@ejemplo.com`,
    password: "Noimporta123",
  });
  check("allowlist: email NO invitado -> {invitado:false} sin crear cuenta",
    noInvitado.status === 200 && noInvitado.json.invitado === false, noInvitado.json);

  // ── 2) Usuario A (cuenta real) + CORTESIA una sola vez.
  const A = await crearUsuario(emailA);
  const { data: c1, error: ec1 } = await admin.rpc("otorgar_cortesia", { p_user_id: A.id, p_monto: 20 });
  check("cortesia: primer otorgamiento deja saldo 20", !ec1 && c1 === 20, { c1, ec1 });
  const { data: c2 } = await admin.rpc("otorgar_cortesia", { p_user_id: A.id, p_monto: 20 });
  check("cortesia: segundo intento NO re-otorga (sigue 20)", c2 === 20 && (await saldoDe(A.id)) === 20, c2);
  const { count: logCortesia } = await admin.from("beta_courtesy_log").select("*", { count: "exact", head: true }).eq("user_id", A.id);
  check("cortesia: beta_courtesy_log tiene UNA fila", logCortesia === 1, logCortesia);

  // ── 3) LA FRONTERA: la identidad invisible no pasa de "Iniciar La Exploracion".
  const I = await crearUsuario(emailInvisible);
  const frontera = await post(I.cookie, "/api/session/start", { texto: "Quiero vender velas artesanales de soya en ferias." });
  check("frontera: invisible -> 401 {login_requerido}", frontera.status === 401 && frontera.json.login_requerido === true, frontera);

  // ── 4) ORGANIZADOR ANONIMO (gratis, sin login) + ADOPCION segura.
  const org = await post(I.cookie, "/api/organizer", {
    texto: "Quiero vender velas artesanales de soya con esencias en ferias de fin de semana; ya vendi seis a conocidos.",
  });
  check("organizador: la identidad invisible SI puede (el gancho es libre)", org.status === 200, { status: org.status, error: org.json.error });
  const proyectoAnon = org.json.project_id as string | undefined;
  if (proyectoAnon) {
    const { adoptarProyectosDeUsuario } = await import("../lib/cuentas");
    const adoptados = await adoptarProyectosDeUsuario(I.id, A.id);
    const { data: pAdoptado } = await admin.from("projects").select("user_id").eq("id", proyectoAnon).single();
    check("adopcion: el proyecto del organizador anonimo paso a la cuenta real",
      adoptados >= 1 && (pAdoptado as { user_id: string }).user_id === A.id, { adoptados, dueno: pAdoptado });
  } else {
    check("adopcion: el organizador devolvio project_id", false, org.json);
  }

  // ── 5) LA CONTABILIDAD A MANO (A: 20 -5 -2 -3 -2 = 8).
  console.log("\n-- plan core (-5) --");
  const inicio = await post(A.cookie, "/api/session/start", {
    texto: "Quiero vender velas artesanales de soya con esencias en ferias; ya vendi seis a conocidos y quiero llegar a desconocidos.",
    project_id: proyectoAnon,
  });
  check("plan core: start pasa la verificacion (saldo 20 >= 5)", inicio.status === 200, inicio);
  const sesionCore = inicio.json.session_id as string;
  await turnosYPlan(A.cookie, sesionCore, [
    "Cada vela me cuesta unos 30 en materiales y la vendo a 80; tardo dos horas por vela.",
    "Mis seis ventas fueron a amigos; nadie desconocido me ha comprado todavia.",
    "Puedo dedicarle 10 horas a la semana y tengo 200 al mes para invertir.",
    "Con eso te conte lo importante, arma mi plan.",
  ]);
  check("plan core: saldo 20 - 5 = 15", (await saldoDe(A.id)) === 15, await saldoDe(A.id));

  console.log("\n-- Tus Numeros (-2, activacion unica) --");
  const act = await post(A.cookie, `/api/project/${proyectoAnon}/numeros`, { activar: true });
  check("numeros: activar entrega el primer tablero", act.status === 200 && act.json.tablero !== undefined, act.status);
  check("numeros: saldo 15 - 2 = 13", (await saldoDe(A.id)) === 13, await saldoDe(A.id));
  // DOBLE-SUBMIT EN VIVO (ruta): repetir activar no descuenta de nuevo.
  const act2 = await post(A.cookie, `/api/project/${proyectoAnon}/numeros`, { activar: true });
  check("doble-submit numeros: sigue 13 (idempotente en la ruta)", act2.status === 200 && (await saldoDe(A.id)) === 13, await saldoDe(A.id));

  console.log("\n-- plan de mundo (-3; preview y diagnostico GRATIS) --");
  const mundoInicio = await post(A.cookie, `/api/project/${proyectoAnon}/world/quality/start`);
  check("preview: arranca gratis (saldo sigue 13)", mundoInicio.status === 200 && (await saldoDe(A.id)) === 13, mundoInicio.status);
  const sesionMundo = mundoInicio.json.session_id as string;
  for (const r of [
    "Mis clientes compran una vez y no vuelvo a saber de ellos; no registro quejas.",
    "Me interesa que vuelvan y me recomienden porque no tengo presupuesto de publicidad.",
  ]) {
    await post(A.cookie, `/api/session/${sesionMundo}/turn`, { respuesta: r });
  }
  const diag = await post(A.cookie, `/api/project/${proyectoAnon}/world/quality/diagnostico`, { session_id: sesionMundo });
  check("diagnostico: gratis (saldo sigue 13)", diag.status === 200 && (await saldoDe(A.id)) === 13, diag.status);
  const resPlanMundo = await fetch(`${BASE_URL}/api/session/${sesionMundo}/plan`, {
    method: "POST",
    headers: { "Content-Type": "application/json", Cookie: A.cookie },
    body: JSON.stringify({}),
  });
  check("plan de mundo: la compra pasa la verificacion (13 >= 3)", resPlanMundo.ok, resPlanMundo.status);
  await consumirSSE(resPlanMundo, () => {});
  check("plan de mundo: saldo 13 - 3 = 10", (await saldoDe(A.id)) === 10, await saldoDe(A.id));

  console.log("\n-- seguimiento core (-2) --");
  const follow = await post(A.cookie, `/api/project/${proyectoAnon}/follow`, { detalles: "Vendi dos velas a desconocidos en la feria." });
  check("follow: pasa la verificacion (10 >= 2)", follow.status === 200, follow);
  const sesionFollow = follow.json.session_id as string;
  await turnosYPlan(A.cookie, sesionFollow, ["Las dos ventas fueron a precio completo; quiero repetirlo cada fin de semana."]);
  check("seguimiento: saldo 10 - 2 = 8 EXACTOS", (await saldoDe(A.id)) === 8, await saldoDe(A.id));

  // ── FILA POR FILA contra credit_transactions.
  const trans = await transaccionesDe(A.id);
  const esperadas = [
    { delta: 20, saldo_resultante: 20, tipo: "grant", concepto: "cortesia" },
    { delta: -5, saldo_resultante: 15, tipo: "consumo", concepto: "plan_completo" },
    { delta: -2, saldo_resultante: 13, tipo: "consumo", concepto: "tus_numeros" },
    { delta: -3, saldo_resultante: 10, tipo: "consumo", concepto: "mundo_activar" },
    { delta: -2, saldo_resultante: 8, tipo: "consumo", concepto: "seguimiento" },
  ];
  check("ledger: exactamente 5 transacciones", trans.length === 5, trans);
  esperadas.forEach((e, i) => {
    const t = trans[i];
    check(
      `ledger fila ${i + 1}: ${e.tipo} ${e.delta} (${e.concepto}) -> saldo ${e.saldo_resultante}`,
      !!t && t.delta === e.delta && t.saldo_resultante === e.saldo_resultante && t.tipo === e.tipo && (t.concepto ?? "").includes(e.concepto),
      t
    );
  });

  // ── 6) IDEMPOTENCIA EN VIVO a nivel ledger: la misma clave no descuenta dos veces.
  const { data: idem } = await admin.rpc("consumir_creditos", {
    p_user_id: A.id, p_concepto: "plan_completo", p_monto: 5, p_idempotency_key: `plan:${sesionCore}`,
  });
  check("idempotencia ledger: repetir plan:{sessionId} devuelve el saldo previo sin descontar",
    idem === 15 && (await saldoDe(A.id)) === 8, { idem, saldo: await saldoDe(A.id) });

  // ── 7) SALDO INSUFICIENTE: rechazo limpio ANTES del esfuerzo, sin cobrar.
  const B = await crearUsuario(emailB); // sin cortesia: saldo 0
  const rechazo = await post(B.cookie, "/api/session/start", { texto: "Quiero un plan para mi idea de panaderia." });
  check("402: B con saldo 0 es rechazado en palabras de persona",
    rechazo.status === 402 && String(rechazo.json.error).includes("Te quedan 0 créditos"), rechazo);
  const { count: sesionesB } = await admin.from("sessions").select("*", { count: "exact", head: true }).eq("user_id", B.id);
  check("402: nada se cobro y nada se creo (cero sesiones de B)", (await saldoDe(B.id)) === 0 && sesionesB === 0, { saldo: await saldoDe(B.id), sesionesB });

  // ── 8) REEMBOLSO con su log (fallo simulado post-cobro).
  const { data: saldoTrasRefund, error: errRefund } = await admin.rpc("reembolsar_creditos", {
    p_user_id: A.id, p_monto: 2, p_motivo: "vuelo_beta: fallo simulado post-cobro",
  });
  const { count: refundLog } = await admin.from("credit_refund_log").select("*", { count: "exact", head: true }).eq("user_id", A.id);
  check("reembolso: 8 + 2 = 10 con su fila en credit_refund_log", saldoTrasRefund === 10 && refundLog === 1, { saldoTrasRefund, errRefund, refundLog });

  // ── 9) RLS EN VIVO: B no ve NADA de A.
  const clienteB = createClient(process.env.NEXT_PUBLIC_SUPABASE_URL!, process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!);
  await clienteB.auth.signInWithPassword({ email: emailB, password: B.password });
  const { data: proyectosVistosPorB } = await clienteB.from("projects").select("id, user_id");
  const veAjeno = (proyectosVistosPorB ?? []).some((p: { user_id: string }) => p.user_id !== B.id);
  check("RLS vivo: el select de B no trae proyectos ajenos", !veAjeno, proyectosVistosPorB?.length);
  const { data: proyectoDeAVistoPorB } = await clienteB.from("projects").select("id").eq("id", proyectoAnon!).maybeSingle();
  check("RLS vivo: B no puede leer el proyecto de A ni por id", proyectoDeAVistoPorB === null, proyectoDeAVistoPorB);
  const { data: ledgerDeAVistoPorB } = await clienteB.from("credit_transactions").select("id").eq("user_id", A.id);
  check("RLS vivo: B no puede leer el ledger de A", (ledgerDeAVistoPorB ?? []).length === 0, ledgerDeAVistoPorB?.length);

  // ── Limpieza: proyectos y usuarios del vuelo.
  await admin.from("projects").delete().eq("user_id", A.id);
  for (const uid of [A.id, B.id, I.id]) await admin.auth.admin.deleteUser(uid);

  console.log(`\n${fallos === 0 ? "VUELO DE DINERO: TODO VERDE (contabilidad 20-5-2-3-2=8 verificada fila por fila)" : `VUELO CON ${fallos} FALLO(S)`}`);
  console.log("(nota honesta: la cortesia y la adopcion se prueban por el MISMO mecanismo que usa auth/confirm; el clic del enlace de correo real no se automatiza)");
  if (fallos > 0) process.exit(1);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
