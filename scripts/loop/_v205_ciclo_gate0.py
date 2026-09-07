# -*- coding: utf-8 -*-
r"""_v205_ciclo_gate0.py . EL CICLO ENTERO DE GATE 0 DE LA VUELTA 205, NUNCA
`run_phase1.py` A SECAS.

COMPUTO DE UNA VUELTA, prefijo de guion bajo: fuera del censo, fuera de la
nomina, no roza la moratoria (acta 199 `4.5`, acta 203 `4.6`). No vigila nada.

LOS OCHO COMANDOS SON LOS MISMOS Y EN EL MISMO ORDEN que corrio la vuelta 204 en
`scripts/loop/_v204_apertura.py`, lineas 470 a 504. NO SE ELIGEN AQUI: se copian
de ese bloque, que es el que el acta 204 reprodujo al digito.

USO:  python scripts/loop/_v205_ciclo_gate0.py APERTURA
      python scripts/loop/_v205_ciclo_gate0.py CIERRE"""
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
PY = sys.executable
VUELTA = int(re.match(r"^_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))
PATRON_FILA_NUMSTAT = re.compile(r"^(\d+|-)\t(\d+|-)\t")


def correr(cmd, shell=False, cwd=None):
    r = subprocess.run(cmd, cwd=cwd or RAIZ, shell=shell, capture_output=True)
    o = (r.stdout + r.stderr).decode("utf-8", errors="replace").replace(chr(13) + NL, NL)
    return r.returncode, o


def escribir(seg, lado, texto):
    ruta = os.path.join(LOOP, "SALIDA_V%d_%s_%s.txt" % (VUELTA, seg, lado))
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(texto)
    return os.path.getsize(ruta)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    lado = sys.argv[1].upper()
    if lado not in ("APERTURA", "CIERRE"):
        print("ROJO: el lado tiene que ser APERTURA o CIERRE.")
        return 1
    print("=== EL CICLO ENTERO DE GATE 0, LADO %s, NUNCA run_phase1.py A SECAS ===" % lado)
    peor = 0
    c, o = correr([PY, "scripts/run_phase1.py", "--reaplico-curaduria"])
    b = escribir("GATE0_CMD1", lado, o + NL + "EXITCODE: %d" % c + NL)
    print("   1/8 run_phase1.py --reaplico-curaduria  EXITCODE %d | %d bytes" % (c, b)); peor = max(peor, c)
    c, o = correr([PY, "scripts/etiquetas_de_cara.py", "--aplicar"])
    b = escribir("CICLO_ETIQUETAS", lado, o + NL + "EXITCODE: %d" % c + NL)
    print("   2/8 etiquetas_de_cara.py --aplicar      EXITCODE %d | %d bytes" % (c, b)); peor = max(peor, c)
    c, o = correr([PY, "scripts/sync_assets_web.py"])
    b = escribir("CICLO_SYNC", lado, o + NL + "EXITCODE: %d" % c + NL)
    print("   3/8 sync_assets_web.py                  EXITCODE %d | %d bytes" % (c, b)); peor = max(peor, c)
    c, o = correr(["git", "diff", "HEAD", "--numstat", "--", "dataset/", "web/", "engine/"])
    b = escribir("CICLO_NUMSTAT", lado, o + NL + "EXITCODE: %d" % c + NL)
    filas = [x for x in o.split(NL) if PATRON_FILA_NUMSTAT.match(x)]
    print("   4/8 git diff HEAD --numstat             EXITCODE %d | filas %d | %d bytes"
          % (c, len(filas), b)); peor = max(peor, c)
    for x in filas:
        print("       FILA: %s" % x)
    c, o = correr([PY, "scripts/loop/vuelta83_conteo_aristas.py", "WORK"])
    b = escribir("CONTEO", lado, o + NL + "EXITCODE: %d" % c + NL)
    print("   5/8 vuelta83_conteo_aristas.py WORK     EXITCODE %d | %d bytes" % (c, b)); peor = max(peor, c)
    c, o = correr([PY, "scripts/loop/vuelta85_medir_desfase_calibrado.py", "WORK"])
    b = escribir("DESFASE_CALIBRADO", lado, o + NL + "EXITCODE: %d" % c + NL)
    print("   6/8 vuelta85_medir_desfase_calibrado    EXITCODE %d | %d bytes" % (c, b)); peor = max(peor, c)
    c, o = correr([PY, "engine/run_all_tests.py"])
    b = escribir("MOTOR", lado, o + NL + "EXITCODE: %d" % c + NL)
    print("   7/8 engine/run_all_tests.py             EXITCODE %d | %d bytes" % (c, b)); peor = max(peor, c)
    c, o = correr("npx tsc --noEmit -p tsconfig.json", shell=True, cwd=os.path.join(RAIZ, "web"))
    b = escribir("TSC", lado, (o if o.strip() else "") + "EXIT=%d" % c + NL)
    print("   8/8a npx tsc --noEmit                   EXITCODE %d | %d bytes" % (c, b)); peor = max(peor, c)
    c, o = correr("pnpm test", shell=True, cwd=os.path.join(RAIZ, "web"))
    b = escribir("WEB", lado, o + NL + "EXITCODE: %d" % c + NL)
    print("   8/8b pnpm test                          EXITCODE %d | %d bytes" % (c, b)); peor = max(peor, c)
    print("CICLO DE %s COMPLETO. PEOR EXITCODE DE LOS OCHO: %d" % (lado, peor))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
