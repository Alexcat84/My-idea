# -*- coding: utf-8 -*-
r"""vuelta170_tarea5b_veredicto_op_l_02.py . TAREA 5.b de la vuelta 170.

MIDE LAS TRES CLAUSULAS DE `OP-L-02` UNA A UNA Y DICE SI QUEDAN CUMPLIDAS, CON
LA MEDICION DELANTE. Y SI QUEDAN, ABRE `OP-L-03` LEYENDO SUS CLAUSULAS DE SU
FICHA, SIN EJECUTAR NADA.

LO QUE ESTE INSTRUMENTO NO HACE, Y ES LO MAS IMPORTANTE QUE HACE: **NO TOCA EL
CAMPO `estado`.** Por la decision del fundador del 4 sep 2026 ese campo esta
jubilado como historico y NO ES LA VARA; la vara del trabajo pendiente es
`scripts/loop/vuelta150_3_relectura_expediente.py`. Un instrumento que
"cerrara" una operacion moviendo `estado` estaria escribiendo en el sitio que
la casa acaba de declarar que no manda.

LAS TRES CLAUSULAS SE LEEN DE LA FICHA, NO SE TECLEAN: se sacan del campo
`verificacion` de `OP-L-02`, y las que son CORRECCIONES DECLARADAS se separan de
las clausulas propiamente dichas, porque una correccion no es una clausula que
cumplir.

COMO SE MIDE CADA UNA:
  1. *"las tres nominas afectadas quedan con cobertura COMPLETA y su forma
     reescrita"*: cobertura de las nominas de `OP-L-02` con el resolutor
     delante, y `forma` de sus entradas del inventario, comprobando que llevan
     el corte de HOY escrito.
  2. *"el marcador del cribado no se mueve: sigue en 2.117"*: se lee como la
     clausula dice (que la OPERACION no lo mueva), y se prueba con `git diff`
     entre el commit de apertura de esta vuelta y HEAD sobre el fichero del
     archivo, mas el recomputo del marcador.
  3. *"cada grupo del backlog lleva su motivo escrito, no solo su cuenta"*: se
     cuenta la tabla del backlog de `LECTURAS_DIRIGIDAS.md` fila a fila y se
     comprueba que la celda de motivo de cada fila no esta vacia.

Y DESPUES ABRE `OP-L-03` LEYENDO SUS CLAUSULAS, sin ejecutar ninguna: el encargo
dice "empezando por leer sus cuatro clausulas en su ficha antes de ejecutar
nada", y si la ficha trae un numero distinto de cuatro, se publica el que trae.

USO:
  python scripts/loop/vuelta170_tarea5b_veredicto_op_l_02.py
"""
import collections
import io
import itertools
import json
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPERACIONES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
INVENTARIO = os.path.join(RAIZ, "docs", "plan", "INVENTARIO.jsonl")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
LECTURAS = os.path.join(RAIZ, "docs", "plan", "LECTURAS_DIRIGIDAS.md")
MJS = os.path.join(RAIZ, "scripts", "vuelta16_generar_actos.mjs")
SELLO = os.path.join(RAIZ, "docs", "loop", "SALIDA_V170_HEAD_APERTURA.txt")
CORTE = "2026-09-04"

LAS_TRES = ["los cuadrantes de mercado", "la ecuacion de valor",
            "la supervision de la IA"]


def cargar(p):
    return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 170, TAREA 5.b: LAS TRES CLAUSULAS DE OP-L-02, MEDIDAS UNA A UNA")
    print("=" * 78)
    print("")

    fichas = cargar(OPERACIONES)
    idx = [i for i, f in enumerate(fichas) if f.get("id_op") == "OP-L-02"]
    if len(idx) != 1:
        print("ROJO: OP-L-02 aparece %d veces." % len(idx))
        return 1
    ficha = fichas[idx[0]]
    verif = ficha.get("verificacion") or []

    print("A) LAS CLAUSULAS, LEIDAS DE LA FICHA Y NO TECLEADAS")
    print("   CIFRA elementos de `verificacion`: %d" % len(verif))
    clausulas = [v for v in verif if not v.startswith("CORRECCION DECLARADA")]
    correcciones = [v for v in verif if v.startswith("CORRECCION DECLARADA")]
    print("   CIFRA clausulas propiamente dichas: %d" % len(clausulas))
    print("   CIFRA correcciones declaradas (no son clausulas que cumplir): %d"
          % len(correcciones))
    for k, c in enumerate(clausulas, 1):
        print("      %d. %s" % (k, c))
    print("")

    veredictos = []

    # ------------------------------------------------------------ clausula 1
    print("B) CLAUSULA 1: cobertura COMPLETA y forma reescrita")
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
        cola[tuple(sorted((res(r["nodo_a"]), res(r["nodo_b"]))))] = r["clase"]
    texto_plan = ""
    dirig = {}
    plan = os.path.join(RAIZ, "docs", "plan")
    pat_cab = re.compile(
        r"^#{1,4}\s+`(LD-\d+)`\s*\.\s*`([a-z0-9_]+)`\s+contra\s+`([a-z0-9_]+)`\s*\.\s*\*\*([A-Z ]+)\*\*",
        re.M)
    pat_fila = re.compile(
        r"^\|\s*\**`([a-z0-9_]+)`\**\s+contra\s+\**`([a-z0-9_]+)`\**\s*\|\s*\**([A-Z][A-Z ]*?)\**\s*\|\s*$",
        re.M)
    for nombre in sorted(os.listdir(plan)):
        if not nombre.endswith(".md"):
            continue
        t = io.open(os.path.join(plan, nombre), encoding="utf-8").read()
        for _ld, a, b, cl in pat_cab.findall(t):
            dirig[tuple(sorted((res(a), res(b))))] = cl.strip().split()[0]
        for a, b, cl in pat_fila.findall(t):
            dirig[tuple(sorted((res(a), res(b))))] = cl.strip().split()[0]
        texto_plan += t

    texto = io.open(MJS, encoding="utf-8").read()
    m = re.search(r"const NOMINAS_OP_L_02 = \[(.*?)\n\];", texto, re.S)
    nominas = [re.findall(r'"([a-z0-9_]+)"', f)
               for f in re.findall(r"\[([^\]]*)\]", m.group(1))]
    print("   NOMINAS_OP_L_02 parseadas del fichero: %d" % len(nominas))
    print("   | # | miembros | vivos | posibles | leidos | SIN | cobertura |")
    print("   |---:|---:|---:|---:|---:|---:|---|")
    sin_total = 0
    for k, nom in enumerate(nominas, 1):
        vivos = sorted(set(res(x) for x in nom))
        pares = [tuple(sorted(p)) for p in itertools.combinations(vivos, 2)]
        sin = [p for p in pares if p not in cola and p not in dirig]
        sin_total += len(sin)
        print("   | %d | %d | %d | %d | %d | %d | %d de %d |"
              % (k, len(nom), len(vivos), len(pares), len(pares) - len(sin),
                 len(sin), len(pares) - len(sin), len(pares)))
    print("   CIFRA pares SIN veredicto en las SEIS nominas: %d" % sin_total)

    inv = cargar(INVENTARIO)
    con_corte = 0
    for nombre in LAS_TRES:
        e = [x for x in inv if x.get("nombre") == nombre]
        if not e:
            print("   ROJO: %r no esta en el inventario." % nombre)
            return 1
        f = e[0].get("forma") or ""
        c = e[0].get("cobertura") or ""
        ok = (CORTE in f and CORTE in c)
        con_corte += 1 if ok else 0
        print("   %-30s forma reescrita con el corte %s: %s | %d caracteres"
              % (nombre, CORTE, "SI" if ok else "NO", len(f)))
    cumple1 = (sin_total == 0 and con_corte == len(LAS_TRES))
    print("   VEREDICTO CLAUSULA 1: %s" % ("CUMPLIDA" if cumple1 else "NO CUMPLIDA"))
    veredictos.append(("1", cumple1))
    print("")

    # ------------------------------------------------------------ clausula 2
    print("C) CLAUSULA 2: el marcador del cribado no se mueve")
    print("   LA CLAUSULA DICE QUE LA OPERACION NO LO MUEVA, no que valga 2.117 hoy,")
    print("   y desde la TAREA 3 de esta vuelta esa lectura esta escrita en la ficha")
    print("   con su fecha de corte al lado, por 9.21.")
    clases = collections.Counter(r["clase"] for r in V)
    print("   marcador recomputado del archivo HOY: %d filas (%s)"
          % (len(V), ", ".join("%s %d" % (k, clases[k]) for k in sorted(clases))))
    head_ap = io.open(SELLO, encoding="utf-8").read().strip() if os.path.exists(SELLO) else ""
    print("   HEAD de apertura, leido del sello: %s" % (head_ap[:8] or "(no hay sello)"))
    if not head_ap:
        print("   ROJO: sin sello de apertura no se puede probar que no se movio.")
        return 1
    c, dif = git(["diff", head_ap, "HEAD", "--numstat", "--",
                  "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"])
    filas = [l for l in dif.splitlines() if l.strip()]
    print("   git diff %s HEAD --numstat -- docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
          % head_ap[:8])
    print("   CIFRA filas del numstat: %d" % len(filas))
    for l in filas:
        print("      %s" % l)
    c, dif2 = git(["diff", "--numstat", "--", "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"])
    filas2 = [l for l in dif2.splitlines() if l.strip()]
    print("   y sin commitear (arbol de trabajo): %d filas" % len(filas2))
    cumple2 = (len(filas) == 0 and len(filas2) == 0)
    print("   VEREDICTO CLAUSULA 2: %s" % ("CUMPLIDA" if cumple2 else "NO CUMPLIDA"))
    veredictos.append(("2", cumple2))
    print("")

    # ------------------------------------------------------------ clausula 3
    print("D) CLAUSULA 3: cada grupo del backlog lleva su motivo escrito")
    lin = io.open(LECTURAS, encoding="utf-8").read().split(chr(10))
    cab = [i for i, l in enumerate(lin, 1)
           if l.strip().startswith("| grupo | pares | motivo")]
    print("   CIFRA tablas del backlog halladas en LECTURAS_DIRIGIDAS.md: %d" % len(cab))
    grupos = []
    for n in cab:
        k = n + 2
        while k <= len(lin) and lin[k - 1].strip().startswith("|"):
            celdas = [x.strip() for x in lin[k - 1].strip().strip("|").split("|")]
            if len(celdas) >= 3 and celdas[0]:
                grupos.append((k, celdas[0], celdas[1], celdas[2]))
            k += 1
    print("   CIFRA grupos del backlog: %d" % len(grupos))
    sin_motivo = []
    for k, g, p, mot in grupos:
        tiene = bool(mot.strip()) and len(mot.strip()) > 10
        if not tiene:
            sin_motivo.append(g)
        print("   linea %-5d %-8s %-46s motivo escrito: %s (%d caracteres)"
              % (k, p[:8], g[:46], "SI" if tiene else "NO", len(mot.strip())))
    cumple3 = (len(grupos) > 0 and not sin_motivo)
    print("   CIFRA grupos SIN motivo escrito: %d %s" % (len(sin_motivo), sin_motivo))
    print("   VEREDICTO CLAUSULA 3: %s" % ("CUMPLIDA" if cumple3 else "NO CUMPLIDA"))
    veredictos.append(("3", cumple3))
    print("")

    print("E) EL VEREDICTO DE OP-L-02, CON LA MEDICION DELANTE")
    for n, ok in veredictos:
        print("   clausula %s: %s" % (n, "CUMPLIDA" if ok else "NO CUMPLIDA"))
    todas = all(ok for _n, ok in veredictos)
    print("   CIFRA clausulas cumplidas: %d de %d"
          % (sum(1 for _n, ok in veredictos if ok), len(veredictos)))
    print("   EL CAMPO `estado` NO SE TOCA, y sigue diciendo %r. No es la vara."
          % ficha.get("estado"))
    print("")

    print("F) LA VARA DEL TRABAJO PENDIENTE, QUE ES EL INSTRUMENTO Y NO EL CAMPO")
    print("   comando: python scripts/loop/vuelta150_3_relectura_expediente.py --corte HEAD")
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run([sys.executable,
                        "scripts/loop/vuelta150_3_relectura_expediente.py",
                        "--corte", "HEAD"], cwd=RAIZ, capture_output=True, env=env)
    sal = r.stdout.decode("utf-8", errors="replace") + r.stderr.decode("utf-8", errors="replace")
    for l in sal.splitlines():
        if re.search(r"CIFRA|OP-L-02|OP-L-03|LISTA sin", l):
            print("   %s" % l.strip())
    print("   exit del instrumento: %d" % r.returncode)
    print("")

    if not todas:
        print("OP-L-02 NO QUEDA CUMPLIDA. NO se abre OP-L-03: el encargo dice")
        print("'solo entonces', y este instrumento lo obedece.")
        return 0

    print("G) OP-L-03 SE ABRE LEYENDO SUS CLAUSULAS, Y NO SE EJECUTA NINGUNA")
    idx3 = [i for i, f in enumerate(fichas) if f.get("id_op") == "OP-L-03"]
    if len(idx3) != 1:
        print("   ROJO: OP-L-03 aparece %d veces." % len(idx3))
        return 1
    f3 = fichas[idx3[0]]
    v3 = f3.get("verificacion") or []
    cl3 = [v for v in v3 if not v.startswith("CORRECCION DECLARADA")]
    co3 = [v for v in v3 if v.startswith("CORRECCION DECLARADA")]
    print("   ficha OP-L-03: linea %d, tipo %s, estado %r, fecha_corte %s"
          % (idx3[0] + 1, f3.get("tipo"), f3.get("estado"), f3.get("fecha_corte")))
    print("   depende_de: %s | bloquea_a: %s" % (f3.get("depende_de"), f3.get("bloquea_a")))
    print("   CIFRA elementos de `verificacion`: %d" % len(v3))
    print("   CIFRA clausulas propiamente dichas: %d" % len(cl3))
    print("   CIFRA correcciones declaradas: %d" % len(co3))
    print("   CONTRASTE, y es contraste y no fuente: el encargo dice CUATRO clausulas.")
    print("   yo cuento %d, %s" % (len(cl3), "CALZA" if len(cl3) == 4 else "NO CALZA"))
    for k, c in enumerate(cl3, 1):
        print("      %d. %s" % (k, c))
    print("   adjudicacion: %s" % (f3.get("adjudicacion") or "(vacia)")[:400])
    print("")
    print("   NO SE EJECUTA NINGUNA DE ELLAS EN ESTA VUELTA: el encargo manda")
    print("   'empezando por leer sus cuatro clausulas en su ficha antes de ejecutar")
    print("   nada', y esta vuelta ya ha entregado sus cinco tareas. Lo leido queda")
    print("   en el reporte para que la vuelta siguiente empiece con la ficha abierta")
    print("   y no con la ficha por abrir.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
