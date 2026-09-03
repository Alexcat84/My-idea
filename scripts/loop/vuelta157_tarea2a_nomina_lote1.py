# -*- coding: utf-8 -*-
"""vuelta157_tarea2a_nomina_lote1.py . TAREA 2.a DE LA VUELTA 157.

LA NOMINA DEL LOTE 1 SALE DE UN COMPUTO, NO DE UNA LISTA TECLEADA. El encargo da
las cifras que el auditor midio y este instrumento LAS RECOMPUTA de
`docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl`. Si no da 6 con puntero y 60 sin
puntero, SALE ROJO Y NO SE LEE NADA.

LA CUENTA DE PARTIDA QUE EL ENCARGO DECLARA (auditor, acta 157):
    122 lecturas dirigidas
    116 sin puntero de paso, de ellas 3 ya en D
      6 con puntero de paso
    113 todavia en C sin puntero

QUE ES UN PUNTERO DE PASO, Y ES LA VARA DEL AUDITOR TAL COMO EL LA DECLARO (acta
157, seccion 5.1): la razon nombra `paso N`, y SE MIRA SOLO EL TEXTO ORIGINAL DE
LA RAZON, o sea lo que hay ANTES del primer corchete de adjudicacion (`  [`).
Las adjudicaciones que las vueltas posteriores anadieron a una razon NO cuentan
como puntero: si contaran, una lectura pasaria a tener figura por lo que un acta
escribio encima de ella, que es justo al reves.

EL LOTE 1 SON 66: las SEIS con puntero mas las SESENTA primeras POR NUMERO de
las que siguen en C sin puntero.

USO:  python scripts/loop/vuelta157_tarea2a_nomina_lote1.py
"""
import io
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REGISTRO = os.path.join(RAIZ, "docs", "plan", "REGISTRO_DE_CITAS_OPC05.jsonl")
NOMINA = os.path.join(RAIZ, "docs", "loop", "NOMINA_V157_LOTE1.json")

PUNTERO = re.compile(r"\bpaso\s+\d+", re.IGNORECASE)


def entradas():
    return [json.loads(x) for x in
            io.open(REGISTRO, encoding="utf-8").read().splitlines() if x.strip()]


def razon_original(razon):
    """El texto de la razon ANTES del primer corchete de adjudicacion."""
    i = razon.find("  [")
    return razon if i < 0 else razon[:i]


def ld_de(e):
    return e["cita"].split(",")[0].strip()


def main():
    E = entradas()
    L = [e for e in E if e.get("via") == "LECTURA_DIRIGIDA"]
    L.sort(key=lambda e: ld_de(e))
    print("=" * 78)
    print("VUELTA 157, TAREA 2.a: LA NOMINA DEL LOTE 1, RECOMPUTADA")
    print("=" * 78)
    print("")
    print("CIFRA entradas del registro de citas: %d" % len(E))
    print("CIFRA entradas con via LECTURA_DIRIGIDA: %d" % len(L))

    con_p = [e for e in L if PUNTERO.search(razon_original(e["razon"]))]
    sin_p = [e for e in L if not PUNTERO.search(razon_original(e["razon"]))]
    sin_p_d = [e for e in sin_p if e["clase"] == "D"]
    sin_p_c = [e for e in sin_p if e["clase"] == "C"]
    con_p_c = [e for e in con_p if e["clase"] == "C"]

    print("CIFRA lecturas dirigidas CON puntero de paso: %d" % len(con_p))
    print("CIFRA lecturas dirigidas SIN puntero de paso: %d" % len(sin_p))
    print("CIFRA de esas sin puntero que YA estan en D: %d (%s)"
          % (len(sin_p_d), ", ".join(ld_de(e) for e in sin_p_d)))
    print("CIFRA todavia en C SIN puntero: %d" % len(sin_p_c))
    print("CIFRA todavia en C CON puntero: %d" % len(con_p_c))
    print("")

    print("LAS SEIS CON PUNTERO, UNA A UNA:")
    for e in con_p:
        m = PUNTERO.findall(razon_original(e["razon"]))
        print("  %-16s clase %-3s punteros: %s" % (ld_de(e), e["clase"], ", ".join(m)))
    print("")

    esperado_con, esperado_sin = 6, 60
    if len(con_p_c) != esperado_con:
        print("ROJO: se esperaban %d con puntero todavia en C y el computo da %d."
              % (esperado_con, len(con_p_c)))
        print("SE PARA Y NO SE LEE NADA.")
        print("FIN")
        return 1

    primeras = sin_p_c[:esperado_sin]
    if len(primeras) != esperado_sin:
        print("ROJO: se esperaban %d sin puntero en C para el lote y solo hay %d."
              % (esperado_sin, len(primeras)))
        print("SE PARA Y NO SE LEE NADA.")
        print("FIN")
        return 1

    lote = sorted(con_p_c + primeras, key=lambda e: ld_de(e))
    ids = [ld_de(e) for e in lote]
    print("EL LOTE 1: %d lecturas" % len(lote))
    print("  las SEIS con puntero : %s" % ", ".join(sorted(ld_de(e) for e in con_p_c)))
    print("  las SESENTA sin puntero van de %s a %s"
          % (ld_de(primeras[0]), ld_de(primeras[-1])))
    print("")
    print("LA NOMINA ENTERA, EN ORDEN:")
    for i in range(0, len(ids), 6):
        print("  " + "  ".join("%-16s" % x for x in ids[i:i + 6]))
    print("")

    with io.open(NOMINA, "w", encoding="utf-8", newline="\n") as fh:
        json.dump({"lote": ids,
                   "con_puntero": sorted(ld_de(e) for e in con_p_c),
                   "sin_puntero": [ld_de(e) for e in primeras]},
                  fh, ensure_ascii=False, indent=1)
    print("CIFRA lecturas del lote 1: %d" % len(lote))
    print("nomina sellada en docs/loop/NOMINA_V157_LOTE1.json")
    print("")
    print("VERDE: el computo da %d con puntero y %d sin puntero, que es lo que el"
          % (len(con_p_c), len(primeras)))
    print("encargo declara. Se puede leer.")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
