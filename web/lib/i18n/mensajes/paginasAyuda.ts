/**
 * Las páginas públicas de ayuda (encargo del fundador del 6 oct 2026, punto 6; en los once idiomas desde el 7 oct
 * 2026, I18N AL DÍA): el pie común de las páginas públicas (app/ui/PaginaPublica.tsx), /eliminar-cuenta (requisito
 * de Google Play: se lee sin la app y sin iniciar sesión) y /preguntas-frecuentes.
 *
 * Marcadores (los pone lib/legal/paginas.ts, nunca se escriben a mano):
 * - {{plan}}, {{seguimiento}}, {{mundo}}: los precios, de precios.ts (regla P1: ningún número de créditos aquí).
 * - {{contacto}}, {{privacidad}}: los correos de soporte y de privacidad.
 * - {{zona}}, {{borrarTuCuenta}}, {{borrarParaSiempre}}: los rótulos reales del centro de cuenta (catálogo cuenta,
 *   `peligro`), para que las instrucciones digan siempre lo mismo que la pantalla.
 * - {{paginaEliminar}}: el nombre de la página «Eliminar tu cuenta» (nav.eliminar).
 * Ningún texto nombra libros, autores ni estudios (regla D1) ni promete lo que el producto no hace (P9).
 */
import type { PorIdioma } from "../config";

const es = {
  nav: {
    inicio: "Volver a My Idea",
    privacidad: "Privacidad",
    terminos: "Términos",
    cookies: "Cookies",
    eliminar: "Eliminar tu cuenta",
    preguntas: "Preguntas frecuentes",
  },
  eliminarCuenta: {
    titulo: "Cómo eliminar tu cuenta de My Idea",
    descripcion: "Instrucciones para eliminar tu cuenta de My Idea y todos tus datos, con o sin acceso a la app.",
    intro: "Puedes eliminar tu cuenta y tus datos cuando quieras. No hace falta instalar nada: se hace desde el navegador.",
    comoTitulo: "Desde la app o la web",
    pasos: [
      "Entra en myideaproject.com con tu cuenta.",
      "Abre el centro de cuenta (Cuenta) y baja hasta «{{zona}}».",
      "Pulsa «{{borrarTuCuenta}}» y escribe la palabra que se te pide para confirmar. Si tienes activada la verificación en dos pasos, te pediremos tu código.",
      "Pulsa «{{borrarParaSiempre}}». La eliminación es inmediata y no se puede deshacer.",
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
    sinAcceso:
      "Escríbenos desde el correo de tu cuenta a {{privacidad}} con el asunto «Eliminar mi cuenta». Comprobaremos que la cuenta es tuya y la eliminaremos en un plazo máximo de 30 días.",
    sinCuentaTitulo: "Si nunca creaste una cuenta",
    sinCuenta: "Las ideas escritas sin cuenta se borran solas a los 30 días sin actividad.",
  },
  preguntas: {
    titulo: "Preguntas frecuentes",
    descripcion: "Respuestas a las preguntas más comunes sobre My Idea: qué es, qué es gratis, créditos, cuenta y privacidad.",
    intro: "Lo que más nos preguntan. Si no encuentras tu respuesta, escríbenos a {{contacto}}.",
    items: [
      { p: "¿Qué es My Idea?", r: "Una app que te hace preguntas con método sobre tu idea de negocio u organización y ordena lo que respondes en un plan para llevarla a la práctica, con su seguimiento." },
      { p: "¿Qué es gratis?", r: "Tu Claridad (ordenar tu idea) es gratis y no necesita cuenta. El diagnóstico de cada mundo también es gratis. Registrar tu avance, tus notas, tus documentos y tus números va incluido." },
      { p: "¿Qué cuesta créditos?", r: "Tu plan usa {{plan}} créditos; cada ciclo de seguimiento o de replanteamiento, {{seguimiento}}; el plan de un mundo, {{mundo}}. Solo se cobran cuando recibes lo prometido; si algo falla, no se cobra o se reembolsa." },
      { p: "¿Necesito una cuenta?", r: "Para la Claridad, no. Para guardar tu trabajo y generar tu plan, sí. Las ideas escritas sin cuenta se borran solas a los 30 días sin actividad." },
      { p: "¿My Idea reemplaza a un asesor profesional?", r: "No. Te da método y orden para decidir, no asesoría legal, contable ni de ningún otro profesional. Las decisiones son tuyas." },
      { p: "¿Cómo elimino mi cuenta?", r: "Desde el centro de cuenta, en «{{zona}}». Si no puedes entrar, escribe a {{privacidad}}. Las instrucciones completas están en la página «{{paginaEliminar}}»." },
      { p: "¿Qué hacen con mis datos?", r: "Tus ideas son tuyas. No vendemos tus datos ni los usamos para publicidad. Todo el detalle está en la Política de privacidad." },
      { p: "¿En qué idiomas funciona?", r: "En once idiomas. La app te habla en el tuyo y puedes cambiarlo cuando quieras." },
      { p: "¿Cómo funciona la sincronización con mi calendario?", r: "Tu calendario se suscribe a tus fechas en una sola vía: lo que cambias en My Idea llega a tu calendario, pero lo que cambies en tu calendario no vuelve a la app. Las apps de calendario, como Google Calendar, actualizan los calendarios suscritos cada varias horas, no al instante, así que un cambio puede tardar en verse." },
      { p: "¿Hay app para Android?", r: "Próximamente en Google Play. Mientras tanto, puedes usar My Idea desde el navegador de tu teléfono." },
    ],
  },
};

const en: typeof es = {
  nav: {
    inicio: "Back to My Idea",
    privacidad: "Privacy",
    terminos: "Terms",
    cookies: "Cookies",
    eliminar: "Delete your account",
    preguntas: "Frequently asked questions",
  },
  eliminarCuenta: {
    titulo: "How to delete your My Idea account",
    descripcion: "Instructions to delete your My Idea account and all your data, with or without access to the app.",
    intro: "You can delete your account and your data at any time. Nothing to install: it is done from the browser.",
    comoTitulo: "From the app or the website",
    pasos: [
      "Sign in at myideaproject.com with your account.",
      "Open the account center (Account) and scroll down to “{{zona}}”.",
      "Tap “{{borrarTuCuenta}}” and type the word shown to confirm. If two-step verification is on, we will ask for your code.",
      "Tap “{{borrarParaSiempre}}”. Deletion is immediate and cannot be undone.",
    ],
    borraTitulo: "What is deleted",
    borra: [
      "Your account, your ideas, your plans, your tasks, your notes, your logbook and your numbers.",
      "Your credit balance and reservations, your security data and the record of your acceptance of the Terms and the Privacy Policy.",
      "Ideas you wrote before creating your account, if they had not been moved to it yet.",
    ],
    quedaTitulo: "What is kept",
    queda:
      "Your credit and payment history becomes anonymous: only the amount, its type and the date remain, with no link to you. An encrypted fingerprint of your email is kept to prevent abuse of welcome offers.",
    sinAccesoTitulo: "If you cannot sign in",
    sinAcceso:
      "Email {{privacidad}} from your account's email address with the subject “Delete my account”. We will confirm the account is yours and delete it within 30 days.",
    sinCuentaTitulo: "If you never created an account",
    sinCuenta: "Ideas written without an account are deleted automatically after 30 days of inactivity.",
  },
  preguntas: {
    titulo: "Frequently asked questions",
    descripcion: "Answers to the most common questions about My Idea: what it is, what is free, credits, account and privacy.",
    intro: "What people ask us most. If you can't find your answer, email us at {{contacto}}.",
    items: [
      { p: "What is My Idea?", r: "An app that asks you methodical questions about your business or organization idea and turns your answers into a plan to put it into practice, with follow-up." },
      { p: "What is free?", r: "Your Clarity (putting your idea in order) is free and needs no account. Each world's diagnosis is free too. Logging your progress, notes, documents and numbers is included." },
      { p: "What costs credits?", r: "Your plan uses {{plan}} credits; each follow-up or rethink cycle, {{seguimiento}}; a world's plan, {{mundo}}. They are charged only when you receive what was promised; if something fails, nothing is charged or it is refunded." },
      { p: "Do I need an account?", r: "Not for Clarity. To save your work and generate your plan, yes. Ideas written without an account are deleted automatically after 30 days of inactivity." },
      { p: "Does My Idea replace a professional advisor?", r: "No. It gives you method and order to decide, not legal, accounting or any other professional advice. The decisions are yours." },
      { p: "How do I delete my account?", r: "From the account center, under “{{zona}}”. If you can't sign in, email {{privacidad}}. Full instructions are on the “{{paginaEliminar}}” page." },
      { p: "What do you do with my data?", r: "Your ideas are yours. We don't sell your data or use it for advertising. All the details are in the Privacy Policy." },
      { p: "Which languages does it support?", r: "Eleven languages. The app speaks to you in yours and you can change it anytime." },
      { p: "How does syncing with my calendar work?", r: "Your calendar subscribes to your dates one way: what you change in My Idea reaches your calendar, but what you change in your calendar doesn't come back to the app. Calendar apps, such as Google Calendar, refresh subscribed calendars every few hours, not instantly, so a change can take a while to show up." },
      { p: "Is there an Android app?", r: "Coming soon to Google Play. Meanwhile, you can use My Idea from your phone's browser." },
    ],
  },
};

const fr: typeof es = {
  nav: {
    inicio: "Retour à My Idea",
    privacidad: "Confidentialité",
    terminos: "Conditions",
    cookies: "Témoins",
    eliminar: "Supprimer ton compte",
    preguntas: "Questions fréquentes",
  },
  eliminarCuenta: {
    titulo: "Comment supprimer ton compte My Idea",
    descripcion: "Instructions pour supprimer ton compte My Idea et toutes tes données, avec ou sans accès à l'application.",
    intro: "Tu peux supprimer ton compte et tes données quand tu veux. Rien à installer : tout se fait depuis le navigateur.",
    comoTitulo: "Depuis l'application ou le site",
    pasos: [
      "Connecte-toi à myideaproject.com avec ton compte.",
      "Ouvre le centre de compte (Compte) et descends jusqu'à « {{zona}} ».",
      "Appuie sur « {{borrarTuCuenta}} » et écris le mot demandé pour confirmer. Si la vérification en deux étapes est activée, nous te demanderons ton code.",
      "Appuie sur « {{borrarParaSiempre}} ». La suppression est immédiate et irréversible.",
    ],
    borraTitulo: "Ce qui est supprimé",
    borra: [
      "Ton compte, tes idées, tes plans, tes tâches, tes notes, ton journal de bord et tes chiffres.",
      "Ton solde de crédits et tes réservations, tes données de sécurité ainsi que la trace de ton acceptation des Conditions et de la Politique de confidentialité.",
      "Les idées écrites avant la création de ton compte, si elles n'y avaient pas encore été transférées.",
    ],
    quedaTitulo: "Ce qui est conservé",
    queda:
      "Ton historique de crédits et de paiements devient anonyme : seuls le montant, son type et la date subsistent, sans aucun lien avec toi. Une empreinte chiffrée de ton adresse courriel est conservée pour prévenir l'abus des offres de bienvenue.",
    sinAccesoTitulo: "Si tu ne peux pas te connecter",
    sinAcceso:
      "Écris-nous depuis l'adresse de ton compte à {{privacidad}} avec l'objet « Supprimer mon compte ». Nous vérifierons que le compte t'appartient et le supprimerons dans un délai maximal de 30 jours.",
    sinCuentaTitulo: "Si tu n'as jamais créé de compte",
    sinCuenta: "Les idées écrites sans compte sont supprimées automatiquement après 30 jours d'inactivité.",
  },
  preguntas: {
    titulo: "Questions fréquentes",
    descripcion: "Réponses aux questions les plus courantes sur My Idea : ce que c'est, ce qui est gratuit, crédits, compte et confidentialité.",
    intro: "Ce qu'on nous demande le plus. Si tu ne trouves pas ta réponse, écris-nous à {{contacto}}.",
    items: [
      { p: "Qu'est-ce que My Idea?", r: "Une application qui te pose des questions méthodiques sur ton idée d'entreprise ou d'organisation et transforme tes réponses en un plan pour la mettre en pratique, avec son suivi." },
      { p: "Qu'est-ce qui est gratuit?", r: "Ta Clarté (mettre ton idée en ordre) est gratuite et ne demande pas de compte. Le diagnostic de chaque monde est aussi gratuit. Enregistrer ta progression, tes notes, tes documents et tes chiffres est inclus." },
      { p: "Qu'est-ce qui coûte des crédits?", r: "Ton plan utilise {{plan}} crédits; chaque cycle de suivi ou de nouveau cap, {{seguimiento}}; le plan d'un monde, {{mundo}}. Ils ne sont prélevés que lorsque tu reçois ce qui est promis; en cas de problème, rien n'est prélevé ou c'est remboursé." },
      { p: "Ai-je besoin d'un compte?", r: "Pour la Clarté, non. Pour enregistrer ton travail et générer ton plan, oui. Les idées écrites sans compte sont supprimées automatiquement après 30 jours d'inactivité." },
      { p: "My Idea remplace-t-elle un conseiller professionnel?", r: "Non. Elle t'apporte une méthode et de l'ordre pour décider, pas des conseils juridiques, comptables ou de tout autre professionnel. Les décisions t'appartiennent." },
      { p: "Comment supprimer mon compte?", r: "Depuis le centre de compte, dans « {{zona}} ». Si tu ne peux pas te connecter, écris à {{privacidad}}. Les instructions complètes sont sur la page « {{paginaEliminar}} »." },
      { p: "Que fait My Idea de mes données?", r: "Tes idées t'appartiennent. Nous ne vendons pas tes données et ne les utilisons pas à des fins publicitaires. Tout le détail est dans la Politique de confidentialité." },
      { p: "Dans quelles langues fonctionne l'application?", r: "En onze langues. L'application te parle dans la tienne et tu peux la changer quand tu veux." },
      { p: "Comment fonctionne la synchronisation avec mon calendrier?", r: "Ton calendrier s'abonne à tes dates dans un seul sens : ce que tu changes dans My Idea arrive dans ton calendrier, mais ce que tu changes dans ton calendrier ne revient pas dans l'application. Les applis de calendrier, comme Google Agenda, actualisent les calendriers auxquels tu es abonné toutes les quelques heures, pas instantanément : un changement peut donc prendre du temps à apparaître." },
      { p: "Y a-t-il une application Android?", r: "Bientôt sur Google Play. D'ici là, tu peux utiliser My Idea depuis le navigateur de ton téléphone." },
    ],
  },
};

const pt: typeof es = {
  nav: {
    inicio: "Voltar ao My Idea",
    privacidad: "Privacidade",
    terminos: "Termos",
    cookies: "Cookies",
    eliminar: "Excluir sua conta",
    preguntas: "Perguntas frequentes",
  },
  eliminarCuenta: {
    titulo: "Como excluir sua conta do My Idea",
    descripcion: "Instruções para excluir sua conta do My Idea e todos os seus dados, com ou sem acesso ao app.",
    intro: "Você pode excluir sua conta e seus dados quando quiser. Não é preciso instalar nada: tudo é feito pelo navegador.",
    comoTitulo: "Pelo app ou pelo site",
    pasos: [
      "Entre em myideaproject.com com sua conta.",
      "Abra a central da conta (Conta) e desça até “{{zona}}”.",
      "Toque em “{{borrarTuCuenta}}” e digite a palavra pedida para confirmar. Se a verificação em duas etapas estiver ativada, vamos pedir o seu código.",
      "Toque em “{{borrarParaSiempre}}”. A exclusão é imediata e não pode ser desfeita.",
    ],
    borraTitulo: "O que é excluído",
    borra: [
      "Sua conta, suas ideias, seus planos, suas tarefas, suas notas, seu diário de bordo e seus números.",
      "Seu saldo de créditos e suas reservas, seus dados de segurança e o registro da sua aceitação dos Termos e da Privacidade.",
      "As ideias que você escreveu antes de criar sua conta, se ainda não tinham passado para ela.",
    ],
    quedaTitulo: "O que é mantido",
    queda:
      "Seu histórico de créditos e de pagamentos fica anônimo: só restam o valor, o tipo e a data, sem nenhum vínculo com você. Uma impressão digital criptografada do seu e-mail é mantida para evitar o abuso das ofertas de boas-vindas.",
    sinAccesoTitulo: "Se você não consegue entrar",
    sinAcceso:
      "Escreva para {{privacidad}} a partir do e-mail da sua conta, com o assunto “Excluir minha conta”. Vamos confirmar que a conta é sua e excluí-la em no máximo 30 dias.",
    sinCuentaTitulo: "Se você nunca criou uma conta",
    sinCuenta: "As ideias escritas sem conta são apagadas automaticamente após 30 dias sem atividade.",
  },
  preguntas: {
    titulo: "Perguntas frequentes",
    descripcion: "Respostas às perguntas mais comuns sobre o My Idea: o que é, o que é grátis, créditos, conta e privacidade.",
    intro: "O que mais nos perguntam. Se não encontrar sua resposta, escreva para {{contacto}}.",
    items: [
      { p: "O que é o My Idea?", r: "Um app que faz perguntas metódicas sobre a sua ideia de negócio ou de organização e organiza suas respostas em um plano para colocá-la em prática, com acompanhamento." },
      { p: "O que é grátis?", r: "Sua Clareza (organizar sua ideia) é grátis e não precisa de conta. O diagnóstico de cada mundo também é grátis. Registrar seu avanço, suas notas, seus documentos e seus números está incluído." },
      { p: "O que custa créditos?", r: "Seu plano usa {{plan}} créditos; cada ciclo de acompanhamento ou de novo rumo, {{seguimiento}}; o plano de um mundo, {{mundo}}. Eles só são cobrados quando você recebe o que foi prometido; se algo falhar, nada é cobrado ou o valor é reembolsado." },
      { p: "Preciso de uma conta?", r: "Para a Clareza, não. Para salvar seu trabalho e gerar seu plano, sim. As ideias escritas sem conta são apagadas automaticamente após 30 dias sem atividade." },
      { p: "O My Idea substitui um assessor profissional?", r: "Não. Ele oferece método e ordem para você decidir, não assessoria jurídica, contábil nem de nenhum outro profissional. As decisões são suas." },
      { p: "Como excluo minha conta?", r: "Pela central da conta, em “{{zona}}”. Se não conseguir entrar, escreva para {{privacidad}}. As instruções completas estão na página “{{paginaEliminar}}”." },
      { p: "O que acontece com meus dados?", r: "Suas ideias são suas. Não vendemos seus dados nem os usamos para publicidade. Todos os detalhes estão na Política de Privacidade." },
      { p: "Em quais idiomas funciona?", r: "Em onze idiomas. O app fala com você no seu idioma e você pode trocá-lo quando quiser." },
      { p: "Como funciona a sincronização com o meu calendário?", r: "Seu calendário assina suas datas em um só sentido: o que você muda no My Idea chega ao seu calendário, mas o que você muda no calendário não volta para o aplicativo. Os apps de calendário, como o Google Agenda, atualizam os calendários assinados a cada algumas horas, não na hora, então uma mudança pode demorar a aparecer." },
      { p: "Tem app para Android?", r: "Em breve no Google Play. Enquanto isso, você pode usar o My Idea pelo navegador do seu celular." },
    ],
  },
};

const de: typeof es = {
  nav: {
    inicio: "Zurück zu My Idea",
    privacidad: "Datenschutz",
    terminos: "Nutzungsbedingungen",
    cookies: "Cookies",
    eliminar: "Dein Konto löschen",
    preguntas: "Häufige Fragen",
  },
  eliminarCuenta: {
    titulo: "So löschst du dein Konto bei My Idea",
    descripcion: "Anleitung, wie du dein Konto bei My Idea und alle deine Daten löschst, mit oder ohne Zugang zur App.",
    intro: "Du kannst dein Konto und deine Daten jederzeit löschen. Du musst nichts installieren: Alles geht im Browser.",
    comoTitulo: "In der App oder auf der Website",
    pasos: [
      "Melde dich auf myideaproject.com mit deinem Konto an.",
      "Öffne die Kontoverwaltung (Konto) und scrolle nach unten zu „{{zona}}“.",
      "Tippe auf „{{borrarTuCuenta}}“ und gib zur Bestätigung das verlangte Wort ein. Wenn die Bestätigung in zwei Schritten aktiv ist, fragen wir dich nach deinem Code.",
      "Tippe auf „{{borrarParaSiempre}}“. Die Löschung erfolgt sofort und lässt sich nicht rückgängig machen.",
    ],
    borraTitulo: "Was gelöscht wird",
    borra: [
      "Dein Konto, deine Ideen, deine Pläne, deine Aufgaben, deine Notizen, dein Logbuch und deine Zahlen.",
      "Dein Guthaben und deine Reservierungen, deine Sicherheitsdaten und der Nachweis, dass du die Nutzungsbedingungen und die Datenschutzerklärung akzeptiert hast.",
      "Die Ideen, die du vor dem Erstellen deines Kontos geschrieben hast, falls sie noch nicht in dein Konto übertragen wurden.",
    ],
    quedaTitulo: "Was erhalten bleibt",
    queda:
      "Dein Guthaben- und Zahlungsverlauf wird anonymisiert: Es bleiben nur der Betrag, seine Art und das Datum, ohne jede Verbindung zu dir. Ein verschlüsselter Fingerabdruck deiner E-Mail-Adresse wird aufbewahrt, um den Missbrauch von Willkommensangeboten zu verhindern.",
    sinAccesoTitulo: "Wenn du dich nicht anmelden kannst",
    sinAcceso:
      "Schreib uns von der E-Mail-Adresse deines Kontos an {{privacidad}} mit dem Betreff „Mein Konto löschen“. Wir prüfen, ob das Konto dir gehört, und löschen es innerhalb von höchstens 30 Tagen.",
    sinCuentaTitulo: "Wenn du nie ein Konto erstellt hast",
    sinCuenta: "Ideen, die ohne Konto geschrieben wurden, werden nach 30 Tagen ohne Aktivität automatisch gelöscht.",
  },
  preguntas: {
    titulo: "Häufige Fragen",
    descripcion: "Antworten auf die häufigsten Fragen zu My Idea: was es ist, was kostenlos ist, Guthaben, Konto und Datenschutz.",
    intro: "Das werden wir am häufigsten gefragt. Wenn du deine Antwort nicht findest, schreib uns an {{contacto}}.",
    items: [
      { p: "Was ist My Idea?", r: "Eine App, die dir methodische Fragen zu deiner Geschäfts- oder Organisationsidee stellt und aus deinen Antworten einen Plan macht, um sie in die Tat umzusetzen, mit regelmäßigem Zwischenstand." },
      { p: "Was ist kostenlos?", r: "Deine Klarheit (deine Idee ordnen) ist kostenlos und braucht kein Konto. Die Diagnose jeder Welt ist ebenfalls kostenlos. Deinen Fortschritt, deine Notizen, deine Dokumente und deine Zahlen festzuhalten, ist inklusive." },
      { p: "Was kostet Guthaben?", r: "Dein Plan kostet {{plan}} Punkte; jeder Zyklus für einen Zwischenstand oder eine Neuausrichtung {{seguimiento}}; der Plan einer Welt {{mundo}}. Abgebucht wird nur, wenn du bekommst, was versprochen wurde; wenn etwas schiefgeht, wird nichts abgebucht oder es wird erstattet." },
      { p: "Brauche ich ein Konto?", r: "Für die Klarheit nicht. Um deine Arbeit zu speichern und deinen Plan zu erstellen, ja. Ideen, die ohne Konto geschrieben wurden, werden nach 30 Tagen ohne Aktivität automatisch gelöscht." },
      { p: "Ersetzt My Idea eine professionelle Beratung?", r: "Nein. Es gibt dir Methode und Ordnung, um zu entscheiden, aber keine Rechts-, Buchhaltungs- oder sonstige professionelle Beratung. Die Entscheidungen triffst du." },
      { p: "Wie lösche ich mein Konto?", r: "In der Kontoverwaltung, unter „{{zona}}“. Wenn du dich nicht anmelden kannst, schreib an {{privacidad}}. Die vollständige Anleitung steht auf der Seite „{{paginaEliminar}}“." },
      { p: "Was passiert mit meinen Daten?", r: "Deine Ideen gehören dir. Wir verkaufen deine Daten nicht und nutzen sie nicht für Werbung. Alle Einzelheiten stehen in der Datenschutzerklärung." },
      { p: "In welchen Sprachen gibt es die App?", r: "In elf Sprachen. Die App spricht deine Sprache, und du kannst sie jederzeit wechseln." },
      { p: "Wie funktioniert die Synchronisierung mit meinem Kalender?", r: "Dein Kalender abonniert deine Termine in eine Richtung: Was du in My Idea änderst, kommt in deinem Kalender an, aber was du im Kalender änderst, geht nicht zurück in die App. Kalender-Apps wie Google Kalender aktualisieren abonnierte Kalender alle paar Stunden, nicht sofort; eine Änderung kann also eine Weile brauchen, bis sie erscheint." },
      { p: "Gibt es eine App für Android?", r: "Bald bei Google Play. Bis dahin kannst du My Idea im Browser deines Handys nutzen." },
    ],
  },
};

const it: typeof es = {
  nav: {
    inicio: "Torna a My Idea",
    privacidad: "Privacy",
    terminos: "Termini",
    cookies: "Cookie",
    eliminar: "Elimina il tuo account",
    preguntas: "Domande frequenti",
  },
  eliminarCuenta: {
    titulo: "Come eliminare il tuo account My Idea",
    descripcion: "Istruzioni per eliminare il tuo account My Idea e tutti i tuoi dati, con o senza accesso all'app.",
    intro: "Puoi eliminare il tuo account e i tuoi dati quando vuoi. Non serve installare nulla: si fa dal browser.",
    comoTitulo: "Dall'app o dal sito",
    pasos: [
      "Accedi a myideaproject.com con il tuo account.",
      "Apri il centro account (Account) e scorri fino a «{{zona}}».",
      "Tocca «{{borrarTuCuenta}}» e scrivi la parola richiesta per confermare. Se hai attivato la verifica in due passaggi, ti chiederemo il tuo codice.",
      "Tocca «{{borrarParaSiempre}}». L'eliminazione è immediata e non si può annullare.",
    ],
    borraTitulo: "Cosa viene eliminato",
    borra: [
      "Il tuo account, le tue idee, i tuoi piani, le tue attività, le tue note, il tuo diario di bordo e i tuoi numeri.",
      "Il tuo saldo di crediti e le tue prenotazioni, i tuoi dati di sicurezza e la registrazione della tua accettazione dei Termini e della Privacy.",
      "Le idee che hai scritto prima di creare il tuo account, se non vi erano ancora state trasferite.",
    ],
    quedaTitulo: "Cosa viene conservato",
    queda:
      "La cronologia dei tuoi crediti e pagamenti diventa anonima: restano solo l'importo, il tipo e la data, senza alcun legame con te. Un'impronta cifrata della tua email viene conservata per evitare abusi delle offerte di benvenuto.",
    sinAccesoTitulo: "Se non riesci ad accedere",
    sinAcceso:
      "Scrivici dall'indirizzo email del tuo account a {{privacidad}} con oggetto «Elimina il mio account». Verificheremo che l'account sia tuo e lo elimineremo entro 30 giorni al massimo.",
    sinCuentaTitulo: "Se non hai mai creato un account",
    sinCuenta: "Le idee scritte senza account si cancellano da sole dopo 30 giorni di inattività.",
  },
  preguntas: {
    titulo: "Domande frequenti",
    descripcion: "Risposte alle domande più comuni su My Idea: cos'è, cosa è gratis, crediti, account e privacy.",
    intro: "Le domande che ci fanno più spesso. Se non trovi la tua risposta, scrivici a {{contacto}}.",
    items: [
      { p: "Cos'è My Idea?", r: "Un'app che ti fa domande con metodo sulla tua idea di impresa o di organizzazione e mette in ordine le tue risposte in un piano per realizzarla, con le sue revisioni." },
      { p: "Cosa è gratis?", r: "La tua Chiarezza (mettere in ordine la tua idea) è gratis e non richiede un account. Anche la diagnosi di ogni mondo è gratis. Registrare i tuoi progressi, le tue note, i tuoi documenti e i tuoi numeri è incluso." },
      { p: "Cosa si paga con i crediti?", r: "Il tuo piano usa {{plan}} crediti; ogni ciclo di revisione o di nuova rotta, {{seguimiento}}; il piano di un mondo, {{mundo}}. I crediti vengono addebitati solo quando ricevi ciò che ti è stato promesso; se qualcosa va storto, non si addebita nulla o i crediti vengono rimborsati." },
      { p: "Mi serve un account?", r: "Per la Chiarezza, no. Per salvare il tuo lavoro e generare il tuo piano, sì. Le idee scritte senza account si cancellano da sole dopo 30 giorni di inattività." },
      { p: "My Idea prende il posto di un consulente professionale?", r: "No. Ti dà metodo e ordine per decidere, non una consulenza legale, contabile o di qualsiasi altro professionista. Le decisioni sono tue." },
      { p: "Come elimino il mio account?", r: "Dal centro account, in «{{zona}}». Se non riesci ad accedere, scrivi a {{privacidad}}. Le istruzioni complete sono nella pagina «{{paginaEliminar}}»." },
      { p: "Cosa succede ai miei dati?", r: "Le tue idee sono tue. Non vendiamo i tuoi dati né li usiamo per la pubblicità. Tutti i dettagli sono nell'Informativa sulla privacy." },
      { p: "In quali lingue funziona?", r: "In undici lingue. L'app ti parla nella tua e puoi cambiarla quando vuoi." },
      { p: "Come funziona la sincronizzazione con il mio calendario?", r: "Il tuo calendario si abbona alle tue date in un solo senso: quello che cambi in My Idea arriva al tuo calendario, ma quello che cambi nel calendario non torna nell'app. Le app di calendario, come Google Calendar, aggiornano i calendari a cui sei abbonato ogni qualche ora, non all'istante, quindi una modifica può metterci un po' a comparire." },
      { p: "C'è un'app per Android?", r: "Presto su Google Play. Nel frattempo, puoi usare My Idea dal browser del tuo telefono." },
    ],
  },
};

const ja: typeof es = {
  nav: {
    inicio: "My Idea に戻る",
    privacidad: "プライバシー",
    terminos: "利用規約",
    cookies: "Cookie",
    eliminar: "アカウントの削除",
    preguntas: "よくある質問",
  },
  eliminarCuenta: {
    titulo: "My Idea のアカウントを削除する方法",
    descripcion: "アプリにアクセスできる場合もできない場合も、My Idea のアカウントとすべてのデータを削除する手順です。",
    intro: "アカウントとデータはいつでも削除できます。インストールは不要で、ブラウザから操作できます。",
    comoTitulo: "アプリまたはウェブサイトから",
    pasos: [
      "アカウントで myideaproject.com にログインします。",
      "アカウントセンター（アカウント）を開き、「{{zona}}」までスクロールします。",
      "「{{borrarTuCuenta}}」をタップし、確認のために表示された言葉を入力します。2段階認証を有効にしている場合は、コードの入力をお願いします。",
      "「{{borrarParaSiempre}}」をタップします。削除はすぐに行われ、元に戻すことはできません。",
    ],
    borraTitulo: "削除されるもの",
    borra: [
      "アカウント、アイデア、プラン、タスク、メモ、活動ログ、数字。",
      "ポイント残高と予約、セキュリティ情報、利用規約とプライバシーポリシーへの同意の記録。",
      "アカウント作成前に書いたアイデアのうち、まだアカウントに移されていなかったもの。",
    ],
    quedaTitulo: "保持されるもの",
    queda:
      "ポイントと支払いの履歴は匿名化されます。残るのは金額、その種類、日付だけで、ご本人との結びつきは一切ありません。歓迎特典の不正利用を防ぐため、メールアドレスを暗号化したハッシュ値は保持されます。",
    sinAccesoTitulo: "ログインできない場合",
    sinAcceso:
      "アカウントのメールアドレスから {{privacidad}} 宛に、件名「アカウントを削除してください」でご連絡ください。アカウントがご本人のものであることを確認し、最長30日以内に削除します。",
    sinCuentaTitulo: "アカウントを作成したことがない場合",
    sinCuenta: "アカウントなしで書いたアイデアは、30日間操作がないと自動的に削除されます。",
  },
  preguntas: {
    titulo: "よくある質問",
    descripcion: "My Idea についてよくある質問への回答です。My Idea とは何か、無料でできること、ポイント、アカウント、プライバシーについて。",
    intro: "よくいただく質問をまとめました。答えが見つからない場合は、{{contacto}} までご連絡ください。",
    items: [
      { p: "My Idea とは何ですか？", r: "ビジネスや組織のアイデアについて方法に沿って質問し、回答を実行のためのプランに整理するアプリです。その後のフォローアップもあります。" },
      { p: "無料でできることは？", r: "明確さ（アイデアの整理）は無料で、アカウントも不要です。各ワールドの診断も無料です。進捗、メモ、書類、数字の記録も含まれています。" },
      { p: "ポイントがかかるのは？", r: "プランは {{plan}} ポイント、フォローアップまたは見直しのサイクルは1回 {{seguimiento}} ポイント、ワールドのプランは {{mundo}} ポイントです。約束どおりのものを受け取ったときだけ差し引かれ、問題が起きた場合は差し引かれないか、返還されます。" },
      { p: "アカウントは必要ですか？", r: "明確さだけなら不要です。作業を保存してプランを作成するには必要です。アカウントなしで書いたアイデアは、30日間操作がないと自動的に削除されます。" },
      { p: "My Idea は専門家の代わりになりますか？", r: "いいえ。判断するための方法と整理を提供するもので、法律、会計、その他の専門家による助言ではありません。決めるのはご自身です。" },
      { p: "アカウントを削除するには？", r: "アカウントセンターの「{{zona}}」から削除できます。ログインできない場合は {{privacidad}} までご連絡ください。詳しい手順は「{{paginaEliminar}}」のページにあります。" },
      { p: "私のデータはどう扱われますか？", r: "アイデアはご自身のものです。データを販売したり、広告に使ったりすることはありません。詳しくはプライバシーポリシーをご覧ください。" },
      { p: "どの言語に対応していますか？", r: "11の言語に対応しています。アプリはお使いの言語で表示され、いつでも変更できます。" },
      { p: "カレンダーとの同期はどのように動きますか？", r: "お使いのカレンダーは、日付を一方向で購読します。My Idea で変更した内容はカレンダーに届きますが、カレンダー側で変更した内容はアプリには戻りません。Google カレンダーなどのカレンダーアプリは、購読しているカレンダーを即時ではなく数時間ごとに更新するため、変更が反映されるまで時間がかかることがあります。" },
      { p: "Android アプリはありますか？", r: "近日 Google Play で公開予定です。それまでは、スマートフォンのブラウザから My Idea をご利用いただけます。" },
    ],
  },
};

const zh: typeof es = {
  nav: {
    inicio: "返回 My Idea",
    privacidad: "隐私",
    terminos: "条款",
    cookies: "Cookie",
    eliminar: "删除你的账户",
    preguntas: "常见问题",
  },
  eliminarCuenta: {
    titulo: "如何删除你的 My Idea 账户",
    descripcion: "删除 My Idea 账户及所有数据的步骤，无论你能否进入应用。",
    intro: "你可以随时删除账户和数据。无需安装任何东西，在浏览器中即可完成。",
    comoTitulo: "通过应用或网站",
    pasos: [
      "用你的账户登录 myideaproject.com。",
      "打开账户中心（账户），向下滚动到“{{zona}}”。",
      "点击“{{borrarTuCuenta}}”，并输入提示的词语进行确认。如果你开启了两步验证，我们会要求你输入验证码。",
      "点击“{{borrarParaSiempre}}”。删除会立即生效，且无法撤销。",
    ],
    borraTitulo: "会删除什么",
    borra: [
      "你的账户、想法、计划、任务、笔记、日志和数字。",
      "你的点数余额和已预留的点数、你的安全数据，以及你接受条款和隐私政策的记录。",
      "你在创建账户之前写下、但尚未转入账户的想法。",
    ],
    quedaTitulo: "会保留什么",
    queda:
      "你的点数和付款历史会被匿名化：只保留金额、类型和日期，与你没有任何关联。你的电子邮箱会以加密指纹的形式保留，用于防止滥用欢迎优惠。",
    sinAccesoTitulo: "如果你无法登录",
    sinAcceso:
      "请用账户的电子邮箱发送邮件至 {{privacidad}}，主题写“删除我的账户”。我们会确认账户属于你，并在最多 30 天内将其删除。",
    sinCuentaTitulo: "如果你从未创建过账户",
    sinCuenta: "未注册账户时写下的想法，在 30 天无活动后会自动删除。",
  },
  preguntas: {
    titulo: "常见问题",
    descripcion: "关于 My Idea 最常见问题的解答：它是什么、哪些免费、点数、账户和隐私。",
    intro: "这些是大家最常问的问题。如果找不到答案，请写信到 {{contacto}}。",
    items: [
      { p: "My Idea 是什么？", r: "一款应用：它围绕你的商业或组织想法，系统地向你提问，把你的回答整理成一份将想法付诸实践的计划，并持续跟进。" },
      { p: "哪些是免费的？", r: "“清晰”阶段（整理你的想法）免费，而且不需要账户。每个世界的诊断也免费。记录进展、笔记、文档和数字都包含在内。" },
      { p: "哪些需要点数？", r: "你的计划需要 {{plan}} 点；每次跟进或重新规划的循环需要 {{seguimiento}} 点；一个世界的计划需要 {{mundo}} 点。只有在你收到承诺的内容时才会扣除；如果出现问题，则不会扣除或会退还。" },
      { p: "我需要账户吗？", r: "使用“清晰”阶段不需要。要保存你的工作并生成计划，则需要。未注册账户时写下的想法，在 30 天无活动后会自动删除。" },
      { p: "My Idea 能取代专业顾问吗？", r: "不能。它为你提供做决定的方法和条理，而不是法律、会计或任何其他专业意见。决定权在你。" },
      { p: "如何删除我的账户？", r: "在账户中心的“{{zona}}”中操作。如果无法登录，请写信到 {{privacidad}}。完整说明见“{{paginaEliminar}}”页面。" },
      { p: "我的数据会被怎样处理？", r: "你的想法属于你。我们不出售你的数据，也不将其用于广告。详情请见隐私政策。" },
      { p: "支持哪些语言？", r: "支持十一种语言。应用会用你的语言和你交流，你也可以随时更改。" },
      { p: "与我的日历同步是怎么运作的？", r: "你的日历以单向方式订阅你的日期：你在 My Idea 中做的修改会同步到你的日历，但你在日历中做的修改不会回到应用。日历应用（例如 Google 日历）每隔几个小时才会更新已订阅的日历，而不是即时更新，所以修改可能要过一段时间才会显示。" },
      { p: "有安卓应用吗？", r: "即将登陆 Google Play。在此之前，你可以用手机浏览器使用 My Idea。" },
    ],
  },
};

const ko: typeof es = {
  nav: {
    inicio: "My Idea로 돌아가기",
    privacidad: "개인정보 보호",
    terminos: "이용약관",
    cookies: "쿠키",
    eliminar: "계정 삭제",
    preguntas: "자주 묻는 질문",
  },
  eliminarCuenta: {
    titulo: "My Idea 계정을 삭제하는 방법",
    descripcion: "앱에 접속할 수 있든 없든 My Idea 계정과 모든 데이터를 삭제하는 방법이에요.",
    intro: "계정과 데이터는 언제든지 삭제할 수 있어요. 설치할 필요 없이 브라우저에서 할 수 있어요.",
    comoTitulo: "앱이나 웹사이트에서",
    pasos: [
      "계정으로 myideaproject.com에 로그인하세요.",
      "계정 센터(계정)를 열고 “{{zona}}”까지 내려가세요.",
      "“{{borrarTuCuenta}}”를 누르고 확인을 위해 안내된 단어를 입력하세요. 2단계 인증을 켜 두었다면 코드를 요청할 거예요.",
      "“{{borrarParaSiempre}}”를 누르세요. 삭제는 바로 이루어지며 되돌릴 수 없어요.",
    ],
    borraTitulo: "삭제되는 것",
    borra: [
      "계정, 아이디어, 계획, 할 일, 메모, 기록장, 숫자.",
      "크레딧 잔액과 예약된 크레딧, 보안 정보, 이용약관과 개인정보 처리방침에 동의한 기록.",
      "계정을 만들기 전에 쓴 아이디어 중 아직 계정으로 옮겨지지 않은 것.",
    ],
    quedaTitulo: "보관되는 것",
    queda:
      "크레딧과 결제 내역은 익명으로 바뀌어요. 금액, 유형, 날짜만 남고 회원님과는 전혀 연결되지 않아요. 환영 혜택의 남용을 막기 위해 이메일의 암호화된 지문은 보관돼요.",
    sinAccesoTitulo: "로그인할 수 없다면",
    sinAcceso:
      "계정 이메일로 {{privacidad}}에 제목을 “내 계정 삭제”로 해서 보내 주세요. 계정이 본인 것인지 확인한 뒤 최대 30일 안에 삭제할게요.",
    sinCuentaTitulo: "계정을 만든 적이 없다면",
    sinCuenta: "계정 없이 쓴 아이디어는 30일 동안 활동이 없으면 자동으로 삭제돼요.",
  },
  preguntas: {
    titulo: "자주 묻는 질문",
    descripcion: "My Idea에 대해 가장 많이 묻는 질문의 답이에요. My Idea가 무엇인지, 무엇이 무료인지, 크레딧, 계정, 개인정보에 관해 알려 드려요.",
    intro: "가장 많이 받는 질문이에요. 답을 찾지 못했다면 {{contacto}}로 문의해 주세요.",
    items: [
      { p: "My Idea는 무엇인가요?", r: "사업이나 조직에 대한 아이디어를 두고 체계적으로 질문하고, 답변을 실행 계획으로 정리해 주는 앱이에요. 이후의 후속 점검도 함께해요." },
      { p: "무엇이 무료인가요?", r: "명확함(아이디어 정리)은 무료이고 계정도 필요 없어요. 각 월드의 진단도 무료예요. 진행 상황, 메모, 문서, 숫자를 기록하는 것도 포함돼 있어요." },
      { p: "크레딧이 드는 것은 무엇인가요?", r: "계획은 {{plan}} 크레딧, 후속 점검이나 재설정 사이클은 한 번에 {{seguimiento}} 크레딧, 월드의 계획은 {{mundo}} 크레딧이에요. 약속한 결과를 받았을 때만 차감되고, 문제가 생기면 차감되지 않거나 환불돼요." },
      { p: "계정이 필요한가요?", r: "명확함 단계에는 필요 없어요. 작업을 저장하고 계획을 만들려면 필요해요. 계정 없이 쓴 아이디어는 30일 동안 활동이 없으면 자동으로 삭제돼요." },
      { p: "My Idea가 전문 상담가를 대신하나요?", r: "아니요. 결정을 내리기 위한 방법과 정리를 제공할 뿐, 법률, 회계 또는 다른 어떤 전문가의 자문도 아니에요. 결정은 본인이 해요." },
      { p: "계정은 어떻게 삭제하나요?", r: "계정 센터의 “{{zona}}”에서 할 수 있어요. 로그인할 수 없다면 {{privacidad}}로 연락해 주세요. 자세한 방법은 “{{paginaEliminar}}” 페이지에 있어요." },
      { p: "제 데이터는 어떻게 쓰이나요?", r: "아이디어는 회원님의 것이에요. 데이터를 판매하거나 광고에 쓰지 않아요. 자세한 내용은 개인정보 처리방침에 있어요." },
      { p: "어떤 언어로 쓸 수 있나요?", r: "11개 언어로 쓸 수 있어요. 앱이 회원님의 언어로 말하고, 언어는 언제든지 바꿀 수 있어요." },
      { p: "내 캘린더와의 동기화는 어떻게 작동하나요?", r: "캘린더는 날짜를 한 방향으로 구독해요. My Idea에서 바꾼 내용은 캘린더에 반영되지만, 캘린더에서 바꾼 내용은 앱으로 돌아오지 않아요. Google 캘린더 같은 캘린더 앱은 구독한 캘린더를 즉시가 아니라 몇 시간마다 새로 고치기 때문에, 변경 사항이 보이기까지 시간이 걸릴 수 있어요." },
      { p: "Android 앱이 있나요?", r: "곧 Google Play에 나와요. 그동안에는 휴대폰 브라우저에서 My Idea를 쓸 수 있어요." },
    ],
  },
};

const ar: typeof es = {
  nav: {
    inicio: "العودة إلى My Idea",
    privacidad: "الخصوصية",
    terminos: "الشروط",
    cookies: "ملفات تعريف الارتباط",
    eliminar: "حذف حسابكم",
    preguntas: "الأسئلة الشائعة",
  },
  eliminarCuenta: {
    titulo: "كيف تحذفون حسابكم في My Idea",
    descripcion: "تعليمات حذف حسابكم في My Idea وجميع بياناتكم، سواء أمكنكم الوصول إلى التطبيق أم لا.",
    intro: "يمكنكم حذف حسابكم وبياناتكم متى شئتم. لا حاجة إلى تثبيت أي شيء: يتم ذلك من المتصفح.",
    comoTitulo: "من التطبيق أو الموقع",
    pasos: [
      "سجّلوا الدخول إلى myideaproject.com بحسابكم.",
      "افتحوا مركز الحساب (الحساب) وانزلوا حتى «{{zona}}».",
      "اضغطوا «{{borrarTuCuenta}}» واكتبوا الكلمة المطلوبة للتأكيد. إذا كان التحقق بخطوتين مفعّلًا، فسنطلب منكم الرمز.",
      "اضغطوا «{{borrarParaSiempre}}». يتم الحذف فورًا ولا يمكن التراجع عنه.",
    ],
    borraTitulo: "ما الذي يُحذف",
    borra: [
      "حسابكم وأفكاركم وخططكم ومهامكم وملاحظاتكم وسجلّ رحلتكم وأرقامكم.",
      "رصيدكم وحجوزاتكم وبيانات الأمان الخاصة بكم وسجلّ موافقتكم على الشروط وسياسة الخصوصية.",
      "الأفكار التي كتبتموها قبل إنشاء حسابكم، إن لم تكن قد نُقلت إليه بعد.",
    ],
    quedaTitulo: "ما الذي يُحتفظ به",
    queda:
      "يصبح سجلّ رصيدكم ومدفوعاتكم مجهول الهوية: يبقى فقط المبلغ ونوعه والتاريخ، دون أي صلة بكم. ونحتفظ ببصمة مشفّرة لبريدكم الإلكتروني لمنع إساءة استخدام عروض الترحيب.",
    sinAccesoTitulo: "إذا لم تتمكنوا من تسجيل الدخول",
    sinAcceso:
      "راسلونا من البريد الإلكتروني لحسابكم على {{privacidad}} بعنوان «حذف حسابي». سنتحقق من أن الحساب لكم ونحذفه خلال 30 يومًا على الأكثر.",
    sinCuentaTitulo: "إذا لم تنشئوا حسابًا من قبل",
    sinCuenta: "تُحذف الأفكار المكتوبة دون حساب تلقائيًا بعد 30 يومًا دون نشاط.",
  },
  preguntas: {
    titulo: "الأسئلة الشائعة",
    descripcion: "إجابات عن أكثر الأسئلة شيوعًا حول My Idea: ما هو، وما المجاني، والرصيد، والحساب، والخصوصية.",
    intro: "هذه أكثر الأسئلة التي تصلنا. إذا لم تجدوا إجابتكم، فراسلونا على {{contacto}}.",
    items: [
      { p: "ما هو My Idea؟", r: "تطبيق يطرح عليكم أسئلة منهجية حول فكرة مشروعكم أو مؤسستكم، ويرتّب إجاباتكم في خطة لوضعها موضع التنفيذ، مع متابعتها." },
      { p: "ما المجاني؟", r: "الوضوح (ترتيب فكرتكم) مجاني ولا يحتاج إلى حساب. وتشخيص كل عالم مجاني أيضًا. أما تسجيل تقدمكم وملاحظاتكم ومستنداتكم وأرقامكم فمشمول." },
      { p: "ما الذي يستهلك الرصيد؟", r: "النقاط المطلوبة لخطتكم: {{plan}}؛ ولكل دورة متابعة أو إعادة توجيه: {{seguimiento}}؛ ولخطة عالم: {{mundo}}. لا تُخصم إلا عندما تتلقّون ما وُعدتم به؛ وإذا حدث خطأ، فلا يُخصم شيء أو تُعاد إليكم." },
      { p: "هل أحتاج إلى حساب؟", r: "لا تحتاجون إليه في مرحلة الوضوح، لكنكم تحتاجون إليه لحفظ عملكم وإنشاء خطتكم. تُحذف الأفكار المكتوبة دون حساب تلقائيًا بعد 30 يومًا من عدم النشاط." },
      { p: "هل يحل My Idea محل مستشار مهني؟", r: "لا. فهو يقدّم لكم المنهج والترتيب لاتخاذ القرار، لا استشارة قانونية أو محاسبية أو من أي مهني آخر. القرارات قراراتكم." },
      { p: "كيف أحذف حسابي؟", r: "من مركز الحساب، في «{{zona}}». إذا لم تتمكنوا من تسجيل الدخول، فراسلوا {{privacidad}}. التعليمات الكاملة في صفحة «{{paginaEliminar}}»." },
      { p: "ماذا يحدث لبياناتي؟", r: "أفكاركم ملك لكم. لا نبيع بياناتكم ولا نستخدمها للإعلان. كل التفاصيل في سياسة الخصوصية." },
      { p: "بأي لغات يعمل؟", r: "بإحدى عشرة لغة. يخاطبكم التطبيق بلغتكم ويمكنكم تغييرها متى شئتم." },
      { p: "كيف تعمل المزامنة مع تقويمي؟", r: "يشترك تقويمكم في مواعيدكم في اتجاه واحد: ما تغيّرونه في My Idea يصل إلى تقويمكم، أما ما تغيّرونه في التقويم فلا يعود إلى التطبيق. تحدّث تطبيقات التقويم، مثل تقويم Google، التقاويم المشترَك فيها كل بضع ساعات وليس فورًا، لذلك قد يستغرق ظهور التغيير بعض الوقت." },
      { p: "هل يوجد تطبيق لأندرويد؟", r: "قريبًا على Google Play. وحتى ذلك الحين، يمكنكم استخدام My Idea من متصفح هاتفكم." },
    ],
  },
};

const hi: typeof es = {
  nav: {
    inicio: "My Idea पर वापस जाएँ",
    privacidad: "गोपनीयता",
    terminos: "शर्तें",
    cookies: "कुकीज़",
    eliminar: "अपना खाता हटाएँ",
    preguntas: "अक्सर पूछे जाने वाले सवाल",
  },
  eliminarCuenta: {
    titulo: "अपना My Idea खाता कैसे हटाएँ",
    descripcion: "ऐप तक पहुँच हो या न हो, अपना My Idea खाता और अपना सारा डेटा हटाने के निर्देश।",
    intro: "आप जब चाहें अपना खाता और अपना डेटा हटा सकते हैं। कुछ भी इंस्टॉल करने की ज़रूरत नहीं: यह ब्राउज़र से होता है।",
    comoTitulo: "ऐप या वेबसाइट से",
    pasos: [
      "अपने खाते से myideaproject.com में साइन इन करें।",
      "खाता केंद्र (खाता) खोलें और नीचे “{{zona}}” तक जाएँ।",
      "“{{borrarTuCuenta}}” पर टैप करें और पुष्टि के लिए माँगा गया शब्द लिखें। अगर आपने दो-चरणीय सत्यापन चालू किया है, तो हम आपसे आपका कोड माँगेंगे।",
      "“{{borrarParaSiempre}}” पर टैप करें। खाता तुरंत हट जाता है और इसे वापस नहीं लाया जा सकता।",
    ],
    borraTitulo: "क्या हटता है",
    borra: [
      "आपका खाता, आपके विचार, आपकी योजनाएँ, आपके काम, आपके नोट्स, आपकी लॉगबुक और आपके आंकड़े।",
      "आपका क्रेडिट बैलेंस और आरक्षण, आपका सुरक्षा डेटा, और शर्तों व गोपनीयता नीति को स्वीकार करने का आपका रिकॉर्ड।",
      "खाता बनाने से पहले लिखे गए आपके विचार, अगर वे अभी तक उसमें नहीं गए थे।",
    ],
    quedaTitulo: "क्या रखा जाता है",
    queda:
      "आपके क्रेडिट और भुगतान का इतिहास गुमनाम हो जाता है: सिर्फ़ राशि, उसका प्रकार और तारीख बचती है, आपसे कोई संबंध नहीं रहता। स्वागत ऑफ़र के दुरुपयोग को रोकने के लिए आपके ईमेल का एन्क्रिप्टेड फ़िंगरप्रिंट रखा जाता है।",
    sinAccesoTitulo: "अगर आप साइन इन नहीं कर पा रहे हैं",
    sinAcceso:
      "अपने खाते वाले ईमेल से {{privacidad}} पर “मेरा खाता हटाएँ” विषय के साथ लिखें। हम पुष्टि करेंगे कि खाता आपका है और ज़्यादा से ज़्यादा 30 दिनों में उसे हटा देंगे।",
    sinCuentaTitulo: "अगर आपने कभी खाता नहीं बनाया",
    sinCuenta: "बिना खाते के लिखे गए विचार 30 दिनों तक कोई गतिविधि न होने पर अपने आप हट जाते हैं।",
  },
  preguntas: {
    titulo: "अक्सर पूछे जाने वाले सवाल",
    descripcion: "My Idea के बारे में सबसे आम सवालों के जवाब: यह क्या है, क्या मुफ़्त है, क्रेडिट, खाता और गोपनीयता।",
    intro: "हमसे सबसे ज़्यादा यही पूछा जाता है। अगर आपको अपना जवाब न मिले, तो हमें {{contacto}} पर लिखें।",
    items: [
      { p: "My Idea क्या है?", r: "एक ऐप जो आपके व्यवसाय या संगठन के विचार पर आपसे व्यवस्थित तरीके से सवाल पूछता है और आपके जवाबों को उसे अमल में लाने की योजना में बदलता है, साथ में फ़ॉलो-अप भी देता है।" },
      { p: "क्या मुफ़्त है?", r: "आपकी स्पष्टता (अपने विचार को व्यवस्थित करना) मुफ़्त है और इसके लिए खाते की ज़रूरत नहीं। हर दुनिया का आकलन भी मुफ़्त है। अपनी प्रगति, नोट्स, दस्तावेज़ और आंकड़े दर्ज करना शामिल है।" },
      { p: "किसमें क्रेडिट लगते हैं?", r: "आपकी योजना में {{plan}} क्रेडिट लगते हैं; हर फ़ॉलो-अप या नई दिशा के चक्र में {{seguimiento}}; किसी दुनिया की योजना में {{mundo}}। ये तभी काटे जाते हैं जब आपको वादा किया गया नतीजा मिलता है; अगर कुछ गड़बड़ होती है, तो कुछ नहीं काटा जाता या क्रेडिट लौटा दिए जाते हैं।" },
      { p: "क्या मुझे खाते की ज़रूरत है?", r: "स्पष्टता के लिए नहीं। अपना काम सहेजने और अपनी योजना बनाने के लिए हाँ। बिना खाते के लिखे गए विचार 30 दिनों तक कोई गतिविधि न होने पर अपने आप हट जाते हैं।" },
      { p: "क्या My Idea किसी पेशेवर सलाहकार का विकल्प है?", r: "नहीं। यह आपको फ़ैसला लेने के लिए तरीका और व्यवस्था देता है, कानूनी, लेखा या किसी और पेशेवर की सलाह नहीं। फ़ैसले आपके हैं।" },
      { p: "मैं अपना खाता कैसे हटाऊँ?", r: "खाता केंद्र में, “{{zona}}” से। अगर आप साइन इन नहीं कर पा रहे हैं, तो {{privacidad}} पर लिखें। पूरे निर्देश “{{paginaEliminar}}” पेज पर हैं।" },
      { p: "मेरे डेटा का क्या होता है?", r: "आपके विचार आपके हैं। हम आपका डेटा नहीं बेचते और न ही उसे विज्ञापन के लिए इस्तेमाल करते हैं। पूरी जानकारी गोपनीयता नीति में है।" },
      { p: "यह किन भाषाओं में काम करता है?", r: "ग्यारह भाषाओं में। ऐप आपकी भाषा में बात करता है और आप उसे जब चाहें बदल सकते हैं।" },
      { p: "मेरे कैलेंडर के साथ सिंक कैसे काम करता है?", r: "आपका कैलेंडर आपकी तारीख़ों को एक ही दिशा में सब्सक्राइब करता है: My Idea में आप जो बदलते हैं वह आपके कैलेंडर तक पहुँचता है, लेकिन कैलेंडर में किया गया बदलाव ऐप में वापस नहीं आता। Google Calendar जैसे कैलेंडर ऐप सब्सक्राइब किए गए कैलेंडर को तुरंत नहीं, बल्कि हर कुछ घंटों में अपडेट करते हैं, इसलिए किसी बदलाव को दिखने में समय लग सकता है।" },
      { p: "क्या Android ऐप है?", r: "जल्द ही Google Play पर। तब तक आप अपने फ़ोन के ब्राउज़र से My Idea इस्तेमाल कर सकते हैं।" },
    ],
  },
};

export const PAGINAS_AYUDA: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
