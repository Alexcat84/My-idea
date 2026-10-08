# Revisión del guion del vuelo contra las reglas cambiadas el 8 oct 2026

Paso 2 del cierre de la corrida final: antes de gastar API, cada fase pendiente del vuelo (`web/scripts/vuelo.ts`) se
revisó contra lo que cambió hoy, para corregir de una vez lo desfasado del GUION sin tocar el producto.

| Regla cambiada hoy | Commit | Fases afectadas | Qué se hizo en el guion |
|---|---|---|---|
| Fechas anteriores al proyecto: se aceptan y son lo DECLARADO, fuera del ritmo y de la puntualidad | b8534e8d8 | 2i, 2k, 2L, 2i-ter | 2i: la fecha anterior prueba que se acepta; las tres clases se miden con tareas hechas hoy (9d09c6aef). 2k, 2L, 2i-ter: las tareas de mundo se dan por hechas hoy y las bases se corren para conservar exactas las diferencias a mano (64f797a78); y nunca antes de que nazca su plan, que en 2k nace segundos antes (`hechoTrasSuPlan`, ea4079cf5) |
| Modo propio de cada mundo | (T3) | 2k, 2L, 2i-ter | sin cambio: 2L fija el modo del mundo y 2i-ter fija core, W1 y W2 de forma explícita; el desglose por dominio de 2k no depende del modo del mundo |
| Tope de 1 USD por sesión con cierre ordenado | 85bf10ad9 | todas las que conversan | sin cambio: el cierre ordenado devuelve `listo_para_plan`, que los bucles `while (r.tipo === "pregunta")` ya manejan; en este vuelo rige el 3,00 de Vercel |
| Calendario de mundos al cerrar la idea (solo calla el viaje principal) | d6b4f2075 | 2i | sin cambio: la tubería del calendario corre después de reabrir la idea |
| Ninguna causa inventada | 6dc6c832c | planes de todas las fases | sin cambio en el guion: lo mide el juez de fidelidad sobre todos los planes del vuelo |
| Modelos 5.5 (y el estimador en Sonnet 5.5) | ae3a0ddcc, fabe3961e | todas | sin cambio: el guion no nombra modelos; los costes los lee COSTES_MODELOS.md |
| Control del modo "a mi ritmo": el juicio sobre la puntualidad, no la expresión suelta | 3b9cb5840 | 2j | el guion usa `juiciosDeRitmo` (lib/coherencia/juicioDeRitmo.ts) |

Fases revisadas sin nada desfasado: 2M (el mundo nunca abandona), 2P (ciclo de protección: fechas futuras del carril,
sin completados), 3 (reporte digital) y 4 (guardián GIGO).
