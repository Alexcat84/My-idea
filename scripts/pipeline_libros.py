#!/usr/bin/env python3
"""
pipeline_libros.py - Fase 3.7: extraccion de nodos de la nueva biblioteca
books/ (post-convergencia). Dos clases de grupos:

  1. "general" (books/General/, con subcarpetas tematicas): libros
     COMPLEMENTARIOS de la telarana principal -- cubren vacios reales
     detectados (clientes/postventa, IA para negocios, liderazgo/crisis,
     marketing/crecimiento, operaciones/logistica, ventas). Sus nodos
     nacen con dominio "core" porque se incorporaran a lo ya existente,
     y el prompt SI conoce la biblioteca core original para que las
     referencias cruzadas apunten a conceptos plausibles de la telarana.
     Salida: books/General/nodos/ (staging aislado; la integracion al
     dataset es un paso posterior con su propio saneamiento).

  2. Add-ons aislados (books/franquicias, books/exportacion,
     books/seguridad_digital): futuros mundos. Mismo contrato que los
     packs HSEQ: prompt aislado (solo los libros del grupo), dominio
     propio inyectado por codigo, salida en books/<grupo>/nodos/.

Hereda de scripts/pipeline_dominio.py (el pipeline probado de los packs):
reanudable via _progreso.json, reintentos con backoff, tolerancia a
preambulos alrededor del JSON, colisiones de node_id con sufijo. Agrega:
  - descubrimiento RECURSIVO de libros (General tiene subcarpetas),
  - etiquetas legibles para archivos con nombres crudos (NIST, export),
  - conteo de tokens reales y costo total por corrida (claude-sonnet-5:
    $2/$10 por MTok en precio introductorio hasta 2026-08-31; lista $3/$15).

Uso:
  python scripts/pipeline_libros.py --grupo general --dry-run
  python scripts/pipeline_libros.py --todos --dry-run
  python scripts/pipeline_libros.py --grupo general
  python scripts/pipeline_libros.py --todos [--max-chunks N]
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
from pipeline_dominio import (  # noqa: E402
    BACKOFF_BASE_SEG,
    MAX_REINTENTOS,
    MAX_TOKENS,
    MAX_WORDS_POR_CHUNK,
    MODEL,
    NODE_SCHEMA_PROMPT,
    OVERLAP_WORDS,
    _extraer_arreglo_json,
    load_progress,
    save_node_sin_colision,
    save_progress,
)

load_dotenv(BASE / ".env")

BOOKS_DIR = BASE / "books"

# Precio introductorio de claude-sonnet-5 (hasta 2026-08-31); lista: $3/$15.
PRICE_INPUT_PER_MTOK = 2.00
PRICE_OUTPUT_PER_MTOK = 10.00

# La biblioteca core ORIGINAL (la de scripts/pipeline.py): contexto para el
# grupo "general", cuyos nodos se integraran a esa misma telarana.
LIBROS_CORE_ORIGINALES = [
    "A Project Manager's Book of Forms",
    "Assembling Tomorrow: A Guide to Designing a Thriving Future",
    "Business Model Generation (Osterwalder)",
    "Change by Design (Tim Brown)",
    "The Art of Thought (Wallas)",
    "The Lean Startup (Eric Ries)",
    "The Startup Owner's Manual (Steve Blank)",
    "The field guide to human-centered design (IDEO)",
    "Value Proposition Design",
    "Winning at New Products",
]

# Nombres legibles para archivos con nombres crudos: es lo que viaja en el
# campo "fuente" de cada nodo. Los stems ya legibles se usan tal cual.
LIBRO_LABELS = {
    "basic-guide-to-exporting_Latest_eg_main_086196":
        "A Basic Guide to Exporting (U.S. Commercial Service, 11th Edition)",
    "NIST.SP.1300":
        "NIST SP 1300: Cybersecurity Framework 2.0 - Small Business Quick-Start Guide",
    "NIST.SP.1314":
        "NIST SP 1314: Risk Management Framework - Small Enterprise Quick Start Guide",
    "NIST.SP.1318":
        "NIST SP 1318: Protecting CUI (SP 800-171 r3) - Small Business Primer",
    "cybersecurity_sb_nist-cyber-framework":
        "Cybersecurity for Small Business: Understanding the NIST Cybersecurity Framework (FTC)",
    "Getting-Started-NIST-Privacy-Framework-Guide":
        "Getting Started with the NIST Privacy Framework: A Guide for Small and Medium Businesses",
}

# grupo -> (carpeta, dominio inyectado, etiqueta humana para el prompt)
GRUPOS = {
    "general": ("General", "core",
                "emprendimiento (complementos de la telaraña principal: clientes y postventa, "
                "IA para negocios, liderazgo y crisis, marketing y crecimiento, "
                "operaciones y logística, ventas)"),
    "franquicias": ("franquicias", "franquicias",
                    "Franquicias (convertir un negocio probado en franquicia y escalarlo)"),
    "exportacion": ("exportacion", "exportacion",
                    "Exportación e internacionalización de pequeñas y medianas empresas"),
    "seguridad_digital": ("seguridad_digital", "seguridad_digital",
                          "Ciberseguridad, privacidad y gestión de riesgo digital para pequeños negocios"),
}


def build_system_prompt_general(book_names):
    lista_core = "\n".join(f"- {n}" for n in LIBROS_CORE_ORIGINALES)
    lista_nuevos = "\n".join(f"{i}. {n}" for i, n in enumerate(book_names, start=1))
    return f"""
Eres un experto en extracción estructurada de conocimiento para sistemas de grafos o 'telarañas'.
Tu tarea es leer fragmentos de libros sobre emprendimiento y extraer CONCEPTOS CLAVE que puedan servir como nodos de acción.

CONTEXTO GLOBAL DE LA BIBLIOTECA:
Esta telaraña principal ya existe y fue construida a partir de estos libros base:
{lista_core}

Ahora se le suman los siguientes libros COMPLEMENTARIOS, que cubren vacíos reales detectados (clientes y postventa, IA para negocios, liderazgo y crisis, marketing y crecimiento, operaciones y logística, ventas). Tú extraes nodos de ESTOS libros:
{lista_nuevos}

Si un concepto requiere conocimientos previos o posteriores, puedes sugerir como 'nodos_previos' o 'nodos_siguientes' conceptos lógicos que se encontrarían en los libros complementarios O en la biblioteca base de la telaraña principal.

Debes devolver EXCLUSIVAMENTE un arreglo JSON válido (una lista de objetos). NO incluyas texto antes ni después del JSON. NO uses formato markdown (```json).
{NODE_SCHEMA_PROMPT}"""


def build_system_prompt_aislado(dominio_label, book_names):
    lista_libros = "\n".join(f"{i}. {name}" for i, name in enumerate(book_names, start=1))
    return f"""
Eres un experto en extracción estructurada de conocimiento para sistemas de grafos o 'telarañas'.
Tu tarea es leer fragmentos de libros sobre {dominio_label} y extraer CONCEPTOS CLAVE que puedan servir como nodos de acción.

CONTEXTO GLOBAL DE LA BIBLIOTECA (dominio "{dominio_label}", AISLADO de cualquier otra área):
Esta telaraña se construye EXCLUSIVAMENTE a partir de los siguientes libros. Si un concepto requiere conocimientos de otro libro, solo puedes sugerir como 'nodos_previos' o 'nodos_siguientes' conceptos lógicos que se encontrarían en ESTOS libros -- nunca inventes referencias a libros de otras áreas (negocios, diseño, etc.) ni asumas que existen nodos fuera de esta lista:
{lista_libros}

Debes devolver EXCLUSIVAMENTE un arreglo JSON válido (una lista de objetos). NO incluyas texto antes ni después del JSON. NO uses formato markdown (```json).
{NODE_SCHEMA_PROMPT}"""


def extract_nodes_from_chunk(client, system_prompt, chunk, book_name, uso):
    """Como pipeline_dominio.extract_nodes_from_chunk, pero acumula tokens
    reales en `uso` ({"in": N, "out": N}) para reportar el costo total."""
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
            uso["in"] += response.usage.input_tokens
            uso["out"] += response.usage.output_tokens

            result_text = ""
            for block in response.content:
                if getattr(block, "type", "") == "text":
                    result_text = block.text
                    break

            if response.stop_reason == "max_tokens":
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
            result_text = _extraer_arreglo_json(result_text.strip())

            return json.loads(result_text), None
        except json.JSONDecodeError as e:
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


def discover_books(grupo_dir):
    """Recursivo: books/General tiene subcarpetas tematicas. Se excluye la
    carpeta de salida nodos/ (y cualquier archivo interno _*)."""
    books = []
    for path in sorted(grupo_dir.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in (".txt", ".md"):
            continue
        if "nodos" in path.relative_to(grupo_dir).parts or path.name.startswith("_"):
            continue
        books.append(path)
    return books


def label_de_libro(path):
    return LIBRO_LABELS.get(path.stem, path.stem)


def process_grupo(nombre, dry_run=False, client=None, presupuesto=None):
    carpeta, dominio_slug, dominio_label = GRUPOS[nombre]
    grupo_dir = BOOKS_DIR / carpeta
    if not grupo_dir.exists():
        print(f"ERROR: no existe la carpeta {grupo_dir}")
        return

    output_dir = grupo_dir / "nodos"
    progress_path = output_dir / "_progreso.json"

    books = discover_books(grupo_dir)
    if not books:
        print(f"[{nombre}] No se encontraron libros .txt/.md.")
        return

    print(f"\n=== Grupo: {nombre} (dominio='{dominio_slug}') ===")
    print(f"  Libros encontrados: {len(books)}")

    book_labels = [label_de_libro(p) for p in books]
    if nombre == "general":
        system_prompt = build_system_prompt_general(book_labels)
    else:
        system_prompt = build_system_prompt_aislado(dominio_label, book_labels)

    plan = []
    total_chunks = 0
    for book_path in books:
        chunks = chunk_text(str(book_path), max_words=MAX_WORDS_POR_CHUNK, overlap_words=OVERLAP_WORDS)
        plan.append((book_path, chunks))
        total_chunks += len(chunks)
        print(f"    - {book_path.relative_to(grupo_dir)}: {len(chunks)} chunk(s)")

    print(f"  Total de llamadas a la API estimadas: {total_chunks}")

    if dry_run:
        return

    output_dir.mkdir(parents=True, exist_ok=True)
    progress = load_progress(progress_path)
    log = {"colisiones_renombradas": [], "nodos_sin_id_descartados": 0, "errores": []}
    uso = {"in": 0, "out": 0}
    t0 = time.time()

    total_nodos = 0
    for book_path, chunks in plan:
        book_name = label_de_libro(book_path)
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
                _cerrar(output_dir, log, uso, t0)
                return
            print(f"    Chunk {i + 1}/{len(chunks)}...")
            nodes, error = extract_nodes_from_chunk(client, system_prompt, chunks[i], book_name, uso)
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
            print(f"      -> {sum(1 for n in nodes if isinstance(n, dict) and n.get('node_id'))} nodo(s) del chunk")

            book_progress["completados"].append(i)
            save_progress(progress_path, progress)  # persistido tras cada chunk

    print(f"\n[{nombre}] Finalizado. Nodos nuevos guardados: {total_nodos}")
    if log["colisiones_renombradas"]:
        print(f"  Colisiones de node_id renombradas: {len(log['colisiones_renombradas'])} (ver log)")
    if log["errores"]:
        print(f"  Chunks con error (se reintentan en la proxima corrida): {len(log['errores'])}")
    _cerrar(output_dir, log, uso, t0)


def _cerrar(output_dir, log, uso, t0):
    costo = uso["in"] / 1_000_000 * PRICE_INPUT_PER_MTOK + uso["out"] / 1_000_000 * PRICE_OUTPUT_PER_MTOK
    elapsed = time.time() - t0
    print(f"  Tokens reales: {uso['in']} in / {uso['out']} out | "
          f"Costo real: ${costo:.4f} (intro {MODEL}) | Tiempo: {elapsed:.1f}s")
    log["uso_tokens"] = uso
    log["costo_usd"] = round(costo, 4)
    log_path = output_dir / "_log_ultima_corrida.json"
    log_path.write_text(json.dumps(log, ensure_ascii=False, indent=2), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--grupo", choices=list(GRUPOS), help="Procesar solo este grupo")
    parser.add_argument("--todos", action="store_true", help="Procesar los 4 grupos (general primero)")
    parser.add_argument("--dry-run", action="store_true",
                         help="Solo muestra libros/chunks encontrados, no llama a la API ni escribe nada")
    parser.add_argument("--max-chunks", type=int, default=None,
                         help="Prueba humo: limita el TOTAL de llamadas a la API en esta corrida")
    args = parser.parse_args()

    if not args.grupo and not args.todos:
        parser.error("especifica --grupo <nombre> o --todos")

    client = None
    if not args.dry_run:
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key or api_key == "tu_clave_api_aqui":
            print("Por favor configura tu ANTHROPIC_API_KEY en el archivo .env")
            sys.exit(1)
        import anthropic
        client = anthropic.Anthropic(api_key=api_key)

    presupuesto = {"restantes": args.max_chunks} if args.max_chunks is not None else None

    grupos_a_correr = list(GRUPOS) if args.todos else [args.grupo]
    for grupo in grupos_a_correr:
        if presupuesto is not None and presupuesto["restantes"] <= 0:
            print(f"\nPresupuesto agotado, no se procesa '{grupo}' en esta corrida.")
            continue
        process_grupo(grupo, dry_run=args.dry_run, client=client, presupuesto=presupuesto)


if __name__ == "__main__":
    main()
