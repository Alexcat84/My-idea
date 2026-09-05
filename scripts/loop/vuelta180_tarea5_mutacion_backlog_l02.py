# -*- coding: utf-8 -*-
r"""vuelta180_tarea5_mutacion_backlog_l02.py . EL CASO POSITIVO POR MUTACION DE
`backlog_l02_resuelto.py`: SI EL RESOLUTOR NO ESTA PUESTO, O SI LOS PARES SE
CUENTAN COMO ESCRITOS Y NO COMO RESUELTOS, ESTE CASO CAE.

TAREA 5 de la vuelta 180. Sujeto: `medir_nomina()` de
`scripts/loop/backlog_l02_resuelto.py`, que es PURA y recibe el mapa de alias, el
diccionario de vivos, el indice de veredictos y el de lecturas dirigidas.

SUJETO CONGELADO, y se dice como: **todo el material va FABRICADO aqui dentro**.
Mapa de alias fabricado, grafo fabricado, veredictos fabricados y lecturas
dirigidas fabricadas. **No lee el archivo, ni el grafo, ni `docs/plan/`, ni
`dataset/`.** El unico fichero que se toca es este.

POR QUE EL CASO C ES EL QUE IMPORTA, Y LO ES PORQUE YA MORDIO HOY. La primera
corrida de `backlog_l02_resuelto.py` salio **en ROJO por su propia guarda de
restas**: contaba los pares ESCRITOS y no los DISTINTOS TRAS RESOLVER, y dos
parejas de miembros escritas distintas pueden resolver AL MISMO par. Es la misma
trampa que `backlog_l03_resuelto.py` declara en su `medir_acto()` y que le mordio
en su primera corrida. **Aqui queda con arnes.**

LOS CASOS, Y TODOS CORREN:

  (A) UNA NOMINA CUYOS MIEMBROS COLAPSAN A UNO da CERO pares reales, y todos sus
      pares salen como DISUELTOS.
  (B) LA CONTRAPRUEBA: quitandole el alias, los pares vuelven. Sin esto, (A) no
      distinguiria un resolutor puesto de una funcion que devuelve cero siempre.
  (C) DOS PAREJAS ESCRITAS QUE RESUELVEN AL MISMO PAR SE CUENTAN UNA VEZ, y la
      identidad `distintos = con veredicto + reales contra el archivo` se
      cumple.
  (D) UN PAR CON VEREDICTO EN EL ARCHIVO no es real; sin el veredicto, si lo es.
  (E) UN PAR CON LECTURA DIRIGIDA sigue siendo real CONTRA EL ARCHIVO y deja de
      serlo CONTRA LAS DOS SEDES. **Las dos columnas dicen cosas distintas y por
      eso van las dos.**
  (F) LOS DOS CAMINOS: si el grafo y el resolutor discrepan, `los_dos_caminos_calzan`
      sale False. Es lo que enciende el rojo del instrumento.

USO:
  python scripts/loop/vuelta180_tarea5_mutacion_backlog_l02.py
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import backlog_l02_resuelto as L2   # noqa: E402

# EL MATERIAL FABRICADO. Ni un id de la campana.
NOMINA = ["nodo_uno", "nodo_dos", "nodo_tres", "nodo_cuatro"]
VIVOS_TODOS = dict((n, True) for n in NOMINA)


def par(a, b):
    return frozenset((a, b))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    p = print
    fallos = []

    def marcar(etiqueta, ok, detalle=""):
        p("   %-66s %s" % (etiqueta, "SI" if ok else "NO"))
        if detalle:
            p("      %s" % detalle)
        if not ok:
            fallos.append(etiqueta)

    p("=" * 78)
    p("CASO POSITIVO POR MUTACION DE backlog_l02_resuelto (vuelta 180, TAREA 5)")
    p("=" * 78)
    p("")
    p("TODO EL MATERIAL VA FABRICADO: nomina de %d miembros de mentira, mapa de"
      % len(NOMINA))
    p("alias fabricado, veredictos fabricados y lecturas dirigidas fabricadas.")
    p("NO SE LEE NI EL ARCHIVO, NI EL GRAFO, NI docs/plan/, NI dataset/.")
    p("")

    p("(A) UNA NOMINA QUE COLAPSA A UN SOLO NODO DA CERO PARES REALES")
    mapa_colapso = {"nodo_dos": "nodo_uno", "nodo_tres": "nodo_uno",
                    "nodo_cuatro": "nodo_uno"}
    m = L2.medir_nomina(NOMINA, mapa_colapso, {"nodo_uno": True}, {}, {})
    p("      pares del instrumento: %d | disueltos: %d | distintos: %d | reales: %d"
      % (m["cifra_pares_del_instrumento"], m["cifra_pares_disueltos"],
         m["cifra_pares_distintos_tras_resolver"], m["cifra_reales_contra_el_archivo"]))
    marcar("A: cero pares reales", m["cifra_reales_contra_el_archivo"] == 0)
    marcar("A: y los seis pares escritos salen como DISUELTOS",
           m["cifra_pares_disueltos"] == 6)
    marcar("A: y cero distintos tras resolver",
           m["cifra_pares_distintos_tras_resolver"] == 0)
    p("")

    p("(B) LA CONTRAPRUEBA: SIN EL ALIAS, LOS PARES VUELVEN")
    m2 = L2.medir_nomina(NOMINA, {}, VIVOS_TODOS, {}, {})
    p("      pares del instrumento: %d | disueltos: %d | distintos: %d | reales: %d"
      % (m2["cifra_pares_del_instrumento"], m2["cifra_pares_disueltos"],
         m2["cifra_pares_distintos_tras_resolver"],
         m2["cifra_reales_contra_el_archivo"]))
    marcar("B: sin alias, los seis pares son reales",
           m2["cifra_reales_contra_el_archivo"] == 6)
    marcar("B: y cero disueltos", m2["cifra_pares_disueltos"] == 0)
    p("")

    p("(C) EL CASO QUE MORDIO HOY: DOS PAREJAS ESCRITAS QUE SON UN SOLO PAR")
    p("    `nodo_dos` es alias de `nodo_uno`, asi que (uno,tres) y (dos,tres) son")
    p("    EL MISMO par una vez resueltos, y hay UNA lectura que hacer, no dos.")
    mapa_dup = {"nodo_dos": "nodo_uno"}
    vivos_dup = {"nodo_uno": True, "nodo_tres": True, "nodo_cuatro": True}
    m3 = L2.medir_nomina(NOMINA, mapa_dup, vivos_dup, {}, {})
    p("      pares del instrumento: %d | disueltos: %d | DISTINTOS: %d | reales: %d"
      % (m3["cifra_pares_del_instrumento"], m3["cifra_pares_disueltos"],
         m3["cifra_pares_distintos_tras_resolver"],
         m3["cifra_reales_contra_el_archivo"]))
    marcar("C: los 6 escritos menos 1 disuelto dejan 5 escritos",
           m3["cifra_pares_del_instrumento"] - m3["cifra_pares_disueltos"] == 5)
    marcar("C: pero los DISTINTOS tras resolver son 3, no 5",
           m3["cifra_pares_distintos_tras_resolver"] == 3)
    marcar("C: y los reales son 3, o sea los distintos y no los escritos",
           m3["cifra_reales_contra_el_archivo"] == 3)
    marcar("C: LA IDENTIDAD distintos = con veredicto + reales contra el archivo",
           (m3["cifra_pares_distintos_tras_resolver"]
            == m3["cifra_pares_con_veredicto"] + m3["cifra_reales_contra_el_archivo"]))
    p("      LA MUTACION DE ESTE CASO: si se contaran los ESCRITOS, la identidad")
    p("      daria 5 = 0 mas 5 y el instrumento publicaria 5 lecturas que hacer")
    p("      donde hay 3. Con los escritos, %d no es igual a %d: CAE."
      % (m3["cifra_pares_del_instrumento"] - m3["cifra_pares_disueltos"],
         m3["cifra_reales_contra_el_archivo"]))
    marcar("C, LA MUTACION: contar escritos NO da lo mismo que contar distintos",
           (m3["cifra_pares_del_instrumento"] - m3["cifra_pares_disueltos"])
           != m3["cifra_pares_distintos_tras_resolver"])
    p("")

    p("(D) UN PAR CON VEREDICTO EN EL ARCHIVO NO ES REAL")
    idx = {par("nodo_uno", "nodo_dos"): ["una fila fabricada"]}
    m4 = L2.medir_nomina(NOMINA, {}, VIVOS_TODOS, idx, {})
    marcar("D: con el veredicto puesto, quedan 5 reales",
           m4["cifra_reales_contra_el_archivo"] == 5,
           "con veredicto: %d" % m4["cifra_pares_con_veredicto"])
    marcar("D, LA CONTRAPRUEBA: sin el veredicto vuelven a ser 6",
           m2["cifra_reales_contra_el_archivo"] == 6)
    p("")

    p("(E) UN PAR CON LECTURA DIRIGIDA: LAS DOS COLUMNAS DICEN COSAS DISTINTAS")
    dirig = {par("nodo_uno", "nodo_dos"): ("A", "FICHERO_FABRICADO.md")}
    m5 = L2.medir_nomina(NOMINA, {}, VIVOS_TODOS, {}, dirig)
    p("      reales contra el archivo: %d | reales contra las dos sedes: %d"
      % (m5["cifra_reales_contra_el_archivo"],
         m5["cifra_reales_contra_las_dos_sedes"]))
    marcar("E: contra el archivo sigue siendo real, o sea 6",
           m5["cifra_reales_contra_el_archivo"] == 6)
    marcar("E: contra las dos sedes deja de serlo, o sea 5",
           m5["cifra_reales_contra_las_dos_sedes"] == 5)
    marcar("E: y la resta que las une esta contada, no supuesta",
           (m5["cifra_reales_contra_el_archivo"]
            - m5["cifra_reales_que_ADEMAS_tienen_dirigida"]
            == m5["cifra_reales_contra_las_dos_sedes"]))
    p("")

    p("(F) LOS DOS CAMINOS: SI DISCREPAN, SE DICE")
    m6 = L2.medir_nomina(NOMINA, {}, {"nodo_uno": True, "nodo_dos": True}, {}, {})
    p("      vivos por resolutor: %d | vivos por grafo: %d | calzan: %s"
      % (m6["cifra_vivos_por_resolutor"], m6["cifra_vivos_por_grafo"],
         m6["los_dos_caminos_calzan"]))
    marcar("F: con el grafo diciendo 2 y el resolutor 4, NO calzan",
           m6["los_dos_caminos_calzan"] is False)
    marcar("F, LA CONTRAPRUEBA: con los dos diciendo 4, SI calzan",
           m2["los_dos_caminos_calzan"] is True)
    p("")

    p("CIFRA comprobaciones: 16 | fallan: %d" % len(fallos))
    if fallos:
        p("ROJO: %d comprobacion(es) no se comportan." % len(fallos))
        for f in fallos:
            p("   " + f)
        p("FIN")
        return 1
    p("VERDE: el resolutor esta puesto de verdad (una nomina que colapsa da cero y "
      "sin el alias vuelve), los pares se cuentan RESUELTOS y no escritos (que es "
      "lo que mordio hoy en la primera corrida del instrumento), el veredicto y la "
      "lectura dirigida restan cada uno en su columna, y los dos caminos se "
      "cotejan de verdad.")
    p("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
