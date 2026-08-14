# REPORTE del ejecutor del bucle, vuelta 13 (FASE II, TERCERA VUELTA: EL BARRIDO DEL PLAN
ENTERO AL CORTE 3.388, Y EL PASO 2 RELEIDO AL DOBLE)

**Sesion ejecutora (Sonnet 5). Fecha de reloj: 13 ago 2026. Rama activa: `bucle`.** MODO DE CIERRE:
cero reparaciones de nodos. **`dataset/` no se toco ni un byte.** La Fase III (mover nodos de
verdad, rama `pasada-unica`) sigue sin abrir.

## Hash y rutas

- **Hash final de esta vuelta:** ver el commit de este mismo archivo (`git log -1`), por encima del
  commit de contenido.
- **Commits de la vuelta:**
  - `d67ee481` TAREA 1 y TAREA 2.A: la nomina de las 46 SI existe (correccion declarada), `OP-S-10`
    remedida y confirmada como la unica operacion movida entre los dos cortes, barrido de las 35
    operaciones que quedaron fuera, `OP-U-02` recomputada con el criterio del propio plan.
  - este commit: TAREA 2.B, comprobacion de integridad final y este reporte.
- **Rutas tocadas:**
  - `docs/plan/RECOMPUTO_3388.md`: cuatro secciones nuevas al final (TAREA 1, TAREA 2.A, el
    recomputo de `OP-U-02`, TAREA 2.B), ninguna reescribe lo verificado en la vuelta 12.
  - `docs/plan/OPERACIONES.jsonl`: dos lineas editadas, `OP-S-10` y `OP-U-02`. Las otras 67, sin
    tocar (verificado por diff: solo 2 de 69 lineas cambiaron).
  - `scripts/loop/barrido_vuelta13.py`: instrumento nuevo esta vuelta, de solo lectura, modelado
    sobre `scripts/plan/recomputo_3388.py`.
  - `docs/loop/REPORTE.md`: este archivo, reescrito entero.

## Marcador del archivo, sin cambio esta vuelta

**3.388.** Esta vuelta no lee cribado nuevo: recomputa el plan sobre el marcador que ya estaba
cerrado. Las 583 A, las 335 componentes, los 280 CERRADOS y los 55 ABIERTOS **no se tocaron y no se
volvieron a medir** (verificado y en verde por la vuelta 12, per instruccion explicita del
encargo).

---

## TAREA 1: dos verificaciones y su cierre

### 1. La nomina de las 46 SI existe

**CORRECCION DECLARADA sobre dos frases falsas del `docs/loop/REPORTE.md` de la vuelta 12** (commit
`77ffde4c`, seccion LO QUE NO SE MIDIO): decia que la nomina de las 46 confirmadas "sigue sin estar
escrita como lista en ningun sitio" y que faltaban "las 10 restantes". **Las dos son falsas.**

**Verificado con instrumento propio antes de escribir.** La nomina vive en
`docs/FICHA_SUBFUSION_GRADIENTE.md`, tabla "Las 128, con su fila y su veredicto" (lineas 3651 a
3780). Comando: parseo de las 128 filas. Resultado: **128 filas, 128 ids distintos, 46 confirmadas
y 82 falsas**, exacto contra la fila de totales que la propia ficha ya publicaba (linea 3640).

**La aritmetica correcta: de las 46 confirmadas, QUINCE tienen A vigente al corte 3.388 y TREINTA Y
UNA no.** El 10 de la vuelta pasada salia de restar mal 46 menos 36 (36 es la interseccion de las
128 CITAS contra las 854 nodos con A, no el numero de confirmadas dentro de ella). El detalle
completo, con las dos listas citadas linea a linea, vive ahora en `docs/plan/RECOMPUTO_3388.md`
(seccion TAREA 1) y se repite abajo en TAREA 2.B.

### 2. `OP-S-10`, la unica operacion del plan que se mueve entre los dos cortes

**Remedido con `scripts/loop/barrido_vuelta13.py` (script nuevo) antes de escribir, tal como pedia
el encargo.**

| | corte 2.117 | corte 3.388 |
|---|---:|---:|
| pares internos leidos de la nomina de 31 | 7 | 17 |
| de esos, clase A | 1 | 2 |
| actos que tocan la nomina | 3 | 6 |
| nodos de la nomina dentro de un acto | 4 | 8 |

**Exacto contra la medicion del auditor, las cuatro cifras.** Verificado ademas contra el universo
entero: de las 43 operaciones del plan con nomina de dos nodos o mas, `OP-S-10` es LA UNICA que
cambia; las otras 42 (incluidas las 28 ya verificadas la vuelta pasada) se remidieron esta vuelta
como control cruzado y dieron CERO cambios.

`OPERACIONES.jsonl` se edito: `OP-S-10` reescribe su nota con las dos cifras (banco 9.21, el corte
viejo no se borra), la nota de orden entre fases (saneo corre despues de fusiones, `00_INDICE.md`),
y el precedente citable `OP-F-03`.

**DISCUTIBLE MARCADO** (detalle completo en `docs/plan/RECOMPUTO_3388.md`): la frase del encargo
"seis de sus treinta y un nodos habran sido absorbidos cuando le llegue el turno" NO se pudo
reproducir con instrumento propio. Verificado que cero de los 31 nodos aparecen hoy en el campo
`nodos` de ninguna operacion FUSION o DESTEJIDO ya LISTA, asi que no hay fusion YA DECIDIDA que
absorba a ninguno todavia. Lo unico medible es que 8 de los 31 caen dentro de un acto que algun dia
se fundira, y de esos SOLO el par `elaboracion_fdd`/`preparar_fdd` es interno a la propia nomina de
`OP-S-10`. Se trae la cifra de seis tal como la dio el encargo, sin reescribirla ni descartarla.

---

## TAREA 2.A: el barrido se completa sobre las 69

**Universo: las 35 operaciones que quedaron fuera de la vuelta pasada** (`OP-F-01` a `OP-F-04-RAC`,
las doce `OP-S-*`, `OP-D-07`, `OP-E-01`, `OP-E-02`, `OP-E-04`, `OP-E-05`, las cinco `OP-C-*`, las
dos `OP-A-*`, `OP-V-01`, `OP-I-01`, `OP-L-01`, `OP-L-03`).

**17 operaciones con nomina de dos nodos o mas** (mas `OP-D-07`, con una sola): medidas con
`scripts/loop/barrido_vuelta13.py`. **CERO cambian salvo `OP-S-10`.** Tabla completa en
`docs/plan/RECOMPUTO_3388.md`.

**18 operaciones sin nomina comparable**: razonamiento de por que su cifra publicada no depende del
corte del cribado intra-dominio (herramientas, codigo, ids, campo fuente, reglas de decision,
doctrina, lecturas ya ejecutadas). **DOS EXCEPCIONES declaradas, no forzadas a la regla:**

- **`OP-I-01` SI depende del corte.** Su nota (11 ago 2026) dice que cuatro dominios (`quality`,
  `health_safety`, `risk_management`, `seguridad_digital`) no habian entrado al cribado intra.
  **Verificado: los cuatro SI tienen pares leidos hoy** (quality 844, health_safety 192,
  risk_management 106, seguridad_digital 27, contra 0 de los cuatro al corte 2.117). No se
  recomputo el inventario entero (fuera del alcance de esta TAREA, que es sobre `OPERACIONES.jsonl`):
  **queda como DISCUTIBLE MARCADO y PENDIENTE DE DOCTRINA.**
- **`OP-L-03` no se pudo verificar en ningun sentido.** Su cifra ("55 pares por leer, en 29 actos")
  describe un backlog fechado alrededor del 12 ago 2026, y el cribado avanzo de 2.117 a 3.388 desde
  entonces (con CINCO actos que estaban abiertos cerrando en ese tramo, medido en la vuelta 11). No
  hay en el repositorio una lista estructurada de los 55 pares con la que recomputar sin inventar.
  **Marcado DISCUTIBLE y PENDIENTE DE DOCTRINA.**

### `OP-U-02`: "el recomputo no abre 48 fusiones: abre 44", recomputada con dos criterios

**Criterio del propio plan** (dueno en mesa o destejido no cuenta como fusion que el recomputo
abra): de los 55 abiertos al corte 3.388, OCHO ya tienen dueno (portafolio en `OP-M-01`, customer
discovery y customer validation en `OP-M-05`, brainstorming en `OP-D-04`, ab_testing en `OP-D-03`,
junta asesora en `OP-M-04`, voz del cliente en `OP-D-02`, pivote en `OP-M-03`). **Al 3.388: no abre
55, abre 47** (la vieja cifra del 2.117, 44, no se borra).

**Criterio ANCHO** (que alguna nomina de CUALQUIER operacion toque algun miembro): **11 de los 55
tocan, 44 no tocan**, exacto contra la medicion del auditor. **Que este segundo 44 tambien de 44 sea
coincidencia queda declarado**: son dos cuentas distintas sobre dos universos de tamano distinto.
Entre los 44 del criterio ancho estan las dos componentes nuevas (15 de `health_safety`, 10 de
`quality`) y el de ocho del ciclo crear medir aprender, que a diferencia de los otros cuatro grandes
NUNCA tuvo dueno en ninguna operacion.

`OPERACIONES.jsonl` se edito: `OP-U-02` agrega esta correccion a su nota, sin borrar el 44 viejo.

### Comprobacion de integridad

| comprobacion | antes | despues |
|---|---:|---:|
| operaciones (lineas) | 69 | 69 |
| ids unicos | 69 | 69 |
| ids duplicados | 0 | 0 |
| `depende_de` rotos | 0 | 0 |
| `bloquea_a` rotos | 0 | 0 |

**Lineas exactas cambiadas: 2 de 69** (`OP-S-10`, `OP-U-02`). Ninguna otra linea se toco.
`dataset/` no se toco ni un byte. No se ejecuto ninguna operacion. No se creo la rama
`pasada-unica`. No se crearon operaciones nuevas.

---

## TAREA 2.B: el paso 2, releido al doble, sobre las 46

**Efecto de la regla del credito (acta vuelta 12, seccion 4): el paso 2 se corre sobre las 46
confirmadas enteras, no solo sobre las 36 con A.**

1. **La nomina de las 46, citada linea a linea, cero se reescriben.** Lista completa en
   `docs/plan/RECOMPUTO_3388.md`, TAREA 2.B punto 1.
2. **Partida en dos: QUINCE con A vigente** (`ab_testing_optimizacion`, `blueprint_de_experiencia`,
   `brainstorming_divergente`, `customer_journey_mapping`, `future_scenarios_planning`,
   `key_partners_hypothesis`, `optimizacion_embudo_get_customers`, `plan_de_adquisicion_acquire`,
   `principio_calidad_mvp`, `producto_minimo_viable`, `producto_unico_superior`,
   `propuesta_gasto_capital`, `seleccion_ceo_fundador`, `split_testing_experimentos_ab`,
   `voz_del_cliente_voc`, todas con dueno en `OP-D-01` a `OP-D-06`) **y TREINTA Y UNA sin ella**
   (lista completa en `docs/plan/RECOMPUTO_3388.md`).
3. **Para las 31, dos preguntas: VEINTINUEVE aparecen en la nomina de alguna operacion** (todas
   `OP-F-*`, decisiones de FUENTE, no de fusion) **y DOS no aparecen en ninguna**
   (`lienzo_modelo_negocio`, `planificacion_recoleccion_datos`).
4. **Las 31 son costuras confirmadas SIN gemelo vigente, o sea destejidos que NO son curas
   acopladas.** Lista declarada de las dos sin dueno alguno en `docs/plan/RECOMPUTO_3388.md`. **NO
   se crearon operaciones nuevas: queda para que el auditor adjudique con la lista delante.**
5. **Ningun nodo se releyo.** Los 46 veredictos son copia literal de
   `docs/FICHA_SUBFUSION_GRADIENTE.md`; lo medido esta vuelta es solo la interseccion por id
   resuelto contra el conjunto de nodos con A y contra las nominas de operaciones.

---

## LO PEDIDO COMO BONUS, SI SOBRABA PRESUPUESTO: las tres nominas en prosa de `OP-L-02`

**Medido, sin escribir nada en `docs/plan/`.** Las tres nominas ya estan documentadas en
`docs/plan/LECTURAS_DIRIGIDAS.md` (lineas 28-41) y en la nota de `OP-L-02` en `OPERACIONES.jsonl`:

| nomina | nodos | pares posibles | leidos al 3.388 |
|---|---:|---:|---:|
| cuadrantes de mercado | 6 | 15 | **15 (cobertura completa)** |
| ecuacion de valor | 5 | 10 | **10 (cobertura completa)** |
| bloque humano de la supervision de la IA | 10 (particion provisional 5+4+1) | 45 | **10 leidos** (cobertura MEZCLADO, no completa: falta releer si alguna A cruza los bloques) |

**Las tres estan cerradas por LECTURA DIRIGIDA, no por el cribado intra-dominio**, asi que el
avance del marcador de 2.117 a 3.388 no las toca (son el mismo universo "fuera de cola" que
`OP-L-02` ya declaro estructuralmente inmune al corte). Cuadrantes y ecuacion de valor llegaron a
cobertura completa en la segunda tanda de `OP-L-02` (8 y 5 lecturas respectivamente); el bloque
humano de la IA tiene sus 10 pares internos leidos pero la particion contra el bloque del mapa
(35 pares mas) sigue sin leerse, tal como ya declaraba `OP-F-02`. **Confirma, no cambia, lo que
`OP-L-02` ya tenia escrito.**

---

## LO QUE NO SE MIDIO ESTA VUELTA

- **La membresia definitiva de OP-S-10** (cuales de sus 31 nodos terminan absorbidos): no se pudo
  medir porque las fusiones de los seis actos que tocan su nomina no estan decididas en ningun
  documento del plan (discutible marcado arriba).
- **El recomputo del inventario completo de `OP-I-01`** (323 entradas, la cifra de "221 actos" que
  tambien esta desactualizada contra los 335 de hoy): fuera del alcance de esta TAREA, que es sobre
  `OPERACIONES.jsonl`. Se declaro la desactualizacion puntual (los cuatro dominios), no se
  recomputo el documento entero.
- **La nomina estructurada de los 55 pares de `OP-L-03`**: no se encontro en ningun archivo del
  repositorio (solo prosa sin ids linea por linea), asi que no se pudo verificar si su backlog sigue
  vigente al 3.388.
- **El lote de cinco lecturas del sales roadmap, la cola de relectura post fusion, el criterio del
  forastero, las lecturas de acto entero de P.5, y las 387 filas de LECTURAS DIRIGIDAS**: fuera de
  esta vuelta por instruccion explicita del encargo.
- **El bloque del mapa de la supervision de la IA contra el bloque humano** (35 pares cruzados): no
  se leyo, tal como ya declaraba `OP-F-02` como PROVISIONAL; el bonus de esta vuelta solo confirmo
  la cifra existente, no la amplio.

---

## DISCUTIBLES MARCADOS, para la relectura ciega del auditor

1. **La cifra "seis de sus treinta y un nodos habran sido absorbidos" de `OP-S-10` (TAREA 1.2) NO
   se pudo reproducir con instrumento propio.** Es el discutible mas importante de la vuelta: se
   trajo la cifra del encargo sin reescribirla ni descartarla, con la medicion completa de por que
   no se pudo verificar (cero fusiones ya decididas que absorban a esos nodos). Si el auditor tiene
   una fuente que el ejecutor no encontro, este es el punto exacto donde traerla.
2. **`OP-I-01` esta desactualizada mas alla de lo corregido aqui** (la cifra de "221 actos" dentro
   de su propia nota, y probablemente otras de sus 323 entradas de inventario que dependen del
   estado del cribado). Se corrigio solo el punto que el encargo permitia medir sin salirse del
   alcance de `OPERACIONES.jsonl`; el resto queda pendiente de un encargo propio.
3. **`OP-L-03` es una excepcion sin verificar, no una excepcion confirmada.** A diferencia de
   `OP-I-01` (donde se pudo medir la desactualizacion exacta), aqui no hay con que medir: se declara
   la imposibilidad en vez de forzar una reasignacion de "no depende del corte" que no se pudo
   comprobar.
4. **El criterio "del propio plan" para `OP-U-02` (dueno en mesa o destejido) se construyo por
   interpretacion del texto de la propia nota de `OP-U-02`** ("van a mesa... o a destejido..."), no
   esta escrito como regla formal en el banco del plan. Es la lectura mas literal posible del texto
   existente, pero el auditor deberia confirmar que "otra fase" significa exactamente "mesa o
   destejido" y no algo mas amplio (por ejemplo, cualquier operacion que ya fije un superviviente).
5. **La tabla de 17 operaciones con nomina de TAREA 2.A reusa integramente el script de OP-S-10**,
   corrido una sola vez sobre las 43 del plan entero: no se corrio una segunda vez de forma
   independiente para las 17 de esta vuelta en particular. El riesgo es bajo (mismo instrumento,
   mismos datos, sin intervencion manual entre medio) pero se declara para que quede escrito.
