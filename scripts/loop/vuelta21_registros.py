# -*- coding: utf-8 -*-
"""VUELTA 21, TAREA 1: la medicion de los cinco registros. SOLO LECTURA.

El acta de la vuelta 20 del auditor (docs/loop/ACTA_AUDITOR.md, secciones 3 a 5)
abre cinco registros aditivos. La regla 1 del ejecutor manda que toda cifra o
nombre propio que se publique salga de un instrumento corrido EN ESTA VUELTA, no
de un acta ni de un reporte anterior. Este instrumento mide, desde el grafo y
desde el plan, TODO lo que los cinco registros van a escribir:

  1. Los pasos de `decision_de_vender_startup` hoy contra los 25 que publica la
     tabla de LOS TRES CASOS de `01_FUENTES.md`, y la comprobacion de historial
     con git: el blob de `dataset/metadata/master_graph.json` en 0e5e0c60 (9 ago),
     en 23f9ac32 (11 ago, el commit que crea 01_FUENTES.md) y en HEAD.
  2. La nomina de los 13 de `OP-F-04-HOR` contra los 14 medidos hoy en el grafo:
     que nodo sobra, y donde tiene cobertura de plan ese nodo.
  3. La posicion del bloque de Horowitz en los 13 de la operacion: cuales no lo
     tienen en la ultima posicion declarada del campo `fuente`.
  4. Los nodos que declaran el MISMO libro dos veces con dos grafias, dentro de
     la tanda de los cuatro y fuera de ella.
  5. El estado de lo reservado y el marcador, para que el reporte no cite una
     cifra sin corrida.

No escribe nada.
"""
import collections
import io
import json
import subprocess
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

RAIZ = Path(__file__).resolve().parents[2]
GRAFO = RAIZ / "dataset" / "metadata" / "master_graph.json"
OPS = RAIZ / "docs" / "plan" / "OPERACIONES.jsonl"
VEREDICTOS = RAIZ / "docs" / "INTRA_DOMINIO_VEREDICTOS.jsonl"
COMPONENTES = RAIZ / "docs" / "plan" / "RECOMPUTO_3388_COMPONENTES.jsonl"
INVENTARIO = RAIZ / "docs" / "plan" / "INVENTARIO.jsonl"

# el canon de la vuelta 19, reproducido tal cual y no importado
CANON = [("Hugos", "Essentials of Supply Chain Man"),
         ("Coleman", "Never Lose a Customer Again"),
         ("Horowitz", "Hard Thing About Hard Thing"),
         ("Weinberg", "Traction"),
         ("Rackham", "SPIN Selling"),
         ("Mollick", "Co-Intelligence")]
CUATRO = ["Coleman", "Horowitz", "Weinberg", "Rackham"]


def titulo(t):
    print()
    print("=" * 98)
    print(t)
    print("=" * 98)


def git(*args):
    try:
        return subprocess.run(["git"] + list(args), cwd=str(RAIZ), check=True,
                              capture_output=True, text=True,
                              encoding="utf-8", errors="replace").stdout.strip()
    except (subprocess.CalledProcessError, OSError) as e:
        return "ERROR: %s" % e


def operaciones():
    ops = []
    with open(OPS, encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.strip()
            if linea:
                ops.append(json.loads(linea))
    return ops


def segmentos(x):
    return [p.strip() for p in (x.get("fuente") or "").split(" | ")]


def main():
    grafo = json.load(open(GRAFO, encoding="utf-8"))
    nodos = grafo["nodos"]
    vivos = {k: x for k, x in nodos.items() if not x.get("deprecado")}
    ops = operaciones()
    por_id = {o["id_op"]: o for o in ops}

    titulo("0. EL SUELO: el grafo y lo reservado, tal como llegan a esta vuelta")
    print("  nodos en el grafo: %d, VIVOS: %d, deprecado: %d" % (
        len(nodos), len(vivos), len(nodos) - len(vivos)))
    print("  operaciones en OPERACIONES.jsonl: %d" % len(ops))
    for ruta, nombre in [(VEREDICTOS, "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"),
                         (COMPONENTES, "RECOMPUTO_3388_COMPONENTES.jsonl"),
                         (INVENTARIO, "docs/plan/INVENTARIO.jsonl")]:
        n = sum(1 for linea in open(ruta, encoding="utf-8") if linea.strip())
        print("  lineas de %-40s %d" % (nombre, n))
    clases = collections.Counter()
    por_dominio = collections.defaultdict(collections.Counter)
    puestos = []
    with open(VEREDICTOS, encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.strip()
            if not linea:
                continue
            v = json.loads(linea)
            clases[v.get("clase")] += 1
            por_dominio[v.get("dominio")][v.get("clase")] += 1
            puestos.append(v.get("puesto_intra"))
    total = sum(clases.values())
    print("  marcador recomputado del archivo: " + ", ".join(
        "%s %d (%.1f)" % (c, clases[c], 100.0 * clases[c] / total)
        for c in sorted(clases)))
    print("  puestos: %d a %d, huecos %d, duplicados %d" % (
        min(puestos), max(puestos),
        len(set(range(min(puestos), max(puestos) + 1)) - set(puestos)),
        len(puestos) - len(set(puestos))))
    print()
    print("  LA TASA POR DOMINIO, recomputada hoy (el cribado no se movio en esta vuelta):")
    print("    %-20s %6s %6s %6s %6s %6s %8s" % (
        "dominio", "pares", "A", "B", "C", "D", "tasa A"))
    for d in sorted(por_dominio):
        c = por_dominio[d]
        n = sum(c.values())
        print("    %-20s %6d %6d %6d %6d %6d %7.1f%%" % (
            d, n, c["A"], c["B"], c["C"], c["D"], 100.0 * c["A"] / n))

    titulo("1. LA FILA 7: los pasos de decision_de_vender_startup, y su historial con git")
    nid = "decision_de_vender_startup"
    pasos = len((vivos.get(nid) or {}).get("pasos_accionables") or [])
    print("  medido hoy en el grafo:                       %d pasos" % pasos)
    print("  01_FUENTES.md, tabla de LOS TRES CASOS:       25 pasos (cifra vieja, 11 ago 2026)")
    print("  fuente declarada: %s" % (vivos[nid].get("fuente") if nid in vivos else "AUSENTE"))
    print()
    print("  Los otros dos apartados de la misma tabla, para saber si el que diverge es uno solo:")
    for otro, pub in [("viral_loop_marketing", 30), ("coeficiente_viral", 16)]:
        hoy = len((vivos.get(otro) or {}).get("pasos_accionables") or [])
        print("    %-28s publica %2d, medido hoy %2d  %s" % (
            otro, pub, hoy, "CALZA" if hoy == pub else "DIFIERE"))
    print()
    print("  EL HISTORIAL DEL BLOB, verificado por mi con git en esta vuelta")
    print("  (la medicion es del auditor, acta de la vuelta 20 seccion 4 punto 1;")
    print("   aqui se REPRODUCE, no se copia):")
    ruta_rel = "dataset/metadata/master_graph.json"
    blobs = {}
    for commit, glosa in [("0e5e0c60", "9 ago 2026, ultimo commit que toca el grafo"),
                          ("23f9ac32", "11 ago 2026, el commit que CREA 01_FUENTES.md"),
                          ("HEAD", "hoy")]:
        b = git("rev-parse", "%s:%s" % (commit, ruta_rel))
        blobs[commit] = b
        print("    %-10s %-46s blob %s" % (commit, glosa, b))
    iguales = len(set(blobs.values())) == 1
    print("    LOS TRES BLOBS SON IDENTICOS: %s" % iguales)
    print()
    print("  Los pasos del nodo EN EL COMMIT QUE CREA 01_FUENTES.md (23f9ac32),")
    print("  leidos de ese blob y no del de hoy:")
    crudo = git("show", "23f9ac32:%s" % ruta_rel)
    if crudo.startswith("ERROR"):
        print("    %s" % crudo)
    else:
        viejo = json.loads(crudo)["nodos"].get(nid) or {}
        print("    pasos en 23f9ac32: %d" % len(viejo.get("pasos_accionables") or []))
        print("    CONSECUENCIA: si son 34 el 11 ago, el nodo NO crecio y el conteo")
        print("    viejo era PARCIAL DE NACIMIENTO.")

    titulo("2. LOS 13 DE OP-F-04-HOR CONTRA LOS 14 MEDIDOS: cual sobra, y donde tiene cobertura")
    seg = collections.defaultdict(set)
    for k, x in vivos.items():
        partes = segmentos(x)
        for nombre, pat in CANON:
            if any(pat in p for p in partes[1:]):
                seg[nombre].add(k)
    hor14 = seg["Horowitz"]
    op = por_id["OP-F-04-HOR"]
    hor13 = set(op["nodos"])
    print("  medidos hoy en el grafo (Horowitz en 2a o posterior posicion): %d" % len(hor14))
    print("  en el campo `nodos` de OP-F-04-HOR (fecha_corte %s):           %d" % (
        op["fecha_corte"], len(hor13)))
    print("  LA NOMINA DE LOS 13 EXISTE Y ES ESA. Sobran en el grafo: %s" % sorted(hor14 - hor13))
    print("  Estan en la operacion y no en el grafo:                  %s" % sorted(hor13 - hor14))
    sobra = sorted(hor14 - hor13)
    print()
    for s in sobra:
        print("  COBERTURA DE PLAN DE %s, barrida sobre las %d operaciones:" % (s, len(ops)))
        for o in ops:
            if s in (o.get("nodos") or []):
                print("     %-14s %-14s %-16s nodos: %d" % (
                    o["id_op"], o["fase"], o["tipo"], len(o["nodos"])))
        print("     menciones del id en los campos de texto de otras operaciones:")
        for o in ops:
            texto = json.dumps({k: v for k, v in o.items() if k != "nodos"},
                               ensure_ascii=False)
            if s in texto:
                print("        %-14s en %s" % (o["id_op"], o["fase"]))

    titulo("3. LA FORMA EN LOS 13 DE LA OPERACION: donde NO cierra el bloque de Horowitz")
    print("  La adjudicacion de OP-F-04-HOR dice que en los 13 el bloque esta")
    print("  'al final de los pasos'. Lo que el instrumento decide solo es si")
    print("  Horowitz ocupa la ULTIMA posicion declarada del campo fuente: un libro")
    print("  que no es el ultimo NO PUEDE tener el bloque final.")
    print()
    fuera = []
    for k in sorted(hor13 | hor14):
        x = vivos.get(k)
        if not x:
            print("  %-40s AUSENTE O DEPRECADO EN EL GRAFO" % k)
            continue
        partes = segmentos(x)
        pos = [i for i, p in enumerate(partes, 1) if "Hard Thing About Hard Thing" in p]
        if len(partes) not in pos:
            fuera.append(k)
            print("  %-40s Horowitz en posicion %s de %d; el ULTIMO declarado es: %s%s" % (
                k, pos, len(partes), partes[-1],
                "   [ESTA EN LOS 13 DE LA OPERACION]" if k in hor13 else ""))
    print()
    print("  de los 13 de la operacion, con Horowitz FUERA de la ultima posicion: %d  %s" % (
        len([k for k in fuera if k in hor13]), sorted(k for k in fuera if k in hor13)))
    print("  de los 14 medidos, con Horowitz FUERA de la ultima posicion:        %d  %s" % (
        len([k for k in fuera if k in hor14]), sorted(k for k in fuera if k in hor14)))
    print("  presencia del bloque: la lectura de pasos nodo por nodo esta en la tabla")
    print("  de la vuelta 20 de 01_FUENTES.md y se CITA, no se recuenta aqui.")

    titulo("4. EL MISMO LIBRO DOS VECES CON DOS GRAFIAS: dentro de la tanda y fuera")
    union = set().union(*[seg[b] for b in CUATRO])
    print("  nodos de la tanda de los cuatro (union): %d" % len(union))
    print()
    print("  DENTRO DE LA TANDA:")
    dentro, fuera_tanda = [], []
    for k in sorted(vivos):
        partes = segmentos(vivos[k])
        for nombre, pat in CANON:
            hits = [p for p in partes if pat in p]
            if len(hits) > 1:
                (dentro if k in union else fuera_tanda).append((k, nombre, hits))
    for k, nombre, hits in dentro:
        print("     %-32s %-9s x%d" % (k, nombre, len(hits)))
        for h in hits:
            print("        %s" % h)
    print()
    print("  FUERA DE LA TANDA (mismo criterio, sobre los %d vivos):" % len(vivos))
    for k, nombre, hits in fuera_tanda:
        print("     %-32s %-9s x%d" % (k, nombre, len(hits)))
        for h in hits:
            print("        %s" % h)

    titulo("5. RESUMEN DE LO QUE LOS CINCO REGISTROS VAN A ESCRIBIR")
    print("  1. fila 7: %d pasos hoy contra 25 publicados; blobs identicos: %s" % (
        pasos, iguales))
    print("  2. la nomina de los 13 vive en OP-F-04-HOR campo nodos; sobra: %s" % sobra)
    print("  3. de los 13, con el bloque fuera de la ultima posicion: %s" % (
        sorted(k for k in fuera if k in hor13)))
    print("  4. mismo libro dos veces con dos grafias: %d en la tanda, %d fuera" % (
        len(dentro), len(fuera_tanda)))
    print("  5. lo reservado NO se toca en esta vuelta: dataset/, veredictos,")
    print("     componentes y el campo `nodos` de las operaciones.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
