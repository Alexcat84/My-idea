# Corrida final, 8 de octubre de 2026

La medición completa de My Idea con los modelos nuevos (Sonnet 5.5 y Haiku 5.5) antes de la beta: la caché de
preguntas, la prueba de coherencia, el vuelo completo contra producción, el juez de fidelidad de lo que la persona lee
y los costes reales. Las horas, las decisiones y cada intento están en [ACTA.md](ACTA.md).

## Cada umbral contra su resultado

| Paso | Umbral (fijado antes de medir) | Resultado | Veredicto |
|---|---|---|---|
| 1. Caché de preguntas: neutrales por niveles | 0 cambios de sentido y como mucho 10 de 200 en lo demás, en una muestra ciega con trampas y árbitro | Cuarta muestra (semilla 20261011): 0 cambios de sentido, 16 de 200 en lo demás, trampas 10/10. Regla de cierre del fundador: lo hallado se corrige y el residuo se declara | **PASA por la regla de cierre** (residuo declarado en el acta, fila 5o) |
| 2. Prueba de coherencia (3 personas × 11 espacios) | papel 0, contexto, adaptadas fieles y trampas, según el fundador | Papel 0, 0, 0; contexto 1 de 112, 1 de 89, 0 de 86; adaptadas fieles 12/12, 18/18, 14/14; trampas 4/4 cada una | **PASA** (umbrales del fundador) |
| 2b. Dictamen del arnés: ficha de memoria | la ficha guarda el papel y el jefe del retrato | papel 'desconocido' y jefe mal para la persona sola | **NO CUMPLE** en la medición; arreglado después (f79be60b9), sin volver a medir |
| 3. Vuelo completo contra producción | todas las verificaciones del guion | Intento 10 (fases 0 a 2P, 91 verificaciones) + fases 3 y 4 sueltas, sobre el mismo código de producto (acta 7k y 7l) | **PASA** |
| 4. Juez de fidelidad, tramo B (coherencia) | 0 contrarios, 0 invenciones, 0 procedencias | 1 invención sostenida por el árbitro en 3 planes; trampa cazada en relectura | **NO PASA** |
| 4. Juez de fidelidad, tramo C (vuelo) | 0 contrarios, 0 invenciones, 0 procedencias | 11 sostenidos en 7 de 14 planes (9 invenciones, 2 contrarios, 0 procedencias); trampas 4/4; Claridades limpias | **NO PASA** |
| 5. Costes | la cifra oficial es la consola del fundador | Saldo inicial 19,67 USD (01:05 UTC); saldo final pendiente. Desglose por pieza y modelo en COSTES_MODELOS.md | **PENDIENTE** de la cifra de la consola |
| 6. Cierre de Vercel | devolver los límites a sus valores por defecto | Borradas LIMITE_ARRANQUES_DIA, FUSIBLE_SESIONES_DIA y PRESUPUESTO_SESION_USD; redespliegue; rigen 5 arranques, 30 sesiones y 1 USD por sesión | **HECHO** |

## El juez de fidelidad (lo que no pasa)

El informe completo, con cada frase, su evidencia y el veredicto del árbitro: [docs/coherencia/2026-10-08/fidelidad.md](../../coherencia/2026-10-08/fidelidad.md).

Lo que se arregló después del tramo C, con pruebas en rojo primero (decisiones del fundador, 8 oct, noche):
- **«Lo que este plan aún no cubre»** se calcula contra las etapas reales del plan y nunca las contradice (c0ab3a89a).
- **La moneda** sale de lo que dijo la persona, nunca de la IA: se quita o se corrige en código antes de entregar el plan,
  y el intérprete guarda la moneda tal como la dijo (bfbd1fddc).
- **Datos del negocio** que la persona no dio y que no vienen de sus nodos se escriben como pregunta o comprobación, en
  los cinco redactores, con las frases reales del informe (bfbd1fddc).

El verificador en producción y la medición barata se resolvieron después: ver la sección siguiente (B NO PASA).

## La medición barata: A (solo reglas) contra B (reglas + verificador)

Los 14 planes del vuelo, redactados de nuevo desde sus entrevistas guardadas (sin guardar nada), pasados por el mismo
juez con trampas sin marca y árbitro, umbral 0. A y B comparten borrador; B es A con el verificador (Sonnet 5.5, sin
desplegar). Informe completo, con cada hallazgo sostenido: [medicion_ab/RESULTADO.md](medicion_ab/RESULTADO.md).

| | A (solo reglas) | B (reglas + verificador) | Umbral |
|---|---:|---:|---:|
| Sostenidos por el árbitro | 14 (11 invenciones, 3 contrarios) | 10 (7 invenciones, 3 contrarios) | 0 |
| Planes con algún sostenido | 7 de 14 | 8 de 14 | 0 |
| Trampas cazadas | 3 de 3 | 3 de 3 (una en la relectura) | todas |
| Coste de API | 1,1161 USD (redactor, compartido) | + 0,7502 USD (verificador) = 1,8664 | tope 2,00 |

**Veredicto: B NO PASA.** Regla de cierre del fundador: se para y se reporta, sin arreglar. El verificador **no se
desplegó** (`VERIFICADOR_PLAN` apagado por defecto). Lo que deja pasar son inventos de negocio plausibles y contrarios de
cálculo u orden que un verificador que solo quita o pregunta no corrige. El juez y el árbitro resolvieron distinto frases
idénticas entre versiones: con umbral 0, un solo caso límite decide. Pendiente de decisión del fundador y de anotar la
cifra final de la consola; el `.env` raíz se queda hasta entonces.

**Defecto de la medición (declarado el 9 oct):** el guion de redacción sumó el estado vivo de hoy (el que siembra la fase 2M,
«kits de huerto») a los planes de mundo; afecta a 3 sostenidos y no cambia el veredicto (sin ellos, A 12 y B 9). Detalle en
[medicion_ab/RESULTADO.md](medicion_ab/RESULTADO.md). Las opciones de decisión están en `docs/PROXIMOS_PASOS.md` §5.

## La segunda medición A/B: el contexto arreglado (9 oct)

Arreglos (ea094911d, rama `fidelidad-contexto`, sin push): en el contexto, la pregunta de la IA y la respuesta de la
persona van separadas y solo la respuesta es dato suyo; la misma regla en los cinco redactores; el verificador busca
también lo que solo aparece en una pregunta y los contrarios de cálculo u orden; sin el defecto del guion. Juez,
relectura y árbitro por la API (Opus 5.5). Informe: [medicion_ab2/RESULTADO.md](medicion_ab2/RESULTADO.md).

| | A (solo reglas) | B (reglas + verificador) | Umbral |
|---|---:|---:|---:|
| Sostenidos por el árbitro | 14 (9 invenciones, 5 contrarios) | 15 (9 invenciones, 6 contrarios) | 0 |
| Planes con algún sostenido | 7 de 14 | 9 de 14 | 0 |
| Trampas cazadas | 3 de 3 | 3 de 3 | todas |
| Coste de API | 1,1126 USD (redactor, compartido) | + 0,7725 USD (verificador) = 1,8851; juez por la API 9,29 estimado | tope 2,10 + 30 |

**Veredicto: B NO PASA.** Se para y se reporta, sin arreglar ni desplegar. Lo buscado desapareció de los borradores
(premisas de preguntas, «siguen vigentes», la resta al revés, la cuota de defectos). Lo que queda: (1) una **frase fija
del motor** («Lo que este plan aún no cubre: validar con clientes reales…», de `plan_readiness`) en 11 de 14 planes,
sostenida como contrario en 3 (B) y 2 (A); sin ella, A 12 y B 12; (2) causas y resultados prometidos en las bisagras del
texto, que el verificador deja pasar; (3) ruido del juez. Y un daño nuevo del verificador que el juez no cuenta: vuelve
pregunta lo que la persona dijo en la misma sesión («¿Usas resina en tus macetas?»).

## La última medición: camino de producción y dos jueces (9 oct)

Versión A sin verificador (apagado), los 14 planes redactados de nuevo por el camino de producción, con la frase de
«aún no cubre» corregida. Dos jueces independientes (Opus 5.5 por la API) y el árbitro solo en lo que encontraron los
dos. Regla de cierre del acta, fila 17. Informe: [medicion_final/RESULTADO.md](medicion_final/RESULTADO.md).

| | Resultado | Regla |
|---|---:|---:|
| Contrarios | 2 | 0 |
| Invenciones | 13 | como mucho 2 |
| Procedencias | 2 | 0 |
| Planes con algún sostenido | 10 de 14 | n/a |
| Trampas cazadas | 3 de 3 | todas |
| Coste | 1,1103 USD redacción + 8,1834 jueces y árbitro = 9,29 | topes 1,50 y 12 |

**Veredicto: NO PASA.** Se para sin arreglar; `fidelidad-contexto` no se funde. Lo que queda lo escribe el redactor:
una procedencia nueva («El material enseña…»), hechos del negocio que nadie dio, causas y resultados prometidos en las
bisagras y dos contrarios de lectura de datos. La frase fija de «aún no cubre» ya no se sostiene en ningún plan.

## El redactor con respaldo: dos mediciones finales (10 oct)

Los cinco puntos de `docs/producto/REDACTOR_CON_RESPALDO.md` en `fidelidad-contexto`; regla de la fila 17 (dos jueces
Opus 5.5 por la API, árbitro en las coincidencias; 0 contrarios, como mucho 2 invenciones, 0 procedencias).

| | Primera (fila 21) | Segunda (fila 23) | Regla |
|---|---:|---:|---:|
| Contrarios | 9 | **3** | 0 |
| Invenciones | 21 | **3** | como mucho 2 |
| Procedencias | 0 | **0** | 0 |
| Planes con algún sostenido | 12 de 14 | 6 de 14 | n/a |
| Coste | 9,63 USD | 8,22 USD | n/a |

**La primera** la estropearon un defecto del guion (las cifras de hoy) y uno de producto (la hora duplicada en la
calculadora). Se arreglaron con el visto del fundador, junto con la candidata del punto 5. **La segunda NO PASA, pero
con 6:**
- la feria de agosto, que llega por el mensaje de entrada del seguimiento (el texto de cada tarea del plan anterior);
- tres temas aplicados al revés dentro de un paso;
- «hecha a mano» en un título.

Informes: [medicion_respaldo/RESULTADO.md](medicion_respaldo/RESULTADO.md) y
[medicion_respaldo2/RESULTADO.md](medicion_respaldo2/RESULTADO.md).

## Qué hay en esta carpeta

| Archivo o carpeta | Qué es |
|---|---|
| [ACTA.md](ACTA.md) | cada paso con su hora, sus decisiones y cada intento del vuelo |
| [COSTES_MODELOS.md](COSTES_MODELOS.md) | coste por corrida, por modelo, por pieza, por llamada y por espacio; la caché; el tope; la consulta SQL; contra el vuelo del 27 sep (Sonnet 4.6 + Haiku 4.5) |
| [coherencia/](coherencia/) | la prueba de coherencia: por proyecto, cada sesión turno por turno y cada documento tal como lo lee la persona |
| [medicion_ab/](medicion_ab/) | la medición barata: los 14 planes redactados de nuevo en A y en B, los veredictos del juez y del árbitro y el informe |
| [medicion_respaldo/](medicion_respaldo/) | primera medición final del redactor con respaldo (NO PASA, 30; defecto del guion y de producto) |
| [medicion_respaldo2/](medicion_respaldo2/) | segunda medición final del redactor con respaldo (NO PASA, 6) |
| [medicion_final/](medicion_final/) | la última medición (camino de producción, dos jueces): planes, cada juez, las coincidencias, cada árbitro y el informe |
| [medicion_ab2/](medicion_ab2/) | la segunda medición A/B (contexto arreglado): planes, veredictos del juez por la API y el informe |
| [vuelo/](vuelo/) | el vuelo final validado (intento 10 + fases 3 y 4): igual, por proyecto, sesión por sesión y cada plan completo |
| [revision_guion_vuelo.md](revision_guion_vuelo.md) | el guion del vuelo revisado contra las reglas cambiadas hoy |
| `vuelo_transcripcion_*.txt` | la salida de cada intento del vuelo |
| `costes_*.json`, `base_vuelo_2026-09-27.json` | los volcados de coste (solo números, con el registro por llamada desde los modelos 5.5) |
| [medicion_cache_anclaje.txt](medicion_cache_anclaje.txt) | el ahorro del arreglo de la caché del anclaje (77,6 % con la misma sesión) |
| `verificacion_neutrales*.md`, `guarda_neutrales*.md`, `JUEZ_*.md` | las muestras ciegas de la caché de preguntas y sus instrucciones |

Sin claves, contraseñas ni correos: todo lo exportado pasa por la limpieza del exportador.
