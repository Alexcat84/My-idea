# -*- coding: utf-8 -*-
r"""verificar_titulos_normalizados.py . LA GUARDA DEL PUNTO CIEGO DE TITULOS
(TAREA 1.g de la vuelta 124, acta de la vuelta 123 seccion 3.4).

POR QUE NACE. La celda "duplicadas de titulo 0" que la cabecera del cribado
publica en sus dos columnas sale de `find_exact_title_duplicates`
(`scripts/run_phase1.py:671`), que agrupa por `titulo_concepto` CRUDO, sin
normalizar. `find_near_duplicate_titles` (linea 689) SI normaliza, pero
EXCLUYE a proposito los pares cuyo titulo normalizado es IGUAL (linea 700,
`ta == tb: continue`), porque nacio para candidatos de fusion SEMANTICA, no
para detectar el MISMO titulo escrito con distinta mayuscula o acento. Un
par que solo difiere en eso se cae por las dos rendijas y la cabecera lo
publica como si no existiera. Esta guarda es la tercera rendija: cierra el
hueco sin tocar `run_phase1.py` ni su Gate 0.

CONTRATO (exacto, del encargo del auditor, TAREA 1.g de la vuelta 124):
  - Lee dataset/metadata/master_graph.json (o --ref REF, cualquier ref de
    git; por defecto WORK, el arbol de trabajo), se queda con los nodos
    VIVOS (`not nodo.get("deprecado")`), normaliza `titulo_concepto` (NFKD,
    sin diacriticos, minusculas, espacios colapsados) y agrupa por esa
    clave normalizada.
  - ROJO EXIT 1 si algun grupo normalizado tiene mas de un id, SALVO los que
    esten en la lista EXCEPCIONES de este mismo fichero (con el id, el
    motivo y la vuelta que la declaro).
  - VERDE EXIT 0 con el recuento: nodos vivos examinados, grupos
    normalizados, duplicados encontrados (antes de restar excepciones) y
    excepciones vigentes.
  - No corrige nada, no toca titulos, no toca run_phase1.py: solo lee y
    grita.

EXCEPCION DE ARRANQUE (vuelta 124, TAREA 1.g): el par
`sistema_responsabilidad_gerencial` / `sistema_responsabilidad_gerencial_2`
("El Sistema es tu Responsabilidad" / "El Sistema es Tu Responsabilidad") es
una de las 28 familias de OP-S-09 y quedo CONTINUA por contenido en la
lectura par a par de la vuelta 123 (`SALIDA_V123_OPS09_LECTURA.jsonl`): el
veredicto NO se reabre aqui (la vara de OP-S-09 es el contenido, no el
titulo), pero el titulo SI queda duplicado a ojos de esta guarda y por eso
entra en EXCEPCIONES, para que la guarda nazca en VERDE hoy y muerda
cualquier par NUEVO a partir de manana. El arreglo del titulo mismo queda
anotado como trabajo POST CAMPAÑA en `docs/PENDIENTES.md` (ficha
campos-sucios-dataset), no se decide aqui.

USO:
  python scripts/loop/verificar_titulos_normalizados.py
  python scripts/loop/verificar_titulos_normalizados.py --ref 6d512a0d

CASO POSITIVO (mutacion, en memoria, no toca disco): se toma el grafo real,
se clona un nodo vivo con un id nuevo y el MISMO `titulo_concepto`, y se
corre la deteccion sobre esa copia; tiene que dar ROJO nombrando el par
inventado. Se corre automaticamente con --autoprueba (no es el modo normal
de uso, es la prueba de mutacion pedida por el contrato).
"""
import argparse
import collections
import json
import os
import re
import subprocess
import sys
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA_GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")

# (id, motivo, vuelta_que_la_declaro)
EXCEPCIONES = [
    ("sistema_responsabilidad_gerencial", "familia OP-S-09 CONTINUA por contenido (SALIDA_V123_OPS09_LECTURA.jsonl); solo el titulo esta duplicado, el veredicto no se reabre", 124),
    ("sistema_responsabilidad_gerencial_2", "familia OP-S-09 CONTINUA por contenido (SALIDA_V123_OPS09_LECTURA.jsonl); solo el titulo esta duplicado, el veredicto no se reabre", 124),
]


def normalizar(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    s = re.sub(r"\s+", " ", s).strip()
    return s


def cargar(ref):
    if ref == "WORK":
        with open(RUTA_GRAFO, encoding="utf-8") as f:
            return json.load(f)
    r = subprocess.run(["git", "show", "%s:dataset/metadata/master_graph.json" % ref],
                       cwd=RAIZ, capture_output=True)
    if r.returncode != 0:
        raise SystemExit("ROJO (arnes): no se pudo leer dataset/metadata/master_graph.json en %s" % ref)
    return json.loads(r.stdout.decode("utf-8"))


def agrupar(nodos):
    """nodos: {node_id: nodo}. Devuelve {clave_normalizada: [ids ordenados]}
    SOLO de los nodos VIVOS."""
    grupos = collections.defaultdict(list)
    vivos = 0
    for nid, n in nodos.items():
        if n.get("deprecado"):
            continue
        vivos += 1
        clave = normalizar(n.get("titulo_concepto"))
        if not clave:
            continue
        grupos[clave].append(nid)
    for clave in grupos:
        grupos[clave].sort()
    return grupos, vivos


def verificar(nodos, excepciones_ids):
    grupos, vivos = agrupar(nodos)
    duplicados = {clave: ids for clave, ids in grupos.items() if len(ids) > 1}
    # Un grupo esta CUBIERTO por la excepcion solo si TODOS sus ids estan en
    # la lista de excepciones. Si un grupo duplicado tiene un id NUEVO que
    # no esta en la excepcion declarada, sigue siendo ROJO: la excepcion
    # cubre el par que se declaro, no cualquier futuro miembro del grupo.
    rojos = {clave: ids for clave, ids in duplicados.items()
             if not all(i in excepciones_ids for i in ids)}
    return grupos, vivos, duplicados, rojos


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", default="WORK")
    ap.add_argument("--autoprueba", action="store_true",
                     help="corre el caso positivo por mutacion (en memoria) y termina")
    a = ap.parse_args()

    grafo = cargar(a.ref)
    nodos = grafo["nodos"]
    excepciones_ids = set(i for i, _m, _v in EXCEPCIONES)

    if a.autoprueba:
        clonado = dict(nodos)
        algun_id = next(nid for nid, n in nodos.items() if not n.get("deprecado") and n.get("titulo_concepto"))
        nodo_original = nodos[algun_id]
        id_falso = "___MUTACION_AUTOPRUEBA___"
        nodo_falso = dict(nodo_original)
        nodo_falso["deprecado"] = False
        nodo_falso["node_id"] = id_falso
        clonado[id_falso] = nodo_falso
        _grupos, _vivos, _duplicados, rojos = verificar(clonado, excepciones_ids)
        clave_esperada = normalizar(nodo_original.get("titulo_concepto"))
        if clave_esperada not in rojos:
            print("CAIDA DE LA AUTOPRUEBA: la mutacion (id %s, clon de %s) no genero ROJO" % (id_falso, algun_id))
            return 1
        print("AUTOPRUEBA VERIFICADA: ROJO con el par inventado (%s, %s), titulo normalizado %r"
              % (sorted(rojos[clave_esperada])[0], sorted(rojos[clave_esperada])[1], clave_esperada))
        return 0

    grupos, vivos, duplicados, rojos = verificar(nodos, excepciones_ids)

    if rojos:
        print("ROJO EXIT 1: %d grupo(s) de titulo normalizado duplicado SIN excepcion vigente (ref %s):" % (len(rojos), a.ref))
        for clave, ids in sorted(rojos.items()):
            print("  %r: %s" % (clave, ", ".join(ids)))
        return 1

    print("VERDE EXIT 0 (ref %s): nodos vivos examinados %d, grupos normalizados %d, "
          "duplicados normalizados encontrados %d, excepciones vigentes %d"
          % (a.ref, vivos, len(grupos), len(duplicados), len(EXCEPCIONES)))
    if duplicados:
        print("duplicados cubiertos por excepcion:")
        for clave, ids in sorted(duplicados.items()):
            print("  %r: %s" % (clave, ", ".join(ids)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
