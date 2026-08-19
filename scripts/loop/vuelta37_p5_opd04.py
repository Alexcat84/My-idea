# -*- coding: utf-8 -*-
"""vuelta37_p5_opd04.py - LA PREGUNTA DE P.5 SOBRE OP-D-04, medida y no recordada.

SOLO LECTURA. No escribe nada fuera de su salida.

SUCESOR DECLARADO de scripts/loop/vuelta35_pares_opd03.py y de
scripts/loop/vuelta35_rancios.py, que la vuelta 35 corrio sobre el acto de
OP-D-03. LO QUE CAMBIA VA DICHO (EJECUTOR.md regla 2): aquellos eran dos
instrumentos con dos varas separadas (la fecha y el texto) sobre un acto de SEIS
nodos con la nomina cableada dentro; este los junta en uno, porque las dos varas
contestan la misma pregunta y separarlas obligo a la vuelta 35 a cruzar dos
salidas a mano. La nomina sigue leyendose del plan con la misma guarda.

QUE MIDE. P.5 (docs/plan/BANCO_DEL_PLAN.md linea 239) manda:

    CADA ACTO SE LEE ENTERO DESPUES DE SU DESTEJIDO Y ANTES DE SU FUSION.

y su alcance quedo adjudicado el 15 ago 2026 por decision del fundador, escrito
en la misma pagina: la relectura de pares rancios y la lectura del acto entero
valen SOLO DENTRO DEL ACTO EN OPERACION, y ningun par de fuera se relee por este
camino. Asi que este instrumento no sale de los SIETE.

TRES COSAS, y cada una con su vara:
  1. LOS 21 PARES INTERNOS posibles de los siete nodos: cuales tienen veredicto
     en el archivo y cuales no. Es la guarda literal del campo verificacion de
     OP-D-04: 'el acto se leyo ENTERO antes de fundirse: cero pares internos sin
     veredicto'.
  2. VARA DE FECHA: un par esta rancio si su lectura (primera aparicion de su
     razon en el archivo, por git log -S) es anterior al ultimo cambio del
     fichero de cualquiera de sus dos nodos.
  3. VARA DE TEXTO: de los que la vara de fecha marca, cuales cambiaron DE
     VERDAD sus pasos accionables entre el commit de la lectura y hoy. Un
     fichero se toca por cosas que no son su texto (un reciprocado, un enlace,
     un campo de fuente) y contar eso como rancio infla el hallazgo.

Solo lo que las DOS varas marcan se declara RANCIO.

Uso: python scripts/loop/vuelta37_p5_opd04.py
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
PLAN = os.path.join(RAIZ, "docs", "plan", "02_DESTEJIDOS.md")

# LA NOMINA NO SE TECLEA DE MEMORIA: se lee de la linea del plan, y el
# instrumento ABORTA si la linea no esta literal. Misma guarda que la 35.
LINEA_NOMINA = (
    "**Acto 1, el mayor: SIETE nodos.** `brainstorming_divergente` mas\n"
    "`brainstorming_efectivo`, `reglas_brainstorming`, `generar_multiples_opciones`,\n"
    "`construir_sobre_ideas_ajenas`, `pensamiento_convergente_divergente`,\n"
    "`design_attitude_vs_decision_attitude`."
)
SIETE = [
    "brainstorming_divergente",
    "brainstorming_efectivo",
    "reglas_brainstorming",
    "generar_multiples_opciones",
    "construir_sobre_ideas_ajenas",
    "pensamiento_convergente_divergente",
    "design_attitude_vs_decision_attitude",
]
# Los pares A que la seccion 54.3 del INTRA_DOMINIO_INFORME atribuye al acto 1.
# NO son fuente: se contrastan contra lo que el archivo diga hoy.
PARES_DEL_INFORME = [234, 586, 823, 834, 844, 885, 943]
GEMELOS = [823, 834, 844]


def git_bytes(*args):
    return subprocess.run(["git"] + list(args), cwd=RAIZ, capture_output=True).stdout


def git(*args):
    return git_bytes(*args).decode("utf-8", "replace").strip()


def fecha_ultimo_cambio(rel):
    return git("log", "-1", "--date=short", "--pretty=format:%ad %h", "--", rel)


def pasos_en(commit, nid):
    crudo = git_bytes("show", "%s:dataset/nodos/%s.json" % (commit, nid))
    if not crudo.strip():
        return None
    try:
        d = json.loads(crudo.decode("utf-8", "replace"))
    except ValueError:
        return None
    return d.get("pasos_accionables") or []


def pasos_hoy(nid):
    d = json.load(io.open(os.path.join(NODOS, nid + ".json"), encoding="utf-8"))
    return d.get("pasos_accionables") or []


def bloque(t):
    print("")
    print("=" * 78)
    print(t)
    print("=" * 78)


def main():
    texto_plan = io.open(PLAN, encoding="utf-8").read()
    if LINEA_NOMINA not in texto_plan:
        print("ABORTA: la nomina de los siete no esta citable en 02_DESTEJIDOS.md")
        return 1
    print("GUARDA DE NOMINA: la linea del plan esta, literal. Los siete se leen de ahi.")

    V = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
    por_par = {}
    for v in V:
        a, b = v.get("nodo_a"), v.get("nodo_b")
        if a and b:
            por_par[(a, b)] = v
            por_par[(b, a)] = v

    bloque("1. LOS SIETE NODOS HOY, con sus pasos y la fecha de su ultimo cambio")
    for nid in SIETE:
        rel = "dataset/nodos/%s.json" % nid
        print("  %-38s %2d pasos   ultimo cambio: %s"
              % (nid, len(pasos_hoy(nid)), fecha_ultimo_cambio(rel)))

    bloque("2. LOS 21 PARES INTERNOS POSIBLES: cuales tienen veredicto")
    filas = []
    sin_registro = []
    for a, b in itertools.combinations(SIETE, 2):
        v = por_par.get((a, b))
        if v is None:
            sin_registro.append((a, b))
            print("  SIN REGISTRO   %-38s contra %s" % (a, b))
            continue
        filas.append(v)
        print("  puesto %-5s %-3s  %-38s contra %s"
              % (v["puesto_intra"], v["clase"], v["nodo_a"], v["nodo_b"]))
    print("")
    print("  con veredicto: %d de 21    sin registro: %d de 21"
          % (len(filas), len(sin_registro)))

    bloque("3. CONTRASTE CONTRA LA SECCION 54.3 DEL INFORME (contraste, no fuente)")
    puestos_medidos = sorted(int(v["puesto_intra"]) for v in filas)
    clases = {}
    for v in filas:
        clases.setdefault(v["clase"], []).append(int(v["puesto_intra"]))
    print("  el informe atribuye al acto 1 estos pares A: %s" % PARES_DEL_INFORME)
    print("  medidos hoy en el archivo, todos los pares del acto: %s" % puestos_medidos)
    for c in sorted(clases):
        print("  clase %s: %s" % (c, sorted(clases[c])))
    a_hoy = sorted(clases.get("A", []))
    if a_hoy == sorted(PARES_DEL_INFORME):
        print("  COINCIDE: los siete pares A del informe son los siete A de hoy.")
    else:
        print("  DISCREPA. Se declara, no se resuelve copiando (EJECUTOR.md regla 2).")
        print("    solo en el informe: %s" % sorted(set(PARES_DEL_INFORME) - set(a_hoy)))
        print("    solo en el archivo: %s" % sorted(set(a_hoy) - set(PARES_DEL_INFORME)))

    bloque("4. VARA DE FECHA: que par se leyo antes de que su nodo cambiara")
    marcados_fecha = []
    detalle = {}
    for v in filas:
        puesto = int(v["puesto_intra"])
        fragmento = (v["razon"] or "")[:120]
        commit = git("log", "-1", "--pretty=format:%H", "-S", fragmento,
                     "--", "docs/INTRA_DOMINIO_VEREDICTOS.jsonl")
        fecha_leido = git("log", "-1", "--date=short", "--pretty=format:%ad", commit)
        posteriores = []
        for nid in (v["nodo_a"], v["nodo_b"]):
            cam = fecha_ultimo_cambio("dataset/nodos/%s.json" % nid)
            fcam = cam.split(" ")[0] if cam else ""
            if fecha_leido and fcam and fcam > fecha_leido:
                posteriores.append((nid, fcam))
        detalle[puesto] = {"commit": commit, "fecha": fecha_leido, "post": posteriores}
        if posteriores:
            marcados_fecha.append(puesto)
            print("  MARCADO  %-5d %-3s leido %s (%s), y cambiaron DESPUES: %s"
                  % (puesto, v["clase"], fecha_leido, commit[:8],
                     ", ".join("%s el %s" % p for p in posteriores)))
        else:
            print("  al dia   %-5d %-3s leido %s (%s)"
                  % (puesto, v["clase"], fecha_leido, commit[:8]))
    print("")
    print("  marcados por fecha: %d -> %s" % (len(marcados_fecha), sorted(marcados_fecha)))

    bloque("5. VARA DE TEXTO: de los marcados, cuales movieron sus pasos de verdad")
    rancios = []
    for v in filas:
        puesto = int(v["puesto_intra"])
        if puesto not in marcados_fecha:
            continue
        commit = detalle[puesto]["commit"]
        movidos = []
        print("  puesto %-5d %-3s  %s contra %s" % (puesto, v["clase"], v["nodo_a"], v["nodo_b"]))
        for nid in (v["nodo_a"], v["nodo_b"]):
            antes = pasos_en(commit, nid)
            ahora = pasos_hoy(nid)
            if antes is None:
                print("     %-38s NO SE PUDO LEER EN ESE COMMIT" % nid)
                continue
            igual = (antes == ahora)
            print("     %-38s pasos entonces %2d, hoy %2d  -> %s"
                  % (nid, len(antes), len(ahora), "IDENTICOS" if igual else "CAMBIARON"))
            if not igual:
                movidos.append((nid, len(antes), len(ahora)))
        if movidos:
            rancios.append((puesto, v["clase"], v["nodo_a"], v["nodo_b"], movidos))
            print("     VEREDICTO: RANCIO por las dos varas")
        else:
            print("     VEREDICTO: al dia (el fichero se toco, el texto no)")

    bloque("VEREDICTO DE P.5 SOBRE OP-D-04")
    print("pares internos posibles      : 21")
    print("con veredicto en el archivo  : %d" % len(filas))
    print("sin registro                 : %d" % len(sin_registro))
    print("marcados por la vara de fecha: %d -> %s" % (len(marcados_fecha), sorted(marcados_fecha)))
    print("RANCIOS por las DOS varas    : %d -> %s"
          % (len(rancios), sorted(r[0] for r in rancios)))
    print("")
    for puesto, clase, a, b, mov in sorted(rancios):
        print("  %-5d %-3s %s contra %s" % (puesto, clase, a, b))
        for nid, antes, ahora in mov:
            print("        %s de %d a %d pasos" % (nid, antes, ahora))
    print("")
    ra = sorted(r[0] for r in rancios if r[1] == "A")
    print("RANCIOS DE CLASE A: %s" % ra)
    print("Y SON LOS QUE SOSTIENEN LA FAMILIA: una A rancia es una arista de familia")
    print("dibujada sobre un texto que ya no existe.")
    print("")
    print("LOS TRES GEMELOS QUE LA NOTA DE OP-D-04 MANDA AL FINAL: %s" % GEMELOS)
    print("  de ellos rancios: %s" % sorted(p for p in ra if p in GEMELOS))
    print("  de ellos al dia : %s" % sorted(p for p in GEMELOS if p not in ra))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
