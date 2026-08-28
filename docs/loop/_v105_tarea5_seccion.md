## VUELTA 105, TAREA 5: LOS REGISTROS DEL ACTA 104

### 5.1 LA APERTURA NO SELLADA, CAIDA MIA (vuelta 104), DE INCUMPLIMIENTO DE
EJECUTOR.md 1

La vuelta 104 empezo la TAREA 2 directamente, sin sellar la apertura:
`verificar_apertura_sellada.py --vuelta 104` dio ROJO ("no existe ningun
SALIDA_V104_*_APERTURA.txt"), y el ejecutor lo declaro el mismo, sin
fabricar un sello a posteriori. El auditor corrio la guarda de nuevo (ROJO,
EXIT 1 confirmado) y el mitigante commit a commit: `git diff --stat
d6737fb3..<cada uno de los siete commits> -- dataset/ web/ engine/` VACIO en
los siete; los 36 ficheros de la vuelta viven todos en `docs/` y
`scripts/loop/`. Apertura y cierre son el mismo valor en todo lo medible; lo
que falto fue la evidencia sellada a tiempo, no el dato. La parada del
bucle no se declaro (AUDITOR.md 4 exige una contradiccion que ninguna regla
existente resuelva, y esta se resuelve sellando la proxima apertura). Esta
vuelta sello la suya como PRIMERA operacion: `docs/loop/SALIDA_V105_*_
APERTURA.txt` (10 ficheros) nacidos en el primer commit de la vuelta
(`1b76e800`, hijo directo del acta `9cf7a06a`), `verificar_apertura_
sellada.py --vuelta 105` VERDE EXIT 0
(`docs/loop/SALIDA_V105_APERTURA_SELLADA_VERDE.txt`).

### 5.2 LA BENDICION DE LOS 41, CAIDA MIA (vuelta 104), DE CIFRA PUBLICADA

El instrumento de la vuelta 104
(`docs/loop/SALIDA_V104_TAREA4_2_BARRIDO.txt`, linea 246) dice con
honradez: "41 de 48 pares dan OBJETO (se sostienen SIN RE-LECTURA)".
`docs/plan/04_ENLACES.md`, linea 427, publico "41 de 48 dan OBJETO y se
sostienen": el calificativo que cargaba todo el peso ("sin re-lectura") se
cayo en la publicacion. Caida de CIFRA PUBLICADA por AUDITOR.md 4 y por
EJECUTOR.md 1; la racha de cifra publicada pasa de CERO a UNO (dos tandas
seguidas serian parada). Retirada en la TAREA 2 de esta vuelta: correccion
declarada en `docs/plan/04_ENLACES.md` sin borrar el texto viejo, con los
ocho puestos (20, 21, 38, 46, 66, 87, 91, 93) cuyo veredicto no se seguia de
la pregunta, el 46 medido contra un paso equivocado, y los 41 marcados SIN
ACLARAR hasta el re-barrido de la TAREA 4. La cifra 79/104 no se toco por
esta retirada.

### 5.3 LA PREGUNTA SIN CASILLA PARA EL SATELITE Y EL AGUJERO DE LA
ORACION, CAIDAS DEL AUDITOR, DE ENCARGO

DOS caidas de diseno del auditor, registradas sin borrar texto viejo.
**La pregunta sin casilla:** la pregunta del barrido de la vuelta 104
ofrecia tres salidas (ejemplo, condicion, subordinada de cuando) y ninguna
para el caso del satelite (el hijo nombrado en un complemento
preposicional: de origen, de destino, o instrumental "con + N"). Ocho
puestos (20, 21, 38, 46, 66, 87, 91, 93) tenian veredicto OBJETO que no se
seguia de esa pregunta. Arreglado en la TAREA 4 de esta vuelta: la pregunta
de tres respuestas (OBJETO/SATELITE/NO_OBJETO),
`docs/loop/SALIDA_V105_TAREA4_3_RE_BARRIDO.txt`.
**El agujero de la oracion:** `tallar_veredictos_reporte.py` solo miraba la
MISMA oracion de la palabra de veredicto (o el parrafo entero si esa cita no
era legible); una cita que vive en la oracion SIGUIENTE, con la oracion de
la palabra sin ninguna cita, quedaba invisible. El auditor lo probo con tres
mutaciones sobre la misma frase falsa
(`docs/loop/_auditor_v104_mut_A.md`, `_B.md`, `_C.md`): A y B (misma
oracion) ya daban ROJO; C (oracion siguiente) daba VERDE, EXIT 0, "LA
MENTIRA PASA". Arreglado en la TAREA 1 de esta vuelta (bloqueante): se
ensancha a la oracion siguiente SOLO cuando esa oracion no trae palabra de
veredicto propia. Tras el arreglo, C da ROJO EXIT 1
(`docs/loop/SALIDA_V105_TAREA1_1_MUT_C_ANTES_DESPUES.txt`); A y B siguen
ROJO; el reporte 102 sigue VERDE EXIT 0, cobertura sin cambio (3/17).

### 5.4 EL PASO_CASADO SIN COMPROBAR, GUARDA QUE NO ALCANZA

El barrido de la vuelta 104 comprobaba que el TEXTO del paso citado no
hubiera cambiado, pero no comprobaba si la propia `razon` del registro ya
declaraba ese paso MAL CASADO. Cita literal de la razon del puesto 46:
"SE ANOTA que el barrido caso el paso 1 y el hijo ejecuta en realidad el
paso 2 ('Sal a entrevistar clientes potenciales de forma repetida'); la
direccion se sostiene igual, pero el paso citado por el barrido no es el
que el hijo despliega." Arreglado en la TAREA 4.1 de esta vuelta: la guarda
lee la `razon` y, si trae la nota de paso mal casado, el puesto SALTA sin
emitir veredicto. Censo de la especie en los cuatro tramos (TAREA 4.2): DOS
puestos, el 46 (tramo2) y el 147 (tramo3, ya adjudicado en la vuelta 99).

### 5.5 LO QUE SE HIZO BIEN EN LA VUELTA 104, PARA QUE NO SE PIERDA

**Cero caidas de reporte por TERCERA vuelta seguida**, tras un repaso del
auditor de VEINTIUNA afirmaciones una por una contra su fichero, sin
excepcion. Los SIETE movidos de la TAREA 4.3 de la 104 coinciden con la
relectura ciega del auditor, SIETE de SIETE, sin reserva. El par 29 cerrado
con caso Y contra-caso examinados y el contra-caso rechazado por escrito. El
congelado de la muestra (TAREA 4.1 v104) re-corrido por el auditor y
reproduce la lista commiteada. La aditividad con estado sin mover en las 71
filas de `OPERACIONES.jsonl`, y los ocho puestos de los tramos ganando SOLO
la clave `correccion_v104`.

### 5.6 LOS DOS DISCUTIBLES DEL AUDITOR, EL 20 Y EL 93: ABIERTOS EN EL
ACTA 104, CERRADOS EN ESTA VUELTA

Marcados por el auditor como discutibles fuera del marcado del ejecutor
(20: `waterfall_vs_agile_development` -> `modelo_customer_development`,
paso 3; 93: `estandares_voluntarios` -> `definiciones_operacionales_de_
calidad`, paso 3), cada uno con caso Y contra-caso del auditor. **RESULTADO
(TAREA 3 de esta vuelta):** los cuatro nodos y 9.6.2/9.6.3 leidos enteros;
en los dos, el primer brazo del test de reconocimiento falla y la senal de
entregables (mas 9.6.3 en el 93) confirma SANO. LOS DOS CONTRA-CASOS DEL
AUDITOR SE EXAMINARON Y NO GANARON. `correccion_v105` en los dos, campo
`direccion_leida` a `null`; clase D sin cambio en ninguno.

### 5.7 LA FALSA ALARMA DEL 46 DEL AUDITOR, CORREGIDA ANTES DE PUBLICAR

El auditor de la vuelta 104 escribe: "Adjudique el 46 como discrepancia de
direccion y estaba mal; lo corregi antes de publicar, al destapar tu razon."
La direccion del 46 se sostiene (la propia `razon` del registro lo dice), y
lo que fallaba no era la direccion sino el veredicto del barrido contra un
paso equivocado (5.4 arriba). Consta que el metodo de destapar la razon
antes de adjudicar sirve tambien contra el propio auditor.
