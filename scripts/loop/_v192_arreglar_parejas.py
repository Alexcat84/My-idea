# -*- coding: utf-8 -*-
r"""_v192_arreglar_parejas.py . ARREGLA LAS DOS PROSAS DE ANTES Y DESPUES QUE
`convenciones_que_no_calzan()` CAZO AL CERRAR LA VUELTA 192.

QUE PASO, Y ES LA GUARDA HACIENDO SU TRABAJO CONTRA MI. Dos secciones anexadas
publicaban un par de bytes de ANTES en prosa, junto al nombre del fichero, y la
guarda de las dos convenciones **exige que una pareja atribuida a una ruta sea
CIERTA HOY**, no historica:

  - la TAREA 1 publicaba `998216 / 998216` cerca de
    `SALIDA_V192_T1A_RECORRIDO_SIN_ESCRIBIR.txt`, que mide 13161;
  - la TAREA 4 publicaba `14724 / 14724` como el ANTES de
    `apertura_del_auditor.py`, que hoy mide 21223.

**LAS DOS CIFRAS ERAN CIERTAS Y LA GUARDA TIENE RAZON IGUAL:** una cifra de bytes
en prosa, al lado de una ruta, se lee como una afirmacion sobre esa ruta. **El
remedio es el que la casa ya tiene para las citas: la cerca.** Un bloque cercado
es una cita de la salida de un instrumento y queda fuera de la guarda, que es
exactamente lo que estas dos cifras son.

NO SE BORRA NINGUNA CIFRA: se mueven a su cerca y se dice de donde salen. El
parche es IDEMPOTENTE y CAE sin escribir si un ancla no aparece.
"""
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NL = chr(10)
CERCA = "`" * 3

T1_VIEJO = """El re corrido escribe `docs/loop/SALIDA_V192_T1A_RECORRIDO_SIN_ESCRIBIR.txt` y
dice con sus palabras que **NO consume el numero `R.55`**. La sede paso de
**998216 bytes en disco y 998216 bytes normalizados a LF** a **1020758 bytes en
disco y 1020758 bytes normalizados a LF** al escribir la entrada, y **no se movio
un byte en el re corrido**."""

T1_NUEVO = """El re corrido escribe `docs/loop/SALIDA_V192_T1A_RECORRIDO_SIN_ESCRIBIR.txt` y
dice con sus palabras que **NO consume el numero `R.55`**. **Lo que la sede se
movio AL ESCRIBIR la entrada va cercado abajo**, citado de la salida del propio
registrador, porque son cifras de ANTES y una cifra de bytes suelta al lado de
una ruta se lee como una afirmacion sobre esa ruta HOY:

@@C@@
L) ESCRITA EN docs/PENDIENTES.md
   la sede pasa de 998216 a 1020758 bytes
   RELEIDA DEL DISCO: la entrada esta byte a byte: SI
@@C@@

**Y en el re corrido no se movio un byte**, que es lo que prueba el bloque de
arriba."""

T4_VIEJO = """**(a) LA CUARTA PUERTA, ANADIDA A `scripts/loop/apertura_del_auditor.py`.** El
fichero pasa de **14724 bytes en disco y 14724 en LF** a **21223 bytes en disco y
21223 en LF**, y **COMPILA**. Lo que se le anade son **cinco funciones y cuatro
constantes**, y ni una linea de las tres puertas viejas se toca:"""

T4_NUEVO = """**(a) LA CUARTA PUERTA, ANADIDA A `scripts/loop/apertura_del_auditor.py`.** **Lo
que el fichero crecio va cercado abajo**, citado de la salida del parche, porque
la primera de las dos cifras es de ANTES y una cifra de bytes suelta al lado de
una ruta se lee como una afirmacion sobre esa ruta HOY:

@@C@@
   apertura_del_auditor.py pasa de 14724 a 21223 bytes en disco
   COMPILA
@@C@@

Lo que se le anade son **cinco funciones y cuatro constantes**, y ni una linea de
las tres puertas viejas se toca:"""

CAMBIOS = [("la prosa de la sede en la TAREA 1", T1_VIEJO, T1_NUEVO),
           ("la prosa del crecimiento en la TAREA 4", T4_VIEJO, T4_NUEVO)]

DESTINOS = ["docs/loop/REPORTE.md",
            "scripts/loop/_v192_t1_seccion.md",
            "scripts/loop/_v192_t4_seccion.md"]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    total = 0
    for rel in DESTINOS:
        p = os.path.join(RAIZ, rel.replace("/", os.sep))
        if not os.path.exists(p):
            print("   NO EXISTE %s" % rel)
            return 1
        t = io.open(p, encoding="utf-8").read().replace(chr(13) + NL, NL)
        antes = len(t.encode("utf-8"))
        tocado = False
        for nombre, viejo, nuevo in CAMBIOS:
            nuevo = nuevo.replace("@@C@@", CERCA)
            if nuevo in t:
                print("   YA ESTABA en %s: %s" % (rel, nombre))
                tocado = True
                continue
            if viejo not in t:
                continue
            t = t.replace(viejo, nuevo, 1)
            print("   aplicado en %s: %s" % (rel, nombre))
            tocado = True
            total += 1
        if tocado:
            io.open(p, "w", encoding="utf-8", newline=NL).write(t)
            print("      %s pasa de %d a %d bytes en disco"
                  % (rel, antes, len(t.encode("utf-8"))))
    if total == 0:
        print("   ROJO: no se aplico ni un cambio. No se toca nada mas.")
        return 1
    print("   CIFRA cambios aplicados: %d" % total)
    return 0


if __name__ == "__main__":
    sys.exit(main())
