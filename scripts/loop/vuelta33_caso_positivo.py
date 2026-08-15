# -*- coding: utf-8 -*-
"""vuelta33_caso_positivo.py

CASO POSITIVO de la fusion de OP-D-02. Se corre DOS veces con el mismo comando:
ANTES de ejecutar (tiene que CAER) y DESPUES (tiene que PASAR). Un caso positivo
que pasa las dos veces no prueba nada, y por eso las pruebas de CONSERVACION, que
si pasan las dos veces a proposito, se cuentan APARTE y no suman al marcador.

SUCESOR DECLARADO de scripts/loop/vuelta32_caso_positivo.py, y lo que cambia va
dicho porque cambiar un instrumento sin declararlo es lo que la regla 2 prohibe:
aquel media UN nodo por ficha (un destejido colapsa dentro del nodo). Una FUSION
toca DOS nodos y a quien los nombraba, asi que este anade tres familias de prueba
que alli no tenian sentido:

  - LA MUERTE DEL ABSORBIDO: `deprecado` en true, y su texto INTACTO
  - EL ALIAS Y LA FICHA: el id del absorbido dentro de `ids_alias` del
    superviviente, y su entrada en `merged_originals`
  - LAS REDIRECCIONES: ningun nodo vivo puede seguir nombrando al absorbido, y
    ninguna lista puede quedar con duplicados ni con auto-arista

Uso: python scripts/loop/vuelta33_caso_positivo.py docs/loop/PLAN_V33_OPD02_FUSION.json
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
    sup, absorbido = plan["superviviente"], plan["absorbido"]

    print("CASO POSITIVO: %s" % plan["operacion"])
    print("=" * 78)
    pasan = caen = 0
    cons_si = cons_no = 0

    def prueba(ok, texto):
        nonlocal pasan, caen
        print("  [%s] %s" % ("PASA" if ok else "CAE ", texto))
        if ok:
            pasan += 1
        else:
            caen += 1

    s = G.get(sup)
    a = G.get(absorbido)
    if s is None or a is None:
        print("  [CAE ] uno de los dos nodos no existe en el grafo")
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
    prueba(s.get("entregable_esperado") == plan["entregable_final"],
           "su entregable es el del plan (absorbe el analisis competitivo y las pruebas de concepto)")
    prueba(s.get("titulo_concepto") == plan["titulo_sin_cambio"], "su titulo NO cambio")
    prueba(s.get("fuente") == plan["fuente_esperada"], "su fuente NO cambio (los dos eran del mismo libro)")

    cuerpo = " ".join(sp)
    print("\nEL PRESERVAR, las tres piezas que la operacion manda salvar")
    for pieza in plan["preservar_literal"]:
        prueba(pieza in cuerpo, "esta literal en los pasos: %r" % pieza)

    print("\nEL ALIAS Y LA FICHA DEL ABSORBIDO")
    prueba(absorbido in (s.get("ids_alias") or []),
           "%r esta en ids_alias del superviviente" % absorbido)
    prueba(any(m.get("node_id") == absorbido for m in (s.get("merged_originals") or [])),
           "%r tiene su entrada en merged_originals" % absorbido)
    prueba(sup not in (s.get("ids_alias") or []),
           "el superviviente NO se tiene a si mismo como alias (la trampa de test_gate_alias)")

    print("\nLA MUERTE DEL ABSORBIDO, %s" % absorbido)
    prueba(bool(a.get("deprecado")), "esta marcado deprecado")
    prueba(os.path.exists(os.path.join(NODOS, absorbido + ".json")),
           "su fichero SIGUE EXISTIENDO: una fusion depreca, no borra")
    prueba(len(a.get("pasos_accionables") or []) == plan["pasos_totales_absorbido"],
           "su texto quedo INTACTO: %d pasos, los mismos que antes"
           % len(a.get("pasos_accionables") or []))

    # CORRECCION DECLARADA (15 ago 2026, dentro de la propia vuelta 33). La primera
    # version de esta prueba contaba TODOS los nodos y cayo despues de ejecutar, con
    # uno: front_end_homework, que esta DEPRECADO. No cayo por la ejecucion: cayo
    # porque la prueba contradecia la politica declarada de la operacion, que
    # redirige SOLO lo vivo (criterio del instrumento sellado de la casa,
    # scripts/plan/simular_fusion.py). La prueba se ajusta a la politica Y SE VUELVE
    # MAS ESTRICTA, no mas laxa: ahora exige que los deprecados que siguen nombrando
    # al absorbido sean EXACTAMENTE los que el plan declara, ni uno mas ni uno menos.
    # Se anota aqui porque cambiar una guarda que cae es de lo que mas hay que mirar.
    print("\nLAS REDIRECCIONES")
    quedan_vivos, quedan_muertos = [], []
    for nid, d in G.items():
        if nid == absorbido:
            continue
        for campo in CAMPOS:
            if absorbido in (d.get(campo) or []):
                if d.get("deprecado") or d.get("deprecated"):
                    quedan_muertos.append((nid, campo))
                else:
                    quedan_vivos.append((nid, campo))
    prueba(not quedan_vivos,
           "ningun nodo VIVO sigue nombrando a %s (quedan %d)" % (absorbido, len(quedan_vivos)))
    declarados = {(r["nodo"], r["campo"])
                  for r in (plan.get("redirecciones_no_tocadas_por_deprecadas") or [])}
    prueba(set(quedan_muertos) == declarados,
           "los deprecados que aun lo nombran son EXACTAMENTE los declarados en el plan: "
           "hoy %s, plan %s" % (sorted(set(quedan_muertos)), sorted(declarados)))
    for r in plan["redirecciones_esperadas"]:
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

    print("\n(conservacion) LOS RASTROS, que pasan las dos veces a proposito")
    for r in plan["rastros"]:
        ok = r in cuerpo
        print("  (conservacion) [%s] el rastro %r sigue vivo" % ("SI" if ok else "NO", r))
        if ok:
            cons_si += 1
        else:
            cons_no += 1

    print()
    print("=" * 78)
    print("RESULTADO: %d PASAN, %d CAEN" % (pasan, caen))
    print("CONSERVACION (aparte, no suma): %d vivos, %d muertos" % (cons_si, cons_no))
    return 0 if caen == 0 else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
