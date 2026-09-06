# -*- coding: utf-8 -*-
r"""_v183b_tallar_tabla_tramos.py . LA TABLA DE LOS TRAMOS DE LA BATERIA,
TALLADA DE SUS PROPIOS FICHEROS DE SALIDA Y NO TECLEADA.

POR QUE EXISTE. `EJECUTOR.md` 1, "LA TABLA SE CUENTA DE SU FICHERO": toda tabla
o cifra del reporte cita el fichero de salida del que sale y se reconstruye
CONTANDO ese fichero antes de publicarla. La caida de la vuelta 76 es el
ejemplar: el reporte publicaba 13 y 12 y su propio fichero, contado, decia 14 y
11. Aqui no hay tallador de cabecera que alcance, porque el tramo mecanico de la
bateria no produce ni marcador ni recomputo, asi que la tabla se talla de los
ficheros.

QUE MIDE, POR FICHERO Y NO POR MEMORIA: bytes de disco, bytes normalizados a LF,
lineas, `sha256` del LF, el exitcode que el propio fichero declara, la duracion
en minutos que el propio fichero declara, la vuelta a la que el fichero se
atribuye en su primera linea y cuantas lineas con `176` le quedan.

CAE EN ROJO ANTES QUE INVENTAR UNA FILA: un tramo sin fichero sale como NO
EXISTE y uno de cero bytes sale como CERO BYTES, y ninguno de los dos se cuenta
como hecho.

USO:
  python scripts/loop/_v183b_tallar_tabla_tramos.py
"""
import hashlib
import io
import os
import re
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)


def medir(ruta):
    datos = io.open(ruta, "rb").read()
    lf = datos.replace(b"\r\n", b"\n")
    texto = lf.decode("utf-8", errors="replace")
    lineas = texto.split(NL)
    def busca(patron, defecto="?"):
        for l in lineas:
            m = re.search(patron, l)
            if m:
                return m.group(1)
        return defecto
    return {
        "bytes_disco": os.path.getsize(ruta),
        "bytes_lf": len(lf),
        "lineas": lf.count(b"\n"),
        "sha": hashlib.sha256(lf).hexdigest()[:16],
        "exit": busca(r"^EXITCODE DEL TRAMO \d+: (\d+)"),
        "min": busca(r"^DURACION DEL TRAMO \(monotona, minutos\): ([\d.]+)"),
        "vuelta": busca(r"^CORRIDA DEL TRAMO \d+ DE \d+, BATERIA DE LA VUELTA (\d+)"),
        "n176": len([l for l in lineas if "176" in l]),
        "nomordio": busca(r"^  NO MORDIO      : (\d+)"),
        "ancla": busca(r"^  ANCLA PERDIDA  : (\d+)"),
        "noreprod": busca(r"^  NO REPRODUCIBLE: (\d+)"),
        "entradas": len([l for l in lineas if "ENTRADA DEL TRAMO: " in l]),
    }


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    import vuelta183_bateria_por_tramos as L   # noqa: E402
    import verificar_mutaciones_viejas as B    # noqa: E402
    tramos = B.reparto_en_tramos(B.VIEJAS, L.TAMANO)
    print("LA TABLA DE LOS TRAMOS, TALLADA DE SUS FICHEROS")
    print("instrumento: scripts/loop/_v183b_tallar_tabla_tramos.py")
    print("nomina: %d entradas | tramos del reparto: %d | tamano: %d"
          % (len(B.VIEJAS), len(tramos), L.TAMANO))
    print("")
    print("| tramo | fichero | bytes disco | bytes LF | lineas | sha256 LF | exit | minutos | se atribuye a | lineas con 176 | entradas |")
    print("|---:|---|---:|---:|---:|---|---:|---:|---:|---:|---:|")
    hechos = 0
    for n in range(1, len(tramos) + 1):
        nombre = L.nombre_tramo(n)
        ruta = os.path.join(LOOP, nombre)
        if not os.path.exists(ruta):
            print("| **%d** | `%s` | **NO EXISTE** | | | | | | | | |" % (n, nombre))
            continue
        m = medir(ruta)
        if m["bytes_disco"] == 0:
            print("| **%d** | `%s` | **CERO BYTES: NO CUENTA** | | | | | | | | |"
                  % (n, nombre))
            continue
        hechos += 1
        print("| **%d** | `%s` | **%d** | %d | %d | `%s` | **%s** | %s | **%s** | %d | %d |"
              % (n, nombre, m["bytes_disco"], m["bytes_lf"], m["lineas"], m["sha"],
                 m["exit"], m["min"], m["vuelta"], m["n176"], m["entradas"]))
    print("")
    print("CIFRA tramos con salida sellada no vacia: %d de %d" % (hechos, len(tramos)))
    print("")
    print("LOS VEREDICTOS DE CADA TRAMO, CONTADOS DE SU PROPIO FICHERO")
    print("| tramo | ancla perdida | no mordio | no reproducible |")
    print("|---:|---:|---:|---:|")
    for n in range(1, len(tramos) + 1):
        ruta = os.path.join(LOOP, L.nombre_tramo(n))
        if not os.path.exists(ruta) or os.path.getsize(ruta) == 0:
            continue
        m = medir(ruta)
        print("| **%d** | %s | **%s** | %s |"
              % (n, m["ancla"], m["nomordio"], m["noreprod"]))
    print("")
    print("LOS LANZADORES, MEDIDOS IGUAL")
    print("| tramo | fichero | bytes disco | lineas | lineas con 176 |")
    print("|---:|---|---:|---:|---:|")
    for n in range(1, len(tramos) + 1):
        nombre = L.nombre_transcripcion(n)
        ruta = os.path.join(LOOP, nombre)
        if not os.path.exists(ruta):
            continue
        m = medir(ruta)
        print("| **%d** | `%s` | %d | %d | %d |"
              % (n, nombre, m["bytes_disco"], m["lineas"], m["n176"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
