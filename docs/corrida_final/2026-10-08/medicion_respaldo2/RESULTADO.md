# Segunda medición final del redactor con respaldo (10 oct 2026)

Los cinco puntos de `docs/producto/REDACTOR_CON_RESPALDO.md` y los arreglos de la fila 22 del acta:
- cifras del momento de cada plan en el guion;
- calculadora sin la hora duplicada (visto del fundador);
- el título del tema de cada tarea hecha o retirada;
- topes con reserva;
- el dataset con la copia fiel cerrada.

Antes de medir, una comprobación sin API (2d) confirmó que el guion entrega al redactor las mismas entradas que
producción en ese momento.

Mismos 14 planes, camino de producción, versión A sin verificador. Regla de la fila 17, semilla 20261018:
- dos jueces Opus 5.5 por la API;
- árbitro en lo que encuentran los dos;
- PASA con 0 contrarios, como mucho 2 invenciones y 0 procedencias.

## Veredicto: NO PASA, pero de 30 a 6

| | Esta medición | Medición anterior (fila 21) | M3 (fila 18) | Regla |
|---|---:|---:|---:|---:|
| Contrarios | **3** | 9 | 2 | 0 |
| Invenciones | **3** | 21 | 13 | como mucho 2 |
| Procedencias | **0** | 0 | 2 | 0 |
| Planes con algún sostenido | 6 de 14 | 12 de 14 | 10 de 14 | n/a |
| Trampas | 3 de 3 (la de contrario, en la relectura) | 3 de 3 | 3 de 3 | todas |

Ninguna marca de cita llegó a ningún plan; ninguna procedencia; ninguna cifra que la persona no hubiera dado.

## Los 6

1. **La feria de agosto, dos veces (f003, f009; planes de seguimiento 31ebf0ea y c73e86f8): una tercera vía.**
   - El punto 5 ya no manda el texto de las tareas en `plan_anterior`.
   - Pero el **mensaje de entrada del seguimiento** (`textoOriginal`), que la app compone con el listado de avance,
     sigue llevando el texto de cada tarea del plan anterior («- Anota si la feria local de agosto te sirve…»).
   - Comprobado en la base, en las dos sesiones.
2. **Tres contrarios de un tema aplicado al revés dentro de un paso**, la categoría que ningún punto cubre (anotada en
   PROXIMOS_PASOS desde el 9 oct):
   - «busca un proveedor alterno de resina», cuando el tema enseña a ir hacia un proveedor único (f002);
   - encargar a otro una decisión que el tema pide no soltar (f001);
   - moldes y empaques como costo fijo, cuando la persona los puso en su costo por pieza y el tema los clasifica como
     variables (f016).
3. **«Plan para tu pieza hecha a mano» (f012):** el título da por hecho cómo fabrica la persona.

## Otras señales, sin efecto en el juez

- La autodeclaración de cobertura falló en 8 de 14 planes.
- Cuatro planes recibieron solo las cifras de la propia sesión: las del proyecto eran posteriores al plan. El guion lo
  avisa plan por plan.

## Coste (estimado por los guiones; la cifra oficial es la consola)

| Pieza | Modelo | USD |
|---|---|---:|
| Redacción de los 14 planes | Sonnet 5.5 | 1,0601 (tope 1,50) |
| Dos jueces por paquete y árbitro | Opus 5.5 | 7,1552 (tope 12) |
| **Total** | | **8,22** |

Se para aquí sin arreglar nada y la rama no se funde en main (regla del fundador). Archivos:
- `A/`;
- `costes.json`;
- `claves_A.json`;
- `veredictos_A/`;
- `redaccion.log`, `juez.log`.
