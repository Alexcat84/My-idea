# -*- coding: utf-8 -*-
"""vuelta37_fuente_primero.py - PASO 1 DEL ORDEN INTERNO DE OP-D-04: LA FUENTE PRIMERO.

La nota de OP-D-04 escribe su orden interno y no lo deja a criterio:
  1. OP-F-02 PRIMERO, la fuente
  2. el destejido despues
  3. los tres gemelos (823, 834 y 844) al final y en un solo acto

Y su campo depende_de nombra DOS operaciones: OP-F-02 y OP-F-03. El encargo de
la vuelta 37 manda VERIFICAR QUE LAS DOS ESTAN EJECUTADAS ANTES DE APOYARSE EN
ELLAS. Este instrumento hace exactamente eso y nada mas: NO TOCA UN SOLO NODO.

POR QUE NO BASTA LEER LA NOTA. Las notas de OP-F-02 y OP-F-03 declaran
'QUEDA HECHA' con fecha 14 ago 2026, y el campo estado de las dos sigue en LISTA
porque el esquema no tiene otro valor. Una nota es un acta, y EJECUTOR.md regla 2
dice que un acta nunca es fuente de una cifra nueva: se cita como contraste. Asi
que aqui se MIDE CONTRA EL GRAFO DE HOY lo que esas notas afirman, y si algo
discrepa se declara en vez de resolverse copiando.

LO QUE SE MIDE, y de donde sale cada cosa que se espera:
  A. OP-F-02: sus TRES nodo propio, con los pasos que su propia nota declara
     (escenarios_de_evolucion_de_la_ia con 6 pasos, critica_del_plan_con_ia con
     5 y ideacion_con_ia_en_la_sesion con 4), vivos y declarados en
     docs/plan/INDICE_ROJO_DECLARADO.jsonl con su operacion.
  B. OP-F-02: ninguno de sus tres nodos de origen declara ya a Mollick (es la
     primera linea de su campo verificacion).
  C. OP-F-02: brainstorming_divergente entra a OP-D-04 CON LA FUENTE YA FIJADA
     (cuarta linea de su verificacion). La fuente fijada esta escrita en
     docs/plan/01_FUENTES.md: Tim Brown, Change by Design.
  D. OP-F-03: sus CUATRO nodo propio, con los pasos que su nota declara
     (estrategia_circular_y_mecanismo_de_retorno 4,
     seleccion_de_proveedores_por_costo_total 9, driver_de_inventario 4 y
     producto_como_servicio_de_acceso 8), vivos y en el indice rojo.
  E. EL CRUCE: cuantos de los SIETE nodos de OP-D-04 estan en las nominas de
     OP-F-02 y de OP-F-03. Se mide, no se supone.

Uso: python scripts/loop/vuelta37_fuente_primero.py
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
ROJO = os.path.join(RAIZ, "docs", "plan", "INDICE_ROJO_DECLARADO.jsonl")

# Las cifras esperadas NO se inventan aqui: son las que las notas de OP-F-02 y
# OP-F-03 declararon el 14 ago 2026 y que este instrumento va a contrastar.
ESPERADO_F02 = {
    "escenarios_de_evolucion_de_la_ia": 6,
    "critica_del_plan_con_ia": 5,
    "ideacion_con_ia_en_la_sesion": 4,
}
ESPERADO_F03 = {
    "estrategia_circular_y_mecanismo_de_retorno": 4,
    "seleccion_de_proveedores_por_costo_total": 9,
    "driver_de_inventario": 4,
    "producto_como_servicio_de_acceso": 8,
}
FUENTE_FIJADA = "Tim Brown"


def leer_nodo(nid):
    ruta = os.path.join(NODOS, nid + ".json")
    if not os.path.exists(ruta):
        return None
    with io.open(ruta, encoding="utf-8") as fh:
        return json.load(fh)


def operacion(idop):
    with io.open(OPS, encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.strip()
            if not linea:
                continue
            o = json.loads(linea)
            if o.get("id_op") == idop:
                return o
    return None


def rojo_por_op():
    por = {}
    with io.open(ROJO, encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.strip()
            if not linea:
                continue
            r = json.loads(linea)
            # EL INDICE ROJO NOMBRA EL NODO 'id', no 'node_id': medido hoy sobre
            # su primera linea. La primera version de este instrumento leyo
            # 'node_id' y REVENTO con KeyError en vez de dar por buena una lista
            # vacia. Queda escrito: fallar ruidoso (banco 9.10).
            por.setdefault(r.get("operacion"), []).append(r)
    return por


def bloque(titulo):
    print("")
    print("=" * 78)
    print(titulo)
    print("=" * 78)


def main():
    fallos = []
    rojo = rojo_por_op()

    op04 = operacion("OP-D-04")
    op02 = operacion("OP-F-02")
    op03 = operacion("OP-F-03")

    bloque("EL ORDEN QUE MANDA, LEIDO DEL PLAN DE HOY")
    print("OP-D-04 depende_de :", op04.get("depende_de"))
    print("OP-D-04 nodos (%d) :" % len(op04["nodos"]))
    for n in op04["nodos"]:
        print("   ", n)
    print("OP-F-02 estado del campo:", op02.get("estado"))
    print("OP-F-03 estado del campo:", op03.get("estado"))
    print("(los dos campos siguen en LISTA porque el esquema no define otro valor;")
    print(" la declaracion de HECHA vive en la nota, y es lo que aqui se contrasta)")

    bloque("A. OP-F-02: LOS TRES NODO PROPIO, MEDIDOS HOY CONTRA EL GRAFO")
    ids_rojo_02 = set(r["id"] for r in rojo.get("OP-F-02", []))
    print("ids declarados en el indice rojo para OP-F-02:", sorted(ids_rojo_02))
    for nid in sorted(ESPERADO_F02):
        esperado = ESPERADO_F02[nid]
        nodo = leer_nodo(nid)
        if nodo is None:
            print("  %-38s AUSENTE DEL GRAFO" % nid)
            fallos.append("A: %s ausente" % nid)
            continue
        pasos = len(nodo.get("pasos_accionables") or [])
        vivo = not nodo.get("deprecado", False)
        en_rojo = nid in ids_rojo_02
        ok = (pasos == esperado) and vivo and en_rojo
        print("  %-38s pasos %d (nota dice %d)  vivo %s  en indice rojo %s   %s"
              % (nid, pasos, esperado, vivo, en_rojo, "OK" if ok else "DISCREPA"))
        if not ok:
            fallos.append("A: %s" % nid)

    bloque("B. OP-F-02: MOLLICK FUERA DE LOS TRES NODOS DE ORIGEN")
    for nid in op02["nodos"]:
        nodo = leer_nodo(nid)
        if nodo is None:
            print("  %-32s AUSENTE" % nid)
            fallos.append("B: %s ausente" % nid)
            continue
        fuente = nodo.get("fuente") or ""
        texto = json.dumps(nodo, ensure_ascii=False)
        hay = "Mollick" in texto
        print("  %-32s Mollick en el fichero entero: %s" % (nid, hay))
        print("      fuente de hoy: %s" % fuente)
        if hay:
            fallos.append("B: %s aun declara Mollick" % nid)

    bloque("C. brainstorming_divergente ENTRA A OP-D-04 CON LA FUENTE FIJADA")
    bd = leer_nodo("brainstorming_divergente")
    fuente_bd = bd.get("fuente") or ""
    trozos = [t for t in fuente_bd.split("|") if t.strip()]
    print("  fuente medida hoy : %s" % fuente_bd)
    print("  la fuente fijada por 01_FUENTES.md nombra a: %s" % FUENTE_FIJADA)
    print("  la contiene: %s" % (FUENTE_FIJADA in fuente_bd))
    print("  fuentes distintas declaradas: %d" % len(trozos))
    if FUENTE_FIJADA not in fuente_bd:
        fallos.append("C: la fuente de brainstorming_divergente no es la fijada")
    if len(trozos) != 1:
        fallos.append("C: brainstorming_divergente declara mas de una fuente")

    bloque("D. OP-F-03: LOS CUATRO NODO PROPIO, MEDIDOS HOY CONTRA EL GRAFO")
    ids_rojo_03 = set(r["id"] for r in rojo.get("OP-F-03", []))
    print("ids declarados en el indice rojo para OP-F-03:", sorted(ids_rojo_03))
    for nid in sorted(ESPERADO_F03):
        esperado = ESPERADO_F03[nid]
        nodo = leer_nodo(nid)
        if nodo is None:
            print("  %-46s AUSENTE DEL GRAFO" % nid)
            fallos.append("D: %s ausente" % nid)
            continue
        pasos = len(nodo.get("pasos_accionables") or [])
        vivo = not nodo.get("deprecado", False)
        en_rojo = nid in ids_rojo_03
        ok = (pasos == esperado) and vivo and en_rojo
        print("  %-46s pasos %d (nota dice %d)  vivo %s  en indice rojo %s   %s"
              % (nid, pasos, esperado, vivo, en_rojo, "OK" if ok else "DISCREPA"))
        if not ok:
            fallos.append("D: %s" % nid)

    bloque("E. EL CRUCE MEDIDO: QUE NODOS DE OP-D-04 TOCAN LA FASE 01")
    siete = set(op04["nodos"])
    en02 = sorted(siete & set(op02["nodos"]))
    en03 = sorted(siete & set(op03["nodos"]))
    print("  de los SIETE de OP-D-04, en la nomina de OP-F-02: %d  %s" % (len(en02), en02))
    print("  de los SIETE de OP-D-04, en la nomina de OP-F-03: %d  %s" % (len(en03), en03))
    print("  OP-F-03 tiene %d nodos en su nomina." % len(op03["nodos"]))
    print("  Si la segunda lista sale vacia, la dependencia OP-D-04 -> OP-F-03 es de")
    print("  ORDEN DE FASE y no de nodo compartido, y asi queda medido.")

    bloque("VEREDICTO DEL PASO 1")
    if fallos:
        print("LA FUENTE NO ESTA LIMPIA. Discrepancias:")
        for f in fallos:
            print("   -", f)
        print("")
        print("PASO 1 EN ROJO: no se sigue con el destejido.")
        return 1
    print("LAS DOS OPERACIONES DE FUENTE ESTAN EJECUTADAS, MEDIDO HOY CONTRA EL GRAFO.")
    print("Tres nodo propio de OP-F-02 y cuatro de OP-F-03, vivos, con los pasos que")
    print("sus notas declaran y declarados en el indice rojo; Mollick fuera de los tres")
    print("origenes; brainstorming_divergente con UNA sola fuente, la fijada.")
    print("")
    print("PASO 1 VERDE: se puede apoyar OP-D-04 en la fase 01.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
