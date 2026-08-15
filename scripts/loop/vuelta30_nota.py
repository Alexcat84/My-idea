"""Vuelta 30: anade una CORRECCION DECLARADA al campo nota de una operacion.

El texto viejo se queda entero delante: esta herramienta solo concatena. Es la
forma generica de lo que scripts/loop/vuelta30_registros.py hizo a mano para
OP-F-02 y OP-F-03, y existe porque la vuelta 30 tiene que escribir varias notas
en momentos distintos (el corte unico de P.20 primero, el saldo de cada tanda
despues) sin reescribir un script por cada una.

GUARDA: si la nota ya trae la marca exacta que se le va a anadir, PARA. Escribir
dos veces la misma correccion es ensuciar el registro, no reforzarlo.

Uso:
    python scripts/loop/vuelta30_nota.py <fichero_de_notas.json> --simular
    python scripts/loop/vuelta30_nota.py <fichero_de_notas.json> --ejecutar

El fichero de notas es {"marca": "...", "notas": {"OP-X": "texto a anadir", ...}}
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")


def main():
    if len(sys.argv) < 3 or sys.argv[2] not in ("--simular", "--ejecutar"):
        print(__doc__)
        return 2
    ficha = json.load(open(sys.argv[1], encoding="utf-8"))
    ejecutar = sys.argv[2] == "--ejecutar"
    marca = ficha["marca"]

    lineas = []
    with open(OPS, encoding="utf-8") as fh:
        for linea in fh:
            if linea.strip():
                lineas.append(json.loads(linea))
    porid = {o["id_op"]: o for o in lineas}

    faltan = [i for i in ficha["notas"] if i not in porid]
    if faltan:
        print("PARA: operaciones inexistentes: %s" % faltan)
        return 1

    print("MARCA: %s" % marca)
    print("=" * 78)
    for i, texto in ficha["notas"].items():
        o = porid[i]
        if marca in (o.get("nota") or ""):
            print("PARA: %s ya trae la marca. No se escribe nada." % i)
            return 1
        anadido = " " + marca + " " + texto
        print("\n%s: nota de %d caracteres, se le anaden %d"
              % (i, len(o.get("nota") or ""), len(anadido)))
        print("  %s" % anadido[:260])
        o["nota"] = (o.get("nota") or "") + anadido

    if not ejecutar:
        print("\nSIMULACION: cero escrituras.")
        return 0

    with open(OPS, "w", encoding="utf-8", newline="") as fh:
        for o in lineas:
            fh.write(json.dumps(o, ensure_ascii=False) + "\n")
    print("\nESCRITO: %d nota(s) en docs/plan/OPERACIONES.jsonl (%d lineas)."
          % (len(ficha["notas"]), len(lineas)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
