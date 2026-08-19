# -*- coding: utf-8 -*-
"""vuelta39_enlazar_p10.py

LA TERCERA SALIDA DE P.10 ENTERA: fundido el subconjunto cerrado, SE ENLAZA EL
RESTO. Los tres vivos que quedan del acto de OP-D-04 son reglas_brainstorming,
pensamiento_convergente_divergente y construir_sobre_ideas_ajenas, y este
instrumento comprueba los TRES pares y escribe SOLO lo que falte.

MODOS: --simular (por defecto, cero escrituras) y --ejecutar.

P.9, TODA ARISTA NUEVA SE ESCRIBE RESUELTA AL DIA DE SU ESCRITURA, y la regla
pide TRES cosas de las que aqui tocan dos:
  - la arista se escribe con el id RESUELTO, no con el de la lectura que la
    justifica;
  - la verificacion incluye que la arista NO NAZCA RESOLVIENDO POR ALIAS: se
    comprueba que el id escrito es el id VIVO. Por eso se corre el resolutor
    sobre los dos extremos ANTES de escribir y se ABORTA si alguno resuelve a
    otra cosa que a si mismo. El resolutor es una red de seguridad, no una
    licencia: si hiciera falta para que la arista llegue, la arista esta mal
    escrita.
  - la tercera (los enlaces corren DESPUES de las fusiones que tocan sus
    destinos) se cumple por el orden de la vuelta, no por este codigo: las dos
    fusiones ya estan ejecutadas y commiteadas cuando esto corre.

SE ESCRIBEN LOS DOS EXTREMOS, no uno. La simetrizacion del paso 5 de run_phase1
sabria completarlo, pero apoyarse en ella para una arista que este instrumento
decide seria dejar el fichero diciendo media verdad hasta que alguien corra el
ciclo. Que el ciclo posterior no tenga NADA que anadir es la prueba.

LA DIRECCION NO SE INVENTA AQUI: la da el motivo del grupo 3 del plan sellado
del taller, que dice por que el procedimiento no se injerta ('vive en
construir_sobre_ideas_ajenas, que queda VIVO y enlazado por P.10'). El
superviviente ENUNCIA la regla entre las suyas y el otro nodo la EJECUTA, y la
condicion de activacion del segundo lo dice con sus palabras: 'Durante sesiones
de brainstorming o co-creacion en equipo'. De la sesion se va a la tecnica.

Uso: python scripts/loop/vuelta39_enlazar_p10.py [--simular|--ejecutar]
"""
import io
import itertools
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
CAMPOS = ("nodos_previos", "nodos_siguientes")
OPUESTO = {"nodos_previos": "nodos_siguientes", "nodos_siguientes": "nodos_previos"}

TRES = ["reglas_brainstorming", "pensamiento_convergente_divergente",
        "construir_sobre_ideas_ajenas"]

# (de, a, campo_en_de, motivo). campo_en_de es donde el ORIGEN declara al DESTINO.
ENLACES = [
    ("reglas_brainstorming", "construir_sobre_ideas_ajenas", "nodos_siguientes",
     "El superviviente del taller ENUNCIA la regla de construir sobre las ideas de otros "
     "(paso 3 del nodo fundido) y NO trae su procedimiento, porque el procedimiento vive "
     "entero en el otro nodo. La condicion de activacion del destino cierra la direccion: "
     "'Durante sesiones de brainstorming o co-creacion en equipo'."),
]


def leer_crudo(nid):
    with io.open(os.path.join(NODOS, nid + ".json"), encoding="utf-8", newline="") as fh:
        bruto = fh.read()
    cola = ""
    while bruto and bruto[-1] in "\r\n":
        cola = bruto[-1] + cola
        bruto = bruto[:-1]
    return json.loads(bruto), cola


def escribir(nid, datos, cola):
    with io.open(os.path.join(NODOS, nid + ".json"), "w", encoding="utf-8", newline="") as fh:
        fh.write(json.dumps(datos, ensure_ascii=False, indent=2) + cola)


def cargar_resolutor():
    g = {}
    for nombre in os.listdir(NODOS):
        if nombre.endswith(".json"):
            d = json.load(io.open(os.path.join(NODOS, nombre), encoding="utf-8"))
            g[d["node_id"]] = d
    alias = {}
    for nid, v in g.items():
        for a in v.get("ids_alias") or []:
            if a != nid:
                alias[a] = nid

    def resolver(n):
        v = g.get(n)
        if v and not v.get("deprecado"):
            return n
        visto, cur = {n}, n
        ultimo = n if v else None
        while cur in alias and alias[cur] not in visto:
            cur = alias[cur]
            visto.add(cur)
            if cur in g:
                ultimo = cur
                if not g[cur].get("deprecado"):
                    return cur
        return ultimo
    return g, resolver


def estado(G):
    filas = []
    for a, b in itertools.combinations(TRES, 2):
        de_a = [c for c in CAMPOS if b in (G[a].get(c) or [])]
        de_b = [c for c in CAMPOS if a in (G[b].get(c) or [])]
        filas.append((a, b, de_a, de_b))
    return filas


def imprimir_estado(G, titulo):
    print("### %s" % titulo)
    for a, b, de_a, de_b in estado(G):
        if de_a and de_b:
            veredicto = "ENLAZADO en los dos extremos"
        elif de_a or de_b:
            veredicto = "COJO, declarado en un solo extremo"
        else:
            veredicto = "SIN ENLACE"
        print("  %-36s %-36s %-30s %s"
              % (a, b, veredicto, "%s / %s" % (de_a or "-", de_b or "-")))


def main():
    modo = "--simular"
    for x in sys.argv[1:]:
        if x in ("--simular", "--ejecutar"):
            modo = x

    print("P.10, TERCERA SALIDA: fundido el subconjunto cerrado, SE ENLAZA EL RESTO")
    print("MODO: %s" % modo)
    print("=" * 78)

    G, resolver = cargar_resolutor()
    for t in TRES:
        if t not in G:
            sys.exit("no existe en dataset/nodos: %s" % t)

    print("### LOS TRES VIVOS, comprobados vivos antes de nada")
    for t in TRES:
        print("  %-36s deprecado=%s  alias=%s"
              % (t, bool(G[t].get("deprecado")), G[t].get("ids_alias")))
    if any(G[t].get("deprecado") for t in TRES):
        sys.exit("alguno de los tres no esta vivo")
    print()

    imprimir_estado(G, "LOS TRES PARES, ANTES")
    print()

    # P.9: los dos extremos de cada arista nueva TIENEN que resolver a si mismos
    print("### P.9, LOS IDS RESUELTOS AL DIA DE SU ESCRITURA")
    fallos = []
    for de, a, campo, _m in ENLACES:
        for x in (de, a):
            r = resolver(x)
            ok = (r == x)
            print("  %-36s resuelve a %-36s %s" % (x, r, "OK" if ok else "ROJO, NACE POR ALIAS"))
            if not ok:
                fallos.append("%s no es el id vivo: resuelve a %s" % (x, r))
    if fallos:
        print()
        for f in fallos:
            print("  [ROJO] %s" % f)
        print("SE ABORTA SIN ESCRIBIR.")
        return 1
    print()

    cambios = {}
    escritas = []
    for de, a, campo, motivo in ENLACES:
        ya_de = a in (G[de].get(campo) or [])
        ya_a = de in (G[a].get(OPUESTO[campo]) or [])
        print("### LA ARISTA: %s .%s -> %s" % (de, campo, a))
        print("  motivo: %s" % motivo)
        print("  ya declarada en el origen : %s" % ya_de)
        print("  ya declarada en el destino: %s" % ya_a)
        if ya_de and ya_a:
            print("  NADA QUE ESCRIBIR: la arista ya esta en los dos extremos.")
            continue
        d_de, c_de = leer_crudo(de)
        d_a, c_a = leer_crudo(a)
        if not ya_de:
            d_de[campo] = list(d_de.get(campo) or []) + [a]
        if not ya_a:
            d_a[OPUESTO[campo]] = list(d_a.get(OPUESTO[campo]) or []) + [de]
        cambios[de] = (d_de, c_de)
        cambios[a] = (d_a, c_a)
        escritas.append((de, campo, a))
        print("  SE ESCRIBEN LOS DOS EXTREMOS.")
    print()

    # cero duplicada y cero auto arista sobre la copia
    for nid, (d, _c) in cambios.items():
        for campo in CAMPOS:
            lista = d.get(campo) or []
            if nid in lista:
                fallos.append("AUTO-ARISTA: %s en %s" % (nid, campo))
            if len(lista) != len(set(lista)):
                fallos.append("DUPLICADA: %s en %s" % (nid, campo))
    print("guarda, cero auto-arista y cero duplicada en lo escrito: %s"
          % ("OK" if not fallos else "ROJO"))
    if fallos:
        for f in fallos:
            print("  [ROJO] %s" % f)
        print("SE ABORTA SIN ESCRIBIR.")
        return 1

    if modo == "--simular":
        print()
        print("SIMULACION: cero escrituras. Se escribirian %d fichero(s)." % len(cambios))
        return 0

    for nid, (d, c) in cambios.items():
        escribir(nid, d, c)
    print()
    print("ESCRITO: %d fichero(s), %d arista(s) nueva(s)." % (len(cambios), len(escritas)))

    G2, _ = cargar_resolutor()
    print()
    imprimir_estado(G2, "LOS TRES PARES, DESPUES")
    cojos = [f for f in estado(G2) if bool(f[2]) != bool(f[3])]
    sin = [f for f in estado(G2) if not f[2] and not f[3]]
    print()
    print("RESULTADO: %d par(es) sin enlace, %d cojo(s). %s"
          % (len(sin), len(cojos),
             "LOS TRES PARES ENLAZADOS EN LOS DOS EXTREMOS." if not sin and not cojos
             else "QUEDA TRABAJO."))
    return 0 if not sin and not cojos else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
