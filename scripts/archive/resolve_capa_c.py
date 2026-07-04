import json
import os

with open(r"C:\Users\AlexDesk\Documents\I have an idea\dataset\metadata\unresolved.json", "r", encoding="utf-8") as f:
    unresolved_data = json.load(f)

alias_map = {}
count = 0

for ghost_id, data in unresolved_data.items():
    mejor = data.get("mejor_candidato")
    if mejor and "node_id" in mejor:
        # Aunque el score sea bajo, para garantizar la conectividad total y eliminar 
        # las islas en esta fase, lo mapeamos a su nodo semántico más cercano.
        alias_map[ghost_id] = mejor["node_id"]
        count += 1

out_path = r"C:\Users\AlexDesk\Documents\I have an idea\dataset\metadata\alias_map_capa_c.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(alias_map, f, indent=2, ensure_ascii=False)

print(f"Finalizado. {count} alias de Capa C resueltos por aproximación semántica. Guardado en {out_path}")
