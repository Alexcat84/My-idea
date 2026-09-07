# -*- coding: utf-8 -*-
r"""_v207_marcas_anexo.py . LE PONE A MI ESQUELETO LAS CUATRO MARCAS QUE
`scripts/loop/anexar_tarea_al_reporte.py` NECESITA, PARA QUE LAS FILAS DE LAS
TAREAS LAS ESCRIBA EL INSTRUMENTO Y NO YO.

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO, fuera del censo y fuera de la
nomina (moratoria de `AUDITOR.md` 6.3).

POR QUE HACE FALTA, Y VA DECLARADO EN VEZ DE ESCONDERSE: mi esqueleto de la
apertura, `scripts/loop/_v207_esqueleto.py`, nacio SIN las marcas
`<!-- TABLA DE TAREAS -->`, `<!-- FIN TABLA DE TAREAS -->`,
`<!-- ANEXO DE TAREAS -->` y `<!-- FIN ANEXO DE TAREAS -->`, que son las que
`anexar_tarea_al_reporte.py` busca. Sin ellas, la fila de cada tarea habria que
teclearla, y eso es justo lo que `EJECUTOR.md` 1 prohibe. **ES UNA CAIDA MIA DEL
ESQUELETO Y VA A LA SECCION 8 DEL REPORTE.**

POR QUE NO SE RE-TALLA EL ESQUELETO ENTERO: el PASO 0 de
`paso0_archivar_anterior.py` mira el reporte QUE SE VA A PISAR, y a estas alturas
ese reporte ya es el MIO, de la vuelta 207. Volver a lanzar el esqueleto le haria
intentar archivar la vuelta 207, que no ha cerrado. **La marca se anade sobre el
texto que ya hay, por adicion, y el texto viejo queda entero.**

LAS GUARDAS, Y SON LAS QUE PUEDEN CAER:
  (a) cada ancla aparece EXACTAMENTE UNA VEZ;
  (b) al salir, las CUATRO marcas aparecen EXACTAMENTE UNA VEZ cada una;
  (c) las dos filas `| **TAREA N** |` siguen ahi, byte a byte, y siguen diciendo
      `ABIERTA, SIN CERRAR`;
  (d) segunda corrida idempotente.
"""
import argparse
import io
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
NL = chr(10)
REPORTE = os.path.join(RAIZ, "docs", "loop", "REPORTE.md")

ABRE_TABLA = "<!-- TABLA DE TAREAS -->"
FIN_TABLA = "<!-- FIN TABLA DE TAREAS -->"
ABRE_ANEXO = "<!-- ANEXO DE TAREAS -->"
FIN_ANEXO = "<!-- FIN ANEXO DE TAREAS -->"
VACIO = "*(vacio: ninguna tarea ha cerrado todavia)*"

CAB_TABLA = "| tarea | que es | estado | lo que dejo sellado |"
CAB_SEC2 = "## 2. LO QUE CADA TAREA DEJO SELLADO (cada tarea ANEXA su fila al cerrarse)"
VEREDICTO = "**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.**"

SEC2_NUEVA = NL.join([
    "## 2. LAS TAREAS, UNA POR UNA (cada seccion se ANEXA al cerrarse su tarea)",
    "",
    ABRE_ANEXO,
    VACIO,
    FIN_ANEXO,
])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--escribir", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA 207: LAS CUATRO MARCAS DEL ANEXO, PUESTAS SOBRE MI PROPIO ESQUELETO")
    w("=" * 78)
    w("")
    texto = io.open(REPORTE, encoding="utf-8").read().replace(chr(13) + NL, NL)
    w("A) EL SUJETO AL ENTRAR")
    w("   docs/loop/REPORTE.md: %d bytes, %d lineas"
      % (len(texto.encode("utf-8")), len(texto.split(NL))))
    ya = all(m in texto for m in (ABRE_TABLA, FIN_TABLA, ABRE_ANEXO, FIN_ANEXO))
    w("   las cuatro marcas YA ESTAN: %s" % ("SI" if ya else "NO"))
    w("")

    filas0 = [l for l in texto.split(NL) if l.startswith("| **TAREA ")]
    w("B) LAS FILAS DE TAREA AL ENTRAR: %d" % len(filas0))
    for l in filas0:
        w("   %s" % l[:96])
    w("   CIFRA filas que dicen ABIERTA, SIN CERRAR: %d"
      % sum(1 for l in filas0 if "ABIERTA, SIN CERRAR" in l))
    w("")

    if ya:
        w("C) NO SE ESCRIBE: las marcas ya estaban. IDEMPOTENTE.")
        salida = NL.join(L) + NL
        print(salida)
        return 0

    w("C) LAS ANCLAS, CADA UNA COMPROBADA")
    rojos = []
    for nombre, ancla in (("cabecera de la tabla", CAB_TABLA),
                          ("cabecera de la seccion 2", CAB_SEC2),
                          ("veredicto sin escribir", VEREDICTO)):
        n = texto.count(ancla)
        w("   %-28s aparece %d vez(ces)" % (nombre, n))
        if n != 1:
            rojos.append("%s aparece %d veces" % (nombre, n))
    if rojos:
        for r in rojos:
            w("   ROJO: " + r)
        w("   NO SE ESCRIBE NADA.")
        print(NL.join(L) + NL)
        return 1
    w("")

    nuevo = texto.replace(CAB_TABLA, ABRE_TABLA + NL + CAB_TABLA, 1)
    # EL FIN DE LA TABLA VA JUSTO DESPUES DE LA ULTIMA FILA DE TAREA.
    lineas = nuevo.split(NL)
    idx = [i for i, l in enumerate(lineas) if l.startswith("| **TAREA ")]
    lineas = lineas[:idx[-1] + 1] + [FIN_TABLA] + lineas[idx[-1] + 1:]
    nuevo = NL.join(lineas)
    # LA SECCION 2 ENTERA SE SUSTITUYE POR EL BLOQUE DE ANEXO. Lo que se quita es
    # la tabla VACIA que el esqueleto dejo de sitio, y su contenido va DENTRO del
    # cuerpo de cada tarea, con sus dos convenciones en el mismo renglon.
    i2 = nuevo.index(CAB_SEC2)
    i3 = nuevo.index(VEREDICTO)
    quitado = nuevo[i2:i3]
    w("D) LO QUE SE SUSTITUYE, DICHO ENTERO Y NO ESCONDIDO")
    for l in quitado.rstrip(NL).split(NL):
        w("   quitado> %s" % l)
    w("   NINGUNA DE ESAS LINEAS LLEVA UNA CIFRA: es la tabla de sitio que el")
    w("   esqueleto dejo vacia, y su contenido pasa al cuerpo de cada tarea.")
    nuevo = nuevo[:i2] + SEC2_NUEVA + NL + NL + nuevo[i3:]
    w("")

    w("E) LAS GUARDAS AL SALIR")
    fallos = 0
    for m in (ABRE_TABLA, FIN_TABLA, ABRE_ANEXO, FIN_ANEXO, VACIO):
        n = nuevo.count(m)
        w("   marca %-34s aparece %d vez(ces)" % (m[:34], n))
        if n != 1:
            fallos += 1
    filas1 = [l for l in nuevo.split(NL) if l.startswith("| **TAREA ")]
    w("   CIFRA filas de tarea al salir: %d (al entrar %d)"
      % (len(filas1), len(filas0)))
    if filas1 != filas0:
        w("   ROJO: las filas de tarea NO estan byte a byte.")
        fallos += 1
    else:
        w("   las filas de tarea estan BYTE A BYTE como estaban")
    w("   CIFRA guiones largos: %d | guiones medios: %d"
      % (nuevo.count(chr(8212)), nuevo.count(chr(8211))))
    if chr(8212) in nuevo or chr(8211) in nuevo:
        fallos += 1
    w("   CIFRA fallos: %d" % fallos)
    if fallos:
        w("   ROJO. NO SE ESCRIBE NADA.")
        print(NL.join(L) + NL)
        return 1
    w("")

    if a.escribir:
        io.open(REPORTE, "w", encoding="utf-8", newline=NL).write(nuevo)
        w("F) ESCRITO docs/loop/REPORTE.md: %d bytes, %d lineas"
          % (len(nuevo.encode("utf-8")), len(nuevo.split(NL))))
    else:
        w("F) MODO MEDICION: no se escribe nada.")
    w("")
    w("FIN")
    salida = NL.join(L) + NL
    print(salida)
    io.open(os.path.join(RAIZ, "docs", "loop", "SALIDA_V207_MARCAS_ANEXO.txt"),
            "w", encoding="utf-8", newline=NL).write(salida)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
