# -*- coding: utf-8 -*-
r"""vuelta172_tarea1b_confirmar_r41.py . ANEXA AL `R.41` LA CONFIRMACION MEDIDA
DE SUS DOCE GLOSAS, POR ADICION Y SIN TOCAR UNA LETRA DE ARRIBA.

EL NOMBRE LLEVA `vuelta172` Y NO `vuelta174`, Y ESO ES A PROPOSITO. Este es el
fichero que el recuadro de apertura del `R.41` PROMETE con estas palabras
exactas, leidas hoy en `docs/PENDIENTES.md:12455`: *"la confirmacion MEDIDA se
anexa al cierre de la vuelta, por adicion y sin tocar una letra de arriba, con
`scripts/loop/vuelta172_tarea1b_confirmar_r41.py`"*. **Renombrarlo dejaria la
promesa apuntando igual a un vacio.** Nace en la vuelta 174, TAREA 2.b, y eso va
dicho dentro del bloque que escribe.

POR QUE IMPORTA QUE EXISTA (clausula 4.5 del acta del auditor de la vuelta 172,
`docs/loop/ACTA_AUDITOR.md:58674`, leida hoy): la entrada llevaba **dos vueltas**
nombrando un fichero que no existia, y desde el 5 sep 2026 eso tiene nombre
propio en `EJECUTOR.md` 1, **LA RUTA QUE PROMETE PRUEBA ES CIFRA**: una ruta
publicada como evidencia que apunta a un fichero inexistente o de cero bytes es
CAIDA DE CIFRA en su sede.

QUE MIDE, Y DE DONDE. Cada una de las doce glosas del `R.41` dice, en futuro,
*"VA A EJECUTARSE EN LA TAREA n DE ESTA VUELTA, Y AL ESCRIBIR ESTA LINEA TODAVIA
NO HA CORRIDO"* o bien *"SE ACATA SIN TOCAR NADA"*. La confirmacion cruza dos
cosas y **no teclea ninguna**:

  (i)  EL NUMERO DE TAREA QUE CADA GLOSA NOMBRA, extraido del propio texto del
       `R.41` con una expresion regular;
  (ii) EL ESTADO DE ESA TAREA, leido de la tabla de tareas del reporte de la
       vuelta 172 **ya cerrado y archivado**, `docs/loop/reportes/REPORTE_V172.md`.

**Y POR ESO ESTE INSTRUMENTO NO PODIA CORRER ANTES DE HOY, NI EN LA 172 NI EN LA
173:** su fuente de estados es un reporte que nadie habia cerrado. La vuelta 172
murio sin cerrarlo y la 173 tampoco lo cerro. **La TAREA 1.a de la vuelta 174 lo
cerro y lo archivo, y solo entonces hubo algo que medir.** Eso no excusa las dos
vueltas de promesa vacia: la explica.

CAE EN ROJO Y NO ESCRIBE NADA si su fuente de estados no existe o mide cero
bytes, que es la regla del 5 sep 2026 aplicada a si mismo: **un instrumento que
nace para arreglar una ruta sobre un vacio no puede leer de otro vacio.**

LA SIMULACION VA SOBRE COPIA EN MEMORIA (`AUDITOR.md` 3): `bloque_de_confirmacion()`
y `anexar_al_r41()` son PURAS, reciben los textos y devuelven texto. Su caso
positivo por mutacion es `scripts/loop/vuelta174_tarea2b_mutacion_confirmar.py`.

USO:
  python scripts/loop/vuelta172_tarea1b_confirmar_r41.py
  python scripts/loop/vuelta172_tarea1b_confirmar_r41.py --solo-comprobar
"""
import argparse
import io
import os
import re
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SEDE = os.path.join(RAIZ, "docs", "PENDIENTES.md")
FUENTE_ESTADOS = os.path.join(RAIZ, "docs", "loop", "reportes", "REPORTE_V172.md")

CAB_R41 = "## R.41."
MARCA_BLOQUE = "LA CONFIRMACION MEDIDA DE LAS DOCE GLOSAS, ANEXADA POR ADICION"

# LA GLOSA NOMBRA SU TAREA, Y EL NUMERO SE EXTRAE, NO SE TECLEA.
PAT_ADJ = re.compile(r"^\s*-\s+\*\*(6\.\d+)\s+\(`([^`]+)`,\s*leida hoy\)\.\s*"
                     r"VIA PREVISTA:\s*([A-Z ]+?)\.\*\*")
PAT_TAREA = re.compile(r"VA A EJECUTARSE EN LA TAREA (\d+)(\.[a-z])?\b")
PAT_ACATA = re.compile(r"SE ACATA SIN TOCAR NADA")
# LA FILA DE LA TABLA DE TAREAS DEL REPORTE, CON SUS CUATRO CELDAS.
PAT_FILA = re.compile(r"^\|\s*\*\*TAREA (\d+)\*\*\s*\|")


def leer(ruta):
    return io.open(ruta, encoding="utf-8").read().replace(chr(13) + NL, NL)


def acotar_r41(texto):
    """LAS LINEAS DEL `R.41`, ACOTADAS POR SU CABECERA Y POR LA SIGUIENTE `## R.`
    o el final. Devuelve `(inicio, fin)` en indices de caracter, o
    `(None, motivo)`. PURA."""
    if texto.count(NL + CAB_R41) != 1:
        return None, ("la cabecera %r aparece %d veces y tiene que aparecer UNA"
                      % (CAB_R41, texto.count(NL + CAB_R41)))
    i = texto.index(NL + CAB_R41) + 1
    m = re.search(r"^## R\.\d+\.", texto[i + len(CAB_R41):], re.M)
    fin = i + len(CAB_R41) + m.start() if m else len(texto)
    return (i, fin), None


def glosas_del_r41(bloque):
    """LAS DOCE GLOSAS, LEIDAS DEL BLOQUE. Devuelve
    `[(clave, via_prevista, tarea, linea_del_acta)]`, con `tarea` como cadena
    (`'2.a'`, `'3'`) o `None` cuando la glosa dice SE ACATA SIN TOCAR NADA.
    PURA: recibe el texto."""
    halladas = []
    lineas = bloque.split(NL)
    for k, l in enumerate(lineas):
        m = PAT_ADJ.match(l)
        if not m:
            continue
        clave, sede_linea, via = m.group(1), m.group(2), m.group(3).strip()
        # La glosa vive en las lineas siguientes hasta la proxima vineta.
        cuerpo = []
        j = k + 1
        while j < len(lineas) and not PAT_ADJ.match(lineas[j]):
            cuerpo.append(lineas[j])
            j += 1
        texto_glosa = " ".join(cuerpo)
        mt = PAT_TAREA.search(texto_glosa)
        if mt:
            tarea = mt.group(1) + (mt.group(2) or "")
        elif PAT_ACATA.search(texto_glosa):
            tarea = None
        else:
            tarea = "?"
        halladas.append((clave, via, tarea, sede_linea))
    return halladas


def estados_del_reporte(texto):
    """EL ESTADO DE CADA TAREA, LEIDO DE LA TABLA DEL REPORTE. Devuelve
    `{numero: celda_de_estado}`. PURA."""
    estados = {}
    for l in texto.split(NL):
        m = PAT_FILA.match(l)
        if not m:
            continue
        celdas = l.split(" | ")
        if len(celdas) != 4:
            continue
        estados[m.group(1)] = celdas[2].strip()
    return estados


def bloque_de_confirmacion(glosas, estados, bytes_fuente):
    """EL BLOQUE QUE SE ANEXA. Devuelve `(texto, motivos)`. PURA: no lee ni
    escribe, para que su caso positivo la pueda tumbar sin tocar el repo."""
    motivos = []
    if not glosas:
        motivos.append("no se leyo ninguna glosa del R.41")
    if not estados:
        motivos.append("no se leyo ninguna fila de la tabla de tareas del reporte")
    sin_tarea = [c for c, _v, t, _s in glosas if t == "?"]
    if sin_tarea:
        motivos.append("estas glosas no dicen ni su tarea ni que se acaten: %s"
                       % ", ".join(sin_tarea))
    if motivos:
        return "", motivos

    filas = []
    n_conf = 0
    for clave, via, tarea, sede_linea in glosas:
        if tarea is None:
            filas.append("| `%s` | %s | (ninguna: se acata) | (no aplica) |"
                         % (clave, via))
            continue
        raiz = tarea.split(".")[0]
        estado = estados.get(raiz)
        if estado is None:
            filas.append("| `%s` | %s | TAREA %s | **LA TABLA DEL REPORTE NO TRAE ESA FILA** |"
                         % (clave, via, tarea))
        else:
            filas.append("| `%s` | %s | TAREA %s | %s |" % (clave, via, tarea, estado))
            n_conf += 1

    reparto = {}
    for _c, via, _t, _s in glosas:
        reparto[via] = reparto.get(via, 0) + 1
    linea_reparto = "; ".join("%s: %d" % (v, reparto[v]) for v in sorted(reparto))

    texto = (
        NL +
        "**%s** (vuelta 174, TAREA 2.b, con" % MARCA_BLOQUE + NL +
        "`scripts/loop/vuelta172_tarea1b_confirmar_r41.py`, que es el fichero que el" + NL +
        "recuadro de arriba nombra). **NI UNA LETRA DE LO ESCRITO ARRIBA SE TOCA:** esto" + NL +
        "va detras, por adicion, exactamente como la entrada prometio." + NL + NL +
        "**LAS DOS COLUMNAS SE MIDEN, NO SE TECLEAN.** La tarea que cada glosa nombra se" + NL +
        "extrae del texto de arriba con una expresion regular; el estado sale de la tabla" + NL +
        "de tareas de `docs/loop/reportes/REPORTE_V172.md` (**%d bytes**, medidos con" % bytes_fuente + NL +
        "`os.path.getsize` en esta corrida)." + NL + NL +
        "| adjudicacion del acta 171 | VIA PREVISTA que se escribio | tarea que la glosa nombra | estado de esa tarea, medido hoy |" + NL +
        "|---|---|---|---|" + NL +
        NL.join(filas) + NL + NL +
        "**CIFRA glosas: %d | reparto por VIA PREVISTA: %s.**" % (len(glosas), linea_reparto) + NL +
        "**CIFRA glosas con tarea nombrada y estado hallado: %d.**" % n_conf + NL + NL +
        "**POR QUE ESTO NO PUDO ESCRIBIRSE ANTES DE HOY, Y NO ES UNA EXCUSA SINO LA" + NL +
        "CAUSA MEDIDA.** La fuente de la ultima columna es el reporte de la vuelta 172" + NL +
        "**cerrado y archivado**, y ese fichero no existio hasta la TAREA 1.a de la" + NL +
        "vuelta 174: la 172 murio sin cerrarlo y la 173 tampoco lo cerro. **Eso no" + NL +
        "excusa las dos vueltas en que esta entrada nombro un fichero inexistente**" + NL +
        "(clausula `4.5` del acta del auditor de la vuelta 172), que desde el 5 sep 2026" + NL +
        "es CAIDA DE CIFRA por la regla LA RUTA QUE PROMETE PRUEBA ES CIFRA." + NL + NL +
        "**Y UN CONTRASTE QUE NO SE RESUELVE COPIANDO, PORQUE LAS DOS COSAS SON" + NL +
        "CIERTAS.** Las filas que apuntan a la TAREA 4 leen el estado de la fila entera," + NL +
        "que es el que el reporte publica. La clausula `4.6` del acta del auditor de la" + NL +
        "vuelta 172 midio aparte que **la 4.a y la 4.b si estan hechas y verificadas** y" + NL +
        "que lo unico que falta es la `4.c`. **La tabla de arriba dice lo que dice la" + NL +
        "fila; la clausula dice lo que midio el auditor. La discrepancia se declara en" + NL +
        "vez de resolverse eligiendo una** (`EJECUTOR.md` 2)." + NL)
    return texto, []


def anexar_al_r41(texto_sede, bloque):
    """LA ANEXION, SOBRE COPIA EN MEMORIA. Devuelve `(texto_nuevo, motivos)`.
    Si hay motivos, `texto_nuevo` es el ORIGINAL sin tocar. PURA."""
    if MARCA_BLOQUE in texto_sede:
        return texto_sede, ["la confirmacion YA ESTA anexada: no se escribe dos veces"]
    corte, motivo = acotar_r41(texto_sede)
    if motivo:
        return texto_sede, [motivo]
    ini, fin = corte
    if not bloque.strip():
        return texto_sede, ["el bloque de confirmacion esta vacio"]
    nuevo = texto_sede[:fin].rstrip(NL) + NL + bloque + texto_sede[fin:]
    if nuevo[:ini] != texto_sede[:ini]:
        return texto_sede, ["se toco texto de ANTES del R.41"]
    if texto_sede[:fin].rstrip(NL) != nuevo[:len(texto_sede[:fin].rstrip(NL))]:
        return texto_sede, ["se toco una letra de arriba dentro del R.41"]
    if len(nuevo) <= len(texto_sede):
        return texto_sede, ["la anexion no es adicion pura: el texto no crecio"]
    # LA GUARDA MIRA EL DELTA, NO EL TOTAL, y el motivo esta medido: la sede es
    # un fichero historico que YA trae guiones largos de 2026 (la TAREA 2.b de
    # la vuelta 172 conto 54 y lo dejo escrito). Una guarda sobre el total se
    # caeria por culpa de texto viejo que nadie escribio hoy, y una guarda que
    # se cae siempre acaba saltandose.
    for malo, nombre in ((chr(8212), "largos"), (chr(8211), "medios")):
        if nuevo.count(malo) != texto_sede.count(malo):
            return texto_sede, ["se colaron guiones %s: el fichero tenia %d y "
                                "quedaria con %d"
                                % (nombre, texto_sede.count(malo), nuevo.count(malo))]
    return nuevo, []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo-comprobar", action="store_true")
    a = ap.parse_args()

    print("=" * 78)
    print("LA CONFIRMACION MEDIDA DEL `R.41`, ANEXADA POR ADICION")
    print("=" * 78)
    print("")

    print("A) LA FUENTE DE LOS ESTADOS, MEDIDA ANTES DE LEERLA")
    print("   (LA RUTA QUE PROMETE PRUEBA ES CIFRA, EJECUTOR.md 1, 5 sep 2026:")
    print("    este instrumento no puede leer de otro vacio)")
    rel_fuente = "docs/loop/reportes/REPORTE_V172.md"
    if not os.path.exists(FUENTE_ESTADOS):
        print("   %s -> NO EXISTE" % rel_fuente)
        print("")
        print("ROJO: sin fuente de estados no hay nada que confirmar. No se escribe.")
        return 1
    bytes_fuente = os.path.getsize(FUENTE_ESTADOS)
    print("   %s -> %d bytes" % (rel_fuente, bytes_fuente))
    if bytes_fuente == 0:
        print("")
        print("ROJO: la fuente de estados mide CERO BYTES. No se escribe.")
        return 1
    reporte = leer(FUENTE_ESTADOS)
    estados = estados_del_reporte(reporte)
    print("   CIFRA filas de tarea leidas de su tabla: %d" % len(estados))
    for k in sorted(estados, key=int):
        print("      TAREA %-3s %s" % (k, estados[k][:96]))
    print("")

    print("B) EL `R.41`, ACOTADO Y CON SUS GLOSAS LEIDAS")
    sede = leer(SEDE)
    corte, motivo = acotar_r41(sede)
    if motivo:
        print("   " + motivo)
        print("")
        print("ROJO: no se puede acotar el R.41. No se escribe nada.")
        return 1
    ini, fin = corte
    bloque_r41 = sede[ini:fin]
    print("   docs/PENDIENTES.md -> %d bytes" % len(sede.encode("utf-8")))
    print("   el R.41 ocupa los bytes %d a %d (%d bytes, %d lineas)"
          % (ini, fin, len(bloque_r41.encode("utf-8")), bloque_r41.count(NL)))
    glosas = glosas_del_r41(bloque_r41)
    print("   CIFRA glosas leidas: %d" % len(glosas))
    for clave, via, tarea, sede_linea in glosas:
        print("      %-5s VIA PREVISTA %-15s tarea nombrada: %-6s (%s)"
              % (clave, via, tarea if tarea else "(ninguna)", sede_linea))
    print("")

    print("C) LA SIMULACION, SOBRE COPIA EN MEMORIA Y SIN TOCAR EL DISCO")
    bloque, motivos = bloque_de_confirmacion(glosas, estados, bytes_fuente)
    for m in motivos:
        print("      " + m)
    if motivos:
        print("")
        print("ROJO: el bloque no se puede componer. No se escribe nada.")
        return 1
    print("   bloque compuesto: %d bytes, %d lineas"
          % (len(bloque.encode("utf-8")), bloque.count(NL)))
    nuevo, motivos = anexar_al_r41(sede, bloque)
    for m in motivos:
        print("      " + m)
    if motivos:
        print("")
        print("ROJO: la anexion no sale limpia. No se escribe nada.")
        return 1
    print("   texto simulado: %d bytes (%+d contra el original)"
          % (len(nuevo.encode("utf-8")),
             len(nuevo.encode("utf-8")) - len(sede.encode("utf-8"))))
    print("")

    if a.solo_comprobar:
        print("SOLO COMPROBAR: la simulacion sale limpia y NO se escribe nada.")
        return 0

    print("D) SE ESCRIBE")
    io.open(SEDE, "w", encoding="utf-8", newline=NL).write(nuevo)
    print("   ESCRITO: docs/PENDIENTES.md (%d bytes)" % len(nuevo.encode("utf-8")))
    print("")

    print("E) LA RELECTURA DEL DISCO, QUE ES LA QUE VALE")
    de_nuevo = leer(SEDE)
    corte2, motivo2 = acotar_r41(de_nuevo)
    r41_nuevo = de_nuevo[corte2[0]:corte2[1]] if not motivo2 else ""
    pruebas = [
        ("el bloque de confirmacion esta escrito", MARCA_BLOQUE in de_nuevo),
        ("y esta DENTRO del R.41", MARCA_BLOQUE in r41_nuevo),
        ("el texto de ARRIBA del R.41 no se toco", sede[:ini] == de_nuevo[:ini]),
        ("el R.41 viejo sigue entero dentro del nuevo",
         bloque_r41.rstrip(NL) in r41_nuevo),
        ("es adicion pura: el fichero crecio",
         len(de_nuevo.encode("utf-8")) > len(sede.encode("utf-8"))),
        ("la promesa de arriba sigue nombrando este fichero",
         "vuelta172_tarea1b_confirmar_r41.py" in r41_nuevo),
        ("y ese fichero ya EXISTE y no mide cero",
         os.path.exists(os.path.join(RAIZ, "scripts", "loop",
                                     "vuelta172_tarea1b_confirmar_r41.py"))
         and os.path.getsize(os.path.join(RAIZ, "scripts", "loop",
                                          "vuelta172_tarea1b_confirmar_r41.py")) > 0),
        ("el R.42 de al lado no se toco",
         de_nuevo.count("## R.42.") == sede.count("## R.42.")),
        ("cero guiones largos y cero guiones medios que no estuvieran ya",
         de_nuevo.count(chr(8212)) == sede.count(chr(8212))
         and de_nuevo.count(chr(8211)) == sede.count(chr(8211))),
    ]
    fallan = 0
    for etiqueta, ok in pruebas:
        print("   %-58s %s" % (etiqueta, "SI" if ok else "NO"))
        if not ok:
            fallan += 1
    print("   CIFRA comprobaciones: %d | fallan: %d" % (len(pruebas), fallan))
    print("")
    if fallan:
        print("ROJO: %d comprobacion(es) de la relectura fallan." % fallan)
        return 1
    print("VERDE: el `R.41` queda con su confirmacion medida anexada, y la ruta que")
    print("       llevaba dos vueltas prometiendo prueba sobre un vacio ya no lo hace.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
