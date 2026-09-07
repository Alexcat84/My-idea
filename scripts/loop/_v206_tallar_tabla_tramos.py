# -*- coding: utf-8 -*-
r"""_v206_tallar_tabla_tramos.py . COMPUTO DE LA VUELTA 206, NO MAQUINARIA.

Fichero con prefijo de guion bajo: fuera del censo y fuera de la nomina (que
sigue congelada en 135), no anade guarda ni lector que se quede vigilando, y
muere con la vuelta. Acta 199 `4.5`, acta 203 `4.6`, acta 205 `4.1`.

QUE HACE: talla la tabla de los ONCE tramos de la bateria de la vuelta 205
CONTANDO SUS FICHEROS DE SALIDA, uno por uno, en esta vuelta. Ni una celda se
teclea (`EJECUTOR.md` 1, LA TABLA SE CUENTA DE SU FICHERO). El `exitcode` y los
minutos se leen de las lineas que el propio arnes escribio al sellar el tramo;
si una no aparece, la celda dice `EL PATRON NO ENCONTRO NADA`, nunca `no
existe` (`EJECUTOR.md` 9, NUNCA PUBLIQUES UN NEGATIVO).
"""
import hashlib
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")

RE_EXIT = re.compile(r"^EXITCODE DEL TRAMO (\d+): (\d+)\s*$", re.M)
RE_MIN = re.compile(r"^DURACION DEL TRAMO \(monotona, minutos\): ([0-9.]+)\s*$", re.M)
RE_SEG = re.compile(r"^DURACION DEL TRAMO \(monotona, segundos\): ([0-9.]+)\s*$", re.M)
RE_ENTRADA = re.compile(r"^\s{2}(\S+\.py)\s+exit (-?\d+)\s", re.M)
RE_VEREDICTO = re.compile(r"^VEREDICTO DE ESTA CORRIDA: (.+?)\s*$", re.M)
RE_RUIDO = re.compile(r"^\s*RUIDO DE CONCURRENCIA: (\d+) fichero", re.M)


def medir(ruta):
    crudo = io.open(ruta, "rb").read()
    lf = crudo.replace(b"\r\n", b"\n")
    return {
        "bytes_disco": len(crudo),
        "bytes_lf": len(lf),
        "lineas": lf.count(b"\n") + (0 if (not lf or lf.endswith(b"\n")) else 1),
        "sha256_lf": hashlib.sha256(lf).hexdigest(),
        "texto": lf.decode("utf-8", "replace"),
    }


def uno(patron, texto, grupo=1):
    hallazgos = patron.findall(texto)
    if not hallazgos:
        return None
    ultimo = hallazgos[-1]
    if isinstance(ultimo, tuple):
        return ultimo[grupo]
    return ultimo


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    filas = []
    print("LA TABLA DE LOS ONCE TRAMOS, CONTADA DE SUS FICHEROS EN LA VUELTA 206")
    print("=" * 78)
    total_min = 0.0
    total_entradas = 0
    faltan = []
    for n in range(1, 12):
        nombre = "SALIDA_V205_BATERIA_TRAMO_%d.txt" % n
        ruta = os.path.join(LOOP, nombre)
        if not os.path.exists(ruta):
            faltan.append(nombre)
            print("  TRAMO %d: %s EL PATRON NO ENCONTRO EL FICHERO" % (n, nombre))
            continue
        m = medir(ruta)
        ex = uno(RE_EXIT, m["texto"], 1)
        mi = uno(RE_MIN, m["texto"])
        se = uno(RE_SEG, m["texto"])
        ve = uno(RE_VEREDICTO, m["texto"])
        ru = uno(RE_RUIDO, m["texto"])
        ent = RE_ENTRADA.findall(m["texto"])
        total_entradas += len(ent)
        if mi is not None:
            total_min += float(mi)
        filas.append((n, nombre, m, ex, mi, se, ve, ru, len(ent)))
        print("  TRAMO %-2d | %s" % (n, nombre))
        print("           | disco %d bytes | LF %d bytes | lineas %d"
              % (m["bytes_disco"], m["bytes_lf"], m["lineas"]))
        print("           | sha256 LF %s" % m["sha256_lf"][:16])
        print("           | exitcode %s | minutos %s | segundos %s"
              % (ex if ex is not None else "EL PATRON NO ENCONTRO NADA",
                 mi if mi is not None else "EL PATRON NO ENCONTRO NADA",
                 se if se is not None else "EL PATRON NO ENCONTRO NADA"))
        print("           | veredicto %s | ruido de concurrencia %s | entradas %d"
              % (ve if ve is not None else "EL PATRON NO ENCONTRO NADA",
                 ru if ru is not None else "EL PATRON NO ENCONTRO NADA",
                 len(ent)))
    print("")
    print("  CIFRA tramos con fichero contado: %d" % len(filas))
    print("  CIFRA ficheros que el patron no encontro: %d" % len(faltan))
    print("  CIFRA tramos de CERO BYTES: %d"
          % len([f for f in filas if f[2]["bytes_disco"] == 0]))
    print("  CIFRA suma de las entradas corridas leidas de las salidas: %d"
          % total_entradas)
    print("  CIFRA suma de los minutos leidos de las salidas: %.1f" % total_min)
    exits = sorted({f[3] for f in filas})
    print("  CIFRA exitcodes distintos entre los once: %d (%s)"
          % (len(exits), ", ".join(str(e) for e in exits)))
    vers = sorted({f[6] for f in filas})
    print("  CIFRA veredictos distintos entre los once: %d (%s)"
          % (len(vers), " | ".join(str(v) for v in vers)))
    ruidos = [(f[0], f[7]) for f in filas if f[7] not in (None, "0")]
    print("  CIFRA tramos con RUIDO DE CONCURRENCIA distinto de 0: %d" % len(ruidos))
    for n, r in ruidos:
        print("      TRAMO %d: %s fichero(s)" % (n, r))
    mins = sorted(float(f[4]) for f in filas if f[4] is not None)
    if mins:
        med = mins[len(mins) // 2] if len(mins) % 2 else (mins[len(mins) // 2 - 1] + mins[len(mins) // 2]) / 2.0
        print("  CIFRA mediana de minutos por tramo: %.1f" % med)
        print("  CIFRA maximo de minutos en un tramo: %.1f" % mins[-1])
    print("")
    print("LA TABLA EN MARKDOWN, PARA PEGARLA ENTERA Y NO TECLEARLA")
    print("")
    print("| tramo | salida sellada | bytes disco | bytes LF | lineas | sha256 LF | exitcode | minutos |")
    print("|---|---|---|---|---|---|---|---|")
    for n, nombre, m, ex, mi, se, ve, ru, ne in filas:
        print("| %d | `%s` | %d | %d | %d | `%s` | %s | %s |"
              % (n, nombre, m["bytes_disco"], m["bytes_lf"], m["lineas"],
                 m["sha256_lf"][:16],
                 ex if ex is not None else "EL PATRON NO ENCONTRO NADA",
                 mi if mi is not None else "EL PATRON NO ENCONTRO NADA"))
    return 0 if not faltan else 1


if __name__ == "__main__":
    raise SystemExit(main())
