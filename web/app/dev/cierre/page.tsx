"use client";

/**
 * /dev/cierre — HARNESS de gate (no es producto). El cierre honesto (canon 12)
 * es un estado dentro de IdeaView, no una ruta, así que para capturar su par
 * app-vs-canon se renderiza aquí con tokens reales, en sus dos estados. Los
 * textos son de muestra (en producción el "porqué" es el motivo real del
 * intérprete). Callbacks no-op: esto solo se mira, no se opera.
 */
import { CierreHonesto } from "@/app/ui/CierreHonesto";
import { elegir } from "@/lib/i18n/config";
import { useIdioma } from "@/lib/i18n/IdiomaProvider";
import { DEV_CIERRE } from "@/lib/i18n/mensajes/devCierre";

const noop = () => {};

export default function PreviewCierre() {
  const t = elegir(DEV_CIERRE, useIdioma());
  return (
    <div className="mx-auto flex max-w-[1060px] flex-col gap-12 px-10 py-12">
      <div data-screen-label="Cierre honesto camino">
        <CierreHonesto
          tipo="camino"
          titulo={t.camino.titulo}
          cuerpo={t.camino.cuerpo}
          porque={t.camino.porque}
          creditosDevueltos={null}
          hayPlan={false}
          onVolverAManos={noop}
          onVolverAIdea={noop}
          onExplorarOtroAngulo={noop}
          onVerMundos={noop}
        />
      </div>

      <div data-screen-label="Cierre honesto mundo">
        <CierreHonesto
          tipo="mundo"
          titulo={t.mundo.titulo}
          cuerpo={t.mundo.cuerpo}
          porque={t.mundo.porque}
          // AUD-09: el preview de un mundo es gratis y no hay reembolso que
          // afirmar (BANCO §6.1: un claim de dinero solo con respaldo del ledger).
          creditosDevueltos={null}
          hayPlan={true}
          onVolverAManos={noop}
          onVolverAIdea={noop}
          onExplorarOtroAngulo={noop}
          onVerMundos={noop}
        />
      </div>
    </div>
  );
}
