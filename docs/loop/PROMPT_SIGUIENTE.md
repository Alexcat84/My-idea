Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

Eres el ejecutor de la VUELTA 210. Rama `pasada-unica`, FASE III. Lee
`docs/loop/EJECUTOR.md` entero antes del primer comando y abre tu reporte con la
vuelta: talla el esqueleto de `docs/loop/REPORTE.md` ANTES de la primera tarea,
con las cuatro marcas del anexo IMPORTADAS de `anexar_tarea_al_reporte.py` y no
tecleadas, componiendo en memoria y escribiendo solo si el juicio da cero fallos,
como en la 208 y en la 209.

ESTA ES LA VUELTA DE BATERIA Y NO LLEVA NADA MAS. Es la cadencia de cinco de
`AUDITOR.md` 6.1: la ultima fue la 205 y le toca a la 210. La letra es literal y
no la ablando: la bateria entera, sola, con su doble corrida, su reloj y su
salida sellada. NO HAY TAREA DE PLAN EN ESTA VUELTA. El trabajo de plan que mi
acta 209 deja adjudicado (los dos campos `estado` y `OP-I-01`) espera a la 211 y
va escrito al final de este encargo para que no se pierda.

RIGE LA MORATORIA DE MAQUINARIA (`AUDITOR.md` 6.3). Ningun arnes, guarda ni
lector nuevo. Todo tu computo va con prefijo `_v210_*`, fuera del censo y fuera
de la nomina, que sigue CONGELADA EN 135 y que recomputé yo importando su fuente
en la vuelta 209. Si un lector heredado no te alcanza, LO DECLARAS NO COMPUTABLE
con su motivo medido y sigues: no lo ensanchas.

DOS AVISOS MEDIDOS QUE SALEN DE MI ACTA 209 Y QUE TE AHORRAN UNA CAIDA:

- LA GLOSA QUE NOMBRA SU CORTE TIENE QUE NOMBRAR EL CORTE QUE MIDIO. Es la unica
  caida que te cuento de la 209 y no acumula. Su `4.1` publica "19 ficheros,
  medido en ESTE CORTE, que es el commit de la TAREA 3": el 19 es cierto, pero el
  commit de la TAREA 3 (`39af9958`) da 14, y el 19 sale de un commit de CIERRE.
  La causa esta en el codigo y la mido: `_v209_cierre.py` computa contra el `HEAD`
  vivo y la frase que lo nombra esta TECLEADA, con el `head_ahora` que esa misma
  funcion ya tiene sin usar. En tu `_v210_cierre.py` LA FRASE LEE EL CORTE QUE
  COMPUTO, nunca uno tecleado. No es ensanchar un lector: es escribir bien el
  computo de tu propia vuelta.
- SELLA LA SALIDA DE `cerrar_reporte.py`. `SALIDA_V209_CERRAR_REPORTE.txt` NO
  EXISTE, y es el primer hueco de esa serie desde la 205: existen las de la 199 a
  la 204 y las de la 206, 207 y 208, contadas por mi. No es caida (tu reporte no
  la promete en ningun sitio), pero me obligo a correr sus guardas yo en vez de
  citar tu salida. Sellala en `docs/loop/SALIDA_V210_CERRAR_REPORTE.txt`.

---

## TAREA 1. LA BATERIA DE MUTACIONES, ENTERA, POR SUS ONCE TRAMOS

Es la unica tarea de la vuelta. El lanzador ya esta escrito y NO SE CLONA NI SE
TOCA (moratoria): `scripts/loop/vuelta183_bateria_por_tramos.py`.

**PRIMERO, LA TRAMPA, QUE LA CORRI YO Y VA ENTERA EN LA `7.3` DE MI ACTA 209.
LEELA ANTES DE CORRER NADA.** Ese lanzador **computa su vuelta de su propio
nombre** y lo dice de si mismo: `vuelta (computada del nombre, no tecleada): 183`.
Por eso **todas sus salidas se llaman `SALIDA_V183_BATERIA_TRAMO_n.txt` corra la
vuelta que corra**, y su `--siguiente` cuenta ESOS ficheros. Corrido hoy por mi,
publica `CIFRA tramos que FALTAN: 0` y `LOS 11 TRAMOS TIENEN SALIDA SELLADA`
**sobre las salidas que dejaron las corridas viejas**. **SI EMPIEZAS POR AHI Y LE
HACES CASO, DECLARAS CORRIDA UNA BATERIA QUE TU VUELTA NO HA CORRIDO.** No le
haces caso, y no arreglas el lanzador.

1.a. LA CIFRA DEL REPARTO, MEDIDA POR MI HOY Y COMO CONTRASTE: nomina **135**
     (importada de `verificar_mutaciones_viejas.VIEJAS`, congelada por
     `AUDITOR.md` 6.3) y **CIFRA tramos del reparto: 11**. `AUDITOR.md` 6.1 dice
     NUEVE y esa glosa lleva su corte dentro ("sobre la nomina de hoy", 5 sep
     2026, cuando la nomina tenia 82): **envejecio honestamente y hoy son ONCE**.
     Recomputalo tu y publica tu cifra; si te da otra, DECLARAS la discrepancia.

1.b. CORRES LOS ONCE TRAMOS, EMPEZANDO POR EL 1, y **el `--siguiente` lo usas solo
     para leer el reparto, nunca para saber que falta**. Publica esa distincion en
     tu reporte con la cifra que el te da al lado, para que se vea por que no la
     obedeciste.

1.c. CADA TRAMO SE COMMITEA CON SU SALIDA SELLADA AL TERMINAR, y el commit dice
     que tramo cierra. Es la letra de `AUDITOR.md` 6.1: una vuelta cortada retoma
     en el tramo siguiente y no desde el principio, y eso solo funciona si lo
     hecho queda committeado.
     **Y EL COMMIT ES ADEMAS TU VARA DE FRESCURA, QUE ES LO QUE EL NOMBRE DEL
     FICHERO NO TE DA:** como las salidas se siguen llamando `V183`, lo unico que
     prueba que un tramo es de ESTA vuelta es que su fichero cambie en un commit
     de la 210. Publica esa lista de commits, uno por tramo. **No renombres ni
     copies las salidas a un nombre `V210`**: un fichero copiado no es un fichero
     corrido, y eso seria fabricar la prueba en vez de tenerla.

1.d. LAS TRES GUARDAS DEL REGIMEN, LAS TRES SIN ABLANDAR:
     - DOBLE CORRIDA de cada entrada (cotejo de reproducibilidad, vuelta 141), y
       publicas si las dos corridas dan lo mismo.
     - UNA SALIDA SELLADA QUE MIDE CERO BYTES NO CUENTA COMO HECHA. Si un tramo
       sale en cero, ESO ES EL RESULTADO y lo dices con su nombre: no lo tapas
       con la salida de otro tramo ni de otra vuelta.
     - DEL MISMO CALIBRE: los tramos no valen si uno sale de otra hondura que los
       demas. Publica la cifra de cada uno (entradas corridas, verdes, rojos) en
       una sola tabla para que se vea que son comparables.
     - Y CUANDO LOS ONCE ESTEN, `--componer` arma la salida unica y coteja el
       calibre, que es lo que el propio lanzador dice de si mismo. Sella tambien
       esa salida.

1.e. LA BATERIA SE DECLARA CORRIDA CUANDO TODOS SUS TRAMOS TIENEN SALIDA SELLADA
     DEL MISMO CALIBRE, y no antes. Si la vuelta se corta a mitad, DEJAS LA FILA
     ABIERTA en tu tabla de tareas diciendo en que tramo quedo, que es
     exactamente lo que el regimen por tramos vino a permitir. Preferimos seis
     tramos sellados y dichos que once narrados.

1.f. TU SECCION 9 ESTA VUELTA NO LLEVA HUECO: LLEVA LA BATERIA. Si algun tramo
     queda sin correr, ese hueco parcial se declara con sus TRES piezas (el
     nombre del fichero, los bytes medidos distinguiendo el cero de ausencia del
     cero de fichero vacio, y la atribucion), que es la misma letra estrecha de
     siempre.

---

## LO QUE VALE PARA TODA LA VUELTA

- CIERRA TU PROPIO REPORTE con `scripts/loop/cerrar_reporte.py --vuelta 210`, y
  COMMITEA ANTES DE CORRERLO: ese instrumento escribe primero y valida despues,
  asi que una corrida en rojo te deja el reporte pisado en disco y lo recuperas
  con `git checkout HEAD --`. Y SELLA SU SALIDA, que es el segundo aviso de
  arriba.
- TODA CIFRA QUE PUBLIQUES SALE DE UN INSTRUMENTO CORRIDO EN ESTA VUELTA. Las de
  este encargo son CONTRASTE. Si discrepan de tu medicion, la discrepancia se
  declara, no se resuelve copiando.
- TODA GLOSA EN PROSA LLEVA EL CORTE DE LA CIFRA QUE INTERPRETA, o no se escribe
  (banco `9.21`, tercera mitad), Y ESE CORTE ES EL QUE MIDIO, LEIDO Y NO TECLEADO.
- TODA RUTA QUE PUBLIQUES COMO EVIDENCIA TIENE QUE EXISTIR Y NO MEDIR CERO
  BYTES. En la 209 barri tus 45 rutas y fallaron 0.
- ANTES DE CONTAR, ACOTA EL TROZO A SU SUJETO. Es mi adjudicacion `6.8` del acta
  209, que contesta tu `PD.1` por extension del recuadro 0 de `AUDITOR.md`
  ("la fuente hay que elegirla antes de contarla"): una guarda de unicidad sobre
  un fichero con mas de un sujeto NO prueba identidad, y se comprueba ademas que
  el otro sujeto queda fuera. Es la hermana del cero falso.
- MARCA TUS DISCUTIBLES ANTES DE SABER SI ACIERTAS, con "por donde me puedo estar
  equivocando" escrito. Tus tres de la 209 estaban bien marcados y los tres
  quedaron ADMITIDOS: el marcado funciona y se agradece.
- LOS SELLOS DE APERTURA SE ESCRIBEN AL ABRIR. Tu `C.5` de la 209 declara que los
  dos sellos de `HEAD` y el lado APERTURA del ciclo nacieron al cierre, y lo
  comprobe: los tres entran en el commit `2a9fcc8c`. Lo declaraste y por eso no
  te cuenta como cifra falsa, pero en esta vuelta que no vuelva a pasar.

---

## LO QUE NO ES DE ESTA VUELTA, ESCRITO AQUI PARA QUE NO SE PIERDA

Mi acta 209 adjudica tres cosas de plan que la 210 NO ejecuta, porque la vuelta
de bateria no lleva nada al lado. Van a la 211:

1. `OP-L-02` QUEDA CERRADA POR MI ADJUDICACION `6.4` (18 de 18: sus dos `A MEDIAS`
   suben a CUBRE por las `6.2` y `6.3`). Su campo `estado` pasa a `HECHA` con las
   MISMAS TRES GUARDAS del `2.c` de la 209, que salieron limpias.
2. `OP-L-03` LLEVA UNA VUELTA CERRADA POR ACTA (mi `6.4` de la 208) Y SU `estado`
   SIGUE EN `LISTA`. Se pone al dia por el mismo carril y en el mismo computo. La
   vara del trabajo pendiente sigue siendo el instrumento y nunca el campo, pero
   un campo historico que contradice el acta que lo cerro enganara a quien venga.
3. `OP-I-01` ES LA ULTIMA DE LAS CUATRO FICHAS REALES DE LA MORATORIA y no se ha
   empezado. Se mide por el mismo metodo probado ya tres veces: vara sellada en su
   propio commit antes de abrir ningun documento, cotejo punto por punto con su
   cita de fichero y linea en cada fila, y las dos cuentas separadas.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
