# -*- coding: utf-8 -*-
"""Fase 3.0: copia los assets estaticos que el motor Python ya produce
(grafo compilado, cache de preguntas, clasificacion de familias) a
web/lib/assets/, y escribe un manifest.json con el SHA256 de cada archivo
copiado. web/lib/assets/checksums.test.ts verifica ese manifest contra
los archivos reales en cada build/test -- si el grafo cambia en Python y
alguien olvida re-correr este script, el build de la web falla en vez de
servir un grafo desactualizado en silencio.

Ademas exporta los SYSTEM_* prompts de prototipo_motor.py a
web/lib/assets/prompts.json (uno por nombre, valor exacto de la constante
Python, no retipeado a mano) para que web/lib/prompts.ts los re-exporte
sin riesgo de una transcripcion distinta byte a byte -- de esa identidad
depende que el prompt caching de Anthropic seccione el prefijo igual que
en Python (umbrales ya calibrados: 4096 tokens Haiku, 2048 Sonnet).

Uso: python scripts/sync_assets_web.py
"""
import hashlib
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
DEST = BASE / "web" / "lib" / "assets"

ASSETS = {
    "master_graph.json": BASE / "dataset" / "metadata" / "master_graph.json",
    "preguntas_cache.json": BASE / "engine" / "preguntas_cache.json",
    "node_families.json": BASE / "engine" / "node_families.json",
    "entry_seeds.json": BASE / "dataset" / "metadata" / "entry_seeds.json",
    # Las listas curadas de los avisos de la tarjeta (decision del fundador del 26 sep 2026,
    # saneamiento tanda 1; docs/POLITICA_MARCO_PAIS.md): web/lib/engine/avisos.ts las lee.
    "jurisdiccion.json": BASE / "dataset" / "metadata" / "jurisdiccion.json",
    "vigencia.json": BASE / "dataset" / "metadata" / "vigencia.json",
}

PROMPTS_A_EXPORTAR = [
    "SYSTEM_CLASIFICACION",
    "SYSTEM_PUERTA_AVANZADA",
    "SYSTEM_INTERPRETE_MULTI",
    "SYSTEM_PROFUNDIZAR",
    "SYSTEM_PREGUNTA_DIRIGIDA",
    "SYSTEM_PLAN",
    "SYSTEM_ESTADO_VIVO",
    "SYSTEM_JUEZ_SESION",
    "SYSTEM_ORGANIZADOR",
    "SYSTEM_REPORTE",
    "SYSTEM_CLASIFICAR_OFERTA",
    "SYSTEM_DIAGNOSTICO_MUNDO",
    "SYSTEM_CAMINOS",
]


def _sha256_bytes(data: bytes) -> str:
    h = hashlib.sha256()
    h.update(data)
    return h.hexdigest()


def _sha256_file(path: Path) -> str:
    return _sha256_bytes(path.read_bytes())


# NADA INTERNO LLEGA AL NAVEGADOR (decision del fundador del 27 sep 2026, punto 2; REGLA ESTRICTA del 26 sep):
# lo que se copia a web/ es la VISTA WEB de cada asset, sin la fuente de los nodos, sus fuentes internas, sus
# correcciones (con sus citas) ni la procedencia de sus fusiones. Todo eso vive solo en dataset/.
# La guarda es web/lib/assets/sinInternos.test.ts.
CLAVES_INTERNAS_NODO = ("fuente", "fuentes_internas", "correcciones", "merged_originals")


def _vista_web(nombre: str, datos):
    if nombre == "master_graph.json":
        for n in datos["nodos"].values():
            for k in CLAVES_INTERNAS_NODO:
                n.pop(k, None)
        return datos
    if nombre == "vigencia.json":
        # La web solo necesita el ANO del aviso; el libro, su fichero y su frase se quedan en dataset/.
        libros = datos["libros"]
        return {"_nota": "Vista web de dataset/metadata/vigencia.json: el ano del aviso de cada nodo, sin el libro.",
                "nodos": {k: {"anio": libros[v["fuente"]]["anio"]} for k, v in datos["nodos"].items()}}
    if nombre == "jurisdiccion.json":
        return {"_nota": "Vista web de dataset/metadata/jurisdiccion.json: pais y clase de cada nodo, sin su motivo.",
                "nodos": {k: {"pais": v["pais"], "clase": v["clase"]} for k, v in datos["nodos"].items()}}
    return datos


def _exportar_prompts():
    """write_bytes en vez de write_text: en Windows, write_text traduce
    '\\n' a '\\r\\n' al escribir (modo texto), lo que produciria un
    archivo en disco con mas bytes que el string original -- y el
    checksum quedaria calculado sobre datos que nunca se escribieron.
    write_bytes no traduce nada; el checksum se calcula sobre los MISMOS
    bytes exactos que terminan en disco."""
    sys.path.insert(0, str(BASE / "engine"))
    import prototipo_motor as pm

    prompts = {nombre: getattr(pm, nombre) for nombre in PROMPTS_A_EXPORTAR}
    destino = DEST / "prompts.json"
    contenido_bytes = (json.dumps(prompts, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    destino.write_bytes(contenido_bytes)
    return destino, contenido_bytes


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    manifest = {}
    for nombre, origen in ASSETS.items():
        if not origen.exists():
            print(f"ERROR: no existe el asset fuente: {origen}")
            raise SystemExit(1)
        destino = DEST / nombre
        # Mismo patron que _exportar_prompts: normalizar EOL a LF y
        # escribir con write_bytes, hasheando LOS MISMOS bytes escritos.
        # (Causa raiz del desync: CRLF de Windows hasheado aqui, LF en git.)
        contenido = origen.read_bytes().replace(b"\r\n", b"\n")
        if nombre in ("master_graph.json", "vigencia.json", "jurisdiccion.json"):
            vista = _vista_web(nombre, json.loads(contenido.decode("utf-8")))
            contenido = (json.dumps(vista, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        destino.write_bytes(contenido)
        manifest[nombre] = {
            "sha256": _sha256_bytes(contenido),
            "bytes": len(contenido),
            "origen": str(origen.relative_to(BASE)).replace("\\", "/"),
        }
        print(f"  {nombre}: {manifest[nombre]['bytes']} bytes, sha256={manifest[nombre]['sha256'][:12]}...")

    destino_prompts, contenido_prompts = _exportar_prompts()
    manifest["prompts.json"] = {
        "sha256": _sha256_bytes(contenido_prompts),
        "bytes": len(contenido_prompts),
        "origen": "engine/prototipo_motor.py (SYSTEM_* constants)",
    }
    print(f"  prompts.json: {manifest['prompts.json']['bytes']} bytes, "
          f"sha256={manifest['prompts.json']['sha256'][:12]}... ({len(PROMPTS_A_EXPORTAR)} prompts)")

    # semantic_index.json no lo genera este script (lo genera
    # build_semantic_index_voyage.py, aparte, porque cuesta dinero real de
    # API y no deberia correr en cada sync) -- pero si ya existe, se suma
    # al mismo manifest para que checksums.test.ts tambien lo vigile.
    semantic_index_path = DEST / "semantic_index.json"
    if semantic_index_path.exists():
        contenido_si = semantic_index_path.read_bytes().replace(b"\r\n", b"\n")
        semantic_index_path.write_bytes(contenido_si)
        manifest["semantic_index.json"] = {
            "sha256": _sha256_bytes(contenido_si),
            "bytes": len(contenido_si),
            "origen": "scripts/build_semantic_index_voyage.py (Voyage AI voyage-4-lite)",
        }
        print(f"  semantic_index.json: {manifest['semantic_index.json']['bytes']} bytes, "
              f"sha256={manifest['semantic_index.json']['sha256'][:12]}...")

    manifest_path = DEST / "manifest.json"
    manifest_path.write_bytes((json.dumps(manifest, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))
    print(f"\nManifest escrito en {manifest_path.relative_to(BASE)}")
    print(f"Assets sincronizados: {list(manifest.keys())}")


if __name__ == "__main__":
    main()
