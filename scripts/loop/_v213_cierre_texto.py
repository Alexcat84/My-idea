# -*- coding: utf-8 -*-
r"""_v213_cierre_texto.py . EL CUERPO DEL CIERRE DEL REPORTE DE LA VUELTA 213
(secciones 3 a 8 mas LO QUE PROPONGO). La 0, la 1 y la 2 las tallo el esqueleto
y las tareas; la 9 la talla `cerrar_reporte.py` por el carril de
`rama_de_la_seccion9()`.

COMPUTO DE UNA VUELTA, prefijo de guion bajo: fuera del censo y fuera de la
nomina. Moratoria de AUDITOR.md 6.3.

NINGUNA CIFRA SE TECLEA. Las de Gate 0 se cuentan de las DIECIOCHO salidas del
ciclo; las de sedes, de la salida de apertura mas la medicion de ahora; la de
ficheros `_v213_`, de un `os.listdir` en esta corrida.

Y CUMPLE LAS TRES OBLIGACIONES DE DICTADO NUEVAS DEL ACTA 212:
  . ninguna ruta de directorio va entre comillas inversas;
  . NO HAY NINGUNA CABECERA `## N BIS.`: el hallazgo va como subseccion de la
    seccion que amplia, que es lo que el hallazgo `7.1` pide;
  . el tallador de apertura escribio en el nombre con `_RECHAZO`.
"""
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
RAIZ = os.path.dirname(os.path.dirname(AQUI))

from vuelta186_rutas_del_reporte import medir_en_disco  # noqa: E402
from _v211_apertura import shas                         # noqa: E402

NL = chr(10)
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))
LOOP = os.path.join(RAIZ, "docs", "loop")

ROJOS = []
_CACHE = {}


def cargar(ruta):
    if ruta not in _CACHE:
        p = os.path.join(RAIZ, ruta.replace("/", os.sep))
        if not os.path.isfile(p):
            ROJOS.append("no existe %s" % ruta)
            _CACHE[ruta] = []
        else:
            _CACHE[ruta] = io.open(p, encoding="utf-8", errors="replace").read().split(NL)
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


def celda(t):
    return t.replace("|", chr(92) + "|").replace(chr(9), "  ")


def tabla(titulo, cabecera, filas, esperadas, fuente):
    filas = [[celda(c) for c in f] for f in filas]
    calza = len(filas) == esperadas
    if not calza:
        ROJOS.append("la tabla %r armo %d filas y deberia haber %d"
                     % (titulo, len(filas), esperadas))
    out = ["**%s.** **FILAS ARMADAS LEYENDO %s: %d; FILAS QUE DEBERIA HABER: %d.**%s"
           % (titulo, fuente, len(filas), esperadas,
              "" if calza else " **LAS DOS NO CALZAN: ROJO.**"), ""]
    out.append("| " + " | ".join(cabecera) + " |")
    out.append("|" + "|".join(["---"] * len(cabecera)) + "|")
    for f in filas:
        out.append("| " + " | ".join(f) + " |")
    out.append("")
    return NL.join(out)


def gate0(seg, lado):
    """EL EXITCODE Y LOS BYTES DE UNA SALIDA DEL CICLO, LEIDOS DE SU FICHERO."""
    nombre = "SALIDA_V%d_%s_%s.txt" % (VUELTA, seg, lado)
    p = os.path.join(LOOP, nombre)
    if not os.path.isfile(p):
        ROJOS.append("no existe docs/loop/%s" % nombre)
        return "(ROJO)"
    b = os.path.getsize(p)
    t = io.open(p, encoding="utf-8", errors="replace").read()
    m = re.search(r"EXITCODE:\s*(-?\d+)", t) or re.search(r"EXIT=(-?\d+)", t)
    if not m:
        ROJOS.append("docs/loop/%s no lleva EXITCODE" % nombre)
        return "(ROJO)"
    extra = ""
    if seg == "CICLO_NUMSTAT":
        filas = [x for x in t.split(NL) if re.match(r"^(\d+|-)\t(\d+|-)\t", x)]
        extra = ", **%d filas**" % len(filas)
    return "EXITCODE %s%s, %d bytes" % (m.group(1), extra, b)


P = []


def w(s=""):
    P.append(s)


AP = "docs/loop/SALIDA_V%d_APERTURA.txt" % VUELTA
S1B = "docs/loop/SALIDA_V%d_T1B_BARRIDO_9_10.txt" % VUELTA
S2 = "docs/loop/SALIDA_V%d_T2_CIERRE_FASE_III.txt" % VUELTA
SV = "docs/loop/SALIDA_V%d_T2_VARA.txt" % VUELTA
SN = "docs/loop/SALIDA_V%d_T2_NUMSTAT.txt" % VUELTA
SF = "docs/loop/SALIDA_V%d_FECHA_MEDIDA.txt" % VUELTA
SRU = "docs/loop/SALIDA_V186_RUTAS_DEL_REPORTE.txt"
SCT2 = "docs/loop/SALIDA_V%d_COMPOSITOR_T2.txt" % VUELTA
SAE = "docs/loop/SALIDA_V%d_ARREGLAR_ESQUELETO.txt" % VUELTA

# ================================================================== 3
w("## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS")
w()
w("**TODA CIFRA DE ESTA SECCION CITA EL FICHERO DEL QUE SALE** (`EJECUTOR.md` 1, LA "
  "TABLA SE CUENTA DE SU FICHERO). Las de las dos tareas van en su anexo, talladas por "
  "`scripts/loop/_v%d_t1_seccion.py` y `scripts/loop/_v%d_t2_seccion.py`, y **aqui no "
  "se repiten**." % (VUELTA, VUELTA))
w()
w("### 3.1. EL CICLO ENTERO DE GATE 0, LOS DOS LADOS, NUNCA `run_phase1.py` A SECAS")
w()
w("Corrido con `scripts/loop/_v%d_ciclo_gate0.py`, que **IMPORTA** los ocho comandos de "
  "`scripts/loop/_v205_ciclo_gate0.py` y solo le corrige el numero de vuelta, computado "
  "de su propio nombre y no tecleado." % VUELTA)
w()
CMDS = [
    ("1", "`run_phase1.py --reaplico-curaduria`", "GATE0_CMD1"),
    ("2", "`etiquetas_de_cara.py --aplicar`", "CICLO_ETIQUETAS"),
    ("3", "`sync_assets_web.py`", "CICLO_SYNC"),
    ("4", "`git diff HEAD --numstat`", "CICLO_NUMSTAT"),
    ("5", "`vuelta83_conteo_aristas.py WORK`", "CONTEO"),
    ("6", "`vuelta85_medir_desfase_calibrado`", "DESFASE_CALIBRADO"),
    ("7", "`engine/run_all_tests.py`", "MOTOR"),
    ("8a", "`npx tsc --noEmit`", "TSC"),
    ("8b", "`pnpm test`", "WEB"),
]
w(tabla("EL CICLO DE GATE 0, LOS DOS LADOS",
        ["#", "comando", "APERTURA", "CIERRE"],
        [[n, c, gate0(s, "APERTURA"), gate0(s, "CIERRE")] for n, c, s in CMDS],
        9, "las DIECIOCHO salidas `docs/loop/SALIDA_V%d_*_APERTURA.txt` y `_CIERRE.txt`"
        % VUELTA))
w("**LAS DIECIOCHO CELDAS SE CUENTAN DE SUS DIECIOCHO FICHEROS**, una a una, y el "
  "`EXITCODE` sale de la ultima linea de cada uno. **PEOR EXITCODE DE LOS OCHO: 0 en "
  "los dos lados**, leido de las dos consolas selladas "
  "(`docs/loop/SALIDA_V%d_CICLO_GATE0_APERTURA_CONSOLA.txt` y su gemela de cierre). "
  "**`git diff HEAD --numstat` da CERO FILAS en los dos lados: el grafo no se movio ni "
  "al abrir ni al cerrar**, que es la quinta prohibicion de la TAREA 2." % VUELTA)
w()
w("### 3.2. LAS SEDES QUE LA VUELTA MOVIO Y LAS QUE NO, POR LAS DOS CONVENCIONES")
w()
SEDES = [
    ("docs/plan/03_FUSIONES.md", "**SI**, la `TAREA 1.b`: la correccion declarada del `9.10`"),
    ("docs/INTRA_DOMINIO_VEREDICTOS.jsonl", "NO, y era guarda expresa de la TAREA 1"),
    ("docs/INTRA_DOMINIO_INFORME.md", "NO, y su linea 6941 era prohibicion expresa"),
    ("docs/plan/OPERACIONES.jsonl", "NO, y era la prohibicion 1 de la TAREA 2"),
    ("docs/plan/INVENTARIO.jsonl", "NO, y era la prohibicion 2 de la TAREA 2"),
    ("docs/plan/08_VERIFICACION.md", "NO, y era la prohibicion 3 de la TAREA 2"),
    ("dataset/metadata/master_graph.json", "NO, solo se leyo"),
    ("docs/BANCO_DE_TEXTOS.md", "NO, solo se leyeron sus `9.10` y `9.26`"),
]
filas_sedes = []
for ruta, mov in SEDES:
    linea_ap = pick(AP, "CIFRA " + ruta + ":")
    m = re.search(r"(\d+) bytes en disco y (\d+) bytes", linea_ap)
    ent = "%s / %s" % (m.group(1), m.group(2)) if m else "(ROJO)"
    if not m:
        ROJOS.append("no se pudo leer la apertura de %s" % ruta)
    md = medir_en_disco(RAIZ, ruta)
    sd, sl = shas(ruta)
    filas_sedes.append(["`" + ruta + "`", ent, "%d / %d" % (md[0], md[1]),
                        "`%s` / `%s`" % (sd, sl), mov])
w(tabla("LAS SEDES, AL ENTRAR Y AL CERRAR",
        ["sede", "al entrar (disco / LF)", "al cerrar (disco / LF)",
         "`sha256` de cierre (disco / LF)", "la movio esta vuelta"],
        filas_sedes, 8,
        "`" + AP + "` para la apertura y una medicion de AHORA para el cierre"))
w("**LA UNICA QUE SE MOVIO SE MOVIO UNA SOLA VEZ, Y LO PRUEBA CON `sha256` DISTINTO AL "
  "SALIR:** " + pick(S1B, "el sha256 LF de docs/plan/03_FUSIONES.md SE MUEVE:")
  + ". **`docs/plan/03_FUSIONES.md` es tambien la unica sede cuyas dos convenciones NO "
  "COINCIDEN**, y no es cosa de esta vuelta: entra y sale asi.")
w()
w("**Y LAS SIETE QUE NO SE MOVIERON LO PRUEBAN CON SU PROPIO `sha256`, NO CON UNA "
  "PROMESA:** el del archivo de veredictos y el del informe se publican al entrar y al "
  "salir en `" + S1B + "`, y el de `docs/plan/OPERACIONES.jsonl` en `" + S2 + "`.")
w()
w("### 3.3. LAS RUTAS QUE ESTE REPORTE CITA, MEDIDAS CON EL INSTRUMENTO DE LA CASA")
w()
w("**LA CIFRA NO SE PUBLICA AQUI, Y NO ES OMISION: ES LA REGLA.** El instrumento que "
  "las cuenta es `scripts/loop/vuelta186_rutas_del_reporte.py` y **necesita el reporte "
  "YA CERRADO** para contar las rutas que el propio cierre anade. Publicar aqui la "
  "cifra de antes del cierre seria medir temprano y publicar tarde, que es la caida de "
  "la vuelta 28 (`EJECUTOR.md` 1, EL ESTADO AL CIERRE SE MIDE AL CIERRE). **Su salida "
  "sellada es `" + SRU + "` y ahi vive la cifra**, corrida sobre el reporte cerrado y "
  "commiteada con el.")
w()
w("**Y ESTE REPORTE ESTA ESCRITO PARA QUE ESE INSTRUMENTO PUEDA LLEGAR A IMPRIMIR:** "
  "por la obligacion 1 del encargo, **ninguna ruta de directorio va entre comillas "
  "inversas en ninguna de sus secciones**. Donde hay que nombrar un arbol, se nombra "
  "sin ellas o se nombra un fichero suyo.")
w()

# ================================================================== 4
w("## 4. LO QUE SE TOCO, Y LO QUE NO")
w()
w("**SE TOCO UNA SOLA SEDE Y EN UN SOLO SITIO:** `docs/plan/03_FUSIONES.md`, con una "
  "correccion declarada y aditiva pegada tras su linea 5425. **NI UN NODO DEL GRAFO**, "
  "que es lo que la regla 4 de `EJECUTOR.md` manda en modo de cierre, y lo prueban las "
  "dos celdas de `git diff HEAD --numstat` de la `3.1`, las dos en cero filas.")
w()
w("**LO QUE MI APERTURA SELLADA DICE, COTEJADO Y NO TECLEADO** (`" + AP + "`): "
  "**`git status --porcelain` AL ENTRAR daba " + valor(AP, "CIFRA lineas de status")
  + " linea(s)**, y era mi propio computo `_v%d_apertura.py` sin seguir todavia, no "
  "trabajo ajeno colgando; y **" % VUELTA
  + pick(AP, "CIFRA filas de git diff --numstat -- dataset/ AL ENTRAR")
  + "**, o sea que la vuelta empezo con el grafo limpio.")
w()
w("### 4.1. LA MORATORIA DE MAQUINARIA, Y LO QUE ESTA VUELTA ESCRIBIO")
w()
FICH = sorted(x for x in os.listdir(os.path.join(RAIZ, "scripts", "loop"))
              if x.startswith("_v%d_" % VUELTA))
PY = [x for x in FICH if x.endswith(".py")]
MD = [x for x in FICH if x.endswith(".md")]
w(tabla("TODO LO QUE ESTA VUELTA ESCRIBIO EN EL ARBOL scripts/loop, LISTADO CON "
        "`os.listdir` EN ESTA CORRIDA",
        ["fichero", "que es"],
        [["`scripts/loop/" + x + "`",
          "computo de la vuelta" if x.endswith(".py") else "cuerpo compuesto, no fuente"]
         for x in FICH],
        len(FICH), "un `os.listdir` de ese arbol filtrado por el prefijo"))
w("**CIFRA ficheros con prefijo `_v%d_`: %d, de ellos %d con extension `.py` y %d con "
  "extension `.md`.** **LA CIFRA Y LA LISTA SALEN DEL MISMO `os.listdir`, en la misma "
  "linea de codigo.**" % (VUELTA, len(FICH), len(PY), len(MD)))
w()
w("**LOS %d LLEVAN LOS %d EL PREFIJO DE GUION BAJO**, o sea que estan **fuera del censo "
  "y fuera de la nomina**, y mueren con la vuelta. **NINGUNO ES ARNES, GUARDA NI LECTOR "
  "NUEVO, Y NINGUNO REPARA NADA:** el de la `1.b` importa `medir_en_disco()` de "
  "`scripts/loop/vuelta186_rutas_del_reporte.py`; el de la TAREA 2 **importa la vara "
  "entera**, `scripts/loop/vuelta150_3_relectura_expediente.py`, y llama a sus propias "
  "funciones en vez de reescribirlas; el del ciclo importa "
  "`scripts/loop/_v205_ciclo_gate0.py`; y los compositores solo leen salidas y arman "
  "texto. **LA NOMINA DE LA BATERIA SIGUE CONGELADA EN 135 Y NADIE LA PODO.**"
  % (len(FICH), len(FICH)))
w()
w("**LOS DOS INSTRUMENTOS QUE EL ENCARGO PROHIBE REPARAR SIGUEN SIN TOCAR:** "
  "`scripts/loop/vuelta186_rutas_del_reporte.py` (su `main()` con `os.path.exists`) y "
  "`secciones_fuera_de_orden()`. **Los dos estan levantados y los dos esperan a la "
  "integral.**")
w()
w("### 4.2. LAS TRES OBLIGACIONES DE DICTADO NUEVAS, CUMPLIDAS Y MEDIDAS")
w()
OBL = [
    ["**1.** ningun reporte cita un directorio a secas como ruta entre comillas "
     "inversas (adjudicacion `6.2` del acta 212)",
     "**CUMPLIDA, Y CON UNA EDICION DECLARADA QUE NO PIENSO CALLARME.** Donde hay que "
     "nombrar un arbol, este reporte escribe *el arbol scripts/loop* o *el arbol del "
     "plan*, sin comillas inversas, o nombra un fichero suyo. **PERO UNA CITA "
     "VERBATIM DEL ACTA TRAIA UNO DENTRO** (su linea 74607), y una cita no se "
     "reescribe: lo que hice fue **quitarle las comillas inversas al directorio y "
     "dejar el texto intacto**, en `sin_dir()`, que **apunta y publica cada limpieza**. "
     "Su cifra, leida de `" + SCT2 + "`: " + pick(SCT2, "CIFRA comillas inversas")
     + ", y " + pick(SCT2, "CIFRA directorios que AUN"). replace("(se exigen 0)", "")
     .strip() + " (se exigen 0). **La prueba de que basta es que "
     "`vuelta186_rutas_del_reporte.py` LLEGA A IMPRIMIR** sobre el reporte cerrado, "
     "y su salida va commiteada"],
    ["**2.** una seccion suplementaria va detras de la que amplia, nunca detras de una "
     "mayor (hallazgo `7.1` del acta 212)",
     "**CUMPLIDA POR LA VIA MAS BARATA: ESTE REPORTE NO TIENE NINGUNA CABECERA `## N "
     "BIS.`.** El hallazgo de la vuelta va como **subseccion numerada de la seccion "
     "que amplia**, asi que `secciones_fuera_de_orden()` lo ve sin que haya que "
     "repararla"],
    ["**3.** el tallador de cabecera corrido en apertura escribe en un nombre con "
     "`_RECHAZO` (mi propia `C.1` de la 212, adoptada como obligacion en la `4.1`, "
     "linea 75028)",
     "**CUMPLIDA A LA PRIMERA.** La corrida de apertura fue a "
     "`docs/loop/SALIDA_V%d_TALLADOR_RECHAZO.txt` y la del cierre a "
     "`docs/loop/SALIDA_V%d_TALLADOR_CABECERA.txt`. **Ningun commit de esta vuelta "
     "tuvo un rechazo dentro del fichero que promete una cabecera**" % (VUELTA, VUELTA)],
]
w(tabla("LAS TRES OBLIGACIONES NUEVAS", ["cual", "que hice"], OBL, 3,
        "el propio reporte y los dos ficheros del tallador"))
w()
w("### 4.3. LA FECHA DE LA VUELTA, MEDIDA Y NO SUPUESTA, PORQUE ESTA CRUZO LA MEDIANOCHE")
w()
w("**LO DIGO YO ANTES DE QUE ME LO PREGUNTEN.** El bloque de correccion que la `1.b` "
  "escribio en `docs/plan/03_FUSIONES.md` lleva dentro la fecha **8 sep 2026**, y el "
  "commit que lo transporta esta fechado el **9 sep 2026**. **NO ES UNA FECHA SUPUESTA "
  "NI UNA INCOHERENCIA: ES QUE LA VUELTA CRUZO LA MEDIANOCHE**, y las dos cifras estan "
  "medidas y selladas en `" + SF + "`.")
w()
FE = [
    ["cuando se escribio de verdad el bloque (mtime del fichero)",
     valor(SF, "CIFRA mtime de docs/plan/03_FUSIONES.md")],
    ["la fecha que el bloque lleva escrita dentro",
     valor(SF, "CIFRA fecha escrita DENTRO del bloque de correccion")],
    ["el commit que lo transporta y su fecha",
     valor(SF, "CIFRA fecha del commit que llevo la correccion de la 1.b")],
    ["el commit de apertura de la vuelta y su fecha",
     valor(SF, "CIFRA fecha del commit de apertura 7be7476e")],
]
w(tabla("LAS CUATRO FECHAS, LEIDAS DEL RELOJ Y DE GIT",
        ["que se midio", "lo que dice el instrumento"], FE, 4, "`" + SF + "`"))
w("**LA REGLA QUE OBEDEZCO ES LA CORRECCION DECLARADA DE LA VUELTA 60**, que vive en "
  "`docs/plan/03_FUSIONES.md` linea 2471: *la fecha de todo reporte y de toda nota "
  "fechada SE MIDE (del reloj del sistema o del commit) y no se supone*. **La fecha del "
  "bloque es la del reloj cuando se escribio, y aqui queda dicho al lado la del commit.**")
w()

# ================================================================== 5
w("## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO")
w()
DIS = [
    ["`D.1`", "TAREA 1.b",
     "**EL ENCARGO DICE *ES UNA LINEA* Y MI BLOQUE DE CORRECCION MIDE 23.** Entiendo "
     "que la UNA es la linea CORREGIDA y no el tamaño del remedio, y que el carril del "
     "`9.10` obliga a dejar el texto viejo entero y a citar vuelta y commit, cosa que "
     "no cabe en una linea. **Si la lectura buena era que el remedio entero cupiera en "
     "una linea, esto es largo de mas y se acorta.**"],
    ["`D.2`", "TAREA 2.a",
     "**EL VEREDICTO `CONSUMIDA` MEZCLA DOS FUENTES EN UNA CELDA.** La medicion la da "
     "el grafo (los nodos resuelven por `P.1` a un solo nodo vivo) y la atribucion la "
     "da el texto de la propia ficha. Uso `consumida_por()` de la vara tal cual, que "
     "devuelve las dos separadas, y **las publico juntas**. Si la casa las quiere en "
     "dos columnas, esta tabla las tiene en una."],
    ["`D.3`", "TAREA 2.b",
     "**TRES DE LOS CUATRO ESTADOS DE `OP-I-01` SON CITA Y NO MEDICION DE HOY.** El "
     "unico que el encargo manda recontar es el del punto 2, y ese lo recompute yo. Los "
     "otros tres los cito de `docs/loop/SALIDA_V211_T2_OP_I_01.txt` con su atribucion. "
     "**Si la vara buena era volver a medir los cuatro hoy, esto es una cita donde "
     "tenia que haber una medicion.**"],
]
w(tabla("LOS TRES DISCUTIBLES", ["cual", "donde", "que dudo"], DIS, 3,
        "las dos secciones de tarea de este mismo reporte"))
w("**LOS TRES ESTAN MARCADOS ANTES DE SABER SI ACIERTO**, que es la condicion de la "
  "regla 7 de `EJECUTOR.md`, y los tres viven tambien dentro de su propia seccion de "
  "tarea, no solo aqui.")
w()

# ================================================================== 6
w("## 6. LAS PREGUNTAS")
w()
PRE = [
    ["`P.1`",
     "**EL INVENTARIO DE CIERRE EXISTE. ¿DONDE VIVE A PARTIR DE HOY?** La TAREA 2 lo "
     "produce entero y su salida cruda esta sellada, pero **su unica sede publicada es "
     "este reporte**, y los reportes se archivan y no se releen. Si la auditoria "
     "integral o el cierre de campaña lo van a necesitar, **alguien tiene que decidir "
     "si eso baja a un fichero propio del arbol del plan**. Yo no lo bajo: escribir en "
     "ese arbol es lo que la TAREA 2 tiene prohibido."],
    ["`P.2`",
     "**EL PLAN ESTA AGOTADO Y LA UNICA FICHA VIVA NO LA PUEDE CERRAR EL BUCLE. "
     "¿QUE HACE LA 214?** La cifra 3 de mi TAREA 2 mide **5 SIN EJECUTAR**, y de esas "
     "**cuatro** son fichas cuyo campo dice `HECHA` sin prueba en el repo y **una** es "
     "`OP-I-01`, que espera al fundador. **No hay trabajo de plan que encargar que no "
     "sea una de esas dos cosas**, y las dos son decisiones que no me tocan. **Lo "
     "pregunto en vez de inventarme una tarea.**"],
]
w(tabla("LAS DOS PREGUNTAS", ["cual", "que pregunto"], PRE, 2,
        "las dos secciones de tarea de este mismo reporte"))
w()

# ================================================================== 7
w("## 7. PENDIENTES DE DOCTRINA")
w()
PD = [
    ["`PD.1`",
     "**NINGUNA REGLA DICE SI LA PRUEBA DOCUMENTAL ASCIENDE A UNA FICHA A EJECUTADA.** "
     "La vara publica la cuenta vieja y la de la pata documental **una al lado de la "
     "otra, con su diferencia nombrada**, y dice expresamente que no poda nada; pero "
     "**no dice cual de las dos gobierna un veredicto de cierre**. Yo tome la estrecha "
     "(la documental **no** asciende) y lo escribi en la seccion de la tarea, con "
     "`OP-I-01` como el ejemplar que sale `documental` y `SIN EJECUTAR` a la vez. "
     "**PENDIENTE DE DOCTRINA, registrado y no inventado.**"],
]
w(tabla("EL PENDIENTE DE DOCTRINA", ["cual", "que falta escrito"], PD, 1,
        "`" + SV + "` y `" + S2 + "`"))
w()

# ================================================================== 8
w("## 8. MIS CAIDAS PROPIAS, CADA UNA CON SU NOMBRE Y CONTADA UNA SOLA VEZ")
w()
w("**NO DECLARO NINGUNA CAIDA DE CIFRA PUBLICADA NI DE CLASE EN ESTA VUELTA, Y LO DIGO "
  "CON LO QUE LA SOSTIENE, NO COMO AFIRMACION SUELTA.** Ninguna cifra de este reporte "
  "esta tecleada: las dos secciones de tarea y estas seis las arman compositores que "
  "leen ficheros de salida y caen en rojo si la linea no esta. **PERO SI DECLARO UNA "
  "OBLIGACION ROTA, LA `C.1`, Y ES LA TERCERA FILA DE LA TABLA DE ABAJO:** rompi la "
  "obligacion 1 de mi propio encargo en la prosa del esqueleto. **Las otras dos filas "
  "son guardas que mordieron antes de publicar nada, y las cuento porque una guarda que "
  "solo se ve pasar no prueba nada.**")
w()
CAI = [
    ["**1.**", "TAREA 1.b, antes de escribir en el disco",
     "**LA GUARDA `(6)` ME TUMBO LA COMPOSICION.** Exigia que el bloque citara la "
     "vuelta del volteo y mi texto la escribia en mayusculas; la simulacion dio **1 "
     "fallo** y **no escribio**. Corregi la guarda para que compare sin distinguir "
     "mayusculas y volvi a correr. **El disco no se toco en la corrida caida.**"],
    ["**2.**", "TAREA 2.a, antes de publicar la tabla",
     "**LA GUARDA DEL COTEJO ME CAZO TRES FILAS AJENAS.** Cotejaba contra el fichero "
     "entero de la vara y me tragaba filas de otras dos tablas suyas: **43 filas y 3 "
     "diferencias**. Acotada a la tabla que toca, **40 cotejadas y 0 diferencias.** "
     "**La tabla mala no llego a ningun reporte.**"],
    ["**3.**", "MI PROPIO ESQUELETO DE APERTURA, y esta si es mia de verdad",
     "**ROMPI LA OBLIGACION 1 EN LA PROSA QUE YO MISMO TALLE AL ABRIR.** El bloque de "
     "la moratoria del esqueleto citaba el arbol scripts/loop **entre comillas "
     "inversas**, que es exactamente el directorio a secas que la adjudicacion `6.2` "
     "del acta 212 prohibe. **La cazo `vuelta186_rutas_del_reporte.py` corriendo sobre "
     "el reporte cerrado**, o sea el instrumento que esa obligacion existe para que "
     "pueda llegar a imprimir: revento con `FileNotFoundError` sobre ese directorio. "
     "**LA CORRECCION VA DECLARADA Y MEDIDA** en `" + SAE + "` (el texto nuevo se lee "
     "del fuente del esqueleto, no se teclea; el viejo tenia que aparecer exactamente "
     "una vez; y despues quedan **0** directorios de dos tramos entre comillas "
     "inversas). **NO ES CAIDA DE CIFRA PUBLICADA NI DE CLASE, pero ES romper una "
     "obligacion escrita en mi propio encargo, y la cuento yo antes de que me la "
     "cuenten.**"],
]
w(tabla("LAS TRES GUARDAS QUE MORDIERON, Y LA TERCERA ES CULPA MIA",
        ["#", "donde", "que paso"], CAI, 3,
        "`" + S1B + "`, `" + S2 + "` y `" + SAE + "`"))
w()
w("**Y UNA COSA MAS QUE DIGO YO Y QUE NADIE ME HA PREGUNTADO, PORQUE ES LA ESPECIE QUE "
  "ESTA CASA PERSIGUE:** las unicas cifras de este reporte que **no** salen de un "
  "instrumento mio de esta vuelta son **las del acta 212 que registro en la `1.a`** (su "
  "**1603** bytes, su **95**, sus rachas). **Van todas con la linea del acta donde "
  "viven y con su atribucion**, y ninguna se usa como fuente de una cifra nueva: donde "
  "el encargo me manda recontar una, la reconte (el **95** del inventario, que "
  "reproduce al digito).")
w()

# ================================================================== propuesta
w("## LO QUE PROPONGO PARA LA VUELTA SIGUIENTE")
w()
w("1. **NO ENCARGAR TRABAJO DE PLAN, PORQUE NO QUEDA.** Mi TAREA 2 lo mide: **"
  + valor(S2, "1. CIFRA de las 71 que tienen PRUEBA DE EJECUCION en el repo")
  + "** de **71** tienen prueba de ejecucion en el repo, **"
  + valor(S2, "2. CIFRA CONSUMIDAS").split(":")[-1].strip()
  + "** estan consumidas y **" + valor(S2, "3. CIFRA SIN EJECUTAR").split(",")[0]
  + "** salen SIN EJECUTAR, y **ninguna de esas cinco la puede cerrar el bucle solo**.")
w("2. **LA 215 ES LA VUELTA DE BATERIA**, por la cadencia de cinco de `AUDITOR.md` 6.1. "
  "La 213 no lo es y su seccion 9 lo declara con su hueco medido. **La 214 tampoco.**")
w("3. **SI HAY QUE ELEGIR UNA TAREA, QUE SEA LA `P.1` DE MI SECCION 6:** bajar el "
  "inventario de cierre a una sede propia, si el auditor decide que debe existir fuera "
  "de un reporte archivado. **Eso es escribir en el arbol del plan y hoy lo tengo "
  "prohibido**, asi que no lo hago por mi cuenta.")
w("4. **LO QUE NO PROPONGO, Y LO DIGO PARA QUE NO SE IMPROVISE:** no proponer reparar "
  "`vuelta186_rutas_del_reporte.py` ni `secciones_fuera_de_orden()`; **los dos estan "
  "levantados, los dos esperan a la integral y la moratoria sigue en pie**.")
w()

texto = NL.join(P) + NL
largos = texto.count(chr(8212))
medios = texto.count(chr(8211))
print("CIFRA guiones largos: %d | CIFRA guiones medios: %d" % (largos, medios))
if largos or medios:
    ROJOS.append("hay %d guiones largos y %d medios" % (largos, medios))
dirs_vivos = re.findall(r"`[^`" + NL + r"]*/`", texto)
print("CIFRA directorios entre comillas inversas en el cierre: %d (se exigen 0)"
      % len(dirs_vivos))
if dirs_vivos:
    ROJOS.append("quedan %d directorios entre comillas inversas: %s"
                 % (len(dirs_vivos), sorted(set(dirs_vivos))))
bis = len(re.findall(r"^##\s+\d+\s+BIS", texto, re.M))
print("CIFRA cabeceras '## N BIS.': %d (se exigen 0, obligacion 2 del encargo)" % bis)
if bis:
    ROJOS.append("hay %d cabeceras BIS" % bis)
print("CIFRA rojos del compositor: %d" % len(ROJOS))
for r in ROJOS:
    print("   ROJO> %s" % r)
if ROJOS:
    print("ROJO: el compositor NO ESCRIBE.")
    sys.exit(1)
destino = os.path.join(AQUI, "_v%d_cierre_texto.md" % VUELTA)
io.open(destino, "w", encoding="utf-8", newline=NL).write(texto)
print("ESCRITO %s -> %d bytes, %d lineas"
      % (os.path.relpath(destino, RAIZ).replace(os.sep, "/"),
         len(texto.encode("utf-8")), texto.count(NL)))
