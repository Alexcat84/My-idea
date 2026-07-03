import re
import os

def clean_text(text):
    """Limpia el texto de caracteres especiales innecesarios o espacios extra."""
    text = re.sub(r'\n{3,}', '\n\n', text)  # Reemplazar múltiples saltos de línea por dos
    return text.strip()

def chunk_text(file_path, max_words=5000, overlap_words=500):
    """
    Lee un archivo txt y lo divide en chunks lógicos basados en párrafos (\n\n),
    agrupándolos hasta alcanzar un límite de palabras.
    Incluye un 'overlap' (solapamiento) para evitar cortar ideas a la mitad.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Archivo no encontrado: {file_path}")

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    content = clean_text(content)
    paragraphs = content.split('\n\n')
    
    chunks = []
    current_chunk = []
    current_word_count = 0
    
    i = 0
    while i < len(paragraphs):
        para = paragraphs[i].strip()
        if not para:
            i += 1
            continue
            
        words_in_para = len(para.split())
        
        if current_word_count + words_in_para > max_words and current_chunk:
            chunks.append("\n\n".join(current_chunk))
            
            # Retroceder 'overlap_words' para el siguiente chunk
            overlap_count = 0
            backtrack_i = i - 1
            while backtrack_i >= 0 and overlap_count < overlap_words:
                overlap_count += len(paragraphs[backtrack_i].split())
                backtrack_i -= 1
            
            i = backtrack_i + 1 # Reiniciar el índice para solapar
            current_chunk = []
            current_word_count = 0
        else:
            current_chunk.append(para)
            current_word_count += words_in_para
            i += 1
            
    if current_chunk:
        chunks.append("\n\n".join(current_chunk))
        
    return chunks

if __name__ == "__main__":
    # Prueba rápida
    import sys
    if len(sys.argv) > 1:
        test_file = sys.argv[1]
        chunks = chunk_text(test_file, max_words=800)
        print(f"Total chunks generados: {len(chunks)}")
        if chunks:
            print(f"Tamaño del primer chunk: {len(chunks[0].split())} palabras.")
            print("--- Primer Chunk ---")
            print(chunks[0][:500] + "...")
