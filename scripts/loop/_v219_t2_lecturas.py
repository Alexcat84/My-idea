# -*- coding: utf-8 -*-
r"""_v219_t2_lecturas.py . LA TAREA 2 DE LA VUELTA 219: LAS DOS CLAUSULAS QUE
TODAVIA SE PUEDEN MOVER LEYENDO.

COMPUTO DE UNA VUELTA, prefijo de guion bajo, fuera del censo y fuera de la
nomina (moratoria de AUDITOR.md 6.3). NO ES ARNES NI GUARDA NI LECTOR NUEVO:
ES LECTURA, que es lo que la moratoria protege.

  2.a  01 FUENTES idx 1, "el material del segundo libro reubicado, no borrado".
       La cifra de las 7 menciones NO SE TECLEA NI SE HEREDA: se reproduce
       llamando a la SONDA DEL INSTRUMENTO DE LA 217 (s_segundo_libro), que es
       la misma que publico el 7, y si sale otra cifra se publican las dos y se
       para. Despues, POR CADA UNA DE LAS 7, una sola pregunta: el material de
       ese segundo libro, esta hoy en algun nodo vivo del grafo, o no esta en
       ninguno? La vara es la de la adjudicacion 4.5 del acta 218 y no se cambia
       a mitad: REUBICADO ES UN HECHO COMPROBABLE EN EL GRAFO, NO UNA FRASE
       ESCRITA EN UNA FICHA. Una sola borrada sin destino deja la clausula en
       A MEDIAS, y no se promedia.

  2.b  05 SANEO idx 1, "los tres de Incoterms con su version". Se localiza la
       anotacion del acta 120 y se publica SU LINEA leida del fichero, y la
       sede donde esa anotacion vive. Despues, por cada uno de los tres: su id,
       si declara version de Incoterms hoy, cual, y DE DONDE SALE esa version
       (el nodo y el campo que la fija). La pregunta de frontera que decide la
       clausula NO LA DECIDO YO: se mide, se escribe mi lectura con su motivo y
       SE MARCA COMO DISCUTIBLE.

  2.c  El recuento de las diecisiete, REHECHO AL CIERRE DE ESTA TAREA y no
       heredado (EJECUTOR.md 1).

  2.d  La parada feliz, solo si las diecisiete quedan en CUBRE.

EL CASO ROJO NO SE PROMETE, Y SE DICE CUAL ES CUAL (EJECUTOR.md 1). Es MAQUINA
de punta a punta, y cae en rojo por si sola: la reproduccion de la cifra de 7,
la lectura del campo fuente de cada nodo, el resolutor, la comprobacion de que
el nodo receptor del unico material mudado lleva sus cuatro actos en sus pasos,
la cuenta de pasos de cada nodo contra la que su registro publico, la
localizacion de las lineas de acta y de PENDIENTES, y la deteccion de la version
de Incoterms campo a campo. LO QUE ES MIO Y SE DECLARA COMO TAL: el reparto
tanda a libro, que va con guarda que exige que la propia ficha nombre ese libro;
y la lectura de frontera de la 2.b, que va MARCADA COMO DISCUTIBLE.

CERO ESCRITURAS EN EL PLAN Y CERO EN EL GRAFO: esta tarea solo lee.

USO:  python scripts/loop/_v219_t2_lecturas.py
"""
import hashlib
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _v217_t1_diecisiete as I217  # noqa: E402
# IMPORTAR NO ES CLONAR (acta 206, adjudicacion 6.5, linea 72517 de
# docs/loop/ACTA_AUDITOR.md, leida en esta vuelta). La sonda del segundo libro
# y el resolutor se IMPORTAN de ahi: aqui no se copia ni una linea de las dos.

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
VUELTA = int(re.search(r"_v(\d+)_", os.path.basename(os.path.abspath(__file__))).group(1))

ACTA = "docs/loop/ACTA_AUDITOR.md"
PEND = "docs/PENDIENTES.md"
PAG01 = "docs/plan/01_FUENTES.md"
PAG05 = "docs/plan/05_SANEO.md"
PAG07 = "docs/plan/07_ADUANA.md"
PAG08 = "docs/plan/08_VERIFICACION.md"
EXPEDIENTE = "docs/plan/OPERACIONES.jsonl"
INVENTARIO = "docs/plan/INVENTARIO.jsonl"
SEDES = (EXPEDIENTE, PAG08, PAG07, PAG01, PAG05, INVENTARIO)

CONTRASTE_MENCIONES = 7

# EL REPARTO DE TANDA A LIBRO ES MIO Y SE DECLARA COMO TAL. La guarda que lo
# defiende: la propia ficha del expediente tiene que NOMBRAR ese apellido en su
# texto, o el instrumento cae en rojo. No se deduce del campo fuente de los
# nodos, porque un nodo que no se toco y uno fundido por P.19 se ven IGUAL ahi.
TANDAS = {
    "OP-F-02": "Mollick",
    "OP-F-03": "Hugos",
    "OP-F-04-COL": "Coleman",
    "OP-F-04-HOR": "Horowitz",
    "OP-F-04-WEI": "Weinberg",
    "OP-F-04-RAC": "Rackham",
}

# DONDE MIRAR PARA SABER QUE MATERIAL CONCRETO ES. NO ES LA RESPUESTA: el
# instrumento localiza el ancla en docs/plan/01_FUENTES.md, publica su numero de
# linea y su texto verbatim, y CAE EN ROJO si no aparece exactamente una vez.
MATERIAL = {
    ("OP-F-03", "principio_calidad_mvp"):
        "| `principio_calidad_mvp` | **1 a 5 / 6 a 10 / 11 a 14** | el tercer bloque:",
    ("OP-F-04-COL", "keep_customers_strategy"):
        "| 8 | **`keep_customers_strategy`** | Blank \\| **Coleman** | **6** |",
    ("OP-F-04-COL", "viral_loop_marketing"):
        "| **`viral_loop_marketing`** | **`P.20`** mas `P.19` mas `P.18` |",
    ("OP-F-04-WEI", "viral_loop_marketing"):
        "| **`viral_loop_marketing`** | **`P.20`** mas `P.19` mas `P.18` |",
    ("OP-F-04-HOR", "decision_de_vender_startup"):
        "| **`decision_de_vender_startup`** | **`P.19`** | **34 a 15** |",
    ("OP-F-04-HOR", "principio_calidad_mvp"):
        "**El nodo pasa de 10 pasos a 7 y queda MULTIFUENTE LEGITIMO",
    ("OP-F-04-WEI", "coeficiente_viral"):
        "| **`coeficiente_viral`** | **`P.19`** | **16 a 8** |",
}

# LO QUE EL REGISTRO PUBLICA QUE EL NODO TIENE QUE MEDIR HOY. Es la prueba de
# que el material esta donde su registro dice: si el nodo no mide eso, ese
# registro no describe el grafo de hoy y el instrumento cae en rojo.
PASOS_PUBLICADOS = {
    "viral_loop_marketing": 23,
    "decision_de_vender_startup": 15,
    "coeficiente_viral": 8,
    "principio_calidad_mvp": 7,
    "keep_customers_strategy": 6,
}

# EL UNICO MATERIAL QUE NO VIVE EN SU PROPIO NODO, con su enrutamiento leido de
# la pagina y su destino comprobado contra el grafo, acto por acto.
MUDADO = {
    ("OP-F-03", "principio_calidad_mvp"): {
        "ancla_ruta": "| `principio_calidad_mvp` | **11 a 14** | "
                      "`ejecucion_incremental_transicion_tecnologica` |",
        "receptor": "ejecucion_incremental_transicion_tecnologica",
        "actos": [
            ("funcionalidades criticas", r"funcionalidades\s+cr[ií]ticas"),
            ("excluir las secundarias", r"[Ee]xcluir\s+deliberadamente\s+"
                                        r"caracter[ií]sticas\s+secundarias"),
            ("lanzar la minima viable", r"[Ll]anzar\s+la\s+soluci[oó]n\s+"
                                        r"m[ií]nima\s+viable"),
            ("iterar con el uso real", r"[Ii]terar\s+y\s+mejorar\s+el\s+sistema\s+"
                                       r"en\s+funci[oó]n\s+del\s+uso\s+real"),
        ],
    },
}

# LAS DOS ANOTACIONES DE LA 2.b. Ancla, no respuesta.
ANCLA_ACTA120_CAB = "# ACTA DE LA VUELTA 120 DEL AUDITOR"
ANCLA_ACTA120_31 = "**`3.1` EL DISCUTIBLE (b) NO ES DOCTRINA NUEVA"
ANCLA_ACTA120_31_ALT = "**3.1 EL DISCUTIBLE (b) NO ES DOCTRINA NUEVA"
ANCLA_PEND = "### SEXTA entrada (vuelta 121, adjudicacion del auditor en el acta 120"
ANCLA_PEND_POST = "nodo no se toca en esta vuelta"

VER_INCOTERMS = re.compile(r"Incoterms\s*((?:19|20)\d\d)", re.I)
CAMPOS = ("titulo_concepto", "resumen_teorico", "pasos_accionables",
          "entregable_esperado", "condiciones_activacion")


def leer(rel):
    return io.open(os.path.join(RAIZ, rel.replace("/", os.sep)),
                   encoding="utf-8").read().replace(chr(13) + NL, NL)


def sha16(rel):
    b = io.open(os.path.join(RAIZ, rel.replace("/", os.sep)), "rb").read()
    return (hashlib.sha256(b).hexdigest()[:16],
            hashlib.sha256(b.replace(b"\r\n", b"\n")).hexdigest()[:16])


def bytes_de(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    b = io.open(p, "rb").read()
    return os.path.getsize(p), len(b.replace(b"\r\n", b"\n"))


def localizar(lineas, ancla, desde=1, hasta=None):
    """DONDE VIVE UN ANCLA EN UN FICHERO YA LEIDO. PURA."""
    return [n for n, l in enumerate(lineas, start=1)
            if n >= desde and (hasta is None or n <= hasta) and ancla in l]


def fuentes_de(nd):
    """EL CAMPO fuente PARTIDO POR SU PROPIO SEPARADOR. PURA."""
    fu = nd.get("fuente")
    if not isinstance(fu, str):
        return []
    return [x.strip() for x in fu.split(" | ") if x.strip()]


def campo_con_version(nd):
    """EL CAMPO DEL NODO DONDE VIVE LA VERSION DE INCOTERMS. PURA.

    Devuelve (campo, version, fragmento) o (None, None, None)."""
    for c in CAMPOS:
        v = nd.get(c)
        trozos = v if isinstance(v, list) else ([v] if v else [])
        for t in trozos:
            m = VER_INCOTERMS.search(str(t))
            if m:
                i = max(0, m.start() - 60)
                return c, m.group(0), str(t)[i:m.end() + 60]
    return None, None, None


def main():
    out = []
    fallos = 0

    def w(s=""):
        out.append(s)

    w("=" * 78)
    w("TAREA 2 DE LA VUELTA %d: LAS DOS CLAUSULAS QUE TODAVIA SE PUEDEN MOVER "
      "LEYENDO" % VUELTA)
    w("=" * 78)
    w("")
    entrada = {}
    w("LOS SHA256 DE LAS SEDES DEL PLAN, AL ENTRAR, POR LAS DOS CONVENCIONES:")
    for rel in SEDES:
        entrada[rel] = sha16(rel)
        bd, bl = bytes_de(rel)
        w("   %s: %d bytes en disco y %d normalizado a LF, sha256 disco %s y "
          "sha256 LF %s" % ((rel, bd, bl) + entrada[rel]))
    w("")

    N = I217.V150.grafo("WORK")
    res = I217.V150.resolutor(N)
    ops = {}
    for n, l in enumerate(I217.lineas(I217.EXPEDIENTE), start=1):
        if l.strip():
            d = json.loads(l)
            ops[d["id_op"]] = (n, d)
    vivos = [k for k, v in N.items() if not v.get("deprecado")]
    w("EL GRAFO DE HOY, MEDIDO Y NO HEREDADO: %d nodos en el censo, %d vivos."
      % (len(N), len(vivos)))
    w("EL EXPEDIENTE DE HOY: %d fichas leidas de %s." % (len(ops), EXPEDIENTE))
    w("")

    # =================================================================== 2.a
    w("=" * 78)
    w("2.a. 01 FUENTES idx 1: EL MATERIAL DEL SEGUNDO LIBRO, REUBICADO O "
      "BORRADO")
    w("=" * 78)
    w("")
    w("   PRIMERO LA CIFRA, REPRODUCIDA CON MI PROPIO INSTRUMENTO Y NO "
      "HEREDADA. La sonda es la MISMA que publico el 7, importada y no clonada: "
      "s_segundo_libro de scripts/loop/_v217_t1_diecisiete.py.")
    ver01, cifras01 = I217.s_segundo_libro({"N": N, "ops": ops})
    for c in cifras01:
        w("      sonda> " + c)
    menciones = []
    for c in cifras01:
        m = re.match(r"^\s*AUN CON DOS O MAS FUENTES>\s*(\S+)\s*/\s*(\S+),\s*"
                     r"(\d+) fuentes$", c)
        if m:
            menciones.append((m.group(1), m.group(2), int(m.group(3))))
    w("")
    w("   CIFRA menciones que TODAVIA declaran mas de una fuente, MEDIDA HOY "
      "POR MI: %d | CIFRA que el acta 217 publica en su linea 77346: %d"
      % (len(menciones), CONTRASTE_MENCIONES))
    if len(menciones) != CONTRASTE_MENCIONES:
        fallos += 1
        w("      PARADA: las dos cifras no calzan y NO SE RESUELVE COPIANDO "
          "(EJECUTOR.md 2). Se publican las dos y se para.")
        w("")
    else:
        w("      LAS DOS CIFRAS CALZAN. Sigo.")
        w("")
    w("   EL VEREDICTO QUE LA SONDA DA HOY POR SU PROPIO DETECTOR (el estrecho, "
      "el que mira si el nodo sigue declarando dos fuentes): %s" % ver01)
    w("   Y ESE NO ES EL DETECTOR QUE EL ENCARGO MANDA USAR. LA VARA ES LA DE "
      "LA ADJUDICACION 4.5 DEL ACTA 218: REUBICADO ES UN HECHO COMPROBABLE EN "
      "EL GRAFO, NO UNA FRASE ESCRITA EN UNA FICHA. La pregunta, una por "
      "mencion: el material de ese segundo libro, ESTA HOY EN ALGUN NODO VIVO "
      "DEL GRAFO, o NO ESTA EN NINGUNO?")
    w("")

    w("   LA GUARDA DEL REPARTO DE TANDA A LIBRO, QUE ES MIO Y VA CON GUARDA:")
    for op_id, libro in sorted(TANDAS.items()):
        if op_id not in ops:
            fallos += 1
            w("      ROJO: la ficha %s no esta en el expediente." % op_id)
            continue
        texto_ficha = json.dumps(ops[op_id][1], ensure_ascii=False)
        nombra = libro.lower() in texto_ficha.lower()
        w("      %-12s -> %-9s | la propia ficha (linea %d del expediente) "
          "nombra ese apellido: %s"
          % (op_id, libro, ops[op_id][0], "SI" if nombra else "NO"))
        if not nombra:
            fallos += 1
    w("")

    ls01 = leer(PAG01).split(NL)
    w("   LA PAGINA DONDE VIVEN LOS REGISTROS DE ESTA CLAUSULA, MEDIDA HOY: "
      "%s, %d lineas leidas." % (PAG01, len(ls01)))
    w("")

    filas_a = []
    vivas, borradas = 0, 0
    for op_id, nid, nfu in menciones:
        libro = TANDAS.get(op_id)
        nd = N.get(nid)
        w("   " + "-" * 72)
        w("   MENCION> ficha %s | nodo %s | libro de la tanda: %s"
          % (op_id, nid, libro))
        if nd is None:
            fallos += 1
            borradas += 1
            w("      ROJO: el nodo no existe en el grafo de hoy.")
            filas_a.append((op_id, nid, libro, "NO EXISTE", "(ninguno)",
                            "el nodo que la declara no esta en el grafo"))
            continue
        dep = bool(nd.get("deprecado"))
        s = res(nid)
        fus = fuentes_de(nd)
        declara = [f for f in fus if libro and libro.lower() in f.lower()]
        npasos = len(nd.get("pasos_accionables") or [])
        w("      el nodo que la declara: %s | vivo: %s | resolutor -> %s | "
          "fuentes hoy: %d | pasos hoy: %d"
          % (nid, "NO" if dep else "SI", s, len(fus), npasos))
        for f in fus:
            w("         fuente> %s" % f)
        pub = PASOS_PUBLICADOS.get(nid)
        if pub is not None:
            w("      CIFRA pasos medidos hoy: %d | CIFRA que su registro "
              "publica: %d | %s" % (npasos, pub,
                                    "CALZA" if npasos == pub else "NO CALZA"))
            if npasos != pub:
                fallos += 1

        ancla_m = MATERIAL.get((op_id, nid))
        donde_m = localizar(ls01, ancla_m) if ancla_m else []
        if len(donde_m) != 1:
            fallos += 1
            w("      ROJO: el ancla del material aparece %d vez(ces) en %s y se "
              "exige 1." % (len(donde_m), PAG01))
            material = "(sin localizar)"
        else:
            material = ls01[donde_m[0] - 1].strip()
            w("      QUE MATERIAL CONCRETO ES, LEIDO DE %s LINEA %d:"
              % (PAG01, donde_m[0]))
            w("         %s" % material)

        if declara:
            vivas += 1
            w("      DONDE VIVE HOY: EN EL PROPIO NODO, que es un nodo VIVO del "
              "grafo. El campo fuente sigue declarando el libro de la tanda "
              "(%s), que es lo que P.19 punto 2 obliga a dejar intacto cuando "
              "el material se funde dentro en vez de salir." % declara[0])
            w("      RESUELTO CON EL RESOLUTOR DELANTE: %s -> %s, y ese nodo "
              "esta %s." % (nid, s, "DEPRECADO" if dep else "VIVO"))
            if dep:
                fallos += 1
                w("      ROJO: el nodo que lo aloja esta deprecado.")
            filas_a.append((op_id, nid, libro, "VIVE", s,
                            "fundido DENTRO del propio nodo, fuente intacta"))
            continue

        w("      EL NODO YA NO DECLARA ESE LIBRO: el material NO esta en el, y "
          "hay que decir DONDE ESTA o dar la constancia de que no esta en "
          "ninguno.")
        mud = MUDADO.get((op_id, nid))
        if mud is None:
            fallos += 1
            borradas += 1
            w("      ROJO: no hay enrutamiento leido para esta mencion. Se "
              "cuenta como BORRADA SIN DESTINO.")
            filas_a.append((op_id, nid, libro, "BORRADA SIN DESTINO",
                            "(ninguno)", "no hay destino leido"))
            continue
        donde_r = localizar(ls01, mud["ancla_ruta"])
        if len(donde_r) != 1:
            fallos += 1
            w("      ROJO: el ancla del enrutamiento aparece %d vez(ces) y se "
              "exige 1." % len(donde_r))
            filas_a.append((op_id, nid, libro, "SIN RUTA LEIDA", "(ninguno)",
                            "el enrutamiento no se localizo"))
            continue
        w("      EL ENRUTAMIENTO, LEIDO DE %s LINEA %d:" % (PAG01, donde_r[0]))
        w("         %s" % ls01[donde_r[0] - 1].strip())
        rid = mud["receptor"]
        rnd = N.get(rid)
        if rnd is None or rnd.get("deprecado"):
            fallos += 1
            borradas += 1
            w("      ROJO: el receptor %s no existe o esta deprecado." % rid)
            filas_a.append((op_id, nid, libro, "DESTINO MUERTO", rid,
                            "el receptor no es un nodo vivo"))
            continue
        rs = res(rid)
        pasos_r = rnd.get("pasos_accionables") or []
        w("      EL RECEPTOR, MEDIDO CONTRA EL GRAFO: %s | vivo: SI | resolutor "
          "-> %s | pasos: %d" % (rid, rs, len(pasos_r)))
        w("      Y EL MATERIAL SE COMPRUEBA ACTO POR ACTO EN SUS PASOS, no por "
          "creer al registro:")
        faltan = 0
        for etiqueta, patron in mud["actos"]:
            hit = [(i, p) for i, p in enumerate(pasos_r, start=1)
                   if re.search(patron, p)]
            if len(hit) == 1:
                w("         acto '%s' -> PASO %d: %s"
                  % (etiqueta, hit[0][0], hit[0][1]))
            else:
                faltan += 1
                w("         acto '%s' -> NO APARECE (o aparece %d veces)"
                  % (etiqueta, len(hit)))
        w("      CIFRA actos del material hallados en el receptor: %d | CIFRA "
          "que el registro promete: %d"
          % (len(mud["actos"]) - faltan, len(mud["actos"])))
        if faltan:
            fallos += 1
            borradas += 1
            filas_a.append((op_id, nid, libro, "INCOMPLETO EN SU DESTINO", rid,
                            "faltan %d actos en el receptor" % faltan))
            continue
        vivas += 1
        filas_a.append((op_id, nid, libro, "VIVE", rid,
                        "mudado al receptor, los %d actos comprobados en sus "
                        "pasos" % len(mud["actos"])))
    w("   " + "-" * 72)
    w("")
    w("   CIFRA menciones cuyo material VIVE en un nodo vivo del grafo: %d | "
      "CIFRA menciones BORRADAS SIN DESTINO: %d | CIFRA total de menciones: %d"
      % (vivas, borradas, len(menciones)))
    w("")
    w("   LA TABLA, ARMADA DE LO MEDIDO ARRIBA Y NO TECLEADA:")
    w("| # | ficha | nodo que la declara | libro de la tanda | vive hoy | donde vive hoy (resuelto) | como |")
    w("|---:|---|---|---|---|---|---|")
    for i, (op_id, nid, libro, est, donde, como) in enumerate(filas_a, start=1):
        w("| %d | `%s` | `%s` | %s | **%s** | `%s` | %s |"
          % (i, op_id, nid, libro, est, donde, como))
    w("   CIFRA filas armadas: %d | CIFRA que deberia haber: %d"
      % (len(filas_a), len(menciones)))
    if len(filas_a) != len(menciones):
        fallos += 1
    w("")
    sube_01 = (len(menciones) == CONTRASTE_MENCIONES and borradas == 0
               and vivas == len(menciones))
    w("   LA VARA, APLICADA SIN PROMEDIAR: si las %d estan reubicadas, la "
      "clausula sube a CUBRE por lectura; UNA SOLA borrada sin destino la deja "
      "en A MEDIAS y esa una se nombra con su id." % len(menciones))
    w("   CIFRA borradas sin destino: %d | CIFRA que la vara tolera: 0"
      % borradas)
    if borradas:
        for f in filas_a:
            if f[3] != "VIVE":
                w("   LA QUE NO CUBRE, CON SU ID: %s / %s, %s"
                  % (f[0], f[1], f[3]))
    w("   VEREDICTO DE 01 FUENTES idx 1: %s"
      % ("CUBRE" if sube_01 else "A MEDIAS"))
    w("")

    # =================================================================== 2.b
    w("=" * 78)
    w("2.b. 05 SANEO idx 1: LOS TRES DE INCOTERMS CON SU VERSION")
    w("=" * 78)
    w("")
    lsa = leer(ACTA).split(NL)
    lsp = leer(PEND).split(NL)
    w("   LOS DOS FICHEROS DE LAS CITAS, MEDIDOS HOY: %s con %d lineas, y %s "
      "con %d lineas." % (ACTA, len(lsa), PEND, len(lsp)))
    cab120 = localizar(lsa, ANCLA_ACTA120_CAB)
    w("   CIFRA lineas donde empieza el acta 120: %d | CIFRA que se exige: 1"
      % len(cab120))
    if len(cab120) != 1:
        fallos += 1
        i120 = 1
    else:
        i120 = cab120[0]
        w("      EL ACTA 120 EMPIEZA EN LA LINEA %d, LEIDA DEL FICHERO> %s"
          % (i120, lsa[i120 - 1]))
    d31 = localizar(lsa, ANCLA_ACTA120_31, desde=i120) \
        or localizar(lsa, ANCLA_ACTA120_31_ALT, desde=i120)
    w("   CIFRA lineas donde vive la adjudicacion 3.1 del acta 120: %d | CIFRA "
      "que se exige: 1" % len(d31))
    if len(d31) != 1:
        fallos += 1
    else:
        n31 = d31[0]
        w("      LA ADJUDICACION 3.1 DEL ACTA 120 VIVE EN LA LINEA %d, Y ESTAS "
          "SON SUS LINEAS LEIDAS DEL FICHERO:" % n31)
        k = n31
        while k <= len(lsa) and lsa[k - 1].strip():
            w("         %d> %s" % (k, lsa[k - 1]))
            k += 1
    w("")
    dpend = localizar(lsp, ANCLA_PEND)
    w("   Y LA ANOTACION EN SU SEDE, QUE ES DONDE EL ACTA 120 LA MANDO. CIFRA "
      "lineas donde vive la SEXTA entrada de %s: %d | CIFRA que se exige: 1"
      % (PEND, len(dpend)))
    if len(dpend) != 1:
        fallos += 1
    else:
        npd = dpend[0]
        w("      LA SEXTA ENTRADA VIVE EN LA LINEA %d DE %s, LEIDA DEL FICHERO> "
          "%s" % (npd, PEND, lsp[npd - 1].strip()))
        dpost = localizar(lsp, ANCLA_PEND_POST, desde=npd, hasta=npd + 40)
        w("      CIFRA lineas de esa entrada que dicen que el nodo NO se toca: "
          "%d | CIFRA que se exige: 1" % len(dpost))
        if len(dpost) != 1:
            fallos += 1
        else:
            k = dpost[0]
            while k <= len(lsp) and lsp[k - 1].strip():
                w("         %d> %s" % (k, lsp[k - 1]))
                k += 1
    w("")

    ln_ops2, ficha2 = ops["OP-S-02"]
    nom = ficha2.get("nodos") or []
    w("   EL SUJETO SON LOS TRES DE LA NOMINA DE OP-S-02, leidos del expediente "
      "(linea %d) y no tecleados. CIFRA nodos de la nomina: %d | CIFRA que la "
      "clausula escribe: 3" % (ln_ops2, len(nom)))
    if len(nom) != 3:
        fallos += 1
    w("   EL ESTADO DE LA FICHA, LEIDO DEL EXPEDIENTE: %s"
      % ficha2.get("estado"))
    w("")
    filas_b = []
    for nid in nom:
        nd = N.get(nid)
        w("   " + "-" * 72)
        if nd is None:
            fallos += 1
            w("   ROJO: %s no existe en el grafo." % nid)
            filas_b.append((nid, "NO EXISTE", "(ninguna)", "(ninguno)",
                            "el nodo no esta en el grafo"))
            continue
        dep = bool(nd.get("deprecado"))
        s = res(nid)
        c_p, v_p, frag_p = campo_con_version(nd)
        snd = N.get(s) if s else None
        c_s, v_s, frag_s = campo_con_version(snd) if snd else (None, None, None)
        cita_s = ("incoterms" in I217.texto_de(snd).lower()) if snd else False
        w("   NODO> %s | vivo: %s | resolutor -> %s"
          % (nid, "NO" if dep else "SI", s))
        w("      declara version en SU PROPIO texto: %s%s"
          % ("SI, " + v_p if v_p else "NO",
             " (campo %s)" % c_p if c_p else ""))
        if frag_p:
            w("         fragmento> ...%s..." % frag_p.replace(NL, " "))
        w("      su SUPERVIVIENTE es %s | ese cita Incoterms: %s | y declara "
          "version: %s%s" % (s, "SI" if cita_s else "NO",
                             "SI, " + v_s if v_s else "NO",
                             " (campo %s)" % c_s if c_s else ""))
        if frag_s and s != nid:
            w("         fragmento del superviviente> ...%s..."
              % frag_s.replace(NL, " "))
        if v_s:
            de_donde = ("%s, campo %s" % (s, c_s))
            estado = "SI, por su superviviente" if s != nid else "SI, en el propio nodo"
        else:
            de_donde = "(ninguno: ni el nodo ni su superviviente la fijan)"
            estado = "NO"
        w("      DE DONDE SALE LA VERSION: %s" % de_donde)
        filas_b.append((nid, estado, v_s or "(ninguna)", de_donde,
                        "vivo" if not dep else "deprecado, resuelve a %s" % s))
    w("   " + "-" * 72)
    w("")
    con_ver = sum(1 for f in filas_b if f[1].startswith("SI"))
    w("   CIFRA de los tres que llegan a una version de Incoterms, por si "
      "mismos o por su superviviente: %d de %d" % (con_ver, len(nom)))
    w("")
    w("   LA TABLA, ARMADA DE LO MEDIDO ARRIBA Y NO TECLEADA:")
    w("| # | nodo de la nomina | declara version hoy | cual | de donde sale | estado del nodo |")
    w("|---:|---|---|---|---|---|")
    for i, (nid, est, cual, donde, edo) in enumerate(filas_b, start=1):
        w("| %d | `%s` | **%s** | %s | %s | %s |"
          % (i, nid, est, cual, donde, edo))
    w("   CIFRA filas armadas: %d | CIFRA que deberia haber: %d"
      % (len(filas_b), len(nom)))
    if len(filas_b) != len(nom):
        fallos += 1
    w("")
    w("   LA PREGUNTA QUE DECIDE LA CLAUSULA ES DE FRONTERA Y NO DE CONTEO, Y "
      "NO LA DECIDO YO: un nodo que la campana DIFIRIO A PROPOSITO Y POR "
      "DECISION ESCRITA, cuenta como incumplimiento de la clausula o como fuera "
      "de su alcance?")
    w("   LO MEDIDO: %d de %d llegan a la version; el que no es el tercero, y "
      "su motivo esta escrito en las dos sedes localizadas arriba." % (con_ver,
                                                                       len(nom)))
    w("   MI LECTURA, CON SU MOTIVO Y MARCADA COMO DISCUTIBLE: la escribo en el "
      "reporte, en la seccion de discutibles, y NO la aplico al recuento. La "
      "clausula se queda donde estaba mientras la frontera no se adjudique.")
    w("   VEREDICTO DE 05 SANEO idx 1 QUE ESTA TAREA APLICA: A MEDIAS (SIN "
      "MOVER), y la razon es que la frontera es del auditor y no mia.")
    w("")

    # =================================================================== 2.c
    w("=" * 78)
    w("2.c. EL RECUENTO DE LAS DIECISIETE, REHECHO AL CIERRE DE ESTA TAREA")
    w("=" * 78)
    w("")
    rel_t1 = "docs/loop/SALIDA_V%d_T1_RECORRIDA_DEL_LECTOR.txt" % VUELTA
    t1 = leer(rel_t1)
    filas17 = []
    dentro = False
    for l in t1.split(NL):
        if "LA TABLA ENTERA AL CIERRE DE ESTA TAREA" in l:
            dentro = True
            continue
        if not dentro:
            continue
        m = re.match(r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*(\d+)\s*\|\s*"
                     r"(CUBRE|A MEDIAS|NO CUBRE)(?:[^|]*)\|\s*(.*?)\s*\|$", l)
        if m:
            filas17.append([int(m.group(1)), m.group(2), int(m.group(3)),
                            m.group(4), m.group(5)])
        elif filas17 and not l.startswith("|"):
            break
    w("   LA FUENTE DE LAS 17 FILAS ES MI PROPIA CORRIDA DE HOY, sellada en "
      "``%s``." % rel_t1)
    w("   CIFRA filas armadas leyendo ese fichero: %d | CIFRA que deberia "
      "haber: 17" % len(filas17))
    if len(filas17) != 17:
        fallos += 1
    antes = {}
    for f in filas17:
        antes[f[3]] = antes.get(f[3], 0) + 1
    w("   EL REPARTO QUE LA TAREA 1 DEJO MEDIDO: CUBRE %d | A MEDIAS %d | NO "
      "CUBRE %d" % (antes.get("CUBRE", 0), antes.get("A MEDIAS", 0),
                    antes.get("NO CUBRE", 0)))
    NUEVOS = {("01 FUENTES", 1): "CUBRE" if sube_01 else "A MEDIAS"}
    subidas = 0
    for f in filas17:
        k = (f[1], f[2])
        if k in NUEVOS and f[3] != NUEVOS[k]:
            w("   SUBE POR LECTURA: %s idx %d, de %s a %s"
              % (f[1], f[2], f[3], NUEVOS[k]))
            f.append(f[3])
            f[3] = NUEVOS[k]
            subidas += 1
    w("   CIFRA clausulas que esta tarea mueve: %d | CIFRA que el encargo pone "
      "en juego: 2 (y la de 05 SANEO no se mueve porque su frontera es del "
      "auditor)" % subidas)
    ahora = {}
    for f in filas17:
        ahora[f[3]] = ahora.get(f[3], 0) + 1
    n_cubre = ahora.get("CUBRE", 0)
    n_medias = ahora.get("A MEDIAS", 0)
    n_no = ahora.get("NO CUBRE", 0)
    w("")
    w("   CIFRA clausulas en CUBRE AL CIERRE DE LA TAREA 2: %d de 17 | CIFRA "
      "que dejo la TAREA 1: %d" % (n_cubre, antes.get("CUBRE", 0)))
    w("   CIFRA clausulas en A MEDIAS AL CIERRE DE LA TAREA 2: %d de 17 | CIFRA "
      "que dejo la TAREA 1: %d" % (n_medias, antes.get("A MEDIAS", 0)))
    w("   CIFRA clausulas en NO CUBRE AL CIERRE DE LA TAREA 2: %d de 17 | CIFRA "
      "que dejo la TAREA 1: %d" % (n_no, antes.get("NO CUBRE", 0)))
    w("")
    w("   LA TABLA ENTERA AL CIERRE DE ESTA TAREA:")
    w("| # | fila | idx | veredicto | la clausula, VERBATIM |")
    w("|---:|---|---:|---|---|")
    for f in filas17:
        nota = (" (SUBE POR LECTURA: la TAREA 1 la dejo en %s)" % f[5]) \
            if len(f) > 5 else ""
        w("| %d | %s | %d | %s%s | %s |" % (f[0], f[1], f[2], f[3], nota, f[4]))
    w("   CIFRA filas de la tabla del cierre: %d | CIFRA que deberia haber: 17"
      % len(filas17))
    w("")
    resto17 = [f for f in filas17 if f[3] != "CUBRE"]
    w("   LAS QUE SIGUEN SIN CUBRIR, CON SU FILA, SU INDICE Y SU CIFRA:")
    for f in resto17:
        w("   %-14s idx %d | %-9s | %s" % (f[1], f[2], f[3], f[4]))
    w("   CIFRA clausulas que siguen sin cubrir: %d" % len(resto17))
    w("")

    # =================================================================== 2.d
    w("=" * 78)
    w("2.d. LA PARADA FELIZ, MEDIDA CONTRA SU PROPIA LETRA Y NO PROPUESTA A OJO")
    w("=" * 78)
    w("")
    w("   LA CONDICION PIDE QUE LAS DIECISIETE QUEDEN EN CUBRE.")
    w("   CIFRA en CUBRE: %d | CIFRA que la condicion exige: 17" % n_cubre)
    w("   LA CONDICION SE CUMPLE: %s" % ("SI" if n_cubre == 17 else "NO"))
    w("   POR TANTO, LA PARADA FELIZ: %s"
      % ("SE PROPONE, con su medicion delante y sin declarar nada consumado"
         if n_cubre == 17 else "NO SE PROPONE, y las que faltan van arriba con "
                               "su fila, su indice y su cifra"))
    w("")

    # ============================================================== EL CIERRE
    w("=" * 78)
    w("ESTA TAREA SOLO LEE, Y SE PRUEBA CON LOS SHA")
    w("=" * 78)
    for rel in SEDES:
        sal = sha16(rel)
        bd, bl = bytes_de(rel)
        w("   %s AL ENTRAR: sha256 disco %s y sha256 LF %s"
          % ((rel,) + entrada[rel]))
        w("   %s AL SALIR:   sha256 disco %s y sha256 LF %s, %d bytes en disco "
          "y %d normalizado a LF" % ((rel,) + sal + (bd, bl)))
        if sal != entrada[rel]:
            fallos += 1
            w("   ROJO: %s SE MOVIO." % rel)
    coinciden = all(sha16(r) == entrada[r] for r in SEDES)
    w("   LOS %d SHA DE LAS SEDES DEL PLAN COINCIDEN AL ENTRAR Y AL SALIR POR "
      "LAS DOS CONVENCIONES: %s" % (len(SEDES) * 2, "SI" if coinciden else "NO"))
    w("")
    w("   EL CASO ROJO, DICHO CUAL ES CUAL: la reproduccion del 7, el campo "
      "fuente, el resolutor, la cuenta de pasos contra la publicada, los cuatro "
      "actos del material mudado dentro de su receptor, las lineas de acta y de "
      "PENDIENTES y la version de Incoterms campo a campo CAEN EN ROJO por si "
      "solas y estan contadas arriba. LO MIO ES EL REPARTO DE TANDA A LIBRO, "
      "que va con guarda que exige que la propia ficha nombre el apellido, Y LA "
      "LECTURA DE FRONTERA DE LA 2.b, QUE VA MARCADA COMO DISCUTIBLE: para esa "
      "NO HAY CASO ROJO AUTOMATICO y se declara en vez de fabricarse uno que se "
      "apruebe solo.")
    w("")
    w("CIFRA comprobaciones que fallan: %d" % fallos)
    w("VERDE: la TAREA 2 sale limpia." if not fallos
      else "ROJO: la TAREA 2 tiene comprobaciones que fallan.")

    texto = NL.join(out) + NL
    destino = os.path.join(LOOP, "SALIDA_V%d_T2_LECTURAS.txt" % VUELTA)
    io.open(destino, "w", encoding="utf-8", newline=NL).write(texto)
    sys.stdout.write(texto)
    sys.stdout.write(NL + "SELLADO EN %s, %d bytes%s"
                     % (os.path.basename(destino), os.path.getsize(destino), NL))
    return 0 if not fallos else 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
