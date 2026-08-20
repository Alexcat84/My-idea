# -*- coding: utf-8 -*-
"""vuelta54_41_enlaces.py . LA DERIVACION DE LOS 41 ENLACES, RE-MEDIDA COMMIT A
COMMIT EN LA VUELTA 54.

POR QUE EXISTE: la TAREA 1.4 del encargo de la vuelta 54 manda adosar al
registro del tramo de la vuelta 53 una nota que publica CINCO cifras (41
enlaces, 45 vistas repartidas en 13, 9 y 23, y CUATRO instancias retiradas con
su nombre). La regla 2 del EJECUTOR dice que toda cifra o nombre propio que se
publique se lee de la salida del instrumento corrido EN ESTA VUELTA, y que un
acta previa NUNCA es fuente de una cifra nueva: se cita como contraste. El acta
de la vuelta 53 (seccion 3, punto 2) ya derivo estas cifras; este instrumento
las vuelve a medir por su cuenta contra git para que la nota no dependa del
acta.

QUE MIDE, de solo lectura y sin tocar el arbol de trabajo (todo por git show):

  1. LOS ENLACES en cada uno de los SEIS commits que van del cierre de la
     vuelta 52 al cierre de la 53, con la MISMA vara que scripts/loop/
     vuelta31_estado.py: suma de nodos_previos mas nodos_siguientes sobre
     TODOS los ficheros de dataset/nodos, deprecados incluidos.
  2. LAS VISTAS que la simetrizacion del paso 5 de run_phase1.py completo en
     cada lote, leidas del symmetrize_added horneado en
     dataset/metadata/phase1_run_log.json de cada commit.
  3. LAS CUATRO INSTANCIAS RETIRADAS que el acta nombra: si estaban ANTES del
     lote y si NO estan DESPUES, campo a campo.

Uso: python scripts/loop/vuelta54_41_enlaces.py
"""
import io
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Los tres separadores se construyen con chr() y no con escapes: este fichero
# se genero desde un heredoc y los escapes se colapsaban al escribirlo.
_TAB = chr(9)
_NL = chr(10)
_NLB = bytes([10])

# Los seis commits, del cierre de la vuelta 52 al cierre de la 53. LOS HASHES
# SE LEEN DEL REPORTE DE LA VUELTA 53 (su cabecera los publica) y se VERIFICAN
# aqui contra git: si alguno no existe, el instrumento cae.
COMMITS = [
    ("d88c42bb", "cierre de la vuelta 52 (acta del auditor)"),
    ("49ae6eef", "vuelta 53, TAREA 1"),
    ("cadc9977", "vuelta 53, LOTE A"),
    ("04bd56de", "vuelta 53, LOTE B"),
    ("90bb930c", "vuelta 53, LOTE C"),
    ("be5d152b", "vuelta 53, el cierre"),
]

# Las CUATRO instancias que el acta 53 nombra como retiradas por la redireccion
# de la fusion: (nodo, campo, destino, lote, especie).
# Las CUATRO instancias que el acta 53 nombra como retiradas por la redireccion
# de la fusion. Cada una es UNA instancia dentro de UN campo de UN nodo, y lo
# que se mide es si el ID ABSORBIDO estaba en ese campo ANTES del lote y ya no
# esta DESPUES:
#   (nodo, campo, id absorbido que desaparece, superviviente al que redirige,
#    commit del lote, especie)
# EN LA AUTO-ARISTA el superviviente ES EL PROPIO NODO, y por eso la instancia
# no se puede reescribir: se retira. EN EL COLAPSO el superviviente YA ESTABA
# en el campo, y por eso las dos instancias colapsan en una.
RETIROS = [
    ("warrant_pricing_venture_debt", "nodos_previos", "warrants_deuda_convertible",
     "warrant_pricing_venture_debt", "cadc9977", "AUTO-ARISTA"),
    ("criterios_seleccion_proyectos_calidad", "nodos_previos", "proceso_nominacion_seleccion",
     "criterios_seleccion_proyectos_calidad", "90bb930c", "AUTO-ARISTA"),
    ("elaboracion_fdd", "nodos_previos", "contratar_abogado_especializado_franquicias",
     "eleccion_abogado_franquicias", "04bd56de", "COLAPSO DE DUPLICADA"),
    ("sistema_estable_causas_comunes", "nodos_siguientes", "critica_gestion_por_objetivos",
     "eliminar_metas_numericas_gerencia", "04bd56de", "COLAPSO DE DUPLICADA"),
]

# Los tres lotes que mueven nodos, con el commit anterior a cada uno.
LOTES = [("cadc9977", "49ae6eef", "LOTE A"), ("04bd56de", "cadc9977", "LOTE B"),
         ("90bb930c", "04bd56de", "LOTE C")]

ANTERIOR = {"cadc9977": "49ae6eef", "04bd56de": "cadc9977", "90bb930c": "04bd56de"}


def git(*args):
    return subprocess.run(["git"] + list(args), cwd=RAIZ, capture_output=True)


def ficheros_de(commit):
    r = git("ls-tree", "-r", "--name-only", commit, "dataset/nodos/")
    if r.returncode != 0:
        raise SystemExit("ROJO: no puedo listar dataset/nodos en %s" % commit)
    return [x for x in r.stdout.decode("utf-8").splitlines() if x.endswith(".json")]


def enlaces_de(commit):
    """LOS ENLACES DE UN COMMIT ENTERO, en UNA sola pasada de git cat-file.

    La primera version de este instrumento llamaba a git show una vez POR
    FICHERO (3.853 por commit, seis commits): 23.000 procesos y no termino en
    dos minutos. Se declara el cambio y el motivo, que es lo que la regla 2
    pide de un instrumento que se toca: la VARA NO CAMBIA (sigue sumando
    nodos_previos mas nodos_siguientes sobre TODOS los ficheros de
    dataset/nodos, deprecados incluidos), cambia como se leen los blobs.
    """
    r = git("ls-tree", "-r", commit, "dataset/nodos/")
    if r.returncode != 0:
        raise SystemExit("ROJO: no puedo listar dataset/nodos en %s" % commit)
    hashes = []
    for linea in r.stdout.decode("utf-8").splitlines():
        if not linea.strip():
            continue
        meta, nombre = linea.split(_TAB, 1)
        if not nombre.endswith(".json"):
            continue
        hashes.append(meta.split()[2])
    p = subprocess.run(["git", "cat-file", "--batch"], cwd=RAIZ,
                       input=(_NL.join(hashes) + _NL).encode("ascii"),
                       capture_output=True)
    if p.returncode != 0:
        raise SystemExit("ROJO: cat-file fallo en %s" % commit)
    buf = p.stdout
    total = 0
    ficheros = 0
    i = 0
    while i < len(buf):
        j = buf.index(_NLB, i)
        cab = buf[i:j].decode("ascii").split()
        tam = int(cab[2])
        cuerpo = buf[j + 1:j + 1 + tam]
        i = j + 1 + tam + 1
        o = json.loads(cuerpo.decode("utf-8"))
        total += len(o.get("nodos_previos") or [])
        total += len(o.get("nodos_siguientes") or [])
        ficheros += 1
    return total, ficheros


def nodo_en(commit, ruta):
    r = git("show", "%s:%s" % (commit, ruta))
    if r.returncode != 0:
        return None
    return json.loads(r.stdout.decode("utf-8"))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("LOS 41 ENLACES, RE-MEDIDOS COMMIT A COMMIT (vuelta 54, TAREA 1.4)")
    print("=" * 78)
    print()

    print("--- 1. LOS ENLACES EN LOS SEIS COMMITS (vara de vuelta31_estado.py) ---")
    print()
    print("  %-10s %-42s %8s %8s" % ("commit", "que es", "enlaces", "delta"))
    previo = None
    enlaces = {}
    for h, que in COMMITS:
        total, ficheros = enlaces_de(h)
        enlaces[h] = total
        d = "" if previo is None else "%+d" % (total - previo)
        print("  %-10s %-42s %8d %8s   (ficheros: %d)" % (h, que, total, d, ficheros))
        previo = total
    print()
    gan = enlaces[COMMITS[-1][0]] - enlaces[COMMITS[0][0]]
    print("  LO QUE EL GRAFO GANA EN LA VUELTA 53: %+d enlaces" % gan)
    print()

    print("--- 2. LAS VISTAS DE LA SIMETRIZACION, del phase1_run_log de cada commit ---")
    print()
    suma = 0
    for h, que in COMMITS:
        r = git("show", "%s:dataset/metadata/phase1_run_log.json" % h)
        if r.returncode != 0:
            print("  %-10s (sin log)" % h)
            continue
        log = json.loads(r.stdout.decode("utf-8"))
        add = log.get("symmetrize_added")
        n = len(add) if isinstance(add, list) else (add or 0)
        if h != COMMITS[0][0]:
            suma += n
        print("  %-10s %-42s vistas anadidas: %d" % (h, que, n))
    print()
    print("  SUMA DE VISTAS DE LOS CINCO COMMITS DE LA VUELTA 53: %d" % suma)
    print()

    print("--- 3. LAS CUATRO INSTANCIAS RETIRADAS, una a una ---")
    print()
    retiradas = 0
    por_lote = {}
    for nodo, campo, absorbido, superviviente, commit, especie in RETIROS:
        antes = nodo_en(ANTERIOR[commit], "dataset/nodos/%s.json" % nodo)
        despues = nodo_en(commit, "dataset/nodos/%s.json" % nodo)
        la = (antes or {}).get(campo) or []
        ld = (despues or {}).get(campo) or []
        estaba = absorbido in la
        sigue = absorbido in ld
        sup_antes = superviviente in la
        sup_despues = superviviente in ld
        ok = estaba and not sigue
        print("  %s.%s (%s, %s)" % (nodo, campo, especie, commit))
        print("     el ABSORBIDO %s estaba ANTES: %s | esta DESPUES: %s"
              % (absorbido, estaba, sigue))
        print("     el SUPERVIVIENTE %s estaba ANTES: %s | esta DESPUES: %s"
              % (superviviente, sup_antes, sup_despues))
        print("     instancia RETIRADA: %s" % ("SI" if ok else "NO"))
        if ok:
            retiradas += 1
            por_lote[commit] = por_lote.get(commit, 0) + 1
        print()
    print("  INSTANCIAS RETIRADAS, contadas una a una: %d" % retiradas)
    print()

    print("--- 4. LA CUENTA POR LOTE: vistas menos retiros contra el delta medido ---")
    print()
    print("  %-10s %-8s %8s %8s %10s %8s" % ("commit", "lote", "vistas", "retiros",
                                             "esperado", "medido"))
    calzan = 0
    for commit, previo_h, nombre in LOTES:
        r = git("show", "%s:dataset/metadata/phase1_run_log.json" % commit)
        log = json.loads(r.stdout.decode("utf-8"))
        add = log.get("symmetrize_added")
        v = len(add) if isinstance(add, list) else (add or 0)
        ret = por_lote.get(commit, 0)
        medido = enlaces[commit] - enlaces[previo_h]
        print("  %-10s %-8s %8d %8d %10s %8s   %s"
              % (commit, nombre, v, ret, "%+d" % (v - ret), "%+d" % medido,
                 "CALZA" if v - ret == medido else "NO CALZA"))
        if v - ret == medido:
            calzan += 1
    print()
    print("  LOTES QUE CALZAN: %d de %d" % (calzan, len(LOTES)))
    print()

    print("--- LA RESTA ---")
    print("  vistas completadas por la simetrizacion : %d" % suma)
    print("  instancias retiradas por la redireccion : %d" % retiradas)
    print("  %d menos %d son %d" % (suma, retiradas, suma - retiradas))
    print("  ganancia MEDIDA de enlaces en la vuelta 53: %+d" % gan)
    print("  CALZA: %s" % ("SI" if suma - retiradas == gan else "NO"))
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
