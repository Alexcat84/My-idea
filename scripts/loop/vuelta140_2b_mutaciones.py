# -*- coding: utf-8 -*-
r"""vuelta140_2b_mutaciones.py . LAS SIETE PRUEBAS DE LA GUARDA DE AFIRMACIONES
DE CIERRE (TAREA 2.b de la vuelta 140, acta de la vuelta 139, caida 4.1).

QUE PRUEBA. `verificar_cifras_del_reporte.py` aprendio en esta vuelta a leer
las afirmaciones de cierre: toda frase que hable del cierre o de la completitud
de una FASE o de un CATALOGO tiene que (1) citar un fichero de salida de
`tallar_estado_de_fase.py` en su ventana y (2) si ese fichero dice
`sin cumplir: N` con N distinto de cero, NOMBRAR LAS N en esa misma ventana.

  (a)     frase de cierre SIN cita: ROJO.
  (b)     frase de cierre con cita a un fichero que dice `sin cumplir: 3` y SIN
          nombrarlas: ROJO NOMBRANDO LAS TRES.
  (b bis) la MISMA frase, el MISMO fichero, pero NOMBRANDO las tres: VERDE. Es el
          caso que la primera version de la guarda tiraba, y por el que se
          reparo: un reporte que dice la verdad sobre una fase que no cierra
          caia igual que uno que la calla.
  (c)     sin la frase: VERDE.
  (c bis) frase con cita a un fichero que dice `sin cumplir: 0`: VERDE y cotejada.
  (d)     el DELIMITADOR de los COMMITS TALLADOS: la misma frase de cierre SIN
          cita, metida DENTRO del bloque delimitado, no se ve; el MISMO texto sin
          las marcas si se ve. Es la contraprueba de que el delimitador quita lo
          delimitado y nada mas.
  (e)     UNA SOLA marca del delimitador: ROJO ruidoso, no silencio.

EL SUJETO ES FABRICADO Y CONGELADO, NO EL REPORTE DE HOY. Se escribe un
reporte minimo en un temporal y dos ficheros de salida de estado de fase
(uno con `sin cumplir: 0` y otro con `sin cumplir: 3`), y LOS TRES SE RETIRAN
AL TERMINAR (P.16, quien fabrica limpia), pase lo que pase, incluso si el
script cae. Asi el caso no depende del arbol de hoy ni deja basura que la
proxima guarda de apertura se coma.

NINGUN VEREDICTO ES UN LITERAL: los siete comparan los FALLOS que la guarda de
verdad acaba de computar sobre el sujeto fabricado, y cada caso lleva su
contraprueba (el mismo camino sin la mutacion). Los nombres de las que faltan
se LEEN del fichero fabricado con la funcion de la propia guarda, no se teclean.

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
                     and ("sin cumplir: %d" % leido[0]) in de_cierre_b[0]
                     and "NO NOMBRA" in de_cierre_b[0])
        print("EL FICHERO FABRICADO DICE sin cumplir: %d y nombra %s (leido, no tecleado)"
              % (leido[0], esperados))
        print("ROJO NOMBRANDO LAS TRES: %s" % nombradas)
        ok_b = nombradas and len(fallos_b) > len(fallos_c)
        print("VEREDICTO (b): %s" % ("VERDE" if ok_b else "ROJO"))

        print("")
        print("=" * 78)
        print("(b bis) LA MISMA FRASE, EL MISMO FICHERO SUCIO, PERO NOMBRANDO LAS TRES")
        print("=" * 78)
        print("Es el caso que la PRIMERA version de la guarda tiraba: un reporte que dice")
        print("la verdad sobre una fase que no cierra caia igual que uno que la calla.")
        frase_nombrando = ("\nLA FASE 99 NO CIERRA, medido en `%s`: faltan %s.\n"
                           % (F_ESTADO_SUCIO, ", ".join(esperados)))
        fallos_bb, _ = correr(CUERPO_BASE + frase_nombrando)
        print("fallos: %d" % len(fallos_bb))
        for x in fallos_bb:
            print("   %s" % x)
        ok_bb = not [x for x in fallos_bb if "AFIRMACION DE CIERRE" in x]
        print("PASA CUANDO LAS NOMBRA: %s" % ok_bb)
        print("CONTRAPRUEBA, la misma frase SIN nombrarlas dio %d fallo(s) de cierre: %s"
              % (len(de_cierre_b), len(de_cierre_b) == 1))
        ok_bb = ok_bb and len(de_cierre_b) == 1
        print("VEREDICTO (b bis): %s" % ("VERDE" if ok_bb else "ROJO"))

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
            print("   linea %d (sujeto '%s', verbo '%s') <-> %s: %s" % c)
        ok_d = not [x for x in fallos_d if "AFIRMACION DE CIERRE" in x] and len(cierres_d) == 1
        print("VEREDICTO (c bis): %s" % ("VERDE" if ok_d else "ROJO"))

        print("")
        print("=" * 78)
        print("(d) EL DELIMITADOR DE LOS COMMITS TALLADOS: CON LAS DOS MARCAS, SE SALTA")
        print("=" * 78)
        print("La frase de cierre SIN cita va DENTRO del bloque delimitado. Con las dos")
        print("marcas, la guarda no la ve; el mismo texto SIN marcas si la ve.")
        dentro = ("\n" + V.MARCA_COMMITS_ABRE + "\n\n```\n"
                  "  abc12345 REPORTE DE LA VUELTA 140: LA FASE 06 NO CIERRA.\n"
                  "```\n\n" + V.MARCA_COMMITS_CIERRA + "\n")
        fallos_d, _ = correr(CUERPO_BASE + dentro)
        de_cierre_d = [x for x in fallos_d if "AFIRMACION DE CIERRE" in x]
        print("con las DOS marcas: %d fallo(s) de cierre" % len(de_cierre_d))
        sin_marcas = dentro.replace(V.MARCA_COMMITS_ABRE, "").replace(V.MARCA_COMMITS_CIERRA, "")
        fallos_sm, _ = correr(CUERPO_BASE + sin_marcas)
        de_cierre_sm = [x for x in fallos_sm if "AFIRMACION DE CIERRE" in x]
        print("SIN las marcas (contraprueba): %d fallo(s) de cierre" % len(de_cierre_sm))
        for x in de_cierre_sm:
            print("   %s" % x)
        ok_dd = (len(de_cierre_d) == 0 and len(de_cierre_sm) == 1)
        print("EL DELIMITADOR QUITA LO DELIMITADO Y NADA MAS: %s" % ok_dd)
        print("VEREDICTO (d): %s" % ("VERDE" if ok_dd else "ROJO"))

        print("")
        print("=" * 78)
        print("(e) UNA SOLA MARCA: ROJO RUIDOSO, NO SILENCIO")
        print("=" * 78)
        solo_una = dentro.replace(V.MARCA_COMMITS_CIERRA, "")
        try:
            correr(CUERPO_BASE + solo_una)
            ok_e = False
            print("NO CAYO: la guarda acepto una sola marca. ROJO.")
        except ValueError as e:
            ok_e = "commits tallados" in str(e)
            print("cayo con ValueError, como debe: %s" % e)
        print("VEREDICTO (e): %s" % ("VERDE" if ok_e else "ROJO"))

        todo = ok_a and ok_b and ok_bb and ok_c and ok_d and ok_dd and ok_e
        print("")
        print("=" * 78)
        print("RESUMEN: (a) %s | (b) %s | (b bis) %s | (c) %s | (c bis) %s | (d) %s | (e) %s"
              % tuple("VERDE" if x else "ROJO"
                      for x in (ok_a, ok_b, ok_bb, ok_c, ok_d, ok_dd, ok_e)))
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
