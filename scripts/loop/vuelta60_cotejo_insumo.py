# -*- coding: utf-8 -*-
"""vuelta60_cotejo_insumo.py . COTEJA LA NOMINA FIJADA DE UN TRAMO CONTRA LOS
NODOS DE HOY, ACTO POR ACTO.

POR QUE EXISTE: el dossier y el cuadro de varas de un tramo se miden UNA VEZ y
se FIJAN, y el encargo prohibe re-medirlos. Pero entre aquella medicion y hoy
puede haberse fundido un lote del mismo tramo, y una fusion CAMBIA los pasos del
superviviente. Un plan que reparte piezas contra indices viejos reparte contra
un nodo que ya no existe. Esto NO re-mide el insumo: lo COTEJA, y dice en que
actos el nodo de hoy ya no calza con la foto fijada.

DE SOLO LECTURA ENTERA. Abre los nodos, cuenta e imprime.

QUE IMPRIME POR ACTO: los dos miembros, si alguno esta DEPRECADO, sus pasos y
condiciones contados HOY, y la comparacion contra los conteos del cuadro de
varas fijado. Marca CALZA o NO CALZA, y separa los actos YA FUNDIDOS (con un
miembro deprecado) de los que siguen vivos.

Uso:
  python scripts/loop/vuelta60_cotejo_insumo.py --tramo docs/loop/TRAMO5_V58.jsonl \
      --varas docs/loop/SALIDA_V58_VARAS_TRAMO5.txt --desde 18 --hasta 50
"""
import argparse
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--tramo", required=True)
    p.add_argument("--varas", required=True)
    p.add_argument("--desde", type=int, default=1)
    p.add_argument("--hasta", type=int, default=10**6)
    a = p.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    filas = [json.loads(l) for l in io.open(os.path.join(RAIZ, a.tramo), encoding="utf-8") if l.strip()]
    claves = sorted({k for k in filas[0] if k.startswith("orden_tramo")})
    if len(claves) != 1:
        print("ROJO: %d claves de ordinal" % len(claves))
        return 1
    ORD = claves[0]

    # El cuadro de varas fijado, leido de su propia salida y no reescrito.
    varas = {}
    for linea in io.open(os.path.join(RAIZ, a.varas), encoding="utf-8"):
        m = re.match(r"\s{2}(\d+)\s+(\S+)\s+(\S+)\s+(\d+)/(\d+)", linea)
        if m:
            varas[int(m.group(1))] = (m.group(2), m.group(3), int(m.group(4)), int(m.group(5)))

    print("=" * 94)
    print("COTEJO DEL INSUMO FIJADO CONTRA LOS NODOS DE HOY")
    print("  nomina: %s | cuadro de varas: %s" % (a.tramo, a.varas))
    print("=" * 94)
    print()

    vivos, fundidos, descalces = 0, 0, 0
    for r in sorted(filas, key=lambda x: x[ORD]):
        n = r[ORD]
        if not (a.desde <= n <= a.hasta):
            continue
        mi = sorted(r["miembros"])
        datos = []
        for x in mi:
            ruta = os.path.join(NODOS, x + ".json")
            if not os.path.exists(ruta):
                datos.append((x, None, None, "NO EXISTE"))
                continue
            o = json.load(io.open(ruta, encoding="utf-8"))
            datos.append((x, len(o.get("pasos_accionables") or []),
                          len(o.get("condiciones_activacion") or []),
                          "DEPRECADO" if o.get("deprecado") else "vivo"))
        estado = "FUNDIDO YA" if any(d[3] != "vivo" for d in datos) else "VIVO"
        if estado == "VIVO":
            vivos += 1
        else:
            fundidos += 1
        v = varas.get(n)
        veredicto = "sin fila en el cuadro"
        if v and estado == "VIVO":
            # el cuadro imprime los miembros en orden alfabetico, igual que mi
            esperado = (v[2], v[3])
            medido = (datos[0][1], datos[1][1])
            ok_nombres = (v[0] == mi[0] and v[1] == mi[1])
            veredicto = ("CALZA" if (esperado == medido and ok_nombres) else "NO CALZA")
            if veredicto == "NO CALZA":
                descalces += 1
        print("  acto %-3d %-9s %-46s %s" % (n, estado, mi[0], mi[1]))
        print("           hoy: pasos %s/%s  cond %s/%s  estado %s/%s | cuadro fijado: pasos %s/%s | %s"
              % (datos[0][1], datos[1][1], datos[0][2], datos[1][2],
                 datos[0][3], datos[1][3],
                 v[2] if v else "?", v[3] if v else "?", veredicto))
    print()
    print("  RESUMEN: actos mirados %d | VIVOS %d | ya fundidos %d | DESCALCES %d"
          % (vivos + fundidos, vivos, fundidos, descalces))
    if descalces:
        print("  ROJO: hay actos vivos cuyo nodo de hoy no calza con la foto fijada.")
        return 1
    print("  VERDE: todos los actos vivos calzan con la foto fijada.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
