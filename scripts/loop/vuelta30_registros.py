"""Vuelta 30, TAREA 1 punto 1: los registros en docs/plan/OPERACIONES.jsonl.

Escribe, como CORRECCION DECLARADA y SIN BORRAR EL TEXTO VIEJO (se anade al final
del campo nota), que OP-F-02 y OP-F-03 quedan HECHAS, y que la correccion 1 de la
relectura conjunta queda APLICADA Y CERRADA.

NADA se copia de un acta: la evidencia que la nota cita se MIDE contra el grafo en
esta corrida (EJECUTOR.md regla 2). Si un id no esta vivo o un conteo no calza, el
script PARA y no escribe. Lo unico que se cita de fuera es la adjudicacion del
auditor, que es texto de acta y va con su seccion y su numero.

Uso:
    python scripts/loop/vuelta30_registros.py --simular
    python scripts/loop/vuelta30_registros.py --ejecutar
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
ROJO = os.path.join(RAIZ, "docs", "plan", "INDICE_ROJO_DECLARADO.jsonl")

# La evidencia que cada nota va a citar, con la cifra que este script tiene que
# reproducir HOY. Si el grafo no la da, no se escribe la nota.
EVIDENCIA = {
    "escenarios_de_evolucion_de_la_ia": 6,
    "critica_del_plan_con_ia": 5,
    "ideacion_con_ia_en_la_sesion": 4,
    "estrategia_circular_y_mecanismo_de_retorno": 4,
    # 9, no 4: la primera pasada de este instrumento traia un 4 puesto por el
    # ejecutor sin medir, y la guarda lo caso antes de escribir nada. La cifra
    # buena es la del grafo de hoy.
    "seleccion_de_proveedores_por_costo_total": 9,
    "driver_de_inventario": 4,
    "producto_como_servicio_de_acceso": 8,
    "framework_caracteristicas_ventajas_beneficios": 8,
    "diferencia_ventaja_beneficio": 4,
}

MARCA = "CORRECCION DECLARADA, 14 ago 2026 (vuelta 30)"


def leer_nodo(nid):
    ruta = os.path.join(NODOS, nid + ".json")
    if not os.path.exists(ruta):
        return None
    with open(ruta, encoding="utf-8") as fh:
        return json.load(fh)


def vivo(d):
    return not d.get("deprecado") and not d.get("deprecated")


def nota_op_f_02(medido):
    return (
        " " + MARCA + ", y nada de lo de arriba se borra: **OP-F-02 QUEDA HECHA**. "
        "Adjudicada por el acta de la vuelta 29 del auditor (docs/loop/ACTA_AUDITOR.md, "
        "seccion 4, punto 4), con estas palabras: 'Por la misma vara, OP-F-02 SE DECLARA "
        "HECHA (tres de tres, 6 y 6, cotejada)'. LA EVIDENCIA, MEDIDA CONTRA EL GRAFO EN "
        "ESTA CORRIDA y no copiada del acta: sus tres nodo propio estan vivos, "
        "escenarios_de_evolucion_de_la_ia con %(escenarios_de_evolucion_de_la_ia)d pasos, "
        "critica_del_plan_con_ia con %(critica_del_plan_con_ia)d y "
        "ideacion_con_ia_en_la_sesion con %(ideacion_con_ia_en_la_sesion)d, y los tres "
        "estan declarados en docs/plan/INDICE_ROJO_DECLARADO.jsonl con su operacion y su "
        "fecha. Del acta se citan las guardas que corrio el auditor y que este script no "
        "vuelve a correr: caso positivo 6 CAEN y 6 PASAN (seccion 1, punto 14) y los tres "
        "cortes cotejados al texto dentro de los treinta de treinta (seccion 1, punto 7). "
        "EL CAMPO estado SE QUEDA EN LISTA y no se toca: ninguna pagina del plan define el "
        "valor HECHA para ese campo, las 71 operaciones estan en LISTA medidas hoy, y "
        "estrenar un valor nuevo seria doctrina y no registro. La declaracion vive en esta "
        "nota, que es donde el encargo de la vuelta 30 la manda."
        % medido
    )


def nota_op_f_03(medido):
    return (
        " " + MARCA + ", y nada de lo de arriba se borra: **OP-F-03 QUEDA HECHA, y con "
        "ella la CORRECCION 1 DE LA RELECTURA CONJUNTA QUEDA APLICADA Y CERRADA**. "
        "Adjudicada por el acta de la vuelta 29 del auditor (docs/loop/ACTA_AUDITOR.md, "
        "seccion 4, punto 4), con estas palabras: 'Pregunta 5 (OP-F-03): SE DECLARA HECHA. "
        "Sus diecinueve bloques estan en el arbol (catorce de la vuelta 27, cinco de esta), "
        "su caso positivo pasa 15 de 15, sus cortes estan cotejados por mi al texto, y Gate "
        "0 y las suites estan verdes por mi corrida'. LA EVIDENCIA DE LOS CUATRO NODO "
        "PROPIO, MEDIDA CONTRA EL GRAFO EN ESTA CORRIDA: "
        "estrategia_circular_y_mecanismo_de_retorno %(estrategia_circular_y_mecanismo_de_retorno)d "
        "pasos, seleccion_de_proveedores_por_costo_total %(seleccion_de_proveedores_por_costo_total)d, "
        "driver_de_inventario %(driver_de_inventario)d y producto_como_servicio_de_acceso "
        "%(producto_como_servicio_de_acceso)d, los cuatro vivos y los cuatro declarados en "
        "docs/plan/INDICE_ROJO_DECLARADO.jsonl. LA CORRECCION 1, que es "
        "docs/loop/PLAN_V28_RELECTURA.json y sus dos mudanzas, queda CONSUMADA ENTERA y se "
        "mide asi hoy: la mudanza d2 del acta 27 dejo vivo a "
        "estrategia_circular_y_mecanismo_de_retorno como nodo propio de la familia Hugos, y "
        "la mudanza d4 dejo a framework_caracteristicas_ventajas_beneficios con "
        "%(framework_caracteristicas_ventajas_beneficios)d pasos y a "
        "diferencia_ventaja_beneficio reducido a %(diferencia_ventaja_beneficio)d, que es "
        "exactamente el cuatro mas cuatro que el plan declara. Del acta se cita lo que el "
        "auditor corrio y este script no repite: la rebanada docs/loop/PLAN_V29_RELECTURA_D1.json "
        "verificada identica al sello de la vuelta 28 (seccion 1, punto 7) y el caso positivo "
        "15 de 15 (seccion 1, punto 14). EL CAMPO estado SE QUEDA EN LISTA por el mismo "
        "motivo escrito en la nota de OP-F-02."
        % medido
    )


NOTAS = {"OP-F-02": nota_op_f_02, "OP-F-03": nota_op_f_03}


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("--simular", "--ejecutar"):
        print(__doc__)
        return 2
    ejecutar = sys.argv[1] == "--ejecutar"

    print("=" * 78)
    print("LA EVIDENCIA, MEDIDA CONTRA EL GRAFO EN ESTA CORRIDA")
    print("=" * 78)
    fallos = []
    medido = {}
    for nid, esperado in EVIDENCIA.items():
        d = leer_nodo(nid)
        if d is None:
            fallos.append("%s: ausente del grafo" % nid)
            print("  [ROJO] %-46s AUSENTE" % nid)
            continue
        n = len(d.get("pasos_accionables") or [])
        medido[nid] = n
        ok = vivo(d) and n == esperado
        if not ok:
            fallos.append("%s: vivo=%s pasos=%d, esperados %d" % (nid, vivo(d), n, esperado))
        print("  [%s] %-46s vivo=%-5s pasos=%2d (esperados %2d)"
              % ("OK  " if ok else "ROJO", nid, vivo(d), n, esperado))

    print()
    print("EL INDICE ROJO DECLARADO, leido hoy")
    rojo = []
    with open(ROJO, encoding="utf-8") as fh:
        for linea in fh:
            if linea.strip():
                rojo.append(json.loads(linea))
    ids_rojo = {x["id"] for x in rojo}
    for nid in ("escenarios_de_evolucion_de_la_ia", "critica_del_plan_con_ia",
                "ideacion_con_ia_en_la_sesion", "estrategia_circular_y_mecanismo_de_retorno",
                "seleccion_de_proveedores_por_costo_total", "driver_de_inventario",
                "producto_como_servicio_de_acceso"):
        presente = nid in ids_rojo
        if not presente:
            fallos.append("%s: no esta en el indice rojo declarado" % nid)
        print("  [%s] %-46s en el indice rojo" % ("OK  " if presente else "ROJO", nid))

    if fallos:
        print()
        print("PARA: %d guarda(s) en rojo. No se escribe nada." % len(fallos))
        for f in fallos:
            print("  - %s" % f)
        return 1

    print()
    print("=" * 78)
    print("LAS NOTAS QUE SE ANADEN (el texto viejo se queda entero delante)")
    print("=" * 78)
    lineas = []
    with open(OPS, encoding="utf-8") as fh:
        for linea in fh:
            if linea.strip():
                lineas.append(json.loads(linea))

    tocadas = 0
    for o in lineas:
        if o["id_op"] not in NOTAS:
            continue
        if MARCA in (o.get("nota") or ""):
            print("\nPARA: %s ya trae la marca %r. No se escribe nada." % (o["id_op"], MARCA))
            return 1
        anadido = NOTAS[o["id_op"]](medido)
        print("\n%s: nota de %d caracteres, se le anaden %d"
              % (o["id_op"], len(o.get("nota") or ""), len(anadido)))
        print("  %s" % anadido[:300].replace("\n", " "))
        o["nota"] = (o.get("nota") or "") + anadido
        tocadas += 1

    if tocadas != len(NOTAS):
        print("\nPARA: se esperaban %d operaciones y se tocaron %d." % (len(NOTAS), tocadas))
        return 1

    if not ejecutar:
        print()
        print("SIMULACION: cero escrituras.")
        return 0

    with open(OPS, "w", encoding="utf-8", newline="") as fh:
        for o in lineas:
            fh.write(json.dumps(o, ensure_ascii=False) + "\n")
    print()
    print("ESCRITO: %d nota(s) en docs/plan/OPERACIONES.jsonl (%d lineas en total)."
          % (tocadas, len(lineas)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
