# -*- coding: utf-8 -*-
"""vuelta103_tarea4_registro_ope03.py . VUELTA 103, TAREA 4: registro aditivo
en `docs/plan/OPERACIONES.jsonl` (nota de `OP-E-03`) de la relectura ciega al
doble del tramo 1 por el centro del `titulo_ratio`, que movio el puesto 31 y
la cifra de cierre de OP-E-03 de 88/95 (51,9%) a 87/96 (52,5% NO RESUELTA).

QUE HACE: anade (NUNCA borra ni sobreescribe) una nota al final del campo
`nota` de `OP-E-03`. NO TOCA `estado`. NO escribe ni retira ninguna arista.

USO:
  python scripts/loop/vuelta103_tarea4_registro_ope03.py --simular
  python scripts/loop/vuelta103_tarea4_registro_ope03.py --aplicar
"""
import argparse
import difflib
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")

MARCA = "REGISTRO ADITIVO, VUELTA 103 TAREA 4 (relectura ciega por el centro, puesto 31)"

NOTA = (
    " | %s: RELECTURA AL DOBLE DEL TRAMO 1 POR EL CENTRO DEL titulo_ratio (8 "
    "puestos: 13, 19, 10, 31, 15, 36, 35, 32, excluidos el 5, los ocho de la "
    "TAREA 3 de la vuelta 102 y el 28/40 de la TAREA 2 de esta vuelta), a "
    "ciegas con `scripts/loop/vuelta103_tarea4_relectura_ciega_centro.py`. 7 "
    "de 8 coincidieron con el registro. EL 31 (`control_estadistico_del_"
    "proceso` contra `causas_comunes_vs_especiales`) discrepo: nueve de los "
    "quince pasos del hijo (comunicacion sin culpa, moral del equipo, "
    "colaboracion entre turnos) son territorio que la madre no tiene en "
    "ningun paso, y el hijo cubre dos pasos distintos de la madre (el 3 y el "
    "6), exceso de genero de la misma especie que movio los pares 172 y 161. "
    "`correccion_v103` en `docs/plan/OP_E_03_LECTURA_TRAMO1_V96.jsonl`, "
    "puesto 31, campo `direccion_leida` a null; clase D no cambia. Recontado "
    "con `scripts/loop/contar_cierre_efectivo.py` "
    "(`docs/loop/SALIDA_V103_TAREA4_CIERRE_EFECTIVO.txt`): clase A 3, B 2, C "
    "1 (par 111), D 177; direccion leida y afirmada 87, NO RESUELTA 96 "
    "(52,5%%); invertidas 2 (pares 16, 114). LA CIFRA VIGENTE ES 87 / 96 "
    "(52,5%%). REGISTRO Y JUICIO, NO CIRUGIA: `estado` no se toca, no se "
    "escribe ni retira ninguna arista."
) % MARCA


def cargar(fallos):
    if not os.path.exists(RUTA):
        fallos.append("no existe %s" % RUTA)
        return None
    filas = []
    with io.open(RUTA, encoding="utf-8") as f:
        for linea in f:
            if linea.strip():
                filas.append(json.loads(linea))
    return filas


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--simular", action="store_true")
    g.add_argument("--aplicar", action="store_true")
    a = ap.parse_args()

    fallos = []
    texto_antes = io.open(RUTA, encoding="utf-8").read()
    filas = cargar(fallos)
    if fallos:
        print("ROJO, %d cosa(s) no cuadran y NO SE ESCRIBE NADA:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1

    objetivo = None
    for f in filas:
        if f.get("id_op") == "OP-E-03":
            objetivo = f
            break

    if objetivo is None:
        fallos.append("OP-E-03 no existe en OPERACIONES.jsonl")
    elif MARCA in (objetivo.get("nota") or ""):
        fallos.append("OP-E-03 ya trae esta nota (no se duplica)")

    if fallos:
        print("ROJO, %d cosa(s) no cuadran y NO SE ESCRIBE NADA:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1

    print("=" * 100)
    print("REGISTRO ADITIVO DE OP-E-03 TAREA 4 (%s)" % ("SIMULACION" if a.simular else "APLICADO"))
    print("=" * 100)
    print("OP-E-03: nota ANTES %d caracteres" % len(objetivo.get("nota") or ""))

    if a.simular:
        print()
        print("SIMULACION: no se escribio nada.")
        return 0

    objetivo["nota"] = (objetivo.get("nota") or "") + NOTA

    with io.open(RUTA, "w", encoding="utf-8", newline="\n") as f:
        for fila in filas:
            f.write(json.dumps(fila, ensure_ascii=False) + "\n")

    texto_despues = io.open(RUTA, encoding="utf-8").read()
    ops = difflib.SequenceMatcher(None, texto_antes, texto_despues).get_opcodes()
    hay_borrado = any(tag in ("delete", "replace") for tag, i1, i2, j1, j2 in ops)
    print()
    print("difflib sobre el fichero entero: %d bloques 'equal', %d 'insert', %d 'delete/replace'"
          % (sum(1 for tag, i1, i2, j1, j2 in ops if tag == "equal"),
             sum(1 for tag, i1, i2, j1, j2 in ops if tag == "insert"),
             sum(1 for tag, i1, i2, j1, j2 in ops if tag in ("delete", "replace"))))
    print("ADITIVO CONFIRMADO: cero bloques delete/replace, nada del texto viejo se toco"
          if not hay_borrado else "ATENCION: hay bloques delete/replace, revisar")
    return 1 if hay_borrado else 0


if __name__ == "__main__":
    raise SystemExit(main())
