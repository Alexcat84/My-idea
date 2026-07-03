import os
import json

def generate_index(dataset_dir, output_file):
    if not os.path.exists(dataset_dir):
        print("No se encontró la carpeta dataset")
        return

    nodes_by_phase = {
        "ideacion": [],
        "validacion": [],
        "planificacion": [],
        "ejecucion": [],
        "otra": []
    }

    for filename in os.listdir(dataset_dir):
        if filename.endswith(".json"):
            filepath = os.path.join(dataset_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    fase = data.get("fase_proyecto", "otra").lower()
                    
                    # Normalizar fases
                    if "ideaci" in fase: fase = "ideacion"
                    elif "valida" in fase: fase = "validacion"
                    elif "planificaci" in fase: fase = "planificacion"
                    elif "ejecuci" in fase: fase = "ejecucion"
                    else: fase = "otra"
                    
                    if fase not in nodes_by_phase:
                        fase = "otra"

                    nodes_by_phase[fase].append(data)
                except Exception as e:
                    pass

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Índice de Nodos: The Lean Startup\n\n")
        f.write("Este documento lista todos los conceptos extraídos y estructurados por el sistema.\n\n")
        
        for phase, nodes in nodes_by_phase.items():
            if not nodes:
                continue
            f.write(f"## Fase: {phase.capitalize()}\n\n")
            for node in nodes:
                f.write(f"### {node.get('titulo_concepto', 'Sin título')} (`{node.get('node_id', '')}`)\n")
                f.write(f"- **Resumen**: {node.get('resumen_teorico', '')[:150]}...\n")
                f.write(f"- **Conecta hacia**: {', '.join(node.get('nodos_siguientes', []))}\n\n")

if __name__ == "__main__":
    dataset_dir = r"..\dataset\nodos"
    # Guardar directamente en la carpeta brain como artifact
    output_file = r"C:\Users\AlexDesk\.gemini\antigravity\brain\8039b8bd-7bfd-4844-a5b5-532107ff4d03\lean_startup_index.md"
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    abs_dataset_dir = os.path.join(script_dir, dataset_dir)
    
    generate_index(abs_dataset_dir, output_file)
