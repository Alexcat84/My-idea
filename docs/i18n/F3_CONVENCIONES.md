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

## Cómo se verifica un catálogo traducido
1. `npx tsc --noEmit -p .` sin errores en tu archivo.
2. `npx vitest run lib/i18n` verde (auditor: claves, marcadores, etiquetas, nada vacío, "My Idea").
3. Leer la traducción entera en voz alta: si suena a traducción, se reescribe.
