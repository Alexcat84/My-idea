/** Rutas de /api/project/[id]/* (sin mundos ni documentos), del calendario y de los packs. */
import type { PorIdioma } from "../config";

const es = {
  borrar: {
    algoSeAtoro: "algo se atoró; intenta de nuevo",
  },
  baseline: {
    faltaPlanOFechas: "falta plan_id o fechas mal formadas",
    noPudimosSellar: "no pudimos sellar la línea base",
  },
  modo: {
    modoInvalido: "modo_camino inválido; usa uno de: {{opciones}}",
    capacidadInvalida: "capacidad_semanal inválida; usa una de: {{opciones}}",
    nadaQueActualizar: "nada que actualizar: manda modo_camino y/o capacidad_semanal",
    espacioNoExiste: "ese espacio no existe",
  },
  checklist: {
    faltaItemId: "falta item_id",
    estadoInvalido: "estado inválido; usa uno de: {{opciones}}",
    notaInvalida: "nota debe ser texto o null",
    completedAtInvalido: "completed_at debe ser una fecha ISO no futura o null",
    motivoInvalido: "no_aplica_motivo debe ser texto o null",
    bandaInvalida: "banda inválida; usa una de: {{opciones}}",
    fechaBaseInvalida: "fecha_base debe ser una fecha ISO o null",
    nadaQueActualizar: "nada que actualizar: manda estado, nota, completed_at, no_aplica_motivo, fecha_base y/o banda",
    itemNoEncontrado: "ítem no encontrado",
  },
  moverFecha: {
    faltaItemOFecha: "falta item_id o fecha mal formada",
    actividadNoEncontrada: "actividad no encontrada",
    yaHecha: "Esta actividad ya está hecha. Si la hiciste en otra fecha, cámbiala desde la actividad.",
    retirada: "Esta actividad está retirada. Reactívala primero para darle una fecha.",
    sinFecha: "esta actividad no tiene una fecha que mover",
  },
  realizar: {
    accionInvalida: "acción inválida; usa 'realizar' o 'reabrir'",
    noPudeGuardarActa:
      "No pude guardar el acta de tu cierre, así que tu idea sigue abierta. Intenta de nuevo en un momento.",
  },
  follow: {
    ideaRealizada: "Diste tu idea por realizada. Reábrela si quieres seguir trabajándola.",
    mundoCompletado: 'Diste "{{mundo}}" por completado. Reábrelo si quieres seguir trabajándolo.',
    primeroExplora: 'Primero explora "{{mundo}}": su seguimiento nace de su plan.',
    puertasRecorridas: 'Ya recorriste todas las puertas de "{{mundo}}".',
  },
  numeros: {
    cifrasNoObjeto: "'numeros' debe ser un objeto de campo: valor",
    valorInvalido: "el valor de '{{campo}}' debe ser un número >= 0 o un rango {min, max}",
    versionNoExiste: "esa versión no existe",
    activaUnaVez: "Tus Números se activa una vez por idea.",
    noNarroInconsistente:
      "No narro una conclusión con estos datos: revisa el guardián de datos y corrige la cifra que no cuadra.",
    noPudeNarrar:
      "No pude narrar tus números en este momento. Tu tablero y tus cifras están al día; intenta narrar de nuevo en un rato.",
  },
  reporte: {
    proyectoNoEncontrado: "proyecto no encontrado",
    respuestaInvalida: "'respuesta' debe ser un string no vacío",
    entrevistaEnCurso: "ya hay una entrevista de reporte en curso; envía 'respuesta' para continuarla",
    sinEntrevista: "no hay una entrevista de reporte en curso; llama sin 'respuesta' para iniciarla",
  },
  bitacora: {
    tituloEspacio: "# Bitácora de {{espacio}}",
  },
  calendario: {
    noEncontrado: "Calendario no encontrado.",
    tuViaje: "Tu viaje",
  },
  packs: {
    packDesconocido: "pack desconocido",
  },
};

const en: typeof es = {
  borrar: {
    algoSeAtoro: "something got stuck; try again",
  },
  baseline: {
    faltaPlanOFechas: "missing plan_id or malformed dates",
    noPudimosSellar: "we couldn't lock in the baseline",
  },
  modo: {
    modoInvalido: "invalid modo_camino; use one of: {{opciones}}",
    capacidadInvalida: "invalid capacidad_semanal; use one of: {{opciones}}",
    nadaQueActualizar: "nothing to update: send modo_camino and/or capacidad_semanal",
    espacioNoExiste: "that space doesn't exist",
  },
  checklist: {
    faltaItemId: "missing item_id",
    estadoInvalido: "invalid estado; use one of: {{opciones}}",
    notaInvalida: "nota must be text or null",
    completedAtInvalido: "completed_at must be an ISO date not in the future, or null",
    motivoInvalido: "no_aplica_motivo must be text or null",
    bandaInvalida: "invalid banda; use one of: {{opciones}}",
    fechaBaseInvalida: "fecha_base must be an ISO date or null",
    nadaQueActualizar: "nothing to update: send estado, nota, completed_at, no_aplica_motivo, fecha_base and/or banda",
    itemNoEncontrado: "item not found",
  },
  moverFecha: {
    faltaItemOFecha: "missing item_id or malformed date",
    actividadNoEncontrada: "activity not found",
    yaHecha: "This activity is already done. If you did it on a different date, change it from the activity itself.",
    retirada: "This activity is set aside. Bring it back first to give it a date.",
    sinFecha: "this activity doesn't have a date to move",
  },
  realizar: {
    accionInvalida: "invalid action; use 'realizar' or 'reabrir'",
    noPudeGuardarActa:
      "I couldn't save the closing record for your idea, so it's still open. Try again in a moment.",
  },
  follow: {
    ideaRealizada: "You marked your idea as achieved. Reopen it if you want to keep working on it.",
    mundoCompletado: 'You marked "{{mundo}}" as completed. Reopen it if you want to keep working on it.',
    primeroExplora: 'Explore "{{mundo}}" first: its follow-up grows out of its plan.',
    puertasRecorridas: 'You\'ve already been through every door in "{{mundo}}".',
  },
  numeros: {
    cifrasNoObjeto: "'numeros' must be an object of field: value",
    valorInvalido: "the value of '{{campo}}' must be a number >= 0 or a range {min, max}",
    versionNoExiste: "that version doesn't exist",
    activaUnaVez: "Your Numbers is activated once per idea.",
    noNarroInconsistente:
      "I won't narrate a conclusion from this data: check the data guardian and fix the figure that doesn't add up.",
    noPudeNarrar:
      "I couldn't narrate your numbers right now. Your dashboard and your figures are up to date; try narrating again in a little while.",
  },
  reporte: {
    proyectoNoEncontrado: "project not found",
    respuestaInvalida: "'respuesta' must be a non-empty string",
    entrevistaEnCurso: "there's already a report interview in progress; send 'respuesta' to continue it",
    sinEntrevista: "there's no report interview in progress; call without 'respuesta' to start one",
  },
  bitacora: {
    tituloEspacio: "# {{espacio}} Logbook",
  },
  calendario: {
    noEncontrado: "Calendar not found.",
    tuViaje: "Your Journey",
  },
  packs: {
    packDesconocido: "unknown pack",
  },
};

const fr: typeof es = {
  borrar: {
    algoSeAtoro: "quelque chose a coincé; réessaie",
  },
  baseline: {
    faltaPlanOFechas: "plan_id manquant ou dates mal formées",
    noPudimosSellar: "nous n'avons pas pu fixer le plan de référence",
  },
  modo: {
    modoInvalido: "modo_camino invalide; utilise l'une de ces valeurs : {{opciones}}",
    capacidadInvalida: "capacidad_semanal invalide; utilise l'une de ces valeurs : {{opciones}}",
    nadaQueActualizar: "rien à mettre à jour : envoie modo_camino et/ou capacidad_semanal",
    espacioNoExiste: "cet espace n'existe pas",
  },
  checklist: {
    faltaItemId: "item_id manquant",
    estadoInvalido: "estado invalide; utilise l'une de ces valeurs : {{opciones}}",
    notaInvalida: "nota doit être du texte ou null",
    completedAtInvalido: "completed_at doit être une date ISO qui n'est pas dans le futur, ou null",
    motivoInvalido: "no_aplica_motivo doit être du texte ou null",
    bandaInvalida: "banda invalide; utilise l'une de ces valeurs : {{opciones}}",
    fechaBaseInvalida: "fecha_base doit être une date ISO ou null",
    nadaQueActualizar: "rien à mettre à jour : envoie estado, nota, completed_at, no_aplica_motivo, fecha_base et/ou banda",
    itemNoEncontrado: "élément introuvable",
  },
  moverFecha: {
    faltaItemOFecha: "item_id manquant ou date mal formée",
    actividadNoEncontrada: "activité introuvable",
    yaHecha: "Cette activité est déjà faite. Si tu l'as faite à une autre date, change-la depuis l'activité.",
    retirada: "Cette activité est mise de côté. Réactive-la d'abord pour lui donner une date.",
    sinFecha: "cette activité n'a pas de date à déplacer",
  },
  realizar: {
    accionInvalida: "action invalide; utilise 'realizar' ou 'reabrir'",
    noPudeGuardarActa: "Je n'ai pas pu enregistrer le bilan de clôture de ton idée, alors elle reste ouverte. Réessaie dans un instant.",
  },
  follow: {
    ideaRealizada: "Tu as déclaré ton idée réalisée. Rouvre-la si tu veux continuer à la travailler.",
    mundoCompletado: "Tu as déclaré « {{mundo}} » terminé. Rouvre-le si tu veux continuer à y travailler.",
    primeroExplora: "Explore d'abord « {{mundo}} » : son suivi naît de son plan.",
    puertasRecorridas: "Tu as déjà franchi toutes les portes de « {{mundo}} ».",
  },
  numeros: {
    cifrasNoObjeto: "'numeros' doit être un objet de la forme champ : valeur",
    valorInvalido: "la valeur de '{{campo}}' doit être un nombre >= 0 ou un intervalle {min, max}",
    versionNoExiste: "cette version n'existe pas",
    activaUnaVez: "Tes chiffres s'activent une seule fois par idée.",
    noNarroInconsistente: "Je ne tire pas de conclusion de ces données : consulte le gardien des données et corrige le chiffre qui ne concorde pas.",
    noPudeNarrar: "Je n'ai pas pu mettre tes chiffres en mots pour le moment. Ton tableau de bord et tes chiffres sont à jour; réessaie un peu plus tard.",
  },
  reporte: {
    proyectoNoEncontrado: "projet introuvable",
    respuestaInvalida: "'respuesta' doit être une chaîne non vide",
    entrevistaEnCurso: "un entretien de rapport est déjà en cours; envoie 'respuesta' pour le poursuivre",
    sinEntrevista: "aucun entretien de rapport n'est en cours; appelle sans 'respuesta' pour en commencer un",
  },
  bitacora: {
    tituloEspacio: "# Journal de bord de {{espacio}}",
  },
  calendario: {
    noEncontrado: "Calendrier introuvable.",
    tuViaje: "Ton parcours",
  },
  packs: {
    packDesconocido: "forfait inconnu",
  },
};

const pt: typeof es = {
  borrar: {
    algoSeAtoro: "algo travou; tente de novo",
  },
  baseline: {
    faltaPlanOFechas: "falta plan_id ou as datas estão mal formatadas",
    noPudimosSellar: "não conseguimos fixar a linha de base",
  },
  modo: {
    modoInvalido: "modo_camino inválido; use um destes: {{opciones}}",
    capacidadInvalida: "capacidad_semanal inválida; use uma destas: {{opciones}}",
    nadaQueActualizar: "nada para atualizar: envie modo_camino e/ou capacidad_semanal",
    espacioNoExiste: "esse espaço não existe",
  },
  checklist: {
    faltaItemId: "falta item_id",
    estadoInvalido: "estado inválido; use um destes: {{opciones}}",
    notaInvalida: "nota deve ser texto ou null",
    completedAtInvalido: "completed_at deve ser uma data ISO não futura ou null",
    motivoInvalido: "no_aplica_motivo deve ser texto ou null",
    bandaInvalida: "banda inválida; use uma destas: {{opciones}}",
    fechaBaseInvalida: "fecha_base deve ser uma data ISO ou null",
    nadaQueActualizar: "nada para atualizar: envie estado, nota, completed_at, no_aplica_motivo, fecha_base e/ou banda",
    itemNoEncontrado: "item não encontrado",
  },
  moverFecha: {
    faltaItemOFecha: "falta item_id ou a data está mal formatada",
    actividadNoEncontrada: "atividade não encontrada",
    yaHecha: "Esta atividade já está feita. Se você a fez em outra data, altere pela própria atividade.",
    retirada: "Esta atividade foi deixada de lado. Reative-a primeiro para dar uma data a ela.",
    sinFecha: "esta atividade não tem uma data para mover",
  },
  realizar: {
    accionInvalida: "ação inválida; use 'realizar' ou 'reabrir'",
    noPudeGuardarActa: "Não consegui salvar a ata do seu encerramento, então sua ideia continua aberta. Tente de novo daqui a pouco.",
  },
  follow: {
    ideaRealizada: "Você deu sua ideia por realizada. Reabra-a se quiser continuar trabalhando nela.",
    mundoCompletado: "Você deu \"{{mundo}}\" por concluído. Reabra-o se quiser continuar trabalhando nele.",
    primeroExplora: "Explore \"{{mundo}}\" primeiro: o acompanhamento dele nasce do plano dele.",
    puertasRecorridas: "Você já percorreu todas as portas de \"{{mundo}}\".",
  },
  numeros: {
    cifrasNoObjeto: "'numeros' deve ser um objeto de campo: valor",
    valorInvalido: "o valor de '{{campo}}' deve ser um número >= 0 ou um intervalo {min, max}",
    versionNoExiste: "essa versão não existe",
    activaUnaVez: "Seus Números são ativados uma vez por ideia.",
    noNarroInconsistente: "Não narro uma conclusão com estes dados: confira o guardião dos dados e corrija o valor que não bate.",
    noPudeNarrar: "Não consegui narrar seus números agora. Seu painel e seus valores estão em dia; tente narrar de novo daqui a pouco.",
  },
  reporte: {
    proyectoNoEncontrado: "projeto não encontrado",
    respuestaInvalida: "'respuesta' deve ser uma string não vazia",
    entrevistaEnCurso: "já existe uma entrevista de relatório em andamento; envie 'respuesta' para continuá-la",
    sinEntrevista: "não há uma entrevista de relatório em andamento; chame sem 'respuesta' para iniciá-la",
  },
  bitacora: {
    tituloEspacio: "# Diário de bordo de {{espacio}}",
  },
  calendario: {
    noEncontrado: "Calendário não encontrado.",
    tuViaje: "Sua Jornada",
  },
  packs: {
    packDesconocido: "pacote desconhecido",
  },
};

const de: typeof es = {
  borrar: {
    algoSeAtoro: "etwas hat gehakt; versuch es noch einmal",
  },
  baseline: {
    faltaPlanOFechas: "plan_id fehlt oder die Daten sind fehlerhaft formatiert",
    noPudimosSellar: "wir konnten den Basisplan nicht festschreiben",
  },
  modo: {
    modoInvalido: "modo_camino ungültig; verwende einen dieser Werte: {{opciones}}",
    capacidadInvalida: "capacidad_semanal ungültig; verwende einen dieser Werte: {{opciones}}",
    nadaQueActualizar: "nichts zu aktualisieren: sende modo_camino und/oder capacidad_semanal",
    espacioNoExiste: "diesen Bereich gibt es nicht",
  },
  checklist: {
    faltaItemId: "item_id fehlt",
    estadoInvalido: "estado ungültig; verwende einen dieser Werte: {{opciones}}",
    notaInvalida: "nota muss Text oder null sein",
    completedAtInvalido: "completed_at muss ein ISO-Datum sein, das nicht in der Zukunft liegt, oder null",
    motivoInvalido: "no_aplica_motivo muss Text oder null sein",
    bandaInvalida: "banda ungültig; verwende einen dieser Werte: {{opciones}}",
    fechaBaseInvalida: "fecha_base muss ein ISO-Datum oder null sein",
    nadaQueActualizar: "nichts zu aktualisieren: sende estado, nota, completed_at, no_aplica_motivo, fecha_base und/oder banda",
    itemNoEncontrado: "Eintrag nicht gefunden",
  },
  moverFecha: {
    faltaItemOFecha: "item_id fehlt oder das Datum ist fehlerhaft formatiert",
    actividadNoEncontrada: "Schritt nicht gefunden",
    yaHecha: "Dieser Schritt ist schon erledigt. Wenn du ihn an einem anderen Tag erledigt hast, ändere das Datum direkt im Schritt.",
    retirada: "Dieser Schritt ist zurückgestellt. Hol ihn zuerst zurück, um ihm ein Datum zu geben.",
    sinFecha: "dieser Schritt hat kein Datum, das sich verschieben ließe",
  },
  realizar: {
    accionInvalida: "ungültige Aktion; verwende 'realizar' oder 'reabrir'",
    noPudeGuardarActa: "Ich konnte das Abschlussprotokoll nicht speichern, deshalb ist deine Idee noch offen. Versuch es gleich noch einmal.",
  },
  follow: {
    ideaRealizada: "Du hast deine Idee als verwirklicht markiert. Öffne sie wieder, wenn du weiter daran arbeiten möchtest.",
    mundoCompletado: "Du hast „{{mundo}}“ als abgeschlossen markiert. Öffne die Welt wieder, wenn du weiter daran arbeiten möchtest.",
    primeroExplora: "Erkunde zuerst „{{mundo}}“: Der Zwischenstand dieser Welt baut auf ihrem Plan auf.",
    puertasRecorridas: "Du bist schon durch alle Türen von „{{mundo}}“ gegangen.",
  },
  numeros: {
    cifrasNoObjeto: "'numeros' muss ein Objekt aus Feld: Wert sein",
    valorInvalido: "der Wert von '{{campo}}' muss eine Zahl >= 0 oder ein Bereich {min, max} sein",
    versionNoExiste: "diese Version gibt es nicht",
    activaUnaVez: "„Deine Zahlen“ aktivierst du einmal pro Idee.",
    noNarroInconsistente: "Aus diesen Daten ziehe ich keine Schlussfolgerung: Prüf den Datenwächter und korrigiere die Zahl, die nicht stimmt.",
    noPudeNarrar: "Ich konnte deine Zahlen gerade nicht in Worte fassen. Deine Übersicht und deine Werte sind aktuell; versuch es in einer Weile noch einmal.",
  },
  reporte: {
    proyectoNoEncontrado: "Projekt nicht gefunden",
    respuestaInvalida: "'respuesta' muss ein nicht leerer String sein",
    entrevistaEnCurso: "es läuft bereits ein Berichtsgespräch; sende 'respuesta', um es fortzusetzen",
    sinEntrevista: "es läuft kein Berichtsgespräch; rufe ohne 'respuesta' auf, um eines zu starten",
  },
  bitacora: {
    tituloEspacio: "# Logbuch zu {{espacio}}",
  },
  calendario: {
    noEncontrado: "Kalender nicht gefunden.",
    tuViaje: "Deine Reise",
  },
  packs: {
    packDesconocido: "unbekanntes Paket",
  },
};

const it: typeof es = {
  borrar: {
    algoSeAtoro: "qualcosa si è inceppato; riprova",
  },
  baseline: {
    faltaPlanOFechas: "manca plan_id o le date non sono valide",
    noPudimosSellar: "non siamo riusciti a fissare la linea di base",
  },
  modo: {
    modoInvalido: "modo_camino non valido; usa uno di questi: {{opciones}}",
    capacidadInvalida: "capacidad_semanal non valida; usa uno di questi: {{opciones}}",
    nadaQueActualizar: "niente da aggiornare: invia modo_camino e/o capacidad_semanal",
    espacioNoExiste: "questo spazio non esiste",
  },
  checklist: {
    faltaItemId: "manca item_id",
    estadoInvalido: "estado non valido; usa uno di questi: {{opciones}}",
    notaInvalida: "nota deve essere testo o null",
    completedAtInvalido: "completed_at deve essere una data ISO non futura o null",
    motivoInvalido: "no_aplica_motivo deve essere testo o null",
    bandaInvalida: "banda non valida; usa uno di questi: {{opciones}}",
    fechaBaseInvalida: "fecha_base deve essere una data ISO o null",
    nadaQueActualizar: "niente da aggiornare: invia estado, nota, completed_at, no_aplica_motivo, fecha_base e/o banda",
    itemNoEncontrado: "elemento non trovato",
  },
  moverFecha: {
    faltaItemOFecha: "manca item_id o la data non è valida",
    actividadNoEncontrada: "attività non trovata",
    yaHecha: "Questa attività è già stata fatta. Se l'hai fatta in un'altra data, cambiala dall'attività stessa.",
    retirada: "Questa attività è stata messa da parte. Riattivala prima di darle una data.",
    sinFecha: "questa attività non ha una data da spostare",
  },
  realizar: {
    accionInvalida: "azione non valida; usa 'realizar' o 'reabrir'",
    noPudeGuardarActa: "Non sono riuscito a salvare il verbale di chiusura, quindi la tua idea resta aperta. Riprova tra un momento.",
  },
  follow: {
    ideaRealizada: "Hai dato la tua idea per realizzata. Riaprila se vuoi continuare a lavorarci.",
    mundoCompletado: "Hai dato \"{{mundo}}\" per completato. Riaprilo se vuoi continuare a lavorarci.",
    primeroExplora: "Prima esplora \"{{mundo}}\": la sua revisione nasce dal suo piano.",
    puertasRecorridas: "Hai già attraversato tutte le porte di \"{{mundo}}\".",
  },
  numeros: {
    cifrasNoObjeto: "'numeros' deve essere un oggetto campo: valore",
    valorInvalido: "il valore di '{{campo}}' deve essere un numero >= 0 o un intervallo {min, max}",
    versionNoExiste: "questa versione non esiste",
    activaUnaVez: "I tuoi numeri si attivano una sola volta per idea.",
    noNarroInconsistente: "Non traggo conclusioni da questi dati: controlla il guardiano dei dati e correggi la cifra che non torna.",
    noPudeNarrar: "Non sono riuscito a raccontare i tuoi numeri in questo momento. Il tuo cruscotto e le tue cifre sono aggiornati; riprova tra un po'.",
  },
  reporte: {
    proyectoNoEncontrado: "progetto non trovato",
    respuestaInvalida: "'respuesta' deve essere una stringa non vuota",
    entrevistaEnCurso: "c'è già un'intervista di resoconto in corso; invia 'respuesta' per continuarla",
    sinEntrevista: "non c'è nessuna intervista di resoconto in corso; chiama senza 'respuesta' per avviarla",
  },
  bitacora: {
    tituloEspacio: "# Diario di bordo di {{espacio}}",
  },
  calendario: {
    noEncontrado: "Calendario non trovato.",
    tuViaje: "Il tuo viaggio",
  },
  packs: {
    packDesconocido: "pacchetto sconosciuto",
  },
};

const ja: typeof es = {
  borrar: {
    algoSeAtoro: "うまく処理できませんでした。もう一度お試しください",
  },
  baseline: {
    faltaPlanOFechas: "plan_idがないか、日付の形式が正しくありません",
    noPudimosSellar: "ベースラインを確定できませんでした",
  },
  modo: {
    modoInvalido: "modo_caminoが無効です。次のいずれかを使ってください：{{opciones}}",
    capacidadInvalida: "capacidad_semanalが無効です。次のいずれかを使ってください：{{opciones}}",
    nadaQueActualizar: "更新する内容がありません。modo_caminoまたはcapacidad_semanalを送ってください",
    espacioNoExiste: "そのスペースは存在しません",
  },
  checklist: {
    faltaItemId: "item_idがありません",
    estadoInvalido: "estadoが無効です。次のいずれかを使ってください：{{opciones}}",
    notaInvalida: "notaはテキストまたはnullである必要があります",
    completedAtInvalido: "completed_atは未来ではないISO形式の日付、またはnullである必要があります",
    motivoInvalido: "no_aplica_motivoはテキストまたはnullである必要があります",
    bandaInvalida: "bandaが無効です。次のいずれかを使ってください：{{opciones}}",
    fechaBaseInvalida: "fecha_baseはISO形式の日付、またはnullである必要があります",
    nadaQueActualizar: "更新する内容がありません。estado、nota、completed_at、no_aplica_motivo、fecha_base、bandaのいずれかを送ってください",
    itemNoEncontrado: "項目が見つかりません",
  },
  moverFecha: {
    faltaItemOFecha: "item_idがないか、日付の形式が正しくありません",
    actividadNoEncontrada: "アクションが見つかりません",
    yaHecha: "このアクションはすでに完了しています。別の日に行った場合は、アクションの画面から日付を変更してください。",
    retirada: "このアクションは外されています。日付を設定するには、先に元に戻してください。",
    sinFecha: "このアクションには動かせる日付がありません",
  },
  realizar: {
    accionInvalida: "操作が無効です。'realizar'または'reabrir'を使ってください",
    noPudeGuardarActa: "締めくくりの完了記録を保存できなかったため、アイデアはまだ開いたままです。少し待ってからもう一度お試しください。",
  },
  follow: {
    ideaRealizada: "このアイデアは実現済みにしています。続けて取り組む場合は、再開してください。",
    mundoCompletado: "「{{mundo}}」は完了にしています。続けて取り組む場合は、再開してください。",
    primeroExplora: "先に「{{mundo}}」を探ってください。フォローアップはそのプランから生まれます。",
    puertasRecorridas: "「{{mundo}}」の扉は、すべて巡り終えました。",
  },
  numeros: {
    cifrasNoObjeto: "'numeros'は「項目: 値」形式のオブジェクトである必要があります",
    valorInvalido: "'{{campo}}'の値は0以上の数値、または範囲{min, max}である必要があります",
    versionNoExiste: "そのバージョンは存在しません",
    activaUnaVez: "「あなたの数字」は、アイデアごとに1回だけ有効化できます。",
    noNarroInconsistente: "このデータでは結論をお伝えできません。「データの番人」を確認して、合わない数字を直してください。",
    noPudeNarrar: "今は数字の解説を書けませんでした。ダッシュボードと数字は最新の状態です。少し時間をおいて、もう一度解説を試してください。",
  },
  reporte: {
    proyectoNoEncontrado: "プロジェクトが見つかりません",
    respuestaInvalida: "'respuesta'は空でない文字列である必要があります",
    entrevistaEnCurso: "レポートのインタビューがすでに進行中です。続けるには'respuesta'を送ってください",
    sinEntrevista: "進行中のレポートのインタビューはありません。始めるには'respuesta'なしで呼び出してください",
  },
  bitacora: {
    tituloEspacio: "# {{espacio}}の活動ログ",
  },
  calendario: {
    noEncontrado: "カレンダーが見つかりません。",
    tuViaje: "あなたの旅",
  },
  packs: {
    packDesconocido: "不明なパックです",
  },
};

const zh: typeof es = {
  borrar: {
    algoSeAtoro: "出了点状况，请再试一次",
  },
  baseline: {
    faltaPlanOFechas: "缺少 plan_id，或日期格式不正确",
    noPudimosSellar: "没能锁定基线",
  },
  modo: {
    modoInvalido: "modo_camino 无效；请使用以下之一：{{opciones}}",
    capacidadInvalida: "capacidad_semanal 无效；请使用以下之一：{{opciones}}",
    nadaQueActualizar: "没有需要更新的内容：请发送 modo_camino 和/或 capacidad_semanal",
    espacioNoExiste: "这个空间不存在",
  },
  checklist: {
    faltaItemId: "缺少 item_id",
    estadoInvalido: "estado 无效；请使用以下之一：{{opciones}}",
    notaInvalida: "nota 必须是文本或 null",
    completedAtInvalido: "completed_at 必须是不晚于今天的 ISO 日期，或 null",
    motivoInvalido: "no_aplica_motivo 必须是文本或 null",
    bandaInvalida: "banda 无效；请使用以下之一：{{opciones}}",
    fechaBaseInvalida: "fecha_base 必须是 ISO 日期或 null",
    nadaQueActualizar: "没有需要更新的内容：请发送 estado、nota、completed_at、no_aplica_motivo、fecha_base 和/或 banda",
    itemNoEncontrado: "找不到该条目",
  },
  moverFecha: {
    faltaItemOFecha: "缺少 item_id，或日期格式不正确",
    actividadNoEncontrada: "找不到该活动",
    yaHecha: "这项活动已经完成了。如果你是在其他日期完成的，请在活动里修改。",
    retirada: "这项活动已被搁置。请先恢复它，才能给它定日期。",
    sinFecha: "这项活动没有可以调整的日期",
  },
  realizar: {
    accionInvalida: "操作无效；请使用 'realizar' 或 'reabrir'",
    noPudeGuardarActa: "我没能保存你的结项记录，所以你的想法仍处于开启状态。请稍后再试。",
  },
  follow: {
    ideaRealizada: "你已将想法标记为已实现。如果想继续推进，请重新开启它。",
    mundoCompletado: "你已将“{{mundo}}”标记为已完成。如果想继续推进，请重新开启它。",
    primeroExplora: "请先探索“{{mundo}}”：它的跟进源自它的计划。",
    puertasRecorridas: "“{{mundo}}”的每一扇门，你都已经走过了。",
  },
  numeros: {
    cifrasNoObjeto: "'numeros' 必须是“字段：值”形式的对象",
    valorInvalido: "'{{campo}}' 的值必须是 >= 0 的数字，或范围 {min, max}",
    versionNoExiste: "这个版本不存在",
    activaUnaVez: "每个想法只能启用一次“你的数字”。",
    noNarroInconsistente: "这些数据我没法给出结论：请查看数据守护的提示，修正对不上的数字。",
    noPudeNarrar: "我暂时没能解读你的数字。你的看板和数据都是最新的；请过一会儿再试着解读。",
  },
  reporte: {
    proyectoNoEncontrado: "找不到该项目",
    respuestaInvalida: "'respuesta' 必须是非空字符串",
    entrevistaEnCurso: "已有一场报告访谈正在进行；发送 'respuesta' 即可继续",
    sinEntrevista: "目前没有正在进行的报告访谈；不带 'respuesta' 调用即可开始",
  },
  bitacora: {
    tituloEspacio: "# {{espacio}}日志",
  },
  calendario: {
    noEncontrado: "找不到日历。",
    tuViaje: "你的旅程",
  },
  packs: {
    packDesconocido: "未知的套餐",
  },
};

const ko: typeof es = {
  borrar: {
    algoSeAtoro: "문제가 생겼어요. 다시 시도해 주세요",
  },
  baseline: {
    faltaPlanOFechas: "plan_id 값이 없거나 날짜 형식이 잘못됐어요",
    noPudimosSellar: "기준 일정을 확정하지 못했어요",
  },
  modo: {
    modoInvalido: "modo_camino 값이 잘못됐어요. 사용할 수 있는 값: {{opciones}}",
    capacidadInvalida: "capacidad_semanal 값이 잘못됐어요. 사용할 수 있는 값: {{opciones}}",
    nadaQueActualizar: "업데이트할 내용이 없어요. modo_camino, capacidad_semanal 중 하나 이상을 보내 주세요",
    espacioNoExiste: "없는 공간이에요",
  },
  checklist: {
    faltaItemId: "item_id 값이 없어요",
    estadoInvalido: "estado 값이 잘못됐어요. 사용할 수 있는 값: {{opciones}}",
    notaInvalida: "nota 값은 텍스트 또는 null이어야 해요",
    completedAtInvalido: "completed_at 값은 미래가 아닌 ISO 날짜 또는 null이어야 해요",
    motivoInvalido: "no_aplica_motivo 값은 텍스트 또는 null이어야 해요",
    bandaInvalida: "banda 값이 잘못됐어요. 사용할 수 있는 값: {{opciones}}",
    fechaBaseInvalida: "fecha_base 값은 ISO 날짜 또는 null이어야 해요",
    nadaQueActualizar: "업데이트할 내용이 없어요. estado, nota, completed_at, no_aplica_motivo, fecha_base, banda 중 하나 이상을 보내 주세요",
    itemNoEncontrado: "항목을 찾을 수 없어요",
  },
  moverFecha: {
    faltaItemOFecha: "item_id 값이 없거나 날짜 형식이 잘못됐어요",
    actividadNoEncontrada: "활동을 찾을 수 없어요",
    yaHecha: "이미 완료한 활동이에요. 다른 날에 했다면 활동에서 날짜를 바꿔 주세요.",
    retirada: "제외한 활동이에요. 날짜를 정하려면 먼저 다시 활성화해 주세요.",
    sinFecha: "이 활동에는 옮길 날짜가 없어요",
  },
  realizar: {
    accionInvalida: "잘못된 동작이에요. 'realizar', 'reabrir' 중 하나를 쓰세요",
    noPudeGuardarActa: "마무리 기록을 저장하지 못해서 아이디어는 아직 열려 있어요. 잠시 후 다시 시도해 주세요.",
  },
  follow: {
    ideaRealizada: "아이디어를 실현으로 표시했어요. 계속 다듬고 싶다면 다시 열어 주세요.",
    mundoCompletado: "“{{mundo}}” 월드를 완료로 표시했어요. 계속 다듬고 싶다면 다시 열어 주세요.",
    primeroExplora: "먼저 “{{mundo}}” 월드를 탐색해 주세요. 후속 점검은 그 계획에서 나와요.",
    puertasRecorridas: "“{{mundo}}” 월드의 문은 이미 모두 둘러봤어요.",
  },
  numeros: {
    cifrasNoObjeto: "'numeros'는 필드: 값 형태의 객체여야 해요",
    valorInvalido: "'{{campo}}' 값은 0 이상(>= 0)의 숫자 또는 {min, max} 범위여야 해요",
    versionNoExiste: "없는 버전이에요",
    activaUnaVez: "나의 숫자는 아이디어마다 한 번 활성화돼요.",
    noNarroInconsistente: "이 데이터로는 결론을 풀어 설명하지 않을게요. 데이터 지킴이를 확인하고 맞지 않는 숫자를 고쳐 주세요.",
    noPudeNarrar: "지금은 숫자를 풀어 설명하지 못했어요. 대시보드와 숫자는 최신 상태예요. 잠시 후 다시 설명을 요청해 주세요.",
  },
  reporte: {
    proyectoNoEncontrado: "프로젝트를 찾을 수 없어요",
    respuestaInvalida: "'respuesta'는 비어 있지 않은 문자열이어야 해요",
    entrevistaEnCurso: "이미 진행 중인 리포트 인터뷰가 있어요. 이어 가려면 'respuesta'를 보내 주세요",
    sinEntrevista: "진행 중인 리포트 인터뷰가 없어요. 시작하려면 'respuesta' 없이 호출해 주세요",
  },
  bitacora: {
    tituloEspacio: "# {{espacio}} 기록장",
  },
  calendario: {
    noEncontrado: "캘린더를 찾을 수 없어요.",
    tuViaje: "나의 여정",
  },
  packs: {
    packDesconocido: "알 수 없는 팩",
  },
};

const ar: typeof es = {
  borrar: {
    algoSeAtoro: "تعثّر شيء ما؛ حاولوا مرة أخرى",
  },
  baseline: {
    faltaPlanOFechas: "plan_id مفقود أو التواريخ بصيغة غير صحيحة",
    noPudimosSellar: "تعذّر تثبيت خط الأساس",
  },
  modo: {
    modoInvalido: "قيمة modo_camino غير صالحة؛ استخدموا إحدى القيم: {{opciones}}",
    capacidadInvalida: "قيمة capacidad_semanal غير صالحة؛ استخدموا إحدى القيم: {{opciones}}",
    nadaQueActualizar: "لا شيء للتحديث: أرسلوا modo_camino و/أو capacidad_semanal",
    espacioNoExiste: "هذه المساحة غير موجودة",
  },
  checklist: {
    faltaItemId: "item_id مفقود",
    estadoInvalido: "قيمة estado غير صالحة؛ استخدموا إحدى القيم: {{opciones}}",
    notaInvalida: "يجب أن تكون nota نصًا أو null",
    completedAtInvalido: "يجب أن يكون completed_at تاريخًا بصيغة ISO غير مستقبلي، أو null",
    motivoInvalido: "يجب أن يكون no_aplica_motivo نصًا أو null",
    bandaInvalida: "قيمة banda غير صالحة؛ استخدموا إحدى القيم: {{opciones}}",
    fechaBaseInvalida: "يجب أن يكون fecha_base تاريخًا بصيغة ISO أو null",
    nadaQueActualizar: "لا شيء للتحديث: أرسلوا estado، nota، completed_at، no_aplica_motivo، fecha_base و/أو banda",
    itemNoEncontrado: "العنصر غير موجود",
  },
  moverFecha: {
    faltaItemOFecha: "item_id مفقود أو التاريخ بصيغة غير صحيحة",
    actividadNoEncontrada: "المهمة غير موجودة",
    yaHecha: "هذه المهمة منجزة بالفعل. إن أنجزتموها في تاريخ آخر، فغيّروا التاريخ من صفحة المهمة نفسها.",
    retirada: "هذه المهمة مستبعدة. أعيدوا تفعيلها أولًا لتحديد تاريخ لها.",
    sinFecha: "ليس لهذه المهمة تاريخ يمكن نقله",
  },
  realizar: {
    accionInvalida: "إجراء غير صالح؛ استخدموا 'realizar' أو 'reabrir'",
    noPudeGuardarActa: "لم أتمكن من حفظ محضر إغلاق فكرتكم، لذا ما زالت مفتوحة. حاولوا مرة أخرى بعد قليل.",
  },
  follow: {
    ideaRealizada: "أعلنتم أن فكرتكم تحقّقت. أعيدوا فتحها إن أردتم مواصلة العمل عليها.",
    mundoCompletado: "أعلنتم اكتمال «{{mundo}}». أعيدوا فتحه إن أردتم مواصلة العمل عليه.",
    primeroExplora: "استكشفوا «{{mundo}}» أولًا: متابعته تنبثق من خطته.",
    puertasRecorridas: "لقد مررتم بكل أبواب «{{mundo}}».",
  },
  numeros: {
    cifrasNoObjeto: "يجب أن تكون 'numeros' كائنًا بصيغة حقل: قيمة",
    valorInvalido: "يجب أن تكون قيمة '{{campo}}' رقمًا >= 0 أو نطاقًا {min, max}",
    versionNoExiste: "هذه النسخة غير موجودة",
    activaUnaVez: "تُفعَّل «أرقامكم» مرة واحدة لكل فكرة.",
    noNarroInconsistente: "لن أصوغ استنتاجًا من هذه البيانات: راجعوا حارس البيانات وصحّحوا الرقم غير المتّسق.",
    noPudeNarrar: "لم أتمكن من شرح أرقامكم الآن. لوحتكم وأرقامكم محدّثة؛ حاولوا طلب الشرح مرة أخرى بعد قليل.",
  },
  reporte: {
    proyectoNoEncontrado: "المشروع غير موجود",
    respuestaInvalida: "يجب أن تكون 'respuesta' نصًا غير فارغ",
    entrevistaEnCurso: "هناك مقابلة تقرير جارية بالفعل؛ أرسلوا 'respuesta' لمتابعتها",
    sinEntrevista: "لا توجد مقابلة تقرير جارية؛ أرسلوا الطلب بدون 'respuesta' لبدئها",
  },
  bitacora: {
    tituloEspacio: "# سجلّ رحلة {{espacio}}",
  },
  calendario: {
    noEncontrado: "التقويم غير موجود.",
    tuViaje: "رحلتكم",
  },
  packs: {
    packDesconocido: "حزمة غير معروفة",
  },
};

const hi: typeof es = {
  borrar: {
    algoSeAtoro: "कुछ अटक गया; फिर से कोशिश करें",
  },
  baseline: {
    faltaPlanOFechas: "plan_id नहीं है या तारीखें गलत फ़ॉर्मेट में हैं",
    noPudimosSellar: "हम बेसलाइन तय नहीं कर पाए",
  },
  modo: {
    modoInvalido: "modo_camino अमान्य है; इनमें से कोई एक इस्तेमाल करें: {{opciones}}",
    capacidadInvalida: "capacidad_semanal अमान्य है; इनमें से कोई एक इस्तेमाल करें: {{opciones}}",
    nadaQueActualizar: "अपडेट करने को कुछ नहीं: modo_camino और/या capacidad_semanal भेजें",
    espacioNoExiste: "वह क्षेत्र मौजूद नहीं है",
  },
  checklist: {
    faltaItemId: "item_id नहीं है",
    estadoInvalido: "estado अमान्य है; इनमें से कोई एक इस्तेमाल करें: {{opciones}}",
    notaInvalida: "nota टेक्स्ट या null होना चाहिए",
    completedAtInvalido: "completed_at आज या उससे पहले की ISO तारीख, या null होना चाहिए",
    motivoInvalido: "no_aplica_motivo टेक्स्ट या null होना चाहिए",
    bandaInvalida: "banda अमान्य है; इनमें से कोई एक इस्तेमाल करें: {{opciones}}",
    fechaBaseInvalida: "fecha_base ISO तारीख या null होना चाहिए",
    nadaQueActualizar: "अपडेट करने को कुछ नहीं: estado, nota, completed_at, no_aplica_motivo, fecha_base और/या banda भेजें",
    itemNoEncontrado: "आइटम नहीं मिला",
  },
  moverFecha: {
    faltaItemOFecha: "item_id नहीं है या तारीख गलत फ़ॉर्मेट में है",
    actividadNoEncontrada: "गतिविधि नहीं मिली",
    yaHecha: "यह गतिविधि पहले ही पूरी हो चुकी है। अगर आपने इसे किसी और तारीख को किया था, तो गतिविधि में जाकर तारीख बदलें।",
    retirada: "यह गतिविधि अलग रखी गई है। इसे तारीख देने के लिए पहले इसे फिर से चालू करें।",
    sinFecha: "इस गतिविधि की कोई तारीख नहीं है जिसे खिसकाया जा सके",
  },
  realizar: {
    accionInvalida: "अमान्य कार्रवाई; 'realizar' या 'reabrir' इस्तेमाल करें",
    noPudeGuardarActa: "आपके समापन का रिकॉर्ड सेव नहीं हो पाया, इसलिए आपका विचार अभी खुला है। थोड़ी देर में फिर से कोशिश करें।",
  },
  follow: {
    ideaRealizada: "आपने अपने विचार को साकार मान लिया है। अगर इस पर आगे काम करना है, तो इसे फिर से खोलें।",
    mundoCompletado: "आपने “{{mundo}}” को पूरा मान लिया है। अगर इस पर आगे काम करना है, तो इसे फिर से खोलें।",
    primeroExplora: "पहले “{{mundo}}” को खोजें: इसका फ़ॉलो-अप इसकी योजना से बनता है।",
    puertasRecorridas: "“{{mundo}}” के सारे दरवाज़े आपने खोल लिए हैं।",
  },
  numeros: {
    cifrasNoObjeto: "'numeros' एक ऑब्जेक्ट होना चाहिए (फ़ील्ड: मान)",
    valorInvalido: "'{{campo}}' का मान >= 0 वाली संख्या या {min, max} रेंज होना चाहिए",
    versionNoExiste: "वह संस्करण मौजूद नहीं है",
    activaUnaVez: "“आपके आंकड़े” हर विचार के लिए एक ही बार सक्रिय होता है।",
    noNarroInconsistente: "इन आंकड़ों से कोई नतीजा नहीं निकाला जा सकता: “डेटा का पहरेदार” देखें और जो संख्या मेल नहीं खाती, उसे सुधारें।",
    noPudeNarrar: "अभी आपके आंकड़ों की कहानी नहीं लिखी जा सकी। आपका डैशबोर्ड और आंकड़े अप-टू-डेट हैं; थोड़ी देर में फिर से कोशिश करें।",
  },
  reporte: {
    proyectoNoEncontrado: "परियोजना नहीं मिली",
    respuestaInvalida: "'respuesta' एक string होना चाहिए, खाली नहीं",
    entrevistaEnCurso: "रिपोर्ट की एक बातचीत पहले से चल रही है; उसे जारी रखने के लिए 'respuesta' भेजें",
    sinEntrevista: "रिपोर्ट की कोई बातचीत नहीं चल रही; शुरू करने के लिए 'respuesta' के बिना कॉल करें",
  },
  bitacora: {
    tituloEspacio: "# {{espacio}} की लॉगबुक",
  },
  calendario: {
    noEncontrado: "कैलेंडर नहीं मिला।",
    tuViaje: "आपकी यात्रा",
  },
  packs: {
    packDesconocido: "अज्ञात पैक",
  },
};

export const SERVIDOR_PROYECTO: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
