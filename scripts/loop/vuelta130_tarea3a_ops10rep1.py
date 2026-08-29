# -*- coding: utf-8 -*-
"""vuelta130_tarea3a_ops10rep1.py . EL NODO QUE LE FALTA A OP-S-10 (TAREA 3.a
de la vuelta 130, <OP> = OPS10REP1): antepone la misma condicion de
activacion que nombra el pais (Estados Unidos) al UNICO nodo VIVO de la
nomina de 31 que quedaba sin cubrir tras los tramos 1 y 2 de las vueltas 126
y 128.

MEDIDO EN ESTA VUELTA (scripts/loop/vuelta130_tarea3a_medir_nomina_ops10.py):
los 31 ids de la nomina resuelven (P.1) a 29 vivos distintos (el resolutor
mueve tres: cinco_categorias_costos_franquicia ->
estimacion_inversion_inicial_franquiciador, elaboracion_fdd -> preparar_fdd,
estructuras_combinadas_franquicia -> prevenir_franquicias_inadvertidas); de
esos 29, 28 ya nombran el pais en condiciones_activacion (los dos
contramodelos mas los 26 escritos en las vueltas 126 y 128) y UNO no:
prevenir_franquicias_inadvertidas, superviviente de
estructuras_combinadas_franquicia, con sus cuatro condiciones viejas y
ninguna nombrando el pais.

MISMA FORMA LITERAL, sin cambios: "Solo aplica si vendes o piensas vender
franquicias en Estados Unidos", antepuesta (posicion 0 de
condiciones_activacion); las cuatro condiciones viejas quedan enteras, en su
orden, DETRAS de la nueva.

CONTENIDO LEIDO ANTES DE ESCRIBIR (regla del encargo): el resumen_teorico
habla de "leyes estatales de franquicia" y los pasos_accionables mandan
"Verificar los umbrales de tarifas y las definiciones especificas de
franquicia en cada estado donde operes o planees operar": el mismo patron de
"estado" que ya sostiene la condicion en registro_estatal_franquicia (donde
"estado" es un estado de EE.UU.). Sus nodos_siguientes incluyen
cumplimiento_ftc_rule_436 (la FTC es la agencia federal de EE.UU.). El
contenido SI sostiene la condicion.

GUARDAS PROPIAS, ademas de las de REGIMEN B: el nodo existe y esta VIVO;
ningun otro campo cambia; las condiciones viejas quedan intactas y en su
orden; cero guiones largos y cero guiones medios en el texto nuevo.

MODOS: --simular (por defecto, cero escrituras) y --ejecutar.
--mutacion-negativa apunta a un nodo DEPRECADO (elaboracion_fdd) para probar
que la guarda aborta SIN ESCRIBIR.

Uso:
  python scripts/loop/vuelta130_tarea3a_ops10rep1.py
  python scripts/loop/vuelta130_tarea3a_ops10rep1.py --ejecutar
  python scripts/loop/vuelta130_tarea3a_ops10rep1.py --mutacion-negativa
"""
import argparse
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")

NODO = "prevenir_franquicias_inadvertidas"
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
                     help="apunta a un nodo DEPRECADO, para probar que la guarda aborta")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    nid = "elaboracion_fdd" if a.mutacion_negativa else NODO

    modo = "MUTACION NEGATIVA (nunca escribe)" if a.mutacion_negativa else ("EJECUTAR" if a.ejecutar else "SIMULAR")
    print("=" * 78)
    print("OP-S-10, OPS10REP1, EL NODO QUE FALTABA (vuelta 130) . MODO %s" % modo)
    print("=" * 78)

    if "—" in CONDICION_NUEVA or "–" in CONDICION_NUEVA or " - " in CONDICION_NUEVA:
        print("SE ABORTA SIN ESCRIBIR: la condicion nueva lleva guion largo o medio.")
        return 1

    fallos = []
    try:
        d, c = leer_crudo(nid)
    except IOError as e:
        fallos.append("%s no se pudo leer: %s" % (nid, e))
        d, c = None, None

    if d is not None and d.get("deprecado"):
        fallos.append("%s esta DEPRECADO" % nid)

    print("guarda 1, el nodo existe y esta VIVO: %s" % ("OK" if not fallos else "ROJO %s" % fallos))
    if fallos:
        print()
        print("SE ABORTA SIN ESCRIBIR, %d fallo(s):" % len(fallos))
        for f in fallos:
            print("  [ROJO] %s" % f)
        return 1

    ya_puesta = (d.get("condiciones_activacion") or [None])[:1] == [CONDICION_NUEVA]
    print("guarda 2, la condicion NO estaba puesta todavia: %s" % ("OK" if not ya_puesta else "ROJO"))
    if ya_puesta:
        fallos.append("la condicion YA esta puesta")
        print()
        print("SE ABORTA SIN ESCRIBIR, %d fallo(s):" % len(fallos))
        for f in fallos:
            print("  [ROJO] %s" % f)
        return 1

    orig = json.loads(json.dumps(d))
    cond = list(d.get("condiciones_activacion") or [])
    d["condiciones_activacion"] = [CONDICION_NUEVA] + cond

    rotos_otros_campos = [k for k in d if k != "condiciones_activacion" and d[k] != orig.get(k)]
    vieja = orig.get("condiciones_activacion") or []
    nueva_cola = d["condiciones_activacion"][1:]
    roto_orden_viejo = nueva_cola != vieja

    print("guarda 3, ningun otro campo cambia: %s" % ("OK" if not rotos_otros_campos else "ROJO %s" % rotos_otros_campos))
    print("guarda 4, las condiciones viejas quedan intactas y en su orden: %s"
          % ("OK" if not roto_orden_viejo else "ROJO"))
    if rotos_otros_campos or roto_orden_viejo:
        fallos.append("guarda 3/4 caida")

    if fallos:
        print()
        print("SE ABORTA SIN ESCRIBIR, %d fallo(s):" % len(fallos))
        for f in fallos:
            print("  [ROJO] %s" % f)
        return 1

    print()
    print("%s.condiciones_activacion: %s" % (nid, json.dumps(d["condiciones_activacion"], ensure_ascii=False)))

    if a.mutacion_negativa:
        print()
        print("MUTACION NEGATIVA: no debia llegar aqui con un nodo DEPRECADO. CAIDA DE LA ARNES.")
        return 1

    if not a.ejecutar:
        print()
        print("SIMULACION: cero escrituras.")
        return 0

    escribir(nid, d, c)
    print()
    print("ESCRITO. ficheros tocados: 1")
    return 0


if __name__ == "__main__":
    sys.exit(main())
