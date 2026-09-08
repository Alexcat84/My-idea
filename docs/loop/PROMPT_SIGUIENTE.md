Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

Eres el ejecutor de la VUELTA 208. Rama `pasada-unica`, FASE III. Lee
`docs/loop/EJECUTOR.md` entero antes del primer comando y abre tu reporte con la
vuelta: talla el esqueleto de `docs/loop/REPORTE.md` ANTES de la primera tarea,
con las CUATRO marcas del anexo puestas (`<!-- TABLA DE TAREAS -->`,
`<!-- ANEXO DE TAREAS -->` y sus dos cierres), que es la `C.1` que la 207 tuvo
que remendar a mano. Mira que exige `anexar_tarea_al_reporte.py` ANTES de tallar,
no despues.

TRES SUB-TAREAS. El tope volvio a CINCO (mi acta 207, adjudicacion `6.5`: la 206
y la 207 cerraron las dos su propio reporte con `cerrar_reporte.py`, que es el
disparador de `AUDITOR.md` 6.2), pero te pongo tres y no cinco porque la TAREA 2
toca una sede sellada del banco y prefiero que sobre guarda a que sobre trabajo.

LA BATERIA NO CORRE EN ESTA VUELTA (`AUDITOR.md` 6.1, mi adjudicacion `6.7`): la
ultima fue la 205 y la siguiente es la 210. Tu seccion 9 cierra con el HUECO
DECLARADO Y MEDIDO y sus TRES piezas juntas, distinguiendo el cero de ausencia
del cero de fichero vacio.

RIGE LA MORATORIA DE MAQUINARIA (`AUDITOR.md` 6.3). Ningun arnes, guarda ni
lector nuevo. Todo tu computo va con prefijo `_v208_*`, fuera del censo y fuera
de la nomina, que sigue CONGELADA EN 135 y que recomputé yo con `ast` en esta
vuelta. Si un lector heredado no te alcanza, LO DECLARAS NO COMPUTABLE con su
motivo medido y sigues: no lo ensanchas.

---

## TAREA 1. LOS REGISTROS DE LA VUELTA 207

1.a. Lee entera mi acta de la vuelta 207 en `docs/loop/ACTA_AUDITOR.md` y REMIDE
     sus cifras de crecimiento con tus comandos. CONTRASTE, para que lo cotejes y
     NO para que lo copies: el acta pasa de 4793964 a 4820516 bytes en disco y a
     4820516 normalizado a LF, o sea 26552 anadidos, con sha256 disco
     `0ca61c2ee053dd0d` y sha256 LF `0ca61c2ee053dd0d`, y 73081 lineas. Mi
     seccion empieza en la linea 72641. Si tu medicion discrepa, DECLARAS la
     discrepancia; no la resuelves copiando.
     AVISO MEDIDO, que a la 207 le costo una caida: `git show 3e523b74^:...` se
     come el acento circunflejo en algunos shells y te devuelve el commit sin el
     padre. Usa `~1` o comprueba que los dos valores son distintos antes de
     restar.

1.b. Escribe `R.72` en `docs/PENDIENTES.md` POR ADICION PURA Y EN SU SEDE. El
     numero NO se teclea: lo computa `scripts/loop/serie_de_registros.py`,
     corrido por ti AL ENTRAR y AL SALIR, y publicas las dos puntas.
     CONTRASTE de la punta de entrada, medido por mi hoy: 63 entradas en total
     (62 en `docs/PENDIENTES.md` y 1 en `docs/plan/CORRECCIONES_A_APLICAR.md`),
     0 colisiones, 0 huecos, mayor `R.71`, siguiente libre `R.72`.
     Publica `git diff --numstat` sobre la sede con sus lineas anadidas y
     BORRADAS, y la cuenta de lineas del texto de entrada que no esten, en orden,
     en el de salida. Corre la segunda vez y publica que crece 0 bytes.

1.c. Registra POR SU NUMERO las OCHO adjudicaciones de mi acta, `6.1` a `6.8`,
     cada una con su linea. Y esta vez la vara del `4.1` del acta 202 SI te va a
     computar: escribi mi acta con los titulos que esa vara ya buscaba y con cada
     clave de la casa llevando su `N.M` al lado. Mi prueba, corrida con el lector
     IMPORTADO y sin tocarle una linea, esta en
     `docs/loop/SALIDA_V207_VARA_SOBRE_MI_ACTA.txt`: da 4 de 4 numerales sobre el
     acta 207 contra 1 de 4 sobre la 206. CORRELA TU y publica lo que te dé. Si
     te da otra cosa, esa discrepancia es un hallazgo y va a tu 3.0.
     Las cinco adjudicaciones que CIERRAN pendientes son la `6.1` (tu `P.2`), la
     `6.3` (tu `P.3`), la `6.4` (tu `PD.1`), la `6.5` (el tope) y la `6.8` (tu
     `P.1`). Dilo al registrarlas.

1.d. CORRIGE MI CAIDA `4.1` CONTRA TI, en el reporte que archives de la 207, por
     CORRECCION DECLARADA y con el texto viejo entero encima. Tu seccion `2.a`
     publica "6 de `verificacion`" y son SIETE. No la corrijas copiandome:
     REMIDELA tu sobre la linea 41 de `docs/plan/OPERACIONES.jsonl`, y cita al
     lado la linea 21 de tu propia salida sellada
     `docs/loop/SALIDA_V207_T2_VARA.txt`, que ya imprimia
     `CIFRA elementos de verificacion: 7`. Deja escrito que la cobertura NO
     cambia: `V.12`, `V.13` y `V.14` salen de `verificacion[0]`, `[1]` y `[2]`, y
     los cuatro elementos no contados son las CORRECCIONES DECLARADAS, que nunca
     fueron puntos de la vara.

---

## TAREA 2. LA `TABLA VIVA DE LOS PUROS`, PUESTA AL DIA POR EL CARRIL DEL `9.10`

ESTO ES LO QUE MI ADJUDICACION `6.3` ENCARGA, Y SALE DE LA `6.1`: el criterio de
HECHO de la fase `06 MESAS` en `docs/plan/08_VERIFICACION.md` exige "cada
decision escrita con su motivo y su COBERTURA AL LADO (banco 9.26)", el banco
`9.26` dice que mientras falte un par la forma es PROVISIONAL, y la propia
`verificacion[2]` de `OP-L-01` pide que "cada nomina afectada se re-mide con su
cobertura al lado". La tabla no lo lleva, y por eso `OP-L-01` no cierra.

2.a. PRIMERO EL DENOMINADOR, Y ESTE ORDEN NO ES DE ADORNO. Recomputa cuantos
     pares POSIBLES tiene cada una de las dos nominas, de su nomina de miembros y
     no de la tabla. MOTIVO MEDIDO, y es mi hallazgo `7.2`: en la junta asesora
     las dos fuentes dicen 6 posibles y solo discrepan en los leidos, o sea que
     es la tabla sin refrescar; pero en la SELECCION DE CANAL la mesa cuenta
     10 de 10 y la tabla 8 de 15, y ahi los DENOMINADORES no coinciden. Escribir
     los leidos sobre un denominador sin comprobar seria arreglar la mitad
     visible. Publica los dos denominadores con el comando que los saca.

2.b. ESCRIBE LAS DOS FILAS en `docs/BANCO_DE_TEXTOS.md`, por el carril del banco
     `9.10` (toda tabla que cita un veredicto se recomputa del archivo), con
     CORRECCION DECLARADA, con el texto viejo entero encima, sin tacharlo y sin
     clave nueva de esquema. Las sedes, medidas por mi hoy: la tabla abre en la
     linea 938 con corte 14 ago 2026 al puesto 1157; la junta asesora es la fila
     de la linea 961 y dice 5 leidos de 6 posibles; la seleccion de canal es la
     de la linea 965 y dice 8 de 15. Lo que la mesa declara esta en
     `docs/plan/LECTURAS_DIRIGIDAS.md:290` y `:291`, con "cobertura COMPLETA" las
     dos. REMIDE las cuatro sedes antes de escribir.
     El corte de la tabla se actualiza tambien: hoy dice 14 ago 2026 y la
     correccion es posterior.

2.c. PUBLICA `docs/BANCO_DE_TEXTOS.md` por las DOS convenciones, antes y despues,
     con sus `sha256`. CONTRASTE de hoy: 182228 bytes en disco y 182228
     normalizado a LF, sha256 disco `68557cd00a3124f4` y sha256 LF
     `68557cd00a3124f4`. Y publica `git diff --numstat` con las lineas anadidas y
     las BORRADAS: si borras una sola linea de texto viejo, es rojo.

2.d. NO CIERRES `OP-L-01` Y NO TOQUES SU CAMPO `estado`. Cerrar una ficha es
     adjudicacion mia. Lo que si haces es dejar MEDIDO si con las dos filas
     escritas la `V.3` pasa de `A MEDIAS` a `CUBRE`, con su cita de fichero y
     linea, para que yo la cierre en la 209 sin volver a medir.
     `docs/plan/OPERACIONES.jsonl` tiene que salir de esta vuelta con el MISMO
     `sha256` con el que entra: 513043 bytes por las dos convenciones y
     `829c583eb779cab6`. Publicalo al cierre.

2.e. Y LA `V.14` VA CORREGIDA POR ADICION, NO REHECHA (mi adjudicacion `6.4`).
     Se sello como NO DOCUMENTAL "porque las nominas del inventario no viven en
     ninguno de los tres documentos", y la cobertura de esas nominas vive en la
     `TABLA VIVA DE LOS PUROS`, que esta en `BANCO_DE_TEXTOS.md`, que es uno de
     los tres. Es la misma especie que tu `D.2` con la `V.4`: se declara al lado,
     con las dos cuentas juntas, y el sello NO se reescribe.

---

## TAREA 3. LA MESA `OP-L-03`, MEDIDA CONTRA LOS DOCUMENTOS QUE SU FICHA NOMBRA

MISMO METODO QUE LA `OP-L-01` DE LA 207, QUE SALIO BIEN Y POR ESO SE REPITE.

3.a. LA VARA PRIMERO, SELLADA EN SU PROPIO COMMIT ANTES DE ABRIR NINGUN
     DOCUMENTO, con cada punto llevando la CITA LITERAL del campo y del elemento
     de la ficha del que sale, y con el computo comprobando VERBATIM que cada
     cita aparece en la ficha. Sella tambien EL REPARTO: cuales son documentales
     y cuales no, con su motivo escrito ANTES de mirar.
     ESCARMIENTO DE LA 207, PARA QUE NO SE REPITA: alli DOS puntos se sellaron
     como no documentales y resultaron tener sede (`V.4` y, cazada por mi, la
     `V.14`). Antes de declarar un punto NO DOCUMENTAL, comprueba que su sede no
     esta en ninguno de los documentos de la evidencia.

3.b. EL COTEJO, punto por punto, con CUBRE, A MEDIAS o NO CUBRE y su cita de
     FICHERO Y LINEA. Una fila sin cita no vale. Y aplica la `6.1`: si un punto
     nombra una nomina o una forma de familia, la cobertura tiene que estar al
     lado en su sede, o no cubre.
     Los documentos que la ficha nombra, medidos por mi hoy con la vara del
     trabajo pendiente (`scripts/loop/vuelta150_3_relectura_expediente.py
     --corte HEAD`, salida en
     `docs/loop/SALIDA_V207_VARA_EXPEDIENTE_AUDITOR.txt`): `BANCO_DEL_PLAN.md`
     61554 y 61554, `LECTURAS_DIRIGIDAS.md` 214916 y 214916, `EJECUTOR.md` 13194
     y 13194, `OP_L_03_LECTURAS.jsonl` 51368 y 51368,
     `OP_L_03_TRIANGULOS.jsonl` 55705 y 55705, y `AUDITOR.md` 30581 y 30581.
     REMIDELOS TU. Ojo con `LECTURAS_DIRIGIDAS.md`: si la TAREA 2 no lo toca,
     tiene que salir igual, y si algo lo mueve, lo dices.

3.c. Publica la COBERTURA MEDIDA Y NO NARRADA, con la lista nominal de los que no
     cubren, y las dos cuentas separadas si el reparto sellado y los veredictos
     no coinciden en numero, como hiciste en la 207.

3.d. NO CIERRES LA FICHA y NO toques su campo `estado`. Proponla y para.

3.e. SI LA TAREA 3 NO CABE CON SUS GUARDAS COMPLETAS, DEJALA ABIERTA Y DILO EN
     LA TABLA. Tu propia frase de la 207 es la regla: una mesa a medias es peor
     que una mesa pendiente. Una fila que siga diciendo ABIERTA, SIN CERRAR es
     una respuesta honesta; una mesa medida a ojo no lo es.

---

## LO QUE VA EN TODA VUELTA, Y NO ES OPCIONAL

- SELLA TU APERTURA antes de la primera operacion, con el HEAD leido de `git` y
  no tecleado, y el estado del arbol. Y si un fichero de identidad nace despues,
  DECLARALO como hiciste en tu `C.2`, no lo disimules.
- EL CICLO ENTERO DE GATE 0 POR LOS DOS LADOS, los ocho comandos en su orden,
  NUNCA `run_phase1.py` a secas. Importa el ciclo, no lo clones (acta 206 `6.5`).
- `git diff HEAD --numstat` sobre `dataset/`, `web/`, `engine/` y `docs/plan/` en
  CERO filas, medido AL CIERRE y no heredado de la apertura.
- LAS SEDES SELLADAS con sus `sha256` por las DOS convenciones, al cierre y
  recomputadas: `INTRA_DOMINIO_VEREDICTOS.jsonl` (4054129 y `0a77b5a35a962621`)
  y `OPERACIONES.jsonl` (513043 y `829c583eb779cab6`). Ni un veredicto ni un
  `estado` se mueven.
- LAS TRES SEDES DEL AUDITOR en 0, distinguiendo el cero de `PARA_ALEXIS.md` como
  DE AUSENCIA DE FICHERO si sigue sin existir.
- CIERRA TU PROPIO REPORTE con `scripts/loop/cerrar_reporte.py --vuelta 208` y
  archiva el mio de la 207 con `archivar_reporte.py`. AVISO MEDIDO, de tu `C.4`:
  ese instrumento ESCRIBE PRIMERO Y VALIDA DESPUES, asi que una corrida en rojo
  te deja el reporte pisado en disco. Committea antes de correrlo y comprueba el
  `sha256` despues.
- TODA CIFRA QUE PUBLIQUES SALE DE UN INSTRUMENTO CORRIDO EN ESTA VUELTA. Las de
  este encargo son CONTRASTE. Si discrepan de tu medicion, la discrepancia se
  declara, no se resuelve copiando.
- TODA RUTA QUE PUBLIQUES COMO EVIDENCIA TIENE QUE EXISTIR Y NO MEDIR CERO
  BYTES. Una ausencia declarada (como tu hueco de bateria) es otra cosa y esa si
  vale, con sus tres piezas.
- MARCA TUS DISCUTIBLES ANTES DE SABER SI ACIERTAS, y con "por donde me puedo
  estar equivocando" escrito. Los seis del sujeto de mi ciega estaban bien
  marcados y acerte cinco: el marcado funciona y se agradece.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
