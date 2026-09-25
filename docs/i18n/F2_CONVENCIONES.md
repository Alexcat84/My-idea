# i18n F2: cómo se extrae un texto al catálogo (convenciones)

F2 saca **todo texto visible** de la app a catálogos en español, sin cambiar ni una letra de lo que
se ve. Diseño: `DISENO.md §3`. Base ya construida en `web/lib/i18n/`. Ejemplo completo: el piloto
`web/app/ui/NotaRapida.tsx` con su catálogo `web/lib/i18n/mensajes/notaRapida.ts`.

## La regla de oro
**Lo que se ve no cambia.** El texto va al catálogo **carácter por carácter** (acentos, comillas,
signos, espacios, puntos suspensivos `…`, mayúsculas). Nada de corregir, mejorar ni unificar textos
de paso: si un texto tiene un error, se copia con el error y se anota aparte. La prueba es
`npx tsx scripts/i18n/extraccion_identica.ts` (desde `web/`): toma todo texto que salió del código y
exige que esté tal cual en un catálogo.

## Qué se extrae y qué no
**Se extrae** (texto que ve una persona): texto de JSX, `placeholder`, `title`, `aria-label`,
`alt`, textos de botones, avisos, errores y mensajes que una ruta devuelve en `error`/`mensaje`/
`aviso` (o cualquier campo que la pantalla muestre), textos que arma `lib/` para la pantalla o para
los documentos (markdown, papel), nombres de estados, etiquetas de gráficos, textos de `confirm()`.

**No se extrae:** `console.log/warn/error` (los registros son para nosotros), mensajes de
excepciones internas que nunca llegan a pantalla, nombres de clases CSS, claves, ids, rutas, valores
que se guardan en la base o se comparan en código (p. ej. `estado === "hecho"`: ese literal es un
DATO; su **etiqueta visible** sí se extrae), los **prompts de la IA** (`lib/prompts.ts`,
`lib/assets/prompts.json`: van en F5), el contenido del grafo, comentarios.

## El catálogo
Un archivo por área en `web/lib/i18n/mensajes/<area>.ts` (nombre en camelCase, único; ej.
`manosALaObra.ts`, `servidorCuenta.ts`). Forma:

```ts
/** De qué pantalla o módulo son estos textos. */
import type { PorIdioma } from "../config";

const es = {
  guardar: "Guardar",
  haceMin: "hace {{n}} min",                       // variables con {{nombre}}
  planListo: "Tu plan <b>ya está</b> listo",        // partes marcadas con etiquetas propias
  creditos: { one: "{{n}} crédito", other: "{{n}} créditos" }, // plurales (Intl.PluralRules)
  estados: { pendiente: "pendiente", hecho: "hecho" },          // grupos anidados
};

export const MANOS: PorIdioma<typeof es> = { es };
```

- Claves en camelCase español, cortas y con sentido (`botonGuardar`, `avisoSinPlan`). Agrupar por
  sección con objetos anidados cuando el archivo es grande.
- Solo cadenas, objetos, listas de cadenas, y objetos de plural `{ one, other }`. **Nunca funciones**
  en el catálogo (el auditor no puede revisar una función).
- Variables: `{{nombre}}` + `interpolar(t.haceMin, { n })` (`@/lib/i18n/interpolar`).
- Plurales: `plural(idioma, n, t.creditos)` (`@/lib/i18n/interpolar`). Úsalo SOLO donde el código de
  hoy ya elige singular/plural; el resultado debe ser idéntico.
- Frases partidas por `<strong>`, `<em>`, `<a>`, `<br/>`: la frase ENTERA va en una clave con
  etiquetas propias y se pinta con `rico(t.clave, { b: (c) => <strong className="...">{c}</strong> })`
  (`@/lib/i18n/rico`, archivo `.tsx`; `<br/>` ya viene incluido). Así el traductor ve la oración
  completa. Si la frase tiene expresiones `{algo}` en medio, van como `{{marcador}}` y se interpola
  ANTES de `rico` (cuidado: el valor interpolado no debe contener `<`).
- El auditor (`lib/i18n/auditor.test.ts`) corre en la suite: mismas claves, mismos `{{}}` y mismas
  etiquetas en cada idioma, nada vacío, "My Idea" intacto.

## Cómo se eligen los textos según dónde estás
| dónde | cómo |
|---|---|
| componente del cliente (`"use client"`) | `const t = elegir(CATALOGO, useIdioma());` (`@/lib/i18n/config`, `@/lib/i18n/IdiomaProvider`). El hook va dentro del componente, arriba, como cualquier hook. |
| componente del servidor / página del servidor | `const t = elegir(CATALOGO, await idiomaDeCookies());` (`@/lib/i18n/servidor`) |
| ruta de `/api` | `const t = elegir(CATALOGO, idiomaDeRequest(request));` (`@/lib/i18n/servidor`) |
| función de `lib/` que arma texto | agrega un último parámetro `idioma: Locale = LOCALE_BASE` y usa `elegir(CATALOGO, idioma)`. Pásale el idioma desde los llamadores que lo tengan a mano (los de tu grupo); los demás quedan con el base por ahora. |
| constante exportada que usan muchos (`MENSAJE_…`) | el texto va al catálogo; la constante queda como `export const X = elegir(CAT, LOCALE_BASE).clave;` (el valor base, para no romper a quien la importa) y **las rutas y componentes de tu grupo** que la muestran eligen por idioma con el catálogo. |
| función de formato (fechas, dinero, decimales) | `@/lib/i18n/formato` (`dinero`, `entero`, `decimal`): idénticos al de hoy en español. |

Un componente de React que no es la raíz y recibe textos por props puede seguir recibiéndolos: lo
importante es que el texto NAZCA en un catálogo.

## Las pruebas que leen frases del código
Muchas pruebas hacen `readFileSync(componente)` y buscan una frase en español. Al extraer, la frase
se muda al catálogo y la prueba falla. **Arréglala para que siga probando lo mismo**: que busque la
frase en el archivo del catálogo (o que importe el catálogo y compare `CAT.es.clave`), y si probaba
que el componente la USA, que busque la clave (`t.clave`) en el componente. Nunca borres una prueba
ni la debilites; si una prueba fija una frase que no puedes mover sin cambiar su sentido, déjala y
repórtalo.

## Seguridad del árbol de trabajo (varios agentes a la vez)
- Trabajas en `C:\Users\AlexDesk\Documents\my-idea-arreglos`, rama `i18n`, **junto con otros agentes
  que editan otros archivos al mismo tiempo**.
- Toca **solo tus archivos** (tu lista) y los catálogos nuevos que crees (con nombre único de tu
  área). Si necesitas cambiar un archivo que no es tuyo, NO lo cambies: repórtalo.
- **Prohibido**: `git commit`, `git checkout`, `git stash`, `git reset`, `git restore`, `git clean`,
  `git merge`, `git pull`, formatear archivos ajenos, `pnpm install`. El commit lo hace quien coordina.
- `npx tsc --noEmit -p .` puede mostrar errores de archivos de otros agentes a medio hacer: juzga
  solo los tuyos.

## Cómo verificas tu grupo antes de terminar
1. `npx vitest run <tus pruebas y las de tus archivos>` en verde.
2. `npx tsc --noEmit -p .` sin errores **en tus archivos**.
3. `npx eslint <tus archivos>` sin errores.
4. `npx tsx scripts/i18n/extraccion_identica.ts`: sin faltantes **en tus archivos** (los de otros
   pueden aparecer a medio hacer).
5. Busca lo que se te pudo escapar: `grep` de comillas con letras en tus archivos.
