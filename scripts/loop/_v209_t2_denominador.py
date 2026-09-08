# -*- coding: utf-8 -*-
r"""_v209_t2_denominador.py . TAREA 2.a DE LA VUELTA 209: EL DENOMINADOR
RECOMPUTADO ANTES DE ESCRIBIR NADA, DE LA NOMINA DE MIEMBROS DE
`docs/INTRA_DOMINIO_INFORME.md` Y NO DE LA TABLA.

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO, fuera del censo y fuera de la
nomina de la bateria (moratoria de `AUDITOR.md` 6.3). **NO ESCRIBE EN NINGUNA
SEDE: SOLO MIDE.** Las dos correcciones las escribe el 2.b, en otro fichero.

**NINGUN LECTOR NUEVO Y NINGUNO CLONADO.** Todo lo que lee viene IMPORTADO de
`scripts/loop/_v208_t2_denominador.py` (`lineas`, `seccion`, `ids_de`, `NOMINAS`,
`INFORME`, `LECTURAS`, `NODOS`) y, por su via, `mapa_de_alias()`, `resolver()` y
`CABECERA_LD` de `vuelta166_tarea2_correccion_op_l_01.py`, que es su sede.
**IMPORTAR NO ES CLONAR** (acta 206, adjudicacion `6.5`).

POR QUE SE VUELVE A CORRER EN VEZ DE HEREDAR EL VERDE DE LA 208: `EJECUTOR.md` 2,
EL INSTRUMENTO MANDA. La salida de la 208 es CONTRASTE, no fuente, y entre las dos
vueltas la sede del banco cambio.

**MANDA LA CONVENCION DEL CORTE DE LA FICHA, O SEA LA LITERAL** (adjudicacion
`6.6` del acta 208, por el banco `9.21` mas `P.1`), **y la resuelta se publica AL
LADO con su fecha**. Eso no se vuelve a decidir aqui: se aplica.

LA GUARDA QUE PUEDE CAER: si el patron no encuentra la seccion o no encuentra
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
from _v208_t2_denominador import (  # noqa: E402
    lineas, seccion, ids_de, NOMINAS, INFORME, LECTURAS, NODOS)
from vuelta166_tarea2_correccion_op_l_01 import (  # noqa: E402
    mapa_de_alias, resolver, CABECERA_LD)

VUELTA = 209

# LAS DOS LINEAS DE `docs/plan/LECTURAS_DIRIGIDAS.md` QUE EL ENCARGO NOMBRA. SON
# SEDES, NO CIFRAS: lo que publican se LEE de la linea y no se teclea aqui. Y se
# COMPRUEBA que la linea es la que se cree antes de leerla.
SEDES_MESA = {
    "tabla por nomina": (31, "| **seleccion de canal** |"),
    "que nominas cambian": (291, "| **seleccion de canal** |"),
}

# LO QUE EL ENCARGO DA COMO CONTRASTE. NO ES FUENTE DE NADA.
CONTRASTE = {
    "node_id": 3853, "alias": 761,
    "junta_lit_miembros": 4, "junta_lit_pares": 6,
    "junta_res_miembros": 2, "junta_res_pares": 1,
    "canal_lit_miembros": 6, "canal_lit_pares": 15,
    "canal_res_miembros": 6, "canal_res_pares": 15,
    "canal_fundidos": 0,
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", default="T2A_DENOMINADOR")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA %d, TAREA 2.a: EL DENOMINADOR PRIMERO, RECOMPUTADO DE LA NOMINA"
      % VUELTA)
    w("DE MIEMBROS Y NO DE LA TABLA")
    w("=" * 78)
    w("")
    w("EL LECTOR VA IMPORTADO Y SIN TOCARLE UNA LINEA (moratoria de AUDITOR.md")
    w("6.3): `lineas`, `seccion`, `ids_de` y `NOMINAS` vienen de")
    w("`_v208_t2_denominador.py`, y `mapa_de_alias`, `resolver` y `CABECERA_LD`")
    w("de `vuelta166_tarea2_correccion_op_l_01.py`. IMPORTAR NO ES CLONAR.")
    w("")

    w("0) EL RESOLUTOR, PUESTO ANTES DE CONTAR NADA (`P.1`)")
    mapa, n_nodos = mapa_de_alias()
    vivos = set()
    for f in sorted(os.listdir(NODOS)):
        if f.endswith(".json"):
            vivos.add(json.load(io.open(os.path.join(NODOS, f),
                                        encoding="utf-8"))["node_id"])
    w("   CIFRA ficheros de nodo leidos de dataset/nodos/: %d" % n_nodos)
    w("   CIFRA node_id distintos en disco: %d" % len(vivos))
    w("   CIFRA alias en el mapa: %d" % len(mapa))
    w("   contraste del encargo: 3853 node_id y 761 alias")
    w("   CALZA: %s" % ("SI" if (len(vivos) == CONTRASTE["node_id"]
                                 and len(mapa) == CONTRASTE["alias"])
                        else "NO, Y LA DISCREPANCIA SE DECLARA"))
    w("")

    ls_inf = lineas(INFORME)
    ls_lec = lineas(LECTURAS)
    w("A) LAS DOS SEDES, MEDIDAS AL ENTRAR POR LAS DOS CONVENCIONES")
    for nombre, ruta, ls in (("docs/INTRA_DOMINIO_INFORME.md", INFORME, ls_inf),
                             ("docs/plan/LECTURAS_DIRIGIDAS.md", LECTURAS, ls_lec)):
        d = io.open(ruta, "rb").read()
        lf = d.replace(b"\r\n", b"\n")
        w("   %s: %d bytes en disco y %d bytes normalizado a LF, %d lineas"
          % (nombre, len(d), len(lf), len(ls)))
    w("")

    resultados = {}
    w("B) LA NOMINA DE MIEMBROS DE CADA UNA, LEIDA DE SU SECCION DEL INFORME")
    for etiqueta, titulo, filtro in NOMINAS:
        w("   --- %s ---" % etiqueta.upper())
        sec = seccion(ls_inf, titulo)
        if sec is None:
            w("   EL PATRON NO ENCONTRO LA SECCION %r. NO SE PUBLICA CIFRA."
              % titulo)
            resultados[etiqueta] = None
            continue
        ini, fin = sec
        w("   seccion hallada: docs/INTRA_DOMINIO_INFORME.md linea %d a %d"
          % (ini, fin))
        w("   titulo literal: %s" % ls_inf[ini - 1].strip())
        if filtro:
            miembros = ids_de(ls_inf, ini, fin, filtro)
        else:
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
        w("   CIFRA miembros FUNDIDOS, o sea que hoy resuelven a otro nodo: %d"
          % len(fundidos))
        for x, r in fundidos:
            w("      %s  ->  %s" % (x, r))
        w("   LAS DOS CONVENCIONES DAN LO MISMO: %s"
          % ("SI" if pos_lit == posibles else
             "NO, y la diferencia se declara en vez de elegir una en silencio"))
        w("   MANDA LA LITERAL, que es la del `fecha_corte` de la ficha")
        w("   (adjudicacion `6.6` del acta 208). La resuelta va AL LADO.")
        resultados[etiqueta] = dict(miembros=miembros, resueltos=distintos,
                                    n=n, posibles=posibles, sec=(ini, fin),
                                    fuera=fuera, literales=literales,
                                    n_lit=n_lit, pos_lit=pos_lit,
                                    fundidos=fundidos)
        w("")

    w("B.1) EL COTEJO CONTRA EL CONTRASTE DEL ENCARGO (contraste, NO fuente)")
    r_j = resultados.get("junta asesora")
    r_c = resultados.get("seleccion de canal")
    filas_cot = []
    if r_j:
        filas_cot += [
            ("junta asesora, miembros LITERAL", r_j["n_lit"],
             CONTRASTE["junta_lit_miembros"]),
            ("junta asesora, pares LITERAL", r_j["pos_lit"],
             CONTRASTE["junta_lit_pares"]),
            ("junta asesora, miembros RESUELTA", r_j["n"],
             CONTRASTE["junta_res_miembros"]),
            ("junta asesora, pares RESUELTA", r_j["posibles"],
             CONTRASTE["junta_res_pares"]),
        ]
    if r_c:
        filas_cot += [
            ("seleccion de canal, miembros LITERAL", r_c["n_lit"],
             CONTRASTE["canal_lit_miembros"]),
            ("seleccion de canal, pares LITERAL", r_c["pos_lit"],
             CONTRASTE["canal_lit_pares"]),
            ("seleccion de canal, miembros RESUELTA", r_c["n"],
             CONTRASTE["canal_res_miembros"]),
            ("seleccion de canal, pares RESUELTA", r_c["posibles"],
             CONTRASTE["canal_res_pares"]),
            ("seleccion de canal, fundidos", len(r_c["fundidos"]),
             CONTRASTE["canal_fundidos"]),
        ]
    discrepan = 0
    for nombre, mio, suyo in filas_cot:
        ok = (mio == suyo)
        if not ok:
            discrepan += 1
        w("   %-40s mio %-6s contraste %-6s %s"
          % (nombre, mio, suyo, "CALZA" if ok else "DISCREPA Y SE DECLARA"))
    w("   CIFRA discrepancias con el contraste del encargo en el 2.a: %d"
      % discrepan)
    w("")

    w("C) LA NOMINA VERIFICADA CONTRA EL GRAFO Y SU CORRECCION DECLARADA,")
    w("   LEIDAS DE SU LINEA Y NO TECLEADAS")
    for i in list(range(5312, 5323)):
        if i <= len(ls_inf):
            w("   docs/INTRA_DOMINIO_INFORME.md:%d | %s" % (i, ls_inf[i - 1].strip()[:150]))
    w("")

    w("D) LO QUE LAS DOS LINEAS DE LA MESA PUBLICAN HOY, LEIDO DE SU LINEA")
    lineas_ok = 0
    for etiqueta, (ln, ancla) in SEDES_MESA.items():
        l = ls_lec[ln - 1] if ln <= len(ls_lec) else ""
        calza = l.startswith(ancla)
        lineas_ok += 1 if calza else 0
        w("   --- %s ---" % etiqueta)
        w("   docs/plan/LECTURAS_DIRIGIDAS.md:%d empieza por %r: %s"
          % (ln, ancla, "SI" if calza else "NO, Y ESO ES ROJO"))
        w("   literal: %s" % l.strip())
    w("   CIFRA lineas de la mesa que calzan con su ancla: %d de %d"
      % (lineas_ok, len(SEDES_MESA)))
    if lineas_ok != len(SEDES_MESA):
        w("   ROJO: alguna de las dos lineas no es la que se cree.")
        salida = NL.join(L) + NL
        print(salida)
        io.open(os.path.join(LOOP, "SALIDA_V%d_%s.txt" % (VUELTA, a.salida)),
                "w", encoding="utf-8", newline=NL).write(salida)
        return 1
    w("")

    w("E) LOS DOS DENOMINADORES, JUNTOS Y SIN ELEGIR EN SILENCIO")
    w("")
    w("   %-22s %-16s %-16s %s"
      % ("nomina", "LITERAL (manda)", "RESUELTA (al lado)", "lo que la mesa dice"))
    fila31 = [c.strip() for c in ls_lec[30].split("|")]
    mesa_miembros = int(re.sub(r"[^0-9]", "", fila31[2]))
    mesa_posibles = int(re.sub(r"[^0-9]", "", fila31[3]))
    mesa_leidos = int(re.sub(r"[^0-9]", "", fila31[4]))
    mesa_fuera = int(re.sub(r"[^0-9]", "", fila31[5]))
    w("   %-22s %-16s %-16s %s"
      % ("seleccion de canal",
         "%d miembros, %d pares" % (r_c["n_lit"], r_c["pos_lit"]),
         "%d miembros, %d pares" % (r_c["n"], r_c["posibles"]),
         "%d miembros, %d pares" % (mesa_miembros, mesa_posibles)))
    w("   %-22s %-16s %-16s %s"
      % ("junta asesora",
         "%d miembros, %d pares" % (r_j["n_lit"], r_j["pos_lit"]),
         "%d miembros, %d pares" % (r_j["n"], r_j["posibles"]),
         "(no es la que el encargo manda corregir)"))
    w("")
    w("   CIFRA leidos que la linea 31 publica: %d" % mesa_leidos)
    w("   CIFRA fuera de cola que la linea 31 publica: %d" % mesa_fuera)
    w("   LA LINEA 31 CALZA CON EL RECOMPUTO: %s"
      % ("SI" if (mesa_miembros == r_c["n_lit"]
                  and mesa_posibles == r_c["pos_lit"])
         else "NO, Y ESA ES LA PRIMERA DE LAS DOS CIFRAS QUE SIGUEN MAL"))
    w("")

    w("F) LOS LEIDOS, PARA QUE EL NUMERADOR TAMPOCO SE HEREDE")
    txt_lec = NL.join(ls_lec)
    lds = CABECERA_LD.findall(txt_lec)
    w("   CIFRA cabeceras LD en docs/plan/LECTURAS_DIRIGIDAS.md hoy: %d" % len(lds))
    dentro = []
    for ld, x, y, clase in lds:
        rx, ry = resolver(mapa, x), resolver(mapa, y)
        if rx in r_c["resueltos"] and ry in r_c["resueltos"]:
            dentro.append((ld, x, y, clase.strip(), rx, ry))
    w("   CIFRA lecturas dirigidas cuyos DOS extremos, TRAS RESOLVER, caen")
    w("   dentro de la seleccion de canal: %d" % len(dentro))
    for ld, x, y, clase, rx, ry in dentro:
        w("      %-8s %s contra %s | clase %s" % (ld, x, y, clase))
    w("")
    w("   LA COBERTURA DE LA SELECCION DE CANAL, MEDIDA Y NO NARRADA:")
    w("   CIFRA leidos publicados por la linea 31: %d" % mesa_leidos)
    w("   CIFRA denominador recomputado en LITERAL: %d" % r_c["pos_lit"])
    leidos_nuevos = mesa_leidos + len(dentro)
    w("   CIFRA leidos mas las lecturas dirigidas de esta nomina: %d mas %d"
      " es %d" % (mesa_leidos, len(dentro), leidos_nuevos))
    w("   COBERTURA: %d de %d" % (leidos_nuevos, r_c["pos_lit"]))
    w("   COMPLETA O PROVISIONAL: %s"
      % ("COMPLETA" if leidos_nuevos >= r_c["pos_lit"]
         else "INCOMPLETA, y por el banco `9.26` la forma es PROVISIONAL"))
    w("")
    w("FIN")

    salida = NL.join(L) + NL
    print(salida)
    io.open(os.path.join(LOOP, "SALIDA_V%d_%s.txt" % (VUELTA, a.salida)),
            "w", encoding="utf-8", newline=NL).write(salida)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
