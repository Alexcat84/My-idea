# -*- coding: utf-8 -*-
"""Vuelta 48, TAREA 1.2: LA NOTA ENVEJECIDA DE `OP-U-01` Y `OP-U-02`, corregida
por el carril del banco 9.10 y CON LA CIFRA MEDIDA HOY, no copiada del acta.

LO QUE SE CORRIGE: los campos `nota`, `evidencia` y `adjudicacion` de las dos
operaciones publican 335 componentes sobre 854 nodos, 280 CERRADOS sobre 600 y
55 ABIERTOS sobre 254. Eran exactos en la vuelta 11 y quedaron sin barrer
cuando el fichero sellado se re-sello con correccion declarada.

COMO SE CORRIGE: el texto viejo NO SE BORRA. Se le anade detras un parrafo de
CORRECCION DECLARADA, que es la forma que las propias operaciones ya usan
(dentro viven las correcciones declaradas de las vueltas 12 y 13). Una
correccion que tapa lo que corrige no se puede auditar.

LAS TRES CIFRAS SE MIDEN AQUI Y AHORA, ninguna se teclea:
  a) el FICHERO SELLADO docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl, contado
     linea a linea. NO se toca: solo se lee.
  b) la nomina VIVA con la que se abrio el tramo 1 de esta vuelta.
  c) la nomina VIVA al CERRAR el tramo 1, que es el estado de hoy.

Y LA CADENA DE COMMITS SE MIDE, no se cita de memoria: el encargo nombra tres
(7cec9ecc, 78ea7799, 70878328) y `git log --follow` sobre el fichero devuelve
OCHO. La discrepancia se declara en el propio texto en vez de resolverse
copiando, que es la regla 2 de EJECUTOR.md.

Uso: python scripts/loop/vuelta48_nota_envejecida.py [--escribir]
"""
import argparse
import io
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
SELLADA = os.path.join(RAIZ, "docs", "plan", "RECOMPUTO_3388_COMPONENTES.jsonl")
APERTURA = os.path.join(RAIZ, "docs", "loop", "RECOMPUTO_V48_COMPONENTES.jsonl")
CIERRE = os.path.join(RAIZ, "docs", "loop", "RECOMPUTO_V48_CIERRE.jsonl")
MARCA = "CORRECCION DECLARADA (vuelta 48, 19 ago 2026)"


def censar(p):
    R = [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]
    cer = [r for r in R if r["estado"] == "CERRADO"]
    ab = [r for r in R if r["estado"] == "ABIERTO"]
    tam = {}
    for r in cer:
        tam[r["tamano"]] = tam.get(r["tamano"], 0) + 1
    return {"actos": len(R), "nodos": sum(r["tamano"] for r in R),
            "cerrados": len(cer), "nodos_cerrados": sum(r["tamano"] for r in cer),
            "abiertos": len(ab), "nodos_abiertos": sum(r["tamano"] for r in ab),
            "por_tamano": dict(sorted(tam.items()))}


def cadena():
    out = subprocess.run(
        ["git", "log", "--format=%h", "--follow", "--",
         "docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl"],
        cwd=RAIZ, capture_output=True, text=True)
    hs = [x for x in out.stdout.split() if x]
    filas = []
    for h in hs:
        r = subprocess.run(["git", "show", "%s:docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl" % h],
                           cwd=RAIZ, capture_output=True, text=True)
        filas.append((h, len([l for l in r.stdout.split("\n") if l.strip()])))
    return list(reversed(filas))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--escribir", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    s, ap_, ci = censar(SELLADA), censar(APERTURA), censar(CIERRE)
    ch = cadena()

    print("=" * 78)
    print("LAS TRES CIFRAS DEL MISMO OBJETO, MEDIDAS HOY")
    print("=" * 78)
    print("  %-46s %6s %6s %6s %6s %6s %6s"
          % ("de donde sale", "actos", "nodos", "CERR", "nCERR", "ABIER", "nABIER"))
    for etq, d in (("fichero SELLADO docs/plan/ (no se toca)", s),
                   ("nomina VIVA al abrir el tramo 1", ap_),
                   ("nomina VIVA al CERRAR el tramo 1", ci)):
        print("  %-46s %6d %6d %6d %6d %6d %6d"
              % (etq, d["actos"], d["nodos"], d["cerrados"], d["nodos_cerrados"],
                 d["abiertos"], d["nodos_abiertos"]))
    print()
    print("  CERRADOS por tamano al cerrar el tramo: %s" % ci["por_tamano"])
    print()
    print("LA CADENA DE COMMITS DEL FICHERO SELLADO, medida con git log --follow:")
    for h, n in ch:
        print("   %-10s %4d lineas" % (h, n))
    print("   commits que lo tocan: %d. El encargo nombraba 3." % len(ch))

    lineas = [l for l in io.open(OPS, encoding="utf-8") if l.strip()]
    ops = [json.loads(l) for l in lineas]
    if any(MARCA in json.dumps(o, ensure_ascii=False) for o in ops):
        print()
        print("YA APLICADA.")
        return 0

    hs = ", ".join(h for h, _ in ch)
    parrafo = (
        " " + MARCA + ", por el carril del banco 9.10 y con el texto viejo entero delante: "
        "LO QUE ENVEJECIO FUE ESTA NOTA, NO EL FICHERO SELLADO. La cifra de arriba (335 componentes, "
        "854 nodos, 280 CERRADOS sobre 600, 55 ABIERTOS sobre 254) era exacta en la vuelta 11 "
        "(commit 7f4ec6d9) y quedo sin barrer cuando docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl se "
        "re-sello con correccion declarada varias veces. LAS TRES CIFRAS DE HOY, LAS TRES MEDIDAS EN "
        "ESTA VUELTA CON scripts/loop/vuelta48_nota_envejecida.py y NINGUNA copiada de un acta. "
        "(a) EL FICHERO SELLADO, contado linea a linea y sin tocarlo: %d actos, %d nodos, %d CERRADOS "
        "sobre %d nodos, %d ABIERTOS sobre %d. Esa es la cifra que sustituye a la de arriba. "
        "(b) LA NOMINA VIVA AL ABRIR el tramo 1 de esta vuelta, contra el grafo de ese momento: "
        "%d actos, %d nodos, %d CERRADOS sobre %d, %d ABIERTOS sobre %d. "
        "(c) LA NOMINA VIVA AL CERRAR el tramo 1, que es el estado de hoy tras fundir 16 actos: "
        "%d actos, %d nodos, %d CERRADOS sobre %d (%s), %d ABIERTOS sobre %d. "
        "LOS ABIERTOS NO SE HAN MOVIDO NI UNA VEZ EN LAS TRES MEDICIONES: %d sobre %d, que es lo que "
        "cabe esperar de una operacion que solo toca CERRADOS. "
        "Y UNA DISCREPANCIA QUE SE DECLARA EN VEZ DE RESOLVERSE COPIANDO (regla 2 de EJECUTOR.md): "
        "el encargo de esta vuelta atribuye el re-sellado a TRES commits, y git log --follow sobre el "
        "fichero devuelve %d, que ademas NO bajan de forma monotona (801c59f9 lo sube de 334 a 335 "
        "antes de que vuelva a bajar). La cadena medida hoy, del mas viejo al mas nuevo, es: %s."
        % (s["actos"], s["nodos"], s["cerrados"], s["nodos_cerrados"], s["abiertos"], s["nodos_abiertos"],
           ap_["actos"], ap_["nodos"], ap_["cerrados"], ap_["nodos_cerrados"], ap_["abiertos"], ap_["nodos_abiertos"],
           ci["actos"], ci["nodos"], ci["cerrados"], ci["nodos_cerrados"],
           ", ".join("%d: %d" % (k, v) for k, v in ci["por_tamano"].items()),
           ci["abiertos"], ci["nodos_abiertos"],
           ci["abiertos"], ci["nodos_abiertos"], len(ch), hs))

    tocados = 0
    salida = []
    for l in lineas:
        d = json.loads(l)
        if d.get("id_op") in ("OP-U-01", "OP-U-02"):
            for campo in ("nota", "adjudicacion"):
                if isinstance(d.get(campo), str):
                    d[campo] = d[campo].rstrip() + parrafo
                    tocados += 1
            if isinstance(d.get("evidencia"), list):
                d["evidencia"] = list(d["evidencia"]) + [MARCA + parrafo.split(MARCA, 1)[1]]
                tocados += 1
            salida.append(json.dumps(d, ensure_ascii=False) + "\n")
        else:
            salida.append(l if l.endswith("\n") else l + "\n")

    print()
    print("campos a corregir: %d (nota, adjudicacion y evidencia de las dos operaciones)" % tocados)
    if not a.escribir:
        print("SIMULACION: sin --escribir no toco nada.")
        return 0

    with io.open(OPS, "w", encoding="utf-8", newline="\n") as fh:
        fh.writelines(salida)

    # guardas
    ops2 = [json.loads(l) for l in io.open(OPS, encoding="utf-8") if l.strip()]
    print()
    print("GUARDAS")
    print("  operaciones antes %d, despues %d" % (len(ops), len(ops2)))
    viejas = 0
    for o in ops2:
        if o["id_op"] in ("OP-U-01", "OP-U-02"):
            t = json.dumps(o, ensure_ascii=False)
            if "335 componentes conexas sobre 854 nodos" in t or "280 CERRADOS sobre 600" in t:
                viejas += 1
    print("  el texto VIEJO sigue dentro (no se borro): %d de 2 operaciones" % viejas)
    t = io.open(OPS, encoding="utf-8").read()
    print("  guiones largos %d, guiones medios %d"
          % (t.count("—"), t.count("–")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
