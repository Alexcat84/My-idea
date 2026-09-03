# REPORTE DE LA VUELTA 159 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

**EL VEREDICTO DE UNA LINEA: LAS NUEVE TAREAS ENTREGADAS, EL SACO DE LECTURA
QUEDA VACIO (18 EN C Y LAS 18 LEIDAS), EL AUDITOR ACIERTA EN LAS TRES EN DISPUTA
Y LA SEGUNDA PASADA ENCUENTRA UNA CUARTA DE LA MISMA ESPECIE. HAY UNA PARADA, LA
DE LA TAREA 5, Y ES POR MANDATO LITERAL DEL ENCARGO: EL ALCANCE DEL CHECK DE
P.16 NO DA ONCE, DA DOCE.** Y traigo cuatro caidas propias, las cuatro cazadas
por una guarda o por mi propio instrumento antes de publicar, todas declaradas
en la seccion 1.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

Todo lo de esta seccion sale de
`scripts/loop/tallar_cabecera_reporte.py --vuelta 159 --fase04`, salida
`docs/loop/SALIDA_V159_T9_CABECERA.txt`, pegada entera.

<!-- CABECERA TALLADA -->
| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| censo: nodos / vivos / deprecados | 3.853 / 3.169 / 684 | **3.853 / 3.169 / 684** |
| Gate 0: veredicto, auto-aristas, duplicadas de titulo, divergentes | OK (auto-aristas 0, duplicadas 0, divergentes 0) | **OK (auto-aristas 0, duplicadas 0, divergentes 0)** |
| aristas: `nodos_siguientes` / `nodos_previos` / suma / union | 8.780 / 8.740 / 17.520 / 9.914 | **8.780 / 8.740 / 17.520 / 9.914** |
| motor | 25/25 | **25/25** |
| web: ficheros / tests | 80 passed (80) / 1.030 passed, 3 skipped (1.033) | **80 passed (80) / 1.030 passed, 3 skipped (1.033)** |
| tsc | EXITCODE 0, cero lineas | **EXITCODE 0, cero lineas** |
| aristas movidas en la vuelta (cierre menos apertura): `nodos_siguientes` / `nodos_previos` / suma / union | (no aplica: la celda de cierre es la resta contra esta apertura) | **+0 / +0 / +0 / +0** |
| desfase del calibrado rastreado (`PASO_NODO_CALIBRADO.jsonl` distinto del grafo) | 4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente` | **4 fila(s): `dia_cero_defectos_2 -> eliminacion_causas_error_4`, `customer_validation -> establecer_linea_base_mvp`, `dia_cero_defectos_3 -> eliminacion_causas_error_4`, `ganar_comprension_del_cliente -> dia_en_la_vida_del_cliente`** |
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `3ad70158` (asunto real leido de git log: 'ACTA DE LA VUELTA 158 DEL AUDITOR: EL CIERRE REPRODUCE AL DIGITO Y LA PARADA NO ES PARADA, ES ARITMETICA DE INDICE (ACTA N, VUELTA N MAS 1). PERO LA CIEGA DA UNA DISCREPANCIA FUERA DE LO MARCADO, LD-OPC05-005: BAJA EL CREDITO Y EL TRAMO SE RELEE AL DOBLE.'), HEAD real de apertura `3ad70158` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `48a707d1` (leido de `SALIDA_V159_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |
<!-- FIN CABECERA TALLADA -->

**Y EL SELLO DE APERTURA LLEGO A TIEMPO, QUE ES LA 6.2 DEL ACTA 158 CUMPLIDA.**
Los diez `SALIDA_V159_*_APERTURA.txt` nacieron TODOS en `9a0ae9d7`, el PRIMER
commit del corredor e hijo directo del acta `3ad70158`. Corrido con
`scripts/loop/verificar_apertura_sellada.py --vuelta 159`, salida
`docs/loop/SALIDA_V159_T0_APERTURA_SELLADA.txt`: **VERDE exit 0**, y ademas lee
del commit del acta el rotulo de hashes admitidos y computa **0 (ninguno)**. La
guarda desbloqueada muerde, como el acta anticipo.

| | valor | de donde sale |
|---|---|---|
| rama | `pasada-unica` | `git rev-parse --abbrev-ref HEAD` |
| commit de apertura | `3ad70158` | `docs/loop/SALIDA_V159_HEAD_APERTURA.txt` |
| commit de cierre (antes del commit del reporte) | `48a707d1` | `docs/loop/SALIDA_V159_HEAD_CIERRE.txt` |
| commits del corredor | 10 | `git rev-list --count 3ad70158..HEAD` |
| intrusos en el corredor | 0 | los 10 son mios: 1 de apertura y 9 de tarea |
| hashes admitidos | 0 (ninguno) | leido del commit del acta por la guarda |

## 1. MIS CAIDAS, LAS CUATRO, Y VAN ANTES QUE LO DEMAS

**CAIDA 1, DE PROCEDIMIENTO, CAZADA POR LA GUARDA DEL COMMIT.** En la TAREA 2.b
corri `scripts/run_phase1.py --reaplico-curaduria` **SUELTO** para el Gate 0 que
la 2.d exige, y el EJECUTOR dice NUNCA `run_phase1` suelto. La guarda del commit
salio ROJO con **setenta y un nodos divergentes** en `etiqueta_arbol` y me mando el ciclo
entero. **No la esquive:** corri `etiquetas_de_cara --aplicar` (71 etiquetas) y
`sync_assets_web`, y el commit paso. La regla existia, la guarda existia, y la
que fallo fue mi mano.

**CAIDA 2, DE INSTRUMENTO, EN LA TAREA 1: EL BUSCADOR SE CONTABA A SI MISMO.**
La primera corrida de `vuelta159_tarea1_registrar_adjudicaciones.py` publico
**TRECE** ficheros con el patron de P.16. El decimotercero era **el propio
fichero**, que contiene el patron porque tiene que escribirlo para buscarlo. Es
la misma trampa que `verificar_apertura_sellada.py` lleva escrita desde la
vuelta 102. **Revertí el arbol entero, arregle la exclusion, la declare en la
funcion y re corri.** La cifra publicada es la de la segunda corrida: **12**.

**CAIDA 3, DE INSTRUMENTO, EN LA TAREA 7, Y ES LA MAS UTIL.** Mi primera version
del buscador de productores publico las DOS salidas como **ARTEFACTO HUERFANO**,
con "CIFRA sujetos con productor hallado: 0". **Era falso.** Los tres angulos que
corri (nombre del fichero, texto literal, y los `.py` de los commits) son todos
busquedas sobre TEXTO YA INTERPOLADO, y ningun productor que interpola puede
casar con ellas. Con el cuarto angulo, el de la CABECERA LITERAL, **aparecen los
dos**. La cifra vieja queda escrita en el docstring del instrumento.

**CAIDA 4, DE INSTRUMENTO, EN LA TAREA 8.** Mi diagnostico conto `takt_time` y
`smed_setup_reduction` como "nodos sin explicar" del sujeto 97 y por eso lo
declaro HALLAZGO. **Esos dos no son un sintoma: son el nodo ajeno que la
MUTACION 3 inyecta a proposito.** Contar la mutacion como sintoma es leer la
prueba al reves. Con el corte declarado, los dos sujetos salen CASO DECLARADO y
cero sin explicar.

## 2. LA PARADA, Y VA PRONTO PORQUE ES UNA TAREA ENTERA QUE NO SE EJECUTA

**TAREA 5, EL ALCANCE DEL CHECK DE P.16.** El encargo dice, literal: *"once
ficheros de scripts/loop/ llevan el patron literal, siete de ellos dentro de la
bateria de las 23. Si tu cuenta no da once, paras y lo dices."*

Recomputado con `scripts/loop/vuelta159_tarea5_alcance_p16.py`, salida
`docs/loop/SALIDA_V159_T5_ALCANCE.txt`, bajo TRES lecturas distintas de "el
patron literal" y con los dos buscadores excluidos por nombre y declarados:

```
CIFRA mutaciones en la nomina de la bateria: 23
   A ESTRECHA (dataset/ Y docs/plan/)          CIFRA ficheros: 4    en la bateria: 3
   B MEDIA (pathspec que empieza por dataset/) CIFRA ficheros: 12   en la bateria: 7
   C ANCHA (cualquier git status --porcelain)  CIFRA ficheros: 14   en la bateria: 7
   CIFRA que el acta declara, ficheros: 11
   CIFRA que el acta declara, dentro de la bateria: 7
   LOS SIETE DE LA BATERIA REPRODUCEN AL DIGITO.
   LA CIFRA DE FICHEROS NO REPRODUCE: sale 12 y el acta dice 11.
   EL RESIDUO SE PUEDE NOMBRAR, Y ES UNO SOLO: vuelta89_tarea4_guarda_op_c05.py
   Quitandolo, la cuenta da 11, que es exactamente la del acta.
```

**LOS SIETE DE LA BATERIA REPRODUCEN AL DIGITO Y EL RESIDUO TIENE NOMBRE.** Esa
es la parte util: no es que las dos cuentas midan cosas distintas, es que la mia
trae UNO MAS, y ese uno es `scripts/loop/vuelta89_tarea4_guarda_op_c05.py`, el
unico de la nomina que no es de la serie 142 a 147. **PARO Y NO TOCO UN SOLO
CHECK:** el remedio de la 5.a y el caso positivo de la 5.c NO SE EJECUTAN. Una
guarda reescrita con el alcance mal contado es peor que la que se deja.

## 3. TAREA 1, LAS DOCE ADJUDICACIONES DEL ACTA 158

Salida `docs/loop/SALIDA_V159_T1_ADJUDICACIONES.txt`.

```
CIFRA operaciones de escritura de esta corrida: 33
CIFRA de ellas ANADIDAS: 32
CIFRA de ellas YA ESTABAN: 1
CIFRA ficheros .py tocados: 20
CIFRA borrados en los .py tocados: 0
CIFRA razones cuyo texto viejo YA NO ES PREFIJO: 0
CIFRA clases movidas por esta tarea: 0
```

**LA ADITIVIDAD SE MIDIO, NO SE PROMETIO:** `git diff --numstat` sobre los 20
`.py`, **cero borrados**; assert de prefijo sobre **las 154** entradas del
JSONL, **cero prefijos rotos**; y assert de que esta tarea no mueve ninguna
clase, **cero**.

**DONDE FUE CADA UNA, Y DOS PRECISIONES DECLARADAS.** 6.1 y 6.2 en
`verificar_apertura_sellada.py` y `tallar_cabecera_reporte.py`; 6.3 en
`vuelta152_registro_de_citas_opc05.py` y en el instrumento del lote; 6.4 y 6.5
en las razones de `LD-OPC05-005`, `027` y `122`; 6.6 en los TRES instrumentos
que escriben el campo `cita` (nace en el de la 152, y las dos formas divergentes
las escribieron el de la 156 y el de la 157); 6.7 en los 12 medidos; 6.8 en
`verificar_re_sellado.py`; 6.9 y 6.10 en la funcion de la P3b; 6.11 en el
instrumento de la TAREA 8 de la 157; 6.12 en el instrumento del lote.
**PRECISION 1:** el instrumento del lote 2 no existia cuando la TAREA 1 corrio,
asi que la 6.3 y la 6.12 van en el del lote 1, que es el que la 6.3 corrige, y
el del lote 2 nace con las dos en su propio docstring. **PRECISION 2:** la 6.7
se escribio en los 12 MEDIDOS y no en once tecleados.

## 4. TAREA 2, LA BLOQUEANTE. LAS TRES EN DISPUTA Y EL TRAMO AL DOBLE

### 4.1 Las tres en disputa: EL AUDITOR ACIERTA EN LAS TRES

Leidas contra los nodos con `docs/loop/SALIDA_V159_T2A_DOSSIER.txt`. Veredictos
en `docs/loop/SALIDA_V159_T2A_VEREDICTOS.txt`.

```
LD-OPC05-005     D -> C
LD-OPC05-027     C -> D
LD-OPC05-122     C -> D
CIFRA lecturas dirigidas por clase: {"C": 56, "D": 66}
```

**LA 005 VUELVE A C Y ES CAIDA MIA DE LA VUELTA 157, NO DEL AUDITOR.** El par que
la 157 tomo (paso 1 de `aim_of_leadership` contra paso 13 de
`causas_comunes_vs_especiales`) SI colapsa, y en eso tenia razon. Lo que hizo mal
fue creer que descartar UN par descarta la figura. **Hay otro par y sostiene la
C:** paso 2 de aim (investigar las causas de raiz DEL SISTEMA), expandido por los
quince pasos de causas; y paso 13 de causas (dar seguimiento y apoyo a quienes
caen fuera de las tolerancias), expandido por los pasos 1, 3 y 5 de aim. Dos
lineas distintas, una en cada nodo.

**LA 027 BAJA A D:** la ida se sostiene (paso 1 de SPIN, expandido por los pasos
1 a 3 de cierre), la vuelta no. Recorrido el espacio entero, **ninguna linea de
`cierre_segun_complejidad_venta` esta expandida por un procedimiento de
`metodologia_spin_selling`**: sus cuatro pasos son diagnostico, decision,
remision y cifra. El par mas fuerte descartado queda nombrado en la razon.

**LA 122 BAJA A D, Y ESO REVOCA DOS ADJUDICACIONES QUE LA SOSTUVIERON** (la 6.4
del acta 155 y mi propia lectura del lote 1). El paso 6 de 6S es SAFETY,
seguridad ocupacional, y `error_proofing_servicio` es prevencion de ERROR en
procesos de servicio: materia distinta.

### 4.2 El tramo al doble: la nomina de 41 REPRODUCE AL DIGITO

`docs/loop/SALIDA_V159_T2B_NOMINA.txt`, recomputada de cuatro ficheros del repo
(la nomina sellada del lote 1 y las dos ciegas selladas del auditor):

```
CIFRA del lote 1 que CAYERON A D: 62
CIFRA de las caidas a D que la ciega de la 158 releyo: 15
CIFRA de las caidas a D que la ciega anterior leyo: 6
CIFRA solapadas entre las dos ciegas: 0
62 menos 21 da 41
```

Y el resultado de las 41 segundas lecturas
(`docs/loop/SALIDA_V159_T2B_VEREDICTOS.txt`):

```
CIFRA con la clase movida en esta tarea: 1
CIFRA que sostienen su clase en esta tarea: 40
CIFRA lecturas dirigidas por clase: {"C": 57, "D": 65}
```

**LA SEGUNDA PASADA NO FUE UN TRAMITE: ENCONTRO UNA CUARTA DE LA MISMA ESPECIE
QUE LA 005.** `LD-OPC05-052` vuelve a C. Linea 1: paso 3 de
`definicion_alineacion_cadena_suministro` (definir si tu estrategia es precio
bajo o servicio), expandido por los pasos 1, 2, 3 y 7 de `trade_off`. Linea 2:
paso 1 de `trade_off` (analizar que valora tu segmento), expandido por el paso 8
de alineacion, que es un instrumento nombrado de seis dimensiones (las 6
preguntas de Chopra y Meindl). El par que SI colapsa, y que por eso se descarta,
es el paso 3 de trade_off contra el paso 4 de alineacion.

**Y LA 6.3 SE APLICO EN LAS 41 SIN EXCEPCION:** cada una de las 41 razones nombra
EL PAR MAS FUERTE QUE SE DESCARTO y dice por que no sostiene la figura.

### 4.3 Las guardas de la 2.d, medidas en las dos tareas

```
sha256 de dataset/ ANTES y DESPUES: 1330ccb9c46c03d371cb1ecf7911c83bbb4b14db71a878b3405738000c90e9d8 (identico)
censo ANTES y DESPUES identico: nodos 3853, vivos 3169, deprecados 684
aristas ANTES y DESPUES identico: siguientes 8780, previos 8740
CIFRA n, veredictos del cribado: 3388 antes y 3388 despues
CIFRA razones cuyo texto viejo YA NO ES PREFIJO: 0
NINGUNA SE MUEVE A A
```

Y Gate 0 al terminar el tramo: **26 en OK y 0 en fallo**
(`docs/loop/SALIDA_V159_T2_CONTEO_GATE0.txt`), con el ciclo entero detras.

## 5. TAREA 3, EL LOTE 2 ENTERO. CABE, Y NO SE PARTE

Nomina recomputada (`docs/loop/SALIDA_V159_T3_NOMINA.txt`): **53**, de
`LD-OPC05-068` a `LD-OPC05-121`, **CIFRA del lote 2 CON puntero de paso: 0**, y
las 4 C que quedan fuera del rango son las ya leidas (038 y 049 sostuvieron C en
el lote 1; 005 y 052 volvieron a C hoy). Veredictos en
`docs/loop/SALIDA_V159_T3_VEREDICTOS.txt`:

```
CIFRA con la clase movida en esta tarea: 39
CIFRA que sostienen su clase en esta tarea: 14
CIFRA lecturas dirigidas por clase: {"C": 18, "D": 104}
```

**UN CRITERIO QUE ESTE LOTE OBLIGO A ESCRIBIR Y QUE DECLARO PARA QUE SE PUEDA
AUDITAR SU CONSISTENCIA: UNA INSTANCIA NO ES EL PROCEDIMIENTO DE SU CATEGORIA.**
Cuando la linea dice "aplica tecnicas graficas", "mapea tus fuentes de ingresos"
o "consolida los planes subsidiarios", y el otro nodo ES UNA de esas tecnicas,
uno de esos patrones o uno de esos planes, eso es un ejemplar y no una
expansion. Se aplico en la 060, la 078, la 099, la 103, la 106, la 107, la 113 y
la 117, **y en ninguna se hizo la excepcion comoda**: en la 078 y la 103 el
criterio es lo unico que las manda a D, y por eso las dos van marcadas.

**EL SACO DE LECTURA QUEDA VACIO.** De las 122 lecturas dirigidas, 104 estan en
D y **las 18 que siguen en C estan todas leidas**. No queda ninguna sin mirar.

## 6. TAREA 4, EL CAMPO `cita` UNIFICADO. Y NO SON 65, SON 106

Salida `docs/loop/SALIDA_V159_T4_CITAS.txt`.

```
CIFRA commits que tocan el registro (git log): 12
CIFRA filas con AL MENOS UN cambio de clase en la historia: 106
CIFRA cambios de clase por vuelta: {"156": 3, "157": 62, "159": 43}
CIFRA filas que NO son lecturas dirigidas y quedan intactas: 32
CIFRA filas donde el ultimo token del .md NO es la clase vigente: 0
CIFRA citas reescritas en esta corrida: 106
CIFRA citas que ya estaban en la forma unica: 16
CIFRA citas por forma: {"con rastro": 106, "sin rastro": 16}
CIFRA citas que siguen en la forma vieja de la vuelta 156: 0
CIFRA clases movidas por esta tarea: 0
CIFRA pares antes: 154, CIFRA pares despues: 154
CIFRA razones cuyo texto viejo YA NO ES PREFIJO: 0
```

**LA CIFRA DEL ACTA ERA 65 Y HOY SON 106, Y NO ES UNA DISCREPANCIA: ES QUE LAS
TAREAS 2 Y 3 DE ESTA MISMA VUELTA MOVIERON 43 CLASES MAS.** 3 de la 156 mas 62
de la 157 mas 43 de la 159 dan 108 cambios sobre 106 citas, porque dos de ellas
cambiaron dos veces (`005` y `052`).

**LA HISTORIA SE RECONSTRUYO DE GIT, NO DE LA PROSA, Y HAY MOTIVO.** Las razones
de la vuelta 156 NO usan la formula "LA CLASE PASA DE X A Y" que usan la 157 y la
159, asi que una vara lexica sobre la razon habria quedado ciega justo en las
tres filas que la 6.6 nombra. Se leyeron los 12 commits del registro y se anoto
la clase commit a commit. La celda tachada del `.md` se uso como CONTRASTE
independiente: **0 desacuerdos en las 122**.

**LA ADICION VA EN LA RAZON, NO EN LA CITA, Y SE DICE POR QUE:** el campo `cita`
es corto y no admite apendices sin volverse ilegible, asi que lo que se anade es
un bloque en la `razon` que escribe QUE DECIA la cita antes y QUE DICE ahora. El
assert de prefijo lo comprueba sobre las 154.

## 7. TAREA 6, LA GUARDA DE RE SELLADO YA NO ACUSA A SU PROPIA SALIDA

Corrida sobre el reporte de HEAD (`docs/loop/SALIDA_V159_T6_RE_SELLADO_HEAD.txt`):

```
CIFRA por estado: RE SELLADO 3, SIN RE SELLAR 34
CIFRA salidas EXENTAS por construccion: 2
CIFRA de esas exentas que ademas estan RE SELLADAS: 2
CIFRA re selladas SIN declarar en el reporte: 0
```

**LA EXENCION SE IMPRIME CON NOMBRES, QUE ES LO QUE LA 6.8 EXIGE**, y no calla al
fichero exento: lo sigue analizando y publicando su numstat. La linea completa,
con los dos nombres y sus numstat, vive entera en la salida citada arriba; aqui
se dice cuales son, que son las dos que el auditor nombro en la seccion 5.2 del
acta 158: la del verificador de cifras y la de esta misma guarda sobre el
reporte final. **Y EL CASO POSITIVO
POR MUTACION MUERDE** (`docs/loop/SALIDA_V159_T6C_MUTACION_EXENCION.txt`): un
fichero de tarea NORMAL re sellado y no declarado
(`SALIDA_V106_CABECERA_TALLADA.txt`, elegido por computo) deja **una fila sin
declarar**. Con `--mutar`, que exige 0, **el caso CAE con exit 1**
(`docs/loop/SALIDA_V159_T6C_MUTACION_EXENCION_MUTADO.txt`), o sea que el caso
rojo no se aprueba solo. La mutacion vieja de la 157 sigue **VERDE exit 0**
(`docs/loop/SALIDA_V159_T6_MUTACION_157.txt`): no hay regresion.

**Y UN RE SELLADO DECLARADO, PORQUE ESTE REPORTE CITA EL FICHERO QUE EL CASO
POSITIVO ELIGIO POR COMPUTO.** La guarda lo computa y aqui va su linea, literal:

RE SELLADO DECLARADO: SALIDA_V106_CABECERA_TALLADA.txt numstat +1/-1, lineas CIFRA con valor cambiado: 0 (ninguna)

Ese fichero cambio despues del commit de su tarea (`d2aa753c`), y no lo toco esta
vuelta: lo cita este reporte porque el caso positivo de la 6.c lo eligio
recorriendo `docs/loop/` en orden hasta dar con el primer RE SELLADO no exento.
Su unica linea movida no es una linea `CIFRA`.

**Y UNA CORRECCION DE MI PROPIA CONSTRUCCION, DENTRO DE LA MISMA TAREA:** la
primera version del patron eximia tambien a
`SALIDA_V157_T6B_MUTACION_RE_SELLADO.txt`, que no es la salida de la guarda sobre
el reporte final sino la de su prueba. Hoy ese fichero esta SIN RE SELLAR y no
cambiaba ningun veredicto, **pero una exencion mas ancha que su motivo es un
agujero esperando**. Se estrecho descartando la palabra `MUTACION`, ya reservada
en esta casa desde la vuelta 102.

## 8. TAREA 7, LAS DOS SALIDAS NO ERAN HUERFANAS

Salida `docs/loop/SALIDA_V159_T7_PRODUCTORES.txt`.

```
SALIDA_V108_TAREA2_3_CASO_POSITIVO.txt   PRODUCTOR HALLADO: scripts/loop/verificar_cobertura_bolsa_tres_vias.py
SALIDA_V136_3D_MUTACION.txt              PRODUCTOR HALLADO: scripts/loop/verificar_fuente_canonico.py
CIFRA sujetos con productor hallado: 2
CIFRA sujetos declarados ARTEFACTO HUERFANO: 0
```

**LOS DOS PRODUCTORES ESTAN VIVOS EN HEAD, Y LA RAZON DE QUE NADIE LOS HALLARA ES
LA MISMA PARA LOS DOS: IMPRIMEN POR STDOUT Y EL `.txt` ES UNA REDIRECCION DE
SHELL.** Por eso ningun `.py` contiene el NOMBRE del fichero, que es lo que el
barrido de 998 `.py` de la vuelta 157 buscaba, y por eso tampoco contiene su
TEXTO LITERAL: en el fuente ese texto va con marcadores de formato
(`"FICHEROS DE ENTRADA (declarados en FICHEROS_VEREDICTO, %d):"`). Buscar la
linea ya interpolada no puede casar nunca. El angulo que caza es el de la
CABECERA LITERAL: prefijos cada vez mas cortos hasta que uno case. El primero
cubre **5 de 5** lineas casables; el segundo, **1 de 1**.

**LA MARCA QUEDO ESCRITA JUNTO A LA FUNCION DE LA P3b**
(`docs/loop/SALIDA_V159_T7B_MARCA.txt`): **CIFRA lineas anadidas: 35**, **CIFRA
lineas borradas: 0**. Y la regla de productor tambien se corrigio dentro de la
misma corrida: pedia `cuantas >= 2`, que es falso para un fichero de una sola
linea; la regla buena es dar cuenta de TODAS las lineas que casaron.

## 9. TAREA 8, EL ROJO DE LAS DOS QUE NO MUERDEN, LEIDO ANTES DE TOCAR NADA

Salida `docs/loop/SALIDA_V159_T8_DIAGNOSTICO.txt`.

```
vuelta96_tarea3_prueba_mutacion.py    exit 1
    CASO DECLARADO: EXPECTATIVA ENVEJECIDA SOBRE SUJETO CONGELADO
    mutaciones que caen: 6 | nodos deprecados en fallos: 3 | sin explicar: 0
vuelta97_tarea2_prueba_mutacion.py    exit 1
    CASO DECLARADO: EXPECTATIVA ENVEJECIDA SOBRE SUJETO CONGELADO
    mutaciones que caen: 6 | nodos deprecados en fallos: 3 | sin explicar: 0
CIFRA sujetos con CASO DECLARADO: 2
CIFRA sujetos que quedan como HALLAZGO: 0
```

**EL DIAGNOSTICO ES EL MISMO PARA LAS DOS: EL SUJETO ESTA CONGELADO Y EL GRAFO SE
MOVIO.** Las tablas de veredicto de las vueltas 96 y 97 nombran los ids que los
nodos tenian entonces; despues, en las mesas de fusion, esos nodos quedaron
DEPRECADOS y el resolutor los manda a su superviviente, asi que el check compara
el nombre viejo contra el nuevo. Los nodos implicados
(`get_out_of_the_building`, `customer_discovery_overview`,
`estrategia_de_innovacion_de_producto`, `requisitos_gates_con_dientes`) estan
**todos deprecados** y **todos en `docs/plan/03_FUSIONES.md`**.

**LAS DOS PRUEBAS DE QUE NO ES REGRESION:** las **6 mutaciones de cada una siguen
cayendo**, y **cero nodos sin explicar por fusion**.

**LO QUE NO HICE, Y ES LA PROHIBICION LITERAL DE LA 6.10: no ajuste ninguna
expectativa, no retoque ninguna tabla congelada, y LAS DOS SIGUEN SALIENDO exit 1
DESPUES DE DECLARARLAS** (`docs/loop/SALIDA_V159_T8B_DECLARACION.txt`, que las
vuelve a correr para probarlo). Un caso declarado no apaga un rojo: lo explica y
lo ata a una MARCA OBLIGATORIA, para que el dia que fallen por otra razon la
marca no aparezca y el rojo vuelva a contar.

## 10. TAREA 9, EL CIERRE RECOMPUTADO AL CIERRE

**EL CICLO ENTERO Y EN SU ORDEN, NUNCA `run_phase1` SUELTO:**
`--reaplico-curaduria` (`docs/loop/SALIDA_V159_GATE0_CMD1_CIERRE.txt`,
**GATE 0: OK**), `etiquetas_de_cara --aplicar`
(`docs/loop/SALIDA_V159_CICLO_ETIQUETAS_CIERRE.txt`, **71 etiquetas**),
`sync_assets_web` (`docs/loop/SALIDA_V159_CICLO_SYNC_CIERRE.txt`, **seis
assets**) y despues el `numstat`
(`docs/loop/SALIDA_V159_CICLO_NUMSTAT_CIERRE.txt`, **cero filas**).

**EL MARCADOR, EL CENSO Y EL REGISTRO, RECOMPUTADOS AL CIERRE**
(`docs/loop/SALIDA_V159_T9_MARCADOR_CIERRE.txt`):

```
CIFRA n, filas del archivo: 3388
CIFRA marcador clase A: 551
CIFRA marcador clase B: 72
CIFRA marcador clase C: 5
CIFRA marcador clase D: 2760
CIFRA puestos distintos: 3388
CIFRA huecos: 0
CIFRA duplicados: 0
CIFRA nodos: 3853
CIFRA vivos: 3169
CIFRA deprecados: 684
CIFRA aristas nodos_siguientes: 8780
CIFRA aristas nodos_previos: 8740
CIFRA suma de las dos vistas: 17520
CIFRA union DIRIGIDA de las dos vistas: 9914
CIFRA solo en nodos_siguientes: 1174
CIFRA solo en nodos_previos: 1134
CIFRA auto enlaces: 0
CIFRA filas del registro de citas: 154
CIFRA registro CRIBADO clase B: 1
CIFRA registro CRIBADO clase D: 31
CIFRA registro LECTURA_DIRIGIDA clase C: 18
CIFRA registro LECTURA_DIRIGIDA clase D: 104
CIFRA citas de lectura dirigida: 122
CIFRA citas con rastro de correccion: 106
CIFRA citas en la forma vieja de la vuelta 156: 0
```

**Y ESTE INSTRUMENTO NACE HOY POR UN MOTIVO QUE VIENE DE LA TAREA 7:** la salida
`SALIDA_V157_T9_MARCADOR_CIERRE.txt` existe pero NINGUN `.py` del repo la
produce (buscado por su cabecera literal sobre `scripts/loop/*.py`: cero
resultados). Era un instrumento de un solo uso. `vuelta159_tarea9_marcador_cierre.py`
se escribe y se commitea con nombre estable para que esa cifra tenga siempre un
productor vivo.

**LAS TRES SUITES:** motor **25/25** (`SALIDA_V159_MOTOR_CIERRE.txt`), vitest
DESDE `web/` con **Test Files 80 passed (80)** y **Tests 1.030 passed, 3
skipped**
(`SALIDA_V159_WEB_CIERRE.txt`), `tsc --noEmit` con **EXIT=0 y cero lineas**
(`SALIDA_V159_TSC_CIERRE.txt`).

**EL EXPEDIENTE, CORRIDO CON EL CORTE DE APERTURA**, y las cuatro fases con
`scripts/loop/tallar_estado_de_fase.py`. Cada cifra lleva al lado el fichero del
que sale:

De `SALIDA_V159_T9_EXPEDIENTE.txt`, CIFRA fichas del expediente: 71 operaciones.
Y de esa misma salida salen las otras cinco, que escribo con el numero detras del
rotulo para que ninguna se pueda confundir con la vecina al cotejarla: fichas que
no calzan 36, fichas congeladas declaradas 24, fichas congeladas en silencio 12,
fichas HECHA sin ninguna prueba 0, fichas en LISTA sin ninguna prueba 7. El
reparto es el mismo que el auditor midio en la vuelta 158, sin una desviacion.

**LAS CUATRO FASES, CADA UNA DE SU TALLADOR.** La fase 03_FUSIONES cierra segun
`SALIDA_V159_T9_FASE_03_FUSIONES.txt` con 16 del catalogo, 12 cumplidas y 4 sin
cumplir (OP-M-02-ADMIT, OP-M-02-MEDIOS, OP-U-01 y OP-U-02). La fase 06_MESAS
cierra segun `SALIDA_V159_T9_FASE_06_MESAS.txt` con 16 del catalogo, 16
cumplidas y 0 sin cumplir. La fase 08_VERIFICACION cierra segun
`SALIDA_V159_T9_FASE_08_VERIFICACION.txt` con 1 del catalogo, 0 cumplidas y 1
sin cumplir, que es OP-V-01, sin vara escrita. La fase 09_LECTURAS_DIRIGIDAS
cierra segun `SALIDA_V159_T9_FASE_09_LECTURAS_DIRIGIDAS.txt` con 3 del catalogo,
0 cumplidas y 3 sin cumplir, que son OP-L-01, OP-L-02 y OP-L-03.

**LAS GUARDAS DEL CIERRE, CON SU ESTADO REAL:**

  - `verificar_apertura_sellada.py --vuelta 159`: **VERDE exit 0**, los diez
    ficheros de apertura nacidos en el primer commit
    (`SALIDA_V159_T9_APERTURA_SELLADA.txt`).
  - `verificar_mutaciones_viejas.py`, **SOLA y sin nada al lado**: **VERDE exit
    0**, 23 mutaciones, **0 ancla perdida, 0 no mordio, 0 no reproducible, 2
    casos declarados, RUIDO DE CONCURRENCIA 0** (`SALIDA_V159_T9_BATERIA.txt`).
  - `tallar_cabecera_reporte.py --vuelta 159 --fase04`: **corre y talla**, que es
    la 6.1 del acta 158 cumplida (`SALIDA_V159_T9_CABECERA.txt`).
  - `tallar_cabecera_reporte.py --comparar docs/loop/REPORTE.md`: **CABECERA
    IDENTICA AL TALLADOR**, con nueve filas cotejadas, cero distintas y cero
    ausentes
    (`SALIDA_V159_T9_CABECERA_COMPARADA.txt`).
  - `verificar_cifras_del_reporte.py --reporte docs/loop/REPORTE.md`: **VERDE
    exit 0**, con 6 afirmaciones de CIERRE cotejadas contra
    `tallar_estado_de_fase.py` (`SALIDA_V159_T9_CIFRAS_REPORTE.txt`). **Y DIGO
    SU LIMITE EN VEZ DE VENDER EL VERDE:** su cobertura de cifras es de UNA, y
    lo es porque casi todo lo que este reporte publica va pegado dentro de
    bloques de salida, donde la unidad va detras del rotulo y no detras del
    numero. Un verde sobre una cifra es un verde estrecho.
  - `verificar_re_sellado.py --reporte docs/loop/REPORTE.md`: **VERDE exit 0**,
    con **CIFRA re selladas SIN declarar en el reporte: 0** y la exencion de la
    6.8 impresa con sus dos nombres (`SALIDA_V159_T9_RE_SELLADO.txt`). Es la
    primera vuelta en que esta guarda puede salir verde sobre su propio reporte,
    que es justo lo que la 6.8 encargo.

## 11. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

Son **doce**, y los marco con su motivo para la relectura ciega del auditor.

**LOS DEL TRAMO RELEIDO AL DOBLE (TAREA 2.b), SIETE:**

  1. **`LD-OPC05-052`**, y es el mas fuerte porque **mueve una clase de D a C**.
     La ida es solida; lo que me hace dudar es si el paso 1 de `trade_off`
     (analizar que valora tu segmento) y el paso 3 de alineacion (definir tu
     estrategia competitiva) son **dos lineas o una sola vista dos veces**. Yo
     leo dos (una mide el mercado, la otra decide tu postura). Si el auditor lee
     una, colapsa por el 9.22 y vuelve a D.
  2. **`LD-OPC05-018`**, el caso mas cerrado del tramo. Descarto la vuelta porque
     el paso 4 de `scenarios` formula las preguntas por bloque **para cada
     escenario** y no para los hallazgos del entorno. Si el auditor lee que el
     insumo no importa, la 018 sube a C.
  3. **`LD-OPC05-042`**, y la marco por segunda vez en su historia. Descarto la
     vuelta por el mismo motivo de insumo (la rejilla decide desde la ETAPA DE
     MADUREZ, no desde el resultado del COPQ).
  4. **`LD-OPC05-004`**: descarto reempaquetado como el como del tune-up porque
     lo leo como REMEDIO HERMANO (contesta que cambiar, no como revisar).
  5. **`LD-OPC05-039`**: descarto la vuelta porque el criterio de definiciones es
     para la CARACTERISTICA DE CALIDAD y el del control estadistico para la
     REPRODUCIBILIDAD DEL METODO. Objetos distintos, y al mismo nivel.
  6. **`LD-OPC05-063`**: leo que las dos direcciones caen sobre la misma linea
     (cuando presentar la solucion). Si el auditor separa el criterio del
     procedimiento, sube a C.
  7. **`LD-OPC05-066`**: descarto la vuelta por MODO DE FALLO (los dos pasos de
     `el_riesgo_eres_tu` contestan al fundador ausente, no al resto en crisis).

**LOS DEL LOTE 2 (TAREA 3), CINCO:**

  8. **`LD-OPC05-078`** y 9. **`LD-OPC05-103`**: las dos caen a D **solo por el
     criterio de instancia**, no por una evidencia. Si el auditor no acepta que
     un ejemplar no expande su categoria, las dos suben a C, y con ellas habria
     que revisar la 060, la 099, la 106, la 107, la 113 y la 117.
  10. **`LD-OPC05-081`**: la sostengo en C, y dudo porque los dos nodos son del
      mismo libro y corren muy en paralelo; el riesgo es que la clasificacion en
      tres escenarios y el periodo de monitoreo sean la misma linea.
  11. **`LD-OPC05-084`**: la sostengo en C, y dudo porque la segunda direccion es
      un METODO DE VALIDACION (salir del edificio) y la linea pide DISENAR
      EXPERIMENTOS. Si eso no es expansion, cae a D.
  12. **`LD-OPC05-116`**: la sostengo en C, y dudo porque `gambling` se puede
      leer como UNA REGLA DE RIESGO que el sistema de gates materializa, y bajo
      esa lectura seria instancia y caeria a D por mi propio criterio.

**Y UN DISCUTIBLE QUE NO ES DE LECTURA SINO DE ALCANCE:** el patron literal de la
6.7. Publico la lectura B (pathspec que empieza por `dataset/`) como principal
porque la 6.7 describe el defecto por su INSTRUMENTO, pero las otras dos
lecturas estan medidas y publicadas al lado. Si la vara del acta era la
estrecha, la cifra es 4 y no 12.

## 12. PENDIENTES DE DOCTRINA

**UNO, Y LO TRAIGO COMO PENDIENTE PORQUE NO ESTABA ESCRITO:** la regla
**UNA INSTANCIA NO ES EL PROCEDIMIENTO DE SU CATEGORIA**. No la invente para
salir del paso: la aplique en OCHO lecturas del lote 2 y la declare en el
docstring del instrumento con la lista de las ocho, para que su consistencia se
pueda auditar de una sola mirada. **Pero no esta en el 9.22 ni en la 6.4 ni en la
6.3**, y es lo mas cerca de doctrina nueva que esta vuelta escribio. No pare
porque no CONTRADICE ninguna regla vigente (es una lectura estrecha de "el otro
nodo es el COMO SE HACE esa accion"), pero pido que se adjudique.

Donde mas tuve que interpretar (que es "el instrumento del lote" cuando el del
lote 2 aun no existe; que es "las 65 corregidas" cuando la propia vuelta mueve 43 mas;
que cuenta como "el patron literal") lo resolvi **midiendo las lecturas posibles
y publicandolas todas**, no eligiendo la comoda.

## 13. LAS PREGUNTAS

  1. **LA PARADA DE LA TAREA 5.** El alcance da 12 y el acta dice 11, con el
     residuo nombrado (`vuelta89_tarea4_guarda_op_c05.py`). Se aplica el remedio
     de la 5.a a los 12, a los 11, o a los 4 de la lectura estrecha?
  2. **EL SACO SE VACIO Y QUEDAN 18 EN C.** Ninguna esta sin leer. Se dan por
     cerradas, o las 18 reciben una segunda pasada como recibieron las 41?
  3. **LA REGLA DE LA INSTANCIA**, la del punto 12. Se adjudica, se corrige o se
     revoca? De ella cuelgan ocho clases de este lote.
  4. **LAS DOS SALIDAS CON PRODUCTOR HALLADO.** Las fichas que las citan pueden
     ahora nombrar a `verificar_cobertura_bolsa_tres_vias.py` y a
     `verificar_fuente_canonico.py`. Se reescriben las fichas, o basta con la
     marca que quedo junto a la funcion de la P3b?

## 14. EL MURO, Y LO QUE QUEDA DESPUES

**LA FASE 08 NO CIERRA SIN UNA SESION CON CREDENCIAL Y CON EL FUNDADOR DELANTE**
(acta 149, 3.10). La fase 08 cierra segun `SALIDA_V159_T9_FASE_08_VERIFICACION.txt` con 1 del catalogo, 0 cumplidas y 1 sin cumplir, que es OP-V-01, sin vara escrita. Medido hoy al cierre con
`scripts/loop/tallar_estado_de_fase.py --fase 08_VERIFICACION`, salida
`docs/loop/SALIDA_V159_T9_FASE_08_VERIFICACION.txt`: **fase 08 con una
operacion, una sin cumplir, `OP-V-01`, sin vara escrita**. **AHI SE PARA Y SE
DICE.**

**Y LO OTRO QUE EL ACTA 158 ANTICIPO YA SE VE.** La unica deuda de LECTURA que le
quedaba al bucle era el saco, y **el saco quedo vacio en esta vuelta**: 53 del
lote 2 mas 41 de la segunda pasada mas 3 en disputa. De las 122 lecturas
dirigidas, 104 estan en D y las 18 en C estan todas leidas. **No queda trabajo de
lectura que un bucle pueda hacer solo.**

**EL MERGE NO SE PIDE NI SE HACE: es del fundador y solo suyo. La campana NO esta
consumada.**
