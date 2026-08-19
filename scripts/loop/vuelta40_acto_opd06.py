# -*- coding: utf-8 -*-
"""vuelta40_acto_opd06.py - OP-D-06 ABIERTA Y MEDIDA, ACTO POR ACTO.

ESTRICTAMENTE DE SOLO LECTURA. No funde nada, no toca un nodo, no escribe en el
archivo ni en el plan.

POR QUE EXISTE, y es un limite del instrumento hallado hoy y no una regla nueva.
`scripts/loop/vuelta39_acto.py --op OP-D-06` **ABORTA**: lee la nomina de
`OPERACIONES.jsonl`, encuentra **18 nodos**, calcula **153 pares posibles** y
declara **144 sin clase en el archivo**. Su salida entera queda sellada en
`docs/loop/SALIDA_V40_OPD06_ACTO.txt` porque el aborto es informacion, no ruido.

**Y NO ES QUE FALTEN 144 VEREDICTOS: ES QUE OP-D-06 NO ES UN ACTO.** El propio
plan lo dice en su titulo, `OP-D-06: LOS NUEVE ACTOS DE DOS`, y trae la tabla
`ADJUDICADO Y COMPLETADO. Los nueve pares` con los nueve pares y sus nueve
puestos. **Son NUEVE actos independientes de dos nodos cada uno**, no uno de
dieciocho: los pares CRUZADOS entre actos distintos no tienen veredicto porque
nunca fueron un par.

Este instrumento LEE ESA PARTICION DEL PLAN (no la inventa ni la teclea: la
extrae de la tabla sellada de `docs/plan/02_DESTEJIDOS.md`) y mide cada acto de
dos por separado, con la misma aritmetica del hermano mayor.

Uso: python scripts/loop/vuelta40_acto_opd06.py
"""
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
NODOS = os.path.join(RAIZ, "dataset", "nodos")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
MD = os.path.join(RAIZ, "docs", "plan", "02_DESTEJIDOS.md")
CAMPOS = ("nodos_previos", "nodos_siguientes")
OPUESTO = {"nodos_previos": "nodos_siguientes", "nodos_siguientes": "nodos_previos"}

# LA MISMA VARA DEL HERMANO MAYOR, copiada literal de vuelta39_acto.py: la prueba
# de 9.3.1 busca el VERBO de adjudicacion, no el id. Buscar el id daria SI casi
# siempre, porque las razones empiezan por "REPITE con <id>" y eso no adjudica
# nada. La vara se copia en vez de reinventarse para que las dos medidas sean
# comparables.
VERBOS_GANADOR = ("GANA ", "GANA.", " gana ", "SOBREVIVE", "sobrevive",
                  "superviviente es", "EL SUPERVIVIENTE")

RE_FILA = re.compile(r"^\|\s*\*{0,2}(\d+)\*{0,2}\s*\|\s*`([a-z0-9_]+)`\s*con\s*`([a-z0-9_]+)`\s*\|")


def particion_del_plan():
    """Los nueve pares, LEIDOS de la tabla sellada y no tecleados aqui."""
    texto = io.open(MD, encoding="utf-8").read()
    ini = texto.index("ADJUDICADO Y COMPLETADO. Los nueve pares")
    trozo = texto[ini:ini + 4000]
    pares = []
    for linea in trozo.splitlines():
        m = RE_FILA.match(linea)
        if m:
            pares.append((int(m.group(1)), m.group(2), m.group(3)))
    return pares


def nodo(nid):
    return json.loads(io.open(os.path.join(NODOS, nid + ".json"),
                              encoding="utf-8").read())


def main():
    pares = particion_del_plan()
    ops = [json.loads(l) for l in io.open(OPS, encoding="utf-8") if l.strip()]
    op = next(o for o in ops if o["id_op"] == "OP-D-06")
    nomina = list(op["nodos"])

    print("OP-D-06 ABIERTA Y MEDIDA, ACTO POR ACTO. 19 ago 2026, vuelta 40")
    print("=" * 78)
    print("LA PARTICION, leida de la tabla sellada de docs/plan/02_DESTEJIDOS.md:")
    print("  actos hallados en la tabla: %d" % len(pares))
    print("  nodos en la nomina de OPERACIONES.jsonl: %d" % len(nomina))
    planos = [x for _p, a, b in pares for x in (a, b)]
    print("  nodos nombrados por la tabla: %d" % len(planos))
    faltan = sorted(set(nomina) - set(planos))
    sobran = sorted(set(planos) - set(nomina))
    print("  GUARDA, la tabla y la nomina son el MISMO conjunto: %s "
          "(faltan %s, sobran %s)"
          % ("OK" if not faltan and not sobran else "ROJO", faltan, sobran))
    print("")
    print("POR QUE ESTO Y NO EL HERMANO MAYOR: vuelta39_acto.py --op OP-D-06 aborta")
    print("con 144 pares sin clase sobre 153 posibles. NO faltan 144 veredictos:")
    print("es que los pares CRUZADOS entre actos distintos nunca fueron un par.")
    print("OP-D-06 son NUEVE actos de dos, y asi lo dice su propio titulo.")

    # los veredictos del archivo, indexados por par no ordenado
    clases = {}
    for l in io.open(VER, encoding="utf-8"):
        if not l.strip():
            continue
        v = json.loads(l)
        clases[frozenset((v["nodo_a"], v["nodo_b"]))] = v

    # el cableado, resuelto por alias (P.1) y sin contarse a si mismo (9.14)
    G = {}
    for nombre in sorted(os.listdir(NODOS)):
        if nombre.endswith(".json"):
            d = nodo(nombre[:-5])
            G[d["node_id"]] = d
    ALIAS = {a: k for k, v in G.items() for a in (v.get("ids_alias") or [])}

    def res(x):
        s = set()
        while x in ALIAS and x not in s:
            s.add(x)
            x = ALIAS[x]
        return x

    grado = {}
    for nid, d in G.items():
        if d.get("deprecado"):
            continue
        for c in CAMPOS:
            for y in (d.get(c) or []):
                t = res(y)
                if t != nid:
                    grado[t] = grado.get(t, 0) + 1

    print("")
    filas = []
    for puesto, a, b in pares:
        v = clases.get(frozenset((a, b)))
        da, db = nodo(a), nodo(b)
        # aristas propias sin reciproco, que es lo que costaria elegir al otro
        def cojas(x, y):
            n = 0
            for c in CAMPOS:
                for z in (G[x].get(c) or []):
                    t = res(z)
                    if t == x or t not in G:
                        continue
                    if x not in (G[t].get(OPUESTO[c]) or []):
                        n += 1
            return n
        filas.append({
            "puesto": puesto, "a": a, "b": b,
            "clase": (v or {}).get("clase", "SIN VEREDICTO"),
            "pasos": (len(da.get("pasos_accionables") or []),
                      len(db.get("pasos_accionables") or [])),
            "fuente_igual": da.get("fuente") == db.get("fuente"),
            "grado": (grado.get(a, 0), grado.get(b, 0)),
            "cojas": (cojas(a, b), cojas(b, a)),
            "vivos": (not da.get("deprecado"), not db.get("deprecado")),
            "razon": (v or {}).get("razon", ""),
        })

    print("=" * 78)
    print("LOS NUEVE ACTOS, MEDIDOS UNO A UNO")
    print("=" * 78)
    print("%-7s %-5s %-44s %-44s %-7s %-9s %-9s %s"
          % ("puesto", "clase", "nodo A", "nodo B", "pasos", "cableado", "cojas",
             "misma fuente"))
    for f in filas:
        print("%-7d %-5s %-44s %-44s %-7s %-9s %-9s %s"
              % (f["puesto"], f["clase"], f["a"][:44], f["b"][:44],
                 "%d/%d" % f["pasos"], "%d/%d" % f["grado"],
                 "%d/%d" % f["cojas"], "SI" if f["fuente_igual"] else "NO"))
    print("")
    reparto = {}
    for f in filas:
        reparto[f["clase"]] = reparto.get(f["clase"], 0) + 1
    print("  reparto de clases: %s" % reparto)
    print("  actos con los DOS nodos vivos: %d de %d"
          % (sum(1 for f in filas if all(f["vivos"])), len(filas)))
    print("  actos de la MISMA fuente: %d de %d"
          % (sum(1 for f in filas if f["fuente_igual"]), len(filas)))
    print("")
    print("=" * 78)
    print("9.3.1 SOBRE LOS PARES A: quien nombra ganador en su razon")
    print("=" * 78)
    for f in filas:
        if f["clase"] != "A":
            print("  %-6d %-5s %s con %s   (la prueba de 9.3.1 solo corre sobre A)"
                  % (f["puesto"], f["clase"], f["a"], f["b"]))
            continue
        r = f["razon"]
        nombra = ("SI" if any(w in r for w in VERBOS_GANADOR) else "NO")
        print("  %-6d A     %s con %s   nombra ganador: %s"
              % (f["puesto"], f["a"], f["b"], nombra))
        print("        razon (%d caracteres): %s" % (len(r), r[:220]))
    print("")
    print("=" * 78)
    print("LO QUE FALTA, y por que no se hizo hoy")
    print("=" * 78)
    print("Cada uno de los nueve es UN ACTO que pide su P.5, su P.8 y su plan")
    print("sellado antes de fundirse, mas los tres cruces con la fase 01 que el")
    print("propio plan avisa (producto_unico_superior y propuesta_gasto_capital en")
    print("OP-F-03, future_scenarios_planning en OP-F-02: en los tres manda fuente")
    print("primero). Esta corrida DEJA LA OPERACION ABIERTA Y MEDIDA, no la")
    print("ejecuta, y lo dice en vez de dar por hecho lo que no se hizo.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
