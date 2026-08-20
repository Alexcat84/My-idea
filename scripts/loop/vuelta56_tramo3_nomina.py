# -*- coding: utf-8 -*-
"""vuelta56_tramo3_nomina.py . EL ABRIDOR DEL TRAMO 3 DE OP-U-01, DETERMINADO
POR MEDICION Y POR DOS CAMINOS.

DE SOLO LECTURA. No toca ni un nodo, ni un veredicto, ni una operacion:
imprime, y solo escribe el fichero que se le nombre en --salida.

LA ARITMETICA ES LA DE LOS DOS INSTRUMENTOS DEL TRAMO 2, COPIADA Y NO
REINVENTADA, y se dice DE CUAL SE COPIA CADA PIEZA porque no son la misma:

  IDENTIDAD POR MIEMBROS, del sucesor de la vuelta 55
  (scripts/loop/vuelta55_tramo2_nomina.py). Un acto no es su numero: es el
  conjunto de ids que nombraba el dia en que su tramo se definio. Por esa
  vara, la LECTURA B del tramo 3 son LOS CINCUENTA ACTOS QUE OCUPABAN LOS
  PUESTOS 101 A 150 DE LA NOMINA DE LA VUELTA 48
  (docs/loop/RECOMPUTO_V48_COMPONENTES.jsonl).

  EL ORDINAL SE DERIVA DEL FICHERO Y NO SE TECLEA, del ABRIDOR de la vuelta
  54 (scripts/loop/vuelta54_tramo2_nomina.py, "for n, (i, r) in
  enumerate(tramo2, 1)"): el ordinal del acto (1 a 50) es SU POSICION EN EL
  ORDEN IMPRESO DE HOY. AQUI SE COPIA EL ABRIDOR Y NO EL SUCESOR, y el motivo
  va escrito: el sucesor derivaba el ordinal del puesto de la 48 menos 50
  porque aquel tramo YA ESTABA ABIERTO y sus ordinales YA ESTABAN PUBLICADOS,
  y cambiarlos habria movido cifras citadas. El tramo 3 se ABRE hoy y no tiene
  ordinal publicado que respetar, asi que la cuenta que toca es la del
  abridor. El puesto de la 48 se imprime AL LADO, en su columna, y dice
  "nuevo" cuando el acto no existia como CERRADO aquel dia.

LOS DOS CAMINOS QUE SE COMPARAN, que es lo que hace que el tramo este
DETERMINADO y no decidido:

  LECTURA A, por el orden de HOY: se re-mide la nomina hoy, se marcan los
  actos de los tramos 1 y 2 que siguen vivos (POR SUS MIEMBROS), se comprueba
  que ocupan un PREFIJO EXACTO de la nomina impresa, y el tramo 3 son los 50
  actos CERRADOS siguientes en el orden impreso.

  LECTURA B, por el orden del dia en que los tramos se definieron: el tramo 3
  son los que ocupaban los puestos 101 a 150 de la nomina de la vuelta 48.

SI LAS DOS COINCIDEN EN CONJUNTO Y EN ORDEN, el tramo esta determinado y no
hay nada que decidir. SI NO COINCIDEN, este instrumento NO elige a ojo: primero
DIAGNOSTICA la divergencia, y solo hay dos formas que la dejan explicada.

  LA VARA VIGENTE ES LA LECTURA A, y esta escrita en docs/plan/03_FUSIONES.md
  desde la vuelta 48, en la cabecera del registro del tramo 1: "El tramo son
  los CINCUENTA primeros actos CERRADOS de la NOMINA RE-MEDIDA AL ABRIRLO, en
  el orden en que el instrumento los imprime, que es la vara que el auditor
  adjudico". La lectura B no es una vara rival: es la comprobacion de que
  entre una apertura y la siguiente no ha pasado nada que el ejecutor no haya
  medido. Por eso la divergencia no se resuelve eligiendo: se EXPLICA.

  LAS DOS UNICAS FORMAS EXPLICADAS, y las dos se comprueban con el fichero
  delante:
    (a) un acto que esta en A y no en B tiene que ser un acto que NO EXISTIA
        como CERRADO en la nomina de la 48 (un CERRADO NACIDO DESPUES: en la
        48 estaba ABIERTO, o partido, o no estaba). Se imprime en que estado
        estaba cada uno de sus miembros aquel dia.
    (b) un acto que esta en B y no en A tiene que CAER HOY DETRAS del corte,
        o sea en un puesto mayor que el ultimo del tramo: esta DESPLAZADO al
        tramo siguiente, no perdido, y se nombra con su puesto de hoy.
  Cualquier otra divergencia (un acto que estaba CERRADO en la 48 dentro de
  otro tramo y hoy se cuela, un acto de B que hoy desaparece sin estar fundido
  limpio, o un desorden dentro del corte) NO esta explicada: es ROJO y PARADA.

LO QUE ESTE ABRIDOR ANADE A LOS DOS ANTERIORES, y va declarado porque es lo
unico que no es copia:

  1. LA GUARDA DEL PREFIJO. El encargo de la vuelta 56 dice que el tramo 3
     empieza "tras el prefijo de los 16 vivos". Ese 16 NO se teclea: se MIDE
     (los actos de hoy que tocan miembros de los tramos 1 o 2) y ademas se
     comprueba que esos actos ocupan los puestos 1 a N sin huecos. Si el
     prefijo tuviera un hueco, la frase "los 50 siguientes" no estaria
     determinada y seria ROJO.
  2. EL ESTADO DE CADA UNO DE LOS 50 DEL TRAMO 3 CONTRA EL GRAFO. Igual que
     el sucesor de la 55 hacia con el tramo 2: si un acto del tramo 3 ya no
     aparece hoy, tiene que estar FUNDIDO limpio (sus ids resuelven a UNO, uno
     esta deprecado y el vivo lleva el alias izado). El tramo 3 se abre HOY y
     no deberia haber ninguno, pero se MIDE en vez de darse por supuesto.
  3. LA FIGURA DE CADA ACTO, DICHA Y NO FORZADA. El encargo manda decir que
     acto del corte no es de fusion pura (tamano 2 y PURO A). Este
     instrumento los NOMBRA uno a uno para que tomen su carril; no los aparta
     ni los fuerza.
  4. LA GUARDA DE LOS CUATRO AJENOS, LEIDA POR DOS CAMINOS. La regla 9 del
     EJECUTOR manda que todo conteo que toque ids pase por el resolutor
     (P.1). Los abridores anteriores buscaban los cuatro ids LITERALES en los
     miembros; aqui se buscan ademas RESUELTOS, porque un ajeno deprecado
     vive hoy dentro del ids_alias de su superviviente y por el camino
     literal la guarda pasaria POR VACIO sin que nadie lo sepa. Los dos
     caminos se imprimen SIEMPRE, calcen o no.

LAS DOS GUARDAS DE SIEMPRE, copiadas: la de los cuatro ajenos y la de solape,
esta vez con los DOS tramos anteriores.

Uso:
  python scripts/loop/vuelta56_tramo3_nomina.py --nomina <RECOMPUTO del dia> \
        [--salida docs/loop/TRAMO3_V56.jsonl]
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
V48 = os.path.join(RAIZ, "docs", "loop", "RECOMPUTO_V48_COMPONENTES.jsonl")
NODOS = os.path.join(RAIZ, "dataset", "nodos")

# 03_FUSIONES.md declara desde el 11 ago 2026 que estos cuatro no se resuelven
# nunca en OP-U-01. Misma lista, palabra por palabra, que la de los abridores
# de los tramos 1 y 2.
AJENOS = ["gates_go_kill_decision_points", "customer_discovery",
          "ab_testing_optimizacion", "brainstorming_divergente"]

TAM_TRAMO = 50
TRAMO = 3


def cargar(p):
    return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]


def leer_nodo(nid):
    p = os.path.join(NODOS, nid + ".json")
    if not os.path.exists(p):
        return None
    return json.load(io.open(p, encoding="utf-8"))


def mapa_alias():
    """EL RESOLUTOR DE P.1, con la aritmetica COPIADA de la del instrumento que
    publica el censo (scripts/loop/vuelta51_censo_colisiones.py, lineas 42 a 53):
    el nodo deprecado NO lleva campo de reenvio; es el nodo VIVO el que iza los
    ids del muerto en su campo ids_alias. Se recorre el catalogo vivo y se
    invierte ese campo."""
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nomina", required=True)
    ap.add_argument("--salida", default=None)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    hoy = [r for r in cargar(a.nomina) if r["estado"] == "CERRADO"]
    v48 = [r for r in cargar(V48) if r["estado"] == "CERRADO"]
    alias = mapa_alias()
    resolver = lambda x: alias.get(x, x)

    print("=" * 78)
    print("EL ABRIDOR DEL TRAMO %d DE OP-U-01 (vuelta 56)" % TRAMO)
    print("identidad POR MIEMBROS del sucesor de la 55; ordinal del ABRIDOR de la 54")
    print("=" * 78)
    print()
    print("  nomina de hoy   : %s (%d actos CERRADOS)" % (a.nomina, len(hoy)))
    print("  nomina de la 48 : %s (%d actos CERRADOS)" % (os.path.relpath(V48, RAIZ), len(v48)))
    print()

    # ---- los tramos ya abiertos, por sus miembros ----
    print("--- LOS TRAMOS YA ABIERTOS, IDENTIFICADOS POR SUS MIEMBROS ---")
    previos = {}
    for t in (1, 2):
        bloque = v48[(t - 1) * TAM_TRAMO:t * TAM_TRAMO]
        mi = set()
        for r in bloque:
            mi |= set(r["miembros"])
        vivos = [i for i, r in enumerate(hoy, 1) if set(r["miembros"]) & mi]
        previos[t] = {"miembros": mi, "vivos": vivos}
        print("  tramo %d: %d actos en la 48, %d miembros, %d vivos hoy en los puestos %s"
              % (t, len(bloque), len(mi), len(vivos), vivos))
    mi_previos = previos[1]["miembros"] | previos[2]["miembros"]
    prefijo = sorted(set(previos[1]["vivos"]) | set(previos[2]["vivos"]))
    print()

    # ---- GUARDA DEL PREFIJO: los vivos ocupan los puestos 1..N, sin huecos ----
    print("--- GUARDA DEL PREFIJO (el 16 se MIDE, no se teclea) ---")
    print("  actos vivos de los tramos 1 y 2 : %d" % len(prefijo))
    print("  puestos que ocupan hoy          : %s" % prefijo)
    contiguo = prefijo == list(range(1, len(prefijo) + 1))
    print("  ocupan los puestos 1 a %d sin huecos: %s"
          % (len(prefijo), "SI" if contiguo else "NO"))
    if not contiguo:
        print()
        print("  ROJO: el prefijo tiene huecos, asi que los 50 siguientes no")
        print("  estan determinados por el texto. PARADA.")
        return 1
    print()

    # ---- LECTURA A: los 50 CERRADOS siguientes en el orden impreso de HOY ----
    resto = [(i, r) for i, r in enumerate(hoy, 1) if not (set(r["miembros"]) & mi_previos)]
    lectA = resto[:TAM_TRAMO]
    print("--- LECTURA A: los %d CERRADOS siguientes en el orden impreso de HOY ---" % TAM_TRAMO)
    print("  actos CERRADOS fuera de los tramos 1 y 2: %d" % len(resto))
    if len(lectA) < TAM_TRAMO:
        print()
        print("  ROJO: no hay %d actos para el tramo. PARADA." % TAM_TRAMO)
        return 1
    print("  puestos de hoy del tramo %d: del %d al %d" % (TRAMO, lectA[0][0], lectA[-1][0]))
    print()

    # ---- LECTURA B: los puestos 101 a 150 de la nomina de la 48 ----
    desde, hasta = (TRAMO - 1) * TAM_TRAMO + 1, TRAMO * TAM_TRAMO
    tramo3_48 = v48[desde - 1:hasta]
    print("--- LECTURA B: los que ocupaban los puestos %d a %d de la nomina de la 48 ---"
          % (desde, hasta))
    print("  actos que definen el tramo %d: %d" % (TRAMO, len(tramo3_48)))
    print()

    filas = []
    rojo = []
    for n, r48 in enumerate(tramo3_48, 1):
        mi = set(r48["miembros"])
        aqui = [(i, r) for i, r in enumerate(hoy, 1) if set(r["miembros"]) & mi]
        if len(aqui) > 1:
            rojo.append((n, "el acto se parte hoy en %d componentes" % len(aqui)))
        if aqui:
            i, r = aqui[0]
            filas.append({"orden": n, "estado_hoy": "VIVO", "puesto_hoy": i,
                          "puesto_v48": (TRAMO - 1) * TAM_TRAMO + n, "acto": r})
        else:
            # tendria que estar FUNDIDO, y se comprueba contra el grafo.
            res = sorted({resolver(m) for m in r48["miembros"]})
            muertos = [m for m in sorted(mi)
                       if (leer_nodo(m) or {}).get("deprecado") is True]
            vivo = [m for m in sorted(mi) if m not in muertos]
            ok = (len(res) == 1 and len(muertos) == len(mi) - 1 and len(vivo) == 1)
            izado = False
            if len(vivo) == 1:
                nv = leer_nodo(vivo[0]) or {}
                al = nv.get("ids_alias") or []
                izado = all(m in al for m in muertos)
            filas.append({"orden": n, "estado_hoy": "FUNDIDO", "puesto_hoy": None,
                          "puesto_v48": (TRAMO - 1) * TAM_TRAMO + n, "acto": None,
                          "miembros": sorted(mi),
                          "superviviente": vivo[0] if len(vivo) == 1 else None,
                          "absorbidos": muertos, "resuelven_a": res,
                          "alias_izado": izado})
            if not ok:
                rojo.append((n, "ni vivo ni fundido limpio: resuelven a %s, muertos %s"
                             % (res, muertos)))

    vivos = [f for f in filas if f["estado_hoy"] == "VIVO"]
    fundidos = [f for f in filas if f["estado_hoy"] == "FUNDIDO"]
    print("  VIVOS hoy   : %d" % len(vivos))
    print("  FUNDIDOS    : %d" % len(fundidos))
    print("  suma        : %d de %d" % (len(vivos) + len(fundidos), len(tramo3_48)))
    if fundidos:
        print()
        print("  --- LOS FUNDIDOS, COMPROBADOS CONTRA EL GRAFO UNO A UNO ---")
        for f in fundidos:
            print("    acto %-3d superviviente %-44s absorbido %-44s resuelven a UNO: %-3s alias izado: %s"
                  % (f["orden"], f["superviviente"], ", ".join(f["absorbidos"]),
                     "SI" if len(f["resuelven_a"]) == 1 else "NO",
                     "SI" if f["alias_izado"] else "NO"))
    if rojo:
        print()
        for n, m in rojo:
            print("     acto %d: %s" % (n, m))
        print("  ROJO DE VERDAD. PARADA.")
        return 1
    print()

    # ---- LAS DOS LECTURAS, COMPARADAS ----
    print("--- LAS DOS LECTURAS, COMPARADAS EN CONJUNTO Y EN ORDEN ---")
    clave = lambda ms: tuple(sorted(ms))
    porV48 = [clave(f["acto"]["miembros"]) for f in sorted(vivos, key=lambda f: f["puesto_v48"])]
    porHOY = [clave(r["miembros"]) for _, r in lectA]
    iguales = porV48 == porHOY
    print("  LECTURA A (orden de HOY) y LECTURA B (orden de la 48): %s"
          % ("CALZAN, mismo conjunto y mismo orden" if iguales else "NO CALZAN"))
    divergencia = None
    if not iguales:
        sa, sb = set(porHOY) - set(porV48), set(porV48) - set(porHOY)
        print("  solo en A: %d | solo en B: %d" % (len(sa), len(sb)))
        print()
        print("  --- LA DIVERGENCIA, DIAGNOSTICADA CON EL FICHERO DELANTE ---")
        # el estado de cada miembro en la nomina ENTERA de la 48 (CERRADOS y ABIERTOS)
        v48_todo = cargar(V48)
        estado48 = {}
        for i, r in enumerate(v48_todo, 1):
            for m in r["miembros"]:
                estado48.setdefault(m, (i, r["estado"], r["tamano"], sorted(r["miembros"])))
        idx48c = {}
        for i, r in enumerate(v48, 1):
            for m in r["miembros"]:
                idx48c.setdefault(m, i)

        sin_explicar = []
        for c in sorted(sa):
            puestos_c = sorted({idx48c[m] for m in c if m in idx48c})
            nacido = not puestos_c
            print("    SOLO EN A: %s" % (", ".join(c)))
            for m in c:
                e = estado48.get(m)
                donde = ("componente %d, %s, tamano %d: %s"
                         % (e[0], e[1], e[2], ", ".join(e[3]))) if e else "NO APARECIA"
                print("       %-42s en la nomina de la 48: %s" % (m, donde))
            if nacido:
                print("       EXPLICADO: CERRADO NACIDO DESPUES de la nomina de la 48.")
            else:
                print("       NO EXPLICADO: ya era CERRADO en la 48, en los puestos %s." % puestos_c)
                sin_explicar.append(("A", c))
        ultimo = lectA[-1][0]
        for c in sorted(sb):
            aqui = [i for i, r in enumerate(hoy, 1) if set(r["miembros"]) == set(c)]
            print("    SOLO EN B: %s" % (", ".join(c)))
            print("       puesto en la nomina de la 48: %s"
                  % sorted({idx48c[m] for m in c if m in idx48c}))
            print("       puesto HOY                  : %s (el corte acaba en el %d)"
                  % (aqui if aqui else "NO APARECE", ultimo))
            if aqui and min(aqui) > ultimo:
                print("       EXPLICADO: DESPLAZADO al tramo siguiente, no perdido.")
            else:
                print("       NO EXPLICADO.")
                sin_explicar.append(("B", c))
        print()
        if sin_explicar:
            print("  ROJO: %d divergencias SIN EXPLICAR. El tramo NO esta determinado. PARADA."
                  % len(sin_explicar))
            return 1
        print("  DIVERGENCIA EXPLICADA ENTERA. El tramo se toma por la VARA VIGENTE, que es")
        print("  la LECTURA A (03_FUSIONES.md, cabecera del registro del tramo 1, vuelta 48:")
        print("  la nomina RE-MEDIDA AL ABRIRLO). La lectura B queda como contraste, con su")
        print("  desfase medido y nombrado, y NO se elige entre las dos a ojo.")
        divergencia = {"solo_en_A": [list(c) for c in sorted(sa)],
                       "solo_en_B": [list(c) for c in sorted(sb)]}
    print()

    # ------------------------------------------------------------------
    # EL TRAMO ES LA LECTURA A, Y DE AQUI EN ADELANTE TODO SE MIDE SOBRE ELLA.
    # EL ORDINAL SE DERIVA DEL FICHERO CONTANDO EL ORDEN IMPRESO DE HOY, que es
    # exactamente lo que hacia el ABRIDOR del tramo 2 (vuelta54_tramo2_nomina.py,
    # "for n, (i, r) in enumerate(tramo2, 1)"). El sucesor de la vuelta 55 lo
    # derivaba del puesto de la 48 porque aquel tramo YA ESTABA ABIERTO y sus
    # ordinales ya estaban publicados; aqui el tramo se ABRE, asi que la
    # aritmetica que toca copiar es la del abridor y no la del sucesor.
    # El puesto de la 48 se imprime AL LADO, en su columna, y dice "nuevo"
    # cuando el acto no existia como CERRADO aquel dia.
    # ------------------------------------------------------------------
    idx48 = {}
    for i, r in enumerate(v48, 1):
        for m in r["miembros"]:
            idx48.setdefault(m, i)
    tramo = []
    for n, (i, r) in enumerate(lectA, 1):
        ps = sorted({idx48[m] for m in r["miembros"] if m in idx48})
        tramo.append({"orden": n, "puesto_hoy": i, "puesto_v48": ps[0] if ps else None,
                      "acto": r})

    print("--- GUARDA DE LOS CUATRO AJENOS (03_FUSIONES.md, 11 ago 2026) ---")
    print("   CAMINO 1, EL LITERAL, que es el que corrian los abridores de los tramos 1 y 2:")
    sucio = []
    for x in AJENOS:
        dentro = [f["orden"] for f in tramo if x in f["acto"]["miembros"]]
        enlote = [i for i, r in enumerate(hoy, 1) if x in r["miembros"]]
        if dentro:
            sucio.append(x)
        print("     %-38s en el TRAMO %d: %-22s en el lote CERRADO entero: %s"
              % (x, TRAMO, "SI, actos %s" % dentro if dentro else "NO",
                 enlote if enlote else "NO"))
    print("   CAMINO 1: %s" % ("ROJO" if sucio else "VERDE, ninguno de los cuatro entra"))
    print()
    print("   CAMINO 2, POR EL RESOLUTOR (regla 9 del EJECUTOR, P.1): un ajeno deprecado")
    print("   vive hoy dentro del ids_alias de su superviviente, y el camino literal no lo ve.")
    bajo_alias = []
    for x in AJENOS:
        p = os.path.join(NODOS, x + ".json")
        d = json.load(io.open(p, encoding="utf-8")) if os.path.exists(p) else None
        dep = (d or {}).get("deprecado") if d else "SIN FICHERO"
        r = resolver(x)
        dentro = [f["orden"] for f in tramo if r in f["acto"]["miembros"]]
        if dentro and r != x:
            bajo_alias.append((x, r, dentro))
        print("     %-38s deprecado: %-6s resuelve a %-32s en el TRAMO %d: %s"
              % (x, dep, r, TRAMO, "SI, actos %s" % dentro if dentro else "NO"))
    if bajo_alias:
        print("   CAMINO 2: MUERDE DONDE EL LITERAL PASABA POR VACIO:")
        for x, r, dentro in bajo_alias:
            print("     el ajeno %s esta hoy dentro de %s, que es miembro del acto %s"
                  % (x, r, dentro))
        print("   ESTE INSTRUMENTO MIDE Y NO DECIDE si eso bloquea: la decision va escrita")
        print("   con su vara en el registro y marcada como discutible en el reporte.")
    else:
        print("   CAMINO 2: VERDE, ningun ajeno entra tampoco bajo el resolutor.")
    print()

    print("--- GUARDA DE SOLAPE CON LOS TRAMOS 1 Y 2 ---")
    solapan = []
    for f in tramo:
        for t in (1, 2):
            com = sorted(set(f["acto"]["miembros"]) & previos[t]["miembros"])
            if com:
                solapan.append((f["orden"], t, com))
    print("   actos del tramo %d que tocan un miembro de un tramo anterior: %d"
          % (TRAMO, len(solapan)))
    for o, t, com in solapan:
        print("     acto %d toca el tramo %d en %s" % (o, t, com))
    print("   GUARDA: %s" % ("ROJO" if solapan else "VERDE, ningun solape"))
    print()

    print("--- EL TRAMO %d, EN EL ORDEN IMPRESO ---" % TRAMO)
    print()
    print("  %-4s %-5s %-6s %-7s %-20s %s"
          % ("acto", "hoy", "en 48", "tamano", "clases internas", "miembros"))
    tam = {}
    figuras = {"PURO A": 0, "MIXTO": 0}
    no_puros = []
    salida = []
    for f in tramo:
        r = f["acto"]
        cl = r["clases_internas"]
        puro = set(cl) == {"A"}
        fusion_pura = puro and r["tamano"] == 2
        figuras["PURO A" if puro else "MIXTO"] += 1
        tam[r["tamano"]] = tam.get(r["tamano"], 0) + 1
        if not fusion_pura:
            no_puros.append((f["orden"], r["tamano"], cl))
        print("  %-4d %-5d %-6s %-7d %-20s %s"
              % (f["orden"], f["puesto_hoy"],
                 f["puesto_v48"] if f["puesto_v48"] else "nuevo",
                 r["tamano"], cl, ", ".join(sorted(r["miembros"]))))
        fila = dict(r)
        fila["orden_tramo3"] = f["orden"]
        fila["puesto_hoy"] = f["puesto_hoy"]
        fila["puesto_v48"] = f["puesto_v48"]
        fila["figura"] = "PURO A" if puro else "MIXTO"
        fila["fusion_pura"] = fusion_pura
        fila["nacido_despues_de_la_48"] = f["puesto_v48"] is None
        fila["ajenos_bajo_resolutor"] = sorted(
            x for x, rr, dentro in bajo_alias if f["orden"] in dentro)
        salida.append(fila)
    print()
    print("  actos del tramo %d      : %d" % (TRAMO, len(tramo)))
    print("  por tamano             : %s" % dict(sorted(tam.items())))
    print("  por figura             : %s" % figuras)
    print("  nodos implicados       : %d" % sum(r["tamano"] for r in salida))
    print("  nodos que MORIRIAN si se funden todos: %d"
          % sum(r["tamano"] - 1 for r in salida))
    print()

    print("--- LOS QUE NO SON DE FUSION PURA (tamano 2 y PURO A), NOMBRADOS ---")
    if not no_puros:
        print("   NINGUNO: los %d son de fusion pura, tamano 2 y PURO A." % len(tramo))
    else:
        for o, t, cl in no_puros:
            print("   acto %-3d tamano %d clases %s  -> TOMA SU CARRIL, no se fuerza" % (o, t, cl))
        print("   son %d de %d." % (len(no_puros), len(tramo)))
    print()

    if a.salida:
        with io.open(a.salida, "w", encoding="utf-8", newline=chr(10)) as f:
            for fila in salida:
                f.write(json.dumps(fila, ensure_ascii=False) + chr(10))
        print("  escrito: %s" % a.salida)
        print()

    print("FIN")
    return 0 if not sucio and not solapan else 1


if __name__ == "__main__":
    raise SystemExit(main())
