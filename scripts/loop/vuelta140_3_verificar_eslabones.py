# -*- coding: utf-8 -*-
r"""vuelta140_3_verificar_eslabones.py . VERIFICA Y DECLARA EL DESTINO CUMPLIDO
DE UNA OPERACION DE ENLACE SIN ESCRIBIR NADA (TAREA 3, remitida 2 de 5, de la
vuelta 140; acta de la vuelta 139, adjudicacion 3.7).

POR QUE EXISTE. `OP-M-01-ESLABONES` NO SE RE-ESCRIBE: sus dos aristas YA estan
presentes hoy (medido por el auditor, 2 de 2, y por `tallar_estado_de_fase.py`
en la TAREA 2.a de esta vuelta). Escribir una arista que ya existe es fabricar
una duplicada, que es exactamente lo que la verificacion 2 de su propia ficha
prohibe con estas palabras: *"el segundo peldano NO SE ANADE, SE HEREDA... Si se
anade ademas, nace una duplicada de la clase OP-S-12"*. Es la misma figura que
`OP-E-01` en la vuelta 87.

ESTE INSTRUMENTO NO ESCRIBE NUNCA. No tiene modo `--ejecutar`, no importa el
escritor y no abre ningun fichero de nodo en modo escritura.

QUE COMPRUEBA, y cada comprobacion sale de una VERIFICACION LITERAL de la ficha:
  (V0) la VUELTA no existe ni literal ni resuelta en ninguno de los dos
       peldanos ("LA VUELTA NO EXISTE NI LITERAL NI RESUELTA en ninguno de los
       dos peldanos, comprobado CON EL RESOLUTOR PUESTO").
  (V1) el segundo peldano esta HEREDADO, no anadido dos veces: se cuenta
       cuantas entradas de las listas tocadas resuelven a el, y tiene que ser
       UNA.
  (V2) el grado no subio de mas: se cuenta cuantas de las aristas de la ficha
       estan presentes y se declara cuantas se escribirian (CERO).
  (V3) los tres actos siguen siendo TRES NODOS VIVOS Y DISTINTOS: la escalera
       los encadena, no los funde.
  (V4) P.9: para cada arista presente se dice CON QUE LITERAL vive y si ese
       literal es el ID VIVO o un id que resuelve por alias. La ficha manda:
       *"si el id escrito no es el id vivo, la arista se rehace"*. Si alguna
       vive solo por alias, este instrumento CAE EN ROJO NOMBRANDOLA y NO
       declara el destino cumplido: la reparacion es de la vuelta, no suya.

USO:
  python scripts/loop/vuelta140_3_verificar_eslabones.py --op OP-M-01-ESLABONES
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tallar_estado_de_fase as T  # noqa: E402


def literales_que_resuelven(lista, objetivo, resolver):
    return [x for x in (lista or []) if resolver(x) == objetivo]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--op", required=True)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    ops = {o["id_op"]: o for o in T.cargar_ops("WORK")}
    if a.op not in ops:
        print("ROJO: %s no existe en docs/plan/OPERACIONES.jsonl" % a.op)
        return 1
    op = ops[a.op]
    nodos = T.cargar_grafo("WORK")
    resolver = T.resolver_de(nodos)

    print("=" * 78)
    print("VERIFICAR Y DECLARAR EL DESTINO DE %s . ESTE INSTRUMENTO NO ESCRIBE" % a.op)
    print("=" * 78)
    print("tipo: %s | fase escrita: %s | estado (contraste): %s"
          % (op.get("tipo"), op.get("fase"), op.get("estado")))

    fallos = []
    pares = T.pares_de_aristas(op, fallos)
    print("pares dirigidos de la ficha: %d" % len(pares))

    # (V3) los nodos de la ficha siguen vivos y distintos
    print("")
    print("(V3) los nodos del acto siguen siendo NODOS DISTINTOS Y VIVOS (la escalera")
    print("     los encadena, NO los funde):")
    resueltos = []
    for x in (op.get("nodos") or []):
        r = resolver(x)
        vivo = T.vivo(nodos.get(r))
        resueltos.append(r)
        print("     %-40s -> %-40s vivo=%s" % (x, r, vivo))
        if not vivo:
            fallos.append("(V3) %s (resuelto %s) NO esta vivo" % (x, r))
    if len(set(resueltos)) != len(resueltos):
        fallos.append("(V3) dos nodos del acto resuelven al MISMO id: %s" % resueltos)
    print("     nodos distintos tras resolver: %d de %d" % (len(set(resueltos)), len(resueltos)))

    presentes = 0
    print("")
    for crudo_o, crudo_d in pares:
        o, d = resolver(crudo_o), resolver(crudo_d)
        print("arista de la ficha: %s -> %s" % (crudo_o, crudo_d))
        if (o, d) != (crudo_o, crudo_d):
            print("   resuelta a: %s -> %s" % (o, d))
        ok, _, _ = T.arista_presente(nodos, resolver, o, d)
        print("   (V2) PRESENTE HOY: %s" % ok)
        if ok:
            presentes += 1
        else:
            fallos.append("(V2) %s -> %s NO esta presente: esta operacion no se puede "
                          "declarar cumplida sin escribirla" % (o, d))

        # (V0) la vuelta
        inversa, _, _ = T.arista_presente(nodos, resolver, d, o)
        print("   (V0) la VUELTA %s -> %s existe: %s" % (d, o, inversa))
        if inversa:
            fallos.append("(V0) la VUELTA %s -> %s EXISTE, y la regla de la escalera la "
                          "prohibe" % (d, o))

        # (V1) y (V4): con que literal vive, y cuantas veces
        n_o = nodos.get(o) or {}
        n_d = nodos.get(d) or {}
        en_sig = literales_que_resuelven(n_o.get("nodos_siguientes"), d, resolver)
        en_prev = literales_que_resuelven(n_d.get("nodos_previos"), o, resolver)
        print("   (V1) literales en %s.nodos_siguientes que resuelven a %s: %s"
              % (o, d, en_sig or "ninguno"))
        print("   (V1) literales en %s.nodos_previos que resuelven a %s: %s"
              % (d, o, en_prev or "ninguno"))
        if len(en_sig) > 1 or len(en_prev) > 1:
            fallos.append("(V1) %s -> %s vive MAS DE UNA VEZ tras resolver (sig=%d, prev=%d): "
                          "es una duplicada de la clase OP-S-12" % (o, d, len(en_sig), len(en_prev)))

        por_alias = [x for x in (en_sig + en_prev) if x != resolver(x)]
        directos = [x for x in (en_sig + en_prev) if x == resolver(x)]
        print("   (V4) P.9: literales que son el ID VIVO: %s | literales que viven por "
              "ALIAS: %s" % (directos or "ninguno", por_alias or "ninguno"))
        if por_alias and not directos:
            fallos.append("(V4) P.9: %s -> %s vive SOLO por alias (%s). La ficha manda que "
                          "'si el id escrito no es el id vivo, la arista se rehace'"
                          % (o, d, ", ".join(por_alias)))
        elif por_alias:
            print("        NOTA: vive de las DOS formas. La directa cumple P.9; la que va")
            print("        por alias es material de OP-S-12, no de esta operacion.")

    print("")
    print("-" * 78)
    print("CIFRA: aristas de la ficha: %d | presentes hoy: %d | que se escribirian: 0"
          % (len(pares), presentes))
    if fallos:
        print("")
        print("ROJO, %d cosa(s) no cuadran. EL DESTINO NO SE DECLARA CUMPLIDO:" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1
    print("")
    print("VERDE: LAS %d ARISTAS DE %s YA ESTAN PRESENTES, cada una UNA SOLA VEZ tras"
          % (len(pares), a.op))
    print("resolver, sin vuelta, con los tres nodos vivos y distintos, y con el id VIVO")
    print("escrito. SU DESTINO SE DECLARA CUMPLIDO Y NO SE RE-ESCRIBE NADA.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
