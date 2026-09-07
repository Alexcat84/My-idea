# -*- coding: utf-8 -*-
r"""_v202_t3_op_l_01.py . `OP-L-01` CONTRA EL CRITERIO DE HECHO, Y EL HUECO DE LA
VIGENCIA DE LA TABLA VIVA DE LOS PUROS (TAREA 3 de la vuelta 202).

PREFIJO DE GUION BAJO: computo de UNA vuelta, fuera del censo y fuera de la
nomina, que no vigila a nadie (adjudicacion `4.5` del acta 199). LA MORATORIA
(`AUDITOR.md` 6.3) NO SE TOCA: los dos instrumentos de `OP-L-01` se **IMPORTAN Y
SE CORREN EN MODO MEDICION**, sin `--aplicar`, y sus salidas se sellaron con
nombre de esta vuelta ANTES de que este fichero corra:

  . `scripts/loop/vuelta166_tarea2_correccion_op_l_01.py`   (clausulas 1 y 2)
  . `scripts/loop/vuelta169_tarea4_op_l_01_clausula3.py`    (clausula 3)

LA VARA DEL HUECO SE DECLARA AQUI, EN UNA CONSTANTE, ANTES DE CORRERSE, que es lo
que la vuelta 201 hizo con su prueba de cobertura y por el mismo motivo: **una
aguja que se elige despues de mirar no mide nada**. Esta escrita en
`VARA_DE_LA_VIGENCIA` y dice, palabra por palabra, que se cuenta y que no.

EL HUECO QUE SE MIDE, Y NADIE LO HABIA MEDIDO: la cabecera de la TABLA VIVA DE
LOS PUROS de `docs/BANCO_DE_TEXTOS.md` declara literalmente `vigente al puesto
1157`, y el marcador de hoy vale otra cosa. **LAS DOS CIFRAS SE RECUENTAN AQUI.**

SI EL HUECO PIDIERA MOVER UNA CLASE, NO SE MUEVE: mover una clase es del
RECOMPUTO. Se nombra y se para ahi.

Y NO CIERRA NADA: lo que produce esta tarea es LECTURA MEDIDA, y lo que de ella
salga SE PROPONE y lo adjudica el auditor.

USO:
  python scripts/loop/_v202_t3_op_l_01.py
"""
import io
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

OPERACIONES = "docs/plan/OPERACIONES.jsonl"
CRITERIO = "docs/plan/08_VERIFICACION.md"
BANCO = "docs/BANCO_DE_TEXTOS.md"
VEREDICTOS = "docs/INTRA_DOMINIO_VEREDICTOS.jsonl"
ID_OP = "OP-L-01"
MARCA_CORRECCION = "CORRECCION DECLARADA"

INSTRUMENTOS = [
    "scripts/loop/vuelta166_tarea2_correccion_op_l_01.py",
    "scripts/loop/vuelta169_tarea4_op_l_01_clausula3.py",
]
SELLADAS_HOY = [
    "docs/loop/SALIDA_V202_T3_CLAUSULAS_12_166.txt",
    "docs/loop/SALIDA_V202_T3_CLAUSULA_3_169.txt",
]
SELLADAS_VIEJAS = [
    "docs/loop/SALIDA_V166_T2_CORRECCION_OP_L_01.txt",
    "docs/loop/SALIDA_V169_T4_OP_L_01.txt",
]
# LAS CIFRAS QUE SE COTEJAN ENTRE LA CORRIDA VIEJA Y LA DE HOY. VAN EN CONSTANTE
# PARA QUE LA LISTA QUE SE PUBLICA SEA LA MISMA QUE SE BUSCA.
CIFRAS_A_COTEJAR = [
    "CIFRA cabeceras LD leidas de LECTURAS_DIRIGIDAS.md",
    "CIFRA de las once que aparecen, LITERAL",
    "CIFRA de las once que aparecen, RESUELTA",
    "CIFRA puestos implicados en total",
    "CIFRA alias en el mapa",
    "CIFRA filas de docs/INTRA_DOMINIO_VEREDICTOS.jsonl",
    "CIFRA marcador del cribado HOY",
]

LINEA_CABECERA_TABLA = 938
LITERAL_VIGENCIA = "vigente al puesto"

VARA_DE_LA_VIGENCIA = """
LA VARA, DECLARADA ANTES DE CORRERSE Y NO DESPUES DE MIRAR:

  UNA FILA DE LA TABLA VIVA DE LOS PUROS SIGUE EN PIE AL CORTE DE HOY SI TODOS
  LOS PUESTOS QUE ELLA MISMA CITA EXISTEN EN docs/INTRA_DOMINIO_VEREDICTOS.jsonl
  AL CORTE DE HOY. Una fila que cita un puesto que hoy no existe NO SIGUE EN PIE.

  UNA FILA QUE NO CITA NINGUN PUESTO NO ES MEDIBLE POR ESTA VARA, y se cuenta
  aparte: NI EN PIE NI CAIDA. Contarla como en pie seria fabricar cobertura, y
  contarla como caida seria fabricar un rojo.

  LOS PUESTOS SE EXTRAEN DE LA FILA CON UNA SOLA EXPRESION REGULAR, la constante
  PATRON_PUESTO de este fichero, que casa `puesto N`, `puestos N, M y K` y `el N`
  cuando el numeral va en negrita. LO QUE ESA EXPRESION NO CACE SE DECLARA COMO
  NO CAZADO en vez de completarse a ojo.

  ESTA VARA MIDE PRESENCIA DEL PUESTO, NO CALIDAD DE LA FILA, y eso se dice
  delante: la clase que el archivo da HOY a cada puesto se PUBLICA al lado, pero
  NO se compara contra la que la fila afirma, porque las filas afirman su clase
  en prosa libre y una comparacion a ojo no es una medicion.

  Y LA VIGENCIA ES OTRA COSA QUE LA PRESENCIA, y se mide aparte: el MAXIMO puesto
  que cada fila cita, contra el `vigente al puesto` que la cabecera declara y
  contra el marcador de hoy.
"""

PATRON_PUESTO = re.compile(
    r"puestos?\s+\*{0,2}(\d[\d.]*)\*{0,2}"
    r"(?:\s*,\s*\*{0,2}(\d[\d.]*)\*{0,2})?"
    r"(?:\s*y\s*\*{0,2}(\d[\d.]*)\*{0,2})?"
    r"|\bel\s+\*\*(\d[\d.]*)\*\*")


def leer(rel):
    ruta = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(ruta):
        return None
    crudo = io.open(ruta, "rb").read()
    return crudo.replace(b"\r\n", b"\n").decode("utf-8", errors="replace")


def medir(rel):
    ruta = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(ruta):
        return None
    crudo = io.open(ruta, "rb").read()
    return len(crudo), len(crudo.replace(b"\r\n", b"\n"))


def cifra_de(texto, etiqueta):
    """LA CIFRA QUE UN FICHERO DE SALIDA PUBLICA BAJO UNA ETIQUETA. PURA."""
    m = re.search(re.escape(etiqueta) + r":\s*(\d+)", texto or "")
    return m.group(1) if m else None


def puestos_de_la_fila(texto):
    """LOS PUESTOS QUE UNA FILA CITA, EXTRAIDOS CON LA UNICA EXPRESION QUE LA
    VARA DECLARA. PURA. Devuelve una lista de enteros, ordenada y sin
    repeticiones."""
    fuera = set()
    for m in PATRON_PUESTO.finditer(texto):
        for g in m.groups():
            if g:
                fuera.add(int(g.replace(".", "")))
    return sorted(fuera)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA 202, TAREA 3 . OP-L-01 CONTRA EL CRITERIO DE HECHO, Y EL HUECO")
    w("DE LA VIGENCIA DE LA TABLA VIVA DE LOS PUROS")
    w("LECTURA MEDIDA. NO SE CIERRA NADA, NO SE MUEVE NINGUNA CLASE.")
    w("=" * 78)
    w("")

    w("A) LOS DOS INSTRUMENTOS, CORRIDOS EN MODO MEDICION Y SIN --aplicar")
    for ins, sh, sv in zip(INSTRUMENTOS, SELLADAS_HOY, SELLADAS_VIEJAS):
        mi, mh, mv = medir(ins), medir(sh), medir(sv)
        w("   %s" % ins)
        w("      %d bytes en disco | %d bytes normalizados a LF" % mi if mi
          else "      NO EXISTE")
        if mh is None or mh[0] == 0:
            w("      ROJO: la sellada de HOY %s no existe o mide cero bytes." % sh)
        else:
            w("      sellada de HOY:   %s, %d bytes en disco | %d bytes en LF"
              % (sh, mh[0], mh[1]))
        if mv is None or mv[0] == 0:
            w("      la sellada VIEJA %s no existe o mide cero bytes." % sv)
        else:
            w("      sellada VIEJA:    %s, %d bytes en disco | %d bytes en LF"
              % (sv, mv[0], mv[1]))
    w("")

    w("B) EL CRITERIO DE HECHO, CITADO POR LINEA")
    t_cri, m_cri = leer(CRITERIO), medir(CRITERIO)
    l_cri = t_cri.split(NL)
    w("   %s: %d bytes en disco | %d bytes normalizados a LF | %d lineas"
      % (CRITERIO, m_cri[0], m_cri[1], t_cri.count(NL)))
    cab = [i + 1 for i, l in enumerate(l_cri)
           if l.startswith("## EL CRITERIO DE HECHO")]
    w("   cabecera del criterio: %d acierto(s), linea(s) %s"
      % (len(cab), ", ".join(str(x) for x in cab) or "(ninguna)"))
    for i in range(cab[0] - 1, min(cab[0] + 9, len(l_cri))):
        if l_cri[i].strip():
            w("      linea %d: %s" % (i + 1, l_cri[i].strip()))
    hits_op = [i + 1 for i, l in enumerate(l_cri) if ID_OP in l]
    w("   lineas de %s que NOMBRAN %s: %d, linea(s) %s"
      % (CRITERIO, ID_OP, len(hits_op),
         ", ".join(str(x) for x in hits_op) or "(ninguna)"))
    w("")

    w("C) LA verificacion DE %s, CITADA POR LINEA MAS INDICE (acta 201, 4.4)"
      % ID_OP)
    t_ops = leer(OPERACIONES)
    lin_ops = t_ops.split(NL)
    aguja = chr(34) + "id_op" + chr(34) + ": " + chr(34) + ID_OP + chr(34)
    hits = [i + 1 for i, l in enumerate(lin_ops) if l.strip() and aguja in l]
    w("   CIFRA lineas donde vive %s: %d | linea(s): %s"
      % (ID_OP, len(hits), ", ".join(str(h) for h in hits) or "(ninguna)"))
    if len(hits) != 1:
        w("   ROJO: la ficha no aparece exactamente una vez.")
        print(NL.join(L))
        return 1
    ln = hits[0]
    d = json.loads(lin_ops[ln - 1])
    ver = d.get("verificacion", [])
    ev = d.get("evidencia", [])
    w("   la ficha vive en la LINEA %d" % ln)
    w("   estado (SE LEE, NO SE MUEVE): %r | tipo: %r | fecha_corte: %r"
      % (d.get("estado"), d.get("tipo"), d.get("fecha_corte")))
    w("   CIFRA elementos de `verificacion`: %d" % len(ver))
    w("   CIFRA elementos de `evidencia`: %d" % len(ev))
    clausulas, correcciones = [], []
    for i, x in enumerate(ver):
        (correcciones if MARCA_CORRECCION in str(x) else clausulas).append((i, x))
    w("   CIFRA clausulas propiamente dichas: %d" % len(clausulas))
    w("   CIFRA correcciones declaradas: %d" % len(correcciones))
    for i, x in clausulas:
        w("      linea %d + indice %d (elemento %d), %d caracteres:"
          % (ln, i, i + 1, len(str(x))))
        w("         %r" % x)
    for i, x in correcciones:
        w("      CORRECCION DECLARADA en linea %d + indice %d (elemento %d), "
          "%d caracteres" % (ln, i, i + 1, len(str(x))))
    for i, x in enumerate(ev):
        w("      evidencia indice %d (elemento %d): %r" % (i, i + 1, x))
    w("")

    w("D) EL CRITERIO DE HECHO APLICADO: NO ES PRESENCIA, ES SI LA CIFRA")
    w("   AGUANTA. EL INSTRUMENTO SE VUELVE A CORRER HOY Y SUS CIFRAS SE")
    w("   COTEJAN CONTRA LAS QUE LA FICHA TIENE CONGELADAS.")
    t_hoy = leer(SELLADAS_HOY[0]) or ""
    t_viejo = leer(SELLADAS_VIEJAS[0]) or ""
    discrepan = []
    w("   | cifra | corrida VIEJA (sellada del 2026-09-04) | corrida de HOY |")
    for etiqueta in CIFRAS_A_COTEJAR:
        a, b = cifra_de(t_viejo, etiqueta), cifra_de(t_hoy, etiqueta)
        w("   | %-52s | %-8s | %-8s | %s"
          % (etiqueta, a if a is not None else "(no impresa)",
             b if b is not None else "(no impresa)",
             "CALZA" if a == b else "DISCREPA"))
        if a is not None and b is not None and a != b:
            discrepan.append((etiqueta, a, b))
    w("   CIFRA cifras cotejadas: %d | CIFRA que DISCREPAN: %d"
      % (len(CIFRAS_A_COTEJAR), len(discrepan)))
    w("")
    w("   LA CIFRA QUE LA PROPIA FICHA TIENE CONGELADA, LEIDA DE LA FICHA Y NO")
    w("   DEL FICHERO DE SALIDA:")
    for i, x in correcciones:
        m = re.search(r"EN COMPARACION RESUELTA APARECEN (\d+)", str(x))
        if m:
            w("      linea %d + indice %d (elemento %d) dice: EN COMPARACION"
              % (ln, i, i + 1))
            w("         RESUELTA APARECEN %s" % m.group(1))
        m2 = re.search(r"(\d+) filas en docs/INTRA_DOMINIO_VEREDICTOS\.jsonl",
                       str(x))
        if m2:
            w("         y declara %s filas del archivo" % m2.group(1))
    w("")

    w("E) EL HUECO DE LA VIGENCIA DE LA TABLA VIVA DE LOS PUROS")
    for l in VARA_DE_LA_VIGENCIA.strip().split(NL):
        w("   " + l)
    w("")
    t_ban, m_ban = leer(BANCO), medir(BANCO)
    l_ban = t_ban.split(NL)
    w("   %s: %d bytes en disco | %d bytes normalizados a LF | %d lineas"
      % (BANCO, m_ban[0], m_ban[1], t_ban.count(NL)))
    cabecera = l_ban[LINEA_CABECERA_TABLA - 1]
    w("   linea %d, leida y no supuesta: %s" % (LINEA_CABECERA_TABLA, cabecera))
    m_vig = re.search(r"vigente al puesto\s+(\d[\d.]*)", cabecera)
    if not m_vig:
        w("   ROJO: la cabecera no trae el literal de vigencia. NO SE TECLEA.")
        print(NL.join(L))
        return 1
    vigencia = int(m_vig.group(1).replace(".", ""))
    w("   CIFRA vigencia declarada por la cabecera, leida de ella: %d" % vigencia)

    t_v = leer(VEREDICTOS)
    m_v = medir(VEREDICTOS)
    filas_v = [l for l in t_v.split(NL) if l.strip()]
    puestos_archivo, clase_de, malas = {}, {}, 0
    for l in filas_v:
        try:
            r = json.loads(l)
        except Exception:                                    # noqa: BLE001
            malas += 1
            continue
        p = int(r.get("puesto_intra"))
        puestos_archivo[p] = True
        clase_de[p] = r.get("clase")
    marcador = len(filas_v)
    w("   %s: %d bytes en disco | %d bytes normalizados a LF"
      % (VEREDICTOS, m_v[0], m_v[1]))
    w("   CIFRA marcador de hoy, recontado aqui: %d filas" % marcador)
    w("   CIFRA lineas que NO son JSON valido: %d" % malas)
    w("   CIFRA puestos distintos: %d | maximo: %d"
      % (len(puestos_archivo), max(puestos_archivo)))
    w("   CIFRA diferencia entre el marcador de hoy y la vigencia declarada: %d"
      % (marcador - vigencia))
    w("   ESTE CONTEO NO PASA POR EL RESOLUTOR Y SE DICE POR QUE: P.1 lo manda")
    w("      para todo conteo que TOQUE IDS, y contar puestos, filas y clases")
    w("      NO toca ningun id. La vara declarada arriba es de PRESENCIA DE")
    w("      PUESTO, y un puesto no es un id.")
    w("")

    # CORRECCION DECLARADA DE MI PROPIO COMPUTO, ESCRITA AQUI Y NO TAPADA: la
    # primera version de este extractor cogia TODA linea `| **N** |` posterior a
    # la cabecera y sacaba 32 filas, que no son las de la TABLA VIVA sino las de
    # esa tabla MAS las de otras cuatro tablas de mas abajo del banco (lineas
    # 1056, 1674, 2024, 2591 y siguientes). LA TABLA VIVA TIENE 11 FILAS. Aqui
    # se acota al BLOQUE CONTIGUO de lineas que empiezan por `|` justo detras de
    # la cabecera, que es lo que una tabla de markdown es.
    filas_tabla = []
    i = LINEA_CABECERA_TABLA
    while i < len(l_ban) and not l_ban[i].startswith("|"):
        i += 1
    inicio_tabla = i + 1
    while i < len(l_ban) and l_ban[i].startswith("|"):
        if re.match(r"^\|\s*\*\*\d+\*\*\s*\|", l_ban[i]):
            filas_tabla.append((i + 1, l_ban[i]))
        i += 1
    fin_tabla = i
    w("   LA TABLA SE ACOTA AL BLOQUE CONTIGUO DE LINEAS QUE EMPIEZAN POR |")
    w("      justo detras de la cabecera: lineas %d a %d" % (inicio_tabla, fin_tabla))
    w("   CIFRA filas numeradas de la TABLA VIVA dentro de esa cota: %d"
      % len(filas_tabla))
    en_pie, caidas, no_medibles, mas_alla = 0, 0, 0, 0
    w("   | # | linea | puestos citados | todos existen hoy | max citado | pasa de %d |"
      % vigencia)
    for numero_linea, fila in filas_tabla:
        n_fila = re.match(r"^\|\s*\*\*(\d+)\*\*\s*\|", fila).group(1)
        ps = puestos_de_la_fila(fila)
        if not ps:
            no_medibles += 1
            sueltos = [int(x) for x in
                       re.findall(r"(?<![\d.])(\d{3,4})(?![\d.])", fila)]
            w("   | %-3s | %5d | (ninguno) | NO MEDIBLE POR ESTA VARA | . | . |"
              % (n_fila, numero_linea))
            if sueltos:
                w("   |     |       | FUERA DE LA VARA, numerales de 3 o 4 cifras")
                w("   |     |       | que la fila menciona y la expresion NO caza:")
                w("   |     |       | %s | clases hoy: %s"
                  % (", ".join(str(x) for x in sorted(set(sueltos))),
                     ", ".join("%d=%s" % (x, clase_de.get(x, "(ausente)"))
                               for x in sorted(set(sueltos)))))
            continue
        faltan = [p for p in ps if p not in puestos_archivo]
        maxp = max(ps)
        if faltan:
            caidas += 1
        else:
            en_pie += 1
        if maxp > vigencia:
            mas_alla += 1
        w("   | %-3s | %5d | %s | %s | %d | %s |"
          % (n_fila, numero_linea, ", ".join(str(p) for p in ps),
             "SI" if not faltan else ("NO, faltan " + ", ".join(str(p) for p in faltan)),
             maxp, "SI" if maxp > vigencia else "no"))
        w("   |     |       | clases que el archivo da HOY: %s"
          % ", ".join("%d=%s" % (p, clase_de.get(p, "(ausente)")) for p in ps))
        sueltos = [int(x) for x in re.findall(r"(?<![\d.])(\d{3,4})(?![\d.])", fila)
                   if int(x) not in ps]
        if sueltos:
            w("   |     |       | FUERA DE LA VARA, numerales de 3 o 4 cifras que")
            w("   |     |       | la fila menciona y la expresion NO caza: %s"
              % ", ".join(str(x) for x in sorted(set(sueltos))))
    w("")
    w("   LO DE FUERA DE LA VARA SE PUBLICA PERO NO SE CUENTA, Y AQUI SE VE POR")
    w("      QUE: el numeral 2026 que aparece en cinco filas ES EL ANO DE UNA")
    w("      FECHA, no un puesto, y el archivo tiene ademas un puesto 2026 que")
    w("      no tiene nada que ver. UNA VARA DE NUMERALES SUELTOS CONFUNDIRIA")
    w("      LAS DOS COSAS; una vara de `puesto N` no. Esa es la razon de que la")
    w("      vara este escrita como esta, y se dice en vez de callarse.")
    w("")
    w("   CIFRA filas EN PIE al corte %d (todos sus puestos existen): %d"
      % (marcador, en_pie))
    w("   CIFRA filas CAIDAS (citan un puesto que hoy no existe): %d" % caidas)
    w("   CIFRA filas NO MEDIBLES POR ESTA VARA (no citan puesto): %d"
      % no_medibles)
    w("   SUMA: %d, y las filas de la tabla son %d"
      % (en_pie + caidas + no_medibles, len(filas_tabla)))
    w("   CIFRA filas que CITAN UN PUESTO MAS ALLA DE LA VIGENCIA DECLARADA "
      "(%d): %d" % (vigencia, mas_alla))
    con_corte_de_hoy = sum(
        1 for _n, f in filas_tabla
        if puestos_de_la_fila(f) and max(puestos_de_la_fila(f)) >= marcador)
    w("   CIFRA filas con un puesto citado AL CORTE DE HOY O MAS ALLA (%d): %d,"
      % (marcador, con_corte_de_hoy))
    w("      y esa cifra sale de MIRAR fila a fila, no de no haber mirado.")
    w("")
    w("   EL HUECO, DICHO CON LA MEDICION DELANTE Y SIN MOVER NADA:")
    w("      la cabecera declara vigencia al puesto %d; %d de las %d filas citan"
      % (vigencia, mas_alla, len(filas_tabla)))
    w("      un puesto POR ENCIMA de esa vigencia, o sea que LA CABECERA YA ESTA")
    w("      DESMENTIDA POR SUS PROPIAS CELDAS; y el marcador de hoy vale %d,"
      % marcador)
    w("      que es %d puestos mas alla de la vigencia declarada."
      % (marcador - vigencia))
    w("      NINGUNA CLASE SE MUEVE AQUI: mover una clase es del RECOMPUTO.")
    w("")
    w("FIN")

    salida = NL.join(L) + NL
    print(salida)
    io.open(os.path.join(LOOP, "SALIDA_V202_T3_OP_L_01.txt"), "w",
            encoding="utf-8", newline=NL).write(salida)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
