# -*- coding: utf-8 -*-
r"""verificar_aristas_vivas.py . LA GUARDA NUEVA DE ARISTAS VIVO-VIVO
(TAREA 1.h de la vuelta 126, encargo docs/loop/PROMPT_SIGUIENTE.md).

POR QUE NACE. La vuelta 125 fusiono OP-S-09 y corto, sin declararlo, una
arista entre dos nodos vivos: dia_cero_defectos_2 -> eliminacion_causas_error_4
existia como dia_cero_defectos_3 -> eliminacion_causas_error ANTES de la
fusion, y la pasada de redireccion de fundir_por_plan.py solo mira nodos
VIVOS al reescribir listas; cuando el citante es OTRO ABSORBIDO de la misma
operacion, esa pasada ya no lo ve (acta de la vuelta 125, seccion 4.1).
Ningun instrumento de la casa comprobaba esto: Gate 0 valida estructura,
el conteo de aristas cuenta totales, el desfase del calibrado compara
contra una foto vieja de 468 filas. Faltaba una guarda que proyectara el
grafo VIVO-VIVO de un ANTES contra el de un DESPUES y dijera, con nombre y
apellido, que se perdio.

QUE HACE. Construye, en cada lado (--antes <ref> y --despues <ref o WORK>),
el conjunto de aristas VIVO-VIVO: un nodo no deprecado que cita a otro no
deprecado, mirando las DOS vistas (nodos_siguientes del origen Y
nodos_previos del destino) y normalizando cada arista a un par ordenado
(origen, destino), deduplicado (si las dos vistas registran la misma
arista, cuenta una vez).

PROYECTA el conjunto de "antes" por el resolutor de "despues": cada
extremo se resuelve con el mapa de alias vivo de DESPUES (igual que
resolver_de() en verificar_fusion_ops09.py, pero sobre TODO el grafo, no
solo los pares de una operacion). Se descartan los pares cuyo extremo
resuelto ya no existe o sigue deprecado en despues, y las auto-aristas que
la resolucion pueda producir (los dos extremos resuelven al mismo nodo).

Imprime, en este orden: aristas vivo-vivo ANTES proyectadas, aristas
vivo-vivo DESPUES, PERDIDAS (en antes-proyectado y no en despues), NUEVAS
(en despues y no en antes-proyectado); y lista los pares de las dos
ultimas. ROJO EXIT 1 si PERDIDAS no es cero. VERDE EXIT 0 si lo es.

USO:
  python scripts/loop/verificar_aristas_vivas.py --antes c9ac2fb8 --despues WORK
  python scripts/loop/verificar_aristas_vivas.py --antes <refA> --despues <refB>

CASO POSITIVO (mutacion, en memoria, no toca disco, --autoprueba): sobre
una copia de WORK se borra, de las dos vistas, una arista vivo-vivo real
(la primera que se halle); "antes" es el WORK real y "despues" es la copia
mutada. PERDIDAS tiene que nombrar exactamente esa arista.
"""
import argparse
import json
import os
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA_GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")


def cargar(ref):
    if ref == "WORK":
        with open(RUTA_GRAFO, encoding="utf-8") as f:
            return json.load(f)["nodos"]
    r = subprocess.run(["git", "show", "%s:dataset/metadata/master_graph.json" % ref],
                       cwd=RAIZ, capture_output=True)
    if r.returncode != 0:
        raise SystemExit("ROJO (arnes): no se pudo leer dataset/metadata/master_graph.json en %s" % ref)
    return json.loads(r.stdout.decode("utf-8"))["nodos"]


def vivo(n):
    return n is not None and not n.get("deprecado")


def aristas_vivo_vivo(nodos):
    aristas = set()
    for nid, n in nodos.items():
        if not vivo(n):
            continue
        for d in (n.get("nodos_siguientes") or []):
            nd = nodos.get(d)
            if vivo(nd):
                aristas.add((nid, d))
        for o in (n.get("nodos_previos") or []):
            no = nodos.get(o)
            if vivo(no):
                aristas.add((o, nid))
    return aristas


def resolver_de(nodos):
    alias = {}
    for nid, n in nodos.items():
        if n.get("deprecado"):
            continue
        for x in (n.get("ids_alias") or []):
            alias[x] = nid

    def resolver(x):
        visto = set()
        while x in alias and x not in visto:
            visto.add(x)
            x = alias[x]
        return x
    return resolver


def proyectar(aristas_antes, nodos_despues, resolver):
    proyectadas = set()
    for o, d in aristas_antes:
        o2, d2 = resolver(o), resolver(d)
        if o2 == d2:
            continue
        if not vivo(nodos_despues.get(o2)):
            continue
        if not vivo(nodos_despues.get(d2)):
            continue
        proyectadas.add((o2, d2))
    return proyectadas


def medir(nodos_antes, nodos_despues):
    aristas_antes = aristas_vivo_vivo(nodos_antes)
    aristas_despues = aristas_vivo_vivo(nodos_despues)
    resolver = resolver_de(nodos_despues)
    proyectadas = proyectar(aristas_antes, nodos_despues, resolver)
    perdidas = proyectadas - aristas_despues
    nuevas = aristas_despues - proyectadas
    return proyectadas, aristas_despues, perdidas, nuevas


def imprimir(proyectadas, aristas_despues, perdidas, nuevas, antes_nombre, despues_nombre):
    print("ANTES (%s) proyectadas: %d" % (antes_nombre, len(proyectadas)))
    print("DESPUES (%s): %d" % (despues_nombre, len(aristas_despues)))
    print("PERDIDAS: %d" % len(perdidas))
    for o, d in sorted(perdidas):
        print("  %s -> %s" % (o, d))
    print("NUEVAS: %d" % len(nuevas))
    for o, d in sorted(nuevas):
        print("  %s -> %s" % (o, d))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--antes")
    ap.add_argument("--despues")
    ap.add_argument("--autoprueba", action="store_true",
                     help="corre el caso positivo por mutacion (en memoria) y termina")
    a = ap.parse_args()

    if a.autoprueba:
        nodos_work = cargar("WORK")
        aristas = aristas_vivo_vivo(nodos_work)
        if not aristas:
            print("CAIDA DE LA ARNES: WORK no tiene ninguna arista vivo-vivo que mutar.")
            return 1
        origen, destino = sorted(aristas)[0]
        clon = {nid: dict(n) for nid, n in nodos_work.items()}
        clon[origen]["nodos_siguientes"] = [x for x in (clon[origen].get("nodos_siguientes") or []) if x != destino]
        clon[destino]["nodos_previos"] = [x for x in (clon[destino].get("nodos_previos") or []) if x != origen]
        proyectadas, aristas_despues, perdidas, nuevas = medir(nodos_work, clon)
        if (origen, destino) not in perdidas:
            print("CAIDA DE LA AUTOPRUEBA: borrar %s -> %s de las dos vistas no aparecio en PERDIDAS" % (origen, destino))
            print("PERDIDAS obtenidas: %r" % sorted(perdidas))
            return 1
        print("AUTOPRUEBA VERIFICADA: ROJO nombrando %s -> %s tras borrarla de las dos vistas en memoria (WORK mutado)"
              % (origen, destino))
        imprimir(proyectadas, aristas_despues, perdidas, nuevas, "WORK", "WORK mutado")
        return 0

    if not a.antes or not a.despues:
        print("ROJO (arnes): --antes y --despues son obligatorios (o usa --autoprueba)")
        return 1

    nodos_antes = cargar(a.antes)
    nodos_despues = cargar(a.despues)
    proyectadas, aristas_despues, perdidas, nuevas = medir(nodos_antes, nodos_despues)
    imprimir(proyectadas, aristas_despues, perdidas, nuevas, a.antes, a.despues)

    if perdidas:
        print("ROJO EXIT 1: %d arista(s) vivo-vivo perdida(s) entre %s y %s." % (len(perdidas), a.antes, a.despues))
        return 1
    print("VERDE EXIT 0: cero aristas vivo-vivo perdidas entre %s y %s." % (a.antes, a.despues))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
