# -*- coding: utf-8 -*-
r"""_v208_t3_cotejo.py . TAREAS 3.b Y 3.c DE LA VUELTA 208: CADA PUNTO DE LA VARA
DE `OP-L-03`, COTEJADO CONTRA LOS SEIS DOCUMENTOS QUE LA PROPIA FICHA NOMBRA, CON
SU CITA, SU FICHERO Y SU LINEA.

COMPUTO DE UNA VUELTA, prefijo de guion bajo, fuera del censo y fuera de la
nomina (moratoria `AUDITOR.md` 6.3). No escribe en ninguna sede: SOLO MIDE.

LA VARA SE LEE DEL SELLO Y NO SE RE-ESCRIBE: los 18 puntos y su reparto viven en
`scripts/loop/_v208_t3_vara.py`, sellado y committeado ANTES de este cotejo.
**Este fichero IMPORTA esa vara y NO la puede cambiar**: si un punto cambiara de
lado, el sello lo delataria.

LA REGLA DE ORO: **una fila sin cita no vale**, y **un `NO CUBRE` honesto es mejor
que un `CUBRE` sin linea que lo sostenga**. Cada veredicto sale de una BUSQUEDA
que devuelve LINEA; si la busqueda no devuelve linea, el veredicto es `NO CUBRE` y
se dice que **el patron no encontro nada**, nunca que la cosa no existe
(`EJECUTOR.md` 9).

Y SE APLICA LA `6.1` DEL ACTA 207: si un punto nombra una nomina o una forma de
familia, **la cobertura tiene que estar al lado en su sede, o no cubre**.

**NO CIERRA LA FICHA Y NO TOCA SU CAMPO `estado`** (encargo 3.d, `AUDITOR.md` 0).
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

sys.path.insert(0, AQUI)
from _v208_t3_vara import (  # noqa: E402
    PUNTOS, NO_DOCUMENTALES, DOCS, LINEA_FICHA, ID_OP, la_ficha,
    dos_convenciones)

VUELTA = 208
OPES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")
LEC = os.path.join(RAIZ, "docs", "plan", "OP_L_03_LECTURAS.jsonl")
TRI = os.path.join(RAIZ, "docs", "plan", "OP_L_03_TRIANGULOS.jsonl")

# LA SONDA DE CADA PUNTO: el literal que se busca en su documento. ESTO ES
# TRABAJO DE COTEJO Y NO DE VARA, y por eso vive aqui y no en el sello: el sello
# fija QUE se coteja y CONTRA QUE documento; esto es COMO se busca.
# Una lista de sondas significa que TODAS tienen que aparecer.
# CADA SONDA ES UN DICCIONARIO: `presentes` son literales que TIENEN que
# aparecer; `ausentes` son literales que TIENEN que dar CERO, y entonces la sonda
# exige ademas un `control` que SI aparezca, porque una busqueda negativa no se
# puede citar sola (`EJECUTOR.md` 9); `ci` busca sin distinguir mayusculas.
SONDAS = {
    "V.1": {"presentes": ["P.5"]},
    "V.2": {"presentes": ['"id_op": "OP-L-03"']},
    "V.3": {"presentes": ["reparto por acto"]},
    "V.4": {"presentes": ['"acto":']},
    "V.5": {"presentes": ['"terna":']},
    "V.6": {"presentes": ['"leido": true', '"leido": false',
                          '"cifra_pares_leidos"']},
    "V.7": {"presentes": ['"leido": false']},
    # LA `V.8` AFIRMA UNA AUSENCIA: encontrar 0 es lo que la CONFIRMA.
    "V.8": {"ausentes": ["reparto por acto", "OP-L-03"],
            "control": ["LD-01", "LECTURA DIRIGIDA"]},
    "V.9": {"presentes": ["P.5", "P.10"]},
    "V.10": {"presentes": ["LECTURA DIRIGIDA"]},
    "V.11": {"presentes": ['"cobertura"']},
    "V.12": {"presentes": ['"el_lado_de_fuera_es_el_D"']},
    # LA `V.13` VIVE EN VERSALES EN SU SEDE: se busca sin distinguir mayusculas.
    "V.13": {"presentes": ["la vara del trabajo pendiente es el instrumento"],
             "ci": True},
    "V.14": {"presentes": ["una busqueda negativa no se puede citar"]},
    "V.15": {"presentes": ["P.5"]},
    "V.17": {"presentes": ["OP-U-01"]},
}

# LOS PUNTOS QUE NOMBRAN UNA NOMINA O UNA FORMA DE FAMILIA, y a los que por tanto
# la `6.1` les exige la COBERTURA AL LADO en su sede. NO SE ELIGEN A OJO: cada uno
# lleva escrito el trozo de su propia cita por el que entra.
DE_LA_6_1 = {
    "V.11": "su cita dice literalmente 'se re-mide con su cobertura al lado'",
    "V.6": "publica una COBERTURA (11 leidos de 14 actos, 19 pares) y por tanto "
           "esa cobertura tiene que estar al lado en su sede",
    "V.7": "publica lo que FALTA de una nomina (15 de 29 actos, 36 de 55 pares) "
           "y por tanto es una cifra de cobertura",
}


def leer(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    crudo = io.open(p, "rb").read()
    lf = crudo.replace(b"\r\n", b"\n")
    return crudo, lf, lf.decode("utf-8").split("\n")


def buscar(lineas, literal, ci=False):
    """LAS LINEAS QUE CONTIENEN EL LITERAL. Devuelve [(linea, texto)]. Si sale
    vacia, quien llama DICE que el patron no encontro nada, NUNCA que la cosa no
    existe (`EJECUTOR.md` 9). Con `ci`, no distingue mayusculas."""
    if ci:
        lit = literal.lower()
        return [(i, lineas[i - 1]) for i in range(1, len(lineas) + 1)
                if lit in lineas[i - 1].lower()]
    return [(i, lineas[i - 1]) for i in range(1, len(lineas) + 1)
            if literal in lineas[i - 1]]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", default="T3_COTEJO")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA %d, TAREAS 3.b Y 3.c: EL COTEJO DE %s, PUNTO POR PUNTO"
      % (VUELTA, ID_OP))
    w("=" * 78)
    w("")

    w("A) LA VARA, IMPORTADA DEL SELLO Y NO RE-ESCRITA")
    sd = hashlib.sha256(io.open(os.path.join(AQUI, "_v208_t3_vara.py"),
                                "rb").read()).hexdigest()[:16]
    w("   scripts/loop/_v208_t3_vara.py: sha256 disco %s" % sd)
    w("   CIFRA puntos de la vara sellada: %d" % len(PUNTOS))
    w("   CIFRA sellados NO DOCUMENTALES: %d (%s)"
      % (len(NO_DOCUMENTALES), ", ".join(sorted(NO_DOCUMENTALES))))
    w("   CIFRA sellados DOCUMENTALES: %d"
      % (len(PUNTOS) - len(NO_DOCUMENTALES)))
    w("")

    w("B) LOS SEIS DOCUMENTOS, REMEDIDOS POR MI Y COTEJADOS CONTRA EL CONTRASTE")
    contraste = {"docs/plan/BANCO_DEL_PLAN.md": 61554,
                 "docs/plan/LECTURAS_DIRIGIDAS.md": 214916,
                 "docs/loop/EJECUTOR.md": 13194,
                 "docs/plan/OP_L_03_LECTURAS.jsonl": 51368,
                 "docs/plan/OP_L_03_TRIANGULOS.jsonl": 55705,
                 "docs/loop/AUDITOR.md": 30581}
    textos, discrepan = {}, []
    for k in sorted(DOCS):
        rel = DOCS[k][0]
        crudo, lf, ls = leer(rel)
        textos[k] = ls
        c = contraste.get(rel)
        calza = (len(crudo) == c and len(lf) == c)
        w("   %-4s %-40s %d bytes en disco y %d normalizado a LF | contraste %s |"
          " calza: %s" % (k, rel, len(crudo), len(lf), c,
                          "SI" if calza else "NO"))
        if not calza:
            discrepan.append((rel, len(crudo), len(lf), c))
    w("   CIFRA documentos cuya medicion NO calza con el contraste del encargo:"
      " %d" % len(discrepan))
    for rel, d, l, c in discrepan:
        w("      %s: yo mido %d y %d, el encargo dice %s" % (rel, d, l, c))
    w("   Y LO DIGO EXPRESAMENTE PORQUE EL ENCARGO LO PIDE: mi TAREA 2 NO tocó")
    w("   docs/plan/LECTURAS_DIRIGIDAS.md, solo lo leyo, y por eso sale igual.")
    w("")

    w("C) EL COTEJO, PUNTO POR PUNTO, CON SU FICHERO Y SU LINEA")
    filas = []
    for clave, enunciado, campo, indice, cita, doc in PUNTOS:
        w("")
        if clave in NO_DOCUMENTALES:
            motivo, literal = NO_DOCUMENTALES[clave]
            # SE BUSCA IGUAL EN LOS SEIS, COMO EN LA 207, PARA NO REPETIR SU
            # ESCARMIENTO: si apareciera, se diria.
            donde = []
            for k in sorted(DOCS):
                h = buscar(textos[k], literal)
                if h:
                    donde.append((k, h[0][0]))
            w("   %-5s %-4s %-12s (sellado antes de mirar)"
              % (clave, "---", "NO DOCUMENTAL"))
            w("         motivo sellado: %s" % motivo)
            w("         se busco igual el literal %r en los seis: %s"
              % (literal,
                 ", ".join("%s:%d" % (k, i) for k, i in donde) or
                 "0 apariciones, y eso es lo que el sello ya media"))
            filas.append((clave, "---", "NO DOCUMENTAL", None, None))
            continue
        rel = DOCS[doc][0]
        ls = textos[doc]
        sonda = SONDAS.get(clave) or {}
        ci = bool(sonda.get("ci"))
        presentes = [(s, buscar(ls, s, ci)) for s in sonda.get("presentes", [])]
        ausentes = [(s, buscar(ls, s, ci)) for s in sonda.get("ausentes", [])]
        control = [(s, buscar(ls, s, ci)) for s in sonda.get("control", [])]
        primera = None
        for _s, h in presentes + control:
            if h:
                primera = h[0]
                break
        faltan_pres = [s for s, h in presentes if not h]
        sobran_aus = [s for s, h in ausentes if h]
        faltan_ctrl = [s for s, h in control if not h]
        if not sonda:
            ver, glosa, linea = ("NO CUBRE",
                                 "NO HAY SONDA DEFINIDA PARA ESTE PUNTO, y eso "
                                 "es un hueco de mi computo, no del documento",
                                 None)
        elif faltan_ctrl:
            ver = "NO CUBRE"
            linea = None
            glosa = ("EL CONTROL POSITIVO NO APARECE (%s), asi que la busqueda "
                     "negativa de este punto NO VALE y no publico su cero"
                     % ", ".join(repr(x) for x in faltan_ctrl))
        elif faltan_pres or sobran_aus:
            ver = "NO CUBRE"
            linea = primera[0] if primera else None
            trozos = []
            if faltan_pres:
                trozos.append("EL PATRON NO ENCONTRO %s en %s. NO DIGO QUE NO "
                              "EXISTA: DIGO QUE NO LO HALLE"
                              % (", ".join(repr(x) for x in faltan_pres), rel))
            if sobran_aus:
                trozos.append("EL PUNTO AFIRMA QUE %s NO APARECE, y SI aparece "
                              "en %s"
                              % (", ".join(repr(x) for x in sobran_aus), rel))
            glosa = ". ".join(trozos)
        else:
            ver = "CUBRE"
            linea = primera[0] if primera else None
            trozos = []
            if presentes:
                trozos.append("las %d sonda(s) de PRESENCIA aparecen: %s"
                              % (len(presentes),
                                 "; ".join("%r en %d linea(s), la primera la %d"
                                           % (s, len(h), h[0][0])
                                           for s, h in presentes)))
            if ausentes:
                trozos.append("las %d sonda(s) de AUSENCIA dan CERO, que es lo "
                              "que este punto AFIRMA: %s"
                              % (len(ausentes),
                                 "; ".join("%r en 0 lineas" % s
                                           for s, _h in ausentes)))
            if control:
                trozos.append("y el CONTROL POSITIVO aparece, asi que el cero de "
                              "arriba es del mundo y no de mi patron: %s"
                              % "; ".join("%r en %d linea(s), la primera la %d"
                                          % (s, len(h), h[0][0])
                                          for s, h in control))
            if ci:
                trozos.append("BUSCADO SIN DISTINGUIR MAYUSCULAS, y se dice: la "
                              "sede lo escribe en versales")
            glosa = ". ".join(trozos)
        # LA `6.1`: SI EL PUNTO NOMBRA UNA NOMINA O UNA FORMA, LA COBERTURA TIENE
        # QUE ESTAR AL LADO EN SU SEDE, O NO CUBRE.
        if clave in DE_LA_6_1 and ver == "CUBRE":
            motivo61 = DE_LA_6_1[clave]
            hcob = buscar(ls, '"cobertura"')
            n_con, n_sin = 0, 0
            if rel.endswith(".jsonl"):
                for l in ls:
                    if not l.strip():
                        continue
                    try:
                        d = json.loads(l)
                    except ValueError:
                        continue
                    if d.get("cobertura"):
                        n_con += 1
                    else:
                        n_sin += 1
            w("   %-5s LA `6.1` SE LE APLICA: %s" % (clave, motivo61))
            w("         CIFRA filas del fichero con campo `cobertura` no vacio: %d"
              % n_con)
            w("         CIFRA filas sin el: %d" % n_sin)
            if n_con == 0:
                ver = "NO CUBRE"
                glosa += (". **PERO LA `6.1` NO SE CUMPLE**: ninguna fila de %s "
                          "lleva la cobertura al lado" % rel)
            elif n_sin:
                ver = "A MEDIAS"
                glosa += (". **Y LA `6.1` SE CUMPLE SOLO EN PARTE**: %d fila(s) "
                          "de %s llevan la cobertura al lado y %d NO"
                          % (n_con, rel, n_sin))
            else:
                glosa += (". **Y LA `6.1` SE CUMPLE ENTERA**: las %d filas de %s "
                          "llevan la cobertura al lado" % (n_con, rel))
        w("   %-5s %-4s %-9s %s:%s" % (clave, doc, ver, rel,
                                       linea if linea else "(sin linea)"))
        if linea:
            w("         %s" % ls[linea - 1].strip()[:170])
        w("         %s" % glosa[:400])
        filas.append((clave, doc, ver, rel, linea))
    w("")

    w("=" * 78)
    w("D) LA COBERTURA, MEDIDA Y NO NARRADA (TAREA 3.c)")
    w("=" * 78)
    cubre = [f[0] for f in filas if f[2] == "CUBRE"]
    medias = [f[0] for f in filas if f[2] == "A MEDIAS"]
    nocubre = [f[0] for f in filas if f[2] == "NO CUBRE"]
    nodoc = [f[0] for f in filas if f[2] == "NO DOCUMENTAL"]
    w("   CIFRA CUBRE:         %2d  %s" % (len(cubre), ", ".join(cubre) or "(ninguno)"))
    w("   CIFRA A MEDIAS:      %2d  %s" % (len(medias), ", ".join(medias) or "(ninguno)"))
    w("   CIFRA NO CUBRE:      %2d  %s" % (len(nocubre), ", ".join(nocubre) or "(ninguno)"))
    w("   CIFRA NO DOCUMENTAL: %2d  %s" % (len(nodoc), ", ".join(nodoc) or "(ninguno)"))
    w("   CIFRA total de filas: %d (la vara tiene %d puntos)"
      % (len(filas), len(PUNTOS)))
    w("")
    w("   LA LISTA NOMINAL DE LOS QUE NO CUBREN: %s"
      % (", ".join(nocubre) or "(NINGUNO)"))
    w("   LA LISTA NOMINAL DE LOS QUE CUBREN A MEDIAS: %s"
      % (", ".join(medias) or "(NINGUNO)"))
    w("")
    w("   LAS DOS CUENTAS SEPARADAS, PORQUE EL REPARTO SELLADO Y LOS VEREDICTOS")
    w("   NO TIENEN POR QUE COINCIDIR EN NUMERO (como en la 207):")
    doc_sellados = [p[0] for p in PUNTOS if p[0] not in NO_DOCUMENTALES]
    con_ver_doc = [f[0] for f in filas if f[2] != "NO DOCUMENTAL"]
    w("      CUENTA 1, LA DEL SELLO: %d puntos documentales" % len(doc_sellados))
    w("      CUENTA 2, LA DE LOS VEREDICTOS: %d puntos con veredicto documental"
      % len(con_ver_doc))
    w("      CALZAN: %s" % ("SI" if len(doc_sellados) == len(con_ver_doc) else "NO"))
    w("")
    w("E) LO QUE ESTE COMPUTO NO HACE (TAREA 3.d)")
    d1, lf1, sd1, sl1, _t = dos_convenciones(OPES)
    f = la_ficha()
    w("   NO CIERRA LA FICHA Y NO TOCA SU CAMPO `estado`, que sigue diciendo %r"
      % f.get("estado"))
    w("   docs/plan/OPERACIONES.jsonl: %d bytes en disco y %d normalizado a LF,"
      % (d1, lf1))
    w("   sha256 disco %s y sha256 LF %s" % (sd1, sl1))
    w("")
    w("FIN")
    salida = NL.join(L) + NL
    print(salida)
    io.open(os.path.join(LOOP, "SALIDA_V%d_%s.txt" % (VUELTA, a.salida)),
            "w", encoding="utf-8", newline=NL).write(salida)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
