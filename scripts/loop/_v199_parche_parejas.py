# -*- coding: utf-8 -*-
"""_v199_parche_parejas.py . PARCHE DE UN SOLO USO. Pone LAS DOS CONVENCIONES,
disco y LF, en la misma linea de cada cifra de bytes o sha que el reporte publica,
que es lo que la guarda de `cerrar_reporte.py` exige desde la vuelta 178 (TAREA
1.e, adjudicacion 7.11 del acta 177). Las quince cifras las nombro la guarda, y
las dos convenciones se REMIDIERON del disco en esta vuelta.

Se aplica al reporte Y a los cuerpos de tarea de los que salio, para que los dos
digan lo mismo. NO cambia ninguna cifra: la anade."""
import io
import os

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SL = os.path.join(RAIZ, "scripts", "loop")
DESTINOS = [
    os.path.join(RAIZ, "docs", "loop", "REPORTE.md"),
    os.path.join(SL, "_v199_t1_seccion.md"),
    os.path.join(SL, "_v199_t2_seccion.md"),
    os.path.join(SL, "_v199_t3_seccion.md"),
    os.path.join(SL, "_v199_t4_seccion.md"),
    os.path.join(SL, "_v199_cierre_texto.md"),
]

CAMBIOS = [
    # TAREA 1
    ("**LA SEDE DE VERDAD NO SE MOVIO:** `789 bytes, sha256 52a780c072700280` al entrar y" + NL
     + "al salir del arnes.",
     "**LA SEDE DE VERDAD NO SE MOVIO**, y va con las dos convenciones porque la de" + NL
     + "bytes no esta fijada: `789 bytes en disco y 789 normalizado a LF`, `sha256 disco" + NL
     + "52a780c072700280 y sha256 LF 52a780c072700280`, al entrar y al salir del arnes."),
    # TAREA 2
    ("**`789 bytes, sha256 52a780c072700280`** al entrar y **lo mismo** al salir,",
     "**`789 bytes en disco y 789 normalizado a LF`**, **`sha256 disco 52a780c072700280 y sha256 LF 52a780c072700280`**, al entrar y al salir,"),
    ("| **M1** | solo la REDIRECCION | **la GUARDA muerde**: exitcode 1 y la sede queda intacta, `sha256 52a780c072700280` |",
     "| **M1** | solo la REDIRECCION | **la GUARDA muerde**: exitcode 1 y la sede queda intacta, `sha256 disco 52a780c072700280 y sha256 LF 52a780c072700280` |"),
    # TAREA 3
    ("| banco medido hoy | 182228 bytes, `sha256` LF `68557cd00a3124f4`, 3119 lineas |",
     "| banco medido hoy | 182228 bytes en disco y 182228 normalizado a LF, `sha256 disco 68557cd00a3124f4 y sha256 LF 68557cd00a3124f4`, 3119 lineas |"),
    # TAREA 4
    ("**VERDE**. Su registro propio mide **51368 bytes**, `sha256` LF" + NL
     + "`d93c59a86372cf50`.",
     "**VERDE**. Su registro propio mide **51368 bytes en disco y 51368 normalizado a LF**, con `sha256 disco d93c59a86372cf50 y sha256 LF d93c59a86372cf50`."),
    ("`docs/INTRA_DOMINIO_INFORME.md` (943970 bytes, 4 aciertos de cabecera con el 52) y",
     "`docs/INTRA_DOMINIO_INFORME.md` (943970 bytes en disco y 943970 normalizado a LF, 4 aciertos de cabecera con el 52) y"),
    ("`docs/BANCO_DE_TEXTOS.md` (182228 bytes, 1 acierto de `TABLA VIVA DE LOS PUROS`).",
     "`docs/BANCO_DE_TEXTOS.md` (182228 bytes en disco y 182228 normalizado a LF, 1 acierto de `TABLA VIVA DE LOS PUROS`)."),
    ("vez de ajustarse**. `docs/plan/INVENTARIO.jsonl` mide **584554 bytes**, `sha256`" + NL
     + "LF `69666b73339f2afe`, **672 filas no vacias**.",
     "vez de ajustarse**. `docs/plan/INVENTARIO.jsonl` mide **584554 bytes en disco y 584554 normalizado a LF**, con `sha256 disco 69666b73339f2afe y sha256 LF 69666b73339f2afe`, y **672 filas no vacias**."),
    ("`docs/plan/10_INVENTARIO.md`, existe con **34258 bytes y 414 lineas**, con el",
     "`docs/plan/10_INVENTARIO.md`, existe con **34258 bytes en disco y 33845 normalizado a LF**, que aqui NO coinciden y por eso se publican las dos, y **414 lineas**, con el"),
    # CIERRE, seccion 4
    ("**4054129 bytes en disco y `sha256` disco `0a77b5a35a962621`** (bloque `D` de la" + NL
     + "  apertura) y **cierra en el mismo valor**.",
     "**4054129 bytes en disco y 4054129 normalizado a LF**, con `sha256 disco 0a77b5a35a962621 y sha256 LF 0a77b5a35a962621` (bloque `D` de la apertura), y **cierra en los mismos valores**."),
    ("- **La sede del turno del auditor no se movio:** `789 bytes, sha256" + NL
     + "  52a780c072700280` al entrar y al salir, medido tres veces por tres instrumentos" + NL
     + "  distintos.",
     "- **La sede del turno del auditor no se movio:** `789 bytes en disco y 789 normalizado a LF`, `sha256 disco 52a780c072700280 y sha256 LF 52a780c072700280`, al entrar y al salir, medido tres veces por tres instrumentos distintos."),
]

for ruta in DESTINOS:
    if not os.path.isfile(ruta):
        print("NO EXISTE, se salta: %s" % ruta)
        continue
    t = io.open(ruta, encoding="utf-8").read().replace(chr(13) + NL, NL)
    tocados = 0
    for viejo, nuevo in CAMBIOS:
        if viejo in t:
            t = t.replace(viejo, nuevo)
            tocados += 1
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print("%-56s %d cambio(s)" % (os.path.relpath(ruta, RAIZ), tocados))
