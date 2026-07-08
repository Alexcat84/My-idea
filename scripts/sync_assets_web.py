# -*- coding: utf-8 -*-
"""Fase 3.0: copia los assets estaticos que el motor Python ya produce
(grafo compilado, cache de preguntas, clasificacion de familias) a
web/lib/assets/, y escribe un manifest.json con el SHA256 de cada archivo
copiado. web/lib/assets/checksums.test.ts verifica ese manifest contra
los archivos reales en cada build/test -- si el grafo cambia en Python y
alguien olvida re-correr este script, el build de la web falla en vez de
servir un grafo desactualizado en silencio.

Uso: python scripts/sync_assets_web.py
"""
import hashlib
import json
import shutil
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
DEST = BASE / "web" / "lib" / "assets"

ASSETS = {
    "master_graph.json": BASE / "dataset" / "metadata" / "master_graph.json",
    "preguntas_cache.json": BASE / "engine" / "preguntas_cache.json",
    "node_families.json": BASE / "engine" / "node_families.json",
}


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


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
            "sha256": _sha256(destino),
            "bytes": destino.stat().st_size,
            "fuente": str(origen.relative_to(BASE)).replace("\\", "/"),
        }
        print(f"  {nombre}: {manifest[nombre]['bytes']} bytes, sha256={manifest[nombre]['sha256'][:12]}...")

    manifest_path = DEST / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"\nManifest escrito en {manifest_path.relative_to(BASE)}")
    print(f"Assets sincronizados: {list(ASSETS.keys())}")


if __name__ == "__main__":
    main()
