# i18n F3: cómo se traduce un catálogo (convenciones)

F3 agrega idiomas a `ACTIVE_LOCALES` (`web/lib/i18n/config.ts`). En cuanto un idioma está activo, el
compilador exige su versión de **cada** catálogo de `web/lib/i18n/mensajes/`. Orden del fundador
(24 sep 2026): **inglés** completo → visto; **francés** → visto; **los otros ocho** juntos, cada uno
con revisión de naturalidad de un segundo modelo. Diseño: `DISENO.md §6` (glosario, **manda**) y §7.
Extracción y forma de los catálogos: `F2_CONVENCIONES.md`.

## La forma
```ts
const es = { … };                       // NO se toca: el español es la base y ya está corregido
const en: typeof es = { … };            // mismas claves, misma forma
export const X: PorIdioma<typeof es> = { es, en };
```
Si el archivo tiene varios catálogos (`esLogin`, `esClaveNueva`…), cada uno gana el suyo (`enLogin`…).

## Lo intocable (el auditor lo revisa: `npx vitest run lib/i18n`)
- **Las claves**, y en `estadosTarea` y similares las claves que son valores de la base.
- **Los marcadores `{{nombre}}`**: los mismos, con el mismo nombre; se pueden mover dentro de la frase.
- **Las etiquetas propias** (`<b>…</b>`, `<correo/>`, `<palabra/>`…): las mismas; se pueden mover.
- **Los plurales `{ one, other }`**: las mismas formas que el español en `en`, `fr`, `pt`, `it`, `de`.
  (En `ja`, `zh`, `ko` basta `other` repetido en `one`; `ar` e `hi` ver su sección cuando lleguen.)
- **"My Idea"** jamás se traduce.
- Lo que va entre comillas simples dentro de un mensaje del servidor (`'respuesta'`, `'realizar'`,
  `'numeros'`) es el nombre de un campo o un valor de la API: **se deja tal cual**.
- La estructura markdown de los documentos (`#`, `**`, `-`, `_…_`, saltos de línea): igual.

## La voz (BANCO_DE_TEXTOS §3, en cada idioma)
- Le habla a **una** persona, en segunda persona, cálido y directo; palabras de persona, nunca
  maquinaria ni jerga de manual ("MVP", "pivot", "stakeholder" crudos: no).
- **Sin guiones largos ni medios** (— –): coma, dos puntos o punto. (Rayas que ya estén en el español
  como separador visual, p. ej. "—" solo como valor vacío, se conservan.)
- La unidad es la **idea**; "proyecto" solo se gana al final del viaje.
- Mayúsculas: como en el español (frase normal), salvo los términos del glosario, que van como en
  §6 ("Your Plan", "Get to Work").
- Puntos suspensivos con el carácter `…`. Las citas «…» del español van con las comillas del idioma
  (`en` “…”, `fr` « … », `de` „…“, `ja` 「…」, `zh` “…”); la bitácora las reconoce todas.
- Nada de "¿" ni "¡" fuera del español.
- Los mensajes del servidor que en español van en minúscula y sin punto final, igual en el otro idioma.

## Términos fijos en inglés (además del glosario §6)
| es | en |
|---|---|
| idea / proyecto | idea / project |
| acción (del checklist) / tarea | action / task |
| etapa / hito | stage / milestone |
| mundo / espacio | world / space |
| cara (de un espacio) | view |
| Seguimiento (el documento y el ritual) | Follow-up |
| Expediente / Bitácora / Cierre honesto | Full Record / Logbook / Honest Close |
| créditos / saldo / recarga | credits / balance / top-up |
| Recarga / Básico / Premium / Profesional (packs) | Top-up / Basic / Premium / Professional |
| potenciar / potenciador | power up / power-up |
| entrevista | interview |
| estados de tarea: sin empezar / apenas empezada / en proceso / hecha / no aplica | not started / just started / in progress / done / doesn't apply |
| retirar (una tarea) | set aside |
| Tus Números / Tu viaje / A mi ritmo / Con fechas | Your Numbers / Your Journey / At my own pace / With dates |
| margen / punto de equilibrio / costo fijo | margin / break-even point / fixed cost |
| doble factor, verificación en dos pasos / código / códigos de rescate | two-step verification / code / recovery codes |
| diagnóstico (de un mundo) / acta de cierre / registro (de un mundo de protección) / replanificación | diagnosis / closing record / {{mundo}} register / plan update |
| recorrido (lo explorado) | path |
| La Chispa (en frases: "la chispa") | The Spark ("the spark") |

## Términos fijos en los otros nueve idiomas (además del glosario §6)
Mismas filas que la tabla del inglés. Donde el glosario §6 ya fija un término (etapas, mundos,
Expediente, Bitácora, Tus Números, Créditos…), manda el glosario.

| es | fr | pt | de | it |
|---|---|---|---|---|
| idea / proyecto | idée / projet | ideia / projeto | Idee / Projekt | idea / progetto |
| acción / tarea | action / tâche | ação / tarefa | Schritt / Aufgabe | azione / attività |
| etapa / hito | étape / jalon | etapa / marco | Etappe / Meilenstein | tappa / traguardo |
| mundo / espacio / cara | monde / espace / vue | mundo / espaço / visão | Welt / Bereich / Ansicht | mondo / spazio / vista |
| Seguimiento | Suivi | Acompanhamento | Zwischenstand | Revisione |
| créditos (cuenta: "{{n}} …") / saldo / recarga | crédits / solde / recharge | créditos / saldo / recarga | Guthaben (cuenta: "{{n}} Punkte") / Guthaben / Aufladung | crediti / saldo / ricarica |
| packs Recarga / Básico / Premium / Profesional | Recharge / Essentiel / Premium / Professionnel | Recarga / Básico / Premium / Profissional | Aufladung / Basis / Premium / Profi | Ricarica / Base / Premium / Professionale |
| potenciar / potenciador | propulser / propulseur | potencializar / potencializador | stärken / Verstärker | potenziare / potenziatore |
| entrevista | entretien | entrevista | Gespräch | intervista |
| estados de tarea | pas commencée / tout juste commencée / en cours / faite / ne s'applique pas | não iniciada / recém-iniciada / em andamento / feita / não se aplica | nicht begonnen / gerade begonnen / in Arbeit / erledigt / trifft nicht zu | non iniziata / appena iniziata / in corso / fatta / non si applica |
| retirar (una tarea) | mettre de côté | deixar de lado | zurückstellen | mettere da parte |
| margen / punto de equilibrio / costo fijo | marge / seuil de rentabilité / coûts fixes | margem / ponto de equilíbrio / custo fixo | Marge / Gewinnschwelle / Fixkosten | margine / punto di pareggio / costi fissi |
| verificación en dos pasos / código / códigos de rescate | vérification en deux étapes / code / codes de récupération | verificação em duas etapas / código / códigos de recuperação | Bestätigung in zwei Schritten / Code / Wiederherstellungscodes | verifica in due passaggi / codice / codici di recupero |
| diagnóstico / acta de cierre / registro de {{mundo}} / replanificación | diagnostic / bilan de clôture / registre de {{mundo}} / mise à jour du plan | diagnóstico / ata de encerramento / registro de {{mundo}} / replanejamento | Diagnose / Abschlussprotokoll / Register für {{mundo}} / Planänderung | diagnosi / verbale di chiusura / registro di {{mundo}} / ripianificazione |
| recorrido | cheminement | percurso | Weg | percorso |
| palabra de borrado | SUPPRIMER | EXCLUIR | LÖSCHEN | ELIMINA |

| es | ja | zh | ko | ar | hi |
|---|---|---|---|---|---|
| idea / proyecto | アイデア / プロジェクト | 想法 / 项目 | 아이디어 / 프로젝트 | فكرة / مشروع | विचार / परियोजना |
| acción / tarea | アクション / タスク | 行动 / 任务 | 실행 항목 / 할 일 | إجراء / مهمة | कदम / काम |
| etapa / hito | ステージ / マイルストーン | 阶段 / 里程碑 | 단계 / 이정표 | مرحلة / محطة | चरण / पड़ाव |
| mundo / espacio / cara | ワールド / スペース / ビュー | 世界 / 空间 / 视图 | 월드 / 공간 / 보기 | عالم / مساحة / عرض | दुनिया / क्षेत्र / दृश्य |
| Seguimiento | フォローアップ | 跟进 | 후속 점검 | متابعة | फ़ॉलो-अप |
| créditos (cuenta) / saldo / recarga | ポイント / 残高 / チャージ | 点数 / 余额 / 充值 | 크레딧 / 잔액 / 충전 | رصيد (cuenta: "{{n}} نقطة") / رصيدكم / شحن | क्रेडिट / बैलेंस / रिचार्ज |
| packs | チャージ / ベーシック / プレミアム / プロフェッショナル | 充值包 / 基础版 / 高级版 / 专业版 | 충전 / 베이직 / 프리미엄 / 프로페셔널 | شحن / أساسي / مميّز / احترافي | रिचार्ज / बेसिक / प्रीमियम / प्रोफ़ेशनल |
| potenciar / potenciador | 強化する / 強化オプション | 赋能 / 赋能工具 | 강화하기 / 강화 옵션 | تعزيز / أداة تعزيز | सशक्त करना / सशक्त विकल्प |
| entrevista | インタビュー | 访谈 | 인터뷰 | مقابلة | बातचीत |
| estados de tarea | 未着手 / 着手したばかり / 進行中 / 完了 / 対象外 | 未开始 / 刚开始 / 进行中 / 已完成 / 不适用 | 시작 전 / 막 시작함 / 진행 중 / 완료 / 해당 없음 | لم تبدأ / بدأت للتو / قيد التنفيذ / منجزة / لا تنطبق | शुरू नहीं हुआ / अभी शुरू हुआ / प्रगति पर / पूरा / लागू नहीं |
| retirar (una tarea) | 外す | 搁置 | 제외하기 | استبعاد | अलग रखना |
| margen / punto de equilibrio / costo fijo | 利益 (1個あたり) / 損益分岐点 / 固定費 | 利润 (每件) / 盈亏平衡点 / 固定成本 | 마진 / 손익분기점 / 고정비 | هامش الربح / نقطة التعادل / التكاليف الثابتة | मार्जिन / ब्रेक-ईवन बिंदु / स्थिर लागत |
| verificación en dos pasos / código / códigos de rescate | 2段階認証 / コード / リカバリーコード | 两步验证 / 验证码 / 恢复码 | 2단계 인증 / 코드 / 복구 코드 | التحقق بخطوتين / رمز / رموز الاسترداد | दो-चरणीय सत्यापन / कोड / रिकवरी कोड |
| diagnóstico / acta de cierre / registro / replanificación | 診断 / 完了記録 / {{mundo}}の記録簿 / 計画の見直し | 诊断 / 结项记录 / {{mundo}}登记册 / 计划调整 | 진단 / 마무리 기록 / {{mundo}} 등록부 / 계획 조정 | تشخيص / محضر الإغلاق / سجل {{mundo}} / تعديل الخطة | आकलन / समापन रिकॉर्ड / {{mundo}} रजिस्टर / योजना में बदलाव |
| recorrido | これまでの道のり | 探索路径 | 탐색 경로 | المسار | रास्ता |
| palabra de borrado | 削除 | 删除 | 삭제 | حذف | हटाएँ |

## Reglas por idioma
- **fr**: tutoiement; neutro válido para Quebec (courriel, jamás "mail"/"e-mail"; sin giros solo de
  Francia; sin anglicismos). Espacio duro (U+00A0) antes de ":" y dentro de « »; nada antes de ; ! ?
- **pt**: Brasil, "você". **de**: "du", sustantivos con mayúscula. **it**: "tu".
- **ja**: です/ます, sin sujeto "あなた" salvo donde el glosario lo pone. Comillas 「」. Sin espacios
  entre palabras.
- **zh**: simplificado, "你". Puntuación de ancho completo（，。：？）; comillas “”.
- **ko**: 해요체. Comillas “” o ‘’.
- **ar**: árabe estándar moderno; **formas neutras primero** (D7): plural de cortesía (أنتم، ـكم،
  افعلوا) en vez del masculino singular. Cifras latinas. Plurales: el catálogo solo admite `one` y
  `other`, e Intl usa `other` para 0, 2, 3-10 y 11+: la forma `other` debe leerse bien con
  cualquier número (sustantivo antes de la cifra: "المهام: {{n}}", o construcciones sin
  concordancia).
- **hi**: आप; devanagari; términos técnicos en inglés solo si son los de uso común (कोड, क्रेडिट).
- **Fechas** (`fechas.ts`, `fechaCorta` de `hitos.ts` y `documentosPapel.ts`): el orden natural de
  cada idioma. ja/zh: `meses` "1月"…, `diaDeMes` "{{mes}}{{d}}日"; ko: "1월"…, "{{mes}} {{d}}일";
  de: "{{d}}. {{mes}}"; fr/it/pt/ar/hi: día y luego mes, meses del idioma (fr/it/pt en minúscula).
- **Plurales en ja, zh y ko**: Intl siempre elige `other`; `one` lleva el mismo texto.

## Cómo se verifica un catálogo traducido
1. `npx tsc --noEmit -p .` sin errores en tu archivo.
2. `npx vitest run lib/i18n` verde (auditor: claves, marcadores, etiquetas, nada vacío, "My Idea").
3. Leer la traducción entera en voz alta: si suena a traducción, se reescribe.
