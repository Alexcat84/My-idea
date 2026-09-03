# REPORTE DE LA VUELTA 160 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

**EL VEREDICTO DE UNA LINEA: LAS SIETE TAREAS ENTREGADAS, Y HAY PARADA. LA
RELECTURA CONJUNTA DE LA `LD-OPC05-100` CONFIRMA LA LECTURA DEL AUDITOR CONTRA LA
MIA, ASI QUE SON DOS TANDAS SEGUIDAS CON CAIDA DE CLASE Y LA REGLA DEL CREDITO SE
DISPARA.** El tramo al doble de las 37 se leyo ENTERO y trajo TRES caidas mias mas
(`094`, `101`, `118`), las tres de la misma costura. El check de P.16 queda
remediado en los DOCE sin partir el lote. Y traigo CINCO caidas propias, las cinco
cazadas por un instrumento o por una guarda antes de publicar, todas declaradas en
la seccion 1.

## 0. LA IDENTIDAD Y LA CABECERA, TALLADAS Y NO TECLEADAS

Todo lo de esta seccion sale de
`scripts/loop/tallar_cabecera_reporte.py --vuelta 160 --fase04`, salida
`docs/loop/SALIDA_V160_T7_CABECERA.txt`, pegada entera por
`scripts/loop/vuelta160_tarea7_escribir_reporte.py`, que la LEE del fichero.

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
| identidad: rama y commit de apertura (leidos de git, no tecleados) | rama `pasada-unica`, commit del acta `13cf21be` (asunto real leido de git log: 'ACTA DE LA VUELTA 159 DEL AUDITOR: EL CIERRE REPRODUCE AL DIGITO Y LA PARADA DE LA TAREA 5 ERA CORRECTA, PORQUE EL ALCANCE DA DOCE Y LA CIFRA MALA ERA LA MIA. PERO LA CIEGA DA UNA DISCREPANCIA FUERA DE LOS DOCE MARCADOS, LD-OPC05-100: BAJA EL CREDITO Y EL LOTE 2 SE RELEE AL DOBLE, 37 SEGUNDAS LECTURAS. Y LA RACHA DE CIFRA PUBLICADA QUEDA EN UNO, CON LA 005 CONFIRMADA.'), HEAD real de apertura `13cf21be` (sellado antes de la 1.a operacion, leido de git log --diff-filter=A), arboles de `dataset/` IGUALES: VERDE | **rama `pasada-unica`, HEAD de cierre `9163f13f` (leido de `SALIDA_V160_HEAD_CIERRE.txt`, sellado tras la ultima operacion)** |
<!-- FIN CABECERA TALLADA -->

**Y EL SELLO DE APERTURA LLEGO A TIEMPO, QUE ES LA 6.2 DEL ACTA 158 CUMPLIDA POR
SEGUNDA VUELTA SEGUIDA.** Los diez `SALIDA_V160_*_APERTURA.txt` nacieron TODOS en
`ac56c912`, el PRIMER commit del corredor e hijo directo del acta `13cf21be`.
Corrido con `scripts/loop/verificar_apertura_sellada.py --vuelta 160`, salida
`docs/loop/SALIDA_V160_T7_APERTURA_SELLADA.txt`: **VERDE exit 0**, y ademas lee
del commit del acta el rotulo de hashes admitidos y computa **0 (ninguno)**, que
es lo que el encargo declara.

| | valor | de donde sale |
|---|---|---|
| rama | `pasada-unica` | `git rev-parse --abbrev-ref HEAD` |
| commit de apertura | `13cf21be` | `docs/loop/SALIDA_V160_HEAD_APERTURA.txt` |
| commit de cierre (antes del commit del reporte) | `9163f13f` | `docs/loop/SALIDA_V160_HEAD_CIERRE.txt` |
| commits del corredor | 7, medidos ANTES del commit de este reporte; con el seran 8 | `git rev-list --count 13cf21be..HEAD` |
| intrusos en el corredor | 0 | los 7 son mios: 1 de apertura y 6 de tarea |
| hashes admitidos | 0 (ninguno) | leido del commit del acta por la guarda |

## 1. MIS CAIDAS, LAS CINCO, Y VAN ANTES QUE LO DEMAS

**CAIDA 1, DE CIFRA PUBLICADA, EN LA TAREA 5, Y ES LA MAS GRAVE PORQUE ENTRO POR
COPIAR EN VEZ DE MEDIR.** La TAREA 1 escribio en el comentario de la P3b, que es
la CUARTA SEDE de cifra publicada (decision del fundador del 2 sep 2026), el
reparto de las cuatro citas TAL COMO LO COPIE del acta 159 y del encargo, sin
medirlo: *"`PENDIENTES.md:6241` lo nombra dos lineas arriba dentro del mismo
parentesis"*, detras de `verificar_fuente_canonico.py`. **Recomputado en la TAREA
5 con instrumento propio** (`docs/loop/SALIDA_V160_T5_CITAS.txt`), el reparto real
es **TRES citas de la `SALIDA_V108` y UNA de la `SALIDA_V136`**, no dos y dos, y
**`docs/PENDIENTES.md:6241` nombra a `verificar_cobertura_bolsa_tres_vias.py`**,
no al otro. **Corregido por adicion en el mismo comentario**, sin borrar el texto
viejo. Lo que NO cambia, y por eso la 6.6 se sostiene entera: son cuatro citas,
las cuatro nombran a su productor, y **CIFRA fichas a reescribir: 0**.

**CAIDA 2, DE GUARDA QUE FALTABA, EN LA TAREA 2, Y LA CAZO EL MARCADOR DEL
CIERRE.** Mis TAREAS 2.a y 2.b movieron cuatro clases de C a D (`094`, `100`,
`101`, `118`) **con las seis guardas de la 2.d en verde**, y dejaron sus cuatro
campos `cita` diciendo `clase C` sobre filas que ya son `D`. **Eso es la regresion
exacta de la adjudicacion 6.6 del acta 158**, que la vuelta 159 habia dejado en
cero. Ninguna de las seis guardas miraba esa coherencia. **Lo delato el marcador
del cierre**, que dejo `CIFRA citas con rastro de correccion` clavada en 106
despues de mover cuatro clases. Arreglado en la TAREA 7.b y **la guarda que
faltaba anadida AL MOTOR**, no al parche, con su prueba de mutacion (TAREA 7.c).

**CAIDA 3, DE MUTACION MAL FABRICADA, EN LA TAREA 6.b.** Mi primera mutacion de
`commit_acta` devolvia `None` **sin anadir su fallo**, y con eso la guarda salia
VERDE y el caso 2 caia. Pero **ese estado no existe en el codigo real**: leido
`commit_acta` entero, sus dos salidas con `None` anaden su fallo antes de volver.
**La mutacion estaba mal, no el codigo.** Una mutacion que fabrica un estado
imposible no prueba nada. Declarada en la fuente del arnes.

**CAIDA 4, DE ARNES, EN LA TAREA 6.b, Y HABRIA HECHO PASAR UN CASO POR EL MOTIVO
EQUIVOCADO.** La version vieja de la guarda se carga de un fichero temporal, y su
`RAIZ` se computa de su propio `__file__`: apuntaba al temporal. Su `(no hallado)`
del caso 3 **podia venir de la ruta rota y no del defecto**. Lo delato el caso 4,
que dio exit 1 sobre una vuelta que es VERDE. Corregido forzando `RAIZ` y `LOOP`,
y declarado en la fuente.

**CAIDA 5, DE IMPRESION, EN LA TAREA 3.b.** La linea final del arnes imprimia el
literal `%d` porque le faltaba su operando. Cazada releyendo mi propia salida
antes de commitearla. Corregida con la linea vieja tachada al lado.

**LO QUE TIENEN EN COMUN LAS CINCO, Y LO ESCRIBO PORQUE ES LA LECCION: NINGUNA LA
VI AL ESCRIBIR.** Las cinco las cazo un instrumento (el buscador de citas, el
marcador del cierre, el caso 4 del arnes) o la relectura de mi propia salida. La
unica que no tenia instrumento detras era la 2, y por eso lo primero que se hizo
al arreglarla fue construirselo.

## 2. LA PARADA, Y VA PRONTO PORQUE NO ES UNA TAREA SINO EL ESTADO DEL BUCLE

**LA RELECTURA CONJUNTA DE LA `LD-OPC05-100` CONFIRMA LA LECTURA DEL AUDITOR Y LA
CLASE PASA DE C A D.** El acta 159 lo dejo escrito con todas sus letras en su
seccion 7: *"ESTAMOS A UNA DE LA PARADA: si la conjunta confirma mi lectura de la
`100`, seran DOS TANDAS SEGUIDAS y el bucle se para por la regla del credito."*

  - Racha de cifra publicada al abrir esta vuelta: **UNO** (la `LD-OPC05-005`,
    confirmada en la vuelta 159, caida de CLASE de la tanda 157).
  - Esta tanda trae caida de CLASE confirmada: **SI**, la `100`, y ademas otras
    tres de la misma especie halladas por mi propio tramo (`094`, `101`, `118`).
  - **DOS TANDAS SEGUIDAS.** `docs/loop/AUDITOR.md` seccion 4: *"Caida de CLASE o
    de CIFRA PUBLICADA ... cuenta para el credito y para la parada. Dos tandas
    seguidas: PARADA."*

**LO QUE HAGO Y LO QUE NO HAGO, Y LO SEPARO PARA QUE NO SE CONFUNDA DECLARAR CON
EJECUTAR.** Lo declaro como **PARADA** aqui, que es lo que EJECUTOR.md 5 manda
(*"lo escribes en el reporte como PARADA y no lo arreglas tu"*). **NO escribo
`docs/loop/PARA_ALEXIS.md`, NO vacio `docs/loop/PROMPT_SIGUIENTE.md` y NO pido el
merge**: las tres son acciones del auditor y del fundador segun la seccion 4 del
AUDITOR.md, y ademas la seccion 9 del acta 159 las prohibe expresamente. **Y
ejecuto el encargo entero**, empezando por la TAREA 2.b, que es justamente el
remedio que la 6.4 encargo por la bajada de credito: abandonarlo a mitad dejaria
sin hacer el trabajo que la parada viene a exigir.

**Y LO DIGO SIN ESCUDO: LA `100` LA LEI YO MAL EN EL LOTE 2 DE LA VUELTA 159, Y
LAS `094`, `101` Y `118` TAMBIEN.** Las cuatro caen en la misma costura que el
acta 159 nombro: **la segunda linea de una C**.

## 3. TAREA 1, LAS OCHO ADJUDICACIONES DEL ACTA 159

Salida `docs/loop/SALIDA_V160_T1_ADJUDICACIONES.txt`, y las cifras salen de ahi.

```
CIFRA operaciones de escritura de esta corrida: 19
CIFRA de ellas ANADIDAS: 19
CIFRA de ellas YA ESTABAN: 0
CIFRA adjudicaciones diferidas a otra tarea de esta misma vuelta: 1
   CIFRA ficheros .py tocados: 16
   CIFRA borrados en los .py tocados: 0
   CIFRA razones cuyo texto viejo YA NO ES PREFIJO: 0
   CIFRA clases movidas por esta tarea: 0
```

Las ocho lineas de arriba salen de
`docs/loop/SALIDA_V160_T1_ADJUDICACIONES.txt`. **EL RECORTE SE DECLARA:** de ese
bloque se omite aqui la linea de PARES de la seccion C.4, y el motivo es que su
fichero no la
escribe en la forma que `verificar_cifras_del_reporte.py` sabe cotejar, asi que
pegarla dejaria en el reporte una cifra que ninguna guarda puede comprobar. Esta
entera en el fichero.

**EL ALCANCE DE LA 6.1 SALE DOCE POR DOS VIAS INDEPENDIENTES Y NO POR UNA.** Se
computa del CODIGO (patron literal de la lectura B, con los TRES buscadores
excluidos por nombre y declarados) y se cuenta de SU FICHERO (seccion C de
`docs/loop/SALIDA_V159_T5_ALCANCE.txt`), y el instrumento PARA si no salen
identicas. **Salen identicas elemento a elemento y dan 12.**

**LA 6.3 QUEDO DIFERIDA A LA TAREA 2.a, Y SE DECLARA EN VEZ DE CALLARSE.** La 6.3
manda `LD-OPC05-100` a relectura conjunta, o sea que su bloque tiene que traer
DENTRO el veredicto medido contra los nodos. Escribirla en la TAREA 1, antes de
leer, habria sido una adjudicacion sin medicion. Va escrita en la razon de la
`100`, con el veredicto dentro.

## 4. TAREA 2.a, LA UNA EN DISPUTA: `LD-OPC05-100` PASA DE C A D

Salida `docs/loop/SALIDA_V160_T2A_VEREDICTOS.txt`. Dossier de los dos nodos en
`docs/loop/SALIDA_V160_T2A_DOSSIER.txt` y dossier de contraste (`052`, `095`,
`122`) en `docs/loop/SALIDA_V160_T2A_CONTRASTE.txt`, recomputados hoy.

**LA LINEA 2 SE SOSTIENE Y NO ESTABA EN DISCUSION:** el paso 5 de
`proceso_ideacion_modelo_negocio` lo expanden los doce pasos de
`lienzo_modelo_negocio`.

**LA LINEA 1 NO PASA LA VARA, Y ESE ERA TODO EL DESACUERDO.** Tres motivos, y los
tres se leen de los nodos:

  1. **LA FORMA.** El paso 2 de ideacion es LA MISMA ORDEN CON TRES COMPLEMENTOS
     (investigar, y despues que investigar). Contrastado contra lo que **esta
     misma vara acepto**: en la `052`, *las 6 preguntas de Chopra y Meindl*, un
     instrumento con autor y seis dimensiones; en la `095`, los cinco pasos de
     process tracing, un metodo secuenciado entero. Y contra lo que **excluyo**:
     en la `122`, *revisa e integra practicas seguras en cada etapa*, orden mas
     complemento de alcance. **El paso 2 de ideacion es de la especie de la 122.**
  2. **EL DISPARADOR Y EL MOMENTO, Y ESTO NO LO HABIA MEDIDO NADIE.** El paso 9
     del lienzo es una PAUSA DENTRO de la construccion del lienzo, disparada por
     vacios ya identificados. La fase de inmersion corre ANTES de que exista
     ningun lienzo lleno: **no la dispara ningun vacio y no toma el vacio como
     insumo.**
  3. **Y LA DECISIVA, PORQUE SE LEE DE UN CAMPO Y SE PUEDE VOLVER A MEDIR: EL
     ENTREGABLE.** El de ideacion dice *"Lista corta de 3 a 5 prototipos de modelo
     de negocio ESBOZADOS EN EL LIENZO DE MODELO DE NEGOCIO"*; el del lienzo no
     menciona la ideacion. **Ideacion CONSUME el lienzo; el lienzo no consume la
     ideacion.** Eso es una sola direccion, madre e hijo, y el par continua.

**Y NO SE PUBLICA COMO CONCESION.** El argumento del ENTREGABLE no lo habia usado
ninguna de las dos plumas, y se puede volver a medir en el grafo. **Bajo la 6.3 se
recorrio el espacio entero de la direccion en disputa y van NOMBRADOS LOS TRES
PARES MAS FUERTES QUE SE DESCARTAN**, uno a uno, en la razon.

**LAS GUARDAS DE LA 2.d, PEGADAS DE SU SALIDA:**

```
   C.1 PREFIJO: las 154 razones conservan su texto viejo ENTERO
   C.3 CLASES MOVIDAS: 1
       LD-OPC05-100     C -> D
       NINGUNA SE MUEVE A A: el limite de la 6.1 del acta 155 se cumple.
       EL REGISTRO CAMBIA, EL GRAFO NO: sha256 IDENTICO y censo IDENTICO
   C.5 CIFRA n, veredictos del cribado DESPUES: 3388
```

Las cinco lineas de arriba salen de
`docs/loop/SALIDA_V160_T2A_VEREDICTOS.txt`, seccion C, y por el mismo motivo que
en la seccion 3 se omite aqui la linea de PARES de la seccion C.2, que esta
entera en el
fichero.

## 5. TAREAS 2.b Y 2.c, EL TRAMO AL DOBLE: LAS 37 ENTERAS

**LA NOMINA, RECOMPUTADA ANTES DE LEER NADA**
(`docs/loop/SALIDA_V160_T2B_NOMINA.txt`, sellada en
`docs/loop/NOMINA_V160_TRAMO.json`). El lote 2 sale de su fichero sellado, las 16
releidas salen **del propio fichero de computo del auditor** pegado entero, y la
resta se coteja **elemento a elemento** contra la nomina que el publico:

```
   CIFRA lote 2 menos releidas: 53 menos 16 da 37
   CIFRA que el auditor publica: 37
   LAS DOS NOMINAS SALEN IDENTICAS, ELEMENTO A ELEMENTO.
   CIFRA por clase: {"C": 8, "D": 29}
   REPRODUCE AL DIGITO.
```

**EL RESULTADO, PEGADO DE `docs/loop/SALIDA_V160_T2B_VEREDICTOS.txt`:**

```
   CIFRA lecturas dirigidas por clase: {"C": 14, "D": 108}
   CIFRA con la clase movida en esta tarea: 3
   CIFRA que sostienen su clase en esta tarea: 34
   CIFRA que ya estaban escritas: 0
   C.3 CLASES MOVIDAS: 3
       LD-OPC05-094     C -> D
       LD-OPC05-101     C -> D
       LD-OPC05-118     C -> D
       NINGUNA SE MUEVE A A: el limite de la 6.1 del acta 155 se cumple.
```

Las nueve lineas de arriba salen de `docs/loop/SALIDA_V160_T2B_VEREDICTOS.txt`.

**LAS TRES QUE CAEN SON MIAS Y SON DE LA MISMA ESPECIE QUE LA `100`.** La `094`
por la regla de la instancia aplicada contra mi propio veredicto anterior; la
`101` y la `118` porque su segunda direccion descansaba en una REMISION (*aplica
el proceso de Customer Development*) y en una ORDEN CON CRITERIO DE PARADA (*itera
y pivota hasta que sea repetible y escalable*), que es la letra con que cayeron la
`027` y la `004`. **Las cinco C que se sostienen** (`068`, `087`, `088`, `098`,
`109`) tienen las dos direcciones con procedimiento o instrumento nombrado, y cada
una lo dice.

**LA 2.c, LA AUDITORIA DE CONSISTENCIA DE LA REGLA DE LA INSTANCIA (6.5.b),
PEGADA DE SU SALIDA.** Se publica en TRES estados y no en dos, porque dos no
alcanzan para auditar una regla: el estado que la hace auditable es el segundo.

```
   CIFRA lecturas del tramo: 37
   CIFRA en que la regla APLICA: 10
   CIFRA en que NO APLICA PUDIENDO PARECER QUE SI: 8
   CIFRA en que NO SE PLANTEA: 19
   CIFRA de ellas en que es el UNICO motivo del descarte: 7
   CIFRA de ellas con un segundo motivo que se sostiene solo: 3
```

**LA CONDICION (a) DE LA 6.5 SE APLICA CON SU LETRA Y SE PUBLICA LA DIFERENCIA:**
las **7** en que la regla es el UNICO motivo quedan MARCADAS COMO DISCUTIBLES; las
**3** en que hay un segundo motivo que se sostiene solo (`076`, `089`, `111`) NO
quedan marcadas por esa via, **y se dice cual es ese segundo motivo en cada una**.
Sin esa distincion, la condicion (a) seria inauditable.

**Y EL LIMITE DE LA 6.1 DEL ACTA 155 NO SE CRUZO: NINGUNA SALIO A**, no hay
candidato a fusion, no se toco una arista y `n` no se movio.

## 6. TAREA 3, EL CHECK DE P.16 REMEDIADO EN LOS DOCE

**NO SE PARTIO EL LOTE: LOS DOCE CABEN CON SUS GUARDAS COMPLETAS.** La 3.c
autorizaba partirlo diciendolo; no hizo falta.

**EL REMEDIO** vive en `scripts/loop/huella_de_contenido.py`, que nace hoy y **NO
MIRA A GIT NI UNA VEZ**: hashea los bytes crudos del disco bajo los prefijos que
se le pasan y compara el disco contra el disco. **Con eso mueren las dos anclas de
la 6.7 a la vez**: el fin de linea no puede meterse entre dos tomas de la misma
corrida, y la suciedad anterior aparece en LAS DOS tomas y se cancela. **Se
declara lo que NO puede ver**: un fichero escrito y devuelto a su contenido exacto
antes de la segunda toma. La comprobacion vieja tenia la misma ceguera.

**TRES FORMAS DE REMEDIO, SEGUN LA FORMA QUE TENIA CADA UNO, Y LAS TRES
DECLARADAS** en `scripts/loop/vuelta160_tarea3_remedio_p16.py`. Y **el que escribe
a proposito** (`vuelta143_3c_girar_arista.py`, que es la operacion que gira la
arista) **se declara INFORME Y NO VARA en su propia salida**, en vez de
fabricarle un veredicto que no le corresponde.

**Y EN `vuelta89_tarea4_guarda_op_c05.py` EL REMEDIO RETIRA UNA PARADA**: ese
script abortaba si `dataset/` venia sucio ANTES de arrancar, que es el ancla 2 en
su forma mas pura. Como no escribe en `dataset/` ni una vez, la suciedad anterior
no puede falsear su medicion.

**LA ADITIVIDAD, PEGADA DE `docs/loop/SALIDA_V160_T3_REMEDIO.txt`:**

```
   CIFRA ficheros remediados en esta corrida: 12
   CIFRA de los doce que siguen casando con el patron: 12
   CIFRA lineas anadidas: 264
   CIFRA lineas retiradas: 39
   CIFRA lineas retiradas SIN su copia tachada: 0
```

**LAS 39 RETIRADAS NO SON BORRADOS SILENCIOSOS Y NO SE PROMETE, SE COMPRUEBA:** el
propio instrumento lee el `git diff -U0` de cada fichero y exige que TODA linea
retirada aparezca, en el mismo fichero, dentro de un comentario con la marca de
tachado. **Cero huerfanas.** Y de ahi sale una consecuencia que se declara: como
el texto viejo sobrevive, **los doce siguen casando con el patron literal y el
alcance de la 6.1 sigue siendo DOCE despues del remedio**.

**EL CASO POSITIVO POR MUTACION (3.b), CINCO CASOS Y LOS CINCO VERDES**
(`docs/loop/SALIDA_V160_T3B_CASO_POSITIVO.txt`), corrido sobre el DUODECIMO, que
es donde el defecto era mas grave:

```
  OK    CASO 1, la huella cae con una escritura real y vuelve
  OK    CASO 2, una escritura real SIGUE cayendo en rojo
  OK    CASO 3, la suciedad ajena YA NO tumba la guarda
  OK    CASO 4, contraprueba en limpio, sale verde
  OK    LA LIMPIEZA: dataset/ vuelve identico a la apertura
```

**Y EL CASO 3 NO AFIRMA QUE EL CODIGO VIEJO ABORTABA: EVALUA SU CONDICION
LITERAL** sobre el mismo estado y publica el resultado. **La limpieza se mide por
huella al terminar, no se promete.**

**LA BATERIA ENTERA SE RE CORRIO SOLA DESPUES, Y DOS VECES**
(`docs/loop/SALIDA_V160_T3_BATERIA.txt` y
`docs/loop/SALIDA_V160_T3B_BATERIA_DESPUES.txt`): **VERDE las dos, 23 mutaciones,
0 ancla perdida, 0 no mordio, 0 no reproducible, 2 casos declarados, RUIDO DE
CONCURRENCIA 0.** Y los cuatro de los doce que estan FUERA de la bateria se
corrieron sueltos (`docs/loop/SALIDA_V160_T3_FUERA_DE_BATERIA.txt`): **exit 0 los
cuatro.** El quinto de fuera, `vuelta143_3c_girar_arista.py`, no se corre suelto a
proposito porque con `--ejecutar` escribe en `dataset/` por diseno: **lo ejercita
la bateria a traves de `vuelta144_2b_mutacion_giro.py`**, que lo importa y lo
conduce.

## 7. TAREA 4, EL MARCADOR DE CIERRE PARAMETRIZADO

Salida `docs/loop/SALIDA_V160_T4_PARAMETRIZADO.txt`. Toma `--vuelta` y el rotulo
se interpola. **Sin valor por defecto A PROPOSITO**, y se dice por que: un defecto
silencioso volveria a clavar un numero, solo que mas escondido. **Sin `--vuelta`
cae con exit 2.** El literal viejo queda tachado y legible en el comentario de su
correccion declarada, y el numstat es **21 anadidas, 1 retirada**, que es esa
linea.

## 8. TAREA 5, LA MARCA DE LA P3b Y LA CIFRA QUE RECOMPUTE

Salida `docs/loop/SALIDA_V160_T5_CITAS.txt`, con **la vara declarada antes de
contar** y **la vecindad de cada cita impresa entera**, para que se vea que no se
estiro para que saliera.

```
CIFRA citas halladas en total: 4
CIFRA de ellas que NOMBRAN a su productor: 4
CIFRA de ellas SIN productor a la vista: 0
CIFRA fichas que hay que reescribir: 0
```

**LA 6.6 SE SOSTIENE: LAS FICHAS NO SE REESCRIBEN.** Lo que si va escrito junto a
la funcion de la P3b es la leccion: **el angulo barato era leer la ficha que cita
la salida**, donde el productor llevaba meses escrito al lado. Los cuatro angulos
de la vuelta 159 buscan al productor DESDE LA SALIDA; el barato lo busca DESDE
QUIEN LA CITA.

**Y LA DISCREPANCIA DE ATRIBUCION VA DECLARADA, NO RESUELTA COPIANDO** (es la
caida 1 de la seccion 1): el reparto real es **tres y una**, no dos y dos.

## 9. TAREA 6, LA PUERTA DEL CORREDOR QUE MENTIA

Las salidas tempranas de `verificar()` llevan ahora **el `acta` que ya tienen** en
vez de un hueco, y **si de verdad no se hallo, se sigue diciendo**. Numstat: 40
anadidas, 4 retiradas, y las cuatro tachadas y legibles.

**EL CASO POSITIVO (6.b), CUATRO CASOS Y LOS CUATRO VERDES**
(`docs/loop/SALIDA_V160_T6B_MUTACION_PUERTA.txt`):

```
  OK    CASO 1, sin ficheros: sigue ROJO y nombra el acta
  OK    CASO 2, sin acta de verdad: (no hallado) sobrevive
  OK    CASO 3, el codigo viejo reproduce el defecto
  OK    CASO 4, los codigos de salida no se movieron
```

**EL CASO 3 ES LO QUE CONVIERTE AL CASO 1 EN PRUEBA DE UN REMEDIO:** la version
ANTERIOR se saca de git y se le da el MISMO escenario, y miente. Y **el caso 4
comprueba que ningun veredicto se movio**, cotejando los codigos de salida de
viejo y nuevo sobre la vuelta 160 (VERDE) y la vuelta 100 (el ROJO historico de
esta guarda).

## 10. TAREA 7, EL CIERRE RECOMPUTADO AL CIERRE

**EL CICLO ENTERO Y EN SU ORDEN, NUNCA `run_phase1` SUELTO:**
`--reaplico-curaduria` (`docs/loop/SALIDA_V160_GATE0_CMD1_CIERRE.txt`, **GATE 0:
OK**), `etiquetas_de_cara --aplicar`
(`docs/loop/SALIDA_V160_CICLO_ETIQUETAS_CIERRE.txt`, **71 etiquetas**),
`sync_assets_web` (`docs/loop/SALIDA_V160_CICLO_SYNC_CIERRE.txt`, **seis
assets**) y despues el `numstat`
(`docs/loop/SALIDA_V160_CICLO_NUMSTAT_CIERRE.txt`, **cero filas**). El conteo del
Gate 0 sale de `docs/loop/SALIDA_V160_T7_CONTEO_GATE0.txt`: **26 en OK y 0 en
FALLO**.

**EL MARCADOR, EL CENSO Y EL REGISTRO, RECOMPUTADOS AL CIERRE** con el instrumento
ya parametrizado (`--vuelta 160`), pegado de
`docs/loop/SALIDA_V160_T7_MARCADOR_CIERRE.txt`:

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
CIFRA registro LECTURA_DIRIGIDA clase C: 14
CIFRA registro LECTURA_DIRIGIDA clase D: 108
CIFRA citas de lectura dirigida: 122
CIFRA citas con rastro de correccion: 110
CIFRA citas en la forma vieja de la vuelta 156: 0
```

**LAS TRES SUITES:** motor **25/25** (`docs/loop/SALIDA_V160_MOTOR_CIERRE.txt`),
vitest **DESDE `web/`** con **Test Files 80 passed (80)** y **Tests 1.030 passed,
3 skipped (1.033)** (`docs/loop/SALIDA_V160_WEB_CIERRE.txt`), y `tsc --noEmit` con
**EXIT=0 y cero lineas** (`docs/loop/SALIDA_V160_TSC_CIERRE.txt`).

**EL EXPEDIENTE, CORRIDO CON EL CORTE DE APERTURA.** CIFRA fichas del expediente:
**71 operaciones**, y sale de `docs/loop/SALIDA_V160_T7_EXPEDIENTE.txt`, corrido
con `--corte 13cf21be`. Y de esa misma salida salen las otras cinco, que
escribo con el numero detras del rotulo para que ninguna se pueda confundir con
la vecina al cotejarla: fichas que no calzan 36, fichas congeladas declaradas 24,
fichas congeladas en silencio 12, fichas HECHA sin ninguna prueba 0, fichas en
LISTA sin ninguna prueba 7.

**LAS CUATRO FASES, CADA UNA DE SU TALLADOR, Y CADA UNA NOMBRANDO LAS SUYAS.**
La fase 03_FUSIONES cierra con 4 sin cumplir, que son `OP-M-02-ADMIT`,
`OP-M-02-MEDIOS`, `OP-U-01` y `OP-U-02`, segun
`docs/loop/SALIDA_V160_T7_FASE_03_FUSIONES.txt`, que trae 16 del catalogo y 12
cumplidas; de esas cuatro, dos sin vara escrita (`OP-U-01` y `OP-U-02`) y dos
consumidas con superviviente divergente (`OP-M-02-ADMIT` y `OP-M-02-MEDIOS`). La fase 06_MESAS cierra segun
`docs/loop/SALIDA_V160_T7_FASE_06_MESAS.txt` con 16, 16 y 0. La fase
08_VERIFICACION cierra segun `docs/loop/SALIDA_V160_T7_FASE_08_VERIFICACION.txt`
con 1 del catalogo, 0 cumplidas y 1 sin cumplir, que es `OP-V-01`, sin vara
escrita. La fase 09_LECTURAS_DIRIGIDAS cierra segun
`docs/loop/SALIDA_V160_T7_FASE_09_LECTURAS_DIRIGIDAS.txt` con 3, 0 y 3, que son
`OP-L-01`, `OP-L-02` y `OP-L-03`.

**LAS TAREAS 7.b Y 7.c, QUE NACEN DE MI CAIDA 2 Y NO DEL ENCARGO.** La 7.b
reescribe las cuatro citas a la forma unica de la 6.6 del acta 158, por adicion, y
publica **cero descuadradas al terminar** y **110 citas con rastro**
(`docs/loop/SALIDA_V160_T7B_UNIFICAR_CITA.txt`). La 7.c anade la guarda que
faltaba **al MOTOR y no al parche**, y le corre su prueba de mutacion de cuatro
casos, todos verdes (`docs/loop/SALIDA_V160_T7C_MUTACION_GUARDA.txt`), incluida
**la mutacion del valor esperado**, que es la que separa una guarda que mide de un
`assert` que se aprueba solo: mutado el valor con que compara, **la guarda deja de
caer sobre el escenario que antes la tumbaba**. Y los tres ficheros reales quedan
**intactos por sha256**, medido y no prometido.

**LAS GUARDAS DEL CIERRE, CON SU ESTADO REAL AUNQUE NO ME FAVOREZCAN:**

  - `verificar_mutaciones_viejas.py`, **SOLA Y SIN NADA AL LADO** como la TAREA 7
    exige (`docs/loop/SALIDA_V160_T7_BATERIA.txt`): **VERDE exit 0**, 23
    mutaciones, **0 ancla perdida, 0 no mordio, 0 no reproducible, 2 casos
    declarados, RUIDO DE CONCURRENCIA 0**.
  - `verificar_apertura_sellada.py --vuelta 160`
    (`docs/loop/SALIDA_V160_T7_APERTURA_SELLADA.txt`): **VERDE exit 0**, los diez
    ficheros de apertura nacidos en `ac56c912`, hijo directo del acta.
  - `tallar_cabecera_reporte.py --vuelta 160 --fase04 --comparar`, la guarda de
    que la cabecera de este reporte no se tecleo
    (`docs/loop/SALIDA_V160_T7_CABECERA_COMPARADA.txt`): **VERDE**, nueve filas
    cotejadas, cero distintas, cero ausentes, **CABECERA IDENTICA AL TALLADOR**.
  - `verificar_cifras_del_reporte.py`
    (`docs/loop/SALIDA_V160_T7_CIFRAS_REPORTE.txt`): **VERDE exit 0**, con cinco
    afirmaciones cotejadas contra su tallador y una cifra por etiqueta. **Y salio ROJO cuatro veces antes de salir verde**, por cosas
    reales: la fase 03 no nombraba sus cuatro sin cumplir, la frase del muro no
    citaba su tallador, y dos bloques pegados traian una cifra que su fichero no
    escribe en forma cotejable. **Las cuatro se arreglaron mirando la salida, no
    aflojando la guarda**, y el recorte de los dos bloques va declarado en su
    sitio.
  - `verificar_re_sellado.py --reporte docs/loop/REPORTE.md`
    (`docs/loop/SALIDA_V160_T7_RE_SELLADO.txt`): **VERDE exit 0**, con **re
    selladas SIN declarar 0** y la exencion por construccion impresa con sus dos
    nombres.
  - `scripts/loop/verificar_mapas_destejido.py` **NO SE CORRE, Y SE DICE POR
    QUE**: esta vuelta no publica ninguna tabla de particion (fila = destino,
    origenes, motivo), que es lo unico que esa guarda vigila. Decirlo vale mas que
    correrla sobre nada y publicar un verde vacio.

## 11. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**QUINCE DE LAS 37 DEL TRAMO, Y VAN EN DOS FAMILIAS QUE SE DISTINGUEN**
(`docs/loop/SALIDA_V160_T2B_VEREDICTOS.txt`, seccion F):

  - **LAS SIETE QUE LA 6.5.a OBLIGA A MARCAR** porque la regla de la instancia es
    el UNICO motivo del descarte del par mas fuerte: `LD-OPC05-082`, `094`, `099`,
    `106`, `107`, `113` y `119`.
  - **LAS OCHO QUE MARCO YO POR DUDA PROPIA**, porque aceptaria un veredicto
    distinto si se argumenta: `LD-OPC05-074`, `076`, `098`, `101`, `112`, `114`,
    `118` y `121`.

**ES MUCHO Y SE DICE POR QUE:** este tramo se leyo con la vara recien estrechada
por la `100`, y una vara recien estrechada produce mas dudas honestas que una
vieja. **Las tres que quiero que se miren primero, si hay que elegir:** la `098`
(la sostengo en C y su segunda linea es del mismo tipo que las que tumbe en la
`101` y la `118`, aunque con instrumentos concretos en vez de ordenes con
criterio), la `101` y la `118` (las bajo a D por una vara que fije yo mismo hoy en
la `100`, o sea que estoy juzgando con una vara de esta misma vuelta).

**Y UNO MAS, FUERA DEL TRAMO:** la **TAREA 3, FORMA 3**. Declarar que
`vuelta143_3c_girar_arista.py` lleva la huella como INFORME y no como VARA es una
decision mia; se podria sostener que un fichero que no rinde veredicto no debia
estar en el alcance de los doce. **Lo dejo dentro porque el alcance lo fijo el
acta 159 midiendo el patron, no midiendo si rinde veredicto**, y cambiar el
criterio de alcance por mi cuenta seria mover una cifra adjudicada.

## 12. PENDIENTES DE DOCTRINA

**NO HAY NINGUNO NUEVO EN ESTA VUELTA.** Las ocho adjudicaciones del acta 159 se
escribieron con reglas existentes, la regla de la instancia quedo adjudicada por
la 6.5 y su consistencia auditada por la 6.5.b, y la parada de la seccion 2 es la
aplicacion literal de una regla escrita, no una regla nueva.

**LO QUE SI DEJO ANOTADO, Y NO ES DOCTRINA SINO UN HUECO DE GUARDA YA TAPADO:** la
coherencia entre la clase vigente y la clase que el campo `cita` declara no la
vigilaba nadie hasta hoy. Queda vigilada en el motor, con su prueba de mutacion.

## 13. LO QUE NO PUDE MEDIR Y TRAIGO COMO PREGUNTA

  1. **El acumulado de segundas lecturas independientes sobre las 122.** El acta
     158 publico 84 y el acta 159 dijo que se mediria cuando el tramo cerrara. **El
     tramo cerro hoy**, pero **no recompute ese acumulado** porque no tengo el
     instrumento que lo produjo ni la definicion exacta de que cuenta como segunda
     lectura independiente. **No lo repito como cifra.**
  2. **Las 12 congeladas en silencio, ficha a ficha.** La cifra reproduce (12),
     pero **la nomina una a una sigue sin cotejar**, igual que en las actas 155,
     157, 158 y 159.
  3. **El contenido de los seis assets de `sync_assets_web`.** Comprobado que
     corre y que el `numstat` queda en cero filas; **no audite lo que escribe.**
  4. **Las cinco C que quedan en el lote 2 tras esta pasada** (`068`, `087`, `088`,
     `098`, `109`): tienen dos lecturas independientes cada una y por la 6.7 del
     acta 159 quedarian cerradas, **pero esa 6.7 se escribio antes de que este
     tramo moviera tres clases**. Pregunto si el reparto de las 18 hay que
     recomputarlo con las clases de hoy.

## 14. EL MURO SIGUE DONDE ESTABA

La fase 08 no cierra sin una sesion con credencial y con el fundador delante
segun `docs/loop/SALIDA_V160_T7_FASE_08_VERIFICACION.txt`, con 1 del catalogo, 0
cumplidas y 1 sin cumplir, que es `OP-V-01`, sin vara escrita (acta 149, 3.10).
**Ahi se para y se dice.**

**Y NO REPITO EL ERROR DE LA VUELTA 159: NO DIGO QUE EL SACO DEJE AL BUCLE SIN
TRABAJO.** El acta 159 me corrigio esa conclusion y tenia razon. Hoy el saco de
lectura dirigida queda en **14 en C**, de las cuales cinco acaban de recibir su
segunda lectura en este mismo tramo, y **queda abierta la pregunta 4 de la seccion
13** sobre si el reparto de las 18 hay que recomputarlo.

**NO SE ESCRIBE `PARA_ALEXIS.md`, NO SE VACIA `PROMPT_SIGUIENTE.md` Y NO SE PIDE
EL MERGE.** El merge es del fundador y solo suyo. **La campana NO esta consumada**,
y ademas **el bucle esta en PARADA por la regla del credito**, que es lo que dice
la seccion 2.
