# -*- coding: utf-8 -*-
"""vuelta156_tarea2a_verificar_contra_grafo.py . TAREA 2.a DE LA VUELTA 156.

LA MITAD DEL TRATO QUE LE TOCA AL EJECUTOR EN LA RELECTURA CONJUNTA DE
`LD-OPC05-097` (adjudicacion 6.1 del acta 155, y AUDITOR.md seccion 3): EL
AUDITOR PONE EL CASO, EL EJECUTOR VERIFICA CONTRA EL GRAFO. Se publica lo que
se mida, salga a favor o en contra.

QUE MIDE, Y TODO SE LEE HOY DE `dataset/nodos/*.json`, no de una nota:
  1. LOS DOS NODOS VIVOS. `deprecado` de cada uno, leido del fichero.
  2. SUS PASOS ENTEROS. Se imprimen los pasos accionables COMPLETOS de los dos,
     sin recortar, para que la lectura se pueda auditar sin volver al disco.
  3. LA ARISTA BIDIRECCIONAL, MEDIDA EN LAS CUATRO VISTAS: A.nodos_siguientes
     trae a B, A.nodos_previos trae a B, B.nodos_siguientes trae a A y
     B.nodos_previos trae a A. Con el resolutor de alias delante (P.1).
  4. SI ALGUNO DE LOS DOS APARECE EN OTRO PAR DEL REGISTRO DE CITAS, y con que
     clase y con que otro nodo.
  5. SI ALGUNO DE LOS DOS APARECE EN ALGUN ACTO DECLARADO del plan
     (docs/plan/*.md y *.jsonl, barrido por nombre de nodo).

INSTRUMENTO PROPIO. Trae su resolutor de alias escrito aqui, copia del de
`vuelta154_tarea2a_universo_bidireccionales.py`, para no depender de que un
modulo de la casa este bien.

NO DECIDE NADA: mide. La decision con la vara va en la TAREA 2.b.

USO:  python scripts/loop/vuelta156_tarea2a_verificar_contra_grafo.py
"""
import glob
import io
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos", "*.json")
REGISTRO = os.path.join(RAIZ, "docs", "plan", "REGISTRO_DE_CITAS_OPC05.jsonl")
PLAN = os.path.join(RAIZ, "docs", "plan")

PAR = ("juran_rcca_metodo", "viaje_diagnostico_remedial")


def cargar():
    todos = {}
    for ruta in sorted(glob.glob(NODOS)):
        d = json.load(io.open(ruta, encoding="utf-8"))
        nid = d.get("node_id") or os.path.splitext(os.path.basename(ruta))[0]
        todos[nid] = d
    return todos


def hacer_resolutor(todos):
    alias_de = {}
    for nid, n in todos.items():
        for a in n.get("ids_alias") or []:
            if a != nid:
                alias_de[a] = nid

    def resolver(nid):
        n = todos.get(nid)
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
            c = todos.get(cur)
            if c is None:
                continue
            ultimo_real = cur
            if not c.get("deprecado"):
                return cur
        return ultimo_real
    return resolver


def pasos_de(n):
    """Los pasos accionables, con el nombre de campo que el nodo use."""
    for k in ("pasos_accionables", "pasos", "acciones"):
        v = n.get(k)
        if isinstance(v, list) and v:
            return k, v
    return None, []


def main():
    print("=" * 96)
    print("VUELTA 156, TAREA 2.a: `LD-OPC05-097` VERIFICADO CONTRA EL GRAFO, HOY")
    print("=" * 96)
    print("Par: %s  <->  %s" % PAR)
    print("")

    todos = cargar()
    resolver = hacer_resolutor(todos)
    a, b = PAR

    print("-" * 96)
    print("1. LOS DOS NODOS, LEIDOS DE dataset/nodos/*.json")
    print("-" * 96)
    vivos = 0
    for nid in PAR:
        n = todos.get(nid)
        if n is None:
            print("  %-32s NO EXISTE EN EL GRAFO" % nid)
            continue
        dep = bool(n.get("deprecado"))
        if not dep:
            vivos += 1
        print("  %-32s deprecado=%-5s  resuelve a %s" % (nid, dep, resolver(nid)))
        print("     titulo: %s" % n.get("titulo"))
        print("     etiqueta_arbol: %s" % n.get("etiqueta_arbol"))
        print("     dominio: %s | fuente: %s" % (n.get("dominio"), n.get("fuente")))
    print("")
    print("  CIFRA nodos vivos del par: %d nodo(s) de 2" % vivos)

    print("")
    print("-" * 96)
    print("2. LOS PASOS ENTEROS DE LOS DOS, SIN RECORTAR")
    print("-" * 96)
    conteo_pasos = {}
    for nid in PAR:
        n = todos.get(nid) or {}
        campo, pasos = pasos_de(n)
        conteo_pasos[nid] = len(pasos)
        print("")
        print("  %s  (campo `%s`, %d paso(s))" % (nid, campo, len(pasos)))
        for i, p in enumerate(pasos, 1):
            texto = p if isinstance(p, str) else json.dumps(p, ensure_ascii=False)
            print("    %2d. %s" % (i, texto))
    print("")
    print("  CIFRA pasos de %s: %d paso(s)" % (a, conteo_pasos[a]))
    print("  CIFRA pasos de %s: %d paso(s)" % (b, conteo_pasos[b]))

    print("")
    print("-" * 96)
    print("3. LA ARISTA, MEDIDA EN LAS CUATRO VISTAS, CON EL RESOLUTOR DELANTE")
    print("-" * 96)
    vistas = []
    for origen, destino in ((a, b), (b, a)):
        n = todos.get(origen) or {}
        for campo in ("nodos_siguientes", "nodos_previos"):
            crudos = n.get(campo) or []
            resueltos = [resolver(x) for x in crudos]
            hay = resolver(destino) in resueltos
            literal = destino in crudos
            vistas.append((origen, campo, destino, hay, literal))
            print("  %-32s .%-16s trae a %-32s : %-5s (literal: %s)"
                  % (origen, campo, destino, hay, literal))
    ida = any(v[3] for v in vistas if v[0] == a and v[1] == "nodos_siguientes") or \
        any(v[3] for v in vistas if v[0] == b and v[1] == "nodos_previos")
    vuelta = any(v[3] for v in vistas if v[0] == b and v[1] == "nodos_siguientes") or \
        any(v[3] for v in vistas if v[0] == a and v[1] == "nodos_previos")
    print("")
    print("  DIRECCION %s -> %s declarada por alguien: %s" % (a, b, ida))
    print("  DIRECCION %s -> %s declarada por alguien: %s" % (b, a, vuelta))
    print("  BIDIRECCIONAL: %s" % (ida and vuelta))
    print("  CIFRA vistas que declaran la arista: %d direccion(es)"
          % sum(1 for v in vistas if v[3]))

    print("")
    print("-" * 96)
    print("4. LOS DOS NODOS EN EL RESTO DEL REGISTRO DE CITAS")
    print("-" * 96)
    R = [json.loads(x) for x in io.open(REGISTRO, encoding="utf-8") if x.strip()]
    print("  Lineas del registro: %d" % len(R))
    otros = []
    for e in R:
        p = e["par"]
        if tuple(sorted(p)) == tuple(sorted(PAR)):
            print("  LA PROPIA ENTRADA: %s | clase %s | via %s" % (e["cita"], e["clase"], e["via"]))
            continue
        for nid in PAR:
            if nid in p:
                otros.append((nid, e))
    if not otros:
        print("  NINGUNO de los dos aparece en otro par del registro.")
    for nid, e in otros:
        vecino = [x for x in e["par"] if x != nid]
        print("  %-32s aparece con %-32s | clase %s | %s"
              % (nid, ", ".join(vecino), e["clase"], e["cita"]))
    print("")
    print("  CIFRA otras entradas del registro que tocan al par: %d linea(s)" % len(otros))

    print("")
    print("-" * 96)
    print("5. LOS DOS NODOS EN LOS ACTOS DECLARADOS DEL PLAN (docs/plan/)")
    print("-" * 96)
    patron = re.compile("|".join(re.escape(x) for x in PAR))
    golpes = []
    for ruta in sorted(glob.glob(os.path.join(PLAN, "*"))):
        if not os.path.isfile(ruta):
            continue
        if os.path.basename(ruta) == "REGISTRO_DE_CITAS_OPC05.jsonl":
            continue
        try:
            texto = io.open(ruta, encoding="utf-8").read()
        except Exception:
            continue
        for i, linea in enumerate(texto.splitlines(), 1):
            if patron.search(linea):
                golpes.append((os.path.basename(ruta), i, linea.strip()[:150]))
    if not golpes:
        print("  NINGUNO de los dos aparece en ningun fichero de docs/plan/.")
    for f, i, linea in golpes:
        print("  %-42s :%-6d %s" % (f, i, linea))
    print("")
    print("  CIFRA lineas de docs/plan/ que nombran a uno de los dos: %d linea(s)" % len(golpes))

    print("")
    print("=" * 96)
    print("LO QUE ESTA TAREA NO HACE: no decide la clase. La decision con la vara va en")
    print("la TAREA 2.b, y la fusion NO se ejecuta en esta vuelta (adjudicacion 6.1 del")
    print("acta 155: si la clase pasa a A, el par se registra como CANDIDATO A FUSION).")
    print("=" * 96)


main()
