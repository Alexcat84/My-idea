# -*- coding: utf-8 -*-
r"""_auditor_v206_ciclo.py . EL CICLO ENTERO DE GATE 0 CORRIDO POR EL AUDITOR DE
LA VUELTA 206, NUNCA `run_phase1.py` A SECAS.

COMPUTO DE UNA VUELTA, prefijo de guion bajo: fuera del censo, fuera de la
nomina, no roza la moratoria (acta 199 `4.5`, acta 203 `4.6`). No vigila nada.

LOS OCHO COMANDOS SON LOS MISMOS Y EN EL MISMO ORDEN que `_v205_ciclo_gate0.py`
lineas 45 a 79. Escribe en `SALIDA_V206_*_AUDITOR.txt` para NO pisar las del
ejecutor: el cotejo es contra las suyas, y pisarlas seria borrar el sujeto."""
import io, os, re, subprocess, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
PY = sys.executable
PATRON_FILA_NUMSTAT = re.compile(r"^(\d+|-)\t(\d+|-)\t")

def correr(cmd, shell=False, cwd=None):
    r = subprocess.run(cmd, cwd=cwd or RAIZ, shell=shell, capture_output=True)
    o = (r.stdout + r.stderr).decode("utf-8", errors="replace").replace(chr(13) + NL, NL)
    return r.returncode, o

def escribir(seg, texto):
    ruta = os.path.join(LOOP, "SALIDA_V206_%s_AUDITOR.txt" % seg)
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(texto)
    return os.path.getsize(ruta)

def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=== CICLO ENTERO DE GATE 0, CORRIDO POR EL AUDITOR DE LA 206 ===")
    peor = 0
    c, o = correr([PY, "scripts/run_phase1.py", "--reaplico-curaduria"])
    b = escribir("GATE0_CMD1", o + NL + "EXITCODE: %d" % c + NL); peor = max(peor, c)
    print("   1/8 run_phase1.py --reaplico-curaduria  EXITCODE %d | %d bytes" % (c, b))
    c, o = correr([PY, "scripts/etiquetas_de_cara.py", "--aplicar"])
    b = escribir("CICLO_ETIQUETAS", o + NL + "EXITCODE: %d" % c + NL); peor = max(peor, c)
    print("   2/8 etiquetas_de_cara.py --aplicar      EXITCODE %d | %d bytes" % (c, b))
    c, o = correr([PY, "scripts/sync_assets_web.py"])
    b = escribir("CICLO_SYNC", o + NL + "EXITCODE: %d" % c + NL); peor = max(peor, c)
    print("   3/8 sync_assets_web.py                  EXITCODE %d | %d bytes" % (c, b))
    c, o = correr(["git", "diff", "HEAD", "--numstat", "--", "dataset/", "web/", "engine/"])
    b = escribir("CICLO_NUMSTAT", o + NL + "EXITCODE: %d" % c + NL); peor = max(peor, c)
    filas = [x for x in o.split(NL) if PATRON_FILA_NUMSTAT.match(x)]
    print("   4/8 git diff HEAD --numstat             EXITCODE %d | filas %d | %d bytes" % (c, len(filas), b))
    for x in filas:
        print("       FILA: %s" % x)
    c, o = correr([PY, "scripts/loop/vuelta83_conteo_aristas.py", "WORK"])
    b = escribir("CONTEO", o + NL + "EXITCODE: %d" % c + NL); peor = max(peor, c)
    print("   5/8 vuelta83_conteo_aristas.py WORK     EXITCODE %d | %d bytes" % (c, b))
    c, o = correr([PY, "scripts/loop/vuelta85_medir_desfase_calibrado.py", "WORK"])
    b = escribir("DESFASE_CALIBRADO", o + NL + "EXITCODE: %d" % c + NL); peor = max(peor, c)
    print("   6/8 vuelta85_medir_desfase_calibrado    EXITCODE %d | %d bytes" % (c, b))
    c, o = correr([PY, "engine/run_all_tests.py"])
    b = escribir("MOTOR", o + NL + "EXITCODE: %d" % c + NL); peor = max(peor, c)
    print("   7/8 engine/run_all_tests.py             EXITCODE %d | %d bytes" % (c, b))
    c, o = correr("npx tsc --noEmit -p tsconfig.json", shell=True, cwd=os.path.join(RAIZ, "web"))
    b = escribir("TSC", (o if o.strip() else "") + "EXIT=%d" % c + NL); peor = max(peor, c)
    print("   8/8a npx tsc --noEmit                   EXITCODE %d | %d bytes" % (c, b))
    c, o = correr("pnpm test", shell=True, cwd=os.path.join(RAIZ, "web"))
    b = escribir("WEB", o + NL + "EXITCODE: %d" % c + NL); peor = max(peor, c)
    print("   8/8b pnpm test                          EXITCODE %d | %d bytes" % (c, b))
    print("CICLO COMPLETO. PEOR EXITCODE DE LOS OCHO: %d" % peor)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
