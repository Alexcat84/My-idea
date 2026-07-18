"use client";

/**
 * /dev/cierre — HARNESS de gate (no es producto). El cierre honesto (canon 12)
 * es un estado dentro de IdeaView, no una ruta, así que para capturar su par
 * app-vs-canon se renderiza aquí con tokens reales, en sus dos estados. Los
 * textos son de muestra (en producción el "porqué" es el motivo real del
 * intérprete). Callbacks no-op: esto solo se mira, no se opera.
 */
import { CierreHonesto } from "@/app/ui/CierreHonesto";

const noop = () => {};

export default function PreviewCierre() {
  return (
    <div className="mx-auto flex max-w-[1060px] flex-col gap-12 px-10 py-12">
      <div data-screen-label="Cierre honesto camino">
        <CierreHonesto
          tipo="camino"
          titulo="Por aquí no encuentro un plan que valga tu tiempo."
          cuerpo="Exploré lo que me contaste y, siendo honesto, este ángulo no me da material suficiente para armarte un plan que de verdad te mueva. Prefiero decírtelo a entregarte relleno. No es un no a tu idea: es un no a este camino."
          porque="Tus respuestas apuntan a un grupo que hoy no puedo verificar que exista con ganas de pagar, y sin una señal real de demanda no tengo de dónde sostener las etapas."
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
          titulo="Calidad y Confianza no es para esta idea, todavía."
          cuerpo="Activé y exploré este mundo con lo que hay hoy, y no encontré un subproyecto que te sume sin inventarte trabajo. Antes que darte un checklist de relleno, prefiero parar aquí. Este mundo te sigue esperando: puedes volver a entrar cuando tu proyecto crezca."
          porque="Calidad y Confianza brilla cuando ya tienes clientes que vuelven y quieres que vuelvan más; tu idea todavía está buscando al primero que no sea un conocido."
          creditosDevueltos={3}
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
