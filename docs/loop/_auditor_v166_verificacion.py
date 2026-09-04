# -*- coding: utf-8 -*-
r"""_auditor_v166_verificacion.py . LOS DIEZ COMANDOS, CORRIDOS POR EL AUDITOR.

No verifico la salida del ejecutor leyendola: la RE CORRO. Mismo orden que
vuelta166_cierre.py, ficheros propios con prefijo _auditor_v166_ para no pisar
ni una salida sellada.
"""
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
PY = sys.executable


def correr(args, shell=False, cwd=None):
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run(args, cwd=cwd or RAIZ, capture_output=True, env=env, shell=shell)
    out = r.stdout.decode("utf-8", errors="replace") + r.stderr.decode("utf-8", errors="replace")
    return r.returncode, out


def escribir(nombre, texto):
    ruta = os.path.join(LOOP, "_auditor_v166_%s.txt" % nombre)
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)
    print("ESCRITO: %s (%d bytes)" % (os.path.basename(ruta), len(texto.encode("utf-8"))))
    sys.stdout.flush()


c, o = correr(["git", "rev-parse", "HEAD"])
escribir("head", o)

c, o = correr([PY, "scripts/run_phase1.py", "--reaplico-curaduria"])
escribir("gate0", o + "\nEXITCODE: %d\n" % c)

c, o = correr([PY, "scripts/etiquetas_de_cara.py", "--aplicar"])
escribir("etiquetas", o + "\nEXITCODE: %d\n" % c)

c, o = correr([PY, "scripts/sync_assets_web.py"])
escribir("sync", o + "\nEXITCODE: %d\n" % c)

c, o = correr(["git", "diff", "HEAD", "--numstat", "--", "dataset/", "web/", "engine/"])
escribir("numstat", o + "\nEXITCODE: %d\n" % c)

c, o = correr([PY, "scripts/loop/vuelta83_conteo_aristas.py", "WORK"])
escribir("conteo", o + "\nEXITCODE: %d\n" % c)

c, o = correr([PY, "scripts/loop/vuelta85_medir_desfase_calibrado.py", "WORK"])
escribir("desfase", o + "\nEXITCODE: %d\n" % c)

c, o = correr([PY, "engine/run_all_tests.py"])
escribir("motor", o + "\nEXITCODE: %d\n" % c)

c, o = correr("npx tsc --noEmit -p tsconfig.json", shell=True, cwd=os.path.join(RAIZ, "web"))
escribir("tsc", (o if o.strip() else "") + "EXIT=%d\n" % c)

c, o = correr("pnpm test", shell=True, cwd=os.path.join(RAIZ, "web"))
escribir("web", o + "\nEXITCODE: %d\n" % c)

print("AUDITOR: LOS DIEZ, CORRIDOS")
