### TAREA 1. LOS REGISTROS Y LAS DOS REPARACIONES DE CODIGO. CERRADA

**1.a EL ACTA 184 ENTRA EN LA SERIE COMO `R.46`, Y EL NUMERO NO SE TECLEA.**
`scripts/loop/serie_de_registros.py`, corrido en esta vuelta, dice **37 entradas
en dos sedes, cero colisiones, cero huecos, siguiente libre `R.46`**. Los cuatro
numerales del titulo salen de contar el acta acotada (`ACTA_AUDITOR.md`, **lineas
64050 a 64432**, 383 lineas) y no de la memoria:

| lo que se cuenta | cifra | patron que la cuenta | el patron de la 183, al lado |
|---|---:|---|---:|
| adjudicaciones numeradas `5.1` a `5.7` | **7** | `claves_entrecomilladas`, nuevo | **0** |
| la adjudicacion **sin numeral** del punto 6 | **1** (linea **64305**) | `PAT_ADJ_SIN_NUMERAL`, nuevo | no existia |
| caidas propias del auditor | **0**, DECLARADAS en la linea **64108** | negrita de frase | **0** de linea |
| caidas del ejecutor | **1**, `E.1`, linea **64337** | patron de linea | **0** con el de la 183 |

(cifras contadas de `docs/loop/SALIDA_V184_T1A_REGISTRO_R46.txt`, **3.916 bytes**,
74 lineas.)

**DOS COSAS QUE ESTA ACTA TRAE Y NINGUNA ANTERIOR, Y LAS DOS SE MIDEN EN VEZ DE
SUPONERSE.** La primera: **el acta 184 escribe sus numerales entre comillas
inversas** (``**`5.1` PD.1, ...``) y la 183 no. Corrido sobre ella el patron
importado, que pide ``**5.1 `` con espacio detras, da **0**. **Se anade un patron
nuevo y el viejo se conserva intacto con su cero publicado al lado**, que es la
doctrina que el propio acta adjudico a favor en su `5.3`. La segunda: **la
adjudicacion del punto 6 no lleva numeral `5.n`**, vive en cabecera de seccion
propia, y **un contador que solo barra `5.n` la pierde**. Se cuenta aparte y el
titulo la nombra.

**EL CERO DE CAIDAS PROPIAS VA CON SU DECLARACION AL LADO O EL INSTRUMENTO HACE
PARADA.** El patron da **0** y el acta lo declara con todas las letras en la linea
**64108**. Si diera cero y el acta no lo declarara, la entrada **no se escribe**:
esa es la guarda, no una advertencia.

**LA DEUDA DE LA SERIE, REMEDIDA EN ESTA VUELTA Y NO HEREDADA DEL `R.45`:**
**8 actas sin entrada propia**, las **173 a 180**, con sus dos extremos computados,
**`R.42` cubre el acta 172** y **`R.43` cubre el acta 181**. **No se rellenan
aqui.**

**CASO POSITIVO POR MUTACION:** `docs/loop/SALIDA_V184_T1A_MUTACION_REGISTRO_184.txt`
(**3.976 bytes**, 60 lineas). **CIFRA fallos: 0.** Siete mutaciones sobre variable
computada, incluida la que quita el punto 6 del acta fabricada y exige que el
cuarto numeral del titulo **cambie con el**.

**1.b LA REPARACION DEL ARNES QUE PARO LA BATERIA, QUE ES LA ADJUDICACION DEL
PUNTO 6.** `scripts/loop/vuelta165_tarea2_mutacion_censo.py`, caso
`A_el_patron_VIEJO_no_ve_dos_de_su_propia_nomina`. **Lo que pasaba antes no se
borra, se cuenta**, y esta escrito entero en el docstring del propio fichero: la
lista era **dos nombres TECLEADOS** contra una nomina que solo crece, y el 5 sep la
medicion daba **cinco**.

Las cuatro cosas que el acta adjudica, ejecutadas sin decidir nada mas:

1. **`esperadas` se computa** de la nomina real por la via directa
   (`[n for n in nomina_real if not PATRON_ARNES_VIEJO.match(n)]`). **No se
   tecleo un 5 encima del 2:** eso es resolver la discrepancia copiando.
2. **El caso A sigue mirando la nomina REAL.** No se apunto a una nomina
   fabricada: es el unico de los trece que la mira, y vaciarlo habria comprado el
   verde.
3. **Los dos ficheros que el auditor de la 165 nombro no se borran.** Viven en
   `LOS_DOS_DE_LA_165` y el caso nuevo,
   `A_los_dos_de_la_165_siguen_DENTRO_del_invisible`, exige que sigan **dentro**
   del conjunto y no que sean **todo** el conjunto. Medido hoy: **de esos dos, los
   que ya no estan dentro son 0**.
4. **La cifra sale con su corte** por banco `9.21`, via `B.sello_de_corte`:
   *"5 (corte: HEAD ..., de 113 de nomina, contadas en esta corrida)"*.

**EL ARNES ENTERO VUELVE A CORRER Y TODOS SUS CASOS CAEN AL MUTAR SU ESPERADO:**
`docs/loop/SALIDA_V184_T1B_ARNES_REPARADO.txt` (**7.314 bytes**, 85 lineas),
**exitcode 0**, **14 casos, 14 pasan, 0 fallan, 14 caen al mutar el esperado**.
El arnes pasa de 13 casos a 14 porque el caso A se parte en dos afirmaciones que
fallan por separado.

**1.c LA ESTIMACION DEL `--plan` SALE CON SU CORTE PEGADO. ES LA ESCALADA.**
`scripts/loop/vuelta183_bateria_por_tramos.py` gana **tres funciones PURAS**:
`linea_de_estimacion()`, `corte_de_la_estimacion()` y `corte_calza()`. Las dos
lineas de `ESTIMACION` salen ahora asi, medidas de la salida real del `--plan` de
hoy:

- `ESTIMACION minutos por tramo de 13 entradas: entre 4.3 y 5.6 (corte: HEAD 2e7bfd57c69e, nomina de 113 entradas contada en esta corrida)`
- `ESTIMACION minutos de la nomina entera: entre 37.3 y 48.6 (corte: HEAD 2e7bfd57c69e, nomina de 113 entradas contada en esta corrida)`

**ARNES PROPIO, `scripts/loop/vuelta184_tarea1c_mutacion_estimacion.py`**, con
salida en `docs/loop/SALIDA_V184_T1C_MUTACION_ESTIMACION.txt` (**5.564 bytes**, 78
lineas): **14 casos, 14 pasan, 0 fallan, 14 caen al mutar el esperado**. **Las dos
mitades fallan por separado**, que es lo que el encargo pide: una linea **sin
corte** devuelve `None` (caso `A_la_forma_VIEJA_no_tiene_corte_y_se_detecta`), y
una linea **con un corte que dice otra nomina** no calza (caso
`B_un_corte_de_otra_nomina_NO_calza`). Y el bloque C **corre `--plan` en un
proceso de verdad** y exige que **las dos** lineas lleven corte y que ese corte
coincida con la nomina que **esa misma corrida** imprime: si alguien devuelve las
lineas a su forma vieja, **ese bloque cae**.

**1.d LA RELECTURA AL DOBLE DEL TRAMO DE LA CIEGA DEL ACTA 184.**
`docs/loop/SALIDA_V184_T1D_RELECTURA_AL_DOBLE.txt` (**12.381 bytes**, 147 lineas).

**EL COTEJO DEL `sha256` FUE ANTES DE LEER UN SOLO PUESTO, Y CALZO:** el sello
`docs/loop/SELLO_APERTURA_AUDITOR_V185.json` (**674 bytes**) declara **38.747
bytes** y `sha256` `f81f1b32594221f1...`; el fichero de hoy mide **38.747 bytes**
y su `sha256` computado es el mismo. **30 puestos** leidos de la ciega sellada
(el acta, contada, lista **0**), **30 vecinos deterministas** con `vecinos()`
importado, **solape 0**, **60 puestos releidos, que es el doble exacto**. Solape
con la ciega anterior (`_auditor_v184_ciega_blind.txt`, 30 puestos): **0**.

| lo que la vara ve en los 60 | cifra |
|---|---:|
| declaran diferenciador | **6** |
| con LESION EXACTA | **1**, el puesto **3.141** |
| con algun nodo muerto en el grafo de hoy | **0** |
| clase `A` | **9** |
| clase `D` | **51** |

**LOS TRES PUESTOS QUE EL AUDITOR PIERDE, MIRADOS CON LA MISMA VARA Y SIN
RE-DECIDIR NINGUNA CLASE:** el **641** (`A`), el **2.493** (`D`) y el **2.594**
(`D`), **los tres dentro del universo releido**, **ninguno declara diferenciador y
ninguno tiene lesion**. **Lo que la vara no ve, esta salida no lo afirma.**

**LO QUE ARRASTRAN 1.b Y 1.c SOBRE LA NOMINA, MEDIDO ANTES DE TOCAR LA BATERIA.**
`scripts/loop/vuelta184_tarea1c_mutacion_estimacion.py` entra en la nomina en su
misma vuelta por la regla del acta 176 punto 7.2, y la medicion la respalda:
`arneses_que_faltan()`, corrido con el fichero escrito y antes de anadirlo, dijo
**faltan 1** y su unico nombre era ese. **La nomina pasa de 112 a 113.** El
registrador de la 1.a **no entra**, porque el censo no lo reconoce como arnes.

`docs/loop/SALIDA_V184_T1_REPARTO_ANTES_Y_DESPUES.txt` (**1.443 bytes**, 27
lineas) mide el reparto **antes y despues**, comparando cada tramo **por su
contenido y no por su tamano**: con tamano 13, **los tramos 1 a 8 salen IDENTICOS
entrada por entrada** y el que crece es el **noveno**, de **8 a 9**. **Las
fronteras de los tramos 1 a 5 no se movieron: 5 de 5 identicos. No hay parada.**

**LOS TRES CLONES DECLARADOS DE ESTA VUELTA, COTEJADOS Y NO AFIRMADOS.**
`docs/loop/SALIDA_V184_COTEJO_DE_CLONES.txt` (**24.487 bytes**, 381 lineas). **No
se afirma que ningun diff salga vacio, y no salen:** el esqueleto tiene **0
sentencias de codigo distintas y 47 literales de texto**; el bloque de apertura
**70 sentencias de codigo y 78 literales**; la relectura al doble **9 tokens de
maquina distintos**. Las tres diferencias son las que estas paginas describen.
