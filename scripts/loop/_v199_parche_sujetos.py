# -*- coding: utf-8 -*-
"""_v199_parche_sujetos.py . PARCHE DE UN SOLO USO. Pone LA RUTA DEL SUJETO en la
misma linea que su pareja de convenciones, que es lo que la guarda de
`cerrar_reporte.py` necesita para atribuir una cifra de bytes a un fichero.

POR QUE, Y ES UNA CAIDA MIA QUE LA GUARDA AJENA CAZO: la pareja `789 / 789` de la
seccion de la TAREA 2 quedaba debajo de una linea que nombra
`SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt`, asi que la guarda se la atribuyo A
ESE fichero y la coteja contra sus 5603 bytes. **La guarda tiene razon:** el 789 es
de la sede del turno y la linea no lo decia. Se arregla NOMBRANDO EL SUJETO, no
quitando la cifra."""
import io
import os

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SL = os.path.join(RAIZ, "scripts", "loop")
DESTINOS = [os.path.join(RAIZ, "docs", "loop", "REPORTE.md"),
            os.path.join(SL, "_v199_t1_seccion.md"),
            os.path.join(SL, "_v199_t2_seccion.md"),
            os.path.join(SL, "_v199_t3_seccion.md"),
            os.path.join(SL, "_v199_t4_seccion.md"),
            os.path.join(SL, "_v199_cierre_texto.md")]

CAMBIOS = [
    ("**LA SEDE DE VERDAD NO SE MOVIO**, y va con las dos convenciones porque la de" + NL
     + "bytes no esta fijada: `789 bytes en disco y 789 normalizado a LF`, `sha256 disco" + NL
     + "52a780c072700280 y sha256 LF 52a780c072700280`, al entrar y al salir del arnes.",
     "**LA SEDE DE VERDAD NO SE MOVIO**, y va con su ruta delante y con las dos convenciones, porque la de bytes no esta fijada:" + NL
     + "`docs/loop/_TURNO_DEL_AUDITOR.json` mide 789 bytes en disco y 789 normalizado a LF, con `sha256 disco 52a780c072700280 y sha256 LF 52a780c072700280`, al entrar y al salir del arnes."),
    ("una constante literal: las dos salen de `sede_medida()`. Corrida de hoy, leida de" + NL
     + "`docs/loop/SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt`:" + NL
     + "**`789 bytes en disco y 789 normalizado a LF`**, **`sha256 disco 52a780c072700280 y sha256 LF 52a780c072700280`**, al entrar y al salir," + NL
     + "**`CIFRA fallos: 0`, VEREDICTO VERDE**. Los catorce casos que ese arnes ya probaba" + NL
     + "siguen enteros: ningun esperado se aflojo y ningun escenario se quito.",
     "una constante literal: las dos salen de `sede_medida()`. Corrida de hoy, leida de" + NL
     + "`docs/loop/SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt`, que cierra con" + NL
     + "**`CIFRA fallos: 0`, VEREDICTO VERDE**." + NL + NL
     + "**LA SEDE, CON SU RUTA EN LA MISMA LINEA QUE SU CIFRA:** `docs/loop/_TURNO_DEL_AUDITOR.json` mide 789 bytes en disco y 789 normalizado a LF, con `sha256 disco 52a780c072700280 y sha256 LF 52a780c072700280`, al entrar y al salir." + NL + NL
     + "Los catorce casos que ese arnes ya probaba" + NL
     + "siguen enteros: ningun esperado se aflojo y ningun escenario se quito."),
    ("| banco medido hoy | 182228 bytes en disco y 182228 normalizado a LF, `sha256 disco 68557cd00a3124f4 y sha256 LF 68557cd00a3124f4`, 3119 lineas | `SALIDA_V199_T3_EJEMPLARES_DEL_BANCO.txt` |",
     "| `docs/BANCO_DE_TEXTOS.md` medido hoy | 182228 bytes en disco y 182228 normalizado a LF, `sha256 disco 68557cd00a3124f4 y sha256 LF 68557cd00a3124f4`, 3119 lineas | la sellada de esta tarea |"),
    ("**VERDE**. Su registro propio mide **51368 bytes en disco y 51368 normalizado a LF**, con `sha256 disco d93c59a86372cf50 y sha256 LF d93c59a86372cf50`.",
     "**VERDE**. Su registro propio `docs/plan/OP_L_03_LECTURAS.jsonl` mide **51368 bytes en disco y 51368 normalizado a LF**, con `sha256 disco d93c59a86372cf50 y sha256 LF d93c59a86372cf50`."),
    ("- **La sede del turno del auditor no se movio:** `789 bytes en disco y 789 normalizado a LF`, `sha256 disco 52a780c072700280 y sha256 LF 52a780c072700280`, al entrar y al salir, medido tres veces por tres instrumentos distintos.",
     "- **La sede del turno del auditor no se movio:** `docs/loop/_TURNO_DEL_AUDITOR.json` mide 789 bytes en disco y 789 normalizado a LF, con `sha256 disco 52a780c072700280 y sha256 LF 52a780c072700280`, al entrar y al salir, medido tres veces por tres instrumentos distintos."),
]

for ruta in DESTINOS:
    if not os.path.isfile(ruta):
        continue
    t = io.open(ruta, encoding="utf-8").read().replace(chr(13) + NL, NL)
    n = 0
    for viejo, nuevo in CAMBIOS:
        if viejo in t:
            t = t.replace(viejo, nuevo)
            n += 1
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print("%-56s %d cambio(s)" % (os.path.relpath(ruta, RAIZ), n))
