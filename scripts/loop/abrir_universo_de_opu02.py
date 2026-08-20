# -*- coding: utf-8 -*-
"""abrir_universo_de_opu02.py . MIDE LA APERTURA DE OP-U-02 Y FIJA SU NOMINA EN
FICHERO PROPIO. NO FUNDE NI UN ACTO.

NOMBRE ESTABLE, y no lleva vuelta: el insumo entra por --componentes y el destino
por --salida. Es la vara del acta 58, pregunta 4, la misma con la que nacieron
abrir_tramo_de_opu01.py y generar_plan_del_lote.py.

ES ESTRICTAMENTE DE SOLO LECTURA SOBRE EL DATASET. Escribe UN fichero, la nomina,
y nada mas. No toca un nodo, no sella un plan y no decide ningun superviviente.

QUE MIDE, y esta es toda su aritmetica:

  1. LOS ABIERTOS. Los toma del jsonl de componentes del recomputo CORRIDO EN LA
     MISMA VUELTA, no de un fichero sellado viejo. El estado ABIERTO lo escribe
     ese recomputo con el criterio de OP-U-01: un acto esta CERRADO si todos sus
     pares internos estan leidos Y ningun miembro tiene par pendiente en la cola.

  2. EL DUENO DE CADA UNO, POR EL RESOLUTOR (P.1). Cada miembro se resuelve por
     la cadena de alias del arbol de HOY antes de compararse, o un acto cuyo
     miembro ya fue absorbido por otra operacion pareceria libre. Se cruza contra
     la nomina de TODAS las operaciones de docs/plan/OPERACIONES.jsonl (campos
     nodos, eliminar y superviviente, los tres resueltos).

  3. LOS DOS CRITERIOS, Y LOS DOS SE IMPRIMEN, porque el plan usa los dos y dan
     cifras distintas:
       ESTRECHO, el del propio plan: solo cuenta como dueno una operacion de
         MESA o de DESTEJIDO. Es el que la nota de OP-U-02 aplica cuando dice
         que el recomputo no abre 55 sino 47.
       ANCHO, el AVISO DE TRAMPA de aquella misma nota: dueno es cualquier
         operacion que toque algun miembro, sea de la fase que sea.

  4. LAS EXCLUSIONES QUE EL PLAN YA ESCRIBE, COMPROBADAS CONTRA EL GRAFO DE HOY
     Y NO SUPUESTAS. Van en --exclusion con la forma id_op:motivo, se buscan
     entre los abiertos medidos y se dice de cada una si SIGUE ABIERTA, si ya
     esta CONSUMIDA (sus nodos ya fundidos o destejidos) o si NO APARECE.

LO QUE ESTE INSTRUMENTO NO HACE, dicho para que nadie le pida lo que no da: NO
elige superviviente, NO reparte piezas y NO declara ningun acto. Solo fija quien
entra en el universo de OP-U-02 y quien no, con su motivo citado.

Uso:
  python scripts/loop/abrir_universo_de_opu02.py
      --componentes docs/loop/_v63_componentes_cierre.jsonl
      --salida docs/loop/NOMINA_OPU02_V63.jsonl
      [--exclusion OP-M-01-FUSION:...] [--simular]
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
OPERACIONES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
NL = chr(10)
MESA_O_DESTEJIDO = ("MESA", "DESTEJIDO")


def cargar_alias():
    """La cadena de alias del arbol de HOY, mas el estado de cada nodo."""
    alias, dep = {}, {}
    for f in sorted(os.listdir(NODOS)):
        if not f.endswith(".json"):
            continue
        d = json.load(io.open(os.path.join(NODOS, f), encoding="utf-8"))
        nid = d["node_id"]
        dep[nid] = bool(d.get("deprecado") or d.get("deprecated"))
        for x in (d.get("ids_alias") or []):
            alias[x] = nid
    return alias, dep


def resolutor(alias):
    def res(x):
        visto = set()
        while x in alias and x not in visto:
            visto.add(x)
            x = alias[x]
        return x
    return res


def es_mesa_o_destejido(op):
    t = (op.get("tipo") or "").upper()
    fase = (op.get("fase") or "").upper()
    return any(k in t for k in MESA_O_DESTEJIDO) or any(k in fase for k in MESA_O_DESTEJIDO)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--componentes", required=True)
    ap.add_argument("--salida", required=True)
    ap.add_argument("--exclusion", action="append", default=[],
                    help="id_op:motivo, repetible. Se comprueba contra lo medido")
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    comps = [json.loads(l) for l in
             io.open(os.path.join(RAIZ, a.componentes.replace("/", os.sep)), encoding="utf-8")
             if l.strip()]
    ops = [json.loads(l) for l in io.open(OPERACIONES, encoding="utf-8") if l.strip()]
    alias, dep = cargar_alias()
    res = resolutor(alias)

    print("=" * 78)
    print("LA APERTURA MEDIDA DE OP-U-02. NO SE FUNDE NI UN ACTO.")
    print("  componentes: %s (%d actos)" % (a.componentes, len(comps)))
    print("  operaciones: docs/plan/OPERACIONES.jsonl (%d)" % len(ops))
    print("  nodos con alias en el arbol de hoy: %d | deprecados: %d"
          % (len(alias), sum(1 for v in dep.values() if v)))
    print("=" * 78)
    print()

    abiertos = [c for c in comps if c["estado"] == "ABIERTO"]
    cerrados = [c for c in comps if c["estado"] == "CERRADO"]
    print("PASO 1: EL CENSO DE LOS ABIERTOS, LEIDO DEL RECOMPUTO DE ESTA VUELTA")
    print("  actos totales : %d" % len(comps))
    print("  CERRADOS      : %d sobre %d nodos"
          % (len(cerrados), sum(c["tamano"] for c in cerrados)))
    print("  ABIERTOS      : %d sobre %d nodos"
          % (len(abiertos), sum(c["tamano"] for c in abiertos)))
    tam = {}
    for c in abiertos:
        tam[c["tamano"]] = tam.get(c["tamano"], 0) + 1
    print("  ABIERTOS por tamano: %s"
          % ", ".join("%d de %d" % (tam[k], k) for k in sorted(tam, reverse=True)))
    print()

    # nomina de cada operacion, RESUELTA
    nominas = {}
    for op in ops:
        ids = set(op.get("nodos") or []) | set(op.get("eliminar") or [])
        if op.get("superviviente"):
            ids.add(op["superviviente"])
        nominas[op["id_op"] or "SIN ID"] = (op, {res(x) for x in ids})

    print("PASO 2: EL DUENO DE CADA ABIERTO, POR EL RESOLUTOR (P.1)")
    print()
    filas = []
    for c in sorted(abiertos, key=lambda x: (-x["tamano"], x["miembros"][0])):
        vivos = [x for x in c["miembros"] if not dep.get(res(x), False)]
        resueltos = {res(x) for x in c["miembros"]}
        duenos_anchos, duenos_estrechos = [], []
        for id_op, (op, ids) in nominas.items():
            if resueltos & ids:
                duenos_anchos.append(id_op)
                if es_mesa_o_destejido(op):
                    duenos_estrechos.append(id_op)
        filas.append({
            "tamano": c["tamano"],
            "miembros": c["miembros"],
            "miembros_resueltos_distintos": sorted(resueltos),
            "miembros_vivos": len(vivos),
            "duenos_mesa_o_destejido": sorted(duenos_estrechos),
            "duenos_cualquier_operacion": sorted(duenos_anchos),
            "abre": not duenos_estrechos,
            "edad": c.get("edad"),
            "clases_internas": c.get("clases_internas"),
        })
    abre = [f for f in filas if f["abre"]]
    fuera = [f for f in filas if not f["abre"]]
    print("  %-6s %-9s %-13s %s" % ("tamano", "abre", "duenos MESA/DEST", "primer miembro"))
    print("  " + "-" * 92)
    for f in filas:
        print("  %-6d %-9s %-13s %s"
              % (f["tamano"], "SI" if f["abre"] else "NO",
                 ",".join(f["duenos_mesa_o_destejido"]) or ".", f["miembros"][0]))
    print()
    print("  CRITERIO ESTRECHO (el del propio plan: dueno en MESA o DESTEJIDO)")
    print("     ABRE  : %d actos sobre %d nodos"
          % (len(abre), sum(f["tamano"] for f in abre)))
    print("     FUERA : %d actos sobre %d nodos"
          % (len(fuera), sum(f["tamano"] for f in fuera)))
    anchos = [f for f in filas if f["duenos_cualquier_operacion"]]
    print("  CRITERIO ANCHO (el AVISO DE TRAMPA: toca CUALQUIER nomina)")
    print("     tocan alguna nomina: %d | no tocan ninguna: %d"
          % (len(anchos), len(filas) - len(anchos)))
    print()

    print("PASO 3: LOS QUE QUEDAN FUERA, CADA UNO CON SU DUENO NOMBRADO")
    print()
    for f in sorted(fuera, key=lambda x: -x["tamano"]):
        print("  tamano %-3d duenos %-40s"
              % (f["tamano"], ", ".join(f["duenos_mesa_o_destejido"])))
        print("     miembros: %s" % ", ".join(f["miembros"]))
    print()

    print("PASO 4: LAS EXCLUSIONES QUE EL PLAN ESCRIBE, COMPROBADAS CONTRA LO MEDIDO")
    print()
    if not a.exclusion:
        print("  NO SE PASO NINGUNA EXCLUSION A ESTE INSTRUMENTO, y por eso este bloque")
        print("  DECLARA SU FALTA en vez de suponerla.")
    for ex in a.exclusion:
        id_op, _, motivo = ex.partition(":")
        op, ids = nominas.get(id_op, (None, set()))
        if op is None:
            print("  %-18s ROJO: no existe esa operacion en OPERACIONES.jsonl" % id_op)
            continue
        toca = [f for f in filas if set(f["miembros_resueltos_distintos"]) & ids]
        vivos = sorted(x for x in ids if not dep.get(x, True))
        muertos = sorted(x for x in ids if dep.get(x, False))
        if toca:
            estado = "SIGUE ABIERTO, y queda fuera por su dueno"
            det = "tamano %s" % ", ".join(str(f["tamano"]) for f in toca)
        elif muertos and not [x for x in ids if x not in dep]:
            estado = "CONSUMIDA: su nomina ya no forma acto abierto"
            det = "%d de %d ids deprecados hoy" % (len(muertos), len(ids))
        else:
            estado = "NO APARECE ENTRE LOS ABIERTOS"
            det = "%d ids vivos, %d deprecados" % (len(vivos), len(muertos))
        print("  %-18s %-46s %s" % (id_op, estado, det))
        print("     nomina de la ficha (%d ids): %s" % (len(ids), ", ".join(sorted(ids))))
        if motivo:
            print("     motivo citado: %s" % motivo)
    print()

    destino = os.path.join(RAIZ, a.salida.replace("/", os.sep))
    if a.simular:
        print("MODO SIMULAR: no se escribe la nomina.")
    else:
        with io.open(destino, "w", encoding="utf-8", newline=NL) as fh:
            for i, f in enumerate(sorted(filas, key=lambda x: (-x["tamano"],
                                                              x["miembros"][0])), 1):
                f2 = dict(f)
                f2["orden_universo"] = i
                fh.write(json.dumps(f2, ensure_ascii=False) + NL)
        print("NOMINA FIJADA: %s (%d filas, una por acto abierto, con sus miembros)"
              % (a.salida, len(filas)))
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
