# -*- coding: utf-8 -*-
"""vuelta45_verificar_opd01_opd02.py - LA VERIFICACION PUNTO POR PUNTO DE
OP-D-01 Y OP-D-02, MEDIDA. ESTRICTAMENTE DE SOLO LECTURA.

EXISTE POR EL ENCARGO DE LA VUELTA 45 (TAREA 1 punto 2), que a su vez viene del
acta de la vuelta 44, seccion 4 punto 3, linea 9688: el registro de OPERACION
HECHA de estas dos NO SE ADIVINA, SE VERIFICA, punto por punto contra su propio
campo `verificacion` de docs/plan/OPERACIONES.jsonl, exactamente como el cierre
de OP-D-06 lo modelo en la vuelta 44.

Y EXISTE POR LA REGLA 1 DE EJECUTOR.md, cuarto renglon: LA TABLA SE IMPRIME, NO
SE TECLEA. Todo lo que sale de aqui se lee HOY de dataset/nodos, de
docs/INTRA_DOMINIO_VEREDICTOS.jsonl y de docs/plan/OPERACIONES.jsonl. Ni una
cifra viene de un acta, de un reporte ni de una nota anterior (regla 2).

LOS CINCO PUNTOS, que son los MISMOS en las dos operaciones (leidos del fichero,
no tecleados aqui):

  1. Gate 0 verde
     -> NO lo mide este instrumento: Gate 0 se corre aparte y su salida se cita.
        Aqui se imprime como PUNTO DE CORRIDA EXTERNA para que no se confunda
        una medicion con una cita.
  2. los congelados <lista> se releen contra el superviviente y salen de la lista
     -> se mide: la clase de HOY de cada puesto, si su razon sigue abriendo con
        marca de congelado, y si la razon declara la relectura.
  3. cada nodo resultante dentro del estandar, o dentro de la excepcion de clase
     de OP-F-01
     -> se mide: los pasos_accionables de cada nodo VIVO de la nomina contra el
        estandar de 3 a 6.
  4. recomputo del cierre transitivo tras el acto (banco 9.21)
     -> se mide: la componente por la relacion gemelo (las A VIGENTES de hoy)
        de cada nodo de la nomina.
  5. el acto se leyo ENTERO antes de fundirse: cero pares internos sin veredicto
     -> se mide: TODOS los pares internos de la nomina, y cuantos no tienen fila
        en el archivo de veredictos.

Uso: python scripts/loop/vuelta45_verificar_opd01_opd02.py
"""
import io
import json
import os
import re
from itertools import combinations

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")

ESTANDAR = (3, 6)
OBJETIVO = ("OP-D-01", "OP-D-02")
# marca de congelado: la razon ABRE con una de estas
MARCA = re.compile(r"^(NO SE JUZGA|NO PUEDO JUZGAR|CONGELAD)", re.I)


def cargar_nodos():
    todos = {}
    for nombre in sorted(os.listdir(NODOS)):
        if nombre.endswith(".json"):
            d = json.loads(io.open(os.path.join(NODOS, nombre), encoding="utf-8").read())
            todos[d["node_id"]] = d
    return todos


def main():
    todos = cargar_nodos()
    vers = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
    por_puesto = dict((v["puesto_intra"], v) for v in vers)
    ops = [json.loads(l) for l in io.open(OPS, encoding="utf-8") if l.strip()]
    por_op = dict((o["id_op"], o) for o in ops)

    alias = {}
    for nid, d in todos.items():
        for a in (d.get("ids_alias") or []):
            alias[a] = nid

    def resolver(x):
        visto = set()
        while x in alias and x not in visto:
            visto.add(x)
            x = alias[x]
        return x

    def vivo(nid):
        d = todos.get(nid)
        return bool(d) and not (d.get("deprecado") or d.get("deprecated"))

    # el par por su par de nodos, resuelto por el resolutor (P.1)
    por_par = {}
    for v in vers:
        k = tuple(sorted((resolver(v["nodo_a"]), resolver(v["nodo_b"]))))
        por_par.setdefault(k, []).append(v)

    # cierre transitivo por la relacion gemelo, con las A VIGENTES de hoy
    ady = {}
    n_a = 0
    for v in vers:
        if v.get("clase") != "A":
            continue
        n_a += 1
        a, b = resolver(v["nodo_a"]), resolver(v["nodo_b"])
        ady.setdefault(a, set()).add(b)
        ady.setdefault(b, set()).add(a)

    def componente(sem):
        pila, visto = [sem], set()
        while pila:
            x = pila.pop()
            if x in visto:
                continue
            visto.add(x)
            for y in ady.get(x, ()):
                if y not in visto:
                    pila.append(y)
        return visto

    print("=" * 78)
    print("LA VERIFICACION DE OP-D-01 Y OP-D-02, PUNTO POR PUNTO, MEDIDA HOY")
    print("=" * 78)
    print()
    print("  pares de clase A vigentes en el archivo hoy: %d" % n_a)
    print("  nodos en dataset/nodos: %d (vivos %d)"
          % (len(todos), sum(1 for n in todos if vivo(n))))
    print("  el estandar de pasos que se aplica: de %d a %d" % ESTANDAR)
    print()
    print("  LOS PUESTOS QUE HOY SIGUEN ABRIENDO CON MARCA DE CONGELADO, en el")
    print("  archivo ENTERO (la lista contra la que se comprueba SALIR de ella):")
    abiertos = [v for v in vers if MARCA.match((v.get("razon") or "").strip())]
    for v in abiertos:
        print("    puesto %-6d clase %-2s  %s con %s"
              % (v["puesto_intra"], v.get("clase"), v["nodo_a"], v["nodo_b"]))
    print("    total: %d" % len(abiertos))

    for id_op in OBJETIVO:
        op = por_op[id_op]
        nomina = list(op.get("nodos") or [])
        print()
        print("=" * 78)
        print("%s  (%s, tipo %s)" % (id_op, op.get("fase"), op.get("tipo")))
        print("=" * 78)
        print("  nomina (%d): %s" % (len(nomina), ", ".join(nomina)))
        print("  superviviente declarado: %r" % op.get("superviviente"))
        print("  estado: %s | fecha_corte: %s | orden: %s"
              % (op.get("estado"), op.get("fecha_corte"), op.get("orden")))
        print("  aristas_nuevas: %r  (vacio = cero aristas que verificar aqui)"
              % (op.get("aristas_nuevas"),))
        print("  eliminar: %r" % (op.get("eliminar"),))
        print("  depende_de: %r | bloquea_a: %r"
              % (op.get("depende_de"), op.get("bloquea_a")))
        print("  nodos de la nomina AUSENTES del grafo: %d"
              % len([n for n in nomina if n not in todos]))
        print()

        for i, punto in enumerate(op["verificacion"], 1):
            print("  ---------------------------------------------------------------")
            print("  PUNTO %d, copiado del fichero: %s" % (i, punto))
            print("  ---------------------------------------------------------------")

            if "Gate 0" in punto:
                print("    CORRIDA EXTERNA, no medida por este instrumento.")
                print("    Se cita la salida de la corrida del ciclo, sellada aparte.")

            elif "congelados" in punto:
                puestos = [int(x) for x in re.findall(r"\b(\d{2,4})\b", punto)]
                print("    puestos leidos del propio punto: %s" % puestos)
                print()
                print("    %-7s %-5s %-42s %-42s %-9s %s"
                      % ("puesto", "clase", "nodo A", "nodo B", "congelado",
                         "la razon declara relectura"))
                fuera = 0
                for p in puestos:
                    v = por_puesto.get(p)
                    if not v:
                        print("    %-7d NO ESTA EN EL ARCHIVO" % p)
                        continue
                    r = (v.get("razon") or "").strip()
                    cong = "SI" if MARCA.match(r) else "NO"
                    if cong == "NO":
                        fuera += 1
                    rel = "SI" if ("REESCRITA" in r or "CORRECCION DECLARADA" in r) else "NO"
                    print("    %-7d %-5s %-42s %-42s %-9s %s"
                          % (p, v.get("clase"), v["nodo_a"], v["nodo_b"], cong, rel))
                print()
                print("    GUARDA: puestos del punto que SALIERON de la lista: %d de %d"
                      % (fuera, len(puestos)))
                print("    GUARDA: puestos del punto que SIGUEN congelados: %d"
                      % (len(puestos) - fuera))

            elif "estandar" in punto:
                print("    %-44s %-8s %-7s %s"
                      % ("nodo de la nomina", "estado", "pasos",
                         "contra el estandar %d a %d" % ESTANDAR))
                dentro = fuera = 0
                for n in nomina:
                    est = "VIVO" if vivo(n) else ("DEPR" if n in todos else "AUSENTE")
                    d = todos.get(n) or {}
                    k = len(d.get("pasos_accionables") or [])
                    if est != "VIVO":
                        marca = "no aplica (no es nodo resultante)"
                    elif ESTANDAR[0] <= k <= ESTANDAR[1]:
                        marca = "DENTRO"
                        dentro += 1
                    else:
                        delta = k - ESTANDAR[1] if k > ESTANDAR[1] else k - ESTANDAR[0]
                        marca = "FUERA por %+d" % delta
                        fuera += 1
                    print("    %-44s %-8s %-7s %s" % (n, est, k, marca))
                print()
                print("    GUARDA: nodos VIVOS de la nomina dentro del estandar: %d" % dentro)
                print("    GUARDA: nodos VIVOS de la nomina FUERA del estandar: %d" % fuera)

            elif "cierre transitivo" in punto:
                print("    %-44s %-8s %-6s %s"
                      % ("nodo de la nomina", "estado", "comp",
                         "miembros de su componente hoy"))
                crecidos = 0
                for n in nomina:
                    est = "VIVO" if vivo(n) else ("DEPR" if n in todos else "AUSENTE")
                    r = resolver(n)
                    comp = componente(r)
                    if len(comp) > 2:
                        crecidos += 1
                    print("    %-44s %-8s %-6d %s"
                          % (n, est, len(comp), ", ".join(sorted(comp))))
                print()
                print("    GUARDA: nodos de la nomina con componente de MAS de dos: %d" % crecidos)

            elif "ENTERO" in punto:
                print("    todos los pares internos de la nomina, resueltos por P.1:")
                print()
                print("    %-42s %-42s %-8s %s" % ("nodo A", "nodo B", "puesto", "clase"))
                sin = 0
                total = 0
                for a, b in combinations(nomina, 2):
                    total += 1
                    k = tuple(sorted((resolver(a), resolver(b))))
                    filas = por_par.get(k) or []
                    if not filas:
                        sin += 1
                        print("    %-42s %-42s %-8s %s" % (a, b, "NINGUNO", "SIN VEREDICTO"))
                    else:
                        for v in filas:
                            print("    %-42s %-42s %-8d %s"
                                  % (a, b, v["puesto_intra"], v.get("clase")))
                print()
                print("    GUARDA: pares internos de la nomina: %d" % total)
                print("    GUARDA: pares internos SIN veredicto en el archivo: %d" % sin)

            else:
                print("    PUNTO NO RECONOCIDO POR EL INSTRUMENTO: se imprime y no se mide.")
            print()

    print("=" * 78)
    print("FIN DE LA VERIFICACION MEDIDA")
    print("=" * 78)


main()
