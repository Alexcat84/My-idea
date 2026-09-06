### TAREA 4. LA ESCALADA: LA PAREJA DE CONVENCIONES DEJA DE BASTAR CON EXISTIR. **CERRADA.**

**EL HUECO, MEDIDO Y NO SOSPECHADO.** `cerrar_reporte.py` publicaba en su bloque
D la linea `toda cifra de bytes y todo sha con su pareja SI`, y **las cuatro
cifras falsas de la `C.1` pasaron por delante de esa linea sin encender nada**.
La causa es exacta: `cifras_sin_pareja()` comprueba que la pareja **EXISTA**, no
que sea **CIERTA**. **Medido en el arnes de esta tarea: de las 7 lineas que la
guarda nueva acusa sobre el texto real de `bb3aaad3`, la guarda vieja acusaba
0.**

**LO QUE SE ESCRIBIO, Y DONDE.**

| pieza | sede | que es |
|---|---|---|
| `dos_convenciones(datos)` | `scripts/loop/vuelta186_rutas_del_reporte.py` | **PURA.** Se SEPARO de dentro del bucle de su `main()` para que la guarda nueva pudiera llamarla. **Una sede, dos llamadores, y NO un tercero.** |
| `medir_en_disco(raiz, ruta)` | la misma | **EL UNICO SITIO QUE TOCA DISCO** para esto. Devuelve `None` y no cero cuando el fichero no existe: cero seria una cifra y la ausencia no lo es. |
| `parejas_publicadas(texto)` | `scripts/loop/cerrar_reporte.py` | **PURA.** Toda pareja publicada contra una ruta, en las **tres formas** que esta casa usa de verdad. |
| `convenciones_que_no_calzan(texto, mediciones)` | la misma | **PURA.** Recibe un MAPA de mediciones, no el disco. |
| `mediciones_de_las_rutas(texto, raiz)` | la misma | el lector unico, que llena ese mapa llamando a la sede de arriba |

**`main()` la llama SIN BANDERA** (lo que se computa no se teclea) y la cablea en
la misma lista del bloque D donde este fichero juzga, con `bloquea=True`, **que
bloquea en LOS DOS CARRILES**: el carril tardio exime una cifra sin pareja y una
seccion 4 muda, que son defectos de un reporte viejo que se declaran; **una cifra
FALSA no es un defecto que se declare, es una cifra falsa**.

**LAS TRES FORMAS, LEIDAS DE REPORTES REALES Y NO INVENTADAS:** (a) `` `<ruta>` ...
N bytes en disco y M bytes normalizados a LF ``; (b) `` `<ruta>` ... disco N bytes
| LF M bytes ``; y (c) **una tabla cuya CABECERA declara que las dos convenciones
son IGUALES y cuyas filas publican UNA sola cifra por ruta**. La tercera hacia
falta: **la cuarta cifra de la `C.1`, el 49804, vive exactamente ahi.**

**Y UNA REGLA QUE LA PROPIA GUARDA SE DESTAPO AL CORRERLA.** En su primera
version acusaba tambien la linea 191 de `bb3aaad3`, donde el reporte dice
*"`docs/PENDIENTES.md` pasa de 894124 bytes en disco a 909780 bytes, la entrada
mide 15655 bytes en disco y 15655 normalizados a LF"*: **la pareja es de LA
ENTRADA escrita, no del fichero**, y atribuirsela habria sido un rojo inventado.
**Si entre la ruta y la pareja hay OTRA cifra de bytes, el sujeto es ambiguo y
esta guarda no atribuye nada.** Es la regla mas estrecha que sigue cazando los
cuatro casos de la `C.1`, donde entre la ruta y su pareja no hay mas que una
coma.

**EL ARNES**, `scripts/loop/vuelta187_tarea4_mutacion_dos_convenciones.py`,
**7 casos, `CIFRA fallos: 0`, `VEREDICTO: VERDE`**, todos con su esperado mutado
cayendo:

| caso | que exige | con el esperado mutado |
|---|---|---|
| **1** | las dos convenciones calzando: **VERDE** | **CAE** |
| **2** | la de **LF** mutada: ROJO, **nombrando LF**, la ruta, la publicada y la medida | **CAE** |
| **3** | la de **DISCO** mutada: ROJO, **nombrando DISCO** | **CAE** |
| **4** | una ruta con **CRLF real**, donde las dos son legitimamente distintas: **VERDE**. Es el caso que impide que la guarda exija que sean iguales | **CAE** |
| **5** | una cifra **sin pareja**: sigue siendo el rojo de `cifras_sin_pareja()`, con su texto de hoy, y **la nueva no la duplica** | **CAE** |
| **5.1** | una **ruta que no existe**: sigue siendo el rojo que ya es, y esta guarda **no lo duplica** | **CAE** |
| **6** | **EL QUE DECIDE**, sobre el texto real de `git show bb3aaad3:docs/loop/REPORTE.md` | **CAE** |

**EL CASO 6, ENTERO.** Sobre ese texto, que mide **46086 bytes en disco y 46086 bytes normalizados a LF** porque el blob de git no lleva CRLF, y **708 lineas**, la
guarda halla **33 parejas publicadas** y acusa **11**, sobre **5 rutas
distintas**:

| ruta | convencion | publicada | medida |
|---|:-:|---:|---:|
| `docs/loop/SALIDA_V186_COTEJO_DE_CLONES.txt` | **LF** | 49804 | **49036** |
| `docs/loop/SALIDA_V186_T2C_CERRAR_REPORTE_184.txt` | **LF** | 6128 | **6030** |
| `docs/loop/SALIDA_V186_T2C_ARCHIVAR_184_SIN_FORZAR.txt` | **LF** | 790 | **780** |
| `docs/loop/SALIDA_V186_T2C_ARCHIVAR_184.txt` | **LF** | 965 | **948** |
| `docs/loop/SALIDA_V186_T2C_MUTACION_CIERRE_TARDIO.txt` | DISCO y LF | 5040 | **5043** |

**`DE LAS CUATRO DE LA C.1, FALTAN POR CAZAR: (ninguna)`**, y **`LA CONVENCION QUE
FALLA EN LAS CUATRO ES LF, Y NO DISCO: SI`**.

**LA QUINTA NO ES UN ROJO INVENTADO, Y ESO NO SE SUPONE: SE MIDE.** El primer
criterio de este caso exigia **cero rutas de mas** y salio en **ROJO** en cuanto
otra tarea de esta misma vuelta movio un fichero; **la corrida en rojo entera
vive en `docs/loop/SALIDA_V187_T4_MUTACION_EN_ROJO.txt`** y el motivo esta dentro
del propio arnes. El criterio nuevo va contra `git show`: una ruta de mas es
**legitima** si el fichero **HA CAMBIADO** desde `bb3aaad3`, e **inventada** solo
si sigue byte a byte igual y aun asi se acusa.

    docs/loop/SALIDA_V186_T2C_MUTACION_CIERRE_TARDIO.txt
       -> en bb3aaad3 5040 bytes | hoy 5043 bytes | HA CAMBIADO: SI
    CIFRA rutas de mas que serian ROJO INVENTADO: 0

**Es un arnes que nace en esta vuelta**, asi que su rojo es parte de escribirlo
(adjudicacion `5.2` del acta 186), la corrida en rojo se pega entera y el motivo
queda dentro del fichero. **Esa es la letra, y aqui se cumple.**
