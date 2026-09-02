# -*- coding: utf-8 -*-
r"""vuelta146_3b_sellar_nomina_aduana.py . SELLA LA NOMINA ADJUDICADA DE LA
COMPROBACION POSICIONAL (TAREA 3.b de la vuelta 146, ejecucion de `OP-A-01`).

QUE ESCRIBE. `dataset/metadata/aduana_fuente_multiple.json`, la nomina de los
nodos vivos que HOY declaran mas de una fuente, con su lista de declaraciones
EN ORDEN. Es el dato contra el que la comprobacion posicional de Gate 0 mide.

LA NOMINA SE GENERA, NO SE TECLEA (`EJECUTOR.md` 1, "la tabla se imprime, no se
teclea"): cada fila sale de leer `dataset/nodos/*.json` en esta corrida. Este
script es idempotente y se puede volver a correr; si el catalogo cambiara, la
nomina cambiaria con el, Y ESO ES PRECISAMENTE LO QUE NO DEBE HACERSE A LA
LIGERA, porque re-sellar la nomina es re-adjudicar: la nomina existe para que
un nodo nuevo con dos libros NO PUEDA ENTRAR CALLADO, y regenerarla sin leer
seria abrirle la puerta. Por eso el fichero lleva su propia advertencia dentro.

QUE NO DICE ESTA NOMINA, y es lo que mas importa que no se lea de mas: NO dice
que el reparto de material de esos nodos este adjudicado por lectura. Dice que
esos son los que habia AL CABLEAR EL CONTROL, con su corte. La aduana garantiza
que la lista no se mueva en silencio, no que la lista sea buena.

USO:
  python scripts/loop/vuelta146_3b_sellar_nomina_aduana.py
"""
import glob
import io
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
DESTINO = os.path.join(RAIZ, "dataset", "metadata", "aduana_fuente_multiple.json")
SEP = " | "


def corte():
    """La fecha se lee de git, nunca se teclea (`EJECUTOR.md`, LA IDENTIDAD SE
    LEE DE GIT)."""
    r = subprocess.run(["git", "log", "-1", "--format=%ad", "--date=short"],
                       cwd=RAIZ, capture_output=True, text=True, check=True)
    return r.stdout.strip()


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    filas = []
    for p in sorted(glob.glob(os.path.join(NODOS, "*.json"))):
        d = json.loads(io.open(p, encoding="utf-8").read())
        if d.get("deprecado"):
            continue
        f = d.get("fuente")
        if not isinstance(f, str):
            continue
        ds = [x.strip() for x in f.split(SEP) if x.strip()]
        if len(ds) > 1:
            filas.append({
                "node_id": d.get("node_id") or os.path.splitext(os.path.basename(p))[0],
                "fuente": ds,
                "pasos_accionables": len(d.get("pasos_accionables") or []),
            })

    doc = {
        "que_es": ("Nomina ADJUDICADA de los nodos vivos que declaran MAS DE UNA "
                   "fuente. Es el dato contra el que mide la comprobacion posicional "
                   "de Gate 0 (OP-A-01, verificacion 1; BANCO_DEL_PLAN.md P.2)."),
        "para_que": ("Que un nodo NUEVO con dos libros no pueda entrar callado, y que "
                     "a un nodo ya adjudicado no se le pueda anadir un segundo libro en "
                     "silencio: la lista se coteja ENTERA Y EN ORDEN."),
        "lo_que_NO_dice": ("NO dice que el reparto de material de estos nodos este "
                           "adjudicado por lectura. Dice que estos son los que habia al "
                           "cablear el control, con su corte."),
        "como_se_cambia": ("Re-sellar esta nomina es RE-ADJUDICAR. No se regenera para "
                           "hacer callar a Gate 0: se lee el nodo nuevo, se adjudica y "
                           "entonces se sella, y el cambio se declara en el reporte."),
        "generado_por": "scripts/loop/vuelta146_3b_sellar_nomina_aduana.py",
        "fecha_corte": corte(),
        "adjudicados": filas,
    }
    with io.open(DESTINO, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(doc, ensure_ascii=False, indent=2) + "\n")
    print("SELLADA %s" % os.path.relpath(DESTINO, RAIZ))
    print("  fecha_corte leida de git: %s" % doc["fecha_corte"])
    print("  adjudicados: %d" % len(filas))
    for x in filas:
        print("     %s -> %d declaracion(es), %d paso(s)"
              % (x["node_id"], len(x["fuente"]), x["pasos_accionables"]))
    print("CIFRA nodos adjudicados con mas de una fuente: %d nodos" % len(filas))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
