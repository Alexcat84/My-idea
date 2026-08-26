# PARA ALEXIS: EL BUCLE SE DETIENE POR RACHA DE CAIDAS DE REPORTE (26 ago 2026, vuelta 76, auditor Opus 5)

## EL MOTIVO, EN UNA FRASE

Tres vueltas seguidas (74, 75 y 76) con al menos una afirmacion equivocada en
el REPORTE, y la regla que tu mismo afinaste el 13 ago dice que tres de la
misma especie ya no son ruido sino patron de dictado suelto: **PARADA**.

**LO IMPORTANTE PRIMERO: LOS DATOS ESTAN VERDES.** Esta parada es de higiene
de dictado, no de integridad del catalogo. Todo lo que la vuelta 76 toco esta
verificado al digito por corrida propia mia: las 26 aristas nuevas, la
reversion de la caida de la vuelta 75, las tres correcciones de
`OPERACIONES.jsonl`, el censo de 32 racimos fila por fila, las cuatro cifras
del cierre, la bolsa y sus diez apartados. **CERO caidas de clase y CERO de
cifra publicada en esta tanda: esa racha se rompio y volvio a cero.**

## LO QUE MAS TE INTERESA, Y ES NUEVO

**El remedio que elegiste el 20 ago 2026 no llega hasta aqui.** Aquel dia se
disparo esta misma parada (vuelta 56) y decidiste la opcion (b): *"la cabecera
del reporte se talla por instrumento"*. El instrumento existe y funciona:
`scripts/loop/tallar_cabecera_reporte.py`. Pero lo abri y **lee
`SALIDA_V<N>_MARCADOR_*.txt` y `SALIDA_V<N>_RECOMPUTO_*.txt`**, que son
salidas **del cribado**. La fase 04 no produce ninguna de las dos: anade
aristas, no funde ni recomputa el marcador. El propio reporte lo dice y hace
bien en decirlo (*"No aplica esta vuelta, y la razon queda citada"*).

**Resultado: desde que el bucle entro al tramo mecanico, todas las cifras del
reporte volvieron a ser frases tecleadas.** Y la segunda caida de esta vuelta
es exactamente eso, la misma especie que el `623` que te detuvo en la 56:

> El reporte publica que la vara 9.6.1 dio **13 CONFIRMA y 12 DEJA IGUAL** en
> el tramo 1. **Su propio fichero de salida, contado por mi, dice 14 y 11.** Y
> corriendo esa misma vara con el criterio que el reporte declara (contar solo
> los hijos **vivos**, cosa que el script en realidad no hace: no filtra
> `deprecado` en ninguna linea) sale **12 y 13**. Tres cuentas distintas, y la
> publicada no coincide con ninguna de las otras dos.

No mueve ningun dato (la columna VOLTEA es CERO en las tres cuentas, y las 25
aristas del tramo 1 se quedan las 25 con cualquiera de ellas). Pero es una
cifra que nadie tallo, en una fase donde el tallador no alcanza.

## EL ESTADO EXACTO

- Rama **`pasada-unica`**, HEAD de la vuelta 76 en **`d301ce37`** (esta acta y
  esta parada van en el commit siguiente). Arbol limpio, `origin` igual a
  `HEAD` al empezar la auditoria.
- **Marcador del cribado**, recomputado por mi hoy: **A 551 / B 72 / C 5 /
  D 2.760**, n **3.388**, puestos del 1 al 3.388, **cero huecos y cero
  duplicados**. Sin cambio: la fase 04 no toca el cribado.
- **Grafo**, recomputado por mi hoy: **3.853 nodos, 3.188 vivos, 665
  deprecados**. Enlaces: **8.897** entradas en `nodos_siguientes`, **8.876** en
  `nodos_previos`, **17.773** de suma, **9.520** de union dirigida unica.
- **FASE III, fase 04 (ENLACES), ABIERTA y a medias.** `OP-E-02` **HECHA**
  (cerrada esta vuelta por declaracion, verificada por mi con el instrumento
  re-corrido y salida identica byte a byte). `OP-E-01` **EN PROGRESO**: dos
  tramos leidos (56 pares), **51 aristas escritas** en la fase, y **297
  candidatos limpios sin leer** en la bolsa filtrada de esta vuelta.
- **TODO VERDE por corrida propia mia**: Gate 0 con su ciclo de tres
  (`GATE 0: OK`, cero auto-aristas, cero duplicadas de titulo, alcanzabilidad
  **100,0%** con 3.188 de 3.188 y 85 semillas, cero enlaces rotos), motor
  **25/25**, web **1.030 pasadas y 3 saltadas** en 80 ficheros, `tsc`
  **exitcode 0 y cero lineas**.
- Las cinco fichas bloqueadas por las fusiones de la fase 06
  (`OP-M-03-ENLACES`, `OP-E-04`, `OP-E-05`, `OP-M-01-ESLABONES`,
  `OP-M-01-SEXTO`) siguen bloqueadas y sin tocar, como su remision manda.

## LAS DOS CAIDAS DE ESTA VUELTA, CON NOMBRE

1. **DENTRO del marcado.** El reporte, seccion 4 discutible 2, dice: *"Ninguna
   de las dos aparece en ningun racimo de `RACIMOS_MIEMBROS.jsonl`"*. Medido
   por mi: **`consejo_de_calidad_y_rol_del_director` SI aparece**, en el
   racimo *"Consejo de calidad"* (quality, 3 miembros, veredicto franja 548),
   junto a `consejo_calidad_2` y `consejo_de_calidad`. **Y el propio reporte
   lo habia tabulado bien en su seccion 1.4**: la seccion 1.4 mide una cosa y
   la seccion 4 afirma la contraria del mismo nodo. No mueve dato: comprobe
   que ninguna arista de esta vuelta nace ni muere en ese nodo.
2. **FUERA del marcado.** El `13/12` de la 9.6.1 contra el `14/11` de su
   propio fichero (arriba). Es la que baja el credito de la tanda y obliga a
   releer el tramo al doble.

**Y UNA CAIDA MIA, que declaro con el mismo nombre.** En mi acta de la vuelta
75 escribi que los dos `medicion_servicios` son *"gemelos"*. El cribado habia
leido ese par exacto (**puesto 2493**) y lo fallo **D**. La disposicion que
adjudique sigue en pie por otra via (`OP-S-09` nombra esa familia y es un
renombre con alias, o sea que el id cambia), asi que no se mueve nada; pero la
palabra era mia, la publique sin consultar el veredicto de archivo, y el
reporte de esta vuelta la heredo de mi acta.

## DOS HALLAZGOS DE FONDO QUE TE SIRVEN MAS QUE LAS CAIDAS

**1. LA VARA BUENA YA ESTABA EN CASA Y NADIE LA USABA EN ESTA FASE.** El
reporte discutia si el **sufijo numerico** de un id basta para aplazar una
arista. Fui a `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` (que es fuente de verdad
por `AUDITOR.md` seccion 0) y **el cribado ya habia leido esos pares**:

| par | puesto | clase | que se hizo |
|---|---:|:---:|---|
| `eliminacion_causas_error_2` contra `_4` | 2557 | **A** (repite) | descartada, bien |
| `mejora_calidad_crosby` contra `concepto_programa_catorce_pasos` | 2868 | **D** | escrita, bien |
| `capacidad_de_proceso` contra `capacidad_de_proceso_2` | 2779 | **D** | escrita, bien |
| `planificacion_estrategica_despliegue` contra `_2` | ninguno | **nunca leido** | descartada por prudencia, bien |

**Las cuatro disposiciones aciertan; el criterio publicado, no.** El sufijo
acierta por casualidad en tres de cuatro y **habria borrado una arista buena**
en el cuarto (el ejecutor no aplico su propio criterio, y menos mal). Lo
adjudique por cita y sin doctrina nueva: **manda el veredicto del cribado
cuando existe; el sufijo solo opina cuando no hay veredicto.**

**2. LA GUARDA QUE YO MISMO ADJUDIQUE TIENE UN AGUJERO CON NOMBRE.** El filtro
`P.9.1` cruza los candidatos contra los campos `eliminar` y `superviviente` de
las operaciones pendientes. **`OP-S-09` tiene `nodos: []`, `eliminar: []` y
`superviviente: null`**: sus **53 familias y 125 nodos vivos** viven en prosa,
en `05_SANEO.md` y en la `nota` de la ficha. **El filtro no puede verla
jamas.** Por eso tres de los cuatro descartes del tramo 2 hubo que
argumentarlos a mano.

## LO QUE SE NECESITA DE TI

1. **Decidir el remedio del dictado para el tramo mecanico.** Cuatro caminos,
   y la decision es tuya:
   - **(a)** Relanzar tal cual con la racha a cero.
   - **(b)** **Extender el tallador a la fase 04** (es la que ataca la causa,
     y es la continuacion natural de lo que ya decidiste el 20 ago): que toda
     tabla del reporte de una fase mecanica se talle de ficheros de salida, no
     se teclee. Las dos caidas de la racha 74-76 son frases tecleadas.
   - **(c)** Una regla mas barata y casi igual de eficaz: **toda tabla del
     reporte cita el fichero del que sale, y el ejecutor la reconstruye
     contando ese fichero antes de publicarla.** La caida del `13/12` la habria
     cazado sola.
   - **(d)** Cambiar el modelo del ejecutor. Lo pongo por completitud, no
     porque lo recomiende: en dos vueltas seguidas el ejecutor Sonnet 5 no ha
     cometido **ni una** caida de clase ni de cifra publicada, y en esta ha
     marcado cinco discutibles honestos, uno de los cuales (el D4) destapo un
     criterio flojo suyo que el mismo puso a revision. El problema medido esta
     en el dictado del reporte, no en el trabajo sobre el dato.
   **Mi recomendacion: (c), y (b) si quieres cerrarlo del todo.**
2. **Visto bueno para llevar a `OPERACIONES.jsonl` la nomina de `OP-S-09`**,
   o al menos su lista de ids, para tapar el agujero del hallazgo 2. Toca el
   alcance de una ficha del plan, asi que no lo hago yo.
3. **Visto bueno para las tres correcciones declaradas** que el encargo de
   reanudacion llevaria (seccion siguiente, TAREA 1). Ninguna borra texto
   viejo.
4. **Nada mas.** No hay doctrina nueva pendiente de escribir, no hay dato
   torcido, y las seis fusiones de la fase 06 siguen enrutadas donde tu las
   dejaste el 26 ago.

## COMO RETOMAR

Relanza el bucle con este primer encargo (lo dejo escrito para que la vuelta
de reanudacion lo copie a `PROMPT_SIGUIENTE.md`):

- **TAREA 1, los registros y las correcciones declaradas.** (1.1) Registrar
  las dos caidas de reporte de la vuelta 76 con su nombre, y la mia de la 75.
  (1.2) Corregir en `REPORTE.md` la frase del discutible 2 sobre
  `RACIMOS_MIEMBROS.jsonl`, con el texto viejo delante y sin reescribirlo, y
  con la fila de la seccion 1.4 citada al lado. (1.3) Corregir
  `scripts/loop/vuelta76_relectura_9_6_1.py`: o filtra `deprecado` de verdad,
  o su docstring y el reporte dejan de decir *vivos*; y re-publicar la tabla
  **contada del fichero de salida**, sea cual sea la cifra que salga. (1.4)
  Anadir a la etiqueta del instrumento de `OP-E-02` su definicion: *miembros
  con nodo vivo TRAS RESOLVER ALIAS*, porque 38 de los 171 estan deprecados y
  solo llegan a vivos por esa via.
- **TAREA 2, la relectura al doble del tramo 2** (la manda `AUDITOR.md`
  seccion 1.2 porque la segunda caida cayo fuera del marcado), **y con la vara
  que esta parada encontro**: cruzar las 26 aristas del tramo 2 contra
  `INTRA_DOMINIO_VEREDICTOS.jsonl` y publicar, par a par, si el cribado ya
  habia leido ese par y con que clase. Cualquier par que el cribado haya
  fallado **A** y este escrito, se revierte con correccion declarada.
- **TAREA 3, el tramo 3 de `OP-E-01`**, recalibrando la bolsa antes de leer
  (el grafo se movio otra vez), con el filtro `P.9.1` corrido antes de leer
  nada, y con el criterio adjudicado: veredicto del cribado primero, sufijo
  solo cuando no hay veredicto.
- **Con el freno nuevo delante:** la racha de reporte vuelve a cero al
  relanzar, pero la regla de las tres seguidas sigue viva; y la de clase o
  cifra publicada esta en **CERO**, no en una.

El acta completa de la vuelta 76 esta en `docs/loop/ACTA_AUDITOR.md`
(verificacion al digito, ciega de los cinco discutibles, adjudicaciones y
metrica de credito). `PROMPT_SIGUIENTE.md` queda **VACIO** como la parada
manda.

DECISION DEL FUNDADOR (26 ago 2026): remedio c como regla inmediata (toda tabla se cuenta
de su fichero), con la extension del tallador (opcion b) como ESCALADA AUTOMATICA si la
racha de reporte vuelve a DOS; visto a la nomina de OP-S-09 en su ficha; visto a las
correcciones declaradas de la TAREA 1; sin cambio de modelos. La racha vuelve a cero y la
fase 04 sigue.
