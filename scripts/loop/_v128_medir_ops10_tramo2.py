# -*- coding: utf-8 -*-
"""Medicion propia de la vuelta 128 para el tramo 2 de OP-S-10 (3.b): de los
28 vivos de la nomina, excluidos los dos contramodelos y los diez ya escritos
en la vuelta 126, cuales de los candidatos restantes hoy no nombran el pais
en condiciones_activacion (deben ser 16, por el contraste del encargo)."""
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

ops = [json.loads(l) for l in open(os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl"), encoding="utf-8") if l.strip()]
op = [o for o in ops if o.get("id_op") == "OP-S-10"][0]
nomina = op["nodos"]
print("nomina OP-S-10: %d ids, unicos %d" % (len(nomina), len(set(nomina))))

hoy = json.load(open(os.path.join(RAIZ, "dataset", "metadata", "master_graph.json"), encoding="utf-8"))["nodos"]

TOCADOS_126 = [
    "alternativa_business_opportunity_licensing",
    "alternativa_trademark_licensing",
    "calculo_roi_franquiciado_2",
    "calificacion_prospectos_award",
    "concepto_de_advances",
    "cumplir_leyes_estatales_franquicia",
    "decision_fpr",
    "decision_marca_comun_branding",
    "desarrollar_manual_operaciones",
    "diseno_programa_capacitacion_franquicia",
]

CONTRAMODELOS = ["comprender_definicion_legal_franquicia"]


def nombra_pais(txt):
    t = (txt or "").lower()
    return "estados unidos" in t or "ee. uu" in t or "eeuu" in t or "ee.uu" in t


vivos = sorted([i for i in nomina if i in hoy and not hoy[i].get("deprecado")])
print("vivos en la nomina (WORK): %d" % len(vivos))
deprecados = sorted([i for i in nomina if i in hoy and hoy[i].get("deprecado")])
print("deprecados en la nomina (WORK): %d -> %s" % (len(deprecados), deprecados))

# localizar los dos contramodelos declarados por la operacion (los que ya condicionan bien)
contramodelos_reales = [i for i in vivos if any(nombra_pais(c) for c in (hoy[i].get("condiciones_activacion") or []))
                         and i not in TOCADOS_126]
print("nodos vivos de la nomina que YA nombran el pais y NO fueron tocados en la 126 (candidatos a contramodelo): %d -> %s"
      % (len(contramodelos_reales), contramodelos_reales))

candidatos = [i for i in vivos if i not in TOCADOS_126
              and not any(nombra_pais(c) for c in (hoy[i].get("condiciones_activacion") or []))]
print("PENDIENTES (vivos, no tocados en 126, hoy no nombran el pais): %d" % len(candidatos))
for i in candidatos:
    print("   %s" % i)
