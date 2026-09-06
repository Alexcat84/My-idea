### TAREA 1. LOS REGISTROS Y LA ESCALADA

**1.a. EL ACTA 182 ENTERA, REGISTRADA COMO `R.44`.** Instrumento
`scripts/loop/vuelta183_tarea1a_registrar_acta182.py`, salida
`docs/loop/SALIDA_V183_T1A_REGISTRO_R44.txt` (**4.498 bytes en disco y 4.498
bytes normalizados a LF**). El numero lo devolvio
`serie_de_registros.siguiente_libre()` y **no se tecleo**: la serie recomputada
de sus dos sedes daba **35 entradas, 0 colisiones y 0 huecos**, y el siguiente
libre **R.44**. Tras escribir: **36 entradas, 0 colisiones y 0 huecos**.
`docs/PENDIENTES.md` pasa de **850.711 bytes** a **862.331 bytes en disco y
862.331 bytes normalizados a LF**.

**LOS TRES NUMERALES DEL TITULO SE CONTARON DEL ACTA ACOTADA** (lineas 63250 a
63681, 432 lineas): **12 adjudicaciones** (7 de la seccion 5, `5.D.1` a `5.D.7`,
lineas 63456, 63465, 63472, 63480, 63489, 63495 y 63503; y 5 de la seccion 7,
`7.1` a `7.5`, lineas 63563, 63578, 63583, 63588 y 63607), **1 caida propia del
auditor** (`C.1`, linea 63294) y **2 caidas del ejecutor** (`E.1` en la 63510 y
`E.2` en la 63532).

**HIZO FALTA CODIGO PROPIO, Y ESTA MEDIDO EN VEZ DE SUPUESTO.** El registrador de
la 182 barre un solo prefijo del tipo `**7.n `: corrido sobre esta acta da **5** y
**dejaria las 7 de la seccion 5 fuera**, porque el acta las escribe como
``**`D.1`,``. Y el patron de caida del auditor de la 182 (``**`C.n`.`` al
principio de linea) **cuenta CERO** sobre el acta 182, que escribe la suya dentro
de una frase en negrita, *"**MI CAIDA PROPIA, `C.1`, Y VA IGUAL AUNQUE EL SELLO
AGUANTARA.**"*; el patron mas viejo (`**CAIDA n.`) tambien cuenta **CERO**. **Se
anaden patrones, no se ensancha el viejo hasta que trague**, y las dos cifras de
cero van publicadas al lado de la buena.

**CASO POSITIVO POR MUTACION VERDE**, salida
`docs/loop/SALIDA_V183_T1A_MUTACION_REGISTRO.txt` (**2.310 bytes en disco y 2.310
bytes normalizados a LF**), **0 fallos**: 4 actas fabricadas con cifras distintas,
los contadores calzan con las cuatro; el esperado mutado **CAE**; el patron de
caida del acta 181 sobre un acta en forma 182 da **CERO**; el prefijo `6.` sobre
un acta que numera `7.n` da **CERO**; y `actas_sin_entrada()`, que es pura, se
tumba sobre una serie fabricada y devuelve el salto y **sus dos extremos**
computados.

**1.b. LA DEUDA DE OCHO REGISTROS, DOCUMENTADA COMO SALTO Y NO RELLENADA.** Va
dentro del propio `R.44`, en una **sola linea de constancia**, que es lo que la
adjudicacion `7.4` del acta 182 encarga con estas palabras: *"la deuda se
documenta como salto, no se inventa"*. Contado por el instrumento y no tecleado
(seccion G de su salida): **8 actas sin entrada propia, las 173 a 180**, con sus
dos extremos **`R.42`, que cubre el acta 172**, y **`R.43`, que cubre el acta
181**. **No se escriben ocho registros de memoria.**

**1.c. LA ESCALADA DE `AUDITOR.md` 1.2, QUE ES LA OPERACION DE CODIGO DE ESTA
VUELTA.** `scripts/loop/cerrar_reporte.py` (**54.697 bytes en disco y 54.697
bytes normalizados a LF**) gana su **septima comprobacion**, cuatro funciones
**PURAS** y un carril nuevo en `main()`:

- `numerales_del_veredicto()`, que lee los numerales **en cifra y en letra**
  (`cero` a `quince`), que es como el veredicto de una linea los escribe.
- `caidas_propias_del_cuerpo()`, que cuenta las cabeceras `C.n` **de la seccion 8
  y solo de ahi**: un reporte cita `C.n` ajenas en su prosa y contarlas seria
  fabricar un rojo.
- `tareas_de_la_tabla()`, que cuenta las filas entre las dos marcas de la tabla,
  reconociendo una fila por llevar `TAREA <numero>` dentro y no por su posicion.
- `numerales_del_veredicto_que_no_calzan()`, que las junta y devuelve los motivos.

**SI UN NUMERAL NO CALZA, EL CIERRE CAE EN ROJO Y NO ESCRIBE NADA:** el carril
`B.1)` corre **antes** del bloque que escribe, sobre `texto + cuerpo`, que son las
dos mitades del reporte (la tabla vive en el esqueleto, la seccion 8 en el
borrador del cierre). **Y cae tambien si el veredicto publica una cifra que el
cuerpo no permite contar**, porque una cifra sin fichero que la sostenga no cierra
un reporte.

**EL CASO ROJO ES REAL Y NO FABRICADO, Y SE PROBO POR MUTACION.** Arnes
`scripts/loop/vuelta183_tarea1c_mutacion_veredicto.py`, salida
`docs/loop/SALIDA_V183_T1C_MUTACION_VEREDICTO.txt` (**7.681 bytes en disco y
7.681 bytes normalizados a LF**), **0 fallos**. El veredicto de la 182 se lee de
`docs/loop/reportes/REPORTE_V182.md:46` y no se teclea; sus contadores, corridos
sobre ese mismo fichero, dan **7 caidas propias** (`C.1` a `C.7`, lineas 509, 518,
524, 531, 538, 545 y 549) y **5 filas de tarea**. La guarda lee `'CINCO'` como 5
tareas y `'SEIS'` como 6 caidas, y **CAE con 1 motivo**: *"el veredicto publica
'SEIS' (6 caidas) y el cuerpo, CONTADO, dice 7"*. El mismo veredicto con el
numeral bueno **PASA con 0 motivos**, y la palabra buena se computa de la cuenta,
no se teclea. **Todos los casos del arnes se corrieron con su esperado mutado y
CAEN**, que es lo unico que prueba que podian fallar.

**1.d. EL HUECO DE LA SECCION 9 YA DICE CUAL DE LOS DOS CASOS ES.** Adjudicacion
`7.1` del acta 182. **Lo que pasaba antes no se borra, se cuenta:** `main()` hacia
`tam = os.path.getsize(ruta_bat) if existe else -1` y la seccion publicaba
`max(tam, 0)`, o sea **el mismo cero en los dos casos**, y el arnes lo mide:
`max(-1, 0) = 0` y `max(0, 0) = 0`. Ahora lo arma `frase_del_caso_del_hueco()`,
**pura y con arnes propio**, que devuelve tres textos distintos: **EL FICHERO NO
EXISTE** (y dice que `getsize` *"no llego a correr sobre el"*), **EL FICHERO
EXISTE Y MIDE CERO** (y dice que *"el cero es una medicion, no el resultado de un
`max`"*) y el tercero para el fichero con cuerpo. **Las tres siguen trayendo su
cifra de bytes y ninguna deja una cifra sin su pareja**, comprobado en el mismo
arnes con `PATRON_BYTES` y con `cifras_sin_pareja()`: **las tres piezas que el
hueco ya exige quedan intactas.**

**LOS TRES ARNESES VIEJOS DEL CIERRE SIGUEN VERDES Y NO SE TOCARON:**
`vuelta172_tarea5_mutacion_cierre.py` **17 de 17**,
`vuelta173_tarea1b_mutacion_hueco.py` **24 de 24** y
`vuelta182_tarea1b_arnes_rama_seccion9.py` **0 fallos**.

**1.e. LA RELECTURA AL DOBLE DEL TRAMO DE LA CIEGA.** Instrumento
`scripts/loop/vuelta183_tarea1e_relectura_al_doble.py`, salida
`docs/loop/SALIDA_V183_T1E_RELECTURA_AL_DOBLE.txt` (**12.375 bytes en disco y
12.375 bytes normalizados a LF**). **30 puestos del tramo + 30 vecinos
deterministas = 60**, solape entre tramo y vecinos **0**, solape con el tramo de
la 181 **0**. **60 releidos: 2 declaran diferenciador, 1 tiene LESION EXACTA (el
puesto 978) y 0 tienen un nodo muerto.** Reparto por clase de los 60: **A 16, B 1,
D 43**. Los seis puestos que el auditor discrepa (375, 393, 1280, 1815, 2416 y
2470) estan **los seis** dentro del universo releido. **Ninguna clase se vuelve a
decidir:** `vecinos()` se importa del instrumento de la 182 y la vara se importa
de `vuelta182_tarea3_diferenciador_movido.py`; lo que la vara no ve, la salida no
lo afirma.

> **CORRECCION DECLARADA, Y NO TAPA LO QUE CORRIGE.** El encargo dice que el tramo
> son *"los 30 puestos de la seccion 9 de mi acta 182"*. **Medido en la apertura,
> antes de escribir ninguna linea de la tarea** (bloque H.8 de
> `docs/loop/SALIDA_V183_APERTURA.txt`): la seccion 9 del acta 182 son las lineas
> **63644 a 63658** y es **LA METRICA DE CREDITO**, una tabla que dice *"puestos |
> 30 aislados, 30 limpios | 736"* **y no lista ningun puesto**; el parseo devolvio
> **CERO**. La ciega del acta 182 es su **seccion 4**, y ahi solo estan **los 6
> puestos que discrepan**. Los 30 viven en el fichero que el propio auditor sello,
> `docs/loop/_auditor_v183_ciega_blind.txt`, y el instrumento **lo coteja contra
> `SELLO_APERTURA_AUDITOR_V183.json` antes de leer un solo puesto**: **41.200
> bytes** declarados y **41.200 bytes** en disco, `sha256` `226f577c7f5a2885` en el
> sello y `226f577c7f5a2885` hoy. **Si no calzaran, no releeria nada.**

**Y UNA COSA QUE ESTA TAREA ENCONTRO Y NO ESTABA ENCARGADA, PORQUE HABRIA PUESTO
LA BATERIA ENTERA EN ROJO.** Al abrir la vuelta, **antes de tocar nada**, el
bloque H.9 de la apertura midio `arneses_que_faltan() HOY: ultima vuelta 180,
faltan 1`, y ese uno es **`vuelta182_tarea2_mutacion_apertura_auditor.py`**: la
vuelta 182 escribio ese arnes en su TAREA 2 y **no lo metio en la nomina**. Con el
fuera, **`hay_rojo_al_cierre()` habria cerrado en ROJO los nueve tramos** de esta
bateria, y un rojo que no senala ninguna guarda rota es justo lo que la `D.4` del
acta 182 llama *"entrenar a mirar los rojos con desgana"*. Entra por la regla de
siempre, que el acta 176 punto 7.2 fijo y la `D.4` del acta 182 reconfirmo: **un
arnes entra en la nomina, y puede entrar en su misma vuelta**. Su clasificacion
era **NO DECIDIBLE** porque trae las dos huellas; la guarda no adivina y pide que
el arnes lo declare, y se declaro **con la medicion delante**: su unica aparicion
de `REPORTE.md` fuera del docstring es **un dato dentro de una tabla de
escenarios** y el fichero fabrica todo lo suyo en un `mkdtemp`. Entra con el, por
la misma regla, **el arnes de la 1.c de esta vuelta**. **La nomina crece de 109 a
111 y no se poda nada.** Remedido despues: `arneses_que_faltan()` **0**,
`nomina_invisible_al_censo()` **0**, `guarda_del_sujeto_congelado()` **0**, y el
reparto sigue dando **NUEVE tramos** con **suma 111**.
