# -*- coding: utf-8 -*-
r"""vuelta141_2_mutaciones.py . LAS MUTACIONES DE LA TAREA 2 DE LA VUELTA 141
(acta de la vuelta 140, adjudicaciones 3.1 y 3.4 y caida 4.1).

Importa scripts/loop/tallar_estado_de_fase.py y MUTA EN MEMORIA. NUNCA escribe
en disco: ni el grafo, ni OPERACIONES.jsonl, ni los dos registros de remision.

TODAS LAS MUTACIONES ELIGEN SU SUJETO POR COMPUTO Y NUNCA TECLEADO
(EJECUTOR.md regla 1, "EL CASO ROJO SE PRUEBA POR MUTACION"): el nombre de la
operacion y el de la direccion mutada salen de recorrer la tabla medida, no de
una constante literal escrita aqui.

  (2.a.i)  LA VUELTA QUE NACE. Se busca por computo una operacion de vara
           ENLACE con regimen PROHIBE que HOY cumple, y dentro de ella una
           direccion cuya vuelta NO existe. Se mete esa vuelta en el grafo en
           memoria. Esperado: la operacion sale NOMBRADA en SIN CUMPLIR y la
           cifra "con destino cumplido" BAJA. Contraprueba: sin mutar, la misma
           operacion NO esta en SIN CUMPLIR.

  (2.a.ii) LA VUELTA QUE MUERE. Se busca por computo una operacion de vara
           ENLACE con regimen PROHIBE que HOY no cumple Y CUYO UNICO DEFECTO ES
           LA VUELTA (todas sus idas presentes). Se quita esa vuelta del grafo
           en memoria, en las dos vistas. Esperado: la operacion SUBE a
           cumplida y la cifra "con destino cumplido" SUBE. Contraprueba: sin
           mutar, la operacion esta en SIN CUMPLIR.

  (2.b)    EL CATALOGO DE UNA MESA. Se corre la medicion con las remisiones
           tal cual y con la TABLA DE REMISION VACIADA (se conserva solo la
           parte del 00_INDICE), y se compara la nomina de la mesa. Esperado:
           con la tabla, OP-M-01-SEXTO esta en la nomina de su mesa; sin la
           tabla, NO esta. La mesa se elige por computo: la que la tabla de
           remision nombra y `bloquea_a` no.

  (2.c)    LA UNIDAD DE LA CELDA. Se fabrica una ficha con DOS filas de
           aristas_nuevas que COLAPSAN en la misma direccion (por alias) y se
           mide: la celda tiene que dar la cuenta de DIRECCIONES (1) y decir
           que 2 filas colapsan. Contraprueba: la misma ficha sin el colapso da
           2 direcciones y "sin colapso". El par alias/vivo se saca del grafo
           por computo.

PRUEBA DE MUTACION DEL PROPIO ARNES (EJECUTOR.md regla 1, "el caso rojo se
prueba por mutacion"): al final se vuelve a correr CADA comprobacion con el
valor esperado CAMBIADO, y se exige que TODAS caigan. Si alguna siguiera verde
con el esperado equivocado, ese assert no podria fallar nunca y el arnes sale
en ROJO diciendolo.

USO:
  python scripts/loop/vuelta141_2_mutaciones.py
"""
import copy
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tallar_estado_de_fase as T

FASE = "06_MESAS"

_resultados = []


def comprobar(nombre, obtenido, esperado):
    """Guarda el OBTENIDO ademas del veredicto, para que la prueba de mutacion
    del final pueda RE-EVALUAR la comparacion con el esperado cambiado en vez
    de darla por supuesta."""
    ok = obtenido == esperado
    _resultados.append((nombre, obtenido, esperado, ok))
    print("   %-6s %s | obtenido=%r esperado=%r" % ("VERDE" if ok else "ROJO", nombre,
                                                    obtenido, esperado))
    return ok


def medir(ops, nodos, remisiones=None):
    lista, cifra, fallos = T.medir(FASE, ops, nodos, remisiones=remisiones)
    return {f["id_op"]: f for f in lista}, cifra, fallos


def quitar_arista(nodos, resolver, origen, destino):
    """Quita origen -> destino en LAS DOS VISTAS, resolviendo por alias."""
    no, nd = nodos[origen], nodos[destino]
    no["nodos_siguientes"] = [x for x in (no.get("nodos_siguientes") or [])
                              if resolver(x) != destino]
    nd["nodos_previos"] = [x for x in (nd.get("nodos_previos") or [])
                           if resolver(x) != origen]


def main():
    ops = T.cargar_ops("WORK")
    nodos = T.cargar_grafo("WORK")
    por_id = {o.get("id_op"): o for o in ops}
    remisiones = T.leer_remisiones(FASE, "WORK")

    base_filas, base_cifra, base_fallos = medir(ops, nodos, copy.deepcopy(remisiones))
    print("BASE (sin mutar): catalogo %d | cumplido %d | sin cumplir %d | fallos %d"
          % (base_cifra["catalogo"], base_cifra["cumplido"], base_cifra["sin_cumplir"],
             len(base_fallos)))
    print("BASE, SIN CUMPLIR: %s" % ", ".join(base_cifra["nombres_sin_cumplir"]))
    print("")

    resolver = T.resolver_de(nodos)

    # ---------------------------------------------------------------- 2.a.i
    print("MUTACION 2.a.i: LA VUELTA QUE NACE (sujeto elegido POR COMPUTO).")
    sujeto_i = None
    for f in base_filas.values():
        if f["vara"] != "ENLACE" or f["cumplido"] is not True:
            continue
        op = por_id[f["id_op"]]
        if T.regimen_de_vuelta(op, [])[0] != "PROHIBE":
            continue
        for ro, rd in T.direcciones_de(T.pares_de_aristas(op, []), resolver):
            if not T.arista_presente(nodos, resolver, rd, ro)[0]:
                sujeto_i = (f["id_op"], ro, rd)
                break
        if sujeto_i:
            break
    if not sujeto_i:
        print("   ROJO (arnes): ninguna operacion ENLACE con regimen PROHIBE, cumplida "
              "hoy y con una direccion limpia. No hay caso que mutar.")
        return 1
    op_i, ro_i, rd_i = sujeto_i
    print("   sujeto computado: %s, direccion %s -> %s; la vuelta que se mete es %s -> %s"
          % (op_i, ro_i, rd_i, rd_i, ro_i))

    nodos_i = copy.deepcopy(nodos)
    nodos_i[rd_i].setdefault("nodos_siguientes", []).append(ro_i)
    filas_i, cifra_i, _ = medir(ops, nodos_i, copy.deepcopy(remisiones))
    comprobar("2.a.i la operacion sale NOMBRADA en SIN CUMPLIR",
              op_i in cifra_i["nombres_sin_cumplir"], True)
    comprobar("2.a.i la cifra de cumplido BAJA",
              cifra_i["cumplido"] < base_cifra["cumplido"], True)
    comprobar("2.a.i la celda nombra la vuelta metida",
              ("%s -> %s" % (rd_i, ro_i)) in filas_i[op_i]["razon"], True)
    comprobar("2.a.i CONTRAPRUEBA sin mutar: la operacion NO esta en SIN CUMPLIR",
              op_i in base_cifra["nombres_sin_cumplir"], False)
    print("")

    # --------------------------------------------------------------- 2.a.ii
    print("MUTACION 2.a.ii: LA VUELTA QUE MUERE (sujeto elegido POR COMPUTO).")
    sujeto_ii = None
    for f in base_filas.values():
        if f["vara"] != "ENLACE" or f["cumplido"] is not False:
            continue
        op = por_id[f["id_op"]]
        if T.regimen_de_vuelta(op, [])[0] != "PROHIBE":
            continue
        dirs = T.direcciones_de(T.pares_de_aristas(op, []), resolver)
        idas = [T.arista_presente(nodos, resolver, ro, rd)[0] for ro, rd in dirs]
        vueltas = [(ro, rd) for ro, rd in dirs
                   if T.arista_presente(nodos, resolver, rd, ro)[0]]
        if all(idas) and len(vueltas) == 1:
            sujeto_ii = (f["id_op"], vueltas[0][0], vueltas[0][1])
            break
    if not sujeto_ii:
        print("   ROJO (arnes): ninguna operacion ENLACE con regimen PROHIBE cuyo UNICO "
              "defecto sea una sola vuelta. No hay caso que mutar.")
        return 1
    op_ii, ro_ii, rd_ii = sujeto_ii
    print("   sujeto computado: %s, direccion %s -> %s; la vuelta que se quita es %s -> %s"
          % (op_ii, ro_ii, rd_ii, rd_ii, ro_ii))

    nodos_ii = copy.deepcopy(nodos)
    quitar_arista(nodos_ii, T.resolver_de(nodos_ii), rd_ii, ro_ii)
    filas_ii, cifra_ii, _ = medir(ops, nodos_ii, copy.deepcopy(remisiones))
    comprobar("2.a.ii la operacion SUBE a cumplida",
              filas_ii[op_ii]["cumplido"], True)
    comprobar("2.a.ii la cifra de cumplido SUBE",
              cifra_ii["cumplido"] > base_cifra["cumplido"], True)
    comprobar("2.a.ii CONTRAPRUEBA sin mutar: la operacion esta en SIN CUMPLIR",
              op_ii in base_cifra["nombres_sin_cumplir"], True)
    print("")

    # ------------------------------------------------------------------ 2.b
    print("MUTACION 2.b: EL CATALOGO DE UNA MESA SIN SU TABLA DE REMISION.")
    solo_indice = {h: dict(m) for h, m in remisiones.items() if m.get("a") is None}
    hija_por_remision = None
    for h, m in sorted(remisiones.items()):
        mesa = m.get("a")
        if not mesa:
            continue
        op_mesa = por_id.get(mesa)
        if op_mesa is not None and h not in (op_mesa.get("bloquea_a") or []):
            hija_por_remision = (mesa, h)
            break
    if not hija_por_remision:
        print("   ROJO (arnes): la tabla de remision no nombra ninguna hija que "
              "bloquea_a no nombre. No hay caso que mutar.")
        return 1
    mesa_b, hija_b = hija_por_remision
    print("   sujeto computado: la mesa %s y su hija %s, que bloquea_a NO nombra"
          % (mesa_b, hija_b))

    filas_con, _, _ = medir(ops, nodos, copy.deepcopy(remisiones))
    filas_sin, _, _ = medir(ops, nodos, copy.deepcopy(solo_indice))
    comprobar("2.b CON la tabla, la nomina de la mesa trae a la hija",
              hija_b in filas_con[mesa_b]["razon"], True)
    comprobar("2.b SIN la tabla, la nomina de la mesa PIERDE a la hija",
              hija_b in filas_sin[mesa_b]["razon"], False)
    comprobar("2.b CON la tabla, la celda dice de donde sale la hija",
              ("%s por remision" % hija_b) in filas_con[mesa_b]["razon"], True)
    print("")

    # ------------------------------------------------------------------ 2.c
    print("MUTACION 2.c: LA UNIDAD DE LA CELDA, FILAS CONTRA DIRECCIONES.")
    par_alias = None
    for nid, n in sorted(nodos.items()):
        if n.get("deprecado"):
            continue
        for a in sorted(n.get("ids_alias") or []):
            if resolver(a) == nid and a != nid:
                par_alias = (a, nid)
                break
        if par_alias:
            break
    origen_c = None
    for nid, n in sorted(nodos.items()):
        if not n.get("deprecado") and nid != par_alias[1]:
            origen_c = nid
            break
    otro_c = None
    for nid, n in sorted(nodos.items()):
        if not n.get("deprecado") and nid not in (par_alias[1], origen_c):
            otro_c = nid
            break
    alias_c, vivo_c = par_alias
    print("   sujeto computado: alias %s que resuelve a %s; origen %s; tercero %s"
          % (alias_c, vivo_c, origen_c, otro_c))

    ficha_colapsa = {
        "id_op": "OP-FICHA-DE-PRUEBA",
        "verificacion": ["UNA SOLA DIRECCION POR ENLACE: la vuelta no debe existir"],
        "aristas_nuevas": ["%s -> %s (nodos_siguientes), por LD-901" % (origen_c, alias_c),
                           "%s -> %s (nodos_siguientes), por LD-902" % (origen_c, vivo_c)],
    }
    ficha_sin_colapso = dict(ficha_colapsa)
    ficha_sin_colapso["aristas_nuevas"] = [
        "%s -> %s (nodos_siguientes), por LD-901" % (origen_c, vivo_c),
        "%s -> %s (nodos_siguientes), por LD-902" % (origen_c, otro_c)]

    fallos_c = []
    _, razon_col = T.destino_de_enlace(ficha_colapsa,
                                       T.pares_de_aristas(ficha_colapsa, fallos_c),
                                       nodos, resolver, fallos_c)
    _, razon_sin = T.destino_de_enlace(ficha_sin_colapso,
                                       T.pares_de_aristas(ficha_sin_colapso, fallos_c),
                                       nodos, resolver, fallos_c)
    print("   celda CON colapso: %s" % razon_col)
    print("   celda SIN colapso: %s" % razon_sin)
    comprobar("2.c con colapso el denominador es de DIRECCIONES (1)",
              "de 1 direcciones" in razon_col, True)
    comprobar("2.c con colapso la celda NOMBRA las filas de ficha como tales",
              "2 filas de ficha colapsan en 1 direcciones" in razon_col, True)
    comprobar("2.c CONTRAPRUEBA sin colapso: dos direcciones y sin colapso",
              "de 2 direcciones" in razon_sin and "sin colapso" in razon_sin, True)
    print("")

    # ------------------------------------------ prueba de mutacion del arnes
    print("PRUEBA DE MUTACION DEL PROPIO ARNES: se cambia el valor esperado de CADA")
    print("comprobacion y se RE-EVALUA la comparacion contra el MISMO valor obtenido.")
    print("La que siga verde con el esperado cambiado no puede fallar nunca y sale ROJA")
    print("aqui (EJECUTOR.md regla 1, 'EL CASO ROJO SE PRUEBA POR MUTACION').")
    no_caen = []
    for nombre, obtenido, esperado, _ok in _resultados:
        esperado_mutado = not esperado
        sigue_verde = (obtenido == esperado_mutado)
        if sigue_verde:
            no_caen.append(nombre)
    print("   comprobaciones corridas: %d | verdes: %d | caen con el esperado mutado: %d"
          % (len(_resultados), sum(1 for r in _resultados if r[3]),
             len(_resultados) - len(no_caen)))
    for nombre in no_caen:
        print("   NO CAE con el esperado mutado: %s" % nombre)

    todas_verdes = all(r[3] for r in _resultados)
    print("")
    if todas_verdes and not no_caen:
        print("VERDE: las %d comprobaciones pasan, y las %d caen al mutarles el esperado."
              % (len(_resultados), len(_resultados)))
        return 0
    print("ROJO: %d comprobacion(es) fallan, %d no caen al mutar su esperado."
          % (sum(1 for r in _resultados if not r[3]), len(no_caen)))
    for nombre, _obtenido, _esperado, ok in _resultados:
        if not ok:
            print("   FALLA: %s" % nombre)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
