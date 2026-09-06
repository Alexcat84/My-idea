# -*- coding: utf-8 -*-
r"""vuelta186_tarea1a_registrar_acta186.py . EL ACTA 186 ENTERA, REGISTRADA EN LA
SERIE `R.N` EN LA FORMA DE LA CASA.

LA MAQUINA NO SE CLONA, SE IMPORTA, y eso lo adjudico la `6.6` del acta 172 como
correcto y obligatorio: `PALABRA` y `titulo_de_la_negrita` se importan de
`scripts/loop/vuelta172_tarea1_registrar_acta171.py`, `claves_de_adjudicacion` y
`cuenta_por_patron` del registrador de la vuelta 182, `actas_sin_entrada` del de
la 183 y `claves_entrecomilladas` del de la 184. Lo unico propio de este fichero
es EL ACOTE DE SU ACTA, LOS PATRONES QUE SU ACTA NECESITA Y SUS GLOSAS.

POR QUE HACE FALTA CODIGO PROPIO OTRA VEZ, MEDIDO Y NO SUPUESTO, Y SON TRES COSAS
QUE EL REGISTRADOR DE LA 185 NO SABE HACER:

  1) EL ACTA 186 TIENE UNA SECCION 7 DE TRES PREGUNTAS NUMERADAS,
     ``**`7.1` `` a ``**`7.3` ``, Y NINGUN REGISTRADOR ANTERIOR LAS CUENTA. Se
     cuentan con `claves_entrecomilladas` IMPORTADA y otro prefijo: no se escribe
     un patron nuevo donde el viejo ya muerde.

  2) EL `6.4` DE ESTA ACTA NO ES UN PENDIENTE: ES UNA ANOTACION, Y EL ACTA LO
     DICE CON SUS PALABRAS (*"ANOTO UN PENDIENTE QUE NO ES MIO Y NO LO CONVIERTO
     EN UNO"*). El registrador de la 185 solo sabia leer ABIERTA o CERRADA y
     hacia PARADA en cualquier otra cosa. Aqui se anade el tercer estado,
     ANOTACION, LEIDO DEL TITULO con la marca literal `NO LO CONVIERTO EN UNO`, y
     los otros dos se conservan intactos.

  3) EL ACTA 186 NO TIENE NINGUNA CAIDA PROPIA DEL AUDITOR Y LO DECLARA CON OTRAS
     PALABRAS. La frase del acta 185 era `NINGUNA CAIDA PROPIA` y aqui la frase es
     `CERO CAIDAS PROPIAS`. LAS DOS SE CUENTAN Y LAS DOS CIFRAS SE PUBLICAN: un
     cero contado y un campo ausente no son lo mismo, y por eso el instrumento
     hace PARADA si sale cero sin que el acta lo declare por ninguna de las dos.

Y UNA CUARTA COSA QUE NO ES UN PATRON SINO UNA CIFRA: LOS CINCO PUESTOS DE LA
`PD.1` NO SE TECLEAN. El encargo los nombra (1778, 2530, 2540, 3141, 3232) y aqui
NO se copian: se leen del parrafo del `6.n` que el propio titulo declara ABIERTO,
y si el acta dijera otros, la entrada diria otros.

LAS CIFRAS DEL TITULO NO SE TECLEAN: se cuentan del acta acotada. Ni el numero de
la entrada: lo devuelve `scripts/loop/serie_de_registros.py` recomputando la serie
de sus DOS sedes. Y LA DEUDA DE LA SERIE SE REMIDE EN ESTA VUELTA y no se hereda
del `R.47`, que es lo que el encargo pide con esas palabras.

LO QUE ESTE FICHERO NO HACE: no toca el acta, no toca el reporte, no toca
`docs/plan/`, no corre la bateria y no escribe ningun veredicto. Escribe UNA
entrada en UNA sede, y si la entrada ya esta, NO la duplica y lo dice.

USO:
  python scripts/loop/vuelta186_tarea1a_registrar_acta186.py
  python scripts/loop/vuelta186_tarea1a_registrar_acta186.py --simular
  python scripts/loop/vuelta186_tarea1a_registrar_acta186.py --mutacion
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
from vuelta184_tarea1a_registrar_acta184 import claves_entrecomilladas   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")
SEDE = os.path.join(RAIZ, "docs", "PENDIENTES.md")
NL = chr(10)

VUELTA_DEL_ACTA = 186
VUELTA_QUE_ESCRIBE = 186
SUFIJO_QUE_ESCRIBE = "186"
CABECERA_ACTA = "# ACTA DEL AUDITOR, VUELTA %d" % VUELTA_DEL_ACTA
PREFIJO_ADJ = "5."
PREFIJO_PD = "6."
PREFIJO_PREG = "7."

PALABRA_CON_CERO = dict(PALABRA)
PALABRA_CON_CERO[0] = "cero"

# LOS PATRONES. Los que llevan `VIEJO` en el nombre son los de las actas
# anteriores y se conservan a proposito: su CERO sobre esta acta es la medicion
# que prueba que hacia falta uno nuevo.
PAT_CAIDA_REPORTE = re.compile(r"^\s*(?:-\s+)?\*\*`?R\.(\d+)`?[,.]")
PAT_CAIDA_EJECUTOR_VIEJO = re.compile(r"^\s*(?:-\s+)?\*\*`?E\.(\d+)`?[,.]")
PAT_CAIDA_AUDITOR_A = re.compile(r"^###\s+\d+\.\d+\s+MI CAIDA PROPIA\s+`A\.(\d+)`")
PAT_CAIDA_AUDITOR_VIEJO = re.compile(r"^\s*(?:-\s+)?\*\*`?C\.(\d+)`?[,.]")
PAT_CAIDA_AUDITOR_PROSA_VIEJO = re.compile(r"^\*\*[^*]*CAIDA[^*]*`C\.(\d+)`")

# LAS DOS FRASES CON LAS QUE UN ACTA PUEDE DECLARAR QUE NO TUVO CAIDA PROPIA. La
# primera es la del acta 185 y la segunda la del acta 186. LAS DOS SE CUENTAN.
FRASE_SIN_CAIDA_PROPIA = "NINGUNA CAIDA PROPIA"
FRASE_CERO_CAIDAS_PROPIAS = "CERO CAIDAS PROPIAS"

# EL PENDIENTE DE DOCTRINA QUE CADA `6.n` NOMBRA, y si lo CIERRA, lo deja
# ABIERTO o es una ANOTACION que no es pendiente propio. Las tres cosas se leen
# del titulo literal del acta y NO se teclean.
PAT_PD_DEL_TITULO = re.compile(r"`PD\.(\d+)`")
PAT_P_DEL_TITULO = re.compile(r"`P\.(\d+)`")
MARCA_ABIERTA = "SIGUE ABIERTA"
MARCA_CERRADA = "ADJUDICAD"
MARCA_ANOTACION = "NO LO CONVIERTO EN UNO"
# LA MARCA CON LA QUE LA CABECERA DE LA SECCION 7 DICE QUE LAS PREGUNTAS ESTAN
# CONTESTADAS. Si la cabecera no la trae, el instrumento hace PARADA en vez de
# suponer que estan contestadas.
MARCA_CONTESTADAS = "LAS CONTESTO"


def cuerpo_del_acta(texto=None):
    """EL ACTA ACOTADA: (lineas, (inicio, fin), error). El fin es el final del
    fichero porque el acta 186 es la ultima escrita; si algun dia dejara de
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
    """LAS LINEAS DONDE EL ACTA DECLARA QUE NO TUVO CAIDAS PROPIAS, POR
    CUALQUIERA DE LAS DOS FRASES QUE LA CASA HA USADO. Devuelve
    (lineas_de_la_frase_185, lineas_de_la_frase_186). PURA.

    Un cero que sale de un patron que no muerde y un cero que el acta declara con
    todas las letras son la misma cifra y NO son la misma evidencia. LAS DOS
    CIFRAS SE PUBLICAN: la vieja da cero sobre esta acta y esa es justamente la
    medicion que prueba que hacia falta la nueva."""
    viejas = [i for i in range(inicio, fin + 1)
              if FRASE_SIN_CAIDA_PROPIA in lineas[i - 1]]
    nuevas = [i for i in range(inicio, fin + 1)
              if FRASE_CERO_CAIDAS_PROPIAS in lineas[i - 1]]
    return viejas, nuevas


def parrafo_de(lineas, linea_cabecera, fin):
    """EL PARRAFO QUE EMPIEZA EN UNA LINEA Y ACABA EN LA PRIMERA LINEA VACIA.
    PURA. Devuelve el texto unido por espacios, para que un patron pueda cruzar
    los saltos de linea que el markdown mete donde le cabe el ancho."""
    trozos = []
    for i in range(linea_cabecera, fin + 1):
        if not lineas[i - 1].strip():
            break
        trozos.append(lineas[i - 1].strip())
    return " ".join(trozos)


def pendientes_de_doctrina(lineas, inicio, fin, titulos):
    """LOS `6.n` DE LA SECCION 6, CON SU ESTADO LEIDO DEL TITULO. Devuelve
    [(clave, pd, estado, linea, titulo)]. PURA.

    EL ESTADO NO SE TECLEA: sale de buscar en el titulo literal, EN ESTE ORDEN,
    `NO LO CONVIERTO EN UNO` (ANOTACION), `SIGUE ABIERTA` (ABIERTA) o
    `ADJUDICAD` (CERRADA). Si un titulo no dijera ninguna de las tres, el estado
    sale como `SIN DECIR` y el instrumento hace PARADA en vez de suponer.

    EL TERCER ESTADO NACE EN LA VUELTA 186 Y NO ES UN ENSANCHE: el `6.4` del acta
    186 no es un pendiente de doctrina, es una ANOTACION de un trabajo que el
    auditor dice expresamente que NO convierte en pendiente propio. Meterlo en el
    saco de los cerrados o en el de los abiertos seria publicar una cifra falsa
    de pendientes."""
    salida = []
    for clave, _n in claves_entrecomilladas(lineas, inicio, fin, PREFIJO_PD):
        ln, tit = titulos[clave]
        m = PAT_PD_DEL_TITULO.search(tit)
        pd = ("PD.%s" % m.group(1)) if m else "(sin PD en el titulo)"
        if MARCA_ANOTACION in tit:
            estado = "ANOTACION"
        elif MARCA_ABIERTA in tit:
            estado = "ABIERTA"
        elif MARCA_CERRADA in tit:
            estado = "CERRADA"
        else:
            estado = "SIN DECIR"
        salida.append((clave, pd, estado, ln, tit))
    return salida


def cabecera_de_la_seccion(lineas, inicio, fin, numero):
    """LA LINEA Y EL TEXTO DE LA CABECERA `## <numero>.` DENTRO DEL ACTA ACOTADA,
    o (None, "") si no esta. PURA."""
    for i in range(inicio, fin + 1):
        if lineas[i - 1].startswith("## %d. " % numero):
            return i, lineas[i - 1].strip()
    return None, ""


def preguntas_de_la_seccion7(lineas, inicio, fin, titulos):
    """LAS PREGUNTAS DE LA SECCION 7, CON SU ESTADO LEIDO DE LA CABECERA DE LA
    PROPIA SECCION. Devuelve (lista, estado, linea_de_la_cabecera, cabecera),
    con lista de [(clave, p, linea, titulo)]. PURA.

    EL ESTADO NO SE TECLEA NI SE SUPONE: sale de buscar `LAS CONTESTO` en la
    cabecera literal de la seccion 7. Si la cabecera no lo dice, el estado es
    `SIN DECIR` y quien llama hace PARADA. Un acta que hace preguntas y no dice
    si las contesta no se registra como si las contestara."""
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
    PURA. Devuelve la lista de enteros, vacia si no los encuentra.

    EL ENCARGO LOS DA (1778, 2530, 2540, 3141, 3232) Y AQUI NO SE COPIAN: se
    localiza el `6.n` cuyo titulo dice `SIGUE ABIERTA`, se toma su parrafo entero
    y se leen los numeros del grupo en negrita que va detras de la palabra `son`.
    Si el acta dijera otros, esta entrada diria otros."""
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
    concordancia dentro del computo. El CERO entra por `PALABRA_CON_CERO`, y va
    en plural porque en castellano el cero es plural.

    LA CIFRA DE PENDIENTES QUE ENTRA AQUI ES LA DE LOS `6.n` DEL ACTA, que en el
    acta 186 son cuatro aunque uno de ellos sea una ANOTACION. El reparto por
    estado va dentro de la entrada, con su nombre, y no se esconde en el titulo:
    contar tres para que cuadre con la glosa seria teclear una cifra."""
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
    "5.4": "EJECUTADA",
    "5.5": "SIN TOCAR NADA",
    "5.6": "SIN TOCAR NADA",
    "5.7": "SIN TOCAR NADA",
    "6.1": "EJECUTADA",
    "6.2": "EJECUTADA",
    "6.3": "SIN TOCAR NADA",
    "6.4": "SIN TOCAR NADA",
    "7.1": "EJECUTADA",
    "7.2": "EJECUTADA",
    "7.3": "EJECUTADA",
}

QUE_HACE_ESTA_VUELTA = {
    "5.1": ("SE ACATA SIN TOCAR NADA. Anadir a la prosa del tallador la procedencia de "
            "la novena columna queda adjudicado como EL REMEDIO y no como una desviacion "
            "del remedio, porque la `R.1` del acta 185 decia justamente que la "
            "enumeracion de procedencias no la incluia. No mueve ninguna celda y no deja "
            "trabajo."),
    "5.2": ("SE ACATA SIN TOCAR NADA, Y EL ACTA LA CONVIERTE EN REGLA POR EXTENSION. La "
            "frontera es EL SELLO: un arnes que nace en la vuelta y todavia no ha sellado "
            "ninguna salida es un arnes EN CONSTRUCCION y su rojo es parte de escribirlo; "
            "desde que su salida se sella y se commitea una vez, su rojo detiene la "
            "vuelta. ESTA VUELTA LA USA, porque escribe cuatro arneses nuevos, y cumple "
            "sus dos condiciones: la corrida en rojo se pega entera y el motivo queda "
            "dentro del propio fichero."),
    "5.3": ("SE ACATA SIN TOCAR NADA, Y LA CONVENCION DEJA DE SER UNA DEDUCCION. El acta "
            "escribe que la negrita marca la vuelta mas alta del reparto, para que la 189 "
            "no tenga que volver a deducirlo. No queda trabajo."),
    "5.4": ("SE ACATA Y SE EJECUTA EN LA TAREA 1.b DE ESTA VUELTA. El acta concede que "
            "medir el dano y decirlo era la conducta correcta, y se queda con la "
            "consecuencia: meter los dos arneses en la nomina es trabajo de encargo y va "
            "BLOQUEANTE. La prueba es `arneses_que_faltan()` devolviendo 0 despues, con "
            "el tamano de la nomina antes y despues."),
    "5.5": ("SE ACATA SIN TOCAR NADA. Guardar el reporte que el instrumento si llego a "
            "escribir y restaurar el arbol con `git checkout` queda adjudicado como la "
            "unica salida que no pierde nada, y es fallar ruidoso aplicado a un "
            "artefacto. El fichero sigue en disco y esta vuelta lo usa como sujeto real "
            "del arnes de la pieza (2)."),
    "5.6": ("SE ACATA SIN TOCAR NADA, Y LA REGLA QUE DEJA ESCRITA SE APLICA AQUI. Cuando "
            "cumplir la letra de una regla exige romper otra, se cumple la que no "
            "destruye evidencia y se declara. Esta vuelta repara el defecto que forzaba "
            "aquella desviacion: la pieza (2) deja de encenderse sobre una cita."),
    "5.7": ("SE ACATA SIN TOCAR NADA. Cerrar el reporte propio sabiendo que el ajeno no "
            "cerro queda adjudicado como cumplir la decision del fundador y no como "
            "eludirla, porque son dos reportes distintos y el 6.2 mide el propio. Esta "
            "vuelta cierra LOS DOS."),
    "6.1": ("`PD.6` CERRADA POR CITA, Y ES UNA DE LAS DOS ADJUDICACIONES QUE MANDAN TOCAR "
            "CODIGO. EJECUTADA EN LA TAREA 2.a DE ESTA VUELTA. La comparacion "
            "`ajena != vuelta` vivia DOS veces en `scripts/loop/cerrar_reporte.py`, y "
            "reparar una sede y no la otra deja el instrumento diciendo dos cosas del "
            "mismo caso. LA CONDICION DEL ACTA NO ES DE ESTILO Y SE CUMPLE AL PIE DE LA "
            "LETRA: la pieza (4) NO recibe una copia sincronizada, LLAMA a la unica sede, "
            "y el arnes cuenta las apariciones de la comparacion en el fichero y EXIGE 1. "
            "La prueba vive en `docs/loop/SALIDA_V186_T2A_MUTACION_PIEZA4.txt`."),
    "6.2": ("`PD.5` CERRADA POR CITA, Y ES LA OTRA QUE MANDA TOCAR CODIGO. EJECUTADA EN "
            "LA TAREA 2.b DE ESTA VUELTA. La pieza (2) buscaba su marca EN TODO EL TEXTO "
            "y se encendia sobre una cita dentro de un bloque cercado, que era su propia "
            "salida citada: un falso positivo no es fallar ruidoso, es ruido. La "
            "reparacion REUSA el desbloqueador que `cifras_sin_pareja()` ya tenia, "
            "separado a una sede y llamado por las dos, y NO escribe un tercero. La "
            "prueba vive en `docs/loop/SALIDA_V186_T2B_MUTACION_PIEZA2_CERCAS.txt`."),
    "6.3": ("`PD.1` SIGUE ABIERTA, QUINTA VUELTA, Y ESTA VUELTA NO LA CIERRA NI LA "
            "ENCARGA. El acta la deja registrada con sus cinco puestos y dice con todas "
            "las letras que darles cola seria doctrina nueva, que es del fundador. Sus "
            "cinco nombres van en esta entrada leidos del acta y no copiados del encargo."),
    "6.4": ("NO ES UN PENDIENTE Y NO SE CONVIERTE EN UNO: ES UNA ANOTACION, Y ASI SE "
            "REGISTRA. El acta anota que con el puesto 338 y el 297 ya son TRES nodos "
            "juzgando la misma puerta del `PMF`, y que eso pide mesa de los tres a la vez "
            "y no tres veredictos de pareja. El propio acta dice que NO lo encarga y NO "
            "lo adjudica, porque es trabajo de plan. ESTA VUELTA NO ABRE ESA MESA, y su "
            "encargo se lo prohibe con esas palabras."),
    "7.1": ("CONTESTADA POR EL ACTA Y EJECUTADA EN LA TAREA 2 DE ESTA VUELTA: las dos "
            "piezas van JUNTAS, en la misma tarea, y CADA UNA CON SU PROPIO ARNES. "
            "Ninguna se prueba con el arnes de la otra, porque son especies distintas: "
            "una es una regla duplicada y la otra un ambito de busqueda."),
    "7.2": ("CONTESTADA POR EL ACTA Y EJECUTADA EN LA TAREA 2.c DE ESTA VUELTA: las "
            "cifras sin pareja del reporte de la 184 NI SE EXIMEN NI SE REESCRIBEN, SE "
            "DECLARAN. `cerrar_reporte.py` gana un carril de CIERRE TARDIO, computado y "
            "no pasado por bandera, donde esas cifras no bloquean pero se declaran una a "
            "una con su linea y su cuenta total DENTRO del propio reporte cerrado. En el "
            "carril normal no cambia nada, y eso se comprueba con el arnes y no con la "
            "vista."),
    "7.3": ("CONTESTADA POR EL ACTA Y EJECUTADA EN LA TAREA 1.b DE ESTA VUELTA: el sujeto "
            "que faltaba es la vuelta 186, y va bloqueante. Sin ello la bateria de la 189 "
            "abriria en rojo por una omision medida con tres vueltas de antelacion."),
}


def _cabeza_de_la_entrada(numero, titulo, claves, pds, preguntas, estado_preg, cab7,
                          titulos, l_aud, l_rep, decl_vieja, decl_nueva,
                          inicio, fin, viejas_adj, viejas_eje, viejas_aud,
                          viejas_aud_prosa):
    """LA PRIMERA MITAD DE LA ENTRADA: la cabecera, los cinco numerales del
    titulo, el reparto de la seccion 6 y las dos familias de caidas con sus
    patrones viejos al lado. Va separada de la segunda mitad solo por tamano;
    las dos son PURAS y las dos reciben lo ya medido."""
    p = []
    p.append("## R.%d. %s" % (numero, titulo))
    p.append("")
    p.append("(Acta del auditor, vuelta %d, secciones 4, 5, 6, 7, 8, 9, 10, 11 y 12;"
             % VUELTA_DEL_ACTA)
    p.append("escrito en la vuelta %d, TAREA 1.a.)" % VUELTA_QUE_ESCRIBE)
    p.append("")
    p.append("Por adicion, como `R.21` a `R.47`. **Corte de todas las cifras de esta")
    p.append("entrada: 6 sep 2026.** El numero de esta entrada NO esta tecleado: lo computa")
    p.append("`scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS sedes.")
    p.append("La SEDE tampoco se supone: sale de la adjudicacion 6.3 del acta 162, que es")
    p.append("la que citan los `R.30` a `R.47`. Salida:")
    p.append("`docs/loop/SALIDA_V%s_T1A_REGISTRO_R%d.txt`."
             % (SUFIJO_QUE_ESCRIBE, numero))
    p.append("")
    p.append("**ESTA ENTRADA SE ESCRIBE CON LA TAREA 1 EN CURSO Y LA TAREA 2 SIN CORRER,")
    p.append("ASI QUE SUS GLOSAS NO AFIRMAN EN PASADO LO QUE TODAVIA NO HA PASADO.** Es la")
    p.append("forma que la `6.4` del acta 172 adjudico como correcta: donde una glosa dice")
    p.append("EJECUTADA, la prueba va nombrada con su fichero de salida; donde dice que va")
    p.append("a ejecutarse, se dice que **todavia no ha corrido** y no se disfraza.")
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
    p.append("**LAS SIETE ADJUDICACIONES SON A FAVOR, LAS SIETE.** El acta no regatea")
    p.append("ninguna.")
    p.append("")
    p.append("**LA SECCION 6 NO TIENE CUATRO PENDIENTES: TIENE CUATRO NUMERALES, Y UNO DE")
    p.append("ELLOS NO ES UN PENDIENTE.** El reparto por estado sale de leer el titulo")
    p.append("literal de cada uno y NO se teclea: **%s**."
             % ("; ".join("%s %s %s" % (c, pd, est) for c, pd, est, _l, _t in pds)))
    p.append("El `6.4` es una **ANOTACION** porque el propio acta escribe que *\"no lo")
    p.append("encargo y no lo adjudico\"*: es trabajo de plan, tiene sede en el archivo, y")
    p.append("convertirlo en pendiente propio seria publicar una cifra falsa de")
    p.append("pendientes. **El titulo cuenta los CUATRO numerales, que es lo que el acta")
    p.append("trae, y el reparto va aqui con su nombre.**")
    p.append("")
    p.append("**EL CONTRASTE QUE PRUEBA QUE LOS PATRONES SE MIDEN Y NO SE SUPONEN.** El")
    p.append("patron SIN comillas inversas, el del acta 183, corrido sobre esta acta da")
    p.append("**%d**. Se conserva intacto y su cero se publica: **se anaden patrones, no se"
             % viejas_adj)
    p.append("ensancha el viejo hasta que trague**.")
    p.append("")
    p.append("**CERO CAIDAS PROPIAS DEL AUDITOR, Y EL CERO VA CONTADO Y NO OMITIDO.** El")
    p.append("patron `A.n` de cabecera de tercer nivel, el que el acta 185 estreno, da")
    p.append("**%d** sobre esta acta. Los dos patrones `C.n` de las actas anteriores se"
             % len(l_aud))
    p.append("corren igual y dan **%d** (patron de linea) y **%d** (patron de negrita de"
             % (viejas_aud, viejas_aud_prosa))
    p.append("frase). **Un cero que sale de un patron que no muerde no es evidencia de")
    p.append("nada**, asi que va con la declaracion del acta al lado: la frase")
    p.append("`%s`, que es la del acta 186, aparece en **%d linea(s)**"
             % (FRASE_CERO_CAIDAS_PROPIAS, len(decl_nueva)))
    p.append("(`docs/loop/ACTA_AUDITOR.md:%s`), y la frase `%s`, que era la"
             % (", ".join(str(x) for x in decl_nueva) or "ninguna",
                FRASE_SIN_CAIDA_PROPIA))
    p.append("del acta 185, aparece en **%d**. **Un cero contado y un campo ausente no son"
             % len(decl_vieja))
    p.append("lo mismo, y por eso este registro lleva el cero escrito en vez de callarse")
    p.append("el campo.**")
    p.append("")
    p.append("**LA CAIDA DEL EJECUTOR SE LLAMA `R.n` Y ES DE REPORTE.** El patron de `E.n`,")
    p.append("el que mordio en las actas 182 y 184, corrido sobre esta da **%d**. Las dos"
             % viejas_eje)
    p.append("cifras se publican y ninguna se resuelve copiando.")
    p.append("")
    return p

def armar_entrada(numero, titulo, claves, pds, preguntas, estado_preg, cab7,
                  titulos, l_aud, l_rep, decl_vieja, decl_nueva, inicio, fin,
                  viejas_adj, viejas_eje, viejas_aud, viejas_aud_prosa,
                  puestos_pd1, salto):
    """LA ENTRADA ENTERA. PURA: recibe todo lo ya medido y no lee ni escribe."""
    faltan, bajo, alto = salto
    p = _cabeza_de_la_entrada(numero, titulo, claves, pds, preguntas,
                              estado_preg, cab7, titulos, l_aud, l_rep,
                              decl_vieja, decl_nueva, inicio, fin, viejas_adj,
                              viejas_eje, viejas_aud, viejas_aud_prosa)
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
    p.append("TECLEADO.** El estado sale de buscar `%s`, `%s` o `%s` en el"
             % (MARCA_ANOTACION, MARCA_ABIERTA, MARCA_CERRADA))
    p.append("titulo literal, en ese orden.")
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
    p.append("registrarlas como contestadas. **Las tres eran del auditor y las contesta el")
    p.append("auditor.**")
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
    p.append("el propio titulo declara ABIERTO. **Son %d puestos: %s.** Es la QUINTA"
             % (len(puestos_pd1),
                ", ".join(str(x) for x in puestos_pd1) or "(ninguno)"))
    p.append("vuelta que la `PD.1` sigue abierta, y el acta dice que darles cola seria")
    p.append("doctrina nueva, o sea del fundador.")
    p.append("")
    p.append("**LA CAIDA DE REPORTE `R.1`, EN LA LINEA %s, Y NO ACUMULA.**"
             % (", ".join(str(x) for x in l_rep) or "(ninguna)"))
    p.append("El reporte de la 185 escribio en su seccion 4 que el arbol abrio *\"con `git")
    p.append("status --porcelain` en cero lineas\"*, y su propia apertura sellada,")
    p.append("`docs/loop/SALIDA_V185_APERTURA.txt` bloque C, dice **`CIFRA lineas de")
    p.append("status: 2`**. La prediccion del docstring era buena cuando se escribio; lo")
    p.append("falso es la frase que le atribuye al bloque C una medicion que el bloque C")
    p.append("contradice. Por la letra afinada del 27 ago 2026 **NO ACUMULA**, porque vive")
    p.append("en la prosa de acompanamiento y no en una tabla, ni en la cabecera, ni en la")
    p.append("conclusion de su seccion, que era cierta. **La racha de reporte se mantiene")
    p.append("en 2**, y a partir de dos `AUDITOR.md` 1.2 es mandatorio: el acta encarga la")
    p.append("escalada en codigo y esta vuelta la ejecuta en la **TAREA 2.d**.")
    p.append("")
    p.append("**LA DEUDA DE LA SERIE, QUE SIGUE DOCUMENTADA COMO SALTO Y SIN RELLENAR.**")
    p.append("Se vuelve a medir en esta vuelta en vez de heredarse del `R.47`:")
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
    p.append("el desfase del acta `VUELTA - 1` **queda encargado y sin ejecutar**, porque")
    p.append("el regimen 6.2 deja esta vuelta en dos sub-tareas; la **mesa de los tres")
    p.append("nodos de la puerta del `PMF`** del `6.4` **no se abre aqui**; y el TRAMO 1 de")
    p.append("la cola post fusion, el par **2.464**, **no se relee aqui**: el encargo lo")
    p.append("pone a la cabeza de la vuelta 187, y esta vez con el tope en cinco si esta")
    p.append("vuelta cierra su reporte.")
    return NL.join(p) + NL


def _acta_fabricada(n_adj, n_pd, n_preg, caidas_aud, caidas_rep,
                    declara_cero=False, puestos=(11, 22, 33),
                    contesta=True, con_anotacion=True):
    """UN ACTA DE MENTIRA para el caso positivo por mutacion. NO toca el repo.

    Escribe los numerales de las secciones 5, 6 y 7 ENTRE COMILLAS INVERSAS, que
    es la forma del acta 186; la caida propia del auditor como cabecera de tercer
    nivel con `A.n`; y la caida del ejecutor como ``**`R.n`.`` al principio de
    linea. El ULTIMO `6.n` es la ANOTACION cuando `con_anotacion`, y el anterior
    es el que SIGUE ABIERTA con sus puestos, que es la forma del acta 186."""
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
    abierto = n_pd - 1 if (con_anotacion and n_pd >= 2) else n_pd
    for k in range(1, n_pd + 1):
        if con_anotacion and k == n_pd and n_pd >= 2:
            L += ["**`6.%d` Y ANOTO UN PENDIENTE QUE NO ES MIO Y %s:** de mentira."
                  % (k, MARCA_ANOTACION), "", "Y su cuerpo.", ""]
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
    L += ["## 8. LA CAIDA DE REPORTE", ""]
    for k in range(1, caidas_rep + 1):
        L += ["**`R.%d`. UNA CAIDA DE MENTIRA.** Y su cuerpo." % k, ""]
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

    Se fabrica un acta con OTRAS cifras, se corre el contador de verdad sobre
    ella, y se exige que las cifras y el titulo CAMBIEN con ella. Despues se muta
    el valor esperado y se comprueba que el caso CAE: si no cayera, el caso no
    probaria nada. NINGUNA COMPARACION DE AQUI ES ENTRE DOS CONSTANTES, Y EL
    SUJETO ES SIEMPRE UN ACTA FABRICADA, NUNCA LA REAL."""
    sys.stdout.reconfigure(encoding="utf-8")
    salida = []
    w = salida.append
    w("CASO POSITIVO POR MUTACION de vuelta186_tarea1a_registrar_acta186.py")
    w("EL SUJETO ES UN ACTA FABRICADA, NUNCA LA REAL.")
    w("")
    fallos = 0
    casos = [(7, 4, 3, 0, 1), (1, 2, 1, 0, 0), (12, 3, 5, 3, 2), (4, 2, 2, 1, 0)]
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
        rep = cuenta_por_patron(lineas, ini, fin, PAT_CAIDA_REPORTE)
        ok = (len(cl) == n_adj and len(pd) == n_pd and len(pr) == n_preg
              and len(aud) == n_aud and len(rep) == n_rep)
        titulo = titulo_de_la_entrada(len(cl), len(pd), len(pr), len(aud), len(rep))
        w("   acta fabricada con adj=%d pd=%d preg=%d aud=%d rep=%d"
          % (n_adj, n_pd, n_preg, n_aud, n_rep))
        w("      los contadores dicen adj=%d pd=%d preg=%d aud=%d rep=%d -> %s"
          % (len(cl), len(pd), len(pr), len(aud), len(rep),
             "CALZA" if ok else "NO CALZA"))
        w("      titulo computado: %s" % titulo)
        if not ok:
            fallos += 1
    w("")
    w("LA MUTACION DEL VALOR ESPERADO, QUE ES LO QUE PRUEBA QUE EL CASO PUEDE CAER:")
    texto = _acta_fabricada(7, 4, 3, 0, 1, declara_cero=True)
    lineas, (ini, fin), _e = cuerpo_del_acta(texto)
    medido = len(claves_entrecomilladas(lineas, ini, fin, PREFIJO_ADJ))
    for esperado in (7, 8):
        w("   con el esperado %d: %s" % (esperado, "PASA" if medido == esperado else "CAE"))
    cae = medido != 8
    w("   medido sobre el acta fabricada (variable computada): %d" % medido)
    w("   EL CASO CAE AL MUTAR EL ESPERADO A 8: %s" % ("SI" if cae else "NO"))
    if not cae:
        fallos += 1
    w("")
    w("LA SEGUNDA MUTACION: LAS PREGUNTAS DE LA SECCION 7, QUE NINGUN REGISTRADOR")
    w("ANTERIOR CUENTA. Si el contador del prefijo 7. no contara de verdad, este")
    w("caso no podria cambiar con el acta.")
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
    w("   patron sin comillas sobre acta en forma 186 -> %d adjudicaciones" % con_viejo)
    w("   EL CASO CAE CON EL PATRON VIEJO: %s" % ("SI" if con_viejo == 0 else "NO"))
    if con_viejo != 0:
        fallos += 1
    w("")
    w("LA CUARTA MUTACION: EL TERCER ESTADO. El ULTIMO numeral de la seccion 6 del")
    w("acta fabricada es una ANOTACION y NO un pendiente. Con el registrador de la")
    w("185, que solo sabia ABIERTA y CERRADA, ese titulo habria salido SIN DECIR y")
    w("el instrumento habria hecho PARADA. Aqui tiene que salir ANOTACION.")
    tit_pd, _e4 = _titulos_de(lineas, ini, fin, PREFIJO_PD)
    estados = [(c, pd, e) for c, pd, e, _l, _t
               in pendientes_de_doctrina(lineas, ini, fin, tit_pd)]
    w("   estados computados: %s" % estados)
    n_anot = len([1 for _c, _p, e in estados if e == "ANOTACION"])
    n_abier = len([1 for _c, _p, e in estados if e == "ABIERTA"])
    n_cerr = len([1 for _c, _p, e in estados if e == "CERRADA"])
    n_sin = len([1 for _c, _p, e in estados if e == "SIN DECIR"])
    ok_est = (n_anot == 1 and n_abier == 1 and n_cerr == 2 and n_sin == 0)
    w("   ANOTACION %d | ABIERTA %d | CERRADA %d | SIN DECIR %d | esperado 1, 1, 2, 0 -> %s"
      % (n_anot, n_abier, n_cerr, n_sin, "CALZA" if ok_est else "NO CALZA"))
    w("   con el esperado MUTADO (0 anotaciones): %s"
      % ("PASA" if n_anot == 0 else "CAE"))
    if not ok_est or n_anot == 0:
        fallos += 1
    sin_anot = _acta_fabricada(7, 4, 3, 0, 1, con_anotacion=False)
    l5, (i5, f5), _e5 = cuerpo_del_acta(sin_anot)
    t5, _z5 = _titulos_de(l5, i5, f5, PREFIJO_PD)
    est5 = [e for _c, _p, e, _l, _t in pendientes_de_doctrina(l5, i5, f5, t5)]
    w("   y sobre un acta SIN anotacion, para que se vea que el estado no esta")
    w("   clavado: %s" % est5)
    if "ANOTACION" in est5:
        w("   LA ANOTACION APARECE DONDE NO LA HAY: NO")
        fallos += 1
    w("")
    return salida, fallos, lineas, ini, fin

def _mutacion_segunda_mitad():
    """LA SEGUNDA MITAD DEL CASO POSITIVO POR MUTACION. Va separada de la
    primera solo por tamano, y la cuenta de fallos es UNA SOLA que atraviesa las
    tres mitades: cada una recibe la cuenta de la anterior y la devuelve."""
    salida, fallos, lineas, ini, fin = _mutacion_primera_mitad()
    w = salida.append
    w("LA QUINTA MUTACION: EL PATRON `C.n` DE LAS ACTAS ANTERIORES Y EL `A.n` SOBRE")
    w("UN ACTA CON CERO CAIDAS PROPIAS. LOS DOS tienen que dar CERO, y el acta tiene")
    w("que DECLARARLO con su frase para que el cero sea evidencia y no ausencia.")
    aud_nuevo = len(cuenta_por_patron(lineas, ini, fin, PAT_CAIDA_AUDITOR_A))
    aud_viejo = len(cuenta_por_patron(lineas, ini, fin, PAT_CAIDA_AUDITOR_VIEJO))
    d_vieja, d_nueva = lineas_que_declaran_cero_caidas(lineas, ini, fin)
    w("   patron `A.n` -> %d | patron `C.n` -> %d" % (aud_nuevo, aud_viejo))
    w("   frase del acta 186 (%r) -> %d linea(s) | frase del acta 185 (%r) -> %d"
      % (FRASE_CERO_CAIDAS_PROPIAS, len(d_nueva),
         FRASE_SIN_CAIDA_PROPIA, len(d_vieja)))
    ok_aud = (aud_nuevo == 0 and aud_viejo == 0 and len(d_nueva) == 1
              and len(d_vieja) == 0)
    w("   EL CERO VA CONTADO Y DECLARADO: %s" % ("SI" if ok_aud else "NO"))
    w("   con el esperado MUTADO (1 caida propia): %s"
      % ("PASA" if aud_nuevo == 1 else "CAE"))
    if not ok_aud or aud_nuevo == 1:
        fallos += 1
    con_caida = _acta_fabricada(7, 4, 3, 2, 1)
    l6, (i6, f6), _e6 = cuerpo_del_acta(con_caida)
    n6 = len(cuenta_por_patron(l6, i6, f6, PAT_CAIDA_AUDITOR_A))
    w("   y sobre un acta CON dos caidas propias, para que se vea que el contador")
    w("   no esta clavado en cero: patron `A.n` -> %d" % n6)
    if n6 != 2:
        fallos += 1
    w("")
    w("LA SEXTA MUTACION: EL PATRON `E.n` SOBRE UNA CAIDA ESCRITA COMO `R.n`.")
    rep_nuevo = len(cuenta_por_patron(lineas, ini, fin, PAT_CAIDA_REPORTE))
    rep_viejo = len(cuenta_por_patron(lineas, ini, fin, PAT_CAIDA_EJECUTOR_VIEJO))
    w("   patron `R.n` -> %d | patron `E.n` -> %d" % (rep_nuevo, rep_viejo))
    ok_rep = (rep_nuevo == 1 and rep_viejo == 0)
    w("   EL NUEVO MUERDE Y EL VIEJO NO: %s" % ("SI" if ok_rep else "NO"))
    if not ok_rep:
        fallos += 1
    w("")
    w("LA SEPTIMA MUTACION: EL ESTADO DE LAS PREGUNTAS, LEIDO DE LA CABECERA DE SU")
    w("SECCION Y NO SUPUESTO. Un acta que pregunta y NO dice que contesta tiene que")
    w("salir SIN DECIR, y el instrumento hace PARADA con ella.")
    tit_pr, _e7 = _titulos_de(lineas, ini, fin, PREFIJO_PREG)
    _lst, estado_si, ln7, cab7 = preguntas_de_la_seccion7(lineas, ini, fin, tit_pr)
    muda = _acta_fabricada(7, 4, 3, 0, 1, contesta=False)
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
    return salida, fallos, lineas, ini, fin

def prueba_de_mutacion():
    """EL CASO POSITIVO POR MUTACION, ENTERO Y CON UNA SOLA CUENTA DE FALLOS."""
    sys.stdout.reconfigure(encoding="utf-8")
    salida, fallos, lineas, ini, fin = _mutacion_segunda_mitad()
    w = salida.append
    w("LA OCTAVA MUTACION: LOS PUESTOS DE LA `PD.1`, LEIDOS DEL ACTA. Se fabrica un")
    w("acta con OTROS puestos y se exige que salgan LOS DEL ACTA y no los del")
    w("encargo. Si estuvieran tecleados, este caso no podria cambiar.")
    for inventados in ((11, 22, 33), (7, 8, 9, 10)):
        t2 = _acta_fabricada(7, 4, 3, 0, 1, puestos=inventados)
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
    t3 = _acta_fabricada(7, 4, 3, 0, 1, puestos=reales)
    l3, (i3, f3), _z3 = cuerpo_del_acta(t3)
    tit3, _e3 = _titulos_de(l3, i3, f3, PREFIJO_PD)
    leidos3 = puestos_de_la_pd1(l3, i3, f3, tit3)
    w("   y con los cinco que el encargo nombra -> leidos %s" % leidos3)
    w("   con el esperado MUTADO [1778, 2530, 2540, 3141, 9999]: %s"
      % ("PASA" if leidos3 == [1778, 2530, 2540, 3141, 9999] else "CAE"))
    if leidos3 == [1778, 2530, 2540, 3141, 9999]:
        fallos += 1
    w("")
    w("LA NOVENA MUTACION: EL SALTO. actas_sin_entrada() es PURA y se importa del")
    w("registrador de la 183; se le pasa una serie fabricada y se comprueba que el")
    w("salto y sus DOS extremos salen de los titulos y no de ninguna constante.")
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
    w("LA DECIMA MUTACION: EL TITULO Y SU CONCORDANCIA, INCLUIDO EL CERO.")
    t0 = titulo_de_la_entrada(7, 4, 3, 0, 1)
    w("   %s" % t0)
    ok_t = ("las siete adjudicaciones numeradas" in t0
            and "los cuatro numerales de la seccion 6" in t0
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
    ruta = os.path.join(LOOP, "SALIDA_V%s_T1A_MUTACION_REGISTRO_186.txt"
                        % SUFIJO_QUE_ESCRIBE)
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0 if fallos == 0 else 1


def _medir():
    """LA PRIMERA MITAD DE main(): acotar el acta y contar. Devuelve o bien un
    entero (codigo de salida, cuando hay PARADA) o bien la tupla de lo medido.
    Va separada solo por tamano."""
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

    w("D) LAS CAIDAS, POR SUS FAMILIAS, Y LOS PATRONES VIEJOS AL LADO")
    l_aud = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_AUDITOR_A)
    l_aud_v = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_AUDITOR_VIEJO)
    l_aud_p = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_AUDITOR_PROSA_VIEJO)
    l_rep = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_REPORTE)
    l_eje_v = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_EJECUTOR_VIEJO)
    decl_vieja, decl_nueva = lineas_que_declaran_cero_caidas(lineas, inicio, fin)
    w("   CAIDAS PROPIAS DEL AUDITOR (patron `A.n`, cabecera de tercer nivel): %d, lineas %s"
      % (len(l_aud), ", ".join(str(x) for x in l_aud) or "(ninguna)"))
    for i in l_aud:
        w("      LINEA %d: %s" % (i, lineas[i - 1].strip()[:130]))
    w("   EL PATRON `C.n` DE LINEA (actas 178 a 182): %d" % len(l_aud_v))
    w("   EL PATRON `C.n` DE NEGRITA DE FRASE (acta 184): %d" % len(l_aud_p))
    w("   CAIDAS DE REPORTE DEL EJECUTOR (patron `R.n`): %d, lineas %s"
      % (len(l_rep), ", ".join(str(x) for x in l_rep) or "(ninguna)"))
    for i in l_rep:
        w("      LINEA %d: %s" % (i, lineas[i - 1].strip()[:130]))
    w("   EL PATRON `E.n` DE LAS ACTAS 182 Y 184: %d" % len(l_eje_v))
    w("   LINEAS CON LA FRASE DEL ACTA 186 (%r): %s"
      % (FRASE_CERO_CAIDAS_PROPIAS,
         ", ".join(str(x) for x in decl_nueva) or "(ninguna)"))
    for i in decl_nueva:
        w("      LINEA %d: %s" % (i, lineas[i - 1].strip()[:130]))
    w("   LINEAS CON LA FRASE DEL ACTA 185 (%r): %s"
      % (FRASE_SIN_CAIDA_PROPIA,
         ", ".join(str(x) for x in decl_vieja) or "(ninguna)"))
    if not l_rep:
        w("   PARADA: el patron de caida de reporte no encuentra ninguna, y el acta")
        w("   186 declara una en su seccion 8. No se escribe una entrada asi.")
        print(NL.join(salida))
        return 1
    if not l_aud and not decl_nueva and not decl_vieja:
        w("   PARADA: cero caidas propias del auditor Y el acta no lo declara por")
        w("   ninguna de las dos frases. Un cero de un patron que no muerde no se")
        w("   publica como medicion.")
        print(NL.join(salida))
        return 1
    w("")
    return salida, lineas, inicio, fin, claves, claves_pd, claves_pr, \
        viejas_adj, l_aud, l_aud_v, l_aud_p, l_rep, l_eje_v, decl_vieja, decl_nueva


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
     l_aud, l_aud_v, l_aud_p, l_rep, l_eje_v, decl_vieja, decl_nueva) = medido
    w = salida.append

    w("E) EL TITULO, CON SUS CINCO NUMERALES COMPUTADOS")
    titulo = titulo_de_la_entrada(len(claves), len(claves_pd), len(claves_pr),
                                  len(l_aud), len(l_rep))
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
        w("   PARADA: %s no dice si cierra, sigue abierto o es anotacion."
          % ", ".join(sin_decir))
        print(NL.join(salida))
        return 1
    w("   REPARTO: CERRADAS %d | ABIERTAS %d | ANOTACIONES %d"
      % (len([1 for _c, _p, e, _l, _t in pds if e == "CERRADA"]),
         len([1 for _c, _p, e, _l, _t in pds if e == "ABIERTA"]),
         len([1 for _c, _p, e, _l, _t in pds if e == "ANOTACION"])))
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
        w("   PARADA: la cabecera de la seccion 7 no dice %r. Un acta que")
        w("   pregunta y no dice si contesta no se registra como si contestara."
          % MARCA_CONTESTADAS)
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

    w("J) LA DEUDA DE LA SERIE, REMEDIDA EN ESTA VUELTA Y NO HEREDADA DEL R.47")
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
                            len(l_eje_v), len(l_aud_v), len(l_aud_p),
                            puestos_pd1, salto)
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
