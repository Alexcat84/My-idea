# -*- coding: utf-8 -*-
r"""vuelta175_apertura.py . EL BLOQUE DE APERTURA DE LA VUELTA 175, ENTERO.

CLON DECLARADO de scripts/loop/vuelta174_apertura.py. Cambia SOLO el numero de
vuelta, el prefijo de las salidas, la lista RUTAS_DEL_ENCARGO y el bloque H, que
aqui mide lo que ESTE encargo promete y nada mas.

ESTA ES UNA VUELTA DE BATERIA (AUDITOR.md 6.1, decision del fundador del 5 sep
2026): la bateria corre CADA CINCO, sola, y no lleva nada mas al lado salvo su
propio reporte. Por eso el bloque H de esta apertura NO mide fichas de plan: mide
LA NOMINA, LOS CINCO ARNESES QUE EL ACTA 174 DICE QUE FALTAN, y LAS CORRIDAS DE
BATERIA QUE SALIERON EN CERO BYTES.

EL BLOQUE H NO TECLEA NINGUN HASH NI NINGUNA CIFRA. La vuelta 79 cayo por
publicar como commit de apertura un hash escrito a mano; aqui todo se LOCALIZA y
se imprime lo que salga. Y la cifra de los cinco que faltan NO se copia del acta:
se recomputa con la funcion pura arneses_que_faltan() de la propia bateria, que
es la unica fuente que la casa reconoce (EJECUTOR.md 2, EL INSTRUMENTO MANDA).

LA CIFRA DE BYTES SE PUBLICA POR LAS DOS CONVENCIONES (hallazgo 4.1 del acta
174, anotado para la 176 y todavia sin convencion fijada). Mientras nadie fije
cual manda, esta apertura mide LAS DOS a la vez, la de disco (os.path.getsize) y
la de git (git cat-file -s), y las imprime juntas. No es doctrina nueva: es la
deuda de lectura que el encargo anota, cumplida en el unico sitio donde se puede
cumplir sin adivinar.

POR QUE SE CORRE AQUI: EJECUTOR.md regla 1, "LA APERTURA SE MIDE ANTES DE LA
PRIMERA OPERACION". Este fichero NO toca REPORTE.md, NO toca la nomina y NO corre
la bateria: sus salidas son SALIDA_V175_*.txt y ninguna es ninguna de esas tres
cosas. El esqueleto de la 175 va en la TAREA 2 y NO aqui.

EL CICLO DE GATE 0 VA ENTERO Y EN SU ORDEN, NUNCA run_phase1 SUELTO.

LO QUE ESTA VUELTA SABE DE SU ARBOL ANTES DE MEDIRLO, PARA NO PODER MAQUILLARLO
DESPUES: git status --porcelain, corrido a mano al abrir la vuelta, dio UNA sola
linea, " M dataset/metadata/master_graph.json", con git diff --numstat VACIO (o
sea diff de CERO filas: suciedad de fin de linea, no cambio de contenido), y
git status --porcelain --untracked-files=all dio esa MISMA unica linea, o sea
CERO ficheros no seguidos. Y git rev-list --count origin/pasada-unica..HEAD salio
0: no hay nada pendiente de empujar, que es lo que la regla 3 de EJECUTOR.md
manda comprobar antes de tocar nada. La prediccion se escribe AQUI, antes de
correr, y los bloques C/D/E/F de abajo la miden sin saber lo que hay escrito.

USO:
  python scripts/loop/vuelta175_apertura.py
"""
import io
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
PY = sys.executable
VUELTA = 175

LOS_CINCO_DEL_ACTA = [
    "vuelta173_tarea1b_mutacion_hueco.py",
    "vuelta174_tarea1a_mutacion_44.py",
    "vuelta174_tarea1b_mutacion_esqueleto.py",
    "vuelta174_tarea1b_mutacion_sellar.py",
    "vuelta174_tarea2b_mutacion_confirmar.py",
]

RUTAS_DEL_ENCARGO = [
    "dataset/metadata/master_graph.json",
    "docs/loop/REPORTE.md",
    "docs/loop/ACTA_AUDITOR.md",
    "docs/loop/EJECUTOR.md",
    "docs/loop/PROMPT_SIGUIENTE.md",
    "docs/loop/reportes/REPORTE_V174.md",
    "docs/loop/SALIDA_V175_BATERIA.txt",
    "docs/loop/SALIDA_V175_TALLADOR_CABECERA.txt",
    "scripts/loop/_v175_cierre_texto.md",
    "scripts/loop/verificar_mutaciones_viejas.py",
    "scripts/loop/cerrar_reporte.py",
    "scripts/loop/archivar_reporte.py",
    "scripts/loop/anexar_tarea_al_reporte.py",
    "scripts/loop/paso0_archivar_anterior.py",
    "scripts/loop/tallar_cabecera_reporte.py",
    "scripts/loop/serie_de_registros.py",
] + ["scripts/loop/" + n for n in LOS_CINCO_DEL_ACTA]


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
w("regimen: VUELTA DE BATERIA (AUDITOR.md 6.1). Dos sub-tareas (AUDITOR.md 6.2).")
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
w(" acta 174: divergen en el numero de finales de linea y NO HAY CONVENCION FIJADA)")
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

w("=== H.1 EL REPORTE DEL ARBOL, QUE ES EL QUE EL ESQUELETO DE LA 175 PISARA ===")
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

w("=== H.3 LAS PIEZAS QUE cerrar_reporte.py PEDIRA PARA CERRAR LA 175 ===")
w("(al abrir NO EXISTE NINGUNA, y eso es lo correcto: las produce esta vuelta)")
for r in ["docs/loop/SALIDA_V175_TALLADOR_CABECERA.txt",
          "scripts/loop/_v175_cierre_texto.md",
          "docs/loop/SALIDA_V175_BATERIA.txt"]:
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
w("REPORTE_V174.md archivado: %s" % ("SI" if "REPORTE_V174.md" in arch else "NO"))
w("")

w("=== H.5 LA NOMINA Y LOS QUE FALTAN, POR SU PROPIA FUNCION PURA ===")
w("(esta es LA CIFRA DE LA TAREA 1. NO se copia del acta: se recomputa aqui)")
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
import verificar_mutaciones_viejas as VMV
ultima, faltan = VMV.arneses_que_faltan()
w("entradas de la nomina VIEJAS: %d" % len(VMV.VIEJAS))
w("arneses que el censo reconoce en scripts/loop/: %d" % len(VMV.arneses_del_directorio()))
w("ficheros .py en scripts/loop/: %d"
  % len([n for n in os.listdir(os.path.join(RAIZ, "scripts", "loop")) if n.endswith(".py")]))
w("ultima vuelta representada en la nomina: %s" % ultima)
w("arneses_que_faltan(): %d" % len(faltan))
for n in faltan:
    w("   FUERA DE LA NOMINA: " + n)
w("nomina_invisible_al_censo(): %d" % len(VMV.nomina_invisible_al_censo()))
w("familias que el censo reconoce: %s" % ", ".join(VMV.FAMILIAS_DE_ARNES))
w("")

w("=== H.6 LOS CINCO QUE EL ACTA 174 NOMBRA, UNO A UNO ===")
w("(el acta los nombra; aqui se comprueba que existen, cuanto miden, si admiten")
w(" --sujeto y si la funcion pura de arriba los devuelve DE VERDAD)")
devueltos = set(faltan)
for n in LOS_CINCO_DEL_ACTA:
    p = os.path.join(RAIZ, "scripts", "loop", n)
    existe = os.path.exists(p)
    txt = io.open(p, encoding="utf-8", errors="replace").read() if existe else ""
    w("%s" % n)
    w("   existe: %s | disco %s bytes | admite --sujeto: %s | lo devuelve arneses_que_faltan(): %s"
      % (existe, os.path.getsize(p) if existe else "NO EXISTE",
         "SI" if "--sujeto" in txt else "NO",
         "SI" if n in devueltos else "NO"))
w("CIFRA de los cinco del acta que la funcion pura confirma: %d de %d"
  % (len([n for n in LOS_CINCO_DEL_ACTA if n in devueltos]), len(LOS_CINCO_DEL_ACTA)))
w("CIFRA que la funcion pura devuelve y el acta NO nombra: %d"
  % len([n for n in faltan if n not in LOS_CINCO_DEL_ACTA]))
for n in faltan:
    if n not in LOS_CINCO_DEL_ACTA:
        w("   NO NOMBRADO POR EL ACTA: " + n)
w("")

w("=== H.7 LAS CORRIDAS DE BATERIA DE docs/loop/, CON SUS BYTES ===")
w("(regla del 5 sep 2026: LA RUTA QUE PROMETE PRUEBA ES CIFRA, y CERO BYTES es")
w(" CAIDA DE CIFRA. El encargo dice que llevan CUATRO vueltas en cero: se mide)")
vacias = 0
todas = [n for n in sorted(os.listdir(LOOP)) if "BATERIA" in n and n.endswith(".txt")]
for n in todas:
    tam = os.path.getsize(os.path.join(LOOP, n))
    if tam == 0:
        vacias += 1
    w("   %-46s -> %d bytes%s" % (n, tam, "   CERO BYTES" if tam == 0 else ""))
w("CIFRA ficheros de bateria en docs/loop/: %d" % len(todas))
w("CIFRA de ellos con CERO BYTES: %d" % vacias)
w("")

w("=== H.8 EL RELOJ DE LAS BATERIAS QUE SI TIENEN CUERPO, COMO CONTRASTE ===")
w("(contraste, NO fuente: EJECUTOR.md 2. La cifra de ESTA vuelta la dara su")
w(" propia corrida y ninguna otra)")
for n in todas:
    p = os.path.join(LOOP, n)
    if os.path.getsize(p) == 0:
        continue
    t = io.open(p, encoding="utf-8", errors="replace").read()
    for l in t.split(NL):
        if ("CIFRA TIEMPO TOTAL" in l and "minutos" in l) or "MUTACIONES VIEJAS." in l:
            w("   %s :: %s" % (n, l.strip()))
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

c, o = correr([PY, "engine/run_all_tests.py"])
escribir("MOTOR", o + "\nEXITCODE: %d\n" % c)

c, o = correr("npx tsc --noEmit -p tsconfig.json", shell=True, cwd=os.path.join(RAIZ, "web"))
escribir("TSC", (o if o.strip() else "") + "EXIT=%d\n" % c)

c, o = correr("pnpm test", shell=True, cwd=os.path.join(RAIZ, "web"))
escribir("WEB", o + "\nEXITCODE: %d\n" % c)

print("BLOQUE DE APERTURA COMPLETO")
