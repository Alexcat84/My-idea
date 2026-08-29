# -*- coding: utf-8 -*-
"""vuelta128_ops10_tramo2_reencuadre.py . SEGUNDO Y ULTIMO TRAMO DE OP-S-10
(TAREA 3.b de la vuelta 128): antepone la misma condicion de activacion que
nombra el pais (Estados Unidos) a los DIECISEIS nodos VIVOS de la nomina que
faltaban tras la vuelta 126.

MISMA FORMA LITERAL que la vuelta 126, sin cambios: "Solo aplica si vendes o
piensas vender franquicias en Estados Unidos", antepuesta (posicion 0 de
condiciones_activacion); las condiciones que ya existian quedan enteras, en
su orden, DETRAS de la nueva. La forma no se discute ni se adapta nodo a
nodo (verificacion 4 de la operacion congela a los dos contramodelos como
modelo).

ALCANCE, MEDIDO EN ESTA VUELTA (scripts/loop/_v128_medir_ops10_tramo2.py):
de los 28 vivos de la nomina de 31, excluidos los DOS contramodelos
(comprender_definicion_legal_franquicia, cumplimiento_ftc_rule_436, ya
condicionan bien) y los DIEZ ya escritos en la vuelta 126, los DIECISEIS
que faltan:
  eleccion_abogado_franquicias
  estimacion_inversion_inicial_franquiciador
  estructura_proveedores_aprobados_designados
  exenciones_legales_franquicia
  financial_performance_representations
  ingresos_por_rebates
  los_tres_grandes_criterios
  multiples_compradores_influyentes
  obtencion_marca_registrada
  preparar_fdd
  proceso_venta_franquicias
  programas_compra_franquicia
  propuesta_valor_franquicia
  proteccion_propiedad_intelectual_franq
  registro_estatal_franquicia
  revision_legal_marketing

CASO obtencion_marca_registrada: su unica condicion vieja dice "Cuando se
planea franquiciar y aun no se posee un trademark federal sobre el nombre de
marca" (adjetivo federal, no pais). Se antepone la condicion nueva IGUAL que
en los demas y NO se reescribe la vieja (el encargo lo prohibe explicitamente).

GUARDAS PROPIAS, ademas de las de REGIMEN B: los dieciseis nodos existen y
estan VIVOS; ningun otro campo de ningun nodo cambia; las condiciones viejas
quedan intactas y en su orden; la condicion nueva es identica en los
dieciseis; cero guiones largos y cero guiones medios en el texto nuevo.

MODOS: --simular (por defecto, cero escrituras) y --ejecutar.
--mutacion-negativa fuerza la nomina a incluir un nodo DEPRECADO
(elaboracion_fdd) para probar que la guarda aborta SIN ESCRIBIR.

Uso:
  python scripts/loop/vuelta128_ops10_tramo2_reencuadre.py
  python scripts/loop/vuelta128_ops10_tramo2_reencuadre.py --ejecutar
  python scripts/loop/vuelta128_ops10_tramo2_reencuadre.py --mutacion-negativa
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")

TRAMO = [
    "eleccion_abogado_franquicias",
    "estimacion_inversion_inicial_franquiciador",
    "estructura_proveedores_aprobados_designados",
    "exenciones_legales_franquicia",
    "financial_performance_representations",
    "ingresos_por_rebates",
    "los_tres_grandes_criterios",
    "multiples_compradores_influyentes",
    "obtencion_marca_registrada",
    "preparar_fdd",
    "proceso_venta_franquicias",
    "programas_compra_franquicia",
    "propuesta_valor_franquicia",
    "proteccion_propiedad_intelectual_franq",
    "registro_estatal_franquicia",
    "revision_legal_marketing",
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
    print("OP-S-10, TRAMO 2, REENCUADRE DE MARCO (vuelta 128) . MODO %s" % modo)
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
