# -*- coding: utf-8 -*-
r"""vuelta169_apertura.py . SELLA EL ESTADO DE APERTURA DE LA VUELTA 169 ANTES
DE LA PRIMERA OPERACION.

POR QUE NACE ASI (EJECUTOR.md regla 1, "LA APERTURA SE MIDE ANTES DE LA PRIMERA
OPERACION", 14 ago 2026): el estado TRAS la primera operacion ya es estado
intermedio, no apertura. Esta vuelta abre ademas con ARBOL SUCIO heredado de la
168, que se corto, y el encargo ordena tratar esos ficheros DENTRO de la TAREA 1
en vez de barrerlos de golpe: por eso su estado exacto (nombre, bytes, si git los
ve) se sella AQUI, antes de tocarlos, o luego no habria forma de probar que
`SALIDA_V168_T3_BATERIA_CIERRE.txt` estaba en CERO BYTES.

LO QUE SELLA, TODO LEIDO Y NADA TECLEADO:
  A. HEAD de apertura, de `git rev-parse HEAD`.
  B. rama, de `git rev-parse --abbrev-ref HEAD`, y su remoto.
  C. `git status --porcelain` entero.
  D. cada ruta no commiteada con sus BYTES y su marca de tiempo.
  E. el diff real de los ficheros que git marca como modificados, en bytes, para
     distinguir una modificacion de verdad de una suciedad de finales de linea.
  F. `git ls-tree` de las rutas que el encargo manda commitear, para probar cual
     esta y cual no esta en el arbol de HEAD.

USO:
  python scripts/loop/vuelta169_apertura.py
"""
import io
import os
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")

RUTAS_DEL_ENCARGO = [
    "docs/loop/SALIDA_V168_T3_BATERIA_CIERRE.txt",
    "scripts/loop/_v168_cierre_tmp.py",
    "dataset/metadata/master_graph.json",
]


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


lineas = []
w = lineas.append

w("SELLO DE APERTURA DE LA VUELTA 169, escrito ANTES de la primera operacion")
w("instrumento: scripts/loop/vuelta169_apertura.py")
w("")

w("=== A. HEAD DE APERTURA (git rev-parse HEAD) ===")
c, head = git(["rev-parse", "HEAD"])
head = head.strip()
w(head)
c, asunto = git(["log", "-1", "--format=%H%x09%ad%x09%s", "--date=iso"])
w(asunto.strip())
w("")

w("=== B. RAMA Y REMOTO ===")
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

w("=== E. DIFF REAL EN BYTES DE LOS MODIFICADOS (para distinguir cambio de suciedad) ===")
c, mod = git(["ls-files", "-m"])
for ruta in [l for l in mod.splitlines() if l.strip()]:
    c2, d = git(["diff", "--", ruta])
    w("%s -> diff de %d bytes" % (ruta, len(d.encode("utf-8"))))
    c3, dw = git(["diff", "--ignore-cr-at-eol", "--", ruta])
    w("   %s -> diff ignorando CR de fin de linea: %d bytes" % (ruta, len(dw.encode("utf-8"))))
w("")

w("=== F. git ls-tree DE HEAD SOBRE ESAS RUTAS (que esta y que no esta en el arbol) ===")
for ruta in RUTAS_DEL_ENCARGO:
    c, t = git(["ls-tree", "HEAD", "--", ruta])
    w("%s -> %s" % (ruta, t.strip() if t.strip() else "NO ESTA EN EL ARBOL DE HEAD"))
w("")

w("FIN DEL SELLO DE APERTURA")

texto = "\n".join(lineas) + "\n"
io.open(os.path.join(LOOP, "SALIDA_V169_APERTURA.txt"), "w", encoding="utf-8", newline="\n").write(texto)
io.open(os.path.join(LOOP, "SALIDA_V169_HEAD_APERTURA.txt"), "w", encoding="utf-8", newline="\n").write(head + "\n")
print(texto)
print("ESCRITO: docs/loop/SALIDA_V169_APERTURA.txt (%d bytes)" % len(texto.encode("utf-8")))
print("ESCRITO: docs/loop/SALIDA_V169_HEAD_APERTURA.txt (%s)" % head)
