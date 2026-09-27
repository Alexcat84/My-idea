/**
 * /creditos, el centro de créditos (app/creditos/page.tsx). Sin cifras de
 * precio: los números salen de lib/precios.ts y solo de ahí (AGENTS.md).
 */
import type { PorIdioma } from "../config";

const es = {
  misIdeas: "Mis ideas /",
  titulo: "Créditos",
  disponibles: "Disponible: {{saldo}}",
  saldoNoDisponible: "saldo no disponible",
  /** La píldora del costo, a la derecha de la cifra. */
  creditos: "créditos",
  heroe: {
    tuSaldo: "Tu saldo",
    noPudeLeer: "No pudimos leer tu saldo en este momento. Recarga la página en un rato.",
    garantiaCuenta:
      "Se verifica tu saldo al inicio de cada acción y se descuenta a la entrega. Si algo falla a mitad, no se cobra nada.",
    sinCuenta: "Tus créditos viven en tu cuenta. Entra o crea la tuya para sumar y usar créditos.",
  },
  sumar: {
    titulo: "Sumar créditos",
    nCreditos: "{{n}} créditos",
    compraPronto: "La compra se abre pronto",
  },
  usar: {
    titulo: "Usa tus créditos según lo que necesites",
    gratis:
      "<b>La Claridad</b> es <g>gratis</g>: tu idea ordenada, la frase, lo que tienes y lo que asumes. El <b>diagnóstico de un mundo</b> también es <g>gratis</g>: el primer vistazo de ese frente.",
  },
  proyecto: {
    etiqueta: "Tu proyecto",
    plan: "Tu Plan",
    planTexto: "Tu viaje completo, de la idea a hacerla realidad: el plan y todo para llevarlo a cabo.",
    cambioRumbo: "Un cambio de rumbo",
    cambioRumboTexto:
      "Cuando la realidad te mueve el plan y necesitas replantear sin empezar de cero: cuentas qué pasó, se conserva lo que ya lograste y tu viaje se rehace desde ahí.",
  },
  /** "Lo que incluye" el plan: el prefijo en <b> va en negrita. */
  incluyePlan: [
    "<b>El plan:</b> tus etapas, con sus entregables, tus tareas y tus fechas de un vistazo.",
    "<b>Manos a la Obra:</b> ejecuta tu plan. Marca lo hecho, añade tus notas y ve tu avance en tiempo real. Incluido, siempre.",
    "<b>Tus Números:</b> el tablero de tu idea (margen, punto de equilibrio, escenarios). Corrige cifras y recalcula cuando quieras.",
    "<b>Tus documentos:</b> tu plan y cada resumen, en archivo y PDF, para leer o guardar.",
    "<b>Tu bitácora:</b> la historia de tu viaje, cada decisión, guardada en orden.",
  ],
  mundo: {
    etiqueta: "Un mundo",
    plan: "El plan de un mundo",
    planTexto:
      "Un frente entero de tu negocio (calidad, riesgos, seguridad…), con su propio espacio dentro de tu mismo proyecto.",
    cambioRumbo: "Un cambio de rumbo en un mundo",
    cambioRumboTexto: "Lo mismo dentro de ese frente, cuando ahí necesitas replantear el rumbo.",
  },
  /** "Lo que incluye" el plan de un mundo. */
  incluyeMundo: [
    "<b>Su plan y su Manos a la Obra:</b> las etapas, tareas y fechas de ese frente, listas para ejecutar igual que tu viaje.",
    "<b>Todo lo del mundo, por separado:</b> su avance, sus documentos y su bitácora, solo de ese frente.",
    "<b>Y queda en tu Expediente:</b> el único documento que reúne tu idea, tu plan y cada mundo, cada uno en su propia sección.",
    "<b>Un mismo proyecto:</b> no es otra cuenta ni otra idea.",
  ],
  mundosPorDesbloquear: "Los mundos que puedes desbloquear",
};

const en: typeof es = {
  misIdeas: "My ideas /",
  titulo: "Credits",
  disponibles: "{{saldo}} available",
  saldoNoDisponible: "balance unavailable",
  creditos: "credits",
  heroe: {
    tuSaldo: "Your balance",
    noPudeLeer: "We couldn't read your balance right now. Reload the page in a little while.",
    garantiaCuenta:
      "Your balance is checked when each action starts and charged when it's delivered. If something fails halfway, you're not charged a thing.",
    sinCuenta: "Your credits live in your account. Log in or create yours to add and use credits.",
  },
  sumar: {
    titulo: "Add credits",
    nCreditos: "{{n}} credits",
    compraPronto: "Purchases open soon",
  },
  usar: {
    titulo: "Use your credits for whatever you need",
    gratis:
      "<b>Clarity</b> is <g>free</g>: your idea laid out, its one-line summary, what you have and what you're assuming. A <b>world diagnosis</b> is <g>free</g> too: your first look at that area.",
  },
  proyecto: {
    etiqueta: "Your project",
    plan: "Your Plan",
    planTexto: "Your whole journey, from idea to reality: the plan and everything you need to carry it out.",
    cambioRumbo: "A change of course",
    cambioRumboTexto:
      "When reality shakes up your plan and you need to rethink it without starting over: you share what happened, everything you've achieved is kept, and your journey is rebuilt from there.",
  },
  incluyePlan: [
    "<b>The plan:</b> your stages, with their deliverables, your tasks, and your dates at a glance.",
    "<b>Get to Work:</b> carry out your plan. Check off what's done, add your notes, and see your progress in real time. Always included.",
    "<b>Your Numbers:</b> your idea's dashboard (margin, break-even point, scenarios). Adjust figures and recalculate whenever you want.",
    "<b>Your documents:</b> your plan and every summary, as a file and a PDF, to read or keep.",
    "<b>Your logbook:</b> the story of your journey, every decision, kept in order.",
  ],
  mundo: {
    etiqueta: "A world",
    plan: "The plan for a world",
    planTexto:
      "A whole area of your business (quality, risks, security…), with its own space inside the same project.",
    cambioRumbo: "A change of course in a world",
    cambioRumboTexto: "The same thing within that area, when you need to rethink your direction there.",
  },
  incluyeMundo: [
    "<b>Its plan and its Get to Work:</b> the stages, tasks, and dates for that area, ready to carry out just like your journey.",
    "<b>Everything in the world, kept separate:</b> its progress, its documents, and its logbook, for that area only.",
    "<b>And it goes into your Full Record:</b> the one document that brings together your idea, your plan, and every world, each in its own section.",
    "<b>One and the same project:</b> not another account, not another idea.",
  ],
  mundosPorDesbloquear: "The worlds you can unlock",
};

const fr: typeof es = {
  misIdeas: "Mes idées /",
  titulo: "Crédits",
  disponibles: "Disponible : {{saldo}}",
  saldoNoDisponible: "solde non disponible",
  creditos: "crédits",
  heroe: {
    tuSaldo: "Ton solde",
    noPudeLeer: "Nous n'avons pas pu lire ton solde pour l'instant. Recharge la page dans un moment.",
    garantiaCuenta: "Ton solde est vérifié au début de chaque action et débité à la livraison. Si quelque chose échoue en cours de route, rien n'est facturé.",
    sinCuenta: "Tes crédits sont liés à ton compte. Connecte-toi ou crée le tien pour ajouter et utiliser des crédits.",
  },
  sumar: {
    titulo: "Ajouter des crédits",
    nCreditos: "{{n}} crédits",
    compraPronto: "L'achat sera bientôt disponible",
  },
  usar: {
    titulo: "Utilise tes crédits selon tes besoins",
    gratis: "<b>La Clarté</b> est <g>gratuite</g> : ton idée mise en ordre, sa phrase, ce que tu as et ce que tu tiens pour acquis. Le <b>diagnostic d'un monde</b> est lui aussi <g>gratuit</g> : un premier coup d'œil sur ce volet.",
  },
  proyecto: {
    etiqueta: "Ton projet",
    plan: "Ton plan",
    planTexto: "Ton parcours complet, de l'idée à sa réalisation : le plan et tout ce qu'il faut pour le mener à bien.",
    cambioRumbo: "Un changement de cap",
    cambioRumboTexto: "Quand la réalité bouscule ton plan et que tu dois le repenser sans repartir de zéro : tu racontes ce qui s'est passé, ce que tu as déjà accompli est conservé, et ton parcours est refait à partir de là.",
  },
  incluyePlan: [
    "<b>Le plan :</b> tes étapes, avec leurs livrables, tes tâches et tes dates en un coup d'œil.",
    "<b>À l'ouvrage :</b> passe à l'action avec ton plan. Coche ce qui est fait, ajoute tes notes et vois ton avancement en temps réel. Inclus, toujours.",
    "<b>Tes chiffres :</b> le tableau de bord de ton idée (marge, seuil de rentabilité, scénarios). Corrige des chiffres et recalcule quand tu veux.",
    "<b>Tes documents :</b> ton plan et chaque résumé, en fichier et en PDF, à lire ou à garder.",
    "<b>Ton journal de bord :</b> l'histoire de ton parcours, chaque décision, gardée dans l'ordre.",
  ],
  mundo: {
    etiqueta: "Un monde",
    plan: "Le plan d'un monde",
    planTexto: "Tout un volet de ton entreprise (qualité, risques, sécurité…), avec son propre espace au sein de ton projet.",
    cambioRumbo: "Un changement de cap dans un monde",
    cambioRumboTexto: "La même chose à l'intérieur de ce volet, quand tu dois y repenser ton cap.",
  },
  incluyeMundo: [
    "<b>Son plan et son étape À l'ouvrage :</b> les étapes, les tâches et les dates de ce volet, prêtes à mettre en œuvre comme ton parcours.",
    "<b>Tout ce qui concerne le monde, à part :</b> son avancement, ses documents et son journal de bord, pour ce volet seulement.",
    "<b>Et tout va dans ton Dossier :</b> le seul document qui réunit ton idée, ton plan et chaque monde, chacun dans sa propre section.",
    "<b>Un seul et même projet :</b> ni un autre compte, ni une autre idée.",
  ],
  mundosPorDesbloquear: "Les mondes que tu peux débloquer",
};

const pt: typeof es = {
  misIdeas: "Minhas ideias /",
  titulo: "Créditos",
  disponibles: "Disponível: {{saldo}}",
  saldoNoDisponible: "saldo indisponível",
  creditos: "créditos",
  heroe: {
    tuSaldo: "Seu saldo",
    noPudeLeer: "Não conseguimos ler seu saldo neste momento. Recarregue a página daqui a pouco.",
    garantiaCuenta: "Seu saldo é verificado no início de cada ação e descontado na entrega. Se algo falhar no meio do caminho, nada é cobrado.",
    sinCuenta: "Seus créditos ficam na sua conta. Entre ou crie a sua para adicionar e usar créditos.",
  },
  sumar: {
    titulo: "Adicionar créditos",
    nCreditos: "{{n}} créditos",
    compraPronto: "A compra abre em breve",
  },
  usar: {
    titulo: "Use seus créditos de acordo com o que você precisa",
    gratis: "<b>A Clareza</b> é <g>gratuita</g>: sua ideia organizada, a frase, o que você tem e o que você supõe. O <b>diagnóstico de um mundo</b> também é <g>gratuito</g>: a primeira olhada nessa frente.",
  },
  proyecto: {
    etiqueta: "Seu projeto",
    plan: "Seu Plano",
    planTexto: "Sua jornada completa, da ideia à realidade: o plano e tudo para colocá-lo em prática.",
    cambioRumbo: "Uma mudança de rumo",
    cambioRumboTexto: "Quando a realidade mexe no seu plano e você precisa repensar sem começar do zero: você conta o que aconteceu, o que já conquistou é mantido e sua jornada é refeita a partir daí.",
  },
  incluyePlan: [
    "<b>O plano:</b> suas etapas, com as entregas, suas tarefas e suas datas num relance.",
    "<b>Mãos à Obra:</b> execute seu plano. Marque o que foi feito, adicione suas notas e veja seu avanço em tempo real. Incluído, sempre.",
    "<b>Seus Números:</b> o painel da sua ideia (margem, ponto de equilíbrio, cenários). Corrija valores e recalcule quando quiser.",
    "<b>Seus documentos:</b> seu plano e cada resumo, em arquivo e PDF, para ler ou guardar.",
    "<b>Seu diário de bordo:</b> a história da sua jornada, cada decisão, guardada em ordem.",
  ],
  mundo: {
    etiqueta: "Um mundo",
    plan: "O plano de um mundo",
    planTexto: "Uma frente inteira do seu negócio (qualidade, riscos, segurança…), com seu próprio espaço dentro do mesmo projeto.",
    cambioRumbo: "Uma mudança de rumo em um mundo",
    cambioRumboTexto: "O mesmo dentro dessa frente, quando é ali que você precisa repensar o rumo.",
  },
  incluyeMundo: [
    "<b>O plano e o Mãos à Obra dele:</b> as etapas, tarefas e datas dessa frente, prontas para executar como na sua jornada.",
    "<b>Tudo do mundo, separado:</b> o avanço, os documentos e o diário de bordo dele, só dessa frente.",
    "<b>E fica no seu Dossiê:</b> o único documento que reúne sua ideia, seu plano e cada mundo, cada um na sua própria seção.",
    "<b>Um mesmo projeto:</b> não é outra conta nem outra ideia.",
  ],
  mundosPorDesbloquear: "Os mundos que você pode desbloquear",
};

const de: typeof es = {
  misIdeas: "Meine Ideen /",
  titulo: "Guthaben",
  disponibles: "{{saldo}} verfügbar",
  saldoNoDisponible: "Guthaben nicht verfügbar",
  creditos: "Punkte",
  heroe: {
    tuSaldo: "Dein Guthaben",
    noPudeLeer: "Wir konnten dein Guthaben gerade nicht abrufen. Lade die Seite gleich noch einmal.",
    garantiaCuenta: "Dein Guthaben wird zu Beginn jedes Vorgangs geprüft und erst bei der Lieferung abgebucht. Wenn unterwegs etwas schiefgeht, wird dir nichts berechnet.",
    sinCuenta: "Dein Guthaben gehört zu deinem Konto. Melde dich an oder erstelle ein Konto, um Guthaben aufzuladen und zu nutzen.",
  },
  sumar: {
    titulo: "Guthaben aufladen",
    nCreditos: "{{n}} Punkte",
    compraPronto: "Kaufen ist bald möglich",
  },
  usar: {
    titulo: "Setz dein Guthaben ein, wie du es brauchst",
    gratis: "<b>Die Klarheit</b> ist <g>kostenlos</g>: deine geordnete Idee, der Kernsatz, was du hast und wovon du ausgehst. Auch die <b>Diagnose einer Welt</b> ist <g>kostenlos</g>: dein erster Blick auf dieses Themenfeld.",
  },
  proyecto: {
    etiqueta: "Dein Projekt",
    plan: "Dein Plan",
    planTexto: "Deine ganze Reise, von der Idee bis zur Wirklichkeit: der Plan und alles, was du brauchst, um ihn umzusetzen.",
    cambioRumbo: "Eine Kurskorrektur",
    cambioRumboTexto: "Wenn die Wirklichkeit deinen Plan durcheinanderbringt und du neu planen musst, ohne bei null anzufangen: Du erzählst, was passiert ist, alles Erreichte bleibt erhalten, und deine Reise wird von dort aus neu aufgebaut.",
  },
  incluyePlan: [
    "<b>Der Plan:</b> deine Etappen mit ihren Ergebnissen, deine Aufgaben und deine Termine auf einen Blick.",
    "<b>Ans Werk:</b> Setz deinen Plan um. Hak ab, was erledigt ist, füg deine Notizen hinzu und sieh deinen Fortschritt in Echtzeit. Immer inklusive.",
    "<b>Deine Zahlen:</b> die Übersicht deiner Idee (Marge, Gewinnschwelle, Szenarien). Korrigiere Zahlen und rechne neu, wann immer du willst.",
    "<b>Deine Dokumente:</b> dein Plan und jede Zusammenfassung, als Datei und als PDF, zum Lesen oder Aufbewahren.",
    "<b>Dein Logbuch:</b> die Geschichte deiner Reise, jede Entscheidung, der Reihe nach festgehalten.",
  ],
  mundo: {
    etiqueta: "Eine Welt",
    plan: "Der Plan für eine Welt",
    planTexto: "Ein ganzes Themenfeld deines Geschäfts (Qualität, Risiken, Sicherheit…), mit einem eigenen Bereich in deinem Projekt.",
    cambioRumbo: "Eine Kurskorrektur in einer Welt",
    cambioRumboTexto: "Dasselbe innerhalb dieses Themenfelds, wenn du dort die Richtung neu bestimmen musst.",
  },
  incluyeMundo: [
    "<b>Eigener Plan, eigenes „Ans Werk“:</b> die Etappen, Aufgaben und Termine dieses Themenfelds, bereit zur Umsetzung wie deine Reise.",
    "<b>Alles aus der Welt, getrennt:</b> ihr Fortschritt, ihre Dokumente und ihr Logbuch, nur für dieses Themenfeld.",
    "<b>Und sie kommt in dein Dossier:</b> das eine Dokument, das deine Idee, deinen Plan und jede Welt zusammenführt, jede in einem eigenen Abschnitt.",
    "<b>Ein und dasselbe Projekt:</b> kein weiteres Konto, keine weitere Idee.",
  ],
  mundosPorDesbloquear: "Die Welten, die du freischalten kannst",
};

const it: typeof es = {
  misIdeas: "Le mie idee /",
  titulo: "Crediti",
  disponibles: "Disponibile: {{saldo}}",
  saldoNoDisponible: "saldo non disponibile",
  creditos: "crediti",
  heroe: {
    tuSaldo: "Il tuo saldo",
    noPudeLeer: "Non siamo riusciti a leggere il tuo saldo in questo momento. Ricarica la pagina tra un po'.",
    garantiaCuenta: "Il saldo viene verificato all'inizio di ogni azione e scalato alla consegna. Se qualcosa si blocca a metà, non ti viene addebitato nulla.",
    sinCuenta: "I tuoi crediti sono legati al tuo account. Accedi o creane uno per aggiungere e usare crediti.",
  },
  sumar: {
    titulo: "Aggiungi crediti",
    nCreditos: "{{n}} crediti",
    compraPronto: "Gli acquisti saranno disponibili a breve",
  },
  usar: {
    titulo: "Usa i tuoi crediti per quello che ti serve",
    gratis: "<b>La Chiarezza</b> è <g>gratis</g>: la tua idea in ordine, la frase che la riassume, ciò che hai e ciò che dai per scontato. Anche la <b>diagnosi di un mondo</b> è <g>gratis</g>: il primo sguardo su quell'ambito.",
  },
  proyecto: {
    etiqueta: "Il tuo progetto",
    plan: "Il tuo piano",
    planTexto: "Il tuo viaggio completo, dall'idea alla realtà: il piano e tutto ciò che serve per metterlo in pratica.",
    cambioRumbo: "Un cambio di rotta",
    cambioRumboTexto: "Quando la realtà ti scombina il piano e devi ripensarlo senza ripartire da zero: racconti cos'è successo, ciò che hai già ottenuto resta e il tuo viaggio viene ricostruito da lì.",
  },
  incluyePlan: [
    "<b>Il piano:</b> le tue tappe, con i loro risultati attesi, le tue attività e le tue date a colpo d'occhio.",
    "<b>Al lavoro:</b> metti in pratica il tuo piano. Segna ciò che hai fatto, aggiungi le tue note e guarda i tuoi progressi in tempo reale. Incluso, sempre.",
    "<b>I tuoi numeri:</b> il cruscotto della tua idea (margine, punto di pareggio, scenari). Correggi le cifre e ricalcola quando vuoi.",
    "<b>I tuoi documenti:</b> il tuo piano e ogni riepilogo, come file e in PDF, da leggere o conservare.",
    "<b>Il tuo diario di bordo:</b> la storia del tuo viaggio, ogni decisione, conservata in ordine.",
  ],
  mundo: {
    etiqueta: "Un mondo",
    plan: "Il piano di un mondo",
    planTexto: "Un intero ambito della tua attività (qualità, rischi, sicurezza…), con un suo spazio dentro lo stesso progetto.",
    cambioRumbo: "Un cambio di rotta in un mondo",
    cambioRumboTexto: "La stessa cosa dentro quell'ambito, quando lì devi ripensare la rotta.",
  },
  incluyeMundo: [
    "<b>Il suo piano e la sua fase Al lavoro:</b> le tappe, le attività e le date di quell'ambito, pronte da mettere in pratica proprio come il tuo viaggio.",
    "<b>Tutto ciò che riguarda il mondo, a parte:</b> i suoi progressi, i suoi documenti e il suo diario di bordo, solo di quell'ambito.",
    "<b>E finisce nel tuo Fascicolo:</b> l'unico documento che riunisce la tua idea, il tuo piano e ogni mondo, ciascuno nella sua sezione.",
    "<b>Un unico progetto:</b> non è un altro account né un'altra idea.",
  ],
  mundosPorDesbloquear: "I mondi che puoi sbloccare",
};

const ja: typeof es = {
  misIdeas: "アイデア一覧 /",
  titulo: "ポイント",
  disponibles: "利用可能：{{saldo}}",
  saldoNoDisponible: "残高を表示できません",
  creditos: "ポイント",
  heroe: {
    tuSaldo: "残高",
    noPudeLeer: "今は残高を読み込めませんでした。しばらくしてから、ページを再読み込みしてください。",
    garantiaCuenta: "残高は各アクションの開始時に確認され、お届けした時点で差し引かれます。途中で問題が起きた場合は、一切差し引かれません。",
    sinCuenta: "ポイントはアカウントに保存されます。ポイントを追加して使うには、ログインするかアカウントを作成してください。",
  },
  sumar: {
    titulo: "ポイントを追加",
    nCreditos: "{{n}}ポイント",
    compraPronto: "購入はまもなく開始します",
  },
  usar: {
    titulo: "必要に応じてポイントを使いましょう",
    gratis: "<b>明確さ</b>は<g>無料</g>です。整理されたアイデア、それをひと言で表したもの、持っているもの、前提にしていること。<b>ワールドの診断</b>も<g>無料</g>です。その分野を最初に見渡せます。",
  },
  proyecto: {
    etiqueta: "プロジェクト",
    plan: "あなたのプラン",
    planTexto: "アイデアを実現するまでの旅のすべて。プランと、それをやり遂げるために必要なものがそろっています。",
    cambioRumbo: "方向転換",
    cambioRumboTexto: "現実の変化でプランが揺らぎ、ゼロからやり直さずに考え直したいときに。起きたことを伝えれば、これまでの成果はそのままに、そこから旅を組み直します。",
  },
  incluyePlan: [
    "<b>プラン：</b>ステージとその成果物、タスク、期日をひと目で。",
    "<b>実行：</b>プランを実行に移します。終えたものにチェックを入れ、メモを残し、進み具合をリアルタイムで確認できます。常に含まれます。",
    "<b>あなたの数字：</b>アイデアのダッシュボード（利益、損益分岐点、シナリオ）。数字を直して、いつでも再計算できます。",
    "<b>ドキュメント：</b>プランと各まとめを、ファイルとPDFで。読むことも保存することもできます。",
    "<b>活動ログ：</b>あなたの旅の歩みと一つひとつの決定を、順番どおりに保存します。",
  ],
  mundo: {
    etiqueta: "ワールド",
    plan: "ワールドのプラン",
    planTexto: "ビジネスのひとつの分野まるごと（品質、リスク、セキュリティ…）を、同じプロジェクトの中の専用スペースで。",
    cambioRumbo: "ワールドでの方向転換",
    cambioRumboTexto: "同じことを、その分野の中で。そこで方向を考え直す必要があるときに。",
  },
  incluyeMundo: [
    "<b>そのワールドのプランと実行：</b>その分野のステージ、タスク、期日。あなたの旅と同じように、すぐに実行できます。",
    "<b>ワールドのことは、すべて別々に：</b>その分野だけの進み具合、ドキュメント、活動ログ。",
    "<b>全記録にも残ります：</b>アイデア、プラン、各ワールドをそれぞれのセクションにまとめた、ただ一つのドキュメントです。",
    "<b>同じひとつのプロジェクト：</b>別のアカウントでも、別のアイデアでもありません。",
  ],
  mundosPorDesbloquear: "解放できるワールド",
};

const zh: typeof es = {
  misIdeas: "我的想法 /",
  titulo: "点数",
  disponibles: "可用{{saldo}}",
  saldoNoDisponible: "暂时无法显示余额",
  creditos: "点数",
  heroe: {
    tuSaldo: "你的余额",
    noPudeLeer: "我们现在读不到你的余额。请过一会儿刷新页面。",
    garantiaCuenta: "每次操作开始时会核对你的余额，交付时才扣除。如果中途出错，一点都不收。",
    sinCuenta: "你的点数保存在你的账户里。登录或创建账户，就能充值和使用点数。",
  },
  sumar: {
    titulo: "充值点数",
    nCreditos: "{{n}}点",
    compraPronto: "即将开放购买",
  },
  usar: {
    titulo: "按你的需要使用点数",
    gratis: "<b>清晰</b>阶段<g>免费</g>：梳理好的想法、一句话概括、你已经拥有的和你正在假设的。<b>世界诊断</b>同样<g>免费</g>：让你先看一眼那个领域。",
  },
  proyecto: {
    etiqueta: "你的项目",
    plan: "你的计划",
    planTexto: "你的完整旅程，从想法到实现：计划，以及把它落地所需的一切。",
    cambioRumbo: "一次方向调整",
    cambioRumboTexto: "当现实打乱了你的计划，你需要重新规划又不想从头开始时：你讲讲发生了什么，已经取得的成果都会保留，你的旅程从那里重新搭建。",
  },
  incluyePlan: [
    "<b>计划：</b>你的各个阶段及其交付成果、你的任务和日期，一目了然。",
    "<b>动手做：</b>执行你的计划。勾选完成的事，添加笔记，实时查看进度。始终包含。",
    "<b>你的数字：</b>你的想法的看板（利润、盈亏平衡点、情景）。随时修改数字、重新计算。",
    "<b>你的文档：</b>你的计划和每份摘要，提供文件和PDF，可以阅读或保存。",
    "<b>你的日志：</b>你旅程的故事，每个决定都按顺序保存。",
  ],
  mundo: {
    etiqueta: "一个世界",
    plan: "一个世界的计划",
    planTexto: "你生意中的一整个领域（质量、风险、安全…），在你同一个项目里拥有自己的空间。",
    cambioRumbo: "某个世界里的方向调整",
    cambioRumboTexto: "和上面一样，只是针对那个领域：当那里需要重新调整方向时。",
  },
  incluyeMundo: [
    "<b>它的计划和它的“动手做”：</b>那个领域的阶段、任务和日期，像你的旅程一样随时可以执行。",
    "<b>这个世界的一切，单独呈现：</b>它的进度、文档和日志，只属于那个领域。",
    "<b>并收入你的完整档案：</b>唯一一份汇集你的想法、你的计划和每个世界的文档，每个世界各占一节。",
    "<b>同一个项目：</b>不是另一个账户，也不是另一个想法。",
  ],
  mundosPorDesbloquear: "你可以解锁的世界",
};

const ko: typeof es = {
  misIdeas: "내 아이디어 /",
  titulo: "크레딧",
  disponibles: "{{saldo}} 사용 가능",
  saldoNoDisponible: "잔액을 확인할 수 없음",
  creditos: "크레딧",
  heroe: {
    tuSaldo: "내 잔액",
    noPudeLeer: "지금은 잔액을 불러오지 못했어요. 잠시 후 페이지를 새로고침해 주세요.",
    garantiaCuenta: "작업을 시작할 때 잔액을 확인하고, 결과를 전달할 때 차감해요. 중간에 문제가 생기면 아무것도 청구되지 않아요.",
    sinCuenta: "크레딧은 계정에 보관돼요. 로그인하거나 계정을 만들면 크레딧을 충전하고 사용할 수 있어요.",
  },
  sumar: {
    titulo: "크레딧 충전",
    nCreditos: "{{n}}크레딧",
    compraPronto: "곧 구매할 수 있어요",
  },
  usar: {
    titulo: "필요한 곳에 크레딧을 쓰세요",
    gratis: "<b>명확함</b>은 <g>무료</g>예요: 정리된 아이디어, 한 줄 요약, 가진 것과 가정하는 것까지요. <b>월드 진단</b>도 <g>무료</g>예요: 그 분야를 처음으로 살펴보는 단계예요.",
  },
  proyecto: {
    etiqueta: "나의 프로젝트",
    plan: "나의 계획",
    planTexto: "아이디어에서 실현까지 이어지는 여정 전체: 계획과 그 계획을 실행하는 데 필요한 모든 것.",
    cambioRumbo: "방향 전환",
    cambioRumboTexto: "현실 때문에 계획이 흔들려서 처음부터가 아니라 지금 자리에서 다시 짜야 할 때: 있었던 일을 이야기하면, 이미 이룬 것은 그대로 두고 그 지점부터 여정을 다시 세워요.",
  },
  incluyePlan: [
    "<b>계획:</b> 단계와 결과물, 할 일, 날짜를 한눈에.",
    "<b>실행하기:</b> 계획을 실행해요. 끝낸 일을 표시하고, 메모를 남기고, 진행 상황을 실시간으로 확인하세요. 언제나 포함돼요.",
    "<b>나의 숫자:</b> 아이디어의 대시보드(마진, 손익분기점, 시나리오). 언제든 수치를 고치고 다시 계산할 수 있어요.",
    "<b>나의 문서:</b> 계획과 모든 요약을 파일과 PDF로 받아 읽거나 보관할 수 있어요.",
    "<b>나의 기록장:</b> 여정의 이야기와 모든 결정이 순서대로 저장돼요.",
  ],
  mundo: {
    etiqueta: "월드 하나",
    plan: "월드 하나의 계획",
    planTexto: "사업의 한 분야 전체(품질, 위험, 보안…)를 같은 프로젝트 안의 별도 공간에서 다뤄요.",
    cambioRumbo: "월드 안에서의 방향 전환",
    cambioRumboTexto: "같은 방식이에요. 그 분야에서 방향을 다시 잡아야 할 때 써요.",
  },
  incluyeMundo: [
    "<b>월드의 계획과 실행하기:</b> 그 분야의 단계, 할 일, 날짜가 나의 여정처럼 바로 실행할 수 있게 준비돼요.",
    "<b>월드의 모든 것을 따로:</b> 그 분야만의 진행 상황, 문서, 기록장.",
    "<b>전체 자료에도 담겨요:</b> 아이디어, 계획, 각 월드를 저마다의 섹션으로 모은 단 하나의 문서예요.",
    "<b>하나의 같은 프로젝트:</b> 다른 계정도, 다른 아이디어도 아니에요.",
  ],
  mundosPorDesbloquear: "열 수 있는 월드",
};

const ar: typeof es = {
  misIdeas: "أفكاري /",
  titulo: "الرصيد",
  disponibles: "المتاح: {{saldo}}",
  saldoNoDisponible: "الرصيد غير متاح",
  creditos: "من النقاط",
  heroe: {
    tuSaldo: "رصيدكم",
    noPudeLeer: "لم نتمكّن من قراءة رصيدكم الآن. أعيدوا تحميل الصفحة بعد قليل.",
    garantiaCuenta: "نتحقّق من رصيدكم عند بدء كل عملية، ولا يُخصم إلا عند التسليم. إن تعثّر شيء في منتصف الطريق، لا يُخصم أي شيء.",
    sinCuenta: "رصيدكم محفوظ في حسابكم. سجّلوا الدخول أو أنشئوا حسابكم لتضيفوا نقاطًا وتستخدموها.",
  },
  sumar: {
    titulo: "إضافة رصيد",
    nCreditos: "{{n}} من النقاط",
    compraPronto: "الشراء متاح قريبًا",
  },
  usar: {
    titulo: "استخدموا رصيدكم حسب ما تحتاجون",
    gratis: "<b>الوضوح</b> <g>مجاني</g>: فكرتكم مرتّبة، وجملتها المختصرة، وما لديكم وما تفترضونه. و<b>تشخيص أي عالم</b> <g>مجاني</g> أيضًا: نظرتكم الأولى إلى ذلك الجانب.",
  },
  proyecto: {
    etiqueta: "مشروعكم",
    plan: "خطتكم",
    planTexto: "رحلتكم كاملة، من الفكرة إلى تحقيقها: الخطة وكل ما يلزم لتنفيذها.",
    cambioRumbo: "تغيير في الاتجاه",
    cambioRumboTexto: "حين يحرّك الواقع خطتكم وتحتاجون إلى إعادة التفكير دون البدء من الصفر: تحكون ما حدث، ويُحفظ ما أنجزتموه، ويُعاد بناء رحلتكم من تلك النقطة.",
  },
  incluyePlan: [
    "<b>الخطة:</b> مراحلكم بمخرجاتها، ومهامكم ومواعيدكم في لمحة واحدة.",
    "<b>إلى العمل:</b> نفّذوا خطتكم. علّموا ما أنجزتموه، وأضيفوا ملاحظاتكم، وتابعوا تقدّمكم لحظة بلحظة. مشمول دائمًا.",
    "<b>أرقامكم:</b> لوحة فكرتكم (هامش الربح، ونقطة التعادل، والسيناريوهات). صحّحوا الأرقام وأعيدوا الحساب متى شئتم.",
    "<b>مستنداتكم:</b> خطتكم وكل ملخص، كملف وبصيغة PDF، للقراءة أو الحفظ.",
    "<b>سجلّ رحلتكم:</b> قصة رحلتكم، كل قرار فيها، محفوظ بالترتيب.",
  ],
  mundo: {
    etiqueta: "عالم",
    plan: "خطة عالم",
    planTexto: "جانب كامل من عملكم (الجودة، المخاطر، السلامة…)، بمساحته الخاصة داخل مشروعكم نفسه.",
    cambioRumbo: "تغيير في الاتجاه داخل عالم",
    cambioRumboTexto: "الشيء نفسه داخل ذلك الجانب، حين تحتاجون هناك إلى إعادة التفكير في الاتجاه.",
  },
  incluyeMundo: [
    "<b>خطته ومرحلة «إلى العمل» الخاصة به:</b> مراحل ذلك الجانب ومهامه ومواعيده، جاهزة للتنفيذ تمامًا مثل رحلتكم.",
    "<b>كل ما يخص العالم، على حدة:</b> تقدّمه ومستنداته وسجلّ رحلته، لذلك الجانب وحده.",
    "<b>ويُضاف إلى ملفكم الكامل:</b> المستند الوحيد الذي يجمع فكرتكم وخطتكم وكل عالم، كلٌّ في قسمه الخاص.",
    "<b>مشروع واحد:</b> ليس حسابًا آخر ولا فكرة أخرى.",
  ],
  mundosPorDesbloquear: "العوالم التي يمكنكم فتحها",
};

const hi: typeof es = {
  misIdeas: "मेरे विचार /",
  titulo: "क्रेडिट",
  disponibles: "{{saldo}} उपलब्ध",
  saldoNoDisponible: "बैलेंस उपलब्ध नहीं",
  creditos: "क्रेडिट",
  heroe: {
    tuSaldo: "आपका बैलेंस",
    noPudeLeer: "हम अभी आपका बैलेंस नहीं पढ़ सके। थोड़ी देर बाद पेज रीलोड करें।",
    garantiaCuenta: "हर काम की शुरुआत में आपका बैलेंस जाँचा जाता है और क्रेडिट डिलीवरी पर ही कटते हैं। अगर बीच में कुछ गड़बड़ हो जाए, तो कुछ भी नहीं कटता।",
    sinCuenta: "आपके क्रेडिट आपके खाते में रहते हैं। क्रेडिट जोड़ने और इस्तेमाल करने के लिए लॉग इन करें या अपना खाता बनाएँ।",
  },
  sumar: {
    titulo: "क्रेडिट जोड़ें",
    nCreditos: "{{n}} क्रेडिट",
    compraPronto: "खरीदारी जल्द शुरू होगी",
  },
  usar: {
    titulo: "अपने क्रेडिट अपनी ज़रूरत के हिसाब से इस्तेमाल करें",
    gratis: "<b>स्पष्टता</b> <g>मुफ़्त</g> है: आपका व्यवस्थित विचार, उसे बताने वाला एक वाक्य, जो आपके पास है और जो आपने मान रखा है। <b>किसी दुनिया का आकलन</b> भी <g>मुफ़्त</g> है: उस पहलू पर पहली नज़र।",
  },
  proyecto: {
    etiqueta: "आपकी परियोजना",
    plan: "आपकी योजना",
    planTexto: "आपकी पूरी यात्रा, विचार से उसे साकार करने तक: योजना और उसे पूरा करने के लिए सब कुछ।",
    cambioRumbo: "नई दिशा",
    cambioRumboTexto: "जब हालात आपकी योजना हिला दें और आपको शून्य से शुरू किए बिना फिर से सोचना हो: बस बताइए कि क्या हुआ, अब तक जो हासिल हुआ वह बना रहता है, और आपकी यात्रा वहीं से फिर से बनती है।",
  },
  incluyePlan: [
    "<b>योजना:</b> आपके चरण, उनके नतीजों, आपके कामों और आपकी तारीखों के साथ, एक नज़र में।",
    "<b>काम शुरू करें:</b> अपनी योजना पर अमल करें। जो हो गया उसे मार्क करें, अपने नोट जोड़ें और अपनी प्रगति तुरंत देखें। हमेशा शामिल।",
    "<b>आपके आंकड़े:</b> आपके विचार का डैशबोर्ड (मार्जिन, ब्रेक-ईवन बिंदु, परिदृश्य)। जब चाहें संख्याएँ सुधारें और फिर से गणना करें।",
    "<b>आपके दस्तावेज़:</b> आपकी योजना और हर सारांश, फ़ाइल और PDF में, पढ़ने या सहेजने के लिए।",
    "<b>आपकी लॉगबुक:</b> आपकी यात्रा की कहानी, हर फ़ैसला, क्रम से सहेजा हुआ।",
  ],
  mundo: {
    etiqueta: "एक दुनिया",
    plan: "एक दुनिया की योजना",
    planTexto: "आपके व्यवसाय का एक पूरा पहलू (गुणवत्ता, जोखिम, सुरक्षा…), आपकी उसी परियोजना के भीतर अपने अलग क्षेत्र के साथ।",
    cambioRumbo: "किसी दुनिया में नई दिशा",
    cambioRumboTexto: "उसी पहलू के भीतर यही सब, जब वहाँ आपको दिशा पर फिर से सोचना हो।",
  },
  incluyeMundo: [
    "<b>उसकी योजना और उसका काम शुरू करें:</b> उस पहलू के चरण, काम और तारीखें, आपकी यात्रा की तरह ही अमल के लिए तैयार।",
    "<b>दुनिया का सब कुछ, अलग से:</b> उसकी प्रगति, उसके दस्तावेज़ और उसकी लॉगबुक, सिर्फ़ उसी पहलू की।",
    "<b>और यह आपके पूरे ब्यौरे में जुड़ जाता है:</b> वह इकलौता दस्तावेज़ जो आपके विचार, आपकी योजना और हर दुनिया को एक साथ लाता है, हर एक अपने अलग हिस्से में।",
    "<b>एक ही परियोजना:</b> न कोई दूसरा खाता, न कोई दूसरा विचार।",
  ],
  mundosPorDesbloquear: "वे दुनियाएँ जिन्हें अनलॉक किया जा सकता है",
};

export const CREDITOS: PorIdioma<typeof es> = { es, en, fr, pt, de, it, ja, zh, ko, ar, hi };
