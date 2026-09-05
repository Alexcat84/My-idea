# -*- coding: utf-8 -*-
r"""vuelta179_tarea2_cobertura_final.py . CUANTOS PARES REALES DE `OP-L-03`
QUEDAN SIN LECTURA, CONTADO Y NO AFIRMADO.

TAREA 2 de la vuelta 179, bloque 2.f. SOLO LECTURA.

POR QUE EXISTE: el reporte iba a publicar "los 18 quedan leidos" como una suma
de cabeza, 8 de la 177 mas 10 de hoy. `EJECUTOR.md` 1 dice que toda cifra del
reporte se reconstruye contando su fichero, asi que se cuenta: se recorren los
pares reales que el instrumento da HOY y se busca cada uno, RESUELTO POR `P.1`,
en el `clases_de_los_pares_por_leer` de su acto.

Y DESDE LA VUELTA 180 (TAREA 3) CADA CIFRA QUE SE PUEDE MOVER DENTRO DE UNA
VUELTA LLEVA SU CORTE PEGADO, cableado donde se genera y no en una frase del
reporte. **TODAS LAS DE ESTE FICHERO SE MUEVEN**, y por eso aqui no hay columna
que separar: las filas del registro de lecturas las escribe la propia vuelta que
lee, y los pares reales dependen de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl`, que la
propia vuelta escribe. La unica que no se mueve dentro de una vuelta de cribado
es la cifra de actos que el instrumento viejo da, que sale de un corte sellado en
la vuelta 15, y va dicho al lado.

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
import verificar_mutaciones_viejas as VMV   # noqa: E402

# EL SELLO DE CORTE, PRESTADO Y NO RE-IMPLEMENTADO (vuelta 180, TAREA 3).
sello = VMV.sello_de_corte

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

    corte = VMV.corte_de_git()
    print("A) LAS DOS FUENTES, MEDIDAS, Y CADA CIFRA CON SU CORTE PEGADO")
    print("   EL CORTE DE TODA ESTA CORRIDA: HEAD %s" % corte)
    print("   CIFRA ficheros de dataset/nodos/ leidos por el resolutor: %s"
          % sello(n_nodos, corte, "ficheros de dataset/nodos/ contados en esta corrida"))
    print("   CIFRA actos que el instrumento da: %d (NO se mueve dentro de una "
          "vuelta: sale del corte sellado en la vuelta 15)" % len(actos))
    print("   CIFRA filas de docs/plan/OP_L_03_LECTURAS.jsonl: %s"
          % sello(len(reg), corte, "filas del registro de lecturas contadas en esta corrida"))
    # EL REPARTO POR VUELTA NO SE TECLEA NI SE LIMITA A DOS VUELTAS: se cuenta
    # del propio registro. Hasta la 179 estaban escritas la 177 y la 179 a mano,
    # y el dia que escriba una tercera vuelta esa lista se quedaba muda.
    por_vuelta_filas = {}
    for d in reg:
        k = d.get("vuelta")
        por_vuelta_filas[k] = por_vuelta_filas.get(k, 0) + 1
    for v in sorted(por_vuelta_filas, key=lambda x: (x is None, x)):
        print("   CIFRA de esas filas escritas por la vuelta %s: %s"
              % (v, sello(por_vuelta_filas[v], corte,
                          "filas de la vuelta %s contadas en esta corrida" % v)))
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
        print("   CIFRA pares con clase escrita por la vuelta %s: %s"
              % (v, sello(len(por_vuelta[v]), corte,
                          "pares con clase de la vuelta %s contados en esta corrida" % v)))
    todas = set().union(*por_vuelta.values()) if por_vuelta else set()
    print("   CIFRA pares distintos con clase escrita, en total: %s"
          % sello(len(todas), corte, "pares con clase contados en esta corrida"))
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
    print("   CIFRA pares reales en todo el backlog: %s"
          % sello(total, corte, "pares reales contados en esta corrida"))
    print("   CIFRA de esos CON lectura escrita en su acto: %s"
          % sello(cubiertos, corte, "pares reales con lectura contados en esta corrida"))
    print("   CIFRA de esos SIN lectura: %s"
          % sello(len(sin), corte, "pares reales sin lectura contados en esta corrida"))
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
