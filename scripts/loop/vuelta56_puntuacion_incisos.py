# -*- coding: utf-8 -*-
"""vuelta56_puntuacion_incisos.py . REPARA LA PUNTUACION DE LOS INCISOS QUE ESTA
MISMA VUELTA ESCRIBIO, Y SOLO ESA.

POR QUE EXISTE, con la caida medida y no supuesta: los lotes A y B de la vuelta
56 adosaron incisos a pasos del superviviente que TERMINABAN EN PUNTO, con un
nexo que empieza por coma. El resultado es una juntura ".," en medio del paso,
que es un defecto de texto visible. Se cazo releyendo las salidas de los planes
sellados ANTES de cerrar la vuelta, y el lote C ya nacio con los nexos
corregidos.

QUE HACE, y nada mas: para CADA marca INCISO de los PLAN_V56_*.json SELLADOS,
reconstruye la juntura exacta que el ejecutor escribio (paso original del
superviviente mas nexo mas inciso) y, SI Y SOLO SI el paso original terminaba en
punto y el nexo empieza por coma, BORRA ESE PUNTO Y NADA MAS. Un solo caracter
por juntura.

LAS GUARDAS, que son las que hacen esto auditable:
  - EL PASO ACTUAL DEL SUPERVIVIENTE TIENE QUE SER, LITERAL, la juntura
    esperada. Si no lo es, ese caso se salta y se dice; no se toca nada a
    ciegas.
  - SOLO SE BORRA EL PUNTO DE LA JUNTURA. La longitud del paso baja EXACTAMENTE
    en uno y el texto resultante tiene que ser el esperado, comprobado antes de
    escribir.
  - EL INCISO Y EL PASO ORIGINAL NO SE TOCAN: ni una letra. Lo unico que cambia
    es el punto que separaba los dos.
  - IDEMPOTENTE: si el paso ya esta en su forma corregida, se cuenta como YA
    ESTABA y no se escribe.
  - SI NINGUNA JUNTURA HAY QUE TOCAR, no escribe ningun fichero.

EL PASO ORIGINAL DEL SUPERVIVIENTE SE LEE DEL COMMIT ANTERIOR A LA FUSION, por
git, para no tener que suponerlo: el plan sellado dice a que paso se adoso el
inciso, y el blob de git dice como era ese paso antes.

Uso:
  python scripts/loop/vuelta56_puntuacion_incisos.py --antes <sha> [--ejecutar]
"""
import argparse
import io
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
LOOP = os.path.join(RAIZ, "docs", "loop")
LOTES = ["A", "B", "C"]


def leer_nodo(nid):
    """LECTURA Y ESCRITURA COPIADAS DE scripts/loop/vuelta49_fundir_tramo.py
    (lineas 86 a 98), para que el fichero conserve EXACTAMENTE su final de
    linea y su cola: reescribir un nodo con otro salto de linea produciria un
    diff de fichero entero donde solo cambia un caracter."""
    with io.open(os.path.join(NODOS, nid + ".json"), encoding="utf-8", newline="") as fh:
        bruto = fh.read()
    cola = ""
    while bruto and bruto[-1] in (chr(13), chr(10)):
        cola = bruto[-1] + cola
        bruto = bruto[:-1]
    return json.loads(bruto), cola


def escribir_nodo(nid, datos, cola):
    with io.open(os.path.join(NODOS, nid + ".json"), "w", encoding="utf-8", newline="") as fh:
        fh.write(json.dumps(datos, ensure_ascii=False, indent=2) + cola)


def leer_commit(nid, commit):
    p = subprocess.run(["git", "show", "%s:dataset/nodos/%s.json" % (commit, nid)],
                       capture_output=True, cwd=RAIZ)
    if p.returncode != 0:
        return None
    return json.loads(p.stdout.decode("utf-8"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--antes", required=True,
                    help="sha del commit ANTERIOR a la fusion del lote")
    ap.add_argument("--ejecutar", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 78)
    print("PUNTUACION DE LOS INCISOS DE LA VUELTA 56, reparada donde queda una")
    print("juntura de punto mas coma. MODO %s" % ("ESCRIBIR" if a.ejecutar else "SIMULAR"))
    print("=" * 78)
    print()
    print("  estado ANTES de las fusiones, leido por git del commit %s" % a.antes)
    print()

    tocar, saltados, ya = [], [], 0
    cadenas = {}
    for L in LOTES:
        ruta = os.path.join(LOOP, "PLAN_V56_OPU01_LOTE_%s.json" % L)
        if not os.path.exists(ruta):
            continue
        plan = json.load(io.open(ruta, encoding="utf-8"))
        for act in plan["actos"]:
            sup = act["superviviente"]
            antes = leer_commit(sup, a.antes)
            if antes is None:
                saltados.append((L, act["orden"], sup, "no se pudo leer del commit"))
                continue
            ps_antes = antes.get("pasos_accionables") or []
            for muere, marcas in act["pasos"].items():
                for idx, m in sorted(marcas.items(), key=lambda x: int(x[0])):
                    if not m.startswith("INCISO:"):
                        continue
                    cual, inciso, nexo = m[len("INCISO:"):].split("|")
                    k = int(cual)
                    if not (1 <= k <= len(ps_antes)):
                        saltados.append((L, act["orden"], sup, "INCISO al paso %d inexistente" % k))
                        continue
                    cadenas.setdefault((L, act["orden"], sup, k), []).append((nexo, inciso))

    # UN PASO PUEDE LLEVAR MAS DE UN INCISO ADOSADO (el acto 11 lleva DOS al
    # mismo paso), y entonces la juntura no es nexo+inciso sino la CADENA
    # entera en su orden. Se reconstruye completa y solo se toca el punto de
    # la PRIMERA juntura, que es el unico defectuoso.
    for (L, orden, sup, k), piezas in sorted(cadenas.items()):
        antes = leer_commit(sup, a.antes)
        ps_antes = (antes or {}).get("pasos_accionables") or []
        if not (1 <= k <= len(ps_antes)):
            saltados.append((L, orden, sup, "INCISO al paso %d inexistente" % k))
            continue
        orig = ps_antes[k - 1]
        cola = "".join(n + i for n, i in piezas)
        if not (orig.endswith(".") and piezas[0][0].startswith(",")):
            continue  # la juntura no tiene el defecto
        tocar.append({"lote": L, "acto": orden, "sup": sup, "k": k,
                      "esperado": orig + cola, "corregido": orig[:-1] + cola})

    print("--- LAS JUNTURAS CON EL DEFECTO, LOCALIZADAS EN LOS PLANES SELLADOS ---")
    print("  junturas con punto mas coma: %d" % len(tocar))
    print()

    cambios, colas, rojo = {}, {}, []
    for t in tocar:
        if t["sup"] not in cambios:
            cambios[t["sup"]], colas[t["sup"]] = leer_nodo(t["sup"])
        d = cambios[t["sup"]]
        ps = d.get("pasos_accionables") or []
        i = t["k"] - 1
        if i >= len(ps):
            rojo.append((t, "el superviviente ya no tiene el paso %d" % t["k"]))
            continue
        if ps[i] == t["corregido"]:
            ya += 1
            continue
        if ps[i] != t["esperado"]:
            rojo.append((t, "el paso actual NO es la juntura esperada"))
            continue
        # LA COMPROBACION QUE HACE ESTO SEGURO: un solo caracter menos.
        if len(t["corregido"]) != len(t["esperado"]) - 1:
            rojo.append((t, "la correccion no borra exactamente un caracter"))
            continue
        ps[i] = t["corregido"]
        print("  acto %-3d %-46s paso %d" % (t["acto"], t["sup"], t["k"]))
        print("      antes  : %s" % t["esperado"])
        print("      despues: %s" % t["corregido"])

    print()
    if ya:
        print("  YA ESTABAN en su forma corregida: %d (idempotente)" % ya)
    if rojo:
        print("  ROJO en %d junturas, y NO se escribe NADA:" % len(rojo))
        for t, motivo in rojo:
            print("     acto %d, %s paso %d: %s" % (t["acto"], t["sup"], t["k"], motivo))
        return 1

    por_escribir = [t for t in tocar]
    if not por_escribir or ya == len(tocar):
        print("  nada que escribir.")
        print()
        print("FIN")
        return 0

    if a.ejecutar:
        for nid, d in sorted(cambios.items()):
            escribir_nodo(nid, d, colas[nid])
        print("  ESCRITO: %d ficheros de nodo, %d junturas corregidas"
              % (len(cambios), len(tocar) - ya))
    else:
        print("  MODO SIMULAR: no se escribe. Serian %d ficheros y %d junturas."
              % (len(cambios), len(tocar) - ya))
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
