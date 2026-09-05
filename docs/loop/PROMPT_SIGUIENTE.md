# ENCARGO DE LA VUELTA 179 (ejecutor). FASE III, EJECUCION. Rama `pasada-unica`.

**Commitea y pushea lo pendiente en la rama activa antes de tocar nada.**

**ESTA VUELTA NO ES DE BATERIA.** La cadencia esta adjudicada en el acta 176 punto
7.8 y reconfirmada en el acta 178 punto 11: **la proxima vuelta de bateria es la
181**, y la 179 y la 180 cierran su seccion 9 con el **HUECO DECLARADO Y MEDIDO**,
con su nombre, sus bytes medidos y su atribucion, **las tres juntas**. Un hueco
declarado no es un hueco escondido.

**EL TOPE SIGUE EN CINCO** por `AUDITOR.md` 6.2, cuyo disparador se cumplio en la
177 y la 178 confirmo entregando cinco. **Este encargo trae cinco, y la TAREA 1
es BLOQUEANTE.**

**ABRE EL REPORTE AL EMPEZAR**, con sus cinco filas vacias, como manda
`EJECUTOR.md` 1 (EL REPORTE ABRE CON LA VUELTA), y **mide el desfase del
calibrado DENTRO DEL BLOQUE DE APERTURA**, antes de la primera operacion. Desde
la 178 una columna de apertura medida al cierre es caida que ACUMULA.

---

## TAREA 1. LOS REGISTROS, LAS CORRECCIONES Y **LA OPERACION DE CODIGO DE LA ESCALADA**. ES BLOQUEANTE.

**(a) LA CORRECCION DECLARADA DE LA CAIDA DE LA 178.** El reporte de la 178
publica, en la prosa de su 1.e, *"16 casos, los 16 pasan y los 16 CAEN"* para
`vuelta178_tarea1e_mutacion_higiene.py`. **Son 18**, y lo dice el propio fichero
que esa frase cita, `docs/loop/SALIDA_V178_T1E_MUTACION.txt`, que yo corri y
volvi a medir. **El reporte archivado `docs/loop/reportes/REPORTE_V178.md` NO se
retoca**: dice lo que se publico. La correccion se declara en el reporte de ESTA
vuelta, con las tres cifras al lado (la publicada, la del fichero y la de tu
re-corrida de hoy).

**(b) LA OPERACION DE CODIGO DE LA ESCALADA, Y ES LA PIEZA QUE MANDA EN ESTA
TAREA.** `AUDITOR.md` 1.2 obliga a encargarla cuando la racha de reporte llega a
dos, y llego (acta 178, seccion 6). **El alcance ya lo autorizo el fundador el 29
ago 2026** (`paradas/2026-08-29-racha-y-escalada-omitida-DECISION.md`), literal:
*"toda tabla y toda cifra del reporte en fases mecanicas se genera contando su
fichero de salida"*. **Lo que se construyo fue la cabecera y las tablas; lo que
falta es la PROSA que cita un fichero, que es donde han caido las dos ultimas.**

Escribe la guarda **dentro de `scripts/loop/cerrar_reporte.py`**, junto a sus
hermanas y con la misma forma que ellas: **una funcion PURA** que reciba el texto
del reporte y un lector de ficheros, para que su arnes pueda tumbarla sin tocar
el repo. Lo que tiene que hacer:

1. Encontrar en el reporte **toda frase que publique una cifra de casos de un
   arnes Y nombre un fichero `SALIDA_V*.txt` en la misma frase o en la misma
   linea**. La forma que hay que cazar es la que fallo: *"N casos, los N pasan y
   los N CAEN"* junto a su ruta.
2. **Leer ese fichero y sacar su cifra propia** (la linea `CIFRA casos que CAEN:
   X de Y` o su hermana `CIFRA casos: X | pasan: Y`).
3. **CAER EN ROJO nombrando la linea, la cifra publicada y la del fichero**, si
   no calzan. **Si el fichero citado no existe o mide cero bytes, tambien es
   ROJO**, por la letra del 5 sep sobre la ruta que promete prueba.
4. **Quedan fuera los bloques cercados**, por el mismo motivo que la guarda de la
   pareja: ahi va pegada la salida cruda y una cita que se retoca deja de ser una
   cita.

**CON SU CASO POSITIVO POR MUTACION, y el caso que lo decide todo es este:** un
reporte fabricado que publica 16 junto a un fichero fabricado que dice 18 tiene
que salir **ROJO nombrando las dos cifras**; el mismo con 18 y 18 tiene que salir
**VERDE**. **Y corre la guarda nueva sobre `docs/loop/reportes/REPORTE_V178.md` y
publica lo que salga**: si caza la caida de la 178 en su primera corrida, dilo con
esas palabras; si no la caza, la guarda no sirve y hay que arreglarla antes de
seguir.

**(c) LOS DOS ARNESES DESTAPADOS ENTRAN EN LA NOMINA** (acta 178, adjudicacion
7.9). `vuelta150_2d_simular_op_c_05.py` y `vuelta160_tarea3b_caso_positivo.py`
entran en `VIEJAS` de `scripts/loop/verificar_mutaciones_viejas.py`. **La regla
que lo manda es la del propio fichero desde la vuelta 148** y **la nomina no se
poda** (`AUDITOR.md` 6.1). Entra tambien **todo arnes que esta vuelta escriba**,
en su misma vuelta, como vienen haciendo las ultimas. **Publica la cuenta entera
con su resta comprobada**, como la 178 hizo en su 1.a: censo, nomina, fuera de la
nomina, invisibles al censo. **Esto va ANTES de la 181 para que el rojo que la
178 anuncio no llegue a existir.**

**(d) EL CORTE DEL DENOMINADOR** (acta 178, adjudicacion 7.2, por `banco 9.21`).
Toda cifra de la nomina que se publique lleva **su corte al lado** (el commit o el
momento en que se midio), no solo el fichero del que se cuenta. El motivo esta
medido: la 178 publico **15 de 92** siendo verdad, y al cerrar la vuelta eran **15
de 98**, porque el denominador crece dentro de la propia vuelta. **Cablealo donde
se genera la cifra, no en una frase.**

---

## TAREA 2. `OP-L-03`: SE LEEN LOS DIEZ PARES REALES DE LOS ACTOS SIN LEER

**El backlog ya esta re-medido y lo verifique yo:** `backlog_l03_resuelto.py` sale
VERDE, los dos caminos calzan en los 40 actos, y de los **73 pares** que el
instrumento da quedan **18 reales**, de los cuales **8 los leyo la 177** y
**quedan 10 en los 34 actos que nadie ha mirado**. **Esos diez son el trabajo de
esta tarea.**

- **Los diez se leen con la vara del banco**, par por par, y **cada uno con su
  veredicto y su razon escrita en `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` solo si
  el par TIENE puesto en la cola**. **Si no lo tiene, NO se inventa un puesto:**
  su clase y su razon van al registro de `OP-L-03`
  (`docs/plan/OP_L_03_LECTURAS.jsonl`), en el campo
  `clases_de_los_pares_por_leer`, que es donde la 177 las puso y donde son
  trazables. **Esa distincion es la del punto 7.8 de mi acta y no se difumina.**
- **El marcador no se toca si no hay puesto**, y si lo hay, **se recomputa del
  archivo** y se publica con sus cuatro clases (`banco 9.10`).
- **Cierra cada acto con su forma escrita**, como la 177 hizo: la figura, su
  cobertura (`banco 9.26`) y lo que queda.
- **Y trae la cifra al lado, siempre las dos:** pares del instrumento y pares
  reales, sin borrar la vieja.

---

## TAREA 3. LOS DIECISEIS TRIANGULOS SE PUBLICAN PARTIDOS POR SU FUENTE

**Adjudicado en el acta 178, punto 7.8, por `banco 9.10` por extension natural, y
NINGUNA CLASE SE MUEVE.** La medicion que lo motiva es mia y la repito para que
la reproduzcas antes de escribir nada:

| | cuantos |
|---|---:|
| lados con clase leida de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` | **38** |
| lados con clase leida de `docs/plan/OP_L_03_LECTURAS.jsonl (vuelta 177)` | **10** |
| triangulos con los TRES lados con veredicto en el archivo | **8** |
| triangulos con al menos un lado SIN veredicto en el archivo | **8** |
| de esos, aquellos en que el lado sin veredicto es el `D` | **6** |

- **`scripts/loop/vuelta178_tarea3_anotar_triangulos.py` publica la cifra
  PARTIDA**, no solo el 16: cuantos descansan enteros en el archivo y cuantos se
  apoyan en un lado de fuera, **y nombra los seis en que el lado de fuera es el
  `D`**, que es el lado que hace que el triangulo sea un triangulo.
- **`docs/plan/OP_L_03_TRIANGULOS.jsonl` gana un campo por fila** que diga si el
  triangulo es recomputable entero del archivo. **El campo `fuente_de_la_clase`
  por lado NO se toca: ya esta bien y es lo que permitio levantar esto.**
- **CERO VEREDICTOS MOVIDOS**, comprobado por `sha256` antes y despues como la
  178 hizo.
- **Con su caso positivo por mutacion** sobre un registro fabricado: un triangulo
  con sus tres lados en el archivo y otro con el `D` fuera tienen que caer en
  casillas distintas, y mutar el esperado tiene que tumbar el caso.

---

## TAREA 4. LAS QUINCE DEL SUJETO CONGELADO SE JUZGAN, UNA A UNA, Y NO SE CABLEA NADA TODAVIA

**Adjudicado en el acta 178, punto 7.3: primero se juzgan, despues se cablea, y
no al reves.** La guarda sale en ROJO con **15 entradas** (7 `SUJETO VIVO`, 8 `NO
DECIDIBLE`) y las quince las verifique yo, nombre a nombre, contra la salida del
ejecutor: son las mismas.

- **Por cada una de las quince, un veredicto escrito con su prueba:** o el arnes
  **de verdad abre un fichero vivo de la campana** y hay que congelarle el sujeto,
  o **lo nombra sin abrirlo** y basta con que lo declare, o **es un caso declarado
  legitimo** y se anota por que.
- **Registro propio, no prosa:** `docs/plan/SUJETO_CONGELADO_VEREDICTOS.jsonl`,
  una fila por arnes, con el nombre, el veredicto, el fichero que abre y la
  evidencia (la linea del codigo).
- **NO se arregla ningun arnes en esta vuelta y NO se cablea la guarda al rojo
  global de la bateria.** Se juzga y se escribe. **El cableado se decide con los
  quince veredictos delante, no antes.**
- **NADA se borra de la nomina** (`AUDITOR.md` 6.1).

---

## TAREA 5. LO QUE NO ENTRA Y NO SE PIERDE, CONTADO EN VOZ ALTA

Ninguna de estas se toca aqui, y las cinco se nombran **con su medicion** (existe,
bytes en disco y normalizados a LF) para que no se caigan:

1. **La segunda sede de la clausula 4.4** en `REPORTE_V172.md:535`.
2. **El docstring de `paso0_archivar_anterior.py`**, que sigue hablando de LA
   VUELTA ANTERIOR cuando la maquina pregunta por EL REPORTE QUE VA A PISAR.
3. **La guarda que falta en la dependencia del `D.4` de la 174**: el esqueleto
   clona en vez de importar y nada avisa si el fichero del que se clono
   desaparece.
4. **El grano del tope de 10 minutos**, que se mide **EN LA 181** con el reloj de
   esa corrida y **no se re-elige a ojo antes**.
5. **La convencion de bytes**, que es del fundador y lleva seis actas subiendo.
   **Sube como pendiente, no como problema:** el remedio provisional (publicar
   siempre las dos) ya es instrumento y esta vuelta salio a coste cero.

---

## EL CIERRE, EN SU ORDEN Y ENTERO

- **Gate 0 en su ciclo completo y en su orden en las dos puntas**, nunca
  `run_phase1` suelto: `run_phase1.py --reaplico-curaduria`, `etiquetas_de_cara.py
  --aplicar`, `sync_assets_web.py`, `git diff HEAD --numstat -- dataset/ web/
  engine/`, `engine/run_all_tests.py`, `npx tsc --noEmit`, `pnpm test`.
- **La guarda de `dataset/` verde antes de cada commit.** `dataset/` no se toca en
  ninguna de las cinco tareas.
- **La cabecera se talla y se pega, no se teclea**, con
  `tallar_cabecera_reporte.py --fase04 --vuelta 179`.
- **La seccion 9 cierra con el HUECO DECLARADO Y MEDIDO**, con sus tres piezas.
- **`cerrar_reporte.py` talla el cierre**, y esta vuelta corre **con la guarda
  nueva de la TAREA 1.b dentro**.
- **Archiva tu propio reporte en tu misma vuelta**, en
  `docs/loop/reportes/REPORTE_V179.md`, leido de git y no del arbol, y publica su
  cotejo byte a byte. **Serian cuatro seguidas.**
- **Marca tus discutibles ANTES de saber si aciertas**, y escribe tus caidas
  propias con su nombre.

Cero guiones largos y cero guiones medios. Deja correr el hook. Si algo
contradice una regla vigente, paras y lo traes. No adivines.
