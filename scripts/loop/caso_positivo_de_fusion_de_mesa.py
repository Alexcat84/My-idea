# -*- coding: utf-8 -*-
"""caso_positivo_de_fusion_de_mesa.py . EL CASO POSITIVO DE LOS DOS INSTRUMENTOS
DE MESA (generar_plan_de_fusion_de_mesa.py y fundir_por_plan.py), CON EL SUJETO
POR ARGUMENTO.

NOMBRE ESTABLE, y no lleva vuelta ni operacion: la operacion entra por --id-op.
Es la vara del acta 58, pregunta 4.

SUCESOR DECLARADO de scripts/loop/_v63_caso_positivo_mesa.py, AL QUE NO
REEMPLAZA: el ancestro queda entero y re-corrible, y el acta 63 cita sus NUEVE
guardas mordiendo. La maquina se copia de el; lo que cambia esta enumerado abajo.

POR QUE NACE, y es una averia MEDIDA en la propia carne del ancestro y no un
capricho. La regla de trabajo del acta 54, pregunta 7, dice que EL CASO POSITIVO
SE FABRICA SOBRE UN ACTO QUE LA PROPIA VUELTA NO VAYA A TOCAR, PARA QUE NO
CADUQUE. El ancestro la cumplio en su vuelta y eligio OP-M-03-II, que la vuelta
63 no tocaba. LA VUELTA 64 EJECUTA OP-M-03-II. Corrido tal cual en la vuelta 64
DESPUES de fundir, el ancestro da ROJO en CUATRO de sus nueve pruebas (la 3, la
4, la 5 y la 6), y no porque las guardas se hayan roto: porque pivotar_o_proceder
ya esta DEPRECADO, el generador cae antes en la guarda de miembro vivo y no llega
nunca a las guardas de cobertura, de inciso y de perdida. LA REGLA NO BASTA SI EL
SUJETO ESTA TALLADO EN EL FICHERO: el sujeto de una vuelta es el ejecutado de la
siguiente. Por eso el sujeto entra por argumento.

LO QUE CAMBIA RESPECTO DEL ANCESTRO, Y ES SOLO ESTO:
  1. --id-op REQUERIDO: el sujeto no se talla, se pasa. Un caso positivo de
     nombre estable que da por supuesta una operacion miente en cuanto se use
     para otra;
  2. GUARDA DE SUJETO VIVO, que es la que le faltaba al ancestro: si los dos
     miembros de la operacion no estan VIVOS hoy, el instrumento cae en ROJO
     ANTES de correr una sola prueba y DICE que el sujeto esta consumido. Fallar
     ruidoso en vez de dar cuatro guardas por no mordidas;
  3. LAS MARCAS DE MENTIRA SE ARMAN DE LA FORMA REAL DE LOS NODOS (cuantos pasos
     y cuantas condiciones tiene cada uno, leidos hoy) en vez de venir talladas
     para un par concreto. Es lo que permite apuntarlo a cualquier par.
NI UNA PRUEBA CAMBIA DE SENTIDO, NI SE ANADE NI SE QUITA NINGUNA: son las mismas
nueve.

LOS PLANES DE MENTIRA SE ESCRIBEN EN FICHEROS TEMPORALES BAJO docs/loop/ Y SE
BORRAN al terminar. El fundidor se llama SIEMPRE en modo SIMULAR: ni en el peor
caso toca un nodo. DE SOLO LECTURA sobre el dataset.

Uso:
  python scripts/loop/caso_positivo_de_fusion_de_mesa.py --id-op OP-M-02-ACCLIMATE
exit 0 si las nueve muerden; exit 1 si alguna no, o si el sujeto no sirve.
"""
import argparse
import io
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "scripts", "loop")
DOCS = os.path.join(RAIZ, "docs", "loop")
NODOS = os.path.join(RAIZ, "dataset", "nodos")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
GENERADOR = os.path.join(LOOP, "generar_plan_de_fusion_de_mesa.py")
FUNDIDOR = os.path.join(LOOP, "fundir_por_plan.py")
DEPRECADO_REAL = "6s_lugar_trabajo"
NL = chr(10)


def nodo(n):
    p = os.path.join(NODOS, n + ".json")
    return json.load(io.open(p, encoding="utf-8")) if os.path.exists(p) else None


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


def prueba_generador(n, titulo, spec, aguja, fallos, basura, id_op):
    nombre = "_caso_positivo_mesa_%d" % n
    basura.append(escribe_contenido(nombre, spec))
    destino = os.path.join(DOCS, "PLAN_V999_%s.json" % id_op.replace("-", ""))
    antes = os.path.exists(destino)
    code, salida = corre([sys.executable, GENERADOR, "--vuelta", "999",
                          "--id-op", id_op, "--contenido", nombre])
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
    ruta = os.path.join(DOCS, "_caso_positivo_mesa_plan_%d.json" % n)
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
    ap = argparse.ArgumentParser()
    ap.add_argument("--id-op", dest="id_op", required=True,
                    help="operacion sujeto; tiene que ser una que la vuelta NO ejecute")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    sys.path.insert(0, LOOP)

    ficha = None
    for l in io.open(OPS, encoding="utf-8"):
        if l.strip() and json.loads(l).get("id_op") == a.id_op:
            ficha = json.loads(l)
    print("=" * 78)
    print("CASO POSITIVO DE LOS INSTRUMENTOS DE FUSION DE MESA")
    print("  sujeto: %s" % a.id_op)
    print("  el fundidor se llama SIEMPRE en modo SIMULAR: ni en el peor caso toca un nodo")
    print("=" * 78)
    if ficha is None:
        print()
        print("ROJO: %s no esta en docs/plan/OPERACIONES.jsonl. PARADA." % a.id_op)
        return 1
    sup = ficha.get("superviviente")
    absorbidos = list(ficha.get("eliminar") or [])
    print()
    print("  --- GUARDA DE SUJETO VIVO, la que el ancestro no tenia ---")
    print("     superviviente de la ficha: %s" % sup)
    print("     absorbidos de la ficha   : %s" % ", ".join(absorbidos))
    if not sup or not absorbidos:
        print("     ROJO: el sujeto tiene que traer superviviente y al menos un absorbido. PARADA.")
        return 1
    # EL SUJETO PUEDE TENER MAS DE UN ABSORBIDO (vuelta 139, TAREA 3).
    # CORRECCION DECLARADA, y el texto viejo de esta guarda era, VERBATIM:
    #     if not sup or len(absorbidos) != 1:
    #         print("     ROJO: el sujeto tiene que ser un PAR con superviviente escrito. PARADA.")
    # NO ERA UNA REGLA, ERA UN LIMITE DEL INSTRUMENTO: la fase 06 abre con
    # OP-M-01-FUSION, que tiene CUATRO absorbidos, y con la guarda vieja el caso
    # positivo de esa fusion no podia correr y habria quedado SIN CASO. Es la
    # misma figura que la 2.a de la vuelta 138 encontro en el generador (el
    # camino de dos o mas absorbidos no habia corrido nunca) y se repara igual:
    # el reparto de mentira se arma POR PAR, que es el unico formato que el
    # generador acepta con dos o mas. NINGUNA PRUEBA CAMBIA DE SENTIDO y no se
    # anade ni se quita ninguna: siguen siendo las mismas NUEVE, y las que mutan
    # una marca mutan la del PRIMER absorbido de la ficha, nombrado en la salida.
    ab = absorbidos[0]
    n_sup = nodo(sup)
    nodos_ab = [(x, nodo(x)) for x in absorbidos]
    n_ab = dict(nodos_ab)[ab]
    muertos = [x for x, d in ([(sup, n_sup)] + nodos_ab)
               if d is None or d.get("deprecado") or d.get("deprecated")]
    for x, d in ([(sup, n_sup)] + nodos_ab):
        print("     %-38s %s" % (x, "AUSENTE" if d is None else
                                 ("DEPRECADO" if (d.get("deprecado") or d.get("deprecated"))
                                  else "VIVO")))
    if muertos:
        print()
        print("     ROJO: EL SUJETO ESTA CONSUMIDO (%s). Un caso positivo sobre un par"
              % ", ".join(muertos))
        print("     ya fundido no prueba nada: el generador cae en la guarda de miembro")
        print("     vivo y NUNCA llega a las guardas de cobertura, inciso y perdida, que")
        print("     quedarian dadas por no mordidas. Apunta el instrumento a un par que")
        print("     esta vuelta NO ejecute (acta 54, pregunta 7). PARADA.")
        return 1

    pasos_sup = list(n_sup.get("pasos_accionables") or [])
    cond_sup = list(n_sup.get("condiciones_activacion") or [])
    pasos_por_ab = {x: list(d.get("pasos_accionables") or []) for x, d in nodos_ab}
    cond_por_ab = {x: list(d.get("condiciones_activacion") or []) for x, d in nodos_ab}
    pasos_ab = pasos_por_ab[ab]
    cond_ab = cond_por_ab[ab]
    print("     el superviviente de hoy: %d pasos y %d condiciones"
          % (len(pasos_sup), len(cond_sup)))
    for x, _d in nodos_ab:
        print("     el absorbido %-26s %d pasos y %d condiciones"
              % (x, len(pasos_por_ab[x]), len(cond_por_ab[x])))
    print("     las marcas de mentira se mutan sobre el PRIMER absorbido: %s" % ab)
    vacios = [x for x, _d in nodos_ab if not pasos_por_ab[x] or not cond_por_ab[x]]
    if not pasos_sup or not cond_sup or vacios:
        print()
        print("     ROJO: el superviviente o algun absorbido (%s) no tiene pasos y"
              % (", ".join(vacios) or "ninguno"))
        print("     condiciones, y las nueve pruebas necesitan las listas de los dos")
        print("     lados. PARADA.")
        return 1

    # LAS MARCAS DE MENTIRA SE ARMAN DE LA FORMA REAL DE LOS NODOS.
    BASE = {
        "titulo": "SUJETO DEL CASO POSITIVO, NO SE EJECUTA NUNCA",
        "superviviente": sup,
        "absorbidos": list(absorbidos),
        "motivo": "motivo de mentira, este plan no se sella jamas",
        # EL REPARTO DE MENTIRA VA POR PAR (vuelta 139): con un solo absorbido
        # da exactamente lo mismo que el dict plano de antes, porque el
        # generador acepta los dos formatos con uno; con dos o mas es el UNICO
        # que el generador acepta desde la 2.a de la vuelta 138.
        "pasos": {x: {str(i): ["CUBIERTO", 1] for i in range(1, len(pasos_por_ab[x]) + 1)}
                  for x, _d in nodos_ab},
        "condiciones": {x: {str(i): ["CUBIERTO", 1] for i in range(1, len(cond_por_ab[x]) + 1)}
                        for x, _d in nodos_ab},
        "nota": "nota de mentira",
        "perdidas": [],
    }
    fallos, basura = [], []

    m = dict(BASE); m["superviviente"] = ab
    prueba_generador(1, "SUPERVIVIENTE que la ficha no escribe", m,
                     "el contenido dice superviviente", fallos, basura, a.id_op)

    m = dict(BASE); m["absorbidos"] = [sup]
    prueba_generador(2, "ABSORBIDO que la ficha no escribe", m,
                     "el contenido dice absorbidos", fallos, basura, a.id_op)

    m = dict(BASE); m["pasos"] = dict(BASE["pasos"])
    m["pasos"][ab] = dict(BASE["pasos"][ab]); del m["pasos"][ab][str(len(pasos_ab))]
    prueba_generador(3, "COBERTURA por OLVIDO: a un paso de %s le falta la marca" % ab, m,
                     "no tiene marca", fallos, basura, a.id_op)

    m = dict(BASE); m["pasos"] = dict(BASE["pasos"])
    m["pasos"][ab] = dict(BASE["pasos"][ab])
    m["pasos"][ab][str(len(pasos_ab) + 4)] = ["CUBIERTO", 1]
    prueba_generador(4, "COBERTURA por SOBRANTE: marca de un paso de %s que no existe" % ab, m,
                     "que sobran", fallos, basura, a.id_op)

    m = dict(BASE); m["pasos"] = dict(BASE["pasos"])
    m["pasos"][ab] = dict(BASE["pasos"][ab])
    m["pasos"][ab]["1"] = ["INCISO", 1, "una parafrasis que no esta en el paso", ", "]
    prueba_generador(5, "INCISO que NO es trozo verbatim del paso que muere", m,
                     "no casa dentro del paso", fallos, basura, a.id_op)

    m = dict(BASE)
    m["perdidas"] = [{"especie": "DE COLOR", "que": "x", "donde": "y", "enrutada_a": "z"}]
    prueba_generador(6, "PERDIDA con especie desconocida", m,
                     "especie de perdida desconocida", fallos, basura, a.id_op)

    plan_dep = {
        "operacion": a.id_op, "rotulo": "PLAN DE MENTIRA", "estado": "MENTIRA",
        "actos": [{"orden": 1, "miembros": [sup, DEPRECADO_REAL], "superviviente": sup,
                   "absorbidos": [DEPRECADO_REAL], "pasos": {DEPRECADO_REAL: {}},
                   "condiciones": {DEPRECADO_REAL: {}}}],
        "declarados_y_no_fundidos": [],
    }
    prueba_fundidor(7, "el plan manda absorber un nodo YA DEPRECADO (guarda 1)",
                    plan_dep, "YA esta deprecado", fallos, basura)

    semilla = sorted(json.load(io.open(os.path.join(
        RAIZ, "dataset", "metadata", "entry_seeds.json"), encoding="utf-8"))["seeds"])[0]
    plan_1b = {
        "operacion": a.id_op, "rotulo": "PLAN DE MENTIRA", "estado": "MENTIRA",
        "actos": [{"orden": 1, "miembros": [sup, semilla], "superviviente": sup,
                   "absorbidos": [semilla], "pasos": {semilla: {}},
                   "condiciones": {semilla: {}}}],
        "declarados_y_no_fundidos": [],
    }
    prueba_fundidor(8, "el plan manda absorber la SEMILLA %s (guarda 1B)" % semilla,
                    plan_1b, "SEMILLA DE ENTRADA", fallos, basura)

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
            if f.startswith("_caso_positivo_mesa_"):
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
    print("RESULTADO: LAS NUEVE MUERDEN, sobre el sujeto %s" % a.id_op)
    print("=" * 78)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
