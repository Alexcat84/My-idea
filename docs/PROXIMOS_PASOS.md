# Próximos pasos con la suscripción normal

**Para quién:** el fundador y la sesión que retome el trabajo después del jueves 8 oct 2026, cuando se cancela Max.
Una suscripción normal no aguanta oleadas de veinte agentes. Aquí queda lo que se hace con pocas llamadas, con saldo
propio o con una decisión del fundador.

**Estado:** reescrito entero el 7 oct 2026 con lo hecho en el encargo del 6 oct. El detalle de cada cosa hecha está en
`docs/ACTA_SANEAMIENTO_FINAL.md`, sección 15.

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
- **Preguntas:** ninguna con falla confirmada sin corregir. En 2 de 85 lotes ningún lector cazó su trampa (las dos
  eran contrarias).

## 2. Decisiones que esperan al fundador

1. **Procedencia, el residuo.**
   - (a) ~~medir otra vez con semilla nueva~~: hecho el 7 oct (medida 5, 5 %);
   - (b) ~~leer el catálogo entero solo para procedencia~~: hecho el 6 y 7 oct (acta 15.8, 458 correcciones).
   - ~~medida 6~~: hecha el 7 oct, 1 de 200 (0,5 %, techo 2,8 % al 95 %; acta 15.10).
   - Lo que queda por decidir:
     - (c) aceptar el residuo declarado (entre 3 y 100 nodos de 3.634, lo más probable unos 20);
     - (d) una segunda lectura total, unos 370 lotes, para buscar 0 en la muestra.
   - Mi recomendación es (c). La segunda lectura costaría lo mismo que la primera para un residuo diez veces menor, y
     las formas que quedan ya son muy blandas.
2. **Los ajustes de prompts que añaden texto.** Están en `docs/auditoria_final/informes/auditoria_prompts.md`, sección
   F: B2 (resto), B4, B5, B7, B8, B9, B10, C1, C2, C3, C5 (resto), C6 y C7. C7 toca la regla D5 y su guarda.
3. **Páginas legales:**
   - la dirección postal del comerciante;
   - la revisión profesional de Privacidad, Términos y Cookies, en español y francés. Cuando el profesional cambie un
     texto se edita el `.md` en `docs/legal/` y se corre `python scripts/sync_legal_web.py`.
4. **`FUNDADOR_EMAILS`:** ponerla en Vercel y en el `.env` con el correo de la cuenta del fundador. Sin ella nadie ve
   los mundos ocultos, tampoco el fundador.
5. **Copy pendiente de visto:**
   - el nombre "Riesgos Bajo Control", que da a entender control;
   - "Tus cifras reales" en la compuerta de Tus Números;
   - las promesas viejas en los mockups de `docs/diseno-canon/`, que son errata para Design.
6. **La licencia de IDEO.org** (CC BY-NC-ND 3.0) frente a la regla D1 y al uso comercial. Decide el fundador o un
   abogado. No se retiró nada.

## 3. Qué gasta cada cosa, y en qué orden

| Paso | Qué gasta | Cuánto |
|---|---|---|
| Re-embebido con Voyage | saldo de Voyage | menos de 0,05 USD |
| Corrida final | saldo de la API de Anthropic | unos 9 a 12 USD (`docs/producto/CORRIDA_FINAL.md`), más las neutrales |
| Juez de fidelidad, auditoría de neutrales | agentes de Claude Code | pocas decenas de agentes |
| Reglas a la forja | una sesión corta | poco |

**El orden importa:** el índice de vectores y la caché viajan dentro del despliegue.
1. Re-embebido.
2. Despliegue.
3. Corrida final.
4. Juez de fidelidad sobre lo que la corrida generó.

## 4. Re-embebido con Voyage (una sola pasada)

Decisión del fundador: Voyage corre una sola vez, al final, con todos los nodos corregidos. Las tandas de la auditoría
cambiaron el texto de **2.808 nodos vivos**, según la prueba en seco del 7 oct (tras la lectura total).

1. Pon `VOYAGE_API_KEY` en el `.env` raíz. La quitas al terminar.
2. Prueba en seco, que no llama a nadie:

   ```
   python scripts/auditoria_final/reembeber.py docs/saneamiento/tandas/final-*.json docs/saneamiento/tandas/procedencia-*.json docs/saneamiento/tandas/medida*.json docs/saneamiento/tandas/barrido*.json docs/saneamiento/tandas/condiciones-*.json docs/saneamiento/tandas/lectura-total-*.json
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
3. **Paso C, vuelo completo:** `pnpm vuelo`.
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

## 6. Reglas a la forja

La forja (`forja-nodos`) convierte libros en nodos para packs futuros. Tiene que limpiar con la misma vara que el
catálogo.

1. **Las guardas como datos:** copiar `dataset/metadata/guardas_contenido.json`, con su versión, a donde la forja lo
   lee.
2. **Las reglas duras D1, D2, D3 y la política C32** de `docs/REGLAS_DE_LA_CASA.md` van al `docs/BANCO_DE_REGLAS.md`
   de la forja, con su fecha y su regla madre. Se añade debajo, nunca se tapa.
3. **Las pautas de procedencia, para que la forja las use:**
   - las de `web/lib/procedencia.test.ts`, en once idiomas;
   - las formas de nombre propio de `engine/test_procedencia_nombres.py` (autoría, "basado en el modelo de", "según X",
     "el filósofo X", citas y referencias).
   - Primero pasan a `guardas_contenido.json` (prueba en rojo primero, versión nueva) y después se copian.
4. **En la forja,** el gate rechaza un candidato que las incumpla. Su prueba va en rojo primero.

## 7. Resto de la etapa 2

- **Retraducción a los diez idiomas** de cada etiqueta corregida, con su huella de vigencia. La guarda de vigencia de
  etiquetas avisa cuál quedó atrasada.
- **Condiciones de los nodos de clase B y A.** Las de los nodos-frontera de otro país (clase C) se leyeron y
  corrigieron el 7 oct (acta 15.5). Las de clase B y A quedan, y se leen con la misma máquina cambiando la clase.
- **A mejora continua, con su ficha:** la ortografía y los calcos del resumen, las condiciones y el título.

## 8. Más adelante

- **Copia fiel.** La copia literal del libro no es prioridad, porque al cliente no le llega tal cual. **Solo llega tal
  cual en el plan sin IA**, que pinta los pasos del nodo sin reescribirlos. Por eso, cuando se retome, se empieza por
  los pasos de los nodos que más salen en ese plan.
- **Valoración con pulgares:** que la persona marque si un paso, una pregunta o un plan le sirvió. Son datos para la
  mejora continua, nunca un juicio público.
- **Mundos sugeridos:** proponer a la persona el mundo que más encaja con lo que contó, sin venderlo como necesario
  (BANCO: el texto no promete lo que falta).
- **Revisión profesional legal:** ver la decisión 3 de la sección 2.
- **Documentos desfasados:** corregidos el 7 oct 2026. `docs/MIGRACION_DE_BASE.md` lista ya las 49 migraciones, y
  `docs/producto/CONTEXTO_ENTREVISTA.md` dice que la 049 está aplicada.
- **Lanzamiento en Google Play:**
  - El botón de la portada pasa de "Próximamente en Google Play" al enlace real, en los once idiomas.
  - La página `/eliminar-cuenta` ya cumple el requisito de Google Play de eliminar la cuenta sin la app.
  - Antes, la revisión profesional de las páginas legales.
