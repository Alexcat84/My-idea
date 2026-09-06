# -*- coding: utf-8 -*-
"""_v188_parejas_del_reporte.py . PONE SU PAREJA A CADA CIFRA DEL REPORTE DE LA
188 QUE LA GUARDA `cifras_sin_pareja()` ACUSO, Y LO HACE A LA VEZ EN
`docs/loop/REPORTE.md` Y EN LOS FICHEROS DE SECCION DE LOS QUE SALIO, PARA QUE LOS
DOS DIGAN LO MISMO.

Auxiliar de una sola vuelta: no es guarda, no entra en la nomina y no publica
ninguna cifra propia. NINGUNA CIFRA CAMBIA DE VALOR: lo que cambia es que cada
una lleve al lado su otra convencion, medida y no supuesta.
"""
import io
import os

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DESTINOS = [
    "docs/loop/REPORTE.md",
    "scripts/loop/_v188_t1_seccion.md",
    "scripts/loop/_v188_t2_seccion.md",
    "scripts/loop/_v188_t3_seccion.md",
    "scripts/loop/_v188_t4_seccion.md",
    "scripts/loop/_v188_t5_seccion.md",
    "scripts/loop/_v188_cierre_texto.md",
]

CAMBIOS = [
    # --- TAREA 1
    ("La sede pasa de **924954 a 943276 bytes**, la" + NL
     + "entrada mide **18321 bytes** y **195 lineas**, esta byte a byte tras releerla del",
     "La sede pasa de **924954 bytes a 943276 bytes**, la entrada mide" + NL
     + "**18321 bytes en disco y 18321 bytes normalizados a LF** y **195 lineas**," + NL
     + "esta byte a byte tras releerla del"),
    # --- TAREA 2
    ("`LD-01` a `LD-11`). `docs/plan/LECTURAS_DIRIGIDAS.md` mide **214916 bytes por" + NL
     + "  las dos convenciones**, `sha256` LF `dda1cdd67042c733` y **2230 lineas**. **Las",
     "`LD-01` a `LD-11`). `docs/plan/LECTURAS_DIRIGIDAS.md` mide" + NL
     + "  **214916 bytes en disco y 214916 bytes normalizados a LF**, su `sha256`" + NL
     + "  normalizado a LF es `dda1cdd67042c733`, y tiene **2230 lineas**. **Las"),
    ("`docs/plan/LECTURAS_DIRIGIDAS.md` existe (**214916 bytes por las dos" + NL
     + "  convenciones**) y trae **en cabecera las 11 de 11** que la ficha describe.",
     "`docs/plan/LECTURAS_DIRIGIDAS.md` existe" + NL
     + "  (**214916 bytes en disco y 214916 bytes normalizados a LF**) y trae **en" + NL
     + "  cabecera las 11 de 11** que la ficha describe."),
    ("(`docs/plan/BANCO_DEL_PLAN.md`, **61554 bytes**, y" + NL
     + "  `docs/plan/LECTURAS_DIRIGIDAS.md`, **214916 bytes**), pero **lo que falta",
     "(`docs/plan/BANCO_DEL_PLAN.md`, **61554 bytes en disco y 61554 bytes" + NL
     + "  normalizados a LF**, y `docs/plan/LECTURAS_DIRIGIDAS.md`, **214916 bytes en" + NL
     + "  disco y 214916 bytes normalizados a LF**), pero **lo que falta"),
    ("(**584554 bytes por las dos convenciones**) con **672 entradas, las 672 JSON",
     "(**584554 bytes en disco y 584554 bytes normalizados a LF**) con **672" + NL
     + "  entradas, las 672 JSON"),
    # --- TAREA 3
    ("`sha256` LF `2e37089d0389e67e`):",
     "su `sha256` normalizado a LF es `2e37089d0389e67e`):"),
    ("`docs/loop/SALIDA_V186_T2C_MUTACION_CIERRE_TARDIO.txt` (**7544 bytes por las dos" + NL
     + "convenciones**, `sha256` LF `be4edc90f2889552`): **`CIFRA casos: 22 | pasan:",
     "`docs/loop/SALIDA_V186_T2C_MUTACION_CIERRE_TARDIO.txt`" + NL
     + "(**7544 bytes en disco y 7544 bytes normalizados a LF**, con su `sha256`" + NL
     + "normalizado a LF en `be4edc90f2889552`): **`CIFRA casos: 22 | pasan:"),
    ("`SALIDA_V186_T2A_MUTACION_PIEZA4.txt` cierra en **3906 bytes por las dos" + NL
     + "convenciones**, `sha256` LF `2b444ffe193d27f9`, y su arnes sigue en",
     "`SALIDA_V186_T2A_MUTACION_PIEZA4.txt` cierra en" + NL
     + "**3906 bytes en disco y 3906 bytes normalizados a LF**, con su `sha256`" + NL
     + "normalizado a LF en `2b444ffe193d27f9`, y su arnes sigue en"),
    ("`docs/loop/SALIDA_V188_T3C_MUTACION_EXCLUSION_POR_ROJO.txt` (**3565 bytes por las" + NL
     + "dos convenciones**, `sha256` LF `622b67673e6d75f4`), **`CIFRA casos: 11 | pasan:",
     "`docs/loop/SALIDA_V188_T3C_MUTACION_EXCLUSION_POR_ROJO.txt`" + NL
     + "(**3565 bytes en disco y 3565 bytes normalizados a LF**, con su `sha256`" + NL
     + "normalizado a LF en `622b67673e6d75f4`), **`CIFRA casos: 11 | pasan:"),
    # --- TAREA 5
    ("| `sha256` LF de la ciega |", "| `sha256`, normalizado a LF, de la ciega |"),
    ("| `sha256` LF del destape |", "| `sha256`, normalizado a LF, del destape |"),
    ("`docs/loop/_auditor_v189_exclusion.txt` mide **1648 bytes por las dos" + NL
     + "convenciones** y lista **351 puestos distintos**",
     "`docs/loop/_auditor_v189_exclusion.txt` mide" + NL
     + "**1648 bytes en disco y 1648 bytes normalizados a LF** y lista **351 puestos" + NL
     + "distintos**"),
    ("**`docs/loop/DISCUTIBLES_DE_CLASE_V188.txt` esta escrito**, mide **10 bytes por" + NL
     + "las dos convenciones**, `sha256` LF `7f3c48b9b2a06c3c`, y **dentro dice",
     "**`docs/loop/DISCUTIBLES_DE_CLASE_V188.txt` esta escrito**, mide" + NL
     + "**10 bytes en disco y 10 bytes normalizados a LF**, su `sha256` normalizado a" + NL
     + "LF es `7f3c48b9b2a06c3c`, y **dentro dice"),
    ("corridas del mismo dia sobre el mismo sujeto (`sha256` LF `6e056e2b9d049861` y" + NL
     + "luego `edd65316f5312cd4`).",
     "corridas del mismo dia sobre el mismo sujeto: su `sha256` normalizado a LF fue" + NL
     + "`6e056e2b9d049861` y luego `edd65316f5312cd4`."),
    # --- CIERRE
    ("`sha256` LF **`6e056e2b9d049861`** en la primera corrida y",
     "su `sha256` normalizado a LF fue **`6e056e2b9d049861`** en la primera corrida y"),
]


def main():
    for rel in DESTINOS:
        p = os.path.join(RAIZ, rel.replace("/", os.sep))
        if not os.path.isfile(p):
            print("NO EXISTE, se salta: %s" % rel)
            continue
        t = io.open(p, encoding="utf-8").read().replace(chr(13) + NL, NL)
        antes = len(t.encode("utf-8"))
        n = 0
        for viejo, nuevo in CAMBIOS:
            if viejo in t:
                t = t.replace(viejo, nuevo)
                n += 1
        if n:
            io.open(p, "w", encoding="utf-8", newline=NL).write(t)
        print("%-44s cambios aplicados: %-3d bytes %d -> %d"
              % (rel, n, antes, len(t.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
