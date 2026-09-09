# REPORTE DE LA VUELTA 217 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

> **ESTE REPORTE SE ABRIO AL EMPEZAR LA VUELTA Y CRECE POR ANEXION** (`EJECUTOR.md`
> 1, "EL REPORTE ABRE CON LA VUELTA"). El esqueleto lo tallo
> `scripts/loop/_v217_esqueleto.py` **antes de la primera tarea**; cada tarea
> ANEXA SU FILA AL CERRARSE con `scripts/loop/anexar_tarea_al_reporte.py`; y el
> cierre lo talla entero `scripts/loop/cerrar_reporte.py`. **Si esta vuelta se
> corta, la fila que siga diciendo ABIERTA, SIN CERRAR es la que no se hizo.**
>
> **LAS CUATRO MARCAS DEL ANEXO NACEN CON EL ESQUELETO, COMO DE LA 209 A LA 216.**
> No se teclean: se **IMPORTAN de `anexar_tarea_al_reporte.py`**, que es el
> instrumento que las lee, y se comprueba ANTES de tallar que es lo que ese
> instrumento exige. **Las cuatro no se citan literalmente en esta prosa a
> proposito**: la guarda las cuenta sobre el fichero entero y una cita en prosa
> las duplicaria. **Y el texto se COMPONE EN MEMORIA, SE JUZGA ENTERO Y SOLO SE
> ESCRIBE SI EL JUICIO DA CERO FALLOS.**
>
> **DOS TAREAS, Y LA 217 NO ES VUELTA DE BATERIA Y NO LA CORRE.** La 215 la
> corrio entera por sus once tramos, y el encargo de esta vuelta lo verifico con
> su cifra: su compuesta mide **93498 bytes en disco y 93498 normalizado a LF**,
> commit `abe21a67`. La cadencia de cinco de `AUDITOR.md` 6.1 pone la siguiente
> en la **220**. La seccion 9 de este reporte cierra por tanto con el **HUECO
> DECLARADO Y MEDIDO** por el carril de la TAREA 1.b de la vuelta 173, con **el
> nombre, los bytes medidos y la atribucion, LAS TRES JUNTAS**, que es lo que la
> 6.1 manda en las vueltas intermedias.
>
> **LA CLAUSULA CATORCE YA NO BLOQUEA, Y NO LO DECIDI YO.** La adjudicacion 5.2
> del acta 217 resuelve el choque entre el encargo de la 216, que ponia la
> condicion de las CATORCE clausulas en CUBRE, y su propia adjudicacion 5.4, que
> daba `OP-I-01` por cerrada por la DECISION 1 del fundador. **Manda el fundador**
> (`docs/loop/paradas/2026-09-09-plan-agotado-DECISION.md`, DECISION 1). Lo que
> queda por medir, y lo mide la TAREA 1, son **las DIECISIETE clausulas de las
> ocho filas de 0 CODIGO a 07 ADUANA**, que la re-medicion de la 216 no toco.
>
> **RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3). Ningun arnes, guarda ni
> lector nuevo, y ninguno reparado: **las dos tareas son MEDICION y
> VERIFICACION**, que es lo que la moratoria protege. Todo lo que esta vuelta
> escribe en el arbol scripts/loop (**sin comillas inversas, por la obligacion del
> 6.2 del acta 212**) son ficheros `_v217_*` **con prefijo de guion bajo, fuera
> del censo y fuera de la nomina**. La nomina sigue **CONGELADA EN 135** y no se
> poda.
>
> **Y RIGE LA PROHIBICION QUE NO SE NEGOCIA: NINGUNA TAREA DE ESTA VUELTA MUEVE EL
> CAMPO DE ESTADO DE NINGUNA FICHA**, ni toca `docs/plan/08_VERIFICACION.md`, ni
> el inventario, ni el expediente. Se mide, se publica y se dice. **No se
> escribe.** El sha256 del expediente y el de la pagina 08 se publican al entrar
> y al salir.
>
> **RIGE LA OBLIGACION DE DICTADO NUEVA DEL ENCARGO DE LA 217, y nace de una
> caida mia de la 216 que su seccion 3.1 me cobra:** toda cifra de "lo que esta
> vuelta escribio" que se mida ANTES del cierre se publica **CON SU HUECO AL
> LADO, LAS DOS CIFRAS JUNTAS**, la medida y la que el propio cierre anade.
>
> **RIGE LA OBLIGACION DE DICTADO DEL 6.6 DEL ACTA 210:** toda cita de un acta
> anterior lleva **LA LINEA** de `docs/loop/ACTA_AUDITOR.md` donde vive el texto
> citado, **y la linea se LEE, no se recuerda**.
>
> **RIGE LA OBLIGACION DE LAS FILAS:** toda tabla que un compositor arme leyendo
> filas de una salida publica, EN LA MISMA LINEA, cuantas filas armo; y si al lado
> va una cifra de cuantas deberia haber, LAS DOS SE ESCRIBEN JUNTAS.
>
> **Y RIGEN LAS TRES OBLIGACIONES DE DICTADO DEL ACTA 212, LAS TRES SIN CODIGO:**
> ningun reporte cita un directorio a secas como ruta entre comillas inversas
> (adjudicacion 6.2); una seccion suplementaria va detras de la que amplia y nunca
> detras de una mayor (hallazgo 7.1); y el tallador de cabecera corrido en la
> apertura escribe en un nombre con `_RECHAZO`, no en el del cierre.
>
> **LOS SELLOS DE APERTURA SE ESCRIBIERON AL ABRIR.**
> `docs/loop/SALIDA_V217_APERTURA.txt`,
> `docs/loop/SALIDA_V217_HEAD_APERTURA.txt` y el lado APERTURA del ciclo de
> Gate 0 nacen **antes de la primera tarea**, no al cierre. **Y el remedio de la
> 215 se mantiene y no se afloja: el ciclo SELLA SU PROPIA CONSOLA en
> `docs/loop/SALIDA_V217_CICLO_GATE0_APERTURA_CONSOLA.txt`, que es el nombre
> exacto que el compositor busca, y cae en rojo por sus dos puertas, la del
> fichero ausente y la del fichero de cero bytes.**

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

<!-- CABECERA TALLADA -->
**LA TABLA, PEGADA ENTERA DEL FICHERO QUE LA LLEVA Y NO TECLEADA.** Salio
de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 217`, y su salida
cruda vive en `docs/loop/SALIDA_V217_TALLADOR_CABECERA.txt` (2478 bytes en disco y 2458 normalizado a LF, 11 filas de
tabla,
contadas por `scripts/loop/cerrar_reporte.py`). **LA CELDA QUE NO SALGA DE UN
INSTRUMENTO NO SE ESCRIBE.**

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.169 / 684 | **3.853 / 3.169 / 684** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 8.780 / 8.740 / 17.520 / 9.914 | **8.780 / 8.740 / 17.520 / 9.914** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 82 passed (82) / 1.040 passed (1.040) | **82 passed (82) / 1.040 passed (1.040)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+0 / +0 / +0 / +0** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `1522d5dc` (asunto real leido de git log: 'ACTA DEL AUDITOR, VUELTA 216: LA ORDEN DEL FUNDADOR ESTA CORRIDA, LA CLAUSULA CATORCE DEJA DE BLOQUEAR POR DECISION SUYA, Y NO DECLARO NADA CONSUMADO PORQUE DIECISIETE CLAUSULAS DEL CRITERIO DE HECHO NO LAS HA MEDIDO NADIE.'), HEAD real de apertura `1522d5dc` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `46865dd6` (leido de `SALIDA_V217_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |

<!-- FIN CABECERA TALLADA -->

## 1. LAS TAREAS DEL ENCARGO, Y SU ESTADO

<!-- TABLA DE TAREAS -->
| tarea | que es | estado | lo que dejo sellado |
|---|---|---|---|
| **TAREA 1** | LAS DIECISIETE CLAUSULAS DE LAS FASES 0 A 07, MEDIDAS UNA POR UNA, Y ES LA ULTIMA PUERTA DEL PLAN Y ES BLOQUEANTE. Sacar CON UN INSTRUMENTO las filas de la seccion POR FASE de `docs/plan/08_VERIFICACION.md`, publicar cuantas filas se armaron y cuantas deberia haber EN LA MISMA LINEA, y medir cada una de las diecisiete clausulas de las ocho filas de 0 CODIGO a 07 ADUANA con su busqueda corrida y su cifra delante, incluidas las que dan cero. Las clausulas con correccion declarada se miden POR SU LECTURA CORREGIDA. El caso rojo se prueba POR MUTACION, en memoria, y toda clausula que no de CUBRE lleva ademas su mutante SANO. Cero escrituras: ni un campo de estado, ni la pagina 08, ni el inventario, ni el expediente | **CERRADA. 17 de 17 clausulas medidas con su sonda corrida: 12 CUBRE, 5 A MEDIAS, 0 NO CUBRE. 17 de 17 mutantes rotos CAEN y 4 de 4 sanos SUBEN. Cero escrituras: los cuatro sha del expediente y de la pagina 08 coinciden al entrar y al salir** | `SALIDA_V217_T1_DIECISIETE.txt`, `SALIDA_V217_T1_CONTRASTE_V150.txt`, `SALIDA_V217_COMPOSITOR_T1.txt` (sus bytes, por las dos convenciones, van dentro de la seccion y no en esta celda) |
| **TAREA 2** | EL CIERRE INTEGRAL Y EL REPORTE, sin aflojar ninguna guarda. El ciclo entero de Gate 0 por los dos lados con su consola SELLADA desde dentro del propio instrumento; las tres suites solas con su exitcode y sus bytes; marcador y censo recomputados cada uno con su comando; las rutas con `scripts/loop/vuelta186_rutas_del_reporte.py` corrido DESPUES de cerrar el reporte; la cabecera con su tallador y su comparacion; y el cierre con `scripts/loop/cerrar_reporte.py`, que con la 215 y la 216 harian tres seguidas. Y las cifras del auditor cotejadas contra las mias en DOS COLUMNAS | **CERRADA. Ciclo de Gate 0 por los dos lados con 18 de 18 salidas selladas, 0 ausentes, 0 de cero bytes y peor exitcode 0; las tres suites solas en exitcode 0; 16 de 16 cifras del auditor cotejadas y 0 que no calzan; 13 sedes cotejadas y 0 movidas; y la cifra de lo escrito publicada CON SU HUECO AL LADO** | `SALIDA_V217_T2_CIERRE.txt`, `SALIDA_V217_CICLO_GATE0_CIERRE_CONSOLA.txt`, `SALIDA_V217_T2_SUITE_MOTOR.txt`, `SALIDA_V217_T2_SUITE_TSC.txt`, `SALIDA_V217_T2_SUITE_WEB.txt`, `SALIDA_V217_T2_MARCADOR.txt`, `SALIDA_V217_T2_ARISTAS.txt`, `SALIDA_V217_COMPOSITOR_T2.txt` (sus bytes van dentro de la seccion) |
<!-- FIN TABLA DE TAREAS -->

## 2. LAS TAREAS, AL DETALLE (cada seccion se ANEXA al cerrarse su tarea)

<!-- ANEXO DE TAREAS -->

### TAREA 1. LAS DIECISIETE CLAUSULAS DE LAS FASES 0 A 07, MEDIDAS UNA POR UNA

**LO QUE SE CORRIO, Y SU RUTA CON SUS BYTES:**
``docs/loop/SALIDA_V217_T1_DIECISIETE.txt``, **37762 bytes en disco y 37339 normalizado a LF**, exitcode 0.
Y el contraste, ``docs/loop/SALIDA_V217_T1_CONTRASTE_V150.txt``, **858 bytes en disco y 837 normalizado
a LF**, exitcode 1 y su motivo escrito abajo.

**EL INSTRUMENTO NO ES NUEVO POR DENTRO Y ESO IMPORTA CON LA MORATORIA
ENCIMA** (`AUDITOR.md` 6.3). Los lectores se **IMPORTAN** de
`scripts/loop/vuelta150_4_tabla_por_fase.py`, que es la sede donde ya viven:
`celdas_de_la_tabla`, `fichas`, `grafo`, `resolutor`, `gate0_checks` y
`guarda_salidas_congeladas`. Lo unico propio de esta vuelta es **el partido de
las celdas en clausulas y las diecisiete sondas**, que es medicion y es lo que
la moratoria protege.

**CIFRA lineas de ese fichero: 626 | CIFRA lineas ejecutadas al cargarlo: 622. La diferencia es SU ULTIMA LINEA DE ENTRADA, una llamada suelta a main() sin guarda, que se descarta para cargar sus lectores sin correr su tabla. EL FICHERO EN DISCO NO SE TOCA: la moratoria prohibe repararlo y no se repara.**

#### 1.a. LAS FILAS Y SUS CLAUSULAS, SACADAS CON UN INSTRUMENTO Y NO A MANO

**LAS CUATRO CIFRAS, CADA UNA CON LA DEL ENCARGO AL LADO Y EN LA MISMA LINEA,
que es lo que la obligacion de las filas manda:**

```
CIFRA FILAS ARMADAS LEYENDO LA TABLA POR FASE: 11 | CIFRA FILAS QUE DEBERIA HABER: 11
CIFRA CLAUSULAS ARMADAS EN LA TABLA ENTERA: 30 | CIFRA QUE DEBERIA HABER: 30
CIFRA FILAS DE 0 CODIGO A 07 ADUANA ARMADAS: 8 | CIFRA QUE DEBERIA HABER: 8
CIFRA CLAUSULAS DE ESAS OCHO FILAS ARMADAS: 17 | CIFRA QUE DEBERIA HABER: 17
CIFRA descuadres contra las cifras del encargo: 0
```

**EL REPARTO POR FILA, CONTADO Y NO TECLEADO** (11 filas leidas del fichero, 11
que deberia haber):

```
  0 CODIGO               clausulas armadas  1 | que deberia haber 1
  01 FUENTES             clausulas armadas  2 | que deberia haber 2
  02 DESTEJIDOS          clausulas armadas  2 | que deberia haber 2
  03 FUSIONES            clausulas armadas  2 | que deberia haber 2
  04 ENLACES             clausulas armadas  2 | que deberia haber 2
  05 SANEO               clausulas armadas  6 | que deberia haber 6
  06 MESAS               clausulas armadas  1 | que deberia haber 1
  07 ADUANA              clausulas armadas  1 | que deberia haber 1
  08 VERIFICACION        clausulas armadas  1 | que deberia haber (fuera de las ocho: el encargo no da cifra)
  09 LECTURAS DIRIGIDAS  clausulas armadas  8 | que deberia haber (fuera de las ocho: el encargo no da cifra)
  10 INVENTARIO          clausulas armadas  4 | que deberia haber (fuera de las ocho: el encargo no da cifra)
```

**LAS DIECISIETE, VERBATIM** (17 filas leidas del fichero, 17 que deberia
haber):

```
  0 CODIGO         idx 0 | cada caso positivo **se cae antes** del arreglo y pasa despues
  01 FUENTES       idx 0 | ningun nodo de la clase con pasos alterados
  01 FUENTES       idx 1 | **el material del segundo libro reubicado, no borrado**
  02 DESTEJIDOS    idx 0 | los **quince congelados** releidos
  02 DESTEJIDOS    idx 1 | **cada perdida en el bloque del que proviene**
  03 FUSIONES      idx 0 | un superviviente por acto, el resto **DEPRECADO CON ALIAS**
  03 FUSIONES      idx 1 | `resolverId` devuelve el superviviente
  04 ENLACES       idx 0 | cada arista nueva **confirmada por lectura**, no por el instrumento
  04 ENLACES       idx 1 | ninguna crea auto-arista tras resolver
  05 SANEO         idx 0 | ningun id vivo con tratado extinto
  05 SANEO         idx 1 | los tres de Incoterms con su version
  05 SANEO         idx 2 | ningun nodo cablea `export.gov`
  05 SANEO         idx 3 | ninguna de las seis herramientas muertas
  05 SANEO         idx 4 | ningun nodo con dos claves de fase
  05 SANEO         idx 5 | **ningun nodo se cita a si mismo tras resolver**
  06 MESAS         idx 0 | cada decision escrita **con su motivo y su cobertura al lado** (banco 9.26)
  07 ADUANA        idx 0 | los cuatro controles mecanicos **corriendo en Gate 0**
```

#### 1.b Y 1.c. EL VEREDICTO DE CADA UNA, CON SU BUSQUEDA CORRIDA

**LA TABLA SALE DEL FICHERO Y SE CUENTA ANTES DE PUBLICARLA: 17 filas de
datos leidas, 17 que deberia haber.**

| # | fila | idx | veredicto | la clausula, VERBATIM |
|---:|---|---:|---|---|
| 1 | 0 CODIGO | 0 | CUBRE | cada caso positivo **se cae antes** del arreglo y pasa despues |
| 2 | 01 FUENTES | 0 | A MEDIAS | ningun nodo de la clase con pasos alterados |
| 3 | 01 FUENTES | 1 | A MEDIAS | **el material del segundo libro reubicado, no borrado** |
| 4 | 02 DESTEJIDOS | 0 | CUBRE | los **quince congelados** releidos |
| 5 | 02 DESTEJIDOS | 1 | A MEDIAS | **cada perdida en el bloque del que proviene** |
| 6 | 03 FUSIONES | 0 | A MEDIAS | un superviviente por acto, el resto **DEPRECADO CON ALIAS** |
| 7 | 03 FUSIONES | 1 | CUBRE | `resolverId` devuelve el superviviente |
| 8 | 04 ENLACES | 0 | CUBRE | cada arista nueva **confirmada por lectura**, no por el instrumento |
| 9 | 04 ENLACES | 1 | CUBRE | ninguna crea auto-arista tras resolver |
| 10 | 05 SANEO | 0 | CUBRE | ningun id vivo con tratado extinto |
| 11 | 05 SANEO | 1 | A MEDIAS | los tres de Incoterms con su version |
| 12 | 05 SANEO | 2 | CUBRE | ningun nodo cablea `export.gov` |
| 13 | 05 SANEO | 3 | CUBRE | ninguna de las seis herramientas muertas |
| 14 | 05 SANEO | 4 | CUBRE | ningun nodo con dos claves de fase |
| 15 | 05 SANEO | 5 | CUBRE | **ningun nodo se cita a si mismo tras resolver** |
| 16 | 06 MESAS | 0 | CUBRE | cada decision escrita **con su motivo y su cobertura al lado** (banco 9.26) |
| 17 | 07 ADUANA | 0 | CUBRE | los cuatro controles mecanicos **corriendo en Gate 0** |

**EL REPARTO, CONTADO DE ESA MISMA TABLA: 12 en CUBRE, 5 en
A MEDIAS, 0 en NO CUBRE y 0 SIN SONDA, de 17.**

**LAS QUE NO DAN CUBRE, CON SU FILA, SU INDICE Y SU CIFRA** (5 lineas
leidas del fichero):

```
01 FUENTES       idx 0 | A MEDIAS  | ningun nodo de la clase con pasos alterados
01 FUENTES       idx 1 | A MEDIAS  | **el material del segundo libro reubicado, no borrado**
02 DESTEJIDOS    idx 1 | A MEDIAS  | **cada perdida en el bloque del que proviene**
03 FUSIONES      idx 0 | A MEDIAS  | un superviviente por acto, el resto **DEPRECADO CON ALIAS**
05 SANEO         idx 1 | A MEDIAS  | los tres de Incoterms con su version
```

**LAS DOS CLAUSULAS CON CORRECCION DECLARADA SE MIDIERON POR SU LECTURA
CORREGIDA, NO A LA LETRA**, y las dos son de la fila `05 SANEO`: *"ningun nodo
cablea export.gov"* (idx 2) y *"ninguna de las seis herramientas muertas"*
(idx 3). La correccion vive en las **lineas 35 a 58** de
`docs/plan/08_VERIFICACION.md`, se leyo entera antes de medir, y su efecto esta
medido: **la de las seis herramientas, medida A LA LETRA, daria NO CUBRE por UNA
mencion viva** (`Alexa` en `inteligencia_de_anuncios_de_la_competencia`), y esa
mencion esta **FUERA de la nomina de `OP-S-04`** y el fundador ya la saco de la
campana. **Medida acotada da CERO menciones dentro de la nomina, y las dos
cifras se publican juntas.**

#### 1.d. EL CASO ROJO NO SE PROMETE, SE PRUEBA POR MUTACION

**17 mutantes rotos leidos del fichero, 17 que deberia haber, y CAEN
17 de 17.** Ninguno toca una ficha, un nodo ni una pagina: se fabrican en
memoria sobre una copia.

```
MUTANTE ROTO  1 | 0 CODIGO         idx 0 | desaparecen las pruebas, las etiquetas y las salid | veredicto NO CUBRE  | CAE: SI
MUTANTE ROTO  2 | 01 FUENTES       idx 0 | un miembro de la clase queda con un solo paso      | veredicto NO CUBRE  | CAE: SI
MUTANTE ROTO  3 | 01 FUENTES       idx 1 | un nodo de la nomina se borra sin dejar alias      | veredicto NO CUBRE  | CAE: SI
MUTANTE ROTO  4 | 02 DESTEJIDOS    idx 0 | aparece un congelado de la nomina de la fase 02    | veredicto NO CUBRE  | CAE: SI
MUTANTE ROTO  5 | 02 DESTEJIDOS    idx 1 | la pagina 02 se queda sin registros y las fichas s | veredicto A MEDIAS  | CAE: SI
MUTANTE ROTO  6 | 03 FUSIONES      idx 0 | un superviviente pierde sus alias                  | veredicto NO CUBRE  | CAE: SI
MUTANTE ROTO  7 | 03 FUSIONES      idx 1 | un absorbido deja de resolver a su superviviente   | veredicto NO CUBRE  | CAE: SI
MUTANTE ROTO  8 | 04 ENLACES       idx 0 | una arista nueva cita un puesto que no existe      | veredicto A MEDIAS  | CAE: SI
MUTANTE ROTO  9 | 04 ENLACES       idx 1 | una arista nueva se cierra sobre si misma          | veredicto NO CUBRE  | CAE: SI
MUTANTE ROTO 10 | 05 SANEO         idx 0 | el id con el tratado extinto vuelve a estar vivo   | veredicto NO CUBRE  | CAE: SI
MUTANTE ROTO 11 | 05 SANEO         idx 1 | los supervivientes pierden la version              | veredicto NO CUBRE  | CAE: SI
MUTANTE ROTO 12 | 05 SANEO         idx 2 | un nodo de la nomina vuelve a cablear el dominio m | veredicto NO CUBRE  | CAE: SI
MUTANTE ROTO 13 | 05 SANEO         idx 3 | un nodo de la nomina vuelve a nombrar dos muertas  | veredicto NO CUBRE  | CAE: SI
MUTANTE ROTO 14 | 05 SANEO         idx 4 | un nodo recibe una segunda clave de fase           | veredicto NO CUBRE  | CAE: SI
MUTANTE ROTO 15 | 05 SANEO         idx 5 | un nodo vivo se cita a si mismo                    | veredicto NO CUBRE  | CAE: SI
MUTANTE ROTO 16 | 06 MESAS         idx 0 | una nomina de mesa se queda sin cobertura          | veredicto A MEDIAS  | CAE: SI
MUTANTE ROTO 17 | 07 ADUANA        idx 0 | dos controles dejan de correr en Gate 0            | veredicto A MEDIAS  | CAE: SI
```

**Y EL REVERSO, PORQUE UNA SONDA QUE NUNCA PUEDE DECIR CUBRE TAMPOCO MIDE:
4 mutantes SANOS, y SUBEN 4.**

```
MUTANTE SANO    | 01 FUENTES       idx 0 | los seis vuelven al texto del grafo previo         | veredicto CUBRE     | SUBE: SI
MUTANTE SANO    | 01 FUENTES       idx 1 | las nominas dejan de declarar un segundo libro     | veredicto CUBRE     | SUBE: SI
MUTANTE SANO    | 03 FUSIONES      idx 0 | los actos sin fundir quedan con un superviviente y | veredicto CUBRE     | SUBE: SI
MUTANTE SANO    | 05 SANEO         idx 1 | los tres supervivientes traen la version           | veredicto CUBRE     | SUBE: SI
```

#### 1.e. NO SE ESCRIBIO NADA, Y SE PRUEBA CON LOS CUATRO SHA

```
SHA256 DE docs/plan/OPERACIONES.jsonl AL ENTRAR: 650578474361eb2b disco y 650578474361eb2b LF
SHA256 DE docs/plan/OPERACIONES.jsonl AL SALIR: 650578474361eb2b disco y 650578474361eb2b LF
SHA256 DE docs/plan/08_VERIFICACION.md AL ENTRAR: 578eeefab6db2fd4 disco y 578eeefab6db2fd4 LF
SHA256 DE docs/plan/08_VERIFICACION.md AL SALIR: 578eeefab6db2fd4 disco y 578eeefab6db2fd4 LF
LOS CUATRO SHA COINCIDEN CON LOS DE LA ENTRADA: SI
```

**Ni un campo de estado, ni la pagina 08, ni el inventario, ni el expediente.**

#### 1.f. LA DISCREPANCIA CONTRA MI PROPIO ENCARGO, DECLARADA Y NO RESUELTA COPIANDO

**MI ENCARGO DICE, VERBATIM: "LAS OCHO FILAS DE 0 CODIGO A 07 ADUANA, CON SUS
DIECISIETE CLAUSULAS, NO LAS HA MEDIDO NADIE CON UNA SONDA CORRIDA". MEDIDO HOY:
ESO ES CIERTO DE LAS DIECISIETE CLAUSULAS Y NO LO ES DE LAS OCHO FILAS.**

`scripts/loop/vuelta150_4_tabla_por_fase.py` **mide las ocho filas**, una por
fase, con su veredicto de tres palabras, y se corrio en las vueltas 150 a 155.
Lo que nadie habia medido, y es lo que esta tarea mide, son **las diecisiete
clausulas por separado**. Las dos cosas se publican y la discrepancia no se
resuelve copiando (`EJECUTOR.md` 2).

**Y HAY UNA SEGUNDA MITAD, MEDIDA CON SU CORRIDA: ESE INSTRUMENTO HOY CAE EN
ROJO.** Corrido en esta vuelta contra mi propio corte, sale con **exitcode 1**:

```
FILAS DE LA TABLA POR FASE, LEIDAS DE docs/plan/08_VERIFICACION.md: 11
AssertionError: la tabla no trae ocho filas: 11
```

**La causa esta medida y no supuesta:** su `assert` exige OCHO filas y la
correccion declarada de la vuelta 214 dejo **ONCE** en la tabla POR FASE, al
anadir las de las fases 08, 09 y 10. **NO LO REPARO Y ESO ES DELIBERADO: la
moratoria de `AUDITOR.md` 6.3 prohibe reparar arneses, y el propio encargo dice
que las dos tareas de esta vuelta son medicion y verificacion.** Se mide, se
publica y se dice. **Y por lo mismo, para cargar sus lectores sin correr su
tabla se descarta SU ULTIMA LINEA DE ENTRADA al ejecutarlo en memoria: el
fichero en disco no se toca ni en un byte.**

#### 1.g. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**Son lectura mia y por eso van aparte** (`EJECUTOR.md` 7). **Cinco.**

| # | sobre que | que decidi y cual es la duda |
|---|---|---|
| **D.a** | `01 FUENTES` idx 0, la vara del ANTES | Publico **A MEDIAS** y no CUBRE. Los seis miembros de la clase conservan su NUMERO de pasos contra el grafo previo, que es lo que la clase protege; pero DOS tienen texto distinto, y aunque los commits que los tocaron no nombran ninguna operacion de la fase 01, el asunto de un commit es un proxy y no una lectura. Si el auditor lee que la clausula protege el numero y no la letra, esta clausula es CUBRE. |
| **D.b** | `01 FUENTES` idx 1, que es 'reubicado' | Publico **A MEDIAS**. La mitad 'no borrado' esta medida y da CERO borradas de 70 menciones. Para la mitad 'reubicado' elegi como vara que el nodo YA NO declare mas de una fuente, y quedan 7 menciones que todavia declaran dos o mas. Si el auditor lee que reubicar es solo mover el bloque y no reducir el campo, la vara es otra. |
| **D.c** | `02 DESTEJIDOS` idx 1, la anchura del detector | Publico **A MEDIAS** con la regla ESTRECHA, que busca la frase de la regla de reparto, y publico al lado la ANCHA, que busca que la ficha nombre un bloque. Las dos cifras estan en la tabla. Si el auditor lee que nombrar el bloque con otras palabras cumple la clausula, esta es CUBRE por la cifra ancha. |
| **D.d** | `03 FUSIONES` idx 0, el universo de la clausula | Publico **A MEDIAS** midiendo TODOS los actos del corte vigente. La mitad del alias cubre entera y sin excepcion; lo que no cubre es que 71 actos siguen con varios miembros vivos, o sea SIN FUNDIR. Si el auditor lee que la clausula solo habla de los actos YA fundidos, como hace el arnes de la vuelta 150 al medir solo las fichas con superviviente escrito, esta clausula es CUBRE. |
| **D.e** | `07 ADUANA` idx 0, cuatro contra cinco | Publico **CUBRE** porque la clausula pide CUATRO y hay CUATRO corriendo y en verde. Pero la pagina 07 y la verificacion de `OP-A-02` nombran CINCO, y el quinto, la revision de toda nomina por el DOMINIO de sus miembros, NO corre. Si el auditor lee que la celda quedo vieja y que la cifra viva es cinco, esta clausula es A MEDIAS. |

**LO QUE NO PROPONGO, Y DIGO POR QUE.** El encargo escribe la condicion de la
parada feliz antes de saber el resultado: *"si las DIECISIETE quedan en CUBRE
con su busqueda corrida y su cifra delante"*. **No quedan: 5 de 17 dan
A MEDIAS**, y estan nombradas arriba con su fila, su indice y su cifra. **Por
tanto NO propongo declarar la campana consumada.** Lo que si digo, porque es lo
que la medicion sostiene: **ninguna de las diecisiete da NO CUBRE**, y las cinco
que no cubren lo hacen por trabajo pendiente medido y nombrado, no por un fallo
del catalogo.

### TAREA 2. EL CIERRE INTEGRAL, MEDIDO DE SUS FICHEROS Y NO TECLEADO

**EL INSTRUMENTO ES `scripts/loop/_v217_t2_cierre.py` Y SU SALIDA SELLADA ES
`docs/loop/SALIDA_V217_T2_CIERRE.txt`, 10425 bytes en disco y 10425 normalizado a LF.** Todas las
tablas de abajo se cuentan de ese fichero.

#### 2.a.1. EL CICLO ENTERO DE GATE 0, LOS DOS LADOS, CON SU CONSOLA SELLADA DESDE DENTRO

**CIFRA salidas selladas del ciclo: 18 | CIFRA que deberia haber: 18**
**CIFRA ausentes: 0 | CIFRA de cero bytes: 0**
**CIFRA salidas SIN exitcode dentro: 0**
**CIFRA peor exitcode de las dieciocho: 0**

**EL REMEDIO DE LA 215 SE MANTIENE Y NO SE AFLOJA:** el ciclo sella su propia
consola desde dentro, en el nombre exacto que el compositor busca, y cae en rojo
por sus dos puertas, la del fichero **ausente** y la del fichero de **cero
bytes**.

**FILAS ARMADAS LEYENDO `docs/loop/SALIDA_V217_T2_CIERRE.txt`: 2. FILAS QUE DEBERIA HABER: 2.**

| lado | fichero de la consola | bytes, por las dos convenciones | peor exitcode que declara |
|---|---|---|---:|
| **APERTURA** | `docs/loop/SALIDA_V217_CICLO_GATE0_APERTURA_CONSOLA.txt` | **965** bytes en disco y **965** bytes normalizado a LF | 0 |
| **CIERRE** | `docs/loop/SALIDA_V217_CICLO_GATE0_CIERRE_CONSOLA.txt` | **961** bytes en disco y **961** bytes normalizado a LF | 0 |

#### 2.a.2. LAS TRES SUITES SOLAS, CADA UNA CON SU EXITCODE Y SUS BYTES

**FILAS ARMADAS: 3. FILAS QUE DEBERIA HABER: 3.**

| suite | fichero | exitcode | bytes, por las dos convenciones |
|---|---|---:|---|
| **motor** | `docs/loop/SALIDA_V217_T2_SUITE_MOTOR.txt` | **0** | **1160** bytes en disco y **1131** bytes normalizado a LF |
| **tsc** | `docs/loop/SALIDA_V217_T2_SUITE_TSC.txt` | **0** | **11** bytes en disco y **11** bytes normalizado a LF |
| **web** | `docs/loop/SALIDA_V217_T2_SUITE_WEB.txt` | **0** | **334** bytes en disco y **334** bytes normalizado a LF |

#### 2.a.3. EL MARCADOR Y EL CENSO, RECOMPUTADOS CON SU COMANDO Y COTEJADOS SIN COPIAR

**LOS DOS COMANDOS, ESCRITOS ANTES DE SU RESULTADO:**
`python scripts/recomputar_marcador.py 3388` y
`python scripts/loop/vuelta83_conteo_aristas.py WORK`.

**FILAS ARMADAS: 16. FILAS QUE DEBERIA HABER: 16. LA COLUMNA DE LA
IZQUIERDA ES MIA Y LA DE LA DERECHA ES LA DEL ENCARGO**, y van separadas porque
son de autores distintos.

| cifra | LA MIA, recomputada hoy | la del encargo, del auditor | calzan |
|---|---:|---:|---|
| marcador n | **3388** | 3388 | SI |
| marcador A | **550** | 550 | SI |
| marcador B | **72** | 72 | SI |
| marcador C | **5** | 5 | SI |
| marcador D | **2761** | 2761 | SI |
| marcador huecos | **0** | 0 | SI |
| censo nodos | **3853** | 3853 | SI |
| censo vivos | **3169** | 3169 | SI |
| censo deprecados | **684** | 684 | SI |
| aristas siguientes | **8780** | 8780 | SI |
| aristas previos | **8740** | 8740 | SI |
| aristas suma | **17520** | 17520 | SI |
| aristas union | **9914** | 9914 | SI |
| Gate 0 peor exitcode | **0** | 0 | SI |
| salidas selladas del ciclo | **18** | 18 | SI |
| salidas ausentes del ciclo | **0** | 0 | SI |

**CIFRA cifras cotejadas: 16 | CIFRA que NO calzan: 0**

#### 2.a.4. LAS SEDES, Y LA PRUEBA MEDIDA DE QUE ESTA VUELTA NO ESCRIBIO NI UNA FICHA

**CIFRA sedes cotejadas: 13 | CIFRA que se movieron: 0**
**CIFRA sedes cuya quietud se midio por sha256 de apertura: 9 | por git diff, porque la apertura no las nombraba: 4**

```
SEDE docs/plan/INVENTARIO.jsonl                 | al abrir 43cea06634e6fc1a | al cerrar 43cea06634e6fc1a | QUIETA | 629533 / 629533 bytes | cotejo de los dos sha256
SEDE docs/plan/OPERACIONES.jsonl                | al abrir 650578474361eb2b | al cerrar 650578474361eb2b | QUIETA | 517181 / 517181 bytes | cotejo de los dos sha256
SEDE docs/plan/08_VERIFICACION.md               | al abrir 578eeefab6db2fd4 | al cerrar 578eeefab6db2fd4 | QUIETA | 73652 / 73652 bytes | cotejo de los dos sha256
SEDE docs/plan/10_INVENTARIO.md                 | al abrir NO_MEDIDA_AL_ABRIR | al cerrar 67f464d3d0b9e067 | QUIETA | 34258 / 33845 bytes | NO MEDIDA AL ABRIR (no estaba en la lista del sello de apertura): su quietud se mide con git diff --numstat HEAD, 0 filas
SEDE docs/plan/LECTURAS_DIRIGIDAS.md            | al abrir NO_MEDIDA_AL_ABRIR | al cerrar a8ba1749b9a3fa13 | QUIETA | 219178 / 219178 bytes | NO MEDIDA AL ABRIR (no estaba en la lista del sello de apertura): su quietud se mide con git diff --numstat HEAD, 0 filas
SEDE docs/INTRA_DOMINIO_VEREDICTOS.jsonl        | al abrir 758edf1f5c313c18 | al cerrar 758edf1f5c313c18 | QUIETA | 4057130 / 4057130 bytes | cotejo de los dos sha256
SEDE docs/INTRA_DOMINIO_INFORME.md              | al abrir NO_MEDIDA_AL_ABRIR | al cerrar c05b6bcd20188a9c | QUIETA | 943970 / 943970 bytes | NO MEDIDA AL ABRIR (no estaba en la lista del sello de apertura): su quietud se mide con git diff --numstat HEAD, 0 filas
SEDE docs/plan/00_INDICE.md                     | al abrir NO_MEDIDA_AL_ABRIR | al cerrar 2e71336cc2fdc387 | QUIETA | 45278 / 45278 bytes | NO MEDIDA AL ABRIR (no estaba en la lista del sello de apertura): su quietud se mide con git diff --numstat HEAD, 0 filas
SEDE docs/BANCO_DE_TEXTOS.md                    | al abrir 8adbd60239509bb4 | al cerrar 8adbd60239509bb4 | QUIETA | 186490 / 186490 bytes | cotejo de los dos sha256
SEDE docs/plan/BANCO_DEL_PLAN.md                | al abrir 7836c8976c585143 | al cerrar 7836c8976c585143 | QUIETA | 61554 / 61554 bytes | cotejo de los dos sha256
SEDE dataset/metadata/master_graph.json         | al abrir 627cc662296f7f00 | al cerrar 627cc662296f7f00 | QUIETA | 8375817 / 8375817 bytes | cotejo de los dos sha256
SEDE docs/loop/ACTA_AUDITOR.md                  | al abrir d1e494504a480ac5 | al cerrar d1e494504a480ac5 | QUIETA | 5092743 / 5092743 bytes | cotejo de los dos sha256
SEDE docs/loop/PROMPT_SIGUIENTE.md              | al abrir 88e737f47a3be5b9 | al cerrar 88e737f47a3be5b9 | QUIETA | 9216 / 9216 bytes | cotejo de los dos sha256
```

#### 2.a.5. LA MORATORIA, Y LA CIFRA CON SU HUECO AL LADO

**LA OBLIGACION DE DICTADO NUEVA DEL ENCARGO DE LA 217 SE CUMPLE AQUI, Y NACE DE
MI CAIDA DE LA 216:** aquella publico **16** ficheros escritos donde el auditor
conto **18**, porque el instrumento corre **antes** de que el cierre escriba los
suyos. La regla que el encargo fija es publicar **las dos cifras juntas**, la
medida y la que el propio cierre anade, y el hueco no se estima: **se nombra
fichero a fichero**.

**CIFRA ficheros de scripts que esta vuelta escribio, MEDIDA AHORA: 7 | CIFRA de esos con el prefijo que le toca: 7**

**CIFRA MEDIDA AHORA: 7 | CIFRA DEL HUECO QUE EL PROPIO CIERRE ANADE: 4 | CIFRA TOTAL DE LA VUELTA, LAS DOS JUNTAS: 11**
**Y LOS DEL HUECO LLEVAN EL PREFIJO IGUAL: 4 de 4, contado de sus propios nombres.**

```
TOCADO scripts/loop/_v217_apertura.py                       | prefijo _v217_: SI
TOCADO scripts/loop/_v217_ciclo_gate0.py                    | prefijo _v217_: SI
TOCADO scripts/loop/_v217_esqueleto.py                      | prefijo _v217_: SI
TOCADO scripts/loop/_v217_t1_diecisiete.py                  | prefijo _v217_: SI
TOCADO scripts/loop/_v217_t1_seccion.md                     | prefijo _v217_: SI
TOCADO scripts/loop/_v217_t1_seccion.py                     | prefijo _v217_: SI
TOCADO scripts/loop/_v217_t2_cierre.py                      | prefijo _v217_: SI
DEL HUECO scripts/loop/_v217_t2_seccion.py                 | ya contado arriba: NO
DEL HUECO scripts/loop/_v217_t2_seccion.md                 | ya contado arriba: NO
DEL HUECO scripts/loop/_v217_cierre_texto.py               | ya contado arriba: NO
DEL HUECO scripts/loop/_v217_cierre_texto.md               | ya contado arriba: NO
```

#### 2.a.6. LA FECHA, MEDIDA Y NO SUPUESTA

**fecha del commit de apertura, leida de git log: 2026-09-09**
**fecha del commit de ahora mismo, leida de git log: 2026-09-09**

**CIFRA comprobaciones que fallan: 0**

<!-- FIN ANEXO DE TAREAS -->

**EL VEREDICTO DE UNA LINEA: LAS DIECISIETE CLAUSULAS DE LAS FASES 0 A 07 ESTAN MEDIDAS UNA POR UNA CON SU SONDA CORRIDA, 12 CUBREN Y 5 QUEDAN A MEDIAS CON SU CIFRA DELANTE, NINGUNA DA NO CUBRE, EL CIERRE INTEGRAL SALE LIMPIO, Y NO PROPONGO LA PARADA FELIZ PORQUE SU CONDICION NO SE CUMPLE.**

## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS

**TODAS SALEN DE `docs/loop/SALIDA_V217_T2_CIERRE.txt`, que las midio y las sello. NINGUNA SE TECLEA.**

### 3.1. EL CICLO ENTERO DE GATE 0, LOS DOS LADOS

**CIFRA salidas selladas del ciclo: 18 | CIFRA que deberia haber: 18**
**CIFRA ausentes: 0 | CIFRA de cero bytes: 0**
**CIFRA salidas SIN exitcode dentro: 0**
**CIFRA peor exitcode de las dieciocho: 0**

**Las dos consolas existen y las sello el propio instrumento**, que es el
remedio de la `3.1` del acta 214, mantenido y sin aflojar por ninguna de sus dos
puertas.

### 3.2. EL MARCADOR, EL CENSO Y LAS SUITES

**CIFRA cifras cotejadas: 16 | CIFRA que NO calzan: 0** Las tres suites corren **solas**, fuera del ciclo, cada una con su
exitcode y sus bytes por las dos convenciones. **La tabla entera esta en la
TAREA 2 del anexo y no se repite aqui**, porque dos versiones de lo mismo es
exactamente lo que esta casa prohibe.

### 3.3. LAS SEDES, Y LA PRUEBA DE QUE ESTA VUELTA NO ESCRIBIO NI UNA FICHA

**CIFRA sedes cotejadas: 13 | CIFRA que se movieron: 0** Esa es la prueba medida de que esta vuelta **no movio ni un nodo,
ni un veredicto, ni un campo de estado**. `docs/loop/ACTA_AUDITOR.md` y
`docs/loop/PROMPT_SIGUIENTE.md`, que son sede del auditor, tambien quedan
quietas.

**Y LA MISMA PRUEBA POR LA OTRA VIA, LA QUE LA TAREA 1 EXIGIA:**

```
SHA256 DE docs/plan/OPERACIONES.jsonl AL ENTRAR: 650578474361eb2b disco y 650578474361eb2b LF
SHA256 DE docs/plan/OPERACIONES.jsonl AL SALIR: 650578474361eb2b disco y 650578474361eb2b LF
SHA256 DE docs/plan/08_VERIFICACION.md AL ENTRAR: 578eeefab6db2fd4 disco y 578eeefab6db2fd4 LF
SHA256 DE docs/plan/08_VERIFICACION.md AL SALIR: 578eeefab6db2fd4 disco y 578eeefab6db2fd4 LF
LOS CUATRO SHA COINCIDEN CON LOS DE LA ENTRADA: SI
```

### 3.4. LAS RUTAS QUE ESTE REPORTE CITA

`scripts/loop/vuelta186_rutas_del_reporte.py` se corre **DESPUES** de cerrar el
reporte, que es cuando el texto ya esta entero, y **su salida se cita en el
commit de cierre**. Va ademas **metido como guarda previa en los tres
compositores de esta vuelta**, que cuentan los guiones largos y los directorios
de dos tramos entre comillas inversas **antes de escribir**.

## 4. LO QUE SE TOCO, Y LO QUE NO

**LA CIFRA VA CON SU HUECO AL LADO, QUE ES LA OBLIGACION DE DICTADO NUEVA DEL
ENCARGO DE LA 217 Y NACE DE MI CAIDA DE LA 216:**

**CIFRA ficheros de scripts que esta vuelta escribio, MEDIDA AHORA: 7 | CIFRA de esos con el prefijo que le toca: 7**
**CIFRA MEDIDA AHORA: 7 | CIFRA DEL HUECO QUE EL PROPIO CIERRE ANADE: 4 | CIFRA TOTAL DE LA VUELTA, LAS DOS JUNTAS: 11**
**Y LOS DEL HUECO LLEVAN EL PREFIJO IGUAL: 4 de 4, contado de sus propios nombres.**

Fuera del censo y fuera de la nomina, que sigue **CONGELADA EN 135**.

**LO QUE LA APERTURA SELLADA PUBLICA, REPETIDO AQUI PORQUE UNA CIFRA AUSENTE Y
UNA CIFRA QUE CALZA NO SON LO MISMO** (guarda `D.1` de `cerrar_reporte.py`):

- **`git status --porcelain` al entrar: 1 linea(s)**, y era mi
  propio script de apertura sin rastrear. **LA CIFRA NO SE TECLEA: se lee de
  la linea `CIFRA lineas de status: 1` del sello de apertura.**
- **CIFRA filas de git diff --numstat -- dataset/ AL ENTRAR: 0**

**LO QUE ESTA VUELTA NO HIZO, DICHO PARA QUE NO SE BUSQUE:** no corrio la
bateria (la 215 la corrio y la cadencia de cinco pone la siguiente en la
**220**); **no reparo `scripts/loop/vuelta150_4_tabla_por_fase.py` aunque lo
encontro en rojo**, porque la moratoria lo prohibe; no toco el lanzador; no podo
ni engordo la nomina; no escribio en `docs/loop/PROMPT_SIGUIENTE.md` ni en
`docs/loop/ACTA_AUDITOR.md`; y **no movio ni un campo de estado**, con los
cuatro `sha256` delante.

**LA FECHA DE LA VUELTA, MEDIDA Y NO SUPUESTA:** leida de `git log` sobre el
commit de apertura y sobre el de ahora mismo.

- **fecha del commit de apertura, leida de git log: 2026-09-09**
- **fecha del commit de ahora mismo, leida de git log: 2026-09-09**

## 5. LAS PARADAS

**NO TRAIGO NINGUNA PARADA, Y LO DIGO CON EL MOTIVO DELANTE.**

**LA UNICA QUE MI ENCARGO ME MANDABA TRAER NO SE DISPARO:** su letra dice *"SI
TU INSTRUMENTO SACA OTRO NUMERO, PARAS Y LO TRAES CON LAS DOS CIFRAS
DELANTE"*, y mi instrumento saca **las mismas cuatro cifras** que el encargo, con
**CIFRA descuadres contra las cifras del encargo: 0**. No hay nada que parar ahi.

**Y LAS CINCO CLAUSULAS QUE NO LLEGAN A CUBRE TAMPOCO SON PARADA:** ninguna da
**NO CUBRE**, las cinco estan en **A MEDIAS por trabajo pendiente medido y
nombrado**, y ninguna contradice una regla vigente ni una cifra publicada con su
corte. **Lo que hay no es algo que parar: es algo que subir, y sube nombrado en
la seccion de la propuesta.**

**LO QUE SI TRAIGO, Y NO ES PARADA SINO HALLAZGO CON SU CORRIDA:**
`scripts/loop/vuelta150_4_tabla_por_fase.py`, que es el arnes que mide las ocho
filas de la tabla POR FASE, **hoy cae en rojo con exitcode 1**, y la causa esta
medida: su `assert` exige OCHO filas y la correccion declarada de la vuelta 214
dejo **ONCE**. **No lo reparo: la moratoria lo prohibe y mi encargo dice que
esta vuelta es medicion y verificacion.** La corrida vive en ``docs/loop/SALIDA_V217_T1_CONTRASTE_V150.txt``.

## 6. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**Los cinco son de la TAREA 1 y los cinco son LECTURAS MIAS de una clausula.**
Estan escritos enteros, con su duda y con lo que cambiaria si el auditor lee al
reves, en la **seccion `1.g` de la TAREA 1 del anexo**, y **no se repiten aqui a
proposito**: dos versiones de lo mismo es lo que esta casa prohibe. Sus rotulos,
para que se puedan citar: **`D.a`** la vara del ANTES de la clase, **`D.b`** que
es reubicar, **`D.c`** la anchura del detector del reparto, **`D.d`** el
universo de la clausula de las fusiones y **`D.e`** cuatro controles contra
cinco.

## 7. LAS PREGUNTAS Y LOS PENDIENTES DE DOCTRINA

**`P.1` LA CELDA DE `07 ADUANA` DICE CUATRO Y SU FASE DICE CINCO. CUAL MANDA?**
Medido hoy: la celda pide **CUATRO controles mecanicos corriendo en Gate 0**, y
**hay cuatro corriendo y los cuatro en verde**. Pero `docs/plan/07_ADUANA.md`
titula su tabla **LOS CINCO CONTROLES MECANICOS QUE LA ACOMPANAN** y la
verificacion de `OP-A-02` escribe *"los CINCO controles mecanicos corriendo"*. El
quinto, **la revision de toda nomina por el DOMINIO de sus miembros**, nacio el
13 ago 2026, **despues** de que se escribiera la celda, y **no corre**. **La
pregunta no la contesto yo:** o la celda quedo vieja y la cifra viva es cinco, o
el quinto control no es de esta celda.

**`P.2` UN ARNES QUE UNA CORRECCION DECLARADA DEJO EN ROJO, SE REPARA CUANDO?**
`scripts/loop/vuelta150_4_tabla_por_fase.py` medía las ocho filas y hoy no
arranca. **La moratoria prohibe repararlo y yo no lo he reparado.** La pregunta
es del fundador: **la auditoria integral lo autoriza, o la vara de las ocho
filas queda retirada y la sustituye la de las diecisiete clausulas de esta
vuelta.**

**PENDIENTES DE DOCTRINA: UNO, Y ES EL DE LA CLASE.** La clausula *"ningun nodo
de la clase con pasos alterados"* no dice **si protege el NUMERO de pasos o su
LETRA**. Medido hoy: por el numero, **6 de 6 quedan intactos**; por la letra,
**2 de 6 tienen texto distinto** al del grafo previo, y **ninguno de los commits
que los tocaron nombra una operacion de la fase 01**. **Registro lo mejor
sostenido, lo marco `D.a` y sigo**, que es lo que `EJECUTOR.md` 5 manda cuando
falta la regla.

## 8. MIS CAIDAS PROPIAS, CADA UNA CON SU NOMBRE Y CONTADA UNA SOLA VEZ

**ES UNA, DE MI PROPIA SONDA, CAZADA DENTRO DE ESTA MISMA VUELTA Y NO PUBLICADA
COMO CIFRA BUENA EN NINGUN SITIO.**

**`C.1` MI MUTANTE SANO DE `03 FUSIONES` NO PODIA SUBIR NUNCA.** Lo fabrique
deprecando a mano los miembros sobrantes de cada acto y anadiendolos a los
`ids_alias` del superviviente. **Un nodo vive en mas de un acto**, asi que
deprecarlo por uno rompia el otro, y la sonda medía **un desorden fabricado por
mi mutante**, no un mundo sano: salio **NO CUBRE** y con el la comprobacion
entera. **Lo cazo mi propio instrumento cayendo en rojo antes de escribir nada.**
Corregido a construir el mundo sano **sin tocar el grafo**, dejando en el
inventario los actos que ya tienen un superviviente unico, **sube a CUBRE** y la
comprobacion pasa: **4 de 4 mutantes sanos suben.** **La version vieja queda
escrita en el codigo, con su motivo, y no se borra.**

**Y UNA SEGUNDA COSA QUE NO CUENTO COMO CAIDA Y DIGO POR QUE:** mi primera
corrida publicaba la clausula `02 DESTEJIDOS` idx 1 con **un solo detector**, el
estrecho. **No era una cifra falsa** y el veredicto no cambia, pero dejaba fuera
que **cuatro fichas nombran su bloque con otras palabras**. Se anadio el
detector **ANCHO** y ahora se publican **las dos cifras**, con el veredicto
saliendo de la estrecha, que es la que no afloja la vara. **Anadir una cifra al
lado no es corregir una falsa**, y por eso va aqui abajo y no arriba.

## LO QUE PROPONGO PARA LA VUELTA SIGUIENTE

**NO PROPONGO LA PARADA FELIZ, Y LA CONDICION NO LA PUSE YO.** Mi encargo la
escribio antes de saber el resultado: *"si las DIECISIETE quedan en CUBRE con su
busqueda corrida y su cifra delante"*. **Medido hoy: 5 de 17 quedan en
A MEDIAS**, cada una con su fila, su indice y su cifra en la TAREA 1. **Por
tanto no propongo declarar la campana consumada.** Quien declara es el auditor;
yo propongo, que es lo que mi encargo manda.

**LO QUE SI DIGO, CON SU CIFRA DELANTE, PORQUE ES LO QUE LA MEDICION SOSTIENE:
NINGUNA DE LAS DIECISIETE DA NO CUBRE**, y **12 de 17 dan CUBRE**. Las
cinco que no cubren lo hacen **por trabajo del plan que no se ha ejecutado**, no
por un fallo del catalogo: **71 actos siguen sin fundir**, **7 menciones siguen
declarando un segundo libro**, y **1 de los 3 de Incoterms** quedo anotado como
trabajo post campana por adjudicacion del acta 120. **Ninguna de las tres es
maquinaria: es plan.**

**LO QUE PROPONGO, CON SU CIFRA DELANTE:**

1. **QUE LA VUELTA SIGUIENTE NO FABRIQUE NADA.** La moratoria aguanta y esta
   vuelta lo demuestra: **7 ficheros escritos en el arbol de scripts, los
   7 con su prefijo**, ninguno en el censo ni en la nomina.
2. **QUE LAS CINCO CLAUSULAS EN A MEDIAS SUBAN NOMBRADAS**, con su cifra, a la
   lista de la seccion 6 del acta, igual que subio la de `OP-I-01`.
3. **QUE EL ROJO DE `vuelta150_4_tabla_por_fase.py` SUBA NOMBRADO Y SIN
   REPARAR**, y que el fundador diga en la auditoria integral si se repara o si
   la vara de las ocho filas queda sustituida por la de las diecisiete
   clausulas.
4. **QUE LA `P.1` SE CONTESTE ANTES DE QUE NADIE TOQUE LA CELDA DE `07
   ADUANA`**, porque cambiarla sin contestarla seria reescribir una vara para
   que pase.

**Y EL MERGE NO SE PIDE: EL BUCLE NO FUNDE RAMAS.**

## 9. LA BATERIA DE MUTACIONES: HUECO DECLARADO Y MEDIDO

**HUECO DECLARADO Y MEDIDO. LA BATERIA DE LA VUELTA 217 NO CORRIO, Y EL HUECO SE DECLARA EN VEZ
DE RELLENARSE CON OTRA COSA.**

**EL NOMBRE DEL FICHERO:** `docs/loop/SALIDA_V217_BATERIA.txt`.

**CUAL DE LOS DOS CASOS ES: EL FICHERO NO EXISTE.** `os.path.exists`
devuelve NO, asi que `os.path.getsize` **no llego a correr sobre el** y no
hay ninguna medicion suya que publicar. Lo que esta seccion recibio de
bateria, medido y no supuesto, son **0 bytes en disco y 0 bytes
normalizados a LF**, **y ese cero sale de que no hay fichero, no de una
medicion sobre uno**. La distincion es del fundador, escrita el 5 sep 2026
en el punto 3 de `la-bateria-sin-techo-DECISION.md`, que nombra los dos
casos y no los confunde.

ATRIBUCION: LA CORRIO EL EJECUTOR DE LA VUELTA 215, ENTERA Y SOLA, POR SUS ONCE TRAMOS, Y EL AUDITOR LA DECLARO CORRIDA. Su salida compuesta en el arbol mide 93498 bytes en disco y 93498 bytes normalizado a LF, medidos por mi en ESTA vuelta con mi propio instrumento y no copiados del encargo, y su commit es abe21a67, leido de git log en esta misma corrida. LA 217 NO LA CORRE PORQUE LA CADENCIA DE CINCO DE AUDITOR.md 6.1 PONE LA SIGUIENTE EN LA 220, y correrla aqui seria saltarse la letra del fundador, no cumplirla.

**POR QUE ESTO CIERRA Y UNA AUSENCIA MUDA NO.** La pieza (4) de este
instrumento admite el hueco declarado desde la vuelta 173, TAREA 1.b
(adjudicacion 6.2 del acta del auditor de la vuelta 172), y la letra es
estrecha: **el nombre, los bytes medidos y la atribucion, LAS TRES JUNTAS**.
Faltando cualquiera de las tres, este instrumento sigue cayendo en ROJO, y
**una corrida de otra vuelta pegada aqui tampoco vale**.
