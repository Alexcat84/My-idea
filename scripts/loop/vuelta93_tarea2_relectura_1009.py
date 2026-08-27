# -*- coding: utf-8 -*-
"""vuelta93_tarea2_relectura_1009.py . VUELTA 93, TAREA 2 (BLOQUEANTE): LA
RELECTURA CONJUNTA DEL PUESTO 1009 DE `OP-E-07`.

POR QUE (acta de la vuelta 92, `docs/loop/ACTA_AUDITOR.md`, seccion 4, lineas
31977 a 32106): el auditor discrepa de su propia adjudicacion de la vuelta 91
sobre el puesto 1009 y manda la relectura a `AUDITOR.md` seccion 1.3
(relectura conjunta), con la decision reservada al ejecutor de esta vuelta.

LA UNICA PREGUNTA QUE `OP-E-07.verificacion` MANDA HACER (docs/plan/
OPERACIONES.jsonl, linea 69): "NO SE RELEE EL PAR: se lee su razon, que ya
esta escrita. Si la razon tampoco lo dice, el par sale de la cosecha y se
anota por que". La pregunta NO es "hay jerarquia posible entre los dos
nodos": es "LA RAZON NOMBRA CUAL DE LOS DOS ES LA MADRE, SI O NO".

ESTE INSTRUMENTO lee la razon COMPLETA de docs/INTRA_DOMINIO_VEREDICTOS.jsonl
para el 1009 y para los dos ejemplares ya adjudicados que sirven de vara
(1083, CONFIRMADO por el acta 91, y 1098, que CAYO en la vuelta 92), y mide
tres cosas, cada una citando la frase literal en la que se apoya:

  1. LA FORMULA CON LA QUE LA RAZON PRESENTA EL "TRAE": la de madre e hijo es
     "trae el procedimiento DE ESA LINEA" o "trae un procedimiento que LA
     MADRE no tiene" (nombra a la madre, literal, como en el 1083); la de la
     clase D es "trae un procedimiento QUE EL OTRO / QUE ESA FASE no tiene"
     (no nombra a la madre, solo se refiere al otro nodo).
  2. SI HAY UNA LINEA NOMBRADA CON SU PASO (numero u ordinal) para alguno de
     los dos nodos, o una formula de indice: la marca positiva que el banco
     9.6.2 exige para reconocer un par madre e hijo (BANCO_DE_TEXTOS.md
     lineas 1771 a 1774, "el hijo cabe entero dentro de UN paso de la
     madre").
  3. SI LA PROPIA RAZON CONTRADICE LA DIRECCION ESCRITA declarando que una
     parte del hijo queda FUERA del solape (lo que el test del punto 2 exige
     que NO pase).

VEREDICTO: si las tres miden en contra de que la razon nombre una madre, el
par SALE por `OP-E-07.verificacion` ("si la razon tampoco lo dice..."), igual
que se hizo con el 1098 en la vuelta 92. ROJO si algun puesto no se puede
leer en `INTRA_DOMINIO_VEREDICTOS.jsonl`.

USO:
  python scripts/loop/vuelta93_tarea2_relectura_1009.py
"""
import io
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VEREDICTOS = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")

FORMULA_MADRE_HIJO_LITERAL = re.compile(r"trae\s+(?:el|un)\s+procedimiento\s+de\s+esa\s+linea", re.IGNORECASE)
NOMBRA_LA_MADRE = re.compile(r"\bla madre\b", re.IGNORECASE)
FORMULA_CLASE_D = re.compile(r"trae\s+un\s+procedimiento\s+que\s+(?:el otro|esa fase)\s+no\s+tiene", re.IGNORECASE)
LINEA_CON_PASO = re.compile(r"(?:paso|pasos)\s+\d|(?:primer|segundo|tercer|cuarto|quinto)\s+paso|dice en su paso", re.IGNORECASE)
FUERA_DEL_SOLAPE = re.compile(r"queda fuera", re.IGNORECASE)


def cargar_veredictos():
    with io.open(VEREDICTOS, encoding="utf-8") as f:
        filas = [json.loads(l) for l in f if l.strip()]
    return {int(v["puesto_intra"]): v for v in filas}


def medir(puesto, razon):
    tiene_formula_madre_hijo = bool(FORMULA_MADRE_HIJO_LITERAL.search(razon))
    nombra_madre = bool(NOMBRA_LA_MADRE.search(razon))
    tiene_formula_d = bool(FORMULA_CLASE_D.search(razon))
    tiene_linea_con_paso = bool(LINEA_CON_PASO.search(razon))
    contradice = bool(FUERA_DEL_SOLAPE.search(razon))
    return {
        "puesto": puesto,
        "formula_madre_hijo_literal": tiene_formula_madre_hijo,
        "nombra_la_madre_literal": nombra_madre,
        "formula_clase_d": tiene_formula_d,
        "tiene_linea_con_paso_numerado": tiene_linea_con_paso,
        "contradice_declarando_fuera_del_solape": contradice,
    }


def main():
    veredictos = cargar_veredictos()
    for p in (1009, 1083, 1098):
        if p not in veredictos:
            print("ROJO: el puesto %d no tiene entrada en %s. NO SE TALLA NADA." % (p, VEREDICTOS))
            return 1

    print("=" * 90)
    print("TAREA 2 (BLOQUEANTE): LA RELECTURA CONJUNTA DEL PUESTO 1009")
    print("=" * 90)
    print()

    for p, etiqueta in ((1083, "VARA: CONFIRMADO por el acta 91 (nombra 'la madre' literal)"),
                       (1098, "VARA: CAYO en la vuelta 92 (formula de clase D, no nombra madre)"),
                       (1009, "EL PUESTO EN DISCREPANCIA")):
        razon = veredictos[p]["razon"]
        m = medir(p, razon)
        print("--- PUESTO %d (%s) ---" % (p, etiqueta))
        print("razon completa:")
        print("  %r" % razon)
        print("medicion: %s" % json.dumps(m, ensure_ascii=False))
        print()

    m1009 = medir(1009, veredictos[1009]["razon"])
    print("=" * 90)
    print("LA PREGUNTA UNICA: LA RAZON DEL 1009 NOMBRA CUAL NODO ES LA MADRE, SI O NO")
    print("=" * 90)
    print("1. usa la formula de madre e hijo ('trae el procedimiento DE ESA LINEA')? %s"
          % m1009["formula_madre_hijo_literal"])
    print("2. nombra 'la madre' literalmente, como el 1083? %s" % m1009["nombra_la_madre_literal"])
    print("3. usa la formula de la clase D ('trae un procedimiento que ESA FASE no tiene',")
    print("   igual en forma a la del 1098, 'que EL OTRO no tiene')? %s" % m1009["formula_clase_d"])
    print("4. hay una linea nombrada con su paso (numero u ordinal) para algun nodo? %s"
          % m1009["tiene_linea_con_paso_numerado"])
    print("5. la propia razon declara que un bloque del hijo queda FUERA del solape")
    print("   (contradice el test del banco 9.6.2, BANCO_DE_TEXTOS.md lineas 1771 a 1774,")
    print("   'el hijo cabe entero dentro de UN paso de la madre')? %s"
          % m1009["contradice_declarando_fuera_del_solape"])
    print()

    respuesta_no_nombra = (not m1009["formula_madre_hijo_literal"]
                           and not m1009["nombra_la_madre_literal"]
                           and m1009["formula_clase_d"]
                           and not m1009["tiene_linea_con_paso_numerado"]
                           and m1009["contradice_declarando_fuera_del_solape"])

    print("=" * 90)
    if respuesta_no_nombra:
        print("VEREDICTO: LA RAZON DEL 1009 NO NOMBRA CUAL NODO ES LA MADRE.")
        print("Se parece al 1098 (formula de clase D, sin linea nombrada, calla la jerarquia)")
        print("y NO se parece al 1083 (que nombra 'la madre' literal).")
        print("Por OP-E-07.verificacion ('si la razon tampoco lo dice, el par sale de la")
        print("cosecha y se anota por que'): EL PAR SALE.")
        return 0
    print("VEREDICTO: LA MEDICION NO CONFIRMA QUE LA RAZON CALLE LA MADRE. REVISAR A MANO")
    print("ANTES DE DECIDIR (esta salida no basta para decidir SALE ni PASA por si sola).")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
