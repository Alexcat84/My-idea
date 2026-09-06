# -*- coding: utf-8 -*-
r"""vuelta190_tarea1a_registrar_acta190.py . EL ACTA 190 ENTERA, REGISTRADA EN LA
SERIE `R.N` EN LA FORMA DE LA CASA, Y ESTE REGISTRADOR SIGUE SIENDO IDEMPOTENTE.

LA MAQUINA NO SE CLONA, SE IMPORTA, y eso lo adjudico la `6.6` del acta 172 como
correcto y obligatorio. De la cadena de registradores se importan
`titulo_de_la_negrita`, `claves_de_adjudicacion`, `claves_entrecomilladas`,
`cuenta_por_patron`, `actas_sin_entrada`, `PALABRA_CON_CERO`,
`seccion_que_contiene`, los patrones de caida, y **la idempotencia entera**
(`marcas_del_acta` y `entradas_que_registran` del registrador de la 189, que es
donde nacieron y donde el auditor las probo re corriendolas).

**LO PROPIO DE ESTE FICHERO SON LAS CUATRO COSAS QUE EL ACTA 190 ESTRENA**, y las
cuatro salen de correr la maquinaria heredada sobre el acta 190, no de suponerlas:

  1) HAY UNA ADJUDICACION **EN CONTRA**, Y EL VOCABULARIO HEREDADO NO SABE LEERLA.
     `estado_de_la_adjudicacion()` del registrador de la 189 conoce cinco marcas
     y **ninguna es `EN CONTRA`**: corrida sobre el titulo de la `4.6` del acta
     190 devolveria `SIN DECIR` y este instrumento haria PARADA. Peor todavia
     seria heredar su regla de cuenta: la 189 **PARABA si algun discutible no
     llevaba `A FAVOR`**, porque las seis de aquella acta lo llevaban. **Hoy son
     seis discutibles y solo CINCO van a favor.** Aqui la marca `EN CONTRA`
     EXISTE, se busca ANTES que `A FAVOR`, y **las dos cifras se publican por
     separado**. Su caso positivo por mutacion fabrica un acta con un `EN CONTRA`
     y exige que la cuenta lo vea; y muta el esperado a "todas a favor" y exige
     que CAIGA.

  2) LA SECCION 6 NO DICE DE QUIEN SON LAS CAIDAS EN SU CABECERA, Y LAS ESCRIBE
     EN LINEA. La cabecera del acta 190 es `## 6. LAS CAIDAS`, a secas: no dice
     `MIAS`, no dice `LAS SUYAS`, no dice `CERO SON DEL EJECUTOR`. Corrido sobre
     ella, `caidas_por_seccion()` de la 189 sacaria **todas huerfanas** y este
     instrumento haria PARADA. Y hay una segunda razon medida: **el patron `C.n`
     de cabeza de linea da CERO sobre el acta 190**, porque sus tres caidas van
     **dentro de un parrafo**, entre parentesis. Aqui la atribucion la hace **LA
     NEGRITA QUE ABRE EL PARRAFO** (`DEL EJECUTOR: ...` frente a `MIAS: ...`), y
     las `C.n` se buscan **en linea**. **La PARADA se conserva entera:** una `C.n`
     en un parrafo cuya negrita no diga ni una cosa ni la otra sale huerfana y
     sigue parando.

  3) UN CERO DE RACHA NO ES UN CERO DE CUENTA, Y CONFUNDIRLOS SERIA PERDER TRES
     CAIDAS. El acta 189 traia `CERO SON DEL EJECUTOR`, que es un cero de CUENTA:
     no hay ninguna. El acta 190 trae `DEL EJECUTOR: CERO QUE ACUMULEN`, y **en
     ese mismo parrafo declara TRES**. Si la marca de cero neutralizadora que la
     `4.1` adjudico se aplicara aqui tal cual, **las tres caidas del ejecutor
     desaparecerian de la cuenta**. Por eso este fichero separa las dos especies
     de cero con sus dos literales, y **el de racha NO neutraliza la atribucion**.
     Probado por mutacion en los dos sentidos.

  4) LOS HALLAZGOS DE LA SECCION 5 SON CUATRO Y SOLO DOS SON "FUERA DEL MARCADO".
     El encargo nombra dos (`5.1` y `5.2`) y la seccion tiene **cuatro** claves
     `5.n`. **Cual de las cuatro cuenta como hallazgo fuera del marcado NO SE
     TECLEA:** sale de la fila `discrepancias y hallazgos FUERA del marcado` de la
     tabla de credito del propio acta, cuyo parentesis se parte por `;`, se
     normaliza, y se busca dentro del titulo literal de cada `5.n`. Las cuatro se
     publican con su titulo; **las que la tabla nombra van marcadas como tales**.

LA PARADA SE CONSERVA ENTERA: un estado, una atribucion o una cuenta que este
registrador no sepa leer sigue siendo PARADA, y no se resuelve a ojo.

LO QUE ESTE FICHERO NO HACE: no toca el acta, no toca el reporte, no toca
`docs/plan/` salvo para LEER, no corre la bateria, no toca la guarda del sujeto
congelado y no escribe ningun veredicto. Escribe UNA entrada en UNA sede, y si el
acta ya esta registrada, NO escribe nada.

USO:
  python scripts/loop/vuelta190_tarea1a_registrar_acta190.py
  python scripts/loop/vuelta190_tarea1a_registrar_acta190.py --simular
  python scripts/loop/vuelta190_tarea1a_registrar_acta190.py --mutacion
"""
import argparse
import io
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import serie_de_registros as SERIE   # noqa: E402
from vuelta172_tarea1_registrar_acta171 import titulo_de_la_negrita   # noqa: E402
from vuelta182_tarea1a_registrar_acta181 import (   # noqa: E402
    claves_de_adjudicacion, cuenta_por_patron)
from vuelta183_tarea1a_registrar_acta182 import actas_sin_entrada   # noqa: E402
from vuelta184_tarea1a_registrar_acta184 import claves_entrecomilladas   # noqa: E402
from vuelta186_tarea1a_registrar_acta186 import (   # noqa: E402
    PALABRA_CON_CERO, PAT_CAIDA_AUDITOR_A, PAT_CAIDA_EJECUTOR_VIEJO,
    PAT_CAIDA_REPORTE, PAT_P_DEL_TITULO)
from vuelta187_tarea1a_registrar_acta187 import (   # noqa: E402
    PAT_CAIDA_C, seccion_que_contiene)
from vuelta188_tarea1a_registrar_acta188 import PAT_CAIDA_C_ESPACIO   # noqa: E402
from vuelta189_tarea1a_registrar_acta189 import (   # noqa: E402
    marcas_del_acta, entradas_que_registran, caidas_por_seccion,
    MARCAS_CERO_EJECUTOR)

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")
SEDE = os.path.join(RAIZ, "docs", "PENDIENTES.md")
NL = chr(10)

VUELTA_DEL_ACTA = 190
VUELTA_QUE_ESCRIBE = 190
SUFIJO_QUE_ESCRIBE = "190"
CABECERA_ACTA = "# ACTA DEL AUDITOR, VUELTA %d" % VUELTA_DEL_ACTA
# LA SECCION DE LAS ADJUDICACIONES ES LA 4, COMO EN EL ACTA 189, Y SE DECLARA EN
# VEZ DE HEREDARSE: el patron entrecomillado de la 188 se corre al lado y su
# cifra se publica.
PREFIJO_ADJ = "4."
PREFIJO_HALLAZGO = "5."
SECCION_DE_LOS_HALLAZGOS = 5
SECCION_DE_LAS_CAIDAS = 6

# LAS MARCAS DE ESTADO DE UNA ADJUDICACION, LEIDAS DEL TITULO LITERAL. Ninguna se
# ensancha: se buscan tal cual y EN ESTE ORDEN. `EN CONTRA` va PRIMERA a
# proposito: un titulo que tumbara algo y a la vez dijera `A FAVOR` de otra cosa
# tiene que salir EN CONTRA, porque tumbar es el hecho que cambia el trabajo.
MARCA_EN_CONTRA = "EN CONTRA"
MARCA_A_FAVOR = "A FAVOR"
MARCA_CUENTA_COMO_CORRIDO = "CUENTA COMO CORRIDO"
MARCA_PRIMERO_SE_MIDE = "PERO PRIMERO SE MIDE"
MARCA_SE_RESTAURA = "SE RESTAURA SIEMPRE"
MARCA_CADUCA = "SE CUMPLIO Y CADUCA"

# EL VOCABULARIO DE LA ATRIBUCION DE ESTA ACTA, LITERAL DE SU SECCION 6 Y SIN
# PARAFRASEAR. NO son cabeceras de seccion: son LAS NEGRITAS QUE ABREN CADA
# PARRAFO, porque `## 6. LAS CAIDAS` no dice de quien son.
MARCAS_LEAD_EJECUTOR = ("DEL EJECUTOR",)
MARCAS_LEAD_AUDITOR = ("MIAS",)
# EL CERO DE CUENTA (el del acta 189) NEUTRALIZA LA ATRIBUCION: una cabecera que
# dice que del ejecutor hay CERO no le esta atribuyendo ninguna caida. Se importa
# tal cual de la 189 y NO se toca.
MARCAS_CERO_DE_CUENTA = tuple(MARCAS_CERO_EJECUTOR)
# EL CERO DE RACHA NO NEUTRALIZA NADA, Y ESA ES LA DISTINCION QUE ESTA VUELTA
# ESTRENA. `DEL EJECUTOR: CERO QUE ACUMULEN` declara cero caidas QUE ABRAN RACHA
# y en el mismo parrafo declara TRES caidas. Tratarlo como cero de cuenta
# borraria las tres.
MARCAS_CERO_DE_RACHA = ("CERO QUE ACUMULEN",)
# LAS FRASES LITERALES DEL CERO, PARA QUE NINGUN CERO SE PUBLIQUE DESNUDO.
FRASE_CERO_AUDITOR = "MIAS: CERO"
FRASE_CERO_RACHA_EJECUTOR = "DEL EJECUTOR: CERO QUE ACUMULEN"
# LA ESPECIE, LITERAL DEL PARRAFO.
MARCA_ESPECIE_METODO = "SON DE METODO"

# LAS `C.n` EN LINEA, ENTRECOMILLADAS CON COMILLA INVERSA, QUE ES COMO EL ACTA
# 190 LAS ESCRIBE. El patron de cabeza de linea de las actas 187 y 188 se corre
# igual y SU CIFRA SE PUBLICA, que hoy es cero.
PAT_C_EN_LINEA = re.compile(r"`C\.(\d+)`")
# LA FILA DE LA TABLA DE CREDITO QUE DICE CUALES HALLAZGOS CUENTAN FUERA.
AGUJA_FILA_FUERA = "discrepancias y hallazgos FUERA del marcado"
AGUJA_FILA_CAIDAS_AUDITOR = "caidas propias del auditor"
AGUJA_FILA_CAIDAS_METODO = "caidas del ejecutor de metodo"


def cuerpo_del_acta(texto=None, cabecera=None):
    """EL ACTA ACOTADA: (lineas, (inicio, fin), error). PURA cuando se le pasan
    `texto` y `cabecera`.

    CLON DECLARADO del de la 189, con su misma diferencia declarada: la cabecera
    es PARAMETRO y no constante de modulo, para que el caso positivo por mutacion
    pueda acotar actas FABRICADAS sin parchear este modulo."""
    cab = cabecera if cabecera is not None else CABECERA_ACTA
    if texto is None:
        texto = io.open(ACTA, encoding="utf-8").read()
    texto = texto.replace(chr(13) + NL, NL)
    lineas = texto.split(NL)
    cabeceras = [i for i, l in enumerate(lineas, 1)
                 if l.startswith("# ACTA DEL AUDITOR, VUELTA ")]
    mias = [i for i in cabeceras if lineas[i - 1].startswith(cab)]
    if len(mias) != 1:
        return None, None, "PARADA: %r aparece %d veces." % (cab, len(mias))
    inicio = mias[0]
    posteriores = [i for i in cabeceras if i > inicio]
    fin = (min(posteriores) - 1) if posteriores else len(lineas)
    return lineas, (inicio, fin), None


def rango_de_seccion(lineas, inicio, fin, numero):
    """(ini, fin) DE LA SECCION `## numero.` DENTRO DEL ACTA ACOTADA, o None.
    PURA."""
    ini = None
    for i in range(inicio, fin + 1):
        if re.match(r"^## %d\." % numero, lineas[i - 1]):
            ini = i
            break
    if ini is None:
        return None
    tope = fin
    for i in range(ini + 1, fin + 1):
        if lineas[i - 1].startswith("## "):
            tope = i - 1
            break
    return (ini, tope)


def parrafos_con_negrita(lineas, ini, fin):
    """LOS PARRAFOS DE UN TRAMO, CON LA NEGRITA QUE LOS ABRE. PURA.

    Devuelve [(linea_de_inicio, linea_de_fin, negrita, texto_del_parrafo)]. La
    negrita es lo que va entre el primer par de `**` cuando el parrafo EMPIEZA
    por `**`; si no empieza por negrita, la negrita sale vacia y quien llame
    decide (aqui: huerfana).

    POR QUE HACE FALTA: la seccion 6 del acta 190 no dice de quien son sus caidas
    en la cabecera, sino en la negrita que abre cada parrafo. Sin esto la
    atribucion habria que hacerla a ojo, y eso es exactamente lo que la casa
    prohibe."""
    salida = []
    bloque = []
    ini_bloque = None
    for i in range(ini, fin + 1):
        l = lineas[i - 1]
        if l.strip() == "":
            if bloque:
                salida.append((ini_bloque, i - 1, bloque))
                bloque = []
                ini_bloque = None
            continue
        if not bloque:
            ini_bloque = i
        bloque.append(l)
    if bloque:
        salida.append((ini_bloque, fin, bloque))
    hechos = []
    for a, b, ls in salida:
        texto = " ".join(x.strip() for x in ls)
        negrita = ""
        if texto.startswith("**"):
            cierre = texto.find("**", 2)
            if cierre > 0:
                negrita = re.sub(r"\s+", " ", texto[2:cierre]).strip()
        hechos.append((a, b, negrita, texto))
    return hechos


def caidas_en_linea(lineas, ini, fin, marcas_eje=None, marcas_aud=None,
                    marcas_cero_cuenta=None, marcas_cero_racha=None):
    """LAS CAIDAS `C.n` ESCRITAS EN LINEA, REPARTIDAS POR LA NEGRITA QUE ABRE SU
    PARRAFO. Devuelve (del_ejecutor, del_auditor, huerfanas). PURA.

    Cada elemento es (linea_del_parrafo, numero, negrita).

    LOS CUATRO VOCABULARIOS SON PARAMETRO, no constantes escondidas, para que el
    caso positivo por mutacion pueda correr cada variante sobre el MISMO texto y
    publicar las dos cifras.

    LAS DOS ESPECIES DE CERO, Y ES LO QUE ESTA VUELTA ESTRENA:

      . `marcas_cero_cuenta` (el `CERO SON DEL EJECUTOR` del acta 189) SI
        neutraliza: una negrita que declara cero caidas del ejecutor no le
        atribuye ninguna, y esa es la `4.1` que el acta 190 adjudico a favor.
      . `marcas_cero_racha` (el `CERO QUE ACUMULEN` del acta 190) NO neutraliza
        nada: declara cero caidas QUE ABRAN RACHA, y en el mismo parrafo el acta
        190 declara TRES. Confundirlas borraria las tres de la cuenta.

    UNA `C.n` EN UN PARRAFO CUYA NEGRITA NO DIGA NI UNA COSA NI LA OTRA SALE
    HUERFANA, y quien llama hace PARADA. Repartir a ojo una caida sin dueno es
    exactamente lo que esta funcion existe para impedir."""
    m_eje = tuple(marcas_eje) if marcas_eje is not None else MARCAS_LEAD_EJECUTOR
    m_aud = tuple(marcas_aud) if marcas_aud is not None else MARCAS_LEAD_AUDITOR
    m_cc = (tuple(marcas_cero_cuenta) if marcas_cero_cuenta is not None
            else MARCAS_CERO_DE_CUENTA)
    m_cr = (tuple(marcas_cero_racha) if marcas_cero_racha is not None
            else MARCAS_CERO_DE_RACHA)
    eje, aud, huerfanas = [], [], []
    for a, _b, negrita, texto in parrafos_con_negrita(lineas, ini, fin):
        nums = sorted(set(int(x) for x in PAT_C_EN_LINEA.findall(texto)))
        if not nums:
            continue
        alta = negrita.upper()
        es_cero_de_cuenta = any(x in alta for x in m_cc)
        # EL CERO DE RACHA SE MIDE Y SE PUBLICA, PERO NO DECIDE NADA AQUI: se
        # nombra en la variable para que se vea que se miro y se descarto a
        # proposito, y no porque nadie pensara en el.
        _es_cero_de_racha = any(x in alta for x in m_cr)
        if any(x in alta for x in m_eje) and not es_cero_de_cuenta:
            destino = eje
        elif any(x in alta for x in m_aud):
            destino = aud
        else:
            destino = huerfanas
        for n in nums:
            destino.append((a, n, negrita))
    return eje, aud, huerfanas


def estado_de_la_adjudicacion(titulo):
    """EL ESTADO DE UNA ADJUDICACION, LEIDO DE SU TITULO LITERAL. PURA.

    NO SE TECLEA NINGUNO: se busca en el titulo, EN ESTE ORDEN, `EN CONTRA`,
    `A FAVOR`, `CUENTA COMO CORRIDO`, `PERO PRIMERO SE MIDE`, `SE RESTAURA
    SIEMPRE` y `SE CUMPLIO Y CADUCA`. **Si un titulo no dijera ninguna de las
    seis, el estado sale `SIN DECIR` y quien llama hace PARADA en vez de
    suponer.**

    `EN CONTRA` VA LA PRIMERA A PROPOSITO. Es la marca que esta acta estrena y la
    que cambia el trabajo: un titulo que tumbara una cosa y adjudicara a favor de
    otra tiene que salir EN CONTRA, porque lo que hay que hacer sale de lo que se
    tumba."""
    alto = titulo.upper()
    if MARCA_EN_CONTRA in alto:
        return "EN CONTRA"
    if MARCA_A_FAVOR in alto:
        return "A FAVOR"
    if MARCA_CUENTA_COMO_CORRIDO in alto:
        return "CONTESTADA Y ENCARGADA"
    if MARCA_PRIMERO_SE_MIDE in alto:
        return "CONTESTADA Y ENCARGADA CON MEDICION PREVIA"
    if MARCA_SE_RESTAURA in alto:
        return "CONTESTADA Y ENCARGADA"
    if MARCA_CADUCA in alto:
        return "REGLA CUMPLIDA QUE CADUCA"
    return "SIN DECIR"


def familia_de_la_adjudicacion(titulo):
    """SI UNA ADJUDICACION ES UN DISCUTIBLE, UNA PREGUNTA O NINGUNA DE LAS DOS.
    PURA. NO SE TECLEA: sale de que su titulo nombre un `D.n` o un `P.n`."""
    if PAT_P_DEL_TITULO.search(titulo):
        return "PREGUNTA"
    if re.search(r"`D\.(\d+)`", titulo):
        return "DISCUTIBLE"
    return "OTRA"


def _normalizar(texto):
    """MINUSCULAS, SIN TILDES, SIN COMILLAS INVERSAS Y CON UN SOLO ESPACIO. PURA.
    Es lo que permite cotejar el parentesis de una fila de tabla contra el titulo
    de un hallazgo sin que una tilde o una comilla decida la cuenta."""
    t = unicodedata.normalize("NFD", texto)
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    t = t.replace("`", " ").replace("*", " ").lower()
    return re.sub(r"[^a-z0-9 ]+", " ", re.sub(r"\s+", " ", t)).strip()


def piezas_de_la_fila(texto_de_la_fila):
    """LOS TROZOS DEL PARENTESIS DE UNA FILA DE LA TABLA DE CREDITO. PURA.

    Devuelve la lista de piezas normalizadas, partiendo por `;` lo que va dentro
    del ULTIMO parentesis de la celda. Los articulos de cabeza (`las`, `los`,
    `la`, `el`) se quitan, porque el titulo del hallazgo no los repite."""
    m = re.findall(r"\(([^)]*)\)", texto_de_la_fila)
    if not m:
        return []
    piezas = []
    for trozo in m[-1].split(";"):
        p = _normalizar(trozo)
        p = re.sub(r"^(las|los|la|el) ", "", p)
        if p:
            piezas.append(p)
    return piezas


def hallazgos_que_la_tabla_nombra(hallazgos, texto_de_la_fila):
    """CUALES `5.n` NOMBRA LA FILA `hallazgos FUERA del marcado`. PURA.

    Devuelve (nombrados, no_nombrados, piezas). `hallazgos` es
    [(clave, linea, titulo)]. El cotejo es: la pieza normalizada del parentesis
    aparece DENTRO del titulo normalizado del hallazgo.

    **CUAL CUENTA NO SE TECLEA.** El encargo nombra dos y la seccion tiene
    cuatro; quien decide es la tabla del propio acta, que es un fichero que se
    cuenta, no un recuerdo."""
    piezas = piezas_de_la_fila(texto_de_la_fila)
    nombrados, sueltos = [], []
    for clave, ln, tit in hallazgos:
        t = _normalizar(tit)
        casan = [p for p in piezas if p in t]
        if casan:
            nombrados.append((clave, ln, tit, casan))
        else:
            sueltos.append((clave, ln, tit))
    return nombrados, sueltos, piezas


def fila_de_la_metrica(lineas, inicio, fin, aguja):
    """UNA FILA DE LA TABLA DE CREDITO DEL ACTA, LEIDA POR SU PRIMERA CELDA.
    Devuelve [(linea, texto)]. PURA."""
    return [(i, lineas[i - 1].strip())
            for i in range(inicio, fin + 1)
            if lineas[i - 1].strip().startswith("| " + aguja)]


def cifras_de_la_vara(texto_del_parrafo):
    """LAS CIFRAS DE LA VARA DE LA `5.4`, LEIDAS DE SU PARRAFO. PURA.

    Devuelve un diccionario {etiqueta: numero_o_None}. Cada etiqueta lleva su
    patron literal al lado, y la que no case sale `None`: **una cifra que no se
    puede leer no se inventa**."""
    t = re.sub(r"\s+", " ", texto_del_parrafo)
    patrones = (
        ("fichas", r"(\d+)\s*\*?\*?\s*fichas"),
        ("que no calzan", r"(\d+) que no calzan"),
        ("en LISTA sin ninguna prueba", r"(\d+) en LISTA sin ninguna prueba"),
        ("CONSUMIDAS por OP-U-01", r"(\d+) estan\s+CONSUMIDAS"),
        ("de TRABAJO REAL", r"(\d+) son TRABAJO REAL"),
        ("mesas con producto en disco", r"(\d+) son mesas"),
        ("menciones de fichero de OP-L-02", r"\((\d+) menciones de fichero"),
    )
    salida = []
    for etiqueta, pat in patrones:
        m = re.search(pat, t)
        salida.append((etiqueta, int(m.group(1)) if m else None, pat))
    return salida


def secciones_del_acta(lineas, inicio, fin):
    """LOS NUMEROS DE LAS SECCIONES `## n.` DEL ACTA, EN ORDEN Y SIN REPETIR.
    PURA. La lista de secciones de la cabecera de la entrada NO se teclea."""
    nums = []
    for i in range(inicio, fin + 1):
        m = re.match(r"^## (\d+)\.", lineas[i - 1])
        if m and int(m.group(1)) not in nums:
            nums.append(int(m.group(1)))
    return nums


def _lista(nums):
    """`0, 1, 2 y 3`. PURA, y con la `y` en su sitio."""
    if not nums:
        return "(ninguna)"
    if len(nums) == 1:
        return str(nums[0])
    return "%s y %s" % (", ".join(str(x) for x in nums[:-1]), nums[-1])


def titulo_de_la_entrada(n_adj, n_hall, n_preg, n_cai_aud, n_cai_eje):
    """El titulo, con sus CINCO numerales COMPUTADOS y no tecleados, y con la
    concordancia dentro del computo. El CERO entra por `PALABRA_CON_CERO`
    importado, y va en plural porque en castellano el cero es plural."""
    def trozo(n, sing, plur):
        if n == 1:
            return "la %s" % sing
        return "las %s %s" % (PALABRA_CON_CERO[n], plur)

    def trozo_m(n, sing, plur):
        if n == 1:
            return "el %s" % sing
        return "los %s %s" % (PALABRA_CON_CERO[n], plur)
    return ("Registro de %s, %s, %s, %s del auditor y %s del ejecutor "
            "del acta de la vuelta %d"
            % (trozo(n_adj, "adjudicacion numerada", "adjudicaciones numeradas"),
               trozo_m(n_hall, "hallazgo de la seccion 5",
                       "hallazgos de la seccion 5"),
               trozo(n_preg, "pregunta contestada", "preguntas contestadas"),
               trozo(n_cai_aud, "caida propia", "caidas propias"),
               trozo(n_cai_eje, "caida", "caidas"),
               VUELTA_DEL_ACTA))


VIA = {
    "4.1": "SIN TOCAR NADA",
    "4.2": "SIN TOCAR NADA",
    "4.3": "SIN TOCAR NADA",
    "4.4": "EJECUTADA EN LAS TAREAS 2 Y 3",
    "4.5": "SIN TOCAR NADA",
    "4.6": "EJECUTADA EN LA TAREA 2",
    "4.7": "SIN TOCAR NADA",
    "4.8": "A LA VUELTA 191",
    "4.9": "EJECUTADA EN LA TAREA 3",
    "4.10": "REGISTRADA AQUI Y APLICADA EN EL ENCARGO",
    "5.1": "A LA VUELTA 191",
    "5.2": "A LA VUELTA 191",
    "5.3": "SIN TOCAR NADA",
    "5.4": "ES LA VARA QUE ORDENA LA TAREA 5",
}

QUE_HACE_ESTA_VUELTA = {
    "4.1": ("SE ACATA SIN TOCAR NADA, Y ESTA VUELTA LA HEREDA POR IMPORTACION EN "
            "VEZ DE COPIARLA. La marca `CERO SON DEL EJECUTOR` como neutralizadora "
            "queda adjudicada a favor, y este registrador la importa literal del de "
            "la 189. **Y aqui se mide algo que el acta no dice:** el acta 190 **NO "
            "usa esa cabecera**, y su cero es de OTRA especie, el de racha. Las dos "
            "se separan mas abajo con sus dos literales."),
    "4.2": ("SE ACATA SIN TOCAR NADA. Publicar las dos cuentas de racha queda a "
            "favor en la forma, y el fondo lo resuelve el propio acta: **la tabla "
            "manda y `acumulan()` se equivoca**, porque la regla del 5 sep 2026 "
            "exige TRES actas seguidas con la misma caida propia. **El encargo que "
            "esto deja abierto** (que `acumulan()` lea la tabla o declare que no es "
            "la sede) **queda FUERA de esta vuelta y va nombrado en el encargo**, "
            "para que la 191 no lo redescubra."),
    "4.3": ("SE ACATA SIN TOCAR NADA. Seguir hasta los diez tramos con exitcode 1 "
            "queda a favor: la vara de CORRIDO es LA SALIDA SELLADA y no el "
            "exitcode. **Esta vuelta no corre la bateria** y no vuelve a tocar esa "
            "decision."),
    "4.4": ("SE ACATA Y SE EJECUTA EN DOS TAREAS DE ESTA MISMA VUELTA. Que un "
            "tramo con exitcode 1 por guarda de nomina CUENTE COMO CORRIDO sale de "
            "la 4.3; que la bateria SEPARE ese caso en su exitcode es la TAREA 3.a, "
            "y la separacion de la deuda que lo hace legible es la TAREA 2.a. **Un "
            "unico `1` para un arnes caido y para una deuda declarada es la "
            "degradacion silenciosa del banco 9.**"),
    "4.5": ("SE ACATA SIN TOCAR NADA. Meter el arnes en rojo en `LOS_QUE_CORREN` "
            "para que la exclusion lo nombre queda a favor: sin el, la salida diria "
            "**0 excluidos**, que es un cero que tapa un rojo."),
    "4.6": ("SE ACATA, Y ES EL UNICO QUE EL ACTA TUMBA. ES LA TAREA 2.b DE ESTA "
            "VUELTA. Sacar `guarda_del_sujeto_congelado()` del veredicto convierte "
            "una deuda visible en una exencion, que es lo que la `4.7` del acta 189 "
            "advirtio con esas palabras. **La guarda vuelve al veredicto**, y su "
            "remedio no es aflojar el rojo sino separar la deuda del fallo, que es "
            "la TAREA 2.a. **Y esta vuelta lo acata sin discutirlo:** el ejecutor "
            "de la 189 lo marco solo como el que menos le convencia."),
    "4.7": ("SE ACATA SIN TOCAR NADA. Retirar la constante muerta en el clon "
            "declarado queda a favor y con el motivo reforzado: su `9` ya no decia "
            "la verdad, y una cifra falsa en el comentario de una guarda es la "
            "cuarta sede de la especie desde el 2 sep 2026."),
    "4.8": ("CONTESTADA POR EL ACTA CON UN ORDEN QUE ESTA VUELTA RESPETA: **PRIMERO "
            "SE MIDE Y DESPUES SE CAMBIA EL CENSO.** El criterio queda adjudicado "
            "(el censo debe ver los carriles `--mutacion` sin fichero propio), pero "
            "la cifra que eso mueve **no esta medida**. **Esta vuelta NO la mide y "
            "NO toca el censo**: la medicion va nombrada en el encargo como una de "
            "las seis que quedan fuera."),
    "4.9": ("CONTESTADA POR EL ACTA Y EJECUTADA EN LA TAREA 3.b DE ESTA VUELTA. Una "
            "salida sellada es la prueba de la vuelta que la sello, y dejar que una "
            "corrida posterior la pise borra el registro. **La bateria pasa a "
            "restaurarlas sola**, en LF, como ya restaura `dataset/`; y si el corte "
            "nuevo interesa, **se escribe al lado con nombre nuevo y su vuelta, "
            "nunca encima**. En la 189 piso TRES y las restauro una persona a mano, "
            "en dos vueltas distintas y a dos personas distintas."),
    "4.10": ("REGISTRADA AQUI Y YA APLICADA EN EL ENCARGO DE ESTA VUELTA. El "
             "disparador de salida de la `AUDITOR.md` 6.2 pedia DOS vueltas "
             "seguidas cerrando su propio reporte y **son TRES**, medidas en git y "
             "no recordadas. **Esta vuelta lleva CINCO sub-tareas** y el bloque B.2 "
             "de su sello de apertura volvio a localizar las tres en git, por el "
             "asunto de su commit, antes de tocar nada."),
    "5.1": ("HALLAZGO DEL AUDITOR FUERA DE LO QUE EL REPORTE MARCA, Y VA A LA "
            "VUELTA 191. El registrador de la 189 cuenta con `len(texto.split(NL))` "
            "y publica 2231 donde `wc -l` da 2230; `cerrar_reporte.py` cuenta con "
            "`texto.count(NL)` y calza. **Esta vuelta no iguala los instrumentos**, "
            "pero **su propio sello de apertura ya publica LAS DOS cifras** del "
            "acta cuando la nombra, que es lo que la casa hizo con los BYTES."),
    "5.2": ("HALLAZGO DEL AUDITOR FUERA DE LO QUE EL REPORTE MARCA, Y VA A LA "
            "VUELTA 191. La serie cierra sin huecos de NUMERO y aun asi tiene un "
            "hueco de CONTENIDO de ocho actas (173 a 180). **Esta entrada lo vuelve "
            "a medir en esta vuelta** con `actas_sin_entrada()`, en vez de "
            "heredarlo, y **no lo rellena**: escribir de memoria los registros de "
            "unas actas que nadie ha releido seria justo lo que `AUDITOR.md` 2 "
            "prohibe."),
    "5.3": ("SE ACATA SIN TOCAR NADA. Es una medicion del auditor sobre su propio "
            "arbol: re corrio tres arneses y el registrador sin `--mutacion`, y "
            "`git diff --numstat` cerro en 0 filas con `docs/PENDIENTES.md` en sus "
            "961248 bytes. **Es el remedio de su `C.2` del acta 189 funcionando**, "
            "y esta vuelta lo vuelve a probar re corriendo su propio registrador."),
    "5.4": ("ES LA VARA QUE ORDENA LA TAREA 5 DE ESTA VUELTA, Y SUS CIFRAS SE LEEN "
            "DEL PARRAFO EN VEZ DE COPIARSE. Confirma medida la `4.1` del acta 189: "
            "`OP-L-02` es la unica de las cuatro fichas de TRABAJO REAL **sin "
            "documento que medir**. **Por eso su encargo es una BUSQUEDA y no una "
            "improvisacion**, y por eso el limite esta escrito: si la busqueda no "
            "encuentra sede, ESO es el resultado, y **no se le inventa una**."),
}


def armar_entrada(numero, titulo, medido):
    """LA ENTRADA ENTERA. PURA: recibe todo lo ya medido en un diccionario y no
    lee ni escribe nada."""
    m = medido
    p = []
    p.append("## R.%d. %s" % (numero, titulo))
    p.append("")
    p.append("(Acta del auditor, vuelta %d, secciones %s; escrito en la vuelta %d,"
             % (VUELTA_DEL_ACTA, _lista(m["secciones"]), VUELTA_QUE_ESCRIBE))
    p.append("TAREA 1.)")
    p.append("")
    p.append("Por adicion, como `R.21` a `R.51`. **Corte de todas las cifras de esta")
    p.append("entrada: 6 sep 2026.** El numero de esta entrada NO esta tecleado: lo computa")
    p.append("`scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS sedes.")
    p.append("La SEDE tampoco se supone: sale de la adjudicacion 6.3 del acta 162, que es")
    p.append("la que citan los `R.30` a `R.51`. Salida:")
    p.append("`docs/loop/SALIDA_V%s_T1A_REGISTRO_R%d.txt`."
             % (SUFIJO_QUE_ESCRIBE, numero))
    p.append("")
    p.append("**ESTA ENTRADA SE ESCRIBE CON LA TAREA 1 EN CURSO Y LAS TAREAS 2 A 5 SIN")
    p.append("EMPEZAR, ASI QUE SUS GLOSAS NO AFIRMAN EN PASADO LO QUE TODAVIA NO HA")
    p.append("PASADO.** Es la forma que la `6.4` del acta 172 adjudico como correcta: donde")
    p.append("una glosa dice que una tarea la ejecuta, la tarea va nombrada; donde dice que")
    p.append("va a ejecutarse, se dice que **todavia no ha corrido**.")
    p.append("")
    p.append("**Y LOS CINCO NUMERALES DEL TITULO TAMPOCO ESTAN TECLEADOS:** se cuentan del")
    p.append("acta acotada (lineas %d a %d) y de ahi sale el numeral en palabra, incluida"
             % (m["inicio"], m["fin"]))
    p.append("la concordancia. **%d adjudicaciones numeradas (`4.1` a `4.%d`, todas en la"
             % (m["n_adj"], m["n_adj"]))
    p.append("seccion 4), %d hallazgos numerados en la seccion 5, %d preguntas contestadas"
             % (m["n_hall"], m["n_preg"]))
    p.append("DENTRO de las adjudicaciones, %d caidas propias del auditor y %d caidas del"
             % (m["n_aud"], m["n_eje"]))
    p.append("ejecutor.**")
    p.append("")
    p.append("**LA FORMA DE LOS NUMERALES SE MIDE CON LOS DOS PATRONES Y LAS DOS CIFRAS SE")
    p.append("PUBLICAN.** Corrido sobre esta acta, **el patron entrecomillado (el del acta")
    p.append("188) da %d y el suelto (el del acta 189) da %d**. **Ninguno de los dos se"
             % (m["n_entrecomillado"], m["n_adj"]))
    p.append("ensancha: se corren los dos y se dice lo que dan.**")
    p.append("")
    p.append("**Y AQUI ESTA LO QUE ESTA ACTA ESTRENA Y LO QUE MAS FACIL SERIA CONTAR MAL:")
    p.append("LAS DIEZ ADJUDICACIONES NO SON DIEZ A FAVOR.** De las %d que nombran un"
             % m["n_adj"])
    p.append("`D.n` o un `P.n`, **%d son discutibles del ejecutor y de esos %d van A FAVOR y"
             % (m["n_discutibles"], m["n_a_favor_discutibles"]))
    p.append("%d va EN CONTRA**. **La marca `EN CONTRA` no es una glosa: se busca literal en"
             % m["n_en_contra_discutibles"])
    p.append("el titulo, ANTES que `A FAVOR`, y sale en la cuenta.** El registrador de la")
    p.append("189 no la conocia: sus cinco marcas no la incluyen, y su regla de cuenta")
    p.append("**PARABA si algun discutible no llevaba `A FAVOR`**, porque los seis de aquel")
    p.append("acta lo llevaban. **Heredarla habria hecho PARAR este instrumento sobre un")
    p.append("acta perfectamente legible, o peor, habria publicado seis a favor.**")
    p.append("")
    p.append("**EL QUE VA EN CONTRA, NOMBRADO:** %s."
             % (", ".join("`%s` (%s)" % (c, d)
                          for c, d in m["en_contra_nombrados"]) or "(ninguno)"))
    p.append("")
    p.append("**LAS %s ADJUDICACIONES NUMERADAS, CON SU LINEA EN EL ACTA LEIDA HOY.** El"
             % PALABRA_CON_CERO[m["n_adj"]].upper())
    p.append("titulo de cada una es LITERAL del fichero; la glosa que sigue es prosa del")
    p.append("ejecutor y va marcada como tal.")
    p.append("")
    for clave, familia, estado, ln, tit in m["adjudicaciones"]:
        p.append("  - **`%s` (`docs/loop/ACTA_AUDITOR.md:%d`, leida hoy). FAMILIA: %s. "
                 "ESTADO: %s. VIA: %s.** Titulo" % (clave, ln, familia, estado,
                                                    VIA.get(clave, "(sin via)")))
        p.append("    literal del acta: *\"%s\"*" % tit)
        p.append("    **QUE HACE ESTA VUELTA CON ELLA (glosa del ejecutor, no del acta):** %s"
                 % QUE_HACE_ESTA_VUELTA.get(clave, "(sin glosa)"))
    p.append("")
    p.append("**LAS %s PREGUNTAS ESTAN CONTESTADAS Y NO TIENEN SECCION PROPIA:** viven"
             % PALABRA_CON_CERO[m["n_preg"]].upper())
    p.append("DENTRO de las adjudicaciones, como en el acta 189. **Cuales son NO se")
    p.append("teclea:** son las %d cuyo titulo nombra un `P.n`, y son **%s**."
             % (m["n_preg"],
                ", ".join("`%s` que nombra `%s`" % (c, pn) for c, pn in m["preguntas"])))
    p.append("")
    p.append("**LOS %s HALLAZGOS DE LA SECCION 5, Y SOLO %s CUENTAN COMO HALLAZGO FUERA"
             % (PALABRA_CON_CERO[m["n_hall"]].upper(),
                PALABRA_CON_CERO[len(m["hall_nombrados"])].upper()))
    p.append("DEL MARCADO.** **Cual cuenta NO SE TECLEA:** sale de la fila")
    p.append("`%s` de la tabla de credito del propio acta," % AGUJA_FILA_FUERA)
    p.append("cuyo parentesis se parte por `;`, se normaliza y se busca dentro del titulo")
    p.append("literal de cada `5.n`. La fila, leida del fichero:")
    p.append("")
    for ln, txt in m["fila_fuera"]:
        p.append("  - `docs/loop/ACTA_AUDITOR.md:%d`: %s" % (ln, txt))
    p.append("")
    p.append("  Las piezas que salen de su parentesis: %s."
             % (", ".join("*%s*" % x for x in m["piezas_fuera"]) or "(ninguna)"))
    p.append("")
    for clave, ln, tit in m["hallazgos"]:
        marca = ("**LA TABLA LA NOMBRA COMO HALLAZGO FUERA DEL MARCADO**"
                 if clave in m["claves_nombradas"] else
                 "no sale en el parentesis de esa fila")
        p.append("  - **`%s` (`docs/loop/ACTA_AUDITOR.md:%d`, leida hoy). VIA: %s.** %s."
                 % (clave, ln, VIA.get(clave, "(sin via)"), marca))
        p.append("    Titulo literal del acta: *\"%s\"*" % tit)
        p.append("    **QUE HACE ESTA VUELTA CON EL (glosa del ejecutor, no del acta):** %s"
                 % QUE_HACE_ESTA_VUELTA.get(clave, "(sin glosa)"))
    p.append("")
    p.append("**LA VARA DE LA `5.4`, CON SUS CIFRAS LEIDAS DEL PARRAFO Y NO COPIADAS DEL")
    p.append("ENCARGO.** El auditor la corrio con `--corte 63d0c5b4` y su salida vive en")
    p.append("`docs/loop/_auditor_v190_vara.txt` (**%d bytes en disco y %d normalizado a"
             % (m["vara_bytes_disco"], m["vara_bytes_lf"]))
    p.append("LF**, medido hoy). Las cifras que su parrafo publica, extraidas una a una:")
    p.append("")
    for etiqueta, valor, _pat in m["vara"]:
        p.append("  - **%s: %s**"
                 % (etiqueta, "NO SE PUDO LEER" if valor is None else valor))
    p.append("")
    p.append("**Y ESO ES LO QUE HACE QUE LA TAREA 5 SEA UNA BUSQUEDA.** `OP-L-02` es la")
    p.append("unica de las cuatro fichas de TRABAJO REAL sin documento que medir. **El")
    p.append("limite va escrito en el propio encargo: si la busqueda no encuentra sede, ESO")
    p.append("es el resultado, y no se le inventa una ni se la declara HECHA.**")
    p.append("")
    p.append("**LAS CAIDAS: %s DEL AUDITOR Y %s DEL EJECUTOR, Y LAS DOS CIFRAS SALEN DE UNA"
             % (PALABRA_CON_CERO[m["n_aud"]].upper(),
                PALABRA_CON_CERO[m["n_eje"]].upper()))
    p.append("MAQUINA QUE ESTA ACTA OBLIGO A ESCRIBIR.** Y aqui van las dos mediciones que")
    p.append("prueban que hacia falta, en vez de afirmarlo:")
    p.append("")
    p.append("  - **EL PATRON `C.n` DE CABEZA DE LINEA DA %d SOBRE ESTA ACTA.** El de la"
             % m["n_c_espacio"])
    p.append("    187 (coma o punto pegados) da %d y el de la 188 (que admite tambien un"
             % m["n_c_crudo"])
    p.append("    espacio) da %d. **Las tres caidas del acta 190 van DENTRO de un parrafo,"
             % m["n_c_espacio"])
    p.append("    entre parentesis**, y ningun patron de cabeza de linea puede verlas.")
    p.append("  - **LA CABECERA DE LA SECCION 6 NO DICE DE QUIEN SON.** Es")
    p.append("    *\"%s\"*, a secas. Corrido sobre ella," % m["cabecera_seccion6"])
    p.append("    `caidas_por_seccion()` del registrador de la 189 saca **ejecutor %d,"
             % m["viejo_eje"])
    p.append("    auditor %d, huerfanas %d**, y con huerfanas este instrumento haria PARADA."
             % (m["viejo_aud"], m["viejo_huerf"]))
    p.append("")
    p.append("**EL REMEDIO ES LEER LA NEGRITA QUE ABRE CADA PARRAFO, QUE ES DONDE ESTA ACTA")
    p.append("SI LO DICE**, y las marcas son literales suyas: `%s` para el ejecutor y"
             % MARCAS_LEAD_EJECUTOR[0])
    p.append("`%s` para el auditor. Con eso el reparto sale **ejecutor %d, auditor %d,"
             % (MARCAS_LEAD_AUDITOR[0], m["n_eje"], m["n_aud"]))
    p.append("huerfanas %d**. Las tres del ejecutor son %s."
             % (m["n_huerf"],
                ", ".join("`C.%d`" % n for _l, n, _c in m["c_eje"]) or "(ninguna)"))
    p.append("")
    p.append("**Y AQUI VA LA DISTINCION QUE ESTA VUELTA ESTRENA, PORQUE CONFUNDIRLA HABRIA")
    p.append("BORRADO LAS TRES: UN CERO DE RACHA NO ES UN CERO DE CUENTA.** El acta 189")
    p.append("traia `%s`, que es un cero de CUENTA: no hay ninguna, y por eso"
             % MARCAS_CERO_DE_CUENTA[0])
    p.append("la `4.1` adjudico que NEUTRALIZA la atribucion. El acta 190 trae")
    p.append("`%s`, que es un cero de RACHA, **y en ese mismo parrafo declara"
             % FRASE_CERO_RACHA_EJECUTOR)
    p.append("TRES caidas**. Aplicarle la neutralizacion de la `4.1` habria dado **cero")
    p.append("caidas del ejecutor** en vez de tres. **Corrido a proposito con la marca de")
    p.append("racha tratada como marca de cuenta, el reparto sale ejecutor %d y auditor %d.**"
             % (m["cero_confundido_eje"], m["cero_confundido_aud"]))
    p.append("")
    p.append("**LA ESPECIE DE LAS TRES, LEIDA DEL PARRAFO Y NO SUPUESTA:** el literal")
    p.append("`%s` aparece en **%d** de los parrafos de la seccion 6, y es el que"
             % (MARCA_ESPECIE_METODO, m["n_parrafos_metodo"]))
    p.append("cubre a las tres. **Ninguna de las tres abre racha**, y eso lo declara la")
    p.append("tabla de credito del acta, leida literal:")
    p.append("")
    for ln, txt in m["fila_metodo"]:
        p.append("  - `docs/loop/ACTA_AUDITOR.md:%d`: %s" % (ln, txt))
    p.append("")
    p.append("**EL CERO DEL AUDITOR VA CONTADO Y NO OMITIDO, Y NO SE PUBLICA DESNUDO.** El")
    p.append("reparto le da **%d** caidas propias, y **un cero que sale de una maquina que"
             % m["n_aud"])
    p.append("no muerde no es evidencia de nada**: va con la declaracion literal del acta al")
    p.append("lado. La frase `%s` aparece en **%d linea(s)**"
             % (FRASE_CERO_AUDITOR, len(m["decl_cero_aud"])))
    p.append("(`docs/loop/ACTA_AUDITOR.md:%s`), y la fila de la tabla de credito dice:"
             % (", ".join(str(x) for x in m["decl_cero_aud"]) or "ninguna"))
    p.append("")
    for ln, txt in m["fila_aud"]:
        p.append("  - `docs/loop/ACTA_AUDITOR.md:%d`: %s" % (ln, txt))
    p.append("")
    p.append("**Si el reparto diera cero y el acta no lo declarara por ninguna frase, este")
    p.append("instrumento haria PARADA.**")
    p.append("")
    p.append("**LOS PATRONES VIEJOS, CORRIDOS IGUAL Y CON SU CIFRA PUBLICADA:** el `A.n` de")
    p.append("cabecera de tercer nivel (acta 185) da **%d**, el `R.n` de caida de reporte da"
             % m["n_a"])
    p.append("**%d** y el `E.n` de las actas 182 y 184 da **%d**. **Las tres se publican y"
             % (m["n_rep"], m["n_eje_viejo"]))
    p.append("ninguna se resuelve copiando.**")
    p.append("")
    p.append("**LA DEUDA DE LA SERIE, QUE ES EL HALLAZGO `5.2` Y QUE SE VUELVE A MEDIR AQUI")
    p.append("EN VEZ DE HEREDARSE DEL `R.51`:**")
    p.append("")
    faltan, bajo, alto = m["salto"]
    p.append("  - **SALTO DE %d REGISTROS EN LA SERIE: las actas %s no tienen"
             % (len(faltan), ("%d a %d" % (min(faltan), max(faltan))) if faltan
                else "(ninguna)"))
    p.append("    entrada propia.** Sus dos extremos, contados por")
    p.append("    `scripts/loop/serie_de_registros.py` y no tecleados: **`R.%s` cubre el"
             % (bajo[0] if bajo else "?"))
    p.append("    acta %s** y **`R.%s` cubre el acta %s**. **No se rellenan aqui:**"
             % (bajo[1] if bajo else "?", alto[0] if alto else "?",
                alto[1] if alto else "?"))
    p.append("    escribir de memoria los registros de unas actas que nadie ha releido")
    p.append("    en esta vuelta seria justo lo que `AUDITOR.md` 2 prohibe.")
    p.append("")
    p.append("**Y ESTA ENTRADA LA ESCRIBE UN REGISTRADOR IDEMPOTENTE, Y LA IDEMPOTENCIA NO")
    p.append("SE RE ESCRIBE: SE IMPORTA DEL DE LA 189, QUE ES DONDE NACIO.** El auditor la")
    p.append("probo en su `5.3` re corriendola: **no escribe nada y `docs/PENDIENTES.md` se")
    p.append("queda en sus 961248 bytes**. La comprobacion es **por el acta y no por el")
    p.append("numero**, con las marcas literales `%s` y `%s`," % marcas_del_acta(VUELTA_DEL_ACTA))
    p.append("y **en LAS DOS SEDES**. Antes de escribir esta entrada, esas marcas aparecian")
    p.append("en **%d linea(s)**." % m["ya_registrada"])
    p.append("")
    p.append("**LO QUE ESTA ENTRADA NO REGISTRA, DICHO PARA QUE NO SE BUSQUE:** no registra")
    p.append("las dos convenciones de `lineas` igualadas, ni `acumulan()` leyendo la tabla,")
    p.append("ni el cotejo de clon declarado que separa, ni la excepcion que publica siempre")
    p.append("su lista, ni la medicion del censo de arneses sin fichero, ni las ocho actas")
    p.append("sin entrada propia rellenadas: **las seis van a la vuelta 191** y el encargo")
    p.append("de esta vuelta ya las lleva nombradas para que no haya que redescubrirlas. **Y")
    p.append("no se poda la nomina de la bateria**, que es la opcion `c` que el fundador")
    p.append("RECHAZO el 5 sep 2026, **ni se corre la bateria**, que cae en la 194.")
    return NL.join(p) + NL


# ---------------------------------------------------------------- LA MUTACION
def _acta_fabricada(n_a_favor, n_en_contra, cabecera_caidas, negrita_eje,
                    negrita_aud, n_caidas_eje, vuelta=None,
                    con_declaracion_cero_aud=True, fila_fuera=None):
    """UN ACTA ENTERA FABRICADA, CON LAS CIFRAS QUE SE LE PIDAN. PURA.

    NO SE TOCA EL REPO PARA PROBAR: el arnes corre sobre este texto. La cabecera
    de la seccion de caidas y LAS DOS NEGRITAS son PARAMETRO, que es lo que
    permite probar los tres repartos (auditor, ejecutor y HUERFANA) y las dos
    especies de cero sin inventar precedencias."""
    v = vuelta if vuelta is not None else VUELTA_DEL_ACTA
    L = []
    L.append("# ACTA DEL AUDITOR, VUELTA %d (fabricada para el arnes)" % v)
    L.append("")
    L.append("## 4. LAS ADJUDICACIONES")
    L.append("")
    k = 0
    for _ in range(n_a_favor):
        k += 1
        L.append("**4.%d `D.%d`, un titulo fabricado. A FAVOR.** Prosa de relleno que" % (k, k))
        L.append("no dice nada y esta aqui para que el parrafo exista.")
        L.append("")
    for _ in range(n_en_contra):
        k += 1
        L.append("**4.%d `D.%d`, otro titulo fabricado. EN CONTRA, Y ES EL QUE TUMBO.**" % (k, k))
        L.append("Prosa de relleno.")
        L.append("")
    k += 1
    L.append("**4.%d `P.1`, una pregunta fabricada. CUENTA COMO CORRIDO, Y ALGO DEBE" % k)
    L.append("PASAR.** Prosa de relleno.")
    L.append("")
    L.append("## 5. LO QUE TRAIGO YO")
    L.append("")
    L.append("**5.1 UNA COSA FABRICADA QUE NADIE MARCO.** Prosa de relleno.")
    L.append("")
    L.append("**5.2 OTRA COSA FABRICADA QUE TAMPOCO.** Prosa de relleno.")
    L.append("")
    L.append("## %d. %s" % (SECCION_DE_LAS_CAIDAS, cabecera_caidas))
    L.append("")
    cs = ", ".join("`C.%d`" % (j + 1) for j in range(n_caidas_eje))
    L.append("**%s** Declara %d (%s), y las tres SON DE METODO." % (negrita_eje, n_caidas_eje, cs))
    L.append("")
    if con_declaracion_cero_aud:
        L.append("**%s** Prosa de relleno." % negrita_aud)
        L.append("")
    L.append("## 7. LA METRICA DE CREDITO")
    L.append("")
    L.append("| | esta vuelta | acumulado |")
    L.append("|---|---:|---:|")
    L.append("| %s | **2** | **1** |"
             % (fila_fuera or (AGUJA_FILA_FUERA
                               + " | **2** (una cosa fabricada; otra cosa fabricada)")))
    L.append("| %s | **0** | ninguna repetida |" % AGUJA_FILA_CAIDAS_AUDITOR)
    L.append("| %s, registradas y sin racha | **%d** | |"
             % (AGUJA_FILA_CAIDAS_METODO, n_caidas_eje))
    L.append("")
    return NL.join(L)


def _caso(w, nombre, obtenido, esperado):
    """UN CASO DEL ARNES, CON SU MUTACION AL LADO. Devuelve 1 si CAE."""
    ok = obtenido == esperado
    w("   %-58s obtenido %-22s esperado %-22s -> %s"
      % (nombre, repr(obtenido), repr(esperado), "PASA" if ok else "CAE"))
    return 0 if ok else 1


def prueba_de_mutacion():
    """EL CASO POSITIVO POR MUTACION, SOBRE ACTAS FABRICADAS Y SEDES FABRICADAS.

    NINGUN assert SE PUBLICA COMO PRUEBA SIN HABER CORRIDO ANTES SU PRUEBA DE
    MUTACION (`EJECUTOR.md` 1, EL CASO ROJO SE PRUEBA POR MUTACION): cada caso
    verde de abajo va seguido de su gemelo con el ESPERADO MUTADO, y el arnes
    exige que el gemelo CAIGA."""
    salida = []
    w = salida.append
    w("=" * 78)
    w("CASO POSITIVO POR MUTACION DEL REGISTRADOR DEL ACTA %d" % VUELTA_DEL_ACTA)
    w("=" * 78)
    w("")
    fallos = 0
    no_cayeron = 0

    CAB_190 = "LAS CAIDAS"
    NEG_EJE = "DEL EJECUTOR: CERO QUE ACUMULEN."
    NEG_AUD = "MIAS: CERO."

    # ---------------------------------------------------------------- BLOQUE A
    w("A) EL ACOTADO DEL ACTA SOBRE UN TEXTO FABRICADO")
    txt = _acta_fabricada(5, 1, CAB_190, NEG_EJE, NEG_AUD, 3)
    lineas, rango, err = cuerpo_del_acta(txt, "# ACTA DEL AUDITOR, VUELTA %d"
                                         % VUELTA_DEL_ACTA)
    fallos += _caso(w, "error de acotado", err, None)
    fallos += _caso(w, "el acta empieza en la linea 1", rango[0] if rango else None, 1)
    w("   LA MUTACION: se pide una cabecera que el texto NO trae, y tiene que PARAR")
    _l2, _r2, err2 = cuerpo_del_acta(txt, "# ACTA DEL AUDITOR, VUELTA 999")
    if err2 is None:
        w("      LA MUTACION NO CAYO: acoto un acta que no existe.")
        no_cayeron += 1
    else:
        w("      LA MUTACION CAE, y su texto es: %s" % err2)
    w("")

    # ---------------------------------------------------------------- BLOQUE B
    w("B) EL ESTADO `EN CONTRA`, QUE ES LO QUE ESTA ACTA ESTRENA")
    ini, fin = rango
    claves = claves_de_adjudicacion(lineas, ini, fin, PREFIJO_ADJ)
    fallos += _caso(w, "adjudicaciones sobre 5 a favor + 1 en contra + 1 pregunta",
                    len(claves), 7)
    estados = []
    for clave, _n in claves:
        pat = re.compile(r"^\s*\*\*%s " % re.escape(clave))
        res, e = titulo_de_la_negrita(lineas, ini, fin, pat, clave)
        estados.append((clave, familia_de_la_adjudicacion(res[1]),
                        estado_de_la_adjudicacion(res[1])))
    disc = [x for x in estados if x[1] == "DISCUTIBLE"]
    favor = [x for x in disc if x[2] == "A FAVOR"]
    contra = [x for x in disc if x[2] == "EN CONTRA"]
    fallos += _caso(w, "discutibles", len(disc), 6)
    fallos += _caso(w, "discutibles A FAVOR", len(favor), 5)
    fallos += _caso(w, "discutibles EN CONTRA", len(contra), 1)
    fallos += _caso(w, "ninguno SIN DECIR",
                    len([x for x in estados if x[2] == "SIN DECIR"]), 0)
    w("   LA MUTACION 1: el esperado de EN CONTRA se cambia a 0 y tiene que CAER")
    if len(contra) == 0:
        w("      LA MUTACION NO CAYO: la marca EN CONTRA no se ve.")
        no_cayeron += 1
    else:
        w("      LA MUTACION CAE: son %d y no 0." % len(contra))
    w("   LA MUTACION 2: la regla de la 189 (todos los discutibles A FAVOR) sobre")
    w("   esta acta, que es la que habria PARADO o publicado seis a favor")
    if len(favor) == len(disc):
        w("      LA MUTACION NO CAYO: %d de %d, la regla vieja no se entera."
          % (len(favor), len(disc)))
        no_cayeron += 1
    else:
        w("      LA MUTACION CAE: %d A FAVOR de %d discutibles, o sea que la regla"
          % (len(favor), len(disc)))
        w("      vieja habria hecho PARADA sobre un acta perfectamente legible.")
    w("   LA MUTACION 3: el orden importa. Un titulo con LAS DOS marcas tiene que")
    w("   salir EN CONTRA, porque `EN CONTRA` se busca primero")
    doble = estado_de_la_adjudicacion("`D.9`, algo. A FAVOR DE UNA COSA Y EN CONTRA DE OTRA.")
    if doble != "EN CONTRA":
        w("      LA MUTACION NO CAYO: sale %r y no EN CONTRA." % doble)
        no_cayeron += 1
    else:
        w("      LA MUTACION CAE: con las dos marcas sale EN CONTRA, no A FAVOR.")
    w("")

    # ---------------------------------------------------------------- BLOQUE C
    w("C) LAS CAIDAS EN LINEA, CON LA ATRIBUCION POR LA NEGRITA DEL PARRAFO")
    r6 = rango_de_seccion(lineas, ini, fin, SECCION_DE_LAS_CAIDAS)
    fallos += _caso(w, "la seccion 6 se localiza", r6 is not None, True)
    eje, aud, hue = caidas_en_linea(lineas, r6[0], r6[1])
    fallos += _caso(w, "reparto (ejecutor, auditor, huerfanas)",
                    (len(eje), len(aud), len(hue)), (3, 0, 0))
    w("   Y EL PATRON DE CABEZA DE LINEA SOBRE LA MISMA SECCION, QUE ES EL QUE NO VE")
    w("   NADA PORQUE LAS `C.n` VAN DENTRO DEL PARRAFO:")
    fallos += _caso(w, "patron `C.n` de cabeza de linea",
                    len(cuenta_por_patron(lineas, r6[0], r6[1], PAT_CAIDA_C_ESPACIO)), 0)
    w("   Y LA MAQUINA DE LA 189 SOBRE LA MISMA SECCION, QUE SACA TODAS HUERFANAS")
    v_eje, v_aud, v_hue = caidas_por_seccion(lineas, r6[0], r6[1])
    fallos += _caso(w, "caidas_por_seccion() de la 189",
                    (len(v_eje), len(v_aud), len(v_hue)), (0, 0, 0))
    w("      (da (0,0,0) porque su patron es de cabeza de linea y aqui no hay")
    w("       ninguna: por eso hacen falta LAS DOS cosas, el patron en linea Y la")
    w("       atribucion por negrita)")
    w("   LA NEGRITA MUDA: un parrafo cuya negrita no diga de quien son")
    txt_mudo = _acta_fabricada(5, 1, CAB_190, "PASARON COSAS.", NEG_AUD, 3)
    lm, rm, _e = cuerpo_del_acta(txt_mudo, "# ACTA DEL AUDITOR, VUELTA %d"
                                 % VUELTA_DEL_ACTA)
    r6m = rango_de_seccion(lm, rm[0], rm[1], SECCION_DE_LAS_CAIDAS)
    e2, a2, h2 = caidas_en_linea(lm, r6m[0], r6m[1])
    fallos += _caso(w, "negrita muda -> huerfanas", (len(e2), len(a2), len(h2)),
                    (0, 0, 3))
    w("      LA PARADA SE CONSERVA ENTERA: %d huerfana(s), y una caida sin dueno no"
      % len(h2))
    w("      se reparte a ojo.")
    w("")

    # ---------------------------------------------------------------- BLOQUE D
    w("D) UN CERO DE RACHA NO ES UN CERO DE CUENTA, Y CONFUNDIRLOS BORRA LAS TRES")
    w("   (la negrita fabricada es %r, que trae CERO QUE ACUMULEN)" % NEG_EJE)
    fallos += _caso(w, "con la separacion puesta: ejecutor", len(eje), 3)
    confundido = caidas_en_linea(lineas, r6[0], r6[1],
                                 marcas_cero_cuenta=(MARCAS_CERO_DE_CUENTA
                                                     + MARCAS_CERO_DE_RACHA))
    fallos += _caso(w, "tratando el cero de RACHA como cero de CUENTA: ejecutor",
                    len(confundido[0]), 0)
    w("   LA MUTACION: si las dos especies de cero fueran la misma, el ejecutor")
    w("   saldria con 0 caidas y las tres del acta desaparecerian de la cuenta")
    if len(confundido[0]) == len(eje):
        w("      LA MUTACION NO CAYO: la distincion no cambia nada.")
        no_cayeron += 1
    else:
        w("      LA MUTACION CAE: %d con la separacion y %d sin ella. Las tres se"
          % (len(eje), len(confundido[0])))
        w("      perderian, y eso es exactamente lo que el encargo avisa.")
    w("   Y EL CERO DE CUENTA DEL ACTA 189 SIGUE NEUTRALIZANDO, QUE ES LA `4.1`:")
    txt_189 = _acta_fabricada(5, 1, CAB_190, "CERO SON DEL EJECUTOR.", NEG_AUD, 3)
    l189, r189, _e = cuerpo_del_acta(txt_189, "# ACTA DEL AUDITOR, VUELTA %d"
                                     % VUELTA_DEL_ACTA)
    r6_189 = rango_de_seccion(l189, r189[0], r189[1], SECCION_DE_LAS_CAIDAS)
    e3, a3, h3 = caidas_en_linea(l189, r6_189[0], r6_189[1])
    fallos += _caso(w, "negrita con CERO SON DEL EJECUTOR -> no le atribuye",
                    (len(e3), len(a3), len(h3)), (0, 0, 3))
    w("")

    # ---------------------------------------------------------------- BLOQUE E
    w("E) LOS HALLAZGOS DE LA SECCION 5 Y LA FILA DE LA TABLA QUE DICE CUALES CUENTAN")
    hall = []
    for clave, _n in claves_de_adjudicacion(lineas, ini, fin, PREFIJO_HALLAZGO):
        pat = re.compile(r"^\s*\*\*%s " % re.escape(clave))
        res, _e = titulo_de_la_negrita(lineas, ini, fin, pat, clave)
        hall.append((clave, res[0], res[1]))
    fallos += _caso(w, "hallazgos `5.n` sobre el fabricado", len(hall), 2)
    fila = fila_de_la_metrica(lineas, ini, fin, AGUJA_FILA_FUERA)
    fallos += _caso(w, "la fila de la tabla se localiza", len(fila), 1)
    nombrados, sueltos, piezas = hallazgos_que_la_tabla_nombra(hall, fila[0][1])
    w("   piezas del parentesis: %s" % ", ".join(repr(x) for x in piezas))
    fallos += _caso(w, "hallazgos que la fila nombra", len(nombrados), 2)
    w("   LA MUTACION: una fila cuyo parentesis nombre otra cosa NO tiene que casar")
    n2, s2, p2 = hallazgos_que_la_tabla_nombra(
        hall, "| %s | **2** (algo que no existe; otra que tampoco) | **1** |"
        % AGUJA_FILA_FUERA)
    if len(n2) != 0:
        w("      LA MUTACION NO CAYO: casan %d cuando no deberia casar ninguna."
          % len(n2))
        no_cayeron += 1
    else:
        w("      LA MUTACION CAE: 0 casan, o sea que el cotejo mira el texto y no")
        w("      cuenta filas a ojo.")
    w("")

    # ---------------------------------------------------------------- BLOQUE F
    w("F) LA IDEMPOTENCIA, IMPORTADA DE LA 189 Y PROBADA IGUAL SOBRE SEDES FABRICADAS")
    marca_titulo, _mc = marcas_del_acta(VUELTA_DEL_ACTA)
    sede_vacia = {"fabricada/A.md": "## R.1. Registro de algo del acta de la vuelta 1\n",
                  "fabricada/B.md": "nada que ver\n"}
    fallos += _caso(w, "sede sin la entrada -> se puede escribir",
                    len(entradas_que_registran(VUELTA_DEL_ACTA, sede_vacia)), 0)
    entrada_falsa = ("## R.99. Registro de lo que sea %s\n\n(Acta del auditor, "
                     "vuelta %d, secciones 4;\n" % (marca_titulo, VUELTA_DEL_ACTA))
    sede_escrita = dict(sede_vacia)
    sede_escrita["fabricada/A.md"] = sede_vacia["fabricada/A.md"] + "\n" + entrada_falsa
    halladas = entradas_que_registran(VUELTA_DEL_ACTA, sede_escrita)
    fallos += _caso(w, "sede CON la entrada -> ya no se escribe", len(halladas), 2)
    puede = len(entradas_que_registran(VUELTA_DEL_ACTA, sede_escrita)) == 0
    if puede:
        w("      LA MUTACION NO CAYO: dejaria escribir una entrada duplicada.")
        no_cayeron += 1
    else:
        w("      LA MUTACION CAE: la segunda escritura queda prohibida, con %d"
          % len(halladas))
        w("      linea(s) de prueba.")
    w("")

    # ---------------------------------------------------------------- BLOQUE G
    w("G) LAS CIFRAS DE LA VARA, SOBRE UN PARRAFO FABRICADO")
    fab = ("**5.4 LA VARA** (`--corte abc`): **71 fichas, 37 que no calzan, 6 en "
           "LISTA sin ninguna prueba, de las cuales 2 estan CONSUMIDAS por "
           "`OP-U-01` y 4 son TRABAJO REAL**; de esas cuatro, **3 son mesas cuyo "
           "producto documental existe en disco** y **`OP-L-02` es la unica SIN "
           "DOCUMENTO QUE MEDIR** (0 menciones de fichero en su evidencia).")
    leidas = dict((e, v) for e, v, _p in cifras_de_la_vara(fab))
    fallos += _caso(w, "fichas", leidas["fichas"], 71)
    fallos += _caso(w, "en LISTA sin ninguna prueba",
                    leidas["en LISTA sin ninguna prueba"], 6)
    fallos += _caso(w, "de TRABAJO REAL", leidas["de TRABAJO REAL"], 4)
    fallos += _caso(w, "menciones de fichero de OP-L-02",
                    leidas["menciones de fichero de OP-L-02"], 0)
    w("   LA MUTACION: sobre un parrafo SIN cifras, todas tienen que salir None y")
    w("   NINGUNA se inventa")
    vacio = dict((e, v) for e, v, _p in cifras_de_la_vara("**5.4 LA VARA.** Nada."))
    if any(v is not None for v in vacio.values()):
        w("      LA MUTACION NO CAYO: alguna cifra sale de la nada: %r" % vacio)
        no_cayeron += 1
    else:
        w("      LA MUTACION CAE: las %d salen None y ninguna se inventa." % len(vacio))
    w("")

    w("=" * 78)
    w("CIFRA casos: los de arriba, uno por linea con PASA o CAE")
    w("CIFRA casos que CAEN: %d" % fallos)
    w("CIFRA mutaciones que NO cayeron (y deberian): %d" % no_cayeron)
    if fallos or no_cayeron:
        w("VEREDICTO: ROJO")
    else:
        w("VEREDICTO: VERDE")
    texto = NL.join(salida) + NL
    ruta = os.path.join(LOOP, "SALIDA_V%s_T1A_MUTACION_REGISTRADOR.txt"
                        % SUFIJO_QUE_ESCRIBE)
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(texto)
    print(texto)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(texto.encode("utf-8"))))
    return 1 if (fallos or no_cayeron) else 0


# ------------------------------------------------------------------ LA MEDIDA
def _medir():
    """LA PRIMERA MITAD DE main(): acotar el acta y contar. Devuelve o bien un
    entero (codigo de salida, cuando hay PARADA) o bien la tupla (salida, medido).

    TODA CIFRA SALE DE AQUI Y NINGUNA DEL ENCARGO. Donde el encargo o el acta
    publican una, se computa la propia y **se publican las dos**."""
    salida = []
    w = salida.append
    w("=" * 78)
    w("VUELTA %d, TAREA 1: EL ACTA %d ENTERA, REGISTRADA"
      % (VUELTA_QUE_ESCRIBE, VUELTA_DEL_ACTA))
    w("=" * 78)
    w("")

    lineas, rango, err = cuerpo_del_acta()
    if err:
        w(err)
        print(NL.join(salida))
        return 1
    inicio, fin = rango
    w("A) EL CUERPO DEL ACTA, ACOTADO ANTES DE CONTAR NADA")
    w("   acta %d: docs/loop/ACTA_AUDITOR.md, lineas %d a %d (%d lineas)"
      % (VUELTA_DEL_ACTA, inicio, fin, fin - inicio + 1))
    w("   docs/loop/ACTA_AUDITOR.md -> disco %d bytes" % os.path.getsize(ACTA))
    secciones = secciones_del_acta(lineas, inicio, fin)
    w("   SECCIONES `## n.` DEL ACTA, LEIDAS Y NO TECLEADAS: %s" % _lista(secciones))
    w("")

    w("B) LA IDEMPOTENCIA, COMPROBADA ANTES DE MEDIR NADA MAS Y POR EL ACTA")
    w("   (la maquina se IMPORTA del registrador de la 189: `marcas_del_acta` y")
    w("    `entradas_que_registran`. No se re escribe una copia)")
    sedes = {}
    for ruta in SERIE.SEDES:
        rel = os.path.relpath(ruta, RAIZ).replace("\\", "/")
        sedes[rel] = io.open(ruta, encoding="utf-8", errors="replace").read()
    marca_t, marca_c = marcas_del_acta(VUELTA_DEL_ACTA)
    w("   las DOS sedes que se miran: %s" % ", ".join(sorted(sedes)))
    w("   las DOS marcas literales, computadas de la vuelta y no tecleadas:")
    w("      %r" % marca_t)
    w("      %r" % marca_c)
    ya = entradas_que_registran(VUELTA_DEL_ACTA, sedes)
    w("   CIFRA lineas que ya registran el acta %d: %d" % (VUELTA_DEL_ACTA, len(ya)))
    for r, i, mk, t in ya:
        w("      %s:%d %r" % (r, i, t[:100]))
    w("   CIFRA bytes de docs/PENDIENTES.md ANTES de tocar nada: %d"
      % os.path.getsize(SEDE))
    w("")

    w("C) LAS ADJUDICACIONES, CONTADAS CON LOS DOS PATRONES Y NO TECLEADAS")
    claves = claves_de_adjudicacion(lineas, inicio, fin, PREFIJO_ADJ)
    entrecomilladas = claves_entrecomilladas(lineas, inicio, fin, PREFIJO_ADJ)
    w("   patron SIN comillas inversas -> %d" % len(claves))
    for clave, cuantas in claves:
        w("      %s -> %d aparicion(es)" % (clave, cuantas))
    w("   patron CON comillas inversas (el del acta 188) -> %d" % len(entrecomilladas))
    dobles = [c for c, n in claves if n != 1]
    if dobles:
        w("   PARADA: hay claves repetidas dentro del acta: %s" % ", ".join(dobles))
        print(NL.join(salida))
        return 1
    if not claves:
        w("   PARADA: ningun patron encuentra adjudicaciones y el acta 190 declara")
        w("   diez. No se escribe una entrada con cero.")
        print(NL.join(salida))
        return 1
    w("")

    w("D) EL TITULO LITERAL DE CADA ADJUDICACION, SU FAMILIA Y SU ESTADO")
    w("   (LA MARCA `EN CONTRA` SE BUSCA ANTES QUE `A FAVOR`, y las dos cifras se")
    w("    publican por separado. El registrador de la 189 no conocia `EN CONTRA` y")
    w("    ademas PARABA si algun discutible no llevaba `A FAVOR`)")
    adjudicaciones = []
    for clave, _n in claves:
        pat = re.compile(r"^\s*\*\*%s " % re.escape(clave))
        res, err2 = titulo_de_la_negrita(lineas, inicio, fin, pat, clave)
        if err2:
            w("   %s -> %s" % (clave, err2))
            print(NL.join(salida))
            return 1
        ln, tit = res
        adjudicaciones.append((clave, familia_de_la_adjudicacion(tit),
                               estado_de_la_adjudicacion(tit), ln, tit))
        w("   %-5s linea %-6d [%s / %s]" % (clave, ln, adjudicaciones[-1][1],
                                            adjudicaciones[-1][2]))
        w("         %s" % tit[:150])
    sin_decir = [c for c, _f, e, _l, _t in adjudicaciones if e == "SIN DECIR"]
    if sin_decir:
        w("   PARADA: %s esta en un estado que este registrador NO SABE LEER."
          % ", ".join(sin_decir))
        print(NL.join(salida))
        return 1
    discutibles = [a for a in adjudicaciones if a[1] == "DISCUTIBLE"]
    preguntas = [a for a in adjudicaciones if a[1] == "PREGUNTA"]
    otras = [a for a in adjudicaciones if a[1] == "OTRA"]
    a_favor = [a for a in discutibles if a[2] == "A FAVOR"]
    en_contra = [a for a in discutibles if a[2] == "EN CONTRA"]
    w("   REPARTO POR FAMILIA: discutibles %d | preguntas %d | otras %d"
      % (len(discutibles), len(preguntas), len(otras)))
    w("   DE LOS DISCUTIBLES: A FAVOR %d | EN CONTRA %d | otro estado %d"
      % (len(a_favor), len(en_contra),
         len(discutibles) - len(a_favor) - len(en_contra)))
    for a in en_contra:
        w("      EN CONTRA: %s -> %s" % (a[0], a[4][:120]))
    if len(a_favor) + len(en_contra) != len(discutibles):
        w("   PARADA: hay discutibles cuyo estado no es ni A FAVOR ni EN CONTRA.")
        print(NL.join(salida))
        return 1
    if not en_contra:
        w("   PARADA: ningun discutible sale EN CONTRA y el acta 190 declara uno, el")
        w("   `D.5`. Si la marca no se ve, la cuenta seria la de la vuelta pasada.")
        print(NL.join(salida))
        return 1
    if not preguntas:
        w("   PARADA: ninguna adjudicacion nombra un `P.n` y el acta 190 declara TRES")
        w("   preguntas contestadas. No se escribe una lista vacia.")
        print(NL.join(salida))
        return 1
    w("")

    w("E) LOS HALLAZGOS DE LA SECCION %d, Y CUALES CUENTAN FUERA DEL MARCADO"
      % SECCION_DE_LOS_HALLAZGOS)
    claves_h = claves_de_adjudicacion(lineas, inicio, fin, PREFIJO_HALLAZGO)
    hallazgos = []
    for clave, _n in claves_h:
        pat = re.compile(r"^\s*\*\*%s " % re.escape(clave))
        res, err3 = titulo_de_la_negrita(lineas, inicio, fin, pat, clave)
        if err3:
            w("   %s -> %s" % (clave, err3))
            print(NL.join(salida))
            return 1
        hallazgos.append((clave, res[0], res[1]))
        w("   %-5s linea %-6d %s" % (clave, res[0], res[1][:120]))
    if not hallazgos:
        w("   PARADA: la seccion %d no trae ninguna clave `5.n`."
          % SECCION_DE_LOS_HALLAZGOS)
        print(NL.join(salida))
        return 1
    fila_fuera = fila_de_la_metrica(lineas, inicio, fin, AGUJA_FILA_FUERA)
    for ln, txt in fila_fuera:
        w("   LA FILA QUE DECIDE (linea %d): %s" % (ln, txt))
    if len(fila_fuera) != 1:
        w("   PARADA: la fila %r aparece %d veces en la tabla de credito."
          % (AGUJA_FILA_FUERA, len(fila_fuera)))
        print(NL.join(salida))
        return 1
    nombrados, sueltos, piezas = hallazgos_que_la_tabla_nombra(hallazgos,
                                                               fila_fuera[0][1])
    w("   PIEZAS DEL PARENTESIS, NORMALIZADAS: %s"
      % ", ".join(repr(x) for x in piezas))
    w("   CIFRA hallazgos que la tabla NOMBRA: %d" % len(nombrados))
    for clave, ln, tit, casan in nombrados:
        w("      %s (linea %d) casa por %s" % (clave, ln, ", ".join(repr(x) for x in casan)))
    w("   CIFRA hallazgos que la tabla NO nombra: %d (%s)"
      % (len(sueltos), ", ".join(c for c, _l, _t in sueltos) or "ninguno"))
    if not nombrados:
        w("   PARADA: la fila de la tabla no casa con ningun hallazgo, y el acta")
        w("   declara dos. No se elige a ojo cual cuenta.")
        print(NL.join(salida))
        return 1
    w("")

    w("F) LAS CAIDAS, CON LA ATRIBUCION HECHA POR LA NEGRITA DE SU PARRAFO")
    r6 = rango_de_seccion(lineas, inicio, fin, SECCION_DE_LAS_CAIDAS)
    if r6 is None:
        w("   PARADA: el acta no tiene seccion %d." % SECCION_DE_LAS_CAIDAS)
        print(NL.join(salida))
        return 1
    ini6, fin6 = r6
    cabecera6 = lineas[ini6 - 1].strip()
    w("   la seccion %d va de la linea %d a la %d" % (SECCION_DE_LAS_CAIDAS, ini6, fin6))
    w("   SU CABECERA, LITERAL: %r" % cabecera6)
    n_c_crudo = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_C)
    n_c_espacio = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_C_ESPACIO)
    l_aud_a = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_AUDITOR_A)
    l_rep = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_REPORTE)
    l_eje_v = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_EJECUTOR_VIEJO)
    w("   patron `C.n` de la 187 (coma o punto pegados): %d" % len(n_c_crudo))
    w("   patron `C.n` de la 188 (admite tambien un espacio): %d" % len(n_c_espacio))
    w("   patron `A.n` de cabecera de tercer nivel (acta 185): %d" % len(l_aud_a))
    w("   patron `R.n` de caida de reporte: %d" % len(l_rep))
    w("   patron `E.n` de las actas 182 y 184: %d" % len(l_eje_v))
    w("   Y LA MAQUINA DE LA 189 SOBRE ESTA SECCION, QUE ES LA QUE NO PUEDE:")
    viejo = caidas_por_seccion(lineas, ini6, fin6)
    w("      caidas_por_seccion(): ejecutor %d | auditor %d | huerfanas %d"
      % (len(viejo[0]), len(viejo[1]), len(viejo[2])))
    w("      (su patron es de cabeza de linea, y las `C.n` del acta 190 van DENTRO")
    w("       de un parrafo, asi que no ve ninguna; y su cabecera de seccion no")
    w("       dice de quien son)")
    c_eje, c_aud, huerfanas = caidas_en_linea(lineas, ini6, fin6)
    w("   CON LA MAQUINA DE ESTA VUELTA (`C.n` en linea + negrita del parrafo):")
    w("      DEL EJECUTOR: %d" % len(c_eje))
    for ln, num, neg in c_eje:
        w("         C.%d en el parrafo de la linea %d, bajo la negrita %r"
          % (num, ln, neg[:70]))
    w("      DEL AUDITOR: %d" % len(c_aud))
    for ln, num, neg in c_aud:
        w("         C.%d en el parrafo de la linea %d, bajo la negrita %r"
          % (num, ln, neg[:70]))
    w("      HUERFANAS: %d" % len(huerfanas))
    for ln, num, neg in huerfanas:
        w("         C.%d en el parrafo de la linea %d, bajo la negrita %r"
          % (num, ln, neg[:70]))
    if huerfanas:
        w("   PARADA: hay %d caida(s) `C.n` en un parrafo cuya negrita no dice de"
          % len(huerfanas))
        w("   quien son. Una caida sin dueno no se reparte a ojo.")
        print(NL.join(salida))
        return 1
    if not c_eje:
        w("   PARADA: no se encuentra ninguna caida del ejecutor y el acta 190")
        w("   declara TRES en su seccion 6.")
        print(NL.join(salida))
        return 1
    w("")

    w("G) LAS DOS ESPECIES DE CERO, SEPARADAS Y MEDIDAS")
    confundido = caidas_en_linea(lineas, ini6, fin6,
                                 marcas_cero_cuenta=(MARCAS_CERO_DE_CUENTA
                                                     + MARCAS_CERO_DE_RACHA))
    w("   marcas de CERO DE CUENTA (importadas de la 189, SI neutralizan): %s"
      % ", ".join(repr(x) for x in MARCAS_CERO_DE_CUENTA))
    w("   marcas de CERO DE RACHA (nuevas hoy, NO neutralizan): %s"
      % ", ".join(repr(x) for x in MARCAS_CERO_DE_RACHA))
    w("   CON LA SEPARACION PUESTA: ejecutor %d | auditor %d" % (len(c_eje), len(c_aud)))
    w("   TRATANDO EL CERO DE RACHA COMO CERO DE CUENTA: ejecutor %d | auditor %d"
      % (len(confundido[0]), len(confundido[1])))
    w("   O SEA QUE CONFUNDIRLAS BORRARIA %d CAIDA(S) DE LA CUENTA."
      % (len(c_eje) - len(confundido[0])))
    parrafos6 = parrafos_con_negrita(lineas, ini6, fin6)
    n_metodo = len([1 for _a, _b, _n, t in parrafos6
                    if MARCA_ESPECIE_METODO in t.upper()])
    w("   la marca de especie %r aparece en %d de los %d parrafos de la seccion"
      % (MARCA_ESPECIE_METODO, n_metodo, len(parrafos6)))
    if not n_metodo:
        w("   PARADA: ningun parrafo declara la especie de las caidas.")
        print(NL.join(salida))
        return 1
    w("")

    w("H) EL CERO DEL AUDITOR, CONTADO Y CON SU DECLARACION AL LADO")
    decl_cero_aud = [i for i in range(inicio, fin + 1)
                     if FRASE_CERO_AUDITOR in lineas[i - 1]]
    decl_cero_racha = [i for i in range(inicio, fin + 1)
                       if FRASE_CERO_RACHA_EJECUTOR in lineas[i - 1]]
    w("   CIFRA caidas propias del auditor que el reparto halla: %d" % len(c_aud))
    w("   la frase %r aparece en %d linea(s): %s"
      % (FRASE_CERO_AUDITOR, len(decl_cero_aud),
         ", ".join(str(x) for x in decl_cero_aud) or "ninguna"))
    for i in decl_cero_aud:
        w("      LINEA %d: %s" % (i, lineas[i - 1].strip()[:120]))
    w("   la frase %r aparece en %d linea(s): %s"
      % (FRASE_CERO_RACHA_EJECUTOR, len(decl_cero_racha),
         ", ".join(str(x) for x in decl_cero_racha) or "ninguna"))
    if not c_aud and not decl_cero_aud:
        w("   PARADA: cero caidas propias del auditor Y el acta no lo declara por la")
        w("   frase. Un cero de una maquina que no muerde no se publica desnudo.")
        print(NL.join(salida))
        return 1
    fila_aud = fila_de_la_metrica(lineas, inicio, fin, AGUJA_FILA_CAIDAS_AUDITOR)
    fila_metodo = fila_de_la_metrica(lineas, inicio, fin, AGUJA_FILA_CAIDAS_METODO)
    for ln, txt in fila_aud + fila_metodo:
        w("   POR LA TABLA (linea %d): %s" % (ln, txt))
    if not fila_aud or not fila_metodo:
        w("   PARADA: la tabla de credito no trae alguna de las dos filas de caidas.")
        print(NL.join(salida))
        return 1
    w("")

    w("I) LA VARA DE LA `5.4`, CON SUS CIFRAS LEIDAS DEL PARRAFO")
    r5 = rango_de_seccion(lineas, inicio, fin, SECCION_DE_LOS_HALLAZGOS)
    parrafo_vara = ""
    for a, _b, negrita, texto in parrafos_con_negrita(lineas, r5[0], r5[1]):
        if negrita.startswith("5.4 ") or texto.startswith("**5.4 "):
            parrafo_vara = texto
            break
    w("   parrafo de la 5.4, %d caracteres" % len(parrafo_vara))
    vara = cifras_de_la_vara(parrafo_vara)
    for etiqueta, valor, pat in vara:
        w("      %-34s %-6s (patron %r)" % (etiqueta, valor, pat))
    sin_leer = [e for e, v, _p in vara if v is None]
    if sin_leer:
        w("   PARADA: %d cifra(s) de la vara no se pudieron leer del parrafo: %s."
          % (len(sin_leer), ", ".join(sin_leer)))
        w("   Una cifra que no se puede leer no se inventa.")
        print(NL.join(salida))
        return 1
    VARA_TXT = os.path.join(LOOP, "_auditor_v190_vara.txt")
    vara_bd = vara_bl = -1
    if os.path.exists(VARA_TXT):
        datos = io.open(VARA_TXT, "rb").read()
        vara_bd = len(datos)
        vara_bl = len(datos.replace(b"\r\n", b"\n"))
        w("   docs/loop/_auditor_v190_vara.txt -> disco %d bytes | LF %d bytes"
          % (vara_bd, vara_bl))
        t_vara = datos.decode("utf-8", errors="replace")
        w("   CIFRA menciones de `OP-L-02` en esa salida: %d" % t_vara.count("OP-L-02"))
    else:
        w("   docs/loop/_auditor_v190_vara.txt -> NO EXISTE")
    w("")

    w("J) EL NUMERO DE LA ENTRADA, QUE NO SE TECLEA")
    halladas = SERIE.entradas()
    numero = SERIE.siguiente_libre(halladas)
    w("   serie recomputada de sus dos sedes: %d entradas" % len(halladas))
    w("   CIFRA colisiones: %d | CIFRA huecos: %d"
      % (len(SERIE.colisiones(halladas)), len(SERIE.huecos(halladas))))
    w("   SIGUIENTE LIBRE: R.%d" % numero)
    w("")

    w("K) LA DEUDA DE LA SERIE, QUE ES EL HALLAZGO 5.2, REMEDIDA AQUI")
    salto = actas_sin_entrada(halladas, 173, VUELTA_DEL_ACTA - 1)
    faltan, bajo, alto = salto
    w("   tramo mirado: actas 173 a %d" % (VUELTA_DEL_ACTA - 1))
    w("   CIFRA actas SIN entrada propia en la serie: %d" % len(faltan))
    w("   LAS QUE FALTAN: %s" % (", ".join(str(x) for x in faltan) or "(ninguna)"))
    w("   EXTREMO BAJO: %s"
      % ("R.%d cubre el acta %d" % bajo if bajo else "(ninguno)"))
    w("   EXTREMO ALTO: %s"
      % ("R.%d cubre el acta %d" % alto if alto else "(ninguno)"))
    w("   el acta 190 publica 8 en su 5.2 -> %s"
      % ("CALZA" if len(faltan) == 8 else "NO CALZA, y la discrepancia se declara"))
    w("")

    medido = {
        "inicio": inicio, "fin": fin, "secciones": secciones,
        "n_adj": len(claves), "n_entrecomillado": len(entrecomilladas),
        "adjudicaciones": adjudicaciones,
        "n_discutibles": len(discutibles), "n_preg": len(preguntas),
        "n_otras": len(otras), "n_a_favor_discutibles": len(a_favor),
        "n_en_contra_discutibles": len(en_contra),
        "en_contra_nombrados": [
            (c, re.search(r"`D\.\d+`", t).group(0).strip("`"))
            for c, _f, _e, _l, t in en_contra],
        "preguntas": [(c, PAT_P_DEL_TITULO.search(t).group(0).strip("`"))
                      for c, _f, _e, _l, t in preguntas],
        "hallazgos": hallazgos, "n_hall": len(hallazgos),
        "hall_nombrados": nombrados,
        "claves_nombradas": set(c for c, _l, _t, _k in nombrados),
        "piezas_fuera": piezas, "fila_fuera": fila_fuera,
        "cabecera_seccion6": cabecera6,
        "c_eje": c_eje, "c_aud": c_aud,
        "n_eje": len(c_eje), "n_aud": len(c_aud), "n_huerf": len(huerfanas),
        "viejo_eje": len(viejo[0]), "viejo_aud": len(viejo[1]),
        "viejo_huerf": len(viejo[2]),
        "cero_confundido_eje": len(confundido[0]),
        "cero_confundido_aud": len(confundido[1]),
        "n_parrafos_metodo": n_metodo,
        "n_c_crudo": len(n_c_crudo), "n_c_espacio": len(n_c_espacio),
        "n_a": len(l_aud_a), "n_rep": len(l_rep), "n_eje_viejo": len(l_eje_v),
        "decl_cero_aud": decl_cero_aud,
        "fila_aud": fila_aud, "fila_metodo": fila_metodo,
        "vara": vara, "vara_bytes_disco": vara_bd, "vara_bytes_lf": vara_bl,
        "salto": salto, "numero": numero, "ya_registrada": len(ya),
        "sedes": sedes,
    }
    return salida, medido


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true",
                    help="mide y arma la entrada, pero NO escribe en la sede")
    ap.add_argument("--mutacion", action="store_true",
                    help="corre el caso positivo por mutacion y no toca nada")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    if a.mutacion:
        return prueba_de_mutacion()

    medido = _medir()
    if isinstance(medido, int):
        return medido
    salida, m = medido
    w = salida.append

    w("L) EL TITULO, CON SUS CINCO NUMERALES COMPUTADOS")
    titulo = titulo_de_la_entrada(m["n_adj"], m["n_hall"], m["n_preg"],
                                  m["n_aud"], m["n_eje"])
    w("   %s" % titulo)
    w("")

    numero = m["numero"]
    entrada = armar_entrada(numero, titulo, m)
    w("M) LA ENTRADA ARMADA")
    w("   %d bytes | %d lineas" % (len(entrada.encode("utf-8")), entrada.count(NL)))
    w("   guiones largos o medios en la entrada: %d"
      % (entrada.count(chr(8212)) + entrada.count(chr(8211))))
    w("")

    texto_sede = io.open(SEDE, encoding="utf-8").read().replace(chr(13) + NL, NL)
    if a.simular:
        w("N) MODO --simular: NO SE ESCRIBE NADA EN LA SEDE.")
        w("")
        w("LA ENTRADA, ENTERA:")
        for l in entrada.split(NL):
            w("   | " + l)
    elif m["ya_registrada"]:
        w("N) NO SE ESCRIBE NADA, Y ESTA ES LA IDEMPOTENCIA HACIENDO SU TRABAJO.")
        w("   el acta %d YA TIENE ENTRADA en la serie: %d linea(s) la nombran."
          % (VUELTA_DEL_ACTA, m["ya_registrada"]))
        w("   NO se escribe una entrada nueva y NO se consume el numero R.%d." % numero)
        w("   docs/PENDIENTES.md sigue en %d bytes." % os.path.getsize(SEDE))
    else:
        nuevo = texto_sede.rstrip(NL) + NL + NL + entrada
        io.open(SEDE, "w", encoding="utf-8", newline=NL).write(nuevo)
        w("N) ESCRITA EN docs/PENDIENTES.md")
        w("   la sede pasa de %d a %d bytes"
          % (len(texto_sede.encode("utf-8")), len(nuevo.encode("utf-8"))))
        rele = io.open(SEDE, encoding="utf-8").read().replace(chr(13) + NL, NL)
        w("   RELEIDA DEL DISCO: la entrada esta byte a byte: %s"
          % ("SI" if entrada.rstrip(NL) in rele else "NO"))
        de_nuevo = SERIE.entradas()
        w("   SERIE RECOMPUTADA DESPUES DE ESCRIBIR: %d entradas, siguiente libre R.%d"
          % (len(de_nuevo), SERIE.siguiente_libre(de_nuevo)))
        w("   CIFRA colisiones: %d | CIFRA huecos: %d"
          % (len(SERIE.colisiones(de_nuevo)), len(SERIE.huecos(de_nuevo))))
        sedes2 = {}
        for ruta in SERIE.SEDES:
            rel = os.path.relpath(ruta, RAIZ).replace("\\", "/")
            sedes2[rel] = io.open(ruta, encoding="utf-8", errors="replace").read()
        w("   Y LA IDEMPOTENCIA, REMEDIDA DESPUES DE ESCRIBIR: el acta %d aparece en"
          % VUELTA_DEL_ACTA)
        w("   %d linea(s), asi que un RE CORRIDO de este instrumento no escribiria"
          % len(entradas_que_registran(VUELTA_DEL_ACTA, sedes2)))
        w("   nada.")
    w("")
    t = NL.join(salida) + NL
    # EL NOMBRE DE LA SALIDA DICE LO QUE PASO, Y NO LO CONTRARIO (`EJECUTOR.md` 1,
    # LA RUTA QUE PROMETE PRUEBA ES CIFRA). Cuando la idempotencia muerde, `numero`
    # es un numero que NO se consumio, y nombrar el fichero con el seria escribir
    # una cifra falsa en una ruta.
    if a.simular:
        nombre = "SALIDA_V%s_T1A_SIMULACION.txt" % SUFIJO_QUE_ESCRIBE
    elif m["ya_registrada"]:
        nombre = "SALIDA_V%s_T1A_RECORRIDO_SIN_ESCRIBIR.txt" % SUFIJO_QUE_ESCRIBE
    else:
        nombre = "SALIDA_V%s_T1A_REGISTRO_R%d.txt" % (SUFIJO_QUE_ESCRIBE, numero)
    ruta = os.path.join(LOOP, nombre)
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
