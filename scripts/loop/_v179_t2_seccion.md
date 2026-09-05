### TAREA 2. `OP-L-03`: LOS DIEZ PARES REALES DE LOS ACTOS SIN LEER, LEIDOS

#### 2.a. LA CIFRA AL LADO, SIEMPRE LAS DOS, Y NINGUNA COPIADA DEL ENCARGO

Contada de `docs/loop/SALIDA_V179_T2_LOS_DIEZ.txt`, que sale de correr
`backlog_l03_resuelto.py` por dentro y no de teclear lo que el encargo dice:

| tramo | actos | pares del instrumento | pares reales |
|---|---:|---:|---:|
| actos QUE LA 177 LEYO | 6 | 29 | **8** |
| actos QUE NADIE HA MIRADO | 34 | 44 | **10** |
| **todo el backlog** | 40 | 73 | **18** |

**Los diez de la fila del medio son el trabajo de esta tarea**, y quedan leidos
los diez. **La columna vieja no se borra:** el instrumento sigue dando 73, y al
lado van los 18 reales.

#### 2.b. DONDE VA CADA VEREDICTO, Y LA DISTINCION NO SE DIFUMINA

**Ninguno de los diez tiene puesto en la cola**, medido y no supuesto:

| donde va el veredicto | pares |
|---|---:|
| `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` (TIENEN puesto) | **0** |
| `docs/plan/OP_L_03_LECTURAS.jsonl` (NO tienen puesto) | **10** |

**Y HAY QUE DECIR POR QUE SALE ASI, EN VEZ DE PRESENTARLO COMO UNA CASUALIDAD DE
ESTOS DIEZ.** Mi primera medicion de este campo estaba mal y la corrijo aqui:
preguntaba si alguno de los DOS EXTREMOS aparece en algun puesto, que es otra
cosa, y con esa vara los diez salian **SI**. La pregunta buena es si **EL PAR**
tiene puesto, y la respuesta es **NO para los diez y no puede ser otra**: un par
real esta definido por `medir_acto()` como el que **no esta ya en el archivo**,
asi que un par real nunca puede traer puesto. El archivo tiene hoy **3.388**
puestos ocupados, del **1** al **3.388**, **cero huecos**, y ninguno libre que
asignar. Eso explica ademas por que los **ocho** que la 177 leyo fueron todos al
registro y ninguno al archivo. **Se mide igualmente y se publica**, porque una
guarda que solo se mira cuando difiere no se puede auditar el dia que difiera.

**EL MARCADOR NO SE TOCA**, y se recomputa igual para poder decirlo
(`docs/loop/SALIDA_V179_T2_ESCRIBIR.txt`, bloque G): **A 551, B 72, C 5, D
2.760, total 3.388**. **Cero veredictos movidos**, comprobado por `sha256` antes
y despues, y los dos son `ea6e850d331d14f0`.

#### 2.c. COMO SE LEYERON, Y EL ARCHIVO SE MIRO ANTES DE JUZGAR

**Dos apoyos por par, y los dos van escritos en cada razon.** El primero es **la
vara del banco** (`9.6.1` y su rama contenido-manda, la linea o el
procedimiento) sobre los `pasos_accionables` de los dos extremos. El segundo es
**lo que el archivo ya dijo por un tercer nodo**, que `banco 9.3` obliga a mirar
porque **una direccion de fusion decidida sobre un par no sobrevive a su
familia**.

Lo mide `scripts/loop/vuelta179_tarea2_vecinos_del_archivo.py`
(`docs/loop/SALIDA_V179_T2_VECINOS.txt`), y **el resultado cambio mi lectura**:

| que salio | pares |
|---|---:|
| pares con al menos un tercero ya juzgado contra LOS DOS extremos | **10** |
| de esos, con una CADENA DE REPITE (los dos en `A` con el mismo tercero) | **7** |
| de esos, con una FRONTERA (uno en `A` y el otro en `D` con el mismo tercero) | **4** |
| pares sin ningun tercero comun | **0** |

**LO DIGO CLARO PORQUE ES UNA CORRECCION DE MI PROPIO TRABAJO EN CURSO:** habia
leido los diez por contenido y tenia **nueve `D` y una `A`**. Con el archivo
delante quedan **seis `A` y cuatro `D`**. **Las cinco que cambiaron las cambio el
archivo, no yo**, y en cada razon esta el puesto que lo hizo.

#### 2.d. LAS DIEZ LECTURAS, CON SU CLASE Y SU APOYO

| par | clase | quien lo sostiene en el archivo |
|---|---|---|
| `colaboracion_cadena_suministro` vs `diagnostico_efecto_latigo` | **A** | 730 (`A`) y 329 (`A`) por `efecto_bullwhip` |
| `compartir_datos_cadena_suministro` vs `diagnostico_efecto_latigo` | **D** | frontera 994 (`D`) contra 329 (`A`) |
| `compra_por_precio_mas_bajo_como_error` vs `relacion_largo_plazo_proveedor_unico` | **D** | dos fronteras en espejo, 2424/3102 y 2421/2927 |
| `creacion_option_pool` vs `employee_pool_esop` | **D** | frontera 1112 (`A`) contra 1193 (`D`). **DISCUTIBLE** |
| `disenar_tests_pass_fail` vs `diseno_experimentos_hipotesis` | **A** | 511 y 467, y el 511 declara la familia de TRES |
| `fase_diseno_prototipado_modelos` vs `prototyping_possibilities` | **A** | 641 (`A`) y 1056 (`A`) por `prototipado_modelos_negocio` |
| `proceso_ideacion_modelo_negocio` vs `prototyping_possibilities` | **D** | frontera 572 (`D`) contra 1056 (`A`) |
| `analisis_trafico_competitivo` vs `captura_conocimiento_mercado` | **A** | 508 y 941, y el 941 dice que el tercero es el mismo nodo |
| `crowdfunding_legal_exemptions_jobs_act` vs `cumplimiento_inversionistas_acreditados` | **A** | 462 (`A`) y 916 (`A`) por `equity_crowdfunding` |
| `evaluacion_tecnologias_disruptivas` vs `explotacion_tecnologias_disruptivas` | **A** | 505 (`A`) y 513 (`A`). **DISCUTIBLE** |

**El reparto: seis `A` y cuatro `D`, y seis mas cuatro son diez.**

#### 2.e. LOS OCHO ACTOS, CERRADOS CON SU FORMA Y SU COBERTURA

Cada uno lleva su `forma` escrita y su `cobertura` (`banco 9.26`) en
`docs/plan/OP_L_03_LECTURAS.jsonl`, que pasa de **6** filas a **14**, **ocho
anadidas por anexion y sin pisar ninguna de la 177**. **Los ocho quedan con cero
pares sin cubrir.** Lo que sale de leerlos enteros y no de a pares:

- **`colaboracion_cadena_suministro`**: una madre con **cero hermanos enlazados**
  y **dos hijos de paso**, y el contenido parte el acto en dos: el hijo de la
  medicion repite con la madre y el del compartir no.
- **`compra_por_precio_mas_bajo_como_error`**: **dos familias de dos** que se
  tocan en una linea y no se funden, cada una con su gemelo ya declarado y **los
  dos cruces en `D`**.
- **`creacion_option_pool`**: una familia de cuatro **partida en dos oficios con
  un nodo a caballo**. Es el unico de los ocho **en que el archivo se contradice
  consigo mismo** por dos terceros distintos, y eso queda escrito.
- **`disenar_tests_pass_fail`**: la familia de **tres** que el propio puesto 511
  declara, con una frontera comun enfrente que **no la parte**.
- **`fase_diseno_prototipado_modelos`**: un acto **partido en dos alturas**, y la
  misma pieza es **hija arriba y gemela abajo**. Dos de abajo se funden, el de
  arriba no.
- **`analisis_trafico_competitivo`**: un racimo de tres con un **gemelo
  ortografico** dentro, que es la figura mas barata de las ocho.
- **`crowdfunding_legal_exemptions_jobs_act`**: un racimo de tres sobre la misma
  regla de valores, **cerrado por el tercero**.
- **`evaluacion_tecnologias_disruptivas`**: el **par gemelo por nombre**, y con
  una cosa anotada que no cambia la clase: **no hay arista entre ellos** y el
  paso 4 de uno es la pregunta que el otro contesta. **No se toca**: la campana
  esta en modo de cierre.

#### 2.f. LO QUE QUEDA

**De los 18 pares reales, los 18 quedan leidos**, y no es una suma de cabeza: lo
cuenta `scripts/loop/vuelta179_tarea2_cobertura_final.py`
(`docs/loop/SALIDA_V179_T2_COBERTURA.txt`), que recorre los pares reales que el
instrumento da hoy y busca cada uno, **resuelto por `P.1`**, en el
`clases_de_los_pares_por_leer` de su acto. **Ocho** los escribio la 177 y **diez**
esta vuelta, **18 con lectura y 0 sin lectura**, y la resta cierra. **Cero pares
reales sin lectura en todo el backlog de `OP-L-03`.** El
estado de la ficha **NO se toca**, que es lo que `EJECUTOR.md` 4 manda mientras la
campana este en modo de cierre.
