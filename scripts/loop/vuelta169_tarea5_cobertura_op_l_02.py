# -*- coding: utf-8 -*-
r"""vuelta169_tarea5_cobertura_op_l_02.py . LA COBERTURA DE LAS SEIS NOMINAS DE
`OP-L-02`, RECOMPUTADA CON EL RESOLUTOR DELANTE (TAREA 5 de la vuelta 169).

POR QUE NACE ASI Y NO A MANO. El encargo de la vuelta 169 manda empezar por el
lote de sales roadmap, *"cinco pares"*, con la cifra de la vuelta 168 delante:
15 pares posibles, 10 CON veredicto y 5 SIN. `EJECUTOR.md` 2 dice que ninguna
nota vieja es fuente de una cifra nueva, y `EJECUTOR.md` 9 que todo conteo que
toque ids pasa por el resolutor antes de contar (`P.1`). Asi que la cobertura
NO se hereda del encargo: se recomputa aqui, nomina por nomina, y si discrepa
del encargo la discrepancia SE DECLARA en vez de resolverse copiando.

DE DONDE SALE CADA COSA, Y LAS TRES SEDES NO SE MEZCLAN:
  1. LA NOMINA sale de `scripts/vuelta16_generar_actos.mjs`, de su constante
     `NOMINAS_OP_L_02`, PARSEADA DEL FICHERO. No se teclea ni un id: si alguien
     cambia esa constante, esta medicion cambia con ella.
  2. LOS VEREDICTOS DE COLA salen de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`.
  3. LAS LECTURAS DIRIGIDAS salen de las cabeceras de `docs/plan/*.md` con la
     forma `### `LD-nn` . `a` contra `b` . **CLASE**`. Son OTRA sede y van
     contadas APARTE, porque una lectura dirigida NO entra en la cola y NO mueve
     el marcador: esa es su definicion escrita.

EL RESOLUTOR ES EL DE LA CASA, con la misma semantica que
`scripts/plan/recomputo_3388.py`: camina la cadena de `ids_alias` hasta el id
final sin ciclar. Se aplica a los miembros de la nomina, a los dos lados de cada
veredicto y a los dos lados de cada lectura dirigida ANTES de contar nada.

Y ADEMAS BUSCA LOS PUENTES DE `P.10`, que es lo unico que la cobertura completa
permite mirar: un nodo con `A` hacia dos nodos que entre si dan `D`. `P.10` dice
que solo se ve mirando la componente entera, y una nomina con cobertura completa
es exactamente eso.

USO:
  python scripts/loop/vuelta169_tarea5_cobertura_op_l_02.py
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
PLAN = os.path.join(RAIZ, "docs", "plan")

PAT_LD = re.compile(
    r"^#{1,4}\s+`(LD-\d+)`\s*\.\s*`([a-z0-9_]+)`\s+contra\s+`([a-z0-9_]+)`\s*\.\s*\*\*([A-Z ]+)\*\*",
    re.M)

# LA SEGUNDA FORMA DE ESCRIBIR UNA LECTURA DIRIGIDA, Y SE ANADE PORQUE LA PRIMERA
# CORRIDA DE ESTE INSTRUMENTO LA PERDIO. La primera tanda y las de LD_*.md llevan
# cabecera con numero `LD-nn`; la SEGUNDA TANDA de `LECTURAS_DIRIGIDAS.md` (los
# cuadrantes, la ecuacion de valor y el bloque humano de la IA) las escribe como
# FILAS DE TABLA, sin numero, con la forma `| `a` contra `b` | **CLASE** |`.
# Contar solo las de cabecera daba 7 de 10 donde la ficha de OP-L-02 declara
# 10 de 10, y publicar esa cifra habria sido publicar el hueco del lector como si
# fuera un hueco del archivo. Se cuentan APARTE de las de cabecera para que se
# vea de cual de las dos formas sale cada par.
PAT_LD_TABLA = re.compile(
    r"^\|\s*\**`([a-z0-9_]+)`\**\s+contra\s+\**`([a-z0-9_]+)`\**\s*\|\s*\**([A-Z][A-Z ]*?)\**\s*\|\s*$",
    re.M)


def leer_nominas():
    """LA NOMINA SE PARSEA DEL FICHERO, NO SE TECLEA."""
    texto = io.open(MJS, encoding="utf-8").read()
    m = re.search(r"const NOMINAS_OP_L_02 = \[(.*?)\n\];", texto, re.S)
    if not m:
        raise SystemExit("ROJO: no se encuentra NOMINAS_OP_L_02 en %s" % MJS)
    filas = re.findall(r"\[([^\]]*)\]", m.group(1))
    return [re.findall(r'"([a-z0-9_]+)"', f) for f in filas]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 169, TAREA 5: COBERTURA DE LAS SEIS NOMINAS DE OP-L-02")
    print("=" * 78)
    print("")

    print("A) LAS SEDES, Y SUS TAMANOS LEIDOS HOY")
    G = json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    ALIAS = {a: k for k, v in G.items() for a in (v.get("ids_alias") or [])}

    def res(x, visto=None):
        visto = visto or set()
        while x in ALIAS and x not in visto:
            visto.add(x)
            x = ALIAS[x]
        return x

    V = [json.loads(l) for l in io.open(VEREDICTOS, encoding="utf-8") if l.strip()]
    nominas = leer_nominas()
    print("   grafo: %d nodos, %d entradas de alias" % (len(G), len(ALIAS)))
    print("   veredictos de cola: %d filas, corte %d"
          % (len(V), max(r["puesto_intra"] for r in V)))
    print("   nominas parseadas de NOMINAS_OP_L_02: %d" % len(nominas))
    print("")

    print("B) LAS LECTURAS DIRIGIDAS, DE SU PROPIA SEDE Y CONTADAS APARTE")
    dirigidas = {}
    de_tabla = []
    for nombre in sorted(os.listdir(PLAN)):
        if not nombre.endswith(".md"):
            continue
        texto = io.open(os.path.join(PLAN, nombre), encoding="utf-8").read()
        hallados = PAT_LD.findall(texto)
        filas = PAT_LD_TABLA.findall(texto)
        if hallados or filas:
            print("   %-34s %d cabeceras LD | %d filas de tabla"
                  % (nombre, len(hallados), len(filas)))
        for ld, a, b, clase in hallados:
            dirigidas[ld] = (a, b, clase.strip(), nombre)
        for a, b, clase in filas:
            de_tabla.append((a, b, clase.strip(), nombre))
    print("   CIFRA lecturas dirigidas CON NUMERO (cabecera): %d" % len(dirigidas))
    print("   CIFRA lecturas dirigidas SIN NUMERO (fila de tabla): %d" % len(de_tabla))
    print("")

    # indices resueltos
    cola = {}
    for r in V:
        cola[tuple(sorted((res(r["nodo_a"]), res(r["nodo_b"]))))] = (r["clase"], r["puesto_intra"])
    dir_idx = {}
    for ld, (a, b, clase, sede) in dirigidas.items():
        dir_idx[tuple(sorted((res(a), res(b))))] = (clase, ld, sede)
    for a, b, clase, sede in de_tabla:
        dir_idx.setdefault(tuple(sorted((res(a), res(b)))), (clase, "(sin numero)", sede))

    print("C) NOMINA POR NOMINA, CON EL RESOLUTOR DELANTE (P.1)")
    print("")
    total_sin = 0
    resumen = []
    for i, mem in enumerate(nominas, 1):
        vivos = sorted({res(m) for m in mem})
        colapsados = len(mem) - len(vivos)
        pares = [tuple(sorted(p)) for p in itertools.combinations(vivos, 2)]
        en_cola = [p for p in pares if p in cola]
        en_dir = [p for p in pares if p not in cola and p in dir_idx]
        sin = [p for p in pares if p not in cola and p not in dir_idx]
        total_sin += len(sin)
        clases = {}
        for p in en_cola:
            clases[cola[p][0]] = clases.get(cola[p][0], 0) + 1
        for p in en_dir:
            clases[dir_idx[p][0]] = clases.get(dir_idx[p][0], 0) + 1
        print("   NOMINA %d: %s%s" % (i, mem[0], " ..." if len(mem) > 1 else ""))
        print("      miembros escritos: %d | vivos tras resolver: %d | colapsados por alias: %d"
              % (len(mem), len(vivos), colapsados))
        print("      CIFRA pares posibles: %d" % len(pares))
        print("      CIFRA con veredicto DE COLA: %d" % len(en_cola))
        print("      CIFRA con LECTURA DIRIGIDA: %d" % len(en_dir))
        print("      CIFRA SIN veredicto de ninguna sede: %d" % len(sin))
        print("      cobertura total: %d de %d" % (len(en_cola) + len(en_dir), len(pares)))
        print("      reparto de clases: %s"
              % ", ".join("%s %d" % (k, v) for k, v in sorted(clases.items())))
        for p in sin:
            print("      SIN VEREDICTO: %s contra %s" % p)
        resumen.append((i, mem[0], len(pares), len(en_cola), len(en_dir), len(sin), clases))

        # P.10: puentes sobre la componente entera
        clase_de = {}
        for p in en_cola:
            clase_de[p] = cola[p][0]
        for p in en_dir:
            clase_de[p] = dir_idx[p][0]
        puentes = []
        for nodo in vivos:
            aes = [o for o in vivos if o != nodo
                   and clase_de.get(tuple(sorted((nodo, o))), "").startswith("A")]
            for x, y in itertools.combinations(sorted(aes), 2):
                if clase_de.get(tuple(sorted((x, y)))) == "D":
                    puentes.append((nodo, x, y))
        if puentes:
            print("      P.10 PUENTES (A con dos que entre si dan D): %d" % len(puentes))
            for n, x, y in puentes:
                print("         puente %s sobre (%s , %s)" % (n, x, y))
        else:
            print("      P.10 PUENTES: 0")
        print("")

    print("D) EL RESUMEN, TALLADO DE LO DE ARRIBA Y NO TECLEADO")
    print("")
    print("| # | nomina | posibles | cola | dirigidas | SIN | cobertura |")
    print("|---:|---|---:|---:|---:|---:|---|")
    for i, cab, pos, ncola, ndir, nsin, _cl in resumen:
        print("| %d | `%s` | %d | %d | %d | %d | %d de %d |"
              % (i, cab, pos, ncola, ndir, nsin, ncola + ndir, pos))
    print("")
    print("   CIFRA pares posibles en las seis: %d" % sum(r[2] for r in resumen))
    print("   CIFRA pares SIN veredicto en las seis: %d" % total_sin)
    print("   CIFRA nominas con cobertura COMPLETA: %d de %d"
          % (sum(1 for r in resumen if r[5] == 0), len(resumen)))
    print("")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
