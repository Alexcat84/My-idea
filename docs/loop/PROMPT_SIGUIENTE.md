# ENCARGO DE LA VUELTA 202 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

Commitea y pushea lo pendiente en la rama activa antes de tocar nada.

## LO QUE MANDA ESTA VUELTA, Y VA DELANTE PARA QUE NO SE DEDUZCA

- **RIGE LA MORATORIA DE MAQUINARIA** (`AUDITOR.md` 6.3): **ninguna vuelta fabrica
  arneses, guardas ni lectores nuevos.** Esta vuelta **no tiene ninguna excepcion**.
  Lo que necesites, **lo importas**: esta vuelta se apoya en instrumentos que **ya
  existen** y los nombro uno a uno abajo. **La nomina sigue CONGELADA en 135.**
- **NO ES VUELTA DE BATERIA.** Corrio entera en la 200 y por la cadencia de cinco de
  `AUDITOR.md` 6.1 **le toca a la 205**. Tu seccion 9 cierra con el **hueco declarado y
  medido** por el carril de `cerrar_reporte.py`: **nombre, bytes medidos y atribucion,
  las tres juntas**.
- **EL TOPE DE SUB-TAREAS ES CINCO** (la racha de cierres valia 2 al abrir la 201 y esta
  vuelta la deja en 3). **Este encargo trae CUATRO.**
- **NO SE MUEVE NINGUN CAMPO `estado`.** La vara del trabajo pendiente es
  `scripts/loop/vuelta150_3_relectura_expediente.py`, nunca el campo (`AUDITOR.md` 0).
- **NO SE MUEVE NINGUNA CLASE NI NINGUN VEREDICTO.** El `sha256` LF de
  `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` abre y cierra igual, y hoy vale
  `0a77b5a35a962621` por las dos convenciones. Publica las dos medidas.
- **`dataset/`, `web/` y `engine/` en cero filas de `numstat`.** Y si corres el Gate 0,
  corre **el ciclo entero de cuatro comandos**, nunca `run_phase1.py` a secas: a secas
  recompila el grafo y revierte 71 etiquetas curadas, y eso tumbo a dos auditores
  seguidos.

## LO QUE EL ACTA 201 ADJUDICO Y NO TIENES QUE VOLVER A LEVANTAR

- **LA PARADA DE LA 201 NO ERA PARADA, Y ESTA DISUELTA** (acta 201, `4.1`).
  `OP-L-02` **si se puede medir sin decidir**: sus seis nominas viven **por id** en la
  constante `NOMINAS_OP_L_02`, y su `verificacion[1]` **sale CUMPLIDA** medida por el
  auditor con `scripts/loop/vuelta170_tarea5b_veredicto_op_l_02.py`. **No la vuelvas a
  levantar.**
- **EL `NO CUMPLIDA` DE SU CLAUSULA 2 ES UN FALSO ROJO** (acta 201, `4.2`): ese
  instrumento diffea contra un HEAD sellado en la vuelta 170 (`46208790`). **Su
  reparacion es de codigo, la moratoria la prohibe y va a la auditoria integral.**
- **LA COORDENADA DE UNA FICHA JSONL ES LINEA MAS INDICE** (acta 201, `4.4`), y desde
  ahora es la convencion. **Sigue usandola.**

## TAREA 1: LA CORRECCION DECLARADA DE LA `evidencia` DE `OP-L-03`, EN SU SEDE

**Adjudicada por el acta 201 en su `4.3`.** El ejecutor de la 201 hizo bien en proponerla
y no escribirla sin adjudicacion; **ahora esta adjudicada y se escribe.**

- **EL CARRIL ES EL DE `OP-I-01` DE LA VUELTA 201, Y NO OTRO:** banco `9.10`, **POR
  ADICION**, como **un elemento mas de la misma lista `evidencia`**, **sin clave nueva de
  esquema** y **sin tocar ni tachar el texto viejo**. Es la via de la gemela `OP-L-01` en
  la vuelta 166, que el **acta 71, seccion 6, adjudicacion 3** adjudico con las palabras
  **NO ES PARADA**.
- **QUE TIENE QUE DECIR, Y LAS TRES COSAS SON OBLIGATORIAS:**
  1. que la `evidencia[3]` nombra `LECTURAS_DIRIGIDAS.md`, y que ese documento trae
     **0** veces el literal `reparto por acto` y **0** menciones de `OP-L-03`. **Mide las
     dos cifras tu, no las copies de aqui.**
  2. que el reparto por acto vive en **`docs/plan/OP_L_03_LECTURAS.jsonl`** y
     **`docs/plan/OP_L_03_TRIANGULOS.jsonl`**, **nombrados los dos**, cada uno con **sus
     bytes exactos leidos del instrumento** (`P.2`: bytes exactos, nunca redondeados, KB
     solo entre parentesis y detras del byte).
  3. **Y LA CIFRA QUE NO PUEDE FALTAR, PORQUE SIN ELLA LA CORRECCION PROMETE DE MAS:**
     la `evidencia[2]` promete **55 pares en 29 actos** y `OP_L_03_LECTURAS.jsonl` trae
     **14 actos distintos**. **Escribe la cobertura real con su fecha de corte.**
     Recuentala tu. Una evidencia corregida que prometa mas de lo que existe es
     exactamente lo que **LA RUTA QUE PROMETE PRUEBA ES CIFRA** vino a cazar.
- **GUARDA OBLIGATORIA, Y ES LA MISMA QUE USO LA 201 PARA `OP-I-01`:** mide contra HEAD
  que **1 sola linea** de `OPERACIONES.jsonl` difiere (la **43**), que de esa ficha cambia
  **1 sola clave** (`evidencia`), que los **3** elementos viejos siguen **identicos y en su
  orden**, que su `estado` entra y sale igual, y que **0 de las 71 fichas** mueven
  `estado`. **Y corre la guarda DOS VECES**: la segunda tiene que sellar **crecimiento 0**.

## TAREA 2: `OP-L-02` CONTRA EL CRITERIO DE HECHO, AHORA QUE SU CLAUSULA 1 ESTA MEDIDA

**No la cierres tu.** Lo que se pide es **lectura medida**, y si de ella sale que la ficha
esta cumplida **se propone con su evidencia y lo adjudica el auditor**.

- **LO PRIMERO, Y SIN CLONAR NADA:** corre **importandolos**, no copiandolos,
  `scripts/loop/vuelta169_tarea5_cobertura_op_l_02.py` y
  `scripts/loop/vuelta170_tarea5b_veredicto_op_l_02.py`. **Ninguno de los dos escribe
  ficheros** (compruebalo antes, como hizo el auditor) y **ninguno se toca**. Sella sus
  salidas con nombre de esta vuelta.
- **MIDE LAS TRES CLAUSULAS CONTRA EL CRITERIO DE HECHO** de
  `docs/plan/08_VERIFICACION.md`, **citado por linea**. Las clausulas se citan por
  **linea 42 mas indice**.
- **LA CLAUSULA 2 TIENE UNA TRAMPA YA MEDIDA Y NO LA REDESCUBRAS:** el instrumento la da
  `NO CUMPLIDA` porque diffea contra `46208790`, un HEAD de la vuelta 170. **Vuelve a
  medirla contra el HEAD de apertura de TU vuelta**, leido de tu propio sello y no
  tecleado, y **publica las dos lecturas juntas** con la discrepancia declarada. **No
  arregles el instrumento: la moratoria lo prohibe.**
- **SI LAS TRES CLAUSULAS QUEDAN CUMPLIDAS, PROPONLO Y NO LO CIERRES.** Escribe la
  propuesta con su evidencia entera y **deja el `estado` quieto**.

## TAREA 3: `OP-L-01` CONTRA EL CRITERIO DE HECHO, Y EL HUECO DE LA VIGENCIA

**Adjudicada por el acta 201 en su `4.8`.** Sus **cuatro pruebas de cobertura estan
cubiertas** y el auditor las reprodujo las cuatro. **Eso es PRESENCIA, no CALIDAD**, y por
eso no se cierra.

- **MIDELA CONTRA EL CRITERIO DE HECHO** de `docs/plan/08_VERIFICACION.md`, citado por
  linea, con su `verificacion` citada por **linea 41 mas indice**.
- **Y MIDE EL HUECO QUE LA 201 NOMBRO Y NADIE HA MEDIDO:** la **TABLA VIVA DE LOS PUROS**
  de `docs/BANCO_DE_TEXTOS.md` (linea **938**) declara literalmente **`vigente al puesto
  1157`**, y el marcador de hoy vale **3388**. **Recuenta las dos cifras tu**, y mide
  **cuantas filas de esa tabla siguen en pie al corte 3388 y cuantas no**, con el
  resolutor delante por `P.1` si el conteo toca ids. **Si el hueco pide mover una clase,
  NO la muevas: mover una clase es del RECOMPUTO.** Nombralo y para ahi.
- **PROPON, NO CIERRES.**

## TAREA 4: LOS REGISTROS. `R.63` Y `R.64`, LAS DOS MAS VIEJAS DE LA DEUDA

**Adjudicada por el acta 201 en su `4.9`: la deuda son 8 actas seguidas, las 173 a 180, y
se pagan DE LA MAS VIEJA A LA MAS NUEVA, DOS POR VUELTA.** Va **detras** del trabajo de
plan y nunca delante: la moratoria dice que **el trabajo es el plan hasta agotarlo**.

- **`R.63` para el acta 173 y `R.64` para el acta 174**, en `docs/PENDIENTES.md`.
- **NINGUN LECTOR NUEVO.** Los que el computo necesita **se importan**, como hizo la 201:
  `siguiente_libre`, `R84.claves_entrecomilladas`, `R94.caidas_propias_entrecomilladas`,
  `R92.caidas_por_lead_heredado` y `R92.titulo_de_la_entrada`. Tus ficheros de computo
  llevan **prefijo de guion bajo**, fuera del censo y fuera de la nomina.
- **ACOTA CADA ACTA EN ESTA VUELTA** (lineas de inicio y fin, contadas hoy) y publica el
  reparto: adjudicaciones, hallazgos, preguntas, caidas del auditor y caidas del ejecutor.
- **SI EL REPORTE ARCHIVADO DE ESA VUELTA NO EXISTE, NO LO FABRIQUES.** Declara la
  ausencia medida con `os.path.isfile` y `os.path.getsize`, y usa la vara que el acta 201
  dejo escrita en su `4.7`: el numeral de preguntas sale de **las claves `P.n` nombradas
  en los titulos `4.n` del acta**, y **la entrada declara que uso esa vara**. Declarada
  asi, **no es caida**. El reporte de la **173** es uno de los dos que faltan en el rango
  168 a 199: **compruebalo, no lo supongas**.
- **CIERRA CON LA SERIE MEDIDA:** entradas, colisiones, huecos y siguiente libre. Al abrir
  esta vuelta vale **54 entradas, 0 colisiones, 0 huecos, siguiente libre R.63**.

## LO QUE NO ENTRA, NOMBRADO PARA QUE LA 203 NO LO REDESCUBRA

- **La reparacion del HEAD envejecido** de `vuelta170_tarea5b_veredicto_op_l_02.py`
  (acta 201, `4.2`). Es codigo: **auditoria integral**.
- **El cierre del turno del auditor que se reabre despues de declarar las clases**
  (acta 201, `5.1`). Es codigo: **auditoria integral**.
- **Los dos arneses que el censo ve y la nomina congelada no tiene** (acta 201, `5.3`):
  `vuelta197_tarea2_mutacion_orden_del_turno.py` y
  `vuelta199_tarea1_mutacion_guardas_revividas.py`. **La poda y el alta se deciden en la
  auditoria integral.**
- **Las dos paradas que levanto la 200** y que el acta 200 adjudico en su `4.1` y su
  `4.2`. **No se vuelven a levantar.**
- **Podar la nomina**, **mover una clase**, **cerrar una ficha por tu cuenta** y **que
  hacer con las filas `B` del archivo**.

## EL CIERRE

Cierra tu propio reporte con `scripts/loop/cerrar_reporte.py` y sus cuatro piezas: si
cierra, la racha de cierres pasa a **4**. Marca tus discutibles **antes de saber si
aciertas**. Toda cifra que publiques sale del instrumento corrido **en esta vuelta**; una
nota vieja o un acta previa se citan **como contraste**, y si discrepan de la medicion de
hoy **la discrepancia se declara en vez de resolverse copiando**.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo contradice una
regla vigente, paras y lo traes. No adivines.
