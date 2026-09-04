# -*- coding: utf-8 -*-
r"""vuelta168_apertura.py . EL BLOQUE DE APERTURA DE LA VUELTA 168.

POR QUE NACE ASI Y NO A MANO: EJECUTOR.md 1 ("LA APERTURA SE MIDE ANTES DE LA
PRIMERA OPERACION") y la guarda verificar_apertura_sellada.py --vuelta 168,
que exige que TODOS los docs/loop/SALIDA_V168_*_APERTURA.txt nazcan en el
MISMO commit y que ese commit sea HIJO DIRECTO del acta 167 (e3152a9c), o
que el CORREDOR que los separa cumpla las condiciones de la seccion "EL
CORREDOR DE LA PARADA" de esa guarda.

LO QUE ESTA VUELTA SABE DE SU CORREDOR ANTES DE CORRER, Y SE DICE EN VEZ DE
CALLARLO: entre el acta 167 (e3152a9c) y este bloque vive edbc1a48, "Decision
del fundador: el campo estado se jubila, la vara es el instrumento, y las seis
de verdad abren", que es la respuesta a la parada. Toca seis rutas y TRES de
ellas caen fuera de la lista blanca de papeles de parada (docs/loop/AUDITOR.md,
docs/loop/EJECUTOR.md, docs/plan/00_INDICE.md), y docs/loop/PROMPT_SIGUIENTE.md
NO trae el rotulo literal que la adjudicacion 6.8 del acta 155 exige para
admitir un hash. La guarda se corre IGUAL y su salida se pega tal cual: si sale
en rojo, el rojo se publica, no se maquilla ni se arregla tocando el encargo.

CORRECCION DECLARADA POR ADICION (4 sep 2026, tras correr la guarda; el parrafo
de arriba NO se borra porque es lo que se predijo antes de medir y taparlo
impediria auditar la prediccion). LA GUARDA SALIO VERDE, exit 0, salida en
docs/loop/SALIDA_V168_APERTURA_GUARDA.txt. EL PARRAFO DE ARRIBA ACERTO EN LOS
HECHOS Y FALLO EN LA CONCLUSION: es cierto que edbc1a48 toca seis rutas y tres
caen fuera de la lista blanca, y es cierto que el encargo no trae el rotulo (la
propia guarda lo imprime: "rotulo ... NO", "HASHES ADMITIDOS ... 0 (ninguno)").
Lo que el parrafo no sabia es que la ADJUDICACION 6.5 DEL ACTA 161 ya trata a
edbc1a48 como PORTADOR DEL ENCARGO tras la parada y lo deja FUERA del censo de
intrusos, porque hace el papel del acta: es el commit que ABRE la vuelta. Con
eso el corredor medido es de 0 commits y no hay nada que admitir. La leccion es
la de siempre: la vara se lee entera antes de predecir su veredicto.

EL CICLO DE GATE 0 VA ENTERO Y EN SU ORDEN, NUNCA run_phase1 SUELTO (encargo
de la 167, heredado por la 168, que lo dice con esas palabras):
--reaplico-curaduria, etiquetas_de_cara --aplicar, sync_assets_web y DESPUES el
numstat.

USO:
  python scripts/loop/vuelta168_apertura.py
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
    ruta = os.path.join(LOOP, "SALIDA_V168_%s_APERTURA.txt" % nombre)
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)
    print("ESCRITO: %s (%d bytes)" % (os.path.basename(ruta), len(texto.encode("utf-8"))))


# 1. HEAD, leido de git y no tecleado
c, o = correr(["git", "rev-parse", "HEAD"])
escribir("HEAD", o)

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
