# -*- coding: utf-8 -*-
r"""_v202_juntar_parejas.py . JUNTA CADA CIFRA DE BYTES CON SU PAREJA EN LA MISMA
LINEA, EN EL REPORTE DE LA VUELTA 202 Y EN LAS FUENTES DE DONDE SALIO.

POR QUE EXISTE, Y ES UNA CAIDA CAZADA POR UNA GUARDA DE LA CASA Y NO POR MI: al
cerrar el reporte, `scripts/loop/cerrar_reporte.py` reprobo el cierre con
**12 cifras publicadas sin su pareja**. Las cifras eran CORRECTAS todas; lo que
fallaba es que **el markdown parte la frase donde le cabe el ancho** y deja el
numero solo en su renglon, sin la segunda convencion al lado. La convencion de
bytes sigue sin fijar y es del fundador; mientras no lo este, **toda cifra de
bytes se publica con las dos**, disco y normalizado a LF, Y EN LA MISMA LINEA,
que es lo que esa guarda mide.

QUE HACE, Y LO QUE NO HACE: **NO QUITA NI UNA CIFRA**. Cada arreglo **junta** la
cifra con su pareja o **anade la segunda convencion medida**, nunca borra la
primera, que es lo que la vuelta 201 dejo escrito cuando le paso lo mismo: *se
arreglo JUNTANDO la cifra con su pareja, nunca quitando la cifra*.

PREFIJO DE GUION BAJO: computo de UNA vuelta, fuera del censo y fuera de la
nomina (adjudicacion `4.5` del acta 199).

USO:
  python scripts/loop/_v202_juntar_parejas.py
"""
import io
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
NL = chr(10)

DESTINOS = [
    "docs/loop/REPORTE.md",
    "scripts/loop/_v202_t1_seccion.md",
    "scripts/loop/_v202_t2_seccion.md",
    "scripts/loop/_v202_t3_seccion.md",
    "scripts/loop/_v202_t4_seccion.md",
    "scripts/loop/_v202_cierre_texto.md",
]

# CADA PAREJA ES (VIEJO, NUEVO). El VIEJO lleva sus saltos de linea tal como el
# markdown los partio; el NUEVO deja la cifra y su pareja EN LA MISMA LINEA.
ARREGLOS = [
    ("mide **214916 bytes en disco y 214916" + NL + "bytes normalizados a LF**",
     "mide **214916 bytes en disco y 214916 bytes normalizados a LF**"),

    ("**crecimiento en" + NL + "disco 0 bytes**",
     "**crecimiento de 0 bytes en disco y de 0 bytes normalizados a LF**"),

    ("entra midiendo **499474 bytes en disco y 499474 en" + NL
     + "LF** y sale midiendo **501883 bytes en disco y 501883 en LF**, con un" + NL
     + "**crecimiento de 2409 bytes**;",
     "entra midiendo **499474 bytes en disco y 499474 bytes normalizados a LF** y "
     "sale midiendo **501883 bytes en disco y 501883 bytes normalizados a LF**, "
     "con un **crecimiento de 2409 bytes en disco y de 2409 bytes normalizados a "
     "LF**;"),

    ("`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` mide **4054129 bytes en disco y 4054129 en"
     + NL + "LF**, y su `sha256` vale **0a77b5a35a962621** por la convencion de disco y"
     + NL + "**0a77b5a35a962621** por la de LF,",
     "`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` mide **4054129 bytes en disco y "
     "4054129 bytes normalizados a LF**, y su `sha256` vale **0a77b5a35a962621** "
     "por la convencion de disco y **0a77b5a35a962621** por la de LF,"),

    ("`scripts/loop/vuelta170_tarea5b_veredicto_op_l_02.py` mide **13487 bytes en disco"
     + NL + "y 13487 bytes normalizados a LF**",
     "`scripts/loop/vuelta170_tarea5b_veredicto_op_l_02.py` mide **13487 bytes en "
     "disco y 13487 bytes normalizados a LF**"),

    ("`docs/loop/SALIDA_V202_T2_COBERTURA_169.txt` (**5559 bytes en disco y 5449 en"
     + NL + "LF**) y `docs/loop/SALIDA_V202_T2_VEREDICTO_170.txt` (**5880 bytes en disco y"
     + NL + "5789 en LF**)",
     "`docs/loop/SALIDA_V202_T2_COBERTURA_169.txt` (**5559 bytes en disco y 5449 "
     "bytes normalizados a LF**) y `docs/loop/SALIDA_V202_T2_VEREDICTO_170.txt` "
     "(**5880 bytes en disco y 5789 bytes normalizados a LF**)"),

    ("Selladas en `docs/loop/SALIDA_V202_T3_CLAUSULAS_12_166.txt` (**32943 bytes en"
     + NL + "disco y 32684 en LF**) y `docs/loop/SALIDA_V202_T3_CLAUSULA_3_169.txt` (**4028"
     + NL + "bytes en disco y 3963 en LF**)",
     "Selladas en `docs/loop/SALIDA_V202_T3_CLAUSULAS_12_166.txt` (**32943 bytes "
     "en disco y 32684 bytes normalizados a LF**) y "
     "`docs/loop/SALIDA_V202_T3_CLAUSULA_3_169.txt` (**4028 bytes en disco y 3963 "
     "bytes normalizados a LF**)"),

    ("`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, que mide **4054129 bytes en disco y"
     + NL + "4054129 bytes normalizados a LF**",
     "`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, que mide **4054129 bytes en disco y "
     "4054129 bytes normalizados a LF**"),

    ("`docs/loop/reportes/REPORTE_V174.md` **existe, 32568 bytes** |",
     "`docs/loop/reportes/REPORTE_V174.md` **existe, 32568 bytes en disco y 32568 "
     "bytes normalizados a LF** |"),

    ("**crecimiento de 10522 bytes**. **La segunda corrida sella" + NL
     + "IDEMPOTENTE**: **0 entradas escritas** y **crecimiento 0 bytes**,",
     "**crecimiento de 10522 bytes en disco y de 10522 bytes normalizados a LF**. "
     "**La segunda corrida sella IDEMPOTENTE**: **0 entradas escritas** y "
     "**crecimiento de 0 bytes en disco y de 0 bytes normalizados a LF**,"),

    ("**4054129 bytes en disco" + NL
     + "  y 4054129 normalizados a LF**, con `sha256` `0a77b5a35a962621` de disco y" + NL
     + "  `0a77b5a35a962621` de LF,",
     "**4054129 bytes en disco y 4054129 bytes normalizados a LF**, con `sha256` "
     "`0a77b5a35a962621` de disco y `0a77b5a35a962621` de LF,"),
]

# LA SEGUNDA FAMILIA DE ARREGLOS, Y LA TRAJO LA MISMA GUARDA EN SU SEGUNDA
# PASADA: `parejas_de_convenciones_que_no_calzan()` reprobo DOS parejas que
# estaban COMPLETAS y eran FALSAS. La frase publicaba, pegado a la ruta, EL
# TAMANO DE ANTES, y la guarda lo leia como el tamano de esa ruta, CON RAZON:
# lo que va detras de una ruta es el tamano de esa ruta. El remedio es el que la
# vuelta 201 dejo escrito cuando le paso lo mismo: PONER DETRAS DE CADA RUTA SU
# TAMANO MEDIDO, y el de antes detras, NUNCA QUITAR LA CIFRA.
ARREGLOS_DEL_SUJETO = [
    ("`docs/plan/OPERACIONES.jsonl` entra midiendo **499474 bytes en disco y "
     "499474 bytes normalizados a LF** y sale midiendo **501883 bytes en disco y "
     "501883 bytes normalizados a LF**, con un **crecimiento de 2409 bytes en "
     "disco y de 2409 bytes normalizados a LF**;",
     "`docs/plan/OPERACIONES.jsonl` mide AL SALIR **501883 bytes en disco y "
     "501883 bytes normalizados a LF**, y ANTES de esta correccion media "
     "**499474 bytes en disco y 499474 bytes normalizados a LF**, con un "
     "**crecimiento de 2409 bytes en disco y de 2409 bytes normalizados a LF**;"),

    ("`docs/PENDIENTES.md` entra midiendo **1091080 bytes en disco y 1091080 bytes"
     + NL + "normalizados a LF** y sale midiendo **1101602 bytes en disco y 1101602 bytes"
     + NL + "normalizados a LF**: **crecimiento de 10522 bytes en disco y de 10522 bytes "
     "normalizados a LF**.",
     "`docs/PENDIENTES.md` mide AL SALIR **1101602 bytes en disco y 1101602 bytes "
     "normalizados a LF**, y ANTES de estas dos entradas media **1091080 bytes en "
     "disco y 1091080 bytes normalizados a LF**, con un **crecimiento de 10522 "
     "bytes en disco y de 10522 bytes normalizados a LF**."),
]

ARREGLOS = ARREGLOS + ARREGLOS_DEL_SUJETO


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    total = 0
    for rel in DESTINOS:
        ruta = os.path.join(RAIZ, rel.replace("/", os.sep))
        if not os.path.isfile(ruta):
            print("   NO EXISTE: %s" % rel)
            continue
        t = io.open(ruta, encoding="utf-8").read().replace(chr(13) + NL, NL)
        antes = len(t.encode("utf-8"))
        n_fichero = 0
        for viejo, nuevo in ARREGLOS:
            n = t.count(viejo)
            if n:
                t = t.replace(viejo, nuevo)
                n_fichero += n
        if n_fichero:
            io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
        despues = len(t.encode("utf-8"))
        print("   %-38s arreglos aplicados: %2d | %d bytes en disco antes y %d "
              "bytes en disco despues" % (rel, n_fichero, antes, despues))
        total += n_fichero
    print("")
    print("CIFRA arreglos declarados: %d" % len(ARREGLOS))
    print("CIFRA arreglos aplicados en total: %d" % total)
    print("NINGUNA CIFRA SE QUITO: cada arreglo JUNTA la cifra con su pareja o")
    print("   ANADE la segunda convencion medida. La primera nunca se borra.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
