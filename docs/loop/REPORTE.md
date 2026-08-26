# REPORTE DE LA VUELTA 69: EL LOTE E DEL TRAMO UNICO DE `OP-U-02`, CINCO FUSIONES, UN DECLARADO Y DOS COLISIONES FABRICADAS

**Fase III, ejecucion continua. Rama `pasada-unica`. 26 ago 2026.**

**FECHA POR DOS RELOJES, CORRIDOS POR MI:** el reloj del sistema da **2026-08-26** y `git log -1
--date=format` sobre el ultimo commit da **2026-08-26**. **Toda cifra de este reporte tiene ese
corte.** La vuelta abrio con el arbol limpio en `763edb5c` y sin cruzar medianoche.

---

## 1. LA CABECERA, TALLADA Y NO TECLEADA

**Generada entera con** `python scripts/loop/tallar_cabecera_reporte.py --vuelta 69` y **pegada sin
tocar una celda** ([`SALIDA_V69_CABECERA.txt`](SALIDA_V69_CABECERA.txt)). **La celda que no salga de
un instrumento no se escribe.**

| | **apertura**, antes de la 1.ª operacion | **cierre, RECOMPUTADO al cierre** |
|---|---:|---:|
| marcador `A` / `B` / `C` / `D` | 551 / 72 / 5 / 2.760 | **551 / 72 / 5 / 2.760** |
| `n`, huecos, duplicados | 3.388 / 0 / 0 | **3.388 / 0 / 0** |
| grafo: ficheros / vivos / deprecados / enlaces | 3.853 / 3.237 / 616 / 17.562 | **3.853 / 3.224 / 629 / 17.588** |
| retrato: `A` crudas / colapsos / pares distintos | 551 / 325 / 226 | **551 / 340 / 211** |
| actos (componentes) | 72 | **67** |
| actos `CERRADOS` / `ABIERTOS` | 26 / 46 | **26 / 41** |
| nodos en `CERRADOS` / `ABIERTOS` | 61 / 199 | **61 / 181** |
| cola de costuras | 1.447 | **1.443** |
| colisiones de clase vigentes | 4 | **6** |
| auto-pares (los dos lados al mismo vivo) | 263 | **268** |
| duplicadas historicas: grupos / nodos | 913 / 723 | **912 / 722** |
| operaciones, estados, dependencias rotas | 71, todas `LISTA`, 0 | **71, todas `LISTA`, 0** |
| entradas del inventario | 672 | **672** |
| las cuatro comprobaciones de `08_VERIFICACION` | TODAS OK (260 igual a 260; 226 igual a 226) | **TODAS OK (242 igual a 242; 211 igual a 211)** |

**LA APERTURA SE MIDIO ANTES DE LA PRIMERA OPERACION** (regla 1): los seis instrumentos de apertura
corrieron con el arbol limpio en `763edb5c`, **antes de escribir nada**, y `git status --porcelain`
tras correrlos dio **CERO ficheros rastreados movidos** (solo las salidas nuevas, sin trackear).
**EL CIERRE SE RECOMPUTO AL CIERRE**, despues de que las cinco fusiones y `run_phase1` movieran el
arbol.

**LA APERTURA DE HOY CALZA AL DIGITO CON EL CIERRE QUE EL ACTA 68 PUBLICO** (72 componentes, 46
`ABIERTOS` sobre 199, cola 1.447, colisiones 4, auto-pares 263, duplicadas 913/723, enlaces 17.562,
3.237 vivos y 616 deprecados), **que es el contraste que la regla 2 permite**: entre las dos vueltas
nadie movio dato.

**LA ARITMETICA DEL SALTO ES COHERENTE ENTERA, y se dice para que no haya que reconstruirla:** cinco
actos fundidos son **menos 5 componentes** (72 a 67), **menos 18 nodos abiertos** (199 a 181),
**menos 13 vivos** (3.237 a 3.224) y **mas 13 deprecados** (616 a 629). La cola baja 4 y las
duplicadas 1.

---

## 2. TAREA 1: EL REGISTRO DEL ACTA 68

`python scripts/loop/vuelta69_registrar_acta68.py`
([`SALIDA_V69_REGISTRO_ACTA68.txt`](SALIDA_V69_REGISTRO_ACTA68.txt)), adosado al final de
[`../plan/03_FUSIONES.md`](../plan/03_FUSIONES.md) **sin reescribir ni una linea de arriba**
(`git diff --numstat`: **`170 0`**).

### 2.1 **LO QUE QUEDA REGISTRADO** (apartados a) a h) de la seccion nueva)

- **LA CAIDA DE REPORTE DEL `D9` CON SU MEDICION**, partida en cinco citas de linea distintas para
  que cada mitad de la frase apunte a la linea que de verdad la dice: **el reporte dijo CUATRO**, **el
  auditor midio SEIS**, **las seis filas nombradas** (3, 4, 7, 8, 9 y 10), **las DOS del pendiente 4**
  y **la lectura con la que el cuatro se entiende y por que no basta**.
- **LA REGLA QUE SALE DE ESA CAIDA**, escrita para que valga sobre todo lote: **toda cuenta agregada
  sobre una tabla se deriva CONTANDO POR MAQUINA en la corrida de esa vuelta**, y **si se excluyen
  filas porque otro discutible las cubre, la frase lo DICE**.
- **EL CONTADOR DE PARADA DE VUELTA A CERO** y **la racha de reporte rota en la cuarta**, con las dos
  cifras leidas de sus lineas.
- **LOS DIECISEIS DISCUTIBLES `A FAVOR`** con su vara citada, uno por fila y con su linea.
- **LAS TRES ADJUDICACIONES NUEVAS**: el superviviente del `acto 18` con sus **cuatro letras** y **las
  CINCO piezas** que el plan tenia que conservar o sellar; **el dueno MEDIDO con su frontera escrita**;
  y **el carril del plan propio del lote `E`**.
- **LOS PENDIENTES HEREDADOS CON SU DESTINO**, los cuatro, mas la parada del cierre de la fase 03.

### 2.2 **LA GUARDA DE CITAS: HEREDADA ENTERA Y COPIADA, NO IMPORTADA, Y VA DICHO POR QUE**

**El acta 68 escribio la regla en su `D14`:** importar vale **DENTRO DE LA MISMA VUELTA**, y el carril
de **copiar** es el que protege a los registradores **de VUELTAS DISTINTAS** de divergir en silencio.
El registrador del acta 68 es de otra vuelta, asi que **la maquina se copio entera** (`derivar`,
`negativas`, `sustituir`, `cotejar_texto`), y **lo unico propio son las agujas**. **El registrador del
lote `E`, que es de ESTA vuelta, si la importa.** **Las dos mitades de la regla aplicadas el mismo
dia.**

| mecanismo | medido en esta vuelta |
|---|---|
| **1. las citas se derivan por aguja** | **64 agujas** en el registro del acta y **18** en el del lote, **cero tecleadas** |
| **2. el texto nuevo se coteja antes de escribir** | **17** citas canonicas en el del acta y **15** en el del lote, **MALAS 0** en los dos |
| **la red ancha** (todo numero de 3 a 5 digitos en negrita) | **67** numeros en el del acta (3 declarados) y **50** en el del lote |
| **las agujas NEGATIVAS** | **2, y las dos de sustancia**: la linea del `CUATRO` del `D9` **NO** contiene `SEIS` (por eso las dos mitades van a citas distintas), y la linea que adjudica el superviviente del `acto 18` **NO** nombra a ningun otro miembro. **Las dos `OK`** |
| **cero citas muertas** | **64 de 64** y **18 de 18** |
| **idempotencia** | **MUERDE en los dos** (`YA ADOSADA` y `YA ADOSADO` en la segunda corrida) |
| **re-cotejo tras adosar** | **`OK (64 de 64)`** y **`OK (18 de 18)`** |

> **LA GUARDA NO MORDIO EN ESTA VUELTA, Y SE DICE EN VEZ DE PRESUMIR DE VERDE:** los dos
> registradores salieron limpios **en su primera corrida**. En la vuelta 68 la guarda saco `ROJO` con
> 14 fallos y con 9; aqui con **0** y **0**. **Que una guarda pase no prueba que mida**: lo que
> prueba que mide son las dos agujas negativas, que si comprobaron una afirmacion que podia ser
> falsa, y el caso positivo de promesas de la seccion 9.

---

## 3. TAREA 2: EL LOTE E, DECLARADO AL ABRIRLO Y ENTREGADO ENTERO

**EL LOTE ABRE CON LA FUSION ADJUDICADA DEL `ACTO 18`** (acta 68, adjudicaciones 1 y 3), **ejecutada
como PRIMERA operacion y dentro de un PLAN PROPIO**: el plan del lote `D` **no se reabrio**, y el acto
**cuenta** en la declaracion como cierre ENTERO. **Despues, el PREFIJO SIN SALTOS desde el `acto 25`**
del `orden_universo` de lo que quedaba del tramo fijado en
[`TRAMO_UNICO_OPU02_V64.jsonl`](TRAMO_UNICO_OPU02_V64.jsonl).

**SE DECLARARON SEIS ACTOS Y 22 NODOS, Y SE ENTREGARON LOS SEIS.**

| acto | miembros | cierra | **FORMA medida** | superviviente |
|---:|---:|---|---|---|
| **18** | 4 | **FUNDIDO** | `EMPATE SIN VARA` | `alianzas_cross_industry`, **adjudicado por el auditor** |
| **25** | 4 | **FUNDIDO** | `CONTENIDO EMPATA` | `enfoque_etapa_investigacion`, **que es PUERTA** |
| **26** | 4 | **FUNDIDO** | `CHOCAN` | `investigacion_etnografica_ideacion`, **que es PUERTA** |
| **27** | 4 | **`DECLARADO Y NO FUNDIDO`** | `TODAS DE ACUERDO` | ninguno se elige |
| **29** | 3 | **FUNDIDO** | `UNA SOLA VARA` | `marco_avances_continuaciones` |
| **30** | 3 | **FUNDIDO** | `CHOCAN` | `viaje_diagnostico_remedial` |

**EL TOPE DEL PREFIJO ES ESTRUCTURAL Y SE DICE, en vez de dejarlo como un numero elegido:** el
siguiente es el **`acto 31`**, y **ese acto TIENE DUENO** (`OP-F-04-WEI` y `OP-S-04` en
`duenos_cualquier_operacion`, medido hoy sobre el fichero fijado). **El encargo prohibe FUNDIR un acto
con dueno**, y el `acto 31` **no trae ninguno de los cuatro motivos sellados** con los que podria
cerrar `DECLARADO` (cero pares `D`, cero puentes, cero triangulos, una familia, una sola puerta,
medido). **O sea que no podria cerrar ENTERO**, y el contrato es entregar lo declarado: **el tope cae
ANTES de el y no despues.**

### 3.1 **`P.5` CONTESTADA ACTO POR ACTO, SOBRE EL TEXTO ESTABLE**

**El acto se leyo ENTERO** con `python scripts/loop/dossier_del_tramo.py --tramo
docs/loop/TRAMO_UNICO_OPU02_V64.jsonl --actos 18,25,26,27,29,30`
([`SALIDA_V69_DOSSIER_LOTE_E.txt`](SALIDA_V69_DOSSIER_LOTE_E.txt), **470 lineas**), con **todos sus
pares internos y su razon entera**.

| acto | libro o libros | pares `A` | pares `D` | puentes | triangulos | puertas | **una familia o dos** |
|---:|---|---:|---:|---:|---:|---:|---|
| **18** | Esty (los 4) | 3 | 0 | 0 | 0 | 0 | **UNA**, y la declara el archivo: el **1871** la ve pasar de dos a tres y el **1903** de tres a cuatro |
| **25** | Rackham (los 4) | **5** | 0 | 0 | 0 | **1** | **UNA**, y **es el acto mejor leido del prefijo**: cinco de seis pares, los cinco en `A` |
| **26** | Brown (2), Cooper (2) | 3 | 0 | 0 | 0 | **1** | **UNA**, y el **839** es **el par que CRUZA** las dos parejas: cuatro nodos del mismo instrumento |
| **27** | Osterwalder (3), Value Proposition Design | 3 | **1** | **1** | **1** | 0 | **UNA, MEZCLADA**, y ademas **una FIGURA con centro y periferia** |
| **29** | Rackham (los 3) | 2 | 0 | 0 | 0 | 0 | **UNA**, y los dos veredictos dicen `REPITE` |
| **30** | Juran (los 3) | 2 | 0 | 0 | 0 | 0 | **UNA**, y el **2838** la cierra `A` **POR CONTENCION** |

**MEDIDO** con `python scripts/loop/vuelta65_puentes_del_tramo.py --tramo ... --detalle`
([`SALIDA_V69_PUENTES_TRAMO.txt`](SALIDA_V69_PUENTES_TRAMO.txt)), **con los ids pasados por el
resolutor (`P.1`)**, y las puertas con `varas_n_arias_del_tramo.py` contra el universo protegido de
**256 ids**.

**LA RESPUESTA *DOS FAMILIAS* DE `P.5` NO SE USO EN NINGUN ACTO DE ESTE LOTE: los SEIS contestaron UNA
familia**, y se dice porque un motivo sellado que no se usa se cuenta como usado si nadie lo dice.

### 3.2 **LAS VARAS POR FORMA, CON SU LETRA Y MEDIDAS POR INSTRUMENTO**

`python scripts/loop/varas_n_arias_del_tramo.py --tramo ... --actos 18,25,26,27,29,30,31`
([`SALIDA_V69_VARAS_N_ARIAS.txt`](SALIDA_V69_VARAS_N_ARIAS.txt)). **Formas del prefijo, contadas por
el instrumento: 1 `EMPATE SIN VARA`, 1 `CONTENIDO EMPATA`, 3 `CHOCAN` (uno de ellos es el `acto 31`,
que NO entra al lote), 1 `TODAS DE ACUERDO` y 1 `UNA SOLA VARA`.**

| acto | pasos | condiciones | cableado | **la letra que decide** |
|---:|---|---|---|---|
| **18** | empatan los 4 en 4 | empatan los 4 en 2 | **empatan dos en 3** | **ninguna vara apunta**: es la fila de `P.8` que dice *empatado y el cableado tambien: se trae al auditor*. **El auditor ya contesto**, y este plan **ejecuta** esa adjudicacion |
| **25** | empatan los 4 en 4 | empatan tres en 2 | **apunta a `enfoque_etapa_investigacion`** (6 contra 3) | **el cableado DECIDE SOLO**, que es el unico supuesto en que `P.8` le da la palabra. **Y apunta a la MISMA puerta que la guarda `1B` obliga a conservar: no hay choque que resolver** |
| **26** | apuntan a `investigacion_etnografica_ideacion` (6 contra 5) | apuntan al OTRO (3 contra 2) | apunta al primero (14 contra 8) | **`CHOCAN`: decide LA PIEZA DECLARADA**, y las otras dos cuentas y la puerta apuntan al mismo sitio. **Este `CHOCAN` no deja residuo** |
| **27** | apuntan a `prototipado_modelos_negocio` (6 contra 5) | al mismo (3 contra 2) | al mismo (14 contra 9) | **la forma mas limpia del prefijo, y aun asi no se funde: `P.10` detiene ANTES** |
| **29** | empatan los 3 en 4 | **apuntan a `marco_avances_continuaciones`** (2 contra 1) | empatan dos en 3 | **UNA SOLA VARA BASTA**: donde el contenido dice algo, el contenido manda, y aqui lo dice la unica que no empata |
| **30** | apuntan a `viaje_diagnostico_remedial` (8 contra 5) | apuntan al OTRO (2 contra 1) | **EMPATA en 4** | **`CHOCAN`: decide LA PIEZA DECLARADA**, y aqui la declaracion es **verbatim**: el **2838** cierra con *A, superviviente `viaje_diagnostico_remedial`* |

**EL ROTULO SOLO Y LA CANTIDAD NUNCA DECIDEN**, y **ninguna vara se teclea**: las tres cuentas por
miembro salen del instrumento.

**LA GUARDA `1B` MUERDE EN DOS ACTOS Y NO PARA NINGUNO**, que es la mitad de su letra que menos se
usa: con **UNA** puerta el acto **si se funde y la puerta SOBREVIVE** (acta 54, pregunta 1); lo que
cierra `DECLARADO` es **DOS o mas**. **Es la primera vez del tramo que esa mitad se aplica dos veces
el mismo dia.**

### 3.3 **LAS CINCO FUSIONES, EN CIFRAS DEL INSTRUMENTO**

`python scripts/loop/fundir_por_plan.py --plan docs/loop/PLAN_V69_OPU02_LOTE_E.json --ejecutar`
([`SALIDA_V69_FUSION_LOTE_E.txt`](SALIDA_V69_FUSION_LOTE_E.txt)), **precedida de la simulacion sobre
copia en memoria** ([`SALIDA_V69_FUSION_SIMULADA.txt`](SALIDA_V69_FUSION_SIMULADA.txt)).

| | acto 18 | acto 25 | acto 26 | acto 29 | acto 30 | **el lote** |
|---|---:|---:|---:|---:|---:|---:|
| absorbidos | 3 | 3 | 3 | 2 | 2 | **13** |
| pasos del superviviente | 4 a **7** | 4 a **6** | 6 a **9** | 4 a **6** | 8 a **8** | |
| condiciones | 2 a **4** | 2 a 2 | 2 a **3** | 2 a 2 | 1 a **2** | |
| piezas repartidas | 18 | 17 | 21 | 10 | 12 | **78** |
| de ellas `APPEND` / `CUBIERTO` / `INCISO` | 5 / 12 / **1** | 2 / 15 / 0 | 4 / 16 / **1** | 2 / 8 / 0 | 1 / 7 / **4** | **14 / 58 / 6** |
| perdidas selladas en campo propio | 7 | 3 | 8 | 1 | 2 | **21** |

**TOTAL: 13 nodos mueren (3.237 vivos a 3.224). Ficheros tocados: 49. Redirecciones sobre nodos
vivos: 38.**

**LAS GUARDAS DE CADA FUSION, LAS CUATRO Y TODAS VERDES EN LAS CINCO:** guarda 1 (miembros vivos y
nomina completa), guarda **1B** (ningun **absorbido** es semilla ni extremo de puente), guarda 2
(cobertura exacta de indices, cero olvidos) y guarda 3 (cero repetidos literales).

**LOS SEIS `INCISO` SE EXTRAJERON DEL NODO Y SE COMPROBARON VERBATIM**, y sus pasos resultantes estan
impresos por el generador:

- **acto 18, al paso 1:** *Identificar desafíos de sostenibilidad compartidos con competidores o
  empresas de la industria**, evaluando antes si la empresa tiene suficiente poder de mercado para
  exigir cambios individualmente***
- **acto 26, al paso 2:** *Observar directamente a los usuarios utilizando o mal utilizando el
  producto durante un período extendido**, involucrando a líderes o clientes (deputizar) en la
  observación de campo para generar empatía directa***
- **acto 30, al paso 1:** *Analizar los síntomas del problema (evidencia observable)**, con un
  análisis de Pareto para descartar variables no relevantes (ej. turno de trabajo)***
- **acto 30, al paso 2:** *Formular teorías sobre las posibles causas**, usando brainstorming y
  diagramas causa-efecto***
- **acto 30, al paso 3:** *Probar las teorías más plausibles con datos**, con un mecanismo de
  recolección que permita correlacionar cada teoría con el defecto observado***
- **acto 30, al paso 4:** *Establecer la(s) causa(s) raíz confirmada(s)**, validando estadísticamente
  cuál teoría explica la mayoría de los casos***

**CERO `INCISO` EN LOS ACTOS 25 Y 29, Y ES POR LA PUNTUACION** (carril del `D5` del acta 66): **los
cuatro pasos de sus supervivientes terminan en punto**, y un `INCISO` con nexo de coma detras de un
punto cae en la guarda de la **JUNTURA ROTA**. **No se forzo ninguno.**

**`P.16`, QUIEN FABRICA LIMPIA, EN EL MISMO COMMIT:** la fusion fabrico **5** duplicadas y **las
limpio en la misma corrida**; **1 auto-arista** retirada; **guarda A** (cero auto-aristas nuevas)
**OK**, **guarda B** (cero duplicadas nuevas tras resolver) **OK**, **guarda C** (los campos que esta
operacion no redacta, intactos: **25 de 25**) y **guarda D** (los 13 absorbidos conservan su texto
**INTACTO**) **OK**. El pasivo del censo propio de la guarda **baja 1** (890 a 889).

**`reanclar_por_resolutor.py` corrido ENTRE la fusion y `run_phase1`**
([`SALIDA_V69_REANCLAJE.txt`](SALIDA_V69_REANCLAJE.txt)): **NADA QUE RE-ANCLAR**, y **se dice por que
en vez de dejarlo como un cero mudo**: el propio fundidor ya habia redirigido **las 38 referencias
vivas** a los absorbidos, asi que cuando el reanclador llego no quedaba ninguna. **Se corrio igual,
que es lo que la guarda pide.**

### 3.4 **EL DIFF DE DUPLICADAS, POR INSTRUMENTO Y CON LA APERTURA SACADA DE `git`**

`python scripts/loop/diff_duplicadas_por_resolutor.py --antes <git show 764523c0:...> --despues
docs/plan/ARISTAS_DUPLICADAS.jsonl`
([`SALIDA_V69_DIFF_DUPLICADAS.txt`](SALIDA_V69_DIFF_DUPLICADAS.txt)).

> **GRUPOS FABRICADOS DE VERDAD: `0`.** **RENOMBRADOS: `0`.** Hay **1 que DESAPARECE**
> (`investigacion_etnografica_ideacion` en `nodos_previos` hacia `seleccion_arenas_estrategicas`), y
> **esta explicado**: era el grupo del absorbido `etnografia_investigacion_usuario` que la fusion
> deduplico al unir los `nodos_previos`. **913 grupos a 912.**

**EL CORTE DE *ANTES* SALE DE `git show` SOBRE EL COMMIT DE LA TAREA 1** (`764523c0`), **anterior a la
fusion**, y el de *despues* es el fichero **tras recompilar el grafo con `run_phase1`**, que es la
leccion de la averia 7.5 de la vuelta 68: **contar duplicadas antes de recompilar lee el grafo viejo
con etiqueta de nuevo.** **Esta vuelta se conto despues del Gate 0 y no antes.**

### 3.5 **EL CENSO DE COLISIONES: LAS ESPERADAS MEDIDAS ANTES DE FUNDIR SOBRE LA BASE `4`, Y CALZA. PERO ESTA VUELTA FABRICA DOS**

`python scripts/loop/vuelta65_colisiones_esperadas.py --plan docs/loop/PLAN_V69_OPU02_LOTE_E.json
--base 4` ([`SALIDA_V69_COLISIONES_ESPERADAS.txt`](SALIDA_V69_COLISIONES_ESPERADAS.txt)), **corrido
sobre el arbol de antes y simulando en memoria, sin tocar un nodo**.

| | |
|---|---:|
| linea base declarada **y MEDIDA sobre el arbol de antes** | **4** |
| **colisiones NUEVAS que la fusion fabricaria** | **2** |
| colisiones que desaparecerian | 0 |
| **ESPERADAS TRAS FUNDIR** | **6** |
| **MEDIDAS al cierre por el censo** | **6** |
| **`CALZA`** | **`SI`** |
| auto-pares, predichos y medidos | **5** nuevos predichos (263 a 268) y **268** medidos al cierre |

**LAS DOS NUEVAS SALEN LAS DOS DE LA FUSION DEL `ACTO 25`, y van nombradas con sus puestos:**

| colision nueva | clases | de donde sale |
|---|---|---|
| `cuatro_etapas_llamada_de_ventas` contra `enfoque_etapa_investigacion` | **`B`** contra **`D`** | el **775** dice `B` contra el superviviente; el **202** y el **1364** dicen `D` contra dos absorbidos |
| `enfoque_etapa_investigacion` contra `modelo_spin_preguntas` | **`B`** contra **`D`** | el **648** y el **769** dicen `B`; el **1422** dice `D` contra un absorbido |

> **LAS DOS SON LA MISMA ESPECIE, y decirlo explica el choque: el MARCO ENTERO contra UNA DE SUS
> ETAPAS.** Contra el superviviente la lectura dijo `B` (dos caras del mismo asunto); contra los
> absorbidos dijo `D` (el todo no repite la parte). **La fusion junta las tres lecturas en un solo par
> y el choque se vuelve visible.** **No es una lectura nueva ni una lectura movida: es una lectura
> vieja que cambia de vecino.**
>
> **EL CARRIL ESTA ESCRITO Y SE APLICA A LA LETRA:** *la duena de una colision que fabrica una fusion
> es quien la fabrica*. **Duena: `OP-U-02`.** Predichas **antes de tocar un nodo**, **selladas en el
> plan**, **publicadas en rojo** y **registradas en `03_FUSIONES.md`** con sus puestos.
>
> **LO QUE NO SE ADJUDICA AQUI: LA LINEA BASE.** Medida al cierre, la base operativa pasaria de **4**
> a **6**. **La base vigente se movio de 2 a 4 por adjudicacion del auditor** (acta 66, pregunta 2), y
> **por eso esta NO la mueve el ejecutor**: va como **pregunta 5** de la seccion 8. **El instrumento
> conserva su defecto en `4` y no se toca.** **VA MARCADO DISCUTIBLE (`D1`).**

**Las dos de la mesa `OP-M-03` no se tocan y las dos viejas de `OP-U-02` siguen vigentes con su
duena.**

### 3.6 **GATE 0 CON SU CICLO DE TRES, Y NO DE CUATRO**

| paso | resultado |
|---|---|
| `python scripts/run_phase1.py --reaplico-curaduria` | **`GATE 0: OK`**, todos los chequeos en `[OK]`; universo **3.224 activos / 629 deprecados**; alcanzabilidad **100,0 por ciento** |
| `python scripts/etiquetas_de_cara.py --aplicar` | **71 etiquetas** re-aplicadas |
| `python scripts/sync_assets_web.py` | **6 assets** mas `manifest.json` |
| **una cuarta corrida** | **NO SE HIZO** |

**LAS TRES SUITES, CORRIDAS POR MI CON EL COMANDO BUENO** (la leccion de la averia 7.1 de la vuelta
68: `--reporter=basic` no existe en `vitest` 4): motor **25/25**
([`SALIDA_V69_SUITE_MOTOR.txt`](SALIDA_V69_SUITE_MOTOR.txt)); web **80 ficheros, 1.030 pasadas, 3
saltadas** ([`SALIDA_V69_SUITE_WEB.txt`](SALIDA_V69_SUITE_WEB.txt)); `tsc --noEmit` **CERO lineas**
([`SALIDA_V69_TSC.txt`](SALIDA_V69_TSC.txt)). **Y el guardian de commit las volvio a correr en verde
en los tres commits de trabajo de esta vuelta.**

### 3.7 **EL REGISTRO EN `03_FUSIONES.md`** (`+440` lineas, `0` borradas)

`python scripts/loop/vuelta69_registro_lote_e.py`
([`SALIDA_V69_REGISTRO_LOTE_E.txt`](SALIDA_V69_REGISTRO_LOTE_E.txt)), **bajo la cabecera de tramo que
la vuelta 65 adoso** (derivada hoy por aguja) y **sin reescribir ni una linea de arriba**
(`git diff --numstat`: **`440 0`**).

**NINGUNA TABLA TECLEADA Y NINGUNA CITA TECLEADA:** el reparto pieza a pieza y las piezas por
absorbido de los **cinco** actos fundidos **se generan del plan sellado**; la ficha del `acto 27`
tambien; las de perdidas **se recortan de la salida del tallador leyendo la columna `acto` por su
sitio**; y **las 42 celdas** de guardas, colisiones, censos y cuentas **se extraen por aguja**.
**Idempotencia MUERDE.**

**EL UNICO CAMBIO SOBRE LA MAQUINA COPIADA DEL REGISTRADOR DE LA VUELTA 68, Y VA DICHO EN SU
DOCSTRING:** `tabla_declarado` **imprime ademas LA FIGURA DEL INVENTARIO** de la que el acto es
ejemplar. El `acto 27` es el **ejemplar 4 de la figura `ESTRELLA (9.23)`** y **su centro es el mismo
nodo puente que `P.10` detecto**: es una razon de cierre **independiente** que la prosa no deberia ser
la unica en decir. **Es exactamente la razon con la que la vuelta 68 anadio la fila de duenos.** **VA
MARCADO DISCUTIBLE (`D8`).**

### 3.8 **LOS DOS RACIMOS CENSADOS QUE ESTE LOTE TOCA, MEDIDOS Y DECLARADOS**

**Es la pieza mas delicada despues de las colisiones, y por eso va en su propio apartado.** **Tres de
los cinco actos fundidos tienen miembros censados en un racimo de
[`../RACIMOS_MIEMBROS.jsonl`](../RACIMOS_MIEMBROS.jsonl)**, y **no todos se comportan igual**.

| racimo censado | nomina | **cuantos de esos entran al acto** | **veredicto medido** |
|---|---:|---|---|
| *La etapa de investigacion en la venta* (`acto 25`) | **3** | **los TRES** | **NO SE PARTE**: el racimo cabe entero dentro del acto |
| *El avance y el compromiso en la venta* (`acto 29`) | **5** | **DOS** | **SE TOCA A MEDIAS, y se declara**: los otros TRES **tienen casa propia medida** |
| *Analisis de causa raiz* (`acto 30`) | **4** | **DOS** | **SE TOCA A MEDIAS, y se declara**: los otros dos (`analisis_causa_raiz_defectos` y `juran_rcca_metodo`) **no entran al acto y ninguno queda deprecado** |

> **EL CASO DEL `ACTO 29` ES EL QUE MAS SE PODIA CONFUNDIR Y POR ESO VA MEDIDO ENTERO:** el censo del
> cribado dice CINCO, pero **`INVENTARIO.jsonl` ya trae la entrada racimo *el compromiso contado tres
> veces*, forma `PURO`, estado sano y forma cerrada, con nomina de exactamente los OTROS TRES**
> (`obtencion_compromiso`, `obtencion_de_compromiso`, `obtencion_compromiso_venta`). **El censo de
> cinco ya estaba PARTIDO en el inventario en un `PURO` de tres mas dos sueltos, y esta fusion opera
> sobre los DOS SUELTOS sin tocar el `PURO` ni una vez.**
>
> **NINGUNO DE LOS TRES RACIMOS TIENE DUENO MEDIDO**, y esto se comprobo **por las tres vias que el
> acta 68 fijo en su seccion 5.2**: los dos campos `duenos_*` del fichero fijado del tramo (vacios en
> los seis actos), el campo `operaciones` de la entrada de inventario (vacio), y **ademas** un barrido
> de `OPERACIONES.jsonl` sobre los 18 miembros del lote. **Ese barrido devolvio UNA sola mencion y se
> declara en vez de callarse**: `analisis_diagnostico_causa` aparece en el **campo `evidencia`** de
> `OP-D-09`, hablando de una arista. **El campo `nodos` de `OP-D-09` es `planificacion_recoleccion_datos`
> y nada mas**, medido hoy: **una mencion en la evidencia de una ficha NO es dueno** por el criterio
> adjudicado.

### 3.9 **LAS PERDIDAS DEL LOTE, CONTADAS POR MAQUINA Y NO DE MEMORIA**

**Es la regla que sale de la caida del `D9` de la vuelta 68, y esta vuelta la estrena sobre si
misma:** la cuenta se deriva **contando por maquina sobre el plan sellado**
([`SALIDA_V69_CUENTA_ATENUANTES.txt`](SALIDA_V69_CUENTA_ATENUANTES.txt)), **con la frase entera y no
con una aguja floja**.

| | contado sobre el plan sellado |
|---|---:|
| **perdidas selladas en campo propio** | **21** |
| de ellas `DE PARAMETRO DE PASO` | **16** |
| de ellas `DE CONDICIONES` | **5** |
| **filas con `ATENUANTE DECLARADO`** | **14** |
| de ellas, de la **especie del pendiente 4** | **6** |
| de ellas, con **`ATENUANTE DECLARADO Y MEDIDO`** | **4** |
| **filas con DOS SEDES en el campo `donde`** | **1** |
| la aritmetica de **la lectura contraria** (una fila por SITIO, no por PIEZA) | **22** y no **21** |

> **Y AQUI VA LA MITAD DE LA REGLA QUE OBLIGA A DECIR LO QUE SE EXCLUYE, porque esta vuelta tiene un
> caso:** **la fila 5** (la crisis REGULATORIA del `acto 18`) **describe en su prosa exactamente el
> mecanismo del pendiente 4** (*la mitad reputacional llega entera por el `APPEND` de la condicion 1
> del hermano*) **pero NO lleva la frase sellada `ATENUANTE DECLARADO`**. **La cuenta por maquina da
> 14 y no 15, y la frase lo dice.** **El plan NO se re-sella para arreglarlo**, porque **un plan
> EJECUTADO no se re-sella** (acta 68, `D15`). **VA MARCADO DISCUTIBLE (`D10`).**

---

## 4. EL `ACTO 18`, LA FUSION QUE EL EJECUTOR NO ELIGIO: LAS CINCO PIEZAS, UNA A UNA

**El acta 68 adjudico el superviviente y nombro CINCO piezas que el plan tenia que CONSERVAR O
SELLAR.** **Las CINCO quedaron CONSERVADAS y NINGUNA sellada como perdida**, y va pieza por pieza
porque ese era el encargo:

| pieza nombrada por el acta 68 | de donde sale | **destino medido** |
|---|---|---|
| publicar y monitorear el cumplimiento colectivo | `co_opetition_industria`, paso 4 | **`APPEND`**, paso 5 del superviviente |
| aplicar el estandar conjunto a los proveedores compartidos | `trabajo_colectivo_estandares_industria`, paso 4 | **`APPEND`**, paso 7 |
| el marco nombrado *Responsible Care* | `trabajo_colectivo_estandares_industria`, paso 3 | **`APPEND`**, paso 6 |
| el encuadre por riesgo reputacional compartido | `trabajo_colectivo_estandares_industria`, condicion 1 | **`APPEND`**, condicion 3 |
| el test del poder de mercado **como arranque explicito** | `colaboracion_sectorial`, paso 1 | **`INCISO` ADOSADO AL PASO 1** |

> **LA QUINTA ES LA QUE OBLIGO A ELEGIR, y por eso se explica:** el acta no pidio *conservar el test*,
> pidio conservarlo **COMO ARRANQUE EXPLICITO**. **Un `APPEND` lo habria puesto de paso 8**, o sea al
> final, que es lo contrario de un arranque; **un `CUBIERTO` lo habria dejado como condicion**, que es
> donde ya estaba y lo que el acta llama insuficiente. **El `INCISO` al paso 1 es la unica de las tres
> marcas que lo deja donde el acta lo quiere.** El paso resultante esta impreso en la seccion 3.3.

**Y LO QUE EL EJECUTOR NO HIZO, dicho para que nadie se lo atribuya: NO re-decidio el superviviente.**
La forma medida sigue siendo `EMPATE SIN VARA` y ninguna vara apunta; **la eleccion es del auditor y
este plan la ejecuta**. **El ejecutor reparte, y el reparto es lo unico que se le puede discutir.**

---

## 5. EL `ACTO 27`, `DECLARADO Y NO FUNDIDO`, EN UNA LINEA

**Cierra por `P.10` con su triangulo MEDIDO y queda vivo y entero.** El nodo puente es
`fase_diseno_prototipado_modelos` y el `D` interno es el puesto **572**, *EL HIJO CON CASA PROPIA*,
que dice que `prototipado_modelos_negocio` **desarrolla el paso 5** de la madre y le anade lo suyo
entero, mientras **la madre se queda con lo suyo**. **Fundir los cuatro deprecaria los dos extremos de
ese `D` contra el mismo superviviente y sellaria que repiten entre si**, que es lo que esa lectura
niega, y ademas es **una cadena de TRES PISOS** que el propio **572** cuenta al cerrar.

> **Y HAY UNA SEGUNDA RAZON INDEPENDIENTE, MEDIDA:** **este acto es el ejemplar numero CUATRO de la
> figura `ESTRELLA (9.23)` de `INVENTARIO.jsonl`**, *la fase de diseno*, con **el centro
> `fase_diseno_prototipado_modelos`, los radios 507 y 641 y el periferico 572 en `D`**. **El centro de
> esa estrella es EXACTAMENTE el nodo puente que `P.10` detecto, y el periferico es EXACTAMENTE el par
> `D`.** **Es la misma forma del `acto 24` de la vuelta 68**, con la estrella de pass/fail. **Una
> fusion entera borraria un ejemplar de una figura del inventario.**

**Su destino comparte carril con el pendiente heredado del subconjunto cerrado: el cierre de la fase
03**, donde ya son **14** los declarados que esperan.

---

## 6. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

**`D1`. ESTA VUELTA FABRICA DOS COLISIONES DE CLASE Y LA BASE OPERATIVA PASARIA DE 4 A 6. ES EL MAS
FUERTE DEL DIA Y LO SE.** El carril esta escrito (*la duena es quien la fabrica*), las dos estaban
**predichas antes de tocar un nodo**, la cuenta **calza al digito** y estan **publicadas en rojo con
su duena**. **Leido al reves**, una fusion que fabrica dos colisiones nuevas es una fusion que habria
que no hacer, y el `acto 25` se podria haber dejado para el cierre de la fase 03 junto con los
declarados. **No pare porque ninguna letra manda parar por una colision predicha** (el precedente del
`acto 8` de la vuelta 66 fabrico dos y no paro), **pero si el auditor lo lee al reves, esta fusion
habria que deshacerla.**

**`D2`. EL NODO DEL `ACTO 26` PASA DE 6 PASOS A 9, QUE IGUALA AL NODO MAS GRANDE DEL TRAMO.** Tres
`APPEND` de paso. Elegi **catalogo mas rico con solapes declarados** sobre `CUBIERTO` que calla texto
vivo, que es el carril del `D8` del acta 67 y del `D4` del acta 68, **y los tres `APPEND` son los que
las razones nombran como propios**. **Pero un nodo de nueve pasos es un nodo de nueve pasos**, y esta
vez el que llega a nueve **es ademas una PUERTA**, o sea un nodo que la gente ve al entrar.

**`D3`. CUATRO `INCISO` EN EL `ACTO 30`, QUE ES LA CIFRA MAS ALTA DE LA CAMPANA.** Ninguno apilado
sobre el mismo paso (la regla del acta 64), los cuatro pasos receptores **no terminan en punto** y los
cuatro resultantes estan impresos arriba. **Mi razon:** el superviviente ya trae ocho pasos y las
cuatro piezas son **parametros de rigor** de gestos que ya tiene, no gestos nuevos; con `APPEND` el
nodo habria llegado a **doce**. **Se puede sostener que cuatro oraciones cosidas con coma en un solo
nodo es una decision de redaccion que la fase 04 puede querer al reves.**

**`D4`. EL `ACTO 29` FUNDE DOS DE LOS CINCO MIEMBROS DE UN RACIMO CENSADO.** Mi lectura es que **el
censo de cinco ya estaba partido en el inventario** en un `PURO` de tres mas dos sueltos, y que la
fusion opera **sobre los dos sueltos**. **Leido al reves**, un racimo censado de cinco es una unidad y
tocar dos de sus miembros lo parte. **El `PURO` de tres no se toca ni una vez, y eso esta medido.**

**`D5`. EL SUPERVIVIENTE DEL `ACTO 30` SALE DE UNA RAZON QUE SU PROPIO AUTOR MARCO DISCUTIBLE
FUERTE.** El **2838** dice `A` **POR CONTENCION** y nombra superviviente, **y en la misma razon avisa
de que quien lea el viaje diagnostico como una PARTE, o como cara distinta por su Pareto y su
validacion estadistica, dira `D`**. **Funde igual, y por eso el reparto mete esas tres piezas de rigor
por `INCISO` en vez de callarlas con `CUBIERTO`**: si la lectura contraria tiene razon, **lo que la
haria valer sigue vivo dentro del superviviente**. **Se puede sostener que un `A` con discutible
fuerte de su autor no deberia fundir sin una segunda lectura.**

**`D6`. UNA SOLA VARA, LA DE CONDICIONES, DECIDE EL `ACTO 29` CON PASOS Y CABLEADO EMPATADOS.** El
margen es **2 contra 1**, que es el margen mas pequeno con el que este tramo ha elegido superviviente.
**La letra dice que una sola vara basta y que donde el contenido dice algo el contenido manda**, y la
vara de condiciones es contenido. **Se puede sostener que una diferencia de UNA condicion es ruido y
que el acto era un `EMPATE SIN VARA` de facto.**

**`D7`. EL TOPE DEL LOTE LO ELIGIO UN ACTO CON DUENO Y NO UN NUMERO.** Declare **seis** porque el
`acto 31` no podia cerrar ENTERO. **Se puede sostener que eso es elegir el tope por conveniencia** (el
lote sale mas corto justo antes de un acto incomodo). **Mi razon:** el contrato es *entregar lo
declarado*, y declarar un acto que **no puede cerrar** es declarar lo que no se va a entregar. **La
alternativa honesta seria declarar mas y saltarse el 31**, y eso rompe el *prefijo SIN SALTOS*.

**`D8`. `tabla_declarado` CRECE CON UNA FILA DE FIGURA DEL INVENTARIO, SIN ENCARGO.** Nadie me pidio
tocar la tabla. **Lo hice porque el `acto 27` es ejemplar de una figura declarada y esa razon de
cierre solo vivia en la prosa.** **Va enumerada en el docstring** y marcada aqui, que son las dos
condiciones del acta 61. **Se puede sostener que es alcance, y que la vuelta 68 ya hizo lo mismo con
los duenos: dos vueltas seguidas anadiendo una fila es una tabla que crece sola.**

**`D9`. CUATRO PERDIDAS LLEVAN `ATENUANTE DECLARADO Y MEDIDO`, o sea que las sello sabiendo que un
`INCISO` o un paso del propio superviviente las repara.** Es el carril del `D10` del acta 68 (*el
sello es del reparto y no del resultado*), **pero cuatro en un lote es el doble que la vuelta pasada**
y **infla la cuenta de 21 con filas que no se pierden de hecho**. **Queda publicado con la cuenta por
maquina al lado para que quien lea pueda restarlas.**

**`D10`. LA FILA 5 DEL PLAN DESCRIBE EL MECANISMO DEL PENDIENTE 4 EN SU PROSA PERO NO LLEVA LA FRASE
SELLADA, Y LA CUENTA POR MAQUINA DA 14 Y NO 15.** Lo vi **al correr la cuenta**, no al escribirla, que
es justo lo que la regla nueva persigue. **No re-selle el plan** porque **un plan ejecutado no se
re-sella** (acta 68, `D15`). **Se puede sostener que la cuenta buena es 15 y que la maquina esta
midiendo una frase y no un hecho.**

**`D11`. EL PLAN SE SELLO DOS VECES.** El primer sello no podia citar el fichero de colisiones
esperadas **porque ese fichero se genera A PARTIR del plan**; medidas las colisiones, **volvi a
sellar** para que la cabecera lo citara. **Los dos sellos estan comparados por maquina y difieren en
UNA sola linea, la del campo `colisiones_esperadas`**
([`SALIDA_V69_DIFF_SELLOS.txt`](SALIDA_V69_DIFF_SELLOS.txt)). **Es exactamente el `D15` de la vuelta
68, que el acta adjudico `A FAVOR`**, y lo marco igual **porque un carril adjudicado una vez no me
autoriza a dejar de marcarlo**.

**`D12`. LOS NEXOS DE LOS `INCISO` SON COSECHA PROPIA MAS LARGA QUE UNA COMA.** Cuatro de los seis
llevan nexos como *, evaluando antes*, *, involucrando*, *, con un* y *, validando*. **El instrumento
solo exige que el TROZO sea verbatim; el nexo es mio.** **Se puede sostener que un nexo de tres
palabras ya es redaccion y no costura**, y que la fase 04 lo va a reescribir. **Mi razon:** un nexo de
coma seca habria dejado pasos ilegibles, y los seis resultantes estan impresos arriba para que se
juzguen leyendolos.

**`D13`. EL `ACTO 26` SELLA OCHO PERDIDAS, LA CIFRA MAS ALTA DE UN ACTO EN TODO EL TRAMO.** Es el
precio de fundir cuatro nodos de **dos libros distintos** con catalogos que se solapan a medias.
**Se puede sostener que un acto que pierde ocho piezas no deberia fundirse**, y que el `839` (el par
que cruza los dos libros) era la unica lectura que lo sostenia.

**`D14`. FUNDIR DOS ACTOS CUYO SUPERVIVIENTE ES UNA PUERTA, EL MISMO DIA.** La letra lo permite con
todas sus letras (una puerta sola sobrevive), **pero es la primera vez del tramo que se usa dos veces
en una vuelta**, y las dos puertas **crecen** (una a 6 pasos y otra a 9). **Una puerta es lo que la
gente ve al entrar**, y esta vuelta engorda dos.

---

## 7. LAS AVERIAS PROPIAS, CAZADAS ANTES DE UNA CIFRA PUBLICADA

**CERO de ellas llego a una cifra publicada ni a un dato movido.**

### 7.1 **ESCRIBI UN NEXO DE `INCISO` SIN SU ACENTO Y HABRIA ENTRADO A UN NODO VIVO**

El nexo del `INCISO` al paso 3 del `acto 30` decia *, con un mecanismo de recoleccion* **sin la tilde
de *recolección***. **El trozo se extrae del nodo y se comprueba verbatim, pero el NEXO es cosecha
propia y nadie lo coteja.** Lo vi **leyendo el paso resultante que el generador imprime en la
simulacion**, antes de sellar el plan. Corregido a *recolección*. **Sin esa lectura, una palabra mal
escrita habria quedado dentro de un nodo del catalogo.**

### 7.2 **ESCRIBI UN FICHERO CON UN HEREDOC Y EL FICHERO NO SE ESCRIBIO**

Mi primer intento de crear el texto del registro del acta 68 murio en el interprete de la orden y
**no escribio nada**. **Lo vi porque comprobe que el fichero existiera en vez de dar por hecho que
existia.** Re-escrito por otra via. **Es la misma especie que las averias 7.1 y 7.4 de la vuelta 68:
una llamada que falla y un resultado que nadie mira.**

### 7.3 **COPIE UN FICHERO A UNA RUTA QUE MI PROPIO INTERPRETE NO VEIA**

Guarde el primer sello del plan en una ruta temporal del interprete de ordenes; el interprete de
Python **no la veia** y el diff de sellos murio con `FileNotFoundError`. **Cero salida util, cero
cifra publicada.** Corregido guardando el primer sello **dentro del repo**
([`_v69_plan_sello1.json`](_v69_plan_sello1.json)), **que ademas lo deja auditable**: el diff de una
sola linea se puede volver a correr.

### 7.4 **ESCRIBI LOS DISCUTIBLES EN LA SECCION 4 Y LA GUARDA DE PROMESAS CAYO EN `ROJO`**

**La guarda mide contra LA SECCION 6 del reporte**, que es donde la casa pone los discutibles desde
la vuelta 61. Yo los abri en la **seccion 4** al reordenar el reporte, y la guarda dio **2 promesas
medidas, 0 CUMPLIDAS, 2 INCUMPLIDAS** (las de los actos 26 y 30). **La cace corriendo la guarda, no
leyendo el `exit`.** **Corregido moviendo el texto, no la guarda**: los discutibles vuelven a la
**seccion 6** y las demas secciones se renumeran detras. **ES LA MISMA AVERIA QUE LA 7.7 DE LA VUELTA
68, repetida por la misma causa** (reordenar el reporte sin mirar donde mide la guarda), **y por eso
va dicha con esa palabra: REPETIDA**. Re-corrida: **2 de 2 CUMPLIDAS**.

---

## 8. PENDIENTES DE DOCTRINA Y PREGUNTAS

1. **EL SUBCONJUNTO CERRADO DE UN ACTO CON PUENTE** (heredado, acta 68 pendiente 4): **ahora son
   CATORCE** los actos declarados que esperan el cierre de la fase 03 (los 13 anteriores mas el
   `acto 27`). Sigue enrutado al **cierre de la fase 03**, donde **la parada de `AUDITOR.md` espera al
   fundador**. **Y con la medicion de la seccion 10 se puede decir algo nuevo: esa lista ya no va a
   crecer por `P.10` en este tramo, porque no quedan actos con puente.**
2. **LA MARCA PARA *YA LO DICE EL `APPEND` DE UN HERMANO*** (heredado, acta 68 pendiente 5): **esta
   vuelta lo paga SEIS veces**, contadas por maquina, que es el triple que la vuelta 68. **El carril
   vigente alcanza, pero la cuenta ya no es anecdotica** (ver `D9` y `D10`).
3. **EL `INCISO` DE CONDICIONES SIGUE SIN EXISTIR** (heredado): **cinco perdidas `DE CONDICIONES`** en
   esta vuelta, enrutadas a la fase 04 por el carril del acta 55, pregunta 5.
4. **EL ESQUEMA DE `OPERACIONES.jsonl`** (heredado): sigue pendiente y **esta vuelta no toco ninguna
   ficha**, asi que no estreno ninguna clave.
5. **NUEVO, Y ES LA PREGUNTA DE MAS PESO DEL DIA: LA LINEA BASE OPERATIVA DEL CENSO DE COLISIONES,
   PASA DE `4` A `6`?** Esta vuelta fabrico **dos** colisiones, predichas y publicadas con su duena
   `OP-U-02`, y el censo al cierre mide **6**. **La base vigente se movio de 2 a 4 por adjudicacion
   del auditor** (acta 66, pregunta 2), **asi que no la muevo yo**: el defecto del instrumento sigue
   en `4` y la proxima corrida caeria en `ROJO` si nadie lo adjudica. **La pregunta concreta: la base
   pasa a 6 por el mismo carril, o el auditor quiere que el ejecutor pase `--base 6` a mano hasta que
   la adjudicacion se escriba?**
6. **NUEVO, Y LO TRAIGO ANTICIPADO: QUE PASA CON UN TRAMO EN EL QUE YA NO QUEDA NINGUN ACTO CON
   PUENTE NI CON `D` INTERNO?** Medido en la seccion 10. **Los motivos sellados 1 y 4 se quedan sin
   sujeto** y los que quedan son la guarda `1B` y la respuesta *DOS FAMILIAS* de `P.5`. **No es una
   parada ni pide doctrina**, pero **cambia lo que el lote siguiente puede esperar** y por eso va
   escrito.

---

## 9. RUTAS TOCADAS Y CENSOS AL CIERRE

**Del grafo (49 ficheros):** los **cinco supervivientes** (`alianzas_cross_industry`,
`enfoque_etapa_investigacion`, `investigacion_etnografica_ideacion`, `marco_avances_continuaciones`,
`viaje_diagnostico_remedial`), sus **trece absorbidos** (`co_opetition_industria`,
`colaboracion_sectorial`, `trabajo_colectivo_estandares_industria`, `etapa_de_investigacion`,
`etapa_investigacion_ventas`, `investigacion_como_habilidad_clave`,
`etnografia_aplicada_en_equipos_multidisciplinarios`, `etnografia_de_proyecto`,
`etnografia_investigacion_usuario`, `advances_vs_continuations`,
`objetivos_de_llamada_orientados_a_avance`, `analisis_causa_raiz_diagnostico`,
`analisis_diagnostico_causa`), los **redirigidos** (38 referencias sobre nodos vivos), mas
`dataset/metadata/master_graph.json` y `dataset/metadata/phase1_run_log.json`.

**Del registro:** `docs/plan/03_FUSIONES.md` (**`+170`** del acta 68 y **`+440`** del lote E, **cero
borradas en los dos**), `docs/plan/ARISTAS_DUPLICADAS.jsonl`, `docs/COSTURAS_INTERNAS.jsonl` y su
resumen, y `web/lib/assets/` por el `sync`. **`docs/plan/OPERACIONES.jsonl` NO se toco**, y
**`scripts/rumbos/banco_rumbos.json` tampoco**, porque el reanclaje no tuvo nada que hacer.

**Instrumentos nuevos (cinco):** `scripts/loop/vuelta69_registrar_acta68.py`,
`scripts/loop/_v69_texto_acta68.py`, `scripts/loop/_v69_lote_e.py`,
`scripts/loop/vuelta69_registro_lote_e.py` y `scripts/loop/_v69_texto_lote_e.py`. **Ningun instrumento
de nombre estable se toco en esta vuelta.**

| censo al cierre | valor |
|---|---|
| **barrido de titulos** ([`SALIDA_V69_BARRIDO.txt`](SALIDA_V69_BARRIDO.txt)), **re-corrido AL CIERRE** | **453 ficheros**, `ROJO` **32** (linea base heredada, **sin mover**), **`AMBAR` 0**, `ROTULADO` **47**, `CENSO` **224**, `ILEGIBLE` **1**. **Los 453 son los 448 del acta 68 mas los CINCO instrumentos nuevos**, contados uno a uno |
| **censo de plantillas talladas** ([`SALIDA_V69_CENSO_PLANTILLAS.txt`](SALIDA_V69_CENSO_PLANTILLAS.txt)) | **CERO TALLADOS** sobre **23** instrumentos de nombre estable |
| **estado de las operaciones** ([`SALIDA_V69_CIERRE.txt`](SALIDA_V69_CIERRE.txt)) | **71**, todas `LISTA`, **0** dependencias rotas, **672** entradas, enlaces **17.588** |
| **casos positivos sobre sujetos que esta vuelta NO toca** ([`SALIDA_V69_CASOS_POSITIVOS.txt`](SALIDA_V69_CASOS_POSITIVOS.txt)) | mesa: **LAS NUEVE MUERDEN** sobre `OP-M-02-ACCLIMATE`; contrato de perdidas: **LAS CUATRO**; varas: **LAS TRES mitades**; promesas: **LAS DOS mitades** |

### 9.1 **LA TASA POR DOMINIO AL CIERRE, IDENTICA A LA DE APERTURA**

**Fundir no volteo ni un veredicto**, y por eso el marcador de cierre sale **identico linea a linea**
al de apertura (comparado por maquina sobre las 21 lineas del fichero: **cero diferencias**).

| dominio | pares | `A` | tasa |
|---|---:|---:|---:|
| compras | 155 | 1 | 0,6 |
| core | 1.445 | 325 | 22,5 |
| entrega | 171 | 2 | 1,2 |
| environmental | 170 | 28 | 16,5 |
| exportacion | 130 | 15 | 11,5 |
| franquicias | 148 | 15 | 10,1 |
| health_safety | 192 | 43 | 22,4 |
| quality | 844 | 119 | 14,1 |
| risk_management | 106 | 0 | 0,0 |
| seguridad_digital | 27 | 3 | 11,1 |

**Corte de todas estas cifras: 26 ago 2026, puesto 3.388.**

---

## 10. LO QUE QUEDA DEL TRAMO, MEDIDO AL CIERRE

([`SALIDA_V69_TRAMO_CIERRE.txt`](SALIDA_V69_TRAMO_CIERRE.txt) y
[`SALIDA_V69_PUENTES_DE_LOS_QUE_QUEDAN.txt`](SALIDA_V69_PUENTES_DE_LOS_QUE_QUEDAN.txt))

| | |
|---|---:|
| actos del tramo unico | **47** |
| cerrados por los lotes A, B, C y D | **20** |
| **cerrados por el lote E (esta vuelta)** | **6** (5 fundidos, 1 declarado) |
| **quedan** | **21 actos** |
| **nodos que quedan** | **63** |
| **el siguiente del prefijo** | el acto **31**, **con dueno** (`OP-F-04-WEI`, `OP-S-04`) |
| de los que quedan, **con nodo puente** | **0** |
| de los que quedan, **con par `D` interno** | **0** |
| de los que quedan, **con dueno medido** | **2** (los actos **31** y **37**) |
| **actos declarados que esperan el cierre de la fase 03** | **14** |

> **UN HECHO MEDIDO QUE CAMBIA LO QUE VIENE, Y LO TRAIGO ANTICIPADO:** **de los 21 actos que quedan,
> NINGUNO trae nodo puente y NINGUNO trae par `D` interno.** **Todos los actos con puente del tramo
> estan ya cerrados.** Con ellos, **el motivo sellado de `P.10` y el cuarto motivo se quedan SIN
> SUJETO en lo que resta del tramo**: lo que queda son **21 actos de tres miembros con dos pares `A`
> leidos y uno sin veredicto**, mas los dos con dueno. **Los lotes que vienen seran casi todos
> fusiones**, y eso cambia el ritmo de las colisiones.

**NO SE FUNDIO NINGUN ACTO CON DUENO**, **no se toco la mesa `OP-M-03` ni sus dos colisiones**, **las
dos colisiones viejas de `OP-U-02` siguen vigentes con su duena**, y **las cinco fichas `OP-M-02`
consumidas no se ejecutaron**: lo consumado no se ejecuta ni se rehace.

---

## 11. CONDICIONES DE PARADA, RECORRIDAS

| condicion | se cumple? |
|---|---|
| doctrina nueva inventada | **NO**: los catorce discutibles y los seis pendientes quedan bajo letra citable (`P.1`, `P.5`, `P.8`, `P.10`, `P.12`, `P.16`, guarda `1B`, y actas 54, 55, 61, 64, 66, 67 y 68). **Lo que no tiene letra va como PREGUNTA, no como regla**: la linea base nueva del censo **se sube como pregunta** y **el instrumento no se toca** |
| contradiccion sin regla de correccion | **NO**: las dos colisiones nuevas **tienen carril escrito** (la duena es quien la fabrica), estaban **predichas** y **calzan al digito** |
| decision de fundador | **NINGUNA SE TOMA**: el merge sigue siendo suyo |
| fallo tecnico repetido | **NO**: Gate 0 y las tres suites en verde |
| campana consumada | **NO**: quedan **21 actos y 63 nodos** del tramo, la mesa `OP-M-03` y las fases 04 en adelante |
| **cierre de la fase 03** (la parada de `AUDITOR.md`) | **NO SE CUMPLE TODAVIA**: quedan 21 actos, dos de ellos con dueno, y los **14** declarados siguen sin destino resuelto |
| credenciales | no hicieron falta |

---

## 12. HASH FINAL Y COMMITS

**Los commits de trabajo de esta vuelta, escritos en la rama `pasada-unica` y leidos hoy con
`git log --oneline`:**

| commit | que lleva |
|---|---|
| **`764523c0`** | **TAREA 1 entera**: el registro del acta 68 (`+170`, `0` borradas, 64 agujas, dos negativas de sustancia) **mas la APERTURA medida antes de la primera operacion** |
| **`471971de`** | **TAREA 2**: el lote E ejecutado (5 fusiones, 1 declarado, 13 nodos muertos, `P.16` limpio, **dos colisiones fabricadas y predichas**, Gate 0 con su ciclo de tres y las tres suites en verde) |
| **`9073ed13`** | **el registro del lote E** (`+440`, `0` borradas, 18 agujas, idempotencia mordiendo, barrido con `AMBAR` en 0) |
| **`331612cc`** | **el reporte entero**, leido hoy con `git log --oneline` |

**EL HASH FINAL DE LA VUELTA ES EL DEL COMMIT QUE ESCRIBE ESTA MISMA LINEA, y por eso no se puede
escribir dentro de si mismo: un commit no puede contener su propio hash.** **Los CUATRO anteriores
estan arriba, ninguno de memoria**, y **la cadena entera queda escrita en esta cabecera**, que es lo
que la regla 7 pide y lo que el commit del reporte no podia contener. Es la misma via que las vueltas 65 a 68 usaron, y la regla 7 pide
exactamente esto: el hash final y los commits anteriores en la cabecera de la seccion 12.

**LAS GUARDAS DE CIERRE, RE-CORRIDAS TRAS ESTA EDICION** (regla 1: lo que la propia vuelta mueve, se
remide antes de publicar):

| guarda | comando | resultado |
|---|---|---|
| **la cabecera se talla, no se teclea** | `tallar_cabecera_reporte.py --vuelta 69 --comparar docs/loop/REPORTE.md` | **`CABECERA: IDENTICA AL TALLADOR`**, 14 filas cotejadas, DISTINTAS 0, ausentes 0 ([`SALIDA_V69_CABECERA_COMPARADA.txt`](SALIDA_V69_CABECERA_COMPARADA.txt)) |
| **las promesas de marcado, por maquina** | `comprobar_promesas_de_marcado.py --reporte docs/loop/REPORTE.md --plan docs/loop/PLAN_V69_OPU02_LOTE_E.json` | **2 promesas medidas, 2 CUMPLIDAS, 0 INCUMPLIDAS** ([`SALIDA_V69_PROMESAS.txt`](SALIDA_V69_PROMESAS.txt)) |
| **el barrido de titulos, re-corrido AL CIERRE** | `barrido_titulos_tallados.py` | **453 ficheros, `ROJO` 32** (linea base sin mover), **`AMBAR` 0**, `ROTULADO` 47, `CENSO` 224 ([`SALIDA_V69_BARRIDO.txt`](SALIDA_V69_BARRIDO.txt)) |
| **la cuenta agregada de perdidas, por maquina** | la regla nueva del acta 68, estrenada sobre esta misma vuelta | **21 perdidas, 14 con atenuante, 6 del pendiente 4, 4 con atenuante medido**, y **la fila excluida DICHA** ([`SALIDA_V69_CUENTA_ATENUANTES.txt`](SALIDA_V69_CUENTA_ATENUANTES.txt)) |

**Cero guiones largos y cero guiones medios**, contados por maquina sobre el fichero entero.
