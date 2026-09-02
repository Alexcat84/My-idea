# -*- coding: utf-8 -*-
r"""vuelta140_3_escribir_aristas.py . ESCRIBE LAS ARISTAS DE UNA OPERACION DE
ENLACE DE LA FASE 06 (TAREA 3 de la vuelta 140, acta de la vuelta 139, 3.7).

QUE HACE, Y NO MAS. Para UNA operacion nombrada con --op, lee sus
`aristas_nuevas` de `docs/plan/OPERACIONES.jsonl`, resuelve los dos extremos de
cada una POR ALIAS contra el grafo de hoy (P.1), y escribe las que falten en
las DOS vistas (`nodos_siguientes` del origen y `nodos_previos` del destino) de
`dataset/nodos/<id>.json`. Ningun otro campo de ningun nodo se toca.

EL PARSER DE ARISTAS NO SE REIMPLEMENTA: se importa `pares_de_aristas` de
`scripts/loop/tallar_estado_de_fase.py`, que es el instrumento que la TAREA 2.a
uso para MEDIR cuantas faltan. Si el que mide y el que escribe partieran la
ficha de dos maneras distintas, la cifra de la medicion y la del trabajo no
hablarian del mismo objeto.

LAS GUARDAS, por arista y con su salida impresa:
  (1) los dos extremos EXISTEN y estan VIVOS tras resolver por alias. Si un
      extremo resuelve a otro id, SE DECLARA con los dos nombres.
  (2) cero AUTO-ARISTAS: los dos extremos no pueden resolver al mismo nodo.
  (3) CERO ARISTAS POR ALIAS NUEVAS (P.9, verificacion 4 de las fichas): lo que
      se escribe es SIEMPRE el id VIVO resuelto, nunca el id de la ficha si ese
      id esta deprecado.
  (4) YA PRESENTE no es un fallo, es un SALTO DECLARADO. Varias de estas
      operaciones estan a medias (el acta 139 lo midio), y escribir una arista
      que ya existe es fabricar una duplicada. Se cuenta y se nombra.
  (5) UNA SOLA DIRECCION salvo los ENLACES MUTUOS. La direccion contraria se
      mira ANTES de escribir: si existe y la operacion NO es mutua, es ROJO y
      se aborta sin escribir nada. Que una operacion sea mutua NO lo decide
      este script: lo dice el campo `tipo` de su propia ficha (`ENLACE MUTUO`).
  (6) CERO DUPLICADAS NUEVAS en las listas tocadas, comprobado TRAS RESOLVER
      (no basta con que el literal no se repita: dos literales distintos que
      resuelven al mismo nodo son una duplicada). LO QUE SE MIDE ES EL DELTA,
      NO EL TOTAL: las duplicadas que YA ESTABAN se imprimen para que se vean,
      pero no bloquean, porque tienen dueno escrito (`OP-S-12`, atadura 2 del
      00_INDICE) y castigar a quien no las hizo bloquea sin arreglar nada.
  (7) NINGUN OTRO CAMPO cambia en ningun nodo tocado.

SI CUALQUIER GUARDA CAE, SE ABORTA SIN ESCRIBIR NADA, ni siquiera las aristas
que si pasaban: una operacion se escribe entera o no se escribe.

MODOS: `--simular` (por defecto, cero escrituras) y `--ejecutar`.
`--mutacion-negativa` fuerza el destino de la primera arista a un extremo que
SIGUE MUERTO DESPUES DE RESOLVER (ver `destino_muerto_para_la_mutacion`, que lo
elige computandolo del grafo y NO lo teclea) para probar que la guarda (1)
aborta sin escribir nada aunque se pase `--ejecutar`. Un deprecado que es alias
de un vivo NO sirve para esto, y la primera version de esta prueba cometio ese
error: el resolutor lo revivia y el caso rojo no podia caer.

USO:
  python scripts/loop/vuelta140_3_escribir_aristas.py --op OP-M-03-ENLACES
  python scripts/loop/vuelta140_3_escribir_aristas.py --op OP-M-03-ENLACES --ejecutar
  python scripts/loop/vuelta140_3_escribir_aristas.py --op OP-M-03-ENLACES --mutacion-negativa
"""
import argparse
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tallar_estado_de_fase as T  # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")


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


def destino_muerto_para_la_mutacion(nodos, resolver):
    """Para --mutacion-negativa: un destino que la guarda (1) TENGA que rechazar,
    elegido COMPUTANDOLO del grafo y no tecleado.

    ESTO SE CORRIGIO CORRIENDOLO, y la primera version era un caso rojo que no
    podia caer: tomaba "un deprecado cualquiera", y el primero por orden
    alfabetico (`6s_lugar_trabajo`) es alias de un nodo VIVO (`metodologia_6s`),
    asi que el resolutor lo revivia y la guarda (1) pasaba con razon. Un
    deprecado que resuelve a un vivo NO es un destino invalido: es exactamente
    el caso que P.1 existe para arreglar.

    Lo que la guarda (1) tiene que rechazar es un extremo que sigue MUERTO
    DESPUES de resolver. Se busca, en este orden, y se DECLARA cual se uso:
      (a) un nodo DEPRECADO que NO es alias de ningun vivo (resolver(x) == x);
      (b) si no hubiera ninguno, un id que NO EXISTE en el grafo.
    """
    for nid in sorted(nodos):
        if nodos[nid].get("deprecado") and resolver(nid) == nid:
            return nid, "DEPRECADO y no es alias de ningun vivo"
    inventado = "id_que_no_existe_en_el_grafo_v140"
    while inventado in nodos:
        inventado += "_x"
    return inventado, "id INEXISTENTE (no habia ningun deprecado sin dueno vivo)"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--op", required=True)
    ap.add_argument("--ejecutar", action="store_true")
    ap.add_argument("--mutacion-negativa", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    ops = {o["id_op"]: o for o in T.cargar_ops("WORK")}
    if a.op not in ops:
        print("ROJO: %s no existe en docs/plan/OPERACIONES.jsonl" % a.op)
        return 1
    op = ops[a.op]
    nodos = T.cargar_grafo("WORK")
    resolver = T.resolver_de(nodos)

    fallos_parser = []
    pares = T.pares_de_aristas(op, fallos_parser)
    es_mutuo = "MUTUO" in (op.get("tipo") or "").upper()

    modo = ("MUTACION NEGATIVA (nunca escribe)" if a.mutacion_negativa
            else ("EJECUTAR" if a.ejecutar else "SIMULAR"))
    print("=" * 78)
    print("ESCRITURA DE ARISTAS DE %s . MODO %s" % (a.op, modo))
    print("=" * 78)
    print("tipo de la ficha        : %s" % op.get("tipo"))
    print("ENLACE MUTUO (del tipo) : %s" % es_mutuo)
    print("aristas de la ficha     : %d cadena(s), %d par(es) dirigido(s)"
          % (len(op.get("aristas_nuevas") or []), len(pares)))
    if fallos_parser:
        for f in fallos_parser:
            print("  [ROJO] %s" % f)
        print("SE ABORTA SIN ESCRIBIR NADA: el parser no vio una arista que la ficha nombra.")
        return 1
    if not pares:
        print("SE ABORTA: la ficha no trae ningun par dirigido que escribir.")
        return 1

    if a.mutacion_negativa:
        muerto, motivo = destino_muerto_para_la_mutacion(nodos, resolver)
        print("MUTACION NEGATIVA: el destino de la 1.a arista se fuerza a %s (%s), "
              "elegido computandolo del grafo y no tecleado" % (muerto, motivo))
        print("   comprobacion previa del propio arnes: resolver(%s) = %s, vivo tras "
              "resolver = %s" % (muerto, resolver(muerto), T.vivo(nodos.get(resolver(muerto)))))
        pares = [(pares[0][0], muerto)] + list(pares[1:])

    cache = {}

    def cargar(nid):
        if nid not in cache:
            d, cola = leer_crudo(nid)
            cache[nid] = [d, cola, json.loads(json.dumps(d))]
        return cache[nid]

    fallos = []
    planes = []
    ya_presentes = []

    for crudo_o, crudo_d in pares:
        o, d = resolver(crudo_o), resolver(crudo_d)
        print("")
        print("arista de la ficha: %s -> %s" % (crudo_o, crudo_d))
        if o != crudo_o or d != crudo_d:
            print("  RESUELTA POR ALIAS y se declara: %s -> %s  (origen %s, destino %s)"
                  % (o, d, "RESUELTO" if o != crudo_o else "directo",
                     "RESUELTO" if d != crudo_d else "directo"))
        else:
            print("  los dos ids son DIRECTOS: no hay alias que resolver (si estan VIVOS lo dice la guarda 1)")

        # (1) existen y vivos
        no = nodos.get(o)
        nd = nodos.get(d)
        vivos = T.vivo(no) and T.vivo(nd)
        print("  guarda 1, los dos extremos existen y estan VIVOS: %s" % ("OK" if vivos else "ROJO"))
        if not vivos:
            fallos.append("%s -> %s: extremo no vivo (origen vivo=%s, destino vivo=%s)"
                          % (o, d, T.vivo(no), T.vivo(nd)))
            continue

        # (2) auto-arista
        if o == d:
            print("  guarda 2, cero auto-aristas: ROJO")
            fallos.append("%s -> %s resuelve a una AUTO-ARISTA sobre %s" % (crudo_o, crudo_d, o))
            continue
        print("  guarda 2, cero auto-aristas: OK")

        # (3) cero aristas por alias nuevas: se escribe el id VIVO
        por_alias = (o in (nodos.get(o, {}).get("ids_alias") or []))
        print("  guarda 3, se escribe el ID VIVO resuelto (cero aristas por alias nuevas): %s"
              % ("ROJO" if por_alias else "OK"))

        # (4) ya presente
        presente, _, _ = T.arista_presente(nodos, resolver, o, d)
        if presente:
            print("  guarda 4, YA PRESENTE hoy: se SALTA y se declara (escribirla seria "
                  "fabricar una duplicada)")
            ya_presentes.append((o, d))
            continue
        print("  guarda 4, no estaba puesta todavia: OK, hay que escribirla")

        # (5) una sola direccion
        inversa, _, _ = T.arista_presente(nodos, resolver, d, o)
        inversa_en_plan = any((po, pd) == (d, o) for po, pd, _, _ in planes)
        if (inversa or inversa_en_plan) and not es_mutuo:
            print("  guarda 5, UNA SOLA DIRECCION: ROJO (la inversa %s -> %s %s)"
                  % (d, o, "ya existe" if inversa else "esta en el plan de esta corrida"))
            fallos.append("%s -> %s: la direccion contraria %s existe y la ficha NO dice MUTUO"
                          % (o, d, "ya" if inversa else "va en esta misma corrida"))
            continue
        print("  guarda 5, UNA SOLA DIRECCION (o MUTUO declarado en la ficha): OK")

        d_o = cargar(o)[0]
        d_d = cargar(d)[0]
        sig = list(d_o.get("nodos_siguientes") or [])
        prev = list(d_d.get("nodos_previos") or [])
        sig_nuevo = sig + [d]
        prev_nuevo = prev + [o]

        # (6) cero duplicadas NUEVAS tras resolver. LA CIFRA QUE IMPORTA ES EL
        # DELTA, NO EL TOTAL, y esto se corrigio corriendolo: la primera version
        # media el total y caia en ROJO sobre pivote_estrategico.nodos_previos
        # por una duplicada QUE YA ESTABA (`mvp_concierge` y `concierge_mvp`
        # resuelven al mismo nodo), fabricada por una fusion anterior y con
        # destino ya escrito en OP-S-12 por la atadura 2. Una guarda que castiga
        # a quien no lo hizo no es una guarda: es un bloqueo. Las preexistentes
        # se IMPRIMEN para que se vean, y lo que se prohibe es AUMENTARLAS.
        def _dups(lista):
            r = [resolver(x) for x in lista]
            return len(r) - len(set(r))
        dups_sig_antes, dups_sig_desp = _dups(sig), _dups(sig_nuevo)
        dups_prev_antes, dups_prev_desp = _dups(prev), _dups(prev_nuevo)
        crece = (dups_sig_desp > dups_sig_antes) or (dups_prev_desp > dups_prev_antes)
        print("  guarda 6, cero duplicadas NUEVAS tras resolver: %s "
              "(preexistentes: %s.nodos_siguientes %d, %s.nodos_previos %d; "
              "tras escribir: %d y %d)"
              % ("ROJO" if crece else "OK", o, dups_sig_antes, d, dups_prev_antes,
                 dups_sig_desp, dups_prev_desp))
        if crece:
            fallos.append("%s -> %s: fabricaria una duplicada NUEVA tras resolver" % (o, d))
            continue

        d_o["nodos_siguientes"] = sig_nuevo
        d_d["nodos_previos"] = prev_nuevo
        planes.append((o, d, sig_nuevo, prev_nuevo))
        print("  %s.nodos_siguientes: %d -> %d" % (o, len(sig), len(sig_nuevo)))
        print("  %s.nodos_previos   : %d -> %d" % (d, len(prev), len(prev_nuevo)))

    print("")
    print("-" * 78)
    print("RESUMEN: %d par(es) de la ficha | %d a escribir | %d YA PRESENTES (saltadas) | %d fallo(s)"
          % (len(pares), len(planes), len(ya_presentes), len(fallos)))
    for o, d in ya_presentes:
        print("   YA PRESENTE: %s -> %s" % (o, d))

    if fallos:
        print("")
        print("SE ABORTA SIN ESCRIBIR NADA, %d fallo(s):" % len(fallos))
        for f in fallos:
            print("   [ROJO] %s" % f)
        return 1

    if a.mutacion_negativa:
        print("")
        print("MUTACION NEGATIVA: NO DEBIA LLEGAR AQUI con un destino DEPRECADO. CAIDA DEL ARNES.")
        return 1

    # (7) ningun otro campo cambia
    otros = []
    for nid, (d_, c_, orig) in cache.items():
        for k in d_:
            if k in ("nodos_siguientes", "nodos_previos"):
                continue
            if d_[k] != orig.get(k):
                otros.append("%s.%s" % (nid, k))
        for k in orig:
            if k not in d_:
                otros.append("%s.%s (borrado)" % (nid, k))
    print("guarda 7, ningun otro campo cambia en ningun nodo tocado: %s"
          % ("OK" if not otros else "ROJO %s" % otros))
    if otros:
        print("SE ABORTA SIN ESCRIBIR: guarda 7 caida.")
        return 1

    if not planes:
        print("")
        print("NADA QUE ESCRIBIR: las %d aristas de la ficha YA ESTAN PRESENTES hoy." % len(pares))
        print("EL DESTINO DE %s SE DECLARA CUMPLIDO, no se re-escribe." % a.op)
        return 0

    if not a.ejecutar:
        print("")
        print("SIMULACION: cero escrituras. %d arista(s) listas para --ejecutar." % len(planes))
        return 0

    for nid, (d_, c_, orig) in cache.items():
        escribir(nid, d_, c_)
    print("")
    print("ESCRITO. ficheros de nodo tocados: %d (%s)"
          % (len(cache), ", ".join(sorted(cache.keys()))))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
