# -*- coding: utf-8 -*-
r"""vuelta141_2e_caso_positivo_fase03.py . EL CASO POSITIVO DE
tallar_estado_de_fase.py SOBRE SUJETO CONGELADO, ESTA VEZ SOBRE UN SUJETO QUE
LA VARA SI PUEDE MEDIR (TAREA 2.e de la vuelta 141).

POR QUE NACE. El acta de la vuelta 140 declara como caida propia del auditor
(4.5, DE ENCARGO) haber elegido mal el sujeto congelado del caso positivo de la
vuelta 140: mando la FASE 05, y nueve de sus diez operaciones son de tipos que
el grafo no puede medir, asi que la expectativa era inalcanzable por
construccion. El sujeto de repuesto que el encargo de la vuelta 141 fija es LA
FASE 03 EN SU COMMIT DE CIERRE, "cuyo catalogo son fusiones con superviviente,
o sea donde la vara de grafo SI muerde".

EL SUJETO, CLAVADO POR COMMIT Y COTEJADO POR sha256 (banco 9.10, y es la misma
figura que el caso (iii) de vuelta140_2a_mutaciones.py con e4464be5): el commit
del cierre de la fase 03 es 62d4f28e, "Decision del fundador: la fase 03 cierra
con remision y el tramo mecanico abre con la pareja nueva", del 26 ago 2026,
asunto LEIDO DE git log en esta vuelta y no tecleado de memoria. Los CUATRO
blobs que el instrumento lee se cotejan en cada corrida: si el ancla se mueve,
el caso cae con ANCLA PERDIDA y no con un verde.

LA EXPECTATIVA DEL ENCARGO, literal: "Tiene que dar su catalogo con destino
cumplido salvo las SEIS remitidas a la fase 06, que en ese corte todavia no
estaban ejecutadas". LAS SEIS NO SE TECLEAN: se leen de la fila "enrutadas a la
fase 06" del docs/plan/00_INDICE.md DE ESE MISMO COMMIT, con el mismo parser que
tallar_estado_de_fase.py ya usa (leer_remisiones).

Y SI NO CALZA, SE DICE Y SE PARA ESE CASO, que es lo que el encargo manda con
esas palabras: no se ajusta la expectativa para que salga verde.

USO:
  python scripts/loop/vuelta141_2e_caso_positivo_fase03.py
"""
import hashlib
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tallar_estado_de_fase as T

RAIZ = T.RAIZ
COMMIT_CONGELADO = "62d4f28e"
FASE = "03_FUSIONES"
FASE_DESTINO_DE_LA_REMISION = "06_MESAS"

# Los sha256 de los CUATRO blobs que el instrumento lee en ese commit. Se
# calcularon corriendo `git show <commit>:<ruta>` en la vuelta 141 y se pegan
# aqui para que el ancla no se pueda mover en silencio.
SHA256_ESPERADOS = {
    "dataset/metadata/master_graph.json":
        "b476d05ac230b42ae52854b3d1b5b4af06e56eb49279bf1155d62c31284436a3",
    "docs/plan/OPERACIONES.jsonl":
        "7ea9c1dae46c155a752b09de55ccb6034043ce4d327335c97e42c693e91cb970",
    "docs/plan/00_INDICE.md":
        "9ef27456a73d39fb46e4558c31dda2c744d8c1fff9daefa6c3afbae72346a2f6",
    "docs/plan/04_ENLACES.md":
        "2276d91a46a086a2060b51951d7d2ebe37432e373c0f4285025387ef3471e2ed",
}


def sha256_del_blob(ref, rel):
    r = subprocess.run(["git", "show", "%s:%s" % (ref, rel)], cwd=RAIZ, capture_output=True)
    if r.returncode != 0:
        return None
    return hashlib.sha256(r.stdout).hexdigest()


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("TAREA 2.e: CASO POSITIVO SOBRE SUJETO CONGELADO, LA FASE %s" % FASE)
    print("=" * 78)

    # LA IDENTIDAD SE LEE DE GIT (EJECUTOR.md regla 1).
    r = subprocess.run(["git", "log", "-1", "--format=%H\x01%ad\x01%s", "--date=short",
                        COMMIT_CONGELADO], cwd=RAIZ, capture_output=True, text=True)
    if r.returncode != 0 or "\x01" not in r.stdout:
        print("ANCLA PERDIDA: git no conoce el commit %s." % COMMIT_CONGELADO)
        return 1
    h, fecha, asunto = r.stdout.strip().split("\x01", 2)
    print("SUJETO CLAVADO POR COMMIT: %s" % h)
    print("   fecha (de git): %s" % fecha)
    print("   asunto (de git): %s" % asunto)
    print("")

    print("LOS CUATRO BLOBS QUE EL INSTRUMENTO LEE, CON SU sha256 DE HOY:")
    faltan = []
    for rel in sorted(SHA256_ESPERADOS):
        sha = sha256_del_blob(COMMIT_CONGELADO, rel)
        if sha is None:
            faltan.append(rel)
            print("   %-40s NO SE PUDO LEER" % rel)
            continue
        esperado = SHA256_ESPERADOS[rel]
        marca = "OK" if (esperado is None or esperado == sha) else "DISTINTO DEL ESPERADO"
        print("   %-40s %s  %s" % (rel, sha[:16], marca))
        if esperado is not None and esperado != sha:
            faltan.append(rel)
    if faltan:
        print("")
        print("ANCLA PERDIDA: %d blob(s) no calzan. El caso NO se corre." % len(faltan))
        return 1
    print("")

    ops = T.cargar_ops(COMMIT_CONGELADO)
    nodos = T.cargar_grafo(COMMIT_CONGELADO)
    lista, cifra, fallos = T.medir(FASE, ops, nodos, ref=COMMIT_CONGELADO)
    T.imprimir(FASE, lista, cifra, fallos, ref=COMMIT_CONGELADO)
    print("")

    # LAS SEIS REMITIDAS NO SE TECLEAN: salen de la fila "enrutadas a la fase 06"
    # del 00_INDICE de ESE MISMO COMMIT, con el parser de la casa.
    remitidas_a_06 = sorted(T.leer_remisiones(FASE_DESTINO_DE_LA_REMISION, COMMIT_CONGELADO))
    en_catalogo = {f["id_op"] for f in lista}
    remitidas_del_catalogo = sorted(x for x in remitidas_a_06 if x in en_catalogo)
    print("LAS REMITIDAS A LA FASE %s, LEIDAS DEL 00_INDICE DE %s (no tecleadas): %d"
          % (FASE_DESTINO_DE_LA_REMISION, COMMIT_CONGELADO, len(remitidas_a_06)))
    print("   %s" % ", ".join(remitidas_a_06))
    print("   de esas, en el catalogo de la fase %s: %d (%s)"
          % (FASE, len(remitidas_del_catalogo), ", ".join(remitidas_del_catalogo)))
    print("")

    sin_cumplir = set(cifra["nombres_sin_cumplir"])
    esperado = set(remitidas_del_catalogo)
    print("LO QUE EL ENCARGO ESPERA: catalogo %d con destino cumplido SALVO las %d "
          "remitidas, o sea cumplido %d y sin cumplir exactamente %s"
          % (cifra["catalogo"], len(esperado), cifra["catalogo"] - len(esperado),
             sorted(esperado)))
    print("LO QUE SALE:              cumplido %d y sin cumplir %s"
          % (cifra["cumplido"], sorted(sin_cumplir)))
    calza = (sin_cumplir == esperado)
    print("CALZA CON LO ESPERADO: %s" % calza)
    print("")

    if calza:
        print("VEREDICTO (2.e): CALZA. El instrumento tiene su caso positivo verde sobre")
        print("sujeto congelado, y el sujeto es uno donde la vara de grafo SI muerde.")
        return 0

    de_mas = sorted(sin_cumplir - esperado)
    de_menos = sorted(esperado - sin_cumplir)
    print("POR QUE NO CALZA, MEDIDO Y NO OPINADO:")
    print("   SIN CUMPLIR DE MAS (%d): %s" % (len(de_mas), ", ".join(de_mas) or "ninguna"))
    print("   SIN CUMPLIR DE MENOS (%d): %s" % (len(de_menos), ", ".join(de_menos) or "ninguna"))
    print("")
    resolver = T.resolver_de(nodos)
    por_id = {o.get("id_op"): o for o in ops}
    for x in de_mas:
        op = por_id.get(x) or {}
        fila = [f for f in lista if f["id_op"] == x][0]
        sup = op.get("superviviente")
        print("   %s | vara %s | tipo %s" % (x, fila["vara"], op.get("tipo")))
        print("      superviviente escrito en la ficha: %r" % sup)
        if sup:
            n = nodos.get(sup)
            print("      ese id: existe=%s | deprecado=%s | RESUELVE POR ALIAS A %r"
                  % (n is not None, (n or {}).get("deprecado"), resolver(sup)))
        print("      razon del instrumento: %s" % fila["razon"][:200])
    print("")
    print("VEREDICTO (2.e): NO CALZA, SE DICE Y SE PARA ESTE CASO.")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
