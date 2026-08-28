# -*- coding: utf-8 -*-
"""vuelta119_tarea3_titulo_ops01.py . VUELTA 119, TAREA 3.1: escribe el
`titulo_concepto` exacto de la decision del fundador
(`docs/loop/paradas/2026-08-28-titulo-nafta-ops01-DECISION.md`) en el
superviviente de `OP-S-01`, `certificado_de_origen_tratados_libre_comercio`.

CORRECCION DECLARADA, no reescritura silenciosa: este instrumento IMPRIME el
titulo VIEJO y el titulo NUEVO (evidencia sellada aparte, nunca se borra el
dato del titulo viejo del expediente) y solo escribe si el titulo VIVO de hoy
es, byte a byte, el titulo viejo esperado (si no lo es, ROJO: no se pisa un
estado que no es el que la decision describe).

Escribe SOLO `dataset/nodos/<id>.json`, preservando el fin de linea original
(patron de `vuelta39_enlazar_p10.py`: leer crudo, separar la cola de
'\r'/'\n', json.dumps(indent=2) + cola). `dataset/metadata/master_graph.json`
y el espejo de `web/` se recompilan aparte, con el ciclo de tres
(`run_phase1.py --reaplico-curaduria`, `etiquetas_de_cara.py --aplicar`,
`sync_assets_web.py`), NUNCA por este script.

Uso: python scripts/loop/vuelta119_tarea3_titulo_ops01.py
"""
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
NID = "certificado_de_origen_tratados_libre_comercio"

TITULO_VIEJO = "Certificado de Origen y Tratados de Libre Comercio (NAFTA, Rules of Origin, RVC)"
TITULO_NUEVO = ("Certificado de Origen y Tratados de Libre Comercio "
                 "(T-MEC/USMCA, Rules of Origin, RVC)")


def leer_crudo(nid):
    with io.open(os.path.join(NODOS, nid + ".json"), encoding="utf-8", newline="") as fh:
        bruto = fh.read()
    cola = ""
    while bruto and bruto[-1] in "\r\n":
        cola = bruto[-1] + cola
        bruto = bruto[:-1]
    return json.loads(bruto), cola


def escribir(nid, datos, cola):
    with io.open(os.path.join(NODOS, nid + ".json"), "w", encoding="utf-8", newline="") as fh:
        fh.write(json.dumps(datos, ensure_ascii=False, indent=2) + cola)


def main():
    datos, cola = leer_crudo(NID)
    actual = datos.get("titulo_concepto")
    print("=" * 78)
    print("VUELTA 119, TAREA 3.1: TITULO DEL SUPERVIVIENTE DE OP-S-01")
    print("=" * 78)
    print("nodo: %s" % NID)
    print("titulo_concepto LEIDO HOY  : %r" % actual)
    print("titulo_concepto ESPERADO (viejo, decision del 28 ago 2026): %r" % TITULO_VIEJO)
    if actual != TITULO_VIEJO:
        raise SystemExit("ROJO: el titulo vivo de hoy no es el titulo viejo que la decision "
                          "describe. NO SE ESCRIBE nada: no se pisa un estado distinto al "
                          "medido por la parada.")
    print()
    print("CORRECCION DECLARADA (28 ago 2026, decision del fundador, salida B, texto exacto):")
    print("  VIEJO -> %r" % TITULO_VIEJO)
    print("  NUEVO -> %r" % TITULO_NUEVO)
    datos["titulo_concepto"] = TITULO_NUEVO
    escribir(NID, datos, cola)
    print()
    print("ESCRITO: dataset/nodos/%s.json, campo titulo_concepto, ningun otro campo tocado." % NID)
    print("El texto viejo NO se borra del expediente: vive citado arriba en este sello y en "
          "docs/PENDIENTES.md / docs/plan/OPERACIONES.jsonl (correccion declarada, TAREA 3.1).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
