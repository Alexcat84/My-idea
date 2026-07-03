import os
import json

def validate_graph(dataset_dir):
    if not os.path.exists(dataset_dir):
        print(f"Directorio no encontrado: {dataset_dir}")
        return

    # 1. Obtener todos los node_ids existentes (basado en los archivos)
    existing_nodes = set()
    node_data = {}
    
    for filename in os.listdir(dataset_dir):
        if filename.endswith(".json"):
            node_id = filename.replace(".json", "")
            existing_nodes.add(node_id)
            
            filepath = os.path.join(dataset_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    node_data[node_id] = data
                except json.JSONDecodeError:
                    print(f"Error leyendo JSON: {filename}")
    
    print(f"Total de nodos encontrados: {len(existing_nodes)}\n")

    # 2. Analizar las conexiones
    broken_links = []
    
    for node_id, data in node_data.items():
        previos = data.get("nodos_previos", [])
        siguientes = data.get("nodos_siguientes", [])
        
        for p in previos:
            if p not in existing_nodes:
                broken_links.append({"from": node_id, "to": p, "type": "previo"})
                
        for s in siguientes:
            if s not in existing_nodes:
                broken_links.append({"from": node_id, "to": s, "type": "siguiente"})

    # 3. Reporte de hallazgos
    if not broken_links:
        print("El grafo es perfecto! Todos los enlaces apuntan a nodos existentes.")
    else:
        print(f"Se encontraron {len(broken_links)} enlaces rotos (referencias a nodos que no existen):")
        for link in broken_links:
            print(f"  - El nodo '{link['from']}' busca un nodo {link['type']} llamado '{link['to']}' (NO EXISTE)")

if __name__ == "__main__":
    dataset_dir = r"..\dataset\nodos"
    script_dir = os.path.dirname(os.path.abspath(__file__))
    abs_dataset_dir = os.path.join(script_dir, dataset_dir)
    
    validate_graph(abs_dataset_dir)
