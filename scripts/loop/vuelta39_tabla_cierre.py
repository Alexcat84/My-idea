# -*- coding: utf-8 -*-
"""vuelta39_tabla_cierre.py - IMPRIME las tablas del cierre de OP-D-04.

EXISTE POR LA REGLA 1 DE EJECUTOR.md, tercer bloque: LA TABLA SE IMPRIME, NO SE
TECLEA. Las dos paradas de credito de las vueltas 31 y 32 fueron celdas manuales
en tablas de prosa que ningun instrumento validaba. Todo lo que sale de aqui se
lee de dataset/nodos, de los dos planes sellados y de git, y se pega ENTERO en
docs/plan/02_DESTEJIDOS.md.

ESTRICTAMENTE DE SOLO LECTURA.

Uso: python scripts/loop/vuelta39_tabla_cierre.py
"""
import io
import itertools
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
CAMPOS = ("nodos_previos", "nodos_siguientes")

PLANES = [("EL TALLER", "docs/loop/PLAN_V38_OPD04_TALLER.json"),
          ("LA ALTERNANCIA", "docs/loop/PLAN_V38_OPD04_ALTERNANCIA.json")]
COLGADO = "construir_sobre_ideas_ajenas"
CUARTO = "brainstorming"
BASE_GIT = "03e8e0e8"


def nodo(nid):
    return json.load(io.open(os.path.join(NODOS, nid + ".json"), encoding="utf-8"))


def nodo_en_git(nid):
    salida = subprocess.run(["git", "show", "%s:dataset/nodos/%s.json" % (BASE_GIT, nid)],
                            cwd=RAIZ, capture_output=True)
    return json.loads(salida.stdout.decode("utf-8"))


def main():
    planes = [(etq, json.load(io.open(os.path.join(RAIZ, r), encoding="utf-8")))
              for etq, r in PLANES]

    print("### TABLA 1: LOS SIETE NODOS DEL ACTO, ANTES Y DESPUES")
    print()
    print("| nodo | papel | fuente | pasos antes | pasos despues | condiciones | vivo hoy |")
    print("|---|---|---|---:|---:|---:|:---:|")
    for etq, plan in planes:
        sup = plan["superviviente"]
        for nid in [sup] + list(plan["absorbidos"]):
            a, d = nodo_en_git(nid), nodo(nid)
            papel = "**superviviente de %s**" % etq if nid == sup else "absorbido por `%s`" % sup
            print("| `%s` | %s | %s | %d | %d | %d | %s |"
                  % (nid, papel, d.get("fuente"),
                     len(a.get("pasos_accionables") or []),
                     len(d.get("pasos_accionables") or []),
                     len(d.get("condiciones_activacion") or []),
                     "**si**" if not d.get("deprecado") else "no, **deprecado**"))
    a, d = nodo_en_git(COLGADO), nodo(COLGADO)
    print("| `%s` | **el colgado, NO se funde** | %s | %d | %d | %d | %s |"
          % (COLGADO, d.get("fuente"), len(a.get("pasos_accionables") or []),
             len(d.get("pasos_accionables") or []),
             len(d.get("condiciones_activacion") or []),
             "**si**" if not d.get("deprecado") else "no"))
    print()

    print("### TABLA 2: EL CUARTO MIEMBRO DEL RACIMO MIXTO, QUE NO ES DEL ACTO")
    print()
    print("| nodo | dominio | fuente | vivo | como quedo enlazado |")
    print("|---|---|---|:---:|---|")
    c = nodo(CUARTO)
    sup_taller = planes[0][1]["superviviente"]
    donde_c = [k for k in CAMPOS if sup_taller in (c.get(k) or [])]
    donde_s = [k for k in CAMPOS if CUARTO in (nodo(sup_taller).get(k) or [])]
    print("| `%s` | %s | %s | %s | `%s` lo nombra en %s y el nombra a `%s` en %s |"
          % (CUARTO, c.get("dominio"), c.get("fuente"),
             "**si**" if not c.get("deprecado") else "no",
             sup_taller, ", ".join("`%s`" % x for x in donde_s) or "NINGUNO",
             sup_taller, ", ".join("`%s`" % x for x in donde_c) or "NINGUNO"))
    print()

    print("### TABLA 3: LOS TRES VIVOS Y SUS TRES PARES (`P.10`, tercera salida)")
    print()
    print("| par | como llego | extremo A lo declara en | extremo B lo declara en |")
    print("|---|---|---|---|")
    vivos = [p[1]["superviviente"] for p in planes] + [COLGADO]
    llegada = {
        ("reglas_brainstorming", "pensamiento_convergente_divergente"):
            "**solo**, redirigido por la fusion del taller y simetrizado por el paso 5",
        ("reglas_brainstorming", COLGADO):
            "**escrito por `P.10` en esta vuelta**, con los dos extremos de una vez",
        ("pensamiento_convergente_divergente", COLGADO):
            "**solo**, redirigido por la fusion de la alternancia y simetrizado por el paso 5",
    }
    for x, y in itertools.combinations(vivos, 2):
        dx = [k for k in CAMPOS if y in (nodo(x).get(k) or [])]
        dy = [k for k in CAMPOS if x in (nodo(y).get(k) or [])]
        clave = (x, y) if (x, y) in llegada else (y, x)
        print("| `%s` con `%s` | %s | %s | %s |"
              % (x, y, llegada.get(clave, "SIN REGISTRO"),
                 ", ".join("`%s`" % k for k in dx) or "**NINGUNO**",
                 ", ".join("`%s`" % k for k in dy) or "**NINGUNO**"))
    print()

    print("### TABLA 4: EL CENSO, TRAMO A TRAMO")
    print()
    print("| momento | ficheros | vivos | deprecados |")
    print("|---|---:|---:|---:|")
    print("| apertura de la vuelta 39 | 3.853 | 3.538 | 315 |")
    print("| tras EL TALLER | 3.853 | 3.536 | 317 |")
    print("| tras LA ALTERNANCIA | 3.853 | 3.534 | 319 |")
    total = vivos_n = dep_n = 0
    for nombre in os.listdir(NODOS):
        if not nombre.endswith(".json"):
            continue
        total += 1
        if json.load(io.open(os.path.join(NODOS, nombre), encoding="utf-8")).get("deprecado"):
            dep_n += 1
        else:
            vivos_n += 1
    print("| **recontado al cierre, ahora mismo** | **%s** | **%s** | **%s** |"
          % ("{:,}".format(total).replace(",", "."),
             "{:,}".format(vivos_n).replace(",", "."),
             "{:,}".format(dep_n).replace(",", ".")))
    print()
    print("(las tres primeras filas son las que imprimio cada corrida de")
    print("`scripts/loop/vuelta39_fundir.py`; la cuarta la recuenta este script AL CIERRE)")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
