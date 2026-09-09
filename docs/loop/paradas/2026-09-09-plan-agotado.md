# PARA ALEXIS. EL BUCLE PARA EN LA VUELTA 213 (9 sep 2026)

## ANTES DE NADA, PARA EL AUDITOR QUE RETOME: EL ORDEN DE APERTURA

**Esto va aqui, y arriba del todo, porque TRES actas seguidas (211, 212 y 213) han roto la
misma letra, y las tres por el mismo motivo: la orden vive en la linea 112 de
`docs/loop/AUDITOR.md` y todo auditor la lee cuando ya ha tocado el repo.**

> **TU COMANDO NUMERO UNO ES `python scripts/loop/apertura_del_auditor.py --estado`.**
> Si dice que hay turno vivo ajeno, el DOS es `--cerrar-turno --vuelta "<N>-cola"`.
> El TRES es el sellado.
> **NINGUN comando anterior a esos tres puede nombrar `docs/loop/REPORTE.md`, ni por su
> nombre completo, ni dentro de un comodin, ni en una lista con otros ficheros.** Nada de
> `wc -l` sobre varios, nada de `ls -l docs/loop/`, nada de `stat` sobre una lista.
> **Y lee la leyenda de las clases del banco (`9.6.1`, `9.6.2`, `9.6.3`) ANTES de aislar el
> sujeto, no despues:** la ratificacion del `9.6.1` lista diez puestos por numero y puede
> quemarte uno.

---

## 1. EL MOTIVO DE LA PARADA

**`AUDITOR.md` 4, condicion `Decision de fundador: todo lo que la casa reserva`.**

**EL PLAN ESTA AGOTADO. LA UNICA FICHA DE TRABAJO REAL QUE QUEDA NO LA PUEDE CERRAR EL
BUCLE, Y NO HAY NINGUNA OTRA TAREA QUE ENCARGAR QUE NO SEA UNA DECISION TUYA.**

**NO ES LA PARADA FELIZ Y NO TE PIDO NINGUN MERGE:** la campaña **no** esta consumada,
porque `OP-I-01` sigue abierta.

**Las dos vueltas anteriores ya te lo subieron (acta 212, seccion 8, punto 1) y siguieron
girando porque aun quedaban tareas reales. Hoy ya no quedan, y encargar trabajo que no
puede mover la puerta es exactamente lo que la moratoria de `AUDITOR.md` 6.3 prohibe.**

## 2. EL ESTADO EXACTO, TODO MEDIDO EN ESTA VUELTA

| que | cuanto |
|---|---|
| rama | `pasada-unica` (el bucle **no** fundio nada) |
| HEAD al cerrar la vuelta 213 | `e71df663` |
| fase | **III, EJECUCION**, sin cerrar |
| marcador, recomputado del archivo | **3388 filas; A 550, B 72, C 5, D 2761** (quieto desde la 212) |
| Gate 0, ciclo entero de ocho comandos, corrido por el auditor | **8 de 8 en EXITCODE 0**, `numstat` en **0** filas |
| censo | 3.853 nodos / 3.169 vivos / 684 deprecados |
| fichas del expediente | **71** |
| con prueba de ejecucion en el repo | **64** |
| consumidas por otra ficha | **2**, las dos por `OP-U-01` |
| **sin ejecutar** | **5**: `OP-V-01`, `OP-L-01`, `OP-L-02`, `OP-L-03`, `OP-I-01` |
| de esas, **trabajo real segun la vara** | **1: `OP-I-01`** |
| suites | motor 25/25, web 82 ficheros y 1.040 tests, `tsc` EXITCODE 0 |

**El inventario de cierre de la Fase III, las 71 fichas leidas del repo y no del campo
`estado`, existe por primera vez y esta sellado en
`docs/loop/SALIDA_V213_T2_CIERRE_FASE_III.txt`.** Ese fichero **no se archiva con el
reporte**: es la base medida sobre la que se hace la auditoria integral.

## 3. LO QUE NECESITO DE TI: TRES DECISIONES

### DECISION 1 (la que desbloquea el cierre): ¿SE MARCAN LAS 95 ENTRADAS DEL INVENTARIO?

`OP-I-01` tiene cuatro puntos de verificacion y **el punto 2 esta en `NO CUBRE`**: *"toda
forma con cobertura incompleta va marcada PROVISIONAL"*. **Recontado hoy por el auditor
sobre `docs/plan/INVENTARIO.jsonl`: 672 entradas, 555 con cobertura de la forma `N de M`,
de ellas 95 INCOMPLETAS y 0 marcadas.**

**No hace falta COMPLETAR la cobertura: hace falta MARCARLA.** El banco `9.26` admite una
cobertura incompleta como cumplimiento **si se dice asi**, y hoy ninguna lo dice.

**Por que es tuya y no del bucle:** marcar esas 95 es **editar datos de docs/plan/ que
ninguna regla ordena hoy** (acta 211, adjudicacion `6.4`, linea 74607 de
`docs/loop/ACTA_AUDITOR.md`).

**Si dices que si, el bucle las marca en una vuelta y `OP-I-01` cierra.**

### DECISION 2: ¿SE ESCRIBEN LAS FILAS QUE FALTAN EN `08_VERIFICACION.md`?

**Medido hoy:** la tabla del CRITERIO DE HECHO tiene **siete** filas, de `01 FUENTES` a
`07 ADUANA`, y **cero** filas para `08`, `09` y `10`. **Las cinco fichas que salen SIN
EJECUTAR viven precisamente en esas tres fases**, o sea que **no hay vara escrita contra la
que medirlas**.

**Por que es tuya:** anadir esas filas **cambia la forma del plan** (acta 211, `6.2`).

### DECISION 3 (la mas barata y la que evita la cuarta caida): ¿MUEVO EL ORDEN DE APERTURA AL PRINCIPIO DE `AUDITOR.md`?

Tres auditores seguidos han roto la misma letra **con el remedio de codigo ya puesto**. El
codigo hace lo unico que puede hacer, que es **negar el sello**, y lo hizo las tres veces:
la 211, la 212 y la 213 **no tienen sello de apertura**. **El agujero no es del codigo: la
orden llega tarde.**

**Es tinta, no maquinaria, asi que la moratoria no lo prohibe; pero mueve un fichero de
gobierno y eso lo decides tu.**

## 4. LO QUE NO HICE, Y LO DIGO PARA QUE NO SE BUSQUE

- **No declare la campaña consumada** y **no pedi el merge de `pasada-unica`**. No lo esta.
- **No marque ni una de las 95 entradas**, no toque `OPERACIONES.jsonl` (mismo `sha256`
  `ca1d95b5b3d19e9e` al entrar y al salir de la vuelta) y no escribi en
  `08_VERIFICACION.md`.
- **No fundi ninguna rama.** El bucle no funde ramas.
- **No repare `vuelta186_rutas_del_reporte.py` ni `secciones_fuera_de_orden()`.** Los dos
  siguen levantados y esperan a la integral.

## 5. LA COLA DE LA AUDITORIA INTEGRAL: TREINTA Y UNA ENTRADAS NOMBRADAS

Las veintiocho del acta 212 mas las tres que levanto en la 213:

1. **La obligacion de dictado de la `6.2` del acta 212 es incumplible por construccion.**
   *"Ningun reporte cita un directorio a secas"* choca con *"la cabecera tiene que ser
   IDENTICA AL TALLADOR"*: el tallador emite dataset/ entre comillas inversas y el
   ejecutor no puede quitarlo sin poner roja la otra guarda. **Medido en cuatro reportes
   archivados; no hace dano hoy porque el patron del instrumento no lo ve.**
2. **La tabla del criterio de HECHO no cubre las fases 08, 09 ni 10** (la DECISION 2).
3. **El propio banco quema sujetos de la ciega:** la ratificacion del `9.6.1` lista diez
   puestos por numero, y el auditor tiene que abrir el banco para leer la leyenda de las
   clases. **Remedio barato: leer la leyenda antes de aislar.**

## 6. COMO RETOMAR

1. Contesta las tres decisiones **en un fichero de docs/loop/paradas/**, como las
   anteriores, para que el bucle pueda citarlas por su ruta.
2. Escribe el encargo de la vuelta **214** en `docs/loop/PROMPT_SIGUIENTE.md`, o pide al
   auditor que lo escriba a partir de tu decision.
3. **Si la DECISION 1 es que si:** la 214 marca las 95 con correccion declarada, `OP-I-01`
   cierra, y la 215 (que es vuelta de bateria por la cadencia de cinco) puede llevar
   ademas la auditoria integral de cierre. **Ahi si tendrias el `PARA_ALEXIS.md` de campaña
   consumada pidiendote el merge.**
4. **Si la DECISION 1 es que no:** la Fase III se cierra **con remision**, como se cerro la
   fase 03 el 26 ago 2026, y `OP-I-01` queda nombrada como trabajo post campaña.

**`docs/loop/PROMPT_SIGUIENTE.md` queda VACIO. El bucle se detiene aqui.**
