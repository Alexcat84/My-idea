# -*- coding: utf-8 -*-
r"""vuelta141_2d_mutacion_commits.py . LA PRUEBA DE MUTACION DE --comparar-commits
(TAREA 2.d de la vuelta 141, acta de la vuelta 140, caida 4.3).

QUE PRUEBA. Que el cotejo nuevo del bloque de commits MUERDE. Se fabrica un
fichero de reporte de mentira, con las dos marcas del delimitador y el bloque
TALLADO DE GIT dentro, y se corre --comparar-commits sobre el:

  (a) CONTRAPRUEBA, bloque intacto: VERDE, exit 0.
  (b) COMMIT INVENTADO metido dentro del bloque: ROJO, exit 1, y la salida
      NOMBRA la linea inventada.
  (c) ORDEN CAMBIADO (dos commits intercambiados): ROJO, exit 1.
  (d) ASUNTO TRUNCADO: VERDE, y la salida DECLARA el truncado en su cuenta.
  (e) ASUNTO CAMBIADO por otro que no es prefijo del real: ROJO, exit 1.

NADA SE TECLEA. El commit de apertura sale de la misma funcion que la fila de
identidad ya usa (commit_apertura_desde_git), los commits salen de git log, y
el hash inventado se fabrica alterando UN caracter del ultimo hash real, con lo
que se comprueba ademas que no existe en git antes de usarlo. P.16, QUIEN
FABRICA LIMPIA: el fichero temporal se borra siempre, y su nombre NO SALE EN LA
SALIDA (la caida 4.2 del acta 140: una salida sellada que no es reproducible).

PRUEBA DE MUTACION DEL PROPIO ARNES (EJECUTOR.md regla 1): al final se
RE-EVALUA cada comprobacion con el valor esperado cambiado y se exige que todas
caigan. La que siga verde con el esperado mutado no puede fallar nunca.

USO:
  python scripts/loop/vuelta141_2d_mutacion_commits.py
"""
import io
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tallar_cabecera_reporte as C

VUELTA = 141

_resultados = []


def comprobar(nombre, obtenido, esperado):
    ok = obtenido == esperado
    _resultados.append((nombre, obtenido, esperado, ok))
    print("   %-6s %s | obtenido=%r esperado=%r" % ("VERDE" if ok else "ROJO", nombre,
                                                    obtenido, esperado))
    return ok


def escribir_reporte(ruta, lineas):
    io.open(ruta, "w", encoding="utf-8", newline="\n").write(
        "# REPORTE DE MENTIRA PARA LA PRUEBA DE MUTACION\n\n"
        + C.MARCA_COMMITS_ABRE + "\n\n```\n"
        + "\n".join(lineas) + "\n```\n\n"
        + C.MARCA_COMMITS_CIERRA + "\n")


def correr(ruta):
    r = subprocess.run([sys.executable,
                        os.path.join(RAIZ, "scripts", "loop", "tallar_cabecera_reporte.py"),
                        "--vuelta", str(VUELTA), "--comparar-commits", ruta],
                       cwd=RAIZ, capture_output=True, text=True)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    fallos = []
    rama = C.rama_actual(fallos)
    apertura, _asunto = C.commit_apertura_desde_git(VUELTA, rama, fallos)
    if fallos:
        for x in fallos:
            print("ROJO (arnes): %s" % x)
        return 1
    reales = C.commits_de_git(apertura, fallos)
    if fallos or not reales:
        print("ROJO (arnes): git log %s..HEAD no da ningun commit que cotejar" % apertura)
        return 1
    print("commit de apertura (de git, no tecleado): %s" % apertura)
    print("commits reales en el rango: %d" % len(reales))
    print("")

    lineas_ok = ["  %s %s" % (h[:8], s) for h, s in reales]

    tmp = tempfile.mkdtemp(prefix="v141_2d_")
    try:
        ruta = os.path.join(tmp, "REPORTE_DE_MENTIRA.md")

        print("(a) CONTRAPRUEBA: EL BLOQUE INTACTO.")
        escribir_reporte(ruta, lineas_ok)
        codigo, salida = correr(ruta)
        comprobar("(a) el bloque intacto da exit 0", codigo, 0)
        comprobar("(a) la salida dice IDENTICO A GIT",
                  "BLOQUE DE COMMITS: IDENTICO A GIT" in salida, True)
        print("")

        print("(b) COMMIT INVENTADO DENTRO DEL BLOQUE.")
        # El hash inventado se FABRICA alterando un caracter del ultimo real, y
        # se comprueba contra git que NO existe antes de usarlo.
        ultimo = reales[-1][0]
        inventado = ("0" if ultimo[0] != "0" else "1") + ultimo[1:]
        existe = subprocess.run(["git", "cat-file", "-e", inventado + "^{commit}"],
                                cwd=RAIZ, capture_output=True).returncode == 0
        comprobar("(b) el hash fabricado NO existe en git (computado)", existe, False)
        print("       hash inventado: %s" % inventado[:8])
        escribir_reporte(ruta, lineas_ok + ["  %s COMMIT QUE NUNCA EXISTIO" % inventado[:8]])
        codigo_b, salida_b = correr(ruta)
        comprobar("(b) el commit inventado da exit 1", codigo_b, 1)
        comprobar("(b) la salida NOMBRA el hash inventado",
                  inventado[:8] in salida_b, True)
        comprobar("(b) la salida dice NO CALZA CON GIT",
                  "BLOQUE DE COMMITS: NO CALZA CON GIT" in salida_b, True)
        print("")

        if len(reales) >= 2:
            print("(c) ORDEN CAMBIADO: DOS COMMITS INTERCAMBIADOS.")
            revuelto = list(lineas_ok)
            revuelto[0], revuelto[1] = revuelto[1], revuelto[0]
            escribir_reporte(ruta, revuelto)
            codigo_c, salida_c = correr(ruta)
            comprobar("(c) el orden cambiado da exit 1", codigo_c, 1)
            comprobar("(c) la salida dice hash distinto o fuera de orden",
                      "fuera de orden" in salida_c, True)
            print("")
        else:
            print("(c) OMITIDO: el rango trae menos de dos commits, no hay orden que romper.")
            print("")

        print("(d) ASUNTO TRUNCADO: TIENE QUE PASAR Y QUEDAR DECLARADO.")
        truncadas = ["  %s %s" % (h[:8], s[:20]) for h, s in reales]
        n_truncados = sum(1 for h, s in reales if len(s) > 20)
        escribir_reporte(ruta, truncadas)
        codigo_d, salida_d = correr(ruta)
        comprobar("(d) el asunto truncado sigue dando exit 0", codigo_d, 0)
        comprobar("(d) la salida DECLARA cuantos asuntos van truncados",
                  ("asuntos TRUNCADOS y declarados como tales: %d" % n_truncados) in salida_d,
                  True)
        print("")

        print("(e) ASUNTO CAMBIADO POR OTRO QUE NO ES PREFIJO DEL REAL.")
        cambiadas = list(lineas_ok)
        cambiadas[0] = "  %s ASUNTO QUE NADIE ESCRIBIO NUNCA" % reales[0][0][:8]
        escribir_reporte(ruta, cambiadas)
        codigo_e, salida_e = correr(ruta)
        comprobar("(e) el asunto cambiado da exit 1", codigo_e, 1)
        comprobar("(e) la salida dice que el asunto NO es prefijo del real",
                  "NO es prefijo del real" in salida_e, True)
        print("")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print("PRUEBA DE MUTACION DEL PROPIO ARNES: se cambia el valor esperado de CADA")
    print("comprobacion y se RE-EVALUA contra el MISMO valor obtenido.")
    no_caen = []
    for nombre, obtenido, esperado, _ok in _resultados:
        if isinstance(esperado, bool):
            mutado = not esperado
        else:
            mutado = esperado + 1
        if obtenido == mutado:
            no_caen.append(nombre)
    verdes = sum(1 for r in _resultados if r[3])
    print("   comprobaciones corridas: %d | verdes: %d | caen con el esperado mutado: %d"
          % (len(_resultados), verdes, len(_resultados) - len(no_caen)))
    for nombre in no_caen:
        print("   NO CAE con el esperado mutado: %s" % nombre)
    print("")
    if verdes == len(_resultados) and not no_caen:
        print("VERDE: las %d comprobaciones pasan, y las %d caen al mutarles el esperado."
              % (len(_resultados), len(_resultados)))
        return 0
    print("ROJO: %d fallan, %d no caen al mutar su esperado."
          % (len(_resultados) - verdes, len(no_caen)))
    for nombre, _o, _e, ok in _resultados:
        if not ok:
            print("   FALLA: %s" % nombre)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
