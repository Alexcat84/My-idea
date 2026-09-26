/** Los correos de la cuenta que manda Supabase Auth por el Send Email Hook
 * (i18n F6, decisión D4): confirmar el registro, invitación, enlace para
 * entrar, recuperar la contraseña, cambio de correo, código de confirmación y
 * los avisos de seguridad. Los arma lib/correosAuth.ts y los manda
 * app/api/auth/hook-correo por Resend, en el idioma guardado de la persona. */
import type { PorIdioma } from "../config";

const es = {
  comun: {
    siBotonNoAbre: "Si el botón no abre, copia este enlace en tu navegador:",
    oEscribeCodigo: "También puedes escribir este código: {{codigo}}",
    firma: "My Idea",
  },
  registro: {
    asunto: "Confirma tu correo en My Idea",
    titulo: "Confirma tu correo",
    cuerpo: "Ya casi está. Confirma tu correo y tu cuenta de My Idea queda lista para seguir con tu idea.",
    boton: "Confirmar mi correo",
    nota: "Si no creaste una cuenta en My Idea, ignora este correo.",
  },
  invitacion: {
    asunto: "Te invitaron a My Idea",
    titulo: "Tienes una invitación",
    cuerpo: "Te invitaron a My Idea. Acepta la invitación para crear tu cuenta y empezar con tu idea.",
    boton: "Aceptar la invitación",
    nota: "Si no esperabas esta invitación, ignora este correo.",
  },
  enlaceEntrar: {
    asunto: "Tu enlace para entrar a My Idea",
    titulo: "Entra a My Idea",
    cuerpo: "Usa este enlace para entrar a tu cuenta. Sirve una sola vez y vence pronto.",
    boton: "Entrar a My Idea",
    nota: "Si no pediste entrar, ignora este correo: nadie entra sin este enlace.",
  },
  recuperar: {
    asunto: "Elige una contraseña nueva para My Idea",
    titulo: "Elige una contraseña nueva",
    cuerpo: "Pediste cambiar tu contraseña. Abre este enlace y elige una nueva.",
    boton: "Elegir contraseña nueva",
    nota: "Si no lo pediste tú, ignora este correo: tu contraseña sigue igual.",
  },
  cambioCorreoActual: {
    asunto: "Confirma el cambio de correo en My Idea",
    titulo: "Confirma el cambio de correo",
    cuerpo: "Pediste cambiar el correo de tu cuenta de {{actual}} a {{nuevo}}. Confírmalo desde aquí.",
    boton: "Confirmar el cambio",
    nota: "Si no lo pediste tú, ignora este correo: tu cuenta sigue con el mismo correo.",
  },
  cambioCorreoNuevo: {
    asunto: "Confirma tu correo nuevo en My Idea",
    titulo: "Confirma tu correo nuevo",
    cuerpo: "Pediste usar {{nuevo}} como el correo de tu cuenta de My Idea. Confírmalo desde aquí.",
    boton: "Confirmar mi correo nuevo",
    nota: "Si no lo pediste tú, ignora este correo: nada cambia sin tu confirmación.",
  },
  reautenticacion: {
    asunto: "Tu código de confirmación de My Idea",
    titulo: "Confirma que eres tú",
    cuerpo: "Escribe este código en My Idea para confirmar que eres tú:",
    nota: "Si no fuiste tú, ignora este correo: nadie hace cambios sin este código.",
  },
  avisos: {
    notaSeguridad: "Si no fuiste tú, pide una contraseña nueva desde la pantalla de entrada de My Idea cuanto antes.",
    contrasenaCambiada: {
      asunto: "Tu contraseña de My Idea cambió",
      cuerpo: "La contraseña de tu cuenta de My Idea acaba de cambiar.",
    },
    correoCambiado: {
      asunto: "El correo de tu cuenta de My Idea cambió",
      cuerpo: "El correo de tu cuenta de My Idea acaba de cambiar. Este aviso llega a tu correo anterior.",
    },
    telefonoCambiado: {
      asunto: "El teléfono de tu cuenta de My Idea cambió",
      cuerpo: "El teléfono de tu cuenta de My Idea acaba de cambiar.",
    },
    accesoVinculado: {
      asunto: "Hay una forma nueva de entrar a tu cuenta de My Idea",
      cuerpo: "Se agregó una forma nueva de entrar a tu cuenta de My Idea.",
    },
    accesoDesvinculado: {
      asunto: "Se quitó una forma de entrar a tu cuenta de My Idea",
      cuerpo: "Se quitó una de las formas de entrar a tu cuenta de My Idea.",
    },
    verificacionAgregada: {
      asunto: "Se agregó un método de verificación en dos pasos",
      cuerpo: "Se agregó un método de verificación en dos pasos a tu cuenta de My Idea.",
    },
    verificacionQuitada: {
      asunto: "Se quitó un método de verificación en dos pasos",
      cuerpo: "Se quitó un método de verificación en dos pasos de tu cuenta de My Idea.",
    },
  },
};

const en: typeof es = {
  comun: {
    siBotonNoAbre: "If the button doesn't open, copy this link into your browser:",
    oEscribeCodigo: "You can also type this code: {{codigo}}",
    firma: "My Idea",
  },
  registro: {
    asunto: "Confirm your email for My Idea",
    titulo: "Confirm your email",
    cuerpo: "Almost there. Confirm your email and your My Idea account will be ready for you to keep going with your idea.",
    boton: "Confirm my email",
    nota: "If you didn't create a My Idea account, ignore this email.",
  },
  invitacion: {
    asunto: "You've been invited to My Idea",
    titulo: "You have an invitation",
    cuerpo: "You've been invited to My Idea. Accept the invitation to create your account and get started with your idea.",
    boton: "Accept the invitation",
    nota: "If you weren't expecting this invitation, ignore this email.",
  },
  enlaceEntrar: {
    asunto: "Your link to sign in to My Idea",
    titulo: "Sign in to My Idea",
    cuerpo: "Use this link to sign in to your account. It works only once and expires soon.",
    boton: "Sign in to My Idea",
    nota: "If you didn't ask to sign in, ignore this email: no one gets in without this link.",
  },
  recuperar: {
    asunto: "Choose a new password for My Idea",
    titulo: "Choose a new password",
    cuerpo: "You asked to change your password. Open this link and choose a new one.",
    boton: "Choose a new password",
    nota: "If you didn't ask for this, ignore this email: your password stays the same.",
  },
  cambioCorreoActual: {
    asunto: "Confirm your email change on My Idea",
    titulo: "Confirm your email change",
    cuerpo: "You asked to change your account email from {{actual}} to {{nuevo}}. Confirm it here.",
    boton: "Confirm the change",
    nota: "If you didn't ask for this, ignore this email: your account keeps the same email.",
  },
  cambioCorreoNuevo: {
    asunto: "Confirm your new email for My Idea",
    titulo: "Confirm your new email",
    cuerpo: "You asked to use {{nuevo}} as the email for your My Idea account. Confirm it here.",
    boton: "Confirm my new email",
    nota: "If you didn't ask for this, ignore this email: nothing changes without your confirmation.",
  },
  reautenticacion: {
    asunto: "Your My Idea confirmation code",
    titulo: "Confirm it's you",
    cuerpo: "Type this code in My Idea to confirm it's you:",
    nota: "If this wasn't you, ignore this email: no one can make changes without this code.",
  },
  avisos: {
    notaSeguridad: "If this wasn't you, request a new password from the My Idea sign-in screen right away.",
    contrasenaCambiada: {
      asunto: "Your My Idea password changed",
      cuerpo: "The password for your My Idea account was just changed.",
    },
    correoCambiado: {
      asunto: "Your My Idea account email changed",
      cuerpo: "The email for your My Idea account was just changed. This notice goes to your previous email.",
    },
    telefonoCambiado: {
      asunto: "Your My Idea account phone number changed",
      cuerpo: "The phone number for your My Idea account was just changed.",
    },
    accesoVinculado: {
      asunto: "There's a new way to sign in to your My Idea account",
      cuerpo: "A new way to sign in was added to your My Idea account.",
    },
    accesoDesvinculado: {
      asunto: "A way to sign in was removed from your My Idea account",
      cuerpo: "One of the ways to sign in to your My Idea account was removed.",
    },
    verificacionAgregada: {
      asunto: "A two-step verification method was added",
      cuerpo: "A two-step verification method was added to your My Idea account.",
    },
    verificacionQuitada: {
      asunto: "A two-step verification method was removed",
      cuerpo: "A two-step verification method was removed from your My Idea account.",
    },
  },
};

const pt: typeof es = {
  comun: {
    siBotonNoAbre: "Se o botão não abrir, copie este link no seu navegador:",
    oEscribeCodigo: "Você também pode digitar este código: {{codigo}}",
    firma: "My Idea",
  },
  registro: {
    asunto: "Confirme seu e-mail no My Idea",
    titulo: "Confirme seu e-mail",
    cuerpo: "Falta pouco. Confirme seu e-mail e sua conta do My Idea fica pronta para você seguir com sua ideia.",
    boton: "Confirmar meu e-mail",
    nota: "Se você não criou uma conta no My Idea, ignore este e-mail.",
  },
  invitacion: {
    asunto: "Você recebeu um convite para o My Idea",
    titulo: "Você tem um convite",
    cuerpo: "Você recebeu um convite para o My Idea. Aceite o convite para criar sua conta e começar com sua ideia.",
    boton: "Aceitar o convite",
    nota: "Se você não esperava este convite, ignore este e-mail.",
  },
  enlaceEntrar: {
    asunto: "Seu link para entrar no My Idea",
    titulo: "Entre no My Idea",
    cuerpo: "Use este link para entrar na sua conta. Ele funciona uma única vez e expira em breve.",
    boton: "Entrar no My Idea",
    nota: "Se você não pediu para entrar, ignore este e-mail: ninguém entra sem este link.",
  },
  recuperar: {
    asunto: "Escolha uma nova senha para o My Idea",
    titulo: "Escolha uma nova senha",
    cuerpo: "Você pediu para trocar sua senha. Abra este link e escolha uma nova.",
    boton: "Escolher nova senha",
    nota: "Se não foi você que pediu, ignore este e-mail: sua senha continua a mesma.",
  },
  cambioCorreoActual: {
    asunto: "Confirme a troca de e-mail no My Idea",
    titulo: "Confirme a troca de e-mail",
    cuerpo: "Você pediu para trocar o e-mail da sua conta de {{actual}} para {{nuevo}}. Confirme aqui.",
    boton: "Confirmar a troca",
    nota: "Se não foi você que pediu, ignore este e-mail: sua conta continua com o mesmo e-mail.",
  },
  cambioCorreoNuevo: {
    asunto: "Confirme seu novo e-mail no My Idea",
    titulo: "Confirme seu novo e-mail",
    cuerpo: "Você pediu para usar {{nuevo}} como o e-mail da sua conta do My Idea. Confirme aqui.",
    boton: "Confirmar meu novo e-mail",
    nota: "Se não foi você que pediu, ignore este e-mail: nada muda sem a sua confirmação.",
  },
  reautenticacion: {
    asunto: "Seu código de confirmação do My Idea",
    titulo: "Confirme que é você",
    cuerpo: "Digite este código no My Idea para confirmar que é você:",
    nota: "Se não foi você, ignore este e-mail: ninguém faz alterações sem este código.",
  },
  avisos: {
    notaSeguridad: "Se não foi você, peça uma nova senha na tela de entrada do My Idea o quanto antes.",
    contrasenaCambiada: {
      asunto: "Sua senha do My Idea foi alterada",
      cuerpo: "A senha da sua conta do My Idea acabou de ser alterada.",
    },
    correoCambiado: {
      asunto: "O e-mail da sua conta do My Idea foi alterado",
      cuerpo: "O e-mail da sua conta do My Idea acabou de ser alterado. Este aviso chega ao seu e-mail anterior.",
    },
    telefonoCambiado: {
      asunto: "O telefone da sua conta do My Idea foi alterado",
      cuerpo: "O telefone da sua conta do My Idea acabou de ser alterado.",
    },
    accesoVinculado: {
      asunto: "Há uma nova forma de entrar na sua conta do My Idea",
      cuerpo: "Uma nova forma de entrar foi adicionada à sua conta do My Idea.",
    },
    accesoDesvinculado: {
      asunto: "Uma forma de entrar foi removida da sua conta do My Idea",
      cuerpo: "Uma das formas de entrar na sua conta do My Idea foi removida.",
    },
    verificacionAgregada: {
      asunto: "Um método de verificação em duas etapas foi adicionado",
      cuerpo: "Um método de verificação em duas etapas foi adicionado à sua conta do My Idea.",
    },
    verificacionQuitada: {
      asunto: "Um método de verificação em duas etapas foi removido",
      cuerpo: "Um método de verificação em duas etapas foi removido da sua conta do My Idea.",
    },
  },
};

const fr: typeof es = {
  comun: {
    siBotonNoAbre: "Si le bouton ne s'ouvre pas, copie ce lien dans ton navigateur :",
    oEscribeCodigo: "Tu peux aussi écrire ce code : {{codigo}}",
    firma: "My Idea",
  },
  registro: {
    asunto: "Confirme ton courriel pour My Idea",
    titulo: "Confirme ton courriel",
    cuerpo: "C'est presque fait. Confirme ton courriel et ton compte My Idea sera prêt pour continuer avec ton idée.",
    boton: "Confirmer mon courriel",
    nota: "Si tu n'as pas créé de compte My Idea, ignore ce courriel.",
  },
  invitacion: {
    asunto: "Tu as reçu une invitation à My Idea",
    titulo: "Tu as une invitation",
    cuerpo: "Tu as reçu une invitation à My Idea. Accepte-la pour créer ton compte et commencer avec ton idée.",
    boton: "Accepter l'invitation",
    nota: "Si tu ne t'attendais pas à cette invitation, ignore ce courriel.",
  },
  enlaceEntrar: {
    asunto: "Ton lien pour te connecter à My Idea",
    titulo: "Connecte-toi à My Idea",
    cuerpo: "Utilise ce lien pour te connecter à ton compte. Il ne fonctionne qu'une fois et expire bientôt.",
    boton: "Me connecter à My Idea",
    nota: "Si tu n'as pas demandé à te connecter, ignore ce courriel : personne n'entre sans ce lien.",
  },
  recuperar: {
    asunto: "Choisis un nouveau mot de passe pour My Idea",
    titulo: "Choisis un nouveau mot de passe",
    cuerpo: "Tu as demandé à changer ton mot de passe. Ouvre ce lien et choisis-en un nouveau.",
    boton: "Choisir un nouveau mot de passe",
    nota: "Si tu n'as rien demandé, ignore ce courriel : ton mot de passe reste le même.",
  },
  cambioCorreoActual: {
    asunto: "Confirme le changement de courriel sur My Idea",
    titulo: "Confirme le changement de courriel",
    cuerpo: "Tu as demandé à remplacer le courriel de ton compte, {{actual}}, par {{nuevo}}. Confirme-le ici.",
    boton: "Confirmer le changement",
    nota: "Si tu n'as rien demandé, ignore ce courriel : ton compte garde le même courriel.",
  },
  cambioCorreoNuevo: {
    asunto: "Confirme ton nouveau courriel pour My Idea",
    titulo: "Confirme ton nouveau courriel",
    cuerpo: "Tu as demandé à utiliser {{nuevo}} comme courriel de ton compte My Idea. Confirme-le ici.",
    boton: "Confirmer mon nouveau courriel",
    nota: "Si tu n'as rien demandé, ignore ce courriel : rien ne change sans ta confirmation.",
  },
  reautenticacion: {
    asunto: "Ton code de confirmation My Idea",
    titulo: "Confirme que c'est bien toi",
    cuerpo: "Écris ce code dans My Idea pour confirmer que c'est bien toi :",
    nota: "Si ce n'était pas toi, ignore ce courriel : personne ne fait de changement sans ce code.",
  },
  avisos: {
    notaSeguridad: "Si ce n'était pas toi, demande sans tarder un nouveau mot de passe depuis l'écran de connexion de My Idea.",
    contrasenaCambiada: {
      asunto: "Ton mot de passe My Idea a changé",
      cuerpo: "Le mot de passe de ton compte My Idea vient de changer.",
    },
    correoCambiado: {
      asunto: "Le courriel de ton compte My Idea a changé",
      cuerpo: "Le courriel de ton compte My Idea vient de changer. Cet avis est envoyé à ton ancien courriel.",
    },
    telefonoCambiado: {
      asunto: "Le numéro de téléphone de ton compte My Idea a changé",
      cuerpo: "Le numéro de téléphone de ton compte My Idea vient de changer.",
    },
    accesoVinculado: {
      asunto: "Une nouvelle façon de te connecter à ton compte My Idea",
      cuerpo: "Une nouvelle façon de te connecter a été ajoutée à ton compte My Idea.",
    },
    accesoDesvinculado: {
      asunto: "Une façon de te connecter a été retirée de ton compte My Idea",
      cuerpo: "L'une des façons de te connecter à ton compte My Idea a été retirée.",
    },
    verificacionAgregada: {
      asunto: "Une méthode de vérification en deux étapes a été ajoutée",
      cuerpo: "Une méthode de vérification en deux étapes a été ajoutée à ton compte My Idea.",
    },
    verificacionQuitada: {
      asunto: "Une méthode de vérification en deux étapes a été retirée",
      cuerpo: "Une méthode de vérification en deux étapes a été retirée de ton compte My Idea.",
    },
  },
};

const de: typeof es = {
  comun: {
    siBotonNoAbre: "Wenn sich der Button nicht öffnet, kopiere diesen Link in deinen Browser:",
    oEscribeCodigo: "Du kannst auch diesen Code eingeben: {{codigo}}",
    firma: "My Idea",
  },
  registro: {
    asunto: "Bestätige deine E-Mail-Adresse für My Idea",
    titulo: "Bestätige deine E-Mail-Adresse",
    cuerpo: "Fast geschafft. Bestätige deine E-Mail-Adresse, dann ist dein Konto bei My Idea bereit und du kannst mit deiner Idee weitermachen.",
    boton: "E-Mail-Adresse bestätigen",
    nota: "Wenn du kein Konto bei My Idea erstellt hast, ignoriere diese E-Mail.",
  },
  invitacion: {
    asunto: "Du wurdest zu My Idea eingeladen",
    titulo: "Du hast eine Einladung",
    cuerpo: "Du wurdest zu My Idea eingeladen. Nimm die Einladung an, um dein Konto zu erstellen und mit deiner Idee loszulegen.",
    boton: "Einladung annehmen",
    nota: "Wenn du diese Einladung nicht erwartet hast, ignoriere diese E-Mail.",
  },
  enlaceEntrar: {
    asunto: "Dein Link zum Anmelden bei My Idea",
    titulo: "Bei My Idea anmelden",
    cuerpo: "Mit diesem Link meldest du dich bei deinem Konto an. Er funktioniert nur einmal und läuft bald ab.",
    boton: "Bei My Idea anmelden",
    nota: "Wenn du dich nicht anmelden wolltest, ignoriere diese E-Mail: Ohne diesen Link kommt niemand hinein.",
  },
  recuperar: {
    asunto: "Wähle ein neues Passwort für My Idea",
    titulo: "Wähle ein neues Passwort",
    cuerpo: "Du wolltest dein Passwort ändern. Öffne diesen Link und wähle ein neues.",
    boton: "Neues Passwort wählen",
    nota: "Wenn du das nicht angefordert hast, ignoriere diese E-Mail: Dein Passwort bleibt, wie es ist.",
  },
  cambioCorreoActual: {
    asunto: "Bestätige die Änderung deiner E-Mail-Adresse bei My Idea",
    titulo: "Bestätige die Änderung deiner E-Mail-Adresse",
    cuerpo: "Du möchtest die E-Mail-Adresse deines Kontos von {{actual}} auf {{nuevo}} ändern. Bestätige es hier.",
    boton: "Änderung bestätigen",
    nota: "Wenn du das nicht angefordert hast, ignoriere diese E-Mail: Dein Konto behält dieselbe E-Mail-Adresse.",
  },
  cambioCorreoNuevo: {
    asunto: "Bestätige deine neue E-Mail-Adresse für My Idea",
    titulo: "Bestätige deine neue E-Mail-Adresse",
    cuerpo: "Du möchtest {{nuevo}} als E-Mail-Adresse für dein Konto bei My Idea verwenden. Bestätige es hier.",
    boton: "Neue E-Mail-Adresse bestätigen",
    nota: "Wenn du das nicht angefordert hast, ignoriere diese E-Mail: Ohne deine Bestätigung ändert sich nichts.",
  },
  reautenticacion: {
    asunto: "Dein Bestätigungscode für My Idea",
    titulo: "Bestätige, dass du es bist",
    cuerpo: "Gib diesen Code in My Idea ein, um zu bestätigen, dass du es bist:",
    nota: "Wenn du das nicht warst, ignoriere diese E-Mail: Ohne diesen Code kann niemand etwas ändern.",
  },
  avisos: {
    notaSeguridad: "Wenn du das nicht warst, fordere sofort über den Anmeldebildschirm von My Idea ein neues Passwort an.",
    contrasenaCambiada: {
      asunto: "Dein Passwort bei My Idea wurde geändert",
      cuerpo: "Das Passwort deines Kontos bei My Idea wurde gerade geändert.",
    },
    correoCambiado: {
      asunto: "Die E-Mail-Adresse deines Kontos bei My Idea wurde geändert",
      cuerpo: "Die E-Mail-Adresse deines Kontos bei My Idea wurde gerade geändert. Dieser Hinweis geht an deine bisherige Adresse.",
    },
    telefonoCambiado: {
      asunto: "Die Telefonnummer deines Kontos bei My Idea wurde geändert",
      cuerpo: "Die Telefonnummer deines Kontos bei My Idea wurde gerade geändert.",
    },
    accesoVinculado: {
      asunto: "Neue Anmeldemöglichkeit für dein Konto bei My Idea",
      cuerpo: "Deinem Konto bei My Idea wurde eine neue Anmeldemöglichkeit hinzugefügt.",
    },
    accesoDesvinculado: {
      asunto: "Eine Anmeldemöglichkeit wurde aus deinem Konto bei My Idea entfernt",
      cuerpo: "Eine der Anmeldemöglichkeiten deines Kontos bei My Idea wurde entfernt.",
    },
    verificacionAgregada: {
      asunto: "Eine Methode für die Bestätigung in zwei Schritten wurde hinzugefügt",
      cuerpo: "Deinem Konto bei My Idea wurde eine Methode für die Bestätigung in zwei Schritten hinzugefügt.",
    },
    verificacionQuitada: {
      asunto: "Eine Methode für die Bestätigung in zwei Schritten wurde entfernt",
      cuerpo: "Aus deinem Konto bei My Idea wurde eine Methode für die Bestätigung in zwei Schritten entfernt.",
    },
  },
};

const it: typeof es = {
  comun: {
    siBotonNoAbre: "Se il pulsante non si apre, copia questo link nel tuo browser:",
    oEscribeCodigo: "Puoi anche scrivere questo codice: {{codigo}}",
    firma: "My Idea",
  },
  registro: {
    asunto: "Conferma la tua email su My Idea",
    titulo: "Conferma la tua email",
    cuerpo: "Ci siamo quasi. Conferma la tua email e il tuo account My Idea sarà pronto per andare avanti con la tua idea.",
    boton: "Conferma la mia email",
    nota: "Se non hai creato un account su My Idea, ignora questa email.",
  },
  invitacion: {
    asunto: "Hai ricevuto un invito a My Idea",
    titulo: "Hai un invito",
    cuerpo: "Hai ricevuto un invito a My Idea. Accettalo per creare il tuo account e iniziare con la tua idea.",
    boton: "Accetta l'invito",
    nota: "Se non ti aspettavi questo invito, ignora questa email.",
  },
  enlaceEntrar: {
    asunto: "Il tuo link per accedere a My Idea",
    titulo: "Accedi a My Idea",
    cuerpo: "Usa questo link per accedere al tuo account. Funziona una sola volta e scade presto.",
    boton: "Accedi a My Idea",
    nota: "Se non hai chiesto di accedere, ignora questa email: senza questo link non entra nessuno.",
  },
  recuperar: {
    asunto: "Scegli una nuova password per My Idea",
    titulo: "Scegli una nuova password",
    cuerpo: "Hai chiesto di cambiare la tua password. Apri questo link e scegline una nuova.",
    boton: "Scegli una nuova password",
    nota: "Se non l'hai chiesto tu, ignora questa email: la tua password resta la stessa.",
  },
  cambioCorreoActual: {
    asunto: "Conferma il cambio di email su My Idea",
    titulo: "Conferma il cambio di email",
    cuerpo: "Hai chiesto di cambiare l'email del tuo account da {{actual}} a {{nuevo}}. Confermalo da qui.",
    boton: "Conferma il cambio",
    nota: "Se non l'hai chiesto tu, ignora questa email: il tuo account mantiene la stessa email.",
  },
  cambioCorreoNuevo: {
    asunto: "Conferma la tua nuova email su My Idea",
    titulo: "Conferma la tua nuova email",
    cuerpo: "Hai chiesto di usare {{nuevo}} come email del tuo account My Idea. Confermalo da qui.",
    boton: "Conferma la mia nuova email",
    nota: "Se non l'hai chiesto tu, ignora questa email: senza la tua conferma non cambia nulla.",
  },
  reautenticacion: {
    asunto: "Il tuo codice di conferma di My Idea",
    titulo: "Conferma che sei tu",
    cuerpo: "Scrivi questo codice in My Idea per confermare che sei tu:",
    nota: "Se non l'hai chiesto tu, ignora questa email: senza questo codice nessuno può fare modifiche.",
  },
  avisos: {
    notaSeguridad: "Se non riconosci questa modifica, chiedi subito una nuova password dalla schermata di accesso di My Idea.",
    contrasenaCambiada: {
      asunto: "La tua password di My Idea è cambiata",
      cuerpo: "La password del tuo account My Idea è appena cambiata.",
    },
    correoCambiado: {
      asunto: "L'email del tuo account My Idea è cambiata",
      cuerpo: "L'email del tuo account My Idea è appena cambiata. Questo avviso arriva al tuo indirizzo precedente.",
    },
    telefonoCambiado: {
      asunto: "Il numero di telefono del tuo account My Idea è cambiato",
      cuerpo: "Il numero di telefono del tuo account My Idea è appena cambiato.",
    },
    accesoVinculado: {
      asunto: "C'è un nuovo modo per accedere al tuo account My Idea",
      cuerpo: "Al tuo account My Idea è stato aggiunto un nuovo modo per accedere.",
    },
    accesoDesvinculado: {
      asunto: "Un modo per accedere è stato rimosso dal tuo account My Idea",
      cuerpo: "Uno dei modi per accedere al tuo account My Idea è stato rimosso.",
    },
    verificacionAgregada: {
      asunto: "È stato aggiunto un metodo di verifica in due passaggi",
      cuerpo: "Al tuo account My Idea è stato aggiunto un metodo di verifica in due passaggi.",
    },
    verificacionQuitada: {
      asunto: "È stato rimosso un metodo di verifica in due passaggi",
      cuerpo: "Dal tuo account My Idea è stato rimosso un metodo di verifica in due passaggi.",
    },
  },
};

const ja: typeof es = {
  comun: {
    siBotonNoAbre: "ボタンが開かない場合は、このリンクをブラウザにコピーしてください：",
    oEscribeCodigo: "こちらのコードを入力することもできます：{{codigo}}",
    firma: "My Idea",
  },
  registro: {
    asunto: "My Ideaのメールアドレスを確認してください",
    titulo: "メールアドレスの確認",
    cuerpo: "あと少しです。メールアドレスを確認すると、My Ideaのアカウントの準備が整い、アイデアの続きに取りかかれます。",
    boton: "メールアドレスを確認する",
    nota: "My Ideaのアカウントを作成した覚えがない場合は、このメールを無視してください。",
  },
  invitacion: {
    asunto: "My Ideaへの招待が届いています",
    titulo: "招待が届いています",
    cuerpo: "My Ideaへの招待が届いています。招待を受けてアカウントを作成し、アイデアづくりを始めましょう。",
    boton: "招待を受ける",
    nota: "心当たりのない招待の場合は、このメールを無視してください。",
  },
  enlaceEntrar: {
    asunto: "My Ideaにログインするためのリンク",
    titulo: "My Ideaにログイン",
    cuerpo: "このリンクからアカウントにログインできます。使えるのは1回だけで、まもなく有効期限が切れます。",
    boton: "My Ideaにログインする",
    nota: "ログインを依頼した覚えがない場合は、このメールを無視してください。このリンクがなければ、誰もログインできません。",
  },
  recuperar: {
    asunto: "My Ideaの新しいパスワードを設定してください",
    titulo: "新しいパスワードの設定",
    cuerpo: "パスワードの変更が依頼されました。このリンクを開いて、新しいパスワードを設定してください。",
    boton: "新しいパスワードを設定する",
    nota: "心当たりがない場合は、このメールを無視してください。パスワードは変わりません。",
  },
  cambioCorreoActual: {
    asunto: "My Idea：メールアドレス変更の確認",
    titulo: "メールアドレス変更の確認",
    cuerpo: "アカウントのメールアドレスを{{actual}}から{{nuevo}}に変更する依頼がありました。こちらから確認してください。",
    boton: "変更を確認する",
    nota: "心当たりがない場合は、このメールを無視してください。メールアドレスは変わりません。",
  },
  cambioCorreoNuevo: {
    asunto: "My Idea：新しいメールアドレスの確認",
    titulo: "新しいメールアドレスの確認",
    cuerpo: "{{nuevo}}をMy Ideaアカウントのメールアドレスとして使う依頼がありました。こちらから確認してください。",
    boton: "新しいメールアドレスを確認する",
    nota: "心当たりがない場合は、このメールを無視してください。確認がなければ何も変わりません。",
  },
  reautenticacion: {
    asunto: "My Ideaの確認コード",
    titulo: "ご本人確認",
    cuerpo: "ご本人であることを確認するため、このコードをMy Ideaに入力してください：",
    nota: "心当たりがない場合は、このメールを無視してください。このコードがなければ、誰も変更できません。",
  },
  avisos: {
    notaSeguridad: "心当たりがない場合は、すぐにMy Ideaのログイン画面から新しいパスワードを設定してください。",
    contrasenaCambiada: {
      asunto: "My Ideaのパスワードが変更されました",
      cuerpo: "My Ideaアカウントのパスワードが変更されました。",
    },
    correoCambiado: {
      asunto: "My Ideaのメールアドレスが変更されました",
      cuerpo: "My Ideaアカウントのメールアドレスが変更されました。このお知らせは以前のメールアドレスにお送りしています。",
    },
    telefonoCambiado: {
      asunto: "My Ideaの電話番号が変更されました",
      cuerpo: "My Ideaアカウントの電話番号が変更されました。",
    },
    accesoVinculado: {
      asunto: "My Ideaに新しいログイン方法が追加されました",
      cuerpo: "My Ideaアカウントに新しいログイン方法が追加されました。",
    },
    accesoDesvinculado: {
      asunto: "My Ideaのログイン方法が削除されました",
      cuerpo: "My Ideaアカウントのログイン方法の1つが削除されました。",
    },
    verificacionAgregada: {
      asunto: "2段階認証の方法が追加されました",
      cuerpo: "My Ideaアカウントに2段階認証の方法が追加されました。",
    },
    verificacionQuitada: {
      asunto: "2段階認証の方法が削除されました",
      cuerpo: "My Ideaアカウントから2段階認証の方法が削除されました。",
    },
  },
};

const zh: typeof es = {
  comun: {
    siBotonNoAbre: "如果按钮打不开，请把这个链接复制到浏览器中：",
    oEscribeCodigo: "你也可以输入这个验证码：{{codigo}}",
    firma: "My Idea",
  },
  registro: {
    asunto: "请确认你在 My Idea 的邮箱",
    titulo: "确认你的邮箱",
    cuerpo: "就差一步了。确认邮箱后，你的 My Idea 账户就准备好了，可以继续推进你的想法。",
    boton: "确认我的邮箱",
    nota: "如果你没有注册 My Idea 账户，请忽略这封邮件。",
  },
  invitacion: {
    asunto: "你收到了 My Idea 的邀请",
    titulo: "你有一份邀请",
    cuerpo: "你收到了 My Idea 的邀请。接受邀请即可创建账户，开始你的想法。",
    boton: "接受邀请",
    nota: "如果你没有预料到这份邀请，请忽略这封邮件。",
  },
  enlaceEntrar: {
    asunto: "你的 My Idea 登录链接",
    titulo: "登录 My Idea",
    cuerpo: "用这个链接登录你的账户。它只能使用一次，并且很快就会过期。",
    boton: "登录 My Idea",
    nota: "如果你没有申请登录，请忽略这封邮件：没有这个链接，谁也无法登录。",
  },
  recuperar: {
    asunto: "为 My Idea 设置新密码",
    titulo: "设置新密码",
    cuerpo: "你申请了修改密码。打开这个链接，设置一个新密码。",
    boton: "设置新密码",
    nota: "如果不是你本人申请，请忽略这封邮件：你的密码不会改变。",
  },
  cambioCorreoActual: {
    asunto: "确认更改你在 My Idea 的邮箱",
    titulo: "确认更改邮箱",
    cuerpo: "你申请把账户邮箱从 {{actual}} 改为 {{nuevo}}。请在这里确认。",
    boton: "确认更改",
    nota: "如果不是你本人申请，请忽略这封邮件：你的账户邮箱保持不变。",
  },
  cambioCorreoNuevo: {
    asunto: "确认你在 My Idea 的新邮箱",
    titulo: "确认你的新邮箱",
    cuerpo: "你申请把 {{nuevo}} 设为 My Idea 账户的邮箱。请在这里确认。",
    boton: "确认我的新邮箱",
    nota: "如果不是你本人申请，请忽略这封邮件：没有你的确认，什么都不会改变。",
  },
  reautenticacion: {
    asunto: "你的 My Idea 确认码",
    titulo: "确认是你本人",
    cuerpo: "在 My Idea 中输入这个验证码，确认是你本人：",
    nota: "如果不是你本人操作，请忽略这封邮件：没有这个验证码，谁也无法做出更改。",
  },
  avisos: {
    notaSeguridad: "如果不是你本人操作，请尽快在 My Idea 的登录页面申请新密码。",
    contrasenaCambiada: {
      asunto: "你的 My Idea 密码已更改",
      cuerpo: "你的 My Idea 账户密码刚刚被更改。",
    },
    correoCambiado: {
      asunto: "你的 My Idea 账户邮箱已更改",
      cuerpo: "你的 My Idea 账户邮箱刚刚被更改。这条通知发送到你之前的邮箱。",
    },
    telefonoCambiado: {
      asunto: "你的 My Idea 账户手机号已更改",
      cuerpo: "你的 My Idea 账户手机号刚刚被更改。",
    },
    accesoVinculado: {
      asunto: "你的 My Idea 账户新增了一种登录方式",
      cuerpo: "你的 My Idea 账户刚刚新增了一种登录方式。",
    },
    accesoDesvinculado: {
      asunto: "你的 My Idea 账户移除了一种登录方式",
      cuerpo: "你的 My Idea 账户刚刚移除了一种登录方式。",
    },
    verificacionAgregada: {
      asunto: "已添加一种两步验证方式",
      cuerpo: "你的 My Idea 账户已添加一种两步验证方式。",
    },
    verificacionQuitada: {
      asunto: "已移除一种两步验证方式",
      cuerpo: "你的 My Idea 账户已移除一种两步验证方式。",
    },
  },
};

const ko: typeof es = {
  comun: {
    siBotonNoAbre: "버튼이 열리지 않으면 이 링크를 브라우저에 복사해 주세요:",
    oEscribeCodigo: "이 코드를 입력해도 돼요: {{codigo}}",
    firma: "My Idea",
  },
  registro: {
    asunto: "My Idea 이메일 주소를 확인해 주세요",
    titulo: "이메일 주소 확인",
    cuerpo: "거의 다 됐어요. 이메일 주소를 확인하면 My Idea 계정이 준비되고, 아이디어를 계속 이어 갈 수 있어요.",
    boton: "이메일 주소 확인하기",
    nota: "My Idea 계정을 만든 적이 없다면 이 메일은 무시하세요.",
  },
  invitacion: {
    asunto: "My Idea 초대장이 도착했어요",
    titulo: "초대장이 있어요",
    cuerpo: "My Idea에 초대받았어요. 초대를 수락하고 계정을 만들어 아이디어를 시작해 보세요.",
    boton: "초대 수락하기",
    nota: "예상하지 못한 초대라면 이 메일은 무시하세요.",
  },
  enlaceEntrar: {
    asunto: "My Idea 로그인 링크",
    titulo: "My Idea에 로그인하기",
    cuerpo: "이 링크로 계정에 로그인할 수 있어요. 한 번만 쓸 수 있고 곧 만료돼요.",
    boton: "My Idea에 로그인",
    nota: "로그인을 요청하지 않았다면 이 메일은 무시하세요. 이 링크 없이는 아무도 들어올 수 없어요.",
  },
  recuperar: {
    asunto: "My Idea 새 비밀번호를 정해 주세요",
    titulo: "새 비밀번호 정하기",
    cuerpo: "비밀번호 변경을 요청하셨어요. 이 링크를 열고 새 비밀번호를 정해 주세요.",
    boton: "새 비밀번호 정하기",
    nota: "본인이 요청하지 않았다면 이 메일은 무시하세요. 비밀번호는 그대로예요.",
  },
  cambioCorreoActual: {
    asunto: "My Idea 이메일 변경을 확인해 주세요",
    titulo: "이메일 변경 확인",
    cuerpo: "계정 이메일을 {{actual}}에서 {{nuevo}}(으)로 바꾸도록 요청하셨어요. 여기에서 확인해 주세요.",
    boton: "변경 확인하기",
    nota: "본인이 요청하지 않았다면 이 메일은 무시하세요. 계정 이메일은 그대로예요.",
  },
  cambioCorreoNuevo: {
    asunto: "My Idea 새 이메일 주소를 확인해 주세요",
    titulo: "새 이메일 주소 확인",
    cuerpo: "{{nuevo}}을(를) My Idea 계정 이메일로 쓰도록 요청하셨어요. 여기에서 확인해 주세요.",
    boton: "새 이메일 주소 확인하기",
    nota: "본인이 요청하지 않았다면 이 메일은 무시하세요. 확인하지 않으면 아무것도 바뀌지 않아요.",
  },
  reautenticacion: {
    asunto: "My Idea 확인 코드",
    titulo: "본인 확인",
    cuerpo: "본인임을 확인하려면 My Idea에 이 코드를 입력해 주세요:",
    nota: "본인이 요청하지 않았다면 이 메일은 무시하세요. 이 코드 없이는 아무도 변경할 수 없어요.",
  },
  avisos: {
    notaSeguridad: "본인이 한 일이 아니라면 My Idea 로그인 화면에서 바로 새 비밀번호를 요청하세요.",
    contrasenaCambiada: {
      asunto: "My Idea 비밀번호가 변경됐어요",
      cuerpo: "My Idea 계정의 비밀번호가 방금 변경됐어요.",
    },
    correoCambiado: {
      asunto: "My Idea 계정 이메일이 변경됐어요",
      cuerpo: "My Idea 계정의 이메일이 방금 변경됐어요. 이 알림은 이전 이메일로 보내 드려요.",
    },
    telefonoCambiado: {
      asunto: "My Idea 계정 전화번호가 변경됐어요",
      cuerpo: "My Idea 계정의 전화번호가 방금 변경됐어요.",
    },
    accesoVinculado: {
      asunto: "My Idea 계정에 새 로그인 방법이 추가됐어요",
      cuerpo: "My Idea 계정에 새 로그인 방법이 방금 추가됐어요.",
    },
    accesoDesvinculado: {
      asunto: "My Idea 계정에서 로그인 방법이 삭제됐어요",
      cuerpo: "My Idea 계정의 로그인 방법 하나가 방금 삭제됐어요.",
    },
    verificacionAgregada: {
      asunto: "2단계 인증 방법이 추가됐어요",
      cuerpo: "My Idea 계정에 2단계 인증 방법이 추가됐어요.",
    },
    verificacionQuitada: {
      asunto: "2단계 인증 방법이 삭제됐어요",
      cuerpo: "My Idea 계정에서 2단계 인증 방법이 삭제됐어요.",
    },
  },
};

const ar: typeof es = {
  comun: {
    siBotonNoAbre: "إن لم يُفتح الزر، فانسخوا هذا الرابط في المتصفح:",
    oEscribeCodigo: "يمكنكم أيضًا كتابة هذا الرمز: {{codigo}}",
    firma: "My Idea",
  },
  registro: {
    asunto: "أكّدوا بريدكم الإلكتروني في My Idea",
    titulo: "أكّدوا بريدكم الإلكتروني",
    cuerpo: "بقيت خطوة واحدة. أكّدوا بريدكم الإلكتروني ليصبح حسابكم في My Idea جاهزًا لمواصلة العمل على فكرتكم.",
    boton: "تأكيد بريدي الإلكتروني",
    nota: "إن لم تنشئوا حسابًا في My Idea، فتجاهلوا هذه الرسالة.",
  },
  invitacion: {
    asunto: "وصلتكم دعوة إلى My Idea",
    titulo: "لديكم دعوة",
    cuerpo: "وصلتكم دعوة إلى My Idea. اقبلوا الدعوة لإنشاء حسابكم والبدء بفكرتكم.",
    boton: "قبول الدعوة",
    nota: "إن لم تكونوا تتوقعون هذه الدعوة، فتجاهلوا هذه الرسالة.",
  },
  enlaceEntrar: {
    asunto: "رابط الدخول إلى My Idea",
    titulo: "ادخلوا إلى My Idea",
    cuerpo: "استخدموا هذا الرابط للدخول إلى حسابكم. يعمل مرة واحدة فقط وتنتهي صلاحيته قريبًا.",
    boton: "الدخول إلى My Idea",
    nota: "إن لم تطلبوا الدخول، فتجاهلوا هذه الرسالة: لا أحد يدخل دون هذا الرابط.",
  },
  recuperar: {
    asunto: "اختاروا كلمة مرور جديدة لـ My Idea",
    titulo: "اختاروا كلمة مرور جديدة",
    cuerpo: "طلبتم تغيير كلمة المرور. افتحوا هذا الرابط واختاروا كلمة جديدة.",
    boton: "اختيار كلمة مرور جديدة",
    nota: "إن لم تطلبوا ذلك، فتجاهلوا هذه الرسالة: كلمة المرور تبقى كما هي.",
  },
  cambioCorreoActual: {
    asunto: "أكّدوا تغيير البريد الإلكتروني في My Idea",
    titulo: "أكّدوا تغيير البريد الإلكتروني",
    cuerpo: "طلبتم تغيير البريد الإلكتروني لحسابكم من {{actual}} إلى {{nuevo}}. أكّدوا ذلك من هنا.",
    boton: "تأكيد التغيير",
    nota: "إن لم تطلبوا ذلك، فتجاهلوا هذه الرسالة: يبقى حسابكم بالبريد نفسه.",
  },
  cambioCorreoNuevo: {
    asunto: "أكّدوا بريدكم الإلكتروني الجديد في My Idea",
    titulo: "أكّدوا بريدكم الإلكتروني الجديد",
    cuerpo: "طلبتم استخدام {{nuevo}} بريدًا إلكترونيًا لحسابكم في My Idea. أكّدوا ذلك من هنا.",
    boton: "تأكيد بريدي الجديد",
    nota: "إن لم تطلبوا ذلك، فتجاهلوا هذه الرسالة: لا يتغيّر شيء دون تأكيدكم.",
  },
  reautenticacion: {
    asunto: "رمز التأكيد الخاص بكم في My Idea",
    titulo: "أكّدوا أنكم أنتم",
    cuerpo: "اكتبوا هذا الرمز في My Idea لتأكيد أنكم أنتم:",
    nota: "إن لم تكونوا أنتم، فتجاهلوا هذه الرسالة: لا أحد يُجري تغييرات دون هذا الرمز.",
  },
  avisos: {
    notaSeguridad: "إن لم تكونوا أنتم، فاطلبوا كلمة مرور جديدة من شاشة الدخول في My Idea في أقرب وقت.",
    contrasenaCambiada: {
      asunto: "تغيّرت كلمة المرور لحسابكم في My Idea",
      cuerpo: "تغيّرت للتو كلمة المرور لحسابكم في My Idea.",
    },
    correoCambiado: {
      asunto: "تغيّر البريد الإلكتروني لحسابكم في My Idea",
      cuerpo: "تغيّر للتو البريد الإلكتروني لحسابكم في My Idea. يصل هذا الإشعار إلى بريدكم السابق.",
    },
    telefonoCambiado: {
      asunto: "تغيّر رقم الهاتف لحسابكم في My Idea",
      cuerpo: "تغيّر للتو رقم الهاتف لحسابكم في My Idea.",
    },
    accesoVinculado: {
      asunto: "أُضيفت طريقة جديدة للدخول إلى حسابكم في My Idea",
      cuerpo: "أُضيفت للتو طريقة جديدة للدخول إلى حسابكم في My Idea.",
    },
    accesoDesvinculado: {
      asunto: "أُزيلت طريقة للدخول من حسابكم في My Idea",
      cuerpo: "أُزيلت للتو إحدى طرق الدخول إلى حسابكم في My Idea.",
    },
    verificacionAgregada: {
      asunto: "أُضيفت طريقة للتحقق بخطوتين",
      cuerpo: "أُضيفت طريقة للتحقق بخطوتين إلى حسابكم في My Idea.",
    },
    verificacionQuitada: {
      asunto: "أُزيلت طريقة للتحقق بخطوتين",
      cuerpo: "أُزيلت طريقة للتحقق بخطوتين من حسابكم في My Idea.",
    },
  },
};

const hi: typeof es = {
  comun: {
    siBotonNoAbre: "अगर बटन न खुले, तो यह लिंक अपने ब्राउज़र में कॉपी करें:",
    oEscribeCodigo: "आप यह कोड भी लिख सकते हैं: {{codigo}}",
    firma: "My Idea",
  },
  registro: {
    asunto: "My Idea पर अपने ईमेल की पुष्टि करें",
    titulo: "अपने ईमेल की पुष्टि करें",
    cuerpo: "बस थोड़ा सा बाकी है। अपने ईमेल की पुष्टि करें, फिर आपका My Idea खाता तैयार हो जाएगा और आप अपने विचार पर आगे बढ़ सकेंगे।",
    boton: "मेरे ईमेल की पुष्टि करें",
    nota: "अगर आपने My Idea पर खाता नहीं बनाया, तो इस ईमेल को अनदेखा करें।",
  },
  invitacion: {
    asunto: "आपको My Idea का न्योता मिला है",
    titulo: "आपके लिए एक न्योता है",
    cuerpo: "आपको My Idea का न्योता मिला है। अपना खाता बनाने और अपने विचार की शुरुआत करने के लिए न्योता स्वीकार करें।",
    boton: "न्योता स्वीकार करें",
    nota: "अगर आपको इस न्योते की उम्मीद नहीं थी, तो इस ईमेल को अनदेखा करें।",
  },
  enlaceEntrar: {
    asunto: "My Idea में लॉग इन करने का आपका लिंक",
    titulo: "My Idea में लॉग इन करें",
    cuerpo: "इस लिंक से अपने खाते में लॉग इन करें। यह सिर्फ़ एक बार काम करता है और जल्द ही एक्सपायर हो जाएगा।",
    boton: "My Idea में लॉग इन करें",
    nota: "अगर आपने लॉग इन करने को नहीं कहा, तो इस ईमेल को अनदेखा करें: इस लिंक के बिना कोई लॉग इन नहीं कर सकता।",
  },
  recuperar: {
    asunto: "My Idea के लिए नया पासवर्ड चुनें",
    titulo: "नया पासवर्ड चुनें",
    cuerpo: "आपने अपना पासवर्ड बदलने को कहा है। यह लिंक खोलें और नया पासवर्ड चुनें।",
    boton: "नया पासवर्ड चुनें",
    nota: "अगर यह आपने नहीं माँगा, तो इस ईमेल को अनदेखा करें: आपका पासवर्ड वही रहेगा।",
  },
  cambioCorreoActual: {
    asunto: "My Idea पर ईमेल बदलने की पुष्टि करें",
    titulo: "ईमेल बदलने की पुष्टि करें",
    cuerpo: "आपने अपने खाते का ईमेल {{actual}} से बदलकर {{nuevo}} करने को कहा है। यहाँ से पुष्टि करें।",
    boton: "बदलाव की पुष्टि करें",
    nota: "अगर यह आपने नहीं माँगा, तो इस ईमेल को अनदेखा करें: आपके खाते का ईमेल वही रहेगा।",
  },
  cambioCorreoNuevo: {
    asunto: "My Idea पर अपने नए ईमेल की पुष्टि करें",
    titulo: "अपने नए ईमेल की पुष्टि करें",
    cuerpo: "आपने {{nuevo}} को अपने My Idea खाते का ईमेल बनाने को कहा है। यहाँ से पुष्टि करें।",
    boton: "मेरे नए ईमेल की पुष्टि करें",
    nota: "अगर यह आपने नहीं माँगा, तो इस ईमेल को अनदेखा करें: आपकी पुष्टि के बिना कुछ नहीं बदलेगा।",
  },
  reautenticacion: {
    asunto: "आपका My Idea पुष्टि कोड",
    titulo: "पुष्टि करें कि यह आप ही हैं",
    cuerpo: "यह पुष्टि करने के लिए कि यह आप ही हैं, My Idea में यह कोड लिखें:",
    nota: "अगर यह आपने नहीं माँगा, तो इस ईमेल को अनदेखा करें: इस कोड के बिना कोई बदलाव नहीं कर सकता।",
  },
  avisos: {
    notaSeguridad: "अगर यह आपने नहीं किया, तो तुरंत My Idea की लॉग इन स्क्रीन से नया पासवर्ड माँगें।",
    contrasenaCambiada: {
      asunto: "आपका My Idea पासवर्ड बदल गया है",
      cuerpo: "आपके My Idea खाते का पासवर्ड अभी-अभी बदला गया है।",
    },
    correoCambiado: {
      asunto: "आपके My Idea खाते का ईमेल बदल गया है",
      cuerpo: "आपके My Idea खाते का ईमेल अभी-अभी बदला गया है। यह सूचना आपके पुराने ईमेल पर भेजी गई है।",
    },
    telefonoCambiado: {
      asunto: "आपके My Idea खाते का फ़ोन नंबर बदल गया है",
      cuerpo: "आपके My Idea खाते का फ़ोन नंबर अभी-अभी बदला गया है।",
    },
    accesoVinculado: {
      asunto: "आपके My Idea खाते में लॉग इन का नया तरीका जुड़ा है",
      cuerpo: "आपके My Idea खाते में लॉग इन करने का एक नया तरीका अभी-अभी जोड़ा गया है।",
    },
    accesoDesvinculado: {
      asunto: "आपके My Idea खाते से लॉग इन का एक तरीका हटाया गया है",
      cuerpo: "आपके My Idea खाते में लॉग इन करने का एक तरीका अभी-अभी हटाया गया है।",
    },
    verificacionAgregada: {
      asunto: "दो-चरणीय सत्यापन का एक तरीका जोड़ा गया है",
      cuerpo: "आपके My Idea खाते में दो-चरणीय सत्यापन का एक तरीका जोड़ा गया है।",
    },
    verificacionQuitada: {
      asunto: "दो-चरणीय सत्यापन का एक तरीका हटाया गया है",
      cuerpo: "आपके My Idea खाते से दो-चरणीय सत्यापन का एक तरीका हटाया गया है।",
    },
  },
};

export const CORREOS_AUTH: PorIdioma<typeof es> = { es, en, pt, fr, de, it, ja, zh, ko, ar, hi };
