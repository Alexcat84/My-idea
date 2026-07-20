// CENTRO DE CUENTA — EL VUELO (2FA + borrados, replica del I Ching).
// HTTP real contra `next dev` en :3000 + base real. Requiere la 029 APLICADA
// y en el .env de la raiz: TOTP_ENCRYPTION_KEY y TWO_FACTOR_EMAIL_CODE_SECRET.
//
// Lo que verifica, en orden:
//   A. estado virgen (sin 2FA, desafio "superado" por vacuidad)
//   B. alta TOTP: enroll (QR) -> verificar con token real -> 8 codigos de rescate
//   C. anti-replay: el MISMO token no pasa dos veces
//   D. el gate por sesion EN VIVO: una sesion nueva sin desafio recibe 403 en
//      el motor pagado; supera el desafio con un codigo de rescate y el 403
//      desaparece (pasa a 402: sin saldo, que es lo correcto)
//   E. un codigo de rescate consumido no vuelve a servir
//   F. desactivar (exige desafio superado) y el gate se apaga
//   G. alta por CORREO (codigo sembrado a mano con la pimienta real: el envio
//      de verdad lo prueba el fundador con su inbox) -> habilitado metodo email
//   H. desafio con codigo de correo en una sesion nueva
//   I. borrar UNA idea: la mia se va con su cascada; la ajena da 404 y queda intacta
//   J. candado: 5 fallos seguidos -> 423
//   K. borrar la cuenta: palabra mala 400; con "ELIMINAR" la cuenta y su mundo
//      desaparecen en cascada, la huella de cortesia queda y el guard la ve
//
// Uso: con `pnpm dev` en :3000,  npx tsx scripts/vuelo_cuenta.ts
import { createClient } from "@supabase/supabase-js";
import { createServerClient } from "@supabase/ssr";
import { authenticator } from "@otplib/preset-default";
import { hashEmailCode } from "../lib/dosFactores";
import { cortesiaYaDadaAlCorreo, huellaDeEmail } from "../lib/cuentas";
import { BASE_URL, cargarEnvRaiz } from "./_shared/http";

cargarEnvRaiz();
const admin = createClient(process.env.NEXT_PUBLIC_SUPABASE_URL!, process.env.SUPABASE_SERVICE_ROLE_KEY!);

let fallos = 0;
function check(nombre: string, cond: boolean, extra?: unknown) {
  console.log(`${cond ? "OK  " : "FALLO"}: ${nombre}${cond ? "" : `  -> ${JSON.stringify(extra)}`}`);
  if (!cond) fallos++;
}

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

async function post(cookie: string, ruta: string, body?: unknown): Promise<{ status: number; json: Record<string, unknown> }> {
  const res = await fetch(`${BASE_URL}${ruta}`, {
    method: "POST",
    headers: { "Content-Type": "application/json", Cookie: cookie },
    body: JSON.stringify(body ?? {}),
  });
  return { status: res.status, json: (await res.json().catch(() => ({}))) as Record<string, unknown> };
}

async function getSeguridad(cookie: string): Promise<Record<string, unknown>> {
  const res = await fetch(`${BASE_URL}/api/cuenta/seguridad`, { headers: { Cookie: cookie } });
  return (await res.json()) as Record<string, unknown>;
}

async function sembrarCodigoEmail(uid: string, codigo: string): Promise<void> {
  const pepper = process.env.TWO_FACTOR_EMAIL_CODE_SECRET!;
  await admin.from("two_factor_email_codes").delete().eq("user_id", uid).is("consumed_at", null);
  const { error } = await admin.from("two_factor_email_codes").insert({
    user_id: uid,
    code_hash: hashEmailCode(codigo, pepper),
    expires_at: new Date(Date.now() + 10 * 60_000).toISOString(),
  });
  if (error) throw error;
}

async function main() {
  if (!process.env.TOTP_ENCRYPTION_KEY || !process.env.TWO_FACTOR_EMAIL_CODE_SECRET) {
    throw new Error("faltan TOTP_ENCRYPTION_KEY / TWO_FACTOR_EMAIL_CODE_SECRET en el .env de la raiz");
  }
  const marca = Date.now();
  const emailV = `vuelo-cuenta-${marca}@my-idea.local`;
  const emailW = `vuelo-cuenta-w-${marca}@my-idea.local`;
  const password = crypto.randomUUID() + crypto.randomUUID();

  const { data: creadoV, error: eV } = await admin.auth.admin.createUser({ email: emailV, password, email_confirm: true });
  if (eV) throw eV;
  const V = creadoV.user.id;
  const { data: creadoW, error: eW } = await admin.auth.admin.createUser({ email: emailW, password, email_confirm: true });
  if (eW) throw eW;
  const W = creadoW.user.id;

  try {
    // ── A. Estado virgen ────────────────────────────────────────────────
    const s1 = await autenticarCon(emailV, password);
    const estadoA = await getSeguridad(s1);
    check("A. sin 2FA al nacer", estadoA.habilitado === false && estadoA.desafioSuperado === true, estadoA);

    // ── B. Alta TOTP ────────────────────────────────────────────────────
    const enroll = await post(s1, "/api/cuenta/2fa/enroll");
    const otpauth = String(enroll.json.otpauthUrl ?? "");
    const secreto = /[?&]secret=([A-Z2-7]+)/.exec(otpauth)?.[1] ?? "";
    check("B. enroll entrega QR + otpauth con secreto", enroll.status === 200 && secreto.length > 0 && String(enroll.json.qrDataUrl ?? "").startsWith("data:image/png"), enroll);

    const token1 = authenticator.generate(secreto);
    const activar = await post(s1, "/api/cuenta/2fa/verificar", { token: token1 });
    const rescates = (activar.json.recoveryCodes ?? []) as string[];
    check("B. verificar activa y entrega 8 codigos de rescate", activar.status === 200 && rescates.length === 8, activar);
    const estadoB = await getSeguridad(s1);
    check("B. estado: habilitado metodo totp, desafio superado en ESTA sesion", estadoB.habilitado === true && estadoB.metodo === "totp" && estadoB.desafioSuperado === true, estadoB);

    // ── C. Anti-replay ──────────────────────────────────────────────────
    const replay = await post(s1, "/api/cuenta/2fa/desafio", { token: token1 });
    check("C. el mismo token NO pasa dos veces (replay)", replay.status === 401, replay);

    // ── D. El gate por sesion, en vivo ──────────────────────────────────
    const s2 = await autenticarCon(emailV, password); // sesion NUEVA: sin desafio
    const gateCerrado = await post(s2, "/api/session/start", { texto: "quiero vender velas artesanales en mi barrio" });
    check("D. sesion nueva sin desafio: el motor pagado da 403", gateCerrado.status === 403 && gateCerrado.json.segundo_factor_requerido === true, gateCerrado);

    // El bypass que cazó el review de seguridad: una sesión con solo el
    // primer factor NO puede reemplazar el candado (re-enrolar TOTP ni
    // cambiar el método a correo).
    const reEnroll = await post(s2, "/api/cuenta/2fa/enroll");
    check("D. sesion sin desafio NO re-enrola TOTP (403)", reEnroll.status === 403 && reEnroll.json.segundo_factor_requerido === true, reEnroll);
    await sembrarCodigoEmail(V, "999999");
    const cambioMetodo = await post(s2, "/api/cuenta/2fa/email/verificar", { code: "999999" });
    check("D. sesion sin desafio NO cambia el metodo a correo (403)", cambioMetodo.status === 403, cambioMetodo);

    const desafioRescate = await post(s2, "/api/cuenta/2fa/desafio", { recoveryCode: rescates[0] });
    check("D. el desafio con codigo de rescate abre la sesion", desafioRescate.status === 200, desafioRescate);
    const gateAbierto = await post(s2, "/api/session/start", { texto: "quiero vender velas artesanales en mi barrio" });
    check("D. superado el desafio ya no hay 403 (402: sin saldo, correcto)", gateAbierto.status === 402, gateAbierto);

    // ── E. Rescate de un solo uso ───────────────────────────────────────
    const s2b = await autenticarCon(emailV, password);
    const rescateRepetido = await post(s2b, "/api/cuenta/2fa/desafio", { recoveryCode: rescates[0] });
    check("E. un rescate consumido no vuelve a servir", rescateRepetido.status === 401, rescateRepetido);

    // ── F. Desactivar ───────────────────────────────────────────────────
    const apagar = await post(s2, "/api/cuenta/2fa/desactivar");
    check("F. desactivar con desafio superado", apagar.status === 200, apagar);
    const s3 = await autenticarCon(emailV, password);
    const estadoF = await getSeguridad(s3);
    const sinGate = await post(s3, "/api/session/start", { texto: "quiero vender velas artesanales en mi barrio" });
    check("F. apagado: sin 2FA y sin 403 en sesion nueva", estadoF.habilitado === false && sinGate.status === 402, { estadoF, status: sinGate.status });

    // ── G. Alta por correo (codigo sembrado con la pimienta real) ───────
    await sembrarCodigoEmail(V, "246810");
    const altaEmail = await post(s3, "/api/cuenta/2fa/email/verificar", { code: "246810" });
    check("G. alta por correo: habilitado + 8 rescates nuevos", altaEmail.status === 200 && ((altaEmail.json.recoveryCodes ?? []) as string[]).length === 8, altaEmail);
    const estadoG = await getSeguridad(s3);
    check("G. metodo email", estadoG.metodo === "email" && estadoG.habilitado === true, estadoG);

    // ── H. Desafio con codigo de correo en sesion nueva ─────────────────
    const s4 = await autenticarCon(emailV, password);
    await sembrarCodigoEmail(V, "135791");
    const desafioEmail = await post(s4, "/api/cuenta/2fa/desafio", { emailCode: "135791" });
    check("H. desafio por correo abre la sesion", desafioEmail.status === 200, desafioEmail);
    const codigoReusado = await post(await autenticarCon(emailV, password), "/api/cuenta/2fa/desafio", { emailCode: "135791" });
    check("H. el codigo de correo es de un solo uso", codigoReusado.status === 400 || codigoReusado.status === 401, codigoReusado);

    // ── I. Borrar una idea (la mia si; la ajena no) ─────────────────────
    const { data: pV, error: epV } = await admin.from("projects").insert({ user_id: V, entrada_original: "idea de prueba del vuelo", titulo: "Idea del vuelo" }).select("id").single();
    if (epV) throw epV;
    const { error: esV } = await admin.from("sessions").insert({ user_id: V, project_id: pV.id, tipo: "gratuito", mensaje_entrada: "hola" });
    if (esV) throw esV;
    const { data: pW, error: epW } = await admin.from("projects").insert({ user_id: W, entrada_original: "idea ajena", titulo: "Idea ajena" }).select("id").single();
    if (epW) throw epW;

    const borrarAjena = await fetch(`${BASE_URL}/api/project/${pW.id}`, { method: "DELETE", headers: { Cookie: s4 } });
    check("I. borrar la idea AJENA: 404 (RLS, sin filtrar existencia)", borrarAjena.status === 404);
    const borrarMia = await fetch(`${BASE_URL}/api/project/${pV.id}`, { method: "DELETE", headers: { Cookie: s4 } });
    const { data: quedaP } = await admin.from("projects").select("id").eq("id", pV.id).maybeSingle();
    const { data: quedaS } = await admin.from("sessions").select("id").eq("project_id", pV.id);
    const { data: quedaAjena } = await admin.from("projects").select("id").eq("id", pW.id).maybeSingle();
    check("I. borrar MI idea: se va con su cascada; la ajena queda intacta", borrarMia.status === 200 && !quedaP && (quedaS ?? []).length === 0 && !!quedaAjena, { status: borrarMia.status, quedaP, quedaS, quedaAjena });

    // ── J. Candado: 5 fallos -> 423 ─────────────────────────────────────
    // Adivinar MAL contra un codigo VIGENTE (sin codigo vigente la ruta da
    // 400 "pide uno nuevo" y no cuenta como intento, igual que el I Ching).
    // OJO contable: el rescate repetido del paso E ya dejo UN fallo en la
    // ventana de 15 min, asi que el candado cae al llegar a 5 acumulados
    // (4 de aqui + 1 de E), no a 5 de este loop. Eso es lo correcto.
    const s5 = await autenticarCon(emailV, password);
    await sembrarCodigoEmail(V, "777777");
    let fallos401 = 0;
    let candados423 = 0;
    for (let i = 0; i < 6; i += 1) {
      const intento = await post(s5, "/api/cuenta/2fa/desafio", { emailCode: "000000" });
      if (intento.status === 401) fallos401 += 1;
      if (intento.status === 423) candados423 += 1;
    }
    check("J. los fallos acumulan (401) y el candado cae en 423 al llegar a 5", fallos401 >= 3 && candados423 >= 1 && fallos401 + candados423 === 6, { fallos401, candados423 });

    // ── K. Borrar la cuenta ─────────────────────────────────────────────
    const { error: eCortesia } = await admin.rpc("otorgar_cortesia", { p_user_id: V });
    if (eCortesia) throw eCortesia;
    const palabraMala = await post(s4, "/api/cuenta/eliminar", { confirmacion: "BORRAR" });
    check("K. sin la palabra exacta, 400 y la cuenta sigue", palabraMala.status === 400, palabraMala);
    const eliminar = await post(s4, "/api/cuenta/eliminar", { confirmacion: "ELIMINAR" });
    check("K. con ELIMINAR (y desafio superado), la cuenta se borra", eliminar.status === 200, eliminar);

    const { data: userTrasBorrar } = await admin.auth.admin.getUserById(V);
    const { data: cuentaTras } = await admin.from("credit_accounts").select("user_id").eq("user_id", V).maybeSingle();
    const { data: seguridadTras } = await admin.from("user_seguridad").select("user_id").eq("user_id", V).maybeSingle();
    const { data: huella } = await admin.from("cortesia_email_log").select("email_hash").eq("email_hash", huellaDeEmail(emailV)).maybeSingle();
    check("K. cascada total: sin auth user, sin ledger, sin seguridad; la huella QUEDA", !userTrasBorrar?.user && !cuentaTras && !seguridadTras && !!huella, { user: !!userTrasBorrar?.user, cuentaTras, seguridadTras, huella });
    check("K. el guard de cortesia VE la huella (borrar-y-volver no re-otorga)", (await cortesiaYaDadaAlCorreo(emailV)) === true);
  } finally {
    // Limpieza: W siempre; V ya se borro (o se borra si algo fallo antes).
    await admin.auth.admin.deleteUser(W).catch(() => {});
    await admin.auth.admin.deleteUser(V).catch(() => {});
    await admin.from("cortesia_email_log").delete().eq("email_hash", huellaDeEmail(emailV));
  }

  console.log(fallos === 0 ? "\nVUELO DE CUENTA: TODO VERDE" : `\nVUELO DE CUENTA: ${fallos} FALLO(S)`);
  if (fallos > 0) process.exitCode = 1;
}

main().catch((e) => {
  console.error("vuelo_cuenta reventó:", e);
  process.exitCode = 1;
});
