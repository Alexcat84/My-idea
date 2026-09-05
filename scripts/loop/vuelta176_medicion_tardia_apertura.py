# -*- coding: utf-8 -*-
r"""vuelta176_medicion_tardia_apertura.py . LAS SEIS MEDICIONES QUE EL TALLADOR
PIDE PARA SU COLUMNA IZQUIERDA, CORRIDAS TARDE Y DICIENDO QUE SE CORRIERON TARDE.

EL NOMBRE DEL FICHERO LLEVA LA VERDAD DENTRO A PROPOSITO: `medicion_tardia`. Esto
NO es un bloque de apertura. Un bloque de apertura se corre ANTES DE LA PRIMERA
OPERACION, y el de esta vuelta NO EXISTE porque no se corrio.

POR QUE PASO, DICHO SIN ADORNO. `AUDITOR.md` 6.1 dice que la vuelta de bateria NO
LLEVA NADA MAS, el encargo traia dos tareas y solo dos, y yo leí que el bloque de
apertura entraba en ese "nada mas". Al llegar al cierre,
`tallar_cabecera_reporte.py --fase04 --vuelta 176` se nego a tallar NADA con
**18 celdas que no se pudieron leer, las 18 del lado APERTURA**, y sin tabla
`cerrar_reporte.py` no puede cerrar el reporte. O sea que aquella lectura mia
BLOQUEA la TAREA 2, y eso ya no es un discutible: es una caida mia y va contada
como tal en la seccion 8 del reporte.

LO QUE NO HAGO, Y ES LO QUE IMPORTA: **NO FABRICO UNA APERTURA**. `EJECUTOR.md` 1
dice, desde la caida de la vuelta 29, que *"el estado TRAS la primera operacion ya
es estado intermedio, no apertura, y se cita como tal"*. Escribir estos ficheros y
callarme seria exactamente esa caida, y ademas con el nombre del fichero mintiendo
por mi.

ENTONCES, ?POR QUE VALEN ESTAS CIFRAS PARA LA COLUMNA IZQUIERDA? PORQUE EL SUJETO
QUE MIDEN NO SE HA MOVIDO, Y ESO ES UNA MEDICION Y NO UNA SUPOSICION. Los seis
instrumentos leen `dataset/`, `web/` y `engine/`, y entre el HEAD de apertura y el
de cierre esos tres arboles son IDENTICOS: `git diff <apertura>..<cierre> --numstat
-- dataset/ web/ engine/` devuelve **CERO FILAS**. Esta comprobacion se corre AQUI
DENTRO, se publica en la salida y **si diera una sola fila este fichero CAE EN
ROJO y no escribe nada**, porque entonces las cifras de hoy no serian las de la
apertura y pegarlas en esa columna seria mentir.

LA DIFERENCIA CON LA CAIDA DE LA VUELTA 29, para que se pueda juzgar y no haya que
creerme: alli la cifra citada como apertura era el estado DESPUES de una operacion
QUE LA HABIA MOVIDO. Aqui se prueba, con el instrumento y delante, que ninguna
operacion de esta vuelta movio el sujeto. Lo que esta vuelta toco fue
`scripts/loop/` y `docs/loop/`, y ninguno de estos seis instrumentos los lee.

QUE ESCRIBE: los seis `SALIDA_V176_*_APERTURA.txt` que el tallador nombra, mas
`docs/loop/SALIDA_V176_APERTURA_MEDIDA_TARDE.txt`, que es la declaracion entera
con su prueba. La declaracion se escribe SIEMPRE, salga verde o rojo.

USO:
  python scripts/loop/vuelta176_medicion_tardia_apertura.py
"""
import io
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
PY = sys.executable
NL = chr(10)


def correr(args, shell=False, cwd=None):
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run(args, cwd=cwd or RAIZ, capture_output=True, env=env, shell=shell)
    out = (r.stdout.decode("utf-8", errors="replace")
           + r.stderr.decode("utf-8", errors="replace"))
    return r.returncode, out


def escribir(nombre, texto):
    ruta = os.path.join(LOOP, "SALIDA_V176_%s_APERTURA.txt" % nombre)
    with io.open(ruta, "w", encoding="utf-8", newline=NL) as f:
        f.write(texto)
    print("ESCRITO: %s (%d bytes)" % (os.path.basename(ruta), len(texto.encode("utf-8"))))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("MEDICION TARDIA. ESTO NO ES UN BLOQUE DE APERTURA Y NO SE LLAMA ASI.")
    print("=" * 78)

    r_ap = os.path.join(LOOP, "SALIDA_V176_HEAD_APERTURA.txt")
    r_ci = os.path.join(LOOP, "SALIDA_V176_HEAD_CIERRE.txt")
    faltan = [os.path.basename(r) for r in (r_ap, r_ci) if not os.path.exists(r)]
    declaracion = []
    w = declaracion.append
    w("LA COLUMNA IZQUIERDA DE LA CABECERA DE LA VUELTA 176 SE MIDIO TARDE")
    w("=" * 78)
    w("")
    w("NO HUBO BLOQUE DE APERTURA EN ESTA VUELTA. No se corrio, y por eso el")
    w("tallador se nego a tallar nada con 18 celdas ilegibles, las 18 del lado")
    w("APERTURA. Estas seis mediciones se corrieron AL CIERRE, DESPUES de todas")
    w("las operaciones de la vuelta, y se dice aqui en vez de dejar que el")
    w("sufijo _APERTURA del nombre del fichero lo diga por mi.")
    w("")
    if faltan:
        w("ROJO: faltan los sellos %s. No se escribe nada." % ", ".join(faltan))
        io.open(os.path.join(LOOP, "SALIDA_V176_APERTURA_MEDIDA_TARDE.txt"),
                "w", encoding="utf-8", newline=NL).write(NL.join(declaracion) + NL)
        print("ROJO: faltan los sellos %s" % ", ".join(faltan))
        return 1
    apertura = io.open(r_ap, encoding="utf-8").read().strip()
    cierre = io.open(r_ci, encoding="utf-8").read().strip()

    w("LOS DOS EXTREMOS, LEIDOS DE SUS SELLOS:")
    w("   apertura: %s" % apertura)
    w("   cierre  : %s" % cierre)
    w("")
    w("LA PRUEBA DE QUE ESTAS CIFRAS SIRVEN IGUAL, Y ES UNA MEDICION Y NO UNA")
    w("SUPOSICION. Los seis instrumentos leen dataset/, web/ y engine/. Si esos")
    w("tres arboles no se movieron entre los dos extremos, lo que se mide hoy es")
    w("lo mismo que se habria medido en la apertura.")
    w("")
    c, numstat = correr(["git", "diff", "--numstat", "%s..%s" % (apertura, cierre),
                         "--", "dataset/", "web/", "engine/"])
    filas = [l for l in numstat.splitlines()
             if l.strip() and chr(9) in l and l.split(chr(9))[0].strip().isdigit()]
    w("   git diff --numstat %s..%s -- dataset/ web/ engine/" % (apertura[:8], cierre[:8]))
    w("   CIFRA filas: %d" % len(filas))
    for l in filas:
        w("      FILA: %s" % l)
    if not filas:
        w("      (ninguna fila)")
    w("")
    print("CIFRA filas de numstat entre los dos extremos: %d" % len(filas))

    if filas:
        w("ROJO: el sujeto SI se movio entre los dos extremos, o sea que las cifras")
        w("de hoy NO son las de la apertura. Este fichero NO escribe ninguna salida")
        w("_APERTURA, porque pegarlas en esa columna seria mentir.")
        io.open(os.path.join(LOOP, "SALIDA_V176_APERTURA_MEDIDA_TARDE.txt"),
                "w", encoding="utf-8", newline=NL).write(NL.join(declaracion) + NL)
        print("ROJO: el sujeto se movio. No se escribe ninguna salida _APERTURA.")
        return 1

    w("CERO FILAS: dataset/, web/ y engine/ son IDENTICOS en los dos extremos. Lo")
    w("que esta vuelta toco fue scripts/loop/ y docs/loop/, y ninguno de estos seis")
    w("instrumentos los lee. Por eso estas cifras valen para la columna izquierda,")
    w("Y AUN ASI SE DECLARA QUE SE MIDIERON TARDE, porque la regla de EJECUTOR.md 1")
    w("sobre la apertura no se cumple diciendo que da igual: se cumple diciendo la")
    w("verdad y poniendo la prueba al lado.")
    w("")
    w("LA CAIDA ES MIA Y VA CONTADA EN LA SECCION 8 DEL REPORTE DE LA VUELTA.")

    # EL CICLO DE GATE 0 VA ENTERO Y EN SU ORDEN, NUNCA `run_phase1` SUELTO.
    # ESTO SE ESCRIBE ASI PORQUE YA SE PAGO DOS VECES: la vuelta 170 lo corrio
    # suelto y el guardian del commit la cazo con 71 nodos divergentes de
    # `etiqueta_arbol`, y ESTA MISMA VUELTA lo volvio a hacer en la primera
    # version de este fichero, que corria el paso 1 y saltaba al motor. El motor
    # salio en rojo con los mismos 71 nodos y la guarda de la TAREA 1.a mordio
    # sobre el arbol de verdad con 72 lineas cambiadas en
    # `dataset/metadata/master_graph.json`. La evidencia esta en
    # `docs/loop/SALIDA_V176_T1A_GUARDA_MORDIO_DE_VERDAD.txt` y no se borra.
    #   1) run_phase1.py --reaplico-curaduria
    #   2) etiquetas_de_cara.py --aplicar   <- reaplica la curaduria de cara
    #   3) sync_assets_web.py               <- la lleva a la copia web
    #   4) git diff HEAD --numstat -- dataset/ web/ engine/  <- SIN FILAS
    print("")
    c, o = correr([PY, "scripts/run_phase1.py", "--reaplico-curaduria"])
    escribir("GATE0_CMD1", o + NL + "EXITCODE: %d" % c + NL)
    c, o = correr([PY, "scripts/etiquetas_de_cara.py", "--aplicar"])
    escribir("CICLO_ETIQUETAS", o + NL + "EXITCODE: %d" % c + NL)
    c, o = correr([PY, "scripts/sync_assets_web.py"])
    escribir("CICLO_SYNC", o + NL + "EXITCODE: %d" % c + NL)
    c, o = correr(["git", "diff", "HEAD", "--numstat", "--",
                   "dataset/", "web/", "engine/"])
    escribir("CICLO_NUMSTAT", o + NL + "EXITCODE: %d" % c + NL)
    c, o = correr([PY, "scripts/loop/vuelta83_conteo_aristas.py", "WORK"])
    escribir("CONTEO", o + NL + "EXITCODE: %d" % c + NL)
    c, o = correr([PY, "scripts/loop/vuelta85_medir_desfase_calibrado.py", "WORK"])
    escribir("DESFASE_CALIBRADO", o + NL + "EXITCODE: %d" % c + NL)
    c, o = correr([PY, "engine/run_all_tests.py"])
    escribir("MOTOR", o + NL + "EXITCODE: %d" % c + NL)
    c, o = correr("npx tsc --noEmit -p tsconfig.json", shell=True,
                  cwd=os.path.join(RAIZ, "web"))
    escribir("TSC", (o if o.strip() else "") + "EXIT=%d" % c + NL)
    c, o = correr("pnpm test", shell=True, cwd=os.path.join(RAIZ, "web"))
    escribir("WEB", o + NL + "EXITCODE: %d" % c + NL)

    io.open(os.path.join(LOOP, "SALIDA_V176_APERTURA_MEDIDA_TARDE.txt"),
            "w", encoding="utf-8", newline=NL).write(NL.join(declaracion) + NL)
    print("")
    print("ESCRITA LA DECLARACION: SALIDA_V176_APERTURA_MEDIDA_TARDE.txt")
    print("MEDICION TARDIA COMPLETA. NO ES UNA APERTURA Y ESTA DICHO.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
