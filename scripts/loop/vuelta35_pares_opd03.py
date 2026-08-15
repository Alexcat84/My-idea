# -*- coding: utf-8 -*-
"""vuelta35_pares_opd03.py - LA PREGUNTA DE P.5 SOBRE OP-D-03, medida y no recordada.

SOLO LECTURA. No escribe nada fuera de su salida.

QUE MIDE, Y POR QUE ES ESTA LA MEDICION Y NO OTRA.

P.5 (docs/plan/BANCO_DEL_PLAN.md linea 239) manda, con estas palabras:

    CADA ACTO SE LEE ENTERO DESPUES DE SU DESTEJIDO Y ANTES DE SU FUSION.

y escribe su motivo en la misma pagina: "leer un par cuyo nodo va a perder la
mitad de sus pasos es leer algo que va a dejar de existir".

El paso 2 del ORDEN INTERNO de OP-D-03 (02_DESTEJIDOS.md linea 980) es "solo
entonces decidir sobre los SEIS nodos", o sea la fusion. Antes de tocarla hay que
contestar, PAR POR PAR y con la fecha al lado: cual de los quince pares internos
del acto se leyo DESPUES del destejido de los nodos que toca, y cual se leyo
contra un texto que ya no existe.

EL REPORTE DE LA VUELTA 34 NOMBRA DOS (el 452 y el 1575). Este instrumento NO
parte de esa cifra: reconstruye la lista desde el archivo y desde git, y al final
la contrasta con la del reporte. Si discrepan, la discrepancia se declara
(EJECUTOR.md regla 2).

COMO SE FECHA UN DESTEJIDO SIN CREERLE A NADIE: por git log sobre el fichero del
nodo en dataset/nodos, que es donde vive su texto. Como se fecha una lectura: por
git log -S sobre la razon del par en el archivo de veredictos, que es la primera
vez que ese texto entro. Las dos fechas son del repositorio, no de un acta.

Uso: python scripts/loop/vuelta35_pares_opd03.py
"""
import io
import itertools
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
NODOS = os.path.join(RAIZ, "dataset", "nodos")

# La nomina NO se teclea de memoria: se lee de la linea del plan, y el
# instrumento aborta si la linea no esta. Es la misma guarda que
# vuelta34_costuras_opd03.py monto sobre las costuras.
PLAN = os.path.join(RAIZ, "docs", "plan", "02_DESTEJIDOS.md")
LINEA_NOMINA = (
    "**Acto 2. SEIS nodos y TRES destejidos.** Costuras: `ab_testing_optimizacion`,\n"
    "`optimizacion_embudo_get_customers`, `split_testing_experimentos_ab`. Sanos:\n"
    "`funnel_get_customers_optimizacion`, `split_testing`, `test_ab_precio`."
)
SEIS = [
    "ab_testing_optimizacion",
    "optimizacion_embudo_get_customers",
    "split_testing_experimentos_ab",
    "funnel_get_customers_optimizacion",
    "split_testing",
    "test_ab_precio",
]


def git(*args):
    out = subprocess.run(["git"] + list(args), cwd=RAIZ, capture_output=True)
    return out.stdout.decode("utf-8", "replace").strip()


def fecha_ultimo_cambio(ruta_rel):
    return git("log", "-1", "--date=short", "--pretty=format:%ad %h", "--", ruta_rel)


def main():
    texto_plan = io.open(PLAN, encoding="utf-8").read()
    if LINEA_NOMINA not in texto_plan:
        print("ABORTA: la nomina de los seis no esta citable en 02_DESTEJIDOS.md")
        return 1
    print("GUARDA DE NOMINA: la linea del plan esta, literal. Los seis se leen de ahi.\n")

    V = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
    por_puesto = {v["puesto_intra"]: v for v in V}
    # el indice por pareja de ids, en los dos ordenes
    # los campos son nodo_a y nodo_b, MEDIDOS con vuelta35_claves.py y no supuestos:
    # la primera version de este instrumento busco id_a e id_b y encontro cero de
    # quince. El fallo queda escrito arriba en vez de borrarse.
    por_par = {}
    for v in V:
        a, b = v.get("nodo_a"), v.get("nodo_b")
        if a and b:
            por_par[(a, b)] = v
            por_par[(b, a)] = v

    print("--- LOS SEIS NODOS HOY, con sus pasos y la fecha de su ultimo cambio ---")
    pasos = {}
    for nid in SEIS:
        rel = "dataset/nodos/%s.json" % nid
        d = json.load(io.open(os.path.join(NODOS, nid + ".json"), encoding="utf-8"))
        pasos[nid] = len(d.get("pasos_accionables") or [])
        print("  %-38s %2d pasos   ultimo cambio: %s"
              % (nid, pasos[nid], fecha_ultimo_cambio(rel)))

    print("\n--- LOS QUINCE PARES INTERNOS, uno por uno ---")
    print("%-5s %-5s %-36s %-36s %s" % ("puesto", "clase", "id_a", "id_b", "leido / cambio"))
    filas = []
    faltan = []
    for a, b in itertools.combinations(SEIS, 2):
        v = por_par.get((a, b))
        if v is None:
            faltan.append((a, b))
            continue
        puesto = v["puesto_intra"]
        rel_a = "dataset/nodos/%s.json" % v["nodo_a"]
        rel_b = "dataset/nodos/%s.json" % v["nodo_b"]
        # cuando entro ESTA razon al archivo (primera aparicion del texto)
        fragmento = (v["razon"] or "")[:120]
        leido = git("log", "-1", "--date=short", "--pretty=format:%ad %h",
                    "-S", fragmento, "--", "docs/INTRA_DOMINIO_VEREDICTOS.jsonl")
        cambio_a = fecha_ultimo_cambio(rel_a)
        cambio_b = fecha_ultimo_cambio(rel_b)
        filas.append({
            "puesto": puesto, "clase": v["clase"], "a": v["nodo_a"], "b": v["nodo_b"],
            "leido": leido, "cambio_a": cambio_a, "cambio_b": cambio_b,
        })
        print("%-6d %-5s %-36s %-36s leido %s" % (puesto, v["clase"], v["nodo_a"], v["nodo_b"], leido))
        print("%-49s %s cambio %s" % ("", "a:", cambio_a))
        print("%-49s %s cambio %s" % ("", "b:", cambio_b))

    print("\npares encontrados: %d de 15" % len(filas))
    if faltan:
        print("PARES SIN REGISTRO EN EL ARCHIVO (%d):" % len(faltan))
        for a, b in faltan:
            print("   %s contra %s" % (a, b))

    # EL VEREDICTO DE P.5: un par esta RANCIO si su lectura es anterior al ultimo
    # cambio de texto de cualquiera de sus dos nodos.
    print("\n--- EL VEREDICTO DE P.5, par por par ---")
    rancios = []
    for f in filas:
        fl = f["leido"].split(" ")[0] if f["leido"] else ""
        fa = f["cambio_a"].split(" ")[0] if f["cambio_a"] else ""
        fb = f["cambio_b"].split(" ")[0] if f["cambio_b"] else ""
        posterior = [n for n, fx in ((f["a"], fa), (f["b"], fb)) if fl and fx and fx > fl]
        if posterior:
            rancios.append(f)
            print("  RANCIO   %-5d %-3s leido %s, y cambiaron DESPUES: %s"
                  % (f["puesto"], f["clase"], fl, ", ".join(posterior)))
        else:
            print("  al dia   %-5d %-3s leido %s" % (f["puesto"], f["clase"], fl))

    print("\nRANCIOS: %d de %d. Puestos: %s"
          % (len(rancios), len(filas), sorted(f["puesto"] for f in rancios)))
    print("de ellos con clase A: %s"
          % sorted(f["puesto"] for f in rancios if f["clase"] == "A"))

    print("\n--- CONTRASTE CONTRA EL REPORTE DE LA VUELTA 34 (no es fuente, es contraste) ---")
    print("el reporte nombro DOS: 452 y 1575.")
    medidos = set(f["puesto"] for f in rancios)
    print("medidos hoy: %s" % sorted(medidos))
    if medidos == {452, 1575}:
        print("COINCIDE.")
    else:
        print("DISCREPA. La discrepancia se declara, no se resuelve copiando (regla 2).")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())

