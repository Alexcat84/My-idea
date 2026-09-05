# -*- coding: utf-8 -*-
r"""vuelta170_tarea4b_registrar_puentes.py . TAREA 4.b de la vuelta 170.

REGISTRA LOS NODOS PUENTE DEL SALES ROADMAP **MEDIDOS Y SIN EJECUTARLOS**, CON
LA SALIDA DE `P.10` NOMBRADA Y CON EL MOTIVO DE LA NO EJECUCION ESCRITO.

POR QUE NACE (adjudicacion 6.10 del acta 169, la pregunta `P.4` del reporte de
la 169). Cerrar la cobertura de esa nomina dejo ver puentes de `P.10`, y `P.10`
nombra la salida sin ambiguedad porque el caso es su TERCERA fila literal:
*"fundir solo el subconjunto CERRADO y enlazar el resto, si todas las lecturas
estan hechas y aun asi se contradicen"*. Y todas lo estan.

PERO NO SE EJECUTA, Y EL MOTIVO ES DE `AUDITOR.md` SECCION 3: ninguna operacion
escrita recoge esta fusion, y ejecutar una fusion que ninguna ficha ordena es la
improvisacion que esa seccion prohibe con esas palabras. Asi que este
instrumento MIDE, COMPRUEBA QUE NADIE LA ORDENA, Y REGISTRA. No funde nada.

QUE MIDE, TODO CON EL RESOLUTOR DELANTE POR `P.1`:
  A. la nomina, parseada de `scripts/vuelta16_generar_actos.mjs` y no tecleada;
  B. las clases de sus pares, de las DOS sedes (la cola del cribado y las
     lecturas dirigidas de `LD_SALES_ROADMAP.md`);
  C. los puentes de `P.10`, computados de esas clases;
  D. LA BUSQUEDA NEGATIVA CON SU COMANDO (`EJECUTOR.md` 9, *"una busqueda
     negativa no se puede citar"*): que NINGUNA de las 71 operaciones escritas
     ordene fundir estos nodos. Se barren `nodos`, `preservar`, `eliminar` y
     `superviviente` de todas las fichas, y se nombra lo que salga.

Y DESPUES ESCRIBE, POR ADICION PURA, dentro del campo `nota` de `OP-L-02` que ya
existe. Cero claves nuevas de esquema, cero palabras viejas borradas.

USO:
  python scripts/loop/vuelta170_tarea4b_registrar_puentes.py
  python scripts/loop/vuelta170_tarea4b_registrar_puentes.py --aplicar
"""
import io
import itertools
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MJS = os.path.join(RAIZ, "scripts", "vuelta16_generar_actos.mjs")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
OPERACIONES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
LD_SALES = os.path.join(RAIZ, "docs", "plan", "LD_SALES_ROADMAP.md")
FICHA = "OP-L-02"
CORTE = "2026-09-04"

PAT_LD = re.compile(
    r"^#+\s*`(LD-\d+)`\s*\.\s*`([a-z0-9_]+)`\s*contra\s*`([a-z0-9_]+)`\s*\.\s*\*\*([^*]+)\*\*",
    re.M)


def cargar(p):
    return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]


def main():
    aplicar = "--aplicar" in sys.argv
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 170, TAREA 4.b: LOS PUENTES DEL SALES ROADMAP, REGISTRADOS Y NO")
    print("EJECUTADOS")
    print("=" * 78)
    print("")

    print("A) LA NOMINA, PARSEADA DE SU FICHERO Y NO TECLEADA")
    texto = io.open(MJS, encoding="utf-8").read()
    m = re.search(r"const NOMINAS_OP_L_02 = \[(.*?)\n\];", texto, re.S)
    if not m:
        print("   ROJO: no se encuentra NOMINAS_OP_L_02.")
        return 1
    filas = re.findall(r"\[([^\]]*)\]", m.group(1))
    nominas = [re.findall(r'"([a-z0-9_]+)"', f) for f in filas]
    mem = nominas[0]
    print("   scripts/vuelta16_generar_actos.mjs: %d nominas" % len(nominas))
    print("   la PRIMERA, el lote del sales roadmap: %d miembros escritos" % len(mem))
    for x in mem:
        print("      %s" % x)
    print("")

    print("B) LOS PARES, CON EL RESOLUTOR DELANTE (P.1)")
    G = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    ALIAS = dict((a, k) for k, v in G.items() for a in (v.get("ids_alias") or []))

    def res(x):
        visto = set()
        while x in ALIAS and x not in visto:
            visto.add(x)
            x = ALIAS[x]
        return x

    vivos = sorted(set(res(x) for x in mem))
    pares = [tuple(sorted(p)) for p in itertools.combinations(vivos, 2)]
    print("   miembros escritos %d | vivos tras resolver %d | colapsados %d"
          % (len(mem), len(vivos), len(mem) - len(vivos)))
    print("   CIFRA pares posibles entre los vivos: %d" % len(pares))
    print("")

    print("C) LAS CLASES, DE SUS DOS SEDES")
    clase_de = {}
    origen = {}
    for r in cargar(VEREDICTOS):
        p = tuple(sorted((res(r["nodo_a"]), res(r["nodo_b"]))))
        if p in pares:
            clase_de[p] = r["clase"]
            origen[p] = "cola, puesto %s" % r["puesto_intra"]
    de_cola = len(clase_de)
    hallados = PAT_LD.findall(io.open(LD_SALES, encoding="utf-8").read())
    for ld, a, b, clase in hallados:
        p = tuple(sorted((res(a), res(b))))
        if p in pares:
            clase_de[p] = clase.strip().split()[0]
            origen[p] = ld
    print("   sede 1, docs/INTRA_DOMINIO_VEREDICTOS.jsonl: %d pares" % de_cola)
    print("   sede 2, docs/plan/LD_SALES_ROADMAP.md: %d cabeceras LD" % len(hallados))
    print("   CIFRA pares con clase: %d de %d" % (len(clase_de), len(pares)))
    sin_clase = [p for p in pares if p not in clase_de]
    print("   CIFRA pares SIN clase: %d" % len(sin_clase))
    for p in sin_clase:
        print("      SIN CLASE: %s contra %s" % p)
    for p in sorted(pares):
        print("      %-2s  %-22s  %s contra %s"
              % (clase_de.get(p, "??"), origen.get(p, "(sin sede)"), p[0], p[1]))
    if sin_clase:
        print("   ROJO: la cobertura no es completa; los puentes no se pueden computar.")
        return 1
    print("")

    print("D) LOS PUENTES DE P.10, COMPUTADOS DE ESAS CLASES")
    print("   P.10: un nodo con A hacia dos nodos que entre si dan D.")
    puentes = []
    for nodo in vivos:
        aes = [o for o in vivos if o != nodo
               and clase_de.get(tuple(sorted((nodo, o))), "").startswith("A")]
        for x, y in itertools.combinations(sorted(aes), 2):
            if clase_de.get(tuple(sorted((x, y)))) == "D":
                puentes.append((nodo, x, y))
    print("   CIFRA puentes: %d" % len(puentes))
    for n, x, y in puentes:
        print("      puente `%s` sobre (`%s` , `%s`)" % (n, x, y))
    print("   CONTRASTE, y es contraste y no fuente: el reporte de la 169 y el acta")
    print("   169 dicen CINCO. Yo computo %d, %s"
          % (len(puentes), "CALZA" if len(puentes) == 5 else "NO CALZA"))
    dobles = {}
    for n, x, y in puentes:
        dobles.setdefault((x, y), []).append(n)
    costuras = dict((k, v) for k, v in dobles.items() if len(v) > 1)
    print("   CIFRA pares con MAS DE UN puente encima (costura, por P.10): %d"
          % len(costuras))
    for (x, y), ns in sorted(costuras.items()):
        print("      sobre (`%s` , `%s`) hacen de puente: %s" % (x, y, ", ".join(ns)))
    print("")

    print("E) LA BUSQUEDA NEGATIVA, CON SU COMANDO (EJECUTOR.md 9)")
    print("   'una busqueda negativa no se puede citar', asi que se barre y se nombra")
    print("   lo que salga. Se buscan los %d nodos vivos en los campos `nodos`,"
          % len(vivos))
    print("   `preservar`, `eliminar` y `superviviente` de TODAS las fichas.")
    fichas = cargar(OPERACIONES)
    tocan = []
    for f in fichas:
        cae = set()
        for campo in ("nodos", "preservar", "eliminar"):
            for x in (f.get(campo) or []):
                if res(x) in vivos:
                    cae.add(x)
        s = f.get("superviviente")
        if s and res(s) in vivos:
            cae.add(s)
        if cae:
            tocan.append((f.get("id_op"), f.get("tipo"), f.get("estado"), sorted(cae)))
    print("   CIFRA fichas barridas: %d" % len(fichas))
    print("   CIFRA fichas que NOMBRAN alguno de estos nodos como sujeto de"
          " fusion: %d" % len(tocan))
    for id_op, tipo, estado, cae in tocan:
        print("      %s (%s, %s): %s" % (id_op, tipo, estado, ", ".join(cae)))
    print("")

    print("F) LO QUE SE VA A REGISTRAR, Y LO QUE NO SE VA A HACER")
    print("   SE REGISTRA: los %d puentes con su medicion y con la salida de P.10"
          % len(puentes))
    print("   nombrada (su TERCERA fila: fundir solo el subconjunto CERRADO y")
    print("   enlazar el resto).")
    print("   NO SE EJECUTA: ninguna fusion, ningun nodo, ninguna arista.")
    print("   MOTIVO, y es de AUDITOR.md seccion 3: %s"
          % ("ninguna operacion escrita ordena esta fusion"
             if not tocan else
             "hay %d ficha(s) que nombran estos nodos, y se nombran arriba" % len(tocan)))
    print("")

    lineas = [l for l in io.open(OPERACIONES, encoding="utf-8") if l.strip()]
    idx = [i for i, f in enumerate(fichas) if f.get("id_op") == FICHA]
    if len(idx) != 1:
        print("   ROJO: %s aparece %d veces." % (FICHA, len(idx)))
        return 1
    i = idx[0]
    nota = fichas[i].get("nota") or ""

    registro = (
        " REGISTRO DE LOS NODOS PUENTE, POR ADICION (%(corte)s, vuelta 170, TAREA "
        "4.b; adjudicacion 6.10 del acta 169). SE REGISTRAN MEDIDOS Y NO SE "
        "EJECUTAN, y las dos mitades de esa frase llevan su motivo escrito. "
        "LA MEDICION, hecha en esta vuelta con el resolutor delante por P.1 y con "
        "la nomina parseada de scripts/vuelta16_generar_actos.mjs (no tecleada): "
        "%(mem)d miembros escritos, %(vivos)d vivos tras resolver, %(pares)d pares "
        "posibles, %(conclase)d con clase y CERO sin clase, leidos de sus DOS "
        "sedes (%(cola)d de la cola de docs/INTRA_DOMINIO_VEREDICTOS.jsonl y el "
        "resto de las cabeceras LD de docs/plan/LD_SALES_ROADMAP.md). "
        "LOS %(np)d PUENTES DE P.10, computados de esas clases y no copiados de "
        "ningun acta: %(lista)s. Y %(ncost)d de esos pares llevan MAS DE UN puente "
        "encima, que es lo que P.10 llama COSTURA y no punto debil: %(costuras)s. "
        "LA SALIDA DE P.10 ESTA NOMBRADA Y NO SE ELIGE AQUI: el caso es su TERCERA "
        "fila literal, 'fundir solo el subconjunto CERRADO y enlazar el resto, si "
        "todas las lecturas estan hechas y aun asi se contradicen', porque la "
        "cobertura es 15 de 15 y por tanto la primera salida, la unica que resuelve "
        "de verdad, YA NO EXISTE. "
        "POR QUE NO SE EJECUTA HOY, Y ES DE AUDITOR.md SECCION 3: NINGUNA OPERACION "
        "ESCRITA RECOGE ESTA FUSION, y ejecutar una fusion que ninguna ficha ordena "
        "es la improvisacion que esa seccion prohibe con esas palabras. LA BUSQUEDA "
        "NEGATIVA SE HIZO CON SU COMANDO en vez de citarse (EJECUTOR.md 9): se "
        "barrieron las %(nfichas)d fichas de docs/plan/OPERACIONES.jsonl buscando "
        "estos nodos en los campos nodos, preservar, eliminar y superviviente, y "
        "salieron %(ntocan)s. "
        "QUEDAN ESPERANDO a la operacion que abra este acto por P.5 y P.8, y hasta "
        "entonces esta entrada es su unica sede. Salida: "
        "docs/loop/SALIDA_V170_T4B_PUENTES.txt. "
        "LO QUE ESTE REGISTRO NO HACE: no funde nada, no adjudica clase a ningun "
        "par, no mueve ni un veredicto, no toca ni un nodo ni una arista, no "
        "escribe operacion nueva y no cambia el estado ni las dependencias de esta "
        "ficha ni de ninguna otra."
        % dict(corte=CORTE, mem=len(mem), vivos=len(vivos), pares=len(pares),
               conclase=len(clase_de), cola=de_cola, np=len(puentes),
               lista="; ".join("`%s` sobre (`%s`, `%s`)" % p for p in puentes),
               ncost=len(costuras),
               costuras="; ".join("sobre (`%s`, `%s`) hacen de puente %s"
                                  % (x, y, " y ".join(ns))
                                  for (x, y), ns in sorted(costuras.items()))
               or "ninguno",
               nfichas=len(fichas),
               ntocan=("CERO" if not tocan
                       else "%d, nombradas en la salida" % len(tocan))))

    nota_nueva = nota + registro
    print("G) LA GUARDA DE ADICION")
    print("   la nota pasa de %d a %d caracteres, y SOLO CRECE: %s"
          % (len(nota), len(nota_nueva), len(nota_nueva) > len(nota)))
    print("   la nota vieja sigue entera dentro: %s" % (nota in nota_nueva))
    if nota not in nota_nueva or len(nota_nueva) <= len(nota):
        print("   ROJO: no se escribe nada.")
        return 1
    print("")

    if not aplicar:
        print("MODO MEDICION: la ficha NO se toca. Corre con --aplicar para escribir.")
        return 0

    nueva = dict(fichas[i])
    nueva["nota"] = nota_nueva
    movidos = [k for k in fichas[i] if k != "nota" and fichas[i][k] != nueva.get(k)]
    print("H) EL ESQUEMA NO CRECE Y NADA MAS SE MUEVE")
    print("   claves antes %d, despues %d | campos movidos de mas: %d %s"
          % (len(fichas[i]), len(nueva), len(movidos), movidos))
    print("   estado antes %r, despues %r"
          % (fichas[i].get("estado"), nueva.get("estado")))
    if len(nueva) != len(fichas[i]) or movidos:
        print("   ROJO: se movio algo que no tocaba.")
        return 1
    lineas[i] = json.dumps(nueva, ensure_ascii=False) + "\n"
    io.open(OPERACIONES, "w", encoding="utf-8", newline="\n").writelines(lineas)

    despues = cargar(OPERACIONES)
    print("")
    print("I) ESCRITO, Y RECONTADO DESPUES DE ESCRIBIR")
    print("   CIFRA fichas antes %d, despues %d" % (len(fichas), len(despues)))
    print("   %s sigue en la linea %d: %s"
          % (FICHA, i + 1, despues[i].get("id_op") == FICHA))
    print("   CIFRA caracteres de la nota en disco: %d" % len(despues[i]["nota"]))
    print("   los %d puentes se nombran en la nota de disco: %d de %d"
          % (len(puentes),
             sum(1 for n, x, y in puentes
                 if ("`%s` sobre (`%s`, `%s`)" % (n, x, y)) in despues[i]["nota"]),
             len(puentes)))
    if len(despues) != len(fichas) or despues[i].get("id_op") != FICHA:
        print("   ROJO: el fichero cambio de forma.")
        return 1
    print("")
    print("VERDE: los %d puentes quedan REGISTRADOS y SIN EJECUTAR." % len(puentes))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
