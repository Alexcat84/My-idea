"""VUELTA 17, instrumento propio del ejecutor. SOLO LECTURA.

Pregunta unica: entre el corte 2.117 y el corte 3.388, cual de los 221 actos
viejos de docs/plan/INVENTARIO.jsonl CRECIO de tamano, y de cuanto a cuanto.

No se copia ninguna cifra de ningun acta, reporte ni nota previa: se mide aqui.
Tres metodos independientes, y los tres tienen que coincidir o se declara la
discrepancia en vez de elegir uno.

  metodo A: superset contra docs/plan/RECOMPUTO_3388_COMPONENTES.jsonl
  metodo B: superset contra las 335 entradas nuevas de tipo acto del propio
            INVENTARIO.jsonl (mismo hecho por otra ruta de datos)
  metodo C: sin superset. Se reconstruye la pertenencia nodo -> componente al
            corte 3.388 y se pregunta, por cada acto viejo, cuantos nodos tiene
            hoy la componente que contiene a su primer miembro.

Uso: python scripts/loop/vuelta17_acto_que_crecio.py
"""

import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
INVENTARIO = os.path.join(RAIZ, "docs", "plan", "INVENTARIO.jsonl")
COMPONENTES = os.path.join(RAIZ, "docs", "plan", "RECOMPUTO_3388_COMPONENTES.jsonl")


def cargar_jsonl(ruta):
    filas = []
    with open(ruta, encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.strip()
            if linea:
                filas.append(json.loads(linea))
    return filas


def sucesor_por_superset(viejo, universo):
    """Devuelve la lista de componentes del universo que CONTIENEN enteros a los
    miembros del acto viejo. Se devuelve la lista completa a proposito: si sale
    con mas de uno o con cero, eso es el hallazgo, no un caso a resolver."""
    conjunto = frozenset(viejo)
    return [c for c in universo if conjunto <= frozenset(c)]


def main():
    inventario = cargar_jsonl(INVENTARIO)
    actos = [o for o in inventario if o.get("tipo") == "acto"]
    viejos = [o for o in actos if o.get("fecha_corte") == "2026-08-11"]
    nuevos = [o for o in actos if o.get("fecha_corte") == "2026-08-13"]
    componentes = cargar_jsonl(COMPONENTES)

    print("MATERIA PRIMA MEDIDA EN ESTA CORRIDA")
    print("  INVENTARIO.jsonl, filas totales:", len(inventario))
    print("  de tipo acto:", len(actos))
    print("  actos con fecha_corte 2026-08-11 (el corte 2.117):", len(viejos))
    print("  actos con fecha_corte 2026-08-13 (el corte 3.388):", len(nuevos))
    print("  RECOMPUTO_3388_COMPONENTES.jsonl, componentes:", len(componentes))
    print()

    universo_a = [c["miembros"] for c in componentes]
    universo_b = [c["miembros"] for c in nuevos]

    # ---- metodo C: pertenencia nodo -> componente al corte 3.388 ----
    pertenencia = {}
    colision = []
    for miembros in universo_a:
        for nodo in miembros:
            if nodo in pertenencia:
                colision.append(nodo)
            pertenencia[nodo] = miembros
    print("METODO C, control previo: nodos distintos en los 335 componentes:",
          len(pertenencia), "| nodos en dos componentes a la vez:", len(colision))
    print()

    resultados = {}
    for etiqueta, universo in (("A", universo_a), ("B", universo_b)):
        crecen, iguales, sin_sucesor, multiples = [], 0, [], []
        for acto in viejos:
            viejos_miembros = acto["miembros"]
            cands = sucesor_por_superset(viejos_miembros, universo)
            if not cands:
                sin_sucesor.append(acto["nombre"])
                continue
            if len(cands) > 1:
                multiples.append(acto["nombre"])
            suc = cands[0]
            if len(suc) > len(viejos_miembros):
                ganados = sorted(set(suc) - set(viejos_miembros))
                crecen.append((acto["nombre"], len(viejos_miembros), len(suc), ganados))
            elif len(suc) == len(viejos_miembros):
                iguales += 1
        resultados[etiqueta] = (crecen, iguales, sin_sucesor, multiples)
        print("METODO", etiqueta)
        print("  identicos en tamano:", iguales)
        print("  crecieron:", len(crecen))
        print("  sin sucesor:", len(sin_sucesor), sin_sucesor)
        print("  con mas de un sucesor:", len(multiples), multiples)
        for nombre, antes, despues, ganados in crecen:
            print("  ->", nombre, ":", antes, "a", despues, "| gana:", ", ".join(ganados))
        print()

    # ---- metodo C, sin superset ----
    crecen_c, iguales_c, huerfanos_c = [], 0, []
    for acto in viejos:
        ancla = acto["miembros"][0]
        comp = pertenencia.get(ancla)
        if comp is None:
            huerfanos_c.append(acto["nombre"])
            continue
        if len(comp) > len(acto["miembros"]):
            ganados = sorted(set(comp) - set(acto["miembros"]))
            crecen_c.append((acto["nombre"], len(acto["miembros"]), len(comp), ganados))
        elif len(comp) == len(acto["miembros"]):
            iguales_c += 1
    print("METODO C")
    print("  identicos en tamano:", iguales_c)
    print("  crecieron:", len(crecen_c))
    print("  cuyo primer miembro no esta en ningun componente:", len(huerfanos_c), huerfanos_c)
    for nombre, antes, despues, ganados in crecen_c:
        print("  ->", nombre, ":", antes, "a", despues, "| gana:", ", ".join(ganados))
    print()

    # ---- veredicto ----
    firma = lambda lista: sorted((n, a, d) for n, a, d, _ in lista)
    fa = firma(resultados["A"][0])
    fb = firma(resultados["B"][0])
    fc = firma(crecen_c)
    print("VEREDICTO")
    if fa == fb == fc:
        print("  los tres metodos coinciden:", fa)
    else:
        print("  DISCREPANCIA ENTRE METODOS, se declara y no se resuelve copiando")
        print("  A:", fa)
        print("  B:", fb)
        print("  C:", fc)

    # ---- contraste con el nombre publicado en la vuelta 16 ----
    print()
    print("CONTRASTE con el nombre publicado en la vuelta 16 (construccion_de_leverage)")
    for nombre in ("construccion_de_leverage", "gestion_terminacion_franquiciado"):
        v = [a for a in viejos if a["nombre"] == nombre]
        n = [a for a in nuevos if a["nombre"] == nombre]
        c = [m for m in universo_a if m and m[0] == nombre]
        print("  ", nombre,
              "| tamano al 2.117:", (len(v[0]["miembros"]) if v else "no es acto viejo"),
              "| tamano al 3.388:", (len(n[0]["miembros"]) if n else "no es acto nuevo"),
              "| en COMPONENTES:", (len(c[0]) if c else "no es primer miembro de ninguno"))


if __name__ == "__main__":
    main()
