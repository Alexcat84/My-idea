Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

ANTES DE ESA PRIMERA LINEA, CORRE LA GUARDA QUE TU MISMO CONSTRUISTE:
`python scripts/loop/guarda_commit_dataset.py`. Si sale ROJO, NO COMMITEES:
restaura `dataset/` contra HEAD, declara la restauracion con su medicion, y
solo entonces sigue. Yo la corri al cerrar mi auditoria y salio VERDE, con 0
filas de `numstat` y 0 blobs divergentes, despues de haber corrido el ciclo
entero de Gate 0. El arbol te llega limpio.

EL TOPE VUELVE A CINCO SUB-TAREAS, Y NO LO DECIDO YO: LO DISPARO TU VUELTA.
`AUDITOR.md` 6.2 dice que el regimen de dos sub-tareas dura HASTA QUE DOS
VUELTAS SEGUIDAS CIERREN SU PROPIO REPORTE con `cerrar_reporte.py`. Lo medi en
git: la 176 cerro en `27b80563` y archivo en `8c176390`; la 177 cerro en
`b9c2f01d` y archivo en `1d29275c`. DOS SEGUIDAS. El tope vuelve a CINCO por la
propia letra de la 6.2, sin que nadie tenga que decidirlo, y este encargo trae
cinco. El regimen temporal queda CUMPLIDO Y CITABLE, no borrado.

LA CADENCIA NO CAMBIA: LA PROXIMA VUELTA DE BATERIA SIGUE SIENDO LA 181. Esta,
la 179 y la 180 cierran su seccion 9 con el HUECO DECLARADO Y MEDIDO, con su
nombre, sus bytes medidos y su atribucion, las tres juntas. La 177 lo hizo bien
y te vale de modelo.

LO QUE VERIFIQUE DE TU VUELTA 177, DICHO PARA QUE SEPAS SOBRE QUE PISAS, Y
TODO CORRIDO POR MI: el ciclo entero de Gate 0 en su orden (`run_phase1` OK
exit 0, numstat 0 filas, motor 25/25, tsc exit 0, web 82 y 1.040); el marcador
3.388 con A 551, B 72, C 5, D 2.760, puestos de 1 a 3.388, cero huecos y cero
duplicados; la cabecera COTEJADA contra el tallador, 11 filas, 0 distintas y 0
ausentes; los 7 commits en su orden, las 42 rutas repartidas 24, 17 y 1, y el
grafo con 0 filas entre los dos sellos; las 69 rutas que nombras, TODAS
existen y NINGUNA mide cero bytes salvo el hueco que declaras; los SEIS arneses
corridos bajo mi mano con sus cifras exactas (20/20, 8/8, 28/28, 24/24, 25/25 y
los 35 del viejo); los dos sha256 de veredictos y operaciones identicos antes y
despues; el universo de `OP-L-03` en 40 actos y 73 pares; y la disolucion
verificada por los DOS caminos, que calzan en los seis actos. TU HALLAZGO ES
REAL Y ES LO MEJOR DE LA VUELTA.

Y TE DIGO LAS TRES COSAS QUE ADJUDIQUE A TU FAVOR CONTRA MI PROPIO ENCARGO: mi
encargo nombraba mal el mayor del reparto (lo lei de la `evidencia` al corte
2117 en vez de la `nota` al 3.388), y ademas te mandaba empezar por un acto que
esta DISUELTO; tenias razon en hacer los SEIS grandes; y tenias razon en no
mover ningun veredicto. Las tres estan escritas en mi acta con mi nombre en
ellas.

TU UNICA CAIDA CONTRA TI ES DE REPORTE Y NO ACUMULA, Y ES DE CONTEO. Publicas
que "el censo ve 153 arneses" y que "los 2 de la 177 no lo eran... la nomina va
de 89 a 92". Medido por mi: el censo ve **154** (y tu propia cuenta se delata,
porque 153 menos 92 son 61 y no los 62 que publicas, mientras que 154 menos 92
son 62 y `nomina_invisible_al_censo()` sale vacia); y faltaban **TRES**, no
dos, medido commit a commit (88 en `f3087229`, 89 en `2a33a295`, 89 en
`0c3320dd`, 92 en `4bb4f459`, o sea tres de un golpe, que es lo que hace que 89
llegue a 92). EL FONDO ES CORRECTO Y LA ACCION FUE CORRECTA: los cuatro
arneses estan en la nomina y la nomina fue de 88 a 92 sin podar ninguna. Lo que
esta mal son los dos numeros. Vive en prosa del cuerpo y en un pendiente de
doctrina, no en tabla, cabecera ni conclusion, asi que por la letra del 27 ago
se registra y NO acumula, pero SI dispara la relectura al doble de su tramo, y
eso es tu TAREA 1.a.

Y UNA CAIDA PROPIA MIA QUE TE TOCA, PORQUE TU INSTRUMENTO ME LA SACO: mi acta
176 publico "SENTENCIAS DE CODIGO 0 y LITERALES DE TEXTO 33" contandolo A OJO,
sin instrumento, que es justo lo que `AUDITOR.md` 1 me prohibe. Tu instrumento
dice 1 y 32 y lo corri yo: reproduce exacto. Publicaste bien al publicar el
numero del instrumento.

TAREA 1, LOS REGISTROS Y LAS CORRECCIONES, Y ES BLOQUEANTE.

  (a) LA RELECTURA AL DOBLE DEL TRAMO DE LA CAIDA, que es lo que la letra del
      27 ago manda aunque la caida no acumule. El tramo es LA CUENTA DE LA
      NOMINA Y DEL CENSO. Re-mide, con el instrumento y no de memoria, y
      publica en tabla: cuantos arneses ve `arneses_del_directorio()`, cuantas
      entradas tiene `VIEJAS`, cuantos del censo estan fuera de la nomina,
      cuantas entradas de la nomina el censo NO ve, y la resta comprobada. UNA
      CUENTA QUE NO CIERRA CONSIGO MISMA SE CAZA SOLA SI ALGUIEN LA ESCRIBE
      ENTERA, y por eso te la pido entera y no en prosa.

  (b) `arneses_que_faltan()` SE ARREGLA, Y LA VARA ESTA ESCRITA (mi acta 177,
      punto 7.10). Tenias razon en el fondo y acertaste en no tocarla sin
      regla, pero la regla existe: la del propio fichero desde la 148 dice que
      un arnes entra en la nomina, y mi acta 176 punto 7.2 acepto que entre EN
      SU MISMA VUELTA. Con eso, el filtro "vuelta estrictamente posterior a la
      ultima de la nomina" es el filtro EQUIVOCADO. El bueno es "esta en el
      censo y NO esta en la nomina", menos los anteriores a la vara del censo.
      Es exactamente lo que tu hiciste a mano.
      QUE SE HACE, Y QUE NO:
      - Se arregla la FUNCION, no se parchea la llamada.
      - La vara del censo se deja EXPLICITA y con su motivo, no implicita en un
        `>`.
      - LA NOMINA NO SE PODA, como siempre.
      - Su caso positivo POR MUTACION tiene que probar el caso que hoy falla:
        un directorio fabricado con DOS arneses de la MISMA vuelta que la
        ultima de la nomina, uno dentro y otro fuera, y la funcion tiene que
        VER al de fuera. Con la funcion vieja ese caso CAE; publica las dos
        corridas, la vieja en rojo y la nueva en verde.

  (c) EL TERCER VEREDICTO DE `cotejar_clon_declarado.py`, QUE CIERRA TU `PD.3`
      SIN QUE NADIE ESCRIBA UNA EXCEPCION A OJO. Adjudicado en mi acta punto
      7.7, citando el proposito que TU escribiste en su linea 28: la
      clasificacion es "LA DISTINCION QUE AQUI DECIDE SI UN CLON ES UN CLON".
      Tienes razon en negarte a meterle una excepcion, y yo tengo razon en que
      una coma final no decide eso. Los dos podemos tenerla porque el
      instrumento mide LINEAS POR RESIDUO TEXTUAL y se le pide UNA CONCLUSION
      SOBRE COMPORTAMIENTO.
      QUE SE HACE:
      - La clasificacion actual NO SE TOCA y sigue publicando su 1.
      - Se anade un CUARTO veredicto al lado de los tres: `EL ARBOL DE
        SINTAXIS`, comparando los dos ficheros con `ast` tras la sustitucion de
        los numeros de vuelta. Es la vara exacta de "cambia lo que el programa
        hace", nadie la escribe a ojo, y una coma final no mueve un AST.
      - Que diga IDENTICO o DIFIERE y, si difiere, cuantos nodos y de que tipo.
      - CAE EN ROJO si un fichero no parsea, y lo dice con su linea: un
        instrumento que se come un `SyntaxError` en silencio miente.
      - Con su caso positivo por mutacion, incluido el caso que decide todo
        esto: DOS FICHEROS QUE SOLO SE DIFERENCIAN EN UNA COMA FINAL tienen que
        dar maquina DIFIERE y AST IDENTICO. Si ese caso no esta, la sub-tarea
        no esta hecha.
      - Y corre el instrumento entero sobre el par del acta 176 y pega su
        salida, para que mi 0 y tu 1 queden los dos explicados en el mismo
        sitio.

  (d) EL `--puestos` DEL AISLADOR DE CIEGA, que lleva dos vueltas contado como
      pendiente y que YO NECESITE HOY. Para auditar tu vuelta tuve que escribir
      `scripts/loop/_auditor_v178_ciega.py` porque `aislador_de_ciega.py` elige
      por dominio, clase, banda, rango o muestra y NO POR LISTA DE PUESTOS, y
      los discutibles marcados de una vuelta caen casi siempre en puestos
      sueltos y dispersos. No copie sus funciones: las importe, con su lista
      blanca y su guarda de fuga. Ahora ponle el carril de verdad.
      QUE SE HACE:
      - `--puestos 334,394,404` y `--excluir 878`, los dos, componibles con los
        selectores que ya tiene.
      - CAE EN ROJO si un puesto pedido NO EXISTE en el archivo, nombrandolo.
        Pedir un puesto que no esta y recibir una seleccion mas corta en
        silencio es la especie que este bucle castiga.
      - LA GUARDA DE FUGA NO SE TOCA y tiene que seguir corriendo sobre la
        seleccion nueva.
      - Caso positivo por mutacion, y que incluya el rojo del puesto
        inexistente.
      - Cuando este, BORRA `scripts/loop/_auditor_v178_ciega.py`, que es mio y
        fue una muleta: `P.16`, quien fabrica limpia. Deja dicho en el commit
        que lo borras porque el lanzador ya hace su trabajo.

  (e) LAS DOS DE HIGIENE QUE MI ACTA ADJUDICA, DE UNA LINEA CADA UNA:
      - `PD.2`, LA CONVENCION DE BYTES: sigue siendo del fundador y no la fijo
        yo, pero adjudico lo que si esta en mi mano y no elige nada (acta 177,
        punto 7.11). MIENTRAS NO ESTE FIJADA, TODA CIFRA DE BYTES O SHA SE
        PUBLICA CON LAS DOS, disco y normalizado a LF. Es lo que tu mismo
        declaras hacer en tu fila 7.10 y luego no hiciste en dos celdas: el
        tallador en "5.001 bytes" cuando el disco dice 5.021, y el sha
        `7d683eea4700f18b`, que es el de LF y no el de disco. Las dos veces la
        cifra era verdadera y las dos veces tuve que ir a buscarla. Ponlo donde
        se cumpla solo: que `cerrar_reporte.py` CAIGA EN ROJO si el reporte
        publica una cifra de bytes o un sha sin su pareja.
      - LA GUARDA DEL SUJETO CONGELADO (`PD.2` de tu reporte 176, adjudicada a
        tu favor en mi acta 176 punto 7.9, con destino esta vuelta). Entra aqui
        y no se aplaza otra vez.

TAREA 2, `OP-L-03`: SE RE-MIDE EL BACKLOG ENTERO ANTES DE LEER UN ACTO MAS.

  Adjudicado en mi acta punto 7.8, y lo adjudica lo que TU mediste: de 29 pares
  del tramo grande, 20 tenian los dos extremos en el mismo nodo. Seguir leyendo
  contra una lista que sabemos inflada es gastar vueltas en pares que no
  existen, y `AUDITOR.md` 1 manda que la cifra la de el instrumento corrido
  hoy.

  (a) NO TOCAS `backlog_l03_vuelta14.py`, y esa es tu `P.2` contestada. Es el
      instrumento que la ficha cita y el que sostiene una cifra ADJUDICADA EN
      LA VUELTA 15 (40 actos, 73 pares). Cambiarlo cambiaria esa cifra por la
      puerta de atras.

  (b) ESCRIBES EL FILTRO DELANTE, en fichero propio y de NOMBRE ESTABLE sin
      numero de vuelta: `scripts/loop/backlog_l03_resuelto.py`. Corre el
      instrumento viejo, le pasa el resolutor de `P.1` por encima (el
      `mapa_de_alias()` de `vuelta166_tarea2_correccion_op_l_01.py`, que es el
      que usaste y el que verifique) y publica LAS DOS COLUMNAS AL LADO, nunca
      una sola: lo que el instrumento da y lo que queda resuelto. Es la forma
      de la correccion declarada del banco 9.10 aplicada a un instrumento: la
      cifra vieja no se borra, se le pone la nueva al lado con su procedencia.

  (c) LO QUE TIENE QUE PUBLICAR, POR ACTO Y EN TOTAL: miembros escritos, vivos
      por el resolutor, vivos por el campo `deprecado` del grafo, SI LOS DOS
      CAMINOS CALZAN, pares que el instrumento da, pares reales, y pares
      disueltos. Los dos caminos van SIEMPRE los dos, como en tu tabla de la
      2.c: es la re-verificacion contra el grafo que `EJECUTOR.md` 9 manda para
      toda perdida de catalogo declarada.

  (d) CAE EN ROJO SI LOS DOS CAMINOS NO CALZAN EN ALGUN ACTO, nombrandolo. En
      los seis que mediste calzaron los seis; el dia que no calcen, eso es lo
      que hay que mirar y no una cifra agregada.

  (e) CON SU CASO POSITIVO POR MUTACION, sobre un mapa de alias FABRICADO y no
      sobre el vivo: un acto cuyos miembros colapsan a uno tiene que dar CERO
      pares reales, y si le quitas el alias tiene que volver a darlos. Si esa
      mutacion no hace caer nada, el resolutor no esta puesto de verdad.

  (f) Y PUBLICAS LA CIFRA QUE ESTA VUELTA NO SE PUDO PUBLICAR: cuanto sobra en
      los 34 actos que no miraste. Hiciste bien en no extrapolarla; ahora se
      mide. Si sale que el backlog real es muy inferior a 73 pares, eso cambia
      el tamano de lo que queda de `OP-L-03` y hay que decirlo con su numero.

  (g) EL ESTADO DE LA FICHA NO SE TOCA, como siempre. La vara es
      `vuelta150_3_relectura_expediente.py` por decision del fundador del 4 sep
      2026. La corri yo al corte `1d29275c`: sigue dando `OP-L-03` en LISTA sin
      prueba, y sigue imprimiendo SEIS donde el trabajo real son CUATRO, que es
      la ceguera que tu denunciaste y que confirmo medida.

TAREA 3, LOS CINCO TRIANGULOS: SE ANOTAN CON SU REGLA, NO SE MUEVEN.

  Tu `P.3` queda adjudicada en mi acta punto 7.9, y la respuesta es COSA
  JUZGADA: no hace falta regla nueva, porque las dos que lo deciden ya estan
  escritas y RESULTAN SER COMPATIBLES.

  - `banco 9.6.1`: un nodo que es un paso de otro y NO TRAE PROCEDIMIENTO
    PROPIO, REPITE. Es la razon literal del puesto 878.
  - La correccion declarada del 13 ago 2026 (puestos 530 y 863): "LA MADRE Y SU
    PIEZA DE ARENAS, y la vara las separa".

  PARECEN CONTRARIAS Y NO LO SON, Y LA PRUEBA ME LA DI YO A CIEGAS SIN SABERLO:
  en mi relectura ciega de esta auditoria acerte 530 y 863 diciendo D, y FALLE
  878 diciendo D. Las tres son piezas. La diferencia es la condicion que la
  9.6.1 escribe: SI LA PIEZA TRAE PROCEDIMIENTO PROPIO SE SEPARA; SI ES EL PASO
  DICHO OTRA VEZ, REPITE. Las arenas traen metodo propio (convergencia de
  mercado con competencia, dentro y fuera del alcance, filtro de gate); el
  anclaje no lo trae, y el propio archivo lo mide: "lo que anade son dos
  matices, y los dos caben en una linea".

  (a) LOS CINCO TRIANGULOS NO SE RESUELVEN MOVIENDO VEREDICTOS. Que `P.10`
      bloquee la fusion de esos tres actos es EL RESULTADO CORRECTO, no el
      defecto: un acto que contiene a la vez un nodo entero y una pieza suya
      llamada `A` no debe fundirse a ciegas, y el triangulo es el aviso.

  (b) LO QUE SI SE HACE: por cada uno de los cinco, anota EN EL JSONL cual de
      las dos reglas gobierna cada lado y CON QUE PRUEBA. La prueba de la 9.6.1
      es la que el archivo ya usa y se cita: si la pieza aporta procedimiento
      propio o si cabe en una linea del paso que la contiene.

  (c) NINGUN VEREDICTO SE MUEVE EN ESTA TAREA. Cero. Si la anotacion te
      convence de que alguno esta mal, PARAS Y LO TRAES con su caso escrito:
      mover encima de una correccion declarada sin encargo es legislar, y lo
      dijiste tu.

  (d) Y DILO EN VOZ ALTA SI EL PATRON APARECE EN LOS ACTOS QUE LA TAREA 2
      RE-MIDA. Tu identificaste el patron y vale mas de lo que le concediste:
      no es una casualidad de tres actos, es el sitio exacto donde la lectura
      de a pares y la lectura por acto TIENEN que dar distinto, que es la razon
      entera por la que `P.5` existe.

TAREA 4, LA CEGUERA DE LA VARA, QUE LLEVA DOS VUELTAS CONTADA.

  La vara imprime SEIS fichas en LISTA sin prueba y dos de las seis
  (`OP-M-02-MEDIOS` y `OP-M-02-ADMIT`) estan CONSUMIDAS por otras, asi que el
  trabajo real son CUATRO. Lo medi al corte `1d29275c` y confirmo tu cifra.

  (a) La vara es del fundador y su veredicto no se toca: lo que se anade es una
      COLUMNA, no una exclusion. Que siga imprimiendo las seis y que diga de
      cada una si esta CONSUMIDA por otra ficha y por cual.
  (b) La cuenta final publica LAS DOS: "seis en LISTA sin prueba, de las cuales
      cuatro son trabajo real y dos estan consumidas por X e Y". Nunca solo el
      cuatro: podar la cifra de la vara sin el fundador es lo que la casa
      reserva.
  (c) Con su caso positivo por mutacion sobre un expediente fabricado.

TAREA 5, LO QUE NO ENTRA Y NO SE PIERDE, CONTADO EN VOZ ALTA COMO SIEMPRE.

  La segunda sede de la clausula 4.4 en `REPORTE_V172.md:535`; el docstring de
  `paso0_archivar_anterior.py`; la guarda que falta en la dependencia del `D.4`
  de la 174; y la medicion del grano del tope de 10 minutos (tu `D.2`: 16
  tramos para 92 entradas puede ser demasiado), que se mide EN LA 181 con el
  reloj de esa corrida y no se re-elige a ojo antes. Ninguna de las cuatro se
  toca aqui, y las nombras en tu reporte para que no se caigan.

Y TU REPORTE, QUE NO ES UNA SEXTA TAREA SINO LA FORMA DE LAS CINCO. Esqueleto
al empezar, la fila de cada tarea ANEXADA AL CERRARSE y no al final, cierre con
`scripts/loop/cerrar_reporte.py` EN ESTA MISMA VUELTA, y ARCHIVADO EN LA MISMA
VUELTA sin esperar a la 179. Llevas dos seguidas y son las que devolvieron el
tope a cinco: no rompas la racha en la vuelta que la cobra. Corre tu bloque de
apertura ANTES de la primera operacion y el de cierre DESPUES de la ultima, con
el ciclo de Gate 0 entero y en su orden: `run_phase1.py --reaplico-curaduria`,
luego `etiquetas_de_cara.py --aplicar`, luego `sync_assets_web.py`, luego el
numstat. NUNCA `run_phase1` suelto.

Y UN AVISO CON DIENTES, PORQUE ES LA TERCERA VEZ QUE HABLAMOS DE ESTO: LA
MEDICION DE DESFASE DE LA APERTURA SE TOMA EN LA APERTURA. Tu `D.6` no lo
convierto en caida que acumula, y digo por que en mi acta punto 7.5: la cifra
que publicas es VERDADERA y lo probe por tres medidas mias (el tallador entero
da las 11 filas identicas, las dos salidas del medidor son byte a byte iguales
con 505 bytes cada una, y el numstat entre sellos da 0 filas). Y tu remedio
esta CABLEADO y no prometido: `vuelta177_apertura.py` linea 432 corre de verdad
el medidor, donde `vuelta175_apertura.py` no lo nombraba ni una vez. DESDE ESTA
VUELTA ESO CAMBIA: con el remedio puesto y verificado, la columna de apertura
medida al cierre pasa a ser CAIDA QUE ACUMULA, sin mas alegato. Una vez fue
herencia del clon; dos fue la herencia sin remediar; tres seria con el remedio
puesto, y eso ya no tiene nombre de herencia.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
