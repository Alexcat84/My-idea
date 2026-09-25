/** /dev/cierre (app/dev/cierre/page.tsx): los textos de MUESTRA del arnés de
 * gate del cierre honesto (no es producto; en producción el "porqué" es el
 * motivo real del intérprete). */
import type { PorIdioma } from "../config";

const es = {
  camino: {
    titulo: "Por aquí no encuentro un plan que valga tu tiempo.",
    cuerpo:
      "Exploré lo que me contaste y, siendo honesto, este ángulo no me da material suficiente para armarte un plan que de verdad te mueva. Prefiero decírtelo a entregarte relleno. No es un no a tu idea: es un no a este camino.",
    porque:
      "Tus respuestas apuntan a un grupo que hoy no puedo verificar que exista con ganas de pagar, y sin una señal real de demanda no tengo de dónde sostener las etapas.",
  },
  mundo: {
    titulo: "Calidad y Confianza no es para esta idea, todavía.",
    cuerpo:
      "Activé y exploré este mundo con lo que hay hoy, y no encontré un subproyecto que te sume sin inventarte trabajo. Antes que darte un checklist de relleno, prefiero parar aquí. Este mundo te sigue esperando: puedes volver a entrar cuando tu proyecto crezca.",
    porque:
      "Calidad y Confianza brilla cuando ya tienes clientes que vuelven y quieres que vuelvan más; tu idea todavía está buscando al primero que no sea un conocido.",
  },
};

export const DEV_CIERRE: PorIdioma<typeof es> = { es };
