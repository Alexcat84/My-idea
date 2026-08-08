#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""censo_duplicacion.py - Mide el catalogo entero contra la vara VIGENTE.

ESTRICTAMENTE DE SOLO LECTURA. No escribe en dataset/, ni en packs/, ni en el
grafo, ni toca produccion. Lo unico que produce es un reporte .md y su JSON de
respaldo, ambos en docs/. Ninguna funcion de este archivo abre un archivo del
dataset en modo escritura, y hay un test que lo custodia.

QUE MIDE Y CONTRA QUE
Compras (46) y entrega (47) son el GRUPO DE CONTROL: los unicos nodos nacidos
del SOP vigente, con su consolidacion y sus cuatro barandas. Todo lo demas es
candidato a optimizacion, incluido risk_management, que fue el limpio de su
generacion pero con el SOP de la v1.4, no el de hoy.

EL INSTRUMENTO
La etapa de fusion de extraer_mundo, en modo SOLO-PROPUESTA. Adaptada aqui
porque alli juzga CONCEPTOS de indice (titulo + una linea) y estos son NODOS ya
nacidos (titulo + resumen + pasos). El original no se toca.

Dos pasos, y el orden importa:

  1. CANDIDATOS, local y gratis: similitud coseno sobre los embeddings Voyage
     que ya existen (web/lib/assets/semantic_index.json, 3.835 nodos, 512
     dimensiones). Solo INTRA-pack: comparar entre dominios no tiene sentido,
     un mundo puede repetir un concepto de otro a proposito.

  2. VEREDICTO, el consolidador: cada cluster candidato se le pasa al modelo
     con la misma pregunta que en la extraccion (esto es el MISMO concepto con
     dos nombres, o son dos que llevan a acciones distintas). Sin el veredicto,
     el numero miente: a 0.90 el propio control produce pares que NO son
     duplicados (dos formas de proteger un paquete se parecen mucho y no son la
     misma).

EL UMBRAL, y por que ese
0.90 de coseno, IDENTICO para los diez packs. Calibrado contra el control: a
0.90 compras da 0 pares y entrega 6; a 0.85 dan 25 y 32, que ya es ruido. El
control es la linea base de lo que la vara considera limpio, asi que el umbral
se elige donde el control casi calla.

Uso:
  python scripts/censo_duplicacion.py --dry-run     # cuenta y estima, no llama
  python scripts/censo_duplicacion.py               # censo completo
  python scripts/censo_duplicacion.py --sin-api     # solo la parte local
"""
import argparse
import json
import os
import random
import re
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

UMBRAL = 0.90
SEMILLA_MUESTREO = 20260807  # fija: el muestreo "al azar" tiene que repetirse
NODOS_POR_MUESTRA = 10
MODEL = "claude-sonnet-5"
TECHOS = (16000, 32000, 64000)
PRECIO_IN_MTOK = 2.00
PRECIO_OUT_MTOK = 10.00

# Los diez, con su era del pipeline. La era es la que explica los numeros: no
# es lo mismo un pack troceado a granel que uno curado concepto a concepto.
ERAS = {
    "core": ("a granel puro", "scripts/pipeline.py, la biblioteca original"),
    "quality": ("a granel puro", "P1-HSEQ, un envio por trozo de libro"),
    "health_safety": ("a granel puro", "P1-HSEQ, un envio por trozo de libro"),
    "environmental": ("a granel puro", "P1-HSEQ, un envio por trozo de libro"),
    "franquicias": ("intermedia", "pipeline_libros, prompt aislado por grupo"),
    "exportacion": ("intermedia", "pipeline_libros, prompt aislado por grupo"),
    "seguridad_digital": ("intermedia", "pipeline_libros, prompt aislado por grupo"),
    "risk_management": ("SOP v1.4", "indice curado a mano, sin consolidador"),
    "compras": ("vara vigente", "CONTROL: indice + consolidador + 4 barandas"),
    "entrega": ("vara vigente", "CONTROL: indice + consolidador + 4 barandas"),
}
CONTROL = ("compras", "entrega")


# ---------------------------------------------------------------------------
# Carga (solo lectura)
# ---------------------------------------------------------------------------
def cargar_grafo():
    with open(BASE / "dataset" / "metadata" / "master_graph.json", encoding="utf-8") as f:
        return json.load(f)["nodos"]


def cargar_embeddings():
    import numpy as np
    with open(BASE / "web" / "lib" / "assets" / "semantic_index.json", encoding="utf-8") as f:
        idx = json.load(f)
    E = np.array(idx["embeddings"], dtype=np.float32)
    E /= np.linalg.norm(E, axis=1, keepdims=True)
    return idx["ids"], E


# ---------------------------------------------------------------------------
# Paso 1: clusters candidatos (local)
# ---------------------------------------------------------------------------
def clusters_candidatos(ids_pack, pos, E, umbral=UMBRAL):
    """Union-find sobre los pares por encima del umbral. Solo intra-pack."""
    import numpy as np
    sub = [pos[x] for x in ids_pack]
    S = E[sub] @ E[sub].T
    np.fill_diagonal(S, -1.0)
    padre = list(range(len(sub)))

    def raiz(i):
        while padre[i] != i:
            padre[i] = padre[padre[i]]
            i = padre[i]
        return i

    pares = []
    for i, j in zip(*np.where(np.triu(S, 1) >= umbral)):
        pares.append((ids_pack[i], ids_pack[j], float(S[i, j])))
        ri, rj = raiz(i), raiz(j)
        if ri != rj:
            padre[ri] = rj

    grupos = defaultdict(list)
    for i in range(len(sub)):
        grupos[raiz(i)].append(ids_pack[i])
    clusters = [sorted(v) for v in grupos.values() if len(v) > 1]
    # El peor par de cada cluster, para ordenar la muestra por gravedad.
    peor = {}
    for a, b, s in pares:
        for c_i, c in enumerate(clusters):
            if a in c and b in c:
                peor[c_i] = max(peor.get(c_i, 0), s)
    return clusters, pares, peor


# ---------------------------------------------------------------------------
# Paso 2: el consolidador da su veredicto (API, solo propuesta)
# ---------------------------------------------------------------------------
PROMPT_VEREDICTO = """Eres un editor de un grafo de conocimiento para emprendedores.

Recibes GRUPOS de nodos que un indice semantico marco como muy parecidos. Para
cada grupo dices si son EL MISMO concepto con dos nombres (habria que fundirlos)
o si son conceptos DISTINTOS que solo se parecen.

La pregunta que decide: si llevan a ACCIONES DISTINTAS, son dos. Si el
emprendedor haria lo mismo leyendo cualquiera de los dos, es uno.

No propongas fundir nada que cambie lo que la persona hace. Ante la duda, di
que son distintos: fundir de mas borra conocimiento, fundir de menos solo deja
un catalogo largo.

Devuelve EXCLUSIVAMENTE un arreglo JSON, sin markdown. Un objeto por grupo:
{
  "grupo": 3,
  "fundir": true,
  "por_que": "Una linea: por que son el mismo o por que no",
  "quedaria": "El titulo del nodo que deberia sobrevivir (si fundir es true)"
}"""


def _texto_de(r):
    for b in r.content:
        if getattr(b, "type", "") == "text":
            return b.text
    return ""


def _arreglo(t):
    t = t.strip()
    for v in ("```json", "```"):
        if t.startswith(v):
            t = t[len(v):]
    if t.endswith("```"):
        t = t[:-3]
    i, j = t.find("["), t.rfind("]")
    return t[i:j + 1] if i != -1 and j > i else t


def juzgar(cliente, clusters, nodos, uso):
    """Veredicto por cluster. Devuelve {indice_cluster: veredicto}."""
    if not clusters:
        return {}
    bloques = []
    for i, c in enumerate(clusters):
        lineas = [f"GRUPO {i}"]
        for nid in c:
            n = nodos[nid]
            lineas.append(f"  - [{n.get('fase_proyecto','?')}] {n.get('titulo_concepto','?')}")
            lineas.append(f"    {(n.get('resumen_teorico') or '')[:220]}")
        bloques.append("\n".join(lineas))

    veredictos = {}
    TANDA = 25
    for k in range(0, len(bloques), TANDA):
        trozo = bloques[k:k + TANDA]
        datos = _llamar(cliente, PROMPT_VEREDICTO, "\n\n".join(trozo), uso)
        for v in datos or []:
            if isinstance(v, dict) and isinstance(v.get("grupo"), int):
                veredictos[v["grupo"]] = v
    return veredictos


def _llamar(cliente, system, prompt, uso):
    ultimo = None
    for techo in TECHOS:
        for intento in range(3):
            try:
                with cliente.messages.stream(model=MODEL, max_tokens=techo, system=system,
                                             messages=[{"role": "user", "content": prompt}]) as s:
                    r = s.get_final_message()
                uso["in"] += r.usage.input_tokens
                uso["out"] += r.usage.output_tokens
                if r.stop_reason == "max_tokens":
                    ultimo = "cortada por el techo"
                    break
                return json.loads(_arreglo(_texto_de(r)))
            except json.JSONDecodeError as e:
                ultimo = f"JSON invalido: {e}"
            except Exception as e:
                ultimo = str(e)
                time.sleep(5 * (intento + 1))
    print(f"    AVISO: tanda sin veredicto ({ultimo})")
    return []


# ---------------------------------------------------------------------------
# Paso 3: las otras tres barandas de la vara vigente
# ---------------------------------------------------------------------------
# Detectores LOCALES, con cita textual. Deliberadamente conservadores: cada
# patron exige contexto para no repetir el falso positivo de "puntual" leido
# como "puntua" (cazado el 2026-08-07).
BARANDAS = {
    "dato_local_cableado": [
        r"\b\d+\s*(?:%|por ciento)\s+(?:de impuesto|de arancel|de iva|de comision)",
        r"\b(?:USD|US\$|\$|EUR|€)\s?\d[\d.,]*",
        r"\bdivid(?:e|ir|iendo)\s+entre\s+\d{3,}",
        r"\b\d{3,}\s*(?:kg|libras|lbs)\b",
        r"\b(?:OSHA|EPA|FDA|IRS|SEC)\b",
        r"\bsalario m[ií]nimo de\b",
    ],
    "matriz_o_puntaje": [
        r"\bmatriz de (?:riesgo|probabilidad|impacto|prioridad)",
        r"\bpuntú[ae]\b|\bpuntua(?:r|ndo|cion|ción)\b",
        r"\bescala de\s*1\s*a\s*(?:5|10)\b|\bdel\s*1\s*al\s*(?:5|10)\b",
        r"\bprobabilidad\s*(?:x|por|\*)\s*impacto\b",
        r"\bnivel de riesgo\s*=\s*",
    ],
    "residuo_corporativo": [
        # `tu equipo` SALIO del patron (adjudicado ago 2026). Era correcto en la
        # era de la EXTRACCION: un nodo recien sacado del libro que decia "tu
        # equipo" arrastraba un organigrama. Pero la re-voz lo escribio A
        # PROPOSITO: es la voz de la casa para quien tiene dos o tres personas
        # trabajando con el. Trece nodos ya re-vozados -- ocho de HSEQ -- caian
        # aqui, y ocho los habia re-vozado esta misma casa.
        #
        # DOCTRINA HERMANA DE LA DE LOS ACENTOS:
        #   "Los detectores deben conocer el trabajo ya hecho, o acaban
        #    cobrandolo dos veces."
        # Y la de origen: una baranda que caza lo correcto no es estricta, esta
        # rota. Aqui ademas no era gratis: re-vozar trece nodos buenos cuesta
        # dinero y arriesga DEGRADARLOS, porque el modelo tiene que cambiar algo
        # para justificar su turno.
        #
        # Los marcadores de TERCERA persona se quedan: esos si delatan que el
        # nodo le habla a una empresa que no es la del lector.
        r"\bsu equipo\b|\bel equipo de\b",
        r"\bel comit[ée]\b|\bun comit[ée]\b",
        r"\btu departamento\b|\bel departamento de\b",
        r"\blos stakeholders\b|\blas partes interesadas\b",
        r"\bsu organizaci[óo]n\b|\btu organizaci[óo]n\b",
        r"\bla alta direcci[óo]n\b|\bla gerencia\b",
        r"\brecursos humanos\b",
    ],
}

# LA EXENCION DE LOCALIZACION (adjudicada ago 2026, mismo principio).
#
# `adaptaciones_sectoriales_iso` decia: "las cGMP que exige la FDA en Estados
# Unidos, O EL ORGANISMO EQUIVALENTE EN TU MERCADO". Es decir: el nodo YA trae
# el reencuadre hecho, y la baranda saltaba por la sigla suelta. Es la ley que
# el auditor ya adjudico: detectar por LO QUE EL NODO DESCRIBE, no por lo que
# menciona.
#
# Si la formula de localizacion aparece cerca de la sigla, el nodo esta
# localizado y no se marca. "Cerca" es la misma frase, no el nodo entero: un
# nodo que localiza una sigla al principio no queda exento para otra que
# cablee al final.
VENTANA_LOCALIZACION = 160
LOCALIZACION = re.compile(
    r"\b(?:o el|o la|o su)\s+(?:organismo|entidad|agencia|autoridad|norma|"
    r"equivalente|etiqueta|sello|regulador)\w*\s+(?:\w+\s+){0,3}"
    r"(?:equivalente\s+)?(?:en|de)\s+tu\s+(?:mercado|pa[ií]s|regi[óo]n)"
    r"|\bla\s+(?:que|de)\s+\w+\s+en\s+tu\s+(?:mercado|pa[ií]s)"
    r"|\baverigua\s+(?:cu[áa]l\s+es\s+)?la\s+de\s+tu\s+(?:mercado|pa[ií]s)"
    r"|\bseg[úu]n\s+tu\s+mercado\b"
    r"|\bexisten\s+en\s+muchos\s+pa[ií]ses\b",
    re.I)


def _esta_localizada(texto, ini, fin):
    """True si la formula de localizacion acompaña a esta mencion concreta."""
    ventana = texto[max(0, ini - VENTANA_LOCALIZACION): fin + VENTANA_LOCALIZACION]
    return bool(LOCALIZACION.search(ventana))


REGISTRO_FP = BASE / "dataset" / "metadata" / "falsos_positivos_adjudicados.json"
_fp = None


def falsos_positivos():
    """(node_id, baranda) -> motivo, de los hallazgos YA JUZGADOS.

    Nace del ciclo de la curacion (ago 2026): tres hallazgos distintos costaron
    tres lecturas para llegar a la misma conclusion -- el detector vio la
    palabra, no lo que el nodo describe. Un hallazgo juzgado no se re-litiga.
    """
    global _fp
    if _fp is None:
        _fp = {}
        if REGISTRO_FP.exists():
            for a in json.loads(REGISTRO_FP.read_text(encoding="utf-8"))["adjudicados"]:
                _fp[(a["node_id"], a["baranda"])] = a["motivo"]
    return _fp


def revisar_barandas(nodo, incluir_juzgados=False):
    """Hallazgos con su CITA textual. Vacio = limpio en la muestra."""
    texto = " ".join([
        nodo.get("titulo_concepto", ""), nodo.get("resumen_teorico", ""),
        " ".join(nodo.get("pasos_accionables") or []),
        " ".join(nodo.get("condiciones_activacion") or []),
        nodo.get("entregable_esperado", "") or "",
    ])
    hallazgos = []
    for baranda, patrones in BARANDAS.items():
        marcado = False
        for p in patrones:
            for m in re.finditer(p, texto, re.I):
                # La exencion de localizacion solo aplica a las siglas: una
                # sigla acompañada de "o el equivalente en tu mercado" no es un
                # dato cableado, es un ejemplo ya localizado. Se busca la
                # SIGUIENTE ocurrencia, no se abandona el patron: un nodo puede
                # localizar una sigla y cablear otra.
                if baranda == "dato_local_cableado" and _esta_localizada(texto, m.start(), m.end()):
                    continue
                ini = max(0, m.start() - 55)
                cita = " ".join(texto[ini:m.end() + 55].split())
                h = {"baranda": baranda, "cita": f"...{cita}..."}
                # YA JUZGADO: se reporta como tal, no se vuelve a discutir. Por
                # defecto NO entra en la lista, para que un lote de trabajo no
                # arrastre nodos que ya se leyeron y estaban bien.
                juzgado = falsos_positivos().get((nodo.get("node_id"), baranda))
                if juzgado:
                    if incluir_juzgados:
                        hallazgos.append(dict(h, ya_juzgado=juzgado))
                    marcado = True
                    break
                hallazgos.append(h)
                marcado = True
                break
            if marcado:
                break
    return hallazgos


# ---------------------------------------------------------------------------
# Paso 4: quien referencia ids de nodos (la atadura de una cirugia futura)
# ---------------------------------------------------------------------------
def censo_referencias(nodos):
    ref = {}

    def leer(rel):
        p = BASE / rel
        if not p.exists():
            return None
        with p.open(encoding="utf-8") as f:
            return json.load(f)

    cache = leer("engine/preguntas_cache.json") or {}
    ref["cache_de_preguntas"] = {
        "archivo": "engine/preguntas_cache.json (y su espejo en web/lib/assets)",
        "cuantos_ids": len(cache),
        "atadura": "por node_id; se regenera con --patch-file, no hay migracion",
    }
    # El archivo es {description, seeds}, no una lista pelada: contar len() del
    # dict daba 2 (sus dos claves) y el numero habria pasado por bueno.
    seeds_raw = leer("dataset/metadata/entry_seeds.json") or {}
    seeds = seeds_raw.get("seeds", seeds_raw) if isinstance(seeds_raw, dict) else seeds_raw
    ref["semillas_del_nucleo"] = {
        "archivo": "dataset/metadata/entry_seeds.json",
        "cuantos_ids": len(seeds),
        "atadura": "por node_id; Gate 0 exige alcanzabilidad >= 99.5% desde aqui",
    }
    packs_seeds = leer("web/lib/assets/packs_entry_seeds.json") or {}
    ref["semillas_de_packs"] = {
        "archivo": "web/lib/assets/packs_entry_seeds.json",
        "cuantos_ids": sum(len(v) for v in packs_seeds.values()),
        "atadura": "por node_id; horneado A MANO por pack, integrar_packs no lo produce",
    }
    brecha = leer("web/lib/assets/brecha_semillas.json") or {}
    ref["mapa_de_brecha"] = {
        "archivo": "web/lib/assets/brecha_semillas.json",
        "cuantos_ids": sum(len(v) for k, v in brecha.items() if isinstance(v, dict)),
        "atadura": "por node_id, fase -> semilla; a mano",
    }
    puentes = 0
    for d in (BASE / "packs").iterdir():
        b = d / "metadata" / "bridges_aprobados.json"
        if b.exists():
            with b.open(encoding="utf-8") as f:
                puentes += len(json.load(f).get("aprobados", []))
    ref["puentes_core_pack"] = {
        "archivo": "packs/*/metadata/bridges_aprobados.json",
        "cuantos_ids": puentes * 2,
        "atadura": "por node_id en ambos extremos; tejidos BIDIRECCIONALES en los nodos fuente",
    }
    entrantes = Counter()
    for nid, n in nodos.items():
        for campo in ("nodos_previos", "nodos_siguientes"):
            for r in n.get(campo) or []:
                entrantes[r] += 1
    ref["aristas_del_grafo"] = {
        "archivo": "dataset/nodos/*.json (y el master compilado)",
        "cuantos_ids": sum(entrantes.values()),
        "atadura": "por node_id; borrar un nodo deja aristas rotas y el Gate 0 lo caza",
    }
    idx = leer("web/lib/assets/semantic_index.json") or {}
    ref["indice_semantico"] = {
        "archivo": "web/lib/assets/semantic_index.json",
        "cuantos_ids": len(idx.get("ids", [])),
        "atadura": "por node_id; se regenera entero (voyage-4-lite), sin migracion",
    }
    fam = leer("engine/node_families.json") or {}
    ref["familias_de_readiness"] = {
        "archivo": "engine/node_families.json",
        "cuantos_ids": len(fam),
        "atadura": "por node_id; se regenera gratis (clasificador por palabras)",
    }
    ref["rutas_historicas"] = {
        "archivo": "tabla project_nodes en Supabase",
        "cuantos_ids": "ver telemetria",
        "atadura": "DURA: es historia de usuarios reales, no se regenera",
    }
    return ref


def telemetria(ids_en_clusters):
    """Cuantos de los nodos en clusters fueron visitados alguna vez. Solo SELECT."""
    try:
        from dotenv import load_dotenv
        load_dotenv(BASE / ".env")
        from supabase import create_client
        url = os.getenv("SUPABASE_URL")
        key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
        if not (url and key):
            return {"error": "sin credenciales en .env"}
        cli = create_client(url, key)
        # PAGINADO obligatorio: un select simple se corta en 1.000 filas sin
        # decirlo. Con el corte, este censo reportaba 66 nodos visitados; las
        # 4.463 filas reales dicen 172. Un numero truncado que parece completo
        # es peor que no tenerlo.
        filas, off = [], 0
        while True:
            r = cli.table("project_nodes").select("node_id, tipo").range(off, off + 999).execute()
            filas += r.data or []
            if not r.data or len(r.data) < 1000:
                break
            off += 1000
        visitados = Counter(f["node_id"] for f in filas if f.get("node_id"))
        cosechados = Counter(f["node_id"] for f in filas
                             if f.get("node_id") and f.get("tipo") == "cosechado")
        en_cluster_vistos = [n for n in ids_en_clusters if n in visitados]
        return {
            "filas_project_nodes": len(filas),
            "nodos_distintos_visitados": len(visitados),
            "nodos_distintos_cosechados": len(cosechados),
            "nodos_en_clusters": len(ids_en_clusters),
            "de_esos_visitados_alguna_vez": len(en_cluster_vistos),
            "detalle_visitados": sorted(en_cluster_vistos)[:40],
        }
    except Exception as e:
        return {"error": f"{type(e).__name__}: {e}"}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--sin-api", action="store_true", help="solo la parte local")
    args = ap.parse_args()

    nodos = cargar_grafo()
    ids, E = cargar_embeddings()
    pos = {n: i for i, n in enumerate(ids)}
    packs = defaultdict(list)
    for nid, n in nodos.items():
        if nid in pos:
            packs[n.get("dominio", "?")].append(nid)

    resultado = {"umbral": UMBRAL, "semilla_muestreo": SEMILLA_MUESTREO, "packs": {}}
    total_clusters = 0
    for d in ERAS:
        cl, pares, peor = clusters_candidatos(sorted(packs[d]), pos, E)
        total_clusters += len(cl)
        en_cluster = sum(len(c) for c in cl)
        resultado["packs"][d] = {
            "n": len(packs[d]), "era": ERAS[d][0], "pipeline": ERAS[d][1],
            "clusters": len(cl), "nodos_en_clusters": en_cluster,
            "tasa_pct": round(100 * en_cluster / max(1, len(packs[d])), 1),
            "pares": len(pares),
            "_clusters": cl, "_peor": {str(k): v for k, v in peor.items()},
        }
        print(f"  {d:<20} {len(packs[d]):>5} nodos  {len(cl):>4} clusters  "
              f"{en_cluster:>4} nodos ({resultado['packs'][d]['tasa_pct']:>5.1f}%)")

    print(f"\n  TOTAL: {total_clusters} clusters candidatos a {UMBRAL}")
    if args.dry_run:
        print(f"  estimado del veredicto: ~{total_clusters // 25 + len(ERAS)} llamadas")
        return

    # barandas: 10 al azar por pack, semilla fija para que se pueda repetir
    rnd = random.Random(SEMILLA_MUESTREO)
    for d in ERAS:
        muestra = rnd.sample(sorted(packs[d]), min(NODOS_POR_MUESTRA, len(packs[d])))
        hall = []
        for nid in muestra:
            for h in revisar_barandas(nodos[nid]):
                hall.append({"node_id": nid, "titulo": nodos[nid].get("titulo_concepto"), **h})
        resultado["packs"][d]["muestra_barandas"] = muestra
        resultado["packs"][d]["hallazgos_barandas"] = hall

    resultado["referencias"] = censo_referencias(nodos)
    en_clusters = sorted({n for d in ERAS for c in resultado["packs"][d]["_clusters"] for n in c})
    resultado["telemetria"] = telemetria(en_clusters)

    uso = {"in": 0, "out": 0}
    if not args.sin_api:
        from dotenv import load_dotenv
        import anthropic
        load_dotenv(BASE / ".env")
        cliente = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        for d in ERAS:
            cl = resultado["packs"][d]["_clusters"]
            if not cl:
                continue
            print(f"\n  veredicto de {d}: {len(cl)} clusters")
            v = juzgar(cliente, cl, nodos, uso)
            resultado["packs"][d]["veredictos"] = {str(k): x for k, x in v.items()}
            reales = [i for i in range(len(cl)) if v.get(i, {}).get("fundir")]
            n_reales = sum(len(cl[i]) for i in reales)
            resultado["packs"][d]["clusters_confirmados"] = len(reales)
            resultado["packs"][d]["nodos_confirmados"] = n_reales
            resultado["packs"][d]["tasa_confirmada_pct"] = round(
                100 * n_reales / max(1, resultado["packs"][d]["n"]), 1)
            print(f"    confirmados {len(reales)}/{len(cl)} -> {n_reales} nodos "
                  f"({resultado['packs'][d]['tasa_confirmada_pct']}%)")

    resultado["costo"] = {
        "tokens_in": uso["in"], "tokens_out": uso["out"],
        "usd": round(uso["in"] / 1e6 * PRECIO_IN_MTOK + uso["out"] / 1e6 * PRECIO_OUT_MTOK, 2),
    }
    salida = BASE / "docs" / "_censo_duplicacion.json"
    salida.write_text(json.dumps(resultado, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n  Datos en {salida}")
    print(f"  Costo medido: ${resultado['costo']['usd']}")


if __name__ == "__main__":
    main()
