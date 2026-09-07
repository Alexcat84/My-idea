# -*- coding: utf-8 -*-
r"""vuelta197_parear_convenciones.py . LE PONE SU PAREJA A CADA CIFRA DE BYTES DEL
REPORTE, MIDIENDOLA DEL DISCO.

POR QUE EXISTE, Y ES UNA GUARDA AJENA QUE ME CAZO A MI. `cerrar_reporte.py` lleva
desde la vuelta 178 una guarda que exige que **toda cifra de bytes vaya con su
pareja: las DOS convenciones, disco y LF**, porque en esta casa no siempre
coinciden y publicar una sola deja la otra sin decir. Corrido sobre mi reporte,
**cayo con 17 cifras sin pareja**, todas en las secciones de tarea que anexe.

LO QUE ESTE FICHERO NO HACE, Y ES LO QUE IMPORTA: **no mete las lineas en una
cerca para que la guarda no las vea.** Esquivar una guarda tapandole los ojos es
peor que la falta que corrige. Lo que hace es **medir las dos convenciones de cada
fichero citado y escribir las dos**, que es lo que la guarda pide.

COMO LO HACE: para cada cita de la forma ``(N bytes)`` o ``mide N bytes`` cuyo
sujeto se pueda resolver a un fichero que EXISTE, remide el fichero y reescribe la
cita en la forma canonica de la casa, *"disco N bytes y LF M bytes"*. **Si el
fichero no existe o la cifra publicada no calza con el disco, NO se reescribe
nada y se dice**: una cifra que no calza es una caida, no un formato.

USO:
  python scripts/loop/vuelta197_parear_convenciones.py
"""
import hashlib
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
REPORTE = os.path.join(LOOP, "REPORTE.md")
SALIDA = os.path.join(LOOP, "SALIDA_V197_PAREAR_CONVENCIONES.txt")

# LAS CITAS A PAREAR, UNA POR UNA, CON SU SUJETO NOMBRADO. El sujeto va explicito
# para que nadie tenga que adivinar de que fichero habla una cifra suelta.
CITAS = [
    ("docs/loop/SALIDA_V197_T1A_REGISTRO_R59.txt", "(14908 bytes)"),
    ("docs/loop/SALIDA_V197_T1A_RECORRIDO_SIN_ESCRIBIR.txt", "(15019 bytes)"),
    ("docs/loop/SALIDA_V197_T1A_MUTACION_REGISTRADOR.txt", "(4085 bytes)"),
    ("docs/loop/ACTA_AUDITOR.md", "**4595886** bytes"),
    ("docs/loop/SALIDA_V197_T2_MUTACION_ORDEN_DEL_TURNO.txt", "(6491 bytes)"),
    ("docs/loop/SALIDA_V197_T2B_CIERRE_DEL_TURNO_197.txt", "(3480 bytes)"),
    ("docs/loop/SALIDA_V197_T2C_GUARDA_MARCADOR_ACTA_197.txt", "(2364 bytes)"),
    ("docs/loop/SALIDA_MARCADOR_AUDITOR_V197.json", "(102 bytes)"),
    ("docs/loop/SALIDA_V197_T3_CIEGA.txt", "(326299 bytes)"),
    ("docs/loop/SALIDA_V197_T3_DESTAPE.txt", "(250425 bytes)"),
    ("docs/loop/SALIDA_V197_T3_MIS_CLASES.txt", "(43605 bytes)"),
    ("docs/loop/SELLO_APERTURA_AUDITOR_V197.json", "(1657 bytes)"),
]


def dos_convenciones(rel):
    """(bytes_disco, bytes_lf, sha_disco, sha_lf) o None si el fichero no esta."""
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(p):
        return None
    d = io.open(p, "rb").read()
    lf = d.replace(b"\r\n", b"\n")
    return (len(d), len(lf), hashlib.sha256(d).hexdigest(),
            hashlib.sha256(lf).hexdigest())


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA 197: LE PONGO SU PAREJA A CADA CIFRA DE BYTES DEL REPORTE")
    w("=" * 78)
    w("")
    w("LA GUARDA QUE ME CAZO: cerrar_reporte.py, vuelta 178 TAREA 1.e, exige que")
    w("toda cifra de bytes vaya con LAS DOS CONVENCIONES. Corrida sobre mi")
    w("reporte cayo con 17 cifras sin pareja. NO SE METEN EN UNA CERCA PARA QUE")
    w("NO LAS VEA: se les mide la pareja y se escribe.")
    w("")
    texto = io.open(REPORTE, encoding="utf-8").read()
    antes = len(texto.encode("utf-8"))
    cambios = 0
    for rel, cita in CITAS:
        m = dos_convenciones(rel)
        if m is None:
            w("   %-56s NO EXISTE, no se reescribe nada" % rel)
            continue
        publicada = int(re.search(r"(\d+)", cita).group(1))
        if publicada != m[0]:
            w("   %-56s LA CIFRA PUBLICADA (%d) NO CALZA CON EL DISCO (%d): NO se"
              % (rel, publicada, m[0]))
            w("      reescribe. Una cifra que no calza es una caida, no un formato.")
            continue
        if cita not in texto:
            w("   %-56s la cita %r no aparece; no se toca nada" % (rel, cita))
            continue
        nueva = ("(disco %d bytes y LF %d bytes)" % (m[0], m[1])
                 if cita.startswith("(")
                 else "disco **%d** bytes y LF **%d** bytes" % (m[0], m[1]))
        n = texto.count(cita)
        texto = texto.replace(cita, nueva)
        cambios += n
        w("   %-56s %d cita(s) -> disco %d | LF %d" % (rel, n, m[0], m[1]))
    io.open(REPORTE, "w", encoding="utf-8", newline=NL).write(texto)
    w("")
    w("CIFRA citas reescritas: %d" % cambios)
    w("docs/loop/REPORTE.md pasa de %d a %d bytes"
      % (antes, len(texto.encode("utf-8"))))
    w("")
    w("LO QUE QUEDA SIN PAREJA A PROPOSITO, Y SE DICE: las cifras de 329 y 801")
    w("bytes del fichero del turno del auditor SI llevan su pareja en la seccion")
    w("4, que es su sede; en las secciones de tarea aparecen como CITA de esa")
    w("medicion y no como medicion nueva. Si la guarda las sigue viendo, se")
    w("publica su cifra y no se esconde.")
    t = NL.join(L) + NL
    io.open(SALIDA, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    return 0


if __name__ == "__main__":
    sys.exit(main())
