# -*- coding: utf-8 -*-
r"""vuelta179_tarea2_cobertura_final.py . CUANTOS PARES REALES DE `OP-L-03`
QUEDAN SIN LECTURA, CONTADO Y NO AFIRMADO.

TAREA 2 de la vuelta 179, bloque 2.f. SOLO LECTURA.

POR QUE EXISTE: el reporte iba a publicar "los 18 quedan leidos" como una suma
de cabeza, 8 de la 177 mas 10 de hoy. `EJECUTOR.md` 1 dice que toda cifra del
reporte se reconstruye contando su fichero, asi que se cuenta: se recorren los
pares reales que el instrumento da HOY y se busca cada uno, RESUELTO POR `P.1`,
en el `clases_de_los_pares_por_leer` de su acto.

USO:
  python scripts/loop/vuelta179_tarea2_cobertura_final.py
"""
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import backlog_l03_resuelto as B   # noqa: E402
import vuelta166_tarea2_correccion_op_l_01 as T   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REGISTRO = os.path.join(RAIZ, "docs", "plan", "OP_L_03_LECTURAS.jsonl")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("LA COBERTURA FINAL DE OP-L-03, CONTADA (vuelta 179, TAREA 2.f)")
    print("=" * 78)
    print("")

    mapa, n_nodos = T.mapa_de_alias()
    vivos = B.vivos_por_grafo()
    idx = B.veredictos_por_par(mapa)
    actos, _s, _c = B.actos_del_instrumento()
    reg = [json.loads(l) for l in io.open(REGISTRO, encoding="utf-8") if l.strip()]

    print("A) LAS DOS FUENTES, MEDIDAS")
    print("   CIFRA ficheros de dataset/nodos/ leidos por el resolutor: %d" % n_nodos)
    print("   CIFRA actos que el instrumento da: %d" % len(actos))
    print("   CIFRA filas de docs/plan/OP_L_03_LECTURAS.jsonl: %d" % len(reg))
    print("   CIFRA de esas filas escritas por la vuelta 177: %d"
          % sum(1 for d in reg if d.get("vuelta") == 177))
    print("   CIFRA de esas filas escritas por la vuelta 179: %d"
          % sum(1 for d in reg if d.get("vuelta") == 179))
    print("")

    por_acto = {}
    por_vuelta = {}
    for d in reg:
        for k in (d.get("clases_de_los_pares_por_leer") or {}):
            x, y = k.split("|", 1)
            par = frozenset((T.resolver(mapa, x), T.resolver(mapa, y)))
            por_acto.setdefault(d["acto"], set()).add(par)
            por_vuelta.setdefault(d.get("vuelta"), set()).add(par)
    print("B) LAS LECTURAS ESCRITAS, CONTADAS DEL REGISTRO Y RESUELTAS POR P.1")
    for v in sorted(por_vuelta, key=lambda x: (x is None, x)):
        print("   CIFRA pares con clase escrita por la vuelta %s: %d" % (v, len(por_vuelta[v])))
    todas = set().union(*por_vuelta.values()) if por_vuelta else set()
    print("   CIFRA pares distintos con clase escrita, en total: %d" % len(todas))
    print("")

    print("C) LOS PARES REALES DE HOY, BUSCADOS UNO A UNO EN SU ACTO")
    total, cubiertos, sin = 0, 0, []
    for _tam, pares_i, miembros in actos:
        m = B.medir_acto(miembros, pares_i, mapa, vivos, idx)
        n = miembros[0]
        for a, b in m["pares_reales"]:
            total += 1
            par = frozenset((T.resolver(mapa, a), T.resolver(mapa, b)))
            if par in por_acto.get(n, set()):
                cubiertos += 1
            else:
                sin.append((n, a, b))
    print("   CIFRA pares reales en todo el backlog: %d" % total)
    print("   CIFRA de esos CON lectura escrita en su acto: %d" % cubiertos)
    print("   CIFRA de esos SIN lectura: %d" % len(sin))
    for n, a, b in sin:
        print("      SIN LECTURA: acto `%s` | %s + %s" % (n, a, b))
    if not sin:
        print("      (ninguno)")
    print("   LA RESTA: %d con lectura mas %d sin lectura = %d, y los reales son %d. CALZA: %s"
          % (cubiertos, len(sin), cubiertos + len(sin), total,
             "SI" if cubiertos + len(sin) == total else "NO"))
    print("")

    if sin:
        print("ROJO: quedan %d pares reales sin lectura." % len(sin))
        print("FIN")
        return 1
    print("VERDE: los %d pares reales del backlog de OP-L-03 tienen lectura escrita."
          % total)
    print("FIN")
    return 0


if __name__ == "__main__":
    sys.exit(main())
