# Próximos pasos con la suscripción normal

**Para quién:** el fundador y la sesión que retome el trabajo después del jueves 8 oct 2026, cuando se cancela Max.
Una suscripción normal no aguanta oleadas de veinte agentes. Aquí queda lo que se hace con pocas llamadas, con saldo
propio o con una decisión del fundador.

**Estado:** reescrito entero el 7 oct 2026 con lo hecho en el encargo del 6 oct, y puesto al día la noche del 7 oct con
las decisiones del fundador de ese día: la copia fiel (regla D2, sección 8) y el i18n al día (sección 2, decisión 8). El detalle de cada cosa hecha está en `docs/ACTA_SANEAMIENTO_FINAL.md`, sección 15.

**Lo que sigue, en este orden, con suscripción normal** (cada punto tiene su sección abajo):
1. **Revisión legal profesional, evaluación de privacidad y dirección postal** (sección 2, decisión 3): sin ellas no se
   lanza en Google Play. **Tarea del fundador ANTES DEL LANZAMIENTO:** hacer con el profesional la evaluación de
   factores relativos a la privacidad que exige la ley de Quebec para comunicar datos fuera de la provincia.
2. **Terminar la copia fiel** (sección 8; NO quedó certificada): verificar la ola k31, ya leída; leer 12 lotes de
   vecindad; reescribir lo retenido; decidir el residuo de resúmenes; medir otra vez.
   Voyage va al día con main del 8 oct 2026 (segunda pasada, sección 4); los pasos no entran en el vector.
3. **Despliegue**, con el índice de la segunda pasada.
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
   - **ANTES DEL LANZAMIENTO, tarea del fundador con el profesional:** la evaluación de factores relativos a la
     privacidad (EFVP) que exige la ley de Quebec antes de comunicar datos personales fuera de la provincia. Desde el
     8 oct 2026 la sección 7 de la Privacidad describe la práctica (proveedores con protecciones contractuales y de
     seguridad adecuadas) y ya no anuncia trámites pendientes: esa evaluación es la que lo respalda. Quién es cada
     proveedor (las categorías de la sección 6) está en el inventario interno, `docs/legal/INVENTARIO_DATOS.md`,
     sección 3;
   - la revisión profesional de Privacidad, Términos y Cookies, en español y francés. Cuando el profesional cambie un
     texto se edita el `.md` en `docs/legal/` y se corre `python scripts/sync_legal_web.py`.
   - **Las traducciones a los otros nueve idiomas** (en, pt, de, it, ja, zh, ko, ar, hi, desde el 7 oct) guardan la
     huella del español del que salieron (`docs/legal/<idioma>/huellas.json`). Si el profesional cambia el español,
     `engine/test_legal_huellas.py` falla hasta retraducirlas: se retraduce el documento cambiado, se pasa la revisión
     de naturalidad del segundo modelo y se corre `python scripts/legal_huellas.py <idioma>` y `sync_legal_web.py`.
   - Para el profesional, anotado: el registro de la aceptación se guarda sin IP ni navegador (lo mínimo); se borra con
     la cuenta; los Términos dicen "al usar la app aceptas" también para el invitado; la cookie `myidea_idioma`
     (preferencia de idioma, un año) no es estrictamente necesaria; la versión vigente de los textos se llama
     `2026-10-08` (proveedores por categorías, sin el símbolo de sección y la sección 7 sin trámites anunciados).
3-bis. **Prueba del calendario en tu Android, de punta a punta** (tarea del fundador, 8 oct 2026): en una idea en modo
   con fechas, abre el calendario, toca «Suscribir», añade el enlace en el calendario del teléfono (Google Calendar) y
   comprueba que aparecen las fechas pendientes, con el nombre del espacio delante. Después cambia una fecha en la app
   y confirma que el teléfono la recoge en la siguiente actualización: las apps de calendario releen un calendario
   suscrito cada varias horas, no al instante, y la suscripción es de una sola vía (lo que cambies en el teléfono no
   vuelve a la app).
3-ter. **Calibración real del estimador** (decisión del fundador, 8 oct 2026). El estimador de bandas
   (`SYSTEM_ESTIMACION_BANDA`, método validado) pasó a Sonnet 5.5 con el visto del fundador: en la revalidación con los
   24 casos del estudio original que siguen en el grafo, los dos modelos tuvieron constancia del 100 %, y la comparación
   con Sonnet 4.6 no prueba exactitud, porque la referencia del estudio también salió de un modelo (ver
   `docs/corrida_final/2026-10-08/revalidacion_estimador.md`). La exactitud se mide contra la realidad: **cuando la
   beta tenga tareas completadas**, comparar la talla estimada de cada tarea con la duración real que registró el
   ritmo personal (el multiplicador del scheduler), **por talla**, y reportar si el estimador tiende a quedarse corto o
   largo en cada una. Si hay un sesgo claro, el ajuste es un cambio a un método validado: se presenta con su evidencia
   y se resella con `python scripts/metodos_validados.py --visto "<nota>"` y "VISTO DEL FUNDADOR" en el commit.
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

## 4. Re-embebido con Voyage (primera pasada hecha, falta la segunda)

**Primera pasada, 7 oct 2026.** El fundador la ordenó antes de que se acabara la cuota, sin esperar al final de la
copia fiel.
- Re-embebió **2.706 nodos vivos**: los que cambiaron título, resumen o condiciones desde el índice anterior, con la
  copia fiel aplicada hasta la tanda k26.
- La lista no salió de los nombres de las tandas, sino de comparar el texto que se embebe
  (`texto_nodo` de `scripts/build_semantic_index_voyage.py`) con el del grafo en el último commit que tocó el índice.
  La línea de tandas habría dado 3.495 nodos, porque cuenta también los nodos donde solo cambiaron los pasos, y los
  pasos no entran en el vector.
- Coherencia antes y después:
  - 3.634 vectores para 3.634 nodos vivos;
  - lista roja vacía, es decir, ningún vector de un nodo no vivo;
  - sin duplicados, dimensión 512;
  - el script no reportó ningún fallo;
  - `MIN_SCORE_SALTO` sigue en 0,3;
  - el vecino más cercano de cada nodo pasó de 0,796 a 0,800 de media.
- Gate 0 y las dos suites en verde.

**Segunda pasada, 8 oct 2026 (orden del fundador, con el estado de main tras k31 parcial):** re-embebió 191 nodos; coherencia igual que la primera: 3.634 vectores para 3.634 vivos, lista roja vacía, sin duplicados, `MIN_SCORE_SALTO` en 0,3, vecino más cercano medio 0,800 → 0,801; Gate 0, tsc y suites en verde.

**Pasadas siguientes:** cada vez que el cierre del dataset (sección 8) cambie resúmenes o condiciones, con el mismo método.
1. Pon `VOYAGE_API_KEY` en el `.env` raíz, o pásala solo al proceso. La quitas al terminar.
2. Saca la lista de nodos con texto embebible cambiado desde el índice vigente:

   ```
   python - <<'EOF'
   import json, subprocess, sys
   sys.path.insert(0, "scripts"); import build_semantic_index_voyage as bsi
   c = subprocess.run(["git", "log", "-1", "--format=%H", "--", "web/lib/assets/semantic_index.json"], capture_output=True, text=True).stdout.strip()
   viejo = json.loads(subprocess.run(["git", "show", c + ":dataset/metadata/master_graph.json"], capture_output=True).stdout)["nodos"]
   nuevo = json.load(open("dataset/metadata/master_graph.json", encoding="utf-8"))["nodos"]
   ids = [k for k, n in nuevo.items() if not n.get("deprecado") and (k not in viejo or bsi.texto_nodo(viejo[k]) != bsi.texto_nodo(n))]
   json.dump([{"node_id": i} for i in ids], open("voyage_ids.json", "w")); print(len(ids))
   EOF
   ```

3. Prueba en seco: `python scripts/auditoria_final/reembeber.py voyage_ids.json`. La pasada de verdad es la misma
   línea con `--yes`. Borra `voyage_ids.json` al terminar.
4. Corre `python scripts/sync_assets_web.py`, Gate 0 y las dos suites (`PYTHONIOENCODING=utf-8 python
   engine/run_all_tests.py` y `cd web && npx vitest run`). Después, commit y despliegue.

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

### Estado al 9 oct 2026: la corrida final está HECHA y parada en una decisión del fundador

Todo en `docs/corrida_final/2026-10-08/` (README = cada umbral contra su resultado; ACTA filas 1 a 13).
- **Pasó:** caché de preguntas (por la regla de cierre, residuo declarado), coherencia (umbrales del fundador), vuelo
  completo (intento 10 + fases 3 y 4), cierre de Vercel (rigen 5 arranques, 30 sesiones, 1 USD por sesión).
- **NO pasó:** el juez de fidelidad, en los dos tramos (B: 1 invención; C: 11 sostenidos en 7 de 14 planes, 9
  invenciones y 2 contrarios). Arreglos ya aplicados después: «Lo que este plan aún no cubre» (c0ab3a89a), la moneda y los
  datos del negocio como pregunta (bfbd1fddc), el costo total con tiempo de la persona (c6e51feec).
- **Medición barata A/B (54b189303 en main, ya en origin):** el verificador de planes (`VERIFICADOR_PLAN`, apagado, SIN
  desplegar) no pasa: A 14 sostenidos en 7 planes, B 10 en 8 (umbral 0). Defecto del guion declarado (8036eaad0, rama
  `fidelidad-contexto`, sin push): 3 sostenidos vienen del estado vivo de hoy, no del producto; sin ellos A 12 y B 9.
- **Dos cosas abiertas:** (1) la cifra final de la consola de Anthropic (saldo inicial 19,67 USD a las 01:05 UTC del 8 oct)
  para cerrar el paso 5 y el desglose de COSTES_MODELOS.md; (2) el `.env` raíz con la clave se queda hasta la decisión.
- **Nada se arregló a propósito** tras el B NO PASA (regla del fundador: se para y se reporta).

**Decisión que espera al fundador** (el verificador no se despliega mientras no la tome):
1. *Aceptar el residuo y lanzar sin verificador:* los inventos que quedan son de negocio plausible (causas, hechos no
   dados) y 2 a 3 contrarios de cálculo u orden; declarar el residuo en el acta como se hizo con las neutrales.
2. *Repetir la medición sin el defecto del guion* (quitar la suma del estado vivo de hoy): coste aproximado 1,9 USD.
   Ojo: el juez y el árbitro resuelven distinto frases idénticas entre versiones; con umbral 0 un solo caso límite decide,
   así que conviene fijar de antemano un umbral distinto de 0 o una regla de cierre como la de las neutrales.
3. *Endurecer el verificador* para corregir contrarios de cálculo u orden (hoy solo quita o pregunta) y volver a medir.
Recomendación: 2 con regla de cierre fijada antes, porque la medición actual tiene un defecto conocido.

### Estado al 9 oct 2026 (noche): la segunda medición A/B, hecha, y B NO PASA otra vez

El fundador eligió "arreglar el contexto y medir" (ACTA filas 14, 14b y 15; informe `docs/corrida_final/2026-10-08/medicion_ab2/RESULTADO.md`).
Todo en la rama `fidelidad-contexto` del clon `my-idea-main`, **sin push y sin fusionar** (decisión del fundador).
- **Resultado:** A 14 sostenidos en 7 de 14 planes; B 15 en 9 (umbral 0); trampas 3/3 en las dos. Juez, relectura y
  árbitro corrieron por la API (Opus 5.5, `web/scripts/corrida_final_juez_api.ts`, 9,29 USD estimados); redacción 1,8851.
- **Lo buscado desapareció** de los borradores: premisas de preguntas de la IA, «siguen vigentes», la resta al revés, la
  cuota de defectos.
- **Lo que queda:** (1) una frase FIJA del motor, «Lo que este plan aún no cubre: validar con clientes reales (...)»
  (`engine/plan_readiness.py:85`, `web/lib/i18n/mensajes/motor.ts:13`), en 11 de 14 planes y sostenida como contrario
  en 3 (B) y 2 (A): no la escribe la IA y ninguna regla de redacción la quita; (2) causas y resultados prometidos en las
  bisagras del texto («suele cuidar el ritmo», «quita el aire de reproche», «sin que te quite tiempo»), que el
  verificador deja pasar; (3) ruido del juez, unos 3 por versión.
- **Daño nuevo del verificador** (el juez no lo cuenta): vuelve pregunta lo que la persona dijo en la misma sesión
  ("¿Usas resina en tus macetas?"), porque desconfía de lo que no está en la foto del contexto al abrir la sesión.

**Decisión que espera al fundador** (nada se arregló: regla de cierre):
1. *La frase fija de «aún no cubre»:* que salga solo cuando el plan de verdad no cubre la validación con clientes, o
   quitarla. Es determinista, barata y con prueba en rojo; por sí sola baja A y B a 12.
2. *El verificador:* que confíe en las respuestas de la sesión y que busque causas y resultados prometidos; o dejarlo
   apagado, porque en dos mediciones no mejora a A de forma clara y añade un 69 % al coste del plan.
3. *El umbral:* con unos 3 sostenidos de ruido del juez por versión, el 0 exige suerte; fijar antes una regla de
   cierre como la de las neutrales (por ejemplo, 0 contrarios y como mucho N invenciones, con residuo declarado).
Recomendación: 1 y 3, con el verificador apagado; medir otra vez solo después de fijar la regla.

**Decisiones del fundador (9 oct, noche):** frase de «aún no cubre» solo si las etapas de verdad no validan con clientes
(producción y motor, hecho); el verificador queda APAGADO; regla de cierre de dos jueces (ACTA fila 17); última
medición por el camino de producción (ACTA fila 16).

**Verificador de planes, APAGADO (`VERIFICADOR_PLAN` sin definir). Su defecto, por si se retoma:** no trata como dato
lo que la persona dijo en la sesión en curso. Esas respuestas sí le llegan (cada turno entra al hilo de la memoria,
`web/lib/db.ts`, y de ahí a `respuestas_de_la_persona`), pero como una lista suelta, sin la pregunta y sin rótulo,
mientras que lo único rotulado como dato de la persona es la foto del contexto tomada al ABRIR la sesión. En la
segunda medición vio «Mi mayor riesgo es que dependo de un solo proveedor de resina» y aun así quitó una frase y volvió
pregunta otras seis («¿Usas resina en tus macetas?»), con el motivo «lo que solo contó una respuesta posterior sin
respaldo en el contexto guardado». Para retomarlo: pasarle lo dicho en la sesión rotulado como en el contexto (la
pregunta de la IA y la respuesta de la persona) y decirle que vale igual que el contexto guardado; y medir que no
convierta en pregunta lo que la persona ya dijo. En dos mediciones no mejoró a A de forma clara y suma un 69 % al
coste del plan.

### Estado al 9 oct 2026 (cierre): la última medición, hecha, y NO PASA

ACTA fila 18; informe `docs/corrida_final/2026-10-08/medicion_final/RESULTADO.md`. Camino de producción, versión A sin
verificador, dos jueces Opus 5.5 por la API y árbitro en las coincidencias: 2 contrarios, 13 invenciones y 2
procedencias en 10 de 14 planes (regla: 0, 2, 0); trampas 3/3; 9,29 USD.
- Arreglado y medido: la frase fija de «aún no cubre» (de 11 planes a 5, ninguno sostenido; ahora en los once
  idiomas), las premisas de las preguntas de la IA, los contrarios de cálculo del primer vuelo.
- Lo que queda lo escribe el redactor: una procedencia nueva («El material enseña…», «El material de este plan…»: la
  palabra con que el payload le nombra los nodos), hechos del negocio no dados (canales que «no pagan lo mismo»,
  tamaños que «no cuestan lo mismo»), causas y resultados prometidos en las bisagras, y dos contrarios de lectura de
  datos (las 12 macetas otra vez; «tus cinco anotaciones» cuando fueron tres).
- Rama `fidelidad-contexto` empujada y SIN fundir. El `.env` raíz sigue puesto hasta la decisión.

**Decisión del fundador (9 oct, noche): REDACTOR CON RESPALDO** (`docs/producto/REDACTOR_CON_RESPALDO.md`), en este
orden y UN PUNTO POR SESIÓN, cada uno con prueba en rojo primero y suites, tsc y Gate 0 en verde. La programación va con
la suscripción, en la sesión principal y sin subagentes; lectores, jueces y árbitros SIEMPRE como guion por la API
(`web/scripts/corrida_final_juez_api.ts`). Si se acerca el límite: terminar el paso, commit, push y anotar aquí.

| Orden | Punto | Estado |
|---|---|---|
| 1 | 1. «Material» y 5. Plan anterior | **HECHO y EN PRODUCCIÓN** (main fec45eebb, despliegue de producción correcto; también fundido en `fidelidad-contexto`, a938102e7) |
| 2 | 4. Menos prosa | **HECHO en `fidelidad-contexto`** (sin fundir): introducción corta (primer párrafo, dos frases como mucho) y etapas solo accionables (pasos, entregable como señal de hecho, primera acción), en el prompt y garantizado por código (`web/lib/engine/menosProsa.ts`, port al motor). Un solo prompt (`SYSTEM_PLAN`) y una sola ruta escriben el plan del núcleo, de mundo, el seguimiento y el replanteo, así que vale para los cuatro. Revisado en pantalla, Expediente y PDF, planes viejos incluidos |
| 3 | 2. Números por código | **HECHO en `fidelidad-contexto`** (ce8bfb459): bloques `numeros_de_la_persona` (cada cifra con lo que dijo, su alcance y lo que no es) y `calculos` (calculadora), regla 4-ter |
| 4 | 3. Citar o callar | **HECHO en `fidelidad-contexto`**: marcas ⟦R⟧ ⟦N:id⟧ ⟦?⟧ con pregunta de reserva; el código valida cada cita al guardar (`citarOCallar.ts`) y las quita también en vivo (filtro del streaming, con su prueba); el motor las quita. Regla 6-bis |
| 5 | Medición | cuando estén los cinco: decir el coste estimado de UNA medición con la regla de la fila 17 y esperar el visto. Revisar también el riesgo del punto 5 (ACTA fila 19): si un seguimiento repite una tarea hecha, la candidata es pasar el título del nodo de cada tarea hecha, no su texto |

Lo hecho en el punto 1: payload `temas_del_recorrido` / `temas_vecinos`; ningún prompt que llega a la IA dice
«material»; `REGLA_SIN_FUENTES` prohíbe citar los temas como fuente; filtro `web/lib/engine/citasDeFuente.ts` en los once
idiomas (motor en español). En el punto 5: de cada tarea viaja su estado y la nota de la persona, nunca su texto.
Riesgo anotado del punto 5: la regla 8-ter («no repetir lo hecho») ya no ve el texto de lo hecho; lo cubren las notas de
la persona, la exclusión de los temas ya cubiertos y las tareas heredadas por código. Vigilarlo en la medición.

**Encargo para Design (sin prisa, decisión del fundador del 10 oct 2026),** tras revisar el formato nuevo del plan
(menos prosa) en pantalla, Expediente y PDF:
- quitar el rótulo «Pasos:» de cada etapa (ahora va pegado al título, porque toda etapa empieza con pasos);
- la introducción del plan como cita (son las palabras de la persona y es la única prosa que queda);
- texto alineado a la izquierda en móvil (el justificado abre huecos grandes entre palabras; ya pasaba antes);
- el rótulo del entregable como «Sabrás que está hecha cuando…», en los once idiomas (copy: catálogo de rótulos del
  plan y su pintado en pantalla, Expediente y PDF).

**Lo que ninguno de los cinco puntos cubre (para después):** tres contrarios de un tema aplicado al revés dentro de un
paso. La cita al tema existe y es la correcta, así que citar o callar no lo ve:
- «busca un segundo proveedor» presentado como evitar el riesgo, cuando el tema lo llama reducir (M2A-f006-2);
- «llama a las referencias que ella misma te facilite», cuando el tema dice que las eliges tú (M2A-f012-2 y M2B-f004-2).
Idea anotada, sin decidir: que los pasos salgan de los pasos del tema adaptados (no reescritos) y que el código compare
cada paso con su origen.

**Decisión anterior que espera al fundador** (superada por la de arriba).

**Para retomar:** el clon de trabajo es `C:/Users/AlexDesk/Documents/my-idea-main` (rama `fidelidad-contexto`); el clon
`I have an idea` solo se pone al día con fast-forward. Merge a main solo con autorización explícita del fundador. Antes
de cualquier commit: `pnpm vitest run` (en `web/`) y `python engine/run_all_tests.py`.

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

- **Copia fiel (regla D2): parada segura el 7 oct 2026 por cuota; NO certificada (acta 15.15 y 15.16).**
  - **Hecho y aplicado en main** (todo lo que pasó el verificador ciego está aplicado; no queda nada verificado
    sin aplicar):
    - la pasada completa: 728 lotes de pasos, resúmenes y condiciones;
    - las reescrituras r1 y r2;
    - la medida 7 con su resultado: copia en 57 de 200 nodos, contrarios 0, invenciones 1;
    - lo hallado en la medida: la tanda h7 (137 correcciones) y la invención corregida;
    - las tandas k29 (72) y k30 (666) de la vecindad de los pasos.
  - **Máquina:** `auditoria-final-claves/copia/copia.py`. Las instrucciones de los agentes están en
    `auditoria-final/copia/`.
  - **Lo que queda, en este orden:**
    1. **Terminar de verificar la ola k31.** La ola tiene 1.915 propuestas de 32 lotes de la vecindad, en 96
       paquetes (`auditoria-final/copia/verif/paq_v_k31_01.json` a `_96.json`).
       - El 8 oct 2026 se verificaron los paquetes 01 a 20, con todas sus trampas cazadas. Su tanda, construida con
         `tanda k31 parcial`, está aplicada en `copia-k31.json`: 347 correcciones en 48 nodos y 53 que no sostienen.
       - Faltan los paquetes 21 a 96. Esos lotes ya figuran en `verificados.json`, así que se usan los paquetes que
         ya existen. El encargo del verificador es el de siempre: `INSTRUCCIONES_VERIFICADOR.md`, con salida
         `verif_v_k31_NN.json`.
       - **OJO al construir la segunda tanda:** `tanda k31` reescribe `copia-k31.json`, y sus ids chocan con los ya
         aplicados, así que el aplicador rechazaría la tanda entera. Hay que copiar los paquetes 21 a 96 bajo un nombre
         de ola nuevo, por ejemplo `k31b` (paquetes y `verif_trampas`), o filtrar de la salida los ids ya aplicados.
         Después se aplica y se corren run_phase1, etiquetas, plan_readiness, sync y commit.
    2. **Leer los 12 lotes de vecindad que quedaron sin leer:** V063, V067, V075, V076, V078, V079 y V081 a V086. Se
       pararon a medias y no dejaron salida. El encargo del lector va en `docs/ACTA_SANEAMIENTO_FINAL.md` 15.16:
       `INSTRUCCIONES_LECTOR.md` más la vara de la medida. Después: `verificacion k32`, verificadores, `tanda k32` y
       aplicar.
    3. **Reescribir lo que no sostuvo:** `python copia.py reescritura r3 k29` toma lo retenido de k29 en adelante: 5
       de k29, 111 de k30 y lo que dejen k31 y k32. Después: `verificacion_r r3`, verificadores, `tanda r3` y aplicar.
       Los 6 retenidos de h7 se le añaden aparte o quedan como residuo.
    4. **Decisión del fundador sobre los resúmenes:** su vecindad abarca 2.154 nodos, casi todos. Si se corre, es una
       segunda pasada completa, y la regla no la permite. Si no, se declara el residuo de resúmenes con su intervalo
       (medida 7: 38 resúmenes con copia confirmada en 21 libros).
    5. **Medida nueva:** muestra nueva con semilla nueva, fijada en el acta antes de sortear, con la misma máquina
       (`auditoria-final-claves/medida7/medida7.py`, cambiando la semilla). Después, la segunda pasada de Voyage
       (sección 4) y el despliegue.
  - **Ojo con los ids de las tandas:** desde k29, el id lleva la ola (`copia-k29-<nodo>-...`). Sin eso, el aplicador
    rechaza la tanda entera porque el id choca con una corrección anterior del mismo elemento.
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
