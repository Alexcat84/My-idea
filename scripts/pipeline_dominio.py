#!/usr/bin/env python3
"""
pipeline_dominio.py - Genera nodos de conocimiento para una categoria
especifica y AISLADA (Books/Especificos/<Categoria>/), sin mezclarse con el
dataset general (dataset/nodos/, dominio "core") ni con otras categorias.

Diferencias clave frente a scripts/pipeline.py (el pipeline del dominio
"core"):
  - El SYSTEM_PROMPT lista SOLO los libros de la categoria que se esta
    procesando -- nunca los libros de otras categorias ni los del dominio
    "core" -- para que el modelo no invente referencias cruzadas hacia
    conceptos que no existen en este grafo aislado.
  - Cada nodo recibe "dominio": "<slug_de_la_categoria>" inyectado por
    codigo (no se le confia al modelo ese campo), listo para el filtro de
    dominios que ya existe en engine/prototipo_motor.py.
  - La salida vive en Books/Especificos/<Categoria>/nodos/, nunca en
    dataset/nodos/.
  - Acepta libros en .txt y en .md indistintamente (scripts/pipeline.py
    solo soportaba .txt).
  - Reanudable: cada chunk procesado se registra en nodos/_progreso.json;
    si se corta a la mitad (o se corre de nuevo por error), los chunks ya
    procesados no se vuelven a enviar a la API (evita pagar dos veces por
    el mismo fragmento).
  - Reintentos con backoff ante errores transitorios de la API (rate
    limit, timeouts de red) -- una corrida de este tamano (decenas/cientos
    de llamadas) es demasiado larga para no tolerar un fallo aislado.
  - Sin colisiones silenciosas: si dos libros de la misma categoria
    generan el mismo node_id, el segundo no pisa al primero -- se le
    agrega un sufijo numerico y se registra en el log.

Uso:
  # Vista previa sin gastar nada (cuenta libros/chunks, no llama a la API)
  python scripts/pipeline_dominio.py --categoria Environmental --dry-run
  python scripts/pipeline_dominio.py --todas --dry-run

  # Corrida real de una categoria
  python scripts/pipeline_dominio.py --categoria "Health and Safety"

  # Corrida real de las tres
  python scripts/pipeline_dominio.py --todas
"""
import argparse
import json
import os
import sys
import time
from pathlib import Path

from dotenv import load_dotenv

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from chunker import chunk_text  # noqa: E402

load_dotenv(BASE / ".env")

ESPECIFICOS_DIR = BASE / "Books" / "Especificos"

# Carpeta de categoria -> (slug de dominio, etiqueta humana para el prompt).
# El slug sigue la misma convencion ascii_id() que usa run_phase1.py para
# los node_id (minusculas, guion bajo, sin acentos) porque en el futuro
# puede terminar viviendo en el mismo tipo de validacion.
CATEGORIAS = {
    "Environmental": ("environmental", "Sostenibilidad Ambiental y Diseño Ecológico"),
    "Health and Safety": ("health_safety", "Seguridad y Salud Ocupacional"),
    "Quality": ("quality", "Gestión de Calidad"),
}

MAX_WORDS_POR_CHUNK = 5000
OVERLAP_WORDS = 500
MODEL = "claude-sonnet-5"
# claude-sonnet-5 soporta hasta 128000 tokens de salida (verificado via
# client.models.retrieve). 8192 resultaba insuficiente para chunks
# inusualmente densos en conceptos -- confirmado en vivo: un capitulo tipo
# "playbook" con ~20 estrategias nombradas corto la respuesta a mitad de
# un string JSON (stop_reason="max_tokens", exactamente en el limite).
# max_tokens es solo un techo -- no se paga por tokens no generados, asi
# que subirlo no tiene costo para los chunks normales que ya entraban
# comodos en 8192.
MAX_TOKENS = 16000
MAX_REINTENTOS = 3
BACKOFF_BASE_SEG = 5

NODE_SCHEMA_PROMPT = """
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


def build_system_prompt(dominio_label, book_names):
    lista_libros = "\n".join(f"{i}. {name}" for i, name in enumerate(book_names, start=1))
    return f"""
Eres un experto en extracción estructurada de conocimiento para sistemas de grafos o 'telarañas'.
Tu tarea es leer fragmentos de libros sobre {dominio_label} y extraer CONCEPTOS CLAVE que puedan servir como nodos de acción.

CONTEXTO GLOBAL DE LA BIBLIOTECA (dominio "{dominio_label}", AISLADO de cualquier otra área):
Esta telaraña se construye EXCLUSIVAMENTE a partir de los siguientes libros. Si un concepto requiere conocimientos de otro libro, solo puedes sugerir como 'nodos_previos' o 'nodos_siguientes' conceptos lógicos que se encontrarían en ESTOS libros -- nunca inventes referencias a libros de otras áreas (negocios, diseño, etc.) ni asumas que existen nodos fuera de esta lista:
{lista_libros}

Debes devolver EXCLUSIVAMENTE un arreglo JSON válido (una lista de objetos). NO incluyas texto antes ni después del JSON. NO uses formato markdown (```json).
{NODE_SCHEMA_PROMPT}"""


# ---------------------------------------------------------------------------
# Llamada a la API con reintentos
# ---------------------------------------------------------------------------

def extract_nodes_from_chunk(client, system_prompt, chunk, book_name):
    prompt = f"Fuente: {book_name}\n\nFragmento de texto:\n{chunk}"

    last_error = None
    for intento in range(1, MAX_REINTENTOS + 1):
        try:
            response = client.messages.create(
                model=MODEL,
                max_tokens=MAX_TOKENS,
                system=system_prompt,
                messages=[{"role": "user", "content": prompt}],
            )
            result_text = ""
            for block in response.content:
                if getattr(block, "type", "") == "text":
                    result_text = block.text
                    break

            if response.stop_reason == "max_tokens":
                # Se corto por el techo de salida antes de que json.loads
                # llegue a fallar mas abajo -- diagnosticado en vivo en un
                # capitulo tipo "playbook" con ~20 conceptos nombrados.
                # Marcarlo explicito ahorra tener que reproducir la llamada
                # para saber si fue esto o un JSON genuinamente mal formado.
                last_error = (f"Respuesta cortada por limite de tokens "
                              f"(stop_reason=max_tokens, {response.usage.output_tokens} "
                              f"tokens usados de {MAX_TOKENS}). Sube MAX_TOKENS si esto se repite.")
                if intento < MAX_REINTENTOS:
                    print(f"    [reintento {intento}/{MAX_REINTENTOS}] {last_error}")
                continue

            result_text = result_text.strip()
            if result_text.startswith("```json"):
                result_text = result_text[7:]
            if result_text.startswith("```"):
                result_text = result_text[3:]
            if result_text.endswith("```"):
                result_text = result_text[:-3]
            result_text = result_text.strip()
            result_text = _extraer_arreglo_json(result_text)

            return json.loads(result_text), None
        except json.JSONDecodeError as e:
            # Comprobado en vivo: el mismo chunk a veces produce JSON valido
            # y a veces no (varianza de muestreo del modelo), asi que SI
            # vale la pena reintentar en vez de rendirse de una -- pero
            # nunca mas de MAX_REINTENTOS veces, para no encadenar
            # reintentos infinitos en un chunk genuinamente problematico.
            last_error = f"JSON invalido: {e}"
            if intento < MAX_REINTENTOS:
                print(f"    [reintento {intento}/{MAX_REINTENTOS}] {last_error}")
        except Exception as e:  # rate limit, timeout, error de red, etc.
            last_error = str(e)
            if intento < MAX_REINTENTOS:
                espera = BACKOFF_BASE_SEG * (2 ** (intento - 1))
                print(f"    [reintento {intento}/{MAX_REINTENTOS}] {last_error} -- esperando {espera}s...")
                time.sleep(espera)
    return [], f"Fallo tras {MAX_REINTENTOS} intentos: {last_error}"


def _extraer_arreglo_json(text):
    """El modelo a veces antepone comentario conversacional antes del
    arreglo JSON real (ej. 'Voy a extraer los conceptos clave: ... [...')
    y a veces agrega texto despues del cierre, pese a la instruccion del
    prompt de devolver EXCLUSIVAMENTE el JSON. Busca el primer '[' y su
    ']' de cierre correspondiente (respetando anidamiento y contenido de
    strings) para tolerar ese preambulo/posambulo en vez de fallar.
    Confirmado en una corrida real: sin esto, un chunk que SI tenia un
    arreglo JSON valido se descartaba entero por el texto alrededor."""
    start = text.find("[")
    if start == -1:
        return text  # sin arreglo detectable; que json.loads reporte el error real
    depth = 0
    in_string = False
    escape = False
    for i in range(start, len(text)):
        ch = text[i]
        if in_string:
            if escape:
                escape = False
            elif ch == "\\":
                escape = True
            elif ch == '"':
                in_string = False
            continue
        if ch == '"':
            in_string = True
        elif ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
            if depth == 0:
                return text[start:i + 1]
    return text[start:]  # sin cierre encontrado (truncado); que json.loads falle con detalle


# ---------------------------------------------------------------------------
# Progreso (reanudable) y guardado de nodos sin colisiones
# ---------------------------------------------------------------------------

def load_progress(progress_path):
    if progress_path.exists():
        return json.loads(progress_path.read_text(encoding="utf-8"))
    return {}


def save_progress(progress_path, progress):
    progress_path.write_text(json.dumps(progress, ensure_ascii=False, indent=2), encoding="utf-8")


def save_node_sin_colision(node, output_dir, dominio_slug, log):
    # "dominio" se inserta justo despues de "fase_proyecto" (nunca se le
    # confia este campo al modelo) para mantener el mismo orden de lectura
    # que usa dataset/nodos/ tras el hotfix v2.1.1.
    ordenado = {}
    insertado = False
    for k, v in node.items():
        ordenado[k] = v
        if k == "fase_proyecto":
            ordenado["dominio"] = dominio_slug
            insertado = True
    if not insertado:
        ordenado["dominio"] = dominio_slug
    node = ordenado

    node_id = node.get("node_id")
    if not node_id:
        log["nodos_sin_id_descartados"] += 1
        return None

    dest = output_dir / f"{node_id}.json"
    final_id = node_id
    suffix = 2
    while dest.exists():
        # Node_id repetido dentro de la MISMA categoria (ej. dos libros
        # cubren el mismo concepto). No se pisa el archivo existente --
        # nunca se pierde un nodo ya guardado por una colision de nombre.
        final_id = f"{node_id}_{suffix}"
        dest = output_dir / f"{final_id}.json"
        suffix += 1
    if final_id != node_id:
        log["colisiones_renombradas"].append({"original": node_id, "guardado_como": final_id})
        node["node_id"] = final_id

    dest.write_text(json.dumps(node, ensure_ascii=False, indent=2), encoding="utf-8")
    return final_id


# ---------------------------------------------------------------------------
# Descubrimiento de libros y procesamiento por categoria
# ---------------------------------------------------------------------------

def discover_books(categoria_dir):
    books = []
    for path in sorted(categoria_dir.iterdir()):
        if path.is_file() and path.suffix.lower() in (".txt", ".md"):
            books.append(path)
    return books


def process_categoria(categoria_nombre, dry_run=False, client=None, presupuesto=None):
    """presupuesto: dict mutable {"restantes": N} compartido entre categorias
    en la misma invocacion -- limita el numero TOTAL de llamadas a la API
    en esta corrida (usado para pruebas humo baratas). None = sin limite."""
    if categoria_nombre not in CATEGORIAS:
        print(f"ERROR: categoria desconocida '{categoria_nombre}'. Opciones: {list(CATEGORIAS)}")
        return

    dominio_slug, dominio_label = CATEGORIAS[categoria_nombre]
    categoria_dir = ESPECIFICOS_DIR / categoria_nombre
    if not categoria_dir.exists():
        print(f"ERROR: no existe la carpeta {categoria_dir}")
        return

    output_dir = categoria_dir / "nodos"
    progress_path = output_dir / "_progreso.json"

    books = discover_books(categoria_dir)
    if not books:
        print(f"[{categoria_nombre}] No se encontraron libros .txt/.md.")
        return

    print(f"\n=== Categoria: {categoria_nombre} (dominio='{dominio_slug}') ===")
    print(f"  Libros encontrados: {len(books)}")

    book_names = [p.stem for p in books]
    system_prompt = build_system_prompt(dominio_label, book_names)

    plan = []
    total_chunks = 0
    for book_path in books:
        chunks = chunk_text(str(book_path), max_words=MAX_WORDS_POR_CHUNK, overlap_words=OVERLAP_WORDS)
        plan.append((book_path, chunks))
        total_chunks += len(chunks)
        print(f"    - {book_path.name}: {len(chunks)} chunk(s)")

    print(f"  Total de llamadas a la API estimadas: {total_chunks}")

    if dry_run:
        return

    output_dir.mkdir(parents=True, exist_ok=True)
    progress = load_progress(progress_path)
    log = {"colisiones_renombradas": [], "nodos_sin_id_descartados": 0, "errores": []}

    total_nodos = 0
    for book_path, chunks in plan:
        book_name = book_path.stem
        book_progress = progress.setdefault(book_name, {"total_chunks": len(chunks), "completados": []})

        if book_progress.get("total_chunks") != len(chunks):
            print(f"  AVISO: '{book_name}' cambio de tamano desde la ultima corrida "
                  f"({book_progress.get('total_chunks')} -> {len(chunks)} chunks). Reprocesando desde cero.")
            book_progress = {"total_chunks": len(chunks), "completados": []}
            progress[book_name] = book_progress

        completados = set(book_progress["completados"])
        pendientes = [i for i in range(len(chunks)) if i not in completados]
        if not pendientes:
            print(f"  '{book_name}': ya completo (reanudado desde progreso previo). Nada que hacer.")
            continue

        print(f"  Procesando '{book_name}': {len(pendientes)}/{len(chunks)} chunk(s) pendientes...")
        for i in pendientes:
            if presupuesto is not None and presupuesto["restantes"] <= 0:
                print("  Presupuesto de llamadas agotado (--max-chunks) -- deteniendo aqui. "
                      "El progreso ya guardado permite continuar despues sin repetir trabajo.")
                log_path = output_dir / "_log_ultima_corrida.json"
                log_path.write_text(json.dumps(log, ensure_ascii=False, indent=2), encoding="utf-8")
                return
            print(f"    Chunk {i + 1}/{len(chunks)}...")
            nodes, error = extract_nodes_from_chunk(client, system_prompt, chunks[i], book_name)
            if presupuesto is not None:
                presupuesto["restantes"] -= 1
            if error:
                print(f"    ERROR (chunk {i + 1} de '{book_name}'): {error}")
                log["errores"].append({"libro": book_name, "chunk": i, "error": error})
                continue  # no se marca como completado -- una proxima corrida lo reintenta

            for node in nodes:
                if isinstance(node, dict) and node.get("node_id"):
                    saved_id = save_node_sin_colision(node, output_dir, dominio_slug, log)
                    if saved_id:
                        total_nodos += 1
                        print(f"      -> nodo guardado: {saved_id}.json")

            book_progress["completados"].append(i)
            save_progress(progress_path, progress)  # persistido tras cada chunk, no solo al final

    print(f"\n[{categoria_nombre}] Finalizado. Nodos nuevos guardados: {total_nodos}")
    if log["colisiones_renombradas"]:
        print(f"  Colisiones de node_id renombradas: {len(log['colisiones_renombradas'])} (ver log)")
    if log["errores"]:
        print(f"  Chunks con error (no completados, se reintentan en la proxima corrida): {len(log['errores'])}")

    log_path = output_dir / "_log_ultima_corrida.json"
    log_path.write_text(json.dumps(log, ensure_ascii=False, indent=2), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--categoria", choices=list(CATEGORIAS), help="Procesar solo esta categoria")
    parser.add_argument("--todas", action="store_true", help="Procesar las 3 categorias")
    parser.add_argument("--dry-run", action="store_true",
                         help="Solo muestra libros/chunks encontrados, no llama a la API ni escribe nada")
    parser.add_argument("--max-chunks", type=int, default=None,
                         help="Prueba humo: limita el TOTAL de llamadas a la API en esta corrida "
                              "(compartido entre categorias si se usa con --todas). "
                              "Los chunks procesados cuentan como progreso real: una corrida "
                              "posterior sin este limite retoma justo donde se quedo.")
    args = parser.parse_args()

    if not args.categoria and not args.todas:
        parser.error("especifica --categoria <nombre> o --todas")

    client = None
    if not args.dry_run:
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key or api_key == "tu_clave_api_aqui":
            print("Por favor configura tu ANTHROPIC_API_KEY en el archivo .env")
            sys.exit(1)
        import anthropic
        client = anthropic.Anthropic(api_key=api_key)

    presupuesto = {"restantes": args.max_chunks} if args.max_chunks is not None else None

    categorias_a_correr = list(CATEGORIAS) if args.todas else [args.categoria]
    for categoria in categorias_a_correr:
        if presupuesto is not None and presupuesto["restantes"] <= 0:
            print(f"\nPresupuesto agotado, no se procesa '{categoria}' en esta corrida.")
            continue
        process_categoria(categoria, dry_run=args.dry_run, client=client, presupuesto=presupuesto)


if __name__ == "__main__":
    main()
