# -*- coding: utf-8 -*-
"""Tablas del reporte: cobertura de la fase 0, costes medidos del piloto y
las dos proyecciones de la campania (solo contrarios; contrarios mas anadidos).

Modelo de la proyeccion (todo con cifras medidas en Reason):
  coste_libro = pasos * (traduccion_por_item + p1_por_item + tasa_marcado * p2_por_item)
              + prueba_de_recall_fija
  - solo contrarios: p1 y tasa del intento 1 (una marca), p2 por item del intento 3
    (el contexto de la pasada 2 es el mismo; la instruccion de cuatro veredictos
    apenas cambia la salida).
  - contrarios mas anadidos: p1 y tasa del intento 3 (dos marcas), p2 del intento 3.
  - prueba de recall fija por libro: generar sinteticos + pasar 28 sinteticos por
    las dos pasadas (se supone que se marcan todos, como en Reason).
  - tiempo de pared: suma de pared de las llamadas / 4 procesos a la vez.
Supuesto declarado: el coste por paso de Reason vale para los demas libros. La
pasada 2 lleva capitulos enteros; un libro con capitulos mas largos cuesta mas.
"""
import json, os, collections
import comun as C

def llamadas():
    return [json.loads(l) for l in open(C.LOG_COSTES, encoding="utf-8")]

def agrega(fil):
    return {"n": len(fil), "usd": sum(f["usd"] for f in fil), "turnos": sum(f["turnos"] or 0 for f in fil),
            "api_s": sum(f["duracion_s"] for f in fil), "pared_s": sum(f["pared_s"] for f in fil),
            "tin": sum(f["tokens_in"] for f in fil), "tout": sum(f["tokens_out"] for f in fil)}

def etapa(e):
    return agrega([f for f in llamadas() if f["etapa"] == e])

def main():
    r1 = json.load(open(os.path.join(C.PIL, "RECALL_i1.json"), encoding="utf-8"))
    r2 = json.load(open(os.path.join(C.PIL, "RECALL_i3.json"), encoding="utf-8"))
    n1, n2 = 419, 431
    tr = agrega([f for f in llamadas() if f["etapa"] in ("traduccion", "traduccion_i2")])
    p1a, p1b, p2 = etapa("pasada1_i1"), etapa("pasada1_i3"), etapa("pasada2_i3")
    p1_2, p2_2 = etapa("pasada1_i2"), etapa("pasada2_i2")
    gen = agrega([f for f in llamadas() if f["etapa"] == "sinteticos"])
    oro = etapa("oro")
    items_p2 = p2["n"]
    k = lambda a, n: {x: a[x] / n for x in ("usd", "turnos", "api_s", "pared_s")}
    tr_i = k(tr, n2)
    p1c_i, p1ca_i, p2_i = k(p1a, n1), k(p1b, n2), k(p2, items_p2)
    tasa_c, tasa_ca = r1["tasa_marcado_reales"], r2["tasa_marcado_reales"]
    def por_paso(p1_i, tasa):
        return {x: tr_i[x] + p1_i[x] + tasa * p2_i[x] for x in tr_i}
    pc, pca = por_paso(p1c_i, tasa_c), por_paso(p1ca_i, tasa_ca)
    fijo = {x: (gen[x] if x in gen else 0) + 28 * (tr_i[x] + p1ca_i[x] + p2_i[x]) for x in ("usd", "turnos", "api_s", "pared_s")}
    out = []
    w = out.append
    w("### Costes medidos del piloto (Opus 5.5 en todo)\n")
    w("| Etapa | Llamadas | USD | Turnos | Tiempo de API (min) | Pared con 4 a la vez (min) | Tokens entrada | Tokens salida |")
    w("|---|---:|---:|---:|---:|---:|---:|---:|")
    for nom, a in (("Sinteticos (contrarios y anadidos)", gen), ("Traduccion de consultas", tr), ("Oro de busqueda (libro entero)", oro),
                   ("Pasada 1, intento 1 (una marca; superado)", p1a), ("Pasada 1, intento 2 (dos marcas; superado)", p1_2),
                   ("Pasada 2, intento 2 (superado)", p2_2), ("Pasada 1, intento 3 (dos marcas; final)", p1b), ("Pasada 2, intento 3 (final)", p2)):
        w(f"| {nom} | {a['n']} | {a['usd']:.2f} | {a['turnos']} | {a['api_s']/60:.1f} | {a['pared_s']/60/4:.1f} | {a['tin']:,} | {a['tout']:,} |")
    tot = agrega(llamadas())
    w(f"| **Total del piloto** | {tot['n']} | **{tot['usd']:.2f}** | {tot['turnos']} | {tot['api_s']/60:.1f} | {tot['pared_s']/60/4:.1f} | {tot['tin']:,} | {tot['tout']:,} |")
    w("")
    w("### Coste por paso y por libro (Reason)\n")
    w("| Modo | Tasa de marcado (reales) | USD por paso | Turnos por paso | Segundos de pared por paso (4 a la vez) | USD Reason (403 pasos + prueba fija) | Horas de pared Reason |")
    w("|---|---:|---:|---:|---:|---:|---:|")
    for nom, pp, tasa in (("Solo contrarios", pc, tasa_c), ("Contrarios mas anadidos", pca, tasa_ca)):
        usd = 403 * pp["usd"] + fijo["usd"]; hr = (403 * pp["pared_s"] + fijo["pared_s"]) / 4 / 3600
        w(f"| {nom} | {tasa:.1%} | {pp['usd']:.3f} | {pp['turnos']:.2f} | {pp['pared_s']/4:.1f} | {usd:.2f} | {hr:.2f} |")
    w(f"\nPrueba de recall fija por libro (generar sinteticos y pasar 28 por las dos pasadas): {fijo['usd']:.2f} USD, {fijo['turnos']:.0f} turnos.\n")
    tabla = json.load(open(os.path.join(C.FID, "INVENTARIO_LIBROS.json"), encoding="utf-8"))
    w("### Cobertura (fase 0), en orden de riesgo\n")
    w("| Orden | Tramo | Libro (campo `fuente`) | Nodos vivos | Pasos | Verificables | NO verificables | Texto usado | Nota |")
    w("|---:|---|---|---:|---:|---:|---:|---|---|")
    for i, r in enumerate(tabla, 1):
        txt = "; ".join(os.path.basename(t) for t in r["texto"])
        w(f"| {i} | {r['tramo']} | {r['libro']} | {r['nodos']} | {r['pasos']} | {r['verificables']} | {r['no_verificables']} | {txt} | {r['nota']} |")
    w(f"| | | **Total** | **{sum(r['nodos'] for r in tabla)}** | **{sum(r['pasos'] for r in tabla)}** | **{sum(r['verificables'] for r in tabla)}** | **{sum(r['no_verificables'] for r in tabla)}** | | |")
    w("")
    for nom, pp in (("SOLO CONTRARIOS", pc), ("CONTRARIOS MAS ANADIDOS", pca)):
        w(f"### Proyeccion: {nom}\n")
        w("| Orden | Tramo | Libro | Pasos | USD | Turnos | Horas de pared (4 a la vez) | USD acumulado |")
        w("|---:|---|---|---:|---:|---:|---:|---:|")
        acc = 0; tt = collections.Counter()
        for i, r in enumerate(tabla, 1):
            s = r["pasos"]
            usd = s * pp["usd"] + fijo["usd"]; tur = s * pp["turnos"] + fijo["turnos"]
            hr = (s * pp["pared_s"] + fijo["pared_s"]) / 4 / 3600
            acc += usd; tt["usd"] += usd; tt["tur"] += tur; tt["hr"] += hr; tt["pasos"] += s
            tt[f"usd{r['tramo']}"] += usd; tt[f"hr{r['tramo']}"] += hr; tt[f"p{r['tramo']}"] += s
            w(f"| {i} | {r['tramo']} | {r['libro'][:80]} | {s} | {usd:.2f} | {tur:.0f} | {hr:.2f} | {acc:.2f} |")
        w(f"| | | **Total** | **{tt['pasos']}** | **{tt['usd']:.2f}** | **{tt['tur']:.0f}** | **{tt['hr']:.1f}** | |")
        w("")
        w("| Tramo | Pasos | USD | Horas de pared |")
        w("|---|---:|---:|---:|")
        for t, nomt in ((1, "1 seguridad y salud"), (2, "2 legal y dinero"), (3, "3 el resto")):
            w(f"| {nomt} | {tt[f'p{t}']} | {tt[f'usd{t}']:.2f} | {tt[f'hr{t}']:.1f} |")
        w("")
    open(os.path.join(C.WORK, "tablas.md"), "w", encoding="utf-8").write(C.sanea("\n".join(out)))
    print("\n".join(out))

if __name__ == "__main__":
    main()
