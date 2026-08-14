# PARA ALEXIS, 14 ago 2026 (vuelta 26): la fase 01 esta parada en el muro del indice semantico y en dos huecos de doctrina

Escrito por el auditor (Fable 5) tras verificar entero el reporte de la vuelta 26 del
ejecutor (Opus 5). El acta completa es la VUELTA 26 de `docs/loop/ACTA_AUDITOR.md`; las
mediciones, en `docs/loop/SALIDA_ACTA26_AUDITOR.txt`.

## EL ESTADO EXACTO

- **Rama `pasada-unica`**, HEAD `e3de957c` mas el commit de esta acta, arbol limpio y
  empujado. FASE 0 CERRADA. FASE II cerrada y verificada desde la vuelta 20.
- **FASE 01:** `OP-F-01` **EJECUTADA, HECHA y verificada por el auditor** (la clase de
  seis manda, cero pasos alterados, la cifra de 18 reescrita como 30 en sus dos sedes).
  `OP-F-02` y `OP-F-03` **a medias, con la mitad documental hecha y verificada**
  (fronteras publicadas, destinos decididos por lectura, los 21 leidos con veredicto, y
  las dos fuentes corregidas). **Las cuatro `OP-F-04` sin ejecutar.**
- **Marcador n 3.388** (A 583, B 89, C 7, D 2.709, cero huecos), **grafo 3.835 nodos
  (3.521 vivos, 314 deprecados), 16.800 enlaces**, 71 operaciones en LISTA. **Gate 0 y
  las tres suites en verde, corridos enteros por el auditor** (motor 24 de 24, web 1.030
  pasadas y 3 saltadas, tsc limpio; las dos copias del grafo en el blob de HEAD).
- **La relectura ciega del auditor coincidio en todo lo marcado:** las fronteras de los
  tres de Mollick (con el bloque de OCHO, no nueve), el destino NODO PROPIO de los tres
  bloques, y los 21 de Hugos veredicto por veredicto (12 si, 2 no, 7 de la tercera
  clase).

## LOS TRES MOTIVOS DE LA PARADA

### 1. CREDENCIALES AUSENTES (la seccion 4 de AUDITOR.md la nombra entera)

Crear un nodo pone `Gate 0` en rojo: el chequeo *todo nodo ACTIVO tiene vector en el
indice semantico* es de cero tolerancia, y el unico instrumento que fabrica vectores
(`scripts/build_semantic_index_voyage.py`) exige `VOYAGE_API_KEY`, que esta fuera del
repo mientras el bucle corre, por regla tuya y bien guardada. El ejecutor lo reprodujo
con un nodo de prueba (nunca commiteado) y el auditor verifico el chequeo en el codigo,
la credencial ausente y el indice (voyage-4-lite, 512 dimensiones, 3.521 ids exactos).

**CORRECCION DEL AUDITOR AL ALCANCE QUE EL REPORTE PUBLICA:** las operaciones que piden
crear nodo son **CINCO, no siete, y las cinco son de la fase 01**: `OP-F-02` (los tres
destinos son nodo propio) y las cuatro `OP-F-04` (su fallback escrito es nodo propio).
El barrido del ejecutor caso `OP-D-08` y `OP-D-09` por NEGACIONES (*"ningun alias se
crea"*, *"NO SE CREAN OPERACIONES NUEVAS"*): esos dos destejidos declaran cero
movimiento de grafo y **NO estan bloqueados por el muro**. El muro es de la fase 01.

### 2. DOCTRINA NUEVA NECESARIA (dos casos, ninguno adjudicable por extension)

- **El metodo de destino dentro de una familia.** `P.3` resuelve hasta la familia; elegir
  el miembro no esta escrito. Toca a las cuatro `OP-F-04` (13 mas 13 mas 13 mas 4 bloques
  contra la familia de Horowitz, 88 vivos de fuente unica) y al reparto de `OP-F-03`
  contra la subfamilia Hugos. Es la misma especie que tu resolviste para `OP-F-02`
  escribiendo la regla de destino por lectura; a las cuatro tandas les falta esa misma
  regla, y su fallback (nodo propio) vuelve al motivo 1.
- **La tercera clase de `OP-F-03`.** Siete nodos (`bundle_ideas`,
  `modelo_hibrido_agile_stage_gate`, `principio_calidad_mvp`,
  `procesamiento_paralelo_con_espirales`, `propuesta_gasto_capital`,
  `reduccion_tamano_de_lote_batch_size`, `schedule_management_plan`) traen material de
  Hugos DE VERDAD, pero de su parte de COMO SE CONSTRUYE UN SISTEMA, no de cadena de
  suministro. Corregir la fuente borraria una atribucion cierta; repartir a la
  subfamilia de cadena los meteria donde no son. La operacion solo tiene esos dos
  desenlaces: falta el tercero, y esa pluma es tuya. La lectura por nodo con su frontera
  ya esta publicada en `01_FUENTES.md`, verificada por lectura ciega del auditor.

Y una adjudicacion que ya quedo hecha en lo adjudicable: **la premisa de `P.3` (el caso
Hugos como "otro tema, la poda era segura") falla nodo a nodo en al menos cuatro de los
doce** (`gestion_inventario`, `ratios_eficiencia_inventario`,
`criterios_seleccion_proveedores`, `analisis_tco_roi_b2b`; el auditor suma un quinto
candidato, `gestion_cuentas_por_cobrar`). Por la propia regla de `P.3`, en esos el
REPARTO ES OBLIGATORIO y la poda deja de ser opcion. Lo unico que falta ahi es el
destino (el hueco de arriba).

### 3. CONTRADICCION DE PLAN, MEDIDA

`docs/plan/08_VERIFICACION.md` manda a la vez **Gate 0 verde entre fases** y **el
reindexado AL FINAL, despues de mover ids** (con su motivo escrito: reindexar antes deja
el indice apuntando a la era anterior). El dia que una operacion cree un nodo, las dos
reglas no pueden cumplirse a la vez. Ninguna regla de correccion existente resuelve esto
sin reescribir una de las dos, y eso es decision de casa.

## LO QUE SE NECESITA DE TI

1. **Como se indexan los nodos que la pasada cree.** Las tres salidas sobre la mesa,
   sin que el bucle elija: (a) dar la credencial al bucle para reindexar dentro de la
   pasada; (b) permitir durante la fase III un Gate 0 con ESE UNICO chequeo en rojo,
   DECLARADO en cada reporte, con el reindexado al final como el plan ya manda; (c)
   partir la pasada en dos, ahora lo que no crea nodos y despues lo que si.
   **Recomendacion del auditor, para que la decidas y no para decidirla:** la (b) es la
   unica que no saca un secreto de la casa y ademas disuelve la contradiccion del motivo
   3 (deja UNA regla: reindexar al final y declarar el rojo esperado), pero reescribe
   una regla vigente del Gate y por eso es tuya.
2. **La regla de destino por lectura para las cuatro `OP-F-04`** (la gemela de la que ya
   escribiste para `OP-F-02`), que sirve tambien para el reparto de `OP-F-03`.
3. **El desenlace de la tercera clase de `OP-F-03`** (por ejemplo, un tercer desenlace
   escrito en la operacion: el bloque de sistemas se separa hacia la subfamilia de
   sistemas de Hugos o forma nodo propio; pero la forma exacta es doctrina tuya).
4. **Un aviso de credito para el proximo encargo:** van DOS tandas seguidas con caida de
   reporte (la 24 y la 26; en la 26 fueron tres con nombre: el alcance de "siete" que
   son cinco, las "nueve salidas" que son once, y una adjudicacion de la vuelta 25
   citada como pendiente). A la tercera tanda seguida el protocolo manda parada por
   patron de dictado suelto.

## COMO RETOMAR

Escribe tus decisiones como correcciones declaradas donde viven las reglas (la regla de
destino en las notas de las cuatro `OP-F-04`, el desenlace tercero en `OP-F-03`, la
decision de indexado en `08_VERIFICACION.md` o en el banco del plan, como hiciste con
`P.17` y con la regla de `OP-F-02`), y relanza el bucle. El encargo de la reanudacion
sale del acta: TAREA 1, los registros pendientes (la linea de la vara del comando 3
contra el HEAD que trae el commit, mas los que tus decisiones abran); TAREA 2, el corte
de `OP-F-02` con sus tres destinos ya leidos, el reparto o poda de `OP-F-03` por `P.3`
remedido, y las cuatro `OP-F-04` con su regla nueva; despues, el modo continuo sigue
solo. Las lecturas ya publicadas (fronteras de Mollick, los 21 de Hugos, los diez del
racimo) NO hay que rehacerlas: estan verificadas dos veces.

DECISION DEL FUNDADOR (14 ago 2026): indexado por opcion B estricta; P.18 destino por
lectura de objeto; tercera clase de OP-F-03 a familia Hugos-sistemas. La fase 01 sigue.
