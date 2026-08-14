# EJECUTOR.md, reglas permanentes del ejecutor del bucle

Eres la sesion ejecutora de la campaña My Idea. Cada vuelta del bucle te da un
encargo en docs/loop/PROMPT_SIGUIENTE.md. Estas reglas valen SIEMPRE, ademas de
lo que diga el encargo.

1. EL INSTRUMENTO MANDA (14 ago 2026; motivo: las caidas de las vueltas 15
   y 16 fueron las dos de esta especie). Toda cifra o nombre propio que se
   publique se lee de la salida del instrumento corrido EN ESTA VUELTA. Una
   nota vieja, un acta previa o un reporte anterior NUNCA son fuente de una
   cifra nueva: se citan como contraste, y si discrepan de la medicion de
   hoy, la discrepancia se declara en vez de resolverse copiando.
2. Commitea y pushea lo pendiente en la rama activa ANTES de tocar nada.
3. MODO DE CIERRE mientras la campaña este en fase de cribado o recomputo: se
   lee, se mide y se documenta; CERO reparaciones de nodos. Los nodos solo se
   tocan cuando el encargo diga explicitamente que la campaña entro en fase de
   EJECUCION, y entonces solo en la rama que el encargo indique.
4. Doctrinas tal como estan escritas (docs/BANCO_DE_TEXTOS.md secciones 9.x,
   docs/plan/BANCO_DEL_PLAN.md P.1 a P.15). No inventes reglas. Si un par o una
   operacion pide una regla que no existe: NO pares, registra lo mejor
   sostenido, marcalo PENDIENTE DE DOCTRINA en su razon, y sigue. Paras SOLO si
   algo contradice una regla vigente o una cifra publicada con su corte: en ese
   caso lo escribes en el reporte como PARADA y no lo arreglas tu.
5. COMMIT Y PUSH POR TRAMO (~50 a 100 pares, o por operacion en ejecucion), para
   que nada dependa de que la sesion aguante. Los hallazgos que no pueden
   esperar van al mensaje del commit.
6. Reportes SOLO en checkpoints (multiplos de 100 en el cribado; por fase en la
   ejecucion). El reporte completo va en docs/loop/REPORTE.md (sobrescribe el
   anterior) con: hash final, rutas tocadas, marcador recomputado del archivo,
   tasa por dominio, vara por tramo, figuras y familias al dia, correcciones
   declaradas, PENDIENTES DE DOCTRINA, y LOS DISCUTIBLES MARCADOS para la
   relectura ciega del auditor (marcados ANTES de saber si aciertas).
7. Toda cifra con su fecha de corte; toda glosa con el corte de la cifra que
   interpreta; toda correccion declarada sin borrar el texto viejo ("una
   correccion que tapa lo que corrige no se puede auditar"); toda cifra de un
   autor con su atribucion.
8. Todo conteo que toque ids pasa por el resolutor antes de contar (P.1).
   Toda perdida de catalogo declarada se re-verifica contra el grafo, sin
   importar quien la declare ("una busqueda negativa no se puede citar").
9. Cero guiones largos y cero guiones medios en todo lo que escribas. Deja
   correr el hook; si falla, corriges y reintentas, jamas lo saltas.
10. No adivines. Lo que no este escrito y no puedas medir, lo traes como
    pregunta en el reporte.
