### TAREA 2. LOS DOS INSTRUMENTOS DE PROCESO

**2.a EL AISLADOR DE LA CIEGA** (adjudicacion 6.1, la bloqueante; nace de la
`CAIDA 1` del acta 169, que es la **segunda vuelta seguida** en que un auditor
quema su sujeto de ciega). Nace `scripts/loop/aislador_de_ciega.py`, con
**nombre estable y sin numero de vuelta**, como `tallar_cabecera_reporte.py`,
`verificar_apertura_sellada.py` y el archivador de abajo.

**LO QUE HACE, EN SU ORDEN, QUE ES LO QUE IMPORTA:** (1) exige un **criterio
escrito** (`--criterio`) y sin el no corre, y lo copia literal a los **dos**
ficheros para que despues no se pueda discutir por que se eligieron esos pares;
(2) elige con selectores deterministas (dominio, clase, banda, rango, muestra
con semilla via `random.Random`, asi que la eleccion se reproduce); (3) escribe
la salida ciega con **solo** `puesto_intra`, `nodo_a`, `nodo_b` y los pasos de
los dos nodos; (4) escribe el destape (`clase`, `razon`) **en otro fichero**;
(5) **antes de escribir nada** pasa la guarda de fuga, y si algo se cuela **no
escribe ninguno de los dos**.

**LA DECISION DE DISENO QUE HACE QUE ESTO FUNCIONE, Y NO ES DE ESTILO:** la
salida ciega **se construye campo a campo desde una LISTA BLANCA**
(`CAMPOS_CIEGOS`), no copiando la fila y quitando lo prohibido. **Una lista
negra se queda ciega ante un campo nuevo del archivo; una lista blanca no.**

**CASO POSITIVO POR MUTACION, y es exactamente el que el acta pide.**
`scripts/loop/vuelta170_tarea2a_mutacion_aislador.py`, salida
`docs/loop/SALIDA_V170_T2A_MUTACION_AISLADOR.txt`, **exit 0**: **24 casos, 24
pasan, 24 caen al mutar el esperado**. El caso central **ensancha la lista
blanca** con `razon`, con `clase` y con **los dos**, y exige que la guarda
muerda **3, 3 y 6** fugas respectivamente. **El parametro `campos` existe en la
firma para esto**: para poder mutar la lista sin tocar el fichero real ni el
disco. **Cero escrituras**: filas y pasos fabricados en memoria.

**Y SE CORRIO EN VIVO SOBRE EL ARCHIVO DE VERDAD**, salida
`docs/loop/SALIDA_V170_T2A_AISLADOR_DEMO.txt`: 3.388 filas leidas, **6 pares
elegidos** (puestos 1174, 1482, 1757, 1768, 1922, 3190), **0 fugas**, ciega de
8.364 bytes y destape de 6.344 bytes en ficheros distintos. **El destape no se
abrio**, y `grep -c "clase\|razon"` sobre la ciega da **0**. El criterio escrito
dice con todas sus letras que **no es el sujeto de ninguna ciega en curso**,
para no quemarle nada al auditor con una demostracion.

**2.b EL ARCHIVADOR DE REPORTES** (adjudicacion 6.4; resuelve el `D.1` y la
pregunta `P.1` del reporte de la 169 **sin doctrina nueva**). Nace
`scripts/loop/archivar_reporte.py`. **No borra nada, no cambia ninguna regla y
no crea sede nueva: le da nombre de fichero a la que ya existia, que era el
commit.**

**LA DECISION DE DISENO, Y ES LA QUE HACE QUE ESTO SE PUEDA CORRER TARDE:** el
texto **se lee de git** (`git show <commit>:docs/loop/REPORTE.md`), **no del
arbol de trabajo**. Un archivador que copiase el arbol solo podria correr en la
ventana exacta anterior al esqueleto, y **si esa ventana se pierde el reporte
queda sin archivar para siempre**. Leyendo de git, **cualquier reporte de
cualquier vuelta pasada se puede archivar en cualquier momento**, que es justo
lo que hacia falta para archivar hacia atras el de la 168.

| que se archiva | de que commit | bytes | lineas | sha256 (LF) |
|---|---|---:|---:|---|
| `docs/loop/reportes/REPORTE_V169.md` | `a77b206f` | 43.586 | 724 | `262f8409de09...` |
| `docs/loop/reportes/REPORTE_V168.md` | `1eec382f` | 31.263 | 530 | `068fe39fb36a...` |

**LAS DOS COPIAS SE COTEJAN CONTRA EL BLOB DE GIT CON `sha256sum`: IDENTICAS
LAS DOS.** Y las cifras de la 168 (31.263 bytes, 530 lineas) **coinciden con las
que el propio mensaje de `1eec382f` publica**, que es una vara independiente.

**EL ORDEN IMPORTA Y SE RESPETO:** el archivador corrio **antes** de que el
esqueleto sobrescribiera `docs/loop/REPORTE.md`. Tallar antes de archivar habria
dejado el reporte de la 169 otra vez sin mas sede que su commit.

**CASO POSITIVO POR MUTACION**, salida
`docs/loop/SALIDA_V170_T2B_MUTACION_ARCHIVADOR.txt`: cuatro mutaciones y un
control. (1) `--vuelta 168` apuntando al commit del reporte de la 169: **CAE**,
exit 1. (2) `--vuelta 169` apuntando al de la 168: **CAE**, exit 1. (3) destino
existente con contenido **distinto** sin `--forzar`: **CAE**, exit 1. (4) la
misma con `--forzar`: **VERDE**, y restituye el `sha256` original. Control: el
par correcto sigue **VERDE**, exit 0.

**UNA CORRECCION DECLARADA POR ADICION DENTRO DE ESA MISMA SALIDA:** la
comprobacion final original murio por una ruta `/tmp` que python no ve en
Windows. **El parrafo no se borra** y la comprobacion se rehace debajo con
`sha256sum`, que ademas es mejor vara que la que fallo.

**LO QUE ESTA TAREA NO HACE, DICHO PARA QUE NADIE LEA DE MAS:** el archivador
**no se enchufa solo** a ninguna secuencia de apertura. Esta vuelta lo corrio a
mano en su apertura. **Automatizarlo dentro del esqueleto seria decidir por el
fundador** sobre el orden de la apertura, y el encargo no lo pide. Queda como
**DISCUTIBLE `D.2`**.
