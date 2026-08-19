# -*- coding: utf-8 -*-
"""vuelta36_cerrar_opd03.py - EL CIERRE DE OP-D-03, escrito por instrumento y no a mano.

SUCESOR DECLARADO de scripts/loop/vuelta34_nota_opd03.py (EJECUTOR.md regla 2), y lo
que cambia va dicho: aquel apendia a la nota el REGISTRO del paso 1 del orden
interno, y este apende el REGISTRO DE CIERRE de la operacion entera.

POR QUE EL ESTADO SE QUEDA EN `LISTA` Y NO SE INVENTA UNO NUEVO. Medido hoy sobre
docs/plan/OPERACIONES.jsonl: las 71 operaciones estan en `LISTA`, y las DOS que ya
se ejecutaron (OP-D-01 y OP-D-02) tambien. La casa registra el hecho consumado en
la NOTA, no en el estado. Inventar un estado `HECHA` seria inventar una regla, y la
regla 5 de EJECUTOR.md lo prohibe. Queda como PENDIENTE DE DOCTRINA en el reporte:
el esquema no tiene con que distinguir una operacion hecha de una pendiente.

GUARDAS, escritas para caer:
  1. la operacion existe y su estado es el que este cierre espera.
  2. el texto viejo de la nota queda LITERAL dentro de la nueva, o aborta.
  3. el acto tiene HOY cero pares A en el archivo, medido y no supuesto: si
     quedara uno, la operacion NO cierra sin fusion y el script ABORTA.
  4. el numero de operaciones no cambia, y ninguna otra se toca.

Uso: python scripts/loop/vuelta36_cerrar_opd03.py
"""
import io
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
VER = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_VEREDICTOS.jsonl")

ID_OP = "OP-D-03"
ESTADO_ESPERADO = "LISTA"
ACTO = ["ab_testing_optimizacion", "funnel_get_customers_optimizacion",
        "optimizacion_embudo_get_customers", "split_testing",
        "split_testing_experimentos_ab", "test_ab_precio"]

CIERRE = (
    " REGISTRO DE CIERRE, 18 ago 2026 (vuelta 36). CORRECCION DECLARADA, y el texto viejo se "
    "queda entero arriba: LA OPERACION CIERRA CON SU DESTEJIDO HECHO Y SIN FUSION, y el paso 2 "
    "de su orden interno (decidir sobre los SEIS nodos) SE RESUELVE SIN FUNDIR NADA porque el "
    "acto DEJO DE EXISTIR. "
    "COMO PASO, con la medicion del dia al lado y no de memoria. El paso 2 exigia por P.5 leer "
    "el acto ENTERO antes de fundirlo. La vuelta 35 lo midio y encontro que CINCO de los seis "
    "pares A del acto se habian emitido contra texto que las cirugias ya se habian llevado (dos "
    "varas independientes, docs/loop/SALIDA_V35_RANCIOS.txt), escribio las cinco relecturas, las "
    "sello y PARO sin volcarlas por la regla 5 de EJECUTOR.md. El fundador las adjudico el 15 ago "
    "2026 en docs/loop/paradas/2026-08-15-p5-rancios-opd03-DECISION.md, con tres decisiones: se "
    "vuelcan las cinco; el 643 SI se lee como dirigida dentro del acto; y la operacion se "
    "resuelve por el 643, D la cierra sin fusion y A la replantea como fusion de dos. "
    "LO EJECUTADO EN LA VUELTA 36. Las cinco relecturas VOLCADAS por el carril del banco 9.10 "
    "con su barrido de tablas derivadas en el mismo acto (277, 374, 452, 1571 y 1575, las cinco "
    "de A a D, docs/loop/_lote_v36.jsonl), marcador recomputado con el instrumento de la casa a "
    "n 3388, A 576, B 83, C 8, D 2721. Y el 643 leido como LECTURA DIRIGIDA LD-82 con los dos "
    "nodos impresos ENTEROS antes de decidir y la arista buscada en LOS DOS SENTIDOS con el "
    "resolutor de P.1 aplicado: D, los dos sanos, sin arista declarada. Volcado por el mismo "
    "carril (docs/loop/_lote_v36_643.jsonl), marcador a n 3388, A 575, B 83, C 8, D 2722. "
    "LA RESPUESTA DE P.5 PARA ESTE ACTO, MEDIDA Y NO DIBUJADA: no es una familia de seis, no son "
    "dos familias, y no queda ni un par. El acto tiene CERO pares A y DESAPARECE del censo de "
    "actos. El instrumento lo confirma al digito (scripts/plan/recomputo_3388.py, salida "
    "docs/loop/SALIDA_V36_RECOMPUTO_3388_B.txt): actos de 335 a 333, cerradas de 281 sobre 604 "
    "nodos a 279 sobre 598, nodos con al menos una A de 851 a 845, y las cuatro comprobaciones "
    "del 08_VERIFICACION.md OK las cuatro. "
    "LOS SEIS NODOS QUEDAN VIVOS Y SANOS. Ninguno se funde, ninguno se deprecia, ninguno pierde "
    "un paso en esta vuelta. El acto existia porque los nodos repetian, y lo que repetia eran "
    "los bloques que OP-F-04-WEI, OP-F-04-RAC y el propio paso 1 de esta operacion se llevaron. "
    "Eso no es un fracaso de la operacion: es el destejido haciendo su trabajo. "
    "EL CAMPO superviviente SE QUEDA EN null A PROPOSITO, y no es un olvido: no hay fusion, asi "
    "que no hay superviviente que fijar. El campo eliminar se queda vacio por lo mismo. "
    "EL ESTADO SE QUEDA EN LISTA porque el esquema de OPERACIONES.jsonl no tiene otro: las 71 "
    "estan en LISTA, incluidas OP-D-01 y OP-D-02, que ya se ejecutaron. Queda anotado como "
    "PENDIENTE DE DOCTRINA: el esquema no distingue una operacion HECHA de una pendiente, y hoy "
    "eso solo se lee en la nota."
)


def main():
    lineas = [l for l in io.open(OPS, encoding="utf-8") if l.strip()]
    ops = [json.loads(l) for l in lineas]
    antes = len(ops)
    print("operaciones en el fichero: %d" % antes)

    print("\nGUARDA 3: el acto tiene HOY cero pares A, medido y no supuesto")
    V = [json.loads(l) for l in io.open(VER, encoding="utf-8") if l.strip()]
    dentro = [v for v in V if v["clase"] == "A" and v["nodo_a"] in ACTO and v["nodo_b"] in ACTO]
    print("  pares A con LOS DOS nodos dentro del acto: %d" % len(dentro))
    for v in dentro:
        print("    ABORTA por este: puesto %d, %s contra %s"
              % (v["puesto_intra"], v["nodo_a"], v["nodo_b"]))
    if dentro:
        print("  Con un solo par A vivo la operacion NO cierra sin fusion. SE PARA.")
        return 1
    print("  OK: cero. La operacion puede cerrar sin fusion.")

    print("\nGUARDAS 1, 2 y 4: la operacion, su estado y su nota")
    tocadas = 0
    for i, o in enumerate(ops):
        if o["id_op"] != ID_OP:
            continue
        if o.get("estado") != ESTADO_ESPERADO:
            print("  ABORTA: %s esta en %r y este cierre esperaba %r"
                  % (ID_OP, o.get("estado"), ESTADO_ESPERADO))
            return 1
        vieja = o.get("nota") or ""
        nueva = vieja + CIERRE
        if vieja not in nueva:
            print("  ABORTA: la nota vieja no queda literal dentro de la nueva")
            return 1
        o["nota"] = nueva
        tocadas += 1
        print("  %s: estado %s (sin tocar), nota de %d a %d caracteres, texto viejo LITERAL "
              "dentro  OK" % (ID_OP, o["estado"], len(vieja), len(nueva)))
    if tocadas != 1:
        print("  ABORTA: se tocaron %d operaciones y este cierre toca exactamente 1" % tocadas)
        return 1
    if len(ops) != antes:
        print("  ABORTA: el total de operaciones cambio")
        return 1

    io.open(OPS, "w", encoding="utf-8", newline="\n").write(
        "".join(json.dumps(o, ensure_ascii=False) + "\n" for o in ops))
    print("\nESCRITO %s: %d operaciones, ninguna alta ni baja, una sola nota tocada."
          % (os.path.relpath(OPS, RAIZ).replace("\\", "/"), len(ops)))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
