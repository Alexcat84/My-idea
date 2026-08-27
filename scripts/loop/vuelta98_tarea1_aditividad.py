# -*- coding: utf-8 -*-
r"""vuelta98_tarea1_aditividad.py . VUELTA 98, TAREA 1: PRUEBA CAMPO A CAMPO QUE
LA CORRECCION DECLARADA DE LAS FECHAS ES PURAMENTE ADITIVA.

POR QUE NACE. El encargo de la vuelta 98 corrige SEIS addenda (el instrumento
encuentra seis, el auditor habia encontrado dos), y cuatro de ellos no estan
nombrados en el encargo: entran por el BORDE DE LA ADJUDICACION 3.7 del acta 97,
que exige (a) que la cifra nueva salga de un instrumento corrido en la vuelta,
(b) que la escritura sea PURAMENTE ADITIVA y no borre el texto viejo, y (c) que
no mueva ninguna decision, ningun alcance y ningun estado. Este instrumento mide
(b) y (c). El (a) lo cubre vuelta98_tarea1_fechas_addenda.py, que lee la fecha
de `git log`.

POR QUE NO BASTA `git diff --numstat`. En un JSONL de un registro por linea,
cambiar una nota reescribe su linea entera: numstat dice "4 anadidas, 4
borradas" aunque no se haya borrado una sola letra de texto. La prueba de
verdad es la RECONSTRUCCION: se borran del texto NUEVO todas las inserciones de
correccion y se comprueba que lo que queda es IGUAL CARACTER A CARACTER al
texto VIEJO. Si sobra o falta un caracter, ROJO.

QUE MIDE, y todo se lee de git, nada se teclea:
  1. el numero de lineas del JSONL antes y despues
  2. el conjunto de id_op antes y despues, y su orden
  3. QUE CAMPOS cambiaron, campo a campo, en todos los registros
  4. la RECONSTRUCCION de cada nota cambiada
  5. que ningun campo de decision se movio: estado, fecha_corte, verificacion,
     evidencia, adjudicacion, nodos, aristas_nuevas, orden

USO:
  python scripts/loop/vuelta98_tarea1_aditividad.py
  python scripts/loop/vuelta98_tarea1_aditividad.py --contra <ref>

SALIDA: exit 0 si la escritura es aditiva y no movio decision; exit 1 si no.
"""
import argparse
import io
import json
import os
import re
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA = "docs/plan/OPERACIONES.jsonl"

RE_INSERCION = re.compile(
    r" \[CORRECCION DECLARADA DE FECHA \(vuelta 98, TAREA 1\)[^\]]*\]")

CAMPOS_DE_DECISION = ("estado", "fecha_corte", "verificacion", "evidencia",
                      "adjudicacion", "nodos", "aristas_nuevas", "orden",
                      "superviviente", "preservar", "eliminar", "depende_de",
                      "bloquea_a", "fase", "tipo", "pregunta_pendiente")


def cargar_ref(ref):
    r = subprocess.run(["git", "show", "%s:%s" % (ref, RUTA)],
                       cwd=RAIZ, capture_output=True)
    if r.returncode != 0:
        raise SystemExit("ROJO: no se pudo leer %s:%s" % (ref, RUTA))
    txt = r.stdout.decode("utf-8")
    return [json.loads(l) for l in txt.splitlines() if l.strip()]


def cargar_work():
    with io.open(os.path.join(RAIZ, RUTA), encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--contra", default="HEAD")
    a = ap.parse_args()

    viejos = cargar_ref(a.contra)
    nuevos = cargar_work()
    fallos = []

    print("=" * 100)
    print("ADITIVIDAD DE LA CORRECCION DE FECHAS, PROBADA CAMPO A CAMPO")
    print("=" * 100)
    print("VIEJO: %s:%s   NUEVO: arbol de trabajo" % (a.contra, RUTA))
    print("LINEAS: antes %d, despues %d" % (len(viejos), len(nuevos)))
    if len(viejos) != len(nuevos):
        fallos.append("el numero de lineas cambio")

    ids_v = [o.get("id_op") for o in viejos]
    ids_n = [o.get("id_op") for o in nuevos]
    print("ID_OP en el mismo orden y sin altas ni bajas: %s"
          % ("SI" if ids_v == ids_n else "NO"))
    if ids_v != ids_n:
        fallos.append("la lista de id_op cambio")

    if len(viejos) != len(nuevos) or ids_v != ids_n:
        print("ROJO: no se puede seguir comparando registro a registro.")
        return 1

    cambios = {}
    for v, n in zip(viejos, nuevos):
        for k in sorted(set(list(v.keys()) + list(n.keys()))):
            if v.get(k) != n.get(k):
                cambios.setdefault(k, []).append(v.get("id_op"))

    print()
    print("CAMPOS QUE CAMBIARON, contados de los propios registros:")
    if not cambios:
        print("   (ninguno)")
    for k in sorted(cambios):
        print("   %-12s en %d registro(s): %s" % (k, len(cambios[k]), ", ".join(cambios[k])))

    for k in CAMPOS_DE_DECISION:
        if k in cambios:
            fallos.append("cambio el campo de decision %r en %s"
                          % (k, ", ".join(cambios[k])))
    otros = [k for k in cambios if k != "nota"]
    if otros:
        fallos.append("cambiaron campos ademas de nota: %s" % ", ".join(sorted(otros)))

    print()
    print("| operacion | nota antes | nota despues | inserciones | reconstruccion == viejo |")
    print("|---|---:|---:|---:|---|")
    tocadas = 0
    for v, n in zip(viejos, nuevos):
        if v.get("nota") == n.get("nota"):
            continue
        tocadas += 1
        va, vb = v.get("nota") or "", n.get("nota") or ""
        ins = len(RE_INSERCION.findall(vb))
        rec = RE_INSERCION.sub("", vb)
        ok = (rec == va)
        print("| %s | %d | %d | %d | %s |"
              % (v.get("id_op"), len(va), len(vb), ins, "SI" if ok else "NO"))
        if not ok:
            fallos.append("la nota de %s NO se reconstruye: se borro o se cambio "
                          "texto viejo" % v.get("id_op"))
        if ins == 0:
            fallos.append("la nota de %s cambio sin ninguna insercion de correccion"
                          % v.get("id_op"))
    print()
    print("NOTAS TOCADAS: %d" % tocadas)

    print()
    if fallos:
        print("ROJO, %d cosa(s) no cuadran:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1
    print("VERDE: la escritura es PURAMENTE ADITIVA (el texto viejo se reconstruye "
          "caracter a caracter en las %d notas tocadas) y NO movio ningun campo de "
          "decision (%s)." % (tocadas, ", ".join(CAMPOS_DE_DECISION)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
