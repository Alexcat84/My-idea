Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE II, RECOMPUTO. MODO DE CIERRE: cero reparaciones de
nodos.

====================================================================
TAREA 1: los cinco puntos de la seccion 5 de la parada archivada
(docs/loop/paradas/2026-08-14-credito-vuelta-16.md), en este orden
====================================================================
1. Corrige la caida con tachado y sin borrar, en
   docs/plan/RECOMPUTO_3388.md linea 1042 y en docs/loop/REPORTE.md: el
   que crecio es gestion_terminacion_franquiciado, de 2 a 3, y remidelo
   con instrumento propio, no copies la cifra del acta. En el tachado
   queda escrito que la caida es del ejecutor y que la fuente correcta
   ya estaba en la nota de OP-U-02.
2. Marca las 221 lineas viejas como superadas por el corte 3.388, cada
   una con el puntero a su sucesora (adjudicacion del discutible 1). La
   lectura aditiva del ejecutor queda, pero hoy esta a medias:
   10_INVENTARIO.md linea 311 manda al lector a esas entradas como LA
   fuente para contestar "si un nodo repite", y hoy contesta dos veces
   con dos nominas y dos cortes.
3. Pon el aviso con tachado en docs/plan/10_INVENTARIO.md (adjudicacion
   del discutible 3): sigue declarando acto 221, TOTAL 336 y corte
   2.117, y su linea 313 dice "todo el inventario es del 11 ago 2026",
   que ya es falso para el archivo al que ella misma manda. No se
   regenera la tabla entera (eso es el disparador de 08_VERIFICACION);
   se le pone el aviso.
4. Registra el hueco nombrado del discutible 2 en la entrada de OP-I-01:
   el campo operaciones de las 335 hereda lo que el campo nodos de las
   operaciones viejas tenga incompleto, y auditarlo operacion por
   operacion es trabajo de la FASE III.
5. Sigue la FASE II por donde estaba: los ejemplares de las veinte
   figuras, el lote de cinco del sales roadmap, la cola de relectura
   post fusion, el criterio del forastero y las lecturas de acto entero
   de P.5.

====================================================================
TAREA 2: DECISION DEL FUNDADOR sobre las dos costuras sin dueño
====================================================================
lienzo_modelo_negocio y planificacion_recoleccion_datos RECIBEN DUEÑO.
Antes estaban declaradas sin operacion propia (docs/plan/RECOMPUTO_3388.md,
seccion 4: "las 31 son costuras confirmadas SIN gemelo vigente" y la
"lista declarada de las DOS que ademas no tienen dueno en ninguna
operacion del plan"; docs/plan/CONTROL_MUESTRA_D.md linea 120 anota que
lienzo_modelo_negocio es una costura de DIECISIETE pasos). Esa
adjudicacion queda revertida hoy por decision del fundador.

Escribe para cada una su operacion de destejido en
docs/plan/OPERACIONES.jsonl, con el paquete estandar del plan: nomina,
superviviente o reparto del bloque (que se preserva), simulacion, caso
positivo, orden y dependencias dentro de la fase que le corresponda.
Usa la evidencia que el frente de costuras ya midio (docs/plan/
RECOMPUTO_3388.md seccion 4 y lo que CONTROL_MUESTRA_D.md ya registro
sobre lienzo_modelo_negocio); no releas los nodos de cero si la
evidencia ya esta escrita. El plan pasa de 69 a 71 operaciones.

VALVULA: si al escribir alguna de las dos exige lecturas nuevas amplias
o una decision no medida, esa operacion NO se fuerza: vuelve a
docs/PENDIENTES.md con la razon escrita, y el plan se queda en 70 o en
69, declarandolo en el reporte.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
