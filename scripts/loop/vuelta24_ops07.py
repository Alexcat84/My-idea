"""OP-S-07 por su letra nueva (correccion declarada del 14 ago 2026, camino A).

Retira 66 enlaces: los 33 vivos que resuelven al propio nodo MAS sus 33
reciprocas literales en el gemelo deprecado que las proyecta de vuelta.
Las 48 alias contra alias del lado deprecado NO se tocan (censadas como inertes).

Modos:
  --simular    P.7: copia en memoria, CERO escrituras. Imprime el censo entero.
  --ejecutar   escribe sobre dataset/nodos, y solo sobre nodos_previos/siguientes.
  --verificar  mide contra HEAD: enlaces retirados, campos movidos, auto aristas.

Todo conteo pasa por el resolutor ANTES de contar (P.1).
"""

import argparse
import collections
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")


def cargar(directorio=NODOS):
    nodos = {}
    for nombre in sorted(os.listdir(directorio)):
        if not nombre.endswith(".json"):
            continue
        with open(os.path.join(directorio, nombre), encoding="utf-8") as fh:
            d = json.load(fh)
        nid = d.get("node_id") or nombre[:-5]
        nodos[nid] = d
    return nodos


def mapa_de_alias(nodos):
    """Copia fiel de mapaDeAlias en web/lib/engine/graph.ts."""
    m = {}
    for nid, n in nodos.items():
        for a in n.get("ids_alias") or []:
            if a != nid:
                m[a] = nid
    return m


def resolver(nid, nodos, alias):
    """Copia fiel de resolverId en web/lib/engine/graph.ts."""
    n = nodos.get(nid)
    if n is not None and not n.get("deprecado"):
        return nid
    visto = {nid}
    cur = nid
    ultimo_real = nid if n is not None else None
    while cur in alias:
        cur = alias[cur]
        if cur in visto:
            break
        visto.add(cur)
        c = nodos.get(cur)
        if c is None:
            continue
        ultimo_real = cur
        if not c.get("deprecado"):
            return cur
    return ultimo_real


CAMPOS = ("nodos_previos", "nodos_siguientes")
OPUESTO = {"nodos_previos": "nodos_siguientes", "nodos_siguientes": "nodos_previos"}


def censo(nodos):
    """Devuelve (vivas, reciprocas, inertes).

    vivas:      (nid_vivo, campo, destino) donde resolver(destino) == nid_vivo
    reciprocas: (nid_deprecado, campo_opuesto, nid_vivo) la vista literal gemela
    inertes:    (nid_deprecado, campo, destino) alias contra alias del mismo
                superviviente, que NO proyectan sobre vivos
    """
    alias = mapa_de_alias(nodos)
    vivas, reciprocas, inertes = [], [], []
    for nid, n in nodos.items():
        deprecado = bool(n.get("deprecado"))
        propio = resolver(nid, nodos, alias)
        for campo in CAMPOS:
            for dest in n.get(campo) or []:
                if dest not in nodos:
                    continue
                r = resolver(dest, nodos, alias)
                if not deprecado:
                    if r == nid:
                        vivas.append((nid, campo, dest))
                elif r == propio and dest != nid:
                    inertes.append((nid, campo, dest))
    # la reciproca literal de cada viva: el gemelo deprecado que la proyecta
    for nid, campo, dest in vivas:
        reciprocas.append((dest, OPUESTO[campo], nid))
    # las reciprocas NO son inertes: se restan del censo de inertes
    setrec = set(reciprocas)
    inertes = [x for x in inertes if x not in setrec]
    return vivas, reciprocas, inertes


def contar_enlaces(nodos):
    total = 0
    for n in nodos.values():
        for campo in CAMPOS:
            total += len(n.get(campo) or [])
    return total


def imprimir_censo(nodos, vivas, reciprocas, inertes):
    alias = mapa_de_alias(nodos)
    vivos = [k for k, v in nodos.items() if not v.get("deprecado")]
    dep = [k for k, v in nodos.items() if v.get("deprecado")]
    print("NODOS: %d  (vivos %d, deprecados %d)" % (len(nodos), len(vivos), len(dep)))
    print("ENLACES (previos + siguientes): %d" % contar_enlaces(nodos))
    print()
    print("== A) LAS VIVAS: enlace de nodo VIVO que resuelve al PROPIO nodo ==")
    print("enlaces: %d   nodos: %d" % (len(vivas), len(set(v[0] for v in vivas))))
    directas = [v for v in vivas if v[2] == v[0]]
    print("directas (dest == nid literal): %d   via alias: %d"
          % (len(directas), len(vivas) - len(directas)))
    por_nodo = collections.Counter(v[0] for v in vivas)
    for nid, c in sorted(por_nodo.items(), key=lambda x: (-x[1], x[0])):
        detalle = ", ".join("%s:%s" % (cp.replace("nodos_", ""), d)
                            for n2, cp, d in vivas if n2 == nid)
        print("  %-45s %d  [%s]" % (nid, c, detalle))
    print()
    print("== B) LAS RECIPROCAS LITERALES en el gemelo deprecado ==")
    print("enlaces: %d   nodos: %d" % (len(reciprocas), len(set(r[0] for r in reciprocas))))
    faltantes = []
    for dnid, campo, vid in reciprocas:
        if vid not in (nodos[dnid].get(campo) or []):
            faltantes.append((dnid, campo, vid))
    print("reciprocas que NO estan escritas en el gemelo: %d" % len(faltantes))
    for f in faltantes:
        print("  FALTA: %s" % (f,))
    print()
    print("== C) LAS ALIAS CONTRA ALIAS, censadas como INERTES (no se tocan) ==")
    print("enlaces: %d   nodos: %d" % (len(inertes), len(set(i[0] for i in inertes))))
    por_dep = collections.Counter(i[0] for i in inertes)
    for nid, c in sorted(por_dep.items(), key=lambda x: (-x[1], x[0]))[:12]:
        print("  %-45s %d" % (nid, c))
    print()
    print("== LA PARTICION ==")
    todo_dep = len(reciprocas) + len(inertes)
    print("lado deprecado bajo criterio B: %d = %d reciprocas + %d inertes"
          % (todo_dep, len(reciprocas), len(inertes)))
    solape = set(reciprocas) & set(inertes)
    print("solape entre las dos mitades: %d" % len(solape))
    print()
    ficheros = set(v[0] for v in vivas) | set(r[0] for r in reciprocas)
    print("== LO QUE OP-S-07 RETIRA ==")
    print("entradas a retirar: %d  (%d vivas + %d reciprocas)"
          % (len(vivas) + len(reciprocas), len(vivas), len(reciprocas)))
    print("ficheros tocados: %d" % len(ficheros))
    print()
    ej = [v for v in vivas if v[0] == "analisis_flujo_de_valor"]
    print("EJEMPLAR ESCRITO EN EL PLAN: analisis_flujo_de_valor -> %s" % (ej,))
    for _, _, d in ej:
        print("  %s existe: %s  deprecado: %s  resuelve a: %s"
              % (d, d in nodos, bool(nodos.get(d, {}).get("deprecado")),
                 resolver(d, nodos, alias)))


def simular():
    nodos = cargar()
    vivas, reciprocas, inertes = censo(nodos)
    imprimir_censo(nodos, vivas, reciprocas, inertes)
    print()
    print("== SIMULACION (P.7): copia en memoria, CERO escrituras ==")
    copia = json.loads(json.dumps(nodos))
    antes = contar_enlaces(copia)
    quitados = 0
    for nid, campo, dest in vivas + reciprocas:
        lista = copia[nid].get(campo) or []
        if dest in lista:
            lista.remove(dest)
            copia[nid][campo] = lista
            quitados += 1
    despues = contar_enlaces(copia)
    print("enlaces antes: %d   despues: %d   baja: %d" % (antes, despues, antes - despues))
    print("entradas efectivamente quitadas: %d" % quitados)
    v2, r2, i2 = censo(copia)
    print("auto aristas de nodo VIVO tras resolver, en la copia: %d en %d nodos"
          % (len(v2), len(set(x[0] for x in v2))))
    print("inertes en la copia (no se tocaron): %d" % len(i2))
    print("SIMULACION OK" if (antes - despues) == 66 and len(v2) == 0
          else "SIMULACION NO CUADRA")


def ejecutar():
    nodos = cargar()
    vivas, reciprocas, inertes = censo(nodos)
    todo = vivas + reciprocas
    print("A RETIRAR: %d entradas (%d vivas + %d reciprocas)"
          % (len(todo), len(vivas), len(reciprocas)))
    porfichero = collections.defaultdict(list)
    for nid, campo, dest in todo:
        porfichero[nid].append((campo, dest))
    escritos = 0
    quitados = 0
    for nid, entradas in sorted(porfichero.items()):
        ruta = os.path.join(NODOS, nid + ".json")
        with open(ruta, encoding="utf-8") as fh:
            bruto = fh.read()
        d = json.loads(bruto)
        cambio = False
        for campo, dest in entradas:
            lista = d.get(campo) or []
            if dest in lista:
                lista.remove(dest)
                d[campo] = lista
                cambio = True
                quitados += 1
            else:
                print("  AVISO: %s no tenia %s en %s" % (nid, dest, campo))
        if cambio:
            # formato IDENTICO al save_node del validador (scripts/run_phase1.py
            # linea 103): indent 2, ensure_ascii False y SIN salto final.
            with open(ruta, "w", encoding="utf-8") as fh:
                json.dump(d, fh, ensure_ascii=False, indent=2)
            escritos += 1
    print("FICHEROS ESCRITOS: %d" % escritos)
    print("ENTRADAS QUITADAS: %d" % quitados)
    despues = cargar()
    print("ENLACES: %d -> %d (baja %d)"
          % (contar_enlaces(nodos), contar_enlaces(despues),
             contar_enlaces(nodos) - contar_enlaces(despues)))


def _head(ruta_rel):
    try:
        return subprocess.run(["git", "show", "HEAD:" + ruta_rel],
                              cwd=RAIZ, capture_output=True, check=True).stdout.decode("utf-8")
    except subprocess.CalledProcessError:
        return None


def verificar():
    nodos = cargar()
    vivas, reciprocas, inertes = censo(nodos)
    print("== VERIFICACION DE OP-S-07, linea por linea de su campo verificacion ==")
    print()
    print("1) ningun nodo VIVO se cita a si mismo, NI directamente NI tras resolver")
    print("   auto aristas de vivos tras resolver: %d en %d nodos  -> %s"
          % (len(vivas), len(set(v[0] for v in vivas)),
             "VERDE" if not vivas else "ROJO"))
    for v in vivas[:20]:
        print("     %s" % (v,))
    print()
    print("2) los 66 enlaces retirados y ningun otro: el conteo de aristas baja en 66")
    cambiados = 0
    retirados = 0
    otros_campos = 0
    for nid, d in nodos.items():
        bruto = _head("dataset/nodos/%s.json" % nid)
        if bruto is None:
            print("     NODO NUEVO (no esta en HEAD): %s" % nid)
            continue
        viejo = json.loads(bruto)
        difcampos = []
        for k in set(list(viejo.keys()) + list(d.keys())):
            if viejo.get(k) != d.get(k):
                difcampos.append(k)
        if not difcampos:
            continue
        cambiados += 1
        for k in difcampos:
            if k in CAMPOS:
                a = viejo.get(k) or []
                b = d.get(k) or []
                quitados = [x for x in a if x not in b]
                anadidos = [x for x in b if x not in a]
                retirados += len(quitados)
                if anadidos:
                    print("     ANADIDO (no debia): %s %s %s" % (nid, k, anadidos))
            else:
                otros_campos += 1
                print("     CAMPO DISTINTO DE previos/siguientes: %s . %s" % (nid, k))
    print("   ficheros con diferencia real contra HEAD: %d" % cambiados)
    print("   ENLACES RETIRADOS (contra HEAD): %d  -> %s"
          % (retirados, "VERDE" if retirados == 66 else "ROJO"))
    print("   CAMPOS DISTINTOS DE previos/siguientes QUE SE MOVIERON: %d  -> %s"
          % (otros_campos, "VERDE" if otros_campos == 0 else "ROJO"))
    print()
    print("3) ids_alias intactos en los nodos tocados")
    malos = 0
    for nid in sorted(set(v[0] for v in vivas) | set(r[0] for r in reciprocas)):
        pass
    for nid, d in nodos.items():
        bruto = _head("dataset/nodos/%s.json" % nid)
        if bruto is None:
            continue
        if (json.loads(bruto).get("ids_alias") or []) != (d.get("ids_alias") or []):
            malos += 1
            print("     ids_alias MOVIDO: %s" % nid)
    print("   ids_alias movidos: %d  -> %s" % (malos, "VERDE" if malos == 0 else "ROJO"))
    print()
    print("4) las 48 alias contra alias siguen intactas (censadas, no tocadas)")
    print("   inertes hoy: %d en %d nodos deprecados"
          % (len(inertes), len(set(i[0] for i in inertes))))
    print()
    print("5) conteo de aristas del grafo")
    print("   enlaces hoy: %d" % contar_enlaces(nodos))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--simular", action="store_true")
    p.add_argument("--ejecutar", action="store_true")
    p.add_argument("--verificar", action="store_true")
    a = p.parse_args()
    if a.simular:
        simular()
    elif a.ejecutar:
        ejecutar()
    elif a.verificar:
        verificar()
    else:
        p.print_help()
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
