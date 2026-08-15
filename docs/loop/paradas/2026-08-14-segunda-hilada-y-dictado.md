# PARA ALEXIS, 14 ago 2026. La fase 01 avanzo de verdad (19 nodos cortados, 20 bloques repartidos) y la parada tiene DOS motivos: la segunda hilada del muro y un patron de dictado que ya sono tres veces

Escrito por el auditor (Fable 5) tras verificar entero el reporte de la vuelta 27 del
ejecutor (Opus 5). Acta completa en `docs/loop/ACTA_AUDITOR.md`, vuelta 27.

## LOS DOS MOTIVOS, cada uno en un parrafo

**1. LA SEGUNDA HILADA DEL MURO.** Tu opcion B abrio `Gate 0` (rojo declarado del indice
para los ids que la pasada crea), pero el MISMO chequeo vive en dos sedes mas que tu
decision no nombra y que yo lei en codigo: `engine/test_aviso_curaduria.py` (fixture que
mide `activos - ids` contra el repo real) y `.githooks/pre-commit` (aborta el commit si
la suite del motor esta en rojo, sin excepcion escrita). Consecuencia medida y
reproducida: **con un nodo nuevo en el arbol, NINGUN commit entra al historial**, ni uno
que no lo toque. Y como el caso por defecto de `P.18` es nodo propio, la cerradura no
bloquea una operacion: **bloquea el fallback de toda la fase 01**. Decidir si tu rojo
declarado vale en esas sedes es pluma tuya: es la misma especie de decision que el acta
26 te mando (reescribir lo que una guarda acepta), y el remedio mecanico exige decidir
donde vive la lista de ids declarados, quien la escribe y como muere al cierre, que
ninguna pagina dice. El ejecutor no salto el hook, no toco el guardian, no devolvio el
`.env` y no falseo ningun verde: la parada es limpia.

**2. PARADA POR PATRON DE DICTADO SUELTO.** La regla afinada del 13 ago manda parar a la
tercera tanda seguida con caida de reporte. Van tres: la 24 (una), la 26 (tres) y la 27
(dos). Y las dos de hoy REINCIDEN en especies ya nombradas con nombre en el acta 26:
*"treinta y tantas salidas"* que son 51 contadas (la especie de las "nueve" que eran
once), y *"la pregunta 5, que sigue sin respuesta"* cuando fue adjudicada en el acta 25
y RE-CERRADA en el acta 26 con la frase *no se re-pregunta*. Importa decirlo entero: en
las CIFRAS la vuelta 27 fue limpia (cero caidas de clase, cero de cifra publicada; el
marcador, el censo, el indice, las nominas y las fronteras se me reprodujeron al
digito). El patron no esta en la medicion: esta en afirmar el estado del registro sin
mirarlo.

## EL ESTADO EXACTO, todo verificado por mi hoy

- Rama `pasada-unica`, HEAD `ca0c82e5` mas el commit de esta acta, todo en `origin`,
  arbol limpio.
- `Gate 0` OK (exit 0) y suites verdes corridas enteras por mi: motor 24 de 24, web 80
  ficheros con 1.030 pasadas y 3 saltadas, `tsc` cero lineas. Ciclo del grafo cerrado:
  71 etiquetas, las dos copias en el blob `6773e389`, byte identico a HEAD.
- Marcador: n 3.388, A 583 (17,2), B 89, C 7, D 2.709, cero huecos. Grafo: 3.835 nodos,
  3.521 vivos, 314 deprecados, 16.800 enlaces. Indice: 3.521 de 3.521, cero sin vector.
  Operaciones: 71, todas LISTA, cero dependencias rotas.
- Fase 01: `OP-F-01` HECHA; `OP-F-04-RAC` HECHA y verificada; `OP-F-03` PARCIAL, 15 de
  19 (adjudicado: no se declara HECHA hasta que los cuatro nodos propios existan);
  `OP-F-02` ejecutada, verificada y DESHECHA por el muro, con plan sellado; `COL`, `HOR`
  y `WEI` sin tocar (39 bloques, nominas ya medidas: Coleman 83 y 68, Horowitz 102 y 88,
  Weinberg 80 y 67).
- Cuatro planes sellados en `docs/loop/PLAN_V27_*.json` que se aplican con un comando el
  dia que la cerradura se abra.
- Relectura ciega de esta acta: nueve de fondo, siete coinciden, DOS discrepan y las dos
  DENTRO del marcado del ejecutor (`economia_circular` que yo mando a nodo propio, y
  `superioridad_producto_beneficios` que yo mando al otro nodo FAB). Van a relectura
  conjunta en la reanudacion; ninguna toca el muro salvo que la primera se confirme.

## LO QUE SE NECESITA DE TI

**1. LA SEDE DEL ROJO DECLARADO (desatasca la fase entera).** Tres salidas sobre la
mesa, sin que el bucle elija:

- (a) **La credencial**, para reindexar dentro de la pasada: la cerradura se abre sola y
  los planes sellados se aplican en un comando. Saca un secreto de la casa mientras el
  bucle corre.
- (b) **Extension escrita de la opcion B a la sede que sea**, con este remedio mecanico
  como propuesta para que lo decidas tu: una lista versionada de ids declarados (por
  ejemplo `docs/plan/INDICE_ROJO_DECLARADO.jsonl`, cada linea con id, operacion que lo
  creo y fecha), que SOLO la pasada escribe; el chequeo de `Gate 0` y el fixture de la
  suite restan exactamente esos ids y los imprimen uno a uno, y CUALQUIER otro id sin
  vector sigue siendo rojo que para; al cierre de la fase III la lista debe quedar VACIA
  con el reindexado hecho y Gate 0 entero en verde, que es lo que tu correccion 2 ya
  exige, asi que la excepcion no puede llegar viva a la auditoria ni al merge.
- (c) **Partir la pasada**: ahora todo lo que no crea nodos (las tres tandas de
  `OP-F-04` tienen bloques con destino a miembro que no tocan el muro), y los nodos
  propios cuando haya credencial.

**Mi recomendacion, para que la decidas y no para decidirla: la (b).** Es la unica que
mantiene el secreto fuera del repo Y deja las tres sedes vigilando cualquier id que no
este declarado, y su clausula de cierre ya esta escrita por ti. La (c) es compatible con
la (b) como orden de trabajo dentro de la reanudacion.

**2. EL PATRON DE DICTADO (que quede curado, no solo contado).** El aviso corrio delante
del encargo y aun asi reincidio en las dos especies avisadas. Propuesta mecanica, para
tu pluma en `EJECUTOR.md` si la adoptas: **toda afirmacion sobre el estado del registro
(actas, adjudicaciones, preguntas previas, conteos de ficheros) se escribe con la
medicion del dia al lado (la linea del acta leida, el conteo corrido), o no se
escribe.** Es la misma cura de siempre en esta casa: el remedio es mecanico, no de
atencion. Si prefieres otra cura (cambiar el modelo del ejecutor, o un chequeo del
reporte previo al commit), es tuya.

## COMO RETOMAR

Escribe tu decision de sede como correccion declarada donde vive la regla (la opcion B
en `08_VERIFICACION.md`), y la cura del dictado donde corresponda (`EJECUTOR.md`), y
relanza el bucle. El encargo de la reanudacion sale del acta, vuelta 27, y ya esta
perfilado:

- **TAREA 1, registros:** la entrada `HUGOS-SISTEMAS` en el inventario (adjudicacion 7,
  citando tu correccion del 14 ago); la relectura conjunta de las dos discrepancias
  (seccion 2 del acta: el ejecutor verifica contra el grafo y decide con la vara, con
  correccion declarada y recomputo si voltea); y el registro de las adjudicaciones 1 a 3
  donde correspondan.
- **TAREA 2, el trabajo segun tu decision:** si (a) o (b), aplicar los planes sellados
  (`OP-F-02` y los cuatro bloques de `OP-F-03`) con sus guardas y despues las tres
  tandas restantes de `OP-F-04` por `P.18`; si (c), primero los bloques a miembro de
  `COL`, `HOR` y `WEI` y los nodos propios quedan sellados esperando credencial. El modo
  continuo sigue solo desde ahi.

Las lecturas ya publicadas y verificadas dos veces (fronteras, destinos releidos a
ciegas en esta acta salvo las dos discrepancias) NO hay que rehacerlas.

`docs/loop/PROMPT_SIGUIENTE.md` queda VACIO a proposito: el bucle esta detenido
esperando tu decision.

DECISION DEL FUNDADOR (14 ago 2026): sede del rojo por opcion B extendida a TODAS las
sedes con la lista INDICE_ROJO_DECLARADO; patron de dictado curado con la regla LA CITA
LLEVA SU LINEA en EJECUTOR.md; sin cambio de modelo. La fase 01 sigue.
