# -*- coding: utf-8 -*-
r"""vuelta172_relectura_al_doble.py . LA SEGUNDA COMPROBACION, Y ESTA VEZ SOBRE
LO PROPIO.

POR QUE NACE, Y LLEVA NOMBRE PROPIO Y AJENO (acta del auditor de la vuelta 171,
seccion 4.1): el encargo de la vuelta 171 mando releer al doble las cuatro
piezas del cierre, y la 171 LO HIZO Y LO HIZO BIEN, sobre el cierre de la 170,
con once comprobaciones desde `git show` y cero fallos. Lo que no hizo fue
aplicarselo a si misma, y se quedo sin cerrar su propio reporte. EL REMEDIO SE
APLICO HACIA ATRAS. Aqui se aplica hacia adelante.

LAS CUATRO PIEZAS, y cada una se comprueba DOS veces: una al hacerla, dentro de
su instrumento y leyendo del disco, y otra AQUI, DESPUES DE COMMITEAR, leyendo
de `git show` lo que se acaba de escribir.

  1. EL REPORTE CERRADO      . secciones 3 a 9 presentes, veredicto escrito,
                               discutibles y caidas contados, cero guiones
                               largos y medios.
  2. LA CABECERA PEGADA      . las filas del fichero del tallador, dentro del
                               reporte commiteado, byte a byte.
  3. LA BATERIA CORRIDA      . la salida de la bateria, dentro de la seccion 9
                               del reporte commiteado, y con bytes de verdad.
  4. EL ARBOL LIMPIO         . `git status --porcelain` sin nada que no sea la
                               suciedad de indice ya medida y `node_modules/`.

NINGUNA CIFRA SE TECLEA: todas salen de `git show`, `git status` o de contar el
fichero que se cita. Y NINGUNA PIEZA SE DA POR BUENA POR HABERSE HECHO: se da
por buena por haberse LEIDO DE GIT despues.

USO:
  python scripts/loop/vuelta172_relectura_al_doble.py --piezas 1,2
  python scripts/loop/vuelta172_relectura_al_doble.py --piezas 1,2,3,4
"""
import argparse
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
TALLADOR_171 = os.path.join(LOOP, "SALIDA_V171_TALLADOR_CABECERA.txt")
NL = chr(10)

# La suciedad ya medida y adjudicada, que NO cuenta como arbol sucio:
#  . master_graph.json con diff de cero bytes (suciedad de indice, medida en las
#    vueltas 169, 170, 171 y en la apertura de la 172).
#  . node_modules/, que no se toca y no entra en .gitignore por decision del
#    fundador (adjudicacion 6.5 del acta 170).
TOLERADAS = ("dataset/metadata/master_graph.json", "node_modules/")


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def leer(ruta):
    return io.open(ruta, encoding="utf-8").read().replace(chr(13) + NL, NL)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--piezas", default="1,2")
    ap.add_argument("--vuelta-del-reporte", type=int, default=171)
    a = ap.parse_args()
    piezas = [int(x) for x in a.piezas.split(",") if x.strip()]
    vr = a.vuelta_del_reporte

    print("=" * 78)
    print("LA RELECTURA AL DOBLE, PIEZAS %s, LEIDA DE GIT DESPUES DE COMMITEAR"
          % ", ".join(str(p) for p in piezas))
    print("=" * 78)
    print("")

    c, head = git(["rev-parse", "--short", "HEAD"])
    head = head.strip()
    c, asunto = git(["log", "-1", "--format=%s"])
    print("HEAD desde el que se lee (git rev-parse, no tecleado): %s" % head)
    print("   su asunto: %s" % asunto.strip()[:96])
    print("")

    fallos = []
    hechas = 0

    # ------------------------------------------------------ PIEZA 1 Y PIEZA 2
    if 1 in piezas or 2 in piezas:
        print("EL SUJETO: docs/loop/REPORTE.md, LEIDO DE git show HEAD:")
        c, stat = git(["show", "--stat", "--format=", "HEAD"])
        en_el_commit = "docs/loop/REPORTE.md" in stat
        print("   docs/loop/REPORTE.md entre los ficheros de %s: %s"
              % (head, "SI" if en_el_commit else "NO"))
        c, rep = git(["show", "HEAD:docs/loop/REPORTE.md"])
        rep = rep.replace(chr(13) + NL, NL)
        print("   CIFRA bytes: %d | saltos de linea: %d"
              % (len(rep.encode("utf-8")), rep.count(NL)))
        print("")

    if 1 in piezas:
        print("PIEZA 1. EL REPORTE CERRADO")
        pruebas = [
            ("es el reporte de la vuelta %d" % vr,
             rep.split(NL, 1)[0].startswith("# REPORTE DE LA VUELTA %d" % vr)),
            ("el veredicto ya no dice SIN ESCRIBIR TODAVIA",
             "SIN ESCRIBIR TODAVIA" not in rep),
            ("el hueco PENDIENTE DE TALLAR AL CIERRE ya no esta",
             "PENDIENTE DE TALLAR AL CIERRE" not in rep),
            ("el veredicto de una linea esta escrito",
             "**EL VEREDICTO DE UNA LINEA:" in rep),
        ]
        for k in range(3, 10):
            pruebas.append(("la seccion %d existe" % k, (NL + "## %d." % k) in rep))
        n_disc = len(re.findall(r"^- \*\*`D\.\d+`", rep, re.M))
        n_caidas = len(re.findall(r"^- \*\*`CAIDA \d+`", rep, re.M))
        print("   CIFRA discutibles contados del fichero commiteado: %d" % n_disc)
        print("   CIFRA caidas contadas del fichero commiteado: %d" % n_caidas)
        pruebas.append(("los cuatro discutibles siguen enteros", n_disc == 4))
        pruebas.append(("la caida sigue entera", n_caidas == 1))
        pruebas.append(("cero guiones largos y cero guiones medios",
                        chr(8212) not in rep and chr(8211) not in rep))
        pruebas.append(("la seccion 3 no publica ningun hash que git no conozca",
                        all(git(["cat-file", "-e", h + "^{commit}"])[0] == 0
                            for h in re.findall(r"^\| \d+ \| `([0-9a-f]{7,40})` \|",
                                                rep, re.M))))
        for etiqueta, cond in pruebas:
            print("   %-58s %s" % (etiqueta, "SI" if cond else "NO"))
            if not cond:
                fallos.append("PIEZA 1: " + etiqueta)
        hechas += len(pruebas)
        print("")

    if 2 in piezas:
        print("PIEZA 2. LA CABECERA PEGADA, COTEJADA FILA A FILA CONTRA EL TALLADOR")
        sal = leer(TALLADOR_171)
        filas = [l.rstrip() for l in sal.split(NL) if l.strip().startswith("|")]
        print("   %s -> %d filas de tabla"
              % (os.path.relpath(TALLADOR_171, RAIZ).replace(os.sep, "/"), len(filas)))
        dentro = 0
        for l in filas:
            hay = l in rep
            if hay:
                dentro += 1
            else:
                fallos.append("PIEZA 2: fila ausente del reporte commiteado: %s" % l[:70])
        print("   CIFRA filas del tallador dentro del reporte commiteado: %d de %d"
              % (dentro, len(filas)))
        cond = dentro == len(filas) and len(filas) >= 8
        print("   %-58s %s" % ("las %d filas estan las %d" % (len(filas), len(filas)),
                               "SI" if cond else "NO"))
        hechas += 1
        print("")

    # ---------------------------------------------------------------- PIEZA 3
    if 3 in piezas:
        print("PIEZA 3. LA BATERIA CORRIDA, DENTRO DE LA SECCION 9 DEL REPORTE")
        c, rep2 = git(["show", "HEAD:docs/loop/REPORTE.md"])
        rep2 = rep2.replace(chr(13) + NL, NL)
        vuelta_viva = int(re.match(r"^# REPORTE DE LA VUELTA (\d+)",
                                   rep2.split(NL, 1)[0]).group(1))
        salida = os.path.join(LOOP, "SALIDA_V%d_BATERIA.txt" % vuelta_viva)
        rel_sal = os.path.relpath(salida, RAIZ).replace(os.sep, "/")
        existe = os.path.exists(salida)
        tam = os.path.getsize(salida) if existe else -1
        print("   el reporte commiteado es el de la vuelta %d" % vuelta_viva)
        print("   %s -> %s" % (rel_sal, ("%d bytes" % tam) if existe else "NO EXISTE"))
        i9 = rep2.index(NL + "## 9.")
        seccion9 = rep2[i9:]
        print("   CIFRA bytes de la seccion 9 del reporte commiteado: %d"
              % len(seccion9.encode("utf-8")))
        texto_bat = leer(salida) if existe and tam > 0 else ""
        lineas_bat = [l for l in texto_bat.split(NL) if l.strip()]
        dentro = sum(1 for l in lineas_bat if l.rstrip() in seccion9)
        print("   CIFRA lineas no vacias de la salida de la bateria: %d" % len(lineas_bat))
        print("   CIFRA de esas lineas que estan dentro de la seccion 9: %d" % dentro)
        pruebas = [
            ("la salida de la bateria existe y no mide cero bytes", existe and tam > 0),
            ("la salida de la bateria entera esta dentro de la seccion 9",
             bool(lineas_bat) and dentro == len(lineas_bat)),
            ("la seccion 9 nombra su fichero de salida", rel_sal in seccion9),
        ]
        for etiqueta, cond in pruebas:
            print("   %-58s %s" % (etiqueta, "SI" if cond else "NO"))
            if not cond:
                fallos.append("PIEZA 3: " + etiqueta)
        hechas += len(pruebas)
        print("")

    # ---------------------------------------------------------------- PIEZA 4
    if 4 in piezas:
        print("PIEZA 4. EL ARBOL LIMPIO, LEIDO DE git status DESPUES DE COMMITEAR")
        c, st = git(["status", "--porcelain"])
        lineas = [l for l in st.split(NL) if l.strip()]
        print("   CIFRA lineas de git status --porcelain: %d" % len(lineas))
        sobrantes = []
        for l in lineas:
            ruta = l[3:].strip().strip('"')
            tolerada = any(ruta == t or ruta.startswith(t) for t in TOLERADAS)
            print("      %-58s %s" % (l[:58], "TOLERADA" if tolerada else "SOBRA"))
            if not tolerada:
                sobrantes.append(ruta)
        c, d = git(["diff", "--numstat", "--", "dataset/metadata/master_graph.json"])
        filas_d = [x for x in d.split(NL) if x.strip()]
        print("   CIFRA filas de numstat de master_graph.json: %d (cero = suciedad)"
              % len(filas_d))
        c, ahead = git(["rev-list", "--left-right", "--count", "HEAD...@{u}"])
        print("   adelante/atras contra el remoto: %s" % ahead.strip())
        pruebas = [
            ("no queda nada suelto fuera de lo tolerado y medido", not sobrantes),
            ("master_graph.json sigue con diff de cero filas", len(filas_d) == 0),
            ("nada por empujar al remoto", ahead.strip().replace(chr(9), " ") == "0 0"),
        ]
        for etiqueta, cond in pruebas:
            print("   %-58s %s" % (etiqueta, "SI" if cond else "NO"))
            if not cond:
                fallos.append("PIEZA 4: " + etiqueta)
        hechas += len(pruebas)
        print("")

    print("=" * 78)
    print("CIFRA comprobaciones corridas: %d | FALLAN: %d" % (hechas, len(fallos)))
    for f in fallos:
        print("   " + f)
    if fallos:
        print("ROJO: la relectura al doble no pasa.")
        return 1
    print("VERDE: las piezas %s se leyeron de git y calzan."
          % ", ".join(str(p) for p in piezas))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
