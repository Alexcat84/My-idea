# -*- coding: utf-8 -*-
r"""vuelta106_tarea4_1_censo.py . VUELTA 106, TAREA 4.1: EL LOTE DE LOS
TRAMOS 3 Y 4, CONTADO HOY.

Cuenta, sobre docs/plan/OP_E_03_LECTURA_TRAMO{3,4}_V9{8,9}.jsonl, las filas
RESUELTA (direccion_leida efectiva, tras aplicar correccion_vNN si la hay,
distinta de null) que NO tienen ni correccion_vNN ni relectura registrada en
docs/loop/CENSO_RELECTURAS_OP_E_03.jsonl (veces_releido == 0). Esas son las
que la pregunta de tres vias todavia no ha tocado.

USO:
  python scripts/loop/vuelta106_tarea4_1_censo.py
"""
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TRAMOS = {
    3: os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO3_V98.jsonl"),
    4: os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO4_V99.jsonl"),
}
CENSO = os.path.join(RAIZ, "docs", "loop", "CENSO_RELECTURAS_OP_E_03.jsonl")

CORREC_RE = re.compile(r"^correccion_v(\d+)$")


def cargar(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def correcciones_ordenadas(fila):
    claves = [(int(m.group(1)), k) for k in fila for m in [CORREC_RE.match(k)] if m]
    claves.sort()
    return [fila[k] for _, k in claves]


def valor_efectivo(fila, campo):
    valor = fila.get(campo)
    for c in correcciones_ordenadas(fila):
        if c.get("campo_corregido") == campo:
            valor = c.get("valor_nuevo")
    return valor


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    censo = {f["puesto_tramo"]: f for f in cargar(CENSO)}

    resultado = {}
    for t, ruta in TRAMOS.items():
        filas = []
        for f in cargar(ruta):
            p = f["puesto_tramo"]
            dir_ef = valor_efectivo(f, "direccion_leida")
            if not dir_ef:
                continue
            tiene_correccion = len(correcciones_ordenadas(f)) > 0
            c = censo.get(p)
            releido = c["veces_releido"] if c else None
            filas.append({"puesto": p, "madre": f["madre_de_la_bolsa"], "hijo": f["hijo_de_la_bolsa"],
                         "paso_casado": f["paso_casado"], "tiene_correccion": tiene_correccion,
                         "veces_releido": releido})
        resultado[t] = filas

    print("=" * 100)
    print("VUELTA 106, TAREA 4.1: EL LOTE DE LOS TRAMOS 3 Y 4, CONTADO HOY")
    print("=" * 100)
    total_resuelta = 0
    total_sin_tocar = 0
    for t in (3, 4):
        filas = resultado[t]
        total_resuelta += len(filas)
        sin_tocar = [f for f in filas if not f["tiene_correccion"] and f["veces_releido"] == 0]
        con_correccion = [f for f in filas if f["tiene_correccion"]]
        total_sin_tocar += len(sin_tocar)
        print()
        print("tramo%d: %d RESUELTA -- puestos %s" % (t, len(filas), [f["puesto"] for f in filas]))
        print("  sin correccion ni relectura (%d): %s" % (len(sin_tocar), [f["puesto"] for f in sin_tocar]))
        print("  con correccion ya declarada (%d): %s" % (len(con_correccion), [f["puesto"] for f in con_correccion]))
    print()
    print("TOTAL RESUELTA tramo3+tramo4: %d" % total_resuelta)
    print("TOTAL sin correccion ni relectura: %d" % total_sin_tocar)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
