# -*- coding: utf-8 -*-
r"""_auditor_v104_ciega.py . AUDITOR DE LA VUELTA 104, RELECTURA CIEGA.

Vuelca, para cada uno de los 48 pares del barrido de la TAREA 4.2, el
paso_casado de la madre LEIDO HOY de dataset/nodos/, mas el titulo, el
entregable y los pasos del hijo. NO imprime el veredicto del ejecutor
(OBJETO / NO_OBJETO), ni su verbo, ni su objeto, ni su motivo, ni la
direccion_leida, ni la razon del registro: eso va al fichero REVEAL, que
se abre DESPUES de adjudicar.

USO:
  python docs/loop/_auditor_v104_ciega.py blind  > docs/loop/_auditor_v104_ciega_blind.txt
  python docs/loop/_auditor_v104_ciega.py reveal > docs/loop/_auditor_v104_ciega_reveal.txt
"""
import io, json, os, sys, re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
T1 = os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO1_V96.jsonl")
T2 = os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO2_V97.jsonl")
NODOS = os.path.join(RAIZ, "dataset", "nodos")
TRAMO1_PUESTOS = [1, 2, 4, 6, 8, 9, 14, 17, 18, 20, 21, 24, 25, 38, 39]

def leer(p):
    return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]

def efectiva(d):
    ks = sorted([k for k in d if k.startswith("correccion_v")],
                key=lambda k: int(re.findall(r"\d+", k)[0]))
    v = d.get("direccion_leida")
    for k in ks:
        c = d[k]
        if c.get("campo_corregido") == "direccion_leida":
            v = c.get("valor_nuevo")
    return v

def nodo(nid):
    return json.load(io.open(os.path.join(NODOS, nid + ".json"), encoding="utf-8"))

filas = []
for d in leer(T1):
    if d["puesto_tramo"] in TRAMO1_PUESTOS:
        filas.append(("TRAMO1", d))
for d in leer(T2):
    if d.get("direccion_leida"):   # RESUELTA en la lectura original
        filas.append(("TRAMO2", d))

modo = sys.argv[1] if len(sys.argv) > 1 else "blind"
out = io.StringIO()
out.write("MODO %s . %d pares\n" % (modo.upper(), len(filas)))
for tramo, d in filas:
    p = d["puesto_tramo"]; m = d["madre_de_la_bolsa"]; h = d["hijo_de_la_bolsa"]
    nm = nodo(m); nh = nodo(h)
    pasos = nm.get("pasos_accionables") or []
    pc = d.get("paso_casado")
    texto = pasos[pc-1] if isinstance(pc, int) and 1 <= pc <= len(pasos) else "(sin paso_casado utilizable: %r)" % pc
    out.write("\n" + "="*96 + "\nPUESTO %d (%s)  madre=%s  hijo=%s  paso_casado=%s\n" % (p, tramo, m, h, pc))
    out.write("PASO CASADO (leido hoy del nodo): %s\n" % texto)
    out.write("TODOS LOS PASOS DE LA MADRE:\n")
    for i, s in enumerate(pasos, 1):
        out.write("   %d) %s\n" % (i, s))
    out.write("HIJO titulo_concepto: %s\n" % nh.get("titulo_concepto"))
    out.write("HIJO entregable_esperado: %s\n" % nh.get("entregable_esperado"))
    out.write("HIJO pasos_accionables:\n")
    for i, s in enumerate(nh.get("pasos_accionables") or [], 1):
        out.write("   %d) %s\n" % (i, s))
    out.write("MADRE entregable_esperado: %s\n" % nm.get("entregable_esperado"))
    if modo == "reveal":
        out.write("--- REVEAL ---\n")
        out.write("direccion_leida ORIGINAL: %s\n" % d.get("direccion_leida"))
        out.write("direccion EFECTIVA hoy  : %s\n" % efectiva(d))
        out.write("razon ORIGINAL: %s\n" % (d.get("razon") or "")[:1200])
        for k in [k for k in d if k.startswith("correccion_v")]:
            out.write("%s: %s\n" % (k, json.dumps(d[k], ensure_ascii=False)[:1500]))
sys.stdout.write(out.getvalue())
