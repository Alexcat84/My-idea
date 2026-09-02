# -*- coding: utf-8 -*-
r"""diagnostico_ciclo_a_medias.py . QUE EL FALSO ROJO SE DELATE SOLO
(TAREA 5 de la vuelta 150). Nombre estable, SIN numero de vuelta.

POR QUE NACE, Y NO ES UNA MEJORA DE ESTILO. En la vuelta 149 el auditor corrio
`run_phase1.py` suelto, fuera del orden del ciclo, y se saco un falso rojo de la
suite del motor: "AssertionError: 71 nodos divergentes entre las dos copias". No
era un rojo del catalogo: era el comando 2 del ciclo sin correr. Es la MISMA
trampa que el acta 147 registro contra si misma en su 4.3.c, y con la 149 son
CUATRO actas seguidas cayendo en ella. El aviso escrito no basta: hace falta que
muerda. Y mordio en la propia vuelta 150, sobre el ejecutor, antes de que esta
guarda existiera: el guardian de commit aborto con las mismas 71 lineas.

QUE HACE. Recibe el diccionario de divergencias entre las dos copias del grafo y
devuelve un DIAGNOSTICO en texto que dice, en una linea, si el rojo es de verdad
o si es un ciclo sin cerrar, Y NOMBRA EL COMANDO QUE FALTA.

COMO LO DECIDE, y es determinista, sin fechas ni mtimes: la curaduria de cara NO
vive en los nodos, vive en `dataset/metadata/etiquetas_de_cara_v1*.json`. El
comando 1 del ciclo (`run_phase1.py`) RECOMPILA `master_graph.json` desde
`dataset/nodos/*.json` y por diseno NO reaplica la curaduria; el comando 2
(`etiquetas_de_cara.py --aplicar`) la vuelve a poner en la copia del dataset; el
comando 3 (`sync_assets_web.py`) la lleva a la copia de la web. Asi que:

  - si TODA la divergencia es del campo `etiqueta_arbol`, y en la copia del
    DATASET la etiqueta NO es la canonica mientras que en la de la WEB SI lo es,
    lo que falta es el COMANDO 2, y se dice con su linea de orden entera;
  - si toda la divergencia es de `etiqueta_arbol` y es al reves (el dataset trae
    la canonica y la web no), lo que falta es el COMANDO 3;
  - si la divergencia toca CUALQUIER OTRO CAMPO, el diagnostico dice, con esas
    palabras, que NO es la firma de un ciclo a medias, y lista los campos. UN
    ROJO LEGITIMO NO SE TAPA (TAREA 5.b): esta guarda anade diagnostico, nunca
    una excepcion. El `assert` sigue cayendo y el exit code sigue siendo 1 en
    los tres casos.

LA OTRA PUERTA, LA DEL `numstat` (TAREA 5.a). `diagnostico_numstat()` dice lo
mismo cuando lo que sale sucio es `dataset/metadata/master_graph.json`, y avisa
ademas de una trampa que mordio al ejecutor en esta misma vuelta 150: `git diff
--numstat` compara el arbol contra el INDICE, no contra HEAD, asi que despues de
un `git add` a mitad del ciclo puede salir sucio con el arbol perfectamente
igual a HEAD. La vara buena es `git diff HEAD --numstat`.

PRUEBA DE MUTACION Y CASO DE CONTROL: scripts/loop/vuelta150_5c_mutacion_ciclo.py.

USO COMO LIBRERIA:
  from diagnostico_ciclo_a_medias import diagnosticar
  print(diagnosticar(dif, nodos_dataset, nodos_web))

USO COMO PROGRAMA (lee las dos copias del disco y diagnostica lo que encuentre):
  python scripts/loop/diagnostico_ciclo_a_medias.py
"""
import glob
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA_DATASET = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
RUTA_WEB = os.path.join(RAIZ, "web", "lib", "assets", "master_graph.json")

ORDEN_DEL_CICLO = (
    "  1) python scripts/run_phase1.py --reaplico-curaduria\n"
    "  2) python scripts/etiquetas_de_cara.py --aplicar        <- reaplica la curaduria\n"
    "  3) python scripts/sync_assets_web.py                    <- la lleva a la copia web\n"
    "  4) git diff HEAD --numstat -- dataset/ web/ engine/     <- tiene que salir SIN FILAS"
)


def etiquetas_canonicas():
    """La curaduria, leida de su fuente y no de los nodos."""
    canon = {}
    for ruta in sorted(glob.glob(os.path.join(RAIZ, "dataset", "metadata",
                                              "etiquetas_de_cara_v1*.json"))):
        try:
            with open(ruta, encoding="utf-8") as fh:
                d = json.load(fh)
        except (OSError, ValueError):
            continue
        if isinstance(d, dict):
            for k, v in d.items():
                if isinstance(v, str):
                    canon[k] = v
    return canon


def diagnosticar(dif, nodos_dataset, nodos_web):
    """dif: {node_id: 'campo,campo'} tal como lo devuelve gemelos_divergentes."""
    if not dif:
        return ""
    campos = set()
    for v in dif.values():
        for c in str(v).split(","):
            if c.strip():
                campos.add(c.strip())

    lineas = []
    lineas.append("")
    lineas.append("  " + "-" * 72)
    lineas.append("  DIAGNOSTICO DEL CICLO (scripts/loop/diagnostico_ciclo_a_medias.py)")
    lineas.append("  nodos divergentes: %d | campos que divergen: %s"
                  % (len(dif), ", ".join(sorted(campos))))

    if campos != {"etiqueta_arbol"}:
        lineas.append("  VEREDICTO: **ESTO NO ES UN CICLO A MEDIAS.** La divergencia toca")
        lineas.append("  campos que el ciclo no escribe (%s)."
                      % ", ".join(sorted(campos - {"etiqueta_arbol"})))
        lineas.append("  ES UN ROJO DE VERDAD y hay que mirarlo. No lo tape el diagnostico.")
        lineas.append("  " + "-" * 72)
        return "\n".join(lineas)

    canon = etiquetas_canonicas()
    falta_2 = falta_3 = sin_canon = 0
    for nid in dif:
        c = canon.get(nid)
        a = (nodos_dataset.get(nid) or {}).get("etiqueta_arbol")
        b = (nodos_web.get(nid) or {}).get("etiqueta_arbol")
        if c is None:
            sin_canon += 1
        elif a != c and b == c:
            falta_2 += 1
        elif a == c and b != c:
            falta_3 += 1

    lineas.append("  la divergencia es SOLO de `etiqueta_arbol`, que es la curaduria de cara,")
    lineas.append("  y la curaduria NO vive en los nodos: vive en")
    lineas.append("  dataset/metadata/etiquetas_de_cara_v1*.json (%d etiquetas canonicas leidas)."
                  % len(canon))
    lineas.append("  reparto contra la canonica: dataset desfasado y web al dia: %d | "
                  "dataset al dia y web desfasada: %d | sin canonica: %d"
                  % (falta_2, falta_3, sin_canon))

    if falta_2 and not falta_3:
        lineas.append("  VEREDICTO: **EL CICLO PUDO QUEDARSE A MEDIAS. FALTA EL COMANDO 2.**")
        lineas.append("  El comando 1 recompilo el grafo y por diseno NO reaplica la curaduria.")
        lineas.append("  FALTA: python scripts/etiquetas_de_cara.py --aplicar")
    elif falta_3 and not falta_2:
        lineas.append("  VEREDICTO: **EL CICLO PUDO QUEDARSE A MEDIAS. FALTA EL COMANDO 3.**")
        lineas.append("  La curaduria esta en el dataset y no llego a la copia de la web.")
        lineas.append("  FALTA: python scripts/sync_assets_web.py")
    elif falta_2 and falta_3:
        lineas.append("  VEREDICTO: **EL CICLO PUDO QUEDARSE A MEDIAS**, con desfase por los")
        lineas.append("  DOS lados. FALTAN el comando 2 y el comando 3, en ese orden.")
    else:
        lineas.append("  VEREDICTO: divergencia de `etiqueta_arbol` que NO calza con ninguna")
        lineas.append("  mitad del ciclo (ninguna de las dos copias trae la canonica).")
        lineas.append("  ES UN ROJO DE VERDAD y hay que mirarlo.")
        lineas.append("  " + "-" * 72)
        return "\n".join(lineas)

    lineas.append("")
    lineas.append("  EL CICLO ENTERO Y EN SU ORDEN:")
    lineas.append(ORDEN_DEL_CICLO)
    lineas.append("")
    lineas.append("  SI DESPUES DE CORRERLO ENTERO LAS DOS COPIAS SIGUEN DIVERGIENDO, ESO")
    lineas.append("  SIGUE SIENDO ROJO Y SIGUE PARANDO. Este diagnostico no es una excepcion.")
    lineas.append("  " + "-" * 72)
    return "\n".join(lineas)


def diagnostico_numstat(filas_sucias):
    """filas_sucias: las lineas de `git diff ... --numstat` que hayan salido."""
    if not filas_sucias:
        return ""
    lineas = []
    lineas.append("")
    lineas.append("  " + "-" * 72)
    lineas.append("  DIAGNOSTICO DEL CICLO, POR LA PUERTA DEL numstat")
    lineas.append("  filas sucias: %d" % len(filas_sucias))
    for f in filas_sucias[:5]:
        lineas.append("    %s" % f)
    if any("dataset/metadata/master_graph.json" in f for f in filas_sucias):
        lineas.append("  master_graph.json del dataset esta sucio. EL CICLO PUDO QUEDARSE A")
        lineas.append("  MEDIAS: el comando 1 recompila y no reaplica la curaduria.")
        lineas.append("")
        lineas.append("  EL CICLO ENTERO Y EN SU ORDEN:")
        lineas.append(ORDEN_DEL_CICLO)
        lineas.append("")
        lineas.append("  Y UNA TRAMPA QUE MORDIO EN LA VUELTA 150: `git diff --numstat` compara")
        lineas.append("  el arbol contra el INDICE, no contra HEAD. Despues de un `git add` a")
        lineas.append("  mitad del ciclo puede salir sucio con el arbol IGUAL a HEAD. La vara")
        lineas.append("  buena es `git diff HEAD --numstat`.")
    lineas.append("  " + "-" * 72)
    return "\n".join(lineas)


def _main():
    import sys
    sys.path.insert(0, os.path.join(RAIZ, "scripts"))
    from run_phase1 import gemelos_divergentes
    with open(RUTA_DATASET, encoding="utf-8") as fh:
        a = json.load(fh)["nodos"]
    with open(RUTA_WEB, encoding="utf-8") as fh:
        b = json.load(fh)["nodos"]
    dif = gemelos_divergentes(a, b)
    if not dif:
        print("las dos copias del grafo dicen lo mismo: nada que diagnosticar.")
        return
    print(diagnosticar(dif, a, b))


if __name__ == "__main__":
    _main()
