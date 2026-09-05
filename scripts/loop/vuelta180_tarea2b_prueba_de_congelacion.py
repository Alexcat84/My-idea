# -*- coding: utf-8 -*-
r"""vuelta180_tarea2b_prueba_de_congelacion.py . LA PRUEBA DE QUE EL RESULTADO
DE LOS CUATRO YA NO SE MUEVE, CORRIDA Y NO PROMETIDA.

TAREA 2.b de la vuelta 180. Los cuatro arneses que la lectura de la 179 puso en
`ABRE FICHERO VIVO` se corren **DOS VECES SEGUIDAS** y se comparan sus salidas.
Es la prueba que el encargo pide con estas palabras: *"correrlo dos veces, o
contra dos cortes del fichero vivo, y que de lo mismo"*.

POR QUE HACE FALTA ENMASCARAR, Y SE DICE CUAL ES EL PRECIO. Tres de los cuatro
fabrican un directorio temporal con sufijo aleatorio y lo IMPRIMEN. Comparar en
crudo daria distinto SIEMPRE, y por un motivo que no es el sujeto. Asi que antes
de comparar se enmascara **toda ruta absoluta** con la constante `<RUTA>`.

**EL PRECIO, DECLARADO Y NO ESCONDIDO:** el enmascarado tapa tambien las rutas
del repo que las salidas imprimen, asi que esta comparacion **no verificaria un
cambio que solo afectara a una ruta impresa**. Es debilidad conocida y acotada, y
la contrapartida es que sin enmascarar la prueba no puede existir. Lo que si
verifica, entero y sin tapar, es **toda cifra, todo sha256, todo veredicto y todo
exit code**, que es donde vive el resultado.

Y VA UNA SEGUNDA MEDIDA QUE NO DEPENDE DEL ENMASCARADO: el `sha256` de los
ficheros vivos que cada arnes tenia atribuidos, medido ANTES de la primera
corrida y DESPUES de la segunda. Si alguno se moviera, esta prueba lo diria.

LO QUE ESTA PRUEBA NO ES: no es un caso positivo por mutacion, y no se publica
como tal. Es una MEDICION de estabilidad. Los casos positivos por mutacion de
los cuatro son los suyos propios y siguen donde estaban.

USO:
  python scripts/loop/vuelta180_tarea2b_prueba_de_congelacion.py
"""
import hashlib
import io
import os
import re
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
NL = chr(10)

LOS_CUATRO = [
    ("vuelta157_tarea4b_mutacion_tachado.py", ["docs/plan/LECTURAS_DIRIGIDAS.md"]),
    ("vuelta160_tarea7c_mutacion_guarda_cita.py",
     ["docs/plan/LECTURAS_DIRIGIDAS.md", "docs/INTRA_DOMINIO_VEREDICTOS.jsonl",
      "docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl"]),
    ("vuelta174_tarea1b_mutacion_esqueleto.py", ["docs/loop/REPORTE.md"]),
    ("vuelta150_2d_simular_op_c_05.py", ["dataset/metadata/master_graph.json"]),
]

PATRON_RUTA_WIN = re.compile(r"[A-Za-z]:[\\/][^\s\"'|)]*")
PATRON_RUTA_POSIX = re.compile(r"/(?:tmp|var/folders)/[^\s\"'|)]*")


def enmascarar(texto):
    """TODA RUTA ABSOLUTA, TAPADA. PURA."""
    t = PATRON_RUTA_WIN.sub("<RUTA>", texto)
    return PATRON_RUTA_POSIX.sub("<RUTA>", t)


def sha_de(ruta):
    p = os.path.join(RAIZ, ruta.replace("/", os.sep))
    if not os.path.isfile(p):
        return "(no existe)"
    datos = io.open(p, "rb").read().replace(b"\r\n", b"\n")
    return hashlib.sha256(datos).hexdigest()


def correr(nombre):
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run([sys.executable, os.path.join(AQUI, nombre)],
                       cwd=RAIZ, capture_output=True, env=env)
    salida = (r.stdout.decode("utf-8", errors="replace")
              + r.stderr.decode("utf-8", errors="replace"))
    return r.returncode, salida


def primera_linea_distinta(a, b):
    la, lb = a.split(NL), b.split(NL)
    for i in range(max(len(la), len(lb))):
        x = la[i] if i < len(la) else "(no hay linea)"
        y = lb[i] if i < len(lb) else "(no hay linea)"
        if x != y:
            return i + 1, x[:150], y[:150]
    return None, None, None


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    p = print
    p("=" * 78)
    p("LA PRUEBA DE QUE EL RESULTADO DE LOS CUATRO YA NO SE MUEVE (vuelta 180, 2.b)")
    p("=" * 78)
    p("")

    fallos = []
    vivos = sorted({r for _n, rs in LOS_CUATRO for r in rs})
    antes = dict((r, sha_de(r)) for r in vivos)
    p("A) EL sha256 DE LOS FICHEROS VIVOS ATRIBUIDOS, ANTES DE LA PRIMERA CORRIDA")
    for r in vivos:
        p("   %-45s %s" % (r, antes[r][:32]))
    p("")

    p("B) CADA UNO, CORRIDO DOS VECES, Y SUS DOS SALIDAS COTEJADAS")
    filas = []
    for nombre, _rutas in LOS_CUATRO:
        c1, s1 = correr(nombre)
        c2, s2 = correr(nombre)
        m1, m2 = enmascarar(s1), enmascarar(s2)
        h1 = hashlib.sha256(m1.encode("utf-8")).hexdigest()
        h2 = hashlib.sha256(m2.encode("utf-8")).hexdigest()
        igual = (m1 == m2) and (c1 == c2)
        p("")
        p("   %s" % nombre)
        p("      exit 1a corrida: %d | exit 2a corrida: %d" % (c1, c2))
        p("      bytes de la salida enmascarada: %d y %d"
          % (len(m1.encode("utf-8")), len(m2.encode("utf-8"))))
        p("      sha256 de la salida enmascarada: %s" % h1[:32])
        p("                                       %s" % h2[:32])
        p("      LAS DOS CORRIDAS DAN LO MISMO: %s" % ("SI" if igual else "NO"))
        if not igual:
            num, x, y = primera_linea_distinta(m1, m2)
            p("      primera linea que difiere: %s" % num)
            p("         1a: %s" % x)
            p("         2a: %s" % y)
            fallos.append("%s: sus dos corridas NO dan lo mismo" % nombre)
        filas.append((nombre, c1, c2, h1[:16], h2[:16], igual))
    p("")

    despues = dict((r, sha_de(r)) for r in vivos)
    p("C) EL sha256 DE LOS MISMOS FICHEROS VIVOS, DESPUES DE LAS OCHO CORRIDAS")
    for r in vivos:
        ig = antes[r] == despues[r]
        p("   %-45s %s  identico: %s" % (r, despues[r][:32], "SI" if ig else "NO"))
        if not ig:
            fallos.append("%s se movio durante las corridas" % r)
    p("")

    p("D) LA TABLA, CONTADA DE LO DE ARRIBA")
    p("")
    p("| arnes | exit 1a | exit 2a | sha de la salida 1a | sha de la salida 2a | estable |")
    p("|---|---:|---:|---|---|---|")
    for nombre, c1, c2, h1, h2, ig in filas:
        p("| `%s` | %d | %d | `%s` | `%s` | **%s** |"
          % (nombre, c1, c2, h1, h2, "SI" if ig else "NO"))
    p("")
    p("   CIFRA arneses medidos: %d" % len(filas))
    p("   CIFRA estables: %d" % sum(1 for f in filas if f[5]))
    p("   CIFRA ficheros vivos vigilados: %d" % len(vivos))
    p("   CIFRA de esos que se movieron: %d"
      % sum(1 for r in vivos if antes[r] != despues[r]))
    p("")

    if fallos:
        p("ROJO: %d fallo(s)." % len(fallos))
        for f in fallos:
            p("   " + f)
        p("FIN")
        return 1
    p("VERDE: los %d arneses dan EXACTAMENTE lo mismo en dos corridas seguidas, "
      "con el mismo exit code y el mismo sha256 de salida enmascarada, y los %d "
      "ficheros vivos que tenian atribuidos no se movieron ni un byte."
      % (len(filas), len(vivos)))
    p("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
