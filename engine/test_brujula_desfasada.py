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


def _con_indice(ids, fn, generado_iso=None):
    """Corre fn con un .npz de juguete que contiene exactamente `ids`.

    `generado_iso=None` reproduce el .npz REAL de hoy, que es anterior al
    registro de la fecha y por tanto no trae el campo."""
    import numpy as np
    tmp = Path(tempfile.mkdtemp()) / "juguete.npz"
    campos = {"ids": np.array(ids, dtype=object).astype(str),
              "embeddings": np.zeros((len(ids), 4), dtype=np.float32)}
    if generado_iso is not None:
        campos["generado_iso"] = np.array(generado_iso)
    np.savez(tmp, **campos)
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


def test_la_fecha_sale_del_ARTEFACTO_y_no_del_sistema_de_archivos():
    """LA FECHA DEL AVISO MENTIA EN UN CLON FRESCO.

    Git NO guarda tiempos de modificacion: en cualquier clon nuevo el .npz nace
    con la fecha del checkout. El aviso, que sacaba la fecha de os.path.getmtime,
    habria dicho "generado hoy" MIENTRAS EXPLICA QUE EL INDICE ESTA DESFASADO.

    Es la misma familia que el "3.604" que se colo por deducir un total en vez de
    contarlo: un dato dentro de un aviso que no es lo que dice ser. Y estos
    avisos existen justamente para no mentir.

    La cura: la fecha se escribe DENTRO del artefacto al generarlo. Si no esta,
    se dice DESCONOCIDA y no se cae de vuelta a getmtime, porque un dato
    equivocado es peor que uno ausente."""
    activos = _activos()
    incompleto = activos[:-1]

    # (1) CON el campo: el aviso muestra ESA fecha, no la del archivo.
    _, con = _capturar(lambda: _con_indice(incompleto, pm._cargar_brujula,
                                           generado_iso="2026-07-08T17:40:00"))
    assert "generado el 2026-07-08" in con, con
    assert "desconocida" not in con, con

    # (2) SIN el campo (el .npz real de hoy): dice desconocida y NO inventa fecha.
    _, sin = _capturar(lambda: _con_indice(incompleto, pm._cargar_brujula))
    assert "fecha de generacion desconocida" in sin, sin
    assert "anterior a este registro" in sin, sin
    import re
    assert not re.search(r"generado el \d{4}-\d{2}-\d{2}", sin), (
        f"invento una fecha sin tener el campo: {sin}")

    # (3) EL REMACHE: getmtime no aparece en el cuerpo del cargador.
    src = (BASE / "engine" / "prototipo_motor.py").read_text(encoding="utf-8")
    cuerpo = src[src.index("def _cargar_brujula"):src.index("def buscar_afines")]
    # Se busca la LLAMADA, no la palabra: el comentario que explica por que no
    # se usa la nombra a proposito, y una asercion sobre la palabra suelta
    # prohibiria documentar la decision.
    assert "getmtime(" not in cuerpo, (
        "el cargador volvio a deducir la fecha del sistema de archivos")
    assert "generado_iso" in cuerpo, "el cargador no lee la fecha del artefacto"

    # (4) y el generador la escribe
    gen = (BASE / "engine" / "build_semantic_index.py").read_text(encoding="utf-8")
    assert "generado_iso=np.array(generado)" in gen, "el generador no guarda la fecha"
    print("  ok: la fecha sale del artefacto; sin campo dice desconocida y no inventa ninguna")


def main():
    for f in (test_indice_al_que_le_falta_UN_activo_apaga_la_brujula,
              test_indice_que_cubre_a_todos_los_activos_busca_normal,
              test_el_apagado_NO_lanza_y_buscar_afines_devuelve_vacio,
              test_avisa_UNA_sola_vez_por_sesion,
              test_el_npz_real_no_se_toca,
              test_la_fecha_sale_del_ARTEFACTO_y_no_del_sistema_de_archivos):
        f()
    print("OK: la brujula del CLI se apaga antes que mentir.")


if __name__ == "__main__":
    main()
