# Promesas públicas: lo que dice más de lo que es verdad (1 oct 2026)

Añadido del fundador del 1 oct 2026, punto 4. Es una revisión única, en solo lectura, de la portada y de todo texto de
venta en español. **Nada se cambia sin el visto.**

**Qué se revisó:**
- `web/app/page.tsx`, `layout.tsx` y `ui/Landing.tsx`;
- los mensajes en español de portada, sitio, créditos, recargas, mundos, potenciar, claridad, nueva idea, calendario,
  Manos a la Obra, documento del plan, Tus Números, corregir cifras, detalle de actividad y vista de la idea;
- `packs_catalog.json`, `precios.ts`, `BANCO_DE_TEXTOS.md` y `docs/legal/`.

**31 hallazgos: 3 altos, 15 medios y 13 bajos.**

## Severidad alta

| # | Dónde | Texto | Lo que es verdad | Propuesta |
|---|---|---|---|---|
| A1 | `portada.ts:85-87`, Landing.tsx:371-378 y el enlace "App" del menú (:141) | "Llévala en el bolsillo" · "Descargar en Google Play" | No hay app Android publicada (`docs/APK_READINESS.md` la trata como futura). El botón no lleva a ningún sitio | "Pronto en Android. Mientras tanto, úsala desde el navegador de tu teléfono." Botón "Abrir en el navegador", o quitar la sección |
| A2 | `portada.ts:94-95`, Landing.tsx:431-432 (`href="#"`) | "Privacidad" · "Términos" | Los textos legales son borradores sin publicar, y la app ya guarda datos y los envía a la IA. Riesgo legal: aparenta una política que no existe | Publicar las páginas tras la revisión profesional. Hasta entonces, "Privacidad: escríbenos a privacy@myideaproject.com" |
| A3 | `claridad.ts:13` (en /nueva y en la vista de la idea) | "Tu Claridad es gratis y queda guardada para siempre." | Las ideas de un invitado sin cuenta se borran a los 30 días sin actividad (`cron/limpiar-invitados`) | "Tu Claridad es gratis. Si creas tu cuenta, queda guardada; sin cuenta se borra a los 30 días sin actividad." |

## Severidad media

| # | Dónde | Texto | Lo que es verdad | Propuesta |
|---|---|---|---|---|
| M1 | `portada.ts:20` | "Comenzar gratis" | Solo la Claridad es gratis. La entrevista pide cuenta (beta privada, por invitación) y 10 créditos, y la compra no está abierta | "Ordena tu idea gratis", con la línea "La Claridad es gratis. Tu plan usa créditos. Hoy estamos en beta privada." |
| M2 | `portada.ts:38` | "pregunta como un buen mentor y estructura como un buen consultor" | BANCO prohíbe "Reemplaza a un consultor" (:178) | "…te hace preguntas con método y ordena lo que respondes en un plan…" |
| M3 | `portada.ts:38, 53`; `nuevaIdea.ts:22` | "no repite plantillas" · "Nada de plantillas" | Las preguntas salen de un banco fijo que se adapta; si falla, sale una plantilla neutral | "Una entrevista que se adapta a tu idea: cada pregunta se ajusta a lo que ya contaste…" |
| M4 | `portada.ts:40, 65` | "recalcula … los pasos exactos hasta el cierre" | Rehacer el plan es un ciclo de 5 créditos, y las fechas son rangos | "Marca lo que hiciste y ve tu avance. Cuando la realidad cambie, pide un nuevo ciclo (5 créditos)…" |
| M5 | `portada.ts:40` | "regresa cuando quieras" | Sin cuenta, la idea se borra a los 30 días | "…con tu cuenta, tu proyecto te espera tal como lo dejaste." |
| M6 | `portada.ts:81` | "hasta verla funcionando en el mundo real" | La app da método, no garantiza el resultado | "…hasta llevarla a la práctica. En cada una sabes dónde estás y cuál es el siguiente paso." |
| M7 | `creditos.ts:34` | "el plan y todo para llevarlo a cabo" | Los ciclos y los mundos se pagan aparte | "Tu plan completo y todo para ejecutarlo… Los ciclos para rehacerlo después se piden aparte." |
| M8 | `packsRecarga.ts:12` | "el viaje entero de una idea" | 30 créditos son el plan, 2 seguimientos y un mundo con su seguimiento | "tu plan, dos ciclos de seguimiento y un mundo con su seguimiento" |
| M9 | `packs_catalog.json:22`, `mundos.ts:13` | "Blinda tus datos…" | Es un diagnóstico y un plan, no protege por sí mismo | "Un plan para proteger tus datos, tus cuentas y la confianza de tus clientes." |
| M10 | `packs_catalog.json:12`, `mundos.ts:11` | "Protege a tu gente … de su peor día." | Un plan, sin garantía de seguridad. Riesgo de responsabilidad | "Prepara a tu gente y a tu negocio para los riesgos de seguridad de tu día a día." |
| M11 | `packs_catalog.json:17`, `mundos.ts:12` | "ventaja que se nota y se cobra" | Promete un resultado económico | "Haz de lo sostenible una ventaja que tus clientes puedan ver." |
| M12 | `packs_catalog.json:32`, `mundos.ts:15` | "en muchos que funcionan igual" | No garantiza que las réplicas funcionen | "Prepara tu negocio probado para replicarlo con el mismo estándar." |
| M13 | `packs_catalog.json:47`, `mundos.ts:18` | "Que llegue entero, a tiempo y sin sorpresas de costo." | Se lee como garantía de entrega | "Planea tus entregas para que lleguen enteras, a tiempo y con costos previstos." |
| M14 | `calendario.ts:80` | "Tu calendario te avisa de cada tarea el mismo día." | Depende del programa: varios ignoran las alarmas de un calendario suscrito | "Cada tarea lleva un aviso para el mismo día; según tu calendario, puede que tengas que activar sus notificaciones." |
| M15 | `planDocumento.ts:26` | "Vuelve a la entrevista cuando quieras: el plan se recalcula" | Es un ciclo de 5 créditos | "¿Cambia algo en el mundo real? Pide un nuevo ciclo (5 créditos) y tu plan se rehace desde donde estés." |

## Severidad baja

| # | Dónde | Texto | Propuesta |
|---|---|---|---|
| B1 | `portada.ts:8` (metadatos) | "Cuéntala, recibe tu plan y ejecútalo." | "Cuéntala, ordénala gratis y, cuando quieras, conviértela en un plan para ejecutarla." |
| B2 | `portada.ts:59` | "Un plan detallado…" | "…(10 créditos, que solo se cobran si lo recibes)." |
| B3 | `portada.ts:62` | "siguiente paso exacto" | "tu siguiente paso" |
| B4 | `portada.ts:47, 88`; `nuevaIdea.ts:19` | "díctala" | "…si tu navegador lo permite" |
| B5 | `portada.ts:40` | "módulos especializados" | "puedes sumar mundos especializados (el diagnóstico es gratis)" |
| B6 | `creditos.ts:44` | "en archivo y PDF" | "en .md o para guardar como PDF desde tu navegador" |
| B7 | `packsRecarga.ts:9` | "un mundo suelto" | "un ciclo de seguimiento o el plan de un mundo" |
| B8 | `packs_catalog.json:7` | "Que tu cliente confíe, vuelva y te recomiende." | "Trabaja la calidad para que tu cliente confíe, vuelva y te recomiende." |
| B9 | `packs_catalog.json:37` | "Ve venir lo que puede fallar…" (el nombre implica control) | "Anticipa lo que puede fallar y decide antes de que decida por ti." |
| B10 | `packs_catalog.json:42` | "al precio que toca" | "Elige con método qué comprar, a quién y a qué precio." |
| B11 | `potenciaTuIdea.ts:10` | "Tus cifras reales…" | "Las cifras que nos das, convertidas en margen, punto de equilibrio y escenarios." |
| B12 | `manosALaObra.ts:114`; `bitacora.ts:61` | "Con fechas y recordatorios" | "Con fechas (y avisos en tu calendario, si lo sincronizas)" |
| B13 | `corregirCifras.ts:30`, `tusNumeros.ts:73, 121`, `detalleActividad.ts:51` | "gratis" en funciones de un plan pagado | "incluido". BANCO reserva "gratis" para la Claridad y los diagnósticos |

## Lo que sí es verdad (sin hallazgo)

- No hay libros, autores, "expertos", "estudios", "personalizado", cifras de mercado ni conteos de nodos en los textos
  públicos.
- Se ven 9 mundos, porque Primer Equipo sigue oculto, y ningún texto cuenta mundos. Una nota de código:
  `?ver=ocultos` no comprueba quién eres, y el comentario de `catalogoMundos.ts:46-47` está desactualizado.
- Los 11 idiomas están activos.
- Lo gratis es verdad: la Claridad, el diagnóstico de mundo y Tus Números incluido.
- Los precios mostrados salen de `precios.ts`. "Si algo falla a mitad, no se cobra nada" coincide con la reserva y su
  liberación.
