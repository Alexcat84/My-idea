# PARA ALEXIS. Parada del bucle, 14 ago 2026 (segunda de la FASE III)

**El bucle esta DETENIDO.** `docs/loop/PROMPT_SIGUIENTE.md` esta vacio a proposito.
**Lo escribe el auditor (Fable 5) al cerrar la vuelta 23. Rama `pasada-unica`.**

---

## 1. EL MOTIVO, en una linea

**Doctrina nueva necesaria: `OP-S-07` (retirar las 33 auto aristas) no puede ejecutarse tal
como esta escrita porque EL PROPIO GATE 0 DESHACE SU TRABAJO POR DISEÑO, y toda salida
reescribe la letra del plan o toca codigo que ninguna operacion ordena** (AUDITOR.md,
seccion 4, condiciones primera y tercera).

Antes de nada: **no es un desastre y no hay datos malos.** La parada se reprodujo
EJECUTANDOLA (ejecutor, vuelta 23) y se verifico por mecanismo (auditor, esta acta); el
grafo esta identico a HEAD, el Gate 0 verde por su ciclo escrito y las tres suites en verde,
todo corrido por el auditor hoy. Es el protocolo funcionando: una operacion cuyo texto no
alcanza es PARADA, no una improvisacion.

## 2. EL ESTADO EXACTO

- **Rama `pasada-unica`**, FASE III en modo de ejecucion continua. **Fase 0: cuatro de siete
  ejecutadas y vivas en el codigo** (`OP-C-01`, `OP-C-02`, `OP-C-03`, `OP-S-06`, commits
  `8b2ba536`, `41a9c570`, `1578e641`, `a1c39585`, punto fijo `9707a67d`); **`OP-S-07`
  PARADA** (dos veces: vuelta 22 documentada, vuelta 23 reproducida ejecutando); **`OP-C-04`
  BLOQUEADA** por su `depende_de` (`OP-S-06`, `OP-S-07`); **`OP-C-05` DIFERIDA** por el suyo
  (`OP-S-12`). Fases 01 a 10 sin tocar.
- **Marcador** (recomputado hoy por el auditor): n 3.388, A 583 / B 89 / C 7 / D 2.709, cero
  huecos. **Grafo:** 3.835 nodos, 3.521 vivos, 314 deprecados, 16.866 enlaces, blob
  `6007c1da` identico a HEAD tras cada medicion.
- **Gate 0 verde por el ciclo escrito, corrido hoy por el auditor:** exit 0, GATE 0: OK, 71
  etiquetas, blob identico. **Suites, corridas hoy por el auditor:** motor 24/24, web 80
  ficheros con 1.030 pasadas y 3 saltadas, tsc limpio.
- **Un accidente del arnes, ya absorbido:** el auditor de la vuelta 22 murio a mitad de
  respuesta (api_error, una sola vez), no dejo acta y el encargo llego repetido a la vuelta
  23. El ejecutor lo trato bien (remidio todo desde cero) y el acta de la vuelta 23 cierra
  las dos vueltas. No es parada por fallo tecnico: fue una vez y el arnes se recupero solo.
- El detalle completo esta en el acta de la vuelta 23 (`docs/loop/ACTA_AUDITOR.md`, linea
  4.812) y las salidas `SALIDA_V23_*.txt` commiteadas.

## 3. EL PROBLEMA QUE NECESITA TU DECISION: OP-S-07 contra el paso 5 del validador

**Los dos textos de la operacion no pueden ser verdad a la vez, y lo demuestra el
instrumento:**

- Su `eliminar`: retirar de los 27 nodos vivos los 33 enlaces que resuelven al propio nodo,
  y **"no se toca ningun otro campo"**.
- Su `verificacion`: ningun vivo se cita a si mismo tras resolver, y el conteo de aristas
  **"baja en 33 exactamente"**.

**El mecanismo, medido:** cada una de las 33 (33 de 33, verificado dos veces) es la vista
reciproca de un enlace que el GEMELO DEPRECADO tiene hacia su superviviente. El paso 5 de
`run_phase1.py` (simetrizar, lineas 396 a 435) fabrica toda reciproca que falte y **la
escribe de vuelta al fichero del nodo**; su unica defensa (`dedupe_and_remove_self`) compara
literal y ninguna de las 33 es literal. Retiras las 33, corres Gate 0, y las 33 vuelven:
variacion neta CERO. La sombra vuelve mientras viva lo que la proyecta.

**Por que ninguna regla escrita lo resuelve:** `P.16` (quien fabrica limpia) gobierna las
fusiones QUE VIENEN y deja escrito que las 33 son trabajo de `OP-S-07` tal como esta
escrita. `OP-S-12` excluye la auto arista a proposito y mide sobre vivos. `OP-C-04` ordena
una guarda en Gate 0, no cambiar el simetrizador. Las reglas de correccion cubren cifras,
no reescribir la letra de una operacion.

**Las cifras que necesitas para decidir, medidas hoy (particion exacta y sin solape):**

| donde | que | cuanto |
|---|---|---:|
| vivos | enlaces que resuelven al propio nodo (criterio A, el escrito) | **33 en 27 nodos** |
| deprecados | reciprocas LITERALES de esas 33 (apuntan al superviviente; son las que el paso 5 proyecta sobre vivos) | **33 en 32 nodos** |
| deprecados | alias contra alias (apuntan a OTRO alias del mismo superviviente; se simetrizan entre deprecados, NO proyectan sobre vivos) | **48 en 33 nodos** |
| deprecados | total bajo el criterio B (resuelve al mismo destino que el propio nodo) | **81 en 59 nodos** |

## 4. LOS CAMINOS QUE VEO (cada uno reescribe algo, por eso es tuyo)

- **A. AMPLIAR la letra de `OP-S-07`:** el `eliminar` retira las 33 vivas Y sus 33
  reciprocas literales del gemelo deprecado (66 entradas en 59 ficheros), y la
  `verificacion` se corrige a "baja en 66". Sin nada que proyectar, el paso 5 no refabrica
  ni rompe la simetria. Coste: correccion declarada de la letra y de una cifra escrita de la
  operacion. Queda una linea tuya sobre las **48 alias contra alias**: se quedan (no
  molestan a los vivos), caen aqui mismo, o son operacion aparte.
- **B. ENSEÑAR AL PASO 5 a resolver antes de fabricar** (no fabricar sobre un vivo la
  reciproca de un enlace que resuelve al propio vivo). Es la doctrina de la nota de
  `OP-S-07` (resolver, no comparar) aplicada al fabricante. Coste: codigo del validador que
  ninguna operacion ordena, y la comprobacion de simetria del Gate tendria que exceptuar
  esos pares o quedaria en rojo. Es mas cirugia que A.
- **C. DIFERIR `OP-S-07`:** contradice su `bloquea_a` escrito y tu decision de adelantarla
  a la fase 0. Lo listo por completitud.

Si quieres mi lectura: **A**, porque mata la causa con datos y no con codigo, su cifra
queda exacta y verificable, y las 48 restantes pueden esperar tu linea sin bloquear nada.

**Y la decision gemela, que viene sola con esta:** la guarda de auto arista de `OP-C-04`
necesita su criterio escrito para deprecados. Con el criterio A (el de `OP-S-07`) un
deprecado da CERO por construccion: la guarda pasaria verde sobre las 81. Con B las ve.
Basta una linea tuya en la nota de `OP-C-04`: sobre vivos criterio A (que en vivos es
identico a B, medido: 33 y 27 por los dos), y sobre deprecados si mide con B o si quedan
fuera de la guarda con el motivo escrito.

## 5. LO QUE YA QUEDO ADJUDICADO y no necesita decision tuya

1. Los ocho discutibles de la vuelta 23: ocho de ocho correctos (acta, seccion 3).
2. El plan NO estrena estado "ejecutada": el commit por operacion es el registro; las 71
   siguen en LISTA salvo que tu digas otra cosa.
3. El falso movimiento de `master_graph.json` en `git status` es artefacto de CRLF: la vara
   es el hash de blob (ya escrita en 08_VERIFICACION.md linea 53); queda encargado un
   renglon expreso alli al reanudar.
4. La salida en rojo de `OP-S-07` commiteada se conserva tal cual: es la prueba de la
   parada (precedente del acta 21).
5. La tanda 22 cargo una caida de reporte (dos numeros de linea desfasados), releida al
   doble; la tanda 23 salio limpia al cien: cero caidas de cualquier especie.

## 6. COMO RETOMAR

1. Escribe tu decision como correccion declarada en `docs/plan/OPERACIONES.jsonl`: la letra
   de `OP-S-07` (camino A o B, con su cifra corregida sin borrar el texto viejo), la linea
   sobre las 48, y el criterio de la guarda de `OP-C-04` sobre deprecados.
2. Escribe el encargo en `docs/loop/PROMPT_SIGUIENTE.md` o pide que el auditor lo escriba
   en su primera vuelta. La TAREA 1 de esa vuelta: registrar estas adjudicaciones (el
   renglon del CRLF en 08_VERIFICACION.md y los registros en las notas de las operaciones
   tocadas). La TAREA 2: ejecutar `OP-S-07` por tu letra nueva, `OP-C-04` al desbloquearse
   (su caso positivo en arbol temporal, ya adjudicado), y seguir la fase 0 al cierre.
3. Relanza el bucle.

El trabajo esta a salvo: nada reservado se toco, `dataset/` esta identico a HEAD (verificado
por hash de blob), el experimento de `OP-S-07` nunca se commiteo, y todo lo medido esta
commiteado con sus salidas en `docs/loop/`.

DECISION DEL FUNDADOR (14 ago 2026): camino A. La letra de OP-S-07 se amplia a las 66; las 48
alias-contra-alias quedan censadas como INERTES; la guarda de OP-C-04 mide sobre VIVOS y los
deprecados quedan fuera con motivo escrito. La fase 0 se cierra.
