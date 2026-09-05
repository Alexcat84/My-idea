#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""backlog_l03_resuelto.py . EL BACKLOG DE `OP-L-03` CON EL RESOLUTOR DE `P.1`
PUESTO POR ENCIMA, Y LAS DOS COLUMNAS AL LADO.

NOMBRE ESTABLE Y SIN NUMERO DE VUELTA, como sus hermanos
`cotejar_clon_declarado.py`, `cerrar_reporte.py`, `archivar_reporte.py`,
`aislador_de_ciega.py` y `guarda_commit_dataset.py`: se invoca cada vez que
alguien quiere saber cuanto queda de `OP-L-03`, y NO SE CLONA.

SOLO LECTURA. No escribe nodos, ni veredictos, ni operaciones, ni la ficha.
Imprime.

POR QUE NACE, Y LO ADJUDICA UNA MEDICION Y NO UNA OPINION (acta 177 punto 7.8).
La vuelta 177 leyo los SEIS actos grandes del backlog y encontro que **de 29
pares del tramo, 20 tenian los dos extremos en el mismo nodo**: el acto ya se
habia fundido despues del corte 3.388 del que el instrumento viejo lo saca.
Seguir leyendo contra una lista que sabemos inflada es gastar vueltas en pares
que no existen.

QUE NO TOCA, Y ES LA PRIMERA REGLA DE ESTE FICHERO.
`scripts/loop/backlog_l03_vuelta14.py` NO SE MODIFICA. Es el instrumento que la
nota de la ficha cita y el que sostiene una cifra ADJUDICADA EN LA VUELTA 15 (40
actos, 73 pares). Cambiarlo cambiaria esa cifra por la puerta de atras. Este
fichero **lo corre como subproceso y le pone el resolutor por encima**.

Y POR ESO PUBLICA LAS DOS COLUMNAS AL LADO, NUNCA UNA SOLA: lo que el
instrumento da y lo que queda resuelto. Es la forma de la CORRECCION DECLARADA
del banco 9.10 aplicada a un instrumento: **la cifra vieja no se borra, se le
pone la nueva al lado con su procedencia**.

Y CADA CIFRA QUE SE PUEDE MOVER DENTRO DE UNA VUELTA LLEVA SU CORTE PEGADO,
CABLEADO DONDE SE GENERA Y NO EN UNA FRASE DEL REPORTE (vuelta 180, TAREA 3;
hallazgo del fundador medido en la seccion 6 del acta 179, adjudicado por
`banco 9.21` y por el punto 7.2 del acta 178). EL MOTIVO ESTA MEDIDO Y NO
SUPUESTO: la 179 publico en su 2.a la tabla de tramos con `6/29/8` y `34/44/10`,
CONTADA DE SU FICHERO Y SIENDO VERDAD, y el mismo instrumento corrido despues de
que su propia TAREA 2 escribiera diez lecturas dio `14/39/18` y `26/34/0`. **Las
dos son verdaderas y sin corte no hay manera de saber cual mira que.** El sello
lo compone `sello_de_corte()` de `scripts/loop/verificar_mutaciones_viejas.py`,
que desde la 180 recibe QUE se esta contando para no escribir la palabra `nomina`
sobre una cifra que no lo es.

QUE CIFRAS DE AQUI SE MUEVEN DENTRO DE UNA VUELTA, Y CUALES NO. **SE MUEVEN** las
que dependen de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` (pares con veredicto, y por
tanto pares reales) y las que dependen de `docs/plan/OP_L_03_LECTURAS.jsonl` (el
reparto por tramo entre actos leidos y actos sin mirar): las dos las escribe la
propia campana dentro de la vuelta. **NO SE MUEVEN** dentro de una vuelta de
cribado los actos y los pares que el instrumento viejo da, que salen de un corte
sellado en la vuelta 15. Esa clasificacion es A MANO, va con su motivo, y su
barrido esta en `scripts/loop/vuelta180_tarea3_barrido_de_cortes.py`.

LOS DOS CAMINOS VAN SIEMPRE LOS DOS (`EJECUTOR.md` 9, toda perdida de catalogo
declarada se re-verifica contra el grafo):

  CAMINO 1, EL RESOLUTOR DE `P.1`: `mapa_de_alias()` de
  `scripts/loop/vuelta166_tarea2_correccion_op_l_01.py`, que lee los
  `ids_alias` de cada fichero de `dataset/nodos/` y resuelve cada id hasta su
  destino. Un miembro esta VIVO si se resuelve a si mismo.

  CAMINO 2, EL CAMPO `deprecado` DEL GRAFO: un miembro esta VIVO si el grafo lo
  tiene y su `deprecado` es falso.

CAE EN ROJO (exit 1) SI LOS DOS CAMINOS NO CALZAN EN ALGUN ACTO, NOMBRANDOLO. El
dia que no calcen, eso es lo que hay que mirar y no una cifra agregada.

QUE PUBLICA POR ACTO Y EN TOTAL: miembros escritos, vivos por el resolutor,
vivos por el grafo, si los dos caminos calzan, pares que el instrumento da,
pares reales y pares disueltos.

QUE ES UN PAR REAL, DICHO ANTES DE CONTARLO para que no se pueda elegir despues:
de las parejas de miembros del acto, se descartan (1) las que tras resolver
tienen los DOS EXTREMOS EN EL MISMO NODO, que es lo que significa que el acto ya
se fundio, y (2) las que YA TIENEN VEREDICTO en
`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` **buscado por el par RESUELTO** (`P.1`, sin
excepcion: los ids con los que un acto esta escrito no son siempre los ids con
los que su veredicto se guardo). Lo que queda es un par real.

SU CASO POSITIVO POR MUTACION es
`scripts/loop/vuelta178_tarea2_mutacion_resolutor.py`, sobre un mapa de alias
FABRICADO y no sobre el vivo: un acto cuyos miembros colapsan a uno tiene que dar
CERO pares reales, y si se le quita el alias tienen que volver a salir.

USO:
  python scripts/loop/backlog_l03_resuelto.py
  python scripts/loop/backlog_l03_resuelto.py --minimo 5   (solo los actos grandes)
"""
import argparse
import io
import json
import os
import re
import subprocess
import sys
from itertools import combinations

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI)
import vuelta166_tarea2_correccion_op_l_01 as T   # noqa: E402
import verificar_mutaciones_viejas as VMV   # noqa: E402

NL = chr(10)
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
# EL REGISTRO DONDE OP-L-03 ESCRIBE SUS LECTURAS. Se lee para saber que actos
# YA se leyeron, en vez de teclear una lista que envejeceria a la vuelta siguiente.
REGISTRO = os.path.join(RAIZ, "docs", "plan", "OP_L_03_LECTURAS.jsonl")
PATRON_ACTO = re.compile(r"^\s*\[(\d+),\s*(\d+) pares\]\s*(.+)$")
PATRON_TOTAL = re.compile(r"^BACKLOG DE OP-L-03 AL CORTE ([\d.]+): (\d+) actos, (\d+) pares")

# EL SELLO DE CORTE, PRESTADO Y NO RE-IMPLEMENTADO (vuelta 180, TAREA 3).
# Una segunda copia de la misma frase seria una segunda sede que envejeceria
# sola: se llama a la de siempre, que es PURA y ya tiene su caso positivo por
# mutacion en `scripts/loop/vuelta179_tarea1d_mutacion_corte.py`.
sello = VMV.sello_de_corte


def actos_del_instrumento():
    """LOS ACTOS DEL BACKLOG, LEIDOS DE LA SALIDA DEL INSTRUMENTO QUE LA FICHA
    CITA. Devuelve (lista de (tamano, pares_del_instrumento, [miembros]), salida).

    Se CORRE `scripts/loop/backlog_l03_vuelta14.py` y se parsea su LISTA
    DECLARADA. No se re-implementa su metodo: si el instrumento cambia, esto
    cambia con el, que es lo que `EJECUTOR.md` 2 manda."""
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run([sys.executable, os.path.join(AQUI, "backlog_l03_vuelta14.py")],
                       cwd=RAIZ, capture_output=True, env=env)
    salida = r.stdout.decode("utf-8", errors="replace")
    dentro = False
    actos = []
    for linea in salida.split(NL):
        if "LISTA DECLARADA" in linea:
            dentro = True
            continue
        if dentro:
            if linea.strip().startswith("DISCUTIBLE"):
                break
            m = PATRON_ACTO.match(linea)
            if m:
                miembros = [x.strip() for x in m.group(3).split(",") if x.strip()]
                actos.append((int(m.group(1)), int(m.group(2)), miembros))
    return actos, salida, r.returncode


def vivos_por_grafo(grafo=None):
    """{id: True si el grafo lo tiene y NO esta deprecado}. CAMINO 2."""
    g = grafo if grafo is not None else json.load(io.open(GRAFO, encoding="utf-8"))["nodos"]
    return dict((k, not bool(v.get("deprecado"))) for k, v in g.items())


def veredictos_por_par(mapa, filas=None):
    """{frozenset({a_resuelto, b_resuelto}): [filas]}. `P.1` antes de contar."""
    idx = {}
    for fila in (filas if filas is not None else T.veredictos()):
        a = T.resolver(mapa, fila["nodo_a"])
        b = T.resolver(mapa, fila["nodo_b"])
        idx.setdefault(frozenset((a, b)), []).append(fila)
    return idx


def medir_acto(miembros, pares_del_instrumento, mapa, vivos_grafo, idx):
    """LA MEDICION DE UN ACTO, PURA. Devuelve un dict.

    PURA a proposito: recibe el mapa de alias, el diccionario de vivos y el
    indice de veredictos, para que su caso positivo por mutacion pueda pasarle
    un mapa FABRICADO y comprobar que el resolutor esta puesto de verdad."""
    resueltos = dict((m, T.resolver(mapa, m)) for m in miembros)
    vivos_res = sorted({v for v in resueltos.values()})
    # CAMINO 2: un miembro vive si el grafo lo tiene sin deprecar. Se cuentan los
    # DESTINOS distintos que quedan vivos, para que la cifra sea comparable con
    # la del camino 1, que tambien cuenta destinos y no nombres escritos.
    vivos_gra = sorted({m for m in miembros if vivos_grafo.get(m, False)})
    calzan = (len(vivos_res) == len(vivos_gra))

    # LOS PARES REALES SE CUENTAN POR EL PAR RESUELTO Y NO POR EL PAR ESCRITO, Y
    # ESO IMPORTA. Dos parejas de miembros distintas pueden resolver al MISMO
    # par: si `b` es alias de `a`, entonces `(a, c)` y `(b, c)` son el mismo par
    # una vez resueltos, y hay UNA lectura que hacer, no dos. Contar los escritos
    # inflaria la cifra exactamente por el mismo mecanismo que este fichero viene
    # a desinflar. Lo cazo su propio caso positivo por mutacion en su primera
    # corrida (caso C), y se arregla aqui en vez de ajustarle el esperado.
    reales, disueltos, con_veredicto = [], [], []
    vistos_reales, vistos_con = set(), set()
    for a, b in combinations(sorted(miembros), 2):
        ra, rb = resueltos[a], resueltos[b]
        if ra == rb:
            disueltos.append((a, b, ra))
            continue
        clave = frozenset((ra, rb))
        if clave in idx:
            if clave not in vistos_con:
                vistos_con.add(clave)
                con_veredicto.append((a, b))
            continue
        if clave not in vistos_reales:
            vistos_reales.add(clave)
            reales.append((a, b))
    return {
        "miembros": sorted(miembros),
        "cifra_miembros": len(miembros),
        "vivos_por_resolutor": vivos_res,
        "cifra_vivos_por_resolutor": len(vivos_res),
        "vivos_por_grafo": vivos_gra,
        "cifra_vivos_por_grafo": len(vivos_gra),
        "los_dos_caminos_calzan": calzan,
        "pares_del_instrumento": pares_del_instrumento,
        "cifra_pares_posibles": len(list(combinations(miembros, 2))),
        "cifra_pares_disueltos": len(disueltos),
        "cifra_pares_con_veredicto": len(con_veredicto),
        "cifra_pares_reales": len(reales),
        "pares_reales": reales,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--minimo", type=int, default=0,
                    help="solo los actos de este tamano de miembros o mas. Por "
                         "defecto 0, o sea TODOS: la cifra que hay que publicar "
                         "es la del backlog entero.")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    p = print

    p("=" * 78)
    p("EL BACKLOG DE OP-L-03, CON EL RESOLUTOR DE P.1 POR ENCIMA")
    p("=" * 78)
    p("")

    corte = VMV.corte_de_git()
    p("A) EL INSTRUMENTO VIEJO, CORRIDO Y NO CITADO DE MEMORIA")
    p("   instrumento: scripts/loop/backlog_l03_vuelta14.py (NO SE TOCA)")
    p("   EL CORTE DE TODA ESTA CORRIDA: HEAD %s" % corte)
    actos, salida, codigo = actos_del_instrumento()
    p("   exit del instrumento: %d" % codigo)
    tot = PATRON_TOTAL.search(salida)
    if tot:
        p("   su linea de total, pegada: BACKLOG DE OP-L-03 AL CORTE %s: %s actos, "
          "%s pares" % (tot.group(1), tot.group(2), tot.group(3)))
    p("   CIFRA actos que su LISTA DECLARADA trae: %d (NO se mueve dentro de una "
      "vuelta: sale del corte sellado en la vuelta 15)" % len(actos))
    p("   CIFRA pares que el instrumento da, sumados de su lista: %d (NO se mueve "
      "dentro de una vuelta: sale del mismo corte)" % sum(x[1] for x in actos))
    if not actos:
        p("   ROJO: el instrumento viejo no da ningun acto. Sin universo no hay nada")
        p("         que resolver, y este fichero no inventa uno.")
        p("FIN")
        return 1
    p("")

    p("B) EL RESOLUTOR Y EL GRAFO, PUESTOS ANTES DE CONTAR NINGUN PAR")
    mapa, n_nodos = T.mapa_de_alias()
    vivos_grafo = vivos_por_grafo()
    filas_v = T.veredictos()
    idx = veredictos_por_par(mapa)
    p("   CAMINO 1, resolutor P.1: mapa_de_alias() de "
      "scripts/loop/vuelta166_tarea2_correccion_op_l_01.py")
    p("      CIFRA ficheros de dataset/nodos/ leidos: %s"
      % sello(n_nodos, corte, "ficheros de dataset/nodos/ contados en esta corrida"))
    p("      CIFRA alias del mapa: %s"
      % sello(len(mapa), corte, "alias del resolutor contados en esta corrida"))
    p("   CAMINO 2, campo deprecado del grafo: dataset/metadata/master_graph.json")
    p("      CIFRA nodos del grafo: %s"
      % sello(len(vivos_grafo), corte, "nodos del grafo contados en esta corrida"))
    p("      CIFRA nodos VIVOS (deprecado falso): %s"
      % sello(sum(1 for v in vivos_grafo.values() if v), corte,
              "nodos vivos contados en esta corrida"))
    p("   CIFRA filas de docs/INTRA_DOMINIO_VEREDICTOS.jsonl: %s"
      % sello(len(filas_v), corte, "filas del archivo contadas en esta corrida"))
    p("   CIFRA pares distintos tras resolver: %s"
      % sello(len(idx), corte, "pares distintos tras resolver contados en esta corrida"))
    p("")

    elegidos = [x for x in actos if x[0] >= a.minimo]
    p("C) LA MEDICION, ACTO POR ACTO Y CON LAS DOS COLUMNAS AL LADO")
    p("   --minimo %d, o sea %d actos de los %d que da el instrumento"
      % (a.minimo, len(elegidos), len(actos)))
    p("")
    p("| acto (primer miembro) | miembros | vivos por resolutor | vivos por grafo | "
      "calzan | pares del instrumento | pares reales | pares disueltos |")
    p("|---|---|---|---|---|---|---|---|")
    medidas = []
    for tam, pares_i, miembros in elegidos:
        m = medir_acto(miembros, pares_i, mapa, vivos_grafo, idx)
        medidas.append((miembros[0], m))
        p("| `%s` | %d | %d | %d | %s | %d | %d | %d |"
          % (miembros[0], m["cifra_miembros"], m["cifra_vivos_por_resolutor"],
             m["cifra_vivos_por_grafo"],
             "SI" if m["los_dos_caminos_calzan"] else "**NO**",
             m["pares_del_instrumento"], m["cifra_pares_reales"],
             m["cifra_pares_disueltos"]))
    p("")

    no_calzan = [(n, m) for n, m in medidas if not m["los_dos_caminos_calzan"]]
    p("D) LOS DOS CAMINOS, COTEJADOS ACTO POR ACTO")
    p("   CIFRA actos medidos: %d (NO se mueve dentro de una vuelta: sale del "
      "corte sellado en la vuelta 15)" % len(medidas))
    p("   CIFRA actos donde los dos caminos CALZAN: %s"
      % sello(sum(1 for _n, m in medidas if m["los_dos_caminos_calzan"]), corte,
              "actos donde los dos caminos calzan contados en esta corrida"))
    p("   CIFRA actos donde NO calzan: %s"
      % sello(len(no_calzan), corte, "actos donde no calzan contados en esta corrida"))
    for nombre, m in no_calzan:
        p("      NO CALZAN en `%s`: resolutor dice %d vivos (%s) y el grafo dice %d "
          "(%s)" % (nombre, m["cifra_vivos_por_resolutor"],
                    ", ".join(m["vivos_por_resolutor"]),
                    m["cifra_vivos_por_grafo"], ", ".join(m["vivos_por_grafo"])))
    p("")

    ins = sum(m["pares_del_instrumento"] for _n, m in medidas)
    rea = sum(m["cifra_pares_reales"] for _n, m in medidas)
    dis = sum(m["cifra_pares_disueltos"] for _n, m in medidas)
    con = sum(m["cifra_pares_con_veredicto"] for _n, m in medidas)
    pos = sum(m["cifra_pares_posibles"] for _n, m in medidas)
    p("E) EL TOTAL, CON LAS DOS COLUMNAS Y SIN BORRAR LA VIEJA")
    p("   EL CORTE DE ESTA TABLA, CABLEADO DONDE SE GENERA: HEAD %s" % corte)
    p("")
    p("| cifra | valor | se mueve dentro de una vuelta |")
    p("|---|---|---|")
    p("| actos que el instrumento da | **%d** | no, sale del corte sellado en la vuelta 15 |"
      % len(medidas))
    p("| pares POSIBLES entre los miembros escritos | **%d** | no, sale del mismo corte |" % pos)
    p("| PARES QUE EL INSTRUMENTO DA (la cifra vieja, que no se borra) | **%d** | no, sale del mismo corte |" % ins)
    p("| pares DISUELTOS (los dos extremos en el mismo nodo tras resolver) | **%s** | SI, depende del resolutor de dataset/ |"
      % sello(dis, corte, "pares disueltos contados en esta corrida"))
    p("| pares que YA TIENEN VEREDICTO buscados por el par RESUELTO | **%s** | SI, depende de docs/INTRA_DOMINIO_VEREDICTOS.jsonl |"
      % sello(con, corte, "pares con veredicto contados en esta corrida"))
    p("| PARES REALES (la cifra nueva, al lado de la vieja) | **%s** | SI, es la resta de las dos de arriba |"
      % sello(rea, corte, "pares reales contados en esta corrida"))
    p("| actos SIN NINGUN PAR REAL | **%s** | SI, se mueve con los pares reales |"
      % sello(sum(1 for _n, m in medidas if m["cifra_pares_reales"] == 0), corte,
              "actos sin ningun par real contados en esta corrida"))
    p("")
    if ins:
        p("   LO QUE SOBRA, EN CRUDO: de los %d pares que el instrumento da, quedan"
          % ins)
        p("   %d reales. SOBRAN %d, que es el %.1f por ciento."
          % (rea, ins - rea, 100.0 * (ins - rea) / ins))
    p("")

    p("F) LO QUE SOBRA EN LOS ACTOS QUE TODAVIA NO SE HAN LEIDO")
    p("   (los leidos NO se teclean: se cuentan del registro")
    p("   docs/plan/OP_L_03_LECTURAS.jsonl, que es donde OP-L-03 escribe)")
    leidos = set()
    if os.path.exists(REGISTRO):
        for linea in io.open(REGISTRO, encoding="utf-8"):
            if linea.strip():
                leidos.add(json.loads(linea).get("acto"))
    p("   CIFRA actos que el registro dice leidos: %s"
      % sello(len(leidos), corte, "actos que el registro dice leidos, contados en esta corrida"))
    p("   CIFRA de esos que el instrumento sigue dando: %s"
      % sello(sum(1 for n, _m in medidas if n in leidos), corte,
              "de esos, los que el instrumento sigue dando, contados en esta corrida"))
    p("")
    # EL CORTE DE LA TABLA DE TRAMOS, CABLEADO DONDE SE GENERA LA TABLA Y NO EN
    # UNA FRASE DEL REPORTE (vuelta 180, TAREA 3). ESTA TABLA ES LA QUE SE MOVIO
    # DENTRO DE LA 179 y la que el fundador midio en la seccion 6 de su acta: sus
    # tres columnas de la izquierda dependen de quien haya escrito en
    # docs/plan/OP_L_03_LECTURAS.jsonl, y ese fichero lo escribe la propia vuelta.
    p("   EL CORTE DE ESTA TABLA, CABLEADO DONDE SE GENERA: HEAD %s" % corte)
    p("   TODA FILA DE ESTA TABLA SE MUEVE DENTRO DE UNA VUELTA: el reparto entre")
    p("   `YA LEIDOS` y `SIN LEER` sale del registro de lecturas, que la campana")
    p("   escribe mientras lee, y los pares reales salen del archivo de veredictos.")
    p("")
    p("| tramo | actos | pares del instrumento | pares reales | pares disueltos | sobran | corte |")
    p("|---|---|---|---|---|---|---|")
    for etiqueta, filtro in (("YA LEIDOS (la 177)", True), ("SIN LEER", False)):
        sub = [(n, m) for n, m in medidas if (n in leidos) == filtro]
        s_ins = sum(m["pares_del_instrumento"] for _n, m in sub)
        s_rea = sum(m["cifra_pares_reales"] for _n, m in sub)
        s_dis = sum(m["cifra_pares_disueltos"] for _n, m in sub)
        p("| %s | **%d** | **%d** | **%d** | **%d** | **%d** | HEAD %s |"
          % (etiqueta, len(sub), s_ins, s_rea, s_dis, s_ins - s_rea, corte))
    p("| **todos** | **%d** | **%d** | **%d** | **%d** | **%d** | HEAD %s |"
      % (len(medidas), ins, rea, dis, ins - rea, corte))
    p("")
    p("   LA MISMA TABLA, CON EL SELLO ENTERO EN CADA CIFRA QUE SE MUEVE:")
    for etiqueta, filtro in (("YA LEIDOS (la 177)", True), ("SIN LEER", False)):
        sub = [(n, m) for n, m in medidas if (n in leidos) == filtro]
        p("      %-20s actos %s" % (etiqueta, sello(len(sub), corte,
          "actos del tramo %s contados en esta corrida" % etiqueta)))
        p("      %-20s pares reales %s" % ("", sello(
            sum(m["cifra_pares_reales"] for _n, m in sub), corte,
            "pares reales del tramo %s contados en esta corrida" % etiqueta)))
    p("")

    if no_calzan:
        p("ROJO: los dos caminos NO CALZAN en %d acto(s), nombrados arriba. Una cifra"
          % len(no_calzan))
        p("      agregada sobre un acto donde el resolutor y el grafo se contradicen")
        p("      no vale nada: eso es lo que hay que mirar, y no el total.")
        p("FIN")
        return 1
    p("VERDE: los dos caminos calzan en los %d actos medidos. El instrumento viejo "
      "da %d pares y quedan %d reales, con %d disueltos y %d ya con veredicto. LAS "
      "DOS COLUMNAS VAN LAS DOS Y LA VIEJA NO SE BORRA."
      % (len(medidas), ins, rea, dis, con))
    p("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
