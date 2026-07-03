import os
import glob
import json

METADATA_DIR = r"C:\Users\AlexDesk\Documents\I have an idea\dataset\metadata"
# fix_spiderweb created dataset_clean, so we apply there and then move
NODOS_DIR = r"C:\Users\AlexDesk\Documents\I have an idea\dataset_clean" 

alias_maps = [
    "alias_map_capa_b.json",
    "alias_map_capa_c.json",
    "alias_map_capa_d_duplicates.json"
]

master_alias = {}

for am_file in alias_maps:
    path = os.path.join(METADATA_DIR, am_file)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            master_alias.update(data)

print(f"Cargados {len(master_alias)} alias manuales/heurísticos.")

files = glob.glob(os.path.join(NODOS_DIR, "*.json"))
updated = 0

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    changed = False
    for key in ["nodos_previos", "nodos_siguientes"]:
        if key in data and isinstance(data[key], list):
            new_list = []
            for ref in data[key]:
                if ref in master_alias:
                    new_list.append(master_alias[ref])
                    changed = True
                else:
                    new_list.append(ref)
            # deduplicate
            data[key] = list(dict.fromkeys(new_list))
            
    if changed:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        updated += 1
        
print(f"Se actualizaron {updated} archivos aplicando todos los alias restantes.")
