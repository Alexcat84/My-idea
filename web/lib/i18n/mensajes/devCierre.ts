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

const fr: typeof es = {
  camino: {
    titulo: "Par ici, je ne trouve pas de plan qui vaille ton temps.",
    cuerpo: "J'ai exploré ce que tu m'as raconté et, pour être honnête, cet angle ne me donne pas assez de matière pour te bâtir un plan qui te fasse vraiment avancer. Je préfère te le dire plutôt que de te livrer du remplissage. Ce n'est pas un non à ton idée : c'est un non à ce chemin.",
    porque: "Tes réponses pointent vers un groupe dont je ne peux pas vérifier aujourd'hui qu'il existe et qu'il est prêt à payer, et sans vrai signal de demande, je n'ai rien sur quoi appuyer les étapes.",
  },
  mundo: {
    titulo: "Qualité et confiance n'est pas pour cette idée, pas encore.",
    cuerpo: "J'ai activé et exploré ce monde avec ce qu'il y a aujourd'hui, et je n'ai pas trouvé de sous-projet qui t'apporte quelque chose sans t'inventer du travail. Plutôt que de te donner une liste d'actions pour faire du remplissage, je préfère m'arrêter ici. Ce monde t'attend toujours : tu pourras y revenir quand ton projet grandira.",
    porque: "Qualité et confiance brille quand tu as déjà des clients qui reviennent et que tu veux qu'ils reviennent plus souvent; ton idée cherche encore son premier client qui ne soit pas une connaissance.",
  },
};

const pt: typeof es = {
  camino: {
    titulo: "Por aqui não encontro um plano que valha o seu tempo.",
    cuerpo: "Explorei o que você me contou e, sendo honesto, este ângulo não me dá material suficiente para montar um plano que realmente faça você avançar. Prefiro dizer isso a te entregar um plano só para encher linguiça. Não é um não para a sua ideia: é um não para este caminho.",
    porque: "Suas respostas apontam para um grupo que hoje não consigo confirmar que exista e esteja disposto a pagar, e sem um sinal real de demanda não tenho onde apoiar as etapas.",
  },
  mundo: {
    titulo: "Qualidade e Confiança não é para esta ideia, por enquanto.",
    cuerpo: "Ativei e explorei este mundo com o que existe hoje, e não encontrei um subprojeto que acrescente algo sem inventar trabalho para você. Em vez de te dar um checklist só para encher linguiça, prefiro parar aqui. Este mundo continua esperando por você: você pode voltar quando seu projeto crescer.",
    porque: "Qualidade e Confiança brilha quando você já tem clientes que voltam e quer que voltem mais; sua ideia ainda está procurando o primeiro cliente que não seja um conhecido.",
  },
};

const de: typeof es = {
  camino: {
    titulo: "Auf diesem Weg finde ich keinen Plan, der deine Zeit wert ist.",
    cuerpo: "Ich habe mir angesehen, was du mir erzählt hast, und ehrlich gesagt gibt mir dieser Ansatz nicht genug Stoff, um dir einen Plan zu bauen, der dich wirklich weiterbringt. Das sage ich dir lieber, als dir Füllmaterial zu liefern. Das ist kein Nein zu deiner Idee: Es ist ein Nein zu diesem Weg.",
    porque: "Deine Antworten deuten auf eine Gruppe, bei der ich heute nicht bestätigen kann, dass es sie gibt und dass sie zahlen will, und ohne ein echtes Zeichen von Nachfrage habe ich nichts, worauf die Etappen stehen könnten.",
  },
  mundo: {
    titulo: "Qualität & Vertrauen passt noch nicht zu dieser Idee.",
    cuerpo: "Ich habe diese Welt mit dem aktiviert und erkundet, was heute da ist, und kein Teilprojekt gefunden, das dir etwas bringt, ohne dir unnötige Arbeit zu erfinden. Statt dir eine Checkliste voller Füllmaterial zu geben, höre ich lieber hier auf. Diese Welt wartet weiter auf dich: Du kannst wieder hinein, wenn dein Projekt wächst.",
    porque: "Qualität & Vertrauen glänzt, wenn du schon Kunden hast, die wiederkommen, und du willst, dass sie öfter kommen; deine Idee sucht noch ihren ersten Kunden, der nicht aus deinem Bekanntenkreis stammt.",
  },
};

const it: typeof es = {
  camino: {
    titulo: "Su questa strada non trovo un piano che valga il tuo tempo.",
    cuerpo: "Ho esplorato quello che mi hai raccontato e, in tutta onestà, questa angolazione non mi dà abbastanza materiale per costruirti un piano che ti faccia davvero andare avanti. Preferisco dirtelo piuttosto che darti del riempitivo. Non è un no alla tua idea: è un no a questa strada.",
    porque: "Le tue risposte indicano un gruppo di persone di cui oggi non posso verificare né l'esistenza né la voglia di pagare, e senza un segnale reale di domanda non ho basi su cui costruire le tappe.",
  },
  mundo: {
    titulo: "Qualità e Fiducia non fa per questa idea, per ora.",
    cuerpo: "Ho attivato ed esplorato questo mondo con quello che c'è oggi, e non ho trovato un sottoprogetto che ti dia qualcosa in più senza inventarti lavoro. Piuttosto che darti una checklist di riempitivo, preferisco fermarmi qui. Questo mondo ti aspetta: puoi rientrarci quando il tuo progetto crescerà.",
    porque: "Qualità e Fiducia dà il meglio quando hai già clienti che tornano e vuoi che tornino più spesso; la tua idea sta ancora cercando il primo cliente che non sia un conoscente.",
  },
};

const ja: typeof es = {
  camino: {
    titulo: "この方向では、時間をかけるに値するプランが見つかりません。",
    cuerpo: "お話しいただいた内容を探ってみましたが、正直に言うと、この切り口では、本当に前へ進めるプランを組み立てるだけの材料がありません。中身のないものをお渡しするより、そうお伝えするほうを選びます。アイデアそのものへの「ノー」ではなく、この道への「ノー」です。",
    porque: "回答から見えてくるのは、お金を払ってでも欲しいと思う人たちが今いるのか、まだ確かめられないグループです。需要の確かなサインがないままでは、ステージを組み立てる土台がありません。",
  },
  mundo: {
    titulo: "「品質と信頼」は、このアイデアにはまだ早いようです。",
    cuerpo: "今ある情報でこのワールドを開いて探ってみましたが、無理に作業を作り出さずに役立つサブプロジェクトは見つかりませんでした。中身のないチェックリストをお渡しするより、ここで止めることにします。このワールドはこれからも待っています。プロジェクトが育ったら、また入ってきてください。",
    porque: "「品質と信頼」が力を発揮するのは、リピートしてくれるお客様がすでにいて、もっと戻ってきてほしいときです。このアイデアは、まだ知り合い以外の最初のお客様を探している段階です。",
  },
};

const zh: typeof es = {
  camino: {
    titulo: "沿着这条路，我找不到值得你花时间的计划。",
    cuerpo: "我仔细看了你告诉我的内容。坦白说，从这个角度，我拿不到足够的素材，没法为你做出一份真正能推动你的计划。与其给你凑数的内容，我宁愿直说。这不是否定你的想法，而是否定这条路。",
    porque: "你的回答指向的人群，我目前无法确认真实存在、也愿意付钱；没有真实的需求信号，我就没有依据来撑起各个阶段。",
  },
  mundo: {
    titulo: "质量与信任暂时还不适合这个想法。",
    cuerpo: "我根据你目前的情况启用并探索了这个世界，但没找到一个真正对你有帮助、又不是凭空给你加活的子项目。与其给你一份凑数的清单，我宁愿在这里停下。这个世界会一直等你：等你的项目成长了，随时可以回来。",
    porque: "当你已经有回头客，并希望他们更常回来时，质量与信任才能大显身手；而你的想法还在寻找第一个不是熟人的客户。",
  },
};

const ko: typeof es = {
  camino: {
    titulo: "이 방향으로는 시간을 들일 만한 계획을 찾지 못했어요.",
    cuerpo: "들려준 내용을 살펴봤는데, 솔직히 말하면 이 방향으로는 정말 앞으로 나아가게 해 줄 계획을 세울 재료가 부족해요. 구색만 갖춘 계획을 건네기보다 솔직하게 말하는 게 낫다고 생각해요. 아이디어를 거절하는 게 아니에요. 이 길을 거절하는 거예요.",
    porque: "답변을 보면, 지금으로서는 실제로 존재하는지도, 돈을 낼 마음이 있는지도 확인할 수 없는 사람들을 향하고 있어요. 실제 수요 신호가 없으면 단계를 세울 근거가 없어요.",
  },
  mundo: {
    titulo: "품질과 신뢰는 아직 이 아이디어에 맞지 않아요.",
    cuerpo: "지금 있는 것으로 이 월드를 활성화해 살펴봤지만, 괜한 일을 만들지 않으면서 도움이 될 하위 프로젝트를 찾지 못했어요. 구색만 갖춘 체크리스트를 건네기보다 여기서 멈추는 게 낫겠어요. 이 월드는 계속 기다리고 있어요. 프로젝트가 자라면 언제든 다시 들어올 수 있어요.",
    porque: "품질과 신뢰는 다시 찾아오는 고객이 이미 있고, 그 고객이 더 자주 오게 만들고 싶을 때 빛을 발해요. 지금 아이디어는 아직 지인이 아닌 첫 고객을 찾는 중이에요.",
  },
};

const ar: typeof es = {
  camino: {
    titulo: "لا أجد في هذا الطريق خطة تستحق وقتكم.",
    cuerpo: "استكشفت ما رويتموه لي، وبصراحة، هذه الزاوية لا تمنحني مادة كافية لأبني لكم خطة تدفعكم إلى الأمام حقًا. أفضّل أن أقول لكم ذلك على أن أسلّمكم حشوًا. ليست «لا» لفكرتكم: إنها «لا» لهذا الطريق.",
    porque: "إجاباتكم تشير إلى فئة لا أستطيع اليوم التحقق من وجودها ولا من استعدادها للدفع، ومن دون إشارة حقيقية إلى الطلب لا أجد ما أبني عليه المراحل.",
  },
  mundo: {
    titulo: "عالم الجودة والثقة لا يناسب هذه الفكرة، ليس بعد.",
    cuerpo: "فعّلت هذا العالم واستكشفته بما لديكم اليوم، ولم أجد مشروعًا فرعيًا يضيف لكم شيئًا من دون أن أخترع لكم عملًا لا حاجة إليه. وبدلًا من أن أعطيكم قائمة مهام للحشو، أفضّل التوقف هنا. هذا العالم ما زال بانتظاركم: يمكنكم العودة إليه حين يكبر مشروعكم.",
    porque: "يتألّق عالم الجودة والثقة حين يكون لديكم عملاء يعودون وتريدون أن يعودوا أكثر؛ أما فكرتكم فما زالت تبحث عن أول عميل ليس من معارفكم.",
  },
};

const hi: typeof es = {
  camino: {
    titulo: "इस रास्ते पर मुझे ऐसी योजना नहीं मिल रही जो आपके समय के लायक हो।",
    cuerpo: "आपने जो बताया, उसे मैंने खंगाला, और सच कहूँ तो यह नज़रिया मुझे इतना आधार नहीं देता कि आपके लिए ऐसी योजना बनाऊँ जो सच में आपको आगे बढ़ाए। खानापूर्ति वाली चीज़ थमाने से अच्छा है कि मैं आपको साफ़ बता दूँ। यह आपके विचार को ना नहीं है: यह इस रास्ते को ना है।",
    porque: "आपके जवाब एक ऐसे समूह की ओर इशारा करते हैं जिसके बारे में आज यह पक्का नहीं किया जा सकता कि वह मौजूद है और पैसे देने को तैयार है, और माँग के किसी असली संकेत के बिना चरणों को टिकाने का कोई आधार नहीं है।",
  },
  mundo: {
    titulo: "गुणवत्ता और भरोसा इस विचार के लिए नहीं है, अभी नहीं।",
    cuerpo: "मैंने आज की स्थिति के साथ इस दुनिया को चालू करके खंगाला, और ऐसी कोई उप-परियोजना नहीं मिली जो आपके लिए बेवजह का काम गढ़े बिना कुछ जोड़े। खानापूर्ति वाली चेकलिस्ट देने से अच्छा है कि मैं यहीं रुक जाऊँ। यह दुनिया आपका इंतज़ार करती रहेगी: जब आपकी परियोजना बढ़े, तब लौट आइए।",
    porque: "गुणवत्ता और भरोसा तब चमकता है जब आपके पास पहले से ऐसे ग्राहक हों जो लौटकर आते हैं और आपकी चाहत हो कि वे और ज़्यादा लौटें; आपका विचार अभी अपना पहला ऐसा ग्राहक ढूँढ रहा है जो कोई जान-पहचान वाला न हो।",
  },
};

export const DEV_CIERRE: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
