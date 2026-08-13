Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. Ficheros del cribado solamente; docs/plan/ solo lectura.
MODO DE CIERRE: cero reparaciones.

====================================================================
TAREA 1: registros de la vuelta 2 del auditor
====================================================================
1. EL UNIVERSO LIMPIO DE LA QUINTA CARA (9.28.1), medicion adjudicada
   por el auditor (acta vuelta 2) por extension del 9.28: procede como
   medicion, no doctrina nueva. Extiende scripts/barrido_quinta_cara.py
   (o haz un hermano de solo lectura) para barrer TAMBIEN el cuerpo del
   nodo (resumen_teorico y pasos_accionables), restringido a los
   dominios de nombre largo en castellano (fuera core, ingles por
   diseño). Universo: pares leidos de esos dominios con denominacion
   foranea en titulo, id o cuerpo. Revision a mano de los hits para
   separar denominacion real de falso positivo (el COC deletreado del
   2.593 muestra que la lista curada no basta sola). Publica en el
   9.28.1 la cota nueva (apariciones sobre universo) con su corte y su
   comando. Si el barrido no cabe en la sesion, dilo en el reporte y no
   lo dictes.
2. LA PRECISION DE LA CAPACIDAD, una linea en el checkpoint 2.800 del
   informe: contada por raiz la familia lleva 8 pares, los 8 D (el
   2.423, establecer contra establecimiento, tambien junta dos nodos de
   la raiz); el 7 de 7 del checkpoint 2.700 contaba la cobertura
   completa del nucleo de cuatro nodos, 6 pares, mas el 2.697. SIN ACTO
   se sostiene sobre los 8. Nada ya escrito se retoca.

====================================================================
TAREA 2: CRIBADO CONTINUO hasta el checkpoint 2.800
====================================================================
Del 2701 al 2800 (python scripts/volcar_pares.py 2701 2706 para
retomar). La cola en orden y sin saltos. Manten el barrido de familia
antes de dictaminar cada par, como lo sistematizaste desde el 2.567:
los dictamenes citan a sus hermanos. Pendientes que la cola traera
sola, no los adelantes: los pares que falten del cumulo del Consejo de
Calidad (su especie queda POR ELEGIR provisional hasta cerrar la
cobertura, adjudicado en el acta vuelta 2) y el sub-cumulo de la
responsabilidad gerencial que sigue abierto.
Reporte completo EN el checkpoint, escrito en docs/loop/REPORTE.md:
marcador recomputado, tasa por dominio, vara por tramo, familias del
9.3 al dia con su especie de ganador, figuras al dia (fusiones mutuas,
señal del idioma, perdidas de nombre a reponer), y los discutibles
marcados ANTES de saber si aciertas, para la relectura ciega del
auditor. Si la sesion alcanza, sigue hacia el 2.900 con la misma regla.
Los hallazgos que no puedan esperar, al mensaje del commit.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
