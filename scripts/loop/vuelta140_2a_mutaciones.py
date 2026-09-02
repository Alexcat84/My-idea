# -*- coding: utf-8 -*-
r"""vuelta140_2a_mutaciones.py . LAS TRES PRUEBAS DE tallar_estado_de_fase.py
(TAREA 2.a de la vuelta 140, acta de la vuelta 139, escalada de la racha de
reporte en DOS).

TODAS LAS MUTACIONES SON EN MEMORIA. Este script NO escribe en el grafo, ni en
OPERACIONES.jsonl, ni en ningun fichero del plan. Solo escribe su propia
salida por stdout.

NINGUNA VARIABLE DE VEREDICTO ES UN LITERAL (EJECUTOR.md regla 1, "EL CASO
ROJO SE PRUEBA POR MUTACION"): las tres comparan cifras que el propio
instrumento acaba de computar, ANTES contra DESPUES, y ademas cada una lleva
su CONTRAPRUEBA (correr el mismo camino SIN mutar y comprobar que la cifra NO
se mueve), para que el caso pueda caer.

  (i)   SE LE QUITA UNA ARISTA PRESENTE AL GRAFO EN MEMORIA. La arista no se
        teclea: se elige computando cual de las de OP-M-01-ESLABONES esta
        presente hoy. Tiene que BAJAR "con destino cumplido" y la operacion
        tiene que salir NOMBRADA en la lista de las que no cumplen.
  (ii)  SE METE EN EL CATALOGO UNA REMITIDA DE MENTIRA que no existe en
        OPERACIONES.jsonl. Tiene que dar ROJO NOMBRANDOLA.
  (iii) CASO POSITIVO SOBRE SUJETO CONGELADO, no sobre el arbol de hoy: la
        fase 05, CERRADA CON REMISION desde la vuelta 136. El sujeto se clava
        POR SU COMMIT, e4464be5 (el acta 136 del auditor), y los CUATRO blobs
        que el instrumento lee se cotejan por sha256 en cada corrida: si el
        ancla se mueve, el caso cae con ANCLA PERDIDA y no con un verde
        (banco 9.10, y es la caida 4.2 del acta 139 puesta como guarda).

USO:
  python scripts/loop/vuelta140_2a_mutaciones.py
"""
import hashlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tallar_estado_de_fase as T  # noqa: E402

# EL ANCLA DEL CASO (iii): el commit del acta 136 del auditor, donde la fase 05
# quedo CERRADA CON REMISION. Clavado por hash, no por "el ultimo commit que
# toca X" (banco 9.10).
COMMIT_CONGELADO = "e4464be5"
SHA256_ESPERADOS = {
    "dataset/metadata/master_graph.json": "48dc4d393388eb2b0761309b03d35058db8b286eb242773d9b31f1c2e317e0d9",
    "docs/plan/OPERACIONES.jsonl": "1338bf8fee4315b2aa8e7092156d2cc69ace5dc00ec4f3c6685e4a97cd72ae3f",
    "docs/plan/00_INDICE.md": "0eb832bb8aba0bff71e5af93d3fe6cc44b8c4a956043c8d4f12f04f2fc8ec255",
    "docs/plan/04_ENLACES.md": "f64648029faf4361c61f16b83cbaa76f22de8bef84e3392fb1225391108af970",
}

FASE = "06_MESAS"
SUJETO_ENLACE = "OP-M-01-ESLABONES"


def cifra_de(fase, ops, nodos, remisiones):
    _, cifra, fallos = T.medir(fase, ops, nodos, remisiones=remisiones)
    return cifra, fallos


def copia_de_nodos(nodos):
    """Copia superficial con las DOS listas de vistas clonadas: es lo unico
    que la mutacion (i) toca."""
    copia = {}
    for nid, n in nodos.items():
        m = dict(n)
        m["nodos_siguientes"] = list(n.get("nodos_siguientes") or [])
        m["nodos_previos"] = list(n.get("nodos_previos") or [])
        copia[nid] = m
    return copia


def caso_i():
    print("=" * 78)
    print("(i) SE LE QUITA UNA ARISTA PRESENTE AL GRAFO EN MEMORIA")
    print("=" * 78)
    ops = T.cargar_ops("WORK")
    nodos = T.cargar_grafo("WORK")
    remisiones = T.leer_remisiones(FASE, "WORK")

    antes, fallos_antes = cifra_de(FASE, ops, nodos, remisiones)
    print("ANTES:  catalogo %d | cumplido %d | sin cumplir %d | sin vara %d"
          % (antes["catalogo"], antes["cumplido"], antes["sin_cumplir"], antes["sin_vara"]))
    print("        sin cumplir: %s" % ", ".join(antes["nombres_sin_cumplir"]))
    if fallos_antes:
        print("ARNES ROTO: el estado de partida ya trae fallos: %s" % fallos_antes)
        return 1

    # LA ARISTA NO SE TECLEA: se computa cual de las de SUJETO_ENLACE esta
    # presente hoy, con el mismo resolutor que usa el instrumento.
    op = [o for o in ops if o.get("id_op") == SUJETO_ENLACE][0]
    resolver = T.resolver_de(nodos)
    presentes = []
    for o, d in T.pares_de_aristas(op, []):
        ok, ro, rd = T.arista_presente(nodos, resolver, o, d)
        if ok:
            presentes.append((ro, rd))
    if not presentes:
        print("ARNES ROTO: %s no tiene ninguna arista presente que quitar" % SUJETO_ENLACE)
        return 1
    victima = presentes[0]
    print("ARISTA ELEGIDA POR COMPUTO (no tecleada): %s -> %s" % victima)

    mutado = copia_de_nodos(nodos)
    o, d = victima
    mutado[o]["nodos_siguientes"] = [x for x in mutado[o]["nodos_siguientes"]
                                     if resolver(x) != d]
    mutado[d]["nodos_previos"] = [x for x in mutado[d]["nodos_previos"]
                                  if resolver(x) != o]

    despues, _ = cifra_de(FASE, ops, mutado, remisiones)
    print("DESPUES: catalogo %d | cumplido %d | sin cumplir %d | sin vara %d"
          % (despues["catalogo"], despues["cumplido"], despues["sin_cumplir"], despues["sin_vara"]))
    print("        sin cumplir: %s" % ", ".join(despues["nombres_sin_cumplir"]))

    bajo = despues["cumplido"] < antes["cumplido"]
    nombrada = (SUJETO_ENLACE in despues["nombres_sin_cumplir"]
                and SUJETO_ENLACE not in antes["nombres_sin_cumplir"])
    print("LA CIFRA DE CUMPLIDO BAJA: %s (%d -> %d)" % (bajo, antes["cumplido"], despues["cumplido"]))
    print("LA OPERACION SALE NOMBRADA: %s" % nombrada)

    # CONTRAPRUEBA: el mismo camino SIN quitar nada. Si esto tambien "bajara",
    # el caso no probaria nada.
    testigo = copia_de_nodos(nodos)
    control, _ = cifra_de(FASE, ops, testigo, remisiones)
    quieto = control["cumplido"] == antes["cumplido"]
    print("CONTRAPRUEBA (copia SIN mutar): cumplido %d, se queda quieto: %s"
          % (control["cumplido"], quieto))

    ok = bajo and nombrada and quieto
    print("VEREDICTO (i): %s" % ("VERDE" if ok else "ROJO"))
    return 0 if ok else 1


def caso_ii():
    print("")
    print("=" * 78)
    print("(ii) UNA REMITIDA DE MENTIRA QUE NO EXISTE EN OPERACIONES.jsonl")
    print("=" * 78)
    ops = T.cargar_ops("WORK")
    nodos = T.cargar_grafo("WORK")
    remisiones = T.leer_remisiones(FASE, "WORK")

    _, fallos_limpio = cifra_de(FASE, ops, nodos, dict(remisiones))
    print("SIN MUTAR: %d fallo(s)" % len(fallos_limpio))

    inventada = "OP-Z-99-FANTASMA"
    presente_en_fichero = any(o.get("id_op") == inventada for o in ops)
    print("EL ID INVENTADO EXISTE EN OPERACIONES.jsonl: %s (computado)" % presente_en_fichero)
    if presente_en_fichero:
        print("ARNES ROTO: el id de mentira existe de verdad; el caso no probaria nada")
        return 1

    sucias = dict(remisiones)
    sucias[inventada] = {"de": None, "a": "OP-M-01", "fuente": "MUTACION EN MEMORIA"}
    _, fallos = cifra_de(FASE, ops, nodos, sucias)
    print("MUTADO: %d fallo(s)" % len(fallos))
    for x in fallos:
        print("   %s" % x)

    nombrada = any(inventada in x for x in fallos)
    subio = len(fallos) > len(fallos_limpio)
    print("ROJO Y LA NOMBRA: %s" % nombrada)
    print("CONTRAPRUEBA (sin mutar no hay fallo nuevo): %s" % subio)
    ok = nombrada and subio and not fallos_limpio
    print("VEREDICTO (ii): %s" % ("VERDE" if ok else "ROJO"))
    return 0 if ok else 1


def caso_iii():
    print("")
    print("=" * 78)
    print("(iii) CASO POSITIVO SOBRE SUJETO CONGELADO: LA FASE 05, CERRADA EN LA VUELTA 136")
    print("=" * 78)
    print("SUJETO CLAVADO POR COMMIT: %s (acta 136 del auditor)" % COMMIT_CONGELADO)
    perdidas = []
    for rel, esperado in sorted(SHA256_ESPERADOS.items()):
        datos = T.leer_ruta(COMMIT_CONGELADO, rel).encode("utf-8")
        real = hashlib.sha256(datos).hexdigest()
        estado = "OK" if real == esperado else "ANCLA PERDIDA"
        if real != esperado:
            perdidas.append(rel)
        print("   %-40s %s  %s" % (rel, real[:16], estado))
    if perdidas:
        print("ROJO, ANCLA PERDIDA en %d fichero(s): %s" % (len(perdidas), ", ".join(perdidas)))
        return 1

    ops = T.cargar_ops(COMMIT_CONGELADO)
    nodos = T.cargar_grafo(COMMIT_CONGELADO)
    lista, cifra, fallos = T.medir("05_SANEO", ops, nodos, ref=COMMIT_CONGELADO)
    T.imprimir("05_SANEO", lista, cifra, fallos, ref=COMMIT_CONGELADO)

    esperado_cumplido = cifra["catalogo"] - 1
    esperado_sin = ["OP-S-12"]
    print("")
    print("LO QUE EL ENCARGO ESPERA: catalogo %d con destino cumplido SALVO OP-S-12, "
          "o sea cumplido %d y sin cumplir exactamente %s"
          % (cifra["catalogo"], esperado_cumplido, esperado_sin))
    print("LO QUE SALE:              cumplido %d y sin cumplir %s"
          % (cifra["cumplido"], cifra["nombres_sin_cumplir"]))
    calza = (cifra["cumplido"] == esperado_cumplido
             and cifra["nombres_sin_cumplir"] == esperado_sin)
    print("CALZA CON LO ESPERADO: %s" % calza)

    # LA EVIDENCIA DE POR QUE NO PUEDE CALZAR, COMPUTADA Y NO TECLEADA: cuantas
    # operaciones del catalogo son INDISTINGUIBLES entre si mirando solo el
    # grafo, y si OP-S-12 esta entre ellas.
    por_id = {o["id_op"]: o for o in ops}
    def huella(o):
        return (tuple(o.get("nodos") or []), o.get("superviviente"),
                tuple(o.get("aristas_nuevas") or []), tuple(o.get("eliminar") or []))
    grupos = {}
    for f in lista:
        grupos.setdefault(huella(por_id[f["id_op"]]), []).append(f["id_op"])
    gemelas = [g for g in grupos.values() if len(g) > 1]
    print("")
    print("POR QUE NO CALZA, MEDIDO Y NO OPINADO:")
    print("   grupos de operaciones con HUELLA DE GRAFO IDENTICA (nodos, superviviente,")
    print("   aristas_nuevas y eliminar, los cuatro campos con los que el grafo se mide): %d"
          % len(gemelas))
    for g in gemelas:
        print("      %s" % ", ".join(sorted(g)))
    con_op_s_12 = [g for g in gemelas if "OP-S-12" in g]
    print("   OP-S-12 comparte huella con otras %d operacion(es) del catalogo: %s"
          % (len(con_op_s_12[0]) - 1 if con_op_s_12 else 0,
             ", ".join(sorted(x for x in (con_op_s_12[0] if con_op_s_12 else []) if x != "OP-S-12")) or "ninguna"))
    print("   NINGUNA VARA DE GRAFO PUEDE SEPARARLAS: %s" % bool(con_op_s_12))
    print("   Lo unico que las separa es el campo `estado`, y el encargo dice")
    print("   expresamente que el destino se mide CONTRA EL GRAFO, NO CONTRA `estado`.")
    print("")
    print("VEREDICTO (iii): %s" % ("VERDE" if calza else "NO CALZA, SE DICE Y SE PARA ESTE CASO"))
    return 0 if calza else 2


def main():
    r1 = caso_i()
    r2 = caso_ii()
    r3 = caso_iii()
    print("")
    print("=" * 78)
    print("RESUMEN: (i) %s | (ii) %s | (iii) %s"
          % ("VERDE" if r1 == 0 else "ROJO",
             "VERDE" if r2 == 0 else "ROJO",
             "VERDE" if r3 == 0 else ("NO CALZA" if r3 == 2 else "ROJO")))
    print("=" * 78)
    return max(r1, r2, r3)


if __name__ == "__main__":
    raise SystemExit(main())
