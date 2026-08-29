# -*- coding: utf-8 -*-
"""vuelta126_ops10_tramo1_reencuadre.py . PRIMER TRAMO DE OP-S-10 (TAREA 3.d
de la vuelta 126): antepone UNA condicion de activacion que nombra EL PAIS
(Estados Unidos) a los DIEZ primeros nodos VIVOS de la nomina de OP-S-10, en
orden alfabetico de id, que hoy NO nombran el pais en condiciones_activacion.

LA FORMA (discutible marcado en el reporte): se reusa LITERAL la clausula del
contramodelo comprender_definicion_legal_franquicia, "Solo aplica si vendes o
piensas vender franquicias en Estados Unidos", identica en los diez nodos, en
vez de una redaccion distinta por nodo. Se antepone (queda en la posicion 0
de condiciones_activacion); las condiciones que ya existian quedan enteras,
en su orden, DETRAS de la nueva.

ALCANCE, EXACTO Y CERRADO, LEIDO DE LA REMEDICION DE 3.c
(docs/loop/SALIDA_V126_3C_REMEDICION_OPS10.txt): de los 28 vivos de la
nomina, se excluyen los DOS contramodelos (ya condicionan bien, verificacion
4 de la operacion) y se toman los primeros DIEZ en orden alfabetico de los
26 restantes:
  alternativa_business_opportunity_licensing
  alternativa_trademark_licensing
  calculo_roi_franquiciado_2
  calificacion_prospectos_award
  concepto_de_advances
  cumplir_leyes_estatales_franquicia
  decision_fpr
  decision_marca_comun_branding
  desarrollar_manual_operaciones
  diseno_programa_capacitacion_franquicia

GUARDAS PROPIAS, ademas de las de REGIMEN B: los diez nodos existen y estan
VIVOS; ningun otro campo de ningun nodo cambia; las condiciones viejas
quedan intactas y en su orden; la condicion nueva es identica en los diez;
cero guiones largos y cero guiones medios en el texto nuevo.

MODOS: --simular (por defecto, cero escrituras) y --ejecutar.
--mutacion-negativa fuerza la nomina a incluir un nodo DEPRECADO
(elaboracion_fdd) para probar que la guarda aborta SIN ESCRIBIR.

Uso:
  python scripts/loop/vuelta126_ops10_tramo1_reencuadre.py
  python scripts/loop/vuelta126_ops10_tramo1_reencuadre.py --ejecutar
  python scripts/loop/vuelta126_ops10_tramo1_reencuadre.py --mutacion-negativa
"""
import argparse
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")

TRAMO = [
    "alternativa_business_opportunity_licensing",
    "alternativa_trademark_licensing",
    "calculo_roi_franquiciado_2",
    "calificacion_prospectos_award",
    "concepto_de_advances",
    "cumplir_leyes_estatales_franquicia",
    "decision_fpr",
    "decision_marca_comun_branding",
    "desarrollar_manual_operaciones",
    "diseno_programa_capacitacion_franquicia",
]

CONDICION_NUEVA = "Solo aplica si vendes o piensas vender franquicias en Estados Unidos"


def ruta(nid):
    return os.path.join(NODOS, nid + ".json")


def leer_crudo(nid):
    with io.open(ruta(nid), encoding="utf-8", newline="") as fh:
        bruto = fh.read()
    cola = ""
    while bruto and bruto[-1] in "\r\n":
        cola = bruto[-1] + cola
        bruto = bruto[:-1]
    return json.loads(bruto), cola


def escribir(nid, datos, cola):
    with io.open(ruta(nid), "w", encoding="utf-8", newline="") as fh:
        fh.write(json.dumps(datos, ensure_ascii=False, indent=2) + cola)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ejecutar", action="store_true")
    ap.add_argument("--mutacion-negativa", action="store_true",
                     help="cuela un nodo DEPRECADO en la nomina, para probar que la guarda aborta")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    nomina = list(TRAMO)
    if a.mutacion_negativa:
        nomina[3] = "elaboracion_fdd"  # DEPRECADO a proposito

    modo = "MUTACION NEGATIVA (nunca escribe)" if a.mutacion_negativa else ("EJECUTAR" if a.ejecutar else "SIMULAR")
    print("=" * 78)
    print("OP-S-10, TRAMO 1, REENCUADRE DE MARCO (vuelta 126) . MODO %s" % modo)
    print("=" * 78)

    if "—" in CONDICION_NUEVA or "–" in CONDICION_NUEVA or " - " in CONDICION_NUEVA:
        print("SE ABORTA SIN ESCRIBIR: la condicion nueva lleva guion largo o medio.")
        return 1

    fallos = []
    datos = {}
    for nid in nomina:
        try:
            d, c = leer_crudo(nid)
        except IOError as e:
            fallos.append("%s no se pudo leer: %s" % (nid, e))
            continue
        if d.get("deprecado"):
            fallos.append("%s esta DEPRECADO" % nid)
            continue
        datos[nid] = (d, c)

    if len(set(nomina)) != len(nomina):
        fallos.append("la nomina tiene ids repetidos")

    print("guarda 1, los %d nodos existen y estan VIVOS: %s" % (len(nomina), "OK" if not fallos else "ROJO %s" % fallos))
    if fallos:
        print()
        print("SE ABORTA SIN ESCRIBIR, %d fallo(s):" % len(fallos))
        for f in fallos:
            print("  [ROJO] %s" % f)
        return 1

    ya_puesta = [nid for nid, (d, c) in datos.items()
                 if (d.get("condiciones_activacion") or [None])[:1] == [CONDICION_NUEVA]]
    if ya_puesta:
        fallos.append("la condicion YA esta puesta en: %s" % ya_puesta)
    print("guarda 2, la condicion NO estaba puesta todavia: %s" % ("OK" if not ya_puesta else "ROJO"))

    if fallos:
        print()
        print("SE ABORTA SIN ESCRIBIR, %d fallo(s):" % len(fallos))
        for f in fallos:
            print("  [ROJO] %s" % f)
        return 1

    orig = {nid: json.loads(json.dumps(d)) for nid, (d, c) in datos.items()}
    for nid, (d, c) in datos.items():
        cond = list(d.get("condiciones_activacion") or [])
        d["condiciones_activacion"] = [CONDICION_NUEVA] + cond

    rotos_otros_campos = []
    rotos_orden_viejo = []
    for nid, (d, c) in datos.items():
        for k in d:
            if k == "condiciones_activacion":
                continue
            if d[k] != orig[nid].get(k):
                rotos_otros_campos.append((nid, k))
        vieja = orig[nid].get("condiciones_activacion") or []
        nueva_cola = d["condiciones_activacion"][1:]
        if nueva_cola != vieja:
            rotos_orden_viejo.append(nid)

    print("guarda 3, ningun otro campo cambia: %s" % ("OK" if not rotos_otros_campos else "ROJO %s" % rotos_otros_campos))
    print("guarda 4, las condiciones viejas quedan intactas y en su orden: %s"
          % ("OK" if not rotos_orden_viejo else "ROJO %s" % rotos_orden_viejo))
    if rotos_otros_campos or rotos_orden_viejo:
        fallos.append("guarda 3/4 caida")

    if fallos:
        print()
        print("SE ABORTA SIN ESCRIBIR, %d fallo(s):" % len(fallos))
        for f in fallos:
            print("  [ROJO] %s" % f)
        return 1

    print()
    for nid in nomina:
        print("%s.condiciones_activacion[0]: %r" % (nid, datos[nid][0]["condiciones_activacion"][0]))

    if a.mutacion_negativa:
        print()
        print("MUTACION NEGATIVA: no debia llegar aqui con un nodo DEPRECADO en la nomina. CAIDA DE LA ARNES.")
        return 1

    if not a.ejecutar:
        print()
        print("SIMULACION: cero escrituras.")
        return 0

    for nid, (d, c) in datos.items():
        escribir(nid, d, c)
    print()
    print("ESCRITO. ficheros tocados: %d" % len(datos))
    return 0


if __name__ == "__main__":
    sys.exit(main())
