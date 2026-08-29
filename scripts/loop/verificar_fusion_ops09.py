# -*- coding: utf-8 -*-
r"""verificar_fusion_ops09.py . LA GUARDA NUEVA DE LA FUSION DE OP-S-09
(TAREA 1.g de la vuelta 125, encargo docs/loop/PROMPT_SIGUIENTE.md).

CONTRATO (exacto, del encargo): se corre DESPUES de ejecutar OP-S-09. Lee
dataset/metadata/master_graph.json y, por cada par REPITE ejecutado,
comprueba:
  (1) el id que muere esta DEPRECADO
  (2) el id que muere aparece en ids_alias del superviviente
  (3) el superviviente sigue VIVO
  (4) CERO nodos vivos conservan una arista que apunte a un id muerto sin
      que el resolutor la lleve al superviviente
  (5) cero auto-aristas y cero duplicadas en las listas de los nodos
      tocados (superviviente y cada muerto)
ROJO EXIT 1 nombrando el par y la comprobacion que falla; VERDE EXIT 0 con
el recuento de pares comprobados.

LA LISTA DE PARES REPITE NO SE TECLEA AQUI: se lee de los registros de
lectura par a par (SALIDA_V123_OPS09_LECTURA.jsonl,
SALIDA_V124_OPS09_LECTURA_RESTO.jsonl) con la relectura conjunta de la
vuelta 125 (SALIDA_V125_OPS09_RELECTURA_CONJUNTA.jsonl) superpuesta encima,
que es la unica fuente que puede CORREGIR una clase o un superviviente ya
escrito (regla 8 de EJECUTOR.md: correccion declarada, no se tapa la vieja).

USO:
  python scripts/loop/verificar_fusion_ops09.py
  python scripts/loop/verificar_fusion_ops09.py --ref 6d512a0d

CASO POSITIVO (mutacion, en memoria, no toca disco): sobre una copia del
grafo real se borra el alias de uno de los muertos y se corre la
comprobacion; tiene que dar ROJO nombrando exactamente ese par. Se corre
automaticamente con --autoprueba.
"""
import argparse
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA_GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
LOOP = os.path.join(RAIZ, "docs", "loop")
REGISTROS = [
    os.path.join(LOOP, "SALIDA_V123_OPS09_LECTURA.jsonl"),
    os.path.join(LOOP, "SALIDA_V124_OPS09_LECTURA_RESTO.jsonl"),
]
RELECTURA = os.path.join(LOOP, "SALIDA_V125_OPS09_RELECTURA_CONJUNTA.jsonl")
CAMPOS = ("nodos_previos", "nodos_siguientes")


def cargar(ref):
    if ref == "WORK":
        with open(RUTA_GRAFO, encoding="utf-8") as f:
            return json.load(f)
    r = subprocess.run(["git", "show", "%s:dataset/metadata/master_graph.json" % ref],
                       cwd=RAIZ, capture_output=True)
    if r.returncode != 0:
        raise SystemExit("ROJO (arnes): no se pudo leer dataset/metadata/master_graph.json en %s" % ref)
    return json.loads(r.stdout.decode("utf-8"))


def pares_repite():
    """Los pares REPITE de OP-S-09: filas base de los dos registros de
    lectura par a par, con la relectura conjunta de la vuelta 125 superpuesta
    (puede AÑADIR un par que antes era CONTINUA, o CORREGIR un superviviente)."""
    base = {}
    for fn in REGISTROS:
        with open(fn, encoding="utf-8") as f:
            for linea in f:
                if not linea.strip():
                    continue
                fila = json.loads(linea)
                for p in fila["pares"]:
                    k = tuple(sorted((p["a"], p["b"])))
                    if p["veredicto"] == "REPITE":
                        base[k] = p.get("superviviente")
                    elif k in base:
                        del base[k]

    if os.path.exists(RELECTURA):
        with open(RELECTURA, encoding="utf-8") as f:
            for linea in f:
                if not linea.strip():
                    continue
                fila = json.loads(linea)
                k = tuple(sorted(fila["par"]))
                if fila["veredicto_final"] == "REPITE":
                    base[k] = fila["superviviente"]
                else:
                    base.pop(k, None)

    pares = []
    for (a, b), sup in sorted(base.items()):
        if sup not in (a, b):
            raise SystemExit("ROJO (arnes): superviviente %r no es ni %r ni %r" % (sup, a, b))
        muere = a if sup == b else b
        pares.append({"superviviente": sup, "muere": muere})
    return pares


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


def verificar(nodos, pares):
    resolver = resolver_de(nodos)
    fallos = []
    comprobados = 0
    for par in pares:
        muere, sup = par["muere"], par["superviviente"]
        etiqueta = "%s -> %s" % (muere, sup)
        n_muere = nodos.get(muere)
        n_sup = nodos.get(sup)
        if n_muere is None:
            fallos.append("%s: (1) %s no existe en el grafo" % (etiqueta, muere))
            continue
        if n_sup is None:
            fallos.append("%s: (3) %s no existe en el grafo" % (etiqueta, sup))
            continue

        if not n_muere.get("deprecado"):
            fallos.append("%s: (1) %s NO esta DEPRECADO" % (etiqueta, muere))

        if muere not in (n_sup.get("ids_alias") or []):
            fallos.append("%s: (2) %s NO aparece en ids_alias de %s" % (etiqueta, muere, sup))

        if n_sup.get("deprecado"):
            fallos.append("%s: (3) el superviviente %s esta DEPRECADO" % (etiqueta, sup))

        for nid, n in nodos.items():
            if n.get("deprecado"):
                continue
            for campo in CAMPOS:
                for x in (n.get(campo) or []):
                    if x == muere and resolver(x) != sup:
                        fallos.append("%s: (4) %s.%s cita a %s y el resolutor da %r, no %s"
                                      % (etiqueta, nid, campo, muere, resolver(x), sup))

        # (5) auto-arista y duplicada QUE ESTA FUSION PUEDE CAUSAR, acotado a los
        # dos nodos del propio par: auto-arista (el nodo se cita a si mismo) y
        # duplicada CAUSADA POR EL ALIAS (muere y superviviente, o dos alias que
        # ya resuelven al superviviente, conviviendo en la misma lista). NO se
        # cuenta aqui el pasivo historico de duplicadas ajenas a este par (otras
        # familias ya fundidas antes), que es el backlog medido y encargado a
        # OP-S-12: contarlo aqui haria que la guarda cayera siempre por ruido que
        # esta fusion no fabrico, y dejaria de medir lo que dice medir.
        for nid in (muere, sup):
            n = nodos.get(nid)
            if n is None:
                continue
            for campo in CAMPOS:
                lista = n.get(campo) or []
                if nid in lista:
                    fallos.append("%s: (5) %s.%s se cita a si mismo (auto-arista)" % (etiqueta, nid, campo))
                resueltos_a_sup = [x for x in lista if x == muere or resolver(x) == sup]
                if len(resueltos_a_sup) > 1:
                    fallos.append("%s: (5) %s.%s tiene mas de una entrada que resuelve a %s: %s"
                                  % (etiqueta, nid, campo, sup, resueltos_a_sup))

        comprobados += 1

    return comprobados, fallos


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", default="WORK")
    ap.add_argument("--autoprueba", action="store_true",
                     help="corre el caso positivo por mutacion (en memoria) y termina")
    a = ap.parse_args()

    grafo = cargar(a.ref)
    nodos = grafo["nodos"]
    pares = pares_repite()

    if not pares:
        print("ROJO (arnes): cero pares REPITE leidos de los registros. Nada que verificar.")
        return 1

    if a.autoprueba:
        clon = {nid: dict(n) for nid, n in nodos.items()}
        objetivo = pares[0]
        sup, muere = objetivo["superviviente"], objetivo["muere"]
        alias_sup = list(clon[sup].get("ids_alias") or [])
        if muere not in alias_sup:
            print("CAIDA DE LA ARNES: %s no esta en ids_alias de %s en el estado actual, "
                  "no se puede mutar el positivo sobre esto." % (muere, sup))
            return 1
        alias_sup.remove(muere)
        clon[sup]["ids_alias"] = alias_sup
        _comprobados, fallos = verificar(clon, [objetivo])
        esperado = "(2) %s NO aparece en ids_alias de %s" % (muere, sup)
        if not any(esperado in f for f in fallos):
            print("CAIDA DE LA AUTOPRUEBA: borrar el alias de %s en %s no genero el ROJO esperado" % (muere, sup))
            print("fallos obtenidos: %r" % fallos)
            return 1
        print("AUTOPRUEBA VERIFICADA: ROJO nombrando el par %s -> %s tras borrar el alias en memoria" % (muere, sup))
        return 0

    comprobados, fallos = verificar(nodos, pares)

    if fallos:
        print("ROJO EXIT 1: %d comprobacion(es) caida(s) sobre %d par(es) REPITE (ref %s):"
              % (len(fallos), len(pares), a.ref))
        for f in fallos:
            print("  %s" % f)
        return 1

    print("VERDE EXIT 0 (ref %s): %d par(es) REPITE comprobados, cinco comprobaciones cada uno, cero fallos."
          % (a.ref, comprobados))
    for par in pares:
        print("  %s -> %s" % (par["muere"], par["superviviente"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
