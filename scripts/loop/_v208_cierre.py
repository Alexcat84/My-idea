# -*- coding: utf-8 -*-
r"""_v208_cierre.py . LOS DOS SELLOS DE IDENTIDAD Y LAS MEDICIONES DE CIERRE DE LA
VUELTA 208, RECOMPUTADAS AL CIERRE Y NO HEREDADAS DE LA APERTURA.

COMPUTO DE UNA VUELTA, prefijo de guion bajo, fuera del censo y fuera de la
nomina (moratoria `AUDITOR.md` 6.3).

EL ESTADO AL CIERRE SE MIDE AL CIERRE (`EJECUTOR.md` 1): toda cifra que describa
el estado al cerrar la vuelta se RECOMPUTA aqui, porque la propia vuelta la pudo
mover.

LOS DOS SELLOS DE IDENTIDAD, Y EL DE APERTURA VA DECLARADO Y NO DISIMULADO:

  . `SALIDA_V208_HEAD_APERTURA.txt` lleva el HEAD de apertura, y **NO SE TECLEA**:
    lo LEE de `docs/loop/SALIDA_V208_APERTURA.txt`, que es el sello que escribi
    ANTES DE LA PRIMERA OPERACION y que quedo committeado. **El VALOR es de
    apertura de verdad; EL FICHERO CON ESE NOMBRE nace ahora**, y eso es una caida
    mia de la misma especie que la `C.2` del reporte de la 207. Va a mi seccion 8
    y no la escondo. El tallador lo va a decir por su cuenta con
    `git log --diff-filter=A`, y hace bien.
  . `SALIDA_V208_HEAD_CIERRE.txt` lleva el HEAD tras la ultima operacion de tarea,
    leido de `git rev-parse HEAD`.
"""
import argparse
import hashlib
import io
import os
import re
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
VUELTA = 208

SEDES_SELLADAS = [
    ("docs/INTRA_DOMINIO_VEREDICTOS.jsonl", 4054129, "0a77b5a35a962621"),
    ("docs/plan/OPERACIONES.jsonl", 513043, "829c583eb779cab6"),
]
SEDES_AUDITOR = ["docs/loop/ACTA_AUDITOR.md", "docs/loop/PROMPT_SIGUIENTE.md",
                 "PARA_ALEXIS.md"]
CARPETAS = ["dataset/", "web/", "engine/", "docs/plan/"]
BATERIA = "docs/loop/SALIDA_V%d_BATERIA.txt" % VUELTA


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def dos_convenciones(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(p):
        return None
    d = io.open(p, "rb").read()
    lf = d.replace(b"\r\n", b"\n")
    return (len(d), len(lf), hashlib.sha256(d).hexdigest()[:16],
            hashlib.sha256(lf).hexdigest()[:16])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", default="CIERRE")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA %d, CIERRE: LOS DOS SELLOS Y LAS MEDICIONES, RECOMPUTADAS AL"
      % VUELTA)
    w("CIERRE Y NO HEREDADAS")
    w("=" * 78)
    w("")

    w("A) EL SELLO DE APERTURA. EL VALOR NO SE TECLEA: SE LEE DE MI PROPIO SELLO")
    ruta_ap = os.path.join(LOOP, "SALIDA_V%d_APERTURA.txt" % VUELTA)
    texto_ap = io.open(ruta_ap, encoding="utf-8").read()
    m = re.search(r"CIFRA HEAD de apertura: ([0-9a-f]{40})", texto_ap)
    if not m:
        w("   ROJO: no se pudo leer el HEAD de apertura de mi propio sello.")
        print(NL.join(L))
        return 1
    head_ap = m.group(1)
    w("   leido de docs/loop/SALIDA_V%d_APERTURA.txt: %s" % (VUELTA, head_ap))
    c, o = git(["log", "-1", "--format=%H", "--", "docs/loop/SALIDA_V%d_APERTURA.txt" % VUELTA])
    w("   ese sello quedo committeado en: %s" % o.strip()[:40])
    io.open(os.path.join(LOOP, "SALIDA_V%d_HEAD_APERTURA.txt" % VUELTA),
            "w", encoding="utf-8", newline=NL).write(head_ap + NL)
    w("   ESCRITO docs/loop/SALIDA_V%d_HEAD_APERTURA.txt" % VUELTA)
    w("   Y LO DECLARO EN VEZ DE DISIMULARLO: el VALOR es de apertura de verdad,")
    w("   pero EL FICHERO CON ESE NOMBRE nace ahora. Es la especie de la C.2 de")
    w("   la 207 y va a mi seccion 8.")
    w("")

    w("B) EL SELLO DE CIERRE, LEIDO DE git rev-parse HEAD")
    c, o = git(["rev-parse", "HEAD"])
    head_ci = o.strip()
    w("   HEAD tras la ultima operacion de tarea: %s" % head_ci)
    c, o2 = git(["log", "-1", "--format=%s"])
    w("   asunto de ese commit (primeros 110): %s" % o2.strip()[:110])
    io.open(os.path.join(LOOP, "SALIDA_V%d_HEAD_CIERRE.txt" % VUELTA),
            "w", encoding="utf-8", newline=NL).write(head_ci + NL)
    w("   ESCRITO docs/loop/SALIDA_V%d_HEAD_CIERRE.txt" % VUELTA)
    w("")

    w("C) NUMSTAT AL CIERRE, RECOMPUTADO CONTRA EL HEAD DE APERTURA Y NO HEREDADO")
    w("   comando: git diff %s --numstat -- <sede>" % head_ap[:8])
    total = 0
    for sede in CARPETAS:
        c, o = git(["diff", head_ap, "--numstat", "--", sede])
        filas = [l for l in o.split(NL) if l.strip()]
        w("   CIFRA filas de %-14s : %d" % (sede, len(filas)))
        for l in filas:
            w("      %s" % l)
        total += len(filas)
    w("   CIFRA total de filas en las cuatro sedes: %d" % total)
    w("")
    w("   Y EL numstat CONTRA HEAD (arbol de trabajo contra el ultimo commit),")
    w("   que es lo que el encargo pide en CERO filas:")
    total_head = 0
    for sede in CARPETAS:
        c, o = git(["diff", "HEAD", "--numstat", "--", sede])
        filas = [l for l in o.split(NL) if l.strip()]
        w("   CIFRA filas de git diff HEAD --numstat -- %-14s : %d"
          % (sede, len(filas)))
        for l in filas:
            w("      %s" % l)
        total_head += len(filas)
    w("   CIFRA total: %d" % total_head)
    w("")

    w("D) LAS SEDES SELLADAS, REMEDIDAS AL CIERRE POR LAS DOS CONVENCIONES")
    malas = 0
    for rel, bytes_c, sha_c in SEDES_SELLADAS:
        d = dos_convenciones(rel)
        if d is None:
            w("   %s: NO EXISTE" % rel)
            malas += 1
            continue
        calza = (d[0] == bytes_c and d[1] == bytes_c and d[2] == sha_c and d[3] == sha_c)
        w("   %s: %d bytes en disco y %d normalizado a LF, sha256 disco %s y"
          % (rel, d[0], d[1], d[2]))
        w("      sha256 LF %s | contraste %d y %s | CALZA POR LAS DOS: %s"
          % (d[3], bytes_c, sha_c, "SI" if calza else "NO"))
        if not calza:
            malas += 1
    w("   CIFRA sedes selladas que NO calzan: %d" % malas)
    w("   NI UN VEREDICTO NI UN `estado` SE MOVIERON: %s"
      % ("CONFIRMADO" if malas == 0 else "ROJO"))
    w("")

    w("E) LAS TRES SEDES DEL AUDITOR, CON EL CERO DISTINGUIDO")
    for rel in SEDES_AUDITOR:
        p = os.path.join(RAIZ, rel.replace("/", os.sep))
        if not os.path.isfile(p):
            w("   CIFRA %s: 0 filas POR AUSENCIA DE FICHERO (no existe en disco)"
              % rel)
            continue
        c, o = git(["diff", head_ap, "--numstat", "--", rel])
        filas = [l for l in o.split(NL) if l.strip()]
        w("   CIFRA %s: %d filas de git diff contra el HEAD de apertura,"
          % (rel, len(filas)))
        w("      FICHERO PRESENTE (%d bytes en disco)" % os.path.getsize(p))
    w("")

    w("F) EL HUECO DE BATERIA, CON SUS TRES PIEZAS")
    p = os.path.join(RAIZ, BATERIA.replace("/", os.sep))
    existe = os.path.isfile(p)
    w("   NOMBRE DEL FICHERO: %s" % BATERIA)
    if not existe:
        w("   BYTES MEDIDOS EN ESTA CORRIDA: 0 bytes, Y ES UN CERO DE AUSENCIA")
        w("      DE FICHERO, NO DE FICHERO VACIO: os.path.isfile devuelve False.")
    else:
        w("   BYTES MEDIDOS EN ESTA CORRIDA: %d bytes, y el fichero SI EXISTE"
          % os.path.getsize(p))
    w("   ATRIBUCION: NADIE la corrio en esta vuelta, ni el ejecutor ni el")
    w("      auditor, y no es una omision sino la cadencia de AUDITOR.md 6.1:")
    w("      la ultima fue la 205 y la siguiente es la 210.")
    ult = os.path.join(LOOP, "SALIDA_V205_BATERIA.txt")
    w("   LA ULTIMA BATERIA DE VERDAD: docs/loop/SALIDA_V205_BATERIA.txt, %s"
      % ("%d bytes en disco" % os.path.getsize(ult) if os.path.isfile(ult)
         else "que tampoco existe en disco"))
    w("")

    w("G) EL REPORTE, MEDIDO ANTES DE CERRARLO")
    d = dos_convenciones("docs/loop/REPORTE.md")
    w("   docs/loop/REPORTE.md: %d bytes en disco y %d normalizado a LF,"
      % (d[0], d[1]))
    w("   sha256 disco %s y sha256 LF %s" % (d[2], d[3]))
    t = io.open(os.path.join(LOOP, "REPORTE.md"), encoding="utf-8").read()
    w("   CIFRA lineas: %d" % len(t.replace(chr(13) + NL, NL).split(NL)))
    w("   CIFRA guiones largos: %d | guiones medios: %d"
      % (t.count(chr(8212)), t.count(chr(8211))))
    w("")

    w("H) LOS FICHEROS QUE ESTA VUELTA ANADIO A scripts/loop/, Y SU PREFIJO")
    c, o = git(["diff", head_ap, "--name-status", "--", "scripts/loop/"])
    nuevos = [l.split("\t")[-1] for l in o.split(NL)
              if l.startswith("A") and l.strip()]
    con = [x for x in nuevos if os.path.basename(x).startswith("_")]
    sin = [x for x in nuevos if not os.path.basename(x).startswith("_")]
    w("   CIFRA ficheros anadidos a scripts/loop/: %d" % len(nuevos))
    w("   CIFRA con prefijo de guion bajo: %d" % len(con))
    w("   CIFRA SIN prefijo de guion bajo: %d (%s)"
      % (len(sin), ", ".join(sin) or "ninguno"))
    for x in sorted(nuevos):
        w("      %s" % x)
    w("")
    w("FIN")
    salida = NL.join(L) + NL
    print(salida)
    io.open(os.path.join(LOOP, "SALIDA_V%d_%s.txt" % (VUELTA, a.salida)),
            "w", encoding="utf-8", newline=NL).write(salida)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
