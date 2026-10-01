"""Ninguna referencia de origen llega a la IA (fundador, 1 oct 2026; docs/REGLAS_DE_LA_CASA.md).

scripts/origen_ia.py es la funcion unica por la que pasa todo texto de nodo antes de llegar a la vista web, que es lo
unico que las llamadas a la IA pueden leer. Quita los titulos y los autores de la lista canonica sin tocar el resto del
texto. Los casos se escriben a mano, con la salida esperada calculada antes de correr la funcion (AGENTS.md).
"""
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE / "scripts"))

import origen_ia as oi  # noqa: E402

CANON = {"titulos": ["Juran's Quality Handbook", "Out of the Crisis"],
         "autores": ["Juran", "Deming", "Crosby", "Esty", "Wallas", "Andy Grove", "Cooper", "Reason"]}


def q(texto):
    return oi.quitar_origen(texto, oi.patrones(CANON))


def test_autor_entre_parentesis_sale_entero():
    # "(Juran)" sale con el espacio que lo precede: "Proceso de Benchmarking de 7 Pasos"
    assert q("Proceso de Benchmarking de 7 Pasos (Juran)")[0] == "Proceso de Benchmarking de 7 Pasos"
    # grupo de nombres unidos por guion, aunque uno no este en la lista: "(Lubin-Esty)" sale entero
    assert q("Modelo de 4 Etapas (Lubin-Esty)")[0] == "Modelo de 4 Etapas"
    assert q("Ciclo PDCA/PDSA (Shewhart-Deming)")[0] == "Ciclo PDCA/PDSA"


def test_autor_dentro_de_un_parentesis_con_mas_texto():
    # ", Crosby" sale y el resto del parentesis queda: "(Red Autogestionada de Profesionales)"
    assert q("Consejo de Calidad (Red Autogestionada de Profesionales, Crosby)")[0] == \
        "Consejo de Calidad (Red Autogestionada de Profesionales)"
    # " de Crosby" sale: "(Paso 6)"
    assert q("Acción Correctiva Sistemática (Paso 6 de Crosby)")[0] == "Acción Correctiva Sistemática (Paso 6)"


def test_de_autor_y_autor_como_adjetivo():
    assert q("Los 14 Puntos de Deming para la Transformación")[0] == "Los 14 Puntos para la Transformación"
    assert q("Benchmarking y la Trilogía de Juran")[0] == "Benchmarking y la Trilogía"
    assert q("Modelo Juran de Calidad por Diseño")[0] == "Modelo de Calidad por Diseño"
    assert q("Método RCCA de Juran (Análisis de Causa Raíz)")[0] == "Método RCCA (Análisis de Causa Raíz)"


def test_titulo_de_libro_sale_con_sus_comillas():
    assert q("Como dice 'Out of the Crisis', mide el sistema.")[0] == "Como dice, mide el sistema."


def test_no_toca_palabras_comunes_ni_excepciones():
    # minusculas: no es un apellido
    assert q("la razón por la que compra ('reason to buy')")[0] == "la razón por la que compra ('reason to buy')"
    # excepcion declarada: una marca de coche, no un autor
    assert q("como hizo BMW con el MINI Cooper.")[0] == "como hizo BMW con el MINI Cooper."
    # metodo sin autor de la lista: intacto
    assert q("Usa el diagrama de Ishikawa y el ciclo PDCA.")[0] == "Usa el diagrama de Ishikawa y el ciclo PDCA."


def test_cada_quita_queda_registrada():
    nuevo, quitas = q("Trilogía de Juran (Planificación, Control y Mejora)")
    assert nuevo == "Trilogía (Planificación, Control y Mejora)"
    assert quitas == [" de Juran"]


def test_vista_de_nodo_y_registro():
    nodo = {"node_id": "x", "titulo_concepto": "Objetivo del Liderazgo (Deming)", "resumen_teorico": "Sin autores.",
            "pasos_accionables": ["Paso uno.", "Aplica el paso 7 de Crosby."], "etiqueta_arbol": "Lidera con un fin"}
    registro = []
    oi.limpiar_nodo(nodo, oi.patrones(CANON), registro)
    assert nodo["titulo_concepto"] == "Objetivo del Liderazgo"
    assert nodo["pasos_accionables"] == ["Paso uno.", "Aplica el paso 7."]
    assert nodo["resumen_teorico"] == "Sin autores."
    assert [(r["node_id"], r["campo"], r["indice"], r["quitado"]) for r in registro] == [
        ("x", "titulo_concepto", None, " (Deming)"), ("x", "pasos_accionables", 1, " de Crosby")]


def test_la_vista_web_del_grafo_no_lleva_ningun_autor_ni_titulo():
    """El grafo de la web, tal como lo leen las llamadas a la IA, no contiene ningun titulo ni autor canonico en
    ningun texto de nodo (salvo las excepciones declaradas)."""
    import json
    canon = oi.cargar_canon()
    pats = oi.patrones(canon)
    g = json.loads((BASE / "web/lib/assets/master_graph.json").read_text(encoding="utf-8"))["nodos"]
    restos = []
    for nid, n in g.items():
        for campo in oi.CAMPOS_TEXTO:
            v = n.get(campo)
            for i, s in enumerate(v if isinstance(v, list) else [v]):
                if isinstance(s, str) and oi.quitar_origen(s, pats)[1]:
                    restos.append((nid, campo, i))
    assert restos == [], restos[:10]


if __name__ == "__main__":
    fallos = 0
    for nombre, f in list(globals().items()):
        if nombre.startswith("test_") and callable(f):
            try:
                f()
                print("OK  ", nombre)
            except Exception as e:  # noqa: BLE001
                fallos += 1
                print("FALLA", nombre, repr(e)[:300])
    sys.exit(1 if fallos else 0)
