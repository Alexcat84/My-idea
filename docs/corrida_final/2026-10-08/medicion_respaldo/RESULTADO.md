# Medición final con el redactor con respaldo (10 oct 2026)

Los cinco puntos de `docs/producto/REDACTOR_CON_RESPALDO.md` en el código (rama `fidelidad-contexto`, 1647854d8).
Mismos 14 planes del vuelo, por el camino de producción, versión A sin verificador. Regla de cierre del acta, fila 17
(escrita en la fila 20 con la semilla 20261017 antes de medir):
- dos jueces Opus 5.5 por la API;
- árbitro en lo que encontraron los dos;
- PASA con 0 contrarios, como mucho 2 invenciones y 0 procedencias.

## Veredicto: NO PASA, y peor que la medición anterior

| | Esta medición | Medición anterior (M3) | Regla |
|---|---:|---:|---:|
| Contrarios | **9** | 2 | 0 |
| Invenciones | **21** | 13 | como mucho 2 |
| Procedencias | **0** | 2 | 0 |
| Planes con algún sostenido | 12 de 14 | 10 de 14 | n/a |
| Trampas | 3 de 3 (la de contrario, en la relectura) | 3 de 3 | todas |

Las marcas de cita no llegaron a ningún plan (0 de 14). Las procedencias bajaron a 0: el punto 1 funcionó.

## Por qué empeoró: 23 de los 30 vienen del bloque de números (punto 2), por dos causas distintas

1. **Defecto del guion de medición (18 sostenidos: f008, f009, f010 y f011).**
   - El guion arma el bloque con los `numeros_proyecto` de HOY, no con las cifras que tenía el proyecto en el momento
     de cada plan.
   - Esos proyectos guardan hoy las cifras que la fase 3 del vuelo siembra a propósito para disparar el guardián GIGO:
     precio 13 contra un costo de 400, 200 al mes, 4 horas.
   - Los planes viejos recibieron cifras que la persona aún no había dado, como «Tú dijiste 200 por mes» o «Con lo
     que diste es 0».
   - Es el mismo tipo de defecto que el estado vivo de hoy en la primera medición. En producción, el plan lee las
     cifras de su momento.
2. **Defecto de producto del punto 2 (5 sostenidos: f006 y f013).**
   - Un costo con la hora incluida (130) estaba guardado como `costo_materiales_unidad` desde antes de c6e51feec.
   - El bloque lo etiqueta bien («incluye su tiempo»), pero la calculadora le sumó otra vez las horas: 130 + 2 × 50 =
     230, con un margen de 20 en lugar de 120.
   - El calculo no debe hacerse cuando la cifra dice que ya incluye el tiempo.

## Los otros 7, ya conocidos

- La feria local de agosto, dos veces (f002, f015).
- Las 12 macetas de Instagram tratadas como total (f005).
- Las referencias que elige el candidato (f004, de los contrarios que ningún punto cubre).
- Fijo frente a comisiones (f001, dos).
- **Una vez el riesgo del punto 5 (f003):** un seguimiento volvió a proponer una tarea que la persona había retirado
  («multiplica tus horas por el valor de tu hora»). La solución candidata está en el acta, fila 19: pasar el título
  del nodo de cada tarea hecha o retirada.

## Otra señal, sin efecto en el juez

La autodeclaración de cobertura (el bloque interno del final) falló en 9 de 14 planes (5 en M3). Afecta a la
etiqueta de plan completo o inicial y al bloque de lo que falta, no a lo que mira el juez.

## Coste (estimado por los guiones; la cifra oficial es la consola)

| Pieza | Modelo | Llamadas | USD |
|---|---|---:|---:|
| Redacción de los 14 planes | Sonnet 5.5 | 14 | 1,0791 (tope 1,50) |
| Dos jueces por paquete y árbitro | Opus 5.5 | 34 + 13 | 8,5553 (tope 12) |
| **Total** | | **61** | **9,63** |

Se para aquí sin arreglar nada y la rama no se funde en main (regla del fundador). Archivos:
- `A/`;
- `costes.json`;
- `claves_A.json`;
- `veredictos_A/`;
- `sostenidos.txt`;
- `redaccion.log`, `juez.log`.
