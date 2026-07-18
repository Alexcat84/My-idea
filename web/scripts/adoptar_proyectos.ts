// ETAPA 2 — adopcion EXPLICITA de proyectos (el checklist del fundador).
// Mueve proyectos concretos (por id) a la cuenta real de un email: user_id se
// reasigna en projects/sessions/plans (el resto cuelga de project_id). Sirve
// para que el fundador reclame SUS proyectos de prueba elegidos; los demas
// proyectos historicos de vuelos quedan invisibles para todos.
//
// Uso (desde web/):
//   npx tsx scripts/adoptar_proyectos.ts correo@dominio.com id1,id2,id3        (dry-run)
//   npx tsx scripts/adoptar_proyectos.ts correo@dominio.com id1,id2,id3 --si   (ejecuta)
//
// Disciplina de dinero e identidad: sin --si SOLO muestra que haria.
import { createClient } from "@supabase/supabase-js";
import { cargarEnvRaiz } from "./_shared/http";

cargarEnvRaiz();
const admin = createClient(process.env.NEXT_PUBLIC_SUPABASE_URL!, process.env.SUPABASE_SERVICE_ROLE_KEY!);

async function main() {
  const [email, idsCrudos, flag] = process.argv.slice(2);
  if (!email || !idsCrudos) {
    console.error("uso: npx tsx scripts/adoptar_proyectos.ts <email> <id1,id2,...> [--si]");
    process.exit(2);
  }
  const ejecutar = flag === "--si";
  const projectIds = idsCrudos.split(",").map((s) => s.trim()).filter(Boolean);

  // 1) La cuenta destino, por email (debe existir: primero el login).
  const { data: lista, error: errUsers } = await admin.auth.admin.listUsers({ perPage: 1000 });
  if (errUsers) throw errUsers;
  const destino = lista.users.find((u) => (u.email ?? "").toLowerCase() === email.toLowerCase());
  if (!destino) {
    console.error(`no existe una cuenta con el email ${email}. Haz login primero (magic link) y reintenta.`);
    process.exit(1);
  }
  console.log(`cuenta destino: ${destino.email} (${destino.id})\n`);

  // 2) Cada proyecto: mostrar titulo + dueno actual; adoptar si --si.
  let movidos = 0;
  for (const pid of projectIds) {
    const { data: p, error } = await admin
      .from("projects")
      .select("id, titulo, entrada_original, user_id")
      .eq("id", pid)
      .maybeSingle();
    if (error) throw error;
    if (!p) {
      console.log(`- ${pid}: NO EXISTE, saltado`);
      continue;
    }
    const fila = p as { id: string; titulo: string | null; entrada_original: string; user_id: string };
    const nombre = (fila.titulo ?? fila.entrada_original ?? "").slice(0, 60);
    if (fila.user_id === destino.id) {
      console.log(`- ${pid}: "${nombre}" ya es de ${email}, nada que hacer`);
      continue;
    }
    console.log(`- ${pid}: "${nombre}" (dueno actual ${fila.user_id})`);
    if (!ejecutar) continue;
    // user_id se reasigna en las tres tablas que lo cargan (001): projects por
    // id, sessions/plans por project_id + dueno actual (un id ajeno no matchea).
    const { error: e1 } = await admin.from("projects").update({ user_id: destino.id }).eq("id", pid).eq("user_id", fila.user_id);
    if (e1) throw e1;
    const { error: e2 } = await admin.from("sessions").update({ user_id: destino.id }).eq("project_id", pid).eq("user_id", fila.user_id);
    if (e2) throw e2;
    const { error: e3 } = await admin.from("plans").update({ user_id: destino.id }).eq("user_id", fila.user_id).in(
      "session_id",
      ((await admin.from("sessions").select("id").eq("project_id", pid)).data ?? []).map((s: { id: string }) => s.id)
    );
    if (e3) throw e3;
    movidos++;
    console.log(`    ADOPTADO -> ${email}`);
  }

  console.log(`\n${ejecutar ? `${movidos} proyecto(s) adoptado(s).` : "DRY-RUN: nada se movio. Repite con --si para ejecutar."}`);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
