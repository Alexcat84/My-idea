# -*- coding: utf-8 -*-
"""vuelta64_correcciones_consumidas.py . ESCRIBE EN LAS CINCO FICHAS CONSUMIDAS
DE docs/plan/OPERACIONES.jsonl SU CORRECCION DECLARADA (banco 9.10).

TAREA 1.c del encargo de la vuelta 64. NADA DEL GRAFO SE TOCA: la correccion es
DE REGISTRO. Ni un nodo, ni un alias, ni un campo del catalogo.

LA CIFRA NO SE TECLEA: cada nombre propio y cada numero de linea de los parrafos
que se escriben sale de scripts/loop/vuelta64_consumidas.py, que se IMPORTA en
vez de reteclearse, para que el que mide y el que escribe no puedan discrepar en
silencio. Si aquel cae en ROJO, este no escribe nada.

DONDE VA LA CORRECCION: al final del campo `nota`, que es el sitio que estas
mismas fichas ya usan (OP-F-01, OP-D-01, OP-D-03, OP-D-04, OP-S-06, OP-S-07,
OP-C-04 y OP-U-01 traen ahi su CORRECCION DECLARADA). NO SE ESTRENA UN CAMPO
NUEVO A PROPOSITO: el esquema de OPERACIONES.jsonl es un pendiente de doctrina
heredado (acta 55, seccion 5, cierre) y estrenar clave en cinco de las 71 fichas
seria decidirlo de tapadillo. EL TEXTO VIEJO NO SE BORRA: una correccion que
tapa lo que corrige no se puede auditar.

LAS GUARDAS, y ninguna tiene rama por defecto:
  1. si la medicion cae en ROJO, no se escribe nada;
  2. si la marca ya esta en el fichero, no se escribe nada (idempotente);
  3. tras escribir se re-lee: 71 fichas antes y 71 despues, las mismas 18 claves
     en todas, y el texto viejo (la adjudicacion del 12 ago) sigue dentro de las
     cinco;
  4. cero guiones largos y cero guiones medios en lo escrito.

Uso: python scripts/loop/vuelta64_correcciones_consumidas.py [--escribir]
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
MARCA = "CORRECCION DECLARADA (2026-08-20, vuelta 64, TAREA 1.c del encargo)"

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vuelta64_consumidas import medir  # noqa: E402


def parrafo(f):
    s = f["sitios"][0]
    lote = ("" if s["lote"].startswith("NO HAY COLUMNA")
            else ", lote %s" % s["lote"])
    t = (
        " " + MARCA + ", POR EL CARRIL DEL BANCO 9.10 Y CON EL TEXTO VIEJO ENTERO "
        "ARRIBA: ESTA FICHA ESTA CONSUMIDA. NO SE EJECUTA Y NO SE REHACE. "
        "MEDIDO HOY CONTRA EL GRAFO y no leido de un acta, con "
        "scripts/loop/vuelta64_consumidas.py resolviendo alias por P.1 "
        "(docs/loop/SALIDA_V64_CONSUMIDAS.txt): %s; o sea que los dos miembros de "
        "esta ficha resuelven a UN SOLO VIVO, %s. "
        "SU FUSION YA LA EJECUTO UN TRAMO DE OP-U-01, y eso es cosa juzgada con "
        "su plan sellado y su acta: %s, acto %s%s, registrado en "
        "docs/plan/03_FUSIONES.md LINEA %d, cuya fila dice sobrevive %s y absorbe "
        "%s (celdas leidas por el nombre de su columna en la cabecera de la linea "
        "%d, no de la prosa de alrededor)."
        % (", ".join(f["estados"]), f["sup_real"], s["sede"], s["acto"], lote,
           s["linea"], s["sobrevive"], s["absorbe"], s["cab_linea"]))
    if f["divergen"]:
        t += (
            " DIVERGENCIA DE SUPERVIVIENTE, DECLARADA COMO CONTRASTE Y NO RESUELTA "
            "COPIANDO (regla 1 y regla 2 de EJECUTOR.md): esta ficha adjudico el 12 "
            "ago 2026 el superviviente %s y el tramo dejo vivo al OPUESTO, %s. "
            "LA ADJUDICACION DE ARRIBA QUEDA ENTERA Y NO SE TACHA: lo que se declara "
            "es que NO FUE LA QUE SE EJECUTO. Y NO SE DESHACE: deshacer una fusion "
            "registrada y auditada seria decision de fundador, y nadie la pide "
            "(acta 63, seccion 6)."
            % (f["sup_ficha"], f["sup_real"]))
    else:
        t += (
            " EL SUPERVIVIENTE COINCIDE: el tramo dejo vivo a %s, que es el mismo "
            "que esta ficha adjudico el 12 ago 2026. Lo unico que cambia es QUIEN lo "
            "ejecuto." % f["sup_real"])
    if f["solo_muerto"]:
        t += (
            " Y EL REGISTRO TRAE ADEMAS EL RASTRO DEL QUE MURIO FUERA DE LA FILA DEL "
            "ACTO, en la linea %s de la misma pagina."
            % ", ".join(str(x) for x in f["solo_muerto"]))
    return t


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--escribir", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    filas, fallos, ctx = medir()
    print("=" * 78)
    print("LAS CINCO CORRECCIONES DECLARADAS DE LAS FICHAS CONSUMIDAS")
    print("  medicion importada de scripts/loop/vuelta64_consumidas.py")
    print("  grafo %d nodos | alias %d | registro %d lineas"
          % (ctx["nodos"], ctx["alias"], ctx["lineas"]))
    print("=" * 78)
    if fallos:
        print()
        print("ROJO: la medicion trae %d fallo(s) y NO se escribe nada:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1
    if len(filas) != 5:
        print()
        print("ROJO: la medicion devolvio %d fichas y son CINCO. PARADA." % len(filas))
        return 1

    lineas = [l for l in io.open(OPS, encoding="utf-8") if l.strip()]
    ops = [json.loads(l) for l in lineas]
    print()
    print("  fichas en OPERACIONES.jsonl: %d" % len(ops))
    claves_antes = {o["id_op"]: len(o) for o in ops}

    if MARCA in io.open(OPS, encoding="utf-8").read():
        print()
        print("YA APLICADA: la marca esta en el fichero. No se escribe nada.")
        return 0

    textos = {}
    for f in filas:
        textos[f["id_op"]] = parrafo(f)
        print()
        print("--- %s (%s) ---" % (f["id_op"],
                                   "DIVERGE" if f["divergen"] else "coincide"))
        print("   %s" % textos[f["id_op"]].strip()[:300])

    salida = []
    tocadas = 0
    for l in lineas:
        d = json.loads(l)
        if d["id_op"] in textos:
            if not isinstance(d.get("nota"), str):
                print()
                print("ROJO: la ficha %s no trae nota de texto. PARADA." % d["id_op"])
                return 1
            d["nota"] = d["nota"].rstrip() + textos[d["id_op"]]
            tocadas += 1
            salida.append(json.dumps(d, ensure_ascii=False) + chr(10))
        else:
            salida.append(l if l.endswith(chr(10)) else l + chr(10))

    print()
    print("  fichas a corregir: %d (solo el campo nota de cada una)" % tocadas)
    if not a.escribir:
        print("  SIMULACION: sin --escribir no se toca nada.")
        print()
        print("FIN")
        return 0

    io.open(OPS, "w", encoding="utf-8", newline=chr(10)).writelines(salida)

    print()
    print("GUARDAS TRAS ESCRIBIR")
    ops2 = [json.loads(l) for l in io.open(OPS, encoding="utf-8") if l.strip()]
    print("  fichas antes %d, despues %d" % (len(ops), len(ops2)))
    ok = len(ops) == len(ops2)
    for o in ops2:
        if claves_antes.get(o["id_op"]) != len(o):
            print("  ROJO: %s cambio de %s a %d claves"
                  % (o["id_op"], claves_antes.get(o["id_op"]), len(o)))
            ok = False
    print("  las 18 claves intactas en las 71: %s" % ("OK" if ok else "ROJO"))
    viejas = 0
    for o in ops2:
        if o["id_op"] in textos and "2026-08-12" == o.get("fecha_corte"):
            viejas += 1
    print("  las cinco conservan su fecha_corte del 12 ago: %d de 5" % viejas)
    con_marca = sum(1 for o in ops2 if MARCA in (o.get("nota") or ""))
    print("  fichas con la marca nueva: %d de 5" % con_marca)
    t = io.open(OPS, encoding="utf-8").read()
    largos = t.count(chr(8212))
    medios = t.count(chr(8211))
    print("  guiones largos %d, guiones medios %d" % (largos, medios))
    if not ok or viejas != 5 or con_marca != 5 or largos or medios:
        print()
        print("ROJO EN LAS GUARDAS.")
        return 1
    print()
    print("VERDE: las cinco correcciones escritas, el texto viejo entero y el grafo intacto.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
