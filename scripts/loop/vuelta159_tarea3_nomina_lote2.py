# -*- coding: utf-8 -*-
"""vuelta159_tarea3_nomina_lote2.py . TAREA 3 DE LA VUELTA 159, LA NOMINA DEL
LOTE 2 DEL SACO.

LA CIFRA NO SE TECLEA Y NO SE CREE. El encargo y la adjudicacion 6.12 del acta
158 dicen 53, de `LD-OPC05-068` a `LD-OPC05-121`, y NINGUNA con puntero de paso
porque el saco pequeno se agoto entero en el lote 1. ESTE INSTRUMENTO LO
RECOMPUTA de `docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl`. Si no da 53, SALE ROJO Y
NO SE LEE NADA.

QUE ES EL LOTE 2, DICHO COMO SE COMPUTA: las lecturas dirigidas que SIGUEN EN C
tras la TAREA 2 de esta vuelta y que NO ha leido ningun lote. Se comprueban las
tres cosas por separado y se publican las tres:
  (a) que son exactamente las que van de 068 a 121;
  (b) que NINGUNA trae puntero de paso en su razon ORIGINAL (el texto anterior
      al primer corchete de adjudicacion, la misma vara del auditor que uso la
      nomina del lote 1);
  (c) que las C que quedan FUERA del lote 2 son las cuatro que ya se leyeron
      (038 y 049, que sostuvieron C en el lote 1; 005 y 052, que volvieron a C
      en la TAREA 2 de esta vuelta), y se nombran una a una.

USO:  python scripts/loop/vuelta159_tarea3_nomina_lote2.py
"""
import io
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REGISTRO = os.path.join(RAIZ, "docs", "plan", "REGISTRO_DE_CITAS_OPC05.jsonl")
SALIDA = os.path.join(RAIZ, "docs", "loop", "NOMINA_V159_LOTE2.json")

PUNTERO = re.compile(r"\bpaso\s+\d+", re.IGNORECASE)
ESPERADO = 53
DESDE, HASTA = 68, 121


def leer(ruta):
    return io.open(ruta, encoding="utf-8").read()


def entradas():
    return [json.loads(x) for x in leer(REGISTRO).splitlines() if x.strip()]


def ld_de(e):
    return e["cita"].split(",")[0].strip()


def razon_original(razon):
    i = razon.find("  [")
    return razon if i < 0 else razon[:i]


def main():
    print("=" * 78)
    print("VUELTA 159, TAREA 3: LA NOMINA DEL LOTE 2, RECOMPUTADA")
    print("=" * 78)
    print("")

    E = entradas()
    L = sorted([e for e in E if e.get("via") == "LECTURA_DIRIGIDA"], key=ld_de)
    print("CIFRA entradas del registro de citas: %d" % len(E))
    print("CIFRA entradas con via LECTURA_DIRIGIDA: %d" % len(L))
    clases = {}
    for e in L:
        clases[e["clase"]] = clases.get(e["clase"], 0) + 1
    print("CIFRA lecturas dirigidas por clase: %s" % json.dumps(clases, sort_keys=True))
    print("")

    en_c = [e for e in L if e["clase"] == "C"]
    print("A) LAS C QUE QUEDAN, Y DE DONDE SALE CADA UNA")
    print("   CIFRA lecturas dirigidas todavia en C: %d" % len(en_c))
    dentro = [e for e in en_c if DESDE <= int(ld_de(e).split("-")[-1]) <= HASTA]
    fuera = [e for e in en_c if e not in dentro]
    print("   CIFRA de esas que caen en el rango %03d a %03d: %d"
          % (DESDE, HASTA, len(dentro)))
    print("   CIFRA de esas que caen FUERA del rango: %d (%s)"
          % (len(fuera), ", ".join(ld_de(e) for e in fuera)))
    print("   Las de fuera son las YA LEIDAS: dos que sostuvieron C en el lote 1")
    print("   y dos que volvieron a C en la TAREA 2 de esta vuelta.")
    print("")

    print("B) EL PUNTERO DE PASO, COMPROBADO Y NO SUPUESTO")
    con_p = [e for e in dentro if PUNTERO.search(razon_original(e["razon"]))]
    print("   CIFRA del lote 2 CON puntero de paso en su razon original: %d" % len(con_p))
    for e in con_p:
        print("      %s : %s" % (ld_de(e), PUNTERO.findall(razon_original(e["razon"]))))
    if con_p:
        print("   ROJO: el encargo declara que NINGUNA trae puntero y el computo halla %d."
              % len(con_p))
        print("   SE PARA Y NO SE LEE NADA.")
        print("FIN")
        return 1
    print("   NINGUNA. El saco pequeno se agoto entero en el lote 1, como declara la 6.12.")
    print("")

    ids = [ld_de(e) for e in dentro]
    print("C) EL LOTE 2, RECOMPUTADO")
    print("   CIFRA lecturas del lote 2: %d" % len(ids))
    print("   CIFRA que el encargo y la 6.12 declaran: %d" % ESPERADO)
    if ids:
        print("   va de %s a %s" % (ids[0], ids[-1]))
    print("")
    print("LA NOMINA ENTERA, EN ORDEN:")
    for i in range(0, len(ids), 6):
        print("  " + "  ".join("%-16s" % x for x in ids[i:i + 6]))
    print("")

    if len(ids) != ESPERADO:
        print("ROJO: el computo da %d y el encargo declara %d." % (len(ids), ESPERADO))
        print("SE PARA Y NO SE LEE NADA.")
        print("FIN")
        return 1

    with io.open(SALIDA, "w", encoding="utf-8", newline="\n") as fh:
        json.dump({"lote": ids,
                   "c_fuera_del_lote": [ld_de(e) for e in fuera]},
                  fh, ensure_ascii=False, indent=1)
    print("nomina sellada en docs/loop/NOMINA_V159_LOTE2.json")
    print("")
    print("VERDE: el computo reproduce la cifra del encargo. Se puede leer.")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
