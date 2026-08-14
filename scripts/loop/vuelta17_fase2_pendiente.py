"""VUELTA 17. Instrumento propio, SOLO LECTURA.

Mide lo que le queda a la FASE II, bloque por bloque, para que deje de ser una
lista de nombres en prosa y pase a ser una NOMINA con cifras y con su corte.

NO cierra ninguno de los bloques: los MIDE. La diferencia importa y se dice: el
bloque grande (los ejemplares de las veinte figuras) es trabajo de LECTURA, y el
grep quedo descartado como instrumento en la vuelta 15 porque doce de las veinte
dan cero menciones teniendo ejemplares declarados. Lo que este script aporta es
el TAMANO y la FORMA exactos de lo que falta, no su contenido.

BLOQUES QUE MIDE
  1. los ejemplares de las veinte figuras
  2. el lote de cinco del sales roadmap, nombrando los cinco pares
  3. la cola de relectura post fusion
  4. el criterio del forastero
  5. las lecturas de acto entero de P.5

Uso: python scripts/loop/vuelta17_fase2_pendiente.py
"""

import json
import os
import re
import itertools
import collections

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
D = lambda *p: os.path.join(RAIZ, *p)


def jsonl(ruta):
    with open(ruta, encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.strip()
            if linea:
                yield json.loads(linea)


def main():
    inventario = list(jsonl(D("docs", "plan", "INVENTARIO.jsonl")))
    veredictos = list(jsonl(D("docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")))
    operaciones = list(jsonl(D("docs", "plan", "OPERACIONES.jsonl")))
    componentes = list(jsonl(D("docs", "plan", "RECOMPUTO_3388_COMPONENTES.jsonl")))

    print("MATERIA PRIMA:", len(inventario), "filas de inventario |", len(veredictos),
          "veredictos |", len(operaciones), "operaciones |", len(componentes), "componentes")
    print()

    # ---------------------------------------------------------------- 1
    print("=" * 78)
    print("BLOQUE 1. LOS EJEMPLARES DE LAS VEINTE FIGURAS")
    print("=" * 78)
    figuras = [o for o in inventario if o["tipo"] == "figura"]
    print("figuras:", len(figuras))

    # una figura NOMBRA sus ejemplares si su nota trae al menos una de estas senales:
    # un id de nodo (minusculas con guion bajo), un puesto citado, o un id de lectura dirigida
    senal_id = re.compile(r"\b[a-z][a-z0-9]*(?:_[a-z0-9]+){2,}\b")
    senal_puesto = re.compile(r"\bpuestos?\s+\d{2,4}\b", re.IGNORECASE)
    senal_ld = re.compile(r"\bLD-\d+\b")

    def declara(cobertura):
        """primer numero del campo cobertura, o None si no lo hay"""
        m = re.search(r"\d+", cobertura)
        return int(m.group()) if m else None

    nombran, no_nombran = [], []
    for f in figuras:
        nota = f["nota"]
        tiene = bool(senal_id.search(nota) or senal_puesto.search(nota) or senal_ld.search(nota))
        (nombran if tiene else no_nombran).append(f)

    print()
    print("  LAS QUE NOMBRAN ALGUN EJEMPLAR EN SU PROPIA NOTA:", len(nombran))
    for f in nombran:
        print("    [", f["fecha_corte"], "]", f["nombre"], "|", f["cobertura"])
    print()
    print("  LAS QUE NO NOMBRAN NINGUNO:", len(no_nombran))
    total_sin_nombre = 0
    for f in no_nombran:
        n = declara(f["cobertura"])
        if n:
            total_sin_nombre += n
        print("    [", f["fecha_corte"], "]", f["nombre"], "|", f["cobertura"])
    print()
    print("  EJEMPLARES DECLARADOS Y SIN NOMBRAR (suma del primer numero de cobertura):",
          total_sin_nombre)
    print("  reparto por fecha_corte de las que nombran:",
          dict(collections.Counter(f["fecha_corte"] for f in nombran)))
    print("  reparto por fecha_corte de las que NO nombran:",
          dict(collections.Counter(f["fecha_corte"] for f in no_nombran)))
    print()

    # ---------------------------------------------------------------- 2
    print("=" * 78)
    print("BLOQUE 2. EL LOTE DE CINCO DEL SALES ROADMAP, con los cinco pares NOMBRADOS")
    print("=" * 78)
    racimo = [o for o in inventario if o["tipo"] == "racimo" and o["nombre"] == "el sales roadmap"]
    assert len(racimo) == 1
    nomina = racimo[0]["miembros"]
    print("nomina:", len(nomina), "nodos |", racimo[0]["cobertura"], "|", racimo[0]["forma"])
    for n in nomina:
        print("   ", n)
    posibles = list(itertools.combinations(sorted(nomina), 2))
    print("pares posibles:", len(posibles))

    en_cola = {}
    for v in veredictos:
        par = tuple(sorted((v["nodo_a"], v["nodo_b"])))
        if par in set(posibles):
            en_cola[par] = v
    print("pares con veredicto:", len(en_cola),
          "| clases:", dict(collections.Counter(v["clase"] for v in en_cola.values())))
    faltan = [p for p in posibles if p not in en_cola]
    print()
    print("LOS QUE FALTAN, nombrados:", len(faltan))
    for a, b in faltan:
        print("   ", a, "contra", b)
    print()
    print("  clases de los que SI estan, par por par:")
    for p in sorted(en_cola, key=lambda x: en_cola[x]["puesto_intra"]):
        v = en_cola[p]
        print("    puesto", v["puesto_intra"], "|", v["clase"], "|", p[0], "contra", p[1])
    print()

    # ---------------------------------------------------------------- 3
    print("=" * 78)
    print("BLOQUE 3. LA COLA DE RELECTURA POST FUSION")
    print("=" * 78)
    marcas = ("post fusion", "postfusion", "relectura")
    en_ops = []
    for o in operaciones:
        texto = json.dumps(o, ensure_ascii=False).lower()
        if any(m in texto for m in marcas):
            en_ops.append(o["id_op"])
    print("operaciones cuyo texto menciona relectura o post fusion:", len(en_ops))
    print("  ", en_ops)
    # las relecturas que las operaciones nombran por puesto en su campo verificacion
    citados = collections.Counter()
    for o in operaciones:
        for linea in o["verificacion"]:
            for num in re.findall(r"\b(\d{3,4})\b", linea):
                if any(w in linea.lower() for w in ("relee", "releen", "releer", "relectura", "salen de la lista")):
                    citados[(o["id_op"], int(num))] += 1
    print("pares que alguna verificacion manda RELEER, con su operacion:", len(citados))
    for (op, puesto), _ in sorted(citados.items()):
        v = [x for x in veredictos if x["puesto_intra"] == puesto]
        clase = v[0]["clase"] if v else "sin veredicto"
        print("   ", op, "-> puesto", puesto, "| clase hoy:", clase)
    print()

    # ---------------------------------------------------------------- 4
    print("=" * 78)
    print("BLOQUE 4. EL CRITERIO DEL FORASTERO")
    print("=" * 78)
    fig = [f for f in figuras if "forastero" in f["nombre"].lower()]
    for f in fig:
        print("figura:", f["nombre"], "|", f["cobertura"], "| corte", f["fecha_corte"])
        print("  estado:", f["estado"])
        print("  miembros nombrados en el campo miembros:", f["miembros"])
    # los dos ejemplares, medidos contra el cribado
    for nid in ("tacticas_cierre_ventas", "incentivos_no_monetarios_advocacy"):
        pares = [v for v in veredictos if nid in (v["nodo_a"], v["nodo_b"])]
        aes = [v for v in pares if v["clase"] == "A"]
        print(" ", nid, "| pares en el cribado:", len(pares),
              "| clases:", dict(collections.Counter(v["clase"] for v in pares)))
        for v in aes:
            otro = v["nodo_b"] if v["nodo_a"] == nid else v["nodo_a"]
            print("     su A es el puesto", v["puesto_intra"], "contra", otro)
    print()

    # ---------------------------------------------------------------- 5
    print("=" * 78)
    print("BLOQUE 5. LAS LECTURAS DE ACTO ENTERO DE P.5")
    print("=" * 78)
    print("P.5: cada acto que vaya a fundirse se lee ENTERO antes de fundirse.")
    abiertos = [c for c in componentes if c["estado"] == "ABIERTO"]
    cerrados = [c for c in componentes if c["estado"] == "CERRADO"]
    print("componentes al corte 3.388:", len(componentes),
          "| CERRADOS", len(cerrados), "| ABIERTOS", len(abiertos))
    completos = [c for c in componentes if c["leidos"] == c["posibles"]]
    incompletos = [c for c in componentes if c["leidos"] < c["posibles"]]
    print("con TODOS sus pares leidos (P.5 es un hecho):", len(completos))
    print("con pares sin leer (P.5 es una condicion pendiente):", len(incompletos))
    print("  pares que faltan en total:", sum(c["posibles"] - c["leidos"] for c in incompletos))
    print("  de esos, EN COLA sin leer:", sum(c["en_cola_sin_leer"] for c in incompletos),
          "| FUERA de cola:", sum(c["fuera_de_cola"] for c in incompletos))
    print()
    print("  los INCOMPLETOS por tamano:",
          dict(sorted(collections.Counter(c["tamano"] for c in incompletos).items())))
    print("  los DIEZ mas grandes con pares sin leer:")
    for c in sorted(incompletos, key=lambda x: -x["tamano"])[:10]:
        print("    tamano", c["tamano"], "|", c["miembros"][0],
              "| leidos", c["leidos"], "de", c["posibles"],
              "| en cola", c["en_cola_sin_leer"], "| fuera", c["fuera_de_cola"],
              "|", c["estado"])


if __name__ == "__main__":
    main()
