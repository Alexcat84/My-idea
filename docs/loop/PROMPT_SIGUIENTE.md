Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. Ficheros del cribado solamente; docs/plan/ solo lectura.
MODO DE CIERRE: cero reparaciones.

AVISO DE CREDITO, leelo primero. Tu tanda anterior (2.901 a 2.925) tuvo
UNA DISCREPANCIA FUERA DE LOS DISCUTIBLES MARCADOS (el 2.916). Por la
regla del credito, el tramo se relee AL DOBLE y eso es la TAREA 1. Una
segunda tanda seguida con discrepancia fuera del marcado DETIENE EL
BUCLE (AUDITOR.md 4). No es un castigo: es la vara. La salida es marcar
mejor, no dictaminar menos.

Tu sesion anterior murio por fallo de API (Connection lost) tras
commitear el 2.925. No perdiste nada: el arbol quedo limpio y empujado.
Commitea por tramos de 25 como venias haciendo, para que un corte no se
lleve trabajo.

====================================================================
TAREA 1: registros de la vuelta 5 del auditor
====================================================================
1. RELECTURA CONJUNTA DE LA GRIETA consejo de calidad (2.916). Tu
   dictaminaste A por transitividad, afirmando que las cuatro fusiones
   previas eran de GEMELOS "por identidad, no por contencion". El caso
   del auditor, en corto: el archivo dice lo contrario con sus propias
   palabras en dos de los cuatro eslabones. El 2.523 (consejo_calidad
   =A= consejo_de_calidad_3) escribe "sus pasos 1 y 2 estan en el otro
   [...] lo que le queda propio son DOS LINEAS" y registra PERDIDA
   NOMBRADA, motivo DESTINO, que es la firma de una absorcion
   asimetrica y no de una identidad; y el 2.662 (consejo_calidad_2 =A=
   consejo_de_calidad_3) escribe "consejo_de_calidad_3 es el mas simple
   [...] y VA DENTRO DE consejo_calidad_2", y ese mismo 2.662 se
   resolvio a su vez por transitividad. Con un eslabon de contencion
   declarado, la cadena no compone. Ademas la lectura directa apunta al
   mismo lado: el 2.523 nombra lo propio de consejo_de_calidad_3
   (coordinar la repeticion del ciclo, institucionalizar como
   estructura permanente) y el 2.663 y el 2.670 nombran lo propio de
   consejo_de_calidad (capacitarse en el metodo, priorizar con Pareto,
   asignar recursos, "lineas a reponer"): conjuntos disjuntos, ninguno
   cabe entero en el otro. Y el 2.549 ya corta dentro de esta familia
   (consejo_de_calidad =D= consejo_de_calidad_y_rol_del_director).
   Verifica contra el grafo (nodos enteros, no titulos) y decide con la
   vara del paso entero:
   a) Si corriges 2.916 a D: correccion declarada con su comando y
      recomputo completo (marcador A 574 a 573 y D 2.255 a 2.256 al
      corte 2.925, tramo 2.901-2.925 de 2 A a 1 A, tasa de quality),
      tachado sin borrar en la razon del 2.916 (la vieja se conserva
      entera, la correccion se agrega al final) y la cifra corregida
      arrastrada al checkpoint 3.000 que escribas.
   b) Si sostienes A: escribe en la razon por que el eslabon 2.523,
      que declara perdida nombrada por DESTINO, compone identidad y no
      absorcion; y por que el 2.549 puede cortar dentro de la misma
      familia sin romper el cumulo.
   Cualquiera de las dos salidas usa reglas existentes. Si al bajar al
   grafo ninguna alcanza, PARAS y lo traes.
2. REGLA ADJUDICADA, vigente desde ya (acta vuelta 5, extension citable
   de la correccion del 2.805, informe 95.3.1). LA TRANSITIVIDAD
   COMPONE CUANDO LOS ESLABONES SON IDENTIDADES (gemelos); NO COMPONE
   CUANDO ALGUNO DE LOS ESLABONES ES UNA CONTENCION, VAYA EN LA
   DIRECCION QUE VAYA. Las dos formas fallan por la misma asimetria:
   que A contenga a g y B contenga a g no da A = B (el caso 2.805), y
   que A quepa en H y B quepa en H tampoco da A = B (el caso 2.916).
   Antes de invocar transitividad, ve a leer la razon de CADA eslabon
   que citas y comprueba que ninguno hable de "cabe en", "va dentro
   de", "lo que le queda propio" o PERDIDA NOMBRADA. Si alguno lo hace,
   la cadena no sirve y el par se lee directo con la vara del paso
   entero.
3. RELECTURA AL DOBLE DEL TRAMO 2.901 A 2.925, por el credito roto.
   Vuelve a leer los 25 pares con el barrido de familia, sin mirar tu
   razon anterior hasta haber adjudicado de nuevo. Foco en las A y en
   toda cadena de transitividad. Al terminar, declara en el commit:
   cuantos sostienes, cuantos cambias, y las correcciones declaradas de
   los que cambien (con recomputo). Si los 25 se sostienen (salvo lo
   que decida la TAREA 1.1), dilo con esa misma claridad.
4. MARCADO DE DISCUTIBLES, precision del acta. El tramo llevo 5 marcas
   en 25 pares; la tanda anterior llevaba marca inline en los 100. El
   marcado del archivo es lo que cuenta para el credito, asi que marca
   de menos es marcar mal. Regla operativa: TODA A lleva marca (es una
   afirmacion falsable de duplicado), y toda D que anule una lectura A
   defendible tambien. Caso concreto que se te paso: el 2.922
   (control_estadistico_del_proceso contra control_estadistico_proceso),
   ids casi identicos y arranque compartido entero, no lleva marca. La
   clase D esta bien y ademas cierra por una transitividad que no
   citaste y el auditor si verifico (2.529 del_proceso =A=
   no_implica_cero_defectos, y 2.633 ese mismo nodo =D= proceso):
   agrega la marca y la cita, sin cambiar la clase.
5. LO VERIFICADO Y EN VERDE, para que no lo toques: la correccion del
   2.805 esta completa y bien hecha (jsonl con tachado sin borrar,
   informe 95.1, 95.2 y la nueva 95.3.1), sus cifras al corte 2.900
   recomputadas por el auditor calzan exacto (A 572, D 2.232, quality
   489/118/24,1 %, tramo 9 A, 2.801-2.825 3 A), y tus 34 citas de
   familia se verificaron una por una contra el archivo sin una sola
   inventada. scripts/recomputar_marcador.py quedo aprobado como
   auxiliar de solo lectura: usalo y declara su comando.
6. NADA MAS DE REGISTRO: el contador de mutuas sigue en DIECIOCHO (el
   tramo 2.901-2.925 no abrio numero: el 2.917 es contencion y el 2.916
   esta en relectura conjunta). La pregunta del Consejo de Calidad NO
   se cierra hasta que la TAREA 1.1 resuelva; la de la responsabilidad
   gerencial sigue abierta (el 2.906 repitio la frontera del 2.850 y el
   2.881). No las adelantes.

====================================================================
TAREA 2: CRIBADO CONTINUO hasta el checkpoint 3.000
====================================================================
Del 2.926 al 3.000 (python scripts/volcar_pares.py 2926 2931 para
retomar). La cola en orden y sin saltos. Manten el barrido de familia
antes de dictaminar cada par, con la regla de la transitividad de la
TAREA 1.2 puesta delante. Commitea cada 25 para no perder trabajo si la
sesion se corta.
Reporte completo EN el checkpoint, escrito en docs/loop/REPORTE.md (que
sigue siendo el de la vuelta 4, corte 2.900: lo reescribes entero):
marcador recomputado (con el efecto de la TAREA 1 si corrigio), tasa por
dominio, vara por tramo, familias del 9.3 al dia con su especie de
ganador, figuras al dia (fusiones mutuas, senal del idioma, perdidas de
nombre a reponer), el resultado de la relectura al doble del tramo
2.901-2.925, y los discutibles marcados ANTES de saber si aciertas, para
la relectura ciega del auditor. Checkpoint compacto tambien al informe
(seccion 96), como el 95.
El checkpoint 3.000 cubre 2.901 a 3.000, incluidos los 25 ya criados.
Si la sesion alcanza, sigue hacia el 3.100 con la misma regla.
Faltan 463 pares hasta el 3.388: quality 330 (hasta el 3.255),
risk_management 106 y seguridad_digital 27.
Los hallazgos que no puedan esperar, al mensaje del commit.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
