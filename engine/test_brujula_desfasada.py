# -*- coding: utf-8 -*-
"""La brujula del CLI se niega a operar desfasada.

EL HALLAZGO (auditoria del segundo indice, ago 2026): hay DOS indices semanticos
vivos y no son comparables. La web usa Voyage con 3.521 vectores; el CLI carga
engine/semantic_index.npz, generado el 2026-07-08 con sentence-transformers, con
1.266 vectores de 384 dimensiones. El CLI era ciego a 2.255 nodos, incluido todo
lo que el ciclo de la curacion toco, y nadie se enteraba: ninguna ruta de la web
lo alcanza, ninguna de las 21 pruebas lo ejercita, y ningun flujo lo regenera.

LA ADJUDICACION fue el PUENTE CORRECTIVO: ni retirarlo ni meterlo al Gate 0.

    "El antidoto se ancla en el PUNTO DE EXPOSICION."

El daño no estaba en el archivo, estaba en el momento en que alguien corre el
CLI y se cree el resultado. Asi que la brujula se apaga sola.

DOS COSAS QUE NO SON NEGOCIABLES, y por eso hay dos fixtures:
  1. CERO TOLERANCIA: si falta UN activo, se apaga. Una brujula que apunta al 36
     por ciento del territorio no es una brujula degradada, es una equivocada.
  2. NO LANZA. El motor sigue con navegacion local, el mismo respaldo que ya
     existe cuando falta la clave de Voyage en la web. Un CLI que no arranca es
     peor que un CLI sin brujula.

El caso que debe cazar se monta con un INDICE DE JUGUETE. El .npz real no se
toca: un test que reescribe el artefacto que audita no es un test.
"""
import io
import json
import os
import sys
import tempfile
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE / "engine"))

import prototipo_motor as pm  # noqa: E402


def _reset():
    """Limpia el cache de la brujula entre casos."""
    pm._BRUJULA_INDICE = None
    pm._BRUJULA_MODELO = None
    pm._BRUJULA_AVISO_IMPRESO = False


def _con_indice(ids, fn):
    """Corre fn con un .npz de juguete que contiene exactamente `ids`."""
    import numpy as np
    tmp = Path(tempfile.mkdtemp()) / "juguete.npz"
    np.savez(tmp, ids=np.array(ids, dtype=object).astype(str),
             embeddings=np.zeros((len(ids), 4), dtype=np.float32))
    real = pm.SEMANTIC_INDEX_PATH
    pm.SEMANTIC_INDEX_PATH = tmp
    _reset()
    try:
        return fn()
    finally:
        pm.SEMANTIC_INDEX_PATH = real
        _reset()


def _capturar(fn):
    antes, buf = sys.stdout, io.StringIO()
    sys.stdout = buf
    try:
        return fn(), buf.getvalue()
    finally:
        sys.stdout = antes


def _activos():
    grafo = json.loads(
        (BASE / "dataset" / "metadata" / "master_graph.json").read_text(encoding="utf-8"))["nodos"]
    return sorted(k for k, n in grafo.items() if not n.get("deprecado"))


def test_indice_al_que_le_falta_UN_activo_apaga_la_brujula():
    """EL CASO QUE DEBE CAZAR. Cero tolerancia: uno basta."""
    activos = _activos()
    incompleto = activos[:-1]  # le falta exactamente uno
    disponible, salida = _capturar(lambda: _con_indice(incompleto, pm._cargar_brujula))
    assert disponible is False, "la brujula opero con un activo fuera del indice"
    assert "APAGADA" in salida, salida
    assert "1 de los" in salida, f"no dice CUANTOS faltan: {salida}"
    assert str(len(activos)) in salida, "no dice sobre cuantos activos"
    assert "build_semantic_index.py" in salida, "no dice como regenerarlo"
    print(f"  ok: con UN activo fuera de {len(activos)}, la brujula se apaga y avisa")


def test_indice_que_cubre_a_todos_los_activos_busca_normal():
    """EL CASO QUE NO DEBE CAZAR. Si cubre a todos, la brujula no se estorba.

    Se comprueba que la comprobacion de cobertura PASA. No se carga el modelo de
    sentence-transformers (descarga de cientos de megas): se verifica que
    `_activos_sin_vector` no encuentra faltantes, que es lo que decide."""
    activos = _activos()
    faltan, total = pm._activos_sin_vector(activos)
    assert faltan == [], f"un indice completo reporta faltantes: {faltan[:5]}"
    assert total == len(activos)
    # y con uno de mas (un deprecado dentro del indice) tampoco se queja: los
    # vectores que sobran no hacen invisible a nadie.
    faltan2, _ = pm._activos_sin_vector(activos + ["un_deprecado_cualquiera"])
    assert faltan2 == [], "un vector de mas apaga la brujula, y no deberia"
    print(f"  ok: con los {len(activos)} activos cubiertos, la cobertura pasa (y un vector de mas no estorba)")


def test_el_apagado_NO_lanza_y_buscar_afines_devuelve_vacio():
    """El motor sigue vivo. Un CLI que no arranca es peor que uno sin brujula."""
    activos = _activos()
    def cuerpo():
        return pm.buscar_afines("cuanto cobro por lo que hago", set())
    r, salida = _capturar(lambda: _con_indice(activos[:-1], cuerpo))
    assert r == [], f"devolvio candidatos con la brujula apagada: {r}"
    assert "APAGADA" in salida
    print("  ok: apagada devuelve [] y no lanza; el motor sigue con navegacion local")


def test_avisa_UNA_sola_vez_por_sesion():
    activos = _activos()
    def cuerpo():
        pm._cargar_brujula()
        pm._cargar_brujula()
        pm.buscar_afines("algo", set())
    _, salida = _capturar(lambda: _con_indice(activos[:-1], cuerpo))
    assert salida.count("APAGADA") == 1, f"el aviso se repite {salida.count('APAGADA')} veces"
    print("  ok: avisa una sola vez por sesion, no en cada turno")


def test_el_npz_real_no_se_toca():
    """Un test que reescribe el artefacto que audita no es un test."""
    real = BASE / "engine" / "semantic_index.npz"
    assert real.exists(), "desaparecio el .npz real"
    src = Path(__file__).read_text(encoding="utf-8")
    assert "semantic_index.npz" not in src.split("def _con_indice")[1].split("def _capturar")[0], (
        "el helper del indice de juguete nombra el .npz real")
    print("  ok: el .npz real sigue en su sitio y ningun caso lo escribe")


def main():
    for f in (test_indice_al_que_le_falta_UN_activo_apaga_la_brujula,
              test_indice_que_cubre_a_todos_los_activos_busca_normal,
              test_el_apagado_NO_lanza_y_buscar_afines_devuelve_vacio,
              test_avisa_UNA_sola_vez_por_sesion,
              test_el_npz_real_no_se_toca):
        f()
    print("OK: la brujula del CLI se apaga antes que mentir.")


if __name__ == "__main__":
    main()
