# i18n F2: informe de cierre (pendiente del visto del fundador)

Rama `i18n`. Commits: `6a887b99` (la base), `124113cb` (la extracción), `1b495e32` (el hilo del
idioma). Convenciones: `F2_CONVENCIONES.md`. Diseño: `DISENO.md §3`.

## Qué quedó hecho
- **La base** (`web/lib/i18n/`): once idiomas con `ACTIVE_LOCALES = ["es"]` (calco del I Ching: el
  compilador exige los catálogos completos sobre los idiomas activos; F3 agrega los otros diez y el
  compilador reclama cada clave que falte), `elegir`, `interpolar`, `plural` (Intl.PluralRules),
  `rico` (frases enteras con partes marcadas), `useIdioma`, `idiomaDeRequest`, `idiomaDeCookies`,
  `formato` (dinero y decimales, idénticos en español), `LANG_DICTADO` (el dictado sigue al idioma;
  en español, `es-MX` como siempre).
- **La cookie y la negociación** en `proxy.ts`: `?lang=xx` manda en esa visita (D9) y actualiza la
  cookie `myidea_idioma`; si no, la cookie; en la primera visita, el `Accept-Language`; y si nada
  coincide, el español. `<html lang dir>` sale de la cookie en el layout.
- **La extracción**: todo texto visible de la app vive en **54 catálogos** en español
  (`web/lib/i18n/mensajes/`, unos 1.520 textos), en nueve áreas. Componentes con
  `elegir(CAT, useIdioma())`, páginas del servidor con `idiomaDeCookies`, rutas con
  `idiomaDeRequest`, funciones de `lib` con el parámetro `idioma`.
- **El hilo del idioma**: donde el código ya tiene el idioma a mano, elige por él (rutas, pantallas,
  preguntas del recorrido, dictado). Las constantes de siempre (`MENSAJE_…`, `ERROR_GENERICO`…)
  siguen existiendo con el valor en español y cada una tiene su función hermana por idioma.
- **El auditor** (en la suite y en el guardián): mismas claves, mismos `{{marcadores}}` y mismas
  etiquetas en cada idioma, nada vacío, "My Idea" intacto, ningún `Partial<Record<Locale`. Y
  `hiloIdioma.test.ts`: ninguna pantalla ni ruta muestra una constante base teniendo el idioma.

## Cómo se probó que nada visible cambió
1. **Verificador de extracción idéntica** (`web/scripts/i18n/extraccion_identica.ts`, probado con
   mutación): todo texto que salió del código está letra por letra en un catálogo. **1.657 textos
   revisados; un solo aviso, falso positivo comprobado a mano** (la frase de "Quedan N acciones…" de
   documentos se armaba con una plantilla anidada; sus dos variantes están enteras en el catálogo).
2. **Comparación lado a lado** por grupo: Manos a la Obra renderizada a HTML antes y después en 17
   escenarios, idéntica; Tus Números en 11 escenarios y el análisis en 2, idénticos; cada generador
   de documentos (Expediente, reporte, acta, registro, plan sin IA) byte a byte, idéntico.
3. **Capturas antes/después** de las pantallas públicas, compiladas localmente (main contra `i18n`),
   en escritorio (1240) y móvil (380). El texto visible se comparó letra por letra:

   | pantalla | texto | píxeles distintos |
   |---|---|---|
   | portada | idéntico | 0 % |
   | /login | idéntico | 0 % |
   | /nueva | idéntico | 0 % |
   | /auth/update-password | idéntico | 0 % |
   | /potenciadores | idéntico | 0 % |
   | /creditos | idéntico | 0,002 % y 0,003 % (suavizado de bordes) |
   | /cuenta | idéntico | 0 % |
   | /ideas | la misma pantalla de error en ambos (sin base de datos real); solo cambia el número aleatorio del error | 0,03 % y 0,1 % |

   Las pantallas con datos (una idea, Manos a la Obra, el calendario, los números) necesitan la base
   real: las cubren la comparación del punto 2 y **el visto del fundador en la vista previa**.
4. Suites: web 1.454 de 1.454, motor 27 de 27, tsc y eslint limpios. La vista previa compila.

## Un cambio técnico sin efecto visible
Las páginas que antes eran estáticas (`/login`, `/nueva`, `/auth/update-password`, la de "no
encontrada") ahora se generan en cada visita, porque el layout lee la cookie del idioma. Toda visita
ya pasa por `proxy.ts`; es lo que permite que en F3 la página llegue en su idioma desde el primer
cuadro. `<html>` lleva ahora `dir="ltr"` (sin efecto en español).

## Lo que queda para las fases siguientes
- **F5 (idioma del proyecto, D2):** el plan, los documentos, el .ics del calendario, el reporte y
  todo lo que se GUARDA siguen en español a propósito; los generadores ya reciben `idioma` y F5 les
  pasará el del proyecto. Decisión abierta para F5: los componentes de papel (`PlanDocumento`,
  `BitacoraPapel`…) eligen hoy sus etiquetas por el idioma de la interfaz.
- **F5 (lo que va a la IA):** prompts, `bloqueRealidad`, `seguimientoComposer`, los encabezados que
  la IA escribe y el código lee (`planParser`, Claridad), el grafo (D3).
- **F3:** "ELIMINAR" (la palabra de confirmación que el servidor compara: traducirla pide que el
  servidor acepte la del idioma); `Descargas` elige un ícono mirando si el título empieza con
  "Seguimiento" (se romperá en otro idioma; hace falta un campo en el índice); el plural de la unidad
  en Tus Números (`pluralDe` es regla del español); las comillas «…» que lee `Bitacora`.

## Errores de texto encontrados (NO corregidos: F2 no cambia textos; propuesta de tanda aparte)
- Sin tilde, en mensajes del servidor: "cuerpo invalido", "escribe un correo valido", "algo se atoro
  de nuestro lado" (entrar y registrar), "sesion no encontrada", "esa version no existe", "no vacio",
  "envia", "accion inválida", "debe ser un numero".
- Sin tilde, en pantalla o documentos: "# Tu plan de accion", "Tus numeros de verdad", la pregunta
  genérica "cuentame… donde estas parado… que es lo que mas…", en Tus Números "la mas directa",
  "Vender mas", "estos numeros", "tus numeros"; los textos del guardián de cifras (GIGO) sin tildes,
  con "--" y un "que que".
- Plurales mal armados: "unidads" (la unidad + "s" en la tarjeta de volumen y en Corregir cifras),
  "Quedan 1 acciones", "1 días" (idea realizada), "Una fecha ya pasó… Puedes moverlas".
- Inconsistencias: "Preparando..." con tres puntos (el resto usa "…"); el título de la portada con
  mayúscula y el h1 en minúscula; el 8 de la contraseña escrito a mano; dos redacciones del enlace
  vencido; "No pude leer tu saldo" (el resto dice "no pudimos"); el aviso de beta privada "…entres
  con tu contraseña o con Google: la lista es la misma." suena forzado; el "© 2026" fijo.

## Un defecto previo encontrado (no causado por F2, no corregido)
El ritual de fechas de Manos a la Obra puede romperse con `RangeError: Invalid time value` cuando una
tarea hecha o retirada no tiene fecha (la primera corrida muestra todas y solo las pendientes reciben
fecha). Ficha en `docs/PENDIENTES.md` (`ritual-fechas-sin-fecha`).
