# -*- coding: utf-8 -*-
"""vuelta54_mesa_tramo2.py . LA MESA DE LOS 50 ACTOS DEL TRAMO 2, con las varas
de P.8 CONTADAS POR MAQUINA y los avisos-especie BUSCADOS EN LA LETRA.

DE SOLO LECTURA. No toca ni un nodo, ni un veredicto, ni una operacion:
imprime.

POR QUE EXISTE: el dossier de P.5 (scripts/loop/vuelta48_dossier_actos.py) da
el acto ENTERO y es lo que hay que LEER; pero las varas que P.8 pesa (pasos,
condiciones, material propio, cableado) SON CUENTAS, y una cuenta tecleada a
mano es exactamente la caida que la regla 1 del EJECUTOR prohibe. Este
instrumento las cuenta y las imprime al lado de la letra, para que la lectura
decida CON las cifras delante en vez de con las cifras recordadas.

LO QUE IMPRIME POR ACTO:

  1. EL VEREDICTO DIRECTO del par, con su puesto, su clase y la formula
     "Sobrevive X" que la razon cierra (P.12 parte 2: mandan los directos).
  2. LOS AVISOS-ESPECIE buscados EN LA LETRA de la razon, que son los cuatro
     que la pagina reserva para DECLARAR en vez de fundir (acta de la vuelta
     50, adjudicacion 2): PROVISIONAL, incompatibilidad expresa, politica de
     catalogo, y la peticion de contar antes de decidir.
  3. LAS VARAS DE CONTENIDO por miembro: pasos, condiciones, y MATERIAL PROPIO
     (los pasos del uno que no estan en el otro, por solape de palabras).
  4. EL CABLEADO por miembro (a cuantos nombra, cuantos lo nombran), que por
     P.8 solo habla a contenido empatado.
  5. LA GUARDA 1B: si alguno de los dos es PUERTA (semilla de entrada o
     extremo de puente aprobado), con lo que la eleccion queda forzada.
  6. LA COLISION QUE LA FUSION FABRICARIA: los pares del archivo que quedarian
     con dos clases sobre el mismo par resuelto.

NO ELIGE NADA. Imprime la mesa; la eleccion se escribe a mano en el plan, con
su razon, tras leer el dossier.

Uso:
  python scripts/loop/vuelta54_mesa_tramo2.py --tramo docs/loop/TRAMO2_V54.jsonl
"""
import argparse
import io
import itertools
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
CAMPOS = ("nodos_previos", "nodos_siguientes")

# Los avisos-especie que la pagina reserva para DECLARAR en vez de fundir.
AVISOS = [
    ("PROVISIONAL", r"PROVISIONAL|provisional"),
    ("INCOMPATIBILIDAD EXPRESA", r"incompatib|no se puede apilar|hay que decidirlo"),
    ("POLITICA DE CATALOGO", r"politica de catalogo|decision de catalogo|la mesa decide"),
    ("PIDE CONTAR ANTES", r"hay que contarla|contar antes de decidir|antes de decidir"),
]

PALABRA = re.compile(r"[a-z0-9]+")


def cargar(p):
    return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]


def pasos_de(o):
    ps = o.get("pasos_accionables") or o.get("pasos") or []
    out = []
    for p in ps:
        if isinstance(p, dict):
            out.append(" ".join(str(v) for v in p.values() if isinstance(v, str)))
        else:
            out.append(str(p))
    return out


def bolsa(txt):
    return set(PALABRA.findall((txt or "").lower()))


def material_propio(mios, suyos):
    """Pasos mios que NO tienen pareja en los suyos.

    La vara es la de la casa y se dice: un paso esta CUBIERTO si comparte con
    algun paso del otro al menos la mitad de sus palabras de contenido. No es
    semantica, es solape lexico, y por eso la cifra va SIEMPRE con la letra al
    lado y nunca sola.
    """
    n = 0
    bs = [bolsa(s) for s in suyos]
    for m in mios:
        bm = bolsa(m)
        if not bm:
            continue
        if not any(len(bm & b) * 2 >= len(bm) for b in bs):
            n += 1
    return n


def protegidos():
    """El universo PROTEGIDO: semillas de entrada mas extremos de puente.

    LA FUENTE ES LA MISMA QUE LA DE scripts/loop/vuelta48_puertas_en_el_lote.py,
    copiada de ahi a proposito: dataset/metadata/entry_seeds.json para el core,
    packs/*/metadata/entry_seeds.json para los mundos y
    packs/*/metadata/bridges_aprobados.json para los extremos de puente. Usar
    otra fuente daria otro universo y la guarda 1B diria otra cosa que el
    instrumento que la publica.
    """
    sem = set(json.load(io.open(os.path.join(RAIZ, "dataset", "metadata",
                                             "entry_seeds.json"),
                                encoding="utf-8")).get("seeds", []))
    n_core = len(sem)
    packs = os.path.join(RAIZ, "packs")
    for d in sorted(os.listdir(packs)):
        q = os.path.join(packs, d, "metadata", "entry_seeds.json")
        if os.path.exists(q):
            sem.update(json.load(io.open(q, encoding="utf-8")))
    pue = set()
    for d in sorted(os.listdir(packs)):
        q = os.path.join(packs, d, "metadata", "bridges_aprobados.json")
        if not os.path.exists(q):
            continue
        for x in json.load(io.open(q, encoding="utf-8")).get("aprobados", []):
            for extremo in ("core", "dominio"):
                if x.get(extremo):
                    pue.add(x[extremo])
    return sem | pue, (n_core, len(sem), len(pue))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tramo", required=True)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    G = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    ALIAS = {x: k for k, v in G.items() for x in (v.get("ids_alias") or [])}

    def res(x):
        s = set()
        while x in ALIAS and x not in s:
            s.add(x)
            x = ALIAS[x]
        return x

    V = cargar(VER)
    directo = {}
    for r in V:
        ra, rb = res(r["nodo_a"]), res(r["nodo_b"])
        if ra != rb:
            directo[frozenset((ra, rb))] = r

    entra = {}
    for k, v in G.items():
        if v.get("deprecado"):
            continue
        for c in CAMPOS:
            for y in (v.get(c) or []):
                entra.setdefault(res(y), set()).add(k)

    prot, cuentas = protegidos()

    tramo = cargar(a.tramo)
    print("=" * 78)
    print("LA MESA DE LOS %d ACTOS DEL TRAMO 2 (vuelta 54)" % len(tramo))
    print("=" * 78)
    print()
    print("  universo PROTEGIDO, misma fuente que vuelta48_puertas_en_el_lote.py:")
    print("     semillas core %d | semillas con las de los mundos %d | extremos de puente %d"
          % cuentas)
    print("     UNION: %d ids" % len(prot))
    print()

    resumen = {"con aviso": 0, "con puerta": 0, "con colision prevista": 0}
    for act in tramo:
        mi = sorted(act["miembros"])
        n = act["orden_tramo2"]
        print("#" * 78)
        print("# ACTO %d del tramo 2 (puesto %d de la nomina de hoy, %s en la de la 48)"
              % (n, act["puesto_hoy"], act["puesto_v48"]))
        print("# %s" % ", ".join(mi))
        print("#" * 78)

        # 1. el veredicto directo
        par = frozenset((res(mi[0]), res(mi[1])))
        r = directo.get(par)
        sob = None
        if r:
            m = re.search(r"Sobrevive ([a-z0-9_]+)", r.get("razon") or "")
            sob = m.group(1) if m else None
            print("  [%s] puesto %-5s   la letra cierra con: %s"
                  % (r["clase"], r["puesto_intra"],
                     ("Sobrevive " + sob) if sob else "(no nombra superviviente)"))
        else:
            print("  SIN VEREDICTO DIRECTO (no deberia pasar en un acto CERRADO)")

        # 2. los avisos-especie
        raz = (r.get("razon") if r else "") or ""
        vistos = [nombre for nombre, pat in AVISOS if re.search(pat, raz)]
        print("  avisos-especie en la letra: %s" % (vistos if vistos else "NINGUNO"))
        if vistos:
            resumen["con aviso"] += 1

        # 3, 4, 5. las varas por miembro
        datos = {}
        for x in mi:
            o = json.load(io.open(os.path.join(NODOS, x + ".json"), encoding="utf-8"))
            datos[x] = o
        print()
        print("  %-52s %5s %5s %6s %5s %5s %s"
              % ("miembro", "pasos", "cond", "propio", "sale", "entra", "puerta"))
        for x in mi:
            o = datos[x]
            otro = mi[1] if x == mi[0] else mi[0]
            ps = pasos_de(o)
            pr = material_propio(ps, pasos_de(datos[otro]))
            sale = len({res(y) for c in CAMPOS for y in (o.get(c) or [])} - {res(x)})
            ent = len(entra.get(res(x), set()) - {x})
            print("  %-52s %5d %5d %6d %5d %5d %s"
                  % (x, len(ps), len(o.get("condiciones_activacion") or []), pr, sale, ent,
                     "SI" if x in prot else "no"))
        puertas = [x for x in mi if x in prot]
        if puertas:
            resumen["con puerta"] += 1
            print("  GUARDA 1B: hay puerta. TIENE que sobrevivir: %s" % ", ".join(puertas))

        # 6. la colision que la fusion fabricaria, por cada eleccion posible
        print()
        for sup in mi:
            abs_ = [x for x in mi if x != sup]
            mapa = dict(ALIAS)
            for x in abs_:
                mapa[x] = sup

            def res2(y):
                s = set()
                while y in mapa and y not in s:
                    s.add(y)
                    y = mapa[y]
                return y

            grupos = {}
            for v in V:
                ra, rb = res2(v["nodo_a"]), res2(v["nodo_b"])
                if ra == rb:
                    continue
                grupos.setdefault(frozenset((ra, rb)), []).append(v)
            col = [(k, g) for k, g in grupos.items()
                   if len({y["clase"] for y in g}) > 1]
            marca = "CIERRA PUERTA" if any(x in prot for x in abs_) else "limpio"
            print("  si sobrevive %-46s colisiones: %d  (%s)"
                  % (sup, len(col), marca))
            for k, g in col:
                print("       %s : %s" % (" + ".join(sorted(k)),
                                          ", ".join("%s %s" % (y["clase"], y["puesto_intra"])
                                                    for y in g)))
            if col:
                resumen["con colision prevista"] += 1
        print()

    print("=" * 78)
    print("RESUMEN: %s" % resumen)
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
