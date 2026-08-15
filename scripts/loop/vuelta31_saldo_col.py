"""Vuelta 31: EL SALDO de una tanda OP-F-04, con las TRES especies.

SUCESOR DE scripts/loop/vuelta30_saldo_opf04.py, y el cambio va declarado con su
motivo, que es lo que la regla 2 del EJECUTOR.md obliga.

Aquel instrumento contaba DOS especies (RESUELTO y FUNDIDO por P.19) y todo lo
demas era PENDIENTE. Para COL eso daria un falso pendiente: la adjudicacion 2 del
acta de la vuelta 30 (linea 6610, leida hoy) declaro keep_customers_strategy
MULTIFUENTE LEGITIMO por extension citable de P.19, SIN corte y con la fuente
intacta, y dijo con estas palabras que *el saldo de COL lo cuenta como especie
propia (EMBEBIDO LEGITIMO), igual que WEI cuenta sus fundidos*. Un solo numero
haria pasar por pendiente lo que es una adjudicacion escrita, que es la misma
mentira al reves que P.19 obliga a evitar con los fundidos.

LAS TRES ESPECIES:
  RESUELTO  el nodo ya no declara el libro de la tanda: su bloque se fue a su
            destino (miembro o nodo propio).
  FUNDIDO   lo declara y esta bien: P.19 lo refundio DENTRO del nodo y el punto 2
            manda que quede MULTIFUENTE LEGITIMO.
  EMBEBIDO  lo declara y esta bien: el material nunca fue un bloque, viaja dentro
            de las frases, y ya vive en el estado final que P.19 produce. No hay
            operacion que ejecutar.
  PENDIENTE cualquier otra cosa. Solo esta cuenta contra el cierre de la tanda.

No escribe nada.

Uso: python scripts/loop/vuelta31_saldo_col.py <ID_OP> <trozo del libro>
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NODOS = os.path.join(RAIZ, "dataset", "nodos")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")

# Los nodos que P.19 dejo a proposito MULTIFUENTE, con la vuelta que lo hizo.
FUNDIDOS_P19 = {
    "coeficiente_viral": "vuelta 30, P.19: fusion interna, multifuente legitimo",
    "decision_de_vender_startup": "vuelta 30, P.19: fusion interna, multifuente legitimo",
    "viral_loop_marketing": "vuelta 30, P.20 mas P.19: corte unico, multifuente legitimo",
}

# El unico EMBEBIDO adjudicado hasta hoy, con el acta que lo declaro. No es una
# excepcion silenciosa: se imprime con su cita y se cuenta aparte.
EMBEBIDOS = {
    "keep_customers_strategy": (
        "acta de la vuelta 30, seccion 4 punto 2: MULTIFUENTE LEGITIMO por "
        "extension citable de P.19, sin corte y con la fuente intacta"),
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

    print("SALDO DE %s, medido contra el grafo de HOY, con las TRES especies" % id_op)
    print("el libro de la tanda: %r" % trozo)
    print("=" * 78)
    resueltos = fundidos = embebidos = pendientes = 0
    for nid in sorted(nomina):
        ruta = os.path.join(NODOS, nid + ".json")
        if not os.path.exists(ruta):
            print("  [AUSENTE ] %s" % nid)
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
        elif nid in EMBEBIDOS:
            estado, marca = "EMBEBIDO", "  (%s)" % EMBEBIDOS[nid]
            embebidos += 1
        else:
            estado, marca = "PENDIENT", ""
            pendientes += 1
        print("  [%s] %-38s pasos %2d  fuente: %s%s" % (estado, nid, pasos, f, marca))

    print()
    print("=" * 78)
    print("NOMINA %d: RESUELTOS %d, FUNDIDOS por P.19 %d, EMBEBIDOS legitimos %d, PENDIENTES %d"
          % (len(nomina), resueltos, fundidos, embebidos, pendientes))
    print("LA TANDA ESTA ENTERA" if pendientes == 0 else "LA TANDA SIGUE PARCIAL")
    return 0


if __name__ == "__main__":
    sys.exit(main())
