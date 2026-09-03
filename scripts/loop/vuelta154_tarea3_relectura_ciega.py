# -*- coding: utf-8 -*-
"""vuelta154_tarea3_relectura_ciega.py . TAREA 3 DE LA VUELTA 154.

LA RELECTURA AL DOBLE DEL TRAMO, que es lo que la regla del credito manda cuando
aparece un hallazgo fuera de lo marcado (acta 153, seccion 7). EL TRAMO ES EL
REGISTRO DE CITAS DE `OP-C-05`, y dentro de el las 121 LECTURAS DIRIGIDAS.

LA MUESTRA SE ELIGE POR COMPUTO Y NO A DEDO, con la zancada escrita en la
salida: zancada 3 arrancando en el puesto 1 sobre los 121 pares de via
LECTURA_DIRIGIDA ordenados por su cita (LD-OPC05-001 en adelante). Da 41
puestos, que pasa del piso de 32 que el encargo fija y es MAS DEL DOBLE de la
muestra de ocho con la que el auditor cerro la vuelta 153.

DOS MODOS, Y EL ORDEN IMPORTA:

  --ciego   imprime SOLO el titulo y los pasos accionables de los dos nodos, sin
            clase, sin via, sin cita y SIN LA RAZON ESCRITA. Es lo unico que el
            lector ve cuando adjudica.
  --destapar
            lee el fichero de adjudicaciones que el lector escribio DESPUES del
            ciego y ANTES de este modo, destapa la razon escrita en el registro
            y coteja. Publica cuantas coinciden y cuantas discrepan, y NO
            arregla ninguna discrepancia: la nombra.

EL FICHERO DE ADJUDICACIONES es docs/loop/SALIDA_V154_T3_MIS_ADJUDICACIONES.txt,
una linea por puesto con el formato `CASO N | CLASE | mi razon`. Se escribe con
el ciego delante y el registro cerrado, y se commitea ANTES de destapar, para
que el orden quede probado por git y no por mi palabra.

LA CLAVE ES EL NUMERO DE CASO Y NO LA CITA, y no es un detalle: el ciego OMITE
la cita a proposito, asi que teclear la cita en el fichero de adjudicaciones
seria haber mirado el registro. El numero de caso es lo unico que el ciego da.

USO:
  python scripts/loop/vuelta154_tarea3_relectura_ciega.py --ciego
  python scripts/loop/vuelta154_tarea3_relectura_ciega.py --destapar
"""
import argparse
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REGISTRO = os.path.join(RAIZ, "docs", "plan", "REGISTRO_DE_CITAS_OPC05.jsonl")
NODOS = os.path.join(RAIZ, "dataset", "nodos")
MIS = os.path.join(RAIZ, "docs", "loop", "SALIDA_V154_T3_MIS_ADJUDICACIONES.txt")

ZANCADA = 3
ARRANQUE = 1


def dirigidas():
    E = []
    for linea in io.open(REGISTRO, encoding="utf-8"):
        if not linea.strip():
            continue
        d = json.loads(linea)
        if d.get("via") == "LECTURA_DIRIGIDA":
            E.append(d)
    E.sort(key=lambda d: d["cita"])
    return E


def muestra():
    E = dirigidas()
    sel = [E[i] for i in range(ARRANQUE - 1, len(E), ZANCADA)]
    return E, sel


def nodo(nid):
    ruta = os.path.join(NODOS, nid + ".json")
    if not os.path.exists(ruta):
        return None
    return json.load(io.open(ruta, encoding="utf-8"))


def ciego():
    E, sel = muestra()
    print("=" * 96)
    print("VUELTA 154, TAREA 3: LA RELECTURA AL DOBLE DEL TRAMO, EN CIEGO")
    print("=" * 96)
    print("UNIVERSO: %d lectura(s) dirigida(s) en docs/plan/REGISTRO_DE_CITAS_OPC05.jsonl"
          % len(E))
    print("MUESTRA POR COMPUTO: zancada %d, arranque en el puesto %d, ordenadas por cita."
          % (ZANCADA, ARRANQUE))
    print("SELECCIONADAS: %d puesto(s). Piso del encargo: 32. Muestra del auditor en la"
          % len(sel))
    print("vuelta 153: 8. Esta pasa del doble de aquella y del piso.")
    print("")
    print("AQUI NO HAY CLASE, NI VIA, NI CITA, NI LA RAZON ESCRITA: solo los dos nodos.")
    print("")
    for k, d in enumerate(sel, 1):
        a, b = d["par"]
        print("=" * 96)
        print("CASO %d de %d" % (k, len(sel)))
        for nid in (a, b):
            n = nodo(nid)
            if n is None:
                print("  --- %s (NO EXISTE COMO FICHERO)" % nid)
                continue
            print("  --- %s (deprecado=%s, dominio=%s)"
                  % (nid, n.get("deprecado"), n.get("dominio")))
            print("      titulo: %s" % n.get("titulo_concepto"))
            for i, p in enumerate(n.get("pasos_accionables") or [], 1):
                print("      %2d. %s" % (i, p))
        print("")
    print("=" * 96)
    print("CIFRA lecturas dirigidas del universo: %d pares" % len(E))
    print("CIFRA puestos de la muestra ciega: %d pares" % len(sel))


def destapar():
    E, sel = muestra()
    if not os.path.exists(MIS):
        print("ROJO: no existe %s. El ciego se adjudica ANTES de destapar." % MIS)
        raise SystemExit(1)
    mias = {}
    for linea in io.open(MIS, encoding="utf-8"):
        linea = linea.strip()
        if not linea or linea.startswith("#") or "|" not in linea:
            continue
        partes = [x.strip() for x in linea.split("|", 2)]
        if len(partes) == 3:
            mias[partes[0]] = (partes[1], partes[2])

    print("=" * 96)
    print("VUELTA 154, TAREA 3: EL DESTAPE Y EL COTEJO")
    print("=" * 96)
    print("MUESTRA POR COMPUTO: zancada %d, arranque %d, %d puesto(s) de %d."
          % (ZANCADA, ARRANQUE, len(sel), len(E)))
    print("Adjudicaciones leidas de %s: %d"
          % (os.path.relpath(MIS, RAIZ).replace("\\", "/"), len(mias)))
    print("")
    print("| # | cita | mi clase a ciegas | clase escrita | coincide |")
    print("|---:|---|---|---|---|")
    coinciden = 0
    discrepan = []
    faltan = []
    for k, d in enumerate(sel, 1):
        cita = d["cita"].split(",")[0].strip()
        clave = "CASO %d" % k
        if clave not in mias:
            faltan.append(cita)
            print("| %d | %s | (SIN ADJUDICAR) | %s | NO |" % (k, cita, d["clase"]))
            continue
        mia, _razon = mias[clave]
        ok = mia.upper().startswith(d["clase"].upper())
        coinciden += 1 if ok else 0
        if not ok:
            discrepan.append((cita, mia, d["clase"]))
        print("| %d | %s | %s | %s | %s |" % (k, cita, mia, d["clase"], "si" if ok else "NO"))
    print("")
    print("CONTADO: %d coinciden, %d discrepan, %d sin adjudicar, sobre %d puesto(s)."
          % (coinciden, len(discrepan), len(faltan), len(sel)))
    print("")
    if discrepan:
        print("LAS QUE DISCREPAN, CON SU CASO ESCRITO Y SIN ARREGLARLAS:")
        for cita, mia, esc in discrepan:
            print("  %s: yo a ciegas %s, escrito %s" % (cita, mia, esc))
    else:
        print("NINGUNA DISCREPA.")
    print("")
    print("EL DESTAPE, PUESTO A PUESTO: mi razon a ciegas contra la razon escrita.")
    for k, d in enumerate(sel, 1):
        cita = d["cita"].split(",")[0].strip()
        mia, razon_mia = mias.get("CASO %d" % k, ("(sin adjudicar)", ""))
        print("")
        print("  CASO %d, %s  %s <-> %s" % (k, cita, d["par"][0], d["par"][1]))
        print("    mi clase a ciegas: %s" % mia)
        print("    mi razon a ciegas: %s" % razon_mia)
        print("    clase escrita    : %s" % d["clase"])
        print("    razon escrita    : %s" % d["razon"])
    print("")
    print("CIFRA puestos releidos en la muestra: %d pares" % len(sel))
    print("CIFRA puestos que coinciden: %d pares" % coinciden)
    print("CIFRA puestos que discrepan: %d pares" % len(discrepan))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ciego", action="store_true")
    ap.add_argument("--destapar", action="store_true")
    a = ap.parse_args()
    if a.ciego:
        ciego()
    elif a.destapar:
        destapar()
    else:
        ap.error("hay que elegir --ciego o --destapar")


main()
