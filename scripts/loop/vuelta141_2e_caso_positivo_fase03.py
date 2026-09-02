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

LA EXPECTATIVA VIEJA, DE LA VUELTA 141, literal del encargo de entonces: "Tiene
que dar su catalogo con destino cumplido salvo las SEIS remitidas a la fase 06,
que en ese corte todavia no estaban ejecutadas". LAS SEIS NO SE TECLEAN: se leen
de la fila "enrutadas a la fase 06" del docs/plan/00_INDICE.md DE ESE MISMO
COMMIT, con el mismo parser que tallar_estado_de_fase.py ya usa
(leer_remisiones). ESA EXPECTATIVA NO SE BORRA DE AQUI: se sigue midiendo y se
sigue publicando, porque es la que la vuelta 141 paro con su medicion encima y
una correccion que tapa lo que corrige no se puede auditar (EJECUTOR.md 8).

--- LA EXPECTATIVA SE RECOMPUTA (TAREA 2.c, vuelta 143) ---

POR QUE CAMBIA (acta de la vuelta 142, adjudicacion 3.1 y caida 4.5 de la casa;
el auditor se declara autor del defecto en su caida 4.6 de encargo). La
expectativa vieja es INALCANZABLE POR CONSTRUCCION y lo dice la propia doctrina
de la casa: la adjudicacion 3.5 del acta 141 fija que una fusion CONSUMIDA CON
SUPERVIVIENTE DIVERGENTE no puede ser NUNCA cumplida, y la vuelta 140 fija que
SIN VARA ESCRITA tampoco. Con esas dos reglas vigentes, "cumplido igual a
catalogo menos las seis remitidas" pide que dos sacos que la doctrina prohibe
vaciar esten vacios. Medido en la vuelta 141 y otra vez en la 142: sobran
CUATRO, y las cuatro son legitimas (OP-M-02-ADMIT y OP-M-02-MEDIOS divergentes,
OP-U-01 y OP-U-02 sin vara escrita).

LA EXPECTATIVA NUEVA, CON LAS TRES CUENTAS QUE LA VARA SI PUEDE PRODUCIR Y LAS
TRES NOMBRADAS, no solo contadas:

  (A) CUMPLIDO mas CONSUMIDAS CON SUPERVIVIENTE DIVERGENTE mas SIN VARA ESCRITA
      es igual al CATALOGO menos las SEIS REMITIDAS, y no solo en la cifra: la
      UNION DE LOS TRES SACOS tiene que ser exactamente el catalogo menos las
      seis, nombre a nombre, y los tres sacos tienen que ser DISJUNTOS.
  (B) NINGUNA DIVERGENTE SALE CUMPLIDA. El saco de las divergentes se computa
      AQUI, directamente de la ficha y del grafo (superviviente escrito
      deprecado, que resuelve por alias a un vivo que la propia ficha lista en
      `eliminar`) y NO de la razon que la vara imprime: si se leyera de la razon
      de la vara, la comprobacion seria circular y no probaria nada.
  (C) NINGUNA DE LAS SEIS REMITIDAS esta en ninguno de los tres sacos: en ese
      corte no estaban ejecutadas, asi que no pueden salir cumplidas, ni
      divergentes, ni sin vara.

Y SE DECLARA POR QUE HACEN FALTA LAS TRES Y NO SOLO LA (A): la (A) SOLA ES
CIEGA a que una divergente se cuente como cumplida, porque las dos estan dentro
de la misma union y moverla de saco no mueve la union. La (B) es la que muerde
ahi, y es la que la prueba de mutacion de esta tarea rompe a proposito
(scripts/loop/vuelta143_2c_mutacion_positivo.py).

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

    # LA EXPECTATIVA VIEJA SE SIGUE MIDIENDO Y PUBLICANDO, SIN BORRARLA
    # (EJECUTOR.md 8: una correccion que tapa lo que corrige no se puede
    # auditar). Ya NO decide el veredicto: lo decide la nueva, de abajo.
    calza_vieja = (sin_cumplir == esperado)
    print("LA EXPECTATIVA VIEJA (vuelta 141), QUE SE SIGUE MIDIENDO Y NO SE BORRA:")
    print("   esperaba: cumplido %d y sin cumplir exactamente %s"
          % (cifra["catalogo"] - len(esperado), sorted(esperado)))
    print("   salia:    cumplido %d y sin cumplir %s"
          % (cifra["cumplido"], sorted(sin_cumplir)))
    print("   CALZA: %s (de mas: %s)"
          % (calza_vieja, ", ".join(sorted(sin_cumplir - esperado)) or "ninguna"))
    print("")

    calza, codigo = evaluar(lista, cifra, ops, nodos, esperado)
    return codigo


def divergentes_por_ficha(lista, ops, nodos):
    """EL SACO DE LAS DIVERGENTES, COMPUTADO DE LA FICHA Y DEL GRAFO Y NO DE LA
    RAZON QUE LA VARA IMPRIME (TAREA 2.c, vuelta 143). Leerlo de la razon de la
    vara haria la comprobacion (B) circular: la vara se estaria examinando con
    su propia respuesta. El criterio es el de la CORRECCION 16: superviviente
    escrito DEPRECADO que resuelve por alias (P.1) a un vivo que la PROPIA ficha
    lista en `eliminar`."""
    resolver = T.resolver_de(nodos)
    por_id = {o.get("id_op"): o for o in ops}
    salida = []
    for f in lista:
        op = por_id.get(f["id_op"]) or {}
        sup = op.get("superviviente")
        if not sup or not T.PATRON_ID_NODO.match(sup) or sup not in nodos:
            continue
        if T.vivo(nodos.get(sup)):
            continue
        destino = resolver(sup)
        if destino != sup and T.vivo(nodos.get(destino)) \
                and destino in (op.get("eliminar") or []):
            salida.append(f["id_op"])
    return sorted(salida)


def evaluar(lista, cifra, ops, nodos, remitidas):
    """LA EXPECTATIVA RECOMPUTADA (TAREA 2.c, vuelta 143). Devuelve
    (calza, codigo_de_salida). Ver el bloque "LA EXPECTATIVA SE RECOMPUTA" del
    docstring del modulo: (A) los tres sacos NOMBRADOS, disjuntos y su union
    igual al catalogo menos las remitidas; (B) ninguna divergente sale cumplida,
    con el saco de divergentes computado FUERA de la vara; (C) ninguna de las
    remitidas esta en ninguno de los tres sacos."""
    catalogo = {f["id_op"] for f in lista}
    cumplidas = {f["id_op"] for f in lista if f["cumplido"] is True}
    divergentes = set(cifra["nombres_divergentes"])
    sin_vara = set(cifra["nombres_sin_vara"])
    union = cumplidas | divergentes | sin_vara
    esperada = catalogo - set(remitidas)

    print("LA EXPECTATIVA RECOMPUTADA (TAREA 2.c, vuelta 143), CON LAS TRES CUENTAS")
    print("NOMBRADAS Y NO SOLO CONTADAS:")
    print("   catalogo %d | remitidas a la fase de destino %d | catalogo menos remitidas %d"
          % (len(catalogo), len(remitidas), len(esperada)))
    print("   CUMPLIDO (%d): %s" % (len(cumplidas), ", ".join(sorted(cumplidas)) or "ninguna"))
    print("   CONSUMIDAS CON SUPERVIVIENTE DIVERGENTE (%d): %s"
          % (len(divergentes), ", ".join(sorted(divergentes)) or "ninguna"))
    print("   SIN VARA ESCRITA (%d): %s" % (len(sin_vara), ", ".join(sorted(sin_vara)) or "ninguna"))
    print("   SUMA DE LAS TRES: %d + %d + %d = %d | catalogo menos remitidas: %d"
          % (len(cumplidas), len(divergentes), len(sin_vara), len(union), len(esperada)))
    print("")

    fallos = []

    # ---- (A) union exacta y sacos disjuntos -------------------------------
    de_mas = sorted(union - esperada)
    de_menos = sorted(esperada - union)
    if de_mas or de_menos:
        fallos.append("(A) la union de los tres sacos NO es el catalogo menos las remitidas: "
                      "de mas %s; de menos %s"
                      % (", ".join(de_mas) or "ninguna", ", ".join(de_menos) or "ninguna"))
    solapes = []
    for nombre_a, saco_a, nombre_b, saco_b in (
            ("cumplido", cumplidas, "divergentes", divergentes),
            ("cumplido", cumplidas, "sin vara", sin_vara),
            ("divergentes", divergentes, "sin vara", sin_vara)):
        comun = sorted(saco_a & saco_b)
        if comun:
            solapes.append("%s y %s comparten %s" % (nombre_a, nombre_b, ", ".join(comun)))
    if solapes:
        fallos.append("(A) los tres sacos NO son disjuntos: " + "; ".join(solapes))
    print("(A) union exacta: %s | sacos disjuntos: %s"
          % (not (de_mas or de_menos), not solapes))

    # ---- (B) ninguna divergente sale cumplida -----------------------------
    reales = divergentes_por_ficha(lista, ops, nodos)
    mal = sorted(x for x in reales if x in cumplidas)
    if mal:
        fallos.append("(B) sale(n) CUMPLIDA(S) una o mas operaciones cuya ficha las hace "
                      "CONSUMIDAS CON SUPERVIVIENTE DIVERGENTE, y la adjudicacion 3.5 del "
                      "acta 141 dice NUNCA cumplido: %s" % ", ".join(mal))
    faltan_en_saco = sorted(x for x in reales if x not in divergentes)
    if faltan_en_saco:
        fallos.append("(B) la ficha y el grafo hacen DIVERGENTE(S) a %s y la vara no la(s) "
                      "publica en su saco" % ", ".join(faltan_en_saco))
    print("(B) divergentes computadas de la ficha y el grafo (%d): %s"
          % (len(reales), ", ".join(reales) or "ninguna"))
    print("    ninguna de ellas sale cumplida: %s | todas estan en el saco de la vara: %s"
          % (not mal, not faltan_en_saco))

    # ---- (C) ninguna remitida en ninguno de los tres sacos ----------------
    coladas = sorted(x for x in remitidas if x in union)
    if coladas:
        fallos.append("(C) remitida(s) dentro de alguno de los tres sacos, cuando en ese "
                      "corte no estaban ejecutadas: %s" % ", ".join(coladas))
    print("(C) ninguna de las %d remitidas esta en los tres sacos: %s"
          % (len(remitidas), not coladas))
    print("")

    if not fallos:
        print("VEREDICTO (2.e): CALZA. El instrumento tiene su caso positivo verde sobre")
        print("sujeto congelado, y el sujeto es uno donde la vara de grafo SI muerde.")
        return True, 0

    print("POR QUE NO CALZA, MEDIDO Y NO OPINADO (%d fallo(s)):" % len(fallos))
    for f in fallos:
        print("   %s" % f)
    print("")
    print("VEREDICTO (2.e): NO CALZA, SE DICE Y SE PARA ESTE CASO.")
    return False, 2


if __name__ == "__main__":
    raise SystemExit(main())
