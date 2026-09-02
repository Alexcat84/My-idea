# -*- coding: utf-8 -*-
r"""vuelta145_2d_aristas_movidas.py . TODA ARISTA QUE SE MUEVE, NOMBRADA Y
ADJUDICADA, CON SU UNIDAD BIEN NOMBRADA. VUELTA 145, TAREA 2.d.

POR QUE NACE (acta 144, caida 4.7 del auditor). La vuelta 144 publico
`docs/loop/SALIDA_V144_3D_ARISTAS_MOVIDAS.txt` con el rotulo *"Aristas
RESUELTAS entre nodos VIVOS"* y las cifras 7.343 y 7.341, PERO EL INSTRUMENTO
QUE LA IMPRIMIO NO QUEDO EN `scripts/`: nadie podia re-correrlo. Y el rotulo
no decia la unidad que de verdad medira: el auditor reprodujo las dos cifras al
digito, pero SOLO exigiendo que la FUENTE este viva; con LOS DOS EXTREMOS vivos
la misma medicion da otras dos. Son DOS UNIDADES, y publicar una con el nombre
de la otra es la especie de la CORRECCION 18.

QUE MIDE, y PUBLICA LAS DOS UNIDADES, cada una con su nombre entero:
  (A) ARISTAS RESUELTAS DE LA UNION DE LAS DOS VISTAS, LEIDAS DE NODOS VIVOS.
      Se recorren `nodos_siguientes` Y `nodos_previos` de cada nodo VIVO (la
      vista de previos, invertida al orden origen-destino), se resuelven los
      dos extremos con el resolutor de la casa (P.1) y se unen los pares. EL
      OTRO EXTREMO PUEDE RESOLVER A UN NODO DEPRECADO y la arista se cuenta
      igual. Es la unidad que la vuelta 144 publico, y su nombre viejo,
      "aristas RESUELTAS entre nodos VIVOS", no la decia.
  (B) ARISTAS RESUELTAS CON LOS DOS EXTREMOS VIVOS. Lo mismo, exigiendo ADEMAS
      que el otro extremo resuelto este vivo.
Las auto-aristas tras resolver se descartan en las dos, y se cuentan aparte.

COMO SE FIJO CUAL ERA LA UNIDAD (A), y se dice porque es una CORRECCION
DECLARADA DENTRO DE LA PROPIA VUELTA 145: la primera version de este
instrumento leyo solo `nodos_siguientes` y dio 7.327 y 7.325, que NO son las
cifras que la vuelta 144 publico. Se midieron las seis variantes posibles sobre
los mismos dos commits y solo UNA reproduce 7.343 y 7.341: la UNION de las dos
vistas con el nodo leido vivo. Las cifras no se ajustaron a la respuesta: se
midio cual definicion las produce y se escribio ESA.

EL CONJUNTO QUE ENTRA Y EL QUE SALE se computan sobre la unidad (A), que es la
que la vuelta 144 uso, y se comprueba ADEMAS que con la unidad (B) salen los
MISMOS conjuntos: si no salieran, seria una diferencia de fondo y no de rotulo,
y el instrumento lo canta.

EL RESOLUTOR ES EL DE LA CASA, importado de `tallar_estado_de_fase`, nunca uno
propio: todo conteo que toca ids pasa por el resolutor antes de contar (P.1,
EJECUTOR.md 9).

USO:
  python scripts/loop/vuelta145_2d_aristas_movidas.py <ref_antes> <ref_despues>
  python scripts/loop/vuelta145_2d_aristas_movidas.py 5fff85f7 c72ce2c0
  python scripts/loop/vuelta145_2d_aristas_movidas.py HEAD WORK
"""
import argparse
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))

import tallar_estado_de_fase as T  # noqa: E402


def vivos_de(nodos):
    return set(k for k, n in nodos.items() if not (n.get("deprecado") or n.get("deprecated")))


def aristas(ref):
    """Devuelve (conjunto_A, conjunto_B, auto_A, auto_B) para `ref`:
      A = aristas resueltas de la UNION de las dos vistas, leidas de nodos VIVOS,
      B = las de A cuyos DOS extremos resueltos estan vivos.
    Cada conjunto es un set de (origen_resuelto, destino_resuelto)."""
    nodos = T.cargar_grafo(ref)
    resolver = T.resolver_de(nodos)
    vivos = vivos_de(nodos)
    a = set()
    auto_a = auto_b = 0
    for nid in vivos:
        # LAS DOS VISTAS. `nodos_previos` se invierte al orden origen-destino
        # para que las dos se unan en la misma unidad.
        pares = ([(nid, x) for x in (nodos[nid].get("nodos_siguientes") or [])] +
                 [(x, nid) for x in (nodos[nid].get("nodos_previos") or [])])
        for origen, destino in pares:
            ro, rd = resolver(origen), resolver(destino)
            if ro == rd:
                auto_a += 1
                if ro in vivos and rd in vivos:
                    auto_b += 1
                continue
            a.add((ro, rd))
    b = set((o, d) for o, d in a if o in vivos and d in vivos)
    return a, b, auto_a, auto_b


def flecha(par):
    return "%s -> %s" % par


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("antes")
    ap.add_argument("despues")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    a_antes, b_antes, auto_a_antes, auto_b_antes = aristas(a.antes)
    a_desp, b_desp, auto_a_desp, auto_b_desp = aristas(a.despues)

    print("GUARDA DE ARISTAS MOVIDAS: TODA ARISTA QUE SE MUEVE, NOMBRADA Y ADJUDICADA")
    print("Instrumento: scripts/loop/vuelta145_2d_aristas_movidas.py (vuelta 145, TAREA 2.d)")
    print("Resolutor de la casa (P.1). ANTES: %s | DESPUES: %s" % (a.antes, a.despues))
    print("=" * 78)
    print("LAS DOS UNIDADES, CADA UNA CON SU NOMBRE ENTERO:")
    print("  (A) aristas resueltas de la UNION de las dos vistas, leidas de nodos VIVOS")
    print("        ANTES %d | DESPUES %d | auto-aristas tras resolver: %d y %d"
          % (len(a_antes), len(a_desp), auto_a_antes, auto_a_desp))
    print("  (B) aristas resueltas CON LOS DOS EXTREMOS VIVOS")
    print("        ANTES %d | DESPUES %d | auto-aristas tras resolver: %d y %d"
          % (len(b_antes), len(b_desp), auto_b_antes, auto_b_desp))
    print("  DIFERENCIA ENTRE LAS DOS UNIDADES (aristas con un extremo que no resuelve a "
          "un nodo vivo): ANTES %d | DESPUES %d"
          % (len(a_antes) - len(b_antes), len(a_desp) - len(b_desp)))
    print("  DELTA (despues menos antes): (A) %+d | (B) %+d"
          % (len(a_desp) - len(a_antes), len(b_desp) - len(b_antes)))
    print("")

    entran_a = sorted(a_desp - a_antes)
    salen_a = sorted(a_antes - a_desp)
    entran_b = sorted(b_desp - b_antes)
    salen_b = sorted(b_antes - b_desp)

    print("ENTRAN (%d), sobre la unidad (A):" % len(entran_a))
    for par in entran_a:
        print("   + %s" % flecha(par))
    print("SALEN (%d), sobre la unidad (A):" % len(salen_a))
    for par in salen_a:
        print("   - %s" % flecha(par))
    print("")
    mismos = (entran_a == entran_b) and (salen_a == salen_b)
    print("LOS MISMOS CONJUNTOS CON LA UNIDAD (B): %s (entran %d, salen %d)"
          % (mismos, len(entran_b), len(salen_b)))
    if not mismos:
        print("   SOLO EN (A), entran: %s" % [flecha(p) for p in sorted(set(entran_a) - set(entran_b))])
        print("   SOLO EN (B), entran: %s" % [flecha(p) for p in sorted(set(entran_b) - set(entran_a))])
        print("   SOLO EN (A), salen : %s" % [flecha(p) for p in sorted(set(salen_a) - set(salen_b))])
        print("   SOLO EN (B), salen : %s" % [flecha(p) for p in sorted(set(salen_b) - set(salen_a))])
    print("")

    print("ADJUDICACION DE CADA UNA, y ninguna se queda sin nombre:")
    print("  Las que ENTRAN por REDIRECCION DE ALIAS (misma arista, el id del absorbido")
    print("  reescrito al del superviviente): su gemela sale en la lista de SALEN.")
    extremos_salen = set()
    for o, d in salen_a:
        extremos_salen.add(o)
        extremos_salen.add(d)
    extremos_entran = set()
    for o, d in entran_a:
        extremos_entran.add(o)
        extremos_entran.add(d)
    huerfanas_entran = [p for p in entran_a if p[0] not in extremos_salen and p[1] not in extremos_salen]
    huerfanas_salen = [p for p in salen_a if p[0] not in extremos_entran and p[1] not in extremos_entran]
    print("  ARISTAS QUE ENTRAN SIN NINGUNA QUE SALGA COMPARTIENDO UN EXTREMO: %d"
          % len(huerfanas_entran))
    for par in huerfanas_entran:
        print("     + %s" % flecha(par))
    print("  ARISTAS QUE SALEN SIN NINGUNA QUE ENTRE COMPARTIENDO UN EXTREMO: %d"
          % len(huerfanas_salen))
    for par in huerfanas_salen:
        print("     - %s" % flecha(par))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
