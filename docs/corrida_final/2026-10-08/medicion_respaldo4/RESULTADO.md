# Cuarta medición final (acta, filas 27 y 28)

Mismos 14 planes del vuelo, camino de producción, versión A sin verificador y sin comprobador (como producción).
Regla de la fila 17, semilla 20261020, escrita antes de medir (f5d6df1f6). Código: `fidelidad-contexto` en 646cccb0f
(main desplegado en d29e0ac0f + el arreglo de margen negativo).

## Veredicto: NO PASA

| | Sostenidos | Tope |
|---|---|---|
| Contrarios | 5 | 0 |
| Invenciones | 2 | 2 (declaradas como residuo) |
| Procedencias | 0 | 0 |

En 4 de 14 planes. Trampas 3 de 3 cazadas por los jueces (f002 invención, f010 contrario, f016 procedencia): la medición
vale. Evolución: M5 6 en 6 planes; M6 2 en 2 (con el comprobador encendido); M7 7 en 4.

Se para aquí sin arreglar. El arreglo de margen negativo no va a main.

## El arreglo de margen negativo funcionó

fb027af0, sección fija: «Punto de equilibrio: ... Todavía no aplica: primero hay que subir el precio o bajar el costo.»
Los gastos fijos «solo importan cuando el margen por unidad sea positivo». El contrario de la fila 26 no vuelve.

## Los siete sostenidos

| Plan | Clase | Afirmación | Por qué (árbitro) |
|---|---|---|---|
| b4a01dea (núcleo) | invención | «Elige tu pieza más vendida» | Supone varios modelos y un historial de ventas; dijo «un producto» y no dio ventas. |
| b4a01dea (núcleo) | contrario | «cuántas piezas salieron de tu última tanda» | «Tanda» supone lotes; ella fabrica una pieza a la vez. |
| 85248377 (salud y seguridad) | contrario | «Guarda los contactos y los pedidos fuera del celular, porque hoy no tienes copias de seguridad.» | Contradice una actividad del núcleo ya hecha (copia de los datos fuera del celular). |
| 85248377 (salud y seguridad) | contrario | «Pon clave al Excel de clientes» | Ya lo hizo: los datos están en un archivo con contraseña. |
| 85248377 (salud y seguridad) | invención | «Compra la mascarilla de polvo y los guantes que ya elegiste» | Eligió una de las dos opciones y no dijo cuál. |
| fb027af0 (núcleo) | contrario | «lo que pagas aunque no hagas ninguna (herramientas, moldes, otros gastos fijos)» | Ella contó los moldes dentro del costo de materiales por maceta; ningún tema los hace fijos. Ya salió en la fila 23 (f016). |
| deb138a3 (calidad) | contrario | «Anota qué resultado te bastaría para dar un lote por parejo» | Fijar un nivel «suficiente» es el nivel de calidad aceptable que el tema manda eliminar (tema aplicado al revés en un paso). |

## Lectura

- Tres de los siete son **premisas sobre la persona** en pasos y primeras acciones («tanda», «tu pieza más vendida», «los
  guantes que ya elegiste»). Citar o callar no los ve porque van en imperativo y los pasos no llevan marca de respaldo.
- Dos contradicen **actividades del núcleo ya hechas** en un plan de mundo (85248377). El redactor recibe esas
  actividades y aun así propone hacerlas, o afirma que faltan.
- **Los moldes como gasto fijo** reaparecen (fila 23 y ahora): una lectura de la persona contra lo que dijo.
- Un tema aplicado al revés en un paso (deb138a3), la categoría para la que se hizo el comprobador (apagado).
- La variación entre corridas es grande: M6 y M7 usan el mismo código salvo el margen negativo y el comprobador, y salen
  2 y 7. Con 14 planes por medición, el umbral de 0 contrarios queda a merced del sorteo de la redacción.

## Coste

| Parte | USD |
|---|---|
| Redacción de los 14 planes (tope 1,50) | 1,1075 |
| Dos jueces y árbitro, Opus 5.5 (tope 10), estimado | 6,8528 |
| **Total** | **7,9603** |

## Archivos

`A/` planes medidos, `costes.json`, `claves_A.json`, `veredictos_A/`, `redaccion.log`, `juez.log`.
