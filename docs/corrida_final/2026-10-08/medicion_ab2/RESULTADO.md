# Segunda medición A/B: el contexto arreglado, con y sin verificador

Decisión del fundador (9 oct 2026): arreglar el contexto y medir otra vez. Arreglos (ea094911d, rama
`fidelidad-contexto`, sin push):
- en el contexto, la pregunta de la IA y la respuesta de la persona van separadas y rotuladas, y solo la respuesta
  es dato suyo;
- la misma regla está en los cinco redactores;
- el verificador marca también lo que solo aparece en una pregunta de la IA, el paso o el cálculo que contradice al
  nodo, y lo que da por hecho algo pendiente;
- el guion de redacción ya no suma el estado vivo de hoy (el defecto declarado de la primera medición).

Mismos 14 planes y mismos paquetes del tramo C.
- **A** = solo reglas;
- **B** = A + el verificador, sobre el mismo borrador.

Escrito en el acta ANTES de medir (filas 14 y 14b):
- semillas de las trampas: A 20261014, B 20261015;
- tope de redacción: 2,10 USD;
- juez, relectura y árbitro **por la API** (Opus 5.5, `web/scripts/corrida_final_juez_api.ts`), tope de 30 USD;
- **regla de cierre:** B pasa solo con 0 contrarios, 0 invenciones y 0 procedencias sostenidos por el árbitro y todas
  sus trampas cazadas; si no, se para y se reporta sin arreglar ni desplegar.

## Veredicto: B NO PASA (y A tampoco)

| | A (solo reglas) | B (reglas + verificador) | Umbral |
|---|---:|---:|---:|
| Sostenidos por el árbitro | **14** (9 invenciones, 5 contrarios, 0 procedencias) | **15** (9 invenciones, 6 contrarios, 0 procedencias) | 0 |
| Planes con al menos un sostenido | 7 de 14 | 9 de 14 | 0 |
| Hallazgos brutos del juez (planes reales) | 16 | 18 | n/a |
| Descartados por el árbitro | 2 | 3 | n/a |
| Trampas sin marca cazadas | 3 de 3 (sin relectura) | 3 de 3 (sin relectura) | todas |

Primera medición, como referencia: A 14 y B 10 (12 y 9 sin el defecto del guion), con jueces que eran subagentes.
El modelo es el mismo, pero el método cambió de vehículo, así que la comparación entre mediciones es orientativa. La
comparación A contra B dentro de esta medición sí es limpia.

## Lo que cambió

**Lo que se buscaba arreglar desapareció de los borradores, tanto en A como en B.** Ninguna de estas frases aparece en
los 14 planes nuevos (en la primera medición sí aparecían):
- la premisa de una pregunta de la IA tomada como hecho («y ya decidiste empezar esta semana»);
- «los números del plan anterior siguen vigentes»;
- la resta al revés;
- la cuota de piezas con defecto por lote.

Ningún sostenido de esta medición es la premisa de una pregunta de la IA.

## Lo que queda: tres familias, y una no la escribe la IA

1. **Una frase fija del motor, no de la IA (3 sostenidos en B, 2 en A).** Es «Lo que este plan aún no cubre: validar
   con clientes reales (conversaciones, una primera versión sencilla de tu producto, pruebas con usuarios, una venta o
   preventa real)». Sale de `plan_readiness` (`engine/plan_readiness.py:85`, `web/lib/i18n/mensajes/motor.ts:13`) y
   aparece en **11 de los 14 planes** de A y de B.
   - El árbitro la sostiene como contrario donde el plan sí trabaja con clientes reales, o donde la persona ya vende
     un producto terminado.
   - En los demás planes el juez no la marcó: la misma frase en 11 planes, sostenida en 3 (B) o 2 (A).
   - El verificador no la toca, y ninguna regla de redacción puede quitarla.
   - Sin esta frase: A = 12, B = 12.
2. **Causas y resultados prometidos en las bisagras del texto (la mayoría de las invenciones).** Las pone el redactor,
   y el verificador las dejó pasar en B. Están en los dos:
   - «que además suele cuidar el ritmo de la producción»;
   - «Predicar con el ejemplo quita el aire de reproche»;
   - «sin que te quite tiempo»;
   - «Ahora el cuidado de cada pieza es lo que sostiene ese precio»;
   - «las quejas llegan porque lo "aceptable" vive solo en tu cabeza»;
   - «esa claridad solo existe en tu cabeza, y por eso acabas haciendo el trabajo tú»;
   - «Chicas y medianas llevan distinto material y distinto tiempo».

   Además, dos contrarios de lectura:
   - las 12 macetas de Instagram tratadas como el total;
   - «llama a las referencias que ella misma te facilite», cuando el nodo dice que eliges tú.
3. **Ruido del juez (3 en cada versión).** Tres frases idénticas en A y en B se sostuvieron solo en B:
   - «aunque todavía no hayas nombrado un riesgo concreto»;
   - «lo más barato y rápido es observar y escuchar»;
   - «Tu producto hecho a mano».

   Lo que se sostuvo solo en A sí lo quitó el verificador en B:
   - «la feria local de agosto»;
   - «Si Instagram pesa mucho, eso confirma…».

## Un daño nuevo del verificador (el juez no lo cuenta)

En el plan de Riesgos (ff010188), la persona dijo en esa misma sesión: «Mi mayor riesgo es que dependo de un solo
proveedor de resina; si sube el precio o desaparece, no puedo producir ni entregar».
- El verificador quitó una frase y volvió pregunta otras seis que se apoyaban en ese dato («¿Usas resina en tus macetas?»,
  «¿Dependes de un solo proveedor?»). Su motivo: «lo que solo contó una respuesta posterior sin respaldo en el
  contexto guardado».
- Desconfía de lo que la persona dice durante la sesión porque todavía no está en la foto del contexto que se tomó al
  abrirla.
- El juez no lo cuenta: una pregunta no es una invención. Pero la persona leería que le preguntan lo que acaba de
  decir.

## Coste

| Pieza | USD |
|---|---:|
| Redactor, 14 planes (un borrador por plan, compartido por A y B) | 1,1126 |
| Verificador (Sonnet 5.5), 14 planes | 0,7725 (media 0,0552; mín 0,0312, máx 0,0805) |
| **Redacción de la medición** | **1,8851** (tope 2,10) |
| Juez, relectura y árbitro por la API (Opus 5.5, 51 llamadas) | 9,29 estimado (tope 30) |

El verificador propuso 87 ediciones, aplicó 83 e ignoró 4; ninguna fue a revisión (el tope del 20 % no se tocó) y no
falló ninguna llamada. El coste del juez es una estimación del guion con 5/25 USD por millón de tokens; la cifra
oficial es la consola del fundador.

## Archivos

- `A/`, `B/`: los 14 planes de cada versión;
- `costes.json`: coste y ediciones del verificador por plan;
- `claves_A.json`, `claves_B.json`: la clave de las trampas;
- `veredictos_A/`, `veredictos_B/`: cada juez, cada árbitro y `resumen.json`;
- `redaccion.log`, `juez.log`.

Se para aquí sin arreglar nada (regla de cierre del fundador). El verificador sigue sin desplegar y la rama sigue sin
fusionar.
