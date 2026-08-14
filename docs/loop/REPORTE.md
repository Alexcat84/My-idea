# REPORTE DE LA VUELTA 21 . Ejecutor: Opus 5 . 14 ago 2026

**Encargo:** los cinco registros del acta de la vuelta 20 (TAREA 1) y la FASE 0 DE CODIGO entera
(TAREA 2), en la rama `pasada-unica`, con la FASE III recien abierta.

> **EL TITULAR, y va primero porque cambia lo que esta vuelta pudo hacer: LA TAREA 1 ESTA ENTERA Y
> VERIFICADA. LA TAREA 2 QUEDO EN PARADA EN SU PRIMER PASO, POR LA CONDICION QUE EL PROPIO ENCARGO
> ESCRIBIO.** El Gate 0 corrido tal cual movio `dataset/metadata/master_graph.json`, que es
> exactamente el caso en que el encargo manda parar. Ninguna de las cinco operaciones de codigo se
> ejecuto, no se toco una sola linea de `web/` ni de `scripts/`, y `dataset/` quedo restaurado a
> HEAD. En vez de improvisar, esta vuelta MIDIO: los 24 sitios que las operaciones nombran siguen
> hoy en su linea exacta.

---

## 0. LO PRIMERO: LOS HASHES, LAS RUTAS Y LO QUE NO SE TOCO

**Rama activa `pasada-unica`, verificada con `git branch --show-current` ANTES de la primera
edicion.** Arbol limpio y sincronizado con `origin/pasada-unica` al abrir (nada pendiente que
commitear: el ultimo commit de la vuelta anterior era `cbc6ce51`).

| tramo | hash | que lleva |
|---|---|---|
| 1 | **`8fe604ef`** | los cinco registros, los dos instrumentos de la TAREA 1 y las cuatro salidas de la linea base |
| 2 | **`d59a02d1`** | el instrumento de los sitios de la fase 0 y su salida |
| 3 | este reporte | |

**LAS RUTAS TOCADAS, la lista completa:**

| ruta | que le paso |
|---|---|
| `docs/plan/01_FUENTES.md` | registros 1 y 2, **aditivos** |
| `docs/plan/OPERACIONES.jsonl` | registros 3 y 4, **una linea cada uno, solo el campo `nota`** |
| `docs/plan/RECOMPUTO_3388.md` | registro 5, **dos parrafos al final, aditivos** |
| `scripts/loop/vuelta21_registros.py` | instrumento nuevo, solo lectura |
| `scripts/loop/vuelta21_tarea1.py` | instrumento nuevo, el que escribe los cinco registros |
| `scripts/loop/vuelta21_fase0_sitios.py` | instrumento nuevo, solo lectura |
| `docs/loop/SALIDA_GATE0_VUELTA21.txt` | la salida del Gate 0 guardada, como el encargo pide |
| `docs/loop/SALIDA_GATE0_DIFF_DATASET_VUELTA21.txt` | el diff que disparo la parada, guardado como prueba |
| `docs/loop/SALIDA_SUITE_VUELTA21.txt` | la salida de la suite del web |
| `docs/loop/SALIDA_V21_REGISTROS.txt` y `SALIDA_V21_FASE0_SITIOS.txt` | las salidas de los dos instrumentos de lectura |
| `docs/loop/REPORTE.md` | este reporte |

**LO RESERVADO, comprobado al cerrar:**

| | estado |
|---|---|
| `dataset/` | **INTACTO contra HEAD.** Lo movio el Gate 0 y se restauro con `git checkout --`; `git status` no lo lista. **CERO commits sobre `dataset/`** |
| `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` | **INTACTO**, 3.388 lineas, ni una leida como par nuevo |
| `RECOMPUTO_3388_COMPONENTES.jsonl` | **INTACTO**, 335 componentes |
| `OPERACIONES.jsonl`, campo `nodos` | **INTACTO en las dos operaciones tocadas** (`OP-F-04-HOR` sigue con sus 13 ids, `OP-S-11` con su lista vacia). Solo cambio `nota` |
| `web/` y `scripts/` de la aplicacion | **CERO lineas tocadas.** Los tres scripts nuevos son de `scripts/loop/` y ninguno se importa desde la app |

**Cero guiones largos y cero guiones medios**, contados por instrumento sobre las tres rutas de
`docs/plan/` y los tres scripts: `0` y `0` en cada una. El hook corrio y dio verde en los dos
commits (`[guardian] verde. Commit permitido.`).

**LA ADITIVIDAD, verificada campo por campo y no de palabra:**

- `OPERACIONES.jsonl`: **71 lineas antes y 71 despues**, dos cambiadas, y en las dos el valor nuevo
  del campo `nota` **empieza por el viejo entero** (comprobado con `str.startswith` contra el blob
  de HEAD). Ningun otro campo se movio.
- `01_FUENTES.md`: 419 lineas antes, 431 despues. **UNA sola linea vieja deja de estar literal**, la
  celda de la fila 7, y el texto viejo **sigue siendo su prefijo exacto**.
- `RECOMPUTO_3388.md`: 1.625 lineas antes, 1.638 despues, **cero lineas viejas desaparecidas**.

---

## 1. EL MARCADOR Y LA TASA, recomputados con instrumento de esta vuelta

**Instrumento: `scripts/loop/vuelta21_registros.py`, corrido hoy sobre
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, `dataset/metadata/master_graph.json`,
`docs/plan/OPERACIONES.jsonl`, `docs/plan/INVENTARIO.jsonl` y
`RECOMPUTO_3388_COMPONENTES.jsonl`. Corte 14 ago 2026. Ninguna cifra de este reporte sale de un
acta ni de un reporte anterior.**

| | medido hoy |
|---|---:|
| lineas del archivo de veredictos | **3.388** |
| **A / B / C / D** | **583 / 89 / 7 / 2.709** (**17,2 / 2,6 / 0,2 / 80,0** por ciento) |
| puestos | **1 a 3.388, cero huecos y cero duplicados** |
| nodos del grafo | **3.835**, de ellos **3.521 vivos** y **314 con la clave `deprecado`** |
| operaciones en `OPERACIONES.jsonl` | **71**, **cero ejecutadas** |
| componentes | **335** . entradas de inventario **671** |

**LA TASA POR DOMINIO, recomputada hoy. El cribado NO se movio en esta vuelta: se republica porque
la regla manda que toda cifra salga de una corrida de hoy, no porque haya cambiado.**

| dominio | pares | A | B | C | D | tasa A |
|---|---:|---:|---:|---:|---:|---:|
| compras | 155 | 1 | 2 | 0 | 152 | 0,6% |
| core | 1.445 | 344 | 87 | 7 | 1.007 | 23,8% |
| entrega | 171 | 2 | 0 | 0 | 169 | 1,2% |
| environmental | 170 | 29 | 0 | 0 | 141 | 17,1% |
| exportacion | 130 | 15 | 0 | 0 | 115 | 11,5% |
| franquicias | 148 | 18 | 0 | 0 | 130 | 12,2% |
| health_safety | 192 | 45 | 0 | 0 | 147 | 23,4% |
| quality | 844 | 126 | 0 | 0 | 718 | 14,9% |
| risk_management | 106 | 0 | 0 | 0 | 106 | 0,0% |
| seguridad_digital | 27 | 3 | 0 | 0 | 24 | 11,1% |

> **VARA POR TRAMO Y FIGURAS: no aplican a esta vuelta y se dice en vez de rellenarlas.** Esta tanda
> **no leyo un solo par** (el cribado sigue CERRADO en 3.388 y los veredictos no se abrieron), asi
> que no hay tramo nuevo que medir ni figura nueva que nombrar. Las **20 figuras de forma y 13 con
> marca de tanda** que la vuelta 20 publico y el acta verifico **no se recomputan aqui**: se citan
> con su corte del 14 ago 2026.

---

## 2. TAREA 1: LOS CINCO REGISTROS, Y DE QUE INSTRUMENTO SALE CADA CIFRA

**Los cinco estan puestos, los cinco son aditivos, ninguno borra ni reescribe nada.** El acta se
cita como ADJUDICACION, que es lo que es; las CIFRAS salen de la corrida de hoy.

### Registro 1: la fila 7 queda ADJUDICADA en la celda de `01_FUENTES.md`

**Medido hoy, no copiado del acta:**

| | |
|---|---:|
| pasos de `decision_de_vender_startup` **en el grafo de hoy** | **34** |
| pasos **en el blob de `23f9ac32`** (11 ago, el commit que CREA `01_FUENTES.md`), leidos de ese blob | **34** |
| blob de `dataset/metadata/master_graph.json` en `0e5e0c60` / `23f9ac32` / HEAD | **`bb423c06...` los tres, IDENTICOS** |
| los otros dos apartados de la misma tabla | `viral_loop_marketing` **30 CALZA**, `coeficiente_viral` **16 CALZA** |

**Consecuencia, y es la del acta reproducida por mi:** el nodo **no crecio**; el 25 y su tramo eran
**PARCIALES DE NACIMIENTO**. El 25 queda entero, la frontera vigente (1 a 10 / 11 a 34) **se cita**
de la tabla de la vuelta 20 y no se recuenta, y el caracter del hallazgo queda.

### Registro 2: la nomina de los 13 SI existe, y el que sobra tiene nombre

| | medido hoy |
|---|---|
| Horowitz en segunda o posterior posicion, en el grafo | **14** |
| campo `nodos` de `OP-F-04-HOR` (fecha_corte 2026-08-11) | **13** |
| **los 14 menos los 13** | **`principio_calidad_mvp`**, y **ninguno de los 13 falta en el grafo** |
| cobertura de plan de ese nodo, barridas **las 71** operaciones | **TRES**: `OP-F-03` (21 nodos), `OP-D-01` (2 nodos) y **`OP-D-06`** (18 nodos) |

> **UNA DIFERENCIA CON EL ACTA, declarada al lado y no callada:** el acta nombra **dos** sedes de
> cobertura (`OP-F-03` y `OP-D-01`). Barridas hoy las 71 operaciones por el campo `nodos`, son
> **TRES**: tambien esta en `OP-D-06`. **No contradice al acta** (que no dijo "solo dos"), la
> ensancha, y el registro escrito en `01_FUENTES.md` lo dice asi, marcando cual es la que el acta no
> nombra.

### Registro 3: `OP-F-04-HOR` recibe su aviso, y el campo `nodos` no se toca

Diff de **UNA linea**. La `nota` pasa de **104 a 831** caracteres y el valor viejo sigue siendo su
prefijo. **Remedido hoy por posicion del campo `fuente`:** `metas_vs_proposito` tiene Horowitz en
**posicion 2 de 3** y el ultimo declarado es *Never Lose a Customer Again*, y **es el UNICO de los
13 en ese caso**. La presencia 13 de 13 queda intacta.

### Registro 4: `OP-S-11` recibe su segundo ejemplar

Diff de **UNA linea**. La `nota` pasa de **1.269 a 2.128** caracteres, aditiva. **Medido hoy sobre
los 3.521 vivos**, los nodos que declaran el mismo libro dos veces con dos grafias son **CUATRO y
ninguno mas**:

| nodo | libro | las dos grafias |
|---|---|---|
| `decision_de_vender_startup` | Horowitz | *Hard Thing About Hard Thing* / *Hard Thing About Hard Things* |
| `plan_mejora_procesos` | Horowitz | las mismas dos |
| `asociaciones_clave` | Hugos | *Essentials of Supply Chain Management* / *Essentials of Supply Chain Mana* |
| `transicion_producto_a_experiencia` | Hugos | las mismas dos |

Los dos primeros estan **dentro** de la tanda de los cuatro libros (44 nodos), los dos de Hugos
**fuera**, y son de la especie truncada que la operacion ya documenta.

### Registro 5: el cierre escrito donde se mide

Dos parrafos al final de la seccion **TAREA (vuelta 20)** de `RECOMPUTO_3388.md`: la **fila 7
ADJUDICADA** (manda el 34, parcial de nacimiento, medido con git) con lo que **la lista B queda
VACIA**, y la **FASE II CERRADA** por el acta de la vuelta 20 con **la FASE III abierta en
`pasada-unica`**. La medicion de la FASE II de la vuelta 20 **no se recomputa ahi**: se cita con su
corte.

---

## 3. TAREA 2.A: LA LINEA BASE. UNA MITAD VERDE Y LA OTRA EN PARADA

### La suite del web: VERDE, y sin tocar el `.env`

```
Test Files  79 passed (79)
     Tests  1003 passed | 3 skipped (1006)
  Duration  17.22s
EXITCODE=0
```

**Nada fallo por credenciales ausentes.** El `.env` sigue fuera del repo y no volvio. Salida entera
en `docs/loop/SALIDA_SUITE_VUELTA21.txt`.

### El Gate 0: LA PARADA, con la prueba delante

**`python scripts/run_phase1.py`, corrido tal cual, sin argumentos. Salida entera en
`docs/loop/SALIDA_GATE0_VUELTA21.txt`.** Y hay que decir las dos mitades por separado, porque no
dicen lo mismo:

| | |
|---|---|
| **el VALIDADOR** | **verde entero**: los chequeos salen todos `[OK]`, incluidos simetria, alias, semillas, puentes y alcanzabilidad **100,0%**, y la linea final del validador dice literalmente **`GATE 0: OK`** |
| **el ORQUESTADOR** | **`EXITCODE=2`**, por el aviso de curaduria que corre DESPUES del validador: **`REVERTISTE LA CURADURIA DE ETIQUETAS`** |

**Y lo que dispara la parada del encargo es el `git status`, no el codigo de salida:**

```
 M dataset/metadata/master_graph.json
 1 file changed, 72 insertions(+), 72 deletions(-)
```

**Medido linea por linea sobre el diff guardado** (`SALIDA_GATE0_DIFF_DATASET_VUELTA21.txt`): de los
**72** cambios, **71 son el campo `etiqueta_arbol`** de 71 nodos, que vuelve del texto curado al
titulo del libro (*Canvas*, *Pivotar*, *DMAIC*), y **el 72 es el salto de linea final del archivo,
que la recompilacion quita** (`\ No newline at end of file`). **Cero cambios de estructura: ningun
id, ninguna arista, ningun `deprecado`.**

**POR QUE PASA, leido del propio codigo y no supuesto** (`scripts/run_phase1.py`, bloque de
comentario de las lineas 941 a 958 y funcion `avisar_curaduria`, 976 a 994): el paso 6 **recompila
`master_graph.json` desde `dataset/nodos/`**, y la curaduria de etiquetas **no vive en los nodos**,
vive en `dataset/metadata/etiquetas_de_cara_v1*.json`. **Cada recompilacion la borra.** El propio
script lo llama *"la clase mas peligrosa de averia: degrada la VOZ sin romper la estructura"*, lo
fecha el **2026-08-07** (integrando compras y entrega), **se niega a auto aplicarla a proposito**
(*"Quien recompila, reaplica"*) y prescribe el remedio: `python scripts/etiquetas_de_cara.py
--aplicar`, con la variante `--reaplico-curaduria` para quien reaplica acto seguido.

**Lo comprobe sin escribir nada:** `scripts/etiquetas_de_cara.py` **en seco** (sin `--aplicar`) dice
**"71 etiquetas cambian; 0 ya estaban en su forma final"**, o sea que el remedio revierte
exactamente lo mismo que la recompilacion movio.

**QUE HICE CON ESO, y es lo que el encargo manda:**

1. **PARE.** Ninguna de las cinco operaciones se ejecuto. Cero lineas de `web/` y cero de los
   scripts de la aplicacion.
2. **No commitee `dataset/`.** Guarde el diff entero como prueba y **restaure el archivo a HEAD**
   con `git checkout -- dataset/metadata/master_graph.json`. Verificado despues: `git status` no
   lista `dataset/`.
3. `dataset/metadata/phase1_run_log.json` **no aparecio como modificado**, asi que el unico
   movimiento fue el del grafo.

### Por que la parada alcanza a las cinco operaciones y no solo al grafo

**No es una sola razon, son tres, y cada una vale sola:**

1. **El encargo lo escribe:** el paso A es "LINEA BASE PRIMERO, **antes de tocar codigo**", y su
   condicion se cumplio. Ejecutar despues de una linea base que no se sostiene es exactamente lo que
   la condicion evita.
2. **`AUDITOR.md` seccion 3 lo escribe para el modo continuo:** *"Gate 0 y suites en verde tras cada
   fase"* y *"CUALQUIER guarda en rojo (...) detiene al ejecutor y convoca al auditor en la vuelta
   siguiente"*. El orquestador esta en rojo **antes** de que yo toque nada, asi que el criterio de
   HECHO del cierre (`08_VERIFICACION.md`, cuya verificacion transversal empieza por **Gate 0
   verde** y **suite verde**, en ese orden) **no se puede alcanzar en esta vuelta sin tocar
   `dataset/`**, que esta reservado.
3. **Dos de las cinco operaciones no alcanzan a ejecutarse sin decidir**, que el encargo tipifica
   como PARADA y no como improvisacion. Detalle en la seccion 4.

---

## 4. LAS CINCO OPERACIONES, MEDIDAS SIN EJECUTAR NINGUNA

**Instrumento `scripts/loop/vuelta21_fase0_sitios.py`, solo lectura, salida en
`docs/loop/SALIDA_V21_FASE0_SITIOS.txt`.** Esto es medicion, no ejecucion.

### 4.1. El mapa de la fase 0 esta INTACTO, y era lo que mas podia haberse podrido

Las notas de `OP-C-01`, `OP-C-02` y `OP-C-03` nombran sitios con **archivo y numero de linea**, y se
escribieron el **11 ago 2026**. Transcritos uno a uno y leidos hoy: **los 24 sitios siguen
exactamente en su linea**, cero ausentes, cero corridos.

| operacion | sitios | comprobados hoy |
|---|---:|---|
| `OP-C-01` | 13 | `planRedactor.ts:53` es `const n = graph[nid];`, `compass.ts:153` es la guarda al reves (`opts.graph[id] && ...`), las tres de `interprete.ts` leen `graph[id].` directo |
| `OP-C-02` | 2 | `plan/route.ts:267` es `.map((nid) => graph[nid].titulo_concepto)` y la `405` acaba en `?? "ideacion"` |
| `OP-C-03` | 9 | `graph.ts:244` es `const n = graph[nid];`, las dos de `recorrido.ts` pasan `graph[nid]` a `obtenerPregunta`, y `start/route.ts:149` es el `if (!(brecha.semillaId in graph))` |

**El resolutor sigue donde el plan dice:** `web/lib/engine/graph.ts:131`,
`export function resolverId(nid: string, graph: Grafo): string | null`, con **11 llamadas** en
`web/**/*.ts`.

### 4.2. `OP-C-04`: su caso positivo no dice sobre que grafo se corre

Su verificacion manda *"reinyectar el enlace de `analisis_flujo_de_valor` a
`value_stream_analysis_lean` y comprobar que Gate 0 SE CAE"*. **No dice si esa reinyeccion va sobre
una copia o sobre `dataset/`**, y la diferencia no es de estilo: `dataset/` esta reservado. La
operacion hermana `OP-C-05` **si lo dice** (*"en una copia se mete a mano un campo"*), lo que hace
mas visible que aqui falta. **Elegir por mi cual de las dos lecturas vale es decidir, y decidir es
lo que el encargo llama improvisacion.** No lo hice.

### 4.3. `OP-C-05`: depende de una operacion de otra fase, y su propia nota la apaga

**Medido:** `OP-C-05` declara `depende_de: ["OP-S-12"]`, y **`OP-S-12` vive en la fase `05_SANEO`**,
no en la 0. Su propia `nota` lo escribe sin ambiguedad, y va citada literal: *"SE ENCIENDE DESPUES
DEL SANEO FINAL: encenderla antes para el trabajo, porque el grafo de hoy la falla 1.056 veces y eso
NO es una regresion, es el estado conocido"*. **Con el texto tal como esta, la fase 0 no puede cerrarse con
`OP-C-05` encendida**, y no hay regla escrita que diga que se escribe apagada, ni que viaje con la
fase 05. Va a las preguntas.

---

## 5. CORRECCIONES Y DISCREPANCIAS DECLARADAS

| # | que | donde queda |
|---:|---|---|
| 1 | **la fila 7: manda el 34** | celda de `01_FUENTES.md`, con el 25 y su tramo enteros |
| 2 | **la nomina de los 13 existe y sobra `principio_calidad_mvp`** | subseccion de la vuelta 20 de `01_FUENTES.md`, con la frase falsa entera al lado |
| 3 | **`principio_calidad_mvp` tiene TRES sedes de cobertura, no dos** | dicho en el mismo registro 2, nombrando la que el acta no nombra (`OP-D-06`) |
| 4 | **`metas_vs_proposito` con el bloque en medio** | `nota` de `OP-F-04-HOR`, con la adjudicacion vieja entera |
| 5 | **cuatro nodos con doble grafia, no uno** | `nota` de `OP-S-11`, con el texto viejo entero |
| 6 | **el Gate 0 corrido tal cual mueve `dataset/`** | este reporte, seccion 3. **No lo arreglo yo** |

---

## 6. ERRORES PROPIOS DE ESTA VUELTA, DECLARADOS CON NOMBRE

- **Mi instrumento reventó al leer el blob viejo con git.** `subprocess` con `text=True` decodifica
  en `cp1252` en Windows y el grafo tiene acentos: `UnicodeDecodeError` en mitad de la seccion 1.
  Lo cace **antes de publicar ninguna cifra**, puse `encoding="utf-8"` explicito y volvi a correr
  entero. Ninguna cifra de este reporte viene de la corrida rota.
- **Escribi el quinto registro con un apano enrevesado** (leia el archivo dos veces dentro de la
  llamada, con una condicion muerta). Lo reescribi como una funcion `anadir_al_final` con ancla de
  cola comprobada **antes de correrlo**, asi que nunca toco el archivo en su forma mala.

---

## 7. PENDIENTES DE DOCTRINA

> **UNO, y lo traigo sin pararme en el porque hay extension citable: NO HAY REGLA QUE DISTINGA UN
> ROJO DE NACIMIENTO DE UN ROJO POR REGRESION EN EL GATE 0.** El orquestador sale en 2 por una
> averia **conocida y fechada el 7 ago 2026**, anterior a la campaña del bucle y ajena a lo que esta
> vuelta hizo. La campaña **ya usa esa distincion en otro sitio**: la `nota` de `OP-C-05` dice que
> el grafo falla su guarda 1.056 veces y que **"eso NO es una regresion, es el estado conocido"**.
> Aplicar la misma frase al aviso de curaduria seria extension natural, **pero la escribio para su
> guarda y no para el Gate 0**, asi que la adjudicacion no es mia. Registrado, no decidido.

---

## 8. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

1. **Haber parado la TAREA 2 ENTERA en vez de ejecutar `OP-C-01`, `OP-C-02` y `OP-C-03`, que no
   tocan `dataset/`.** A favor de lo que hice: el encargo dice "PARAS" sin repartir, la linea base
   es del paso A y el criterio de HECHO de la fase pide Gate 0 verde, que hoy no se alcanza sin
   tocar lo reservado. En contra: tres de las cinco operaciones viven enteras en `web/` y su
   verificacion es la suite, que esta verde; se podrian haber hecho y dejar dos en parada. **Elegi
   no partir la fase.** Es el discutible mas gordo de la vuelta y lo pongo el primero.
2. **Haber restaurado `dataset/` con `git checkout --` en vez de dejar el arbol sucio** para que el
   auditor lo viera con sus ojos. A favor: el encargo dice "un grafo ya limpio no debe moverse" y lo
   reservado tiene que acabar la vuelta como empezo; ademas guarde el diff entero commiteado, que
   dice lo mismo sin dejar el arbol sucio. En contra: descarte trabajo del arbol, y eso es
   irreversible.
3. **Haber medido los 24 sitios sin que el encargo lo pidiera.** A favor: es solo lectura, es el
   modo que la campaña permite en cierre, y le da al auditor un mapa que caduca en cuanto alguien
   edite `web/`. En contra: es iniciativa fuera del encargo, y el encargo decia PARAS.
4. **Haber ensanchado el registro 2 con `OP-D-06`, que el acta no nombra.** A favor: es lo medido
   hoy y callarlo seria publicar media cifra. En contra: mete en un registro de adjudicacion ajena
   un dato que la adjudicacion no contenia.
5. **Haber corrido la suite del web despues de que el Gate 0 ya hubiera disparado la parada.** A
   favor: es la otra mitad del paso A, es solo lectura y sin ella el auditor no sabria si la suite
   esta verde. En contra: si la parada era inmediata, la suite sobraba.
6. **El rotulo `(vuelta 21)` en los cinco registros.** El acta que los ordena se titula "VUELTA 20"
   pero dice de si misma que es *"la anunciada como vuelta 21"*. Elegi numerar mi tanda como **21**
   (la 20 fue la anterior del ejecutor) y citar el acta siempre como **"el acta de la vuelta 20"**,
   nunca como 21, para que no haya dos cosas con el mismo numero. **Puede que el auditor numere su
   acta como 21 y entonces mi rotulo colisione.**
7. **Haber puesto el registro 1 dentro de la celda de la tabla**, que queda larga, en vez de en una
   nota debajo. El acta dice "en la celda", asi que segui la letra; el coste es una celda de tabla
   de nueve lineas.
8. **Haber reproducido con git la medicion de blobs del auditor** en vez de citarla y ya. A favor:
   la regla 1 dice que toda cifra publicada sale de instrumento corrido en esta vuelta, y el 34 lo
   publico yo en `01_FUENTES.md`. En contra: se parece a reabrir una adjudicacion cerrada. **Sale
   identica: los tres blobs son `bb423c06`.**
9. **Haber commiteado el diff de `dataset/` dentro de `docs/loop/`.** A favor: una parada sin prueba
   es una afirmacion. En contra: deja texto del grafo (con acentos y titulos) en una sede que no es
   la suya.

---

## 9. LAS PREGUNTAS QUE TRAIGO, porque no las puedo medir

1. **Que quiere decir "Gate 0 en verde" en el criterio de cierre de la fase 0: el VALIDADOR o el
   ORQUESTADOR.** Hoy el validador dice `GATE 0: OK` con todos sus chequeos y el orquestador sale
   con 2. La fase 0 no se puede cerrar sin esa definicion, y las dos lecturas son defendibles.
2. **Quien reaplica la curaduria durante la pasada, y con que permiso.** La FASE III recompila el
   grafo muchas veces (cada fase mueve ids), y cada recompilacion borra 71 etiquetas curadas. Si
   `dataset/` sigue reservado para el ejecutor, el grafo termina la pasada **con la voz degradada y
   sin que nada se queje**, que es justo el modo de fallo que el canon de fallar ruidoso prohibe.
   **Esta pregunta no es de esta vuelta: es de toda la fase III.**
3. **`dataset/` sigue reservado en la FASE III?** La pasada, por definicion, mueve ids en
   `dataset/`. Todo lo escrito hasta hoy (incluida la seccion 9 del acta de la vuelta 20) trata
   `dataset/` como intocable. Hace falta la frase que abra esa puerta, y con que guardas.
4. **El caso positivo de `OP-C-04`: sobre copia o sobre `dataset/`?** Su texto no lo dice y su
   hermana `OP-C-05` si. Sin eso no se puede ejecutar sin decidir.
5. **`OP-C-05` se queda en la fase 0 apagada, o viaja con `OP-S-12` a la fase 05?** Depende de una
   operacion de otra fase y su nota manda encenderla despues del saneo final.

---

## 10. CONDICIONES DE PARADA: UNA SE CUMPLE, Y ES LA QUE EL ENCARGO ESCRIBIO

| condicion | estado |
|---|---|
| **linea base del Gate 0** | **SE CUMPLE.** `dataset/` se movio al correrlo. Declarada, con prueba, sin arreglar y sin commitear |
| doctrina nueva necesaria | **no**, pero queda **un pendiente de doctrina** (seccion 7) con su extension citable propuesta y no decidida |
| contradiccion sin resolver | **no** en lo medido: los cinco registros calzan con el acta y la unica diferencia (`OP-D-06`) se declara al lado |
| decision de fundador | **nada reservado se toco.** `dataset/` restaurado a HEAD, veredictos, componentes y campos `nodos` intactos, cero merges |
| fallo tecnico | **no.** Arbol limpio, hook verde en los dos commits, cero guiones. La suite del web verde y sin `.env` en el repo |
| credito de tanda | esta tanda **no publica ninguna clase ni cifra nueva del cribado**; los cinco registros van con su instrumento delante |
| campaña consumada | **no** |

> **LO QUE QUEDA PARA LA VUELTA SIGUIENTE, dicho sin adornar: la FASE 0 DE CODIGO NO EMPEZO.** El
> encargo la pedia entera y esta vuelta entrega **la TAREA 1 completa y verificada** mas **la linea
> base medida con su parada declarada**. La fase 01 tampoco se empezo, como el encargo manda. La
> verificacion completa de apertura sigue siendo del auditor, y ahora tiene delante una pregunta que
> antes no estaba: **el Gate 0 de hoy no puede darse por verde sin tocar lo reservado.**
