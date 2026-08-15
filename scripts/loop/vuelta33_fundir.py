# -*- coding: utf-8 -*-
"""vuelta33_fundir.py

EJECUTA la fusion sellada en docs/loop/PLAN_V33_OPD02_FUSION.json. Es la PRIMERA
fusion del plan de la pasada unica que se escribe contra `dataset/`, y por eso
lleva mas guardas que un destejido: un destejido colapsa dentro de un nodo, una
fusion MATA un nodo y redirige a quien lo nombraba.

MODOS: --simular (por defecto, cero escrituras) y --ejecutar.

LAS GUARDAS, todas escritas para CAER y no para pasar:

  1. FUENTE de los dos nodos igual a la del plan, y ninguno deprecado todavia.
  2. CONTEOS de pasos y condiciones de los dos nodos iguales a los del plan.
  3. GUARDA DE TEXTO: cada paso y cada condicion de los dos nodos empieza por su
     prefijo sellado. Si alguien edito un nodo entre el sellado y la ejecucion,
     esto cae.
  4. COBERTURA EXACTA: los 5 mas 5 pasos y las 3 mas 2 condiciones aparecen cada
     uno en exactamente un destino.
  5. PRESERVAR LITERAL: las tres piezas del campo `preservar` de OP-D-02 tienen
     que quedar dentro de los pasos escritos.
  6. RASTROS: cada rastro del plan sigue vivo en el nodo resultante.
  7. CERO AUTO-ARISTA: el superviviente no puede acabar nombrandose a si mismo.
  8. CERO DUPLICADA: ninguna lista de aristas puede acabar con el mismo id dos
     veces (la clase OP-S-12, que toda fusion fabrica: aqui se limpia en el acto).
  9. EL CENSO NO CAMBIA: 3.853 ficheros antes y despues. Una fusion NO borra el
     fichero del absorbido, lo deprecia. Los 314 alias con fichero propio del
     archivo son exactamente esa convencion, medida hoy.

QUE ESCRIBE, y nada mas que eso:
  - el superviviente: pasos, condiciones, entregable, resumen, ids_alias mas el
    id del absorbido, merged_originals mas su ficha
  - el absorbido: `deprecado: true`, y NADA MAS. Su texto se queda entero, que es
    lo que hace auditable la fusion
  - los nodos que nombraban al absorbido: la referencia pasa al superviviente

Uso:
  python scripts/loop/vuelta33_fundir.py [--simular|--ejecutar]
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
PLAN = os.path.join(RAIZ, "docs", "loop", "PLAN_V33_OPD02_FUSION.json")
CAMPOS = ("nodos_previos", "nodos_siguientes")


def ruta(nid):
    return os.path.join(NODOS, nid + ".json")


def leer_crudo(nid):
    with io.open(ruta(nid), encoding="utf-8", newline="") as fh:
        bruto = fh.read()
    cola = ""
    while bruto and bruto[-1] in "\r\n":
        cola = bruto[-1] + cola
        bruto = bruto[:-1]
    return json.loads(bruto), cola


def escribir(nid, datos, cola):
    with io.open(ruta(nid), "w", encoding="utf-8", newline="") as fh:
        fh.write(json.dumps(datos, ensure_ascii=False, indent=2) + cola)


def main():
    modo = "--simular"
    for x in sys.argv[1:]:
        if x in ("--simular", "--ejecutar"):
            modo = x
    plan = json.load(io.open(PLAN, encoding="utf-8"))
    sup, absorbido = plan["superviviente"], plan["absorbido"]

    print("PLAN     : %s" % PLAN)
    print("OPERACION: %s" % plan["operacion"])
    print("MODO     : %s" % modo)
    print("=" * 78)

    fallos = []
    censo_antes = len([f for f in os.listdir(NODOS) if f.endswith(".json")])
    print("censo de ficheros ANTES: %d" % censo_antes)

    s, cola_s = leer_crudo(sup)
    a, cola_a = leer_crudo(absorbido)

    # GUARDA 1
    for nid, d in ((sup, s), (absorbido, a)):
        if d.get("fuente") != plan["fuente_esperada"]:
            fallos.append("%s: fuente inesperada %r" % (nid, d.get("fuente")))
        if d.get("deprecado") or d.get("deprecated"):
            fallos.append("%s: ya esta deprecado" % nid)
    print("guarda 1, fuente y vida de los dos nodos: %s" % ("OK" if not fallos else "ROJO"))

    sp = list(s.get("pasos_accionables") or [])
    ap = list(a.get("pasos_accionables") or [])
    sc = list(s.get("condiciones_activacion") or [])
    ac = list(a.get("condiciones_activacion") or [])

    # GUARDA 2
    esperados = (plan["pasos_totales_superviviente"], plan["pasos_totales_absorbido"],
                 plan["condiciones_totales_superviviente"], plan["condiciones_totales_absorbido"])
    reales = (len(sp), len(ap), len(sc), len(ac))
    if reales != esperados:
        fallos.append("conteos %s, el plan esperaba %s" % (reales, esperados))
    print("guarda 2, conteos %s contra %s: %s"
          % (reales, esperados, "OK" if reales == esperados else "ROJO"))

    # GUARDA 3
    malos = []
    for lista, prefijos, etq in (
        (sp, plan["prefijos_superviviente"], "pasos de " + sup),
        (ap, plan["prefijos_absorbido"], "pasos de " + absorbido),
        (sc, plan["prefijos_condiciones_superviviente"], "condiciones de " + sup),
        (ac, plan["prefijos_condiciones_absorbido"], "condiciones de " + absorbido),
    ):
        if len(lista) != len(prefijos):
            malos.append("%s: %d contra %d prefijos" % (etq, len(lista), len(prefijos)))
            continue
        for i, p in enumerate(prefijos):
            if not lista[i].startswith(p):
                malos.append("%s, %d: no calza con %r" % (etq, i + 1, p))
    if malos:
        fallos.extend(malos)
    print("guarda 3, texto contra los prefijos sellados: %d de %d calzan"
          % (len(sp) + len(ap) + len(sc) + len(ac) - len(malos), len(sp) + len(ap) + len(sc) + len(ac)))

    # GUARDA 4
    for etq, grupos, esperado in (
        ("pasos", plan["grupos_pasos"],
         ["S%d" % i for i in range(1, len(sp) + 1)] + ["A%d" % i for i in range(1, len(ap) + 1)]),
        ("condiciones", plan["grupos_condiciones"],
         ["SC%d" % i for i in range(1, len(sc) + 1)] + ["AC%d" % i for i in range(1, len(ac) + 1)]),
    ):
        usados = [o for g in grupos for o in g["origenes"]]
        rep = sorted({o for o in usados if usados.count(o) > 1})
        fal = sorted(set(esperado) - set(usados))
        sob = sorted(set(usados) - set(esperado))
        print("guarda 4, cobertura de %s: %d de %d, repetidos %s, faltan %s, sobran %s"
              % (etq, len(usados), len(esperado), rep, fal, sob))
        if rep or fal or sob:
            fallos.append("cobertura rota en %s" % etq)

    pasos_finales = list(plan["pasos_finales"])
    cond_finales = list(plan["condiciones_finales"])
    cuerpo = " ".join(pasos_finales)

    # GUARDA 5
    for pieza in plan["preservar_literal"]:
        if pieza not in cuerpo:
            fallos.append("preservar ausente: %r" % pieza)
    print("guarda 5, las tres piezas del preservar, literales: %d de %d presentes"
          % (sum(1 for p in plan["preservar_literal"] if p in cuerpo), len(plan["preservar_literal"])))

    # GUARDA 6
    vivos = sum(1 for r in plan["rastros"] if r in cuerpo)
    if vivos != len(plan["rastros"]):
        for r in plan["rastros"]:
            if r not in cuerpo:
                fallos.append("rastro muerto: %r" % r)
    print("guarda 6, rastros vivos en el resultado: %d de %d" % (vivos, len(plan["rastros"])))

    # Las redirecciones, medidas contra el grafo de HOY y no contra el plan.
    todos = {}
    for nombre in sorted(os.listdir(NODOS)):
        if nombre.endswith(".json"):
            d, c = leer_crudo(nombre[:-5])
            todos[d["node_id"]] = (d, c)
    # SOLO SE REDIRIGE LO VIVO, y el criterio no es mio: es el del instrumento
    # sellado de la casa, scripts/plan/simular_fusion.py, que salta los deprecados
    # al listar las entradas que se redirigen (su linea 87). Un nodo deprecado es
    # registro historico, y su cableado se conserva por la misma razon por la que
    # el texto del absorbido se conserva: para que la fusion se pueda auditar.
    # LOS DEPRECADOS QUE NOMBRAN AL ABSORBIDO NO SE FILTRAN EN SILENCIO: SE
    # IMPRIMEN CON SU NOMBRE Y SE DICE QUE NO SE TOCAN.
    redirecciones, muertos = [], []
    for nid, (d, _c) in todos.items():
        if nid == absorbido:
            continue
        for campo in CAMPOS:
            if absorbido in (d.get(campo) or []):
                if d.get("deprecado") or d.get("deprecated"):
                    muertos.append((nid, campo))
                else:
                    redirecciones.append((nid, campo))
    print("redirecciones medidas hoy sobre nodos VIVOS: %d" % len(redirecciones))
    for nid, campo in redirecciones:
        print("    %-40s %-18s -> %s" % (nid, campo, sup))
    print("nodos DEPRECADOS que nombran al absorbido y NO se tocan: %d" % len(muertos))
    for nid, campo in muertos:
        print("    %-40s %-18s (deprecado: se deja como registro historico)" % (nid, campo))
    esperadas = {(r["nodo"], r["campo"]) for r in plan["redirecciones_esperadas"]}
    if set(redirecciones) != esperadas:
        fallos.append("las redirecciones de hoy no son las del plan: hoy %s, plan %s"
                      % (sorted(set(redirecciones)), sorted(esperadas)))
    print("guarda de redirecciones contra el plan: %s"
          % ("OK" if set(redirecciones) == esperadas else "ROJO"))

    if fallos:
        print()
        print("SE ABORTA SIN ESCRIBIR, %d fallo(s):" % len(fallos))
        for f in fallos:
            print("  [ROJO] %s" % f)
        return 1

    # --- construir el resultado sobre COPIA EN MEMORIA ---
    s_nuevo = json.loads(json.dumps(s))
    s_nuevo["pasos_accionables"] = pasos_finales
    s_nuevo["condiciones_activacion"] = cond_finales
    s_nuevo["entregable_esperado"] = plan["entregable_final"]
    s_nuevo["resumen_teorico"] = plan["resumen_final"]
    alias = list(s_nuevo.get("ids_alias") or [])
    if absorbido not in alias:
        alias.append(absorbido)
    s_nuevo["ids_alias"] = alias
    merged = list(s_nuevo.get("merged_originals") or [])
    if not any(m.get("node_id") == absorbido for m in merged):
        merged.append({"node_id": absorbido,
                       "titulo": a.get("titulo_concepto"),
                       "fuente": a.get("fuente")})
    s_nuevo["merged_originals"] = merged

    a_nuevo = json.loads(json.dumps(a))
    a_nuevo["deprecado"] = True

    cambios = {sup: (s_nuevo, cola_s), absorbido: (a_nuevo, cola_a)}
    for nid, campo in redirecciones:
        d, c = todos[nid]
        d2 = cambios.get(nid, (json.loads(json.dumps(d)), c))[0]
        lista = [sup if x == absorbido else x for x in (d2.get(campo) or [])]
        limpia, vistos = [], set()
        for x in lista:
            if x not in vistos:
                vistos.add(x)
                limpia.append(x)
        d2[campo] = limpia
        cambios[nid] = (d2, c)

    # GUARDA 7 y 8, sobre la copia ya construida
    for nid, (d, _c) in cambios.items():
        for campo in CAMPOS:
            lista = d.get(campo) or []
            if nid in lista:
                fallos.append("AUTO-ARISTA: %s se nombra a si mismo en %s" % (nid, campo))
            if len(lista) != len(set(lista)):
                fallos.append("DUPLICADA: %s tiene repetidos en %s" % (nid, campo))
    print("guarda 7, cero auto-arista: %s" % ("OK" if not fallos else "ROJO"))
    print("guarda 8, cero duplicada: %s" % ("OK" if not fallos else "ROJO"))

    if fallos:
        print()
        print("SE ABORTA SIN ESCRIBIR, %d fallo(s):" % len(fallos))
        for f in fallos:
            print("  [ROJO] %s" % f)
        return 1

    print()
    print("EL RESULTADO, sobre copia en memoria:")
    print("  %s: %d pasos, %d condiciones, alias %s"
          % (sup, len(s_nuevo["pasos_accionables"]), len(s_nuevo["condiciones_activacion"]),
             s_nuevo["ids_alias"]))
    for i, p in enumerate(s_nuevo["pasos_accionables"], 1):
        print("    %d. %s" % (i, p))
    print("  entregable: %s" % s_nuevo["entregable_esperado"])
    print("  %s: deprecado True, texto INTACTO (%d pasos, %d condiciones)"
          % (absorbido, len(a_nuevo.get("pasos_accionables") or []),
             len(a_nuevo.get("condiciones_activacion") or [])))
    print("  ficheros que se tocarian: %d" % len(cambios))

    if modo == "--simular":
        print()
        print("SIMULACION: cero escrituras.")
        return 0

    for nid, (d, c) in cambios.items():
        escribir(nid, d, c)
    censo_despues = len([f for f in os.listdir(NODOS) if f.endswith(".json")])
    print()
    print("ESCRITO. censo de ficheros DESPUES: %d (antes %d)" % (censo_despues, censo_antes))
    if censo_despues != censo_antes:
        print("  [ROJO] EL CENSO SE MOVIO, y una fusion no borra ficheros")
        return 1
    print("guarda 9, el censo no se movio: OK")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
