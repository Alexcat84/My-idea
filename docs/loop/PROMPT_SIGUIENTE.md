Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

Eres el ejecutor de la VUELTA 195. Rama `pasada-unica`. FASE III, EJECUCION.

NO ES VUELTA DE BATERIA. La 194 la corrio entera por sus diez tramos y la proxima
cae en la 199, por la cadencia de `AUDITOR.md` 6.1. Tu seccion 9 cierra con el
HUECO DECLARADO Y MEDIDO por el carril de la TAREA 1.b de la vuelta 173, con su
medicion, su atribucion y su corrida. Un hueco declarado no es un hueco escondido.

VAN CUATRO SUB-TAREAS Y DOS SON BLOQUEANTES. El tope de CINCO esta ganado y
medido: `AUDITOR.md` 6.2 pedia DOS vueltas seguidas cerrando su propio reporte con
`cerrar_reporte.py`, y la racha iba en 9 al abrir la 194, que ademas cerro el suyo
en exitcode 0. CUENTALA TU DEL INSTRUMENTO con
`scripts/loop/vuelta192_racha_de_cierres.py` y publica lo que salga. Ese
instrumento PISA su propia sellada: si la corres, restaurala con `git checkout --`
y REMIDELA antes de darla por restaurada.

ABRE EL REPORTE AL EMPEZAR, con su esqueleto tallado y en su propio commit, y mide
tu desfase de calibrado DENTRO del bloque de apertura y ANTES de la primera
operacion.

Y ARREGLA DE UNA VEZ LO QUE TU PROPIO REPORTE DE LA 194 SE DECLARO EN SU `C.3`, que
es la causa de sus otras dos caidas: TU BLOQUE DE APERTURA TIENE QUE CORRER EL
CICLO COMPLETO, `tsc` Y `pnpm test` INCLUIDOS, y tiene que escribir el los dos
literales exactos que la guarda `D.1` de `cerrar_reporte.py` busca en la seccion 4.
Llevas DOS vueltas seguidas heredando esas dos caidas por clonar el bloque de la
vuelta anterior sin leer su seccion 8.1. Un clon declarado hereda tambien los
defectos declarados de su fuente. Si no lo arreglas aqui, la 196 las hereda otra
vez y entonces son tres.

Y UNA COSA QUE ME PASO A MI EN ESTA AUDITORIA Y TE AHORRO: no te inventes la
definicion de una cifra que ya tiene instrumento. Yo conte `union` y `vivos` a mano
sobre `master_graph.json`, me salieron 6605 y 3853, y no calzaban con tu cabecera.
El equivocado era yo: `scripts/loop/vuelta83_conteo_aristas.py HEAD` da
`union 9914` y `vivos 3169`, que es lo que tu publicabas. La vara es el
instrumento, tambien cuando el que mide es el auditor.

=============================================================================
TAREA 1. LOS REGISTROS. BLOQUEANTE.
=============================================================================

El acta 195 entra en la serie con el numero que devuelva
`scripts/loop/serie_de_registros.py`, computado y no tecleado (hoy el siguiente
libre es `R.57`, contado por mi del instrumento en esta vuelta, pero lo dice el
instrumento y no este encargo).

La entrada registra, y cada cifra se cuenta del cuerpo acotado del acta y no de
aqui:

  - LAS DIEZ ADJUDICACIONES `4.1` a `4.10`, Y LAS DIEZ VAN A FAVOR: siete son tus
    discutibles (`D.1` a `D.7`) y las tres restantes son tus preguntas `P.1`, `P.2`
    y `P.3`, dos de ellas contestadas por extension citable con la cita comprobada
    contra su fichero. CERO EN CONTRA, y es la QUINTA acta seguida.
  - LOS TRES HALLAZGOS DE LA SECCION 5, que no salen de ningun discutible: la fila
    de credito del acta 194 que rotula mal su cifra (`5.1`), el rojo de la bateria
    que SI es reparable (`5.2`), y `--componer` que publica VERDE sobre diez tramos
    rojos (`5.3`).
  - CERO CAIDAS DEL EJECUTOR EN LA VUELTA 194, de cifra publicada y de reporte.
    Verifique tus cifras una a una contra mis propios comandos y todas calzan.
    LA RACHA DE REPORTE, que el acta 194 dejo en 1, VUELVE A CERO. No hay escalada
    que encargar, y lo digo expresamente para que no se lea como olvido.
  - UNA CAIDA PROPIA DEL AUDITOR, `C.1`, DE METODO: lei `clase` y `razon` del
    archivo con `json` a mano en vez de por `AP.marcador()` y
    `AP.leer_veredictos()`, que es la cuarta puerta y que ya ofrecia las dos cosas
    sin coste. El sujeto NO se quemo y lo probe DESPUES por la propia puerta: 30 de
    30 sellados vuelven TAPADOS y 0 destapes apuntados. Se registra con su nombre.
  - LA METRICA DE CREDITO de la seccion 7 con sus cifras, incluida la fila de
    puestos: 30 aislados, 30 cotejados, CERO QUEMADOS, que es la diferencia con la
    194 y se debe a que tus mensajes de commit ya no publican clases por puesto.
    ESO FUNCIONO: registralo.
  - Y LA FILA DE CAIDAS PROPIAS VA PARTIDA EN DOS, las que ACUMULAN y el total del
    cuerpo, que es el remedio de mi hallazgo `5.1` aplicado a mi propia tabla.

EL REGISTRADOR SIGUE SIENDO IDEMPOTENTE: re corrido no escribe nada. Pruebalo re
corriendolo, con la sede medida en bytes antes y despues.

=============================================================================
TAREA 2. LA RELECTURA AL DOBLE DE MI TRAMO. BLOQUEANTE, Y ES DEUDA MIA QUE
PAGAS TU CON EL INSTRUMENTO.
=============================================================================

`AUDITOR.md` 1.2: dos discrepancias mias cayeron FUERA de mi marcado, `654` y
`719`, asi que EL CREDITO DE MI TANDA BAJA Y EL TRAMO SE RELEE AL DOBLE.

EL TRAMO Y EL DOBLE ESTAN CERRADOS DESDE HOY, computados y no tecleados, en
`docs/loop/_auditor_v195_doble_para_la_196.txt`, para que no se elijan despues de
mirar:

  EL TRAMO son los 30 puestos de `docs/loop/_auditor_v195_ciega_blind.txt`.
  EL DOBLE son sus 30 vecinos deterministas: 11, 25, 72, 134, 160, 205, 398, 614,
  655, 720, 881, 910, 975, 976, 1071, 1207, 1373, 1808, 1819, 2032, 2159, 2428,
  2662, 2838, 2915, 3072, 3091, 3173, 3187, 3331.

QUE HACER:

  a) `vecinos()` SE IMPORTA de `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py`
     y NO se copia, con `evitar` cargado de TODO lo consumido y contado de sus
     ficheros, que hoy son DOCE y dan 591 puestos. Recomputalo tu y publica lo que
     salga: si tu cifra no es 591, publica la tuya y di de que ficheros sale.
     El solape con el tramo y con el universo tiene que salir CERO POR
     CONSTRUCCION, no por suerte.
  b) LEE LOS 60 A CIEGAS, tramo y doble, con `aislador_de_ciega.py`, y escribe tus
     clases ANTES de abrir el destape.
  c) LA VARA ES `docs/BANCO_DE_TEXTOS.md` `9.6.1`, citada por numero y no
     parafraseada. Y LLEVATE MI ERROR PUESTO, que es lo mas util que saco de mi
     tanda: la vara de contenido-manda es EL SUELO, NO EL TECHO. Antes de aplicarla
     pregunta si el par pertenece a una familia con REGLA PROPIA ya fijada, porque
     entonces manda la especifica. Yo perdi el `719` por no preguntarlo: hay regla
     fijada en el puesto `595` (*"en una serie por fases, dos nodos de fases
     distintas son sanos y dos nodos de la MISMA fase son gemelos"*) con el `580`
     de precedente vivo, y yo llame `A` a lo que es `D`.
  d) Y NO TE SALTES LA `B`. Yo emiti CERO `B` en 30 pares y el archivo tenia una,
     el `654`: dos listas del mismo paso del embudo, cruzadas en el medio, sin
     arista y sin que ninguna nombre a la otra. Un lector que solo reparte `A` y
     `D` no esta leyendo mas fino, esta perdiendo una clase entera.
  e) PUBLICA EL COTEJO con sus cifras: cuantos coinciden, cuantos discrepan, y
     cuales caen dentro y fuera de tu marcado. Marca tus discutibles ANTES de
     saber si aciertas.

=============================================================================
TAREA 3. EL ROJO DE LA BATERIA, ATACADO EN SU CAUSA. NO ES VUELTA DE BATERIA Y
POR ESO ES EL SITIO.
=============================================================================

ES MI HALLAZGO `5.2`, Y ES LA ADJUDICACION DE TU PREGUNTA `P.2`. Tu reporte da el
rojo por *"roto y que yo no podia arreglar hoy"* y teme que la 199 salga igual con
la lista mas larga. LAS TRES CAUSAS TIENEN REMEDIO ESCRITO Y NINGUNA ES DEL
FUNDADOR. La leo de los ficheros y no de memoria:

  `verificar_mutaciones_viejas.py` dice, desde la vuelta 148: *"LO QUE ESTA REGLA
  EXIGE ES SUJETO CONGELADO. EL PLAZO DE UNA VUELTA ERA EL MEDIO, NO EL FIN."* Y
  `AUDITOR.md` 6.1 dice *"LA NOMINA SIGUE CRECIENDO: NADIE LA PODA SIN EL
  FUNDADOR"*. LO RESERVADO ES PODARLA, NO HACERLA CRECER. La opcion `c` que el
  fundador RECHAZO el 5 sep 2026 era JUBILAR ARNESES VIEJOS, que es exactamente lo
  contrario de anadir. El *"NO TOQUES LA NOMINA"* de los encargos anteriores se
  escribio para VUELTAS DE BATERIA y contra LA PODA, y esta no es vuelta de
  bateria.

QUE HACER:

  a) LOS SEIS QUE EL CENSO VE Y LA NOMINA NO TIENE ENTRAN EN LA NOMINA, cada uno
     CON SU SUJETO CONGELADO y cotejado contra su blob de git, que es la condicion
     que la regla exige. Son, leidos de `SALIDA_V194_BATERIA_TRAMO_7.txt` y no
     tecleados por mi de memoria: `vuelta191_tarea3_mutacion_lineas.py`,
     `vuelta191_tarea4_mutacion_veredicto.py`,
     `vuelta191_tarea6_mutacion_bloque_tallado.py`,
     `vuelta192_tarea4_mutacion_cuarta_puerta.py`,
     `vuelta193_tarea4e_mutacion_sello_entre_procesos.py` y
     `vuelta194_tarea2c_mutacion_sede_del_turno.py`. RECUENTALOS TU del instrumento
     al empezar: si el censo ve otros o son otro numero, publica el tuyo.
  b) EL QUE NO PUEDA TENER SUJETO CONGELADO ENTRA COMO CASO DECLARADO, con su
     marca, que es lo que la propia regla manda para ese caso.
  c) LAS TRES ENTRADAS SIN SUJETO CONGELADO que ya estan dentro
     (`vuelta186_tarea2c_mutacion_cierre_tardio.py`,
     `vuelta187_tarea4_mutacion_dos_convenciones.py`,
     `vuelta188_tarea4_mutacion_cobertura_parejas.py`, las tres ancladas a
     `REPORTE.md` VIVO) se resuelven POR LA MISMA REGLA: o se les congela el
     sujeto, o pasan a CASO DECLARADO con su marca. El propio mensaje rojo del
     instrumento lo dicta.
  d) `vuelta172_tarea5_mutacion_cierre.py` NO MUERDE, y lleva asi desde la 189.
     Una guarda que no muerde no es una guarda: arreglala para que caiga cuando
     tiene que caer, o declarala rota con su motivo medido si no se puede.
  e) NO SE PODA NADA. No se quita ni una entrada. La nomina solo crece.
  f) AL CERRAR, CORRE LA BATERIA SOLO SOBRE LO QUE TOCASTE para comprobar que el
     rojo que atacaste se apago, y PUBLICA LA CIFRA de arneses fuera de la nomina y
     de entradas sin sujeto congelado. NO corras la bateria entera: no es su vuelta
     y su cadencia es de `AUDITOR.md` 6.1. Si tras esto la cifra no es cero, dilo
     con su numero y su lista en vez de redondearla.
  g) CON SU CASO POSITIVO POR MUTACION, que pruebe la cosa que falla hoy: que la
     mirada de la nomina sobre si misma CAIGA cuando un arnes que el censo ve se
     queda fuera de la nomina sin ser caso declarado.

=============================================================================
TAREA 4. `--componer` DEJA DE PUBLICAR VERDE SOBRE DIEZ ROJOS.
=============================================================================

ES MI HALLAZGO `5.3` Y LA OTRA MITAD DE TU `P.3`. Tu `SALIDA_V194_BATERIA_COMPUESTA.txt`
termina en *"VERDE: los 10 tramos cubren la nomina entera"* con exitcode 0,
mientras los diez tramos traen `CLASE DEL VEREDICTO: ROJO POR FALLO` y exitcode 1.
Lo verifique yo tramo a tramo. Es cierto EN LO QUE MIDE, la cobertura, y enganoso
EN LO QUE PARECE DECIR, el estado de la bateria. Banco `9.1`: el instrumento debe
caerse en vez de mentir.

  a) `--componer` PROPAGA EL PEOR VEREDICTO DE LOS TRAMOS a su propio exitcode y a
     su linea final. Cobertura entera y algun tramo en rojo NO es VERDE.
  b) LAS DOS COSAS SE SIGUEN DICIENDO POR SEPARADO: la cobertura con su cifra y el
     veredicto con la suya. Que propague el rojo no puede borrar que la cobertura
     estaba completa, que es informacion util y medida.
  c) CON SU CASO POSITIVO POR MUTACION, con la salida de la 194 de sujeto
     congelado, que es el caso real: diez tramos rojos con cobertura 127 de 127
     tienen que dar ROJO.
  d) ESTO LLEVA VUELTAS EN LA LISTA DE LO QUE SIGUE FUERA como *"el exitcode 2
     propagado a `--componer`"*. Hoy tiene su caso medido delante y por eso entra.

=============================================================================
LO QUE NO ENTRA, DICHO PARA QUE NO SE COLE NI SE REDESCUBRA
=============================================================================

Ni cribado, ni recomputo, ni operaciones del plan, ni las mesas anotadas, ni podar
la nomina, ni la bateria entera, que no es su vuelta y cae en la 199.

Y SIGUEN FUERA, NOMBRADAS PARA QUE LA 196 NO LAS REDESCUBRA:

  - EL DESFASE DE `PATRONES_ACTA`, que apunta al acta de `VUELTA - 1`. El acta 193
    lo dejo despues de la bateria de la 194 y la 194 lo paso a la 195; con cuatro
    sub-tareas puestas lo paso yo a la 196 EN PRIMER LUGAR DE LA COLA, y lo digo
    con su motivo en vez de dejarlo caer: las cuatro de hoy atacan causas y esta
    es cosmetica de cabecera.
  - LA FILA DE CREDITO DEL ACTA CON SU ROTULO ARREGLADO. Es mi hallazgo `5.1` y ya
    lo aplique a MI tabla en el acta 195; lo que queda es que el instrumento que
    talla esa fila lo imponga, y eso es codigo.
  - LA GUARDA DE CODIGO DEL HALLAZGO `5.3` DEL ACTA 194, los mensajes de commit sin
    clases por puesto ni reparto de ciega. A MANO YA FUNCIONA Y ESTA MEDIDO: esta
    vuelta mis 30 llegaron con CERO QUEMADOS frente a los ONCE de la 194. La guarda
    durable sigue pendiente.
  - `acumulan()` que lea la tabla, o que declare en su salida que no es la sede.
  - El cotejo de clon declarado que separa sentencia de codigo de cambio de texto.
  - La excepcion que publica siempre su lista.
  - La medicion del censo de arneses con carril de mutacion sin fichero propio.
  - Las ocho actas sin entrada propia en la serie (173 a 180), medidas y no
    arregladas.
  - Que el campo `evidencia` de `OP-L-02` nombre los ficheros que ya existen. Su
    ESTADO NO SE MUEVE: sigue en `LISTA`, y declararla HECHA es del fundador.
  - QUE HACER CON LAS 72 FILAS `B` DEL ARCHIVO. Lo dejo NOMBRADO y medido y no
    resuelto, porque mover una clase esta reservado y eso es del RECOMPUTO. La
    cifra la recompute hoy por la cuarta puerta: `A 551, B 72, C 5, D 2760` sobre
    3388 filas. Y anado un dato para quien recompute: en mis 30 el archivo tiene
    UNA `B` y yo emiti CERO, o sea que el sesgo de los lectores contra esa clase
    esta medido en las dos direcciones.

Y NO SE MUEVE NINGUN VEREDICTO: el `sha256` LF de
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` tiene que abrir y cerrar en
`0a77b5a35a962621`, que es lo que medi hoy por las dos convenciones sobre 4054129
bytes. Y `dataset/` no se toca a mano: el `numstat` se mide al entrar y al salir y
las dos cifras se publican. El ciclo de Gate 0 se corre ENTERO, con
`run_phase1.py --reaplico-curaduria` y despues `etiquetas_de_cara.py --aplicar`:
medido por mi hoy, asi da CERO lineas en `dataset/`, `web/` y `engine/`.

Y SI RE CORRES UN INSTRUMENTO QUE PISA UNA SALIDA SELLADA AJENA, RESTAURALA CON
`git checkout --` Y REMIDELA ANTES DE DARLA POR RESTAURADA, Y NO LE TOQUES LOS
FINALES DE LINEA A MANO.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
