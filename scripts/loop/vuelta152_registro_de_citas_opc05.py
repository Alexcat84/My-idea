# -*- coding: utf-8 -*-
"""VUELTA 152, TAREA 6.a: EL REGISTRO DE CITAS DE `OP-C-05`.

LA DECISION DEL FUNDADOR QUE LO MANDA (2 sep 2026, PREGUNTA 1, opcion c con
atajo de registro, en
docs/loop/paradas/2026-09-02-opc05-bidireccionales-DECISION.md): la mitad de
bidireccionales de OP-C-05 exige que CADA par bidireccional entre vivos tenga un
VEREDICTO DE LECTURA REGISTRADO CON CITA. La lista blanca deja de ser una lista
a mano y pasa a ser un REGISTRO DE CITAS. UN PAR SIN CITA ES ROJO.

LAS DOS VIAS QUE VALEN, Y NO HAY UNA TERCERA AUTOMATICA:

  (1) EL CRIBADO, cuando el par existe en docs/INTRA_DOMINIO_VEREDICTOS.jsonl
      con clase D, B o C. La C es el enlace mutuo legitimo del banco 9.22; la D
      y la B son pares leidos que NO se funden, o sea que la arista de ida y
      vuelta entre ellos no es una escalera que haya que retirar. La cita es EL
      PUESTO.
  (2) LA DECLARACION SELLADA DE P.10, cuando el par cae bajo un nodo puente ya
      declarado y la salida escrita fue DECLARADO Y NO FUNDIDO.

  (3) Y lo que no cubran las dos, VA A LECTURA DIRIGIDA POR P.5, se registra en
      docs/plan/LECTURAS_DIRIGIDAS.md y entra aqui con via LECTURA_DIRIGIDA.
      Este instrumento NO la inventa: la lee de su fichero.

P.1 NO ES OPCIONAL AQUI, Y LA DIFERENCIA ESTA MEDIDA. Todo conteo que toque ids
pasa por el resolutor antes de contar. Sin resolver, el mismo grafo da 147
pares; resolviendo da 153. Las SEIS que faltan solo aparecen tras la resolucion,
y sin ella el registro se daria por completo dejando seis pares sin cita. El
instrumento resuelve LOS DOS LADOS, tanto los del grafo como los del archivo del
cribado (un par leido hace ochenta vueltas puede tener hoy los dos ids
deprecados y resolver a otros dos), y lo dice en su salida.

CONTRASTE QUE PRUEBA QUE MIDE BIEN: sobre el mergebase con main (36b57d78)
tienen que salir 83 pares, no 153.

USO:
  python scripts/loop/vuelta152_registro_de_citas_opc05.py
  python scripts/loop/vuelta152_registro_de_citas_opc05.py --escribir
  python scripts/loop/vuelta152_registro_de_citas_opc05.py --ref <REF>
"""
import argparse
import collections
import io
import json
import os
import re
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
VERED = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
LD = os.path.join(RAIZ, "docs", "plan", "LECTURAS_DIRIGIDAS.md")
REGISTRO = os.path.join(RAIZ, "docs", "plan", "REGISTRO_DE_CITAS_OPC05.jsonl")

CLASES_QUE_VALEN = ("D", "B", "C")

# LOS PUENTES DE P.10, leidos de docs/plan/BANCO_DEL_PLAN.md, seccion P.10, tabla
# LOS TRES EJEMPLARES. Solo cuentan los que la tabla cierra como DECLARADO Y NO
# FUNDIDO, o sea aquellos cuya columna "como acabo" dice que el par NO se funde y
# se enlaza. Se escriben aqui con su fila para que la cita se pueda ir a ver.
PUENTES_P10 = {
    "customer_validation": "P.10 ejemplar 3, tabla LOS TRES EJEMPLARES: puente doble con "
                           "filosofia_customer_validation sobre LD-59; 'no queda lectura que "
                           "desempate: se funde solo el triangulo cerrado y el cuarto SE ENLAZA'",
    "filosofia_customer_validation": "P.10 ejemplar 3, tabla LOS TRES EJEMPLARES: puente doble con "
                                     "customer_validation sobre LD-59; el cuarto SE ENLAZA",
}


def cargar(ref):
    if ref == "WORK":
        return json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    b = subprocess.run(["git", "show", "%s:dataset/metadata/master_graph.json" % ref],
                       capture_output=True, cwd=RAIZ)
    if b.returncode:
        raise SystemExit("ROJO: no se pudo leer %s" % ref)
    return json.loads(b.stdout.decode("utf-8"))["nodos"]


def hacer_resolver(N):
    """P.1, RE ESCRITO AQUI y no importado del codigo que esta guarda vigila."""
    alias = {}
    for nid, n in N.items():
        for a in (n.get("ids_alias") or []):
            if a != nid:
                alias[a] = nid

    def r(nid):
        n = N.get(nid)
        if n is not None and not n.get("deprecado"):
            return nid
        visto, cur, ult = {nid}, nid, (nid if n is not None else None)
        while cur in alias:
            cur = alias[cur]
            if cur in visto:
                break
            visto.add(cur)
            c = N.get(cur)
            if c is None:
                continue
            ult = cur
            if not c.get("deprecado"):
                return cur
        return ult
    return r


def bidireccionales(N, resolver=True):
    r = hacer_resolver(N)
    S = set()
    for nid, n in N.items():
        if n.get("deprecado"):
            continue
        for d in (n.get("nodos_siguientes") or []):
            if d not in N:
                continue
            a, b = (r(nid), r(d)) if resolver else (nid, d)
            if a and b and a != b and not N[a].get("deprecado") and not N[b].get("deprecado"):
                S.add((a, b))
    return {tuple(sorted(p)) for p in S if (p[1], p[0]) in S}


def citas_del_cribado(N):
    """El archivo del cribado, con LOS DOS LADOS RESUELTOS con el resolutor de
    hoy. Un par leido hace ochenta vueltas puede traer dos ids que hoy estan
    deprecados: sin resolver, ese veredicto se perderia."""
    r = hacer_resolver(N)
    idx = collections.defaultdict(list)
    for x in io.open(VERED, encoding="utf-8"):
        if not x.strip():
            continue
        d = json.loads(x)
        a, b = r(d["nodo_a"]), r(d["nodo_b"])
        if a and b and a != b:
            idx[tuple(sorted((a, b)))].append(d)
    return idx


def citas_de_lectura_dirigida(N):
    """Las lecturas de esta campana escritas en docs/plan/LECTURAS_DIRIGIDAS.md
    con la marca de registro de citas de OP-C-05. Se leen de su fichero: este
    instrumento NO adjudica, solo recoge."""
    r = hacer_resolver(N)
    out = {}
    if not os.path.exists(LD):
        return out
    texto = io.open(LD, encoding="utf-8").read()
    patron = re.compile(
        r"REGISTRO DE CITAS `OP-C-05`\s*\|\s*([a-z0-9_]+)\s*<->\s*([a-z0-9_]+)\s*\|\s*"
        r"([A-Z]+)\s*\|\s*(LD-[A-Za-z0-9.\-]+)\s*\|\s*([^\n|]+)")
    for m in patron.finditer(texto):
        a, b = r(m.group(1)), r(m.group(2))
        if not a or not b or a == b:
            continue
        out[tuple(sorted((a, b)))] = {
            "clase": m.group(3), "ld": m.group(4), "motivo": m.group(5).strip()}
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", default="WORK")
    ap.add_argument("--escribir", action="store_true")
    args = ap.parse_args()

    N = cargar(args.ref)
    CON = bidireccionales(N, True)
    SIN = bidireccionales(N, False)
    print("REF: %s" % args.ref)
    print("=" * 96)
    print("P.1 PRIMERO, Y CON LA DIFERENCIA MEDIDA")
    print("=" * 96)
    print("  pares bidireccionales entre vivos RESOLVIENDO ALIAS (P.1) : %d" % len(CON))
    print("  pares bidireccionales entre vivos SIN resolver            : %d" % len(SIN))
    print("  pares que SOLO aparecen tras resolver                     : %d" % len(CON - SIN))
    for p in sorted(CON - SIN):
        print("      %s <-> %s" % p)
    print("  SIN P.1 el registro se daria por completo dejando esos pares sin cita.")
    print("")

    cribado = citas_del_cribado(N)
    lecturas = citas_de_lectura_dirigida(N)

    registro, sin_veredicto = [], []
    for p in sorted(CON):
        a, b = p
        filas = [x for x in cribado.get(p, []) if x["clase"] in CLASES_QUE_VALEN]
        malas = [x for x in cribado.get(p, []) if x["clase"] not in CLASES_QUE_VALEN]
        if filas:
            f = sorted(filas, key=lambda x: (x["clase"] != "C", x.get("puesto_intra") or 0))[0]
            registro.append({
                "par": [a, b], "via": "CRIBADO", "clase": f["clase"],
                "cita": "puesto %s, dominio %s, clase %s"
                        % (f.get("puesto_intra"), f.get("dominio"), f["clase"]),
                "nodo_a_leido": f["nodo_a"], "nodo_b_leido": f["nodo_b"],
                "razon": (f.get("razon") or "")[:400]})
            continue
        if p in lecturas:
            L = lecturas[p]
            registro.append({
                "par": [a, b], "via": "LECTURA_DIRIGIDA", "clase": L["clase"],
                "cita": "%s, clase %s" % (L["ld"], L["clase"]),
                "nodo_a_leido": a, "nodo_b_leido": b, "razon": L["motivo"]})
            continue
        puente = [x for x in (a, b) if x in PUENTES_P10]
        if puente:
            registro.append({
                "par": [a, b], "via": "P.10", "clase": "DECLARADO Y NO FUNDIDO",
                "cita": PUENTES_P10[puente[0]],
                "nodo_a_leido": a, "nodo_b_leido": b,
                "razon": "nodo puente declarado en P.10; su salida escrita es enlazar, no fundir"})
            continue
        sin_veredicto.append((p, malas))

    print("=" * 96)
    print("EL CRUCE, CONTADO")
    print("=" * 96)
    porvia = collections.Counter(x["via"] for x in registro)
    for via in ("CRIBADO", "P.10", "LECTURA_DIRIGIDA"):
        print("  con cita por %-18s : %d" % (via, porvia.get(via, 0)))
    print("  CON CITA, TOTAL              : %d de %d" % (len(registro), len(CON)))
    print("  SIN VEREDICTO                : %d" % len(sin_veredicto))
    print("")
    if registro:
        print("  clases de las citas del cribado: %s"
              % dict(collections.Counter(x["clase"] for x in registro if x["via"] == "CRIBADO")))
    print("")

    print("=" * 96)
    print("LOS PARES SIN VEREDICTO (%d). ESTOS SON LOS QUE VAN A LECTURA DIRIGIDA POR P.5."
          % len(sin_veredicto))
    print("=" * 96)
    for (a, b), malas in sin_veredicto:
        extra = ""
        if malas:
            extra = "  [OJO: el cribado SI trae este par con clase %s, que NO vale aqui]" % (
                ", ".join(sorted({x["clase"] for x in malas})))
        print("  %-46s <-> %s%s" % (a, b, extra))
    print("")

    if args.escribir:
        lineas = [json.dumps(x, ensure_ascii=False, sort_keys=True) for x in registro]
        io.open(REGISTRO, "w", encoding="utf-8", newline="\n").write("\n".join(lineas) + "\n")
        print("ESCRITO: docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl con %d entrada(s)." % len(registro))
        vuelto = [json.loads(x) for x in io.open(REGISTRO, encoding="utf-8") if x.strip()]
        assert len(vuelto) == len(registro), "el registro no releyo lo que escribio"
        assert {tuple(sorted(x["par"])) for x in vuelto} == {tuple(sorted(x["par"])) for x in registro}
        print("  [OK] releido y cotejado: %d entradas, mismos pares." % len(vuelto))
        print("  [OK] pares del grafo cubiertos: %d de %d. SIN CITA: %d"
              % (len(registro), len(CON), len(sin_veredicto)))


main()
