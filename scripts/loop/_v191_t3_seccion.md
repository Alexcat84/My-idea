### TAREA 3. LAS DOS CONVENCIONES DE `lineas`. CERRADA EN VERDE, MIDIENDO PRIMERO.

**LA MEDICION VA PRIMERO Y EL ARREGLO DESPUES**, que es lo que el encargo pide y
la misma disciplina que la `P.2` del acta 190. El instrumento nuevo y estable es
`scripts/loop/dos_convenciones_de_lineas.py`, sin numero de vuelta porque lo va a
llamar cualquiera.

**LA VARA, ESCRITA ANTES DE CONTAR NADA.** `len(texto.split(NL))` cuenta TROZOS y
deja un trozo final vacio que **no es una linea**: da uno de mas y **no calza con
`wc -l`**. `texto.count(NL)` cuenta SALTOS y **si calza**. `len(splitlines())`
calza cuando el texto termina en salto. **ROJO es una cosa sola y comprobable:
contar por SPLIT y por ninguna de las que calzan.**

**(a) LA MEDICION. LAS DOS CIFRAS SALEN DE FICHEROS SELLADOS Y NINGUNA SE TECLEA:**
`docs/loop/SALIDA_V191_T3_CENSO_ANTES.txt` y
`docs/loop/SALIDA_V191_T3_CENSO_DESPUES.txt`. **El de ANTES no se puede pedir al
arbol una vez arreglado**, asi que `scripts/loop/vuelta191_tarea3_censo.py` saca
los `scripts/loop/*.py` de `HEAD` con `git show` a un directorio temporal y corre
sobre ellos **el detector de HOY**: dos estados del sujeto, **una sola vara**.

| | ANTES (1325 ficheros de `HEAD`) | DESPUES (1329 del arbol) |
|---|---:|---:|
| **ROJO**, cuentan SOLO por la que no calza | **12** | **0** |
| VERDE, publican la pareja | 38 | 54 |
| VERDE, solo por una que calza | 141 | 141 |
| sitios `split` | 68 | 85 |
| sitios `count` | 266 | 292 |
| sitios `splitlines` | 34 | 37 |
| sitios `split` ya corregidos con `- 1` | 1 | 6 |

**LOS DOCE EN ROJO, NOMBRADOS**, del bloque `B` del censo de ANTES:
`_v145_cuerpo_reporte.py`, `_v63_construir_fundidor.py` (2 sitios),
`vuelta162_tarea6_escribir_reporte.py`, `vuelta164_tarea7_escribir_reporte.py`,
`vuelta165_tarea7_escribir_reporte.py`, `vuelta166_tarea3b_motivo.py`,
`vuelta166_tarea4b_correccion_declarada.py`, `vuelta166_tarea5b_frontera_ld07.py`,
`vuelta168_tarea1_adosar_nota_r36.py` (2), `vuelta182_tarea1b_remedio_e1.py` (2),
`vuelta47_marcador_indice.py` y `vuelta65_caso_positivo_generador.py`.
**Ninguno es un instrumento de nombre estable de la cadena viva**: `cerrar_reporte.py`,
`archivar_reporte.py` y `anexar_tarea_al_reporte.py` ya contaban por la que calza,
medido uno a uno.

**Y AQUI VA UNA CORRECCION DECLARADA SIN BORRAR LO QUE CORRIGE.** La PRIMERA
version del detector saco **13** en rojo, no 12. Al mirarlos uno a uno, el
decimotercero era un **falso positivo**:
`vuelta183_tarea1b_mutacion_atribucion.py` escribe `len(mutado.split(NL)) - 1`,
que es **exactamente** `count(NL)`. Y no era inocuo: **ese fichero esta en la
nomina de la bateria** (comprobado contra `verificar_mutaciones_viejas.VIEJAS`,
127 entradas), o sea que "arreglarlo" habria movido una salida sellada que la
bateria de la 194 compara byte a byte. **El detector aprendio la cuarta
categoria**, `split_corregido`, que cuenta como que CALZA, y un sitio corregido
**no se cuenta ademas como sitio SPLIT**: acusar al que ya se corrigio es la misma
especie de cifra falsa que este detector caza.

**(b) EL ARREGLO.** `scripts/loop/vuelta191_tarea3_arreglar_lineas.py`, salida
`docs/loop/SALIDA_V191_T3_ARREGLO.txt`. **La lista no la escribi yo: sale del
censo**, y el instrumento CAE EN ROJO si su lista no calza con la del censo. **12
ficheros tocados, 15 sitios reemplazados**, cada uno con su `(viejo, nuevo)`
literal y **exigiendo que el viejo aparezca EXACTAMENTE UNA VEZ**: un reemplazo
que no sabe donde cae no se hace. Los 15 quedan publicando **la pareja, con
`wc -l` nombrado dentro de la propia frase**. Antes de tocar nada comprueba la
nomina de la bateria: **0 de los 12 estan en ella**. Y **los 12 siguen
compilando**, comprobado en memoria.

**NO SE TOCA NINGUN NUMERO YA PUBLICADO EN UN REPORTE CERRADO.** Lo que cambia es
lo que esos instrumentos IMPRIMIRIAN si se volvieran a correr. **El "2231 lineas"
del reporte de la 190 se queda donde esta**, y esta es la explicacion al lado:
`docs/plan/LECTURAS_DIRIGIDAS.md` da **2230 por `count(NL)`** y **2231 por
`len(split(NL))`**, y **`wc -l` corrido hoy dice `2230`**. La cifra no era
inventada: la imprimia su instrumento.

**DOS CORRECCIONES MAS DEL PROPIO ARREGLO, DECLARADAS IGUAL.** (i) Su
comprobacion de compilado usaba `py_compile` con `cfile=os.devnull`, y en Windows
`nul` no es un fichero regular: **los 12 salieron NO COMPILA y ninguno estaba
roto**. Se compila en memoria. (ii) Re corrido, el instrumento **se acusaba a si
mismo**: despues de arreglar los doce el censo ya no los saca y la lista dejaba de
calzar. **Un arreglo que se declara roto por haber funcionado no sirve de
guarda**: ahora un fichero nombrado que YA lleva la frase de la pareja sale
`YA ARREGLADO`. **Re corrido hoy: 0 tocados, 0 sitios, VEREDICTO VERDE.**

**(c) EL CASO POSITIVO POR MUTACION: VERDE, 0 casos que caen y 0 mutaciones que no
cayeron**, en
`docs/loop/SALIDA_V191_T3_MUTACION_LINEAS.txt`
(disco 5836 bytes | LF 5836 bytes). **Ninguna
variable de veredicto es una constante literal**: todas salen de correr la guarda
sobre un texto fabricado. Los seis bloques:

- **el fuente que publica SOLO por SPLIT sale ROJO**, y pedirle VERDE **CAE**. Es
  literalmente lo que el encargo manda cazar.
- **`NO APLICA` no es VERDE**: un fichero que no cuenta lineas no ha aprobado
  nada, y confundirlos dejaria pasar cualquier cosa.
- **la SPLIT corregida con `- 1` no se acusa**, con sus 0 sitios SPLIT y 1
  corregido.
- **la pareja sobre textos de largo conocido**: `(3, 4)` si el texto termina en
  salto y `(2, 3)` si no. Si las dos convenciones dieran lo mismo no habria nada
  que arreglar, y la mutacion lo comprueba.
- **el censo sobre un directorio fabricado**: 0 rojos, se mete el defecto, **1
  rojo y lo nombra**.
- **el ejemplar del acta 190 cotejado contra `wc -l` DE VERDAD**, corrido como
  proceso: `count` da 2230 y `wc -l` da 2230, **CALZA**; `split` da 2231, **no
  calza**.

**Y LA GUARDA SE APLICA A QUIEN LA ESCRIBIO**, que es el bloque `E` del arnes:
los **ocho** instrumentos de esta vuelta salen **0 en ROJO**. Una guarda que no se
aplica a su autor no es una guarda.
