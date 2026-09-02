# -*- coding: utf-8 -*-
r"""verificar_fuente_canonico.py . TAREA 3.d de la vuelta 136. El criterio de
HECHO de la fase 08 (`docs/plan/08_VERIFICACION.md:9`, "UNA FASE ESTA HECHA
CUANDO SU VERIFICACION SE CAERIA SI EL FALLO VOLVIERA"), no un adorno.

Recorre los nodos vivos, parte `fuente` por ` | `, y cae ROJO EXIT 1
nombrando el nodo y la grafia si ALGUNA declaracion no esta en el conjunto
de canonicas de la tabla ya adjudicada (docs/plan/OP_S_11_MAPEO_PROPUESTO.md,
columna "canonica propuesta", 54 valores distintos en el corte de la
vuelta 136).

Y CAE ROJO IGUAL, NOMBRANDO EL NODO, SI UN NODO VIVO TRAE `fuente` AUSENTE,
VACIO O SIN NI UNA DECLARACION (clausula de campo presente, reparacion 1.b de
la vuelta 137, parada del 29 ago 2026 punto 3). Antes de esa reparacion el
cargador hacia `if not fu: continue` y un nodo sin declaracion salia LIMPIO.

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


# LA CLAUSULA DE CAMPO PRESENTE (reparacion 1.b de la vuelta 137, parada del 29
# ago 2026 punto 3). Hasta hoy cargar_nodos_vivos() hacia `if not fu: continue`:
# un nodo vivo SIN declaracion no tenia nada que comprobar y salia LIMPIO. Hoy no
# muerde a nadie (los 3.184 vivos tienen `fuente`, medido en la vuelta 136), pero
# esta guarda queda cableada como uno de los cinco controles mecanicos de la
# aduana OP-A-02, cuyo caso es justamente UN NODO NUEVO ENTRANDO, o sea el caso
# en que el campo puede faltar. Un nodo vivo con `fuente` vacio, ausente, o cuyo
# campo no produzca ni una sola declaracion, CAE ROJO NOMBRANDOLO.
MOTIVO_NO_CANONICA = "no es canonica de la tabla"
MOTIVO_AUSENTE = "campo `fuente` AUSENTE en un nodo vivo"
MOTIVO_VACIO = "campo `fuente` VACIO en un nodo vivo"
MOTIVO_SIN_DECLARACIONES = "campo `fuente` presente pero sin ni una declaracion"

_SIN_OVERRIDE = object()


def cargar_nodos_vivos(overrides=None):
    """Devuelve lista de (id_nodo, fuente) de TODOS los nodos vivos, incluidos
    los que traen `fuente` vacio o ausente (esos salen con fuente None o ""):
    filtrarlos aqui era el agujero que la reparacion 1.b cierra.
    `overrides` (dict id_nodo -> fuente) permite sustituir el valor en
    MEMORIA para la prueba de mutacion, sin tocar disco. Un override a None
    simula el campo AUSENTE y uno a "" el campo VACIO."""
    overrides = overrides or {}
    out = []
    for p in sorted(glob.glob(os.path.join(NODOS, "*.json"))):
        d = json.loads(io.open(p, encoding="utf-8").read())
        if d.get("deprecado"):
            continue
        id_nodo = d.get("node_id") or os.path.splitext(os.path.basename(p))[0]
        ov = overrides.get(id_nodo, _SIN_OVERRIDE)
        fu = d.get("fuente") if ov is _SIN_OVERRIDE else ov
        out.append((id_nodo, fu))
    return out


def verificar(overrides=None):
    """Devuelve (ok, incumplimientos). incumplimientos es una lista de
    (id_nodo, grafia_no_canonica, motivo)."""
    mapa = cargar_tabla()
    canonicas = set(mapa.values())
    incumplimientos = []
    for id_nodo, fuente in cargar_nodos_vivos(overrides):
        if fuente is None:
            incumplimientos.append((id_nodo, "", MOTIVO_AUSENTE))
            continue
        if not str(fuente).strip():
            incumplimientos.append((id_nodo, "", MOTIVO_VACIO))
            continue
        declaraciones = declaraciones_de(fuente)
        if not declaraciones:
            incumplimientos.append((id_nodo, str(fuente), MOTIVO_SIN_DECLARACIONES))
            continue
        for d in declaraciones:
            if d not in canonicas:
                incumplimientos.append((id_nodo, d, MOTIVO_NO_CANONICA))
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
    nombrado = any(n == nodo_mutado and g == grafia_vieja for n, g, _m in incump_mutado)
    if ok_mutado or not nombrado:
        print("AUTOPRUEBA FALLIDA: la mutacion de '%s' en %s no produjo ROJO nombrandolo." %
              (grafia_vieja, nodo_mutado))
        return 1

    print("AUTOPRUEBA VERIFICADA: copia en memoria de %s, canonica '%s' devuelta a su "
          "grafia vieja '%s', cae ROJO nombrando el nodo y la grafia (cero escritura a disco)." %
          (nodo_mutado, canonica_objetivo, grafia_vieja))

    # SEGUNDA AUTOPRUEBA, LA CLAUSULA DE CAMPO PRESENTE (reparacion 1.b de la
    # vuelta 137). Las dos formas del agujero, sobre copia en memoria: el campo
    # AUSENTE (override a None) y el campo VACIO (override a "").
    testigo = cargar_nodos_vivos()[0][0]
    for etiqueta, valor, motivo in [("AUSENTE", None, MOTIVO_AUSENTE),
                                     ("VACIO", "", MOTIVO_VACIO),
                                     ("SOLO ESPACIOS", "   ", MOTIVO_VACIO)]:
        ok_c, incump_c = verificar(overrides={testigo: valor})
        cazado = any(n == testigo and m == motivo for n, _g, m in incump_c)
        if ok_c or not cazado:
            print("AUTOPRUEBA DE CAMPO PRESENTE FALLIDA: con `fuente` %s en %s la guarda "
                  "NO cayo nombrandolo." % (etiqueta, testigo))
            return 1
        print("AUTOPRUEBA DE CAMPO PRESENTE VERIFICADA (%s): copia en memoria de %s, cae "
              "ROJO con el motivo '%s' (cero escritura a disco)." % (etiqueta, testigo, motivo))
    return 0


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    if "--autoprueba" in sys.argv:
        return autoprueba()

    ok, incumplimientos = verificar()
    if ok:
        vivos = cargar_nodos_vivos()
        print("VERDE EXIT 0: los %d nodos vivos traen `fuente` PRESENTE y con al menos una "
              "declaracion, y todas sus declaraciones son canonicas de la tabla." % len(vivos))
        return 0
    print("ROJO, %d incumplimiento(s):" % len(incumplimientos))
    for id_nodo, grafia, motivo in incumplimientos:
        if grafia:
            print("  %s: '%s' %s" % (id_nodo, grafia, motivo))
        else:
            print("  %s: %s" % (id_nodo, motivo))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
