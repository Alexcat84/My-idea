# -*- coding: utf-8 -*-
r"""_integral_ciclo_gate0.py . EL CICLO ENTERO DE GATE 0 Y LAS TRES SUITES DE LA
AUDITORIA INTEGRAL (9 sep 2026), PASO 2.a y 2.b, SELLADO CON EL PREFIJO
`_integral_` QUE EL FUNDADOR PIDE.

NO ES UN CLON: los ocho comandos y su orden se IMPORTAN de
`_v205_ciclo_gate0.py` (importar no es clonar, acta 206 `6.5`). Lo unico que
cambia es el NOMBRE de las salidas selladas: `SALIDA_integral_<segmento>_<lado>.txt`
en vez de `SALIDA_V<vuelta>_...`, porque la integral no es una vuelta y no debe
sellar sobre las salidas de ninguna. La consola entera se escribe ademas en
`SALIDA_integral_CICLO_GATE0_<lado>_CONSOLA.txt`, y el instrumento CAE en rojo si
esa consola no existe o mide cero bytes (remedio de la 215, acta 214 `3.1`).

LOS OCHO, EN SU ORDEN: run_phase1.py --reaplico-curaduria; etiquetas_de_cara.py
--aplicar; sync_assets_web.py; git diff HEAD --numstat sobre dataset/, web/ y
engine/; conteo de aristas; desfase calibrado; engine/run_all_tests.py (suite
del motor); npx tsc --noEmit y pnpm test (las otras dos suites).

USO:  python scripts/loop/_integral_ciclo_gate0.py APERTURA
      python scripts/loop/_integral_ciclo_gate0.py CIERRE
"""
import io
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import _v205_ciclo_gate0 as C   # noqa: E402

ROTULO = "integral"


def escribir(seg, lado, texto):
    ruta = os.path.join(C.LOOP, "SALIDA_%s_%s_%s.txt" % (ROTULO, seg, lado))
    io.open(ruta, "w", encoding="utf-8", newline=C.NL).write(texto)
    return os.path.getsize(ruta)


C.escribir = escribir


class Tee(object):
    def __init__(self, original, ruta):
        self.original = original
        self.f = io.open(ruta, "w", encoding="utf-8", newline=C.NL)

    def write(self, s):
        self.original.write(s)
        self.f.write(s)

    def flush(self):
        self.original.flush()
        self.f.flush()

    def reconfigure(self, **kw):
        self.original.reconfigure(**kw)


def main():
    lado = (sys.argv[1] if len(sys.argv) > 1 else "").upper()
    if lado not in ("APERTURA", "CIERRE"):
        print("ROJO: el lado tiene que ser APERTURA o CIERRE.")
        return 1
    consola = os.path.join(C.LOOP, "SALIDA_%s_CICLO_GATE0_%s_CONSOLA.txt" % (ROTULO, lado))
    original = sys.stdout
    tee = Tee(original, consola)
    sys.stdout = tee
    try:
        print("CICLO DE GATE 0 DE LA AUDITORIA INTEGRAL, LADO %s, salidas SALIDA_%s_*_%s.txt" % (lado, ROTULO, lado))
        rc = C.main()
    finally:
        sys.stdout = original
        tee.flush()
        tee.f.close()
    if not os.path.exists(consola) or os.path.getsize(consola) == 0:
        print("ROJO: la consola %s no existe o mide cero bytes." % consola)
        return 1
    print("CONSOLA SELLADA: %s (%d bytes)" % (consola, os.path.getsize(consola)))
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
