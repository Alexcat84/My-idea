# -*- coding: utf-8 -*-
"""Cuarto pase de la limpieza M11: reparte los 471 nodos (copia/ con las once tandas) en 16 lotes con la semilla escrita
antes de repartir (../m11-claves/umbral_y_semilla_auditoria.json, cuarto_pase) y 1 o 2 trampas SIN MARCA por lote, en ids
reales. Cada nodo lleva sus avisos mecanicos (candidatos, no veredictos): lexico de regionalismos de ambos lados, primera
persona del plural, "a cargo" sin posesivo, calcos conocidos y demostrativos que pueden no tener antecedente.

    python pase4/repartir.py
"""
import glob
import json
import os
import random
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
TRABAJO = AQUI.parent
SEM = json.loads((TRABAJO.parent / "m11-claves" / "umbral_y_semilla_auditoria.json").read_text(encoding="utf-8"))["cuarto_pase"]["semilla_reparto_pase4"]
NLOTES = 16

AVISOS = [
    ("regionalismo", r"\b(pegas?|apañ\w*|li[aá](r|da|do|ndo|ste|s)\b|fastidi\w*|cog(er|e|es|ió|iste|ido)\b|móvil|ordenador|coche|tío|tía|curr(o|ar|ando)|chaval\w*|majo|guay|flip\w*|mola|molar|pill(ar|a|ó|aste)\b|bronca|la lata|a por\b|tir(a|ar|ando) de\b|chapuza|cabre\w*|jaleo|follón|cutre|enchuf\w*|mogollón|hacer la pelota|pelota\b|vale[,.]|auto\b|computadora|celular|platic\w*|chamba|ahorita|carro\b|plata\b|chévere|bacán|agarr\w*|jal(ar|a|ó)\b|piso\b|zumo|gafas|vídeo|tope de|a tope|currículum|fichaje|prima\b|metedura|meter la pata|la has|tela\b|chungo|pasta\b)"),
    ("voz", r"\b(nuestr[oa]s?|nosotr[oa]s|(?!(?:vamos|próximos|extremos|últimos|legítimos|mismos|mínimos|máximos|primos|ánimos|términos|íntimos|óptimos|supremos|remos|temos)\b)\w*[^íéá\W]\w*(amos|emos|imos|íamos|ábamos|aremos|eremos|iremos)\b)"),
    ("coherencia", r"(?<!\btu )(?<!\bsu )(?<!\bmi )(?<!\bsus )(?<!\btus )\ba cargo\b"),
    ("calco", r"\b(entreg\w+ (el|un|tu|la|su) (mensaje|guía|opinión|crítica|retroalimentación)|guía entregada|hac\w+ sentido|tom\w+ (una )?acción|aplic\w+ (a|para) (un|el|la|una) (puesto|trabajo)|en base a|a nivel de|jug\w+ un (rol|papel)|empoder\w+|agend(ar|es|ó|aste|a tu|a una)|cheque\w+|impact\w+ (en|a)\b|direccion\w+|soport\w+|eventualmente|realiz\w+ que|posición\b|remov\w+|salvar el día|al final del día|hac\w+ la diferencia|dar seguimiento|asum\w+ que|aplicación\b|audiencia\b|honr\w+|captur\w+|escal(ar|a|ó)\b|atender a (la|una) reunión|introduc\w+ a (alguien|tu|un|una)|ir al punto|tiene sentido|chance|feedback|mentoría|coachear|coaching|staff|manager)"),
    ("coherencia", r"\b(este mismo|esta misma|ese mismo|esa misma|estos mismos|el paso anterior|la lista anterior|más arriba|más abajo|ya descrit\w+|antes descrit\w+|como se dijo|dicho proceso)\b"),
]


def avisos(n):
    out = []
    campos = [("titulo_concepto", n["titulo_concepto"]), ("resumen_teorico", n["resumen_teorico"]), ("entregable_esperado", n["entregable_esperado"])]
    campos += [("pasos_accionables[%d]" % i, s) for i, s in enumerate(n["pasos_accionables"])]
    campos += [("condiciones_activacion[%d]" % i, s) for i, s in enumerate(n["condiciones_activacion"])]
    for campo, t in campos:
        for tipo, pat in AVISOS:
            for m in re.finditer(pat, t, re.I):
                out.append({"campo": campo, "tipo_posible": tipo, "texto": m.group(0),
                            "contexto": t[max(0, m.start() - 60):m.end() + 40]})
    L = len(n["resumen_teorico"])
    if not 400 <= L <= 600:
        out.append({"campo": "resumen_teorico", "tipo_posible": "longitud", "texto": "%d caracteres" % L, "contexto": ""})
    return out


def main():
    rnd = random.Random(SEM)
    ev = {c["node_id"]: c["cita"]["evidencia"] for c in json.loads((TRABAJO / "tanda_m11_limpieza.json").read_text(encoding="utf-8")) if c["veredicto"] == "RESUMEN"}
    ids = sorted(os.path.basename(p)[:-5] for p in glob.glob(str(TRABAJO / "copia" / "primer_equipo" / "nodos" / "*.json")))
    rnd.shuffle(ids)
    lotes = [ids[i::NLOTES] for i in range(NLOTES)]
    TIPOS = ["coherencia", "coherencia", "regionalismo", "calco", "ortografia"]
    REG = [("inconveniente", "pega"), ("se las arregla", "se apaña"), ("tomar", "coger"), ("equivocarte", "liarla")]
    CAL = [("dar la guía", "entregar la guía"), ("importa", "hace la diferencia"), ("programa", "agenda"), ("comprueba", "chequea")]
    clave, total = {}, 0
    for k, lote in enumerate(lotes, 1):
        nn = "%02d" % k
        nodos = []
        for nid in lote:
            n = json.loads((TRABAJO / "copia" / "primer_equipo" / "nodos" / ("%s.json" % nid)).read_text(encoding="utf-8"))
            a = avisos(n)
            total += len(a)
            nodos.append({"node_id": nid, "titulo_concepto": n["titulo_concepto"], "resumen_teorico": n["resumen_teorico"],
                          "pasos_accionables": list(n["pasos_accionables"]), "entregable_esperado": n["entregable_esperado"],
                          "condiciones_activacion": list(n["condiciones_activacion"]), "evidencia": ev[nid], "avisos": a})
        for _ in range(rnd.choice([1, 2])):
            tipo = rnd.choice(TIPOS)
            for intento in range(300):
                nd = rnd.choice(nodos)
                if nd["node_id"] in clave:
                    continue
                i = rnd.randrange(len(nd["pasos_accionables"]))
                p = nd["pasos_accionables"][i]
                if tipo == "coherencia":
                    nuevo = p.rstrip(".") + ", como con el cliente de la fábrica que viste antes."
                elif tipo in ("regionalismo", "calco"):
                    a, b = rnd.choice(REG if tipo == "regionalismo" else CAL)
                    if a not in p:
                        continue
                    nuevo = p.replace(a, b, 1)
                else:
                    m = re.search(r"\b(que|de|los|las)\b", p)
                    if not m:
                        continue
                    rep = {"que": "qe", "de": "del", "los": "lo", "las": "la"}[m.group(1)]
                    nuevo = p[:m.start()] + rep + p[m.end():]
                if nuevo == p:
                    continue
                nd["pasos_accionables"][i] = nuevo
                clave[nd["node_id"]] = {"lote": nn, "campo": "pasos_accionables[%d]" % i, "tipo": tipo, "original": p, "plantado": nuevo}
                break
        (AQUI / ("entrada_%s.json" % nn)).write_text(json.dumps({"lote": nn, "nodos": nodos}, ensure_ascii=False, indent=1), encoding="utf-8")
    (TRABAJO.parent / "m11-claves" / "pase4.json").write_text(json.dumps({"semilla": SEM, "trampas": clave}, ensure_ascii=False, indent=1), encoding="utf-8")
    print("%d lotes, %d nodos, %d avisos, %d trampas sin marca" % (len(lotes), sum(map(len, lotes)), total, len(clave)))


if __name__ == "__main__":
    main()
