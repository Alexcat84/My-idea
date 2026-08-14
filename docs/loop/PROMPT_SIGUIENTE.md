Commitea y pushea lo pendiente en la rama activa antes de tocar nada.
SESION EJECUTORA. FASE II, RECOMPUTO, vuelta 15. MODO DE CIERRE: cero
reparaciones de nodos. La FASE III no se abre y `pasada-unica` no se crea.

TU VUELTA 14 VERIFICO AL CIEN POR CIEN. Remedi las tres correcciones con
instrumento propio y ademas reconstrui el corte 2.117 entero: tu metodo de
OP-L-03 reproduce el 29 y el 55 publicados con su reparto exacto. La racha de
caidas de reporte queda cortada. La unica caida de esta vuelta es MIA y la
arreglas tu en la TAREA 1, punto 2.

====================================================================
TAREA 1: registro y tres correcciones
====================================================================
Lee antes de tocar nada: docs/loop/ACTA_AUDITOR.md, seccion VUELTA 14,
apartados 2, 4, 5 y 6.

1. OP-L-03 QUEDA ADJUDICADO EN CUARENTA ACTOS Y SETENTA Y TRES PARES.
   Tu discutible 1 se cierra a favor de la lectura literal, y no por
   preferencia: reconstrui el corte 2.117 con recomputo_3388.py sobre el
   blob viejo y tu metodo devuelve 29 actos y 55 pares, el reparto exacto
   de la nota, y LOS MISMOS CUATRO ACTOS en disputa ya estaban dentro de
   aquel 55. El criterio ancho habria dado 25 y 51, que contradice el
   banco. Registra la adjudicacion en la nota de OP-L-03 (se AGREGA, no se
   borra el discutible) y con tachado en docs/plan/RECOMPUTO_3388.md.

2. LA COBERTURA DEL RACIMO DE LA SUPERVISION DE LA IA ESTA MAL Y EL ERROR
   ES MIO, no tuyo: la frase "10 de 45 ... los 35 restantes siguen sin
   leerse" la bendije yo en el acta de la vuelta 13 y tu la copiaste a
   docs/plan/RECOMPUTO_3388.md. REMIDELA TU, no copies mi cifra: nomina de
   diez de INTRA_DOMINIO_INFORME.md secciones 11.bis.1 y 11.bis.3 (bloque
   humano 5, bloque del mapa 4, suelto 1), cuenta cuantos de los 45 pares
   estan en INTRA_DOMINIO_VEREDICTOS.jsonl y suma las lecturas dirigidas
   del bloque humano que viven fuera de cola. Escribe la cifra que te
   salga, con tachado sobre la vieja y sin borrarla, y con su corte.
   Y arrastra las cifras publicadas que dependen de ella, cada una con su
   corte nuevo y sin borrar el viejo (banco 9.21 y 9.26):
   - la nota de OP-F-02 en OPERACIONES.jsonl ("cobertura 14 de 45 pares"
     al puesto 1.517),
   - la entrada de tipo racimo "la supervision de la IA" en
     docs/plan/INVENTARIO.jsonl, que ademas lista OCHO miembros cuando la
     nomina vigente es de DIEZ,
   - docs/plan/10_INVENTARIO.md, la fila de ese racimo.

3. LA ETIQUETA "PENDIENTE DE DOCTRINA" DE OP-I-01 SE CORRIGE. El acta de
   la vuelta 13, adjudicacion 6.4, ya dice lo contrario: no es doctrina,
   es un encargo propio de recomputo. Corrigela en la nota de OP-I-01 y en
   RECOMPUTO_3388.md, con tachado y sin borrar. No cuenta como caida: es
   etiqueta, no medicion.

====================================================================
TAREA 2: el recomputo del inventario de OP-I-01 al corte 3.388
====================================================================
La regla que gobierna esta tarea es la de la FASE II: ninguna cifra
publicada queda sin recomputar con su corte nuevo.

1. MIDE PRIMERO EL ARCHIVO VIVO, no la nota. docs/plan/INVENTARIO.jsonl
   tiene hoy mas entradas de las que la nota de OP-I-01 declara: la nota
   dice 323 entradas con 14 defectos y 12 figuras. Cuenta tu el archivo
   por campo `tipo` y publica lo que te salga. La nota esta desfasada por
   DOS vias a la vez, por el corte y por el propio archivo, y las dos hay
   que decirlas.

2. RECOMPUTA CADA SUMANDO AL CORTE 3.388, cada uno con su instrumento
   nombrado y su cifra vieja al lado sin borrar:
   a. dominios: los diez, con sus pares leidos y su tasa de A al 3.388,
      contados de INTRA_DOMINIO_VEREDICTOS.jsonl.
   b. actos: los 335 de RECOMPUTO_3388_COMPONENTES.jsonl, con su reparto
      CERRADOS y ABIERTOS. Esta ya la mediste en la vuelta 14; solo
      citala con su corte.
   c. racimos: los trece, cada uno con su nomina y su cobertura remedida
      (banco 9.26, la forma se escribe con su cobertura al lado).
      Empieza por la supervision de la IA, que ya remides en la TAREA 1.
   d. familias de ids, figuras y defectos: para cada grupo di primero
      CUALES de sus cifras dependen del corte del cribado y cuales no.
      Remide las que dependan. Las que no dependan, declaralas con su
      motivo escrito, no las midas por cumplir.

3. PUBLICA EL TOTAL NUEVO con su fecha de corte, y deja escritas al lado
   las dos cifras viejas (323 de la nota y la que cuentes hoy del
   archivo). Si algun sumando queda sin remedir, el total se publica
   igual pero DICIENDO cual de sus partes no se midio: nada de sumas
   mezcladas sin avisar, que eso ya lo hiciste bien en la vuelta 14.

4. NO REGENERES LAS 221 ENTRADAS DE TIPO ACTO. Reescribir 335 lineas de
   un documento que otros citan es alcance, y el alcance se trae antes de
   gastarlo. Escribe el PLAN de esa regeneracion como discutible marcado:
   que campos llevaria cada entrada, de que instrumento salen, cuantas
   lineas se escriben y se borran, que citas de otros documentos se
   romperian, y cuanto cuesta. Yo lo adjudico en la vuelta siguiente.

5. Todo lo escrito va en una seccion nueva AL FINAL de
   docs/plan/RECOMPUTO_3388.md, sin reescribir nada anterior, mas la nota
   de OP-I-01 puesta al dia.

====================================================================
VERIFICACIONES FIJAS
====================================================================
- Toda declaracion de que algo falta, no existe o no esta leido se
  comprueba contra el archivo que acabas de citar, antes de escribirla.
- NUEVA, y nace de mi propia caida de esta vuelta (banco 9.10, toda tabla
  que cita un veredicto se recomputa del archivo): TODA CIFRA DE
  COBERTURA O DE CONTEO QUE COPIES DE UN ACTA, DE UN ENCARGO O DE UNA
  NOTA VIEJA SE REMIDE CONTRA EL ARCHIVO ANTES DE ESCRIBIRLA, AUNQUE TE
  LA BAJE EL AUDITOR. Una adjudicacion se obedece; una cifra se remide.
- dataset/ no se toca ni un byte. No se ejecuta ninguna operacion. No se
  crea la rama pasada-unica. No se crean operaciones nuevas.
- Marca tus discutibles al final del reporte, como siempre: son lo
  primero que releo.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
