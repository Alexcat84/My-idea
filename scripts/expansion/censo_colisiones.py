# -*- coding: utf-8 -*-
"""Expansión v1.3 — censo de colisiones (RUNBOOK §1). Verifica cada id de un
grupo NUEVO contra el censo completo: dataset/nodos (core+packs integrados),
packs/*/nodos, y los demás grupos nuevos. Colisión → renombra con sufijo de
dominio (lección analisis_competitivo_calidad), actualizando las referencias
internas del propio grupo, y deja registro en <grupo>/metadata (o junto a
nodos/ si el grupo aún vive en books/).

Uso:
  python scripts/expansion/censo_colisiones.py <carpeta_nodos_grupo> <sufijo_dominio> [--aplicar]
Sin --aplicar solo reporta.
"""
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]


def ids_censo(excluir: Path) -> dict[str, str]:
    """id -> origen, de todo el universo salvo la carpeta del grupo."""
    censo = {}
    fuentes = [BASE / "dataset" / "nodos"]
    fuentes += sorted((BASE / "packs").glob("*/nodos"))
    fuentes += sorted((BASE / "books").glob("*/nodos"))
    for carpeta in fuentes:
        if not carpeta.exists() or carpeta.resolve() == excluir.resolve():
            continue
        for f in carpeta.glob("*.json"):
            if f.name.startswith("_"):
                continue
            censo.setdefault(f.stem, str(carpeta.relative_to(BASE)))
    return censo


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    carpeta = Path(sys.argv[1]).resolve()
    sufijo = sys.argv[2]
    aplicar = "--aplicar" in sys.argv

    censo = ids_censo(carpeta)
    propios = sorted(f.stem for f in carpeta.glob("*.json") if not f.name.startswith("_"))
    colisiones = [nid for nid in propios if nid in censo]

    print(f"Grupo: {carpeta} ({len(propios)} nodos) vs censo de {len(censo)} ids")
    print(f"Colisiones: {len(colisiones)}")
    registro = []
    for nid in colisiones:
        nuevo = f"{nid}_{sufijo}"
        k = 2
        while nuevo in censo or (carpeta / f"{nuevo}.json").exists():
            nuevo = f"{nid}_{sufijo}_{k}"
            k += 1
        print(f"  {nid} (ya en {censo[nid]}) -> {nuevo}")
        registro.append({"original": nid, "nuevo": nuevo, "colisiona_con": censo[nid]})
        if aplicar:
            ruta = carpeta / f"{nid}.json"
            d = json.loads(ruta.read_text(encoding="utf-8"))
            d["node_id"] = nuevo
            (carpeta / f"{nuevo}.json").write_text(
                json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            ruta.unlink()

    if aplicar and registro:
        # actualizar referencias internas del grupo a los ids renombrados
        mapa = {r["original"]: r["nuevo"] for r in registro}
        tocados = 0
        for f in carpeta.glob("*.json"):
            if f.name.startswith("_"):
                continue
            d = json.loads(f.read_text(encoding="utf-8"))
            cambio = False
            for campo in ("nodos_previos", "nodos_siguientes"):
                lista = d.get(campo) or []
                nueva = [mapa.get(x, x) for x in lista]
                if nueva != lista:
                    d[campo] = nueva
                    cambio = True
            if cambio:
                f.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                tocados += 1
        print(f"Referencias internas actualizadas en {tocados} nodo(s).")

        meta = carpeta.parent / "metadata"
        meta.mkdir(exist_ok=True)
        (meta / "colisiones_censo_global.json").write_text(
            json.dumps(registro, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Registro: {meta / 'colisiones_censo_global.json'}")


if __name__ == "__main__":
    main()
