# -*- coding: utf-8 -*-
"""Puntua las trampas y consolida la limpieza M11.

    python consolidar.py puntuar            trampas del redactor y del verificador, por lote
    python consolidar.py arbitro NN         arma la entrada del arbitro del lote NN (los FALLA reales)
    python consolidar.py tanda              arma la tanda de correcciones declaradas con lo final de todos los lotes

Texto final de cada elemento: el del redactor si el verificador dijo OK; el del arbitro si dijo FALLA.
"""
import glob
import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ORQ = Path(r"C:\Users\AlexDesk\AppData\Local\Temp\claude\c--Users-AlexDesk-Documents-I-have-an-idea\35709856-d3a7-4f79-ad7e-c0e77323cd47\scratchpad")
PACK = AQUI / "primer_equipo" / "nodos"
REGLA_VOZ = "voz de libro, citas en ingles y voz de la casa: el cliente no ve el libro, el texto, el autor ni ingles (decision del fundador, 28 sep 2026; docs/saneamiento/instrumentos/M11_LIMPIEZA.md)"
REGLA_ATRIB = "ningun libro ni autor llega al cliente (AGENTS.md; decision del fundador, 26 y 28 sep 2026)"
REGLA_CIFRA = "regla de la cifra (docs/POLITICA_MARCO_PAIS.md): la cifra de mercado sale"
INSTR = "limpieza M11: redactor, verificador ciego con trampas y arbitro (docs/saneamiento/instrumentos/M11_LIMPIEZA.md)"


def cargar(carpeta, nombre):
    p = AQUI / carpeta / nombre
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


def textos(n):
    out = {"titulo_concepto": n["titulo_concepto"], "entregable_esperado": n["entregable_esperado"]}
    for i, t in enumerate(n["pasos_accionables"]):
        out["pasos_accionables[%d]" % i] = t
    for i, t in enumerate(n["condiciones_activacion"]):
        out["condiciones_activacion[%d]" % i] = t
    return out


def puntuar():
    clave_r = json.loads((ORQ / "clave_trampas_redactor.json").read_text(encoding="utf-8"))
    plantados = clave_r["plantados"]
    marcas = {"voz": "obra original", "cifra": "20.000", "autor": "Grove"}
    tot = {k: [0, 0] for k in marcas}
    for tid, info in sorted(clave_r["trampas"].items()):
        s = cargar("redactor", "lote_%s.json" % info["lote"])
        e = cargar("entrada", "lote_%s.json" % info["lote"])
        if not s:
            continue
        nodo_e = next(n for n in e["nodos"] if n["node_id"] == tid)
        nodo_s = next((n for n in s["nodos"] if n["node_id"] == tid), None)
        finales = textos(nodo_e)
        for c in (nodo_s or {}).get("cambios") or []:
            k = c["campo"] + ("" if c.get("indice") is None else "[%d]" % c["indice"])
            finales[k] = c["texto_nuevo"]
        todo = " ".join(finales.values())
        for tipo, m in marcas.items():
            tot[tipo][1] += 1
            if m not in todo:
                tot[tipo][0] += 1
    print("TRAMPAS DEL REDACTOR (quitadas / plantadas):", {k: "%d/%d" % tuple(v) for k, v in tot.items()})
    clave_v = json.loads((ORQ / "clave_trampas_verificador.json").read_text(encoding="utf-8")) if (ORQ / "clave_trampas_verificador.json").exists() else {"trampas": {}}
    cazadas, total = 0, 0
    for item, info in sorted(clave_v["trampas"].items()):
        nn = item.split("_")[1]
        v = cargar("verificador", "salida_%s.json" % nn)
        if not v:
            continue
        total += 1
        r = next((x for x in v["items"] if x["item"] == item), None)
        if r and r["veredicto"] == "FALLA":
            cazadas += 1
        else:
            print("  el verificador NO cazo", item, info["tipo"])
    print("TRAMPAS DEL VERIFICADOR (cazadas / plantadas): %d/%d" % (cazadas, total))


def arbitro(nn):
    v = cargar("verificador", "salida_%s.json" % nn)
    e = cargar("verificador", "entrada_%s.json" % nn)
    por = {i["item"]: i for i in e["items"]}
    casos = []
    for r in v["items"]:
        if r["veredicto"] != "FALLA" or r["item"].startswith("vtrampa_"):
            continue
        casos.append(dict(por[r["item"]], objecion=r.get("motivo"), propuesta_verificador=r.get("propuesta")))
    (AQUI / "arbitro").mkdir(exist_ok=True)
    (AQUI / "arbitro" / ("entrada_%s.json" % nn)).write_text(json.dumps({"lote": nn, "casos": casos}, ensure_ascii=False, indent=1), encoding="utf-8")
    print("lote %s: %d casos al arbitro" % (nn, len(casos)))


def tanda():
    tanda, faltan = [], []
    aj = AQUI / "ajustes_orquestador.json"
    ajustes = {x["item"]: x for x in json.loads(aj.read_text(encoding="utf-8"))["ajustes"]} if aj.exists() else {}
    for p in sorted(glob.glob(str(AQUI / "redactor" / "lote_*.json"))):
        nn = Path(p).stem.split("_")[1]
        s = json.loads(Path(p).read_text(encoding="utf-8"))
        v = cargar("verificador", "salida_%s.json" % nn)
        a = cargar("arbitro", "salida_%s.json" % nn)
        if v is None:
            faltan.append("lote %s sin verificar" % nn)
            continue
        veredicto_v = {x["item"]: x for x in v["items"]}
        final_a = {x["item"]: x for x in (a or {}).get("casos", [])}
        for n in s["nodos"]:
            nid = n["node_id"]
            if nid.startswith("trampa_"):
                continue
            nodo = json.loads((PACK / ("%s.json" % nid)).read_text(encoding="utf-8"))
            piezas = [("resumen_teorico", None, n["resumen"]["texto"], "RESUMEN", [], n["resumen"])]
            for c in n.get("cambios") or []:
                piezas.append((c["campo"], c.get("indice"), c["texto_nuevo"], c["veredicto"], c.get("fragmentos") or [], c))
            for campo, indice, texto, ver, frags, c in piezas:
                item = "%s|%s%s" % (nid, campo, "" if indice is None else "[%d]" % indice)
                r = veredicto_v.get(item)
                if r is None:
                    faltan.append("%s sin veredicto del verificador" % item)
                    continue
                if r["veredicto"] == "FALLA":
                    fa = final_a.get(item)
                    if not fa:
                        faltan.append("%s: FALLA sin decision del arbitro" % item)
                        continue
                    texto = fa["texto_final"]
                    if fa.get("lineas") or fa.get("fichero"):
                        # el arbitro puede corregir la evidencia del resumen (fichero o lineas mal citados)
                        c = dict(c, fichero=fa.get("fichero") or c.get("fichero"), lineas=fa.get("lineas") or c.get("lineas"))
                if item in ajustes:
                    texto = ajustes[item]["texto_final"]
                anterior = nodo[campo] if indice is None else nodo[campo][indice]
                if texto == anterior:
                    continue
                frags = [f for f in frags if f and f not in texto]
                corr = {"id": "m11-limpieza-%s-%s" % (nid, campo if indice is None else "%s-%d" % (campo, indice)),
                        "fecha": "2026-09-28", "node_id": nid, "campo": campo, "veredicto": ver,
                        "texto_anterior": anterior, "texto_nuevo": texto,
                        "decision": "limpieza M11 (%s): %s%s" % (ver, "verificador OK" if r["veredicto"] == "OK" else "arbitro: " + final_a[item].get("decision", ""),
                                                             ("; ajuste del orquestador: " + ajustes[item]["motivo"]) if item in ajustes else ""),
                        "auditoria": "docs/saneamiento/resultados/M11/ (redactor, verificador y arbitro, lote %s)" % nn,
                        "motivos": c.get("motivos") or []}
                if indice is not None:
                    corr["indice"] = indice
                if ver == "RESUMEN":
                    corr["cita"] = {"instrumento": INSTR, "evidencia": {"fichero": c["fichero"], "lineas": c["lineas"]}}
                elif ver in ("VOZ", "ATRIBUCION", "CIFRA"):
                    if not frags:
                        corr["veredicto"] = "ORTOGRAFIA" if ver == "VOZ" and set(corr["motivos"]) <= {"ortografia"} else ver
                    regla = {"VOZ": REGLA_VOZ, "ATRIBUCION": REGLA_ATRIB, "CIFRA": REGLA_CIFRA}[ver]
                    corr["cita"] = {"regla": regla, "fragmentos": frags or ["(texto reescrito entero: %s)" % ", ".join(corr["motivos"])]}
                else:
                    corr["cita"] = {"instrumento": INSTR, "evidencia": "lote %s, %s" % (nn, "verificado" if r["veredicto"] == "OK" else "arbitrado")}
                tanda.append(corr)
    if faltan:
        print("TANDA INCOMPLETA:")
        for f in faltan[:40]:
            print("  " + f)
        return 1
    destino = AQUI / "tanda_m11_limpieza.json"
    destino.write_text(json.dumps(tanda, ensure_ascii=False, indent=1), encoding="utf-8")
    print("tanda: %d correcciones en %d nodos -> %s" % (len(tanda), len({c["node_id"] for c in tanda}), destino))
    return 0


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "puntuar":
        puntuar()
    elif cmd == "arbitro":
        arbitro(sys.argv[2])
    elif cmd == "tanda":
        sys.exit(tanda())
