# -*- coding: utf-8 -*-
"""verificar_caso_rojo_por_mutacion.py . TAREA 3.b de la vuelta 90 (decision
del fundador del 29 ago 2026, opcion b), Y LA REGLA NUEVA DE EJECUTOR.md,
"EL CASO ROJO SE PRUEBA POR MUTACION", ESTRENANDOSE SOBRE SI MISMA.

POR QUE NACE, CON EL EJEMPLAR DELANTE (acta de la vuelta 89, seccion 3.2,
`docs/loop/ACTA_AUDITOR.md` lineas 30210 a 30244). El reporte de la vuelta 89
publico un "caso rojo" (`scripts/loop/vuelta89_tarea3_rebase_ope06.py`, lineas
504 a 531) donde `veredicto_2` era una CONSTANTE LITERAL (`veredicto_2 =
"ENTRA"`) y el `assert` comparaba `"ENTRA"` con `"ENTRA"`: no podia salir en
rojo nunca, y el reporte lo presento como prueba de que el criterio se
comporta.

QUE ES UNA PRUEBA DE MUTACION AQUI, EXACTO (no basta con cambiar el literal
del lado derecho del assert: eso solo prueba que dos cadenas distintas son
distintas, y no dice nada del CRITERIO). La mutacion tiene que caer sobre LA
ENTRADA que el criterio recibe, y verificar que EL VEREDICTO CAMBIA cuando la
entrada cambia. Si el veredicto NO cambia (el criterio ignora la entrada, o
la variable comparada nunca fue mas que un literal disfrazado de resultado),
ESO es lo que hace que un assert "no pueda fallar nunca", y este instrumento
lo declara ROJO en vez de dejarlo pasar.

CONTRATO, para que cualquier caso rojo futuro lo use (import, no CLI, es lo
que un script de vuelta necesita):

  from scripts.loop.verificar_caso_rojo_por_mutacion import probar_por_mutacion

  probar_por_mutacion(
      nombre="caso 2 de la TAREA 3.d",
      criterio=clasificar,              # funcion REAL bajo prueba, criterio(entrada) -> veredicto
      entrada=fabricada_2,              # la entrada fabricada, la que da el caso VERDE
      veredicto_esperado="ENTRA",       # lo que criterio(entrada) tiene que dar
      entrada_mutada=fabricada_2_negada,# LA MISMA entrada con el campo decisivo invertido
      veredicto_tras_mutar="NO_ENTRA",  # lo que criterio(entrada_mutada) tiene que dar
  )

VEREDICTO: SystemExit (ROJO, no imprime "PROBADO") si:
  (a) criterio(entrada) != veredicto_esperado (el caso VERDE no se sostiene), o
  (b) criterio(entrada_mutada) == criterio(entrada) (el veredicto NO CAMBIO al
      mutar la entrada: la variable comparada no depende de una entrada que el
      codigo compute, sospechosa de ser un literal, EXACTAMENTE el defecto de
      la vuelta 89), o
  (c) veredicto_esperado == veredicto_tras_mutar (error de construccion del
      PROPIO caso: si los dos veredictos esperados son iguales, la mutacion no
      esta pidiendo un cambio real y no prueba nada).
Imprime la corrida entera (los dos veredictos, los dos esperados) y devuelve
True solo si las tres condiciones de arriba fallan (o sea, el caso SI se
comporta y SI depende de la entrada).

AUTOPRUEBA (`python verificar_caso_rojo_por_mutacion.py`), el caso positivo Y
el caso negativo de este mismo instrumento, los dos obligatorios antes de que
nadie lo use en una vuelta:

  CASO POSITIVO (VERDE): un `criterio` de juguete que SI lee su entrada
  (busca una palabra) da veredictos distintos con la entrada normal y con la
  mutada: `probar_por_mutacion` tiene que devolver True.

  CASO NEGATIVO (EL DEFECTO DE LA VUELTA 89, REPRODUCIDO A PROPOSITO): un
  `criterio` de juguete que IGNORA su entrada y siempre devuelve "ENTRA" (la
  forma exacta de `veredicto_2 = "ENTRA"`): `probar_por_mutacion` TIENE que
  caer con SystemExit, nombrando que el veredicto no cambio. Si este caso NO
  cae, el instrumento no sirve y se declara asi, no se publica.

USO:
  python scripts/loop/verificar_caso_rojo_por_mutacion.py
"""
import sys


def probar_por_mutacion(nombre, criterio, entrada, veredicto_esperado,
                        entrada_mutada, veredicto_tras_mutar):
    """Ver el contrato completo en el docstring del modulo. Devuelve True si
    el caso pasa las tres comprobaciones; levanta SystemExit (ROJO) si no."""
    if veredicto_esperado == veredicto_tras_mutar:
        raise SystemExit(
            "ROJO DE CONSTRUCCION en %r: veredicto_esperado y veredicto_tras_mutar son "
            "iguales (%r): la mutacion no pide un cambio real, no prueba nada. Elegir una "
            "entrada_mutada cuyo veredicto correcto sea DISTINTO." % (nombre, veredicto_esperado))

    real = criterio(entrada)
    real_mutado = criterio(entrada_mutada)

    print("=" * 78)
    print("PRUEBA DE MUTACION: %s" % nombre)
    print("=" * 78)
    print("  entrada normal -> criterio da: %r (esperado: %r)" % (real, veredicto_esperado))
    print("  entrada MUTADA -> criterio da: %r (esperado: %r)" % (real_mutado, veredicto_tras_mutar))

    if real != veredicto_esperado:
        raise SystemExit(
            "ROJO en %r: el caso VERDE no se sostiene. criterio(entrada) dio %r, se "
            "esperaba %r. NO SE PUBLICA COMO PRUEBA." % (nombre, real, veredicto_esperado))

    if real_mutado == real:
        raise SystemExit(
            "ROJO en %r: EL VEREDICTO NO CAMBIO al mutar la entrada (%r en los dos casos). "
            "Es EXACTAMENTE el defecto de la vuelta 89 (acta 89, seccion 3.2): un assert que "
            "compara una variable que no depende de lo que el codigo compute sobre la "
            "entrada no es un caso rojo, aunque el numero de la izquierda y el de la derecha "
            "sean distintos entre si. NO SE PUBLICA COMO PRUEBA." % (nombre, real))

    if real_mutado != veredicto_tras_mutar:
        raise SystemExit(
            "ROJO en %r: la entrada mutada SI cambio el veredicto (a %r), pero no al valor "
            "que se esperaba (%r): revisar la mutacion o el criterio." % (nombre, real_mutado, veredicto_tras_mutar))

    print("  PROBADO POR MUTACION: el veredicto SI depende de la entrada, y los dos lados "
          "calzan con lo esperado.")
    print()
    return True


def _autoprueba():
    """CASO POSITIVO y CASO NEGATIVO de este propio instrumento, con toy
    criterios fabricados a proposito (nunca dataset/, nunca un fichero real)."""
    print("#" * 78)
    print("AUTOPRUEBA DE verificar_caso_rojo_por_mutacion.py")
    print("#" * 78)
    print()

    # --- CASO POSITIVO: un criterio que SI lee su entrada ---
    def criterio_real(fila):
        return "ENTRA" if "desarrolla" in fila["frase"].lower() else "NO_ENTRA"

    entrada = {"frase": "El hijo desarrolla el paso 2 de la madre entero."}
    entrada_mutada = {"frase": "Ninguno de los dos hace nada del otro."}

    ok = probar_por_mutacion(
        nombre="CASO POSITIVO (criterio que si depende de la entrada)",
        criterio=criterio_real, entrada=entrada, veredicto_esperado="ENTRA",
        entrada_mutada=entrada_mutada, veredicto_tras_mutar="NO_ENTRA",
    )
    assert ok is True, "el caso positivo tenia que devolver True"
    print("CASO POSITIVO: PROBADO (probar_por_mutacion devolvio True, como se esperaba).")
    print()

    # --- CASO NEGATIVO: el defecto EXACTO de la vuelta 89, reproducido a proposito ---
    def criterio_falso_de_la_vuelta_89(fila):
        return "ENTRA"  # ignora `fila` por completo: es literalmente veredicto_2 = "ENTRA"

    cayo = False
    try:
        probar_por_mutacion(
            nombre="CASO NEGATIVO (el defecto de la vuelta 89, reproducido a proposito)",
            criterio=criterio_falso_de_la_vuelta_89, entrada=entrada,
            veredicto_esperado="ENTRA", entrada_mutada=entrada_mutada,
            veredicto_tras_mutar="NO_ENTRA",
        )
    except SystemExit as e:
        cayo = True
        print("CASO NEGATIVO: CAYO EN ROJO COMO SE ESPERABA. Mensaje:")
        print("   %s" % e)
    if not cayo:
        print()
        print("ROJO DEL PROPIO INSTRUMENTO: el caso negativo (el defecto de la vuelta 89 "
              "reproducido a proposito) NO cayo. Este instrumento no sirve: no se publica "
              "como prueba de nada hasta que este caso caiga.")
        return 1

    print()
    print("LOS DOS CASOS DE LA AUTOPRUEBA SE COMPORTAN COMO SE ESPERA: el positivo pasa, y "
          "el negativo (el defecto exacto de la vuelta 89) cae en rojo. El instrumento esta "
          "probado por mutacion sobre si mismo.")
    return 0


if __name__ == "__main__":
    sys.exit(_autoprueba())
