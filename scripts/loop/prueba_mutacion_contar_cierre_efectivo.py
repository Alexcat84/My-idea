# -*- coding: utf-8 -*-
r"""prueba_mutacion_contar_cierre_efectivo.py . VUELTA 101, TAREA 1.1: la
prueba de mutacion de scripts/loop/contar_cierre_efectivo.py, RESCRITA EN
RELATIVO (ninguna expectativa es un literal de cifra congelado).

POR QUE SE RESCRIBE (acta de la vuelta 100, seccion 3, "CAIDA DE GUARDA
ENVEJECIDA"). La version de la vuelta 100 congelaba dos literales, "94/89
(48,6%)" y "95/88 (48,1%)": eran el estado de OP-E-03 el dia que esa TAREA
corrio. Las TAREAS 3 y 5 de esa MISMA vuelta 100 anadieron cuatro
`correccion_v100` mas sobre el tramo 4, y el estado de hoy es 90/93 (50,8%):
la prueba quedo EN ROJO PARA SIEMPRE contra su propio remedio, por la peor
via posible (nadie la puede poner verde sin reescribir el numero esperado,
que es borrar la comprobacion). "EL ESTADO AL CIERRE SE MIDE AL CIERRE"
(EJECUTOR.md 1): medir temprano y publicar tarde sin remedir es la misma
especie de caida que citar sin mirar, y una prueba que solo puede estar
verde el dia que nace no es una prueba.

TRES CASOS, LOS MISMOS TRES, ENUNCIADOS CONTRA EL ESTADO REAL DE HOY:
  (a) CONTROL VERDE: el instrumento corre VERDE sobre las filas reales de
      hoy, y su `n` es el que sea (no se supone 183 ni ningun otro numero:
      se lee de la propia salida y se comprueba que sea la suma de los
      cuatro ficheros de tramo).
  (b) QUITAR `correccion_v99` DE LA FILA 147 (mutando una copia temporal,
      el fichero real NO se toca) tiene que MOVER la direccion en
      EXACTAMENTE UNO respecto del control, y en el sentido de MAS
      afirmadas (con_dir sube en 1, sin_dir baja en 1): sea cual sea la
      cifra de partida, sin la correccion del 99 la fila 147 vuelve a
      contar su `direccion_leida` crudo, que es DIRECCION AFIRMADA.
  (c) UN `correccion_vXX` CON `campo_corregido` INVENTADO (mutando la misma
      fila 147 con un campo desconocido) tiene que dar ROJO citandolo.

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


def main():
    salidas = []

    # (a) control verde sobre el estado REAL de hoy, sin suponer ninguna cifra
    d_a, fallos_a = cce.cifras([TRAMO1, TRAMO2, TRAMO3, TRAMO4])
    n_esperado = sum(n for _, n in [(None, len(cargar(r))) for r in
                                     (TRAMO1, TRAMO2, TRAMO3, TRAMO4)])
    ok_a = (not fallos_a and d_a is not None and d_a["n"] == n_esperado
            and d_a["con_dir"] + len(d_a["sin_dir"]) == d_a["n"])
    salidas.append("(a) CONTROL VERDE sobre el estado de hoy (sin cifra congelada):")
    if d_a is None:
        salidas.append("    ROJO: %s" % "; ".join(fallos_a))
    else:
        pct = 100.0 * len(d_a["sin_dir"]) / d_a["n"]
        salidas.append("    n=%d (esperado por suma de los 4 ficheros: %d), clase A %d B %d C %d D %d, "
                       "direccion %d/%d (%s%%)"
                       % (d_a["n"], n_esperado, d_a["clases"]["A"], d_a["clases"]["B"],
                          d_a["clases"]["C"], d_a["clases"]["D"], d_a["con_dir"],
                          len(d_a["sin_dir"]), ("%.1f" % pct).replace(".", ",")))
    salidas.append("    ESPERADO: VERDE, n == suma de los 4 ficheros, con_dir + sin_dir == n")
    salidas.append("    %s" % ("PASA" if ok_a else "FALLA"))
    salidas.append("")

    # (b) quitar correccion_v99 del 147: tiene que mover la direccion en
    # EXACTAMENTE UNO respecto del control (a), hacia MAS afirmadas.
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
        d_b, fallos_b = cce.cifras([TRAMO1, TRAMO2, ruta_b, TRAMO4])
    finally:
        os.remove(ruta_b)
    ok_b = False
    if d_a is not None and d_b is not None and not fallos_b:
        delta_con_dir = d_b["con_dir"] - d_a["con_dir"]
        delta_sin_dir = len(d_b["sin_dir"]) - len(d_a["sin_dir"])
        ok_b = (d_b["n"] == d_a["n"] and delta_con_dir == 1 and delta_sin_dir == -1)
    salidas.append("(b) SIN correccion_v99 en el 147 (copia temporal, el fichero real no se toca), "
                   "RESPECTO DEL CONTROL (a):")
    if d_b is None:
        salidas.append("    ROJO: %s" % "; ".join(fallos_b))
    else:
        pct_b = 100.0 * len(d_b["sin_dir"]) / d_b["n"]
        salidas.append("    n=%d, direccion %d/%d (%s%%); delta con_dir=%+d, delta sin_dir=%+d"
                       % (d_b["n"], d_b["con_dir"], len(d_b["sin_dir"]),
                          ("%.1f" % pct_b).replace(".", ","),
                          d_b["con_dir"] - d_a["con_dir"], len(d_b["sin_dir"]) - len(d_a["sin_dir"])))
    salidas.append("    ESPERADO: delta con_dir = +1, delta sin_dir = -1 respecto de (a) "
                   "(la fila 147 vuelve a DIRECCION AFIRMADA sin la correccion del 99)")
    salidas.append("    %s" % ("PASA" if ok_b else "FALLA"))
    salidas.append("")

    # (c) campo_corregido inventado: ROJO, sin importar el estado de las cifras.
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
        d_c, fallos_c = cce.cifras([TRAMO1, TRAMO2, ruta_c, TRAMO4])
    finally:
        os.remove(ruta_c)
    ok_c = (d_c is None and any("titulo_ratio" in x and "DESCONOCIDO" in x for x in fallos_c))
    salidas.append("(c) correccion_vXX con campo_corregido inventado ('titulo_ratio'):")
    if d_c is None:
        salidas.append("    ROJO:")
        for x in fallos_c:
            salidas.append("       %s" % x)
    else:
        salidas.append("    (no debio dar VERDE)")
    salidas.append("    ESPERADO: ROJO citando 'titulo_ratio' como DESCONOCIDO")
    salidas.append("    %s" % ("PASA" if ok_c else "FALLA"))
    salidas.append("")

    todo_ok = ok_a and ok_b and ok_c
    salidas.append("RESULTADO GLOBAL: %s" % ("TODOS PASAN" if todo_ok else "HAY FALLOS"))

    print("\n".join(salidas))
    return 0 if todo_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
