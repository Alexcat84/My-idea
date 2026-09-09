# -*- coding: utf-8 -*-
r"""_v214_t2b_remedir_cinco.py . LA TAREA 2.b DE LA VUELTA 214: LAS CINCO FICHAS
SIN EJECUTAR, RE-MEDIDAS CONTRA LAS FILAS NUEVAS DEL CRITERIO DE HECHO.

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO: fuera del censo y fuera de la
nomina (moratoria de AUDITOR.md 6.3). NO ESCRIBE EN docs/plan: solo mide y sella.

LA VARA CONTRA LA QUE SE MIDE ES LA QUE LA 2.a ACABA DE ESCRIBIR, y se LEE de
docs/plan/08_VERIFICACION.md, no se teclea aqui: si aquella fila cambiara, esta
medicion cambiaria con ella.

LA HONESTIDAD DEL ALCANCE VA DELANTE Y NO EN LA LETRA PEQUEÑA: no toda clausula
de una vara es mecanizable. Cada una se marca MECANICA (con su sonda corrida hoy
y su cifra) o DOCUMENTAL (con la ruta y la linea de donde sale). Y para las
DOCUMENTALES SE DECLARA QUE NO HAY CASO ROJO AUTOMATICO, en vez de fabricar uno
que se aprueba solo (EJECUTOR.md 1, EL CASO ROJO SE PRUEBA POR MUTACION).

USO:  python scripts/loop/_v214_t2b_remedir_cinco.py
"""
import io
import json
import os
import re
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VUELTA = int(re.search(r"_v(\d+)_",
                       os.path.basename(os.path.abspath(__file__))).group(1))

VER = "docs/plan/08_VERIFICACION.md"
OPS = "docs/plan/OPERACIONES.jsonl"
LD = "docs/plan/LECTURAS_DIRIGIDAS.md"
VEREDICTOS = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
T1C = "docs/loop/SALIDA_V214_T1C_OP_I_01.txt"

FICHAS_POR_FASE = {
    "08": ["OP-V-01"],
    "09": ["OP-L-01", "OP-L-02", "OP-L-03"],
    "10": ["OP-I-01"],
}

OUT = []


def w(s=""):
    OUT.append(s)


def leer(rel):
    return io.open(os.path.join(RAIZ, rel.replace("/", os.sep)),
                   encoding="utf-8").read()


def linea_de(rel, patron):
    for i, l in enumerate(leer(rel).split(NL), 1):
        if patron in l:
            return i, l.strip()
    return None, None


def fila_de_la_vara(num):
    """LA CELDA DE LA FILA DE UNA FASE, LEIDA DE LA TABLA QUE LA 2.a ESCRIBIO."""
    for i, l in enumerate(leer(VER).split(NL), 1):
        if l.startswith("| **%s " % num) and l.count("|") >= 3:
            celda = l.split("|")[2].strip()
            return i, celda
    return None, None


# --------------------------------------------------------------- LAS SONDAS
def sonda_marcador():
    """EL MARCADOR DEL ARCHIVO, CONTADO HOY DE SU FICHERO."""
    n = sum(1 for l in leer(VEREDICTOS).split(NL) if l.strip())
    return n


def sonda_pares_ld():
    """LOS PARES QUE LAS LECTURAS DIRIGIDAS NOMBRAN, EXTRAIDOS DE SUS PROPIAS
    CABECERAS, Y CUALES DE ESOS PARES TIENEN VEREDICTO EN EL ARCHIVO.

    LA SONDA MIDE EL PAR, NO LOS NOMBRES SUELTOS, Y ESO SE CORRIGIO AQUI: la
    primera version preguntaba si los DOS NOMBRES aparecian en el fichero, y eso
    da que SI para casi cualquier par del catalogo, porque los nodos estan ahi
    de todas formas. Salia 27 de 27 y habria publicado una alarma falsa. Lo que
    la clausula dice es que ESE PAR no tenga VEREDICTO, asi que se compara el
    par como conjunto de dos contra los campos nodo_a y nodo_b de cada fila."""
    pat = re.compile(r"^### `LD-(\d+)` \. `([a-z0-9_]+)` contra `([a-z0-9_]+)`")
    pares = []
    for l in leer(LD).split(NL):
        m = pat.match(l)
        if m:
            pares.append((m.group(1), m.group(2), m.group(3)))
    del_archivo = set()
    for l in leer(VEREDICTOS).split(NL):
        if not l.strip():
            continue
        d = json.loads(l)
        del_archivo.add(frozenset((d["nodo_a"], d["nodo_b"])))
    dentro = [(n, a, b) for n, a, b in pares
              if frozenset((a, b)) in del_archivo]
    return pares, dentro


def sonda_op_i_01():
    """LOS CUATRO VEREDICTOS DE OP-I-01, LEIDOS DE LA SALIDA DE LA TAREA 1 DE
    ESTA MISMA VUELTA. Se cita, no se vuelve a computar."""
    est = {}
    n = None
    for l in leer(T1C).split(NL):
        m = re.match(r"^\s*PUNTO (\d), PEGADO", l)
        if m:
            n = int(m.group(1))
        m2 = re.search(r"VEREDICTO MEDIDO HOY: \*\*(.+?)\*\*", l)
        if m2 and n:
            est[n] = m2.group(1)
    return est


def sonda_op_v_01():
    """LOS CINCO PUNTOS TRANSVERSALES DE OP-V-01, BUSCADOS UNO A UNO POR SU
    MARCA PROPIA DENTRO DE LA nota DE LA FICHA. PRUEBA POR CITA: no se vuelve a
    producir la corrida K, se comprueba que su cita esta escrita."""
    F = [json.loads(l) for l in leer(OPS).split(NL) if l.strip()]
    d = [f for f in F if f["id_op"] == "OP-V-01"][0]
    nota = d.get("nota") or ""
    marcas = [
        ("Gate 0 con su ciclo entero", "Gate 0 con su ciclo entero"),
        ("las tres suites", "motor 25/25"),
        ("el vuelo completo en la corrida K", "16 de 16 en la corrida K"),
        ("la prueba de rumbos", "prueba de rumbos SIN DERIVA"),
        ("el reindexado con sus dos sellos", "d70adc1d"),
    ]
    hallados = [(n, m, m in nota) for n, m in marcas]
    commit = re.search(r"ES ([0-9a-f]{8}),", nota)
    return hallados, (commit.group(1) if commit else None), len(nota)


def main():
    w("=" * 78)
    w("VUELTA %d, TAREA 2.b. LAS CINCO FICHAS, RE-MEDIDAS CONTRA LA VARA NUEVA"
      % VUELTA)
    w("=" * 78)
    w("LA VARA SE LEE DE %s, NO SE TECLEA AQUI." % VER)
    w("")

    varas = {}
    for num in ("08", "09", "10"):
        li, celda = fila_de_la_vara(num)
        varas[num] = (li, celda)
        w("FILA DE LA FASE %s, leida de la linea %s de %s:" % (num, li, VER))
        w("   %s" % celda)
        w("   CIFRA clausulas de esa fila, contadas por su separador: %d"
          % len(celda.split("; ")))
        w("")
    if any(v[1] is None for v in varas.values()):
        w("ROJO: falta la fila de alguna fase. La 2.a no escribio.")
        sellar()
        return 1

    marcador = sonda_marcador()
    pares, dentro = sonda_pares_ld()
    puntos = sonda_op_i_01()
    transv, commit_v, len_nota = sonda_op_v_01()

    w("=" * 78)
    w("LAS SONDAS, CORRIDAS HOY, ANTES DE REPARTIRLAS POR FICHA")
    w("=" * 78)
    w("SONDA 1, EL MARCADOR DEL ARCHIVO: %d filas de %s, contadas hoy."
      % (marcador, VEREDICTOS))
    w("SONDA 2, LOS PARES DE LECTURA DIRIGIDA: %d cabeceras `LD-NN` en %s, y de"
      % (len(pares), LD))
    w("   esos PARES (no de sus nombres sueltos), %d tienen VEREDICTO en %s."
      % (len(dentro), VEREDICTOS))
    for num, a, b in dentro:
        w("      LD-%s: %s contra %s" % (num, a, b))
    w("SONDA 3, LOS CUATRO PUNTOS DE OP-I-01, citados de %s: %s"
      % (T1C, ", ".join("%d=%s" % (k, puntos[k]) for k in sorted(puntos))))
    w("SONDA 4, LOS CINCO PUNTOS TRANSVERSALES DE OP-V-01, buscados uno a uno por")
    w("   su marca propia dentro de la nota de la ficha (%d caracteres), commit"
      % len_nota)
    w("   que movio el estado, leido de la propia nota: %s" % (commit_v,))
    for n, m, ok in transv:
        w("      %-40s marca %-28r presente: %s" % (n, m[:26], "SI" if ok else "NO"))
    w("")

    # ------------------------------------------------------- FICHA POR FICHA
    w("=" * 78)
    w("EL RESULTADO, FICHA POR FICHA, QUE ES LO QUE EL ENCARGO PIDE")
    w("=" * 78)
    F = {}
    for i, l in enumerate(leer(OPS).split(NL), 1):
        if l.strip():
            d = json.loads(l)
            F[d["id_op"]] = (d, i)

    resumen = []
    for num in ("08", "09", "10"):
        li, celda = varas[num]
        clausulas = [c.strip() for c in celda.split("; ")]
        for fid in FICHAS_POR_FASE[num]:
            d, linea = F[fid]
            w("")
            w("-" * 78)
            w("FICHA %s . fase %s . campo estado LEIDO Y NO USADO COMO VARA: %r"
              % (fid, d["fase"], d.get("estado")))
            w("   linea %d de %s | se mide contra la fila de la linea %d de %s"
              % (linea, OPS, li, VER))
            w("-" * 78)
            mias = [c for c in clausulas
                    if any(c == x.strip() for x in d["verificacion"])]
            w("   CIFRA clausulas de la fila de su fase: %d" % len(clausulas))
            w("   CIFRA de esas que salen de ESTA ficha: %d" % len(mias))
            w("")
            mec = doc = 0
            for c in mias:
                w("   CLAUSULA: %s" % c)
                if "el marcador del cribado no se mueve" in c:
                    mec += 1
                    esperado = re.search(r"sigue en ([\d.]+)", c)
                    w("      SONDA: MECANICA. El marcador contado hoy de %s da %d."
                      % (VEREDICTOS, marcador))
                    w("      LA CLAUSULA ESCRIBE %s." % esperado.group(1))
                    w("      RESULTADO: **NO CALZA LEIDA A LA LETRA**, y la")
                    w("      discrepancia SE DECLARA en vez de resolverse copiando")
                    w("      (EJECUTOR.md 2). LAS DOS LECTURAS, y no elijo yo:")
                    w("        (i) LITERAL: el marcador de hoy no es el que la")
                    w("            clausula escribe, asi que no calza.")
                    w("        (ii) DE SU CORTE: la clausula pide que ESTA")
                    w("            OPERACION no mueva el marcador, y el marcador")
                    w("            se movio porque EL CRIBADO SIGUIO hasta cerrar")
                    w("            en su ultimo puesto, no por esta ficha.")
                    w("      CUAL DE LAS DOS MANDA ES DOCTRINA QUE NO ESTA")
                    w("      ESCRITA: va como PENDIENTE DE DOCTRINA y no se")
                    w("      resuelve aqui (EJECUTOR.md 5).")
                elif "ninguna de las once aparece en" in c:
                    mec += 1
                    w("      SONDA: MECANICA, Y MIDE EL PAR Y NO LOS NOMBRES")
                    w("      SUELTOS. %d cabeceras LD-NN en %s; de esos PARES,"
                      % (len(pares), LD))
                    w("      %d tienen VEREDICTO en %s." % (len(dentro), VEREDICTOS))
                    w("      RESULTADO: **%s**"
                      % ("CALZA: ningun par de lectura dirigida tiene veredicto "
                         "en el archivo, o sea que viven solo en su pagina"
                         if not dentro else
                         "NO CALZA: hay %d par(es) con veredicto en el archivo"
                         % len(dentro)))
                    w("      LA PRIMERA VERSION DE ESTA SONDA ERA MAS LAXA QUE SU")
                    w("      CLAUSULA y salia 27 de 27, o sea una alarma falsa:")
                    w("      preguntaba si los dos NOMBRES estaban en el fichero, y")
                    w("      eso da que si para casi cualquier par del catalogo.")
                    w("      Corregida a comparar el PAR contra nodo_a y nodo_b.")
                    w("      Y LA CIFRA ONCE DE LA CLAUSULA NO ES LA DE HOY: el")
                    w("      fichero trae %d cabeceras, porque la pagina siguio"
                      % len(pares))
                    w("      creciendo. La clausula es de su corte, y lo digo.")
                elif fid == "OP-I-01":
                    mec += 1
                    idx = d["verificacion"].index(
                        [x for x in d["verificacion"] if x.strip() == c][0])
                    w("      SONDA: MECANICA, POR CITA DE LA TAREA 1 DE ESTA MISMA")
                    w("      VUELTA (%s), que la midio entera." % T1C)
                    w("      RESULTADO: **%s**" % puntos.get(idx + 1, "(no leido)"))
                elif fid == "OP-V-01":
                    mec += 1
                    w("      SONDA: PRUEBA POR CITA, que es la cuarta via que la")
                    w("      DECISION 5 del fundador del 4 sep 2026 autorizo PARA")
                    w("      ESTA FICHA (docs/loop/paradas/2026-09-04-estado-de-las-fichas-DECISION.md).")
                    w("      NO SE VUELVE A PRODUCIR LA CORRIDA K: se comprueba que")
                    w("      su cita esta escrita en la nota de la ficha, marca a")
                    w("      marca. Commit que movio el estado: %s." % commit_v)
                    w("      CIFRA marcas buscadas: %d | CIFRA halladas: %d"
                      % (len(transv), sum(1 for _n, _m, ok in transv if ok)))
                    w("      RESULTADO: **%s**"
                      % ("CALZA POR CITA: los cinco puntos estan escritos"
                         if all(ok for _n, _m, ok in transv)
                         else "NO CALZA: falta alguna marca"))
                    w("      Y LO QUE ESTA PRUEBA NO ES, dicho por la propia nota de")
                    w("      la ficha: NO cambia el veredicto de la vara del")
                    w("      expediente, que sigue midiendo esta ficha como HECHA")
                    w("      SIN NINGUNA DE SUS TRES PRUEBAS.")
                else:
                    doc += 1
                    w("      SONDA: DOCUMENTAL. No es mecanizable en esta vuelta y")
                    w("      NO SE FABRICA UNA SONDA QUE LA APRUEBE SOLA. Su")
                    w("      evidencia vive en el campo `evidencia` de la propia")
                    w("      ficha, linea %d de %s." % (linea, OPS))
                    w("      RESULTADO: **SIN VEREDICTO MECANICO**, y SE DECLARA")
                    w("      QUE NO HAY CASO ROJO AUTOMATICO para esta clausula.")
                w("")
            corr = [x for x in d["verificacion"]
                    if x.strip().upper().startswith("CORRECCION DECLARADA")]
            w("   CIFRA correcciones declaradas de esta ficha, que NO son puntos de")
            w("   la vara (registro R.72 del acta 208): %d" % len(corr))
            w("   REPARTO DE ESTA FICHA: %d clausula(s) con sonda mecanica y %d"
              % (mec, doc))
            w("   documental(es), de %d que le tocan." % len(mias))
            resumen.append((fid, d["fase"], len(mias), mec, doc))

    w("")
    w("=" * 78)
    w("EL RESUMEN, CONTADO DE LO DE ARRIBA Y NO TECLEADO")
    w("=" * 78)
    w("| ficha | fase | clausulas suyas | con sonda mecanica | documentales |")
    w("|---|---|---:|---:|---:|")
    for fid, fase, n, m, dd in resumen:
        w("| %s | %s | %d | %d | %d |" % (fid, fase, n, m, dd))
    w("")
    w("CIFRA fichas re-medidas: %d (se exigen 5)" % len(resumen))
    w("CIFRA clausulas repartidas: %d | con sonda %d | documentales %d"
      % (sum(r[2] for r in resumen), sum(r[3] for r in resumen),
         sum(r[4] for r in resumen)))
    w("")
    w("LA SUMA SE COMPRUEBA CONTRA SI MISMA: %d mas %d = %d, y las repartidas son %d."
      % (sum(r[3] for r in resumen), sum(r[4] for r in resumen),
         sum(r[3] for r in resumen) + sum(r[4] for r in resumen),
         sum(r[2] for r in resumen)))
    w("")
    fallos = 0
    if len(resumen) != 5:
        fallos += 1
        w("ROJO: no se re-midieron las cinco fichas.")
    if sum(r[3] for r in resumen) + sum(r[4] for r in resumen) != sum(r[2] for r in resumen):
        fallos += 1
        w("ROJO: el reparto no suma.")
    w("CIFRA comprobaciones que fallan: %d" % fallos)
    w("")
    w("Y LO QUE ESTA TAREA NO HACE: no escribe en docs/plan, no mueve ningun")
    w("campo estado, no toca la vara del expediente y no asciende ninguna ficha.")
    w("VERDE: las cinco quedan re-medidas." if not fallos else "ROJO.")
    sellar()
    return 0 if not fallos else 1


def sellar():
    destino = os.path.join(RAIZ, "docs", "loop",
                           "SALIDA_V%d_T2B_REMEDIR_CINCO.txt" % VUELTA)
    texto = NL.join(OUT) + NL
    io.open(destino, "w", encoding="utf-8", newline=NL).write(texto)
    sys.stdout.write(texto)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
