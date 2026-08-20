# -*- coding: utf-8 -*-
"""vuelta56_tallar_planes.py . TALLA LAS TABLAS DE LA VUELTA 56 DESDE LOS PLANES
SELLADOS, PARA QUE NINGUNA CELDA SE TECLEE.

SUCESOR DECLARADO de scripts/loop/vuelta55_tallar_planes.py, cuya aritmetica se
copia entera. LO UNICO QUE CAMBIA: los ficheros son los PLAN_V56_*.json, los
lotes son A, B y C, la lista de FRASES DE CABECERA reconoce las formas que esta
vuelta uso, y se anade UNA TABLA MAS, la de los actos DECLARADOS Y NO FUNDIDOS,
que la vuelta 55 no necesitaba en su tallador porque su registro los llevaba a
mano.

LA FORMA DEL VEREDICTO NO SE ADIVINA: se lee del propio motivo sellado por su
frase de cabecera. Si un motivo no empieza por ninguna de las frases conocidas,
sale ROJO con el acto nombrado en vez de caer en una categoria por defecto: una
clasificacion silenciosa es justo la caida que este instrumento existe para no
repetir.

DE SOLO LECTURA. No escribe ningun fichero: imprime.

Uso: python scripts/loop/vuelta56_tallar_planes.py
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
FORMAS = [
    ("LA GUARDA RESTRINGE Y EL CONTENIDO ELIGE",
     "LA PUERTA SOBREVIVE, con el choque registrado"),
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
    print("LAS TABLAS DE LA VUELTA 56, TALLADAS DE LOS PLANES SELLADOS")
    print("=" * 78)
    print()

    todos = []
    rojo = []
    for L in LOTES:
        p = os.path.join(LOOP, "PLAN_V56_OPU01_LOTE_%s.json" % L)
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
        p = os.path.join(LOOP, "PLAN_V56_OPU01_LOTE_%s.json" % L)
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
