# -*- coding: utf-8 -*-
"""vuelta65_colisiones_esperadas.py . LA CUENTA ESPERADA DE COLISIONES DE CLASE
DEL LOTE A DE OP-U-02, SIMULADA SOBRE EL ARBOL DE ANTES DE FUNDIR.

SE MIDE ANTES Y NO DESPUES, Y ESA ES LA MITAD DEL PUNTO. Es la leccion del D5 de
la vuelta 64, registrada por el acta 64: la cuenta esperada se midio DESPUES de
fundir y quedo como caida de procedimiento autodeclarada. Aqui se mide antes,
sobre el arbol tal como esta, simulando la fusion EN MEMORIA sin tocar un nodo.

LA LINEA BASE ES 2 Y ESTA DECLARADA (acta 64, pregunta 3): las dos colisiones
que OP-M-03-II dejo vigentes son de la mesa OP-M-03 y las resuelve la mesa en su
turno. Toda operacion corre el censo con esperadas MEDIDAS sobre esa base, y un
delta no predicho por la operacion es PARADA de guarda.

LA MAQUINA DEL CENSO ES LA DE scripts/loop/vuelta51_censo_colisiones.py, copiada
de sus lineas 45 a 70 y no re-inventada: mapa de alias construido SOLO con nodos
VIVOS, veredictos agrupados por su PAR RESUELTO, auto-pares separados y no
contados como colision, y colision es un grupo con DOS O MAS clases publicadas.
LO UNICO QUE SE ANADE es la simulacion: al mapa de alias se le suma, EN MEMORIA,
lo que la fusion del plan haria (cada absorbido pasa a resolver al superviviente
de su acto).

DE SOLO LECTURA ENTERO. No escribe ni un nodo.

Uso:
  python scripts/loop/vuelta65_colisiones_esperadas.py --plan docs/loop/PLAN_V65_OPU02_LOTE_A.json
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
NL = chr(10)


def alias_vivos():
    """COPIA de vuelta51_censo_colisiones.py: solo nodos VIVOS aportan alias."""
    alias = {}
    for nombre in sorted(os.listdir(NODOS)):
        if not nombre.endswith(".json"):
            continue
        d = json.load(io.open(os.path.join(NODOS, nombre), encoding="utf-8"))
        if d.get("deprecado") or d.get("deprecated"):
            continue
        for x in (d.get("ids_alias") or []):
            alias[x] = d["node_id"]
    return alias


def censar(alias):
    """COPIA LITERAL DE LA ARITMETICA de vuelta51_censo_colisiones.py, lineas 56 a
    72. LA PRIMERA VERSION DE ESTE FICHERO NO ERA COPIA Y SE DICE: conto los
    AUTO-PARES por VEREDICTO (dio 278) donde el censo de la casa los cuenta por
    GRUPO RESUELTO DISTINTO (da 256, la cifra publicada en la cabecera de la
    vuelta 64). Dos instrumentos de la campana contando distinto en silencio es
    justo lo que la regla 2 persigue, y por eso aqui se agrupa primero y se
    separan despues los grupos de UN solo elemento, igual que el ancestro."""
    def res(x):
        return alias.get(x, x)

    grupos = {}
    for l in io.open(VER, encoding="utf-8"):
        if not l.strip():
            continue
        v = json.loads(l)
        na, nb = res(v["nodo_a"]), res(v["nodo_b"])
        grupos.setdefault(frozenset((na, nb)), []).append((v.get("clase") or "").upper())
    auto = [k for k in grupos if len(k) == 1]
    col = {k: sorted(set(vs)) for k, vs in grupos.items()
           if len(k) > 1 and len(set(vs)) > 1}
    return col, len(auto)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", required=True)
    ap.add_argument("--base", type=int, default=2,
                    help="la linea base declarada del censo (acta 64, pregunta 3)")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    plan = json.load(io.open(os.path.join(RAIZ, a.plan.replace("/", os.sep)), encoding="utf-8"))
    print("=" * 78)
    print("LA CUENTA ESPERADA DE COLISIONES, SIMULADA ANTES DE FUNDIR")
    print("  plan       : %s" % a.plan)
    print("  operacion  : %s" % plan.get("operacion"))
    print("  linea base : %d, DECLARADA (acta 64, pregunta 3)" % a.base)
    print("=" * 78)

    alias = alias_vivos()
    antes, auto_antes = censar(alias)
    print()
    print("  ANTES DE FUNDIR (el arbol tal como esta, medido ahora):")
    print("     COLISIONES DE CLASE VIGENTES : %d" % len(antes))
    print("     AUTO-PARES                   : %d" % auto_antes)
    for k in sorted(antes, key=lambda s: sorted(s)):
        print("        %s | clases %s" % (" contra ".join(sorted(k)), antes[k]))
    if len(antes) != a.base:
        print()
        print("  ROJO: el censo de ANTES da %d y la linea base declarada es %d."
              % (len(antes), a.base))
        print("  PARADA: la base se mide, no se supone.")
        return 1

    # LA SIMULACION: cada absorbido pasa a resolver a su superviviente.
    simulado = dict(alias)
    movidos = 0
    for acto in plan["actos"]:
        for muere in acto["absorbidos"]:
            simulado[muere] = acto["superviviente"]
            movidos += 1
    print()
    print("  LA SIMULACION EN MEMORIA: %d absorbido(s) de %d acto(s) pasan a resolver a su "
          "superviviente. NO SE TOCA NI UN NODO." % (movidos, len(plan["actos"])))

    despues, auto_despues = censar(simulado)
    print()
    print("  DESPUES DE FUNDIR (simulado):")
    print("     COLISIONES DE CLASE VIGENTES : %d" % len(despues))
    print("     AUTO-PARES                   : %d" % auto_despues)
    for k in sorted(despues, key=lambda s: sorted(s)):
        print("        %s | clases %s" % (" contra ".join(sorted(k)), despues[k]))

    nuevas = {k: v for k, v in despues.items() if k not in antes}
    idas = {k: v for k, v in antes.items() if k not in despues}
    print()
    print("  EL DELTA, QUE ES LO QUE LA GUARDA MIRA:")
    print("     colisiones NUEVAS que la fusion fabricaria : %d" % len(nuevas))
    for k in sorted(nuevas, key=lambda s: sorted(s)):
        print("        %s | clases %s" % (" contra ".join(sorted(k)), nuevas[k]))
    print("     colisiones que DESAPARECERIAN              : %d" % len(idas))
    for k in sorted(idas, key=lambda s: sorted(s)):
        print("        %s | clases %s" % (" contra ".join(sorted(k)), idas[k]))
    print("     auto-pares NUEVOS (pares internos del acto): %d" % (auto_despues - auto_antes))
    print()
    print("  ESPERADAS TRAS FUNDIR = %d, y es %d de base mas %d nuevas menos %d idas"
          % (a.base + len(nuevas) - len(idas), a.base, len(nuevas), len(idas)))
    print()
    if nuevas:
        print("LA FUSION FABRICA COLISIONES Y HAY QUE PREDECIRLAS EN EL PLAN.")
    else:
        print("LA FUSION NO FABRICA NI UNA COLISION: la cuenta esperada del censo de cierre")
        print("es la linea base, %d." % (a.base - len(idas)))
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
