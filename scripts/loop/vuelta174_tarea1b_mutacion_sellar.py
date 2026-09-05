# -*- coding: utf-8 -*-
r"""vuelta174_tarea1b_mutacion_sellar.py . EL CASO POSITIVO POR MUTACION DE
`sellar()`, LA FUNCION PURA DE `vuelta174_sellar_fila_cerrada.py`.

POR QUE EXISTE. `EJECUTOR.md` 1, clausula del 29 ago 2026. Este instrumento nace
para que una celda de estado no pueda volver a sellarse contra un vacio, que es
la caida `4.4`. Publicarlo sin haber tumbado sus guardas seria repetir la especie
con otro traje.

SUJETO CONGELADO: las tablas de mentira son cadenas literales de este proceso.
**CERO LECTURAS DE DISCO Y CERO ESCRITURAS**, salvo el bloque final, que prueba
`medir()` contra ficheros que crea y borra en un temporal.

USO:
  python scripts/loop/vuelta174_tarea1b_mutacion_sellar.py
"""
import io
import os
import shutil
import sys
import tempfile

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))

import vuelta174_sellar_fila_cerrada as S  # noqa: E402

MED = [("docs/loop/SALIDA_V174_T1B_CERRAR_REPORTE_174.txt", 1234)]

FILA1 = ("| **TAREA 1** | lo que sea | **CERRADA EN SU 1.a; EL CIERRE PENDIENTE** "
         "| `X`, `Y` |")
FILA2 = "| **TAREA 2** | lo que sea | **CERRADA** | `Z` |"


def tabla(f1=FILA1, f2=FILA2, cabeza="", cola=""):
    return (cabeza +
            "<!-- TABLA DE TAREAS -->" + NL +
            "| tarea | que encarga | estado | donde vive la prueba |" + NL +
            "|---|---|---|---|" + NL + f1 + NL + f2 + NL +
            "<!-- FIN TABLA DE TAREAS -->" + NL + cola)


def correr():
    print("=" * 78)
    print("CASO POSITIVO POR MUTACION DE sellar(), VUELTA 174")
    print("=" * 78)
    print("")
    verdes = 0
    rojos = 0

    def marcar(etiqueta, ok, detalle=""):
        nonlocal verdes, rojos
        print("   %-62s %s" % (etiqueta, "SI" if ok else "NO"))
        if detalle:
            print("      -> " + detalle[:100])
        if ok:
            verdes += 1
        else:
            rojos += 1

    print("-" * 78)
    print("(A) LOS ROJOS DE sellar(), Y EL TEXTO VUELVE INTACTO")
    print("-" * 78)
    casos = [
        ("sin ninguna ruta medida", tabla(), "1", [], "sin prueba no se sella"),
        ("si la fila de la tarea no esta", tabla(), "9", MED, "aparece 0 veces"),
        ("si la fila esta DOS veces", tabla(cola=FILA1 + NL), "1", MED,
         "aparece 2 veces"),
        ("si la fila no tiene cuatro celdas",
         tabla(f1="| **TAREA 1** | solo tres | **CERRADA** |"), "1", MED,
         "celdas y tiene que tener 4"),
        ("si la celda YA estaba sellada",
         tabla(f1="| **TAREA 1** | lo que sea | ~~**CERRADA**~~ ya sellada | `X` |"),
         "1", MED, "YA esta sellada"),
    ]
    for etiqueta, texto, tarea, med, esperado in casos:
        nuevo, motivos = S.sellar(texto, tarea, "CERRADA", med)
        ok = (bool(motivos) and any(esperado in m for m in motivos)
              and nuevo == texto)
        marcar("cae %s" % etiqueta, ok, motivos[0] if motivos else "(sin motivo)")
    print("")

    print("-" * 78)
    print("(B) EL CASO VERDE")
    print("-" * 78)
    base = tabla()
    nuevo, motivos = S.sellar(base, "1", "CERRADA", MED)
    comprobaciones = [
        ("no devuelve ningun motivo", not motivos),
        ("el estado viejo sigue ENTERO",
         "**CERRADA EN SU 1.a; EL CIERRE PENDIENTE**" in nuevo),
        ("y esta TACHADO",
         "~~**CERRADA EN SU 1.a; EL CIERRE PENDIENTE**~~" in nuevo),
        ("el estado nuevo esta al lado", "**CERRADA**" in nuevo),
        ("la ruta de la prueba esta nombrada", MED[0][0] in nuevo),
        ("y sus bytes MEDIDOS van al lado", "**1234 bytes**" in nuevo),
        ("la fila de la TAREA 2 no se toco",
         FILA2 in nuevo and nuevo.count(FILA2) == 1),
        ("solo se tacha UNA celda", nuevo.count("~~") == 2),
        ("es adicion: el texto crecio", len(nuevo) > len(base)),
        ("la fila sigue teniendo cuatro celdas",
         len([l for l in nuevo.split(NL)
              if l.startswith("| **TAREA 1** |")][0].split(" | ")) == 4),
    ]
    for etiqueta, ok in comprobaciones:
        marcar(etiqueta, ok)
    print("")

    print("-" * 78)
    print("(C) LOS BYTES NO SON UNA CONSTANTE: OTRA MEDIDA DA OTRO TEXTO")
    print("-" * 78)
    otro, _m = S.sellar(base, "1", "CERRADA", [("docs/loop/OTRA.txt", 99)])
    marcar("con otra medida escribe otros bytes", "**99 bytes**" in otro)
    marcar("y NO escribe los de la otra corrida", "**1234 bytes**" not in otro)
    marcar("y nombra la otra ruta", "docs/loop/OTRA.txt" in otro)
    print("")

    print("-" * 78)
    print("(D) medir(), CONTRA FICHEROS DE VERDAD EN UN TEMPORAL")
    print("-" * 78)
    tmp = tempfile.mkdtemp(prefix="v174_sellar_")
    try:
        rel_dir = os.path.relpath(tmp, RAIZ).replace(os.sep, "/")
        lleno = os.path.join(tmp, "lleno.txt")
        vacio = os.path.join(tmp, "vacio.txt")
        # `newline=NL` NO ES ADORNO. La primera version de este arnes escribia
        # sin el, y en Windows el modo texto traduce el salto de linea a CRLF:
        # el fichero medía 6 bytes y este caso esperaba 5. EL ARNES SE CAYO Y
        # TENIA RAZON `medir()`, no la expectativa. Se fija el salto para que la
        # cifra esperada sea la misma en cualquier maquina.
        io.open(lleno, "w", encoding="utf-8", newline=NL).write("hola" + NL)
        io.open(vacio, "w", encoding="utf-8", newline=NL).write("")
        m, mot = S.medir([rel_dir + "/lleno.txt"])
        marcar("mide un fichero que existe y no esta vacio (5 bytes exactos)",
               not mot and len(m) == 1 and m[0][1] == 5, str(m))
        m, mot = S.medir([rel_dir + "/vacio.txt"])
        marcar("CAE si el fichero mide CERO BYTES",
               bool(mot) and "CERO BYTES" in mot[0], mot[0] if mot else "")
        m, mot = S.medir([rel_dir + "/no_existe.txt"])
        marcar("CAE si el fichero NO EXISTE",
               bool(mot) and "NO EXISTE" in mot[0], mot[0] if mot else "")
        m, mot = S.medir([rel_dir + "/lleno.txt", rel_dir + "/no_existe.txt"])
        marcar("y CAE aunque solo UNA de varias falte", bool(mot))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
        print("   temporal borrado: existe -> %s"
              % ("SI" if os.path.exists(tmp) else "NO"))
    print("")

    total = verdes + rojos
    print("=" * 78)
    print("CIFRA casos: %d | verdes: %d | rojos: %d" % (total, verdes, rojos))
    print("=" * 78)
    if rojos:
        print("ROJO: %d comprobacion(es) no se comportan." % rojos)
        return 1
    print("VERDE: las %d comprobaciones se comportan. Una celda no se puede sellar"
          % total)
    print("       contra un fichero inexistente ni contra uno de cero bytes.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(correr())
