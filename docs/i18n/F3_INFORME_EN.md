# i18n F3, grupo 1: el inglés (pendiente del visto del fundador)

Rama `i18n`. Orden del fundador (24 sep 2026): primero los errores del español, después el inglés
completo con su visto, luego el francés, luego los otros ocho. Convenciones: `F3_CONVENCIONES.md`.

## Qué quedó hecho
- **`ACTIVE_LOCALES = ["es", "en"]`.** Los 56 catálogos tienen su versión en inglés (unos 1.540
  textos). El compilador y el auditor (mismas claves, marcadores, etiquetas, nada vacío, "My Idea"
  intacto) están en verde.
- **Los nueve mundos** se nombran en el idioma de la interfaz (glosario §6) con su promesa:
  catálogo `mensajes/mundos.ts`. Su español es copia de `packs_catalog.json`, y una prueba falla si
  las dos copias dejan de coincidir. Se nombran así en las pantallas, las pestañas, las vitrinas de
  créditos y Potencia tu idea, la bitácora, el calendario, Mis ideas y los avisos de las rutas.
- **Selector de idioma, manual y opcional** (el automático por cookie y navegador sigue mandando).
  Decisión del fundador del 25 sep: a la derecha de **toda** pantalla. En cada cabecera (portada,
  Mis ideas, la idea, créditos, cuenta, potenciadores) va un globo con "ES"/"EN", que en móvil queda
  solo en globo. En las pantallas sin cabecera (acceso, idea nueva, contraseña) va fijo arriba a la
  derecha. También está en el pie de la portada y en /cuenta. Al tocarlo aparecen los idiomas, cada
  uno escrito en su propio alfabeto. Elegir uno recarga la página con `?lang=xx` y `proxy.ts` escribe
  la cookie (D9).
- **Ver la vista previa con sesión iniciada:** el inicio con Google (y el enlace de los correos)
  vuelve a la dirección que Supabase tiene autorizada. Si la de la vista previa no está en
  Authentication → URL Configuration → Redirect URLs, te devuelve a producción (`main`), que solo
  habla español. Con correo y contraseña te quedas en la vista previa.
  Comprobado en el navegador: un navegador en inglés entra en inglés; al elegir Español se queda en
  español también en las páginas siguientes.
- **Formatos en inglés:** "$1,200", fechas "March 20" / "Friday, March 20", fecha corta del mapa
  de hitos "Feb 3" (antes el orden día-mes estaba fijo en el código), la palabra de borrado
  "DELETE" y el plural de la unidad ("candles", "boxes").
- **Revisado en el navegador** (compilado local, sin base de datos): la portada, /login, /nueva,
  /auth/update-password y /creditos en inglés, sin restos de español.

## Lo que sigue en español dentro de la interfaz en inglés (a propósito, no es un olvido)
Todo esto depende del **idioma del proyecto** (D2), que llega en **F5**:
- Todo lo que escribe la IA: preguntas de la entrevista, la Claridad, el plan y los seguimientos.
- Las etiquetas del riel y las preguntas que vienen del grafo (D3: traducción derivada, F5).
- Los documentos y sus títulos en Descargas (Expediente, plan, bitácora, informe, acta, registro),
  el plan básico sin IA y el calendario `.ics`.
- Los correos de Supabase (D4, F6) y los textos legales (D5, F6).

## Elecciones de traducción para tu visto
- Eslogan: "Turn your creativity into action". "Un interlocutor serio": "a serious sounding board".
- "Verificación en dos pasos": "two-step verification". "Códigos de rescate": "recovery codes".
- "Diagnóstico" de un mundo: "diagnosis". "Acta de cierre": "closing record".
  "Registro de {mundo}": "{mundo} register". "Replanificación": "plan update". "Recorrido": "path".
- "Frente" (un mundo como área del negocio): "area". "El cierre" como hito: "The close".
- Estados de una tarea: not started / just started / in progress / done / doesn't apply.
  "Retirar" una tarea: "set aside".
- "Mi idea" (nombre del calendario): "My idea", con "idea" en minúscula para no confundirlo con la
  marca.
- Las fechas se pasan de largo sin regañar: "date passed", no "overdue".

## Errores del español
- **Corregidos antes de traducir** (decisión a): toda la tanda de `F2_INFORME.md`, "kites" (y
  "camiónes"), y tres errores que aparecieron al traducir: la raya en "Primero explora «…» — …"
  (la voz la prohíbe), "Manos a la obra" sin la mayúscula del glosario (3 textos) y "MVP" en el
  ejemplo de la portada ("Calidad y diseño en tu primera versión"). La guardia
  `lib/i18n/ortografiaEs.test.ts` impide que vuelvan.
- **Sin corregir, para tu decisión:**
  - En Tus Números, "precio al que **la** vendes hoy" y "lo que te cuesta hacer**la**" suponen que
    la unidad es femenina. Con "pan" se leería "el pan… la vendes".
  - Los espejos en Python de la pregunta genérica (`engine/prototipo_motor.py`) y del guardián de
    cifras (`engine/calculadora.py`) siguen sin tildes. La web no los usa, y `engine/` queda fuera
    de F3.
  - "Realizada" en los hitos, frente a "Realizado" en el glosario. Parece concordancia con "idea" y
    no se tocó.

## Para F5 (lo encontró la traducción)
- `lib/engine/checklist.ts` y `lib/planParser.ts` solo entienden "## Etapa N:", "Esta semana" y
  "_Plan completo_". Hoy no se rompe nada, porque el plan básico se genera en español. Cuando el
  plan salga en otro idioma, hacen falta los marcadores neutros de `DISENO.md §5`.
- La pregunta genérica mete `titulo_concepto` en la pregunta; conviene revisarla contra la regla
  "la etiqueta enamora" (AGENTS.md).
