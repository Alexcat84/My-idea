# -*- coding: utf-8 -*-
r"""guarda_commit_dataset.py . LA GUARDA DEL COMMIT: NO SE COMMITEA `dataset/`
CON UNA MUTACION DE BATERIA SIN RESTAURAR DENTRO.

NOMBRE ESTABLE Y SIN NUMERO DE VUELTA, como `verificar_mutaciones_viejas.py`,
`cerrar_reporte.py`, `paso0_archivar_anterior.py` y `tallar_cabecera_reporte.py`:
esta guarda tiene que correr en LA PRIMERA LINEA DE TODO ENCARGO, en toda vuelta,
y una guarda que se clona por vuelta es una guarda que un dia no se clona.

POR QUE NACE, Y LA CAUSA ESTA MEDIDA POR EL AUDITOR EN SU ACTA DE LA VUELTA 175,
NO SUPUESTA. La vuelta 175 murio DENTRO de la bateria. El arnes
`scripts/loop/vuelta154_tarea2d_mutacion_guarda.py` mete a proposito un alias
deprecado en las dos listas de `ab_testing_optimizacion`, `run_phase1` lo
simetriza, y su restauracion vive en un `finally`: A UN `finally` LO MATA QUIEN
MATE AL PROCESO. El arbol le llego al auditor con esa arista bidireccional
metida en `dataset/`, y el la restauro a mano con `git checkout --` sobre cuatro
ficheros.

EL AGUJERO NO ESTA EN LA BATERIA, ESTA UN PASO ANTES, Y ES EL QUE ENCARGA. La
primera linea de todo encargo dice "commitea y pushea lo pendiente", y con el
arbol asi esa linea METE LA MUTACION EN LA HISTORIA DEL CATALOGO. El auditor lo
midio en vez de suponerlo: corrio el arnes culpable entero y su CASO A pone
Gate 0 en rojo nombrando el par (`ab_testing_optimizacion` contra
`abandonar_arreglos_rapidos`, 155 pares tras resolver, 154 con cita, 1 SIN
CITA), o sea que la arista NO podia entrar callada por Gate 0. Podia entrar
callada POR EL COMMIT, que corre antes que Gate 0.

QUE HACE, Y ES LO UNICO QUE HACE:

  1. Mide `git diff --numstat -- dataset/`. SI DEVUELVE UNA SOLA FILA, ROJO, y
     nombra los ficheros uno a uno con sus lineas anadidas y borradas.
  2. Mide TAMBIEN `git status --porcelain -- dataset/`, que NO manda en el
     veredicto pero se publica, porque las dos preguntas NO dan siempre lo
     mismo y callar la diferencia seria esconderla. En Windows un fichero
     puede salir como ` M` en `git status` y dar CERO FILAS en `--numstat`:
     ocurre cuando el contenido es identico y lo unico que cambio es el mtime o
     el final de linea que `core.autocrlf` normaliza al vuelo.
  3. Para cada fichero que `git status` nombre, COTEJA SU CONTENIDO de verdad:
     `git hash-object <ruta>` contra `git rev-parse HEAD:<ruta>`. Si los dos
     blobs coinciden, el contenido es identico byte a byte y la `M` es de
     estado, no de contenido. Eso se dice con esas palabras y con los dos
     hashes al lado, para que nadie tenga que fiarse de la frase.

EL VEREDICTO SIGUE LA LETRA DEL ENCARGO: manda `--numstat`. Las otras dos
mediciones son corroboracion publicada, y si alguna vez `--numstat` diera cero
filas mientras los blobs DIFIEREN, esta guarda cae en ROJO igual y lo dice: dos
instrumentos que se contradicen sobre el catalogo son motivo de parada, no de
elegir el que conviene.

EL CASO ROJO SE PRUEBA POR MUTACION (`EJECUTOR.md` 1, 29 ago 2026): `--mutar`
NO compara literales. Fabrica un repo de git de verdad en un temporal, con un
`dataset/` dentro y un commit, y corre LA MISMA funcion `filas_sucias()` TRES
VECES: sobre el arbol limpio (tiene que dar CERO filas y VERDE), despues de
ensuciar el fichero (tiene que dar UNA fila, con EL NOMBRE SACADO DE GIT y no
tecleado, y ROJO), y despues de restaurarlo (tiene que volver solo a VERDE, que
es lo que distingue una guarda que mide de una que dice ROJO siempre).

USO:
  python scripts/loop/guarda_commit_dataset.py
  python scripts/loop/guarda_commit_dataset.py --mutar
"""
import argparse
import io
import os
import shutil
import stat
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NL = chr(10)


def _forzar_borrado(funcion, ruta, _exc):
    """P.16 EN WINDOWS. `git init` deja los objetos de `.git/objects` en SOLO
    LECTURA, y `shutil.rmtree` a secas falla contra ellos sin decir nada y deja
    el temporal en pie. Se midio aqui: la primera version de este fichero
    imprimia "el temporal se retira" y a renglon seguido "Existe todavia: True",
    o sea que la propia linea que anunciaba la retirada se desmentia sola. Se
    quita el bit de solo lectura y se reintenta."""
    os.chmod(ruta, stat.S_IWRITE)
    funcion(ruta)


def git(args, cwd):
    """Devuelve (exitcode, stdout). LA STDERR SE DESCARTA A PROPOSITO: en
    Windows git escribe ahi el aviso de LF/CRLF y ese aviso no es una fila."""
    r = subprocess.run(["git"] + args, cwd=cwd, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def filas_sucias(raiz, ruta="dataset/"):
    """LAS FILAS DE `git diff --numstat -- <ruta>`, una tupla por fila.

    Devuelve una lista de (anadidas, borradas, fichero). VACIA quiere decir que
    no hay ni una sola fila, que es la unica situacion en la que se puede
    commitear. NO interpreta nada: parte la salida de git y ya."""
    _c, salida = git(["diff", "--numstat", "--", ruta], raiz)
    filas = []
    for linea in salida.splitlines():
        if not linea.strip():
            continue
        partes = linea.split(chr(9))
        if len(partes) >= 3:
            filas.append((partes[0], partes[1], partes[2]))
        else:
            filas.append(("?", "?", linea.strip()))
    return filas


def ficheros_de_status(raiz, ruta="dataset/"):
    """LOS FICHEROS QUE `git status --porcelain` NOMBRA bajo <ruta>, con su
    codigo de dos letras. NO MANDA EN EL VEREDICTO: se publica al lado."""
    _c, salida = git(["status", "--porcelain", "--", ruta], raiz)
    out = []
    for linea in salida.splitlines():
        if len(linea) > 3:
            out.append((linea[:2], linea[3:].strip().strip(chr(34))))
    return out


def blobs_que_difieren(raiz, ficheros):
    """PARA CADA FICHERO, LOS DOS BLOBS: el del arbol y el de HEAD.

    Devuelve una lista de (ruta, blob_arbol, blob_head, iguales). Es la
    comprobacion que distingue una `M` de contenido de una `M` de estado."""
    out = []
    for ruta in ficheros:
        _c1, b1 = git(["hash-object", ruta], raiz)
        _c2, b2 = git(["rev-parse", "HEAD:%s" % ruta], raiz)
        b1 = b1.strip()
        b2 = b2.strip()
        out.append((ruta, b1, b2, bool(b1) and b1 == b2))
    return out


def veredicto(filas, difieren):
    """LOS MOTIVOS DE ROJO. VACIO quiere decir VERDE. PURA: recibe lo medido.

    Dos motivos, y el segundo existe porque dos instrumentos que se contradicen
    sobre el catalogo son parada y no eleccion:
      (1) `--numstat` devuelve una fila o mas;
      (2) `--numstat` calla pero los blobs DIFIEREN."""
    motivos = []
    if filas:
        motivos.append(
            "(1) `git diff --numstat -- dataset/` devuelve %d fila(s), y la letra "
            "del encargo dice que UNA SOLA FILA YA ES PARADA: commitear esto "
            "meteria una mutacion de bateria en el catalogo. Los ficheros: %s"
            % (len(filas), ", ".join(f for _a, _b, f in filas)))
    rotos = [(r, a, h) for r, a, h, ig in difieren if not ig]
    if not filas and rotos:
        motivos.append(
            "(2) `--numstat` da CERO FILAS pero %d fichero(s) tienen un blob de "
            "arbol distinto del de HEAD. Dos instrumentos que se contradicen "
            "sobre el catalogo son PARADA: %s"
            % (len(rotos), ", ".join("%s (%s contra %s)" % (r, a[:8], h[:8])
                                     for r, a, h in rotos)))
    return motivos


def mirar(raiz, titulo):
    """MIDE Y PUBLICA. Devuelve (ok, filas). No escribe nada en el repo."""
    print("-" * 78)
    print(titulo)
    print("-" * 78)
    filas = filas_sucias(raiz)
    print("  CIFRA filas de `git diff --numstat -- dataset/`: %d" % len(filas))
    for a, b, f in filas:
        print("      FILA: +%s -%s  %s" % (a, b, f))
    if not filas:
        print("      (ninguna fila)")

    est = ficheros_de_status(raiz)
    print("  CIFRA ficheros que `git status --porcelain -- dataset/` nombra: %d"
          % len(est))
    for cod, f in est:
        print("      STATUS %r %s" % (cod, f))
    if not est:
        print("      (ninguno)")

    dif = blobs_que_difieren(raiz, [f for _cod, f in est])
    print("  CIFRA ficheros con blob de arbol DISTINTO del de HEAD: %d"
          % len([1 for _r, _a, _h, ig in dif if not ig]))
    for r, a, h, ig in dif:
        print("      %s" % r)
        print("         blob del arbol: %s" % (a[:16] or "(no se pudo leer)"))
        print("         blob de HEAD  : %s" % (h[:16] or "(no se pudo leer)"))
        print("         CONTENIDO IDENTICO: %s" % ("SI" if ig else "NO"))
    if est and dif and all(ig for _r, _a, _h, ig in dif) and not filas:
        print("      LOS BLOBS CALZAN: la `M` de `git status` es de ESTADO (mtime o")
        print("      final de linea normalizado por core.autocrlf), no de CONTENIDO.")

    motivos = veredicto(filas, dif)
    print("")
    if motivos:
        print("  ROJO, %d motivo(s). NO SE COMMITEA `dataset/`:" % len(motivos))
        for m in motivos:
            print("      " + m)
        print("      REMEDIO: `git checkout -- <fichero>` sobre los que salgan, y")
        print("      volver a correr esta guarda hasta que de CERO FILAS.")
    else:
        print("  VERDE: cero filas y cero blobs divergentes. `dataset/` se puede")
        print("  commitear sin meter ninguna mutacion en el catalogo.")
    return (not motivos), filas


def prueba_por_mutacion():
    """EL CASO POSITIVO, SOBRE UN REPO DE GIT DE VERDAD Y NO SOBRE LITERALES."""
    print("=" * 78)
    print("PRUEBA DE MUTACION DE LA GUARDA DEL COMMIT")
    print("=" * 78)
    print("NO SE COMPARAN LITERALES: se fabrica un repo de git de verdad en un")
    print("temporal, con su `dataset/` y su commit, y se corre LA MISMA funcion")
    print("`filas_sucias()` sobre el arbol limpio, sobre el sucio y sobre el")
    print("restaurado.")
    print("")
    tmp = tempfile.mkdtemp(prefix="guarda_commit_dataset_")
    fallos = []
    sujeto_rel = "dataset/metadata/master_graph.json"
    try:
        git(["init", "-q"], tmp)
        git(["config", "user.email", "prueba@local"], tmp)
        git(["config", "user.name", "prueba"], tmp)
        os.makedirs(os.path.join(tmp, "dataset", "metadata"))
        sujeto = os.path.join(tmp, "dataset", "metadata", "master_graph.json")
        io.open(sujeto, "w", encoding="utf-8", newline=NL).write(
            chr(123) + '"nodes": [' + chr(123) + '"id": "ab_testing_optimizacion", '
            '"rel": []' + chr(125) + ']' + chr(125) + NL)
        otro = os.path.join(tmp, "fuera_de_dataset.txt")
        io.open(otro, "w", encoding="utf-8", newline=NL).write("esto no es dataset" + NL)
        git(["add", "-A"], tmp)
        git(["commit", "-q", "-m", "sujeto de la prueba"], tmp)
        print("  repo fabricado en un temporal, con %s dentro" % sujeto_rel)
        print("")

        ok_a, filas_a = mirar(tmp, "CASO A. EL ARBOL LIMPIO. TIENE QUE DAR VERDE.")
        if filas_a:
            fallos.append("CASO A: el arbol limpio devuelve %d fila(s) y tenia que "
                          "devolver CERO" % len(filas_a))
        if not ok_a:
            fallos.append("CASO A: el arbol limpio sale ROJO y tenia que salir VERDE")
        print("")

        # LA MUTACION: se mete una arista de mentira, que es exactamente la forma
        # de la que el arnes de la 154 dejo en el arbol de la 175.
        io.open(sujeto, "w", encoding="utf-8", newline=NL).write(
            chr(123) + '"nodes": [' + chr(123) + '"id": "ab_testing_optimizacion", '
            '"rel": ["abandonar_arreglos_rapidos"]' + chr(125) + ']' + chr(125) + NL)
        # Y SE ENSUCIA TAMBIEN ALGO DE FUERA DE dataset/, para comprobar que la
        # guarda mira `dataset/` y no "el repo entero".
        io.open(otro, "a", encoding="utf-8", newline=NL).write("y esto tampoco" + NL)

        ok_b, filas_b = mirar(tmp, "CASO B. EL ARBOL CON LA MUTACION SIN RESTAURAR. "
                                   "TIENE QUE DAR ROJO.")
        if ok_b:
            fallos.append("CASO B: el arbol sucio sale VERDE. LA GUARDA NO MUERDE.")
        if len(filas_b) != 1:
            fallos.append("CASO B: se esperaba EXACTAMENTE 1 fila y salieron %d"
                          % len(filas_b))
        nombres = [f for _a, _b, f in filas_b]
        # EL NOMBRE NO SE TECLEA COMO ESPERADO SUELTO: se exige que la fila que
        # git devuelve sea la del sujeto que esta prueba ensucio, y que la de
        # fuera de dataset/ NO este.
        if nombres != [sujeto_rel]:
            fallos.append("CASO B: la fila que git devuelve es %s y el sujeto "
                          "ensuciado es %s" % (nombres, sujeto_rel))
        if any("fuera_de_dataset" in n for n in nombres):
            fallos.append("CASO B: la guarda esta mirando fuera de dataset/")
        print("")

        # Y EL TERCER CASO, QUE ES EL QUE PRUEBA QUE LA GUARDA SE PUEDE APAGAR:
        # se restaura y tiene que volver sola a VERDE. Sin este caso, una guarda
        # que dijera ROJO SIEMPRE pasaria los dos anteriores.
        git(["checkout", "--", sujeto_rel], tmp)
        ok_c, filas_c = mirar(tmp, "CASO C. RESTAURADO CON `git checkout --`. TIENE "
                                   "QUE VOLVER SOLO A VERDE.")
        if filas_c:
            fallos.append("CASO C: tras restaurar quedan %d fila(s)" % len(filas_c))
        if not ok_c:
            fallos.append("CASO C: tras restaurar sigue en ROJO, o sea que esta "
                          "guarda dice ROJO pase lo que pase y no mide nada")
    finally:
        shutil.rmtree(tmp, onerror=_forzar_borrado)
        print("")
        print("  P.16: el temporal se retira. Existe todavia: %s" % os.path.exists(tmp))

    print("")
    print("=" * 78)
    if fallos:
        print("ROJO DE LA MUTACION, %d fallo(s):" % len(fallos))
        for f in fallos:
            print("   " + f)
        return 1
    print("VERDE DE LA MUTACION: los TRES casos se comportan. El limpio da cero")
    print("filas, el sucio da UNA fila con el nombre que git devuelve, y el")
    print("restaurado vuelve solo a cero. La guarda muerde y se puede apagar.")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutar", action="store_true",
                    help="EL CASO POSITIVO POR MUTACION, sobre un repo fabricado")
    ap.add_argument("--raiz", default=RAIZ,
                    help="raiz sobre la que medir (por defecto, este repo)")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    if a.mutar:
        return prueba_por_mutacion()

    print("=" * 78)
    print("LA GUARDA DEL COMMIT, ANTES DE COMMITEAR NADA DE `dataset/`")
    print("=" * 78)
    ok, _filas = mirar(a.raiz, "EL ARBOL DE TRABAJO DE ESTE REPO, AHORA MISMO")
    print("")
    print("FIN")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
