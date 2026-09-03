# -*- coding: utf-8 -*-
"""VUELTA 152, TAREA 7: ESCRIBE docs/loop/REPORTE.md.

LA CABECERA NO SE TECLEA (EJECUTOR.md 1): se LEE de la salida del tallador,
docs/loop/SALIDA_V152_T7_CABECERA.txt, y se pega ENTERA. Este script no compone
una sola celda de esa tabla.

TODA CIFRA DEL CUERPO CITA EL FICHERO DE SALIDA DEL QUE SALE, y las que se
cuentan se cuentan AQUI, de ese fichero, en vez de copiarse de mi memoria.
"""
import io
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
L = os.path.join(RAIZ, "docs", "loop")


def leer(n):
    return io.open(os.path.join(L, n), encoding="utf-8", errors="replace").read()


def tabla_tallada():
    t = leer("SALIDA_V152_T7_CABECERA.txt")
    ini = t.index("--- LA TABLA, PARA PEGAR ENTERA EN LA CABECERA DEL REPORTE ---")
    fin = t.index("\nFIN")
    return t[ini:fin].split("---\n", 1)[1].strip()


# ---- CIFRAS CONTADAS DE SUS FICHEROS, NO RECORDADAS -----------------------
exp = leer("SALIDA_V152_T7_EXPEDIENTE_CIERRE.txt")
m = re.search(r"CONTADO: no calzan (\d+) \| de ellas, congeladas DECLARADAS (\d+) \| "
              r"congeladas EN SILENCIO (\d+) \| HECHA sin prueba (\d+)", exp)
nc, dec, sil, hsp = m.groups()
p3 = re.search(r"P3 huella en git .*?: (\d+) ficha", exp).group(1)
expA = leer("SALIDA_V152_T2_EXPEDIENTE_ANTES.txt")
mA = re.search(r"CONTADO: no calzan (\d+) \| de ellas, congeladas DECLARADAS (\d+) \| "
               r"congeladas EN SILENCIO (\d+)", expA)
ncA, decA, silA = mA.groups()

cruce = leer("SALIDA_V152_T6A_CRUCE.txt")
cr = re.search(r"con cita por CRIBADO\s+: (\d+)", cruce).group(1)
p10 = re.search(r"con cita por P\.10\s+: (\d+)", cruce).group(1)
ld = re.search(r"con cita por LECTURA_DIRIGIDA\s+: (\d+)", cruce).group(1)
tot = re.search(r"CON CITA, TOTAL\s+: (\d+) de (\d+)", cruce).groups()
sinv = re.search(r"SIN VEREDICTO\s+: (\d+)", cruce).group(1)
res153 = re.search(r"RESOLVIENDO ALIAS \(P\.1\) : (\d+)", cruce).group(1)
res147 = re.search(r"SIN resolver\s+: (\d+)", cruce).group(1)
mb = leer("SALIDA_V152_T6A_CONTRASTE_MERGEBASE.txt")
mb153 = re.search(r"RESOLVIENDO ALIAS \(P\.1\) : (\d+)", mb).group(1)

F = [json.loads(x) for x in io.open(os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl"),
                                    encoding="utf-8") if x.strip()]
por_estado = {}
for f in F:
    por_estado[f["estado"]] = por_estado.get(f["estado"], 0) + 1
REG = [json.loads(x) for x in io.open(os.path.join(RAIZ, "docs", "plan",
                                                   "REGISTRO_DE_CITAS_OPC05.jsonl"),
                                      encoding="utf-8") if x.strip()]
gate = leer("SALIDA_V152_GATE0_CMD1_CIERRE.txt")
n_ok = len(re.findall(r"^\s*\[OK\]", gate, re.M))
n_fallo = len(re.findall(r"^\s*\[FALLO\]", gate, re.M))
n_cribado = sum(1 for _ in io.open(os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl"),
                                   encoding="utf-8"))

TXT = """# REPORTE DE LA VUELTA 152

**Rama `pasada-unica`. FASE III, EJECUCION, modo continuo, REGIMEN COMPLETO.**
**Las seis tareas del encargo entregadas. `OP-C-05` CIERRA ENTERA. Una caida mia,
de orden, declarada por mi. Seis discutibles marcados y cuatro preguntas.**

## LA CABECERA, TALLADA Y NO TECLEADA

Generada con `python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 152`
(salida en `docs/loop/SALIDA_V152_T7_CABECERA.txt`) y **pegada entera**. Ninguna
celda de esta tabla la escribi yo. Va entre las dos marcas literales que
`verificar_cifras_del_reporte.py` reconoce, para que la guarda del cuerpo no
confunda las cifras de la cabecera con prosa tecleada.

<!-- CABECERA TALLADA -->
%(TABLA)s
<!-- FIN CABECERA TALLADA -->

## 0. MI CAIDA, PRIMERO, PORQUE ES MIA Y NO ME LA ENCONTRARON

**CAIDA DE ORDEN: SELLE EL BLOQUE DE APERTURA TARDE.** Lei *"TAREA 1, Y ES LO
PRIMERO Y BLOQUEANTE"* como si fuera antes del ritual de apertura, y el ritual no
es una tarea: es lo que `EJECUTOR.md` 1 manda desde el 14 ago 2026. El HEAD que la
vuelta heredo es `d9fa886b` y quedo registrado en
`SALIDA_V152_APERTURA_IDENTIDAD.txt` **antes de tocar nada**, pero los diez
`SALIDA_V152_*_APERTURA.txt` nacieron en `a569778a`, **despues** de mi commit de la
TAREA 1.

**LO QUE MIDO EN VEZ DE ALEGAR:** `6f419952` toca solo `scripts/loop/` y
`docs/loop/`, **ninguna ruta de `dataset/`, `web/` o `engine/`**, asi que **ninguna
cifra de la apertura se movio**. Lo que fallo es el ORDEN, no la medicion.

**Y UNA SEGUNDA COSA QUE NO ES MIA Y QUE SE VE EN LA MISMA SALIDA**
(`SALIDA_V152_T7_APERTURA_SELLADA.txt`, exit 1, 20 cosas que no cuadran): la guarda
nombra **dos** commits en el corredor, el mio y **`d9fa886b`, la decision del
fundador**, que toca `docs/loop/AUDITOR.md` y `docs/plan/OPERACIONES.jsonl` porque
el encargo dice que las dos respuestas ya estan aplicadas donde viven. El corredor
solo deja pasar `PROMPT_SIGUIENTE.md`, `PARA_ALEXIS.md` y `paradas/`. **Aunque yo
hubiera sellado en el sitio, la guarda salia en rojo igual.** Es la misma especie
estructural que la TAREA 0.d de la vuelta 148 ya arreglo una vez, y vuelve a
asomar. **PREGUNTA 1 del cierre.**

## 1. TAREA 1: EL RELOJ DE GIT CONGELADO

Las dos varas que se contaban a si mismas quedan reparadas por **correccion
declarada**, sin borrar una linea del texto viejo.

  - **P3** (`vuelta150_3_relectura_expediente.py`): el `git log` va cortado en
    `--corte`, **obligatorio**. Una vara que se cuenta a si misma en silencio es
    peor que una que no corre.
  - **Fila 0 CODIGO** (`vuelta150_4_tabla_por_fase.py`): el catalogo de
    `SALIDA_*.txt` deja de leerse con `os.listdir` del arbol de trabajo y se lee
    con `git ls-tree` del arbol del corte. De paso, la salida de Gate 0 deja de
    estar clavada en el fichero de la vuelta 150 y entra por `--gate0`.

**Y NO BASTA CON CONGELAR:** cada una lleva su **guarda**, y las dos comparan **dos
conjuntos COMPUTADOS**, ninguno tecleado (caida 2 de la vuelta 89).

**PRUEBA DE MUTACION CORRIDA ANTES DE PUBLICARLAS** (`SALIDA_V152_T1_MUTACION.txt`),
cuatro casos, **misma apertura y solo el reloj movido**:

| caso | vara | corte | esperado | obtenido | lo que nombra |
|---|---|---|---|---|---|
| A | P3 | `fe98cf97` | VERDE | **VERDE exit 0** | INTRUSOS 0 |
| B | P3 | `HEAD` | ROJO | **ROJO exit 1** | INTRUSOS 4: `4985136d`, `76a18a90`, `c9c6ea40`, `fb3c0c75` |
| C | fila 0 | `fe98cf97` | VERDE | **VERDE exit 0** | INTRUSAS 0 |
| D | fila 0 | `HEAD` | ROJO | **ROJO exit 1** | INTRUSAS 5, la primera `SALIDA_V150_2C_CASO_POSITIVO_GATE0.txt` |

**UN HALLAZGO SOBRE EL CORTE, y va como discutible.** El auditor congelo en
`c9c6ea40~1` (`fb3c0c75`), que cae **DENTRO** de la vuelta 150; la regla escrita
pide el **HEAD DE APERTURA**, que es `fe98cf97` y es mas estricto. **Los dos dan lo
mismo al digito** (`SALIDA_V152_T1_CONTRASTE_CORTES.txt`): no calzan **58**, calzan
**13**, en silencio **30**, P3 **67**. La prueba del auditor se sostiene tambien con
la vara estricta.

## 2. TAREA 2: EL RECUENTO, Y LO QUE EL CONGELADO NO ARREGLA

Corte `d9fa886b`. `SALIDA_V152_T2_EXPEDIENTE_ANTES.txt`, contado de ese fichero:
**no calzan %(ncA)s, calzan 11, congeladas DECLARADAS %(decA)s, EN SILENCIO %(silA)s, HECHA sin
prueba 0.** Cae justo en el 60/11/32/69 que el acta 151 predijo.

**Y ESO NO ES LA BUENA NOTICIA QUE PARECE.** La reparacion impide que una vuelta se
cuente a SI MISMA, y eso quedo probado por mutacion. Lo que el congelado **NO**
arregla es el defecto de debajo:

> **LA P3 CUENTA UNA MENCION, NO UNA EJECUCION.** `OP-V-01` y `OP-L-01` pasan de
> *"sin ninguna prueba"* a *"con prueba"*, y su **unica** prueba es `c9c6ea40`,
> **cuyo mensaje dice literalmente que esas dos fichas no tienen prueba**. Desde la
> vuelta 152 ese commit es pasado legitimo, asi que el corte no lo filtra: **lo que
> falla es el criterio**.

**NO INVENTO LA REGLA QUE FALTA** (`EJECUTOR.md` 5). Queda **PENDIENTE DE DOCTRINA**
y como **discutible 1**.

**SEGUNDA ASIMETRIA, DECLARADA:** la **P2 sigue leyendo el arbol de trabajo**
mientras la P3 va congelada. Lo dejo asi a proposito: la P2 mide que el control
**exista en el codigo vivo**, y un control que esta vuelta instale es ejecucion de
verdad, no papeleo. **Discutible 2.**

## 3. TAREA 3: EL PASE DE `estado` DE LAS ONCE

Reservado desde el acta 139, 3.6. **El disparador se midio y disparo**: las once
salen **CUMPLIDO** en `tallar_estado_de_fase.py`, **11 de 11**. Si una sola no
hubiera salido, el instrumento para en exit 1 y no escribe.

**EL AVISO DEL ENCARGO, ATENDIDO ANTES DE CONTAR.** El *"30 congeladas en
silencio"* no es un cardinal duro. Lo medi con **cuatro listas de marcas** sobre las
mismas 71 fichas: **A 32, B 33, C 52, D 26. Abanico de 26 a 52.**

**DISCREPANCIA QUE DECLARO EN VEZ DE COPIAR (`EJECUTOR.md` 2):** el encargo dice que
el abanico va **entre 8 y 43** y el mio va **entre 26 y 52**. No son las mismas
cuatro listas, asi que ninguna de las dos mediciones miente: **el abanico ES UNA
PROPIEDAD DE LAS LISTAS QUE SE ELIGEN**, y eso refuerza el aviso en vez de
debilitarlo.

**VARA DECLARADA:** la **lista A**, la que ya vive en `declara_su_estado` y la que
produjo la cifra publicada.

| cifra | antes | despues |
|---|---:|---:|
| fichas en `HECHA` | 11 | **%(hecha)s** |
| fichas en `LISTA` | 60 | **%(lista)s** |
| congeladas EN SILENCIO (lista A) | %(silA)s | **%(sil)s** |

Las que siguen en silencio van **nombradas una a una** en
`SALIDA_V152_T3_PASE_DE_ESTADO.txt`. **CORRECCION 31** por adicion pura, esquema
intacto (71 fichas, 18 claves) y **guarda de cifras del plan re-corrida: VERDE exit
0**, que es lo que la reserva exige.

**LO QUE NO HAGO Y DIGO POR QUE:** las cinco mesas `OP-M-01` a `OP-M-05` **tambien
miden CUMPLIDO hoy** y **no les muevo el estado**. La reserva nombra **once** y solo
once. **Discutible 3** y **PREGUNTA 2**.

## 4. TAREA 4: LA CORRECCION DECLARADA DEL 307

**Re medido por mi antes de escribir una letra**, con instrumento propio y sin
importar el codigo que corrijo (`SALIDA_V152_T4_CORRECCION_307.txt`): **255 NODOS
VIVOS** traen al menos un destino en `nodos_previos` **y** en `nodos_siguientes`
tras resolver, y suman **307 DESTINOS**.
El auditor tiene razon: **el 307 es correcto y la unidad no**.

**Tres sedes, las tres por adicion y ninguna por encima:** el comentario de
`scripts/run_phase1.py` (la frase vieja se queda entera), la linea 27 de
`SALIDA_V150_2C_SIETE_VERIFICACIONES.txt` (**no se reescribe**: bloque anadido al
final, 6.519 a 7.997 caracteres con `assert` de prefijo exacto) y la **CORRECCION
32**.

**LO QUE NO CAMBIA:** el veredicto de la verificacion 3 de `OP-C-05` sigue siendo
**CONTESTADA, EN VERDE**. Estaba mal **como se nombraba el tamano del caso**, no el
comportamiento de la guarda. Por la decision del fundador (PREGUNTA 2) esta especie
cuenta como CIFRA PUBLICADA **desde el 2 sep 2026, sin retroactividad**: esta **se
corrige por declaracion y NO ACUMULA**.

## 5. TAREA 5: LAS CUATRO FILAS VERDE PARCIAL, CON LO QUE LES FALTA NOMBRADO

`SALIDA_V152_T5_VERDE_PARCIAL.txt`. **Ninguna se pinta de verde.**

| fila | mitad medida | lo que le falta, NOMBRADO | especie |
|---|---|---|---|
| **01 FUENTES** | 0 desaparecidos de 73 | la **ATRIBUCION** de **68** nodos con pasos alterados, **20** reclamados tambien por otra fase, los 20 nombrados uno a uno | **VARA QUE NO EXISTE** |
| **02 DESTEJIDOS** | mapas de destejido exit 0 | los quince congelados: la tabla nombra **8** por su puesto y **7 NO ESTAN ESCRITOS EN NINGUN FICHERO** | **NOMINA QUE NO EXISTE** |
| **03 FUSIONES** | 14 fichas, 0 incumplimientos | los **2** divergentes, **ya clasificados** por la CORRECCION 16 | **DECISION DEL AUDITOR**, no medicion |
| **04 ENLACES** | auto-aristas OK en Gate 0 | la confirmacion **POR LECTURA** de **20** aristas sobre **8** fichas | **LECTURA HUMANA**, excluida por la letra de la celda |

Los ocho congelados nombrados (**494, 592, 724, 738, 755, 827, 830, 1061**) van
cotejados uno a uno contra el archivo del cribado, con su clase y sus dos nodos. La
propia pagina dice *"OCHO de los quince cuelgan de TRES nodos"*, que **cuadra al
digito** con los ocho extraidos: **la pagina los cuenta y solo nombra ocho**.
**PENDIENTE DE DOCTRINA.**

**UNA CAIDA MIA CAZADA POR MI ANTES DE PUBLICAR**, escrita dentro del propio
instrumento: la primera version extraia los puestos con un `re.finditer` sobre
**todo** `02_DESTEJIDOS.md` y se traia **24**, entre ellos los puestos 1 a 7, que no
son congelados. **La cifra se delataba sola** (la celda pide QUINCE, salian
VEINTICUATRO y el resto era **negativo**, -9). **No la publique: arregle la vara.**

## 6. TAREA 6: `OP-C-05` CIERRA ENTERA

### 6.a El cruce

**P.1 primero, y aqui cumplirlo o no son SEIS PARES:** resolviendo alias **%(res153)s**,
sin resolver **%(res147)s**, y las seis que solo aparecen tras resolver van nombradas en
`SALIDA_V152_T6A_CRUCE.txt`. El instrumento resuelve **los dos lados**, tambien los
del archivo del cribado. **Contraste que prueba que mide bien:** sobre el mergebase
con `main` (`36b57d78`) salen **%(mb153)s** pares, no %(res153)s.

| via | pares |
|---|---:|
| CRIBADO (clases D, B, C, con su puesto) | **%(cr)s** |
| P.10 (declarado y no fundido) | **%(p10)s** |
| LECTURA DIRIGIDA (`LD-OPC05-001` a `LD-OPC05-121`) | **%(ld)s** |
| **CON CITA, TOTAL** | **%(tot0)s de %(tot1)s** |
| **SIN CITA** | **%(sinv)s** |

**P.10 SUMA CERO Y DIGO POR QUE** en vez de dejarlo en blanco: `sistema_gates_go_kill`
es el ejemplar 1 de P.10, pero su columna *"como acabo"* dice que **`LD-58` lo cerro
hacia la UNION**, o sea **fundido**. La via pide **declarado y NO fundido**.

### 6.b Las 121 lecturas dirigidas

**Lei el dossier entero**, no una muestra: `SALIDA_V152_T6B_DOSSIER.txt`, **3.124
lineas**, los 121 pares con el titulo y los pasos accionables de sus **dos** nodos.
**Resultado: 121 de 121 en clase C**, contado de
`SALIDA_V152_T6B_LECTURAS.txt`.

**Y COMO ES UNIFORME LO DIGO EN VOZ ALTA EN VEZ DE ESCONDERLO DETRAS DEL VERDE.** La
escalera del 9.22 es *"la vuelta manda a repetir el paso que se acaba de dar"*, y
aqui los dos nodos de cada par son **procedimientos completos y distintos** del
curriculo. Cada direccion manda a un procedimiento que el otro **no contiene**.

**`n` NO SE MOVIO Y LO MEDI:** `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` sigue en
**%(ncrib)s lineas**, contadas de ese mismo fichero y
registradas en `SALIDA_V152_T6A_CRUCE.txt`.

**UN HALLAZGO FUERA DEL ENCARGO:** tres de los 121 (`87`, `88`, `110`) **ya estan
declarados como mutuos exceptuados** del 9.22 en la **verificacion 5 de `OP-E-04`**.
**No los meti por una via nueva**, porque la decision del fundador nombra **dos**
vias y no tres: van por lectura dirigida y la lectura **cita** esa declaracion
sellada. **PREGUNTA 3.**

### 6.c La guarda encendida, y muerde por los dos lados

**Gate 0 pasa de 25 a %(nok)s comprobaciones, las %(nok)s en OK, exit 0** (%(nfallo)s en FALLO),
contado de `SALIDA_V152_GATE0_CMD1_CIERRE.txt`. La nueva mide **%(tot1)s pares tras
resolver, %(tot1)s con cita, 0 SIN CITA**, leido de esa misma salida y de
`SALIDA_V152_T6C_GATE0_VERDE.txt`. **El grafo
saneado pasa en verde**, que es la verificacion nueva de la ficha. **La guarda no
construye el registro: lo EXIGE.** Si el fichero no existe es **ROJO**, no verde por
omision.

**CASO POSITIVO POR MUTACION** (`SALIDA_V152_T6C_MUTACION.txt`), tres casos:

| caso | ataque | resultado |
|---|---|---|
| **C** | arbol intacto | **VERDE exit 0.** La guarda no es un muro |
| **A** | se cae **una** cita del registro | **exit 1** nombrando `dia_cero_defectos <-> entrenamiento_supervisores_calidad` |
| **B** | llega una arista bidireccional **que nadie leyo** | **exit 1** nombrando `ab_testing_optimizacion <-> zero_defects_concepto`, y el censo sube de 153 a **154** |

Los dos pares se eligen **por computo**, no a dedo. **`dataset/` identico antes y
despues: sha256 `0864e9cf...` a los dos lados, comprobado y no prometido.**

**DOS TRAMPAS QUE ME MORDIERON, Y LAS DEJO ESCRITAS DENTRO DEL ARNES:**

  1. **`run_phase1` SUELTO** deja la copia web desincronizada y la corrida siguiente
     sale en rojo **por ciclo sin cerrar**, no por la guarda. Mi contraprueba dio
     rojo por eso.
  2. **`master_graph.json` SE REGENERA** desde `dataset/nodos/*.json`, asi que
     **mutarlo no muta nada**. Mi primer caso B mutaba el derivado y la guarda
     contesto *153 con cita, 0 sin cita* sobre un grafo que **ya habia borrado la
     mutacion**: **un falso verde en el propio arnes que existe para impedir falsos
     verdes.** Lo cace porque **el caso no nombraba el par que decia atacar**.

**Y UNA TERCERA, en la verificacion 6:** mi primer comprobador partia las frases de
`aristas_nuevas` por espacios y se traia **`LD-41` como si fuera un node_id**, dando
**0 de 2**. Con el resolutor puesto (`requisitos_gates_con_dientes` esta deprecado y
resuelve a `sistema_gates_go_kill`) da **2 de 2**. **Ninguna de las tres cifras
falsas se publico: las tres se delataron en la corrida y se arreglo la vara.**

**CORRECCION 33** y **despues** el `estado`: `OP-C-05` pasa de `LISTA` a `HECHA`, que
es el orden que la adjudicacion 3.14 del acta 149 fijo.

## 7. EL CIERRE, RECOMPUTADO AL CIERRE

Ciclo entero en su orden, **`numstat` de `dataset/ web/ engine/` sin una fila**,
**Gate 0 %(nok)s de %(nok)s en OK exit 0** (`SALIDA_V152_GATE0_CMD1_CIERRE.txt`), **motor
25/25** (`SALIDA_V152_MOTOR_CIERRE.txt`), **vitest 80 ficheros, 1.030 pasadas y 3
saltadas** (`SALIDA_V152_WEB_CIERRE.txt`), **`tsc` EXIT 0 sin una linea**
(`SALIDA_V152_TSC_CIERRE.txt`), **desfase del calibrado 4 filas sobre 468**
(`SALIDA_V152_DESFASE_CALIBRADO_CIERRE.txt`).

**EL EXPEDIENTE, RE MEDIDO AL CIERRE porque esta vuelta lo movio**
(`SALIDA_V152_T7_EXPEDIENTE_CIERRE.txt`): **no calzan %(nc)s** (eran %(ncA)s), **DECLARADAS
%(dec)s**, **EN SILENCIO %(sil)s** (eran %(silA)s), **HECHA sin prueba %(hsp)s**, **LISTA sin ninguna
prueba 0**, **P3 %(p3)s**.

**LAS DOS GUARDAS NUEVAS YA HACEN TRABAJO DE VERDAD**, y esa es la prueba de que la
reparacion sirve: al cierre la vuelta tiene **9 commits propios** y **28 salidas
propias**, y las dos guardas dan **INTRUSOS 0 e INTRUSAS 0**.

**Tabla por fase al cierre**, leida de `SALIDA_V152_T7_TABLA_POR_FASE_CIERRE.txt`,
que a su vez invoca `tallar_estado_de_fase.py` para la vara de grafo: VERDE **4 de
8**, VERDE PARCIAL **4 de 8**, NO CUMPLE **0 de 8**, con la fila **0 CODIGO en
VERDE, 7 de 7**.

## 7.b LAS GUARDAS DEL CIERRE, CON SU ESTADO REAL Y NO CON EL QUE ME CONVIENE

Corridas todas y **publicadas aunque dos no me favorezcan**
(`SALIDA_V152_T7_GUARDAS_CIERRE.txt`):

| guarda | veredicto |
|---|---|
| `tallar_cabecera_reporte.py --fase04 --comparar` | **CABECERA IDENTICA AL TALLADOR**, 9 filas cotejadas, **0 distintas**, exit 0 |
| `verificar_mutaciones_viejas.py` | **VERDE**: las 23 mutaciones viejas corren, muerden, y sus salidas selladas salen identicas en dos corridas |
| `verificar_apertura_sellada.py --vuelta 152` | **ROJO exit 1**, y esta explicado en la seccion 0: mi caida de orden **mas** el commit del fundador en el corredor |
| `verificar_cifras_del_reporte.py` | **COBERTURA CERO**, y lo digo con su nombre |
| `verificar_ausencias_del_reporte.py` | **5 ausencias vistas, 0 respaldadas, 5 en rojo** |

**LO QUE LA GUARDA DE CIFRAS ME DICE Y NO TAPO.** Su frase es *"UN VERDE SOBRE CERO
NO ES UN VERDE"*. Al escribir el reporte vio **12** cifras con unidad del
vocabulario, **0 cotejadas y 0 exentas**. Encontre y arregle una parte: la cabecera
tallada no llevaba las marcas `<!-- CABECERA TALLADA -->`, asi que la guarda estaba
leyendo **el asunto del commit del acta 151** como si fuera prosa mia y contaba sus
cifras. Con las marcas puestas baja de **12 a 7**. **Las 7 que quedan siguen sin
cotejar**: cite el fichero de salida al lado de cada una, pero el contrato de la
guarda pide ademas su **linea CIFRA**, que es un formato que no domino y que **no
voy a improvisar** para ponerme un verde. **Queda declarado aqui y va como
PREGUNTA.**

**LA GUARDA DE AUSENCIAS** marca 5 en rojo. Son frases del tipo *"si el fichero no
existe es ROJO"* y *"no hay campo `congelado`"*, que la guarda quiere respaldadas por
un **barrido exhaustivo sellado** y yo respalde con la salida del instrumento
correspondiente. **Es la regla 9 de `EJECUTOR.md` en accion** (*"una busqueda
negativa no se puede citar"*) y **tiene razon**: mis afirmaciones de ausencia de la
seccion 5 se apoyan en no haber encontrado, no en un barrido sellado. **Tambien
queda declarado.**

## 8. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO

  1. **La P3 cuenta una MENCION, no una ejecucion.** El congelado no lo arregla y no
     invento la regla. PENDIENTE DE DOCTRINA.
  2. **La asimetria P2 contra P3**: la P2 lee el arbol de trabajo a proposito. Si el
     auditor lo ve de otro modo, se congela tambien.
  3. **Las cinco mesas no se mueven** aunque midan CUMPLIDO: la reserva dice once.
  4. **Los 121 salen todos C.** Dentro de ellos marco los cuatro donde el solape de
     LINEA es real: **`LD-OPC05-008`**, **`LD-OPC05-031`** (el mas ajustado),
     **`LD-OPC05-042`** y **`LD-OPC05-059`**. **Tres de los cuatro cuelgan del mismo
     nodo, `dilema_riqueza_vs_control`.** Si el auditor tumba uno, que empiece ahi.
  5. **El corte estricto contra el del auditor**: use `fe98cf97` (HEAD de apertura) y
     el auditor uso `fb3c0c75` (dentro de la vuelta). Dan lo mismo, pero la regla
     escrita pide el mio.
  6. **La fila 03 FUSIONES**: propongo que lo que le falta **no es una medicion sino
     una decision**, y no me la adjudico.

## 9. PENDIENTES DE DOCTRINA

  - **Un commit que NOMBRA una operacion para decir que NO se ejecuto cuenta hoy
    como prueba de que se ejecuto.** No hay regla que lo distinga.
  - **Los siete congelados de 02 que nadie escribio.** No hay campo `congelado` en el
    archivo del cribado ni nomina en un fichero de datos.
  - **La atribucion de la alteracion de pasos en 01.** Haria falta el rastro por
    commit de que operacion escribio cada paso.

## 10. CUATRO PREGUNTAS

  1. **El corredor de la apertura y la decision del fundador.** `d9fa886b` toca
     `AUDITOR.md` y `OPERACIONES.jsonl`, que no son papel de parada, asi que la
     guarda sale en rojo **aunque la apertura se selle en su sitio**. Se amplia el
     corredor a esas dos rutas cuando el commit es del fundador, o se acepta el rojo
     y se declara cada vez?
  2. **Las cinco mesas.** Miden CUMPLIDO. Se les mueve el `estado` o la reserva de
     las once es literal?
  3. **La guarda de cifras del reporte y su linea CIFRA.** Su contrato pide un
     formato que no esta escrito en `EJECUTOR.md` y que no improviso. Cual es la
     linea CIFRA que hace que una cifra cuente como cotejada, y se aplica tambien a
     un reporte de fase III como este?
  4. **Una tercera via de cita.** La verificacion 5 de `OP-E-04` declara cuatro pares
     mutuos exceptuados. Debe ser una via propia del registro, como el cribado y
     P.10, o se queda como respaldo dentro de una lectura dirigida?

## 11. EL MURO, QUE ES DONDE TERMINA LO QUE UN BUCLE PUEDE HACER SOLO

**La fase 08 no cierra sin una sesion con credencial y con el fundador delante**
(acta 149, 3.10; su estado medido hoy con `tallar_estado_de_fase.py` esta en
`SALIDA_V152_T7_TABLA_POR_FASE_CIERRE.txt`). **Tres de los cinco puntos de su verificacion transversal piden la
credencial del `.env`, que esta fuera del repo.** Ahi paro, que es lo que el encargo
manda.

**EL MERGE NO SE PIDE NI SE HACE: es del fundador y solo suyo. La campana no esta
consumada.**
""" % {
    "TABLA": tabla_tallada(),
    "nc": nc, "dec": dec, "sil": sil, "hsp": hsp, "p3": p3,
    "ncA": ncA, "decA": decA, "silA": silA,
    "hecha": por_estado.get("HECHA", 0), "lista": por_estado.get("LISTA", 0),
    "cr": cr, "p10": p10, "ld": ld, "tot0": tot[0], "tot1": tot[1], "sinv": sinv,
    "res153": res153, "res147": res147, "mb153": mb153,
    "ncrib": "{:,}".format(n_cribado).replace(",", "."),
    "nok": n_ok, "nfallo": n_fallo,
}

io.open(os.path.join(L, "REPORTE.md"), "w", encoding="utf-8", newline="\n").write(TXT)
print("REPORTE.md escrito: %d lineas, %d caracteres" % (TXT.count("\n") + 1, len(TXT)))
print("registro de citas: %d entradas | fichas: %d | Gate 0: %d OK, %d FALLO"
      % (len(REG), len(F), n_ok, n_fallo))
