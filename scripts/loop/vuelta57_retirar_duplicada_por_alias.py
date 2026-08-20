# -*- coding: utf-8 -*-
"""vuelta57_retirar_duplicada_por_alias.py . P.16, QUIEN FABRICA LIMPIA, PARA LA
DUPLICADA QUE SOLO SE VE POR EL RESOLUTOR.

SUCESOR DECLARADO de scripts/loop/vuelta43_retirar_arista_interna.py, al que NO
reemplaza y cuya forma de trabajo se copia entera: retirar ANTES, en los DOS
sentidos, y dejar que el ejecutor de fusiones corra despues ENTERO Y SIN TOCAR,
con sus guardas juzgando el resultado.

POR QUE NACE, con el rojo REAL delante y no uno inventado: la simulacion del
lote A del tramo 4 salio en ROJO con
  DUPLICADA NUEVA: documentacion_exportacion en nodos_previos resuelve dos
  veces a incoterms_reglas_comerciales_internacionales
y la guarda hizo lo correcto. LA CAUSA, MEDIDA: `documentacion_exportacion`
nombra en sus previos a `glosario_terminos_incoterms`, que YA HOY resuelve a
`incoterms_reglas_comerciales_internacionales`, y ademas a
`terminos_de_venta_incoterms`, que hoy resuelve a si mismo y que el acto 17
absorbe. Al fundir, las dos entradas pasan a resolver al mismo nodo vivo.

LA DIFERENCIA CON EL INSTRUMENTO DEL QUE DESCIENDE, y es la que motiva un
fichero nuevo: aquel retiraba la arista INTERNA DEL PAR, la que el superviviente
y el absorbido se dan el uno al otro. Esta duplicada NO es interna al par: vive
en la lista de un TERCER nodo, y el camino literal no la ve porque la otra mitad
del choque no es el id absorbido sino un alias suyo. Es la misma grieta que la
guarda de los ajenos de la vuelta 56 destapo, en otro sitio: LO QUE NO SE LEE
POR EL RESOLUTOR NO SE VE.

LO QUE RETIRA, exactamente y nada mas: la entrada cuyo id es EL ABSORBIDO del
acto, y la entrada reciproca (el tercer nodo dentro de la lista opuesta del
absorbido). Las dos, por el mismo motivo que el instrumento de la vuelta 43
escribio: retirar una sola deja la vista reciproca coja y el paso 5 de
run_phase1 la vuelve a escribir.

  Y NO SE PIERDE NINGUN CAMINO DEL GRAFO, que es lo que hace legitimo retirar:
  el tercer nodo sigue unido al superviviente por la OTRA entrada, la del alias
  que ya resolvia a el. Lo que se retira es la que la fusion vuelve REDUNDANTE,
  no una arista con contenido propio. Eso se COMPRUEBA por nodo antes de tocar
  nada, y si no se cumple es ROJO y no se retira.

SI ALGUNA DUPLICADA NUEVA NO LA FABRICA UN ABSORBIDO DE ESTE PLAN, es ROJO y no
se escribe nada: este instrumento limpia lo que su propia operacion fabrica, y
el pasivo ajeno es de OP-S-12.

NO toca el texto de ningun nodo: ni pasos, ni condiciones, ni titulo, ni
etiqueta, ni resumen, ni entregable. Solo nodos_previos y nodos_siguientes.

Uso:
  python scripts/loop/vuelta57_retirar_duplicada_por_alias.py --plan RUTA.json
  python scripts/loop/vuelta57_retirar_duplicada_por_alias.py --plan RUTA.json --ejecutar
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
CAMPOS = ("nodos_previos", "nodos_siguientes")
OPUESTO = {"nodos_previos": "nodos_siguientes", "nodos_siguientes": "nodos_previos"}


def ruta(nid):
    return os.path.join(NODOS, nid + ".json")


def leer(nid):
    return json.loads(io.open(ruta(nid), encoding="utf-8").read())


def escribir(nid, d):
    io.open(ruta(nid), "w", encoding="utf-8", newline="\n").write(
        json.dumps(d, ensure_ascii=False, indent=2) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", required=True)
    ap.add_argument("--ejecutar", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    plan = json.load(io.open(a.plan, encoding="utf-8"))
    pares = []
    for act in plan["actos"]:
        for ab in act["absorbidos"]:
            pares.append((act["orden"], act["superviviente"], ab))

    print("=" * 78)
    print("P.16 POR EL RESOLUTOR: LAS DUPLICADAS QUE ESTA FUSION FABRICARIA")
    print("MODO %s" % ("EJECUTAR" if a.ejecutar else "SIMULAR"))
    print("=" * 78)
    print("  plan: %s | actos: %d" % (a.plan, len(plan["actos"])))
    print()

    vivos = {}
    alias_hoy = {}
    for nombre in sorted(os.listdir(NODOS)):
        if not nombre.endswith(".json"):
            continue
        d = leer(nombre[:-5])
        if d.get("deprecado") or d.get("deprecated"):
            continue
        vivos[d["node_id"]] = d
        for x in (d.get("ids_alias") or []):
            alias_hoy[x] = d["node_id"]

    alias_post = dict(alias_hoy)
    for _, sup, ab in pares:
        alias_post[ab] = sup

    def resolver(mapa, x):
        v = set()
        while x in mapa and x not in v:
            v.add(x)
            x = mapa[x]
        return x

    absorbidos = {ab: (n, sup) for n, sup, ab in pares}
    hallados, rojos = [], []
    for nid, d in sorted(vivos.items()):
        for campo in CAMPOS:
            lista = d.get(campo) or []
            antes, despues = {}, {}
            for x in lista:
                antes.setdefault(resolver(alias_hoy, x), []).append(x)
                despues.setdefault(resolver(alias_post, x), []).append(x)
            for destino, entradas in despues.items():
                if len(entradas) < 2:
                    continue
                if len(antes.get(destino, [])) >= 2:
                    continue  # YA ESTABA duplicada: pasivo de OP-S-12, no mio
                culpables = [x for x in entradas if x in absorbidos]
                otras = [x for x in entradas if x not in absorbidos]
                if not culpables or not otras:
                    rojos.append((nid, campo, destino, entradas))
                    continue
                # LO QUE EL EJECUTOR YA ARREGLA SOLO NO SE TOCA, y se dice por
                # que: el ejecutor de fusiones sustituye el id absorbido por el
                # del superviviente Y DESPUES DEDUPLICA LITERAL. Si la otra
                # entrada ES el superviviente escrito con su propio nombre, esa
                # sustitucion deja el id repetido y la deduplicacion literal lo
                # resuelve sin ayuda. La duplicada que SOBREVIVE al ejecutor es
                # solo la que llega por un ALIAS, porque ahi las dos cadenas son
                # distintas y solo el resolutor las ve iguales. Medido hoy sobre
                # el lote A: de las CUATRO que este instrumento encontraba,
                # TRES eran de la primera especie y el ejecutor las limpiaba
                # solo; la unica real es la de documentacion_exportacion, que es
                # la que su guarda final reporto en ROJO.
                if any(x == destino for x in otras):
                    continue
                for x in culpables:
                    hallados.append((nid, campo, x, destino, otras,
                                     absorbidos[x][0], absorbidos[x][1]))

    if not hallados and not rojos:
        print("  NINGUNA. Esta fusion no fabrica ninguna duplicada por alias.")
        print()
        print("FIN")
        return 0

    print("  DUPLICADAS QUE LA FUSION FABRICARIA: %d" % len(hallados))
    for nid, campo, x, destino, otras, orden, sup in hallados:
        print("    %s | %s" % (nid, campo))
        print("       la fabrica el acto %d: %s pasa a resolver a %s" % (orden, x, sup))
        print("       el camino que YA existia y se conserva: %s" % ", ".join(otras))
        print("       SE RETIRA la entrada %s, y la reciproca en %s.%s"
              % (x, x, OPUESTO[campo]))
    print()
    if rojos:
        print("  ROJO: %d duplicadas que este plan NO fabrica del todo. No se escribe nada:"
              % len(rojos))
        for nid, campo, destino, entradas in rojos:
            print("    %s | %s | resuelven a %s: %s" % (nid, campo, destino, entradas))
        return 1

    if not a.ejecutar:
        print("  MODO SIMULAR: no se escribe nada.")
        print()
        print("FIN")
        return 0

    tocados = 0
    for nid, campo, x, destino, otras, orden, sup in hallados:
        d = leer(nid)
        lista = d.get(campo) or []
        if x in lista:
            d[campo] = [y for y in lista if y != x]
            escribir(nid, d)
            tocados += 1
            print("  retirado: %s.%s ya no nombra a %s" % (nid, campo, x))
        # LA RECIPROCA, por el mismo motivo que la vuelta 43 escribio
        da = leer(x)
        op = OPUESTO[campo]
        lop = da.get(op) or []
        if nid in lop:
            da[op] = [y for y in lop if y != nid]
            escribir(x, da)
            tocados += 1
            print("  retirado: %s.%s ya no nombra a %s (la reciproca)" % (x, op, nid))
    print()
    print("  entradas retiradas: %d" % tocados)
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
