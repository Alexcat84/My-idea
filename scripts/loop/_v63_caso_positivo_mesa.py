# -*- coding: utf-8 -*-
"""_v63_caso_positivo_mesa.py . EL CASO POSITIVO DE LOS DOS INSTRUMENTOS QUE
NACEN EN LA VUELTA 63: generar_plan_de_fusion_de_mesa.py y fundir_por_plan.py.

POR QUE HACE FALTA ADEMAS DEL HEREDADO. El caso positivo heredado
(scripts/loop/vuelta57_caso_positivo.py) pone a fallar las guardas del ANCESTRO,
scripts/loop/vuelta49_fundir_tramo.py, y se re-corre entero en esta vuelta como
contraste. Pero NO toca ni el generador de mesa ni el fundidor nuevo, y una
guarda que solo se declara verde no se sabe si muerde. Esto lo cubre.

LA REGLA DE TRABAJO SE MANTIENE, que es la del acta 54, pregunta 7: EL CASO
POSITIVO SE FABRICA SOBRE UN ACTO QUE LA PROPIA VUELTA NO VAYA A TOCAR, para que
no caduque. Aqui el sujeto es OP-M-03-II (pivote_o_proceder absorbe
pivotar_o_proceder), que es la fusion de mesa siguiente de la misma mesa del
pivote, con LOS DOS MIEMBROS VIVOS hoy, y que esta vuelta NO ejecuta: la vuelta
63 ejecuta OP-M-03-I y OP-M-02-PROG, y ninguna de las dos la nombra.

LAS OCHO MENTIRAS, y cada una AISLA UNA guarda:
  por el GENERADOR de mesa (que en todas ellas tiene que caer sin escribir plan)
    1. el contenido nombra un SUPERVIVIENTE que la ficha no escribe
    2. el contenido nombra un ABSORBIDO que la ficha no escribe
    3. cobertura por OLVIDO: a un paso del que muere le falta la marca
    4. cobertura por SOBRANTE: hay una marca para un paso que no existe
    5. el INCISO no es trozo verbatim del paso que muere
    6. una perdida con ESPECIE desconocida
  por el FUNDIDOR nuevo (siempre en modo SIMULAR, ni en el peor caso toca un nodo)
    7. el plan manda absorber un nodo QUE YA ESTA DEPRECADO (guarda 1)
    8. el plan manda absorber una SEMILLA DE ENTRADA (guarda 1B)
  y una NOVENA que no es una mentira sino LA MITAD POSITIVA DE LA CORRECCION DEL
  TITULO: un plan SIN el campo operacion tiene que imprimir SIN OPERACION
  DECLARADA EN EL PLAN, que es justo lo que el ancestro no podia hacer porque
  llevaba OP-U-01 tallado en el literal.

LOS PLANES DE MENTIRA SE ESCRIBEN EN FICHEROS TEMPORALES BAJO docs/loop/ Y SE
BORRAN al terminar. DE SOLO LECTURA sobre el dataset.

Uso: python scripts/loop/_v63_caso_positivo_mesa.py
exit 0 si las nueve muerden; exit 1 si alguna no.
"""
import io
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "scripts", "loop")
DOCS = os.path.join(RAIZ, "docs", "loop")
GENERADOR = os.path.join(LOOP, "generar_plan_de_fusion_de_mesa.py")
FUNDIDOR = os.path.join(LOOP, "fundir_por_plan.py")
ID_OP = "OP-M-03-II"
SUP = "pivote_o_proceder"
ABS = "pivotar_o_proceder"
DEPRECADO_REAL = "6s_lugar_trabajo"
NL = chr(10)

BASE = {
    "titulo": "SUJETO DEL CASO POSITIVO, NO SE EJECUTA NUNCA",
    "superviviente": SUP,
    "absorbidos": [ABS],
    "motivo": "motivo de mentira, este plan no se sella jamas",
    "pasos": {"1": ["CUBIERTO", 1], "2": ["CUBIERTO", 2], "3": ["CUBIERTO", 3],
              "4": ["CUBIERTO", 7], "5": ["CUBIERTO", 7]},
    "condiciones": {"1": ["CUBIERTO", 1], "2": ["CUBIERTO", 1]},
    "nota": "nota de mentira",
    "perdidas": [],
}


def escribe_contenido(nombre, spec):
    ruta = os.path.join(LOOP, nombre + ".py")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(
        "# -*- coding: utf-8 -*-" + NL
        + '"""CONTENIDO DE MENTIRA DEL CASO POSITIVO. Se borra al terminar."""' + NL
        + "FUSION = " + repr(spec) + NL)
    return ruta


def corre(cmd):
    p = subprocess.run(cmd, cwd=RAIZ, capture_output=True)
    return p.returncode, (p.stdout + p.stderr).decode("utf-8", "replace")


def prueba_generador(n, titulo, spec, aguja, fallos, basura):
    nombre = "_caso_positivo_v63_%d" % n
    basura.append(escribe_contenido(nombre, spec))
    destino = os.path.join(DOCS, "PLAN_V999_%s.json" % ID_OP.replace("-", ""))
    antes = os.path.exists(destino)
    code, salida = corre([sys.executable, GENERADOR, "--vuelta", "999",
                          "--id-op", ID_OP, "--contenido", nombre])
    escribio = os.path.exists(destino) and not antes
    linea = [l for l in salida.split(NL) if aguja in l]
    print()
    print("  %d. %s" % (n, titulo))
    print("     exit=%d | escribio plan: %s" % (code, "SI" if escribio else "NO"))
    for l in linea[:2]:
        print("     %s" % l.strip()[:150])
    ok = code == 1 and not escribio and linea
    print("     VEREDICTO: %s" % ("LA GUARDA MUERDE" if ok else "LA GUARDA NO MUERDE"))
    if not ok:
        fallos.append("prueba %d (%s) no mordio" % (n, titulo))
    if escribio:
        os.remove(destino)


def prueba_fundidor(n, titulo, plan, aguja, fallos, basura, espera_rojo=True):
    ruta = os.path.join(DOCS, "_caso_positivo_v63_plan_%d.json" % n)
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(
        json.dumps(plan, ensure_ascii=False, indent=1) + NL)
    basura.append(ruta)
    code, salida = corre([sys.executable, FUNDIDOR, "--plan", ruta])
    linea = [l for l in salida.split(NL) if aguja in l]
    print()
    print("  %d. %s" % (n, titulo))
    print("     exit=%d" % code)
    for l in linea[:2]:
        print("     %s" % l.strip()[:150])
    ok = (code == 1 if espera_rojo else code == 0) and linea
    print("     VEREDICTO: %s"
          % ("LA GUARDA MUERDE" if espera_rojo and ok
             else ("EL TITULO LO DICE" if ok else "NO PASA")))
    if not ok:
        fallos.append("prueba %d (%s) no dio lo esperado" % (n, titulo))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    sys.path.insert(0, LOOP)
    print("=" * 78)
    print("CASO POSITIVO DE LOS INSTRUMENTOS DE MESA DE LA VUELTA 63")
    print("  sujeto: %s (%s absorbe %s), QUE ESTA VUELTA NO EJECUTA" % (ID_OP, SUP, ABS))
    print("  el fundidor se llama SIEMPRE en modo SIMULAR: ni en el peor caso toca un nodo")
    print("=" * 78)
    fallos, basura = [], []

    m = dict(BASE); m["superviviente"] = ABS
    prueba_generador(1, "SUPERVIVIENTE que la ficha no escribe", m,
                     "el contenido dice superviviente", fallos, basura)

    m = dict(BASE); m["absorbidos"] = [SUP]
    prueba_generador(2, "ABSORBIDO que la ficha no escribe", m,
                     "el contenido dice absorbidos", fallos, basura)

    m = dict(BASE); m["pasos"] = dict(BASE["pasos"]); del m["pasos"]["3"]
    prueba_generador(3, "COBERTURA por OLVIDO: a un paso le falta la marca", m,
                     "no tiene marca", fallos, basura)

    m = dict(BASE); m["pasos"] = dict(BASE["pasos"]); m["pasos"]["9"] = ["CUBIERTO", 1]
    prueba_generador(4, "COBERTURA por SOBRANTE: marca de un paso que no existe", m,
                     "que sobran", fallos, basura)

    m = dict(BASE); m["pasos"] = dict(BASE["pasos"])
    m["pasos"]["2"] = ["INCISO", 2, "una parafrasis que no esta en el paso", ", "]
    prueba_generador(5, "INCISO que NO es trozo verbatim del paso que muere", m,
                     "no casa dentro del paso", fallos, basura)

    m = dict(BASE)
    m["perdidas"] = [{"especie": "DE COLOR", "que": "x", "donde": "y", "enrutada_a": "z"}]
    prueba_generador(6, "PERDIDA con especie desconocida", m,
                     "especie de perdida desconocida", fallos, basura)

    plan_ok = {
        "operacion": ID_OP, "rotulo": "PLAN DE MENTIRA", "estado": "MENTIRA",
        "actos": [{"orden": 1, "miembros": [SUP, DEPRECADO_REAL], "superviviente": SUP,
                   "absorbidos": [DEPRECADO_REAL], "pasos": {DEPRECADO_REAL: {}},
                   "condiciones": {DEPRECADO_REAL: {}}}],
        "declarados_y_no_fundidos": [],
    }
    prueba_fundidor(7, "el plan manda absorber un nodo YA DEPRECADO (guarda 1)",
                    plan_ok, "YA esta deprecado", fallos, basura)

    semilla = sorted(json.load(io.open(os.path.join(
        RAIZ, "dataset", "metadata", "entry_seeds.json"), encoding="utf-8"))["seeds"])[0]
    plan_1b = {
        "operacion": ID_OP, "rotulo": "PLAN DE MENTIRA", "estado": "MENTIRA",
        "actos": [{"orden": 1, "miembros": [SUP, semilla], "superviviente": SUP,
                   "absorbidos": [semilla], "pasos": {semilla: {}},
                   "condiciones": {semilla: {}}}],
        "declarados_y_no_fundidos": [],
    }
    prueba_fundidor(8, "el plan manda absorber la SEMILLA %s (guarda 1B)" % semilla,
                    plan_1b, "SEMILLA DE ENTRADA", fallos, basura)

    plan_sin_op = dict(plan_1b)
    plan_sin_op = json.loads(json.dumps(plan_1b))
    del plan_sin_op["operacion"]
    prueba_fundidor(9, "plan SIN campo operacion: el titulo lo DICE en vez de suponer OP-U-01",
                    plan_sin_op, "SIN OPERACION DECLARADA EN EL PLAN", fallos, basura)

    for r in basura:
        if os.path.exists(r):
            os.remove(r)
    pyc = os.path.join(LOOP, "__pycache__")
    if os.path.isdir(pyc):
        for f in os.listdir(pyc):
            if f.startswith("_caso_positivo_v63_"):
                os.remove(os.path.join(pyc, f))
    print()
    print("  ficheros de mentira borrados: %d" % len(basura))
    print()
    print("=" * 78)
    if fallos:
        print("ROJO, %d prueba(s) no dieron lo esperado:" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1
    print("RESULTADO: LAS NUEVE MUERDEN")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
