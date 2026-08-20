# -*- coding: utf-8 -*-
"""retirar_entrada_redundante.py . P.16 A POSTERIORI: RETIRA UNA ENTRADA QUE UNA
FUSION YA CONSUMADA DEJO REDUNDANTE, EN LOS DOS SENTIDOS.

NOMBRE ESTABLE (acta 58, pregunta 4): el sujeto entra entero por argumento
(--nodo, --campo, --entrada) y el titulo no talla ninguna cifra.

SUCESOR DECLARADO, EN FORMA, de scripts/loop/vuelta43_retirar_arista_interna.py:
retirar la entrada Y SU RECIPROCA, porque retirar una sola deja la vista coja y
el paso 5 de run_phase1 la vuelve a escribir.

POR QUE NACE, y el motivo esta MEDIDO, no supuesto. El instrumento de P.16
(scripts/loop/retirar_duplicada_por_resolutor.py) corre ANTES de fundir, sobre
el arbol todavia sin tocar. En el lote A del tramo 5 de la vuelta 59 se le
escapo UNA duplicada por una regla que su ancestro traia (si la otra entrada ES
el superviviente escrito con su propio nombre, el ejecutor deduplica solo), y
esa regla vale SOLO cuando el culpable es el absorbido literal: si llega por un
alias, el ejecutor no lo sustituye y la duplicada sobrevive. La regla ya quedo
arreglada en aquel instrumento para las proximas corridas, PERO el lote de esta
vuelta ya estaba fundido cuando el censo del cierre lo destapo, y aquel
instrumento no sabe correr sobre un arbol ya fundido. P.16 dice QUIEN FABRICA
LIMPIA, asi que se limpia aqui en vez de dejarse de pasivo.

EL CASO MEDIDO QUE LO ESTRENA:
  definicion_calidad_conformidad | nodos_siguientes
  nombra a la vez a programa_catorce_pasos_crosby y a
  programa_mejora_calidad_14_pasos. El primero es alias (por cadena) del
  segundo desde que el acto 1 fundio programa_de_mejora_de_calidad, asi que los
  dos resuelven al mismo vivo y la entrada por alias sobra.

LA GUARDA QUE HACE LEGITIMO RETIRAR, y sin ella no escribe nada: OTRA entrada de
la misma lista tiene que resolver YA al mismo destino. Lo que se retira es lo
que la fusion volvio REDUNDANTE, nunca un camino con contenido propio. Si esa
condicion no se cumple, es ROJO.

NO toca el texto de ningun nodo: ni pasos, ni condiciones, ni titulo, ni
etiqueta, ni resumen, ni entregable. Solo nodos_previos y nodos_siguientes.

Uso:
  python scripts/loop/retirar_entrada_redundante.py --nodo N --campo C --entrada E
  ... --ejecutar
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
OPUESTO = {"nodos_previos": "nodos_siguientes", "nodos_siguientes": "nodos_previos"}


def ruta(nid):
    return os.path.join(NODOS, nid + ".json")


def leer(nid):
    return json.loads(io.open(ruta(nid), encoding="utf-8").read())


def escribir(nid, d):
    io.open(ruta(nid), "w", encoding="utf-8", newline="\n").write(
        json.dumps(d, ensure_ascii=False, indent=2) + "\n")


def mapa_alias():
    """La cadena ENTERA, incluidos los deprecados, que es como la lee el censo
    docs/plan/ARISTAS_DUPLICADAS.jsonl. El instrumento de antes de fundir solo
    mira los vivos, y por eso no ve este caso."""
    out = {}
    for nombre in sorted(os.listdir(NODOS)):
        if not nombre.endswith(".json"):
            continue
        d = leer(nombre[:-5])
        for x in (d.get("ids_alias") or []):
            out[x] = d["node_id"]
    return out


def resolver(mapa, x):
    v = set()
    while x in mapa and x not in v:
        v.add(x)
        x = mapa[x]
    return x


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nodo", required=True)
    ap.add_argument("--campo", required=True, choices=sorted(OPUESTO))
    ap.add_argument("--entrada", required=True)
    ap.add_argument("--ejecutar", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 78)
    print("P.16 A POSTERIORI: UNA ENTRADA REDUNDANTE, EN LOS DOS SENTIDOS")
    print("MODO %s" % ("EJECUTAR" if a.ejecutar else "SIMULAR"))
    print("=" * 78)
    print("  %s | %s | retirar %s" % (a.nodo, a.campo, a.entrada))
    print()

    alias = mapa_alias()
    d = leer(a.nodo)
    lista = d.get(a.campo) or []
    if a.entrada not in lista:
        print("  ROJO: %s no esta en %s.%s. No se escribe nada." % (a.entrada, a.nodo, a.campo))
        return 1

    destino = resolver(alias, a.entrada)
    otras = [x for x in lista if x != a.entrada and resolver(alias, x) == destino]
    print("  la entrada resuelve a : %s" % destino)
    print("  otras entradas de la misma lista que YA resuelven ahi: %s"
          % (", ".join(otras) if otras else "NINGUNA"))
    print()
    if not otras:
        print("  ROJO: ninguna otra entrada resuelve a ese destino, asi que esta NO es")
        print("        redundante: retirarla PERDERIA el camino. No se escribe nada.")
        return 1

    print("  VERDE: el camino se conserva por %s, y la entrada que se retira sobra." % otras[0])
    print("  SE RETIRA %s de %s.%s, y la reciproca en %s.%s"
          % (a.entrada, a.nodo, a.campo, a.entrada, OPUESTO[a.campo]))
    print()
    if not a.ejecutar:
        print("  MODO SIMULAR: no se escribe nada.")
        print()
        print("FIN")
        return 0

    tocados = 0
    d[a.campo] = [x for x in lista if x != a.entrada]
    escribir(a.nodo, d)
    tocados += 1
    print("  retirado: %s.%s ya no nombra a %s" % (a.nodo, a.campo, a.entrada))

    da = leer(a.entrada)
    op = OPUESTO[a.campo]
    lop = da.get(op) or []
    if a.nodo in lop:
        da[op] = [x for x in lop if x != a.nodo]
        escribir(a.entrada, da)
        tocados += 1
        print("  retirado: %s.%s ya no nombra a %s (la reciproca)" % (a.entrada, op, a.nodo))

    print()
    print("  entradas retiradas: %d" % tocados)
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
