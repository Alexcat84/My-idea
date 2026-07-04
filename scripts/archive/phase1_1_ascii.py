import os
import glob
import json
import unicodedata

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

NODOS_DIR = r"C:\Users\AlexDesk\Documents\I have an idea\dataset\nodos"
files = glob.glob(os.path.join(NODOS_DIR, "*.json"))

rename_map = {}

# Step 1: Rename files and build rename_map
for file_path in files:
    filename = os.path.basename(file_path)
    # the filenames might have been mangled by git or os, we decode safely or just replace non-ascii
    # Actually, let's just do a manual replace for the common ones since it's only 12 files.
    # Or use unicodedata.
    clean_name = remove_accents(filename).replace('ñ', 'n').replace('Ñ', 'n')
    
    # some mangled files from git output looked like "dise\342\224..."
    # let's just do a robust ascii conversion
    clean_name = "".join([c if ord(c) < 128 else '_' for c in clean_name])
    clean_name = clean_name.replace('__', '_').replace('_.json', '.json')
    
    if clean_name != filename:
        old_id = filename.replace('.json', '')
        new_id = clean_name.replace('.json', '')
        # However, due to file system encoding on windows, let's just rename it via os.rename
        new_path = os.path.join(NODOS_DIR, clean_name)
        try:
            os.rename(file_path, new_path)
            rename_map[old_id] = new_id
            print(f"Renamed: {old_id.encode('utf-8', 'ignore')} -> {new_id}")
        except Exception as e:
            print(f"Error renaming {filename.encode('utf-8', 'ignore')}: {e}")

# Step 2: Update references in ALL files
if rename_map:
    all_files = glob.glob(os.path.join(NODOS_DIR, "*.json"))
    updated_count = 0
    for file_path in all_files:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        changed = False
        for key in ["nodos_previos", "nodos_siguientes"]:
            if key in data and isinstance(data[key], list):
                new_list = []
                for ref in data[key]:
                    # check if the ref is in the rename map
                    # wait, the ref might be the original string before mangling, e.g. "diseño"
                    # let's normalize the ref as well if it has non-ascii
                    norm_ref = "".join([c if ord(c) < 128 else '_' for c in remove_accents(ref).replace('ñ', 'n')])
                    norm_ref = norm_ref.replace('__', '_')
                    
                    # If it maps to one of our new_ids, or if the ref itself was changed
                    # But actually we just check rename_map
                    if ref in rename_map:
                        new_list.append(rename_map[ref])
                        changed = True
                    else:
                        # try normalized
                        if norm_ref != ref:
                            new_list.append(norm_ref)
                            changed = True
                        else:
                            new_list.append(ref)
                data[key] = new_list
                
        # Also update node_id if it's inside the json
        if data.get("node_id") in rename_map:
            data["node_id"] = rename_map[data["node_id"]]
            changed = True
            
        if changed:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            updated_count += 1
            
    print(f"Fase 1.1 Completada: {len(rename_map)} IDs normalizados, {updated_count} archivos actualizados.")
else:
    print("Fase 1.1: No se encontraron archivos con caracteres especiales.")
