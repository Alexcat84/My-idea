Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

Eres el ejecutor de la vuelta 181 de la campana My Idea. FASE III, EJECUCION,
rama `pasada-unica`. Lee `docs/loop/EJECUTOR.md` entero antes de empezar y sigue
su ciclo: bloque de apertura corrido ENTERO y ANTES de la primera operacion (con
el desfase del calibrado DENTRO de el), esqueleto del reporte abierto al empezar
con sus filas vacias, cada tarea ANEXA su fila al cerrarse, y el cierre lo talla
`scripts/loop/cerrar_reporte.py`.

**ESTA ES LA VUELTA DE BATERIA, Y NO LLEVA NADA MAS.** `AUDITOR.md` 6.1: la
bateria corre CADA CINCO, en VUELTA PROPIA, y **la propia es esta**, adjudicada en
el acta 176 punto 7.8 y reconfirmada en las actas 178, 179 y 180. La 180 fue la
ULTIMA que declaro el hueco. **AQUI SE CORRE.**

**EL TOPE DE ESTA VUELTA ES DOS SUB-TAREAS, Y NO ES UN DESCUIDO: ES LA
ADJUDICACION 6.8 DE MI ACTA 180.** `AUDITOR.md` 6.2 devolvio el tope a cinco, pero
la 6.1 y la 6.2 salen de la MISMA parada del 5 sep 2026 y la 6.2 se concedio
*"combinada con la (a)"*, o sea subordinada a ella. **La vuelta de bateria no
lleva trabajo de plan al lado.** El tope vuelve a cinco en la 182.

**LO QUE NO ENTRA EN ESTA VUELTA, DICHO PARA QUE NO SE COUELE:** no se lee ningun
par, no se escribe ningun veredicto, no se toca el marcador, no se toca el estado
de ninguna ficha, no se toca `docs/plan/`, no se arregla la `P.1` de tu reporte y
no se toca `cerrar_reporte.py`. **Las dos van a la 182 y estan escritas en los
puntos 6.6 y 6.8 de mi acta 180.**

---

## TAREA 1 (BLOQUEANTE). LOS REGISTROS, Y LO QUE HEREDAS DE MI ACTA 180

**1.a. LO QUE MI ACTA LEVANTA CONTRA LA 180, Y ES UNA SOLA COSA.** Anota en tu
reporte, leyendolo de `docs/loop/ACTA_AUDITOR.md` (cabecera en la linea `62449`) y
citando la linea de cada cosa que copies:

- **UNA CAIDA DE REPORTE, LA `E.1`, Y ACUMULA.** La cabecera de tu seccion 9 salio
  `## 9. LA BATERIA DE MUTACIONES, CORRIDA ENTERA Y SOLA AL CIERRE` **y la bateria
  no corrio**. La causa esta medida en la seccion 5 de mi acta: pasaste a
  `--bateria` el fichero `docs/loop/SALIDA_V180_HUECO_BATERIA.txt`, que **si
  existe y trae 21 lineas**, asi que `cerrar_reporte.py` entro por la rama del
  `if lineas_bat:` en vez de la del hueco, y con eso **`hueco_declarado_que_falta()`
  no corrio sobre tu seccion 9**. Las 177, 178 y 179 pasaron
  `SALIDA_V<N>_BATERIA.txt`, un fichero que NO existe, y por eso entraron por la
  rama buena. **La racha de reporte pasa de CERO a UNO.**
- **NO HAY NINGUNA CAIDA DE CIFRA PUBLICADA.** Racha de cifra publicada **0**.
  Verifique una a una las cifras del bloque del hueco y **las tres son ciertas**.
- **NO HAY NINGUNA CORRECCION DECLARADA QUE ARRASTRES.**
- **TUS CINCO DISCUTIBLES QUEDAN ADJUDICADOS A TU FAVOR LOS CINCO**, puntos 6.1 a
  6.5 de mi acta. El `D.1` ademas **corrige mi propio encargo**, y lo registro como
  caida mia: `vuelta174_tarea1b_mutacion_esqueleto.py` no abria ningun fichero
  vivo y tenias razon.
- **MI CAIDA PROPIA, LA TERCERA SEGUIDA**, esta en la seccion 2 de mi acta con el
  remedio que ata al auditor de esta vuelta. **No es trabajo tuyo**, pero **lo
  citas en tu reporte** para que quede en el carril de lectura.

**1.b. Y ANOTAS LO QUE NO SE HACE AQUI Y CUANDO SE HACE**, con su punto de acta:
la `P.1` (`vuelta172_tarea1c_guarda_que_mordio.py`, en rojo y fuera del censo)
queda adjudicada en el **6.6**, y el remedio del `E.1` en el **6.8**. **Las dos en
la 182, no aqui.**

---

## TAREA 2. LA BATERIA DE MUTACIONES, ENTERA, SOLA, Y CON SU RELOJ

**ESTA ES LA TAREA. NO HAY OTRA.**

**2.a. LA CORRIDA, ENTERA Y SIN TRAMOS.** `scripts/loop/verificar_mutaciones_viejas.py`
**sin `--tramo`**, sobre la nomina entera, que al cierre de la 180 tiene **108
entradas** (censo 168, fuera de la nomina 60), medido por mi. **Cada entrada se
corre DOS VECES**, que es el cotejo de reproducibilidad de la vuelta 141, y ese
cotejo **no se afloja**. La salida va a `docs/loop/SALIDA_V181_BATERIA.txt`, con
**ese nombre exacto y sin ninguna palabra en medio**, y se publica en tu seccion 9
**completa y sin recortar**.

**Y AQUI VA LA UNICA GUARDA NUEVA QUE ESTA VUELTA LLEVA, QUE ES DE UNA LINEA Y
NACE DE LA `E.1`:** publica en tu reporte, leido de la salida del propio
`cerrar_reporte.py`, el valor de **`vuelta que lleva dentro el nombre del fichero`**.
**Tiene que decir 181.** Si dice `None` o dice otro numero, **paras**: significa
que el fichero que le pasaste no es la bateria de esta vuelta, y ese es exactamente
el agujero por el que la 180 se colo.

**2.b. EL RELOJ, MEDIDO EN ESTA CORRIDA Y NO ELEGIDO A OJO.** Tu propia seccion 7
subio el grano del tope de 10 minutos como pendiente, y dijo que **se mide EN LA
181 con el reloj de esa corrida**. Publica:

- el **tiempo total** de la corrida entera,
- el **tiempo por entrada**, con su **maximo, su minimo y su mediana**, y **el
  nombre del arnes mas lento**,
- y **si el tope de 10 minutos se toco o no**, con la cifra al lado y no con un
  adjetivo.

**Se mide, se publica y no se cambia nada:** el grano del tope es decision del
fundador y aqui solo se le pone la medida delante.

**2.c. EL VEREDICTO DE LAS SEIS PIEZAS, UNA A UNA.** `hay_rojo_al_cierre()` decide
el rojo global con seis piezas y esta vuelta es la primera que las corre todas
juntas desde que la 180 cablo la sexta. **Publica el estado de cada una por
separado** (perdidas, no mordio, no reproducible, faltan de la nomina, invisibles
al censo, sujeto sin congelar), **cada una con su cifra**, y no solo el color
final. Al cierre de la 180 las seis daban cero bajo mi mano; **si alguna sale
distinta, la nombras con su arnes y su cifra**.

**2.d. LA DOBLE CORRIDA SE COTEJA Y SE PUBLICA COMO TAL.** Cuantos arneses dieron
salida identica en sus dos corridas y cuantos no. **Si alguno no reproduce, se
nombra**: esa es la mitad entera del cotejo de la 141.

**2.e. NADA SE PODA DE LA NOMINA** (`AUDITOR.md` 6.1, y no es discutible). Si esta
vuelta no escribe ningun arnes, la nomina sigue en **108** y lo dices con su corte
pegado. **Y si la bateria destapa un arnes roto, NO lo borras ni lo sacas de la
nomina: lo dejas en rojo, lo nombras y lo traes.** Borrar guardas es lo que la
casa reserva.

---

## LO QUE VALE PARA LAS DOS

- **CADA TABLA SE CUENTA DE SU FICHERO** y cada cifra sale del instrumento corrido
  en esta vuelta. Una cifra tecleada al lado del fichero que la desmiente es la
  caida que `cerrar_reporte.py` ya caza sola desde la 179.
- **NINGUNA CIFRA QUE PUBLIQUES SALE DE UN FICHERO QUE NO ESCRIBA UN INSTRUMENTO
  DEL REPO.** Es la mitad agravante de la `E.1`: el bloque del hueco de la 180
  entro tecleado, salio cierto, y nadie lo comprobo.
- **TODA RUTA QUE PUBLIQUES COMO PRUEBA ES UNA CIFRA PUBLICADA** (`AUDITOR.md` 4,
  letra del 5 sep). Si apunta a un fichero inexistente o de cero bytes, es caida
  de cifra.
- **TODA CIFRA DE BYTES O `sha` VA POR LAS DOS CONVENCIONES** mientras la del
  fundador no este fijada. Va por octava acta.
- **CICLO DE GATE 0 ENTERO Y EN SU ORDEN EN LAS DOS PUNTAS**, nunca `run_phase1`
  suelto: `run_phase1.py --reaplico-curaduria`, `etiquetas_de_cara.py --aplicar`,
  `sync_assets_web.py`, `git diff HEAD --numstat`, `engine/run_all_tests.py`,
  `npx tsc --noEmit` y `pnpm test`.
- **LA GUARDA DE `dataset/` ANTES DE CADA COMMIT.** `dataset/` no se toca en
  ninguna de las dos tareas.
- **MARCA TUS DISCUTIBLES** antes de saber si aciertas, y si alguno es una clase,
  **no publiques esa clase en una tabla** o lo quemas como sujeto ciego
  (adjudicacion 7.1 del acta 179).
- **CIERRA Y ARCHIVA TU PROPIO REPORTE EN ESTA MISMA VUELTA**, con
  `cerrar_reporte.py` y `archivar_reporte.py --vuelta 181`, y coteja las tres
  copias en su fichero propio y fuera del reporte. **Van cinco seguidas.**

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice
una regla vigente, paras y lo traes. No adivines.
