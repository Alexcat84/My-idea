import os
import json
import re
from dotenv import load_dotenv
import anthropic
from chunker import chunk_text

# Cargar variables de entorno
load_dotenv()

# Inicializar cliente de Anthropic
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
            max_tokens=8192,         # Sonnet permite respuestas mucho más largas
            system=SYSTEM_PROMPT,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        # Obtener el texto de la respuesta ignorando los bloques de pensamiento
        result_text = ""
        for block in response.content:
            if getattr(block, "type", "") == "text":
                result_text = block.text
                break
        
        # Limpiar posibles bloques markdown (```json ... ```)
        if result_text.startswith("```json"):
            result_text = result_text[7:]
        if result_text.endswith("```"):
            result_text = result_text[:-3]
            
        result_text = result_text.strip()
        
        # Convertir a JSON
        nodes = json.loads(result_text)
        return nodes
    except json.JSONDecodeError as e:
        print(f"Error al decodificar JSON de Claude: {e}")
        try:
            raw_text = result_text if 'result_text' in locals() else 'N/A'
            print("Respuesta raw:", raw_text.encode('cp1252', errors='replace').decode('cp1252'))
        except Exception:
            print("Respuesta raw: [No se pudo imprimir por error de codificación]")
        return []
    except Exception as e:
        print(f"Error en la API de Anthropic: {e}")
        return []

def process_book(file_path, output_dir):
    book_name = os.path.basename(file_path).replace(".txt", "")
    print(f"Procesando libro: {book_name}")
    
    # 1. Hacer Chunking
    chunks = chunk_text(file_path, max_words=5000)
    print(f"Total de chunks a procesar: {len(chunks)}")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    total_nodes_extracted = 0
    
    # 2. Procesar TODO el libro
    for i, chunk in enumerate(chunks):
        print(f"Procesando chunk {i+1}/{len(chunks)}...")
        nodes = extract_nodes_from_chunk(chunk, book_name)
        
        for node in nodes:
            if isinstance(node, dict) and "node_id" in node:
                # Guardar el JSON
                node_id = node["node_id"]
                file_name = f"{node_id}.json"
                file_dest = os.path.join(output_dir, file_name)
                
                with open(file_dest, 'w', encoding='utf-8') as f:
                    json.dump(node, f, ensure_ascii=False, indent=2)
                
                total_nodes_extracted += 1
                print(f"  -> Nodo guardado: {file_name}")
                
    print(f"\nFinalizado. Total de nodos extraídos en esta prueba: {total_nodes_extracted}")

if __name__ == "__main__":
    txt_directory = r"..\txt"
    output_directory = r"..\dataset\nodos"
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    abs_txt_dir = os.path.join(script_dir, txt_directory)
    abs_output = os.path.join(script_dir, output_directory)
    
    if not os.path.exists(abs_txt_dir):
        print(f"Directorio de textos no encontrado: {abs_txt_dir}")
        exit(1)
        
    skip_files = [
        "The Lean Startup_ How Today's E - Eric Ries.txt",
        "A Project Manager's Book of For - Cynthia Stackpole Snyder.txt",
        "Assembling Tomorrow_ A Guide to - Scott Doorley.txt",
        "Business Model Generation_ A Ha - Osterwalder, Alexander.txt",
        "Change by Design, Revised and U - Tim Brown.txt",
        "The Art of Thought - Wallas, Graham.txt"
    ]
    
    for filename in os.listdir(abs_txt_dir):
        if filename.endswith(".txt") and filename not in skip_files:
            abs_book_path = os.path.join(abs_txt_dir, filename)
            process_book(abs_book_path, abs_output)
            print("-" * 50)

