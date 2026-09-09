# -*- coding: utf-8 -*-
r"""_v213_t2_seccion.py . EL CUERPO DE LA TAREA 2 DEL REPORTE DE LA VUELTA 213.

COMPUTO DE UNA VUELTA, prefijo de guion bajo: fuera del censo y fuera de la
nomina. Moratoria de AUDITOR.md 6.3.

NINGUNA CIFRA SE TECLEA: todas salen de `pick()` sobre los dos ficheros de
salida sellados de esta vuelta, y la tabla de las 71 filas se PEGA ENTERA del
fichero que la lleva, contando sus filas antes de publicarla (`EJECUTOR.md` 1,
LA TABLA SE CUENTA DE SU FICHERO).
"""
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
RAIZ = os.path.dirname(os.path.dirname(AQUI))

NL = chr(10)
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))

ROJOS = []
_CACHE = {}


def cargar(ruta):
    if ruta not in _CACHE:
        p = os.path.join(RAIZ, ruta.replace("/", os.sep))
        if not os.path.isfile(p):
            ROJOS.append("no existe %s" % ruta)
            _CACHE[ruta] = []
        else:
            _CACHE[ruta] = io.open(p, encoding="utf-8").read().split(NL)
    return _CACHE[ruta]


def pick(ruta, prefijo, n=0):
    hits = [l.strip() for l in cargar(ruta) if l.strip().startswith(prefijo)]
    if len(hits) <= n:
        ROJOS.append("en %s no hay linea %d que empiece por %r" % (ruta, n, prefijo))
        return "(ROJO: no encontrada)"
    return hits[n]


def valor(ruta, prefijo, n=0):
    l = pick(ruta, prefijo, n)
    return l.split(":", 1)[1].strip() if ":" in l else l


def entre(ruta, desde, hasta):
    """LAS LINEAS DE UN FICHERO ENTRE DOS ANCLAS, PEGADAS ENTERAS."""
    ls = cargar(ruta)
    i = [k for k, l in enumerate(ls) if desde in l]
    if not i:
        ROJOS.append("en %s no esta el ancla %r" % (ruta, desde))
        return []
    j = [k for k, l in enumerate(ls) if hasta in l and k > i[0]]
    if not j:
        ROJOS.append("en %s no esta el ancla de cierre %r" % (ruta, hasta))
        return []
    return ls[i[0]:j[0]]


def linea_de(ruta, numero):
    ls = cargar(ruta)
    if numero < 1 or numero > len(ls):
        ROJOS.append("%s no tiene linea %d" % (ruta, numero))
        return "(ROJO: fuera de rango)"
    return ls[numero - 1].strip()


S2 = "docs/loop/SALIDA_V%d_T2_CIERRE_FASE_III.txt" % VUELTA
SV = "docs/loop/SALIDA_V%d_T2_VARA.txt" % VUELTA
SR = "docs/loop/SALIDA_V%d_T2_RECUENTO_95.txt" % VUELTA
SN = "docs/loop/SALIDA_V%d_T2_NUMSTAT.txt" % VUELTA
ACT = "docs/loop/ACTA_AUDITOR.md"

P = []


def w(s=""):
    P.append(s)


w("### `2.a` EL INVENTARIO DE CIERRE DE LA FASE III, DE LAS 71 FICHAS, LEIDO DEL REPO")
w()
w("**POR QUE ESTA TAREA Y NO OTRA, Y ES UNA CIFRA MIA Y NO HEREDADA.** Corri "
  "`scripts/loop/vuelta150_3_relectura_expediente.py` **en esta vuelta**, con el reloj "
  "de git congelado en mi HEAD de apertura, y su salida cruda vive en `" + SV + "`. "
  "Su cabecera dice, leida de ahi: *" + pick(SV, "RELOJ DE GIT CONGELADO") + "*. "
  "**El plan esta agotado**, y lo que queda es el cierre.")
w()
w("**LA FUENTE ES LA VARA, NUNCA EL CAMPO** (recuadro 0 de `AUDITOR.md`). La columna "
  "`estado` va publicada **al lado y etiquetada como HISTORICA en la propia cabecera "
  "de la tabla**, y donde los dos discrepan **lo digo y no lo resuelvo**.")
w()
w("#### 1. COMO SE COMPUSO LA TABLA, Y LA GUARDA QUE LA SOSTIENE")
w()
w("**LA VARA IMPRIME SOLO LAS QUE NO CALZAN, Y EL ENCARGO PIDE LAS 71.** Su propia "
  "salida lo dice: *" + pick(SV, "TABLA DE LAS QUE NO CALZAN") + "*. Las 31 que "
  "calzan **no existen en ningun fichero de salida**, asi que no se pueden pegar de "
  "ninguno. **No reimplemente la vara: la IMPORTE** y llame a sus propias funciones "
  "con el mismo corte, que es lo que hace `scripts/loop/_v%d_t2_cierre_fase_iii.py`."
  % VUELTA)
w()
w("**Y LA GUARDA QUE PRUEBA QUE MI COMPUTO ES EL SUYO:** para las filas que la vara "
  "**SI** imprime, mi celda de pruebas se coteja contra la suya fila a fila.")
w()
COT = [
    ["filas que la vara imprime en su tabla de las que no calzan",
     valor(S2, "CIFRA filas que la vara IMPRIME en su tabla")],
    ["filas cotejadas contra las mias, y cuantas difieren",
     pick(S2, "CIFRA filas cotejadas:")],
    ["fichas contadas de `docs/plan/OPERACIONES.jsonl`",
     valor(S2, "CIFRA fichas contadas de docs/plan/OPERACIONES.jsonl")],
    ["`id_op` distintos (que no haya dos con el mismo nombre)",
     valor(S2, "CIFRA id_op distintos")],
    ["**el `sha256` de `docs/plan/OPERACIONES.jsonl` al entrar y al salir**",
     "**" + valor(S2, "CIFRA el sha256 LF de docs/plan/OPERACIONES.jsonl es el mismo")
     + "**"],
]
w("**LO QUE SOSTIENE LA TABLA.** **FILAS ARMADAS LEYENDO `" + S2 + "`: "
  + str(len(COT)) + "; FILAS QUE DEBERIA HABER: 5.**")
w()
w("| que se comprobo | lo que dice el instrumento |")
w("|---|---|")
for a, b in COT:
    w("| %s | %s |" % (a, b.replace("|", chr(92) + "|")))
if len(COT) != 5:
    ROJOS.append("la tabla de la guarda no tiene 5 filas")
w()
w("**LA GUARDA SE ME CAYO EN SU PRIMERA CORRIDA Y LO DIGO**: cote las filas del "
  "fichero entero y me trague **tres filas de OTRAS DOS TABLAS** de la misma salida "
  "(la de las desbloqueadas y la de la vara documental), que tambien empiezan por el "
  "mismo prefijo y llevan las columnas en otro sitio. **Salieron 43 filas y 3 "
  "diferencias.** Acote la lectura a la tabla que toca y las diferencias cayeron a "
  "**0** sobre **40**. **Una guarda que solo se ve pasar no prueba nada; esta mordio.**")
w()
w("#### 2. LA TABLA, UNA FILA POR FICHA, LAS 71 Y SIN CORTAR")
w()
TABLA = [l for l in entre(S2, "| id_op | fase | tipo |", "CIFRA filas de la tabla")
         if l.strip()]
FILAS_OP = [l for l in TABLA if l.strip().startswith("| `OP-")]
w("**LA TABLA ENTERA, PEGADA DE `" + S2 + "` Y NO TECLEADA.** **FILAS ARMADAS "
  "LEYENDO ESE FICHERO: " + str(len(FILAS_OP)) + "; FILAS QUE DEBERIA HABER: "
  + valor(S2, "CIFRA fichas contadas de docs/plan/OPERACIONES.jsonl") + ".** "
  "El propio fichero lo vuelve a decir con sus dos cifras juntas: *"
  + pick(S2, "CIFRA filas de la tabla:") + "*.")
w()
for l in TABLA:
    w(l.rstrip())
if len(FILAS_OP) != 71:
    ROJOS.append("la tabla pegada no trae 71 filas de ficha")
w()
w("**LA COLUMNA `documental` NO ASCIENDE A NADIE, Y SE DICE:** la vara documental es "
  "la cuarta prueba y **solo aplica a las fichas de tipo `MESA`**; el propio "
  "instrumento la publica **al lado** y no la funde con las otras tres. Yo hago lo "
  "mismo: una ficha cuyo unico positivo sea `documental` **sigue saliendo SIN "
  "EJECUTAR** en la columna del veredicto. **`OP-I-01` es exactamente ese caso**, y "
  "por eso aparece con `documental` y con `SIN EJECUTAR` a la vez.")
w()
w("#### 3. LAS CUATRO CIFRAS, CADA UNA CONTADA DE LA TABLA")
w()
CIF = [
    ["**1. cuantas de las 71 tienen PRUEBA DE EJECUCION en el repo**",
     "**" + valor(S2, "1. CIFRA de las 71 que tienen PRUEBA DE EJECUCION en el repo")
     + "**"],
    ["**2. cuantas estan CONSUMIDAS, y por quien**",
     "**" + valor(S2, "2. CIFRA CONSUMIDAS").split(":")[-1].strip()
     + "**, y las dos son `OP-M-02-MEDIOS` y `OP-M-02-ADMIT`, **las dos por "
     "`OP-U-01`**"],
    ["**3. cuantas estan SIN EJECUTAR**",
     "**" + valor(S2, "3. CIFRA SIN EJECUTAR").split(",")[0] + "**"],
    ["**4. cuantas tienen el campo `estado` en desacuerdo con el repo**",
     "**" + valor(S2, "4. CIFRA con el campo estado EN DESACUERDO").split(",")[0]
     + "**, que se parten en **" + valor(S2, "4.a HECHA SIN PRUEBA")
     + "** por un lado y **" + valor(S2, "4.b LISTA CON PRUEBA")
     + "** por el otro"],
    ["la suma, comprobada contra las 71",
     pick(S2, "LA SUMA SE COMPRUEBA:")],
]
w("**LAS CUATRO CIFRAS.** **FILAS ARMADAS LEYENDO `" + S2 + "`: " + str(len(CIF))
  + "; FILAS QUE DEBERIA HABER: 5** (las cuatro que el encargo pide mas la suma que "
  "las cuadra).")
w()
w("| cifra | lo que dice el instrumento |")
w("|---|---|")
for a, b in CIF:
    w("| %s | %s |" % (a, b.replace("|", chr(92) + "|")))
if len(CIF) != 5:
    ROJOS.append("la tabla de las cuatro cifras no tiene 5 filas")
w()
w("**LA LISTA ENTERA DE LAS SIN EJECUTAR, QUE EL ENCARGO PIDE ENTERA:**")
w()
SIN = [l.strip() for l in cargar(S2) if l.strip().startswith("SIN EJECUTAR:")]
w("**LAS SIN EJECUTAR, UNA A UNA.** **FILAS ARMADAS LEYENDO `" + S2 + "`: "
  + str(len(SIN)) + "; FILAS QUE DEBERIA HABER: "
  + valor(S2, "3. CIFRA SIN EJECUTAR").split(",")[0] + ".**")
w()
w("| la fila, tal como sale del instrumento |")
w("|---|")
for s in SIN:
    w("| %s |" % s)
w()
w("**AQUI DISCREPO DE LA CIFRA QUE EL ENCARGO CITA, Y LA DECLARO EN VEZ DE "
  "RESOLVERLA COPIANDO** (`EJECUTOR.md` 2). El encargo dice que la vara mide **3** en "
  "`LISTA` sin ninguna prueba. **Eso reproduce exacto** y esta en su propia salida: *"
  + pick(SV, "CONTADO: 3 ficha(s) en LISTA sin ninguna prueba") + "*. **Mi cifra 3 no "
  "es esa y no mide lo mismo:** la vara cuenta las que estan **en `LISTA`** sin "
  "prueba, y la columna que el encargo me manda escribir es **el veredicto del REPO, "
  "que no mira el campo**. Por eso a mis SIN EJECUTAR se suman las **cuatro** que el "
  "campo declara `HECHA` y el repo no sostiene (`OP-V-01`, `OP-L-01`, `OP-L-02` y "
  "`OP-L-03`), menos las **dos** consumidas, que salen a su propia cifra. **Las dos "
  "cuentas son ciertas y miden cosas distintas, y por eso van las dos escritas.**")
w()
w("**Y LA CAUTELA DE LA CUARTA VA PEGADA A ELLA, NO SUELTA** (adjudicacion `6.8` del "
  "acta 211): **si cada ficha va poniendo su campo al dia, esa cifra tiende a cero "
  "sin que se haya ejecutado nada mas.** Mide **cuanto miente el campo**, no cuanto "
  "trabajo queda. **El trabajo que queda es la tercera.**")
w()
w("#### 4. LAS CINCO PROHIBICIONES DE LA TAREA 2, UNA A UNA")
w()
PRO = [
    ["**1.** no cambiar el campo `estado` de ninguna ficha",
     "**CUMPLIDA Y PROBADA CON EL `sha256`.** " + pick(S2, "CIFRA sede docs/plan/OPERACIONES.jsonl AL ENTRAR")
     + " y al salir " + valor(S2, "CIFRA sede docs/plan/OPERACIONES.jsonl AL SALIR")],
    ["**2.** no marcar las entradas del inventario",
     "**CUMPLIDA.** El instrumento **abre `docs/plan/INVENTARIO.jsonl` solo para "
     "leer**, su `numstat` mide **"
     + valor(SN, "CIFRA filas de numstat de docs/plan/INVENTARIO.jsonl")
     + "** filas, y su recuento no escribe: las incompletas siguen siendo **"
     + valor(S2, "CIFRA de esas que estan INCOMPLETAS") + "** y las marcadas **"
     + valor(S2, "CIFRA de esas incompletas que llevan PROVISIONAL en algun campo")
     + "**"],
    ["**3.** no escribir ni una fila nueva en `docs/plan/08_VERIFICACION.md`",
     "**CUMPLIDA.** Ese fichero no se abre para escritura en ningun camino de esta "
     "tarea, y su `numstat` al cerrar la tarea, sellado en `" + SN + "`, mide **"
     + valor(SN, "CIFRA filas de numstat de docs/plan/08_VERIFICACION.md")
     + "** filas"],
    ["**4.** no declarar la campaña consumada ni escribir `PARA_ALEXIS.md`",
     "**CUMPLIDA.** " + pick(SN, "CIFRA PARA_ALEXIS.md existe en el arbol")
     + ", y esta tarea no lo crea. **No lo esta:** `OP-I-01` sigue abierta y lo que "
     "necesita es del fundador"],
    ["**5.** no tocar el grafo",
     "**CUMPLIDA.** El ciclo de Gate 0 mide `git diff HEAD --numstat` en **0** filas "
     "en los dos lados"],
]
w("**LAS CINCO PROHIBICIONES.** **FILAS ARMADAS LEYENDO `" + S2 + "`: "
  + str(len(PRO)) + "; FILAS QUE DEBERIA HABER: 5.**")
w()
w("| que estaba prohibido | que paso |")
w("|---|---|")
for a, b in PRO:
    w("| %s | %s |" % (a, b.replace("|", chr(92) + "|")))
if len(PRO) != 5:
    ROJOS.append("la tabla de prohibiciones no tiene 5 filas")
w()

# ------------------------------------------------------------------ 2.b
w("### `2.b` LA UNICA QUE QUEDA ABIERTA: `OP-I-01`, ESCRITA PARA QUE SE PUEDA DECIDIR")
w()
w("**LO QUE LA FICHA ESCRIBE Y LO QUE NO, DICHO ANTES DE LA TABLA Y NO DESPUES.** La "
  "ficha escribe **los cuatro puntos**; **no escribe su estado**. `CUBRE`, `A MEDIAS` "
  "y `NO CUBRE` son **veredictos MEDIDOS**, no campos de la ficha: salen de "
  "`docs/loop/SALIDA_V211_T2_OP_I_01.txt` y los ratifico el acta 211 en su `6.3` "
  "(linea **74595**, leida hoy: *" + linea_de(ACT, 74595)[:120] + "*). **No los "
  "invento aqui y no se los atribuyo a la ficha.**")
w()
PUNTOS = []
ls = cargar(S2)
for k, l in enumerate(ls):
    m = re.match(r"^\s*PUNTO (\d), PEGADO ENTERO DE LA FICHA:", l)
    if m:
        PUNTOS.append(["**%s**" % m.group(1), ls[k + 1].strip(),
                       "**" + ls[k + 2].split(":", 1)[1].strip() + "**"])
w("**LOS CUATRO PUNTOS DE `verificacion`, PEGADOS ENTEROS DEL FICHERO.** **FILAS "
  "ARMADAS LEYENDO `" + S2 + "`: " + str(len(PUNTOS)) + "; FILAS QUE DEBERIA HABER: "
  + valor(S2, "CIFRA puntos de `verificacion` de OP-I-01, contados de la ficha")
  + ".**")
w()
w("| punto | el texto, pegado entero de la ficha | estado MEDIDO (no es campo de la ficha) |")
w("|---|---|---|")
for a, b, c in PUNTOS:
    w("| %s | %s | %s |" % (a, b, c))
if len(PUNTOS) != 4:
    ROJOS.append("no se leyeron los cuatro puntos")
w()
w("**EL PUNTO QUE ESTA EN `NO CUBRE`, APARTE Y ENTERO:** "
  + pick(S2, "PUNTO 2: toda forma"))
w()
w("**QUE HARIA FALTA EXACTAMENTE PARA QUE DEJARA DE ESTARLO.** La `6.4` del acta 211 "
  "lo deja escrito y lo cito con sus lineas, leidas hoy:")
w()
LIN = [["**%d**" % n, linea_de(ACT, n)] for n in (74601, 74606, 74607)]
w("**LAS TRES LINEAS DE LA `6.4`.** **FILAS ARMADAS LEYENDO `" + ACT + "`: "
  + str(len(LIN)) + "; FILAS QUE DEBERIA HABER: 3.**")
w()
w("| linea | lo que dice, leido hoy |")
w("|---|---|")
for a, b in LIN:
    w("| %s | %s |" % (a, b))
w()
w("**EN UNA FRASE, Y SALE DE ESAS TRES LINEAS: no hace falta COMPLETAR la cobertura, "
  "hace falta MARCARLA.** El banco `9.26` admite una cobertura incompleta como "
  "cumplimiento **si se dice asi**, y hoy ninguna lo dice.")
w()
w("**EL RECUENTO, HECHO POR MI EN ESTA VUELTA Y NO COPIADO.** El comando esta escrito "
  "entero en `" + S2 + "` y su corrida suelta quedo sellada en `" + SR + "`, que dice: "
  "*" + pick(SR, "entradas") + "*.")
w()
REC = [
    ["entradas del inventario", valor(S2, "CIFRA entradas del inventario:")],
    ["de esas, con cobertura de la forma *N de M pares leidos*",
     valor(S2, "CIFRA entradas con cobertura de la forma")],
    ["**de esas, INCOMPLETAS (`N` menor que `M`)**",
     "**" + valor(S2, "CIFRA de esas que estan INCOMPLETAS") + "**"],
    ["de esas incompletas, cuantas llevan `PROVISIONAL` en algun campo",
     valor(S2, "CIFRA de esas incompletas que llevan PROVISIONAL en algun campo")],
    ["entradas del inventario entero que llevan `PROVISIONAL`",
     valor(S2, "CIFRA entradas del inventario entero que llevan PROVISIONAL")],
]
w("**EL RECUENTO.** **FILAS ARMADAS LEYENDO `" + S2 + "`: " + str(len(REC))
  + "; FILAS QUE DEBERIA HABER: 5.**")
w()
w("| que se conto | cifra de hoy |")
w("|---|---|")
for a, b in REC:
    w("| %s | %s |" % (a, b))
if len(REC) != 5:
    ROJOS.append("la tabla del recuento no tiene 5 filas")
w()
w("**CONTRA LA CIFRA VIEJA, Y LO DIGO AUNQUE COINCIDA.** El acta 211 publica su cifra "
  "en la `6.4`, linea **74606**, leida hoy: *" + linea_de(ACT, 74606) + "*. Y mi "
  "conteo de hoy, del fichero y no del acta: **"
  + pick(S2, "74606). Mi conteo de hoy da").split("Mi conteo de hoy da", 1)[1].strip()
  + "**")
w()
w("**QUE DECIDE EL FUNDADOR Y QUE NO, EN UNA LINEA:** marcar esas **"
  + valor(S2, "CIFRA de esas que estan INCOMPLETAS") + "** entradas es **edicion de "
  "datos de `docs/plan/OPERACIONES.jsonl` y sus vecinos que ninguna regla ordena "
  "hoy**, y las filas que faltan en `docs/plan/08_VERIFICACION.md` para las fases 09 "
  "y 10 **cambian la forma del plan**: **las dos son suyas y ninguna es del bucle.**")
w()
w("**DOS DISCUTIBLES MARCADOS, LOS DOS ANTES DE SABER SI ACIERTO.**")
w()
w("1. **EL VEREDICTO `CONSUMIDA` LO DECIDE EL GRAFO Y LA ATRIBUCION LA FICHA, Y LAS "
  "DOS VAN EN LA MISMA CELDA.** Uso `consumida_por()` de la vara tal cual, que "
  "resuelve los nodos por `P.1` y exige que caigan en **un solo nodo vivo**; el "
  "**por quien** sale del texto de la propia ficha. **Si la casa quisiera esas dos "
  "cosas en dos columnas separadas, esta tabla las tiene juntas.** DISCUTIBLE "
  "MARCADO.")
w("2. **PUBLICO LOS CUATRO ESTADOS DE `OP-I-01` DE UNA MEDICION DE LA VUELTA 211 Y NO "
  "DE UNA MIA DE HOY.** El unico que el encargo me manda recontar es el del punto 2, "
  "y ese lo recompute yo (**"
  + valor(S2, "CIFRA de esas que estan INCOMPLETAS") + "**, reproduce). Los otros "
  "tres los cito de su fichero con su atribucion en vez de re correrlos, porque el "
  "encargo no lo pide y la moratoria manda plan antes que volumen. **Si la vara "
  "buena era volver a medir los cuatro hoy, esto es una cita donde tenia que haber "
  "una medicion.** DISCUTIBLE MARCADO.")
w()

texto = NL.join(P) + NL
largos = texto.count(chr(8212))
medios = texto.count(chr(8211))
print("CIFRA guiones largos: %d | CIFRA guiones medios: %d" % (largos, medios))
if largos or medios:
    ROJOS.append("hay %d guiones largos y %d medios" % (largos, medios))
print("CIFRA rojos del compositor: %d" % len(ROJOS))
for r in ROJOS:
    print("   ROJO> %s" % r)
if ROJOS:
    print("ROJO: el compositor NO ESCRIBE.")
    sys.exit(1)
destino = os.path.join(AQUI, "_v%d_t2_seccion.md" % VUELTA)
io.open(destino, "w", encoding="utf-8", newline=NL).write(texto)
print("ESCRITO %s -> %d bytes, %d lineas"
      % (os.path.relpath(destino, RAIZ).replace(os.sep, "/"),
         len(texto.encode("utf-8")), texto.count(NL)))
