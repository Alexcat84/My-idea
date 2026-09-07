# -*- coding: utf-8 -*-
r"""_v203_reparto_de_actas_viejas.py . EL COMPUTO DEL REPARTO DE UN ACTA DE LA
CONVENCION ANTERIOR A LA 184, POR LA VARA QUE EL ACTA 202 ADJUDICO EN SU `4.1`.

PREFIJO DE GUION BAJO, Y EL ENCARGO DE ESTA VUELTA LO AUTORIZA POR SU NOMBRE:
fuera del censo y fuera de la nomina, un computo de una vuelta que muere con
ella, que es lo que el `4.5` del acta 199 dice que NO roza la moratoria.

SE ESCRIBE UNA SOLA VEZ Y LO USAN LAS DOS TAREAS: la TAREA 1 (la correccion
declarada de `R.63` y `R.64`, actas 173 y 174) y la TAREA 4 (`R.65` y `R.66`,
actas 175 y 176). El encargo lo manda con estas palabras: *reutiliza el computo
de la TAREA 1, no escribas un segundo*.

LA VARA, CITADA Y NO PARAFRASEADA (acta 202, `4.1`, por extension del `4.7` del
acta 201): **el numeral se toma de la seccion cuyo PROPIO TITULO lo nombra,
NUNCA del numero de seccion, y dentro de ella las claves se cuentan por su
propia numeracion `N.M`, lleve o no comillas inversas.**

NINGUN LECTOR NUEVO PERMANENTE. Los heredados se IMPORTAN:

  . `R84.claves_entrecomilladas()`         . las claves `N.M`, ahora con
                                             `plantilla` OPCIONAL, que es el
                                             unico ensanche y no toca a ninguno
                                             de sus catorce llamantes
  . `R94.caidas_propias_entrecomilladas()` . las `C.n` del ejecutor
  . `R92.caidas_por_lead_heredado()`       . el contraste heredado, al lado
  . `R95.cifras_de_la_fila_de_puestos()`   . la metrica, si su forma calza
  . `SERIE.entradas/siguiente_libre/...`   . el numero, que no se teclea

LAS TRES FORMAS DE CLAVE NO SE INVENTAN: SE MIDIERON. Se contaron sobre las
cuatro actas de esta vuelta antes de escribir el patron, y son:

  1. `**`6.1` TITULO`   negrita CON comillas inversas . la forma de la 184 en
                        adelante, que es la que el heredado ya leia
  2. `**6.1 TITULO`     negrita SIN comillas inversas . las ADJUDICACIONES de
                        las actas 173, 174, 175 y 176
  3. `### 4.1 TITULO`   titular markdown . los HALLAZGOS de las actas 173 y 174

Y LA TRAMPA QUE EL PATRON TIENE QUE ESQUIVAR, MEDIDA Y NO SUPUESTA: en el cuerpo
de estas actas hay lineas como ``**3.388 filas, A 551, ...**`` y
``**32.568 bytes**``, que son CIFRAS CON SEPARADOR DE MILLAR y no claves. No se
cuelan porque la clave se busca **por su prefijo exacto**, que es el numero de
LA SECCION, y `3.` y `32.` no son el numero de ninguna seccion de las que se
miran.
"""
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

sys.path.insert(0, AQUI)
import vuelta184_tarea1a_registrar_acta184 as R84           # noqa: E402
import vuelta192_tarea1a_registrar_acta192 as R92           # noqa: E402
import vuelta194_tarea1a_registrar_acta194 as R94           # noqa: E402
import vuelta195_tarea1a_registrar_acta195 as R95           # noqa: E402

ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")

# LA PLANTILLA ANCHA, CON LAS TRES FORMAS MEDIDAS. Lleva UN solo `%s`, donde va
# la clave ya escapada, que es el contrato del parametro `plantilla` de
# `R84.claves_entrecomilladas()`.
PLANTILLA_ANCHA = r"^\s*(?:\*\*`?|#{2,4}\s+`?)%s`?[ .:,]"

# LA PLANTILLA VIEJA, COPIADA BYTE A BYTE DE LO QUE LA 184 TENIA DENTRO, PARA
# PODER CORRER LAS DOS AL LADO Y MEDIR LA DIFERENCIA EN VEZ DE AFIRMARLA.
PLANTILLA_VIEJA = r"^\s*\*\*`%s` "

# LOS TITULOS QUE NOMBRAN CADA NUMERAL. LA VARA DICE QUE EL NUMERAL SE TOMA DE
# LA SECCION CUYO PROPIO TITULO LO NOMBRA, asi que aqui vive LO QUE SE BUSCA EN
# EL TITULO, y nunca un numero de seccion.
MARCAS = {
    "adjudicaciones": ("ADJUDICACIONES", "LA ADJUDICACION"),
    "hallazgos": ("LOS HALLAZGOS", "HALLAZGOS"),
    "caidas_del_auditor": ("MIS CAIDAS PROPIAS", "MIS PROPIAS CAIDAS"),
    "caidas_del_ejecutor": ("LA CAIDA DEL EJECUTOR", "LAS CAIDAS DEL EJECUTOR"),
}

# LA FORMA DE CLAVE DE LAS SECCIONES DE CAIDAS DE ESTAS ACTAS VIEJAS, TAMBIEN
# MEDIDA ANTES DE ESCRIBIRSE: `- **`CAIDA 1`. TITULO`. NO es `N.M`, y por eso
# NO se cuenta con la plantilla ancha: se cuenta con la suya y SE DECLARA.
PAT_CAIDA_VIEJA = re.compile(r"^\s*[-*]?\s*\*\*`CAIDA (\d+)`")


def cuerpo_del_acta(vuelta, texto=None):
    """EL ACTA ACOTADA: (lineas, (inicio, fin), error). PURA cuando se le pasa
    `texto`. La cota se COMPUTA de las cabeceras y CAE EN ROJO si la cabecera no
    aparece exactamente una vez. Clonada del registrador de la 200 y de la 202,
    con la vuelta por parametro en vez de por constante."""
    if texto is None:
        texto = io.open(ACTA, encoding="utf-8").read()
    texto = texto.replace(chr(13) + NL, NL)
    lineas = texto.split(NL)
    pat = re.compile(r"^#\s*ACTA DEL AUDITOR,\s*VUELTA %d\b" % vuelta)
    hits = [i for i, l in enumerate(lineas, 1) if pat.match(l)]
    if len(hits) != 1:
        return lineas, None, ("la cabecera de la vuelta %d aparece %d veces y se "
                              "necesita exactamente 1" % (vuelta, len(hits)))
    ini = hits[0]
    sig = [i for i, l in enumerate(lineas, 1)
           if i > ini and re.match(r"^#\s+ACTA\b", l)]
    fin = (sig[0] - 1) if sig else len(lineas)
    return lineas, (ini, fin), None


def secciones(lineas, ini, fin):
    """LAS SECCIONES DEL ACTA, cada una (numero, linea, titulo, desde, hasta).
    PURA. El numero se LEE de la cabecera y el titulo tambien: aqui no se decide
    nada, se transcribe lo que el documento escribe."""
    cabs = []
    for i in range(ini, fin + 1):
        m = re.match(r"^##\s+(\d+)\.\s*(.+?)\s*$", lineas[i - 1])
        if m:
            cabs.append((int(m.group(1)), i, m.group(2)))
    salida = []
    for k, (num, i, titulo) in enumerate(cabs):
        hasta = (cabs[k + 1][1] - 1) if k + 1 < len(cabs) else fin
        salida.append((num, i, titulo, i, hasta))
    return salida


def seccion_por_titulo(secs, marcas):
    """LA SECCION CUYO PROPIO TITULO NOMBRA EL NUMERAL. Devuelve la lista de las
    que calzan, que quien llama publica entera: si son 0 se DECLARA que ninguna
    seccion titula ese numeral, y si son mas de 1 se DECLARA la ambiguedad. AQUI
    NO SE ELIGE POR NUMERO DE SECCION, que es justo lo que la vara prohibe."""
    return [s for s in secs if any(m in s[2] for m in marcas)]


def claves_de(lineas, sec, plantilla=None):
    """LAS CLAVES `N.M` DE UNA SECCION, contadas por SU PROPIA NUMERACION.
    Devuelve (claves, lineas_por_clave). El prefijo es el numero de la seccion,
    leido de su cabecera, NUNCA tecleado."""
    num, _i, _t, a, b = sec
    prefijo = "%d." % num
    claves = R84.claves_entrecomilladas(lineas, a, b, prefijo,
                                        plantilla=plantilla or PLANTILLA_ANCHA)
    donde = {}
    for clave, _n in claves:
        pat = re.compile((plantilla or PLANTILLA_ANCHA) % re.escape(clave))
        donde[clave] = [i for i in range(a, b + 1) if pat.match(lineas[i - 1])]
    return claves, donde


def caidas_viejas(lineas, a, b):
    """LAS CAIDAS DE LA FORMA `- **`CAIDA n`. TITULO`, que es la que estas actas
    viejas usan. Devuelve (clave, linea, literal). NO es `N.M` y por eso NO se
    cuenta con la plantilla ancha: se cuenta con la suya y se declara."""
    salida = []
    for i in range(a, b + 1):
        m = PAT_CAIDA_VIEJA.match(lineas[i - 1])
        if m:
            salida.append(("CAIDA %s" % m.group(1), i, lineas[i - 1].strip()))
    return salida


PAT_LEAD_DE_CAIDA = re.compile(
    r"^\s*[-*]?\s*\*\*`?((?:CAIDA|AMAGO)[^*`:.]*)")


def leads_de_caida(lineas, a, b):
    """LOS ENCABEZADOS EN NEGRITA QUE ABREN CON LA PALABRA `CAIDA` O `AMAGO`,
    LLEVEN O NO NUMERO Y LLEVEN O NO COMILLAS INVERSAS. Devuelve (lead, linea,
    literal). PURA.

    POR QUE HACE FALTA, Y ESTA MEDIDO, NO SUPUESTO: el acta 176 escribe su caida
    del ejecutor como ``**CAIDA DE REPORTE 1: ...``, que **no es `N.M`** y
    **tampoco es ``**`CAIDA n`.``**. Un lector que solo mirase esas dos formas
    publicaria un CERO sobre una seccion que el acta titula LA CAIDA DEL
    EJECUTOR, CON SU NOMBRE, y ese cero se leeria como que no hubo caida. Esta
    lectura va AL LADO de las otras dos, no en vez de ellas, y quien llama
    publica las tres."""
    salida = []
    for i in range(a, b + 1):
        m = PAT_LEAD_DE_CAIDA.match(lineas[i - 1])
        if m:
            salida.append((m.group(1).strip(), i, lineas[i - 1].strip()))
    return salida


def preguntas_del_reporte(ruta):
    """LAS CLAVES `P.n` QUE EL REPORTE PONE EN SU SECCION DE PREGUNTAS, y el
    titulo literal de esa seccion. Devuelve (claves, titulo). Clonada del
    registrador de la 200 y de la 202, con la ruta por parametro. CAE
    devolviendo lista vacia y el motivo si el fichero no esta o si la seccion no
    aparece una sola vez, y ENTONCES LA CIFRA NO SE PUBLICA POR ESTA VIA."""
    if not os.path.isfile(ruta):
        return [], "(no existe %s)" % os.path.basename(ruta)
    lineas_r = io.open(ruta, encoding="utf-8").read().replace(
        chr(13) + NL, NL).split(NL)
    hits = [i for i, l in enumerate(lineas_r, 1)
            if re.match(r"^##\s+\d+\.\s+PREGUNTAS\b", l)]
    if len(hits) != 1:
        return [], "la seccion de PREGUNTAS aparece %d veces" % len(hits)
    a = hits[0]
    sig = [i for i, l in enumerate(lineas_r, 1)
           if i > a and re.match(r"^##\s+\d+\.", l)]
    b = (sig[0] - 1) if sig else len(lineas_r)
    claves = []
    for i in range(a, b + 1):
        for m in re.finditer(r"`(P\.\d+)`", lineas_r[i - 1]):
            if m.group(1) not in claves:
                claves.append(m.group(1))
    return claves, "%s (lineas %d a %d)" % (lineas_r[a - 1].strip(), a, b)


def filas_que_empiezan(lineas, ini, fin, prefijos):
    """LAS FILAS DE TABLA QUE EMPIEZAN POR UNO DE LOS PREFIJOS, con su linea. Se
    PEGAN enteras y no se les extrae ninguna cifra: son citas."""
    salida = []
    for i in range(ini, fin + 1):
        s = lineas[i - 1].strip()
        if any(s.startswith(p) for p in prefijos):
            salida.append((i, s))
    return salida


def medir_acta(vuelta, w):
    """MIDE UN ACTA VIEJA ENTERA POR LA VARA DEL `4.1` Y DEVUELVE SU
    DICCIONARIO, o None si la cota no se puede computar. NO ESCRIBE NADA."""
    datos = io.open(ACTA, "rb").read()
    lf = datos.replace(b"\r\n", b"\n")
    lineas, cota, err = cuerpo_del_acta(vuelta)
    w("   docs/loop/ACTA_AUDITOR.md: disco %d bytes | LF %d bytes"
      % (len(datos), len(lf)))
    if err:
        w("   ROJO: %s" % err)
        return None
    ini, fin = cota
    w("   CUERPO ACOTADO del acta %d: lineas %d a %d, %d lineas"
      % (vuelta, ini, fin, fin - ini + 1))

    secs = secciones(lineas, ini, fin)
    w("   CIFRA secciones `## N. TITULO` del cuerpo: %d" % len(secs))
    for num, i, titulo, a, b in secs:
        w("      seccion %-2d linea %5d  lineas %d a %d  %s"
          % (num, i, a, b, titulo[:70]))

    m = dict(vuelta=vuelta, ini=ini, fin=fin, bytes_disco=len(datos),
             bytes_lf=len(lf), lineas=lineas, secs=secs)

    # LOS CUATRO NUMERALES QUE SALEN DE UNA SECCION TITULADA.
    for etiqueta in ("adjudicaciones", "hallazgos", "caidas_del_auditor",
                     "caidas_del_ejecutor"):
        cand = seccion_por_titulo(secs, MARCAS[etiqueta])
        w("   %s: %d seccion(es) cuyo TITULO lo nombra"
          % (etiqueta.upper().replace("_", " "), len(cand)))
        for num, i, titulo, _a, _b in cand:
            w("      -> seccion %d, linea %d, titulo literal: %r" % (num, i, titulo))
        if len(cand) != 1:
            w("      NINGUNA CIFRA POR ESTA VIA, Y SE DECLARA EN VEZ DE PUBLICAR")
            w("      UN CERO: %s."
              % ("ninguna seccion de esta acta titula ese numeral"
                 if not cand else
                 "el titulo lo nombran %d secciones y eso seria DECIDIR"
                 % len(cand)))
            m[etiqueta] = None
            m[etiqueta + "_sec"] = None
            continue
        sec = cand[0]
        m[etiqueta + "_sec"] = sec
        if etiqueta.startswith("caidas"):
            # LA FORMA DE CLAVE DE LAS CAIDAS DE ESTAS ACTAS NO ES `N.M`, y eso
            # se mide y se dice: se cuentan LAS DOS formas, la vieja `CAIDA n` y
            # la `N.M` de la vara, y las dos se publican.
            nm, donde = claves_de(lineas, sec)
            viejas = caidas_viejas(lineas, sec[3], sec[4])
            leads = leads_de_caida(lineas, sec[3], sec[4])
            heredado = R94.caidas_propias_entrecomilladas(lineas, sec[3], sec[4])
            w("      claves `%d.M` por la vara: %d (%s)"
              % (sec[0], len(nm), ", ".join(c for c, _n in nm) or "ninguna"))
            w("      claves `CAIDA n` de la forma vieja: %d (%s)"
              % (len(viejas), ", ".join(c for c, _l, _t in viejas) or "ninguna"))
            w("      leads en negrita que abren con CAIDA o AMAGO: %d (%s)"
              % (len(leads), "; ".join(c for c, _l, _t in leads) or "ninguno"))
            for c, ln, tt in leads:
                w("         linea %5d | %s" % (ln, tt[:110]))
            w("      `R94.caidas_propias_entrecomilladas()` heredado: %d"
              % len(heredado))
            m[etiqueta] = dict(nm=nm, donde=donde, viejas=viejas, leads=leads,
                               heredado=heredado, sec=sec)
        else:
            nm, donde = claves_de(lineas, sec)
            viejo, _d = claves_de(lineas, sec, PLANTILLA_VIEJA)
            w("      claves `%d.M` POR LA VARA ANCHA: %d (%s)"
              % (sec[0], len(nm), ", ".join(c for c, _n in nm) or "ninguna"))
            w("      claves `%d.M` POR LA PLANTILLA HEREDADA, publicada al lado:"
              " %d (%s)"
              % (sec[0], len(viejo), ", ".join(c for c, _n in viejo) or "ninguna"))
            m[etiqueta] = dict(nm=nm, donde=donde, heredado=viejo, sec=sec)

    # EL CONTRASTE HEREDADO ENTERO, SOBRE EL CUERPO Y NO SOBRE UNA SECCION.
    for pref in ("4.", "5.", "6.", "7.", "C.A"):
        h = R84.claves_entrecomilladas(lineas, ini, fin, pref)
        w("   CONTRASTE HEREDADO R84.claves_entrecomilladas(prefijo %r) -> %d"
          % (pref, len(h)))
    eje_h, aud_h, hue_h = R92.caidas_por_lead_heredado(lineas, ini, fin)
    w("   CONTRASTE HEREDADO R92.caidas_por_lead_heredado() -> ejecutor %d, "
      "auditor %d, huerfanas %d" % (len(eje_h), len(aud_h), len(hue_h)))
    m["eje_h"], m["aud_h"], m["hue_h"] = eje_h, aud_h, hue_h

    # LAS PREGUNTAS CONTESTADAS. LA VARA DEL `4.7` DEL ACTA 201: las claves
    # `P.n` NOMBRADAS EN LOS TITULOS DE LAS ADJUDICACIONES, filtradas contra la
    # seccion de PREGUNTAS del reporte archivado CUANDO ESE REPORTE EXISTE.
    nombradas = []
    if m.get("adjudicaciones"):
        for clave, _n in m["adjudicaciones"]["nm"]:
            for ln in m["adjudicaciones"]["donde"][clave]:
                for mm in re.finditer(r"`(P\.\d+)`", lineas[ln - 1]):
                    if mm.group(1) not in nombradas:
                        nombradas.append(mm.group(1))
    ruta_rep = os.path.join(LOOP, "reportes", "REPORTE_V%d.md" % vuelta)
    existe_rep = os.path.isfile(ruta_rep)
    bytes_rep = os.path.getsize(ruta_rep) if existe_rep else None
    del_reporte, seccion_preg = preguntas_del_reporte(ruta_rep)
    w("   docs/loop/reportes/REPORTE_V%d.md existe: %s"
      % (vuelta, "SI" if existe_rep else "NO"))
    w("   bytes medidos con os.path.getsize: %s"
      % (bytes_rep if existe_rep else
         "NINGUNO, y el cero sale de que NO HAY FICHERO, no de medir uno"))
    w("   CIFRA claves `P.n` nombradas en los titulos de las adjudicaciones: %d"
      " (%s)" % (len(nombradas), ", ".join(nombradas) or "ninguna"))
    w("   CIFRA claves `P.n` que el reporte llama pregunta: %d (%s)  [%s]"
      % (len(del_reporte), ", ".join(del_reporte) or "ninguna", seccion_preg))
    # EL FILTRO SOLO SE PUEDE CORRER SI HAY REPORTE **Y** SI ESE REPORTE TIENE
    # SU SECCION DE PREGUNTAS. Las dos cosas se miden aparte y se dicen aparte:
    # UN REPORTE QUE EXISTE PERO NO TITULA NINGUNA SECCION DE PREGUNTAS deja el
    # filtro tan inservible como un reporte que no existe, y publicar entonces
    # un 0 se leeria como que el acta no contesto ninguna pregunta, que es la
    # lectura falsa que la vuelta 201 ya rechazo en su entrada de la 198.
    hay_seccion = existe_rep and not seccion_preg.startswith(
        "la seccion de PREGUNTAS aparece")
    if hay_seccion:
        preguntas = [p for p in nombradas if p in del_reporte]
        via = "FILTRADAS contra la seccion de PREGUNTAS del reporte archivado"
    elif existe_rep:
        preguntas = list(nombradas)
        via = ("NOMBRADAS EN LOS TITULOS DE LAS ADJUDICACIONES, porque el "
               "reporte de esa vuelta SI EXISTE pero NO TITULA NINGUNA SECCION "
               "DE PREGUNTAS y el filtro no se puede correr (vara del `4.7` del "
               "acta 201)")
    else:
        preguntas = list(nombradas)
        via = ("NOMBRADAS EN LOS TITULOS DE LAS ADJUDICACIONES, porque el "
               "reporte de esa vuelta NO EXISTE y el filtro no se puede correr "
               "(vara del `4.7` del acta 201)")
    w("   CIFRA preguntas del numeral: %d, por la via: %s" % (len(preguntas), via))
    m.update(nombradas=nombradas, del_reporte=del_reporte, preguntas=preguntas,
             via_preguntas=via, existe_rep=existe_rep, bytes_rep=bytes_rep,
             seccion_preg=seccion_preg, hay_seccion_preg=hay_seccion,
             fuera=[p for p in nombradas if p not in preguntas],
             ruta_rep="docs/loop/reportes/REPORTE_V%d.md" % vuelta)

    # LA METRICA DE CREDITO, PEGADA Y NO EXTRAIDA.
    filas = filas_que_empiezan(lineas, ini, fin,
                               ("| relecturas", "| puestos", "| discrepancias",
                                "| caidas"))
    fila_puestos = [(ln, s) for ln, s in filas if s.startswith("| puestos")]
    lectura = None
    if fila_puestos:
        lectura = R95.cifras_de_la_fila_de_puestos(fila_puestos[0][1])
        w("   R95.cifras_de_la_fila_de_puestos() sobre la linea %d devuelve %r"
          % (fila_puestos[0][0], lectura))
    for ln, s in filas:
        w("   linea %5d | %s" % (ln, s))
    m["filas"] = filas
    m["lectura_puestos"] = lectura
    return m


def prueba_por_mutacion(w):
    """EL CASO ROJO DE LA UNICA CONDUCTA PROPIA DE ESTE FICHERO, CORRIDO ANTES DE
    ESCRIBIR NADA (`EJECUTOR.md` 1, EL CASO ROJO SE PRUEBA POR MUTACION).

    Lo que se prueba es EL ENSANCHE DE LA PLANTILLA, sobre textos FABRICADOS
    aqui dentro, sin tocar el repo. NINGUN VEREDICTO ES UNA CONSTANTE LITERAL:
    todos salen de correr `R84.claves_entrecomilladas()` sobre esos textos, y la
    segunda pasada MUTA el esperado y exige que CADA CASO CAIGA."""
    casos = [
        ("negrita CON comillas, la forma de la 184",
         ["**`6.1` TITULO", "**`6.2` TITULO"], "6.", 2, 2),
        ("negrita SIN comillas, la forma de las adjudicaciones viejas",
         ["**6.1 TITULO", "**6.2 TITULO", "**6.3 TITULO"], "6.", 3, 0),
        ("titular markdown, la forma de los hallazgos viejos",
         ["### 4.1 TITULO", "### 4.2 TITULO"], "4.", 2, 0),
        ("la cifra con separador de millar NO es una clave",
         ["**3.388 filas, A 551, B 72**"], "3.", 0, 0),
        ("la cifra de bytes con millar NO es una clave",
         ["**32.568 bytes** y sale identico"], "32.", 0, 0),
        ("la numeracion CORTA en el primer hueco",
         ["**6.1 TITULO", "**6.3 TITULO"], "6.", 1, 0),
        ("una clave citada EN MITAD de la prosa no cuenta",
         ["hablo de la **6.1 TITULO** por ahi"], "6.", 0, 0),
        ("seccion vacia da cero por las dos plantillas",
         ["texto cualquiera"], "6.", 0, 0),
        ("la 10 y siguientes tambien entran, que es la 174",
         ["**6.%d TITULO" % k for k in range(1, 11)], "6.", 10, 0),
    ]
    verdes = rojos = distintos = 0
    w("   LA PLANTILLA HEREDADA CORRE AL LADO, ENTERA Y SIN TOCAR, que es lo")
    w("   unico que convierte 'hacia falta ensancharla' en una medicion:")
    for nombre, lineas, prefijo, esp_ancha, esp_vieja in casos:
        ancha = R84.claves_entrecomilladas(lineas, 1, len(lineas), prefijo,
                                           plantilla=PLANTILLA_ANCHA)
        vieja = R84.claves_entrecomilladas(lineas, 1, len(lineas), prefijo,
                                           plantilla=PLANTILLA_VIEJA)
        por_defecto = R84.claves_entrecomilladas(lineas, 1, len(lineas), prefijo)
        ok = (len(ancha) == esp_ancha and len(vieja) == esp_vieja
              and len(por_defecto) == len(vieja))
        if len(ancha) != len(vieja):
            distintos += 1
        w("   %-56s ancha %-2d (esp %-2d) vieja %-2d (esp %-2d) defecto %-2d %s"
          % (nombre[:56], len(ancha), esp_ancha, len(vieja), esp_vieja,
             len(por_defecto), "VERDE" if ok else "ROJO"))
        verdes += 1 if ok else 0
        rojos += 0 if ok else 1
    w("   CIFRA casos donde la ancha y la heredada DISCREPAN: %d" % distintos)
    w("   LA TERCERA COLUMNA ES LA QUE PRUEBA QUE NINGUN LLAMANTE VIEJO SE")
    w("   MUEVE: `defecto` es la funcion llamada SIN el parametro nuevo, y en")
    w("   los %d casos da EXACTAMENTE lo mismo que la plantilla heredada."
      % len(casos))
    w("   LA SEGUNDA PASADA MUTA EL ESPERADO Y EXIGE QUE CADA CASO CAIGA:")
    caen = 0
    for nombre, lineas, prefijo, esp_ancha, _esp_vieja in casos:
        ancha = R84.claves_entrecomilladas(lineas, 1, len(lineas), prefijo,
                                           plantilla=PLANTILLA_ANCHA)
        if len(ancha) != esp_ancha + 1:
            caen += 1
    w("   CIFRA casos que CAEN con el esperado mutado: %d de %d"
      % (caen, len(casos)))
    w("   CIFRA casos: %d | verdes: %d | rojos: %d" % (len(casos), verdes, rojos))
    return rojos == 0 and caen == len(casos)
