# -*- coding: utf-8 -*-
"""Vuelta 41, TAREA 1.3: anade al FINAL de la salida de scripts/costuras_internas.py
la linea que declara el limite adjudicado en el acta de la vuelta 40 (seccion 5,
pregunta 2, linea 8574): la cola global NO es base de lectura mientras el
MIN_BLOQUE siga siendo decision pendiente del fundador.

NO TOCA UMBRALES, NI FIXTURES, NI NODOS: solo anade lineas de impresion al final
de main(). La cifra del porcentaje se MIDE en la propia corrida (len(filas) sobre
len(activos)) y no se teclea, por la regla 1 del EJECUTOR.md.
"""
# ROTULO titulo especie=PROCEDENCIA cita=vuelta:40 fuente=docs/loop/ACTA_AUDITOR.md prueba="ACTA DE LA VUELTA 40 DEL AUDITOR" corte=2026-08-20 motivo="cita el acta de la vuelta 40, seccion 5, pregunta 2, que es lo que ejecuta"
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DEST = os.path.join(RAIZ, "scripts", "costuras_internas.py")

VIEJO = '''                 "VUELVE A DISPARAR" if f["entra"] else "sigue sin disparar"))
    return 0
'''

NUEVO = '''                 "VUELVE A DISPARAR" if f["entra"] else "sigue sin disparar"))

    # EL LIMITE DE ESTE INSTRUMENTO, DECLARADO EN SU PROPIA SALIDA (19 ago 2026,
    # vuelta 41, TAREA 1.3 del encargo, que lo ordena citando la pregunta 2 del
    # acta de la vuelta 40, linea 8574: "LA COLA AL 42,3 COMO BASE DE LECTURA:
    # NO LO ES, y debe decirlo el propio instrumento").
    #
    # POR QUE VA AQUI Y NO EN UN DOCUMENTO: para que nadie herede la cola como
    # base de lectura sin leerlo. El encabezado ya dice CITA Y NO JUZGA; esto
    # dice de que tamano es la cita y que NO autoriza.
    #
    # LA CIFRA SE MIDE, NO SE TECLEA (regla 1 del EJECUTOR.md): el porcentaje
    # sale de esta corrida, no de la nota de la vuelta 34 ni del acta.
    pct = 100.0 * len(filas) / len(activos) if activos else 0.0
    print("  LIMITE DECLARADO (acta de la vuelta 40, seccion 5, pregunta 2): "
          "LA COLA GLOBAL NO ES BASE DE LECTURA.")
    print("    Hoy son %d nodos sobre %d activos, el %s por ciento del catalogo, "
          "y ese tamano es el PENDIENTE DE DOCTRINA del MIN_BLOQUE = 2."
          % (len(filas), len(activos), ("%.1f" % pct).replace(".", ",")))
    print("    Que umbral acompana a MIN_BLOQUE = 2 lo DECIDE EL FUNDADOR y "
          "nadie lo ha tocado. Mientras siga pendiente:")
    print("    este instrumento sirve NODO A NODO. La medida de un nodo concreto "
          "(bloque, corte, pareja) NO depende de la tasa de la cola,")
    print("    pero el RANKING GLOBAL no se hereda como criterio de lectura ni "
          "como orden de trabajo. CITA Y NO JUZGA.")
    return 0
'''


def main():
    txt = io.open(DEST, encoding="utf-8").read()
    if VIEJO not in txt:
        raise SystemExit("PARADA: el anclaje no aparece tal cual en %s" % DEST)
    if txt.count(VIEJO) != 1:
        raise SystemExit("PARADA: el anclaje aparece %d veces" % txt.count(VIEJO))
    txt = txt.replace(VIEJO, NUEVO)
    io.open(DEST, "w", encoding="utf-8", newline="").write(txt)
    print("PARCHE APLICADO sobre %s" % DEST)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
