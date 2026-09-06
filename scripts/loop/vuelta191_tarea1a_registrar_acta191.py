# -*- coding: utf-8 -*-
r"""vuelta191_tarea1a_registrar_acta191.py . EL ACTA 191 ENTERA, REGISTRADA EN LA
SERIE `R.N` EN LA FORMA DE LA CASA, Y ESTE REGISTRADOR SIGUE SIENDO IDEMPOTENTE.

LA MAQUINA NO SE CLONA, SE IMPORTA, y eso lo adjudico la `6.6` del acta 172 como
correcto y obligatorio. De la cadena de registradores se importan
`titulo_de_la_negrita`, `claves_de_adjudicacion`, `claves_entrecomilladas`,
`cuenta_por_patron`, `actas_sin_entrada`, `PALABRA_CON_CERO`, los patrones de
caida, **la idempotencia entera** (`marcas_del_acta` y `entradas_que_registran`
del registrador de la 189) y del registrador de la 190 la maquina que ESTA vuelta
necesita entera: `cuerpo_del_acta`, `rango_de_seccion`, `parrafos_con_negrita`,
`caidas_en_linea`, `familia_de_la_adjudicacion`, `_normalizar`,
`fila_de_la_metrica` y `secciones_del_acta`.

**LO PROPIO DE ESTE FICHERO SON LAS CUATRO COSAS QUE EL ACTA 191 ESTRENA**, y las
cuatro salen de correr la maquinaria heredada sobre el acta 191 y ver donde se
rompe, no de suponerlas:

  1) NO HAY NINGUNA ADJUDICACION `EN CONTRA`, Y LA MAQUINA DE LA 190 SE ROMPE
     JUSTO POR ESO. El `main()` del registrador de la 190 lleva escrito
     `if not en_contra: PARADA`, porque su acta declaraba una y queria que la
     marca nueva se viera de verdad. **Sobre el acta 191, que no tiene ninguna,
     esa guarda para un acta perfectamente legible.** Aqui el cero de `EN CONTRA`
     **es un resultado y se publica como tal**, y lo que sigue parando es lo que
     de verdad no se puede leer: un discutible cuyo estado no sea NI a favor NI
     en contra. Su caso positivo por mutacion fabrica un acta que SI lleva un
     `EN CONTRA` y exige que la cuenta lo vea, y corre ademas la guarda VIEJA de
     la 190 sobre el acta de hoy para publicar que habria parado.

  2) LAS TRES PREGUNTAS SE CONTESTAN CON TRES MARCAS QUE EL VOCABULARIO NO TIENE.
     `4.7` cierra en `LA MITAD BARATA SE ADJUDICA, LA CARA NO SE TOCA`, `4.8` en
     `ENCARGADA COMO BLOQUEANTE` y `4.9` en `SI, POR EXTENSION CITABLE Y SIN
     DOCTRINA NUEVA`. **Ninguna de las seis marcas de la 190 las ve**, y con el
     vocabulario heredado las tres saldrian `SIN DECIR` y este instrumento haria
     PARADA. Las tres se anaden LITERALES, y **la PARADA por `SIN DECIR` se
     conserva entera**.

  3) LAS CAIDAS DEL ACTA 191 NO SE LLAMAN `C.n`: SE LLAMAN POR LA CLAVE DEL
     DOCUMENTO QUE LAS DECLARA. Su seccion 6 dice `Declara tres (5.1, ...; 5.2,
     ...; 5.3, ...)` para el ejecutor, que son claves del REPORTE de la 190, y
     `MIAS: UNA, DE METODO, Y ES LA 5.3` para el auditor, que es clave de ESTA
     acta. **El patron `C.n` da CERO sobre esta seccion**, medido y no supuesto,
     asi que la maquina de la 190 sacaria `(0, 0, 0)` y su guarda `if not c_eje`
     pararia. Aqui las caidas se cuentan por la clave `N.M` entrecomillada y **la
     atribucion la sigue haciendo LA NEGRITA QUE ABRE EL PARRAFO**, importada
     tal cual. **La PARADA por huerfana se conserva entera.**

  4) LA FILA DE LA TABLA QUE DICE CUALES HALLAZGOS CUENTAN FUERA SEPARA POR COMA
     Y NO POR PUNTO Y COMA, Y ADEMAS PARAFRASEA. `piezas_de_la_fila()` de la 190
     parte por `;`: sobre esta fila da UNA sola pieza y casa con CERO hallazgos,
     o sea PARADA. Partiendo tambien por `,` da TRES piezas y casa con UNO, y
     **eso tampoco decide nada por si solo**. Quien decide es **el numeral de la
     propia fila**, leido de ella: si dice tantos como claves `5.n` tiene la
     seccion, los `5.n` que cuentan fuera son TODOS, y el cotejo por subcadena se
     publica al lado **como lo que es, una medicion mas debil que solo resuelve
     una de las tres porque el acta parafrasea en vez de citar**.

LA PARADA SE CONSERVA ENTERA: un estado, una atribucion o una cuenta que este
registrador no sepa leer sigue siendo PARADA, y no se resuelve a ojo.

LO QUE ESTE FICHERO NO HACE: no toca el acta, no toca el reporte, no toca
`docs/plan/` salvo para LEER, no corre la bateria, no toca ninguna guarda de la
nomina y no escribe ningun veredicto. Escribe UNA entrada en UNA sede, y si el
acta ya esta registrada, NO escribe nada.

USO:
  python scripts/loop/vuelta191_tarea1a_registrar_acta191.py
  python scripts/loop/vuelta191_tarea1a_registrar_acta191.py --simular
  python scripts/loop/vuelta191_tarea1a_registrar_acta191.py --mutacion
"""
import argparse
import hashlib
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
    PALABRA_CON_CERO, PAT_CAIDA_AUDITOR_A, PAT_CAIDA_EJECUTOR_VIEJO,
    PAT_CAIDA_REPORTE, PAT_P_DEL_TITULO)
from vuelta187_tarea1a_registrar_acta187 import PAT_CAIDA_C   # noqa: E402
from vuelta188_tarea1a_registrar_acta188 import PAT_CAIDA_C_ESPACIO   # noqa: E402
from vuelta189_tarea1a_registrar_acta189 import (   # noqa: E402
    marcas_del_acta, entradas_que_registran, caidas_por_seccion)
from vuelta190_tarea1a_registrar_acta190 import (   # noqa: E402
    cuerpo_del_acta, rango_de_seccion, parrafos_con_negrita, caidas_en_linea,
    familia_de_la_adjudicacion, fila_de_la_metrica, secciones_del_acta,
    _normalizar, _lista, PAT_C_EN_LINEA,
    MARCAS_LEAD_EJECUTOR, MARCAS_LEAD_AUDITOR, MARCAS_CERO_DE_CUENTA,
    MARCAS_CERO_DE_RACHA)

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
# NO SE TOCA: el acta se abre SOLO EN LECTURA y su sha256 se publica.
ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")
SEDE = os.path.join(RAIZ, "docs", "PENDIENTES.md")
NL = chr(10)

VUELTA_DEL_ACTA = 191
VUELTA_QUE_ESCRIBE = 191
SUFIJO_QUE_ESCRIBE = "191"
CABECERA_ACTA = "# ACTA DEL AUDITOR, VUELTA %d" % VUELTA_DEL_ACTA
PREFIJO_ADJ = "4."
PREFIJO_HALLAZGO = "5."
SECCION_DE_LOS_HALLAZGOS = 5
SECCION_DE_LAS_CAIDAS = 6
SECCION_DE_LA_METRICA = 7

# LAS MARCAS DE ESTADO DE UNA ADJUDICACION, LEIDAS DEL TITULO LITERAL. Ninguna se
# ensancha: se buscan tal cual y EN ESTE ORDEN. `EN CONTRA` sigue yendo PRIMERA,
# aunque esta acta no tenga ninguna: el orden es de la 190 y no se toca por que
# hoy no muerda.
MARCA_EN_CONTRA = "EN CONTRA"
MARCA_A_FAVOR = "A FAVOR"
# LAS TRES MARCAS QUE EL ACTA 191 ESTRENA, LITERALES DE SUS TRES PREGUNTAS.
MARCA_MITAD_BARATA = "LA MITAD BARATA SE ADJUDICA"
MARCA_ENCARGADA_BLOQUEANTE = "ENCARGADA COMO BLOQUEANTE"
MARCA_EXTENSION_CITABLE = "POR EXTENSION CITABLE"
# LAS DE LA 190, QUE SE CONSERVAN AUNQUE HOY NO MUERDAN: retirarlas seria
# estrechar el vocabulario a lo que el acta de hoy usa, y la proxima acta que las
# use haria PARAR el instrumento.
MARCA_CUENTA_COMO_CORRIDO = "CUENTA COMO CORRIDO"
MARCA_PRIMERO_SE_MIDE = "PERO PRIMERO SE MIDE"
MARCA_SE_RESTAURA = "SE RESTAURA SIEMPRE"
MARCA_CADUCA = "SE CUMPLIO Y CADUCA"

MARCA_ESPECIE_METODO = "DE METODO"

# LAS CLAVES `N.M` ENTRECOMILLADAS, QUE ES COMO EL ACTA 191 NOMBRA SUS CAIDAS.
PAT_CLAVE_NUMERAL = re.compile(r"`(\d+\.\d+)`")
AGUJA_FILA_FUERA = "discrepancias y hallazgos FUERA del marcado"
AGUJA_FILA_CAIDAS_AUDITOR = "caidas propias del auditor"
AGUJA_FILA_CAIDAS_METODO = "caidas del ejecutor de metodo"
AGUJA_FILA_PUESTOS = "puestos"
# LA NOTA QUE EL ENCARGO MANDA REGISTRAR CON ESAS PALABRAS, BUSCADA EN LA FILA DE
# PUESTOS. No se parafrasea: si no esta, se dice que no esta.
#
# Y LA CAJA NO SE EXIGE, PERO SE MIDE Y SE PUBLICA. El encargo la escribe
# `SOLAPE TOTAL` y el acta la escribe `solape TOTAL`: son LAS MISMAS PALABRAS con
# otra caja. Exigirla literal caracter a caracter habria hecho PARAR este
# instrumento por una mayuscula, que es lo contrario de lo que la guarda existe
# para cazar; ignorarla del todo seria dejar de mirar. Se compara en mayusculas y
# **se publica el literal que el acta trae de verdad**.
NOTA_DE_PUESTOS = "SOLAPE TOTAL"


def estado_de_la_adjudicacion(titulo):
    """EL ESTADO DE UNA ADJUDICACION, LEIDO DE SU TITULO LITERAL. PURA.

    NO SE TECLEA NINGUNO: se busca en el titulo, EN ESTE ORDEN, `EN CONTRA`,
    `A FAVOR`, y despues las marcas de pregunta contestada, las TRES nuevas del
    acta 191 primero y las CUATRO heredadas de la 190 detras. **Si un titulo no
    dijera ninguna, el estado sale `SIN DECIR` y quien llama hace PARADA en vez
    de suponer.**

    `EN CONTRA` VA LA PRIMERA A PROPOSITO, Y SE QUEDA AUNQUE ESTA ACTA NO TENGA
    NINGUNA: un titulo que tumbara una cosa y adjudicara a favor de otra tiene
    que salir EN CONTRA, porque lo que hay que hacer sale de lo que se tumba."""
    alto = titulo.upper()
    if MARCA_EN_CONTRA in alto:
        return "EN CONTRA"
    if MARCA_A_FAVOR in alto:
        return "A FAVOR"
    if MARCA_MITAD_BARATA in alto:
        return "CONTESTADA A MEDIAS, LA MITAD BARATA ADJUDICADA"
    if MARCA_ENCARGADA_BLOQUEANTE in alto:
        return "CONTESTADA Y ENCARGADA COMO BLOQUEANTE"
    if MARCA_EXTENSION_CITABLE in alto:
        return "CONTESTADA A FAVOR POR EXTENSION CITABLE"
    if MARCA_CUENTA_COMO_CORRIDO in alto:
        return "CONTESTADA Y ENCARGADA"
    if MARCA_PRIMERO_SE_MIDE in alto:
        return "CONTESTADA Y ENCARGADA CON MEDICION PREVIA"
    if MARCA_SE_RESTAURA in alto:
        return "CONTESTADA Y ENCARGADA"
    if MARCA_CADUCA in alto:
        return "REGLA CUMPLIDA QUE CADUCA"
    return "SIN DECIR"


def caidas_por_numeral(lineas, ini, fin, marcas_eje=None, marcas_aud=None,
                       marcas_cero_cuenta=None, marcas_cero_racha=None,
                       patron=None):
    """LAS CAIDAS NOMBRADAS POR SU CLAVE `N.M`, REPARTIDAS POR LA NEGRITA QUE ABRE
    SU PARRAFO. Devuelve (del_ejecutor, del_auditor, huerfanas). PURA.

    Cada elemento es (linea_del_parrafo, clave, negrita).

    POR QUE HACE FALTA, Y ES UNA MEDICION: el acta 191 no escribe `C.n` en su
    seccion 6. Escribe `Declara tres (5.1, ...; 5.2, ...; 5.3, ...)` para el
    ejecutor, con las claves del REPORTE de la 190, y `MIAS: UNA, DE METODO, Y ES
    LA 5.3` para el auditor, con la clave de esta misma acta. **El patron `C.n`
    da CERO sobre esta seccion**, y con cero la guarda de la 190 para.

    LO QUE NO CAMBIA, Y ES LA MITAD QUE IMPORTA: la atribucion la sigue haciendo
    LA NEGRITA QUE ABRE EL PARRAFO, importada de la 190 sin tocarla, con sus dos
    especies de cero. **El cero de CUENTA neutraliza; el de RACHA no.** Una clave
    en un parrafo cuya negrita no diga de quien es sale HUERFANA y quien llama
    hace PARADA.

    LAS CLAVES SE DEDUPLICAN POR PARRAFO a proposito: el parrafo del ejecutor
    nombra `5.2` dos veces (la tercera caida y, al final, el hallazgo `5.2` del
    propio auditor). Contar apariciones en vez de claves distintas daria cuatro
    donde el acta declara tres."""
    m_eje = tuple(marcas_eje) if marcas_eje is not None else MARCAS_LEAD_EJECUTOR
    m_aud = tuple(marcas_aud) if marcas_aud is not None else MARCAS_LEAD_AUDITOR
    m_cc = (tuple(marcas_cero_cuenta) if marcas_cero_cuenta is not None
            else MARCAS_CERO_DE_CUENTA)
    m_cr = (tuple(marcas_cero_racha) if marcas_cero_racha is not None
            else MARCAS_CERO_DE_RACHA)
    pat = patron if patron is not None else PAT_CLAVE_NUMERAL
    eje, aud, huerfanas = [], [], []
    for a, _b, negrita, texto in parrafos_con_negrita(lineas, ini, fin):
        claves = sorted(set(pat.findall(texto)),
                        key=lambda x: [int(y) for y in x.split(".")])
        if not claves:
            continue
        alta = negrita.upper()
        es_cero_de_cuenta = any(x in alta for x in m_cc)
        _es_cero_de_racha = any(x in alta for x in m_cr)
        if any(x in alta for x in m_eje) and not es_cero_de_cuenta:
            destino = eje
        elif any(x in alta for x in m_aud):
            destino = aud
        else:
            destino = huerfanas
        for k in claves:
            destino.append((a, k, negrita))
    return eje, aud, huerfanas


def piezas_de_la_fila(texto_de_la_fila, separadores=(";", ",")):
    """LOS TROZOS DEL PARENTESIS DE UNA FILA DE LA TABLA DE CREDITO. PURA.

    CLON DECLARADO del de la 190 CON UNA DIFERENCIA DECLARADA Y MEDIDA: los
    separadores son PARAMETRO. La fila de la 190 separaba por `;` y la del acta
    191 separa por `,`; partiendo solo por `;` esta fila da UNA pieza y casa con
    CERO hallazgos. **Las dos particiones se corren y las dos cifras se
    publican**, que es lo que la casa hace con los BYTES y con las LINEAS."""
    m = re.findall(r"\(([^)]*)\)", texto_de_la_fila)
    if not m:
        return []
    crudo = m[-1]
    trozos = [crudo]
    for sep in separadores:
        siguiente = []
        for t in trozos:
            siguiente.extend(t.split(sep))
        trozos = siguiente
    piezas = []
    for trozo in trozos:
        p = _normalizar(trozo)
        p = re.sub(r"^(las|los|la|el) ", "", p)
        if p:
            piezas.append(p)
    return piezas


def numeral_de_la_fila(texto_de_la_fila):
    """LA CIFRA DE LA SEGUNDA CELDA DE UNA FILA DE LA TABLA DE CREDITO. PURA.

    Devuelve el entero o None. **Es quien decide cuantos hallazgos cuentan
    fuera del marcado cuando el parentesis parafrasea en vez de citar**, y por
    eso se lee de la fila y no se teclea. Una fila cuya celda no traiga cifra
    devuelve None y quien llama hace PARADA."""
    celdas = [c.strip() for c in texto_de_la_fila.strip().strip("|").split("|")]
    if len(celdas) < 2:
        return None
    m = re.search(r"\*\*(\d+)\*\*|^(\d+)\b", celdas[1])
    if not m:
        return None
    return int(m.group(1) or m.group(2))


def hallazgos_que_la_tabla_nombra(hallazgos, texto_de_la_fila,
                                  separadores=(";", ",")):
    """CUALES `5.n` NOMBRA POR SUBCADENA LA FILA `hallazgos FUERA del marcado`.
    PURA. Devuelve (nombrados, no_nombrados, piezas).

    CLON DECLARADO del de la 190 con los separadores como parametro. **Y con su
    alcance dicho en voz alta: esto NO decide cuantos cuentan.** Sobre el acta
    191 casa UNO de TRES, porque la fila parafrasea (`la restauracion que no
    restaura`) donde el titulo dice otra cosa (`git checkout -- NO ES
    RESTAURACION BYTE A BYTE`). Quien decide es `numeral_de_la_fila()`."""
    piezas = piezas_de_la_fila(texto_de_la_fila, separadores)
    nombrados, sueltos = [], []
    for clave, ln, tit in hallazgos:
        t = _normalizar(tit)
        casan = [p for p in piezas if p in t]
        if casan:
            nombrados.append((clave, ln, tit, casan))
        else:
            sueltos.append((clave, ln, tit))
    return nombrados, sueltos, piezas


def filas_de_la_metrica(lineas, ini, fin):
    """TODAS LAS FILAS DE DATOS DE LA TABLA DE CREDITO. PURA.

    Devuelve [(linea, texto)] saltando la cabecera y el separador. Existe porque
    el encargo pide LA METRICA ENTERA con sus cifras y no solo tres filas
    escogidas: una tabla se pega entera o no se pega."""
    salida = []
    for i in range(ini, fin + 1):
        l = lineas[i - 1].strip()
        if not l.startswith("|"):
            continue
        if set(l) <= set("|-: "):
            continue
        if l.startswith("| |"):
            continue
        salida.append((i, l))
    return salida


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
    "4.4": "SIN TOCAR NADA",
    "4.5": "EJECUTADA EN LA TAREA 2",
    "4.6": "SIN TOCAR NADA",
    "4.7": "REGISTRADA AQUI, Y SU ESTADO NO SE MUEVE",
    "4.8": "EJECUTADA EN LA TAREA 2",
    "4.9": "A LA VUELTA 192",
    "5.1": "ES LA TAREA 5 DE ESTA VUELTA",
    "5.2": "ES LA TAREA 4 DE ESTA VUELTA",
    "5.3": "SIN TOCAR NADA",
}

QUE_HACE_ESTA_VUELTA = {
    "4.1": ("SE ACATA SIN TOCAR NADA. Ampliar la guarda por una funcion hermana "
            "en vez de cambiarle la firma queda a favor, y el motivo que el acta "
            "da es el que esta vuelta hereda: **la hermana LLAMA a la original en "
            "vez de copiar su logica**, asi que no hay dos fuentes de verdad. "
            "**Esta vuelta no toca ninguna guarda de la nomina** y no vuelve a "
            "abrir esa decision."),
    "4.2": ("SE ACATA SIN TOCAR NADA. La vara del `MOTIVO ESCRITO` queda a favor "
            "no por razonable sino **por cuando se escribio**, antes de medir y "
            "publicada en la simulacion previa. **Esta vuelta no la mueve ni la "
            "estrecha**, y su fragilidad sigue declarada en el instrumento con su "
            "fecha, que es donde se puede discutir."),
    "4.3": ("SE ACATA SIN TOCAR NADA. Que el exitcode de la deuda sea `2` queda a "
            "favor, y el acta dice ademas que **que numero exacto sea no lo fija "
            "ninguna regla**. **Esta vuelta no corre la bateria ni toca su "
            "lanzador**, asi que el `2` se queda donde esta."),
    "4.4": ("SE ACATA SIN TOCAR NADA. Que `SUJETO VIVO` cuente como FALLO y no "
            "como deuda queda a favor, y el acta mide lo que eso mueve HOY: "
            "**cero**, porque esa lista esta vacia. **Decide como se leeran las "
            "proximas vueltas y no mueve ninguna cifra de esta.**"),
    "4.5": ("SE ACATA Y SE EJECUTA EN LA TAREA 2 DE ESTA VUELTA. Que la tarea 4 de "
            "la 190 NO se auto encargara su relectura al doble queda a favor: "
            "**`AUDITOR.md` 1.2 pone el doble en la mano del auditor**, y el acta "
            "191 la encarga ella misma como TAREA 2 bloqueante. **Traerla medida "
            "fue lo correcto; encargarsela a si mismo no lo habria sido.**"),
    "4.6": ("SE ACATA SIN TOCAR NADA. No darle sede a `OP-L-02` pudiendo "
            "argumentarlo queda a favor **y el acta anade que era lo unico que se "
            "podia hacer**: declarar que una salida de vuelta cuenta como producto "
            "documental **cambia el criterio de HECHO de la fase 08**, y eso lo "
            "reserva el fundador. **Esta vuelta no toca `docs/plan/` mas que para "
            "leer.**"),
    "4.7": ("REGISTRADA AQUI, Y SU ESTADO NO SE MUEVE. La mitad barata queda "
            "adjudicada (que el campo `evidencia` **nombre los ficheros que ya "
            "existen**), y la cara no se toca. **El encargo de esta vuelta la "
            "deja EXPRESAMENTE fuera** y dice con esas palabras que `OP-L-02` "
            "**sigue en `LISTA`** y que declararla HECHA es del fundador. **Esta "
            "vuelta no escribe ni una linea de `docs/plan/OPERACIONES.jsonl`.**"),
            # NO SE TOCA ni una linea de OPERACIONES.jsonl: es texto de la glosa.
    "4.8": ("CONTESTADA Y EJECUTADA EN LA TAREA 2 DE ESTA VUELTA. Que la "
            "discrepancia del `3182` baja el credito de la tanda queda contestado "
            "que SI, y con una precision que el acta subraya: **la relectura del "
            "auditor sobre los mismos 30 NO es el doble y no lo sustituye**. Al "
            "doble es **mas extension**, treinta vecinos nuevos; lo del auditor es "
            "**otro lector sobre la misma extension**. **Son dos controles "
            "distintos y en esta vuelta corren los dos.**"),
    "4.9": ("CONTESTADA A FAVOR Y NO ENTRA EN ESTA VUELTA, Y EL PROPIO ENCARGO LO "
            "DICE PARA QUE LA 192 NO LA REDESCUBRA. Que el exitcode `2` deba "
            "propagarse a `--componer` sale **por extension citable del banco 9 y "
            "sin doctrina nueva**: una composicion que aplana los dos rojos que el "
            "tramo distinguio comete la misma falta un piso mas arriba. **Esta "
            "vuelta no corre la bateria ni toca su lanzador.**"),
    "5.1": ("HALLAZGO DEL AUDITOR FUERA DE LO QUE EL REPORTE MARCA, Y ES LA TAREA "
            "5 DE ESTA VUELTA. Ocho de los treinta tumban a los dos lectores y "
            "ninguno lleva la marca `DISCUTIBLE MARCADO` que 427 filas del archivo "
            "si llevan. **El encargo lo manda medir sobre toda la historia de "
            "ciegas y no sobre treinta casos**, con el universo declarado ANTES de "
            "contar, y **prohibe escribir ni una fila del archivo**: ponerle la "
            "marca a ocho razones seria editar datos publicados sobre una muestra "
            "de treinta."),
    "5.2": ("HALLAZGO DEL AUDITOR FUERA DE LO QUE EL REPORTE MARCA, Y ES LA TAREA "
            "4 DE ESTA VUELTA. La etiqueta del veredicto sale duplicada porque "
            "`cerrar_reporte.py` la pega sin comprobar si ya venia puesta. **El "
            "arreglo es que CAIGA EN ROJO diciendo que recibio y que esperaba**, "
            "no que la limpie en silencio. **Y el reporte de la 190 no se "
            "reescribe:** esta cerrado y archivado byte a byte."),
    "5.3": ("SE ACATA SIN TOCAR NADA, Y ESTA VUELTA LA APLICA COMO REGLA DE "
            "TRABAJO. `git checkout --` devuelve el fichero en CRLF y cambia los "
            "bytes publicados, asi que **una salida sellada ajena que se pise se "
            "restaura leyendo el blob y escribiendolo en LF, y se REMIDE antes de "
            "darla por restaurada**. **Es caida propia del auditor, declarada por "
            "el, y esta vuelta la hereda como precaucion y no como reproche.**"),
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
    p.append("Por adicion, como `R.21` a `R.52`. **Corte de todas las cifras de esta")
    p.append("entrada: 6 sep 2026.** El numero de esta entrada NO esta tecleado: lo computa")
    p.append("`scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS sedes.")
    p.append("La SEDE tampoco se supone: sale de la adjudicacion 6.3 del acta 162, que es")
    p.append("la que citan los `R.30` a `R.52`. Salida:")
    p.append("`docs/loop/SALIDA_V%s_T1A_REGISTRO_R%d.txt`."
             % (SUFIJO_QUE_ESCRIBE, numero))
    p.append("")
    p.append("**ESTA ENTRADA SE ESCRIBE CON LA TAREA 1 EN CURSO Y LAS TAREAS 2 A 5 SIN")
    p.append("EMPEZAR, ASI QUE SUS GLOSAS NO AFIRMAN EN PASADO LO QUE TODAVIA NO HA")
    p.append("PASADO.** Es la forma que la `6.4` del acta 172 adjudico como correcta.")
    p.append("")
    p.append("**Y LOS CINCO NUMERALES DEL TITULO TAMPOCO ESTAN TECLEADOS:** se cuentan del")
    p.append("acta acotada (lineas %d a %d) y de ahi sale el numeral en palabra, incluida"
             % (m["inicio"], m["fin"]))
    p.append("la concordancia. **%d adjudicaciones numeradas (`4.1` a `4.%d`, todas en la"
             % (m["n_adj"], m["n_adj"]))
    p.append("seccion 4), %d hallazgos numerados en la seccion 5, %d preguntas contestadas"
             % (m["n_hall"], m["n_preg"]))
    p.append("DENTRO de las adjudicaciones, %d caida propia del auditor y %d caidas del"
             % (m["n_aud"], m["n_eje"]))
    p.append("ejecutor.**")
    p.append("")
    p.append("**LA FORMA DE LOS NUMERALES SE MIDE CON LOS DOS PATRONES Y LAS DOS CIFRAS SE")
    p.append("PUBLICAN.** Corrido sobre esta acta, **el patron entrecomillado (el del acta")
    p.append("188) da %d y el suelto (el del acta 189) da %d**. **Ninguno de los dos se"
             % (m["n_entrecomillado"], m["n_adj"]))
    p.append("ensancha: se corren los dos y se dice lo que dan.**")
    p.append("")
    p.append("**LO QUE ESTA ACTA ESTRENA, Y ES UN CERO: NO HAY NINGUNA ADJUDICACION `EN")
    p.append("CONTRA`, Y LA MAQUINA DE LA 190 SE ROMPE JUSTO POR ESO.** De las %d que"
             % m["n_adj"])
    p.append("nombran un `D.n` o un `P.n`, **%d son discutibles del ejecutor y los %d van A"
             % (m["n_discutibles"], m["n_a_favor_discutibles"]))
    p.append("FAVOR**; **EN CONTRA salen %d**. El registrador de la 190 llevaba escrito en"
             % m["n_en_contra_discutibles"])
    p.append("su `main()` un `if not en_contra: PARADA`, puesto a proposito porque su acta")
    p.append("declaraba una y queria que la marca nueva se viera de verdad. **Corrida esa")
    p.append("guarda vieja sobre el acta %d, PARA: %s.** Aqui el cero es un RESULTADO y se"
             % (VUELTA_DEL_ACTA, "SI" if m["vieja_pararia"] else "no"))
    p.append("publica como tal, y **lo que sigue parando es lo que de verdad no se puede")
    p.append("leer**: un discutible cuyo estado no sea NI a favor NI en contra, que hoy son")
    p.append("**%d**." % m["n_discutibles_sin_sentido"])
    p.append("")
    p.append("**Y LA SEGUNDA COSA QUE ESTRENA: LAS TRES PREGUNTAS SE CONTESTAN CON TRES")
    p.append("MARCAS QUE EL VOCABULARIO NO TENIA.** Corrido con el vocabulario de la 190 y")
    p.append("nada mas, **%d titulo(s) saldrian `SIN DECIR`** y este instrumento haria"
             % m["n_sin_decir_vieja"])
    p.append("PARADA sobre un acta perfectamente legible. Las tres marcas se anaden")
    p.append("LITERALES (`%s`, `%s` y `%s`), **las cuatro heredadas de la 190 se conservan"
             % (MARCA_MITAD_BARATA, MARCA_ENCARGADA_BLOQUEANTE,
                MARCA_EXTENSION_CITABLE))
    p.append("aunque hoy no muerdan** (estrechar el vocabulario a lo que el acta de hoy usa")
    p.append("haria parar la proxima que las use) y **la PARADA por `SIN DECIR` se conserva")
    p.append("entera**.")
    p.append("")
    p.append("**LAS %s ADJUDICACIONES NUMERADAS, CON SU LINEA EN EL ACTA LEIDA HOY.** El"
             % PALABRA_CON_CERO[m["n_adj"]].upper())
    p.append("titulo de cada una es LITERAL del fichero; la glosa que sigue es prosa del")
    p.append("ejecutor y va marcada como tal.")
    p.append("")
    for clave, familia, estado, ln, tit in m["adjudicaciones"]:
        # NO SE TOCA: es una CITA de la linea del acta dentro del texto de la entrada.
        p.append("  - **`%s` (`docs/loop/ACTA_AUDITOR.md:%d`, leida hoy). FAMILIA: %s. "
                 "ESTADO: %s. VIA: %s.** Titulo" % (clave, ln, familia, estado,
                                                    VIA.get(clave, "(sin via)")))
        p.append("    literal del acta: *\"%s\"*" % tit)
        p.append("    **QUE HACE ESTA VUELTA CON ELLA (glosa del ejecutor, no del acta):** %s"
                 % QUE_HACE_ESTA_VUELTA.get(clave, "(sin glosa)"))
    p.append("")
    p.append("**LAS %s PREGUNTAS ESTAN CONTESTADAS Y NO TIENEN SECCION PROPIA:** viven"
             % PALABRA_CON_CERO[m["n_preg"]].upper())
    p.append("DENTRO de las adjudicaciones, como en las actas 189 y 190. **Cuales son NO se")
    p.append("teclea:** son las %d cuyo titulo nombra un `P.n`, y son **%s**."
             % (m["n_preg"],
                ", ".join("`%s` que nombra `%s`" % (c, pn) for c, pn in m["preguntas"])))
    p.append("")
    p.append("**LOS %s HALLAZGOS DE LA SECCION 5, Y LOS %s CUENTAN COMO HALLAZGO FUERA DEL"
             % (PALABRA_CON_CERO[m["n_hall"]].upper(),
                PALABRA_CON_CERO[m["n_fuera"]].upper()))
    p.append("MARCADO. CUANTOS NO SE TECLEA, Y AQUI HAY QUE DECIR POR QUE LA MAQUINA DE LA")
    p.append("190 TAMPOCO PODIA CON ESTO.** Su `piezas_de_la_fila()` parte el parentesis por")
    p.append("`;`, y **la fila del acta 191 separa por `,`**: partiendo solo por `;` da")
    p.append("**%d** pieza(s) y casa con **%d** hallazgo(s), o sea PARADA. Partiendo tambien"
             % (m["n_piezas_pyc"], m["n_casan_pyc"]))
    p.append("por `,` da **%d** piezas y casa con **%d**, **y eso tampoco decide nada por si"
             % (m["n_piezas"], len(m["hall_nombrados"])))
    p.append("solo**, porque la fila PARAFRASEA donde el titulo dice otra cosa. **Quien")
    p.append("decide es el numeral de la propia fila, leido de ella: dice %d, y la seccion"
             % m["numeral_fila"])
    p.append("tiene %d claves `5.n`.** La fila, leida del fichero:" % m["n_hall"])
    p.append("")
    for ln, txt in m["fila_fuera"]:
        # NO SE TOCA: es una CITA de la linea del acta dentro del texto de la entrada.
        p.append("  - `docs/loop/ACTA_AUDITOR.md:%d`: %s" % (ln, txt))
    p.append("")
    p.append("  Las piezas que salen de su parentesis partiendo por `;` y por `,`: %s."
             % (", ".join("*%s*" % x for x in m["piezas_fuera"]) or "(ninguna)"))
    p.append("")
    for clave, ln, tit in m["hallazgos"]:
        marca = ("**la subcadena de la fila SI lo nombra**"
                 if clave in m["claves_nombradas"] else
                 "la subcadena de la fila NO lo nombra, y aun asi cuenta, porque "
                 "quien decide es el numeral")
        # NO SE TOCA: es una CITA de la linea del acta dentro del texto de la entrada.
        p.append("  - **`%s` (`docs/loop/ACTA_AUDITOR.md:%d`, leida hoy). VIA: %s.** %s."
                 % (clave, ln, VIA.get(clave, "(sin via)"), marca))
        p.append("    Titulo literal del acta: *\"%s\"*" % tit)
        p.append("    **QUE HACE ESTA VUELTA CON EL (glosa del ejecutor, no del acta):** %s"
                 % QUE_HACE_ESTA_VUELTA.get(clave, "(sin glosa)"))
    p.append("")
    p.append("**LAS CAIDAS: %s DEL AUDITOR Y %s DEL EJECUTOR, Y AQUI VA LA TERCERA COSA QUE"
             % (PALABRA_CON_CERO[m["n_aud"]].upper(),
                PALABRA_CON_CERO[m["n_eje"]].upper()))
    p.append("ESTA ACTA ESTRENA: SUS CAIDAS NO SE LLAMAN `C.n`.** Se llaman por la clave del")
    p.append("documento que las declara, y las dos mediciones que lo prueban en vez de")
    p.append("afirmarlo:")
    p.append("")
    p.append("  - **EL PATRON `C.n` EN LINEA (el de la 190) DA %d SOBRE LA SECCION 6.** El"
             % m["n_c_en_linea_s6"])
    p.append("    de cabeza de linea de la 187 da %d y el de la 188 da %d sobre el acta"
             % (m["n_c_crudo"], m["n_c_espacio"]))
    p.append("    entera. **Con cero, `caidas_en_linea()` de la 190 saca (%d, %d, %d) y su"
             % (m["v190_eje"], m["v190_aud"], m["v190_huerf"]))
    p.append("    guarda `if not c_eje` PARA.**")
    p.append("  - **LA MAQUINA DE LA 189 SOBRE LA MISMA SECCION SACA (%d, %d, %d)**, porque"
             % (m["v189_eje"], m["v189_aud"], m["v189_huerf"]))
    p.append("    su patron es de cabeza de linea y aqui no hay ninguna.")
    p.append("")
    p.append("**EL REMEDIO ES CONTAR LA CLAVE `N.M` ENTRECOMILLADA Y DEJAR LA ATRIBUCION")
    p.append("DONDE YA ESTABA: EN LA NEGRITA QUE ABRE EL PARRAFO**, importada de la 190 sin")
    p.append("tocarla. Con eso el reparto sale **ejecutor %d, auditor %d, huerfanas %d**."
             % (m["n_eje"], m["n_aud"], m["n_huerf"]))
    p.append("Las del ejecutor son %s y la del auditor es %s."
             % (", ".join("`%s`" % k for _l, k, _n in m["c_eje"]) or "(ninguna)",
                ", ".join("`%s`" % k for _l, k, _n in m["c_aud"]) or "(ninguna)"))
    p.append("")
    p.append("**Y LAS CLAVES SE DEDUPLICAN POR PARRAFO A PROPOSITO:** el parrafo del")
    p.append("ejecutor nombra `5.2` DOS veces, la tercera vez para decir que la etiqueta")
    p.append("duplicada **no se la cuenta a el**. Contando apariciones en vez de claves")
    p.append("distintas saldrian **%d** donde el acta declara **%d**."
             % (m["n_eje_por_apariciones"], m["n_eje"]))
    p.append("")
    p.append("**LAS DOS ESPECIES DE CERO SIGUEN SEPARADAS, Y SE VUELVE A MEDIR EN VEZ DE")
    p.append("HEREDARSE.** La negrita del ejecutor es `%s`, que es un cero de RACHA:"
             % m["negrita_eje"])
    p.append("declara cero caidas QUE ABRAN RACHA y **en el mismo parrafo declara %d**."
             % m["n_eje"])
    p.append("Tratado como cero de CUENTA, el reparto sale **ejecutor %d**, o sea que"
             % m["cero_confundido_eje"])
    p.append("confundirlas borraria **%d** caida(s) de la cuenta."
             % (m["n_eje"] - m["cero_confundido_eje"]))
    p.append("")
    p.append("**LA CAIDA DEL AUDITOR VA ESCRITA COMO UNA Y NO OMITIDA**, que es lo que el")
    p.append("encargo pide con esas palabras. La negrita que la declara es literal del")
    p.append("acta: `%s`. **La especie de todas ellas se lee del parrafo y no se supone:**"
             % m["negrita_aud"])
    p.append("el literal `%s` aparece en **%d** de los %d parrafos de la seccion 6."
             % (MARCA_ESPECIE_METODO, m["n_parrafos_metodo"], m["n_parrafos6"]))
    p.append("")
    p.append("**LA METRICA DE CREDITO DE LA SECCION %d, PEGADA ENTERA DEL FICHERO Y NO"
             % SECCION_DE_LA_METRICA)
    p.append("RESUMIDA.** Son **%d** filas de datos, contadas y no tecleadas:" % m["n_filas7"])
    p.append("")
    for ln, txt in m["filas7"]:
        # NO SE TOCA: es una CITA de la linea del acta dentro del texto de la entrada.
        p.append("  - `docs/loop/ACTA_AUDITOR.md:%d`: %s" % (ln, txt))
    p.append("")
    p.append("**Y LA FILA DE PUESTOS VA CON SU NOTA, QUE ES LO QUE EL ENCARGO MANDA")
    p.append("REGISTRAR:** los 30 de esta acta son **SOLAPE TOTAL a proposito, o sea control")
    p.append("y NO cobertura nueva**. El literal que el acta escribe de verdad, leido y no")
    p.append("parafraseado, es `%s`; comparado TAL CUAL contra el `%s` del encargo da"
             % (m["nota_literal"], NOTA_DE_PUESTOS))
    p.append("**%s**, y comparado en mayusculas da **%s**. **Las dos cifras se publican**,"
             % ("SI" if m["nota_exacta"] else "NO",
                "SI" if m["nota_de_puestos"] else "NO"))
    p.append("porque son las MISMAS PALABRAS con otra caja: exigir la caja literal habria")
    p.append("hecho PARAR este instrumento por una mayuscula, que es lo contrario de lo que")
    p.append("la guarda existe para cazar. **Si las palabras no estuvieran, este instrumento")
    p.append("haria PARADA**, porque el encargo pide esa nota y una nota que no esta no se")
    p.append("parafrasea.")
    p.append("")
    p.append("**LA DEUDA DE LA SERIE, REMEDIDA AQUI EN VEZ DE HEREDARSE DEL `R.52`:**")
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
    p.append("    el encargo de esta vuelta las deja EXPRESAMENTE fuera, medidas y no")
    p.append("    arregladas.")
    p.append("")
    p.append("**Y ESTA ENTRADA LA ESCRIBE UN REGISTRADOR IDEMPOTENTE, Y LA IDEMPOTENCIA NO")
    p.append("SE RE ESCRIBE: SE IMPORTA DEL DE LA 189, QUE ES DONDE NACIO.** La comprobacion")
    p.append("es **por el acta y no por el numero**, con las marcas literales `%s` y `%s`,"
             % marcas_del_acta(VUELTA_DEL_ACTA))
    p.append("y **en LAS DOS SEDES**. Antes de escribir esta entrada, esas marcas aparecian")
    p.append("en **%d linea(s)**." % m["ya_registrada"])
    p.append("")
    p.append("**LO QUE ESTA ENTRADA NO REGISTRA, DICHO PARA QUE NO SE BUSQUE:** no registra")
    p.append("`acumulan()` leyendo la tabla, ni el cotejo de clon declarado que separa, ni")
    p.append("la excepcion que publica siempre su lista, ni la medicion del censo de arneses")
    p.append("con carril de mutacion sin fichero propio, ni las ocho actas sin entrada")
    p.append("propia rellenadas, ni el exitcode 2 propagado a `--componer`, ni el estado de")
    p.append("`OP-L-02` movido: **el encargo de esta vuelta las nombra una a una como")
    p.append("fuera**. **Y no se poda la nomina de la bateria**, que es la opcion `c` que el")
    p.append("fundador RECHAZO el 5 sep 2026, **ni se corre la bateria**, que cae en la 194.")
    return NL.join(p) + NL


# ---------------------------------------------------------------- LA MUTACION
def _acta_fabricada(n_a_favor, n_en_contra, cabecera_caidas, negrita_eje,
                    negrita_aud, claves_eje, vuelta=None,
                    fila_fuera=None, marca_pregunta=None,
                    nota_puestos=NOTA_DE_PUESTOS):
    """UN ACTA ENTERA FABRICADA, CON LAS CIFRAS QUE SE LE PIDAN. PURA.

    NO SE TOCA EL REPO PARA PROBAR: el arnes corre sobre este texto. La cabecera
    de la seccion de caidas, LAS DOS NEGRITAS, las claves de caida y la marca de
    la pregunta son PARAMETRO, que es lo que permite probar los repartos y los
    vocabularios sin inventar precedencias."""
    v = vuelta if vuelta is not None else VUELTA_DEL_ACTA
    mp = marca_pregunta if marca_pregunta is not None else (
        "ENCARGADA COMO BLOQUEANTE")
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
    L.append("**4.%d `P.1`, una pregunta fabricada. %s.** Prosa de relleno." % (k, mp))
    L.append("")
    L.append("## 5. LO QUE TRAIGO YO")
    L.append("")
    L.append("**5.1 UNA COSA FABRICADA QUE NADIE MARCO.** Prosa de relleno.")
    L.append("")
    L.append("**5.2 OTRA COSA FABRICADA QUE TAMPOCO.** Prosa de relleno.")
    L.append("")
    L.append("**5.3 UNA TERCERA COSA FABRICADA.** Prosa de relleno.")
    L.append("")
    L.append("## %d. %s" % (SECCION_DE_LAS_CAIDAS, cabecera_caidas))
    L.append("")
    cs = "; ".join("`%s`, una cosa" % c for c in claves_eje)
    L.append("**%s** Declara %d (%s), y las tres son DE METODO."
             % (negrita_eje, len(set(claves_eje)), cs))
    L.append("")
    L.append("**%s** Prosa de relleno." % negrita_aud)
    L.append("")
    L.append("## %d. LA METRICA DE CREDITO" % SECCION_DE_LA_METRICA)
    L.append("")
    L.append("| | esta vuelta | acumulado |")
    L.append("|---|---:|---:|")
    L.append("| %s | 30 aislados, **30 de %s a proposito** | **1.006** |"
             % (AGUJA_FILA_PUESTOS, nota_puestos))
    L.append("| %s |" % (fila_fuera or (
        AGUJA_FILA_FUERA
        + " | **3** (una cosa fabricada, otra cosa fabricada, una tercera cosa "
          "fabricada) | **151** |")))
    L.append("| %s | **1**, de metodo | ninguna repetida |" % AGUJA_FILA_CAIDAS_AUDITOR)
    L.append("| %s, registradas y sin racha | **%d** | |"
             % (AGUJA_FILA_CAIDAS_METODO, len(set(claves_eje))))
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
    MUTACION (`EJECUTOR.md` 1): cada caso verde de abajo va seguido de su gemelo
    con el ESPERADO MUTADO, y el arnes exige que el gemelo CAIGA."""
    salida = []
    w = salida.append
    w("=" * 78)
    w("CASO POSITIVO POR MUTACION DEL REGISTRADOR DEL ACTA %d" % VUELTA_DEL_ACTA)
    w("=" * 78)
    w("")
    fallos = 0
    no_cayeron = 0

    CAB = "LAS CAIDAS"
    NEG_EJE = "DEL EJECUTOR: CERO QUE ACUMULEN."
    NEG_AUD = "MIAS: UNA, DE METODO, Y ES LA `5.3`."
    CAB_FAB = "# ACTA DEL AUDITOR, VUELTA %d" % VUELTA_DEL_ACTA

    # ---------------------------------------------------------------- BLOQUE A
    w("A) EL CERO DE `EN CONTRA` NO ROMPE LA MAQUINA, Y ESO SE PRUEBA CON UN ACTA")
    w("   QUE SI LLEVA UNA Y CON OTRA QUE NO")
    txt_sin = _acta_fabricada(6, 0, CAB, NEG_EJE, NEG_AUD, ["5.1", "5.2", "5.3"])
    txt_con = _acta_fabricada(5, 1, CAB, NEG_EJE, NEG_AUD, ["5.1", "5.2", "5.3"])
    for etiqueta, txt, esp_favor, esp_contra in (
            ("acta SIN ninguna EN CONTRA", txt_sin, 6, 0),
            ("acta CON una EN CONTRA", txt_con, 5, 1)):
        lineas, rango, err = cuerpo_del_acta(txt, CAB_FAB)
        fallos += _caso(w, "%s: acotado sin error" % etiqueta, err, None)
        ini, fin = rango
        estados = []
        for clave, _n in claves_de_adjudicacion(lineas, ini, fin, PREFIJO_ADJ):
            pat = re.compile(r"^\s*\*\*%s " % re.escape(clave))
            res, _e = titulo_de_la_negrita(lineas, ini, fin, pat, clave)
            estados.append((clave, familia_de_la_adjudicacion(res[1]),
                            estado_de_la_adjudicacion(res[1])))
        disc = [x for x in estados if x[1] == "DISCUTIBLE"]
        favor = [x for x in disc if x[2] == "A FAVOR"]
        contra = [x for x in disc if x[2] == "EN CONTRA"]
        fallos += _caso(w, "%s: A FAVOR" % etiqueta, len(favor), esp_favor)
        fallos += _caso(w, "%s: EN CONTRA" % etiqueta, len(contra), esp_contra)
        fallos += _caso(w, "%s: SIN DECIR" % etiqueta,
                        len([x for x in estados if x[2] == "SIN DECIR"]), 0)
    w("   LA MUTACION 1: sobre el acta que SI lleva una, se muta el esperado a 0 y")
    w("   tiene que CAER")
    lineas_c, rango_c, _e = cuerpo_del_acta(txt_con, CAB_FAB)
    est_c = []
    for clave, _n in claves_de_adjudicacion(lineas_c, rango_c[0], rango_c[1],
                                            PREFIJO_ADJ):
        pat = re.compile(r"^\s*\*\*%s " % re.escape(clave))
        res, _e2 = titulo_de_la_negrita(lineas_c, rango_c[0], rango_c[1], pat, clave)
        est_c.append(estado_de_la_adjudicacion(res[1]))
    n_contra_fab = len([x for x in est_c if x == "EN CONTRA"])
    if n_contra_fab == 0:
        w("      LA MUTACION NO CAYO: la marca EN CONTRA no se ve ni cuando esta.")
        no_cayeron += 1
    else:
        w("      LA MUTACION CAE: son %d y no 0, o sea que la marca sigue viva."
          % n_contra_fab)
    w("   LA MUTACION 2: la guarda VIEJA de la 190 (`if not en_contra: PARADA`)")
    w("   corrida sobre el acta SIN ninguna, que es la de hoy")
    lineas_s, rango_s, _e = cuerpo_del_acta(txt_sin, CAB_FAB)
    est_s = []
    for clave, _n in claves_de_adjudicacion(lineas_s, rango_s[0], rango_s[1],
                                            PREFIJO_ADJ):
        pat = re.compile(r"^\s*\*\*%s " % re.escape(clave))
        res, _e2 = titulo_de_la_negrita(lineas_s, rango_s[0], rango_s[1], pat, clave)
        est_s.append(estado_de_la_adjudicacion(res[1]))
    pararia = not [x for x in est_s if x == "EN CONTRA"]
    if not pararia:
        w("      LA MUTACION NO CAYO: la guarda vieja no habria parado, o sea que")
        w("      este bloque no prueba nada.")
        no_cayeron += 1
    else:
        w("      LA MUTACION CAE: la guarda vieja PARA sobre un acta legible, y por")
        w("      eso este registrador no la hereda.")
    w("   LA MUTACION 3: el orden importa. Un titulo con LAS DOS marcas tiene que")
    w("   salir EN CONTRA")
    doble = estado_de_la_adjudicacion("`D.9`, algo. A FAVOR DE UNA COSA Y EN CONTRA DE OTRA.")
    if doble != "EN CONTRA":
        w("      LA MUTACION NO CAYO: sale %r y no EN CONTRA." % doble)
        no_cayeron += 1
    else:
        w("      LA MUTACION CAE: con las dos marcas sale EN CONTRA, no A FAVOR.")
    w("")

    # ---------------------------------------------------------------- BLOQUE B
    w("B) LAS TRES MARCAS NUEVAS DE PREGUNTA CONTESTADA, Y EL VOCABULARIO VIEJO")
    for marca, esperado in ((MARCA_MITAD_BARATA,
                             "CONTESTADA A MEDIAS, LA MITAD BARATA ADJUDICADA"),
                            (MARCA_ENCARGADA_BLOQUEANTE,
                             "CONTESTADA Y ENCARGADA COMO BLOQUEANTE"),
                            ("SI, POR EXTENSION CITABLE Y SIN DOCTRINA NUEVA",
                             "CONTESTADA A FAVOR POR EXTENSION CITABLE")):
        fallos += _caso(w, "marca %r" % marca[:34],
                        estado_de_la_adjudicacion("`P.1`, algo. %s." % marca),
                        esperado)
    w("   LA MUTACION: con el vocabulario de la 190 y nada mas, las tres tienen que")
    w("   salir SIN DECIR")
    viejas = (MARCA_EN_CONTRA, MARCA_A_FAVOR, MARCA_CUENTA_COMO_CORRIDO,
              MARCA_PRIMERO_SE_MIDE, MARCA_SE_RESTAURA, MARCA_CADUCA)
    n_ciegas = 0
    for marca in (MARCA_MITAD_BARATA, MARCA_ENCARGADA_BLOQUEANTE,
                  "SI, POR EXTENSION CITABLE Y SIN DOCTRINA NUEVA"):
        t = ("`P.1`, algo. %s." % marca).upper()
        if not any(v in t for v in viejas):
            n_ciegas += 1
    if n_ciegas != 3:
        w("      LA MUTACION NO CAYO: el vocabulario viejo ve %d de 3." % (3 - n_ciegas))
        no_cayeron += 1
    else:
        w("      LA MUTACION CAE: las 3 salen SIN DECIR con el vocabulario viejo, o")
        w("      sea que heredarlo habria hecho PARAR este instrumento.")
    w("")

    # ---------------------------------------------------------------- BLOQUE C
    w("C) LAS CAIDAS POR CLAVE `N.M`, CON LA ATRIBUCION POR LA NEGRITA DEL PARRAFO")
    r6 = rango_de_seccion(lineas_s, rango_s[0], rango_s[1], SECCION_DE_LAS_CAIDAS)
    fallos += _caso(w, "la seccion 6 se localiza", r6 is not None, True)
    eje, aud, hue = caidas_por_numeral(lineas_s, r6[0], r6[1])
    fallos += _caso(w, "reparto (ejecutor, auditor, huerfanas)",
                    (len(eje), len(aud), len(hue)), (3, 1, 0))
    w("   Y LAS DOS MAQUINAS VIEJAS SOBRE LA MISMA SECCION, QUE NO VEN NADA:")
    v190 = caidas_en_linea(lineas_s, r6[0], r6[1])
    fallos += _caso(w, "caidas_en_linea() de la 190 (patron `C.n`)",
                    (len(v190[0]), len(v190[1]), len(v190[2])), (0, 0, 0))
    v189 = caidas_por_seccion(lineas_s, r6[0], r6[1])
    fallos += _caso(w, "caidas_por_seccion() de la 189",
                    (len(v189[0]), len(v189[1]), len(v189[2])), (0, 0, 0))
    w("      (las dos dan cero porque buscan `C.n`, y esta acta no escribe ninguna:")
    w("       por eso hace falta contar la clave `N.M`)")
    w("   LA NEGRITA MUDA: un parrafo cuya negrita no diga de quien son")
    txt_mudo = _acta_fabricada(6, 0, CAB, "PASARON COSAS.", NEG_AUD,
                               ["5.1", "5.2", "5.3"])
    lm, rm, _e = cuerpo_del_acta(txt_mudo, CAB_FAB)
    r6m = rango_de_seccion(lm, rm[0], rm[1], SECCION_DE_LAS_CAIDAS)
    e2, a2, h2 = caidas_por_numeral(lm, r6m[0], r6m[1])
    fallos += _caso(w, "negrita muda -> huerfanas", (len(e2), len(a2), len(h2)),
                    (0, 1, 3))
    w("      LA PARADA SE CONSERVA ENTERA: %d huerfana(s), y una caida sin dueno no"
      % len(h2))
    w("      se reparte a ojo.")
    w("   LA DEDUPLICACION POR PARRAFO: una clave repetida no cuenta dos veces")
    txt_rep = _acta_fabricada(6, 0, CAB, NEG_EJE, NEG_AUD,
                              ["5.1", "5.2", "5.3", "5.2"])
    lr, rr, _e = cuerpo_del_acta(txt_rep, CAB_FAB)
    r6r = rango_de_seccion(lr, rr[0], rr[1], SECCION_DE_LAS_CAIDAS)
    er, ar, hr = caidas_por_numeral(lr, r6r[0], r6r[1])
    fallos += _caso(w, "con `5.2` escrita dos veces: ejecutor", len(er), 3)
    n_apar = len(PAT_CLAVE_NUMERAL.findall(
        " ".join(lr[r6r[0] - 1:r6r[1]])))
    if n_apar <= 3:
        w("      LA MUTACION NO CAYO: el texto no tiene claves repetidas, asi que")
        w("      este caso no prueba la deduplicacion.")
        no_cayeron += 1
    else:
        w("      LA MUTACION CAE: hay %d apariciones y %d claves distintas del"
          % (n_apar, len(er) + len(ar)))
        w("      ejecutor mas el auditor, o sea que contar apariciones daria de mas.")
    w("   EL CERO DE RACHA NO NEUTRALIZA, EL DE CUENTA SI")
    conf = caidas_por_numeral(lineas_s, r6[0], r6[1],
                              marcas_cero_cuenta=(MARCAS_CERO_DE_CUENTA
                                                  + MARCAS_CERO_DE_RACHA))
    fallos += _caso(w, "tratando el cero de RACHA como de CUENTA: ejecutor",
                    len(conf[0]), 0)
    if len(conf[0]) == len(eje):
        w("      LA MUTACION NO CAYO: la distincion no cambia nada.")
        no_cayeron += 1
    else:
        w("      LA MUTACION CAE: %d con la separacion y %d sin ella."
          % (len(eje), len(conf[0])))
    w("")

    # ---------------------------------------------------------------- BLOQUE D
    w("D) LA FILA QUE DICE CUALES HALLAZGOS CUENTAN FUERA, Y LOS DOS SEPARADORES")
    ini_s, fin_s = rango_s
    hall = []
    for clave, _n in claves_de_adjudicacion(lineas_s, ini_s, fin_s, PREFIJO_HALLAZGO):
        pat = re.compile(r"^\s*\*\*%s " % re.escape(clave))
        res, _e = titulo_de_la_negrita(lineas_s, ini_s, fin_s, pat, clave)
        hall.append((clave, res[0], res[1]))
    fallos += _caso(w, "hallazgos `5.n` sobre el fabricado", len(hall), 3)
    fila = fila_de_la_metrica(lineas_s, ini_s, fin_s, AGUJA_FILA_FUERA)
    fallos += _caso(w, "la fila de la tabla se localiza", len(fila), 1)
    fallos += _caso(w, "el numeral de la fila, leido y no tecleado",
                    numeral_de_la_fila(fila[0][1]), 3)
    n1, s1, p1 = hallazgos_que_la_tabla_nombra(hall, fila[0][1], separadores=(";",))
    n2, s2, p2 = hallazgos_que_la_tabla_nombra(hall, fila[0][1])
    w("   piezas partiendo solo por `;`: %d -> casan %d" % (len(p1), len(n1)))
    w("   piezas partiendo por `;` y por `,`: %d -> casan %d" % (len(p2), len(n2)))
    if len(p2) <= len(p1):
        w("      LA MUTACION NO CAYO: la coma no parte nada, o sea que el cambio de")
        w("      separadores no hace falta.")
        no_cayeron += 1
    else:
        w("      LA MUTACION CAE: %d piezas contra %d, o sea que partir solo por `;`"
          % (len(p2), len(p1)))
        w("      dejaba la fila sin trocear.")
    w("   LA MUTACION: una fila SIN cifra en su celda tiene que dar None y no un")
    w("   numero inventado")
    sin_cifra = numeral_de_la_fila("| %s | muchas | **151** |" % AGUJA_FILA_FUERA)
    if sin_cifra is not None:
        w("      LA MUTACION NO CAYO: sale %r de una celda sin cifra." % sin_cifra)
        no_cayeron += 1
    else:
        w("      LA MUTACION CAE: sale None y ninguna cifra se inventa.")
    w("")

    # ---------------------------------------------------------------- BLOQUE E
    w("E) LA NOTA DE LA FILA DE PUESTOS, EXIGIDA LITERAL")
    fila_p = fila_de_la_metrica(lineas_s, ini_s, fin_s, AGUJA_FILA_PUESTOS)
    fallos += _caso(w, "la fila de puestos se localiza", len(fila_p), 1)
    fallos += _caso(w, "lleva el literal %r" % NOTA_DE_PUESTOS,
                    NOTA_DE_PUESTOS in fila_p[0][1].upper(), True)
    w("   LA CAJA: la misma nota con la caja del acta real (`solape TOTAL`) tiene")
    w("   que seguir contando, porque son las mismas palabras")
    txt_caja = _acta_fabricada(6, 0, CAB, NEG_EJE, NEG_AUD, ["5.1", "5.2", "5.3"],
                               nota_puestos="solape TOTAL")
    lc, rc, _e = cuerpo_del_acta(txt_caja, CAB_FAB)
    fpc = fila_de_la_metrica(lc, rc[0], rc[1], AGUJA_FILA_PUESTOS)
    fallos += _caso(w, "con la caja del acta real, comparado en mayusculas",
                    NOTA_DE_PUESTOS in fpc[0][1].upper(), True)
    if NOTA_DE_PUESTOS in fpc[0][1]:
        w("      LA MUTACION NO CAYO: la comparacion literal la ve igual, o sea que")
        w("      la caja no cambia nada y este caso no prueba nada.")
        no_cayeron += 1
    else:
        w("      LA MUTACION CAE: comparada TAL CUAL la nota real NO se ve, o sea")
        w("      que exigir la caja habria parado el instrumento por una mayuscula.")
    w("   LA MUTACION: un acta cuya fila de puestos NO traiga la nota tiene que")
    w("   salir en falso, y quien llama para")
    txt_sn = _acta_fabricada(6, 0, CAB, NEG_EJE, NEG_AUD, ["5.1", "5.2", "5.3"],
                             nota_puestos="cobertura nueva")
    lsn, rsn, _e = cuerpo_del_acta(txt_sn, CAB_FAB)
    fp2 = fila_de_la_metrica(lsn, rsn[0], rsn[1], AGUJA_FILA_PUESTOS)
    if fp2 and NOTA_DE_PUESTOS in fp2[0][1].upper():
        w("      LA MUTACION NO CAYO: la nota sale hasta cuando no esta.")
        no_cayeron += 1
    else:
        w("      LA MUTACION CAE: sin la nota, la comprobacion da falso.")
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
    if len(halladas) == 0:
        w("      LA MUTACION NO CAYO: dejaria escribir una entrada duplicada.")
        no_cayeron += 1
    else:
        w("      LA MUTACION CAE: la segunda escritura queda prohibida, con %d"
          % len(halladas))
        w("      linea(s) de prueba.")
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

    lineas, rango, err = cuerpo_del_acta(None, CABECERA_ACTA)
    if err:
        w(err)
        print(NL.join(salida))
        return 1
    inicio, fin = rango
    w("A) EL CUERPO DEL ACTA, ACOTADO ANTES DE CONTAR NADA")
    # NO SE TOCA: se publica el tramo leido; el acta no se escribe.
    w("   acta %d: docs/loop/ACTA_AUDITOR.md, lineas %d a %d"
      % (VUELTA_DEL_ACTA, inicio, fin))
    w("   LAS DOS CONVENCIONES DE `lineas` SOBRE EL TRAMO, QUE ES LA TAREA 3 DE")
    w("   ESTA MISMA VUELTA: por `fin - inicio + 1` da %d" % (fin - inicio + 1))
    # EL SUJETO DE ESTE INSTRUMENTO ESTA VIVO A PROPOSITO Y AQUI SE DICE POR QUE
    # (vuelta 192, TAREA 3.b). Un registrador TIENE que leer el acta de hoy:
    # congelarlo lo romperia. Lo que si se puede, y es lo que se hace desde esta
    # linea, es PUBLICAR EL `sha256` DE LO QUE ACABA DE LEER, para que una corrida
    # que lea otra acta se pueda detectar. NO SE TOCA el acta: se abre en lectura.
    _datos_acta = io.open(ACTA, "rb").read()
    _lf_acta = _datos_acta.replace(b"\r\n", b"\n")
    w("   docs/loop/ACTA_AUDITOR.md -> disco %d bytes | LF %d bytes"
      % (len(_datos_acta), len(_lf_acta)))
    w("   sha256 LF del acta leida: %s" % hashlib.sha256(_lf_acta).hexdigest())
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
        w("   PARADA: ningun patron encuentra adjudicaciones y el acta 191 declara")
        w("   nueve. No se escribe una entrada con cero.")
        print(NL.join(salida))
        return 1
    w("")

    w("D) EL TITULO LITERAL DE CADA ADJUDICACION, SU FAMILIA Y SU ESTADO")
    w("   (EL VOCABULARIO LLEVA LAS TRES MARCAS NUEVAS DEL ACTA 191 Y CONSERVA LAS")
    w("    SEIS DE LA 190. `EN CONTRA` sigue buscandose PRIMERO aunque hoy no")
    w("    muerda)")
    adjudicaciones = []
    n_sin_decir_vieja = 0
    VIEJAS = (MARCA_EN_CONTRA, MARCA_A_FAVOR, MARCA_CUENTA_COMO_CORRIDO,
              MARCA_PRIMERO_SE_MIDE, MARCA_SE_RESTAURA, MARCA_CADUCA)
    for clave, _n in claves:
        pat = re.compile(r"^\s*\*\*%s " % re.escape(clave))
        res, err2 = titulo_de_la_negrita(lineas, inicio, fin, pat, clave)
        if err2:
            w("   %s -> %s" % (clave, err2))
            print(NL.join(salida))
            return 1
        ln, tit = res
        if not any(v in tit.upper() for v in VIEJAS):
            n_sin_decir_vieja += 1
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
    w("   CON EL VOCABULARIO DE LA 190 Y NADA MAS, saldrian SIN DECIR: %d"
      % n_sin_decir_vieja)
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
    sin_sentido = [a for a in discutibles if a[2] not in ("A FAVOR", "EN CONTRA")]
    if sin_sentido:
        w("   PARADA: hay %d discutible(s) cuyo estado no es ni A FAVOR ni EN CONTRA:"
          % len(sin_sentido))
        for a in sin_sentido:
            w("      %s -> %s" % (a[0], a[4][:120]))
        print(NL.join(salida))
        return 1
    w("   EL CERO DE `EN CONTRA` ES UN RESULTADO Y NO UNA PARADA. La guarda VIEJA")
    w("   de la 190 (`if not en_contra: PARADA`) corrida sobre esta acta: %s"
      % ("PARARIA" if not en_contra else "no pararia"))
    if not preguntas:
        w("   PARADA: ninguna adjudicacion nombra un `P.n` y el acta 191 declara TRES")
        w("   preguntas contestadas. No se escribe una lista vacia.")
        print(NL.join(salida))
        return 1
    w("")

    w("E) LOS HALLAZGOS DE LA SECCION %d, Y CUANTOS CUENTAN FUERA DEL MARCADO"
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
    n1, s1, piezas_pyc = hallazgos_que_la_tabla_nombra(hallazgos, fila_fuera[0][1],
                                                       separadores=(";",))
    nombrados, sueltos, piezas = hallazgos_que_la_tabla_nombra(hallazgos,
                                                               fila_fuera[0][1])
    w("   PARTIENDO SOLO POR `;` (la maquina de la 190): %d pieza(s), casan %d"
      % (len(piezas_pyc), len(n1)))
    w("      %s" % ", ".join(repr(x) for x in piezas_pyc))
    w("   PARTIENDO POR `;` Y POR `,`: %d pieza(s), casan %d"
      % (len(piezas), len(nombrados)))
    w("      %s" % ", ".join(repr(x) for x in piezas))
    for clave, ln, tit, casan in nombrados:
        w("      %s (linea %d) casa por %s" % (clave, ln, ", ".join(repr(x) for x in casan)))
    w("   LOS QUE LA SUBCADENA NO NOMBRA: %d (%s)"
      % (len(sueltos), ", ".join(c for c, _l, _t in sueltos) or "ninguno"))
    numeral = numeral_de_la_fila(fila_fuera[0][1])
    w("   EL NUMERAL DE LA PROPIA FILA, LEIDO Y NO TECLEADO: %s" % numeral)
    if numeral is None:
        w("   PARADA: la fila no trae cifra en su celda. Una cifra que no se puede")
        w("   leer no se inventa.")
        print(NL.join(salida))
        return 1
    if numeral == len(hallazgos):
        n_fuera = len(hallazgos)
        w("   EL NUMERAL CALZA CON LAS CLAVES `5.n` DE LA SECCION (%d = %d), asi que"
          % (numeral, len(hallazgos)))
        w("   los %d cuentan fuera del marcado. El cotejo por subcadena queda al lado"
          % n_fuera)
        w("   como lo que es: una medicion mas debil, que solo resuelve %d de %d"
          % (len(nombrados), len(hallazgos)))
        w("   porque la fila PARAFRASEA en vez de citar.")
    elif numeral == len(nombrados):
        n_fuera = len(nombrados)
        w("   EL NUMERAL CALZA CON LOS QUE LA SUBCADENA NOMBRA (%d), y son esos."
          % numeral)
    else:
        w("   PARADA: el numeral dice %d, las claves `5.n` son %d y la subcadena"
          % (numeral, len(hallazgos)))
        w("   nombra %d. Ninguna de las dos vias resuelve, y no se elige a ojo."
          % len(nombrados))
        print(NL.join(salida))
        return 1
    w("")

    w("F) LAS CAIDAS, CONTADAS POR LA CLAVE `N.M` Y ATRIBUIDAS POR LA NEGRITA")
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
    texto6 = " ".join(lineas[ini6 - 1:fin6])
    n_c_en_linea_s6 = len(set(PAT_C_EN_LINEA.findall(texto6)))
    w("   patron `C.n` EN LINEA (el de la 190) sobre la seccion 6: %d"
      % n_c_en_linea_s6)
    w("   patron `C.n` de cabeza de linea de la 187 sobre el acta: %d" % len(n_c_crudo))
    w("   patron `C.n` de cabeza de linea de la 188 sobre el acta: %d" % len(n_c_espacio))
    w("   patron `A.n` de cabecera de tercer nivel (acta 185): %d" % len(l_aud_a))
    w("   patron `R.n` de caida de reporte: %d" % len(l_rep))
    w("   patron `E.n` de las actas 182 y 184: %d" % len(l_eje_v))
    v190 = caidas_en_linea(lineas, ini6, fin6)
    v189 = caidas_por_seccion(lineas, ini6, fin6)
    w("   LAS DOS MAQUINAS VIEJAS SOBRE ESTA SECCION, QUE ES DONDE SE ROMPEN:")
    w("      caidas_en_linea() de la 190: ejecutor %d | auditor %d | huerfanas %d"
      % (len(v190[0]), len(v190[1]), len(v190[2])))
    w("      caidas_por_seccion() de la 189: ejecutor %d | auditor %d | huerfanas %d"
      % (len(v189[0]), len(v189[1]), len(v189[2])))
    c_eje, c_aud, huerfanas = caidas_por_numeral(lineas, ini6, fin6)
    w("   CON LA MAQUINA DE ESTA VUELTA (clave `N.M` + negrita del parrafo):")
    w("      DEL EJECUTOR: %d" % len(c_eje))
    for ln, k, neg in c_eje:
        w("         %s en el parrafo de la linea %d, bajo la negrita %r"
          % (k, ln, neg[:70]))
    w("      DEL AUDITOR: %d" % len(c_aud))
    for ln, k, neg in c_aud:
        w("         %s en el parrafo de la linea %d, bajo la negrita %r"
          % (k, ln, neg[:70]))
    w("      HUERFANAS: %d" % len(huerfanas))
    for ln, k, neg in huerfanas:
        w("         %s en el parrafo de la linea %d, bajo la negrita %r"
          % (k, ln, neg[:70]))
    if huerfanas:
        w("   PARADA: hay %d caida(s) en un parrafo cuya negrita no dice de quien"
          % len(huerfanas))
        w("   son. Una caida sin dueno no se reparte a ojo.")
        print(NL.join(salida))
        return 1
    if not c_eje:
        w("   PARADA: no se encuentra ninguna caida del ejecutor y el acta 191")
        w("   declara TRES en su seccion 6.")
        print(NL.join(salida))
        return 1
    if not c_aud:
        w("   PARADA: no se encuentra ninguna caida propia del auditor y el acta 191")
        w("   declara UNA, escrita como una y no omitida.")
        print(NL.join(salida))
        return 1
    parrafos6 = parrafos_con_negrita(lineas, ini6, fin6)
    negrita_eje = c_eje[0][2]
    negrita_aud = c_aud[0][2]
    apar_eje = 0
    for _a, _b, neg, txt in parrafos6:
        if any(x in neg.upper() for x in MARCAS_LEAD_EJECUTOR):
            apar_eje = len(PAT_CLAVE_NUMERAL.findall(txt))
    w("   CLAVES DEL EJECUTOR contadas por APARICIONES en vez de por claves")
    w("   distintas: %d (por eso se deduplica por parrafo)" % apar_eje)
    confundido = caidas_por_numeral(lineas, ini6, fin6,
                                    marcas_cero_cuenta=(MARCAS_CERO_DE_CUENTA
                                                        + MARCAS_CERO_DE_RACHA))
    w("   TRATANDO EL CERO DE RACHA COMO CERO DE CUENTA: ejecutor %d | auditor %d"
      % (len(confundido[0]), len(confundido[1])))
    w("   O SEA QUE CONFUNDIRLAS BORRARIA %d CAIDA(S) DE LA CUENTA."
      % (len(c_eje) - len(confundido[0])))
    n_metodo = len([1 for _a, _b, _n, t in parrafos6
                    if MARCA_ESPECIE_METODO in t.upper()])
    w("   la marca de especie %r aparece en %d de los %d parrafos de la seccion"
      % (MARCA_ESPECIE_METODO, n_metodo, len(parrafos6)))
    if not n_metodo:
        w("   PARADA: ningun parrafo declara la especie de las caidas.")
        print(NL.join(salida))
        return 1
    w("")

    w("G) LA METRICA DE CREDITO DE LA SECCION %d, ENTERA" % SECCION_DE_LA_METRICA)
    r7 = rango_de_seccion(lineas, inicio, fin, SECCION_DE_LA_METRICA)
    if r7 is None:
        w("   PARADA: el acta no tiene seccion %d." % SECCION_DE_LA_METRICA)
        print(NL.join(salida))
        return 1
    filas7 = filas_de_la_metrica(lineas, r7[0], r7[1])
    w("   la seccion %d va de la linea %d a la %d"
      % (SECCION_DE_LA_METRICA, r7[0], r7[1]))
    w("   CIFRA filas de datos: %d" % len(filas7))
    for ln, txt in filas7:
        w("      LINEA %-6d %s" % (ln, txt))
    if not filas7:
        w("   PARADA: la tabla de credito no trae ninguna fila de datos.")
        print(NL.join(salida))
        return 1
    fila_p = fila_de_la_metrica(lineas, inicio, fin, AGUJA_FILA_PUESTOS)
    w("   LA FILA DE PUESTOS, QUE EL ENCARGO MANDA REGISTRAR CON SU NOTA: %d"
      % len(fila_p))
    for ln, txt in fila_p:
        w("      LINEA %-6d %s" % (ln, txt))
    nota_exacta = bool(fila_p) and NOTA_DE_PUESTOS in fila_p[0][1]
    nota = bool(fila_p) and NOTA_DE_PUESTOS in fila_p[0][1].upper()
    literal = ""
    if fila_p:
        mm = re.search(r"(?i)(solape\s+total)", fila_p[0][1])
        literal = mm.group(1) if mm else ""
    w("   el literal %r aparece TAL CUAL en la fila de puestos: %s"
      % (NOTA_DE_PUESTOS, "SI" if nota_exacta else "NO"))
    w("   comparado en mayusculas: %s" % ("SI" if nota else "NO"))
    w("   LO QUE EL ACTA ESCRIBE DE VERDAD, LEIDO Y NO PARAFRASEADO: %r" % literal)
    w("   (las dos cifras se publican: exigir la caja literal habria hecho PARAR")
    w("    este instrumento por una mayuscula)")
    if not nota:
        w("   PARADA: el encargo pide registrar la fila de puestos CON SU NOTA de")
        w("   solape total, y la fila no la trae. Una nota que no esta no se")
        w("   parafrasea.")
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

    w("H) EL NUMERO DE LA ENTRADA, QUE NO SE TECLEA")
    halladas = SERIE.entradas()
    numero = SERIE.siguiente_libre(halladas)
    w("   serie recomputada de sus dos sedes: %d entradas" % len(halladas))
    w("   CIFRA colisiones: %d | CIFRA huecos: %d"
      % (len(SERIE.colisiones(halladas)), len(SERIE.huecos(halladas))))
    w("   SIGUIENTE LIBRE: R.%d" % numero)
    w("")

    w("I) LA DEUDA DE LA SERIE, REMEDIDA AQUI Y NO HEREDADA")
    salto = actas_sin_entrada(halladas, 173, VUELTA_DEL_ACTA - 1)
    faltan, bajo, alto = salto
    w("   tramo mirado: actas 173 a %d" % (VUELTA_DEL_ACTA - 1))
    w("   CIFRA actas SIN entrada propia en la serie: %d" % len(faltan))
    w("   LAS QUE FALTAN: %s" % (", ".join(str(x) for x in faltan) or "(ninguna)"))
    w("   EXTREMO BAJO: %s"
      % ("R.%d cubre el acta %d" % bajo if bajo else "(ninguno)"))
    w("   EXTREMO ALTO: %s"
      % ("R.%d cubre el acta %d" % alto if alto else "(ninguno)"))
    w("   el encargo dice OCHO (173 a 180) -> %s"
      % ("CALZA" if len(faltan) == 8 else "NO CALZA, y la discrepancia se declara"))
    w("")

    medido = {
        "inicio": inicio, "fin": fin, "secciones": secciones,
        "n_adj": len(claves), "n_entrecomillado": len(entrecomilladas),
        "adjudicaciones": adjudicaciones,
        "n_discutibles": len(discutibles), "n_preg": len(preguntas),
        "n_otras": len(otras), "n_a_favor_discutibles": len(a_favor),
        "n_en_contra_discutibles": len(en_contra),
        "n_discutibles_sin_sentido": len(sin_sentido),
        "vieja_pararia": not en_contra,
        "n_sin_decir_vieja": n_sin_decir_vieja,
        "preguntas": [(c, PAT_P_DEL_TITULO.search(t).group(0).strip("`"))
                      for c, _f, _e, _l, t in preguntas],
        "hallazgos": hallazgos, "n_hall": len(hallazgos),
        "hall_nombrados": nombrados,
        "claves_nombradas": set(c for c, _l, _t, _k in nombrados),
        "piezas_fuera": piezas, "fila_fuera": fila_fuera,
        "n_piezas": len(piezas), "n_piezas_pyc": len(piezas_pyc),
        "n_casan_pyc": len(n1), "numeral_fila": numeral, "n_fuera": n_fuera,
        "cabecera_seccion6": cabecera6,
        "c_eje": c_eje, "c_aud": c_aud,
        "n_eje": len(c_eje), "n_aud": len(c_aud), "n_huerf": len(huerfanas),
        "n_eje_por_apariciones": apar_eje,
        "negrita_eje": negrita_eje, "negrita_aud": negrita_aud,
        "v190_eje": len(v190[0]), "v190_aud": len(v190[1]),
        "v190_huerf": len(v190[2]),
        "v189_eje": len(v189[0]), "v189_aud": len(v189[1]),
        "v189_huerf": len(v189[2]),
        "cero_confundido_eje": len(confundido[0]),
        "cero_confundido_aud": len(confundido[1]),
        "n_parrafos_metodo": n_metodo, "n_parrafos6": len(parrafos6),
        "n_c_crudo": len(n_c_crudo), "n_c_espacio": len(n_c_espacio),
        "n_c_en_linea_s6": n_c_en_linea_s6,
        "n_a": len(l_aud_a), "n_rep": len(l_rep), "n_eje_viejo": len(l_eje_v),
        "filas7": filas7, "n_filas7": len(filas7),
        "fila_puestos": fila_p, "nota_de_puestos": nota,
        "nota_exacta": nota_exacta, "nota_literal": literal,
        "fila_aud": fila_aud, "fila_metodo": fila_metodo,
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

    w("J) EL TITULO, CON SUS CINCO NUMERALES COMPUTADOS")
    titulo = titulo_de_la_entrada(m["n_adj"], m["n_hall"], m["n_preg"],
                                  m["n_aud"], m["n_eje"])
    w("   %s" % titulo)
    w("")

    numero = m["numero"]
    entrada = armar_entrada(numero, titulo, m)
    w("K) LA ENTRADA ARMADA")
    w("   %d bytes | %d lineas por count(NL) | %d por len(split(NL))"
      % (len(entrada.encode("utf-8")), entrada.count(NL), len(entrada.split(NL))))
    w("   guiones largos o medios en la entrada: %d"
      % (entrada.count(chr(8212)) + entrada.count(chr(8211))))
    w("")

    texto_sede = io.open(SEDE, encoding="utf-8").read().replace(chr(13) + NL, NL)
    if a.simular:
        w("L) MODO --simular: NO SE ESCRIBE NADA EN LA SEDE.")
        w("")
        w("LA ENTRADA, ENTERA:")
        for l in entrada.split(NL):
            w("   | " + l)
    elif m["ya_registrada"]:
        w("L) NO SE ESCRIBE NADA, Y ESTA ES LA IDEMPOTENCIA HACIENDO SU TRABAJO.")
        w("   el acta %d YA TIENE ENTRADA en la serie: %d linea(s) la nombran."
          % (VUELTA_DEL_ACTA, m["ya_registrada"]))
        w("   NO se escribe una entrada nueva y NO se consume el numero R.%d." % numero)
        w("   docs/PENDIENTES.md sigue en %d bytes." % os.path.getsize(SEDE))
    else:
        nuevo = texto_sede.rstrip(NL) + NL + NL + entrada
        io.open(SEDE, "w", encoding="utf-8", newline=NL).write(nuevo)
        w("L) ESCRITA EN docs/PENDIENTES.md")
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
