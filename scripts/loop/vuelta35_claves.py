# -*- coding: utf-8 -*-
"""vuelta35_claves.py - SOLO LECTURA. Las claves reales del archivo de veredictos.

Nace de un fallo propio y por eso queda escrito en vez de borrarse: la primera
version de vuelta35_pares_opd03.py busco los ids en los campos id_a e id_b y
encontro CERO de quince pares. Adivinar el nombre de un campo es adivinar
(EJECUTOR.md regla 11), y la cura es mirar el fichero.

Uso: python scripts/loop/vuelta35_claves.py
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")


def main():
    V = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
    print("registros: %d" % len(V))
    print("claves del primero: %s" % sorted(V[0].keys()))
    print()
    for v in V:
        if v.get("puesto_intra") == 452:
            print("--- EL PUESTO 452, entero salvo la razon ---")
            for k in sorted(v.keys()):
                s = json.dumps(v[k], ensure_ascii=False)
                print("  %-22s %s" % (k, s[:400]))
            break
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
