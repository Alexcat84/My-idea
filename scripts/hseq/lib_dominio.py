"""Fase P1-HSEQ: utilidades compartidas para el saneamiento por dominio.

Los tres dominios viven en "packs/<clave_dominio>/nodos/" y JAMAS se
mezclan entre si ni con dataset/nodos (el core). Todo script de esta fase
importa de aqui para garantizar el mismo mapeo y las mismas reglas.
"""
from __future__ import annotations
import json
import os
import re
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
BASE = RAIZ / "packs"

# carpeta -> clave de dominio (la que llevan los nodos en su campo `dominio`)
CATEGORIAS = {
    "environmental": "environmental",
    "health_safety": "health_safety",
    "quality": "quality",
}

# Expansión v1.3: los pasos pueden apuntarse a packs NUEVOS sin re-tocar los
# HSEQ ya integrados (que quedan congelados). HSEQ_CATEGORIAS acepta una
# lista separada por comas de carpetas bajo packs/.
_cats_env = os.environ.get("HSEQ_CATEGORIAS", "").strip()
if _cats_env:
    CATEGORIAS = {c.strip(): c.strip() for c in _cats_env.split(",") if c.strip()}


def dir_nodos(categoria: str) -> Path:
    return BASE / categoria / "nodos"


def dir_metadata(categoria: str) -> Path:
    d = BASE / categoria / "metadata"
    d.mkdir(parents=True, exist_ok=True)
    return d


def cargar_dominio(categoria: str) -> dict[str, dict]:
    """Carga todos los nodos JSON de un dominio como {node_id: data}."""
    nodos: dict[str, dict] = {}
    for f in sorted(dir_nodos(categoria).glob("*.json")):
        with open(f, encoding="utf-8") as fh:
            nodos[f.stem] = json.load(fh)
    return nodos


def guardar_nodo(categoria: str, node_id: str, data: dict) -> None:
    data["node_id"] = node_id
    ruta = dir_nodos(categoria) / f"{node_id}.json"
    with open(ruta, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
        fh.write("\n")


def borrar_nodo(categoria: str, node_id: str) -> None:
    (dir_nodos(categoria) / f"{node_id}.json").unlink()


def a_ascii(texto: str) -> str:
    """Misma regla del core: NFKD, fuera diacriticos, [a-z0-9_], colapsado."""
    plano = unicodedata.normalize("NFKD", texto)
    plano = "".join(c for c in plano if not unicodedata.combining(c))
    plano = plano.lower()
    plano = re.sub(r"[^a-z0-9_]+", "_", plano)
    return re.sub(r"_+", "_", plano).strip("_")


def norm_titulo(titulo: str) -> str:
    """Normalizacion para comparar titulos en dedup (ASCII, sin parentesis)."""
    t = re.sub(r"\([^)]*\)", " ", titulo or "")
    return a_ascii(t)


def refs(data: dict) -> list[tuple[str, int, str]]:
    """Itera (campo, indice, ref) sobre nodos_previos y nodos_siguientes."""
    out = []
    for campo in ("nodos_previos", "nodos_siguientes"):
        for i, r in enumerate(data.get(campo) or []):
            out.append((campo, i, r))
    return out


def escribir_json(ruta: Path, obj) -> None:
    with open(ruta, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=2)
        fh.write("\n")


def similitud(a: str, b: str) -> float:
    """rapidfuzz si esta instalado (como en el core); difflib como respaldo."""
    try:
        from rapidfuzz import fuzz  # type: ignore
        return fuzz.token_sort_ratio(a, b) / 100.0
    except ImportError:
        from difflib import SequenceMatcher
        return SequenceMatcher(None, a, b).ratio()
