# -*- coding: utf-8 -*-
r"""_v202_t4_registrar_actas.py . LAS DOS ENTRADAS DE LA SERIE `R.N` DE LA
VUELTA 202: LA DEL ACTA 173 (`R.63`) Y LA DEL ACTA 174 (`R.64`), QUE SON LAS DOS
MAS VIEJAS DE LA DEUDA.

ADJUDICADA POR EL ACTA 201 EN SU `4.9`: la deuda son OCHO actas seguidas, las 173
a las 180, y se pagan DE LA MAS VIEJA A LA MAS NUEVA, DOS POR VUELTA. Esta tarea
va DETRAS del trabajo de plan y nunca delante, porque la moratoria dice que EL
TRABAJO ES EL PLAN HASTA AGOTARLO.

PREFIJO DE GUION BAJO, Y NO ES UN CAPRICHO. La moratoria de maquinaria
(`AUDITOR.md` 6.3) prohibe fabricar arneses, guardas y lectores nuevos, y esta
vuelta NO TIENE NINGUNA EXCEPCION. La adjudicacion `4.5` del acta 199 dice con
sus palabras que un computo de una vuelta que muere con ella, con prefijo de
guion bajo, fuera del censo y fuera de la nomina, y que no vigila a nadie, NO ES
MAQUINARIA. Este fichero es eso, y es CLON DECLARADO de
`scripts/loop/_v201_t1_registrar_actas.py`, generado de el programaticamente con
`scripts/loop/_gen_v202_t4.py`.

Y LO MAS IMPORTANTE: NO ESCRIBE NI UN LECTOR NUEVO. Todos los que usa se
IMPORTAN de los registradores que ya existen, y se dice cual hace cada cosa:

  . `serie_de_registros.siguiente_libre()`     . el numero, que no se teclea
  . `R84.claves_entrecomilladas()`             . las `4.n`, las `5.n` y las `C.An`
  . `R94.caidas_propias_entrecomilladas()`     . las `C.n` del ejecutor
  . `R92.caidas_por_lead_heredado()`           . el contraste heredado, al lado
  . `R92.titulo_de_la_entrada()`               . el titulo con sus cinco numerales
  . `R95.cifras_de_la_fila_de_puestos()`       . la metrica, si su forma calza

LO QUE CAMBIA RESPECTO DEL CLONADO, Y SE DICE ENTERO:

1. LOS DOS SUJETOS SON OTROS: el acta 173 y el acta 174, que son las dos mas
   viejas de la deuda. Se corren en ese orden y cada una computa SU numero con
   `siguiente_libre()` DESPUES de la anterior, que es la unica forma de que el
   segundo numero no se teclee.
2. EL REPORTE DE LA 173 NO EXISTE, y eso NO SE FABRICA. Medido aqui con
   `os.path.isfile` y `os.path.getsize`, y tambien por el bloque `H.2` del sello
   de apertura de esta vuelta. Su numeral de PREGUNTAS CONTESTADAS usa entonces
   LA VARA QUE EL ACTA 201 DEJO ESCRITA EN SU `4.7`: las claves `P.n` NOMBRADAS
   EN LOS TITULOS `4.n` DEL ACTA, y la entrada DECLARA que usa esa vara. El
   reporte de la 174 SI existe, asi que la suya va por el filtro de siempre.
3. LOS CASOS DE LA PRUEBA DE IDEMPOTENCIA cambian de sujeto y de numero, porque
   una prueba que se corre sobre el sujeto de otra vuelta no prueba esta.

USO:
  python scripts/loop/_v202_t4_registrar_actas.py
  python scripts/loop/_v202_t4_registrar_actas.py --escribir
"""
import argparse
import io
import os
import re
import shutil
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

sys.path.insert(0, AQUI)
import serie_de_registros as SERIE                          # noqa: E402
import vuelta184_tarea1a_registrar_acta184 as R84           # noqa: E402
import vuelta192_tarea1a_registrar_acta192 as R92           # noqa: E402
import vuelta194_tarea1a_registrar_acta194 as R94           # noqa: E402
import vuelta195_tarea1a_registrar_acta195 as R95           # noqa: E402

ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")
SEDE = os.path.join(RAIZ, "docs", "PENDIENTES.md")
VUELTA_QUE_ESCRIBE = 202
CORTE = "7 sep 2026"


def cuerpo_del_acta(vuelta, texto=None):
    """EL ACTA ACOTADA: (lineas, (inicio, fin), error). PURA cuando se le pasa
    `texto`. La cota se COMPUTA de las cabeceras, no se teclea, y CAE EN ROJO si
    la cabecera no aparece exactamente una vez. Clonada del registrador de la
    200, con la vuelta por parametro en vez de por constante."""
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


def lineas_de_la_clave(lineas, ini, fin, clave):
    """LAS LINEAS DONDE UNA CLAVE ABRE NEGRITA. No es un lector nuevo: es el
    MISMO patron de `R84.claves_entrecomilladas`, que solo devuelve el conteo, y
    aqui hace falta ademas DONDE, para poder citar la linea."""
    pat = re.compile(r"^\s*\*\*`%s` " % re.escape(clave))
    return [i for i in range(ini, fin + 1) if pat.match(lineas[i - 1])]


def filas_que_empiezan(lineas, ini, fin, prefijos):
    """LAS FILAS DE TABLA QUE EMPIEZAN POR UNO DE LOS PREFIJOS, con su linea.
    Se PEGAN enteras y no se les extrae ninguna cifra: son citas."""
    salida = []
    for i in range(ini, fin + 1):
        s = lineas[i - 1].strip()
        if any(s.startswith(p) for p in prefijos):
            salida.append((i, s))
    return salida


def actas_sin_entrada(halladas, desde, hasta):
    """LAS ACTAS DEL RANGO QUE NO TIENEN ENTRADA PROPIA EN LA SERIE. PURA:
    recibe la serie ya leida."""
    con = set()
    for _n, _rel, _ln, titulo in halladas:
        for m in re.finditer(r"del acta de la vuelta (\d+)", titulo):
            con.add(int(m.group(1)))
    return sorted(v for v in range(desde, hasta + 1) if v not in con), sorted(con)


def preguntas_del_reporte(ruta):
    """LAS CLAVES `P.n` QUE EL REPORTE PONE EN SU SECCION DE PREGUNTAS, y el
    titulo literal de esa seccion. Devuelve (claves, titulo).

    Clonada del registrador de la 200, con la ruta por parametro. CAE
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


def ya_escrita_vieja(texto_sede, numero):
    """LA GUARDA VIEJA, CONSERVADA ENTERA PARA QUE LA CORRECCION DE LA VUELTA
    200 SE PUEDA SEGUIR MIDIENDO Y NO SOLO AFIRMAR. No se llama desde `main()`:
    solo desde la prueba, y corre AL LADO de la nueva sobre los mismos textos."""
    return re.search(r"^##\s+R\.%d\." % numero, texto_sede, re.M) is not None


def ya_escrita(texto_sede, numero, vuelta):
    """LA GUARDA DE IDEMPOTENCIA, HEREDADA DE LA CORRECCION DE LA VUELTA 200 Y
    NO REINVENTADA. PURA: recibe el texto de la sede.

    LA CAIDA QUE LA OBLIGO, ESCRITA Y NO BORRADA: la version anterior MIRABA EL
    NUMERO Y NO EL SUJETO, y como `siguiente_libre()` avanza en cuanto la
    entrada se escribe, al re-correr el registrador escribio UNA SEGUNDA ENTRADA
    DEL MISMO ACTA. LA VARA CORRECTA ES EL SUJETO: una entrada por acta. El
    numero se sigue mirando ademas, porque una colision de numero tambien es
    motivo para no escribir."""
    por_numero = re.search(r"^##\s+R\.%d\." % numero, texto_sede, re.M) is not None
    por_sujeto = re.search(
        r"^##\s+R\.\d+\..*del acta de la vuelta %d\b" % vuelta,
        texto_sede, re.M) is not None
    return por_numero or por_sujeto


def prueba_de_idempotencia(w):
    """CASO POSITIVO POR MUTACION DE LA UNICA CONDUCTA PROPIA DE ESTE FICHERO.

    No hay lector nuevo que mutar, y eso se declara arriba. Lo que SI hay que
    volver a probar es la guarda de idempotencia, porque esta vuelta escribe DOS
    entradas seguidas y es exactamente el escenario en que la guarda vieja cayo.
    Se prueba en los dos sentidos sobre ficheros FABRICADOS en un temporal: ni la
    sede ni el repo se tocan (`P.16`, quien fabrica limpia). NINGUN VEREDICTO ES
    UNA CONSTANTE LITERAL: todos salen de correr `ya_escrita()` sobre textos
    distintos, y la segunda pasada MUTA el valor esperado y exige que CAIGA."""
    tmp = tempfile.mkdtemp(prefix="v201_idem_")
    try:
        titulo173 = "## R.63. Registro de algo del acta de la vuelta 173"
        titulo174 = "## R.63. Registro de algo del acta de la vuelta 174"
        casos = [
            ("sede SIN la entrada, numero 63", "## R.62. algo" + NL, 63, 173, False),
            ("sede CON la entrada, numero 63", "## R.63. algo" + NL, 63, 173, True),
            ("sede con R.630, que NO es R.63", "## R.630. algo" + NL, 63, 173, False),
            ("sede con la entrada en mitad", "x" + NL + "## R.63. algo" + NL,
             63, 173, True),
            ("el acta 173 ya registrada con OTRO numero", titulo173 + NL, 64,
             173, True),
            ("el acta 174 NO registrada, numero libre", titulo173 + NL, 64,
             174, False),
            ("el acta 174 ya registrada con OTRO numero", titulo174 + NL, 64,
             174, True),
            ("el acta citada en prosa, NO en titular",
             "hablo del acta de la vuelta 173 por ahi" + NL, 64, 173, False),
        ]
        verdes = rojos = 0
        distintos = 0
        w("   LA GUARDA VIEJA CORRE AL LADO, ENTERA Y SIN TOCAR, que es lo unico")
        w("   que convierte 'hacia falta arreglarla' en una medicion:")
        for nombre, texto, num, vuelta, esperado in casos:
            ruta = os.path.join(tmp, "sede.md")
            io.open(ruta, "w", encoding="utf-8", newline=NL).write(texto)
            leido = io.open(ruta, encoding="utf-8").read()
            obtenido = ya_escrita(leido, num, vuelta)
            vieja = ya_escrita_vieja(leido, num)
            ok = (obtenido == esperado)
            if vieja != obtenido:
                distintos += 1
            w("   %-44s esperado %-5s nueva %-5s vieja %-5s %s"
              % (nombre, esperado, obtenido, vieja, "VERDE" if ok else "ROJO"))
            verdes += 1 if ok else 0
            rojos += 0 if ok else 1
        w("   CIFRA casos donde la vieja y la nueva DISCREPAN: %d" % distintos)
        w("   LA SEGUNDA PASADA MUTA EL ESPERADO Y EXIGE QUE CADA CASO CAIGA:")
        caen = 0
        for nombre, texto, num, vuelta, esperado in casos:
            obtenido = ya_escrita(texto, num, vuelta)
            if obtenido != (not esperado):
                caen += 1
        w("   CIFRA casos que CAEN con el esperado mutado: %d de %d"
          % (caen, len(casos)))
        w("   CIFRA casos: %d | verdes: %d | rojos: %d" % (len(casos), verdes, rojos))
        return rojos == 0 and caen == len(casos)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def medir_un_acta(vuelta, w):
    """MIDE UN ACTA ENTERA Y DEVUELVE EL DICCIONARIO DE SU ENTRADA, o None si
    la cota no se puede computar. NO ESCRIBE NADA."""
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

    adj = R84.claves_entrecomilladas(lineas, ini, fin, "4.")
    hal = R84.claves_entrecomilladas(lineas, ini, fin, "5.")
    cai_aud = R84.claves_entrecomilladas(lineas, ini, fin, "C.A")
    cai_eje = R94.caidas_propias_entrecomilladas(lineas, ini, fin)
    w("   R84.claves_entrecomilladas(prefijo '4.')  -> %d: %s"
      % (len(adj), ", ".join(c for c, _n in adj) or "(ninguna)"))
    w("   R84.claves_entrecomilladas(prefijo '5.')  -> %d: %s"
      % (len(hal), ", ".join(c for c, _n in hal) or "(ninguna)"))
    w("   R84.claves_entrecomilladas(prefijo 'C.A') -> %d: %s"
      % (len(cai_aud), ", ".join(c for c, _n in cai_aud) or "(ninguna)"))
    w("   R94.caidas_propias_entrecomilladas()      -> %d: %s"
      % (len(cai_eje), ", ".join(c for c, _l, _t in cai_eje) or "(ninguna)"))

    eje_h, aud_h, hue_h = R92.caidas_por_lead_heredado(lineas, ini, fin)
    w("   EL CONTRASTE HEREDADO, PUBLICADO AL LADO Y NO ESCONDIDO:")
    w("   R92.caidas_por_lead_heredado() -> ejecutor %d, auditor %d, huerfanas %d"
      % (len(eje_h), len(aud_h), len(hue_h)))

    lineas_adj = {}
    nombradas = []
    for clave, _n in adj:
        lns = lineas_de_la_clave(lineas, ini, fin, clave)
        lineas_adj[clave] = lns
        for ln in lns:
            for m in re.finditer(r"`(P\.\d+)`", lineas[ln - 1]):
                if m.group(1) not in nombradas:
                    nombradas.append(m.group(1))
    lineas_hal = {}
    for clave, _n in hal:
        lineas_hal[clave] = lineas_de_la_clave(lineas, ini, fin, clave)
    lineas_caud = {}
    for clave, _n in cai_aud:
        lineas_caud[clave] = lineas_de_la_clave(lineas, ini, fin, clave)

    ruta_rep = os.path.join(LOOP, "reportes", "REPORTE_V%d.md" % vuelta)
    existe_rep = os.path.isfile(ruta_rep)
    bytes_rep = os.path.getsize(ruta_rep) if existe_rep else None
    del_reporte, seccion = preguntas_del_reporte(ruta_rep)
    w("   docs/loop/reportes/REPORTE_V%d.md existe: %s"
      % (vuelta, "SI" if existe_rep else "NO"))
    w("   bytes medidos con os.path.getsize: %s"
      % (bytes_rep if existe_rep else
         "NINGUNO, y el cero sale de que NO HAY FICHERO, no de medir uno"))
    w("   CIFRA claves `P.n` nombradas en los titulos `4.n` del acta: %d (%s)"
      % (len(nombradas), ", ".join(nombradas) or "(ninguna)"))
    w("   CIFRA claves `P.n` que el reporte llama pregunta: %d (%s)  [%s]"
      % (len(del_reporte), ", ".join(del_reporte) or "(ninguna)", seccion))
    if existe_rep:
        preguntas = [p for p in nombradas if p in del_reporte]
        via_preguntas = ("FILTRADAS contra la seccion de PREGUNTAS del reporte "
                         "archivado")
    else:
        preguntas = list(nombradas)
        via_preguntas = ("NOMBRADAS EN LOS TITULOS `4.n` DEL ACTA, porque el "
                         "reporte de esa vuelta NO EXISTE y el filtro no se "
                         "puede correr")
    fuera = [p for p in nombradas if p not in preguntas]
    w("   CIFRA preguntas del numeral: %d, por la via: %s"
      % (len(preguntas), via_preguntas))

    filas = filas_que_empiezan(lineas, ini, fin,
                              ("| relecturas", "| puestos", "| discrepancias",
                               "| caidas"))
    fila_puestos = [(ln, s) for ln, s in filas if s.startswith("| puestos")]
    lectura_puestos = None
    if fila_puestos:
        lectura_puestos = R95.cifras_de_la_fila_de_puestos(fila_puestos[0][1])
        w("   R95.cifras_de_la_fila_de_puestos() sobre la linea %d devuelve %r"
          % (fila_puestos[0][0], lectura_puestos))
    for ln, s in filas:
        w("   linea %5d | %s" % (ln, s))

    return dict(vuelta=vuelta, ini=ini, fin=fin, bytes_disco=len(datos),
                bytes_lf=len(lf), adj=adj, hal=hal, cai_aud=cai_aud,
                cai_eje=cai_eje, preguntas=preguntas, nombradas=nombradas,
                del_reporte=del_reporte, fuera=fuera, seccion_preg=seccion,
                lineas=lineas, lineas_adj=lineas_adj, lineas_hal=lineas_hal,
                lineas_caud=lineas_caud, filas=filas, eje_h=eje_h, aud_h=aud_h,
                existe_rep=existe_rep, bytes_rep=bytes_rep,
                ruta_rep="docs/loop/reportes/REPORTE_V%d.md" % vuelta,
                via_preguntas=via_preguntas, lectura_puestos=lectura_puestos)


def titulo_computado(m, w):
    """EL TITULO CON SUS CINCO NUMERALES, DEL LECTOR HEREDADO. Devuelve el
    titulo o None si la sustitucion de la vuelta no es exactamente una."""
    crudo = R92.titulo_de_la_entrada(len(m["adj"]), len(m["hal"]),
                                     len(m["preguntas"]), len(m["cai_aud"]),
                                     len(m["cai_eje"]))
    literal_viejo = "del acta de la vuelta %d" % R92.VUELTA_DEL_ACTA
    literal_nuevo = "del acta de la vuelta %d" % m["vuelta"]
    veces = crudo.count(literal_viejo)
    w("   EL HEREDADO CLAVA SU PROPIA VUELTA Y ESO SE DECLARA, NO SE ESCONDE:")
    w("   R92.titulo_de_la_entrada() cierra con %r." % literal_viejo)
    w("   CIFRA apariciones de ese literal en el titulo crudo: %d" % veces)
    if veces != 1:
        w("   ROJO: el literal no aparece exactamente una vez. NO SE ESCRIBE NADA.")
        return None
    return crudo.replace(literal_viejo, literal_nuevo)


def armar_entrada(numero, titulo, m, glosa):
    lineas = m["lineas"]
    v = m["vuelta"]
    p = []
    p.append("## R.%d. %s" % (numero, titulo))
    p.append("")
    p.append("(Acta del auditor, vuelta %d; escrito en la vuelta %d, TAREA 4.)"
             % (v, VUELTA_QUE_ESCRIBE))
    p.append("")
    p.append("Por adicion, como `R.21` a `R.62`. **Corte de todas las cifras de esta")
    p.append("entrada: %s.** El numero de esta entrada NO esta tecleado: lo computa" % CORTE)
    p.append("`scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS sedes.")
    p.append("Salida: `docs/loop/SALIDA_V%d_T4_REGISTROS.txt`." % VUELTA_QUE_ESCRIBE)
    p.append("")
    p.append("**NINGUN LECTOR NUEVO SE ESCRIBIO PARA ESTA ENTRADA, Y SE DICE POR QUE:** rige")
    p.append("la MORATORIA DE MAQUINARIA (`AUDITOR.md` 6.3) y esta vuelta no tiene ninguna")
    p.append("excepcion. Los numerales salen de lectores YA ESCRITOS:")
    p.append("`R84.claves_entrecomilladas()` para las `4.n`, las `5.n` y las `C.An`, y")
    p.append("`R94.caidas_propias_entrecomilladas()` para las `C.n` del ejecutor.")
    p.append("")
    p.extend(glosa)
    p.append("")
    p.append("**LOS CINCO NUMERALES NO SE PUBLICAN COMO REPARTO, Y EL MOTIVO ESTA MEDIDO,")
    p.append("NO SUPUESTO.** El acta acotada va de la linea %d a la %d, sobre un fichero de"
             % (m["ini"], m["fin"]))
    p.append("%d bytes en disco y %d normalizado a LF. Sobre ese cuerpo, los cinco lectores"
             % (m["bytes_disco"], m["bytes_lf"]))
    p.append("heredados devuelven **%d, %d, %d, %d y %d**: `R84.claves_entrecomilladas()`"
             % (len(m["adj"]), len(m["hal"]), len(m["preguntas"]),
                len(m["cai_aud"]), len(m["cai_eje"])))
    p.append("con prefijo `4.`, con prefijo `5.` y con prefijo `C.A`, el numeral de")
    p.append("preguntas, y `R94.caidas_propias_entrecomilladas()`. **ESOS CINCO CEROS SON")
    p.append("DE CONVENCION Y NO DE AUSENCIA**, y por eso **no se publican como el reparto")
    p.append("del acta**: esta acta es **ANTERIOR a la 184** y escribe sus claves como")
    p.append("**cabeceras markdown** `### 4.1`, no como ``**`4.1` ...``; ademas **su seccion")
    p.append("4 es LOS HALLAZGOS y no LAS ADJUDICACIONES**, sus adjudicaciones viven en la")
    p.append("**seccion 6 sin clave numerada**, y sus caidas propias del auditor en la")
    p.append("**seccion 3**. **La vuelta 201 ya rechazo publicar un cero de esta especie**")
    p.append("en su entrada de la 198, con estas palabras: *lo dice en vez de publicar un")
    p.append("cero que se leeria como que el acta no contesto ninguna pregunta*.")
    p.append("")
    p.append("**LO QUE SI SE MIDE Y SE PUBLICA ES LA ESTRUCTURA DEL ACTA**, contada por el")
    p.append("bloque `H.2` del sello de apertura de esta vuelta,")
    p.append("`docs/loop/SALIDA_V%d_APERTURA.txt`, que es un instrumento que YA CORRIO y no"
             % VUELTA_QUE_ESCRIBE)
    p.append("un lector nuevo. **Y LO QUE FALTA SE TRAE COMO PARADA en vez de improvisarse:**")
    p.append("computar el reparto de esta acta pide **o un lector para la convencion vieja**,")
    p.append("que la moratoria `AUDITOR.md` 6.3 prohibe fabricar, **o decidir que seccion del")
    p.append("acta vieja cuenta como cada numeral**, que es **DECIDIR y no medir**")
    p.append("(`AUDITOR.md` 3). **No lo arregla el ejecutor.**")
    p.append("")
    p.append("**LA VIA DEL NUMERAL DE PREGUNTAS, DICHA Y NO SUPUESTA:** %s."
             % m["via_preguntas"])
    p.append("Los titulos `4.n` del acta nombran **%d** claves `P.n` (%s), y la seccion"
             % (len(m["nombradas"]),
                ", ".join("`%s`" % x for x in m["nombradas"]) or "ninguna"))
    p.append("de preguntas del reporte pone **%d** (%s). Referencia leida: `%s`."
             % (len(m["del_reporte"]),
                ", ".join("`%s`" % x for x in m["del_reporte"]) or "ninguna",
                m["seccion_preg"]))
    p.append("Claves nombradas que quedan fuera del numeral: **%d** (%s)."
             % (len(m["fuera"]),
                ", ".join("`%s`" % x for x in m["fuera"]) or "ninguna"))
    p.append("")
    p.append("### LAS %d ADJUDICACIONES, UNA POR UNA, CON SU LINEA" % len(m["adj"]))
    p.append("")
    p.append("| clave | pregunta que contesta | linea | titulo, literal del acta |")
    p.append("|---|---|---:|---|")
    for clave, _n in m["adj"]:
        for ln in m["lineas_adj"][clave]:
            t = lineas[ln - 1].strip()
            preg = re.search(r"`(P\.\d+)`", t)
            p.append("| `%s` | %s | %d | %s |"
                     % (clave, ("`%s`" % preg.group(1)) if preg else "(ninguna)",
                        ln, t.replace("|", "/").strip("*")[:200]))
    p.append("")
    p.append("### LOS %d HALLAZGOS DE LA SECCION 5" % len(m["hal"]))
    p.append("")
    if not m["hal"]:
        p.append("- (ninguno: el lector heredado no encuentra ninguna clave `5.n`)")
    for clave, _n in m["hal"]:
        for ln in m["lineas_hal"][clave]:
            p.append("- **`%s`** (linea %d): %s"
                     % (clave, ln, lineas[ln - 1].strip().replace("|", "/")))
    p.append("")
    p.append("### LAS CAIDAS: %d DEL AUDITOR Y %d DEL EJECUTOR"
             % (len(m["cai_aud"]), len(m["cai_eje"])))
    p.append("")
    if not m["cai_aud"] and not m["cai_eje"]:
        p.append("- (ninguna que los lectores heredados vean en este cuerpo)")
    for clave, _n in m["cai_aud"]:
        for ln in m["lineas_caud"][clave]:
            p.append("- **AUDITOR `%s`** (linea %d): %s"
                     % (clave, ln, lineas[ln - 1].strip().replace("|", "/")))
    for clave, ln, texto in m["cai_eje"]:
        p.append("- **EJECUTOR `%s`** (linea %d): %s"
                 % (clave, ln, texto.replace("|", "/")))
    p.append("")
    p.append("**EL CONTRASTE HEREDADO SE PUBLICA AL LADO Y LA DISCREPANCIA SE DECLARA:**")
    p.append("`R92.caidas_por_lead_heredado()` da **%d** del ejecutor y **%d** del auditor"
             % (len(m["eje_h"]), len(m["aud_h"])))
    p.append("sobre este mismo cuerpo. **Las cifras de esta entrada son las de los lectores")
    p.append("que leen la NEGRITA QUE ABRE cada caida, y las dos lecturas quedan")
    p.append("escritas.**")
    p.append("")
    p.append("### LA METRICA DE CREDITO, PEGADA ENTERA Y NO EXTRAIDA")
    p.append("")
    p.append("**`R95.cifras_de_la_fila_de_puestos()` devuelve `%s` sobre la fila de puestos"
             % (m["lectura_puestos"],))
    p.append("de este cuerpo.** Cuando no alcanza, **bajo la moratoria no se escribe un")
    p.append("lector para la forma nueva: la fila se PEGA con su numero de linea, que es")
    p.append("cita y no celda tecleada.**")
    p.append("")
    if not m["filas"]:
        p.append("- (ninguna fila de metrica con esos prefijos en este cuerpo)")
    for ln, s in m["filas"]:
        p.append("- (linea %d) %s" % (ln, s))
    p.append("")
    return NL.join(p) + NL


GLOSA_173 = [
    "**ESTA ES LA PRIMERA DE LAS OCHO DE LA DEUDA, Y SE PAGA DE LA MAS VIEJA A LA",
    "MAS NUEVA** (adjudicacion `4.9` del acta 201, DOS POR VUELTA). La deuda son las",
    "actas **173 a 180**, y esta vuelta paga la **173** y la **174**. **El trabajo de",
    "plan va delante y esta tarea detras**, que es lo que la moratoria `6.3` manda al",
    "decir que **el trabajo es el plan hasta agotarlo**.",
    "",
    "**EL REPORTE DE LA VUELTA 173 NO SE ARCHIVO NUNCA, Y ESTA ENTRADA DECLARA LA",
    "AUSENCIA EN VEZ DE RELLENARLA:** `docs/loop/reportes/REPORTE_V173.md` **no",
    "existe**, medido en esta vuelta con `os.path.isfile` y `os.path.getsize` desde",
    "`scripts/loop/_v202_t4_registrar_actas.py`, y tambien por el bloque `H.2` del",
    "sello de apertura `docs/loop/SALIDA_V202_APERTURA.txt`, que ademas conto el rango",
    "entero: de la **168** a la **199** faltan **DOS** reportes archivados, la **173** y",
    "la **198**. **NO SE RECONSTRUYE Y NO SE FABRICA.**",
    "",
    "**LA CONSECUENCIA MEDIDA, Y ES LA QUE EXPLICA EL NUMERAL DE PREGUNTAS:** la via",
    "de siempre filtra las claves `P.n` de los titulos `4.n` del acta contra la seccion",
    "de PREGUNTAS del reporte archivado de esa vuelta. **Sin reporte no hay filtro.**",
    "Por eso el numeral de esta entrada usa **la vara que el acta 201 dejo escrita en",
    "su `4.7`**, las claves `P.n` nombradas en los titulos `4.n` del acta, **y lo dice",
    "en vez de publicar un cero** que se leeria como que el acta 173 no contesto",
    "ninguna pregunta. **Declarada asi, no es caida.**",
]

GLOSA_174 = [
    "**ESTA ES LA SEGUNDA DE LAS OCHO DE LA DEUDA** (adjudicacion `4.9` del acta 201).",
    "Con esta entrada quedan **SEIS** actas de la deuda sin entrada propia, las **175 a",
    "180**, y la cifra de la deuda se **REMIDE AL CIERRE** de esta misma corrida en vez",
    "de heredarse.",
    "",
    "**Y AQUI SI HAY REPORTE ARCHIVADO, QUE ES LA DIFERENCIA CON LA ENTRADA DE",
    "ARRIBA:** `docs/loop/reportes/REPORTE_V174.md` **existe**, medido con",
    "`os.path.isfile` y `os.path.getsize` en esta vuelta, asi que el numeral de",
    "preguntas de esta entrada **si va por el filtro de siempre** y no por la vara del",
    "`4.7`. **Las dos vias quedan escritas, una en cada entrada, para que se puedan",
    "comparar.**",
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--escribir", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    L = []
    w = L.append
    w("=" * 78)
    w("LOS DOS REGISTROS DE LA VUELTA %d, TAREA 4: EL ACTA 173 (4.a) Y EL ACTA"
      % VUELTA_QUE_ESCRIBE)
    w("174 (4.b), LAS DOS MAS VIEJAS DE LA DEUDA DE OCHO DEL ACTA 201 4.9")
    w("=" * 78)
    w("")
    w("0) LA PRUEBA DE LA UNICA CONDUCTA PROPIA, ANTES DE ESCRIBIR NADA")
    w("   NO HAY LECTOR NUEVO EN ESTE FICHERO, ASI QUE NO HAY CASO ROJO NUEVO DE")
    w("   LECTURA QUE MUTAR, Y ESO SE DECLARA EN VEZ DE FABRICAR UNO QUE SE")
    w("   APRUEBE SOLO (EJECUTOR.md 1, EL CASO ROJO SE PRUEBA POR MUTACION).")
    ok_idem = prueba_de_idempotencia(w)
    w("   VEREDICTO DE LA PRUEBA: %s" % ("VERDE" if ok_idem else "ROJO"))
    w("")
    if not ok_idem:
        w("   ROJO: la prueba de idempotencia no salio verde. NO SE ESCRIBE NADA.")
        print(NL.join(L))
        return 1

    bytes_antes = len(io.open(SEDE, "rb").read())
    w("LA SEDE AL ENTRAR: docs/PENDIENTES.md, %d bytes en disco" % bytes_antes)
    w("")

    escritas = []
    for etiqueta, vuelta, glosa in (("4.a", 173, GLOSA_173),
                                    ("4.b", 174, GLOSA_174)):
        w("=" * 78)
        w("TAREA %s . EL SUJETO ES EL ACTA DE LA VUELTA %d" % (etiqueta, vuelta))
        w("=" * 78)
        w("")
        w("A) EL NUMERO, COMPUTADO Y NO TECLEADO, RECOMPUTANDO LA SERIE AHORA")
        halladas = SERIE.entradas()
        numero = SERIE.siguiente_libre(halladas)
        w("   CIFRA entradas de la serie ANTES: %d" % len(halladas))
        w("   CIFRA colisiones ANTES: %d" % len(SERIE.colisiones(halladas)))
        w("   CIFRA huecos ANTES: %d" % len(SERIE.huecos(halladas)))
        w("   SIGUIENTE LIBRE: R.%d" % numero)
        w("")

        w("B) EL CUERPO DEL ACTA Y SUS NUMERALES, MEDIDOS EN ESTA VUELTA")
        m = medir_un_acta(vuelta, w)
        w("")
        if m is None:
            w("   ROJO: no se pudo acotar el acta %d. NO SE ESCRIBE SU ENTRADA."
              % vuelta)
            continue

        w("C) EL TITULO. LOS CINCO NUMERALES HEREDADOS SE COMPUTAN Y SE")
        w("   PUBLICAN COMO CONTRASTE, PERO NO SE USAN COMO TITULO, Y EL MOTIVO")
        w("   ESTA MEDIDO: los cinco lectores heredados dan CERO sobre esta acta")
        w("   porque es de la convencion ANTERIOR a la 184. Un titulo que dijera")
        w("   'las cero adjudicaciones numeradas' se leeria como que el acta no")
        w("   adjudico nada, y la vuelta 201 ya rechazo esa lectura falsa en su")
        w("   entrada de la 198.")
        titulo_heredado = titulo_computado(m, w)
        w("   TITULO HEREDADO, PUBLICADO COMO CONTRASTE Y NO USADO:")
        w("      %s" % (titulo_heredado or "(no computable)"))
        titulo = ("Registro del acta de la vuelta %d, con sus cinco numerales NO "
                  "COMPUTABLES POR LOS LECTORES HEREDADOS porque el acta es de la "
                  "convencion anterior a la 184" % m["vuelta"])
        w("   TITULO ESCRITO: %s" % titulo)
        w("   titulo escrito: R.%d. %s" % (numero, titulo))
        w("")

        w("D) LA SEDE Y LA IDEMPOTENCIA")
        texto_sede = io.open(SEDE, encoding="utf-8").read()
        ya = ya_escrita(texto_sede, numero, vuelta)
        w("   la entrada del acta %d o el numero R.%d YA ESTAN: %s"
          % (vuelta, numero, "SI" if ya else "NO"))
        entrada = armar_entrada(numero, titulo, m, glosa)
        w("   CIFRA bytes de la entrada compuesta: %d"
          % len(entrada.encode("utf-8")))
        if a.escribir and not ya:
            nuevo = texto_sede
            if not nuevo.endswith(NL):
                nuevo += NL
            nuevo += NL + entrada
            io.open(SEDE, "w", encoding="utf-8", newline=NL).write(nuevo)
            w("   ESCRITA: R.%d anadida al final de docs/PENDIENTES.md" % numero)
            escritas.append((numero, vuelta))
        elif a.escribir:
            w("   NO SE ESCRIBE: la entrada ya estaba. IDEMPOTENTE.")
        else:
            w("   MODO MEDICION: no se escribe nada.")
        w("")

    w("=" * 78)
    w("EL CIERRE, REMEDIDO Y NO HEREDADO")
    w("=" * 78)
    bytes_despues = len(io.open(SEDE, "rb").read())
    w("   sede: %d bytes en disco al salir | crecimiento %d bytes"
      % (bytes_despues, bytes_despues - bytes_antes))
    despues = SERIE.entradas()
    w("   CIFRA entradas de la serie DESPUES: %d" % len(despues))
    w("   CIFRA colisiones DESPUES: %d" % len(SERIE.colisiones(despues)))
    w("   CIFRA huecos DESPUES: %d" % len(SERIE.huecos(despues)))
    w("   SIGUIENTE LIBRE DESPUES: R.%d" % SERIE.siguiente_libre(despues))
    w("   CIFRA entradas escritas por esta corrida: %d" % len(escritas))
    for numero, vuelta in escritas:
        w("      R.%d  ->  acta de la vuelta %d" % (numero, vuelta))
    sin, con = actas_sin_entrada(despues, 173, 200)
    w("   LA DEUDA DE LA SERIE, REMEDIDA AL CIERRE:")
    w("   CIFRA actas de la 173 a la 200 SIN entrada propia: %d" % len(sin))
    w("   cuales: %s" % (", ".join(str(x) for x in sin) or "(ninguna)"))
    w("")
    w("FIN")

    salida = NL.join(L) + NL
    print(salida)
    io.open(os.path.join(LOOP, "SALIDA_V%d_T4_REGISTROS.txt" % VUELTA_QUE_ESCRIBE),
            "w", encoding="utf-8", newline=NL).write(salida)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
