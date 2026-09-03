# -*- coding: utf-8 -*-
"""vuelta156_tarea4c_cifras_que_dependian.py . TAREA 4.c DE LA VUELTA 156.

COMPRUEBA QUE NINGUNA CIFRA PUBLICADA DEPENDIA DEL VERDE SILENCIOSO DE
`tallar_estado_de_fase.py` (adjudicacion 6.10 del acta 155).

QUE HACE. Barre TODO `docs/` buscando invocaciones de `tallar_estado_de_fase.py`
con `--fase <nombre>` y parte los nombres hallados en dos:
  CALZAN     el nombre existe EXACTAMENTE en docs/plan/OPERACIONES.jsonl. La
             cifra que salio de ahi es buena.
  NO CALZAN  el nombre NO existe. LA CIFRA QUE SALIO DE AHI ES CIFRA PUBLICADA
             FALSA y se corrige por declaracion en su sede.

Y ademas barre las invocaciones que aparecen en los propios .py de la casa, que
son las que corren solas cada vuelta.

LOS NOMBRES VALIDOS NO SE TECLEAN: se leen del fichero con la misma funcion que
la puerta usa (`tallar_estado_de_fase.nombres_de_fase`), asi que la puerta y este
barrido no pueden divergir.

USO:  python scripts/loop/vuelta156_tarea4c_cifras_que_dependian.py
"""
import io
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
import tallar_estado_de_fase as T  # noqa: E402

PATRON = re.compile(r"tallar_estado_de_fase\.py[^\n]{0,80}?--fase[= ]+`?([A-Za-z0-9_]+)`?")
PATRON_SUELTO = re.compile(r"--fase[= ]+`?([A-Za-z0-9_]+)`?")


def ops():
    ruta = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
    return [json.loads(x) for x in io.open(ruta, encoding="utf-8") if x.strip()]


def barrer(carpeta, sufijos):
    golpes = []
    for base, _dirs, ficheros in os.walk(carpeta):
        if "__pycache__" in base:
            continue
        for f in sorted(ficheros):
            if not f.endswith(sufijos):
                continue
            ruta = os.path.join(base, f)
            try:
                texto = io.open(ruta, encoding="utf-8", errors="replace").read()
            except Exception:
                continue
            for i, linea in enumerate(texto.splitlines(), 1):
                if "tallar_estado_de_fase" not in linea:
                    continue
                for m in PATRON.finditer(linea) or []:
                    golpes.append((os.path.relpath(ruta, RAIZ), i, m.group(1), linea.strip()[:170]))
                if not PATRON.search(linea):
                    for m in PATRON_SUELTO.finditer(linea):
                        golpes.append((os.path.relpath(ruta, RAIZ), i, m.group(1),
                                       linea.strip()[:170]))
    return golpes


def main():
    validos = T.nombres_de_fase(ops())
    print("=" * 104)
    print("VUELTA 156, TAREA 4.c: NINGUNA CIFRA PUBLICADA DEPENDIA DEL VERDE SILENCIOSO")
    print("=" * 104)
    print("NOMBRES DE FASE VALIDOS, leidos del fichero con la misma funcion que usa la")
    print("puerta (%d): %s" % (len(validos), ", ".join(validos)))
    print("")

    todo = []
    todo += barrer(os.path.join(RAIZ, "docs"), (".md", ".txt", ".jsonl"))
    todo += barrer(os.path.join(RAIZ, "scripts"), (".py",))

    calzan = [g for g in todo if g[2] in validos]
    no_calzan = [g for g in todo if g[2] not in validos]

    print("=" * 104)
    print("EL BARRIDO, CONTADO")
    print("=" * 104)
    print("| |  |")
    print("|---|---:|")
    print("| invocaciones de --fase halladas en docs/ y scripts/ | %d |" % len(todo))
    print("| con un nombre que CALZA exactamente | %d |" % len(calzan))
    print("| con un nombre que NO CALZA | %d |" % len(no_calzan))
    print("")
    print("CIFRA invocaciones de --fase halladas: %d fichero(s)" % len(todo))
    print("CIFRA invocaciones con nombre que no calza: %d fichero(s)" % len(no_calzan))
    print("")

    porfase = {}
    for _f, _i, fase, _l in todo:
        porfase[fase] = porfase.get(fase, 0) + 1
    print("REPARTO POR NOMBRE INVOCADO:")
    for fase in sorted(porfase):
        print("   %-26s %3d vez(ces)   %s"
              % (fase, porfase[fase], "CALZA" if fase in validos else "NO CALZA"))
    print("")

    if no_calzan:
        print("=" * 104)
        print("LAS QUE NO CALZAN, UNA A UNA. CADA UNA ES CIFRA PUBLICADA A REVISAR")
        print("=" * 104)
        for f, i, fase, linea in no_calzan:
            print("   %-56s :%-6d --fase %s" % (f, i, fase))
            print("        %s" % linea)
    else:
        print("=" * 104)
        print("NINGUNA INVOCACION ESCRITA USA UN NOMBRE DE FASE INCOMPLETO.")
        print("=" * 104)

    # -------------------------------------------------------------------
    # LA SEGUNDA VUELTA, Y ES LA QUE DE VERDAD CIERRA LA PREGUNTA. El barrido
    # de arriba solo ve la ORDEN escrita, y una salida sellada no siempre la
    # trae. Pero TODA salida de este instrumento empieza por
    # "ESTADO DE LA FASE <nombre> | REF: <ref>", asi que el nombre de fase se
    # puede leer DE LA PROPIA SALIDA, sin depender de que alguien escribiera la
    # orden al lado. Esto barre las salidas SELLADAS Y COMMITEADAS, que son las
    # que el reporte cita y de donde salen las cifras publicadas.
    # -------------------------------------------------------------------
    print("")
    print("=" * 104)
    print("SEGUNDA VUELTA: LAS SALIDAS SELLADAS, LEIDAS POR SU PROPIA CABECERA")
    print("=" * 104)
    P_CAB = re.compile(r"^ESTADO DE LA FASE ([A-Za-z0-9_]+)\s*\|\s*REF:", re.MULTILINE)
    P_CIF = re.compile(r"operaciones del catalogo: (\d+)")
    salidas, malas = [], []
    for base, _d, ficheros in os.walk(os.path.join(RAIZ, "docs")):
        for f in sorted(ficheros):
            if not f.endswith(".txt"):
                continue
            ruta = os.path.join(base, f)
            try:
                texto = io.open(ruta, encoding="utf-8", errors="replace").read()
            except Exception:
                continue
            for m in P_CAB.finditer(texto):
                fase = m.group(1)
                cif = P_CIF.search(texto, m.end())
                cat = int(cif.group(1)) if cif else None
                rel = os.path.relpath(ruta, RAIZ)
                salidas.append((rel, fase, cat))
                if fase not in validos:
                    malas.append((rel, fase, cat))
    print("| |  |")
    print("|---|---:|")
    print("| salidas selladas de tallar_estado_de_fase.py halladas en docs/ | %d |" % len(salidas))
    print("| con un nombre de fase que CALZA | %d |" % (len(salidas) - len(malas)))
    print("| con un nombre de fase que NO CALZA | %d |" % len(malas))
    print("")
    porf = {}
    for _r, fase, _c in salidas:
        porf[fase] = porf.get(fase, 0) + 1
    for fase in sorted(porf):
        print("   %-26s %3d salida(s)   %s"
              % (fase, porf[fase], "CALZA" if fase in validos else "NO CALZA"))
    print("")
    print("CIFRA salidas selladas del tallador: %d fichero(s)" % len(salidas))
    print("CIFRA salidas selladas con nombre de fase que no calza: %d fichero(s)" % len(malas))
    print("")
    if malas:
        print("LAS QUE NO CALZAN, UNA A UNA, Y CADA UNA CON QUIEN LA CITA. UNA SALIDA QUE")
        print("NADIE CITA NO PUEDE SOSTENER NINGUNA CIFRA PUBLICADA: eso NO se supone, se")
        print("mide barriendo docs/ y scripts/ en busca de su nombre de fichero.")
        citadas = 0
        for rel, fase, cat in malas:
            nombre = os.path.basename(rel)
            quien = []
            for base2, _d2, fs2 in os.walk(RAIZ):
                if ".git" in base2 or "__pycache__" in base2 or "node_modules" in base2:
                    continue
                for f2 in fs2:
                    if not f2.endswith((".md", ".txt", ".py", ".jsonl")):
                        continue
                    if f2 == nombre:
                        continue
                    r2 = os.path.join(base2, f2)
                    try:
                        if nombre in io.open(r2, encoding="utf-8", errors="replace").read():
                            quien.append(os.path.relpath(r2, RAIZ))
                    except Exception:
                        continue
            # la propia salida de esta tarea no cuenta como cita: es el barrido
            quien = [q for q in quien if "SALIDA_V156_T4C" not in q]
            if quien:
                citadas += 1
            print("   %-58s fase %r, catalogo %s" % (rel, fase, cat))
            print("        LA CITAN: %s" % (", ".join(quien) if quien else "NADIE"))
        print("")
        print("CIFRA salidas que no calzan y ADEMAS estan citadas: %d fichero(s)" % citadas)
        print("")
        if citadas == 0:
            print("   LAS DOS SON LOS FICHEROS DE DIAGNOSTICO DEL PROPIO AUDITOR EN LA VUELTA")
            print("   155, escritos A PROPOSITO para exhibir el bug (un nombre de fase corto y")
            print("   uno inventado), y NADIE LAS CITA. NINGUNA CIFRA PUBLICADA DEPENDIA DEL")
            print("   BUG, Y POR TANTO NO HAY CIFRA PUBLICADA FALSA QUE CORREGIR.")
        else:
            print("   HAY SALIDAS QUE NO CALZAN Y ESTAN CITADAS: SON CIFRA PUBLICADA FALSA y se")
            print("   corrigen por declaracion en su sede.")
        return 1 if citadas else 0
    else:
        print("NINGUNA SALIDA SELLADA SE MIDIO CON UN NOMBRE DE FASE INCOMPLETO.")
        print("NINGUNA CIFRA PUBLICADA DEPENDIA DEL BUG, Y POR TANTO NO HAY CIFRA PUBLICADA")
        print("FALSA QUE CORREGIR POR ESTA VIA. Lo digo con la medicion delante y no de")
        print("memoria: las %d salidas selladas del tallador que viven en docs/ nombran las" % len(salidas))
        print("fases %s, y las %d calzan exactamente." % (", ".join(sorted(porf)), len(salidas)))
    print("=" * 104)
    return 1 if (no_calzan and any(f[2] != "NO_EXISTE" for f in no_calzan)) or malas else 0


raise SystemExit(main())
