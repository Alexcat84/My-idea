# -*- coding: utf-8 -*-
r"""_v205_tallar_tabla_tramos.py . LA TABLA DE LOS TRAMOS DE LA BATERIA DE LA
VUELTA 205, TALLADA CONTANDO SUS FICHEROS DE SALIDA Y NO TECLEADA.

POR QUE EXISTE (`EJECUTOR.md` 1, LA TABLA SE CUENTA DE SU FICHERO, 26 ago 2026):
"TODA TABLA O CIFRA DEL REPORTE CITA EL FICHERO DE SALIDA DEL QUE SALE, Y SE
RECONSTRUYE CONTANDO ESE FICHERO ANTES DE PUBLICARLA. Si no existe fichero que
contar, LA TABLA NO SE PUBLICA."

COMPUTO DE UNA VUELTA, con prefijo de guion bajo: fuera del censo, fuera de la
nomina, no roza la moratoria (acta 199 `4.5`, acta 203 `4.6`). No vigila nada y
muere con la vuelta.

CADA CELDA SALE DEL FICHERO DEL TRAMO. Los bytes de disco y los normalizados a
LF van EN EL MISMO RENGLON, que es la quinta comprobacion de `cerrar_reporte.py`.
UN FICHERO QUE NO EXISTE O QUE MIDE CERO BYTES SE PUBLICA COMO TAL, no se calla:
`EJECUTOR.md` 1, LA RUTA QUE PROMETE PRUEBA ES CIFRA."""
import hashlib
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

P_EXIT = re.compile(r"^EXITCODE DEL TRAMO \d+:\s*(\d+)", re.M)
P_MIN = re.compile(r"^DURACION DEL TRAMO \(monotona, minutos\):\s*([\d.]+)", re.M)
P_INI = re.compile(r"^INICIO \(reloj de pared, UTC\):\s*(\S+)", re.M)
P_FIN = re.compile(r"^FIN \(reloj de pared, UTC\):\s*(\S+)", re.M)
P_ENTRADAS = re.compile(r"^\s+ENTRADA DEL TRAMO:", re.M)
P_VER = re.compile(r"^\s+CLASE DEL VEREDICTO:\s*(.+?)\s*\|", re.M)
P_FALLO = re.compile(r"^\s+CIFRA de FALLO:\s*(.+)$", re.M)
P_ANCLA = re.compile(r"^\s+ANCLA PERDIDA\s*:\s*(\d+)", re.M)
P_MORDIO = re.compile(r"^\s+NO MORDIO\s*:\s*(\d+)", re.M)
P_REPRO = re.compile(r"^\s+NO REPRODUCIBLE:\s*(\d+)", re.M)
P_RUIDO = re.compile(r"^\s+RUIDO DE CONCURRENCIA:\s*(\d+)", re.M)


def uno(patron, texto, defecto="(no se pudo leer)"):
    m = patron.search(texto)
    return m.group(1) if m else defecto


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    total = int(sys.argv[1]) if len(sys.argv) > 1 else 11
    filas, resumen = [], []
    suma_disco = suma_lf = suma_min = 0.0
    entradas = 0
    ausentes = vacios = 0
    for n in range(1, total + 1):
        nombre = "SALIDA_V205_BATERIA_TRAMO_%d.txt" % n
        ruta = os.path.join(LOOP, nombre)
        if not os.path.exists(ruta):
            ausentes += 1
            filas.append("| %d | `%s` | NO EXISTE | NO EXISTE | NO EXISTE | NO EXISTE | NO EXISTE |"
                         % (n, nombre))
            continue
        crudo = io.open(ruta, "rb").read()
        lf = crudo.replace(b"\r\n", b"\n")
        if len(crudo) == 0:
            vacios += 1
        texto = lf.decode("utf-8", errors="replace")
        sha = hashlib.sha256(lf).hexdigest()[:16]
        ex = uno(P_EXIT, texto)
        mi = uno(P_MIN, texto)
        ent = len(P_ENTRADAS.findall(texto))
        entradas += ent
        suma_disco += len(crudo)
        suma_lf += len(lf)
        try:
            suma_min += float(mi)
        except ValueError:
            pass
        filas.append("| %d | `%s` | %d bytes en disco y %d normalizado a LF | `%s` | %d | %s | %s |"
                     % (n, nombre, len(crudo), len(lf), sha, ent, ex, mi))
        resumen.append("| %d | %s | %s | %s | %s | %s | %s |"
                       % (n, uno(P_ANCLA, texto), uno(P_MORDIO, texto),
                          uno(P_REPRO, texto), uno(P_RUIDO, texto),
                          uno(P_VER, texto), uno(P_INI, texto) + " a " + uno(P_FIN, texto)))

    print("LA TABLA DEL SELLADO, CONTADA DE LOS %d FICHEROS Y NO TECLEADA" % total)
    print("")
    print("| tramo | salida sellada | bytes (las dos convenciones) | sha256 LF | entradas | exitcode | minutos |")
    print("|---|---|---|---|---|---|---|")
    for f in filas:
        print(f)
    print("")
    print("LA TABLA DEL VEREDICTO DE CADA TRAMO, CONTADA DE LOS MISMOS FICHEROS")
    print("")
    print("| tramo | ancla perdida | no mordio | no reproducible | ruido de concurrencia | clase del veredicto | reloj de pared UTC |")
    print("|---|---|---|---|---|---|---|")
    for f in resumen:
        print(f)
    print("")
    print("CIFRA tramos con fichero en disco: %d de %d" % (total - ausentes, total))
    print("CIFRA tramos AUSENTES: %d" % ausentes)
    print("CIFRA tramos de CERO BYTES: %d" % vacios)
    print("CIFRA suma de las entradas corridas, sumada de las lineas ENTRADA DEL TRAMO: %d" % entradas)
    print("CIFRA suma de bytes de los tramos: %d en disco y %d normalizado a LF"
          % (int(suma_disco), int(suma_lf)))
    print("CIFRA suma de minutos de los tramos, sumada de sus lineas de duracion: %.1f" % suma_min)
    print("CIFRA suma de horas: %.2f" % (suma_min / 60.0))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
