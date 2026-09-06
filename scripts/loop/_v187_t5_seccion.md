### TAREA 5. LA NOMINA, LA DECLARACION DEL 184, LA CIFRA DEL H.5 Y EL CIERRE. **CERRADA, CON UNA PARADA DECLARADA.**

#### 5.a LA NOMINA: DE 115 A 121, Y `arneses_que_faltan()` DEVUELVE **0**

**ERA UNA CAIDA MEDIDA CON DOS VUELTAS DE ANTELACION, Y POR SEGUNDA VEZ
SEGUIDA.** El bloque H.3 del sello de apertura, corrido **antes de tocar nada**,
midio `arneses_que_faltan()` devolviendo **`ultima vuelta 185, faltan 4`**.

| | apertura | cierre |
|---|---:|---:|
| censo de arneses del directorio | **181** | **181** |
| tamano de la nomina | **115** | **121** |
| `arneses_que_faltan()` | **4** | **0** |
| `nomina_invisible_al_censo()` | **0** | **0** |
| `guarda_del_sujeto_congelado()` | **0** sin congelar | **0** sin congelar |

**LOS SEIS QUE ENTRAN**, los cuatro de la 186 mas **los dos que nacen hoy**, y
los seis comprobados uno a uno dentro de la nomina (**6 de 6**):
`vuelta186_tarea2a_mutacion_pieza4.py`,
`vuelta186_tarea2b_mutacion_pieza2_cercas.py`,
`vuelta186_tarea2c_mutacion_cierre_tardio.py`,
`vuelta186_tarea2d_mutacion_seccion4.py`,
`vuelta187_tarea4_mutacion_dos_convenciones.py` y
`vuelta187_tarea5b_mutacion_seccion4_tardio.py`.

**NO SE PODA NADA.** La opcion `c` de la parada del 5 sep sigue RECHAZADA por el
fundador y aqui se hace lo contrario, que es completarla. **Y el instrumento de
esta tarea no entra en la nomina, y se mide en vez de decirse:**
`vuelta187_tarea5a_nomina.py` **no esta en el censo de arneses** y **no esta en la
nomina**.

**LA DOBLE CORRIDA EN PROCESOS APARTE: LOS SEIS SON DETERMINISTAS.** Los seis dan
**el mismo `sha256` en las dos corridas**. Ninguna salida cambia sola.

| arnes | exitcode | `sha256` LF, las dos corridas |
|---|:-:|---|
| `vuelta186_tarea2a_mutacion_pieza4.py` | 0 | `9bb37980006e99d3` en las dos |
| `vuelta186_tarea2b_mutacion_pieza2_cercas.py` | 0 | `cf0e9dfc2a8bf63d` en las dos |
| **`vuelta186_tarea2c_mutacion_cierre_tardio.py`** | **1** | `5541805c720b9770` en las dos |
| `vuelta186_tarea2d_mutacion_seccion4.py` | 0 | `443a4f12e3b2ce76` en las dos |
| `vuelta187_tarea4_mutacion_dos_convenciones.py` | 0 | `969c147da84ac882` en las dos |
| `vuelta187_tarea5b_mutacion_seccion4_tardio.py` | 0 | `a0e622551af7ca0a` en las dos |

> ## PARADA. UN ARNES YA SELLADO CAE EN ROJO, Y NO LO ARREGLO
>
> **`scripts/loop/vuelta186_tarea2c_mutacion_cierre_tardio.py` sale en ROJO**,
> con **`CIFRA casos: 18 | pasan: 16`** y **`CIFRA fallos: 2`**. **La corrida
> entera vive en
> `docs/loop/SALIDA_V187_T5B_ARNES_SELLADO_186_2C_EN_ROJO.txt`.** Lo que cae es
> su **CASO E**, y lo pego literal:
>
> ```
>       CIFRA apariciones de `not tardio` en el instrumento: 2
>       ESPERADO exactamente 1 -> NO CALZA
>       MUTACION del esperado (exigir 2): PASA
> ```
>
> **LA CAUSA ES EXACTA Y ES MIA, Y LA DIGO PRIMERO.** Ese caso cuenta las
> apariciones de `not tardio` en `cerrar_reporte.py` y **exige EXACTAMENTE 1**,
> porque cuando se escribio **la unica guarda eximida en el carril tardio era la
> de las cifras sin pareja**. La **TAREA 5.b de esta vuelta anade la segunda
> exencion**, la de la `2.d`, que es **literalmente lo que el encargo manda**, y
> con ella la cuenta pasa a **2**.
>
> **NO LO ARREGLO, Y POR LA LETRA:** *"Si cualquier arnes YA SELLADO cae en rojo,
> te detienes ahi, lo traes con su salida entera, sin re-correrlo y sin
> arreglarlo"*. **Cambiar ese `1` por un `2` seria aflojar la guarda que existe
> para impedir que el carril tardio se ensanche solo**, y quien decide si la
> exencion ordenada por el encargo cabe dentro de esa cuenta **no soy yo**.
>
> **LO QUE SI HICE, Y LO DIGO PARA QUE SE PUEDA AUDITAR:** la primera corrida
> clobbero su salida sellada y **la restaure con `git checkout`**; despues, la
> doble corrida de la 5.a la volvio a correr **dos veces** y su salida quedo
> resellada en rojo con `git diff --numstat` de **7 lineas**. **Es
> DETERMINISTA**: el mismo `sha256` en las dos corridas.
>
> **Y LO QUE NO SOSTENGO:** no afirmo que el arnes este mal. Afirmo que **su
> esperado y el encargo de esta vuelta dicen cosas distintas**, y eso es una
> contradiccion entre dos reglas vigentes, que es exactamente el caso en que
> `EJECUTOR.md` 5 manda parar y traerlo.

**Y LAS SALIDAS SELLADAS DE LA 186 SE MOVIERON, CON SU CAUSA MEDIDA.** Esta
vuelta toco `cerrar_reporte.py`, que es el sujeto de los cuatro arneses de la
186, y sus salidas publican **numeros de linea** de ese fichero. `git diff
--numstat` de cada una: `2A` **4 lineas** (solo numeros de linea: la 700 pasa a
la 770 y la 1223 a la 1446, con el veredicto intacto), `2B` **0**, `2C` **7**
(la parada de arriba), `2D` **0**.

#### 5.b LA DECLARACION DEL DEFECTO DEL REPORTE DE LA 184. ES LA `P.2`

**LA PREMISA DE LA PREGUNTA ERA FALSA Y ESTA MEDIDO.**
`docs/loop/SALIDA_V184_APERTURA.txt` **existe** y mide **34194 bytes en disco y 34194 bytes normalizados a LF**, y publica **`CIFRA lineas de status: 2`** y
**`numstat AL ENTRAR: 0`**. **El rojo no es por falta de apertura.** Corrido hoy
sobre los dos ficheros reales:

    seccion4_que_no_calza(REPORTE_V184.md, SALIDA_V184_APERTURA.txt)
    ->  CIFRA motivos en rojo: 1
        "LA SECCION 4 DEL REPORTE NO AFIRMA NADA sobre 'CIFRA lineas de
         status'. La apertura sellada docs/loop/SALIDA_V184_APERTURA.txt
         dice 2, y una cifra ausente y una cifra que calza NO son lo mismo"

**LO QUE SE ESCRIBIO:** `declaracion_de_seccion4()` en `cerrar_reporte.py`,
**PURA** y **hermana exacta** de `declaracion_de_cifras_sin_pareja()`. Misma
puerta, misma forma, **y por eso no se escribe una tercera manera de declarar un
defecto**. En el carril tardio `main()` la computa **sobre el texto ya armado** y
la anexa; en el bloque D.1 la exencion **se coteja POR CONTENCION**: si la marca
no esta o algun motivo no esta declarado, **vuelve a ser rojo**. **Una exencion
sin su declaracion seria una exencion muda, y eso es lo que el banco 9 prohibe.**

**`docs/loop/reportes/REPORTE_V184.md` NO SE REABRE Y NO SE REESCRIBE SU SECCION
4.** Lo que se le anade es la declaracion. **Reescribir su seccion 4 seria
escribir en pasado lo que no paso.**

**EL ARNES**, `scripts/loop/vuelta187_tarea5b_mutacion_seccion4_tardio.py`, **7
casos, `CIFRA fallos: 0`, `VEREDICTO: VERDE`**:

| caso | que exige | con el esperado mutado |
|---|---|---|
| **A** | en el carril **NORMAL** la seccion 4 muda **BLOQUEA**, leido de la columna `bloquea` real de `main()` en el fichero fuente | **CAE** |
| **B** | en el **TARDIO** no bloquea y **aparece DECLARADA**, cotejada por contencion | **CAE** (dos mutaciones) |
| **B.1** | la declaracion **no se acusa a si misma**: 1 motivo antes y 1 despues de anexarla | **CAE** |
| **C** | **cero motivos**: la declaracion se escribe igual y **dice cero** | **CAE** |
| **D** | sobre los ficheros **REALES** del 184: **1 motivo**, y la declaracion **lo nombra** (1 de 1) | **CAE** (dos mutaciones) |
| **E** | la guarda de las dos convenciones de la TAREA 4 **bloquea en los dos carriles** | **CAE** |
| **F** | la exencion **no es gratis**: sin declaracion, vuelve a ser rojo | **CAE** |

**SU PRIMERA CORRIDA SALIO EN ROJO Y SE PEGA ENTERA**, que es lo que la
adjudicacion `5.2` del acta 186 manda para un arnes que nace en la vuelta:
`docs/loop/SALIDA_V187_T5B_MUTACION_SECCION4_TARDIO_EN_ROJO.txt`, **`CIFRA
fallos: 1`**. El motivo esta dentro del propio fichero: **el arnes fabricaba su
seccion 4 con la frase `CIFRA lineas de status` cuando la guarda busca el
MARCADOR literal `git status --porcelain`**. *Un arnes que fabrica su sujeto con
otras palabras que las que la guarda busca no prueba la guarda: prueba la
parafrasis.* Ahora los dos marcadores **se importan de la guarda** y no se
teclean.

#### 5.c LA CIFRA INUTIL DEL BLOQUE H.5, REPARADA, CON SU ANTES Y SU DESPUES

El bloque de apertura de la 186 conto los puestos de las ciegas con el patron en
mayusculas cuando las ciegas los escriben como `puesto_intra`. El bloque H.5 de
esta vuelta cuenta con **LOS DOS** y publica **LAS DOS CIFRAS**:

| fichero | cifra VIEJA (patron de la 186) | cifra NUEVA (`puesto_intra`) |
|---|---:|---:|
| `docs/loop/_auditor_v188_ciega_blind.txt` | **0** | **30** |
| `docs/loop/_auditor_v188_ciega_reveal.txt` | **0** | **30** |
| `docs/loop/_auditor_v187_ciega_blind.txt` | **0** | **30** |
| `docs/loop/_auditor_v188_mis_clases.txt` | **0** | **0** |

**TRES DE LOS CUATRO DEJAN DE SER CERO. EL CUARTO SIGUE EN CERO, Y ES CORRECTO,
Y SE DICE EN VEZ DE DISIMULARLO:** `_auditor_v188_mis_clases.txt` **no escribe
`puesto_intra` en ninguna linea**; escribe una TABLA con cabecera `puesto | mi
clase | dudoso | mi razon en una linea`. **Su cero no es una cifra inutil: es la
medicion correcta de un fichero con otro formato.**

#### 5.d EL CIERRE

El esqueleto se tallo con sus **cinco filas vacias** y **cada tarea anexo la suya
al cerrarse**. La cabecera se talla con
`python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 187` y su
salida vive en `docs/loop/SALIDA_V187_TALLADOR_CABECERA.txt`. **Cero celdas
tecleadas.**
