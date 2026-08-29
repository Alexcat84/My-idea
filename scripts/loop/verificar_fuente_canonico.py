# -*- coding: utf-8 -*-
r"""verificar_fuente_canonico.py . TAREA 3.d de la vuelta 136. El criterio de
HECHO de la fase 08 (`docs/plan/08_VERIFICACION.md:9`, "UNA FASE ESTA HECHA
CUANDO SU VERIFICACION SE CAERIA SI EL FALLO VOLVIERA"), no un adorno.

Recorre los nodos vivos, parte `fuente` por ` | `, y cae ROJO EXIT 1
nombrando el nodo y la grafia si ALGUNA declaracion no esta en el conjunto
de canonicas de la tabla ya adjudicada (docs/plan/OP_S_11_MAPEO_PROPUESTO.md,
columna "canonica propuesta", 54 valores distintos en el corte de la
vuelta 136).

Reusa `vuelta136_simular_ops11.cargar_tabla` y
`vuelta136_simular_ops11.declaraciones_de`: no reimplementa el parseo de la
tabla ni la particion del campo.

Uso:
  python scripts/loop/verificar_fuente_canonico.py
  python scripts/loop/verificar_fuente_canonico.py --autoprueba
"""
import glob
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vuelta136_simular_ops11 import cargar_tabla, declaraciones_de  # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")


def cargar_nodos_vivos(overrides=None):
    """Devuelve lista de (id_nodo, fuente) de nodos vivos con `fuente`.
    `overrides` (dict id_nodo -> fuente) permite sustituir el valor en
    MEMORIA para la prueba de mutacion, sin tocar disco."""
    overrides = overrides or {}
    out = []
    for p in sorted(glob.glob(os.path.join(NODOS, "*.json"))):
        d = json.loads(io.open(p, encoding="utf-8").read())
        if d.get("deprecado"):
            continue
        id_nodo = d.get("node_id") or os.path.splitext(os.path.basename(p))[0]
        fu = overrides.get(id_nodo, d.get("fuente"))
        if not fu:
            continue
        out.append((id_nodo, fu))
    return out


def verificar(overrides=None):
    """Devuelve (ok, incumplimientos). incumplimientos es una lista de
    (id_nodo, grafia_no_canonica)."""
    mapa = cargar_tabla()
    canonicas = set(mapa.values())
    incumplimientos = []
    for id_nodo, fuente in cargar_nodos_vivos(overrides):
        for d in declaraciones_de(fuente):
            if d not in canonicas:
                incumplimientos.append((id_nodo, d))
    return (len(incumplimientos) == 0), incumplimientos


def autoprueba():
    """Prueba de mutacion (EJECUTOR.md 1, EL CASO ROJO SE PRUEBA POR
    MUTACION): sobre una COPIA EN MEMORIA del grafo ya escrito, le devuelve
    a UN nodo su grafia vieja no canonica y comprueba que cae ROJO
    nombrandolo. Cero escritura a disco."""
    mapa = cargar_tabla()
    canonicas = set(mapa.values())

    ok_antes, incump_antes = verificar()
    if not ok_antes:
        print("AUTOPRUEBA NO CONCLUYENTE: el arbol real YA esta ROJO antes de mutar "
              "(%d incumplimiento(s)); la mutacion no se puede probar sobre un grafo "
              "que no esta limpio." % len(incump_antes))
        return 1

    # busca un nodo YA canonico con al menos una declaracion cuya grafia
    # vieja no canonica exista en la tabla (grafia != canonica).
    grafia_vieja = None
    for grafia, canonica in mapa.items():
        if grafia != canonica:
            grafia_vieja = grafia
            canonica_objetivo = canonica
            break
    if grafia_vieja is None:
        print("AUTOPRUEBA NO CONCLUYENTE: la tabla no trae ningun par grafia != canonica.")
        return 1

    nodo_mutado = None
    for id_nodo, fuente in cargar_nodos_vivos():
        declaraciones = declaraciones_de(fuente)
        if canonica_objetivo in declaraciones:
            nueva = [grafia_vieja if d == canonica_objetivo else d for d in declaraciones]
            nodo_mutado = id_nodo
            fuente_mutada = " | ".join(nueva)
            break
    if nodo_mutado is None:
        print("AUTOPRUEBA NO CONCLUYENTE: ningun nodo vivo declara la canonica "
              "'%s' para mutarla de vuelta a su grafia vieja." % canonica_objetivo)
        return 1

    ok_mutado, incump_mutado = verificar(overrides={nodo_mutado: fuente_mutada})
    nombrado = any(n == nodo_mutado and g == grafia_vieja for n, g in incump_mutado)
    if ok_mutado or not nombrado:
        print("AUTOPRUEBA FALLIDA: la mutacion de '%s' en %s no produjo ROJO nombrandolo." %
              (grafia_vieja, nodo_mutado))
        return 1

    print("AUTOPRUEBA VERIFICADA: copia en memoria de %s, canonica '%s' devuelta a su "
          "grafia vieja '%s', cae ROJO nombrando el nodo y la grafia (cero escritura a disco)." %
          (nodo_mutado, canonica_objetivo, grafia_vieja))
    return 0


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    if "--autoprueba" in sys.argv:
        return autoprueba()

    ok, incumplimientos = verificar()
    if ok:
        print("VERDE EXIT 0: todas las declaraciones de `fuente` de los nodos vivos "
              "son canonicas de la tabla.")
        return 0
    print("ROJO, %d incumplimiento(s):" % len(incumplimientos))
    for id_nodo, grafia in incumplimientos:
        print("  %s: '%s' no es canonica de la tabla" % (id_nodo, grafia))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
