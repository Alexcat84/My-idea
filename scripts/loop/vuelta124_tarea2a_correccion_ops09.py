# -*- coding: utf-8 -*-
"""vuelta124_tarea2a_correccion_ops09.py . TAREA 2.a de la vuelta 124.

Anade, ADITIVAMENTE, al final del campo "nota" de OP-S-09 en
docs/plan/OPERACIONES.jsonl, la correccion declarada del alcance de la
lectura par a par (acta de la vuelta 123, 4.2 y 3.1): la vuelta 123 leyo 39
pares CONSECUTIVOS por una cifra que el encargo del auditor fijo;
MESA_RACIMOS.md:214 dice "par a par" sin decir consecutivos; los pares del
racimo son 51; los 12 que faltaban se leyeron en la vuelta 124
(SALIDA_V124_OPS09_LECTURA_RESTO.jsonl); los 39 leidos quedan firmes.

No toca ninguna otra linea del fichero. Se mide con git diff --numstat y con
grep -c "^-[^-]" sobre el diff, que tienen que dar 1 linea tocada y CERO
borrados.

USO:
  python scripts/loop/vuelta124_tarea2a_correccion_ops09.py
"""
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")

CORRECCION = (
    " CORRECCION DECLARADA (vuelta 124, TAREA 2.a, acta de la vuelta 123 "
    "secciones 4.2 y 3.1, caida propia del auditor): la lectura par a par de "
    "la vuelta 123 (docs/loop/SALIDA_V123_OPS09_LECTURA.jsonl) cubrio 39 "
    "pares CONSECUTIVOS dentro de cada familia (suma de (n-1) por familia), "
    "cifra que el encargo de esa vuelta fijo; `docs/MESA_RACIMOS.md:214` dice "
    "\"dentro del racimo se lee par a par\" SIN decir consecutivos. Los pares "
    "TOTALES del racimo son 51 (suma de C(n,2) sobre los miembros de cada "
    "familia), medido con codigo propio en "
    "`scripts/loop/vuelta124_tarea2a_contar_pares_racimo.py` "
    "(`docs/loop/SALIDA_V124_TAREA2A_CONTEO_PARES.txt`). Los 12 pares que "
    "faltaban se leyeron en esta misma vuelta, familia por familia, contra "
    "el grafo de HOY: 11 CONTINUA y 1 REPITE (`estrategia_de_innovacion_de_"
    "producto` <-> `estrategia_innovacion_producto`, superviviente "
    "`estrategia_de_innovacion_de_producto`, alias hereda "
    "`estrategia_innovacion_producto`), registrados en "
    "`docs/loop/SALIDA_V124_OPS09_LECTURA_RESTO.jsonl`. Los 39 pares leidos "
    "en la vuelta 123 QUEDAN FIRMES Y NO SE RELEEN. Los 51 pares del racimo "
    "quedan completos, verificado por "
    "`scripts/loop/vuelta124_verificar_51_pares_completos.py` "
    "(`docs/loop/SALIDA_V124_TAREA3A_51_COMPLETOS.txt`)."
)


def main():
    with io.open(RUTA, encoding="utf-8") as f:
        lineas = f.read().split("\n")

    tocada = 0
    for i, linea in enumerate(lineas):
        if not linea.strip():
            continue
        d = json.loads(linea)
        if d.get("id_op") == "OP-S-09":
            if CORRECCION in d["nota"]:
                raise SystemExit("ARNES: la correccion ya esta aplicada, no se duplica")
            d["nota"] = d["nota"] + CORRECCION
            lineas[i] = json.dumps(d, ensure_ascii=False)
            tocada += 1

    if tocada != 1:
        raise SystemExit("ARNES: se esperaba tocar exactamente 1 fila (OP-S-09), se tocaron %d" % tocada)

    with io.open(RUTA, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lineas))
    print("escrito: OP-S-09.nota, +%d caracteres aditivos" % len(CORRECCION))


if __name__ == "__main__":
    main()
