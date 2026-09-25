/** Rutas de la entrevista (/api/session/*), del organizador (/api/organizer*) y los cierres honestos de lib/apiSesion.ts. */
import type { PorIdioma } from "../config";

const es = {
  turno: {
    faltaRespuesta: "falta 'respuesta'",
  },
  regenerar: {
    noEncontrePlan: "No encontré ese plan.",
    planCompleto: "Este plan ya está completo: no hay nada que regenerar.",
  },
  plan: {
    noPudeTerminar: "No pude terminar de escribir tu plan. Lo que contaste está guardado; intenta de nuevo.",
  },
  organizador: {
    noPudeOrganizar: "No pude organizar tu idea en este momento. Intenta de nuevo en un rato.",
    yaOrdenada: "Esta idea ya está ordenada.",
    truncado:
      "tu idea trae mucho y se pasó de lo que puedo organizar de una sola vez; recórtala un poco o cuéntamela por partes e intenta de nuevo",
    noPudimosOrganizar: "no pudimos organizar tu idea en este momento; tu texto quedó guardado, intenta de nuevo",
  },
  /** FASE B (canon 12): el cierre honesto, título y cuerpo (apiSesion.ts). */
  cierre: {
    caminoTitulo: "Por aquí no encuentro un plan que valga tu tiempo.",
    caminoCuerpo:
      "Exploré lo que me contaste y, siendo honesto, este ángulo no me da material suficiente para " +
      "armarte un plan que de verdad te mueva. Prefiero decírtelo a entregarte relleno. No es un no a " +
      "tu idea: es un no a este camino.",
    mundoTitulo: "{{nombre}} no es para esta idea, todavía.",
    mundoCuerpo:
      "Activé y exploré este mundo con lo que hay hoy, y no encontré un subproyecto que te sume sin " +
      "inventarte trabajo. Antes que darte un checklist de relleno, prefiero parar aquí. Este mundo te " +
      "sigue esperando: puedes volver a entrar cuando tu proyecto crezca.",
    mundoSinNombre: "Este mundo",
    seguimientoTitulo: "En este ciclo no encontré una puerta nueva en {{nombre}}.",
    seguimientoCuerpo:
      "Revisé lo que me contaste y no encontré algo nuevo que valga un plan en este mundo sin " +
      "inventarte trabajo. Tu plan y tu avance en este mundo siguen intactos: puedes seguir con " +
      "ellos y volver a contarme cuando haya novedades.",
    seguimientoSinNombre: "este mundo",
  },
};

const en: typeof es = {
  turno: {
    faltaRespuesta: "missing 'respuesta'",
  },
  regenerar: {
    noEncontrePlan: "I couldn't find that plan.",
    planCompleto: "This plan is already complete: there's nothing to regenerate.",
  },
  plan: {
    noPudeTerminar: "I couldn't finish writing your plan. What you told me is saved; try again.",
  },
  organizador: {
    noPudeOrganizar: "I couldn't organize your idea right now. Try again in a little while.",
    yaOrdenada: "This idea is already organized.",
    truncado:
      "your idea has a lot in it, more than I can organize in one go; trim it a little or tell it to me in parts and try again",
    noPudimosOrganizar: "we couldn't organize your idea right now; your text is saved, try again",
  },
  cierre: {
    caminoTitulo: "Down this path, I can't find a plan that's worth your time.",
    caminoCuerpo:
      "I explored what you told me and, to be honest, this angle doesn't give me enough material to " +
      "build you a plan that would really move you forward. I'd rather tell you than hand you filler. It's not a no to " +
      "your idea: it's a no to this path.",
    mundoTitulo: "{{nombre}} isn't for this idea, not yet.",
    mundoCuerpo:
      "I activated and explored this world with what you have today, and I didn't find a subproject that adds real value without " +
      "inventing busywork for you. Rather than give you a filler checklist, I'd rather stop here. This world is " +
      "still waiting for you: you can come back in when your project grows.",
    mundoSinNombre: "This world",
    seguimientoTitulo: "This cycle, I didn't find a new door in {{nombre}}.",
    seguimientoCuerpo:
      "I went over what you told me and didn't find anything new that's worth a plan in this world without " +
      "inventing busywork for you. Your plan and your progress in this world are still intact: you can keep going with " +
      "them and come back to tell me when there's news.",
    seguimientoSinNombre: "this world",
  },
};

const fr: typeof es = {
  turno: {
    faltaRespuesta: "il manque 'respuesta'",
  },
  regenerar: {
    noEncontrePlan: "Je n'ai pas trouvé ce plan.",
    planCompleto: "Ce plan est déjà complet : il n'y a rien à régénérer.",
  },
  plan: {
    noPudeTerminar: "Je n'ai pas pu finir de rédiger ton plan. Ce que tu m'as raconté est enregistré; réessaie.",
  },
  organizador: {
    noPudeOrganizar: "Je n'ai pas pu organiser ton idée pour le moment. Réessaie un peu plus tard.",
    yaOrdenada: "Cette idée est déjà organisée.",
    truncado: "ton idée contient beaucoup de choses, plus que je ne peux en organiser d'un seul coup; raccourcis-la un peu ou raconte-la-moi en plusieurs parties, puis réessaie",
    noPudimosOrganizar: "nous n'avons pas pu organiser ton idée pour le moment; ton texte est enregistré, réessaie",
  },
  cierre: {
    caminoTitulo: "Par ici, je ne trouve pas de plan qui vaille ton temps.",
    caminoCuerpo: "J'ai exploré ce que tu m'as raconté et, pour être honnête, cet angle ne me donne pas assez de matière pour te bâtir un plan qui te fasse vraiment avancer. Je préfère te le dire plutôt que de te livrer du remplissage. Ce n'est pas un non à ton idée : c'est un non à ce chemin.",
    mundoTitulo: "{{nombre}} n'est pas pour cette idée, pas encore.",
    mundoCuerpo: "J'ai activé et exploré ce monde avec ce qu'il y a aujourd'hui, et je n'ai pas trouvé de sous-projet qui t'apporte quelque chose sans t'inventer du travail. Plutôt que de te donner une liste d'actions pour faire du remplissage, je préfère m'arrêter ici. Ce monde t'attend toujours : tu pourras y revenir quand ton projet grandira.",
    mundoSinNombre: "Ce monde",
    seguimientoTitulo: "Dans ce cycle, je n'ai pas trouvé de nouvelle porte dans {{nombre}}.",
    seguimientoCuerpo: "J'ai revu ce que tu m'as raconté et je n'ai rien trouvé de nouveau qui vaille un plan dans ce monde sans t'inventer du travail. Ton plan et ton avancement dans ce monde restent intacts : tu peux continuer avec eux et revenir m'en parler quand il y aura du nouveau.",
    seguimientoSinNombre: "ce monde",
  },
};

const pt: typeof es = {
  turno: {
    faltaRespuesta: "falta 'respuesta'",
  },
  regenerar: {
    noEncontrePlan: "Não encontrei esse plano.",
    planCompleto: "Este plano já está completo: não há nada para regenerar.",
  },
  plan: {
    noPudeTerminar: "Não consegui terminar de escrever seu plano. O que você contou está salvo; tente de novo.",
  },
  organizador: {
    noPudeOrganizar: "Não consegui organizar sua ideia agora. Tente de novo daqui a pouco.",
    yaOrdenada: "Esta ideia já está organizada.",
    truncado: "sua ideia tem muita coisa e passou do que consigo organizar de uma vez só; encurte um pouco ou me conte por partes e tente de novo",
    noPudimosOrganizar: "não conseguimos organizar sua ideia agora; seu texto ficou salvo, tente de novo",
  },
  cierre: {
    caminoTitulo: "Por aqui não encontro um plano que valha o seu tempo.",
    caminoCuerpo: "Explorei o que você me contou e, sendo honesto, este ângulo não me dá material suficiente para montar um plano que realmente faça você avançar. Prefiro te dizer isso a te entregar algo só para encher espaço. Não é um não para a sua ideia: é um não para este caminho.",
    mundoTitulo: "{{nombre}} não é para esta ideia, por enquanto.",
    mundoCuerpo: "Ativei e explorei este mundo com o que existe hoje, e não encontrei um subprojeto que acrescente algo de verdade sem inventar trabalho para você. Em vez de te dar um checklist só para encher espaço, prefiro parar aqui. Este mundo continua esperando por você: você pode voltar a entrar quando seu projeto crescer.",
    mundoSinNombre: "Este mundo",
    seguimientoTitulo: "Neste ciclo não encontrei uma porta nova em {{nombre}}.",
    seguimientoCuerpo: "Revisei o que você me contou e não encontrei nada novo que valha um plano neste mundo sem inventar trabalho para você. Seu plano e seu avanço neste mundo continuam intactos: você pode seguir com eles e voltar a me contar quando houver novidades.",
    seguimientoSinNombre: "este mundo",
  },
};

const de: typeof es = {
  turno: {
    faltaRespuesta: "'respuesta' fehlt",
  },
  regenerar: {
    noEncontrePlan: "Ich habe diesen Plan nicht gefunden.",
    planCompleto: "Dieser Plan ist schon vollständig: Es gibt nichts neu zu erstellen.",
  },
  plan: {
    noPudeTerminar: "Ich konnte deinen Plan nicht fertig schreiben. Was du erzählt hast, ist gespeichert; versuch es noch einmal.",
  },
  organizador: {
    noPudeOrganizar: "Ich konnte deine Idee gerade nicht ordnen. Versuch es in einer Weile noch einmal.",
    yaOrdenada: "Diese Idee ist schon geordnet.",
    truncado: "in deiner Idee steckt so viel, dass ich sie nicht auf einmal ordnen kann; kürze sie ein wenig oder erzähl sie mir in Teilen und versuch es noch einmal",
    noPudimosOrganizar: "wir konnten deine Idee gerade nicht ordnen; dein Text ist gespeichert, versuch es noch einmal",
  },
  cierre: {
    caminoTitulo: "Auf diesem Weg finde ich keinen Plan, der deine Zeit wert ist.",
    caminoCuerpo: "Ich habe erkundet, was du mir erzählt hast, und ehrlich gesagt gibt mir dieser Blickwinkel nicht genug Stoff, um dir einen Plan zu bauen, der dich wirklich weiterbringt. Das sage ich dir lieber, als dir Füllmaterial zu geben. Das ist kein Nein zu deiner Idee: Es ist ein Nein zu diesem Weg.",
    mundoTitulo: "{{nombre}} passt noch nicht zu dieser Idee.",
    mundoCuerpo: "Ich habe diese Welt mit dem aktiviert und erkundet, was heute da ist, und kein Teilprojekt gefunden, das dich weiterbringt, ohne dir unnötige Arbeit auszudenken. Statt dir eine Checkliste voller Füllmaterial zu geben, höre ich lieber hier auf. Diese Welt wartet weiter auf dich: Du kannst wiederkommen, wenn dein Projekt wächst.",
    mundoSinNombre: "Diese Welt",
    seguimientoTitulo: "In dieser Runde habe ich in {{nombre}} keine neue Tür gefunden.",
    seguimientoCuerpo: "Ich habe durchgesehen, was du mir erzählt hast, und nichts Neues gefunden, das in dieser Welt einen Plan wert ist, ohne dir unnötige Arbeit auszudenken. Dein Plan und dein Fortschritt in dieser Welt bleiben unberührt: Du kannst damit weitermachen und mir wieder erzählen, wenn es Neues gibt.",
    seguimientoSinNombre: "diese Welt",
  },
};

const it: typeof es = {
  turno: {
    faltaRespuesta: "manca 'respuesta'",
  },
  regenerar: {
    noEncontrePlan: "Non ho trovato questo piano.",
    planCompleto: "Questo piano è già completo: non c'è niente da rigenerare.",
  },
  plan: {
    noPudeTerminar: "Non sono riuscito a finire di scrivere il tuo piano. Quello che mi hai raccontato è salvato; riprova.",
  },
  organizador: {
    noPudeOrganizar: "Non sono riuscito a organizzare la tua idea in questo momento. Riprova tra un po'.",
    yaOrdenada: "Questa idea è già in ordine.",
    truncado: "la tua idea è così ricca che supera quello che riesco a organizzare in una volta sola; accorciala un po' o raccontamela a pezzi e riprova",
    noPudimosOrganizar: "non siamo riusciti a organizzare la tua idea in questo momento; il tuo testo è salvato, riprova",
  },
  cierre: {
    caminoTitulo: "Su questa strada non trovo un piano che valga il tuo tempo.",
    caminoCuerpo: "Ho esplorato quello che mi hai raccontato e, a essere onesto, questa angolazione non mi dà abbastanza materiale per costruirti un piano che ti faccia davvero avanzare. Preferisco dirtelo piuttosto che darti del riempitivo. Non è un no alla tua idea: è un no a questa strada.",
    mundoTitulo: "{{nombre}} non fa per questa idea, per ora.",
    mundoCuerpo: "Ho attivato ed esplorato questo mondo con quello che c'è oggi, e non ho trovato un sottoprogetto che ti dia qualcosa in più senza inventarti lavoro. Piuttosto che darti una checklist di riempitivo, preferisco fermarmi qui. Questo mondo continua ad aspettarti: puoi rientrarci quando il tuo progetto crescerà.",
    mundoSinNombre: "Questo mondo",
    seguimientoTitulo: "In questo ciclo non ho trovato una porta nuova in {{nombre}}.",
    seguimientoCuerpo: "Ho rivisto quello che mi hai raccontato e non ho trovato niente di nuovo che valga un piano in questo mondo senza inventarti lavoro. Il tuo piano e i tuoi progressi in questo mondo restano intatti: puoi andare avanti con loro e tornare a raccontarmi quando ci saranno novità.",
    seguimientoSinNombre: "questo mondo",
  },
};

const ja: typeof es = {
  turno: {
    faltaRespuesta: "'respuesta'がありません",
  },
  regenerar: {
    noEncontrePlan: "そのプランが見つかりませんでした。",
    planCompleto: "このプランはすでに完成しています。作り直すものはありません。",
  },
  plan: {
    noPudeTerminar: "プランを最後まで書けませんでした。話してくれた内容は保存されています。もう一度お試しください。",
  },
  organizador: {
    noPudeOrganizar: "今はアイデアを整理できませんでした。少し時間をおいて、もう一度お試しください。",
    yaOrdenada: "このアイデアはすでに整理されています。",
    truncado: "アイデアの内容が多く、一度に整理できる量を超えました。少し短くするか、何回かに分けて教えてから、もう一度お試しください",
    noPudimosOrganizar: "今はアイデアを整理できませんでした。文章は保存されているので、もう一度お試しください",
  },
  cierre: {
    caminoTitulo: "この方向では、時間をかける価値のあるプランが見つかりません。",
    caminoCuerpo: "話してくれたことを探ってみましたが、正直に言うと、この角度からは本当に前に進めるプランを作るだけの材料がありません。中身のないものを渡すより、そうお伝えしたいと思います。アイデアへの「ノー」ではありません。この道筋への「ノー」です。",
    mundoTitulo: "{{nombre}}は、このアイデアにはまだ早いようです。",
    mundoCuerpo: "今ある情報でこのワールドを有効化して探ってみましたが、余計な作業を作らずに役立つサブプロジェクトは見つかりませんでした。水増しのチェックリストを渡すより、ここで止めたいと思います。このワールドはこれからも待っています。プロジェクトが育ったら、また入ってきてください。",
    mundoSinNombre: "このワールド",
    seguimientoTitulo: "今回のサイクルでは、{{nombre}}に新しい扉は見つかりませんでした。",
    seguimientoCuerpo: "話してくれたことを見直しましたが、余計な作業を作らずに、このワールドでプランにする価値のある新しいことは見つかりませんでした。このワールドのプランと進み具合はそのままです。このまま続けて、何か動きがあったらまた教えてください。",
    seguimientoSinNombre: "このワールド",
  },
};

const zh: typeof es = {
  turno: {
    faltaRespuesta: "缺少 'respuesta'",
  },
  regenerar: {
    noEncontrePlan: "我没找到这个计划。",
    planCompleto: "这个计划已经完整了：没有需要重新生成的内容。",
  },
  plan: {
    noPudeTerminar: "我没能写完你的计划。你说的内容都已保存；请再试一次。",
  },
  organizador: {
    noPudeOrganizar: "我暂时没能整理你的想法。请过一会儿再试。",
    yaOrdenada: "这个想法已经整理好了。",
    truncado: "你的想法内容很多，超出了我一次能整理的量；请稍微精简一下，或者分几次告诉我，然后再试一次",
    noPudimosOrganizar: "我们暂时没能整理你的想法；你的文字已保存，请再试一次",
  },
  cierre: {
    caminoTitulo: "沿着这条路，我找不到值得你花时间的计划。",
    caminoCuerpo: "我探索了你告诉我的内容，坦白说，这个角度给我的素材不够，没法为你制定一个真正能推动你的计划。与其给你凑数的东西，我宁愿直说。这不是否定你的想法：只是这条路走不通。",
    mundoTitulo: "{{nombre}}暂时还不适合这个想法。",
    mundoCuerpo: "我根据你现在的情况开启并探索了这个世界，没有找到一个既能帮到你、又不是凭空给你加活的子项目。与其给你一份凑数的清单，我宁愿在这里停下。这个世界会一直等你：等你的项目成长了，随时可以回来。",
    mundoSinNombre: "这个世界",
    seguimientoTitulo: "这一轮，我在{{nombre}}里没有找到新的门。",
    seguimientoCuerpo: "我看了你告诉我的内容，在这个世界里没有找到值得做成计划、又不是凭空给你加活的新东西。你在这个世界的计划和进展都完好无损：你可以继续推进，有新情况时再来告诉我。",
    seguimientoSinNombre: "这个世界",
  },
};

const ko: typeof es = {
  turno: {
    faltaRespuesta: "'respuesta' 값이 없어요",
  },
  regenerar: {
    noEncontrePlan: "그 계획을 찾지 못했어요.",
    planCompleto: "이 계획은 이미 완성됐어요. 다시 만들 부분이 없어요.",
  },
  plan: {
    noPudeTerminar: "계획을 끝까지 쓰지 못했어요. 들려준 내용은 저장돼 있으니 다시 시도해 주세요.",
  },
  organizador: {
    noPudeOrganizar: "지금은 아이디어를 정리하지 못했어요. 잠시 후 다시 시도해 주세요.",
    yaOrdenada: "이미 정리된 아이디어예요.",
    truncado: "아이디어에 담긴 내용이 많아서 한 번에 정리할 수 있는 양을 넘었어요. 조금 줄이거나 나눠서 들려준 뒤 다시 시도해 주세요",
    noPudimosOrganizar: "지금은 아이디어를 정리하지 못했어요. 쓰신 내용은 저장됐으니 다시 시도해 주세요",
  },
  cierre: {
    caminoTitulo: "이 방향에서는 시간을 들일 만한 계획이 보이지 않아요.",
    caminoCuerpo: "들려준 내용을 살펴봤는데, 솔직히 이 각도로는 정말 앞으로 나아가게 해 줄 계획을 세울 재료가 부족해요. 구색만 갖춘 계획을 드리느니 솔직하게 말씀드리는 게 낫다고 생각해요. 아이디어가 안 된다는 뜻이 아니에요. 이 길이 아니라는 뜻이에요.",
    mundoTitulo: "{{nombre}}, 이 아이디어에는 아직 때가 아니에요.",
    mundoCuerpo: "지금 있는 것으로 이 월드를 활성화해 탐색해 봤지만, 억지로 일을 만들지 않고서는 보탬이 될 하위 프로젝트를 찾지 못했어요. 구색만 갖춘 체크리스트를 드리느니 여기서 멈추는 게 낫겠어요. 이 월드는 계속 기다리고 있어요. 프로젝트가 자라면 언제든 다시 들어올 수 있어요.",
    mundoSinNombre: "이 월드",
    seguimientoTitulo: "이번 사이클에서는 {{nombre}}에서 새로운 문을 찾지 못했어요.",
    seguimientoCuerpo: "들려준 내용을 살펴봤지만, 억지로 일을 만들지 않고서는 이 월드에서 계획으로 삼을 만한 새로운 것이 보이지 않았어요. 이 월드의 계획과 진행 상황은 그대로예요. 계속 이어 가다가 새로운 소식이 생기면 다시 들려주세요.",
    seguimientoSinNombre: "이 월드",
  },
};

const ar: typeof es = {
  turno: {
    faltaRespuesta: "'respuesta' مفقودة",
  },
  regenerar: {
    noEncontrePlan: "لم أجد تلك الخطة.",
    planCompleto: "هذه الخطة مكتملة بالفعل: لا شيء لإعادة إنشائه.",
  },
  plan: {
    noPudeTerminar: "لم أتمكن من إكمال كتابة خطتكم. ما حدّثتموني به محفوظ؛ حاولوا مرة أخرى.",
  },
  organizador: {
    noPudeOrganizar: "لم أتمكن من ترتيب فكرتكم الآن. حاولوا مرة أخرى بعد قليل.",
    yaOrdenada: "هذه الفكرة مرتّبة بالفعل.",
    truncado: "فكرتكم تحمل الكثير، أكثر مما أستطيع ترتيبه دفعة واحدة؛ اختصروها قليلًا أو حدّثوني بها على أجزاء ثم حاولوا مرة أخرى",
    noPudimosOrganizar: "تعذّر ترتيب فكرتكم الآن؛ نصّكم محفوظ، حاولوا مرة أخرى",
  },
  cierre: {
    caminoTitulo: "في هذا الطريق لا أجد خطة تستحق وقتكم.",
    caminoCuerpo: "استكشفت ما حدّثتموني به، وبصراحة، هذه الزاوية لا تمنحني مادة كافية لأبني لكم خطة تدفعكم إلى الأمام حقًا. أفضّل أن أقول لكم ذلك على أن أقدّم لكم حشوًا. هذا ليس رفضًا لفكرتكم: إنه رفض لهذا الطريق.",
    mundoTitulo: "{{nombre}} ليس لهذه الفكرة، ليس بعد.",
    mundoCuerpo: "فعّلت هذا العالم واستكشفته بما هو متاح اليوم، ولم أجد مشروعًا فرعيًا يضيف لكم قيمة دون أن أختلق لكم عملًا. بدلًا من أن أعطيكم قائمة مهام للحشو، أفضّل التوقف هنا. هذا العالم ما زال في انتظاركم: يمكنكم العودة إليه حين يكبر مشروعكم.",
    mundoSinNombre: "هذا العالم",
    seguimientoTitulo: "في هذه الدورة لم أجد بابًا جديدًا في {{nombre}}.",
    seguimientoCuerpo: "راجعت ما حدّثتموني به ولم أجد جديدًا يستحق خطة في هذا العالم دون أن أختلق لكم عملًا. خطتكم وتقدّمكم في هذا العالم باقيان كما هما: يمكنكم المضي فيهما والعودة لتحدّثوني حين يستجدّ شيء.",
    seguimientoSinNombre: "هذا العالم",
  },
};

const hi: typeof es = {
  turno: {
    faltaRespuesta: "'respuesta' नहीं है",
  },
  regenerar: {
    noEncontrePlan: "वह योजना नहीं मिली।",
    planCompleto: "यह योजना पहले से पूरी है: दोबारा बनाने को कुछ नहीं है।",
  },
  plan: {
    noPudeTerminar: "आपकी योजना पूरी नहीं लिखी जा सकी। आपने जो बताया, वह सहेजा हुआ है; फिर से कोशिश करें।",
  },
  organizador: {
    noPudeOrganizar: "अभी आपका विचार व्यवस्थित नहीं हो पाया। थोड़ी देर में फिर से कोशिश करें।",
    yaOrdenada: "यह विचार पहले से व्यवस्थित है।",
    truncado: "आपके विचार में बहुत कुछ है, और यह एक बार में व्यवस्थित करने की सीमा से ज़्यादा है; इसे थोड़ा छोटा करें या हिस्सों में बताएँ, और फिर से कोशिश करें",
    noPudimosOrganizar: "हम अभी आपका विचार व्यवस्थित नहीं कर पाए; आपका लिखा सहेजा हुआ है, फिर से कोशिश करें",
  },
  cierre: {
    caminoTitulo: "इस रास्ते पर मुझे ऐसी योजना नहीं दिखती जो आपके समय के लायक हो।",
    caminoCuerpo: "आपने जो बताया, उसे मैंने खोजा, और सच कहूँ तो इस पहलू में इतनी सामग्री नहीं है कि मैं आपके लिए ऐसी योजना बना सकूँ जो सच में आपको आगे बढ़ाए। खानापूर्ति वाली चीज़ देने से अच्छा है कि मैं आपको साफ़ बता दूँ। यह आपके विचार को ना नहीं है: यह इस रास्ते को ना है।",
    mundoTitulo: "{{nombre}} इस विचार के लिए नहीं है, अभी नहीं।",
    mundoCuerpo: "आज जो कुछ है, उसके साथ मैंने इस दुनिया को सक्रिय करके खोजा, और मुझे ऐसी कोई उप-परियोजना नहीं मिली जो बिना फ़ालतू काम गढ़े आपके काम आए। खानापूर्ति वाली चेकलिस्ट देने से अच्छा है कि मैं यहीं रुक जाऊँ। यह दुनिया आपका इंतज़ार करती रहेगी: जब आपकी परियोजना बढ़े, तब लौट आइए।",
    mundoSinNombre: "यह दुनिया",
    seguimientoTitulo: "इस चक्र में मुझे {{nombre}} में कोई नया दरवाज़ा नहीं मिला।",
    seguimientoCuerpo: "आपने जो बताया, उसे मैंने देखा, और इस दुनिया में ऐसा कुछ नया नहीं मिला जिस पर बिना फ़ालतू काम गढ़े योजना बन सके। इस दुनिया में आपकी योजना और प्रगति वैसी ही हैं: उन पर काम जारी रखें, और जब कुछ नया हो, मुझे फिर बताइए।",
    seguimientoSinNombre: "इस दुनिया",
  },
};

export const SERVIDOR_SESION: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
