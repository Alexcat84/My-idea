# -*- coding: utf-8 -*-
r"""_v202_t1_correccion_op_l_03.py . LA CORRECCION DECLARADA DE LA `evidencia` DE
`OP-L-03`, ESCRITA EN SU SEDE (TAREA 1 de la vuelta 202).

ADJUDICADA POR EL ACTA 201 EN SU `4.3`. El ejecutor de la 201 la propuso y no la
escribio sin adjudicacion; ahora esta adjudicada y se escribe.

PREFIJO DE GUION BAJO Y POR EL MISMO MOTIVO QUE SUS HERMANOS: la moratoria
(`AUDITOR.md` 6.3) prohibe fabricar arneses, guardas y lectores nuevos, y la
adjudicacion `4.5` del acta 199 dice que un computo de UNA vuelta, con prefijo de
guion bajo, fuera del censo y fuera de la nomina, y que no vigila a nadie, NO ES
MAQUINARIA. Este fichero es EL GEMELO de
`scripts/loop/_v201_t2_correccion_op_i_01.py`, que hizo lo mismo con `OP-I-01`:
su carril, su orden de guardas y su forma vienen de ahi.

EL CARRIL ES EL DE `OP-I-01` DE LA VUELTA 201 Y NO OTRO: banco `9.10`, POR
ADICION, como UN ELEMENTO MAS de la misma lista `evidencia`, SIN CLAVE NUEVA DE
ESQUEMA y SIN TOCAR NI TACHAR EL TEXTO VIEJO. Es la via de la gemela `OP-L-01` en
la vuelta 166, que el acta 71, seccion 6, adjudicacion 3, adjudico CON LAS
PALABRAS NO ES PARADA.

QUE TIENE QUE DECIR LA CORRECCION, Y LAS TRES COSAS SON OBLIGATORIAS:

  1. QUE EL DOCUMENTO QUE LA `evidencia` NOMBRA NO TRAE LO QUE PROMETE. El
     elemento 3 de la lista (indice 2 en base 0) nombra `LECTURAS_DIRIGIDAS.md`,
     y ese documento trae CERO apariciones del literal `reparto por acto` y CERO
     menciones de `OP-L-03`. LAS DOS CIFRAS SE MIDEN AQUI, contando el fichero, y
     NO SE COPIAN DEL ENCARGO. Y la busqueda va POSITIVA ademas de negativa,
     porque `EJECUTOR.md` 9 dice que una busqueda negativa no se puede citar
     sola.

  2. DONDE VIVE DE VERDAD EL REPARTO POR ACTO: en `docs/plan/OP_L_03_LECTURAS.jsonl`
     y en `docs/plan/OP_L_03_TRIANGULOS.jsonl`, LOS DOS NOMBRADOS, cada uno con
     SUS BYTES EXACTOS leidos del disco (`P.2`: bytes exactos, nunca redondeados,
     KB solo entre parentesis y detras del byte).

  3. LA COBERTURA REAL CON SU FECHA DE CORTE, QUE ES LA CIFRA QUE NO PUEDE
     FALTAR. El elemento 2 de la lista promete `55 pares en 29 actos`; el fichero
     de lecturas, recontado hoy, trae otra cifra. UNA EVIDENCIA CORREGIDA QUE
     PROMETA MAS DE LO QUE EXISTE ES EXACTAMENTE LO QUE `LA RUTA QUE PROMETE
     PRUEBA ES CIFRA` VINO A CAZAR.

NINGUNA CIFRA SE TECLEA: la vieja se LEE de la ficha y se cita por linea mas
indice (acta 201, `4.4`), y la de hoy se RECUENTA aqui leyendo los ficheros linea
a linea.

Y NINGUN CAMPO `estado` SE MUEVE. La vara del trabajo pendiente es el
instrumento, nunca el campo `estado` (recuadro de `AUDITOR.md` 0, decision del
fundador del 4 sep 2026). Este computo CAE EN ROJO si al reescribir la ficha
cualquier clave distinta de `evidencia` cambia de valor.

EL ORDEN DE LAS GUARDAS NO ES CASUAL, Y VIENE HEREDADO DE UNA CAIDA MEDIDA DE LA
201: la guarda de IDEMPOTENCIA va DELANTE de la que cita la cifra vieja, porque
la propia correccion CITA esa cifra verbatim, y en la segunda corrida la guarda
de la cifra caeria POR EL MOTIVO EQUIVOCADO. La 201 lo pago con una correccion
declarada de su propio fichero; aqui se hereda ya arreglado y se dice de donde
viene.

USO:
  python scripts/loop/_v202_t1_correccion_op_l_03.py
  python scripts/loop/_v202_t1_correccion_op_l_03.py --escribir
  python scripts/loop/_v202_t1_correccion_op_l_03.py --escribir --sufijo _IDEM
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

OPERACIONES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
DOC_DE_LA_EVIDENCIA = "docs/plan/LECTURAS_DIRIGIDAS.md"
FICHEROS_DEL_REPARTO = [
    "docs/plan/OP_L_03_LECTURAS.jsonl",
    "docs/plan/OP_L_03_TRIANGULOS.jsonl",
]
ID_OP = "OP-L-03"
LITERAL_REPARTO = "reparto por acto"
MARCA = "CORRECCION DECLARADA (2026-09-07, vuelta 202, TAREA 1)"
# LAS VARIANTES DE LA BUSQUEDA POSITIVA. Van en constante para que la lista que
# se publica sea LA MISMA que se busca, y no una prosa paralela.
VARIANTES = ("reparto por acto", "reparto por", "por acto", "OP-L-03",
             "OP_L_03", "OP L 03", "OP_L_03_LECTURAS", "OP_L_03_TRIANGULOS")


def medir(rel):
    """LOS BYTES DE UN FICHERO POR LAS DOS CONVENCIONES. Devuelve
    (bytes_disco, bytes_lf, texto) o None si no existe."""
    ruta = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(ruta):
        return None
    crudo = io.open(ruta, "rb").read()
    lf = crudo.replace(b"\r\n", b"\n")
    return len(crudo), len(lf), lf.decode("utf-8", errors="replace")


def reparto_de_un_fichero(texto):
    """EL REPARTO POR ACTO DE UN FICHERO JSONL, CONTADO Y NO HEREDADO. PURA:
    recibe el texto. Devuelve un diccionario con filas, lineas no JSON, actos
    distintos, actos leidos y suma de pares leidos."""
    filas = [l for l in texto.split(NL) if l.strip()]
    actos, leidos, no_leidos, pares, malas = [], [], [], 0, 0
    for l in filas:
        try:
            d = json.loads(l)
        except Exception:                                    # noqa: BLE001
            malas += 1
            continue
        if "acto" in d:
            actos.append(d["acto"])
        if d.get("leido") is True:
            leidos.append(d.get("acto"))
        elif d.get("leido") is False:
            no_leidos.append(d.get("acto"))
        pares += d.get("cifra_pares_leidos") or 0
    return dict(filas=len(filas), malas=malas, actos=actos,
                distintos=sorted(set(actos)), leidos=sorted(set(leidos)),
                no_leidos=sorted(set(no_leidos)), pares_leidos=pares)


def linea_de_la_ficha(lineas, id_op=ID_OP):
    """LA LINEA 1-INDEXADA DE UNA FICHA EN `OPERACIONES.jsonl`. PURA: recibe las
    lineas ya leidas. Devuelve None si no hay exactamente un acierto."""
    aguja = chr(34) + "id_op" + chr(34) + ": " + chr(34) + id_op + chr(34)
    hits = [i for i, l in enumerate(lineas, 1) if l.strip() and aguja in l]
    return hits[0] if len(hits) == 1 else None


def elementos_con(lista, patron):
    """LOS INDICES 1-INDEXADOS DE LOS ELEMENTOS DE UNA LISTA QUE CASAN CON UN
    PATRON. PURA. Existe para CITAR la cifra vieja por su sitio en vez de
    teclearla."""
    pat = re.compile(patron)
    return [i for i, x in enumerate(lista, 1) if pat.search(str(x))]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--escribir", action="store_true")
    ap.add_argument("--sufijo", default="")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA 202, TAREA 1 . LA CORRECCION DECLARADA DE LA evidencia DE %s" % ID_OP)
    w("adjudicada por el acta 201 en su 4.3. CARRIL: banco 9.10, POR ADICION.")
    w("=" * 78)
    w("")

    w("A) LA FICHA, LOCALIZADA POR LINEA, Y SU evidencia CITADA POR LINEA MAS")
    w("   INDICE (acta 201, 4.4). SE PUBLICAN LAS DOS NUMERACIONES DEL INDICE.")
    crudo_ops = io.open(OPERACIONES, "rb").read()
    lf_ops = crudo_ops.replace(b"\r\n", b"\n")
    lineas_ops = lf_ops.decode("utf-8").split(NL)
    w("   docs/plan/OPERACIONES.jsonl: disco %d bytes | LF %d bytes"
      % (len(crudo_ops), len(lf_ops)))
    w("   CIFRA lineas NO VACIAS: %d" % len([x for x in lineas_ops if x.strip()]))
    ln = linea_de_la_ficha(lineas_ops)
    w("   LINEA DE LA FICHA %s: %s" % (ID_OP, ln))
    if ln is None:
        w("   ROJO: la ficha no aparece exactamente una vez. NO SE ESCRIBE NADA.")
        print(NL.join(L))
        return 1
    d = json.loads(lineas_ops[ln - 1])
    ev = d.get("evidencia", [])

    # LA GUARDA DE IDEMPOTENCIA VA DELANTE, HEREDADA YA ARREGLADA DE LA CAIDA
    # DECLARADA DE LA VUELTA 201 EN SU TAREA 2: la propia correccion CITA las
    # cifras viejas verbatim, asi que una guarda de cifra puesta delante caeria
    # en la segunda corrida POR EL MOTIVO EQUIVOCADO.
    if any(MARCA in str(x) for x in ev):
        w("   LA MARCA %r YA ESTA en `evidencia`: la correccion se escribio en"
          % MARCA)
        w("   una corrida anterior. IDEMPOTENTE, NO SE ESCRIBE NADA, y se sale")
        w("   AQUI, ANTES de las guardas de cifra, porque la propia correccion")
        w("   CITA esas cifras verbatim y esas guardas caerian por el motivo")
        w("   equivocado. EL ORDEN VIENE HEREDADO DE LA CAIDA DECLARADA DE LA 201.")
        w("   CIFRA elementos de `evidencia` al entrar: %d" % len(ev))
        w("   crecimiento en disco: 0 bytes")
        w("")
        w("FIN")
        salida = NL.join(L) + NL
        print(salida)
        io.open(os.path.join(
            LOOP, "SALIDA_V202_T1_CORRECCION_OP_L_03%s.txt" % a.sufijo), "w",
            encoding="utf-8", newline=NL).write(salida)
        return 0

    w("   estado de la ficha (SE LEE, NO SE MUEVE): %r" % d.get("estado"))
    w("   fecha_corte de la ficha: %r" % d.get("fecha_corte"))
    w("   CIFRA elementos de `evidencia`: %d" % len(ev))
    for i, x in enumerate(ev):
        w("      evidencia indice %d (elemento %d): %r" % (i, i + 1, x))
    w("")

    w("B) LA PRIMERA DE LAS TRES COSAS OBLIGATORIAS: EL DOCUMENTO QUE LA")
    w("   evidencia NOMBRA NO TRAE LO QUE PROMETE. LAS DOS CIFRAS SE CUENTAN")
    w("   AQUI Y NO SE COPIAN DEL ENCARGO.")
    idx_doc = elementos_con(ev, r"LECTURAS_DIRIGIDAS\.md")
    w("   CIFRA elementos de `evidencia` que NOMBRAN LECTURAS_DIRIGIDAS.md: %d,"
      % len(idx_doc))
    w("      elementos %s (indices %s)"
      % (", ".join(str(x) for x in idx_doc) or "(ninguno)",
         ", ".join(str(x - 1) for x in idx_doc) or "(ninguno)"))
    if len(idx_doc) != 1:
        w("   ROJO: el documento no esta nombrado en exactamente un elemento.")
        w("   NO SE ESCRIBE NADA: la clausula vieja se cita, no se busca a ojo.")
        print(NL.join(L))
        return 1
    clausula_vieja = ev[idx_doc[0] - 1]
    w("   LA CLAUSULA QUE SE CORRIGE, CITADA: linea %d de" % ln)
    w("      docs/plan/OPERACIONES.jsonl, `evidencia` elemento %d (indice %d):"
      % (idx_doc[0], idx_doc[0] - 1))
    w("      %r" % clausula_vieja)
    m_doc = medir(DOC_DE_LA_EVIDENCIA)
    if m_doc is None:
        w("   ROJO: NO EXISTE %s. NO SE ESCRIBE NADA." % DOC_DE_LA_EVIDENCIA)
        print(NL.join(L))
        return 1
    bd_doc, blf_doc, t_doc = m_doc
    w("   %s: disco %d bytes | LF %d bytes | %d lineas por count(NL)"
      % (DOC_DE_LA_EVIDENCIA, bd_doc, blf_doc, t_doc.count(NL)))
    n_reparto = t_doc.count(LITERAL_REPARTO)
    n_ficha = t_doc.count(ID_OP)
    w("   CIFRA apariciones del literal %r: %d" % (LITERAL_REPARTO, n_reparto))
    w("   CIFRA menciones de %r: %d" % (ID_OP, n_ficha))
    w("   LA BUSQUEDA POSITIVA, PORQUE UNA BUSQUEDA NEGATIVA NO SE PUEDE CITAR")
    w("      SOLA (EJECUTOR.md 9). Las %d variantes buscadas y su cuenta:"
      % len(VARIANTES))
    for var in VARIANTES:
        w("      %-22s %d aparicion(es)" % (var, t_doc.count(var)))
    w("")

    w("C) LA SEGUNDA: DONDE VIVE DE VERDAD EL REPARTO POR ACTO, LOS DOS")
    w("   FICHEROS NOMBRADOS Y CON SUS BYTES EXACTOS (P.2)")
    medidas = {}
    for fr in FICHEROS_DEL_REPARTO:
        m = medir(fr)
        if m is None:
            w("   ROJO: NO EXISTE %s. NO SE ESCRIBE NADA." % fr)
            print(NL.join(L))
            return 1
        bd, blf, t = m
        rep = reparto_de_un_fichero(t)
        medidas[fr] = (bd, blf, rep)
        w("   %s" % fr)
        w("      disco %d bytes (%.1f KB) | LF %d bytes" % (bd, bd / 1024.0, blf))
        w("      CIFRA filas no vacias: %d" % rep["filas"])
        w("      CIFRA lineas que NO son JSON valido: %d" % rep["malas"])
        w("      CIFRA actos DISTINTOS: %d" % len(rep["distintos"]))
        w("      CIFRA actos con `leido` en true: %d | en false: %d"
          % (len(rep["leidos"]), len(rep["no_leidos"])))
        w("      SUMA de `cifra_pares_leidos`: %d" % rep["pares_leidos"])
        w("      los actos distintos: %s" % ", ".join(rep["distintos"]))
        if rep["malas"]:
            w("      ROJO: hay lineas que no son JSON. NO SE ESCRIBE NADA.")
            print(NL.join(L))
            return 1
    w("")

    w("D) LA TERCERA, Y ES LA QUE NO PUEDE FALTAR: LA COBERTURA REAL CONTRA LO")
    w("   QUE LA evidencia PROMETE. LA CIFRA VIEJA SE LEE DE LA FICHA.")
    idx_prom = elementos_con(ev, r"\d+\s+pares?\s+en\s+\d+\s+actos?")
    w("   CIFRA elementos de `evidencia` que prometen pares en actos: %d,"
      % len(idx_prom))
    w("      elementos %s (indices %s)"
      % (", ".join(str(x) for x in idx_prom) or "(ninguno)",
         ", ".join(str(x - 1) for x in idx_prom) or "(ninguno)"))
    if len(idx_prom) != 1:
        w("   ROJO: la promesa no esta en exactamente un elemento. NO SE ESCRIBE.")
        print(NL.join(L))
        return 1
    promesa = ev[idx_prom[0] - 1]
    mp = re.search(r"(\d+)\s+pares?\s+en\s+(\d+)\s+actos?", str(promesa))
    pares_prom, actos_prom = mp.group(1), mp.group(2)
    w("   LA PROMESA, CITADA: linea %d, `evidencia` elemento %d (indice %d):"
      % (ln, idx_prom[0], idx_prom[0] - 1))
    w("      %r" % promesa)
    w("   CIFRAS LEIDAS DE ESE ELEMENTO (no tecleadas): %s pares en %s actos"
      % (pares_prom, actos_prom))
    m_corte = re.search(r"corte puesto\s+(\d+)", str(promesa))
    w("   corte que la propia promesa declara: puesto %s"
      % (m_corte.group(1) if m_corte else "(no declarado)"))
    rep_lec = medidas[FICHEROS_DEL_REPARTO[0]][2]
    rep_tri = medidas[FICHEROS_DEL_REPARTO[1]][2]
    w("   LA COBERTURA DE HOY, RECONTADA AQUI:")
    w("      actos con ficha de lectura: %d de los %s prometidos"
      % (len(rep_lec["distintos"]), actos_prom))
    w("      de esos, con `leido` en true: %d" % len(rep_lec["leidos"]))
    w("      pares leidos, sumando `cifra_pares_leidos`: %d de los %s prometidos"
      % (rep_lec["pares_leidos"], pares_prom))
    w("      actos con ficha de triangulo: %d" % len(rep_tri["distintos"]))
    faltan_actos = int(actos_prom) - len(rep_lec["distintos"])
    faltan_pares = int(pares_prom) - rep_lec["pares_leidos"]
    w("      CIFRA actos prometidos SIN ficha de lectura: %d" % faltan_actos)
    w("      CIFRA pares prometidos SIN lectura registrada: %d" % faltan_pares)
    w("   LA PROMESA NO SE RETIRA Y NO ES UNA MENTIRA: viaja con su corte, el")
    w("      11 ago 2026, y con ese corte era lo que se iba a hacer. LO QUE LA")
    w("      CORRECCION ANADE ES CUANTO DE ESO EXISTE HOY, con SU corte.")
    w("")

    w("E) LA CORRECCION, COMPUESTA CON TODAS LAS CIFRAS MEDIDAS ARRIBA")
    correccion = (
        "%s, POR EL CARRIL DEL BANCO 9.10 Y CON EL TEXTO VIEJO ENTERO ARRIBA, "
        "SIN TACHARLO Y SIN CLAVE NUEVA DE ESQUEMA (es un elemento mas de esta "
        "misma lista evidencia, que es la via que la ficha gemela OP-L-01 uso en "
        "la vuelta 166 y que el acta 71, seccion 6, adjudicacion 3, adjudico CON "
        "LAS PALABRAS NO ES PARADA, y la misma que la vuelta 201 uso para "
        "OP-I-01). "
        "(1) LO QUE SE CORRIGE es la clausula que en esta lista dice, verbatim: "
        "'%s'. MEDIDO HOY, CON FECHA DE CORTE 2026-09-07 y contando el fichero "
        "en la vuelta 202 con scripts/loop/_v202_t1_correccion_op_l_03.py: "
        "docs/plan/LECTURAS_DIRIGIDAS.md, que mide %d bytes en disco y %d "
        "normalizados a LF, trae %d apariciones del literal 'reparto por acto' y "
        "%d menciones de OP-L-03. La busqueda se corrio tambien POSITIVA sobre "
        "%d variantes, porque una busqueda negativa no se puede citar sola "
        "(EJECUTOR.md 9). EL DOCUMENTO NO ES EL QUE TRAE EL REPARTO: LA EVIDENCIA "
        "APUNTABA AL DOCUMENTO EQUIVOCADO. "
        "(2) EL REPARTO POR ACTO VIVE, CON FECHA DE CORTE 2026-09-07, EN DOS "
        "FICHEROS Y LOS DOS SE NOMBRAN: docs/plan/OP_L_03_LECTURAS.jsonl, que "
        "mide %d bytes en disco y %d normalizados a LF, con %d filas, %d actos "
        "distintos y 0 lineas que no sean JSON valido; y "
        "docs/plan/OP_L_03_TRIANGULOS.jsonl, que mide %d bytes en disco y %d "
        "normalizados a LF, con %d filas, %d actos distintos y 0 lineas que no "
        "sean JSON valido. "
        "(3) LA COBERTURA REAL, RECONTADA HOY CON FECHA DE CORTE 2026-09-07, "
        "PORQUE UNA EVIDENCIA CORREGIDA QUE PROMETA MAS DE LO QUE EXISTE ES LO "
        "QUE LA REGLA 'LA RUTA QUE PROMETE PRUEBA ES CIFRA' VINO A CAZAR: el "
        "elemento 2 de esta misma lista promete '%s pares en %s actos' con corte "
        "11 ago 2026, y docs/plan/OP_L_03_LECTURAS.jsonl trae hoy %d actos "
        "distintos, de los cuales %d tienen leido en true y %d en false, y sus "
        "campos cifra_pares_leidos suman %d pares. O SEA: %d de los %s actos "
        "prometidos siguen sin ficha de lectura, y %d de los %s pares prometidos "
        "siguen sin lectura registrada. LA PROMESA VIEJA NO ES UNA MENTIRA Y NO "
        "SE RETIRA: con su corte era lo que se iba a hacer; lo que esta "
        "correccion anade es CUANTO DE ESO EXISTE HOY, con su propio corte. "
        "NINGUN CAMPO estado SE MUEVE con esta correccion: la vara del trabajo "
        "pendiente es el instrumento y nunca el campo estado (recuadro de "
        "AUDITOR.md 0, decision del fundador del 4 sep 2026)."
        % (MARCA, clausula_vieja, bd_doc, blf_doc, n_reparto, n_ficha,
           len(VARIANTES),
           medidas[FICHEROS_DEL_REPARTO[0]][0], medidas[FICHEROS_DEL_REPARTO[0]][1],
           rep_lec["filas"], len(rep_lec["distintos"]),
           medidas[FICHEROS_DEL_REPARTO[1]][0], medidas[FICHEROS_DEL_REPARTO[1]][1],
           rep_tri["filas"], len(rep_tri["distintos"]),
           pares_prom, actos_prom, len(rep_lec["distintos"]),
           len(rep_lec["leidos"]), len(rep_lec["no_leidos"]),
           rep_lec["pares_leidos"], faltan_actos, actos_prom,
           faltan_pares, pares_prom))
    w("   CIFRA caracteres de la correccion: %d" % len(correccion))
    w("   CIFRA guiones largos y medios: %d"
      % (correccion.count(chr(8212)) + correccion.count(chr(8211))))
    w("   LAS TRES COSAS OBLIGATORIAS, COMPROBADAS UNA A UNA DENTRO DEL TEXTO:")
    for etiqueta, aguja in (
            ("(1) el documento y sus dos ceros", "menciones de OP-L-03"),
            ("(2) OP_L_03_LECTURAS.jsonl nombrado", "OP_L_03_LECTURAS.jsonl"),
            ("(2) OP_L_03_TRIANGULOS.jsonl nombrado", "OP_L_03_TRIANGULOS.jsonl"),
            ("(3) la cobertura real", "LA COBERTURA REAL, RECONTADA HOY"),
            ("(3) la fecha de corte de hoy", "2026-09-07")):
        w("      %-40s %d aparicion(es)" % (etiqueta, correccion.count(aguja)))
    w("")
    w("   EL TEXTO DE LA CORRECCION, ENTERO:")
    for trozo in [correccion[i:i + 76] for i in range(0, len(correccion), 76)]:
        w("   | " + trozo)
    w("")

    w("F) LA GUARDA DE QUE NADA MAS SE MUEVE")
    nuevo = dict(d)
    nuevo["evidencia"] = list(ev) + [correccion]
    cambian = [k for k in set(list(d) + list(nuevo))
               if k != "evidencia" and d.get(k) != nuevo.get(k)]
    w("   CIFRA claves distintas de `evidencia` que cambian de valor: %d  %s"
      % (len(cambian), ", ".join(sorted(cambian)) or "(ninguna)"))
    w("   CIFRA claves de la ficha antes: %d | despues: %d" % (len(d), len(nuevo)))
    w("   MISMAS CLAVES Y EN EL MISMO ORDEN: %s"
      % ("SI" if list(d) == list(nuevo) else "NO, y se declara"))
    w("   CIFRA elementos de `evidencia` antes: %d | despues: %d"
      % (len(ev), len(nuevo["evidencia"])))
    w("   LOS %d VIEJOS SIGUEN IDENTICOS Y EN SU ORDEN: %s"
      % (len(ev), "SI" if nuevo["evidencia"][:len(ev)] == list(ev) else "NO"))
    w("   estado ANTES: %r | estado DESPUES: %r"
      % (d.get("estado"), nuevo.get("estado")))
    if cambian:
        w("   ROJO: alguna clave distinta de `evidencia` se movio. NO SE ESCRIBE.")
        print(NL.join(L))
        return 1
    w("")

    w("G) LA ESCRITURA")
    if a.escribir:
        linea_nueva = json.dumps(nuevo, ensure_ascii=False)
        todas = list(lineas_ops)
        todas[ln - 1] = linea_nueva
        io.open(OPERACIONES, "w", encoding="utf-8",
                newline=NL).write(NL.join(todas))
        w("   ESCRITA: la linea %d de docs/plan/OPERACIONES.jsonl" % ln)
    else:
        w("   MODO MEDICION: no se escribe nada.")
    despues = io.open(OPERACIONES, "rb").read()
    w("   docs/plan/OPERACIONES.jsonl al salir: disco %d bytes | LF %d bytes"
      % (len(despues), len(despues.replace(b"\r\n", b"\n"))))
    w("   crecimiento en disco: %d bytes" % (len(despues) - len(crudo_ops)))
    lineas_fin = despues.replace(b"\r\n", b"\n").decode("utf-8").split(NL)
    w("   CIFRA lineas NO VACIAS al salir: %d"
      % len([x for x in lineas_fin if x.strip()]))
    malas_fin = 0
    for x in lineas_fin:
        if not x.strip():
            continue
        try:
            json.loads(x)
        except Exception:                                    # noqa: BLE001
            malas_fin += 1
    w("   CIFRA lineas que NO son JSON valido al salir: %d" % malas_fin)
    w("")
    w("FIN")

    salida = NL.join(L) + NL
    print(salida)
    io.open(os.path.join(
        LOOP, "SALIDA_V202_T1_CORRECCION_OP_L_03%s.txt" % a.sufijo), "w",
        encoding="utf-8", newline=NL).write(salida)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
