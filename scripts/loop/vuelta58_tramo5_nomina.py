# -*- coding: utf-8 -*-
"""vuelta58_tramo5_nomina.py . EL ABRIDOR DEL TRAMO 5 DE OP-U-01, DETERMINADO
POR MEDICION Y POR DOS CAMINOS.

SUCESOR DECLARADO de scripts/loop/vuelta57_tramo4_nomina.py, al que NO
reemplaza. El fichero se copio BYTE A BYTE y solo despues se le cambio lo que se
declara abajo. La aritmetica se copia entera: identidad POR MIEMBROS del sucesor de
la vuelta 55, ORDINAL contado sobre el orden impreso de HOY del abridor de la
vuelta 54, guarda del prefijo, guarda de los cuatro ajenos por los DOS caminos,
guarda de solape, y el diagnostico de divergencia con sus DOS FORMAS EXPLICADAS.

DE SOLO LECTURA. No toca ni un nodo, ni un veredicto, ni una operacion: imprime,
y solo escribe el fichero que se le nombre en --salida.

LO UNICO QUE NO ES COPIA EN ESTA VUELTA, y es poco a proposito: EL TRAMO 4 ENTRA
EN LA LISTA DE TRAMOS PREVIOS, con su fichero fijado docs/loop/TRAMO4_V57.jsonl,
igual que el 2 y el 3; el ordinal pasa a orden_tramo5; y los rotulos de prosa que
nombraban tres tramos nombran cuatro. La maquina de las dos lecturas, el
diagnostico de divergencias, la guarda del prefijo, la de los ajenos por los dos
caminos y la de solape se copian ENTERAS y no se tocan.

  Y EL PREFIJO DE ESTA VUELTA NO SE HEREDA: la vuelta 58 DESHIZO el acto 32 del
  tramo 4 (TAREA 1.1), asi que los vivos del tramo 4 pasaron de SEIS a SIETE. El
  instrumento no lleva ese numero escrito en ninguna parte: lo MIDE de la nomina
  del dia, y si el prefijo tuviera huecos caeria en ROJO.

LO QUE LA VUELTA 57 YA HABIA CAMBIADO, y se conserva entero:

  LA LECTURA B YA NO PUEDE SER UN BLOQUE FIJO DE LA NOMINA DE LA 48, y el motivo
  esta MEDIDO y no supuesto. Hasta el tramo 3, la lectura B era "los que ocupaban
  los puestos 101 a 150 de la nomina de la vuelta 48". Para el tramo 4 esa
  formula ya no vale, porque EL TRAMO 3 REALMENTE ABIERTO NO ES EL BLOQUE 101 A
  150: la vuelta 56 midio que un CERRADO NACIDO DESPUES se colo en el corte y
  que el acto del puesto 150 de la 48 (`crecimiento_ingresos_verdes` mas
  `generacion_ingresos_verdes`) quedo DESPLAZADO al tramo siguiente, que es
  este. Tomar el bloque 151 a 200 dejaria ese acto fuera de las DOS lecturas y
  la comprobacion se volveria ciega justo donde la vuelta anterior encontro
  algo.

  LA LECTURA B DEL TRAMO 4 ES, ENTONCES: los CERRADOS de la nomina de la 48, EN
  SU ORDEN, saltando los que pertenecen a los tramos 1, 2 o 3 TAL COMO QUEDARON
  FIJADOS, y tomando los cincuenta siguientes. Es la misma idea de siempre (el
  orden del dia en que los tramos se definieron) escrita de forma que sobreviva
  a que un tramo no sea un bloque contiguo.

  Y LOS TRAMOS PREVIOS SE IDENTIFICAN POR SU FICHERO FIJADO, no por un bloque:
  el tramo 1 no tiene fichero propio y se toma del bloque 1 a 50 de la 48; el
  tramo 2 de `docs/loop/TRAMO2_V54.jsonl` y el tramo 3 de
  `docs/loop/TRAMO3_V56.jsonl`, que son las nominas con las que se abrieron. El
  instrumento COMPRUEBA ademas que el fichero del tramo 2 calza con el bloque 51
  a 100 de la 48, porque aquella apertura si calzaba, y si dejara de calzar seria
  una divergencia nueva y no un detalle.

LAS DOS LECTURAS Y LA VARA, sin cambio:

  LECTURA A, la VARA VIGENTE (03_FUSIONES.md, cabecera del registro del tramo 1,
  vuelta 48): los CINCUENTA primeros actos CERRADOS de la NOMINA RE-MEDIDA AL
  ABRIRLO, tras el prefijo de los vivos de los tramos anteriores.

  LECTURA B, el contraste. Si las dos calzan, el tramo esta determinado. Si no,
  este instrumento NO elige a ojo: DIAGNOSTICA, y solo continua si toda
  divergencia cae en una de las dos formas explicadas (un CERRADO nacido despues
  en el lado A; un acto que hoy cae DETRAS del corte en el lado B). Cualquier
  otra es ROJO y PARADA.

MODO DE CONTINUACION (--fijado), copiado del de la vuelta 56 con el mismo motivo
escrito: cuando el tramo ya esta fijado en su fichero no se vuelve a abrir, se
re-mide sobre esa nomina, porque en cuanto se funde un acto del tramo la lectura
encoge y la otra rellena con actos del tramo siguiente.

Uso:
  python scripts/loop/vuelta58_tramo5_nomina.py --nomina <RECOMPUTO del dia> \
        [--salida docs/loop/TRAMO5_V58.jsonl]
  python scripts/loop/vuelta58_tramo5_nomina.py --nomina <...> \
        --fijado docs/loop/TRAMO5_V58.jsonl
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
V48 = os.path.join(LOOP, "RECOMPUTO_V48_COMPONENTES.jsonl")
FIJADO_T2 = os.path.join(LOOP, "TRAMO2_V54.jsonl")
FIJADO_T3 = os.path.join(LOOP, "TRAMO3_V56.jsonl")
FIJADO_T4 = os.path.join(LOOP, "TRAMO4_V57.jsonl")
NODOS = os.path.join(RAIZ, "dataset", "nodos")

# 03_FUSIONES.md declara desde el 11 ago 2026 que estos cuatro no se resuelven
# nunca en OP-U-01. Misma lista, palabra por palabra, que la de los abridores de
# los tramos 1, 2 y 3.
AJENOS = ["gates_go_kill_decision_points", "customer_discovery",
          "ab_testing_optimizacion", "brainstorming_divergente"]

TAM_TRAMO = 50
TRAMO = 5


def cargar(p):
    return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]


def leer_nodo(nid):
    p = os.path.join(NODOS, nid + ".json")
    if not os.path.exists(p):
        return None
    return json.load(io.open(p, encoding="utf-8"))


def mapa_alias():
    """EL RESOLUTOR DE P.1, con la aritmetica COPIADA de la del instrumento que
    publica el censo (scripts/loop/vuelta51_censo_colisiones.py): el nodo
    deprecado NO lleva campo de reenvio; es el nodo VIVO el que iza los ids del
    muerto en su campo ids_alias. Se recorre el catalogo vivo y se invierte."""
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


def medir_fijado(a, hoy, resolver):
    """MODO CONTINUACION. Aritmetica copiada del sucesor de la vuelta 55 por la
    via del abridor de la 56: identidad POR MIEMBROS, y el que no aparece hoy
    tiene que estar FUNDIDO LIMPIO contra el grafo."""
    fijado = cargar(a.fijado)
    print("=" * 78)
    print("EL TRAMO %d DE OP-U-01, RE-MEDIDO SOBRE SU NOMINA FIJADA" % TRAMO)
    print("aritmetica copiada del sucesor de la vuelta 55; identidad POR MIEMBROS")
    print("=" * 78)
    print()
    print("  nomina de hoy   : %s (%d actos CERRADOS)" % (a.nomina, len(hoy)))
    print("  tramo fijado en : %s (%d actos)" % (a.fijado, len(fijado)))
    print()

    vivos, fundidos, rojo = [], [], []
    for r in fijado:
        n = r["orden_tramo%d" % TRAMO]
        mi = set(r["miembros"])
        aqui = [(i, x) for i, x in enumerate(hoy, 1) if set(x["miembros"]) & mi]
        if aqui:
            vivos.append((n, aqui[0][0], sorted(mi)))
            continue
        res = sorted({resolver(m) for m in sorted(mi)})
        muertos = [m for m in sorted(mi) if (leer_nodo(m) or {}).get("deprecado") is True]
        vivo = [m for m in sorted(mi) if m not in muertos]
        izado = False
        if len(vivo) == 1:
            izado = all(m in ((leer_nodo(vivo[0]) or {}).get("ids_alias") or [])
                        for m in muertos)
        ok = (len(res) == 1 and len(muertos) == len(mi) - 1 and len(vivo) == 1 and izado)
        fundidos.append((n, vivo[0] if vivo else None, muertos, len(res) == 1, izado))
        if not ok:
            rojo.append((n, "no esta fundido limpio: resuelven a %s, muertos %s"
                         % (res, muertos)))

    print("  VIVOS hoy   : %d" % len(vivos))
    print("  FUNDIDOS    : %d" % len(fundidos))
    print("  suma        : %d de %d" % (len(vivos) + len(fundidos), len(fijado)))
    print()
    print("--- LOS FUNDIDOS, COMPROBADOS CONTRA EL GRAFO UNO A UNO ---")
    for n, sup, abso, uno, izado in fundidos:
        print("  acto %-3d superviviente %-46s absorbido %-46s resuelven a UNO: %-3s alias izado: %s"
              % (n, sup, ", ".join(abso), "SI" if uno else "NO", "SI" if izado else "NO"))
    print("  COMPROBACION: %s" % ("ROJO" if rojo else
                                  "VERDE, los %d estan fundidos limpios" % len(fundidos)))
    print()
    print("--- LOS QUE SIGUEN VIVOS, CON SU PUESTO DE HOY ---")
    for n, puesto, mi in vivos:
        print("  acto %-3d puesto de hoy %-4d  %s" % (n, puesto, ", ".join(mi)))
    print()
    if rojo:
        for n, m in rojo:
            print("     acto %d: %s" % (n, m))
        print("  ROJO DE VERDAD. PARADA.")
        return 1
    print("FIN")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vuelta", type=int, default=None,
                    help="la vuelta que abre el tramo; va en el titulo. Sin ella el "
                         "titulo no la nombra, en vez de heredar una vieja.")
    ap.add_argument("--nomina", required=True)
    ap.add_argument("--salida", default=None)
    ap.add_argument("--fijado", default=None,
                    help="jsonl del tramo YA FIJADO: mide su estado de hoy en vez de re-abrirlo")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    hoy = [r for r in cargar(a.nomina) if r["estado"] == "CERRADO"]
    v48_todo = cargar(V48)
    v48 = [r for r in v48_todo if r["estado"] == "CERRADO"]
    alias = mapa_alias()
    resolver = lambda x: alias.get(x, x)

    if a.fijado:
        return medir_fijado(a, hoy, resolver)

    print("=" * 78)
    # LA VUELTA SALE DEL ARGUMENTO Y NO DE UNA CONSTANTE, por la misma vara de la
    # TAREA 1.3 de esta vuelta: el ancestro llevaba "(vuelta 57)" tallado a mano en
    # este print, que es la especie del titulo envejecido del cuadro de varas. Sin
    # --vuelta el titulo no la nombra, en vez de heredar una vieja.
    print("EL ABRIDOR DEL TRAMO %d DE OP-U-01%s"
          % (TRAMO, "" if a.vuelta is None else " (vuelta %d)" % a.vuelta))
    print("sucesor declarado del abridor del tramo %d: la LECTURA B no es un bloque"
          % (TRAMO - 1))
    print("fijo de la 48, sino la nomina de la 48 saltando los tramos FIJADOS")
    print("=" * 78)
    print()
    print("  nomina de hoy   : %s (%d actos CERRADOS)" % (a.nomina, len(hoy)))
    print("  nomina de la 48 : %s (%d actos CERRADOS)"
          % (os.path.relpath(V48, RAIZ), len(v48)))
    print()

    # ---- los tramos ya abiertos, POR SU FICHERO FIJADO ----
    print("--- LOS TRAMOS YA ABIERTOS, IDENTIFICADOS POR SUS MIEMBROS ---")
    previos = {}
    fuentes = {
        1: ("el bloque 1 a 50 de la nomina de la 48 (no tiene fichero propio)",
            [r["miembros"] for r in v48[:TAM_TRAMO]]),
        2: (os.path.relpath(FIJADO_T2, RAIZ),
            [r["miembros"] for r in cargar(FIJADO_T2)]),
        3: (os.path.relpath(FIJADO_T3, RAIZ),
            [r["miembros"] for r in cargar(FIJADO_T3)]),
        4: (os.path.relpath(FIJADO_T4, RAIZ),
            [r["miembros"] for r in cargar(FIJADO_T4)]),
    }
    for t in (1, 2, 3, 4):
        fuente, listas = fuentes[t]
        mi = set()
        for ms in listas:
            mi |= set(ms)
        vivos = [i for i, r in enumerate(hoy, 1) if set(r["miembros"]) & mi]
        previos[t] = {"miembros": mi, "vivos": vivos, "actos": listas}
        print("  tramo %d: %d actos, %d miembros, %d vivos hoy en los puestos %s"
              % (t, len(listas), len(mi), len(vivos), vivos))
        print("           fuente: %s" % fuente)
    print()

    # ---- COMPROBACION: el fichero del tramo 2 calza con el bloque 51 a 100 ----
    print("--- EL TRAMO 2 CONTRA SU BLOQUE DE LA 48 (aquella apertura SI calzaba) ---")
    bloque2 = [tuple(sorted(r["miembros"])) for r in v48[TAM_TRAMO:2 * TAM_TRAMO]]
    fich2 = [tuple(sorted(ms)) for ms in previos[2]["actos"]]
    calza2 = bloque2 == fich2
    print("   bloque 51 a 100 de la 48: %d actos | fichero fijado: %d actos"
          % (len(bloque2), len(fich2)))
    print("   calzan en conjunto y en orden: %s" % ("SI" if calza2 else "NO"))
    if not calza2:
        print("   ROJO: el tramo 2 dejo de calzar con su bloque. Es divergencia nueva. PARADA.")
        return 1
    print()

    # ---- EL TRAMO 3 CONTRA SU BLOQUE, que ya se sabe que NO calza ----
    print("--- EL TRAMO 3 CONTRA SU BLOQUE DE LA 48 (la vuelta 56 midio que NO calza) ---")
    bloque3 = [tuple(sorted(r["miembros"])) for r in v48[2 * TAM_TRAMO:3 * TAM_TRAMO]]
    fich3 = [tuple(sorted(ms)) for ms in previos[3]["actos"]]
    solo_f = [c for c in fich3 if c not in bloque3]
    solo_b = [c for c in bloque3 if c not in fich3]
    print("   en el fichero y no en el bloque: %d  %s"
          % (len(solo_f), [", ".join(c) for c in solo_f]))
    print("   en el bloque y no en el fichero: %d  %s"
          % (len(solo_b), [", ".join(c) for c in solo_b]))
    print("   ES LO QUE LA VUELTA 56 DEJO ESCRITO, y por eso la LECTURA B de este tramo")
    print("   se arma saltando los tramos FIJADOS en vez de tomar un bloque contiguo.")
    print()

    mi_previos = (previos[1]["miembros"] | previos[2]["miembros"]
                  | previos[3]["miembros"] | previos[4]["miembros"])
    prefijo = sorted(set(previos[1]["vivos"]) | set(previos[2]["vivos"])
                     | set(previos[3]["vivos"]) | set(previos[4]["vivos"]))

    # ---- GUARDA DEL PREFIJO: los vivos ocupan los puestos 1..N, sin huecos ----
    print("--- GUARDA DEL PREFIJO (el numero se MIDE, no se teclea ni se hereda) ---")
    print("  actos vivos de los tramos 1, 2, 3 y 4: %d" % len(prefijo))
    print("  puestos que ocupan hoy             : %s" % prefijo)
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
    resto = [(i, r) for i, r in enumerate(hoy, 1)
             if not (set(r["miembros"]) & mi_previos)]
    lectA = resto[:TAM_TRAMO]
    print("--- LECTURA A: los %d CERRADOS siguientes en el orden impreso de HOY ---"
          % TAM_TRAMO)
    print("  actos CERRADOS fuera de los tramos 1, 2, 3 y 4: %d" % len(resto))
    if len(lectA) < TAM_TRAMO:
        print()
        print("  ROJO: no hay %d actos para el tramo. PARADA." % TAM_TRAMO)
        return 1
    print("  puestos de hoy del tramo %d: del %d al %d"
          % (TRAMO, lectA[0][0], lectA[-1][0]))
    print()

    # ---- LECTURA B: la nomina de la 48 saltando los tramos FIJADOS ----
    print("--- LECTURA B: la nomina de la 48, EN SU ORDEN, saltando los tramos fijados ---")
    restoB = [(i, r) for i, r in enumerate(v48, 1)
              if not (set(r["miembros"]) & mi_previos)]
    lectB = restoB[:TAM_TRAMO]
    print("  CERRADOS de la 48 fuera de los tramos 1, 2, 3 y 4: %d" % len(restoB))
    if len(lectB) < TAM_TRAMO:
        print("  AVISO: la 48 solo aporta %d actos a esta lectura." % len(lectB))
    else:
        print("  puestos de la 48 del tramo %d: del %d al %d (no tienen por que ser contiguos)"
              % (TRAMO, lectB[0][0], lectB[-1][0]))
    print()

    # ---- el estado de HOY de cada acto de la lectura B ----
    filas, rojo = [], []
    for n, (p48, r48) in enumerate(lectB, 1):
        mi = set(r48["miembros"])
        aqui = [(i, r) for i, r in enumerate(hoy, 1) if set(r["miembros"]) & mi]
        if len(aqui) > 1:
            rojo.append((n, "el acto se parte hoy en %d componentes" % len(aqui)))
        if aqui:
            i, r = aqui[0]
            filas.append({"orden": n, "estado_hoy": "VIVO", "puesto_hoy": i,
                          "puesto_v48": p48, "acto": r})
        else:
            res = sorted({resolver(m) for m in r48["miembros"]})
            muertos = [m for m in sorted(mi)
                       if (leer_nodo(m) or {}).get("deprecado") is True]
            vivo = [m for m in sorted(mi) if m not in muertos]
            ok = (len(res) == 1 and len(muertos) == len(mi) - 1 and len(vivo) == 1)
            izado = False
            if len(vivo) == 1:
                al = (leer_nodo(vivo[0]) or {}).get("ids_alias") or []
                izado = all(m in al for m in muertos)
            filas.append({"orden": n, "estado_hoy": "FUNDIDO", "puesto_hoy": None,
                          "puesto_v48": p48, "acto": None, "miembros": sorted(mi),
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
    print("  suma        : %d de %d" % (len(vivos) + len(fundidos), len(lectB)))
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
    porV48 = [clave(f["acto"]["miembros"])
              for f in sorted(vivos, key=lambda f: f["orden"])]
    porHOY = [clave(r["miembros"]) for _, r in lectA]
    iguales = porV48 == porHOY
    print("  LECTURA A (orden de HOY) y LECTURA B (orden de la 48): %s"
          % ("CALZAN, mismo conjunto y mismo orden" if iguales
             else "NO CALZAN"))
    divergencia = None
    if not iguales:
        sa, sb = set(porHOY) - set(porV48), set(porV48) - set(porHOY)
        print("  solo en A: %d | solo en B: %d" % (len(sa), len(sb)))
        if not sa and not sb:
            print("  MISMO CONJUNTO, DISTINTO ORDEN: eso no es una de las dos formas")
            print("  explicadas. ROJO. PARADA.")
            return 1
        print()
        print("  --- LA DIVERGENCIA, DIAGNOSTICADA CON EL FICHERO DELANTE ---")
        estado48 = {}
        for i, r in enumerate(v48_todo, 1):
            for m in r["miembros"]:
                estado48.setdefault(m, (i, r["estado"], r["tamano"],
                                        sorted(r["miembros"])))
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
                print("       NO EXPLICADO: ya era CERRADO en la 48, en los puestos %s."
                      % puestos_c)
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
    # EL TRAMO ES LA LECTURA A. EL ORDINAL SE CUENTA SOBRE EL ORDEN IMPRESO DE
    # HOY, que es lo que hacia el ABRIDOR del tramo 2 (vuelta54_tramo2_nomina.py)
    # y lo que copio el del tramo 3: el tramo se ABRE hoy y no tiene ordinal
    # publicado que respetar. El puesto de la 48 se imprime AL LADO y dice
    # "nuevo" cuando el acto no existia como CERRADO aquel dia.
    # ------------------------------------------------------------------
    idx48 = {}
    for i, r in enumerate(v48, 1):
        for m in r["miembros"]:
            idx48.setdefault(m, i)
    tramo = []
    for n, (i, r) in enumerate(lectA, 1):
        ps = sorted({idx48[m] for m in r["miembros"] if m in idx48})
        tramo.append({"orden": n, "puesto_hoy": i,
                      "puesto_v48": ps[0] if ps else None, "acto": r})

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

    print("--- GUARDA DE SOLAPE CON LOS TRAMOS 1, 2 Y 3 ---")
    solapan = []
    for f in tramo:
        for t in (1, 2, 3):
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
        fila["orden_tramo5"] = f["orden"]
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
    if divergencia:
        print("  divergencia declarada  : %s" % json.dumps(divergencia, ensure_ascii=False))
    print()

    print("--- LOS QUE NO SON DE FUSION PURA (tamano 2 y PURO A), NOMBRADOS ---")
    if not no_puros:
        print("   NINGUNO: los %d son de fusion pura, tamano 2 y PURO A." % len(tramo))
    else:
        for o, t, cl in no_puros:
            print("   acto %-3d tamano %d clases %s  -> TOMA SU CARRIL, no se fuerza"
                  % (o, t, cl))
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
