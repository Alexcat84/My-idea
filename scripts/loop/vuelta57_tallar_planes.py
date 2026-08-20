# -*- coding: utf-8 -*-
"""vuelta57_tallar_planes.py . SUCESOR DECLARADO de scripts/loop/vuelta56_tallar_planes.py,
al que NO reemplaza. LA ARITMETICA ES LA SUYA, COPIADA ENTERA Y NO RETECLEADA: las
formas se leen del MOTIVO SELLADO por expresion regular, las piezas se cuentan de las
marcas del plan, y el instrumento cae en ROJO con el acto nombrado si un motivo no
encaja en ninguna forma conocida.

LO UNICO QUE CAMBIA, y va declarado porque es lo unico que no es copia: los ficheros
son los PLAN_V57_OPU01_LOTE_*.json y el tramo es el 4. El ancestro lleva la vuelta
escrita a mano en la ruta, y por eso hace falta un fichero nuevo en vez de un
argumento: sus cifras ya las cita el registro del tramo 3 en docs/plan/03_FUSIONES.md,
y esa es la figura que la vara del acta 54, pregunta 3, manda resolver con SUCESOR
DECLARADO Y ARITMETICA COPIADA.

DE SOLO LECTURA. No toca ni un nodo ni un plan: imprime.
"""

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
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("LAS TABLAS DE LA VUELTA 57, TALLADAS DE LOS PLANES SELLADOS")
    print("=" * 78)
    print()

    todos = []
    rojo = []
    for L in LOTES:
        p = os.path.join(LOOP, "PLAN_V57_OPU01_LOTE_%s.json" % L)
        plan = json.load(io.open(p, encoding="utf-8"))
        for act in plan["actos"]:
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
    ndec = 0
    for L in LOTES:
        p = os.path.join(LOOP, "PLAN_V57_OPU01_LOTE_%s.json" % L)
        plan = json.load(io.open(p, encoding="utf-8"))
        for d in plan.get("declarados_y_no_fundidos", []):
            ndec += 1
            print("| **%d** | %s | %s | **%s** | %s |"
                  % (d["orden"], L, ", ".join("`%s`" % m for m in d["miembros"]),
                     d["especie"], d["acumula_para"]))
    print("| **suma** | | **%d declarados** | | |" % ndec)
    print()
    print("  actos tallados: %d | piezas: %d | perdidas nombradas: %d"
          % (len(todos), sum(x["piezas"] for x in todos),
             sum(x["perdidas"] for x in todos)))
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
