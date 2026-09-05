# -*- coding: utf-8 -*-
r"""cotejar_clon_declarado.py . UN CLON DECLARADO DEJA DE SER UNA AFIRMACION Y
PASA A SER UNA MEDICION.

NOMBRE ESTABLE Y SIN NUMERO DE VUELTA, como sus hermanos
`paso0_archivar_anterior.py`, `tallar_cabecera_reporte.py`, `archivar_reporte.py`,
`serie_de_registros.py`, `anexar_tarea_al_reporte.py`, `cerrar_reporte.py`,
`aislador_de_ciega.py` y `guarda_commit_dataset.py`: se invoca cada vez que una
vuelta clona un fichero de la anterior, y NO SE CLONA, para que el proximo clon
no lo pierda.

POR QUE NACE, Y LA CAUSA ESTA MEDIDA POR EL AUDITOR (acta de la vuelta 176,
seccion 5, CAIDA DE REPORTE 1). El reporte de la 176 publicaba que el `diff` del
esqueleto con el de la 175, con todo `175` y `176` sustituido por `NNN`, "SALE
VACIO". El auditor lo corrio y NO SALE VACIO: 58 lineas de diff, y 33 de ellas
de la maquina. Pero lo midio hasta el fondo antes de acusar, y el fondo cambia
la gravedad entera: de esas 33, SENTENCIAS DE CODIGO 0 y LITERALES DE TEXTO 33.
O sea que lo que la frase QUERIA DECIR (la maquina no cambia) era cierto, y lo
que PUBLICABA (el diff sale vacio) era falso.

DE AHI SALEN LAS DOS COSAS QUE ESTE FICHERO HACE Y QUE UN `diff` pelado no hace:

  1. CUATRO VEREDICTOS SEPARADOS Y NO UNO. `FICHERO ENTERO`, `SOLO DOCSTRING`,
     `SOLO LA MAQUINA` y, desde la vuelta 178, `EL ARBOL DE SINTAXIS`. Un clon
     declarado casi nunca es identico entero (el docstring cuenta de que va la
     vuelta, y debe contarlo), asi que un unico veredicto sobre el fichero
     entero no responde la pregunta que se hace.
  2. LA CLASIFICACION DE LO QUE DIFIERA EN LA MAQUINA, en SENTENCIAS DE CODIGO
     y LITERALES DE TEXTO, que es LA DISTINCION QUE AQUI DECIDE SI UN CLON ES UN
     CLON. Cambiar el texto que un script imprime no es cambiar el script;
     cambiar una llamada, un import o una rama si lo es.

COMO CLASIFICA, Y ES MECANICO, NO A OJO: POR TOKEN Y NO POR LINEA. Se tokeniza
cada fichero y se fabrica su FLUJO DE CODIGO: la misma secuencia de tokens, con
el VALOR de cada token de texto (STRING, COMMENT y el trozo de texto de una
f-string) sustituido por la constante `<TEXTO>` y todo lo demas intacto. Los dos
flujos de codigo se cotejan, y las lineas que tocan los tokens que difieren SON
LAS SENTENCIAS DE CODIGO; las demas lineas que difieren en crudo son LITERALES
DE TEXTO.

POR QUE POR TOKEN Y NO POR LINEA, QUE ES LA VERSION QUE PROBE PRIMERO Y ESTABA
MAL. La primera version tapaba CARACTER A CARACTER dentro de la linea, y eso
conserva la LONGITUD: dos cadenas distintas quedaban como dos hileras de puntos
de distinto largo, o sea SEGUIAN DIFIRIENDO, y el instrumento clasificaba como
SENTENCIA DE CODIGO exactamente lo que venia a descartar. Corrida contra el par
que el auditor midio daba SENTENCIAS 33 y LITERALES 0, justo del reves que su
medicion. Y una cadena de varias lineas es peor todavia: si el clon la alarga o
la acorta, el conteo de LINEAS cambia y ninguna comparacion linea a linea puede
verlo como el mismo trozo de texto. POR TOKEN NO PASA NINGUNA DE LAS DOS COSAS:
una cadena de veinte lineas es UN token, y normalizada vale `<TEXTO>` a los dos
lados mida lo que mida.

EL CUARTO VEREDICTO, Y POR QUE NACE (vuelta 178, TAREA 1.c; adjudicacion del
acta 177 punto 7.7). El auditor conto A OJO las diferencias del par del acta 176
y publico SENTENCIAS DE CODIGO 0; este instrumento, corrido, dice 1. Los dos
tenian razon, y ese es justo el problema: EL INSTRUMENTO MIDE LINEAS POR RESIDUO
TEXTUAL Y SE LE PEDIA UNA CONCLUSION SOBRE COMPORTAMIENTO. La unica sentencia
que sobrevivia a tapar cadenas y comentarios era UNA COMA FINAL, que mueve un
token y no mueve nada mas.

LA CLASIFICACION VIEJA NO SE TOCA Y SIGUE PUBLICANDO SU 1. Meterle una excepcion
para comas seria decidir a ojo, dentro del instrumento, LA DISTINCION QUE AQUI
DECIDE SI UN CLON ES UN CLON. Lo que se anade es una vara distinta AL LADO: el
ARBOL DE SINTAXIS, comparado con `ast` tras la misma sustitucion de numeros de
vuelta. Nadie lo escribe a ojo, y una coma final no mueve un AST.

Y VA EN DOS MITADES, POR EL MISMO MOTIVO QUE LOS TRES DE ARRIBA: `AST DEL
FICHERO ENTERO` y `AST SIN EL DOCSTRING`. El docstring de un clon cambia
siempre, asi que un unico AST sobre el fichero entero diria DIFIERE en todos los
clones reales. Cuando difieren, se publica CUANTOS NODOS Y DE QUE TIPO, no un
DIFIERE pelado.

CAE EN ROJO SI UN FICHERO NO PARSEA, y lo dice con su linea. Es la segunda
condicion de rojo por defecto, al lado de "falta un fichero": sin arbol no hay
cuarto veredicto, y publicar tres de cuatro como si fueran cuatro seria comerse
un `SyntaxError` en silencio.

SI UN FICHERO NO SE PUEDE TOKENIZAR, LA CLASIFICACION NO SE INVENTA: se dice en
voz alta que no hay clasificacion y por que, y eso ES el resultado. Un
instrumento que se calla cuando no puede medir es peor que no tenerlo (banco 9,
fallar ruidoso).

LOS DOS NUMEROS SE SUSTITUYEN EN LOS DOS FICHEROS, y no cada uno en el suyo. Es
lo que el `diff` original decia hacer ("con todo `175` y `176` sustituido por
`NNN`") y es lo correcto: los clones se nombran entre si, asi que un fichero de
la 177 que menciona la 176 tiene que normalizarse igual que el de la 176 que
menciona su propio numero. Sustituir solo el propio dejaria diferencias de
mentira en cada referencia cruzada.

CAE EN ROJO (exit 1) SI LE FALTA UN FICHERO O SI UN FICHERO NO PARSEA, que son
sus dos condiciones de rojo por defecto: que los dos difieran NO es un fallo, es
el veredicto que se venia a buscar.

Y HAY DOS CARRILES QUE BLOQUEAN, NO UNO, PORQUE EL PRIMERO QUE ESCRIBI NO SERVIA
PARA LO QUE ESTE FICHERO EXISTE. `--exigir-maquina-identica` enrojece en cuanto
difiere UNA linea de maquina, contando las que solo cambian de texto: es el
carril ESTRICTO, y su propio caso positivo por mutacion demostro que casi ningun
clon real lo pasa, porque un clon cambia las cadenas que imprime. El carril util
es `--exigir-codigo-identico`, que enrojece solo si difiere una SENTENCIA DE
CODIGO, o sea exactamente lo que un clon declarado promete. Los dos se quedan y
cada uno dice para que es.

SUS CASOS POSITIVOS POR MUTACION SON DOS, y ninguno sustituye al otro:
`scripts/loop/vuelta177_tarea1d_mutacion_cotejo.py`, que le fabrica clones de
mentira en un directorio temporal (identicos, distintos solo en el docstring,
distintos solo en una cadena, distintos en una llamada de verdad) y exige que
los tres veredictos de lineas y la clasificacion salgan como tienen que salir en
cada uno; y `scripts/loop/vuelta178_tarea1c_mutacion_ast.py`, que prueba el
cuarto veredicto e incluye EL CASO QUE LO DECIDE TODO: dos ficheros que solo se
diferencian en UNA COMA FINAL tienen que dar maquina DIFIERE y AST IDENTICO.

A PARTIR DE LA VUELTA 178, NINGUN REPORTE ESCRIBE "CLON DECLARADO" SIN PEGAR LA
SALIDA DE ESTE FICHERO.

USO:
  python scripts/loop/cotejar_clon_declarado.py \
      --a scripts/loop/vuelta176_cierre.py --num-a 176 \
      --b scripts/loop/vuelta177_cierre.py --num-b 177

  python scripts/loop/cotejar_clon_declarado.py --a ... --b ... \
      --num-a 176 --num-b 177 --exigir-maquina-identica
"""
import argparse
import ast
import difflib
import io
import os
import sys
import tokenize

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Los tipos de token cuyo CONTENIDO es texto y no maquina. Los tres de f-string
# de Python 3.12 se piden con getattr porque en versiones anteriores no existen
# y este fichero tiene que poder correr en las dos.
TIPOS_DE_TEXTO = tuple(
    t for t in (
        tokenize.STRING,
        tokenize.COMMENT,
        getattr(tokenize, "FSTRING_MIDDLE", None),
    ) if t is not None
)


def leer(ruta):
    """El texto del fichero, normalizado a LF. None si no se puede leer."""
    if not os.path.isfile(ruta):
        return None
    return io.open(ruta, encoding="utf-8", errors="replace").read().replace(
        chr(13) + NL, NL)


def con_nnn(texto, numeros):
    """EL TEXTO CON LOS DOS NUMEROS DE VUELTA SUSTITUIDOS POR NNN. PURA.

    Los DOS numeros se sustituyen en el MISMO texto, no cada uno en su fichero:
    ver el docstring de arriba. Se sustituyen de mas largo a mas corto para que
    un numero que sea prefijo de otro no se coma al otro a medias."""
    for n in sorted({str(x) for x in numeros}, key=len, reverse=True):
        texto = texto.replace(n, "NNN")
    return texto


def flujo_de_tokens(texto, indices_doc):
    """LOS TOKENS DE LA MAQUINA, CON SUS LINEAS. Devuelve (lista, None) o
    (None, motivo). PURA: no lee ni escribe nada.

    Cada elemento es (tipo, valor, primera_linea, ultima_linea), con las lineas
    en base 1. Se DEJAN FUERA los tokens que empiezan dentro del docstring de
    modulo (que es lo que separa la maquina del docstring) y los tokens de
    andamiaje que no son ni codigo ni texto (ENCODING, ENDMARKER, NEWLINE, NL,
    INDENT y DEDENT), porque su numero cambia con el formato y no con la
    maquina."""
    fuera = {tokenize.ENCODING, tokenize.ENDMARKER, tokenize.NEWLINE,
             tokenize.NL, tokenize.INDENT, tokenize.DEDENT}
    try:
        toks = list(tokenize.generate_tokens(io.StringIO(texto).readline))
    except (tokenize.TokenError, IndentationError, SyntaxError, ValueError) as e:
        return None, "no se pudo tokenizar: %s: %s" % (type(e).__name__, e)
    salida = []
    for tk in toks:
        if tk.type in fuera:
            continue
        if (tk.start[0] - 1) in indices_doc:
            continue
        salida.append((tk.type, tk.string, tk.start[0], tk.end[0]))
    return salida, None


def normalizar(flujo):
    """EL FLUJO DE CODIGO: el mismo flujo con el VALOR de cada token de texto
    sustituido por la constante `<TEXTO>`. PURA.

    Es lo unico que separa una sentencia de un literal: si dos flujos
    normalizados son iguales, LA MAQUINA ES LA MISMA por mucho que los ficheros
    digan cosas distintas. Y una cadena de veinte lineas es UN token, asi que
    alargarla o acortarla no mueve nada aqui."""
    return [(tipo, ("<TEXTO>" if tipo in TIPOS_DE_TEXTO else valor))
            for tipo, valor, _sr, _er in flujo]


def lineas_de_tokens(flujo, indices):
    """LAS LINEAS (base 1) QUE TOCAN LOS TOKENS DE ESOS INDICES. PURA."""
    tocadas = set()
    for i in indices:
        if 0 <= i < len(flujo):
            _t, _v, sr, er = flujo[i]
            tocadas.update(range(sr, er + 1))
    return tocadas


def arbol_de_sintaxis(texto):
    """EL ARBOL DE SINTAXIS DEL TEXTO. Devuelve (arbol, None) o (None, motivo).
    PURA: no lee ni escribe nada.

    EL MOTIVO LLEVA SU LINEA SIEMPRE QUE PYTHON LA DE, y esa es la mitad del
    valor de este veredicto: un instrumento que se come un `SyntaxError` en
    silencio miente (banco 9, fallar ruidoso), y uno que lo canta sin decir
    DONDE obliga a buscarlo a mano."""
    try:
        return ast.parse(texto), None
    except (SyntaxError, ValueError) as e:
        linea = getattr(e, "lineno", None)
        return None, ("%s%s: %s"
                      % (type(e).__name__,
                         (" en la linea %d" % linea) if linea else "",
                         getattr(e, "msg", None) or e))


def sin_docstring_de_modulo(arbol):
    """EL CUERPO DEL MODULO SIN SU DOCSTRING. Devuelve un `ast.Module` nuevo.
    PURA.

    POR QUE HACE FALTA, Y NO ES UN CAPRICHO: el docstring de un clon declarado
    CAMBIA SIEMPRE, porque cuenta de que va la vuelta y debe contarlo. Un unico
    veredicto de AST sobre el fichero entero diria DIFIERE en todos los clones
    reales y no responderia la pregunta que se hace. Por eso este fichero
    publica LOS DOS arboles, el entero y el de la maquina, igual que ya publica
    el fichero entero y la maquina por separado en los tres veredictos de
    lineas."""
    cuerpo = list(arbol.body)
    if cuerpo:
        n0 = cuerpo[0]
        if (isinstance(n0, ast.Expr) and isinstance(n0.value, ast.Constant)
                and isinstance(n0.value.value, str)):
            cuerpo = cuerpo[1:]
    return ast.Module(body=cuerpo, type_ignores=list(arbol.type_ignores))


def huella_de_arbol(arbol):
    """EL VOLCADO CANONICO DEL ARBOL, SIN POSICIONES. PURA.

    `include_attributes=False` deja fuera lineas y columnas a proposito: mover
    una sentencia de linea no cambia lo que el programa hace, y este veredicto
    mide exactamente eso."""
    return ast.dump(arbol, annotate_fields=True, include_attributes=False)


def censo_de_nodos(arbol):
    """{tipo_de_nodo: cuantos}. PURA. Es lo que permite decir CUANTOS NODOS Y DE
    QUE TIPO cuando los dos arboles difieren, en vez de un DIFIERE pelado."""
    cuenta = {}
    for n in ast.walk(arbol):
        k = type(n).__name__
        cuenta[k] = cuenta.get(k, 0) + 1
    return cuenta


def diferencia_de_censos(ca, cb):
    """[(tipo, cuantos_en_a, cuantos_en_b)] SOLO de los tipos que no empatan,
    ordenado por el tamano de la diferencia. PURA."""
    tipos = set(ca) | set(cb)
    filas = [(t, ca.get(t, 0), cb.get(t, 0)) for t in tipos
             if ca.get(t, 0) != cb.get(t, 0)]
    return sorted(filas, key=lambda f: (-abs(f[1] - f[2]), f[0]))


def rango_del_docstring(texto):
    """LOS INDICES (base 0) DE LAS LINEAS DEL DOCSTRING DE MODULO, como set.

    Vacio si el modulo no tiene docstring. Devuelve (set, None) o (None, motivo)
    si el fichero no es Python parseable. PURA."""
    try:
        arbol = ast.parse(texto)
    except (SyntaxError, ValueError) as e:
        return None, "no se pudo parsear: %s: %s" % (type(e).__name__, e)
    if not arbol.body:
        return set(), None
    n0 = arbol.body[0]
    es_doc = (isinstance(n0, ast.Expr) and isinstance(n0.value, ast.Constant)
              and isinstance(n0.value.value, str))
    if not es_doc:
        return set(), None
    return set(range(n0.lineno - 1, (n0.end_lineno or n0.lineno))), None


def partir(lineas, indices_doc):
    """(docstring, maquina) como listas de (numero_de_linea, texto). PURA."""
    doc, maq = [], []
    for i, l in enumerate(lineas):
        (doc if i in indices_doc else maq).append((i + 1, l))
    return doc, maq


def indices_que_difieren(a, b):
    """LOS INDICES DE CADA LADO QUE DIFIEREN, como (set_a, set_b). PURA.

    `a` y `b` son listas de cadenas. Se usa SequenceMatcher y se toman los
    tramos `replace`, `delete` e `insert`: lo que queda fuera de `equal`."""
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    ia, ib = set(), set()
    for etiqueta, i1, i2, j1, j2 in sm.get_opcodes():
        if etiqueta == "equal":
            continue
        ia.update(range(i1, i2))
        ib.update(range(j1, j2))
    return ia, ib


def cotejar(texto_a, texto_b, numeros):
    """EL COTEJO ENTERO, PURO. Devuelve un dict con los tres veredictos y la
    clasificacion. No lee ni escribe nada: recibe los dos textos ya leidos.

    Que sea pura es lo que permite que su caso positivo por mutacion le fabrique
    clones de mentira en memoria y compruebe cada veredicto sin tocar el repo."""
    na = con_nnn(texto_a, numeros)
    nb = con_nnn(texto_b, numeros)

    r = {"entero_identico": (na == nb), "motivos": []}

    la, lb = na.split(NL), nb.split(NL)
    doc_a, mot_a = rango_del_docstring(na)
    doc_b, mot_b = rango_del_docstring(nb)
    if mot_a:
        r["motivos"].append("A: " + mot_a)
    if mot_b:
        r["motivos"].append("B: " + mot_b)
    doc_a = doc_a if doc_a is not None else set()
    doc_b = doc_b if doc_b is not None else set()

    da, ma = partir(la, doc_a)
    db, mb = partir(lb, doc_b)
    r["lineas_doc_a"], r["lineas_doc_b"] = len(da), len(db)
    r["lineas_maquina_a"], r["lineas_maquina_b"] = len(ma), len(mb)

    r["docstring_identico"] = ([t for _n, t in da] == [t for _n, t in db])
    r["maquina_identica"] = ([t for _n, t in ma] == [t for _n, t in mb])

    # EL CUARTO VEREDICTO: EL ARBOL DE SINTAXIS (vuelta 178, TAREA 1.c;
    # adjudicacion del acta 177 punto 7.7). Los tres de arriba miden LINEAS y
    # TOKENS, y a una conclusion sobre COMPORTAMIENTO le falta una vara que no
    # dependa del formato. Una coma final mueve un token y NO mueve un AST.
    aa, mot_aa = arbol_de_sintaxis(na)
    ab, mot_ab = arbol_de_sintaxis(nb)
    r["ast_no_parsea"] = ([("A", mot_aa)] if mot_aa else []) + \
                         ([("B", mot_ab)] if mot_ab else [])
    if aa is None or ab is None:
        r["ast_hay"] = False
        r["ast_identico_entero"] = None
        r["ast_identico_maquina"] = None
        r["ast_censo_distinto"] = []
        r["ast_nodos_a"], r["ast_nodos_b"] = None, None
    else:
        r["ast_hay"] = True
        r["ast_identico_entero"] = (huella_de_arbol(aa) == huella_de_arbol(ab))
        sa, sb = sin_docstring_de_modulo(aa), sin_docstring_de_modulo(ab)
        r["ast_identico_maquina"] = (huella_de_arbol(sa) == huella_de_arbol(sb))
        censo_a, censo_b = censo_de_nodos(sa), censo_de_nodos(sb)
        r["ast_nodos_a"] = sum(censo_a.values())
        r["ast_nodos_b"] = sum(censo_b.values())
        r["ast_censo_distinto"] = diferencia_de_censos(censo_a, censo_b)

    # EL DIFF CRUDO DE LA MAQUINA
    ia, ib = indices_que_difieren([t for _n, t in ma], [t for _n, t in mb])
    r["maquina_difieren_a"] = sorted(ia)
    r["maquina_difieren_b"] = sorted(ib)
    r["n_maquina_difieren"] = len(ia) + len(ib)

    # LA CLASIFICACION, POR TOKEN Y NO POR LINEA (ver el docstring de arriba)
    fa, mot_fa = flujo_de_tokens(na, doc_a)
    fb, mot_fb = flujo_de_tokens(nb, doc_b)
    if mot_fa:
        r["motivos"].append("A: " + mot_fa)
    if mot_fb:
        r["motivos"].append("B: " + mot_fb)

    if fa is None or fb is None:
        r["clasifica"] = False
        r["sentencias"], r["literales"] = [], []
        r["codigo_identico"] = None
        return r

    ja, jb = indices_que_difieren(normalizar(fa), normalizar(fb))
    r["clasifica"] = True
    # EL VEREDICTO DE FONDO, que es el que la frase del clon queria decir:
    # ningun token de codigo difiere, o sea LA MAQUINA ES LA MISMA aunque el
    # texto que imprime no lo sea.
    r["codigo_identico"] = (not ja and not jb)
    r["n_tokens_codigo_a"], r["n_tokens_codigo_b"] = len(fa), len(fb)
    r["n_tokens_que_difieren"] = len(ja) + len(jb)

    sent_a = lineas_de_tokens(fa, ja)
    sent_b = lineas_de_tokens(fb, jb)
    r["sentencias"] = ([("A", ma[i][0], ma[i][1]) for i in sorted(ia)
                        if ma[i][0] in sent_a]
                       + [("B", mb[i][0], mb[i][1]) for i in sorted(ib)
                          if mb[i][0] in sent_b])
    r["literales"] = ([("A", ma[i][0], ma[i][1]) for i in sorted(ia)
                       if ma[i][0] not in sent_a]
                      + [("B", mb[i][0], mb[i][1]) for i in sorted(ib)
                         if mb[i][0] not in sent_b])
    return r


def imprimir(r, ruta_a, ruta_b, numeros):
    p = print
    p("=" * 78)
    p("COTEJO DE CLON DECLARADO")
    p("=" * 78)
    p("  A: %s" % ruta_a)
    p("  B: %s" % ruta_b)
    p("  numeros de vuelta sustituidos por NNN EN LOS DOS FICHEROS: %s"
      % ", ".join(str(n) for n in numeros))
    p("  CIFRA lineas de docstring: A %d | B %d" % (r["lineas_doc_a"], r["lineas_doc_b"]))
    p("  CIFRA lineas de maquina:   A %d | B %d"
      % (r["lineas_maquina_a"], r["lineas_maquina_b"]))
    p("")
    p("LOS CUATRO VEREDICTOS, SEPARADOS Y NO UNO")
    p("  1) FICHERO ENTERO  : %s" % ("IDENTICO" if r["entero_identico"] else "DIFIERE"))
    p("  2) SOLO DOCSTRING  : %s" % ("IDENTICO" if r["docstring_identico"] else "DIFIERE"))
    p("  3) SOLO LA MAQUINA : %s" % ("IDENTICO" if r["maquina_identica"] else "DIFIERE"))
    p("  4) EL ARBOL DE SINTAXIS (vuelta 178, TAREA 1.c). Los tres de arriba miden")
    p("     LINEAS y TOKENS; este mide EL ARBOL, que es la vara de 'cambia lo que")
    p("     el programa hace'. Una coma final mueve un token y NO mueve un AST.")
    if not r.get("ast_hay"):
        p("     NO HAY VEREDICTO DE AST, y se dice en vez de inventarlo:")
        for lado, motivo in r.get("ast_no_parsea") or []:
            p("        %s: %s" % (lado, motivo))
        p("     UN FICHERO QUE NO PARSEA ES ROJO EN ESTE INSTRUMENTO.")
    else:
        p("     4.a) AST DEL FICHERO ENTERO   : %s"
          % ("IDENTICO" if r["ast_identico_entero"] else "DIFIERE"))
        p("     4.b) AST SIN EL DOCSTRING     : %s"
          % ("IDENTICO" if r["ast_identico_maquina"] else "DIFIERE"))
        p("     CIFRA nodos del arbol sin docstring: A %d | B %d"
          % (r["ast_nodos_a"], r["ast_nodos_b"]))
        if r["ast_identico_maquina"]:
            p("     LOS DOS ARBOLES SON EL MISMO ARBOL. Lo que difiera en lineas o")
            p("     en tokens NO CAMBIA LO QUE EL PROGRAMA HACE.")
        else:
            filas = r["ast_censo_distinto"]
            p("     CIFRA tipos de nodo que NO empatan: %d" % len(filas))
            for tipo, na_, nb_ in filas:
                p("        %-22s A %5d | B %5d | diferencia %+d"
                  % (tipo, na_, nb_, nb_ - na_))
            if not filas:
                p("        (ninguno: los censos por tipo empatan y aun asi los")
                p("        arboles difieren, o sea que lo que cambia es el VALOR de")
                p("        algun nodo y no cuantos hay)")
    p("")
    if r["maquina_identica"]:
        p("LA MAQUINA NO CAMBIA EN NADA, Y ESTA MEDIDO Y NO AFIRMADO.")
        p("  CIFRA lineas de maquina que difieren: 0")
        p("")
        return
    p("LA MAQUINA DIFIERE. LA CLASIFICACION, QUE ES LO QUE DECIDE SI ES UN CLON")
    p("  CIFRA lineas de maquina que difieren: %d" % r["n_maquina_difieren"])
    if r.get("clasifica"):
        p("  CIFRA tokens de maquina: A %d | B %d"
          % (r["n_tokens_codigo_a"], r["n_tokens_codigo_b"]))
        p("  CIFRA tokens que difieren con el texto normalizado: %d"
          % r["n_tokens_que_difieren"])
        p("  EL FLUJO DE CODIGO ES EL MISMO (la maquina no cambia): %s"
          % ("SI" if r["codigo_identico"] else "NO"))
    if not r["clasifica"]:
        p("  NO HAY CLASIFICACION, y se dice en vez de inventarla:")
        for m in r["motivos"]:
            p("     %s" % m)
        p("")
        return
    p("  CIFRA SENTENCIAS DE CODIGO: %d" % len(r["sentencias"]))
    p("  CIFRA LITERALES DE TEXTO:   %d" % len(r["literales"]))
    p("")
    p("  LAS SENTENCIAS DE CODIGO, UNA A UNA (lo que sobrevive a tapar cadenas")
    p("  y comentarios, o sea lo que de verdad cambia la maquina):")
    if not r["sentencias"]:
        p("     (ninguna)")
    for lado, n, t in r["sentencias"]:
        p("     %s:%d  %s" % (lado, n, t.strip()[:110]))
    p("")
    p("  LOS LITERALES DE TEXTO, UNA A UNA (lo que desaparece al tapar cadenas y")
    p("  comentarios, o sea lo que solo cambia lo que el fichero DICE):")
    if not r["literales"]:
        p("     (ninguno)")
    for lado, n, t in r["literales"]:
        p("     %s:%d  %s" % (lado, n, t.strip()[:110]))
    p("")
    for m in r["motivos"]:
        p("  DECLARADO: %s" % m)
    p("")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", required=True, help="el fichero del que se clono")
    ap.add_argument("--b", required=True, help="el clon")
    ap.add_argument("--num-a", dest="num_a", type=int, required=True)
    ap.add_argument("--num-b", dest="num_b", type=int, required=True)
    ap.add_argument("--exigir-maquina-identica", dest="exigir",
                    action="store_true",
                    help="extiende el rojo a que difiera UNA SOLA LINEA de la "
                         "maquina, contando las que solo cambian de texto. Es el "
                         "carril ESTRICTO y casi ningun clon real lo pasa.")
    ap.add_argument("--exigir-codigo-identico", dest="exigir_codigo",
                    action="store_true",
                    help="extiende el rojo a que difiera una SENTENCIA DE CODIGO, "
                         "dejando pasar las lineas que solo cambian de texto. ES "
                         "EL CARRIL UTIL: es lo que un clon declarado promete.")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    ta, tb = leer(a.a), leer(a.b)
    faltan = [r for r, t in ((a.a, ta), (a.b, tb)) if t is None]
    if faltan:
        print("=" * 78)
        print("COTEJO DE CLON DECLARADO")
        print("=" * 78)
        print("ROJO: falta(n) %d fichero(s) y sin los dos no hay cotejo que hacer."
              % len(faltan))
        for r in faltan:
            print("   NO EXISTE O NO SE PUEDE LEER: %s" % r)
        return 1

    r = cotejar(ta, tb, (a.num_a, a.num_b))
    imprimir(r, a.a, a.b, (a.num_a, a.num_b))

    # ROJO SI UN FICHERO NO PARSEA (vuelta 178, TAREA 1.c). Es la segunda
    # condicion de rojo por defecto de este instrumento, al lado de "falta un
    # fichero", y por el mismo motivo: sin poder construir el arbol NO HAY
    # CUARTO VEREDICTO, y un instrumento que se come un SyntaxError en silencio
    # publica tres veredictos de cuatro como si fueran los cuatro.
    if r.get("ast_no_parsea"):
        print("ROJO: %d fichero(s) no parsean y sin arbol no hay cuarto veredicto."
              % len(r["ast_no_parsea"]))
        for lado, motivo in r["ast_no_parsea"]:
            print("   %s: %s" % (lado, motivo))
        return 1

    if a.exigir and not r["maquina_identica"]:
        print("ROJO POR --exigir-maquina-identica: la maquina difiere en %d linea(s)."
              % r["n_maquina_difieren"])
        return 1
    if a.exigir_codigo:
        if not r.get("clasifica"):
            print("ROJO POR --exigir-codigo-identico: no se pudo clasificar, y una")
            print("      clasificacion que no se pudo hacer no se da por buena.")
            return 1
        if not r["codigo_identico"]:
            print("ROJO POR --exigir-codigo-identico: difieren %d SENTENCIA(S) DE "
                  "CODIGO." % len(r["sentencias"]))
            return 1
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
