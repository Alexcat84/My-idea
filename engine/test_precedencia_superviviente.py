# -*- coding: utf-8 -*-
"""La precedencia del superviviente: SEMILLA > TELEMETRIA > PROPUESTO.

EL CASO REAL QUE LA ORIGINO (Fase 2 de la curacion del motor, ago 2026). El
cluster 11 del nucleo junta:

    analisis_flujo_de_valor        SEMILLA de entrada,  0 visitas
    value_stream_analysis_lean     nodo interior,       1 visita

Con la regla vieja ("mas historia gana") el superviviente habria sido el nodo
interior, y la SEMILLA se habria deprecado: una visita contra cero cerrando una
puerta de entrada del recorrido.

    "Las visitas de una PUERTA y las de un nodo INTERIOR miden cosas distintas,
     asi que no compiten."

El Gate 0 lo habria cazado despues ("ninguna semilla deprecada"), y por eso el
arreglo no vive alli:

    "El Gate es el paracaidas, no el diseño."
"""
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE / "scripts"))

PODA = BASE / "scripts" / "preparar_poda.py"


def _superviviente(cluster, semillas, vis, cos, quedaria=None, titulos=None):
    """La misma funcion que preparar_poda define dentro de main(), reconstruida
    aqui con sus tres reglas. El test de abajo comprueba que el codigo real las
    tiene; este ejerce la logica."""
    ss = [n for n in cluster if n in semillas]
    if ss:
        elegido = max(ss, key=lambda n: (vis.get(n, 0), cos.get(n, 0)))
        return elegido, ("semilla" if len(ss) == 1 else "semilla (dos en el cluster)")
    con = [n for n in cluster if vis.get(n)]
    if con:
        return max(con, key=lambda n: (vis.get(n, 0), cos.get(n, 0))), "telemetría"
    for n in cluster:
        if (titulos or {}).get(n) == quedaria:
            return n, "propuesto"
    return cluster[0], "primero"


def test_el_caso_real_del_cluster_11():
    c = ["analisis_flujo_de_valor", "value_stream_analysis_lean"]
    semillas = {"analisis_flujo_de_valor"}
    vis = {"value_stream_analysis_lean": 1}  # la semilla tiene 0
    elegido, por = _superviviente(c, semillas, vis, {})
    assert elegido == "analisis_flujo_de_valor", (
        f"eligio {elegido}: una visita contra cero acaba de cerrar una puerta")
    assert por == "semilla"
    print("  ok: la semilla con 0 visitas gana al nodo interior con 1")


def test_entre_dos_semillas_decide_la_telemetria():
    c = ["puerta_a", "puerta_b", "interior"]
    semillas = {"puerta_a", "puerta_b"}
    vis = {"puerta_a": 3, "puerta_b": 40, "interior": 900}
    elegido, por = _superviviente(c, semillas, vis, {})
    assert elegido == "puerta_b", elegido
    assert "dos en el cluster" in por
    print("  ok: entre dos puertas manda la telemetria; el interior no compite aunque tenga 900")


def test_sin_semilla_manda_la_telemetria_como_siempre():
    c = ["a", "b"]
    elegido, por = _superviviente(c, set(), {"a": 2, "b": 9}, {})
    assert (elegido, por) == ("b", "telemetría")
    print("  ok: sin semilla en el cluster, la regla vieja sigue mandando")


def test_sin_semilla_y_sin_historia_manda_el_propuesto():
    c = ["a", "b"]
    elegido, por = _superviviente(c, set(), {}, {}, quedaria="El bueno",
                                  titulos={"a": "El otro", "b": "El bueno"})
    assert (elegido, por) == ("b", "propuesto")
    print("  ok: sin semilla y sin historia, manda el propuesto del consolidador")


def test_el_codigo_real_tiene_la_precedencia():
    """El remache: la logica de arriba no sirve de nada si el script no la trae."""
    src = PODA.read_text(encoding="utf-8")
    cuerpo = src[src.index("def superviviente("):src.index("md = [")]
    assert "SEMILLAS" in cuerpo, "el superviviente no mira las semillas"
    assert cuerpo.index("semillas = [") < cuerpo.index("con_historia = ["), (
        "la telemetria se evalua ANTES que la semilla: la precedencia esta al reves")
    assert "SEMILLAS = set(" in src, "las semillas no se cargan"
    assert 'entry_seeds.json' in src, "no se leen del asset que usa el motor"
    assert "SEMILLA > TELEMETRIA > PROPUESTO" in src, "la regla no queda escrita en el indice"
    print("  ok: preparar_poda.py trae la precedencia y la declara en su indice")


def test_las_semillas_salen_del_asset_vivo():
    """Una lista de semillas escrita a mano aqui envejeceria en silencio, y el
    sintoma seria deprecar una puerta creyendo que no lo era."""
    import preparar_poda as P
    reales = set(json.loads(
        (BASE / "web" / "lib" / "assets" / "entry_seeds.json").read_text(encoding="utf-8"))["seeds"])
    assert P.SEMILLAS == reales, "la lista de semillas del podador no es la del motor"
    assert len(P.SEMILLAS) >= 20, f"solo {len(P.SEMILLAS)} semillas"
    print(f"  ok: las {len(P.SEMILLAS)} semillas salen del asset vivo")


def main():
    for f in (test_el_caso_real_del_cluster_11,
              test_entre_dos_semillas_decide_la_telemetria,
              test_sin_semilla_manda_la_telemetria_como_siempre,
              test_sin_semilla_y_sin_historia_manda_el_propuesto,
              test_el_codigo_real_tiene_la_precedencia,
              test_las_semillas_salen_del_asset_vivo):
        f()
    print("OK: una puerta no se depreca por una visita contra cero.")


if __name__ == "__main__":
    main()
