### TAREA 4. LOS NUMEROS QUE FALTAN

**4.a LAS LECTURAS DIRIGIDAS SIN NUMERO `LD`: MEDIDAS, Y TRAIDAS COMO PARADA.**
Instrumento `scripts/loop/vuelta170_tarea4a_lecturas_sin_numero.py`, salida
`docs/loop/SALIDA_V170_T4A_LECTURAS_SIN_NUMERO.txt`, **exit 0**.

**LO QUE SE MIDIO PRIMERO, Y CALZA.** La segunda tanda se acota antes de contar
nada (`docs/plan/LECTURAS_DIRIGIDAS.md`, lineas **327 a 518**), sus tablas de
lectura se localizan por su cabecera `| par | clase |` y sus filas se cuentan:

| tabla | filas |
|---|---:|
| LOS CUADRANTES DE MERCADO: 15 de 15, y cae | 8 |
| LA ECUACION DE VALOR: 10 de 10, y cae | 5 |
| LA SUPERVISION DE LA IA, bloque humano: 10 de 10, y cae | 3 |
| **total** | **16** |
| de ellas **sin numero `LD`** | **16** |

La propia tanda dice en prosa **"SE LEEN DIECISEIS"**, y yo cuento **16**:
**CALZA**. Es contraste, no fuente.

**Y AQUI ESTA LA PARADA.** El encargo manda computar *"el siguiente libre ...
igual que `serie_de_registros.py` computa los `R.n`"*, y **la serie `LD` no se
parece a la serie `R.n`**. Corrido HOY el instrumento de la casa que ya existe
para esto, `scripts/loop/vuelta48_contar_ld.py`, salida
`docs/loop/SALIDA_V170_T4A_CONTAR_LD.txt`:

| que se mide | serie `R.n` | serie `LD` |
|---|---:|---:|
| entradas hechas | 31 | **82** |
| rango | R.9 a R.39 | **LD-01 a LD-138** |
| **huecos** | **0** | **54** |
| tramos corridos de huecos | 0 | **2**: LD-12 a LD-27 (**16**) y LD-100 a LD-137 (38) |

**CON CERO HUECOS, "EL SIGUIENTE LIBRE" TIENE UN SOLO SIGNIFICADO. CON 54, NO.**
Los dos caminos dan numeros distintos para las mismas 16 lecturas:

| camino | numeros | a favor | en contra |
|---|---|---|---|
| **1**, la vara literal del encargo (`mayor mas uno`) | **LD-139 a LD-154** | es la vara que el encargo nombra por su nombre, y **no inventa ninguna regla** | pone lecturas del **11 ago 2026** despues de `LD-138`, que es de una tanda muy posterior, y deja los 54 huecos donde estan |
| **2**, rellenar el tramo que encaja | **LD-12 a LD-27** | son **exactamente 16**, los mismos que filas; el tramo **empieza donde acaba la primera tanda (`LD-11`) y acaba donde empieza la tercera (`LD-28`)**, o sea que es el sitio cronologico exacto | **"rellenar huecos" NO es lo que `serie_de_registros.py` hace**, y adoptarlo seria **regla nueva** |

**NO ESCRIBO NINGUNA NUMERACION**, y no es prudencia: es que `EJECUTOR.md` 5
dice que no se inventan reglas, y el propio encargo dice, con estas palabras,
*"Si al contarlas el instrumento dice algo distinto de lo que este encargo
supone, PARAS Y LO TRAES."* **Lo dice, y lo hago.**

**LO QUE HACE FALTA PARA CERRARLA, Y CABE EN UNA LINEA:** decir si el siguiente
libre de la serie `LD` es **el mayor mas uno** o **el primer hueco**. Con esa
linea el instrumento escribe los 16 numeros en una vuelta.

**4.b LOS CINCO NODOS PUENTE DEL SALES ROADMAP: REGISTRADOS MEDIDOS Y NO
EJECUTADOS.** Instrumento
`scripts/loop/vuelta170_tarea4b_registrar_puentes.py`, salida
`docs/loop/SALIDA_V170_T4B_PUENTES.txt`, **exit 0**. Corrido antes en modo
medicion, que no toca la ficha.

**TODO MEDIDO EN ESTA VUELTA CON EL RESOLUTOR DELANTE POR `P.1`**, con la nomina
**parseada** de `scripts/vuelta16_generar_actos.mjs` y no tecleada: 6 miembros
escritos, **6 vivos tras resolver**, 0 colapsados, **15 pares posibles**, **15
con clase y CERO sin clase**, leidos de sus **dos** sedes (10 de la cola de
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` y 5 de las cabeceras `LD-66` a `LD-70` de
`docs/plan/LD_SALES_ROADMAP.md`).

**LOS CINCO PUENTES, COMPUTADOS DE ESAS CLASES Y NO COPIADOS DE NINGUN ACTA:**

| puente | sus dos `A` |
|---|---|
| `hoja_de_ruta_de_ventas` | `estrategia_de_ventas` , `refinar_sales_roadmap` |
| `refinar_sales_roadmap` | `hoja_de_ruta_de_ventas` , `sales_roadmap_vs_sales_force` |
| `refinar_sales_roadmap` | `sales_roadmap` , `sales_roadmap_vs_sales_force` |
| `sales_roadmap` | `estrategia_de_ventas` , `refinar_sales_roadmap` |
| `sales_roadmap_vs_sales_force` | `customer_validation_sales_roadmap` , `refinar_sales_roadmap` |

**El acta 169 y el reporte de la 169 dicen CINCO; yo computo CINCO: CALZA.**

**Y UNA COSA QUE MI MEDICION ANADE Y NADIE HABIA NOMBRADO:** el par
(`estrategia_de_ventas`, `refinar_sales_roadmap`) lleva **DOS** puentes encima,
`hoja_de_ruta_de_ventas` y `sales_roadmap`. **Eso es lo que `P.10` llama
COSTURA y no punto debil**, con sus palabras: *"un puente puede ser doble ...
y entonces la componente no tiene un punto debil: tiene una costura."*

**LA SALIDA DE `P.10` QUEDA NOMBRADA Y NO SE ELIGE AQUI:** es su **tercera fila
literal**, *"fundir solo el subconjunto CERRADO y enlazar el resto, si todas las
lecturas estan hechas y aun asi se contradicen"*, porque la cobertura es **15 de
15** y por tanto la primera salida, **la unica que resuelve de verdad, ya no
existe**.

**POR QUE NO SE EJECUTA, Y LA BUSQUEDA NEGATIVA VA CON SU COMANDO** (`EJECUTOR.md`
9, *"una busqueda negativa no se puede citar"*): se barrieron **las 71 fichas**
de `docs/plan/OPERACIONES.jsonl` buscando los 6 nodos vivos en los campos
`nodos`, `preservar`, `eliminar` y `superviviente`, y salieron **CERO**.
**Ninguna operacion escrita recoge esta fusion**, y ejecutar una fusion que
ninguna ficha ordena es la improvisacion que `AUDITOR.md` seccion 3 prohibe con
esas palabras.

**LO ESCRITO:** un registro por adicion dentro del campo `nota` de `OP-L-02` que
ya existe, **sin clave nueva de esquema**. La nota pasa de **3.106 a 5.578
caracteres** y **solo crece**; la nota vieja sigue **entera** dentro; los cinco
puentes se nombran en la nota de disco, **5 de 5**; 71 fichas antes y despues;
**cero campos movidos** ademas de `nota`; y el `estado` sigue diciendo `LISTA`.
