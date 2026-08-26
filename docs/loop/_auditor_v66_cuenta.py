# -*- coding: utf-8 -*-
"""Cuenta independiente del auditor, vuelta 66 (Fable 5).

Verifica las TRES fusiones del lote B del tramo unico de OP-U-02 (actos 7,
8 y 9) contra el arbol VIVO y contra el arbol de APERTURA (eaa33c77), sin
reusar los verificadores del ejecutor. Cada comprobacion imprime OK o FALLO
con su detalle. El plan sellado (PLAN_V66_OPU02_LOTE_B.json) es el contrato;
el grafo es el estado. Ademas comprueba que los tres actos DECLARADOS Y NO
FUNDIDOS (5, 10 y 11) quedaron con sus nodos INTACTOS al byte.
"""
import json, subprocess, sys, itertools, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

APERTURA = "eaa33c77"

fallos = []
n_ok = 0
def check(nombre, cond, detalle=""):
    global n_ok
    if cond:
        n_ok += 1
        print("OK   ", nombre)
    else:
        fallos.append(nombre)
        print("FALLO", nombre, "|", detalle)

def vivo(nid):
    return json.load(open("dataset/nodos/%s.json" % nid, encoding="utf-8"))

def apertura(nid):
    raw = subprocess.run(["git", "show", "%s:dataset/nodos/%s.json" % (APERTURA, nid)],
                         capture_output=True).stdout
    return json.loads(raw)

plan = json.load(open("docs/loop/PLAN_V66_OPU02_LOTE_B.json", encoding="utf-8"))

ESPERADO = {
    7: dict(sup="six_sigma_dmaic", pasos=12, cond=8, piezas=38,
            append=11, cubierto=27, inciso=0, perdidas=11),
    8: dict(sup="cierre_segun_complejidad_venta", pasos=12, cond=7, piezas=29,
            append=11, cubierto=17, inciso=1, perdidas=8),
    9: dict(sup="marco_analisis_mercado_cadena_suministro", pasos=21, cond=7, piezas=40,
            append=21, cubierto=18, inciso=1, perdidas=12),
}

todos_absorbidos = []

for acto in plan["actos"]:
    o = acto["orden"]
    e = ESPERADO[o]
    sup, absorbidos = acto["superviviente"], acto["absorbidos"]
    check("acto %d: superviviente es %s" % (o, e["sup"]), sup == e["sup"], sup)
    check("acto %d: 5 absorbidos" % o, len(absorbidos) == 5, str(len(absorbidos)))
    todos_absorbidos += absorbidos

    s_hoy, s_ap = vivo(sup), apertura(sup)
    check("acto %d: superviviente VIVO" % o, not s_hoy.get("deprecado"))
    check("acto %d: %d pasos hoy" % (o, e["pasos"]),
          len(s_hoy["pasos_accionables"]) == e["pasos"], str(len(s_hoy["pasos_accionables"])))
    check("acto %d: %d condiciones hoy" % (o, e["cond"]),
          len(s_hoy["condiciones_activacion"]) == e["cond"], str(len(s_hoy["condiciones_activacion"])))

    # los pasos y condiciones VIEJOS del superviviente: prefijo intacto salvo INCISO
    incisos = {}
    for m, rep in acto["pasos"].items():
        for idx, v in rep.items():
            if isinstance(v, str) and v.startswith("INCISO:"):
                destino, literal, prefijo = v.split("|")[0], v.split("|")[1], v.split("|")[2]
                incisos[int(destino.split(":")[1])] = (m, int(idx), literal, prefijo)
    viejos_p = s_ap["pasos_accionables"]
    for i, viejo in enumerate(viejos_p, 1):
        nuevo = s_hoy["pasos_accionables"][i - 1]
        if i in incisos:
            m, idx, literal, prefijo = incisos[i]
            check("acto %d: paso %d = viejo mas inciso" % (o, i),
                  nuevo.startswith(viejo) and nuevo.endswith(prefijo + literal),
                  nuevo[:80])
            texto_origen = apertura(m)["pasos_accionables"][idx - 1]
            check("acto %d: inciso del paso %d VERBATIM del absorbido %s" % (o, i, m),
                  literal in texto_origen, literal[:60])
        else:
            check("acto %d: paso %d del superviviente INTACTO" % (o, i), nuevo == viejo)
    viejos_c = s_ap["condiciones_activacion"]
    for i, viejo in enumerate(viejos_c, 1):
        check("acto %d: condicion %d del superviviente INTACTA" % (o, i),
              s_hoy["condiciones_activacion"][i - 1] == viejo)

    # cada APPEND VERBATIM al texto de apertura de su absorbido, y cobertura exacta
    n_app = n_cub = n_inc = 0
    pasos_nuevos = s_hoy["pasos_accionables"][len(viejos_p):]
    cond_nuevas = s_hoy["condiciones_activacion"][len(viejos_c):]
    pend_p, pend_c = list(pasos_nuevos), list(cond_nuevas)
    for m in absorbidos:
        m_ap = apertura(m)
        rep_p, rep_c = acto["pasos"][m], acto["condiciones"][m]
        check("acto %d: reparto de %s cubre EXACTO sus pasos" % (o, m),
              sorted(int(k) for k in rep_p) == list(range(1, len(m_ap["pasos_accionables"]) + 1)),
              str(sorted(rep_p.keys())))
        check("acto %d: reparto de %s cubre EXACTO sus condiciones" % (o, m),
              sorted(int(k) for k in rep_c) == list(range(1, len(m_ap["condiciones_activacion"]) + 1)),
              str(sorted(rep_c.keys())))
        for idx, v in sorted(rep_p.items(), key=lambda kv: int(kv[0])):
            texto = m_ap["pasos_accionables"][int(idx) - 1]
            if v == "APPEND":
                n_app += 1
                check("acto %d: APPEND paso %s de %s VERBATIM" % (o, idx, m),
                      texto in pend_p, texto[:60])
                if texto in pend_p: pend_p.remove(texto)
            elif v.startswith("CUBIERTO"):
                n_cub += 1
            elif v.startswith("INCISO"):
                n_inc += 1
        for idx, v in sorted(rep_c.items(), key=lambda kv: int(kv[0])):
            texto = m_ap["condiciones_activacion"][int(idx) - 1]
            if v == "APPEND":
                n_app += 1
                check("acto %d: APPEND condicion %s de %s VERBATIM" % (o, idx, m),
                      texto in pend_c, texto[:60])
                if texto in pend_c: pend_c.remove(texto)
            elif v.startswith("CUBIERTO"):
                n_cub += 1
            elif v.startswith("INCISO"):
                n_inc += 1
    check("acto %d: cero pasos nuevos sin origen" % o, not pend_p, str(pend_p)[:80])
    check("acto %d: cero condiciones nuevas sin origen" % o, not pend_c, str(pend_c)[:80])
    check("acto %d: APPEND %d" % (o, e["append"]), n_app == e["append"], str(n_app))
    check("acto %d: CUBIERTO %d" % (o, e["cubierto"]), n_cub == e["cubierto"], str(n_cub))
    check("acto %d: INCISO %d" % (o, e["inciso"]), n_inc == e["inciso"], str(n_inc))
    check("acto %d: piezas %d" % (o, e["piezas"]), n_app + n_cub + n_inc == e["piezas"],
          str(n_app + n_cub + n_inc))
    check("acto %d: perdidas %d en campo propio" % (o, e["perdidas"]),
          len(acto["perdidas"]) == e["perdidas"], str(len(acto["perdidas"])))

    # los 5 absorbidos: deprecados hoy, texto INTACTO al byte contra apertura
    # (AVERIA PROPIA DECLARADA: la primera version leia x.get("id") donde el
    # esquema usa node_id, y dio 15 fallos falsos; la misma especie que el
    # acta 64 declaro con id contra id_op. Corregida antes de publicar.)
    mo = s_hoy.get("merged_originals") or []
    mo_ids = [x.get("node_id") if isinstance(x, dict) else x for x in mo]
    for m in absorbidos:
        m_hoy, m_ap = vivo(m), apertura(m)
        check("acto %d: %s deprecado hoy" % (o, m), bool(m_hoy.get("deprecado")))
        check("acto %d: %s conserva pasos/condiciones/resumen/entregable INTACTOS" % (o, m),
              all(m_hoy.get(k) == m_ap.get(k) for k in
                  ("pasos_accionables", "condiciones_activacion", "resumen", "entregable_esperado")))
        check("acto %d: %s cargado en merged_originals del superviviente" % (o, m), m in mo_ids)

# los tres DECLARADOS: ni un nodo tocado
for d in plan["declarados_y_no_fundidos"]:
    o = d["acto"]
    for m in d.get("miembros", []):
        try:
            intacto = vivo(m) == apertura(m)
        except Exception as ex:
            intacto, detalle = False, str(ex)
        check("declarado %d: %s INTACTO al byte contra apertura" % (o, m), intacto)

# universo: 15 muertos, cero referencias vivas a absorbidos, cero auto-aristas
# (AVERIA PROPIA DECLARADA: la primera version buscaba master["nodes"] como
# lista con clave id; el esquema real es master["nodos"], dict por node_id.
# Cazada por el propio traceback antes de publicar cifra alguna.)
master = json.load(open("dataset/metadata/master_graph.json", encoding="utf-8"))
nodos = master["nodos"]
vivos = {nid: n for nid, n in nodos.items() if not n.get("deprecado")}
check("universo: 3247 vivos", len(vivos) == 3247, str(len(vivos)))
absset = set(todos_absorbidos)
check("15 absorbidos en total", len(absset) == 15, str(len(absset)))
check("los 15 muertos en el master", all(nodos[a].get("deprecado") for a in absset))
malas = auto = 0
for nid, n in vivos.items():
    for campo in ("nodos_siguientes", "nodos_previos"):
        for dst in n.get(campo) or []:
            if dst in absset: malas += 1
            if dst == nid: auto += 1
check("cero referencias vivas a un absorbido", malas == 0, str(malas))
check("cero auto-aristas entre vivos", auto == 0, str(auto))

print()
print("TOTAL: %d comprobaciones, %d fallos" % (n_ok + len(fallos), len(fallos)))
if fallos:
    print("FALLOS:", *fallos, sep="\n  ")
    sys.exit(1)
print("CERO FALLOS")
