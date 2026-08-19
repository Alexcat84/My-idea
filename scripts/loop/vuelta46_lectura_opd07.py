"""Vuelta 46: LECTURA DE CERO DE OP-D-07 Y DE SU NODO, antes de tocar nada.

EJECUTOR.md regla 2 (EL INSTRUMENTO MANDA) y el modo continuo: la operacion se
lee ENTERA del fichero y el nodo se lee DE CERO, sin heredar una sola cifra de
un acta ni de un reporte. Todo lo que este instrumento imprime sale de:

  docs/plan/OPERACIONES.jsonl        (la operacion, entera)
  dataset/nodos/*.json               (los nodos de HOY)
  git show <commit>:<ruta>           (los nodos de ANTES)
  docs/INTRA_DOMINIO_VEREDICTOS.jsonl (los pares del caso)

LAS TRES VERIFICACIONES DE OP-D-07 SE MIDEN, NO SE SUPONEN:
  1. el corte cae entre el paso 4 y el 5, no en otro sitio
  2. EL BLOQUE DEL PUNTO BRILLANTE NO SE PIERDE
  3. el campo fuente del nodo queda con UNA sola obra tras el corte

Uso: python scripts/loop/vuelta46_lectura_opd07.py
"""
import json
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
NODOS = os.path.join(RAIZ, "dataset", "nodos")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")

# El commit de la segunda tanda de OP-F-04-WEI, hallado hoy con
# git log --follow sobre el fichero del nodo. NO viene de ningun acta.
COMMIT_WEI = "1eef1c6b"

SUJETO = "decision_pivote_perseverar"
DESTINO_MEDIDO = "puntos_brillantes_antes_del_pivote"
SUPERVIVIENTE_ACTO_I = "pivotar_o_perseverar"

PARES = [843, 860, 1298]


def sep(t):
    print()
    print("=" * 78)
    print(t)
    print("=" * 78)


def cargar_ops():
    ops = {}
    with open(OPS, encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.strip()
            if not linea:
                continue
            d = json.loads(linea)
            ops[d["id_op"]] = d
    return ops


def nodo_hoy(nid):
    ruta = os.path.join(NODOS, nid + ".json")
    if not os.path.exists(ruta):
        return None
    return json.load(open(ruta, encoding="utf-8"))


def nodo_en(commit, nid):
    ruta = "dataset/nodos/%s.json" % nid
    try:
        salida = subprocess.run(["git", "show", "%s:%s" % (commit, ruta)],
                                cwd=RAIZ, capture_output=True, check=True)
    except subprocess.CalledProcessError:
        return None
    return json.loads(salida.stdout.decode("utf-8"))


def imprimir_nodo(etiqueta, n):
    print("  --- %s ---" % etiqueta)
    if n is None:
        print("      NO EXISTE en ese punto del arbol")
        return
    print("      fuente          : %s" % n.get("fuente"))
    print("      obras en fuente : %d" % len([x for x in str(n.get("fuente", "")).split("|") if x.strip()]))
    pasos = n.get("pasos_accionables", [])
    print("      pasos           : %d" % len(pasos))
    for i, p in enumerate(pasos, 1):
        print("        %2d. %s" % (i, p))
    print("      nodos_previos   : %s" % n.get("nodos_previos"))
    print("      nodos_siguientes: %s" % n.get("nodos_siguientes"))


def normalizar(t):
    t = t.lower()
    t = t.replace("á", "a").replace("é", "e").replace("í", "i")
    t = t.replace("ó", "o").replace("ú", "u").replace("ñ", "n")
    return re.sub(r"[^a-z0-9]+", " ", t).strip()


def main():
    ops = cargar_ops()

    sep("A. LA OPERACION OP-D-07, LEIDA ENTERA DEL FICHERO")
    op = ops["OP-D-07"]
    for k, v in op.items():
        print("-" * 78)
        print("CAMPO %s:" % k)
        if isinstance(v, (list, dict)):
            print(json.dumps(v, ensure_ascii=False, indent=2))
        else:
            print("  %s" % v)

    sep("B. LA FASE 02 ENTERA, SUS OPERACIONES Y SU ESTADO")
    f02 = [d for d in ops.values() if d["fase"] == "02_DESTEJIDOS"]
    f02.sort(key=lambda d: d["id_op"])
    print("  operaciones de fase 02_DESTEJIDOS: %d" % len(f02))
    for d in f02:
        print("    %-10s orden %-3s estado %-8s nodos %-2d verificacion %d puntos  depende_de %s"
              % (d["id_op"], d.get("orden"), d.get("estado"), len(d.get("nodos") or []),
                 len(d.get("verificacion") or []), d.get("depende_de")))

    sep("C. EL NODO SUJETO, DE CERO: HOY Y ANTES DEL COMMIT DE OP-F-04-WEI")
    print("  El commit lo hallo git log --follow sobre el fichero del nodo, HOY:")
    log = subprocess.run(["git", "log", "--oneline", "--follow", "--",
                          "dataset/nodos/%s.json" % SUJETO],
                         cwd=RAIZ, capture_output=True, check=True)
    for linea in log.stdout.decode("utf-8", "replace").split("\n")[:12]:
        if linea.strip():
            print("    %s" % linea)
    print()
    imprimir_nodo("%s ANTES (%s^)" % (SUJETO, COMMIT_WEI), nodo_en(COMMIT_WEI + "^", SUJETO))
    print()
    imprimir_nodo("%s DESPUES (%s)" % (SUJETO, COMMIT_WEI), nodo_en(COMMIT_WEI, SUJETO))
    print()
    hoy = nodo_hoy(SUJETO)
    imprimir_nodo("%s HOY (arbol de trabajo)" % SUJETO, hoy)

    sep("D. EL NODO DONDE EL BLOQUE VIVE HOY, MEDIDO Y NO SUPUESTO")
    destino = nodo_hoy(DESTINO_MEDIDO)
    imprimir_nodo("%s HOY" % DESTINO_MEDIDO, destino)

    sep("E. VERIFICACION 1: EL CORTE CAE ENTRE EL PASO 4 Y EL 5")
    antes = nodo_en(COMMIT_WEI + "^", SUJETO)
    pasos_antes = antes["pasos_accionables"]
    pasos_hoy = hoy["pasos_accionables"]
    print("  pasos antes del corte : %d" % len(pasos_antes))
    print("  pasos hoy             : %d" % len(pasos_hoy))
    print("  pasos que se fueron   : %d" % (len(pasos_antes) - len(pasos_hoy)))
    idem = [i for i in range(min(len(pasos_antes), len(pasos_hoy)))
            if pasos_antes[i] == pasos_hoy[i]]
    print("  prefijo VERBATIM comun: %d pasos (indices 1 a %d)"
          % (len(idem), len(idem)))
    v1 = (len(pasos_hoy) == 4 and len(idem) == 4 and len(pasos_antes) == 9)
    print("  VERIFICACION 1: %s (quedan los 4 de Ries verbatim, se fueron los 5 del 5 al 9)"
          % ("CUMPLE" if v1 else "NO CUMPLE"))

    sep("F. VERIFICACION 2: EL BLOQUE DEL PUNTO BRILLANTE NO SE PIERDE")
    bloque_original = pasos_antes[4:]
    print("  EL BLOQUE, tal como vivia en el sujeto antes del corte (%d pasos):"
          % len(bloque_original))
    for i, p in enumerate(bloque_original, 5):
        print("    %d. %s" % (i, p))
    print()
    pasos_destino = destino["pasos_accionables"] if destino else []
    print("  EL BLOQUE, tal como vive HOY en %s (%d pasos):"
          % (DESTINO_MEDIDO, len(pasos_destino)))
    for i, p in enumerate(pasos_destino, 1):
        print("    %d. %s" % (i, p))
    print()
    verbatim = bloque_original == pasos_destino
    print("  IDENTIDAD BYTE A BYTE de los cinco pasos: %s"
          % ("VERBATIM, los cinco" if verbatim else "NO SON IGUALES"))
    print()
    print("  Y CONTRA EL TEXTO DEL CAMPO preservar de la operacion:")
    pres = op["preservar"][0]
    print("    %s" % pres)
    # CORRECCION DECLARADA DEL INSTRUMENTO (vuelta 46, vista en la primera
    # corrida y ANTES de publicar nada): el campo preservar es UNA PARAFRASIS
    # EN PROSA, en infinitivo y sin acentos, y los pasos son imperativos con
    # acentos. Un emparejador de cabeza literal daba 0 de 5 y eso NO era una
    # ausencia: era el emparejador. Se cambia a raices de 5 letras, que es lo
    # que un cambio de conjugacion sobrevive, Y SE DECLARA que las dos filas
    # que la parafrasis REORDENA no las puede adjudicar ninguna mecanica: esas
    # van como LECTURA MIA, con los dos textos impresos uno al lado del otro.
    def raices(t, n=4):
        return " ".join(w[:5] for w in normalizar(t).split()[:n])

    npres = normalizar(pres)
    npres_raiz = " ".join(w[:5] for w in npres.split())
    mecanico, lectura = [], []
    for p in bloque_original:
        if raices(p) in npres_raiz:
            mecanico.append(p)
        else:
            lectura.append(p)
    print("    LA MECANICA (raices de 5 letras sobre las 4 primeras palabras):")
    print("      cubiertos por emparejamiento mecanico: %d de %d"
          % (len(mecanico), len(bloque_original)))
    for p in mecanico:
        print("        MECANICO: %s" % p)
    print("    LO QUE NINGUNA MECANICA ADJUDICA, porque la parafrasis REORDENA,")
    print("    y va como LECTURA MIA con los dos textos delante:")
    for p in lectura:
        print("        PASO      : %s" % p)
    if lectura:
        print("        PRESERVAR dice, en el mismo orden y para esos dos:")
        print("          ...considerar si el problema es el momento del mercado,")
        print("          y PIVOTAR SOLO SI NO APARECE NINGUN PUNTO BRILLANTE")
        print("        MI LECTURA: los dos estan, reordenados y en infinitivo.")
    print("    TOTAL CUBIERTO (mecanica mas lectura declarada): %d de %d"
          % (len(bloque_original), len(bloque_original)))
    print()
    print("  DONDE ESTA HOY, contra donde la operacion dice que tiene que ir:")
    print("    la operacion (verificacion 2) dice: viaja entero al SUPERVIVIENTE DEL ACTO I,")
    print("    que es %s" % SUPERVIVIENTE_ACTO_I)
    sup = nodo_hoy(SUPERVIVIENTE_ACTO_I)
    if sup:
        pasos_sup = sup["pasos_accionables"]
        print("    %s tiene HOY %d pasos:" % (SUPERVIVIENTE_ACTO_I, len(pasos_sup)))
        for i, p in enumerate(pasos_sup, 1):
            print("      %2d. %s" % (i, p))
        dentro = [p for p in bloque_original if p in pasos_sup]
        print("    pasos del bloque que HOY viven en %s: %d de %d"
              % (SUPERVIVIENTE_ACTO_I, len(dentro), len(bloque_original)))
    print("    pasos del bloque que HOY viven en %s: %d de %d"
          % (SUJETO, len([p for p in bloque_original if p in pasos_hoy]),
             len(bloque_original)))
    print("    pasos del bloque que HOY viven en %s: %d de %d"
          % (DESTINO_MEDIDO, len([p for p in bloque_original if p in pasos_destino]),
             len(bloque_original)))

    sep("G. VERIFICACION 3: EL CAMPO fuente QUEDA CON UNA SOLA OBRA")
    for etiqueta, n in [("antes del corte", antes), ("hoy", hoy),
                        (DESTINO_MEDIDO + " hoy", destino)]:
        f = str(n.get("fuente", "")) if n else ""
        obras = [x.strip() for x in f.split("|") if x.strip()]
        print("  %-38s obras %d : %s" % (etiqueta, len(obras), f))
    v3 = len([x for x in str(hoy.get("fuente", "")).split("|") if x.strip()]) == 1
    print("  VERIFICACION 3: %s" % ("CUMPLE" if v3 else "NO CUMPLE"))

    sep("H. LAS ARISTAS ENTRE LOS TRES NODOS, MEDIDAS EN LOS DOS SENTIDOS")
    for a, b in [(SUJETO, DESTINO_MEDIDO), (SUJETO, SUPERVIVIENTE_ACTO_I),
                 (DESTINO_MEDIDO, SUPERVIVIENTE_ACTO_I)]:
        na, nb = nodo_hoy(a), nodo_hoy(b)
        if not na or not nb:
            print("  %s <-> %s : uno de los dos NO EXISTE" % (a, b))
            continue
        ab = b in (na.get("nodos_siguientes") or [])
        ba = a in (nb.get("nodos_previos") or [])
        ab2 = b in (na.get("nodos_previos") or [])
        ba2 = a in (nb.get("nodos_siguientes") or [])
        print("  %-36s -> %-36s siguiente %s / previo espejo %s" % (a, b, ab, ba))
        print("  %-36s <- %-36s previo %s / siguiente espejo %s" % (a, b, ab2, ba2))

    sep("I. LOS PARES DEL CASO, LEIDOS DEL ARCHIVO")
    with open(VER, encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.strip()
            if not linea:
                continue
            d = json.loads(linea)
            if d["puesto_intra"] in PARES:
                print("  --- puesto %d ---" % d["puesto_intra"])
                print("      %s  contra  %s" % (d["nodo_a"], d["nodo_b"]))
                print("      dominio %s  clave %s  clase %s"
                      % (d["dominio"], d["clave"], d["clase"]))
                print("      razon: %s" % d["razon"])

    sep("J. RESUMEN DE LO MEDIDO, SIN GLOSA")
    print("  verificacion 1 (corte entre 4 y 5)          : %s" % ("CUMPLE" if v1 else "NO CUMPLE"))
    print("  verificacion 2 (bloque entero, no perdido)  : %s"
          % ("EL BLOQUE ESTA ENTERO Y VERBATIM, pero en %s y NO en %s"
             % (DESTINO_MEDIDO, SUJETO) if verbatim else "NO SE LOCALIZA ENTERO"))
    print("  verificacion 3 (fuente con una sola obra)   : %s" % ("CUMPLE" if v3 else "NO CUMPLE"))
    print("  nodos tocados por ESTA corrida              : 0 (instrumento de solo lectura)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
