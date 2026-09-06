### TAREA 4. LA ESCALADA: LA GUARDA QUE VEIA LA MITAD, Y LA SECCION QUE SE DUPLICA. CERRADA EN VERDE

**LA RACHA DE REPORTE SIGUE EN DOS, ASI QUE `AUDITOR.md` 1.2 SIGUE SIENDO
MANDATORIO.** La escalada de la 187 esta descargada; esta es la siguiente, y sale
de una medicion del auditor.

#### 4.a LA COBERTURA DE LA GUARDA DE LAS DOS CONVENCIONES

**EL HUECO, MEDIDO Y REPRODUCIDO POR MI EN LA APERTURA ANTES DE TOCAR NADA:**
corrida sobre el texto real de `git show 9a06b7c8:docs/loop/REPORTE.md`,
`parejas_publicadas()` veia **TRES** parejas
(`docs/PENDIENTES.md`, `docs/plan/08_VERIFICACION.md` y
`docs/loop/SALIDA_V184_APERTURA.txt`). **Ahora ve SEIS**, y las tres nuevas son las
que el acta nombra:

| linea | ruta | pareja | forma que se le escapaba |
|---:|---|---|---|
| 82 | `docs/loop/SALIDA_V187_TALLADOR_CABECERA.txt` | 2444 / 2424 | dice **"2424 normalizado a LF"**, en singular y sin repetir la palabra bytes |
| 368 | `docs/loop/SELLO_APERTURA_AUDITOR_V188.json` | 802 / 802 | separa las dos convenciones **con una coma** y envuelve las cifras en negrita |
| 398 | `docs/loop/_auditor_v188_exclusion.txt` | 1372 / 1372 | la ruta esta **dos lineas mas arriba**, en una fila de tabla |

**LAS TRES FORMAS SON LITERALES DE ESE REPORTE Y NO INVENTADAS**, y las tres van
en el arnes con su mutacion cayendo.

**LA REGLA DE LA AMBIGUEDAD NO SE TOCO, Y ESA ES LA MITAD QUE IMPIDE CAMBIAR UN
HUECO POR OTRO PEOR.** Si entre la ruta y la pareja hay **otra** cifra de bytes, el
sujeto sigue siendo ambiguo y la guarda **no atribuye nada**. Lo mismo para la
ruta de arriba: **solo se acepta la linea anterior mas cercana que nombre
EXACTAMENTE UNA ruta**, y solo si entre ella y la pareja no hay otra cifra de
bytes, contando el resto de aquella linea y todas las de en medio. El caso del
`15655` del reporte de la 186 **sigue saliendo sin atribuir**, y ahora ademas sale
**nombrado**.

**LA COBERTURA, QUE ES LA MITAD QUE IMPORTA, Y AHORA LA PUBLICA LA PROPIA GUARDA.**
Sobre el texto real del reporte de la 187:

- **`CIFRA parejas que VE y atribuye: 6`**
- **`CIFRA lineas fuera de cerca con alguna cifra de bytes, que es el universo
  donde una pareja podria estar: 6`** (lineas 82, 196, 338, 398, 515 y 536)
- **`CIFRA de esas que ademas nombran una ruta en su misma linea: 5`**
- **`CIFRA parejas vistas y NO atribuidas: 2`**, y van **nombradas una a una con su
  motivo**:
  - **linea 515**, `15655 / 15655`: *"AMBIGUA: entre la ruta `docs/PENDIENTES.md` y
    la pareja hay otra cifra de bytes, asi que el sujeto no esta claro y esta
    guarda NO atribuye nada"*.
  - **linea 536**, `46086 / 46086`: *"SIN SUJETO: ni esta linea ni las 4 anteriores
    nombran UNA sola ruta que se le pueda atribuir"*.

**Y EL DENOMINADOR SE MIDIO ANTES DE ELEGIRLO:** no es "rutas con cifra de bytes en
su misma linea", porque **eso dejaria la pareja de la linea 398 fuera de su propio
universo**, que es precisamente la forma que esta vuelta viene a cubrir. El
universo son **las lineas con cifra de bytes**, y la cuenta de las que ademas
llevan ruta al lado se publica a su lado, no en su lugar.

**Y AQUI VA UNA MEDICION QUE CAMBIO EL CASO DECISIVO, Y SE DECLARA EN VEZ DE
DISIMULARSE.** Lo primero que probe fue cotejar las seis contra **el arbol de ese
commit**, que parece lo correcto. **No lo es, y lo prueba una cifra:** git guarda
los ficheros **con LF**, asi que **la convencion DISCO de un fichero con CRLF no se
puede recuperar de git**. Ese cotejo acusaba a
`docs/loop/SALIDA_V187_TALLADOR_CABECERA.txt` de publicar **2444** en disco cuando
git dice **2424**, **y la acusacion era falsa**: git nunca tuvo la version con
CRLF. **Es la caida del recuadro de `AUDITOR.md` 0 otra vez: la fuente hay que
elegirla antes de contarla.**

**ASI QUE EL CASO DECISIVO COTEJA CONTRA EL DISCO DE HOY**, que es la **misma
fuente que la guarda usa en produccion**, con **una sola excepcion mecanica y
declarada**: las rutas que **esta misma vuelta** ha movido desde ese commit. **La
lista no se teclea**: sale de `git diff --name-only 9a06b7c8 -- <ruta>`. Resultado:

- **`CIFRA parejas que NO calzan contra el disco de hoy: 2`**, las dos de
  `docs/PENDIENTES.md` (publicada 924954, hoy 943276).
- **`CIFRA de esas que son de una ruta QUE ESTA VUELTA MOVIO: 2`**, y la movio la
  TAREA 1 de esta vuelta al escribir la `R.50`.
- **`CIFRA de esas que NO tienen esa excusa, que es el veredicto: 0`.**

**SEIS VISTAS Y CERO QUE NO CALCEN SIN EXCUSA. Las dos cifras se publican, no
solo la que conviene.**

#### 4.b LA SECCION QUE SE DUPLICA. ES LA `C.4`

**`piezas_que_faltan()` EXIGE AHORA QUE LAS SECCIONES SEAN UNICAS Y ESTEN EN
ORDEN**, no solo que existan. **Es la misma especie que la escalada de al lado
corrida un paso:** comprobar que algo **este** no es comprobar que este **bien**.

**EL ROJO VIEJO NO SE REESCRIBE:** una seccion que falta sigue cayendo con su texto
de hoy, palabra por palabra (`(3) faltan las secciones 5`), y el arnes lo exige.
Lo que se **anade** son dos motivos, cada uno con **sus lineas nombradas**.

**SOBRE EL TEXTO REAL DEL REPORTE DE LA 187, LA PIEZA (3) LO ACUSA:**

```
(3) hay secciones DUPLICADAS: `## 9.` aparece 2 veces, en las lineas 870, 920
(3) hay secciones FUERA DE ORDEN: `## 9.` en la linea 920 va detras de `## 10.` en la linea 877
```

**Y EL ORDEN SE MIDE POR LA POSICION, NO POR LA PRIMERA APARICION, Y ESO ES LO QUE
LO HACE FUNCIONAR:** mirando solo la primera aparicion de cada cabecera el reporte
de la 187 sale `0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10` y **parece ordenado**. Leyendolas
en el orden en que estan escritas sale `..., 9, 10, 9`. **Medir el orden por la
primera aparicion es no medirlo**, y esa frase esta escrita dentro de la funcion.

**Y NO ACUSA A CUALQUIERA, MEDIDO SOBRE LOS TRES REPORTES ARCHIVADOS ANTERIORES:**
`REPORTE_V184.md`, `REPORTE_V185.md` y `REPORTE_V186.md` tienen **1 seccion `## 9.`
cada uno**, **0 duplicadas y 0 fuera de orden**.

#### EL ARNES, QUE NACE EN ESTA VUELTA

`scripts/loop/vuelta188_tarea4_mutacion_cobertura_parejas.py`. Salida:
`docs/loop/SALIDA_V188_T4_MUTACION_COBERTURA_PAREJAS.txt`, **`CIFRA casos: 17 |
pasan: 17`**, **`CIFRA casos que CAEN al mutar su esperado: 16 de 16`**, **`CIFRA
fallos: 0`**, **`VEREDICTO: VERDE`**, exitcode **0**.

**Y ESTE ARNES NACIO EN ROJO Y SE PUBLICA QUE NACIO EN ROJO**, por la adjudicacion
`5.2` del acta 186: su primera corrida dio **`CIFRA fallos: 3`** y **`VEREDICTO:
ROJO`**, y los tres eran hallazgos de verdad, no fallos del sujeto: (1) el cotejo
contra el arbol del commit acusaba en falso al tallador por la convencion de
disco; (2) el denominador de la cobertura dejaba fuera la pareja de la linea 398;
y (3) el caso C arrastraba a los dos. **Los tres se repararon en el arnes, ninguno
aflojando el sujeto**, y el motivo esta escrito dentro del propio fichero.

**Y ESTA VUELTA NO ESCRIBE DOS SECCIONES 9.** La unica seccion 9 de este reporte es
la que talla `scripts/loop/cerrar_reporte.py` al cerrar, y lo que hubiera que decir
de la bateria va ahi dentro.
