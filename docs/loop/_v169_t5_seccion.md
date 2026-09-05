### TAREA 5, EL LOTE DE SALES ROADMAP: ESTA LEIDO DESDE HACE TRES SEMANAS, Y LO COMPRUEBO LEYENDOLO A CIEGAS PRIMERO

**Salidas:** `docs/loop/SALIDA_V169_T5_LOTE_SALES_ROADMAP.txt` y
`docs/loop/SALIDA_V169_T5_COBERTURA_OP_L_02.txt`.
**Instrumentos:** `scripts/loop/vuelta169_tarea5_lote_sales_roadmap.py` y
`scripts/loop/vuelta169_tarea5_cobertura_op_l_02.py`.

**(5.a) LO QUE EL ENCARGO SUPONE Y LO QUE LA MEDICION DICE.** El encargo manda
leer cinco pares con estas palabras: *"YO NO LOS LEI Y NO LES PUSE CLASE"*, y la
ficha de `OP-L-02` lo sostenia, porque su nota decia *"NO se leyeron los 5 de
sales roadmap"*. **MEDIDO HOY: LOS CINCO ESTAN LEIDOS DESDE EL 14 ago 2026**,
como `LD-66` a `LD-70`, saldo **1 A y 4 D**. **CUMPLIDO POR CONSUNCION**, que es
la misma especie que la parada de la vuelta 167 sobre `OP-C-01` y que la `6.6`
del acta 168 sobre las dos `OP-M-02`.

**CUATRO SEDES INDEPENDIENTES LO DICEN, Y LAS CUATRO SE LEYERON HOY** (seccion C
de la salida): las cinco cabeceras de `docs/plan/LD_SALES_ROADMAP.md`; la fila
del universo de `docs/plan/LECTURAS_DIRIGIDAS.md`, donde el `5` pendiente esta
**tachado y puesto a `0`**; y las **dos** entradas de `INVENTARIO.jsonl` (el acto
`customer_validation_sales_roadmap` y el racimo `el sales roadmap`), las dos con
cobertura **15 de 15** citando `LD-66 a LD-70` por el carril del 9.10.

**Y LA QUINTA NO ES UNA CITA: ES LA RELECTURA A CIEGAS.** Clasifique los cinco
pares por mi cuenta, con la vara del banco `9.6.1` y sus precisiones `9.6.2` (la
vara tiene direccion) y `9.6.3` (el tamano del solape no decide), mas `P.11` (una
advertencia es linea, no procedimiento), **leidas en su fuente y no de memoria**,
y con los diez veredictos de cola delante. **Escribi las cinco clases y marque
los discutibles ANTES de abrir `LD_SALES_ROADMAP.md`.** Tabla pegada entera de la
seccion D:

| par | ciega del ejecutor | el archivo | coincide | marcado DISCUTIBLE |
|---|:-:|:-:|:-:|:-:|
| `customer_validation_sales_roadmap` contra `estrategia_de_ventas` | D | D (LD-66) | SI | no |
| `customer_validation_sales_roadmap` contra `sales_roadmap` | D | D (LD-67) | SI | no |
| `estrategia_de_ventas` contra `hoja_de_ruta_de_ventas` | A | A (LD-68) | SI | **SI** |
| `estrategia_de_ventas` contra `refinar_sales_roadmap` | D | D (LD-69) | SI | **SI** |
| `estrategia_de_ventas` contra `sales_roadmap_vs_sales_force` | D | D (LD-70) | SI | no |

**COINCIDEN 5 DE 5.** Saldo de la ciega `A 1, D 4`; saldo del archivo `A 1, D 4`.
**Y los dos que marque DISCUTIBLE son los dos que de verdad me costaron**, con su
motivo escrito antes de saber el resultado: el `LD-68` porque solo `P.11`
resuelve si lo que anade `hoja_de_ruta_de_ventas` es procedimiento o linea, y el
`LD-69` porque su `D` **crea un triangulo `A` mas `A` mas `D`** con los puestos
192 y 966.

**NO HAY CASO ROJO AUTOMATICO PARA LA CIEGA, Y SE DECLARA EN VEZ DE FABRICARSE
UNO.** La tabla de mis cinco clases es **a mano** y no hay nada que mutar en ella
que pruebe algo; fabricar un `assert` que se aprobara solo seria la caida 2 de la
vuelta 89. **Lo que si cae es el cotejo**, si el archivo cambiara sus clases.

**(5.b) NO HAY NOMINA SIGUIENTE QUE LEER, Y NO ES POR FALTA DE VUELTA: ES POR
MEDICION.** Las **seis** nominas de `OP-L-02`, recomputadas hoy con el resolutor
delante y contando **las tres sedes** (cola, cabeceras `LD-nn` y filas de tabla
de la segunda tanda):

| # | nomina | posibles | cola | dirigidas | SIN | cobertura |
|---:|---|---:|---:|---:|---:|---|
| 1 | `customer_validation_sales_roadmap` | 15 | 10 | 5 | 0 | **15 de 15** |
| 2 | `clasificacion_mercados_cadena_suministro` | 0 | 0 | 0 | 0 | **0 de 0** |
| 3 | `alineacion_etica_ia_negocio` | 10 | 7 | 3 | 0 | **10 de 10** |
| 4 | `construccion_de_valor_percibido` | 10 | 5 | 5 | 0 | **10 de 10** |
| 5 | `channels_hypothesis_physical` | 10 | 8 | 2 | 0 | **10 de 10** |
| 6 | `formalizar_junta_asesora` | 1 | 1 | 0 | 0 | **1 de 1** |

**46 pares posibles, 0 sin veredicto, 6 de 6 nominas con cobertura COMPLETA.**

**LA NOMINA 2 DA CERO PARES POSIBLES, Y NO ES UN HUECO: SUS SEIS MIEMBROS
RESUELVEN AL MISMO NODO VIVO.** Ya esta fundida. La 6 baja de cuatro miembros a
dos por lo mismo. **Contarlas como nominas sin leer habria sido contar dos veces
lo que la cirugia ya cerro.**

**UNA CAIDA MIA EN ESTE MISMO INSTRUMENTO, CAZADA MIDIENDO Y DECLARADA.** Su
primera version solo leia las lecturas dirigidas con cabecera `### LD-nn`, y la
SEGUNDA TANDA de `LECTURAS_DIRIGIDAS.md` las escribe como **filas de tabla sin
numero**. Daba `7 de 10` donde la ficha declara `10 de 10`. **Publicar esa cifra
habria sido publicar el hueco del lector como si fuera un hueco del archivo.**
Corregido con el segundo patron, y las dos formas se cuentan **aparte** para que
se vea de cual sale cada par.

**LO QUE LA COBERTURA COMPLETA DEJA VER, Y ES LO QUE `P.10` DICE QUE SOLO SE VE
ASI: CINCO NODOS PUENTE** en la nomina del sales roadmap (seccion F):

| puente | sobre |
|---|---|
| `hoja_de_ruta_de_ventas` | (`estrategia_de_ventas`, `refinar_sales_roadmap`) |
| `refinar_sales_roadmap` | (`hoja_de_ruta_de_ventas`, `sales_roadmap_vs_sales_force`) |
| `refinar_sales_roadmap` | (`sales_roadmap`, `sales_roadmap_vs_sales_force`) |
| `sales_roadmap` | (`estrategia_de_ventas`, `refinar_sales_roadmap`) |
| `sales_roadmap_vs_sales_force` | (`customer_validation_sales_roadmap`, `refinar_sales_roadmap`) |

**`P.10` dice que la componente NO se funde hasta que ese triangulo se cierre**, y
que un puente **solo se ve mirando la componente entera**. **Los traigo medidos y
NO los resuelvo: ninguna clase se mueve por esta vuelta.**

**LO ESCRITO:** la nota de `OP-L-02` corregida por el carril del 9.10, con la
frase *"NO se leyeron los 5 de sales roadmap"* **tachada y entera**. **Esa frase
era cierta el dia que se escribio y dejo de serlo tres dias despues**: lo que se
corrige no es una mentira, es **una nota que no siguio a su sujeto**.
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` **no se toca**, cero campos movidos ademas
de `nota`, y el `estado` sigue en `LISTA`, que es lo que la 6.7 reserva.
