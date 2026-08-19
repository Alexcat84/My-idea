# -*- coding: utf-8 -*-
"""vuelta43_retirar_arista_interna.py - P.16, QUIEN FABRICA LIMPIA, EJECUTADO.

RETIRA LA ARISTA INTERNA DEL PAR QUE LA SIMULACION DE LA FUSION REPORTA COMO
AUTO-ARISTA NACIENTE, en los DOS sentidos, antes de fundir.

POR QUE EXISTE, y va escrito porque un instrumento nuevo dentro de un acto tiene
que traer su motivo delante:

  docs/plan/BANCO_DEL_PLAN.md, P.16, adoptada el 14 ago 2026 por decision del
  fundador, dice literalmente: "TODA OPERACION DE FUSION RETIRA, EN SU MISMO
  COMMIT, LA ARISTA INTERNA DEL PAR QUE SU PROPIA SIMULACION REPORTA COMO
  AUTO-ARISTA NACIENTE", y su punto 1 lo dice con el reparto de trabajo dentro:
  "si P.7 (la simulacion previa a toda operacion de mesa) reporta que el par a
  fusionar deja una arista interna sin retirar, sea AUTO-ARISTA o ARISTA
  DUPLICADA, LA OPERACION la retira en el mismo commit que ejecuta la fusion".
  Su punto 2 prohibe aplazarlo a un saneo posterior, porque aplazarlo "es
  exactamente como nacieron las 33 auto-aristas y las 1.056 entradas duplicadas
  de hoy".

  El acto 361 de OP-D-06 es EL PRIMERO de la campana en el que el superviviente
  y el absorbido son VECINOS DIRECTOS, y por eso es el primero en el que la
  guarda 10 de scripts/loop/vuelta39_fundir.py sale en ROJO y ABORTA SIN
  ESCRIBIR. La guarda hizo lo correcto: el ejecutor de fusiones redirige y
  deduplica, y NO retira. Quien retira es la operacion, y esto es la operacion.

LO QUE NO HACE, y es deliberado: NO toca scripts/loop/vuelta39_fundir.py. Sus
trece guardas estan escritas contra un esquema y un comportamiento, y cambiarle
la logica dentro de un acto para que deje de quejarse seria apagar la alarma en
vez de atender el fuego. La arista se retira ANTES, el ejecutor corre despues
ENTERO Y SIN TOCAR, y sus trece guardas juzgan el resultado.

LO QUE RETIRA, exactamente y nada mas: las entradas en las que el superviviente
nombra a un absorbido, y las entradas en las que un absorbido nombra al
superviviente. Las dos, porque retirar una sola deja la vista reciproca coja y
el paso 5 de run_phase1 la VUELVE A ESCRIBIR, con lo que la auto-arista
reaparece por la puerta de atras.

NO toca el texto de ningun nodo: ni pasos, ni condiciones, ni titulo, ni
etiqueta, ni resumen, ni entregable. Solo nodos_previos y nodos_siguientes.

Uso:
  python scripts/loop/vuelta43_retirar_arista_interna.py --plan RUTA.json
  python scripts/loop/vuelta43_retirar_arista_interna.py --plan RUTA.json --ejecutar
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
CAMPOS = ("nodos_previos", "nodos_siguientes")


def leer(nid):
    ruta = os.path.join(NODOS, nid + ".json")
    return json.loads(io.open(ruta, encoding="utf-8").read()), ruta


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", required=True)
    ap.add_argument("--ejecutar", action="store_true")
    args = ap.parse_args()

    plan = json.loads(io.open(args.plan, encoding="utf-8").read())
    sup = plan["superviviente"]
    absorbidos = list(plan["absorbidos"])

    print("PLAN         : %s" % os.path.relpath(args.plan, RAIZ).replace("\\", "/"))
    print("OPERACION    : %s" % plan["operacion"])
    print("SUPERVIVIENTE: %s" % sup)
    print("ABSORBIDOS   : %s" % ", ".join(absorbidos))
    print("MODO         : %s" % ("--ejecutar" if args.ejecutar else "solo lectura"))
    print("REGLA        : P.16, QUIEN FABRICA LIMPIA "
          "(docs/plan/BANCO_DEL_PLAN.md, 14 ago 2026, decision del fundador)")
    print("=" * 78)

    # --- la arista interna, medida en los dos sentidos ---
    quitar = []
    for nid, otros in [(sup, absorbidos)] + [(a, [sup]) for a in absorbidos]:
        d, _ruta = leer(nid)
        for campo in CAMPOS:
            for x in (d.get(campo) or []):
                if x in otros:
                    quitar.append({"nodo": nid, "campo": campo, "vecino": x})
    quitar.sort(key=lambda r: (r["nodo"], r["campo"], r["vecino"]))

    print("LA ARISTA INTERNA DEL PAR, medida en los dos sentidos: %d entrada(s)"
          % len(quitar))
    for r in quitar:
        print("    %-46s %-18s -> %s" % (r["nodo"], r["campo"], r["vecino"]))

    if not quitar:
        print()
        print("NADA QUE RETIRAR: el par no tiene arista interna. P.16 no aplica a "
              "este acto y no correr nada no es un rojo.")
        print("EXIT=0")
        return 0

    # --- el texto de los implicados, medido ANTES, para poder jurar que no se toco ---
    huella_antes = {}
    for nid in [sup] + absorbidos:
        d, _r = leer(nid)
        huella_antes[nid] = json.dumps(
            [d.get("titulo_concepto"), d.get("etiqueta_arbol"),
             d.get("pasos_accionables"), d.get("condiciones_activacion"),
             d.get("entregable_esperado"), d.get("resumen_teorico")],
            ensure_ascii=False, sort_keys=True)

    if not args.ejecutar:
        print()
        print("SIMULACION: cero escrituras. Corre con --ejecutar para retirarla.")
        print("EXIT=0")
        return 0

    # --- la retirada ---
    por_nodo = {}
    for r in quitar:
        por_nodo.setdefault(r["nodo"], []).append(r)
    tocados = 0
    for nid, filas in sorted(por_nodo.items()):
        d, ruta = leer(nid)
        for campo in CAMPOS:
            fuera = set(f["vecino"] for f in filas if f["campo"] == campo)
            if not fuera:
                continue
            d[campo] = [x for x in (d.get(campo) or []) if x not in fuera]
        io.open(ruta, "w", encoding="utf-8", newline="\n").write(
            json.dumps(d, ensure_ascii=False, indent=2) + "\n")
        tocados += 1

    print()
    print("ESCRITO. ficheros tocados: %d" % tocados)

    # --- guardas propias ---
    fallos = []

    restan = []
    for nid, otros in [(sup, absorbidos)] + [(a, [sup]) for a in absorbidos]:
        d, _r = leer(nid)
        for campo in CAMPOS:
            for x in (d.get(campo) or []):
                if x in otros:
                    restan.append((nid, campo, x))
    print("guarda A, cero arista interna del par tras retirar: %s (%d)"
          % ("OK" if not restan else "ROJO", len(restan)))
    if restan:
        fallos.append("quedan aristas internas: %s" % restan)

    for nid in [sup] + absorbidos:
        d, _r = leer(nid)
        ahora = json.dumps(
            [d.get("titulo_concepto"), d.get("etiqueta_arbol"),
             d.get("pasos_accionables"), d.get("condiciones_activacion"),
             d.get("entregable_esperado"), d.get("resumen_teorico")],
            ensure_ascii=False, sort_keys=True)
        ok = (ahora == huella_antes[nid])
        print("guarda B, %-44s texto INTACTO (titulo, etiqueta, pasos, "
              "condiciones, entregable, resumen): %s" % (nid, "OK" if ok else "ROJO"))
        if not ok:
            fallos.append("el texto de %s cambio" % nid)

    print()
    if fallos:
        print("RESULTADO: %d FALLO(S)" % len(fallos))
        for f in fallos:
            print("  [ROJO] %s" % f)
        print("EXIT=1")
        return 1
    print("RESULTADO: TODAS LAS GUARDAS VERDES")
    print("EXIT=0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
