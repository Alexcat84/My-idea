# -*- coding: utf-8 -*-
"""vuelta150_2d_simular_op_c_05.py . SIMULACION PREVIA DE OP-C-05 SOBRE COPIA
EN MEMORIA, mas su CASO ROJO POR MUTACION SOBRE VARIABLE COMPUTADA, mas la
comprobacion de que dataset/ queda IDENTICO antes y despues (TAREA 2.d de la
vuelta 150).

NO TOCA UN SOLO FICHERO. Carga el grafo, se hace una copia en memoria con
copy.deepcopy, inyecta el estado malo EN LA COPIA y corre sobre ella la MISMA
logica que scripts/run_phase1.py cablea en Gate 0. El arnes mide el sha256 de
dataset/metadata/master_graph.json y de dataset/nodos/ al empezar y al acabar y
LO COMPARA: si difiere, sale en rojo.

EL CASO ROJO ES POR MUTACION SOBRE VARIABLE COMPUTADA (EJECUTOR.md 1, "EL CASO
ROJO SE PRUEBA POR MUTACION"): la variable del veredicto es `medido`, que sale
de contar la salida de la guarda, nunca un literal comparado consigo mismo. La
mutacion cambia EL VALOR ESPERADO y comprueba que el assert CAE.

USO:
  python scripts/loop/vuelta150_2d_simular_op_c_05.py
"""
import copy
import hashlib
import json
import os

RUTA_GRAFO = "dataset/metadata/master_graph.json"
RUTA_NODOS = "dataset/nodos"


def sha_dir():
    h = hashlib.sha256()
    for nombre in sorted(os.listdir(RUTA_NODOS)):
        with open(os.path.join(RUTA_NODOS, nombre), "rb") as fh:
            h.update(nombre.encode("utf-8"))
            h.update(fh.read())
    return h.hexdigest()


def sha_fichero(ruta):
    with open(ruta, "rb") as fh:
        return hashlib.sha256(fh.read().replace(b"\r\n", b"\n")).hexdigest()


def hacer_resolutor(nodos_todos):
    """Copia fiel del _resolver de scripts/run_phase1.py, que a su vez es copia
    fiel de resolverId (web/lib/engine/graph.ts)."""
    alias_de = {}
    for _nid, _n in nodos_todos.items():
        for _a in _n.get("ids_alias") or []:
            if _a != _nid:
                alias_de[_a] = _nid

    def _resolver(nid):
        n = nodos_todos.get(nid)
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
            c = nodos_todos.get(cur)
            if c is None:
                continue
            ultimo_real = cur
            if not c.get("deprecado"):
                return cur
        return ultimo_real
    return _resolver


def guarda(nodos_todos):
    """LA MISMA LOGICA que scripts/run_phase1.py cablea en Gate 0, escrita una
    sola vez aqui para poder correrla sobre una copia en memoria."""
    _resolver = hacer_resolutor(nodos_todos)
    activos = {k: v for k, v in nodos_todos.items() if not v.get("deprecado")}
    salida = []
    for nid in sorted(activos):
        n = activos[nid]
        for campo in ("nodos_previos", "nodos_siguientes"):
            por_destino = {}
            for dest in n.get(campo) or []:
                if dest not in nodos_todos:
                    continue
                por_destino.setdefault(_resolver(dest), []).append(dest)
            for destino, entradas in sorted(por_destino.items()):
                if len(entradas) > 1:
                    salida.append("%s.%s -> %s (por %s)" % (nid, campo, destino, entradas))
    return salida


def buscar_victima(N):
    """Un nodo VIVO con una arista a un destino VIVO que tenga al menos un
    alias vivo en el grafo. Devuelve (nodo, campo, destino, alias_del_destino)."""
    for nid in sorted(N):
        n = N[nid]
        if n.get("deprecado"):
            continue
        for campo in ("nodos_siguientes", "nodos_previos"):
            for dest in n.get(campo) or []:
                d = N.get(dest)
                if d is None or d.get("deprecado"):
                    continue
                for a in d.get("ids_alias") or []:
                    if a != dest and a in N:
                        return nid, campo, dest, a
    return None


def main():
    sha_grafo_antes = sha_fichero(RUTA_GRAFO)
    sha_nodos_antes = sha_dir()
    print("dataset/ ANTES: master_graph sha256=%s | dataset/nodos sha256=%s"
          % (sha_grafo_antes[:12], sha_nodos_antes[:12]))

    with open(RUTA_GRAFO, encoding="utf-8") as fh:
        N = json.load(fh)["nodos"]

    print("")
    print("CASO NEGATIVO (verificacion 2 de la ficha): el grafo saneado por OP-S-12,")
    print("tal como esta hoy, sobre COPIA EN MEMORIA.")
    limpio = copy.deepcopy(N)
    medido_limpio = len(guarda(limpio))
    esperado_limpio = 0
    print("  medido (COMPUTADO por la guarda) = %d | esperado = %d"
          % (medido_limpio, esperado_limpio))
    assert medido_limpio == esperado_limpio, "el grafo de hoy no pasa en verde"
    print("  VERDE")

    v = buscar_victima(N)
    assert v is not None, "no hay victima con alias vivo: la simulacion no se puede montar"
    nodo, campo, destino, alias = v

    print("")
    print("CASO POSITIVO (verificacion 1 de la ficha): en la COPIA se mete a mano")
    print("[destino, alias_de_destino] y la guarda TIENE que fallar nombrando")
    print("nodo, campo y destino.")
    print("  victima: %s.%s ya trae %s; se le anade su alias %s" % (nodo, campo, destino, alias))
    sucio = copy.deepcopy(N)
    sucio[nodo][campo] = list(sucio[nodo][campo]) + [alias]
    salida_sucia = guarda(sucio)
    medido_sucio = len(salida_sucia)
    esperado_sucio = 1
    print("  medido (COMPUTADO por la guarda) = %d | esperado = %d"
          % (medido_sucio, esperado_sucio))
    assert medido_sucio == esperado_sucio, "la guarda NO caza la duplicada inyectada"
    linea = salida_sucia[0]
    print("  linea de la guarda: %s" % linea)
    assert nodo in linea and campo in linea and destino in linea, \
        "la guarda no nombra nodo, campo y destino"
    print("  NOMBRA NODO, CAMPO Y DESTINO: los tres estan en la linea")
    print("  ROJO como se pedia")

    print("")
    print("CASO DE BORDE (verificacion 3 de la ficha): el mismo destino en")
    print("nodos_previos Y en nodos_siguientes NO debe fallar.")
    borde = copy.deepcopy(N)
    otro = None
    for nid in sorted(borde):
        n = borde[nid]
        if n.get("deprecado"):
            continue
        s = [d for d in (n.get("nodos_siguientes") or [])
             if d in borde and not borde[d].get("deprecado")]
        if s and s[0] not in (n.get("nodos_previos") or []):
            otro = (nid, s[0])
            break
    assert otro is not None, "no hay nodo donde montar el caso de borde"
    nid_b, dest_b = otro
    borde[nid_b]["nodos_previos"] = list(borde[nid_b].get("nodos_previos") or []) + [dest_b]
    medido_borde = len(guarda(borde))
    esperado_borde = 0
    print("  montado: %s tiene ahora %s en nodos_siguientes Y en nodos_previos"
          % (nid_b, dest_b))
    print("  medido (COMPUTADO por la guarda) = %d | esperado = %d"
          % (medido_borde, esperado_borde))
    assert medido_borde == esperado_borde, "el caso de borde dispara la guarda, y no debe"
    print("  VERDE: la ida y vuelta no es una duplicada")

    print("")
    print("CASO ROJO POR MUTACION, SOBRE VARIABLE COMPUTADA (EJECUTOR.md 1).")
    print("Se cambia EL VALOR ESPERADO de cada uno de los tres asserts de arriba")
    print("y se comprueba que el caso CAE. `medido` no se toca: sigue saliendo")
    print("de contar la salida de la guarda.")
    caidas = 0
    for etiqueta, medido, esperado_mutado in (
            ("caso negativo", medido_limpio, 1),
            ("caso positivo", medido_sucio, 0),
            ("caso de borde", medido_borde, 1)):
        try:
            assert medido == esperado_mutado
            print("  %s: el assert NO cayo con esperado=%d. LA PRUEBA NO PRUEBA NADA"
                  % (etiqueta, esperado_mutado))
        except AssertionError:
            caidas += 1
            print("  %s: assert %d == %d CAE. El caso muerde."
                  % (etiqueta, medido, esperado_mutado))
    esperado_caidas = 3
    print("  caidas (COMPUTADO) = %d | esperado = %d" % (caidas, esperado_caidas))
    assert caidas == esperado_caidas, "alguna mutacion no cayo"

    sha_grafo_despues = sha_fichero(RUTA_GRAFO)
    sha_nodos_despues = sha_dir()
    print("")
    print("dataset/ DESPUES: master_graph sha256=%s | dataset/nodos sha256=%s"
          % (sha_grafo_despues[:12], sha_nodos_despues[:12]))
    assert sha_grafo_antes == sha_grafo_despues, "master_graph.json CAMBIO"
    assert sha_nodos_antes == sha_nodos_despues, "dataset/nodos CAMBIO"
    print("dataset/ IDENTICO ANTES Y DESPUES: comprobado por el propio arnes.")
    print("")
    print("SIMULACION VERDE.")


main()
