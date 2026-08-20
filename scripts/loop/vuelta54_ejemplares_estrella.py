# -*- coding: utf-8 -*-
"""vuelta54_ejemplares_estrella.py . LOS TRES EJEMPLARES DE LA PRECISION DE LA
ESTRELLA, MEDIDOS EN ESTA VUELTA.

POR QUE EXISTE: la TAREA 1.1 del encargo de la vuelta 54 manda adosar al 9.3.1
del banco una nota que publica, por cada uno de los tres actos, el CENTRO, sus
pares A con su clase y su formula Sobrevive, y el superviviente que lo absorbio.
La regla 2 del EJECUTOR dice que toda cifra o nombre propio que se publique se
lee de la salida del instrumento corrido EN ESTA VUELTA. El acta 53 y el reporte
53 ya los nombran; este instrumento los vuelve a medir para que la nota no
dependa de ellos.

QUE MIDE, de solo lectura:

  1. TODOS los pares del archivo que tocan a cada centro, con su clase de HOY
     y su clase AL ABRIR LA VUELTA 53 (commit d88c42bb, leido por git), y la
     formula "Sobrevive X" que cada razon cierra. La clase que importa para la
     figura de la estrella es la de ANTES de la vuelta 53, porque es con la
     que se leyo el acto; la de hoy va al lado como contraste.
  2. SI EL CENTRO PERDIO ALGUN PAR A, que es la prueba del GANADOR POR DERECHO
     del 9.3.1 corregido (contar SOLO los pares A).
  3. EL ESTADO DE HOY de centro y superviviente en dataset/nodos (deprecado o
     vivo), y el alias del centro izado al superviviente.

Uso: python scripts/loop/vuelta54_ejemplares_estrella.py
"""
import io
import json
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")
NODOS = os.path.join(RAIZ, "dataset", "nodos")

# El commit del cierre de la vuelta 52, que es el estado con el que la vuelta
# 53 leyo los tres actos.
ANTES = "d88c42bb"

# (nombre del acto, centro, superviviente que lo absorbe)
EJEMPLARES = [
    ("el pareto", "analisis_pareto", "analisis_pareto_de_proveedores"),
    ("el poka yoke", "mistake_proofing_poka_yoke_2", "error_proofing_servicio"),
    ("el dmaic select", "proceso_nominacion_seleccion", "criterios_seleccion_proyectos_calidad"),
]


def veredictos(texto):
    return [json.loads(l) for l in texto.splitlines() if l.strip()]


def sobrevive(razon):
    m = re.search(r"Sobrevive ([a-z0-9_]+)", razon or "")
    return m.group(1) if m else None


def nodo(nid):
    ruta = os.path.join(NODOS, nid + ".json")
    if not os.path.exists(ruta):
        return None
    return json.load(io.open(ruta, encoding="utf-8"))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("LOS TRES EJEMPLARES DE LA PRECISION DE LA ESTRELLA (vuelta 54, TAREA 1.1)")
    print("=" * 78)
    print()

    hoy = veredictos(io.open(VER, encoding="utf-8").read())
    r = subprocess.run(["git", "show", "%s:docs/INTRA_DOMINIO_VEREDICTOS.jsonl" % ANTES],
                       cwd=RAIZ, capture_output=True)
    if r.returncode != 0:
        raise SystemExit("ROJO: no puedo leer los veredictos en %s" % ANTES)
    viejo = {p["puesto_intra"]: p for p in veredictos(r.stdout.decode("utf-8"))}

    print("  clase ANTES = la del commit %s (cierre de la vuelta 52), que es con la" % ANTES)
    print("  que la vuelta 53 leyo los tres actos. clase HOY = la del archivo vigente.")
    print()

    todo_ok = True
    for titulo, centro, sup in EJEMPLARES:
        print("-" * 78)
        print("ACTO: %s   |   CENTRO: %s" % (titulo, centro))
        print("-" * 78)
        pares_a_antes = []
        pierde = []
        for p in hoy:
            if centro not in (p["nodo_a"], p["nodo_b"]):
                continue
            n = p["puesto_intra"]
            v = viejo.get(n)
            cl_antes = v["clase"] if v else "(no estaba)"
            sob_antes = sobrevive(v.get("razon") if v else None)
            otro = p["nodo_b"] if p["nodo_a"] == centro else p["nodo_a"]
            print("  puesto %-5s  clase ANTES: %-12s clase HOY: %-3s  contra %s"
                  % (n, cl_antes, p["clase"], otro))
            print("     la letra cierra con: %s" % ("Sobrevive " + sob_antes if sob_antes
                                                    else "(no nombra superviviente)"))
            if cl_antes == "A":
                pares_a_antes.append(n)
                if sob_antes and sob_antes != centro:
                    pierde.append(n)
        print()
        print("  pares A al abrir la vuelta 53 : %s (son %d)"
              % (pares_a_antes, len(pares_a_antes)))
        print("  pares A que el centro PIERDE  : %s" % (pierde if pierde else "NINGUNO"))
        print("  GANADOR POR DERECHO de sus pares A (9.3.1 corregido, solo cuenta las A): %s"
              % ("SI" if pares_a_antes and not pierde else "NO"))
        oc = nodo(centro)
        os_ = nodo(sup)
        print("  el CENTRO hoy       : %s | deprecado: %s"
              % (centro, (oc or {}).get("deprecado")))
        print("  el SUPERVIVIENTE hoy: %s | deprecado: %s | lleva el alias del centro: %s"
              % (sup, (os_ or {}).get("deprecado"),
                 centro in ((os_ or {}).get("ids_alias") or [])))
        if not (oc and oc.get("deprecado") is True):
            todo_ok = False
            print("  ROJO: el centro NO esta deprecado")
        if not (os_ and not os_.get("deprecado")):
            todo_ok = False
            print("  ROJO: el superviviente NO esta vivo")
        print()

    print("=" * 78)
    print("LOS TRES CENTROS MUERTOS Y LOS TRES SUPERVIVIENTES VIVOS: %s"
          % ("SI" if todo_ok else "NO"))
    print("FIN")
    return 0 if todo_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
