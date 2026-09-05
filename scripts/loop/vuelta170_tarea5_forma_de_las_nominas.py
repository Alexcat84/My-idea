# -*- coding: utf-8 -*-
r"""vuelta170_tarea5_forma_de_las_nominas.py . TAREA 5.a de la vuelta 170.

RE ESCRIBE LA **FORMA** DE LAS TRES NOMINAS AFECTADAS POR LA SEGUNDA TANDA DE
`OP-L-02`, CON SU COBERTURA AL LADO (banco `9.26`) Y CON EL RESOLUTOR DELANTE
(`P.1`), POR ADICION Y SIN BORRAR LA FORMA VIEJA.

POR QUE NACE. La clausula 1 de `OP-L-02` dice, verbatim: *"las tres nominas
afectadas quedan con cobertura COMPLETA y su forma reescrita"*. La cobertura YA
esta (medida en la vuelta 169 y remedida aqui); **lo que faltaba es LA FORMA
REESCRITA**, y esa es la tarea.

LAS TRES NOMINAS, Y NO SE TECLEAN: son las tres que la segunda tanda cerro, y su
sede es `docs/plan/INVENTARIO.jsonl`. El instrumento las localiza por nombre y
CAE EN ROJO si alguna no aparece exactamente una vez.

LO QUE EL RESOLUTOR SEPARA, Y ES LA MITAD QUE HACE FALTA. Una forma escrita el
11 ago 2026 habla de una nomina que ese dia tenia N miembros vivos. Desde
entonces **la campana ha fundido**, y hay nominas que HOY no tienen los mismos
nodos vivos que entonces. Contar sin resolver haria que una nomina fundida
siguiera pareciendo entera, que es exactamente lo que `P.1` existe para impedir.
Asi que cada nomina se mide **dos veces**: como esta escrita, y como queda tras
resolver.

LAS DOS SEDES DE LECTURA NO SE MEZCLAN, y van contadas aparte: la COLA
(`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`) y las LECTURAS DIRIGIDAS, que no entran
en la cola y no mueven su marcador, y que se escriben de DOS formas (cabecera
con numero `LD-nn` y fila de tabla sin numero, que es como estan las 16 de la
segunda tanda; ver la PARADA de la TAREA 4.a).

Y `9.16` VIAJA CON CADA FORMA QUE SE ESCRIBE: **EL SUB-PURO ES UNA PROMESA, NO
UN RESULTADO.** Ninguna forma nueva se escribe como final si le falta un par.

CERO CLAVES NUEVAS DE ESQUEMA: se escribe DENTRO de los campos `forma` y
`cobertura` que ya existen, con el texto viejo entero delante.

USO:
  python scripts/loop/vuelta170_tarea5_forma_de_las_nominas.py
  python scripts/loop/vuelta170_tarea5_forma_de_las_nominas.py --aplicar
"""
import collections
import io
import itertools
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
INVENTARIO = os.path.join(RAIZ, "docs", "plan", "INVENTARIO.jsonl")
MJS = os.path.join(RAIZ, "scripts", "vuelta16_generar_actos.mjs")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
PLAN = os.path.join(RAIZ, "docs", "plan")
CORTE = "2026-09-04"

LAS_TRES = ["los cuadrantes de mercado", "la ecuacion de valor",
            "la supervision de la IA"]

PAT_LD = re.compile(
    r"^#{1,4}\s+`(LD-\d+)`\s*\.\s*`([a-z0-9_]+)`\s+contra\s+`([a-z0-9_]+)`\s*\.\s*\*\*([A-Z ]+)\*\*",
    re.M)
PAT_LD_TABLA = re.compile(
    r"^\|\s*\**`([a-z0-9_]+)`\**\s+contra\s+\**`([a-z0-9_]+)`\**\s*\|\s*\**([A-Z][A-Z ]*?)\**\s*\|\s*$",
    re.M)


def cargar(p):
    return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]


def leer_nominas():
    """LAS NOMINAS DE OP-L-02, PARSEADAS DEL FICHERO Y NO TECLEADAS."""
    texto = io.open(MJS, encoding="utf-8").read()
    m = re.search(r"const NOMINAS_OP_L_02 = \[(.*?)\n\];", texto, re.S)
    if not m:
        raise SystemExit("ROJO: no se encuentra NOMINAS_OP_L_02 en %s" % MJS)
    filas = re.findall(r"\[([^\]]*)\]", m.group(1))
    return [re.findall(r'"([a-z0-9_]+)"', f) for f in filas]


def medir(miembros, res, cola, dirigidas):
    """LA MEDICION, EN UN SOLO SITIO, para que la del racimo y la de la nomina
    salgan de la MISMA maquina y no de dos copias."""
    vivos = sorted(set(res(x) for x in miembros))
    colapsos = [(x, res(x)) for x in miembros if res(x) != x]
    pares = [tuple(sorted(p)) for p in itertools.combinations(vivos, 2)]
    de_cola = [p for p in pares if p in cola]
    de_dir = [p for p in pares if p not in cola and p in dirigidas]
    sin = [p for p in pares if p not in cola and p not in dirigidas]
    clases = collections.Counter()
    clase_de = {}
    for p in de_cola:
        clases[cola[p][0]] += 1
        clase_de[p] = cola[p][0]
    for p in de_dir:
        clases[dirigidas[p][0]] += 1
        clase_de[p] = dirigidas[p][0]
    puentes = []
    for nodo in vivos:
        aes = [o for o in vivos if o != nodo
               and clase_de.get(tuple(sorted((nodo, o))), "").startswith("A")]
        for x, y in itertools.combinations(sorted(aes), 2):
            if clase_de.get(tuple(sorted((x, y)))) == "D":
                puentes.append((nodo, x, y))
    return dict(mem=len(miembros), vivos=len(vivos), colapsos=colapsos,
                pares=len(pares), cola=len(de_cola), dirig=len(de_dir),
                sin=len(sin), sin_pares=sin, clases=dict(sorted(clases.items())),
                puentes=puentes,
                superviviente=vivos[0] if len(vivos) == 1 else None)


def main():
    aplicar = "--aplicar" in sys.argv
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 170, TAREA 5.a: LA FORMA DE LAS TRES NOMINAS, RE ESCRITA CON SU")
    print("COBERTURA AL LADO (9.26) Y CON EL RESOLUTOR DELANTE (P.1)")
    print("=" * 78)
    print("")

    print("A) LAS SEDES, LEIDAS HOY")
    G = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    ALIAS = dict((a, k) for k, v in G.items() for a in (v.get("ids_alias") or []))

    def res(x):
        visto = set()
        while x in ALIAS and x not in visto:
            visto.add(x)
            x = ALIAS[x]
        return x

    V = cargar(VEREDICTOS)
    cola = {}
    for r in V:
        cola[tuple(sorted((res(r["nodo_a"]), res(r["nodo_b"]))))] = (
            r["clase"], r["puesto_intra"])
    print("   grafo: %d nodos, %d entradas de alias" % (len(G), len(ALIAS)))
    print("   cola: %d filas, corte %d, %d pares distintos tras resolver"
          % (len(V), max(r["puesto_intra"] for r in V), len(cola)))
    dirigidas = {}
    n_cab = n_tab = 0
    for nombre in sorted(os.listdir(PLAN)):
        if not nombre.endswith(".md"):
            continue
        texto = io.open(os.path.join(PLAN, nombre), encoding="utf-8").read()
        for ld, a, b, clase in PAT_LD.findall(texto):
            dirigidas[tuple(sorted((res(a), res(b))))] = (clase.strip().split()[0], ld)
            n_cab += 1
        for a, b, clase in PAT_LD_TABLA.findall(texto):
            dirigidas[tuple(sorted((res(a), res(b))))] = (
                clase.strip().split()[0], "fila de tabla en %s" % nombre)
            n_tab += 1
    print("   lecturas dirigidas: %d con cabecera `LD-nn`, %d como fila de tabla"
          % (n_cab, n_tab))
    print("   CIFRA pares dirigidos distintos tras resolver: %d" % len(dirigidas))
    print("")

    inv = cargar(INVENTARIO)
    lineas = [l for l in io.open(INVENTARIO, encoding="utf-8") if l.strip()]
    print("B) LAS TRES NOMINAS, LOCALIZADAS EN docs/plan/INVENTARIO.jsonl")
    print("   CIFRA entradas del inventario: %d" % len(inv))
    pos = {}
    for nombre in LAS_TRES:
        idx = [i for i, e in enumerate(inv) if e.get("nombre") == nombre]
        if len(idx) != 1:
            print("   ROJO: %r aparece %d veces." % (nombre, len(idx)))
            return 1
        pos[nombre] = idx[0]
        print("   %-30s linea %d, tipo %s, %d miembros escritos"
              % (nombre, idx[0] + 1, inv[idx[0]].get("tipo"),
                 len(inv[idx[0]].get("miembros") or [])))
    print("")

    print("C) LA NOMINA DE OP-L-02 QUE LE CORRESPONDE A CADA RACIMO, CASADA POR")
    print("   INTERSECCION DE MIEMBROS Y NO POR NOMBRE")
    nominas = leer_nominas()
    print("   NOMINAS_OP_L_02 parseadas de scripts/vuelta16_generar_actos.mjs: %d"
          % len(nominas))
    casada = {}
    for nombre in LAS_TRES:
        mem = set(res(x) for x in (inv[pos[nombre]].get("miembros") or []))
        mejor, cuantos = None, 0
        for k, nom in enumerate(nominas):
            c = len(mem & set(res(x) for x in nom))
            if c > cuantos:
                mejor, cuantos = k, c
        casada[nombre] = mejor
        print("   %-30s nomina %s de OP-L-02, %d miembros escritos, %d en comun"
              % (nombre, mejor + 1 if mejor is not None else "(ninguna)",
                 len(nominas[mejor]) if mejor is not None else 0, cuantos))
    print("")

    print("D) CADA NOMINA, MEDIDA DOS VECES: COMO ESTA ESCRITA Y TRAS RESOLVER")
    medido = {}
    medido_nomina = {}
    for nombre in LAS_TRES:
        e = inv[pos[nombre]]
        mem = e.get("miembros") or []
        m = medir(mem, res, cola, dirigidas)
        medido[nombre] = m
        k = casada[nombre]
        mn = medir(nominas[k], res, cola, dirigidas) if k is not None else None
        medido_nomina[nombre] = mn
        print("   %s" % nombre)
        print("      EL RACIMO ENTERO, tal como el inventario lo escribe:")
        print("         miembros escritos %d | vivos tras resolver %d | colapsados %d"
              % (m["mem"], m["vivos"], len(m["colapsos"])))
        for a, b in m["colapsos"]:
            print("            %s -> %s" % (a, b))
        print("         pares posibles %d | de cola %d | dirigidas %d | SIN veredicto %d"
              % (m["pares"], m["cola"], m["dirig"], m["sin"]))
        for p in m["sin_pares"]:
            print("            SIN VEREDICTO: %s contra %s" % p)
        print("         reparto de clases: %s" % (m["clases"] or "(ninguna)"))
        print("         P.10 puentes: %d" % len(m["puentes"]))
        for n, x, y in m["puentes"]:
            print("            puente `%s` sobre (`%s` , `%s`)" % (n, x, y))
        if mn is not None and mn["mem"] != m["mem"]:
            print("      LA NOMINA DE OP-L-02, QUE ES UN SUBCONJUNTO Y SE MIDE APARTE:")
            print("         miembros escritos %d | vivos %d | pares %d | leidos %d"
                  " | SIN %d | clases %s"
                  % (mn["mem"], mn["vivos"], mn["pares"],
                     mn["pares"] - mn["sin"], mn["sin"], mn["clases"] or "(ninguna)"))
        print("      forma escrita hoy:     %r" % e.get("forma"))
        print("      cobertura escrita hoy: %r" % e.get("cobertura"))
        print("")

    print("E) LA FORMA NUEVA DE CADA UNA, COMPUESTA DE LO MEDIDO Y NO TECLEADA")
    nuevas = {}
    for nombre in LAS_TRES:
        m = medido[nombre]
        mn = medido_nomina[nombre]
        e = inv[pos[nombre]]
        # LA COLETILLA DEL SUBCONJUNTO, y existe porque sin ella la forma del
        # racimo entero se leeria como si la segunda tanda no hubiera cerrado
        # nada. La nomina que OP-L-02 cerro puede ser un SUBCONJUNTO del racimo,
        # y entonces las dos cifras son ciertas y hablan de universos distintos.
        coletilla = ""
        if mn is not None and mn["mem"] != m["mem"]:
            coletilla = (" Y LA NOMINA QUE `OP-L-02` CERRO ES UN SUBCONJUNTO DE ESTE "
                         "RACIMO, ASI QUE SUS DOS CIFRAS SON CIERTAS Y HABLAN DE "
                         "UNIVERSOS DISTINTOS: la nomina son %d miembros escritos, %d "
                         "vivos, %d pares posibles, %d leidos y %d SIN veredicto, "
                         "reparto %s. Medida con la MISMA maquina que la de arriba, en "
                         "la misma corrida."
                         % (mn["mem"], mn["vivos"], mn["pares"],
                            mn["pares"] - mn["sin"], mn["sin"],
                            ", ".join("%s %d" % (k, v) for k, v in mn["clases"].items())
                            or "ninguna"))
        if m["vivos"] == 1:
            forma = ("FUNDIDA. Al corte %s la nomina entera resuelve a UN SOLO NODO "
                     "VIVO, `%s`: sus %d miembros escritos colapsan a 1 por "
                     "`ids_alias` y no queda ningun par que leer, asi que NO TIENE "
                     "FORMA que medir. La forma vieja de este campo, sin tocar y "
                     "cierta en su corte: %r"
                     % (CORTE, m["superviviente"], m["mem"], e.get("forma"))) + coletilla
            cobertura = ("0 de 0 al corte %s: no hay pares entre un solo nodo. "
                         "El texto viejo de este campo, sin tocar: %r"
                         % (CORTE, e.get("cobertura")))
        elif m["sin"] == 0:
            aes = m["clases"].get("A", 0)
            des = m["clases"].get("D", 0)
            forma = ("%s, con cobertura COMPLETA al corte %s: %d de %d pares leidos "
                     "entre los %d nodos VIVOS tras resolver (%d de la cola y %d por "
                     "lectura dirigida), reparto %s. %s"
                     "POR EL BANCO 9.26 la forma deja de ser provisional SOLO porque "
                     "no falta ningun par, y por 9.16 se dice ademas lo que la "
                     "cobertura completa permite decir y no mas: EL SUB-PURO ES UNA "
                     "PROMESA, NO UN RESULTADO, y esta nomina ya no promete nada "
                     "porque esta leida entera. La forma vieja de este campo, sin "
                     "tocar y cierta en su corte: %r"
                     % ("MEZCLADO" if aes and des else
                        ("REPITE ENTERA" if des == 0 else "SANA ENTERA"),
                        CORTE, m["pares"] - m["sin"], m["pares"], m["vivos"],
                        m["cola"], m["dirig"],
                        ", ".join("%s %d" % (k, v) for k, v in m["clases"].items()),
                        ("NO SE FUNDE TODAVIA, y el motivo esta medido: la nomina "
                         "trae %d NODO(S) PUENTE de P.10 (%s), y P.10 dice que la "
                         "componente NO se funde hasta que ese triangulo se cierre. "
                         % (len(m["puentes"]),
                            "; ".join("`%s` sobre (`%s`, `%s`)" % p for p in m["puentes"]))
                         if m["puentes"] else
                         "No hay ningun nodo puente de P.10 en ella. "),
                        e.get("forma"))) + coletilla
            cobertura = ("%d de %d al corte %s, con el resolutor delante por P.1 "
                         "(%d de la cola, %d por lectura dirigida, 0 sin veredicto). "
                         "El texto viejo de este campo, sin tocar: %r"
                         % (m["pares"] - m["sin"], m["pares"], CORTE, m["cola"],
                            m["dirig"], e.get("cobertura")))
        else:
            forma = ("PROVISIONAL al corte %s, y lo es por el banco 9.26: faltan %d "
                     "pares por leer de los %d posibles entre los %d nodos VIVOS "
                     "tras resolver, y mientras falte un par la forma no se cierra. "
                     "Leidos %d (%d de la cola y %d por lectura dirigida), reparto "
                     "%s. Y por 9.16, EL SUB-PURO ES UNA PROMESA, NO UN RESULTADO: "
                     "esta racha no dice nada de lo que falta. La forma vieja de "
                     "este campo, sin tocar y cierta en su corte: %r"
                     % (CORTE, m["sin"], m["pares"], m["vivos"],
                        m["pares"] - m["sin"], m["cola"], m["dirig"],
                        ", ".join("%s %d" % (k, v) for k, v in m["clases"].items())
                        or "ninguna", e.get("forma"))) + coletilla
            cobertura = ("%d de %d al corte %s, con el resolutor delante por P.1 "
                         "(%d de la cola, %d por lectura dirigida, %d SIN veredicto). "
                         "El texto viejo de este campo, sin tocar: %r"
                         % (m["pares"] - m["sin"], m["pares"], CORTE, m["cola"],
                            m["dirig"], m["sin"], e.get("cobertura")))
        nuevas[nombre] = (forma, cobertura)
        print("   %s" % nombre)
        print("      forma nueva:     %s" % forma[:150])
        print("      cobertura nueva: %s" % cobertura[:150])
        print("")

    print("F) LA GUARDA DE ADICION: NINGUNA PALABRA VIEJA SE PIERDE")
    fallos = []
    for nombre in LAS_TRES:
        e = inv[pos[nombre]]
        forma, cobertura = nuevas[nombre]
        ok_f = repr(e.get("forma")) in forma
        ok_c = repr(e.get("cobertura")) in cobertura
        print("   %-30s la forma vieja sigue dentro: %s | la cobertura vieja: %s"
              % (nombre, ok_f, ok_c))
        if not (ok_f and ok_c):
            fallos.append(nombre)
    if fallos:
        print("   ROJO: se perderia texto viejo en %s. No se escribe nada." % fallos)
        return 1
    print("")

    if not aplicar:
        print("MODO MEDICION: el inventario NO se toca. Corre con --aplicar.")
        return 0

    print("G) EL ESQUEMA NO CRECE Y NADA MAS SE MUEVE")
    for nombre in LAS_TRES:
        i = pos[nombre]
        vieja = inv[i]
        nueva = dict(vieja)
        nueva["forma"], nueva["cobertura"] = nuevas[nombre]
        movidos = [k for k in vieja
                   if k not in ("forma", "cobertura") and vieja[k] != nueva.get(k)]
        print("   %-30s claves antes %d, despues %d | movidos de mas: %d %s"
              % (nombre, len(vieja), len(nueva), len(movidos), movidos))
        print("      estado antes %r, despues %r"
              % (vieja.get("estado"), nueva.get("estado")))
        if len(nueva) != len(vieja) or movidos:
            print("   ROJO: se movio algo que no tocaba.")
            return 1
        lineas[i] = json.dumps(nueva, ensure_ascii=False) + "\n"
    io.open(INVENTARIO, "w", encoding="utf-8", newline="\n").writelines(lineas)
    print("")

    despues = cargar(INVENTARIO)
    print("H) ESCRITO, Y RECONTADO DESPUES DE ESCRIBIR")
    print("   CIFRA entradas antes %d, despues %d" % (len(inv), len(despues)))
    tipos_antes = collections.Counter(x.get("tipo") for x in inv)
    tipos_despues = collections.Counter(x.get("tipo") for x in despues)
    print("   reparto por tipo antes:   %s" % dict(sorted(tipos_antes.items())))
    print("   reparto por tipo despues: %s" % dict(sorted(tipos_despues.items())))
    for nombre in LAS_TRES:
        i = pos[nombre]
        print("   %-30s sigue en la linea %d: %s | forma de %d caracteres"
              % (nombre, i + 1, despues[i].get("nombre") == nombre,
                 len(despues[i].get("forma") or "")))
    if len(despues) != len(inv) or tipos_antes != tipos_despues:
        print("   ROJO: el fichero cambio de forma.")
        return 1
    print("")
    print("VERDE: las tres formas quedan re escritas por adicion, con su cobertura")
    print("al lado y con el resolutor delante.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
