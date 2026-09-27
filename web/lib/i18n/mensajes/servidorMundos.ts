/** Rutas de /api/project/[id]/world/[pack]/* (abrir, explorar, diagnosticar y cerrar un mundo). */
import type { PorIdioma } from "../config";

const es = {
  unlock: {
    noPudimosActivar: "no pudimos activar el mundo, intenta de nuevo",
  },
  start: {
    diagnosticoListo:
      'Tu diagnóstico de "{{mundo}}" ya está listo: puedes releerlo y generar su plan cuando quieras. ' +
      "Cuando tu proyecto avance de ciclo, podrás explorarlo de nuevo gratis.",
    puertasRecorridas: "Ya recorriste todas las puertas de este mundo.",
    preparando: "Este mundo se está preparando. Muy pronto podrás explorarlo.",
    noPudimosAbrir: "no pudimos abrir el mundo, intenta de nuevo",
  },
  completar: {
    accionInvalida: "acción inválida; usa 'completar' o 'reabrir'",
    noPudeGuardarActa:
      'No pude guardar el acta del cierre de "{{mundo}}", así que sigue abierto. Intenta de nuevo en un momento.',
    noPudimosGuardar: "no pudimos guardar; intenta de nuevo",
  },
  diagnostico: {
    sinExploracion: "No encontré la exploración de este mundo. Vuelve a explorarlo desde su espacio.",
    sinRespuestas: "Esta exploración todavía no tiene respuestas que diagnosticar.",
    esSeguimiento: "Este es un ciclo de seguimiento: termina en tu plan, no en un diagnóstico.",
    noPudimosRedactar: "no pudimos redactar tu diagnóstico; intenta de nuevo en un momento",
    noPudimosGuardar: "no pudimos guardar tu diagnóstico; intenta de nuevo",
  },
};

const en: typeof es = {
  unlock: {
    noPudimosActivar: "we couldn't activate the world, try again",
  },
  start: {
    diagnosticoListo:
      'Your "{{mundo}}" diagnosis is ready: you can reread it and generate its plan whenever you want. ' +
      "When your project moves on to its next cycle, you'll be able to explore it again for free.",
    puertasRecorridas: "You've already been through every door in this world.",
    preparando: "This world is still being prepared. You'll be able to explore it very soon.",
    noPudimosAbrir: "we couldn't open the world, try again",
  },
  completar: {
    accionInvalida: "invalid action; use 'completar' or 'reabrir'",
    noPudeGuardarActa:
      'I couldn\'t save the closing record for "{{mundo}}", so it\'s still open. Try again in a moment.',
    noPudimosGuardar: "we couldn't save; try again",
  },
  diagnostico: {
    sinExploracion: "I couldn't find this world's exploration. Explore it again from its space.",
    sinRespuestas: "This exploration doesn't have any answers to diagnose yet.",
    esSeguimiento: "This is a follow-up cycle: it ends in your plan, not in a diagnosis.",
    noPudimosRedactar: "we couldn't write your diagnosis; try again in a moment",
    noPudimosGuardar: "we couldn't save your diagnosis; try again",
  },
};

const fr: typeof es = {
  unlock: {
    noPudimosActivar: "nous n'avons pas pu activer le monde, réessaie",
  },
  start: {
    diagnosticoListo: "Ton diagnostic « {{mundo}} » est prêt : tu peux le relire et générer son plan quand tu veux. Quand ton projet passera au cycle suivant, tu pourras l'explorer de nouveau gratuitement.",
    puertasRecorridas: "Tu as déjà franchi toutes les portes de ce monde.",
    preparando: "Ce monde est en préparation. Tu pourras l'explorer très bientôt.",
    noPudimosAbrir: "nous n'avons pas pu ouvrir le monde, réessaie",
  },
  completar: {
    accionInvalida: "action invalide; utilise 'completar' ou 'reabrir'",
    noPudeGuardarActa: "Je n'ai pas pu enregistrer le bilan de clôture de « {{mundo}} », alors il reste ouvert. Réessaie dans un instant.",
    noPudimosGuardar: "nous n'avons pas pu enregistrer; réessaie",
  },
  diagnostico: {
    sinExploracion: "Je n'ai pas trouvé l'exploration de ce monde. Explore-le de nouveau depuis son espace.",
    sinRespuestas: "Cette exploration n'a pas encore de réponses à diagnostiquer.",
    esSeguimiento: "C'est un cycle de suivi : il se termine par ton plan, pas par un diagnostic.",
    noPudimosRedactar: "nous n'avons pas pu rédiger ton diagnostic; réessaie dans un instant",
    noPudimosGuardar: "nous n'avons pas pu enregistrer ton diagnostic; réessaie",
  },
};

const pt: typeof es = {
  unlock: {
    noPudimosActivar: "não conseguimos ativar o mundo, tente de novo",
  },
  start: {
    diagnosticoListo: "Seu diagnóstico de \"{{mundo}}\" já está pronto: você pode relê-lo e gerar o plano dele quando quiser. Quando seu projeto avançar de ciclo, você poderá explorá-lo de novo de graça.",
    puertasRecorridas: "Você já passou por todas as portas deste mundo.",
    preparando: "Este mundo está sendo preparado. Muito em breve você poderá explorá-lo.",
    noPudimosAbrir: "não conseguimos abrir o mundo, tente de novo",
  },
  completar: {
    accionInvalida: "ação inválida; use 'completar' ou 'reabrir'",
    noPudeGuardarActa: "Não consegui salvar a ata de encerramento de \"{{mundo}}\", então ele continua aberto. Tente de novo daqui a pouco.",
    noPudimosGuardar: "não conseguimos salvar; tente de novo",
  },
  diagnostico: {
    sinExploracion: "Não encontrei a exploração deste mundo. Explore-o de novo a partir do espaço dele.",
    sinRespuestas: "Esta exploração ainda não tem respostas para diagnosticar.",
    esSeguimiento: "Este é um ciclo de acompanhamento: termina no seu plano, não em um diagnóstico.",
    noPudimosRedactar: "não conseguimos escrever seu diagnóstico; tente de novo daqui a pouco",
    noPudimosGuardar: "não conseguimos salvar seu diagnóstico; tente de novo",
  },
};

const de: typeof es = {
  unlock: {
    noPudimosActivar: "wir konnten die Welt nicht aktivieren, versuch es noch einmal",
  },
  start: {
    diagnosticoListo: "Deine Diagnose für „{{mundo}}“ ist fertig: Du kannst sie jederzeit wieder lesen und den Plan dazu erstellen. Wenn dein Projekt in den nächsten Zyklus geht, kannst du diese Welt erneut kostenlos erkunden.",
    puertasRecorridas: "Du bist schon durch alle Türen dieser Welt gegangen.",
    preparando: "Diese Welt wird gerade vorbereitet. Schon bald kannst du sie erkunden.",
    noPudimosAbrir: "wir konnten die Welt nicht öffnen, versuch es noch einmal",
  },
  completar: {
    accionInvalida: "ungültige Aktion; nutze 'completar' oder 'reabrir'",
    noPudeGuardarActa: "Ich konnte das Abschlussprotokoll für „{{mundo}}“ nicht speichern, deshalb bleibt die Welt offen. Versuch es gleich noch einmal.",
    noPudimosGuardar: "wir konnten nicht speichern; versuch es noch einmal",
  },
  diagnostico: {
    sinExploracion: "Ich habe die Erkundung dieser Welt nicht gefunden. Erkunde sie noch einmal von ihrem Bereich aus.",
    sinRespuestas: "Diese Erkundung hat noch keine Antworten, aus denen sich eine Diagnose erstellen lässt.",
    esSeguimiento: "Dieser Zyklus gehört zu einem Zwischenstand: Er endet in deinem Plan, nicht in einer Diagnose.",
    noPudimosRedactar: "wir konnten deine Diagnose nicht schreiben; versuch es gleich noch einmal",
    noPudimosGuardar: "wir konnten deine Diagnose nicht speichern; versuch es noch einmal",
  },
};

const it: typeof es = {
  unlock: {
    noPudimosActivar: "non siamo riusciti ad attivare il mondo, riprova",
  },
  start: {
    diagnosticoListo: "La tua diagnosi di \"{{mundo}}\" è pronta: puoi rileggerla e generare il suo piano quando vuoi. Quando il tuo progetto passerà al ciclo successivo, potrai esplorare di nuovo questo mondo gratis.",
    puertasRecorridas: "Hai già attraversato tutte le porte di questo mondo.",
    preparando: "Questo mondo è in preparazione. Molto presto potrai esplorarlo.",
    noPudimosAbrir: "non siamo riusciti ad aprire il mondo, riprova",
  },
  completar: {
    accionInvalida: "azione non valida; usa 'completar' o 'reabrir'",
    noPudeGuardarActa: "Non ho potuto salvare il verbale di chiusura di \"{{mundo}}\", quindi resta aperto. Riprova tra un momento.",
    noPudimosGuardar: "non siamo riusciti a salvare; riprova",
  },
  diagnostico: {
    sinExploracion: "Non ho trovato l'esplorazione di questo mondo. Esploralo di nuovo dal suo spazio.",
    sinRespuestas: "Questa esplorazione non ha ancora risposte da diagnosticare.",
    esSeguimiento: "Questo è un ciclo di revisione: finisce nel tuo piano, non in una diagnosi.",
    noPudimosRedactar: "non siamo riusciti a scrivere la tua diagnosi; riprova tra un momento",
    noPudimosGuardar: "non siamo riusciti a salvare la tua diagnosi; riprova",
  },
};

const ja: typeof es = {
  unlock: {
    noPudimosActivar: "ワールドを有効にできませんでした。もう一度お試しください",
  },
  start: {
    diagnosticoListo: "「{{mundo}}」の診断ができあがりました。いつでも読み返して、そのプランを作成できます。プロジェクトが次のサイクルに進んだら、もう一度無料で探求できます。",
    puertasRecorridas: "このワールドの扉は、すべて巡り終えました。",
    preparando: "このワールドは準備中です。もうすぐ探求できるようになります。",
    noPudimosAbrir: "ワールドを開けませんでした。もう一度お試しください",
  },
  completar: {
    accionInvalida: "無効なアクションです。'completar' か 'reabrir' を使ってください",
    noPudeGuardarActa: "「{{mundo}}」の完了記録を保存できなかったため、まだ開いたままです。少し待ってからもう一度お試しください。",
    noPudimosGuardar: "保存できませんでした。もう一度お試しください",
  },
  diagnostico: {
    sinExploracion: "このワールドの探求が見つかりませんでした。そのスペースから、もう一度探求してください。",
    sinRespuestas: "この探求には、まだ診断できる回答がありません。",
    esSeguimiento: "これはフォローアップのサイクルです。行き着く先は診断ではなく、プランです。",
    noPudimosRedactar: "診断を書き上げられませんでした。少し待ってからもう一度お試しください",
    noPudimosGuardar: "診断を保存できませんでした。もう一度お試しください",
  },
};

const zh: typeof es = {
  unlock: {
    noPudimosActivar: "我们没能开启这个世界，请再试一次",
  },
  start: {
    diagnosticoListo: "你的“{{mundo}}”诊断已经准备好了：你可以随时重读，也可以随时生成它的计划。等你的项目进入下一个周期，你可以再次免费探索它。",
    puertasRecorridas: "这个世界的每一扇门你都已经走过了。",
    preparando: "这个世界还在准备中。很快你就能探索了。",
    noPudimosAbrir: "我们没能打开这个世界，请再试一次",
  },
  completar: {
    accionInvalida: "无效的操作；请使用 'completar' 或 'reabrir'",
    noPudeGuardarActa: "我没能保存“{{mundo}}”的结项记录，所以它仍处于开启状态。请稍后再试。",
    noPudimosGuardar: "我们没能保存，请再试一次",
  },
  diagnostico: {
    sinExploracion: "我没找到这个世界的探索记录。请从它的空间重新探索。",
    sinRespuestas: "这次探索还没有可以诊断的回答。",
    esSeguimiento: "这是一个跟进周期：它的终点是你的计划，而不是诊断。",
    noPudimosRedactar: "我们没能写出你的诊断，请稍后再试",
    noPudimosGuardar: "我们没能保存你的诊断，请再试一次",
  },
};

const ko: typeof es = {
  unlock: {
    noPudimosActivar: "월드를 활성화하지 못했어요. 다시 시도해 주세요",
  },
  start: {
    diagnosticoListo: "“{{mundo}}” 진단이 준비됐어요. 언제든 다시 읽고 그 계획을 만들 수 있어요. 프로젝트가 다음 사이클로 넘어가면 다시 무료로 탐색할 수 있어요.",
    puertasRecorridas: "이 월드의 문은 이미 모두 둘러봤어요.",
    preparando: "이 월드는 아직 준비 중이에요. 곧 탐색할 수 있어요.",
    noPudimosAbrir: "월드를 열지 못했어요. 다시 시도해 주세요",
  },
  completar: {
    accionInvalida: "잘못된 요청이에요. 'completar' 또는 'reabrir'를 사용하세요",
    noPudeGuardarActa: "“{{mundo}}”의 마무리 기록을 저장하지 못해서 아직 열려 있어요. 잠시 후 다시 시도해 주세요.",
    noPudimosGuardar: "저장하지 못했어요. 다시 시도해 주세요",
  },
  diagnostico: {
    sinExploracion: "이 월드의 탐색 기록을 찾지 못했어요. 월드 공간에서 다시 탐색해 주세요.",
    sinRespuestas: "이 탐색에는 아직 진단할 답변이 없어요.",
    esSeguimiento: "이건 후속 점검 사이클이에요. 진단이 아니라 계획으로 끝나요.",
    noPudimosRedactar: "진단을 작성하지 못했어요. 잠시 후 다시 시도해 주세요",
    noPudimosGuardar: "진단을 저장하지 못했어요. 다시 시도해 주세요",
  },
};

const ar: typeof es = {
  unlock: {
    noPudimosActivar: "لم نتمكّن من تفعيل العالم، حاولوا مجددًا",
  },
  start: {
    diagnosticoListo: "تشخيصكم لعالم «{{mundo}}» جاهز: يمكنكم إعادة قراءته وإنشاء خطته متى شئتم. وحين ينتقل مشروعكم إلى دورته التالية، ستتمكّنون من استكشافه مجددًا مجانًا.",
    puertasRecorridas: "لقد عبرتم بالفعل كل أبواب هذا العالم.",
    preparando: "هذا العالم قيد التجهيز. قريبًا جدًا ستتمكّنون من استكشافه.",
    noPudimosAbrir: "لم نتمكّن من فتح العالم، حاولوا مجددًا",
  },
  completar: {
    accionInvalida: "إجراء غير صالح؛ استخدموا 'completar' أو 'reabrir'",
    noPudeGuardarActa: "لم أتمكّن من حفظ محضر إغلاق «{{mundo}}»، لذا يبقى مفتوحًا. حاولوا مجددًا بعد لحظات.",
    noPudimosGuardar: "لم نتمكّن من الحفظ؛ حاولوا مجددًا",
  },
  diagnostico: {
    sinExploracion: "لم أعثر على استكشاف هذا العالم. استكشفوه مجددًا من مساحته.",
    sinRespuestas: "لا تتضمّن هذه الجولة من الاستكشاف بعد إجابات يمكن تشخيصها.",
    esSeguimiento: "هذه دورة متابعة: تنتهي بخطتكم، لا بتشخيص.",
    noPudimosRedactar: "لم نتمكّن من كتابة تشخيصكم؛ حاولوا مجددًا بعد لحظات",
    noPudimosGuardar: "لم نتمكّن من حفظ تشخيصكم؛ حاولوا مجددًا",
  },
};

const hi: typeof es = {
  unlock: {
    noPudimosActivar: "हम दुनिया सक्रिय नहीं कर सके, फिर से कोशिश करें",
  },
  start: {
    diagnosticoListo: "“{{mundo}}” का आपका आकलन तैयार है: इसे जब चाहें फिर से पढ़ें और इसकी योजना बनाएँ। जब आपकी परियोजना अगले चक्र में पहुँचेगी, तो इस दुनिया की फिर से मुफ़्त में खोजबीन की जा सकेगी।",
    puertasRecorridas: "इस दुनिया के सारे दरवाज़े आपने खोल लिए हैं।",
    preparando: "यह दुनिया अभी तैयार हो रही है। बहुत जल्द इसकी खोजबीन की जा सकेगी।",
    noPudimosAbrir: "हम दुनिया नहीं खोल सके, फिर से कोशिश करें",
  },
  completar: {
    accionInvalida: "अमान्य कार्रवाई; 'completar' या 'reabrir' इस्तेमाल करें",
    noPudeGuardarActa: "“{{mundo}}” का समापन रिकॉर्ड सहेजा नहीं जा सका, इसलिए यह दुनिया अभी खुली है। थोड़ी देर में फिर से कोशिश करें।",
    noPudimosGuardar: "हम सहेज नहीं सके; फिर से कोशिश करें",
  },
  diagnostico: {
    sinExploracion: "इस दुनिया की खोजबीन नहीं मिली। इसके क्षेत्र से इसकी फिर से खोजबीन करें।",
    sinRespuestas: "इस खोजबीन में अभी ऐसे कोई जवाब नहीं हैं जिनका आकलन किया जा सके।",
    esSeguimiento: "यह एक फ़ॉलो-अप चक्र है: यह आपकी योजना पर खत्म होता है, आकलन पर नहीं।",
    noPudimosRedactar: "हम आपका आकलन नहीं लिख सके; थोड़ी देर में फिर से कोशिश करें",
    noPudimosGuardar: "हम आपका आकलन सहेज नहीं सके; फिर से कोशिश करें",
  },
};

export const SERVIDOR_MUNDOS: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
