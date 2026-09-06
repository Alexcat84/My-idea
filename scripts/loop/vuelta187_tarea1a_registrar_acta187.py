# -*- coding: utf-8 -*-
r"""vuelta187_tarea1a_registrar_acta187.py . EL ACTA 187 ENTERA, REGISTRADA EN LA
SERIE `R.N` EN LA FORMA DE LA CASA.

LA MAQUINA NO SE CLONA, SE IMPORTA, y eso lo adjudico la `6.6` del acta 172 como
correcto y obligatorio. De `scripts/loop/vuelta186_tarea1a_registrar_acta186.py`
se importan `PALABRA_CON_CERO`, `parrafo_de`, `cabecera_de_la_seccion`,
`lineas_que_declaran_cero_caidas` y las dos frases del cero; y por su cadena
llegan `titulo_de_la_negrita`, `claves_entrecomilladas`, `cuenta_por_patron`,
`claves_de_adjudicacion` y `actas_sin_entrada`. **Lo unico propio de este fichero
es EL ACOTE DE SU ACTA, LOS DOS PATRONES QUE SU ACTA NECESITA Y SUS GLOSAS.**

POR QUE HACE FALTA CODIGO PROPIO OTRA VEZ, MEDIDO Y NO SUPUESTO, Y SON DOS COSAS
QUE EL REGISTRADOR DE LA 186 NO SABE HACER:

  1) EL `6.2` DEL ACTA 187 NO ES UN PENDIENTE, NO ES UNA ANOTACION Y NO ESTA
     CERRADO: ES UNA **CORRECCION POR DECLARACION**, Y ES UN ESTADO NUEVO. El
     acta escribe *"LA `PD.7` DEL REPORTE NO ES UN PENDIENTE DE DOCTRINA, Y LO
     CORRIJO SIN CASTIGARLO"* y en su cuerpo *"Se corrige por declaracion"*. El
     registrador de la 186 sabia leer ABIERTA, CERRADA y ANOTACION, y con este
     titulo habria sacado `SIN DECIR` y habria hecho PARADA. **El cuarto estado
     se anade LEIDO DEL TITULO con la marca literal `NO ES UN PENDIENTE DE
     DOCTRINA`, y los otros tres se conservan intactos.** Y la PARADA se
     conserva entera: **un estado que el registrador no sabe leer sigue siendo
     PARADA**, y no se mete en el saco de los abiertos ni en el de los cerrados.

  2) LA CAIDA DEL EJECUTOR DEL ACTA 187 SE LLAMA `C.1`, Y `C.n` ERA EL PATRON DE
     LAS CAIDAS PROPIAS DEL AUDITOR EN LAS ACTAS 178 A 184. **El mismo patron
     nombra hoy dos familias distintas**, asi que contar por patron a secas
     publicaria UNA caida propia del auditor donde el acta declara CERO. Aqui la
     atribucion **no la hace el patron: la hace LA SECCION EN QUE LA CAIDA VIVE**,
     leyendo la cabecera `## 8.` y mirando si nombra al EJECUTOR o al AUDITOR. Y
     si una `C.n` cayera en una seccion cuya cabecera no nombra a ninguno de los
     dos, **es PARADA**: una caida sin dueno no se reparte a ojo.

LAS CIFRAS DEL TITULO NO SE TECLEAN: se cuentan del acta acotada. Ni el numero de
la entrada: lo devuelve `scripts/loop/serie_de_registros.py` recomputando la serie
de sus DOS sedes. **`R.49` NO se da por bueno porque lo diga el encargo.** Y LA
DEUDA DE LA SERIE SE REMIDE EN ESTA VUELTA y no se hereda del `R.48`.

LOS CINCO PUESTOS DE LA `PD.1` NO SE TECLEAN tampoco: se leen del parrafo del
`6.n` que el propio titulo declara ABIERTO, y si el acta dijera otros, la entrada
diria otros.

LO QUE ESTE FICHERO NO HACE: no toca el acta, no toca el reporte, no toca
`docs/plan/`, no corre la bateria y no escribe ningun veredicto. Escribe UNA
entrada en UNA sede, y si la entrada ya esta, NO la duplica y lo dice.

USO:
  python scripts/loop/vuelta187_tarea1a_registrar_acta187.py
  python scripts/loop/vuelta187_tarea1a_registrar_acta187.py --simular
  python scripts/loop/vuelta187_tarea1a_registrar_acta187.py --mutacion
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

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")
SEDE = os.path.join(RAIZ, "docs", "PENDIENTES.md")
NL = chr(10)

VUELTA_DEL_ACTA = 187
VUELTA_QUE_ESCRIBE = 187
SUFIJO_QUE_ESCRIBE = "187"
CABECERA_ACTA = "# ACTA DEL AUDITOR, VUELTA %d" % VUELTA_DEL_ACTA
PREFIJO_ADJ = "5."
PREFIJO_PD = "6."
PREFIJO_PREG = "7."

# EL CUARTO ESTADO, QUE NACE EN ESTA VUELTA. La marca es literal del titulo del
# `6.2` del acta 187 y NO una parafrasis.
MARCA_CORRECCION = "NO ES UN PENDIENTE DE DOCTRINA"

# EL PATRON DE LA CAIDA `C.n` EN NEGRITA AL PRINCIPIO DE LINEA. Es el mismo que
# las actas 178 a 184 usaban para LAS CAIDAS PROPIAS DEL AUDITOR, y el acta 187
# lo usa para LA CAIDA DEL EJECUTOR. Por eso aqui NO decide la familia: la
# decide la seccion, en `caidas_c_por_seccion()`.
PAT_CAIDA_C = re.compile(r"^\s*(?:-\s+)?\*\*`?C\.(\d+)`?[,.]")
# LAS DOS PALABRAS CON LAS QUE UNA CABECERA DE SECCION DECLARA DE QUIEN ES LA
# CAIDA QUE ESA SECCION TRATA.
DUENO_EJECUTOR = "EJECUTOR"
DUENO_AUDITOR = "MI CAIDA"


def cuerpo_del_acta(texto=None):
    """EL ACTA ACOTADA: (lineas, (inicio, fin), error). El fin es el final del
    fichero porque el acta 187 es la ultima escrita; si algun dia dejara de
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


def seccion_que_contiene(lineas, inicio, fin, linea):
    """LA CABECERA `## ...` MAS CERCANA POR ENCIMA DE UNA LINEA, DENTRO DEL ACTA
    ACOTADA. Devuelve (linea_de_la_cabecera, texto), o (None, "") si la linea no
    vive debajo de ninguna. PURA.

    Existe porque la atribucion de una caida `C.n` no la puede hacer su patron:
    el mismo patron nombro caidas del AUDITOR en las actas 178 a 184 y nombra la
    del EJECUTOR en el acta 187."""
    cab = None
    for i in range(inicio, min(linea, fin) + 1):
        if lineas[i - 1].startswith("## "):
            cab = i
    return (cab, lineas[cab - 1].strip()) if cab else (None, "")


def caidas_c_por_seccion(lineas, inicio, fin):
    """LAS CAIDAS `C.n` DEL ACTA, REPARTIDAS POR EL DUENO QUE DECLARA LA CABECERA
    DE SU SECCION. Devuelve (del_ejecutor, del_auditor, sin_dueno), tres listas
    de (linea, numero, cabecera). PURA.

    LA ATRIBUCION NO SE TECLEA Y NO SE SUPONE: sale de mirar si la cabecera de la
    seccion en que la caida vive nombra al `EJECUTOR` o dice `MI CAIDA`. Una
    `C.n` cuya seccion no diga ni una cosa ni la otra sale en `sin_dueno`, y
    quien llama hace PARADA. **Repartir a ojo una caida sin dueno es exactamente
    lo que esta funcion existe para impedir.**"""
    eje, aud, huerfanas = [], [], []
    for i in range(inicio, fin + 1):
        m = PAT_CAIDA_C.match(lineas[i - 1])
        if not m:
            continue
        _ln, cab = seccion_que_contiene(lineas, inicio, fin, i)
        fila = (i, int(m.group(1)), cab)
        if DUENO_EJECUTOR in cab.upper():
            eje.append(fila)
        elif DUENO_AUDITOR in cab.upper():
            aud.append(fila)
        else:
            huerfanas.append(fila)
    return eje, aud, huerfanas


def pendientes_de_doctrina(lineas, inicio, fin, titulos):
    """LOS `6.n` DE LA SECCION 6, CON SU ESTADO LEIDO DEL TITULO. Devuelve
    [(clave, pd, estado, linea, titulo)]. PURA.

    EL ESTADO NO SE TECLEA: sale de buscar en el titulo literal, EN ESTE ORDEN,
    `NO ES UN PENDIENTE DE DOCTRINA` (CORRECCION POR DECLARACION), `NO LO
    CONVIERTO EN UNO` (ANOTACION), `SIGUE ABIERTA` (ABIERTA) o `ADJUDICAD`
    (CERRADA). **Si un titulo no dijera ninguna de las cuatro, el estado sale
    como `SIN DECIR` y el instrumento hace PARADA en vez de suponer.**

    EL CUARTO ESTADO NACE EN LA VUELTA 187 Y NO ES UN ENSANCHE: el `6.2` del acta
    187 no cierra un pendiente, no lo deja abierto y no es la anotacion de un
    trabajo ajeno. **Es una correccion de especie sobre una numeracion que el
    reporte de la 186 puso mal**, y el acta lo dice con estas palabras: *"Se
    corrige por declaracion (...) y el numero `PD.7` queda libre"*. Meterlo en el
    saco de los cerrados diria que un pendiente se resolvio, y meterlo en el de
    los abiertos diria que hay uno pendiente. **Las dos serian cifras falsas.**"""
    salida = []
    for clave, _n in claves_entrecomilladas(lineas, inicio, fin, PREFIJO_PD):
        ln, tit = titulos[clave]
        m = PAT_PD_DEL_TITULO.search(tit)
        pd = ("PD.%s" % m.group(1)) if m else "(sin PD en el titulo)"
        if MARCA_CORRECCION in tit:
            estado = "CORRECCION POR DECLARACION"
        elif MARCA_ANOTACION in tit:
            estado = "ANOTACION"
        elif MARCA_ABIERTA in tit:
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
    PURA. Identica en forma a la de la 186: el estado sale de `LAS CONTESTO` en
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
    PURA. Devuelve la lista de enteros, vacia si no los encuentra."""
    for clave, pd, estado, ln, _tit in pendientes_de_doctrina(
            lineas, inicio, fin, titulos):
        if estado != "ABIERTA":
            continue
        parrafo = parrafo_de(lineas, ln, fin)
        m = re.search(r"\(\*\*([0-9,\sy]+)\*\*\)", parrafo)
        if not m:
            m = re.search(r"\bson\s+\*\*([0-9,\sy]+)\*\*", parrafo)
        if not m:
            return []
        return [int(x) for x in re.findall(r"\d+", m.group(1))]
    return []


def titulo_de_la_entrada(n_adj, n_pd, n_preg, n_cai_aud, n_cai_rep):
    """El titulo, con sus CINCO numerales COMPUTADOS y no tecleados, y con la
    concordancia dentro del computo. El CERO entra por `PALABRA_CON_CERO`
    importado, y va en plural porque en castellano el cero es plural.

    LA CIFRA DE LA SECCION 6 QUE ENTRA AQUI ES LA DE SUS `6.n`, que en el acta
    187 son dos aunque uno de ellos sea una CORRECCION POR DECLARACION. El
    reparto por estado va dentro de la entrada, con su nombre."""
    def trozo(n, sing, plur):
        if n == 1:
            return "la %s" % sing
        return "las %s %s" % (PALABRA_CON_CERO[n], plur)

    def trozo_m(n, sing, plur):
        if n == 1:
            return "el %s" % sing
        return "los %s %s" % (PALABRA_CON_CERO[n], plur)
    return ("Registro de %s, %s, %s, %s del auditor y %s de reporte del "
            "ejecutor del acta de la vuelta %d"
            % (trozo(n_adj, "adjudicacion numerada", "adjudicaciones numeradas"),
               trozo_m(n_pd, "numeral de la seccion 6",
                       "numerales de la seccion 6"),
               trozo(n_preg, "pregunta contestada", "preguntas contestadas"),
               trozo(n_cai_aud, "caida propia", "caidas propias"),
               trozo(n_cai_rep, "caida", "caidas"),
               VUELTA_DEL_ACTA))


VIA = {
    "5.1": "SIN TOCAR NADA",
    "5.2": "SIN TOCAR NADA",
    "5.3": "SIN TOCAR NADA",
    "5.4": "SIN TOCAR NADA",
    "5.5": "SIN TOCAR NADA",
    "5.6": "EJECUTADA",
    "6.1": "SIN TOCAR NADA",
    "6.2": "SIN TOCAR NADA",
    "7.1": "SIN TOCAR NADA",
    "7.2": "EJECUTADA",
    "7.3": "EJECUTADA",
}

QUE_HACE_ESTA_VUELTA = {
    "5.1": ("SE ACATA SIN TOCAR NADA. El acta confirma que un comentario que NOMBRA la "
            "comparacion no es una segunda sede que decida, y que quitarlo para complacer "
            "a un grep seria empeorar el fichero para mejorar una cifra. No mueve ninguna "
            "celda y no deja trabajo."),
    "5.2": ("SE ACATA SIN TOCAR NADA, Y LA REGLA QUE DEJA ESCRITA MANDA EN ESTA VUELTA. "
            "Que una guarda caiga en rojo cuando le falta su vara no es doctrina nueva: "
            "es el banco 9, fallar ruidoso. Esta vuelta escribe DOS guardas nuevas y las "
            "dos siguen esa letra: la ruta que no existe sigue siendo rojo y el hueco "
            "declarado de la seccion 9 sigue siendo su unica excepcion."),
    "5.3": ("SE ACATA SIN TOCAR NADA. `es_cierre_tardio()` se queda como esta: "
            "estrecharlo habria sido doctrina nueva metida dentro de una guarda, y el "
            "acta mide que abrirlo de mas no puede aflojar nada porque "
            "`piezas_que_faltan()` ni siquiera tiene parametro de carril. **La TAREA 5.b "
            "de esta vuelta se apoya en ese carril tal como esta y no lo toca.**"),
    "5.4": ("SE ACATA SIN TOCAR NADA. El archivado forzado del reporte de la 184 queda "
            "adjudicado como sustitucion y no como pisada, porque el texto viejo sigue "
            "entero en otra sede y las dos corridas se publicaron. Esta vuelta NO reabre "
            "`REPORTE_V184.md` y su encargo se lo prohibe con esas palabras."),
    "5.5": ("SE ACATA SIN TOCAR NADA EN LA CONDUCTA, Y LA CONSECUENCIA QUE EL ACTA MIDE "
            "SE EJECUTA EN LA TAREA 5.b. El acta corrio `seccion4_que_no_calza()` sobre "
            "los ficheros reales del 184 y saco **1 motivo en rojo**: el reporte ya "
            "cerrado no pasa la guarda que su propia vuelta cableo. Lo que esta vuelta "
            "hace con eso no es reescribir el 184, es DECLARAR el defecto por el carril "
            "de cierre tardio."),
    "5.6": ("SE ACATA Y SE EJECUTA EN LA TAREA 3 DE ESTA VUELTA. El acta convierte el "
            "`D.6` en una observacion sobre la clase `B` entera y le pone tres casos "
            "medidos (338, 226, 603) donde el reporte tenia uno. El encargo manda contar "
            "las `B` del universo releido y publicar, PARA CADA UNA, si declara "
            "diferenciador, si tiene lesion exacta y si tiene nodo muerto. **Solo se "
            "cuenta y se publica: no se interpreta y no se adjudica.**"),
    "6.1": ("`PD.1` SIGUE ABIERTA, SEXTA VUELTA, Y ESTA VUELTA NO LA CIERRA NI LA "
            "ENCARGA. El acta la deja registrada con sus cinco puestos y dice con todas "
            "las letras que darles cola seria doctrina nueva, que es del fundador. Sus "
            "cinco nombres van en esta entrada leidos del acta y no copiados del encargo."),
    "6.2": ("NO ES UN PENDIENTE DE DOCTRINA Y NO SE REGISTRA COMO TAL: ES UNA CORRECCION "
            "POR DECLARACION, Y ES UN ESTADO NUEVO EN ESTA SERIE. El reporte de la 186 "
            "numero como `PD.7` una anotacion que el acta 186 dijo expresamente que no "
            "convertia en pendiente. El acta 187 lo corrige sin castigarlo: **la mesa del "
            "`PMF` es TRABAJO DE PLAN con sede en `PENDIENTES.md`, no un pendiente de "
            "doctrina, y el numero `PD.7` queda libre.** Esta vuelta NO abre esa mesa ni "
            "la del 603 ni la de figuras del 226, y su encargo se lo prohibe con esas "
            "palabras."),
    "7.1": ("CONTESTADA POR EL ACTA Y SIN TRABAJO NUEVO: el conteo de la segunda copia se "
            "queda SOLO EN CODIGO y el arnes de la `2.a` de la 186 se queda como esta. "
            "El acta deja escrito por donde se apretaria si algun dia hiciera falta, y "
            "esta vuelta no aprieta ahi."),
    "7.2": ("CONTESTADA POR EL ACTA Y EJECUTADA EN LA TAREA 5.b DE ESTA VUELTA. La "
            "pregunta del ejecutor de la 186 partia de una premisa falsa y el acta la "
            "mide: `docs/loop/SALIDA_V184_APERTURA.txt` existe. El rojo viene de que la "
            "seccion 4 del 184 no AFIRMA la cifra de status. **La `2.d` entra en el "
            "carril de CIERRE TARDIO por la misma puerta que las cifras sin pareja: NO "
            "bloquea, pero se DECLARA dentro del propio reporte cerrado, con su motivo "
            "entero. En el carril normal sigue bloqueando entera, y eso lo exige el "
            "arnes, no la vista.**"),
    "7.3": ("CONTESTADA POR EL ACTA Y EJECUTADA EN LA TAREA 5.a DE ESTA VUELTA, "
            "BLOQUEANTE. `arneses_que_faltan()` devolvia CUATRO al abrir esta vuelta, la "
            "bateria es la 189 y quedan dos vueltas. Entran los cuatro de la 186 MAS los "
            "que nazcan hoy, y la prueba es la funcion devolviendo **0** al cerrar, con "
            "el tamano de la nomina antes y despues. **No se poda nada: la opcion `c` del "
            "5 sep esta RECHAZADA por el fundador.**"),
}


def _cabeza_de_la_entrada(numero, titulo, claves, pds, preguntas, estado_preg, cab7,
                          titulos, l_aud, l_rep, decl_vieja, decl_nueva,
                          inicio, fin, viejas_adj, viejas_eje, c_eje, c_aud):
    """LA PRIMERA MITAD DE LA ENTRADA: la cabecera, los cinco numerales del
    titulo, el reparto de la seccion 6 y las dos familias de caidas con sus
    patrones viejos al lado. PURA: recibe todo lo ya medido."""
    p = []
    p.append("## R.%d. %s" % (numero, titulo))
    p.append("")
    p.append("(Acta del auditor, vuelta %d, secciones 4, 5, 6, 7, 8, 9, 10, 11, 12 y 13;"
             % VUELTA_DEL_ACTA)
    p.append("escrito en la vuelta %d, TAREA 1.a.)" % VUELTA_QUE_ESCRIBE)
    p.append("")
    p.append("Por adicion, como `R.21` a `R.48`. **Corte de todas las cifras de esta")
    p.append("entrada: 6 sep 2026.** El numero de esta entrada NO esta tecleado: lo computa")
    p.append("`scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS sedes,")
    p.append("y `R.49` NO se dio por bueno porque lo dijera el encargo. La SEDE tampoco se")
    p.append("supone: sale de la adjudicacion 6.3 del acta 162, que es la que citan los")
    p.append("`R.30` a `R.48`. Salida:")
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
    p.append("seccion 7 (`7.1` a `7.%d`), %d caidas propias del auditor y %d caida de"
             % (len(preguntas), len(l_aud), len(l_rep)))
    p.append("reporte del ejecutor.**")
    p.append("")
    p.append("**LAS %s ADJUDICACIONES SON A FAVOR, LAS %s.** El acta no regatea ninguna."
             % (PALABRA_CON_CERO[len(claves)].upper(),
                PALABRA_CON_CERO[len(claves)].upper()))
    p.append("")
    p.append("**LA SECCION 6 NO TIENE DOS PENDIENTES: TIENE DOS NUMERALES, Y UNO DE ELLOS")
    p.append("NO ES UN PENDIENTE.** El reparto por estado sale de leer el titulo literal de")
    p.append("cada uno y NO se teclea: **%s**."
             % ("; ".join("%s %s %s" % (c, pd, est) for c, pd, est, _l, _t in pds)))
    p.append("El `6.2` es una **CORRECCION POR DECLARACION**, que es un ESTADO NUEVO en")
    p.append("esta serie y no uno de los tres que ya habia. No cierra un pendiente, no lo")
    p.append("deja abierto y no es la anotacion de un trabajo ajeno: **corrige la especie")
    p.append("de una numeracion que el reporte de la 186 puso mal**, y el acta lo escribe")
    p.append("asi: *\"Se corrige por declaracion: la mesa del `PMF` es TRABAJO DE PLAN con")
    p.append("sede en `PENDIENTES.md`, no un pendiente de doctrina\"*, y **el numero `PD.7`")
    p.append("queda libre**. **La `PD.7` del reporte de la 186 NO es un pendiente de")
    p.append("doctrina, y esta entrada no la cuenta como tal.** Meterla en el saco de los")
    p.append("cerrados diria que un pendiente se resolvio; meterla en el de los abiertos")
    p.append("diria que hay uno pendiente. **Las dos serian cifras falsas.**")
    p.append("")
    p.append("**EL CONTRASTE QUE PRUEBA QUE LOS PATRONES SE MIDEN Y NO SE SUPONEN.** El")
    p.append("patron SIN comillas inversas, el del acta 183, corrido sobre esta acta da")
    p.append("**%d**. Se conserva intacto y su cero se publica: **se anaden patrones, no se"
             % viejas_adj)
    p.append("ensancha el viejo hasta que trague**.")
    p.append("")
    p.append("**CERO CAIDAS PROPIAS DEL AUDITOR, Y EL CERO VA CONTADO Y NO OMITIDO.** El")
    p.append("patron `A.n` de cabecera de tercer nivel, el que el acta 185 estreno, da")
    p.append("**%d** sobre esta acta. **Y AQUI HAY UNA TRAMPA QUE ESTA ENTRADA DESARMA EN"
             % len(l_aud))
    p.append("VEZ DE PISAR:** el patron `C.n` de las actas 178 a 184 nombraba LAS CAIDAS")
    p.append("PROPIAS DEL AUDITOR, y el acta 187 usa `C.1` para LA CAIDA DEL EJECUTOR.")
    p.append("Contar por patron a secas habria publicado **una** caida propia del auditor")
    p.append("donde el acta declara **cero**. **La atribucion no la hace el patron: la hace")
    p.append("LA SECCION EN QUE LA CAIDA VIVE**, y sale de mirar su cabecera. Repartidas")
    p.append("asi: **%d del ejecutor y %d del auditor**." % (len(c_eje), len(c_aud)))
    for ln, num, cab in c_eje:
        p.append("  - `C.%d` en `docs/loop/ACTA_AUDITOR.md:%d`, bajo la cabecera *\"%s\"*,"
                 % (num, ln, cab))
        p.append("    que nombra al **EJECUTOR**.")
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
    p.append("**EL PATRON `R.n`, CON EL QUE EL ACTA 186 NOMBRO SU CAIDA DE REPORTE,")
    p.append("CORRIDO SOBRE ESTA ACTA DA %d, Y EL PATRON `E.n` DE LAS ACTAS 182 Y 184 DA"
             % len(l_rep))
    p.append("%d.** Las tres cifras se publican y ninguna se resuelve copiando." % viejas_eje)
    p.append("")
    return p


def armar_entrada(numero, titulo, claves, pds, preguntas, estado_preg, cab7,
                  titulos, l_aud, l_rep, decl_vieja, decl_nueva, inicio, fin,
                  viejas_adj, viejas_eje, c_eje, c_aud, puestos_pd1, salto):
    """LA ENTRADA ENTERA. PURA: recibe todo lo ya medido y no lee ni escribe."""
    faltan, bajo, alto = salto
    p = _cabeza_de_la_entrada(numero, titulo, claves, pds, preguntas,
                              estado_preg, cab7, titulos, l_aud, l_rep,
                              decl_vieja, decl_nueva, inicio, fin, viejas_adj,
                              viejas_eje, c_eje, c_aud)
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
    p.append("TECLEADO.** El estado sale de buscar `%s`, `%s`, `%s`"
             % (MARCA_CORRECCION, MARCA_ANOTACION, MARCA_ABIERTA))
    p.append("o `%s` en el titulo literal, en ese orden. **Si un titulo no dijera ninguna"
             % MARCA_CERRADA)
    p.append("de las cuatro, el instrumento haria PARADA en vez de meterlo en el saco de")
    p.append("los abiertos o en el de los cerrados.**")
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
    p.append("registrarlas como contestadas. **Las tres eran del ejecutor de la 186 y las")
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
    p.append("el propio titulo declara ABIERTO. **Son %d puestos: %s.** Es la SEXTA"
             % (len(puestos_pd1),
                ", ".join(str(x) for x in puestos_pd1) or "(ninguno)"))
    p.append("vuelta que la `PD.1` sigue abierta, y el acta dice que darles cola seria")
    p.append("doctrina nueva, o sea del fundador.")
    p.append("")
    p.append("**LA CAIDA DEL EJECUTOR `C.1`, EN LA LINEA %s, Y NO ACUMULA.**"
             % (", ".join(str(ln) for ln, _n, _c in c_eje) or "(ninguna)"))
    p.append("Son las cuatro cifras de bytes que el reporte de la 186 publico con la")
    p.append("convencion de LF **supuesta en vez de medida**. **Y EL ACTA 187 LE CORRIGE LA")
    p.append("ESPECIE, AFLOJANDO EN VEZ DE APRETAR:** el reporte de la 186 se acuso a si")
    p.append("mismo de *\"caida de cifra publicada\"* y el acta mide que **no lo es**,")
    p.append("porque las sedes de la cifra publicada son cuatro y `REPORTE.md` no es")
    p.append("ninguna de ellas. **Es caida de REPORTE.** Y no acumula, tambien por la")
    p.append("letra del 27 ago 2026: el acta fue a `git show bb3aaad3` a mirar donde vivia")
    p.append("cada una de las cuatro y **las cuatro viven en lista de rutas o en prosa de")
    p.append("acompanamiento**, no en tabla, cabecera ni conclusion. **La racha de reporte")
    p.append("se mantiene en 2 y la de cifra publicada sigue en 0.** A partir de dos,")
    p.append("`AUDITOR.md` 1.2 es mandatorio: el acta encarga la escalada en codigo y esta")
    p.append("vuelta la ejecuta en la **TAREA 4**.")
    p.append("")
    p.append("**LA DEUDA DE LA SERIE, QUE SIGUE DOCUMENTADA COMO SALTO Y SIN RELLENAR.**")
    p.append("Se vuelve a medir en esta vuelta en vez de heredarse del `R.48`:")
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
    p.append("la **mesa de los tres nodos de la puerta del `PMF`** (puestos 338 y 297), la")
    p.append("del **603** y la de figuras del **226** **no se abren aqui**, y el encargo lo")
    p.append("prohibe con esas palabras: son trabajo de plan de otra vuelta y su sede es")
    p.append("`docs/PENDIENTES.md`. **El numero `PD.7` queda libre y ninguna entrada de")
    p.append("esta serie lo ocupa.**")
    return NL.join(p) + NL


def _acta_fabricada(n_adj, n_pd, n_preg, caidas_aud, caidas_rep,
                    declara_cero=False, puestos=(11, 22, 33),
                    contesta=True, con_correccion=True, dueno_ejecutor=True):
    """UN ACTA DE MENTIRA para el caso positivo por mutacion. NO toca el repo.

    Escribe los numerales de las secciones 5, 6 y 7 ENTRE COMILLAS INVERSAS, que
    es la forma del acta 187; la caida propia del auditor como cabecera de tercer
    nivel con `A.n`; y la caida del ejecutor como ``**`C.n`,`` al principio de
    linea, DEBAJO de una cabecera que dice de quien es. El ULTIMO `6.n` es la
    CORRECCION POR DECLARACION cuando `con_correccion`, y el anterior es el que
    SIGUE ABIERTA con sus puestos, que es la forma del acta 187.

    `dueno_ejecutor=False` fabrica el caso huerfano: la misma `C.n` bajo una
    cabecera que NO dice de quien es, que es el que tiene que hacer PARADA."""
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
    abierto = n_pd - 1 if (con_correccion and n_pd >= 2) else n_pd
    for k in range(1, n_pd + 1):
        if con_correccion and k == n_pd and n_pd >= 2:
            L += ["**`6.%d` LA `PD.9` DEL REPORTE %s, Y LO CORRIJO:** de mentira."
                  % (k, MARCA_CORRECCION), "", "Y su cuerpo.", ""]
        elif k == abierto:
            L += ["**`6.%d` `PD.1` %s, DE MENTIRA.** Los puestos (**%s**)"
                  % (k, MARCA_ABIERTA, ", ".join(str(x) for x in puestos)),
                  "estan medidos en otro sitio.", ""]
        else:
            L += ["**`6.%d` `PD.%d`, UN PENDIENTE DE MENTIRA: ADJUDICADO.** Y su cuerpo."
                  % (k, k + 4), ""]
    cab = "## 7. LAS PREGUNTAS, QUE ERAN MIAS Y %s" % (
        MARCA_CONTESTADAS if contesta else "NO DIGO NADA")
    L += [cab, ""]
    for k in range(1, n_preg + 1):
        L += ["**`7.%d` `P.%d`, UNA PREGUNTA DE MENTIRA.** Y su respuesta." % (k, k), ""]
    L += ["## 8. LA CAIDA PROPIA DEL %s, DE MENTIRA"
          % (DUENO_EJECUTOR if dueno_ejecutor else "QUIEN SEA"), ""]
    for k in range(1, caidas_rep + 1):
        L += ["**`C.%d`, UNA CAIDA DE MENTIRA.** Y su cuerpo." % k, ""]
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


def _mutacion_primera_mitad():
    """EL CASO POSITIVO POR MUTACION, SOBRE VARIABLE COMPUTADA Y NO SOBRE
    CONSTANTE LITERAL (`EJECUTOR.md` 1, EL CASO ROJO SE PRUEBA POR MUTACION).

    EL SUJETO ES SIEMPRE UN ACTA FABRICADA, NUNCA LA REAL, que es lo que el
    encargo de la vuelta 187 manda con esas palabras."""
    sys.stdout.reconfigure(encoding="utf-8")
    salida = []
    w = salida.append
    w("CASO POSITIVO POR MUTACION de vuelta187_tarea1a_registrar_acta187.py")
    w("EL SUJETO ES UN ACTA FABRICADA, NUNCA LA REAL.")
    w("")
    fallos = 0
    casos = [(6, 2, 3, 0, 1), (1, 2, 1, 0, 0), (12, 3, 5, 3, 2), (4, 2, 2, 1, 0)]
    for n_adj, n_pd, n_preg, n_aud, n_rep in casos:
        texto = _acta_fabricada(n_adj, n_pd, n_preg, n_aud, n_rep,
                                declara_cero=True)
        lineas, rango, err = cuerpo_del_acta(texto)
        if err:
            w("   %r -> %s" % ((n_adj, n_pd, n_preg, n_aud, n_rep), err))
            fallos += 1
            continue
        ini, fin = rango
        cl = claves_entrecomilladas(lineas, ini, fin, PREFIJO_ADJ)
        pd = claves_entrecomilladas(lineas, ini, fin, PREFIJO_PD)
        pr = claves_entrecomilladas(lineas, ini, fin, PREFIJO_PREG)
        aud = cuenta_por_patron(lineas, ini, fin, PAT_CAIDA_AUDITOR_A)
        c_eje, c_aud, huer = caidas_c_por_seccion(lineas, ini, fin)
        ok = (len(cl) == n_adj and len(pd) == n_pd and len(pr) == n_preg
              and len(aud) == n_aud and len(c_eje) == n_rep and not huer)
        titulo = titulo_de_la_entrada(len(cl), len(pd), len(pr), len(aud),
                                      len(c_eje))
        w("   acta fabricada con adj=%d pd=%d preg=%d aud=%d rep=%d"
          % (n_adj, n_pd, n_preg, n_aud, n_rep))
        w("      los contadores dicen adj=%d pd=%d preg=%d aud=%d rep=%d huerfanas=%d -> %s"
          % (len(cl), len(pd), len(pr), len(aud), len(c_eje), len(huer),
             "CALZA" if ok else "NO CALZA"))
        w("      titulo computado: %s" % titulo)
        if not ok:
            fallos += 1
    w("")
    w("LA MUTACION DEL VALOR ESPERADO, QUE ES LO QUE PRUEBA QUE EL CASO PUEDE CAER:")
    texto = _acta_fabricada(6, 2, 3, 0, 1, declara_cero=True)
    lineas, (ini, fin), _e = cuerpo_del_acta(texto)
    medido = len(claves_entrecomilladas(lineas, ini, fin, PREFIJO_ADJ))
    for esperado in (6, 7):
        w("   con el esperado %d: %s" % (esperado, "PASA" if medido == esperado else "CAE"))
    cae = medido != 7
    w("   medido sobre el acta fabricada (variable computada): %d" % medido)
    w("   EL CASO CAE AL MUTAR EL ESPERADO A 7: %s" % ("SI" if cae else "NO"))
    if not cae:
        fallos += 1
    w("")
    w("LA SEGUNDA MUTACION: LAS PREGUNTAS DE LA SECCION 7.")
    medido_pr = len(claves_entrecomilladas(lineas, ini, fin, PREFIJO_PREG))
    for esperado in (3, 4):
        w("   con el esperado %d: %s"
          % (esperado, "PASA" if medido_pr == esperado else "CAE"))
    cae_pr = medido_pr != 4
    w("   medido: %d | EL CASO CAE AL MUTAR EL ESPERADO A 4: %s"
      % (medido_pr, "SI" if cae_pr else "NO"))
    if not cae_pr:
        fallos += 1
    w("")
    w("LA TERCERA MUTACION: EL PATRON SIN COMILLAS, EL DEL ACTA 183. Sobre un acta")
    w("que numera con comillas inversas tiene que dar CERO.")
    con_viejo = len(claves_de_adjudicacion(lineas, ini, fin, PREFIJO_ADJ))
    w("   patron sin comillas sobre acta en forma 187 -> %d adjudicaciones" % con_viejo)
    w("   EL CASO CAE CON EL PATRON VIEJO: %s" % ("SI" if con_viejo == 0 else "NO"))
    if con_viejo != 0:
        fallos += 1
    w("")
    return salida, fallos, lineas, ini, fin


def _mutacion_segunda_mitad():
    """LA SEGUNDA MITAD: EL CUARTO ESTADO Y LA ATRIBUCION DE LA CAIDA `C.n`, que
    son las dos cosas que este registrador estrena. La cuenta de fallos es UNA
    SOLA y atraviesa las tres mitades."""
    salida, fallos, lineas, ini, fin = _mutacion_primera_mitad()
    w = salida.append
    w("LA CUARTA MUTACION: EL CUARTO ESTADO. El ULTIMO numeral de la seccion 6 del")
    w("acta fabricada es una CORRECCION POR DECLARACION y NO un pendiente. Con el")
    w("registrador de la 186, que solo sabia ABIERTA, CERRADA y ANOTACION, ese")
    w("titulo habria salido SIN DECIR y el instrumento habria hecho PARADA.")
    tit_pd, _e4 = _titulos_de(lineas, ini, fin, PREFIJO_PD)
    estados = [(c, pd, e) for c, pd, e, _l, _t
               in pendientes_de_doctrina(lineas, ini, fin, tit_pd)]
    w("   estados computados: %s" % estados)
    n_corr = len([1 for _c, _p, e in estados if e == "CORRECCION POR DECLARACION"])
    n_abier = len([1 for _c, _p, e in estados if e == "ABIERTA"])
    n_cerr = len([1 for _c, _p, e in estados if e == "CERRADA"])
    n_anot = len([1 for _c, _p, e in estados if e == "ANOTACION"])
    n_sin = len([1 for _c, _p, e in estados if e == "SIN DECIR"])
    ok_est = (n_corr == 1 and n_abier == 1 and n_cerr == 0 and n_anot == 0
              and n_sin == 0)
    w("   CORRECCION %d | ABIERTA %d | CERRADA %d | ANOTACION %d | SIN DECIR %d |"
      % (n_corr, n_abier, n_cerr, n_anot, n_sin))
    w("   esperado 1, 1, 0, 0, 0 -> %s" % ("CALZA" if ok_est else "NO CALZA"))
    w("   con el esperado MUTADO (0 correcciones): %s"
      % ("PASA" if n_corr == 0 else "CAE"))
    if not ok_est or n_corr == 0:
        fallos += 1
    sin_corr = _acta_fabricada(6, 2, 3, 0, 1, con_correccion=False)
    l5, (i5, f5), _e5 = cuerpo_del_acta(sin_corr)
    t5, _z5 = _titulos_de(l5, i5, f5, PREFIJO_PD)
    est5 = [e for _c, _p, e, _l, _t in pendientes_de_doctrina(l5, i5, f5, t5)]
    w("   y sobre un acta SIN correccion, para que se vea que el estado no esta")
    w("   clavado: %s" % est5)
    if "CORRECCION POR DECLARACION" in est5:
        w("   LA CORRECCION APARECE DONDE NO LA HAY: NO")
        fallos += 1
    w("")
    w("LA QUINTA MUTACION, Y ES LA QUE EL ENCARGO PIDE CON NOMBRE: UN ESTADO QUE EL")
    w("REGISTRADOR NO SABE LEER TIENE QUE HACER PARADA, NO CAER EN EL SACO DE LOS")
    w("ABIERTOS NI EN EL DE LOS CERRADOS. Se fabrica un `6.n` cuyo titulo no dice")
    w("ninguna de las cuatro marcas y se exige SIN DECIR.")
    raro = _acta_fabricada(6, 2, 3, 0, 1, con_correccion=False)
    raro = raro.replace("**`6.2` `PD.1` %s, DE MENTIRA.**" % MARCA_ABIERTA,
                        "**`6.2` `PD.1` EN UN ESTADO QUE NADIE ESCRIBIO.**")
    l9, (i9, f9), _e9 = cuerpo_del_acta(raro)
    t9, _z9 = _titulos_de(l9, i9, f9, PREFIJO_PD)
    est9 = [e for _c, _p, e, _l, _t in pendientes_de_doctrina(l9, i9, f9, t9)]
    w("   estados sobre el acta del estado desconocido: %s" % est9)
    hay_sin = "SIN DECIR" in est9
    w("   SALE `SIN DECIR`, QUE ES LA PARADA: %s" % ("SI" if hay_sin else "NO"))
    w("   con el esperado MUTADO (ninguno SIN DECIR): %s"
      % ("PASA" if not hay_sin else "CAE"))
    if not hay_sin:
        fallos += 1
    w("")
    w("LA SEXTA MUTACION: LA ATRIBUCION DE LA CAIDA `C.n`, QUE LA HACE LA SECCION Y")
    w("NO EL PATRON. El mismo `C.1` bajo una cabecera que nombra al EJECUTOR es del")
    w("ejecutor; bajo una que dice MI CAIDA es del auditor; y bajo una que no dice")
    w("ninguna de las dos es HUERFANA y hace PARADA.")
    c_eje, c_aud, huer = caidas_c_por_seccion(lineas, ini, fin)
    w("   acta con cabecera del EJECUTOR -> ejecutor %d | auditor %d | huerfanas %d"
      % (len(c_eje), len(c_aud), len(huer)))
    huerf = _acta_fabricada(6, 2, 3, 0, 1, dueno_ejecutor=False)
    l7, (i7, f7), _e7 = cuerpo_del_acta(huerf)
    c_eje2, c_aud2, huer2 = caidas_c_por_seccion(l7, i7, f7)
    w("   acta con cabecera SIN dueno -> ejecutor %d | auditor %d | huerfanas %d"
      % (len(c_eje2), len(c_aud2), len(huer2)))
    ok_atr = (len(c_eje) == 1 and len(c_aud) == 0 and len(huer) == 0
              and len(c_eje2) == 0 and len(huer2) == 1)
    w("   LA ATRIBUCION SIGUE A LA CABECERA: %s" % ("SI" if ok_atr else "NO"))
    w("   con el esperado MUTADO (la huerfana atribuida al ejecutor): %s"
      % ("PASA" if len(c_eje2) == 1 else "CAE"))
    if not ok_atr or len(c_eje2) == 1:
        fallos += 1
    w("   Y EL PATRON A SECAS, EL QUE ESTA MUTACION EXISTE PARA DESARMAR: sobre el")
    w("   acta con cabecera del EJECUTOR, `cuenta_por_patron` con el patron `C.n`")
    crudo = cuenta_por_patron(lineas, ini, fin, PAT_CAIDA_C)
    w("   da %d, que es exactamente la cifra que habria publicado UNA caida propia" % len(crudo))
    w("   del auditor donde el acta declara CERO.")
    if len(crudo) != 1:
        fallos += 1
    w("")
    return salida, fallos, lineas, ini, fin


def prueba_de_mutacion():
    """EL CASO POSITIVO POR MUTACION, ENTERO Y CON UNA SOLA CUENTA DE FALLOS."""
    sys.stdout.reconfigure(encoding="utf-8")
    salida, fallos, lineas, ini, fin = _mutacion_segunda_mitad()
    w = salida.append
    w("LA SEPTIMA MUTACION: EL PATRON `A.n` Y LA DECLARACION DEL CERO.")
    aud_nuevo = len(cuenta_por_patron(lineas, ini, fin, PAT_CAIDA_AUDITOR_A))
    d_vieja, d_nueva = lineas_que_declaran_cero_caidas(lineas, ini, fin)
    w("   patron `A.n` -> %d" % aud_nuevo)
    w("   frase %r -> %d linea(s) | frase %r -> %d"
      % (FRASE_CERO_CAIDAS_PROPIAS, len(d_nueva),
         FRASE_SIN_CAIDA_PROPIA, len(d_vieja)))
    ok_aud = (aud_nuevo == 0 and len(d_nueva) == 1 and len(d_vieja) == 0)
    w("   EL CERO VA CONTADO Y DECLARADO: %s" % ("SI" if ok_aud else "NO"))
    w("   con el esperado MUTADO (1 caida propia): %s"
      % ("PASA" if aud_nuevo == 1 else "CAE"))
    if not ok_aud or aud_nuevo == 1:
        fallos += 1
    con_caida = _acta_fabricada(6, 2, 3, 2, 1)
    l6, (i6, f6), _e6 = cuerpo_del_acta(con_caida)
    n6 = len(cuenta_por_patron(l6, i6, f6, PAT_CAIDA_AUDITOR_A))
    w("   y sobre un acta CON dos caidas propias, para que se vea que el contador")
    w("   no esta clavado en cero: patron `A.n` -> %d" % n6)
    if n6 != 2:
        fallos += 1
    w("")
    w("LA OCTAVA MUTACION: EL PATRON `R.n` Y EL `E.n` SOBRE UNA CAIDA ESCRITA COMO")
    w("`C.n`. Los dos tienen que dar CERO, y su cero es la medicion que prueba que")
    w("hacia falta la atribucion por seccion.")
    rep_r = len(cuenta_por_patron(lineas, ini, fin, PAT_CAIDA_REPORTE))
    rep_e = len(cuenta_por_patron(lineas, ini, fin, PAT_CAIDA_EJECUTOR_VIEJO))
    w("   patron `R.n` -> %d | patron `E.n` -> %d" % (rep_r, rep_e))
    ok_rep = (rep_r == 0 and rep_e == 0)
    w("   LOS DOS VIEJOS DAN CERO: %s" % ("SI" if ok_rep else "NO"))
    if not ok_rep:
        fallos += 1
    w("")
    w("LA NOVENA MUTACION: EL ESTADO DE LAS PREGUNTAS, LEIDO DE LA CABECERA.")
    tit_pr, _e7 = _titulos_de(lineas, ini, fin, PREFIJO_PREG)
    _lst, estado_si, ln7, cab7 = preguntas_de_la_seccion7(lineas, ini, fin, tit_pr)
    muda = _acta_fabricada(6, 2, 3, 0, 1, contesta=False)
    l8, (i8, f8), _e8 = cuerpo_del_acta(muda)
    tit8, _z8 = _titulos_de(l8, i8, f8, PREFIJO_PREG)
    _l8, estado_no, _ln8, cab8 = preguntas_de_la_seccion7(l8, i8, f8, tit8)
    w("   cabecera que SI contesta (linea %s): %r -> %s" % (ln7, cab7, estado_si))
    w("   cabecera que NO lo dice: %r -> %s" % (cab8, estado_no))
    ok_pr = (estado_si == "CONTESTADA" and estado_no == "SIN DECIR")
    w("   EL ESTADO SIGUE A LA CABECERA: %s" % ("SI" if ok_pr else "NO"))
    w("   con el esperado MUTADO (la muda tambien CONTESTADA): %s"
      % ("PASA" if estado_no == "CONTESTADA" else "CAE"))
    if not ok_pr or estado_no == "CONTESTADA":
        fallos += 1
    w("")
    w("LA DECIMA MUTACION: LOS PUESTOS DE LA `PD.1`, LEIDOS DEL ACTA.")
    for inventados in ((11, 22, 33), (7, 8, 9, 10)):
        t2 = _acta_fabricada(6, 2, 3, 0, 1, puestos=inventados)
        l2, (i2, f2), _z = cuerpo_del_acta(t2)
        tit2, err2 = _titulos_de(l2, i2, f2, PREFIJO_PD)
        if err2:
            w("   %s" % err2)
            fallos += 1
            continue
        leidos = puestos_de_la_pd1(l2, i2, f2, tit2)
        ok_p = leidos == list(inventados)
        w("   acta con puestos %s -> leidos %s -> %s"
          % (list(inventados), leidos, "CALZA" if ok_p else "NO CALZA"))
        if not ok_p:
            fallos += 1
    reales = (1778, 2530, 2540, 3141, 3232)
    t3 = _acta_fabricada(6, 2, 3, 0, 1, puestos=reales)
    l3, (i3, f3), _z3 = cuerpo_del_acta(t3)
    tit3, _e3 = _titulos_de(l3, i3, f3, PREFIJO_PD)
    leidos3 = puestos_de_la_pd1(l3, i3, f3, tit3)
    w("   y con los cinco que el encargo nombra -> leidos %s" % leidos3)
    w("   con el esperado MUTADO [1778, 2530, 2540, 3141, 9999]: %s"
      % ("PASA" if leidos3 == [1778, 2530, 2540, 3141, 9999] else "CAE"))
    if leidos3 == [1778, 2530, 2540, 3141, 9999]:
        fallos += 1
    w("")
    w("LA UNDECIMA MUTACION: EL SALTO. actas_sin_entrada() es PURA y se importa del")
    w("registrador de la 183.")
    serie_falsa = [
        (10, "docs/PENDIENTES.md", 1, "## R.10. Registro del acta de la vuelta 100"),
        (11, "docs/PENDIENTES.md", 2, "## R.11. Registro del acta de la vuelta 101"),
        (12, "docs/PENDIENTES.md", 3, "## R.12. Registro del acta de la vuelta 105"),
    ]
    faltan, bajo, alto = actas_sin_entrada(serie_falsa, 100, 105)
    w("   faltan (computado): %s" % faltan)
    w("   extremo bajo: %s | extremo alto: %s" % (bajo, alto))
    ok_salto = (faltan == [102, 103, 104] and bajo == (11, 101) and alto == (12, 105))
    w("   EL SALTO Y SUS EXTREMOS CALZAN: %s" % ("SI" if ok_salto else "NO"))
    if not ok_salto:
        fallos += 1
    w("")
    w("LA DUODECIMA MUTACION: EL TITULO Y SU CONCORDANCIA, INCLUIDO EL CERO.")
    t0 = titulo_de_la_entrada(6, 2, 3, 0, 1)
    w("   %s" % t0)
    ok_t = ("las seis adjudicaciones numeradas" in t0
            and "los dos numerales de la seccion 6" in t0
            and "las tres preguntas contestadas" in t0
            and "las cero caidas propias" in t0
            and "la caida de reporte del ejecutor" in t0)
    w("   DICE LAS CINCO COSAS Y CONCUERDA: %s" % ("SI" if ok_t else "NO"))
    if not ok_t:
        fallos += 1
    t1 = titulo_de_la_entrada(3, 1, 1, 2, 2)
    w("   y con otras cifras, para que se vea que no esta clavada: %s" % t1)
    if ("las tres adjudicaciones" not in t1
            or "el numeral de la seccion 6" not in t1
            or "la pregunta contestada" not in t1
            or "las dos caidas propias" not in t1
            or "las dos caidas de reporte" not in t1):
        w("   LA CONCORDANCIA NO SIGUE A LAS CIFRAS: NO")
        fallos += 1
    else:
        w("   LA CONCORDANCIA SIGUE A LAS CIFRAS: SI")
    w("")
    w("CIFRA fallos: %d" % fallos)
    w("VEREDICTO: %s" % ("VERDE" if fallos == 0 else "ROJO"))
    t = NL.join(salida) + NL
    ruta = os.path.join(LOOP, "SALIDA_V%s_T1A_MUTACION_REGISTRO_187.txt"
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
    w("   prefijo: %r, con el numeral ENTRE COMILLAS INVERSAS" % PREFIJO_ADJ)
    w("   CIFRA adjudicaciones numeradas halladas: %d" % len(claves))
    for clave, cuantas in claves:
        w("      %s -> %d aparicion(es)" % (clave, cuantas))
    viejas_adj = claves_de_adjudicacion(lineas, inicio, fin, PREFIJO_ADJ)
    w("   EL CONTRASTE QUE PRUEBA QUE HACIA FALTA EL PATRON ENTRECOMILLADO:")
    w("      el patron SIN comillas, el del acta 183 -> %d sobre esta acta"
      % len(viejas_adj))
    dobles = [c for c, n in claves if n != 1]
    if dobles:
        w("   PARADA: hay claves repetidas dentro del acta: %s" % ", ".join(dobles))
        print(NL.join(salida))
        return 1
    w("")

    w("C) LOS NUMERALES DE LA SECCION 6 Y LAS PREGUNTAS DE LA 7, CON EL MISMO PATRON")
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
    c_eje, c_aud, huerfanas = caidas_c_por_seccion(lineas, inicio, fin)
    decl_vieja, decl_nueva = lineas_que_declaran_cero_caidas(lineas, inicio, fin)
    w("   CAIDAS PROPIAS DEL AUDITOR (patron `A.n`, cabecera de tercer nivel): %d, lineas %s"
      % (len(l_aud), ", ".join(str(x) for x in l_aud) or "(ninguna)"))
    w("   EL PATRON `C.n` A SECAS, SIN MIRAR LA SECCION: %d" % len(l_c_crudo))
    w("   Y REPARTIDO POR LA CABECERA DE SU SECCION, QUE ES LA ATRIBUCION BUENA:")
    w("      DEL EJECUTOR: %d" % len(c_eje))
    for ln, num, cab in c_eje:
        w("         LINEA %d: C.%d bajo %r" % (ln, num, cab[:100]))
        w("            %s" % lineas[ln - 1].strip()[:130])
    w("      DEL AUDITOR: %d" % len(c_aud))
    for ln, num, cab in c_aud:
        w("         LINEA %d: C.%d bajo %r" % (ln, num, cab[:100]))
    w("      HUERFANAS (sin dueno declarado en su cabecera): %d" % len(huerfanas))
    for ln, num, cab in huerfanas:
        w("         LINEA %d: C.%d bajo %r" % (ln, num, cab[:100]))
    w("   CAIDAS DE REPORTE CON EL PATRON `R.n` DEL ACTA 186: %d" % len(l_rep))
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
        w("   PARADA: no se encuentra ninguna caida del ejecutor, y el acta 187")
        w("   declara una en su seccion 8. No se escribe una entrada asi.")
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
            decl_nueva)


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
     l_aud, l_rep, l_eje_v, c_eje, c_aud, decl_vieja, decl_nueva) = medido
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

    w("G) EL ESTADO DE CADA NUMERAL DE LA SECCION 6, LEIDO DE SU TITULO")
    pds = pendientes_de_doctrina(lineas, inicio, fin, titulos)
    for clave, pd, estado, ln, _tit in pds:
        w("   %s nombra %s -> %s (linea %d)" % (clave, pd, estado, ln))
    sin_decir = [c for c, _p, e, _l, _t in pds if e == "SIN DECIR"]
    if sin_decir:
        w("   PARADA: %s esta en un estado que este registrador NO SABE LEER. No se"
          % ", ".join(sin_decir))
        w("   mete en el saco de los abiertos ni en el de los cerrados.")
        print(NL.join(salida))
        return 1
    w("   REPARTO: CERRADAS %d | ABIERTAS %d | ANOTACIONES %d | CORRECCIONES POR "
      "DECLARACION %d"
      % (len([1 for _c, _p, e, _l, _t in pds if e == "CERRADA"]),
         len([1 for _c, _p, e, _l, _t in pds if e == "ABIERTA"]),
         len([1 for _c, _p, e, _l, _t in pds if e == "ANOTACION"]),
         len([1 for _c, _p, e, _l, _t in pds
              if e == "CORRECCION POR DECLARACION"])))
    puestos_pd1 = puestos_de_la_pd1(lineas, inicio, fin, titulos)
    w("   LOS PUESTOS DEL NUMERAL ABIERTO, LEIDOS DEL ACTA: %s"
      % (", ".join(str(x) for x in puestos_pd1) or "(ninguno)"))
    if not puestos_pd1:
        w("   PARADA: el numeral abierto no nombra ningun puesto y el acta dice")
        w("   que tiene cinco nombres. No se escribe una lista vacia.")
        print(NL.join(salida))
        return 1
    w("")

    w("H) LAS PREGUNTAS DE LA SECCION 7, CON SU ESTADO LEIDO DE LA CABECERA")
    preguntas, estado_preg, ln7, cab7 = preguntas_de_la_seccion7(
        lineas, inicio, fin, titulos)
    w("   cabecera de la seccion 7 (linea %s): %s" % (ln7, cab7))
    w("   estado que esa cabecera declara: %s" % estado_preg)
    if estado_preg == "SIN DECIR":
        w("   PARADA: la cabecera de la seccion 7 no dice %r. Un acta que"
          % MARCA_CONTESTADAS)
        w("   pregunta y no dice si contesta no se registra como si contestara.")
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

    w("J) LA DEUDA DE LA SERIE, REMEDIDA EN ESTA VUELTA Y NO HEREDADA DEL R.48")
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
    w("K) LA IDEMPOTENCIA, COMPROBADA ANTES DE ESCRIBIR")
    w("   la marca %r ya esta en la sede: %s"
      % (marca, "SI" if marca in texto_sede else "NO"))
    w("   la entrada entera ya esta: %s" % ("SI" if ya else "NO"))
    w("")

    entrada = armar_entrada(numero, titulo, claves, pds, preguntas, estado_preg,
                            (ln7, cab7), titulos, l_aud, l_rep, decl_vieja,
                            decl_nueva, inicio, fin, len(viejas_adj),
                            len(l_eje_v), c_eje, c_aud, puestos_pd1, salto)
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
