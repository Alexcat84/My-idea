# -*- coding: utf-8 -*-
"""vuelta148_2c_mutacion_vara_parada.py . PRUEBA DE MUTACION de la UNIDAD QUE
LA VUELTA 148 LE ANADE A LA VARA DE LA FASE 07 (TAREA 2.3, sobre la caida
4.4.c del acta 147), y de la REMISION de A1.3 a A2.6 (TAREA 1.c).

LO QUE HAY QUE PROBAR, Y ES LO CONTRARIO DE LO COMODO. La vuelta 148 hace que
la vara publique 9 de 9 enteros y que la fase 07 quede sin control pendiente.
Una vara que solo sabe decir que si no vale nada: hay que ensenar que CAE, y
que cae por los dos motivos nuevos.

  CASO A. EL ESTADO REAL DE HOY, computado y no tecleado: A2.6 con su parada
     CERRADA (la decision del fundador existe en el disco) y A1.3 entero por
     REMISION a A2.6.
  CASO B. LA PARADA ABIERTA. Se muta, EN COPIA EN MEMORIA, el slug de la
     parada de A2.6 por uno cuya `-DECISION.md` no existe. A2.6 tiene que
     perder el rotulo de entero y pasar a "CON PARADA ABIERTA ENCIMA".
  CASO C. LA CASCADA, que es lo que hace honesta a la remision: en esa MISMA
     mutacion, A1.3 tiene que caer CON el, porque su otra mitad se apoya en
     A2.6. Si A1.3 siguiera entero con A2.6 caido, la remision seria un
     interruptor con nombre bonito.
  CASO D. LA REMISION QUE NO EXISTE. Se muta el destino de A1.3 a un control
     que no esta en la tabla: tiene que caer tambien, en vez de darse por
     bueno por no encontrar con quien compararse.
  CASO E. EL FICHERO DE LA PARADA MANDA, NO EL NOMBRE. Un slug inventado que
     no tiene ni `.md` cuenta como SIN PARADA, no como parada abierta: la
     vara no puede inventarse paradas que nadie escribio.

NADA DE ESTO TOCA EL DISCO: se mutan copias de las fichas de `CONTROLES` y se
llaman las funciones puras `estado_de_parada`, `entero` y `rotulo_de`. Las
sondas y las mutaciones de codigo NO se vuelven a correr aqui (las corre la
vara), asi que este arnes es barato y no repite trabajo ajeno.

USO:
  python scripts/loop/vuelta148_2c_mutacion_vara_parada.py
"""
import copy
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))

import vuelta145_3b_vara_de_codigo_fase07 as V

SLUG_SIN_DECISION = "2026-09-02-parada-inventada-por-el-arnes-de-la-148"


def filas_simuladas(controles, muerden_todos=True):
    """Las filas que la vara arma, pero SIN correr sondas ni mutaciones: aqui
    se prueba la ARITMETICA DEL ROTULO, no la instalacion, que la vara ya mide
    en su propia corrida. `hay`, `aplica` y `muerde` se ponen en el estado que
    la vara midio de verdad hoy (los nueve instalados y mordiendo), para que lo
    unico que cambie entre casos sea lo que se muta."""
    filas = [(c, muerden_todos, "sonda simulada", True, muerden_todos, "mutacion simulada")
             for c in controles]
    return filas, dict((f[0]["id"], f) for f in filas)


def veredicto(controles):
    filas, por_id = filas_simuladas(controles)
    enteros = [f[0]["id"] for f in filas if V.entero(f, por_id)]
    rotulos = dict((f[0]["id"], V.rotulo_de(f, por_id)) for f in filas)
    return enteros, rotulos


def main():
    fallos = []

    # LA TABLA REAL, leida del modulo de la vara y no reescrita aqui.
    reales = V.CONTROLES
    print("CONTROLES EN LA TABLA REAL DE LA VARA: %d" % len(reales))
    a13 = next(c for c in reales if c["id"] == "A1.3")
    a26 = next(c for c in reales if c["id"] == "A2.6")
    print("A1.3 remite su mitad semantica a: %r" % a13.get("mitad_remitida_a"))
    print("A2.6 declara la parada: %r" % a26.get("parada"))
    est, det = V.estado_de_parada(a26.get("parada"))
    print("estado de esa parada, LEIDO DEL DISCO: %s [%s]" % (est, det))
    if est != "CERRADA":
        fallos.append("PREVIO: la parada de A2.6 deberia estar CERRADA hoy y esta %s" % est)

    # ---------------- CASO A: el estado real ----------------
    enteros_a, rotulos_a = veredicto(reales)
    print("")
    print("CASO A (estado real de hoy): %d entero(s) de %d" % (len(enteros_a), len(reales)))
    print("   A1.3 -> %s" % rotulos_a["A1.3"])
    print("   A2.6 -> %s" % rotulos_a["A2.6"])
    if len(enteros_a) != len(reales):
        fallos.append("CASO A: hoy deberian ser enteros los %d y son %d"
                      % (len(reales), len(enteros_a)))
    if "A1.3" not in enteros_a or "A2.6" not in enteros_a:
        fallos.append("CASO A: A1.3 o A2.6 no cuentan como enteros hoy")

    # ---------------- CASO B y C: la parada abierta y su cascada ----------------
    mutados = copy.deepcopy(reales)
    next(c for c in mutados if c["id"] == "A2.6")["parada"] = SLUG_SIN_DECISION
    # El fichero de la pregunta tiene que EXISTIR para que la parada sea
    # "abierta"; se simula sin escribir en el disco parcheando la comprobacion
    # de existencia SOLO para ese slug.
    real_exists = os.path.exists

    def exists_parcheado(ruta):
        if ruta.endswith("%s.md" % SLUG_SIN_DECISION):
            return True          # la pregunta existe
        if ruta.endswith("%s-DECISION.md" % SLUG_SIN_DECISION):
            return False         # y NO tiene respuesta
        return real_exists(ruta)

    os.path.exists = exists_parcheado
    try:
        est_b, det_b = V.estado_de_parada(SLUG_SIN_DECISION)
        enteros_b, rotulos_b = veredicto(mutados)
    finally:
        os.path.exists = real_exists

    print("")
    print("CASO B (parada de A2.6 mutada a una SIN decision): estado=%s" % est_b)
    print("   A2.6 -> %s" % rotulos_b["A2.6"])
    print("CASO C (la cascada):")
    print("   A1.3 -> %s" % rotulos_b["A1.3"])
    print("   enteros: %d de %d (eran %d)" % (len(enteros_b), len(mutados), len(enteros_a)))
    if est_b != "ABIERTA":
        fallos.append("CASO B: la parada mutada deberia leerse ABIERTA y se lee %s" % est_b)
    if "A2.6" in enteros_b:
        fallos.append("CASO B: A2.6 sigue contando como entero con una parada ABIERTA encima")
    if "PARADA ABIERTA" not in rotulos_b["A2.6"]:
        fallos.append("CASO B: el rotulo de A2.6 no nombra la parada abierta: %r"
                      % rotulos_b["A2.6"])
    if "A1.3" in enteros_b:
        fallos.append("CASO C: A2.6 cayo y A1.3 sigue entero: la remision es un interruptor, "
                      "no una dependencia")
    if len(enteros_b) != len(enteros_a) - 2:
        fallos.append("CASO C: deberian caer EXACTAMENTE dos (A2.6 y A1.3) y cayeron %d"
                      % (len(enteros_a) - len(enteros_b)))

    # ---------------- CASO D: la remision a un control que no existe ----------------
    mutados_d = copy.deepcopy(reales)
    next(c for c in mutados_d if c["id"] == "A1.3")["mitad_remitida_a"] = "A9.9_no_existe"
    enteros_d, rotulos_d = veredicto(mutados_d)
    print("")
    print("CASO D (A1.3 remite a un control que no esta en la tabla):")
    print("   A1.3 -> %s" % rotulos_d["A1.3"])
    if "A1.3" in enteros_d:
        fallos.append("CASO D: A1.3 se dio por entero remitiendo a un control inexistente")

    # ---------------- CASO E: un slug sin fichero no es una parada ----------------
    est_e, det_e = V.estado_de_parada("2026-01-01-esto-no-existe-en-ninguna-parte")
    print("")
    print("CASO E (slug sin fichero): estado=%s [%s]" % (est_e, det_e))
    if est_e != "SIN PARADA":
        fallos.append("CASO E: un slug sin fichero deberia dar SIN PARADA y da %s" % est_e)
    est_f, _ = V.estado_de_parada(None)
    if est_f != "SIN PARADA":
        fallos.append("CASO E: un control sin campo parada deberia dar SIN PARADA y da %s" % est_f)

    print("")
    if fallos:
        print("ROJO, la unidad nueva de la vara NO se sostiene (%d):" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1
    print("VERDE: los cinco casos se comportan. Con la parada CERRADA los nueve son enteros;")
    print("mutada a una parada SIN decision, A2.6 pierde el rotulo Y ARRASTRA A A1.3, que es")
    print("lo que hace honesta a la remision; una remision a un control inexistente cae; y un")
    print("slug sin fichero no se inventa una parada.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
