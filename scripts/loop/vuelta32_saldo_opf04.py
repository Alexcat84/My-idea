"""Vuelta 32: EL SALDO de una tanda OP-F-04, sucesor de vuelta30_saldo_opf04.py.

SUCESOR DECLARADO, con el cambio y su motivo dentro (EJECUTOR.md regla 2). Mide
exactamente lo mismo, linea por linea, con UN SOLO cambio: el censo de nodos que
P.19 dejo a proposito MULTIFUENTE gana su CUARTA entrada, principio_calidad_mvp,
fundido en esta vuelta 32.

POR QUE ESE CENSO SE ESCRIBE A MANO Y NO SE DEDUCE, que es la pregunta que este
cambio obliga a contestar: un nodo que sigue declarando el libro de la tanda o no
se toco, o se resolvio POR FUSION INTERNA. Las dos cosas se ven igual en el campo
fuente, asi que la unica manera honesta de distinguirlas es NOMBRAR los fundidos
uno por uno y contarlos aparte, que es lo que el instrumento de la vuelta 30 ya
hacia. Un instrumento que dedujera 'fundido' de la sola presencia del libro
convertiria cada bloque SIN TOCAR en un falso verde.

EL CONTRASTE, y se publica en vez de resolverse copiando: el instrumento viejo
corrido HOY sobre esta misma tanda da NOMINA 14, RESUELTOS 12, FUNDIDOS 1,
PENDIENTES 1 (salida en docs/loop/SALIDA_V32_SALDO_HOR_VIEJO.txt), porque no
conoce el fundido de esta vuelta. La diferencia entre las dos corridas es
exactamente esa entrada y nada mas.

Uso:
    python scripts/loop/vuelta32_saldo_opf04.py <ID_OP> <trozo del libro>
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")

# Los nodos que P.19 dejo a proposito MULTIFUENTE, con la vuelta que lo hizo.
# No es una excepcion silenciosa: se imprime como tal y se cuenta aparte.
FUNDIDOS_P19 = {
    "coeficiente_viral": "vuelta 30, P.19: fusion interna, multifuente legitimo",
    "decision_de_vender_startup": "vuelta 30, P.19: fusion interna, multifuente legitimo",
    "viral_loop_marketing": "vuelta 30, P.20 mas P.19: corte unico, multifuente legitimo",
    "principio_calidad_mvp": "vuelta 32, P.19: fusion interna del 14vo, multifuente legitimo",
}


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    id_op, trozo = sys.argv[1], sys.argv[2]

    ops = {}
    with open(OPS, encoding="utf-8") as fh:
        for linea in fh:
            if linea.strip():
                o = json.loads(linea)
                ops[o["id_op"]] = o
    nomina = ops[id_op]["nodos"]

    print("SALDO DE %s, medido contra el grafo de HOY" % id_op)
    print("el libro de la tanda: %r" % trozo)
    print("=" * 78)
    resueltos = fundidos = pendientes = 0
    for nid in sorted(nomina):
        ruta = os.path.join(NODOS, nid + ".json")
        if not os.path.exists(ruta):
            print("  [AUSENTE] %s" % nid)
            pendientes += 1
            continue
        with open(ruta, encoding="utf-8") as fh:
            d = json.load(fh)
        f = d.get("fuente") or ""
        pasos = len(d.get("pasos_accionables") or [])
        sigue = trozo.lower() in f.lower()
        if not sigue:
            estado, marca = "RESUELTO", ""
            resueltos += 1
        elif nid in FUNDIDOS_P19:
            estado, marca = "FUNDIDO ", "  (%s)" % FUNDIDOS_P19[nid]
            fundidos += 1
        else:
            estado, marca = "PENDIENT", ""
            pendientes += 1
        print("  [%s] %-38s pasos %2d  fuente: %s%s" % (estado, nid, pasos, f, marca))

    print()
    print("=" * 78)
    print("NOMINA %d: RESUELTOS %d, FUNDIDOS por P.19 %d, PENDIENTES %d"
          % (len(nomina), resueltos, fundidos, pendientes))
    print("LA TANDA ESTA ENTERA" if pendientes == 0 else "LA TANDA SIGUE PARCIAL")
    return 0


if __name__ == "__main__":
    sys.exit(main())
