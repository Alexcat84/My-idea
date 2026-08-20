"""Vuelta 47, TAREA 3.2: LA LECTURA DE CERO DE OP-U-01, ANTES DE TOCAR NADA.

OP-U-01 es la primera operacion de la fase 03 por el criterio adjudicado en esta misma
vuelta (docs/plan/03_FUSIONES.md, EL ORDEN DE ESTA FASE). Antes de abrirla se lee
ENTERA del fichero y se RE-MIDE su nomina contra el grafo de hoy, porque la cifra que
la operacion publica (280 actos cerrados sobre 600 nodos, corte 3.388) se midio en la
vuelta 12, ANTES de que las fases 01 y 02 fundieran y deprecaran nodos. La regla 2 de
EJECUTOR.md es explicita: una nota vieja nunca es fuente de una cifra nueva.

De solo lectura. No escribe ni un nodo ni una operacion.

La nomina de hoy la produce el instrumento de la casa,
scripts/plan/recomputo_3388.py --salida docs/loop/RECOMPUTO_V47_COMPONENTES.jsonl,
que resuelve por alias ANTES de contar (P.1). Este instrumento la LEE y la contrasta
contra la nomina SELLADA docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl, que NO se toca.

Uso: python scripts/loop/vuelta47_lectura_opu01.py
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
SELLADA = os.path.join(RAIZ, "docs", "plan", "RECOMPUTO_3388_COMPONENTES.jsonl")
HOY = os.path.join(RAIZ, "docs", "loop", "RECOMPUTO_V47_COMPONENTES.jsonl")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")

# Los cuatro actos que 03_FUSIONES.md declara que NO se resuelven en OP-U-01 nunca:
# el de 13 y el de 9 van a mesa, y dos grandes van a destejido.
AJENOS = {
    "OP-M-01": "gates_go_kill_decision_points",
    "OP-M-05": "customer_discovery",
    "OP-D-03": "ab_testing_optimizacion",
    "OP-D-04": "brainstorming_divergente",
}


def sep(t):
    print()
    print("=" * 78)
    print(t)
    print("=" * 78)


def cargar(p):
    return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]


def main():
    ops = cargar(OPS)
    op = [o for o in ops if o["id_op"] == "OP-U-01"]
    if not op:
        print("PARADA: OP-U-01 no esta en el fichero")
        return 2
    op = op[0]

    sep("1. OP-U-01 LEIDA ENTERA DEL FICHERO, CAMPO POR CAMPO")
    print("  campos en la linea: %d" % len(op))
    for k in op:
        v = op[k]
        if isinstance(v, list):
            print("  %-18s lista de %d" % (k, len(v)))
            for i, x in enumerate(v, 1):
                print("      %d. %s" % (i, x if len(str(x)) < 400
                                        else str(x)[:400] + " [...]"))
        elif isinstance(v, str) and len(v) > 400:
            print("  %-18s texto de %d caracteres" % (k, len(v)))
            print("      %s [...]" % v[:400])
        else:
            print("  %-18s %s" % (k, v))

    sep("2. LA NOMINA DE HOY CONTRA LA NOMINA SELLADA")
    sell = cargar(SELLADA)
    hoy = cargar(HOY)
    print("  sellada : %s" % os.path.relpath(SELLADA, RAIZ).replace("\\", "/"))
    print("  de hoy  : %s" % os.path.relpath(HOY, RAIZ).replace("\\", "/"))
    print()
    campos = sorted(set(sell[0].keys()))
    print("  campos de cada fila: %s" % campos)

    def clave(c):
        return tuple(sorted(c.get("miembros") or c.get("nodos") or []))

    def estado(c):
        for k in ("estado", "cerrado", "clase"):
            if k in c:
                return c[k]
        return "?"

    ss = {clave(c): c for c in sell}
    hh = {clave(c): c for c in hoy}
    print()
    print("  %-34s %8s %8s" % ("", "sellada", "hoy"))
    print("  %-34s %8d %8d" % ("actos (componentes)", len(sell), len(hoy)))
    print("  %-34s %8d %8d" % ("nodos dentro de actos",
                               sum(len(clave(c)) for c in sell),
                               sum(len(clave(c)) for c in hoy)))
    cer_s = [c for c in sell if str(estado(c)).upper().startswith("CERRAD")]
    cer_h = [c for c in hoy if str(estado(c)).upper().startswith("CERRAD")]
    print("  %-34s %8d %8d" % ("CERRADOS", len(cer_s), len(cer_h)))
    print("  %-34s %8d %8d" % ("nodos en CERRADOS",
                               sum(len(clave(c)) for c in cer_s),
                               sum(len(clave(c)) for c in cer_h)))
    print("  %-34s %8d %8d" % ("ABIERTOS", len(sell) - len(cer_s),
                               len(hoy) - len(cer_h)))

    solo_sell = sorted(set(ss) - set(hh))
    solo_hoy = sorted(set(hh) - set(ss))
    print()
    print("  actos de la sellada que HOY ya no estan igual: %d" % len(solo_sell))
    print("  actos de hoy que la sellada no tenia igual   : %d" % len(solo_hoy))

    sep("3. POR QUE SE MOVIO: LOS NODOS QUE LA SELLADA CONTABA Y HOY ESTAN DEPRECADOS")
    g = json.load(io.open(GRAFO, encoding="utf-8"))
    nodos = g["nodos"]
    vivos = {k for k, v in nodos.items() if not v.get("deprecado")}
    deprec = {k for k, v in nodos.items() if v.get("deprecado")}
    print("  grafo: %d vivos, %d deprecados" % (len(vivos), len(deprec)))
    en_sellada = set()
    for c in sell:
        en_sellada.update(clave(c))
    muertos = sorted(en_sellada & deprec)
    print("  nodos que la nomina SELLADA contaba y hoy estan DEPRECADOS: %d"
          % len(muertos))
    for m in muertos:
        print("      %s" % m)
    print()
    print("  LECTURA: cada uno de esos lo absorbio una fusion de las fases 01 o 02,")
    print("  que corrieron DESPUES de sellarse la nomina. Por eso la cifra de la")
    print("  operacion (280 sobre 600) no se copia: se re-mide.")

    sep("4. LOS CUATRO ACTOS QUE ESTA OPERACION NO RESUELVE NUNCA")
    print("  03_FUSIONES.md los nombra: el de 13 y el de 9 van a mesa (OP-M-01 y")
    print("  OP-M-05) y dos grandes van a destejido (OP-D-03 y OP-D-04).")
    print()
    for dueno, ancla in sorted(AJENOS.items()):
        halladas = [(len(clave(c)), estado(c)) for c in hoy if ancla in clave(c)]
        if not halladas:
            print("  %-10s ancla %-38s NO aparece en ninguna componente de hoy"
                  % (dueno, ancla))
        for tam, est in halladas:
            print("  %-10s ancla %-38s componente de %d, %s"
                  % (dueno, ancla, tam, est))
    print()
    print("  GUARDA: ninguno de los cuatro puede aparecer como CERRADO y entrar en")
    print("  el lote de OP-U-01. Si alguno aparece CERRADO, esta operacion NO lo")
    print("  toca: su dueno esta escrito en otra fase.")

    sep("5. EL LOTE REAL DE OP-U-01, HOY, POR TAMANO")
    porta = {}
    for c in cer_h:
        t = len(clave(c))
        porta[t] = porta.get(t, 0) + 1
    print("  CERRADOS por tamano: %s" % dict(sorted(porta.items())))
    print("  total de actos a fundir: %d" % len(cer_h))
    print("  total de nodos implicados: %d" % sum(len(clave(c)) for c in cer_h))
    print("  nodos que MUEREN si se funden todos (tamano menos 1 por acto): %d"
          % sum(len(clave(c)) - 1 for c in cer_h))
    print()
    print("  Y NINGUNO DE ESOS ACTOS TRAE SU SUPERVIVIENTE ESCRITO: el campo")
    print("  superviviente de OP-U-01 es null y sus nodos son lista vacia. La")
    print("  eleccion la dan las DOS REGLAS DE EJECUCION de 03_FUSIONES.md")
    print("  (sobrevive por CONTENIDO; a contenido empatado desempata el grafo) mas")
    print("  P.8, acto por acto y con lectura escrita. Eso es lo que hace que esta")
    print("  operacion se ejecute POR TRAMOS y no en una sentada.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
