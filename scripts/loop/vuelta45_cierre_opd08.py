# -*- coding: utf-8 -*-
"""vuelta45_cierre_opd08.py - EL CIERRE DE OP-D-08, MEDIDO. SOLO LECTURA.

EXISTE POR LA REGLA 1 DE EJECUTOR.md, cuarto renglon (la tabla se imprime, no se
teclea) y por su segundo renglon (el estado al cierre SE MIDE AL CIERRE): esta
vuelta movio el marcador con la relectura del 784, asi que la tabla del cierre se
RECOMPUTA aqui y no se copia de la apertura.

Contesta los NUEVE puntos del campo verificacion de OP-D-08, leidos del fichero
y no tecleados, y remata con el estado recomputado.

Uso: python scripts/loop/vuelta45_cierre_opd08.py
"""
import io
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
COLA = os.path.join(RAIZ, "docs", "COSTURAS_INTERNAS.jsonl")
CAMPOS = ("nodos_previos", "nodos_siguientes")

NODO = "lienzo_modelo_negocio"
OTRO = "swot_business_model_canvas"
MARCA = re.compile(r"^(NO SE JUZGA|NO PUEDO JUZGAR|CONGELAD)", re.I)


def main():
    todos = {}
    for nombre in sorted(os.listdir(NODOS)):
        if nombre.endswith(".json"):
            d = json.loads(io.open(os.path.join(NODOS, nombre), encoding="utf-8").read())
            todos[d["node_id"]] = d
    vers = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
    por_puesto = dict((v["puesto_intra"], v) for v in vers)

    alias = {}
    for nid, d in todos.items():
        for a in (d.get("ids_alias") or []):
            alias[a] = nid

    def resolver(x):
        visto = set()
        while x in alias and x not in visto:
            visto.add(x)
            x = alias[x]
        return x

    ady = {}
    n_a = 0
    for v in vers:
        if v.get("clase") != "A":
            continue
        n_a += 1
        a, b = resolver(v["nodo_a"]), resolver(v["nodo_b"])
        ady.setdefault(a, set()).add(b)
        ady.setdefault(b, set()).add(a)

    def componente(sem):
        pila, visto = [sem], set()
        while pila:
            x = pila.pop()
            if x in visto:
                continue
            visto.add(x)
            for y in ady.get(x, ()):
                if y not in visto:
                    pila.append(y)
        return visto

    op = None
    for l in io.open(OPS, encoding="utf-8"):
        if l.strip():
            d = json.loads(l)
            if d.get("id_op") == "OP-D-08":
                op = d
                break

    print("=" * 78)
    print("EL CIERRE DE OP-D-08, MEDIDO HOY CONTRA EL ARCHIVO Y EL GRAFO")
    print("=" * 78)

    print()
    print("### (1) LOS NUEVE PUNTOS DEL CAMPO verificacion, copiados del fichero")
    print()
    for i, p in enumerate(op["verificacion"], 1):
        print("  %d. %s" % (i, p[:150] + ("..." if len(p) > 150 else "")))

    print()
    print("### (2) EL CASO POSITIVO: EL PAR 784, RELEIDO Y JUZGADO")
    print()
    v = por_puesto[784]
    print("  puesto 784 | clase HOY: %s | %s contra %s"
          % (v["clase"], v["nodo_a"], v["nodo_b"]))
    r = (v.get("razon") or "").strip()
    print("  su razon ABRE con marca de congelado: %s" % bool(MARCA.match(r)))
    print("  su razon lleva la frase NO SE JUZGA HOY: %s" % ("NO SE JUZGA HOY" in r))
    print("  su razon declara la correccion: %s" % ("CORRECCION DECLARADA" in r))
    print("  su razon conserva la vieja a la vista: %s"
          % ("LA RAZON VIEJA SE CONSERVA ENTERA" in r))
    print()
    n_hoy = sum(1 for x in vers if "NO SE JUZGA HOY" in (x.get("razon") or ""))
    abiertos = [x for x in vers if MARCA.match((x.get("razon") or "").strip())]
    print("  pares del archivo ENTERO con la frase NO SE JUZGA HOY: %d" % n_hoy)
    print("  pares del archivo ENTERO que abren con marca de congelado: %d" % len(abiertos))
    for x in abiertos:
        print("    puesto %-6d clase %-2s  %s con %s"
              % (x["puesto_intra"], x.get("clase"), x["nodo_a"], x["nodo_b"]))

    print()
    print("### (3) EL RECOMPUTO DEL CIERRE TRANSITIVO tras el acto (banco 9.21)")
    print()
    print("  pares de clase A vigentes en el archivo hoy: %d" % n_a)
    for nid in (NODO, OTRO):
        comp = componente(resolver(nid))
        print("  %-32s componente hoy: %d  (%s)"
              % (nid, len(comp) or 1, ", ".join(sorted(comp)) or nid))
    print()
    print("  LA GUARDA QUE LA OPERACION ESCRIBIO: 'si el 784 saliera A este nodo")
    print("  dejaria de ser componente de uno'. Salio D, asi que NO aporta arista")
    print("  y el nodo SIGUE siendo componente de uno.")

    print()
    print("### (4) CERO MOVIMIENTO DE GRAFO, re-medido al cierre")
    print()
    d = todos[NODO]
    prev, sig = d.get("nodos_previos") or [], d.get("nodos_siguientes") or []
    total = sum(len(x.get(c) or []) for x in todos.values() for c in CAMPOS)
    print("  vecinos de %s: %d previos + %d siguientes = %d"
          % (NODO, len(prev), len(sig), len(prev) + len(sig)))
    print("  entradas de arista del grafo entero: %d sobre %d ficheros"
          % (total, len(todos)))
    print("  ids_alias creados por este acto: %d"
          % len(d.get("ids_alias") or []))
    print("  el nodo sigue VIVO: %s"
          % (not (d.get("deprecado") or d.get("deprecated"))))
    print()
    print("  LA ARISTA DEL PAR 784, buscada al cierre en los DOS sentidos:")
    e = todos[OTRO]
    print("    %s -> %s en siguientes: %s" % (NODO, OTRO, OTRO in sig))
    print("    %s -> %s en previos   : %s"
          % (OTRO, NODO, NODO in (e.get("nodos_previos") or [])))
    print("    ARISTA DIRIGIDA CON SU ESPEJO: %s"
          % (OTRO in sig and NODO in (e.get("nodos_previos") or [])))

    print()
    print("### (5) EL RECUENTO QUE CIERRA LA CIRUGIA, y el nodo resultante")
    print()
    pasos = d.get("pasos_accionables") or []
    bajo = [p.lower() for p in pasos]
    print("  pasos: %d  |  condiciones: %d  |  fuente: %s"
          % (len(pasos), len(d.get("condiciones_activacion") or []), d.get("fuente")))
    print("  pasos con el literal 'cada uno de los 9 bloques': %d"
          % sum(1 for p in bajo if u"cada uno de los 9 bloques" in p))
    print("  pasos que mandan imprimir: %d" % sum(1 for p in bajo if u"imprimir" in p))
    print()
    for i, p in enumerate(pasos, 1):
        print("   %2d. %s" % (i, p))

    print()
    print("### (6) LA SENAL DE COSTURA DEL NODO, antes y despues")
    print()
    cola = [json.loads(l) for l in io.open(COLA, encoding="utf-8") if l.strip()]
    porid = dict((x["node_id"], x) for x in cola)
    x = porid.get(NODO)
    if x:
        print("  %s EN LA COLA: pasos %d | bloque %s (corte tras %s) | pareja %s"
              % (NODO, x["pasos"], x["sim_bloque"], x["corte"], x["sim_pareja"]))
        print("    disparo_bloque %s | disparo_pareja %s"
              % (x["disparo_bloque"], x["disparo_pareja"]))
    else:
        print("  %s FUERA DE LA COLA" % NODO)
    print("  nodos en la cola: %d sobre %d activos"
          % (len(cola), sum(1 for n in todos.values()
                            if not (n.get("deprecado") or n.get("deprecated")))))
    print()
    print("  CITA Y NO JUZGA: la cola global no es base de lectura (limite")
    print("  declarado por el acta de la vuelta 40, seccion 5 pregunta 2).")

    print()
    print("### (7) EL ESTADO AL CIERRE, RECOMPUTADO AL CIERRE (regla 1)")
    print()
    f = vv = dd = 0
    for nid, x in todos.items():
        f += 1
        if x.get("deprecado") or x.get("deprecated"):
            dd += 1
        else:
            vv += 1
    import collections
    c = collections.Counter(x["clase"] for x in vers)
    print("  ficheros    : %d" % f)
    print("  vivos       : %d" % vv)
    print("  deprecados  : %d" % dd)
    print("  enlaces     : %d (previos mas siguientes)" % total)
    print("  cola de costuras: %d nodos sobre %d activos (%.1f por ciento)"
          % (len(cola), vv, 100.0 * len(cola) / vv))
    print("  marcador    : n %d | A %d B %d C %d D %d | tasa de A %.1f por ciento"
          % (len(vers), c["A"], c["B"], c["C"], c["D"], 100.0 * c["A"] / len(vers)))
    print("  estado declarado en OPERACIONES.jsonl: %s | fecha_corte: %s"
          % (op.get("estado"), op.get("fecha_corte")))
    print("  aristas_nuevas de la operacion: %r (vacio = cero aristas que poner)"
          % (op.get("aristas_nuevas"),))

    print()
    print("=" * 78)
    print("FIN DEL CIERRE MEDIDO")
    print("=" * 78)
    return 0


raise SystemExit(main())
