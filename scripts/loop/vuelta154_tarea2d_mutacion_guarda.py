# -*- coding: utf-8 -*-
"""vuelta154_tarea2d_mutacion_guarda.py . TAREA 2.d DE LA VUELTA 154.

EL CASO POSITIVO POR MUTACION DE LA GUARDA ENSANCHADA DE `OP-C-05`, Y MUERDE
POR EL LADO QUE HASTA HOY ERA CIEGO.

LO QUE EL ENCARGO PIDE, LITERAL: "una arista bidireccional metida SOLO por
`nodos_previos` de un nodo vivo tiene que TUMBAR Gate 0 nombrando el par. Sobre
copia, con dataset/ identico antes y despues comprobado por sha256. Y
CONTRAPRUEBA OBLIGATORIA: la guarda VIEJA sobre esa misma mutacion tiene que
salir VERDE. Si sale roja, tu mutacion no ataca el punto ciego y no prueba
nada."

--- POR QUE LA MUTACION INGENUA NO SIRVE, Y SE DICE EN VEZ DE CALLARSE ---

La primera forma que se piensa (meter el id CRUDO de un nodo vivo B en
`A.nodos_previos`) NO ATACA NADA, y el motivo esta medido en este mismo fichero,
`step5_symmetrize`: el PASO 5 de `run_phase1` COMPLETA las aristas crudas ANTES
de que Gate 0 corra. Metida asi, la vuelta aparece sola en `B.nodos_siguientes`
y entonces LA GUARDA VIEJA TAMBIEN LA VE. La contraprueba saldria roja y la
mutacion no probaria nada, que es exactamente lo que el encargo advierte.

--- DONDE VIVE DE VERDAD EL PUNTO CIEGO ---

La simetrizacion trabaja con IDS CRUDOS; la guarda trabaja con IDS RESUELTOS.
Ese desfase es el agujero, y es el que produjo el par real
(`metodologia_6s` <-> `error_proofing_servicio`): `metodologia_6s` nombra dos
ids DEPRECADOS que resuelven al mismo nodo vivo, uno en cada lista. El paso 5
mira los ids crudos y escribe la vista reciproca DENTRO DEL NODO DEPRECADO, que
no es el vivo, asi que la direccion resuelta de vuelta NUNCA aparece en
`nodos_siguientes` de ningun vivo. La guarda vieja no podia verla.

LA MUTACION REPRODUCE ESA FORMA, no otra: a un nodo vivo `A` se le mete, EN SUS
DOS LISTAS, un id DEPRECADO que resuelve a otro nodo vivo `B`. Tras resolver
quedan las dos direcciones A hacia B y B hacia A, o sea un par bidireccional
entre vivos SIN CITA; y como el paso 5 solo toca el nodo deprecado, la lista
`nodos_siguientes` de `B` sigue sin nombrar a `A` y la guarda vieja sigue ciega.

--- TODO SOBRE VARIABLE COMPUTADA (EJECUTOR.md 1) ---

Ni `A`, ni `B`, ni el alias se teclean: los tres se ELIGEN POR COMPUTO sobre el
arbol de hoy, con la primera pareja que cumple las condiciones en orden
alfabetico, y el par que se espera ver nombrado se compone de esas variables y
se busca DESPUES en la salida real de Gate 0. No hay un literal comparandose
consigo mismo.

--- LOS TRES CASOS ---

  (A) MUTACION contra la guarda NUEVA  ->  se espera ROJO nombrando el par
  (B) MUTACION contra la guarda VIEJA  ->  se espera VERDE (contraprueba)
  (C) ARBOL INTACTO contra la NUEVA    ->  se espera VERDE

La guarda VIEJA no se reimplementa aqui: se saca LITERAL de git a un fichero
temporal dentro de `scripts/`, para que su `BASE` resuelva al mismo repo, y se
borra al final. Una copia a mano de la vara vieja no probaria nada sobre la vara
vieja.

Y SE SACA DE UNA REFERENCIA FIJA, NO DE `HEAD`: el HEAD DE APERTURA de la
vuelta, leido de `docs/loop/SALIDA_V154_HEAD_APERTURA.txt`. Ver la correccion
declarada en el CASO B: con `HEAD` este arnes daba verde mientras el ensanche no
estaba commiteado y rojo en cuanto lo estuvo, porque `HEAD` habia pasado a ser
la guarda NUEVA. Una contraprueba anclada a una referencia movil es un falso
verde esperando su dia.

CADA CASO PARTE DE ARBOL LIMPIO Y VUELVE A ARBOL LIMPIO: la mutacion se rehace
entera para el caso B, porque la corrida del caso A deja el arbol simetrizado y
reutilizarlo mediria otra cosa.

DATASET/ INTACTO, COMPROBADO Y NO PROMETIDO: sha256 de `dataset/` entero antes y
despues, y todo lo tocado se restaura en un `finally`.

USO:  python scripts/loop/vuelta154_tarea2d_mutacion_guarda.py
"""
import glob
import hashlib
import io
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
VIEJA = os.path.join(RAIZ, "scripts", "_v154_guarda_vieja_run_phase1.py")


def huella_dataset():
    h = hashlib.sha256()
    base = os.path.join(RAIZ, "dataset")
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames.sort()
        for n in sorted(filenames):
            ruta = os.path.join(dirpath, n)
            h.update(os.path.relpath(ruta, base).replace("\\", "/").encode())
            with open(ruta, "rb") as fh:
                for trozo in iter(lambda: fh.read(1 << 20), b""):
                    h.update(trozo)
    return h.hexdigest()


def restaurar():
    subprocess.run(["git", "checkout", "--", "dataset", "web/lib/assets"],
                   cwd=RAIZ, capture_output=True)


def ciclo(script):
    """EL CICLO ENTERO, NUNCA run_phase1 SUELTO (leccion de la vuelta 152: run_phase1
    suelto deja la copia web desincronizada y la corrida siguiente sale roja por
    CICLO SIN CERRAR, no por la guarda)."""
    r = subprocess.run([sys.executable, script, "--reaplico-curaduria"],
                       capture_output=True, cwd=RAIZ)
    salida = r.stdout.decode("utf-8", "replace") + r.stderr.decode("utf-8", "replace")
    for extra, args in (("etiquetas_de_cara.py", ["--aplicar"]), ("sync_assets_web.py", [])):
        subprocess.run([sys.executable, os.path.join("scripts", extra)] + args,
                       capture_output=True, cwd=RAIZ)
    lineas = [x.strip() for x in salida.splitlines() if "REGISTRADO CON CITA" in x]
    return r.returncode, (lineas[0] if lineas else "(la guarda no aparece en la salida)")


def cargar_nodos():
    todos = {}
    for ruta in sorted(glob.glob(os.path.join(NODOS, "*.json"))):
        d = json.load(io.open(ruta, encoding="utf-8"))
        todos[d.get("node_id") or os.path.splitext(os.path.basename(ruta))[0]] = d
    return todos


def elegir_por_computo():
    """Elige A (vivo), B (vivo) y ALIAS (deprecado que resuelve a B), con A y B
    SIN ninguna relacion resuelta hoy en ninguna de las dos listas. Todo por
    computo y en orden alfabetico: el primero que cumple."""
    todos = cargar_nodos()
    alias_de = {}
    for nid, n in todos.items():
        for a in n.get("ids_alias") or []:
            if a != nid:
                alias_de[a] = nid

    def resolver(nid):
        n = todos.get(nid)
        if n is not None and not n.get("deprecado"):
            return nid
        visto, cur = {nid}, nid
        ultimo = nid if n is not None else None
        while cur in alias_de:
            cur = alias_de[cur]
            if cur in visto:
                break
            visto.add(cur)
            c = todos.get(cur)
            if c is None:
                continue
            ultimo = cur
            if not c.get("deprecado"):
                return cur
        return ultimo

    vivos = {n for n in todos if not todos[n].get("deprecado")}
    # alias DEPRECADOS que resuelven a un vivo, agrupados por su destino vivo
    por_destino = {}
    for a in sorted(alias_de):
        if a in todos and todos[a].get("deprecado"):
            d = resolver(a)
            if d in vivos:
                por_destino.setdefault(d, []).append(a)

    def vecinos_resueltos(nid):
        s = set()
        for campo in ("nodos_siguientes", "nodos_previos"):
            for dest in todos[nid].get(campo) or []:
                if dest in todos:
                    s.add(resolver(dest))
        return s

    for A in sorted(vivos):
        va = vecinos_resueltos(A)
        for B in sorted(por_destino):
            if B == A or B in va:
                continue
            if A in vecinos_resueltos(B):
                continue
            return A, B, por_destino[B][0]
    return None, None, None


def mutar(A, alias):
    ruta = os.path.join(NODOS, A + ".json")
    d = json.load(io.open(ruta, encoding="utf-8"))
    d["nodos_siguientes"] = list(d.get("nodos_siguientes") or []) + [alias]
    d["nodos_previos"] = list(d.get("nodos_previos") or []) + [alias]
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(d, ensure_ascii=False, indent=2) + "\n")


def main():
    print("=" * 96)
    print("VUELTA 154, TAREA 2.d: EL CASO POSITIVO POR MUTACION DE LA GUARDA ENSANCHADA")
    print("=" * 96)

    restaurar()
    ciclo(os.path.join("scripts", "run_phase1.py"))
    ANTES = huella_dataset()
    print("sha256 de dataset/ ANTES (arbol normalizado): %s" % ANTES)
    print("")

    A, B, ALIAS = elegir_por_computo()
    assert A and B and ALIAS, "no se hallo pareja por computo"
    par_esperado = " <-> ".join(sorted([A, B]))
    print("ELEGIDOS POR COMPUTO (no tecleados):")
    print("  A     (vivo, el que se muta) : %s" % A)
    print("  B     (vivo, el destino)     : %s" % B)
    print("  ALIAS (deprecado que resuelve a B, se mete en LAS DOS listas de A): %s" % ALIAS)
    print("  par que se espera ver nombrado: %s" % par_esperado)
    print("")

    resultados = []
    try:
        # --- CASO A: mutacion contra la guarda NUEVA ---
        mutar(A, ALIAS)
        rc, linea = ciclo(os.path.join("scripts", "run_phase1.py"))
        nombra = par_esperado in linea or (A in linea and B in linea)
        resultados.append(("A", "MUTACION contra la guarda NUEVA", "ROJO nombrando el par",
                           rc, linea, nombra))
        restaurar()

        # --- CASO B: LA MISMA mutacion contra la guarda VIEJA (contraprueba) ---
        #
        # CORRECCION DECLARADA (vuelta 154, hallada al RE CORRER este arnes
        # despues de commitear la TAREA 2). LA REFERENCIA ERA MOVIL, Y ESO ES UN
        # FALSO VERDE ESPERANDO SU DIA: aqui ponia `git show
        # HEAD:scripts/run_phase1.py`, y `HEAD` avanza. Mientras el ensanche no
        # estaba commiteado, `HEAD` traia la guarda VIEJA y el caso B salia
        # verde; en cuanto la TAREA 2 se commiteo, `HEAD` PASO A SER LA GUARDA
        # NUEVA y el caso B se cayo publicando 155 pares y 1 sin cita, que es la
        # guarda nueva hablando y no la vieja. El arnes lo canto en ROJO, que es
        # exactamente lo que tenia que hacer.
        #
        # LA VARA PASA A SER EL HEAD DE APERTURA DE LA VUELTA, leido del sello
        # que la propia apertura dejo y NO tecleado: ese commit es, por
        # construccion, anterior a toda operacion de esta vuelta, asi que su
        # `run_phase1.py` es la guarda vieja pase lo que pase con `HEAD`.
        with io.open(os.path.join(RAIZ, "docs", "loop",
                                  "SALIDA_V154_HEAD_APERTURA.txt"), encoding="utf-8") as fh:
            ref_vieja = fh.read().strip()
        print("LA GUARDA VIEJA SE SACA DE %s, el HEAD DE APERTURA leido de su sello,"
              % ref_vieja[:8])
        print("y NO de HEAD: HEAD es una referencia MOVIL y ya no trae la vara vieja.")
        print("")
        with io.open(VIEJA, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(subprocess.run(["git", "show", "%s:scripts/run_phase1.py" % ref_vieja],
                                    cwd=RAIZ, capture_output=True).stdout.decode("utf-8", "replace"))
        mutar(A, ALIAS)
        rc2, linea2 = ciclo(os.path.join("scripts", "_v154_guarda_vieja_run_phase1.py"))
        resultados.append(("B", "LA MISMA mutacion contra la guarda VIEJA", "VERDE (contraprueba)",
                           rc2, linea2, None))
        restaurar()

        # --- CASO C: arbol intacto contra la guarda NUEVA ---
        rc3, linea3 = ciclo(os.path.join("scripts", "run_phase1.py"))
        resultados.append(("C", "ARBOL INTACTO contra la guarda NUEVA", "VERDE",
                           rc3, linea3, None))
    finally:
        restaurar()
        if os.path.exists(VIEJA):
            os.remove(VIEJA)
        ciclo(os.path.join("scripts", "run_phase1.py"))

    DESPUES = huella_dataset()
    print("| caso | que se prueba | esperado | exit | la linea de la guarda, literal |")
    print("|---|---|---|---:|---|")
    for c, que, esp, rc, linea, _n in resultados:
        print("| %s | %s | %s | %d | %s |" % (c, que, esp, rc, linea))
    print("")

    for c, que, esp, rc, linea, nombra in resultados:
        print("CASO %s (%s)" % (c, que))
        print("  esperado: %s | exit real: %d" % (esp, rc))
        print("  linea de la guarda: %s" % linea)
        if nombra is not None:
            print("  nombra el par %s: %s" % (par_esperado, "SI" if nombra else "NO"))
        print("")

    a_rc, a_linea, a_nombra = resultados[0][3], resultados[0][4], resultados[0][5]
    b_rc, b_linea = resultados[1][3], resultados[1][4]
    c_rc, c_linea = resultados[2][3], resultados[2][4]

    ok_a = a_rc != 0 and "SIN CITA" in a_linea and a_nombra
    ok_b = b_rc == 0 and "0 SIN CITA" in b_linea
    ok_c = c_rc == 0 and "0 SIN CITA" in c_linea

    print("=" * 96)
    print("VEREDICTOS")
    print("  CASO A, la guarda NUEVA MUERDE por el lado ciego y nombra el par: %s"
          % ("SI" if ok_a else "NO"))
    print("  CASO B, la guarda VIEJA sale VERDE sobre la MISMA mutacion (la mutacion")
    print("          ataca el punto ciego de verdad): %s" % ("SI" if ok_b else "NO"))
    print("  CASO C, la guarda NUEVA sale VERDE sobre el arbol intacto: %s"
          % ("SI" if ok_c else "NO"))
    print("")
    print("sha256 de dataset/ DESPUES: %s" % DESPUES)
    print("dataset/ IDENTICO antes y despues: %s" % (ANTES == DESPUES))
    print("")
    # LAS LINEAS `CIFRA` DE LOS PARES (vuelta 154, TAREA 7.b; adjudicacion 6.8):
    # las cifras de la tabla de arriba viven dentro de la linea literal de la
    # guarda y la convencion generica de recuento no sabe sacarlas de ahi. Se
    # publican aparte, extraidas de esa misma linea por expresion regular.
    import re as _re
    for c, _q, _e, _rc, linea, _n in resultados:
        m = _re.search(r"(\d+) par\(es\) bidireccional\(es\) tras resolver, "
                       r"(\d+) con cita, (\d+) SIN CITA", linea)
        if m:
            # UNA ETIQUETA POR CASO Y CON UNA PALABRA UNICA CADA UNA (mutada,
            # vieja, intacta): si dos etiquetas de la misma unidad comparten
            # todas sus palabras, la guarda de cifras no puede saber contra cual
            # cotejar y lo dice en rojo, con razon.
            _mote = {"A": "mutada", "B": "vieja", "C": "intacta"}[c]
            print("CIFRA pares que ve la guarda %s en el caso %s: %s pares"
                  % (_mote, c, m.group(1)))
    print("CIFRA casos de mutacion corridos: %d comprobaciones" % len(resultados))
    print("CIFRA casos de mutacion que salen como se esperaba: %d comprobaciones"
          % sum([ok_a, ok_b, ok_c]))
    print("CIFRA ficheros de dataset movidos por esta prueba: %d ficheros"
          % (0 if ANTES == DESPUES else 1))

    assert ANTES == DESPUES, "dataset/ se movio y no debia"
    assert ok_a, "la guarda nueva NO muerde por el lado ciego"
    assert ok_b, "la guarda VIEJA sale roja: la mutacion no ataca el punto ciego"
    assert ok_c, "la guarda nueva no sale verde sobre el arbol intacto"
    print("")
    print("LOS TRES CASOS SALEN COMO SE ESPERABA.")


main()
