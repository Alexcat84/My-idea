# -*- coding: utf-8 -*-
"""fijar_tramo_de_opu02.py . COTEJA LA NOMINA FIJADA DE OP-U-02 CONTRA EL GRAFO
DE HOY Y FIJA EL FICHERO DEL TRAMO. NO FUNDE NI UN ACTO.

NOMBRE ESTABLE, y no lleva vuelta: la nomina entra por --nomina, las componentes
del dia por --componentes y el destino por --salida. Es la vara del acta 58,
pregunta 4, la misma con la que nacieron abrir_tramo_de_opu01.py y
abrir_universo_de_opu02.py.

HERMANO de scripts/loop/abrir_tramo_de_opu01.py, NO sucesor, y la diferencia es
de forma del tramo y no de aritmetica: aquel corta CINCUENTA actos de una nomina
que no cabe entera y por eso necesita dos lecturas, guarda de prefijo y guarda de
solape entre tramos. AQUI NO HAY NADA QUE CORTAR. El acta 63 (pregunta 5) dejo
adjudicado que el tramo es PREFIJO CON TOPE y no minimo, y los actos que abren
CABEN BAJO EL TOPE DE CINCUENTA: el tramo es UNO, es TODO EL UNIVERSO, y se
declara TRAMO UNICO Y FINAL POR AGOTAMIENTO al abrirlo. Un instrumento que
partiera esto en tramos estaria inventando un corte que la doctrina no pide.

EL FICHERO QUE ESCRIBE NO SE LLAMA TRAMO<N>_V<vuelta>.jsonl A PROPOSITO: ese es
el patron con el que abrir_tramo_de_opu01.py DESCUBRE los tramos ya fijados de
OP-U-01 (su RE_FIJADO), y meterle dentro un tramo de OTRA operacion le movia la
cuenta del siguiente tramo sin que nadie lo notara. Fallar ruidoso empieza por no
fabricar la trampa.

LAS GUARDAS, y ninguna tiene rama por defecto. Si una sola cae, NO se escribe el
fichero y el instrumento PARA con la medicion delante:

  1. IDENTIDAD DE LA NOMINA CONTRA LAS COMPONENTES DE HOY. Cada fila de la nomina
     tiene que casar con una componente ABIERTA de hoy por CONJUNTO DE MIEMBROS
     RESUELTOS (P.1), no por posicion ni por tamano. Una nomina que ya no describe
     el grafo no se fija: se trae.
  2. NINGUN MIEMBRO QUE ABRE ESTA DEPRECADO HOY. Un acto cuyo miembro ya fue
     absorbido por otra operacion no es un acto libre.
  3. LOS QUE QUEDAN FUERA SIGUEN FUERA. Cada fila con abre false tiene que seguir
     teniendo dueno de MESA o DESTEJIDO medido hoy, y no heredado del fichero.
  4. EL TOPE. Los que abren tienen que caber bajo el tope de cincuenta; si no
     caben, el tramo NO es unico y este instrumento no sirve.
  5. LA SUMA CIERRA. abren mas fuera igual al total de filas de la nomina.

DE SOLO LECTURA sobre el dataset. Escribe UN fichero, el del tramo, y nada mas.
No sella un plan, no elige superviviente y no funde nada.

Uso:
  python scripts/loop/fijar_tramo_de_opu02.py
      --nomina docs/loop/NOMINA_OPU02_V63.jsonl
      --componentes docs/loop/_v64_componentes_cierre.jsonl
      --salida docs/loop/TRAMO_UNICO_OPU02_V64.jsonl [--simular]
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
TOPE = 50
MESA_O_DESTEJIDO = ("MESA", "DESTEJIDO")


def cargar_alias():
    alias, dep = {}, {}
    for f in sorted(os.listdir(NODOS)):
        if not f.endswith(".json"):
            continue
        d = json.load(io.open(os.path.join(NODOS, f), encoding="utf-8"))
        nid = d["node_id"]
        dep[nid] = bool(d.get("deprecado") or d.get("deprecated"))
        for x in (d.get("ids_alias") or []):
            alias.setdefault(x, nid)
    return alias, dep


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nomina", required=True)
    ap.add_argument("--componentes", required=True)
    ap.add_argument("--salida", required=True)
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    alias, dep = cargar_alias()

    def res(x):
        v = set()
        while x in alias and x not in v:
            v.add(x)
            x = alias[x]
        return x

    nomina = [json.loads(l) for l in
              io.open(os.path.join(RAIZ, a.nomina.replace("/", os.sep)), encoding="utf-8")
              if l.strip()]
    comps = [json.loads(l) for l in
             io.open(os.path.join(RAIZ, a.componentes.replace("/", os.sep)), encoding="utf-8")
             if l.strip()]
    abiertas = [c for c in comps if c.get("estado") == "ABIERTO"]
    ops = [json.loads(l) for l in io.open(OPERACIONES, encoding="utf-8") if l.strip()]

    print("=" * 78)
    print("EL TRAMO UNICO DE OP-U-02: LA NOMINA COTEJADA CONTRA EL GRAFO DE HOY")
    print("  nomina fijada : %s (%d filas)" % (a.nomina, len(nomina)))
    print("  componentes   : %s (%d, de ellas %d ABIERTAS)"
          % (a.componentes, len(comps), len(abiertas)))
    print("  alias del arbol de hoy: %d | nodos deprecados: %d"
          % (len(alias), sum(1 for v in dep.values() if v)))
    print("=" * 78)

    fallos = []
    abren = [f for f in nomina if f.get("abre")]
    fuera = [f for f in nomina if not f.get("abre")]
    print()
    print("  la nomina dice: %d abren, %d quedan fuera, %d en total"
          % (len(abren), len(fuera), len(nomina)))
    if len(abren) + len(fuera) != len(nomina):
        fallos.append("la suma de abren y fuera no da el total de la nomina")

    print()
    print("--- GUARDA 1: IDENTIDAD CONTRA LAS COMPONENTES ABIERTAS DE HOY ---")
    por_conjunto = {}
    for c in abiertas:
        por_conjunto[frozenset(res(m) for m in c["miembros"])] = c
    calzan, no_calzan = 0, []
    for f in nomina:
        k = frozenset(res(m) for m in f["miembros"])
        if k in por_conjunto:
            calzan += 1
        else:
            no_calzan.append(f)
    print("   filas que calzan con una componente ABIERTA de hoy: %d de %d"
          % (calzan, len(nomina)))
    for f in no_calzan:
        print("      NO CALZA (tamano %d, orden_universo %s): %s"
              % (f.get("tamano"), f.get("orden_universo"), ", ".join(f["miembros"][:6])))
    if no_calzan:
        fallos.append("%d fila(s) de la nomina ya no describen una componente ABIERTA de hoy"
                      % len(no_calzan))
    sobran = len(abiertas) - calzan
    print("   componentes ABIERTAS de hoy sin fila en la nomina: %d" % sobran)
    if sobran:
        vistos = {frozenset(res(m) for m in f["miembros"]) for f in nomina}
        for c in abiertas:
            if frozenset(res(m) for m in c["miembros"]) not in vistos:
                print("      SIN FILA (tamano %d): %s"
                      % (len(c["miembros"]), ", ".join(c["miembros"][:6])))
        fallos.append("hay %d componente(s) ABIERTA(s) de hoy sin fila en la nomina" % sobran)

    print()
    print("--- GUARDA 2: NINGUN MIEMBRO QUE ABRE ESTA DEPRECADO HOY ---")
    muertos = []
    for f in abren:
        for m in f["miembros"]:
            if dep.get(m, False):
                muertos.append((f.get("orden_universo"), m))
    print("   miembros deprecados entre los %d actos que abren: %d" % (len(abren), len(muertos)))
    for o, m in muertos:
        print("      orden_universo %s -> %s DEPRECADO (resuelve a %s)" % (o, m, res(m)))
    if muertos:
        fallos.append("%d miembro(s) de actos que abren estan deprecados hoy" % len(muertos))

    print()
    print("--- GUARDA 3: LOS QUE QUEDAN FUERA SIGUEN TENIENDO DUENO HOY ---")
    duenos_por_nodo = {}
    for o in ops:
        if not any(t in (o.get("tipo") or "").upper() for t in MESA_O_DESTEJIDO):
            continue
        campos = list(o.get("nodos") or []) + list(o.get("eliminar") or [])
        if o.get("superviviente"):
            campos.append(o["superviviente"])
        for x in campos:
            duenos_por_nodo.setdefault(res(x), set()).add(o["id_op"])
    sin_dueno = []
    for f in fuera:
        ds = set()
        for m in f["miembros"]:
            ds |= duenos_por_nodo.get(res(m), set())
        print("   orden_universo %-3s tamano %-3d duenos de mesa o destejido HOY: %s"
              % (f.get("orden_universo"), f.get("tamano"),
                 ", ".join(sorted(ds)) or "NINGUNO"))
        print("      la nomina decia: %s"
              % (", ".join(f.get("duenos_mesa_o_destejido") or []) or "NINGUNO"))
        if not ds:
            sin_dueno.append(f)
    print("   los %d de fuera siguen con dueno: %s"
          % (len(fuera), "SI" if not sin_dueno else "NO, %d sin dueno" % len(sin_dueno)))
    if sin_dueno:
        fallos.append("%d acto(s) que la nomina deja fuera ya NO tienen dueno hoy"
                      % len(sin_dueno))

    print()
    print("--- GUARDA 4: EL TOPE, Y POR QUE EL TRAMO ES UNO ---")
    print("   actos que abren: %d | tope del tramo: %d | caben: %s"
          % (len(abren), TOPE, "SI" if len(abren) <= TOPE else "NO"))
    print("   El acta 63, pregunta 5, adjudica que el tramo es PREFIJO CON TOPE y")
    print("   NO minimo. Como los %d caben bajo el tope, el prefijo es el universo" % len(abren))
    print("   ENTERO: TRAMO UNICO Y FINAL POR AGOTAMIENTO, declarado al abrirlo.")
    if len(abren) > TOPE:
        fallos.append("los %d que abren NO caben bajo el tope de %d: el tramo no es unico"
                      % (len(abren), TOPE))

    nodos_abren = sum(len(f["miembros"]) for f in abren)
    nodos_fuera = sum(len(f["miembros"]) for f in fuera)
    print()
    print("   nodos en los actos que abren : %d" % nodos_abren)
    print("   nodos en los que quedan fuera: %d" % nodos_fuera)
    print("   por tamano de acto: %s"
          % dict(sorted({t: sum(1 for f in abren if len(f["miembros"]) == t)
                         for t in sorted({len(f["miembros"]) for f in abren})}.items())))

    print()
    print("=" * 78)
    if fallos:
        print("ROJO, %d fallo(s), y NO se escribe el fichero del tramo:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        print()
        print("PARADA: la medicion de hoy no calza con la nomina fijada.")
        return 1

    filas = sorted(abren, key=lambda f: f.get("orden_universo") or 0)
    if a.simular:
        print("MODO SIMULAR: no se escribe el fichero. Serian %d filas." % len(filas))
        print("=" * 78)
        return 0
    destino = os.path.join(RAIZ, a.salida.replace("/", os.sep))
    with io.open(destino, "w", encoding="utf-8", newline=NL) as fh:
        for f in filas:
            g = dict(f)
            g["tramo"] = "UNICO Y FINAL POR AGOTAMIENTO"
            g["operacion"] = "OP-U-02"
            fh.write(json.dumps(g, ensure_ascii=False) + NL)
    print("TRAMO FIJADO: %s, %d filas en su orden_universo."
          % (a.salida, len(filas)))
    print("NI UN ACTO SE FUNDE AQUI: este fichero solo dice quien entra y en que orden.")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
