# -*- coding: utf-8 -*-
"""vuelta55_tramo2_nomina.py . EL TRAMO 2 DE OP-U-01 RE-IDENTIFICADO POR SUS
MIEMBROS CUANDO EL TRAMO YA ESTA ABIERTO Y PARCIALMENTE CONSUMIDO.

SUCESOR DECLARADO de scripts/loop/vuelta54_tramo2_nomina.py. LA LOGICA DE
AQUEL NO SE TOCA y su aritmetica se copia entera aqui. El motivo esta escrito
con todas sus letras porque es un hallazgo de esta vuelta, no una comodidad:

  AQUEL INSTRUMENTO NACIO PARA ABRIR UN TRAMO, NO PARA CONTINUARLO. Compara
  la LECTURA A (los 50 actos CERRADOS siguientes en el orden impreso de HOY)
  contra la LECTURA B (los que ocupaban los puestos 51 a 100 de la nomina de
  la vuelta 48) y cae en ROJO si no dan el mismo conjunto en el mismo orden.
  El dia que se abrio el tramo las dos calzaban al acto y al orden, y el acta
  de la vuelta 54 lo verifico por dos caminos. PERO EN CUANTO SE FUNDE UN
  ACTO DEL TRAMO, EL ROJO ES INEVITABLE Y NO SIGNIFICA LO QUE DICE: el acto
  fundido deja de ser una componente CERRADA de dos miembros (sus dos ids
  resuelven ya al mismo nodo vivo), asi que sale de la nomina, la LECTURA B
  encoge, y la LECTURA A rellena hasta 50 con actos del tramo SIGUIENTE. El
  rojo no dice "el tramo no esta determinado": dice "el tramo ya se toco".

  LA VARA DE ESTE SUCESOR ES LA DEL ACTA 54, PREGUNTA 3, tal como esta
  escrita: un instrumento de guarda cuyas cifras YA ESTAN CITADAS por
  registros (el registro del tramo 2 en docs/plan/03_FUSIONES.md publica su
  tabla de las dos lecturas) NO se repara: se le escribe un sucesor declarado
  con la aritmetica copiada. Aquel sigue en el repo, intacto, y su rojo de
  hoy queda registrado como lo que es.

LA IDENTIDAD DEL TRAMO 2, MEDIDA Y NO DECIDIDA. La doctrina de la pagina es
identificar los actos POR SUS MIEMBROS y no por su numero, y por eso aqui el
tramo 2 es, por definicion, LOS CINCUENTA ACTOS QUE OCUPABAN LOS PUESTOS 51 A
100 DE LA NOMINA DE LA VUELTA 48 (docs/loop/RECOMPUTO_V48_COMPONENTES.jsonl),
identificados por los miembros que nombraban. Cada uno de esos cincuenta esta
hoy en uno de dos estados, y el instrumento lo MIDE contra el grafo:

  VIVO   : hay una componente CERRADA de hoy que toca alguno de sus miembros.
  FUNDIDO: no la hay, y entonces se comprueba contra el grafo que sus dos
           miembros resuelven al mismo nodo vivo, que uno de los dos esta
           deprecado y que el superviviente lleva el alias izado. Si esa
           comprobacion falla, es ROJO de verdad y PARA.

EL ORDINAL DEL ACTO (1 a 50) ES EL PUESTO DE LA VUELTA 48 MENOS 50, que es la
misma cuenta con la que la vuelta 54 lo imprimio y con la que el encargo de la
vuelta 55 nombra los actos. No se teclea: se deriva del fichero.

EL CALZAR QUE ESTE SUCESOR SI EXIGE (y que es el que aquel hacia, adaptado al
tramo consumido): LOS SUPERVIVIENTES, EN EL ORDEN IMPRESO DE HOY, TIENEN QUE
SER LOS MISMOS Y EN EL MISMO ORDEN que los supervivientes ordenados por su
puesto de la vuelta 48. Si eso no calza, el tramo si estaria indeterminado y
para. Y ADEMAS: los supervivientes tienen que ser un PREFIJO de la LECTURA A
de hoy, o sea que ningun acto ajeno al tramo se cuela por delante.

LAS DOS GUARDAS DE SIEMPRE, copiadas: la de los cuatro ajenos y la de solape
con el tramo 1.

DE SOLO LECTURA. No toca ni un nodo, ni un veredicto, ni una operacion: solo
escribe el fichero que se le nombre en --salida.

Uso:
  python scripts/loop/vuelta55_tramo2_nomina.py --nomina <RECOMPUTO del dia> \
        [--salida docs/loop/TRAMO2_V55.jsonl]
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
# nunca en OP-U-01. Misma lista, palabra por palabra, que la del ancestro.
AJENOS = ["gates_go_kill_decision_points", "customer_discovery",
          "ab_testing_optimizacion", "brainstorming_divergente"]

TAM_TRAMO = 50


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
    print("EL TRAMO 2 DE OP-U-01, RE-IDENTIFICADO POR SUS MIEMBROS (vuelta 55)")
    print("SUCESOR DECLARADO de vuelta54_tramo2_nomina.py, aritmetica copiada")
    print("=" * 78)
    print()
    print("  nomina de hoy   : %s (%d actos CERRADOS)" % (a.nomina, len(hoy)))
    print("  nomina de la 48 : %s (%d actos CERRADOS)" % (os.path.relpath(V48, RAIZ), len(v48)))
    print()

    # ---- el tramo 1, por sus miembros (aritmetica copiada del ancestro) ----
    tramo1 = v48[:TAM_TRAMO]
    mi1 = set()
    for r in tramo1:
        mi1 |= set(r["miembros"])
    print("--- EL TRAMO 1, IDENTIFICADO POR SUS MIEMBROS Y NO POR SU NUMERO ---")
    print("  actos del tramo 1 en la nomina de la 48: %d" % len(tramo1))
    print("  miembros que esos 50 actos nombraban   : %d" % len(mi1))
    vivos1 = [(i, r) for i, r in enumerate(hoy, 1) if set(r["miembros"]) & mi1]
    print("  actos de HOY que tocan a alguno        : %d, en los puestos %s"
          % (len(vivos1), [i for i, _ in vivos1]))
    print()

    # ---- el tramo 2, por sus miembros, con su ordinal derivado ----
    tramo2_48 = v48[TAM_TRAMO:2 * TAM_TRAMO]
    print("--- EL TRAMO 2, POR LOS MIEMBROS DE LOS PUESTOS 51 A 100 DE LA 48 ---")
    print("  actos que definen el tramo 2: %d" % len(tramo2_48))
    print()

    # LECTURA A de hoy: los CERRADOS de hoy que no tocan al tramo 1.
    lectA = [(i, r) for i, r in enumerate(hoy, 1) if not (set(r["miembros"]) & mi1)]

    filas = []
    rojo_fusion = []
    for n, r48 in enumerate(tramo2_48, 1):
        mi = set(r48["miembros"])
        aqui = [(i, r) for i, r in enumerate(hoy, 1) if set(r["miembros"]) & mi]
        if len(aqui) > 1:
            rojo_fusion.append((n, "el acto se parte hoy en %d componentes" % len(aqui)))
        if aqui:
            i, r = aqui[0]
            filas.append({"orden": n, "estado_hoy": "VIVO", "puesto_hoy": i,
                          "puesto_v48": TAM_TRAMO + n, "acto": r})
        else:
            # tiene que estar FUNDIDO, y se comprueba contra el grafo.
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
                          "puesto_v48": TAM_TRAMO + n, "acto": None,
                          "miembros": sorted(mi),
                          "superviviente": vivo[0] if len(vivo) == 1 else None,
                          "absorbidos": muertos, "resuelven_a": res,
                          "alias_izado": izado})
            if not ok:
                rojo_fusion.append((n, "no esta fundido limpio: resuelven a %s, muertos %s"
                                    % (res, muertos)))

    vivos = [f for f in filas if f["estado_hoy"] == "VIVO"]
    fundidos = [f for f in filas if f["estado_hoy"] == "FUNDIDO"]
    print("  VIVOS hoy   : %d" % len(vivos))
    print("  FUNDIDOS    : %d" % len(fundidos))
    print("  suma        : %d de %d" % (len(vivos) + len(fundidos), len(tramo2_48)))
    print()

    print("--- LOS FUNDIDOS, COMPROBADOS CONTRA EL GRAFO UNO A UNO ---")
    for f in fundidos:
        print("  acto %-3d superviviente %-46s absorbido %-46s resuelven a UNO: %-3s alias izado: %s"
              % (f["orden"], f["superviviente"], ", ".join(f["absorbidos"]),
                 "SI" if len(f["resuelven_a"]) == 1 else "NO",
                 "SI" if f["alias_izado"] else "NO"))
    print("  COMPROBACION: %s" % ("ROJO" if rojo_fusion else
                                  "VERDE, los %d estan fundidos limpios" % len(fundidos)))
    if rojo_fusion:
        for n, m in rojo_fusion:
            print("     acto %d: %s" % (n, m))
        print()
        print("  ROJO DE VERDAD. PARADA.")
        return 1
    print()

    # ---- EL CALZAR DE LA CONTINUACION ----
    print("--- EL CALZAR DE LA CONTINUACION (las dos lecturas, adaptadas) ---")
    clave = lambda ms: tuple(sorted(ms))
    porV48 = [clave(f["acto"]["miembros"]) for f in sorted(vivos, key=lambda f: f["puesto_v48"])]
    porHOY = [clave(f["acto"]["miembros"]) for f in sorted(vivos, key=lambda f: f["puesto_hoy"])]
    calza_orden = porV48 == porHOY
    print("  A, orden impreso de HOY, contra B, orden de la vuelta 48: %s"
          % ("CALZAN, mismo conjunto y mismo orden" if calza_orden else "NO CALZAN"))
    prefijo = [clave(r["miembros"]) for _, r in lectA[:len(vivos)]]
    calza_prefijo = prefijo == porHOY
    print("  los %d supervivientes son el PREFIJO de la LECTURA A de hoy: %s"
          % (len(vivos), "SI" if calza_prefijo else "NO"))
    if not (calza_orden and calza_prefijo):
        print()
        print("  ROJO: el tramo NO esta determinado por el texto. PARADA.")
        return 1
    print()

    print("--- GUARDA DE LOS CUATRO AJENOS (03_FUSIONES.md, 11 ago 2026) ---")
    sucio = []
    for x in AJENOS:
        dentro = [f["orden"] for f in vivos if x in f["acto"]["miembros"]]
        enlote = [i for i, r in enumerate(hoy, 1) if x in r["miembros"]]
        if dentro:
            sucio.append(x)
        print("   %-38s en el TRAMO 2 vivo: %-22s en el lote CERRADO entero: %s"
              % (x, "SI, actos %s" % dentro if dentro else "NO",
                 enlote if enlote else "NO"))
    print("   GUARDA: %s" % ("ROJO" if sucio else "VERDE, ninguno de los cuatro entra"))
    print()

    print("--- GUARDA DE SOLAPE CON EL TRAMO 1 ---")
    solapan = [(f["orden"], sorted(set(f["acto"]["miembros"]) & mi1)) for f in vivos
               if set(f["acto"]["miembros"]) & mi1]
    print("   actos vivos del tramo 2 que tocan un miembro del tramo 1: %d" % len(solapan))
    print("   GUARDA: %s" % ("ROJO" if solapan else "VERDE, ningun solape"))
    print()

    print("--- EL TRAMO 2 VIVO, EN EL ORDEN DEL TRAMO ---")
    print()
    print("  %-4s %-5s %-6s %-7s %-20s %s"
          % ("acto", "hoy", "en 48", "tamano", "clases internas", "miembros"))
    tam = {}
    figuras = {"PURO A": 0, "MIXTO": 0}
    salida = []
    for f in sorted(vivos, key=lambda f: f["orden"]):
        r = f["acto"]
        cl = r["clases_internas"]
        puro = set(cl) == {"A"}
        figuras["PURO A" if puro else "MIXTO"] += 1
        tam[r["tamano"]] = tam.get(r["tamano"], 0) + 1
        print("  %-4d %-5d %-6d %-7d %-20s %s"
              % (f["orden"], f["puesto_hoy"], f["puesto_v48"], r["tamano"], cl,
                 ", ".join(sorted(r["miembros"]))))
        fila = dict(r)
        fila["orden_tramo2"] = f["orden"]
        fila["puesto_hoy"] = f["puesto_hoy"]
        fila["puesto_v48"] = f["puesto_v48"]
        fila["figura"] = "PURO A" if puro else "MIXTO"
        salida.append(fila)
    print()
    print("  actos VIVOS del tramo 2: %d" % len(vivos))
    print("  por tamano             : %s" % dict(sorted(tam.items())))
    print("  por figura             : %s" % figuras)
    print("  nodos implicados       : %d" % sum(r["tamano"] for r in salida))
    print("  nodos que MORIRIAN si se funden todos: %d"
          % sum(r["tamano"] - 1 for r in salida))
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
