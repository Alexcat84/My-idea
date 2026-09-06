## 3. LO QUE ESTA VUELTA SOSTIENE, Y NI UNA PALABRA MAS

**LAS CINCO TAREAS CERRARON Y NINGUN VEREDICTO DEL ARCHIVO SE MOVIO.**
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y cierra en **4054129 bytes en disco y
4054129 bytes normalizados a LF**, `sha256` LF `0a77b5a35a962621`, medido en el
bloque de apertura, en los dos instrumentos de la TAREA 2 y otra vez al cierre.

**LO QUE SOSTENGO, UNO A UNO:**

1. **El acta 192 entra como `R.54`**, con el numero computado por
   `serie_de_registros.py` y no tecleado, y **el registrador aprendio tres cosas
   que ninguna maquina heredada sabia leer**. La que importa: **el ejecutor
   declara sus caidas EN RANGO** (`` `C.1` a `C.6` ``), y contar claves distintas
   **da 2 donde el acta declara 6**. Ninguna guarda heredada caza esa cifra falsa,
   porque las dos claves existen de verdad.
2. **La relectura al doble salio MAL PARA MI, y esa es la cifra que cuenta:** 20
   coinciden, 10 discrepan, y **TRES caen FUERA de mis quince dudosos**. Las tres
   son la misma especie: **conte solape de pasos donde la vara de la casa pregunta
   si uno es una LINEA del otro desplegada en PROCEDIMIENTO.**
3. **Los dos `SUJETO VIVO` estan arreglados por carriles distintos**, porque no
   eran el mismo caso: uno era **falso positivo** y el otro **tiene el sujeto vivo
   de verdad y declararlo congelado habria sido mentir**.
4. **La cuarta puerta existe**, y **el arnes de la nomina sobre ese mismo fichero
   sigue reproduciendo byte a byte** (4982 bytes en disco y 4982 en LF, `sha256`
   LF `ce85fd0cc659774c`, antes y despues).
5. **El formato unico existe, ya se uso**, y **recupera exactamente los tres
   cotejos que el acta nombraba** como dejados fuera por formato.

**Y LO QUE NO SOSTENGO, DICHO IGUAL DE FUERTE:** no sostengo que los dos `SUJETO
VIVO` amenazaran la bateria de la 194, **porque medi que no entran en la nomina**;
no sostengo ninguna conclusion sobre la marca contra la dificultad, **porque el
encargo prohibe re medirla aqui**; y no sostengo que mi criterio de lectura sea
el bueno: **medi que en 3 de 30 no lo es.**

## 4. EL ESTADO DEL ARBOL, LEIDO DE LA APERTURA SELLADA Y NO TECLEADO

**LAS CIFRAS DE ESTA SECCION SALEN DE `docs/loop/SALIDA_V192_APERTURA.txt`**, que
se escribio **antes de la primera operacion**, y no de lo que yo recuerde.

- El arbol abrio con **`git status --porcelain`** en **1** linea, y es
  **`?? scripts/loop/vuelta192_apertura.py`**: **el propio bloque de apertura**,
  todavia sin seguir por git cuando su bloque `C` corrio. **`CIFRA ficheros no
  seguidos: 1`**, ese mismo.
- **`git diff --numstat -- dataset/` AL ENTRAR: 0 filas.** **AL SALIR: 0 filas**,
  medido por el paso 4 del ciclo del bloque de cierre. **Las dos cifras se
  publican**, y `dataset/` no se toco a mano en ningun momento.
- **HEAD real de apertura: `485c2f3e`**, sellado en
  `docs/loop/SALIDA_V192_HEAD_APERTURA.txt` **antes de la primera operacion**, y
  es el commit del acta 192.
- **EL DESFASE DEL CALIBRADO SE MIDIO EN LA APERTURA**, dentro de su bloque y
  **antes de la primera operacion**: **4 filas sobre 468 del calibrado**, las
  mismas que al cierre. **Una columna de apertura medida al cierre es caida que
  acumula**, y por eso se midio donde toca.

**LAS CIFRAS DEL ENCARGO, COMPROBADAS UNA A UNA CONTRA EL INSTRUMENTO Y NO
COPIADAS.** El bloque de apertura las computa todas y publica LAS DOS cuando
discrepan:

| lo que el encargo dice | lo que el instrumento midio | |
|---|---|---|
| el siguiente libre de la serie es `R.54` | `R.54`, con 45 entradas, 0 colisiones y 0 huecos | CALZA |
| son DIEZ adjudicaciones `4.1` a `4.10` | 10 claves con el patron suelto; 0 con el entrecomillado | CALZA |
| las diez van A FAVOR y ninguna EN CONTRA | 7 discutibles, los 7 A FAVOR, 0 EN CONTRA; y 3 preguntas contestadas con marcas nuevas | CALZA en el fondo, y el reparto se publica |
| son TRES los hallazgos de la seccion 5 | 3 claves `5.n` | CALZA |
| DOS caidas propias del auditor, una de cifra publicada | 2, con 0 huerfanas, y la especie leida del parrafo: `C.1` de cifra publicada, `C.2` de metodo | CALZA |
| SEIS caidas del ejecutor, de metodo | 6, **expandiendo el rango** `` `C.1` a `C.6` ``; contando claves distintas darian 2 | CALZA, y las dos cifras se publican |
| en el reporte de la 191 el `D.7` va antes del `D.6` | CALZA por la vara del titulo del discutible; NO CALZA por la de la mencion suelta, y las dos se publican | CALZA por la que responde |
| el tramo de la TAREA 2 son 30 puestos y el 2832 esta dentro | 30, y el 2832 DENTRO | CALZA |
| son los mismos 30 que el auditor releyo | diferencia simetrica 0 | CALZA |
| 471 consumidos por la 191, 501 con su tanda | 471 y 501, contados de sus seis ficheros | CALZA |
| el archivo cierra en `0a77b5a35a962621` | identico, y por las dos convenciones | CALZA |
| la guarda da `sujeto_vivo 2` y `sin_motivo 6` sobre los doce | 2 y 6 en la apertura, antes de tocar nada | CALZA |
| los dos `SUJETO VIVO` **entran en la nomina a la vuelta siguiente** | **NO ENTRAN**: la regla de entrada exige `mutacion`, `caso_positivo` o `simular` en el NOMBRE, y de los DOCE el censo ve TRES, ninguno de ellos con sujeto vivo | **NO CALZA, y va como correccion declarada** |
| el sello del auditor: disco 1145 bytes y LF 1145 bytes, ciega disco 41952 bytes y LF 41952 bytes, destape disco 33884 bytes y LF 33884 bytes | identicos, y sus dos `sha256` CALZAN contra el sello | CALZA |
| SEIS vueltas seguidas cierran su propio reporte (186 a 191) | **SIETE** (185 a 191), contadas del inventario entero por `vuelta192_racha_de_cierres.py`; el acta 191 venia contando CINCO | **NO CALZA, y las cuatro cifras se publican** |

## 5. LAS CORRECCIONES DECLARADAS DE ESTA VUELTA

**NINGUNA BORRA LO QUE CORRIGE**, que es la regla (`EJECUTOR.md` 8).

**5.1 CONTRA EL ACTA 192: LOS DOS `SUJETO VIVO` NO ENTRAN EN LA NOMINA.** El
titulo del hallazgo `5.1` dice que *"ENTRAN EN LA NOMINA DE LA BATERIA A LA VUELTA
SIGUIENTE"*, y el encargo hace bloqueante la tarea *"por la bateria de la 194"*.
**Medido con la regla del propio fichero**, `VMV.PATRON_ARNES`: de los DOCE
ficheros de la 191, **el censo ve TRES**, `arneses_que_faltan()` **reclama esos
TRES**, y **con `SUJETO VIVO` y reclamados: CERO**. **La cifra vieja se queda donde
esta.** Lo que NO cambia: **la medicion de `2` y `6` del auditor era correcta**, y
el arreglo se hizo igual porque la `4.4` del acta 191 dice que `SUJETO VIVO` es
FALLO.

**5.2 CONTRA MI PROPIO SELLO DE APERTURA: LA RACHA DE CIERRES.** El bloque `B.2`
de mi apertura publico **racha 7** mirando una **VENTANA TECLEADA** de 185 a 191:
**esa cifra es el borde de mi ventana y no la racha**. Lo cace antes de publicarlo
y escribi `scripts/loop/vuelta192_racha_de_cierres.py`, que cuenta del
**inventario entero**: **10 ficheros de cierre en disco, 9 en verde, racha seguida
de 7 (185 a 191), cortada por la 184**, que tiene fichero y no trae la linea de
piezas. **Las cuatro cifras se publican juntas**: 5 del acta 191, 6 del encargo, 7
de mi ventana, 7 del inventario. Que la ventana acertara por casualidad no la hace
una medicion.

**5.3 CONTRA MI PRIMER PARCHE DE LA TAREA 3, CAZADA SIMULANDO.** Mi primer parche
usaba `replace(..., 1)` y el registrador tiene **la misma linea DOS veces**; con
una sola aparicion sin marca, `motivo_del_sujeto_vivo()` devuelve False para el
fichero entero. **Lo enseño el modo `--simular`, que corre antes de escribir**, y
`insertar_motivos()` pasa a ir linea a linea sobre todas las apariciones.
**Ninguna cifra falsa llego a publicarse.**

**5.4 CONTRA MI PRIMERA CORRIDA DEL LECTOR DE COTEJOS VIEJOS.**
`_auditor_v191_cotejo_ciega.txt` salia con **39 filas y denominador 30**, que es
imposible. Causa medida: **ese fichero lista cada discrepancia DOS VECES**, 9
duplicadas sobre 30 puestos distintos. Se anadio `deduplicar()`, **que cuenta
cuantas quita**, y un aviso que publica cualquier fichero con mas filas que
denominador. **Se cazo mirando la salida antes de pegarla en el reporte.**

**5.5 SOBRE EL ORDINAL DEL DESFASE DE `PATRONES_ACTA`.** El reporte de la 191 se
llama a si mismo **la SEPTIMA vuelta** del desfase. **Esa palabra no sale de
ningun instrumento**, asi que no la copio ni le sumo uno a ojo: lo que si se puede
contar es que **3 reportes archivados traen el literal `DESFASE DECLARADO`** (189,
190 y 191). **Las dos cifras van publicadas en la seccion 0 y la discrepancia se
declara en vez de resolverse copiando.**

## 6. PENDIENTES DE DOCTRINA

**NINGUNO NUEVO.** Las cinco tareas se resolvieron con reglas vigentes, y donde
hizo falta una decision que no me toca **la traigo como pregunta en la seccion 7
en vez de inventar la regla**.

## 7. LAS PREGUNTAS QUE TRAIGO

**`P.1` LA ESCALADA DE MI PROPIA TANDA, QUE NO ME AUTO ENCARGO.** La TAREA 2 dio
**TRES discrepancias FUERA de mis dudosos**, no una. `AUDITOR.md` 1.2 dice que eso
baja el credito de toda la tanda y que el tramo se relee al doble, **y la `4.5`
del acta 192 acaba de adjudicar por segunda vez que el doble esta en la mano del
auditor y no en la mia**. Lo traigo medido, con sus numeros y sus nombres. **La
pregunta es si tres de una vez cambia algo del regimen, o si es el mismo doble de
siempre.**

**`P.2` LOS DOS `NO DECIDIBLE SIN MOTIVO` QUE SI ENTRAN EN LA NOMINA.**
`vuelta191_tarea3_mutacion_lineas.py` corre `wc -l` sobre `LECTURAS_DIRIGIDAS.md`
viva, y `vuelta191_tarea6_mutacion_bloque_tallado.py` **abre `docs/loop/REPORTE.md`
vivo** y se lo pasa a `--comparar`. **Son los que de verdad pueden no reproducir
en la 194**, y el auditor ya vio a uno de ellos no reproducir. **El encargo me
prohibe arreglarlos a ciegas y no los toco.** La pregunta es si se les escribe el
motivo (deuda declarada) o si se les congela el sujeto, **que es una decision
sobre lo que esos arneses tienen que probar y no una decision mia**.

**`P.3` LA VARA CON LA QUE LEO.** Mis tres discrepancias de fuera del marcado
salen todas de contar **solape de pasos**, y la vara de la casa (`9.6.1`) pregunta
**si uno es una LINEA del otro desplegada en PROCEDIMIENTO**. **No cambio mi
criterio a mitad de camino y no lo cambio ahora**, porque cambiarlo despues de ver
el resultado es lo que la `4.4` del acta 192 acaba de adjudicar como trampa. **La
pregunta es si el criterio escrito para las ciegas debe pasar a ser el del banco,
y quien lo decide.**

## 8. LAS CAIDAS PROPIAS DE ESTA VUELTA, LO QUE QUEDA EN ROJO, Y LOS DISCUTIBLES

**CAIDAS PROPIAS: CUATRO, LAS CUATRO DE METODO Y NINGUNA LLEGO A PUBLICAR UNA
CIFRA FALSA.** Van con su clave y su cabecera, que es la forma de la casa, y las
tres primeras remiten a la correccion declarada que las repara en la seccion 5.
**TRES LAS CACE YO Y LA CUARTA ME LA CAZO LA MAQUINA**, y esa diferencia se dice
en vez de difuminarse. **Cero caidas de cifra publicada y cero rutas vacias.**

**`C.1`. MEDI UNA RACHA SOBRE UNA VENTANA QUE TECLEE YO.** El bloque `B.2` de mi
sello de apertura publico **racha 7** mirando de la 185 a la 191, **y esa ventana
la escribi a mano**: una racha que se corta justo donde acaba la ventana que uno
eligio no es una medicion de la racha. **La cazo yo mirando el inventario de disco
antes de publicar el reporte**, y la reparacion es
`scripts/loop/vuelta192_racha_de_cierres.py`, que cuenta del inventario entero.
Correccion declarada `5.2`. **De metodo: la cifra final no cambio, pero pudo
haber cambiado y yo no lo habria sabido.**

**`C.2`. PARCHEE CON `replace(..., 1)` UN FICHERO QUE TENIA LA LINEA DOS VECES.**
El registrador de la 191 repite la misma linea de `p.append`, y con una sola
aparicion sin marca `motivo_del_sujeto_vivo()` devuelve False para el fichero
entero. **La cazo el modo `--simular`, que corre antes de escribir**, y la
reparacion es `insertar_motivos()`, que va linea a linea sobre todas las
apariciones y es idempotente. Correccion declarada `5.3`. **De metodo: nada llego
al disco mal.**

**`C.3`. MI LECTOR DE COTEJOS VIEJOS SACO 39 FILAS SOBRE UN DENOMINADOR DE 30.**
Es imposible por construccion y lo era por una causa medible: ese fichero lista
cada discrepancia dos veces. **La cazo yo leyendo la salida antes de pegarla en el
reporte**, y la reparacion es `deduplicar()`, que ademas CUENTA cuantas quita.
Correccion declarada `5.4`. **De metodo: la cifra falsa no salio de la salida del
instrumento.**

**`C.4`. PUBLIQUE DOS PARES DE BYTES DE ANTES EN PROSA, AL LADO DE SU RUTA, Y
ESTA ME LA CAZO LA MAQUINA Y NO YO.** La TAREA 1 escribia `998216 / 998216` cerca
de `SALIDA_V192_T1A_RECORRIDO_SIN_ESCRIBIR.txt`, y la TAREA 4 escribia
`14724 / 14724` como el ANTES de `apertura_del_auditor.py`. **Las dos cifras eran
CIERTAS y la guarda tiene razon igual:** una pareja de bytes en prosa, junto a una
ruta, se lee como una afirmacion sobre esa ruta HOY, y hoy esos ficheros miden
otra cosa. **`cerrar_reporte.py` se nego a escribir el reporte hasta que las
arregle**, con las cuatro parejas nombradas y su linea. El remedio es el que la
casa ya tiene para las citas: **la cerca**, que es lo que esas dos cifras son.
**Ninguna cifra se borro: se movieron a su bloque cercado con su procedencia.**
**Es la misma especie que la `C.6` del reporte de la 191, y la anoto asi: la
guarda que existe para cazar esto lo cazo, que es exactamente para lo que se
construyo.**

**LO QUE QUEDA EN ROJO: NADA EN ROJO, Y UNA COSA EN AMBAR QUE SE DECLARA.** La
guarda de entrada a la nomina sale **VERDE CON DEUDA DECLARADA**, que no es verde
a secas: **2 de los 3 arneses que entran traen un sujeto vivo sin motivo
escrito**. Va como `P.2`.

**LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO:**

**`D.1` (DE VARA). EL NUMERAL DE LA FILA DECIDE CUANTOS HALLAZGOS CUENTAN FUERA,
Y ESTA VEZ EL COTEJO POR SUBCADENA RESUELVE CERO DE TRES.** La fila del acta dice
**3** y la seccion tiene **3** claves `5.n`, asi que calzan; pero las tres piezas
del parentesis (*2832*, *dos arneses de sujeto vivo*, *cuarta puerta del sello*)
**no aparecen dentro de ninguno de los tres titulos**. **Acepte el numeral igual**,
que es lo que la `4.1` del acta 192 adjudico A FAVOR hace una vuelta. **Lo marco
porque el 3 pudo salir de una coincidencia**: la fila nombra el `2832`, que no es
un `5.n`, y no nombra el `5.3`.

**`D.2` (DE CRITERIO, Y ES EL QUE MAS ME PESA). NO CAMBIE MI CRITERIO DE LECTURA
AUNQUE ME TUMBO TRES VECES.** Mis clases se escribieron con el mismo literal de la
190 y la 191, y **las tres discrepancias de fuera del marcado salen de contar
solape de pasos**. Pude reescribirlo despues del destape y **no lo hice**, porque
un criterio que se ensancha despues de ver el resultado no mide nada. **Lo marco
porque la alternativa (adoptar la vara `9.6.1` para las ciegas) puede ser lo
correcto y yo no lo adjudico.**

**`D.3` (DE ALCANCE). ESCRIBI LA PIEZA `a` DE LA TAREA 5 ANTES DE LA TAREA 5, Y LA
USE EN LA TAREA 2.** El formato unico se escribio cuando la TAREA 2 necesitaba un
cotejo, y esa tarea es su primer usuario. **Lo defiendo asi: una plantilla que
nadie ha corrido no esta probada, y usarla en la tarea que la necesitaba es la
prueba mas barata que hay.** **Lo marco porque adelanta una pieza de una tarea
posterior**, y quien lea el orden de los commits lo vera.

**`D.4` (DE ALCANCE). TOQUE `apertura_del_auditor.py`, QUE UNA ENTRADA DE LA
NOMINA NOMBRA, ANTES DE LA BATERIA DE LA 194.** Es exactamente el riesgo que la
`4.7` del acta 192 usa para dejar `tallar_cabecera_reporte.py` fuera de esta
vuelta. **Lo hice porque el encargo lo pide con esas palabras**, y **lo comprobe en
vez de confiar**: re corri el arnes con el parche puesto y su salida sellada
reproduce byte a byte. **Lo marco porque la comprobacion la elegi yo y podia
haberme salido mal.**

**`D.5` (DE ALCANCE). PUSE LA GUARDA NUEVA EN UN FICHERO PROPIO EN VEZ DE DENTRO
DE `verificar_mutaciones_viejas.py`.** La razon esta medida (**42 entradas de la
nomina lo nombran**) y es la misma que la `4.7`. **Lo marco porque el precio es una
guarda mas que hay que acordarse de correr**, y esta casa sabe lo que le pasa a lo
que hay que acordarse de correr.

**`D.6` (DE FONDO). LE ANADI A UN INSTRUMENTO DE UNA VUELTA CERRADA UNA LINEA QUE
CAMBIA SU SALIDA.** `vuelta191_tarea1a_registrar_acta191.py` ahora publica el
`sha256` del acta que lee, y **eso no es solo un comentario: es comportamiento**.
Lo hice porque **una huella de congelado falsa habria sido peor**, y porque la
`4.3` del acta 192 adjudico A FAVOR tocar codigo de vueltas cerradas mientras no
se reescriba una cifra publicada ni una salida de la nomina. **Lo marco porque es
lo mas invasivo que hice, y porque no lo corri: el anclaje se decidio leyendo el
texto, y correrlo habria pisado una salida sellada de la 191.**

**`D.7` (DE UNIVERSO). MI LECTOR DE COTEJOS VIEJOS SACA A UNO DE LOS SEIS QUE
ENTRABAN.** `_auditor_v155_cotejo_t3.txt` sale porque exijo **las dos clases Y el
denominador**. **Lo defiendo asi: un criterio mas estrecho que ademas sube la
cifra dice algo; uno mas ancho no diria nada.** **Lo marco porque el universo
cambio de forma y no solo de tamano**, y quien mida la marca contra la dificultad
sobre el universo nuevo estara midiendo sobre otro conjunto.
