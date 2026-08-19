# -*- coding: utf-8 -*-
"""vuelta41_lectura_acto.py - UN ACTO DE OP-D-06, LEIDO ENTERO Y CON LA CITA DELANTE.

ESTRICTAMENTE DE SOLO LECTURA. No funde, no toca un nodo, no regenera ninguna
cola: LEE LA COLA QUE EL INSTRUMENTO YA ENTREGO (docs/COSTURAS_INTERNAS.jsonl).

SUCESOR DECLARADO de scripts/loop/vuelta40_costuras_opd05.py, al que NO
reemplaza. Aquel tenia la nomina de OP-D-05 TECLEADA en el codigo, porque era un
acto unico de tres nodos. OP-D-06 son NUEVE actos de dos y su particion vive en
la tabla sellada de docs/plan/02_DESTEJIDOS.md, asi que aqui la nomina se LEE de
esa tabla con el mismo lector que ya usa scripts/loop/vuelta40_acto_opd06.py
(regla 1 del EJECUTOR.md: la tabla se imprime, no se teclea).

LAS CINCO COSAS QUE SEPARA, y separarlas es el punto:

  (a) LA NOMINA del acto, leida de la tabla sellada, y el aviso de solape del
      plan comprobado contra el fichero en vez de recordado.
  (b) QUE CITA EL INSTRUMENTO DE COSTURAS sobre los dos nodos: dentro o fuera de
      la cola entregada, con su ficha entera si esta dentro. EL INSTRUMENTO CITA
      Y NO JUZGA, y desde la vuelta 41 su propia salida declara ademas que LA
      COLA GLOBAL NO ES BASE DE LECTURA.
  (c) EL TEXTO ENTERO de los dos nodos, que es lo unico que decide, con P.11 a
      mano para separar advertencia de procedimiento.
  (d) P.5: el par, su clase y su razon ENTERA del archivo, y la comprobacion de
      que el subconjunto es CERRADO (ningun otro par del archivo mete a un
      tercero en este acto).
  (e) P.8: el cableado (grados por P.1) y las aristas propias sin reciproco, que
      es el COSTE MEDIDO de elegir a uno o a otro. El cableado ACOMPANA, NO
      DECIDE, y por eso se imprime al final y no al principio.

Uso: python scripts/loop/vuelta41_lectura_acto.py --puesto 285
"""
import argparse
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
COLA = os.path.join(RAIZ, "docs", "COSTURAS_INTERNAS.jsonl")
MD = os.path.join(RAIZ, "docs", "plan", "02_DESTEJIDOS.md")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
CAMPOS = ("nodos_previos", "nodos_siguientes")
OPUESTO = {"nodos_previos": "nodos_siguientes", "nodos_siguientes": "nodos_previos"}

# La misma vara del hermano mayor (vuelta39_acto.py y vuelta40_acto_opd06.py):
# 9.3.1 busca el VERBO de adjudicacion, NO el id. Se copia literal para que las
# tres medidas sean comparables.
VERBOS_GANADOR = ("GANA ", "GANA.", " gana ", "SOBREVIVE", "sobrevive",
                  "superviviente es", "EL SUPERVIVIENTE")

# El par que el AVISO DE SOLAPE del plan nombra, leido de la tabla y comprobado
# aparte: es el unico acto de los nueve que NO elige superviviente.
PAR_DEL_AVISO = frozenset(("principio_calidad_mvp", "producto_minimo_viable"))

RE_FILA = re.compile(
    r"^\|\s*\*{0,2}(\d+)\*{0,2}\s*\|\s*`([a-z0-9_]+)`\s*con\s*`([a-z0-9_]+)`\s*\|")


def particion_del_plan():
    texto = io.open(MD, encoding="utf-8").read()
    ini = texto.index("ADJUDICADO Y COMPLETADO. Los nueve pares")
    trozo = texto[ini:ini + 4000]
    pares = []
    for linea in trozo.splitlines():
        m = RE_FILA.match(linea)
        if m:
            pares.append((int(m.group(1)), m.group(2), m.group(3)))
    return pares


def nodo(nid):
    return json.loads(io.open(os.path.join(NODOS, nid + ".json"),
                              encoding="utf-8").read())


def raya(t):
    print("")
    print("=" * 78)
    print(t)
    print("=" * 78)


def volcar(nid, d):
    print("")
    print("-" * 78)
    print("  %s   %s" % (nid, "VIVO" if not d.get("deprecado") else "DEPRECADO"))
    print("-" * 78)
    print("  titulo    : %s" % d.get("titulo_concepto"))
    print("  etiqueta  : %s" % d.get("etiqueta_arbol"))
    print("  dominio   : %s" % d.get("dominio"))
    print("  fuente    : %s" % d.get("fuente"))
    print("  alias     : %s" % (d.get("ids_alias") or []))
    print("  PASOS (%d):" % len(d.get("pasos_accionables") or []))
    for i, p in enumerate(d.get("pasos_accionables") or [], 1):
        print("    %d. %s" % (i, p))
    print("  CONDICIONES (%d):" % len(d.get("condiciones_activacion") or []))
    for i, c in enumerate(d.get("condiciones_activacion") or [], 1):
        print("    c%d. %s" % (i, c))
    print("  ENTREGABLE: %s" % d.get("entregable_esperado"))
    print("  RESUMEN   : %s" % d.get("resumen_teorico"))
    print("  previos   (%d): %s" % (len(d.get("nodos_previos") or []),
                                    d.get("nodos_previos") or []))
    print("  siguientes(%d): %s" % (len(d.get("nodos_siguientes") or []),
                                    d.get("nodos_siguientes") or []))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--puesto", type=int, required=True)
    args = ap.parse_args()

    pares = particion_del_plan()
    fila = [p for p in pares if p[0] == args.puesto]
    if not fila:
        sys.exit("PARADA: el puesto %d no esta en la tabla sellada (%s)"
                 % (args.puesto, [p[0] for p in pares]))
    puesto, A, B = fila[0]

    raya("(a) LA NOMINA DEL ACTO %d, LEIDA DE LA TABLA SELLADA" % puesto)
    print("  nodo A: %s" % A)
    print("  nodo B: %s" % B)
    print("  la tabla sellada trae %d actos; este es el numero %d de los nueve"
          % (len(pares), [p[0] for p in pares].index(puesto) + 1))
    ops = [json.loads(l) for l in io.open(OPS, encoding="utf-8") if l.strip()]
    op = next(o for o in ops if o["id_op"] == "OP-D-06")
    print("  los dos estan en la nomina de OPERACIONES.jsonl: %s"
          % ("SI" if A in op["nodos"] and B in op["nodos"] else "NO [ROJO]"))
    texto_md = io.open(MD, encoding="utf-8").read()
    ini = texto_md.index("## `OP-D-06`")
    fin = texto_md.index("## VERIFICACION DE LA FASE", ini)
    seccion = texto_md[ini:fin]
    print("")
    print("  EL AVISO DE SOLAPE DEL PLAN, comprobado contra el fichero y no recordado:")
    dentro = False
    for linea in seccion.splitlines():
        if "AVISO DE SOLAPE" in linea:
            dentro = True
        if dentro:
            print("    %s" % linea.rstrip())
            if "no dos trabajos" in linea:
                break
    print("")
    print("  ESTE ACTO ESTA NOMBRADO EN EL AVISO DE SOLAPE: %s"
          % ("SI, y por eso NO elige superviviente"
             if frozenset((A, B)) == PAR_DEL_AVISO else "NO"))
    print("")
    print("  EL REPARTO YA ESCRITO PARA ESTE ACTO, si lo tiene:")
    hallado = False
    for linea in seccion.splitlines():
        if linea.startswith("| `") and ("puesto %d" % puesto) in linea:
            print("    %s" % linea.rstrip())
            hallado = True
    if not hallado:
        print("    NINGUNO ESCRITO. Se resuelve con la regla adjudicada: cada")
        print("    perdida al bloque del que proviene, y la que no tenga bloque")
        print("    al superviviente.")

    raya("(b) QUE CITA EL INSTRUMENTO DE COSTURAS SOBRE LOS DOS NODOS")
    print("  Fuente: docs/COSTURAS_INTERNAS.jsonl, LA COLA QUE EL INSTRUMENTO YA")
    print("  ENTREGO. No se recalcula ni una cifra. EL INSTRUMENTO CITA Y NO JUZGA,")
    print("  y desde la vuelta 41 su salida declara ademas que LA COLA GLOBAL NO ES")
    print("  BASE DE LECTURA mientras el MIN_BLOQUE siga pendiente del fundador.")
    cola = {}
    for l in io.open(COLA, encoding="utf-8"):
        if l.strip():
            f = json.loads(l)
            cola[f["node_id"]] = f
    print("  nodos en la cola entregada: %d" % len(cola))
    for nid in (A, B):
        print("")
        f = cola.get(nid)
        if not f:
            print("  %-44s FUERA DE LA COLA: el instrumento NO lo cita" % nid)
            continue
        print("  %-44s CITADO por el instrumento" % nid)
        print("      pasos %d | pareja %.1f (pasos %s) | bloque %s | corte tras %s"
              % (f["pasos"], f["sim_pareja"], f["pareja"], f["sim_bloque_texto"],
                 f["corte"]))
        print("      disparo por pareja: %s | por bloque: %s | franja 44-45: %s"
              % (f["disparo_pareja"], f["disparo_bloque"], f["franja_44_45"]))
        print("      paso A de la pareja citada: %s" % f["paso_a"])
        print("      paso B de la pareja citada: %s" % f["paso_b"])

    raya("(c) EL TEXTO ENTERO DE LOS DOS NODOS, que es lo unico que decide")
    dA, dB = nodo(A), nodo(B)
    volcar(A, dA)
    volcar(B, dB)

    raya("(d) P.5: EL PAR, SU CLASE, SU RAZON ENTERA, Y EL CIERRE DEL SUBCONJUNTO")
    veredictos = []
    for l in io.open(VER, encoding="utf-8"):
        if l.strip():
            veredictos.append(json.loads(l))
    clases = {frozenset((v["nodo_a"], v["nodo_b"])): v for v in veredictos}
    v = clases.get(frozenset((A, B)))
    if not v:
        print("  [ROJO] el par no tiene veredicto en el archivo")
    else:
        print("  puesto %s | clase %s | %s con %s"
              % (v.get("puesto_intra"), v.get("clase"), v.get("nodo_a"), v.get("nodo_b")))
        print("  RAZON ENTERA (%d caracteres):" % len(v.get("razon") or ""))
        print("    %s" % (v.get("razon") or ""))
        r = v.get("razon") or ""
        if v.get("clase") == "A":
            print("  9.3.1, LA VARA DEL VERBO: nombra ganador en su razon: %s"
                  % ("SI" if any(w in r for w in VERBOS_GANADOR)
                     else "NO, es POR ELEGIR"))
        else:
            print("  9.3.1 SOLO CORRE SOBRE A. Esta es clase %s." % v.get("clase"))
    print("")
    print("  EL SUBCONJUNTO, CERRADO O NO: todo par del ARCHIVO que meta a un")
    print("  tercero con cualquiera de los dos (P.5 pide el acto entero).")
    terceros = []
    for w in veredictos:
        s = {w["nodo_a"], w["nodo_b"]}
        if s == {A, B}:
            continue
        if s & {A, B}:
            terceros.append((w.get("puesto_intra"), w.get("clase"), w["nodo_a"],
                             w["nodo_b"]))
    if not terceros:
        print("    NINGUNO. El subconjunto de los dos es CERRADO: UNA familia de dos.")
    else:
        for t in sorted(terceros):
            print("    puesto %-5s clase %-3s %s con %s" % t)
        print("    %d par(es) con tercero." % len(terceros))
        print("")
        print("    LA GUARDA QUE DECIDE SI EL ACTO ES DE DOS: un acto se construye")
        print("    por TRANSITIVIDAD SOBRE LAS A. Un tercero unido por B o por D NO")
        print("    entra en el acto; uno unido por A SI, y entonces el acto no seria")
        print("    de dos y habria que PARAR.")
        con_a = [t2 for t2 in terceros if t2[1] == "A"]
        print("    terceros de clase A: %d  ->  %s"
              % (len(con_a),
                 "el acto ES de dos, como la tabla sellada dice" if not con_a
                 else "[ROJO] PARADA: %s" % (con_a,)))
        print("")
        print("    Y LOS QUE VUELVEN A LA COLA DE RELECTURA POST FUSION (08_VERIFICACION:")
        print("    un par vuelve cuando uno de sus dos nodos MUERE o CAMBIA DE TEXTO, y")
        print("    solo los B y los C, porque son los que estaban en el filo):")
        cola_re = [t2 for t2 in terceros if t2[1] in ("B", "C")]
        for t2 in sorted(cola_re):
            print("      puesto %-5s clase %-3s %s con %s" % t2)
        print("      %d par(es) a releer al cierre de este acto." % len(cola_re))

    raya("(e) P.8: EL CABLEADO, QUE ACOMPANA Y NO DECIDE")
    G = {}
    for nombre in sorted(os.listdir(NODOS)):
        if nombre.endswith(".json"):
            d = nodo(nombre[:-5])
            G[d["node_id"]] = d
    ALIAS = {a: k for k, v2 in G.items() for a in (v2.get("ids_alias") or [])}

    def res(x):
        s = set()
        while x in ALIAS and x not in s:
            s.add(x)
            x = ALIAS[x]
        return x

    grado = {}
    for nid, d in G.items():
        if d.get("deprecado"):
            continue
        for c in CAMPOS:
            for y in (d.get(c) or []):
                t = res(y)
                if t != nid:
                    grado[t] = grado.get(t, 0) + 1

    def cojas(x):
        n, det = 0, []
        for c in CAMPOS:
            for z in (G[x].get(c) or []):
                t = res(z)
                if t == x or t not in G:
                    continue
                if x not in (G[t].get(OPUESTO[c]) or []):
                    n += 1
                    det.append((c, t))
        return n, det

    for nid in (A, B):
        n, det = cojas(nid)
        print("  %-44s cableado (grado por P.1): %-4d | aristas propias sin"
              " reciproco: %d %s" % (nid, grado.get(nid, 0), n, det if det else ""))
    print("")
    print("  EL COSTE MEDIDO DE LA ELECCION: elegir a uno u otro solo pierde")
    print("  aristas si el que muere tiene aristas SIN RECIPROCO, porque las")
    print("  reciprocas las reescribe la simetrizacion de run_phase1, paso 5.")
    print("")
    print("  Y LA PRELACION, dicha antes de mirar: MANDA EL CONTENIDO. Este bloque")
    print("  se lee DESPUES del (c) y del (d), y si apunta al lado contrario del")
    print("  contenido, PIERDE. Se imprime para poder decir que no hizo falta.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
