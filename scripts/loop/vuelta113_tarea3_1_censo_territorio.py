# -*- coding: utf-8 -*-
"""vuelta113_tarea3_1_censo_territorio.py . TAREA 3.1 de la vuelta 113:
RECUENTA, ANTES DE LEER, el territorio viejo (las NO RESUELTA que quedaron
sin leer del lote de 80 de la vuelta 112) y el territorio nuevo (las filas
cuya direccion en base fue ANULADA a None por una correccion_vNN declarada).

Replica, en su propia logica de solo lectura, el mismo criterio de
resolucion de correcciones que contar_cierre_efectivo.py (la mas reciente
correccion_vNN, por numero ascendente, que declare campo_corregido ==
"direccion_leida" manda sobre el valor crudo).

USO:
  python scripts/loop/vuelta113_tarea3_1_censo_territorio.py
"""
import io
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TRAMOS = [
    os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO1_V96.jsonl"),
    os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO2_V97.jsonl"),
    os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO3_V98.jsonl"),
    os.path.join(RAIZ, "docs", "plan", "OP_E_03_LECTURA_TRAMO4_V99.jsonl"),
]
CORREC_RE = re.compile(r"^correccion_v(\d+)$")

# el lote de 80 leidos enteros de la vuelta 112 (SALIDA_V112_TAREA3_1_CENSO_88.txt
# y el reporte 112: "los 8 que quedan para la vuelta 113: 168, 170, 171, 173,
# 176, 178, 181, 183" son los NO cubiertos por ese lote).
LOTE_80_V112_YA_LEIDOS = None  # se calcula: 88 nunca reabiertas menos los 8 declarados


def cargar():
    filas = []
    for ruta in TRAMOS:
        with io.open(ruta, encoding="utf-8") as f:
            filas.extend(json.loads(l) for l in f if l.strip())
    return filas


def correcciones_ordenadas(fila):
    claves = [(int(m.group(1)), k) for k in fila for m in [CORREC_RE.match(k)] if m]
    claves.sort()
    return [(n, fila[k]) for n, k in claves]


def direccion_final_y_origen(fila):
    """Devuelve (direccion_final, num_correccion_que_la_fijo_o_None,
    tiene_alguna_correccion_de_direccion)."""
    actual = fila.get("direccion_leida")
    num_ultima = None
    hubo_correccion_direccion = False
    for num, c in correcciones_ordenadas(fila):
        if c.get("campo_corregido") == "direccion_leida":
            actual = c.get("valor_nuevo")
            num_ultima = num
            hubo_correccion_direccion = True
    return actual, num_ultima, hubo_correccion_direccion


def main():
    filas = cargar()
    no_resuelta = []          # direccion_final es None/vacia
    nunca_reabiertas = []     # NO_RESUELTA sin ninguna correccion sobre direccion_leida
    anuladas_por_correccion = []  # NO_RESUELTA CON correccion que la puso en None
    con_correccion_que_no_anula = []  # tiene correccion_vNN pero no es del tipo "anula direccion"

    for fila in filas:
        puesto = fila["puesto_tramo"]
        direccion_final, num_correccion, hubo_correccion_direccion = direccion_final_y_origen(fila)
        es_no_resuelta = not direccion_final
        tiene_alguna_correccion = bool(correcciones_ordenadas(fila))

        if es_no_resuelta:
            no_resuelta.append(puesto)
            if hubo_correccion_direccion:
                anuladas_por_correccion.append(puesto)
            else:
                nunca_reabiertas.append(puesto)
        elif tiene_alguna_correccion:
            con_correccion_que_no_anula.append(puesto)

    print("FILAS TOTALES: %d" % len(filas))
    print("NO RESUELTA (direccion final vacia): %d" % len(no_resuelta))
    print("  nunca reabiertas (sin correccion_vNN sobre direccion_leida): %d" % len(nunca_reabiertas))
    print("  anuladas a None por correccion_vNN declarada: %d" % len(anuladas_por_correccion))
    print("  suma %d + %d == %d NO RESUELTA: %s"
          % (len(nunca_reabiertas), len(anuladas_por_correccion), len(no_resuelta),
             "CUADRA" if len(nunca_reabiertas) + len(anuladas_por_correccion) == len(no_resuelta) else "NO CUADRA"))
    print()
    print("nunca reabiertas, lista completa (%d): %s" % (len(nunca_reabiertas), nunca_reabiertas))
    print()
    print("anuladas por correccion, lista completa (%d): %s" % (len(anuladas_por_correccion), anuladas_por_correccion))
    print()
    print("con correccion_vNN que NO anula la direccion (fuera de este territorio) (%d): %s"
          % (len(con_correccion_que_no_anula), con_correccion_que_no_anula))

    ya_leidos_112 = [p for p in nunca_reabiertas if p not in
                     (168, 170, 171, 173, 176, 178, 181, 183)]
    print()
    print("de las 'nunca reabiertas', las que YA se leyeron en el lote de 80 de la vuelta 112: %d"
          % len(ya_leidos_112))
    faltan = [p for p in nunca_reabiertas if p in (168, 170, 171, 173, 176, 178, 181, 183)]
    print("las que quedan del territorio viejo (deberian ser 168,170,171,173,176,178,181,183): %s" % faltan)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
