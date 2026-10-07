/**
 * Páginas públicas de cuenta y de ayuda (encargo del fundador del 6 oct 2026, punto 6): las instrucciones para
 * eliminar la cuenta (requisito de Google Play: accesible sin la app y sin iniciar sesión) y las preguntas
 * frecuentes. Estructura tomada de The Original I Ching (apps/web/src/app/delete-account y faqs).
 *
 * Idiomas: español y francés, como los textos legales, más inglés para quien llega desde la ficha de Google Play en
 * cualquier otro idioma. Los precios salen SIEMPRE de precios.ts (regla P1): aquí no se escribe ningún número de
 * créditos. Ningún texto nombra libros, autores ni estudios (regla D1).
 */
import { PRECIOS } from "@/lib/precios";

export type IdiomaPagina = "es" | "fr" | "en";

export function idiomaDePagina(idioma: string): IdiomaPagina {
  return idioma === "es" || idioma === "fr" ? idioma : "en";
}

/** Los textos legales existen en español y francés; cualquier otro idioma lee el español. */
export function idiomaLegal(idioma: string): "es" | "fr" {
  return idioma === "fr" ? "fr" : "es";
}

const CONTACTO = "support@myideaproject.com";
const PRIVACIDAD = "privacy@myideaproject.com";

export const NAV = {
  es: { inicio: "Volver a My Idea", privacidad: "Privacidad", terminos: "Términos", cookies: "Cookies",
        eliminar: "Eliminar tu cuenta", preguntas: "Preguntas frecuentes",
        soloEsFr: "Este documento está disponible en español y en francés." },
  fr: { inicio: "Retour à My Idea", privacidad: "Confidentialité", terminos: "Conditions", cookies: "Témoins",
        eliminar: "Supprimer ton compte", preguntas: "Questions fréquentes",
        soloEsFr: "Ce document est disponible en espagnol et en français." },
  en: { inicio: "Back to My Idea", privacidad: "Privacy", terminos: "Terms", cookies: "Cookies",
        eliminar: "Delete your account", preguntas: "Frequently asked questions",
        soloEsFr: "This document is available in Spanish and French." },
} as const;

export const ELIMINAR_CUENTA = {
  es: {
    titulo: "Cómo eliminar tu cuenta de My Idea",
    descripcion: "Instrucciones para eliminar tu cuenta de My Idea y todos tus datos, con o sin acceso a la app.",
    intro: "Puedes eliminar tu cuenta y tus datos cuando quieras. No hace falta instalar nada: se hace desde el navegador.",
    comoTitulo: "Desde la app o la web",
    pasos: [
      "Entra en myideaproject.com con tu cuenta.",
      "Abre el centro de cuenta (Cuenta) y baja hasta «Zona de peligro».",
      "Pulsa «Borrar tu cuenta» y escribe la palabra que se te pide para confirmar. Si tienes activada la verificación en dos pasos, te pediremos tu código.",
      "Pulsa «Borrar mi cuenta para siempre». La eliminación es inmediata y no se puede deshacer.",
    ],
    borraTitulo: "Qué se borra",
    borra: [
      "Tu cuenta, tus ideas, tus planes, tus tareas, tus notas, tu bitácora y tus números.",
      "Tu saldo de créditos y tus reservas, tus datos de seguridad y el registro de tu aceptación de los Términos y la Privacidad.",
      "Las ideas que escribiste antes de crear tu cuenta, si aún no habían pasado a ella.",
    ],
    quedaTitulo: "Qué se conserva",
    queda:
      "Tu historial de créditos y de pagos queda anónimo: solo el monto, su tipo y la fecha, sin ningún vínculo contigo. Una huella cifrada de tu correo se conserva para evitar el abuso de las ofertas de bienvenida.",
    sinAccesoTitulo: "Si no puedes entrar",
    sinAcceso: `Escríbenos desde el correo de tu cuenta a ${PRIVACIDAD} con el asunto «Eliminar mi cuenta». Comprobaremos que la cuenta es tuya y la eliminaremos en un plazo máximo de 30 días.`,
    sinCuentaTitulo: "Si nunca creaste una cuenta",
    sinCuenta: "Las ideas escritas sin cuenta se borran solas a los 30 días sin actividad.",
  },
  fr: {
    titulo: "Comment supprimer ton compte My Idea",
    descripcion: "Instructions pour supprimer ton compte My Idea et toutes tes données, avec ou sans accès à l'application.",
    intro: "Tu peux supprimer ton compte et tes données quand tu veux. Rien à installer : tout se fait depuis le navigateur.",
    comoTitulo: "Depuis l'application ou le site",
    pasos: [
      "Connecte-toi à myideaproject.com avec ton compte.",
      "Ouvre le centre de compte (Compte) et descends jusqu'à « Zone de danger ».",
      "Appuie sur « Supprimer ton compte » et écris le mot demandé pour confirmer. Si la vérification en deux étapes est activée, nous te demanderons ton code.",
      "Appuie sur « Supprimer définitivement mon compte ». La suppression est immédiate et irréversible.",
    ],
    borraTitulo: "Ce qui est supprimé",
    borra: [
      "Ton compte, tes idées, tes plans, tes tâches, tes notes, ton journal de bord et tes chiffres.",
      "Ton solde de crédits et tes réservations, tes données de sécurité ainsi que le registre de ton acceptation des Conditions et de la Confidentialité.",
      "Les idées écrites avant la création de ton compte, si elles n'y avaient pas encore été transférées.",
    ],
    quedaTitulo: "Ce qui est conservé",
    queda:
      "Ton historique de crédits et de paiements devient anonyme : seuls le montant, son type et la date subsistent, sans aucun lien avec toi. Une empreinte chiffrée de ton adresse courriel est conservée pour prévenir l'abus des offres de bienvenue.",
    sinAccesoTitulo: "Si tu ne peux pas te connecter",
    sinAcceso: `Écris-nous depuis l'adresse de ton compte à ${PRIVACIDAD} avec l'objet « Supprimer mon compte ». Nous vérifierons que le compte t'appartient et le supprimerons dans un délai maximal de 30 jours.`,
    sinCuentaTitulo: "Si tu n'as jamais créé de compte",
    sinCuenta: "Les idées écrites sans compte sont supprimées automatiquement après 30 jours d'inactivité.",
  },
  en: {
    titulo: "How to delete your My Idea account",
    descripcion: "Instructions to delete your My Idea account and all your data, with or without access to the app.",
    intro: "You can delete your account and your data at any time. Nothing to install: it is done from the browser.",
    comoTitulo: "From the app or the website",
    pasos: [
      "Sign in at myideaproject.com with your account.",
      "Open the account center (Account) and scroll down to “Danger zone”.",
      "Tap “Delete your account” and type the word shown to confirm. If two-step verification is on, we will ask for your code.",
      "Tap “Delete my account forever”. Deletion is immediate and cannot be undone.",
    ],
    borraTitulo: "What is deleted",
    borra: [
      "Your account, your ideas, your plans, your tasks, your notes, your log and your numbers.",
      "Your credit balance and reservations, your security data and the record of your acceptance of the Terms and the Privacy policy.",
      "Ideas you wrote before creating your account, if they had not been moved to it yet.",
    ],
    quedaTitulo: "What is kept",
    queda:
      "Your credit and payment history becomes anonymous: only the amount, its type and the date remain, with no link to you. An encrypted fingerprint of your email is kept to prevent abuse of welcome offers.",
    sinAccesoTitulo: "If you cannot sign in",
    sinAcceso: `Email us from your account address at ${PRIVACIDAD} with the subject “Delete my account”. We will confirm the account is yours and delete it within 30 days at most.`,
    sinCuentaTitulo: "If you never created an account",
    sinCuenta: "Ideas written without an account are deleted automatically after 30 days of inactivity.",
  },
} as const;

const P = PRECIOS;

export const PREGUNTAS = {
  es: {
    titulo: "Preguntas frecuentes",
    descripcion: "Respuestas a las preguntas más comunes sobre My Idea: qué es, qué es gratis, créditos, cuenta y privacidad.",
    intro: "Lo que más nos preguntan. Si no encuentras tu respuesta, escríbenos a " + CONTACTO + ".",
    items: [
      { p: "¿Qué es My Idea?", r: "Una app que te hace preguntas con método sobre tu idea de negocio u organización y ordena lo que respondes en un plan para llevarla a la práctica, con su seguimiento." },
      { p: "¿Qué es gratis?", r: "Tu Claridad (ordenar tu idea) es gratis y no necesita cuenta. El diagnóstico de cada mundo también es gratis. Registrar tu avance, tus notas, tus documentos y tus números va incluido." },
      { p: "¿Qué cuesta créditos?", r: `Tu plan usa ${P.plan_completo} créditos; cada ciclo de seguimiento o de replanteamiento, ${P.seguimiento}; el plan de un mundo, ${P.mundo_activar}. Solo se cobran cuando recibes lo prometido; si algo falla, no se cobra o se reembolsa.` },
      { p: "¿Necesito una cuenta?", r: "Para la Claridad, no. Para guardar tu trabajo y generar tu plan, sí. Las ideas escritas sin cuenta se borran solas a los 30 días sin actividad." },
      { p: "¿My Idea reemplaza a un asesor profesional?", r: "No. Te da método y orden para decidir, no asesoría legal, contable ni de ningún otro profesional. Las decisiones son tuyas." },
      { p: "¿Cómo elimino mi cuenta?", r: "Desde el centro de cuenta, en «Zona de peligro». Si no puedes entrar, escribe a " + PRIVACIDAD + ". Las instrucciones completas están en la página «Eliminar tu cuenta»." },
      { p: "¿Qué hacen con mis datos?", r: "Tus ideas son tuyas. No vendemos tus datos ni los usamos para publicidad. Todo el detalle está en la Política de privacidad." },
      { p: "¿En qué idiomas funciona?", r: "En once idiomas. La app te habla en el tuyo y puedes cambiarlo cuando quieras." },
      { p: "¿Hay app para Android?", r: "Próximamente en Google Play. Mientras tanto, puedes usar My Idea desde el navegador de tu teléfono." },
    ],
  },
  fr: {
    titulo: "Questions fréquentes",
    descripcion: "Réponses aux questions les plus courantes sur My Idea : ce que c'est, ce qui est gratuit, crédits, compte et confidentialité.",
    intro: "Ce qu'on nous demande le plus. Si tu ne trouves pas ta réponse, écris-nous à " + CONTACTO + ".",
    items: [
      { p: "Qu'est-ce que My Idea ?", r: "Une application qui te pose des questions méthodiques sur ton idée d'entreprise ou d'organisation et transforme tes réponses en un plan pour la mettre en pratique, avec son suivi." },
      { p: "Qu'est-ce qui est gratuit ?", r: "Ta Clarté (mettre ton idée en ordre) est gratuite et ne demande pas de compte. Le diagnostic de chaque monde est aussi gratuit. Enregistrer ta progression, tes notes, tes documents et tes chiffres est inclus." },
      { p: "Qu'est-ce qui coûte des crédits ?", r: `Ton plan utilise ${P.plan_completo} crédits; chaque cycle de suivi ou de réorientation, ${P.seguimiento}; le plan d'un monde, ${P.mundo_activar}. Ils ne sont prélevés que lorsque tu reçois ce qui est promis; en cas de problème, rien n'est prélevé ou c'est remboursé.` },
      { p: "Ai-je besoin d'un compte ?", r: "Pour la Clarté, non. Pour enregistrer ton travail et générer ton plan, oui. Les idées écrites sans compte sont supprimées automatiquement après 30 jours d'inactivité." },
      { p: "My Idea remplace-t-elle un conseiller professionnel ?", r: "Non. Elle t'apporte une méthode et de l'ordre pour décider, pas un avis juridique, comptable ni d'aucun autre professionnel. Les décisions t'appartiennent." },
      { p: "Comment supprimer mon compte ?", r: "Depuis le centre de compte, dans « Zone de danger ». Si tu ne peux pas te connecter, écris à " + PRIVACIDAD + ". Les instructions complètes sont sur la page « Supprimer ton compte »." },
      { p: "Que faites-vous de mes données ?", r: "Tes idées t'appartiennent. Nous ne vendons pas tes données et ne les utilisons pas à des fins publicitaires. Tout le détail est dans la Politique de confidentialité." },
      { p: "Dans quelles langues fonctionne l'application ?", r: "En onze langues. L'application te parle dans la tienne et tu peux la changer quand tu veux." },
      { p: "Y a-t-il une application Android ?", r: "Bientôt sur Google Play. D'ici là, tu peux utiliser My Idea depuis le navigateur de ton téléphone." },
    ],
  },
  en: {
    titulo: "Frequently asked questions",
    descripcion: "Answers to the most common questions about My Idea: what it is, what is free, credits, account and privacy.",
    intro: "What people ask us most. If you can't find your answer, email us at " + CONTACTO + ".",
    items: [
      { p: "What is My Idea?", r: "An app that asks you methodical questions about your business or organization idea and turns your answers into a plan to put it into practice, with follow-up." },
      { p: "What is free?", r: "Your Clarity (putting your idea in order) is free and needs no account. Each world's diagnosis is free too. Logging your progress, notes, documents and numbers is included." },
      { p: "What costs credits?", r: `Your plan uses ${P.plan_completo} credits; each follow-up or rethink cycle, ${P.seguimiento}; a world's plan, ${P.mundo_activar}. They are charged only when you receive what was promised; if something fails, nothing is charged or it is refunded.` },
      { p: "Do I need an account?", r: "Not for Clarity. To save your work and generate your plan, yes. Ideas written without an account are deleted automatically after 30 days of inactivity." },
      { p: "Does My Idea replace a professional advisor?", r: "No. It gives you method and order to decide, not legal, accounting or any other professional advice. The decisions are yours." },
      { p: "How do I delete my account?", r: "From the account center, under “Danger zone”. If you can't sign in, email " + PRIVACIDAD + ". Full instructions are on the “Delete your account” page." },
      { p: "What do you do with my data?", r: "Your ideas are yours. We don't sell your data or use it for advertising. All the details are in the Privacy policy." },
      { p: "Which languages does it support?", r: "Eleven languages. The app speaks to you in yours and you can change it anytime." },
      { p: "Is there an Android app?", r: "Coming soon to Google Play. Meanwhile, you can use My Idea from your phone's browser." },
    ],
  },
} as const;
