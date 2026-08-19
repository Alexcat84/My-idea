# -*- coding: utf-8 -*-
"""vuelta40_registros_no_grafo.py - DONDE VIVEN LOS TRES NODOS DE OP-D-05 FUERA
DEL GRAFO, buscado ANTES de fundir y no despues.

ESTRICTAMENTE DE SOLO LECTURA.

POR QUE EXISTE, y es la leccion de la vuelta 39 escrita en instrumento. Aquella
vuelta sello un plan de fusion con sus 17 referencias de NODO enumeradas, ejecuto,
y EL GATE 0 CAYO EN ROJO: un puente aprobado de `packs/quality` seguia apuntando
al recien deprecado, porque un puente NO VIVE EN EL GRAFO y ni el plan ni la
simulacion de `P.7` lo miran. El acta de la vuelta 39 adjudico el remedio (correr
`reanclar_por_resolutor.py` entre la fusion y `run_phase1`, practica para toda
fusion futura) y recomendo al fundador que los planes enumeren tambien estos
registros. ESO ES LO QUE ESTE INSTRUMENTO MIDE, para que la sorpresa no se repita.

QUE BARRE: todo el repo salvo el propio grafo, los nodos, la carpeta de la
campana (docs/loop, que es prosa de vueltas) y lo que no es texto. Lo que
encuentre se enumera con su fichero y su linea, y se clasifica en REGISTRO (un
json de datos que el motor lee) o MENCION (prosa).

Uso:
  python scripts/loop/vuelta40_registros_no_grafo.py \\
      --id seleccion_ceo_fundador --id asignacion_de_titulos_ejecutivos \\
      --id errores_comunes_asignacion_roles
"""
import argparse
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Lo que NO se barre, y por que.
SALTAR_DIR = {
    ".git": "no es contenido",
    "node_modules": "dependencias",
    "__pycache__": "binario",
    ".next": "compilado",
    "dataset/nodos": "ES el grafo, y esa parte la cubren la simulacion y el ejecutor",
    "docs/loop": "prosa de las vueltas del bucle, no un registro que el motor lea",
}
EXT_TEXTO = (".json", ".jsonl", ".md", ".ts", ".tsx", ".js", ".py", ".txt",
             ".yml", ".yaml", ".sql", ".csv")
# Los ficheros que el motor o la web LEEN como datos: si uno de estos nombra a un
# nodo que se va a deprecar, la fusion tiene que tocarlo o Gate 0 caera.
REGISTROS = (".json", ".jsonl", ".sql", ".csv")

# ===========================================================================
# LA CLASIFICACION, y es lo que convierte una lista larga en una decision.
# ===========================================================================
# El barrido crudo caza 251 apariciones y ninguna decision sale de ahi: hay que
# separar QUE HAY QUE TOCAR de QUE NO SE TOCA JAMAS. Tres clases, con su regla:
#
#   REGENERADO  lo reescribe el ciclo (run_phase1, etiquetas_de_cara,
#               sync_assets_web) o el propio instrumento que lo produce. NO se
#               toca a mano: se corre el ciclo y se mira el diff.
#   ARCHIVO     registro historico de una medicion CON SU CORTE. NO se reescribe
#               nunca, porque reescribirlo seria falsificar la medicion. Un
#               veredicto de agosto nombra al nodo que existia en agosto.
#   VIVO        registro que el motor lee y que mantiene una mano, no un script.
#               ES EL UNICO QUE UNA FUSION TIENE QUE REDIRIGIR, y es la clase a
#               la que pertenece bridges_aprobados.json, que fue la sorpresa de
#               la vuelta 39.
CLASES = (
    ("REGENERADO", (
        "dataset/metadata/master_graph.json",
        "dataset/metadata/phase1",
        "web/lib/assets/",
        "engine/node_families.json",
        "engine/preguntas_cache.json",
        "docs/COSTURAS_INTERNAS",
    )),
    ("ARCHIVO", (
        "docs/INTRA_DOMINIO_", "docs/FRANJA_", "docs/plan/",
        "dataset/metadata/ghost_", "dataset/metadata/expansion_v13/",
        "dataset/metadata/merged_originals_v11/",
        "dataset/metadata/enriquecimientos_v13.json",
        "books/", "packs/_core/poda/", "scripts/_actos_",
    )),
)


def clase_de(rel):
    for nombre, prefijos in CLASES:
        for p in prefijos:
            if rel.startswith(p):
                return nombre
    return "VIVO"


def salta(rel):
    r = rel.replace("\\", "/")
    for d in SALTAR_DIR:
        if r == d or r.startswith(d + "/"):
            return True
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--id", action="append", required=True)
    args = ap.parse_args()
    ids = args.id

    print("LOS TRES NODOS BUSCADOS FUERA DEL GRAFO, 19 ago 2026 (vuelta 40)")
    for i in ids:
        print("  - %s" % i)
    print("")
    print("CARPETAS SALTADAS, con su motivo:")
    for d, m in sorted(SALTAR_DIR.items()):
        print("  %-18s %s" % (d, m))
    print("")

    hallazgos = {i: [] for i in ids}
    ficheros = 0
    for base, dirs, nombres in os.walk(RAIZ):
        rel_base = os.path.relpath(base, RAIZ)
        dirs[:] = [d for d in dirs
                   if not salta(os.path.join(rel_base, d) if rel_base != "." else d)]
        for nombre in nombres:
            if not nombre.endswith(EXT_TEXTO):
                continue
            rel = os.path.relpath(os.path.join(base, nombre), RAIZ)
            if salta(rel):
                continue
            ficheros += 1
            try:
                texto = io.open(os.path.join(base, nombre), encoding="utf-8").read()
            except (UnicodeDecodeError, OSError):
                continue
            for i in ids:
                if i in texto:
                    for n, linea in enumerate(texto.splitlines(), 1):
                        if i in linea:
                            hallazgos[i].append((rel.replace("\\", "/"), n,
                                                 linea.strip()[:150]))

    print("ficheros de texto barridos: %d" % ficheros)
    print("")
    vivos, cuenta = {}, {"REGENERADO": 0, "ARCHIVO": 0, "VIVO": 0, "mencion": 0}
    for i in ids:
        print("=" * 78)
        print("%s: %d apariciones" % (i, len(hallazgos[i])))
        print("=" * 78)
        if not hallazgos[i]:
            print("  NINGUNA fuera del grafo.")
        for rel, n, linea in hallazgos[i]:
            if not rel.endswith(REGISTROS):
                cuenta["mencion"] += 1
                continue
            c = clase_de(rel)
            cuenta[c] += 1
            if c == "VIVO":
                vivos.setdefault(rel, []).append((i, n, linea))
        por_fichero = {}
        for rel, n, linea in hallazgos[i]:
            por_fichero.setdefault(rel, 0)
            por_fichero[rel] += 1
        for rel in sorted(por_fichero):
            c = clase_de(rel) if rel.endswith(REGISTROS) else "mencion"
            print("  [%-10s] %-62s %d linea(s)" % (c, rel, por_fichero[rel]))
        print("")

    print("=" * 78)
    print("EL REPARTO POR CLASE, que es lo que decide")
    print("=" * 78)
    for c in ("REGENERADO", "ARCHIVO", "VIVO", "mencion"):
        print("  %-11s %d apariciones" % (c, cuenta[c]))
    print("")
    print("  REGENERADO: lo reescribe el ciclo. No se toca a mano.")
    print("  ARCHIVO   : medicion con su corte. NO se reescribe: seria falsificarla.")
    print("  VIVO      : el motor lo lee y lo mantiene una mano. ES EL QUE HAY QUE")
    print("              REDIRIGIR, y es la clase de bridges_aprobados.json.")
    print("")
    print("=" * 78)
    print("LOS REGISTROS VIVOS QUE NOMBRAN A ALGUNO DE LOS TRES: %d" % len(vivos))
    print("=" * 78)
    if not vivos:
        print("  NINGUNO.")
    for rel in sorted(vivos):
        print("  %s" % rel)
        for i, n, linea in vivos[rel]:
            print("      %s:%d  %s" % (i, n, linea))
    print("")
    print("LA COMPROBACION DIRIGIDA sobre la clase que fallo en la vuelta 39:")
    import glob
    for f in sorted(glob.glob(os.path.join(RAIZ, "packs", "*", "metadata",
                                           "bridges_aprobados.json"))):
        rel = os.path.relpath(f, RAIZ).replace("\\", "/")
        t = io.open(f, encoding="utf-8").read()
        n = sum(t.count(i) for i in ids)
        print("  %-52s nombra a los tres: %d veces" % (rel, n))
    print("")
    print("Si los VIVOS son CERO, la fusion no tiene ningun registro fuera del")
    print("grafo que redirigir, y el re-anclaje posterior tiene que salir en")
    print("blanco. Eso NO exime de correrlo: el acta de la vuelta 39 lo adjudico")
    print("como practica para TODA fusion futura, y una guarda que solo se corre")
    print("cuando se sospecha no es una guarda.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
