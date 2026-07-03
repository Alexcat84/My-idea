import os
import glob
import json
import random

NODOS_DIR = r"C:\Users\AlexDesk\Documents\I have an idea\dataset\nodos"
files = glob.glob(os.path.join(NODOS_DIR, "*.json"))

nodes = {}
incoming = {}
for f in files:
    with open(f, "r", encoding="utf-8") as file:
        data = json.load(file)
        node_id = data["node_id"]
        nodes[node_id] = data
        if node_id not in incoming:
            incoming[node_id] = []

for node_id, data in nodes.items():
    for n_sig in data.get("nodos_siguientes", []):
        if n_sig in nodes:
            if n_sig not in incoming:
                incoming[n_sig] = []
            incoming[n_sig].append(node_id)

orphans = [n for n, incom in incoming.items() if len(incom) == 0]
print(f"Total huérfanos encontrados: {len(orphans)}")

# Agrupar nodos no huérfanos por fase
parents_by_phase = {"ideacion": [], "validacion": [], "planificacion": [], "ejecucion": []}
for node_id, data in nodes.items():
    if node_id not in orphans:
        fase = data.get("fase_proyecto", "ideacion")
        if fase in parents_by_phase:
            parents_by_phase[fase].append(node_id)

# Para cada huérfano, encontrar un padre por similitud de palabras clave o aleatorio
count = 0
for orphan_id in orphans:
    orphan_data = nodes[orphan_id]
    fase = orphan_data.get("fase_proyecto", "ideacion")
    
    if fase not in parents_by_phase or not parents_by_phase[fase]:
        # Fallback si no hay padres en la fase
        fase = list(parents_by_phase.keys())[0]
        
    candidates = parents_by_phase[fase]
    # Buscar palabras clave comunes en el titulo
    words = set(orphan_data.get("titulo_concepto", "").lower().split())
    
    best_parent = None
    best_overlap = -1
    
    for cand in candidates:
        cand_words = set(nodes[cand].get("titulo_concepto", "").lower().split())
        overlap = len(words.intersection(cand_words))
        if overlap > best_overlap:
            best_overlap = overlap
            best_parent = cand
            
    if best_parent is None:
        best_parent = random.choice(candidates)
        
    # Conectar
    if "nodos_siguientes" not in nodes[best_parent]:
        nodes[best_parent]["nodos_siguientes"] = []
    nodes[best_parent]["nodos_siguientes"].append(orphan_id)
    
    if "nodos_previos" not in nodes[orphan_id]:
        nodes[orphan_id]["nodos_previos"] = []
    nodes[orphan_id]["nodos_previos"].append(best_parent)
    
    count += 1

# Guardar archivos modificados
for node_id, data in nodes.items():
    file_path = os.path.join(NODOS_DIR, f"{node_id}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Fase 1.3 Completada: {count} huérfanos reconectados usando parentesco léxico y heurístico.")
