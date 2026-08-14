"""OP-C-04: el CASO POSITIVO, en arbol de trabajo temporal y NUNCA commiteado.

Inyecta el estado malo que las dos guardas tienen que cazar:

  1. AUTO ARISTA VIA ALIAS: devuelve `value_stream_analysis_lean` a los
     nodos_previos de `analisis_flujo_de_valor`. Ese id es alias del propio
     nodo, asi que una guarda LITERAL lo deja pasar y una que RESUELVE lo caza.
     Es el ejemplar que la verificacion de OP-C-04 nombra por su nombre.

  2. CLAVE FUERA DE LA LISTA BLANCA: devuelve la clave `fase_проekto` (con
     п, р y о CIRILICAS) a `crosby_habilidad_transmision`. Es la clave exacta
     que OP-S-06 retiro, recuperada de su forma original en el commit fa2e6011,
     no retipeada a ojo.

El estado malo vive SOLO en el arbol de trabajo. Se restaura con
`git checkout -- dataset/` acto seguido, y la salida del Gate 0 caido queda
como prueba en docs/loop/.

Uso:
  python scripts/loop/vuelta24_opc04_caso_positivo.py --inyectar
  python scripts/loop/vuelta24_opc04_caso_positivo.py --comprobar
"""

import argparse
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")

# п, р y о cirilicas. Se escribe por punto de codigo para que ni un editor ni
# una copia por pantalla puedan convertirla en su gemela latina sin que se note.
CLAVE_CIRILICA = "fase_" + "про" + "ekto"

AUTO_ARISTA = ("analisis_flujo_de_valor", "nodos_previos", "value_stream_analysis_lean")
CLAVE_SUCIA = ("crosby_habilidad_transmision", CLAVE_CIRILICA, "ejecucion")


def _ruta(nid):
    return os.path.join(NODOS, nid + ".json")


def _leer(nid):
    with open(_ruta(nid), encoding="utf-8") as fh:
        return json.load(fh)


def _escribir(nid, d):
    # formato IDENTICO al save_node del validador (scripts/run_phase1.py:103)
    with open(_ruta(nid), "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=2)


def inyectar():
    print("CLAVE CIRILICA que se va a inyectar: %s"
          % CLAVE_CIRILICA.encode("unicode_escape").decode("ascii"))
    print("  puntos de codigo: %s" % [hex(ord(c)) for c in CLAVE_CIRILICA])
    print("  se ve identica a 'fase_proekto' en pantalla y NO lo es")
    print()

    nid, campo, dest = AUTO_ARISTA
    d = _leer(nid)
    lista = d.get(campo) or []
    if dest in lista:
        print("1) AUTO ARISTA: ya estaba, no se toca")
    else:
        lista.append(dest)
        d[campo] = lista
        _escribir(nid, d)
        print("1) AUTO ARISTA inyectada: %s . %s += %s" % (nid, campo, dest))

    nid2, clave, valor = CLAVE_SUCIA
    d2 = _leer(nid2)
    if clave in d2:
        print("2) CLAVE SUCIA: ya estaba, no se toca")
    else:
        d2[clave] = valor
        _escribir(nid2, d2)
        print("2) CLAVE SUCIA inyectada: %s . %s = %r"
              % (nid2, clave.encode("unicode_escape").decode("ascii"), valor))
    print()
    print("ESTADO MALO EN EL ARBOL DE TRABAJO. Restaurar con: git checkout -- dataset/")


def comprobar():
    """Confirma que el estado malo esta puesto, antes de correr el Gate."""
    nid, campo, dest = AUTO_ARISTA
    hay_arista = dest in (_leer(nid).get(campo) or [])
    nid2, clave, _ = CLAVE_SUCIA
    hay_clave = clave in _leer(nid2)
    print("auto arista via alias presente: %s" % hay_arista)
    print("clave cirilica presente:        %s" % hay_clave)
    print("claves de %s: %s"
          % (nid2, [k.encode("unicode_escape").decode("ascii") for k in _leer(nid2)]))
    return 0 if (hay_arista and hay_clave) else 1


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--inyectar", action="store_true")
    p.add_argument("--comprobar", action="store_true")
    a = p.parse_args()
    if a.inyectar:
        inyectar()
        return 0
    if a.comprobar:
        return comprobar()
    p.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
