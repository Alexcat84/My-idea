Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE
EJECUCION CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias
por operacion.

La decision del fundador que desbloquea esta vuelta esta en
docs/loop/paradas/2026-08-29-racha-y-escalada-omitida-DECISION.md:
OPCIONES (a) Y (b), LAS DOS. La escalada del 26 ago se ejecuta por fin
como operacion de codigo, y nace la regla del caso rojo probado por
mutacion, ya escrita en EJECUTOR.md regla 1 como EL CASO ROJO SE PRUEBA
POR MUTACION. En AUDITOR.md queda escrito ademas que al llegar la racha a
DOS el auditor ENCARGA la escalada en el mismo acta, que es lo que falto.
Sin cambio de modelos. La racha de reporte vuelve a CERO y OP-E-06 abre
con la bolsa V90.

- TAREA 1, los registros. Registrar las dos caidas de reporte de la
  vuelta 89 con su nombre y su medicion (acta 89, seccion 3), y la del
  auditor, la escalada automatica no encargada (acta 89, seccion 6 punto
  1). Registrar las siete adjudicaciones de la seccion 4 del acta 89,
  cada una por su numero.
- TAREA 2, la bolsa de OP-E-06 corregida, a fichero propio nuevo.
  docs/plan/OP_E_06_REBASE_V90.jsonl, partiendo de la V89 (117 filas, que
  NO se toca ni se borra), con las dos adjudicaciones aplicadas: entra el
  puesto 530 (estrategia_de_innovacion_de_producto ->
  estrategia_de_innovacion_y_tecnologia, adjudicacion 4.1) y sale el
  puesto 932 (cumplimiento_magnuson_moss ->
  mecanismo_resolucion_disputas, adjudicacion 4.2). Cifra esperada: 117
  filas, conjunto distinto. Si da otra cosa, paras y lo traes. Y el
  motivo del 581 y del 650 se anota en PENDIENTES como candidatos de una
  pasada posterior (adjudicacion 4.3): se caen por como quedo cosechada
  su frase, no por su contenido.
- TAREA 3, LA OPERACION DE CODIGO DE LA ESCALADA, Y ES BLOQUEANTE: va
  ANTES DE TOCAR OP-E-06, o sea antes de la TAREA 4. El fundador eligio
  (a) Y (b), asi que lleva las dos mitades.
  (3.a) LA ESCALADA, que es la que se decidio el 26 ago y quedo sin
  ejecutar: extender scripts/loop/tallar_cabecera_reporte.py (o un
  tallador hermano) para que TODA TABLA Y TODA CIFRA DEL REPORTE EN LAS
  FASES MECANICAS SE GENERE CONTANDO SU FICHERO DE SALIDA, no solo la
  cabecera. La vara de si alcanza: las DOS caidas de la vuelta 89 tienen
  que caer dentro de su alcance, porque la primera es una tabla de conteo
  de un fichero y la segunda es una afirmacion sobre una salida. Con su
  mecanica de ROJO igual que las filas ya talladas: si no puede contar el
  fichero, no talla nada y sale con exit 1, jamas inventa una cifra.
  (3.b) EL CASO ROJO PROBADO POR MUTACION, que es la regla nueva
  estrenandose sobre si misma: el caso rojo del instrumento de (3.a) no
  se publica sin correr antes su prueba de mutacion, cambiando el valor
  esperado y comprobando que CAE, con esa corrida citada en el reporte. Y
  la mutacion se hace sobre una variable QUE EL CODIGO COMPUTE, no sobre
  una constante literal: un assert que compara un literal consigo mismo
  no es un caso rojo. Si alguna parte de la clasificacion es una tabla a
  mano y no hay nada que mutar, se declara que ahi NO HAY CASO ROJO
  AUTOMATICO en vez de fabricar uno que se aprueba solo.
- TAREA 4, abrir OP-E-06 con la bolsa V90, la via de OP-C-05 cableada
  (--antes y --despues con su sello propio de la vuelta), y la semantica
  canonica de resolverId para la escritura (la de
  aristas_duplicadas_tras_resolver.py, que camina la cadena entera).
- Con el freno delante: la racha de reporte vuelve a cero al relanzar,
  pero la regla de las tres seguidas sigue viva; y la de clase o cifra
  publicada esta en CERO, no en una.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
