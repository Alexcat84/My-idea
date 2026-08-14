"""OP-F-03, tercera linea de verificacion: LA FUENTE SE CORRIGE en los nodos que
declaran un libro cuyo material no aparece.

Los dos nodos salen de la lectura de los 21, publicada en
docs/plan/01_FUENTES.md (seccion LOS 21 LEIDOS UNO A UNO). Este script NO decide:
aplica lo ya escrito.

Uso:
    python scripts/loop/vuelta26_opf03.py --simular
    python scripts/loop/vuelta26_opf03.py --ejecutar

La simulacion trabaja sobre copia en memoria y no escribe nada.
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")

# nodo -> (fuente que tiene que estar hoy, fuente que queda)
CORRECCIONES = {
    "gestion_libro_abierto_obm": (
        "Financial Intelligence for Entrepreneurs | "
        "Essentials of Supply Chain Management - Michael H. Hugos",
        "Financial Intelligence for Entrepreneurs",
    ),
    "seleccion_estrategia_pricing": (
        "The Startup Owner's Manual - Steve Blank | "
        "Essentials of Supply Chain Management - Michael H. Hugos",
        "The Startup Owner's Manual - Steve Blank",
    ),
}


def ruta(nid):
    return os.path.join(NODOS, nid + ".json")


def main():
    modo = sys.argv[1] if len(sys.argv) > 1 else "--simular"
    if modo not in ("--simular", "--ejecutar"):
        print(__doc__)
        return 2

    print("OP-F-03, correccion de fuente. Modo: %s" % modo)
    print("=" * 78)
    fallos = []
    for nid, (esperada, nueva) in CORRECCIONES.items():
        # EL FINAL DE FICHERO SE PRESERVA TAL CUAL. El dataset NO es uniforme:
        # unos nodos acaban en salto de linea y otros no, y escribir con
        # json.dump a secas le quita el salto al que lo tenia. Eso es un cambio
        # de formato que ninguna operacion ordena.
        with open(ruta(nid), encoding="utf-8", newline="") as fh:
            crudo = fh.read()
        cola = "\n" if crudo.endswith("\n") else ""
        d = json.loads(crudo)
        actual = d.get("fuente", "")
        print("\nNODO   : %s" % nid)
        print("ANTES  : %s" % actual)
        print("DESPUES: %s" % nueva)
        print("PASOS  : %d (no se toca ninguno)" % len(d.get("pasos_accionables", [])))
        if actual != esperada:
            fallos.append((nid, actual))
            print("  [ROJO] la fuente de hoy NO es la que este script espera. NO se toca.")
            continue
        print("  [OK] la fuente de hoy es exactamente la esperada")
        if modo == "--ejecutar":
            d["fuente"] = nueva
            with open(ruta(nid), "w", encoding="utf-8", newline="") as fh:
                fh.write(json.dumps(d, ensure_ascii=False, indent=2) + cola)
            print("  ESCRITO (final de fichero preservado: %r)" % cola)

    print()
    print("=" * 78)
    if fallos:
        print("PARADA: %d nodo(s) con fuente inesperada. Nada se escribio en ellos." % len(fallos))
        for nid, actual in fallos:
            print("  %s -> %r" % (nid, actual))
        return 1
    print("Los %d nodos calzan con lo esperado." % len(CORRECCIONES))
    if modo == "--simular":
        print("SIMULACION: cero escrituras.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
