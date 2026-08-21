# -*- coding: utf-8 -*-
"""varas_n_arias_del_tramo.py . LAS VARAS POR FORMA DE UN ACTO DE N MIEMBROS,
UNA FILA POR MIEMBRO Y UNA FORMA POR ACTO.

NOMBRE ESTABLE Y SIN NUMERO DE VUELTA NI DE TRAMO: el tramo entra por --tramo y
los actos por --actos. Este fichero no se clona cada vuelta.

POR QUE NACE, y no es un capricho. scripts/loop/vuelta58_varas_tramo.py publica
UNA FILA POR ACTO con DOS miembros, porque nacio para OP-U-01, donde la
componente ERA el par. Los actos de OP-U-02 van de 3 a 15 miembros: corrido
sobre ellos, aquel cuadro compararia d[0] contra d[1] de sorted(miembros) y
dejaria a los demas fuera EN SILENCIO. La vuelta 66 le escribio la guarda que
lo impide (correccion declarada, cambio 2 de su docstring) y este fichero es el
que hace la lectura que aquel no puede hacer.

LA ARITMETICA DE LA FORMA SE COPIA Y NO SE RETECLEA: el bloque que decide
TODAS DE ACUERDO / UNA SOLA VARA / CHOCAN / CONTENIDO EMPATA / EMPATE SIN VARA
sale LITERAL de scripts/loop/vuelta58_varas_tramo.py (su bloque `conte`), para
que dos instrumentos de la campana no la calculen distinto en silencio. Lo unico
que se generaliza es LA FLECHA, y la generalizacion es la que la campana ya usa
por escrito: en el acto 3 del lote A de la vuelta 65 las varas se dijeron
"6 pasos contra un MAXIMO de 5, 3 condiciones contra 2 y cableado 14 contra 9".

  LA FLECHA, N-ARIA: para cada vara se mira el MAXIMO entre los miembros. Si UN
  SOLO miembro lo alcanza, la vara APUNTA a ese miembro. Si lo alcanzan dos o
  mas, la vara EMPATA y no apunta a nadie. Con dos miembros esto da exactamente
  lo mismo que la flecha vieja, que es lo que la hace una generalizacion y no
  una regla nueva.

LAS PUERTAS SE IMPRIMEN Y NO SE ADIVINAN: el universo protegido (semillas de
entrada mas extremos de puente aprobado) se lee igual que en el ancestro, y cada
miembro que sea puerta sale marcado. LA GUARDA 1B NO SE APLICA AQUI: este
fichero CUENTA Y PUBLICA, no decide. Que hacer cuando la puerta y el contenido
apuntan a lados distintos lo dice el acta 54, pregunta 1, y lo decide el
ejecutor con la medicion delante.

TODO ID PASA POR EL RESOLUTOR ANTES DE CONTAR (P.1) en el cableado, igual que el
ancestro.

DE SOLO LECTURA. Imprime; no toca nada.

Uso:
  python scripts/loop/varas_n_arias_del_tramo.py
      --tramo docs/loop/TRAMO_UNICO_OPU02_V64.jsonl [--actos 5,7,8,9]
"""

import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
CAMPOS = ("nodos_previos", "nodos_siguientes")
NL = chr(10)


def cargar(p):
    return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]


def resolutor():
    """P.1: id a id VIVO siguiendo alias."""
    G = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    ALIAS = {a: k for k, v in G.items() for a in (v.get("ids_alias") or [])}

    def res(x):
        visto = set()
        while x in ALIAS and x not in visto:
            visto.add(x)
            x = ALIAS[x]
        return x

    return G, res


def protegidos():
    """SEMILLAS DE ENTRADA mas EXTREMOS DE PUENTE APROBADO. LA MAQUINA SE COPIA
    LITERAL de scripts/loop/vuelta58_varas_tramo.py, lineas 104 a 122, y NO se
    re-inventa, para que dos instrumentos de la campana no lean puertas distintas
    en silencio."""
    sem = set(json.load(io.open(os.path.join(RAIZ, "dataset", "metadata",
                                             "entry_seeds.json"),
                                encoding="utf-8")).get("seeds", []))
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
    return sem | pue


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tramo", required=True)
    ap.add_argument("--actos", default=None)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    tramo = cargar(a.tramo)
    if not tramo:
        print("ROJO: el fichero del tramo esta vacio. PARADA.")
        return 1
    # LA CLAVE DEL ORDINAL SE DESCUBRE DEL FICHERO, los dos prefijos conocidos, que
    # es la misma maquina corregida de sus dos hermanos.
    ORD = ROT = None
    for prefijo in ("orden_tramo", "orden_universo"):
        claves = sorted({k for k in tramo[0] if k.startswith(prefijo)})
        if len(claves) > 1:
            print("ROJO: %d claves de ordinal con el prefijo %s (%s). PARADA."
                  % (len(claves), prefijo, claves))
            return 1
        if len(claves) == 1:
            ORD = claves[0]
            ROT = (ORD.replace("orden_tramo", "") if prefijo == "orden_tramo"
                   else str(tramo[0].get("tramo") or "SIN ROTULO EN EL FICHERO DEL TRAMO"))
            break
    if ORD is None:
        print("ROJO: el fichero del tramo no trae ninguna clave de ordinal conocida "
              "(orden_tramo, orden_universo). Trae: %s. PARADA." % sorted(tramo[0]))
        return 1

    pedidos = None
    if a.actos:
        pedidos = {int(x) for x in a.actos.split(",") if x.strip()}
        tramo = [x for x in tramo if x[ORD] in pedidos]
        faltan = pedidos - {x[ORD] for x in tramo}
        if faltan:
            print("ROJO: los actos %s no estan en el tramo. PARADA." % sorted(faltan))
            return 1

    G, res = resolutor()
    prot = protegidos()

    print("=" * 110)
    print("VARAS POR FORMA, N-ARIAS, DEL TRAMO %s" % ROT)
    print("  fichero del tramo: %s" % a.tramo)
    print("  universo PROTEGIDO (semillas mas extremos de puente): %d ids" % len(prot))
    print("=" * 110)
    print()
    print("  pasos y cond son las varas de CONTENIDO contables; cab es el CABLEADO,")
    print("  que por P.8 solo habla a contenido empatado. La marca < indica que ese")
    print("  miembro es EL UNICO que alcanza el maximo de esa vara, o sea que la vara")
    print("  APUNTA a el. Si dos o mas lo alcanzan, la vara EMPATA y no apunta.")
    print()

    formas = {}
    for act in tramo:
        mi = sorted(act["miembros"])
        d = []
        for x in mi:
            ruta = os.path.join(NODOS, x + ".json")
            if not os.path.exists(ruta):
                print("ROJO: no existe el fichero del nodo %s. PARADA." % x)
                return 1
            o = json.load(io.open(ruta, encoding="utf-8"))
            d.append({
                "id": x,
                "pasos": len(o.get("pasos_accionables") or []),
                "cond": len(o.get("condiciones_activacion") or []),
                "cab": len({res(y) for c in CAMPOS for y in (o.get(c) or [])} - {res(x)}),
            })

        def flecha(k):
            """N-ARIA: apunta al UNICO que alcanza el maximo, o empata (None)."""
            mx = max(x[k] for x in d)
            duenos = [x["id"] for x in d if x[k] == mx]
            return (duenos[0] if len(duenos) == 1 else None), mx

        fp, mxp = flecha("pasos")
        fc, mxc = flecha("cond")
        fk, mxk = flecha("cab")

        # LA ARITMETICA DE LA FORMA, COPIADA LITERAL de vuelta58_varas_tramo.py.
        # Alli las flechas son 1 o 2 o 0; aqui son el id del miembro o None. La
        # forma del bloque no cambia: se filtran las varas de contenido que no
        # empatan y se mira si apuntan al mismo lado o a lados distintos.
        conte = [x for x in (fp, fc) if x]
        if not conte:
            forma = "CONTENIDO EMPATA" if fk else "EMPATE SIN VARA"
        elif len(set(conte)) == 2:
            forma = "CHOCAN"
        elif len(conte) == 1:
            forma = "UNA SOLA VARA"
        else:
            forma = "TODAS DE ACUERDO"
        formas[forma] = formas.get(forma, 0) + 1

        puertas = [x["id"] for x in d if x["id"] in prot]
        print("-" * 110)
        print("ACTO %s | %d miembros | FORMA: %s" % (act[ORD], len(mi), forma))
        print("   maximos medidos: pasos %d, condiciones %d, cableado %d" % (mxp, mxc, mxk))
        print("   la vara de PASOS       apunta a: %s" % (fp or "EMPATA, no apunta"))
        print("   la vara de CONDICIONES apunta a: %s" % (fc or "EMPATA, no apunta"))
        print("   el CABLEADO (P.8)      apunta a: %s" % (fk or "EMPATA, no apunta"))
        if puertas:
            print("   PUERTAS DENTRO DEL ACTO (guarda 1B, no se absorben): %s"
                  % ", ".join(puertas))
        else:
            print("   PUERTAS DENTRO DEL ACTO: NINGUNA (la guarda 1B pasa por vacio)")
        print()
        print("      %-56s %6s %6s %6s" % ("miembro", "pasos", "cond", "cab"))
        for x in d:
            marcas = "".join([
                " <pasos" if x["id"] == fp else "",
                " <cond" if x["id"] == fc else "",
                " <cab" if x["id"] == fk else "",
                "  [PUERTA]" if x["id"] in prot else "",
            ])
            print("      %-56s %6d %6d %6d%s"
                  % (x["id"], x["pasos"], x["cond"], x["cab"], marcas))
        print()

    print("=" * 110)
    print("  actos mirados: %d | POR FORMA: %s" % (len(tramo), formas))
    print()
    print("LO QUE ESTO NO HACE: no elige superviviente, no aplica la guarda 1B y no funde.")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
