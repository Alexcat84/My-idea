# -*- coding: utf-8 -*-
r"""vuelta140_2b_mutaciones.py . LAS TRES PRUEBAS DE LA GUARDA DE AFIRMACIONES
DE CIERRE (TAREA 2.b de la vuelta 140, acta de la vuelta 139, caida 4.1).

QUE PRUEBA. `verificar_cifras_del_reporte.py` aprendio en esta vuelta a leer
las afirmaciones de cierre: toda frase que diga que una FASE o un CATALOGO
cierra, queda completo o esta entero tiene que citar un fichero de salida de
`tallar_estado_de_fase.py`, y ese fichero tiene que decir `sin cumplir: 0`.

  (a) frase de cierre SIN cita: ROJO.
  (b) frase de cierre con cita a un fichero que dice `sin cumplir: 3`: ROJO
      NOMBRANDO LAS TRES.
  (c) sin la frase: VERDE.

EL SUJETO ES FABRICADO Y CONGELADO, NO EL REPORTE DE HOY. Se escribe un
reporte minimo en un temporal y dos ficheros de salida de estado de fase
(uno con `sin cumplir: 0` y otro con `sin cumplir: 3`), y LOS TRES SE RETIRAN
AL TERMINAR (P.16, quien fabrica limpia), pase lo que pase, incluso si el
script cae. Asi el caso no depende del arbol de hoy ni deja basura que la
proxima guarda de apertura se coma.

NINGUN VEREDICTO ES UN LITERAL: los tres comparan el EXIT y los FALLOS que la
guarda de verdad acaba de computar sobre el sujeto fabricado, y cada caso
lleva su contraprueba (el mismo camino sin la mutacion).

USO:
  python scripts/loop/vuelta140_2b_mutaciones.py
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verificar_cifras_del_reporte as V  # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")

# Los tres temporales. El prefijo V999 no colisiona con ninguna vuelta real y
# el segmento MUTACION es el que verificar_apertura_sellada.py ya sabe
# descartar por convencion desde la vuelta 102.
F_ESTADO_LIMPIO = "SALIDA_V999_MUTACION_ESTADO_LIMPIO.txt"
F_ESTADO_SUCIO = "SALIDA_V999_MUTACION_ESTADO_SUCIO.txt"
F_REPORTE = "_v140_2b_reporte_fabricado.md"

ESTADO_LIMPIO = """ESTADO DE LA FASE 99_FABRICADA | REF: SUJETO FABRICADO

| id_op | veredicto |
|---|---|
| OP-Z-01 | CUMPLIDO |

CIFRA: operaciones del catalogo: 1 | con destino cumplido: 1 | sin cumplir: 0 | de ellas, sin vara escrita: 0
SIN CUMPLIR (0): ninguna
SIN VARA ESCRITA (0): ninguna
"""

ESTADO_SUCIO = """ESTADO DE LA FASE 99_FABRICADA | REF: SUJETO FABRICADO

| id_op | veredicto |
|---|---|
| OP-Z-01 | CUMPLIDO |
| OP-Z-02 | SIN CUMPLIR |
| OP-Z-03 | SIN CUMPLIR |
| OP-Z-04 | SIN CUMPLIR |

CIFRA: operaciones del catalogo: 4 | con destino cumplido: 1 | sin cumplir: 3 | de ellas, sin vara escrita: 0
SIN CUMPLIR (3): OP-Z-02, OP-Z-03, OP-Z-04
SIN VARA ESCRITA (0): ninguna
"""

CUERPO_BASE = """# REPORTE FABRICADO PARA LA MUTACION 2.b DE LA VUELTA 140

Este fichero es un sujeto de prueba. No es un reporte de la campana.

El motor pasa entero y la web tambien.
"""

FRASE_SIN_CITA = "\nLA FASE 99 CIERRA SU CATALOGO.\n"
FRASE_CON_CITA_SUCIA = ("\nLA FASE 99 CIERRA SU CATALOGO, medido en "
                        "`%s`.\n" % F_ESTADO_SUCIO)
FRASE_CON_CITA_LIMPIA = ("\nLA FASE 99 CIERRA SU CATALOGO, medido en "
                         "`%s`.\n" % F_ESTADO_LIMPIO)


def escribir(nombre, contenido):
    ruta = os.path.join(LOOP, nombre)
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(contenido)
    return ruta


def retirar(*nombres):
    for n in nombres:
        ruta = os.path.join(LOOP, n)
        if os.path.exists(ruta):
            os.remove(ruta)


def correr(cuerpo):
    """Corre la guarda de verdad sobre el sujeto fabricado y devuelve
    (fallos, cierres_cotejados). Nada tecleado: es la funcion real."""
    ruta = escribir(F_REPORTE, cuerpo)
    cierres = []
    fallos, _cot, _ex, _tot = V.verificar(ruta, cierres_out=cierres)
    return fallos, cierres


def main():
    escribir(F_ESTADO_LIMPIO, ESTADO_LIMPIO)
    escribir(F_ESTADO_SUCIO, ESTADO_SUCIO)
    try:
        print("=" * 78)
        print("(c) CONTRAPRUEBA PRIMERO: EL MISMO CUERPO SIN LA FRASE DE CIERRE")
        print("=" * 78)
        fallos_c, cierres_c = correr(CUERPO_BASE)
        print("fallos: %d" % len(fallos_c))
        for x in fallos_c:
            print("   %s" % x)
        ok_c = not fallos_c
        print("VEREDICTO (c): %s" % ("VERDE" if ok_c else "ROJO"))

        print("")
        print("=" * 78)
        print("(a) FRASE DE CIERRE SIN CITA")
        print("=" * 78)
        fallos_a, _ = correr(CUERPO_BASE + FRASE_SIN_CITA)
        print("fallos: %d" % len(fallos_a))
        for x in fallos_a:
            print("   %s" % x)
        de_cierre_a = [x for x in fallos_a if "AFIRMACION DE CIERRE" in x]
        ok_a = len(de_cierre_a) == 1 and "SIN cita" in de_cierre_a[0]
        print("ROJO Y ES DE LA ESPECIE CORRECTA: %s" % ok_a)
        print("CONTRAPRUEBA: sin la frase habia %d fallo(s), con ella %d"
              % (len(fallos_c), len(fallos_a)))
        ok_a = ok_a and len(fallos_a) > len(fallos_c)
        print("VEREDICTO (a): %s" % ("VERDE" if ok_a else "ROJO"))

        print("")
        print("=" * 78)
        print("(b) FRASE DE CIERRE CITANDO UN FICHERO QUE DICE sin cumplir: 3")
        print("=" * 78)
        fallos_b, _ = correr(CUERPO_BASE + FRASE_CON_CITA_SUCIA)
        print("fallos: %d" % len(fallos_b))
        for x in fallos_b:
            print("   %s" % x)
        de_cierre_b = [x for x in fallos_b if "AFIRMACION DE CIERRE" in x]
        # Las TRES tienen que salir NOMBRADAS, y los nombres se leen del
        # fichero fabricado, no de una lista tecleada aqui.
        leido = V.leer_estado_de_fase(ESTADO_SUCIO)
        esperados = leido[1]
        nombradas = (len(de_cierre_b) == 1
                     and all(n in de_cierre_b[0] for n in esperados)
                     and ("sin cumplir: %d" % leido[0]) in de_cierre_b[0])
        print("EL FICHERO FABRICADO DICE sin cumplir: %d y nombra %s (leido, no tecleado)"
              % (leido[0], esperados))
        print("ROJO NOMBRANDO LAS TRES: %s" % nombradas)
        ok_b = nombradas and len(fallos_b) > len(fallos_c)
        print("VEREDICTO (b): %s" % ("VERDE" if ok_b else "ROJO"))

        print("")
        print("=" * 78)
        print("(c bis) LA MISMA FRASE CITANDO UN FICHERO QUE DICE sin cumplir: 0")
        print("=" * 78)
        fallos_d, cierres_d = correr(CUERPO_BASE + FRASE_CON_CITA_LIMPIA)
        print("fallos: %d" % len(fallos_d))
        for x in fallos_d:
            print("   %s" % x)
        print("afirmaciones de cierre COTEJADAS: %d" % len(cierres_d))
        for c in cierres_d:
            print("   linea %d (sujeto '%s', verbo '%s') <-> %s" % c)
        ok_d = not [x for x in fallos_d if "AFIRMACION DE CIERRE" in x] and len(cierres_d) == 1
        print("VEREDICTO (c bis): %s" % ("VERDE" if ok_d else "ROJO"))

        todo = ok_a and ok_b and ok_c and ok_d
        print("")
        print("=" * 78)
        print("RESUMEN: (a) %s | (b) %s | (c) %s | (c bis) %s"
              % tuple("VERDE" if x else "ROJO" for x in (ok_a, ok_b, ok_c, ok_d)))
        print("=" * 78)
        return 0 if todo else 1
    finally:
        # P.16: QUIEN FABRICA, LIMPIA. Pase lo que pase.
        retirar(F_ESTADO_LIMPIO, F_ESTADO_SUCIO, F_REPORTE)
        quedan = [n for n in (F_ESTADO_LIMPIO, F_ESTADO_SUCIO, F_REPORTE)
                  if os.path.exists(os.path.join(LOOP, n))]
        print("P.16, temporales retirados: %s" % ("SI" if not quedan else "NO, quedan %s" % quedan))


if __name__ == "__main__":
    raise SystemExit(main())
