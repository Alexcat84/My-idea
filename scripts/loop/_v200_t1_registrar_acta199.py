# -*- coding: utf-8 -*-
r"""_v200_t1_registrar_acta199.py . LA ENTRADA DE LA SERIE `R.N` PARA EL ACTA 199.

PREFIJO DE GUION BAJO, Y NO ES UN CAPRICHO. La moratoria de maquinaria
(`AUDITOR.md` 6.3) prohibe fabricar arneses, guardas y lectores nuevos, y esta
vuelta NO TIENE NINGUNA EXCEPCION. La adjudicacion `4.5` del acta 199 dice con
sus palabras que un computo de una vuelta que muere con ella, con prefijo de
guion bajo, fuera del censo y fuera de la nomina, y que no vigila a nadie, NO ES
MAQUINARIA: es una instancia de un computo ordenado. Este fichero es eso.

Y LO MAS IMPORTANTE: NO ESCRIBE NI UN LECTOR NUEVO. Todos los que usa se
IMPORTAN de los registradores que ya existen, y se dice cual hace cada cosa:

  . `serie_de_registros.siguiente_libre()`            . el numero, que no se teclea
  . `R84.claves_entrecomilladas()`                    . las `4.n`, las `5.n` y las `C.An`
  . `R94.caidas_propias_entrecomilladas()`            . las `C.n` del ejecutor
  . `R92.caidas_por_lead_heredado()`                  . el contraste heredado, publicado al lado
  . `R92.titulo_de_la_entrada()`                      . el titulo con sus cinco numerales

LO QUE NO SE PUEDE LEER CON UN LECTOR HEREDADO SE DECLARA Y SE CITA, NO SE
FABRICA. `R95.cifras_de_la_fila_de_puestos()` devuelve `(None, None, None, None)`
sobre la fila de puestos del acta 199, porque esa fila tiene otra forma
(`51 sellados, 49 cotejados, 2 en mi hueco`). Aqui NO se escribe un lector para
esa forma: la fila se PEGA ENTERA con su numero de linea, que es cita y no celda
tecleada.

USO:
  python scripts/loop/_v200_t1_registrar_acta199.py --medir
  python scripts/loop/_v200_t1_registrar_acta199.py --escribir
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
VUELTA_DEL_ACTA = 199
VUELTA_QUE_ESCRIBE = 200


def cuerpo_del_acta(texto=None, vuelta=VUELTA_DEL_ACTA):
    """EL ACTA ACOTADA: (lineas, (inicio, fin), error). PURA cuando se le pasa
    `texto`. La cota se COMPUTA de las cabeceras, no se teclea, y CAE EN ROJO si
    la cabecera no aparece exactamente una vez."""
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
    recibe la serie ya leida. La entrada nombra su acta en el titulo con la
    forma `del acta de la vuelta N`."""
    con = set()
    for _n, _rel, _ln, titulo in halladas:
        for m in re.finditer(r"del acta de la vuelta (\d+)", titulo):
            con.add(int(m.group(1)))
    return sorted(v for v in range(desde, hasta + 1) if v not in con), sorted(con)


REPORTE_199 = os.path.join(LOOP, "reportes", "REPORTE_V199.md")


def preguntas_del_reporte(ruta=None):
    """LAS CLAVES `P.n` QUE EL REPORTE PONE EN SU SECCION DE PREGUNTAS, y el
    titulo literal de esa seccion. Devuelve (claves, titulo).

    NO ES UN LECTOR DE ACTA NI VIGILA A NADIE: es el mismo computo de acotar por
    cabeceras que ya hace `cuerpo_del_acta()`, aplicado al reporte, porque LA
    FUENTE HAY QUE ELEGIRLA ANTES DE CONTARLA y quien decide si una `P.n` es
    pregunta o discutible es el reporte que la escribio, no el acta que la cita.
    CAE devolviendo lista vacia y el motivo si la seccion no aparece una sola
    vez, y entonces la cifra NO se publica."""
    ruta = ruta or REPORTE_199
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
    """LA GUARDA VIEJA, CONSERVADA ENTERA PARA QUE LA CORRECCION SE PUEDA MEDIR
    Y NO SOLO AFIRMAR. No se llama desde `main()`: solo desde la prueba, y
    corre AL LADO de la nueva sobre los mismos textos."""
    return re.search(r"^##\s+R\.%d\." % numero, texto_sede, re.M) is not None


def ya_escrita(texto_sede, numero, vuelta=VUELTA_DEL_ACTA):
    """LA GUARDA DE IDEMPOTENCIA. PURA: recibe el texto de la sede.

    CORRECCION DECLARADA, MEDIDA EN ESTA MISMA VUELTA Y SIN TAPAR LO QUE CORRIGE
    (`EJECUTOR.md` 8). LO QUE ESTA FUNCION HACIA ANTES, ESCRITO Y NO BORRADO:

        return re.search("^##  R.%d." % numero, texto_sede, re.M) is not None

    o sea, MIRABA EL NUMERO Y NO EL SUJETO. Y el numero lo elige
    `SERIE.siguiente_libre()`, que AVANZA en cuanto la entrada se escribe: al
    re-correr el registrador para probar la idempotencia, el siguiente libre ya
    era `R.61`, la guarda dijo que `R.61` no estaba (y era cierto) y ESCRIBIO UNA
    SEGUNDA ENTRADA DEL MISMO ACTA. Medido: la sede paso de 1079444 a 1086030
    bytes en disco y la serie de 52 a 53 entradas. La duplicada se retiro con
    `git checkout --` y la sede volvio a su estado del commit.

    LA VARA CORRECTA ES EL SUJETO: una entrada por acta. Se busca el literal que
    el propio titulo de la entrada escribe, `del acta de la vuelta N`, que es el
    mismo que `actas_sin_entrada()` ya usa para medir la deuda de la serie. El
    numero se sigue mirando ademas, porque una colision de numero tambien es
    motivo para no escribir."""
    por_numero = re.search(r"^##\s+R\.%d\." % numero, texto_sede, re.M) is not None
    por_sujeto = re.search(
        r"^##\s+R\.\d+\..*del acta de la vuelta %d\b" % vuelta,
        texto_sede, re.M) is not None
    return por_numero or por_sujeto


def prueba_de_idempotencia(w):
    """CASO POSITIVO POR MUTACION DE LA UNICA CONDUCTA PROPIA DE ESTE FICHERO.

    No hay lector nuevo que mutar, y eso se declara arriba. Lo que SI es propio
    de aqui es la guarda de idempotencia, y se prueba en los dos sentidos sobre
    ficheros FABRICADOS en un temporal: ni la sede ni el repo se tocan (P.16,
    quien fabrica limpia). NINGUN VEREDICTO ES UNA CONSTANTE LITERAL: los cuatro
    salen de correr `ya_escrita()` sobre textos distintos, y la segunda pasada
    MUTA el valor esperado y exige que CAIGA."""
    tmp = tempfile.mkdtemp(prefix="v200_idem_")
    try:
        titulo199 = "## R.60. Registro de algo del acta de la vuelta 199"
        titulo198 = "## R.60. Registro de algo del acta de la vuelta 198"
        casos = [
            ("sede SIN la entrada, numero 60", "## R.59. algo" + NL, 60, False),
            ("sede CON la entrada, numero 60", "## R.60. algo" + NL, 60, True),
            ("sede con R.600, que NO es R.60", "## R.600. algo" + NL, 60, False),
            ("sede con la entrada en mitad", "x" + NL + "## R.60. algo" + NL,
             60, True),
            # LOS TRES DE LA CORRECCION DECLARADA: la guarda vieja miraba el
            # NUMERO y estos tres son los que la tumban.
            ("el acta ya registrada con OTRO numero", titulo199 + NL, 61, True),
            ("otra acta con el mismo numero libre", titulo198 + NL, 61, False),
            ("el acta citada en prosa, NO en titular",
             "hablo del acta de la vuelta 199 por ahi" + NL, 61, False),
        ]
        verdes = rojos = 0
        distintos = 0
        w("   LA GUARDA VIEJA CORRE AL LADO, ENTERA Y SIN TOCAR, que es lo unico")
        w("   que convierte 'hacia falta arreglarla' en una medicion:")
        for nombre, texto, num, esperado in casos:
            ruta = os.path.join(tmp, "sede.md")
            io.open(ruta, "w", encoding="utf-8", newline=NL).write(texto)
            leido = io.open(ruta, encoding="utf-8").read()
            obtenido = ya_escrita(leido, num)
            vieja = ya_escrita_vieja(leido, num)
            ok = (obtenido == esperado)
            if vieja != obtenido:
                distintos += 1
            w("   %-42s esperado %-5s nueva %-5s vieja %-5s %s"
              % (nombre, esperado, obtenido, vieja, "VERDE" if ok else "ROJO"))
            verdes += 1 if ok else 0
            rojos += 0 if ok else 1
        w("   CIFRA casos donde la vieja y la nueva DISCREPAN: %d" % distintos)
        w("   LA SEGUNDA PASADA MUTA EL ESPERADO Y EXIGE QUE CADA CASO CAIGA:")
        caen = 0
        for nombre, texto, num, esperado in casos:
            obtenido = ya_escrita(texto, num)
            if obtenido != (not esperado):
                caen += 1
        w("   CIFRA casos que CAEN con el esperado mutado: %d de %d"
          % (caen, len(casos)))
        w("   CIFRA casos: %d | verdes: %d | rojos: %d" % (len(casos), verdes, rojos))
        return rojos == 0 and caen == len(casos)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--escribir", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    L = []
    w = L.append
    w("=" * 78)
    w("REGISTRO DEL ACTA %d EN LA SERIE R.N (vuelta %d, TAREA 1)"
      % (VUELTA_DEL_ACTA, VUELTA_QUE_ESCRIBE))
    w("=" * 78)
    w("")
    w("A) EL NUMERO, COMPUTADO Y NO TECLEADO")
    halladas = SERIE.entradas()
    numero = SERIE.siguiente_libre(halladas)
    w("   CIFRA entradas de la serie ANTES: %d" % len(halladas))
    w("   CIFRA colisiones ANTES: %d" % len(SERIE.colisiones(halladas)))
    w("   CIFRA huecos ANTES: %d" % len(SERIE.huecos(halladas)))
    w("   SIGUIENTE LIBRE: R.%d" % numero)
    w("")

    w("B) EL CUERPO DEL ACTA, ACOTADO EN ESTA VUELTA Y NO HEREDADO")
    datos = io.open(ACTA, "rb").read()
    lf = datos.replace(b"\r\n", b"\n")
    lineas, cota, err = cuerpo_del_acta()
    w("   docs/loop/ACTA_AUDITOR.md: disco %d bytes | LF %d bytes"
      % (len(datos), len(lf)))
    if err:
        w("   ROJO: %s" % err)
        print(NL.join(L))
        return 1
    ini, fin = cota
    w("   CUERPO ACOTADO: lineas %d a %d, %d lineas" % (ini, fin, fin - ini + 1))
    w("")

    w("C) LOS NUMERALES, CONTADOS DEL CUERPO ACOTADO CON LECTORES HEREDADOS")
    w("   NINGUN LECTOR ES NUEVO. Se dice cual lee cada cosa.")
    adj = R84.claves_entrecomilladas(lineas, ini, fin, "4.")
    hal = R84.claves_entrecomilladas(lineas, ini, fin, "5.")
    cai_aud = R84.claves_entrecomilladas(lineas, ini, fin, "C.A")
    cai_eje = R94.caidas_propias_entrecomilladas(lineas, ini, fin)
    w("   R84.claves_entrecomilladas(prefijo '4.')  -> %d: %s"
      % (len(adj), ", ".join(c for c, _n in adj)))
    w("   R84.claves_entrecomilladas(prefijo '5.')  -> %d: %s"
      % (len(hal), ", ".join(c for c, _n in hal)))
    w("   R84.claves_entrecomilladas(prefijo 'C.A') -> %d: %s"
      % (len(cai_aud), ", ".join(c for c, _n in cai_aud)))
    w("   R94.caidas_propias_entrecomilladas()      -> %d: %s"
      % (len(cai_eje), ", ".join(c for c, _l, _t in cai_eje)))
    w("")
    w("   EL CONTRASTE HEREDADO, PUBLICADO AL LADO Y NO ESCONDIDO:")
    eje_h, aud_h, hue_h = R92.caidas_por_lead_heredado(lineas, ini, fin)
    w("   R92.caidas_por_lead_heredado() -> ejecutor %d, auditor %d, huerfanas %d"
      % (len(eje_h), len(aud_h), len(hue_h)))
    for ln, clave, negrita, _her in eje_h:
        w("      EJE %-5s linea %d: %s" % (clave, ln, negrita[:70]))
    for ln, clave, negrita, _her in aud_h:
        w("      AUD %-5s linea %d: %s" % (clave, ln, (negrita or "(sin negrita)")[:70]))
    w("   LA DISCREPANCIA SE DECLARA EN VEZ DE RESOLVERSE CALLANDO: el heredado")
    w("   da %d del ejecutor porque cuenta tambien la cita de `C.2` del parrafo"
      % len(eje_h))
    w("   del FILO, que el acta declara COMO CITA y no como caida nueva; y da %d"
      % len(aud_h))
    w("   del auditor porque las lee de la TABLA de la metrica, donde las tres")
    w("   `C.n` del ejecutor estan citadas. Las cifras que esta entrada publica")
    w("   son las de los lectores de arriba, que leen la NEGRITA QUE ABRE cada")
    w("   caida, y las dos lecturas quedan escritas.")
    w("")

    w("D) LAS PREGUNTAS CONTESTADAS, CONTADAS DE LOS DOS FICHEROS Y NO DE UNO")
    w("   LA FUENTE HAY QUE ELEGIRLA ANTES DE CONTARLA (regla del fundador, 4 sep")
    w("   2026). Aqui se cuentan LAS DOS y se dice cual manda: los titulos `4.n`")
    w("   del acta nombran claves `P.n`, y el REPORTE es quien decide cuales de")
    w("   esas claves son PREGUNTAS y cuales son DISCUTIBLES.")
    nombradas = []
    lineas_adj = {}
    for clave, _n in adj:
        lns = lineas_de_la_clave(lineas, ini, fin, clave)
        lineas_adj[clave] = lns
        for ln in lns:
            for m in re.finditer(r"`(P\.\d+)`", lineas[ln - 1]):
                if m.group(1) not in nombradas:
                    nombradas.append(m.group(1))
    w("   CIFRA claves `P.n` nombradas en los titulos `4.n` del acta: %d"
      % len(nombradas))
    w("   cuales: %s" % ", ".join(nombradas))
    del_reporte, seccion = preguntas_del_reporte()
    w("   CIFRA claves `P.n` que el reporte pone en su seccion de PREGUNTAS: %d"
      % len(del_reporte))
    w("   cuales: %s   (seccion: %s)" % (", ".join(del_reporte), seccion))
    preguntas = [p for p in nombradas if p in del_reporte]
    fuera = [p for p in nombradas if p not in del_reporte]
    w("   CIFRA preguntas CONTESTADAS (las nombradas que el reporte llama")
    w("      pregunta): %d, cuales: %s" % (len(preguntas), ", ".join(preguntas)))
    w("   CIFRA claves nombradas que el reporte NO llama pregunta: %d, cuales: %s"
      % (len(fuera), ", ".join(fuera) or "(ninguna)"))
    w("   LA DISCREPANCIA SE DECLARA Y NO SE RESUELVE CALLANDO: el acta dice en su")
    w("   apertura y en su seccion 6 que son LAS CUATRO PREGUNTAS DEL REPORTE, y")
    w("   sus titulos `4.n` nombran %d claves `P.n`. Las dos son ciertas sobre"
      % len(nombradas))
    w("   sujetos distintos, y el numeral del titulo de esta entrada usa el %d,"
      % len(preguntas))
    w("   que es el que calza con la cifra del acta.")
    w("")

    w("E) LAS ADJUDICACIONES, UNA POR UNA, CON SU LINEA Y SU TITULO LITERAL")
    for clave, _n in adj:
        for ln in lineas_adj[clave]:
            w("   %-4s linea %d: %s" % (clave, ln, lineas[ln - 1].strip()))
    w("")

    w("F) LOS HALLAZGOS, UNO POR UNO, CON SU LINEA Y SU TITULO LITERAL")
    lineas_hal = {}
    for clave, _n in hal:
        lns = lineas_de_la_clave(lineas, ini, fin, clave)
        lineas_hal[clave] = lns
        for ln in lns:
            w("   %-4s linea %d: %s" % (clave, ln, lineas[ln - 1].strip()))
    w("")

    w("G) LAS CAIDAS, UNA POR UNA, CON SU LINEA Y SU TITULO LITERAL")
    lineas_caud = {}
    for clave, _n in cai_aud:
        lns = lineas_de_la_clave(lineas, ini, fin, clave)
        lineas_caud[clave] = lns
        for ln in lns:
            w("   AUDITOR  %-5s linea %d: %s" % (clave, ln, lineas[ln - 1].strip()))
    for clave, ln, texto in cai_eje:
        w("   EJECUTOR %-5s linea %d: %s" % (clave, ln, texto))
    w("")

    w("H) LA METRICA, PEGADA ENTERA Y NO EXTRAIDA")
    w("   EL LECTOR HEREDADO NO ALCANZA Y SE DICE: R95.cifras_de_la_fila_de_puestos()")
    filas = filas_que_empiezan(lineas, ini, fin,
                              ("| relecturas", "| puestos", "| discrepancias",
                               "| caidas"))
    fila_puestos = [(ln, s) for ln, s in filas if s.startswith("| puestos")]
    if fila_puestos:
        w("   sobre la fila de puestos (linea %d) devuelve %r"
          % (fila_puestos[0][0], R95.cifras_de_la_fila_de_puestos(fila_puestos[0][1])))
        w("   POR ESO LA FILA SE PEGA Y NO SE EXTRAE. Una cifra que un lector")
        w("   heredado no sabe leer NO SE TECLEA: se cita con su linea.")
    for ln, s in filas:
        w("   linea %5d | %s" % (ln, s))
    w("")

    w("I) LA DEUDA DE LA SERIE, REMEDIDA Y NO HEREDADA")
    sin, con = actas_sin_entrada(halladas, 173, VUELTA_DEL_ACTA)
    w("   CIFRA actas de la 173 a la %d SIN entrada propia: %d"
      % (VUELTA_DEL_ACTA, len(sin)))
    w("   cuales: %s" % (", ".join(str(x) for x in sin) or "(ninguna)"))
    w("   CIFRA actas del rango CON entrada propia: %d"
      % len([x for x in con if 173 <= x <= VUELTA_DEL_ACTA]))
    w("")

    w("J) EL CASO POSITIVO POR MUTACION")
    w("   NO HAY LECTOR NUEVO EN ESTE FICHERO, ASI QUE NO HAY CASO ROJO NUEVO DE")
    w("   LECTURA QUE MUTAR, Y ESO SE DECLARA EN VEZ DE FABRICAR UNO QUE SE")
    w("   APRUEBE SOLO (EJECUTOR.md 1, EL CASO ROJO SE PRUEBA POR MUTACION). LO")
    w("   QUE SI ES PROPIO DE AQUI ES LA GUARDA DE IDEMPOTENCIA, Y SE PRUEBA:")
    ok_idem = prueba_de_idempotencia(w)
    w("   VEREDICTO DE LA PRUEBA: %s" % ("VERDE" if ok_idem else "ROJO"))
    w("")

    crudo = R92.titulo_de_la_entrada(len(adj), len(hal), len(preguntas),
                                     len(cai_aud), len(cai_eje))
    w("K) EL TITULO, CON SUS CINCO NUMERALES COMPUTADOS")
    w("   EL HEREDADO CLAVA SU PROPIA VUELTA Y ESO SE DECLARA, NO SE ESCONDE:")
    w("   R92.titulo_de_la_entrada() cierra con `del acta de la vuelta 192`,")
    w("   porque es el registrador de la 192 y ese numero vive en su constante.")
    w("   Aqui se SUSTITUYE ese literal por el de esta acta, y la sustitucion se")
    w("   mide: si el literal no aparece EXACTAMENTE UNA VEZ, no se escribe nada.")
    literal_viejo = "del acta de la vuelta %d" % R92.VUELTA_DEL_ACTA
    literal_nuevo = "del acta de la vuelta %d" % VUELTA_DEL_ACTA
    veces = crudo.count(literal_viejo)
    w("   CIFRA apariciones de %r en el titulo crudo: %d" % (literal_viejo, veces))
    if veces != 1:
        w("   ROJO: el literal no aparece exactamente una vez. NO SE ESCRIBE NADA.")
        print(NL.join(L))
        return 1
    titulo = crudo.replace(literal_viejo, literal_nuevo)
    w("   titulo crudo:  %s" % crudo)
    w("   titulo escrito: R.%d. %s" % (numero, titulo))
    w("")

    texto_sede = io.open(SEDE, encoding="utf-8").read()
    bytes_antes = len(io.open(SEDE, "rb").read())
    w("L) LA SEDE Y LA IDEMPOTENCIA")
    w("   sede: docs/PENDIENTES.md, %d bytes en disco al entrar" % bytes_antes)
    w("   la entrada R.%d YA ESTA ESCRITA: %s"
      % (numero, "SI" if ya_escrita(texto_sede, numero) else "NO"))

    if not ok_idem:
        w("   ROJO: la prueba de idempotencia no salio verde. NO SE ESCRIBE NADA.")
        print(NL.join(L))
        return 1

    entrada = armar_entrada(numero, titulo, dict(
        ini=ini, fin=fin, bytes_disco=len(datos), bytes_lf=len(lf),
        adj=adj, hal=hal, cai_aud=cai_aud, cai_eje=cai_eje,
        preguntas=preguntas, nombradas=nombradas, del_reporte=del_reporte,
        fuera=fuera, seccion_preg=seccion,
        lineas=lineas, lineas_adj=lineas_adj,
        lineas_hal=lineas_hal, lineas_caud=lineas_caud, filas=filas,
        sin=sin, eje_h=eje_h, aud_h=aud_h))

    if a.escribir and not ya_escrita(texto_sede, numero):
        nuevo = texto_sede
        if not nuevo.endswith(NL):
            nuevo += NL
        nuevo += NL + entrada
        io.open(SEDE, "w", encoding="utf-8", newline=NL).write(nuevo)
        w("   ESCRITA: R.%d anadida al final de docs/PENDIENTES.md" % numero)
    elif a.escribir:
        w("   NO SE ESCRIBE: la entrada ya estaba. IDEMPOTENTE.")
    else:
        w("   MODO MEDICION: no se escribe nada.")

    bytes_despues = len(io.open(SEDE, "rb").read())
    w("   sede: %d bytes en disco al salir | crecimiento %d bytes"
      % (bytes_despues, bytes_despues - bytes_antes))
    despues = SERIE.entradas()
    w("   CIFRA entradas de la serie DESPUES: %d" % len(despues))
    w("   CIFRA colisiones DESPUES: %d" % len(SERIE.colisiones(despues)))
    w("   CIFRA huecos DESPUES: %d" % len(SERIE.huecos(despues)))
    w("   SIGUIENTE LIBRE DESPUES: R.%d" % SERIE.siguiente_libre(despues))
    w("")
    w("FIN")

    salida = NL.join(L) + NL
    print(salida)
    io.open(os.path.join(LOOP, "SALIDA_V%d_T1A_REGISTRO_R%d.txt"
                         % (VUELTA_QUE_ESCRIBE, numero)),
            "w", encoding="utf-8", newline=NL).write(salida)
    return 0


def armar_entrada(numero, titulo, m):
    lineas = m["lineas"]
    p = []
    p.append("## R.%d. %s" % (numero, titulo))
    p.append("")
    p.append("(Acta del auditor, vuelta %d, secciones 0, 1, 2, 3, 4, 5, 6, 7 y 8; "
             "escrito en la vuelta %d, TAREA 1.)"
             % (VUELTA_DEL_ACTA, VUELTA_QUE_ESCRIBE))
    p.append("")
    p.append("Por adicion, como `R.21` a `R.59`. **Corte de todas las cifras de esta")
    p.append("entrada: 7 sep 2026.** El numero de esta entrada NO esta tecleado: lo computa")
    p.append("`scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS sedes.")
    p.append("Salida: `docs/loop/SALIDA_V%d_T1A_REGISTRO_R%d.txt`."
             % (VUELTA_QUE_ESCRIBE, numero))
    p.append("")
    p.append("**ESTA ENTRADA SE ESCRIBE CON LA TAREA 2 SIN EMPEZAR, ASI QUE SUS GLOSAS NO")
    p.append("AFIRMAN EN PASADO LO QUE TODAVIA NO HA PASADO** (la forma que la `6.4` del")
    p.append("acta 172 adjudico como correcta). **La 200 SI es vuelta de bateria**")
    p.append("(`AUDITOR.md` 6.1, cadencia de cinco desde la 194 y encargo expreso de la")
    p.append("199), y por eso su TAREA 2 es la bateria entera y no hay trabajo de plan al")
    p.append("lado.")
    p.append("")
    p.append("**NINGUN LECTOR NUEVO SE ESCRIBIO PARA ESTA ENTRADA, Y SE DICE POR QUE:** rige")
    p.append("la MORATORIA DE MAQUINARIA (`AUDITOR.md` 6.3) y esta vuelta no tiene ninguna")
    p.append("excepcion. Los numerales salen de lectores YA ESCRITOS:")
    p.append("`R84.claves_entrecomilladas()` para las `4.n`, las `5.n` y las `C.An`, y")
    p.append("`R94.caidas_propias_entrecomilladas()` para las `C.n` del ejecutor.")
    p.append("")
    p.append("**LOS CINCO NUMERALES DEL TITULO NO ESTAN TECLEADOS:** se cuentan del acta")
    p.append("acotada (lineas %d a %d, sobre un fichero de %d bytes en disco y %d "
             "normalizado a LF). **%d adjudicaciones numeradas (`4.1` a `4.%d`), %d "
             "hallazgos numerados en la seccion 5, %d preguntas contestadas DENTRO de las "
             "adjudicaciones, %d caidas propias del auditor y %d caidas del ejecutor.**"
             % (m["ini"], m["fin"], m["bytes_disco"], m["bytes_lf"],
                len(m["adj"]), len(m["adj"]), len(m["hal"]), len(m["preguntas"]),
                len(m["cai_aud"]), len(m["cai_eje"])))
    p.append("")
    p.append("**LA CIFRA DE PREGUNTAS SE CUENTA DE LOS DOS FICHEROS Y NO DE UNO, Y LA")
    p.append("DIFERENCIA SE DECLARA:** los titulos `4.n` del acta nombran **%d** claves"
             % len(m["nombradas"]))
    p.append("`P.n` (%s), y la seccion `%s` del reporte de la 199 pone **%d**"
             % (", ".join("`%s`" % x for x in m["nombradas"]),
                m["seccion_preg"], len(m["del_reporte"])))
    p.append("(%s). **La que sobra es %s**, que el reporte marca como DISCUTIBLE en su"
             % (", ".join("`%s`" % x for x in m["del_reporte"]),
                ", ".join("`%s`" % x for x in m["fuera"]) or "(ninguna)"))
    p.append("seccion 5 y no como pregunta en su seccion 6. **El numeral del titulo usa")
    p.append("las %d que el reporte llama pregunta**, que es la cifra que el acta publica"
             % len(m["preguntas"]))
    p.append("en su apertura y en su seccion 6. **Las dos lecturas quedan escritas.**")
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
    for clave, _n in m["hal"]:
        for ln in m["lineas_hal"][clave]:
            p.append("- **`%s`** (linea %d): %s"
                     % (clave, ln, lineas[ln - 1].strip().replace("|", "/")))
    p.append("")
    p.append("### LAS CAIDAS: %d DEL AUDITOR Y %d DEL EJECUTOR"
             % (len(m["cai_aud"]), len(m["cai_eje"])))
    p.append("")
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
    p.append("sobre este mismo cuerpo. Las **%d** del ejecutor incluyen la cita de `C.2`"
             % len(m["eje_h"]))
    p.append("que vive en el parrafo del FILO, que el acta declara COMO CITA y no como")
    p.append("caida nueva; y las **%d** del auditor las lee de la TABLA de la metrica,"
             % len(m["aud_h"]))
    p.append("donde las `C.n` del ejecutor estan citadas. **Las cifras de esta entrada son")
    p.append("las de los lectores que leen la NEGRITA QUE ABRE cada caida, y las dos")
    p.append("lecturas quedan escritas.**")
    p.append("")
    p.append("### LA METRICA DE CREDITO, PEGADA ENTERA Y NO EXTRAIDA")
    p.append("")
    p.append("**`R95.cifras_de_la_fila_de_puestos()` NO ALCANZA SOBRE ESTA ACTA y se dice:**")
    p.append("devuelve `(None, None, None, None)` sobre su fila de puestos, porque esa fila")
    p.append("tiene otra forma. **Bajo la moratoria no se escribe un lector para la forma")
    p.append("nueva: la fila se PEGA con su numero de linea, que es cita y no celda")
    p.append("tecleada.**")
    p.append("")
    for ln, s in m["filas"]:
        p.append("- (linea %d) %s" % (ln, s))
    p.append("")
    p.append("### LAS TRES CORRECCIONES DE CIFRA QUE ESTA MISMA TAREA ESCRIBE")
    p.append("")
    p.append("La seccion 3 del acta levanta **tres caidas de reporte**, y las tres se")
    p.append("corrigen **en su sede**, `docs/loop/reportes/REPORTE_V199.md`, por el carril")
    p.append("del banco `9.10` mas `EJECUTOR.md` 8, **con el texto viejo entero y sin")
    p.append("tachar**. La `C.1` es **la que acumula** y su cifra **no se corrige")
    p.append("tecleando el dos**: se recomputa corriendo `V.arneses_que_faltan(vara=148)`")
    p.append("en la apertura de esta vuelta.")
    p.append("")
    p.append("### LA DEUDA DE LA SERIE, REMEDIDA Y NO HEREDADA")
    p.append("")
    p.append("Actas 173 a %d sin entrada propia en la serie: **%d** (%s). **La cifra se")
    p.append("recomputa cada vuelta y no se hereda.**")
    p[-2] = p[-2] % (VUELTA_DEL_ACTA, len(m["sin"]),
                     ", ".join(str(x) for x in m["sin"]) or "ninguna")
    p.append("")
    return NL.join(p) + NL


if __name__ == "__main__":
    raise SystemExit(main())
