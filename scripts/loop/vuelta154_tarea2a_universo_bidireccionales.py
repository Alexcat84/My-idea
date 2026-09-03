# -*- coding: utf-8 -*-
"""vuelta154_tarea2a_universo_bidireccionales.py . TAREA 2.a DE LA VUELTA 154.

MIDE EL UNIVERSO DE PARES BIDIRECCIONALES ENTRE NODOS VIVOS CON LAS CUATRO
VARAS DE LA TABLA DEL ACTA 153, SECCION 4.1, Y PUBLICA LAS CUATRO CIFRAS, NO
SOLO LA QUE CONVENGA.

  vara 1  fuentes VIVAS, solo `nodos_siguientes`  (la que la guarda usa hoy)
  vara 2  fuentes VIVAS, LOS DOS campos
  vara 3  TODAS las fuentes, solo `nodos_siguientes`
  vara 4  TODAS las fuentes, LOS DOS campos

INSTRUMENTO PROPIO, ESCRITO HOY. No importa `run_phase1` ni ningun modulo de la
casa: lee `dataset/nodos/*.json` a pelo y trae su PROPIO resolutor de alias,
escrito aqui. Si coincidiera con el de la casa por casualidad no probaria nada;
lo que se busca es una segunda medicion independiente que reproduzca (o no) la
del auditor.

EL CONTRASTE ESPERADO, escrito ANTES de correr (acta 153, 4.1): 153 / 154 / 155
/ 157 pares, con 0 / 1 / 2 / 4 sin cita. SI LAS CUATRO NO SALEN, SE PARA Y SE
TRAE: o la medicion del auditor o la mia esta mal, y eso se resuelve antes de
tocar la guarda.

EL RESOLUTOR (P.1, "todo conteo que toque ids pasa por el resolutor antes de
contar"): copia de `resolverId` de web/lib/engine/graph.ts, la misma que
`scripts/run_phase1.py` lleva dentro, reescrita aqui a mano. Un id vivo se
resuelve a si mismo; un id deprecado sigue su cadena de `ids_alias` hasta el
primer nodo vivo, y si no llega a ninguno devuelve el ultimo nodo real que
piso.

QUE ES UN PAR BIDIRECCIONAL, y la definicion es la misma para las cuatro varas:
tras resolver los dos extremos, A distinto de B, LOS DOS VIVOS, y existe la
direccion A hacia B Y la direccion B hacia A dentro del conjunto de direcciones
que la vara admite. Lo unico que cambia entre varas es QUE DIRECCIONES ENTRAN:
de que nodos (vivos o todos) y de que campos (uno o dos).

USO:  python scripts/loop/vuelta154_tarea2a_universo_bidireccionales.py
"""
import glob
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos", "*.json")
REGISTRO = os.path.join(RAIZ, "docs", "plan", "REGISTRO_DE_CITAS_OPC05.jsonl")

ESPERADO = [(153, 0), (154, 1), (155, 2), (157, 4)]


def cargar():
    todos = {}
    for ruta in sorted(glob.glob(NODOS)):
        d = json.load(io.open(ruta, encoding="utf-8"))
        nid = d.get("node_id") or os.path.splitext(os.path.basename(ruta))[0]
        todos[nid] = d
    return todos


def tabla_de_alias(todos):
    alias_de = {}
    for nid, n in todos.items():
        for a in n.get("ids_alias") or []:
            if a != nid:
                alias_de[a] = nid
    return alias_de


def hacer_resolutor(todos, alias_de):
    def resolver(nid):
        n = todos.get(nid)
        if n is not None and not n.get("deprecado"):
            return nid
        visto = {nid}
        cur = nid
        ultimo_real = nid if n is not None else None
        while cur in alias_de:
            cur = alias_de[cur]
            if cur in visto:
                break
            visto.add(cur)
            c = todos.get(cur)
            if c is None:
                continue
            ultimo_real = cur
            if not c.get("deprecado"):
                return cur
        return ultimo_real
    return resolver


def direcciones(todos, resolver, vivos, solo_fuentes_vivas, campos):
    """Conjunto de direcciones (A, B) tras resolver, con los DOS extremos vivos
    y A distinto de B. `solo_fuentes_vivas` restringe los nodos de partida;
    `campos` dice de que listas se leen los destinos."""
    dirs = set()
    for nid in sorted(todos):
        if solo_fuentes_vivas and todos[nid].get("deprecado"):
            continue
        for campo in campos:
            for dest in todos[nid].get(campo) or []:
                if dest not in todos:
                    continue  # referencia rota: la caza el chequeo de enlaces
                a, b = resolver(nid), resolver(dest)
                if a and b and a != b and a in vivos and b in vivos:
                    if campo == "nodos_previos":
                        # `nodos_previos` declara la arista EN SENTIDO
                        # CONTRARIO: "B es previo mio" es la direccion B -> A.
                        # Meterla como A -> B invertiria la mitad del universo.
                        dirs.add((b, a))
                    else:
                        dirs.add((a, b))
    return dirs


def pares(dirs):
    return sorted({tuple(sorted(p)) for p in dirs if (p[1], p[0]) in dirs})


def citados():
    if not os.path.exists(REGISTRO):
        return set()
    s = set()
    for linea in io.open(REGISTRO, encoding="utf-8"):
        if not linea.strip():
            continue
        p = json.loads(linea).get("par") or []
        if len(p) == 2:
            s.add(tuple(sorted(p)))
    return s


def main():
    todos = cargar()
    alias_de = tabla_de_alias(todos)
    resolver = hacer_resolutor(todos, alias_de)
    vivos = {n for n in todos if not todos[n].get("deprecado")}
    cit = citados()

    print("=" * 92)
    print("VUELTA 154, TAREA 2.a: EL UNIVERSO DE PARES BIDIRECCIONALES, CON LAS CUATRO VARAS")
    print("=" * 92)
    print("INSTRUMENTO PROPIO, escrito hoy, sin importar codigo de la casa.")
    print("Nodos leidos de dataset/nodos/*.json: %d | vivos %d | deprecados %d"
          % (len(todos), len(vivos), len(todos) - len(vivos)))
    print("Nodos con ids_alias: %d | entradas en la tabla de alias: %d"
          % (sum(1 for n in todos.values() if n.get("ids_alias")), len(alias_de)))
    print("Registro de citas: %s, %d par(es) citado(s)"
          % ("docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl", len(cit)))
    print("")

    VARAS = [
        ("1", "fuentes VIVAS, solo nodos_siguientes (la de la guarda de hoy)",
         True, ("nodos_siguientes",)),
        ("2", "fuentes VIVAS, LOS DOS campos",
         True, ("nodos_siguientes", "nodos_previos")),
        ("3", "TODAS las fuentes, solo nodos_siguientes",
         False, ("nodos_siguientes",)),
        ("4", "TODAS las fuentes, LOS DOS campos",
         False, ("nodos_siguientes", "nodos_previos")),
    ]

    resultados = []
    for num, nombre, solo_vivas, campos in VARAS:
        d = direcciones(todos, resolver, vivos, solo_vivas, campos)
        P = pares(d)
        sin = [p for p in P if p not in cit]
        resultados.append((num, nombre, len(d), P, sin))

    print("| vara | que admite | direcciones | pares bidireccionales | sin cita |")
    print("|---|---|---:|---:|---:|")
    for num, nombre, nd, P, sin in resultados:
        print("| %s | %s | %d | %d | %d |" % (num, nombre, nd, len(P), len(sin)))
    print("")

    print("LOS PARES SIN CITA, NOMBRADOS UNO A UNO POR VARA (nunca resumidos):")
    for num, nombre, nd, P, sin in resultados:
        print("  vara %s (%s): %d sin cita" % (num, nombre, len(sin)))
        for a, b in sin:
            print("      %s <-> %s" % (a, b))
    print("")

    print("EL CONTRASTE CONTRA LA TABLA DEL ACTA 153, SECCION 4.1")
    print("(cifras del auditor, citadas como contraste, NO como fuente):")
    print("| vara | pares esperados | pares medidos hoy | sin cita esperados | sin cita medidos | cuadra |")
    print("|---|---:|---:|---:|---:|---|")
    cuadran = 0
    for (num, nombre, nd, P, sin), (ep, es) in zip(resultados, ESPERADO):
        ok = (len(P) == ep and len(sin) == es)
        cuadran += 1 if ok else 0
        print("| %s | %d | %d | %d | %d | %s |"
              % (num, ep, len(P), es, len(sin), "SI" if ok else "NO"))
    print("")
    print("CIFRA varas que cuadran con el acta 153: %d comprobaciones" % cuadran)
    print("CIFRA pares con la vara de la guarda de hoy: %d pares" % len(resultados[0][3]))
    print("CIFRA pares con la vara de los dos campos sobre fuentes vivas: %d pares"
          % len(resultados[1][3]))
    print("CIFRA pares sin cita con la vara de los dos campos sobre fuentes vivas: %d pares"
          % len(resultados[1][4]))
    print("")

    if cuadran == 4:
        print("LAS CUATRO CUADRAN. La medicion del auditor reproduce con instrumento")
        print("propio y no hay nada que parar.")
    else:
        print("PARADA: %d de 4 varas NO cuadran con el acta 153. No se toca la guarda"
              % (4 - cuadran))
        print("hasta que se resuelva cual de las dos mediciones esta mal.")

    print("")
    print("=" * 92)
    print("LA ARITMETICA QUE EL ACTA 153, 4.3 USA PARA CERRAR EL AGUJERO, RE MEDIDA AQUI")
    print("=" * 92)
    # Relaciones de ida y vuelta DECLARADAS DENTRO DE UN NODO VIVO: el nodo trae
    # el mismo destino resuelto en sus DOS listas.
    destinos = 0
    nodos_con = 0
    mutuas = 0
    solo_un_lado = []
    for nid in sorted(vivos):
        n = todos[nid]
        sig = {resolver(d) for d in (n.get("nodos_siguientes") or []) if d in todos}
        prev = {resolver(d) for d in (n.get("nodos_previos") or []) if d in todos}
        comunes = {d for d in (sig & prev) if d and d != nid and d in vivos}
        if comunes:
            nodos_con += 1
            destinos += len(comunes)
        for d in sorted(comunes):
            m = todos[d]
            sig_d = {resolver(x) for x in (m.get("nodos_siguientes") or []) if x in todos}
            prev_d = {resolver(x) for x in (m.get("nodos_previos") or []) if x in todos}
            if nid in (sig_d & prev_d):
                mutuas += 1
            else:
                solo_un_lado.append((nid, d))
    print("Nodos VIVOS que declaran ida y vuelta dentro de sus dos listas: %d" % nodos_con)
    print("Destinos asi declarados: %d" % destinos)
    print("De esos destinos, MUTUOS (los declaran los dos nodos): %d, o sea %d par(es)"
          % (mutuas, mutuas // 2))
    print("DECLARADOS POR UN SOLO LADO: %d" % len(solo_un_lado))
    for a, b in solo_un_lado:
        print("    %s declara ida y vuelta hacia %s, y %s no se la devuelve" % (a, b, b))
    print("")
    print("CIFRA destinos de ida y vuelta declarados dentro de un nodo vivo: %d direcciones"
          % destinos)
    print("CIFRA nodos vivos que los declaran: %d nodos" % nodos_con)
    print("CIFRA destinos declarados por un solo lado: %d direcciones" % len(solo_un_lado))


main()
