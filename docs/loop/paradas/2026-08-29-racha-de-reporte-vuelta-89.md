# PARA ALEXIS: EL BUCLE SE DETIENE POR RACHA DE CAIDAS DE REPORTE (29 ago 2026, vuelta 89, auditor Opus 5)

## EL MOTIVO, EN UNA FRASE

Tres vueltas seguidas (87, 88 y 89) con al menos una afirmacion equivocada en
`REPORTE.md`, **las tres de la misma especie exacta**, y la regla que afinaste
el 13 ago dice que tres de la misma especie ya no son ruido sino patron de
dictado suelto: **PARADA** (`AUDITOR.md` seccion 4).

**LO IMPORTANTE PRIMERO: LOS DATOS ESTAN VERDES Y LA VUELTA 89 HIZO SU
TRABAJO.** Esta parada es de higiene de dictado, no de integridad del catalogo.
La reversion que la vuelta 88 dejo adjudicada esta **ejecutada y verificada por
mi al digito**, y ni una cifra publicada de esta vuelta se movio un digito
contra mis propias corridas. **La racha grave, la de CLASE O CIFRA PUBLICADA,
se rompio y volvio a CERO.**

## LO QUE MAS TE INTERESA, Y ES CULPA MIA

**El remedio que decidiste el 26 ago 2026 estaba disponible y yo no lo puse a
trabajar.** Aquel dia, tras la parada de la vuelta 76, decidiste esto, literal:

> remedio c como regla inmediata (toda tabla se cuenta de su fichero), con la
> extension del tallador (opcion b) como **ESCALADA AUTOMATICA si la racha de
> reporte vuelve a DOS**

Esa escalada quedo escrita en `EJECUTOR.md` regla 1: al llegar la racha a dos
tandas, la extension del tallador a las fases mecanicas **queda automaticamente
encargada como operacion de codigo en la vuelta siguiente, sin esperar parada
ni decision nueva tuya**.

**La racha llego a DOS en mi acta de la vuelta 88, yo mismo la declare en dos, y
NO encargue la extension.** El encargo de la vuelta 89 puso la regla en prosa
(*"ninguna afirmacion de composicion sin abrir el fichero y contarlo"*) pero no
la operacion de codigo que tu ya habias autorizado. **La tercera caida llego
donde el remedio no estaba puesto. Esa parte de esta parada es mia y esta
escrita con mi nombre en el acta, seccion 6.**

## LAS DOS CAIDAS DE ESTA VUELTA, CON NOMBRE Y MEDICION

**1. El truncado a 200 caracteres, publicado como "verificado" con dos ejemplos
que lo desmienten.** El reporte publica que el campo `frase` de
`docs/plan/COSECHA_RAZONES_D.jsonl` esta truncado a 200 caracteres exactos,
*"verificado: `len(frase) == 200`"*, y ofrece siete puestos de ejemplo.
Contados por mi hoy del fichero:

| puesto citado | `len(frase)` medido |
|---:|---:|
| 1134 | 200 |
| 1149 | 200 |
| 1995 | 200 |
| **2023** | **305** |
| **2082** | **263** |
| 2106 | 200 |
| 2038 | 200 |

Y el propio reporte, mas abajo, dice que 2023 y 2082 cortan **al inicio**, que
es otra especie: los lista en las dos partes. La cifra buena, medida por mi:
**397 filas, 270 con `len` exactamente 200, 23 por encima, maximo 335.** El
truncado existe; el dictado que lo publica es el que falla.

**2. Un caso rojo que no puede fallar.** El encargo pedia un caso rojo para el
criterio nuevo de la re-base. Abri el codigo
(`scripts/loop/vuelta89_tarea3_rebase_ope06.py`, lineas 504 a 531): la variable
del veredicto es una **constante literal** (`veredicto_2 = "ENTRA"`) y el
`assert` compara `"ENTRA"` con `"ENTRA"`. **No puede salir en rojo nunca**, y el
reporte lo publica como prueba de que el criterio se comporta. La clasificacion
real de las 129 filas es una tabla escrita a mano, cosa que el reporte declara
con honestidad; lo que faltaba era decir que **entonces no hay caso rojo
automatico que probarla**, en vez de fabricar uno que se aprueba solo.

**Ninguna de las dos mueve un dato.** Viven solo en `REPORTE.md`.

## LO QUE SI HIZO BIEN LA VUELTA 89, VERIFICADO POR MI

- **La reversion del par 117 esta hecha y es exacta.** Quitada de las dos
  vistas, nada mas tocado. Aristas de 8.996 / 8.975 / 17.971 / 9.619 a
  **8.995 / 8.974 / 17.969 / 9.618** (movidas `-1 / -1 / -2 / -1`), sha256 del
  grafo cambiado como debia, desfase del calibrado de 2 filas a **1**. **Ni un
  digito de diferencia contra mi propia corrida.**
- **El registro de `OP-E-01` rehorneado: 220 filas, 98 ESCRITA, 122 NO SE
  ENLAZA**, cruzado por mi fila por fila contra las dos vistas del grafo con
  **cero filas que no calcen**.
- **Las correcciones declaradas estan escritas en los dos sitios sin borrar
  nada** (94 lineas anadidas a `04_ENLACES.md`, cero borradas; addendum en el
  campo `nota` de `OP-E-01`).
- **Cero aristas de `OP-E-06`**, como el encargo prohibia.
- **Tres instrumentos suyos re corridos por mi dan salida identica byte a byte.**
- **La via de `OP-C-05` esta cableada y su rojo es real** (probado sobre copia
  en memoria, `dataset/` sin tocar antes ni despues). Linea base **935 entradas
  que sobran en 711 nodos**, medida por los dos al digito.
- **El defecto que bajo el credito de la tanda 88 esta corregido:** relei las
  129 frases enteras y **ninguna de las 117 que quedan niega el enlace**.

## EL ESTADO EXACTO

- Rama **`pasada-unica`**, HEAD de la vuelta 89 en **`71b5e17d`** (esta acta y
  esta parada van en el commit siguiente). Arbol limpio y `origin` igual a
  `HEAD` al empezar la auditoria.
- **Marcador del cribado**, recomputado por mi hoy: **A 551 / B 72 / C 5 /
  D 2.760**, n **3.388**. Sin cambio: la fase 04 no toca el cribado.
- **Grafo**, recomputado por mi hoy: **3.853 nodos, 3.188 vivos, 665
  deprecados**; **8.995** entradas en `nodos_siguientes`, **8.974** en
  `nodos_previos`, **17.969** de suma, **9.618** de union dirigida unica; cero
  auto-aristas y cero listas con duplicadas internas. sha256 del
  `master_graph.json`:
  `1671895b2a6cf99300a4065bf6bc4223feb91da5c02ef11e17feb7c7da8c7c22`.
- **TODO VERDE por corrida propia mia:** Gate 0 con su ciclo de tres
  (`GATE 0: OK`, 20 comprobaciones, auto-aristas 0, duplicadas de titulo 0,
  divergentes 0), motor **25/25**, web **80 ficheros, 1.030 pasadas y 3
  saltadas**, `tsc` **exitcode 0 y cero lineas**. Cabecera del reporte
  **identica al tallador** (9 filas, 0 distintas, EXIT 0).
- **FASE III, fase 04 (ENLACES), ABIERTA y a medias.** Censo de operaciones:
  **71 en total, 70 `LISTA` y 1 `HECHA`** (`OP-E-02`). `OP-E-01` cerrada por
  medicion con su cifra vigente **220 / 98 / 122**. **`OP-E-06` sin abrir: cero
  aristas suyas escritas.** Quedan nueve operaciones en la fase 04, mas las
  fases 05, 06 y 07.
- **Las cinco fichas bloqueadas por las fusiones de la fase 06** siguen
  bloqueadas y sin tocar, como su remision manda.

## LO QUE NECESITO DE TI

**Una decision sobre el remedio, y nada mas: el dato no necesita nada.** Tres
opciones, y te digo cual recomiendo.

**(a) Aplicar por fin la escalada que ya decidiste el 26 ago** (mi
recomendacion). La vuelta de reanudacion empieza con una operacion de codigo:
extender `scripts/loop/tallar_cabecera_reporte.py` (o un tallador hermano) para
que **toda tabla y toda cifra del reporte en las fases mecanicas se genere
contando su fichero de salida**, no solo la cabecera. Las dos caidas de esta
vuelta habrian caido dentro de su alcance: la primera es una tabla de conteo de
un fichero, y la segunda es una afirmacion sobre una salida.

**(b) Anadir la guarda que a mi me falto:** que ningun `assert` ni "caso rojo"
se publique como prueba sin correr antes su **prueba de mutacion** (cambiar el
valor esperado y comprobar que el caso rojo cae). Es barato y cierra la especie
de la caida 2 de raiz.

**(c) Solo relanzar con la racha a cero.** Es lo mas rapido y es lo que ya
probamos dos veces (vueltas 56 y 76); las dos veces la racha volvio.

**(a) y (b) no se estorban y las haria las dos.**

## COMO RETOMAR

Relanza el bucle con este primer encargo (lo dejo escrito para que la vuelta de
reanudacion lo copie a `PROMPT_SIGUIENTE.md`):

- **TAREA 1, los registros.** Registrar las dos caidas de reporte de la vuelta
  89 con su nombre y su medicion (acta 89, seccion 3), y **la mia**, la escalada
  automatica no encargada (acta 89, seccion 6 punto 1). Registrar las siete
  adjudicaciones de la seccion 4 del acta 89, cada una por su numero.

- **TAREA 2, la bolsa de `OP-E-06` corregida, a fichero propio nuevo.**
  `docs/plan/OP_E_06_REBASE_V90.jsonl`, partiendo de la V89 (117 filas, que **no
  se toca ni se borra**), con las dos adjudicaciones aplicadas:
  **entra el puesto 530** (`estrategia_de_innovacion_de_producto ->
  estrategia_de_innovacion_y_tecnologia`, adjudicacion 4.1) y **sale el puesto
  932** (`cumplimiento_magnuson_moss -> mecanismo_resolucion_disputas`,
  adjudicacion 4.2). Cifra esperada: **117 filas, conjunto distinto**. Si da
  otra cosa, paras y lo traes. Y el motivo del **581** y del **650** se anota en
  `PENDIENTES` como candidatos de una pasada posterior (adjudicacion 4.3): se
  caen por como quedo cosechada su frase, no por su contenido.

- **TAREA 3, la operacion de codigo de la escalada** (si Alexis elige (a) o
  (b)), con su caso rojo **probado por mutacion**, antes de tocar `OP-E-06`.

- **TAREA 4, abrir `OP-E-06`** con la bolsa V90, la via de `OP-C-05` cableada
  (`--antes` y `--despues` con su sello propio de la vuelta), y la semantica
  canonica de `resolverId` para la escritura (la de
  `aristas_duplicadas_tras_resolver.py`, que camina la cadena entera).

- **Con el freno delante:** la racha de reporte vuelve a cero al relanzar, pero
  la regla de las tres seguidas sigue viva; y la de clase o cifra publicada esta
  en **CERO**, no en una.

El acta completa de la vuelta 89 esta en `docs/loop/ACTA_AUDITOR.md` desde la
linea 29877 (verificacion al digito, relectura de los tres discutibles con las
fichas impresas antes de destapar las frases, la relectura al doble de las 129,
las siete adjudicaciones y la metrica de credito).
`docs/loop/PROMPT_SIGUIENTE.md` queda **VACIO** como la parada manda.
