# PARA ALEXIS. EL BUCLE SE DETIENE (3 sep 2026, auditor de la vuelta 160)

## EL MOTIVO, EN UNA LINEA

**Se disparo la regla del credito de `docs/loop/AUDITOR.md` seccion 4: DOS TANDAS
SEGUIDAS con caida de CLASE confirmada.** No es un fallo tecnico, no es doctrina
nueva y no es la campana consumada. **Es la regla que tu afinaste el 13 de agosto
haciendo exactamente lo que se le pidio: parar el bucle cuando la lectura falla
dos tandas seguidas en el mismo sitio.**

## LO QUE PASO, Y VA CON LA CARA QUE TIENE

  - **TANDA DE LA VUELTA 157 (lote 1 de lecturas dirigidas):** la `LD-OPC05-005`
    se publico como D, la relectura conjunta la devolvio a C, y eso es una caida
    de CLASE. Registrada en el acta 159. **Racha: uno.**
  - **TANDA DE LA VUELTA 159 (lote 2):** la `LD-OPC05-100` se publico como C. Yo
    la lei a ciegas como D en la vuelta 159 y la mande a relectura conjunta. **En
    la vuelta 160 el ejecutor la verifico contra los nodos y me dio la razon: pasa
    a D.** Y al releer el tramo entero encontro **tres mas de la misma costura**
    (`094`, `101`, `118`), todas por su cuenta y antes que yo. **Racha: dos.**
  - **La costura es siempre la misma y por eso importa:** la SEGUNDA LINEA de un
    par clasificado C. Es decir, se acepta como expansion algo que solo NOMBRA en
    vez de PROCEDIMENTAR.

## LO QUE NO ES, PARA QUE NO LO LEAS PEOR DE LO QUE ES

  - **NO es que el ejecutor este leyendo mal ahora.** En mi relectura ciega de la
    vuelta 160 leimos igual **23 de 24 casos**, con **cero discrepancias en los
    quince discutibles marcados**, y la unica discrepancia de fuera se resolvio
    **contra mi**: su razon ya nombraba el par que a mi me convencio y lo
    descartaba por escrito, con mejor argumento que el mio.
  - **NO es que se haya escondido nada.** El ejecutor declaro la parada el mismo
    en su reporte, con la cuenta hecha, y **no ejecuto ninguna accion de parada
    por su mano** (no escribio este fichero, no vacio el encargo y no pidio el
    merge), que es exactamente lo que su protocolo le manda.
  - **NO hay dato roto.** El grafo no se movio ni un byte en toda la vuelta.

## EL ESTADO EXACTO, MEDIDO POR MI HOY Y NO RECORDADO

  - **Rama:** `pasada-unica`. **HEAD:** `aa6bb622`. **Commit del acta 159:**
    `13cf21be`. **Corredor:** ocho commits, todos del ejecutor, cero intrusos.
  - **Fase:** III, EJECUCION, en modo continuo. El cribado y el recomputo estan
    cerrados; lo que corre son las lecturas dirigidas y las guardas.
  - **Marcador (archivo de cribado):** n **3.388**, **A 551, B 72, C 5, D 2.760**,
    huecos **0**, duplicados **0**.
  - **Censo del grafo:** **3.853** nodos, **3.169** vivos, **684** deprecados.
    **Aristas:** 8.780 / 8.740 / suma 17.520 / union dirigida 9.914, cero auto
    enlaces.
  - **Registro de citas OPC05:** **154** filas. Lectura dirigida **122**, hoy
    **14 en C y 108 en D**. Cribado **B 1 y D 31**.
  - **Gate 0: 26 en OK y 0 en FALLO**, corrido por mi con el ciclo entero y
    **identico linea por linea** al del ejecutor. **Motor 25/25.** **Web: 80
    ficheros, 1.030 pasadas y 3 saltadas.** **tsc: exit 0 y cero lineas.**
    **`git diff --numstat` de `dataset/ web/ engine/`: cero filas.**
  - **Expediente:** 71 fichas, 36 que no calzan, 24 congeladas declaradas, 12
    congeladas en silencio, 0 HECHA sin prueba, 7 en LISTA sin prueba.
  - **Fases:** 03 en 16/12/4 (`OP-M-02-ADMIT`, `OP-M-02-MEDIOS`, `OP-U-01`,
    `OP-U-02`); 06 en 16/16/0; 08 en 1/0/1 (`OP-V-01`); 09 en 3/0/3.
  - **Todo lo de arriba lo corri yo en esta vuelta con mis propios comandos.** Las
    salidas quedan en `docs/loop/_auditor_v160_*`.

## EL MURO QUE SIGUE DONDE ESTABA

La fase 08 **no cierra sin una sesion con credencial y contigo delante** (acta
149, seccion 3.10). El `.env` esta fuera del repo mientras el bucle corre, y eso
esta bien: la propia AUDITOR.md dice que si una suite las necesita, que falle
visible. **Esto no lo puede resolver ninguna vuelta mas.**

## LO QUE NECESITO DE TI, Y SON TRES DECISIONES SEPARADAS

**1. LA DECISION DE FONDO: QUE HACER CON LA VARA DE LA LECTURA DIRIGIDA.**
Las cuatro caidas de las dos tandas son todas de la misma especie, y la especie
tiene nombre desde el acta 158: **nombrar no es procedimentar**. La vara existe y
esta escrita, pero se ha ido estrechando vuelta a vuelta (la `122`, luego la
regla de la instancia de la 6.5, luego la `100`), y **el ejecutor lo dijo en su
propio reporte**: leyo el ultimo tramo *"con la vara recien estrechada"* y por eso
marco quince discutibles de treinta y siete, mas del doble de lo normal. Las
opciones, y no elijo yo:

  - **(a) Congelar la vara y seguir.** Se escribe la vara definitiva en un solo
    sitio citable, con sus casos aceptados y excluidos (`052` y `095` aceptan,
    `122` y `100` excluyen), y el bucle reanuda con la racha a cero. Es lo mas
    barato y ataca la causa real, que es que la vara se movia.
  - **(b) Releer el saco entero con la vara de hoy.** Hoy quedan **14 en C** y las
    catorce tienen ya dos lecturas independientes o mas (cinco de ellas tres). Una
    pasada mas seria trabajo honesto pero no barato.
  - **(c) Parar el frente de lectura dirigida y dejar las C como estan.** El resto
    de la campana no depende de ellas: lo que falta de verdad es el muro de la
    fase 08, que es tuyo.

**2. SI REANUDAS, CON QUE MODELOS.** Ahora mismo: ejecutor Opus 5, auditor Opus 5.
La regla del credito no dice nada de esto; lo pregunto porque en cierres
anteriores lo cambiaste antes de un tramo distinto.

**3. LA DEUDA MEDIDA QUE DEJO ANOTADA, POR SI QUIERES QUE ENTRE EN EL PRIMER
ENCARGO AL REANUDAR.** No la arreglo yo porque el bucle se detiene aqui:

  - **El instrumento del alcance de P.16 envejece solo.**
    `scripts/loop/vuelta159_tarea5_alcance_p16.py` excluye a los buscadores **por
    nombre**, asi que hoy da **15** en vez de 12 y sale exit 1. Lo revise: **los
    tres nuevos son de la vuelta 160 y ninguno trae el defecto** (dos son
    buscadores y el tercero usa la huella de contenido como vara). **La cifra del
    reporte es correcta; lo que hay que arreglar es la exclusion.**
  - **El contenido de los seis assets de `sync_assets_web` nunca se audito.**
    Comprobamos que corre y que no deja diferencia, pero **nadie ha mirado lo que
    escribe**. Lleva pendiente desde el acta 157, o sea cuatro actas.
  - **La definicion de SEGUNDA LECTURA INDEPENDIENTE no esta escrita en ningun
    sitio.** Yo mido hoy **120 de 122** con marca de segunda lectura y **82 con
    dos marcas**; el acta 158 publico **84** con otra definicion. **No copio esa
    cifra ni la mia encima de la suya: lo que falta es la definicion, no el
    numero.**

## COMO SE RETOMA

1. Decides el punto 1 y, si quieres, el 2 y el 3.
2. Escribes tu decision en `docs/loop/paradas/` con la forma de las anteriores
   (un fichero de planteo y uno de `-DECISION`), que es de donde las reglas nuevas
   entran al bucle sin inventarse.
3. Se escribe el encargo de la vuelta 161 en `docs/loop/PROMPT_SIGUIENTE.md`, que
   **hoy queda vacio a proposito**, y se relanza. **La racha del credito se
   reinicia solo si tu decision lo dice**; yo no la reinicio por mi cuenta.

## Y EL MERGE

**No lo pido y no lo hago.** `pasada-unica` no se funde a staging ni a produccion
por mano del bucle, ni ahora ni al final: eso es tuyo y solo tuyo. **La campana no
esta consumada**, y esta parada no es la parada feliz.
