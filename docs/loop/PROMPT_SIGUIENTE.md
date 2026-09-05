Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

ANTES DE ESA PRIMERA LINEA, CORRE LA GUARDA QUE TU MISMO CONSTRUISTE:
`python scripts/loop/guarda_commit_dataset.py`. Si sale ROJO, NO COMMITEES:
restaura `dataset/` contra HEAD, declara la restauracion con su medicion, y
solo entonces sigue. Ese es el agujero que la 175 destapo y que tu guarda
tapa; no lo dejes sin usar el dia que sirve.

AVISO SOBRE UNA `M` QUE NO ES MUTACION, MEDIDO POR MI EN ESTA AUDITORIA: el
arbol puede llegarte con `M dataset/metadata/master_graph.json` en `git
status` y CERO filas en `git diff --numstat`. Lo medi: disco y HEAD son
IDENTICOS byte a byte, 8.375.817 bytes y sha256 `627cc662296f7f00` los dos.
Es cache de `stat` por el CRLF de Windows. Tu guarda lo adjudica bien con su
cotejo de blobs. No restaures lo que no esta mutado, y no lo des por bueno
sin medirlo tampoco.

ESTA VUELTA NO ES DE BATERIA, Y LA CADENCIA QUEDA ADJUDICADA EN MI ACTA 176,
punto 7.8: LA PROXIMA VUELTA DE BATERIA ES LA 181, no la 180. El contador se
reancla a la vuelta que de verdad la corrio, porque `AUDITOR.md` 6.1 habla de
una VUELTA DE BATERIA propia y la 175 no lo fue: murio sin producir una
linea. En esta vuelta y en las tres siguientes, la seccion 9 de tu reporte
cierra con el HUECO DECLARADO Y MEDIDO por el carril de la TAREA 1.b de la
173, con su medicion, su atribucion y su corrida. Un hueco declarado no es un
hueco escondido.

EL TOPE SIGUE EN DOS SUB-TAREAS (`AUDITOR.md` 6.2) y este encargo trae
exactamente dos. LA 176 CERRO SU PROPIO REPORTE Y LO ARCHIVO EN SU MISMA
VUELTA: es la PRIMERA de las dos seguidas. SI TU CIERRAS EL TUYO, EL TOPE
VUELVE A CINCO POR LA PROPIA LETRA DE LA 6.2, sin que nadie tenga que
decidirlo. Esta vuelta vale por eso ademas de por su trabajo.

Y CORRE TU BLOQUE DE APERTURA. La 176 no lo corrio por leer que entraba en el
"la vuelta de bateria no lleva nada mas" de la 6.1, y esa lectura queda
CORREGIDA en mi acta, punto 7.1: la 6.1 saca el TRABAJO DE PLAN, no el
aparato de abrir y cerrar la vuelta. Si lo sacara, sacaria tambien el
reporte, y la 6.1 y la 6.2 se contradirian. Ademas esta vuelta no es de
bateria, asi que la duda ni se plantea.

LO QUE VERIFIQUE DE TU VUELTA 176, DICHO PARA QUE SEPAS SOBRE QUE PISAS: la
bateria 88 de 88 con su doble corrida, sus 18 numeros de tramo, las tres
medidas de la salida unica (60.197 bytes, 995 lineas, sha256
`2f86d9e075d4e5ce`), las cinco cuentas de veredicto, los 13 commits, las 39
rutas, el marcador 3.388 con A 551 B 72 C 5 D 2.760 y cero huecos, el ciclo
entero de Gate 0 corrido por mi, las 11 filas del tallador COTEJADAS Y
IDENTICAS, las dos ternas de archivado y el reloj de 31,9 minutos: TODO
REPRODUCE. Y las 55 rutas que tu reporte nombra EXISTEN Y NINGUNA MIDE CERO
BYTES. Fue una vuelta buena y el trabajo de esta se apoya en ella.

TAREA 1, LOS REGISTROS Y LAS CORRECCIONES, Y ES BLOQUEANTE.

  (a) DEJA CONSTANCIA de que has leido mi acta 176 (`docs/loop/ACTA_AUDITOR.md`,
      a partir de la linea 60402), nombrando en tu reporte las siete
      adjudicaciones de su seccion 7 y que hace cada una contigo.

  (b) EL ARNES DEL ROJO, Y ES LO PRIMERO QUE SE ARREGLA. Mi acta adjudica la
      `P.1` que tu trajiste sin elegir: SE COMPUTA EL ESPERADO. En
      `scripts/loop/vuelta166_tarea2_mutacion_correccion.py`, linea 175, el
      caso `H_el_texto_nombra_las_tres` compara `real.count("cae sobre")`
      contra un `3` TECLEADO, mientras el `real` sale de
      `T.medir_clausula_1()` sobre el registro VIVO, que hoy da 11. Lo
      reproduje: exit 1, 19 casos, 18 pasan, 1 falla.
      QUE SE HACE, Y QUE NO:
      - El esperado se COMPUTA de la misma fuente viva, para que el caso siga
        comprobando lo que existe para comprobar: que el texto nombra TODOS
        los hallazgos, sean tres u once.
      - NO se pasa a CASO DECLARADO. Apagar una guarda que mide mal es lo
        contrario de fallar ruidoso (banco §9), y esta descartado con motivo
        en mi acta.
      - NO se re-ancla a un sujeto congelado: eso lo dejaria midiendo contra
        un registro que ya no es el vivo.
      - LA NOMINA NO SE PODA. La entrada se queda; lo que se arregla es su
        medicion. Esto no es discutible y no es tuyo ni mio.
      - Su caso positivo POR MUTACION tiene que probar que el arnes SIGUE
        MORDIENDO: muta el texto para que deje de nombrar un hallazgo y el
        caso `H` tiene que CAER. Un esperado computado que no puede fallar
        nunca no es una guarda, es un adorno.
      - Corre el arnes entero al terminar y publica sus 19 casos con su exit.

  (c) LA CORRECCION DECLARADA DE MI CAIDA DE REPORTE 1. Tu reporte de la 176
      publica que el `diff` del clon declarado, con `175` y `176` sustituidos
      por `NNN`, "sale VACIO". LO CORRI Y NO SALE VACIO: 58 lineas de diff, y
      33 de ellas de la maquina. Lo medi hasta el fondo antes de acusar y el
      fondo te da la razon: de esas 33, SENTENCIAS DE CODIGO 0, LITERALES DE
      TEXTO 33 (las dos filas de tarea y la prosa que el esqueleto escribe). Y
      en `vuelta176_cierre.py` la maquina sale VACIA de verdad. O sea que lo
      que quieres decir es cierto y lo que publicas es falso.
      LA MISMA FRASE ESTA EN DOS DOCSTRINGS DE `scripts/`:
      `vuelta176_esqueleto_reporte.py` y `vuelta176_cierre.py`. Corrigelas POR
      DECLARACION, sin borrar de que iban, igual que el fundador corrigio el
      "307 nodos vivos" de `run_phase1.py`. El reporte archivado de la 176 NO
      se reescribe: la correccion vive aqui y en el codigo.

  (d) Y EL INSTRUMENTO QUE LA HACE INNECESARIA, porque una frase corregida a
      mano vuelve a torcerse. Escribe `scripts/loop/cotejar_clon_declarado.py`
      (nombre estable, sin numero de vuelta) que reciba dos ficheros y sus dos
      numeros de vuelta, sustituya los dos por `NNN` e imprima TRES veredictos
      separados y no uno: FICHERO ENTERO, SOLO DOCSTRING, SOLO LA MAQUINA. Y
      que cuando la maquina difiera, CLASIFIQUE las lineas en SENTENCIAS DE
      CODIGO y LITERALES DE TEXTO, que es la distincion que aqui decide si un
      clon es un clon. CAE EN ROJO si le falta un fichero. Con su caso
      positivo por mutacion, como todo. A partir de la 178, ningun reporte
      escribe "clon declarado" sin pegar la salida de este fichero.

  (e) LAS DOS CORRECCIONES CHICAS QUE MI ACTA ADJUDICA Y QUE SON DE UNA LINEA
      CADA UNA:
      - `D.5`: saca la salida del lanzador de tramo FUERA de `docs/loop/`.
        Tienes razon en que hoy da RUIDO 0 medido, y tienes razon en que es
        suerte de buffer. Un control que funciona por una propiedad que nadie
        garantiza no es un control.
      - El tallador de cabecera SELLA SU PROPIO RECHAZO. Tu reporte publica
        "37 celdas que no se pudieron leer, 18 del lado APERTURA" y no puedo
        re-verificar el 37, porque los ficheros de cierre ya existen y el
        tallador no dejo salida de aquel rechazo. Que cuando se niegue a
        tallar escriba un `SALIDA_V<N>_TALLADOR_RECHAZO.txt` con las celdas
        que no pudo leer y de que lado estan.

  (f) `D.3` Y `P.3`, EL TAMANO DE TRAMO SE COMPUTA Y NO SE ELIGE. Cuando la
      181 reparta la bateria, el reparto se hara por TOPE DE MINUTOS, no por
      tope de entradas, y el tamano se computara del reloj medido de la
      corrida anterior. Tu propia tabla es el argumento: estimaste 3,3 a 4,3
      minutos por tramo y el tramo 4 tardo 15,9. Deja el tope de minutos
      escrito y computado dentro de `reparto_en_tramos()`, con su caso
      positivo, para que la 181 no lo tenga que decidir a ojo.

  (g) LO QUE NO ENTRA EN ESTA VUELTA Y NO SE PIERDE, contado en voz alta: la
      GUARDA DEL SUJETO CONGELADO (`PD.2`, adjudicada a favor tuyo en mi acta
      7.9, entra en la 178); la CEGUERA DE LA VARA, que no distingue una
      ficha CONSUMIDA por otra de una ficha PENDIENTE y por eso imprime SEIS
      donde el trabajo real son CUATRO (178); la convencion de bytes, que sube
      al fundador y no la decido yo; la segunda sede de la clausula 4.4 en
      `REPORTE_V172.md:535`; el `--excluir` del aislador de ciega; el
      docstring de `paso0_archivar_anterior.py`; y la guarda que falta en la
      dependencia del `D.4` de la 174.

TAREA 2, `OP-L-03`, QUE LLEVA SIETE VUELTAS APLAZADA Y SE DESAPLAZA AQUI.

  La vara de hoy (`scripts/loop/vuelta150_3_relectura_expediente.py --corte
  8c176390`, corrida por mi) la da en LISTA sin ninguna prueba de ejecucion,
  con `OP-L-01`, `OP-L-02` y `OP-I-01`. Es trabajo de plan de verdad y esta
  vuelta lo hace.

  (a) LEE SU FICHA ENTERA ANTES DE TOCAR NADA: la entrada `OP-L-03` de
      `docs/plan/OPERACIONES.jsonl` (fase `09_LECTURAS_DIRIGIDAS`, tipo MESA,
      con su `verificacion` de cuatro puntos, su `adjudicacion` y su `nota`
      con el reparto por tamano de acto) y `docs/plan/LECTURAS_DIRIGIDAS.md`.
      El universo esta MEDIDO desde el 11 ago 2026: 55 pares en 29 actos,
      corte puesto 2117. DOS YA ESTAN LEIDOS como lectura dirigida de la
      primera tanda, `LD-04` y `LD-08`, y NO se releen ni se les acuna numero
      nuevo (adjudicacion 4.1 del acta de la vuelta 19).

  (b) EL CRITERIO ES `P.5` DEL BANCO DEL PLAN Y SE CITA, NO SE PARAFRASEA
      (banco 9.5.0): cada acto que vaya a fundirse SE LEE ENTERO despues de su
      destejido y antes de su fusion. La lectura es del ACTO, no de la pareja:
      la regla de FAMILIA DECLARADA del informe intra-dominio dice que una
      familia juzgada de a pares da incoherencia, porque la pregunta no es de
      pares. Una decision por acto.

  (c) EL TRAMO DE ESTA VUELTA, Y NO MAS: LOS ACTOS GRANDES PRIMERO, que son
      donde la lectura por acto cambia algo. Empieza por
      `cierre_segun_complejidad_venta` (seis miembros, seis pares por leer de
      quince, el mayor del reparto) y sigue por los cuatro actos de CINCO
      miembros. Si el tramo se te agota antes, PARA Y DILO con la cuenta
      exacta de lo leido y lo que queda: el resto va a la 178. Prefiero medio
      `OP-L-03` medido que uno entero apurado.

  (d) CADA LECTURA SE REGISTRA EN JSONL, NO SE NARRA EN PROSA. Acto, miembros
      con su fuente, pares que le tocan con su puesto, la forma que sale de
      leerlo entero, y si esa forma CAMBIA respecto de lo que el par decia por
      separado. Si cambia, se re-mide CON SU COBERTURA AL LADO, que es la
      cuarta linea de la `verificacion` de la ficha y el banco 9.26.

  (e) NINGUN VEREDICTO SE MUEVE EN ESTA VUELTA SIN CORRECCION DECLARADA Y
      RECOMPUTO. Si una lectura entera te obliga a cambiar la clase de un par,
      eso es correccion declarada por el carril del banco 9.10, con el texto
      viejo entero arriba y sin tacharlo, Y CON EL MARCADOR RECOMPUTADO
      detras. Si son mas de dos, PARA Y TRAELO: mover el marcador es cifra
      publicada y no se hace de pasada.

  (f) LAS 55 LECTURAS MARCADAS "LECTURA DIRIGIDA" NO ENTRAN EN LA COLA NI
      MUEVEN SU MARCADOR. Es la segunda linea de la `verificacion` de la
      ficha y es facil de romper sin querer.

  (g) EL ESTADO DE `OP-L-03` NO LO TOCAS AUNQUE LA TERMINES. La vara es
      `vuelta150_3_relectura_expediente.py`, nunca el campo `estado`, y esa
      decision es del fundador (4 sep 2026). Lo que dejas es el registro y la
      medicion; quien lea despues corre la vara.

Y TU REPORTE, QUE NO ES UNA TERCERA TAREA SINO LA FORMA DE ESTAS DOS.
Esqueleto al empezar con `scripts/loop/vuelta177_esqueleto_reporte.py`, la
fila de cada tarea ANEXADA AL CERRARSE y no al final, cierre con
`scripts/loop/cerrar_reporte.py` EN ESTA MISMA VUELTA, y ARCHIVADO EN LA
MISMA VUELTA sin esperar a la 178. Corre tu bloque de apertura ANTES de la
primera operacion y tu bloque de cierre DESPUES de la ultima, con el ciclo de
Gate 0 entero y en su orden: `run_phase1.py --reaplico-curaduria`, luego
`etiquetas_de_cara.py --aplicar`, luego `sync_assets_web.py`, luego el
numstat. NUNCA `run_phase1` suelto: te mordio en la 176 y esta escrito en el
docstring que tu mismo clonaste.

SOBRE LA LETRA (f) DE MI ENCARGO ANTERIOR, QUE ESCRIBI MAL Y AQUI QUEDA
REESCRITA. Decia "SI UN TRAMO SALE EN ROJO, PARA AHI Y TRAELO" y a la vez te
pedia la bateria ENTERA, y las dos tiraban en sentidos opuestos. Tu elegiste
bien y lo marcaste como discutible: mi acta 176 te da la razon en el punto
7.6 y la culpa de la ambiguedad es mia. LA LETRA BUENA, PARA CUANDO VUELVA A
HACER FALTA: un rojo NO SE RE-CORRE Y NO SE TOCA NI EL ARNES NI SU SUJETO; se
commitea en rojo y se trae. Lo que SI se sigue haciendo es correr las
entradas que no son el rojo, en acto aparte y declarado, porque eso no
enmascara nada, lo anade. Enmascarar es re-correr; parar del todo es ocultar
resultados.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
