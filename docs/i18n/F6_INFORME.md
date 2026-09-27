# i18n F6: correos, documentos, legales, SEO y guardias (HECHA, con visto del fundador)

**Visto del fundador (25 sep 2026):** hook de correos activado y probado (un registro nuevo con el
correo en chino llegó y la cuenta de prueba se borró limpia), documentos en el idioma correcto,
`robots.txt` y `sitemap.xml` respondiendo. Legales en francés con "vous": aprobados, sin enlazar
hasta la revisión profesional. En `main` con la etiqueta `web-v2.10.0`: **el proyecto de idiomas
queda CERRADO.**

Rama `i18n`, commit `55cbb5af`. Diseño: `DISENO.md §3.6, §4` y las decisiones D2, D4, D5, D8, D9.
Sin migraciones: F6 no toca la base.

## Lo que hace falta del fundador
1. **Configurar el hook de correos** (D4), paso a paso en `F6_CORREOS.md`. Orden obligatorio: el
   código en producción primero; después el secreto `SEND_EMAIL_HOOK_SECRET` en Vercel (Production y
   Preview, mismo valor: hay un solo proyecto de Supabase) y el redespliegue; y solo al final activar el
   hook en Supabase. Si el hook se activa antes de que exista la ruta, ningún registro recibe su correo.
   Para volver atrás basta con desactivarlo: Supabase vuelve a sus plantillas.
2. **El visto de F6**, en producción (la vista previa redirige el acceso a producción).
3. **Los legales en francés** (`docs/legal/fr/`) quedan como borradores sin enlazar, igual que los de
   español, hasta tu aprobación y la del profesional. El traductor usó "vous", que es el registro
   habitual de un texto legal en Quebec, aunque la app diga "tu": decisión tuya o del profesional.

## Qué quedó hecho
- **Correos (D4):** los correos de Supabase (confirmar cuenta, entrar con enlace, recuperar la
  contraseña, cambio de correo, reautenticación y siete avisos de seguridad) los escribe la app en el
  idioma guardado de cada persona (`user_metadata.idioma`), por el Send Email Hook con Resend
  (`web/app/api/auth/hook-correo`, firma Standard Webhooks verificada con node:crypto, falla cerrado).
  El idioma se guarda al registrarse, al entrar con contraseña y al entrar con Google. El correo del
  doble factor sale en el idioma de la interfaz, con `lang` y `dir` (el árabe, de derecha a izquierda).
- **Documentos (D2):** Expediente, bitácora, informe, acta, registro, reporte y cada ciclo del plan,
  en .md y en PDF, salen en el idioma de la idea (`idiomaDeDocumentos`: el de la idea si es de los
  once; si no, el de la interfaz; una idea anterior a F5 cuenta como español). El papel impreso lleva
  `lang` y `dir` y la tipografía de su escritura (`PapelEnIdioma`). El plan en pantalla también sigue
  el idioma de la idea; botones y navegación siguen la interfaz.
- **Fechas:** la elisión del italiano ("l'8 marzo", "dall'11 aprile"; nunca ante "1º"), el primero
  del mes como ordinal en italiano ("1º marzo") y en francés ("1er mars").
- **Respaldos sin IA:** las listas de palabras de `readiness.ts` y `familiasDesdeEncabezados` entienden
  los once idiomas; fuera de ellos, la degradación queda registrada (evento
  `respaldo_familias_sin_palabras` y un aviso en el registro), nunca en silencio.
- **Legales (D5):** `docs/legal/fr/` con Confidentialité, Conditions, Témoins e Inventaire des
  données, traducción fiel con la terminología de la Ley 25.
- **SEO (D9):** metadatos por idioma, `hreflang` de los once más `x-default` hacia las variantes
  `?lang=xx`, canónica propia de cada variante, `robots.txt` (solo la portada se indexa) y
  `sitemap.xml`. `robots.txt` y `sitemap.xml` son rutas públicas en `proxy.ts`: un buscador no acuña
  una identidad invisible.
- **Guardias por idioma (D8):** `frasesProhibidas.ts`, once reglas del BANCO con sus patrones en los
  once idiomas (rayas, "...", jerga cruda, el trato en plural, el regaño, "a medias", los claims
  prohibidos y las frases muertas), barridas sobre todo el catálogo y las etiquetas del riel. Siete
  etiquetas del riel en alemán, italiano y portugués trataban de "ustedes" y quedaron en "tú".

## Arreglos encontrados en el camino
- Las cajas de mundos de Descargas no recibían su Reporte ni su Registro con la interfaz en otro
  idioma (nombraban los mundos en español).
- La bitácora impresa y la portadilla de cada ciclo ponían las fechas en español en todos los idiomas.
- El calendario y el mapa de hitos armaban fechas sin el ordinal del primero del mes.

## Antes de cerrar: las 41 etiquetas corregidas y la guardia de vigencia
- La sesión del dataset corrigió en `main` 41 etiquetas en español (`6871a11e`: las tres dudas de
  F5; `0f46772d`: 38 más). Sus traducciones se habían derivado del español viejo. Se volvieron a
  derivar las 41 en los diez idiomas: un modelo tradujo desde el español nuevo (con el viejo, el título
  y la traducción anterior como contexto) y un segundo modelo (Sonnet) revisó. Cuatro correcciones
  evidentes aplicadas (en `capital_social_founder` y `warrants_financiamiento`, ko
  `warrants_financiamiento`, de `sintesis_hipotesis_modelo_negocio`) y seis discutibles aplicados con
  la regla del fundador (la versión del revisor salvo choque con el glosario; ninguna chocaba): en y de
  `autoacusacion_antes_mala_noticia`, fr `aprobacion_alta_direccion` y `rol_green_belt_six_sigma`, ko
  `acuerdo_de_co_venta_y_votacion`, hi `clausula_personas_clave_banker`.
- **La guardia de vigencia** (`lib/i18n/etiquetasVigencia.test.ts`, `lib/i18n/vigenciaEtiquetas.ts`):
  cada etiqueta traducida guarda la huella (SHA-256, 12 hex) del español del que salió, en
  `lib/i18n/etiquetas/huellas/<idioma>.json`. Si el español cambia, la guardia falla hasta que se vuelva
  a traducir. En rojo primero: con las huellas del español viejo, marcó exactamente 41 vencidas en cada
  idioma (la guardia de F5 las dejaba pasar porque solo exigía que existiera una traducción).
  `scripts/i18n/etiquetasRiel.ts exportar` saca ahora las que faltan **y las vencidas**, y `aplicar`
  guarda la huella nueva.

## Verificación
Todo con prueba en rojo primero (salvo una prueba de la ruta de la bitácora, escrita después).
Web 1.886 de 1.886, motor 28 de 28, tsc y eslint limpios, extracción idéntica sin avisos (el español
visible no cambió) y Gate 0 OK con el ciclo completo.
