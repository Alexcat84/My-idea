# Última medición: el camino de producción y dos jueces

Decisión del fundador (9 oct 2026, visto del punto 6). Los mismos 14 planes del vuelo, redactados de nuevo **por el
camino de producción** (acta fila 16), en la versión A: sin verificador, que queda APAGADO.

Ya iban en el código:
- la frase de «aún no cubre: validar con clientes» solo cuando las etapas de verdad no validan con clientes;
- el contexto con la pregunta de la IA y la respuesta de la persona separadas;
- las reglas de los cinco redactores.

Cómo se juzgó:
- dos jueces independientes por paquete (Opus 5.5 por la API);
- el árbitro (Opus 5.5) solo vio los hallazgos que encontraron los dos;
- trampas con la semilla 20261016.

**Regla de cierre del acta, fila 17, escrita antes de medir:** 0 contrarios, como mucho 2 invenciones (declaradas
como residuo) y 0 procedencias; todas las trampas cazadas.

## Veredicto: NO PASA

| | Resultado | Regla |
|---|---:|---:|
| Contrarios sostenidos | **2** | 0 |
| Invenciones sostenidas | **13** | como mucho 2 |
| Procedencias sostenidas | **2** | 0 |
| Planes con algún sostenido | 10 de 14 | n/a |
| Hallazgos de los dos jueces (17 paquetes, trampas incluidas) | 33 y 29 | n/a |
| Coincidencias en los planes reales que llegaron al árbitro | 19 (17 sostenidas, 2 descartadas) | n/a |
| Trampas cazadas | 3 de 3, por los jueces, sin relectura | todas |

Los dos jueces coincidieron en casi todo: lo que queda no es ruido de un solo juez.

Lo que sí cambió desde la medición anterior: la frase fija de «aún no cubre» salió en 5 planes (antes, 11), solo en
mundos cuyas etapas no tratan con clientes, y ningún sostenido es esa frase.

## Lo que queda (todo lo escribe el redactor)

1. **Procedencia nueva: «el material».** El redactor nombra su propia fuente:
   - «El material enseña que la seguridad funciona cuando la gente participa» (Salud y Seguridad 85248377);
   - «El material de este plan no cubre seguridad informática en detalle» (núcleo 31ebf0ea).

   Es la palabra con la que el payload le llama a los nodos. Las dos se sostuvieron como procedencia (insinúan de dónde
   sale el consejo).
2. **Hechos del negocio que nadie dio, dichos como ciertos (la mayoría de las invenciones):**
   - «la tienda de plantas y Instagram no pagan lo mismo» (dos planes);
   - el margen «distinto en la tienda, en Instagram y en la feria»;
   - «no cuestan lo mismo» (los dos tamaños);
   - «quienes siguieron comprando ya te conocían»;
   - «el lote puede dejarte piezas paradas»;
   - «la feria local de agosto»: viene arrastrada del plan anterior, donde ya era un invento.
3. **Causas y resultados prometidos en las bisagras:**
   - «Este es el paso que más te ayuda a dejar de apagar incendios»;
   - «Quien va bien y nunca lo oye queda sin referencia»;
   - «Contratar con método evita repetir lo que hoy te cuesta»;
   - «por eso tus lotes no salen parejos»;
   - «ahí se esconde un gasto que aún no estás viendo»;
   - «tu tiempo es el recurso más escaso».
4. **Dos contrarios de lectura de datos:**
   - las 12 macetas de Instagram tratadas como el total, otra vez (Riesgos ff010188);
   - «tus cinco anotaciones tomaron más de lo previsto», cuando el registro dice que solo tres se atrasaron (Salud y
     Seguridad 0e481ad8).

Las tres mediciones apuntan a lo mismo: lo que el redactor afirma por su cuenta en los conectores (causas,
consecuencias, diferencias entre canales). No son fallos de memoria ni de contexto, ni de las frases fijas del código.

## Coste (estimado por los guiones; la cifra oficial es la consola del fundador)

| Pieza | Modelo | Llamadas | USD |
|---|---|---:|---:|
| Redacción de los 14 planes por el camino de producción | Sonnet 5.5 | 14 | 1,1103 (tope 1,50) |
| Dos jueces por paquete y árbitro en las coincidencias | Opus 5.5 | 34 + 10 | 8,1834 (tope 12) |
| **Total** | | **58** | **9,29** |

## Archivos

- `A/`: los 14 planes;
- `costes.json`: coste por plan y avisos del estado vivo (ninguno);
- `claves_A.json`: la clave de las trampas;
- `veredictos_A/`: cada juez (`_j1`, `_j2`), las coincidencias (`fNNN.json`), cada árbitro y `resumen.json`;
- `redaccion.log`, `juez.log`.

Se para aquí sin arreglar nada (regla del fundador). La rama `fidelidad-contexto` no se funde en main.
