# -*- coding: utf-8 -*-
"""vuelta64_lectura_opm03ii.py . LA LECTURA DE ACTO DE `P.5` Y LAS VARAS POR
FORMA DE `OP-M-03-II`, MEDIDAS HOY Y ANTES DE FUNDIR.

SOLO LECTURA. Es la corrida que la REGLA DE LA FICHA ENVEJECIDA pide (acta 63,
pregunta 1): las mediciones selladas de la ficha se RE-CORREN el dia de la
ejecucion, y si todas las vias convergen se ejecuta con la divergencia declarada.

LO QUE IMPRIME, en este orden:
  1. EL ACTO ENTERO, los dos nodos con todos sus campos de texto, que es lo que
     P.5 pide leer antes de fundir y la pregunta que contesta (UNA familia o DOS);
  2. LAS VARAS POR FORMA de hoy (pasos, condiciones y cableado) contra las que la
     ficha sello el 12 ago 2026, con la divergencia al lado si la hay. EL CABLEADO
     SE CUENTA CON LA VARA DEL INSTRUMENTO, que es la de scripts/plan/simular_fusion.py
     (entrantes sobre nodos NO deprecados, contando los dos campos por separado), y
     al lado va MI cuenta cruda como contraste declarado. Son DOS varas, y la que
     se publica es la del instrumento: es el manejo que el acta 63 ya declaro para
     los enlaces;
  3. LAS BUSQUEDAS NEGATIVAS de cada perdida que el reparto va a sellar, corridas
     sobre el json ENTERO del superviviente. Una busqueda negativa no se puede
     citar si no se corre (regla 9), y aqui se corre ANTES de escribir el plan.
     LAS AGUJAS QUE CASAN CON OTRO SENTIDO SE DECLARAN EN VEZ DE ESTRECHARSE EN
     SILENCIO: la lista SENTIDO_AJENO de abajo lleva cada una con su cita.

Uso: python scripts/loop/vuelta64_lectura_opm03ii.py
"""
import io
import json
import os
import sys
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
ID_OP = "OP-M-03-II"
CAMPOS = ("nodos_previos", "nodos_siguientes")

# Las agujas de cada perdida que el reparto de esta vuelta piensa sellar, en
# ASCII sin tildes. Si alguna sale PRESENTE en el superviviente, la perdida NO
# existe y el reparto se rehace antes de sellar nada.
NEGATIVAS = [
    ("paso 1, el proposito de la reunion",
     ["con calma", "en que punto estas", "evaluar con calma"]),
    ("paso 4, el destino de la rama que pivota",
     ["vuelves al inicio", "y vuelves al"]),
    ("paso 5, los criterios de la decision",
     ["los criterios", "criterios que usaste", "criterio"]),
    ("condicion 1, la cadencia y la puerta de gasto",
     ["cada fase", "antes de invertir", "invertir mas en desarrollo"]),
]

# AGUJAS QUE CASAN PERO CON OTRO SENTIDO, DECLARADAS EN VEZ DE CALLADAS. La
# primera corrida de este instrumento uso la aguja suelta "al inicio" y salio
# PRESENTE; leida en su sitio, es OTRA COSA, y por eso la aguja se estrecha CON
# LA CITA DELANTE en vez de estrecharse en silencio, que seria fabricar la vara.
SENTIDO_AJENO = [
    ("al inicio",
     "vive en el resumen_teorico del superviviente (comparas como trabaja el "
     "cliente en la vida real con lo que habias supuesto AL INICIO), donde "
     "significa AL PRINCIPIO DEL PLAN; el paso 4 del que muere dice VUELVES AL "
     "INICIO del proceso, que es el destino de la rama que pivota. Dos sentidos, "
     "y la aguja que vale es la larga"),
]

CAMPOS_TEXTO = ("titulo_concepto", "resumen_teorico", "entregable_esperado",
                "etiqueta_arbol", "fase_proyecto", "dominio", "fuente")


def sin_acentos(s):
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn")


def nodo(n):
    return json.load(io.open(os.path.join(NODOS, n + ".json"), encoding="utf-8"))


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ficha = None
    for l in io.open(OPS, encoding="utf-8"):
        if l.strip() and json.loads(l).get("id_op") == ID_OP:
            ficha = json.loads(l)
    if ficha is None:
        print("ROJO: %s no esta en OPERACIONES.jsonl. PARADA." % ID_OP)
        return 1
    sup = ficha["superviviente"]
    absorbidos = list(ficha["eliminar"])
    if len(absorbidos) != 1:
        print("ROJO: la ficha declara %d absorbidos y este acto es un par. PARADA."
              % len(absorbidos))
        return 1
    mue = absorbidos[0]

    print("=" * 78)
    print("LECTURA DE ACTO P.5 Y VARAS POR FORMA DE %s, MEDIDAS HOY" % ID_OP)
    print("  ficha: docs/plan/OPERACIONES.jsonl | fecha de corte %s | estado %s"
          % (ficha.get("fecha_corte"), ficha.get("estado")))
    print("  superviviente que la ficha adjudica: %s" % sup)
    print("  absorbe: %s" % mue)
    print("=" * 78)

    print()
    print("--- 1. EL ACTO ENTERO, LEIDO ANTES DE FUNDIR (P.5) ---")
    ns = {}
    for n in (sup, mue):
        d = nodo(n)
        ns[n] = d
        print()
        print("  ### %s   (deprecado: %s)"
              % (n, bool(d.get("deprecado") or d.get("deprecated"))))
        for c in CAMPOS_TEXTO:
            if d.get(c):
                print("     %-20s %s" % (c, d[c]))
        for etq, campo in (("paso", "pasos_accionables"),
                           ("condicion", "condiciones_activacion"),
                           ("previo", "nodos_previos"),
                           ("siguiente", "nodos_siguientes"),
                           ("alias", "ids_alias")):
            v = d.get(campo) or []
            print("     %s (%d):" % (campo, len(v)))
            for i, t in enumerate(v, 1):
                print("        %-9s %d. %s" % (etq, i, t))

    print()
    print("--- 1b. LA PREGUNTA DE P.5: UNA FAMILIA O DOS ---")
    misma = (ns[sup].get("fuente") == ns[mue].get("fuente")
             and ns[sup].get("fase_proyecto") == ns[mue].get("fase_proyecto")
             and ns[sup].get("dominio") == ns[mue].get("dominio"))
    print("  fuente        : %r contra %r" % (ns[sup].get("fuente"), ns[mue].get("fuente")))
    print("  fase_proyecto : %r contra %r"
          % (ns[sup].get("fase_proyecto"), ns[mue].get("fase_proyecto")))
    print("  dominio       : %r contra %r" % (ns[sup].get("dominio"), ns[mue].get("dominio")))
    print("  las tres calzan por maquina: %s" % ("SI" if misma else "NO"))
    print("  UNA sola familia: mismo libro, misma fase, mismo dominio, y los dos")
    print("  titulos son el mismo nombre en dos formas, que es lo que el puesto 268")
    print("  dice y lo que la lectura de los siete pasos contra los cinco confirma.")
    if not misma:
        print("  ROJO: la lectura de acto no sostiene UNA familia. PARADA.")
        return 1

    print()
    print("--- 2. LAS VARAS POR FORMA, MEDIDAS HOY CONTRA LO QUE LA FICHA SELLO ---")
    G = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]

    def grado_instrumento(k):
        """LA VARA DEL INSTRUMENTO, copiada de scripts/plan/simular_fusion.py:
        entrantes sobre nodos NO deprecados, contando los DOS campos por
        separado. Es la que la ficha uso y la que se publica."""
        return sum(1 for _kk, vv in G.items() if not vv.get("deprecado")
                   for c in CAMPOS if k in (vv.get(c) or []))

    def grado_crudo(k):
        """MI CUENTA CRUDA, que es OTRA VARA y va como contraste declarado: cada
        nodo que lo nombra cuenta UNA vez, y los deprecados tambien cuentan."""
        return sum(1 for kk, vv in G.items() if kk != k
                   and any(k in (vv.get(c) or []) for c in CAMPOS))

    p_sup, p_mue = len(ns[sup]["pasos_accionables"]), len(ns[mue]["pasos_accionables"])
    c_sup = len(ns[sup].get("condiciones_activacion") or [])
    c_mue = len(ns[mue].get("condiciones_activacion") or [])
    g_sup, g_mue = grado_instrumento(sup), grado_instrumento(mue)
    x_sup, x_mue = grado_crudo(sup), grado_crudo(mue)
    print("  %-22s pasos %2d | condiciones %2d | LO NOMBRAN %2d (vara del instrumento)"
          % (sup, p_sup, c_sup, g_sup))
    print("  %-22s pasos %2d | condiciones %2d | LO NOMBRAN %2d (vara del instrumento)"
          % (mue, p_mue, c_mue, g_mue))
    print()

    def apunta(a, b):
        return sup if a > b else (mue if b > a else "EMPATE")
    print("  vara de PASOS       %2d contra %2d -> apunta a %s"
          % (p_sup, p_mue, apunta(p_sup, p_mue)))
    print("  vara de CONDICIONES %2d contra %2d -> apunta a %s"
          % (c_sup, c_mue, apunta(c_sup, c_mue)))
    print("  vara de CABLEADO    %2d contra %2d -> apunta a %s"
          % (g_sup, g_mue, apunta(g_sup, g_mue)))
    print()
    print("  LAS DOS VARAS DE CONTENIDO CHOCAN (pasos a un lado, condiciones al otro),")
    print("  y en un CHOCAN decide LA PIEZA DECLARADA (acta 53, pregunta 3), que aqui")
    print("  es la adjudicacion sellada de la ficha y nombra a %s." % sup)
    print("  EL CABLEADO NO ENTRA: P.8 dice que el cableado DESEMPATA y no decide, y")
    print("  solo habla a contenido EMPATADO. Aqui el contenido NO empata.")
    print()
    print("  UNA VARA MIA DICHA, y son DOS varas y no una discrepancia: mi cuenta")
    print("  cruda (cada nodo que lo nombra UNA vez, y los deprecados tambien) da")
    print("  %d contra %d. La que se publica es la del instrumento, que es la que la"
          % (x_mue, x_sup))
    print("  ficha uso. Es el mismo manejo que el acta 63 declaro para los enlaces.")
    print()
    print("  LO QUE LA FICHA SELLO EL 12 ago 2026, citado como CONTRASTE y no como")
    print("  fuente (regla 2): el cableado da 10 a %s contra 5 a %s, y AUN ASI pierde."
          % (mue, sup))
    calza = (g_mue, g_sup) == (10, 5)
    print("  MEDIDO HOY con la vara del instrumento: %d contra %d. %s"
          % (g_mue, g_sup,
             "CALZA AL DIGITO con la ficha." if calza
             else "NO CALZA, y la divergencia se declara en el motivo del plan."))

    print()
    print("--- 3. LAS BUSQUEDAS NEGATIVAS DE LAS PERDIDAS, CORRIDAS Y NO CITADAS ---")
    entero = sin_acentos(json.dumps(ns[sup], ensure_ascii=False).lower())
    print("  json ENTERO de %s: %d caracteres" % (sup, len(entero)))
    malas = []
    total = 0
    for etq, agujas in NEGATIVAS:
        print("  %s:" % etq)
        for a in agujas:
            total += 1
            pres = sin_acentos(a.lower()) in entero
            if pres:
                malas.append((etq, a))
            print("     %-34s %s" % (a, "PRESENTE" if pres else "AUSENTE"))
    print()
    print("  AGUJAS QUE CASAN CON OTRO SENTIDO, DECLARADAS Y NO ESTRECHADAS EN SILENCIO:")
    for a, motivo in SENTIDO_AJENO:
        pres = sin_acentos(a.lower()) in entero
        print("     %-34s %s" % (a, "PRESENTE" if pres else "AUSENTE"))
        print("        %s" % motivo)
    print()
    if malas:
        print("  ROJO: %d aguja(s) PRESENTES en el superviviente. Esas perdidas NO"
              % len(malas))
        print("  existen y el reparto se rehace antes de sellar nada:")
        for etq, a in malas:
            print("     %s -> %r" % (etq, a))
        return 1
    print("  LAS %d AGUJAS, TODAS AUSENTES: las cuatro perdidas del reparto existen."
          % total)

    print()
    print("--- 4. LA JUNTURA DEL UNICO INCISO, COMPROBADA ANTES DE SELLAR ---")
    p7 = ns[sup]["pasos_accionables"][6]
    p4 = ns[mue]["pasos_accionables"][3]
    print("  paso 7 del superviviente: %s" % p7)
    print("  acaba en punto: %s" % p7.rstrip().endswith((".", "!", "?")))
    print("  paso 4 del que muere    : %s" % p4)
    trozo = "hacia la validacion con clientes"
    print("  el trozo pedido en ASCII: %r" % trozo)
    print("  casa dentro del paso 4 sin tildes: %s"
          % (sin_acentos(trozo.lower()) in sin_acentos(p4.lower())))
    print("  paso resultante previsto: %s %s" % (p7, trozo))
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
