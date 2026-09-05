# -*- coding: utf-8 -*-
r"""vuelta172_apertura.py . EL BLOQUE DE APERTURA DE LA VUELTA 172, ENTERO.

CLON DECLARADO de scripts/loop/vuelta171_apertura.py, que a su vez era clon
declarado de vuelta170_apertura.py. Cambia SOLO el numero de vuelta, el prefijo
de las salidas, la lista RUTAS_DEL_ENCARGO y el bloque H, que aqui mide tres
cosas propias de este encargo: el reporte en HEAD (que sigue siendo el de la
171 sin cerrar), el commit que de verdad toca REPORTE.md por ultima vez, y si
los tres arneses de la 171 estan o no en la nomina de la bateria.

EL BLOQUE H NO TECLEA NINGUN HASH. La vuelta 79 cayo por publicar como commit
de apertura un hash escrito a mano; aqui el commit que toca REPORTE.md se
LOCALIZA con git log -1 -- docs/loop/REPORTE.md y se imprime lo que salga.

POR QUE SE CORRE AQUI Y NO DONDE EL ENCARGO LO PONE, Y SE DICE EN VEZ DE
CALLARSE: el encargo manda cerrar primero el reporte de la 171 (TAREA 1.a) y
solo despues tallar el esqueleto de la 172, que SOBRESCRIBE
docs/loop/REPORTE.md. Ese motivo vale para el ESQUELETO y NO vale para este
fichero, que no toca REPORTE.md: sus salidas son SALIDA_V172_*_APERTURA.txt y
ninguna es REPORTE.md. EJECUTOR.md regla 1 dice "LA APERTURA SE MIDE ANTES DE
LA PRIMERA OPERACION", y esa regla es permanente. Las dos reglas se cumplen
enteras y esta es la misma desviacion declarada que la 171 declaro como su D.1.

EL CICLO DE GATE 0 VA ENTERO Y EN SU ORDEN, NUNCA run_phase1 SUELTO.

LO QUE ESTA VUELTA SABE DE SU ARBOL ANTES DE MEDIRLO, PARA NO PODER MAQUILLARLO
DESPUES: git status --porcelain, corrido a mano al abrir la vuelta, dio TRES
lineas: " M dataset/metadata/master_graph.json", "?? node_modules/" y
"?? docs/loop/SALIDA_V172_AUDITOR_BATERIA.txt". La tercera se commiteo por la
regla 3 de EJECUTOR.md ANTES de correr esto, asi que aqui ya no debe salir; las
otras dos si, y no se commitean. La prediccion se escribe AQUI, antes de
correr, y los bloques C/D/E/F de abajo la miden sin saber lo que hay escrito.

USO:
  python scripts/loop/vuelta172_apertura.py
"""
import io
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
PY = sys.executable
VUELTA = 172

RUTAS_DEL_ENCARGO = [
    "dataset/metadata/master_graph.json",
    "docs/loop/REPORTE.md",
    "docs/loop/ACTA_AUDITOR.md",
    "docs/loop/SALIDA_V171_BATERIA.txt",
    "docs/loop/SALIDA_V171_TALLADOR_CABECERA.txt",
    "docs/loop/SALIDA_V172_AUDITOR_BATERIA.txt",
    "scripts/loop/vuelta171_cierre.py",
    "scripts/loop/vuelta171_tarea5a_mutacion_enchufe.py",
    "scripts/loop/verificar_mutaciones_viejas.py",
    "scripts/loop/vuelta48_contar_ld.py",
    "docs/plan/LECTURAS_DIRIGIDAS.md",
    "docs/PENDIENTES.md",
]


def correr(args, shell=False, cwd=None):
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run(args, cwd=cwd or RAIZ, capture_output=True, env=env, shell=shell)
    out = r.stdout.decode("utf-8", errors="replace") + r.stderr.decode("utf-8", errors="replace")
    return r.returncode, out


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def escribir(nombre, texto):
    ruta = os.path.join(LOOP, "SALIDA_V%d_%s_APERTURA.txt" % (VUELTA, nombre))
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)
    print("ESCRITO: %s (%d bytes)" % (os.path.basename(ruta), len(texto.encode("utf-8"))))


# ---------------------------------------------------------------- A. EL SELLO
lineas = []
w = lineas.append
w("SELLO DE APERTURA DE LA VUELTA %d, escrito ANTES de la primera operacion" % VUELTA)
w("instrumento: scripts/loop/vuelta%d_apertura.py" % VUELTA)
w("")

w("=== A. HEAD DE APERTURA (git rev-parse HEAD) ===")
c, head = git(["rev-parse", "HEAD"])
head = head.strip()
w(head)
c, asunto = git(["log", "-1", "--format=%H%x09%ad%x09%s", "--date=iso"])
w(asunto.strip())
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

w("=== D. BYTES DE CADA RUTA QUE EL ENCARGO NOMBRA ===")
for ruta in RUTAS_DEL_ENCARGO:
    p = os.path.join(RAIZ, ruta.replace("/", os.sep))
    if os.path.exists(p):
        w("%s -> %d bytes" % (ruta, os.path.getsize(p)))
    else:
        w("%s -> NO EXISTE" % ruta)
w("")

w("=== E. DIFF REAL EN BYTES DE LOS MODIFICADOS (cambio contra suciedad) ===")
c, mod = git(["ls-files", "-m"])
for ruta in [l for l in mod.splitlines() if l.strip()]:
    c2, d = git(["diff", "--", ruta])
    w("%s -> diff de %d bytes" % (ruta, len(d.encode("utf-8"))))
    c3, dw = git(["diff", "--ignore-cr-at-eol", "--", ruta])
    w("   %s -> diff ignorando CR de fin de linea: %d bytes" % (ruta, len(dw.encode("utf-8"))))
w("")

w("=== F. LO NO SEGUIDO POR GIT, FICHERO A FICHERO CON SUS BYTES ===")
c, unt = git(["status", "--porcelain", "--untracked-files=all"])
n_unt = 0
for l in unt.splitlines():
    if l.startswith("?? "):
        r = l[3:].strip().strip('"')
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
NL = chr(10)
w("primera linea: %s" % (rep.split(NL, 1)[0].strip() if rep else "(vacio)"))
w("lineas (saltos de linea contados): %d" % rep.count(NL))
w("bytes: %d" % len(rep.encode("utf-8")))
MARCAS = ["SIN ESCRIBIR TODAVIA", "PENDIENTE DE TALLAR AL CIERRE"]
MARCAS = MARCAS + [NL + "## %d." % k for k in range(3, 10)]
for marca in MARCAS:
    w("   contiene %-34s -> %s" % (repr(marca), "SI" if marca in rep else "NO"))
w("")

w("=== H.2 EL COMMIT QUE DE VERDAD TOCA REPORTE.md POR ULTIMA VEZ ===")
w("(no se teclea ningun hash: se localiza con git log y se imprime lo que salga)")
c, cual = git(["log", "--format=%h%x09%s", "-12"])
w("los doce ultimos commits:")
for l in cual.splitlines():
    w("   " + l)
c, ult = git(["log", "-1", "--format=%h", "--", "docs/loop/REPORTE.md"])
w("ultimo commit que TOCA docs/loop/REPORTE.md: %s" % ult.strip())
c, asu = git(["log", "-1", "--format=%s", ult.strip()])
w("   su asunto: %s" % asu.strip()[:110])
w("")

w("=== H.3 LA BATERIA DE LA 171 Y LOS TRES ARNESES, MEDIDOS ===")
for r in ["docs/loop/SALIDA_V171_BATERIA.txt", "docs/loop/SALIDA_V172_AUDITOR_BATERIA.txt"]:
    p = os.path.join(RAIZ, r.replace("/", os.sep))
    w("%s -> %s" % (r, ("%d bytes" % os.path.getsize(p)) if os.path.exists(p) else "NO EXISTE"))
NOM = os.path.join(RAIZ, "scripts", "loop", "verificar_mutaciones_viejas.py")
nomina = io.open(NOM, encoding="utf-8").read()
ARNESES = ["vuelta171_mutacion_busqueda_acta.py", "vuelta171_tarea1a_mutacion_registro.py", "vuelta171_tarea5a_mutacion_enchufe.py"]
for arnes in ARNESES:
    existe = os.path.exists(os.path.join(RAIZ, "scripts", "loop", arnes))
    w("%s -> existe: %s | nombrado en la nomina: %s" % (arnes, "SI" if existe else "NO", "SI" if arnes in nomina else "NO"))
w("")

w("FIN DEL SELLO DE APERTURA")

texto = "\n".join(lineas) + "\n"
io.open(os.path.join(LOOP, "SALIDA_V%d_APERTURA.txt" % VUELTA), "w",
        encoding="utf-8", newline="\n").write(texto)
print(texto)
escribir("HEAD", head + "\n")

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

c, o = correr([PY, "scripts/loop/vuelta85_medir_desfase_calibrado.py", "WORK"])
escribir("DESFASE_CALIBRADO", o + "\nEXITCODE: %d\n" % c)

c, o = correr([PY, "engine/run_all_tests.py"])
escribir("MOTOR", o + "\nEXITCODE: %d\n" % c)

c, o = correr("npx tsc --noEmit -p tsconfig.json", shell=True, cwd=os.path.join(RAIZ, "web"))
escribir("TSC", (o if o.strip() else "") + "EXIT=%d\n" % c)

c, o = correr("pnpm test", shell=True, cwd=os.path.join(RAIZ, "web"))
escribir("WEB", o + "\nEXITCODE: %d\n" % c)

print("BLOQUE DE APERTURA COMPLETO")
