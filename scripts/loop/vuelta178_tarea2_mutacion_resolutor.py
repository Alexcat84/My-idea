# -*- coding: utf-8 -*-
r"""vuelta178_tarea2_mutacion_resolutor.py . EL CASO POSITIVO POR MUTACION DE
`backlog_l03_resuelto.py`, SOBRE UN MAPA DE ALIAS FABRICADO.

TAREA 2.e de la vuelta 178. La letra del encargo se cita: "un acto cuyos
miembros colapsan a uno tiene que dar CERO pares reales, y si le quitas el alias
tiene que volver a darlos. Si esa mutacion no hace caer nada, el resolutor no
esta puesto de verdad."

SUJETO CONGELADO, que es la condicion de entrada en la nomina desde la vuelta
148: el mapa de alias, el grafo y los veredictos que este arnes usa estan
FABRICADOS AQUI, en memoria. NO se lee `dataset/nodos/`, NO se lee
`dataset/metadata/master_graph.json` y NO se lee
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` para decidir ningun caso. Es lo unico que
hace que el verde de esta vuelta sobreviva a la vuelta siguiente: contra el mapa
vivo, cualquier fusion nueva moveria las cifras y este arnes se volveria rojo sin
que nada estuviera roto.

NINGUN VEREDICTO ES UNA CONSTANTE LITERAL (`EJECUTOR.md` 1, caida 2 de la vuelta
89): cada caso sale de correr `medir_acto()`, que es pura, y la segunda pasada
MUTA EL VALOR ESPERADO y exige que CAIGA.

LA MUTACION QUE MANDA ES LA DEL ALIAS, Y VA EN LOS DOS SENTIDOS:
  CON el alias puesto, los tres miembros del acto colapsan a uno y los tres
  pares salen DISUELTOS: cero pares reales.
  SIN el alias, los tres miembros son tres nodos distintos y los tres pares
  VUELVEN. Si quitar el alias no cambiara la cifra, el resolutor no estaria
  haciendo nada y este instrumento seria un `combinations()` con adornos.

USO:
  python scripts/loop/vuelta178_tarea2_mutacion_resolutor.py
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import backlog_l03_resuelto as B   # noqa: E402

NL = chr(10)

# EL ACTO FABRICADO. Tres miembros que en el mapa CON alias son el mismo nodo.
ACTO = ["nodo_madre", "nodo_alias_uno", "nodo_alias_dos"]
MAPA_CON_ALIAS = {"nodo_alias_uno": "nodo_madre", "nodo_alias_dos": "nodo_madre"}
MAPA_SIN_ALIAS = {}

# UN SEGUNDO ACTO donde solo DOS de los tres colapsan, para que la cifra no sea
# de todo o nada: tiene que quedar exactamente UN par real.
ACTO_2 = ["otra_madre", "otra_alias", "tercero_vivo"]
MAPA_PARCIAL = {"otra_alias": "otra_madre"}

GRAFO_VIVO = {"nodo_madre": {"deprecado": False},
              "nodo_alias_uno": {"deprecado": True},
              "nodo_alias_dos": {"deprecado": True},
              "otra_madre": {"deprecado": False},
              "otra_alias": {"deprecado": True},
              "tercero_vivo": {"deprecado": False}}

# EL GRAFO QUE MIENTE, para probar que el ROJO de los dos caminos MUERDE: aqui
# `nodo_alias_uno` figura VIVO aunque el resolutor lo mande a `nodo_madre`.
GRAFO_QUE_MIENTE = dict(GRAFO_VIVO)
GRAFO_QUE_MIENTE["nodo_alias_uno"] = {"deprecado": False}

# LOS VEREDICTOS FABRICADOS. Uno solo, y sobre el par RESUELTO del acto 2.
VEREDICTOS = [{"nodo_a": "otra_alias", "nodo_b": "tercero_vivo", "clase": "D"}]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    p = print
    p("=" * 78)
    p("CASO POSITIVO POR MUTACION DEL RESOLUTOR (vuelta 178, TAREA 2.e)")
    p("=" * 78)
    p("")
    p("EL MATERIAL, TODO FABRICADO Y NADA LEIDO DEL REPO:")
    p("   acto 1:      %s" % ", ".join(ACTO))
    p("   mapa CON alias: %s" % MAPA_CON_ALIAS)
    p("   acto 2:      %s" % ", ".join(ACTO_2))
    p("   mapa parcial:   %s" % MAPA_PARCIAL)
    p("")

    casos = []
    vivos = B.vivos_por_grafo(GRAFO_VIVO)

    p("A) CON EL ALIAS PUESTO, EL ACTO COLAPSA A UNO Y NO QUEDA NINGUN PAR REAL")
    idx_vacio = B.veredictos_por_par(MAPA_CON_ALIAS, [])
    m1 = B.medir_acto(ACTO, 3, MAPA_CON_ALIAS, vivos, idx_vacio)
    p("   vivos por resolutor: %d (%s)"
      % (m1["cifra_vivos_por_resolutor"], ", ".join(m1["vivos_por_resolutor"])))
    p("   vivos por grafo:     %d (%s)"
      % (m1["cifra_vivos_por_grafo"], ", ".join(m1["vivos_por_grafo"])))
    p("   los dos caminos calzan: %s" % m1["los_dos_caminos_calzan"])
    p("   pares del instrumento: %d | reales: %d | disueltos: %d"
      % (m1["pares_del_instrumento"], m1["cifra_pares_reales"],
         m1["cifra_pares_disueltos"]))
    casos.append(("A_con_alias_CERO_pares_reales", m1["cifra_pares_reales"], 0))
    casos.append(("A_con_alias_los_TRES_disueltos", m1["cifra_pares_disueltos"], 3))
    casos.append(("A_con_alias_UN_solo_vivo", m1["cifra_vivos_por_resolutor"], 1))
    casos.append(("A_con_alias_los_dos_caminos_calzan",
                  m1["los_dos_caminos_calzan"], True))
    p("")

    p("B) LA MUTACION QUE MANDA: SE QUITA EL ALIAS Y LOS PARES TIENEN QUE VOLVER")
    vivos_sin = B.vivos_por_grafo(
        dict((k, {"deprecado": False}) for k in ACTO))
    idx_vacio2 = B.veredictos_por_par(MAPA_SIN_ALIAS, [])
    m2 = B.medir_acto(ACTO, 3, MAPA_SIN_ALIAS, vivos_sin, idx_vacio2)
    p("   vivos por resolutor: %d" % m2["cifra_vivos_por_resolutor"])
    p("   pares reales: %d | disueltos: %d"
      % (m2["cifra_pares_reales"], m2["cifra_pares_disueltos"]))
    casos.append(("B_sin_alias_VUELVEN_los_tres_pares", m2["cifra_pares_reales"], 3))
    casos.append(("B_sin_alias_CERO_disueltos", m2["cifra_pares_disueltos"], 0))
    casos.append(("B_sin_alias_TRES_vivos", m2["cifra_vivos_por_resolutor"], 3))
    p("   LO QUE ESTA MUTACION PRUEBA: quitar el alias cambia la cifra de 0 a 3.")
    p("   Si no la cambiara, el resolutor no estaria puesto y este instrumento")
    p("   seria un combinations() con adornos.")
    p("")

    p("C) UN ACTO DONDE SOLO DOS DE TRES COLAPSAN, PARA QUE NO SEA TODO O NADA")
    idx3 = B.veredictos_por_par(MAPA_PARCIAL, [])
    m3 = B.medir_acto(ACTO_2, 3, MAPA_PARCIAL, vivos, idx3)
    p("   vivos por resolutor: %d (%s)"
      % (m3["cifra_vivos_por_resolutor"], ", ".join(m3["vivos_por_resolutor"])))
    p("   pares reales: %d | disueltos: %d"
      % (m3["cifra_pares_reales"], m3["cifra_pares_disueltos"]))
    casos.append(("C_parcial_UN_par_real", m3["cifra_pares_reales"], 1))
    casos.append(("C_parcial_UN_par_disuelto", m3["cifra_pares_disueltos"], 1))
    p("")

    p("D) EL VEREDICTO SE BUSCA POR EL PAR RESUELTO, QUE ES P.1 SIN EXCEPCION")
    p("   el veredicto fabricado esta escrito con `otra_alias`, que resuelve a")
    p("   `otra_madre`. Si se buscara por el id ESCRITO, el par saldria como real.")
    idx4 = B.veredictos_por_par(MAPA_PARCIAL, VEREDICTOS)
    m4 = B.medir_acto(ACTO_2, 3, MAPA_PARCIAL, vivos, idx4)
    p("   pares reales con el veredicto puesto: %d" % m4["cifra_pares_reales"])
    p("   pares con veredicto: %d" % m4["cifra_pares_con_veredicto"])
    casos.append(("D_el_veredicto_resuelto_baja_el_par_real",
                  m4["cifra_pares_reales"], 0))
    casos.append(("D_lo_cuenta_como_par_con_veredicto",
                  m4["cifra_pares_con_veredicto"], 1))
    p("")

    p("E) EL ROJO DE LOS DOS CAMINOS MUERDE: SE LE DA UN GRAFO QUE MIENTE")
    vivos_mentira = B.vivos_por_grafo(GRAFO_QUE_MIENTE)
    m5 = B.medir_acto(ACTO, 3, MAPA_CON_ALIAS, vivos_mentira, idx_vacio)
    p("   vivos por resolutor: %d | vivos por grafo: %d | calzan: %s"
      % (m5["cifra_vivos_por_resolutor"], m5["cifra_vivos_por_grafo"],
         m5["los_dos_caminos_calzan"]))
    casos.append(("E_con_el_grafo_que_miente_NO_calzan",
                  m5["los_dos_caminos_calzan"], False))
    p("   Si esta fila saliera SI, la comprobacion de los dos caminos seria un")
    p("   adorno: diria que calzan pase lo que pase.")
    p("")

    p("F) PASADA 1, LOS CASOS TAL CUAL")
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

    p("G) PASADA 2, SE MUTA EL VALOR ESPERADO Y CADA CASO TIENE QUE CAER")
    caen = 0
    for nombre, real, esperado in casos:
        mutado = (not esperado) if isinstance(esperado, bool) else esperado + 1
        cae = (real != mutado)
        p("   %-46s %s" % (nombre, "CAE" if cae else "NO CAE (ROJO)"))
        if cae:
            caen += 1
    p("   CIFRA casos que CAEN: %d de %d" % (caen, len(casos)))
    p("")

    if fallos or caen != len(casos):
        p("ROJO DE LA MUTACION: el resolutor no esta puesto de verdad.")
        p("FIN")
        return 1
    p("VERDE DE LA MUTACION: %d casos, los %d pasan y los %d CAEN al mutarles el "
      "valor esperado. CON el alias el acto colapsa a uno y da CERO pares reales; "
      "QUITADO el alias los tres pares VUELVEN; un colapso parcial deja "
      "exactamente uno; el veredicto se busca por el par RESUELTO y no por el id "
      "escrito; y la comprobacion de los dos caminos MUERDE cuando el grafo "
      "contradice al resolutor." % (len(casos), len(casos), len(casos)))
    p("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
