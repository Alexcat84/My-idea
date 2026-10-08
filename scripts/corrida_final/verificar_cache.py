# -*- coding: utf-8 -*-
"""VERIFICACION DE LO GENERADO EN EL PASO 1 DE LA CORRIDA FINAL (decision del fundador, 8 oct 2026).

Cuatro subcomandos. Ninguno llama a la API: los jueces son agentes de Claude Code.

    papeles  --salida <md>
        Guarda automatica sobre el 100 % de las neutrales (de base y de entrada): una neutral que nombra un papel o
        una estructura (jefe, equipo, socios, recursos humanos...) tiene que plantearlo en condicional o como pregunta
        por su existencia ("si tienes...", "hay alguien...", "trabajas con..."). Las que no, se listan con su motivo.
        La procedencia y la voz de libro las cubren las guardas de siempre sobre toda la cache web
        (web/lib/procedencia.test.ts, web/lib/vozDeCliente.test.ts), que corren con las suites.

    muestra  --paquetes <dir> --claves <dir> [--semilla 20261008]
        MUESTRA CIEGA de 200 pares base/neutral (proporcional entre bases y entradas, con al menos 10 de entrada),
        mas 1 trampa sin marca por cada 20: una neutral de OTRO nodo del mismo dominio puesta como si fuera la de la
        base (busca otra cosa). Se barajan y se reparten en paquetes de 21. Las claves van a otra carpeta.

    nuevas   --paquetes <dir> --claves <dir> [--semilla 20261008]
        Las PREGUNTAS NUEVAS del paso 1 (nodos que no tenian pregunta), cada una con su propio nodo, mas 1 trampa sin
        marca por cada 5: copias de una pregunta real con un contrario, una invencion (cifra o plazo que el nodo no
        dice) o una pregunta de otro nodo (logica que no encaja). Se juzgan contra su nodo.

    contar   --veredictos <dir> --claves <dir> --modo muestra|nuevas --salida <md>
        Junta los veredictos de los jueces con las claves y saca la cuenta contra el umbral.
        muestra: como mucho 1 de cada 20 pares REALES con fallo de fidelidad; todas las trampas cazadas.
        nuevas: 0 contrarios, 0 invenciones, 0 logica que no encaja entre las REALES; todas las trampas cazadas.
"""
import argparse
import json
import random
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(BASE / "engine"))
import build_question_cache as bqc  # noqa: E402  (GENERO: la misma regla que rechaza al generar)
CACHE = BASE / "engine" / "preguntas_cache.json"
GRAFO = BASE / "dataset" / "metadata" / "master_graph.json"
LISTA_NUEVAS = BASE / "docs" / "corrida_final" / "2026-10-08" / "preguntas_nuevas.json"

PAPEL = re.compile(
    r"\b(jef[ea]s?|recursos humanos|directiv\w*|departamento\w*|emplead\w*|equipo\w*|subordinad\w*|gerente\w*|"
    r"socio\w*|colaborador\w*|junta|cofundador\w*|personal a tu cargo)\b", re.I)
CONDICIONAL = re.compile(
    r"\b(si|cuando|en caso|hay alguien|alguien|tienes|cuentas con|trabajas con|llegas a|llegaras|piensas|planeas|"
    r"quien|quienes|podr[ií]as|podr[ií]a|ser[ií]a|ya hay|existe)\b", re.I)


def cargar():
    cache = json.loads(CACHE.read_text(encoding="utf-8"))
    grafo = json.loads(GRAFO.read_text(encoding="utf-8"))["nodos"]
    return cache, grafo


def vivo(nid, grafo):
    return nid in grafo and not grafo[nid].get("deprecado")


def pares(cache, grafo):
    """(nid, clase, pregunta, neutral) de cada neutral generada en un nodo vivo."""
    out = []
    for nid, e in cache.items():
        if not vivo(nid, grafo):
            continue
        if e.get("pregunta") and e.get("pregunta_neutral"):
            out.append((nid, "base", e["pregunta"], e["pregunta_neutral"]))
        if e.get("pregunta_entrada") and e.get("pregunta_entrada_neutral"):
            out.append((nid, "entrada", e["pregunta_entrada"], e["pregunta_entrada_neutral"]))
    return out


def frases(texto):
    return [f for f in re.split(r"(?<=[.?!¿¡])\s+", texto) if f.strip()]


def falta_papel(neutral):
    """None si la neutral no supone papeles; si no, el papel que da por hecho."""
    for f in frases(neutral):
        m = PAPEL.search(f)
        if m and not CONDICIONAL.search(f):
            return m.group(0)
    return None


# Los cuatro patrones de la muestra que no paso (decision del fundador, 8 oct 2026). El genero y la segunda peticion
# son precisos (el generador ya los rechaza); las personas sin condicional y el contexto perdido son heuristicas: la
# guarda los reporta para revisarlos, no los da por fallo sin mirar.
PERSONAS = re.compile(
    r"\b(las personas que (trabajan|colaboran|te acompañan|te ayudan)|quienes (trabajan|colaboran) contigo|"
    r"quienes te acompañan|la gente que trabaja contigo|tu gente|tus compañer\w+|tus colaborador\w+|tu equipo|"
    r"las personas de tu equipo)\b", re.I)
CONDICIONAL_PERSONAS = re.compile(
    r"\b(si|en caso|alg[uú]n d[ií]a|alguna vez|en alg[uú]n momento|quiz[aá]s?|llegaras|llegas a|trabajen|tengas|"
    r"tuvieras|contaras|cuentes)\b", re.I)
# El contexto propio: temas concretos que, si estan en la base, deben seguir en la neutral (por su raiz).
ANCLAS = ["franquic", "proveedor", "export", "import", "aduan", "inversionist", "financiaci", "segurid", "accident",
          "lesi", "riesg", "calidad", "ambient", "residu", "emisi", "energ", "cumplimiento", "legal", "contrat",
          "certific", "patent", "licenci"]


def patrones(base, neutral):
    """Los patrones de fallo que la guarda detecta en una neutral (lista vacia = ninguno)."""
    out = []
    if bqc.GENERO.search(neutral):
        out.append("genero")
    if neutral.count("?") > base.count("?"):
        out.append("segunda_peticion")
    if any(PERSONAS.search(f) and not CONDICIONAL_PERSONAS.search(f) for f in frases(neutral)):
        out.append("personas_sin_condicional")
    b, n = base.lower(), neutral.lower()
    if any(a in b and a not in n for a in ANCLAS):
        out.append("contexto_perdido")
    return out


def cmd_papeles(a):
    cache, grafo = cargar()
    todos = pares(cache, grafo)
    fallos = [(nid, clase, neu, falta_papel(neu)) for nid, clase, _b, neu in todos if falta_papel(neu)]
    por_patron = {}
    for nid, clase, b, neu in todos:
        for pat in patrones(b, neu):
            por_patron.setdefault(pat, []).append((nid, clase, b, neu))
    sin = [nid for nid, e in cache.items() if vivo(nid, grafo) and e.get("pregunta") and not e.get("pregunta_neutral")]
    sin_e = [nid for nid, e in cache.items()
             if vivo(nid, grafo) and e.get("pregunta_entrada") and not e.get("pregunta_entrada_neutral")]
    L = ["# Guarda automatica de las neutrales (100 %): papeles supuestos y los cuatro patrones", "",
         f"Neutrales revisadas: {len(todos)} ({sum(1 for p in todos if p[1] == 'base')} de base, "
         f"{sum(1 for p in todos if p[1] == 'entrada')} de entrada).",
         f"Bases vivas sin neutral: {len(sin)}. Entradas vivas sin neutral: {len(sin_e)}.",
         f"Neutrales que nombran un papel sin condicional: **{len(fallos)}**.", ""]
    for nid, clase, neu, papel in fallos:
        L.append(f"- `{nid}` ({clase}), papel «{papel}»: {neu}")
    for pat, titulo in [("genero", "Marcan el género del lector (precisa)"),
                        ("segunda_peticion", "Más preguntas que su base (precisa)"),
                        ("personas_sin_condicional", "Personas sin condicional (heurística: revisar)"),
                        ("contexto_perdido", "Contexto propio de la base perdido (heurística: revisar)")]:
        casos = por_patron.get(pat, [])
        L += ["", f"## {titulo}: **{len(casos)}**", ""]
        for nid, clase, b, neu in casos:
            L += [f"- `{nid}` ({clase})", f"  - base: {b}", f"  - neutral: {neu}"]
    Path(a.salida).parent.mkdir(parents=True, exist_ok=True)
    Path(a.salida).write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L[:6]))
    return 0


def repartir(items, tam):
    return [items[i:i + tam] for i in range(0, len(items), tam)]


def cmd_muestra(a):
    cache, grafo = cargar()
    rnd = random.Random(a.semilla)
    todos = pares(cache, grafo)
    bases = [p for p in todos if p[1] == "base"]
    entradas = [p for p in todos if p[1] == "entrada"]
    n_ent = max(10, round(200 * len(entradas) / max(1, len(todos))))
    n_ent = min(n_ent, len(entradas))
    elegidos = rnd.sample(entradas, n_ent) + rnd.sample(bases, 200 - n_ent)
    # trampas: 1 por cada 20 -> 10. Una base real de fuera de la muestra con la neutral de otro nodo del mismo dominio.
    usados = {(p[0], p[1]) for p in elegidos}
    resto = [p for p in todos if (p[0], p[1]) not in usados]
    trampas = []
    for p in rnd.sample(resto, 40):
        dom = grafo[p[0]].get("dominio", "core")
        otros = [q for q in todos if q[0] != p[0] and grafo[q[0]].get("dominio", "core") == dom
                 and q[0] not in grafo[p[0]].get("nodos_siguientes", [])]
        if not otros:
            continue
        q = rnd.choice(otros)
        trampas.append({"nid": p[0], "clase": p[1], "base": p[2], "neutral": q[3], "neutral_de": q[0]})
        if len(trampas) == 10:
            break
    items = [{"nid": p[0], "clase": p[1], "base": p[2], "neutral": p[3], "trampa": False} for p in elegidos]
    items += [{**t, "trampa": True} for t in trampas]
    rnd.shuffle(items)
    paquetes, claves = Path(a.paquetes), Path(a.claves)
    paquetes.mkdir(parents=True, exist_ok=True)
    claves.mkdir(parents=True, exist_ok=True)
    clave = {}
    for i, lote in enumerate(repartir(items, 21), 1):
        pid = f"n{i:02d}"
        salida = []
        for j, it in enumerate(lote, 1):
            iid = f"{pid}-{j:02d}"
            etiqueta = grafo[it["nid"]].get("etiqueta_arbol") or grafo[it["nid"]].get("titulo_concepto", "")
            salida.append({"id": iid, "tema": etiqueta, "pregunta_base": it["base"], "pregunta_neutral": it["neutral"]})
            clave[iid] = {k: it[k] for k in ("nid", "clase", "trampa")} | ({"neutral_de": it["neutral_de"]} if it["trampa"] else {})
        (paquetes / f"{pid}.json").write_text(json.dumps({"paquete": pid, "pares": salida}, ensure_ascii=False, indent=2),
                                              encoding="utf-8")
    (claves / "claves_muestra.json").write_text(json.dumps(clave, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"muestra: {len(elegidos)} reales ({n_ent} de entrada) + {len(trampas)} trampas en "
          f"{len(repartir(items, 21))} paquetes")
    return 0


def cmd_nuevas(a):
    cache, grafo = cargar()
    rnd = random.Random(a.semilla)
    nuevas = json.loads(Path(a.lista).read_text(encoding="utf-8")) if a.lista else json.loads(LISTA_NUEVAS.read_text(encoding="utf-8"))
    nuevas = [x["nid"] if isinstance(x, dict) else x for x in nuevas]
    reales = [{"nid": nid, "pregunta": cache[nid]["pregunta"], "trampa": None} for nid in nuevas]
    # trampas: 1 por cada 5, de los tres tipos, sobre copias de preguntas reales
    n_tr = max(3, round(len(reales) / 5))
    trampas = []
    for k, r in enumerate(rnd.sample(reales, n_tr)):
        tipo = ["contrario", "invencion", "logica"][k % 3]
        p = r["pregunta"].rstrip("?").rstrip()
        if tipo == "contrario":
            texto = p + ", sabiendo que en esta etapa lo mejor es no hablar todavía con nadie de fuera?"
        elif tipo == "invencion":
            texto = p + ", sabiendo que la norma exige hacerlo en un plazo máximo de 30 días y con al menos 50 casos?"
        else:
            otro = rnd.choice([x for x in reales if x["nid"] != r["nid"]])
            texto = otro["pregunta"]
        trampas.append({"nid": r["nid"], "pregunta": texto, "trampa": tipo})
    items = reales + trampas
    rnd.shuffle(items)
    paquetes, claves = Path(a.paquetes), Path(a.claves)
    paquetes.mkdir(parents=True, exist_ok=True)
    claves.mkdir(parents=True, exist_ok=True)
    clave = {}
    for i, lote in enumerate(repartir(items, 18), 1):
        pid = f"q{i:02d}"
        salida = []
        for j, it in enumerate(lote, 1):
            iid = f"{pid}-{j:02d}"
            n = grafo[it["nid"]]
            sig = [grafo[s].get("etiqueta_arbol") or grafo[s].get("titulo_concepto", "")
                   for s in cache[it["nid"]].get("candidatos", []) if s in grafo][:6]
            salida.append({
                "id": iid,
                "nodo": {"concepto": n.get("titulo_concepto", ""), "resumen": n.get("resumen_teorico", ""),
                         "condiciones": n.get("condiciones_activacion", []), "entregable": n.get("entregable_esperado", ""),
                         "siguientes": sig},
                "pregunta": it["pregunta"],
            })
            clave[iid] = {"nid": it["nid"], "trampa": it["trampa"]}
        (paquetes / f"{pid}.json").write_text(json.dumps({"paquete": pid, "preguntas": salida}, ensure_ascii=False, indent=2),
                                              encoding="utf-8")
    (claves / "claves_nuevas.json").write_text(json.dumps(clave, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"nuevas: {len(reales)} reales + {len(trampas)} trampas en {len(repartir(items, 18))} paquetes")
    return 0


def cmd_contar(a):
    claves_dir, ver_dir = Path(a.claves), Path(a.veredictos)
    clave = json.loads((claves_dir / ("claves_muestra.json" if a.modo == "muestra" else "claves_nuevas.json")).read_text(encoding="utf-8"))
    veredictos = {}
    for f in sorted(ver_dir.glob("*.json")):
        for v in json.loads(f.read_text(encoding="utf-8"))["veredictos"]:
            veredictos[v["id"]] = v
    faltan = [i for i in clave if i not in veredictos]
    L = [f"# Recuento de la verificacion ciega ({a.modo})", ""]
    if a.modo == "muestra":
        reales = [i for i, c in clave.items() if not c["trampa"]]
        trampas = [i for i, c in clave.items() if c["trampa"]]
        fallo = [i for i in reales if veredictos.get(i, {}).get("veredicto") != "fiel"]
        cazadas = [i for i in trampas if veredictos.get(i, {}).get("veredicto") != "fiel"]
        tope = len(reales) // 20
        pasa = len(fallo) <= tope and len(cazadas) == len(trampas) and not faltan
        L += [f"Pares reales: {len(reales)}. Con fallo: **{len(fallo)}** (tope: {tope}, 1 de cada 20).",
              f"Trampas cazadas: **{len(cazadas)}/{len(trampas)}**. Sin veredicto: {len(faltan)}.",
              f"**{'PASA' if pasa else 'NO PASA'}**", "", "## Fallos en pares reales"]
        for i in fallo:
            v = veredictos.get(i, {})
            L.append(f"- {i} `{clave[i]['nid']}` ({clave[i]['clase']}): {v.get('veredicto')}: {v.get('motivo', '')}")
        L += ["", "## Trampas no cazadas"] + [f"- {i} `{clave[i]['nid']}`" for i in trampas if i not in cazadas]
    else:
        reales = [i for i, c in clave.items() if not c["trampa"]]
        trampas = [i for i, c in clave.items() if c["trampa"]]
        malos = [i for i in reales if veredictos.get(i, {}).get("veredicto") in ("contrario", "invencion", "logica")]
        cazadas = [i for i in trampas if veredictos.get(i, {}).get("veredicto") in ("contrario", "invencion", "logica")]
        pasa = not malos and len(cazadas) == len(trampas) and not faltan
        L += [f"Preguntas nuevas reales: {len(reales)}. Con contrario, invencion o logica que no encaja: **{len(malos)}** (umbral 0).",
              f"Trampas cazadas: **{len(cazadas)}/{len(trampas)}**. Sin veredicto: {len(faltan)}.",
              f"**{'PASA' if pasa else 'NO PASA'}**", "", "## Hallazgos en preguntas reales"]
        for i in malos:
            v = veredictos[i]
            L.append(f"- {i} `{clave[i]['nid']}`: {v['veredicto']}: {v.get('motivo', '')}")
        L += ["", "## Trampas no cazadas"] + [f"- {i} `{clave[i]['nid']}` ({clave[i]['trampa']})" for i in trampas if i not in cazadas]
    Path(a.salida).parent.mkdir(parents=True, exist_ok=True)
    Path(a.salida).write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L[:5]))
    return 0 if pasa else 1


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("papeles"); p.add_argument("--salida", required=True)
    for nombre in ("muestra", "nuevas"):
        p = sub.add_parser(nombre)
        p.add_argument("--paquetes", required=True); p.add_argument("--claves", required=True)
        p.add_argument("--semilla", type=int, default=20261008)
        p.add_argument("--lista", default=None, help="nuevas: solo los nodos de este JSON (lista de ids o de objetos con nid)")
    p = sub.add_parser("contar")
    p.add_argument("--veredictos", required=True); p.add_argument("--claves", required=True)
    p.add_argument("--modo", choices=["muestra", "nuevas"], required=True); p.add_argument("--salida", required=True)
    a = ap.parse_args()
    return {"papeles": cmd_papeles, "muestra": cmd_muestra, "nuevas": cmd_nuevas, "contar": cmd_contar}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
