# -*- coding: utf-8 -*-
"""vuelta102_tarea4_registro_fase0.py . VUELTA 102, TAREA 4: EL REGISTRO
ADITIVO DE LA ADJUDICACION DE LA FASE 0 DEL AUDITOR (acta de la vuelta 101,
secciones 5.1 a 5.3).

QUE HACE: anade (NUNCA borra ni sobreescribe) una nota al final del campo
`nota` de `OP-E-01` y `OP-E-03` en `docs/plan/OPERACIONES.jsonl`, registrando
que la fase 04 queda en 1 HECHA (`OP-E-02`), 2 EJECUTABLES (`OP-E-01`,
`OP-E-03`) y 7 BLOQUEADAS, por la adjudicacion del auditor (acta 101, 5.1 a
5.3): las seis operaciones de codigo y saneo de la fase 0 estan EJECUTADAS Y
NO BLOQUEAN, medido por el codigo y el dato vivos (no por el commit ni por
`estado`), y esa medicion cubre por extension `AUDITOR.md` preambulo ("el
estado de verdad es el repo") mas el acta 100 4.2 ("una dependencia con
registro de cierre escrito NO bloquea aunque su campo diga LISTA").

NO TOCA `estado`: sigue sin voto en la aritmetica de dependencias (acta 100
4.2, doctrina vigente). NO escribe ni retira ninguna arista.

USO:
  python scripts/loop/vuelta102_tarea4_registro_fase0.py --simular
  python scripts/loop/vuelta102_tarea4_registro_fase0.py --aplicar

MECANICA DE ROJO: si `OP-E-01` u `OP-E-03` no existen en OPERACIONES.jsonl,
o si ya tienen esta misma nota (para no duplicarla si se corre dos veces),
no se escribe nada y sale con exit 1.
"""
import argparse
import difflib
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")

MARCA = "REGISTRO ADITIVO, VUELTA 102 TAREA 4 (acta de la vuelta 101, 5.1 a 5.3)"

NOTA_COMUN = (
    " | %s: LA FASE 04 QUEDA EN 1 HECHA (OP-E-02), 2 EJECUTABLES (OP-E-01, "
    "OP-E-03) Y 7 BLOQUEADAS (OP-M-03-ENLACES, OP-E-04, OP-E-05, "
    "OP-M-01-ESLABONES, OP-M-01-SEXTO, OP-E-06, OP-E-07), por la adjudicacion "
    "del auditor: LAS SEIS OPERACIONES DE CODIGO Y SANEO DE LA FASE 0 "
    "(OP-C-01, OP-C-02, OP-C-03, OP-C-04, OP-S-06, OP-S-07) ESTAN EJECUTADAS Y "
    "NO BLOQUEAN, medido por el CODIGO Y EL DATO de hoy (no por el commit ni "
    "por `estado`), cubierto por AUDITOR.md preambulo (\"el estado de verdad "
    "es el repo, no tu memoria\") mas el acta 100 4.2 (\"una dependencia con "
    "registro de cierre escrito NO bloquea aunque su campo diga LISTA\"). Las "
    "siete BLOQUEADAS esperan OP-M-01 y OP-M-03 (dos mesas de la fase 06) y "
    "OP-M-01-FUSION y OP-M-03-III (dos fusiones enrutadas a la fase 06 por la "
    "remision del 26 ago 2026), nunca \"cuatro mesas\" (tallar_nombre_de_"
    "operacion.py, docs/loop/SALIDA_V102_TAREA1_2_NOMBRES_FASE04.txt). ESTE "
    "ES UN REGISTRO, NO UNA CIRUGIA: `estado` NO SE TOCA (sigue sin voto en "
    "la aritmetica de dependencias, acta 100 4.2), no se escribe ni retira "
    "ninguna arista, no se abre la fase 05 ni la 06, no se mueve ninguna "
    "operacion de fase. La propia nota de OP-E-03 ya dice que su producto es "
    "el juicio y no el grafo (\"CERO ARISTAS ESCRITAS O RETIRADAS EN TODA LA "
    "OPERACION\"), y ese juicio esta completo, 183 de 183."
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

    objetivo = {}
    for f in filas:
        if f.get("id_op") in ("OP-E-01", "OP-E-03"):
            objetivo[f["id_op"]] = f

    for id_op in ("OP-E-01", "OP-E-03"):
        f = objetivo.get(id_op)
        if f is None:
            fallos.append("%s no existe en OPERACIONES.jsonl" % id_op)
            continue
        if MARCA in (f.get("nota") or ""):
            fallos.append("%s ya trae esta nota (no se duplica)" % id_op)

    if fallos:
        print("ROJO, %d cosa(s) no cuadran y NO SE ESCRIBE NADA:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1

    print("=" * 100)
    print("REGISTRO ADITIVO DE LA FASE 0 (%s)" % ("SIMULACION" if a.simular else "APLICADO"))
    print("=" * 100)
    for id_op in ("OP-E-01", "OP-E-03"):
        print("%s: nota ANTES %d caracteres" % (id_op, len(objetivo[id_op].get("nota") or "")))

    if a.simular:
        print()
        print("SIMULACION: no se escribio nada.")
        return 0

    for id_op in ("OP-E-01", "OP-E-03"):
        objetivo[id_op]["nota"] = (objetivo[id_op].get("nota") or "") + NOTA_COMUN

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
