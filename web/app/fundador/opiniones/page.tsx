/**
 * /fundador/opiniones — el panel del fundador (decisión del 8 oct 2026): las opiniones de todas las cuentas, con
 * filtros por tipo y valoración, el contexto interno de cada una (plan, ciclo, mundo, nodos) y la exportación a CSV.
 * Protegido con FUNDADOR_EMAILS (lib/fundador.ts, esFundador): para cualquier otra identidad es un 404, como si no
 * existiera. Lee con la service role (lib/opinionesServidor.ts) solo después de esa comprobación.
 */
import Link from "next/link";
import { notFound } from "next/navigation";
import { OPINIONES_TIPO } from "@/lib/dbContract";
import { esFundador } from "@/lib/fundador";
import { elegir } from "@/lib/i18n/config";
import { interpolar } from "@/lib/i18n/interpolar";
import { OPINIONES } from "@/lib/i18n/mensajes/opiniones";
import { idiomaDeCookies } from "@/lib/i18n/servidor";
import { filtrosDe } from "@/lib/opiniones";
import { listarOpiniones } from "@/lib/opinionesServidor";
import { createClient } from "@/lib/supabase/server";

export const dynamic = "force-dynamic";
export const metadata = { robots: { index: false, follow: false } };

const SELECT = "rounded-cinta border border-hairline bg-surface px-3 py-1.5 text-[13px] text-ink";

export default async function PanelOpiniones({ searchParams }: { searchParams: Promise<Record<string, string | string[] | undefined>> }) {
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!esFundador(user)) notFound();

  const o = elegir(OPINIONES, await idiomaDeCookies());
  const p = o.panel;
  const crudos = await searchParams;
  const params = new URLSearchParams();
  for (const k of ["tipo", "valoracion"]) {
    const v = crudos[k];
    if (typeof v === "string" && v) params.set(k, v);
  }
  const filtros = filtrosDe(params);
  const consulta = new URLSearchParams();
  if (filtros.tipo) consulta.set("tipo", filtros.tipo);
  if (filtros.valoracion) consulta.set("valoracion", filtros.valoracion);
  const opiniones = await listarOpiniones(filtros);

  return (
    <main className="mx-auto w-full max-w-6xl flex-1 px-4 py-10 sm:px-6">
      <div className="flex flex-wrap items-baseline gap-3">
        <h1 className="text-2xl font-bold tracking-tight">{p.titulo}</h1>
        <span className="text-sm text-dim tabular-nums">{interpolar(p.total, { n: opiniones.length })}</span>
        <Link href="/ideas" className="ms-auto text-[13px] text-dim hover:text-ink">
          My <span className="text-accent">Idea</span>
        </Link>
      </div>

      <form method="get" className="mt-6 flex flex-wrap items-end gap-3">
        <label className="flex flex-col gap-1 text-[12px] text-dim">
          {p.tipo}
          <select name="tipo" defaultValue={filtros.tipo ?? ""} className={SELECT}>
            <option value="">{p.todos}</option>
            {OPINIONES_TIPO.map((t) => (
              <option key={t} value={t}>
                {p.tipos[t]}
              </option>
            ))}
          </select>
        </label>
        <label className="flex flex-col gap-1 text-[12px] text-dim">
          {p.valoracion}
          <select name="valoracion" defaultValue={filtros.valoracion ?? ""} className={SELECT}>
            <option value="">{p.todos}</option>
            <option value="malo">{o.tarjeta.valoracion.malo}</option>
            <option value="bueno">{o.tarjeta.valoracion.bueno}</option>
            <option value="excelente">{o.tarjeta.valoracion.excelente}</option>
            <option value="sin">{p.sinValoracion}</option>
          </select>
        </label>
        <button type="submit" className="rounded-cinta border border-accent/40 bg-accent/10 px-4 py-1.5 text-[13px] font-medium text-accent hover:bg-accent/20">
          {p.filtrar}
        </button>
        <a
          href={`/api/fundador/opiniones?${consulta.toString() ? `${consulta.toString()}&` : ""}formato=csv`}
          className="ms-auto rounded-cinta border border-hairline px-4 py-1.5 text-[13px] text-ink hover:border-accent/50 hover:text-accent"
        >
          {p.exportar}
        </a>
      </form>

      {opiniones.length === 0 ? (
        <p className="mt-10 text-sm text-dim">{p.vacio}</p>
      ) : (
        <div className="mt-6 overflow-x-auto rounded-panel border border-hairline">
          <table className="w-full min-w-[860px] border-collapse text-start text-[13px]">
            <thead className="bg-surface text-[11px] uppercase tracking-[1.2px] text-dim">
              <tr>
                <th className="px-3 py-2 font-semibold">{p.fecha}</th>
                <th className="px-3 py-2 font-semibold">{p.tipo}</th>
                <th className="px-3 py-2 font-semibold">{p.valoracion}</th>
                <th className="px-3 py-2 font-semibold">{p.motivo}</th>
                <th className="px-3 py-2 font-semibold">{p.texto}</th>
                <th className="px-3 py-2 font-semibold">{p.idioma}</th>
                <th className="px-3 py-2 font-semibold">{p.contexto}</th>
              </tr>
            </thead>
            <tbody>
              {opiniones.map((f) => {
                const c = f.contexto as { etiqueta?: string; ciclo?: number; mundo?: string; nodos?: string[] };
                return (
                  <tr key={f.id} className="border-t border-hairline align-top">
                    <td className="whitespace-nowrap px-3 py-2 tabular-nums text-dim">{f.created_at.slice(0, 16).replace("T", " ")}</td>
                    <td className="px-3 py-2">{p.tipos[f.tipo]}</td>
                    <td className={"px-3 py-2 " + (f.valoracion === "malo" ? "text-warn" : f.valoracion === "excelente" ? "text-done" : "")}>
                      {f.valoracion ? o.tarjeta.valoracion[f.valoracion] : <span className="text-dim">{p.sinValoracion}</span>}
                    </td>
                    <td className="px-3 py-2">{f.motivo ? o.tarjeta.motivo[f.motivo] : ""}</td>
                    <td className="max-w-[340px] whitespace-pre-wrap px-3 py-2">{f.texto ?? ""}</td>
                    <td className="px-3 py-2 uppercase text-dim">{f.idioma}</td>
                    <td className="px-3 py-2">
                      {f.tipo === "general" ? (
                        ""
                      ) : (
                        <details>
                          <summary className="cursor-pointer text-dim hover:text-ink">{p.verContexto}</summary>
                          <dl className="mt-2 grid grid-cols-[auto_1fr] gap-x-3 gap-y-1 text-[12px]">
                            <dt className="text-dim">proyecto</dt>
                            <dd className="font-mono">{f.proyecto_id ?? ""}</dd>
                            <dt className="text-dim">objeto</dt>
                            <dd className="font-mono">{f.objeto_id ?? ""}</dd>
                            <dt className="text-dim">etiqueta</dt>
                            <dd>{c.etiqueta ?? ""}</dd>
                            <dt className="text-dim">ciclo</dt>
                            <dd>{c.ciclo ?? ""}</dd>
                            <dt className="text-dim">mundo</dt>
                            <dd>{c.mundo ?? ""}</dd>
                            <dt className="text-dim">nodos</dt>
                            <dd className="font-mono">{(c.nodos ?? []).join(", ")}</dd>
                          </dl>
                        </details>
                      )}
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      )}
    </main>
  );
}
