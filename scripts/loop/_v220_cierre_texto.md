## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**TODAS SALEN DE** ``docs/loop/SALIDA_V220_CIERRE_INTEGRAL.txt``, **11281 bytes en disco y 11281 normalizado a LF**, que corrio con
**exitcode 0**. **NINGUNA ESTA TECLEADA.**

### 3.1. EL CICLO ENTERO DE GATE 0, LOS DOS LADOS

- CIFRA salidas selladas del ciclo: 18 | CIFRA que deberia haber: 18
- CIFRA ausentes: 0 | CIFRA de cero bytes: 0
- CONSOLA APERTURA  docs/loop/SALIDA_V220_CICLO_GATE0_APERTURA_CONSOLA.txt | 1077 bytes en disco y 1077 normalizado a LF | peor exitcode que declara: 0
- CONSOLA CIERRE    docs/loop/SALIDA_V220_CICLO_GATE0_CIERRE_CONSOLA.txt | 1073 bytes en disco y 1073 normalizado a LF | peor exitcode que declara: 0

### 3.2. LAS TRES SUITES SOLAS

- SUITE motor  docs/loop/SALIDA_V220_T2_SUITE_MOTOR.txt | EXITCODE 0 | 1131 bytes en disco y 1131 normalizado a LF
- SUITE tsc    docs/loop/SALIDA_V220_T2_SUITE_TSC.txt | EXITCODE 0 | 24 bytes en disco y 24 normalizado a LF
- SUITE web    docs/loop/SALIDA_V220_T2_SUITE_WEB.txt | EXITCODE 0 | 336 bytes en disco y 336 normalizado a LF

### 3.3. EL MARCADOR Y EL CENSO, RECOMPUTADOS CON SU COMANDO

- MARCADOR: n 3388 | A 550 | B 71 | C 5 | D 2762 | huecos 0
- CENSO: nodos 3853 vivos 3169 deprecados 684
- ARISTAS: siguientes 8780 previos 8740 suma 17520 union 9914

### 3.4. LAS TRECE CIFRAS, COTEJADAS CONTRA LAS QUE LA 219 PUBLICO

- COTEJO marcador n             | LA MIA 3388     | la 219 3388     | esperado quieta, sin movimiento                         | QUIETA Y CALZA
- COTEJO marcador A             | LA MIA 550      | la 219 550      | esperado quieta, sin movimiento                         | QUIETA Y CALZA
- COTEJO marcador B             | LA MIA 71       | la 219 71       | esperado quieta, sin movimiento                         | QUIETA Y CALZA
- COTEJO marcador C             | LA MIA 5        | la 219 5        | esperado quieta, sin movimiento                         | QUIETA Y CALZA
- COTEJO marcador D             | LA MIA 2762     | la 219 2762     | esperado quieta, sin movimiento                         | QUIETA Y CALZA
- COTEJO marcador huecos        | LA MIA 0        | la 219 0        | esperado quieta, sin movimiento                         | QUIETA Y CALZA
- COTEJO censo nodos            | LA MIA 3853     | la 219 3853     | esperado quieta, sin movimiento                         | QUIETA Y CALZA
- COTEJO censo vivos            | LA MIA 3169     | la 219 3169     | esperado quieta, sin movimiento                         | QUIETA Y CALZA
- COTEJO censo deprecados       | LA MIA 684      | la 219 684      | esperado quieta, sin movimiento                         | QUIETA Y CALZA
- COTEJO aristas siguientes     | LA MIA 8780     | la 219 8780     | esperado quieta, sin movimiento                         | QUIETA Y CALZA
- COTEJO aristas previos        | LA MIA 8740     | la 219 8740     | esperado quieta, sin movimiento                         | QUIETA Y CALZA
- COTEJO aristas suma           | LA MIA 17520    | la 219 17520    | esperado quieta, sin movimiento                         | QUIETA Y CALZA
- COTEJO aristas union          | LA MIA 9914     | la 219 9914     | esperado quieta, sin movimiento                         | QUIETA Y CALZA

- CIFRA cifras cotejadas: 13 | CIFRA que NO calzan: 0

## 4. LO QUE SE TOCO, Y LO QUE NO

### 4.0. LO QUE LA APERTURA SELLADA DICE, AFIRMADO AQUI Y NO CALLADO

**UNA CIFRA AUSENTE Y UNA CIFRA QUE CALZA NO SON LO MISMO**, asi que la seccion
4 lo dice en vez de darlo por sabido. Las dos salen de ``docs/loop/SALIDA_V220_APERTURA.txt``,
**7388 bytes en disco y 7388 normalizado a LF**, que se sello ANTES de la primera operacion:

- CIFRA lineas de git status --porcelain AL ENTRAR, leida de la apertura sellada: 1
- CIFRA filas de git diff --numstat -- dataset/ AL ENTRAR: 0

### 4.1. LAS TRECE SEDES, COTEJADAS POR sha256 ENTRE LA APERTURA Y EL CIERRE

- SEDE docs/plan/INVENTARIO.jsonl                 | al abrir 43cea06634e6fc1a | al cerrar 43cea06634e6fc1a | QUIETA | 629533 bytes en disco y 629533 bytes normalizado a LF | cotejo de los dos sha256
- SEDE docs/plan/OPERACIONES.jsonl                | al abrir 650578474361eb2b | al cerrar 650578474361eb2b | QUIETA | 517181 bytes en disco y 517181 bytes normalizado a LF | cotejo de los dos sha256
- SEDE docs/plan/08_VERIFICACION.md               | al abrir 578eeefab6db2fd4 | al cerrar 578eeefab6db2fd4 | QUIETA | 73652 bytes en disco y 73652 bytes normalizado a LF | cotejo de los dos sha256
- SEDE docs/plan/07_ADUANA.md                     | al abrir 6f5f91619adec6e0 | al cerrar 6f5f91619adec6e0 | QUIETA | 3815 bytes en disco y 3723 bytes normalizado a LF | cotejo de los dos sha256
- SEDE docs/plan/01_FUENTES.md                    | al abrir f965abf6c3ca95c3 | al cerrar f965abf6c3ca95c3 | QUIETA | 128187 bytes en disco y 126666 bytes normalizado a LF | cotejo de los dos sha256
- SEDE docs/plan/02_DESTEJIDOS.md                 | al abrir NO_MEDIDA_AL_ABRIR | al cerrar ba8476e48144db2c | QUIETA | 478539 bytes en disco y 473876 bytes normalizado a LF | NO MEDIDA AL ABRIR: su quietud se mide con git diff --numstat HEAD, 0 filas
- SEDE docs/INTRA_DOMINIO_VEREDICTOS.jsonl        | al abrir 4a6f32cf7ea71096 | al cerrar 4a6f32cf7ea71096 | QUIETA | 4066944 bytes en disco y 4063556 bytes normalizado a LF | cotejo de los dos sha256
- SEDE docs/INTRA_DOMINIO_INFORME.md              | al abrir NO_MEDIDA_AL_ABRIR | al cerrar c05b6bcd20188a9c | QUIETA | 943970 bytes en disco y 943970 bytes normalizado a LF | NO MEDIDA AL ABRIR: su quietud se mide con git diff --numstat HEAD, 0 filas
- SEDE docs/BANCO_DE_TEXTOS.md                    | al abrir 8adbd60239509bb4 | al cerrar 8adbd60239509bb4 | QUIETA | 186490 bytes en disco y 186490 bytes normalizado a LF | cotejo de los dos sha256
- SEDE docs/plan/BANCO_DEL_PLAN.md                | al abrir 7836c8976c585143 | al cerrar 7836c8976c585143 | QUIETA | 61554 bytes en disco y 61554 bytes normalizado a LF | cotejo de los dos sha256
- SEDE dataset/metadata/master_graph.json         | al abrir 627cc662296f7f00 | al cerrar 627cc662296f7f00 | QUIETA | 8375817 bytes en disco y 8375817 bytes normalizado a LF | cotejo de los dos sha256
- SEDE docs/loop/ACTA_AUDITOR.md                  | al abrir 2094cea854b381fc | al cerrar 2094cea854b381fc | QUIETA | 5174597 bytes en disco y 5174597 bytes normalizado a LF | cotejo de los dos sha256
- SEDE docs/loop/PROMPT_SIGUIENTE.md              | al abrir a5fa555192f4b562 | al cerrar a5fa555192f4b562 | QUIETA | 7918 bytes en disco y 7918 bytes normalizado a LF | cotejo de los dos sha256

- CIFRA sedes cotejadas: 13 | CIFRA que se movieron: 0
- CIFRA sedes que se movieron A PROPOSITO y estaban declaradas: 0 | CIFRA que se movieron SIN AVISO: 0

**Y LO QUE ESTO SIGNIFICA CON UNA BATERIA ENTERA POR MEDIO, QUE NO ES POCO:**
los arneses de la bateria **SI escriben mientras corren**, y aun asi las trece
quedan QUIETAS. No es una afirmacion: **cada uno de los once tramos comprueba en
su PASO 5 que `git diff --numstat` sobre el arbol del dataset da CERO filas al
salir**, y las once comprobaciones salieron limpias.

### 4.2. LA MORATORIA, MEDIDA Y NO ALEGADA

- CIFRA ficheros de scripts que esta vuelta escribio, MEDIDA AHORA: 14 | CIFRA de esos con el prefijo que le toca: 14

- CIFRA MEDIDA AHORA: 14 | CIFRA DEL HUECO QUE EL PROPIO CIERRE ANADE: 2 | CIFRA TOTAL DE LA VUELTA, LAS DOS JUNTAS: 16

**NINGUN ARNES, GUARDA NI LECTOR NUEVO, Y NINGUNO REPARADO.** En particular
**NO se reparo el carril del lanzador de la bateria que dice cual tramo toca**,
que el acta 219 midio mintiendo (caida `5.1`, **linea 77991** de
`docs/loop/ACTA_AUDITOR.md`, leida hoy del fichero), **ni el rotulo de la salida
compuesta**, ni `scripts/loop/vuelta150_4_tabla_por_fase.py`. **La nomina sigue
CONGELADA EN 135**, y esta vuelta lo mide: el compositor de la bateria dice
`CIFRA entradas de la nomina (leida del modulo): 135`.

### 4.3. LAS RUTAS QUE ESTE REPORTE PROMETE COMO PRUEBA

**UNA RUTA PUBLICADA COMO EVIDENCIA ES UNA CIFRA PUBLICADA** (`EJECUTOR.md` 1,
5 sep 2026), y una que apunte a un fichero inexistente o de cero bytes es caida
de cifra. Las 29 que este cuerpo nombra se comprobaron ANTES de
escribirlo:

- **CIFRA rutas comprobadas: 29 | CIFRA que no existen: 0 | CIFRA que
  miden cero bytes: 0**

## 5. LAS PARADAS

**HAY PARADA, Y SON DOS, LAS DOS DE LA TAREA 2 Y NINGUNA LA ARREGLO YO.** El
encargo `2.e` lo dice con estas palabras: *si un tramo sale en rojo, no lo
arregles: paralo y traelo*. **Los once tramos salen en `ROJO POR FALLO`,
exitcode 1.**

### PARADA 1. SIETE ARNESES QUE NO MUERDEN, Y ESA ES LA ESPECIE QUE EL ENCARGO NOMBRA

**LA CIFRA, SUMADA SOBRE LOS ONCE TRAMOS Y LEIDA DE SUS PROPIAS SALIDAS:**
CIFRA arneses que NO MORDIERON en esta corrida: 7. **Los siete, uno a uno y con su tramo:**

- `vuelta160_tarea6b_mutacion_puerta.py`
- `vuelta165_tarea6_mutacion_op_l_01.py`
- `vuelta166_tarea2_mutacion_correccion.py`
- `vuelta168_tarea1_mutacion_nota.py`
- `vuelta168_tarea2_mutacion_reconstructor.py`
- `vuelta171_mutacion_busqueda_acta.py`
- `vuelta185_tarea1c_mutacion_bateria_continuada.py`

**LO QUE DECIDE SI ESTO ES NUEVO O YA VENIA, MEDIDO CONTRA LA VERSION
COMMITEADA EN EL HEAD DE APERTURA Y NO CONTRA MI RECUERDO:** CIFRA tramos cuya lista de los que no mordieron es IDENTICA a la de la corrida anterior: 11 de 11

**POR QUE ES DEL FUNDADOR Y NO MIA:** *un mutante que no muere es una guarda que
no muerde*, y esa es la especie del 7 sep 2026. **No la reparo** porque la
moratoria `AUDITOR.md` 6.3 lo prohibe y porque el encargo me manda traerla, no
arreglarla.

### PARADA 2. DOS ARNESES QUE EL CENSO VE Y LA NOMINA CONGELADA NO TIENE, Y SON DOS REGLAS VIGENTES CHOCANDO

**LOS DOS, POR SU NOMBRE:**

- `vuelta197_tarea2_mutacion_orden_del_turno.py`
- `vuelta199_tarea1_mutacion_guardas_revividas.py`

- CIFRA arneses fuera de la nomina, distintos: 2

**LAS DOS REGLAS, LAS DOS VIGENTES Y LAS DOS ESCRITAS.** La del propio fichero
de la bateria dice, desde la vuelta 148, que **un arnes entra en la nomina**, y
el acta 176 punto 7.2 acepto que entre en su misma vuelta. La moratoria
`AUDITOR.md` 6.3, del 7 sep 2026, dice que **la nomina queda CONGELADA EN 135:
ni crece ni se poda**, y que **la poda se decide en la auditoria integral y no
antes**. **Los dos arneses nacieron en las vueltas 197 y 199**, o sea entre una
regla y la otra. **Mientras las dos esten puestas, esta bateria no puede salir
en verde**, y eso lo decide el fundador, no yo.

**Y LO DIGO CONTRA MI PROPIO INTERES:** esta es la razon por la que la bateria
de la 215 tambien salio en rojo por los once tramos, y **el acta 219 la da por
corrida** (adjudicacion sobre la 215 aparte, su seccion 1 la cita como corrida
con su commit `abe21a67`). **Yo la declaro corrida por el mismo criterio que
ella**, y marco como discutible que ese criterio sea el bueno.

## 6. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**SEIS, TRES POR TAREA, Y CADA UNO VIVE ENTERO EN SU SECCION DEL ANEXO CON SU
MOTIVO.** Aqui van nombrados para que se encuentren de un vistazo:

| # | tarea | lo que decidi |
|---|---|---|
| **D.1** | TAREA 1 | que la cifra sin la adjudicacion se mide re-corriendo el lector de la 219, y no re-sondando las diecisiete desde el grafo |
| **D.2** | TAREA 1 | que la subida de `05 SANEO` idx 1 se aplica en mi aritmetica y en ningun fichero del plan |
| **D.3** | TAREA 1 | que el movimiento de la salida sellada de la 219 al re-correr su lector no es caida de nadie |
| **D.4** | TAREA 2 | que corri los once tramos en vez de pararme en el primero que salio en rojo |
| **D.5** | TAREA 2 | que los siete que no mordieron suben como PARADA y no como caida mia, y que aun asi declaro la bateria corrida |
| **D.6** | TAREA 2 | que la salida unica se deja con el nombre y el rotulo que el lanzador le pone |

## 7. LAS PREGUNTAS Y LOS PENDIENTES DE DOCTRINA

1. **PENDIENTE DE DOCTRINA: QUE SIGNIFICA QUE UNA BATERIA ESTE CORRIDA CUANDO
   SUS ARNESES NO MUERDEN.** `AUDITOR.md` 6.1 dice que **la bateria se declara
   corrida cuando los once tramos tienen salida sellada DEL MISMO CALIBRE**, y
   eso se cumple y esta medido. **No dice nada de su veredicto.** Con siete
   arneses que no muerden, *corrida* y *sana* dejan de ser lo mismo, y **la
   letra actual solo mide la primera**. No invento la regla que falta: la traigo.
2. **PREGUNTA: SI LAS DOS REGLAS DE LA NOMINA VAN A SEGUIR CHOCANDO HASTA LA
   AUDITORIA INTEGRAL, LA BATERIA NO PUEDE SALIR EN VERDE EN NINGUNA VUELTA.**
   Lo digo con su cifra: **2 arneses fuera**, y la moratoria dice que la poda se
   decide en la integral. **Es del fundador y no la resuelvo.**
3. **PREGUNTA: SI UNA SALIDA SELLADA QUE NO REPRODUCE BYTE A BYTE ES DE SUYO UNA
   CAIDA DE DATO.** Mi guarda midio que `docs/loop/SALIDA_V219_T2_LECTURAS.txt`
   se mueve al re-correr su lector, en UNA linea, la del conteo de lineas del
   acta. **Mi lectura es que no es caida de nadie y que es diferencia de fecha de
   corte**, y va marcada como discutible `D.3`. **Si la casa quiere otra cosa, la
   escribe el fundador.**

## 8. MIS CAIDAS PROPIAS, CADA UNA CON SU NOMBRE Y CONTADA UNA SOLA VEZ

**DOS, LAS DOS CAZADAS POR MIS PROPIAS GUARDAS EN ROJO, Y NINGUNA LLEGO A SER
CIFRA PUBLICADA.** El texto viejo queda escrito en el codigo sin borrar en las
dos, porque una correccion que tapa lo que corrige no se puede auditar.

**C.1. MI GUARDA DE LOS NUEVE FICHEROS CONTABA CUALQUIER MOVIMIENTO COMO ROJO A
SECAS, Y ME LO CANTO.** Al re-correr `scripts/loop/_v219_t2_lecturas.py`, su
propia salida sellada se movio, y la corrida salio en **ROJO con 1 comprobacion
fallando**. La causa esta medida y no supuesta: ese lector imprime **el numero de
lineas que el acta tiene hoy**, y el acta crecio con el acta 219 entera entre la
corrida del auditor y la mia. **La regla nueva exige MAS y no menos**: sigue
siendo rojo que se mueva cualquier fichero que no sea la salida propia del
lector, y de la salida propia se exige ademas que la diferencia sea de UNA sola
linea y que sea la del conteo del acta. **Y la regla nueva se probo por mutacion
antes de publicarla**, en cuatro casos, con su salida en
``docs/loop/SALIDA_V220_T1_MUTACION.txt``, **2326 bytes en disco y 2326 normalizado a LF**.

**C.2. EL PATRON QUE LEE LA CUENTA DE ENTRADAS DEL COMPOSITOR PEDIA UN SOLO
ESPACIO, Y EL COMPOSITOR ALINEA ESA COLUMNA A LA DERECHA.** El tramo 11 tiene
**5 entradas** y no 13, asi que lleva dos espacios y no casaba. La cifra que
salio de mi propia guarda fue **10 tramos de 11 y 130 entradas de 135**, en
ROJO, y **no llego a ningun reporte**. Corregido a `\s+`, la cifra es **11 de 11
y 135 de 135**.

**CIFRA caidas propias de esta vuelta: 2 | CIFRA de ellas que llegaron a ser
cifra publicada: 0 | CIFRA de ellas cazadas por mis propias guardas: 2.**

## LO QUE PROPONGO PARA LA VUELTA SIGUIENTE

**LA PARADA FELIZ NO SE PROPONE, Y LA CONDICION NO LA PUSE YO.** Pide **las
diecisiete en CUBRE**, y **con la adjudicacion `4.5` del acta 219 aplicada hay
QUINCE**:

```
CIFRA clausulas en CUBRE, MEDIDA HOY POR MI LECTOR SIN LA ADJUDICACION: 14 de 17
CIFRA clausulas en CUBRE, CON LA ADJUDICACION 4.5 APLICADA: 15 de 17
CIFRA clausulas en A MEDIAS, CON LA ADJUDICACION 4.5 APLICADA: 2 de 17
CIFRA en CUBRE con la adjudicacion aplicada: 15 | CIFRA que la condicion exige: 17
LA CONDICION SE CUMPLE: NO
```

**LAS DOS QUE FALTAN, CON SU FILA, SU INDICE Y SU CIFRA:**

```
03 FUSIONES    idx 0 | A MEDIAS  | 71 actos sin fundir por la lectura ancha, SEIS fusiones de 19 nodos por la estrecha
07 ADUANA      idx 0 | A MEDIAS  | el quinto control sin correr, mas la celda del punto 2
```

**LO QUE PROPONGO, CON SU CIFRA DELANTE:**

1. **QUE LAS DOS PARADAS DE LA SECCION 5 SE ADJUDIQUEN ANTES QUE NADA**, porque
   de ellas cuelga si esta bateria cuenta como corrida sana o solo como corrida.
   **7 arneses que no muerden** y **2 fuera de la nomina congelada**.
2. **QUE LA COLISION DE LAS DOS REGLAS DE LA NOMINA SE RESUELVA O SE DECLARE
   HASTA LA INTEGRAL**, porque mientras siga puesta **ninguna bateria puede salir
   en verde**, y una guarda que no puede aprobar nunca es una guarda que se acaba
   saltando.
3. **QUE LA VUELTA SIGUIENTE VUELVA AL PLAN Y NO FABRIQUE NADA.** La moratoria
   aguanta y esta vuelta lo vuelve a medir: **CIFRA ficheros de scripts que esta vuelta escribio, MEDIDA AHORA: 14 | CIFRA de esos con el prefijo que le toca: 14**.
4. **QUE LAS DOS CLAUSULAS QUE QUEDAN SUBAN NOMBRADAS** a la lista de la seccion
   6 del acta, con su cifra, como subieron las de la 219.
5. **QUE LA 225 SEA LA SIGUIENTE VUELTA DE BATERIA**, que es lo que la cadencia
   de cinco de `AUDITOR.md` 6.1 dice y no una preferencia mia: esta fue la 220.

**Y EL MERGE NO SE PIDE: EL BUCLE NO FUNDE RAMAS.**
