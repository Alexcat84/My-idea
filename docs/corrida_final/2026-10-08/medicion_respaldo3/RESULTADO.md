# Tercera medición final (acta, filas 25 y 26)

Mismos 14 planes del vuelo, camino de producción, versión A sin verificador, **comprobador paso contra nodo encendido**.
Regla de la fila 17, semilla 20261019, escrita antes de medir (69f4f0bd2). Código: `fidelidad-contexto` en 2b8221159.

## Veredicto: NO PASA

| | Sostenidos | Tope |
|---|---|---|
| Contrarios | 1 | 0 |
| Invenciones | 1 | 2 (declaradas como residuo) |
| Procedencias | 0 | 0 |

En 2 de 14 planes. Trampas 3 de 3 cazadas por los jueces (f006 contrario, f008 procedencia, f009 invención): la medición vale.
Evolución: M5 (fila 23) 6 sostenidos en 6 planes; M6 2 en 2.

Se para aquí sin arreglar. El comprobador NO se despliega y la rama no va a main.

## Los dos sostenidos

1. **Contrario, fb027af0 (núcleo), sección fija «¿Puede sostenerse tu idea?»** (prosa, no un paso):
   «Con las cifras que me diste, tu costo de hacer una maceta, contando tu hora, es mayor que lo que cobras. Hay un
   número que aún no sabes y es el que decide cuántas macetas necesitas vender cada mes.»
   El árbitro: con margen negativo (102 de costo contra 85 de precio), la fórmula del tema `punto_equilibrio_unidades`
   no da ninguna cantidad; lo que decide primero es el precio o el costo, no los costos fijos que faltan.
   El comprobador no lo ve: solo juzga pasos.
2. **Invención, b4a01dea (núcleo), paso 1.5:** «Prepárate para comentarios impredecibles y a veces dolorosos: son los
   que más te ayudan a ajustar.» La cola («son los que más te ayudan a ajustar») es un resultado en superlativo que
   ningún tema da. El comprobador busca contradicciones, no invenciones; y la cola de dos puntos no la corta
   `validarCitas` (solo corta colas con «porque», «ya que»...).

Lo que ya no aparece: la feria de agosto (2a), «hecha a mano» (2b: el título de b4a01dea ahora es otro), y los tres
contrarios de la M5 dentro de pasos.

## El comprobador en la medición

Juzgó 300 pasos con tema en 14 planes y quitó 4. Leídos uno por uno, **al menos 3 son falsos positivos**:

| Plan | Paso quitado | Juicio |
|---|---|---|
| ff010188 2.4 | «Marca los riesgos improbables pero capaces de hundirte... y no los sueltes aunque su probabilidad sea baja.» | Dice lo mismo que el tema. Falso positivo. |
| ee6de956 3.4 | «Antes de invertir más, haz una prueba rápida de interés...» | El tema dice «considera hacer antes una prueba rápida»: matiz, no lo contrario. Falso positivo. |
| 8b7764c4 5.4 | «...no uses el instinto de pocos minutos ni preguntas hipotéticas...» | El propio motivo del modelo dice que «coincide con el tema». Falso positivo. |
| 85248377 2.4 | «Aplica primero el control del peligro peor y deja los menores para después, si los recursos no alcanzan...» | El tema dice «controlar sin demora los peligros serios»: discutible. |

La guarda de las dos frases citadas tal cual no basta: el modelo cita bien y aun así marca lo que no es contrario.
Ninguno de los 4 quitados era un hallazgo de los jueces. Coste del comprobador en la medición: 0,1638 USD (14 planes,
0,012 por plan de media).

## Coste

| Parte | USD |
|---|---|
| Redacción de los 14 planes + comprobador (tope 1,60) | 1,1436 |
| Dos jueces y árbitro, Opus 5.5 (tope 12), estimado | 6,5875 |
| **Medición** | **7,7311** |
| Pruebas del punto 3 con los 3 contrarios (antes de medir) | 0,6253 |

## Archivos

`A/` planes medidos (ya comprobados), `A_previo/` los mismos antes del comprobador, `costes.json` (con lo que propuso
y quitó el comprobador en cada plan), `claves_A.json`, `veredictos_A/`, `redaccion.log`, `juez.log`.
