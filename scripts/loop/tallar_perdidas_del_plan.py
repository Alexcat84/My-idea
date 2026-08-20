# -*- coding: utf-8 -*-
"""tallar_perdidas_del_plan.py . TALLA LA TABLA DE LAS PERDIDAS NOMBRADAS DE LOS
PLANES SELLADOS, LEYENDOLAS DE UN CAMPO PROPIO DEL JSON Y NO DE LA PROSA.

NOMBRE ESTABLE, sin numero de vuelta ni de lote: los dos entran por argumento.

POR QUE NACE. Es el PENDIENTE DE INSTRUMENTO que el acta de la vuelta 60 dejo
escrito con todas sus letras (seccion 5, cierre): el tallador de perdidas SOLO
CUENTA LAS QUE LLEVAN EL TOKEN en la prosa del reparto, y en los lotes B y C del
tramo 5 hubo CUATRO perdidas sin token que el instrumento no vio. El acta lo
separo de la doctrina a proposito: "NO es doctrina sino instrumento y va al
encargo: los planes del tramo 6 nacen con la perdida sellada en campo legible por
maquina".

EL ANCESTRO NO SE TOCA ni se corrige: scripts/loop/vuelta56_tallar_perdidas_v55.py
sigue entero y re-corrible, y sus cifras siguen citadas por los registros de los
tramos 3, 4 y 5. Este instrumento es SUCESOR y convive con el.

===========================================================================
EL CONTRATO DE LA PERDIDA SELLADA EN CAMPO PROPIO, version 1
===========================================================================

Un plan que lo cumple lleva EN LA RAIZ:

    "contrato_de_perdidas": "CAMPO PROPIO v1"

y CADA acto lleva, SIEMPRE, una lista `perdidas`. La lista puede estar VACIA, y
ahi esta la mitad util del contrato:

    LISTA VACIA es una DECLARACION de que el acto cierra con cero perdidas.
    CAMPO AUSENTE es que el plan NO LO DICE, y eso es ROJO.

La diferencia entre las dos cosas es justo lo que la prosa no sabia distinguir:
un plan sin token podia ser un acto sin perdidas o un acto cuya perdida se
escribio con otras palabras, y el tallador viejo las contaba igual (o sea, no
las contaba).

Cada entrada de `perdidas` lleva CUATRO claves, todas obligatorias:

    especie   una de las tres que la campana ya tiene escritas, y solo esas:
              DE PARAMETRO DE PASO, DE CONDICIONES, DE NOMBRE.
              Una especie nueva es ROJO, no una categoria por defecto: estrenar
              clase de perdida en un plan sellado es doctrina y no imprenta.
    que       la pieza perdida, en las palabras del plan.
    donde     donde vive en el absorbido (paso 3, condicion 2, el titulo...).
    enrutada_a  quien puede pagarla (por ejemplo la fase 04, que redacta los
              titulos, que es el carril del acta 59 pregunta 4).

===========================================================================
LAS GUARDAS, Y NINGUNA TIENE RAMA POR DEFECTO
===========================================================================

  1. CONTRATO DECLARADO Y CAMPO AUSENTE: ROJO con el acto nombrado.
  2. ESPECIE DESCONOCIDA: ROJO con el acto y la especie nombrados.
  3. CLAVE QUE FALTA en una entrada: ROJO con el acto y la clave nombrados.
  4. EL CRUCE CONTRA LA PROSA, que es la guarda que hace fiable al campo: si la
     `nota_del_reparto` de un acto trae el token PERDIDA NOMBRADA en una frase
     que NO dice que se repone, y el campo `perdidas` de ese acto esta VACIO,
     ES ROJO. Prosa y campo diciendo cosas distintas es exactamente la averia
     que este contrato existe para no heredar, y el instrumento prefiere caer a
     elegir cual de los dos cree.
     AL REVES NO ES ROJO Y SE DICE POR QUE: una perdida en el campo SIN token en
     la prosa es el caso bueno, el que el ancestro no veia. Es el motivo entero
     del contrato.

MODO HEREDADO (--por-token): para los planes SELLADOS ANTES del contrato, que no
llevan el campo y no se reeditan (un plan sellado es el registro de lo que se
decidio aquel dia). Cuenta como el ancestro, POR TOKEN, y lo dice en la cabecera
de su propia salida con la advertencia de que esa cuenta ES CORTA POR
CONSTRUCCION. No se elige el modo en silencio: si el plan declara el contrato se
lee por campo, y si no lo declara hay que pedir --por-token con todas sus letras.

DE SOLO LECTURA. No escribe ningun fichero: imprime.

Uso:
  python scripts/loop/tallar_perdidas_del_plan.py --vuelta 61 --lotes A,B
  python scripts/loop/tallar_perdidas_del_plan.py --vuelta 60 --lotes B,C --por-token
  python scripts/loop/tallar_perdidas_del_plan.py --plan docs/loop/PLAN_X.json

SALIDA: exit 0 si talla; exit 1 en cualquier ROJO.
"""
import argparse
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")

CONTRATO = "CAMPO PROPIO v1"
MARCA = "PERDIDA NOMBRADA"
CLAVES = ("especie", "que", "donde", "enrutada_a")
ESPECIES = ("DE PARAMETRO DE PASO", "DE CONDICIONES", "DE NOMBRE")

# Las tres formas en que la prosa dice que la perdida que la RAZON nombro esta
# REPUESTA por esta fusion, o sea lo contrario de una perdida. Copiadas literales
# de scripts/loop/tallar_planes_del_tramo.py, que las midio en la vuelta 60 sobre
# los lotes B y C del tramo 5: de SEIS apariciones del token, CINCO eran de estas.
REPUESTA = ("SE REPONE", "SE REPONEN", "NO SE PIERDE")


def frases(texto):
    return [t.strip() for t in re.split(r"(?<=[.])\s+", texto or "") if t.strip()]


def apariciones_de_token(nota):
    """Las frases con el token que NO dicen que la perdida se repone."""
    fuera = []
    for f in frases(nota):
        if MARCA not in f:
            continue
        if any(r in f.upper() for r in REPUESTA):
            continue
        fuera.append(f)
    return fuera


def leer(ruta):
    return json.load(io.open(ruta, encoding="utf-8"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vuelta", type=int, default=None)
    ap.add_argument("--lotes", default=None, help="lista separada por comas: A,B,C")
    ap.add_argument("--plan", action="append", default=None,
                    help="ruta de un plan, repetible. Alternativa a --vuelta y --lotes.")
    ap.add_argument("--prefijo", default="PLAN_V%d_OPU01_LOTE_%s.json",
                    help="patron del nombre del plan, con la vuelta y el lote")
    ap.add_argument("--por-token", action="store_true", dest="por_token",
                    help="modo heredado para planes anteriores al contrato")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    rutas = []
    if a.plan:
        rutas = [x if os.path.isabs(x) else os.path.join(RAIZ, x.replace("/", os.sep))
                 for x in a.plan]
    elif a.vuelta is not None and a.lotes:
        for L in [x.strip() for x in a.lotes.split(",") if x.strip()]:
            rutas.append(os.path.join(LOOP, a.prefijo % (a.vuelta, L)))
    else:
        print("ROJO: hacen falta --vuelta y --lotes, o --plan.")
        return 1

    fallos = []
    print("=" * 100)
    print("LAS PERDIDAS NOMBRADAS, TALLADAS DE LOS PLANES SELLADOS")
    print("  modo: %s" % ("POR TOKEN EN LA PROSA (heredado)" if a.por_token
                          else "POR CAMPO PROPIO DEL JSON (contrato %s)" % CONTRATO))
    print("=" * 100)
    print()

    filas = []
    total_actos = 0
    for ruta in rutas:
        rel = os.path.relpath(ruta, RAIZ)
        if not os.path.exists(ruta):
            fallos.append("no existe el plan %s" % rel)
            continue
        plan = leer(ruta)
        contrato = plan.get("contrato_de_perdidas")
        actos = plan.get("actos") or []
        total_actos += len(actos)
        print("  plan: %-58s actos %-4d contrato: %s"
              % (rel, len(actos), contrato or "NINGUNO (anterior al contrato)"))

        if a.por_token:
            if contrato == CONTRATO:
                fallos.append("el plan %s SI declara el contrato y se pidio --por-token: "
                              "el modo no se elige en silencio, se lee por campo" % rel)
                continue
            for acto in actos:
                for f in apariciones_de_token(acto.get("nota_del_reparto")):
                    filas.append({"plan": rel, "acto": acto.get("orden"),
                                  "especie": "SIN CLASIFICAR (modo heredado)",
                                  "que": f[:160], "donde": "prosa", "enrutada_a": ""})
            continue

        if contrato != CONTRATO:
            fallos.append("el plan %s NO declara el contrato %r. Se lee por campo o se pide "
                          "--por-token con todas sus letras: el modo no se elige solo."
                          % (rel, CONTRATO))
            continue

        for acto in actos:
            n = acto.get("orden")
            if "perdidas" not in acto:
                fallos.append("%s acto %s: el plan declara el contrato y el acto NO trae el "
                              "campo perdidas. Lista vacia y campo ausente NO son lo mismo."
                              % (rel, n))
                continue
            per = acto["perdidas"]
            if not isinstance(per, list):
                fallos.append("%s acto %s: el campo perdidas no es una lista" % (rel, n))
                continue
            for p in per:
                faltan = [k for k in CLAVES if k not in p]
                if faltan:
                    fallos.append("%s acto %s: a una perdida le faltan las claves %s"
                                  % (rel, n, ", ".join(faltan)))
                    continue
                if p["especie"] not in ESPECIES:
                    fallos.append("%s acto %s: especie desconocida %r. Las escritas son: %s"
                                  % (rel, n, p["especie"], ", ".join(ESPECIES)))
                    continue
                filas.append({"plan": rel, "acto": n, "especie": p["especie"],
                              "que": p["que"], "donde": p["donde"],
                              "enrutada_a": p["enrutada_a"]})
            # GUARDA 4: el cruce contra la prosa
            sueltas = apariciones_de_token(acto.get("nota_del_reparto"))
            if sueltas and not per:
                fallos.append("%s acto %s: la prosa trae el token %r en %d frase(s) que NO "
                              "dicen que se repone, y el campo perdidas esta VACIO. Prosa y "
                              "campo dicen cosas distintas y este instrumento no elige."
                              % (rel, n, MARCA, len(sueltas)))
    print()

    if fallos:
        print("--- ROJO: %d, Y NO SE EMITE TABLA ---" % len(fallos))
        for f in fallos:
            print("    %s" % f)
        print("FIN")
        return 1

    print("--- LA TABLA ---")
    print()
    print("| plan | acto | especie | que se pierde | donde vive | enrutada a |")
    print("|---|---:|---|---|---|---|")
    for f in sorted(filas, key=lambda x: (x["plan"], x["acto"] or 0)):
        print("| %s | %s | %s | %s | %s | %s |"
              % (os.path.basename(f["plan"]), f["acto"], f["especie"],
                 f["que"], f["donde"], f["enrutada_a"]))
    if not filas:
        print("| (ninguna) | | | | | |")
    print()

    por_especie = {}
    for f in filas:
        por_especie[f["especie"]] = por_especie.get(f["especie"], 0) + 1
    print("  planes leidos      : %d" % len(rutas))
    print("  actos leidos       : %d" % total_actos)
    print("  perdidas nombradas : %d" % len(filas))
    print("  por especie        : %s" % (dict(sorted(por_especie.items())) or "{}"))
    if a.por_token:
        print()
        print("  AVISO, Y NO ES ADORNO: esta cuenta es CORTA POR CONSTRUCCION. El modo")
        print("  heredado solo ve las perdidas que llevan el token en la prosa, y en los")
        print("  lotes B y C del tramo 5 hubo CUATRO que no lo llevaban (acta 60,")
        print("  seccion 1). Un plan del contrato %s no tiene este problema." % CONTRATO)
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
