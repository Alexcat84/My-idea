# -*- coding: utf-8 -*-
r"""_v208_t3_vara.py . TAREA 3.a DE LA VUELTA 208: LA VARA DE `OP-L-03`, SELLADA
EN SU PROPIO COMMIT ANTES DE COTEJAR NINGUN DOCUMENTO.

COMPUTO DE UNA VUELTA, prefijo de guion bajo, fuera del censo y fuera de la
nomina (moratoria `AUDITOR.md` 6.3). No escribe en ninguna sede: SOLO MIDE Y
SELLA.

POR QUE VA EN SU PROPIO COMMIT: una vara escrita despues de mirar se acomoda a lo
que se vio. Este fichero se committea ANTES del cotejo, y el cotejo lo IMPORTA sin
poder cambiarlo. Es el mismo metodo que la 207 uso con `OP-L-01`, que salio bien y
por eso se repite.

LA SEDE FINA ES `campo[indice]` Y NO UN NUMERO DE LINEA: la ficha entera vive en
UNA sola linea de `docs/plan/OPERACIONES.jsonl`, la **43**. Decir "linea 43"
dieciseis veces no localiza nada.

EL ESCARMIENTO DE LA 207, APLICADO Y NO SOLO CITADO. Alli DOS puntos se sellaron
como NO DOCUMENTALES y resultaron tener sede (`V.4` y, cazada por el auditor, la
`V.14`). AQUI, ANTES DE SELLAR UN PUNTO COMO NO DOCUMENTAL, SE BUSCA SU LITERAL EN
LOS SEIS DOCUMENTOS DE LA EVIDENCIA Y EL RESULTADO SE ESCRIBE DENTRO DEL SELLO. Si
la busqueda lo encuentra, el punto se sella DOCUMENTAL. **La busqueda va tambien
POSITIVA**, con un literal de control que TIENE que aparecer, porque una busqueda
negativa no se puede citar sola (`EJECUTOR.md` 9).

LO QUE ESTE COMPUTO DECLARA CON HONESTIDAD Y NO DISIMULA: de los seis documentos,
**yo ya habia abierto tres antes de esta tarea y en esta misma vuelta**:
`docs/loop/EJECUTOR.md` (lo manda el encargo como primer acto de la vuelta),
`docs/loop/AUDITOR.md` (citado por el encargo) y
`docs/plan/LECTURAS_DIRIGIDAS.md` (lo midio la TAREA 2). **Los otros tres los abro
por primera vez en el cotejo.** El sello sigue siendo sello: lo que garantiza es
que la vara y su reparto se escriben ANTES de cotejar, y eso se cumple; pero
decir "antes de abrir ningun documento" sin esta nota seria falso.
"""
import argparse
import hashlib
import io
import json
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

VUELTA = 208
ID_OP = "OP-L-03"
LINEA_FICHA = 43
OPES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")

# LOS SEIS DOCUMENTOS QUE LA FICHA NOMBRA, con la clave corta con que el cotejo
# los cita. NO SE ELIGEN AQUI POR GUSTO: cada uno sale de un campo de la ficha, y
# el campo va escrito al lado.
DOCS = {
    "BDP": ("docs/plan/BANCO_DEL_PLAN.md", "evidencia[0], 'BANCO_DEL_PLAN.md P.5'"),
    "LD": ("docs/plan/LECTURAS_DIRIGIDAS.md",
           "evidencia[2], 'LECTURAS_DIRIGIDAS.md, el reparto por acto'"),
    "LEC": ("docs/plan/OP_L_03_LECTURAS.jsonl",
            "evidencia[3], que la nombra como sede real del reparto por acto"),
    "TRI": ("docs/plan/OP_L_03_TRIANGULOS.jsonl",
            "evidencia[3], que la nombra como la segunda sede real"),
    "EJE": ("docs/loop/EJECUTOR.md",
            "evidencia[3], 'una busqueda negativa no se puede citar sola "
            "(EJECUTOR.md 9)'"),
    "AUD": ("docs/loop/AUDITOR.md",
            "evidencia[3], 'la vara del trabajo pendiente es el instrumento y "
            "nunca el campo estado (recuadro de AUDITOR.md 0)'"),
}

# LA VARA. Cada punto: (clave, enunciado, campo, indice o None, CITA LITERAL que
# tiene que aparecer VERBATIM en ese campo de la ficha, documento contra el que se
# coteja o None si se sella NO DOCUMENTAL).
PUNTOS = [
    ("V.1", "LA REGLA `P.5` DEL `BANCO_DEL_PLAN.md`, QUE ES LO QUE ESTA MESA "
            "INVOCA COMO SU PRIMERA EVIDENCIA",
     "evidencia", 0, "BANCO_DEL_PLAN.md P.5", "BDP"),
    ("V.2", "EL REPARTO MEDIDO EL 11 AGO 2026: 55 PARES EN 29 ACTOS, CORTE "
            "PUESTO 2117",
     "evidencia", 1, "MEDIDO el 11 ago 2026: 55 pares en 29 actos, corte puesto 2117",
     "LEC"),
    ("V.3", "EL REPARTO POR ACTO EN `LECTURAS_DIRIGIDAS.md`",
     "evidencia", 2, "LECTURAS_DIRIGIDAS.md, el reparto por acto", "LD"),
    ("V.4", "LA PRIMERA SEDE REAL DEL REPARTO: `OP_L_03_LECTURAS.jsonl`, CON 14 "
            "FILAS, 14 ACTOS DISTINTOS Y 0 LINEAS QUE NO SEAN JSON VALIDO",
     "evidencia", 3,
     "docs/plan/OP_L_03_LECTURAS.jsonl, que mide 51368 bytes en disco y 51368 "
     "normalizados a LF, con 14 filas, 14 actos distintos y 0 lineas que no sean "
     "JSON valido", "LEC"),
    ("V.5", "LA SEGUNDA SEDE REAL: `OP_L_03_TRIANGULOS.jsonl`, CON 19 FILAS, 8 "
            "ACTOS DISTINTOS Y 0 LINEAS QUE NO SEAN JSON VALIDO",
     "evidencia", 3,
     "docs/plan/OP_L_03_TRIANGULOS.jsonl, que mide 55705 bytes en disco y 55705 "
     "normalizados a LF, con 19 filas, 8 actos distintos y 0 lineas que no sean "
     "JSON valido", "TRI"),
    ("V.6", "LA COBERTURA RECONTADA: 11 ACTOS CON `leido` EN TRUE, 3 EN FALSE, Y "
            "`cifra_pares_leidos` SUMANDO 19 PARES",
     "evidencia", 3,
     "14 actos distintos, de los cuales 11 tienen leido en true y 3 en false, y "
     "sus campos cifra_pares_leidos suman 19 pares", "LEC"),
    ("V.7", "LO QUE FALTA, DICHO POR LA PROPIA FICHA: 15 DE LOS 29 ACTOS SIN "
            "FICHA DE LECTURA Y 36 DE LOS 55 PARES SIN LECTURA REGISTRADA",
     "evidencia", 3,
     "15 de los 29 actos prometidos siguen sin ficha de lectura, y 36 de los 55 "
     "pares prometidos siguen sin lectura registrada", "LEC"),
    ("V.8", "LA BUSQUEDA NEGATIVA QUE LA CORRECCION DE LA 202 PUBLICA: 0 "
            "APARICIONES DE 'reparto por acto' Y 0 MENCIONES DE `OP-L-03` EN "
            "`LECTURAS_DIRIGIDAS.md`",
     "evidencia", 3,
     "trae 0 apariciones del literal 'reparto por acto' y 0 menciones de OP-L-03",
     "LD"),
    ("V.9", "LA CLAUSULA 1 DE VERIFICACION: NINGUN ACTO SE FUNDE CON UN PAR "
            "INTERNO SIN VEREDICTO",
     "verificacion", 0, "ningun acto se funde con un par interno sin veredicto",
     "BDP"),
    ("V.10", "LA CLAUSULA 2 DE VERIFICACION: LAS 55 MARCADAS LECTURA DIRIGIDA NO "
             "ENTRAN EN LA COLA NI MUEVEN SU MARCADOR",
     "verificacion", 1,
     "las 55 lecturas marcadas LECTURA DIRIGIDA: no entran en la cola ni mueven "
     "su marcador", "LD"),
    ("V.11", "LA CLAUSULA 3 DE VERIFICACION: CADA ACTO CUYA LECTURA COMPLETA "
             "CAMBIE SU FORMA SE RE-MIDE CON SU COBERTURA AL LADO",
     "verificacion", 2,
     "cada acto cuya lectura completa cambie su forma se re-mide con su cobertura "
     "al lado", "LEC"),
    ("V.12", "LA TERCERA MITAD DE LA VARA NUEVA: LO QUE BLOQUEA UNA FUSION ES EL "
             "TRIANGULO A MAS A MAS D MEDIDO DE `P.10`",
     "verificacion", 3,
     "el TRIANGULO A mas A mas D MEDIDO de P.10", "TRI"),
    ("V.13", "LA REMISION DEL `estado`: LA VARA DEL TRABAJO PENDIENTE ES EL "
             "INSTRUMENTO Y NUNCA EL CAMPO `estado`",
     "evidencia", 3,
     "la vara del trabajo pendiente es el instrumento y nunca el campo estado "
     "(recuadro de AUDITOR.md 0, decision del fundador del 4 sep 2026)", "AUD"),
    ("V.14", "LA REMISION DE LA BUSQUEDA NEGATIVA: UNA BUSQUEDA NEGATIVA NO SE "
             "PUEDE CITAR SOLA",
     "evidencia", 3,
     "porque una busqueda negativa no se puede citar sola (EJECUTOR.md 9)", "EJE"),
    ("V.15", "LA ADJUDICACION: POR LA REGLA `P.5`, CADA ACTO QUE VAYA A FUNDIRSE "
             "SE LEE ENTERO DESPUES DE SU DESTEJIDO Y ANTES DE SU FUSION",
     "adjudicacion", None,
     "Por la regla P.5, cada acto que vaya a fundirse se lee ENTERO despues de su "
     "destejido y antes de su fusion", "BDP"),
    ("V.16", "EL RECOMPUTO AL CORTE 3.388: EL BACKLOG SUBE A CUARENTA ACTOS Y "
             "SETENTA Y TRES PARES",
     "nota", None,
     "el backlog SUBIO de 29 actos y 55 pares (corte 2117, el viejo no se borra) "
     "a CUARENTA actos y SETENTA Y TRES pares", None),
    # V.17 SE SELLA DOCUMENTAL, Y NO ES UN CAMBIO DE OPINION: ES EL RESULTADO DE
    # LA COMPROBACION DEL ESCARMIENTO. Mi primer borrador lo sellaba NO
    # DOCUMENTAL por ser estructura de la ficha, y la busqueda obligatoria de su
    # literal en los seis documentos, corrida ANTES de sellar, encontro `OP-U-01`
    # en `BANCO_DEL_PLAN.md` y en `LECTURAS_DIRIGIDAS.md`. La guarda cayo en rojo
    # y no dejo sellar. ESO ES MOVER UN PUNTO ANTES DE MIRAR EL COTEJO, que es lo
    # que el escarmiento pide, y NO despues, que es lo que el sello prohibe.
    ("V.17", "LAS DEPENDENCIAS: SEIS FICHAS DE LAS QUE DEPENDE Y DOS A LAS QUE "
             "BLOQUEA",
     "depende_de", None, None, "BDP"),
    ("V.18", "LA SEGUNDA MITAD DE LA VARA NUEVA: UN PAR SIN LEER ES EL QUE ESTA "
             "EN COLA Y SIN VEREDICTO, Y LOS 47 ACTOS TRAEN CERO EN "
             "`en_cola_sin_leer`",
     "verificacion", 3,
     "los 47 actos del tramo traen CERO en en_cola_sin_leer", None),
]

# LOS QUE SE SELLAN NO DOCUMENTALES, CON SU MOTIVO ESCRITO ANTES DE MIRAR. Cada
# uno lleva ademas EL LITERAL QUE SE BUSCA EN LOS SEIS DOCUMENTOS antes de
# sellarlo: si aparece, el punto NO se puede sellar aqui y el computo cae en rojo.
NO_DOCUMENTALES = {
    "V.16": ("es una CIFRA DE RECOMPUTO cuya sede declarada es "
             "docs/plan/RECOMPUTO_3388.md, que NO es ninguno de los seis "
             "documentos que la ficha nombra",
             "CUARENTA actos y SETENTA Y TRES pares"),
    "V.18": ("es una CLAUSULA sobre el campo en_cola_sin_leer de "
             "scripts/plan/recomputo_3388.py, que NO es ninguno de los seis",
             "en_cola_sin_leer"),
}

# EL LITERAL DE CONTROL DE CADA DOCUMENTO: TIENE que aparecer. Si no aparece, la
# busqueda negativa de arriba no vale nada y el computo cae en rojo.
CONTROL = {"BDP": "P.5", "LD": "LD-01", "LEC": "acto", "TRI": "acto",
           "EJE": "EJECUTOR", "AUD": "AUDITOR"}


def dos_convenciones(ruta):
    d = io.open(ruta, "rb").read()
    lf = d.replace(b"\r\n", b"\n")
    return (len(d), len(lf), hashlib.sha256(d).hexdigest()[:16],
            hashlib.sha256(lf).hexdigest()[:16], lf.decode("utf-8"))


def la_ficha():
    _d, _lf, _sd, _sl, t = dos_convenciones(OPES)
    ls = t.split(NL)
    return json.loads(ls[LINEA_FICHA - 1])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", default="T3_VARA")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA %d, TAREA 3.a: LA VARA DE %s, SELLADA ANTES DEL COTEJO"
      % (VUELTA, ID_OP))
    w("=" * 78)
    w("")

    w("A) LA FICHA, SELLADA")
    d0, lf0, sd0, sl0, _t = dos_convenciones(OPES)
    w("   docs/plan/OPERACIONES.jsonl: %d bytes en disco y %d normalizado a LF,"
      % (d0, lf0))
    w("   sha256 disco %s y sha256 LF %s" % (sd0, sl0))
    f = la_ficha()
    if f.get("id_op") != ID_OP:
        w("   ROJO: la linea %d no es la ficha %s." % (LINEA_FICHA, ID_OP))
        print(NL.join(L))
        return 1
    w("   la ficha %s vive en la LINEA %d" % (ID_OP, LINEA_FICHA))
    w("   CIFRA campos de la ficha: %d" % len(f))
    w("   CIFRA elementos de `evidencia`: %d" % len(f.get("evidencia", [])))
    w("   CIFRA elementos de `verificacion`: %d" % len(f.get("verificacion", [])))
    corr_e = len([1 for x in f.get("evidencia", [])
                  if str(x).strip().startswith("CORRECCION DECLARADA")])
    corr_v = len([1 for x in f.get("verificacion", [])
                  if str(x).strip().startswith("CORRECCION DECLARADA")])
    w("   de esos, CORRECCIONES DECLARADAS: %d en evidencia y %d en verificacion"
      % (corr_e, corr_v))
    w("   CIFRA `depende_de`: %d (%s)"
      % (len(f.get("depende_de") or []), ", ".join(f.get("depende_de") or [])))
    w("   CIFRA `bloquea_a`: %d (%s)"
      % (len(f.get("bloquea_a") or []), ", ".join(f.get("bloquea_a") or [])))
    w("   `fecha_corte`: %s" % f.get("fecha_corte"))
    w("   `estado`: %s   <- SE LEE COMO DATO Y NO SE TOCA (AUDITOR.md 0)"
      % f.get("estado"))
    w("   `orden`: %s | `tipo`: %s | `fase`: %s"
      % (f.get("orden"), f.get("tipo"), f.get("fase")))
    w("")

    w("B) LOS SEIS DOCUMENTOS QUE LA FICHA NOMBRA, Y DE QUE CAMPO SALE CADA UNO")
    textos = {}
    for k, (rel, deque) in DOCS.items():
        p = os.path.join(RAIZ, rel.replace("/", os.sep))
        if not os.path.isfile(p):
            w("   %-4s %-40s NO EXISTE" % (k, rel))
            textos[k] = None
            continue
        dd, ll, sd, sl, t = dos_convenciones(p)
        textos[k] = t
        w("   %-4s %-40s %d bytes en disco y %d normalizado a LF" % (k, rel, dd, ll))
        w("        sale de: %s" % deque)
    w("")
    w("   LO QUE DECLARO Y NO DISIMULO: de los seis, TRES los abri antes de esta")
    w("   tarea y en esta misma vuelta: EJE (lo manda el encargo como primer acto),")
    w("   AUD (citado por el encargo) y LD (lo midio mi TAREA 2). Los otros tres")
    w("   los abro por primera vez en el cotejo. El sello garantiza que la vara y")
    w("   su reparto se escriben ANTES de cotejar, y eso se cumple.")
    w("")

    w("C) LA VARA. CADA PUNTO CON SU CITA COMPROBADA VERBATIM CONTRA LA FICHA")
    fallan = 0
    for clave, enunciado, campo, indice, cita, doc in PUNTOS:
        w("")
        w("   %-5s %s" % (clave, enunciado))
        sede = campo if indice is None else "%s[%d]" % (campo, indice)
        w("         sede: `%s`, linea %d del fichero" % (sede, LINEA_FICHA))
        if cita is None:
            w("         cita: (no hay literal: el punto es sobre la ESTRUCTURA del")
            w("               campo, no sobre su texto)")
            continue
        valor = f.get(campo)
        if indice is not None:
            valor = valor[indice] if isinstance(valor, list) and len(valor) > indice else ""
        verbatim = cita in str(valor)
        w("         cita: %r" % cita[:150])
        w("         la cita aparece VERBATIM en esa sede: %s"
          % ("SI" if verbatim else "NO"))
        if not verbatim:
            fallan += 1
    w("")
    w("   CIFRA puntos de la vara: %d" % len(PUNTOS))
    w("   CIFRA citas que NO aparecen verbatim: %d" % fallan)
    if fallan:
        w("   ROJO: una cita no aparece verbatim. LA VARA NO SE SELLA.")
        print(NL.join(L))
        return 1
    w("")

    w("D) EL ESCARMIENTO DE LA 207: ANTES DE SELLAR UN PUNTO COMO NO DOCUMENTAL,")
    w("   SE BUSCA SU LITERAL EN LOS SEIS DOCUMENTOS")
    w("   Y LA BUSQUEDA VA TAMBIEN POSITIVA, con un literal de control por")
    w("   documento que TIENE que aparecer (`EJECUTOR.md` 9).")
    w("")
    w("   EL CONTROL POSITIVO, PRIMERO:")
    control_falla = 0
    for k, lit in CONTROL.items():
        t = textos.get(k)
        n = t.count(lit) if t else 0
        w("      %-4s el literal de control %-12r aparece %d vez(ces)" % (k, lit, n))
        if n == 0:
            control_falla += 1
    w("   CIFRA controles positivos que NO aparecen: %d" % control_falla)
    if control_falla:
        w("   ROJO: un control positivo no aparece. La busqueda negativa no vale.")
        print(NL.join(L))
        return 1
    w("")
    hallados = []
    for clave, (motivo, literal) in sorted(NO_DOCUMENTALES.items()):
        w("   %-5s literal que se busca: %r" % (clave, literal))
        for k in sorted(DOCS):
            t = textos.get(k)
            n = t.count(literal) if t else 0
            w("         %-4s %-40s -> %d aparicion(es)" % (k, DOCS[k][0], n))
            if n:
                hallados.append((clave, k, n))
    w("   CIFRA puntos candidatos a NO DOCUMENTAL cuyo literal SI aparece en")
    w("   alguno de los seis: %d" % len(hallados))
    for clave, k, n in hallados:
        w("      %s aparece %d vez(ces) en %s" % (clave, n, DOCS[k][0]))
    if hallados:
        w("   ROJO: no se puede sellar como NO DOCUMENTAL un punto cuya sede SI")
        w("   esta en uno de los seis. LA VARA NO SE SELLA.")
        print(NL.join(L))
        return 1
    w("")

    w("E) EL REPARTO DE LA VARA, SELLADO ANTES DE COTEJAR NINGUN DOCUMENTO")
    docs_p = [p[0] for p in PUNTOS if p[0] not in NO_DOCUMENTALES]
    w("   CIFRA puntos que SE COTEJAN contra los seis documentos: %d" % len(docs_p))
    w("      %s" % ", ".join(docs_p))
    w("   CIFRA puntos que NO son documentales: %d" % len(NO_DOCUMENTALES))
    for clave in sorted(NO_DOCUMENTALES):
        w("      %-5s %s" % (clave, NO_DOCUMENTALES[clave][0]))
    w("   Y CADA UNO DE LOS TRES SE BUSCO EN LOS SEIS ANTES DE SELLARSE, con 0")
    w("   apariciones y con el control positivo en verde. EL SELLO NO ES UNA")
    w("   SUPOSICION: ES UNA MEDICION.")
    w("")
    w("   EL REPARTO POR DOCUMENTO DE LOS QUE SI SE COTEJAN:")
    por_doc = {}
    for p in PUNTOS:
        if p[0] in NO_DOCUMENTALES:
            continue
        por_doc.setdefault(p[5], []).append(p[0])
    for k in sorted(por_doc):
        w("      %-4s %-40s %d punto(s): %s"
          % (k, DOCS[k][0], len(por_doc[k]), ", ".join(por_doc[k])))
    w("")
    w("   SI EL COTEJO QUISIERA MOVER UN PUNTO DE UN LADO AL OTRO DESPUES DE")
    w("   MIRAR, ESTE SELLO LO DELATARIA.")
    w("")
    w("F) LO QUE ESTE COMPUTO NO HACE")
    w("   NO cierra la ficha, NO toca su campo `estado` y NO escribe una sola")
    w("   linea en ninguna sede. `docs/plan/OPERACIONES.jsonl` sigue en %d bytes"
      % d0)
    d1, lf1, sd1, sl1, _t2 = dos_convenciones(OPES)
    w("   en disco y %d normalizado a LF, sha256 disco %s y sha256 LF %s,"
      % (lf1, sd1, sl1))
    w("   IDENTICO al de la apertura de esta corrida: %s"
      % ("SI" if (d0, lf0, sd0, sl0) == (d1, lf1, sd1, sl1) else "NO"))
    w("")
    w("FIN DE LA VARA")
    salida = NL.join(L) + NL
    print(salida)
    io.open(os.path.join(LOOP, "SALIDA_V%d_%s.txt" % (VUELTA, a.salida)),
            "w", encoding="utf-8", newline=NL).write(salida)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
