# -*- coding: utf-8 -*-
r"""vuelta184_tarea1a_registrar_acta184.py . EL ACTA 184 ENTERA, REGISTRADA EN LA
SERIE `R.N` EN LA FORMA DE LA CASA.

LA MAQUINA NO SE CLONA, SE IMPORTA, y eso lo adjudico la `6.6` del acta 172 como
correcto y obligatorio: `PALABRA` y `titulo_de_la_negrita` se importan de
`scripts/loop/vuelta172_tarea1_registrar_acta171.py`, `claves_de_adjudicacion` y
`cuenta_por_patron` del registrador de la vuelta 182, y `actas_sin_entrada` del de
la 183. Lo unico propio de este fichero es EL ACOTE DE SU ACTA, LOS PATRONES QUE
SU ACTA NECESITA Y SUS GLOSAS.

POR QUE HACE FALTA CODIGO PROPIO OTRA VEZ, MEDIDO Y NO SUPUESTO, Y SON TRES COSAS:

  1) EL ACTA 184 ESCRIBE SUS NUMERALES ENTRE COMILLAS INVERSAS. El acta 183 los
     escribia ``**5.1 ...`` y el acta 184 los escribe ``**`5.1` PD.1, ...``. El
     patron importado, que pide ``**5.1 `` con espacio detras, cuenta **CERO**
     sobre esta acta, y esa cifra se publica al lado de la buena. SE ANADE UN
     PATRON, NO SE ENSANCHA EL VIEJO hasta que trague: la forma entrecomillada se
     nombra, se mide y se declara.

  2) EL ACTA 184 TIENE UNA ADJUDICACION QUE NO LLEVA NUMERAL `5.n`. Es la de su
     punto 6, *"LA ADJUDICACION QUE EL EJECUTOR TRAJO SIN RESOLVER, Y ES TRABAJO
     MIO"*, que vive en una seccion propia y no en la lista de la seccion 5. UN
     CONTADOR QUE SOLO BARRE `5.n` LA PIERDE, y perder una adjudicacion en el
     registro es exactamente la especie que esta serie existe para impedir. Se
     cuenta APARTE, con su patron propio, y el titulo de la entrada la nombra.

  3) LA CAIDA DEL EJECUTOR VUELVE A LA FORMA DEL ACTA 182 y deja la del acta 183.
     El acta 183 la escribia dentro del titulo de su primera adjudicacion; el acta
     184 la escribe otra vez como ``**`E.1`, ...`` al principio de linea, en su
     seccion 7. Los DOS patrones se corren y las DOS cifras se publican, que es lo
     que prueba cual muerde hoy.

LAS CAIDAS PROPIAS DEL AUDITOR SON CERO, Y UN CERO SE PUBLICA CON SU DECLARACION
AL LADO O NO VALE. Es la regla que estreno el registrador de la 183 y que el
encargo de esta vuelta repite con todas las letras: si el patron diera cero Y el
acta no lo declarara, el instrumento HACE PARADA en vez de escribir la entrada.

LAS CIFRAS DEL TITULO NO SE TECLEAN: se cuentan del acta acotada. Ni el numero de
la entrada: lo devuelve `scripts/loop/serie_de_registros.py` recomputando la serie
de sus DOS sedes. Y LA DEUDA DE LA SERIE SE REMIDE EN ESTA VUELTA y no se hereda
del `R.45`, que es lo que el encargo pide con esas palabras.

LO QUE ESTE FICHERO NO HACE: no toca el acta, no toca el reporte, no toca
`docs/plan/`, no corre la bateria y no escribe ningun veredicto. Escribe UNA
entrada en UNA sede, y si la entrada ya esta, NO la duplica y lo dice.

USO:
  python scripts/loop/vuelta184_tarea1a_registrar_acta184.py
  python scripts/loop/vuelta184_tarea1a_registrar_acta184.py --simular
  python scripts/loop/vuelta184_tarea1a_registrar_acta184.py --mutacion
"""
import argparse
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import serie_de_registros as SERIE   # noqa: E402
from vuelta172_tarea1_registrar_acta171 import (   # noqa: E402
    PALABRA, titulo_de_la_negrita)
from vuelta182_tarea1a_registrar_acta181 import (   # noqa: E402
    claves_de_adjudicacion, cuenta_por_patron)
from vuelta183_tarea1a_registrar_acta182 import actas_sin_entrada   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")
SEDE = os.path.join(RAIZ, "docs", "PENDIENTES.md")
NL = chr(10)

VUELTA_DEL_ACTA = 184
VUELTA_QUE_ESCRIBE = 184
SUFIJO_QUE_ESCRIBE = "184"
CABECERA_ACTA = "# ACTA DEL AUDITOR, VUELTA %d" % VUELTA_DEL_ACTA
PREFIJO_ADJ = "5."

PALABRA_CON_CERO = dict(PALABRA)
PALABRA_CON_CERO[0] = "cero"

# LOS PATRONES. Los que llevan `VIEJO` en el nombre son los de las actas
# anteriores y se conservan a proposito: su CERO sobre esta acta es la medicion
# que prueba que hacia falta uno nuevo.
PAT_CAIDA_EJECUTOR = re.compile(r"^\s*(?:-\s+)?\*\*`?E\.(\d+)`?[,.]")
PAT_CAIDA_EJECUTOR_EN_TITULO_VIEJO = re.compile(
    r"^\*\*\d+\.\d+ .*CAIDA DEL EJECUTOR, `E\.(\d+)`")
PAT_CAIDA_AUDITOR = re.compile(r"^\s*(?:-\s+)?\*\*`?C\.(\d+)`?[,.]")
PAT_CAIDA_AUDITOR_PROSA = re.compile(r"^\*\*[^*]*CAIDA[^*]*`C\.(\d+)`")
FRASE_SIN_CAIDA_PROPIA = "NINGUNA CAIDA PROPIA"

# LA ADJUDICACION SIN NUMERAL, LA DEL PUNTO 6. Su sede es una CABECERA DE SECCION
# y no una negrita de lista, y por eso tiene patron propio.
PAT_ADJ_SIN_NUMERAL = re.compile(r"^##\s+6\.\s+LA ADJUDICACION\b")
CLAVE_SIN_NUMERAL = "punto 6"


def claves_entrecomilladas(lineas, inicio, fin, prefijo, tope=40):
    """LAS ADJUDICACIONES ESCRITAS ``**`5.1` ...``, o sea con el numeral entre
    comillas inversas, que es la forma del acta 184. PURA.

    ES UN PATRON NUEVO Y NO UN ENSANCHE DEL VIEJO: el importado sigue intacto y
    su cifra sobre esta acta se publica al lado. La diferencia entre anadir y
    ensanchar es la que el reporte de la 183 uso en su 1.a y la que el acta 184
    adjudico a favor en su `5.3`."""
    claves = []
    for k in range(1, tope + 1):
        clave = "%s%d" % (prefijo, k)
        pat = re.compile(r"^\s*\*\*`%s` " % re.escape(clave))
        cuantas = len([i for i in range(inicio, fin + 1) if pat.match(lineas[i - 1])])
        if cuantas == 0:
            break
        claves.append((clave, cuantas))
    return claves


def cuerpo_del_acta(texto=None):
    """EL ACTA ACOTADA: (lineas, (inicio, fin), error). El fin es el final del
    fichero porque el acta 184 es la ultima escrita; si algun dia dejara de
    serlo, la cabecera siguiente seria la frontera. CAE EN ROJO antes que contar
    de mas.

    PURA cuando se le pasa `texto`, que es lo que permite que el caso positivo
    por mutacion la corra sobre un acta fabricada sin tocar el repo."""
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


def lineas_que_declaran_cero_caidas(lineas, inicio, fin):
    """LAS LINEAS DONDE EL ACTA DECLARA QUE NO TUVO CAIDAS PROPIAS. PURA.

    Un cero que sale de un patron que no muerde y un cero que el acta declara con
    todas las letras son la misma cifra y NO son la misma evidencia."""
    return [i for i in range(inicio, fin + 1)
            if FRASE_SIN_CAIDA_PROPIA in lineas[i - 1]]


def lineas_de_la_adjudicacion_sin_numeral(lineas, inicio, fin):
    """LA ADJUDICACION QUE NO LLEVA NUMERAL `5.n`, LOCALIZADA POR SU CABECERA DE
    SECCION. PURA. Devuelve la lista de lineas donde aparece, para que el numero
    salga de contarla y no de recordarla."""
    return [i for i in range(inicio, fin + 1)
            if PAT_ADJ_SIN_NUMERAL.match(lineas[i - 1])]


def titulo_de_la_entrada(n_adj, n_sin_numeral, n_cai_aud, n_cai_eje):
    """El titulo, con sus CUATRO numerales COMPUTADOS y no tecleados, y con la
    concordancia dentro del computo. El CERO entra por `PALABRA_CON_CERO`, y va
    en plural porque en castellano el cero es plural.

    EL CUARTO NUMERAL ES NUEVO Y ES EL DEL PUNTO 6: si no estuviera, el titulo
    diria siete adjudicaciones cuando el acta trae ocho, y una entrada que cuenta
    de menos es peor que no tenerla."""
    def trozo(n, sing, plur):
        if n == 1:
            return "la %s" % sing
        return "las %s %s" % (PALABRA_CON_CERO[n], plur)
    if n_sin_numeral == 1:
        cola = "la adjudicacion del punto 6"
    else:
        cola = "las %s adjudicaciones sin numeral" % PALABRA_CON_CERO[n_sin_numeral]
    return ("Registro de %s numeradas, %s, %s del auditor y %s del ejecutor "
            "del acta de la vuelta %d"
            % (trozo(n_adj, "adjudicacion", "adjudicaciones"),
               cola,
               trozo(n_cai_aud, "caida propia", "caidas propias"),
               trozo(n_cai_eje, "caida", "caidas"),
               VUELTA_DEL_ACTA))


VIA = {
    "5.1": "SIN TOCAR NADA",
    "5.2": "SIN TOCAR NADA",
    "5.3": "SIN TOCAR NADA",
    "5.4": "SIN TOCAR NADA",
    "5.5": "SIN TOCAR NADA",
    "5.6": "SIN TOCAR NADA",
    "5.7": "SIN TOCAR NADA",
    CLAVE_SIN_NUMERAL: "EJECUTADA",
}

QUE_HACE_ESTA_VUELTA = {
    "5.1": ("SE ACATA SIN TOCAR NADA, Y ES UNA CONCESION AL EJECUTOR. La fila de la "
            "continuacion entro como TAREA 3 y no renumerando la tabla, y el acta lo "
            "adjudica a favor citando `EJECUTOR.md` 8: renumerar habria pisado una fila "
            "ya cerrada y ya auditada. No hay trabajo pendiente en ella."),
    "5.2": ("SE ACATA SIN TOCAR NADA, Y EL ACTA LA SACA DE LA LISTA DE DISCUTIBLES. El "
            "sufijo `183B` de las salidas de apertura no era una preferencia de nombre: "
            "pisar `docs/loop/SALIDA_V183_APERTURA.txt` habria falseado una cifra que el "
            "acta 183 ya publica como prueba. LA REGLA QUE DEJA SE APLICA HOY: el bloque "
            "de apertura de esta vuelta escribe con sufijo `184` y no pisa ninguna "
            "salida sellada de la 183."),
    "5.3": ("SE ACATA SIN TOCAR NADA, Y SU DOCTRINA SE APLICA EN LA TAREA 1.a DE ESTA "
            "MISMA VUELTA. El acta concede el ensanche del guarda porque lo forzaron dos "
            "casos reales y porque las citas legitimas se eximen NOMBRANDOLAS. Aqui pasa "
            "lo mismo con los numerales entrecomillados del acta 184: SE ANADE UN PATRON "
            "NUEVO, `claves_entrecomilladas`, y el viejo se conserva intacto con su cero "
            "publicado al lado."),
    "5.4": ("SE ACATA SIN TOCAR NADA. Los dos prefijos de `mkdtemp` que quedaban fuera "
            "de la letra del encargo quedan concedidos, y su medicion la confirmo el "
            "propio auditor: las menciones falsas bajan de tres por fichero a una."),
    "5.5": ("SE ACATA SIN TOCAR NADA. La cuarta ruta escrita entera queda concedida por "
            "la misma regla que la `5.2`, y esta vuelta la sigue aplicando: toda ruta "
            "que este reporte publique como prueba va con su carpeta y su prefijo."),
    "5.6": ("SE ACATA SIN TOCAR NADA, Y ESTA VUELTA VUELVE A HACER LA MISMA CUENTA. El "
            "arnes que entra a la nomina en su misma vuelta queda concedido por el acta "
            "176 punto 7.2. Lo que el acta 184 ANOTA sin convertirlo en regla, y esta "
            "entrada recoge sin adornar, es que una entrada que entra en su propia vuelta "
            "NO HA PASADO NUNCA POR UNA BATERIA antes de contar como guarda, y que las "
            "tres entradas que hicieron fallar al arnes de la 165 entraron asi."),
    "5.7": ("SE ACATA SIN TOCAR NADA, Y ES LA QUE ORDENA LA TAREA 1.b DE ESTA VUELTA. El "
            "acta adjudica a favor, y sin regatear, no haber arreglado el rojo del tramo "
            "5: actualizar la lista tecleada para que calzara con la medicion de hoy es "
            "resolver la discrepancia copiando, que `EJECUTOR.md` 2 prohibe con todas las "
            "letras. La eleccion entre los dos caminos la hace el auditor en su punto 6, "
            "y esta vuelta EJECUTA esa eleccion."),
    CLAVE_SIN_NUMERAL: (
        "EJECUTADA EN LA TAREA 1.b DE ESTA VUELTA, QUE ES SU OPERACION DE CODIGO, Y ES LA "
        "UNICA ADJUDICACION DEL ACTA QUE MANDA TOCAR CODIGO. El auditor descarta el camino "
        "de la nomina fabricada porque mataria lo unico que el caso A aporta, que es ser el "
        "UNICO de los trece que mira la nomina REAL, y adjudica cuatro cosas que se ejecutan "
        "sin decidir nada mas: `esperadas` deja de teclearse y se computa de la nomina real; "
        "los dos ficheros que el auditor de la 165 nombro NO se borran y el caso pasa a "
        "exigir que sigan DENTRO del conjunto invisible en vez de ser TODO el conjunto, que "
        "es una afirmacion que no envejece porque la nomina solo crece; la cifra sale con su "
        "corte por banco `9.21`, con el tamano de nomina y el `HEAD` al lado; y el arnes "
        "entero tiene que seguir mordiendo, o sea que todos sus casos CAEN al mutar su "
        "esperado. La prueba vive en `docs/loop/SALIDA_V184_T1B_ARNES_REPARADO.txt`."),
}


def armar_entrada(numero, titulo, claves, titulos, l_sin_num, l_aud, l_eje,
                  l_declara, inicio, fin, viejas_adj, viejas_eje, viejas_aud, salto):
    faltan, bajo, alto = salto
    p = []
    p.append("## R.%d. %s" % (numero, titulo))
    p.append("")
    p.append("(Acta del auditor, vuelta %d, secciones 2, 5, 6, 7 y 9; escrito en la"
             % VUELTA_DEL_ACTA)
    p.append("vuelta %d, TAREA 1.a.)" % VUELTA_QUE_ESCRIBE)
    p.append("")
    p.append("Por adicion, como `R.21` a `R.45`. **Corte de todas las cifras de esta")
    p.append("entrada: 6 sep 2026.** El numero de esta entrada NO esta tecleado: lo computa")
    p.append("`scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS sedes.")
    p.append("La SEDE tampoco se supone: sale de la adjudicacion 6.3 del acta 162, que es")
    p.append("la que citan los `R.30` a `R.45`. Salida:")
    p.append("`docs/loop/SALIDA_V%s_T1A_REGISTRO_R%d.txt`."
             % (SUFIJO_QUE_ESCRIBE, numero))
    p.append("")
    p.append("**ESTA ENTRADA SE ESCRIBE CON LA TAREA 1 EN CURSO Y LA TAREA 2 SIN CORRER,")
    p.append("ASI QUE SUS GLOSAS NO AFIRMAN EN PASADO LO QUE TODAVIA NO HA PASADO.** Es la")
    p.append("forma que la `6.4` del acta 172 adjudico como correcta: donde una glosa dice")
    p.append("EJECUTADA, la prueba va nombrada con su fichero de salida; donde dice que va")
    p.append("a ejecutarse, se dice que **todavia no ha corrido** y no se disfraza.")
    p.append("")
    p.append("**Y LOS CUATRO NUMERALES DEL TITULO TAMPOCO ESTAN TECLEADOS:** se cuentan del")
    p.append("acta acotada (lineas %d a %d) y de ahi sale el numeral en palabra, incluida"
             % (inicio, fin))
    p.append("la concordancia. **%d adjudicaciones numeradas (`5.1` a `5.%d`, todas en la"
             % (len(claves), len(claves)))
    p.append("seccion 5), %d adjudicacion sin numeral (la del punto 6), %d caidas propias"
             % (len(l_sin_num), len(l_aud)))
    p.append("del auditor y %d caida del ejecutor (`E.n`).**" % len(l_eje))
    p.append("")
    p.append("**LA ADJUDICACION DEL PUNTO 6 SE CUENTA APARTE, Y ESA ES LA NOVEDAD DE ESTE")
    p.append("REGISTRO.** No lleva numeral `5.n`: vive en una cabecera de seccion propia")
    p.append("(`docs/loop/ACTA_AUDITOR.md:%s`). **Un contador que solo barra `5.n` la"
             % (", ".join(str(x) for x in l_sin_num) or "(ninguna)"))
    p.append("pierde**, y perder una adjudicacion en el registro es justo la especie que")
    p.append("esta serie existe para impedir. Es ademas **la unica del acta que manda tocar")
    p.append("codigo**: las siete numeradas son concesiones al ejecutor.")
    p.append("")
    p.append("**EL ACTA 184 ESCRIBE SUS NUMERALES ENTRE COMILLAS INVERSAS Y LA 183 NO.**")
    p.append("Corrido sobre esta acta el patron importado, que pide ``**5.1 `` con espacio")
    p.append("detras, da **%d**. Se anade un patron nuevo, `claves_entrecomilladas`, y el"
             % viejas_adj)
    p.append("viejo se conserva intacto: **se anaden patrones, no se ensancha el viejo hasta")
    p.append("que trague**, que es la doctrina que el propio acta adjudico a favor en su")
    p.append("`5.3`.")
    p.append("")
    p.append("**Y LA CAIDA DEL EJECUTOR VUELVE A LA FORMA DEL ACTA 182.** El acta 183 la")
    p.append("escribia dentro del titulo de su primera adjudicacion; **el acta 184 la")
    p.append("escribe otra vez como ``**`E.1`, ...`` al principio de linea**, en su seccion")
    p.append("7. El patron del acta 183, corrido sobre esta, cuenta **%d**. Las dos cifras"
             % viejas_eje)
    p.append("se publican y ninguna se resuelve copiando.")
    p.append("")
    p.append("**LAS CAIDAS PROPIAS DEL AUDITOR SON CERO, Y EL CERO VA CON SU DECLARACION")
    p.append("AL LADO.** El patron de negrita de frase cuenta **%d** sobre esta acta y el"
             % len(l_aud))
    p.append("patron de linea cuenta **%d**, y un cero que sale de un patron que no muerde"
             % viejas_aud)
    p.append("no es evidencia de nada. Lo que lo sostiene es que **el acta lo declara con")
    p.append("todas las letras**, en la linea **%s**: *\"NINGUNA CAIDA PROPIA ESTA VUELTA,"
             % (", ".join(str(x) for x in l_declara) or "(ninguna)"))
    p.append("Y LO DECLARO CON TODAS LAS LETRAS EN VEZ DE DEJAR QUE UN PATRON QUE NO MUERDE")
    p.append("LO DIGA POR MI\"*. **Si el patron diera cero y el acta no lo declarara, el")
    p.append("instrumento haria PARADA en vez de escribir esta entrada.**")
    p.append("")
    p.append("**LAS %s ADJUDICACIONES, CON SU LINEA EN EL ACTA LEIDA HOY.** El titulo de"
             % PALABRA_CON_CERO[len(claves) + len(l_sin_num)].upper())
    p.append("cada una es LITERAL del fichero; la glosa que sigue es prosa del ejecutor y")
    p.append("va marcada como tal.")
    p.append("")
    for clave, _n in claves:
        ln, tit = titulos[clave]
        p.append("  - **`%s` (`docs/loop/ACTA_AUDITOR.md:%d`, leida hoy). VIA: %s.** Titulo"
                 % (clave, ln, VIA[clave]))
        p.append("    literal del acta: *\"%s\"*" % tit)
        p.append("    **QUE HACE ESTA VUELTA CON ELLA (glosa del ejecutor, no del acta):** %s"
                 % QUE_HACE_ESTA_VUELTA[clave])
    if CLAVE_SIN_NUMERAL in titulos:
        ln, tit = titulos[CLAVE_SIN_NUMERAL]
        p.append("  - **LA DEL %s, SIN NUMERAL (`docs/loop/ACTA_AUDITOR.md:%d`, leida hoy)."
                 % (CLAVE_SIN_NUMERAL.upper(), ln))
        p.append("    VIA: %s.** Titulo literal del acta: *\"%s\"*"
                 % (VIA[CLAVE_SIN_NUMERAL], tit))
        p.append("    **QUE HACE ESTA VUELTA CON ELLA (glosa del ejecutor, no del acta):** %s"
                 % QUE_HACE_ESTA_VUELTA[CLAVE_SIN_NUMERAL])
    p.append("")
    p.append("**LA CAIDA DEL EJECUTOR, EN LA LINEA %s, Y NO ACUMULA.**"
             % ", ".join(str(x) for x in l_eje))
    p.append("El `E.1` es **LA ESTIMACION DEL `--plan` PUBLICADA SIN SU CORTE Y YA VENCIDA")
    p.append("DENTRO DE SU PROPIA VUELTA**: el reporte de la 183 publico dos veces `36,6 y")
    p.append("47,7` minutos como estimacion de hoy cuando la nomina ya era de `112` y el")
    p.append("`--plan` de hoy dice `37,0 y 48,2`. **El acta declara que NO acumula**, por la")
    p.append("decision del 27 ago 2026, porque las dos cifras viven en **prosa de")
    p.append("acompanamiento** y no en tabla, cabecera o conclusion; **la racha de reporte")
    p.append("se queda en 2** y tres seguidas que acumulen serian PARADA. **Y el remedio no")
    p.append("es una advertencia:** el acta lo encarga en codigo, y esta vuelta lo pone en")
    p.append("la TAREA 1.c, con la estimacion saliendo con su corte pegado en la misma")
    p.append("linea y un arnes propio que CAE si sale sin el.")
    p.append("")
    p.append("**LA DEUDA DE LA SERIE, QUE SIGUE DOCUMENTADA COMO SALTO Y SIN RELLENAR.**")
    p.append("Se vuelve a medir en esta vuelta en vez de heredarse del `R.45`:")
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
    p.append("**LO QUE ESTA ENTRADA NO REGISTRA, DICHO PARA QUE NO SE BUSQUE:** la `PD.1`")
    p.append("de las cinco `D` con el diferenciador ya presente el dia del veredicto sigue")
    p.append("**registrada y sin resolver**; el instrumento de vigencia de las ocho `A`")
    p.append("rancias por `P.5` **sigue sin cablear**, porque su adjudicacion lo manda a la")
    p.append("primera vuelta de trabajo y esta sigue siendo **vuelta de bateria**; y el")
    p.append("TRAMO 1 de la cola post fusion, el par **2.464**, **no se relee aqui**.")
    return NL.join(p) + NL


def _acta_fabricada(n_adj, caidas_aud, caidas_eje, declara_cero=True,
                    con_punto_6=True):
    """UN ACTA DE MENTIRA para el caso positivo por mutacion. NO toca el repo.

    Escribe los numerales ENTRE COMILLAS INVERSAS, que es la forma del acta 184,
    la caida del ejecutor al principio de linea, que es la forma del acta 182, y
    la adjudicacion del punto 6 como cabecera de seccion. Las tres cosas son
    exactamente las que este fichero existe para cubrir."""
    L = ["# ACTA DEL AUDITOR, VUELTA %d (fabricada)" % VUELTA_DEL_ACTA, ""]
    if declara_cero and caidas_aud == 0:
        L += ["**%s ESTA VUELTA, Y LO DECLARO.** Y su cuerpo."
              % FRASE_SIN_CAIDA_PROPIA, ""]
    for k in range(1, caidas_aud + 1):
        L += ["**`C.%d`, LA CAIDA PROPIA DE MENTIRA EN NEGRITA.** Y su cuerpo." % k, ""]
    L += ["## 5. LAS ADJUDICACIONES", ""]
    for k in range(1, n_adj + 1):
        L += ["**`5.%d` UN TITULO DE MENTIRA NUMERO %d.** Y su cuerpo." % (k, k), ""]
    if con_punto_6:
        L += ["## 6. LA ADJUDICACION QUE EL EJECUTOR TRAJO SIN RESOLVER, DE MENTIRA", ""]
    L += ["## 7. LAS CAIDAS DEL EJECUTOR", ""]
    for k in range(1, caidas_eje + 1):
        L += ["**`E.%d`, UNA CAIDA DE MENTIRA.** Y su cuerpo." % k, ""]
    return NL.join(L) + NL


def prueba_de_mutacion():
    """EL CASO POSITIVO POR MUTACION, SOBRE VARIABLE COMPUTADA Y NO SOBRE
    CONSTANTE LITERAL (`EJECUTOR.md` 1, EL CASO ROJO SE PRUEBA POR MUTACION).

    Se fabrica un acta con OTRAS cifras, se corre el contador de verdad sobre
    ella, y se exige que las cifras y el titulo CAMBIEN con ella. Despues se muta
    el valor esperado y se comprueba que el caso CAE: si no cayera, el caso no
    probaria nada."""
    sys.stdout.reconfigure(encoding="utf-8")
    salida = []
    w = salida.append
    w("CASO POSITIVO POR MUTACION de vuelta184_tarea1a_registrar_acta184.py")
    w("")
    fallos = 0
    casos = [(7, 0, 1), (1, 1, 1), (12, 3, 2), (4, 0, 0)]
    for n_adj, n_aud, n_eje in casos:
        texto = _acta_fabricada(n_adj, n_aud, n_eje)
        lineas, rango, err = cuerpo_del_acta(texto)
        if err:
            w("   %r -> %s" % ((n_adj, n_aud, n_eje), err))
            fallos += 1
            continue
        ini, fin = rango
        cl = claves_entrecomilladas(lineas, ini, fin, PREFIJO_ADJ)
        sn = lineas_de_la_adjudicacion_sin_numeral(lineas, ini, fin)
        aud = cuenta_por_patron(lineas, ini, fin, PAT_CAIDA_AUDITOR)
        eje = cuenta_por_patron(lineas, ini, fin, PAT_CAIDA_EJECUTOR)
        ok = (len(cl) == n_adj and len(aud) == n_aud and len(eje) == n_eje
              and len(sn) == 1)
        titulo = titulo_de_la_entrada(len(cl), len(sn), len(aud), len(eje))
        w("   acta fabricada con adj=%d aud=%d eje=%d" % (n_adj, n_aud, n_eje))
        w("      los contadores dicen adj=%d sin_numeral=%d aud=%d eje=%d -> %s"
          % (len(cl), len(sn), len(aud), len(eje), "CALZA" if ok else "NO CALZA"))
        w("      titulo computado: %s" % titulo)
        if not ok:
            fallos += 1
    w("")
    w("LA MUTACION DEL VALOR ESPERADO, QUE ES LO QUE PRUEBA QUE EL CASO PUEDE CAER:")
    texto = _acta_fabricada(7, 0, 1)
    lineas, (ini, fin), _e = cuerpo_del_acta(texto)
    medido = len(claves_entrecomilladas(lineas, ini, fin, PREFIJO_ADJ))
    esperado_bueno = 7
    esperado_mutado = 8
    w("   medido sobre el acta fabricada (variable computada): %d" % medido)
    w("   con el esperado BUENO   (%d): %s"
      % (esperado_bueno, "PASA" if medido == esperado_bueno else "CAE"))
    w("   con el esperado MUTADO  (%d): %s"
      % (esperado_mutado, "PASA" if medido == esperado_mutado else "CAE"))
    cae_al_mutar = medido != esperado_mutado
    w("   EL CASO CAE AL MUTAR EL ESPERADO: %s" % ("SI" if cae_al_mutar else "NO"))
    if not cae_al_mutar:
        fallos += 1
    w("")
    w("LA SEGUNDA MUTACION: EL PATRON SIN COMILLAS, EL DEL ACTA 183. Sobre un acta")
    w("que numera ``**`5.n` `` tiene que dar CERO, que es el motivo de este fichero.")
    con_viejo = len(claves_de_adjudicacion(lineas, ini, fin, PREFIJO_ADJ))
    w("   patron sin comillas sobre acta en forma 184 -> %d adjudicaciones" % con_viejo)
    w("   EL CASO CAE CON EL PATRON VIEJO: %s" % ("SI" if con_viejo == 0 else "NO"))
    if con_viejo != 0:
        fallos += 1
    w("")
    w("LA TERCERA MUTACION: LA ADJUDICACION DEL PUNTO 6, QUITADA DEL ACTA. El")
    w("contador tiene que decir CERO y el titulo tiene que CAMBIAR con el, o el")
    w("cuarto numeral no estaria contando nada.")
    sin6 = _acta_fabricada(7, 0, 1, con_punto_6=False)
    l6, (i6, f6), _z = cuerpo_del_acta(sin6)
    n6 = len(lineas_de_la_adjudicacion_sin_numeral(l6, i6, f6))
    t_con = titulo_de_la_entrada(7, 1, 0, 1)
    t_sin = titulo_de_la_entrada(7, 0, 0, 1)
    w("   acta SIN el punto 6 -> %d adjudicacion(es) sin numeral" % n6)
    w("   titulo con el punto 6: %s" % t_con)
    w("   titulo sin el punto 6: %s" % t_sin)
    ok6 = (n6 == 0 and t_con != t_sin
           and "la adjudicacion del punto 6" in t_con
           and "la adjudicacion del punto 6" not in t_sin)
    w("   EL CUARTO NUMERAL CUENTA DE VERDAD: %s" % ("SI" if ok6 else "NO"))
    if not ok6:
        fallos += 1
    w("")
    w("LA CUARTA MUTACION: EL PATRON DE CAIDA DEL EJECUTOR DEL ACTA 183. Sobre un")
    w("acta que la escribe al principio de linea tiene que dar CERO.")
    eje_viejo = len(cuenta_por_patron(lineas, ini, fin,
                                      PAT_CAIDA_EJECUTOR_EN_TITULO_VIEJO))
    w("   patron del acta 183 sobre acta en forma 184 -> %d caidas" % eje_viejo)
    w("   EL CASO CAE CON EL PATRON DE LA 183: %s" % ("SI" if eje_viejo == 0 else "NO"))
    if eje_viejo != 0:
        fallos += 1
    w("")
    w("LA QUINTA MUTACION: EL CERO DE CAIDAS PROPIAS CON Y SIN SU DECLARACION. Es")
    w("la diferencia entre un cero medido y un cero que nadie sostiene.")
    con_decl = _acta_fabricada(3, 0, 1, declara_cero=True)
    sin_decl = _acta_fabricada(3, 0, 1, declara_cero=False)
    l1, (i1, f1), _x = cuerpo_del_acta(con_decl)
    l2, (i2, f2), _y = cuerpo_del_acta(sin_decl)
    d1 = lineas_que_declaran_cero_caidas(l1, i1, f1)
    d2 = lineas_que_declaran_cero_caidas(l2, i2, f2)
    w("   acta que DECLARA el cero -> %d linea(s) de declaracion, lineas %s"
      % (len(d1), d1))
    w("   acta que NO lo declara   -> %d linea(s) de declaracion" % len(d2))
    ok_decl = (len(d1) == 1 and len(d2) == 0)
    w("   EL INSTRUMENTO DISTINGUE LOS DOS CEROS: %s" % ("SI" if ok_decl else "NO"))
    if not ok_decl:
        fallos += 1
    w("")
    w("LA SEXTA MUTACION: EL SALTO. actas_sin_entrada() es PURA y se importa del")
    w("registrador de la 183; se le pasa una serie fabricada y se comprueba que el")
    w("salto y sus DOS extremos salen de los titulos y no de ninguna constante.")
    serie_falsa = [
        (10, "docs/PENDIENTES.md", 1, "## R.10. Registro del acta de la vuelta 100"),
        (11, "docs/PENDIENTES.md", 2, "## R.11. Registro del acta de la vuelta 101"),
        (12, "docs/PENDIENTES.md", 3, "## R.12. Registro del acta de la vuelta 105"),
    ]
    faltan, bajo, alto = actas_sin_entrada(serie_falsa, 100, 105)
    w("   serie fabricada: cubre las vueltas 100, 101 y 105")
    w("   faltan (computado): %s" % faltan)
    w("   extremo bajo (computado): %s | extremo alto (computado): %s" % (bajo, alto))
    ok_salto = (faltan == [102, 103, 104] and bajo == (11, 101) and alto == (12, 105))
    w("   EL SALTO Y SUS EXTREMOS CALZAN: %s" % ("SI" if ok_salto else "NO"))
    if not ok_salto:
        fallos += 1
    w("")
    w("LA SEPTIMA MUTACION: EL NUMERAL CERO EN EL TITULO Y SU CONCORDANCIA.")
    t0 = titulo_de_la_entrada(7, 1, 0, 1)
    w("   titulo con cero caidas propias: %s" % t0)
    ok_cero = ("las cero caidas propias del auditor" in t0
               and "la caida del ejecutor" in t0
               and "las siete adjudicaciones numeradas" in t0)
    w("   DICE EL CERO Y CONCUERDA: %s" % ("SI" if ok_cero else "NO"))
    if not ok_cero:
        fallos += 1
    t1 = titulo_de_la_entrada(7, 1, 2, 1)
    w("   y con dos, para que se vea que la concordancia no esta clavada: %s" % t1)
    if "las dos caidas propias del auditor" not in t1:
        fallos += 1
    w("")
    w("CIFRA fallos: %d" % fallos)
    w("VEREDICTO: %s" % ("VERDE" if fallos == 0 else "ROJO"))
    t = NL.join(salida) + NL
    ruta = os.path.join(LOOP, "SALIDA_V%s_T1A_MUTACION_REGISTRO_184.txt"
                        % SUFIJO_QUE_ESCRIBE)
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0 if fallos == 0 else 1


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

    w("B) LAS ADJUDICACIONES NUMERADAS, CONTADAS Y NO TECLEADAS")
    claves = claves_entrecomilladas(lineas, inicio, fin, PREFIJO_ADJ)
    w("   prefijo de esta acta: %r, con el numeral ENTRE COMILLAS INVERSAS"
      % PREFIJO_ADJ)
    w("   CIFRA adjudicaciones numeradas halladas: %d" % len(claves))
    for clave, cuantas in claves:
        w("      %s -> %d aparicion(es)" % (clave, cuantas))
    viejas_adj = claves_de_adjudicacion(lineas, inicio, fin, PREFIJO_ADJ)
    w("   EL CONTRASTE QUE PRUEBA QUE HACIA FALTA UN PATRON NUEVO:")
    w("      el patron SIN comillas, el del acta 183 -> %d sobre esta acta"
      % len(viejas_adj))
    w("      (se anade un patron, NO se ensancha el viejo hasta que trague)")
    dobles = [c for c, n in claves if n != 1]
    if dobles:
        w("   PARADA: hay claves repetidas dentro del acta: %s" % ", ".join(dobles))
        print(NL.join(salida))
        return 1
    w("")

    w("C) LA ADJUDICACION SIN NUMERAL, LA DEL PUNTO 6, CONTADA APARTE")
    l_sin_num = lineas_de_la_adjudicacion_sin_numeral(lineas, inicio, fin)
    w("   CIFRA adjudicaciones sin numeral: %d, en las lineas %s"
      % (len(l_sin_num), ", ".join(str(x) for x in l_sin_num) or "(ninguna)"))
    for i in l_sin_num:
        w("      LINEA %d: %s" % (i, lineas[i - 1].strip()[:130]))
    if len(l_sin_num) != 1:
        w("   PARADA: el acta 184 trae UNA adjudicacion sin numeral y el contador")
        w("   dice %d. No se escribe una entrada con una cuenta que no calza."
          % len(l_sin_num))
        print(NL.join(salida))
        return 1
    if len(claves) + len(l_sin_num) != len(VIA):
        w("   PARADA: el acta trae %d adjudicaciones y las glosas cubren %d."
          % (len(claves) + len(l_sin_num), len(VIA)))
        print(NL.join(salida))
        return 1
    w("")

    w("D) LAS CAIDAS, POR SUS FAMILIAS, Y LOS PATRONES DE LA 183 AL LADO")
    l_aud = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_AUDITOR_PROSA)
    l_aud_v = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_AUDITOR)
    l_eje = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_EJECUTOR)
    l_eje_v = cuenta_por_patron(lineas, inicio, fin,
                                PAT_CAIDA_EJECUTOR_EN_TITULO_VIEJO)
    l_declara = lineas_que_declaran_cero_caidas(lineas, inicio, fin)
    w("   CAIDAS DEL EJECUTOR (patron de linea, el del acta 182 y el 184): %d, lineas %s"
      % (len(l_eje), ", ".join(str(x) for x in l_eje) or "(ninguna)"))
    for i in l_eje:
        w("      LINEA %d: %s" % (i, lineas[i - 1].strip()[:130]))
    w("   EL PATRON DEL ACTA 183 (dentro del titulo de una adjudicacion): %d"
      % len(l_eje_v))
    w("   CAIDAS PROPIAS DEL AUDITOR (patron de negrita de frase): %d" % len(l_aud))
    w("   EL PATRON DE LINEA: %d" % len(l_aud_v))
    w("   LINEAS DONDE EL ACTA DECLARA QUE NO TUVO NINGUNA: %s"
      % (", ".join(str(x) for x in l_declara) or "(ninguna)"))
    for i in l_declara:
        w("      LINEA %d: %s" % (i, lineas[i - 1].strip()[:130]))
    if not l_eje:
        w("   PARADA: el patron de caida del ejecutor no encuentra ninguna.")
        print(NL.join(salida))
        return 1
    if not l_aud and not l_declara:
        w("   PARADA: cero caidas propias del auditor Y el acta no lo declara.")
        w("   Un cero de un patron que no muerde no se publica como medicion.")
        print(NL.join(salida))
        return 1
    w("")

    w("E) EL TITULO, CON SUS CUATRO NUMERALES COMPUTADOS")
    titulo = titulo_de_la_entrada(len(claves), len(l_sin_num), len(l_aud), len(l_eje))
    w("   %s" % titulo)
    w("")

    w("F) LOS TITULOS LITERALES DE CADA ADJUDICACION, LEIDOS DEL ACTA")
    titulos = {}
    for clave, _n in claves:
        pat = re.compile(r"^\s*\*\*`%s` " % re.escape(clave))
        res, err2 = titulo_de_la_negrita(lineas, inicio, fin, pat, clave)
        if err2:
            w("   %s -> %s" % (clave, err2))
            print(NL.join(salida))
            return 1
        titulos[clave] = res
        w("   %s (linea %d): %s" % (clave, res[0], res[1][:130]))
    ln6 = l_sin_num[0]
    titulos[CLAVE_SIN_NUMERAL] = (ln6, lineas[ln6 - 1].lstrip("# ").strip())
    w("   %s (linea %d): %s"
      % (CLAVE_SIN_NUMERAL, ln6, titulos[CLAVE_SIN_NUMERAL][1][:130]))
    w("")

    w("G) EL NUMERO DE LA ENTRADA, QUE NO SE TECLEA")
    halladas = SERIE.entradas()
    numero = SERIE.siguiente_libre(halladas)
    w("   serie recomputada de sus dos sedes: %d entradas" % len(halladas))
    w("   CIFRA colisiones: %d | CIFRA huecos: %d"
      % (len(SERIE.colisiones(halladas)), len(SERIE.huecos(halladas))))
    w("   SIGUIENTE LIBRE: R.%d" % numero)
    w("")

    w("H) LA DEUDA DE LA SERIE, REMEDIDA EN ESTA VUELTA Y NO HEREDADA DEL R.45")
    salto = actas_sin_entrada(halladas, 173, VUELTA_DEL_ACTA - 1)
    faltan, bajo, alto = salto
    w("   tramo mirado: actas 173 a %d" % (VUELTA_DEL_ACTA - 1))
    w("   CIFRA actas SIN entrada propia en la serie: %d" % len(faltan))
    w("   LAS QUE FALTAN: %s" % (", ".join(str(x) for x in faltan) or "(ninguna)"))
    w("   EXTREMO BAJO (ultimo registro que cubre un acta anterior al salto): %s"
      % ("R.%d cubre el acta %d" % bajo if bajo else "(ninguno)"))
    w("   EXTREMO ALTO (primer registro que cubre un acta posterior): %s"
      % ("R.%d cubre el acta %d" % alto if alto else "(ninguno)"))
    w("")

    marca = "## R.%d." % numero
    texto_sede = io.open(SEDE, encoding="utf-8").read().replace(chr(13) + NL, NL)
    ya = ("## R.%d. %s" % (numero, titulo)) in texto_sede
    w("I) LA IDEMPOTENCIA, COMPROBADA ANTES DE ESCRIBIR")
    w("   la marca %r ya esta en la sede: %s"
      % (marca, "SI" if marca in texto_sede else "NO"))
    w("   la entrada entera ya esta: %s" % ("SI" if ya else "NO"))
    w("")

    entrada = armar_entrada(numero, titulo, claves, titulos, l_sin_num, l_aud,
                            l_eje, l_declara, inicio, fin, len(viejas_adj),
                            len(l_eje_v), len(l_aud_v), salto)
    w("J) LA ENTRADA ARMADA")
    w("   %d bytes | %d lineas" % (len(entrada.encode("utf-8")), entrada.count(NL)))
    w("")

    if a.simular:
        w("K) MODO --simular: NO SE ESCRIBE NADA EN LA SEDE.")
        w("")
        w("LA ENTRADA, ENTERA:")
        for l in entrada.split(NL):
            w("   | " + l)
    elif ya:
        w("K) NO SE ESCRIBE: la entrada ya esta en la sede, byte a byte.")
    else:
        nuevo = texto_sede.rstrip(NL) + NL + NL + entrada
        io.open(SEDE, "w", encoding="utf-8", newline=NL).write(nuevo)
        w("K) ESCRITA EN docs/PENDIENTES.md")
        w("   la sede pasa de %d a %d bytes"
          % (len(texto_sede.encode("utf-8")), len(nuevo.encode("utf-8"))))
        rele = io.open(SEDE, encoding="utf-8").read().replace(chr(13) + NL, NL)
        w("   RELEIDA DEL DISCO: la entrada esta byte a byte: %s"
          % ("SI" if entrada.rstrip(NL) in rele else "NO"))
        w("   guiones largos o medios en la entrada: %d"
          % (entrada.count(chr(8212)) + entrada.count(chr(8211))))
        de_nuevo = SERIE.entradas()
        w("   serie recomputada TRAS escribir: %d entradas, siguiente libre R.%d"
          % (len(de_nuevo), SERIE.siguiente_libre(de_nuevo)))
        w("   CIFRA colisiones tras escribir: %d" % len(SERIE.colisiones(de_nuevo)))
        w("   CIFRA huecos tras escribir: %d" % len(SERIE.huecos(de_nuevo)))

    t = NL.join(salida) + NL
    ruta = os.path.join(LOOP, "SALIDA_V%s_T1A_REGISTRO_R%d.txt"
                        % (SUFIJO_QUE_ESCRIBE, numero))
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
