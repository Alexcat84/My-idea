### TAREA 4. LA ENTRADA A LA COLA, Y EL TRAMO DECLARADO

Instrumento `scripts/loop/vuelta182_tarea4_entrar_a_la_cola.py`, salida
`docs/loop/SALIDA_V182_T4_COLA.txt` (**1.054 bytes**). Escribe en
`docs/plan/08_VERIFICACION.md` la seccion **LA ENTRADA POR EL DIFERENCIADOR
MOVIDO (5 sep 2026, vuelta 182)**, generada **leyendo el JSON de la TAREA 3** y no
tecleada.

**LA SEDE, MEDIDA ANTES Y DESPUES:** `docs/plan/08_VERIFICACION.md` pasa de
**64.355** a **67.121 bytes** y de **833** a **882 lineas**; **crece 2.766 bytes** y
**lineas que desaparecen: 0**. La lista del 12 ago 2026 sigue entera y el ancla
tambien, las dos comprobadas releyendo el fichero del disco.

**LO QUE ENTRA A LA COLA: el puesto 2.464, y nada mas.** Es la unica `D` que pasa
las tres condiciones. **El tramo queda declarado aqui y no se improvisa despues:**
**TRAMO 1 y unico con lo medido hoy, el unico par de arriba**, y se relee **entero
o no cuenta**; si el instrumento volviera a nombrar mas, cada grupo nuevo abre **su
propio tramo con su fecha**.

> **EN ESTA VUELTA NO SE RELEE NINGUN PAR**, que es literalmente lo que el encargo
> manda: *"se entra a la cola y se declara el tramo; no se releen 543 pares, que es
> justo lo que la decision evita"*. Ninguna clase cambia y el archivo de veredictos
> no se toca.

> **SOBRE `verificar_mapas_destejido.py`:** `EJECUTOR.md` 1 lo exige para **toda
> tabla de particion** (fila = destino, origenes, motivo). **La tabla de esta cola
> no es de particion**: sus filas son `par | clase | que le pasa | tras que
> operacion`, no hay destino ni origenes y no reparte nada. **Se dice, en vez de
> correr un instrumento sobre una tabla que no es la suya y publicar un verde que
> no significa nada.**
