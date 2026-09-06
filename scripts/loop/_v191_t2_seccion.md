### TAREA 2. LA RELECTURA AL DOBLE DEL TRAMO DEL 3182. CERRADA, Y CON UNA DISCREPANCIA FUERA DEL MARCADO QUE TRAIGO ENTERA.

**QUIEN LA ENCARGA, PORQUE ESO ES LA MITAD DEL ASUNTO: LA ENCARGA EL AUDITOR.**
La TAREA 4 de la 190 dejo la deuda **medida y no auto encargada**, y la `4.5` del
acta 191 lo adjudico A FAVOR con esta razon leida hoy
(`docs/loop/ACTA_AUDITOR.md:67496`): *"`AUDITOR.md` 1.2 pone el doble en mi mano,
no en la suya, y LA ESCALADA SE ENCARGA, NO SOLO SE DECLARA es una regla contra
MI, no contra el ejecutor"*.

**LOS TRES PASOS, CADA UNO EN SU COMMIT, Y EL ORDEN LEIDO DE GIT Y NO
PROMETIDO.** El instrumento del cotejo lo comprueba solo y **CAE EN ROJO si no
puede leerlo**: aislamiento en **`2a414476`**, mis clases en **`5915621a`**, y el
destape se abre despues. `git status` del fichero de clases: **limpio**.

**EL TRAMO Y EL DOBLE, TODO CONTADO DE FICHEROS Y NADA TECLEADO**
(`SALIDA_V191_T2_AISLAMIENTO.txt`, disco 6348 bytes | LF 6348 bytes):

| lo que el encargo dice | lo que se conto hoy | |
|---|---|---|
| el tramo son 30 puestos y el 3182 esta dentro | 30 puestos de `SALIDA_V190_T4_CIEGA.txt`, el 3182 **DENTRO** | CALZA |
| son los mismos 30 que el auditor releyo en el acta 191 | diferencia simetrica contra `_auditor_v191_ciega_blind.txt`: **0** | CALZA |
| 441 consumidos antes de la 190 | **441**, union de cuatro ficheros | CALZA |
| 471 con los 30 de la tanda de la 190 | **471**, union de los cinco | CALZA |
| 30 vecinos, el doble exacto | **30** vecinos, **60** en total | CALZA |
| solape 0 con el tramo y 0 con el universo | **0** y **0**, y salen **POR CONSTRUCCION**: `evitar` va DENTRO de la llamada a `vecinos()`, no comprobado despues | CALZA |

**`vecinos()` VA IMPORTADA Y NO COPIADA** de
`scripts/loop/vuelta182_tarea1c_relectura_al_doble.py`: **su regla no se toca,
cambia lo que se le pasa** (`5.2` del acta 188). El aislador cerro con
**exitcode 0**, **0 fugas** del destape en la ciega, y las palabras `clase`,
`razon` y `DISCUTIBLE` aparecen **0 veces** en el texto ciego.

**EL COTEJO, CONTADO DE `docs/loop/SALIDA_V191_T2_COTEJO.txt`
(disco 6851 bytes | LF 6851 bytes) Y NO TECLEADO:**

| | cifra |
|---|---:|
| releidos | **30** |
| COINCIDEN | **23** |
| DISCREPAN | **7** |
| discrepancias DENTRO de mis dudosos | **6** (201, 716, 1369, 1813, 3087, 3183) |
| discrepancias FUERA de mis dudosos | **1** (2832) |
| dudosos mios que SI coincidieron | **7** de 13 |

**MI REPARTO: A 7, B 3, D 20. EL DEL ARCHIVO: A 4, B 1, C 1, D 24.** Los dos
declarados antes de destapar el primero, y el segundo contado del destape.

**LA QUE CAE FUERA DE MIS DUDOSOS ES EL 2832, Y VA ENTERA.** Dije **A** y el
archivo dice **D**. `eliminacion_barreras_orgullo_del_trabajo` contra
`remover_barreras_orgullo_trabajo`: ids casi gemelos, misma fuente (punto 12 de
Deming), y **tres de los cuatro pasos del corto se parecen a los del largo**. Yo
lo lei como repeticion. **La razon del archivo no es retorica y me tumba con una
medicion que yo no tenia:** `sim_tit 68,7` y una **transitividad de dos
subcumulos** (`eliminacion` = A = `orgullo_por_el_trabajo` en el 2816, pero
`remover` = D = `orgullo_por_el_trabajo` en el 2450, y `remover` vive con
`barreras_orgullo_trabajo` en el 2516, que a su vez es D contra `orgullo` en el
2564). **Los dos cumulos estan separados**, y el contenido lo respalda.
**Se resuelve a favor del archivo y no traigo ninguna correccion.**

**Y AQUI VA LA CONSECUENCIA, DECLARADA Y NO EJECUTADA, QUE ES EXACTAMENTE LA
LECCION DE LA `4.5`.** `AUDITOR.md` 1.2 dice que una discrepancia FUERA del
marcado **baja el credito de toda la tanda y obliga a releer ese tramo al
doble**. Eso vuelve a pasar hoy, sobre el tramo de la propia TAREA 2. **NO ME LO
AUTO ENCARGO**: quien encarga el doble es el auditor, y la 190 aprendio esa
leccion por la via cara. **Queda MEDIDA aqui, con su nombre y su cifra**, para
que el acta 192 decida.

**Y UNA MEDICION QUE LE IMPORTA A LA TAREA 5 Y QUE SALIO DE AQUI SIN
BUSCARLA.** De los 30 del doble, **3 llevan `DISCUTIBLE MARCADO`** (2832, 2911 y
3327), y **el 2832 es a la vez el unico que me tumbo fuera de mis dudosos**. O
sea: **el unico caso de esta tanda que sorprendio al lector SI llevaba la marca**,
que es lo contrario de lo que el acta 191 midio sobre los suyos (ocho que
tumbaron a dos lectores y **cero** con la marca). **Dos tandas de treinta apuntan
en direcciones opuestas, y eso no es una ley: es exactamente por que la TAREA 5
es una medicion y no un arreglo.**

**NO SE TOCO NINGUNA CLASE.** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y cierra
en **disco 4054129 bytes | LF 4054129 bytes**, y su **`sha256` disco
`0a77b5a35a962621` y `sha256` LF `0a77b5a35a962621`** son el mismo, medidos al
entrar y al salir del instrumento de aislamiento y otra vez al final del cotejo. `git diff --numstat -- dataset/`: **0 filas**.

**Y UN INSTRUMENTO QUE ANTES NO EXISTIA.** El cotejo de la vuelta 190 vive en
disco pero **ningun fichero commiteado lo produce**: `grep -rl "EL COTEJO,
DESPUES DE ABRIR EL DESTAPE" scripts/loop/` da **cero** ficheros, corrido en esta
vuelta. Una tabla que solo existe en su salida no se puede volver a correr, y
`EJECUTOR.md` 1 dice que **la tabla se imprime, no se teclea**. El de esta vuelta
es `scripts/loop/vuelta191_tarea2b_cotejo.py`, y **lee mis clases y el destape de
sus ficheros y cuenta**, sin decidir ninguna clase.
