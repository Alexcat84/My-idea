Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. Ficheros del cribado solamente; docs/plan/ solo lectura.
MODO DE CIERRE: cero reparaciones.

====================================================================
TAREA 1: registros de la vuelta 1 del auditor
====================================================================
1. CHECKPOINT 2.600 AL INFORME. Apende a docs/INTRA_DOMINIO_INFORME.md la
   seccion "CHECKPOINT 2.600" compacta: marcador (A 522, B 89, C 7,
   D 1.982; 20,1 global), quality a 36,0 con su vara por tramo, familias
   del 9.3 con su especie, fusiones mutuas 13.a (2.575) y 14.a (2.597),
   la señal del idioma en cinco, y los commits f3c3750c (archivo) y
   5834d869 (reporte y correccion declarada). Cifras del reporte ya
   verificado por el auditor; no re-narres, remite a REPORTE.md en git.
   El acta del auditor (vuelta 1) adjudico esta continuidad: la fuente de
   checkpoints del informe no queda trunca en el 2.500.
2. LA PRECISION DE LA FECHA, donde vive la regla del corte (la tercera
   mitad del 11 ago: toda glosa lleva el corte). Una linea adjudicada por
   el auditor en el acta vuelta 1: EL ORDEN CANONICO ES EL CORTE, NO LA
   FECHA; lo transcrito conserva la fecha de su adjudicador; lo nuevo se
   firma con reloj real mas corte. Nada ya escrito se retoca.
3. LA TASA DE LA QUINTA CARA (9.28.1), medicion encargada con universo
   definido: sobre los nodos de los 2.600 pares leidos, barre
   titulo_concepto y node_id buscando siglas (dos o mas mayusculas
   seguidas) y terminos en otro idioma; revisa a mano los hits para
   separar denominacion real de falso positivo; publica cuantos PARES del
   archivo tienen denominacion en otro idioma en juego (ese es el
   universo) y la tasa de la señal (apariciones sobre universo). Anota la
   cifra en el 9.28.1 con su corte y el comando usado. Si el barrido no
   cabe en la sesion, dilo en el reporte y no lo dictes.

====================================================================
TAREA 2: CRIBADO CONTINUO hasta el checkpoint 2.700
====================================================================
Del 2601 al 2700 (python scripts/volcar_pares.py 2601 2606 para
retomar). La cola en orden y sin saltos. Manten el barrido de familia
antes de dictaminar cada par, como lo sistematizaste desde el 2.567: los
dictamenes citan a sus hermanos. Pendientes de familia que la cola traera
sola, no las adelantes: a capacidad y a seriedad les falta un par a cada
una para cerrar su cobertura.
Reporte completo EN el checkpoint, escrito en docs/loop/REPORTE.md:
marcador recomputado, tasa por dominio, vara por tramo, familias del 9.3
al dia con su especie de ganador, figuras al dia (fusiones mutuas, señal
del idioma, perdidas de nombre a reponer), y los discutibles marcados
ANTES de saber si aciertas, para la relectura ciega del auditor. Si la
sesion alcanza, sigue hacia el 2.800 con la misma regla. Los hallazgos
que no puedan esperar, al mensaje del commit.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
