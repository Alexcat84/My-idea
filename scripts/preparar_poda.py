#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""preparar_poda.py - El indice de fusion de un pack, para la poda del fundador.

SOLO LECTURA sobre el dataset y los packs: lee el censo, el grafo y la
telemetria, y escribe UN archivo de revision en packs/<pack>/poda/. Ningun nodo
se toca aqui. La consolidacion es el paso siguiente y no arranca sin el visto.

Formato: el mismo de los indices de extraccion que el fundador ya conoce.
Se borran las lineas de lo que NO debe fundirse; lo que quede se consolida.

QUE LLEVA CADA CLUSTER
  - los titulos lado a lado, con su etapa y su id
  - el veredicto textual del consolidador, con el nodo que propone conservar
  - LA TELEMETRIA de cada nodo: si fue visitado y si fue cosechado alguna vez.
    Es el dato que cambia la decision: fundir dos nodos que nadie piso es
    barato; fundir uno por el que paso gente pide mirar cual sobrevive.
  - las tres barandas nuevas marcadas INLINE donde el detector las hallo.

Sobre las barandas: el censo las muestreo con 10 nodos por pack (quality dio
0/10). Para la cirugia eso no sirve, asi que aqui los detectores corren sobre
TODOS los nodos del pack. Son locales y gratis; no hay razon para muestrear.

Uso:
  python scripts/preparar_poda.py --pack quality
"""
import argparse
import json
import os
import sys
from collections import Counter, defaultdict
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from censo_duplicacion import BARANDAS, revisar_barandas  # noqa: E402

ETAPA = {"ideacion": "ideación", "validacion": "validación",
         "planificacion": "planificación", "ejecucion": "ejecución"}
NOMBRE_BARANDA = {
    "dato_local_cableado": "DATO LOCAL",
    "matriz_o_puntaje": "MATRIZ",
    "residuo_corporativo": "CORPORATIVO",
}


def telemetria_por_nodo():
    """visitas y cosechas por node_id. Paginado: el select simple corta en
    1.000 filas sin avisar, y un conteo truncado aqui decidiria mal una poda."""
    from dotenv import load_dotenv
    load_dotenv(BASE / ".env")
    from supabase import create_client
    cli = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_SERVICE_ROLE_KEY"))
    filas, off = [], 0
    while True:
        r = cli.table("project_nodes").select("node_id, tipo").range(off, off + 999).execute()
        filas += r.data or []
        if not r.data or len(r.data) < 1000:
            break
        off += 1000
    vis = Counter(f["node_id"] for f in filas if f.get("node_id"))
    cos = Counter(f["node_id"] for f in filas
                  if f.get("node_id") and f.get("tipo") == "cosechado")
    return vis, cos, len(filas)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pack", required=True)
    args = ap.parse_args()
    pack = args.pack

    censo = json.loads((BASE / "docs" / "_censo_duplicacion.json").read_text(encoding="utf-8"))
    if pack not in censo["packs"]:
        print(f"ERROR: {pack} no esta en el censo")
        sys.exit(2)
    datos = censo["packs"][pack]
    grafo = json.loads(
        (BASE / "dataset" / "metadata" / "master_graph.json").read_text(encoding="utf-8"))["nodos"]

    clusters, ver, peor = datos["_clusters"], datos.get("veredictos", {}), datos.get("_peor", {})
    confirmados = [(i, c) for i, c in enumerate(clusters) if ver.get(str(i), {}).get("fundir")]
    confirmados.sort(key=lambda t: (-len(t[1]), -float(peor.get(str(t[0]), 0))))

    vis, cos, filas = telemetria_por_nodo()
    print(f"  telemetria: {filas} filas de project_nodes")

    # Barandas sobre TODOS los nodos del pack, no sobre una muestra de 10.
    del_pack = [nid for nid, n in grafo.items() if n.get("dominio") == pack]
    hall = {nid: revisar_barandas(grafo[nid]) for nid in del_pack}
    hall = {k: v for k, v in hall.items() if v}
    por_baranda = Counter(h["baranda"] for v in hall.values() for h in v)

    # LA REGLA DEL SUPERVIVIENTE (adjudicada por fundador+auditor, 2026-08-07).
    # El consolidador juzga por CONTENIDO y no ve la telemetria. Cuando
    # discrepan manda la telemetria: la continuidad del id mas pisado es la que
    # menos fricción crea con project_nodes, que es historia de gente real. El
    # contenido del propuesto no se pierde: se rescata DENTRO del superviviente.
    # Sin historia en ningun nodo del cluster, manda el propuesto.
    def superviviente(c, v):
        con_historia = [n for n in c if vis.get(n)]
        if con_historia:
            elegido = max(con_historia, key=lambda n: (vis.get(n, 0), cos.get(n, 0)))
            return elegido, "telemetría"
        for n in c:
            if grafo[n].get("titulo_concepto") == v.get("quedaria"):
                return n, "propuesto"
        return c[0], "primero (sin historia y sin propuesta legible)"

    md = [f"# Índice de fusión de {pack}", "",
          f"{len(confirmados)} clusters propuestos, {sum(len(c) for _, c in confirmados)} nodos "
          f"de los {len(del_pack)} del pack.", "",
          "**Borra las líneas de lo que NO debe fundirse. Lo que quede se consolida.**", "",
          "## La regla del superviviente (vigente)", "",
          "**Sobrevive el nodo con más historia.** La telemetría es la voz de los "
          "caminos reales, y conservar el id más pisado es lo que menos fricción crea "
          "con `project_nodes`. El contenido del que proponía el consolidador **no se "
          "pierde**: se rescata dentro del superviviente.", "",
          "Si ningún nodo del cluster tiene historia, manda el propuesto del "
          "consolidador. **Tu ojo es la única excepción**: donde discrepes, tacha y "
          "escribe cuál debe quedarse.", "",
          "`visto N` = veces que apareció en el recorrido de alguien. "
          "`cosechado N` = veces que se llevó a un plan. Ningún nodo se borra: los "
          "absorbidos salen de la selección y su id sigue existiendo.", ""]

    for orden, (i, c) in enumerate(confirmados, start=1):
        v = ver[str(i)]
        sim = float(peor.get(str(i), 0))
        tocados = sum(1 for n in c if vis.get(n))
        gana, motivo = superviviente(c, v)
        md.append(f"## {orden}. {len(c)} nodos · similitud {sim:.3f}"
                  + (f" · **{tocados} con historia**" if tocados else " · sin historia"))
        md.append("")
        md.append(f"> {v.get('por_que','')}")
        md.append("")
        md.append(f"**Sobrevive: `{gana}`** ({motivo})")
        md.append("")
        for nid in c:
            n = grafo[nid]
            marcas = []
            if vis.get(nid):
                marcas.append(f"visto {vis[nid]}")
            if cos.get(nid):
                marcas.append(f"cosechado {cos[nid]}")
            for h in hall.get(nid, []):
                marcas.append(f"**{NOMBRE_BARANDA[h['baranda']]}**")
            sufijo = f"  ·  {' · '.join(marcas)}" if marcas else ""
            marca = ""
            if nid == gana:
                marca = "**← SOBREVIVE**"
            elif n.get("titulo_concepto") == v.get("quedaria"):
                marca = "*(el consolidador proponía este; su contenido se rescata)*"
            md.append(f"- [{ETAPA.get(n.get('fase_proyecto'), '?')}] "
                      f"**{n.get('titulo_concepto')}** `{nid}`{sufijo} {marca}")
            for h in hall.get(nid, []):
                md.append(f"    - {NOMBRE_BARANDA[h['baranda']]}: {h['cita'][:170]}")
        md.append("")

    md += ["---", "", "## Las tres barandas nuevas en todo el pack", "",
           f"Los detectores corrieron sobre los {len(del_pack)} nodos, no sobre una muestra: "
           f"son locales y gratis. {len(hall)} nodos dieron algún hallazgo.", ""]
    for b, n in por_baranda.most_common():
        md.append(f"- **{NOMBRE_BARANDA[b]}**: {n} nodos")
    md.append("")
    fuera = sorted(k for k in hall if not any(k in c for _, c in confirmados))
    if fuera:
        md += ["", f"### {len(fuera)} nodos con hallazgo que NO están en ningún cluster", "",
               "Estos no los toca la fusión: son otra decisión, y va aparte.", ""]
        for nid in fuera[:40]:
            etiquetas = " · ".join(NOMBRE_BARANDA[h["baranda"]] for h in hall[nid])
            md.append(f"- **{grafo[nid].get('titulo_concepto')}** `{nid}` — {etiquetas}")
        if len(fuera) > 40:
            md.append(f"- … y {len(fuera) - 40} más (en el JSON)")

    salida = BASE / "packs" / pack / "poda"
    salida.mkdir(parents=True, exist_ok=True)
    (salida / f"INDICE_DE_FUSION_{pack}.md").write_text("\n".join(md), encoding="utf-8")
    (salida / f"_poda_{pack}.json").write_text(json.dumps({
        "regla_superviviente": "el nodo con mas historia; sin historia, el propuesto",
        "pack": pack, "umbral": censo["umbral"],
        "clusters": [{"orden": o, "indice": i, "nodos": c,
                      "similitud": float(peor.get(str(i), 0)),
                      "por_que": ver[str(i)].get("por_que"),
                      "quedaria": ver[str(i)].get("quedaria"),
                      "sobrevive": superviviente(c, ver[str(i)])[0],
                      "sobrevive_por": superviviente(c, ver[str(i)])[1],
                      "telemetria": {n: {"visto": vis.get(n, 0), "cosechado": cos.get(n, 0)} for n in c}}
                     for o, (i, c) in enumerate(confirmados, start=1)],
        "barandas": {k: v for k, v in hall.items()},
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"  {len(confirmados)} clusters, {sum(len(c) for _, c in confirmados)} nodos")
    print(f"  barandas: {len(hall)} nodos con hallazgo {dict(por_baranda)}")
    print(f"  -> {salida / f'INDICE_DE_FUSION_{pack}.md'}")


if __name__ == "__main__":
    main()
