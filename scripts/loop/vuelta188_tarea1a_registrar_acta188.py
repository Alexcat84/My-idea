# -*- coding: utf-8 -*-
r"""vuelta188_tarea1a_registrar_acta188.py . EL ACTA 188 ENTERA, REGISTRADA EN LA
SERIE `R.N` EN LA FORMA DE LA CASA.

LA MAQUINA NO SE CLONA, SE IMPORTA, y eso lo adjudico la `6.6` del acta 172 como
correcto y obligatorio. De `scripts/loop/vuelta187_tarea1a_registrar_acta187.py`
se importan `cuerpo_del_acta`, `seccion_que_contiene`, `preguntas_de_la_seccion7`,
`_titulos_de` y `PAT_CAIDA_C`; y por su cadena llegan `titulo_de_la_negrita`,
`claves_entrecomilladas`, `cuenta_por_patron`, `claves_de_adjudicacion`,
`actas_sin_entrada`, `PALABRA_CON_CERO`, `parrafo_de`,
`cabecera_de_la_seccion` y `lineas_que_declaran_cero_caidas`. **Lo unico propio
de este fichero son LAS DOS COSAS QUE EL ACTA 188 ESTRENA, LOS DOS ESTADOS NUEVOS
QUE SU SECCION 6 NECESITA, Y SUS GLOSAS.**

POR QUE HACE FALTA CODIGO PROPIO OTRA VEZ, MEDIDO Y NO SUPUESTO. Son CUATRO
cosas, y las cuatro salen de correr el registrador de la 187 sobre el acta 188:

  1) LA ATRIBUCION DE UNA SECCION DE CAIDAS MIXTA. La seccion 8 del acta 188
     lleva CUATRO caidas bajo UNA cabecera: `C.1` y `C.2` **declaradas por el
     ejecutor** y `C.3` y `C.4` **levantadas por el auditor**. **Las cuatro son
     DEL EJECUTOR**, porque la atribucion la hace LA CABECERA y no quien las
     encontro. Eso ya lo sabia hacer el registrador de la 187; lo que NO sabia es
     leer ESTA cabecera.

  2) Y AQUI VA UNA DISCREPANCIA MEDIDA QUE SE DECLARA EN VEZ DE RESOLVERSE
     COPIANDO (`EJECUTOR.md` 2). El encargo de la 188 dice, con estas palabras,
     que *"la seccion que las contiene lo dice en su cabecera"*. **Lo medi antes
     de creerlo y la cabecera literal NO contiene la palabra `EJECUTOR`**: dice
     `## 8. LAS CAIDAS, LAS SUYAS DECLARADAS Y LAS DOS QUE LEVANTO YO`. Con el
     vocabulario de la 187 (`EJECUTOR` o `MI CAIDA`) esa cabecera sale SIN DUENO
     y las cuatro caidas salen HUERFANAS, que es PARADA. **Asi que la cabecera SI
     dice de quien son, pero con otras palabras**: `LAS SUYAS`, que en un acta
     que el auditor escribe SOBRE el ejecutor son las del ejecutor. **Se anade
     esa marca LITERAL, leida del acta de hoy, y la vieja se conserva intacta y
     su cifra se publica al lado.** Las dos cuentas van en la entrada.

  3) EL ESTADO DE LOS `6.n` NECESITA DOS MARCAS NUEVAS, Y LAS DOS SON LITERALES
     DEL ACTA 188. El `6.2` dice *"`PD.8` NACE Y LA DEJO ABIERTA"* y el `6.3`
     dice *"LAS TRES MESAS ANOTADAS SIGUEN ANOTADAS Y NO SE ABREN"*. Con el
     vocabulario heredado (`SIGUE ABIERTA`, `ADJUDICAD`, `NO LO CONVIERTO EN
     UNO`, `NO ES UN PENDIENTE DE DOCTRINA`) los dos salen `SIN DECIR`, que es
     PARADA. **La PARADA se conserva entera**: un titulo que no diga NINGUNA de
     las marcas sigue saliendo `SIN DECIR` y sigue parando, y eso se prueba por
     mutacion.

  4) UNA CAIDA PUEDE NO ACUMULAR PARA NINGUNA RACHA, Y ESO NO ES LO MISMO QUE NO
     EXISTIR. El acta 188 registra CUATRO caidas del ejecutor y **CERO** que
     acumulen: las cuatro son DE METODO. **Las dos cifras se publican juntas y se
     dice por que difieren**, en vez de publicar solo la del cero (que diria que
     no paso nada) o solo la del cuatro (que diria que alguna racha subio).

LAS CIFRAS DEL TITULO NO SE TECLEAN: se cuentan del acta acotada. Ni el numero de
la entrada: lo devuelve `scripts/loop/serie_de_registros.py` recomputando la serie
de sus DOS sedes. **`R.50` NO se da por bueno porque lo diga la apertura.** Y LA
DEUDA DE LA SERIE SE REMIDE EN ESTA VUELTA y no se hereda del `R.49`.

LOS CINCO PUESTOS DE LA `PD.1` NO SE TECLEAN tampoco: se leen del parrafo del
`6.n` que el propio titulo declara ABIERTO, y si el acta dijera otros, la entrada
diria otros.

LO QUE ESTE FICHERO NO HACE: no toca el acta, no toca el reporte, no toca
`docs/plan/`, no corre la bateria y no escribe ningun veredicto. Escribe UNA
entrada en UNA sede, y si la entrada ya esta, NO la duplica y lo dice.

USO:
  python scripts/loop/vuelta188_tarea1a_registrar_acta188.py
  python scripts/loop/vuelta188_tarea1a_registrar_acta188.py --simular
  python scripts/loop/vuelta188_tarea1a_registrar_acta188.py --mutacion
"""
import argparse
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import serie_de_registros as SERIE   # noqa: E402
from vuelta172_tarea1_registrar_acta171 import titulo_de_la_negrita   # noqa: E402
from vuelta182_tarea1a_registrar_acta181 import (   # noqa: E402
    claves_de_adjudicacion, cuenta_por_patron)
from vuelta183_tarea1a_registrar_acta182 import actas_sin_entrada   # noqa: E402
from vuelta184_tarea1a_registrar_acta184 import claves_entrecomilladas   # noqa: E402
from vuelta186_tarea1a_registrar_acta186 import (   # noqa: E402
    PALABRA_CON_CERO, cabecera_de_la_seccion, lineas_que_declaran_cero_caidas,
    parrafo_de, FRASE_CERO_CAIDAS_PROPIAS, FRASE_SIN_CAIDA_PROPIA,
    MARCA_ABIERTA, MARCA_ANOTACION, MARCA_CERRADA, MARCA_CONTESTADAS,
    PAT_CAIDA_AUDITOR_A, PAT_CAIDA_EJECUTOR_VIEJO, PAT_CAIDA_REPORTE,
    PAT_PD_DEL_TITULO, PAT_P_DEL_TITULO)
from vuelta187_tarea1a_registrar_acta187 import (   # noqa: E402
    MARCA_CORRECCION, PAT_CAIDA_C, seccion_que_contiene)

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")
SEDE = os.path.join(RAIZ, "docs", "PENDIENTES.md")
NL = chr(10)

VUELTA_DEL_ACTA = 188
VUELTA_QUE_ESCRIBE = 188
SUFIJO_QUE_ESCRIBE = "188"
CABECERA_ACTA = "# ACTA DEL AUDITOR, VUELTA %d" % VUELTA_DEL_ACTA
PREFIJO_ADJ = "5."
PREFIJO_PD = "6."
PREFIJO_PREG = "7."

# LAS DOS MARCAS DE ESTADO QUE NACEN EN ESTA VUELTA, LITERALES DEL ACTA 188 Y NO
# PARAFRASEADAS. Se ANADEN a las cuatro heredadas; ninguna de las cuatro se
# ensancha ni se toca, y la cifra del vocabulario viejo se publica al lado.
MARCA_ABIERTA_2 = "LA DEJO ABIERTA"        # titulo del `6.2` del acta 188
MARCA_ANOTACION_2 = "SIGUEN ANOTADAS"      # titulo del `6.3` del acta 188

# EL VOCABULARIO DE LA CABECERA QUE ATRIBUYE UNA CAIDA. `LAS SUYAS` nace en esta
# vuelta y es literal de la cabecera de la seccion 8 del acta 188.
MARCAS_DUENO_EJECUTOR = ("EJECUTOR", "LAS SUYAS")
MARCAS_DUENO_AUDITOR = ("MI CAIDA",)

# EL PATRON DE LA CAIDA `C.n` QUE ESTA VUELTA ANADE, Y POR QUE. El heredado
# (`PAT_CAIDA_C`, de la vuelta 187) exige una COMA O UN PUNTO pegados al numeral:
# ``**`C.3`,``. El acta 188 escribe sus dos primeras con un ESPACIO detras
# (``**`C.1` DEL EJECUTOR, DECLARADA POR EL:``), asi que el patron viejo, corrido
# sobre esta acta, encuentra DOS de las CUATRO. **Se anade un patron; el viejo se
# conserva intacto y su cifra se publica al lado.** La diferencia entre anadir y
# ensanchar es la que el acta 184 adjudico a favor en su `5.3`.
PAT_CAIDA_C_ESPACIO = re.compile(r"^\s*(?:-\s+)?\*\*`?C\.(\d+)`?[,.\s]")

# LAS MARCAS CON LAS QUE EL BLOQUE DE UNA CAIDA DECLARA QUE NO ACUMULA. Literales
# del acta 188. La busqueda se hace sobre el bloque EN MAYUSCULAS, porque el acta
# escribe `NO ACUMULA` en la negrita del titulo y `no acumula` en la prosa.
MARCAS_NO_ACUMULA = ("NO ACUMULA", "NO LA METO EN NINGUNA RACHA")


def cuerpo_del_acta(texto=None):
    """EL ACTA ACOTADA: (lineas, (inicio, fin), error). PURA cuando se le pasa
    `texto`, que es lo que permite que el caso positivo por mutacion la corra
    sobre un acta FABRICADA sin tocar el repo.

    NO SE IMPORTA la del registrador de la 187 porque aquella lleva `CABECERA_187`
    clavada en una constante de modulo; aqui la frontera es la del acta 188. El
    cuerpo de la funcion es el mismo y se declara como CLON."""
    if texto is None:
        texto = io.open(ACTA, encoding="utf-8").read()
    texto = texto.replace(chr(13) + NL, NL)
    lineas = texto.split(NL)
    cabeceras = [i for i, l in enumerate(lineas, 1)
                 if l.startswith("# ACTA DEL AUDITOR, VUELTA ")]
    mias = [i for i in cabeceras if lineas[i - 1].startswith(CABECERA_ACTA)]
    if len(mias) != 1:
        return None, None, "PARADA: %r aparece %d veces." % (CABECERA_ACTA, len(mias))
    inicio = mias[0]
    posteriores = [i for i in cabeceras if i > inicio]
    fin = (min(posteriores) - 1) if posteriores else len(lineas)
    return lineas, (inicio, fin), None


def caidas_c_por_seccion(lineas, inicio, fin, marcas_eje=None, marcas_aud=None,
                         patron=None):
    """LAS CAIDAS `C.n` DEL ACTA, REPARTIDAS POR EL DUENO QUE DECLARA LA CABECERA
    DE SU SECCION. Devuelve (del_ejecutor, del_auditor, sin_dueno), tres listas
    de (linea, numero, cabecera). PURA.

    LOS DOS VOCABULARIOS SON PARAMETRO, no constantes escondidas, para que el
    caso positivo por mutacion pueda correr la version VIEJA y la NUEVA sobre el
    MISMO texto y publicar las dos cifras. Con los valores por defecto se
    comporta como la nueva.

    LA PRECEDENCIA ESTA ESCRITA Y NO ES UN DESCUIDO: si la cabecera trae una
    marca de EJECUTOR, la caida es del ejecutor **aunque la cabecera diga ademas
    que la levanto el auditor**. Es exactamente el caso del acta 188, cuya
    cabecera dice *"LAS SUYAS DECLARADAS Y LAS DOS QUE LEVANTO YO"* y cuyas
    cuatro caidas son del ejecutor. **La atribucion la hace la cabecera y no
    quien encontro la caida.**

    Una `C.n` cuya seccion no diga ni una cosa ni la otra sale en `sin_dueno` y
    quien llama hace PARADA. **Repartir a ojo una caida sin dueno es exactamente
    lo que esta funcion existe para impedir**, y esa PARADA se conserva entera."""
    m_eje = tuple(marcas_eje) if marcas_eje is not None else MARCAS_DUENO_EJECUTOR
    m_aud = tuple(marcas_aud) if marcas_aud is not None else MARCAS_DUENO_AUDITOR
    pat = patron if patron is not None else PAT_CAIDA_C_ESPACIO
    eje, aud, huerfanas = [], [], []
    for i in range(inicio, fin + 1):
        m = pat.match(lineas[i - 1])
        if not m:
            continue
        _ln, cab = seccion_que_contiene(lineas, inicio, fin, i)
        fila = (i, int(m.group(1)), cab)
        alta = cab.upper()
        if any(x in alta for x in m_eje):
            eje.append(fila)
        elif any(x in alta for x in m_aud):
            aud.append(fila)
        else:
            huerfanas.append(fila)
    return eje, aud, huerfanas


def bloque_de_la_caida(lineas, ln, fin, patron=None):
    """EL BLOQUE ENTERO DE UNA CAIDA: desde su linea hasta la siguiente caida o la
    siguiente cabecera `## `, lo que llegue antes. Devuelve el texto unido por
    espacios. PURA.

    NO SE USA `parrafo_de()`, Y ESO SE MIDIO ANTES DE DECIDIRLO. `parrafo_de()`
    se para en la primera linea vacia, y en el acta 188 la declaracion de que una
    caida NO ACUMULA vive DOS parrafos mas abajo de su titulo (la `C.3` la escribe
    bajo *"LA ESPECIE Y SI ACUMULA"*). Leyendo solo el primer parrafo, las cuatro
    salian como QUE ACUMULAN, que es exactamente la cifra falsa que este
    instrumento existe para no publicar."""
    pat = patron if patron is not None else PAT_CAIDA_C_ESPACIO
    trozos = []
    for i in range(ln + 1, fin + 1):
        l = lineas[i - 1]
        if l.startswith("## ") or pat.match(l):
            break
        trozos.append(l.strip())
    return " ".join([lineas[ln - 1].strip()] + trozos)


def acumulan(lineas, fin, caidas, patron=None):
    """DE UNAS CAIDAS YA LOCALIZADAS, CUALES ACUMULAN PARA ALGUNA RACHA.

    Devuelve (las_que_acumulan, las_que_no), dos listas de (linea, numero). PURA.

    NO SE TECLEA NINGUNA: se lee EL BLOQUE ENTERO de cada caida y se busca en el
    una de las marcas literales con que el acta declara que no acumula. **Una
    caida cuyo bloque no diga nada se cuenta como QUE ACUMULA**, que es el lado
    seguro: dar por bueno el silencio seria aflojar una racha sin que nadie lo
    escribiera."""
    si, no = [], []
    for ln, num, _cab in caidas:
        bloque = bloque_de_la_caida(lineas, ln, fin, patron).upper()
        if any(x in bloque for x in MARCAS_NO_ACUMULA):
            no.append((ln, num))
        else:
            si.append((ln, num))
    return si, no


def pendientes_de_doctrina(lineas, inicio, fin, titulos, vocabulario_viejo=False):
    """LOS `6.n` DE LA SECCION 6, CON SU ESTADO LEIDO DEL TITULO. Devuelve
    [(clave, pd, estado, linea, titulo)]. PURA.

    EL ESTADO NO SE TECLEA: sale de buscar en el titulo literal, EN ESTE ORDEN,
    `NO ES UN PENDIENTE DE DOCTRINA` (CORRECCION POR DECLARACION), `NO LO
    CONVIERTO EN UNO` o `SIGUEN ANOTADAS` (ANOTACION), `SIGUE ABIERTA` o `LA DEJO
    ABIERTA` (ABIERTA), o `ADJUDICAD` (CERRADA). **Si un titulo no dijera ninguna
    de las seis, el estado sale como `SIN DECIR` y el instrumento hace PARADA en
    vez de suponer.**

    `vocabulario_viejo=True` corre con las CUATRO marcas de la 187 y sin las dos
    nuevas. Existe para que el caso positivo por mutacion pueda publicar LAS DOS
    cifras sobre el mismo texto: la vieja saca `SIN DECIR` en dos de los tres
    numerales del acta 188, y esa es la medicion que prueba que las marcas nuevas
    hacian falta. **Se anaden marcas, no se ensancha ninguna hasta que trague.**"""
    marcas_anot = (MARCA_ANOTACION,) if vocabulario_viejo else (
        MARCA_ANOTACION, MARCA_ANOTACION_2)
    marcas_abie = (MARCA_ABIERTA,) if vocabulario_viejo else (
        MARCA_ABIERTA, MARCA_ABIERTA_2)
    salida = []
    for clave, _n in claves_entrecomilladas(lineas, inicio, fin, PREFIJO_PD):
        ln, tit = titulos[clave]
        m = PAT_PD_DEL_TITULO.search(tit)
        pd = ("PD.%s" % m.group(1)) if m else "(sin PD en el titulo)"
        if MARCA_CORRECCION in tit:
            estado = "CORRECCION POR DECLARACION"
        elif any(x in tit for x in marcas_anot):
            estado = "ANOTACION"
        elif any(x in tit for x in marcas_abie):
            estado = "ABIERTA"
        elif MARCA_CERRADA in tit:
            estado = "CERRADA"
        else:
            estado = "SIN DECIR"
        salida.append((clave, pd, estado, ln, tit))
    return salida


def preguntas_de_la_seccion7(lineas, inicio, fin, titulos):
    """LAS PREGUNTAS DE LA SECCION 7, CON SU ESTADO LEIDO DE LA CABECERA DE LA
    PROPIA SECCION. Devuelve (lista, estado, linea_de_la_cabecera, cabecera).
    PURA. Identica en forma a la de la 187: el estado sale de `LAS CONTESTO` en
    la cabecera literal, y si no lo dice, sale `SIN DECIR` y quien llama para."""
    ln_cab, cab = cabecera_de_la_seccion(lineas, inicio, fin, 7)
    estado = "CONTESTADA" if (cab and MARCA_CONTESTADAS in cab) else "SIN DECIR"
    lista = []
    for clave, _n in claves_entrecomilladas(lineas, inicio, fin, PREFIJO_PREG):
        ln, tit = titulos[clave]
        m = PAT_P_DEL_TITULO.search(tit)
        p = ("P.%s" % m.group(1)) if m else "(sin P en el titulo)"
        lista.append((clave, p, ln, tit))
    return lista, estado, ln_cab, cab


def puestos_de_la_pd1(lineas, inicio, fin, titulos):
    """LOS CINCO PUESTOS QUE LA `PD.1` NOMBRA, LEIDOS DEL ACTA Y NO TECLEADOS.
    PURA. Devuelve la lista de enteros del PRIMER numeral ABIERTO que los traiga,
    vacia si ninguno los trae.

    EL ACTA 188 TIENE DOS NUMERALES ABIERTOS (`PD.1` y `PD.8`) Y SOLO EL PRIMERO
    NOMBRA PUESTOS, asi que este recorrido NO se para en el primer abierto como
    hacia el de la 187: sigue hasta encontrar uno con puestos. Si se parara en el
    primero y ese no los trajera, publicaria una lista vacia sobre un acta que si
    los nombra, y eso es una cifra falsa."""
    for clave, pd, estado, ln, _tit in pendientes_de_doctrina(
            lineas, inicio, fin, titulos):
        if estado != "ABIERTA":
            continue
        parrafo = parrafo_de(lineas, ln, fin)
        m = re.search(r"\(\*\*([0-9,\sy]+)\*\*\)", parrafo)
        if not m:
            m = re.search(r"\bson\s+\*\*([0-9,\sy]+)\*\*", parrafo)
        if not m:
            continue
        return [int(x) for x in re.findall(r"\d+", m.group(1))]
    return []


def titulo_de_la_entrada(n_adj, n_pd, n_preg, n_cai_aud, n_cai_eje):
    """El titulo, con sus CINCO numerales COMPUTADOS y no tecleados, y con la
    concordancia dentro del computo. El CERO entra por `PALABRA_CON_CERO`
    importado, y va en plural porque en castellano el cero es plural.

    LA CIFRA DE CAIDAS DEL EJECUTOR ES LA DE LAS `C.n` QUE LA CABECERA DE SU
    SECCION ATRIBUYE AL EJECUTOR, sin importar quien las encontro. El reparto
    entre declaradas y levantadas va DENTRO de la entrada, con su nombre."""
    def trozo(n, sing, plur):
        if n == 1:
            return "la %s" % sing
        return "las %s %s" % (PALABRA_CON_CERO[n], plur)

    def trozo_m(n, sing, plur):
        if n == 1:
            return "el %s" % sing
        return "los %s %s" % (PALABRA_CON_CERO[n], plur)
    return ("Registro de %s, %s, %s, %s del auditor y %s de metodo del ejecutor "
            "del acta de la vuelta %d"
            % (trozo(n_adj, "adjudicacion numerada", "adjudicaciones numeradas"),
               trozo_m(n_pd, "numeral de la seccion 6",
                       "numerales de la seccion 6"),
               trozo(n_preg, "pregunta contestada", "preguntas contestadas"),
               trozo(n_cai_aud, "caida propia", "caidas propias"),
               trozo(n_cai_eje, "caida", "caidas"),
               VUELTA_DEL_ACTA))


VIA = {
    "5.1": "SIN TOCAR NADA",
    "5.2": "EJECUTADA",
    "5.3": "EJECUTADA",
    "5.4": "SIN TOCAR NADA",
    "5.5": "SIN TOCAR NADA",
    "5.6": "SIN TOCAR NADA",
    "6.1": "SIN TOCAR NADA",
    "6.2": "SIN TOCAR NADA",
    "6.3": "SIN TOCAR NADA",
    "7.1": "EJECUTADA",
    "7.2": "EJECUTADA",
    "7.3": "EJECUTADA",
}

QUE_HACE_ESTA_VUELTA = {
    "5.1": ("SE ACATA SIN TOCAR NADA. El acta adjudica a favor la forma de la correccion "
            "del 2464, anexada a la `razon` en vez de en campo propio, y mide que lo que "
            "las reglas escritas exigen esta todo cumplido. Lo que si es del fundador "
            "queda como `PD.8` y esta vuelta NO lo toca: anadir un campo noveno a "
            "`docs/INTRA_DOMINIO_VEREDICTOS.jsonl` es cambiar el esquema del archivo "
            "maestro. El `sha256` LF del archivo abre y cierra en el mismo valor."),
    "5.2": ("SE ACATA Y SU REMEDIO SE EJECUTA EN LA TAREA 5.a DE ESTA VUELTA. El acta "
            "adjudica a favor la conducta (declarar la desviacion con sus dos puestos en "
            "vez de torcer una funcion congelada a mitad de la medicion) y confirma el "
            "solape de 2 desde fuera, con su propia exclusion de 351. El remedio va "
            "ADITIVO y no toca la vara: `vecinos()` recibe un conjunto `evitar` POR "
            "PARAMETRO, y sin el se comporta exactamente igual que hoy, cosa que su arnes "
            "prueba."),
    "5.3": ("SE ACATA Y SU REMEDIO SE EJECUTA EN LA TAREA 3.c DE ESTA VUELTA. El acta "
            "deja escrita la letra para que no se re-litigue: un arnes sellado en rojo "
            "detiene AL ARNES, no a la vuelta, y la vuelta se cierra con la parada "
            "declarada. La mitad que SI se rompio (`sin re-correrlo`) va aparte como "
            "`C.3` y su remedio es que la doble corrida de la nomina EXCLUYA "
            "explicitamente cualquier arnes que ya haya salido en rojo en esa misma "
            "vuelta, y lo DIGA en su salida."),
    "5.4": ("SE ACATA SIN TOCAR NADA. El registro anexado a `docs/plan/08_VERIFICACION.md` "
            "queda adjudicado a favor: entra por adicion, dentro de la seccion, la seccion "
            "sigue siendo una y no cambia ninguna decision de plan. Esta vuelta NO vuelve "
            "a tocar esa sede."),
    "5.5": ("SE ACATA SIN TOCAR NADA, Y ES EL DISCUTIBLE DE CLASE QUE EL ACTA CELEBRA. La "
            "relectura del 2464 sostiene la `D`, y el acta anade una prueba independiente "
            "que el ejecutor no podia tener: el puesto 3148 cayo en su ciega, lo adjudico "
            "`D` a ciegas y el archivo dice `D`. **NINGUNA CLASE SE VUELVE A DECIDIR EN "
            "ESTA VUELTA** y el marcador no se mueve."),
    "5.6": ("SE ACATA SIN TOCAR NADA. La restauracion con `git checkout` de las salidas "
            "selladas que las corridas pisaron queda adjudicada a favor. Lo que el acta NO "
            "adjudica a favor es haberlas re-corrido, y eso va como `C.3`, con su remedio "
            "en la TAREA 3.c."),
    "6.1": ("`PD.1` SIGUE ABIERTA, SEPTIMA VUELTA, Y ESTA VUELTA NO LA CIERRA NI LA "
            "ENCARGA. Las cinco `D` con el diferenciador ya presente el dia del veredicto "
            "siguen sin pasar el disparador escrito, y darles cola seria doctrina nueva, "
            "que es del fundador. Sus cinco nombres van en esta entrada leidos del acta y "
            "no copiados del encargo."),
    "6.2": ("`PD.8` NACE ABIERTA Y ESTA VUELTA NO LA TOCA. La forma de una correccion "
            "declarada dentro de `docs/INTRA_DOMINIO_VEREDICTOS.jsonl` no esta escrita, y "
            "es del fundador porque toca el ESQUEMA del archivo maestro, no porque el caso "
            "no se pudiera resolver. El acta verifico la premisa: el archivo tiene OCHO "
            "campos y ninguno es de correccion. **El encargo de esta vuelta prohibe anadir "
            "ningun campo con esas palabras.**"),
    "6.3": ("ES ANOTACION Y NO PENDIENTE, Y ESTA VUELTA NO ABRE NINGUNA DE LAS TRES MESAS. "
            "La del `PMF` (puestos 338 y 297, y ahora tambien el 670 que el acta suma "
            "desde su ciega de hoy), la del 603 y la de figuras del 226 **no se encargan y "
            "no se adjudican**: el acta las anota para que la vuelta que abra esa carpeta "
            "las encuentre juntas, y el encargo se lo prohibe al ejecutor con esas mismas "
            "palabras."),
    "7.1": ("CONTESTADA POR EL ACTA Y EJECUTADA EN LA TAREA 3 DE ESTA VUELTA, BLOQUEANTE. "
            "La PARADA que el reporte de la 187 declaro NO era parada: no hay dos reglas "
            "vigentes en conflicto, hay un esperado tecleado en la 186 y una orden escrita "
            "de la 187 que lo dejo viejo. **El ejecutor hizo bien en no cambiar el `1` por "
            "un `2`**, porque eso dejaria otra cifra tecleada que la proxima exencion "
            "volveria a dejar vieja. El caso E pasa a computar el INVENTARIO de guardas "
            "eximidas en el carril tardio, con sus nombres, cotejado contra una lista "
            "autorizada y escrita. **Es bloqueante porque la bateria es la 189 y ese arnes "
            "sale hoy en rojo.**"),
    "7.2": ("CONTESTADA POR EL ACTA Y EJECUTADA EN LA TAREA 3.b DE ESTA VUELTA. La "
            "distincion del ejecutor es la correcta y no es doctrina nueva: lo que cambia "
            "entre dos corridas del mismo dia sobre el mismo sujeto es PARADA; lo que se "
            "mueve porque su sujeto se movio, no. El remedio barato va aqui: toda salida "
            "de arnes que publique numeros de linea de un fichero vivo publica al lado el "
            "`sha256` de ese fichero."),
    "7.3": ("CONTESTADA POR EL ACTA Y EJECUTADA EN LA TAREA 5.a DE ESTA VUELTA. El solape "
            "se le exige AL UNIVERSO, porque la exclusion existe para que nadie relea lo "
            "ya leido y los 60 se leen todos. **Pero eso no convierte en caida lo que el "
            "ejecutor hizo**: la respuesta correcta a una vara que no llega no es torcerla, "
            "es declararla y arreglarla en la vuelta siguiente, y eso es lo que va "
            "encargado."),
}


def _cabeza_de_la_entrada(numero, titulo, claves, pds, preguntas, estado_preg, cab7,
                          titulos, l_aud, decl_vieja, decl_nueva, inicio, fin,
                          viejas_adj, viejas_rep, viejas_eje, c_eje, c_aud,
                          huerf_viejo, si_acum, no_acum, estados_viejos):
    """LA PRIMERA MITAD DE LA ENTRADA: la cabecera, los cinco numerales del
    titulo, el reparto de la seccion 6 con sus DOS vocabularios, y las caidas con
    su atribucion y su cuenta de racha. PURA: recibe todo lo ya medido."""
    p = []
    p.append("## R.%d. %s" % (numero, titulo))
    p.append("")
    p.append("(Acta del auditor, vuelta %d, secciones 4, 5, 6, 7, 8, 9, 10, 11, 12 y 13;"
             % VUELTA_DEL_ACTA)
    p.append("escrito en la vuelta %d, TAREA 1.a.)" % VUELTA_QUE_ESCRIBE)
    p.append("")
    p.append("Por adicion, como `R.21` a `R.49`. **Corte de todas las cifras de esta")
    p.append("entrada: 6 sep 2026.** El numero de esta entrada NO esta tecleado: lo computa")
    p.append("`scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS sedes.")
    p.append("La SEDE tampoco se supone: sale de la adjudicacion 6.3 del acta 162, que es")
    p.append("la que citan los `R.30` a `R.49`. Salida:")
    p.append("`docs/loop/SALIDA_V%s_T1A_REGISTRO_R%d.txt`."
             % (SUFIJO_QUE_ESCRIBE, numero))
    p.append("")
    p.append("**ESTA ENTRADA SE ESCRIBE CON LA TAREA 1 EN CURSO Y LAS TAREAS 2 A 5 SIN")
    p.append("CORRER, ASI QUE SUS GLOSAS NO AFIRMAN EN PASADO LO QUE TODAVIA NO HA")
    p.append("PASADO.** Es la forma que la `6.4` del acta 172 adjudico como correcta: donde")
    p.append("una glosa dice EJECUTADA, la tarea que la ejecuta va nombrada; donde dice que")
    p.append("va a ejecutarse, se dice que **todavia no ha corrido** y no se disfraza.")
    p.append("")
    p.append("**Y LOS CINCO NUMERALES DEL TITULO TAMPOCO ESTAN TECLEADOS:** se cuentan del")
    p.append("acta acotada (lineas %d a %d) y de ahi sale el numeral en palabra, incluida"
             % (inicio, fin))
    p.append("la concordancia. **%d adjudicaciones numeradas (`5.1` a `5.%d`, todas en la"
             % (len(claves), len(claves)))
    p.append("seccion 5), %d numerales en la seccion 6 (`6.1` a `6.%d`), %d preguntas en la"
             % (len(pds), len(pds), len(preguntas)))
    p.append("seccion 7 (`7.1` a `7.%d`), %d caidas propias del auditor y %d caidas de"
             % (len(preguntas), len(l_aud), len(c_eje)))
    p.append("metodo del ejecutor.**")
    p.append("")
    p.append("**LAS %s ADJUDICACIONES SON A FAVOR, LAS %s.** El acta no regatea ninguna."
             % (PALABRA_CON_CERO[len(claves)].upper(),
                PALABRA_CON_CERO[len(claves)].upper()))
    p.append("")
    p.append("**LA SECCION 6 TRAE %s NUMERALES Y NO %s PENDIENTES.** El reparto por estado"
             % (PALABRA_CON_CERO[len(pds)].upper(),
                PALABRA_CON_CERO[len(pds)].upper()))
    p.append("sale de leer el titulo literal de cada uno y NO se teclea: **%s**."
             % ("; ".join("%s %s %s" % (c, pd, est) for c, pd, est, _l, _t in pds)))
    p.append("Dos de los tres estan ABIERTOS y el tercero es una ANOTACION que el acta")
    p.append("**no encarga y no adjudica**.")
    p.append("")
    p.append("**Y AQUI VA LA MEDICION QUE PRUEBA QUE ESTE REGISTRADOR HACIA FALTA, EN VEZ")
    p.append("DE AFIRMARLO.** Con el vocabulario de estados de la vuelta 187 (las cuatro")
    p.append("marcas `%s`, `%s`, `%s` y `%s`) corrido"
             % (MARCA_CORRECCION, MARCA_ANOTACION, MARCA_ABIERTA, MARCA_CERRADA))
    p.append("sobre ESTA MISMA acta, los estados salen **%s**: dos de los tres dicen"
             % ("; ".join("%s %s" % (c, e) for c, e in estados_viejos)))
    p.append("`SIN DECIR`, que es **PARADA**. Las dos marcas nuevas son LITERALES del acta")
    p.append("188 y no parafrasis: `%s` sale del titulo del `6.2` y `%s`"
             % (MARCA_ABIERTA_2, MARCA_ANOTACION_2))
    p.append("del titulo del `6.3`. **Se anaden marcas; ninguna de las cuatro viejas se")
    p.append("ensancha ni se toca, y LA PARADA SE CONSERVA ENTERA: un titulo que no diga")
    p.append("ninguna de las seis sigue saliendo `SIN DECIR` y sigue parando.**")
    p.append("")
    p.append("**EL CONTRASTE QUE PRUEBA QUE LOS PATRONES SE MIDEN Y NO SE SUPONEN.** El")
    p.append("patron de adjudicacion SIN comillas inversas, el del acta 183, corrido sobre")
    p.append("esta acta da **%d**. Se conserva intacto y su cero se publica." % viejas_adj)
    p.append("")
    p.append("**CERO CAIDAS PROPIAS DEL AUDITOR, Y EL CERO VA CONTADO Y NO OMITIDO.** El")
    p.append("patron `A.n` de cabecera de tercer nivel, el que el acta 185 estreno, da")
    p.append("**%d** sobre esta acta. Es la SEPTIMA acta seguida sin caida propia del"
             % len(l_aud))
    p.append("auditor, y el acta lo dice con esas palabras.")
    p.append("")
    p.append("**Un cero que sale de un patron que no muerde no es evidencia de nada**, asi")
    p.append("que va con la declaracion del acta al lado: la frase")
    p.append("`%s`, que el acta 186 estreno, aparece en **%d linea(s)**"
             % (FRASE_CERO_CAIDAS_PROPIAS, len(decl_nueva)))
    p.append("(`docs/loop/ACTA_AUDITOR.md:%s`), y la frase `%s`, que era la"
             % (", ".join(str(x) for x in decl_nueva) or "ninguna",
                FRASE_SIN_CAIDA_PROPIA))
    p.append("del acta 185, aparece en **%d**. **Un cero contado y un campo ausente no son"
             % len(decl_vieja))
    p.append("lo mismo, y por eso este registro lleva el cero escrito en vez de callarse")
    p.append("el campo.**")
    p.append("")
    p.append("**EL PATRON `R.n` DE LA CAIDA DE REPORTE DA %d SOBRE ESTA ACTA, Y EL `E.n` DE"
             % viejas_rep)
    p.append("LAS ACTAS 182 Y 184 DA %d.** Las dos cifras se publican y ninguna se resuelve"
             % viejas_eje)
    p.append("copiando: **esta acta no registra ninguna caida de reporte del ejecutor**, y")
    p.append("eso es una medicion, no una omision.")
    p.append("")
    return p


def _caidas_de_la_entrada(lineas, c_eje, c_aud, huerf_viejo, si_acum, no_acum,
                          n_patron_viejo):
    """EL BLOQUE DE LAS CAIDAS: la atribucion por cabecera con sus DOS
    vocabularios, y la cuenta de cuantas acumulan. PURA."""
    p = []
    p.append("**LAS %s CAIDAS DEL EJECUTOR, CON SU LINEA, Y LA ATRIBUCION HECHA POR LA"
             % PALABRA_CON_CERO[len(c_eje)].upper())
    p.append("CABECERA DE SU SECCION Y NO POR QUIEN LAS ENCONTRO.** Es la primera vez que")
    p.append("esta serie registra una seccion de caidas MIXTA: dos las declaro el ejecutor")
    p.append("y dos las levanto el auditor, **y las cuatro son del ejecutor**.")
    p.append("")
    for ln, num, cab in c_eje:
        p.append("  - `C.%d` en `docs/loop/ACTA_AUDITOR.md:%d`, bajo la cabecera *\"%s\"*."
                 % (num, ln, cab))
    p.append("")
    p.append("**Y ANTES DE LA ATRIBUCION HUBO QUE ANADIR UN PATRON, Y SU CIFRA VIEJA VA")
    p.append("PUBLICADA.** El patron `C.n` de la vuelta 187 exige una COMA O UN PUNTO")
    p.append("pegados al numeral (``**`C.3`,``), y el acta 188 escribe sus dos primeras con")
    p.append("un ESPACIO detras (``**`C.1` DEL EJECUTOR``). Corrido sobre esta acta, el")
    p.append("patron viejo encuentra **%d de las %d**. **Se anade un patron; el viejo se"
             % (n_patron_viejo, len(c_eje)))
    p.append("conserva intacto y su cifra se publica al lado.**")
    p.append("")
    p.append("**Y AQUI SE DECLARA UNA DISCREPANCIA MEDIDA EN VEZ DE RESOLVERSE COPIANDO**")
    p.append("(`EJECUTOR.md` 2). El encargo de la vuelta 188 dice que *\"la seccion que las")
    p.append("contiene lo dice en su cabecera\"*. **Se midio antes de creerlo: la cabecera")
    p.append("literal NO contiene la palabra `EJECUTOR`.** Con el vocabulario de la 187")
    p.append("(`EJECUTOR` o `MI CAIDA`) las cuatro salen **HUERFANAS**, y una caida sin")
    p.append("dueno es PARADA. Corrido asi sobre esta misma acta: **ejecutor %d, auditor %d,"
             % (len(huerf_viejo[0]), len(huerf_viejo[1])))
    p.append("huerfanas %d**. **La cabecera SI dice de quien son, pero con otras palabras:**"
             % len(huerf_viejo[2]))
    p.append("`LAS SUYAS`, que en un acta que el auditor escribe sobre el ejecutor son las")
    p.append("del ejecutor. Esa marca se ANADE, literal, y la vieja se conserva.")
    p.append("")
    p.append("**LA PRECEDENCIA VA ESCRITA Y NO ES UN DESCUIDO:** si la cabecera trae una")
    p.append("marca de EJECUTOR, la caida es del ejecutor **aunque la cabecera diga ademas")
    p.append("que la levanto el auditor**, que es literalmente lo que dice esta. **La")
    p.append("PARADA se conserva entera**: una `C.n` bajo una cabecera que no diga ni una")
    p.append("cosa ni la otra sigue saliendo huerfana y sigue parando.")
    p.append("")
    p.append("**Y LAS DOS CUENTAS VAN JUNTAS, PORQUE UNA CAIDA QUE NO ACUMULA NO ES UNA")
    p.append("CAIDA QUE NO EXISTE.** Leido del parrafo de cada una y no tecleado:")
    p.append("")
    p.append("  - **CIFRA caidas del ejecutor registradas: %d.**" % len(c_eje))
    p.append("  - **CIFRA de esas que ACUMULAN para alguna racha: %d.**" % len(si_acum))
    p.append("  - **CIFRA de esas que NO acumulan: %d**, y son %s."
             % (len(no_acum),
                ", ".join("`C.%d`" % n for _l, n in no_acum) or "(ninguna)"))
    p.append("")
    p.append("**POR QUE DIFIEREN, DICHO Y NO DEJADO A QUE ALGUIEN LO DEDUZCA:** las %d son"
             % len(c_eje))
    p.append("**de METODO**, y las rachas que esta casa lleva son otras dos: la de **cifra")
    p.append("publicada**, que sigue en **0**, y la de **reporte**, que **se mantiene en")
    p.append("2** sin sumar. **Publicar solo el cero diria que no paso nada; publicar solo")
    p.append("el %d diria que alguna racha subio. Las dos son falsas por separado.** La"
             % len(c_eje))
    p.append("cuenta sale de buscar en el parrafo de cada caida las marcas literales con")
    p.append("que el acta declara que no acumula, y **una caida cuyo parrafo no dijera nada")
    p.append("se contaria como QUE ACUMULA**, que es el lado seguro.")
    p.append("")
    return p


def armar_entrada(numero, titulo, claves, pds, preguntas, estado_preg, cab7,
                  titulos, l_aud, decl_vieja, decl_nueva, inicio, fin,
                  viejas_adj, viejas_rep, viejas_eje, c_eje, c_aud, huerf_viejo,
                  si_acum, no_acum, estados_viejos, puestos_pd1, salto, lineas,
                  n_patron_viejo):
    """LA ENTRADA ENTERA. PURA: recibe todo lo ya medido y no lee ni escribe."""
    faltan, bajo, alto = salto
    p = _cabeza_de_la_entrada(numero, titulo, claves, pds, preguntas,
                              estado_preg, cab7, titulos, l_aud, decl_vieja,
                              decl_nueva, inicio, fin, viejas_adj, viejas_rep,
                              viejas_eje, c_eje, c_aud, huerf_viejo, si_acum,
                              no_acum, estados_viejos)
    p.append("**LAS %s ADJUDICACIONES NUMERADAS, CON SU LINEA EN EL ACTA LEIDA HOY.** El"
             % PALABRA_CON_CERO[len(claves)].upper())
    p.append("titulo de cada una es LITERAL del fichero; la glosa que sigue es prosa del")
    p.append("ejecutor y va marcada como tal.")
    p.append("")
    for clave, _n in claves:
        ln, tit = titulos[clave]
        p.append("  - **`%s` (`docs/loop/ACTA_AUDITOR.md:%d`, leida hoy). VIA: %s.** Titulo"
                 % (clave, ln, VIA[clave]))
        p.append("    literal del acta: *\"%s\"*" % tit)
        p.append("    **QUE HACE ESTA VUELTA CON ELLA (glosa del ejecutor, no del acta):** %s"
                 % QUE_HACE_ESTA_VUELTA[clave])
    p.append("")
    p.append("**LOS %s NUMERALES DE LA SECCION 6, CON SU ESTADO LEIDO DEL TITULO Y NO"
             % PALABRA_CON_CERO[len(pds)].upper())
    p.append("TECLEADO.** El estado sale de buscar en el titulo literal, en este orden,")
    p.append("`%s`; `%s` o `%s`; `%s` o"
             % (MARCA_CORRECCION, MARCA_ANOTACION, MARCA_ANOTACION_2, MARCA_ABIERTA))
    p.append("`%s`; y `%s`. **Si un titulo no dijera ninguna de las seis, el"
             % (MARCA_ABIERTA_2, MARCA_CERRADA))
    p.append("instrumento haria PARADA en vez de meterlo en el saco de los abiertos o en el")
    p.append("de los cerrados.**")
    p.append("")
    for clave, pd, estado, ln, tit in pds:
        p.append("  - **`%s`, que nombra `%s`, estado %s (`docs/loop/ACTA_AUDITOR.md:%d`,"
                 % (clave, pd, estado, ln))
        p.append("    leida hoy). VIA: %s.** Titulo literal del acta: *\"%s\"*"
                 % (VIA[clave], tit))
        p.append("    **QUE HACE ESTA VUELTA CON EL (glosa del ejecutor, no del acta):** %s"
                 % QUE_HACE_ESTA_VUELTA[clave])
    p.append("")
    p.append("**LAS %s PREGUNTAS DE LA SECCION 7, LAS %s CONTESTADAS.** El estado NO se"
             % (PALABRA_CON_CERO[len(preguntas)].upper(),
                PALABRA_CON_CERO[len(preguntas)].upper()))
    p.append("teclea ni se supone: sale de la cabecera literal de la seccion 7")
    p.append("(`docs/loop/ACTA_AUDITOR.md:%s`), que dice *\"%s\"*."
             % (cab7[0] if cab7[0] else "?", cab7[1]))
    p.append("Si esa cabecera no dijera `%s`, este instrumento haria PARADA en vez de"
             % MARCA_CONTESTADAS)
    p.append("registrarlas como contestadas. **Las tres eran del ejecutor de la 187 y las")
    p.append("contesta el auditor.**")
    p.append("")
    for clave, pr, ln, tit in preguntas:
        p.append("  - **`%s`, que nombra `%s`, estado %s (`docs/loop/ACTA_AUDITOR.md:%d`,"
                 % (clave, pr, estado_preg, ln))
        p.append("    leida hoy). VIA: %s.** Titulo literal del acta: *\"%s\"*"
                 % (VIA[clave], tit))
        p.append("    **QUE HACE ESTA VUELTA CON ELLA (glosa del ejecutor, no del acta):** %s"
                 % QUE_HACE_ESTA_VUELTA[clave])
    p.append("")
    p.append("**LOS CINCO PUESTOS DE LA `PD.1`, LEIDOS DEL ACTA Y NO TECLEADOS.** El")
    p.append("encargo los nombra y aqui NO se copian: salen del parrafo del numeral que")
    p.append("el propio titulo declara ABIERTO y que ademas los trae. **Son %d puestos:"
             % len(puestos_pd1))
    p.append("%s.** Es la SEPTIMA vuelta que la `PD.1` sigue abierta, y el acta dice que"
             % (", ".join(str(x) for x in puestos_pd1) or "(ninguno)"))
    p.append("darles cola seria doctrina nueva, o sea del fundador. **Y esta vuelta le")
    p.append("anade una medicion del propio auditor: su criba de hoy nombra exactamente")
    p.append("esos cinco ademas del 2464.**")
    p.append("")
    p += _caidas_de_la_entrada(lineas, c_eje, c_aud, huerf_viejo, si_acum,
                               no_acum, n_patron_viejo)
    p.append("**LA DEUDA DE LA SERIE, QUE SIGUE DOCUMENTADA COMO SALTO Y SIN RELLENAR.**")
    p.append("Se vuelve a medir en esta vuelta en vez de heredarse del `R.49`:")
    p.append("")
    if faltan:
        p.append("  - **SALTO DE %d REGISTROS EN LA SERIE: las actas %d a %d no tienen"
                 % (len(faltan), min(faltan), max(faltan)))
        p.append("    entrada propia.** Sus dos extremos, contados por")
        p.append("    `scripts/loop/serie_de_registros.py` y no tecleados: **`R.%s` cubre el"
                 % (bajo[0] if bajo else "?"))
        p.append("    acta %s** y **`R.%s` cubre el acta %s**. **No se rellenan aqui:**"
                 % (bajo[1] if bajo else "?", alto[0] if alto else "?",
                    alto[1] if alto else "?"))
        p.append("    escribir de memoria los registros de unas actas que nadie ha releido")
        p.append("    en esta vuelta seria justo lo que `AUDITOR.md` 2 prohibe.")
    else:
        p.append("  - **NO HAY SALTO:** todas las actas del tramo medido tienen entrada")
        p.append("    propia en la serie. La constancia se escribe igual, porque una")
        p.append("    comprobacion que solo se publica cuando falla no se puede auditar.")
    p.append("")
    p.append("**LO QUE ESTA ENTRADA NO REGISTRA, DICHO PARA QUE NO SE BUSQUE:** el")
    p.append("instrumento de vigencia de las `A` rancias por `P.5` **sigue sin cablear**;")
    p.append("**las tres mesas anotadas del `6.3` no se abren aqui** (la del `PMF` con los")
    p.append("puestos 338, 297 y 670, la del **603** y la de figuras del **226**), y el")
    p.append("encargo lo prohibe con esas palabras: son trabajo de plan de otra vuelta y su")
    p.append("sede es `docs/PENDIENTES.md`. **Y no se anade ningun campo a")
    p.append("`docs/INTRA_DOMINIO_VEREDICTOS.jsonl`**, que es la `PD.8` y es del fundador.")
    return NL.join(p) + NL


def _acta_fabricada(n_adj, n_pd, n_preg, caidas_aud, caidas_eje,
                    declara_cero=False, puestos=(11, 22, 33),
                    contesta=True, con_anotacion=True, cabecera_ejecutor="LAS SUYAS",
                    acumulan_todas=False, estado_raro=False,
                    caida_con_espacio=True, no_acumula_lejos=False):
    """UN ACTA DE MENTIRA para el caso positivo por mutacion. NO toca el repo.

    Escribe los numerales de las secciones 5, 6 y 7 ENTRE COMILLAS INVERSAS, que
    es la forma del acta 188; la caida propia del auditor como cabecera de tercer
    nivel con `A.n`; y las del ejecutor como ``**`C.n`,`` al principio de linea,
    DEBAJO de una cabecera cuya frase de dueno es PARAMETRO.

    LOS `6.n`, EN LA FORMA DEL ACTA 188: el PRIMERO es el que `SIGUE ABIERTA` con
    sus puestos, el SEGUNDO el que `LA DEJO ABIERTA` sin puestos (que es lo que
    obliga a que `puestos_de_la_pd1` no se pare en el primer abierto), y el
    ULTIMO la ANOTACION con `SIGUEN ANOTADAS` cuando `con_anotacion`."""
    L = ["# ACTA DEL AUDITOR, VUELTA %d (fabricada)" % VUELTA_DEL_ACTA, ""]
    if declara_cero and caidas_aud == 0:
        L += ["**%s MIAS, DE MENTIRA.** Y su cuerpo."
              % FRASE_CERO_CAIDAS_PROPIAS, ""]
    L += ["## 2. MI APERTURA DE MENTIRA", ""]
    for k in range(1, caidas_aud + 1):
        L += ["### 2.%d MI CAIDA PROPIA `A.%d`, DE MENTIRA" % (k, k), "",
              "Y su cuerpo.", ""]
    L += ["## 5. LAS ADJUDICACIONES", ""]
    for k in range(1, n_adj + 1):
        L += ["**`5.%d` UN TITULO DE MENTIRA NUMERO %d.** Y su cuerpo." % (k, k), ""]
    L += ["## 6. LOS NUMERALES DE LA SECCION 6", ""]
    for k in range(1, n_pd + 1):
        if k == 1:
            if estado_raro:
                L += ["**`6.1` `PD.1` EN UN ESTADO QUE NADIE ESCRIBIO.** Los puestos",
                      "(**%s**) estan medidos en otro sitio."
                      % ", ".join(str(x) for x in puestos), ""]
            else:
                L += ["**`6.1` `PD.1` %s, DE MENTIRA.** Los puestos (**%s**)"
                      % (MARCA_ABIERTA, ", ".join(str(x) for x in puestos)),
                      "estan medidos en otro sitio.", ""]
        elif con_anotacion and k == n_pd and n_pd >= 3:
            L += ["**`6.%d` LAS TRES MESAS ANOTADAS %s Y NO SE ABREN.** De mentira."
                  % (k, MARCA_ANOTACION_2), "", "Y su cuerpo.", ""]
        elif k == 2:
            L += ["**`6.2` `PD.8` NACE Y %s, CON SU SEDE BIEN PUESTA.** Sin puestos."
                  % MARCA_ABIERTA_2, "", "Y su cuerpo.", ""]
        else:
            L += ["**`6.%d` `PD.%d`, UN PENDIENTE DE MENTIRA: ADJUDICADO.** Y su cuerpo."
                  % (k, k + 4), ""]
    cab = "## 7. LAS PREGUNTAS, QUE ERAN MIAS Y %s" % (
        MARCA_CONTESTADAS if contesta else "NO DIGO NADA")
    L += [cab, ""]
    for k in range(1, n_preg + 1):
        L += ["**`7.%d` `P.%d`, UNA PREGUNTA DE MENTIRA.** Y su respuesta." % (k, k), ""]
    L += ["## 8. LAS CAIDAS, %s DECLARADAS Y LAS DOS QUE LEVANTO YO"
          % cabecera_ejecutor, ""]
    # LA PUNTUACION DE DETRAS DEL NUMERAL ES PARAMETRO: el acta 187 escribia
    # ``**`C.1`,`` (coma) y el acta 188 escribe ``**`C.1` DEL EJECUTOR`` (espacio).
    sep = " DE MENTIRA" if caida_con_espacio else ", DE MENTIRA"
    for k in range(1, caidas_eje + 1):
        if acumulan_todas:
            L += ["**`C.%d`%s QUE SI SUMA.** Y su cuerpo." % (k, sep), ""]
        elif no_acumula_lejos:
            L += ["**`C.%d`%s.** Y su primer parrafo, que no dice nada de rachas."
                  % (k, sep), "",
                  "Y un parrafo de en medio, tambien mudo.", "",
                  "LA ESPECIE Y SI ACUMULA: es de metodo y NO ACUMULA.", ""]
        else:
            L += ["**`C.%d`%s.** Es de metodo y NO ACUMULA." % (k, sep), ""]
    return NL.join(L) + NL


def _titulos_de(lineas, ini, fin, prefijo):
    """LOS TITULOS LITERALES DE UN PREFIJO, PARA QUE EL CASO POR MUTACION PUEDA
    CORRER LAS FUNCIONES PURAS SIN TOCAR EL REPO."""
    titulos = {}
    for clave, _n in claves_entrecomilladas(lineas, ini, fin, prefijo):
        pat = re.compile(r"^\s*\*\*`%s` " % re.escape(clave))
        res, err = titulo_de_la_negrita(lineas, ini, fin, pat, clave)
        if err:
            return None, err
        titulos[clave] = res
    return titulos, None


def _mutacion_contadores(w):
    """LOS CONTADORES BASICOS, SOBRE ACTAS FABRICADAS. Devuelve (fallos, lineas,
    ini, fin) del acta canonica de la prueba."""
    fallos = 0
    w("PRIMERA MUTACION: LOS CONTADORES, SOBRE CUATRO ACTAS FABRICADAS.")
    casos = [(6, 3, 3, 0, 4), (1, 3, 1, 0, 1), (12, 4, 5, 3, 2), (4, 3, 2, 1, 0)]
    for n_adj, n_pd, n_preg, n_aud, n_eje in casos:
        texto = _acta_fabricada(n_adj, n_pd, n_preg, n_aud, n_eje,
                                declara_cero=True)
        lineas, rango, err = cuerpo_del_acta(texto)
        if err:
            w("   %r -> %s" % ((n_adj, n_pd, n_preg, n_aud, n_eje), err))
            fallos += 1
            continue
        ini, fin = rango
        cl = claves_entrecomilladas(lineas, ini, fin, PREFIJO_ADJ)
        pd = claves_entrecomilladas(lineas, ini, fin, PREFIJO_PD)
        pr = claves_entrecomilladas(lineas, ini, fin, PREFIJO_PREG)
        aud = cuenta_por_patron(lineas, ini, fin, PAT_CAIDA_AUDITOR_A)
        c_eje, c_aud, huer = caidas_c_por_seccion(lineas, ini, fin)
        ok = (len(cl) == n_adj and len(pd) == n_pd and len(pr) == n_preg
              and len(aud) == n_aud and len(c_eje) == n_eje and not huer)
        w("   fabricada adj=%d pd=%d preg=%d aud=%d eje=%d -> contadores adj=%d "
          "pd=%d preg=%d aud=%d eje=%d huerfanas=%d -> %s"
          % (n_adj, n_pd, n_preg, n_aud, n_eje, len(cl), len(pd), len(pr),
             len(aud), len(c_eje), len(huer), "CALZA" if ok else "NO CALZA"))
        if not ok:
            fallos += 1
    texto = _acta_fabricada(6, 3, 3, 0, 4, declara_cero=True)
    lineas, (ini, fin), _e = cuerpo_del_acta(texto)
    w("   titulo computado: %s"
      % titulo_de_la_entrada(6, 3, 3, 0, 4))
    medido = len(claves_entrecomilladas(lineas, ini, fin, PREFIJO_ADJ))
    for esperado in (6, 7):
        w("   con el esperado %d de adjudicaciones: %s"
          % (esperado, "PASA" if medido == esperado else "CAE"))
    if medido == 7:
        fallos += 1
    con_viejo = len(claves_de_adjudicacion(lineas, ini, fin, PREFIJO_ADJ))
    w("   el patron SIN comillas, el del acta 183, sobre esta forma -> %d" % con_viejo)
    if con_viejo != 0:
        fallos += 1
    w("")
    return fallos, lineas, ini, fin


def _mutacion_estados(w, lineas, ini, fin):
    """LOS DOS ESTADOS NUEVOS Y LA PARADA QUE SE CONSERVA."""
    fallos = 0
    w("SEGUNDA MUTACION: LOS DOS ESTADOS NUEVOS DE LA SECCION 6, Y LAS DOS CIFRAS.")
    tit_pd, _e = _titulos_de(lineas, ini, fin, PREFIJO_PD)
    nuevos = [(c, e) for c, _p, e, _l, _t
              in pendientes_de_doctrina(lineas, ini, fin, tit_pd)]
    viejos = [(c, e) for c, _p, e, _l, _t
              in pendientes_de_doctrina(lineas, ini, fin, tit_pd,
                                        vocabulario_viejo=True)]
    w("   con el vocabulario NUEVO: %s" % nuevos)
    w("   con el vocabulario VIEJO, el de la 187: %s" % viejos)
    n_sin_viejo = len([1 for _c, e in viejos if e == "SIN DECIR"])
    n_sin_nuevo = len([1 for _c, e in nuevos if e == "SIN DECIR"])
    ok = (n_sin_nuevo == 0 and n_sin_viejo == 2)
    w("   SIN DECIR con el nuevo: %d | con el viejo: %d | esperado 0 y 2 -> %s"
      % (n_sin_nuevo, n_sin_viejo, "CALZA" if ok else "NO CALZA"))
    if not ok:
        fallos += 1
    w("   MUTACION del esperado (exigir 2 SIN DECIR con el vocabulario nuevo): %s"
      % ("PASA" if n_sin_nuevo == 2 else "CAE"))
    if n_sin_nuevo == 2:
        fallos += 1
    w("")
    w("   Y LA PARADA SE CONSERVA ENTERA: un titulo que no diga NINGUNA de las seis")
    w("   marcas tiene que seguir saliendo SIN DECIR.")
    raro = _acta_fabricada(6, 3, 3, 0, 4, estado_raro=True)
    l2, (i2, f2), _z = cuerpo_del_acta(raro)
    t2, _z2 = _titulos_de(l2, i2, f2, PREFIJO_PD)
    est2 = [e for _c, _p, e, _l, _t in pendientes_de_doctrina(l2, i2, f2, t2)]
    hay = "SIN DECIR" in est2
    w("      estados sobre el acta del estado desconocido: %s" % est2)
    w("      SALE `SIN DECIR`, QUE ES LA PARADA: %s" % ("SI" if hay else "NO"))
    w("      MUTACION del esperado (exigir que ninguno sea SIN DECIR): %s"
      % ("PASA" if not hay else "CAE"))
    if not hay:
        fallos += 1
    w("")
    w("   Y LOS PUESTOS NO SE PARAN EN EL PRIMER ABIERTO SIN PUESTOS. El acta")
    w("   fabricada tiene DOS numerales abiertos y solo el primero los trae.")
    for inventados in ((11, 22, 33), (7, 8, 9, 10), (1778, 2530, 2540, 3141, 3232)):
        t3 = _acta_fabricada(6, 3, 3, 0, 4, puestos=inventados)
        l3, (i3, f3), _z3 = cuerpo_del_acta(t3)
        tt3, _z4 = _titulos_de(l3, i3, f3, PREFIJO_PD)
        leidos = puestos_de_la_pd1(l3, i3, f3, tt3)
        okp = leidos == list(inventados)
        w("      acta con puestos %s -> leidos %s -> %s"
          % (list(inventados), leidos, "CALZA" if okp else "NO CALZA"))
        if not okp:
            fallos += 1
    t4 = _acta_fabricada(6, 3, 3, 0, 4, puestos=(1778, 2530, 2540, 3141, 3232))
    l4, (i4, f4), _z5 = cuerpo_del_acta(t4)
    tt4, _z6 = _titulos_de(l4, i4, f4, PREFIJO_PD)
    leidos4 = puestos_de_la_pd1(l4, i4, f4, tt4)
    w("      MUTACION del esperado [1778, 2530, 2540, 3141, 9999]: %s"
      % ("PASA" if leidos4 == [1778, 2530, 2540, 3141, 9999] else "CAE"))
    if leidos4 == [1778, 2530, 2540, 3141, 9999]:
        fallos += 1
    w("")
    return fallos


def _mutacion_atribucion(w):
    """LA ATRIBUCION MIXTA Y LOS DOS VOCABULARIOS DE CABECERA."""
    fallos = 0
    w("TERCERA MUTACION: LA ATRIBUCION DE UNA SECCION DE CAIDAS MIXTA, QUE ES LO")
    w("QUE ESTE REGISTRADOR ESTRENA. La cabecera decide, no quien la encontro.")
    escenarios = [
        ("cabecera con `LAS SUYAS`, la del acta 188", "LAS SUYAS", 4, 0, 0),
        ("cabecera con `EJECUTOR`, la del acta 187", "DEL EJECUTOR, LAS SUYAS X", 4, 0, 0),
        ("cabecera con `MI CAIDA`", "MI CAIDA PROPIA X", 0, 4, 0),
        ("cabecera que no dice de quien son", "LAS DE ALGUIEN", 0, 0, 4),
    ]
    for etiqueta, frase, e_eje, e_aud, e_hue in escenarios:
        texto = _acta_fabricada(6, 3, 3, 0, 4, cabecera_ejecutor=frase)
        lin, (i, f), _z = cuerpo_del_acta(texto)
        c_e, c_a, hu = caidas_c_por_seccion(lin, i, f)
        ok = (len(c_e) == e_eje and len(c_a) == e_aud and len(hu) == e_hue)
        w("   %-46s -> ejecutor %d | auditor %d | huerfanas %d | esperado %d/%d/%d -> %s"
          % (etiqueta, len(c_e), len(c_a), len(hu), e_eje, e_aud, e_hue,
             "CALZA" if ok else "NO CALZA"))
        if not ok:
            fallos += 1
        w("      MUTACION del esperado (exigir ejecutor %d): %s"
          % (e_eje + 1, "PASA" if len(c_e) == e_eje + 1 else "CAE"))
        if len(c_e) == e_eje + 1:
            fallos += 1
    w("")
    w("   Y EL VOCABULARIO VIEJO, EL DE LA 187, SOBRE LA CABECERA DEL ACTA 188:")
    texto = _acta_fabricada(6, 3, 3, 0, 4)
    lin, (i, f), _z = cuerpo_del_acta(texto)
    v_e, v_a, v_h = caidas_c_por_seccion(lin, i, f, marcas_eje=("EJECUTOR",),
                                         marcas_aud=("MI CAIDA",))
    w("      ejecutor %d | auditor %d | HUERFANAS %d" % (len(v_e), len(v_a), len(v_h)))
    ok_v = (len(v_e) == 0 and len(v_h) == 4)
    w("      esperado 0 del ejecutor y 4 huerfanas, que es la PARADA -> %s"
      % ("CALZA" if ok_v else "NO CALZA"))
    if not ok_v:
        fallos += 1
    w("      MUTACION del esperado (exigir 4 del ejecutor con el vocabulario viejo): %s"
      % ("PASA" if len(v_e) == 4 else "CAE"))
    if len(v_e) == 4:
        fallos += 1
    w("")
    return fallos


def _mutacion_patron(w):
    """EL PATRON DE LA `C.n` CON ESPACIO, QUE ES LO QUE EL ACTA 188 ESCRIBE."""
    fallos = 0
    w("CUARTA MUTACION: EL PATRON DE LA CAIDA `C.n`, Y LAS DOS CIFRAS.")
    w("   El acta 187 escribia ``**`C.1`,`` (coma pegada) y la 188 escribe")
    w("   ``**`C.1` DEL EJECUTOR`` (espacio). El patron heredado exige coma o punto.")
    for etiqueta, con_espacio, e_viejo, e_nuevo in (
            ("acta en la forma de la 188 (espacio)", True, 0, 4),
            ("acta en la forma de la 187 (coma)", False, 4, 4)):
        texto = _acta_fabricada(6, 3, 3, 0, 4, caida_con_espacio=con_espacio)
        lin, (i, f), _z = cuerpo_del_acta(texto)
        viejo = len(cuenta_por_patron(lin, i, f, PAT_CAIDA_C))
        nuevo = len(cuenta_por_patron(lin, i, f, PAT_CAIDA_C_ESPACIO))
        ok = (viejo == e_viejo and nuevo == e_nuevo)
        w("   %-40s -> patron viejo %d | patron nuevo %d | esperado %d y %d -> %s"
          % (etiqueta, viejo, nuevo, e_viejo, e_nuevo,
             "CALZA" if ok else "NO CALZA"))
        if not ok:
            fallos += 1
        w("      MUTACION del esperado (exigir %d con el patron viejo): %s"
          % (e_viejo + 1, "PASA" if viejo == e_viejo + 1 else "CAE"))
        if viejo == e_viejo + 1:
            fallos += 1
    w("   EL PATRON VIEJO SE CONSERVA INTACTO Y SU CERO SE PUBLICA: se ANADE un")
    w("   patron, no se ensancha el viejo hasta que trague.")
    w("")
    return fallos


def _mutacion_racha(w):
    """LA CUENTA DE LAS QUE ACUMULAN, QUE NO ES LA CUENTA DE LAS QUE HAY."""
    fallos = 0
    w("QUINTA MUTACION: UNA CAIDA QUE NO ACUMULA NO ES UNA CAIDA QUE NO EXISTE.")
    for etiqueta, kw, e_si, e_no in (
            ("cuatro que declaran NO ACUMULA en su primer parrafo", {}, 0, 4),
            ("cuatro que lo declaran DOS PARRAFOS MAS ABAJO",
             dict(no_acumula_lejos=True), 0, 4),
            ("cuatro que no dicen nada", dict(acumulan_todas=True), 4, 0)):
        texto = _acta_fabricada(6, 3, 3, 0, 4, **kw)
        lin, (i, f), _z = cuerpo_del_acta(texto)
        c_e, _c_a, _hu = caidas_c_por_seccion(lin, i, f)
        si, no = acumulan(lin, f, c_e)
        ok = (len(c_e) == 4 and len(si) == e_si and len(no) == e_no)
        w("   %-52s -> caidas %d | acumulan %d | no acumulan %d | esperado %d y %d -> %s"
          % (etiqueta, len(c_e), len(si), len(no), e_si, e_no,
             "CALZA" if ok else "NO CALZA"))
        if not ok:
            fallos += 1
        w("      MUTACION del esperado (exigir %d que acumulan): %s"
          % (e_si + 1, "PASA" if len(si) == e_si + 1 else "CAE"))
        if len(si) == e_si + 1:
            fallos += 1
    w("   EL BLOQUE SE LEE ENTERO Y NO SOLO EL PRIMER PARRAFO: con `parrafo_de()`")
    w("   el segundo caso habria dado 4 que acumulan, que es una cifra falsa.")
    lejos = _acta_fabricada(6, 3, 3, 0, 4, no_acumula_lejos=True)
    lin2, (i2, f2), _z2 = cuerpo_del_acta(lejos)
    c_e2, _a2, _h2 = caidas_c_por_seccion(lin2, i2, f2)
    solo_parrafo = len([1 for ln, _n, _c in c_e2
                        if not any(x in parrafo_de(lin2, ln, f2).upper()
                                   for x in MARCAS_NO_ACUMULA)])
    w("   CONTRASTE, leyendo solo el primer parrafo: %d de %d saldrian ACUMULANDO"
      % (solo_parrafo, len(c_e2)))
    if solo_parrafo != 4:
        fallos += 1
    w("   EL SILENCIO SE CUENTA COMO QUE ACUMULA, QUE ES EL LADO SEGURO: dar por")
    w("   bueno un silencio seria aflojar una racha sin que nadie lo escribiera.")
    w("")
    return fallos


def prueba_de_mutacion():
    """EL CASO POSITIVO POR MUTACION, ENTERO Y CON UNA SOLA CUENTA DE FALLOS.
    EL SUJETO ES SIEMPRE UN ACTA FABRICADA, NUNCA LA REAL."""
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("CASO POSITIVO POR MUTACION de vuelta188_tarea1a_registrar_acta188.py")
    w("EL SUJETO ES UN ACTA FABRICADA, NUNCA LA REAL.")
    w("=" * 78)
    w("")
    fallos, lineas, ini, fin = _mutacion_contadores(w)
    fallos += _mutacion_estados(w, lineas, ini, fin)
    fallos += _mutacion_atribucion(w)
    fallos += _mutacion_patron(w)
    fallos += _mutacion_racha(w)

    w("SEXTA MUTACION: EL PATRON `A.n`, LA DECLARACION DEL CERO Y LOS DOS PATRONES")
    w("VIEJOS DE CAIDA DEL EJECUTOR.")
    aud_nuevo = len(cuenta_por_patron(lineas, ini, fin, PAT_CAIDA_AUDITOR_A))
    d_vieja, d_nueva = lineas_que_declaran_cero_caidas(lineas, ini, fin)
    rep_r = len(cuenta_por_patron(lineas, ini, fin, PAT_CAIDA_REPORTE))
    rep_e = len(cuenta_por_patron(lineas, ini, fin, PAT_CAIDA_EJECUTOR_VIEJO))
    w("   patron `A.n` -> %d | frase del cero -> %d linea(s) | frase de la 185 -> %d"
      % (aud_nuevo, len(d_nueva), len(d_vieja)))
    w("   patron `R.n` -> %d | patron `E.n` -> %d" % (rep_r, rep_e))
    ok = (aud_nuevo == 0 and len(d_nueva) == 1 and len(d_vieja) == 0
          and rep_r == 0 and rep_e == 0)
    w("   EL CERO VA CONTADO Y DECLARADO, Y LOS VIEJOS DAN CERO: %s"
      % ("SI" if ok else "NO"))
    if not ok:
        fallos += 1
    w("   MUTACION del esperado (exigir 1 caida propia del auditor): %s"
      % ("PASA" if aud_nuevo == 1 else "CAE"))
    if aud_nuevo == 1:
        fallos += 1
    con_caida = _acta_fabricada(6, 3, 3, 2, 4)
    l6, (i6, f6), _e6 = cuerpo_del_acta(con_caida)
    n6 = len(cuenta_por_patron(l6, i6, f6, PAT_CAIDA_AUDITOR_A))
    w("   y sobre un acta CON dos caidas propias, para que se vea que el contador")
    w("   no esta clavado en cero: patron `A.n` -> %d" % n6)
    if n6 != 2:
        fallos += 1
    w("")

    w("SEPTIMA MUTACION: EL ESTADO DE LAS PREGUNTAS, LEIDO DE LA CABECERA.")
    tit_pr, _e7 = _titulos_de(lineas, ini, fin, PREFIJO_PREG)
    _lst, estado_si, ln7, cab7 = preguntas_de_la_seccion7(lineas, ini, fin, tit_pr)
    muda = _acta_fabricada(6, 3, 3, 0, 4, contesta=False)
    l8, (i8, f8), _e8 = cuerpo_del_acta(muda)
    tit8, _z8 = _titulos_de(l8, i8, f8, PREFIJO_PREG)
    _l8, estado_no, _ln8, cab8 = preguntas_de_la_seccion7(l8, i8, f8, tit8)
    w("   cabecera que SI contesta (linea %s): %r -> %s" % (ln7, cab7, estado_si))
    w("   cabecera que NO lo dice: %r -> %s" % (cab8, estado_no))
    ok_pr = (estado_si == "CONTESTADA" and estado_no == "SIN DECIR")
    w("   EL ESTADO SIGUE A LA CABECERA: %s" % ("SI" if ok_pr else "NO"))
    w("   MUTACION del esperado (la muda tambien CONTESTADA): %s"
      % ("PASA" if estado_no == "CONTESTADA" else "CAE"))
    if not ok_pr or estado_no == "CONTESTADA":
        fallos += 1
    w("")

    w("OCTAVA MUTACION: EL SALTO. actas_sin_entrada() es PURA y se importa.")
    serie_falsa = [
        (10, "docs/PENDIENTES.md", 1, "## R.10. Registro del acta de la vuelta 100"),
        (11, "docs/PENDIENTES.md", 2, "## R.11. Registro del acta de la vuelta 101"),
        (12, "docs/PENDIENTES.md", 3, "## R.12. Registro del acta de la vuelta 105"),
    ]
    faltan, bajo, alto = actas_sin_entrada(serie_falsa, 100, 105)
    ok_s = (faltan == [102, 103, 104] and bajo == (11, 101) and alto == (12, 105))
    w("   faltan %s | bajo %s | alto %s -> %s"
      % (faltan, bajo, alto, "CALZA" if ok_s else "NO CALZA"))
    if not ok_s:
        fallos += 1
    w("")

    w("NOVENA MUTACION: EL TITULO Y SU CONCORDANCIA, INCLUIDO EL CERO.")
    t0 = titulo_de_la_entrada(6, 3, 3, 0, 4)
    w("   %s" % t0)
    ok_t = ("las seis adjudicaciones numeradas" in t0
            and "los tres numerales de la seccion 6" in t0
            and "las tres preguntas contestadas" in t0
            and "las cero caidas propias" in t0
            and "las cuatro caidas de metodo del ejecutor" in t0)
    w("   DICE LAS CINCO COSAS Y CONCUERDA: %s" % ("SI" if ok_t else "NO"))
    if not ok_t:
        fallos += 1
    t1 = titulo_de_la_entrada(3, 1, 1, 2, 1)
    w("   y con otras cifras: %s" % t1)
    if ("las tres adjudicaciones" not in t1
            or "el numeral de la seccion 6" not in t1
            or "la pregunta contestada" not in t1
            or "las dos caidas propias" not in t1
            or "la caida de metodo del ejecutor" not in t1):
        w("   LA CONCORDANCIA NO SIGUE A LAS CIFRAS: NO")
        fallos += 1
    else:
        w("   LA CONCORDANCIA SIGUE A LAS CIFRAS: SI")
    w("")

    w("CIFRA fallos: %d" % fallos)
    w("VEREDICTO: %s" % ("VERDE" if fallos == 0 else "ROJO"))
    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V%s_T1A_MUTACION_REGISTRO_188.txt"
                        % SUFIJO_QUE_ESCRIBE)
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0 if fallos == 0 else 1


def _medir():
    """LA PRIMERA MITAD DE main(): acotar el acta y contar. Devuelve o bien un
    entero (codigo de salida, cuando hay PARADA) o bien la tupla de lo medido."""
    salida = []
    w = salida.append
    w("=" * 78)
    w("VUELTA %d, TAREA 1.a: EL ACTA %d ENTERA, REGISTRADA"
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
    w("")

    w("B) LAS ADJUDICACIONES NUMERADAS DE LA SECCION 5, CONTADAS Y NO TECLEADAS")
    claves = claves_entrecomilladas(lineas, inicio, fin, PREFIJO_ADJ)
    w("   CIFRA adjudicaciones numeradas halladas: %d" % len(claves))
    for clave, cuantas in claves:
        w("      %s -> %d aparicion(es)" % (clave, cuantas))
    viejas_adj = claves_de_adjudicacion(lineas, inicio, fin, PREFIJO_ADJ)
    w("   el patron SIN comillas, el del acta 183 -> %d sobre esta acta"
      % len(viejas_adj))
    dobles = [c for c, n in claves if n != 1]
    if dobles:
        w("   PARADA: hay claves repetidas dentro del acta: %s" % ", ".join(dobles))
        print(NL.join(salida))
        return 1
    w("")

    w("C) LOS NUMERALES DE LA SECCION 6 Y LAS PREGUNTAS DE LA 7")
    claves_pd = claves_entrecomilladas(lineas, inicio, fin, PREFIJO_PD)
    claves_pr = claves_entrecomilladas(lineas, inicio, fin, PREFIJO_PREG)
    w("   prefijo de la seccion 6: %r -> %d numerales" % (PREFIJO_PD, len(claves_pd)))
    for clave, cuantas in claves_pd:
        w("      %s -> %d aparicion(es)" % (clave, cuantas))
    w("   prefijo de la seccion 7: %r -> %d preguntas" % (PREFIJO_PREG, len(claves_pr)))
    for clave, cuantas in claves_pr:
        w("      %s -> %d aparicion(es)" % (clave, cuantas))
    if len(claves) + len(claves_pd) + len(claves_pr) != len(VIA):
        w("   PARADA: el acta trae %d numerales y las glosas cubren %d."
          % (len(claves) + len(claves_pd) + len(claves_pr), len(VIA)))
        print(NL.join(salida))
        return 1
    w("")

    w("D) LAS CAIDAS, POR SUS FAMILIAS, CON LA ATRIBUCION HECHA POR LA SECCION")
    l_aud = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_AUDITOR_A)
    l_rep = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_REPORTE)
    l_eje_v = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_EJECUTOR_VIEJO)
    l_c_crudo = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_C)
    l_c_nuevo = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_C_ESPACIO)
    c_eje, c_aud, huerfanas = caidas_c_por_seccion(lineas, inicio, fin)
    huerf_viejo = caidas_c_por_seccion(lineas, inicio, fin,
                                       marcas_eje=("EJECUTOR",),
                                       marcas_aud=("MI CAIDA",))
    decl_vieja, decl_nueva = lineas_que_declaran_cero_caidas(lineas, inicio, fin)
    w("   CAIDAS PROPIAS DEL AUDITOR (patron `A.n`): %d, lineas %s"
      % (len(l_aud), ", ".join(str(x) for x in l_aud) or "(ninguna)"))
    w("   EL PATRON `C.n` DE LA 187 (coma o punto pegados), SIN MIRAR LA SECCION: %d"
      % len(l_c_crudo))
    w("      lineas: %s" % (", ".join(str(x) for x in l_c_crudo) or "(ninguna)"))
    w("   EL PATRON `C.n` DE ESTA VUELTA (admite tambien un espacio): %d"
      % len(l_c_nuevo))
    w("      lineas: %s" % (", ".join(str(x) for x in l_c_nuevo) or "(ninguna)"))
    w("   CON EL VOCABULARIO DE CABECERA DE LA 187 (`EJECUTOR` o `MI CAIDA`):")
    w("      ejecutor %d | auditor %d | HUERFANAS %d"
      % (len(huerf_viejo[0]), len(huerf_viejo[1]), len(huerf_viejo[2])))
    for ln, num, cab in huerf_viejo[2]:
        w("         LINEA %d: C.%d bajo %r" % (ln, num, cab[:100]))
    w("   CON EL VOCABULARIO DE ESTA VUELTA (anade `LAS SUYAS`, literal del acta):")
    w("      DEL EJECUTOR: %d" % len(c_eje))
    for ln, num, cab in c_eje:
        w("         LINEA %d: C.%d bajo %r" % (ln, num, cab[:100]))
        w("            %s" % lineas[ln - 1].strip()[:130])
    w("      DEL AUDITOR: %d" % len(c_aud))
    w("      HUERFANAS: %d" % len(huerfanas))
    for ln, num, cab in huerfanas:
        w("         LINEA %d: C.%d bajo %r" % (ln, num, cab[:100]))
    si_acum, no_acum = acumulan(lineas, fin, c_eje)
    w("   LAS DOS CUENTAS, QUE NO SON LA MISMA:")
    w("      CIFRA caidas del ejecutor registradas: %d" % len(c_eje))
    w("      CIFRA de esas que ACUMULAN para alguna racha: %d" % len(si_acum))
    w("      CIFRA de esas que NO acumulan: %d (%s)"
      % (len(no_acum), ", ".join("C.%d" % n for _l, n in no_acum) or "ninguna"))
    w("   CAIDAS DE REPORTE CON EL PATRON `R.n`: %d" % len(l_rep))
    w("   EL PATRON `E.n` DE LAS ACTAS 182 Y 184: %d" % len(l_eje_v))
    w("   LINEAS CON LA FRASE DEL ACTA 186 (%r): %s"
      % (FRASE_CERO_CAIDAS_PROPIAS,
         ", ".join(str(x) for x in decl_nueva) or "(ninguna)"))
    for i in decl_nueva:
        w("      LINEA %d: %s" % (i, lineas[i - 1].strip()[:130]))
    w("   LINEAS CON LA FRASE DEL ACTA 185 (%r): %s"
      % (FRASE_SIN_CAIDA_PROPIA,
         ", ".join(str(x) for x in decl_vieja) or "(ninguna)"))
    if huerfanas:
        w("   PARADA: hay %d caida(s) `C.n` en una seccion cuya cabecera no dice de"
          % len(huerfanas))
        w("   quien son. Una caida sin dueno no se reparte a ojo.")
        print(NL.join(salida))
        return 1
    if not c_eje:
        w("   PARADA: no se encuentra ninguna caida del ejecutor, y el acta 188")
        w("   declara cuatro en su seccion 8. No se escribe una entrada asi.")
        print(NL.join(salida))
        return 1
    if not l_aud and not decl_nueva and not decl_vieja:
        w("   PARADA: cero caidas propias del auditor Y el acta no lo declara por")
        w("   ninguna de las dos frases. Un cero de un patron que no muerde no se")
        w("   publica como medicion.")
        print(NL.join(salida))
        return 1
    w("")
    return (salida, lineas, inicio, fin, claves, claves_pd, claves_pr,
            viejas_adj, l_aud, l_rep, l_eje_v, c_eje, c_aud, decl_vieja,
            decl_nueva, huerf_viejo, si_acum, no_acum, l_c_crudo)


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
    (salida, lineas, inicio, fin, claves, claves_pd, claves_pr, viejas_adj,
     l_aud, l_rep, l_eje_v, c_eje, c_aud, decl_vieja, decl_nueva, huerf_viejo,
     si_acum, no_acum, l_c_crudo) = medido
    w = salida.append

    w("E) EL TITULO, CON SUS CINCO NUMERALES COMPUTADOS")
    titulo = titulo_de_la_entrada(len(claves), len(claves_pd), len(claves_pr),
                                  len(l_aud), len(c_eje))
    w("   %s" % titulo)
    w("")

    w("F) LOS TITULOS LITERALES, LEIDOS DEL ACTA")
    titulos = {}
    for clave, _n in claves + claves_pd + claves_pr:
        pat = re.compile(r"^\s*\*\*`%s` " % re.escape(clave))
        res, err2 = titulo_de_la_negrita(lineas, inicio, fin, pat, clave)
        if err2:
            w("   %s -> %s" % (clave, err2))
            print(NL.join(salida))
            return 1
        titulos[clave] = res
        w("   %s (linea %d): %s" % (clave, res[0], res[1][:130]))
    w("")

    w("G) EL ESTADO DE CADA NUMERAL DE LA SECCION 6, CON LOS DOS VOCABULARIOS")
    pds = pendientes_de_doctrina(lineas, inicio, fin, titulos)
    pds_viejo = pendientes_de_doctrina(lineas, inicio, fin, titulos,
                                       vocabulario_viejo=True)
    estados_viejos = [(c, e) for c, _p, e, _l, _t in pds_viejo]
    for clave, pd, estado, ln, _tit in pds:
        w("   %s nombra %s -> %s (linea %d)" % (clave, pd, estado, ln))
    w("   CON EL VOCABULARIO DE LA 187, SOBRE ESTA MISMA ACTA: %s"
      % "; ".join("%s %s" % (c, e) for c, e in estados_viejos))
    w("   CIFRA `SIN DECIR` con el vocabulario viejo: %d"
      % len([1 for _c, e in estados_viejos if e == "SIN DECIR"]))
    sin_decir = [c for c, _p, e, _l, _t in pds if e == "SIN DECIR"]
    if sin_decir:
        w("   PARADA: %s esta en un estado que este registrador NO SABE LEER."
          % ", ".join(sin_decir))
        print(NL.join(salida))
        return 1
    w("   REPARTO: CERRADAS %d | ABIERTAS %d | ANOTACIONES %d | CORRECCIONES %d"
      % (len([1 for _c, _p, e, _l, _t in pds if e == "CERRADA"]),
         len([1 for _c, _p, e, _l, _t in pds if e == "ABIERTA"]),
         len([1 for _c, _p, e, _l, _t in pds if e == "ANOTACION"]),
         len([1 for _c, _p, e, _l, _t in pds
              if e == "CORRECCION POR DECLARACION"])))
    puestos_pd1 = puestos_de_la_pd1(lineas, inicio, fin, titulos)
    w("   LOS PUESTOS DEL NUMERAL ABIERTO QUE LOS TRAE, LEIDOS DEL ACTA: %s"
      % (", ".join(str(x) for x in puestos_pd1) or "(ninguno)"))
    if not puestos_pd1:
        w("   PARADA: ningun numeral abierto nombra puestos y el acta dice que la")
        w("   `PD.1` tiene cinco. No se escribe una lista vacia.")
        print(NL.join(salida))
        return 1
    w("")

    w("H) LAS PREGUNTAS DE LA SECCION 7, CON SU ESTADO LEIDO DE LA CABECERA")
    preguntas, estado_preg, ln7, cab7 = preguntas_de_la_seccion7(
        lineas, inicio, fin, titulos)
    w("   cabecera de la seccion 7 (linea %s): %s" % (ln7, cab7))
    w("   estado que esa cabecera declara: %s" % estado_preg)
    if estado_preg == "SIN DECIR":
        w("   PARADA: la cabecera de la seccion 7 no dice %r." % MARCA_CONTESTADAS)
        print(NL.join(salida))
        return 1
    for clave, pr, ln, _tit in preguntas:
        w("   %s nombra %s -> %s (linea %d)" % (clave, pr, estado_preg, ln))
    w("")

    w("I) EL NUMERO DE LA ENTRADA, QUE NO SE TECLEA")
    halladas = SERIE.entradas()
    numero = SERIE.siguiente_libre(halladas)
    w("   serie recomputada de sus dos sedes: %d entradas" % len(halladas))
    w("   CIFRA colisiones: %d | CIFRA huecos: %d"
      % (len(SERIE.colisiones(halladas)), len(SERIE.huecos(halladas))))
    w("   SIGUIENTE LIBRE: R.%d" % numero)
    w("")

    w("J) LA DEUDA DE LA SERIE, REMEDIDA EN ESTA VUELTA Y NO HEREDADA DEL R.49")
    salto = actas_sin_entrada(halladas, 173, VUELTA_DEL_ACTA - 1)
    faltan, bajo, alto = salto
    w("   tramo mirado: actas 173 a %d" % (VUELTA_DEL_ACTA - 1))
    w("   CIFRA actas SIN entrada propia en la serie: %d" % len(faltan))
    w("   LAS QUE FALTAN: %s" % (", ".join(str(x) for x in faltan) or "(ninguna)"))
    w("   EXTREMO BAJO: %s"
      % ("R.%d cubre el acta %d" % bajo if bajo else "(ninguno)"))
    w("   EXTREMO ALTO: %s"
      % ("R.%d cubre el acta %d" % alto if alto else "(ninguno)"))
    w("")

    marca = "## R.%d." % numero
    texto_sede = io.open(SEDE, encoding="utf-8").read().replace(chr(13) + NL, NL)
    ya = ("## R.%d. %s" % (numero, titulo)) in texto_sede
    w("K) LA IDEMPOTENCIA, COMPROBADA ANTES DE ESCRIBIR")
    w("   la marca %r ya esta en la sede: %s"
      % (marca, "SI" if marca in texto_sede else "NO"))
    w("   la entrada entera ya esta: %s" % ("SI" if ya else "NO"))
    w("")

    entrada = armar_entrada(numero, titulo, claves, pds, preguntas, estado_preg,
                            (ln7, cab7), titulos, l_aud, decl_vieja, decl_nueva,
                            inicio, fin, len(viejas_adj), len(l_rep),
                            len(l_eje_v), c_eje, c_aud, huerf_viejo, si_acum,
                            no_acum, estados_viejos, puestos_pd1, salto, lineas,
                            len(l_c_crudo))
    w("L) LA ENTRADA ARMADA")
    w("   %d bytes | %d lineas" % (len(entrada.encode("utf-8")), entrada.count(NL)))
    w("")

    if a.simular:
        w("M) MODO --simular: NO SE ESCRIBE NADA EN LA SEDE.")
        w("")
        w("LA ENTRADA, ENTERA:")
        for l in entrada.split(NL):
            w("   | " + l)
    elif ya:
        w("M) NO SE ESCRIBE: la entrada ya esta en la sede, byte a byte.")
    else:
        nuevo = texto_sede.rstrip(NL) + NL + NL + entrada
        io.open(SEDE, "w", encoding="utf-8", newline=NL).write(nuevo)
        w("M) ESCRITA EN docs/PENDIENTES.md")
        w("   la sede pasa de %d a %d bytes"
          % (len(texto_sede.encode("utf-8")), len(nuevo.encode("utf-8"))))
        rele = io.open(SEDE, encoding="utf-8").read().replace(chr(13) + NL, NL)
        w("   RELEIDA DEL DISCO: la entrada esta byte a byte: %s"
          % ("SI" if entrada.rstrip(NL) in rele else "NO"))
        w("   guiones largos o medios en la entrada: %d"
          % (entrada.count(chr(8212)) + entrada.count(chr(8211))))
        de_nuevo = SERIE.entradas()
        w("   SERIE RECOMPUTADA DESPUES DE ESCRIBIR: %d entradas, siguiente libre R.%d"
          % (len(de_nuevo), SERIE.siguiente_libre(de_nuevo)))
        w("   CIFRA colisiones: %d | CIFRA huecos: %d"
          % (len(SERIE.colisiones(de_nuevo)), len(SERIE.huecos(de_nuevo))))
    w("")
    t = NL.join(salida) + NL
    ruta = os.path.join(LOOP, "SALIDA_V%s_T1A_REGISTRO_R%d.txt"
                        % (SUFIJO_QUE_ESCRIBE, numero))
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
