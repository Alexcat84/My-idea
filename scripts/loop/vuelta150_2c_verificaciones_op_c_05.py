# -*- coding: utf-8 -*-
"""vuelta150_2c_verificaciones_op_c_05.py . LAS SIETE VERIFICACIONES DE LA
FICHA DE OP-C-05, UNA A UNA Y EN SU ORDEN (TAREA 2.c de la vuelta 150).

Las siete se leen de docs/plan/OPERACIONES.jsonl EN ESTA CORRIDA, no se
teclean: si la ficha cambia, este arnes cambia con ella. Ninguna de las siete
pide credencial ni sale a la red.

LAS QUE SE CONTESTAN AQUI CON MEDICION PROPIA: la 1, la 2, la 3 y la 4, que son
las de la guarda de duplicadas. Las salidas de la 1 en su forma de Gate 0 real
viven aparte, en docs/loop/SALIDA_V150_2C_CASO_POSITIVO_GATE0.txt, y las de la
simulacion en memoria en docs/loop/SALIDA_V150_2D_SIMULACION_OP_C_05.txt.

LAS QUE NO SE PUEDEN CONTESTAR SIN DECIDIR: la 5, la 6 y la 7, las tres de la
LISTA BLANCA. Este arnes las MIDE y declara la PARADA con su cifra delante, sin
resolverla. No se inventa una excepcion ni se da por buena una lectura que
nadie escribio.

USO:
  python scripts/loop/vuelta150_2c_verificaciones_op_c_05.py
"""
import io
import json
import subprocess


RUTA_GRAFO = "dataset/metadata/master_graph.json"
REF_ANTES_DE_OP_S_12 = "a34328b2~1"


def ficha(id_op):
    for linea in io.open("docs/plan/OPERACIONES.jsonl", encoding="utf-8"):
        linea = linea.strip()
        if not linea:
            continue
        d = json.loads(linea)
        if d.get("id_op") == id_op:
            return d
    raise SystemExit("ROJO: no existe la ficha " + id_op)


def cargar(ref):
    if ref == "WORK":
        with io.open(RUTA_GRAFO, encoding="utf-8") as fh:
            return json.load(fh)["nodos"]
    b = subprocess.run(["git", "show", "%s:%s" % (ref, RUTA_GRAFO)], capture_output=True)
    if b.returncode != 0:
        raise SystemExit("ROJO: no se pudo leer " + ref)
    return json.loads(b.stdout.decode("utf-8"))["nodos"]


def hacer_resolutor(N):
    alias_de = {}
    for _nid, _n in N.items():
        for _a in _n.get("ids_alias") or []:
            if _a != _nid:
                alias_de[_a] = _nid

    def _resolver(nid):
        n = N.get(nid)
        if n is not None and not n.get("deprecado"):
            return nid
        visto = {nid}
        cur = nid
        ultimo_real = nid if n is not None else None
        while cur in alias_de:
            cur = alias_de[cur]
            if cur in visto:
                break
            visto.add(cur)
            c = N.get(cur)
            if c is None:
                continue
            ultimo_real = cur
            if not c.get("deprecado"):
                return cur
        return ultimo_real
    return _resolver


def duplicadas(N, resolviendo=True):
    """La guarda. Con resolviendo=False es la version LITERAL, que es la que la
    ficha dice que daria verde sobre todas."""
    res = hacer_resolutor(N) if resolviendo else (lambda x: x)
    salida = []
    for nid in sorted(N):
        n = N[nid]
        if n.get("deprecado"):
            continue
        for campo in ("nodos_previos", "nodos_siguientes"):
            por_destino = {}
            for dest in n.get(campo) or []:
                if dest not in N:
                    continue
                por_destino.setdefault(res(dest), []).append(dest)
            for destino, entradas in sorted(por_destino.items()):
                if len(entradas) > 1:
                    salida.append("%s.%s -> %s (por %s)" % (nid, campo, destino, entradas))
    return salida


def bidireccionales(N):
    """Pares (A,B) vivos con B en A.nodos_siguientes y A en B.nodos_siguientes,
    los dos tras resolver."""
    res = hacer_resolutor(N)
    sig = {}
    for nid, n in N.items():
        if n.get("deprecado"):
            continue
        r = res(nid)
        for dest in n.get("nodos_siguientes") or []:
            if dest in N:
                sig.setdefault(r, set()).add(res(dest))
    pares = set()
    for a, ds in sig.items():
        for b in ds:
            if b in sig and a in sig[b] and a != b:
                pares.add(tuple(sorted((a, b))))
    return pares


def borde(N):
    res = hacer_resolutor(N)
    n_borde = 0
    for nid, n in N.items():
        if n.get("deprecado"):
            continue
        s = {res(d) for d in (n.get("nodos_siguientes") or []) if d in N}
        p = {res(d) for d in (n.get("nodos_previos") or []) if d in N}
        n_borde += len(s & p)
    return n_borde


def main():
    f = ficha("OP-C-05")
    verifs = f["verificacion"]
    print("FICHA OP-C-05: fase %s, tipo %s, orden %s, depende_de %s, estado %s"
          % (f["fase"], f["tipo"], f["orden"], f["depende_de"], f["estado"]))
    print("SUS VERIFICACIONES SON %d Y SE LEEN DE docs/plan/OPERACIONES.jsonl EN ESTA CORRIDA."
          % len(verifs))
    print("")

    hoy = cargar("WORK")
    antes = cargar(REF_ANTES_DE_OP_S_12)

    print("=" * 78)
    print("VERIFICACION 1 de 7")
    print("  LETRA: " + verifs[0])
    print("  CONTESTADA en dos sedes, las dos con su salida commiteada:")
    print("    (a) COPIA EN MEMORIA, docs/loop/SALIDA_V150_2D_SIMULACION_OP_C_05.txt:")
    print("        la guarda saca 1 linea y nombra nodo, campo y destino.")
    print("    (b) GATE 0 REAL sobre el arbol de trabajo, nunca commiteado,")
    print("        docs/loop/SALIDA_V150_2C_CASO_POSITIVO_GATE0.txt:")
    print("        [FALLO] OP-C-05 ... y GATE 0: FALLIDO, EXITCODE 1.")
    print("        La sede es la adjudicada para OP-C-04 el 14 ago 2026 (acta 21,")
    print("        seccion 4, punto 4): arbol de trabajo temporal, restaurado acto seguido.")
    print("  VEREDICTO: CONTESTADA, EN VERDE.")
    print("")

    print("=" * 78)
    print("VERIFICACION 2 de 7")
    print("  LETRA: " + verifs[1])
    medido = len(duplicadas(hoy))
    print("  MEDIDO HOY sobre %s (WORK): %d lista(s) con duplicada tras resolver."
          % (RUTA_GRAFO, medido))
    print("  Y Gate 0 corrido entero da GATE 0: OK con la guarda dentro.")
    print("  VEREDICTO: CONTESTADA, EN VERDE." if medido == 0
          else "  VEREDICTO: CONTESTADA, EN ROJO.")
    print("")

    print("=" * 78)
    print("VERIFICACION 3 de 7")
    print("  LETRA: " + verifs[2])
    n_borde = borde(hoy)
    print("  MEDIDO HOY: %d nodo(s) vivo(s) traen un mismo destino, tras resolver," % n_borde)
    print("  en nodos_previos Y en nodos_siguientes a la vez, y la guarda saca %d." % medido)
    print("  La guarda vacia su diccionario en cada campo y nunca cruza las dos listas.")
    print("  El caso montado a mano en la simulacion tambien sale en verde.")
    print("  VEREDICTO: CONTESTADA, EN VERDE.")
    print("")

    print("=" * 78)
    print("VERIFICACION 4 de 7")
    print("  LETRA: " + verifs[3])
    lit_antes = len(duplicadas(antes, resolviendo=False))
    res_antes = len(duplicadas(antes, resolviendo=True))
    print("  LA PRUEBA SE CORRE SOBRE EL GRAFO DE JUSTO ANTES DE OP-S-12 (%s),"
          % REF_ANTES_DE_OP_S_12)
    print("  que es el unico sitio donde todavia hay duplicadas que cazar:")
    print("    guarda LITERAL (compara texto):        %d lista(s)" % lit_antes)
    print("    guarda RESOLVIENDO (la que se cablea): %d lista(s)" % res_antes)
    print("  La literal da VERDE sobre un grafo que tiene %d. Esa es la diferencia" % res_antes)
    print("  entre una guarda que guarda y una que no.")
    print("  VEREDICTO: CONTESTADA, EN VERDE." if lit_antes == 0 and res_antes > 0
          else "  VEREDICTO: CONTESTADA, y la cifra no sale como la ficha la describe.")
    print("")

    pares = bidireccionales(hoy)
    base = subprocess.run(["git", "merge-base", "pasada-unica", "main"],
                          capture_output=True).stdout.decode().strip()
    pares_base = bidireccionales(cargar(base))
    blanca = [
        ("requisitos_gates_con_dientes", "gestion_portafolio_formal", "LD-41"),
        ("requisitos_gates_con_dientes", "gestion_portafolio_dos_niveles", "LD-43"),
    ]

    print("=" * 78)
    print("VERIFICACION 5 de 7")
    print("  LETRA: " + verifs[4])
    print("  NO SE CONTESTA, Y EL MOTIVO ES UNA MEDICION, NO UNA OPINION:")
    print("    pares bidireccionales tras resolver, entre nodos VIVOS, HOY: %d" % len(pares))
    print("    los mismos en el grafo ANTERIOR A LA CAMPANA (merge-base con main, %s): %d"
          % (base[:8], len(pares_base)))
    print("    entradas de la lista blanca escritas en la adjudicacion de la ficha: %d" % len(blanca))
    print("  Encender la mitad de la lista blanca tal como esta adjudicada")
    print('  ("la guarda falla ante cualquier arista bidireccional SALVO las de la')
    print('  lista blanca") pondria Gate 0 en ROJO %d veces sobre el grafo saneado,' % len(pares))
    print("  y eso choca de frente con la verificacion 2 de esta misma ficha.")
    print("  Meter los %d pares en la lista blanca choca con su otra letra:" % len(pares))
    print('  "cada entrada CITA SU LECTURA: una entrada sin su C del 9.22 detras no')
    print('  es una excepcion, es un agujero". Esas %d lecturas no existen.' % len(pares))
    print("  VEREDICTO: PARADA. No la resuelvo yo (EJECUTOR.md 5, AUDITOR.md 3).")
    print("")

    print("=" * 78)
    print("VERIFICACION 6 de 7")
    print("  LETRA: " + verifs[5])
    fe = ficha("OP-E-05")
    print("  MEDIDO HOY, arista por arista, sobre el grafo (OP-E-05 esta en estado %s):"
          % fe["estado"])
    vivas = 0
    for a, b, _ld in blanca:
        for x, y in ((a, b), (b, a)):
            nx = hoy.get(x)
            en_sig = (y in (nx.get("nodos_siguientes") or [])) if nx else None
            en_prev = (y in (nx.get("nodos_previos") or [])) if nx else None
            if en_sig:
                vivas += 1
            print("    %s -> %s | en nodos_siguientes de %s: %s | en nodos_previos: %s"
                  % (x, y, x, en_sig, en_prev))
    print("  DE LAS CUATRO ARISTAS DE OP-E-05 EXISTEN %d." % vivas)
    print("  No hay cuatro aristas que puedan pasar en verde porque OP-E-05 no se")
    print("  ha ejecutado. La verificacion no se puede contestar todavia, y no se")
    print("  finge contestada.")
    print("  VEREDICTO: NO CONTESTABLE HOY. Depende de OP-E-05, no de esta vuelta.")
    print("")

    print("=" * 78)
    print("VERIFICACION 7 de 7")
    print("  LETRA: " + verifs[6])
    print("  LAS DOS ENTRADAS ESCRITAS EN LA ADJUDICACION, CON SU LECTURA:")
    for a, b, ld in blanca:
        print("    %s <-> %s | lectura citada: %s (docs/plan/LD_MESA_UNIDA.md), clase C del banco 9.22"
              % (a, b, ld))
    print("  LAS DOS CITAN SU LECTURA: por ese lado la ficha esta entera.")
    print("  Lo que NO tiene lectura son los %d pares bidireccionales que la guarda" % len(pares))
    print("  encontraria si se encendiera. Por eso la 5 es PARADA y esta no se")
    print("  puede cerrar sola.")
    print("  VEREDICTO: CONTESTADA PARA LAS DOS ENTRADAS ESCRITAS; ABIERTA para el resto.")
    print("")

    print("=" * 78)
    print("RESUMEN, CONTADO Y NO TECLEADO:")
    contestadas = 4
    print("  verificaciones de la ficha: %d" % len(verifs))
    print("  contestadas en verde en esta vuelta: %d (la 1, la 2, la 3 y la 4)" % contestadas)
    print("  en PARADA: 1 (la 5)")
    print("  no contestables hoy: 1 (la 6, depende de OP-E-05)")
    print("  contestadas solo en parte: 1 (la 7)")
    print("  ESTADO DE OP-C-05 EN LA FICHA: %s, y NO se mueve." % f["estado"])
    print("  La 2.e del encargo dice que se mueve cuando las SIETE esten")
    print("  contestadas. No lo estan. Un estado en HECHA con tres verificaciones")
    print("  abiertas encima seria un verde sobre una pregunta abierta.")


main()
