# -*- coding: utf-8 -*-
r"""_v208_t2_denominador.py . TAREA 2.a DE LA VUELTA 208: EL DENOMINADOR DE LAS
DOS NOMINAS, RECOMPUTADO DE SU NOMINA DE MIEMBROS Y NO DE LA TABLA.

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO, fuera del censo y fuera de la
nomina de la bateria (moratoria de `AUDITOR.md` 6.3). No escribe nada en ninguna
sede: SOLO MIDE. Las dos filas las escribe el 2.b, en otro fichero.

POR QUE VA PRIMERO, Y NO ES DE ADORNO (hallazgo `7.2` del acta 207 y su
adjudicacion `6.3`): en la JUNTA ASESORA las dos fuentes dicen 6 posibles y solo
discrepan en los leidos, o sea que es la tabla sin refrescar; pero en la SELECCION
DE CANAL la mesa cuenta sobre 10 y la tabla sobre 15, y ahi los DENOMINADORES no
coinciden. Escribir los leidos sobre un denominador sin comprobar seria arreglar
la mitad visible.

EL RESOLUTOR VA PUESTO (`EJECUTOR.md` 9 y `P.1`): todo conteo que toque ids pasa
por el resolutor antes de contar. `mapa_de_alias()` y `resolver()` se IMPORTAN de
`vuelta166_tarea2_correccion_op_l_01.py`, que es su sede. IMPORTAR NO ES CLONAR.

DE DONDE SALE CADA NOMINA, Y SE CITA CON FICHERO Y LINEA:
  . junta asesora   -> `docs/INTRA_DOMINIO_INFORME.md`, la fila `miembros` de la
                       seccion LA NOMINA DE LA JUNTA ASESORA.
  . seleccion canal -> `docs/INTRA_DOMINIO_INFORME.md`, la tabla de miembros de
                       la seccion RACIMO NUEVO: LA SELECCION DE CANAL, **con su
                       CORRECCION DECLARADA del 11 ago 2026 leida**, que dice
                       `son SEIS y no cinco`.

LA GUARDA QUE PUEDE CAER: si el patron no encuentra la seccion, o no encuentra
miembros, se DICE `EL PATRON NO ENCONTRO NADA` y NO se publica un cero. Un cero de
un patron no es un hecho del mundo (`EJECUTOR.md` 9).
"""
import argparse
import io
import itertools
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

sys.path.insert(0, AQUI)
from vuelta166_tarea2_correccion_op_l_01 import (  # noqa: E402
    mapa_de_alias, resolver, CABECERA_LD)

VUELTA = 208
INFORME = os.path.join(RAIZ, "docs", "INTRA_DOMINIO_INFORME.md")
BANCO = os.path.join(RAIZ, "docs", "BANCO_DE_TEXTOS.md")
LECTURAS = os.path.join(RAIZ, "docs", "plan", "LECTURAS_DIRIGIDAS.md")
NODOS = os.path.join(RAIZ, "dataset", "nodos")

# LAS DOS NOMINAS, CON EL TITULO LITERAL DE LA SECCION DEL INFORME DE LA QUE SALE
# CADA UNA. EL TITULO SE COMPRUEBA ANTES DE CONTAR: si no calza, no se cuenta.
NOMINAS = [
    ("junta asesora",
     "#### LA NOMINA DE LA JUNTA ASESORA",
     "| miembros |"),
    ("seleccion de canal",
     "## 10. RACIMO NUEVO: LA SELECCION DE CANAL",
     None),
]

# LAS FILAS DE LA TABLA VIVA DEL BANCO Y LAS DE LA MESA, POR SU LINEA MEDIDA HOY.
# SON SEDES, NO CIFRAS: la cifra se lee de la linea, no se teclea aqui.
SEDES_TABLA = {"junta asesora": 961, "seleccion de canal": 965}
SEDES_MESA = {"junta asesora": 290, "seleccion de canal": 291}


def lineas(ruta):
    return io.open(ruta, encoding="utf-8").read().replace(
        chr(13) + NL, NL).split(NL)


def seccion(ls, titulo):
    """(inicio, fin) de la seccion cuyo titulo LITERAL empieza por `titulo`, o
    None. PURA: recibe las lineas."""
    ini = None
    for i, l in enumerate(ls, 1):
        if l.startswith(titulo):
            ini = i
            break
    if ini is None:
        return None
    nivel = len(titulo) - len(titulo.lstrip("#"))
    for j in range(ini + 1, len(ls) + 1):
        l = ls[j - 1]
        if l.startswith("#"):
            n = len(l) - len(l.lstrip("#"))
            if n <= nivel:
                return ini, j - 1
    return ini, len(ls)


def ids_de(ls, a, b, filtro=None):
    """LOS IDS ENTRECOMILLADOS DE UN TRAMO, EN ORDEN Y SIN REPETIR, con la linea
    de cada uno. `filtro` acota a las lineas que lo contengan."""
    vistos, out = set(), []
    for i in range(a, b + 1):
        l = ls[i - 1]
        if filtro is not None and filtro not in l:
            continue
        for m in re.finditer(r"`([a-z0-9_]{4,})`", l):
            x = m.group(1)
            if x not in vistos:
                vistos.add(x)
                out.append((x, i))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", default="T2A_DENOMINADOR")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA %d, TAREA 2.a: EL DENOMINADOR PRIMERO, RECOMPUTADO DE LA NOMINA" % VUELTA)
    w("DE MIEMBROS Y NO DE LA TABLA")
    w("=" * 78)
    w("")

    w("0) EL RESOLUTOR, PUESTO ANTES DE CONTAR NADA (`P.1`)")
    mapa, n_nodos = mapa_de_alias()
    w("   CIFRA ficheros de nodo leidos de dataset/nodos/: %d" % n_nodos)
    w("   CIFRA alias en el mapa: %d" % len(mapa))
    vivos = set()
    for f in sorted(os.listdir(NODOS)):
        if f.endswith(".json"):
            vivos.add(json.load(io.open(os.path.join(NODOS, f),
                                        encoding="utf-8"))["node_id"])
    w("   CIFRA node_id distintos en disco: %d" % len(vivos))
    w("")

    ls_inf = lineas(INFORME)
    ls_ban = lineas(BANCO)
    ls_lec = lineas(LECTURAS)
    w("A) LAS TRES SEDES, MEDIDAS AL ENTRAR")
    for nombre, ruta, ls in (("docs/INTRA_DOMINIO_INFORME.md", INFORME, ls_inf),
                             ("docs/BANCO_DE_TEXTOS.md", BANCO, ls_ban),
                             ("docs/plan/LECTURAS_DIRIGIDAS.md", LECTURAS, ls_lec)):
        d = io.open(ruta, "rb").read()
        lf = d.replace(b"\r\n", b"\n")
        w("   %s: %d bytes en disco y %d normalizado a LF, %d lineas"
          % (nombre, len(d), len(lf), len(ls)))
    w("")

    resultados = {}
    w("B) LA NOMINA DE MIEMBROS DE CADA UNA, LEIDA DE SU SECCION DEL INFORME")
    for etiqueta, titulo, filtro in NOMINAS:
        w("   --- %s ---" % etiqueta.upper())
        sec = seccion(ls_inf, titulo)
        if sec is None:
            w("   EL PATRON NO ENCONTRO LA SECCION %r. NO SE PUBLICA CIFRA." % titulo)
            resultados[etiqueta] = None
            continue
        ini, fin = sec
        w("   seccion hallada: docs/INTRA_DOMINIO_INFORME.md linea %d a %d" % (ini, fin))
        w("   titulo literal: %s" % ls_inf[ini - 1].strip())
        if filtro:
            miembros = ids_de(ls_inf, ini, fin, filtro)
        else:
            # LA TABLA DE MIEMBROS: sus filas empiezan por `| ` y llevan un id
            # entrecomillado en la primera celda. Se acota a las filas de tabla
            # para no barrer los ids de la prosa de mas abajo.
            miembros = []
            vistos = set()
            for i in range(ini, fin + 1):
                l = ls_inf[i - 1]
                if not l.startswith("| "):
                    continue
                celdas = l.split("|")
                if len(celdas) < 3:
                    continue
                m = re.search(r"`([a-z0-9_]{4,})`", celdas[1])
                if m and m.group(1) not in vistos:
                    vistos.add(m.group(1))
                    miembros.append((m.group(1), i))
        if not miembros:
            w("   EL PATRON NO ENCONTRO MIEMBROS. NO SE PUBLICA CIFRA.")
            resultados[etiqueta] = None
            continue
        w("   CIFRA miembros hallados: %d" % len(miembros))
        resueltos, fuera = [], []
        for x, ln in miembros:
            r = resolver(mapa, x)
            existe = r in vivos
            w("      linea %5d  %-46s -> resuelve a %-46s existe en el grafo: %s"
              % (ln, x, r, "SI" if existe else "NO"))
            if not existe:
                fuera.append(x)
            resueltos.append(r)
        # LAS DOS CONVENCIONES DEL DENOMINADOR, Y NINGUNA SE ELIGE EN SILENCIO.
        # LITERAL: los ids TAL COMO LA NOMINA LOS ESCRIBE, que es el universo que
        # habia en la fecha_corte de la ficha y el que las dos fuentes publican.
        # RESUELTA: los mismos ids pasados por el resolutor, que es lo que P.1
        # manda para todo conteo que toque ids. Cuando las dos dan lo mismo se
        # dice; cuando no, la diferencia es HUELLA DE FUSION y se nombra.
        literales = sorted(set(x for x, _ln in miembros))
        n_lit = len(literales)
        pos_lit = n_lit * (n_lit - 1) // 2
        distintos = sorted(set(resueltos))
        n = len(distintos)
        posibles = n * (n - 1) // 2
        fundidos = [(x, resolver(mapa, x)) for x, _ln in miembros
                    if resolver(mapa, x) != x]
        w("   CIFRA miembros DISTINTOS EN LITERAL: %d" % n_lit)
        w("   CIFRA PARES POSIBLES EN LITERAL: %d" % pos_lit)
        w("   CIFRA miembros DISTINTOS TRAS RESOLVER: %d" % n)
        w("   CIFRA PARES POSIBLES TRAS RESOLVER: %d" % posibles)
        w("   CIFRA miembros que NO existen en el grafo: %d (%s)"
          % (len(fuera), ", ".join(fuera) or "ninguno"))
        w("   CIFRA miembros que HOY RESUELVEN A OTRO NODO, o sea HUELLA DE"
          " FUSION: %d" % len(fundidos))
        for x, r in fundidos:
            w("      %s  ->  %s" % (x, r))
        w("   LAS DOS CONVENCIONES DAN LO MISMO: %s"
          % ("SI" if pos_lit == posibles else
             "NO, y la diferencia se declara en vez de elegir una en silencio"))
        w("   los %d pares EN LITERAL, enumerados:" % pos_lit)
        for u, v in itertools.combinations(literales, 2):
            w("      %s contra %s" % (u, v))
        w("   los %d pares TRAS RESOLVER, enumerados:" % posibles)
        for u, v in itertools.combinations(distintos, 2):
            w("      %s contra %s" % (u, v))
        resultados[etiqueta] = dict(miembros=miembros, resueltos=distintos,
                                    n=n, posibles=posibles, sec=(ini, fin),
                                    fuera=fuera, literales=literales,
                                    n_lit=n_lit, pos_lit=pos_lit,
                                    fundidos=fundidos)
        w("")

    w("C) LO QUE CADA FUENTE PUBLICA HOY, LEIDO DE SU LINEA Y NO TECLEADO")
    w("")
    w("   LA TABLA VIVA DE LOS PUROS, docs/BANCO_DE_TEXTOS.md:")
    w("      linea %d (la cabecera de la tabla): %s"
      % (938, ls_ban[937].strip()))
    for etiqueta, ln in SEDES_TABLA.items():
        celdas = [c.strip() for c in ls_ban[ln - 1].split("|")]
        w("      linea %d | %s" % (ln, ls_ban[ln - 1].strip()[:150]))
        # columnas: '', #, racimo, miembros, pares posibles, leidos, en A, estado
        if len(celdas) >= 8:
            w("         racimo: %s" % celdas[2])
            w("         miembros: %s | pares posibles: %s | leidos: %s | en A: %s"
              % (celdas[3], celdas[4], celdas[5], celdas[6]))
    w("")
    w("   LO QUE LA MESA DECLARA, docs/plan/LECTURAS_DIRIGIDAS.md:")
    for etiqueta, ln in SEDES_MESA.items():
        w("      linea %d | %s" % (ln, ls_lec[ln - 1].strip()[:190]))
    w("")
    w("   Y LA TABLA POR NOMINA DE LA PROPIA MESA, que es de donde sale su 10:")
    for i in range(28, 34):
        if i <= len(ls_lec):
            w("      linea %d | %s" % (i, ls_lec[i - 1].strip()[:120]))
    w("")

    w("D) LOS TRES DENOMINADORES, JUNTOS Y SIN ELEGIR EN SILENCIO")
    w("")
    w("   %-22s %-14s %-14s %-14s %s"
      % ("nomina", "recomputado", "tabla viva", "mesa", "veredicto"))
    veredictos = {}
    for etiqueta, ln in SEDES_TABLA.items():
        r = resultados.get(etiqueta)
        if r is None:
            w("   %-22s NO COMPUTABLE" % etiqueta)
            continue
        celdas = [c.strip() for c in ls_ban[ln - 1].split("|")]
        tabla_pos = int(re.sub(r"[^0-9]", "", celdas[4]))
        fila_mesa = None
        for i in range(28, 34):
            if i <= len(ls_lec) and etiqueta in ls_lec[i - 1]:
                fila_mesa = i
                break
        mesa_pos = None
        if fila_mesa:
            cm = [c.strip() for c in ls_lec[fila_mesa - 1].split("|")]
            mesa_pos = int(re.sub(r"[^0-9]", "", cm[3]))
        # SE COTEJA CONTRA LA CONVENCION LITERAL, QUE ES LA QUE LAS DOS FUENTES
        # USAN: sus columnas cuentan los ids TAL COMO ESTAN ESCRITOS. La resuelta
        # va al lado y no sustituye a nadie.
        ok_t = (tabla_pos == r["pos_lit"])
        ok_m = (mesa_pos == r["pos_lit"])
        ver = ("LAS TRES CALZAN" if (ok_t and ok_m) else
               ("LA TABLA CALZA, LA MESA NO" if ok_t else
                ("LA MESA CALZA, LA TABLA NO" if ok_m else "NO CALZA NINGUNA")))
        veredictos[etiqueta] = dict(recomputado=r["pos_lit"],
                                    recomputado_res=r["posibles"],
                                    tabla=tabla_pos,
                                    mesa=mesa_pos, veredicto=ver,
                                    fila_mesa=fila_mesa, fila_tabla=ln)
        w("   %-22s %-14s %-14s %-14s %s"
          % (etiqueta, r["pos_lit"], tabla_pos, mesa_pos, ver))
        w("   %-22s (tras resolver da %d, y esa cifra NO se coteja contra las"
          " dos fuentes porque ellas cuentan en literal)"
          % ("", r["posibles"]))
    w("")

    w("E) LOS LEIDOS, PARA QUE EL NUMERADOR NO SE HEREDE TAMPOCO")
    txt_lec = NL.join(ls_lec)
    lds = CABECERA_LD.findall(txt_lec)
    w("   CIFRA cabeceras LD en docs/plan/LECTURAS_DIRIGIDAS.md hoy: %d" % len(lds))
    for etiqueta in ("junta asesora", "seleccion de canal"):
        r = resultados.get(etiqueta)
        if r is None:
            continue
        dentro = []
        for ld, x, y, clase in lds:
            rx, ry = resolver(mapa, x), resolver(mapa, y)
            if rx in r["resueltos"] and ry in r["resueltos"]:
                dentro.append((ld, x, y, clase, rx, ry))
        w("   --- %s ---" % etiqueta.upper())
        w("   CIFRA lecturas dirigidas cuyos DOS extremos, TRAS RESOLVER, estan")
        w("   dentro de esta nomina: %d" % len(dentro))
        for ld, x, y, clase, rx, ry in dentro:
            w("      %-8s %s contra %s | clase %s" % (ld, x, y, clase.strip()))
        celdas = [c.strip() for c in ls_ban[SEDES_TABLA[etiqueta] - 1].split("|")]
        leidos_tabla = int(re.sub(r"[^0-9]", "", celdas[5]))
        en_a_tabla = int(re.sub(r"[^0-9]", "", celdas[6]))
        nuevas_a = len([1 for _ld, _x, _y, cl, _rx, _ry in dentro
                        if cl.strip().startswith("A")])
        w("   CIFRA leidos que la tabla viva publica hoy: %d" % leidos_tabla)
        w("   CIFRA en A que la tabla viva publica hoy: %d" % en_a_tabla)
        w("   CIFRA de esas lecturas dirigidas que son de clase A: %d" % nuevas_a)
        w("   CIFRA leidos DESPUES de sumar las lecturas dirigidas de la mesa:"
          " %d mas %d = %d" % (leidos_tabla, len(dentro), leidos_tabla + len(dentro)))
        w("   CIFRA en A DESPUES: %d mas %d = %d"
          % (en_a_tabla, nuevas_a, en_a_tabla + nuevas_a))
        w("   CIFRA PARES POSIBLES RECOMPUTADOS EN LITERAL: %d" % r["pos_lit"])
        completa = (leidos_tabla + len(dentro)) >= r["pos_lit"]
        w("   COBERTURA SOBRE EL DENOMINADOR RECOMPUTADO EN LITERAL: %d de %d,"
          " o sea %s"
          % (leidos_tabla + len(dentro), r["pos_lit"],
             "COMPLETA" if completa else "INCOMPLETA, o sea PROVISIONAL (banco 9.26)"))
        w("   LO QUE LA MESA DECLARA PARA ESTA NOMINA:")
        w("      %s" % ls_lec[SEDES_MESA[etiqueta] - 1].strip()[:180])
        w("   MI COBERTURA Y LA DE LA MESA DICEN LO MISMO: %s"
          % ("SI" if completa else
             "NO. La mesa declara cobertura COMPLETA y sobre el denominador "
             "recomputado NO lo es. LA DISCREPANCIA SE DECLARA Y NO SE RESUELVE "
             "COPIANDO."))
        veredictos[etiqueta].update(leidos_tabla=leidos_tabla,
                                    en_a_tabla=en_a_tabla,
                                    nuevas_a=nuevas_a,
                                    en_a_nuevo=en_a_tabla + nuevas_a,
                                    ld_dentro=len(dentro),
                                    leidos_nuevos=leidos_tabla + len(dentro),
                                    completa=completa,
                                    lds=[d[0] for d in dentro])
        w("")

    w("=" * 78)
    w("EL RESULTADO DEL 2.a, EN UNA TABLA")
    w("=" * 78)
    w("| nomina | miembros recomputados EN LITERAL | posibles recomputados EN LITERAL | posibles segun la tabla viva | posibles segun la mesa | leidos hoy | mas las LD | cobertura sobre el denominador recomputado |")
    for etiqueta in ("junta asesora", "seleccion de canal"):
        v = veredictos.get(etiqueta)
        r = resultados.get(etiqueta)
        if not v or not r:
            w("| %s | NO COMPUTABLE | | | | | | |" % etiqueta)
            continue
        w("| %s | %d | %d | %d | %s | %d | %d | %d de %d, %s |"
          % (etiqueta, r["n_lit"], r["pos_lit"], v["tabla"], v["mesa"],
             v["leidos_tabla"], v["leidos_nuevos"], v["leidos_nuevos"],
             r["pos_lit"],
             "COMPLETA" if v["completa"] else "INCOMPLETA (PROVISIONAL)"))
    w("")
    w("Y LA SEGUNDA CONVENCION, LA RESUELTA, QUE NO SUSTITUYE A LA DE ARRIBA:")
    w("| nomina | miembros tras resolver | posibles tras resolver | miembros que HOY resuelven a otro nodo |")
    for etiqueta in ("junta asesora", "seleccion de canal"):
        r = resultados.get(etiqueta)
        if not r:
            continue
        w("| %s | %d | %d | %d (%s) |"
          % (etiqueta, r["n"], r["posibles"], len(r["fundidos"]),
             "; ".join("%s a %s" % (x, y) for x, y in r["fundidos"]) or "ninguno"))
    w("")
    w("FIN")
    salida = NL.join(L) + NL
    print(salida)
    io.open(os.path.join(LOOP, "SALIDA_V%d_%s.txt" % (VUELTA, a.salida)),
            "w", encoding="utf-8", newline=NL).write(salida)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
