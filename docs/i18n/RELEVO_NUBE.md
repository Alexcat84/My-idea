# Relevo del proyecto de idiomas a Claude Code en la nube

**Decisión del fundador (24 sep 2026):** el proyecto de idiomas de My Idea pasa a una sesión de
Claude Code en la nube. Este documento es todo lo que esa sesión necesita; no supone ningún chat
previo.

**UN SOLO ACTOR:** desde este relevo, **solo la sesión en la nube escribe en la rama `i18n`**. La
sesión local que hizo F0 a F2 ya no la toca. Otra sesión local trabaja en paralelo en el catálogo de
conocimiento (campaña de "fidelidad", ramas propias) y **sube a `main` con frecuencia**: por eso las
reglas de fusión de abajo.

## 1. Qué es el proyecto
My Idea (app Next.js en `web/`, motor Python en `engine/`, grafo de conocimiento en `dataset/`) pasa
a hablar **11 idiomas**: es, en, pt, fr, de, it, ja, zh, ko, ar, hi. El **español es la base**. El
grafo de conocimiento **se queda en español** (no se traduce). Diseño completo: `docs/i18n/DISENO.md`
(léelo entero antes de empezar; §3 arquitectura, §6 glosario, §7 decisiones, §8 plan por fases).

## 2. Estado exacto por fase (al relevo)

| fase | estado | commits |
|---|---|---|
| **F0** diseño, inventario, glosario, decisiones | **HECHA** | `cf55b1b2` (diseño), `06c1a06e` (decisiones D1-D9), `d2ce48df` (inventario de datos y borradores legales), `80d0a38f` (glosario y legales con las decisiones) |
| **F1** medición del buscador multilingüe | **HECHA** | `0debace9`; informe `docs/i18n/F1_BUSCADOR.md` |
| **F2** base de idiomas + todos los textos al catálogo en español, la app idéntica | **HECHA, CON VISTO DEL FUNDADOR, EN PRODUCCIÓN** | `6a887b99` (base), `124113cb` (extracción), `1b495e32` (hilo del idioma), `20c0250e` (informe `docs/i18n/F2_INFORME.md`); en `main` con `9361c569`, etiqueta `web-v2.7.0` |
| **F3** las otras 10 traducciones con el glosario; formatos por idioma | **HECHA, CON VISTO DEL FUNDADOR, EN `main`** (sin interruptor, decisión del 25 sep 2026) | `73811801` … `ed8dd15a`; informes `F3_INFORME_EN.md` y `F3_INFORME_OTROS.md`; en `main` con `434a9c1b`, etiqueta `web-v2.8.0` |
| **F4** árabe RTL; tipografías CJK y devanagari solo al elegirlas; capturas de cada una | **HECHA, CON VISTO DEL FUNDADOR (25 sep 2026), EN `main`** | `434a9c1b` (`F4_INFORME.md`); `main` avanzó por avance rápido `9361c569..434a9c1b` |
| **F5** idioma del proyecto (`projects.idioma`, migración 046), prompts con idioma de salida, remedio del buscador, plantillas de los generadores sin IA, D3; **más** los idiomas fuera de los once y el conteo anónimo (decisión del 25 sep 2026) | **HECHA, PENDIENTE DEL VISTO** y de aplicar la 046 (`F5_INFORME.md`) | `ccd91a19` … `c00f3570` |
| **F6** correos (D4), documentos, la elisión del italiano ("l'8 marzo", decisión del 25 sep 2026), legales (D5, francés obligatorio), SEO y `hreflang` (D9); auditor y guardias de frases por idioma | por hacer | — |

### Lo que F2 dejó construido (y cómo se usa)
- `web/lib/i18n/config.ts`: `LOCALES` (11), **`ACTIVE_LOCALES = ["es"]`** (los que se sirven hoy),
  `LOCALE_BASE = "es"`, `PorIdioma<T> = Record<ActiveLocale, T>`, `elegir(CAT, idioma)`,
  `htmlLang`, `htmlDir`, `NOMBRE_IDIOMA`, `LANG_DICTADO` (la variante del dictado por voz).
  **F3 empieza agregando idiomas a `ACTIVE_LOCALES`: el compilador reclamará cada clave de cada
  catálogo que falte en ese idioma** (patrón del I Ching).
- 54 catálogos en `web/lib/i18n/mensajes/*.ts` (unos 1.520 textos), cada uno `const es = {…};
  export const X: PorIdioma<typeof es> = { es };`. Convenciones: `docs/i18n/F2_CONVENCIONES.md`
  (variables `{{n}}` con `interpolar`, plurales `{ one, other }` con `plural`, frases con partes
  marcadas con etiquetas propias y `rico()`).
- `proxy.ts` negocia el idioma: `?lang=xx` (D9) > cookie `myidea_idioma` > `Accept-Language` >
  español; escribe la cookie. El layout pone `<html lang dir>` desde la cookie.
- Componentes: `elegir(CAT, useIdioma())`; páginas del servidor: `idiomaDeCookies()`; rutas:
  `idiomaDeRequest(request)`; funciones de `lib`: último parámetro `idioma` (base por omisión).
- `web/lib/i18n/formato.ts`: `dinero`, `entero`, `decimal` (en español, idénticos a lo de antes;
  **F3 decide el formato de cada idioma**).
- Lo que F2 dejó a propósito para después: ver `docs/i18n/F2_INFORME.md` ("Lo que queda para las
  fases siguientes"). Incluye para **F3**: la palabra "ELIMINAR" que el servidor compara, el ícono de
  `Descargas` elegido por el título en español, el plural de la unidad en Tus Números (`pluralDe`),
  las comillas «…» que lee `Bitacora`; y la lista de **~30 errores de texto en español** encontrados y
  NO corregidos (el fundador decide si se corrigen en una tanda aparte; si se corrigen, que sea antes
  de traducir esos textos).

## 3. Las decisiones del fundador (resumen; lo que manda es `DISENO.md §7`)
- **D1. Glosario APROBADO** (`DISENO.md §6`), con cuatro ajustes suyos (en "Get to Work", en "From
  Workshop to Customer", fr "Propulse ton idée", de "Richtig einkaufen"). La **revisión de
  naturalidad por un segundo modelo, exigida antes de F3, YA SE HIZO** (`DISENO.md §6`, "Revisión de
  naturalidad"): lo evidente se aplicó y los 8 discutibles los aprobó el fundador el 26 sep 2026. F3
  usa las tablas de §6 **tal cual**. "My Idea" no se traduce jamás.
- **D2.** La interfaz sigue la preferencia del usuario (cookie); el plan y los documentos siguen el
  **idioma del proyecto** (se detecta de la idea, F5).
- **D3.** Etiquetas del riel en traducción **derivada** por idioma (archivos aparte; el grafo no se
  toca), y fuera del español las preguntas las adapta la IA. El auditor exige etiqueta en cada idioma
  para todo nodo vivo.
- **D4.** Sí al Send Email Hook de Supabase con Resend y el catálogo; los pasos de configuración se
  entregan al fundador en F6.
- **D5.** Textos legales: borradores en `docs/legal/` (Quebec, Canadá; responsable: Alexis Adalberto
  Antonio García Hurtado, empresa individual, nombre a confirmar contra Revenu Québec; contacto
  privacidad@myideaproject.com), marcados BORRADOR, **no enlazados desde la app** hasta que el
  fundador los apruebe. La versión francesa será obligatoria.
- **D6.** Formato por idioma con `Intl`, símbolo "$" por ahora; la moneda por proyecto es función
  futura (ficha `moneda-por-proyecto` en `docs/PENDIENTES.md`).
- **D7.** `pt` de Brasil, `zh` simplificado (`zh-Hans`), `fr` neutral válido para Quebec, el registro
  de §6 (tú; `ja` です/ます; `ko` 해요체; `ar` estándar moderno; `hi` आप). En árabe, **formas neutras
  primero** y el masculino gramatical solo sin alternativa.
- **D8.** `docs/BANCO_DE_TEXTOS.md` es el canon en español; en los otros idiomas, el catálogo; las
  guardias de frases prohibidas corren sobre cada uno.
- **D9.** `?lang=xx` en la URL manda en esa visita y actualiza la cookie; los `hreflang` apuntan a
  esas variantes.
- **F1 y su remedio:** Voyage entiende la idea en los 11 idiomas (solape temático al nivel de una
  paráfrasis en español), pero fuera del español las puntuaciones salen más bajas y el umbral
  `MIN_SCORE_SALTO = 0,3` deja la mitad de los saltos (2,8 a 3,25 candidatos contra 7,35). **Remedio
  aprobado para F5:** traducir la CONSULTA al español (Haiku) antes de buscar; el grafo no se toca; si
  la traducción falla, se busca con el original y la caída queda registrada. Descartado: bajar el
  umbral por idioma.

## 4. Montar el entorno en la nube
```bash
# 1) Los hooks del repo: el guardián de commit (.githooks/pre-commit) corre el motor, tsc sobre web/
#    si el commit toca web/, y la suite web. Sin esto no hay guardián.
git config core.hooksPath .githooks
#    (el hook va con permiso de ejecución desde el relevo: sin él, git lo IGNORA en Linux y lo dice
#    solo con un "hint"; en Windows corre igual)

# 2) Python (el motor y Gate 0). Python 3.12.
pip install anthropic python-dotenv      # sentence-transformers es opcional (índice local), no hace falta

# 3) Web. Node 24 y pnpm 10 (en local: node v24.5.0, pnpm 10.33.2).
cd web && pnpm install --frozen-lockfile
```
**Comandos exactos** (desde `web/` salvo que se diga):

| qué | comando |
|---|---|
| tipos | `npx tsc --noEmit -p .` (si falla por tipos viejos de Next: `rm -rf .next/types`) |
| lint | `npx eslint <archivos>` o `pnpm lint` |
| suite web | `npx vitest run` (si la máquina va lenta: `--maxWorkers=4`) |
| build | `pnpm build` con variables de relleno NO secretas: `NEXT_PUBLIC_SUPABASE_URL=http://127.0.0.1:9 NEXT_PUBLIC_SUPABASE_ANON_KEY=relleno SUPABASE_URL=http://127.0.0.1:9 SUPABASE_ANON_KEY=relleno SUPABASE_SERVICE_ROLE_KEY=relleno pnpm build` |
| auditor de claves (catálogos) | `npx vitest run lib/i18n` (auditor: mismas claves, `{{marcadores}}` y etiquetas en cada idioma, nada vacío, "My Idea" intacto; `hiloIdioma.test.ts`: nadie muestra una constante base teniendo el idioma) |
| extracción idéntica | `npx tsx scripts/i18n/extraccion_identica.ts [base]` (lo que salga del código debe estar letra por letra en un catálogo; hoy da 1 falso positivo conocido en `app/api/project/[id]/documentos/route.ts`, la plantilla anidada de "Quedan N acciones…") |
| suite del motor | desde la raíz: `python engine/run_all_tests.py` (27 de 27) |
| Gate 0 | desde la raíz, **SIEMPRE este ciclo y en este orden** (corrección del fundador, 24 sep 2026): `python scripts/etiquetas_de_cara.py --aplicar` → `python scripts/sync_assets_web.py` → `python scripts/run_phase1.py --reaplico-curaduria` → debe decir `GATE 0: OK`. Después, si `dataset/metadata/master_graph.json` quedó modificado sin tocarlo a propósito: `git checkout -- dataset/metadata/master_graph.json` (no se commitea). Necesita `pip install rapidfuzz numpy`. **Correr `run_phase1.py` solo, sin el paso de etiquetas, da un falso `FALLIDO`** ("71 nodos divergentes", todos `etiqueta_arbol`): no es un rojo de `main`, es el ciclo a medias. |

Las suites no necesitan claves: ningún test cambia de veredicto según haya o no secretos
(AGENTS.md).

## 5. Las reglas
- **No tocar `dataset/`** (ni `engine/`, salvo lo que una fase diga: F5 toca los prompts de
  `engine/prototipo_motor.py` y se re-sincronizan a `web/lib/assets/prompts.json`).
- **Prueba en rojo primero** donde aplique (una función nueva, un arreglo): el valor esperado sale
  de un cálculo a mano escrito en el test, nunca de copiar lo que la función devuelve (AGENTS.md).
- **Commit y push frecuentes** a `i18n`. El guardián corre en cada commit; **nunca `--no-verify`**.
- **Traer `main` a `i18n` al menos una vez al día** (`git fetch origin && git merge origin/main`) y
  resolver los choques **en el acto**; tras cada fusión, suites y Gate 0 en verde antes del push.
- **Nada va a `main` sin el visto del fundador en la vista previa de Vercel** de la rama `i18n`:
  https://my-idea-git-i18n-alexs-projects-e8bf95b4.vercel.app (la abre el fundador con su sesión de
  Vercel). Al subir a `main`: `git fetch`, fusionar `origin/main`, suites verdes, comprobar que
  `origin/main` no se movió (`git merge-base --is-ancestor origin/main HEAD`) y solo entonces push.
- **Nada visible cambia en español** al traducir: F3 solo agrega idiomas; el auditor y la extracción
  idéntica lo vigilan. Ningún texto en español se "mejora" de paso.
- Reglas de la casa que siguen vigentes: los precios solo en `web/lib/precios.ts`; la etiqueta del
  árbol (`etiqueta_arbol`) en las superficies de navegación; `docs/BANCO_DE_TEXTOS.md` para voz y
  claims (AGENTS.md completo en la raíz).
- **Reportes** al fundador: abren con la fase y su estado, o con "NECESITO AL FUNDADOR" y por qué.

## 6. Lo que la nube NO puede hacer
- **Nada que requiera claves.** Ninguna clave se sube ni se configura en la nube (ni Anthropic, ni
  Voyage, ni Supabase, ni Upstash, ni Resend, ni Vercel). El repo no tiene ninguna y así se queda:
  `.env.example` (raíz y `web/`) lista las variables **sin valores**.
- **Las pruebas con la IA real** (entrevista, plan, traducción de consultas de F5) **se hacen en la
  vista previa de Vercel** de la rama `i18n`, que sí tiene las claves configuradas. La nube prepara el
  código y las pruebas deterministas; el fundador mira la vista previa.
- **Las migraciones las aplica el fundador** en el SQL Editor de Supabase. La nube escribe el archivo
  en `supabase/migrations/` (siguiente número libre: **046**) y su bloque en
  `supabase/migrations/my_idea_check_migraciones.sql` (SQL plano, sin funciones), y se lo pide.
- **Traducir con un modelo en la nube** no es posible sin clave: las traducciones de F3 las escribe
  la propia sesión (es un modelo) siguiendo el glosario, o se preparan para que el fundador las
  genere; nunca con una clave subida al entorno.

## 7. Seguridad comprobada al relevo
- Ningún `.env` real en el árbol ni en el historial (ningún archivo `.env` fue agregado jamás en
  ninguna rama; solo los `.env.example`).
- Búsqueda en el historial de la rama de claves con forma de API (Anthropic `sk-ant-`, Resend `re_`,
  Voyage `pa-`, JWT, GitHub, AWS): **ninguna**.
- Lo único en el historial es la contraseña del usuario de desarrollo de la Fase 3.2 (commits de
  julio de 2026 anteriores a `c8246035`): ya salió del código en `c8246035` y **se rotó** en Supabase
  Auth (AGENTS.md, "Ninguna credencial en archivos versionados"). Está quemada y sin valor.

## 8. Por dónde empieza la nube (F3)
1. `git config core.hooksPath .githooks`, instalar, correr todo lo de §4 en verde.
2. Leer `DISENO.md` completo, `F2_CONVENCIONES.md`, `F2_INFORME.md` y el glosario §6.
3. Preguntar al fundador (si no lo dijo) si la tanda de errores de texto en español va antes de F3.
4. Agregar un idioma a `ACTIVE_LOCALES` (sugerido: `en` primero), completar sus catálogos con el
   glosario, formatos de ese idioma en `formato.ts`, pruebas; vista previa; visto; y así con los demás
   (o por grupos, como decida el fundador).

## 9. F3 en la nube: lo hecho y el punto de espera (25 sep 2026)
- **Entorno:** Node 22 y pnpm 10.33.0 en el contenedor (no 24): tsc, suites y extracción idéntica
  en verde igual. Python 3.11 con `anthropic python-dotenv rapidfuzz numpy`.
- **Hecho (`73811801`), sin cambiar nada visible en español:** formatos de cada idioma en
  `formato.ts` (D6, cifras latinas en todos); el ícono del Seguimiento por un campo del índice; la
  cita del motivo de la bitácora con las comillas de cada idioma (`lib/i18n/comillas.ts`);
  `pluralDe(unidad, idioma)`; la palabra de borrado por idioma (`lib/i18n/palabraEliminar.ts`, el
  servidor acepta la del idioma y siempre "ELIMINAR").
- **Un error más del español, no corregido:** `pluralDe("kit")` da "kites" (se suma a la lista de
  `F2_INFORME.md`).
- **Decisiones del fundador (24 sep 2026), respuesta a ese punto de espera:**
  a. **Primero los errores del español:** la tanda de `F2_INFORME.md` más "kites", con prueba en rojo
     donde aplique, antes de traducir cualquier texto afectado.
  b. **Traducción por grupos:** primero **inglés completo** → vista previa → visto; después
     **francés** (neutro, válido para Quebec, sin anglicismos) → visto; después los **otros ocho
     juntos**, cada uno con la revisión de naturalidad de un segundo modelo (lo evidente se aplica, lo
     discutible sube al fundador).
  c. **Cifras latinas en todos los idiomas, árabe incluido: APROBADO.**
- **Gate 0:** el `FALLIDO` que anoté arriba era el ciclo a medias (ver §4, el orden exacto); con el
  ciclo completo da `GATE 0: OK`.
- **Inglés (grupo 1): hecho, pendiente del visto.** Informe en `F3_INFORME_EN.md` (qué sigue en
  español a propósito hasta F5, elecciones de traducción, errores del español). Convenciones y
  términos fijos para los siguientes idiomas: `F3_CONVENCIONES.md`. Siguiente: el **francés** (neutro,
  válido para Quebec, sin anglicismos), solo después del visto del inglés.
- **Los otros nueve idiomas: hechos, pendientes del visto** (decisión del fundador del 25 sep:
  seguir con todos hasta terminar). Informe con los discutibles de cada idioma, los errores del
  español que quedan para el fundador y lo pendiente para F4: `F3_INFORME_OTROS.md`. Cómo se
  traduce o corrige un idioma sin chocar: `scripts/i18n/traducir.ts` (exportar, validar, aplicar).

## 10. F3 y F4 en `main`; F5 en curso (25 sep 2026)
- **Visto del fundador a F4 (25 sep 2026). Decisión:** F3 y F4 pasan a `main` **sin interruptor**
  (no hay usuarios activos hasta que termine el proyecto de idiomas). `main` avanzó por avance
  rápido a `434a9c1b`, con suites, tsc, lint, build y Gate 0 en verde antes.
- **La etiqueta `web-v2.8.0`** existe anotada en el clon de la nube, sobre `434a9c1b`, pero el proxy
  de git de la nube rechaza empujar etiquetas (HTTP 403; las ramas sí pasan). La crea el fundador:
  `git fetch origin && git tag -a web-v2.8.0 434a9c1b -m "i18n F3 y F4" && git push origin web-v2.8.0`,
  o en GitHub → Releases con la etiqueta `web-v2.8.0` sobre `434a9c1b`. El sello en vivo
  (`v·434a9c1`) lo comprueba el fundador: la nube no alcanza producción.
- **"il 8 marzo" en italiano** (la elisión "l'8 marzo") va a **F6**.
- **F5** sigue en la rama `i18n`, con dos añadidos del fundador: los **idiomas fuera de los once**
  (una idea escrita en otro idioma) y el **conteo anónimo** de los idiomas en que se escribe. La
  migración queda escrita con su nombre y la aplica el fundador en Supabase.
- **F5 hecha, pendiente del visto** (`F5_INFORME.md`, discutibles del riel en
  `F5_DISCUTIBLES_RIEL.md`). La migración 046 (`my_idea_046_idioma_del_proyecto.sql`) la aplica el
  fundador; el código funciona con y sin ella.
- **Para mantener las etiquetas del riel** (D3): si el grafo gana nodos, `etiquetasRiel.test.ts`
  falla. `cd web && npx tsx scripts/i18n/etiquetasRiel.ts exportar <idioma> <salida.json> --lote 800`
  exporta solo las que faltan; se traducen con las reglas de F3 y se aplican con `aplicar`.
