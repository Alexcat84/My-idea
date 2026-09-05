# -*- coding: utf-8 -*-
r"""vuelta177_apertura.py . EL BLOQUE DE APERTURA DE LA VUELTA 177, ENTERO.

CLON DECLARADO de scripts/loop/vuelta175_apertura.py (la 176 no escribio
apertura: no corrio su bloque, y esa lectura suya queda CORREGIDA en el acta 176
punto 7.1). Cambia el numero de vuelta, el prefijo de las salidas, la lista
RUTAS_DEL_ENCARGO y el bloque H, que aqui mide lo que ESTE encargo promete y
nada mas.

LA AFIRMACION DE CLON NO SE PUBLICA COMO COMPROBADA AQUI, Y SE DICE POR QUE.
El acta 176, seccion 5, tumbo la frase "el diff sale VACIO" que los ficheros de
la 176 llevaban en su docstring: la corrio y salieron 58 lineas de diff, 33 de
ellas de la maquina. Este fichero NO repite esa frase. El cotejo de este clon se
hace con el instrumento que nace en la TAREA 1.d de esta misma vuelta,
scripts/loop/cotejar_clon_declarado.py, y su salida se pega en el reporte. Hasta
que ese instrumento corra, lo unico que este docstring afirma es la INTENCION del
clon, no su resultado.

ESTA VUELTA NO ES DE BATERIA. La cadencia esta adjudicada en el acta 176 punto
7.8: la proxima vuelta de bateria es la 181, no la 180, porque el contador se
reancla a la vuelta que de verdad la corrio y la 175 no lo fue. Por eso el bloque
H de esta apertura NO mide la nomina como sujeto de la vuelta: mide LOS SEIS
SUJETOS DE LA TAREA 1 (el arnes del rojo, las dos frases del clon declarado, la
salida del lanzador dentro de docs/loop/, el rechazo sin sellar del tallador y el
tope de tramo sin computar) y EL UNIVERSO DE OP-L-03 de la TAREA 2.

EL BLOQUE H NO TECLEA NINGUN HASH NI NINGUNA CIFRA. La vuelta 79 cayo por
publicar como commit de apertura un hash escrito a mano; aqui todo se LOCALIZA y
se imprime lo que salga. La cifra viva del caso H del arnes del rojo NO se copia
del encargo ni del acta: se recomputa llamando a las funciones puras del propio
sujeto, que es la unica fuente que la casa reconoce (EJECUTOR.md 2, EL
INSTRUMENTO MANDA). Y el universo de OP-L-03 NO se copia de la nota de la ficha:
se recomputa con scripts/plan/backlog_l03_vuelta14.py, que es el instrumento que
la propia nota cita.

LA CIFRA DE BYTES SE PUBLICA POR LAS DOS CONVENCIONES (hallazgo 4.1 del acta
174, subido al fundador en el acta 176 seccion 8 punto 1 y TODAVIA SIN
CONVENCION FIJADA). Mientras nadie fije cual manda, esta apertura mide LAS DOS a
la vez, la de disco (os.path.getsize) y la de git (git cat-file -s), y las
imprime juntas.

POR QUE SE CORRE AQUI: EJECUTOR.md regla 1, "LA APERTURA SE MIDE ANTES DE LA
PRIMERA OPERACION". Este fichero NO toca REPORTE.md, NO toca la nomina, NO corre
la bateria y NO escribe en docs/plan/: sus salidas son SALIDA_V177_*.txt. El
esqueleto de la 177 va DESPUES de esto y no aqui.

EL CICLO DE GATE 0 VA ENTERO Y EN SU ORDEN, NUNCA run_phase1 SUELTO.

LO QUE ESTA VUELTA SABE DE SU ARBOL ANTES DE MEDIRLO, PARA NO PODER MAQUILLARLO
DESPUES: git status --porcelain, corrido a mano al abrir la vuelta, dio UNA sola
linea, " M dataset/metadata/master_graph.json", con git diff --numstat de CERO
filas, y scripts/loop/guarda_commit_dataset.py salio VERDE cotejando los blobs
(arbol cb33552aedddab4d contra HEAD cb33552aedddab4d, CONTENIDO IDENTICO: SI), o
sea que la M es de estado y no de contenido y NO SE RESTAURO NADA porque no habia
nada que restaurar. La prediccion se escribe AQUI, antes de correr, y los bloques
C/D/E/F de abajo la miden sin saber lo que hay escrito.

USO:
  python scripts/loop/vuelta177_apertura.py
"""
import io
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
PY = sys.executable
VUELTA = 177

# LOS SEIS SUJETOS DE LA TAREA 1, nombrados aqui para que el bloque H no los
# pueda elegir despues de ver el resultado.
SUJETOS_T1 = [
    "scripts/loop/vuelta166_tarea2_mutacion_correccion.py",
    "scripts/loop/vuelta176_esqueleto_reporte.py",
    "scripts/loop/vuelta176_cierre.py",
    "scripts/loop/vuelta176_bateria_por_tramos.py",
    "scripts/loop/tallar_cabecera_reporte.py",
    "scripts/loop/verificar_mutaciones_viejas.py",
]

RUTAS_DEL_ENCARGO = [
    "dataset/metadata/master_graph.json",
    "docs/loop/REPORTE.md",
    "docs/loop/ACTA_AUDITOR.md",
    "docs/loop/EJECUTOR.md",
    "docs/loop/PROMPT_SIGUIENTE.md",
    "docs/loop/reportes/REPORTE_V176.md",
    "docs/plan/OPERACIONES.jsonl",
    "docs/plan/LECTURAS_DIRIGIDAS.md",
    "docs/INTRA_DOMINIO_VEREDICTOS.jsonl",
    "scripts/plan/backlog_l03_vuelta14.py",
    "scripts/loop/vuelta150_3_relectura_expediente.py",
    "scripts/loop/cotejar_clon_declarado.py",
    "scripts/loop/guarda_commit_dataset.py",
    "scripts/loop/cerrar_reporte.py",
    "scripts/loop/archivar_reporte.py",
    "scripts/loop/anexar_tarea_al_reporte.py",
    "scripts/loop/paso0_archivar_anterior.py",
    "scripts/loop/serie_de_registros.py",
] + SUJETOS_T1

FRASE_CLON = "SALE VACIO"


def correr(args, shell=False, cwd=None):
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run(args, cwd=cwd or RAIZ, capture_output=True, env=env, shell=shell)
    out = r.stdout.decode("utf-8", errors="replace") + r.stderr.decode("utf-8", errors="replace")
    return r.returncode, out


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def bytes_de_git(ruta):
    """Los bytes que git guarda para esa ruta en HEAD, o None si no esta.
    LA SEGUNDA CONVENCION del hallazgo 4.1 del acta 174, medida y no supuesta."""
    c, o = git(["cat-file", "-s", "HEAD:" + ruta])
    o = o.strip()
    return int(o) if c == 0 and o.isdigit() else None


def escribir(nombre, texto):
    ruta = os.path.join(LOOP, "SALIDA_V%d_%s_APERTURA.txt" % (VUELTA, nombre))
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)
    print("ESCRITO: %s (%d bytes)" % (os.path.basename(ruta), len(texto.encode("utf-8"))))


# ---------------------------------------------------------------- A. EL SELLO
lineas = []
w = lineas.append
NL = chr(10)
w("SELLO DE APERTURA DE LA VUELTA %d, escrito ANTES de la primera operacion" % VUELTA)
w("instrumento: scripts/loop/vuelta%d_apertura.py" % VUELTA)
w("regimen: VUELTA NORMAL, NO DE BATERIA (acta 176 punto 7.8: la proxima es la 181).")
w("         Dos sub-tareas (AUDITOR.md 6.2, regimen temporal todavia vigente).")
w("")

w("=== A. HEAD DE APERTURA (git rev-parse HEAD) ===")
c, head = git(["rev-parse", "HEAD"])
head = head.strip()
w(head)
c, asunto = git(["log", "-1", "--format=%H%x09%ad%x09%s", "--date=iso"])
w(asunto.strip()[:400])
w("")

w("=== B. RAMA Y REMOTO (leidos de git, no tecleados) ===")
c, rama = git(["rev-parse", "--abbrev-ref", "HEAD"])
w("rama: " + rama.strip())
c, up = git(["rev-parse", "--abbrev-ref", "@{u}"])
w("remoto de seguimiento: " + (up.strip() if c == 0 else "(ninguno)"))
c, ahead = git(["rev-list", "--left-right", "--count", "HEAD...@{u}"])
w("adelante/atras contra el remoto (HEAD...upstream): " + (ahead.strip() if c == 0 else "(no medible)"))
w("")

w("=== C. git status --porcelain ENTERO ===")
c, st = git(["status", "--porcelain"])
for l in st.splitlines():
    w(l)
w("CIFRA lineas de status: %d" % len([l for l in st.splitlines() if l.strip()]))
w("")

w("=== D. BYTES DE CADA RUTA QUE EL ENCARGO NOMBRA, POR LAS DOS CONVENCIONES ===")
w("(disco = os.path.getsize; git = git cat-file -s HEAD:<ruta>. Hallazgo 4.1 del")
w(" acta 174: divergen en el numero de finales de linea y SIGUE SIN CONVENCION)")
for ruta in RUTAS_DEL_ENCARGO:
    p = os.path.join(RAIZ, ruta.replace("/", os.sep))
    g = bytes_de_git(ruta)
    if os.path.exists(p):
        w("%s -> disco %d bytes | git %s"
          % (ruta, os.path.getsize(p), ("%d bytes" % g) if g is not None else "NO ESTA EN HEAD"))
    else:
        w("%s -> disco NO EXISTE | git %s"
          % (ruta, ("%d bytes" % g) if g is not None else "NO ESTA EN HEAD"))
w("")

w("=== E. DIFF REAL EN BYTES DE LOS MODIFICADOS (cambio contra suciedad) ===")
c, mod = git(["ls-files", "-m"])
for ruta in [l for l in mod.splitlines() if l.strip()]:
    c2, d = git(["diff", "--", ruta])
    w("%s -> diff de %d bytes" % (ruta, len(d.encode("utf-8"))))
    c3, dn = git(["diff", "--numstat", "--", ruta])
    w("   %s -> git diff --numstat: %d filas" % (ruta, len([l for l in dn.splitlines() if l.strip()])))
w("")

w("=== F. LO NO SEGUIDO POR GIT, FICHERO A FICHERO CON SUS BYTES ===")
c, unt = git(["status", "--porcelain", "--untracked-files=all"])
n_unt = 0
for l in unt.splitlines():
    if l.startswith("?? "):
        r = l[3:].strip().strip(chr(34))
        p = os.path.join(RAIZ, r.replace("/", os.sep))
        tam = os.path.getsize(p) if os.path.isfile(p) else -1
        w("%s -> %s" % (r, ("%d bytes" % tam) if tam >= 0 else "(no es fichero)"))
        n_unt += 1
w("CIFRA ficheros no seguidos: %d" % n_unt)
w("")

w("=== G. git ls-tree DE HEAD SOBRE ESAS RUTAS ===")
for ruta in RUTAS_DEL_ENCARGO:
    c, t = git(["ls-tree", "HEAD", "--", ruta])
    w("%s -> %s" % (ruta, t.strip() if t.strip() else "NO ESTA EN EL ARBOL DE HEAD"))
w("")

w("=== H. EL REPORTE EN HEAD, MEDIDO SIN CREERLE AL ENCARGO ===")
c, rep = git(["show", "HEAD:docs/loop/REPORTE.md"])
w("primera linea: %s" % (rep.split(NL, 1)[0].strip() if rep else "(vacio)"))
w("lineas (saltos de linea contados): %d" % rep.count(NL))
w("bytes en git: %d" % len(rep.encode("utf-8")))
MARCAS = ["SIN ESCRIBIR TODAVIA", "PENDIENTE DE TALLAR AL CIERRE",
          "ABIERTA, SIN CERRAR", "HUECO DECLARADO Y MEDIDO"]
MARCAS = MARCAS + [NL + "## %d." % k for k in range(3, 10)]
for marca in MARCAS:
    w("   contiene %-34s -> %s" % (repr(marca), "SI" if marca in rep else "NO"))
w("")

w("=== H.1 EL REPORTE DEL ARBOL, QUE ES EL QUE EL ESQUELETO DE LA 177 PISARA ===")
RUTA_REP = os.path.join(LOOP, "REPORTE.md")
arbol = io.open(RUTA_REP, encoding="utf-8").read().replace(chr(13) + NL, NL)
w("primera linea: %s" % arbol.split(NL, 1)[0].strip())
w("bytes en disco (normalizado a LF): %d | saltos de linea: %d"
  % (len(arbol.encode("utf-8")), arbol.count(NL)))
w("bytes en disco (crudos, os.path.getsize): %d" % os.path.getsize(RUTA_REP))
w("identico byte a byte al de HEAD: %s"
  % ("SI" if arbol == rep.replace(chr(13) + NL, NL) else "NO"))
for marca in MARCAS:
    w("   contiene %-34s -> %s" % (repr(marca), "SI" if marca in arbol else "NO"))
w("")

w("=== H.2 EL COMMIT QUE DE VERDAD TOCA REPORTE.md POR ULTIMA VEZ ===")
w("(no se teclea ningun hash: se localiza con git log y se imprime lo que salga)")
c, cual = git(["log", "--format=%h%x09%s", "-6"])
w("los seis ultimos commits:")
for l in cual.splitlines():
    w("   " + l[:150])
c, ult = git(["log", "-1", "--format=%h", "--", "docs/loop/REPORTE.md"])
w("ultimo commit que TOCA docs/loop/REPORTE.md: %s" % ult.strip())
c, asu = git(["log", "-1", "--format=%s", ult.strip()])
w("   su asunto: %s" % asu.strip()[:150])
w("")

w("=== H.3 LAS PIEZAS QUE cerrar_reporte.py PEDIRA PARA CERRAR LA 177 ===")
w("(al abrir NO EXISTE NINGUNA, y eso es lo correcto: las produce esta vuelta.")
w(" La de bateria NO SE VA A PRODUCIR: esta vuelta no es de bateria y la seccion 9")
w(" cierra con el HUECO DECLARADO Y MEDIDO, acta 176 punto 7.8)")
for r in ["docs/loop/SALIDA_V177_TALLADOR_CABECERA.txt",
          "scripts/loop/_v177_cierre_texto.md",
          "docs/loop/SALIDA_V177_BATERIA.txt"]:
    p = os.path.join(RAIZ, r.replace("/", os.sep))
    if os.path.exists(p):
        w("%s -> %d bytes" % (r, os.path.getsize(p)))
    else:
        w("%s -> NO EXISTE" % r)
w("")

w("=== H.4 QUE REPORTES ESTAN YA ARCHIVADOS EN docs/loop/reportes/ ===")
DIRA = os.path.join(LOOP, "reportes")
arch = sorted(os.listdir(DIRA)) if os.path.isdir(DIRA) else []
for n in arch:
    g = bytes_de_git("docs/loop/reportes/" + n)
    w("   %s -> disco %d bytes | git %s"
      % (n, os.path.getsize(os.path.join(DIRA, n)),
         ("%d bytes" % g) if g is not None else "NO ESTA EN HEAD"))
w("CIFRA reportes archivados: %d" % len(arch))
w("REPORTE_V176.md archivado: %s" % ("SI" if "REPORTE_V176.md" in arch else "NO"))
w("")

w("=== H.5 EL ARNES DEL ROJO, MEDIDO SIN CORRERLO Y SIN CREERLE AL ENCARGO ===")
w("(TAREA 1.b. El encargo dice que la linea 175 compara contra un 3 tecleado y")
w(" que la medicion viva da 11. NI UNA NI OTRA SE COPIAN: se localiza la linea")
w(" en el fichero y se recomputa la cifra viva con las funciones puras del sujeto)")
ARNES = os.path.join(RAIZ, "scripts", "loop", "vuelta166_tarea2_mutacion_correccion.py")
txt_arnes = io.open(ARNES, encoding="utf-8").read().replace(chr(13) + NL, NL)
ls_arnes = txt_arnes.split(NL)
w("fichero: scripts/loop/vuelta166_tarea2_mutacion_correccion.py (%d lineas)" % len(ls_arnes))
for i, l in enumerate(ls_arnes, 1):
    if "H_el_texto_nombra" in l or "H_con_un_hallazgo" in l:
        w("   LINEA %d: %s" % (i, l.strip()))
w("CIFRA lineas que llevan el literal 'cae sobre': %d"
  % len([l for l in ls_arnes if "cae sobre" in l]))
try:
    sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
    import vuelta166_tarea2_correccion_op_l_01 as T166   # noqa: E402
    _mapa, _nn = T166.mapa_de_alias()
    _once = T166.las_once()
    _V = T166.veredictos()
    _nl, _nr, _npl, _npr, _hall = T166.medir_clausula_1(_mapa, _once, _V)
    _real = T166.texto_correccion_1(_hall, _nl, _nr, _npl, _npr, len(_mapa), len(_V))
    w("CIFRA hallazgos que la medicion VIVA da hoy (len(hall)): %d" % len(_hall))
    w("CIFRA veces que el texto real dice 'cae sobre': %d" % _real.count("cae sobre"))
    w("CIFRA filas de docs/INTRA_DOMINIO_VEREDICTOS.jsonl: %d" % len(_V))
    w("CIFRA alias del mapa: %d" % len(_mapa))
    w("EL ESPERADO TECLEADO Y LA MEDICION VIVA COINCIDEN: %s"
      % ("SI" if _real.count("cae sobre") == 3 else "NO"))
except Exception as e:
    w("NO SE PUDO RECOMPUTAR LA CIFRA VIVA: %r" % (e,))
w("")

w("=== H.6 LAS DOS FRASES DEL CLON DECLARADO, LOCALIZADAS Y NO SUPUESTAS ===")
w("(TAREA 1.c. El acta 176 seccion 5 dice que la frase esta en DOS docstrings de")
w(" scripts/. Aqui se busca el literal %r en todo scripts/loop/ y se imprime lo" % FRASE_CLON)
w(" que salga, sin dar por buena la cifra dos)")
sede = []
DIRS = os.path.join(RAIZ, "scripts", "loop")
for n in sorted(os.listdir(DIRS)):
    if not n.endswith(".py"):
        continue
    t = io.open(os.path.join(DIRS, n), encoding="utf-8", errors="replace").read()
    if FRASE_CLON in t:
        cuantas = t.count(FRASE_CLON)
        sede.append(n)
        w("   %s -> %d vez/veces" % (n, cuantas))
w("CIFRA ficheros de scripts/loop/ con el literal %r: %d" % (FRASE_CLON, len(sede)))
w("")

w("=== H.7 LA SALIDA DEL LANZADOR DE TRAMO DENTRO DE docs/loop/ (D.5) ===")
w("(TAREA 1.e. Se cuentan los ficheros de lanzador que HOY viven en docs/loop/,")
w(" que es lo que el acta 176 punto 7.5 manda sacar de ahi)")
lanz = [n for n in sorted(os.listdir(LOOP)) if "LANZADOR" in n.upper()]
for n in lanz:
    w("   %-52s -> %d bytes" % (n, os.path.getsize(os.path.join(LOOP, n))))
w("CIFRA ficheros de LANZADOR dentro de docs/loop/: %d" % len(lanz))
LANZ = os.path.join(RAIZ, "scripts", "loop", "vuelta176_bateria_por_tramos.py")
t_lanz = io.open(LANZ, encoding="utf-8").read().replace(chr(13) + NL, NL)
w("el lanzador nombra tempfile (fichero de trabajo fuera de docs/loop/): %s"
  % ("SI" if "tempfile" in t_lanz else "NO"))
w("el lanzador escribe su PROPIA transcripcion a algun sitio: %s"
  % ("SI" if "TRANSCRIPCION" in t_lanz else "NO"))
w("")

w("=== H.8 EL RECHAZO DEL TALLADOR, QUE HOY NO DEJA RASTRO ===")
w("(TAREA 1.e. El acta 176 seccion 9 punto 4 dice que el 37 no se puede")
w(" re-verificar porque el tallador no dejo salida de aquel rechazo)")
rech = [n for n in sorted(os.listdir(LOOP)) if "TALLADOR_RECHAZO" in n]
for n in rech:
    w("   %s -> %d bytes" % (n, os.path.getsize(os.path.join(LOOP, n))))
w("CIFRA ficheros SALIDA_V<N>_TALLADOR_RECHAZO.txt en docs/loop/: %d" % len(rech))
TALL = os.path.join(RAIZ, "scripts", "loop", "tallar_cabecera_reporte.py")
t_tall = io.open(TALL, encoding="utf-8").read().replace(chr(13) + NL, NL)
w("el tallador nombra TALLADOR_RECHAZO en su codigo: %s"
  % ("SI" if "TALLADOR_RECHAZO" in t_tall else "NO"))
for i, l in enumerate(t_tall.split(NL), 1):
    if "no se pudieron leer" in l:
        w("   LINEA %d: %s" % (i, l.strip()))
w("")

w("=== H.9 EL TAMANO DE TRAMO, QUE HOY SE ELIGE Y NO SE COMPUTA (D.3 y P.3) ===")
BAT = os.path.join(RAIZ, "scripts", "loop", "verificar_mutaciones_viejas.py")
t_bat = io.open(BAT, encoding="utf-8").read().replace(chr(13) + NL, NL)
for i, l in enumerate(t_bat.split(NL), 1):
    if "def reparto_en_tramos" in l or "tamano-tramo" in l or "tamano_tramo" in l:
        w("   LINEA %d: %s" % (i, l.strip()[:130]))
w("reparto_en_tramos nombra minutos hoy: %s"
  % ("SI" if "minutos" in t_bat.split("def reparto_en_tramos", 1)[-1][:4000] else "NO"))
w("el fichero nombra tope_de_minutos: %s" % ("SI" if "tope_de_minutos" in t_bat else "NO"))
w("el fichero nombra tamano_por_minutos: %s" % ("SI" if "tamano_por_minutos" in t_bat else "NO"))
w("")

w("=== H.10 EL UNIVERSO DE OP-L-03, RECOMPUTADO Y NO COPIADO DE SU NOTA ===")
w("(TAREA 2. El encargo cita 55 pares en 29 actos, corte 2117, que es la")
w(" fecha_corte de la ficha. La nota de la MISMA ficha declara un recomputo")
w(" adjudicado en la vuelta 15 al corte 3388. Se corre el instrumento que la")
w(" propia nota cita y se imprime lo que salga, sin elegir entre los dos)")
c, o = correr([PY, "scripts/plan/backlog_l03_vuelta14.py"])
w("comando: python scripts/plan/backlog_l03_vuelta14.py -> exit %d" % c)
for l in o.split(NL):
    if l.strip():
        w("   " + l.rstrip()[:160])
w("")

w("=== H.11 LA VARA DEL TRABAJO PENDIENTE, CORRIDA POR MI EN ESTA VUELTA ===")
w("(la vara es scripts/loop/vuelta150_3_relectura_expediente.py y NUNCA el campo")
w(" estado, decision del fundador del 4 sep 2026)")
c, o = correr([PY, "scripts/loop/vuelta150_3_relectura_expediente.py", "--corte", head])
w("comando: vuelta150_3_relectura_expediente.py --corte %s -> exit %d" % (head[:8], c))
for l in o.split(NL):
    if ("LISTA" in l or "CIFRA" in l or "OP-L-03" in l or "OP-L-01" in l
            or "OP-L-02" in l or "OP-I-01" in l):
        w("   " + l.rstrip()[:160])
w("")

w("FIN DEL SELLO DE APERTURA")

texto = NL.join(lineas) + NL
io.open(os.path.join(LOOP, "SALIDA_V%d_APERTURA.txt" % VUELTA), "w",
        encoding="utf-8", newline=NL).write(texto)
print(texto)
escribir("HEAD", head + NL)

# ------------------------------------------------- B. EL BLOQUE DE MEDICIONES
c, o = correr([PY, "scripts/run_phase1.py", "--reaplico-curaduria"])
escribir("GATE0_CMD1", o + "\nEXITCODE: %d\n" % c)

c, o = correr([PY, "scripts/etiquetas_de_cara.py", "--aplicar"])
escribir("CICLO_ETIQUETAS", o + "\nEXITCODE: %d\n" % c)

c, o = correr([PY, "scripts/sync_assets_web.py"])
escribir("CICLO_SYNC", o + "\nEXITCODE: %d\n" % c)

c, o = correr(["git", "diff", "HEAD", "--numstat", "--", "dataset/", "web/", "engine/"])
escribir("CICLO_NUMSTAT", o + "\nEXITCODE: %d\n" % c)

c, o = correr([PY, "scripts/loop/vuelta83_conteo_aristas.py", "WORK"])
escribir("CONTEO", o + "\nEXITCODE: %d\n" % c)

# EL DESFASE DEL CALIBRADO, QUE ESTE BLOQUE NO MEDIA Y EL DE CIERRE SI.
#
# ANADIDO EN LA VUELTA 177, Y ES UN DEFECTO HEREDADO QUE SE ARREGLA AQUI EN VEZ
# DE VOLVER A PAGARLO. El bloque de apertura del que este desciende
# (`vuelta175_apertura.py`) NO corria este paso y el de cierre SI: la palabra
# "desfase" sale 0 veces en aquel y 2 veces en el de cierre. Consecuencia
# medida: `tallar_cabecera_reporte.py --fase04` exige LAS DOS columnas, asi que
# con la apertura coja el tallador NO PODIA SALIR VERDE NUNCA por el lado
# izquierdo, dijera lo que dijera el resto. En la 177 salio ROJO por exactamente
# esas 2 celdas, las 2 del lado APERTURA, y quedo sellado en
# `docs/loop/SALIDA_V177_T1E_RECHAZO_REAL.txt` por la guarda que la TAREA 1.e de
# esta misma vuelta acababa de poner. La guarda se estreno cazando a su autor.
#
# LO QUE ESTO NO ARREGLA, Y SE DICE: en la 177 la medicion se tomo TARDE, al
# cierre, porque el rechazo se descubrio al cierre. Va declarada como tal en el
# reporte, con la prueba que la sostiene: `git diff --numstat` entre los dos
# sellos da 0 filas sobre `dataset/`, `web/` y `engine/`, y la salida de
# apertura resulta IDENTICA byte a byte a la de cierre (sha256 `7d683eea4700f18b`
# las dos), o sea que el arbol que este instrumento lee es el mismo en las dos
# puntas. DESDE LA 178 SE TOMA AQUI, EN SU SITIO, y esta linea es lo que lo
# garantiza.
c, o = correr([PY, "scripts/loop/vuelta85_medir_desfase_calibrado.py", "WORK"])
escribir("DESFASE_CALIBRADO", o + "\nEXITCODE: %d\n" % c)

c, o = correr([PY, "engine/run_all_tests.py"])
escribir("MOTOR", o + "\nEXITCODE: %d\n" % c)

c, o = correr("npx tsc --noEmit -p tsconfig.json", shell=True, cwd=os.path.join(RAIZ, "web"))
escribir("TSC", (o if o.strip() else "") + "EXIT=%d\n" % c)

c, o = correr("pnpm test", shell=True, cwd=os.path.join(RAIZ, "web"))
escribir("WEB", o + "\nEXITCODE: %d\n" % c)

print("BLOQUE DE APERTURA COMPLETO")
