# -*- coding: utf-8 -*-
r"""vuelta174_sellar_fila_cerrada.py . SELLA LA CELDA DE ESTADO DE UNA FILA DE
TAREA **DESPUES** DE QUE SU PRUEBA EXISTA, Y SE NIEGA A SELLARLA SI NO EXISTE.

POR QUE NACE, Y ES EL REMEDIO EXACTO DE LA CAIDA `4.4`. La fila de la TAREA 5 del
reporte de la vuelta 172 decia **CERRADA** nombrando
`docs/loop/SALIDA_V172_T5_CERRAR_REPORTE.txt`, **que no existia**. La causa no
fue mentir: fue que la ultima tarea de una vuelta **no puede citar la prueba de
su propio cierre**, porque esa prueba se escribe despues de la fila. Quien
escribe la fila antes tiene dos salidas malas (afirmar sobre un vacio, o no
anexar la fila) y una buena, que es esta: **anexar la fila con lo que es cierto
en ese momento y SELLAR la celda cuando la prueba exista, midiendola.**

LA GUARDA, Y ES LA QUE PUEDE CAER (`EJECUTOR.md` 1, LA RUTA QUE PROMETE PRUEBA ES
CIFRA, 5 sep 2026): este instrumento **NO ESCRIBE NADA** si

  (a) alguna de las rutas que se le pasan NO EXISTE, o
  (b) alguna mide CERO BYTES, o
  (c) la fila de esa tarea no aparece exactamente una vez, o
  (d) la fila no tiene sus cuatro celdas, o
  (e) el sellado tocaria alguna otra fila.

Y si sella, **el estado viejo queda ENTERO Y TACHADO** con el nuevo al lado, que
es el carril `9.10`: una correccion que tapa lo que corrige no se puede auditar.

`sellar()` es PURA: recibe el texto y las medidas y devuelve texto. Su caso
positivo por mutacion es `scripts/loop/vuelta174_tarea1b_mutacion_sellar.py`.

USO:
  python scripts/loop/vuelta174_sellar_fila_cerrada.py --tarea 1 \
      --estado "CERRADA" \
      --pruebas docs/loop/SALIDA_V174_T1B_CERRAR_REPORTE_174.txt
"""
import argparse
import io
import os
import re
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REPORTE = os.path.join(RAIZ, "docs", "loop", "REPORTE.md")


def leer(ruta):
    return io.open(ruta, encoding="utf-8").read().replace(chr(13) + NL, NL)


def medir(rutas):
    """LAS RUTAS, MEDIDAS EN EL DISCO. Devuelve `(medidas, motivos)` con
    `medidas` como `[(ruta, bytes)]`. Es lo unico que este fichero lee."""
    medidas, motivos = [], []
    for r in rutas:
        p = os.path.join(RAIZ, r.replace("/", os.sep))
        if not os.path.exists(p):
            motivos.append("la ruta %s NO EXISTE, y una ruta que promete prueba "
                           "sobre un vacio es CAIDA DE CIFRA" % r)
            continue
        tam = os.path.getsize(p)
        if tam == 0:
            motivos.append("la ruta %s existe pero mide CERO BYTES" % r)
            continue
        medidas.append((r, tam))
    return medidas, motivos


def sellar(texto, tarea, estado, medidas):
    """EL SELLADO, SOBRE COPIA EN MEMORIA. Devuelve `(texto_nuevo, motivos)`; si
    hay motivos, el texto vuelve INTACTO. PURA: ni lee ni escribe."""
    motivos = []
    if not medidas:
        motivos.append("no se paso ninguna ruta medida: sin prueba no se sella")
        return texto, motivos
    ancla = "| **TAREA %s** |" % tarea
    filas = [l for l in texto.split(NL) if l.startswith(ancla)]
    if len(filas) != 1:
        motivos.append("la fila %r aparece %d veces y tiene que aparecer UNA"
                       % (ancla, len(filas)))
        return texto, motivos
    vieja = filas[0]
    celdas = vieja.split(" | ")
    if len(celdas) != 4:
        motivos.append("la fila de la tarea %s tiene %d celdas y tiene que tener 4"
                       % (tarea, len(celdas)))
        return texto, motivos
    estado_viejo = celdas[2].strip()
    if estado_viejo.startswith("~~"):
        motivos.append("la celda de estado YA esta sellada: no se sella dos veces")
        return texto, motivos

    prueba = ", ".join("`%s` (**%d bytes**)" % (r, t) for r, t in medidas)
    celda_nueva = ("~~%s~~ **%s**, sellado al cierre por "
                   "`scripts/loop/vuelta174_sellar_fila_cerrada.py` contra %s, "
                   "MEDIDA con `os.path.getsize` antes de nombrarla"
                   % (estado_viejo, estado, prueba))
    nueva = " | ".join([celdas[0], celdas[1], celda_nueva, celdas[3]])
    nuevo = texto.replace(vieja, nueva)

    otras = [k for k in re.findall(r"\| \*\*TAREA (\d+)\*\* \|", texto)
             if k != str(tarea)]
    for k in otras:
        a = "| **TAREA %s** |" % k
        antes = [l for l in texto.split(NL) if l.startswith(a)]
        despues = [l for l in nuevo.split(NL) if l.startswith(a)]
        if antes != despues:
            motivos.append("el sellado toco la fila de la TAREA %s" % k)
    if estado_viejo not in nuevo:
        motivos.append("el estado viejo se perdio, y el 9.10 dice que NO se borra")
    if "~~%s~~" % estado_viejo not in nuevo:
        motivos.append("el estado viejo no quedo tachado")
    if len(nuevo) <= len(texto):
        motivos.append("el sellado no es adicion: el texto no crecio")
    for malo, nombre in ((chr(8212), "largos"), (chr(8211), "medios")):
        if nuevo.count(malo) != texto.count(malo):
            motivos.append("se colaron guiones %s" % nombre)
    if motivos:
        return texto, motivos
    return nuevo, []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tarea", required=True)
    ap.add_argument("--estado", required=True)
    ap.add_argument("--pruebas", required=True, nargs="+")
    ap.add_argument("--solo-comprobar", action="store_true")
    a = ap.parse_args()

    print("=" * 78)
    print("SE SELLA LA CELDA DE ESTADO DE LA TAREA %s, CON SU PRUEBA MEDIDA" % a.tarea)
    print("=" * 78)
    print("")

    print("A) LAS RUTAS QUE SE VAN A NOMBRAR, MEDIDAS ANTES DE NOMBRARLAS")
    print("   (LA RUTA QUE PROMETE PRUEBA ES CIFRA, EJECUTOR.md 1, 5 sep 2026)")
    medidas, motivos = medir(a.pruebas)
    for r, t in medidas:
        print("   %-58s %d bytes" % (r, t))
    for m in motivos:
        print("   " + m)
    if motivos:
        print("")
        print("ROJO: no se sella nada. Una celda no se sella contra un vacio.")
        return 1
    print("   CIFRA rutas medidas y no vacias: %d" % len(medidas))
    print("")

    print("B) LA SIMULACION, SOBRE COPIA EN MEMORIA")
    texto = leer(REPORTE)
    print("   docs/loop/REPORTE.md -> %d bytes" % len(texto.encode("utf-8")))
    nuevo, motivos = sellar(texto, a.tarea, a.estado, medidas)
    for m in motivos:
        print("   " + m)
    if motivos:
        print("")
        print("ROJO: la simulacion no sale limpia y no se escribe nada.")
        return 1
    print("   texto simulado: %d bytes (%+d)"
          % (len(nuevo.encode("utf-8")),
             len(nuevo.encode("utf-8")) - len(texto.encode("utf-8"))))
    print("")

    if a.solo_comprobar:
        print("SOLO COMPROBAR: la simulacion sale limpia y no se escribe nada.")
        return 0

    print("C) SE ESCRIBE Y SE RELEE DEL DISCO")
    io.open(REPORTE, "w", encoding="utf-8", newline=NL).write(nuevo)
    de_nuevo = leer(REPORTE)
    ancla = "| **TAREA %s** |" % a.tarea
    fila = [l for l in de_nuevo.split(NL) if l.startswith(ancla)][0]
    pruebas = [
        ("el estado viejo sigue entero en la fila", "~~" in fila),
        ("y el estado nuevo esta escrito", "**%s**" % a.estado in fila),
        ("la ruta de la prueba esta nombrada",
         all(r in fila for r, _t in medidas)),
        ("y sus bytes medidos van al lado",
         all("**%d bytes**" % t in fila for _r, t in medidas)),
        ("las cuatro piezas del cierre siguen en pie",
         "**EL VEREDICTO DE UNA LINEA:" in de_nuevo
         and "PENDIENTE DE TALLAR AL CIERRE" not in de_nuevo
         and all((NL + "## %d." % k) in de_nuevo for k in range(3, 10))),
        ("cero guiones largos y cero guiones medios",
         chr(8212) not in de_nuevo and chr(8211) not in de_nuevo),
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
    print("VERDE: la celda queda sellada contra una prueba que existe y esta medida.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
