# -*- coding: utf-8 -*-
r"""vuelta143_2a_mutaciones.py . LA PRUEBA DE MUTACION DE LA TAREA 2.a de la
vuelta 143 (acta de la vuelta 142, adjudicacion 3.3 y caida 4.3: el regimen de
vuelta pasa a ser POR PAR y la vara aprende a leer la excepcion de la ficha).

TODO EN MEMORIA, NUNCA EN DISCO: se cargan el grafo y las operaciones, se mutan
los DICCIONARIOS cargados y se vuelve a llamar a la vara. `dataset/` y
`docs/plan/` no se tocan ni una vez, y el arnes lo comprueba al final con
`git status --porcelain`.

EL SUJETO SE ELIGE POR COMPUTO, NUNCA TECLEADO: la PRIMERA operacion ENLACE del
catalogo de la fase cuya ficha DISPARA la excepcion del 9.22 con pares
nombrados, en el orden del catalogo. Si no hay ninguna, el caso se declara
OMITIDO POR FALTA DE SUJETO y ESO ES ROJO, no verde.

POR QUE HACE FALTA UN GRAFO SIMULADO, Y SE DECLARA: hoy el sujeto sale SIN
CUMPLIR por defectos que la TAREA 3 todavia no ha reparado (le faltan idas y
tiene una vuelta bajo PROHIBE). Mutar sobre ese estado no probaria nada, porque
ya esta en rojo: la mutacion (i) tiene que hacer BAJAR una cifra, y para eso la
cifra tiene que estar arriba antes. Asi que el arnes construye EN MEMORIA el
grafo en el que la ficha esta EJECUTADA ENTERA (todas sus idas escritas y
retiradas las vueltas de los pares NO exceptuados) y comprueba primero, como
CONTRAPRUEBA, que sobre ese grafo el sujeto sale CUMPLIDO. Ese grafo simulado es
el sujeto de las mutaciones (i) y (ii). Nada de esto se escribe en disco.

CINCO COMPROBACIONES, todas con la expectativa COMPUTADA comparando antes y
despues, nunca contra una frase literal:

  (0)   CONTRAPRUEBA SIN MUTAR sobre el grafo simulado: el sujeto sale CUMPLIDO
        y NO esta en la lista de SIN CUMPLIR.
  (i)   Se mete la VUELTA de una direccion cuyo par NO esta exceptuado (elegida
        por computo). El sujeto tiene que salir NOMBRADO en SIN CUMPLIR y la
        cifra `con destino cumplido` tiene que BAJAR.
  (ii)  Sobre el mismo grafo simulado se QUITA una direccion de un par SI
        exceptuado (elegida por computo). El sujeto tiene que salir SIN CUMPLIR
        **por FALTA**, no por vuelta: su celda tiene que nombrarla en "sin la
        IDA" y NO puede haber ninguna direccion bajo PROHIBE con la vuelta
        presente.
  (iii) Se BORRA de la ficha la linea de la excepcion y se comprueba que la
        operacion vuelve al regimen PROHIBE de hoy, CON EL MISMO TEXTO DE CELDA
        que la vara publica ahora mismo sobre el grafo real: el comportamiento
        viejo no se rompio. La expectativa NO se teclea, se lee de la salida de
        la vara sobre el arbol de hoy.
  (P.16) `dataset/` y `docs/plan/` sin tocar.

USO:
  python scripts/loop/vuelta143_2a_mutaciones.py --fase 06_MESAS

--- ADJUDICACION 6.7 DEL ACTA 158 (3 sep 2026): EL CHECK DE P.16 SE CINE AL
CONTENIDO Y A LA VENTANA DEL PROPIO SCRIPT ---

REGISTRO POR ADICION. Nada de lo escrito arriba se borra, y el check que este
fichero lleva NO se modifica al escribir esto: esto es la adjudicacion, no el
remedio.

LAS DOS ANCLAS QUE SE MUEVEN EN LA MISMA LINEA, y el hallazgo es del ejecutor de
la vuelta 157, que lo trajo como pregunta en vez de esquivarlo callando. El
docstring dice que se comprueba que `dataset/` y `docs/plan/` NO SE TOCAN NI UNA
VEZ, o sea CONTENIDO. El instrumento es `git status --porcelain`, que ademas de
contenido ve:
  (i)  ESTADO DE FIN DE LINEA. Este repo tiene `core.autocrlf`, asi que un
       fichero reescrito por el ciclo queda marcado como modificado aunque su
       sha256 NORMALIZADO sea identico al de HEAD. Paso de verdad en la vuelta
       157 y tumbo tres mutaciones de la bateria en ROJO con el contenido
       intacto.
  (ii) SUCIEDAD ANTERIOR AL ARRANQUE DEL SCRIPT, que no es suya. El veredicto de
       este check depende de si alguien committeo tocando `dataset/` antes, y no
       de si las mutaciones de este fichero tocaron el dataset.

EL REMEDIO ADJUDICADO: huella de CONTENIDO tomada ANTES y DESPUES de las
mutaciones DENTRO del propio script, y comparada consigo misma. Con su caso
positivo por mutacion: si una mutacion escribe de verdad en `dataset/` o en
`docs/plan/`, el check SIGUE SALIENDO ROJO.

EL ALCANCE, Y AQUI HAY UNA DISCREPANCIA DE CIFRA QUE SE DECLARA EN VEZ DE
COPIARSE: el acta 158 mide ONCE ficheros con el patron literal, siete de ellos
dentro de la bateria de las 23. El recomputo de la vuelta 159
(`scripts/loop/vuelta159_tarea1_registrar_adjudicaciones.py`, funcion
`ficheros_con_patron_p16`, salida `docs/loop/SALIDA_V159_T1_ADJUDICACIONES.txt`)
da DOCE ficheros, y los SIETE de la bateria reproducen exactamente. El duodecimo
es `scripts/loop/vuelta89_tarea4_guarda_op_c05.py`: excluirlo devuelve los once
del acta al digito. La cifra de la vuelta 159 es la del computo, y por eso el
remedio de la 6.7 queda EN PARADA, declarada en el reporte de la vuelta 159.
"""
import argparse
import copy
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tallar_estado_de_fase as T


def enlaces_del_catalogo(fase, ops, nodos):
    """Las del catalogo que la vara enruta a ENLACE, EN EL ORDEN DEL CATALOGO."""
    remisiones = T.leer_remisiones(fase)
    fallos = []
    catalogo, por_id = T.construir_catalogo(fase, ops, remisiones, fallos)
    salida = []
    for x in catalogo:
        op = por_id[x]
        if T.es_mesa(op):
            continue
        sup = op.get("superviviente")
        if sup and T.PATRON_ID_NODO.match(sup) and sup in nodos:
            continue
        if T.pares_de_aristas(op, fallos):
            salida.append(op)
    return salida


def veredicto_de(op, nodos):
    resolver = T.resolver_de(nodos)
    fallos = []
    pares = T.pares_de_aristas(op, fallos)
    return T.destino_de_enlace(op, pares, nodos, resolver, fallos)


def escribir(nodos, resolver, origen, destino):
    """Escribe la arista EN MEMORIA en las dos vistas, con los ids resueltos."""
    o, d = resolver(origen), resolver(destino)
    if o == d:
        return
    sig = nodos[o].setdefault("nodos_siguientes", [])
    if not any(resolver(x) == d for x in sig):
        sig.append(d)
    prev = nodos[d].setdefault("nodos_previos", [])
    if not any(resolver(x) == o for x in prev):
        prev.append(o)


def retirar(nodos, resolver, origen, destino):
    """Retira la arista EN MEMORIA de las dos vistas, con los ids resueltos."""
    o, d = resolver(origen), resolver(destino)
    nodos[o]["nodos_siguientes"] = [x for x in (nodos[o].get("nodos_siguientes") or [])
                                    if resolver(x) != d]
    nodos[d]["nodos_previos"] = [x for x in (nodos[d].get("nodos_previos") or [])
                                 if resolver(x) != o]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fase", default="06_MESAS")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    ops = T.cargar_ops("WORK")
    nodos = T.cargar_grafo("WORK")
    resolver = T.resolver_de(nodos)
    enlaces = enlaces_del_catalogo(a.fase, ops, nodos)

    print("=" * 78)
    print("MUTACIONES DE LA TAREA 2.a | vuelta 143 | FASE %s" % a.fase)
    print("Todo EN MEMORIA. El sujeto se ELIGE POR COMPUTO, no se teclea.")
    print("ENLACES en el catalogo de la fase: %d (%s)"
          % (len(enlaces), ", ".join(o.get("id_op") for o in enlaces)))
    print("=" * 78)

    resultados = []

    # ---- EL SUJETO: el primer ENLACE con excepcion nombrada, por computo ----
    sujeto = None
    exceptuados = set()
    for op in enlaces:
        # LOS FALLOS SE RECOGEN Y CANTAN (TAREA 2.b, vuelta 144). Antes se
        # tiraban: un parseo roto dejaba `conj` vacio, la ficha se saltaba en
        # silencio y el arnes acababa diciendo "OMITIDO POR FALTA DE SUJETO"
        # como si ninguna ficha disparara la excepcion, cuando lo que pasaba era
        # que la lectura habia fallado. Son dos cosas distintas y se dicen
        # distinto.
        fallos_exc_lectura = []
        conj, cita, nomina = T.pares_exceptuados_de(op, resolver, fallos_exc_lectura)
        if fallos_exc_lectura:
            print("")
            print("ROJO: no se pudo leer la excepcion de %s (%d fallo(s)):"
                  % (op.get("id_op"), len(fallos_exc_lectura)))
            for f in fallos_exc_lectura:
                print("   %s" % f)
            print("SIN LECTURA FIABLE NO SE ELIGE SUJETO. ESO ES ROJO, no verde.")
            return 1
        if conj:
            sujeto, exceptuados, cita_exc, nomina_exc = op, conj, cita, nomina
            break
    if sujeto is None:
        print("")
        print("OMITIDO POR FALTA DE SUJETO: ninguna operacion ENLACE de la fase %s dispara "
              "la excepcion del 9.22 con pares nombrados, asi que no hay nada que mutar. "
              "ESO ES ROJO, no verde." % a.fase)
        return 1

    pares = T.pares_de_aristas(sujeto, [])
    dirs = T.direcciones_de(pares, resolver)
    dirs_exc = [(o, d) for o, d in dirs if frozenset((o, d)) in exceptuados]
    dirs_no_exc = [(o, d) for o, d in dirs if frozenset((o, d)) not in exceptuados]
    print("")
    print("SUJETO ELEGIDO POR COMPUTO: %s" % sujeto.get("id_op"))
    print("   excepcion disparada por: %s" % cita_exc)
    print("   PARES EXCEPTUADOS QUE LA FICHA NOMBRA (%d): %s" % (len(nomina_exc),
                                                                 ", ".join(nomina_exc)))
    print("   direcciones totales %d | de pares EXCEPTUADOS %d | de pares NO exceptuados %d"
          % (len(dirs), len(dirs_exc), len(dirs_no_exc)))

    # ---- (iii) PRIMERO SE FOTOGRAFIA EL COMPORTAMIENTO VIEJO ---------------
    # La expectativa del caso (iii) NO se teclea: es la celda que la vara
    # publica HOY sobre el grafo real cuando la ficha NO lleva la excepcion.
    # Se computa aqui, sobre el arbol sin tocar, antes de fabricar nada.
    op_sin_exc = copy.deepcopy(sujeto)
    op_sin_exc["verificacion"] = [
        ln for ln in (sujeto.get("verificacion") or [])
        if not any(f in (ln or "").lower() for f in T.FRASES_EXCEPCION_PAR)]
    cumplido_sin, razon_sin = veredicto_de(op_sin_exc, nodos)
    quitadas = len(sujeto.get("verificacion") or []) - len(op_sin_exc["verificacion"])
    esperado_viejo = ("regimen de vuelta PROHIBE por la ficha (%s): la vuelta presente "
                      "IMPIDE cumplir")
    # La cita se computa de la propia ficha, no se teclea.
    reg_base, cita_base = T.regimen_de_vuelta(op_sin_exc, [])
    esperado_viejo = esperado_viejo % cita_base
    ok = (quitadas == 1) and (reg_base == "PROHIBE") and razon_sin.endswith(esperado_viejo) \
        and ("PARES EXCEPTUADOS" not in razon_sin) and (cumplido_sin is not True)
    resultados.append(("iii sin la linea de la excepcion la ficha vuelve al regimen PROHIBE "
                       "de siempre, con el MISMO texto de celda: el comportamiento viejo no "
                       "se rompio", ok))
    print("")
    print("(iii) lineas de verificacion quitadas: %d | regimen de base recomputado: %s (%s)"
          % (quitadas, reg_base, cita_base))
    print("      la celda termina en el texto viejo: %s"
          % razon_sin.endswith(esperado_viejo))
    print("      la celda NO trae desglose por par: %s" % ("PARES EXCEPTUADOS" not in razon_sin))

    # ---- EL GRAFO SIMULADO: la ficha EJECUTADA ENTERA ----------------------
    nodos_ok = copy.deepcopy(nodos)
    res_ok = T.resolver_de(nodos_ok)
    for o, d in dirs:
        escribir(nodos_ok, res_ok, o, d)
    for o, d in dirs_no_exc:
        retirar(nodos_ok, res_ok, d, o)
    cumplido0, razon0 = veredicto_de(sujeto, nodos_ok)
    ok = cumplido0 is True
    resultados.append(("0 CONTRAPRUEBA sin mutar sobre el grafo simulado: %s sale CUMPLIDA"
                       % sujeto.get("id_op"), ok))
    print("")
    print("(0) grafo simulado (ficha ejecutada entera) -> cumplido=%s" % cumplido0)
    print("    %.230s" % razon0)

    # ---- (i) LA VUELTA DE UN PAR **NO** EXCEPTUADO -------------------------
    if not dirs_no_exc:
        print("")
        print("OMITIDO POR FALTA DE SUJETO en (i): la ficha no tiene ninguna direccion de "
              "par NO exceptuado. ESO ES ROJO.")
        return 1
    nodos_i = copy.deepcopy(nodos_ok)
    res_i = T.resolver_de(nodos_i)
    o_i, d_i = dirs_no_exc[0]
    escribir(nodos_i, res_i, d_i, o_i)
    cumplido_i, razon_i = veredicto_de(sujeto, nodos_i)
    # LA CIFRA SE COMPUTA CON LA VARA ENTERA, no a ojo.
    def cifra_con(nodos_x):
        lista, cifra, _f = T.medir(a.fase, ops, nodos_x)
        return cifra
    cifra_0 = cifra_con(nodos_ok)
    cifra_i = cifra_con(nodos_i)
    ok = (cumplido_i is not True) \
        and (sujeto.get("id_op") in cifra_i["nombres_sin_cumplir"]) \
        and (sujeto.get("id_op") not in cifra_0["nombres_sin_cumplir"]) \
        and (cifra_i["cumplido"] < cifra_0["cumplido"])
    resultados.append(("i la VUELTA de una direccion cuyo par NO esta exceptuado deja a %s "
                       "NOMBRADA en SIN CUMPLIR y hace BAJAR la cifra de cumplidas"
                       % sujeto.get("id_op"), ok))
    print("")
    print("(i) metida la vuelta %s -> %s (par NO exceptuado) -> cumplido=%s" % (d_i, o_i, cumplido_i))
    print("    cumplidas antes %d, despues %d | sin cumplir antes %s, despues %s"
          % (cifra_0["cumplido"], cifra_i["cumplido"],
             cifra_0["nombres_sin_cumplir"], cifra_i["nombres_sin_cumplir"]))
    print("    %.230s" % razon_i)

    # ---- (ii) FALTA UNA DIRECCION DE UN PAR **SI** EXCEPTUADO --------------
    if not dirs_exc:
        print("")
        print("OMITIDO POR FALTA DE SUJETO en (ii): la ficha no tiene ninguna direccion de "
              "par exceptuado. ESO ES ROJO.")
        return 1
    nodos_ii = copy.deepcopy(nodos_ok)
    res_ii = T.resolver_de(nodos_ii)
    o_ii, d_ii = dirs_exc[0]
    retirar(nodos_ii, res_ii, o_ii, d_ii)
    cumplido_ii, razon_ii = veredicto_de(sujeto, nodos_ii)
    falta = "sin la IDA: " in razon_ii and ("%s -> %s" % (o_ii, d_ii)) in razon_ii
    sin_vuelta_culpable = "bajo PROHIBE con la VUELTA presente (impiden cumplir) 0" in razon_ii
    ok = (cumplido_ii is not True) and falta and sin_vuelta_culpable
    resultados.append(("ii quitada una direccion de un par SI exceptuado, %s sale SIN "
                       "CUMPLIR por FALTA (nombrada en 'sin la IDA') y NO por vuelta "
                       "(cero direcciones bajo PROHIBE con la vuelta presente)"
                       % sujeto.get("id_op"), ok))
    print("")
    print("(ii) quitada la ida %s -> %s (par SI exceptuado) -> cumplido=%s"
          % (o_ii, d_ii, cumplido_ii))
    print("     la nombra en 'sin la IDA': %s | cero vueltas culpables: %s"
          % (falta, sin_vuelta_culpable))
    print("     %.230s" % razon_ii)

    # ---- P.16: el disco no se toco ----------------------------------------
    sucio = subprocess.run(["git", "status", "--porcelain", "--", "dataset/", "docs/plan/"],
                           cwd=T.RAIZ, capture_output=True, text=True).stdout.strip()
    ok = (sucio == "")
    resultados.append(("P.16 dataset/ y docs/plan/ SIN TOCAR tras las mutaciones", ok))
    print("")
    print("git status --porcelain -- dataset/ docs/plan/ : %r" % sucio)

    print("")
    print("=" * 78)
    verdes = 0
    for nombre, o in resultados:
        print("  %-5s %s" % ("VERDE" if o else "ROJO", nombre))
        verdes += 1 if o else 0
    print("CIFRA de la bateria 2.a: %d comprobaciones" % len(resultados))
    print("CIFRA verdes de la bateria 2.a: %d comprobaciones" % verdes)
    print("=" * 78)
    if verdes != len(resultados):
        print("ROJO: %d de %d casos no se comportan." % (len(resultados) - verdes, len(resultados)))
        return 1
    print("VERDE: los %d casos se comportan." % len(resultados))
    return 0


if __name__ == "__main__":
    sys.exit(main())
