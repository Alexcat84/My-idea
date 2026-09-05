Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

Eres el ejecutor de la vuelta 180 de la campana My Idea. FASE III, EJECUCION,
rama `pasada-unica`. Lee `docs/loop/EJECUTOR.md` entero antes de empezar y sigue
su ciclo: bloque de apertura corrido ENTERO y ANTES de la primera operacion (con
el desfase del calibrado DENTRO de el), esqueleto del reporte abierto al empezar
con sus cinco filas vacias, cada tarea ANEXA su fila al cerrarse, y el cierre lo
talla `scripts/loop/cerrar_reporte.py`.

**ESTA VUELTA NO ES DE BATERIA Y LA SIGUIENTE SI.** `AUDITOR.md` 6.1: la bateria
corre CADA CINCO en vuelta propia, y **la proxima es la 181**, adjudicada en el
acta 176 punto 7.8 y reconfirmada en las actas 178 punto 11 y 179 punto 11. La
seccion 9 de tu reporte cierra con el **HUECO DECLARADO Y MEDIDO** y sus TRES
piezas juntas: el nombre del fichero, sus bytes medidos por las dos convenciones,
y la atribucion. **Y esta es la ULTIMA vuelta que lo declara: la 181 lo corre.**

**EL TOPE SIGUE EN CINCO** (`AUDITOR.md` 6.2, cumplido en la 177 y confirmado en
la 178 y la 179). Este encargo lleva cinco.

**LO QUE MANDA ESTA VUELTA, EN UNA LINEA: DEJAR LA PISTA LIMPIA PARA LA 181.** La
guarda del sujeto congelado sale hoy en ROJO con 17 entradas y la 181 la va a
correr. Las TAREAS 1 y 2 son BLOQUEANTES y van en ese orden.

---

## TAREA 1 (BLOQUEANTE). LOS REGISTROS, Y LA ETIQUETA DE FUENTE QUE YO AUTORIZO TOCAR

**1.a. LOS REGISTROS.** Anota en tu reporte que el acta del auditor de la vuelta
179 esta escrita en `docs/loop/ACTA_AUDITOR.md` y que **no levanta ninguna caida
contra la 179**: la racha de reporte vuelve a CERO y la racha de cifra publicada
sigue en CERO. **No hay ninguna correccion declarada que arrastres de la 179.**

**1.b. LA ETIQUETA DE FUENTE, ARREGLADA, Y ESTO LEVANTA TU PARADA DE LA 3.f.**
Hiciste bien en pararte: mi encargo de la 179 decia que `fuente_de_la_clase` no se
toca, y `EJECUTOR.md` 5 te manda parar en vez de improvisar. **La adjudicacion
7.7 del acta 179 estrecha esa instruccion mia, que es lo unico que estaba en
conflicto.** Lo que aquel encargo protegia era que **ninguna clase ni su
procedencia se movieran**; un literal que atribuye a la vuelta 177 cinco lecturas
de la 179 **no protege eso, lo rompe**, contra `EJECUTOR.md` 8, toda cifra de un
autor con su atribucion.

Arreglalo asi y no de otra manera:

- `clases_por_par()` **lee la vuelta de la fila del registro** en vez de traer el
  literal `"docs/plan/OP_L_03_LECTURAS.jsonl (vuelta 177)"` clavado. La etiqueta
  de cada lado dice la vuelta que de verdad escribio esa clase.
- **NINGUNA CLASE SE MUEVE.** Comprueba `sha256` de
  `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` y de `docs/plan/OP_L_03_LECTURAS.jsonl`
  **antes y despues**, dentro del propio instrumento, y publica los cuatro.
- **VUELVE A CORRER** `vuelta179_tarea3_etiqueta_de_fuente.py` despues del
  arreglo. Antes daba 15 etiquetados como de la 177, de los cuales 10 verdaderos
  y **5 falsos**. Publica las DOS mediciones, la de antes y la de despues, cada
  una con su corte, y **la de despues tiene que dar 0 falsos**. Si no da 0, paras
  y lo traes.
- Vuelve a correr tambien `vuelta178_tarea3_anotar_triangulos.py` y publica el
  reparto de lados por fuente con las etiquetas nuevas. **El total de lados y el
  total de triangulos no pueden cambiar: 19 triangulos y 57 lados con clase.** Si
  cambian, paras.
- **Caso positivo por mutacion** sobre un registro fabricado, con al menos un
  lado escrito por una vuelta y otro por otra, que CAE si la etiqueta vuelve a
  quedarse clavada en un literal.

---

## TAREA 2 (BLOQUEANTE, Y ES LA QUE LIMPIA LA PISTA DE LA 181). EL SUJETO CONGELADO, RESUELTO Y CABLEADO

**LA ADJUDICACION QUE LA ORDENA ES LA 7.8 DEL ACTA 179, y sigue tu propia
recomendacion:** cablear hoy con 17 pondria la bateria de la 181 en un rojo
permanente que todo el mundo aprende a ignorar, y eso es degradacion silenciosa
(`banco 9`). **El orden es: los trece declaran, los cuatro congelan, y SOLO
ENTONCES se cablea.** Los diecisiete estan juzgados en
`docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl`, que verifique fila por fila.

**2.a. LOS TRECE QUE NO ABREN NADA VIVO DECLARAN SU SUJETO.** Son los **11** que
tu lectura clasifico `LO NOMBRA SIN ABRIRLO` y los **2** que salieron `ABRE UN
SUJETO YA CLAVADO` (`vuelta135_2e_mutacion_1.py` y `_2.py`, los dos por
`git show e12e4c362fe734ff:docs/loop/REPORTE.md`). **A los trece les falta
declararlo, no arreglarlo**, y eso lo dice tu propio registro en su campo
`que_haria_falta`. Una linea por arnes con el literal que la guarda busca.
**NINGUNA otra linea de esos ficheros se toca**, y lo compruebas con
`git diff --numstat` sobre `scripts/loop/` publicando las lineas anadidas por
fichero.

**2.b. LOS CUATRO QUE SI ABREN, CONGELADOS DE VERDAD.** Son
`vuelta157_tarea4b_mutacion_tachado.py` (`LECTURAS_DIRIGIDAS.md`),
`vuelta160_tarea7c_mutacion_guarda_cita.py` (`LECTURAS_DIRIGIDAS.md` e
`INTRA_DOMINIO_VEREDICTOS.jsonl`), `vuelta174_tarea1b_mutacion_esqueleto.py`
(`REPORTE.md`) y `vuelta150_2d_simular_op_c_05.py` (`master_graph.json`). **El
de la 160 merece cuidado y tu ya escribiste por que:** copia el fichero vivo a un
temporal en cada corrida, asi que parece congelado y no lo es. **Cada uno pasa a
un sujeto que no dependa de lo que el fichero vivo diga hoy**, y por cada uno
publicas: que abria, que abre ahora, y **la prueba de que su resultado ya no se
mueve** (correrlo dos veces, o contra dos cortes del fichero vivo, y que de lo
mismo). Si alguno no se puede congelar sin decidir algo que el encargo no dice,
**paras y lo traes**: eso es `AUDITOR.md` 3, una operacion cuyo texto no alcanza.

**2.c. Y SOLO ENTONCES, EL CABLEADO.** La guarda del sujeto congelado entra al
**rojo global de la bateria**. Antes de cablear, la corres y publicas su cifra con
su corte pegado (hoy da **17 de 103 al corte `c348de45f70f`**, medido por mi).
Despues de cablear, la vuelves a correr: **tiene que dar 0**. Si no da 0, **NO
CABLEAS**, publicas cuantas quedan y por que, y paras. **Un cableado que deja la
181 en rojo es peor que no cablear**, y ese es el motivo entero de esta tarea.

**2.d. NADA SE PODA DE LA NOMINA** (`AUDITOR.md` 6.1). Los arneses que esta
vuelta escriba entran en `verificar_mutaciones_viejas.py` con la cuenta entera y
la resta comprobada, **antes de la 181**, y el denominador va con su corte por la
1.d de la 179.

---

## TAREA 3. EL CORTE, CABLEADO DONDE TODAVIA FALTA

**EL HALLAZGO ES MIO Y ESTA MEDIDO EN LA SECCION 6 DEL ACTA 179.** No es una
caida tuya: tu tabla de tramos de la 2.a esta contada de su fichero, que es lo
que `EJECUTOR.md` 1 manda, y sus cifras eran verdad. **Lo que le falta es el
corte.** Tu 2.a publica 6 actos / 29 pares / 8 reales y 34 / 44 / 10; el mismo
instrumento corrido hoy da **14 / 39 / 18** y **26 / 34 / 0**, porque tu propia
TAREA 2 lo movio. Las dos son verdaderas y **sin corte no hay manera de saber
cual mira que**.

- Cablea el sello de `sello_de_corte()` **donde se genera la tabla de tramos** de
  `backlog_l03_resuelto.py`, no en una frase del reporte. Adjudicado por
  `banco 9.21` y por el punto 7.2 del acta 178, la misma extension que ya usaste
  para el denominador de la nomina.
- **Barre el resto:** publica la lista de toda cifra de ese instrumento y de
  `vuelta179_tarea2_cobertura_final.py` **que pueda moverse dentro de una vuelta**
  y di cuales llevan corte y cuales no. **Las que no lo lleven, lo llevan al
  terminar esta tarea.**
- Caso positivo por mutacion: dos cortes distintos con la misma cifra no se
  confunden, y la misma cifra con dos cortes distintos tampoco.

---

## TAREA 4. LAS DOS PENDIENTES BARATAS DE TU TAREA 5, QUE YA LLEVAN VUELTAS SUBIENDO

Las mediste tu en la 179 y las dos siguen sin instrumento. **Ninguna es de
opinion: las dos son texto que miente sobre su propia maquina.**

**4.a. EL DOCSTRING DE `scripts/loop/paso0_archivar_anterior.py`.** Sigue
hablando de **la vuelta anterior** cuando la maquina ya pregunta por **el reporte
que va a pisar**. **La maquina esta bien; el texto que la describe, no.** Lo
arreglas y publicas la linea vieja y la nueva, sin borrar la vieja del reporte.
**Y de paso escribes la guarda que hace visible la diferencia**: hoy las dos
preguntas coinciden y por eso la divergencia no se ve en corrida. Un caso
fabricado donde NO coinciden, que demuestre que la maquina responde a la pregunta
buena.

**4.b. LA GUARDA QUE FALTA EN LA DEPENDENCIA DEL `D.4` DE LA 174.** El esqueleto
del reporte **clona** `vuelta_del_reporte_del_arbol()` en vez de importarla, y
**nada avisa si el fichero del que se clono desaparece**. Lo declaraste en su
docstring y sigue sin instrumento. Escribe la guarda: si la fuente del clon no
existe, **CAE EN ROJO nombrandola**, y no sigue en silencio. Con su caso positivo
por mutacion sobre una ruta fabricada que no existe.

---

## TAREA 5. EL BACKLOG DE `OP-L-02`, MEDIDO Y NO LEIDO

`OP-L-03` queda con **18 pares reales y 0 sin lectura**, verificado por mi. La
vara del fundador (`vuelta150_3_relectura_expediente.py --corte <HEAD>`) dice que
**quedan cuatro fichas de trabajo real**: `OP-L-01`, `OP-L-02`, `OP-L-03` y
`OP-I-01`. **La vara es esa salida y nunca el campo `estado`.**

**MIDE `OP-L-02` CON LA MISMA VARA RESUELTA QUE CERRO `OP-L-03`, Y NO LEAS NI UN
PAR.** Lo que se pide es exactamente lo que la 177 y la 179 hicieron para
`OP-L-03`:

- Corre el instrumento viejo de `OP-L-02` por dentro, sin citarlo de memoria, y
  publica **los pares que da**.
- Pasa el resolutor de `P.1` y publica **los pares REALES**, o sea los que no
  estan ya en el archivo tras resolver a nodo vivo. **Las dos columnas van las
  dos y la vieja no se borra** (`banco 9.10`).
- Publica el reparto por tramo (actos ya leidos contra actos sin mirar) **con su
  corte pegado**, por la TAREA 3 de este mismo encargo.
- **Los dos caminos tienen que calzar** en todos los actos medidos, como en
  `backlog_l03_resuelto.py`. Si no calzan, publicas donde y paras.

**LO QUE NO HACES EN ESTA TAREA:** no lees ningun par, no escribes ningun
veredicto, no tocas el marcador y **no tocas el estado de ninguna ficha**
(`EJECUTOR.md` 4, modo de cierre). **Y NO TOCAS LOS CINCO PARES DE SALES
ROADMAP:** `docs/plan/LECTURAS_DIRIGIDAS.md` los deja expresamente como decision
revocable del fundador, y esta subida en el punto 8 del acta 179. Nombralos y
dejalos.

---

## LO QUE VALE PARA LAS CINCO

- **CADA TABLA SE CUENTA DE SU FICHERO** y cada cifra sale del instrumento
  corrido en esta vuelta. Una cifra tecleada al lado del fichero que la desmiente
  es la caida que `cerrar_reporte.py` ya caza sola desde la 179.
- **TODA RUTA QUE PUBLIQUES COMO PRUEBA ES UNA CIFRA PUBLICADA** (`AUDITOR.md` 4,
  letra del 5 sep). Si apunta a un fichero inexistente o de cero bytes, es caida
  de cifra.
- **TODA CIFRA DE BYTES O `sha` VA POR LAS DOS CONVENCIONES** mientras la del
  fundador no este fijada.
- **CICLO DE GATE 0 ENTERO Y EN SU ORDEN EN LAS DOS PUNTAS**, nunca `run_phase1`
  suelto: `run_phase1.py --reaplico-curaduria`, `etiquetas_de_cara.py --aplicar`,
  `sync_assets_web.py`, `git diff HEAD --numstat`, `engine/run_all_tests.py`,
  `npx tsc --noEmit` y `pnpm test`.
- **LA GUARDA DE `dataset/` ANTES DE CADA COMMIT.** `dataset/` no se toca en
  ninguna de las cinco tareas.
- **CASO POSITIVO POR MUTACION** en cada instrumento nuevo, y **todo arnes que
  escribas entra en la nomina en esta misma vuelta**, antes de la 181.
- **MARCA TUS DISCUTIBLES** y, cuando el discutible sea una clase, **marcalo sin
  publicar la clase en una tabla si quieres que se pueda leer a ciegas**: por la
  adjudicacion 7.1 del acta 179, un discutible cuya clase va en una tabla del
  reporte queda quemado como sujeto ciego y el auditor tiene que leer su base de
  evidencia en su lugar.
- **CIERRA Y ARCHIVA TU PROPIO REPORTE EN ESTA MISMA VUELTA**, con
  `cerrar_reporte.py` y `archivar_reporte.py --vuelta 180`, y coteja las tres
  copias en su fichero propio y fuera del reporte. **Van cuatro seguidas.**

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
