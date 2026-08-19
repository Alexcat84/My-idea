# -*- coding: utf-8 -*-
"""vuelta39_caso_positivo.py

CASO POSITIVO de las dos fusiones de OP-D-04. Se corre DOS veces con el MISMO
comando: ANTES de ejecutar (tiene que CAER) y DESPUES (tiene que PASAR). Un caso
positivo que pasa las dos veces no prueba nada, y por eso las pruebas de
CONSERVACION, que si pasan las dos veces a proposito, se cuentan APARTE y no
suman al marcador.

SUCESOR DECLARADO de scripts/loop/vuelta33_caso_positivo.py, y lo que cambia va
dicho porque cambiar un instrumento sin declararlo es lo que la regla 2 prohibe:

  1. DOS ABSORBIDOS por operacion, no uno: la muerte, el alias y la ficha se
     comprueban por cada uno de los dos.
  2. LA FUENTE DEL SUPERVIVIENTE se comprueba, y las de los absorbidos SE
     IMPRIMEN Y NO SE EXIGEN IGUALES: los dos actos de OP-D-04 son de FUENTE
     MIXTA, medido. Lo que se exige es que la fuente de cada absorbido viaje
     verbatim a su ficha de merged_originals, que es donde el archivo la guarda.
  3. EL PRESERVAR Y LOS RASTROS se buscan en el NODO RESULTANTE ENTERO (pasos,
     condiciones, entregable y resumen) y se imprime EN CUAL sobreviven. Tres
     piezas de la alternancia viven en el entregable y en el resumen, medido.
  4. LA ETIQUETA DEL ARBOL se comprueba ademas del titulo (a6 del acta de la
     vuelta 38 nombra las dos).
  5. EL CUARTO MIEMBRO: si el plan lo trae, se comprueba que la arista con
     brainstorming quede declarada EN LOS DOS EXTREMOS.

Uso: python scripts/loop/vuelta39_caso_positivo.py docs/loop/PLAN_V38_OPD04_TALLER.json
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
CAMPOS = ("nodos_previos", "nodos_siguientes")


def cargar():
    fuera = {}
    for nombre in sorted(os.listdir(NODOS)):
        if nombre.endswith(".json"):
            d = json.load(io.open(os.path.join(NODOS, nombre), encoding="utf-8"))
            fuera[d["node_id"]] = d
    return fuera


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    plan = json.load(io.open(sys.argv[1], encoding="utf-8"))
    G = cargar()
    sup = plan["superviviente"]
    absorbidos = list(plan["absorbidos"])
    sim = plan["simulacion"]

    print("CASO POSITIVO: %s" % plan["operacion"])
    print("=" * 78)
    pasan = caen = 0
    cons_si = cons_no = 0
    marcador = {"pasan": 0, "caen": 0}

    def prueba(ok, texto):
        print("  [%s] %s" % ("PASA" if ok else "CAE ", texto))
        marcador["pasan" if ok else "caen"] += 1

    s = G.get(sup)
    if s is None or any(G.get(m) is None for m in absorbidos):
        print("  [CAE ] alguno de los TRES nodos no existe en el grafo")
        return 1

    print("\nEL SUPERVIVIENTE, %s" % sup)
    sp = s.get("pasos_accionables") or []
    sc = s.get("condiciones_activacion") or []
    prueba(len(sp) == len(plan["pasos_finales"]),
           "tiene %d pasos, los %d que el plan deja" % (len(sp), len(plan["pasos_finales"])))
    prueba(len(sc) == len(plan["condiciones_finales"]),
           "tiene %d condiciones, las %d que el plan deja" % (len(sc), len(plan["condiciones_finales"])))
    prueba(sp == plan["pasos_finales"], "sus pasos son EXACTAMENTE los del plan sellado, letra a letra")
    prueba(sc == plan["condiciones_finales"], "sus condiciones son exactamente las del plan")
    prueba(s.get("entregable_esperado") == plan["entregable_final"], "su entregable es el del plan")
    prueba(s.get("resumen_teorico") == plan["resumen_final"], "su resumen es el del plan")
    prueba(s.get("titulo_concepto") == plan["titulo_sin_cambio"],
           "su titulo NO cambio (a6 del acta): %r" % plan["titulo_sin_cambio"])
    prueba(s.get("etiqueta_arbol") == plan["etiqueta_arbol_sin_cambio"],
           "su etiqueta_arbol NO cambio (a6 del acta): %r" % plan["etiqueta_arbol_sin_cambio"])
    prueba(s.get("fuente") == plan["fuente_esperada"], "su fuente NO cambio")

    partes = {"pasos": " ".join(sp),
              "condiciones": " ".join(sc),
              "entregable": s.get("entregable_esperado") or "",
              "resumen": s.get("resumen_teorico") or ""}

    def sedes(pieza):
        return [k for k in ("pasos", "condiciones", "entregable", "resumen") if pieza in partes[k]]

    print("\nEL PRESERVAR, las piezas que la operacion manda salvar, con su sede impresa")
    for pieza in plan["preservar_literal"]:
        d_sedes = sedes(pieza)
        prueba(bool(d_sedes), "sobrevive literal en %s: %r" % (d_sedes or "NINGUN CAMPO", pieza))

    print("\nEL ALIAS Y LA FICHA DE LOS DOS ABSORBIDOS")
    for muere in absorbidos:
        prueba(muere in (s.get("ids_alias") or []), "%r esta en ids_alias del superviviente" % muere)
        ficha = [m for m in (s.get("merged_originals") or []) if m.get("node_id") == muere]
        prueba(bool(ficha), "%r tiene su entrada en merged_originals" % muere)
        if ficha:
            prueba(ficha[0].get("fuente") == (G[muere].get("fuente")),
                   "la ficha de %r guarda su fuente verbatim: %r" % (muere, ficha[0].get("fuente")))
    prueba(sup not in (s.get("ids_alias") or []),
           "el superviviente NO se tiene a si mismo como alias (la trampa de test_gate_alias)")

    for muere in absorbidos:
        print("\nLA MUERTE DEL ABSORBIDO, %s" % muere)
        a = G[muere]
        prueba(bool(a.get("deprecado")), "esta marcado deprecado")
        prueba(os.path.exists(os.path.join(NODOS, muere + ".json")),
               "su fichero SIGUE EXISTIENDO: una fusion depreca, no borra")
        prueba(len(a.get("pasos_accionables") or []) == plan["pasos_totales"][muere],
               "su texto quedo INTACTO: %d pasos, los mismos que antes"
               % len(a.get("pasos_accionables") or []))
        prueba(len(a.get("condiciones_activacion") or []) == plan["condiciones_totales"][muere],
               "sus condiciones quedaron INTACTAS: %d"
               % len(a.get("condiciones_activacion") or []))

    print("\nLAS REDIRECCIONES")
    quedan_vivos, quedan_muertos = [], []
    for nid, d in G.items():
        if nid in absorbidos:
            continue
        for campo in CAMPOS:
            for muere in absorbidos:
                if muere in (d.get(campo) or []):
                    if d.get("deprecado") or d.get("deprecated"):
                        quedan_muertos.append((nid, campo, muere))
                    else:
                        quedan_vivos.append((nid, campo, muere))
    prueba(not quedan_vivos,
           "ningun nodo VIVO sigue nombrando a los dos absorbidos (quedan %d)" % len(quedan_vivos))
    declarados = sorted((r["nodo"], r["campo"], r["nombraba"])
                        for r in (sim.get("redirecciones_no_tocadas_por_deprecadas") or []))
    prueba(sorted(quedan_muertos) == declarados,
           "los deprecados que aun los nombran son EXACTAMENTE los del plan: hoy %s, plan %s"
           % (sorted(quedan_muertos), declarados))
    for r in sim["redirecciones_esperadas"]:
        d = G.get(r["nodo"]) or {}
        prueba(sup in (d.get(r["campo"]) or []),
               "%s.%s ya apunta a %s" % (r["nodo"], r["campo"], sup))

    dupes = auto = 0
    for nid, d in G.items():
        for campo in CAMPOS:
            lista = d.get(campo) or []
            if len(lista) != len(set(lista)):
                dupes += 1
            if nid in lista:
                auto += 1
    prueba(dupes == 0, "cero listas de aristas con duplicados en TODO el grafo (halladas %d)" % dupes)
    prueba(auto == 0, "cero auto-aristas en TODO el grafo (halladas %d)" % auto)

    cuarto = plan.get("cuarto_miembro")
    if cuarto:
        print("\nEL CUARTO MIEMBRO, %s, declarado en LOS DOS EXTREMOS" % cuarto)
        c = G.get(cuarto) or {}
        aqui = [k for k in CAMPOS if cuarto in (s.get(k) or [])]
        alla = [k for k in CAMPOS if sup in (c.get(k) or [])]
        prueba(bool(aqui), "%s nombra a %s en %s" % (sup, cuarto, aqui or "NINGUN CAMPO"))
        prueba(bool(alla), "%s nombra a %s en %s" % (cuarto, sup, alla or "NINGUN CAMPO"))

    print("\n(conservacion) LOS RASTROS, que pasan las dos veces a proposito")
    for r in plan["rastros"]:
        d_sedes = sedes(r)
        print("  (conservacion) [%s] el rastro %r sigue vivo en %s"
              % ("SI" if d_sedes else "NO", r, d_sedes or "NINGUN CAMPO"))
        if d_sedes:
            cons_si += 1
        else:
            cons_no += 1

    pasan, caen = marcador["pasan"], marcador["caen"]
    print()
    print("=" * 78)
    print("RESULTADO: %d PASAN, %d CAEN" % (pasan, caen))
    print("CONSERVACION (aparte, no suma): %d vivos, %d muertos" % (cons_si, cons_no))
    return 0 if caen == 0 else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
