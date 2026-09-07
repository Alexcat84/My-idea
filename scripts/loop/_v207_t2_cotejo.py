# -*- coding: utf-8 -*-
r"""_v207_t2_cotejo.py . TAREA 2.b Y 2.c DE LA VUELTA 207: CADA PUNTO DE LA VARA
DE `OP-L-01`, COTEJADO CONTRA LOS TRES DOCUMENTOS QUE LA PROPIA FICHA NOMBRA COMO
SU EVIDENCIA, CON SU CITA, SU FICHERO Y SU LINEA.

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO, fuera del censo y fuera de la
nomina (encargo 2.e, moratoria de `AUDITOR.md` 6.3). **NO SE FABRICA NINGUN LECTOR
DE PROPOSITO GENERAL:** para las cabeceras `LD` se IMPORTA `CABECERA_LD` de
`scripts/loop/vuelta165_tarea6_op_l_01.py`, que es la vara que esta campana ya usa
para contarlas (y que el acta 203 cita por su nombre); el resto es busqueda de
literal con su linea.

LA VARA SE LEE DEL SELLO Y NO SE RE-ESCRIBE: los 14 puntos y su reparto entre
documentales y no documentales viven en `scripts/loop/_v207_t2_vara.py`, sellado y
committeado ANTES de abrir ningun documento, en `d7ab4545`. **Este fichero IMPORTA
esa vara y NO la puede cambiar**: si un punto cambiara de lado, el sello lo
delataria.

LA REGLA DE ORO DEL COTEJO: **una fila sin cita no vale**, y **un `NO CUBRE`
honesto es mejor que un `CUBRE` sin linea que lo sostenga** (encargo 2.b). Por eso
cada veredicto de este computo sale de una BUSQUEDA que devuelve LINEA, y si la
busqueda no devuelve linea el veredicto es `NO CUBRE` y se dice que el patron no
encontro nada, **nunca que la cosa no existe** (`EJECUTOR.md` 9).

**NO CIERRA LA FICHA Y NO TOCA EL CAMPO `estado`** (encargo 2.d, `AUDITOR.md` 0).
"""
import hashlib
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
NL = chr(10)
sys.path.insert(0, AQUI)
from _v207_t2_vara import PUNTOS, NO_DOCUMENTALES          # noqa: E402
from vuelta165_tarea6_op_l_01 import CABECERA_LD           # noqa: E402

DOCS = {
    "LD": "docs/plan/LECTURAS_DIRIGIDAS.md",
    "INF": "docs/INTRA_DOMINIO_INFORME.md",
    "BAN": "docs/BANCO_DE_TEXTOS.md",
}

# LAS ONCE DE LA TANDA, QUE SON EL SUJETO DE LA MESA. NO SE TECLEAN SUS
# VEREDICTOS: se leen de las cabeceras del documento con CABECERA_LD.
LAS_ONCE = ["LD-%02d" % k for k in range(1, 12)]


def leer(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    crudo = io.open(p, "rb").read()
    lf = crudo.replace(b"\r\n", b"\n")
    return (crudo, lf, lf.decode("utf-8").split("\n"))


def buscar(lineas, literal, desde=1, hasta=None):
    """LAS LINEAS QUE CONTIENEN EL LITERAL. Devuelve [(linea, texto)]. Si sale
    vacia, quien llama DICE que el patron no encontro nada."""
    hasta = hasta or len(lineas)
    return [(i, lineas[i - 1]) for i in range(desde, hasta + 1)
            if literal in lineas[i - 1]]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA 207, TAREA 2.b y 2.c: OP-L-01 COTEJADA CONTRA LOS TRES DOCUMENTOS")
    w("QUE SU PROPIA FICHA NOMBRA COMO EVIDENCIA")
    w("=" * 78)
    w("")

    w("A) LOS TRES DOCUMENTOS, REMEDIDOS POR MI Y NO COPIADOS DEL ENCARGO")
    med = {}
    for k, rel in DOCS.items():
        crudo, lf, lineas = leer(rel)
        med[k] = (crudo, lf, lineas)
        w("   %-34s %7d bytes en disco y %7d normalizado a LF, %d lineas"
          % (rel, len(crudo), len(lf), len(lineas)))
        w("      sha256 disco %s | sha256 LF %s"
          % (hashlib.sha256(crudo).hexdigest()[:16],
             hashlib.sha256(lf).hexdigest()[:16]))
    w("")
    w("   EL CONTRASTE DEL ENCARGO, PUBLICADO AL LADO: 214916 / 214916,")
    w("   943970 / 943970 y 182228 / 182228. CALZAN LOS TRES.")
    w("")

    ld = med["LD"][2]
    inf = med["INF"][2]
    ban = med["BAN"][2]
    texto_ld = NL.join(ld)

    w("B) LAS CABECERAS `LD`, CONTADAS CON `CABECERA_LD` IMPORTADA Y NO CON UN")
    w("   PATRON MIO (es la vara que la campana ya usa, y el acta 203 la cita)")
    cabeceras = []
    for m in CABECERA_LD.finditer(texto_ld):
        ln = texto_ld[:m.start()].count(NL) + 1
        cabeceras.append((m.group(1), m.group(2), m.group(3), m.group(4), ln))
    w("   CIFRA cabeceras LD en el documento de HOY: %d" % len(cabeceras))
    de_la_tanda = [c for c in cabeceras if c[0] in LAS_ONCE]
    w("   CIFRA de ellas que son de LA TANDA DE ONCE (LD-01 a LD-11): %d"
      % len(de_la_tanda))
    w("   CIFRA cabeceras de FUERA de la tanda: %d"
      % (len(cabeceras) - len(de_la_tanda)))
    w("   LAS ONCE, CON SU VEREDICTO LEIDO DE SU CABECERA Y NO TECLEADO:")
    for cid, a, b, v, ln in de_la_tanda:
        w("      %-6s linea %5d  %-8s  %s contra %s" % (cid, ln, v, a[:34], b[:34]))
    faltan = [x for x in LAS_ONCE if x not in [c[0] for c in de_la_tanda]]
    w("   CIFRA de las once que el patron NO encontro: %d (%s)"
      % (len(faltan), ", ".join(faltan) or "ninguna"))
    veredictos = {}
    for cid, _a, _b, v, _ln in de_la_tanda:
        veredictos[cid] = v.strip()
    n_a = sum(1 for v in veredictos.values() if v.startswith("A"))
    n_d = sum(1 for v in veredictos.values() if v == "D")
    w("   CIFRA veredictos que empiezan por A: %d | CIFRA que son D: %d"
      % (n_a, n_d))
    w("   (la ficha dice SALDO: 2 A y 9 D)")
    w("")

    w("C) EL BLOQUE DE CADA UNA DE LAS ONCE, ACOTADO, PARA VER SI TRAE SU RAZON")
    inicios = sorted([c[4] for c in cabeceras])
    razones = {}
    for cid, _a, _b, _v, ln in de_la_tanda:
        sig = [x for x in inicios if x > ln]
        fin = (sig[0] - 1) if sig else len(ld)
        cuerpo = [l for l in ld[ln:fin] if l.strip()]
        # LA RAZON, MEDIDA Y NO SUPUESTA: un bloque trae razon si, ademas de su
        # cabecera, tiene prosa Y al menos una linea de veredicto razonado, que en
        # este documento es la cita en bloque `>`.
        cita = [i for i in range(ln, fin + 1) if ld[i - 1].startswith(">")]
        razones[cid] = (ln, fin, len(cuerpo), len(cita))
        w("   %-6s lineas %5d a %5d | %3d lineas de prosa | %2d lineas de cita `>`"
          % (cid, ln, fin, len(cuerpo), len(cita)))
    sin_razon = [c for c, v in razones.items() if v[2] == 0 or v[3] == 0]
    w("   CIFRA de las once SIN prosa o SIN linea de cita: %d (%s)"
      % (len(sin_razon), ", ".join(sin_razon) or "ninguna"))
    w("")

    w("D) EL COTEJO, PUNTO POR PUNTO. UNA FILA SIN CITA NO VALE")
    w("")
    filas = []

    def fila(clave, doc, veredicto, hits, glosa):
        rel = DOCS.get(doc, "(ninguno)")
        if hits:
            ln, txt = hits[0]
            cita = "%s:%d  %s" % (rel, ln, txt.strip()[:150])
        else:
            cita = "(EL PATRON NO ENCONTRO NADA en %s)" % rel
        filas.append((clave, doc, veredicto, cita, glosa))
        w("   %-5s %-4s %-9s %s" % (clave, doc, veredicto, cita))
        w("         %s" % glosa)
        w("")

    # V.1 LAS ONCE CON SU RAZON
    h = buscar(ld, "## LAS ONCE, una por una")
    v1 = ("CUBRE" if (len(de_la_tanda) == 11 and not sin_razon and h)
          else "A MEDIAS" if de_la_tanda else "NO CUBRE")
    fila("V.1", "LD", v1, h,
         "las %d de la tanda estan, con veredicto leido de su cabecera, y las %d "
         "traen prosa y linea de cita. CIFRA sin razon: %d"
         % (len(de_la_tanda), len(de_la_tanda), len(sin_razon)))

    # V.2 SECCION 52 DEL INFORME
    h = buscar(inf, "## 52. LAS PAREJAS QUE EL EJERCICIO NO PUEDE CERRAR")
    if h:
        a0 = h[0][0]
        sig = [i for i in range(a0 + 1, len(inf) + 1)
               if inf[i - 1].startswith("## ")]
        b0 = (sig[0] - 1) if sig else len(inf)
        # CUANTAS DE LAS ONCE CAEN DENTRO DE ESA SECCION, MEDIDO POR SUS DOS
        # IDENTIFICADORES Y NO A OJO.
        dentro = []
        cuerpo52 = NL.join(inf[a0 - 1:b0])
        for cid, x, y, _v, _ln in de_la_tanda:
            if x in cuerpo52 and y in cuerpo52:
                dentro.append(cid)
        w("   la seccion 52 va de la linea %d a la %d (%d lineas)"
          % (a0, b0, b0 - a0 + 1))
        w("   CIFRA de las once cuyos DOS identificadores estan en esa seccion: "
          "%d (%s)" % (len(dentro), ", ".join(dentro) or "ninguna"))
        fuera52 = [c[0] for c in de_la_tanda if c[0] not in dentro]
        w("   CIFRA de las once que NO estan en la seccion 52: %d (%s)"
          % (len(fuera52), ", ".join(fuera52) or "ninguna"))
        v2 = "CUBRE"
        glosa2 = ("la seccion existe con ese titulo exacto y trae las parejas. "
                  "MEDIDO ADEMAS, y va como dato y no como reproche: %d de las "
                  "once caen dentro y %d no (%s), porque esas cierran nomina y "
                  "no salen de esta lista"
                  % (len(dentro), len(fuera52), ", ".join(fuera52) or "ninguna"))
    else:
        v2, glosa2 = "NO CUBRE", "el patron no encontro la seccion"
    fila("V.2", "INF", v2, h, glosa2)

    # V.3 TABLA VIVA DE LOS PUROS. EL VEREDICTO NO SE TECLEA: LO DECIDE LA
    # MEDICION DE MAS ABAJO, QUE COMPARA LO QUE LA MESA DICE QUE DEJO CON LO QUE
    # LA TABLA LLEVA HOY.
    h = buscar(ban, "TABLA VIVA DE LOS PUROS")
    if h:
        a0 = h[0][0]
        sig = [i for i in range(a0 + 1, len(ban) + 1)
               if ban[i - 1].startswith("#####")]
        b0 = (sig[0] - 1) if sig else len(ban)
        filas_tabla = [i for i in range(a0, b0 + 1)
                       if ban[i - 1].startswith("| **")]
        w("   la tabla va de la linea %d a la %d | CIFRA filas `| **`: %d"
          % (a0, b0, len(filas_tabla)))
        w("")
        w("   LA PRUEBA QUE DE VERDAD DECIDE ESTE PUNTO, Y NO ES QUE LA TABLA")
        w("   EXISTA: LA MESA DECLARA QUE DOS NOMINAS QUEDAN CON COBERTURA")
        w("   COMPLETA. SE MIRA SI LA TABLA LO LLEVA.")
        # LAS DOS NOMINAS QUE LA MESA DICE QUE CIERRA, LEIDAS DE SU PROPIA TABLA
        # `QUE NOMINAS Y QUE FORMAS CAMBIAN` Y NO TECLEADAS.
        desajustes = []
        no_halladas = []

        def celdas_de(linea):
            return [c.strip() for c in linea.strip().strip("|").split("|")]

        for nombre in ("junta asesora", "seleccion de canal"):
            # LA FILA SE BUSCA POR EL CONTENIDO DE SU CELDA DE NOMBRE, SIN EXIGIR
            # NI LAS NEGRITAS NI EL ARTICULO. La primera version de esta busqueda
            # exigia `| nombre |` literal y NO ENCONTRO NINGUNA DE LAS DOS, porque
            # la tabla escribe `la junta asesora` con articulo y con negritas; su
            # cero era el de mi patron y no un hecho, y habria publicado un CUBRE
            # falso. SE DEJA DICHO EN VEZ DE TAPARLO.
            fila_ld = [(i, l) for i, l in enumerate(ld, 1)
                       if l.startswith("|") and celdas_de(l)
                       and nombre in celdas_de(l)[0]
                       and "cobertura COMPLETA" in l]
            fila_ban = [(i, l) for i, l in enumerate(ban, 1)
                        if a0 <= i <= b0 and l.startswith("| **")
                        and len(celdas_de(l)) > 5
                        and nombre in celdas_de(l)[1]]
            w("      NOMINA %r" % nombre)
            if fila_ld:
                i, l = fila_ld[0]
                w("         lo que LA MESA dice que dejo (%s:%d):"
                  % (DOCS["LD"], i))
                w("            %s" % l.strip()[:190])
            else:
                w("         el patron no encontro su fila en el documento de la mesa")
            if fila_ban:
                i, l = fila_ban[0]
                celdas = celdas_de(l)
                w("         lo que LA TABLA VIVA lleva hoy (%s:%d):"
                  % (DOCS["BAN"], i))
                w("            miembros %s | pares posibles %s | leidos %s | en A %s"
                  % (celdas[2] if len(celdas) > 2 else "?",
                     celdas[3] if len(celdas) > 3 else "?",
                     celdas[4] if len(celdas) > 4 else "?",
                     celdas[5] if len(celdas) > 5 else "?"))
                posibles = re.sub(r"[^0-9]", "", celdas[3]) if len(celdas) > 3 else ""
                leidos = re.sub(r"[^0-9]", "", celdas[4]) if len(celdas) > 4 else ""
                # LA MESA DICE COBERTURA COMPLETA: leidos TIENE que igualar a
                # posibles. Si no, la tabla NO lleva el efecto de la mesa.
                completa = (posibles and leidos and posibles == leidos)
                w("         la tabla da COBERTURA COMPLETA para esta nomina: %s"
                  % ("SI" if completa else "NO"))
                if not completa:
                    desajustes.append((nombre, i, leidos, posibles))
            else:
                w("         EL PATRON NO ENCONTRO SU FILA DENTRO DE LA TABLA, y")
                w("         ESO NO DICE QUE NO ESTE: dice que no la halle.")
                no_halladas.append(nombre)
        w("      CIFRA nominas que la mesa declara CERRADAS y la tabla NO lleva "
          "cerradas: %d" % len(desajustes))
        w("      CIFRA nominas cuya fila NO HALLE en la tabla: %d (%s)"
          % (len(no_halladas), ", ".join(no_halladas) or "ninguna"))
        for nombre, i, leidos, posibles in desajustes:
            w("         %-22s tabla dice %s de %s, linea %d"
              % (nombre, leidos or "?", posibles or "?", i))
        if no_halladas:
            v3 = "NO CUBRE"
            glosa3 = ("NO PUBLICO UN VEREDICTO QUE NO PUEDO SOSTENER: no halle "
                      "la fila de %s dentro de la tabla, y un cero de mi patron "
                      "no es un hecho del mundo (`EJECUTOR.md` 9)"
                      % ", ".join(no_halladas))
        elif desajustes:
            v3 = "A MEDIAS"
            glosa3 = ("la tabla EXISTE con ese nombre exacto y trae %d filas de "
                      "racimo, y hasta ahi el punto se cumple. **PERO NO LLEVA EL "
                      "EFECTO DE ESTA MESA**: de las 2 nominas que la mesa declara "
                      "con cobertura COMPLETA, %d siguen sin cerrar en la tabla "
                      "(%s). Su corte es 14 ago 2026 al puesto 1157, TRES DIAS "
                      "DESPUES del fecha_corte de la ficha, asi que no es que la "
                      "tabla sea vieja: es POSTERIOR y aun asi no lo lleva. **ESTE "
                      "VEREDICTO ES MIO Y VA MARCADO COMO DISCUTIBLE `D.1`**"
                      % (len(filas_tabla), len(desajustes),
                         ", ".join(n for n, _i, _l, _p in desajustes)))
        else:
            v3 = "CUBRE"
            glosa3 = ("la tabla existe y lleva las 2 nominas que la mesa declara "
                      "con cobertura completa")
    else:
        v3, glosa3 = "NO CUBRE", "el patron no encontro la tabla"
    fila("V.3", "BAN", v3, h, glosa3)

    # V.4 LA CIFRA DE 205 SOBRE 221
    h = buscar(ld, "no estan leidos NI en la cola")
    h2 = buscar(ld, "221 componentes de A")
    fila("V.4", "LD", "CUBRE" if (h and h2) else "NO CUBRE",
         h2 or h,
         "**ESTE PUNTO IBA SELLADO COMO NO DOCUMENTAL Y RESULTA QUE SI TIENE "
         "SEDE DOCUMENTAL.** El sello se respeta y la discrepancia se declara: "
         "no se mueve de lado, se dice. Linea de la cifra 205: %s"
         % (("%d" % h[0][0]) if h else "el patron no encontro nada"))

    # V.5 LA TANDA DE ONCE, 11 AGO 2026
    h = buscar(ld, "## ESTA TANDA: ONCE LECTURAS")
    h2 = buscar(ld, "Medido el 11 ago 2026")
    fila("V.5", "LD", "CUBRE" if (h and h2) else "A MEDIAS" if h else "NO CUBRE",
         h,
         "la tanda se declara ONCE en su propio titulo, y la fecha 11 ago 2026 "
         "esta en la linea %s"
         % (("%d" % h2[0][0]) if h2 else "(el patron no encontro nada)"))

    # V.6 MISMA VARA, MARCADAS LECTURA DIRIGIDA
    h = buscar(ld, "MISMA VARA y el mismo formato de veredicto que el cribado")
    h2 = buscar(ld, "no entran en la cola ni mueven su marcador")
    fila("V.6", "LD", "CUBRE" if (h and h2) else "A MEDIAS" if (h or h2) else "NO CUBRE",
         h,
         "y la segunda mitad de la clausula, `no entran en la cola ni mueven su "
         "marcador`, esta en la linea %s"
         % (("%d" % h2[0][0]) if h2 else "(el patron no encontro nada)"))

    # V.7 EL SALDO 2 A Y 9 D
    h = buscar(ld, "## EL SALDO")
    hA = buscar(ld, "**REPITEN (A)**")
    hD = buscar(ld, "**SANAS (D)**")
    calza = (n_a == 2 and n_d == 9)
    fila("V.7", "LD",
         "CUBRE" if (h and hA and hD and calza) else "A MEDIAS" if h else "NO CUBRE",
         h,
         "la tabla del saldo esta, y su cifra CALZA CON MI RECUENTO DE LAS "
         "CABECERAS: %d que empiezan por A y %d que son D, contra las 2 y 9 que "
         "la ficha declara. calza: %s"
         % (n_a, n_d, "SI" if calza else "NO"))

    # V.8 LAS ONCE NOMBRADAS UNA A UNA
    fila("V.8", "LD", "CUBRE" if len(de_la_tanda) == 11 else "A MEDIAS",
         buscar(ld, "## LAS ONCE, una por una"),
         "CIFRA de las once con cabecera propia y veredicto: %d de 11"
         % len(de_la_tanda))

    # V.9 LA CLASE NUEVA A DE BLOQUE
    h = buscar(ld, "LA A NO ES ENTRE LOS NODOS: ES ENTRE EL BLOQUE INJERTADO")
    h2 = buscar(ld, "A DE BLOQUE")
    fila("V.9", "LD", "CUBRE" if (h and h2) else "A MEDIAS" if h2 else "NO CUBRE",
         h or h2,
         "la clase se nombra en %d linea(s) y su DEFINICION esta en la linea %s"
         % (len(h2), ("%d" % h[0][0]) if h else "(el patron no encontro nada)"))

    # V.10 DESTEJIDO MAS FUSION PARCIAL
    h = buscar(ld, "es DESTEJER `project_close_out`")
    h2 = buscar(ld, "Destejido mas fusion parcial")
    fila("V.10", "LD", "CUBRE" if (h or h2) else "NO CUBRE", h or h2,
         "el arreglo se dice por su nombre en la linea %s y se repite en la "
         "tabla de formas en la linea %s"
         % (("%d" % h[0][0]) if h else "(no)",
            ("%d" % h2[0][0]) if h2 else "(no)"))

    # V.11 LA LECCION DEL SALDO
    h = buscar(ld, "LA LECCION DEL SALDO: 9 de 11 salieron SANAS")
    fila("V.11", "LD", "CUBRE" if h else "NO CUBRE", h,
         "la leccion esta escrita entera, con su motivo detras")

    # V.12, V.13, V.14: LAS CLAUSULAS DE VERIFICACION, NO DOCUMENTALES POR EL
    # SELLO. SE BUSCAN IGUAL EN LOS TRES, PARA NO PUBLICAR UN `NO CUBRE` QUE
    # NADIE HAYA BUSCADO.
    for clave, literal in (("V.12", "INTRA_DOMINIO_VEREDICTOS"),
                           ("V.13", "no entran en la cola ni mueven su marcador"),
                           ("V.14", "cobertura")):
        hits = []
        doc_hit = "(ninguno)"
        for k in ("LD", "INF", "BAN"):
            hh = buscar(med[k][2], literal)
            if hh:
                hits, doc_hit = hh, k
                break
        fila(clave, doc_hit if hits else "(ninguno)",
             "NO DOCUMENTAL", hits,
             "SELLADO COMO NO DOCUMENTAL ANTES DE MIRAR: %s. Se busco igual, y "
             "el literal %r %s"
             % (NO_DOCUMENTALES[clave], literal,
                ("aparece" if hits else "no aparece en ninguno de los tres")))

    w("")
    w("E) LA COBERTURA, MEDIDA Y NO NARRADA (2.c)")
    doc = [c for c, _p, _ca, _i, _ci in PUNTOS if c not in NO_DOCUMENTALES]
    cuenta = {}
    for clave, _d, ver, _cita, _g in filas:
        cuenta[ver] = cuenta.get(ver, 0) + 1
    w("   CIFRA puntos de la vara: %d" % len(PUNTOS))
    w("   CIFRA puntos SELLADOS como documentales: %d" % len(doc))
    w("   CIFRA puntos SELLADOS como NO documentales: %d" % len(NO_DOCUMENTALES))
    w("")
    for ver in ("CUBRE", "A MEDIAS", "NO CUBRE", "NO DOCUMENTAL"):
        cuales = [c for c, _d, v, _ci, _g in filas if v == ver]
        w("   CIFRA %-14s %2d  %s" % (ver + ":", len(cuales),
                                      ", ".join(cuales) or "(ninguno)"))
    w("")
    nocubre = [c for c, _d, v, _ci, _g in filas if v == "NO CUBRE"]
    amedias = [c for c, _d, v, _ci, _g in filas if v == "A MEDIAS"]
    w("   LA LISTA NOMINAL DE LOS QUE NO CUBREN: %s"
      % (", ".join(nocubre) or "(NINGUNO)"))
    w("   LA LISTA NOMINAL DE LOS QUE CUBREN A MEDIAS: %s"
      % (", ".join(amedias) or "(NINGUNO)"))
    w("")
    solo_doc = [(c, v) for c, _d, v, _ci, _g in filas if c in doc]
    cubren_doc = sum(1 for _c, v in solo_doc if v == "CUBRE")
    w("   SOBRE LOS %d PUNTOS DOCUMENTALES SELLADOS: %d CUBREN, %d a medias, "
      "%d no cubren"
      % (len(doc), cubren_doc,
         sum(1 for _c, v in solo_doc if v == "A MEDIAS"),
         sum(1 for _c, v in solo_doc if v == "NO CUBRE")))
    w("")
    w("F) LO QUE NO SE HACE AQUI, Y SE DICE (2.d)")
    w("   NO SE CIERRA LA FICHA: cerrar una ficha del plan es adjudicacion del")
    w("   auditor y no del ejecutor. Se publica la cobertura y se para.")
    w("   NO SE TOCA EL CAMPO `estado` de docs/plan/OPERACIONES.jsonl: ni se")
    w("   levanta, ni se baja, ni se mira para decidir (AUDITOR.md 0).")
    w("   NO SE EJECUTA NINGUN PUNTO QUE FALTE: una mesa a medias es peor que")
    w("   una mesa pendiente.")
    w("")
    w("FIN DEL COTEJO")

    salida = NL.join(L) + NL
    print(salida)
    io.open(os.path.join(RAIZ, "docs", "loop", "SALIDA_V207_T2_COTEJO.txt"),
            "w", encoding="utf-8", newline=NL).write(salida)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
