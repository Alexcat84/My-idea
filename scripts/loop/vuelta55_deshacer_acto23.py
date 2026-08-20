# -*- coding: utf-8 -*-
"""vuelta55_deshacer_acto23.py . LA MITAD PRIMERA DE LA CORRECCION DECLARADA DEL
ACTO 23 DEL TRAMO 2: DESHACER LA FUSION EJECUTADA EN LA VUELTA 54.

POR QUE EXISTE. La vuelta 54 fundio el acto 23 con
modelo_cascada_desarrollo_producto de superviviente, decidido POR EL CABLEADO
SOLO con el contenido dado por empatado. El acta de la vuelta 54 (seccion 3) y
la relectura conjunta de esta vuelta leen la razon del puesto 340 y encuentran
que declara UN SOLO gesto propio, y del OTRO lado: "El segundo anade no
contratar estructuras completas, VP de ventas y equipos, antes de validar, QUE
ES EL UNICO GESTO PROPIO". Material propio declarado de UN SOLO LADO es una
vara de contenido NO empatada (acta 54, pregunta 4), y una vara de contenido no
empatada BASTA: el contenido no empataba y el cableado no tenia que hablar.

LO QUE ESTE INSTRUMENTO HACE, Y LO QUE NO HACE. Deshace, y solo deshace. La
fusion en la direccion correcta la ejecuta despues el instrumento de siempre
(scripts/loop/vuelta49_fundir_tramo.py) con su plan sellado y sus guardas
enteras, para que la correccion no invente ninguna via nueva.

EL ALCANCE ESTA MEDIDO, NO SUPUESTO. El acto 23 se ejecuto dentro del lote B
(commit ca191ee6), junto con otros nueve actos. Los ficheros que ese commit
toco son 50, y los que el acto 23 toco son CUATRO, medidos asi:

    git diff --name-only 0feef54e ca191ee6 -- dataset/nodos/
    y de esos, los que mencionan en su diff alguno de los dos ids del acto 23

Los cuatro son el superviviente, el absorbido y los dos nodos vivos cuya arista
la fusion redirigio (customer_development_modelo y stage_gate_system). Ninguno
de los cuatro se ha vuelto a tocar despues de ca191ee6, comprobado por git, y
el diff entero de cada uno entre 0feef54e y ca191ee6 es atribuible al acto 23.
Por eso el deshacer es exacto: se restaura el BLOB de 0feef54e, que es el
estado con el lote A ya ejecutado y el lote B todavia no.

  OJO CON stage_gate_system: es el SUPERVIVIENTE del acto 8, que se ejecuto en
  el lote A. Restaurarlo al blob de 0feef54e conserva el acto 8 entero, porque
  0feef54e ES el commit del lote A. Restaurarlo a un commit anterior habria
  borrado el acto 8, y por eso el commit de referencia no se elige: se mide.

EL INSTRUMENTO COMPRUEBA ANTES DE ESCRIBIR, y si algo no calza no escribe nada:
  - que los cuatro ficheros no se hayan tocado despues de ca191ee6;
  - que el diff de cada uno entre los dos commits mencione los ids del acto 23;
  - que tras restaurar, el absorbido quede VIVO y el superviviente tambien, y
    que ninguno de los dos lleve al otro en ids_alias.

MODOS: --simular (por defecto, cero escrituras) y --ejecutar.

Uso: python scripts/loop/vuelta55_deshacer_acto23.py [--ejecutar]
"""
import argparse
import io
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ANTES = "0feef54e"   # el commit del lote A: el acto 23 todavia no se ha tocado
LOTE_B = "ca191ee6"  # el commit del lote B: el acto 23 ya esta fundido

SUP_VIEJO = "modelo_cascada_desarrollo_producto"
ABS_VIEJO = "modelo_tradicional_introduccion_producto"
FICHEROS = ["dataset/nodos/customer_development_modelo.json",
            "dataset/nodos/modelo_cascada_desarrollo_producto.json",
            "dataset/nodos/modelo_tradicional_introduccion_producto.json",
            "dataset/nodos/stage_gate_system.json"]


def git(*args):
    p = subprocess.run(["git"] + list(args), capture_output=True, cwd=RAIZ)
    return p.returncode, p.stdout.decode("utf-8", "replace"), p.stderr.decode("utf-8", "replace")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ejecutar", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    modo = "EJECUTAR" if a.ejecutar else "SIMULAR"
    print("=" * 78)
    print("DESHACER EL ACTO 23 DEL TRAMO 2 . MODO %s" % modo)
    print("=" * 78)
    print()
    fallos = []

    # --- 1. el alcance, re-medido aqui y no copiado ---
    rc, out, _ = git("diff", "--name-only", ANTES, LOTE_B, "--", "dataset/nodos/")
    tocados = [x.strip() for x in out.splitlines() if x.strip()]
    print("  ficheros de nodos que el lote B (%s) toco: %d" % (LOTE_B, len(tocados)))
    del_acto = []
    # LA VARA DE ATRIBUCION, EN SUS DOS MITADES. La primera version de este
    # instrumento solo tenia la primera y CAYO EN ROJO ella sola, que es lo que
    # se le pide a una guarda: el fichero del ABSORBIDO no se nombra a si mismo
    # en su propio diff (su unico cambio es la linea "deprecado": true), asi que
    # buscar el id en las lineas del diff lo dejaba fuera. Se anade la mitad que
    # faltaba y se declara: un fichero es del acto 23 si su diff MENCIONA alguno
    # de los dos ids, o si el fichero ES el de uno de los dos miembros.
    propios = {"dataset/nodos/%s.json" % SUP_VIEJO, "dataset/nodos/%s.json" % ABS_VIEJO}
    for f in tocados:
        if f.replace("\\", "/") in propios:
            del_acto.append(f)
            continue
        rc, d, _ = git("diff", ANTES, LOTE_B, "--", f)
        marcado = [l for l in d.splitlines()
                   if l[:1] in "+-" and l[:3] not in ("+++", "---")
                   and (SUP_VIEJO in l or ABS_VIEJO in l)]
        if marcado:
            del_acto.append(f)
    print("  de esos, los que el ACTO 23 toco: %d" % len(del_acto))
    for f in del_acto:
        print("     %s" % f)
    if sorted(del_acto) != sorted(FICHEROS):
        fallos.append("el alcance medido no calza con el declarado: medido %s" % sorted(del_acto))
    print("  el alcance medido calza con el declarado: %s"
          % ("SI" if sorted(del_acto) == sorted(FICHEROS) else "NO"))
    print()

    # --- 2. ninguno tocado despues del lote B ---
    rc, out, _ = git("diff", "--name-only", LOTE_B, "HEAD", "--", *FICHEROS)
    despues = [x.strip() for x in out.splitlines() if x.strip()]
    print("  ficheros tocados DESPUES del lote B: %d %s" % (len(despues), despues))
    if despues:
        fallos.append("hay ficheros tocados despues del lote B: %s" % despues)
    print()

    # --- 3. el arbol de trabajo esta limpio en esos cuatro ---
    rc, out, _ = git("status", "--porcelain", "--", *FICHEROS)
    sucio = [x for x in out.splitlines() if x.strip()]
    print("  esos cuatro, sucios en el arbol de trabajo: %d %s" % (len(sucio), sucio))
    if sucio:
        fallos.append("hay ficheros sucios: %s" % sucio)
    print()

    if fallos:
        print("  ROJO, %d fallos y NO se escribe nada:" % len(fallos))
        for f in fallos:
            print("     %s" % f)
        return 1

    print("  ESTADO DE HOY, antes de deshacer:")
    for nid in (SUP_VIEJO, ABS_VIEJO):
        d = json.load(io.open(os.path.join(RAIZ, "dataset", "nodos", nid + ".json"),
                              encoding="utf-8"))
        print("     %-46s deprecado %-6s pasos %d cond %d ids_alias %s"
              % (nid, bool(d.get("deprecado")), len(d.get("pasos_accionables") or []),
                 len(d.get("condiciones_activacion") or []), d.get("ids_alias")))
    print()

    if not a.ejecutar:
        print("  MODO SIMULAR: no se escribe nada. Los cuatro ficheros se restaurarian")
        print("  al blob de %s con: git checkout %s -- <los cuatro>" % (ANTES, ANTES))
        print()
        print("FIN")
        return 0

    rc, out, err = git("checkout", ANTES, "--", *FICHEROS)
    if rc != 0:
        print("  ROJO: el checkout fallo: %s" % err)
        return 1
    print("  RESTAURADOS los cuatro ficheros al blob de %s" % ANTES)
    print()

    print("  ESTADO TRAS DESHACER:")
    ok = True
    for nid in (SUP_VIEJO, ABS_VIEJO):
        d = json.load(io.open(os.path.join(RAIZ, "dataset", "nodos", nid + ".json"),
                              encoding="utf-8"))
        vivo = not d.get("deprecado")
        alias = d.get("ids_alias") or []
        print("     %-46s vivo %-6s pasos %d cond %d ids_alias %s"
              % (nid, vivo, len(d.get("pasos_accionables") or []),
                 len(d.get("condiciones_activacion") or []), alias))
        if not vivo:
            ok = False
        if SUP_VIEJO in alias or ABS_VIEJO in alias:
            ok = False
    print("  LOS DOS VIVOS Y SIN ALIAS CRUZADO: %s" % ("SI" if ok else "NO"))
    print()
    print("FIN")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
