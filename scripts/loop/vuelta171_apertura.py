# -*- coding: utf-8 -*-
r"""vuelta171_apertura.py . EL BLOQUE DE APERTURA DE LA VUELTA 171, ENTERO.

CLON DECLARADO de scripts/loop/vuelta170_apertura.py, que a su vez era la suma
declarada de vuelta168_apertura.py (el ciclo de Gate 0 entero y en su orden mas
censo, aristas, desfase, motor, tsc y web) y de vuelta169_apertura.py (el sello
del arbol). Cambia SOLO el numero de vuelta, el prefijo de las salidas y el
bloque H, que mide el reporte en HEAD sin creerle al encargo.

POR QUE SE CORRE AQUI Y NO DONDE EL ENCARGO LO PONE, Y SE DICE EN VEZ DE
CALLARSE: el encargo de la 171 manda un orden de apertura nuevo (1 cerrar el
reporte de la 170, 2 archivarlo, 3 tallar el esqueleto y correr el bloque de
apertura) porque el esqueleto SOBRESCRIBE docs/loop/REPORTE.md. Ese motivo vale
para el ESQUELETO, que escribe en REPORTE.md, y NO vale para este fichero, que
no lo toca: sus salidas son SALIDA_V171_*_APERTURA.txt y ninguna es REPORTE.md.
EJECUTOR.md regla 1 dice "LA APERTURA SE MIDE ANTES DE LA PRIMERA OPERACION", y
esa regla es permanente. Asi que la MEDICION de apertura va aqui, antes de
tocar nada, y el TALLADO del esqueleto va donde el encargo lo pone, despues de
cerrar y archivar el reporte de la 170. Las dos reglas se cumplen enteras.

EL CICLO DE GATE 0 VA ENTERO Y EN SU ORDEN, NUNCA run_phase1 SUELTO.

LO QUE ESTA VUELTA SABE DE SU ARBOL ANTES DE MEDIRLO, PARA NO PODER MAQUILLARLO
DESPUES: git status --porcelain, corrido a mano antes de escribir este fichero,
da DOS lineas: " M dataset/metadata/master_graph.json" y "?? node_modules/". El
encargo predice las dos y manda no commitear ninguna: la primera es suciedad de
indice con diff de cero bytes, la segunda no se toca y no entra en .gitignore
por decision del fundador. La prediccion se escribe AQUI, antes de correr, y el
bloque C/D/E/F de abajo la mide sin saber lo que hay escrito arriba.

USO:
  python scripts/loop/vuelta171_apertura.py
"""
import io
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
PY = sys.executable
VUELTA = 171

RUTAS_DEL_ENCARGO = [
    "dataset/metadata/master_graph.json",
    "docs/loop/REPORTE.md",
    "docs/loop/ACTA_AUDITOR.md",
    "scripts/loop/_v170_cierre_texto.md",
    "docs/loop/SALIDA_V170_BATERIA.txt",
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
w("primera linea: %s" % (rep.split("\n", 1)[0].strip() if rep else "(vacio)"))
w("lineas: %d" % rep.count("\n"))
for marca in ["SIN ESCRIBIR TODAVIA", "PENDIENTE DE TALLAR AL CIERRE",
              "## 3.", "## 4.", "## 5.", "## 6.", "## 7.", "## 8.", "## 9."]:
    w("   contiene %-34s -> %s" % (repr(marca), "SI" if marca in rep else "NO"))
c, stat = git(["show", "--stat", "--format=", "29f04e86"])
w("ficheros que toca el commit 29f04e86 (el que dice llevar el bloque de cierre):")
for l in stat.splitlines():
    if l.strip():
        w("   " + l.strip())
w("   REPORTE.md entre ellos: %s" % ("SI" if "docs/loop/REPORTE.md" in stat else "NO"))
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
