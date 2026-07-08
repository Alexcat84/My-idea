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
import shutil
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
DEST = BASE / "web" / "lib" / "assets"

ASSETS = {
    "master_graph.json": BASE / "dataset" / "metadata" / "master_graph.json",
    "preguntas_cache.json": BASE / "engine" / "preguntas_cache.json",
    "node_families.json": BASE / "engine" / "node_families.json",
}

PROMPTS_A_EXPORTAR = [
    "SYSTEM_CLASIFICACION",
    "SYSTEM_PUERTA_AVANZADA",
    "SYSTEM_INTERPRETE_MULTI",
    "SYSTEM_PROFUNDIZAR",
    "SYSTEM_PREGUNTA_DIRIGIDA",
    "SYSTEM_PLAN",
    "SYSTEM_ESTADO_VIVO",
    "SYSTEM_ORGANIZADOR",
    "SYSTEM_REPORTE",
    "SYSTEM_CLASIFICAR_OFERTA",
]


def _sha256_bytes(data: bytes) -> str:
    h = hashlib.sha256()
    h.update(data)
    return h.hexdigest()


def _sha256_file(path: Path) -> str:
    return _sha256_bytes(path.read_bytes())


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
        shutil.copyfile(origen, destino)
        manifest[nombre] = {
            "sha256": _sha256_file(destino),
            "bytes": destino.stat().st_size,
            "fuente": str(origen.relative_to(BASE)).replace("\\", "/"),
        }
        print(f"  {nombre}: {manifest[nombre]['bytes']} bytes, sha256={manifest[nombre]['sha256'][:12]}...")

    destino_prompts, contenido_prompts = _exportar_prompts()
    manifest["prompts.json"] = {
        "sha256": _sha256_bytes(contenido_prompts),
        "bytes": len(contenido_prompts),
        "fuente": "engine/prototipo_motor.py (SYSTEM_* constants)",
    }
    print(f"  prompts.json: {manifest['prompts.json']['bytes']} bytes, "
          f"sha256={manifest['prompts.json']['sha256'][:12]}... ({len(PROMPTS_A_EXPORTAR)} prompts)")

    manifest_path = DEST / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"\nManifest escrito en {manifest_path.relative_to(BASE)}")
    print(f"Assets sincronizados: {list(ASSETS.keys())} + prompts.json")


if __name__ == "__main__":
    main()
