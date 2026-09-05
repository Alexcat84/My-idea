Commitea y pushea lo pendiente en la rama activa antes de tocar nada. Mira
`git status` antes de nada. Lo que vas a encontrar y como se trata, uno por uno:
`dataset/metadata/master_graph.json` modificado con diff de cero bytes es
suciedad de indice y NO se commitea, como la 169 y la 170 midieron y
declararon; `node_modules/` NO se toca y NO entra en `.gitignore` (adjudicacion
6.5 de mi acta 170: `.gitignore` no tiene hoy ninguna linea de `node_modules`,
medido por mi, y anadirla es decision del fundador); y los dos ficheros que la
vuelta 170 dejo sueltos, `docs/loop/SALIDA_V170_BATERIA.txt` (cero bytes) y
`scripts/loop/_v170_cierre_texto.md` (150 lineas, el bloque de cierre entero),
**YA LOS COMMITEE YO CON MI ACTA Y NO SE BORRA NINGUNO**: el primero es la
prueba medida de que la bateria no corrio y el segundo es la fuente de la
TAREA 1, y dejarlos sueltos era arriesgarse a perder el objeto que este encargo
manda usar.

SESION EJECUTORA. FASE III, EJECUCION. RAMA pasada-unica. MODO DE EJECUCION
CONTINUA (AUDITOR.md seccion 3), con las guardas obligatorias por operacion.
El acta que manda es la de la vuelta 170 (docs/loop/ACTA_AUDITOR.md, cabecera
al final del fichero); sus adjudicaciones 6.1 a 6.12 son la letra de este
encargo.

LO QUE YA ESTA VERIFICADO Y NO HAY QUE VOLVER A HACER: las cinco tareas de la
170 reproducen bajo mis instrumentos. Marcador 3.388 con A 551, B 72, C 5,
D 2.760 y cero huecos. Gate 0 con su ciclo entero VERDE por mi mano, numstat de
cero filas, motor 25/25, tsc exit 0, web 82 ficheros y 1.040 pasadas. Censo
3.853 / 3.169 / 684 y aristas 8.780 / 8.740 / 17.520 / 9.914 con cero
auto-aristas. Inventario 672 entradas con 54 familia_de_ids. 71 fichas. La tabla
de tachadas del comentario del arnes la reconte A MANO desde los blobs de git,
sin usar tu instrumento: 12 en `3ffc2091` (vuelta 58), 13 en `33fe1380` (vuelta
166) y 13 en `c6ac70f6` (vuelta 167), con dieciocho de las diecinueve filas
identicas entre los dos ultimos blobs. TU CORRECCION DE LA CUARTA SEDE ES
CORRECTA Y NO SE VUELVE A TOCAR. Los cinco puentes del sales roadmap los
recompute desde cero con mi propio resolutor y salen los cinco, con 15 de 15
pares con clase y reparto A 7 D 8. Las tres formas de las nominas reproducen.

LA VARA DEL TRABAJO PENDIENTE SIGUE SIENDO EL INSTRUMENTO,
scripts/loop/vuelta150_3_relectura_expediente.py --corte HEAD, NUNCA EL CAMPO
`estado`. Corrida por mi hoy: 71 fichas, 37 que no calzan, 6 en LISTA sin
ninguna prueba, y de esas seis las dos OP-M-02 siguen CUMPLIDAS POR CONSUNCION
por la 6.6 del acta 168 y NO se ejecutan. El trabajo real son cuatro fichas.

Y LO PRIMERO QUE TIENES QUE SABER, PORQUE ES LA RAZON DE QUE ESTE ENCARGO SEA EL
QUE ES: LA VUELTA 170 HIZO SU TRABAJO Y NO CERRO SU REPORTE. El commit
`29f04e86`, titulado "EL BLOQUE DE CIERRE DE LA VUELTA 170, ENTERO", toca doce
ficheros y `docs/loop/REPORTE.md` no es ninguno de ellos. El reporte en HEAD
sigue diciendo "EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA" y "PENDIENTE DE
TALLAR AL CIERRE", y sus secciones 3 a 9 no existen: viven sin commitear en
`scripts/loop/_v170_cierre_texto.md`, escrito a las 22:45:34, tres minutos
DESPUES del commit que dice llevarlo. Y la bateria no corrio: su fichero de
salida mide cero bytes. NADA DE ESTO ES UNA CAIDA DE CIFRA PUBLICADA NI DE
REPORTE, porque `REPORTE.md` dice la verdad y dice que le falta el cierre; pero
tres de mis tres hallazgos de esta vuelta estan en ese mismo tramo, y por eso EL
TRAMO QUE SE RELEE AL DOBLE ES EL BLOQUE DE CIERRE.

LA RELECTURA AL DOBLE, Y ES OBLIGATORIA (AUDITOR.md 1.2, credito de tanda bajado
en mi acta 170 por tres hallazgos FUERA del marcado, los tres en el cierre): EL
TRAMO QUE SE RELEE AL DOBLE ES EL BLOQUE DE CIERRE DE LA VUELTA. Sus cuatro
piezas son el reporte cerrado, la cabecera tallada pegada, la bateria corrida
entera, y el arbol limpio. CADA UNA DE LAS CUATRO SE COMPRUEBA DOS VECES: una al
hacerla, y otra DESPUES DE COMMITEAR, leyendo del arbol y de `git show` lo que
acabas de escribir. Un commit cuyo asunto afirme algo que su propio `--stat` no
respalda es lo que esta vuelta viene a no repetir. Y el reporte dice que se
comprobo y con que comando.

EL REPORTE ABRE CON LA VUELTA (EJECUTOR.md regla 1), pero ESTA VEZ EL ORDEN DE
LA APERTURA CAMBIA Y ES OBLIGATORIO, porque el esqueleto sobreescribe
`docs/loop/REPORTE.md` sin preguntar y lo que hay ahi dentro todavia hace falta:
(1) CIERRAS el reporte de la 170 en su sitio y lo commiteas; (2) SOLO ENTONCES
corres `scripts/loop/archivar_reporte.py` para la 170, que lee de git y por eso
necesita ese commit hecho; (3) SOLO ENTONCES tallas el esqueleto de la 171 y
corres el bloque de apertura entero. Tallar antes de cerrar destruiria el objeto
que este encargo te manda cerrar. TOPE DE CINCO TAREAS POR VUELTA, y este
encargo trae exactamente cinco.

- TAREA 1, BLOQUEANTE Y VA PRIMERA: LOS REGISTROS Y EL CIERRE QUE FALTO.
  (1.a) El acta 170 y sus adjudicaciones 6.1 a 6.12 al `R.40`, por el mismo
  carril de siempre, con el numero computado por
  scripts/loop/serie_de_registros.py y NO tecleado (hoy da 31 entradas, mayor
  R.39, siguiente libre R.40; recomputalo tu). Y con su arnes de mutacion del
  registro, que la vuelta 169 prometio y no escribio y la 170 si escribio: sigue
  a la 170, no a la 169.
  (1.b) CIERRAS EL REPORTE DE LA VUELTA 170. El cuerpo ya existe: son las
  secciones 3 a 9 de `scripts/loop/_v170_cierre_texto.md`, y se anexan al
  reporte TAL COMO ESTAN, sin reescribirlas y sin suavizar ninguno de sus ocho
  discutibles ni de sus cinco caidas. Encima va la cabecera tallada, que sale de
  `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 170` y que YA SALIO
  VERDE con las dos columnas al cierre de la 170 (esta en
  `docs/loop/SALIDA_V170_TALLADOR_CABECERA.txt`): se pega esa tabla, no se
  teclea. Y se escribe el veredicto de una linea, que hoy dice "SIN ESCRIBIR
  TODAVIA".
  (1.c) LA SECCION 9 DEL REPORTE DE LA 170, "LA BATERIA", SE ESCRIBE DICIENDO LA
  VERDAD Y NO SE RELLENA CON UNA CORRIDA DE HOY. La bateria de la vuelta 170 no
  corrio: dilo, con la medicion delante (`docs/loop/SALIDA_V170_BATERIA.txt`,
  cero bytes) y con el motivo (la vuelta se corto). Y remite a la seccion 5 de mi
  acta 170, que trae la corrida que hice yo. ESCRIBIR AHI UNA CORRIDA DE LA 171
  COMO SI FUERA DE LA 170 SERIA EXACTAMENTE LA ESPECIE QUE ESTA CAMPANA
  PERSIGUE. No lo hagas.
  (1.d) Y SOLO ENTONCES, el archivador para la 170 y el esqueleto de la 171.

- TAREA 2, BLOQUEANTE PARA LA 3: EL BORRADOR QUE ENVENENO UN INSTRUMENTO
  (adjudicacion 6.3). `docs/loop/_v170_t4_seccion.md` nombra `LD-12`, `LD-27`,
  `LD-100`, `LD-137`, `LD-139` y `LD-154`, y `scripts/loop/vuelta48_contar_ld.py`
  barre `docs/` entero excluyendo por nombre solo `SALIDA_*`, `ACTA_AUDITOR.md`,
  `PROMPT_SIGUIENTE.md`, `REPORTE.md` y los registros del arnes. Resultado
  medido por mi en los dos cortes, con un worktree limpio para el primero: en
  `222ca6a7` el instrumento da 82 hechas, universo hasta `LD-138`, 54 huecos y 2
  nombradas sin seccion; en HEAD da 82 hechas, universo hasta `LD-154`, 64
  huecos y 8 nombradas sin seccion. TU CIFRA DE 54 ERA CIERTA CUANDO LA MEDISTE
  Y LA REPRODUJE EXACTA; lo que pasa es que el commit que la trajo la convirtio
  en 64. Los CINCO `docs/loop/_v170_t*_seccion.md` se MUEVEN a `scripts/loop/`
  con `git mv`, que es donde tu misma vuelta aparco el borrador del cierre. NO SE
  BORRA NADA Y NO SE EDITA NINGUNO. Despues vuelves a correr el contador y
  publicas las tres lecturas al lado (la de `222ca6a7`, la de HEAD antes de
  mover, y la de despues de mover), y compruebas que las dos varas convergen: el
  mayor de las HECHAS y el mayor del UNIVERSO tienen que dar los dos `LD-138`.
  SI NO CONVERGEN, PARAS Y LO TRAES.

- TAREA 3, LA NUMERACION `LD`, QUE YA NO ES PARADA (adjudicacion 6.1). Traiste
  la pregunta como doctrina nueva y no lo es: tu propio encargo nombraba
  `serie_de_registros.py` por su nombre, y ese instrumento LLEVA LA DEFINICION
  ESCRITA EN SU CODIGO, en las lineas 97 a 102, con docstring: "EL NUMERO QUE NO
  SE TECLEA. Uno mas que el mayor escrito en CUALQUIERA de...", y
  `return (max(nums) + 1) if nums else 1`. Sin condicional de huecos y sin
  excepcion. EL SIGUIENTE LIBRE ES EL MAYOR MAS UNO, y el camino es el 1.
  Hiciste bien en parar antes que inventar; lo que te falto fue abrir el fichero
  del instrumento que el encargo te nombraba. Asi que las 16 filas de tabla de la
  segunda tanda de `docs/plan/LECTURAS_DIRIGIDAS.md` (lineas 327 a 518, tres
  tablas de 8, 5 y 3 filas, las 16 sin numero, contadas por mi) GANAN `LD-139` a
  `LD-154` POR ADICION PURA, con los numeros COMPUTADOS POR INSTRUMENTO despues
  de la TAREA 2 y SIN TOCAR UNA PALABRA de su texto. Numerar no es reescribir.
  Con su caso positivo por mutacion, que tiene que CAER si el instrumento teclea
  un numero en vez de computarlo. El `D.6` (que el tramo `LD-12` a `LD-27` mida
  exactamente 16 y caiga justo entre la primera tanda y la tercera) queda
  DECLARADO EN EL REPORTE COMO CONTRASTE MEDIDO Y NO COMO FUNDAMENTO: el propio
  instrumento dice que esos numeros nunca fueron nombrados, o sea que nadie los
  asigno, y una adyacencia no es una asignacion.

- TAREA 4, LAS DOS DEUDAS DE REGISTRO (adjudicaciones 6.4 y 6.11).
  (4.a) EL AGUJERO DEL `R.38`, QUE ES TU HALLAZGO Y LO VERIFIQUE: la entrada
  `R.38` de `docs/PENDIENTES.md`, escrita por la vuelta 169, afirma que "el arnes
  hermano lo prueba por mutacion en vez de afirmarlo", y ese arnes no existe
  (`ls scripts/loop/ | grep mutacion_registro` da 164, 165, 166, 167, 168 y 170,
  y ninguno de la 169; corrido por mi hoy). "No es mio y el encargo no me manda
  tocarlo" no vale para una afirmacion falsa en la serie de registros: la serie
  es una sola y la lee todo el que venga detras. Se corrige por el carril del
  banco 9.10, con la frase vieja ENTERA Y TACHADA y la correccion fechada debajo
  con su medicion pegada. Traerlo estuvo bien; dejarlo, no.
  (4.b) EL `81` DE `docs/plan/00_INDICE.md:644`, que es tu `P.2`: publica 81
  lecturas dirigidas hechas con corte 19 ago 2026 y el instrumento mide 82 hoy.
  No es una mentira, lleva su corte. Se le adosa la cifra de hoy por 9.21, POR
  ADICION Y SIN TOCAR LA LETRA VIEJA, y se hace DESPUES de la TAREA 2, porque el
  contador es el mismo instrumento que la TAREA 2 limpia.

- TAREA 5, LOS TRES INSTRUMENTOS QUE FALTAN (adjudicaciones 6.6, 6.9 y 6.12).
  (5.a) EL ARCHIVADOR SE ENCHUFA, que es tu `D.2`. Un archivador que hay que
  acordarse de correr no cierra el agujero de la 6.4 del acta 169, lo aplaza; y
  esta vuelta acaba de demostrar de que va, porque el esqueleto sobreescribe
  `REPORTE.md` sin preguntar. Se llama como paso 0 del esqueleto, y EL ESQUELETO
  SE NIEGA A ESCRIBIR SI EL REPORTE ANTERIOR NO ESTA ARCHIVADO, que es el canon
  de fallar ruidoso del banco. Con su caso positivo por mutacion, y que el caso
  CAIGA si el esqueleto escribe con el archivo ausente.
  (5.b) EL CENSO DEL CAMPO `forma`, que es tu `D.5`, tu `P.4` y tu `PD.2`. Dices
  que no encontraste vocabulario cerrado, y eso es una busqueda negativa que no
  se puede citar (EJECUTOR.md 9), asi que se mide: barrido de las 672 entradas de
  `docs/plan/INVENTARIO.jsonl` con la nomina de palabras de `forma` y su cuenta,
  cada una con cuantas entradas la usan. Con el censo delante o hay vocabulario y
  se dice si `FUNDIDA` cabe, o no lo hay y sube al fundador como hallazgo.
  MIENTRAS TANTO LA PALABRA SE QUEDA: describe un hecho que verifique (6
  miembros, un solo nodo vivo, cero pares) y ninguna regla escrita la prohibe.
  MEDIR ANTES DE LEGISLAR.
  (5.c) LOS 8 PARES SIN LEER de `la supervision de la IA`, que es tu `P.5`. No
  afirmo que sean backlog nuevo porque no lo he medido, y tu tampoco. Barrido
  MEDIDO sobre las 71 fichas de `docs/plan/OPERACIONES.jsonl` buscando esos 8
  pares en `nodos`, `preservar`, `eliminar` y `superviviente`, con los 8
  nombrados uno a uno y con el comando escrito al lado, porque una busqueda
  negativa no se puede citar.

LO QUE ESTE ENCARGO NO TRAE, DICHO PARA QUE NO LO BUSQUES: `OP-L-03` queda
abierta y leida y NO se ejecuta esta vuelta. Sus tres clausulas y su adjudicacion
las dejaste leidas en el reporte de la 170 y ahi siguen. El motivo es el tope de
cinco tareas y el hecho de que la vuelta 170 dejo su cierre a medias: primero se
paga eso, y la ficha empieza la vuelta 172 abierta y no por abrir.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
