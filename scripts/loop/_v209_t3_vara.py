# -*- coding: utf-8 -*-
r"""_v209_t3_vara.py . TAREA 3.a DE LA VUELTA 209: LA VARA DE `OP-L-02`, SELLADA
EN SU PROPIO COMMIT ANTES DE COTEJAR NINGUN DOCUMENTO.

COMPUTO DE UNA VUELTA, prefijo de guion bajo, fuera del censo y fuera de la
nomina (moratoria `AUDITOR.md` 6.3). No escribe en ninguna sede: SOLO MIDE Y
SELLA.

POR QUE VA EN SU PROPIO COMMIT: una vara escrita despues de mirar se acomoda a lo
que se vio. Este fichero se committea ANTES del cotejo, y el cotejo lo IMPORTA sin
poder cambiarlo. Es el metodo que la 207 uso con `OP-L-01` y la 208 con
`OP-L-03`, las dos veces bien, y por eso se repite igual.

LA SEDE FINA ES `campo[indice]` Y NO UN NUMERO DE LINEA: la ficha entera vive en
UNA sola linea de `docs/plan/OPERACIONES.jsonl`, la **42**. Decir "linea 42"
dieciocho veces no localiza nada.

LO QUE ESTA FICHA TIENE DE DISTINTO, Y ES LO QUE EL ENCARGO AVISA MEDIDO:
  . `evidencia` TIENE UN SOLO ELEMENTO Y ES PROSA. **No nombra ningun fichero**,
    y por eso `vuelta150_3_relectura_expediente.py` la lista como la unica de las
    tres mesas SIN DOCUMENTO QUE MEDIR. **Eso no la deja sin cotejar:** se coteja
    contra lo que su prosa AFIRMA, que es una cifra con su fecha de corte.
  . `adjudicacion` y `nota` TRAEN TEXTO, y las otras dos mesas no lo tenian igual.
    **Ahi es donde vive lo que la mesa decidio**, y de ahi salen la mayoria de los
    puntos de esta vara.

EL ESCARMIENTO, APLICADO Y NO SOLO CITADO. En la 207 dos puntos se sellaron NO
DOCUMENTALES y tenian sede; en la 208 el mismo escarmiento movio la `V.17` a
DOCUMENTAL **antes** de sellar. AQUI, ANTES DE SELLAR UN PUNTO COMO NO DOCUMENTAL,
SE BUSCA SU LITERAL EN EL CORPUS Y EL RESULTADO SE ESCRIBE DENTRO DEL SELLO. Si la
busqueda lo encuentra, **la vara CAE EN ROJO** y el punto hay que sellarlo
DOCUMENTAL. **La busqueda va tambien POSITIVA**, con un literal de control por
documento que TIENE que aparecer, porque una busqueda negativa no se puede citar
sola (`EJECUTOR.md` 9).

LO QUE ESTE COMPUTO DECLARA CON HONESTIDAD Y NO DISIMULA: de los documentos del
corpus, **cuatro ya estaban abiertos por mi en esta misma vuelta y por causa ajena
a esta vara**: `docs/plan/OPERACIONES.jsonl` y `docs/plan/LECTURAS_DIRIGIDAS.md`
(los movio la TAREA 2), `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` (lo midio mi sello
de apertura) y `docs/loop/ACTA_AUDITOR.md` (lo manda la TAREA 1). **Los demas los
abro por primera vez en el cotejo.** El sello sigue siendo sello: lo que garantiza
es que la vara y su reparto se escriben ANTES de cotejar, y eso se cumple; decir
"antes de abrir ningun documento" sin esta nota seria falso. Es la letra que el
acta 208 adjudico en su `6.7` al ADMITIR el `D.3`.
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

VUELTA = 209
ID_OP = "OP-L-02"
LINEA_FICHA = 42
OPES = os.path.join(RAIZ, "docs", "plan", "OPERACIONES.jsonl")

# LOS DOCUMENTOS DEL CORPUS, con la clave corta con que el cotejo los cita. NO SE
# ELIGEN AQUI POR GUSTO: cada uno sale de un campo de la ficha, y el campo va
# escrito al lado.
DOCS = {
    "CORTE": ("docs/loop/SALIDA_V170_T3_DEUDAS_DE_CORTE.txt",
              "verificacion[3], 'Salida: docs/loop/SALIDA_V170_T3_DEUDAS_DE_CORTE.txt'"),
    "LDSR": ("docs/plan/LD_SALES_ROADMAP.md",
             "nota, 'viven en docs/plan/LD_SALES_ROADMAP.md con su razon una por una'"),
    "COB": ("docs/loop/SALIDA_V169_T5_COBERTURA_OP_L_02.txt",
            "nota, '(docs/loop/SALIDA_V169_T5_COBERTURA_OP_L_02.txt)'"),
    "LOTE": ("docs/loop/SALIDA_V169_T5_LOTE_SALES_ROADMAP.txt",
             "nota, 'Ver docs/loop/SALIDA_V169_T5_LOTE_SALES_ROADMAP.txt'"),
    "PUEN": ("docs/loop/SALIDA_V170_T4B_PUENTES.txt",
             "nota, 'Salida: docs/loop/SALIDA_V170_T4B_PUENTES.txt'"),
    "VER": ("docs/INTRA_DOMINIO_VEREDICTOS.jsonl",
            "verificacion[3], 'RECOMPUTANDO docs/INTRA_DOMINIO_VEREDICTOS.jsonl LINEA A LINEA'"),
    "INV": ("docs/plan/INVENTARIO.jsonl",
            "nota, 'las dos entradas de INVENTARIO.jsonl'"),
    "ACTOS": ("scripts/vuelta16_generar_actos.mjs",
              "nota, 'la nomina parseada de scripts/vuelta16_generar_actos.mjs'"),
    "OPS": ("docs/plan/OPERACIONES.jsonl",
            "nota, 'se barrieron las 71 fichas de docs/plan/OPERACIONES.jsonl'"),
    "LD": ("docs/plan/LECTURAS_DIRIGIDAS.md",
           "nota, 'la fila del universo de LECTURAS_DIRIGIDAS.md'"),
    "BDP": ("docs/plan/BANCO_DEL_PLAN.md",
            "nota, 'la operacion que abra este acto por P.5 y P.8' y 'lo que P.10 llama COSTURA'"),
}

# EL LITERAL DE CONTROL DE CADA DOCUMENTO: TIENE que aparecer. Si no aparece, la
# busqueda negativa de ese documento NO VALE y la vara cae (`EJECUTOR.md` 9).
# CORRECCION DECLARADA DENTRO DEL PROPIO SELLO (7 sep 2026, vuelta 209, TAREA
# 3.a), y el texto viejo NO se borra: el control de `CORTE` era `"marcador"`, y
# LA PRIMERA CORRIDA DE ESTA VARA CAYO EN ROJO POR EL, con `aparece 0 vez(ces)`.
# **EL FICHERO NO ESTABA MAL: MI ELECCION SI.** `SALIDA_V170_T3_DEUDAS_DE_CORTE.
# txt` habla del marcador por su sede y su cifra (`docs/INTRA_DOMINIO_VEREDICTOS.
# jsonl: 3388 filas`, linea 48) y **nunca escribe la palabra**. Un control
# positivo que no aparece no invalida el documento: invalida el control, y por eso
# la guarda existe. Se cambia por `OP-L-02`, que es la ficha de la que ese fichero
# habla y que aparece en su linea 9. **Esto se cambia ANTES de sellar y se declara
# aqui; lo que NO se ha tocado es ni un punto de la vara ni el reparto documental.**
CONTROL = {
    "CORTE": "OP-L-02", "LDSR": "LD-66", "COB": "cobertura",
    "LOTE": "sales_roadmap", "PUEN": "puente", "VER": "puesto",
    "INV": "cobertura", "ACTOS": "acto", "OPS": "OP-L-02",
    "LD": "LECTURA DIRIGIDA", "BDP": "P.10",
}

# LA VARA. Un punto por cada AFIRMACION COMPROBABLE de la ficha, cada uno con la
# CITA LITERAL del campo y del elemento del que sale. El cotejo comprueba las
# citas VERBATIM contra la ficha y CAE EN ROJO si una no aparece.
#
# (clave, campo, cita literal verbatim, que hay que comprobar)
PUNTOS = [
    ("V.1", "tipo",
     "MESA",
     "la ficha se declara MESA, y por tanto su criterio de HECHO es el de la "
     "fila 06 MESAS de docs/plan/08_VERIFICACION.md"),
    ("V.2", "orden",
     "2",
     "es la SEGUNDA de las tres mesas de la fase 09"),
    ("V.3", "fecha_corte",
     "2026-08-11",
     "toda cifra de la ficha se juzga contra ESTE corte y no contra hoy "
     "(banco 9.21)"),
    ("V.4", "depende_de",
     "OP-D-01",
     "las tres de las que depende existen en el fichero y se pueden nombrar"),
    ("V.5", "evidencia[0]",
     "MEDIDO el 11 ago 2026: 205 pares fuera de cola, 11 leidos, 194 pendientes",
     "la unica evidencia de la ficha es PROSA con su fecha de corte; se coteja "
     "contra lo que afirma, y sus tres cifras tienen que cuadrar entre si"),
    ("V.6", "verificacion[0]",
     "las tres nominas afectadas quedan con cobertura COMPLETA y su forma reescrita",
     "las TRES nominas tienen que poder NOMBRARSE desde la propia ficha; si no "
     "se pueden, la ficha no alcanza y eso es PARADA (AUDITOR.md 3)"),
    ("V.7", "verificacion[1]",
     "el marcador del cribado no se mueve: sigue en 2.117",
     "la clausula exige que la operacion NO MUEVA el marcador; el 2.117 es el "
     "valor en el fecha_corte, testigo y no condicion"),
    ("V.8", "verificacion[2]",
     "cada grupo del backlog lleva su motivo escrito, no solo su cuenta",
     "cada grupo del backlog documentado tiene que traer su motivo, no solo su "
     "numero"),
    ("V.9", "verificacion[3]",
     "el marcador del cribado vale 3388, repartido en A 551, B 72, C 5, D 2760",
     "la CORRECCION DECLARADA del 4 sep 2026 publica el marcador de ese dia con "
     "su reparto; se remide hoy contra el archivo"),
    ("V.10", "verificacion[3]",
     "Salida: docs/loop/SALIDA_V170_T3_DEUDAS_DE_CORTE.txt",
     "la ruta que la correccion declara como su prueba existe y no mide cero "
     "bytes (EJECUTOR.md 1, LA RUTA QUE PROMETE PRUEBA ES CIFRA)"),
    ("V.11", "adjudicacion",
     "SE LEEN SOLO LOS QUE CUELGAN DE UNA MESA O DE UNA NOMINA ABIERTA",
     "la decision de la mesa, escrita; es la que el criterio de HECHO exige que "
     "lleve su motivo y su cobertura al lado"),
    ("V.12", "adjudicacion",
     "SEGUNDA TANDA LEIDA: 16 lecturas, 2 A y 14 D",
     "el saldo de la segunda tanda, que tiene que cuadrar con el reparto por "
     "nomina de la nota"),
    ("V.13", "nota",
     "SE LEYERON 16: cuadrantes de mercado (8), ecuacion de valor (5) y el bloque humano de la supervision de la IA (3)",
     "las TRES nominas de la V.6, NOMBRADAS, y sus tres cuentas sumando 16"),
    ("V.14", "nota",
     "LOS CINCO SE LEYERON el 14 ago 2026 como LD-66 a LD-70, y viven en docs/plan/LD_SALES_ROADMAP.md",
     "las cinco cabeceras LD-66 a LD-70 estan en ese documento"),
    ("V.15", "nota",
     "las SEIS nominas de esta ficha tienen HOY cobertura COMPLETA, cero pares sin veredicto en ninguna sede",
     "la afirmacion de las SEIS, con su salida sellada al lado"),
    ("V.16", "nota",
     "BACKLOG DOCUMENTADO, 189 pares: 126 esperan destejido, 55 son resto sin mesa ni nomina, 5 de sales roadmap con clase ya decidida, y 3 ya leidas en la primera tanda",
     "el backlog con sus cuatro grupos, cada uno con su motivo escrito, y las "
     "cuatro cuentas sumando 189: es la sede que la V.8 exige"),
    ("V.17", "nota",
     "6 miembros escritos, 6 vivos tras resolver, 15 pares posibles, 15 con clase y CERO sin clase",
     "la medicion del acto del sales roadmap, con el resolutor delante"),
    ("V.18", "nota",
     "se barrieron las 71 fichas de docs/plan/OPERACIONES.jsonl buscando estos nodos en los campos nodos, preservar, eliminar y superviviente, y salieron CERO",
     "la busqueda negativa que la nota declara HECHA CON SU COMANDO; se "
     "re-verifica contra el grafo porque una busqueda negativa no se puede citar "
     "(EJECUTOR.md 9)"),
]

# LOS QUE SE SELLAN NO DOCUMENTALES, CON SU MOTIVO ESCRITO ANTES DE MIRAR, Y CON
# EL LITERAL QUE SE VA A BUSCAR EN EL CORPUS. Si ese literal APARECE, la vara CAE.
NO_DOCUMENTALES = {
    "V.1": ("es estructura de la propia ficha: el campo `tipo`. No hay documento "
            "que pueda decir que esta ficha es una MESA mas que ella misma.",
            None),
    "V.2": ("es estructura de la propia ficha: el campo `orden`.", None),
    "V.3": ("es estructura de la propia ficha: el campo `fecha_corte`.", None),
    "V.5": ("es la unica `evidencia` de la ficha y es PROSA que NO NOMBRA NINGUN "
            "FICHERO. Se coteja contra lo que afirma y contra la propia nota, no "
            "contra un documento que la ficha no nombra.",
            "205 pares fuera de cola, 11 leidos, 194 pendientes"),
    "V.7": ("la clausula habla de lo que la OPERACION no debe hacer, no de lo que "
            "un documento dice. El marcador se mide del archivo, y eso lo hace la "
            "V.9; aqui lo que se juzga es la clausula.",
            "el marcador del cribado no se mueve: sigue en 2.117"),
}


def dos_convenciones(ruta):
    crudo = io.open(ruta, "rb").read()
    lf = crudo.replace(b"\r\n", b"\n")
    return (len(crudo), len(lf), hashlib.sha256(crudo).hexdigest()[:16],
            hashlib.sha256(lf).hexdigest()[:16], lf.decode("utf-8", "replace"))


def la_ficha():
    texto = io.open(OPES, encoding="utf-8").read().replace(chr(13) + NL, NL)
    ls = texto.split(NL)
    return json.loads(ls[LINEA_FICHA - 1]), ls[LINEA_FICHA - 1]


def valor_del_campo(d, campo):
    """EL TEXTO DEL CAMPO QUE UN PUNTO CITA. Admite `campo[indice]`."""
    if "[" in campo:
        base, idx = campo[:-1].split("[")
        v = d.get(base)
        if not isinstance(v, list) or int(idx) >= len(v):
            return None
        return str(v[int(idx)])
    v = d.get(campo)
    if isinstance(v, list):
        return " ".join(str(x) for x in v)
    return str(v)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", default="T3A_VARA")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    fallos = 0

    w("=" * 78)
    w("VUELTA %d, TAREA 3.a: LA VARA DE %s, SELLADA ANTES DE COTEJAR NADA"
      % (VUELTA, ID_OP))
    w("=" * 78)
    w("")

    w("A) LA FICHA, MEDIDA AL ENTRAR")
    d0, lf0, sd0, sl0, _ = dos_convenciones(OPES)
    w("   docs/plan/OPERACIONES.jsonl: %d bytes en disco y %d bytes normalizado "
      "a LF" % (d0, lf0))
    w("   sha256 disco %s y sha256 LF %s" % (sd0, sl0))
    d, linea = la_ficha()
    w("   linea %d, id_op leido: %s" % (LINEA_FICHA, d["id_op"]))
    if d["id_op"] != ID_OP:
        w("   ROJO: la linea %d no es %s." % (LINEA_FICHA, ID_OP))
        fallos += 1
    w("   CIFRA campos de la ficha: %d" % len(d))
    w("   CIFRA bytes de la linea de la ficha: %d en disco y %d normalizado a LF"
      % (len(linea.encode("utf-8")), len(linea.encode("utf-8"))))
    w("   tipo %r | orden %r | fecha_corte %r | estado %r"
      % (d.get("tipo"), d.get("orden"), d.get("fecha_corte"), d.get("estado")))
    w("   CIFRA elementos de depende_de: %d (%s)"
      % (len(d.get("depende_de") or []), ", ".join(d.get("depende_de") or [])))
    w("   CIFRA elementos de bloquea_a: %d (%s)"
      % (len(d.get("bloquea_a") or []),
         ", ".join(d.get("bloquea_a") or []) or "vacio"))
    w("   CIFRA elementos de evidencia: %d" % len(d.get("evidencia") or []))
    w("   CIFRA elementos de verificacion: %d" % len(d.get("verificacion") or []))
    n_corr = len([1 for e in (d.get("verificacion") or [])
                  if "CORRECCION DECLARADA" in str(e)])
    w("   CIFRA elementos de verificacion que son CORRECCION DECLARADA: %d" % n_corr)
    w("   CIFRA caracteres de adjudicacion: %d | de nota: %d"
      % (len(str(d.get("adjudicacion") or "")), len(str(d.get("nota") or ""))))
    w("   pregunta_pendiente: %r" % d.get("pregunta_pendiente"))
    w("")
    w("   EL COTEJO CONTRA EL CONTRASTE DEL ENCARGO (contraste, NO fuente):")
    cot = [("campos", len(d), 18), ("tipo", d.get("tipo"), "MESA"),
           ("orden", d.get("orden"), 2),
           ("fecha_corte", d.get("fecha_corte"), "2026-08-11"),
           ("depende_de", len(d.get("depende_de") or []), 3),
           ("bloquea_a", len(d.get("bloquea_a") or []), 0),
           ("evidencia", len(d.get("evidencia") or []), 1),
           ("verificacion", len(d.get("verificacion") or []), 4),
           ("verificacion CORRECCION", n_corr, 1),
           ("estado", d.get("estado"), "LISTA")]
    disc = 0
    for nombre, mio, suyo in cot:
        ok = (mio == suyo)
        if not ok:
            disc += 1
        w("      %-26s mio %-14s contraste %-14s %s"
          % (nombre, mio, suyo, "CALZA" if ok else "DISCREPA Y SE DECLARA"))
    w("   CIFRA discrepancias con el contraste del encargo en el 3.a: %d" % disc)
    w("")

    w("B) LAS %d CITAS, COMPROBADAS **VERBATIM** CONTRA SU CAMPO" % len(PUNTOS))
    w("   (si una no aparece EXACTAMENTE en su campo, la vara CAE EN ROJO)")
    for clave, campo, cita, _que in PUNTOS:
        v = valor_del_campo(d, campo)
        if v is None:
            w("   %-5s %-18s ROJO: el campo no existe o el indice se sale" % (clave, campo))
            fallos += 1
            continue
        hay = cita in v
        w("   %-5s %-18s cita de %d caracteres aparece VERBATIM: %s"
          % (clave, campo, len(cita), "SI" if hay else "NO, Y ESO ES ROJO"))
        if not hay:
            fallos += 1
            w("         buscada: %r" % cita[:110])
    w("   CIFRA citas que NO aparecen verbatim en su campo: %d" % fallos)
    w("")

    w("C) EL CORPUS, MEDIDO Y CON SU CONTROL POSITIVO")
    textos = {}
    for k, (rel, de_donde) in sorted(DOCS.items()):
        p = os.path.join(RAIZ, rel.replace("/", os.sep))
        if not os.path.isfile(p):
            w("   %-6s %-52s NO EXISTE" % (k, rel))
            fallos += 1
            continue
        dd, ll, _sd, _sl, t = dos_convenciones(p)
        textos[k] = t
        w("   %-6s %-52s %d bytes en disco y %d bytes normalizado a LF"
          % (k, rel, dd, ll))
        w("          sale de: %s" % de_donde)
        if dd == 0:
            w("          ROJO: mide cero bytes.")
            fallos += 1
    w("")
    w("   EL CONTROL POSITIVO, PRIMERO: UNA BUSQUEDA NEGATIVA NO SE PUEDE CITAR")
    w("   SOLA (`EJECUTOR.md` 9). Cada literal de control TIENE que aparecer.")
    ctrl_fallan = 0
    for k in sorted(CONTROL):
        if k not in textos:
            continue
        n = textos[k].count(CONTROL[k])
        w("      %-6s literal de control %-20r aparece %d vez(ces)"
          % (k, CONTROL[k], n))
        if n == 0:
            ctrl_fallan += 1
    w("   CIFRA controles positivos que FALLAN: %d" % ctrl_fallan)
    if ctrl_fallan:
        w("   ROJO: si el control no aparece, la busqueda negativa de ese")
        w("   documento no vale y no se puede sellar nada con ella.")
        fallos += ctrl_fallan
    w("")

    w("D) EL ESCARMIENTO: ANTES DE SELLAR UN PUNTO COMO NO DOCUMENTAL, SE BUSCA")
    w("   SU LITERAL EN EL CORPUS. SI APARECE, LA VARA CAE Y EL PUNTO SE SELLA")
    w("   DOCUMENTAL.")
    aparecen = 0
    for clave in sorted(NO_DOCUMENTALES):
        motivo, literal = NO_DOCUMENTALES[clave]
        w("   --- %s ---" % clave)
        w("       motivo, escrito ANTES de mirar: %s" % motivo)
        if literal is None:
            w("       NO SE BUSCA LITERAL: el punto es un campo de la propia ficha")
            w("       (`tipo`, `orden`, `fecha_corte`), y su unica sede posible es")
            w("       la ficha. Buscarlo en el corpus no seria una prueba de nada.")
            continue
        w("       literal que se busca: %r" % literal[:100])
        donde = []
        for k in sorted(textos):
            # LA SEDE DE LA PROPIA FICHA QUEDA FUERA A PROPOSITO: `OPERACIONES.
            # jsonl` CONTIENE LA FICHA, asi que encontrar ahi el literal de su
            # propio campo no probaria que tenga sede documental, probaria que la
            # ficha existe.
            if k == "OPS":
                continue
            n = textos[k].count(literal)
            if n:
                donde.append((k, n))
        w("       CIFRA documentos del corpus donde APARECE: %d (%s)"
          % (len(donde), ", ".join("%s x%d" % x for x in donde) or "ninguno"))
        w("       (`OPS` queda fuera de esta busqueda: contiene la propia ficha)")
        if donde:
            aparecen += 1
            w("       ROJO: no se puede sellar NO DOCUMENTAL un punto cuya sede SI")
            w("       existe. Hay que sellarlo DOCUMENTAL.")
    w("   CIFRA puntos candidatos a NO DOCUMENTAL cuyo literal SI aparece en el")
    w("   corpus: %d" % aparecen)
    fallos += aparecen
    w("")

    w("E) EL REPARTO DOCUMENTAL, SELLADO **AHORA**, ANTES DE MIRAR NINGUNA CIFRA")
    docs_p = [p[0] for p in PUNTOS if p[0] not in NO_DOCUMENTALES]
    w("   CIFRA puntos de la vara: %d" % len(PUNTOS))
    w("   CIFRA puntos DOCUMENTALES: %d" % len(docs_p))
    w("      %s" % ", ".join(docs_p))
    w("   CIFRA puntos NO DOCUMENTALES: %d" % len(NO_DOCUMENTALES))
    for clave in sorted(NO_DOCUMENTALES):
        w("      %-5s %s" % (clave, NO_DOCUMENTALES[clave][0][:88]))
    w("   la suma cuadra con el total: %s"
      % ("SI" if len(docs_p) + len(NO_DOCUMENTALES) == len(PUNTOS) else "NO"))
    if len(docs_p) + len(NO_DOCUMENTALES) != len(PUNTOS):
        fallos += 1
    w("")

    w("F) LOS %d PUNTOS, ENTEROS Y CON SU CITA" % len(PUNTOS))
    for clave, campo, cita, que in PUNTOS:
        w("   --- %s (%s) --- %s"
          % (clave, campo,
             "NO DOCUMENTAL" if clave in NO_DOCUMENTALES else "DOCUMENTAL"))
        w("       cita literal: %s" % cita)
        w("       que se comprueba: %s" % que)
    w("")

    w("=" * 78)
    w("CIFRA comprobaciones que fallan en el sello de la vara: %d" % fallos)
    w("VEREDICTO DEL SELLO: %s" % ("VERDE" if fallos == 0 else "ROJO"))
    w("=" * 78)
    salida = NL.join(L) + NL
    print(salida)
    io.open(os.path.join(LOOP, "SALIDA_V%d_%s.txt" % (VUELTA, a.salida)),
            "w", encoding="utf-8", newline=NL).write(salida)
    return 0 if fallos == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
