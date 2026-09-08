# -*- coding: utf-8 -*-
r"""_v210_rutas.py . EL BARRIDO DE LAS RUTAS QUE EL REPORTE DE LA VUELTA 210
PUBLICA, UNA A UNA, CONTRA EL DISCO.

COMPUTO DE UNA VUELTA, prefijo de guion bajo, fuera del censo y fuera de la
nomina (moratoria `AUDITOR.md` 6.3).

LA LETRA QUE OBEDECE (`EJECUTOR.md` 1, LA RUTA QUE PROMETE PRUEBA ES CIFRA):
*"una ruta publicada como evidencia cuenta como CIFRA PUBLICADA en su sede, y si
apunta a un fichero inexistente o de CERO BYTES es CAIDA DE CIFRA"*.

LA UNICA EXENCION VA NOMBRADA, NO ENSANCHANDO EL PATRON. `docs/loop/reportes/
REPORTE_V210.md` aparece en la `C.3` de la seccion 8 **como el fichero que esta
vuelta RETIRO**, no como evidencia de nada: la frase que lo nombra dice que se
retiro con `git rm` y por que. **Una ruta que se nombra para decir que NO debe
existir no promete ninguna prueba**, y por eso se exime NOMBRANDOLA aqui, con su
motivo escrito, que es como esta casa exime y no ensanchando el patron hasta que
trague. Se sigue midiendo y se sigue imprimiendo: lo unico que cambia es que no
cuenta como fallo.

USO:  python scripts/loop/_v210_rutas.py
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NL = chr(10)
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))

PATRON_RUTA = re.compile(r"`((?:docs|scripts|dataset|engine|web|paradas)/"
                         r"[A-Za-z0-9_./-]+)`")
PATRON_SUELTO = re.compile(r"`(SALIDA_V\d+_[A-Za-z0-9_.]+\.txt)`")

EXIMIDAS = {
    "docs/loop/reportes/REPORTE_V%d.md" % VUELTA:
        "la nombra la C.3 de la seccion 8 como el fichero que esta vuelta "
        "RETIRO con git rm, no como evidencia. El archivo de una vuelta lo "
        "escribe la vuelta SIGUIENTE, asi que su ausencia es lo correcto.",
}


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ruta_rep = os.path.join(RAIZ, "docs", "loop", "REPORTE.md")
    t = io.open(ruta_rep, encoding="utf-8").read().replace(chr(13) + NL, NL)
    todas = sorted(set(PATRON_RUTA.findall(t))
                   | set("docs/loop/" + x for x in PATRON_SUELTO.findall(t)))
    out = []
    w = out.append
    w("EL BARRIDO DE LAS RUTAS QUE EL REPORTE DE LA VUELTA %d PUBLICA." % VUELTA)
    w("LA RUTA QUE PROMETE PRUEBA ES CIFRA (EJECUTOR.md 1).")
    w("")
    w("CIFRA rutas distintas halladas en docs/loop/REPORTE.md: %d" % len(todas))
    w("CIFRA rutas EXIMIDAS, nombradas una a una y no por patron: %d" % len(EXIMIDAS))
    for r, motivo in sorted(EXIMIDAS.items()):
        w("  EXIMIDA: %s" % r)
        w("     motivo: %s" % motivo)
    w("")
    fallan = []
    for r in todas:
        p = os.path.join(RAIZ, r.replace("/", os.sep))
        if not os.path.exists(p):
            estado = "NO EXISTE (ausencia, no cero)"
            if r not in EXIMIDAS:
                fallan.append((r, estado))
        elif os.path.getsize(p) == 0:
            estado = "CERO BYTES (fichero vacio, no ausencia)"
            if r not in EXIMIDAS:
                fallan.append((r, estado))
        else:
            estado = "%d bytes en disco" % os.path.getsize(p)
        w("  %-58s %s%s" % (r, estado, "   [EXIMIDA]" if r in EXIMIDAS else ""))
    w("")
    w("CIFRA rutas que FALLAN (no existen o miden cero, sin contar las eximidas): %d"
      % len(fallan))
    for r, e in fallan:
        w("  FALLA: %s -> %s" % (r, e))
    if not fallan:
        w("  (ninguna, y el cero va escrito)")
    texto = NL.join(out) + NL
    destino = os.path.join(RAIZ, "docs", "loop", "SALIDA_V%d_RUTAS.txt" % VUELTA)
    io.open(destino, "w", encoding="utf-8", newline=NL).write(texto)
    sys.stdout.write(texto)
    return 1 if fallan else 0


if __name__ == "__main__":
    sys.exit(main())
