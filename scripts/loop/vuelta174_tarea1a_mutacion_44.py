# -*- coding: utf-8 -*-
r"""vuelta174_tarea1a_mutacion_44.py . EL CASO POSITIVO POR MUTACION DE
`corregir()`, LA FUNCION PURA DE `vuelta174_tarea1a_corregir_44.py`.

POR QUE EXISTE. `EJECUTOR.md` 1, clausula del 29 ago 2026: **NINGUN assert,
GUARDA O CASO ROJO SE PUBLICA COMO PRUEBA SIN HABER CORRIDO ANTES SU PRUEBA DE
MUTACION**. La caida 2 de la vuelta 89 fue publicar como prueba un caso rojo que
no podia fallar nunca, porque el veredicto era una constante literal. Aqui NADA
es constante: cada caso construye un reporte de mentira DISTINTO, se lo pasa a la
funcion de verdad, y comprueba que el motivo que se esperaba SALE Y NOMBRADO.

SUJETO CONGELADO: los reportes de mentira son cadenas literales de este proceso.
**CERO LECTURAS DE DISCO Y CERO ESCRITURAS.** Este arnes no puede tocar el repo
ni aunque quiera, que es lo que lo hace corrible cuantas veces haga falta.

LA VARA DE CADA CASO: se dice que motivo se espera, se corre, y se comprueba
(a) que la lista de motivos NO esta vacia cuando se espera rojo, (b) que un
motivo esperado aparece dentro de alguno de los devueltos, y (c) que el texto
devuelto es EL ORIGINAL SIN TOCAR, porque la funcion no escribe reportes a
medias. El caso VERDE comprueba lo contrario de las tres.

USO:
  python scripts/loop/vuelta174_tarea1a_mutacion_44.py
"""
import io
import os
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))

import vuelta174_tarea1a_corregir_44 as C

MEDICION = ["- `docs/loop/SALIDA_V172_T5_CERRAR_REPORTE.txt` -> **NO EXISTE**"]

FILA_5 = ("| **TAREA 5** | EL CIERRE DEL REPORTE DEJA DE SER UN PASO A MANO | "
          "**CERRADA** | `SALIDA_V172_T5_MUTACION_CIERRE.txt`, "
          "`_T5_CERRAR_REPORTE` (la corrida de esta misma vuelta) |")


def reporte(fila5=FILA_5, fin_tabla="<!-- FIN TABLA DE TAREAS -->", cola="",
            cabeza=""):
    """UN REPORTE DE MENTIRA, ARMADO PIEZA A PIEZA. Todas las piezas son
    parametros justamente para que cada caso pueda quitar UNA."""
    return (cabeza +
            "# REPORTE DE LA VUELTA 172 (ejecutor)." + NL + NL +
            "<!-- TABLA DE TAREAS -->" + NL +
            "| tarea | que encarga | estado | donde vive la prueba |" + NL +
            "|---|---|---|---|" + NL +
            "| **TAREA 1** | lo que sea | **CERRADA** | `X` |" + NL +
            "| **TAREA 2** | lo que sea | **CERRADA** | `X` |" + NL +
            "| **TAREA 3** | lo que sea | **CERRADA** | `X` |" + NL +
            "| **TAREA 4** | lo que sea | **ABIERTA, SIN CERRAR** | `X` |" + NL +
            fila5 + NL +
            fin_tabla + NL + NL +
            "## 2. LAS TAREAS, UNA POR UNA" + NL + cola)


CASOS = []


def caso(nombre, texto, motivo_esperado, medicion=None):
    CASOS.append((nombre, texto, motivo_esperado,
                  MEDICION if medicion is None else medicion))


# ------------------------------------------------------------- LOS CASOS ROJOS
caso("1. la correccion YA ESTA escrita (idempotencia)",
     reporte(cola=NL + "> **" + C.MARCA_CORRECCION + ", por el carril).**" + NL),
     "YA ESTA escrita")

caso("2. la marca de fin de tabla NO esta",
     reporte(fin_tabla="<!-- otra cosa -->"),
     "aparece 0 veces")

caso("3. la marca de fin de tabla esta DOS veces",
     reporte(cola=NL + "<!-- FIN TABLA DE TAREAS -->" + NL),
     "aparece 2 veces")

caso("4. la fila de la TAREA 5 NO esta",
     reporte(fila5="| **TAREA 6** | lo que sea | **CERRADA** | `X` |"),
     "aparece 0 veces")

caso("5. la fila de la TAREA 5 esta DOS veces",
     reporte(cola=NL + FILA_5 + NL),
     "aparece 2 veces")

caso("6. no se pasa ninguna medicion",
     reporte(),
     "sin la medicion que la sostiene", medicion=[])

caso("7. la fila no trae la celda `| **CERRADA** |`",
     reporte(fila5=FILA_5.replace("| **CERRADA** |", "| **ABIERTA** |")),
     "no trae la celda")

caso("8. la fila no trae la prueba falsa",
     reporte(fila5=FILA_5.replace(C.PRUEBA_VIEJA, "`_T5_OTRA_COSA`")),
     "no trae la prueba falsa")

caso("9. la fila trae la prueba falsa DOS veces",
     reporte(fila5=FILA_5.replace(C.PRUEBA_VIEJA,
                                  C.PRUEBA_VIEJA + " y " + C.PRUEBA_VIEJA)),
     "exactamente una vez (trae 2)")

caso("10. el reporte YA trae un guion largo de antes",
     reporte(cabeza="lo que sea " + chr(8212) + NL),
     "guiones largos o medios")

caso("11. el reporte YA trae un guion medio de antes",
     reporte(cabeza="lo que sea " + chr(8211) + NL),
     "guiones largos o medios")


def correr():
    print("=" * 78)
    print("CASO POSITIVO POR MUTACION DE corregir(), VUELTA 174 TAREA 1.a")
    print("=" * 78)
    print("SUJETO CONGELADO: cero lecturas de disco, cero escrituras.")
    print("")
    verdes = 0
    rojos = 0

    for nombre, texto, esperado, medicion in CASOS:
        nuevo, motivos = C.corregir(texto, medicion)
        hay = bool(motivos)
        nombrado = any(esperado in m for m in motivos)
        intacto = (nuevo == texto)
        ok = hay and nombrado and intacto
        print("%-52s %s" % (nombre, "CAE, y por su motivo" if ok else "NO CAE"))
        print("      espera %r | motivos: %d | nombrado: %s | texto intacto: %s"
              % (esperado, len(motivos), "SI" if nombrado else "NO",
                 "SI" if intacto else "NO"))
        if motivos:
            print("      -> " + motivos[0][:96])
        if ok:
            verdes += 1
        else:
            rojos += 1
        print("")

    print("-" * 78)
    print("EL CASO VERDE, QUE ES EL QUE PRUEBA QUE LOS ROJOS NO SON ROJOS SIEMPRE")
    print("-" * 78)
    base = reporte()
    nuevo, motivos = C.corregir(base, MEDICION)
    comprobaciones = [
        ("no devuelve ningun motivo", not motivos),
        ("el texto SI cambia", nuevo != base),
        ("el CERRADA viejo sigue entero", "**CERRADA**" in nuevo),
        ("y esta tachado", "~~**CERRADA**~~" in nuevo),
        ("solo se tacha UNO de los cinco CERRADA",
         nuevo.count("~~**CERRADA**~~") == 1),
        ("la prueba falsa sigue entera", C.PRUEBA_VIEJA in nuevo),
        ("y esta tachada", "~~" + C.PRUEBA_VIEJA + "~~" in nuevo),
        ("la prueba que si existe NO se toca",
         "`SALIDA_V172_T5_MUTACION_CIERRE.txt`," in nuevo),
        ("el bloque de correccion esta", C.MARCA_CORRECCION in nuevo),
        ("y esta DEBAJO de la tabla",
         nuevo.index(C.MARCA_CORRECCION) > nuevo.index(C.FIN_TABLA)),
        ("la medicion viaja dentro del bloque", MEDICION[0] in nuevo),
        ("las otras cuatro filas siguen una vez cada una",
         all(nuevo.count("| **TAREA %d** |" % k) == 1 for k in (1, 2, 3, 4))),
        ("es adicion: el texto nuevo es mas largo",
         len(nuevo) > len(base)),
        ("cero guiones largos y medios",
         chr(8212) not in nuevo and chr(8211) not in nuevo),
    ]
    for etiqueta, ok in comprobaciones:
        print("   %-52s %s" % (etiqueta, "SI" if ok else "NO"))
        if ok:
            verdes += 1
        else:
            rojos += 1
    print("")

    print("-" * 78)
    print("LA MUTACION DEL PROPIO ARNES (la prueba de que estos casos pueden caer)")
    print("-" * 78)
    print("Se le pide a la funcion un motivo que NO existe y se comprueba que el")
    print("arnes lo detecta como NO CAE, en vez de aprobarlo por parecido:")
    _n, motivos = C.corregir(reporte(fin_tabla="<!-- otra cosa -->"), MEDICION)
    falso = any("un motivo que nadie devuelve jamas" in m for m in motivos)
    print("   un motivo inventado aparece entre los devueltos: %s"
          % ("SI, y eso seria el arnes roto" if falso else "NO, como debe ser"))
    if falso:
        rojos += 1
    else:
        verdes += 1
    print("")

    total = verdes + rojos
    print("=" * 78)
    print("CIFRA casos: %d | verdes: %d | rojos: %d" % (total, verdes, rojos))
    print("=" * 78)
    if rojos:
        print("ROJO: %d comprobacion(es) no se comportan." % rojos)
        return 1
    print("VERDE: las %d comprobaciones se comportan, y cada guarda de corregir()"
          % total)
    print("       cae por su propio motivo cuando se le quita su pieza.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(correr())
