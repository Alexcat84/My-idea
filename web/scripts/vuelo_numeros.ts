// FASE B (canon 14) - vuelo de Tus Numeros como TABLERO VIVO. Via HTTP real
// contra un `next dev` en :3000, con verificacion directa de Supabase por
// service-role. Cubre el ciclo completo que pidio el fundador, con los
// conteos calculados A MANO en comentario ANTES del assert (regla AGENTS.md):
//
//   crear idea con cifras -> activar (activado_at UNA vez) -> resultado v1
//   -> corregir UNA cifra por el recolector -> el recalculo cambia el
//   veredicto/palancas coherentemente -> la v1 PERSISTE con su fecha y la v2
//   se inserta -> re-narracion archiva la anterior -> activacion repetida y
//   simultanea NO duplican el ancla -> tope diario responde en palabras Y el
//   recalculo sigue vivo despues del tope.
//
// Uso: con `pnpm dev` en :3000,  npx tsx scripts/vuelo_numeros.ts
import { createClient } from "@supabase/supabase-js";
import { autenticarComoDevUser, BASE_URL, cargarEnvRaiz, getJson, postJson } from "./_shared/http";
import { TOPE_RENARRACION_DIA } from "../lib/numerosVivo";

cargarEnvRaiz();
const admin = createClient(process.env.NEXT_PUBLIC_SUPABASE_URL!, process.env.SUPABASE_SERVICE_ROLE_KEY!);

let fallos = 0;
function check(nombre: string, cond: boolean, extra?: unknown) {
  console.log(`${cond ? "OK  " : "FALLO"}: ${nombre}${cond ? "" : `  -> ${JSON.stringify(extra)}`}`);
  if (!cond) fallos++;
}

type Resp = Record<string, unknown>;
function pick<T = unknown>(o: Resp, ...path: string[]): T {
  let cur: unknown = o;
  for (const k of path) cur = (cur as Record<string, unknown>)?.[k];
  return cur as T;
}

function campo(valor: number) {
  return { valor, unidad: null, texto_original: "" };
}

async function sembrarProyecto(userId: string, titulo: string, numeros: Record<string, unknown>) {
  const { data, error } = await admin
    .from("projects")
    .insert({
      user_id: userId,
      entrada_original: titulo,
      titulo,
      fase_actual: "planificacion",
      status: "active",
      tipo_oferta: "producto_fisico",
      unidad_venta: "vela",
      numeros_proyecto: numeros,
    })
    .select("id")
    .single();
  if (error) throw error;
  return (data as { id: string }).id;
}

async function versiones(pid: string) {
  const { data } = await admin
    .from("project_numeros_versiones")
    .select("id, numeros, narracion, narracion_at, created_at")
    .eq("project_id", pid)
    .order("created_at", { ascending: true });
  return (data ?? []) as Array<{ id: string; numeros: Record<string, { valor: number }>; narracion: string | null; narracion_at: string | null; created_at: string }>;
}

async function main() {
  const cookie = await autenticarComoDevUser();
  const { data: lista } = await admin.auth.admin.listUsers();
  const dev = lista.users.find((u) => u.email === "dev@my-idea.local");
  if (!dev) throw new Error("no encuentro el dev user dev@my-idea.local");
  const userId = dev.id;

  // ── Proyecto A: velas de soya, arranca SIN cifras (las mete el recolector).
  const pidA = await sembrarProyecto(userId, "Velas de soya del vuelo", {});
  const ruta = `/api/project/${pidA}/numeros`;

  // 1) Activar. El ancla se pone UNA vez.
  const act1 = await postJson(cookie, ruta, { activar: true });
  check("activar: activado=true y activado_ahora=true", act1.activado === true && act1.activado_ahora === true, act1);
  const pA1 = (await admin.from("projects").select("tus_numeros_activado_at").eq("id", pidA).single()).data as {
    tus_numeros_activado_at: string | null;
  };
  check("DB: tus_numeros_activado_at quedo puesto", pA1.tus_numeros_activado_at != null);
  const anclaOriginal = pA1.tus_numeros_activado_at;

  // 2) Resultado v1: el recolector mete las cifras de PERDIDA.
  //   costo = 30 + 2h x $6 = 42 ; precio 38 ; fijos 200 ; capacidad 5/sem
  //   margen = 38 - 42 = -4  (-10.5%) -> estado PERDIDA
  //   palanca precio (arreglo, piso 30%): 42 / 0.70 = $60 ; margen @60 = +$18
  //   palanca volumen: BLOQUEADA (margen <= 0)
  const velas = {
    costo_materiales_unidad: 30,
    horas_por_unidad: 2,
    valor_hora: 6,
    precio_tentativo: 38,
    costos_fijos_mensuales: 200,
    capacidad_semanal: 5,
  };
  // Envuelto {valor,...} para sembrar directamente en numeros_proyecto (el
  // recolector envuelve solo; una siembra directa debe traerlo ya envuelto).
  const velasWrapped = Object.fromEntries(Object.entries(velas).map(([k, v]) => [k, campo(v)]));
  const v1 = await postJson(cookie, ruta, { numeros: velas });
  check("v1: veredicto PERDIDA (ambar)", pick(v1, "veredicto", "tono") === "perdida", pick(v1, "veredicto", "tono"));
  check("v1: margen calculado -4", pick(v1, "tablero", "margen") === -4, pick(v1, "tablero", "margen"));
  check("v1: palanca precio meta $60 (42/0.70)", pick(v1, "tablero", "palancas", "precio", "meta") === 60);
  check("v1: palanca volumen BLOQUEADA honesta", pick(v1, "tablero", "palancas", "volumen", "bloqueada") === true);

  const trasV1 = await versiones(pidA);
  check("v1: una version insertada", trasV1.length === 1, trasV1.length);
  const fechaV1 = trasV1[0]?.created_at;

  // 3) Corregir UNA cifra: subir el precio de $38 a $70 (el recolector).
  //   nuevo margen = 70 - 42 = 28  (40%) -> estado SANO (>= piso 30%)
  //   -> el veredicto pasa de perdida a sano, y el volumen se DESBLOQUEA.
  const v2 = await postJson(cookie, ruta, { numeros: { precio_tentativo: 70 } });
  check("v2: veredicto pasa a SANO", pick(v2, "veredicto", "tono") === "sano", pick(v2, "veredicto", "tono"));
  check("v2: margen recalculado 28", pick(v2, "tablero", "margen") === 28, pick(v2, "tablero", "margen"));
  check("v2: palanca volumen ya NO bloqueada", pick(v2, "tablero", "palancas", "volumen", "bloqueada") === false);

  const trasV2 = await versiones(pidA);
  check("v2: se inserto (2 versiones)", trasV2.length === 2, trasV2.length);
  check("v1 PERSISTE con su precio original 38", trasV2[0]?.numeros?.precio_tentativo?.valor === 38, trasV2[0]?.numeros?.precio_tentativo?.valor);
  check("v2 guarda el precio corregido 70", trasV2[1]?.numeros?.precio_tentativo?.valor === 70, trasV2[1]?.numeros?.precio_tentativo?.valor);
  check("v1 conserva su fecha (no se reescribio)", trasV2[0]?.created_at === fechaV1);

  // 4) Re-narracion archiva la anterior: dos narrar => dos filas con narracion,
  //    ninguna sobrescrita (append-only).
  await postJson(cookie, ruta, { narrar: true });
  const trasNarrar1 = await versiones(pidA);
  const idsNarradas1 = trasNarrar1.filter((v) => v.narracion_at != null).map((v) => v.id);
  await postJson(cookie, ruta, { narrar: true });
  const trasNarrar2 = await versiones(pidA);
  const narradas2 = trasNarrar2.filter((v) => v.narracion_at != null);
  check("re-narracion inserta filas nuevas (no UPDATE): >= 2 narradas", narradas2.length >= 2, narradas2.length);
  check("la narracion anterior NO se borro ni reescribio", idsNarradas1.every((id) => narradas2.some((v) => v.id === id)));

  // 4.5) La PUERTA de los faltantes (fix del tablero vivo): dar los datos del
  //   ciclo de caja los saca de faltantes y estrena la seccion "Tu ciclo de caja".
  //   Antes (v2, sano, sin datos de ciclo) los 3 estan en faltantes:
  const faltAntes = pick<string[]>(v2, "tablero", "faltantes");
  check("puerta: antes, los 3 campos del ciclo estan en faltantes",
    faltAntes.includes("dias_inventario") && faltAntes.includes("dias_cobro_clientes") && faltAntes.includes("dias_pago_proveedores"), faltAntes);
  //   CCE = dias_inventario + dias_cobro - dias_pago = 40 + 30 - 20 = 50.
  const conCiclo = await postJson(cookie, ruta, { numeros: { dias_inventario: 40, dias_cobro_clientes: 30, dias_pago_proveedores: 20 } });
  check("puerta: CCE = 50 dias (estrena la seccion Tu ciclo de caja)", pick(conCiclo, "tablero", "cicloDias") === 50, pick(conCiclo, "tablero", "cicloDias"));
  const faltDespues = pick<string[]>(conCiclo, "tablero", "faltantes");
  check("puerta: los 3 campos del ciclo SALEN de faltantes (recompensa visible)",
    !faltDespues.includes("dias_inventario") && !faltDespues.includes("dias_cobro_clientes") && !faltDespues.includes("dias_pago_proveedores"), faltDespues);

  // 4.6) El historial de versiones (la promesa "quedan guardadas" con su puerta):
  //   la lista trae fecha + veredicto + margen de cada una, la vigente marcada,
  //   y se puede VISITAR una pasada en modo lectura con SUS numeros de entonces.
  const presente = await getJson(cookie, ruta);
  const hist = pick<Array<{ id: string; tono: string | null; margen: unknown; vigente: boolean }>>(presente, "historial");
  check("historial: lista con la vigente marcada y las demas como pasadas",
    Array.isArray(hist) && hist.length >= 2 && hist[0].vigente === true && hist.slice(1).every((h) => h.vigente === false), hist?.length);
  const idV1 = trasV2[0]?.id;
  const filaV1 = hist.find((h) => h.id === idV1);
  check("historial: v1 figura con SU veredicto (perdida) y margen (-4) de entonces",
    !!filaV1 && filaV1.tono === "perdida" && filaV1.margen === -4, filaV1);
  //   Visitar v1 en modo lectura: su snapshot, sus numeros de entonces.
  const leerV1 = await getJson(cookie, `${ruta}?version=${idV1}`);
  check("visitar v1: modo historico con SUS numeros (margen -4, veredicto perdida)",
    pick(leerV1, "historico") === true && pick(leerV1, "tablero", "margen") === -4 && pick(leerV1, "veredicto", "tono") === "perdida",
    { historico: pick(leerV1, "historico"), margen: pick(leerV1, "tablero", "margen") });
  check("visitar v1: el payload de lectura NO trae puerta de edicion (numeros_declarados)",
    pick(leerV1, "numeros_declarados") === undefined, Object.keys(leerV1));

  // 5) Idempotencia (repetida): activar de nuevo NO vuelve a marcar.
  const actRep = await postJson(cookie, ruta, { activar: true });
  check("activar repetido: activado_ahora=false", actRep.activado_ahora === false, actRep.activado_ahora);
  const pA2 = (await admin.from("projects").select("tus_numeros_activado_at").eq("id", pidA).single()).data as {
    tus_numeros_activado_at: string | null;
  };
  check("DB: el ancla NO cambio (una sola vez)", pA2.tus_numeros_activado_at === anclaOriginal);

  // 6) Idempotencia (simultanea): dos activaciones en paralelo sobre una idea
  //    fresca -> EXACTAMENTE una marca (la prueba de la carrera / WHERE atomico).
  const pidB = await sembrarProyecto(userId, "Idea fresca para la carrera", velasWrapped);
  const rutaB = `/api/project/${pidB}/numeros`;
  const [c1, c2] = await Promise.all([postJson(cookie, rutaB, { activar: true }), postJson(cookie, rutaB, { activar: true })]);
  const ganadores = [c1, c2].filter((r) => r.activado_ahora === true).length;
  check("carrera: exactamente UNA activacion gana (activado_ahora=true)", ganadores === 1, ganadores);

  // 7) Tope diario: sembramos TOPE filas narradas HOY, el narrar siguiente
  //    responde en palabras Y el recalculo sigue vivo despues del tope.
  const pidC = await sembrarProyecto(userId, "Idea para el tope diario", velasWrapped);
  const rutaC = `/api/project/${pidC}/numeros`;
  const ahora = new Date().toISOString();
  await admin.from("project_numeros_versiones").insert(
    Array.from({ length: TOPE_RENARRACION_DIA }, () => ({
      project_id: pidC,
      numeros: Object.fromEntries(Object.entries(velas).map(([k, v]) => [k, campo(v)])),
      tipo_oferta: "producto_fisico",
      narracion: "relectura sembrada",
      narracion_at: ahora,
    }))
  );
  const topeResp = await postJson(cookie, rutaC, { narrar: true });
  check("tope: responde limite_relecturas=true", topeResp.limite_relecturas === true, topeResp.limite_relecturas);
  check("tope: el mensaje habla en palabras de persona", String(topeResp.mensaje ?? "").includes("limite de relecturas"), topeResp.mensaje);
  const recalcTrasTope = await postJson(cookie, rutaC, { numeros: { precio_tentativo: 80 } });
  check("tope: el recalculo determinista SIGUE vivo tras el tope", pick(recalcTrasTope, "tablero", "margen") === 80 - 42, pick(recalcTrasTope, "tablero", "margen"));

  // Limpieza: borrar los proyectos del vuelo (CASCADE limpia sus versiones).
  await admin.from("projects").delete().in("id", [pidA, pidB, pidC]);

  console.log(`\n${fallos === 0 ? "VUELO DE TUS NUMEROS: TODO VERDE" : `VUELO CON ${fallos} FALLO(S)`}`);
  if (fallos > 0) process.exit(1);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
