### TAREA 3. LA RELECTURA AL DOBLE DEL TRAMO DE LA CIEGA DEL ACTA 187. **CERRADA, Y CON UNA DESVIACION DECLARADA.**

**EL COTEJO DEL `sha256` VA ANTES DE LEER UN SOLO PUESTO, Y SE COMPUTO EN VEZ DE
COPIARSE DEL ENCARGO.**

| | el sello dice | medido hoy | |
|---|---|---|:-:|
| `docs/loop/SELLO_APERTURA_AUDITOR_V188.json` | | disco **802** bytes, LF **802** bytes | |
| bytes de la ciega | **42599** | **42599** | **CALZA** |
| `sha256` de la ciega | `ea6d846cb7e0c73e0d2e9794906b2551bb32d939b8ad88f02bbc473b73e79c55` | identico | **CALZA** |

**`EL FICHERO ES EL QUE EL SELLO DICE: SI`.** El nombre del sello **no se dedujo
del numero de vuelta**: siendo acta **187**, se llama **`V188`**. **El `V186` no
existe y no se fabrica.**

**EL TRAMO Y SU DOBLE.** El tramo se leyo de la ciega sellada, **no del acta**,
que en su seccion 4 (lineas **65635 a 65699**, cabecera *"LA RELECTURA CIEGA: 26
DE 30, Y LAS CUATRO LAS PIERDO YO"*) lista **0 puestos**.

- **30 puestos del tramo**: 226, 252, 255, 293, 426, 603, 954, 1222, 1286, 1332,
  1341, 1367, 1509, 1540, 1612, 1676, 1703, 1910, 1912, 1953, 2124, 2177, 2382,
  2448, 2834, 2953, 3030, 3158, 3314, 3340.
- **30 vecinos deterministas**, con `vecinos()` **IMPORTADA** de
  `scripts/loop/vuelta182_tarea1c_relectura_al_doble.py` y **no copiada**.
- **60 puestos releidos. `ES EL DOBLE DEL TRAMO: SI`.**

**LOS TRES SOLAPES, MEDIDOS Y NO SUPUESTOS. Y EL TERCERO NO SALE CERO, ASI QUE SE
DECLARA EN VEZ DE ARREGLARSE.**

| solape | contra | cifra |
|---|---|---:|
| **F.1** | el tramo contra sus vecinos | **0** |
| **F.2** | el tramo contra `docs/loop/_auditor_v187_ciega_blind.txt` (30 puestos) | **0** |
| **F.2** | el **universo entero** contra esa misma ciega | **0** |
| **F.3** | el **tramo** contra los puestos de `docs/loop/_auditor_v188_exclusion.txt` | **0** |
| **F.3** | el **universo entero** contra esa misma exclusion | **2** |

**La exclusion mide 1372 bytes y lista 293 puestos distintos, CONTADOS del
fichero y no copiados del criterio.** Los dos que cruzan son **1287** (vecino
determinista del **1286**) y **2383** (vecino determinista del **2382**), **los
dos VECINOS y ninguno del tramo**.

> **POR QUE NO LO ARREGLO, Y ES UNA DESVIACION DECLARADA Y NO UN DESCUIDO.** El
> encargo pide **solape 0 con los 293**. **El tramo lo cumple: 0.** Los que
> cruzan salen de `vecinos()`, que es una funcion **importada y congelada**;
> cambiarla aqui para que la cifra saliera cero seria **mover la vara a mitad de
> la medicion**, que es exactamente lo que `P.5.1` prohibe. **Se publica la cifra
> y se nombran los dos puestos.** **DISCUTIBLE DE METODO, MARCADO.**

**LAS CIFRAS DE LA RELECTURA MECANICA, con la maquina IMPORTADA de
`scripts/loop/vuelta182_tarea3_diferenciador_movido.py`:**

| | cifra |
|---|---:|
| puestos releidos | **60** |
| que declaran diferenciador | **3** |
| con **lesion exacta** | **0** |
| con algun **nodo muerto** en el grafo de hoy | **0** |
| clase `A` en el universo | **8** |
| clase `B` en el universo | **4** |
| clase `D` en el universo | **48** |

**`NINGUNA CLASE SE VOLVIO A DECIDIR.`** Esta relectura es la **mecanica** del
tramo con la vara, no una lectura de juicio.

**LAS CUATRO DISCREPANCIAS DEL AUDITOR, MIRADAS CON LA MISMA VARA. LAS CUATRO
CAEN DENTRO DEL UNIVERSO RELEIDO.**

| puesto | clase | declara | lesion | nodo muerto | nodos |
|---:|:-:|:-:|:-:|:-:|---|
| **226** | `B` | no | no | no | `antidilucion_provisiones` contra `antidilution_weighted_average_broad_narrow` |
| **603** | `B` | no | no | no | `decision_autofinanciamiento_vs_inversion` contra `decision_intensidad_capital` |
| **1612** | `D` | no | no | no | `elegir_caja_correcta` contra `elegir_resistencia_caja_peso` |
| **2448** | `D` | **SI** | no | no | `entrenamiento_y_control_estadistico` contra `importancia_de_la_capacitacion` |

**LO QUE LA VARA VE, Y NI UNA PALABRA MAS:** de los cuatro, **solo el 2448
declara un diferenciador**, y **ninguno de los cuatro tiene lesion exacta ni nodo
muerto**. **Lo que la vara no ve, aqui no se afirma.**

**EL CENSO DE LAS `B` DEL UNIVERSO, UNA POR UNA CON SUS TRES COMPROBACIONES.
SOLO SE CUENTA Y SE PUBLICA.**

| puesto | declara diferenciador | lesion exacta | nodo muerto | nodos |
|---:|:-:|:-:|:-:|---|
| **226** | NADA | NADA | NADA | `antidilucion_provisiones` contra `antidilution_weighted_average_broad_narrow` |
| **253** | NADA | NADA | NADA | `fase_acclimate` contra `fase_acclimate_experiencia_cliente` |
| **603** | NADA | NADA | NADA | `decision_autofinanciamiento_vs_inversion` contra `decision_intensidad_capital` |
| **604** | NADA | NADA | NADA | `mapa_de_influencia` contra `mapa_organizacional_influencia` |

| la cuenta | cifra |
|---|---:|
| `B` en el universo releido | **4 de 60** |
| `B` que declaran diferenciador | **0** |
| `B` con lesion exacta | **0** |
| `B` con algun nodo muerto | **0** |
| **`B` que dan NADA en las tres** | **4 de 4** |
| `B` en TODO el archivo, contadas del archivo | **72 de 3388 filas** |
| de las cuatro discrepancias, cuales son `B` | **226 y 603** |

> **Y AQUI SE PARA.** Esta salida **no dice** que la vara sea ciega a la clase
> `B`, **no adjudica** ninguna de estas cuatro y **no propone** nada. Publica la
> cuenta y las tres columnas, que es exactamente lo que el encargo pide. **Si la
> vara resulta ciega a la clase `B` entera, eso es un hallazgo del fundador y no
> mio.**

**EL COTEJO DE LOS CLONES DECLARADOS DE ESTA VUELTA, CON LO QUE SALGA Y SIN
AFIRMAR QUE NINGUN DIFF SALE VACIO** (`docs/loop/SALIDA_V187_COTEJO_DE_CLONES.txt`,
tres cotejos, los tres con `EXITCODE: 0`):

| clon | fichero entero | docstring | maquina | AST sin docstring | lineas de maquina que difieren |
|---|:-:|:-:|:-:|:-:|---:|
| `vuelta186_apertura.py` a `vuelta187_apertura.py` | DIFIERE | DIFIERE | DIFIERE | DIFIERE | **452** |
| `vuelta186_esqueleto_reporte.py` a `vuelta187_esqueleto_reporte.py` | DIFIERE | DIFIERE | DIFIERE | DIFIERE | **68** |
| `vuelta186_tarea1c_relectura_al_doble.py` a `vuelta187_tarea3_relectura_al_doble.py` | DIFIERE | DIFIERE | DIFIERE | DIFIERE | **148** |

**Los tres DIFIEREN por los cuatro veredictos, y es lo esperado:** un clon
declarado de esta casa cambia el sufijo, las rutas, los bloques propios y las
glosas. **La afirmacion de clon se mide, no se promete.**
