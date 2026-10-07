# Próximos pasos con la suscripción normal

**Para quién:** el fundador y la sesión que retome el trabajo después del jueves 8 oct 2026, cuando se cancela Max.
Una suscripción normal no aguanta oleadas de veinte agentes. Aquí queda lo que se hace con pocas llamadas, con saldo
propio o con una decisión del fundador.

**Estado:** reescrito entero el 7 oct 2026 con lo hecho en el encargo del 6 oct, y puesto al día la noche del 7 oct con
las decisiones del fundador de ese día: la copia fiel (regla D2, sección 8) y el i18n al día (sección 2, decisión 8). El detalle de cada cosa hecha está en `docs/ACTA_SANEAMIENTO_FINAL.md`, sección 15.

**Lo que sigue, en este orden, con suscripción normal** (cada punto tiene su sección abajo):
1. **Revisión legal profesional y dirección postal** (sección 2, decisión 3): sin ellas no se lanza en Google Play.
2. **Re-embebido con Voyage** (sección 4): una sola pasada, al final, con la copia fiel incluida, menos de 0,05 USD.
   Se pide la clave al fundador en ese momento.
3. **Despliegue**, con el índice nuevo.
4. **Corrida final con la API** (sección 5): unos 9 a 12 USD más las neutrales.
5. **Lanzamiento en Google Play** (sección 8).
El saneamiento continuo (sección 7) quedó completo la noche del 7 oct: las dos corrientes leídas enteras y su pasada
de cierre hecha.

## 1. Dónde quedó todo

**Hecho en el encargo del 6 oct** (acta 15):
- **Calculadora y estimador protegidos** como métodos validados (REGLAS M1). Para resellarlos hace falta el visto del
  fundador en el mensaje del commit.
- **Procedencia:**
  - los 5 elementos que quedaban, como consejo con su matiz;
  - barrido 1, de atribuciones blandas: 90 correcciones;
  - medida 4, con semilla 20261006 fijada antes;
  - barrido 2, de nombres propios: 76 correcciones;
  - guarda nueva `engine/test_procedencia_nombres.py`.
  - Todo verificado a ciegas.
- **Auditoría de las 3.374 preguntas contra su nodo:** 171 corregidas (146 de lógica, 15 contrarias y 10 que
  inventaban), todas verificadas a ciegas.
- **Páginas públicas:** `/privacidad`, `/terminos` y `/cookies` en español y francés; `/eliminar-cuenta` sin app ni
  sesión; `/preguntas-frecuentes`. El botón dice "Próximamente en Google Play".
- **Salida de la IA:**
  - 7a: los ajustes de prompts que solo quitan (los demás, abajo, para el visto).
  - 7b: el extractor del juez de fidelidad, las condiciones nuevas de `coherencia.ts`, el contexto en `prioridad.ts`
    y la guarda de contexto en toda llamada.
  - 7c: `?ver=ocultos` comprueba quién eres (`FUNDADOR_EMAILS`).
- **Punto 8:**
  - las 28 promesas no graves, corregidas en 11 idiomas;
  - las condiciones de los 104 nodos-frontera de otro país, leídas contra el libro: 55 correcciones verificadas a
    ciegas.

**Hecho el 7 oct por la tarde** (decisiones del fundador de ese día):
- **Prompts de la sección F:** aprobados y aplicados con su guarda (main bfc9eb73).
- **Consentimiento legal versionado:** navegar es libre; la aceptación se pide junto al botón al generar la evaluación
  gratuita ("Aceptar y generar") y la exige el servidor (428) antes de tocar la IA o el buscador; queda también en la
  identidad invisible y la adopción la traslada a la cuenta al confirmar el correo; aviso de cookies que no tapa nada;
  /login enlaza a Términos y Privacidad. Migración 050 aplicada. Regla P24.
- **Reglas a la forja:** `guardas_contenido.json` 1.1.0 con las pautas de procedencia desde una sola fuente; la aduana de
  `forja-nodos` usa esa copia versionada y su BANCO hereda las 57 reglas de contenido y método (forja-nodos 1a70e45d).
- **Condiciones de las clases B y A** de `jurisdiccion.json`: leídas contra el libro, 22 correcciones (acta 15.12).
- **Saneamiento continuo** completo (acta 15.13 y 15.14; sección 7).

**El veredicto del dataset, sin adornos:**
- **Contrarios e invenciones duras:** 0 en la muestra de la medida 3, con un residuo por nodo de 0 a 1,9 % al 95 %
  (acta 14).
- **Procedencia: la medida 4 NO dio 0.** Hubo 18 de 200 nodos, un 9 %, de 5,8 a 13,8 % al 95 %. Se corrigieron los 20
  de la muestra y 76 del catálogo con el barrido 2. Queda la atribución que no lleva nombre propio ni verbo de autoría,
  que ninguna búsqueda mecánica ve. Ver la decisión 1 de la sección 2.
  - **Medida 5** (7 oct, semilla 20261008, después del barrido 2): 10 de 200 nodos, un 5 % (de 2,7 a 9,0 %). Es la
    mitad, pero no 0. Lo que queda son formas sin nombre ni verbo de autoría: "los mejores X", "hay quien", un autor
    nombrado de pasada, una cita sin fuente. Se corrigieron las 10 (acta 15.7).
  - **Lectura total** (6 y 7 oct): los 3.634 nodos vivos, 368 lotes con su trampa (368 de 368 cazadas). Se aplicaron
    458 correcciones en 393 nodos, cada una con árbitro y verificación ciega contra el libro (acta 15.8). No es una
    medida: falta la medida 6 para saber cuánto queda.
  - **Medida 6** (7 oct, semilla 20261023, después de la lectura total): 1 de 200 nodos, un 0,5 % (de 0,09 a 2,8 %).
    Baja de forma concluyente desde el 5 %, pero no es 0. El hallazgo ("ejemplos documentados") quedó corregido (acta
    15.10).
  - **El fundador acepta el residuo declarado** (7 oct, acta 15.11): de 0,09 a 2,8 % por nodo, entre 3 y 100 nodos,
    lo más probable unos 20. No hay segunda lectura total.
- **Preguntas:** ninguna con falla confirmada sin corregir. En 2 de 85 lotes ningún lector cazó su trampa (las dos
  eran contrarias).

## 2. Decisiones que esperan al fundador

1. ~~**Procedencia, el residuo.**~~ **Decidida el 7 oct (acta 15.11): se acepta el residuo declarado** de la
   medida 6 (de 0,09 a 2,8 % por nodo). No hay segunda lectura total.
2. ~~**Los ajustes de prompts que añaden texto.**~~ **Decididos el 7 oct:** aprobados B2, B4, B5, B7, B8, B9, B10,
   C1, C2, C3, C5 y C7 con el ajuste propuesto, y C6 solo en parte (el ejemplo de $850/$170 se marca como cifras
   ficticias; la ayuda de cómo conseguir los datos se queda). Aplicados, con su guarda: `docs/auditoria_final/informes/
   auditoria_prompts.md`, sección F.
3. **Páginas legales:**
   - la dirección postal del comerciante;
   - la revisión profesional de Privacidad, Términos y Cookies, en español y francés. Cuando el profesional cambie un
     texto se edita el `.md` en `docs/legal/` y se corre `python scripts/sync_legal_web.py`.
   - **Las traducciones a los otros nueve idiomas** (en, pt, de, it, ja, zh, ko, ar, hi, desde el 7 oct) guardan la
     huella del español del que salieron (`docs/legal/<idioma>/huellas.json`). Si el profesional cambia el español,
     `engine/test_legal_huellas.py` falla hasta retraducirlas: se retraduce el documento cambiado, se pasa la revisión
     de naturalidad del segundo modelo y se corre `python scripts/legal_huellas.py <idioma>` y `sync_legal_web.py`.
   - Para el profesional, anotado: el registro de la aceptación se guarda sin IP ni navegador (lo mínimo); se borra con
     la cuenta; los Términos dicen "al usar la app aceptas" también para el invitado; la cookie `myidea_idioma`
     (preferencia de idioma, un año) no es estrictamente necesaria; la versión vigente de los textos se llama
     `2026-10-07.2`.
4. **`FUNDADOR_EMAILS`:** sirve para que solo la cuenta del fundador vea y camine los mundos sin publicar con
   `?ver=ocultos`. Valor: el correo con el que el fundador inicia sesión en My Idea (varios, separados por comas). Dónde:
   Vercel, Settings, Environment Variables, entorno Production, y volver a desplegar. Sin ella nadie los ve, tampoco el
   fundador.
5. **Copy pendiente de visto:**
   - el nombre "Riesgos Bajo Control", que da a entender control;
   - "Tus cifras reales" en la compuerta de Tus Números;
   - las promesas viejas en los mockups de `docs/diseno-canon/`, que son errata para Design.
6. ~~**La licencia de IDEO.org**~~ **Decidida el 7 oct (acta 15.11): los nodos se quedan.** Anotada en
   `fuentes_canonicas.json` y en `docs/internos/INVENTARIO_FUENTES.md`.
7. **Tres choques de la forja que el fundador debería ver** (declarados en D.63 de su BANCO y resueltos hoy por su D.13,
   gana la regla más reciente): el "puente" de su D.30 frente a la regla de la casa de que un consejo práctico no es
   defecto; los pasos que dicen "la frase del libro" o "el texto dice", que desde hoy caen en su aduana; y que los nodos
   de la forja van sin tildes. Además, su aduana exige el glosario sin condiciones ("marketing" no entra), más estricta
   que el catálogo de hoy.

8. **I18N al día (7 oct, main df709c18e):** legales, preguntas frecuentes y eliminar cuenta en los once idiomas, y
   94 evidentes de naturalidad aplicados en diez idiomas. **Lo discutible está en `docs/i18n/DISCUTIBLES_I18N_AL_DIA.md`**
   (140 de interfaz, 43 de ayuda, 52 legales) con siete decisiones transversales: el término árabe de créditos (رصيد
   del glosario o نقاط de la interfaz); el registro formal en los legales de alemán, coreano y japonés; Privacidad §2
   dice "español o francés" pero la base solo guarda es/fr (migración 050); falta la nota de prevalencia en el francés;
   Términos §11 dice que la referencia es el francés; la frase repetida de Privacidad §10 en español; y la frase de
   entrada de la nota de prevalencia. Las que tocan el español o el francés esperan a la revisión profesional (cambiar
   el texto sube la versión y pide aceptar de nuevo).

## 3. Qué gasta cada cosa, y en qué orden

| Paso | Qué gasta | Cuánto |
|---|---|---|
| Re-embebido con Voyage | saldo de Voyage | menos de 0,05 USD |
| Corrida final | saldo de la API de Anthropic | unos 9 a 12 USD (`docs/producto/CORRIDA_FINAL.md`), más las neutrales |
| Juez de fidelidad, auditoría de neutrales | agentes de Claude Code | pocas decenas de agentes |

**El orden importa:** el índice de vectores y la caché viajan dentro del despliegue.
1. Re-embebido.
2. Despliegue.
3. Corrida final.
4. Juez de fidelidad sobre lo que la corrida generó.

## 4. Re-embebido con Voyage (una sola pasada)

Decisión del fundador: Voyage corre una sola vez, al final, con todos los nodos corregidos. Las tandas de la auditoría
cambiaron el texto de **3.187 nodos vivos**, según la prueba en seco del cierre del saneamiento continuo (noche del
7 oct). Si entra otra tanda, la prueba en seco del día da el número de verdad.

1. Pon `VOYAGE_API_KEY` en el `.env` raíz. La quitas al terminar.
2. Prueba en seco, que no llama a nadie:

   ```
   python scripts/auditoria_final/reembeber.py docs/saneamiento/tandas/final-*.json docs/saneamiento/tandas/procedencia-*.json docs/saneamiento/tandas/medida*.json docs/saneamiento/tandas/barrido*.json docs/saneamiento/tandas/condiciones-*.json docs/saneamiento/tandas/lectura-total-*.json docs/saneamiento/tandas/voz-*.json docs/saneamiento/tandas/copia-*.json
   ```

   Si después de esta fecha entra otra tanda que cambie texto de nodos, se añade a la línea.
3. La pasada de verdad: la misma línea con `--yes` al final.
4. Corre `python scripts/sync_assets_web.py` y las dos suites (`PYTHONIOENCODING=utf-8 python engine/run_all_tests.py`
   y `cd web && npx vitest run`). Después, commit y despliegue.

**Si el script dice "NO SE ESCRIBE":** comprueba la coherencia del índice y no escribe nada si algo falla.
- Comprueba:
  - todo nodo vivo tiene vector;
  - no hay ids duplicados;
  - todos los vectores tienen la misma dimensión;
  - solo cambian los vectores pedidos;
  - cada vector nuevo queda más cerca de su vector viejo que de cualquier otro.
- Si falla solo la última comprobación, el script nombra los nodos y se miran a mano. Puede pasar una de dos cosas:
  - la corrección cambió de qué trata el nodo, y se revisa;
  - el nodo y su vecino son gemelos, y van a la mesa de duplicados.
- No se afloja la comprobación.

## 5. Corrida final (saldo de la API)

Está entera en `docs/producto/CORRIDA_FINAL.md`, con su lista de comprobación, sus créditos, su coste y la consulta
que compara la app con el saldo.

1. **Paso A, completar la caché, Y AUDITAR LAS NEUTRALES.** Las versiones neutrales de las preguntas se generan con
   la API en este paso. Antes de usarse se leen igual que las 3.374 bases: contra su nodo, con dos lectores, trampas
   sin marca, árbitro y reemplazo verificado a ciegas. La máquina está en `auditoria-final-claves/preguntas/`
   (auditoria.py, hacer_vq.py y hacer_tanda.py) y el aplicador es `scripts/fidelidad/corregir_preguntas.py`, que ya
   acepta el campo `pregunta_neutral`. Con suscripción normal, por tandas pequeñas.
2. **Paso B, prueba de coherencia** (`cd web && npx tsx scripts/coherencia.ts`; sin `--confirmo-gasto` no gasta).
   - Son 33 recorridos.
   - Desde el 7 oct la condición de salida exige el dictamen, la continuidad desde el núcleo con todas las respuestas,
     la ficha, el hilo, el contexto en cada llamada (con la lista blanca de los organizadores) y las cuatro
     condiciones de caché.
   - Riesgo a mirar en el informe: si el primer envío de un turno falla después de que el servidor ya guardó la
     respuesta, el reintento la guarda dos veces en el hilo, y la condición del hilo falla. Si pasa, se mira esa
     sesión antes de dar la prueba por caída.
3. **Paso C, vuelo completo:** `pnpm vuelo`. Desde el 7 oct los arneses aceptan los textos legales antes de generar
   (`aceptarTextosLegales` en `web/scripts/_shared/http.ts`); sin eso el servidor responde 428.
4. **Paso D, juez de fidelidad de la salida.**
   - El extractor ya existe (`web/scripts/juezFidelidad.ts`, con sus funciones en `web/lib/coherencia/juezFidelidad.ts`).
     Arma un paquete por salida y planta 1 trampa sin marca por cada 5.
   - Los jueces y el árbitro son agentes de Claude Code, con las instrucciones de `docs/producto/JUEZ_FIDELIDAD.md`.
   - Uso, desde `web/`: `npx tsx scripts/juezFidelidad.ts --desde <hora 4 de la lista, ISO UTC> --paquetes <carpeta fuera
     del repo> --claves <otra carpeta fuera del repo>`. Sin `--escribir` solo dice lo que haría. Las trampas son
     `ceil(n/5)`, con semilla 20261007, y sus claves van solo a la carpeta de claves.
   - Umbral fijado antes: 0 contrarios, 0 invenciones y 0 procedencias.
5. **Medición de saldo:** la consulta de `costo_usd` de `CORRIDA_FINAL.md` contra el saldo real de la consola de
   Anthropic, antes y después.

La regla D1 vale también aquí: si una respuesta de la IA nombra un libro, un autor o "los estudios", o insinúa un
origen, es un fallo que se anota con su sesión.

## 6. ~~Reglas a la forja~~ (hecho el 7 oct)

La forja (`forja-nodos`) hereda las reglas de contenido y de método de `docs/REGLAS_DE_LA_CASA.md` (D.63 de su BANCO) y
su aduana usa la copia versionada de `guardas_contenido.json` 1.1.0 (`config/`, con su prueba de versión y huella), que
rechaza al candidato que incumple voz, glosario o procedencia (D.62). Main 45412e3e y forja-nodos 1a70e45d.
- **Cuando cambie una guarda:** se sube `VERSION_GUARDAS` en `web/lib/guardasContenido.ts`, se regenera el JSON
  (`cd web && npx tsx scripts/exportar_guardas.ts`) y en la forja se corre `python scripts/copiar_guardas.py`, que
  imprime la versión y la huella nuevas para su `src/guardas_contenido.py`.

## 7. Resto de la etapa 2

- **Retraducción a los diez idiomas** de cada etiqueta corregida, con su huella de vigencia. La guarda de vigencia de
  etiquetas avisa cuál quedó atrasada.
- ~~**Condiciones de los nodos de clase B y A.**~~ Leídas y corregidas el 7 oct (acta 15.12): 22 correcciones en 22
  nodos. Con las de clase C (acta 15.5), las condiciones de los 239 nodos de `jurisdiccion.json` quedan leídas.
- **A mejora continua, con su ficha:** la ortografía y los calcos del resumen y el título.
- **Saneamiento continuo (acta 15.13 y 15.14), completo la noche del 7 oct.** Dos corrientes:
  - condiciones del resto de nodos contra el libro: `auditoria-final-claves/condiciones_resto/condiciones_resto.py`,
    243 lotes;
  - la voz de lo que el cliente ve crudo (etiqueta, ortografía y calcos en etiqueta, pasos y entregable):
    `auditoria-final-claves/voz/voz.py`, 146 lotes.
  - Cada ola: lectores (uno por lote, con trampa; segundo lector si no la caza), `estado`, `arbitraje <ola>`, árbitros,
    (`confirmados <ola>` en condiciones), `verificacion <ola>`, verificadores, `tanda <ola>`, aplicar, el ciclo entero
    (Gate 0, etiquetas, familias, sincronizar), retraducir las etiquetas que cambien
    (`npx tsx scripts/i18n/etiquetasRiel.ts exportar|aplicar`) y las dos suites antes del commit.
  - Resultado: voz, 3.524 correcciones en 1.798 nodos; condiciones, 196 en 189 nodos. Lo que la verificación no
    sostuvo se reescribió y volvió a verificarse (voz-v21, condiciones-resto-c27); queda una sola etiqueta como estaba
    (acta 15.14, cierre).
  - Si hace falta otra pasada: `releer <lote>` rearma un lote con trampa nueva, `reescritura <ola>` manda lo retenido
    a un reescritor, y `estado` dice por dónde va cada corriente.

## 8. Más adelante

- **Copia fiel (regla D2), en curso desde el 7 oct (acta 15.15).** Decisión del fundador: se corrige ya, primero los
  PASOS de los 3.634 nodos vivos y después los RESÚMENES y las CONDICIONES; se cambia la forma, nunca el contenido.
  Máquina: `auditoria-final-claves/copia/copia.py` (`estado`, `verificacion <ola>`, `tanda <ola>`, `reescritura <ola>`;
  instrucciones en `auditoria-final/copia/`). Resúmenes y condiciones van en lotes con los mismos nodos (R### y C###),
  un lector para los dos. Regla de parada fijada: muestra de 200 nodos con semilla 20261028 (copia, y como control
  contrarios e invenciones); se cierra si la copia da como mucho 1 cada 20 nodos y contrarios e invenciones 0. Lo que
  falte al agotarse la cuota queda dicho en el acta 15.15.
- **Valoración con pulgares:** que la persona marque si un paso, una pregunta o un plan le sirvió. Son datos para la
  mejora continua, nunca un juicio público.
- **Mundos sugeridos:** proponer a la persona el mundo que más encaja con lo que contó, sin venderlo como necesario
  (BANCO: el texto no promete lo que falta).
- **Revisión profesional legal:** ver la decisión 3 de la sección 2.
- **Documentos desfasados:** corregidos el 7 oct 2026. `docs/MIGRACION_DE_BASE.md` lista ya las 49 migraciones, y
  `docs/producto/CONTEXTO_ENTREVISTA.md` dice que la 049 está aplicada.
- **Lanzamiento en Google Play** (después de la corrida final):
  - Antes: la revisión profesional de las páginas legales y la dirección postal del comerciante (sección 2,
    decisión 3).
  - La página `/eliminar-cuenta` ya cumple el requisito de Google Play de eliminar la cuenta sin la app, y el
    consentimiento versionado ya registra la aceptación.
  - El botón de la portada pasa de "Próximamente en Google Play" al enlace real, en los once idiomas.
