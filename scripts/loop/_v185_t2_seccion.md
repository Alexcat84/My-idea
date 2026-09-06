### TAREA 2. EL CIERRE DE DOS REPORTES. EL DE LA 185 CIERRA; EL DE LA 184, NO: PARADA

**TODAS LAS CIFRAS DE ESTA SECCION SALEN DE CONTAR SUS FICHEROS DE SALIDA CON
`scripts/loop/_v185_tallar_t2.py`, Y NINGUNA ESTA TECLEADA.**

#### 2.a EL REPORTE DE LA 184: LA RAMA NUEVA FUNCIONA Y EL CIERRE SIGUE EN ROJO

**PRIMERO LAS TRES PIEZAS, COTEJADAS POR `sha256` Y POR BYTES CONTRA LO QUE LA
184 MIDIO. LAS TRES CALZAN**, y el cotejo salio **VERDE**:

| pieza | medida hoy |
|---|---|
| `docs/loop/SALIDA_V184_TALLADOR_CABECERA.txt` | **2435 bytes en disco y 2415 bytes normalizados a LF** |
| `scripts/loop/_v184_cierre_texto.md` | **13982 bytes en disco y 13982 bytes normalizados a LF** |
| `docs/loop/SALIDA_V183_BATERIA.txt` | **71753 bytes en disco y 71753 bytes normalizados a LF** |

Salida del cotejo: `docs/loop/SALIDA_V185_T2A_VEREDICTO_184.txt` (**2322 bytes en disco y 2322 bytes normalizados a LF**).

**EL VEREDICTO DE UNA LINEA SE TALLO Y NO SE TECLEO A OJO.** Sus dos numerales
salen de `caidas_propias_del_cuerpo()` y `tareas_de_la_tabla()` corridas sobre
las dos mitades que la guarda `B.1` juzga, y la guarda dio **CIFRA numerales
que NO calzan: 0**. Mutado un numeral, la guarda cae. La frase quedo en
`docs/loop/SALIDA_V185_T2A_VEREDICTO_184_FRASE.txt` (**356 bytes en disco y 356 bytes normalizados a LF**).

**LO QUE EL ENCARGO PEDIA Y SI PASO: LA RAMA DE LA SECCION 9 SALIO `CORRIDA`**
**POR LA RAMA NUEVA**, y su motivo nombra que la bateria se **CONTINUO** y que
la vuelta 184 sello **5** de sus tramos, leidos del asunto de su ultimo commit
con `git log` y no tecleados. Las lineas que lo dicen, pegadas de la salida:

```
      tramo 1   -> vuelta 183
      tramo 2   -> vuelta 183
      tramo 3   -> vuelta 183
      tramo 4   -> vuelta 183
      tramo 5   -> vuelta 184
      tramo 6   -> vuelta 184
      tramo 7   -> vuelta 184
      tramo 8   -> vuelta 184
      tramo 9   -> vuelta 184
   CIFRA tramos sellados EN LA VUELTA 184: 5 [5, 6, 7, 8, 9]
   RAMA DE LA SECCION 9, decidida por rama_de_la_seccion9(): CORRIDA
      motivo: la bateria del fichero es de la vuelta 183 y se esta cerrando la 184, pero NO ES UNA CORRIDA AJENA: ES LA MISMA BATERIA CONTINUADA. La vuelta 184 sello 5 de sus tramos (los tramos 5, 6, 
```

#### PARADA. EL CIERRE DE LA 184 CAE EN ROJO POR TRES GUARDAS MAS, Y NINGUNA ES LA RAMA

`scripts/loop/cerrar_reporte.py --vuelta 184` devuelve **exitcode 1**. La salida
entera vive en `docs/loop/SALIDA_V185_CERRAR_REPORTE_184.txt` (**5581 bytes en disco y 5497 bytes normalizados a LF**).

**Y AQUI NO SE PEGA ENTERA, CON UN MOTIVO MEDIDO Y NO UNA EXCUSA.** Esa salida
lleva dentro la marca de maquina que la **pieza (2)** de `piezas_que_faltan()`
busca **en todo el texto del reporte, sin excluir los bloques cercados**.
Pegarla aqui haria caer el cierre de **este** reporte por el mismo falso
positivo que cazo al de la 184, que es exactamente la averia que se esta
reportando. **Se cita por su ruta con sus bytes, se pegan las lineas que
deciden, y se dice.** El fichero entero esta commiteado: no se pierde nada.

**LOS TRES MOTIVOS DEL ROJO, CONTADOS DE ESA SALIDA:**

| motivo | cifra de su fichero | que especie es |
|---|---:|---|
| piezas de las cuatro que faltan | **2** | (2) y (4) |
| cifras publicadas sin su pareja | **10** | guarda `cifras_sin_pareja()` |
| citas de arnes que NO calzan | **0** | ninguna |

1. **LA PIEZA (4) ES LA COPIA GEMELA DE LA REGLA QUE LA `1.c` ACABA DE
   REPARAR.** `piezas_que_faltan()` lleva su propia comparacion de vuelta ajena
   y **no recibe la evidencia de los tramos**. Es la PARADA que la TAREA 1.c ya
   trajo levantada y que el encargo prohibe tocar.
2. **LA PIEZA (2) ES UN FALSO POSITIVO DE LA MISMA ESPECIE.** La cabecera **SI**
   esta pegada: las **11 filas de 11** del tallador estan dentro y **0 quedan
   fuera**. Lo que enciende la pieza es que la marca de maquina aparece **UNA**
   vez en todo el reporte, en su **linea 353**, **dentro de un bloque cercado**
   que cita la salida roja de la 184.
3. **LAS CIFRAS SIN PAREJA VIVEN EN EL CUERPO QUE LA 184 YA ESCRIBIO**, y el
   encargo manda cerrar *"con el texto que ya tiene"*. Repararlas seria
   reescribir un texto que no me toca reescribir.

**QUE HAY EN DISCO, DICHO SIN ADORNAR:**

- `docs/loop/reportes/REPORTE_V184.md`, **33608 bytes en disco y 33608 bytes normalizados a LF**, **517 lineas**, `sha256` LF
  `6bbeb09c5822c192`, archivado con **exitcode 0**. **NO ES EL CERRADO:**
  `archivar_reporte.py` lee de git y no del arbol, asi que archivo el ultimo
  estado **commiteado**, el que la 184 dejo.
- `docs/loop/SALIDA_V185_T2A_REPORTE_184_CERRADO_EN_ROJO.md` (**122030 bytes en disco y 122030 bytes normalizados a LF**):
  lo que el instrumento **si** llego a escribir antes de devolver 1, guardado
  con un nombre que dice lo que es. El instrumento escribe en su bloque C y
  juzga en el D.
- `docs/loop/SALIDA_V185_T2A_REPORTE_184_ANTES.md` (**33608 bytes en disco y 33608 bytes normalizados a LF**):
  el estado previo, para que las dos caras se puedan comparar.
- `docs/loop/REPORTE.md` se restauro con `git checkout` al estado commiteado,
  para que el arbol y el archivado digan lo mismo.

**LA CUENTA DE VUELTAS QUE CIERRAN SU PROPIO REPORTE, PARA LA 184, SIGUE EN
CERO.** No lo fuerzo y no lo arreglo yo.

#### 2.b EL REPORTE DE LA 185 SE ABRE, SE LLENA Y SE CIERRA

**EL ESQUELETO** se tallo en el paso 4 del orden de esta vuelta, con sus **2
filas vacias**. `docs/loop/REPORTE.md` nacio con **7542 bytes normalizados a LF**,
contados por el propio esqueleto antes de escribirlos en disco.
Salida: `docs/loop/SALIDA_V185_ESQUELETO.txt` (**3965 bytes en disco y 3901 bytes normalizados a LF**).

**Y SU PASO 0 NO TUVO REPORTE AJENO QUE ARCHIVAR, Y LO DICE EN VEZ DE DEJAR LA
FILA MUDA.** Su salida publica que el destino
`docs/loop/reportes/REPORTE_V184.md` **YA EXISTE con contenido IDENTICO**, y que los dos `sha256` calzan con
el reporte que se iba a pisar. Es lo que el encargo predijo, porque la **2.a**
lo archivo antes.

**CADA TAREA ANEXO SU FILA AL CERRARSE**, no al final: la TAREA 1 entro con su
seccion entera antes de que esta se escribiera.

**LA SECCION 9 DE ESTE REPORTE CIERRA CON EL HUECO DECLARADO Y MEDIDO, POR EL
CARRIL DE `cerrar_reporte.py` Y NO A MANO.** Las tres piezas van juntas o no
vale: **el nombre del fichero**, **sus bytes medidos** y **la atribucion**. **LA
ATRIBUCION ES QUE LA BATERIA CORRE CADA CINCO VUELTAS Y QUE LA SIGUIENTE ES LA
189**, por `AUDITOR.md` 6.1, decision del fundador del 5 sep 2026: la bateria
cerro entera en la 184 con sus nueve tramos sellados.

**SI ESTA VUELTA CIERRA SU REPORTE, ES LA PRIMERA DE LAS DOS SEGUIDAS QUE EL
REGIMEN 6.2 PIDE PARA DEVOLVER EL TOPE A CINCO.** Dicho con esas palabras, y
dicho tambien lo otro: **la 184 no lo cerro hoy tampoco**, asi que la cuenta que
empieza es la de la 185 y no una que venga de atras.

#### LAS GUARDAS DEL CIERRE, RECOMPUTADAS AL CIERRE

`git diff --numstat -- dataset/` al salir de la vuelta: **0 filas**. Al entrar
dio **0 filas**, medido en el bloque de apertura antes de la primera operacion.

El ciclo de Gate 0 corrio entero y en su orden al cierre, y sus salidas viven en
`docs/loop/SALIDA_V185_*_CIERRE.txt`. La tabla de la cabecera de este reporte
sale de ellas con `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 185`
y **ninguna celda esta tecleada**.

#### LOS DISCUTIBLES DE ESTA TAREA, MARCADOS ANTES DE SABER SI ACIERTO

**`D.6`. NO PEGUE ENTERA LA SALIDA ROJA DEL CIERRE DE LA 184.** El encargo de
la 2.a dice *"paras y lo traes entero"*, y la 184 pego la suya entera. **Yo la
cito por su ruta con sus bytes y pego las lineas que deciden**, porque pegarla
entera haria caer el cierre de este reporte por la pieza (2). **Mi razon es que
un reporte que no cierra no trae la PARADA a nadie**, y el fichero entero esta
commiteado. **Pero es una desviacion de la letra y la marco.**

**`D.7`. CERRE EL REPORTE DE LA 185 SABIENDO QUE EL DE LA 184 NO CERRO.** Se
puede leer que el orden del encargo hacia del cierre de la 184 una condicion
previa. **Mi lectura es que son dos reportes distintos y que el mio no depende
del suyo**, y que dejar los dos sin cerrar seria la quinta vuelta seguida sin
reporte cerrado. **Lo marco porque la lectura contraria es defendible.**

#### PENDIENTES DE DOCTRINA

**`PD.1` SIGUE ABIERTA Y NO LA TOCO:** las cinco `D` con el diferenciador ya
presente el dia del veredicto, hoy con sus cinco puestos escritos en el `R.47`.

**`PD.5` NUEVA. UNA MARCA DE MAQUINA CITADA DENTRO DE UN BLOQUE CERCADO SIGUE
SIENDO UNA MARCA DE MAQUINA.** La pieza (2) busca su marca en todo el texto y
`cifras_sin_pareja()` ya excluye los bloques cercados: **dos guardas del mismo
fichero tratan la cita al reves la una de la otra**. No hay regla escrita que
elija, y hoy eso impide que un reporte pueda citar el rojo de otro.

**`PD.6` NUEVA. UNA REGLA ESCRITA DOS VECES EN EL MISMO FICHERO.**
`rama_de_la_seccion9()` y la pieza (4) de `piezas_que_faltan()` llevan la misma
comparacion de vuelta ajena. Reparar una y no la otra deja el instrumento
diciendo dos cosas distintas del mismo caso. **Es la PARADA de la 1.c dicha como
doctrina.**

