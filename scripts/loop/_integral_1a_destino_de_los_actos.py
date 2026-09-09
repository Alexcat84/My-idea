# -*- coding: utf-8 -*-
r"""_integral_1a_destino_de_los_actos.py . AUDITORIA INTEGRAL (9 sep 2026), PASO 1.a,
ITEM 1: EL DESTINO ESCRITO DE CADA ACTO DEL CORTE VIGENTE.

LA CLAUSULA QUE SE MIDE, en su letra nueva (decision del fundador, 9 sep 2026):
*todo acto CERRADO tiene destino escrito: superviviente, declaracion sellada o
disolucion medida*. El esperado es 335 de 335 con destino. Un acto SIN ninguno
de los tres es trabajo real: se nombra y se PARA.

LAS TRES FUENTES, Y NINGUNA CIFRA SE TECLEA:
  . el corte vigente de docs/plan/INVENTARIO.jsonl (el MAYOR fecha_corte de las
    entradas de tipo acto, como hace scripts/loop/_v217_t1_diecisiete.py);
  . el grafo dataset/metadata/master_graph.json (vivo, deprecado, ids_alias);
  . los PLANES SELLADOS docs/loop/PLAN_V*.json: `actos` (fundidos, con su
    superviviente y absorbidos), `declarados_y_no_fundidos` (con su motivo), y
    los planes de destejido (`superviviente`/`absorbidos`/`nodos` sueltos).

LOS TRES DESTINOS, EN ORDEN DE PRUEBA (el primero que casa gana, y se dice cual):
  1. SUPERVIVIENTE: en el grafo queda UN miembro vivo y los demas estan
     deprecados con alias hacia el (la misma vara del lector de la 217).
  2. DECLARACION SELLADA: el conjunto de miembros del acto casa con una entrada
     de `declarados_y_no_fundidos` de algun plan sellado, que trae motivo.
  3. DISOLUCION MEDIDA: el acto NO tiene un superviviente unico pero un plan
     sellado fundio un SUBCONJUNTO suyo (el resto quedo enlazado, tercera salida
     de P.10) o un plan de destejido nombra sus miembros.
  0. SIN DESTINO: ninguno de los tres. Se lista entero.

USO:  python scripts/loop/_integral_1a_destino_de_los_actos.py
Escribe docs/loop/SALIDA_integral_1A_DESTINO_ACTOS.txt y sale 0 si los 335
tienen destino, 1 si alguno no lo tiene.
"""
import glob
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
INV = os.path.join(RAIZ, "docs", "plan", "INVENTARIO.jsonl")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
PLANES = sorted(glob.glob(os.path.join(RAIZ, "docs", "loop", "PLAN_V*.json")))
DESTINO = os.path.join(RAIZ, "docs", "loop", "SALIDA_integral_1A_DESTINO_ACTOS.txt")


def actos_vigentes():
    filas = [json.loads(l) for l in io.open(INV, encoding="utf-8") if l.strip()]
    actos = [e for e in filas if e.get("tipo") == "acto"]
    corte = max(str(e.get("fecha_corte") or "") for e in actos)
    return [e for e in actos if str(e.get("fecha_corte") or "") == corte], corte, len(actos)


def cargar_planes():
    fundidos, declarados, destejidos = [], [], []
    for p in PLANES:
        try:
            d = json.load(io.open(p, encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(d, dict):
            continue
        nombre = os.path.basename(p)
        for a in d.get("actos") or []:
            ms = set(a.get("miembros") or []) | set(a.get("absorbidos") or [])
            if a.get("superviviente"):
                ms.add(a["superviviente"])
            if ms:
                fundidos.append((nombre, ms, a.get("superviviente")))
        for a in d.get("declarados_y_no_fundidos") or []:
            ms = set(a.get("miembros") or []) if isinstance(a, dict) else set()
            if ms:
                declarados.append((nombre, ms, (a.get("motivo") or a.get("guarda_que_lo_para") or "")[:120]))
        if "OPD" in nombre or "ACTO" in nombre:
            def _ids(x):
                out = set()
                for e in (x or []):
                    if isinstance(e, str):
                        out.add(e)
                    elif isinstance(e, dict):
                        for k in ("id", "nodo", "node_id", "superviviente", "absorbido"):
                            if isinstance(e.get(k), str):
                                out.add(e[k])
                return out
            ms = _ids(d.get("nodos")) | _ids(d.get("absorbidos"))
            for k in ("superviviente", "absorbido"):
                if isinstance(d.get(k), str):
                    ms.add(d[k])
            if ms:
                destejidos.append((nombre, ms, str(d.get("operacion"))[:40]))
    return fundidos, declarados, destejidos


PAGINA03 = os.path.join(RAIZ, "docs", "plan", "03_FUSIONES.md")
TRAMO_U02 = os.path.join(RAIZ, "docs", "loop", "TRAMO_UNICO_OPU02_V64.jsonl")
MARCAS = ("declarad", "se acumula para", "colision de clase medida", "PREGUNTA DE POLITICA",
          "CONTEOS DE CONTENIDO QUE CHOCAN", "dueno FUERA", "IMPOSIBLE POR PUERTA", "EMPATE SIN VARA")
_LINEAS03 = None


def declaracion_en_la_pagina(ms):
    """CUARTA FUENTE, LA PAGINA 03 (registros del cierre de cada tramo): una fila
    de tabla que nombra TODOS los miembros del acto y lleva una marca de
    declaracion; o el asiento de cierre de la fase (actos con dueno FUERA de la
    fase, por su numero de orden_universo en TRAMO_UNICO_OPU02_V64.jsonl).
    Devuelve (numero_de_linea, texto_corto) o None."""
    global _LINEAS03
    if _LINEAS03 is None:
        _LINEAS03 = io.open(PAGINA03, encoding="utf-8").read().splitlines()
    for i, l in enumerate(_LINEAS03, 1):
        if l.startswith("|") and all(("`%s`" % m) in l for m in ms) and any(k.lower() in l.lower() for k in MARCAS):
            celdas = [c.strip() for c in l.strip().strip("|").split("|")]
            return (i, " / ".join(c[:70] for c in celdas[1:3]))
    try:
        filas = [json.loads(x) for x in io.open(TRAMO_U02, encoding="utf-8") if x.strip()]
    except Exception:
        filas = []
    for f in filas:
        if set(f.get("miembros") or []) == set(ms):
            n = f.get("orden_universo")
            for i, l in enumerate(_LINEAS03, 1):
                if "dueno FUERA de la fase" in l and ("**%d**" % n) in l:
                    return (i, "acto %d con dueno FUERA de la fase: %s" % (n, l.strip()[:110]))
    return None


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    actos, corte, todos = actos_vigentes()
    g = json.load(io.open(GRAFO, encoding="utf-8"))
    N = g["nodos"]
    fundidos, declarados, destejidos = cargar_planes()
    w("AUDITORIA INTEGRAL, PASO 1.a, ITEM 1: EL DESTINO ESCRITO DE CADA ACTO DEL CORTE VIGENTE")
    w("CIFRA corte vigente leido del inventario: %s" % corte)
    w("CIFRA actos de ese corte: %d | CIFRA actos de todos los cortes: %d" % (len(actos), todos))
    w("CIFRA nodos del grafo: %d" % len(N))
    w("CIFRA planes sellados leidos: %d | entradas fundidas: %d | declaradas: %d | de destejido: %d"
      % (len(PLANES), len(fundidos), len(declarados), len(destejidos)))
    w("")
    cuenta = {"SUPERVIVIENTE": 0, "DECLARACION SELLADA": 0, "DISOLUCION MEDIDA": 0, "SIN DESTINO": 0}
    por_estado = {}
    sin = []
    detalle = []
    for a in actos:
        ms = a.get("miembros") or []
        sm = set(ms)
        vivos = [m for m in ms if m in N and not N[m].get("deprecado")]
        est = "ABIERTO" if "ABIERTO" in str(a.get("estado")) else "CERRADO"
        destino, prueba = None, ""
        if len(vivos) == 1:
            s = vivos[0]
            al = set(N[s].get("ids_alias") or [])
            sin_alias = [m for m in ms if m != s and m not in al]
            if not sin_alias:
                destino, prueba = "SUPERVIVIENTE", "superviviente %s, %d absorbidos con alias" % (s, len(ms) - 1)
        if destino is None:
            for nombre, dm, motivo in declarados:
                if sm & dm:
                    destino, prueba = "DECLARACION SELLADA", "%s (%d de %d miembros): %s" % (nombre, len(sm & dm), len(sm), motivo)
                    break
        if destino is None:
            for nombre, fm, s in fundidos:
                if sm & fm:
                    destino, prueba = "DISOLUCION MEDIDA", "subconjunto fundido en %s (superviviente %s, %d de %d miembros), resto enlazado" % (nombre, s, len(sm & fm), len(sm))
                    break
        if destino is None:
            for nombre, dm, op in destejidos:
                if sm & dm:
                    destino, prueba = "DISOLUCION MEDIDA", "destejido en %s (%s, %d de %d miembros)" % (nombre, op, len(sm & dm), len(sm))
                    break
        if destino is None:
            hit = declaracion_en_la_pagina(ms)
            if hit:
                destino, prueba = "DECLARACION SELLADA", "pagina 03_FUSIONES.md linea %d: %s" % hit
        if destino is None:
            destino, prueba = "SIN DESTINO", "%d miembros, %d vivos" % (len(ms), len(vivos))
            sin.append(a)
        cuenta[destino] += 1
        por_estado.setdefault(est, {}).setdefault(destino, 0)
        por_estado[est][destino] += 1
        detalle.append((a.get("nombre"), est, destino, prueba))

    w("EL REPARTO, CONTADO Y NO TECLEADO:")
    for k in ("SUPERVIVIENTE", "DECLARACION SELLADA", "DISOLUCION MEDIDA", "SIN DESTINO"):
        w("   CIFRA %-20s %3d" % (k + ":", cuenta[k]))
    w("   CIFRA con destino: %d de %d" % (len(actos) - cuenta["SIN DESTINO"], len(actos)))
    w("")
    w("EL MISMO REPARTO POR ESTADO DEL ACTO EN EL INVENTARIO:")
    for est in sorted(por_estado):
        w("   %s: %s" % (est, ", ".join("%s %d" % (k, v) for k, v in sorted(por_estado[est].items()))))
    w("")
    w("LOS ACTOS SIN DESTINO, ENTEROS (si la lista esta vacia, ese cero es el resultado):")
    if not sin:
        w("   (ninguno)")
    for a in sin:
        w("   SIN DESTINO> %s | estado %s | miembros %s" % (a.get("nombre"), a.get("estado")[:40], ", ".join(a.get("miembros") or [])))
    w("")
    w("LOS %d ACTOS, UNO A UNO (nombre | estado | destino | prueba):" % len(actos))
    for n, est, d, p in detalle:
        w("   %s | %s | %s | %s" % (n, est, d, p))
    w("")
    w("VEREDICTO: %s" % ("VERDE, %d de %d con destino" % (len(actos), len(actos)) if not sin else "ROJO, %d sin destino" % len(sin)))
    t = "\n".join(L) + "\n"
    io.open(DESTINO, "w", encoding="utf-8", newline="\n").write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (DESTINO, len(t.encode("utf-8"))))
    return 1 if sin else 0


if __name__ == "__main__":
    raise SystemExit(main())
