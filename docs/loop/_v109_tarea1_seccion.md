## VUELTA 109, TAREA 1: LOS REGISTROS DEL ACTA 108

### 1.1 LOS DOS VUELCOS SIN DECLARAR (87 y 91), CAIDA DEL EJECUTOR, DE
EXPEDIENTE CON REFLEJO EN EL REPORTE

Cruzados a mano por el auditor los seis ficheros de veredicto puesto a
puesto: cinco puestos cambiaron de veredicto entre barridos en toda la
historia (87, 91, 109, 123, 145). Tres SI se declararon (109, 123, 145, dos
de ellos por el propio ejecutor, dentro de la fila o de la linea de resumen
del fichero que los revierte). Dos NO: el 87 (v105 SATELITE -> v108
OBJETO, ni en la fila, ni en el reporte, ni marcado DISCUTIBLE) y el 91
(v105 SATELITE -> v108 OBJETO, marcado DISCUTIBLE pero descrito como
"podria leerse SATELITE con otra vara", cuando ya se leyo asi, con esta
misma vara, por un instrumento de la casa). Tabla de los cinco vuelcos de
la historia:

| puesto | vuelta vieja -> nueva | veredicto viejo -> nuevo | declarado |
|---|---|---|---|
| 87 | 105 -> 108 | SATELITE -> OBJETO | NO, hasta la vuelta 109 |
| 91 | 105 -> 108 | SATELITE -> OBJETO | NO, hasta la vuelta 109 |
| 109 | 106 -> 107 | OBJETO -> SATELITE | SI (resumen del fichero, "nuevo hallazgo") |
| 123 | 106 -> 107 | SATELITE -> OBJETO | SI (fila propia, "ya barrido... y SOSTENIDO") |
| 145 | 106 -> 107 | SATELITE -> OBJETO | SI (fila propia, "revertido... correccion_v107") |

Constancia: NO es caida de clase ni de cifra publicada (ninguna cifra sale
falsa; las dos lecturas enteras de la vuelta 105 ya SOSTUVIERON el 87 y el
91, sin correccion). Por la letra del fundador del 27 ago, NO acumula: la
racha de reporte sigue en UNO y la de cifra publicada vuelve a CERO.
Remedio de esta vuelta: TAREA 2 (instrumento estable
`verificar_vuelco_de_veredicto.py`) y TAREA 2.5 (las dos filas corregidas
de forma aditiva).

### 1.2 EL PRECEDENTE MAL CITADO EN LA FILA DEL 87

La fila vieja del 87 invocaba "el patron del 116", y el 116 dice lo
contrario. El 116 (`metodologia_spin_selling` -> `preguntas_need_payoff`):
"no hay objeto rival compitiendo... todo el contenido sustantivo del paso
vive en el complemento" (el verbo "Prepararse" es intransitivo, sin objeto
propio). El 87
(`emprendedor_como_puesto_de_trabajo` -> `contabilidad_innovacion_pivote`):
"todo el contenido sustantivo del metodo vive en el complemento
instrumental", pero AQUI el verbo "Evalua" SI tiene objeto propio y
distinto ("ese trabajo"). Son formas CONTRARIAS: en el 116 no hay objeto
que dispute el complemento porque el verbo carece de el; en el 87 SI lo
hay. Resuelto por la TAREA 3 de esta misma vuelta: el 87 vuelve a
SATELITE.

### 1.3 EL 64 Y EL 91, LOS DOS CERRADOS

Los dos DISCUTIBLES marcados en el reporte de la vuelta 108, adjudicados
por el auditor sobre los nodos antes de destapar nada, los dos CERRADOS y
los dos a favor del ejecutor.

**El 64** (`clasificar los defectos por gravedad, causa y responsabilidad`):
OBJETO, porque el hijo ejecuta el verbo sobre el objeto directo mismo (su
paso 2 elabora la lista DE DEFECTOS y su entregable es la tabla de esos
defectos); el contra-caso de las tres ordenes coordinadas se cae porque en
el 109 el objeto directo no era lo que el hijo tocaba y aqui SI lo es.

**El 91** (`establecer gates o puntos de decision formales con criterios
visibles de Go/Kill`): OBJETO, con la razon escrita de las DOS maneras.
LA DEL EJECUTOR (reporte de la vuelta 108): "un punto de decision formal
se define por sus criterios; no hay materia propia del objeto que el
complemento deje fuera, distinto del 109". LA DEL AUDITOR (encargo de la
vuelta 109), que llega al mismo sitio por camino distinto: el sintagma
"con criterios visibles de Go/Kill" cuelga del NOMBRE `gates`, no del
verbo (no se establecen gates POR MEDIO DE criterios, se establecen gates
QUE TIENEN criterios), asi que los criterios viven DENTRO del objeto
directo, patron del 102, confirmado por la senal de entregables del
9.6.2.

El 64 y el 91 dejan de estar marcados DISCUTIBLE.

### 1.4 MIS DOS CAIDAS PROPIAS DEL AUDITOR (acta 108, corregidas por el
propio auditor)

**La de ENCARGO:** el encargo de la vuelta 108 nombro "el 147" como
precedente de la via que no toca `direccion_leida`; medido contra el
grafo, el 147 trae `correccion_v99` sobre `direccion_leida` (direccion
anulada), y el precedente real es el 148, que trae `correccion_v99` con
`campo_corregido` "vara (cita)" y el mismo texto de vara, por el mismo
defecto de paso mal casado.

**La de ACTA:** en la mutacion L, `tallar_cabecera_reporte.py --comparar`
empareja por ETIQUETA y no por posicion, asi que intercambiar motor y tsc
no dispara DISTINTA ahi; el acta 107 lo daba por hueco sin serlo. Esta
segunda la corrigio el propio auditor ANTES de publicarla: escribio que el
orden de las filas quedaba sin guarda, fue a MEDIRLO, fabrico la mutacion
M (`docs/loop/_auditor_v108_mut/mM.md`, el REPORTE.md con las filas motor
y tsc intercambiadas) y la corrio contra la OTRA guarda
(`verificar_cabecera_pegada_o_condensada.py --vuelta 108 --reporte`): dio
ROJO EXIT 1 senalando exactamente CUATRO celdas. EL ORDEN SI ESTA
GUARDADO, por la otra guarda.

### 1.5 LA GUARDA DEL ORDEN SI ALCANZA

Salida de la mutacion M (`docs/loop/_auditor_v108_mut/out_mM.txt`): ROJO
EXIT 1 en CUATRO celdas (filas 4 y 6, apertura y cierre, motor y tsc
intercambiados). La M es del auditor desde la vuelta 108 y va en la
corrida de cada vuelta; ya no se anota como hueco lo que la mutacion M ya
prueba que no lo es.

### 1.6 EL CHOQUE DE LAS DOS GUARDAS DE CABECERA, ADJUDICADO POR EL
AUDITOR (acta 108, seccion 2)

`verificar_cabecera_pegada_o_condensada.py` exige que la cabecera sea
IDENTICA a la del tallador; `tallar_veredictos_reporte.py` exigia que cada
palabra de veredicto citara un fichero con veredicto legible, y la fila de
identidad (que el propio `tallar_cabecera_reporte.py` escribe, no
editable) caia en ese cerco sin ser prosa del ejecutor. Adjudicado por el
auditor como CHOQUE ENTRE DOS REGLAS ESCRITAS, no doctrina nueva
(AUDITOR.md 1.3): el cerco de `tallar_veredictos_reporte.py` pesa la PROSA
que el ejecutor escribe, no el texto pegado literal de un tallador.
Remediado en la TAREA 4 de esta misma vuelta: el instrumento corre
`tallar_cabecera_reporte.py` de verdad y excluye del cerco toda linea
IDENTICA a la que ese comando imprime, diciendo cuantas excluye.
