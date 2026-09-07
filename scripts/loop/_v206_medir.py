# -*- coding: utf-8 -*-
"""Computo de la vuelta 206. Mide bytes de disco, bytes LF, lineas y sha256 LF."""
import hashlib
import os
import sys


def medir(ruta):
    if not os.path.exists(ruta):
        return None
    crudo = open(ruta, "rb").read()
    lf = crudo.replace(b"\r\n", b"\n")
    return {
        "ruta": ruta,
        "bytes_disco": len(crudo),
        "bytes_lf": len(lf),
        "lineas": lf.count(b"\n") + (0 if (not lf or lf.endswith(b"\n")) else 1),
        "sha256_lf": hashlib.sha256(lf).hexdigest()[:16],
    }


if __name__ == "__main__":
    for ruta in sys.argv[1:]:
        m = medir(ruta)
        if m is None:
            print("%s | NO EXISTE" % ruta)
        else:
            print("%s | disco %d | LF %d | lineas %d | sha256LF %s"
                  % (m["ruta"], m["bytes_disco"], m["bytes_lf"], m["lineas"], m["sha256_lf"]))
