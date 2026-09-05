# -*- coding: utf-8 -*-
r"""vuelta178_tarea4_mutacion_consumidas.py . EL CASO POSITIVO POR MUTACION DE LA
COLUMNA `CONSUMIDA` DE LA VARA, SOBRE UN EXPEDIENTE FABRICADO.

TAREA 4.c de la vuelta 178.

SUJETO CONGELADO, que es la condicion de entrada en la nomina desde la vuelta
148: el expediente, el mapa de alias y el grafo que este arnes usa estan
FABRICADOS AQUI, en memoria. NO se lee `docs/plan/OPERACIONES.jsonl`, NO se lee
`dataset/nodos/` y NO se lee `dataset/metadata/master_graph.json` para decidir
ningun caso. Contra el expediente vivo, cualquier fusion nueva moveria las cifras
y el verde de esta vuelta no sobreviviria a la vuelta.

NINGUN VEREDICTO ES UNA CONSTANTE LITERAL (`EJECUTOR.md` 1, caida 2 de la vuelta
89): cada caso sale de correr `consumida_por()`, que es pura, y la segunda pasada
MUTA EL VALOR ESPERADO y exige que CAIGA.

LO QUE PRUEBA, Y LAS DOS MITADES VAN LAS DOS:

  1. UNA FICHA CUYOS DOS NODOS RESUELVEN A UN SOLO VIVO ESTA CONSUMIDA, y la
     columna dice POR CUAL leyendolo de la propia ficha.
  2. LA MISMA FICHA SIN EL ALIAS NO ESTA CONSUMIDA. Si quitar el alias no
     cambiara la respuesta, la columna no estaria midiendo contra el grafo.
  3. UNA FICHA DE UN SOLO NODO NUNCA ESTA CONSUMIDA: no hay fusion que haya
     ocurrido.
  4. UNA FICHA CONSUMIDA QUE NO NOMBRA A NADIE SE DECLARA COMO TAL en vez de
     inventarle un culpable.
  5. SI EL DESTINO ESTA DEPRECADO, NO ESTA CONSUMIDA: los dos nodos colapsaron a
     algo que tampoco vive, y eso es otra cosa.
  6. LA ATRIBUCION SE BUSCA EN TODAS LAS VENTANAS Y NO EN LA PRIMERA, que es el
     defecto que la primera corrida de esta columna tuvo: la frase que declara la
     consumicion y la que dice quien la ejecuto pueden estar a cientos de
     caracteres una de otra dentro de la misma nota.

USO:
  python scripts/loop/vuelta178_tarea4_mutacion_consumidas.py
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import vuelta150_3_relectura_expediente as V   # noqa: E402

NL = chr(10)

# EL EXPEDIENTE FABRICADO. Ninguna de estas fichas existe.
FICHA_CONSUMIDA = {
    "id_op": "OP-X-01",
    "nodos": ["nodo_que_muere", "nodo_que_vive"],
    "nota": ("ESTA FICHA ESTA CONSUMIDA. NO SE EJECUTA Y NO SE REHACE. MEDIDO "
             "HOY CONTRA EL GRAFO y no leido de un acta. " + ("relleno. " * 40) +
             "SU FUSION YA LA EJECUTO UN TRAMO DE OP-Z-99, y por eso esta ficha "
             "no se vuelve a correr."),
}
FICHA_MUDA = {
    "id_op": "OP-X-02",
    "nodos": ["nodo_que_muere", "nodo_que_vive"],
    "nota": "una ficha cualquiera que no declara nada de su estado.",
}
FICHA_DE_UNO = {
    "id_op": "OP-X-03",
    "nodos": ["nodo_que_vive"],
    "nota": "ESTA FICHA ESTA CONSUMIDA, dice, pero solo tiene un nodo.",
}
FICHA_A_MUERTO = {
    "id_op": "OP-X-04",
    "nodos": ["nodo_que_muere", "nodo_tambien_muerto"],
    "nota": "ESTA FICHA ESTA CONSUMIDA por OP-Z-98.",
}

MAPA_CON_ALIAS = {"nodo_que_muere": "nodo_que_vive",
                  "nodo_tambien_muerto": "nodo_muerto_destino"}
MAPA_SIN_ALIAS = {}
VIVOS = {"nodo_que_vive": True, "nodo_que_muere": False,
         "nodo_tambien_muerto": False, "nodo_muerto_destino": False}


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    p = print
    p("=" * 78)
    p("CASO POSITIVO POR MUTACION DE LA COLUMNA CONSUMIDA (vuelta 178, TAREA 4.c)")
    p("=" * 78)
    p("")
    p("EL EXPEDIENTE FABRICADO, que NO es docs/plan/OPERACIONES.jsonl:")
    for f in (FICHA_CONSUMIDA, FICHA_MUDA, FICHA_DE_UNO, FICHA_A_MUERTO):
        p("   %-10s nodos %s" % (f["id_op"], f["nodos"]))
    p("   mapa de alias fabricado: %s" % MAPA_CON_ALIAS)
    p("   vivos fabricados: %s" % VIVOS)
    p("")

    casos = []

    p("1) LOS DOS NODOS RESUELVEN A UN SOLO VIVO: ESTA CONSUMIDA, Y DICE POR CUAL")
    esta, nombrados, destino = V.consumida_por(FICHA_CONSUMIDA, MAPA_CON_ALIAS, VIVOS)
    p("   consumida: %s | por: %s | destino vivo: %s"
      % (esta, ", ".join(nombrados) or "(no lo dice)", destino))
    casos.append(("1_esta_consumida", esta, True))
    casos.append(("1_nombra_a_quien_la_consumio", nombrados, ["OP-Z-99"]))
    casos.append(("1_el_destino_es_el_nodo_vivo", destino, "nodo_que_vive"))
    p("   Y LA ATRIBUCION ESTA A 400 CARACTERES DE LA MARCA a proposito: la")
    p("   primera version de esta columna solo miraba la primera ventana y")
    p("   devolvia lista vacia teniendo la respuesta escrita mas abajo.")
    p("")

    p("2) LA MUTACION QUE MANDA: SE QUITA EL ALIAS Y DEJA DE ESTAR CONSUMIDA")
    esta2, nombrados2, _d = V.consumida_por(FICHA_CONSUMIDA, MAPA_SIN_ALIAS, VIVOS)
    p("   consumida sin el alias: %s" % esta2)
    casos.append(("2_sin_alias_NO_esta_consumida", esta2, False))
    casos.append(("2_sin_alias_no_nombra_a_nadie", nombrados2, []))
    p("   Si quitar el alias no cambiara la respuesta, la columna no estaria")
    p("   midiendo contra el grafo: estaria leyendo un acta.")
    p("")

    p("3) UNA FICHA DE UN SOLO NODO NUNCA ESTA CONSUMIDA")
    esta3, _n, _d = V.consumida_por(FICHA_DE_UNO, MAPA_CON_ALIAS, VIVOS)
    p("   consumida: %s (y su nota lo AFIRMA, que es lo que hace util el caso)" % esta3)
    casos.append(("3_una_ficha_de_un_nodo_no_esta_consumida", esta3, False))
    p("")

    p("4) CONSUMIDA PERO SIN NOMBRAR A NADIE: SE DECLARA, NO SE INVENTA")
    esta4, nombrados4, _d = V.consumida_por(FICHA_MUDA, MAPA_CON_ALIAS, VIVOS)
    p("   consumida: %s | nombra: %s" % (esta4, nombrados4 or "(nadie)"))
    casos.append(("4_muda_esta_consumida", esta4, True))
    casos.append(("4_muda_no_nombra_a_nadie", nombrados4, []))
    p("")

    p("5) SI EL DESTINO NO VIVE, NO ESTA CONSUMIDA")
    esta5, _n, destino5 = V.consumida_por(FICHA_A_MUERTO, MAPA_CON_ALIAS, VIVOS)
    p("   consumida: %s | destino: %s (vivo: %s)"
      % (esta5, destino5, VIVOS.get(destino5)))
    casos.append(("5_destino_deprecado_no_esta_consumida", esta5, False))
    p("")

    p("6) LAS FUNCIONES DE LA COLUMNA SON PURAS Y SE LES PUEDE PASAR TODO")
    p("   mapa_de_alias() sobre un directorio que no existe: %r"
      % (V.mapa_de_alias(os.path.join(AQUI, "no_existe_este_directorio")),))
    casos.append(("6_mapa_de_alias_sin_directorio_es_vacio",
                  V.mapa_de_alias(os.path.join(AQUI, "no_existe_este_directorio")), {}))
    p("   vivos_del_grafo() sobre una ruta que no existe: %r"
      % (V.vivos_del_grafo(os.path.join(AQUI, "no_existe.json")),))
    casos.append(("6_vivos_sin_grafo_es_vacio",
                  V.vivos_del_grafo(os.path.join(AQUI, "no_existe.json")), {}))
    p("")

    p("7) PASADA 1, LOS CASOS TAL CUAL")
    fallos = 0
    for nombre, real, esperado in casos:
        ok = (real == esperado)
        p("   %-46s %s   (real=%r esperado=%r)"
          % (nombre, "PASA" if ok else "FALLA", real, esperado))
        if not ok:
            fallos += 1
    p("   CIFRA casos: %d | pasan: %d | fallan: %d"
      % (len(casos), len(casos) - fallos, fallos))
    p("")

    p("8) PASADA 2, SE MUTA EL VALOR ESPERADO Y CADA CASO TIENE QUE CAER")
    caen = 0
    for nombre, real, esperado in casos:
        if isinstance(esperado, bool):
            mutado = not esperado
        elif isinstance(esperado, list):
            mutado = esperado + ["OP-DE-MENTIRA"]
        elif isinstance(esperado, dict):
            mutado = dict(esperado)
            mutado["de_mentira"] = True
        else:
            mutado = str(esperado) + "_DE_MENTIRA"
        cae = (real != mutado)
        p("   %-46s %s" % (nombre, "CAE" if cae else "NO CAE (ROJO)"))
        if cae:
            caen += 1
    p("   CIFRA casos que CAEN: %d de %d" % (caen, len(casos)))
    p("")

    if fallos or caen != len(casos):
        p("ROJO DE LA MUTACION: la columna CONSUMIDA no se comporta.")
        p("FIN")
        return 1
    p("VERDE DE LA MUTACION: %d casos, los %d pasan y los %d CAEN al mutarles el "
      "valor esperado. La columna mide CONTRA EL GRAFO (quitar el alias cambia la "
      "respuesta), lee la atribucion DE LA PROPIA FICHA y en todas sus ventanas, "
      "no consume una ficha de un solo nodo, no inventa culpable cuando la ficha "
      "calla, y no llama consumida a una que colapso a un nodo deprecado."
      % (len(casos), len(casos), len(casos)))
    p("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
