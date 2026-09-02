# -*- coding: utf-8 -*-
"""vuelta144_3a_mutaciones.py . LAS CUATRO MUTACIONES DE LA TAREA 3.a, v144.

Prueban la rama nueva de `medir()`: LA MESA QUE DECLARA SU FIGURA EN SU PROPIO
`tipo` SE MIDE CON LAS VARAS DE SU FIGURA (acta 143, adjudicacion 3.9;
CORRECCION 20).

  (i)   sobre la ficha EJECUTADA en memoria (grafo simulado), la mesa sale
        CUMPLIDA. ES LA CONTRAPRUEBA, y sin ella las otras tres no probarian
        nada: una vara que dijera siempre SIN CUMPLIR las pasaria todas.
  (ii)  con UNA de las dos fusiones a medias, sale SIN CUMPLIR y NOMBRA cual.
  (iii) con el enlace en la DIRECCION EQUIVOCADA, sale SIN CUMPLIR POR EL
        ENLACE y no por las fusiones.
  (iv)  borrada la frase de la figura del `tipo`, la mesa vuelve a NO
        COMPUTABLE con EL MISMO TEXTO DE CELDA que salia antes de esta tarea.
        El texto viejo no se teclea: se lee del fichero de salida
        docs/loop/SALIDA_V144_2A_ESTADO_DESPUES.txt, que es la tabla tallada
        ANTES de la 3.a (EJECUTOR.md, "LA TABLA SE CUENTA DE SU FICHERO").

TODO EN MEMORIA Y CON CERO ESCRITURAS. El grafo simulado es el patron que
`vuelta142_2c_mutaciones.py` estreno y que el acta 143 aprobo (adjudicacion
3.7). Los veredictos se comparan contra variables que el codigo computa, nunca
contra literales (EJECUTOR.md regla 1).
"""
import copy
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
import tallar_estado_de_fase as T  # noqa: E402

TABLA_ANTES = os.path.join(RAIZ, "docs", "loop", "SALIDA_V144_2A_ESTADO_DESPUES.txt")


def emparejamiento_declarado_de(op):
    """{superviviente: [absorbidos]} LEIDO DE LA PROPIA FICHA, no tecleado.

    LA DECISION DE LECTURA, DECLARADA: la ficha de `OP-M-04` no trae el reparto
    en un campo, pero SI lo escribe en una linea de `verificacion` que nombra,
    frase a frase, con que alias queda cada superviviente:

        "identificar_consejo_asesores queda con DOS alias: el que ya tenia,
         identificar_advisory_board, y el nuevo identificar_junta_asesores.
         formalizar_junta_asesora queda con uno: formalize_advisory_board"

    Se parte la linea en frases, se toma la frase que EMPIEZA por el id de un
    superviviente, y los eliminados de la ficha que aparezcan en esa frase son
    sus absorbidos. Si un eliminado no cae en ninguna frase, o cae en dos, se
    devuelve None y el llamador lo canta: no se adivina."""
    sups = [x for x in (op.get("nodos") or [])
            if re.search(r"\b%s\b" % re.escape(x), op.get("superviviente") or "")]
    elim = list(op.get("eliminar") or [])
    for linea in (op.get("verificacion") or []):
        frases = re.split(r"(?<=[.;])\s+", linea)
        reparto = {s: [] for s in sups}
        casas = {x: 0 for x in elim}
        for frase in frases:
            duenos = [s for s in sups if frase.strip().startswith(s)]
            if len(duenos) != 1:
                continue
            for x in elim:
                if re.search(r"\b%s\b" % re.escape(x), frase):
                    reparto[duenos[0]].append(x)
                    casas[x] += 1
        if all(v == 1 for v in casas.values()) and all(reparto[s] for s in sups):
            return reparto, linea
    return None, None


def ficha(id_op):
    for o in T.cargar_ops("WORK"):
        if o.get("id_op") == id_op:
            return o
    raise SystemExit("ROJO PREVIO: no esta la ficha " + id_op)


def grafo_ejecutado(nodos, op, reparto, origen, destino):
    """El grafo TAL COMO QUEDA si la mesa se ejecuta: los absorbidos deprecados
    y en los ids_alias de su superviviente, la arista vieja retirada y la de la
    escalera puesta en sus dos vistas."""
    g = copy.deepcopy(nodos)
    for sup, absorbidos in reparto.items():
        alias = list(g[sup].get("ids_alias") or [])
        for x in absorbidos:
            g[x]["deprecado"] = True
            if x not in alias:
                alias.append(x)
        g[sup]["ids_alias"] = alias
    res = T.resolver_de(g)
    # la arista vieja, en la direccion contraria a la escalera, se retira
    g[destino]["nodos_siguientes"] = [y for y in (g[destino].get("nodos_siguientes") or [])
                                      if res(y) != origen]
    g[origen]["nodos_previos"] = [y for y in (g[origen].get("nodos_previos") or [])
                                  if res(y) != destino]
    # la arista de la escalera se escribe en las dos vistas, con ids resueltos
    g[origen].setdefault("nodos_siguientes", []).append(destino)
    g[destino].setdefault("nodos_previos", []).append(origen)
    return g


def celda_de(op, nodos):
    """La celda que la vara saca hoy para esta ficha, medida sobre este grafo."""
    fallos = []
    cumplido, razon = T.destino_de_mesa_con_figura(op, nodos, T.resolver_de(nodos), fallos)
    return cumplido, razon, fallos


def celda_de_la_tabla(op, nodos, remisiones):
    """La celda ENTERA que `medir()` produce para esta operacion, con la rama
    que le toque. Se usa para la mutacion (iv), que compara contra la tabla
    vieja."""
    ops = [o for o in T.cargar_ops("WORK") if o.get("id_op") != op.get("id_op")] + [op]
    filas, cifra, fallos = T.medir("06_MESAS", ops, nodos, remisiones=remisiones)
    for f in filas:
        if f["id_op"] == op.get("id_op"):
            return f
    return None


def razon_de_la_tabla_vieja(id_op):
    """La celda de `razon` que la tabla tallada ANTES de la 3.a publica para
    esta operacion. SE LEE DEL FICHERO, no se teclea."""
    if not os.path.exists(TABLA_ANTES):
        return None
    for l in io.open(TABLA_ANTES, encoding="utf-8"):
        if l.startswith("| %s |" % id_op):
            celdas = [c.strip() for c in l.strip().strip("|").split("|")]
            return celdas[5]
    return None


def main():
    op = ficha("OP-M-04")
    nodos = T.cargar_grafo("WORK")
    remisiones = T.leer_remisiones("06_MESAS", "WORK")

    print("MUTACIONES DE LA TAREA 3.a | vuelta 144 | %s" % op.get("id_op"))
    print("Todo EN MEMORIA, cero escrituras. Grafo simulado y veredictos POR COMPUTO.")
    print("=" * 78)

    reparto, linea_reparto = emparejamiento_declarado_de(op)
    if reparto is None:
        print("ROJO PREVIO: la ficha no declara su reparto de absorbidos de forma legible. "
              "Sin reparto no hay ficha ejecutada que simular.")
        return 1
    sups = sorted(reparto)
    print("EL REPARTO, LEIDO DE LA FICHA (no tecleado):")
    for s in sups:
        print("   %s absorbe %s" % (s, ", ".join(reparto[s])))
    print("   leido de: %s" % linea_reparto[:110])

    fallos_dir = []
    origen, destino = T._direccion_del_enlace(op, sups, fallos_dir)
    print("LA DIRECCION DEL ENLACE, LEIDA DE LA FICHA: %s -> %s (fallos: %d)"
          % (origen, destino, len(fallos_dir)))
    print("")

    resultados = []
    g_ejec = grafo_ejecutado(nodos, op, reparto, origen, destino)

    # ---- (i) LA CONTRAPRUEBA ----------------------------------------------
    cum_i, razon_i, fallos_i = celda_de(op, g_ejec)
    ok_i = cum_i is True and not fallos_i
    print("(i) CONTRAPRUEBA, ficha EJECUTADA sobre el grafo simulado:")
    print("     cumplido: %r | fallos: %d" % (cum_i, len(fallos_i)))
    print("     %s" % razon_i[:400])
    print("     VEREDICTO: %s" % ("OK" if ok_i else "ROJO"))
    resultados.append(("(i) ejecutada en memoria sale CUMPLIDA", ok_i))
    print("")

    # ---- (ii) UNA FUSION A MEDIAS -----------------------------------------
    # A medias = el absorbido esta en los ids_alias de su superviviente pero NO
    # esta deprecado. El sujeto se elige POR COMPUTO: el primer absorbido del
    # primer superviviente en orden.
    sup_roto = sups[0]
    absorbido_roto = sorted(reparto[sup_roto])[0]
    g_ii = copy.deepcopy(g_ejec)
    g_ii[absorbido_roto]["deprecado"] = False
    cum_ii, razon_ii, _ = celda_de(op, g_ii)
    nombra_ii = absorbido_roto in razon_ii and "NO esta deprecado" in razon_ii
    enlace_sigue = "el enlace CUMPLIDO" in razon_ii
    ok_ii = cum_ii is False and nombra_ii and enlace_sigue
    print("(ii) UNA FUSION A MEDIAS (%s sin deprecar, absorbido de %s):"
          % (absorbido_roto, sup_roto))
    print("     cumplido: %r" % cum_ii)
    print("     NOMBRA al absorbido y dice que no esta deprecado: %s" % nombra_ii)
    print("     y el enlace sigue CUMPLIDO (o sea que cae por la fusion): %s" % enlace_sigue)
    print("     %s" % razon_ii[:400])
    print("     VEREDICTO: %s" % ("OK" if ok_ii else "ROJO"))
    resultados.append(("(ii) fusion a medias, SIN CUMPLIR y la nombra", ok_ii))
    print("")

    # ---- (iii) EL ENLACE EN LA DIRECCION EQUIVOCADA -----------------------
    g_iii = copy.deepcopy(nodos)
    for sup, absorbidos in reparto.items():
        alias = list(g_iii[sup].get("ids_alias") or [])
        for x in absorbidos:
            g_iii[x]["deprecado"] = True
            if x not in alias:
                alias.append(x)
        g_iii[sup]["ids_alias"] = alias
    res_iii = T.resolver_de(g_iii)
    # la escalera se pone AL REVES: destino -> origen, y la buena no se pone.
    g_iii[origen]["nodos_siguientes"] = [y for y in (g_iii[origen].get("nodos_siguientes") or [])
                                         if res_iii(y) != destino]
    g_iii[destino]["nodos_previos"] = [y for y in (g_iii[destino].get("nodos_previos") or [])
                                       if res_iii(y) != origen]
    if destino not in (g_iii[destino].get("nodos_siguientes") or []):
        g_iii[destino].setdefault("nodos_siguientes", []).append(origen)
    g_iii[origen].setdefault("nodos_previos", []).append(destino)
    cum_iii, razon_iii, _ = celda_de(op, g_iii)
    cae_por_enlace = "el enlace SIN CUMPLIR" in razon_iii
    fusiones_bien = ("%d de %d fusiones con destino cumplido" % (len(sups), len(sups))) in razon_iii
    reparto_ok = "reparto de absorbidos OK" in razon_iii
    ok_iii = cum_iii is False and cae_por_enlace and fusiones_bien and reparto_ok
    print("(iii) EL ENLACE EN LA DIRECCION EQUIVOCADA (%s -> %s puesta, la buena no):"
          % (destino, origen))
    print("     cumplido: %r" % cum_iii)
    print("     cae POR EL ENLACE: %s | las dos fusiones siguen cumplidas: %s | reparto OK: %s"
          % (cae_por_enlace, fusiones_bien, reparto_ok))
    print("     %s" % razon_iii[:400])
    print("     VEREDICTO: %s" % ("OK" if ok_iii else "ROJO"))
    resultados.append(("(iii) enlace al reves, cae por el enlace", ok_iii))
    print("")

    # ---- (iv) SIN LA FRASE DE LA FIGURA -----------------------------------
    op_iv = json.loads(json.dumps(op))
    tipo = op_iv.get("tipo") or ""
    i = tipo.lower().find(T.FRASE_FIGURA_DOS_FUSIONES_UN_ENLACE)
    quito = i >= 0
    op_iv["tipo"] = (tipo[:i] + "MESA ADJUDICADA" + tipo[i + len(T.FRASE_FIGURA_DOS_FUSIONES_UN_ENLACE):]
                     if quito else tipo)
    sigue_siendo_mesa = T.es_mesa(op_iv)
    ya_no_declara = T.figura_declarada_de(op_iv) is None
    fila_iv = celda_de_la_tabla(op_iv, nodos, remisiones)
    vieja = razon_de_la_tabla_vieja(op.get("id_op"))
    misma_celda = vieja is not None and fila_iv is not None and fila_iv["razon"] == vieja
    ok_iv = (quito and sigue_siendo_mesa and ya_no_declara and fila_iv is not None
             and fila_iv["cumplido"] is None and fila_iv["vara"] == "MESA" and misma_celda)
    print("(iv) BORRADA LA FRASE DE LA FIGURA DEL `tipo`:")
    print("     la frase se quito de verdad: %s | sigue siendo MESA: %s | ya no declara "
          "figura: %s" % (quito, sigue_siendo_mesa, ya_no_declara))
    print("     vara: %r | cumplido: %r (NO COMPUTABLE es None)"
          % (fila_iv["vara"] if fila_iv else None, fila_iv["cumplido"] if fila_iv else None))
    print("     LA CELDA SALE IDENTICA A LA DE LA TABLA VIEJA (leida de %s): %s"
          % (os.path.basename(TABLA_ANTES), misma_celda))
    print("     celda de hoy : %s" % (fila_iv["razon"] if fila_iv else "(ninguna)"))
    print("     celda vieja  : %s" % (vieja or "(no se pudo leer del fichero)"))
    print("     VEREDICTO: %s" % ("OK" if ok_iv else "ROJO"))
    resultados.append(("(iv) sin la figura, vuelve a NO COMPUTABLE igual", ok_iv))
    print("")

    print("=" * 78)
    buenas = sum(1 for _, ok in resultados if ok)
    for nombre, ok in resultados:
        print("  %-48s %s" % (nombre, "OK" if ok else "ROJO"))
    sucio = T.subprocess.run(["git", "status", "--porcelain", "--", "dataset/", "docs/plan/"],
                             cwd=RAIZ, capture_output=True, text=True).stdout.strip()
    print("")
    print("P.16, dataset/ y docs/plan/ SIN TOCAR tras las mutaciones: %s" % (not sucio))
    if sucio:
        for ln in sucio.splitlines():
            print("   %s" % ln)
    print("")
    print("MUTACIONES QUE MUERDEN: %d de %d" % (buenas, len(resultados)))
    return 0 if buenas == len(resultados) and not sucio else 1


if __name__ == "__main__":
    raise SystemExit(main())
