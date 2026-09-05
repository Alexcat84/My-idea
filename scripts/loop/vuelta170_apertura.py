# -*- coding: utf-8 -*-
r"""vuelta170_apertura.py . EL BLOQUE DE APERTURA DE LA VUELTA 170, ENTERO.

POR QUE NACE ASI, Y ES LA CAIDA 1 QUE LA VUELTA 169 SE PUSO Y NO CAZO A TIEMPO:
la 169 sello el HEAD y nada mas (scripts/loop/vuelta169_apertura.py, commit
8404495d), y SELLAR EL HEAD NO ES SELLAR LA APERTURA. Sin GATE0_CMD1, CONTEO,
DESFASE_CALIBRADO, MOTOR, TSC y WEB del lado APERTURA, el tallador de la
cabecera (--fase04) no puede leer la mitad izquierda de su tabla y sale en rojo
con las celdas ilegibles. La 169 publico ese rojo entero en vez de rellenarlo a
mano, e hizo bien; el remedio no es publicarlo mejor, es CORRER EL BLOQUE.

Este fichero es, por tanto, la SUMA DECLARADA de dos antecesores, y ninguno de
los dos se pierde:
  - scripts/loop/vuelta168_apertura.py, que trae el ciclo de Gate 0 entero y en
    su orden (--reaplico-curaduria, etiquetas_de_cara --aplicar, sync_assets_web
    y DESPUES el numstat) mas censo, aristas, desfase, motor, tsc y web;
  - scripts/loop/vuelta169_apertura.py, que trae el SELLO del arbol (rama,
    remoto, status entero, bytes por ruta, diff en bytes de los modificados y
    ls-tree), y que en esta vuelta hace falta igual porque el arbol vuelve a
    abrir sucio.

EL CICLO DE GATE 0 VA ENTERO Y EN SU ORDEN, NUNCA run_phase1 SUELTO.

LO QUE ESTA VUELTA SABE DE SU ARBOL ANTES DE MEDIRLO, PARA NO PODER MAQUILLARLO
DESPUES: git status --porcelain, corrido a mano antes de escribir este fichero,
da DOS lineas: ` M dataset/metadata/master_graph.json` y `?? node_modules/`. El
encargo predice la primera (suciedad de indice con diff de cero bytes, como la
169 midio) y manda tratar la segunda dentro de la TAREA 1. La prediccion se
escribe AQUI, antes de correr, y el bloque D/E/F de abajo la mide sin saber lo
que hay escrito arriba.

USO:
  python scripts/loop/vuelta170_apertura.py
"""
import io
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
PY = sys.executable

RUTAS_DEL_ENCARGO = [
    "dataset/metadata/master_graph.json",
    "docs/loop/REPORTE.md",
    "docs/loop/ACTA_AUDITOR.md",
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
    ruta = os.path.join(LOOP, "SALIDA_V170_%s_APERTURA.txt" % nombre)
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)
    print("ESCRITO: %s (%d bytes)" % (os.path.basename(ruta), len(texto.encode("utf-8"))))


# ---------------------------------------------------------------- A. EL SELLO
lineas = []
w = lineas.append
w("SELLO DE APERTURA DE LA VUELTA 170, escrito ANTES de la primera operacion")
w("instrumento: scripts/loop/vuelta170_apertura.py")
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
w("FIN DEL SELLO DE APERTURA")

texto = "\n".join(lineas) + "\n"
io.open(os.path.join(LOOP, "SALIDA_V170_APERTURA.txt"), "w", encoding="utf-8", newline="\n").write(texto)
print(texto)
escribir("HEAD", head + "\n")

# ------------------------------------------------- B. EL BLOQUE DE MEDICIONES
# 2. GATE 0, paso 1 del ciclo
c, o = correr([PY, "scripts/run_phase1.py", "--reaplico-curaduria"])
escribir("GATE0_CMD1", o + "\nEXITCODE: %d\n" % c)

# 3. ciclo, paso 2
c, o = correr([PY, "scripts/etiquetas_de_cara.py", "--aplicar"])
escribir("CICLO_ETIQUETAS", o + "\nEXITCODE: %d\n" % c)

# 4. ciclo, paso 3
c, o = correr([PY, "scripts/sync_assets_web.py"])
escribir("CICLO_SYNC", o + "\nEXITCODE: %d\n" % c)

# 5. ciclo, paso 4: el numstat, DESPUES de los tres anteriores
c, o = correr(["git", "diff", "HEAD", "--numstat", "--", "dataset/", "web/", "engine/"])
escribir("CICLO_NUMSTAT", o + "\nEXITCODE: %d\n" % c)

# 6. censo y aristas
c, o = correr([PY, "scripts/loop/vuelta83_conteo_aristas.py", "WORK"])
escribir("CONTEO", o + "\nEXITCODE: %d\n" % c)

# 7. desfase del calibrado
c, o = correr([PY, "scripts/loop/vuelta85_medir_desfase_calibrado.py", "WORK"])
escribir("DESFASE_CALIBRADO", o + "\nEXITCODE: %d\n" % c)

# 8. motor
c, o = correr([PY, "engine/run_all_tests.py"])
escribir("MOTOR", o + "\nEXITCODE: %d\n" % c)

# 9. tsc
c, o = correr("npx tsc --noEmit -p tsconfig.json", shell=True, cwd=os.path.join(RAIZ, "web"))
escribir("TSC", (o if o.strip() else "") + "EXIT=%d\n" % c)

# 10. suites de la web
c, o = correr("pnpm test", shell=True, cwd=os.path.join(RAIZ, "web"))
escribir("WEB", o + "\nEXITCODE: %d\n" % c)

print("BLOQUE DE APERTURA COMPLETO")
