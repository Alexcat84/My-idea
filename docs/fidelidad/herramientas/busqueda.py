# -*- coding: utf-8 -*-
"""Recuperacion de fragmentos por paso, y la medida que elige el metodo.

Metodo A (lexico solo): BM25 propio con el titulo del nodo y el paso tal
cual (espanol) contra el libro (ingles). Solo casa por cognados.
Metodo B (consultas traducidas + lexico): el modelo escribe, a ciegas y por
lotes barajados, 3 consultas en ingles por paso; BM25 por consulta y fusion
de rankings (RRF), mas la consulta del titulo del nodo con medio peso.
Metodo C (hibrido): B mas el ranking de A fundido como una consulta mas.
Metodo D (hibrido por turnos): las mismas cinco listas de C, tomadas por
turno rotatorio (el primero de cada una, luego el segundo...) en vez de RRF.
Voyage queda SIN MEDIR: no hay clave en esta sesion.

La vara (oro):
  - cada sintetico: las lineas del pasaje del que se genero;
  - el contrario conocido (prevalencia_omisiones, paso 2): L1943 y L2170;
  - 40 pasos reales al azar: Opus lee el libro ENTERO numerado y dice que
    lineas tratan el mismo asunto (una sola llamada, a ciegas del metodo).

uso: python busqueda.py traducir | oro | medir | recuperar <metodo> <k>
"""
import json, os, random, sys
from concurrent.futures import ThreadPoolExecutor
import comun as C

LOTE_TRAD = 12

SIS_TRAD = ("Eres un bibliotecario que prepara busquedas en un libro en ingles de ciencia de la seguridad "
            "(James Reason, 1997). Respondes SOLO con JSON valido.")

def _items():
    return C.lee_jsonl(os.path.join(C.PIL, f"items_mezclados_i{C.INTENTO}.jsonl"))

def traducir():
    ruta = os.path.join(C.PIL, f"consultas_traducidas_i{C.INTENTO}.json")
    previas = json.load(open(ruta, encoding="utf-8")) if os.path.exists(ruta) else {}
    items = [it for it in _items() if it["id"] not in previas]
    lotes = [items[i:i + LOTE_TRAD] for i in range(0, len(items), LOTE_TRAD)]
    def uno(ix_lote):
        ix, lote = ix_lote
        cuerpo = "\n\n".join(f"ID {it['id']}\nNodo: {it['titulo']}\nContexto: {it['resumen'][:400]}\nPaso: {it['paso']}" for it in lote)
        prompt = f"""Para cada paso (en espanol) escribe 3 consultas de busqueda EN INGLES para encontrar en el libro los
pasajes que tratan ese mismo asunto. Usa el vocabulario que usaria el propio libro (terminos tecnicos, sinonimos,
nombres propios, siglas). Cada consulta de 4 a 12 palabras. Ademas, una consulta "nodo" con el tema del nodo.

{cuerpo}

Responde SOLO con un array JSON: [{{"id": "...", "consultas": ["...", "...", "..."], "nodo": "..."}}]"""
        datos, _ = C.llama("traduccion" + ("" if C.INTENTO == "1" else f"_i{C.INTENTO}"), f"lote_{ix:03d}", SIS_TRAD, prompt)
        return datos
    out = dict(previas)
    with ThreadPoolExecutor(C.MAX_PAR) as ex:
        for datos in ex.map(uno, enumerate(lotes)):
            for d in datos: out[d["id"]] = d
    faltan = [it["id"] for it in _items() if it["id"] not in out]
    assert not faltan, faltan
    C.escribe_json(ruta, out)
    print(len(out), "items con consultas")

def libro_numerado():
    L = C.lineas_libro()
    return "\n".join(f"L{i+1}: {t.strip()}" for i, t in enumerate(L) if t.strip() and t.strip() != "●")

def oro():
    items = _items()
    clave = json.load(open(os.path.join(C.PRU, f"CLAVE_CIEGA_i{C.INTENTO}.json"), encoding="utf-8"))["clave"]
    reales = [it for it in items if clave[it["id"]]["tipo"] == "real"
              and not (clave[it["id"]]["nodo"] == "prevalencia_omisiones" and clave[it["id"]]["paso_idx"] == 1)]
    muestra = random.Random(40).sample(reales, 40)
    cuerpo = "\n".join(f"ID {it['id']} | Nodo: {it['titulo']} | Paso: {it['paso']}" for it in muestra)
    prompt = f"""Abajo esta el libro entero de James Reason, con cada parrafo numerado (Lnnn). Despues vienen 40 pasos
de un catalogo en espanol extraido de ese libro. Para cada paso, di en que lineas trata el libro ESE MISMO asunto:
las que habria que leer para juzgar si el libro apoya o contradice el paso. De 1 a 6 lineas, la mas directa primero.
Si el libro no trata el asunto, lista vacia.

=== LIBRO ===
{libro_numerado()}
=== FIN DEL LIBRO ===

=== PASOS ===
{cuerpo}

Responde SOLO con un array JSON: [{{"id": "...", "lineas": [n, ...]}}]"""
    datos, coste = C.llama("oro", "muestra40", "Eres un lector experto y minucioso. Respondes SOLO con JSON valido.", prompt, timeout=3000)
    C.escribe_json(os.path.join(C.PIL, f"oro_busqueda_i{C.INTENTO}.json"), {d["id"]: d["lineas"] for d in datos})
    print(len(datos), coste)

# ── RECUPERACION ────────────────────────────────────────────────────────────

_cache = {}
def indice():
    if "bm" not in _cache:
        frags = C.lee_jsonl(os.path.join(C.WORK, "fragmentos.jsonl"))
        _cache["frags"] = frags
        _cache["bm"] = C.BM25([f["texto"] for f in frags])
    return _cache["frags"], _cache["bm"]

def recuperar_item(it, metodo, k, consultas=None):
    frags, bm = indice()
    if metodo == "A":
        r, _ = bm.ranking(it["titulo"] + " " + it["paso"])
        return [frags[i]["id"] for i in r[:k]]
    q = consultas[it["id"]]
    rks = [bm.ranking(c)[0] for c in q["consultas"]] + [bm.ranking(q["nodo"])[0]]
    pesos = [1.0] * len(q["consultas"]) + [0.5]
    if metodo in ("C", "D"):  # B mas el ranking lexico del texto en espanol (A) como una consulta mas
        rks.append(bm.ranking(it["titulo"] + " " + it["paso"])[0]); pesos.append(1.0)
    if metodo == "D":  # turno rotatorio: el primero de cada ranking, luego el segundo de cada uno...
        r, vistos = [], set()
        for pos_ in range(200):
            for rk in rks:
                if rk[pos_] not in vistos:
                    vistos.add(rk[pos_]); r.append(rk[pos_])
            if len(r) >= k: break
        return [frags[i]["id"] for i in r[:k]]
    r = C.rrf(rks, pesos)
    return [frags[i]["id"] for i in r[:k]]

def vara():
    items = _items()
    clave = json.load(open(os.path.join(C.PRU, f"CLAVE_CIEGA_i{C.INTENTO}.json"), encoding="utf-8"))["clave"]
    oro_ = json.load(open(os.path.join(C.PIL, f"oro_busqueda_i{C.INTENTO}.json"), encoding="utf-8"))
    v = {}
    for it in items:
        o = clave[it["id"]]
        if o["tipo"] == "sintetico":
            v[it["id"]] = ("sintetico" if o.get("clase", "CONTRARIO") == "CONTRARIO" else "anadido", o["lineas"])
        elif o["nodo"] == "prevalencia_omisiones" and o["paso_idx"] == 1:
            v[it["id"]] = ("conocido", [1943, 2170])
        elif it["id"] in oro_ and oro_[it["id"]]:
            v[it["id"]] = ("real", oro_[it["id"]])
    return items, v

def medir():
    frags, _ = indice()
    pos = {f["id"]: (f["l_ini"], f["l_fin"]) for f in frags}
    items, v = vara()
    cons = json.load(open(os.path.join(C.PIL, f"consultas_traducidas_i{C.INTENTO}.json"), encoding="utf-8"))
    byid = {it["id"]: it for it in items}
    ks = [3, 5, 8, 10, 12, 15, 20]
    tabla = {}
    for metodo in ("A", "B", "C", "D"):
        for grupo in ("sintetico", "anadido", "conocido", "real"):
            ids = [i for i, (g, _) in v.items() if g == grupo]
            fila = {}
            for k in ks:
                alguno = todas = 0
                for i in ids:
                    got = recuperar_item(byid[i], metodo, k, cons)
                    cub = {g for g in v[i][1] for f in got if pos[f][0] <= g <= pos[f][1]}
                    alguno += bool(cub); todas += cub == set(v[i][1])
                fila[k] = {"alguna_linea": f"{alguno}/{len(ids)}", "todas_las_lineas": f"{todas}/{len(ids)}"}
            tabla[f"{metodo}:{grupo}"] = fila
    C.escribe_json(os.path.join(C.PIL, f"MEDIDA_BUSQUEDA_i{C.INTENTO}.json"), tabla)
    for kk, fila in tabla.items():
        print(kk, {k: f["alguna_linea"] + " (" + f["todas_las_lineas"] + ")" for k, f in fila.items()})

if __name__ == "__main__":
    {"traducir": traducir, "oro": oro, "medir": medir}[sys.argv[1]]()
