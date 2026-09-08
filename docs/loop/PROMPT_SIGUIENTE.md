# ENCARGO DE LA VUELTA 212 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

**RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3): ningun arnes, guarda ni lector
nuevo. Lo que escribas en `scripts/loop/` lleva prefijo `_v212_`, fuera del censo y
fuera de la nomina. **La nomina de la bateria sigue CONGELADA EN 135 y no se poda.**

**LA 212 NO ES VUELTA DE BATERIA.** La 210 la corrio entera (11 tramos, verificado por
mi en git) y la cadencia de cinco de `AUDITOR.md` 6.1 pone la siguiente en la **215**.
La seccion 9 de tu reporte cierra con **HUECO DECLARADO Y MEDIDO**: nombre del fichero,
bytes medidos y atribucion, **las tres juntas**, por el carril de `rama_de_la_seccion9()`.

**DOS SUB-TAREAS.** El tope de cinco esta disponible (el disparador de `AUDITOR.md` 6.2
se cumplio: la 209, la 210 y la 211 cerraron su propio reporte con `cerrar_reporte.py`),
pero el trabajo que queda cabe en dos y una adjudicacion favorable no engorda un encargo.

**SIGUE RIGIENDO LA OBLIGACION DE DICTADO DEL `6.6` DEL ACTA 210** (linea **74203** de
`docs/loop/ACTA_AUDITOR.md`): toda cita de un acta anterior lleva **LA LINEA** donde vive
el texto citado, **y la linea se LEE, no se recuerda**.

**Y SE ANADE UNA, QUE SALE DE LA `4.1` Y LA `7.3` DE MI ACTA DE HOY Y NO CUESTA CODIGO:**

> **TODA TABLA QUE UN COMPOSITOR ARME LEYENDO FILAS DE UNA SALIDA PUBLICA, EN LA MISMA
> LINEA, CUANTAS FILAS ARMO; Y SI AL LADO VA UNA CIFRA DE CUANTAS DEBERIA HABER, LAS DOS
> SE ESCRIBEN JUNTAS.** Motivo medido en la 211: la `2.e` se titulaba *LAS TRES SEDES*,
> decia **3 de 3** y su tabla llevaba **DOS** filas, porque el patron del compositor
> usaba `(\w+)` donde el instrumento escribe `NO COINCIDEN`, que son dos palabras. **El
> patron estaba estructuralmente ciego al unico caso que habia que publicar.** No
> arregles ese compositor: es `_v211_*` y muere con su vuelta. **Cumple la regla en los
> tuyos.**

---

## TAREA 1. LOS REGISTROS, Y LA RELECTURA CONJUNTA DEL PUESTO 730

**1.a. EL ACTA 212 DEL AUDITOR EMPIEZA EN LA LINEA 74334 de `docs/loop/ACTA_AUDITOR.md`**
(mi acta de la 211). Leela desde ahi y cita por linea, no de memoria.

**1.b. LA RELECTURA CONJUNTA DEL PUESTO `730`, QUE ES EL CUERPO DE ESTA TAREA.**

MI CASO, ESCRITO CON SU EVIDENCIA, ESTA EN LA `7.1` DE MI ACTA. En una linea: **el
veredicto `A` del puesto 730 se sostiene sobre una lectura que su propia razon llama
vieja, y la ratificacion del banco `9.6.1` del 12 ago 2026 (*EL CERO ENTRA EN LA REGLA*)
la jubilo.** Lo que yo medi y publico para que lo verifiques o lo tumbes:

- La razon del archivo dice de si misma: *"LA CLASE QUEDA EN A por la lectura vieja del
  cero-enlazados (...) si manda el contenido (...) o sea CONTINUA, y seria D (...) lo dejo
  anotado aqui en vez de elegir yo"*.
- El banco `9.6.1` dice: *"CERO ENLAZADOS ES EL CASO EXTREMO DEL MITAD-O-MENOS. Sin ni un
  hermano enlazado no hay mayoria de la que tirar: la silueta no dice nada y manda el
  contenido"*.
- Medido por mi contra `dataset/metadata/master_graph.json`:
  `colaboracion_cadena_suministro` tiene **UNA** arista de salida, a
  `optimizacion_tecnologia_cadena_suministro`, que **no es ninguno de sus hijos de paso**.
- Cerco medido por mi sobre las 3388 filas: **13** razones nombran el cero-enlazados
  (A 4, D 9); **11** nombran *el choque de la seccion 19*, y **diez de esas once son los
  diez que la ratificacion del banco declara ya resueltos** (490, 497, 522, 555, 557, 568,
  582, 586, 610, 624). **El 730 es el undecimo y no esta en esa lista.** Es ademas **el
  UNICO del archivo que dice "lectura vieja" y el UNICO que dice "seria D"**.
- Y no es rezagado anterior a la regla: **el 730 se cribo DESPUES del 658 y del 678**, que
  son los dos casos que forzaron la ratificacion.
- De los diez ya resueltos, los dos que quedaron en `A` (568 y 586) lo estan **por
  contenido**, no por silueta. **Nadie sostiene una `A` por la silueta.**

**LO QUE TE TOCA, Y EN ESTE ORDEN:**

1. **VERIFICA CONTRA EL GRAFO, NO CONTRA MI ACTA.** Resuelve a nodo vivo las aristas de
   `colaboracion_cadena_suministro` y publica cuantos de sus hijos de paso enlaza.
   Publica tambien mis cinco cifras de cerco recomputadas por ti (13, 4, 9, 11, 10).
2. **APLICA LA VARA TU MISMO** y publica que devuelve, con la direccion del `9.6.2` (que
   anade el HIJO a la MADRE, nunca al reves) y la vara de LINEA o PROCEDIMIENTO del
   informe 67.6. **Escribe QUE le queda a cada nodo cuando le quitas lo que dice el otro.**
3. **DECIDE CON LA VARA, NO CON MI CASO.** Si tu medicion tumba mi lectura, **dilo y no lo
   cambies**: un auditor que se equivoca prefiere que se lo digan a que se lo obedezcan.
4. **SI SE CONFIRMA, LA CORRECCION VA POR EL CARRIL DEL BANCO `9.10`:** correccion
   **declarada** en la fila del 730, con **el texto viejo entero encima y sin tacharlo**, y
   **el marcador RECOMPUTADO del archivo con `apertura_del_auditor.marcador()`**, nunca
   restado a mano. Publica el marcador **antes y despues**, los dos.
5. **GUARDA OBLIGATORIA:** cuenta las filas de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` al
   entrar y al salir (**3388** las dos veces si solo cambias una clase), y publica la sede
   **por las dos convenciones**, con `sha256` distinto al salir. **Y el caso rojo por
   mutacion ANTES de escribir nada.**

**1.c. LA `P.2`, QUE YA TIENE ADJUDICACION Y SOLO FALTA EJECUTARLA** (mi `6.7`). El campo
`nodos` de `OP-F-04-HOR` mide **14** y su propia `adjudicacion` dice *"LEIDOS LOS 13"*.
**Correccion declarada por el banco `9.10`** sobre el campo `adjudicacion`, con el texto
viejo entero encima, **citando `docs/plan/01_FUENTES.md` lineas 1168 y 1453**, que es donde
vive el motivo (el 14.º volvio por decision del fundador). **NO toques el campo `nodos` ni
el `estado`.** Mismas tres guardas que la `1.b` de la 211 (sede por las dos convenciones al
entrar y al salir, cuentas por `estado` antes y despues mas `git diff --numstat` sobre
`docs/plan/`, y la recarga del `jsonl` linea a linea), y **el rojo probado por mutacion**.

**1.d. REGISTRA EN EL REPORTE, SIN EJECUTARLAS, LAS CUATRO ADJUDICACIONES QUE NO TE PIDEN
TRABAJO:** mi `6.2` (el criterio de hecho de una ficha de fase 10 es el general, citando la
linea **9** de `docs/plan/08_VERIFICACION.md` y su titulo *"EL CRITERIO DE HECHO, y es uno
solo"*), mi `6.3` (**`OP-I-01` NO se cierra y su `estado` se queda en `LISTA` con motivo
escrito**), mi `6.4` (el `NO CUBRE` del punto 2 se sostiene) y mi `6.5` (el cubo se llama
desde hoy **LOS PASOS DE HOY SON LOS DEL BLOQUE 1**, no *EL BLOQUE YA VIVE APARTE*).
**No toques `OP-I-01`. No marques las 95 entradas del inventario: eso sube al fundador.**

---

## TAREA 2. LA COLA DE RELECTURA, BAJO LA REGLA QUE LA 730 DEJA PUESTA

**Esta tarea SOLO se abre si la `1.b` CONFIRMA el cambio del 730.** Si lo tumba, esta
tarea no existe y lo escribes asi en tu reporte, con la cifra que la tumbo.

**QUE ES:** el cerco que yo medi encontro **13** razones que nombran el cero-enlazados y
**4 de ellas estan en `A`**. Diez estan cubiertas por la ratificacion. **Lo que no medi, y
por eso lo encargo en vez de afirmarlo:** si alguna de esas cuatro `A` (fuera del 730)
sostiene su clase **por la silueta y no por el contenido**.

1. **LISTA LAS CUATRO** con su puesto, sus dos nodos y su razon entera.
2. **PARA CADA UNA, publica DE QUE depende su clase**, citando la frase de su propia razon:
   **silueta** (cuantos hermanos enlaza la madre) o **contenido** (la vara de LINEA o
   PROCEDIMIENTO). **Esto es lectura y cita, no re-cribado.**
3. **LAS QUE DEPENDAN DEL CONTENIDO SE QUEDAN COMO ESTAN Y LO DICES.** Ya verifique dos
   (568 y 586) y las dos son de contenido; **verificalas tu tambien y publica si coincides
   conmigo o no.**
4. **SI APARECE ALGUNA QUE DEPENDA DE LA SILUETA, NO LA CAMBIES: MARCALA COMO DISCUTIBLE Y
   TRAELA.** Una cosa es corregir el par que su propia razon deja sin resolver y otra es
   abrir una cola de re-cribado por mi cuenta. **Yo no la abro y tu tampoco.**

---

## LAS GUARDAS QUE NO SE AFLOJAN, Y VAN AQUI PARA QUE NO HAYA QUE BUSCARLAS

- **CICLO ENTERO DE GATE 0, LOS DOS LADOS**, nunca `run_phase1.py` a secas.
- **SIMULACION PREVIA** sobre copia en memoria de toda escritura en `docs/plan/` o en
  `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, y **CASO POSITIVO POR MUTACION** de cada
  computo, **corrido ANTES de escribir nada** y con su salida sellada.
- **CERO cifras tecleadas.** Toda cifra sale de la salida de un instrumento y cita su
  fichero. **Es la caida `C.2` de la 211 y la `4.1` que le anote: la unica defensa que
  funciona es contar el fichero.**
- **CABECERA TALLADA** con `tallar_cabecera_reporte.py --fase04 --vuelta 212` y cotejada
  con `--comparar`.
- **CIERRA TU PROPIO REPORTE** con `scripts/loop/cerrar_reporte.py` y **sella su salida**
  en `docs/loop/SALIDA_V212_CERRAR_REPORTE.txt`.
- **MARCA TUS DISCUTIBLES ANTES DE SABER SI ACIERTAS.** Los de la 211 funcionaron: **de
  mis cinco fallos de ciega, los dos que cayeron dentro del marcado son los dos que tu
  marca habia anunciado por nombre.** Eso es la guarda haciendo su trabajo.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una
regla vigente, paras y lo traes. No adivines.
