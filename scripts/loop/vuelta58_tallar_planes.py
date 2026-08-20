# -*- coding: utf-8 -*-
"""vuelta58_tallar_planes.py . SUCESOR DECLARADO de scripts/loop/vuelta57_tallar_planes.py,
al que NO reemplaza. LA ARITMETICA ES LA SUYA, COPIADA ENTERA Y NO RETECLEADA (el
fichero se copio byte a byte y solo despues se le anadio lo de abajo): las formas se
leen del MOTIVO SELLADO, las piezas se cuentan de las marcas del plan, y el
instrumento cae en ROJO con el acto nombrado si un motivo no encaja en ninguna forma
conocida.

POR QUE NACE. La TAREA 1.1 de la vuelta 58 DESHIZO el acto 32 del tramo 4: la
relectura conjunta confirmo el caso del auditor (acta 57, D4) y el acto quedo
DECLARADO por empate sin vara. Las cuatro tablas del registro del tramo 4 en
docs/plan/03_FUSIONES.md salieron del ancestro y ahora publican 44 fusiones donde
hay 43, y una forma (LOS TRES CONTEOS EMPATAN y decide la pieza declarada POR
CANTIDAD) que ya no existe en el tramo. La regla 1 dice que esas tablas se generan
del instrumento y se pegan enteras: para eso hace falta que el instrumento sepa que
un acto SELLADO fue retirado despues.

EL PLAN SELLADO NO SE TOCA, Y ESE ES EL PUNTO. Los PLAN_V57_*.json se quedan como
estan, con el acto 32 dentro y su motivo entero, porque un plan sellado es el
registro de lo que se decidio aquel dia y reescribirlo taparia lo que se corrige.
Lo que este sucesor anade es UN ARGUMENTO, --retirado, que saca al acto de las
tablas de fusion y lo pasa a la de DECLARADOS con su especie y su carril, dejando
constancia impresa de que el motivo sellado sigue ahi.

LO UNICO QUE CAMBIA:
  --retirado N|especie|carril   (repetible) retira el acto N de las tablas 1, 2 y 3
                                y lo anade a la tabla 4 con esa especie y ese carril.
  --vuelta N                    el titulo, que en el ancestro era constante.
Ninguna celda de la aritmetica se toca. Sin --retirado, este fichero imprime
EXACTAMENTE lo mismo que su ancestro, y eso se comprueba corriendo los dos.

DE SOLO LECTURA. No toca ni un nodo ni un plan: imprime.
"""

import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
LOTES = ["A", "B", "C"]

# Las frases de cabecera que el generador de planes escribe al principio de cada
# motivo. El orden importa: se prueba de la mas especifica a la mas general.
# LAS FRASES QUE ESTA VUELTA ANADE van marcadas: son formas que el tramo 4
# estreno y que el tallador de la vuelta 56 no podia reconocer. Ninguna de las
# viejas se toca ni se renombra, para que las dos corridas sigan comparables.
FORMAS = [
    ("LA GUARDA RESTRINGE Y ADEMAS LOS TRES CONTEOS",
     "LA PUERTA SOBREVIVE y los conteos concuerdan, contra la razon declarada"),
    ("LA GUARDA RESTRINGE Y EL CONTENIDO ELIGE",
     "LA PUERTA SOBREVIVE, con el choque registrado"),
    ("LA PIEZA DECLARADA GANA A UN CONTEO",
     "LA PIEZA DECLARADA GANA A UN CONTEO de contenido"),
    ("LOS TRES CONTEOS EMPATAN Y DECIDE LA PIEZA DECLARADA POR CANTIDAD",
     "LOS TRES CONTEOS EMPATAN y decide la pieza declarada POR CANTIDAD"),
    ("LOS CONTEOS EMPATAN Y LA PIEZA DECLARADA DECIDE",
     "LOS CONTEOS EMPATAN y la PIEZA DECLARADA decide"),
    ("TODAS LAS VARAS DE CONTENIDO DE ACUERDO",
     "TODAS LAS VARAS de contenido de acuerdo"),
    ("CONTEOS DE CONTENIDO CONTRA PIEZA DECLARADA",
     "CONTEOS QUE CHOCAN CON LA PIEZA DECLARADA, y decide la declarada"),
    ("CONTENIDO, UNA SOLA VARA NO EMPATADA",
     "UNA SOLA VARA de contenido no empatada, y BASTA"),
    ("CONTENIDO, TODAS LAS VARAS DE ACUERDO",
     "TODAS LAS VARAS de contenido de acuerdo"),
    ("EL CONTENIDO EMPATA ENTERO Y EL CABLEADO DECIDE SOLO",
     "EL CONTENIDO EMPATA y EL CABLEADO DECIDE SOLO"),
]


def forma_de(motivo):
    for clave, nombre in FORMAS:
        if motivo.startswith(clave):
            return nombre
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vuelta", type=int, default=57)
    ap.add_argument("--retirado", action="append", default=[],
                    help="N|especie|carril . acto SELLADO que se retiro despues")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    # LO UNICO QUE ESTE SUCESOR ANADE, primera mitad: los retirados.
    retirados = {}
    for crudo in a.retirado:
        partes = crudo.split("|", 2)
        if len(partes) != 3 or not partes[0].strip().isdigit():
            print("  ROJO: --retirado mal formado (%s). Se espera N|especie|carril."
                  % crudo)
            return 1
        retirados[int(partes[0])] = (partes[1].strip(), partes[2].strip())

    print("=" * 78)
    print("LAS TABLAS DEL TRAMO 4, TALLADAS DE LOS PLANES SELLADOS (vuelta %d)" % a.vuelta)
    if retirados:
        print("ACTOS RETIRADOS DESPUES DEL SELLADO: %s"
              % ", ".join(str(n) for n in sorted(retirados)))
        print("El plan sellado NO se toca: el motivo del acto sigue entero en su fichero.")
    print("=" * 78)
    print()

    todos = []
    rojo = []
    sacados = []
    for L in LOTES:
        p = os.path.join(LOOP, "PLAN_V57_OPU01_LOTE_%s.json" % L)
        plan = json.load(io.open(p, encoding="utf-8"))
        for act in plan["actos"]:
            if act["orden"] in retirados:
                esp, carril = retirados[act["orden"]]
                sacados.append({"orden": act["orden"], "lote": L,
                                "miembros": act["miembros_del_acto_entero"],
                                "especie": esp, "acumula_para": carril,
                                "forma_sellada": forma_de(act["motivo"])})
                continue
            c = {"APPEND": 0, "CUBIERTO": 0, "INCISO": 0}
            for d in (act["pasos"], act["condiciones"]):
                for marcas in d.values():
                    for m in marcas.values():
                        k = ("APPEND" if m == "APPEND"
                             else "INCISO" if m.startswith("INCISO") else "CUBIERTO")
                        c[k] += 1
            f = forma_de(act["motivo"])
            if f is None:
                rojo.append((L, act["orden"]))
            perdidas = act["nota_del_reparto"].count("PERDIDA NOMBRADA")
            todos.append({"lote": L, "orden": act["orden"],
                          "sup": act["superviviente"], "abs": act["absorbidos"][0],
                          "forma": f, "piezas": sum(c.values()),
                          "append": c["APPEND"], "cubierto": c["CUBIERTO"],
                          "inciso": c["INCISO"], "perdidas": perdidas})

    if rojo:
        print("  ROJO: motivos cuya forma no se reconoce: %s" % rojo)
        return 1

    print("--- TABLA 1: LOS TRES LOTES, CON SUS PIEZAS ---")
    print()
    print("| lote | actos | fundidos | mueren | piezas | enteras | ya dichas | de `INCISO` | perdidas nombradas |")
    print("|---|---|---:|---:|---:|---:|---:|---:|---:|")
    for L in LOTES:
        f = [x for x in todos if x["lote"] == L]
        print("| **%s** | %s | **%d** | **%d** | **%d** | %d | %d | **%d** | **%d** |"
              % (L, ", ".join(str(x["orden"]) for x in f), len(f), len(f),
                 sum(x["piezas"] for x in f), sum(x["append"] for x in f),
                 sum(x["cubierto"] for x in f), sum(x["inciso"] for x in f),
                 sum(x["perdidas"] for x in f)))
    print("| **los tres** | | **%d** | **%d** | **%d** | **%d** | **%d** | **%d** | **%d** |"
          % (len(todos), len(todos), sum(x["piezas"] for x in todos),
             sum(x["append"] for x in todos), sum(x["cubierto"] for x in todos),
             sum(x["inciso"] for x in todos), sum(x["perdidas"] for x in todos)))
    print()

    print("--- TABLA 2: LA FORMA DEL VEREDICTO, CONTADA DE LOS MOTIVOS SELLADOS ---")
    print()
    cuenta = {}
    for x in todos:
        cuenta.setdefault(x["forma"], []).append(x["orden"])
    print("| la forma, leida del motivo sellado | cuantos | los actos |")
    print("|---|---:|---|")
    for f in sorted(cuenta, key=lambda k: (-len(cuenta[k]), k)):
        print("| **%s** | **%d** | %s |"
              % (f, len(cuenta[f]), ", ".join(str(n) for n in sorted(cuenta[f]))))
    print("| **suma** | **%d** | |" % sum(len(v) for v in cuenta.values()))
    print()

    print("--- TABLA 3: ACTO A ACTO, SUPERVIVIENTE Y ABSORBIDO ---")
    print()
    print("| acto | lote | sobrevive | absorbe | piezas | enteras | ya dichas | `INCISO` |")
    print("|---:|:---:|---|---|---:|---:|---:|---:|")
    for x in sorted(todos, key=lambda x: x["orden"]):
        print("| **%d** | %s | `%s` | `%s` | %d | %d | %d | %d |"
              % (x["orden"], x["lote"], x["sup"], x["abs"], x["piezas"],
                 x["append"], x["cubierto"], x["inciso"]))
    print()
    print("--- TABLA 4: LOS ACTOS DECLARADOS Y NO FUNDIDOS ---")
    print()
    print("| acto | lote | sus miembros | especie | se acumula para |")
    print("|---:|:---:|---|---|---|")
    # LO UNICO QUE ESTE SUCESOR ANADE, segunda mitad: los retirados entran aqui,
    # en su sitio por orden, junto a los que ya nacieron declarados.
    filas = []
    for L in LOTES:
        p = os.path.join(LOOP, "PLAN_V57_OPU01_LOTE_%s.json" % L)
        plan = json.load(io.open(p, encoding="utf-8"))
        for d in plan.get("declarados_y_no_fundidos", []):
            filas.append((d["orden"], L, d["miembros"], d["especie"],
                          d["acumula_para"]))
    for s in sacados:
        filas.append((s["orden"], s["lote"], s["miembros"], s["especie"],
                      s["acumula_para"]))
    for orden, L, miembros, especie, carril in sorted(filas):
        print("| **%d** | %s | %s | **%s** | %s |"
              % (orden, L, ", ".join("`%s`" % m for m in miembros), especie, carril))
    print("| **suma** | | **%d declarados** | | |" % len(filas))
    print()
    if sacados:
        print("--- TABLA 5: LOS RETIRADOS DESPUES DEL SELLADO, CON SU FORMA VIEJA ---")
        print()
        print("| acto | lote | la forma que el motivo SELLADO le dio | donde queda ahora |")
        print("|---:|:---:|---|---|")
        for s in sorted(sacados, key=lambda x: x["orden"]):
            print("| **%d** | %s | %s | **%s** |"
                  % (s["orden"], s["lote"], s["forma_sellada"], s["especie"]))
        print()
    print("  actos tallados: %d | piezas: %d | perdidas nombradas: %d | retirados: %d"
          % (len(todos), sum(x["piezas"] for x in todos),
             sum(x["perdidas"] for x in todos), len(sacados)))
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
