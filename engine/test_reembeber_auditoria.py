# -*- coding: utf-8 -*-
"""scripts/auditoria_final/reembeber.py: el re-embebido de los nodos corregidos deja el indice coherente, y si no, no
escribe. Con un embebedor FALSO (sin clave y sin red): el veredicto no depende de los secretos del ambiente."""
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "auditoria_final"))
import reembeber as rb  # noqa: E402

grafo = {
    "a": {"titulo_concepto": "A", "resumen_teorico": "alfa", "condiciones_activacion": []},
    "b": {"titulo_concepto": "B", "resumen_teorico": "beta", "condiciones_activacion": []},
    "c": {"titulo_concepto": "C", "resumen_teorico": "gamma", "condiciones_activacion": []},
    "viejo": {"titulo_concepto": "V", "resumen_teorico": "v", "deprecado": True},
}
indice = {"model": "m", "dimension": 3, "ids": ["a", "b", "c"], "embeddings": [[1, 0, 0], [0, 1, 0], [0, 0, 1]]}

# 1. re-embeber 'b' con un vector que sigue siendo el suyo: coherente, solo cambia 'b'
nuevo, inf = rb.reembeber(["b"], grafo, indice, lambda textos: [[0.1, 0.9, 0.0] for _ in textos])
assert inf == {"pedidos": 1, "cambiados": 1, "fallos": []}, inf
assert nuevo["embeddings"][1] == [0.1, 0.9, 0.0] and nuevo["embeddings"][0] == [1, 0, 0]
assert indice["embeddings"][1] == [0, 1, 0]  # no muta el original

# 2. un deprecado no se re-embebe
_, inf = rb.reembeber(["viejo"], grafo, indice, lambda textos: [[1, 1, 1] for _ in textos])
assert inf["pedidos"] == 0 and inf["fallos"] == [], inf

# 3. un vector nuevo que queda mas cerca del viejo de 'a' que del suyo: no es coherente, se dice
_, inf = rb.reembeber(["b"], grafo, indice, lambda textos: [[1, 0.01, 0] for _ in textos])
assert any("junto al suyo viejo" in f for f in inf["fallos"]), inf

# 4. otra dimension: no es coherente
_, inf = rb.reembeber(["b"], grafo, indice, lambda textos: [[0, 1] for _ in textos])
assert any("dimension" in f for f in inf["fallos"]), inf

# 5. los ids salen de las tandas VOZ, no de las de aristas (el texto de una arista no cambia el vector)
import json, tempfile  # noqa: E401
d = tempfile.mkdtemp()
p1 = os.path.join(d, "voz.json"); json.dump([{"node_id": "b", "veredicto": "VOZ"}], open(p1, "w"))
p2 = os.path.join(d, "aristas.json"); json.dump([{"operacion": "TEJER", "desde": "a", "hacia": "c"}], open(p2, "w"))
assert rb.ids_de_tandas([p1, p2]) == ["b"], rb.ids_de_tandas([p1, p2])
print("TODO OK: re-embebido coherente o no se escribe")
