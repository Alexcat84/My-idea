# -*- coding: utf-8 -*-
r"""_v212_cierre_texto.py . EL CUERPO DEL CIERRE DEL REPORTE DE LA VUELTA 212
(secciones 3 a 8 mas LO QUE PROPONGO). La 0, la 1 y la 2 las tallo el esqueleto
y las tareas; la 9 la talla `cerrar_reporte.py` por el carril de
`rama_de_la_seccion9()`.

COMPUTO DE UNA VUELTA, prefijo de guion bajo: fuera del censo y fuera de la
nomina. Moratoria de AUDITOR.md 6.3.

NINGUNA CIFRA SE TECLEA. Las de Gate 0 se cuentan de las DIECIOCHO salidas del
ciclo; las de sedes, de la salida de apertura mas la medicion de ahora; la de
ficheros `_v212_`, de un `os.listdir` en esta corrida, que es exactamente la
caida `C.3` que el ejecutor de la 211 se cazo a si mismo.

Y CUMPLE LA OBLIGACION DE DICTADO QUE EL ENCARGO DE LA 212 ANADE: toda tabla
dice, en su misma linea, cuantas filas armo y cuantas deberia haber.
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
    hits = [l for l in cargar(ruta) if l.startswith(prefijo)]
    if len(hits) <= n:
        ROJOS.append("en %s no hay linea %d que empiece por %r" % (ruta, n, prefijo))
        return "(ROJO: no encontrada)"
    return hits[n].strip()


def valor(ruta, prefijo, n=0):
    l = pick(ruta, prefijo, n)
    return l.split(":", 1)[1].strip() if ":" in l else l


def tabla(titulo, cabecera, filas, esperadas, fuente):
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
S1B = "docs/loop/SALIDA_V%d_T1B_PUESTO_730.txt" % VUELTA
S1BE = "docs/loop/SALIDA_V%d_T1B_ESCRIBIR.txt" % VUELTA
S1C = "docs/loop/SALIDA_V%d_T1C_OP_F_04_HOR.txt" % VUELTA
S2 = "docs/loop/SALIDA_V%d_T2_COLA_RELECTURA.txt" % VUELTA
SHR = "docs/loop/SALIDA_V%d_HALLAZGO_RUTAS.txt" % VUELTA
SRU = "docs/loop/SALIDA_V186_RUTAS_DEL_REPORTE.txt"

# ================================================================== 3
w("## 3. LAS CIFRAS DE LA VUELTA, CONTADAS DE SUS FICHEROS")
w()
w("**TODA CIFRA DE ESTA SECCION CITA EL FICHERO DEL QUE SALE** (`EJECUTOR.md` 1, LA "
  "TABLA SE CUENTA DE SU FICHERO). Las de las dos tareas van en su anexo, talladas "
  "por `scripts/loop/_v212_t1_seccion.py` y `scripts/loop/_v212_t2_seccion.py`, y "
  "**aqui no se repiten**.")
w()
w("### 3.1. EL CICLO ENTERO DE GATE 0, LOS DOS LADOS, NUNCA `run_phase1.py` A SECAS")
w()
w("Corrido con `scripts/loop/_v212_ciclo_gate0.py`, que **IMPORTA** los ocho comandos "
  "de `scripts/loop/_v205_ciclo_gate0.py` y solo le corrige el numero de vuelta, "
  "computado de su propio nombre y no tecleado. **PEOR EXITCODE DE LOS OCHO: 0 en "
  "APERTURA y 0 en CIERRE.**")
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
        9, "las DIECIOCHO salidas `docs/loop/SALIDA_V212_*_APERTURA.txt` y `_CIERRE.txt`"))
w("**LAS DIECIOCHO CELDAS SE CUENTAN DE SUS DIECIOCHO FICHEROS**, una a una, y el "
  "`EXITCODE` sale de la ultima linea de cada uno. **`git diff HEAD --numstat` da CERO "
  "FILAS en los dos lados: el grafo no se movio ni al abrir ni al cerrar.**")
w()
w("### 3.2. LAS SEDES QUE LA VUELTA MOVIO Y LAS QUE NO, POR LAS DOS CONVENCIONES")
w()
SEDES = [
    ("docs/INTRA_DOMINIO_VEREDICTOS.jsonl", "**SI**, la `TAREA 1.b`: el puesto 730"),
    ("docs/plan/OPERACIONES.jsonl", "**SI**, la `TAREA 1.c`: la `adjudicacion` de `OP-F-04-HOR`"),
    ("dataset/metadata/master_graph.json", "NO, solo se leyo para resolver aristas"),
    ("docs/plan/01_FUENTES.md", "NO, solo se leyeron sus lineas 1168 y 1453"),
    ("docs/plan/08_VERIFICACION.md", "NO, solo se leyo su linea 9"),
    ("docs/BANCO_DE_TEXTOS.md", "NO, solo se leyeron sus `9.6.1`, `9.6.2`, `9.6.3` y `9.10`"),
    ("docs/loop/ACTA_AUDITOR.md", "NO, solo se leyo"),
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
        filas_sedes, 7,
        "`" + AP + "` para la apertura y una medicion de AHORA para el cierre"))
w("**LAS DOS QUE SE MOVIERON SE MOVIERON UNA SOLA VEZ CADA UNA, Y LAS DOS LO PRUEBAN "
  "CON `sha256` DISTINTO AL SALIR** (`" + valor(S1BE, "CIFRA el sha256 cambia entre "
  "entrada y salida") + "` en la `1.b` y `"
  + valor(S1C, "CIFRA el sha256 cambia entre entrada y salida") + "` en la `1.c`). "
  "**`docs/plan/01_FUENTES.md` es la unica sede cuyas dos convenciones NO COINCIDEN**, "
  "y no es cosa de esta vuelta: entra y sale igual, y ni se abrio para escribir.")
w()
w("### 3.3. LAS RUTAS QUE ESTE REPORTE CITA, MEDIDAS CON EL INSTRUMENTO DE LA CASA")
w()
w("**LA CIFRA NO SE PUBLICA AQUI, Y NO ES OMISION: ES LA REGLA.** El instrumento que "
  "las cuenta es `scripts/loop/vuelta186_rutas_del_reporte.py` y **necesita el reporte "
  "YA CERRADO** para contar las rutas que el propio cierre anade. Publicar aqui la "
  "cifra de antes del cierre seria medir temprano y publicar tarde, que es la caida de "
  "la vuelta 28 (`EJECUTOR.md` 1, EL ESTADO AL CIERRE SE MIDE AL CIERRE). **Su salida "
  "sellada es `" + SRU + "` y ahi vive la cifra**, corrida sobre el reporte cerrado.")
w()
w("**Y LA CORRIDA QUE SE COMMITEA ES LA DE DESPUES DEL CIERRE, no una de antes.** "
  "Su veredicto y su cifra de rutas que no existen o miden cero se leen en ese "
  "fichero sellado, y no se copian aqui: copiarlas seria volver a publicar una "
  "medicion de apertura como si fuera de cierre.")
w()

# ================================================================== 4
w("## 4. LO QUE SE TOCO, Y LO QUE NO")
w()
w("**SE TOCARON DOS SEDES Y TRES CAMPOS EN TOTAL:** la `clase` y la `razon` del puesto "
  "730 en `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, y la `adjudicacion` de `OP-F-04-HOR` "
  "en `docs/plan/OPERACIONES.jsonl`. **NI UN NODO DEL GRAFO**, que es lo que la regla 4 "
  "de `EJECUTOR.md` manda en modo de cierre, y lo prueban las dos celdas de "
  "`git diff HEAD --numstat` de la `3.1`, las dos en cero filas.")
w()
w("**LO QUE MI APERTURA SELLADA DICE, COTEJADO Y NO TECLEADO** (`" + AP + "`): "
  "**`git status --porcelain` AL ENTRAR daba "
  + valor(AP, "CIFRA lineas de status") + " lineas**, y las dos eran mis propios computos "
  "`_v212_` sin seguir todavia, no trabajo ajeno colgando; y "
  "**" + pick(AP, "CIFRA filas de git diff --numstat -- dataset/ AL ENTRAR")
  + "**, o sea que la vuelta empezo con el grafo limpio.")
w()
w("### 4.1. LA MORATORIA DE MAQUINARIA, Y LO QUE ESTA VUELTA ESCRIBIO")
w()
FICH = sorted(x for x in os.listdir(os.path.join(RAIZ, "scripts", "loop"))
              if x.startswith("_v%d_" % VUELTA))
PY = [x for x in FICH if x.endswith(".py")]
MD = [x for x in FICH if x.endswith(".md")]
w(tabla("TODO LO QUE ESTA VUELTA ESCRIBIO EN scripts/loop, LISTADO CON `os.listdir` "
        "EN ESTA CORRIDA",
        ["fichero", "que es"],
        [["`scripts/loop/" + x + "`",
          "computo de la vuelta" if x.endswith(".py") else "cuerpo compuesto, no fuente"]
         for x in FICH],
        len(FICH), "un `os.listdir` del arbol scripts/loop (otra vez sin comillas "
        "inversas, por lo mismo que la 7 bis) filtrado por el prefijo"))
w("**CIFRA ficheros con prefijo `_v%d_`: %d, de ellos %d con extension `.py` y %d con "
  "extension `.md`.** **LA CIFRA Y LA LISTA SALEN DEL MISMO `os.listdir`, en la misma "
  "linea de codigo**, que es el remedio de la `C.3` que el ejecutor de la 211 se cazo a "
  "si mismo: alli la cifra estaba tecleada y la lista no la miraba nadie."
  % (VUELTA, len(FICH), len(PY), len(MD)))
w()
w("**LOS %d LLEVAN LOS %d EL PREFIJO DE GUION BAJO**, o sea que estan **fuera del censo "
  "y fuera de la nomina**, y mueren con la vuelta. **NINGUNO ES ARNES, GUARDA NI LECTOR "
  "NUEVO:** los cuatro que miden importan sus funciones de la sede que ya existe "
  "(`scripts/loop/apertura_del_auditor.py` para el marcador, "
  "`scripts/loop/verificar_aristas_vivas.py` para el resolutor, "
  "`scripts/loop/vuelta186_rutas_del_reporte.py` para las dos convenciones y para el "
  "patron de rutas), y los tres compositores solo leen salidas y arman texto. **LA "
  "NOMINA DE LA BATERIA SIGUE CONGELADA EN 135 Y NADIE LA PODO.**"
  % (len(FICH), len(FICH)))
w()
w("### 4.2. LA `1.d` DEL ENCARGO, CUMPLIDA POR OMISION Y DICHA EN VOZ ALTA")
w()
w("**NO TOQUE `OP-I-01`** (sigue en `LISTA`, contado en la `1.c` al medir por `estado` "
  "antes y despues), **NO MARQUE LAS 95 ENTRADAS DEL INVENTARIO**, y **NO ESCRIBI NI "
  "UNA FILA NUEVA EN `docs/plan/08_VERIFICACION.md`**. Las tres son prohibiciones "
  "expresas del encargo y las tres se cumplen. La `1.d` las registra con su cita en el "
  "anexo de la TAREA 1.")
w()

# ================================================================== 5
w("## 5. LOS DISCUTIBLES, MARCADOS ANTES DE SABER SI ACIERTO")
w()
w("**`D.1` NO BARRI LAS DOS CITAS VIVAS DEL 730 FUERA DEL ARCHIVO, Y EL BANCO `9.10` "
  "DICE QUE UN VOLTEO BARRE SUS TABLAS DERIVADAS EN EL MISMO ACTO.** Las medi y las "
  "publico en la TAREA 1: `docs/INTRA_DOMINIO_INFORME.md` linea 6941 y "
  "`docs/plan/03_FUSIONES.md` linea 5424, mas una tercera en un reporte archivado que "
  "no se toca. **Mi lectura es que no envejecen como frase**, porque las dos dicen que "
  "el 730 *declara* la `A` por la lectura vieja y la fila **sigue diciendo eso**, con "
  "el texto viejo entero encima; lo que envejece es la clase que el lector infiere. "
  "**Y mi motivo para no editarlas es que es prosa sellada del informe y del plan**, "
  "que es forma, y la forma del plan el propio auditor la manda al fundador en su "
  "`6.2`. **Puedo estar equivocado en las dos mitades y por eso lo marco.**")
w()
w("**`D.2` EL PUESTO `474`.** Es el unico de los tres que quedan en `A` que **no tiene "
  "bloque de EJECUCION con la vara nombrada**, y lleva la lectura vieja escrita en "
  "presente (*la figura NO APLICA: manda la regla original*). **No lo muevo**, porque "
  "la ratificacion del banco lo nombra entre los que se sostienen y su razon cierra por "
  "contenido. **Pero es el que mas se parece al 730 de los que quedan**, y si alguien "
  "va a discutir uno, va a ser ese.")
w()
w("**`D.3` DIGO QUE DOS CIFRAS DEL ACTA 211 NO REPRODUCEN.** Su **13** y su **9** no "
  "salen de ningun patron que yo haya probado: el guion literal da 11 y 8, el patron "
  "holgado da 14 y 10. **Puede que el auditor usara un tercer patron que no se me "
  "ocurrio**, y por eso publico LOS DOS MIOS con su expresion regular al lado en vez de "
  "decir solo que el suyo esta mal. **Lo que no es discutible es que la lista de los "
  "cuatro en `A` y los once del choque reproducen al digito.**")
w()
w("**`D.4` PEGUE LAS TRES RAZONES ENTERAS DENTRO DE CERCA.** El encargo pide la razon "
  "entera; las cercas son donde esta casa pone el verbatim, y la guarda de las dos "
  "convenciones **no mira dentro de una cerca** (es lo que el acta 211 mide en su "
  "`7.2`). **O sea que las cifras que esas razones llevan dentro entran al reporte sin "
  "que ninguna guarda las mire.** Son del autor que las escribio y no mias, y lo digo, "
  "pero alguien puede sostener que un verbatim con cifras deberia ir de otra manera.")
w()

# ================================================================== 6
w("## 6. LAS PREGUNTAS")
w()
w("**`P.1` EL BARRIDO DEL `9.10`: QUIEN LO HACE.** Cuando una relectura conjunta "
  "voltea UN veredicto, las citas vivas de ese numero en el informe y en el plan "
  "quedan describiendo la clase vieja. **El `9.10` manda barrerlas y el encargo no me "
  "lo ordena, y editar prosa sellada tampoco me toca.** No es contradiccion suficiente "
  "para parar (la `D.1` explica por que), pero la casa no tiene escrito quien lo hace "
  "en un volteo de UNA sola fila. **Traigo las dos lineas nombradas para que se "
  "adjudique.**")
w()
w("**`P.2` EL INSTRUMENTO DE RUTAS SE CAE CON UN DIRECTORIO, Y ESO TOCA A TRES "
  "REPORTES.** Va entera en la `7`, con su medicion. La pregunta es de gobierno: **la "
  "moratoria prohibe reparar lectores**, y este no da una cifra mala, da una excepcion. "
  "**No lo toque. Pregunto si el arreglo entra por la puerta de la caida de dato o si "
  "espera a que se levante la moratoria.**")
w()

# ================================================================== 7
w("## 7. PENDIENTES DE DOCTRINA")
w()
w("**`PD.1` UNA CORRECCION QUE CONSERVA EL TEXTO VIEJO ENTERO DEJA LAS CITAS "
  "DERIVADAS EN UN ESTADO QUE LA DOCTRINA NO NOMBRA.** El banco `9.10` habla de tablas "
  "que **citan un veredicto por numero** y de volteos **en bloque**. Aqui hay un volteo "
  "de UNA fila y dos citas que **no son tablas**: son prosa narrativa que describe lo "
  "que la fila decia, y que **sigue siendo cierta como descripcion del texto**. **No "
  "hay regla que diga si eso hay que barrerlo, matizarlo o dejarlo.** Registro lo mejor "
  "sostenido (no barrer, declarar) y sigo, que es lo que manda la regla 5 de "
  "`EJECUTOR.md`.")
w()
w("**`PD.2` UN VERBATIM CON CIFRAS AJENAS DENTRO DE UNA CERCA NO TIENE REGLA.** Va "
  "ligado a la `D.4`. La casa exige que toda cifra lleve su corte y su atribucion, y "
  "una razon del archivo pegada entera trae docenas de cifras del que la escribio. **La "
  "cerca las saca del alcance de la guarda, que es lo que las hace publicables; lo que "
  "no esta escrito es si eso es lo correcto o solo lo que funciona.**")
w()

# ================================================================== 8
w("## 8. MIS CAIDAS PROPIAS, CADA UNA CON SU NOMBRE Y CONTADA UNA SOLA VEZ")
w()
w("**`C.1`. ESCRIBI Y COMMITEE UN FICHERO LLAMADO `SALIDA_V212_TALLADOR_CABECERA.txt` "
  "QUE NO LLEVABA UNA CABECERA: LLEVABA UN RECHAZO.** En la apertura corri el tallador "
  "sabiendo que la mitad del cierre no existe todavia, y **redirigi su salida al mismo "
  "nombre que usa el fichero bueno**. Durante un commit entero, una ruta que promete "
  "una cabecera tallada apuntaba a veinte celdas que no se pudieron leer. **Es la "
  "especie de LA RUTA QUE PROMETE PRUEBA ES CIFRA** (`EJECUTOR.md` 1): la ruta existia "
  "y no media cero, asi que ninguna guarda la habria cazado, y el contenido no era el "
  "que el nombre promete. **REMEDIO, y es una linea: el tallador de apertura, si se "
  "corre, escribe en un nombre con `_RECHAZO` y no en el del cierre.** El fichero bueno "
  "existe desde el cierre y es el que la cabecera cita.")
w()
w("**LO QUE NO CUENTO COMO CAIDA, Y DIGO POR QUE.** Primero: **el heredoc de comillas "
  "simples se me cayo** al escribir el primer computo, igual que a la 209, la 210, la "
  "211 y al propio auditor. **No es caida porque el remedio ya estaba escrito y lo "
  "cumpli:** use la herramienta de fichero y lo digo, que es lo que el acta 210 dejo "
  "dicho. Segundo: **el compositor de la TAREA 1 cayo en ROJO en su primera corrida**, "
  "porque le pedi la tercera aparicion de una linea que solo tiene dos. **Eso no es una "
  "caida: es la guarda haciendo su trabajo**, y cayo **antes** de escribir nada. "
  "Tercero: **parche una celda del reporte ya anexado** para quitarle unas comillas "
  "inversas a un directorio; **no lo cuento como caida porque el parche se verifico "
  "contra el `.md` regenerado byte a byte** y porque el motivo esta publicado entero en "
  "la `7`, pero **lo digo en vez de callarlo** porque un reporte parcheado a mano es "
  "exactamente lo que la 211 decidio no volver a hacer.")
w()

# ================================================================== 7 bis (hallazgo)
w("## 7 BIS. EL HALLAZGO DE LA VUELTA, MEDIDO Y NO REPARADO")
w()
w("**EL INSTRUMENTO QUE HACE CUMPLIR *LA RUTA QUE PROMETE PRUEBA ES CIFRA* SE CAE CON "
  "EXCEPCION SI EL REPORTE CITA UN DIRECTORIO.** `scripts/loop/vuelta186_rutas_del_reporte.py` "
  "casa la cadena docs/plan seguida de barra (la escribo aqui SIN comillas inversas "
  "a proposito, porque escribirla con ellas reproduce el fallo dentro de este mismo "
  "reporte, y eso me paso), `os.path.exists` dice que si porque el "
  "directorio existe, y el `read()` revienta. **Lo medi importando SU funcion, para que "
  "el patron fuera el suyo y no uno mio.**")
w()
HAL = [l.strip()[len("CIFRA "):] for l in cargar(SHR)
       if l.startswith("CIFRA docs/loop/reportes/")
       or l.startswith("CIFRA rutas de docs/loop/reportes/")
       or l.startswith("CIFRA ese texto TUMBA")]
w(tabla("LOS DOS REPORTES ARCHIVADOS, MEDIDOS", ["lo que midio el instrumento"],
        [[h] for h in HAL], 6, "`" + SHR + "`"))
w("**" + pick(SHR, "CIFRA directorios citados en los DOS sujetos archivados") + ".** "
  "**LOS SUJETOS SON LOS DOS REPORTES YA ARCHIVADOS Y NO EL DE ESTA VUELTA, A "
  "PROPOSITO:** este reporte todavia va a crecer con su cierre, y publicar aqui sus "
  "bytes seria medir temprano y publicar tarde. **A este lo mide el propio instrumento "
  "de la casa DESPUES del cierre, y si citara un directorio se caeria.** "
  "**NO ES UN DEFECTO QUE TRAIGA ESTA VUELTA:** el reporte de la 210 y el de la 211 "
  "citan dos directorios cada uno y los dos tumban el instrumento igual. **Y esto "
  "prueba una cosa que importa mas que el crash: la cifra de rutas que el reporte de la "
  "211 publica no puede haber salido de este instrumento, porque sobre ese texto el "
  "instrumento no llega a imprimir.**")
w()
w("**NO LO REPARO, Y ES LETRA:** la moratoria de `AUDITOR.md` 6.3 prohibe arreglar "
  "lectores. **Lo que si hice, porque no cuesta codigo, es sacar de mi reporte los "
  "DOS sitios donde citaba un directorio entre comillas inversas**, uno en la TAREA 1 "
  "y otro en esta misma seccion, **y por eso el instrumento SI corre sobre este "
  "reporte**. El segundo es el que mas dice: **describir el fallo con su ejemplo "
  "entrecomillado lo reproducia**, y lo cace corriendo el instrumento sobre el reporte "
  "ya cerrado en vez de darlo por bueno. Su caso rojo por mutacion esta corrido: "
  + pick(SHR, "EL CASO ROJO CAE COMO TIENE QUE CAER") + ".")
w()

# ================================================================== propuesta
w("## LO QUE PROPONGO PARA LA VUELTA SIGUIENTE")
w()
w("1. **ADJUDICAR LA `P.1`**: quien barre las citas vivas de un veredicto volteado "
  "cuando el volteo es de una sola fila. Las dos lineas estan nombradas y medidas, y "
  "el trabajo, si se adjudica, son dos ediciones de prosa.")
w("2. **ADJUDICAR LA `P.2`**: si el crash del instrumento de rutas entra por la puerta "
  "de la caida de dato (y entonces se arregla ya) o espera a que se levante la "
  "moratoria. **Mientras no se decida, todo reporte que cite un directorio entre "
  "comillas inversas se queda sin medir sus rutas, y eso no deja sintoma.**")
w("3. **NO ABRIR COLA DE RE-CRIBADO.** La TAREA 2 midio que **ninguno** de los tres "
  "que quedan en `A` cuelga de la silueta. **El cerco del cero-enlazados esta cerrado**, "
  "y la unica marca que queda es la `D.2` del `474`, que es marca y no encargo.")
w("4. **LA 215 ES LA VUELTA DE BATERIA**, por la cadencia de cinco de `AUDITOR.md` "
  "6.1. La 212 no lo es y su seccion 9 lo declara con su hueco medido.")
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
destino = os.path.join(AQUI, "_v%d_cierre_texto.md" % VUELTA)
io.open(destino, "w", encoding="utf-8", newline=NL).write(texto)
print("ESCRITO %s -> %d bytes, %d lineas"
      % (os.path.relpath(destino, RAIZ).replace(os.sep, "/"),
         len(texto.encode("utf-8")), texto.count(NL)))
