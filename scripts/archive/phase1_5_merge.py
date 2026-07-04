import json
import os

NODOS_DIR = r"C:\Users\AlexDesk\Documents\I have an idea\dataset\nodos"
METADATA_DIR = r"C:\Users\AlexDesk\Documents\I have an idea\dataset\metadata"

clusters = {
    "producto_minimo_viable": [
        "mvp_minimo_viable", 
        "producto_minimo_viable_mvp", 
        "minimum_viable_product_discovery",
        "minimum_viable_product_mvp"
    ],
    "lienzo_modelo_negocio": [
        "business_model_canvas_hcd",
        "business_model_canvas_ideo",
        "business_model_canvas_refresher"
    ]
}

alias_map_dupes = {}
count = 0

for canonical, dupes in clusters.items():
    canon_path = os.path.join(NODOS_DIR, f"{canonical}.json")
    if not os.path.exists(canon_path):
        print(f"Advertencia: Nodo canónico no existe {canonical}")
        continue
        
    with open(canon_path, "r", encoding="utf-8") as f:
        canon_data = json.load(f)
        
    for dupe in dupes:
        dupe_path = os.path.join(NODOS_DIR, f"{dupe}.json")
        if not os.path.exists(dupe_path):
            continue
            
        with open(dupe_path, "r", encoding="utf-8") as f:
            dupe_data = json.load(f)
            
        # Merge lists without duplicates
        for key in ["pasos_accionables", "condiciones_activacion", "nodos_previos", "nodos_siguientes"]:
            if key in dupe_data and isinstance(dupe_data[key], list):
                if key not in canon_data:
                    canon_data[key] = []
                # append unique items
                for item in dupe_data[key]:
                    if item not in canon_data[key]:
                        canon_data[key].append(item)
                        
        # Register in alias map
        alias_map_dupes[dupe] = canonical
        count += 1
        
        # Delete duplicate file
        os.remove(dupe_path)
        print(f"Fusionado y eliminado duplicado: {dupe}")
        
    # Save canonical
    with open(canon_path, "w", encoding="utf-8") as f:
        json.dump(canon_data, f, indent=2, ensure_ascii=False)
    print(f"Nodo canónico actualizado: {canonical}")

alias_out = os.path.join(METADATA_DIR, "alias_map_capa_d_duplicates.json")
with open(alias_out, "w", encoding="utf-8") as f:
    json.dump(alias_map_dupes, f, indent=2, ensure_ascii=False)

print(f"Fase 1.5 Completada. {count} duplicados fusionados semánticamente.")
