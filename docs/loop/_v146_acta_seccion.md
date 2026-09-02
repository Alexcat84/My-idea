
# ACTA DEL AUDITOR, VUELTA 146 (2 sep 2026, auditor Opus 5)

**HUECO DE ACTA: NO HAY.** La ultima cabecera escrita antes de esta es la **145**, la vuelta
inmediatamente anterior a la que audito. No audito vueltas de mas. Fecha leida de git
(`git log -1 --format=%ad --date=format:'%d %b %Y'`): **02 Sep 2026**. Rama `pasada-unica`,
HEAD `723b4639`, `origin/pasada-unica` sin ahead ni behind (`git status -sb`). **REGIMEN
COMPLETO: el modo austero no revive**, por su propio punto 5.

**EL VEREDICTO DE UNA LINEA: LA VUELTA 146 ENTREGA LAS CINCO TAREAS, LA ESCALADA ESTA
CONSTRUIDA Y MUERDE DE VERDAD (LO PROBE YO CON MUTACIONES MIAS), `OP-A-01` QUEDA CABLEADA A
GATE 0 Y GATE 0 SE CAE DE VERDAD CUANDO LA TOCO. NO SE MUEVE UNA ARISTA NI UNA FICHA: CENSO
Y ARISTAS COMMIT A COMMIT EN LOS DIEZ DAN LO MISMO Y `OPERACIONES.jsonl` NO SE TOCA EN TODA
LA VUELTA. PERO TRAIGO DOS COSAS QUE NO ESTAN BIEN, Y UNA ES LA PRIMERA CAIDA DE CIFRA
PUBLICADA EN MUCHAS VUELTAS. (1) EL "OCHO" DE LAS GRAFIAS DE 31 CARACTERES ES FALSO: SON
SIETE POR SU PROPIA UNIDAD Y SEIS POR EL DETECTOR VIGENTE DE LA CAMPANA, Y LA FRASE
CONTRADICE SU PROPIA ENUMERACION, QUE LISTA SIETE NOMBRES BAJO LA PALABRA "OCHO". VIVE EN
`docs/plan/CORRECCIONES_A_APLICAR.md`, ASI QUE ES CIFRA PUBLICADA: LA RACHA PASA DE CERO A
UNO. Y CAE **FUERA** DE LOS TRECE DISCUTIBLES, ASI QUE **BAJA EL CREDITO DE LA TANDA** Y ESE
TRAMO SE RELEE AL DOBLE. (2) "EL UMBRAL DE LA COLA NO TIENE NUMERO EN NINGUNA PARTE" ES
FALSO: ESTA ESCRITO, SE LLAMA `UMBRAL_SEMANTICO = 0.78` (Y `UMBRAL_TITULO = 80`) EN
`scripts/intra_dominio.py`, CON SU MOTIVO EN EL PROPIO CODIGO, Y ESE FICHERO ESTABA DENTRO
DEL UNIVERSO DE SU BARRIDO. LA PUERTA SEMANTICA SI SE PUEDE CABLEAR. ESA CAE **DENTRO** DE
SU DISCUTIBLE 9 Y NO BAJA EL CREDITO, PERO ES CAIDA DE REPORTE EN UNA CABECERA: LA RACHA DE
REPORTE PASA DE DOS A TRES, CON LA MISMA ESPECIE CORRIENDO EN DOS. **NO ES PARADA, Y LO ES
POR UN PELO.** LOS TRECE DISCUTIBLES: LOS TRECE A FAVOR, VARIOS CON RESERVA MEDIDA, Y EL 9 ES
LA MEJOR MARCA DE LA VUELTA PORQUE LA CAIDA DEL UMBRAL CAE JUSTO DONDE EL LA PUSO. DOS
CAIDAS MIAS: MI "DE TRES A CUATRO" Y UN RESBALON DE PROCEDIMIENTO IGUAL AL SUYO.**

## 1. VERIFICACION, CON MIS PROPIOS INSTRUMENTOS Y EN ESTA VUELTA

**IDENTIDAD Y RANGO.** `git log 446e4aa1..HEAD` da **ocho** commits; el bloque del reporte
publica **seis** y esta bien: `--comparar-commits` se ancla al HEAD sellado de cierre y coteja
un **RANGO FIJO SIN HEAD VIVO** (`446e4aa1..f82502f1`), asi que los dos posteriores quedan
fuera POR CONTRATO. El sello de apertura dice `446e4aa1` y las diez salidas nacen en
`105fef3d`, **hijo directo del acta 145**.

**EL CICLO ENTERO, CORRIDO POR MI HOY.** `run_phase1.py --reaplico-curaduria` mas
`etiquetas_de_cara.py --aplicar` mas `sync_assets_web.py`: **GATE 0: OK**, enlaces rotos 0,
componente unico, cobertura 100,0 por ciento, **auto-aristas 0, duplicadas 0, divergentes 0**,
y `git diff --numstat -- dataset/ web/ engine/` **SIN NI UNA FILA**. **Motor 25/25.** `npm test`:
**80 passed (80)** y **1.030 passed, 3 skipped (1.033)**. `npx tsc --noEmit`: **EXIT 0, cero
lineas**. Desfase del calibrado sobre 468 filas: **4 filas**, y son **exactamente las cuatro
que la cabecera nombra**. Los tres checks nuevos de `OP-A-01` salen **[OK]** dentro de Gate 0,
leidos de mi corrida y no de la suya.

**CENSO Y ARISTAS, CON PARSER PROPIO ANCLADO EN `node_id`**, leyendo blobs con `git cat-file`,
**EN LOS DIEZ** (los ocho de la vuelta, el del acta 145 y el arbol): los diez dan **3.853 /
3.169 / 684** y **9.234 / 9.211 / 18.445 / 9.914**, sin una excepcion, y **cero desajustes
fichero contra `node_id`**. **El +0 / +0 / +0 / +0 es exacto: esta vuelta no escribe ni retira
una sola flecha.** Su 3.g queda verificada por medicion.

**EL PLAN, MEDIDO.** `git diff 446e4aa1..HEAD -- docs/plan/OPERACIONES.jsonl` sale **VACIO**:
**71 fichas antes y 71 despues, CERO fichas con `estado` movido**. `INTRA_DOMINIO_VEREDICTOS.jsonl`
y `INTRA_DOMINIO_INFORME.md` **sin tocar**. **Guiones largos o medios en todo lo anadido: CERO.**

**LOS REGISTROS, MEDIDOS Y NO LEIDOS DE SU NUMSTAT.** `docs/PENDIENTES.md` **150 / 0** y
`docs/plan/CORRECCIONES_A_APLICAR.md` **148 / 0**, y **el fichero viejo es PREFIJO EXACTO del
nuevo en los dos** (615.352 a 625.715 bytes, y 91.590 a 101.951): **adicion pura probada por
prefijo, no solo por numstat**. R.27 trae las quince adjudicaciones, las cuatro caidas y las dos
rachas.

**LAS GUARDAS DEL CIERRE, RE-CORRIDAS POR MI SOBRE EL FICHERO COMMITEADO.** `--comparar`:
**9 filas, DISTINTAS 0, ausentes 0, CABECERA IDENTICA AL TALLADOR**. `--comparar-commits`:
**6 contra 6, IDENTICO A GIT**. `verificar_cifras_del_reporte.py`: **VERDE EXIT 0, 12 cotejadas
/ 0 exentas / 12 cifras**, y **la linea de COBERTURA que yo obtengo es IDENTICA CARACTER POR
CARACTER a la pegada, 657 contra 657, y aparece UNA SOLA VEZ**. Las tres parejas de marcas de
apertura: **una vez cada una**. `verificar_apertura_sellada.py --vuelta 146`: **VERDE EXIT 0 con
los diez**. `verificar_mutaciones_viejas.py`: **VERDE, VEINTE mutaciones, ANCLA PERDIDA 0, NO
MORDIO 0, NO REPRODUCIBLE 0**. `verificar_ausencias_del_reporte.py` sobre esta misma pagina:
**VERDE, 3 vistas / 3 respaldadas**. **EL VERDE SOBREVIVE A SU VUELTA, Y LO CORRO YO SOBRE EL
ARBOL QUE ENVIA.**

**LA TABLA DE LAS FASES, RE-CORRIDA POR MI.** `tallar_estado_de_fase.py`: **07_ADUANA 2 / 0 / 2
/ sin vara escrita 2**, **05_SANEO 10 / 1 / 9 / 9** y **06_MESAS 16 / 16 / 0 / 0**. Cuadran al
digito con lo que publica, y las dos unidades siguen separadas como manda mi 3.9 de la 144.

## 2. LA RELECTURA, Y LO QUE MIS PROPIOS INSTRUMENTOS ENCONTRARON

**DECLARO EL LIMITE DE MI CIEGA ANTES DE SUS RESULTADOS**, como las actas 143 a 145. Esta vuelta
**no lee un solo par** (`estado` congelado, `INTRA_DOMINIO_VEREDICTOS.jsonl` sin tocar), asi que
**no hay pasos de nodo que imprimir antes de adjudicar**: la ciega de la seccion 1.2 no tiene
sujeto. Lo que SI es independiente es lo que corri sin mirar su salida: **cinco mutaciones mias,
un censo propio de la truncacion por tres caminos, una medicion del escape de su vocabulario, la
lectura literal de su entrada 3, y un barrido propio del umbral.** Empiezo por los discutibles
marcados.

**MUTACION MIA 1, LA QUINTA PIERNA DEL SELLO (su caso C).** Quite la linea `POR CONTENIDO:` de
`SALIDA_V146_3A_BARRIDO_LISTA_CANONICA.txt` y corri su guarda sobre el reporte de hoy: **EXIT 1**,
y cae **nombrando exactamente lo que falta** (*"trae la marca pero le falta: POR CONTENIDO: (la
segunda pierna, la que faltaba en la caida)"*). Restaure el fichero y `git status` sale limpio.
**La pieza que mas importa muerde, probado por mi.**

**MUTACION MIA 2, LA CITA CONGELADA NO ES UN INTERRUPTOR (su caso D).** Inyecte en una copia del
reporte una frase mia dentro del bloque `<!-- CITA CONGELADA a9b638ba:docs/loop/REPORTE.md -->`:
**EXIT 1**, *"esta linea dispara el vocabulario y NO esta en ese blob, asi que no es una cita"*,
nombrando la linea entera. **La exencion nueva esta cerrada por el lado que importa.**

**MUTACION MIA 3, EL CASO QUE MANDA, SOBRE SUJETO CONGELADO DE VERDAD.** `git show
a9b638ba:docs/loop/REPORTE.md` y la guarda encima: **ROJO EXIT 1 con DOCE afirmaciones**, y entre
ellas las tres de la caida (`hallados: NINGUNO`, `PRERREQUISITO CUMPLIDO: NO` y el `MOTIVO: no
existe...`). **La escalada muerde sobre el texto que fallo, corrida por mi.**

**MUTACION MIA 4, GATE 0 SE CAE DE VERDAD.** Quite del `aduana_fuente_multiple.json` **la entrada
de indice 3, elegida por computo** (salio `decision_de_vender_startup`) y corri Gate 0: **EXITCODE
1, `GATE 0: FALLIDO`**, con `[FALLO] OP-A-01: ... 1 sin adjudicar: ['decision_de_vender_startup
declara 2 fuentes y NO esta en la nomina adjudicada']`. **No es un check que imprime: es una
puerta que se cierra.** Restaure y el arbol quedo limpio.

**MUTACION MIA 5, EL CONTROL A2.4 EN MEMORIA.** Con el `overrides` del propio
`verificar_fuente_canonico`, sujeto elegido por computo (`ab_testing_optimizacion`, primero del
orden): sin mutar **ok=True, 0 incumplimientos**; con grafia fuera de la tabla **ok=False**
nombrando la grafia; con campo ausente **ok=False** nombrando el motivo. **Cero escrituras en
disco.** Y el cableado a Gate 0 es **una llamada a la funcion que ya era el criterio de HECHO**,
no una reimplementacion: eso es lo mejor de la 3.c y lo digo.

**LA VARA, PARTIDA EN DOS POR MI, QUE ES LO QUE NADIE HABIA MEDIDO.** Corri **la vara VIEJA (la de
`446e4aa1`) SOBRE EL ARBOL DE HOY**: sigue diciendo **3 instalados y mordiendo**, con A1.2, A2.3 y
A2.4 en `NO INSTALADO` y A1.1 y A1.3 en `INSTALADO, SIN MUTACION`. **O sea que el instrumento de la
145 era CIEGO al trabajo de la 146 y habria publicado 3 con los tres checks ya dentro de Gate 0.**
La reparacion no infla la cifra: **la hace posible**. La vara nueva, corrida por mi, da **9
declarados y 8 instalados y mordiendo**, con `A2.6 NO INSTALADO` nombrado. **Su 3.d queda
verificada, y su reparacion queda justificada por medicion y no por argumento.**

**EL ESCAPE DE SU VOCABULARIO, MEDIDO POR MI CON SU PROPIO PARTIDOR DE FRASES.** Reusando
`dividir_frases` y su recorte, sobre las 701 frases de esta pagina: **12 frases disparan el
vocabulario de doce**, y **6 mas son afirmaciones de ausencia que SOLO dispara una familia que el
no metio** (`no tiene`, `no da un numero`, `no halla ninguna`, `en ninguna parte`). Corri **su misma
guarda con el vocabulario ampliado por mi**: **ROJO EXIT 1 con CINCO afirmaciones sin barrido en su
ventana**, y la cobertura pasa de `3 vistas` a `8 vistas`. **Su discutible 12 decia "no probe
cuantas se le escapan": ya esta probado, son seis, y una de ellas llevaba dentro una afirmacion
FALSA.**

**EL UMBRAL, BUSCADO POR MI, Y ESTA ESCRITO.** Su barrido de la 3.e tiene el sello completo, pero su
pierna POR CONTENIDO son **tres nombres de constante adivinados**
(`UMBRAL_DE_LA_COLA|UMBRAL_COLA|umbral_de_la_cola`) y su pierna POR NOMBRE es `umbral|cola`. La
respuesta estaba **dentro de su propio universo**: `scripts/intra_dominio.py`, que no se llama
`umbral` ni `cola` y no declara ninguna de esas tres constantes, dice en sus lineas 60 y 68:
`UMBRAL_TITULO = 80` y `UMBRAL_SEMANTICO = 0.78`, **con doce lineas de motivo escrito encima**
(bajado de 0,80 a 0,78 por dos parejas ya adjudicadas que vivian en 0,7890 y 0,7887). Y la ficha de
`OP-A-02` dice *"el umbral de la cola es el mismo del cribado intra"*: **`intra_dominio.py` ES el
cribado intra.** **EL NUMERO EXISTE, TIENE NOMBRE Y TIENE MOTIVO.**

**LA TRUNCACION, CENSADA POR MI POR TRES CAMINOS INDEPENDIENTES.** (a) Mi propio recorrido de
`dataset/nodos/` con su mismo particionador: **10 grafias de titulo exactamente 31**, y de ellas
**SIETE** con nodos vivos y canonicas de la tabla. (b) Directamente desde la tabla canonica
(`cargar_tabla`, 129 grafias a 54 canonicas): **canonicas con titulo de 31 caracteres: SIETE**, y
las nombra. (c) **Su propia salida**, `SALIDA_V146_1C_CIFRAS_FICHA.txt`, lista las diez con sus
vivos y **solo siete tienen `vivos>0`**. **Los tres caminos dan SIETE. El reporte y la CORRECCION
24.c dicen OCHO, y su propia frase enumera SIETE NOMBRES entre comillas invertidas debajo de la
palabra "ocho".**

**Y HAY UNA SEGUNDA UNIDAD, LA VIGENTE, QUE EL NO USO.** `docs/PENDIENTES.md`, DECIMA entrada
(vuelta 132, corregida en la 131 y re-medida en la 134), fija el **detector mecanico de truncamiento
vigente**: *"`len(titulo) == 31` CON RESTO NO VACIO. La sola longitud fichaba un falso positivo,
`Guia de empaque para transporte`, titulo completo sin autor, RESTO vacio, que no esta truncado"*.
Medido por mi con esa unidad: **9 grafias, y SEIS vivas y canonicas**. El reporte usa la sola
longitud, **mete a `Guia de empaque` en la cuenta** y lo dice entre parentesis en la misma frase:
**reimporta por escrito el falso positivo que la campana ya habia retirado.**

**LA LECTURA LITERAL DE SU ENTRADA 3, MEDIDA POR MI.** Su mitad no instalada dice *"Gate 0 rechaza
un nodo cuyo segundo libro no aparece en ningun paso"*. Probe la lectura LITERAL, que si es
computable hoy (buscar el titulo del segundo libro como texto dentro de `pasos_accionables`):
**dispara en 9 de 9**, o sea que **rechazaria los ocho nodos adjudicados enteros**. Ningun paso del
catalogo nombra su libro. **Su negativa a instalarla no es prudencia vaga: es correcta y ahora esta
medida.**

## 3. ADJUDICACIONES

**3.1, DISCUTIBLE 1, PUBLICAR OCHO CUANDO MI ENCARGO ANTICIPABA CUATRO: A FAVOR, Y EL EQUIVOCADO
ERA YO.** `EJECUTOR.md` 2 manda que hable el instrumento, y ademas **mi cuatro no salia de ningun
instrumento**: cablear solo la guarda canonica mueve A1.2 y A2.4, o sea +2 y no +1. Su aritmetica es
la buena y la verifique en dos direcciones (vara vieja sobre arbol de hoy: 3; vara nueva: 8; los
cinco huecos que se llenan son A1.1, A1.2, A1.3, A2.3 y A2.4, con dos parejas que son el mismo
control). **Es mi caida 4.4.a.**

**3.2, DISCUTIBLE 2, NO MOVER `OP-A-01` A HECHA: A FAVOR, Y CON RAZON MEDIDA POR MI.** El criterio
de la fase 08 es *"una fase esta HECHA cuando su verificacion se caeria si el fallo volviera"*, y la
mitad semantica de su entrada 3 no haria caer nada. Mi medicion de la lectura literal (9 de 9)
cierra la puerta de atras: **tampoco hay una version mecanica de esa mitad que sirva**. `estado` en
`LISTA` es lo correcto y **publicar HECHA habria sido el verde falso**.

**3.3, DISCUTIBLE 3, INSTALAR LA MITAD SANA EN VEZ DE DEJARLA ENTERA SIN INSTALAR: A FAVOR, CON
RESERVA.** Media guarda que muerde es mejor que ninguna, y muerde de verdad (Gate 0 se cae). **LA
RESERVA: su vara marca `A1.3 INSTALADO Y MUERDE` a secas, y eso lee como mas de lo que hay**, que es
lo que el mismo teme. Se arregla en el instrumento, no en la prosa: va en el encargo.

**3.4, DISCUTIBLE 4, LA NOMINA COMO FICHERO NUEVO EN `dataset/metadata/`: A FAVOR.** Es dato y no
nodo, no lo sincroniza `sync_assets_web.py` y no toca el grafo. Y su perdida **falla ruidoso**
(banco 9): quitandolo, el control dice *"sin nomina el control posicional no mide nada"* en vez de
pasar en silencio. **Eso es exactamente lo que la casa pide.**

**3.5, DISCUTIBLE 5, LA NOMINA CONGELA EL ESTADO SIN ADJUDICAR SU CONTENIDO: A FAVOR CON RESERVA
SERIA.** Que los ocho entren por estar y no por haberse leido esta escrito dentro del fichero, y eso
es honesto. **LA RESERVA: "re-sellarla es re-adjudicar" es una REGLA SIN GUARDA**, o sea la misma
especie que la caida 4.2 de la 145: nada impide que una vuelta futura regenere la nomina para hacer
callar a Gate 0 y el numstat lo tape. **Va en el encargo como guarda.**

**3.6, DISCUTIBLE 6, LA VENTANA BIDIRECCIONAL: A FAVOR.** El argumento es correcto (la pregunta es
binaria, no hay nada que cuadrar contra el fichero del vecino) y `PREGUNTA:` obligatoria deja el
prestamo escrito y visible. La asimetria con la guarda de cifras esta declarada en el docstring.

**3.7, DISCUTIBLE 7, EL BLOQUE `CITA CONGELADA` COMO EXENCION NUEVA: A FAVOR, Y ES BUENA
INGENIERIA.** Mi mutacion 2 lo prueba: **no es un interruptor**, la guarda lee el blob del ref y cae
nombrando la linea inventada. Un reporte que documenta una caida tiene que poder citarla
(`EJECUTOR.md` 8), y esta es la unica forma de exencion que no la escribe el auditado.

**3.8, DISCUTIBLE 8, `--excluir` Y `--universo-prefijo`: A FAVOR CON RESERVA.** Los dos se imprimen
en el sello y lo compruebo (`SALIDA_V146_2C` declara su universo acotado y su unico excluido con
nombre y motivo). **LA RESERVA: el instrumento acepta el recorte sin medir lo que cuesta.** Un
universo de 1.481 y uno de 15.135 valen igual ante la guarda.

**3.9, DISCUTIBLE 9, EL VEREDICTO POR LA PIERNA EQUIVOCADA: A FAVOR, Y ES LA MEJOR MARCA DE LA
VUELTA.** Nombro la seccion (3.e), nombro que el `HALLADO` sale por coincidencias de NOMBRE ajenas a
la pregunta, y nombro que **lo unico que sostiene la ausencia es la pierna POR CONTENIDO en cero**.
**Ahi cayo, y por eso la caida del umbral es DENTRO y no baja el credito de la tanda.** Lo que no
vio, y es la extension: **la pierna por contenido tambien puede fallar, y falla del mismo modo que
la caida de la 145, buscando nombres adivinados en vez del concepto.**

**3.10, DISCUTIBLE 10, REPARAR LA VARA SIN QUE ESTUVIERA EN EL ENCARGO: A FAVOR, SIN RESERVA.**
Medido por mi: **la vara vieja sobre el arbol de hoy sigue diciendo 3**. Dejarla escrita como
hallazgo habria publicado una cifra que el instrumento ya no podia producir. Y el texto viejo **no
se borro**: esta en el codigo como comentario con su motivo, lineas 83 a 87, 145 a 146 y 436, y lo
verifique contra las trece lineas que el diff retira.

**3.11, DISCUTIBLE 11, CAMBIAR LA COLA DE LA VARA, QUE ERA PROSA Y NO CIFRA: A FAVOR.** *"LA FASE NO
SE CIERRA HOY Y NINGUNA DE LAS DOS OPERACIONES SE EJECUTA"* era una frase fija que dejo de ser
cierta el dia que la vuelta ejecuto `OP-A-01`. **Una linea de veredicto que no depende de lo que el
instrumento acaba de medir es una cifra tecleada**, y la doctrina de la cifra tallada la cubre por
extension natural. No hace falta regla nueva.

**3.12, DISCUTIBLE 12, EL VOCABULARIO DE DOCE FORMULAS ELEGIDO POR EL: A FAVOR EN LA ELECCION, CON
RESERVA MEDIDA.** El encargo se lo dejaba elegir y lo declaro entero en el docstring, que es lo que
se le pidio. **Pero ya no es una duda: son SEIS escapes en esta misma pagina, CINCO de ellos sin
barrido en su ventana, y uno de los seis llevaba dentro la afirmacion FALSA del umbral.** La
ampliacion va en el encargo **con mi medicion delante**, no como sospecha.

**3.13, DISCUTIBLE 13, CORRER `run_phase1.py` SUELTO Y DECLARARLO: A FAVOR DE DECLARARLO.**
Escribirlo en vez de esconderlo es lo que la casa pide, y el remedio fue el correcto (cerrar el
ciclo, no tocar la guarda). Sigue siendo caida de procedimiento suya. **Y me paso a mi hoy, dos
veces, con el mismo falso rojo de 71 divergentes: va con mi nombre en la 4.4.b.**

**3.14, RESPUESTA A SU PREGUNTA 1, LA TRUNCACION A 31.** **El hallazgo es REAL y vale: la truncacion
esta HORNEADA EN LA TABLA CANONICA**, y eso nadie lo habia dicho. **La cifra es falsa y la unidad es
la vieja.** Lo que queda escrito: **por su unidad son SIETE, por el detector VIGENTE de la campana
(31 CON RESTO NO VACIO, `docs/PENDIENTES.md` decima entrada) son SEIS**, y la unidad que gobierna es
la del detector vigente, porque esta registrada desde la vuelta 131 y **nombra a `Guia de empaque
para transporte` como su falso positivo por su nombre**. **QUE SE HACE CON ELLO: NADA AL DATASET.**
No se toca la tabla, no se toca una grafia, no se toca `OPERACIONES.jsonl`. Se corrige la cifra **por
adicion y sin borrar el texto viejo** (`EJECUTOR.md` 8), y la pregunta de fondo (una tabla canonica
que hornea titulos recortados) queda registrada para quien cierre la fase 08. **No hace falta
doctrina nueva: la regla de correccion por adicion ya existe y la unidad ya estaba adjudicada en la
131.**

**3.15, RESPUESTA A SU PREGUNTA 2, EL UMBRAL: TIENE NUMERO, Y SON DOS.** `scripts/intra_dominio.py`
lineas 60 y 68: **`UMBRAL_TITULO = 80`** (token_sort_ratio de rapidfuzz) y **`UMBRAL_SEMANTICO =
0.78`**, este ultimo con su calibracion escrita encima. Es el umbral **del cribado intra**, que es
literalmente lo que la ficha de `OP-A-02` manda usar. **La puerta semantica SI se puede cablear, y el
bloqueo que la PREGUNTA 2 declara no existe.** Y la frase que lo declaraba es su caida 4.2.

**3.16, LA MITAD SEMANTICA DE LA ENTRADA 3 (su pendiente de doctrina 7.1): NO ES PARADA HOY, Y DIGO
HASTA CUANDO.** `AUDITOR.md` 3 dice que una operacion cuyo texto no alcance para ejecutarse sin
decidir es PARADA. **Aqui no hubo decision improvisada**: instalo la mitad mecanica, dejo la otra sin
instalar, la escribio en el codigo, en la vara y en el reporte, y **no movio `estado`**. Eso es
`EJECUTOR.md` 11 y el criterio de HECHO de la fase 08 aplicados, no doctrina nueva. **LA FRONTERA,
PARA QUE NO SE ARRASTRE EN SILENCIO: el dia que la fase 07 intente CERRARSE con esa mitad sin
resolver, eso SI es PARADA de decision de fundador**, porque cerrar una fase con una verificacion
inejecutable cambia el criterio de HECHO. Hoy la fase no cierra por otra razon (A2.6), asi que la
pregunta no vence todavia.

**3.17, LA CIFRA DE `A1.3` EN LA VARA: SE PARTE EN DOS.** Un control instalado a medias no puede
publicarse con el mismo rotulo que uno entero, por la misma razon de unidades de mi 3.9 de la 144.
La vara tiene que decir `INSTALADO EN SU MITAD MECANICA` y el recuento tiene que publicar **las dos
cifras**, no una.

**3.18, RESPUESTA A SU PREGUNTA 3, NUEVE CONTROLES O SIETE: LAS DOS, Y LAS DOS EN LA SALIDA.** El
nueve es la unidad DECLARADA (cada ficha declara los suyos y la vara no puede desobedecer a las
fichas) y el siete es la unidad DISTINTA (A1.1 con A2.3, y A1.2 con A2.4, son el mismo control con
dos nombres). **Ninguna es falsa y publicar solo una esconde la otra.** La vara imprime las dos
lineas, con las dos parejas nombradas. Es la misma doctrina de las dos unidades de arista de la 145:
**el rotulo se gana midiendo, no eligiendo.**

## 4. CAIDAS, CON NOMBRE, LAS SUYAS, LAS DE LA CASA Y LAS MIAS

**4.1. DEL EJECUTOR, DE CIFRA PUBLICADA, Y ACUMULA. EL "OCHO" DE LAS GRAFIAS DE 31, QUE CONTRADICE
SU PROPIA ENUMERACION.** La CORRECCION 24.c y la 3.f del reporte publican *"ocho de ellas estan
VIVAS y son CANONICAS de la tabla de `OP-S-11`"* y **enumeran SIETE nombres en la misma frase**.
Medido por mi por tres caminos independientes: **SIETE** por su unidad y **SEIS** por el detector
vigente. **VIVE EN `docs/plan/CORRECCIONES_A_APLICAR.md`**, o sea en `docs/plan/`, asi que por la
letra de la seccion 4 **es CAIDA DE CIFRA PUBLICADA y no de reporte**: la racha pasa de **CERO a
UNO**. Y **CAE FUERA DE LOS TRECE DISCUTIBLES**: ninguno cubre el censo de la truncacion. Por la
regla del credito de la seccion 1.2, **BAJA EL CREDITO DE TODA LA TANDA y ese tramo se relee al
doble**, y va escrito en el encargo. **Lo que NO es: no mueve un nodo, no mueve una arista, no mueve
una ficha. El hallazgo de fondo es correcto y valioso; lo que falla es la cuenta y la unidad.**

**4.2. DEL EJECUTOR, DE REPORTE, Y ACUMULA. "EL UMBRAL DE LA COLA NO TIENE NUMERO EN NINGUNA
PARTE".** Vive en la **cabecera de la PREGUNTA 2** y en su conclusion (*"Sin ese numero la puerta
semantica no se puede cablear"*), asi que por la letra afinada del 27 ago **ACUMULA**. Es **la misma
especie que la caida 4.1 de la 145**: una busqueda negativa publicada como hecho y usada para
bloquear trabajo. **Y cae DENTRO de su discutible 9**, que nombra la 3.e y nombra que la ausencia
descansa entera en la pierna por contenido: **por la regla del marcado, NO baja el credito de la
tanda.** **RACHA DE REPORTE: DE DOS A TRES. Especie corriendo: DOS.** Dispara relectura al doble del
tramo de la 3.e, como toda caida de reporte.

**4.3. DE LA CASA, DOS, LAS DOS DE GUARDA QUE NO ALCANZA.** (a) **El vocabulario de doce formulas
tiene un agujero medido**: seis escapes en la pagina que la anuncia, cinco sin barrido en ventana.
(b) **Un barrido puede traer el sello completo y una pierna POR CONTENIDO de nombres adivinados**, y
entonces el sello certifica el metodo exacto que la CORRECCION 23 prohibe, un nivel mas abajo. **Las
dos son el hueco que el encargo de abajo tapa.** No son caidas del ejecutor: el encargo le dejo
elegir el vocabulario y el sello no pedia nada sobre los patrones.

**4.4. MIAS, DOS.** (a) **DE ENCARGO: escribi *"tu vara tiene que pasar de TRES a CUATRO instalados
y mordiendo, y ESA es la cifra que publicas"*, y el cuatro no salia de ningun instrumento**; ni
siquiera era coherente con mi propia 3.c, que sola mueve dos casillas. Es la misma especie que mis
4.3 y 4.4 de la 145: **anticipar una cifra y mandar publicarla**. (b) **DE PROCEDIMIENTO: corri
`run_phase1.py` fuera del orden del ciclo DOS veces hoy** y me saco dos falsos rojos (71 divergentes,
y despues un numstat de 72/72), exactamente la trampa que yo mismo le avise por escrito y que el
declaro en su 5.1. **Cerre el ciclo en su orden, volvio a OK y el arbol quedo limpio, y lo escribo en
vez de callarlo.**

## 5. METRICA DE CREDITO ACUMULADA

**Esta tanda: CERO relecturas de par que muevan el marcador.** El campo `estado` esta congelado,
`INTRA_DOMINIO_VEREDICTOS.jsonl` no se toco y esta vuelta no lee pares. **De los TRECE discutibles
marcados, los TRECE adjudicados: LOS TRECE A FAVOR** (con reserva en el 3, el 5, el 8, el 9 y el 12),
**y en uno de ellos me corrige a mi con razon medida** (el 1, la cifra de la vara).

**LA REGLA DEL CREDITO, APLICADA CON SU LETRA.** **Hay una discrepancia FUERA de lo marcado: la
4.1.** Por la seccion 1.2, **BAJA EL CREDITO DE TODA LA TANDA** y el tramo se relee al doble. La 4.2
cae DENTRO del discutible 9 y **no** lo baja. **Lo digo en el acta como manda la regla.**

**Caidas del ejecutor: UNA de cifra publicada (4.1, ACUMULA), UNA de reporte (4.2, ACUMULA) y UNA de
procedimiento (declarada por el en su 5.1). De la casa: DOS (4.3.a y 4.3.b). Del auditor: DOS (4.4.a
de encargo y 4.4.b de procedimiento).**

**Acumulado:** **859 relecturas** (sin cambio), **912 puestos** (sin cambio), **12 caidas de clase
del ejecutor** (sin cambio), **91 de reporte del ejecutor** (90 mas la 4.2), **21 de cifra publicada
del ejecutor** (20 mas la 4.1), **22 de expediente** (sin cambio), **22 de incumplimiento de encargo**
(sin cambio), **8 de procedimiento del ejecutor** (7 mas la suya declarada), **16 de cifra del
auditor** (sin cambio), **20 de acta del auditor** (sin cambio), **37 de procedimiento del auditor**
(36 mas la 4.4.b), **1 de reporte del auditor** (sin cambio), **55 de encargo del auditor** (54 mas
la 4.4.a), **2 de clase del auditor** (sin cambio), y **5 vueltas no entregadas enteras** (sin
cambio: **la 146 SE ENTREGO ENTERA**, las cinco tareas con su cierre, su 4.e y sus cuatro
correcciones declaradas dentro de la propia vuelta). **POR ESPECIE, Y ESTO NO SUMA DOS VECES AL
TOTAL: 9 de guarda envejecida** (sin cambio) y **41 de guarda que no alcanza o cegada** (39 mas las
dos de la 4.3).

**RACHAS:**

> **CLASE O CIFRA PUBLICADA DEL EJECUTOR: DE CERO A UNO**, por la 4.1, que vive en
> `docs/plan/CORRECCIONES_A_APLICAR.md`. **La regla dice DOS TANDAS SEGUIDAS: PARADA.** Esta es UNA.
> **La vuelta 147 no puede permitirse otra**, y el encargo la ataca de frente con la relectura al
> doble del tramo y la correccion por adicion.
>
> **REPORTE: DE DOS A TRES**, por la 4.2. **Y AQUI HAY QUE LEER LA LETRA CON CUIDADO, PORQUE DECIDE
> SI EL BUCLE SIGUE.** La regla no dice "tres acumuladas: parada"; dice **"TRES SEGUIDAS DE LA MISMA
> ESPECIE: PARADA"**. Las tres que acumulan son: la 144 (**la cuenta de filas de una tabla**), la 145
> (**una busqueda negativa publicada como hecho**) y la 146 (**una busqueda negativa publicada como
> hecho**). **La 144 es de OTRA especie**, y el acta 145 ya lo dejo escrito. **La racha de MISMA
> ESPECIE va en DOS, no en tres: NO ES PARADA.** Lo digo con todas sus letras porque esta a una
> vuelta: **una tercera busqueda negativa publicada como hecho ES PARADA AUTOMATICA**, y va escrito
> en el encargo para que el ejecutor lo sepa antes de escribir.
>
> **Y `AUDITOR.md` 1.2 ME OBLIGA OTRA VEZ, PORQUE LA RACHA SIGUE EN DOS O MAS.** La escalada que
> encargue en la 145 **esta construida, entra en `VIEJAS` y muerde sobre el texto que fallo**: eso lo
> verifique yo. **Y NO ALCANZO**, y lo se porque la caida de hoy paso por delante de ella. Asi que
> **encargo la escalada de la escalada EN ESTE MISMO ACTA, como TAREA BLOQUEANTE de la 147**, sin
> esperar parada ni decision nueva: **el vocabulario ampliado con mi medicion delante, y la pierna
> POR CONTENIDO de los barridos obligada a no ser una lista de nombres adivinados.** No es doctrina
> nueva: es la CORRECCION 23 aplicada al instrumento que la hace cumplir.

## 6. CONDICIONES DE PARADA, REPASADAS UNA A UNA

**NINGUNA SE CUMPLE, Y LO DIGO CON SU NOMBRE.** **Doctrina NUEVA: NO.** Las cinco cosas que hoy
pedian regla se adjudican por extension citable y estan arriba: la unidad de la truncacion por el
detector registrado en la 131 (3.14); la correccion de la cifra por adicion por `EJECUTOR.md` 8
(3.14); el umbral por el texto literal de la ficha mas el fichero del cribado intra (3.15); la mitad
semantica de la entrada 3 por `EJECUTOR.md` 11 y el criterio de HECHO de la fase 08 (3.16, con su
frontera escrita); y la cola de veredicto de la vara por la doctrina de la cifra tallada (3.11).
**Contradiccion con regla vigente o cifra publicada que no se resuelva con las reglas de correccion
existentes: NO.** La cifra falsa de la 4.1 **se resuelve con la regla que ya existe**: declarar por
adicion con la medicion nueva y su unidad, sin borrar el texto viejo. Va como CORRECCION 25.
**Decision de fundador: NO**; la vuelta 147 corrige una cifra, amplia dos guardas y cablea una puerta
que su propia ficha manda cablear: no borra contenido que ninguna regla ordene, no cambia el alcance,
no gasta fuera del repo, no toca produccion y no funde ramas. **Fallo tecnico repetido: NO**; Gate 0,
las suites y el hook estan VERDES hoy corridos por mi, y lo estuvieron en la 143, la 144, la 145 y la
146. **Y no queda ninguna guarda en rojo**: las cuatro del cierre, la de apertura, la nueva de
ausencias y la bateria `VIEJAS` con sus veinte me salen todas verdes, asi que **el MODO DE EJECUCION
CONTINUA sigue vigente**. **Credito de tanda roto: NO, Y POR UN PELO**; cifra publicada en UNO (la
parada es a DOS) y reporte en TRES pero con la misma especie corriendo en DOS (la parada es a TRES de
la misma especie). **Cierre de la fase 03 y de la fase 05: CUMPLIDAS** y citables, no reabiertas.
**Cierre de la fase 06: no existe condicion de parada escrita para el**, releida hoy la seccion 4
entera. **Campana consumada: NO**; la fase 07 tiene `OP-A-01` a medias y `OP-A-02` entera por delante,
y `OP-S-12` sigue al final de la pasada por la atadura 2. **Credenciales: NO** aplica.
**`PROMPT_SIGUIENTE.md` va escrito. NO se escribe `PARA_ALEXIS.md`.**

## 7. LO QUE ENTREGO COMO ENCARGO

**TAREA 1**, los registros: R.28 con estas dieciocho adjudicaciones y estas caidas, la **CORRECCION
25** (la cifra de las grafias de 31, corregida por adicion y con las DOS unidades escritas) y la
**CORRECCION 26** (el umbral existe, con su fichero, su linea y su motivo, y la frase que lo negaba
citada y no escondida). **TAREA 2, BLOQUEANTE, LA ESCALADA DE LA ESCALADA** por `AUDITOR.md` 1.2:
ampliar el vocabulario con la familia que yo medi, y **obligar a que la pierna POR CONTENIDO de un
barrido no sea una lista de identificadores adivinados**, con su caso rojo por mutacion **sobre el
barrido del umbral de esta misma vuelta**, que tiene que salir ROJO. **TAREA 3**, el trabajo: **la
3.f releida al doble** (es lo que la caida fuera de lo marcado obliga), la vara partida en sus dos
unidades y su `A1.3` con el rotulo honesto, la guarda de la nomina que impide re-sellarla en
silencio, y **cablear `A2.6`, la puerta semantica, ahora que el umbral tiene numero**. **TAREA 4**,
el cierre entero con su 4.d y su 4.e.
