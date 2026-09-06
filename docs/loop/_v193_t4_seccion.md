### TAREA 4. LA CUARTA PUERTA QUE SOBREVIVA AL PROCESO. **CERRADA EN VERDE.**

**a) LA BITACORA Y EL SELLO SOBREVIVEN AL PROCESO**, en el fichero del turno
`docs/loop/_TURNO_DEL_AUDITOR.json`, que **se carga al IMPORTAR el modulo** (no
solo en el CLI: el turno del auditor pasa por `import apertura_del_auditor`) y se
reescribe en cada toque. `apuntar()`, `sellar()` y las dos funciones de clases
persisten; `olvidar_todo()` **tambien borra el fichero**, porque un olvido que
deja la memoria limpia y el disco sucio es un olvido a medias.

**b) `sellar()` CAE EN ROJO SI YA HAY SELLO EN DISCO PARA ESA VUELTA.** La guarda
nueva, `sello_en_disco()`, **va ANTES de `puede_sellar()` a proposito**:
`puede_sellar()` mira la MEMORIA, y la memoria muere con el proceso. **El sello ya
escrito es la unica prueba que sobrevive**, y reescribirlo borra la bitacora que
lo acompanaba.

**c) EL CLI PUEDE DECLARAR LAS CLASES, con `--declarar-clases RUTA --vuelta N`**,
leyendo el sello **de disco** por `puede_declarar_clases_con_sello()`. Sin esto la
cuarta puerta no la podia usar nadie que sellara por CLI, o sea nadie. **Y no se
afloja la guarda vieja:** la de los destapes sigue siendo la de la bitacora, y la
bitacora ahora sobrevive al proceso. Se anade tambien `--olvidar-turno`, que borra
el fichero **y lo dice**: es un acto, no un descuido.

**d) LA FRASE QUE PROMETIA LO QUE NO HACIA YA NO ESTA SOLA EN EL DOCSTRING.** El
literal *"el sello, que es lo que el acta cita como prueba, no se pueda escribir
despues"* **se conserva** (una correccion que tapa lo que corrige no se puede
auditar) y debajo va una seccion nueva que dice **que era falso fuera de un mismo
proceso, con la prueba del auditor citada por su ruta**, que ahora es cierto, y
**que sigue sin poderse**: el fichero del turno se puede borrar a mano (y quien lo
borre empieza limpio, **pero el sello en disco sigue estando y la guarda `b`
muerde igual**); el fichero del turno no sabe de que vuelta es hasta que se sella;
y sigue sin saber si lo leido era del sujeto cuando el archivo se abre por fuera.

**e) EL CASO POSITIVO POR MUTACION, Y ES DE OTRA ESPECIE QUE EL DE LA 192.**
`scripts/loop/vuelta193_tarea4e_mutacion_sello_entre_procesos.py`, salida en
`docs/loop/SALIDA_V193_T4E_MUTACION_SELLO_ENTRE_PROCESOS.txt` (4613 bytes,
**VEREDICTO: VERDE**). **Por que hacia falta uno nuevo y no bastaba el de la 192:
aquel corre todos sus escenarios DENTRO DE UN MISMO PROCESO, y ahi la guarda vieja
SI mordia. El agujero vivia justo en la costura que aquel arnes no cruzaba.** Este
**lanza procesos de verdad con `subprocess`**, que es la unica forma de probar que
el estado sobrevive. Sus mutaciones, todas corridas:

- el proceso 2 **VE** el `REPORTE.md` que apunto el proceso 1, y `puede_sellar()`
  dice **NO**. **Si la bitacora no sobreviviera, entraria vacio y diria SI.**
- el caso que el encargo nombra: tocar un prohibido en un proceso y **en otro
  proceso volver a sellar con el sello ya en disco**. `sellar()` **CAE**, y el
  motivo que publica **nombra el DISCO y no la memoria**.
- el carril `c` **deja declarar clases a un proceso que no sello**, y **CAE sin
  sello en disco**: sin sello no hay sujeto.
- y **el destape sigue quemando entre procesos**: con un `veredictos:destape`
  apuntado en otro proceso, declarar **CAE**.

**Su sujeto esta CONGELADO:** todo se fabrica en un `mkdtemp` y se retira; **no
toca `docs/loop/`, no toca el turno del auditor de verdad** (se comprueba al
cerrar) y **no imprime el nombre del temporal**, que se tapa con
`sin_el_temporal()` incluso cuando se cuela dentro de los informes que el modulo
devuelve. **Corrido dos veces da 4613 bytes y `sha256` `10c2d2d1e9eb06ce` las
dos.**

**Y UNA COSA QUE ESTE ARNES DECLARA EN VEZ DE DISIMULAR:** el sello del bloque `D`
**se monta a mano**, porque el aislador de verdad necesita el archivo de
veredictos y este arnes no lo fabrica ni lo toca. Lo que ahi se prueba es la
guarda de DISCO, y para eso basta con que el fichero del sello exista. Va escrito
dentro de la propia salida.

**f) NO SE CLONO EL FICHERO.** `apertura_del_auditor.py` tiene nombre estable y se
le anadio: cuatro funciones nuevas (`_guardar_turno`, `_cargar_turno`,
`sello_en_disco`, `puede_declarar_clases_con_sello`, `declarar_clases_con_sello`),
dos banderas de CLI y una seccion de docstring. **No hay una version 2.**

**g) SU ARNES DE LA NOMINA RE CORRIDO CON EL PARCHE PUESTO, Y REPRODUCE BYTE A
BYTE.** `vuelta192_tarea4_mutacion_cuarta_puerta.py` corrido **dos veces** con
este parche en el arbol: **4282 bytes y `sha256` `4779fcd04bc5b2da` las dos**,
**exactamente lo que el encargo pide**, con **VEREDICTO: VERDE**. **NO HAY
PARADA.** Y `git status` no deja el fichero del turno tirado: el arnes lo limpia
con `olvidar_todo()`, que es lo que ese metodo hace ahora.
