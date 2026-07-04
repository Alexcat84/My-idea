import os
import sys
import json
import re
import anthropic

# Añadir la ruta de scripts originales para poder importar chunker sin tocar el repo original
sys.path.append(r"C:\Users\AlexDesk\Documents\I have an idea\scripts")
from chunker import chunk_text

# Cargar dotenv desde la raíz del proyecto para leer el API KEY
from dotenv import load_dotenv
load_dotenv(r"C:\Users\AlexDesk\Documents\I have an idea\.env")

api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key or api_key == "tu_clave_api_aqui":
    print("Por favor configura tu ANTHROPIC_API_KEY en el archivo .env")
    exit(1)

client = anthropic.Anthropic(api_key=api_key)

SYSTEM_PROMPT = """
Eres un experto en extracción estructurada de conocimiento para sistemas de grafos o 'telarañas'.
Tu tarea es leer fragmentos de libros sobre emprendimiento y diseño, y extraer CONCEPTOS CLAVE que puedan servir como nodos de acción.

CONTEXTO GLOBAL DE LA BIBLIOTECA:
Ten en cuenta que esta telaraña se construye a partir de los siguientes libros. Si un concepto requiere conocimientos de otro libro, puedes sugerir como 'nodos_previos' o 'nodos_siguientes' conceptos lógicos que se encontrarían en ellos:
1. A Project Manager's Book of Forms
2. Assembling Tomorrow: A Guide to Designing a Thriving Future
3. Business Model Generation (Osterwalder)
4. Change by Design (Tim Brown)
5. The Art of Thought (Wallas)
6. The Lean Startup (Eric Ries)
7. The Startup Owner's Manual (Steve Blank)
8. The field guide to human-centered design (IDEO)
9. Value Proposition Design
10. Winning at New Products
11. Financial Intelligence for Entrepreneurs
12. The Founder's Dilemmas
13. Venture Deals

Debes devolver EXCLUSIVAMENTE un arreglo JSON válido (una lista de objetos). NO incluyas texto antes ni después del JSON. NO uses formato markdown (```json).

Estructura requerida para cada objeto en el arreglo:
{
  "node_id": "identificador_unico_en_minusculas_y_guiones_bajos",
  "fase_proyecto": "ideacion | validacion | planificacion | ejecucion",
  "titulo_concepto": "Nombre del Concepto",
  "fuente": "Nombre del libro de donde viene (lo recibirás en el prompt)",
  "resumen_teorico": "Explicación detallada pero concisa",
  "pasos_accionables": ["Paso 1", "Paso 2"],
  "entregable_esperado": "Qué debe tener listo el usuario",
  "nodos_previos": ["node_ids_asumidos_previos"],
  "nodos_siguientes": ["node_ids_asumidos_siguientes"],
  "condiciones_activacion": ["Cuando usar este concepto (ej: Si el usuario no tiene mercado)"]
}

Si un fragmento de texto NO contiene conceptos estructurables, devuelve una lista vacía: []
"""

def extract_nodes_from_chunk(chunk, book_name):
    prompt = f"Fuente: {book_name}\n\nFragmento de texto:\n{chunk}"
    
    try:
        response = client.messages.create(
            model="claude-sonnet-5", # Usando el modelo de alta capacidad con descuento
            max_tokens=8192,
            system=SYSTEM_PROMPT,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        result_text = ""
        for block in response.content:
            if getattr(block, "type", "") == "text":
                result_text = block.text
                break
        
        if result_text.startswith("```json"):
            result_text = result_text[7:]
        if result_text.endswith("```"):
            result_text = result_text[:-3]
            
        result_text = result_text.strip()
        
        nodes = json.loads(result_text)
        return nodes
    except json.JSONDecodeError as e:
        print(f"Error al decodificar JSON de Claude: {e}")
        return []
    except Exception as e:
        print(f"Error en la API de Anthropic: {e}")
        return []

def process_book(file_path, output_dir):
    book_name = os.path.basename(file_path).replace(".txt", "")
    print(f"Procesando libro: {book_name}")
    
    chunks = chunk_text(file_path, max_words=5000)
    print(f"Total de chunks a procesar: {len(chunks)}")
    
    total_nodes_extracted = 0
    
    for i, chunk in enumerate(chunks):
        print(f"Procesando chunk {i+1}/{len(chunks)}...")
        nodes = extract_nodes_from_chunk(chunk, book_name)
        
        for node in nodes:
            if isinstance(node, dict) and "node_id" in node:
                node_id = node["node_id"]
                file_name = f"{node_id}.json"
                file_dest = os.path.join(output_dir, file_name)
                
                with open(file_dest, 'w', encoding='utf-8') as f:
                    json.dump(node, f, ensure_ascii=False, indent=2)
                
                total_nodes_extracted += 1
                print(f"  -> Nodo guardado: {file_name}")
                
    print(f"\nFinalizado. Total de nodos extraídos de {book_name}: {total_nodes_extracted}")

if __name__ == "__main__":
    work_dir = r"C:\Users\AlexDesk\Documents\I have an idea\New txt"
    
    for filename in os.listdir(work_dir):
        if filename.endswith(".txt"):
            abs_book_path = os.path.join(work_dir, filename)
            process_book(abs_book_path, work_dir)
            print("-" * 50)
