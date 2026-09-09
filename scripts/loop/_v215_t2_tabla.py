# -*- coding: utf-8 -*-
r"""_v215_t2_tabla.py . LA TABLA DE LOS ONCE TRAMOS DE LA BATERIA DE LA 215, Y EL
COTEJO CONTRA LOS ONCE DE LA 210, LEIDOS LOS DOS LADOS DE SUS FICHEROS.

COMPUTO DE UNA VUELTA, prefijo de guion bajo (moratoria de AUDITOR.md 6.3).

POR QUE EXISTE, Y NO ES MAQUINARIA NUEVA EN EL SENTIDO DE LA MORATORIA: no
vigila nada, no entra en ninguna nomina y muere con la vuelta. Es la tabla que
EJECUTOR.md 1 manda RECONSTRUIR CONTANDO EL FICHERO antes de publicarla.

LOS DOS LADOS SE LEEN, NINGUNO SE RECUERDA. El lado de HOY sale de los once
ficheros sellados que hay en el arbol; el lado de la 210 sale de git show sobre
el commit que sello cada uno de esos mismos ficheros en aquella vuelta, y ese
commit se LEE de git log con --skip=1 sobre la ruta, no se teclea.

PARA QUE SIRVE EL COTEJO: para saber si los NO MORDIO de hoy son NUEVOS o son
los mismos que aquella corrida ya traia. Un arnes que lleva rojo desde antes y
uno que se acaba de romper NO son la misma noticia, y publicarlos juntos sin
distinguirlos seria publicar una alarma que no se sabe leer.

USO:  python scripts/loop/_v215_t2_tabla.py
"""
import hashlib
import io
import os
import re
import subprocess
import sys

NL = chr(10)
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))
PATRON_FILA = re.compile(r"^  (\S+\.py)\s+exit (-?\d+)\s+(.+?)\s+([\d.]+)s\s*$")
TRAMOS = 11


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def rel(n):
    return "docs/loop/SALIDA_V183_BATERIA_TRAMO_%d.txt" % n


def cifra(texto, etiqueta):
    for l in texto.split(NL):
        if etiqueta in l:
            m = re.search(r"(-?\d+)", l.split(etiqueta, 1)[1])
            if m:
                return int(m.group(1))
    return None


def veredictos(texto):
    """LAS FILAS POR ARNES DE UNA SALIDA DE TRAMO. PURA."""
    fuera = []
    for l in texto.split(NL):
        m = PATRON_FILA.match(l.replace(chr(13), ""))
        if m:
            fuera.append((m.group(1), int(m.group(2)), m.group(3).strip()))
    return fuera


def lado(texto):
    """LO QUE SE PUBLICA DE UN TRAMO, CONTADO DE SU TEXTO. PURA."""
    filas = veredictos(texto)
    clases = {}
    for _, _, clase in filas:
        clases[clase] = clases.get(clase, 0) + 1
    m = re.search(r"EXITCODE DEL TRAMO \d+: (-?\d+)", texto)
    d = re.search(r"DURACION DEL TRAMO \(monotona, minutos\): ([\d.]+)", texto)
    return {
        "filas": len(filas),
        "clases": clases,
        "no_mordio": [n for n, _, c in filas if c == "NO MORDIO"],
        "ancla": [n for n, _, c in filas if c == "ANCLA PERDIDA"],
        "no_repro": [n for n, _, c in filas if c == "NO REPRODUCIBLE"],
        "declarado": [n for n, _, c in filas if c == "CASO DECLARADO"],
        "exitcode": m.group(1) if m else "(no leido)",
        "minutos": d.group(1) if d else "(no leido)",
        "bytes": len(texto.encode("utf-8")),
        "sha": hashlib.sha256(
            texto.replace(chr(13) + NL, NL).encode("utf-8")).hexdigest()[:12],
    }


def main():
    print("LOS ONCE TRAMOS DE HOY, CONTADOS DE SUS FICHEROS SELLADOS")
    hoy, viejo, commits = {}, {}, {}
    for n in range(1, TRAMOS + 1):
        p = os.path.join(RAIZ, rel(n).replace("/", os.sep))
        if not os.path.isfile(p) or os.path.getsize(p) == 0:
            print("ROJO: el tramo %d no tiene salida sellada o mide cero bytes." % n)
            return 1
        hoy[n] = lado(io.open(p, encoding="utf-8").read())
        # EL COMMIT DE LA CORRIDA ANTERIOR DE ESE MISMO FICHERO, LEIDO DE git log
        # CON --skip=1: el ultimo es el mio de esta vuelta, el anterior es el suyo.
        _, log = git(["log", "--skip=1", "-1", "--format=%h|%ad|%s",
                      "--date=short", "--", rel(n)])
        trozos = log.strip().split("|", 2)
        commits[n] = trozos if len(trozos) == 3 else ["(sin commit)", "", ""]
        c, txt = git(["show", "%s:%s" % (commits[n][0], rel(n))])
        viejo[n] = lado(txt) if c == 0 and txt.strip() else None

    print("")
    print("| tramo | entradas | OK | CASO DECLARADO | NO MORDIO | ANCLA PERDIDA | "
          "NO REPRODUCIBLE | exitcode | minutos | bytes | sha256 |")
    print("|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|")
    tot = {"filas": 0, "OK": 0, "CASO DECLARADO": 0, "NO MORDIO": 0,
           "ANCLA PERDIDA": 0, "NO REPRODUCIBLE": 0}
    for n in range(1, TRAMOS + 1):
        h = hoy[n]
        print("| **%d** | %d | %d | %d | %d | %d | %d | %s | %s | %d | `%s` |"
              % (n, h["filas"], h["clases"].get("OK", 0),
                 h["clases"].get("CASO DECLARADO", 0),
                 h["clases"].get("NO MORDIO", 0),
                 h["clases"].get("ANCLA PERDIDA", 0),
                 h["clases"].get("NO REPRODUCIBLE", 0),
                 h["exitcode"], h["minutos"], h["bytes"], h["sha"]))
        tot["filas"] += h["filas"]
        for k in ("OK", "CASO DECLARADO", "NO MORDIO", "ANCLA PERDIDA",
                  "NO REPRODUCIBLE"):
            tot[k] += h["clases"].get(k, 0)
    print("")
    print("CIFRA filas de tramo armadas: %d | CIFRA que deberia haber: %d"
          % (TRAMOS, TRAMOS))
    print("CIFRA entradas corridas sumando los once tramos: %d | CIFRA nomina: 135"
          % tot["filas"])
    for k in ("OK", "CASO DECLARADO", "NO MORDIO", "ANCLA PERDIDA",
              "NO REPRODUCIBLE"):
        print("CIFRA %s en los once: %d" % (k, tot[k]))
    suma = sum(tot[k] for k in ("OK", "CASO DECLARADO", "NO MORDIO",
                                "ANCLA PERDIDA", "NO REPRODUCIBLE"))
    print("CIFRA suma de las cinco clases: %d | CIFRA filas: %d (se exige que "
          "calcen)" % (suma, tot["filas"]))
    print("")

    print("LOS ARNESES QUE CAEN HOY, CON SU NOMBRE Y SU TRAMO")
    caidos_hoy = []
    for n in range(1, TRAMOS + 1):
        for clase in ("NO MORDIO", "ANCLA PERDIDA", "NO REPRODUCIBLE"):
            clave = {"NO MORDIO": "no_mordio", "ANCLA PERDIDA": "ancla",
                     "NO REPRODUCIBLE": "no_repro"}[clase]
            for nombre in hoy[n][clave]:
                caidos_hoy.append((n, clase, nombre))
    print("CIFRA arneses de la nomina que CAEN hoy: %d" % len(caidos_hoy))
    for n, clase, nombre in caidos_hoy:
        print("CAE tramo %d | %s | %s" % (n, clase, nombre))
    print("")

    print("EL COTEJO CONTRA LA CORRIDA ANTERIOR DE CADA FICHERO, LEIDA DE git show")
    nuevos, repetidos, sanados = [], [], []
    for n in range(1, TRAMOS + 1):
        v = viejo[n]
        marca = "(sin corrida anterior legible)"
        if v is not None:
            marca = ("commit %s del %s, asunto (70) %s"
                     % (commits[n][0], commits[n][1], commits[n][2][:70]))
        print("TRAMO %d, corrida anterior: %s" % (n, marca))
        if v is None:
            continue
        h_caen = set(hoy[n]["no_mordio"] + hoy[n]["ancla"] + hoy[n]["no_repro"])
        v_caen = set(v["no_mordio"] + v["ancla"] + v["no_repro"])
        for nombre in sorted(h_caen - v_caen):
            nuevos.append((n, nombre))
        for nombre in sorted(h_caen & v_caen):
            repetidos.append((n, nombre))
        for nombre in sorted(v_caen - h_caen):
            sanados.append((n, nombre))
    print("")
    print("CIFRA arneses que CAEN HOY Y NO CAIAN EN LA CORRIDA ANTERIOR: %d"
          % len(nuevos))
    for n, nombre in nuevos:
        print("NUEVO tramo %d | %s" % (n, nombre))
    print("CIFRA arneses que CAEN HOY Y YA CAIAN: %d" % len(repetidos))
    for n, nombre in repetidos:
        print("REPETIDO tramo %d | %s" % (n, nombre))
    print("CIFRA arneses que CAIAN Y HOY NO CAEN: %d" % len(sanados))
    for n, nombre in sanados:
        print("SANADO tramo %d | %s" % (n, nombre))
    print("")

    fallos = 0
    if suma != tot["filas"]:
        fallos += 1
        print("ROJO: las cinco clases no suman las filas.")
    if tot["filas"] != 135:
        fallos += 1
        print("ROJO: los once tramos no suman las 135 entradas de la nomina.")
    print("CIFRA comprobaciones que fallan: %d" % fallos)
    if fallos:
        return 1
    print("VERDE: los once tramos estan, suman la nomina entera, y los caidos "
          "van con su nombre y con su cotejo contra la corrida anterior.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
