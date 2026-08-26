# -*- coding: utf-8 -*-
"""_v73_borde_del_dueno.py . EL BORDE DEL DUENO DEL LOTE I, MIRADO POR MAQUINA.

NO ES UN INSTRUMENTO DE NOMBRE ESTABLE: es la sonda de esta vuelta, y va con su
numero por delante para que nadie la confunda con una vara de la casa. Mide
exactamente lo que el encargo de la vuelta 73 pide mirar antes de sellar un plan,
y NO decide nada.

QUE MIRA, Y POR QUE CADA COSA:
  1. LOS DOS CAMPOS duenos_* DEL FICHERO FIJADO para los actos del lote y para
     los DOS que se saltan (31 y 37), porque los saltos van declarados CON SU
     DUENO CITADO y una cita sin medicion no vale (regla 1).
  2. INVENTARIO.jsonl, entrada a entrada, para todos los miembros del lote: de
     que tipo es cada entrada que los toca, y en particular si alguna
     familia_de_ids cubre la NOMINA ENTERA de un acto. La adjudicacion 2 del acta
     71 manda que una familia_de_ids de nomina ENTERA sin resolucion aprobada vaya
     como PREGUNTA y no como fusion, y una busqueda negativa no se puede citar
     (regla 9): hay que barrer y contar, no dejar de encontrar.
  3. RACIMOS_MIEMBROS.jsonl, por si algun miembro vive en la nomina de un racimo.
  4. LAS MENCIONES en OPERACIONES.jsonl, CAMPO A CAMPO y no por grep, porque lo
     que hace dueno a una operacion es una de las TRES fuentes que la adjudicacion
     2 del acta 68 fija, y una mencion en el campo nota NO es ninguna de ellas.

DE SOLO LECTURA. No escribe nada.

Uso: python scripts/loop/_v73_borde_del_dueno.py
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TRAMO = os.path.join(RAIZ, "docs", "loop", "TRAMO_UNICO_OPU02_V64.jsonl")
INV = os.path.join(RAIZ, "docs", "plan", "INVENTARIO.jsonl")
RAC = os.path.join(RAIZ, "docs", "RACIMOS_MIEMBROS.jsonl")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")

LOTE = [49, 50, 51, 53]
SALTOS = [31, 37]


def cargar(p):
    return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    filas = {int(r["orden_universo"]): r for r in cargar(TRAMO)}

    print("=" * 78)
    print("EL BORDE DEL DUENO DEL LOTE I, MEDIDO Y NO SUPUESTO")
    print("=" * 78)
    print()
    print("--- 1. LOS DOS CAMPOS duenos_* DEL FICHERO FIJADO ---")
    print("  (los del lote tienen que estar VACIOS; los DOS saltos tienen que")
    print("   traer el dueno que el acta 69 les adjudico, y aqui se lee)")
    for o in LOTE + SALTOS:
        r = filas[o]
        etq = "LOTE I" if o in LOTE else "SALTO"
        print("     acto %-3d %-7s duenos_mesa_o_destejido=%s  duenos_cualquier_operacion=%s"
              % (o, etq, r.get("duenos_mesa_o_destejido") or [],
                 r.get("duenos_cualquier_operacion") or []))
    miembros = []
    for o in LOTE:
        miembros.extend(filas[o]["miembros"])
    print()
    print("  miembros del lote I, contados: %d" % len(miembros))

    print()
    print("--- 2. INVENTARIO.jsonl, BARRIDO ENTERO ---")
    inv = cargar(INV)
    print("  entradas del inventario, contadas hoy: %d" % len(inv))
    tocan = []
    for e in inv:
        ms = set(e.get("miembros") or [])
        cruce = [m for m in miembros if m in ms]
        if cruce:
            tocan.append((e, cruce))
    print("  entradas que TOCAN a alguno de los %d miembros: %d" % (len(miembros), len(tocan)))
    por_tipo = {}
    for e, _ in tocan:
        por_tipo[e["tipo"]] = por_tipo.get(e["tipo"], 0) + 1
    for t in sorted(por_tipo):
        print("     de tipo %-16s : %d" % (t, por_tipo[t]))
    print()
    print("  UNA A UNA, con el acto que tocan y su cobertura:")
    enteras = 0
    for e, cruce in tocan:
        actos = sorted(set(o for o in LOTE if any(m in filas[o]["miembros"] for m in cruce)))
        for o in actos:
            nom = filas[o]["miembros"]
            dentro = [m for m in cruce if m in nom]
            cobertura = "%d de %d" % (len(dentro), len(nom))
            entera = len(dentro) == len(nom)
            if e["tipo"] == "familia_de_ids" and entera:
                enteras += 1
            print("     [%-14s] %-34s acto %-3d cubre %-8s %s | operaciones=%s"
                  % (e["tipo"], str(e.get("nombre"))[:34], o, cobertura,
                     "NOMINA ENTERA" if entera else "PARTE",
                     e.get("operaciones") or []))
            if e.get("nota"):
                print("        nota: %s" % e["nota"][:200])
    print()
    print("  familia_de_ids que cubren la NOMINA ENTERA de un acto del lote: %d" % enteras)
    print("  (la adjudicacion 2 del acta 71: si hubiera alguna SIN resolucion")
    print("   aprobada, va como PREGUNTA y no como fusion)")

    print()
    print("--- 3. RACIMOS_MIEMBROS.jsonl ---")
    rac = cargar(RAC)
    print("  lineas de racimos barridas: %d" % len(rac))
    hits = []
    for r in rac:
        for m in r.get("miembros") or []:
            if m.get("node_id") in miembros:
                hits.append((r["racimo"], m["node_id"]))
    print("  miembros del lote que aparecen en alguna nomina de racimo: %d" % len(hits))
    for nombre, nid in hits:
        print("     %-52s en el racimo %s" % (nid, nombre))

    print()
    print("--- 4. LAS MENCIONES EN OPERACIONES.jsonl, CAMPO A CAMPO ---")
    ops = cargar(OPS)
    print("  fichas leidas: %d" % len(ops))
    total = 0
    fichas = set()
    for op in ops:
        for campo, valor in sorted(op.items()):
            if campo == "id_op":
                continue
            texto = json.dumps(valor, ensure_ascii=False)
            for m in miembros:
                if m in texto:
                    total += 1
                    fichas.add(op["id_op"])
                    print("     %-16s campo %-18s menciona %s" % (op["id_op"], campo, m))
    print()
    print("  MENCIONES en total: %d, en %d fichas: %s"
          % (total, len(fichas), sorted(fichas)))
    print("  LAS TRES FUENTES QUE HACEN DUENO (acta 68, adjudicacion 2) son los")
    print("  campos nodos, preservar y eliminar de la ficha. Menciones en nota NO")
    print("  hacen dueno. Reparto por campo:")
    campos = {}
    for op in ops:
        for campo, valor in sorted(op.items()):
            if campo == "id_op":
                continue
            texto = json.dumps(valor, ensure_ascii=False)
            n = sum(1 for m in miembros if m in texto)
            if n:
                campos[campo] = campos.get(campo, 0) + n
    for c in sorted(campos):
        marca = "  <-- HACE DUENO" if c in ("nodos", "preservar", "eliminar") else ""
        print("     campo %-18s : %d%s" % (c, campos[c], marca))
    print()
    print("FIN")
    return 0


if __name__ == "__main__":
    sys.exit(main())
