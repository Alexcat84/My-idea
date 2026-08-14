# PARA ALEXIS. Parada del bucle, 14 ago 2026

**El bucle esta DETENIDO.** `docs/loop/PROMPT_SIGUIENTE.md` esta vacio a proposito.
**Lo escribe el auditor (Fable 5) al cerrar la vuelta 21. Rama `pasada-unica`.**

---

## 1. EL MOTIVO, en una linea

**Doctrina nueva necesaria: `OP-C-04` (fase 0 de codigo) no puede ejecutarse tal como esta
escrita sin decidir entre textos del plan que se contradicen, y toda salida reescribe el orden o
la letra del plan, que es decision de la casa** (AUDITOR.md, seccion 4, condiciones primera y
tercera).

Antes de nada: **no es un desastre y no hay datos malos.** La tanda 21 del ejecutor verifico al
cien por cien (cero caidas de cualquier especie, el credito intacto y la racha de caidas de
reporte rota a CERO), y de las cinco preguntas que trajo, cuatro quedaron adjudicadas con regla
escrita y medicion. Esta parada es el protocolo funcionando: una operacion cuyo texto no alcanza
es PARADA, no una improvisacion.

## 2. EL ESTADO EXACTO

- **Rama `pasada-unica`**, FASE III abierta, **fase 0 SIN EMPEZAR**: cero operaciones ejecutadas
  (las 71 en estado LISTA), cero lineas de `web/` o `scripts/` de la aplicacion tocadas.
- **Marcador** (recomputado hoy): n 3.388, A 583 / B 89 / C 7 / D 2.709, cero huecos. **Grafo:**
  3.835 nodos, 3.521 vivos, 314 deprecado, blob `bb423c06` identico a HEAD tras cada medicion.
- **Suite del web:** verde (79 archivos, 1.003 en verde, 3 saltados), sin `.env` en el repo.
- **Gate 0:** su ciclo verde EXISTE y quedo medido (seccion 3.1 de abajo). La TAREA 1 de la
  vuelta 21 (los cinco registros del cierre de la FASE II) esta entera y verificada.
- El detalle completo esta en el acta de la vuelta 21 (`docs/loop/ACTA_AUDITOR.md`) y las
  mediciones en `docs/loop/SALIDA_ACTA21_AUDITOR.txt` (instrumento
  `scripts/loop/acta21_auditor_medir.py`).

## 3. LO QUE YA QUEDO RESUELTO y no necesita decision tuya

1. **La parada del Gate 0 de la vuelta 21 (el grafo se movia al correrlo) esta RESUELTA por la
   regla escrita del propio instrumento.** `run_phase1.py` recompila el grafo y borra la
   curaduria de etiquetas a proposito (averia cazada el 7 ago 2026, comentario en el propio
   script); el remedio esta escrito ahi mismo: "Quien recompila, reaplica". Medido hoy:
   `python scripts/run_phase1.py --reaplico-curaduria` sale en CERO con `GATE 0: OK`, y
   `python scripts/etiquetas_de_cara.py --aplicar` acto seguido deja `master_graph.json`
   **byte-identico a HEAD** (mismo hash de blob, salto de linea incluido). "Gate 0 en verde"
   queda definido: el orquestador en cero por esa via escrita.
2. **`dataset/` en la FASE III:** se mueve SOLO por lo que una operacion del plan ordena; todo
   movimiento que ninguna operacion ordena sigue reservado. En la fase 0 ninguna operacion toca
   el grafo.
3. **`OP-C-05`:** se queda en la fase 0 DIFERIDA por su `depende_de` escrito (`OP-S-12`); no
   bloquea nada (`bloquea_a` vacio). Sin decision pendiente.
4. **La sede de los casos positivos que inyectan estado malo:** arbol de trabajo temporal, nunca
   commiteado, restaurado a HEAD acto seguido, con la salida guardada como prueba.

## 4. EL PROBLEMA QUE SI NECESITA TU DECISION: OP-C-04

`OP-C-04` manda añadir a Gate 0 dos guardas: la comprobacion de **auto-arista con resolucion** y
la **lista blanca de claves del nodo**. Medido hoy con instrumento propio:

- El grafo de HOY tiene **33 auto-aristas tras resolver, sobre 27 nodos** (el peor,
  `costo_de_mala_calidad_copq`, con 7; ninguna directa): exactamente las cifras que la nota de
  `OP-S-07` publica. Su reparacion es **`OP-S-07`, fase 05_SANEO**, despues de las fusiones.
- Las claves sucias de hoy son las que **`OP-S-06` (fase 05)** repara: `fase_проekto` (cirilica),
  `fase_project`, y `fuentes_adicionales` en cuatro nodos. Y ademas `merged_originals` vive en
  **269 nodos** y nadie escribio si va dentro o fuera de la lista blanca.
- El caso positivo de la operacion ("REinyectar el enlace de `analisis_flujo_de_valor` y ver que
  Gate 0 se cae") presupone un grafo post saneo: **ese enlace sigue puesto hoy.**

**La contradiccion:** el plan quiere `OP-C-04` ANTES de todo lo que mueve un id (su `bloquea_a`
sobre `OP-S-01`, `OP-S-09` y `OP-F-01`, y la fila 1 del 00_INDICE: sin las guardas, una fusion
mal hecha no da sintoma), el protocolo exige **Gate 0 en verde tras cada fase**, y la guarda,
añadida hoy, tumba el Gate con 33 mas 6 fallos de **estado conocido** que solo la fase 05
limpia. Los tres textos no pueden ser verdad a la vez, y el plan distinguio a proposito el caso
gemelo (`OP-C-05` SI lleva diferimiento escrito; `OP-C-04` lleva lo contrario), asi que no hay
extension citable: es doctrina nueva.

**Los tres caminos que veo, cada uno reescribe algo del plan (por eso es tuyo):**

- **A. ADELANTAR el saneo minimo a la fase 0:** ejecutar la retirada de las 33 auto-aristas
  (`OP-S-07`) y la limpieza de claves (`OP-S-06`) antes o junto con `OP-C-04`. La guarda queda
  activa durante las fusiones, que es su razon de ser. Coste: dos operaciones de la fase 05
  cambian de sitio en el orden escrito.
- **B. LINEA BASE DECLARADA dentro de la guarda:** la guarda nace conociendo las 33 y las claves
  de hoy (lista escrita en la operacion) y tumba el Gate solo con lo que EXCEDA la linea base;
  la lista se vacia cuando `OP-S-07` y `OP-S-06` ejecuten. Coste: doctrina nueva de linea base y
  su sede, y una guarda mas compleja.
- **C. DIFERIR la guarda con su saneo** (el trato de `OP-C-05`): la fase 0 queda en `OP-C-01` a
  `OP-C-03`. Coste: las fusiones corren SIN la guarda de auto-aristas, exactamente lo que la
  fila 1 del indice dice que no debe pasar, y el `bloquea_a` escrito de `OP-C-04` queda en letra
  muerta.

Si quieres mi lectura: **A** es el unico camino que conserva el proposito escrito de la guarda
sin doctrina nueva de mecanismo; su unico coste es de orden. Pero mover operaciones de fase es
cambiar el plan, y eso la casa se lo reservo. Tambien te toca una linea sobre
**`merged_originals`** (dentro o fuera de la lista blanca) y, si eliges A o B, si la fase 0
puede ejecutar `OP-C-01` a `OP-C-03` mientras tanto (sus textos estan completos y verificados:
los 24 sitios siguen en su linea exacta).

## 5. COMO RETOMAR

1. Escribe tu decision donde corresponda: la letra de `OP-C-04` (y de `OP-S-06`/`OP-S-07` si
   eliges A) en `docs/plan/OPERACIONES.jsonl` como correccion declarada, o una regla nueva en
   `AUDITOR.md` si prefieres doctrina general.
2. Escribe el encargo de la reanudacion en `docs/loop/PROMPT_SIGUIENTE.md` (o pide que el
   auditor lo escriba en su primera vuelta): la TAREA 1 son los registros de las adjudicaciones
   del acta de la vuelta 21 (la definicion del Gate 0 verde en `08_VERIFICACION.md`, las notas
   de `OP-C-04` y `OP-C-05`), y la TAREA 2 la fase 0 por el camino que decidas. **OJO: la linea
   base del Gate 0 en ese encargo debe usar el ciclo escrito (el par de comandos del punto 3.1),
   no la invocacion a secas.**
3. Relanza el bucle.

El trabajo esta a salvo: nada reservado se toco, el arbol esta limpio, y todo lo medido esta
commiteado con sus salidas en `docs/loop/`.
