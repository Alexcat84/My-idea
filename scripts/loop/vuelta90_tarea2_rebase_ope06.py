# -*- coding: utf-8 -*-
"""vuelta90_tarea2_rebase_ope06.py . VUELTA 90, TAREA 2 (decision del fundador
del 29 ago 2026, TAREA 2 de docs/loop/paradas/2026-08-29-racha-y-escalada-omitida-DECISION.md,
adjudicaciones 4.1 y 4.2 del acta de la vuelta 89).

LA BOLSA V90, A FICHERO PROPIO NUEVO. Parte de
docs/plan/OP_E_06_REBASE_V89.jsonl (117 filas, que NO SE TOCA NI SE BORRA) y
aplica las dos adjudicaciones de la relectura ciega del auditor:

  ENTRA el puesto 530 (estrategia_de_innovacion_de_producto ->
  estrategia_de_innovacion_y_tecnologia, adjudicacion 4.1): su frase cita la
  linea entera del paso 3 de la madre, y el criterio que deja dentro a los
  puestos 1169 y 1002 no puede dejarlo fuera. La fila se toma de
  docs/plan/OP_E_06_REBASE_V88.jsonl (129 filas), que es donde vivia antes de
  que la vuelta 89 la sacara.

  SALE el puesto 932 (cumplimiento_magnuson_moss -> mecanismo_resolucion_
  disputas, adjudicacion 4.2): su propia frase nombra a cuatro hermanos de la
  madre y mecanismo_resolucion_disputas no es ninguno de los cuatro.

CIFRA ESPERADA: 117 filas (117 mas el 530 menos el 932), CONJUNTO DISTINTO de
V89 (coincide en el numero, no en el conjunto). Verificado en tiempo de
ejecucion: si la cuenta final no es 117, o si el conjunto de puestos resulta
igual al de V89, el instrumento CAE ROJO (exit 1) y no escribe nada.

NO SE ESCRIBE NINGUNA ARISTA DE OP-E-06 EN ESTE INSTRUMENTO: nunca toca
dataset/nodos ni dataset/metadata. Ese es el trabajo de la TAREA 4.

USO:
  python scripts/loop/vuelta90_tarea2_rebase_ope06.py
"""
import io
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PLAN = os.path.join(RAIZ, "docs", "plan")
V88 = os.path.join(PLAN, "OP_E_06_REBASE_V88.jsonl")
V89 = os.path.join(PLAN, "OP_E_06_REBASE_V89.jsonl")
SALIDA = os.path.join(PLAN, "OP_E_06_REBASE_V90.jsonl")

PUESTO_ENTRA = 530
PUESTO_SALE = 932


def cargar_jsonl(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def main():
    bolsa_v88 = cargar_jsonl(V88)
    bolsa_v89 = cargar_jsonl(V89)
    puestos_v89 = {f["puesto"] for f in bolsa_v89}

    print("=" * 90)
    print("VUELTA 90, TAREA 2: LA BOLSA V90, PARTIENDO DE V89 (%d filas)" % len(bolsa_v89))
    print("=" * 90)

    if PUESTO_SALE not in puestos_v89:
        print("ROJO: el puesto %d (el que tiene que SALIR) no esta en V89: no hay nada que "
              "sacar, revisar la adjudicacion" % PUESTO_SALE)
        return 1
    if PUESTO_ENTRA in puestos_v89:
        print("ROJO: el puesto %d (el que tiene que ENTRAR) YA esta en V89: no hay nada que "
              "anadir, revisar la adjudicacion" % PUESTO_ENTRA)
        return 1

    filas_entra = [f for f in bolsa_v88 if f["puesto"] == PUESTO_ENTRA]
    if len(filas_entra) != 1:
        print("ROJO: el puesto %d aparece %d veces en V88 (se esperaba exactamente 1): no se "
              "toma la fila sin ambiguedad" % (PUESTO_ENTRA, len(filas_entra)))
        return 1
    fila_entra = filas_entra[0]

    bolsa_v90 = [f for f in bolsa_v89 if f["puesto"] != PUESTO_SALE]
    bolsa_v90.append(fila_entra)
    bolsa_v90.sort(key=lambda f: f["puesto"])
    puestos_v90 = {f["puesto"] for f in bolsa_v90}

    print("SALE (adjudicacion 4.2): puesto %d (%s -> %s)" % (
        PUESTO_SALE,
        [f for f in bolsa_v89 if f["puesto"] == PUESTO_SALE][0]["nodo_a"],
        [f for f in bolsa_v89 if f["puesto"] == PUESTO_SALE][0]["nodo_b"]))
    print("ENTRA (adjudicacion 4.1): puesto %d (%s -> %s), tomado de V88" % (
        PUESTO_ENTRA, fila_entra["nodo_a"], fila_entra["nodo_b"]))
    print()

    # VERIFICACION OBLIGATORIA: la cifra tiene que ser 117 y el conjunto tiene
    # que ser DISTINTO del de V89 (coincide en numero, no en conjunto).
    if len(bolsa_v90) != 117:
        print("ROJO: la bolsa V90 tiene %d filas, se esperaban 117. NO SE ESCRIBE NADA."
              % len(bolsa_v90))
        return 1
    if puestos_v90 == puestos_v89:
        print("ROJO: el conjunto de puestos de V90 es IGUAL al de V89: las dos "
              "adjudicaciones no movieron nada. NO SE ESCRIBE NADA.")
        return 1

    diferencia_entra = puestos_v90 - puestos_v89
    diferencia_sale = puestos_v89 - puestos_v90
    if diferencia_entra != {PUESTO_ENTRA} or diferencia_sale != {PUESTO_SALE}:
        print("ROJO: la diferencia de conjuntos no es exactamente {+%d, -%d} (entra %s, sale "
              "%s). NO SE ESCRIBE NADA." % (PUESTO_ENTRA, PUESTO_SALE,
                                             sorted(diferencia_entra), sorted(diferencia_sale)))
        return 1

    with io.open(SALIDA, "w", encoding="utf-8", newline="\n") as fh:
        for f in bolsa_v90:
            fh.write(json.dumps(f, ensure_ascii=False) + "\n")

    print("VERIFICADO: 117 filas, conjunto DISTINTO de V89 (+%d, -%d exactos)."
          % (PUESTO_ENTRA, PUESTO_SALE))
    print("escrito: %s" % SALIDA)
    print()
    print("V88 (129, con el filtro de palabras) y V89 (117, con el criterio de direccion) "
          "SE DEJAN DELANTE, no se tocan. V90 es la bolsa vigente para abrir OP-E-06.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
