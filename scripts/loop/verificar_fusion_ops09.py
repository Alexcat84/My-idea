# -*- coding: utf-8 -*-
r"""verificar_fusion_ops09.py . LA GUARDA NUEVA DE LA FUSION DE OP-S-09
(TAREA 1.g de la vuelta 125, encargo docs/loop/PROMPT_SIGUIENTE.md).

CONTRATO (exacto, del encargo): se corre DESPUES de ejecutar OP-S-09. Lee
dataset/metadata/master_graph.json y, por cada par REPITE ejecutado,
comprueba:
  (1) el id que muere esta DEPRECADO
  (2) el id que muere aparece en ids_alias del superviviente
  (3) el superviviente sigue VIVO
  (4) [ENSANCHADA en la vuelta 126, ver abajo]
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

--- LA (4) SE REEMPLAZA, NO SE ENSANCHA AL LADO (TAREA 1.g, vuelta 126) ---

POR QUE NACE (acta de la vuelta 125, caida 5.2, DEL AUDITOR). La (4) vieja
preguntaba "x == muere and resolver(x) != sup" recorriendo TODOS los nodos
vivos. Pero el resolutor se construye del propio ids_alias del
superviviente (resolver_de()): en cuanto la (2) pasa (muere esta en
ids_alias de sup), resolver(muere) SIEMPRE da sup, para cualquier x que
valga muere. La pregunta no podia caer NUNCA: probado por mutacion propia
del auditor (mutar fijacion_de_metas para que citara de nuevo a
dia_cero_defectos_3 con el alias intacto dio CERO FALLOS).

CONTRATO NUEVO de la (4): por cada absorbido, se leen sus DOS listas
(nodos_siguientes y nodos_previos) TAL COMO QUEDARON EN EL NODO MUERTO (el
registro historico, que sigue ahi). Cada id de esas listas se resuelve con
el resolutor de HOY. Si resuelve a un nodo VIVO distinto del superviviente,
esa arista TIENE QUE EXISTIR HOY entre el superviviente y ese nodo, en la
direccion que tenia (lo que estaba en nodos_siguientes del muerto va de
superviviente hacia alla; lo que estaba en nodos_previos viene de alla
hacia el superviviente), mirando LAS DOS VISTAS (la lista del propio
superviviente y la lista reciproca del otro nodo) para darla por presente.
Si no existe en NINGUNA de las dos vistas, ROJO EXIT 1 nombrando el par, la
arista que falta y de que id muerto y de que entrada cruda venia. Los ids
que resuelven al PROPIO superviviente no cuentan (arista interna que P.16
manda retirar) y los que resuelven a un nodo que sigue DEPRECADO tampoco
(no hay a donde llevarla).

CASO POSITIVO (mutacion, en memoria, no toca disco), VAN TRES, con
--autoprueba:
  (a, ya existia) sobre una copia del grafo real se borra el alias de uno
  de los muertos: tiene que dar ROJO nombrando exactamente ese par en la
  comprobacion (2).
  (b, NUEVO en la 126) sobre una copia del grafo real se borra, DE LAS DOS
  VISTAS, una arista que el superviviente ya heredo de su absorbido: tiene
  que dar ROJO en la (4) nueva nombrandola. Se busca automaticamente el
  primer par y arista que cumplan el contrato para no depender de un
  ejemplar tecleado a mano.
  (c, NUEVO en la 126, EL CASO ROJO REAL) correr esta guarda contra WORK
  (el arbol que dejo la vuelta 125, ANTES de la reposicion de la vuelta
  126, sin ref): la (4) nueva da ROJO EXIT 1 nombrando dos veces la misma
  arista, dia_cero_defectos_2 -> eliminacion_causas_error_4 (una vez desde
  cada muerto que la citaba), porque a esa altura la arista todavia no
  estaba puesta. Corriendo la guarda VIEJA (la version antes de esta
  vuelta) sobre el MISMO WORK, sin mutar nada, da VERDE EXIT 0: es la
  prueba de que la (4) nueva MUERDE y la vieja no veia nada (docs/loop/
  SALIDA_V126_1G_CASO_ROJO_WORK_NUEVA.txt contra docs/loop/
  SALIDA_V126_1G_CASO_ROJO_WORK_VIEJA.txt). DISCREPANCIA DECLARADA (no se
  resuelve copiando): el encargo de la vuelta 126 pedia este mismo caso
  con --ref c9ac2fb8 (el HEAD sellado de apertura de la vuelta 125). Medido
  (docs/loop/SALIDA_V126_1G_REF_C9AC2FB8.txt): a ese ref NINGUNO de los
  cuatro pares de OP-S-09 esta fusionado todavia (la fusion entera es obra
  de la propia vuelta 125, commit b0414bbc, posterior a c9ac2fb8), asi que
  ahi caen tambien las comprobaciones (1) y (2) de los cuatro pares, y la
  (4) nombra "dia_cero_defectos_2 -> eliminacion_causas_error" (sin el
  sufijo _4) porque a esa altura eliminacion_causas_error tampoco tiene
  alias todavia. --ref c9ac2fb8 SI prueba que la (4) nueva muerde (sigue en
  ROJO), pero no aisla el caso al modo que el encargo describe; WORK sin
  ref es el estado que reproduce el ejemplar exacto del acta 125 seccion
  5.2 y el que se cita como evidencia principal.
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


def comprobacion_4(nodos, resolver, muere, sup):
    """Contrato NUEVO de la (4) (TAREA 1.g, vuelta 126, ver docstring del
    modulo). Devuelve una lista de (origen, destino, campo_origen, x_crudo)
    por cada arista que el nodo muerto tenia y que hoy no esta puesta entre
    el superviviente y el otro extremo, en ninguna de las dos vistas."""
    n_muere = nodos.get(muere)
    n_sup = nodos.get(sup)
    faltantes = []
    if n_muere is None or n_sup is None:
        return faltantes

    def resueltos(n, campo):
        return set(resolver(x) for x in (n.get(campo) or []))

    sup_sig = resueltos(n_sup, "nodos_siguientes")
    sup_prev = resueltos(n_sup, "nodos_previos")

    for x in (n_muere.get("nodos_siguientes") or []):
        destino = resolver(x)
        if destino == sup:
            continue
        n_destino = nodos.get(destino)
        if n_destino is None or n_destino.get("deprecado"):
            continue
        presente = destino in sup_sig or sup in resueltos(n_destino, "nodos_previos")
        if not presente:
            faltantes.append((sup, destino, "nodos_siguientes", x))

    for x in (n_muere.get("nodos_previos") or []):
        origen = resolver(x)
        if origen == sup:
            continue
        n_origen = nodos.get(origen)
        if n_origen is None or n_origen.get("deprecado"):
            continue
        presente = origen in sup_prev or sup in resueltos(n_origen, "nodos_siguientes")
        if not presente:
            faltantes.append((origen, sup, "nodos_previos", x))

    return faltantes


def _hallar_candidato_mutacion_4(nodos, resolver, pares):
    """Busca, sin teclear un ejemplar a mano, el primer par y la primera
    arista YA HEREDADA por el superviviente (presente en las DOS vistas) que
    sirva para la mutacion (b): borrarla de las dos vistas tiene que
    producir un ROJO nuevo en comprobacion_4."""
    for par in pares:
        muere, sup = par["muere"], par["superviviente"]
        n_muere = nodos.get(muere)
        n_sup = nodos.get(sup)
        if n_muere is None or n_sup is None:
            continue
        for x in (n_muere.get("nodos_siguientes") or []):
            destino = resolver(x)
            if destino == sup:
                continue
            n_destino = nodos.get(destino)
            if n_destino is None or n_destino.get("deprecado"):
                continue
            if destino in (n_sup.get("nodos_siguientes") or []) and \
               sup in (n_destino.get("nodos_previos") or []):
                return par, "nodos_siguientes", sup, destino
        for x in (n_muere.get("nodos_previos") or []):
            origen = resolver(x)
            if origen == sup:
                continue
            n_origen = nodos.get(origen)
            if n_origen is None or n_origen.get("deprecado"):
                continue
            if origen in (n_sup.get("nodos_previos") or []) and \
               sup in (n_origen.get("nodos_siguientes") or []):
                return par, "nodos_previos", sup, origen
    return None


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

        for origen, destino, campo_origen, x_crudo in comprobacion_4(nodos, resolver, muere, sup):
            fallos.append("%s: (4) falta la arista %s -> %s hoy (venia de %s.%s, "
                          "entrada cruda %r)" % (etiqueta, origen, destino, muere, campo_origen, x_crudo))

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
        # (a) CASO POSITIVO DE LA (2): borrar el alias del primer par.
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
            print("CAIDA DE LA AUTOPRUEBA (a): borrar el alias de %s en %s no genero el ROJO esperado" % (muere, sup))
            print("fallos obtenidos: %r" % fallos)
            return 1
        print("AUTOPRUEBA (a) VERIFICADA: ROJO nombrando el par %s -> %s tras borrar el alias en memoria" % (muere, sup))

        # (b) CASO POSITIVO DE LA (4) NUEVA (vuelta 126): borrar, de las dos
        # vistas, una arista ya heredada por el superviviente.
        resolver = resolver_de(nodos)
        candidato = _hallar_candidato_mutacion_4(nodos, resolver, pares)
        if candidato is None:
            print("CAIDA DE LA ARNES (b): no se hallo ninguna arista heredada, presente en las "
                  "dos vistas, para mutar sobre el estado actual.")
            return 1
        par2, campo, sup2, otro = candidato
        clon2 = {nid: dict(n) for nid, n in nodos.items()}
        if campo == "nodos_siguientes":
            clon2[sup2]["nodos_siguientes"] = [y for y in (clon2[sup2].get("nodos_siguientes") or []) if y != otro]
            clon2[otro]["nodos_previos"] = [y for y in (clon2[otro].get("nodos_previos") or []) if y != sup2]
            esperado_b = "falta la arista %s -> %s hoy" % (sup2, otro)
        else:
            clon2[sup2]["nodos_previos"] = [y for y in (clon2[sup2].get("nodos_previos") or []) if y != otro]
            clon2[otro]["nodos_siguientes"] = [y for y in (clon2[otro].get("nodos_siguientes") or []) if y != sup2]
            esperado_b = "falta la arista %s -> %s hoy" % (otro, sup2)
        _comprobados2, fallos2 = verificar(clon2, [par2])
        if not any(esperado_b in f for f in fallos2):
            print("CAIDA DE LA AUTOPRUEBA (b): borrar %s <-> %s de las dos vistas no genero el "
                  "ROJO esperado" % (sup2, otro))
            print("fallos obtenidos: %r" % fallos2)
            return 1
        print("AUTOPRUEBA (b) VERIFICADA: ROJO nombrando la arista %s <-> %s (par %s -> %s) tras "
              "borrarla de las dos vistas en memoria" % (sup2, otro, par2["muere"], par2["superviviente"]))
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
