# -*- coding: utf-8 -*-
r"""vuelta189_tarea1a_registrar_acta189.py . EL ACTA 189 ENTERA, REGISTRADA EN LA
SERIE `R.N` EN LA FORMA DE LA CASA, Y ESTE REGISTRADOR NACE IDEMPOTENTE.

LA MAQUINA NO SE CLONA, SE IMPORTA, y eso lo adjudico la `6.6` del acta 172 como
correcto y obligatorio. De la cadena de registradores se importan
`titulo_de_la_negrita`, `claves_de_adjudicacion`, `claves_entrecomilladas`,
`cuenta_por_patron`, `actas_sin_entrada`, `PALABRA_CON_CERO`,
`cabecera_de_la_seccion`, `lineas_que_declaran_cero_caidas`, `parrafo_de`,
`seccion_que_contiene`, `bloque_de_la_caida`, `acumulan`, `caidas_c_por_seccion`
y los patrones de caida. **Lo propio de este fichero son LAS CINCO COSAS QUE EL
ACTA 189 ESTRENA.**

POR QUE HACE FALTA CODIGO PROPIO, MEDIDO Y NO SUPUESTO. Son CINCO, y las cinco
salen de correr la maquinaria heredada sobre el acta 189:

  1) LA SECCION DE LAS ADJUDICACIONES CAMBIA DE NUMERO Y DE FORMA. En el acta 188
     eran la seccion 5 y se escribian ``**`5.1` ...`` (numeral ENTRE COMILLAS
     INVERSAS). En el acta 189 son la seccion **4** y se escriben ``**4.1 ...``
     (numeral SIN comillas). Corrido sobre esta acta, el patron entrecomillado da
     **0** y el suelto da **10**. **Las dos cifras se publican**; ninguno de los
     dos patrones se ensancha.

  2) LA ATRIBUCION DE LAS CAIDAS SE INVIERTE, Y EL VOCABULARIO HEREDADO SE
     EQUIVOCA. La cabecera de la seccion 6 del acta 189 dice
     `## 6. LAS CAIDAS. DOS SON MIAS Y CERO SON DEL EJECUTOR`. **Contiene la
     palabra `EJECUTOR`**, asi que el vocabulario de la 188
     (`MARCAS_DUENO_EJECUTOR = ("EJECUTOR", "LAS SUYAS")`, con precedencia del
     ejecutor) le atribuye **las dos caidas al ejecutor**, que es **falso**: el
     acta dice `MIA` en las dos y `DEL EJECUTOR: CERO` en su prosa. **La cifra
     vieja se publica al lado**, porque un vocabulario que se equivoca callado es
     peor que uno que no muerde.

     **EL REMEDIO NO ES ENSANCHAR NI QUITAR NADA:** se anade la marca de auditor
     `SON MIAS`, literal de la cabecera, y se anade una marca de **CERO
     DECLARADO**, `CERO SON DEL EJECUTOR`, tambien literal. Una cabecera que
     declara **cero** caidas del ejecutor **no le esta atribuyendo ninguna**: la
     mencion de la palabra es una declaracion de cero, no una atribucion. Es la
     unica lectura que no obliga a inventar precedencias. **La PARADA se conserva
     entera:** una `C.n` bajo una cabecera que no diga ni una cosa ni la otra
     sigue saliendo huerfana y sigue parando.

  3) EL CERO DEL EJECUTOR SE REGISTRA COMO CERO Y NO SE OMITE, Y NO SE PUBLICA
     DESNUDO. Un cero que sale de un patron que no muerde no es evidencia de
     nada, asi que va con la declaracion literal del acta al lado
     (`DEL EJECUTOR: CERO`), contada en su linea. **Si el patron diera cero y el
     acta no lo declarara por ninguna frase, esto hace PARADA.**

  4) LAS PREGUNTAS NO TIENEN SECCION PROPIA: viven DENTRO de las adjudicaciones.
     El acta 188 las traia en su seccion 7; el acta 189 contesta `P.1`, `P.2` y
     `P.3` en las adjudicaciones `4.7`, `4.8` y `4.9`. **Cual adjudicacion es una
     pregunta NO SE TECLEA:** sale de que su titulo literal nombre un `P.n`, del
     mismo modo que las de discutible nombran un `D.n`. Y la seccion 5 trae UNA
     adjudicacion mas, la de la bateria, localizada por su negrita `ADJUDICO:`.

  5) LA IDEMPOTENCIA, QUE ES LO QUE SALE DE LA `C.2` DEL ACTA 189 Y ES DEL PROPIO
     REGISTRADOR. Hoy `scripts/loop/vuelta188_tarea1a_registrar_acta188.py`, RE
     CORRIDO, **no detecta que el acta ya esta registrada y escribe una entrada
     nueva duplicada con el numero siguiente**. La causa esta en su linea 1348 y
     se puede leer: `ya = ("## R.%d. %s" % (numero, titulo)) in texto_sede`, donde
     `numero` es **el siguiente libre**, o sea un numero que por construccion NO
     puede estar todavia en la sede. **Comprobar la idempotencia por el numero que
     se va a escribir es no comprobarla.** El auditor lo cazo re corriendolo y
     tuvo que revertir a mano una `R.51` fantasma de 196 lineas.

     **AQUI LA COMPROBACION ES POR EL ACTA Y NO POR EL NUMERO**, y mira **LAS DOS
     SEDES** de la serie, no una: si alguna entrada ya registra el acta 189, este
     instrumento **sale sin escribir y lo dice con su cifra**. Su caso positivo
     por mutacion escribe dos veces sobre una sede fabricada y **la segunda CAE**.

LA PARADA SE CONSERVA ENTERA: un estado, una atribucion o una cuenta que este
registrador no sepa leer sigue siendo PARADA, y no se resuelve a ojo.

LO QUE ESTE FICHERO NO HACE: no toca el acta, no toca el reporte, no toca
`docs/plan/` salvo para LEER `LECTURAS_DIRIGIDAS.md` y medir sus etiquetas, no
corre la bateria y no escribe ningun veredicto. Escribe UNA entrada en UNA sede,
y si el acta ya esta registrada, NO escribe nada.

USO:
  python scripts/loop/vuelta189_tarea1a_registrar_acta189.py
  python scripts/loop/vuelta189_tarea1a_registrar_acta189.py --simular
  python scripts/loop/vuelta189_tarea1a_registrar_acta189.py --mutacion
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
    PALABRA_CON_CERO, lineas_que_declaran_cero_caidas,
    FRASE_CERO_CAIDAS_PROPIAS, FRASE_SIN_CAIDA_PROPIA,
    PAT_CAIDA_AUDITOR_A, PAT_CAIDA_EJECUTOR_VIEJO, PAT_CAIDA_REPORTE,
    PAT_PD_DEL_TITULO, PAT_P_DEL_TITULO)
from vuelta187_tarea1a_registrar_acta187 import (   # noqa: E402
    PAT_CAIDA_C, seccion_que_contiene)
from vuelta188_tarea1a_registrar_acta188 import (   # noqa: E402
    PAT_CAIDA_C_ESPACIO, acumulan, bloque_de_la_caida,
    MARCAS_DUENO_EJECUTOR, MARCAS_DUENO_AUDITOR)

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")
SEDE = os.path.join(RAIZ, "docs", "PENDIENTES.md")
NL = chr(10)

VUELTA_DEL_ACTA = 189
VUELTA_QUE_ESCRIBE = 189
SUFIJO_QUE_ESCRIBE = "189"
CABECERA_ACTA = "# ACTA DEL AUDITOR, VUELTA %d" % VUELTA_DEL_ACTA
# LA SECCION DE LAS ADJUDICACIONES ES LA 4 EN ESTA ACTA Y ERA LA 5 EN LA ANTERIOR.
# El prefijo NO se hereda: se declara aqui y el patron entrecomillado de la 188 se
# corre al lado para publicar su cifra.
PREFIJO_ADJ = "4."
# LA SECCION QUE TRAE LA ADJUDICACION SUELTA (la de la bateria) Y SU NEGRITA.
SECCION_DEL_HALLAZGO = 5
PAT_ADJ_SUELTA = re.compile(r"^\*\*ADJUDICO: ")

# EL VOCABULARIO DE LA ATRIBUCION. Las marcas heredadas se IMPORTAN y no se
# reescriben; lo que esta vuelta anade va aqui, literal del acta 189 y sin
# parafrasear.
MARCA_AUDITOR_NUEVA = "SON MIAS"
MARCAS_DUENO_AUDITOR_189 = tuple(MARCAS_DUENO_AUDITOR) + (MARCA_AUDITOR_NUEVA,)
# LA MARCA DE CERO DECLARADO. Una cabecera que dice que del ejecutor hay CERO no
# le esta atribuyendo ninguna caida: la palabra `EJECUTOR` esta ahi para declarar
# un cero, no para repartir. Literal de la cabecera de la seccion 6 del acta 189.
MARCAS_CERO_EJECUTOR = ("CERO SON DEL EJECUTOR",)
# LA FRASE CON QUE LA PROSA DEL ACTA DECLARA EL CERO. Literal, y su linea se
# cuenta: el cero no se publica desnudo.
FRASE_CERO_DEL_EJECUTOR = "DEL EJECUTOR: CERO"

# LAS MARCAS DE ESTADO DE UNA ADJUDICACION, LEIDAS DEL TITULO LITERAL. Ninguna se
# ensancha: se buscan tal cual y en este orden.
MARCA_A_FAVOR = "A FAVOR"
MARCA_CORRECCION_PROPIA = "CORRECCION DECLARADA SOBRE MI PROPIA SEDE"
MARCA_SIN_DOCTRINA = "NO HACE FALTA DOCTRINA NUEVA"
MARCA_RACHA = "LA RACHA DE REPORTE SE CORTA"
MARCA_ENCARGO = "EL COTEJO DEBE"


def cuerpo_del_acta(texto=None, cabecera=None):
    """EL ACTA ACOTADA: (lineas, (inicio, fin), error). PURA cuando se le pasan
    `texto` y `cabecera`.

    CLON DECLARADO del de la 188 CON UNA DIFERENCIA QUE SE DICE: alli la cabecera
    era una constante de modulo y aqui es PARAMETRO. No es capricho: el caso
    positivo por mutacion necesita acotar actas FABRICADAS cuya cabecera no es la
    de esta vuelta, y una constante de modulo obliga a parchear el modulo para
    probarlo, que es justo lo que un arnes no debe hacer."""
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


def caidas_por_seccion(lineas, inicio, fin, marcas_eje=None, marcas_aud=None,
                       marcas_cero_eje=None, patron=None):
    """LAS CAIDAS `C.n`, REPARTIDAS POR EL DUENO QUE DECLARA LA CABECERA DE SU
    SECCION. Devuelve (del_ejecutor, del_auditor, sin_dueno). PURA.

    LOS TRES VOCABULARIOS SON PARAMETRO, no constantes escondidas, para que el
    caso positivo por mutacion pueda correr la version VIEJA y la NUEVA sobre el
    MISMO texto y publicar las dos cifras.

    LA REGLA NUEVA, Y ES UNA SOLA: **una cabecera que DECLARA CERO caidas del
    ejecutor no le atribuye ninguna**. Con `marcas_cero_eje` vacio esta funcion se
    comporta EXACTAMENTE como la de la 188 (precedencia del ejecutor), y asi es
    como el arnes corre la version vieja sin tener que copiarla.

    Una `C.n` cuya seccion no diga ni una cosa ni la otra sale en `sin_dueno` y
    quien llama hace PARADA. **Repartir a ojo una caida sin dueno es exactamente
    lo que esta funcion existe para impedir**, y esa PARADA se conserva entera."""
    m_eje = tuple(marcas_eje) if marcas_eje is not None else MARCAS_DUENO_EJECUTOR
    m_aud = tuple(marcas_aud) if marcas_aud is not None else MARCAS_DUENO_AUDITOR_189
    m_cero = tuple(marcas_cero_eje) if marcas_cero_eje is not None else MARCAS_CERO_EJECUTOR
    pat = patron if patron is not None else PAT_CAIDA_C_ESPACIO
    eje, aud, huerfanas = [], [], []
    for i in range(inicio, fin + 1):
        m = pat.match(lineas[i - 1])
        if not m:
            continue
        _ln, cab = seccion_que_contiene(lineas, inicio, fin, i)
        fila = (i, int(m.group(1)), cab)
        alta = cab.upper()
        declara_cero = any(x in alta for x in m_cero)
        if any(x in alta for x in m_eje) and not declara_cero:
            eje.append(fila)
        elif any(x in alta for x in m_aud):
            aud.append(fila)
        else:
            huerfanas.append(fila)
    return eje, aud, huerfanas


def estado_de_la_adjudicacion(titulo):
    """EL ESTADO DE UNA ADJUDICACION, LEIDO DE SU TITULO LITERAL. PURA.

    NO SE TECLEA NINGUNO: se busca en el titulo, EN ESTE ORDEN, `A FAVOR`,
    `CORRECCION DECLARADA SOBRE MI PROPIA SEDE`, `NO HACE FALTA DOCTRINA NUEVA`,
    `LA RACHA DE REPORTE SE CORTA` y `EL COTEJO DEBE`. **Si un titulo no dijera
    ninguna de las cinco, el estado sale `SIN DECIR` y quien llama hace PARADA en
    vez de suponer.**"""
    alto = titulo.upper()
    if MARCA_A_FAVOR in alto:
        return "A FAVOR"
    if MARCA_CORRECCION_PROPIA in alto:
        return "CORRECCION DECLARADA DEL AUDITOR"
    if MARCA_SIN_DOCTRINA in alto:
        return "CONTESTADA SIN DOCTRINA NUEVA"
    if MARCA_RACHA in alto:
        return "RACHA CORTADA"
    if MARCA_ENCARGO in alto:
        return "CONTESTADA Y ENCARGADA"
    return "SIN DECIR"


def familia_de_la_adjudicacion(titulo):
    """SI UNA ADJUDICACION ES UN DISCUTIBLE, UNA PREGUNTA O NINGUNA DE LAS DOS.
    PURA. NO SE TECLEA: sale de que su titulo nombre un `D.n` o un `P.n`."""
    if PAT_P_DEL_TITULO.search(titulo):
        return "PREGUNTA"
    if re.search(r"`D\.(\d+)`", titulo):
        return "DISCUTIBLE"
    return "OTRA"


def marcas_del_acta(vuelta):
    """LAS DOS MARCAS LITERALES CON QUE UNA ENTRADA DE LA SERIE DICE QUE REGISTRA
    EL ACTA `vuelta`. PURA, y computadas de la vuelta y no tecleadas.

    LA PRIMERA es la del TITULO (`... del acta de la vuelta N`) y la SEGUNDA la
    del cuerpo (`(Acta del auditor, vuelta N,`). Las dos son la FORMA DE LA CASA
    y las escriben todos los registradores desde el `R.30`."""
    return ("del acta de la vuelta %d" % vuelta,
            "(Acta del auditor, vuelta %d," % vuelta)


def entradas_que_registran(vuelta, textos_por_sede):
    """LAS ENTRADAS QUE YA REGISTRAN EL ACTA `vuelta`. PURA: recibe
    {ruta: texto} y devuelve [(ruta, linea, marca, texto_de_la_linea)].

    ESTA ES LA IDEMPOTENCIA QUE FALTABA, Y SE COMPRUEBA POR EL ACTA, NO POR EL
    NUMERO. La del registrador de la 188 preguntaba si `## R.<siguiente>.` ya
    estaba en la sede, y `<siguiente>` es por construccion un numero que todavia
    no existe: la respuesta era NO siempre, y por eso re correrlo duplicaba. Aqui
    se busca la marca del ACTA, en LAS DOS SEDES, y si aparece en alguna, no se
    escribe nada."""
    marcas = marcas_del_acta(vuelta)
    halladas = []
    for ruta in sorted(textos_por_sede):
        texto = textos_por_sede[ruta].replace(chr(13) + NL, NL)
        for i, linea in enumerate(texto.split(NL), 1):
            for marca in marcas:
                if marca in linea:
                    halladas.append((ruta, i, marca, linea.strip()))
    return halladas


def titulo_de_la_entrada(n_adj, n_suelta, n_preg, n_cai_aud, n_cai_eje):
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
               trozo_m(n_suelta, "hallazgo adjudicado de la seccion 5",
                       "hallazgos adjudicados de la seccion 5"),
               trozo(n_preg, "pregunta contestada", "preguntas contestadas"),
               trozo(n_cai_aud, "caida propia", "caidas propias"),
               trozo(n_cai_eje, "caida", "caidas"),
               VUELTA_DEL_ACTA))


VIA = {
    "4.1": "SIN TOCAR NADA",
    "4.2": "SIN TOCAR NADA",
    "4.3": "SIN TOCAR NADA",
    "4.4": "A LA VUELTA 190",
    "4.5": "SIN TOCAR NADA",
    "4.6": "SIN TOCAR NADA",
    "4.7": "A LA VUELTA 190",
    "4.8": "A LA VUELTA 190",
    "4.9": "REGISTRADA AQUI",
    "4.10": "REGISTRADA AQUI",
    "5.ADJUDICO": "EJECUTADA",
}

QUE_HACE_ESTA_VUELTA = {
    "4.1": ("SE ACATA SIN TOCAR NADA. El acta adjudica a favor declarar `OP-L-02` "
            "como PARADA en vez de resolverla, y anade que NO ES PARADA DE CAMPANA "
            "todavia: es una MEDICION NO CORRIDA, porque nadie ha buscado si las "
            "tres nominas que su `verificacion` nombra tienen sede en el repo. "
            "**Esa busqueda va a la VUELTA 190 y esta vuelta no la hace**, porque "
            "su encargo dice con todas las letras que nada mas entra en la 189."),
    "4.2": ("SE ACATA SIN TOCAR NADA. `OP-I-01` queda como `(a)`: el producto "
            "existe y la cubre, y la brecha de +349 entre 672 y 323 es ANOTACION y "
            "no encargo. Su sede es `docs/PENDIENTES.md` y es trabajo de plan de "
            "otra vuelta."),
    "4.3": ("SE ACATA SIN TOCAR NADA, Y ES EL ELOGIO QUE MAS IMPORTA DE LAS SEIS. "
            "El acta verifico que la cabecera de la seccion 8 del acta 188 NO "
            "contiene la palabra `EJECUTOR` y que el encargo afirmaba lo "
            "contrario: la conducta adjudicada es medir en vez de creerle al "
            "encargo y declarar la discrepancia en vez de taparla. **Esta vuelta "
            "vuelve a hacer exactamente eso con la cabecera de la seccion 6 del "
            "acta 189**, que se equivoca en el otro sentido."),
    "4.4": ("SE ACATA, Y LA CONDICION QUE EL ACTA LE PUSO VA A LA VUELTA 190. El "
            "cotejo contra el disco de hoy con excepcion mecanica queda a favor; "
            "la condicion es que la excepcion PUBLIQUE SIEMPRE SU LISTA, aunque "
            "este vacia, y eso es codigo que el encargo de la 190 ya lleva escrito. "
            "**Esta vuelta no lo toca.**"),
    "4.5": ("SE ACATA SIN TOCAR NADA. El denominador de lineas con cifra de bytes "
            "queda a favor, y la anotacion del propio ejecutor se conserva: la "
            "cobertura dice cual de los dos universos publica, porque un universo "
            "de lineas no es un universo de sujetos."),
    "4.6": ("SE ACATA SIN TOCAR NADA. Acotar la `3.b` a dos de los cuatro arneses "
            "queda a favor: el ejecutor midio cuales publican numeros de linea del "
            "fichero vivo y son dos, y ponerselo a los otros dos habria movido dos "
            "salidas selladas para nada."),
    "4.7": ("CONTESTADA POR EL ACTA, Y SU REMEDIO VA A LA VUELTA 190. La `P.1` no "
            "necesita doctrina nueva: `NO DECIDIBLE` se queda como esta porque "
            "deja la deuda visible, y meterlo en `CASOS_DECLARADOS` convertiria "
            "una deuda en una exencion. Lo encargado es que la "
            "`guarda_del_sujeto_congelado()` SEPARE en su salida las `NO DECIDIBLE` "
            "que traen motivo escrito de las que no. **La lista de exentos NO se "
            "abre, y esta vuelta no toca la guarda.**"),
    "4.8": ("CONTESTADA POR EL ACTA, Y SU REMEDIO VA A LA VUELTA 190. La `P.2` se "
            "contesta separando el clon que ANADE codigo del que CAMBIA codigo: el "
            "cotejo publica las dos cifras y solo cae en rojo cuando alguna "
            "sentencia del original no sobrevive. **Esta vuelta usa el cotejo tal "
            "como esta hoy** para su clon de la bateria, y pega su salida entera "
            "salga lo que salga."),
    "4.9": ("CONTESTADA POR EL ACTA CON UNA CORRECCION DECLARADA SOBRE SU PROPIA "
            "SEDE, Y ESTA ENTRADA LA REGISTRA SIN BORRAR EL TEXTO VIEJO. El acta "
            "188 escribio *de `LD-01` hasta `LD-98`* y esa cifra es falsa por dos "
            "motivos: ni el maximo es 98, ni la serie es continua. **El documento "
            "NO se toca:** la numeracion no monotona se anota y no se arregla."),
    "4.10": ("REGISTRADA AQUI CON LAS DOS CIFRAS, LA VIEJA Y LA NUEVA. El acta 188 "
             "mantuvo la racha de reporte en **2** y lo hizo bien, porque la "
             "escalada estaba encargada y no construida; hoy la escalada existe, "
             "esta cableada donde `cerrar_reporte.py` juzga y sale verde, y la "
             "vuelta 188 vuelve a cerrar con cero caidas de reporte. **Dos vueltas "
             "seguidas sin ninguna cortan la racha**, y por eso vuelve a **0**. "
             "**La discrepancia con el acta 188 se declara, no se copia.**"),
    "5.ADJUDICO": ("SE ACATA Y SE EJECUTA EN LA TAREA 2 DE ESTA VUELTA. La bateria "
                   "de la 189 corre ENTERA sobre la nomina de hoy y NO hereda ni "
                   "una salida sellada de la corrida 183/184, con un clon declarado "
                   "cuyo `--siguiente` cuenta desde cero. **Y no se borra nada:** "
                   "las nueve salidas de la 183 se quedan donde estan. El bloque "
                   "H.4 del sello de apertura de esta vuelta reprodujo el hallazgo "
                   "entero antes de tocar nada: nomina 125, DIEZ tramos, y "
                   "`--siguiente` diciendo EL SIGUIENTE ES EL TRAMO 10."),
}


def etiquetas_ld(texto):
    """LAS ETIQUETAS `LD-nn` DISTINTAS DE UN TEXTO Y SU MAXIMO. PURA.

    Devuelve (cuantas_distintas, minima, maxima). Es la mitad computable de la
    correccion declarada de la `4.9`: la cifra no se copia del acta, se vuelve a
    medir aqui y se publican LAS DOS."""
    etiquetas = sorted(set(re.findall(r"\bLD-(\d+)\b", texto)), key=int)
    if not etiquetas:
        return 0, None, None
    return len(etiquetas), "LD-" + etiquetas[0], "LD-" + etiquetas[-1]


def racha_declarada(lineas, inicio, fin):
    """LO QUE UN ACTA DICE DE LA RACHA DE REPORTE EN SU TABLA DE CREDITO, LEIDO Y
    NO TECLEADO. Devuelve [(linea, texto)]. PURA."""
    return [(i, lineas[i - 1].strip())
            for i in range(inicio, fin + 1)
            if "racha de reporte" in lineas[i - 1]]


def fila_de_la_metrica(lineas, inicio, fin, aguja):
    """UNA FILA DE LA TABLA DE CREDITO DEL ACTA, LEIDA POR SU PRIMERA CELDA.
    Devuelve [(linea, texto)]. PURA.

    POR QUE EXISTE Y NO SE USA `acumulan()` PARA TODO: `acumulan()` mira el
    BLOQUE de cada caida, y el acta 189 declara lo que hace con las rachas de sus
    caidas propias en la TABLA de la seccion 7, no dentro del bloque de la `C.2`.
    Son DOS mediciones de alcance distinto y **aqui se publican las dos**, en vez
    de elegir la que convenga."""
    return [(i, lineas[i - 1].strip())
            for i in range(inicio, fin + 1)
            if lineas[i - 1].strip().startswith("| " + aguja)]


def especie_de_la_caida(lineas, ln, fin):
    """LA ESPECIE QUE UNA CAIDA DECLARA EN SU BLOQUE. PURA.

    Devuelve `DE METODO`, `DE CLASE`, `DE CIFRA PUBLICADA` o `SIN DECIR`. Si sale
    `SIN DECIR`, quien llama hace PARADA: una caida sin especie no se clasifica a
    ojo."""
    bloque = bloque_de_la_caida(lineas, ln, fin).upper()
    for marca, especie in (("ESPECIE: **DE METODO**", "DE METODO"),
                           ("ESPECIE: **DE CLASE**", "DE CLASE"),
                           ("ESPECIE: **DE CIFRA PUBLICADA**", "DE CIFRA PUBLICADA")):
        if marca in bloque:
            return especie
    return "SIN DECIR"


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
    p.append("Por adicion, como `R.21` a `R.50`. **Corte de todas las cifras de esta")
    p.append("entrada: 6 sep 2026.** El numero de esta entrada NO esta tecleado: lo computa")
    p.append("`scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS sedes.")
    p.append("La SEDE tampoco se supone: sale de la adjudicacion 6.3 del acta 162, que es")
    p.append("la que citan los `R.30` a `R.50`. Salida:")
    p.append("`docs/loop/SALIDA_V%s_T1A_REGISTRO_R%d.txt`."
             % (SUFIJO_QUE_ESCRIBE, numero))
    p.append("")
    p.append("**ESTA ENTRADA SE ESCRIBE CON LA TAREA 1 EN CURSO Y LA TAREA 2, QUE ES LA")
    p.append("BATERIA, SIN CORRER, ASI QUE SUS GLOSAS NO AFIRMAN EN PASADO LO QUE TODAVIA")
    p.append("NO HA PASADO.** Es la forma que la `6.4` del acta 172 adjudico como correcta:")
    p.append("donde una glosa dice EJECUTADA, la tarea que la ejecuta va nombrada; donde")
    p.append("dice que va a ejecutarse, se dice que **todavia no ha corrido**.")
    p.append("")
    p.append("**Y LOS CINCO NUMERALES DEL TITULO TAMPOCO ESTAN TECLEADOS:** se cuentan del")
    p.append("acta acotada (lineas %d a %d) y de ahi sale el numeral en palabra, incluida"
             % (m["inicio"], m["fin"]))
    p.append("la concordancia. **%d adjudicaciones numeradas (`4.1` a `4.%d`, todas en la"
             % (m["n_adj"], m["n_adj"]))
    p.append("seccion 4), %d adjudicacion suelta en la seccion 5 (la de la bateria), %d"
             % (m["n_suelta"], m["n_preg"]))
    p.append("preguntas contestadas DENTRO de las adjudicaciones, %d caidas propias del"
             % m["n_aud"])
    p.append("auditor y %d caidas del ejecutor.**" % m["n_eje"])
    p.append("")
    p.append("**LA SECCION DE LAS ADJUDICACIONES CAMBIO DE NUMERO Y DE FORMA, Y LAS DOS")
    p.append("CIFRAS SE PUBLICAN.** En el acta 188 eran la seccion 5 y se escribian")
    p.append("``**`5.1` ...`` (numeral ENTRE COMILLAS INVERSAS); en el acta 189 son la")
    p.append("seccion **4** y se escriben ``**4.1 ...`` (numeral SIN comillas). Corrido")
    p.append("sobre esta acta, **el patron entrecomillado da %d y el suelto da %d**."
             % (m["n_entrecomillado"], m["n_adj"]))
    p.append("**Ninguno de los dos se ensancha: se corren los dos y se dice lo que dan.**")
    p.append("")
    p.append("**LAS SEIS PRIMERAS SON LOS SEIS DISCUTIBLES DEL EJECUTOR Y LAS SEIS VAN A")
    p.append("FAVOR, Y ESO ESTA MEDIDO Y NO TECLEADO.** Cual adjudicacion es un discutible")
    p.append("y cual es una pregunta **sale de que su titulo literal nombre un `D.n` o un")
    p.append("`P.n`**, no de una lista escrita a mano: **%d nombran un `D.n`, %d nombran un"
             % (m["n_discutibles"], m["n_preg"]))
    p.append("`P.n` y %d no nombran ninguno**. De las %d que nombran un `D.n`, **las %d"
             % (m["n_otras"], m["n_discutibles"], m["n_a_favor_discutibles"]))
    p.append("llevan `A FAVOR` en su titulo literal**. **Si alguna no lo llevara, este")
    p.append("instrumento haria PARADA en vez de escribir que las seis son a favor.**")
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
    p.append("**Y LA SECCION 5 TRAE UNA ADJUDICACION MAS, QUE NO LLEVA NUMERAL Y POR ESO")
    p.append("NINGUN PATRON DE `4.n` LA VE.** Se localiza por su negrita de apertura")
    p.append("`ADJUDICO: ` dentro de la seccion %d, y es la que ORDENA la TAREA 2 de esta"
             % SECCION_DEL_HALLAZGO)
    p.append("vuelta:")
    p.append("")
    for clave, ln, tit in m["sueltas"]:
        p.append("  - **`%s` (`docs/loop/ACTA_AUDITOR.md:%d`, leida hoy). VIA: %s.** Titulo"
                 % (clave, ln, VIA.get(clave, "(sin via)")))
        p.append("    literal del acta: *\"%s\"*" % tit)
        p.append("    **QUE HACE ESTA VUELTA CON ELLA (glosa del ejecutor, no del acta):** %s"
                 % QUE_HACE_ESTA_VUELTA.get(clave, "(sin glosa)"))
    p.append("")
    p.append("**LAS TRES PREGUNTAS ESTAN CONTESTADAS Y NO TIENEN SECCION PROPIA.** El acta")
    p.append("188 las traia en su seccion 7; el acta 189 las contesta DENTRO de las")
    p.append("adjudicaciones. **Cuales son NO se teclea:** son las %d cuyo titulo nombra un"
             % m["n_preg"])
    p.append("`P.n`, y son **%s**. Su estado sale del titulo de cada una y no de una"
             % ", ".join("`%s` que nombra `%s`" % (c, pn)
                         for c, pn in m["preguntas"]))
    p.append("cabecera de seccion, porque esta acta no tiene esa cabecera que leer.")
    p.append("")
    p.append("**LA CORRECCION DECLARADA DEL AUDITOR SOBRE SU PROPIA SEDE (`4.9`), CON EL")
    p.append("TEXTO VIEJO SIN BORRAR.** El acta 188 escribio *\"de `LD-01` hasta `LD-98`\"*")
    p.append("y el acta 189 declara esa cifra FALSA por dos motivos: ni el maximo es 98, ni")
    p.append("la serie es continua. **Y aqui la cifra buena NO se copia del acta: se vuelve")
    p.append("a medir en esta vuelta** sobre `docs/plan/LECTURAS_DIRIGIDAS.md`")
    p.append("(%d bytes en disco, leido hoy):" % m["ld_bytes"])
    p.append("")
    p.append("  - **CIFRA etiquetas `LD-nn` distintas: %d.**" % m["ld_distintas"])
    p.append("  - **La minima es `%s` y la maxima es `%s`.**"
             % (m["ld_min"], m["ld_max"]))
    p.append("  - `LD-154` aparece en la linea **%s** y `LD-98` en la **%s**."
             % (", ".join(str(x) for x in m["ld_lineas_154"]) or "(ninguna)",
                ", ".join(str(x) for x in m["ld_lineas_98"]) or "(ninguna)"))
    p.append("  - **Lo que el acta 189 publica y lo que yo mido: %s.**"
             % ("CALZAN" if m["ld_calza"] else "NO CALZAN, y la discrepancia se declara"))
    p.append("")
    p.append("**EL DOCUMENTO NO SE TOCA:** la numeracion no monotona se anota y no se")
    p.append("arregla, que es lo que el acta adjudica. **Y el texto viejo no se borra:**")
    p.append("queda escrito aqui cual era, con su fecha, al lado del bueno.")
    p.append("")
    p.append("**LA RACHA DE REPORTE SE CORTA Y VUELVE A 0, Y ESO CAMBIA LO QUE DECIA EL")
    p.append("ACTA 188. LAS DOS CIFRAS VAN JUNTAS, LEIDAS DEL FICHERO Y NO TECLEADAS:**")
    p.append("")
    for etiqueta, filas in (("acta 188", m["racha_188"]), ("acta 189", m["racha_189"])):
        for ln, txt in filas:
            p.append("  - **%s** (`docs/loop/ACTA_AUDITOR.md:%d`): %s"
                     % (etiqueta, ln, txt))
    p.append("")
    p.append("El acta 188 la mantuvo en **2** y lo hizo bien: la escalada estaba")
    p.append("**encargada** y no construida. El acta 189 mide que hoy **existe, esta")
    p.append("cableada donde `cerrar_reporte.py` juzga y sale verde**, y que la vuelta 188")
    p.append("vuelve a cerrar con cero caidas de reporte. **La palabra de la regla es")
    p.append("SEGUIDAS: dos vueltas seguidas sin ninguna cortan la racha.** La discrepancia")
    p.append("entre las dos actas **se declara aqui en vez de copiarse**.")
    p.append("")
    p.append("**LAS %s CAIDAS PROPIAS DEL AUDITOR, CON SU LINEA Y SU ESPECIE LEIDA DEL"
             % PALABRA_CON_CERO[m["n_aud"]].upper())
    p.append("BLOQUE.** La atribucion la hace **la cabecera de su seccion** y no quien las")
    p.append("encontro:")
    p.append("")
    for (ln, num, cab), especie in zip(m["c_aud"], m["especies_aud"]):
        p.append("  - `C.%d` en `docs/loop/ACTA_AUDITOR.md:%d`, especie **%s**, bajo la"
                 % (num, ln, especie))
        p.append("    cabecera *\"%s\"*." % cab)
    p.append("")
    p.append("**Y AQUI VA LA MEDICION QUE PRUEBA QUE ESTE REGISTRADOR HACIA FALTA, EN VEZ")
    p.append("DE AFIRMARLO, Y ESTA VEZ EL VOCABULARIO HEREDADO NO ES QUE NO MUERDA: ES QUE")
    p.append("SE EQUIVOCA.** La cabecera de la seccion 6 del acta 189 dice")
    p.append("*\"%s\"* y **contiene la palabra `EJECUTOR`**." % m["cabecera_caidas"])
    p.append("Con el vocabulario de la vuelta 188 (`EJECUTOR` y `LAS SUYAS` para el")
    p.append("ejecutor, con precedencia del ejecutor) corrido sobre ESTA MISMA acta, el")
    p.append("reparto sale **ejecutor %d, auditor %d, huerfanas %d**: **las dos caidas"
             % (m["viejo_eje"], m["viejo_aud"], m["viejo_huerf"]))
    p.append("quedarian atribuidas al ejecutor, y eso es falso**, porque el acta escribe")
    p.append("`MIA` en las dos y `DEL EJECUTOR: CERO` en su prosa.")
    p.append("")
    p.append("**EL REMEDIO NO ES ENSANCHAR NI QUITAR NADA, Y SON DOS MARCAS, LAS DOS")
    p.append("LITERALES DEL ACTA:** se anade `%s` como marca de AUDITOR, y se anade"
             % MARCA_AUDITOR_NUEVA)
    p.append("`%s` como marca de **CERO DECLARADO**. Una cabecera que"
             % MARCAS_CERO_EJECUTOR[0])
    p.append("declara **cero** caidas del ejecutor **no le esta atribuyendo ninguna**: la")
    p.append("mencion de la palabra es una declaracion de cero, no un reparto. Con el")
    p.append("vocabulario de esta vuelta el reparto sale **ejecutor %d, auditor %d,"
             % (m["n_eje"], m["n_aud"]))
    p.append("huerfanas %d**. **La PARADA se conserva entera:** una `C.n` bajo una cabecera"
             % m["n_huerf"])
    p.append("que no diga ni una cosa ni la otra sigue saliendo huerfana y sigue parando.")
    p.append("")
    p.append("**CERO CAIDAS DEL EJECUTOR, Y EL CERO VA CONTADO Y NO OMITIDO.** El patron")
    p.append("`C.n` con espacio da **%d** caidas en el acta y **las %d se atribuyen al"
             % (m["n_c_total"], m["n_aud"]))
    p.append("auditor**, asi que del ejecutor quedan **%d**. **Un cero que sale de un"
             % m["n_eje"])
    p.append("patron que no muerde no es evidencia de nada**, asi que va con la declaracion")
    p.append("literal del acta al lado: la frase `%s` aparece en"
             % FRASE_CERO_DEL_EJECUTOR)
    p.append("**%d linea(s)** (`docs/loop/ACTA_AUDITOR.md:%s`). **Si el patron diera cero y"
             % (len(m["decl_cero_eje"]),
                ", ".join(str(x) for x in m["decl_cero_eje"]) or "ninguna"))
    p.append("el acta no lo declarara, este instrumento haria PARADA.**")
    p.append("")
    p.append("**EL PATRON `R.n` DE LA CAIDA DE REPORTE DA %d SOBRE ESTA ACTA, EL `E.n` DE"
             % m["n_rep"])
    p.append("LAS ACTAS 182 Y 184 DA %d, Y EL `A.n` DE CABECERA DE TERCER NIVEL DA %d.**"
             % (m["n_eje_viejo"], m["n_a"]))
    p.append("Las tres cifras se publican y ninguna se resuelve copiando. **El `A.n` da %d"
             % m["n_a"])
    p.append("y aun asi el auditor declara DOS caidas propias**: las escribe como `C.n`,")
    p.append("que es la forma nueva, y por eso el patron viejo no las ve. **Publicar solo")
    p.append("el %d diria que el auditor no declaro ninguna, y es falso.**" % m["n_a"])
    p.append("")
    p.append("**Y LAS DOS CUENTAS DE RACHA VAN JUNTAS, PORQUE SON DE ALCANCE DISTINTO Y LA")
    p.append("DIFERENCIA SE DECLARA EN VEZ DE ELEGIRSE LA QUE CONVIENE.**")
    p.append("")
    p.append("  - **POR BLOQUE** (`acumulan()`, que busca las marcas literales dentro del")
    p.append("    bloque de cada caida): **%d de las %d dicen que NO acumulan** (%s), y"
             % (len(m["no_acum"]), m["n_aud"],
                ", ".join("`C.%d`" % n for _l, n in m["no_acum"]) or "ninguna"))
    p.append("    **%d no lo dicen en su bloque** (%s). Una caida cuyo bloque no diga nada"
             % (len(m["si_acum"]),
                ", ".join("`C.%d`" % n for _l, n in m["si_acum"]) or "ninguna"))
    p.append("    **se cuenta como QUE ACUMULA**, que es el lado seguro.")
    p.append("  - **POR LA TABLA DE CREDITO DEL ACTA** (seccion 7), leida literal:")
    for ln, txt in m["fila_aud"]:
        p.append("    `docs/loop/ACTA_AUDITOR.md:%d`: %s" % (ln, txt))
    p.append("")
    p.append("**LA DISCREPANCIA SE DECLARA:** el bloque de la `C.2` **no** repite la")
    p.append("formula de no acumular que la `C.1` si escribe, y la tabla de credito **si**")
    p.append("declara que ninguna de las dos abre racha. **Son dos mediciones de alcance")
    p.append("distinto y las dos se publican**; la del bloque es la que este instrumento")
    p.append("computa y la de la tabla es la que el acta declara. **Ninguna se resuelve")
    p.append("copiando la otra.**")
    p.append("")
    p.append("**LA DEUDA DE LA SERIE, QUE SIGUE DOCUMENTADA COMO SALTO Y SIN RELLENAR.**")
    p.append("Se vuelve a medir en esta vuelta en vez de heredarse del `R.50`:")
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
    p.append("**Y ESTA ENTRADA LA ESCRIBE UN REGISTRADOR IDEMPOTENTE, QUE ES LO QUE SALE")
    p.append("DE LA `C.2` DEL ACTA 189 Y ES DEL PROPIO INSTRUMENTO.** El registrador del")
    p.append("acta 188, re corrido, **no detecta que el acta ya esta registrada y escribe")
    p.append("una entrada nueva duplicada con el numero siguiente**; el auditor lo cazo y")
    p.append("tuvo que revertir a mano una `R.51` fantasma de 196 lineas. **La causa se")
    p.append("puede leer en su linea 1348:** comprueba si `## R.<siguiente>.` ya esta en la")
    p.append("sede, y `<siguiente>` es por construccion un numero que todavia no existe.")
    p.append("**Comprobar la idempotencia por el numero que se va a escribir es no")
    p.append("comprobarla.** Este registrador la comprueba **por el acta**, con las marcas")
    p.append("literales `%s` y `%s`, y **en LAS DOS SEDES**."
             % marcas_del_acta(VUELTA_DEL_ACTA))
    p.append("Antes de escribir esta entrada, esas marcas aparecian en **%d linea(s)**."
             % m["ya_registrada"])
    p.append("")
    p.append("**LO QUE ESTA ENTRADA NO REGISTRA, DICHO PARA QUE NO SE BUSQUE:** no registra")
    p.append("la relectura al doble del tramo del puesto **2422**, ni la `P.1` en codigo, ni")
    p.append("la `P.2` en codigo, ni la condicion del `D.4`, ni la busqueda de la sede de")
    p.append("`OP-L-02`: **las cinco van a la vuelta 190** y su encargo ya las lleva")
    p.append("escritas enteras. **Y no se poda la nomina de la bateria**, que es la opcion")
    p.append("`c` que el fundador RECHAZO el 5 sep 2026.")
    return NL.join(p) + NL


# ---------------------------------------------------------------- LA MUTACION
def _acta_fabricada(n_adj, caidas_aud, caidas_eje, cabecera_caidas,
                    vuelta=None, con_declaracion_cero=True):
    """UN ACTA ENTERA FABRICADA, CON LAS CIFRAS QUE SE LE PIDAN. PURA.

    NO SE TOCA EL REPO PARA PROBAR: el arnes corre sobre este texto. Y la
    cabecera de la seccion de caidas es PARAMETRO, que es lo que permite probar
    los tres repartos (auditor, ejecutor y HUERFANA) sin inventar precedencias."""
    v = vuelta if vuelta is not None else VUELTA_DEL_ACTA
    L = []
    L.append("# ACTA DEL AUDITOR, VUELTA %d (fabricada para el arnes)" % v)
    L.append("")
    L.append("## 4. LAS ADJUDICACIONES")
    L.append("")
    for k in range(1, n_adj + 1):
        etiqueta = ("`D.%d`" % k) if k <= n_adj - 1 else "`P.1`"
        L.append("**4.%d %s, un titulo fabricado. A FAVOR.** Prosa de relleno que"
                 % (k, etiqueta))
        L.append("no dice nada y esta aqui para que el parrafo exista.")
        L.append("")
    L.append("## 5. EL HALLAZGO")
    L.append("")
    L.append("**ADJUDICO: UNA COSA FABRICADA QUE SE ADJUDICA SOLA.** Prosa de relleno.")
    L.append("")
    L.append("## 6. %s" % cabecera_caidas)
    L.append("")
    for k in range(1, caidas_aud + caidas_eje + 1):
        L.append("**`C.%d`, FABRICADA.** Prosa de relleno. Especie: **de metodo**. No" % k)
        L.append("acumula, y se dice aqui.")
        L.append("")
    if con_declaracion_cero:
        L.append("**%s.** Prosa de relleno." % FRASE_CERO_DEL_EJECUTOR)
        L.append("")
    L.append("## 7. LA METRICA DE CREDITO")
    L.append("")
    L.append("| caidas propias del auditor | **%d** | ninguna repetida |" % caidas_aud)
    L.append("| caidas del ejecutor de reporte | **0** | racha de reporte: CORTADA |")
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
    exige que el gemelo CAIGA. Un arnes cuyos casos rojos no caen no prueba
    nada."""
    salida = []
    w = salida.append
    w("=" * 78)
    w("CASO POSITIVO POR MUTACION DEL REGISTRADOR DEL ACTA %d" % VUELTA_DEL_ACTA)
    w("=" * 78)
    w("")
    fallos = 0
    mutaciones_que_no_cayeron = 0

    # ---------------------------------------------------------------- BLOQUE A
    w("A) EL ACOTADO DEL ACTA SOBRE UN TEXTO FABRICADO")
    txt = _acta_fabricada(3, 2, 0, "LAS CAIDAS. DOS SON MIAS Y CERO SON DEL EJECUTOR")
    lineas, rango, err = cuerpo_del_acta(txt, "# ACTA DEL AUDITOR, VUELTA %d"
                                         % VUELTA_DEL_ACTA)
    fallos += _caso(w, "error de acotado", err, None)
    fallos += _caso(w, "el acta empieza en la linea 1", rango[0] if rango else None, 1)
    w("   LA MUTACION: se pide una cabecera que el texto NO trae, y tiene que PARAR")
    _l2, _r2, err2 = cuerpo_del_acta(txt, "# ACTA DEL AUDITOR, VUELTA 999")
    if err2 is None:
        w("      LA MUTACION NO CAYO: acoto un acta que no existe.")
        mutaciones_que_no_cayeron += 1
    else:
        w("      LA MUTACION CAE, y su texto es: %s" % err2)
    w("")

    # ---------------------------------------------------------------- BLOQUE B
    w("B) LAS ADJUDICACIONES, CONTADAS CON LOS DOS PATRONES SOBRE EL FABRICADO")
    ini, fin = rango
    n_suelto = len(claves_de_adjudicacion(lineas, ini, fin, PREFIJO_ADJ))
    n_comillas = len(claves_entrecomilladas(lineas, ini, fin, PREFIJO_ADJ))
    fallos += _caso(w, "patron SIN comillas sobre 3 fabricadas", n_suelto, 3)
    fallos += _caso(w, "patron CON comillas sobre 3 fabricadas", n_comillas, 0)
    w("   LA MUTACION: el esperado del patron suelto se cambia a 4 y tiene que CAER")
    if n_suelto == 4:
        w("      LA MUTACION NO CAYO.")
        mutaciones_que_no_cayeron += 1
    else:
        w("      LA MUTACION CAE: %d no es 4." % n_suelto)
    w("")

    # ---------------------------------------------------------------- BLOQUE C
    w("C) LA ATRIBUCION DE LAS CAIDAS, CON LOS DOS VOCABULARIOS Y LOS TRES CASOS")
    cab_189 = "LAS CAIDAS. DOS SON MIAS Y CERO SON DEL EJECUTOR"
    cab_188 = "LAS CAIDAS, LAS SUYAS DECLARADAS Y LAS DOS QUE LEVANTO YO"
    cab_muda = "LAS COSAS QUE PASARON"
    for etiqueta, cab, esperado in (
            ("cabecera al modo 189 (MIAS + CERO del ejecutor)", cab_189, (0, 2, 0)),
            ("cabecera al modo 188 (LAS SUYAS)", cab_188, (2, 0, 0)),
            ("cabecera que no dice de quien son", cab_muda, (0, 0, 2))):
        t = _acta_fabricada(3, 2, 0, cab)
        ls, rg, _e = cuerpo_del_acta(t, "# ACTA DEL AUDITOR, VUELTA %d" % VUELTA_DEL_ACTA)
        eje, aud, hue = caidas_por_seccion(ls, rg[0], rg[1])
        fallos += _caso(w, etiqueta, (len(eje), len(aud), len(hue)), esperado)
    w("   Y EL VOCABULARIO VIEJO SOBRE LA CABECERA DEL 189, QUE ES EL QUE SE EQUIVOCA:")
    t = _acta_fabricada(3, 2, 0, cab_189)
    ls, rg, _e = cuerpo_del_acta(t, "# ACTA DEL AUDITOR, VUELTA %d" % VUELTA_DEL_ACTA)
    eje_v, aud_v, hue_v = caidas_por_seccion(
        ls, rg[0], rg[1], marcas_aud=MARCAS_DUENO_AUDITOR, marcas_cero_eje=())
    fallos += _caso(w, "vocabulario de la 188 sobre la cabecera de la 189",
                    (len(eje_v), len(aud_v), len(hue_v)), (2, 0, 0))
    w("   LA MUTACION: se le quita la marca de CERO DECLARADO al vocabulario nuevo")
    w("   sobre la cabecera del 189, y el reparto TIENE QUE cambiar de (0,2,0)")
    eje_m, aud_m, hue_m = caidas_por_seccion(ls, rg[0], rg[1], marcas_cero_eje=())
    if (len(eje_m), len(aud_m), len(hue_m)) == (0, 2, 0):
        w("      LA MUTACION NO CAYO: sin la marca de cero el reparto no cambia.")
        mutaciones_que_no_cayeron += 1
    else:
        w("      LA MUTACION CAE: sin ella sale (%d, %d, %d) en vez de (0, 2, 0)."
          % (len(eje_m), len(aud_m), len(hue_m)))
    t_mudo = _acta_fabricada(3, 2, 0, cab_muda)
    ls_m, rg_m, _e = cuerpo_del_acta(t_mudo, "# ACTA DEL AUDITOR, VUELTA %d"
                                     % VUELTA_DEL_ACTA)
    _e2, _a2, hue_mudo = caidas_por_seccion(ls_m, rg_m[0], rg_m[1])
    w("   Y LA PARADA SE CONSERVA ENTERA: la cabecera muda deja %d huerfana(s), y una"
      % len(hue_mudo))
    w("   caida huerfana no se reparte a ojo: hace PARADA.")
    w("")

    # ---------------------------------------------------------------- BLOQUE D
    w("D) LA DECLARACION DEL CERO DEL EJECUTOR, QUE NO SE PUBLICA DESNUDO")
    t_con = _acta_fabricada(3, 2, 0, cab_189, con_declaracion_cero=True)
    t_sin = _acta_fabricada(3, 2, 0, cab_189, con_declaracion_cero=False)
    for etiqueta, tt, esperado in (("con la declaracion del cero", t_con, 1),
                                   ("SIN la declaracion del cero", t_sin, 0)):
        ls, rg, _e = cuerpo_del_acta(tt, "# ACTA DEL AUDITOR, VUELTA %d"
                                     % VUELTA_DEL_ACTA)
        n = len([i for i in range(rg[0], rg[1] + 1)
                 if FRASE_CERO_DEL_EJECUTOR in ls[i - 1]])
        fallos += _caso(w, etiqueta, n, esperado)
    w("   LA MUTACION: el acta SIN declaracion tiene que dar 0 y por eso el")
    w("   instrumento hace PARADA en vez de publicar un cero desnudo.")
    w("")

    # ---------------------------------------------------------------- BLOQUE E
    w("E) LA IDEMPOTENCIA, SOBRE SEDES FABRICADAS: ESCRIBIR DOS VECES TIENE QUE CAER")
    marca_titulo, marca_cuerpo = marcas_del_acta(VUELTA_DEL_ACTA)
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
    w("   LA SEGUNDA ESCRITURA, SIMULADA: se intenta escribir otra vez sobre la sede")
    w("   que ya la tiene, y el instrumento TIENE QUE NEGARSE.")
    puede_escribir = len(entradas_que_registran(VUELTA_DEL_ACTA, sede_escrita)) == 0
    if puede_escribir:
        w("      LA MUTACION NO CAYO: dejaria escribir una entrada duplicada.")
        mutaciones_que_no_cayeron += 1
    else:
        w("      LA MUTACION CAE: la segunda escritura queda prohibida, con %d"
          % len(halladas))
        w("      linea(s) de prueba: %s"
          % "; ".join("%s:%d %r" % (r, i, mk) for r, i, mk, _t in halladas))
    w("   Y LA COMPROBACION VIEJA, LA DEL REGISTRADOR DE LA 188, SOBRE LA MISMA SEDE:")
    w("   pregunta si `## R.<siguiente>.` ya esta, y `<siguiente>` no existe todavia.")
    vieja = ("## R.100. " in sede_escrita["fabricada/A.md"])
    fallos += _caso(w, "la comprobacion por NUMERO ve la entrada", vieja, False)
    w("      POR ESO DUPLICABA: la vieja dice que NO esta y la nueva dice que SI.")
    w("")

    # ---------------------------------------------------------------- BLOQUE F
    w("F) EL REGISTRADOR DE LA 188, RE CORRIDO SOBRE EL REPO DE VERDAD, SIN CORRERLO")
    w("   (no se corre: se mide su linea 1348 y se comprueba que el acta 188 SI")
    w("    tiene entrada, o sea que un re corrido suyo escribiria una duplicada)")
    sedes_reales = {}
    for ruta in SERIE.SEDES:
        rel = os.path.relpath(ruta, RAIZ).replace("\\", "/")
        sedes_reales[rel] = io.open(ruta, encoding="utf-8", errors="replace").read()
    ya_188 = entradas_que_registran(188, sedes_reales)
    fallos += _caso(w, "el acta 188 YA tiene entrada en la serie", len(ya_188) > 0, True)
    for r, i, mk, t in ya_188:
        w("      %s:%d %r" % (r, i, t[:88]))
    w("")

    # ---------------------------------------------------------------- BLOQUE G
    w("G) LAS ETIQUETAS `LD-nn`, SOBRE UN TEXTO FABRICADO Y SOBRE EL DE VERDAD")
    fab = "LD-01 LD-01 LD-07 LD-154 LD-98"
    fallos += _caso(w, "distintas sobre el fabricado", etiquetas_ld(fab)[0], 4)
    fallos += _caso(w, "maxima sobre el fabricado", etiquetas_ld(fab)[2], "LD-154")
    w("   LA MUTACION: el esperado de la maxima se cambia a `LD-98` y tiene que CAER")
    if etiquetas_ld(fab)[2] == "LD-98":
        w("      LA MUTACION NO CAYO.")
        mutaciones_que_no_cayeron += 1
    else:
        w("      LA MUTACION CAE: la maxima es %s y no LD-98, que es EXACTAMENTE la"
          % etiquetas_ld(fab)[2])
        w("      especie de la cifra falsa que el acta 188 publico.")
    w("")

    w("=" * 78)
    w("CIFRA casos: los de arriba, uno por linea con PASA o CAE")
    w("CIFRA casos que CAEN: %d" % fallos)
    w("CIFRA mutaciones que NO cayeron (y deberian): %d" % mutaciones_que_no_cayeron)
    if fallos or mutaciones_que_no_cayeron:
        w("VEREDICTO: ROJO")
    else:
        w("VEREDICTO: VERDE")
    texto = NL.join(salida) + NL
    ruta = os.path.join(LOOP, "SALIDA_V%s_T1A_MUTACION_REGISTRADOR.txt"
                        % SUFIJO_QUE_ESCRIBE)
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(texto)
    print(texto)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(texto.encode("utf-8"))))
    return 1 if (fallos or mutaciones_que_no_cayeron) else 0


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
    w("   Y EL CONTRASTE CON LA COMPROBACION VIEJA, LA DEL REGISTRADOR DE LA 188:")
    w("      la suya pregunta si `## R.<siguiente>.` ya esta en UNA sede, y")
    w("      `<siguiente>` es por construccion un numero que todavia no existe.")
    ya_188 = entradas_que_registran(188, sedes)
    w("      sobre el acta 188, la comprobacion POR EL ACTA halla %d linea(s):"
      % len(ya_188))
    for r, i, mk, t in ya_188:
        w("         %s:%d %r" % (r, i, t[:100]))
    w("")

    w("C) LAS ADJUDICACIONES, CONTADAS CON LOS DOS PATRONES Y NO TECLEADAS")
    claves = claves_de_adjudicacion(lineas, inicio, fin, PREFIJO_ADJ)
    entrecomilladas = claves_entrecomilladas(lineas, inicio, fin, PREFIJO_ADJ)
    w("   patron SIN comillas inversas (el del acta 189) -> %d" % len(claves))
    for clave, cuantas in claves:
        w("      %s -> %d aparicion(es)" % (clave, cuantas))
    w("   patron CON comillas inversas (el del acta 188) -> %d" % len(entrecomilladas))
    dobles = [c for c, n in claves if n != 1]
    if dobles:
        w("   PARADA: hay claves repetidas dentro del acta: %s" % ", ".join(dobles))
        print(NL.join(salida))
        return 1
    if not claves:
        w("   PARADA: ningun patron encuentra adjudicaciones y el acta 189 declara")
        w("   diez. No se escribe una entrada con cero.")
        print(NL.join(salida))
        return 1
    w("")

    w("D) EL TITULO LITERAL DE CADA ADJUDICACION, SU FAMILIA Y SU ESTADO")
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
    w("   REPARTO POR FAMILIA: discutibles %d | preguntas %d | otras %d"
      % (len(discutibles), len(preguntas), len(otras)))
    w("   DE LOS DISCUTIBLES, LOS QUE LLEVAN `A FAVOR` EN SU TITULO: %d de %d"
      % (len(a_favor), len(discutibles)))
    if len(a_favor) != len(discutibles):
        w("   PARADA: el encargo dice que los seis discutibles van A FAVOR y el acta")
        w("   no lo dice en %d de ellos. No se escribe lo que no se lee."
          % (len(discutibles) - len(a_favor)))
        print(NL.join(salida))
        return 1
    if not preguntas:
        w("   PARADA: ninguna adjudicacion nombra un `P.n` y el acta 189 declara TRES")
        w("   preguntas contestadas. No se escribe una lista vacia.")
        print(NL.join(salida))
        return 1
    w("")

    w("E) LA ADJUDICACION SUELTA DE LA SECCION %d, LOCALIZADA POR SU NEGRITA"
      % SECCION_DEL_HALLAZGO)
    ini5 = None
    fin5 = fin
    for i in range(inicio, fin + 1):
        if re.match(r"^## %d\." % SECCION_DEL_HALLAZGO, lineas[i - 1]):
            ini5 = i
            break
    if ini5 is not None:
        for i in range(ini5 + 1, fin + 1):
            if lineas[i - 1].startswith("## "):
                fin5 = i - 1
                break
    sueltas = []
    if ini5 is None:
        w("   PARADA: el acta no tiene seccion %d." % SECCION_DEL_HALLAZGO)
        print(NL.join(salida))
        return 1
    w("   la seccion %d va de la linea %d a la %d" % (SECCION_DEL_HALLAZGO, ini5, fin5))
    res, err3 = titulo_de_la_negrita(lineas, ini5, fin5, PAT_ADJ_SUELTA,
                                     "la adjudicacion suelta")
    if err3:
        w("   %s" % err3)
        print(NL.join(salida))
        return 1
    ln5, tit5 = res
    sueltas.append(("5.ADJUDICO", ln5, tit5))
    w("   linea %d: %s" % (ln5, tit5[:160]))
    w("")

    w("F) LAS CAIDAS, CON LA ATRIBUCION HECHA POR LA CABECERA DE SU SECCION")
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
    c_eje, c_aud, huerfanas = caidas_por_seccion(lineas, inicio, fin)
    viejo = caidas_por_seccion(lineas, inicio, fin,
                               marcas_aud=MARCAS_DUENO_AUDITOR, marcas_cero_eje=())
    w("   CON EL VOCABULARIO DE LA 188 (sin `SON MIAS` y sin la marca de CERO):")
    w("      ejecutor %d | auditor %d | huerfanas %d"
      % (len(viejo[0]), len(viejo[1]), len(viejo[2])))
    for ln, num, cab in viejo[0]:
        w("         AL EJECUTOR (y es FALSO): LINEA %d C.%d bajo %r" % (ln, num, cab[:90]))
    w("   CON EL VOCABULARIO DE ESTA VUELTA (anade `%s` y la marca de CERO `%s`):"
      % (MARCA_AUDITOR_NUEVA, MARCAS_CERO_EJECUTOR[0]))
    w("      DEL EJECUTOR: %d" % len(c_eje))
    w("      DEL AUDITOR: %d" % len(c_aud))
    for ln, num, cab in c_aud:
        w("         LINEA %d: C.%d bajo %r" % (ln, num, cab[:90]))
        w("            %s" % lineas[ln - 1].strip()[:130])
    w("      HUERFANAS: %d" % len(huerfanas))
    for ln, num, cab in huerfanas:
        w("         LINEA %d: C.%d bajo %r" % (ln, num, cab[:90]))
    if huerfanas:
        w("   PARADA: hay %d caida(s) `C.n` en una seccion cuya cabecera no dice de"
          % len(huerfanas))
        w("   quien son. Una caida sin dueno no se reparte a ojo.")
        print(NL.join(salida))
        return 1
    if not c_aud:
        w("   PARADA: no se encuentra ninguna caida propia del auditor, y el acta 189")
        w("   declara DOS en su seccion 6. No se escribe una entrada asi.")
        print(NL.join(salida))
        return 1
    especies = [especie_de_la_caida(lineas, ln, fin) for ln, _n, _c in c_aud]
    w("   LA ESPECIE DE CADA CAIDA PROPIA, LEIDA DE SU BLOQUE: %s"
      % ", ".join("C.%d %s" % (n, e) for (_l, n, _c), e in zip(c_aud, especies)))
    if "SIN DECIR" in especies:
        w("   PARADA: alguna caida no declara su especie en su bloque.")
        print(NL.join(salida))
        return 1
    w("")

    w("G) EL CERO DEL EJECUTOR, CONTADO Y CON SU DECLARACION AL LADO")
    decl_cero = [i for i in range(inicio, fin + 1)
                 if FRASE_CERO_DEL_EJECUTOR in lineas[i - 1]]
    decl_vieja, decl_nueva = lineas_que_declaran_cero_caidas(lineas, inicio, fin)
    w("   CIFRA caidas del ejecutor que el reparto halla: %d" % len(c_eje))
    w("   la frase %r aparece en %d linea(s): %s"
      % (FRASE_CERO_DEL_EJECUTOR, len(decl_cero),
         ", ".join(str(x) for x in decl_cero) or "ninguna"))
    for i in decl_cero:
        w("      LINEA %d: %s" % (i, lineas[i - 1].strip()[:120]))
    w("   la frase %r (acta 186) aparece en %d linea(s)"
      % (FRASE_CERO_CAIDAS_PROPIAS, len(decl_nueva)))
    w("   la frase %r (acta 185) aparece en %d linea(s)"
      % (FRASE_SIN_CAIDA_PROPIA, len(decl_vieja)))
    if not c_eje and not decl_cero:
        w("   PARADA: cero caidas del ejecutor Y el acta no lo declara por la frase.")
        w("   Un cero de un patron que no muerde no se publica como medicion.")
        print(NL.join(salida))
        return 1
    w("")

    w("H) LAS DOS CUENTAS DE RACHA, QUE SON DE ALCANCE DISTINTO")
    si_acum, no_acum = acumulan(lineas, fin, c_aud)
    w("   POR BLOQUE: acumulan %d (%s) | no acumulan %d (%s)"
      % (len(si_acum), ", ".join("C.%d" % n for _l, n in si_acum) or "ninguna",
         len(no_acum), ", ".join("C.%d" % n for _l, n in no_acum) or "ninguna"))
    fila_aud = fila_de_la_metrica(lineas, inicio, fin, "caidas propias del auditor")
    for ln, txt in fila_aud:
        w("   POR LA TABLA (linea %d): %s" % (ln, txt))
    w("   LA DISCREPANCIA SE DECLARA Y NO SE RESUELVE COPIANDO: el bloque de una de")
    w("   ellas no repite la formula, la tabla si declara que ninguna abre racha.")
    w("")

    w("I) LA RACHA DE REPORTE, CON LAS DOS CIFRAS LEIDAS DE LAS DOS ACTAS")
    lineas188, rango188, err188 = cuerpo_del_acta(
        cabecera="# ACTA DEL AUDITOR, VUELTA 188")
    racha_188 = []
    if err188:
        w("   NO SE PUDO ACOTAR EL ACTA 188: %s" % err188)
    else:
        racha_188 = racha_declarada(lineas188, rango188[0], rango188[1])
    racha_189 = racha_declarada(lineas, inicio, fin)
    for etiqueta, filas in (("acta 188", racha_188), ("acta 189", racha_189)):
        for ln, txt in filas:
            w("   %s (linea %d): %s" % (etiqueta, ln, txt))
    if not racha_188 or not racha_189:
        w("   PARADA: alguna de las dos actas no dice nada de la racha de reporte, y")
        w("   la `4.10` exige publicar LAS DOS cifras.")
        print(NL.join(salida))
        return 1
    w("")

    w("J) LA CORRECCION DECLARADA DE LA `4.9`, REMEDIDA HOY Y NO COPIADA DEL ACTA")
    LD = os.path.join(RAIZ, "docs", "plan", "LECTURAS_DIRIGIDAS.md")
    t_ld = io.open(LD, encoding="utf-8", errors="replace").read()
    ld_n, ld_min, ld_max = etiquetas_ld(t_ld)
    lin_ld = t_ld.replace(chr(13) + NL, NL).split(NL)
    ld_154 = [i for i, l in enumerate(lin_ld, 1) if "LD-154" in l]
    ld_98 = [i for i, l in enumerate(lin_ld, 1) if "LD-98" in l]
    w("   docs/plan/LECTURAS_DIRIGIDAS.md -> disco %d bytes | %d lineas"
      % (os.path.getsize(LD), len(lin_ld)))
    w("   CIFRA etiquetas `LD-nn` distintas: %d" % ld_n)
    w("   minima %s | maxima %s" % (ld_min, ld_max))
    w("   `LD-154` en la(s) linea(s): %s" % ", ".join(str(x) for x in ld_154))
    w("   `LD-98` en la(s) linea(s): %s" % ", ".join(str(x) for x in ld_98))
    ld_calza = (ld_n == 68 and ld_max == "LD-154")
    w("   el acta 189 publica 68 distintas y maximo `LD-154` -> %s"
      % ("CALZA" if ld_calza else "NO CALZA, y la discrepancia se declara"))
    w("")

    w("K) EL NUMERO DE LA ENTRADA, QUE NO SE TECLEA")
    halladas = SERIE.entradas()
    numero = SERIE.siguiente_libre(halladas)
    w("   serie recomputada de sus dos sedes: %d entradas" % len(halladas))
    w("   CIFRA colisiones: %d | CIFRA huecos: %d"
      % (len(SERIE.colisiones(halladas)), len(SERIE.huecos(halladas))))
    w("   SIGUIENTE LIBRE: R.%d" % numero)
    w("")

    w("L) LA DEUDA DE LA SERIE, REMEDIDA EN ESTA VUELTA Y NO HEREDADA DEL R.50")
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

    medido = {
        "inicio": inicio, "fin": fin, "secciones": secciones,
        "n_adj": len(claves), "n_entrecomillado": len(entrecomilladas),
        "adjudicaciones": adjudicaciones, "sueltas": sueltas,
        "n_suelta": len(sueltas),
        "n_discutibles": len(discutibles), "n_preg": len(preguntas),
        "n_otras": len(otras), "n_a_favor_discutibles": len(a_favor),
        "preguntas": [(c, PAT_P_DEL_TITULO.search(t).group(0).strip("`"))
                      for c, _f, _e, _l, t in preguntas],
        "c_aud": c_aud, "especies_aud": especies,
        "n_aud": len(c_aud), "n_eje": len(c_eje), "n_huerf": len(huerfanas),
        "viejo_eje": len(viejo[0]), "viejo_aud": len(viejo[1]),
        "viejo_huerf": len(viejo[2]),
        "n_c_total": len(n_c_espacio), "n_c_crudo": len(n_c_crudo),
        "n_a": len(l_aud_a), "n_rep": len(l_rep), "n_eje_viejo": len(l_eje_v),
        "decl_cero_eje": decl_cero,
        "si_acum": si_acum, "no_acum": no_acum, "fila_aud": fila_aud,
        "racha_188": racha_188, "racha_189": racha_189,
        "ld_bytes": os.path.getsize(LD), "ld_distintas": ld_n,
        "ld_min": ld_min, "ld_max": ld_max,
        "ld_lineas_154": ld_154, "ld_lineas_98": ld_98, "ld_calza": ld_calza,
        "cabecera_caidas": c_aud[0][2],
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

    w("M) EL TITULO, CON SUS CINCO NUMERALES COMPUTADOS")
    titulo = titulo_de_la_entrada(m["n_adj"], m["n_suelta"], m["n_preg"],
                                  m["n_aud"], m["n_eje"])
    w("   %s" % titulo)
    w("")

    numero = m["numero"]
    entrada = armar_entrada(numero, titulo, m)
    w("N) LA ENTRADA ARMADA")
    w("   %d bytes | %d lineas" % (len(entrada.encode("utf-8")), entrada.count(NL)))
    w("   guiones largos o medios en la entrada: %d"
      % (entrada.count(chr(8212)) + entrada.count(chr(8211))))
    w("")

    texto_sede = io.open(SEDE, encoding="utf-8").read().replace(chr(13) + NL, NL)
    if a.simular:
        w("O) MODO --simular: NO SE ESCRIBE NADA EN LA SEDE.")
        w("")
        w("LA ENTRADA, ENTERA:")
        for l in entrada.split(NL):
            w("   | " + l)
    elif m["ya_registrada"]:
        w("O) NO SE ESCRIBE NADA, Y ESTA ES LA IDEMPOTENCIA HACIENDO SU TRABAJO.")
        w("   el acta %d YA TIENE ENTRADA en la serie: %d linea(s) la nombran."
          % (VUELTA_DEL_ACTA, m["ya_registrada"]))
        w("   NO se escribe una entrada nueva y NO se consume el numero R.%d." % numero)
    else:
        nuevo = texto_sede.rstrip(NL) + NL + NL + entrada
        io.open(SEDE, "w", encoding="utf-8", newline=NL).write(nuevo)
        w("O) ESCRITA EN docs/PENDIENTES.md")
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
        w("   nada. Eso es lo que la `C.2` del acta 189 pedia.")
    w("")
    t = NL.join(salida) + NL
    # EL NOMBRE DE LA SALIDA DICE LO QUE PASO, Y NO LO CONTRARIO. Si la entrada no
    # se escribio, la salida NO se llama `REGISTRO_R<n>`: ese nombre prometeria un
    # registro que no existe, y `EJECUTOR.md` 1 dice que una ruta publicada como
    # prueba es CIFRA. Cuando la idempotencia muerde, `numero` es un numero que NO
    # se consumio, y nombrar el fichero con el seria escribir una cifra falsa en
    # una ruta.
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
