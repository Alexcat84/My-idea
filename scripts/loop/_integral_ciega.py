# -*- coding: utf-8 -*-
r"""_integral_ciega.py . LA CIEGA FINAL DE LA AUDITORIA INTEGRAL (9 sep 2026),
PASO 2.g: 20 FUSIONES AL AZAR CONTRA SU TABLA DE PERDIDAS Y REPARTO, Y 20
ENLACES DE LA FASE 04 CONTRA SU LECTURA REGISTRADA, CON SEMILLA ESCRITA Y LAS
CLASES DECLARADAS ANTES DE MIRAR.

LAS DOS MITADES, Y QUE SE DECLARA EN CADA UNA:

  FUSIONES. Universo: las entradas `actos` de los planes sellados
  `docs/loop/PLAN_V*.json` cuyo superviviente sigue VIVO en el grafo y cuyos
  absorbidos siguen en el grafo como DEPRECADOS (o sea, cuya fusion se
  ejecuto y cuyo texto absorbido se conserva). Se sortean 20 actos con la
  semilla. La salida CIEGA trae, por acto, los pasos y condiciones DE HOY del
  superviviente y los pasos y condiciones del absorbido (el texto del nodo
  deprecado). El lector declara, por absorbido, UNA clase:
     ENTERO       . todo lo que el absorbido decia esta en el superviviente,
                    literal o cubierto por un paso equivalente;
     CON PERDIDA  . algo del absorbido no esta en el superviviente.
  El DESTAPE trae lo que el plan dice: `perdidas` no vacia para ese absorbido
  (o una perdida cuyo `donde` lo nombra) es CON PERDIDA; si no, ENTERO. El
  reparto (CUBIERTO, APPEND, INCISO) se imprime en el destape como prueba.

  ENLACES. Universo: `docs/plan/OP_E_06_DIRECCION_V90.jsonl` y
  `docs/plan/OP_E_07_DIRECCION_V94.jsonl` (madre e hijo por puesto), los pares
  cuyos dos nodos siguen vivos. Se sortean 20. La salida CIEGA trae los dos
  nodos en orden BARAJADO como X e Y, con titulo, resumen y pasos, sin la
  palabra madre ni hijo. El lector declara cual es la MADRE (el que trae el
  procedimiento del que el otro es una linea). El DESTAPE trae la direccion
  registrada.

LA GUARDA DE FUGA: antes de escribir, se comprueba que ningun texto del destape
(las clases esperadas, la palabra madre e hijo junto a un id) aparece en la
salida ciega.

USO:
  python scripts/loop/_integral_ciega.py --aislar --semilla 20260909
  (el lector escribe docs/loop/SALIDA_integral_CIEGA_DECLARACIONES.json)
  python scripts/loop/_integral_ciega.py --cotejar
"""
import argparse
import glob
import io
import json
import os
import random
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
CIEGA = os.path.join(LOOP, "SALIDA_integral_CIEGA.txt")
DESTAPE = os.path.join(LOOP, "SALIDA_integral_CIEGA_DESTAPE.json")
DECL = os.path.join(LOOP, "SALIDA_integral_CIEGA_DECLARACIONES.json")
COTEJO = os.path.join(LOOP, "SALIDA_integral_CIEGA_COTEJO.txt")
E06 = os.path.join(RAIZ, "docs", "plan", "OP_E_06_DIRECCION_V90.jsonl")
E07 = os.path.join(RAIZ, "docs", "plan", "OP_E_07_DIRECCION_V94.jsonl")


def nodos():
    return json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]


def texto_nodo(n):
    L = []
    L.append("   titulo: %s" % n.get("titulo_concepto"))
    L.append("   resumen: %s" % str(n.get("resumen_teorico") or "")[:400])
    for i, p in enumerate(n.get("pasos_accionables") or [], 1):
        L.append("   paso %d: %s" % (i, p))
    for i, c in enumerate(n.get("condiciones_activacion") or [], 1):
        L.append("   condicion %d: %s" % (i, c))
    return L


def universo_fusiones(N):
    out = []
    for p in sorted(glob.glob(os.path.join(LOOP, "PLAN_V*.json"))):
        try:
            d = json.load(io.open(p, encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(d, dict):
            continue
        for a in d.get("actos") or []:
            s = a.get("superviviente")
            abs_ = [x for x in (a.get("absorbidos") or []) if x in N and N[x].get("deprecado")]
            if not s or s not in N or N[s].get("deprecado") or not abs_:
                continue
            out.append((os.path.basename(p), a, abs_))
    return out


def universo_enlaces(N):
    out = []
    for ruta in (E06, E07):
        for l in io.open(ruta, encoding="utf-8"):
            if not l.strip():
                continue
            d = json.loads(l)
            m, h = d.get("madre"), d.get("hijo")
            if m in N and h in N and not N[m].get("deprecado") and not N[h].get("deprecado"):
                out.append((os.path.basename(ruta), d))
    return out


def aislar(semilla):
    N = nodos()
    rnd = random.Random(semilla)
    UF = universo_fusiones(N)
    UE = universo_enlaces(N)
    fus = rnd.sample(UF, 20)
    enl = rnd.sample(UE, 20)
    ciega = []
    destape = {"semilla": semilla, "universo_fusiones": len(UF), "universo_enlaces": len(UE), "fusiones": [], "enlaces": []}
    ciega.append("CIEGA FINAL DE LA AUDITORIA INTEGRAL (9 sep 2026). SEMILLA %d, ESCRITA ANTES DE SORTEAR." % semilla)
    ciega.append("universo de fusiones: %d actos ejecutados con absorbido deprecado en el grafo | universo de enlaces: %d pares con los dos nodos vivos" % (len(UF), len(UE)))
    ciega.append("LAS CLASES SE DECLARAN EN SALIDA_integral_CIEGA_DECLARACIONES.json ANTES DE ABRIR EL DESTAPE.")
    ciega.append("")
    ciega.append("=" * 78)
    ciega.append("MITAD 1: VEINTE FUSIONES. Por absorbido: ENTERO o CON PERDIDA.")
    ciega.append("=" * 78)
    for k, (plan, a, abs_) in enumerate(fus, 1):
        s = a["superviviente"]
        ciega.append("")
        ciega.append("F%02d  superviviente: %s" % (k, s))
        ciega.extend(texto_nodo(N[s]))
        for x in abs_:
            ciega.append("  absorbido: %s" % x)
            ciega.extend(texto_nodo(N[x]))
        esperado = {}
        perd = a.get("perdidas") or []
        for x in abs_:
            con = [pp for pp in perd if isinstance(pp, dict) and x in str(pp.get("donde") or "")]
            esperado[x] = "CON PERDIDA" if con else "ENTERO"
        destape["fusiones"].append({"clave": "F%02d" % k, "plan": plan, "superviviente": s, "absorbidos": abs_,
                                    "esperado": esperado, "perdidas": perd,
                                    "reparto_pasos": a.get("pasos"), "reparto_condiciones": a.get("condiciones")})
    ciega.append("")
    ciega.append("=" * 78)
    ciega.append("MITAD 2: VEINTE ENLACES DE LA FASE 04. Por par: cual de X e Y es la MADRE.")
    ciega.append("=" * 78)
    for k, (reg, d) in enumerate(enl, 1):
        m, h = d["madre"], d["hijo"]
        par = [m, h]
        rnd.shuffle(par)
        ciega.append("")
        ciega.append("E%02d  puesto %s" % (k, d.get("puesto")))
        for et, nid in zip(("X", "Y"), par):
            ciega.append("  %s: %s" % (et, nid))
            ciega.extend(texto_nodo(N[nid]))
        destape["enlaces"].append({"clave": "E%02d" % k, "registro": reg, "puesto": d.get("puesto"), "X": par[0], "Y": par[1],
                                   "madre": m, "hijo": h, "esperado": "X" if par[0] == m else "Y"})
    texto = "\n".join(ciega) + "\n"
    # guarda de fuga
    fugas = []
    for f in destape["fusiones"]:
        for x, e in f["esperado"].items():
            if ("%s: %s" % (x, e)) in texto:
                fugas.append(x)
    for e in destape["enlaces"]:
        if ("madre: %s" % e["madre"]) in texto or ("hijo: %s" % e["hijo"]) in texto:
            fugas.append(e["madre"])
    if fugas:
        print("ROJO: fuga del destape en la ciega: %s. NO SE ESCRIBE NADA." % fugas[:5])
        return 1
    io.open(CIEGA, "w", encoding="utf-8", newline="\n").write(texto)
    io.open(DESTAPE, "w", encoding="utf-8", newline="\n").write(json.dumps(destape, ensure_ascii=False, indent=1))
    print("ESCRITA la ciega: %s (%d lineas) y el destape aparte: %s. NO ABRIR EL DESTAPE HASTA DECLARAR." % (CIEGA, len(ciega), DESTAPE))
    return 0


def cotejar():
    destape = json.load(io.open(DESTAPE, encoding="utf-8"))
    decl = json.load(io.open(DECL, encoding="utf-8"))
    L = []
    w = L.append
    w("COTEJO DE LA CIEGA FINAL (semilla %d). Filas: TODAS, no solo las discrepancias." % destape["semilla"])
    w("")
    w("MITAD 1: FUSIONES (por absorbido)")
    w("| clave | superviviente | absorbido | declarado | esperado (plan) | veredicto |")
    w("|---|---|---|---|---|---|")
    tot = ok = 0
    for f in destape["fusiones"]:
        for x in f["absorbidos"]:
            dcl = (decl.get("fusiones", {}).get(f["clave"], {}) or {}).get(x, "(sin declarar)")
            esp = f["esperado"][x]
            v = "COINCIDE" if dcl == esp else "DISCREPA"
            tot += 1
            ok += (v == "COINCIDE")
            w("| %s | %s | %s | %s | %s | %s |" % (f["clave"], f["superviviente"], x, dcl, esp, v))
    w("")
    w("CIFRA absorbidos cotejados: %d | COINCIDEN: %d | DISCREPAN: %d" % (tot, ok, tot - ok))
    w("")
    w("MITAD 2: ENLACES (la madre)")
    w("| clave | puesto | X | Y | declarado | esperado (registro) | veredicto |")
    w("|---|---|---|---|---|---|---|")
    tot2 = ok2 = 0
    for e in destape["enlaces"]:
        dcl = decl.get("enlaces", {}).get(e["clave"], "(sin declarar)")
        v = "COINCIDE" if dcl == e["esperado"] else "DISCREPA"
        tot2 += 1
        ok2 += (v == "COINCIDE")
        w("| %s | %s | %s | %s | %s | %s (madre %s) | %s |" % (e["clave"], e["puesto"], e["X"], e["Y"], dcl, e["esperado"], e["madre"], v))
    w("")
    w("CIFRA enlaces cotejados: %d | COINCIDEN: %d | DISCREPAN: %d" % (tot2, ok2, tot2 - ok2))
    w("")
    w("LAS DISCREPANCIAS, CON LO QUE EL PLAN O EL REGISTRO DICE:")
    n = 0
    for f in destape["fusiones"]:
        for x in f["absorbidos"]:
            dcl = (decl.get("fusiones", {}).get(f["clave"], {}) or {}).get(x, "(sin declarar)")
            if dcl != f["esperado"][x]:
                n += 1
                w("   %s %s: declarado %s, plan %s (%s); perdidas del plan: %s; reparto pasos: %s"
                  % (f["clave"], x, dcl, f["esperado"][x], f["plan"],
                     json.dumps([pp.get("donde") for pp in f["perdidas"] if isinstance(pp, dict)], ensure_ascii=False)[:200],
                     json.dumps((f["reparto_pasos"] or {}).get(x), ensure_ascii=False)[:200]))
    for e in destape["enlaces"]:
        dcl = decl.get("enlaces", {}).get(e["clave"], "(sin declarar)")
        if dcl != e["esperado"]:
            n += 1
            w("   %s puesto %s: declarado %s, registro %s (madre %s, hijo %s, %s)" % (e["clave"], e["puesto"], dcl, e["esperado"], e["madre"], e["hijo"], e["registro"]))
    if not n:
        w("   (ninguna)")
    texto = "\n".join(L) + "\n"
    io.open(COTEJO, "w", encoding="utf-8", newline="\n").write(texto)
    print(texto)
    return 0


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--aislar", action="store_true")
    ap.add_argument("--cotejar", action="store_true")
    ap.add_argument("--semilla", type=int, default=None)
    a = ap.parse_args()
    if a.aislar:
        if a.semilla is None:
            print("ROJO: la semilla se escribe antes de sortear (--semilla).")
            return 1
        return aislar(a.semilla)
    if a.cotejar:
        return cotejar()
    ap.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
