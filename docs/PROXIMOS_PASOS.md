# Próximos pasos tras la auditoría final

**Para quién:** el fundador y la sesión que retome el trabajo con una suscripción normal, después de que se cancele Max
(jueves 8 oct 2026). Una suscripción normal no aguanta oleadas de veinte lectores. Por eso aquí solo queda trabajo que
se hace con pocas llamadas o con saldo propio.

**Estado de este documento:** borrador del 30 sep 2026. Se cierra antes de que se agote la cuota del jueves 8, con el
resultado de la etapa 1, de la medida 2 y de la etapa 2 (sección 5).

## 1. Qué gasta cada cosa

| Paso | Qué gasta | Cuánto |
|---|---|---|
| Re-embebido con Voyage | saldo de Voyage, no la suscripción | menos de 0,05 USD |
| Corrida final | **saldo de la API de Anthropic**, no la suscripción | unos 8,5 a 11,5 USD (`docs/producto/CORRIDA_FINAL.md`) |
| Copia de las reglas a la forja | una sesión corta de Claude Code, sin agentes de lectura | poco |
| Lo que la auditoría deje abierto | depende: ver sección 5 | |

El orden importa: el índice de vectores y la caché viajan dentro del despliegue. Primero se re-embebe, después se
despliega y al final se corre la corrida.

## 2. Re-embebido con Voyage (una sola pasada)

Decisión del fundador: Voyage corre una sola vez, al final del remedio, con todos los nodos corregidos. Las tandas de
la auditoría final (`docs/saneamiento/tandas/final-*.json` y `procedencia-*.json`) cambiaron el texto de unos 2.444
nodos vivos. Las constancias CASA no cambian el texto y no se re-embeben.

1. Pon `VOYAGE_API_KEY` en el `.env` raíz. Lo retiras al terminar.
2. Prueba en seco. No llama a nadie y dice cuántos nodos haría:

   ```
   python scripts/auditoria_final/reembeber.py docs/saneamiento/tandas/final-*.json docs/saneamiento/tandas/procedencia-*.json
   ```

3. La pasada de verdad: la misma línea con `--yes` al final.
4. `python scripts/sync_assets_web.py`, las dos suites (`PYTHONIOENCODING=utf-8 python engine/run_all_tests.py` y
   `cd web && npx vitest run`), commit y despliegue.

**Si el script dice "NO SE ESCRIBE":** comprueba que el índice queda coherente y, si algo falla, no escribe nada. Esto
es lo que comprueba:
- todo nodo vivo tiene vector;
- no hay ids duplicados;
- todos los vectores tienen la misma dimensión;
- solo cambian los vectores pedidos;
- cada vector nuevo queda más cerca de su vector viejo que de cualquier otro.

Esa última comprobación se pensó para correcciones de voz. Una corrección de fondo puede acercar un nodo a un vecino
casi gemelo. Si falla solo por eso, el script nombra los nodos. Se miran a mano y se decide: o la corrección cambió de
qué trata el nodo (y hay que revisarla), o el nodo y su vecino son gemelos (y va a la mesa de duplicados). No se afloja
la comprobación para que pase.

## 3. Corrida final (saldo de la API)

Está entera en `docs/producto/CORRIDA_FINAL.md`, con su lista de comprobación, sus créditos, su coste y la consulta
que compara la app con el saldo:
- paso A: completar la caché;
- paso B: prueba de coherencia, con 33 recorridos;
- paso C: vuelo completo.

Lo que añade la auditoría:
- Va **después** del re-embebido y de su despliegue.
- La regla dura D1 vale también aquí. Si una respuesta de la IA nombra un libro, un autor, "los estudios" o insinúa
  un origen, es un fallo que se anota con su sesión. `REGLA_SIN_FUENTES` va en toda llamada
  (`web/lib/reglaSinFuentes.ts`).
- El aviso de vigencia ya no lleva año: "Verifica la norma vigente en tu país: estas reglas cambian con el tiempo".

## 4. Copia de las reglas a la forja

La forja (`forja-nodos`) convierte libros en nodos para packs futuros. Tiene que limpiar con la misma vara que el
catálogo, para que un pack nuevo no traiga de vuelta lo que la auditoría quitó.

1. **Las guardas como datos:** copiar `dataset/metadata/guardas_contenido.json` (con su versión) al sitio donde la
   forja lo lee.
2. **Las reglas duras D1, D2 y D3 y la política C32** de `docs/REGLAS_DE_LA_CASA.md` entran al
   `docs/BANCO_DE_REGLAS.md` de la forja como reglas nuevas, con su fecha y su regla madre en My-idea. El banco se
   corrige añadiendo debajo, nunca tapando:
   - D1: ningún origen visible;
   - D2: ninguna copia fiel;
   - D3: ningún nodo vivo se retira;
   - C32: devolver el sentido y el término preciso, nunca un pasaje palabra por palabra.
3. **Las pautas de procedencia** (el prefijo "Sugerencia de My Idea" y las atribuciones genéricas, en once idiomas)
   viven hoy en `web/lib/procedencia.test.ts`. Para que la forja las use, primero pasan a `guardas_contenido.json`
   (prueba en rojo primero, versión nueva) y después se copian.
4. En la forja, su gate rechaza un candidato que las incumpla. Su prueba va en rojo primero.

## 5. Lo que deja abierta la auditoría

Se completa al cierre de la semana. Esto es lo previsto:

- **Etapa 1:** cerrada con su riesgo residual declarado (Wilson 95 %) en `docs/ACTA_SANEAMIENTO_FINAL.md`, sección 9.9.
- **Medida 2** (semilla 20261010): con el criterio de copias fieles (U14), y la ortografía y los calcos exigidos solo
  en los campos que el cliente ve crudos.
- **Etapa 2,** si cupo: retraducción a los diez idiomas de cada etiqueta corregida, con su huella de vigencia.
- **A mejora continua, con su ficha:** la ortografía y los calcos del resumen, las condiciones y el título.
- **Decisión del fundador o de un abogado:** la licencia de IDEO.org (CC BY-NC-ND 3.0) frente a la regla D1 y al uso
  comercial. No se retiró nada.

## 6. Plan del miércoles 7 y el jueves 8 de octubre (decisión del fundador, 1 oct 2026)

La cuota semanal se renueva el martes 6 a las 23:00, y el Max se cancela el jueves 8. Todo lo que lleva muchos agentes
se hace en estos dos días, **en este orden**, con commit después de cada punto.

### a. Páginas legales y de cuenta

Se copia la estructura de The Original I Ching, que está en local en `C:/Users/AlexDesk/Documents/iching-app`.

| Página de My Idea | Referencia en el I Ching | Contenido |
|---|---|---|
| Privacidad | `apps/web/src/app/privacy` y `components/legal/PrivacyArticleContent.tsx` | Publicada desde `docs/legal/PRIVACIDAD.md` y `docs/legal/fr/CONFIDENTIALITE.md` (español y francés), con su fecha de última actualización |
| Términos | `apps/web/src/app/terms` y `components/legal/TermsArticleContent.tsx` | Desde `docs/legal/TERMINOS.md` y `docs/legal/fr/CONDITIONS.md`, con su fecha |
| Cookies | `components/CookieConsentGate.tsx` y `lib/cookie-consent.ts` | Desde `docs/legal/COOKIES.md` y `docs/legal/fr/TEMOINS.md` |
| Instrucciones para eliminar la cuenta | `apps/web/src/app/delete-account` (y `api/account/delete`) | **Página pública que funciona sin la app**: es requisito de Google Play. Explica cómo pedir la eliminación desde la app y sin ella, qué se borra y en qué plazo. El borrado de cuenta ya está en producción (`web-v2.6.9`, migración 044) |
| Preguntas frecuentes | `apps/web/src/app/faqs` y `components/FaqAccordion.tsx` | Incluye la eliminación de cuenta, los créditos y qué es gratis, que la Claridad sin cuenta se borra a los 30 días, y la privacidad |

- Los enlaces de la app apuntan a ellas: el pie de la portada (hoy `href="#"`), el centro de cuenta y la ficha de
  Google Play.
- La revisión profesional queda pendiente, para afinarlas después de publicarlas.
- La guarda `procedencia.test.ts` sigue mandando: ningún libro ni autor en estas páginas.

### b. Auditoría de preguntas

Acta, sección 14.2.

- 3.374 preguntas: 3.288 base y 86 de entrada.
- Lotes de 40 con su nodo saneado y una trampa sin marca de las tres clases (contraria, inventa, lógica que no
  encaja).
- Dos lectores Opus y árbitro.
- Las que fallen se reemplazan por corrección declarada con `scripts/fidelidad/corregir_preguntas.py`, verificadas a
  ciegas.
- Unos 210 a 220 agentes en unas 12 olas.

### c. Los otros 18 ajustes de prompts

`docs/auditoria_final/informes/auditoria_prompts.md`, secciones B y C. Los 6 graves ya están aplicados (1 oct).

### d. El script del juez de fidelidad y los cambios a `coherencia.ts`

- **El extractor del juez:** paso D de `docs/producto/CORRIDA_FINAL.md`, ficha `juez-fidelidad-salida`.
- **Los cambios a la prueba de coherencia** (`docs/auditoria_final/informes/estado_memoria_contexto.md`):
  - ficha e hilo;
  - continuidad desde el núcleo y con todas las respuestas;
  - contexto en cada llamada, con lista blanca;
  - las cuatro condiciones de caché.

### e. Las promesas no graves y las condiciones de los nodos de otro país

- **Promesas:** los 28 hallazgos medios y bajos de `docs/auditoria_final/informes/promesas_publicas.md`.
- **Condiciones:** las condiciones de activación de los nodos-frontera de otro país (ficha
  `condiciones-frontera-otro-pais`).

## 7. Después del jueves 8, con la suscripción normal

1. **Corrida final con la API** (sección 3 y `docs/producto/CORRIDA_FINAL.md`, pasos A a D). Antes, las versiones
   neutrales de A2 se generan y se auditan como el resto de las preguntas.
2. **Re-embebido con Voyage**, una sola pasada (sección 2).
3. **Copia de las reglas a la forja** (sección 4).
4. **Lanzamiento en Google Play.** El botón de la portada pasa de "Próximamente en Google Play" al enlace real, en los
   once idiomas.
