# -*- coding: utf-8 -*-
"""vuelta49_inciso_adosado.py . EL INCISO ADOSADO, la figura de la tabla de seis
motivos, aplicada a UN paso de UN superviviente ya fundido.

QUE ES Y DE DONDE SALE. La TABLA DE LOS SEIS MOTIVOS DE PERDIDA DE LINEA
(docs/plan/02_DESTEJIDOS.md) tiene un gesto llamado SALVAGUARDA cuyo remedio
escrito es literalmente este: "el inciso se adosa al paso que protege". El
precedente vivo es OP-D-02 paso 1 (02_DESTEJIDOS.md linea 220, leida hoy):
"el superviviente manda identificar la hipotesis y no dice contra que sesgo se
decide cual es la critica. El paso 10 trae la prueba (que alguien PAGARIA por
resolverlo) y el inciso se adosa al paso que protege."

POR QUE ESTE INSTRUMENTO EXISTE, y no lo hace el de fundir: vuelta48_fundir_tramo
solo sabe DOS destinos para una pieza, APPEND (viaja entera como paso nuevo) o
CUBIERTO:n (ya lo dice el paso n). El INCISO ADOSADO es el tercero y no lo tenia:
la pieza NO viaja entera (duplicaria lo que el superviviente ya manda) pero
TAMPOCO esta cubierta del todo. Faltaba el gesto de en medio.

EL CONTRATO, y es lo que impide una errata:
  - El plan NO redacta el inciso: lo NOMBRA como un TROZO VERBATIM del paso del
    nodo que muere, y la guarda 2 comprueba que ese trozo esta LITERAL dentro de
    ese paso. Si el plan se inventa una palabra, esto cae en rojo y no escribe.
  - Lo unico que este instrumento aporta de su cosecha es el NEXO (una coma y una
    preposicion), que va escrito en el plan y se imprime aparte para que se pueda
    discutir por separado del contenido.
  - Guarda de P.5 sobre el texto: el paso del superviviente tiene que ser HOY,
    byte a byte, el que el plan dice que era. Si el nodo se movio desde que se
    leyo, esto aborta.
  - Guarda de idempotencia: si el inciso YA esta dentro del paso, no se escribe
    nada y se dice. Correr dos veces no apila.

MODOS: --simular (por defecto, cero escrituras) y --ejecutar.

Uso:
  python scripts/loop/vuelta49_inciso_adosado.py --plan docs/loop/PLAN_V49_INCISO_ACTO49.json [--ejecutar]
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")


def ruta(nid):
    return os.path.join(NODOS, nid + ".json")


def leer_crudo(nid):
    with io.open(ruta(nid), encoding="utf-8", newline="") as fh:
        bruto = fh.read()
    cola = ""
    while bruto and bruto[-1] in "\r\n":
        cola = bruto[-1] + cola
        bruto = bruto[:-1]
    return json.loads(bruto), cola


def escribir(nid, datos, cola):
    with io.open(ruta(nid), "w", encoding="utf-8", newline="") as fh:
        fh.write(json.dumps(datos, ensure_ascii=False, indent=2) + cola)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", required=True)
    ap.add_argument("--ejecutar", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    plan = json.load(io.open(a.plan, encoding="utf-8"))
    modo = "EJECUTAR" if a.ejecutar else "SIMULAR"
    print("=" * 78)
    print("INCISO ADOSADO . MODO %s" % modo)
    print("plan: %s (%s)" % (a.plan, plan["estado"]))
    print("figura: %s" % plan["figura"])
    print("=" * 78)

    fallos = []
    escrituras = []
    for inc in plan["incisos"]:
        sup, i_sup = inc["superviviente"], int(inc["paso_superviviente"])
        ori, i_ori = inc["origen"], int(inc["paso_origen"])
        print()
        print("-" * 78)
        print("ACTO %s . %s paso %d  <==  %s paso %d"
              % (inc["acto"], sup, i_sup, ori, i_ori))

        ds, cola = leer_crudo(sup)
        do, _ = leer_crudo(ori)
        pasos = list(ds.get("pasos_accionables") or [])
        pasos_o = list(do.get("pasos_accionables") or [])

        # GUARDA 0: los dos nodos estan donde el plan dice, y en el estado que dice.
        rotos0 = []
        if ds.get("deprecado"):
            rotos0.append("%s esta DEPRECADO y el plan lo llama superviviente" % sup)
        if not do.get("deprecado"):
            rotos0.append("%s NO esta deprecado y el plan lo llama origen absorbido" % ori)
        if ori not in (ds.get("ids_alias") or []):
            rotos0.append("%s no figura en ids_alias de %s: no son el mismo acto" % (ori, sup))
        if not (1 <= i_sup <= len(pasos)):
            rotos0.append("el superviviente no tiene paso %d (tiene %d)" % (i_sup, len(pasos)))
        if not (1 <= i_ori <= len(pasos_o)):
            rotos0.append("el origen no tiene paso %d (tiene %d)" % (i_ori, len(pasos_o)))
        fallos.extend("%s" % r for r in rotos0)
        print("  guarda 0, los dos nodos en el estado que el plan dice: %s"
              % ("OK" if not rotos0 else "ROJO %s" % rotos0))
        if rotos0:
            continue

        texto_sup = pasos[i_sup - 1]
        texto_ori = pasos_o[i_ori - 1]
        print("  paso del superviviente HOY : %s" % texto_sup)
        print("  paso del origen (INTACTO)  : %s" % texto_ori)

        # GUARDA 1, P.5 SOBRE EL TEXTO: el paso es HOY el que el plan leyo.
        ok1 = texto_sup == inc["texto_superviviente_al_leerlo"]
        if not ok1:
            fallos.append("P.5: el paso %d de %s cambio desde que se leyo" % (i_sup, sup))
        print("  guarda 1, P.5 (el paso es byte a byte el que el plan leyo): %s"
              % ("OK" if ok1 else "ROJO"))

        # GUARDA 2: el inciso es un trozo VERBATIM del paso del que muere.
        ok2 = inc["inciso_verbatim"] in texto_ori
        if not ok2:
            fallos.append("el inciso NO es trozo verbatim del paso %d de %s" % (i_ori, ori))
        print("  guarda 2, el inciso es trozo VERBATIM del origen: %s"
              % ("OK" if ok2 else "ROJO"))
        print("     inciso : %r" % inc["inciso_verbatim"])
        print("     nexo   : %r  (LO UNICO que este instrumento aporta de su cosecha)"
              % inc["nexo"])

        # GUARDA 3, IDEMPOTENCIA: si ya esta, no se apila.
        if inc["inciso_verbatim"] in texto_sup:
            print("  guarda 3, idempotencia: EL INCISO YA ESTA DENTRO. Cero escrituras.")
            continue
        print("  guarda 3, idempotencia: el inciso NO esta todavia. Procede.")

        nuevo = texto_sup + inc["nexo"] + inc["inciso_verbatim"]
        print("  paso RESULTANTE            : %s" % nuevo)

        # GUARDA 4: solo cambia ESE paso, y nada mas del nodo.
        pasos_nuevos = list(pasos)
        pasos_nuevos[i_sup - 1] = nuevo
        if len(set(pasos_nuevos)) != len(pasos_nuevos):
            fallos.append("el superviviente %s quedaria con un paso repetido literal" % sup)
        d2 = json.loads(json.dumps(ds))
        d2["pasos_accionables"] = pasos_nuevos
        distintos = sorted(k for k in set(list(ds) + list(d2)) if ds.get(k) != d2.get(k))
        if distintos != ["pasos_accionables"]:
            fallos.append("cambiaria mas que pasos_accionables: %s" % distintos)
        print("  guarda 4, SOLO cambia pasos_accionables: %s (%s)"
              % ("OK" if distintos == ["pasos_accionables"] else "ROJO", distintos))
        escrituras.append((sup, d2, cola))

    if fallos:
        print()
        print("SE ABORTA SIN ESCRIBIR, %d fallo(s):" % len(fallos))
        for f in fallos:
            print("  [ROJO] %s" % f)
        return 1

    print()
    print("=" * 78)
    print("RESUMEN: %d inciso(s) a adosar, %d nodo(s) a escribir"
          % (len(plan["incisos"]), len(escrituras)))
    if not a.ejecutar:
        print("SIMULACION: cero escrituras.")
        return 0
    for nid, datos, cola in escrituras:
        escribir(nid, datos, cola)
        print("ESCRITO: %s" % nid)
    return 0


if __name__ == "__main__":
    sys.exit(main())
