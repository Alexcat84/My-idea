#!/usr/bin/env python3
"""Herramienta de analisis temporal (NO parte del pipeline auditor) para
revisar los grupos candidatos de dedup con evidencia real de contenido,
en vez de aprobar a ciegas por coincidencia de titulo/id. Para cada grupo:
similitud de resumen_teorico (SequenceMatcher), si la fuente coincide, y
solapamiento de pasos_accionables. Imprime una recomendacion + motivo;
la decision final la toma un humano/el agente, esto es solo evidencia."""
import json
import sys
from difflib import SequenceMatcher
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from lib_dominio import CATEGORIAS, cargar_dominio, dir_metadata


def sim(a, b):
    return SequenceMatcher(None, a or "", b or "").ratio()


def analizar(cat):
    nodos = cargar_dominio(cat)
    candidatos = json.load(open(dir_metadata(cat) / "dedup_candidatos.json", encoding="utf-8"))
    resultados = []
    for g in candidatos:
        keeper = g["keeper"]
        kd = nodos.get(keeper, {})
        detalle_miembros = []
        sims = []
        for otro in g["fusionar"]:
            od = nodos.get(otro, {})
            s_resumen = sim(kd.get("resumen_teorico", ""), od.get("resumen_teorico", ""))
            s_pasos = sim(" ".join(kd.get("pasos_accionables") or []), " ".join(od.get("pasos_accionables") or []))
            misma_fuente = kd.get("fuente") == od.get("fuente")
            sims.append(s_resumen)
            detalle_miembros.append({
                "id": otro, "titulo": od.get("titulo_concepto", ""),
                "fuente": od.get("fuente", ""), "sim_resumen": round(s_resumen, 3),
                "sim_pasos": round(s_pasos, 3), "misma_fuente": misma_fuente,
            })
        min_sim = min(sims) if sims else 0
        max_sim = max(sims) if sims else 0
        tipo_grupo = "sufijo_numerico" if all(m["id"].rsplit("_", 1)[-1].isdigit() or True for m in []) else "titulo"
        # clasificar por si el id base (sin sufijo _N) coincide con el keeper
        import re
        base_keeper = re.sub(r"_\d+$", "", keeper)
        es_sufijo = all(re.sub(r"_\d+$", "", m["id"]) == base_keeper for m in detalle_miembros)
        recomendacion = "aprobar" if min_sim >= 0.55 else ("revisar" if min_sim >= 0.35 else "rechazar")
        resultados.append({
            "keeper": keeper, "titulo_keeper": kd.get("titulo_concepto", ""),
            "fuente_keeper": kd.get("fuente", ""),
            "es_sufijo_numerico": es_sufijo,
            "miembros": detalle_miembros,
            "min_sim_resumen": round(min_sim, 3), "max_sim_resumen": round(max_sim, 3),
            "recomendacion": recomendacion,
        })
    return resultados


if __name__ == "__main__":
    todo = {}
    for cat in CATEGORIAS:
        r = analizar(cat)
        todo[cat] = r
        conteo = {"aprobar": 0, "revisar": 0, "rechazar": 0}
        for g in r:
            conteo[g["recomendacion"]] += 1
        print(f"{cat}: {len(r)} grupos -- aprobar={conteo['aprobar']} revisar={conteo['revisar']} rechazar={conteo['rechazar']}")
    Path("scripts/hseq/_dedup_analisis.json").write_text(
        json.dumps(todo, ensure_ascii=False, indent=2), encoding="utf-8")
    print("\nDetalle completo en scripts/hseq/_dedup_analisis.json")
