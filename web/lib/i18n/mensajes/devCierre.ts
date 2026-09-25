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

const en: typeof es = {
  camino: {
    titulo: "I can't find a plan worth your time down this road.",
    cuerpo:
      "I explored what you told me and, to be honest, this angle doesn't give me enough to build you a plan that would really move you forward. I'd rather tell you that than hand you filler. It's not a no to your idea: it's a no to this road.",
    porque:
      "Your answers point to a group I can't confirm exists today and is willing to pay, and without a real sign of demand I have nothing to build the stages on.",
  },
  mundo: {
    titulo: "Quality & Trust isn't for this idea, not yet.",
    cuerpo:
      "I activated and explored this world with what you have today, and I didn't find a subproject that adds something without inventing busywork for you. Rather than give you a filler checklist, I'd rather stop here. This world is still waiting for you: you can come back in when your project grows.",
    porque:
      "Quality & Trust shines when you already have customers who come back and you want them to come back more; your idea is still looking for its first customer who isn't someone you know.",
  },
};

export const DEV_CIERRE: PorIdioma<typeof es> = { es, en };
