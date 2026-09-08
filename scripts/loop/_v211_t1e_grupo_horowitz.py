# -*- coding: utf-8 -*-
r"""_v211_t1e_grupo_horowitz.py . TAREA 1.e DE LA VUELTA 211: LA MEDICION QUE NO
ARREGLA NADA. **CONTAR, Y NADA MAS** (hallazgo `7.1` del acta 210, linea 74223
de `docs/loop/ACTA_AUDITOR.md`).

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO, fuera del censo y fuera de la
nomina (moratoria de `AUDITOR.md` 6.3). **NO TOCA NI UN NODO**: abre el grafo en
lectura y no escribe en el jamas.

QUE MIDE, y son las tres preguntas del encargo y ninguna mas:

  (a) si `posicionamiento_de_empresa` aparece en `docs/plan/02_DESTEJIDOS.md` y en
      que operacion de `docs/plan/OPERACIONES.jsonl` vive;
  (b) si los otros injertos del grupo HOROWITZ estan en el mismo estado, o sea si
      su segundo bloque sigue DENTRO del nodo o ya vive APARTE, con la particion
      publicada por nombre;
  (c) si la particion NO es uniforme, decirlo y **parar ahi**.

LA VARA DE LA PARTICION, Y NO ES MIA. La tabla de `docs/plan/01_FUENTES.md`,
lineas **1462 a 1477**, publica por nodo **los libros declarados y la frontera
leida** (`1 a 5 / 6 a 9`, etc.) medida el 11 y el 14 ago 2026. De esa frontera
salen dos cifras por nodo **sin teclear ninguna**: el ultimo paso del BLOQUE 1 y
el ultimo paso del NODO ENTERO. Contra ellas se pone la CIFRA de
`pasos_accionables` que el nodo tiene HOY en `dataset/metadata/master_graph.json`:

  - hoy == total de la frontera   -> **EL BLOQUE SIGUE DENTRO**
  - hoy == fin del bloque 1       -> **EL BLOQUE YA VIVE APARTE**
  - cualquier otra cifra          -> **NI UNA COSA NI LA OTRA, y se declara**

**LA TABLA SE LEE DEL FICHERO, NO SE TECLEA** (`EJECUTOR.md` 1, LA TABLA SE
IMPRIME, NO SE TECLEA). Si el barrido no encuentra la tabla, o encuentra un
numero de filas distinto del que hay en el campo `nodos` de la operacion, el
computo lo dice y no inventa.

**EL CASO ROJO SE PRUEBA POR MUTACION** (`EJECUTOR.md` 1). `--mutar` corre el
mismo computo desplazando en uno el fin del bloque 1 de cada fila, y exige que la
particion CAMBIE. Si sale igual, la comparacion no compara nada.
"""
import argparse
import io
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))

FUENTES = os.path.join(RAIZ, "docs", "plan", "01_FUENTES.md")
DESTEJIDOS = os.path.join(RAIZ, "docs", "plan", "02_DESTEJIDOS.md")
OPS = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
GRAFO = os.path.join(RAIZ, "dataset", "metadata", "master_graph.json")
NODO_DEL_HALLAZGO = "posicionamiento_de_empresa"
TABLA_DESDE, TABLA_HASTA = 1462, 1477


def lf(ruta):
    return io.open(ruta, "rb").read().replace(b"\r\n", b"\n").decode("utf-8")


def filas_de_la_tabla():
    """LA TABLA DE LOS INJERTOS DE HOROWITZ, BARRIDA DE 01_FUENTES.md Y NO
    TECLEADA. Devuelve (numero de fila, nodo, libros, tramos) por fila."""
    lineas = lf(FUENTES).split(NL)
    out = []
    for n in range(TABLA_DESDE, TABLA_HASTA + 1):
        cruda = lineas[n - 1]
        if not cruda.startswith("|"):
            continue
        # LA CELDA DE LIBROS LLEVA PIPES ESCAPADOS (`Wasserman \| Horowitz`), y
        # partir por "|" a secas los toma por separadores y corre las columnas
        # una plaza. CAIDA PROPIA DE ESTA VUELTA, cazada porque la corrida dio
        # CATORCE filas SIN FRONTERA LEGIBLE y aun asi se llamo uniforme.
        celdas = [c.replace(chr(0), "|").strip() for c in
                  cruda.strip().strip("|").replace("\\|", chr(0)).split("|")]
        if len(celdas) < 5 or not celdas[0].isdigit():
            continue
        nodo = celdas[1].strip("*` ").replace("`", "")
        libros = celdas[2]
        tramos = [(int(a), int(b))
                  for a, b in re.findall(r"(\d+)\s+a\s+(\d+)", celdas[3])]
        out.append((int(celdas[0]), n, nodo, libros, tramos, celdas[4]))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutar", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append

    def cerrar(codigo):
        salida = NL.join(L) + NL
        print(salida)
        nombre = "T1E_GRUPO_HOROWITZ" + ("_MUTADO" if a.mutar else "")
        io.open(os.path.join(LOOP, "SALIDA_V%d_%s.txt" % (VUELTA, nombre)),
                "w", encoding="utf-8", newline=NL).write(salida)
        return codigo

    w("=" * 78)
    w("VUELTA %d, TAREA 1.e: EL GRUPO HOROWITZ, CONTADO. NO SE TOCA NI UN NODO."
      % VUELTA)
    if a.mutar:
        w("*** CORRIDA MUTADA: el fin del bloque 1 de cada fila se desplaza en +1")
        w("*** a proposito. SE EXIGE QUE LA PARTICION CAMBIE.")
    w("=" * 78)
    w("")

    w("(a.1) EL NODO DEL HALLAZGO 7.1 EN docs/plan/02_DESTEJIDOS.md")
    texto_d = lf(DESTEJIDOS)
    menciones = texto_d.count(NODO_DEL_HALLAZGO)
    w("   CIFRA menciones de %r en 02_DESTEJIDOS.md: %d"
      % (NODO_DEL_HALLAZGO, menciones))
    w("   contraste del encargo: 0")
    w("   CALZA: %s" % ("SI" if menciones == 0 else "NO, Y LA DISCREPANCIA SE DECLARA"))
    if menciones:
        for i, l in enumerate(texto_d.split(NL), 1):
            if NODO_DEL_HALLAZGO in l:
                w("      linea %d: %s" % (i, l[:150]))
    w("")

    w("(a.2) EN QUE OPERACION DE docs/plan/OPERACIONES.jsonl VIVE")
    texto_o = lf(OPS)
    vive_en = []
    total_fichas = 0
    for i, l in enumerate(texto_o.split(NL), 1):
        if not l.strip():
            continue
        total_fichas += 1
        d = json.loads(l)
        if NODO_DEL_HALLAZGO in (d.get("nodos") or []):
            vive_en.append((i, d))
    w("   CIFRA fichas barridas: %d" % total_fichas)
    w("   CIFRA operaciones cuyo campo nodos lo contiene: %d" % len(vive_en))
    w("   contraste del encargo: 1")
    for i, d in vive_en:
        w("      linea %d | id_op %s | tipo %s | estado %r | fase %s"
          % (i, d["id_op"], d.get("tipo"), d.get("estado"), d.get("fase")))
        w("         CIFRA nodos del campo: %d" % len(d.get("nodos") or []))
        w("         adjudicacion (primeros 90): %s"
          % (d.get("adjudicacion") or "")[:90])
    w("")

    if len(vive_en) != 1:
        w("   ROJO: no hay UNA sola operacion. Se declara y se para.")
        return cerrar(1)
    op = vive_en[0][1]
    nodos_op = list(op.get("nodos") or [])

    w("(a.3) LA CIFRA DE NODOS DE LA OPERACION, CONTADA HOY CONTRA SU CONTRASTE")
    w("   CIFRA nodos del campo `nodos` de %s, contada hoy: %d"
      % (op["id_op"], len(nodos_op)))
    w("   contraste del encargo: 13")
    w("   contraste de la propia adjudicacion de la ficha: la frase LEIDOS LOS 13")
    w("   CALZAN: %s"
      % ("SI" if len(nodos_op) == 13 else "NO, Y LA DISCREPANCIA SE DECLARA SIN RESOLVERLA"))
    w("")

    w("(b) LA VARA DE LA PARTICION, BARRIDA DE docs/plan/01_FUENTES.md")
    w("    lineas %d a %d, y NO TECLEADA" % (TABLA_DESDE, TABLA_HASTA))
    filas = filas_de_la_tabla()
    w("   CIFRA filas leidas de la tabla: %d" % len(filas))
    w("   CIFRA nodos del campo `nodos` de la operacion: %d" % len(nodos_op))
    en_tabla = set(f[2] for f in filas)
    en_campo = set(nodos_op)
    w("   CIFRA nodos de la tabla que NO estan en el campo: %d %s"
      % (len(en_tabla - en_campo), sorted(en_tabla - en_campo)))
    w("   CIFRA nodos del campo que NO estan en la tabla: %d %s"
      % (len(en_campo - en_tabla), sorted(en_campo - en_tabla)))
    w("")

    G = json.load(io.open(GRAFO, encoding="utf-8"))
    N = G["nodos"]
    w("   CIFRA nodos del grafo: %d (total_nodos declarado: %s)"
      % (len(N), G.get("total_nodos")))
    w("")

    w("(b) LA PARTICION, NODO POR NODO Y CON SUS NOMBRES")
    w("")
    w("| # | nodo | frontera leida | fin bloque 1 | total de la frontera | pasos HOY | veredicto |")
    w("|---:|---|---|---:|---:|---:|---|")
    reparto = {}
    detalle = []
    for num, linea_tabla, nodo, libros, tramos, _bloque in filas:
        if not tramos:
            veredicto = "SIN FRONTERA LEGIBLE"
            fin1 = total = None
            hoy = None
        else:
            fin1 = tramos[0][1]
            total = tramos[-1][1]
            if a.mutar:
                fin1 = fin1 + 1
            n = N.get(nodo)
            hoy = None if n is None else len(n.get("pasos_accionables") or [])
            if n is None:
                veredicto = "EL NODO NO ESTA EN EL GRAFO"
            elif hoy == total:
                veredicto = "EL BLOQUE SIGUE DENTRO"
            elif hoy == fin1:
                veredicto = "EL BLOQUE YA VIVE APARTE"
            else:
                veredicto = "NI UNA COSA NI LA OTRA"
        reparto[veredicto] = reparto.get(veredicto, 0) + 1
        detalle.append((num, nodo, veredicto, hoy, fin1, total, linea_tabla, libros))
        frontera = " / ".join("%d a %d" % t for t in tramos) if tramos else "(ninguna)"
        w("| %d | `%s` | %s | %s | %s | %s | **%s** |"
          % (num, nodo, frontera, fin1, total, hoy, veredicto))
    w("")

    w("(b) EL REPARTO, CONTADO DE LA TABLA DE ARRIBA")
    for k in sorted(reparto):
        w("   %-28s %d nodo(s)" % (k, reparto[k]))
    w("   CIFRA nodos repartidos: %d" % sum(reparto.values()))
    w("")
    for k in sorted(reparto):
        w("   %s:" % k)
        for num, nodo, v, hoy, fin1, total, lt, libros in detalle:
            if v == k:
                w("      %2d. %-42s pasos hoy %s (bloque 1 acaba en %s, frontera entera %s)"
                  % (num, nodo, hoy, fin1, total))
    w("")

    # LA GUARDA CONTRA EL FALSO VERDE, Y NACE DE UNA CAIDA DE ESTA MISMA VUELTA:
    # con el barrido roto las CATORCE filas cayeron en un solo cubo, SIN FRONTERA
    # LEGIBLE, y "un solo cubo" se leyo como PARTICION UNIFORME. Un reparto que
    # no pudo medir nada NO es uniforme: es un reparto que no existe.
    sin_medir = sum(v for k, v in reparto.items()
                    if k in ("SIN FRONTERA LEGIBLE", "EL NODO NO ESTA EN EL GRAFO"))
    w("   CIFRA nodos que NO se pudieron medir: %d (se exige 0)" % sin_medir)
    if sin_medir:
        w("   ROJO: con nodos sin medir la palabra UNIFORME no se escribe.")
        w("")
        w("FIN")
        return cerrar(1)

    uniforme = len(reparto) == 1
    w("(c) LA PARTICION ES UNIFORME: %s" % ("SI" if uniforme else "NO"))
    if not uniforme:
        w("   EL ENCARGO MANDA PARAR AQUI: decidir que hacer con una operacion de")
        w("   fuente sin destino NO ES DE ESTA VUELTA. Se mide, se publica y se para.")
    w("")

    if a.mutar:
        w("LO QUE LA MUTACION EXIGE: que este reparto NO sea el de la corrida limpia.")
        w("   reparto con el dato mutado: %s"
          % ", ".join("%s=%d" % (k, reparto[k]) for k in sorted(reparto)))
        w("   (se coteja a mano contra la corrida limpia, que se corre primero)")
    w("")
    w("FIN")
    return cerrar(0)


if __name__ == "__main__":
    raise SystemExit(main())
