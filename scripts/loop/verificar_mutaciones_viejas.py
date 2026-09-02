# -*- coding: utf-8 -*-
"""verificar_mutaciones_viejas.py . LAS CUATRO MUTACIONES VIEJAS, EN EL CICLO DE
CIERRE DE CADA VUELTA, Y ANCLA PERDIDA CUENTA COMO ROJO.

NOMBRE ESTABLE, SIN NUMERO DE VUELTA, como verificar_apertura_sellada.py y
tallar_cabecera_reporte.py: se corre igual en toda vuelta y no se clona.

POR QUE NACE (encargo de la vuelta 138, TAREA 2.b, ultimo parrafo: "LA GUARDA
PARA QUE NO VUELVA A PASAR: las cuatro mutaciones viejas entran en el ciclo de
cierre de cada vuelta, y a partir de que esten re-ancladas, ANCLA PERDIDA cuenta
como ROJO"). Tres de las cuatro (vuelta135_2e_mutacion_1, _2 y _3) estaban
ancladas a un literal de docs/loop/REPORTE.md, que se sobreescribe cada vuelta:
desde la 135 caian con "ROJO PREVIO" sin llegar a probar nada, y nadie lo
midio hasta la mutacion D de la vuelta 137. La 2.b de la vuelta 138 las
re-anclo a docs/loop/SUJETO_FIJO_V135_2E_REPORTE_134.md, un sujeto propio y
congelado que ellas mismas cotejan contra el blob del acta 134 en cada corrida.

LA DIFERENCIA CON LA MUTACION D DE LA VUELTA 137, dicha con todas sus letras:
aquella distinguia LA GUARDA NO MORDIO (fallo de verdad) de ANCLA PERDIDA (la
mutacion no llega a correr), y hacia BIEN en distinguirlas, porque entonces las
tres estaban desancladas y contarlo como fallo de la guarda habria sido mentir
en la otra direccion. DESDE QUE ESTAN RE-ANCLADAS ESA DISTINCION SE ACABA: una
mutacion que no encuentra su sujeto es una guarda que no mide, y aqui es ROJO.

QUE COMPRUEBA. Corre las cuatro y exige EXIT 0 de cada una. Clasifica:
  OK             . exit 0, la mutacion corrio y mordio.
  ANCLA PERDIDA  . la salida trae "ROJO PREVIO": el sujeto no esta o no es el
                   que la mutacion espera. ROJO.
  NO MORDIO      . exit distinto de 0 sin "ROJO PREVIO": la guarda que la
                   mutacion prueba dejo de morder. ROJO.

PRUEBA DE MUTACION (EJECUTOR regla 1, sobre una variable QUE EL CODIGO COMPUTA):
--mutar-ancla fabrica una copia del sujeto fijo CON EL ANCLA ARRANCADA en un
directorio temporal, apunta alli las tres re-ancladas con --sujeto, y exige que
las tres salgan clasificadas como ANCLA PERDIDA y que el veredicto sea ROJO. La
variable del veredicto es la lista `perdidas`, construida leyendo la salida real
de cada proceso; no hay ningun literal comparado consigo mismo. P.16, QUIEN
FABRICA LIMPIA: la copia temporal se retira siempre.

USO:
  python scripts/loop/verificar_mutaciones_viejas.py
  python scripts/loop/verificar_mutaciones_viejas.py --mutar-ancla
"""
import argparse
import io
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "scripts", "loop")
SUJETO_FIJO = os.path.join(RAIZ, "docs", "loop", "SUJETO_FIJO_V135_2E_REPORTE_134.md")

# Las CUATRO. La primera fabrica su propio reporte y nunca estuvo anclada a
# REPORTE.md, por eso no admite --sujeto y no entra en la prueba del ancla.
VIEJAS = [
    ("vuelta133_tarea2e_mutacion_cifras.py", False),
    ("vuelta135_2e_mutacion_1.py", True),
    ("vuelta135_2e_mutacion_2.py", True),
    ("vuelta135_2e_mutacion_3.py", True),
]

# EL ANCLA QUE SE ARRANCA en --mutar-ancla. Es el literal que las tres buscan.
ANCLAS = ["118 grafias (sin instrumento)", "54 grupos (sin instrumento)"]


def correr(script, sujeto=None):
    cmd = [sys.executable, os.path.join(LOOP, script)]
    if sujeto:
        cmd += ["--sujeto", sujeto]
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=RAIZ)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def clasificar(codigo, salida):
    if codigo == 0:
        return "OK"
    if "ROJO PREVIO" in salida:
        return "ANCLA PERDIDA"
    return "NO MORDIO"


def primera_linea_util(salida):
    for l in salida.splitlines():
        if l.strip():
            return l.strip()[:150]
    return "(sin salida)"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutar-ancla", dest="mutar", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 78)
    print("LAS CUATRO MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO.")
    if a.mutar:
        print("MODO MUTACION: sujeto con el ancla arrancada. TIENE QUE DAR ROJO.")
    print("=" * 78)

    sujeto = None
    tmp = None
    try:
        if a.mutar:
            if not os.path.exists(SUJETO_FIJO):
                print("ROJO: no existe el sujeto fijo %s." % SUJETO_FIJO)
                return 1
            tmp = tempfile.mkdtemp(prefix="ancla_arrancada_")
            texto = io.open(SUJETO_FIJO, encoding="utf-8").read()
            arrancadas = 0
            for ancla in ANCLAS:
                if ancla in texto:
                    texto = texto.replace(ancla, "CIFRA ARRANCADA POR LA PRUEBA DE MUTACION")
                    arrancadas += 1
            print("  anclas arrancadas de la copia: %d de %d" % (arrancadas, len(ANCLAS)))
            if arrancadas != len(ANCLAS):
                print("ROJO: el sujeto fijo no traia las %d anclas. PARADA." % len(ANCLAS))
                return 1
            sujeto = os.path.join(tmp, "SUJETO_CON_EL_ANCLA_ARRANCADA.md")
            io.open(sujeto, "w", encoding="utf-8", newline="\n").write(texto)
            print("  copia con el ancla arrancada: %s" % sujeto)

        filas = []
        for script, admite_sujeto in VIEJAS:
            usar = sujeto if (a.mutar and admite_sujeto) else None
            codigo, salida = correr(script, usar)
            estado = clasificar(codigo, salida)
            filas.append((script, codigo, estado, primera_linea_util(salida)))
    finally:
        if tmp:
            shutil.rmtree(tmp, ignore_errors=True)
            print("  P.16: la copia temporal se retira. Existe todavia: %s" % os.path.exists(tmp))

    print("")
    for script, codigo, estado, prim in filas:
        print("  %-38s exit %d  %-14s" % (script, codigo, estado))
        if estado != "OK":
            print("      %s" % prim)

    perdidas = [s for s, _, e, _ in filas if e == "ANCLA PERDIDA"]
    no_mordio = [s for s, _, e, _ in filas if e == "NO MORDIO"]
    print("")
    print("  ANCLA PERDIDA: %d (%s)" % (len(perdidas), ", ".join(perdidas) or "ninguna"))
    print("  NO MORDIO    : %d (%s)" % (len(no_mordio), ", ".join(no_mordio) or "ninguna"))

    if a.mutar:
        esperadas = [s for s, admite in VIEJAS if admite]
        bien = sorted(perdidas) == sorted(esperadas)
        print("")
        if bien:
            print("VERDE DE LA MUTACION: las %d re-ancladas caen como ANCLA PERDIDA cuando se"
                  % len(esperadas))
            print("les arranca el ancla, y el veredicto de esta guarda seria ROJO.")
            print("FIN")
            return 0
        print("ROJO DE LA MUTACION: se esperaban %d ANCLA PERDIDA (%s) y salieron %d (%s)."
              % (len(esperadas), ", ".join(esperadas), len(perdidas), ", ".join(perdidas)))
        print("FIN")
        return 1

    if perdidas or no_mordio:
        print("")
        print("ROJO: %d con el ancla perdida y %d que no mordieron."
              % (len(perdidas), len(no_mordio)))
        print("FIN")
        return 1
    print("")
    print("VERDE: las %d mutaciones viejas corren y muerden." % len(filas))
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
