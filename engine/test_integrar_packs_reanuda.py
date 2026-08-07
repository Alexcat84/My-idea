# -*- coding: utf-8 -*-
"""La reanudacion por paso de scripts/integrar_packs.py.

LA AVERIA DE ORIGEN (2026-08-07, integrando compras y entrega): el paso (a)
copio los nodos a dataset/ y el paso (e) fallo. Al reintentar, el script
dedujo el estado de un efecto del paso (a) -- "ya hay nodos en dataset/" --
declaro los packs integrados y dijo "no hay packs pendientes, nada que
hacer". Salio con codigo 0 y los pasos b a f jamas corrieron: el grafo
quedaba sin familias, sin cache de preguntas parchada, sin indice semantico
y sin sincronizar a la web. Un exito falso, que es peor que un fallo.

La leccion: el estado de una linea de ensamblaje se ESCRIBE, no se deduce
del rastro de uno de sus pasos.

Aqui se prueba la decision pura. Que cada paso corra de verdad lo cubre la
propia linea; lo que no puede volver a pasar es que la decision diga "nada
que hacer" habiendo trabajo pendiente.
"""
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE / "scripts"))

from integrar_packs import PASOS, decidir_accion, pasos_pendientes  # noqa: E402


def test_el_escenario_exacto_de_la_averia():
    # Paso (a) hecho, (b) a (f) pendientes. Y descubrir_packs ya NO ve packs
    # pendientes, porque los nodos estan en dataset/: ese era el veneno.
    estado = {"packs": ["compras", "entrega"], "hechos": ["a_nodos_y_puentes"]}
    accion, faltan = decidir_accion(estado, pendientes=[])
    assert accion == "reanudar", f"dijo '{accion}' con trabajo a medias"
    assert "e_gate0" in faltan and "f_sync" in faltan, faltan
    assert len(faltan) == len(PASOS) - 1, faltan
    print(f"  ok: con (a) hecho y sin packs pendientes, REANUDA {len(faltan)} pasos")


def test_nunca_dice_nada_con_pasos_pendientes():
    # Para cualquier corte posible de la linea, la respuesta es reanudar.
    for corte in range(len(PASOS)):
        estado = {"packs": ["compras"], "hechos": PASOS[:corte]}
        accion, faltan = decidir_accion(estado, pendientes=[])
        assert accion == "reanudar", f"corte en {corte}: dijo '{accion}'"
        assert faltan == PASOS[corte:], (corte, faltan)
    print(f"  ok: los {len(PASOS)} cortes posibles reanudan, ninguno calla")


def test_completa_y_limpia():
    estado = {"packs": ["compras"], "hechos": list(PASOS)}
    assert pasos_pendientes(estado) == []
    # Un archivo de estado con todo hecho es un huerfano: no hay que reanudar
    # nada, y el script lo borra en vez de arrastrarlo para siempre.
    assert decidir_accion(estado, pendientes=[]) == ("nada", [])
    print("  ok: con todos los pasos hechos, el estado es huerfano y no reanuda")


def test_arranque_limpio():
    assert decidir_accion(None, pendientes=["compras"]) == ("integrar", ["compras"])
    assert decidir_accion(None, pendientes=[]) == ("nada", [])
    print("  ok: sin estado previo, integra si hay packs y calla si no los hay")


def main():
    for f in (test_el_escenario_exacto_de_la_averia,
              test_nunca_dice_nada_con_pasos_pendientes,
              test_completa_y_limpia, test_arranque_limpio):
        f()
    print("OK: la linea de ensamblaje reanuda o grita, nunca calla a medias.")


if __name__ == "__main__":
    main()
