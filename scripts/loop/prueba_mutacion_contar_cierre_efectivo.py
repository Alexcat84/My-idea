# -*- coding: utf-8 -*-
r"""prueba_mutacion_contar_cierre_efectivo.py . VUELTA 100, TAREA 1, PUNTO 1.3:
la prueba de mutacion de scripts/loop/contar_cierre_efectivo.py, con su
fichero de salida commiteado (docs/loop/SALIDA_V100_TAREA1_MUTACION.txt).

TRES CASOS, NINGUNO SUPUESTO:
  (a) CONTROL VERDE sobre las 183 reales: tiene que dar A 3, B 2, C 1, D 177
      y direccion 94 / 89 (48,6%).
  (b) QUITAR `correccion_v99` DE LA FILA 147 (mutando una copia temporal de
      TRAMO3_V98.jsonl, el fichero real NO se toca) tiene que devolver
      95 / 88: eso prueba que el instrumento SI estaba aplicando la
      correccion de verdad, porque sin ella vuelve al crudo de la vuelta 99.
  (c) UN `correccion_vXX` CON `campo_corregido` INVENTADO (mutando la misma
      fila 147 con un campo desconocido) tiene que dar ROJO por la guarda de
      1.2: ninguna cifra se escribe.

USO:
  python scripts/loop/prueba_mutacion_contar_cierre_efectivo.py
"""
import copy
import importlib.util
import io
import json
import os
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MODULO_RUTA = os.path.join(RAIZ, "scripts", "loop", "contar_cierre_efectivo.py")
TRAMO3 = os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO3_V98.jsonl")
TRAMO1 = os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO1_V96.jsonl")
TRAMO2 = os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO2_V97.jsonl")
TRAMO4 = os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO4_V99.jsonl")

spec = importlib.util.spec_from_file_location("contar_cierre_efectivo", MODULO_RUTA)
cce = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cce)


def cargar(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def escribir_tmp(filas):
    fd, ruta = tempfile.mkstemp(suffix=".jsonl")
    os.close(fd)
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        for fila in filas:
            f.write(json.dumps(fila, ensure_ascii=False) + "\n")
    return ruta


def resultado_texto(rutas):
    d, fallos = cce.cifras(rutas)
    if fallos:
        return "ROJO:\n" + "\n".join("   %s" % x for x in fallos)
    pct = 100.0 * len(d["sin_dir"]) / d["n"]
    return ("VERDE: n=%d clase A %d B %d C %d D %d, direccion %d/%d (%s%%)"
            % (d["n"], d["clases"]["A"], d["clases"]["B"], d["clases"]["C"],
               d["clases"]["D"], d["con_dir"], len(d["sin_dir"]),
               ("%.1f" % pct).replace(".", ",")))


def main():
    salidas = []

    # (a) control verde
    r_a = resultado_texto([TRAMO1, TRAMO2, TRAMO3, TRAMO4])
    ok_a = r_a == "VERDE: n=183 clase A 3 B 2 C 1 D 177, direccion 94/89 (48,6%)"
    salidas.append("(a) CONTROL VERDE, 183 reales:")
    salidas.append("    %s" % r_a)
    salidas.append("    ESPERADO: VERDE: n=183 clase A 3 B 2 C 1 D 177, direccion 94/89 (48,6%)")
    salidas.append("    %s" % ("PASA" if ok_a else "FALLA"))
    salidas.append("")

    # (b) quitar correccion_v99 del 147
    filas3 = cargar(TRAMO3)
    filas3_b = copy.deepcopy(filas3)
    tocado = False
    for f in filas3_b:
        if f.get("puesto_tramo") == 147:
            f.pop("correccion_v99", None)
            tocado = True
    assert tocado, "la fila 147 no aparecio en TRAMO3_V98.jsonl"
    ruta_b = escribir_tmp(filas3_b)
    try:
        r_b = resultado_texto([TRAMO1, TRAMO2, ruta_b, TRAMO4])
    finally:
        os.remove(ruta_b)
    ok_b = r_b == "VERDE: n=183 clase A 3 B 2 C 1 D 177, direccion 95/88 (48,1%)"
    salidas.append("(b) SIN correccion_v99 en el 147 (copia temporal, el fichero real no se toca):")
    salidas.append("    %s" % r_b)
    salidas.append("    ESPERADO: VERDE: n=183 clase A 3 B 2 C 1 D 177, direccion 95/88 (48,1%)")
    salidas.append("    %s" % ("PASA" if ok_b else "FALLA"))
    salidas.append("")

    # (c) campo_corregido inventado
    filas3_c = copy.deepcopy(filas3)
    tocado = False
    for f in filas3_c:
        if f.get("puesto_tramo") == 147:
            f["correccion_v99"] = dict(f["correccion_v99"])
            f["correccion_v99"]["campo_corregido"] = "titulo_ratio"
            tocado = True
    assert tocado, "la fila 147 no aparecio en TRAMO3_V98.jsonl"
    ruta_c = escribir_tmp(filas3_c)
    try:
        r_c = resultado_texto([TRAMO1, TRAMO2, ruta_c, TRAMO4])
    finally:
        os.remove(ruta_c)
    ok_c = r_c.startswith("ROJO:") and "titulo_ratio" in r_c and "DESCONOCIDO" in r_c
    salidas.append("(c) correccion_vXX con campo_corregido inventado ('titulo_ratio'):")
    salidas.append("    %s" % r_c)
    salidas.append("    ESPERADO: ROJO citando 'titulo_ratio' como DESCONOCIDO")
    salidas.append("    %s" % ("PASA" if ok_c else "FALLA"))
    salidas.append("")

    todo_ok = ok_a and ok_b and ok_c
    salidas.append("RESULTADO GLOBAL: %s" % ("TODOS PASAN" if todo_ok else "HAY FALLOS"))

    print("\n".join(salidas))
    return 0 if todo_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
