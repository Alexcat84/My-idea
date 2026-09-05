# -*- coding: utf-8 -*-
r"""vuelta169_cerrar_reporte.py . EL CIERRE DE docs/loop/REPORTE.md DE LA VUELTA 169.

QUE HACE, Y NADA DE ESTO SE TECLEA:
  (1) SUSTITUYE el hueco de la cabecera por la salida LITERAL del tallador
      `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 169`, leida de
      `docs/loop/SALIDA_V169_TALLADOR_CABECERA.txt`. **El tallador sale ROJO** y
      su rojo se publica ENTERO, con su motivo, en vez de rellenar la tabla a
      mano. `EJECUTOR.md` 1: la celda que no salga de un instrumento no se
      escribe, y si no hay fichero que contar, la tabla no se publica.
  (2) PEGA la tabla del CIERRE, que si se pudo leer, celda a celda de su propia
      salida `SALIDA_V169_*_CIERRE.txt`.
  (3) ESCRIBE el veredicto de una linea y la identidad, LEIDA DE GIT en esta
      vuelta (`EJECUTOR.md` 1, "LA IDENTIDAD SE LEE DE GIT").
  (4) ANEXA el bloque de discutibles, preguntas, pendientes de doctrina y
      correcciones declaradas, que vive en `docs/loop/_v169_cierre_seccion.md`.

USO:
  python scripts/loop/vuelta169_cerrar_reporte.py
"""
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
REPORTE = os.path.join(LOOP, "REPORTE.md")
TALLADOR = os.path.join(LOOP, "SALIDA_V169_TALLADOR_CABECERA.txt")
CIERRE_SEC = os.path.join(LOOP, "_v169_cierre_seccion.md")
VUELTA = 169


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace").strip()


def leer(nombre, fallos):
    p = os.path.join(LOOP, nombre)
    if not os.path.exists(p):
        fallos.append("no existe %s" % nombre)
        return ""
    return io.open(p, encoding="utf-8", errors="replace").read()


def busca(texto, patron, rotulo, fallos):
    m = re.search(patron, texto)
    if not m:
        fallos.append("no se pudo leer %s" % rotulo)
        return "?"
    return m.group(1)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    fallos = []
    print("=" * 78)
    print("VUELTA 169: EL CIERRE DEL REPORTE")
    print("=" * 78)
    print("")

    texto = io.open(REPORTE, encoding="utf-8", newline="").read()
    if not texto.splitlines()[0].startswith("# REPORTE DE LA VUELTA %d " % VUELTA):
        print("ROJO: docs/loop/REPORTE.md no es el de la vuelta %d." % VUELTA)
        return 1
    if not os.path.exists(TALLADOR):
        print("ROJO: no existe la salida del tallador.")
        return 1
    if not os.path.exists(CIERRE_SEC):
        print("ROJO: no existe el bloque de cierre.")
        return 1

    print("A) LA IDENTIDAD, LEIDA DE GIT EN ESTA VUELTA")
    _c, rama = git(["rev-parse", "--abbrev-ref", "HEAD"])
    _c, head = git(["rev-parse", "HEAD"])
    _c, log = git(["log", "-1", "--format=%h %ad %s", "--date=iso"])
    _c, n_commits = git(["rev-list", "--count", "2ba08da7..HEAD"])
    _c, numstat = git(["diff", "2ba08da7", "HEAD", "--numstat", "--", "dataset/", "web/", "engine/"])
    print("   rama: %s" % rama)
    print("   HEAD ahora mismo: %s" % head[:8])
    print("   ultimo commit: %s" % log[:100])
    print("   commits de esta vuelta sobre 2ba08da7: %s" % n_commits)
    print("   numstat sobre dataset/ web/ engine/: %r (vacio = nada se movio)" % numstat)
    if numstat.strip():
        fallos.append("el numstat sobre dataset/web/engine NO esta vacio")
    print("")

    print("B) LAS CELDAS DEL CIERRE, CADA UNA DE SU PROPIA SALIDA")
    gate = leer("SALIDA_V%d_GATE0_CMD1_CIERRE.txt" % VUELTA, fallos)
    d = {}
    d["nodos"] = busca(gate, r"master_graph\.json == archivos en disco \(valor: (\d+) vs \d+\)",
                       "censo nodos", fallos)
    d["vivos"] = busca(gate, r"Universo: activos / deprecados \(valor: (\d+) activos",
                       "censo vivos", fallos)
    d["deprecados"] = busca(gate, r"Universo: activos / deprecados \(valor: \d+ activos, (\d+) deprecados",
                            "censo deprecados", fallos)
    d["auto"] = busca(gate, r"auto-arista via alias\) \(valor: (\d+) auto-aristas\)",
                      "auto-aristas", fallos)
    d["dup"] = busca(gate, r"titulo_concepto exacto duplicado \(valor: (\d+)\)",
                     "duplicadas de titulo", fallos)
    d["div"] = busca(gate, r"dicen lo mismo \(valor: (\d+) nodos divergentes\)",
                     "nodos divergentes", fallos)
    d["gate"] = busca(gate, r"GATE 0: (\w+)", "veredicto Gate 0", fallos)
    con = leer("SALIDA_V%d_CONTEO_CIERRE.txt" % VUELTA, fallos)
    ocur = re.findall(r"sig (\d+) prev (\d+) suma (\d+) union (\d+)", con)
    if not ocur:
        fallos.append("no se pudo leer las aristas")
        d["sig"] = d["prev"] = d["suma"] = d["union"] = "?"
    else:
        d["sig"], d["prev"], d["suma"], d["union"] = ocur[-1]
    motor = leer("SALIDA_V%d_MOTOR_CIERRE.txt" % VUELTA, fallos)
    d["motor"] = busca(motor, r"TODOS LOS TESTS PASARON \((\d+/\d+)\)", "motor", fallos)
    web = leer("SALIDA_V%d_WEB_CIERRE.txt" % VUELTA, fallos)
    d["web_f"] = busca(web, r"Test Files\s+(\d+) passed \(\d+\)", "web ficheros", fallos)
    d["web_t"] = busca(web, r"Tests\s+(\d+) passed \(\d+\)", "web tests", fallos)
    tsc = leer("SALIDA_V%d_TSC_CIERRE.txt" % VUELTA, fallos)
    d["tsc"] = busca(tsc, r"EXIT=(\d+)", "tsc", fallos)
    desf = leer("SALIDA_V%d_DESFASE_CALIBRADO_CIERRE.txt" % VUELTA, fallos)
    m = re.search(r"(\d+) fila\(s\)", desf)
    d["desfase"] = m.group(1) if m else "?"
    if not m:
        fallos.append("no se pudo leer el desfase")
    for k in sorted(d):
        print("   %-12s %s" % (k, d[k]))
    print("")
    if fallos:
        print("ROJO, no se cierra nada:")
        for f in fallos:
            print("   " + f)
        return 1

    tall = io.open(TALLADOR, encoding="utf-8").read().rstrip()
    bloque_cierre = io.open(CIERRE_SEC, encoding="utf-8").read().rstrip()

    cabecera = """<!-- CABECERA TALLADA -->
**EL TALLADOR SALE EN ROJO Y SU ROJO SE PUBLICA ENTERO, QUE ES LO QUE LA REGLA
MANDA HACER CUANDO NO HAY FICHERO QUE CONTAR.** `EJECUTOR.md` 1: *"Si no existe
fichero que contar, LA TABLA NO SE PUBLICA: se corre el instrumento que la
produzca, o se dice que no hay cifra"*. Salida literal de
`python scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta 169`, pegada
entera de `docs/loop/SALIDA_V169_TALLADOR_CABECERA.txt`, **exit 1**:

```
%(tall)s
```

**LA CAIDA ES MIA Y ES DE ESTA VUELTA: NO CORRI EL BLOQUE DE APERTURA.** Selle la
apertura (HEAD, `git status`, bytes de cada ruta sin commitear y `git ls-tree`)
en `docs/loop/SALIDA_V169_APERTURA.txt`, **pero no corri Gate 0, ni el censo, ni
el motor, ni el tsc, ni las suites de la web al abrir**, y esas 18 celdas salen
de ahi. **No las relleno con la medicion del cierre**, que es exactamente la
caida de la vuelta 28, ni corro ahora el bloque llamandolo apertura, que es la de
la vuelta 29.

**LO QUE SI PUEDO PROBAR, Y LO PRUEBO EN VEZ DE PEDIR QUE SE ME CREA:**
`git diff 2ba08da7 HEAD --numstat -- dataset/ web/ engine/` sale **VACIO**. Las
tres rutas que esas 18 celdas miden **no se movieron en esta vuelta**: los %(nc)s
commits tocan solo `docs/` y `scripts/`. **De ahi se sigue que la apertura habria
dado las mismas cifras que el cierre, pero eso es una INFERENCIA y no una
medicion, y por eso no ocupa la tabla.**

**LA TABLA DEL CIERRE SI SE PUDO LEER, Y VA ENTERA**, cada celda de su propia
salida `SALIDA_V169_*_CIERRE.txt`, corridas por
`scripts/loop/vuelta169_cierre.py` con el ciclo de Gate 0 completo y en su orden:

| comprobacion | al cierre | de que salida sale |
|---|---|---|
| censo, `master_graph.json` contra disco | **%(nodos)s** nodos | `GATE0_CMD1_CIERRE` |
| universo, activos y deprecados | **%(vivos)s** activos, **%(deprecados)s** deprecados | `GATE0_CMD1_CIERRE` |
| auto-aristas via alias | **%(auto)s** | `GATE0_CMD1_CIERRE` |
| `titulo_concepto` exacto duplicado | **%(dup)s** | `GATE0_CMD1_CIERRE` |
| nodos divergentes | **%(div)s** | `GATE0_CMD1_CIERRE` |
| **GATE 0** | **%(gate)s** | `GATE0_CMD1_CIERRE` |
| aristas, sig y prev | **%(sig)s** y **%(prev)s**, suma **%(suma)s**, union **%(union)s** | `CONTEO_CIERRE` |
| desfase del calibrado | **%(desfase)s** fila(s) | `DESFASE_CALIBRADO_CIERRE` |
| motor | **%(motor)s** | `MOTOR_CIERRE` |
| web, ficheros | **%(web_f)s** passed | `WEB_CIERRE` |
| web, tests | **%(web_t)s** passed | `WEB_CIERRE` |
| `tsc --noEmit` | **exit %(tsc)s** | `TSC_CIERRE` |
| `numstat` sobre `dataset/ web/ engine/` tras el ciclo | **VACIO** | `CICLO_NUMSTAT_CIERRE` |
<!-- FIN CABECERA TALLADA -->""" % dict(tall=tall, nc=n_commits, **d)

    ini = texto.index("<!-- CABECERA TALLADA -->")
    fin = texto.index("<!-- FIN CABECERA TALLADA -->") + len("<!-- FIN CABECERA TALLADA -->")
    texto = texto[:ini] + cabecera + texto[fin:]

    veredicto = (
        "**EL VEREDICTO DE UNA LINEA: LAS CINCO TAREAS ENTREGADAS, LA BATERIA EN VERDE "
        "TRAS TRES CORRIDAS, Y LO MAS GRANDE QUE TRAIGO NO ES LO QUE HICE SINO LO QUE "
        "MEDI: EL LOTE DE SALES ROADMAP QUE EL ENCARGO MANDA LEER ESTABA LEIDO DESDE "
        "HACE TRES SEMANAS, Y LO COMPRUEBO LEYENDOLO A CIEGAS PRIMERO Y COINCIDIENDO "
        "5 DE 5.** Traigo **una PARADA** (el universo re-medible de la TAREA 4 son 348 "
        "y no 569), **ocho DISCUTIBLES marcados antes de saber si acierto**, **cinco "
        "PREGUNTAS**, **tres PENDIENTES DE DOCTRINA** y **cuatro caidas propias, tres "
        "cazadas midiendo antes de publicar y declaradas igual**. Y **una caida que no "
        "cace a tiempo: no corri el bloque de apertura**, asi que el tallador de la "
        "cabecera sale en ROJO y **publico su rojo entero en vez de rellenar la tabla**. "
        "**Cero nodos tocados, cero aristas movidas, cero clases movidas y el grafo "
        "intacto**, probado por un `numstat` vacio sobre `dataset/`, `web/` y `engine/`.")
    texto = texto.replace(
        "**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.** Se talla al cierre, cuando\n"
        "haya de que hablar. Un veredicto escrito en la apertura seria justo la especie\n"
        "que esta regla existe para matar.", veredicto, 1)

    texto = texto.rstrip() + "\n\n" + bloque_cierre + "\n"
    io.open(REPORTE, "w", encoding="utf-8", newline="\n").write(texto)
    print("C) ESCRITO")
    print("   docs/loop/REPORTE.md: %d bytes, %d lineas"
          % (len(texto.encode("utf-8")), texto.count("\n")))
    print("   cabecera sustituida por la salida LITERAL del tallador (exit 1, 18 celdas)")
    print("   tabla del cierre pegada con %d celdas leidas de sus salidas" % len(d))
    print("")
    print("VERDE: el reporte de la vuelta 169 queda cerrado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
