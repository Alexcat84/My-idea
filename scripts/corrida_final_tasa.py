# -*- coding: utf-8 -*-
"""La TASA REAL de hallazgos por plan (decision del fundador, 10 oct 2026, noche, punto 3; acta de la corrida final).

No es aprobado o suspenso: es el dato para decidir la beta. Junta varias corridas de la medicion (cada una con sus 14
planes redactados de nuevo, dos jueces y arbitro, sus trampas) y cuenta lo SOSTENIDO por el arbitro en las salidas
reales (las trampas no cuentan), por plan y por tipo:
  - hallazgos por plan redactado: media con su intervalo al 95 % de Poisson exacto (Garwood) y, porque las corridas
    del mismo plan no son independientes, tambien con un bootstrap que remuestrea los 14 planes;
  - planes redactados con al menos un hallazgo: proporcion con su intervalo de Wilson al 95 %;
  - el detalle por plan (sus corridas) y la validez (trampas cazadas en cada corrida).

  python scripts/corrida_final_tasa.py <dir_juez_1> <dir_juez_2> ... [--salida informe.json]
  (cada dir con claves_A/claves.json y veredictos_A/resumen.json, como los deja corrida_final_juez_api.ts)
"""
import json
import math
import random
import sys

TIPOS = ("contrario", "invencion", "procedencia")


def _j(p):
    return json.load(open(p, encoding="utf-8"))


def wilson(k, n, z=1.959964):
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    c = (p + z * z / (2 * n)) / (1 + z * z / n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return max(0.0, c - h), min(1.0, c + h)


def _gamma_inc_inv(k, p):
    """Cuantil de la Gamma(k, 1) por biseccion (sin scipy): lo usa el intervalo exacto de Poisson."""
    if k <= 0:
        return 0.0

    def cdf(x):
        # P(Gamma(k,1) <= x) = 1 - P(Poisson(x) <= k-1) para k entero
        s, t = 0.0, math.exp(-x)
        for i in range(int(k)):
            s += t
            t *= x / (i + 1)
        return 1 - s

    lo, hi = 0.0, max(10.0, 10 * k)
    for _ in range(200):
        mid = (lo + hi) / 2
        if cdf(mid) < p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def poisson_media(total, n):
    """Intervalo exacto (Garwood) al 95 % de la media por unidad: total de eventos en n unidades."""
    lo = 0.0 if total == 0 else _gamma_inc_inv(total, 0.025)
    hi = _gamma_inc_inv(total + 1, 0.975)
    return lo / n, hi / n


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    salida = sys.argv[sys.argv.index("--salida") + 1] if "--salida" in sys.argv else None
    if "--salida" in sys.argv:
        args = [a for a in args if a != salida]
    filas, validez = [], []
    for corrida, d in enumerate(args, 1):
        claves = {c["paquete"]: c for c in _j(d + "/claves_A/claves.json")["claves"]}
        res = _j(d + "/veredictos_A/resumen.json")
        validez.append({"corrida": corrida, "dir": d, "trampas": res["trampas"],
                        "todas_cazadas": all(t.get("cazada_juez") or t.get("cazada_relectura") for t in res["trampas"].values())})
        for p in res["por_plan"]:
            c = claves[p["paquete"]]
            if c["origen"] != "real":
                continue
            cuenta = {t: sum(1 for s in p["sostenidos"] if s["clase"] == t) for t in TIPOS}
            filas.append({"corrida": corrida, "plan_id": c["ref"]["plan_id"], "dominio": c["ref"]["dominio"],
                          "sostenidos": p["sostenidos"], **cuenta})
    n = len(filas)
    planes = sorted({f["plan_id"] for f in filas})
    rng = random.Random(20261010)
    out = {"corridas": len(args), "planes_redactados": n, "planes_distintos": len(planes), "validez": validez, "por_tipo": {}}
    for t in TIPOS + ("contrario+invencion",):
        val = (lambda f: f["contrario"] + f["invencion"]) if t == "contrario+invencion" else (lambda f, t=t: f[t])
        total = sum(val(f) for f in filas)
        con = sum(1 for f in filas if val(f) > 0)
        lo, hi = poisson_media(total, n)
        # bootstrap por plan: remuestrea los planes (con sus corridas) 5.000 veces
        por_plan = {p: [val(f) for f in filas if f["plan_id"] == p] for p in planes}
        medias = []
        for _ in range(5000):
            m = [x for p in (rng.choice(planes) for _ in planes) for x in por_plan[p]]
            medias.append(sum(m) / len(m))
        medias.sort()
        wl, wh = wilson(con, n)
        out["por_tipo"][t] = {
            "total": total,
            "media_por_plan": round(total / n, 3),
            "ic95_poisson": [round(lo, 3), round(hi, 3)],
            "ic95_bootstrap_por_plan": [round(medias[124], 3), round(medias[4874], 3)],
            "planes_con_alguno": con,
            "proporcion_con_alguno": round(con / n, 3),
            "ic95_wilson": [round(wl, 3), round(wh, 3)],
        }
    out["por_plan"] = [{"plan_id": p, "dominio": next(f["dominio"] for f in filas if f["plan_id"] == p),
                        "por_corrida": [{t: f[t] for t in TIPOS} for f in filas if f["plan_id"] == p],
                        "sostenidos": [s for f in filas if f["plan_id"] == p for s in f["sostenidos"]]} for p in planes]
    for t, v in out["por_tipo"].items():
        print("%-20s total %3d | media/plan %.3f IC95 Poisson %.3f-%.3f, bootstrap %.3f-%.3f | planes con alguno %d de %d (%.0f %%, Wilson %.0f-%.0f %%)"
              % (t, v["total"], v["media_por_plan"], *v["ic95_poisson"], *v["ic95_bootstrap_por_plan"], v["planes_con_alguno"], n,
                 100 * v["proporcion_con_alguno"], 100 * v["ic95_wilson"][0], 100 * v["ic95_wilson"][1]))
    print("validez:", [(v["corrida"], v["todas_cazadas"]) for v in validez])
    if salida:
        json.dump(out, open(salida, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
