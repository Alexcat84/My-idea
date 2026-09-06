# -*- coding: utf-8 -*-
"""_v188_correccion_de_cifras.py . LA CORRECCION DECLARADA DE LAS CIFRAS QUE MI
PROPIA GUARDA NUEVA CAZO AL CERRAR LA VUELTA 188.

QUE PASO, MEDIDO Y NO SUPUESTO. La TAREA 3 publico los bytes y el `sha256` de dos
salidas de arnes tal como estaban cuando esa tarea cerro. Despues, la **doble
corrida de la 5.d** volvio a correr esos arneses, y **la 3.b les habia anadido el
sello del sujeto**, asi que sus salidas crecieron. Las cifras de la TAREA 3
quedaron viejas.

QUIEN LO CAZO: **la guarda de las dos convenciones que esta misma vuelta acaba de
ensanchar** (TAREA 4.a). Corrida por `cerrar_reporte.py` al cerrar, acuso
`SALIDA_V186_T2C_MUTACION_CIERRE_TARDIO.txt` publicando **7544** cuando el disco
dice **7545**. **La escalada se caza a si misma en su primera corrida de verdad.**

COMO SE CORRIGE: **el texto viejo NO SE BORRA**. Cada cifra nueva lleva al lado la
que sustituye y el motivo, porque una correccion que tapa lo que corrige no se
puede auditar.

Auxiliar de una sola vuelta: no es guarda y no entra en la nomina.
"""
import io
import os

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DESTINOS = [
    "docs/loop/REPORTE.md",
    "scripts/loop/_v188_t3_seccion.md",
]

MOTIVO = (
    "**CORRECCION DECLARADA DE ESTA MISMA VUELTA:** esta seccion publico primero "
    "**%s** y **%s**, medidos cuando la TAREA 3 cerro. **La cifra vieja se "
    "conserva aqui y no se tapa.** El fichero se movio despues, cuando la **doble "
    "corrida de la 5.d** volvio a correr el arnes ya con el sello del sujeto que "
    "la 3.b le anadio. **Lo cazo la guarda de las dos convenciones que esta misma "
    "vuelta ensancho en la TAREA 4.a**, al cerrar: acuso la pareja publicada "
    "contra el disco. **La escalada se caza a si misma en su primera corrida de "
    "verdad.**")

CAMBIOS = [
    ("`docs/loop/SALIDA_V186_T2C_MUTACION_CIERRE_TARDIO.txt`" + NL
     + "(**7544 bytes en disco y 7544 bytes normalizados a LF**, con su `sha256`" + NL
     + "normalizado a LF en `be4edc90f2889552`): **`CIFRA casos: 22 | pasan:",
     "`docs/loop/SALIDA_V186_T2C_MUTACION_CIERRE_TARDIO.txt`" + NL
     + "(**7545 bytes en disco y 7545 bytes normalizados a LF**, con su `sha256`" + NL
     + "normalizado a LF en `0efa4f8f7fc856c7`; " + MOTIVO % ("7544", "`be4edc90f2889552`")
     + "): **`CIFRA casos: 22 | pasan:"),
    ("`SALIDA_V186_T2A_MUTACION_PIEZA4.txt` cierra en" + NL
     + "**3906 bytes en disco y 3906 bytes normalizados a LF**, con su `sha256`" + NL
     + "normalizado a LF en `2b444ffe193d27f9`, y su arnes sigue en",
     "`SALIDA_V186_T2A_MUTACION_PIEZA4.txt` cierra en" + NL
     + "**3908 bytes en disco y 3908 bytes normalizados a LF**, con su `sha256`" + NL
     + "normalizado a LF en `176eb049f8c898aa` ("
     + (MOTIVO % ("3906", "`2b444ffe193d27f9`"))
     + "), y su arnes sigue en"),
    ("`docs/loop/SALIDA_V188_T3C_MUTACION_EXCLUSION_POR_ROJO.txt`" + NL
     + "(**3565 bytes en disco y 3565 bytes normalizados a LF**, con su `sha256`" + NL
     + "normalizado a LF en `622b67673e6d75f4`), **`CIFRA casos: 11 | pasan:",
     "`docs/loop/SALIDA_V188_T3C_MUTACION_EXCLUSION_POR_ROJO.txt`" + NL
     + "(**3565 bytes en disco y 3565 bytes normalizados a LF**, con su `sha256`" + NL
     + "normalizado a LF en `4d052ee1f1fce39e`; **CORRECCION DECLARADA: esta seccion"
     + " publico primero el `sha256` `622b67673e6d75f4`, y esa cifra vieja se"
     + " conserva. El arnes crecio al anadirse el arnes de `vecinos()` a la lista"
     + " que la doble corrida publica; los bytes no se movieron y el `sha256` si,"
     + " que es exactamente por lo que se miden los dos**), **`CIFRA casos: 11 | pasan:"),
    ("(`scripts/loop/cerrar_reporte.py`, **97163 bytes normalizados a LF, 1844 lineas**," + NL
     + "su `sha256` normalizado a LF es `2e37089d0389e67e`):",
     "(`scripts/loop/cerrar_reporte.py`, que cuando la TAREA 3 corrio media" + NL
     + "**97163 por las dos convenciones** y **1844 lineas**, con su `sha256`" + NL
     + "normalizado a LF en `2e37089d0389e67e`." + NL
     + NL
     + "**CORRECCION DECLARADA DE ESTA MISMA VUELTA, Y LA CIFRA VIEJA DE ARRIBA NO SE" + NL
     + "TAPA:** al cerrar la vuelta, ese mismo `scripts/loop/cerrar_reporte.py` mide" + NL
     + "**108128 bytes en disco y 108128 bytes normalizados a LF**, con su `sha256`" + NL
     + "normalizado a LF en `745a15a8e693ec5c`, **porque la TAREA 4 lo cambio" + NL
     + "despues**. La historica se escribe **sin la palabra bytes al lado a" + NL
     + "proposito**, para que no se publique como una pareja de convenciones que el" + NL
     + "disco de hoy ya no sostiene. **Las dos mediciones se publican y ninguna se" + NL
     + "tapa, que es justo lo que el sello del sujeto de la 3.b existe para hacer" + NL
     + "legible.**" + NL
     + NL
     + "El inventario de la TAREA 3, con el sujeto de aquel momento):"),
]


def main():
    for rel in DESTINOS:
        p = os.path.join(RAIZ, rel.replace("/", os.sep))
        t = io.open(p, encoding="utf-8").read().replace(chr(13) + NL, NL)
        antes = len(t.encode("utf-8"))
        n = 0
        for viejo, nuevo in CAMBIOS:
            if viejo in t:
                t = t.replace(viejo, nuevo)
                n += 1
        if n:
            io.open(p, "w", encoding="utf-8", newline=NL).write(t)
        print("%-40s cambios: %-3d bytes %d -> %d"
              % (rel, n, antes, len(t.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
