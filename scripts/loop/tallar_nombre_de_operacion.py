# -*- coding: utf-8 -*-
"""tallar_nombre_de_operacion.py . EL TALLADOR DE NOMBRES DE OPERACION
(TAREA 1.2 de la vuelta 102, encargo del auditor, acta de la vuelta 101,
"SEGUNDA, DE REPORTE, MISMA ESPECIE, Y TAMBIEN ACUMULA").

POR QUE NACE, CON EL EJEMPLAR DELANTE. El reporte de la vuelta 101 escribio
"Las CUATRO mesas de la fase 06" para nombrar a `OP-M-01`, `OP-M-01-FUSION`,
`OP-M-03` y `OP-M-03-III`. Ni son cuatro mesas ni son de la fase 06: el
campo `fase` de `docs/plan/OPERACIONES.jsonl` dice que `OP-M-01` y `OP-M-03`
son `06_MESAS`, pero `OP-M-01-FUSION` y `OP-M-03-III` son `03_FUSIONES`.
`docs/plan/03_FUSIONES.md` linea 9246 ya las nombra por su nombre: son DOS
de las SEIS FUSIONES ENRUTADAS a la fase 06 (la fase 03 cierra con remision,
no con fusion hecha).

QUE HACE, EXACTO Y NADA MAS. Dado un id de operacion, saca de
`docs/plan/OPERACIONES.jsonl` su `fase` y su `tipo` REALES (nunca los
teclea) y decide su CLASE:

  - `fase == "06_MESAS"`               -> "mesa de la fase 06"
  - `fase == "03_FUSIONES"` Y el id esta en la fila "FUSIONES ENRUTADAS a la
    fase 06" de `docs/plan/03_FUSIONES.md` (leida de ese fichero, no de una
    lista tecleada aqui) -> "fusion enrutada a la fase 06"
  - cualquier otro caso                -> "fase %s" % fase, sin clase especial

Con varios ids, AGRUPA por clase y COMPONE la frase contando cada grupo, en
vez de que el ejecutor la teclee. Si algun id no existe en OPERACIONES.jsonl,
o si no se pudo leer la fila de fusiones enrutadas de 03_FUSIONES.md, ES
ROJO y no compone nada (misma mecanica que el resto de esta familia de
talladores).

USO:
  python scripts/loop/tallar_nombre_de_operacion.py OP-M-01 OP-M-01-FUSION OP-M-03 OP-M-03-III

VARA DE SI ALCANZA (caso positivo OBLIGATORIO): con esos cuatro ids, la
frase compuesta tiene que decir DOS mesas de la fase 06 y DOS fusiones
enrutadas a la fase 06, no "cuatro mesas".
"""
import argparse
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA_OPERACIONES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
RUTA_FUSIONES_MD = os.path.join(RAIZ, "docs", "plan", "03_FUSIONES.md")

RE_FILA_ENRUTADAS = re.compile(r"FUSIONES ENRUTADAS a la fase 06", re.IGNORECASE)
RE_ID_OP = re.compile(r"`(OP-[A-Z0-9-]+)`")


def cargar_operaciones(fallos):
    if not os.path.exists(RUTA_OPERACIONES):
        fallos.append("no existe %s" % RUTA_OPERACIONES)
        return {}
    d = {}
    with io.open(RUTA_OPERACIONES, encoding="utf-8") as f:
        for n, linea in enumerate(f, 1):
            linea = linea.strip()
            if not linea:
                continue
            try:
                obj = json.loads(linea)
            except Exception as e:
                fallos.append("linea %d de OPERACIONES.jsonl no es JSON valido: %s" % (n, e))
                continue
            if "id_op" in obj:
                d[obj["id_op"]] = obj
    return d


def cargar_fusiones_enrutadas(fallos):
    """Lee, de docs/plan/03_FUSIONES.md, la fila cuya primera celda menciona
    'FUSIONES ENRUTADAS a la fase 06' y devuelve el conjunto de ids de
    operacion citados entre backticks en esa MISMA fila. Nunca teclea la
    lista: la lee del fichero."""
    if not os.path.exists(RUTA_FUSIONES_MD):
        fallos.append("no existe %s" % RUTA_FUSIONES_MD)
        return set()
    texto = io.open(RUTA_FUSIONES_MD, encoding="utf-8").read()
    for linea in texto.splitlines():
        if RE_FILA_ENRUTADAS.search(linea):
            ids = set(RE_ID_OP.findall(linea))
            if ids:
                return ids
    fallos.append("no se encontro en %s ninguna fila con 'FUSIONES ENRUTADAS a la fase 06'"
                  % RUTA_FUSIONES_MD)
    return set()


def clase_de(id_op, ficha, enrutadas):
    fase = ficha.get("fase", "?")
    if fase == "06_MESAS":
        return "mesa de la fase 06"
    if fase == "03_FUSIONES" and id_op in enrutadas:
        return "fusion enrutada a la fase 06"
    return "fase %s" % fase


PLURAL = {
    "mesa de la fase 06": ("mesa de la fase 06", "mesas de la fase 06"),
    "fusion enrutada a la fase 06": ("fusion enrutada a la fase 06", "fusiones enrutadas a la fase 06"),
}


def componer_frase(clases_por_id):
    """clases_por_id: lista de (id_op, clase), en el orden dado. Agrupa por
    clase (preservando el primer orden de aparicion) y compone la frase."""
    orden = []
    grupos = {}
    for id_op, clase in clases_por_id:
        if clase not in grupos:
            grupos[clase] = []
            orden.append(clase)
        grupos[clase].append(id_op)
    partes = []
    for clase in orden:
        ids = grupos[clase]
        n = len(ids)
        singular, plural = PLURAL.get(clase, (clase, clase + "(s)"))
        etiqueta = singular if n == 1 else plural
        numero = {1: "UNA", 2: "DOS", 3: "TRES", 4: "CUATRO", 5: "CINCO",
                  6: "SEIS", 7: "SIETE", 8: "OCHO"}.get(n, str(n))
        partes.append("%s %s (%s)" % (numero, etiqueta, ", ".join("`%s`" % i for i in ids)))
    return " y ".join(partes)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ops", nargs="+", help="ids de operacion, por ejemplo OP-M-01 OP-M-01-FUSION")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    fallos = []
    operaciones = cargar_operaciones(fallos)
    enrutadas = cargar_fusiones_enrutadas(fallos)
    if fallos:
        print("ROJO, %d cosa(s) no se pudieron leer y NO SE COMPONE NADA:" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1

    clases_por_id = []
    for id_op in a.ops:
        ficha = operaciones.get(id_op)
        if ficha is None:
            fallos.append("%s no existe en OPERACIONES.jsonl" % id_op)
            continue
        clase = clase_de(id_op, ficha, enrutadas)
        clases_por_id.append((id_op, clase))
        print("%s -- fase real: %s -- tipo real: %s -- clase: %s"
              % (id_op, ficha.get("fase", "?"), ficha.get("tipo", "?"), clase))

    if fallos:
        print("ROJO, %d cosa(s) no se pudieron leer y NO SE COMPONE NADA:" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1

    print()
    print("FRASE COMPUESTA: %s" % componer_frase(clases_por_id))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
