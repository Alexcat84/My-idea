# -*- coding: utf-8 -*-
r"""vuelta185_tarea1a_registrar_acta185.py . EL ACTA 185 ENTERA, REGISTRADA EN LA
SERIE `R.N` EN LA FORMA DE LA CASA.

LA MAQUINA NO SE CLONA, SE IMPORTA, y eso lo adjudico la `6.6` del acta 172 como
correcto y obligatorio: `PALABRA` y `titulo_de_la_negrita` se importan de
`scripts/loop/vuelta172_tarea1_registrar_acta171.py`, `claves_de_adjudicacion` y
`cuenta_por_patron` del registrador de la vuelta 182, `actas_sin_entrada` del de
la 183 y `claves_entrecomilladas` del de la 184. Lo unico propio de este fichero
es EL ACOTE DE SU ACTA, LOS PATRONES QUE SU ACTA NECESITA Y SUS GLOSAS.

POR QUE HACE FALTA CODIGO PROPIO OTRA VEZ, MEDIDO Y NO SUPUESTO, Y SON TRES COSAS:

  1) EL ACTA 185 NO TIENE UNA SOLA ADJUDICACION SIN NUMERAL: TIENE UNA SECCION 6
     ENTERA DE CUATRO PENDIENTES DE DOCTRINA, NUMERADOS ``**`6.1` `` a
     ``**`6.4` ``. El registrador de la 184 contaba UNA adjudicacion sin numeral
     con un patron de cabecera de seccion; aqui la seccion 6 numera sus cuatro
     entradas con la MISMA forma entrecomillada que la seccion 5, asi que el
     patron entrecomillado de la 184 SE IMPORTA Y SE REUSA con otro prefijo. NO
     se escribe un patron nuevo donde el viejo ya muerde.

  2) LA CAIDA PROPIA DEL AUDITOR SE LLAMA `A.n` Y NO `C.n`, Y VIVE EN UNA
     CABECERA `###`. El acta 185 la escribe *"### 2.1 MI CAIDA PROPIA `A.1`, Y ES
     DE NOMBRE"*, y ella misma la declara **especie nueva** en su seccion 9. Los
     patrones `C.n` de las actas anteriores SE CONSERVAN INTACTOS y su cifra
     sobre esta acta se publica al lado: un cero que prueba que hacia falta un
     patron nuevo vale mas que un patron ensanchado hasta que trague.

  3) LA CAIDA DEL EJECUTOR SE LLAMA `R.n` (caida de REPORTE) Y NO `E.n`. Se
     escribe ``**`R.1`. ...`` al principio de linea, que es la forma del `E.1`
     del acta 184 con otra letra. Se anade el patron, se conserva el de `E.n`, y
     LAS DOS CIFRAS SE PUBLICAN.

Y UNA CUARTA COSA QUE NO ES UN PATRON SINO UNA CIFRA: LOS CINCO PUESTOS DE LA
`PD.1` NO SE TECLEAN. El encargo los nombra (1778, 2530, 2540, 3141, 3232) y aqui
NO se copian: se leen del parrafo del `6.4` del acta con un patron, y si el acta
dijera otros, la entrada diria otros.

LAS CIFRAS DEL TITULO NO SE TECLEAN: se cuentan del acta acotada. Ni el numero de
la entrada: lo devuelve `scripts/loop/serie_de_registros.py` recomputando la serie
de sus DOS sedes. Y LA DEUDA DE LA SERIE SE REMIDE EN ESTA VUELTA y no se hereda
del `R.46`, que es lo que el encargo pide con esas palabras.

LO QUE ESTE FICHERO NO HACE: no toca el acta, no toca el reporte, no toca
`docs/plan/`, no corre la bateria y no escribe ningun veredicto. Escribe UNA
entrada en UNA sede, y si la entrada ya esta, NO la duplica y lo dice.

USO:
  python scripts/loop/vuelta185_tarea1a_registrar_acta185.py
  python scripts/loop/vuelta185_tarea1a_registrar_acta185.py --simular
  python scripts/loop/vuelta185_tarea1a_registrar_acta185.py --mutacion
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

VUELTA_DEL_ACTA = 185
VUELTA_QUE_ESCRIBE = 185
SUFIJO_QUE_ESCRIBE = "185"
CABECERA_ACTA = "# ACTA DEL AUDITOR, VUELTA %d" % VUELTA_DEL_ACTA
PREFIJO_ADJ = "5."
PREFIJO_PD = "6."

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
FRASE_SIN_CAIDA_PROPIA = "NINGUNA CAIDA PROPIA"

# EL PENDIENTE DE DOCTRINA QUE CADA `6.n` NOMBRA, y si lo CIERRA o lo deja
# ABIERTO. Las dos cosas se leen del titulo literal del acta y NO se teclean:
# el titulo del `6.4` dice "SIGUE ABIERTA" y los otros tres dicen "ADJUDICAD".
PAT_PD_DEL_TITULO = re.compile(r"`PD\.(\d+)`")
MARCA_ABIERTA = "SIGUE ABIERTA"
MARCA_CERRADA = "ADJUDICAD"


def cuerpo_del_acta(texto=None):
    """EL ACTA ACOTADA: (lineas, (inicio, fin), error). El fin es el final del
    fichero porque el acta 185 es la ultima escrita; si algun dia dejara de
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
    todas las letras son la misma cifra y NO son la misma evidencia. En el acta
    185 esto tiene que dar CERO, porque el auditor SI declara una caida propia."""
    return [i for i in range(inicio, fin + 1)
            if FRASE_SIN_CAIDA_PROPIA in lineas[i - 1]]


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
    """LOS PENDIENTES DE DOCTRINA DE LA SECCION 6, CON SU ESTADO LEIDO DEL
    TITULO. Devuelve [(clave, pd, estado, linea, titulo)]. PURA.

    EL ESTADO NO SE TECLEA: sale de buscar `SIGUE ABIERTA` o `ADJUDICAD` en el
    titulo literal del acta. Si un titulo no dijera ninguna de las dos cosas, el
    estado sale como `SIN DECIR` y el instrumento hace PARADA en vez de suponer."""
    salida = []
    for clave, _n in claves_entrecomilladas(lineas, inicio, fin, PREFIJO_PD):
        ln, tit = titulos[clave]
        m = PAT_PD_DEL_TITULO.search(tit)
        pd = ("PD.%s" % m.group(1)) if m else "(sin PD en el titulo)"
        if MARCA_ABIERTA in tit:
            estado = "ABIERTA"
        elif MARCA_CERRADA in tit:
            estado = "CERRADA"
        else:
            estado = "SIN DECIR"
        salida.append((clave, pd, estado, ln, tit))
    return salida


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
        m = re.search(r"\bson\s+\*\*([0-9,\sy]+)\*\*", parrafo)
        if not m:
            return []
        return [int(x) for x in re.findall(r"\d+", m.group(1))]
    return []


def titulo_de_la_entrada(n_adj, n_pd, n_cai_aud, n_cai_rep):
    """El titulo, con sus CUATRO numerales COMPUTADOS y no tecleados, y con la
    concordancia dentro del computo. El CERO entra por `PALABRA_CON_CERO`, y va
    en plural porque en castellano el cero es plural."""
    def trozo(n, sing, plur):
        if n == 1:
            return "la %s" % sing
        return "las %s %s" % (PALABRA_CON_CERO[n], plur)

    def trozo_m(n, sing, plur):
        if n == 1:
            return "el %s" % sing
        return "los %s %s" % (PALABRA_CON_CERO[n], plur)
    return ("Registro de %s, %s, %s del auditor y %s de reporte del "
            "ejecutor del acta de la vuelta %d"
            % (trozo(n_adj, "adjudicacion numerada", "adjudicaciones numeradas"),
               trozo_m(n_pd, "pendiente de doctrina", "pendientes de doctrina"),
               trozo(n_cai_aud, "caida propia", "caidas propias"),
               trozo(n_cai_rep, "caida", "caidas"),
               VUELTA_DEL_ACTA))


VIA = {
    "5.1": "SIN TOCAR NADA",
    "5.2": "SIN TOCAR NADA",
    "5.3": "SIN TOCAR NADA",
    "5.4": "SIN TOCAR NADA",
    "5.5": "SIN TOCAR NADA",
    "5.6": "SIN TOCAR NADA",
    "5.7": "SIN TOCAR NADA",
    "6.1": "SIN TOCAR NADA",
    "6.2": "EJECUTADA",
    "6.3": "SIN TOCAR NADA",
    "6.4": "SIN TOCAR NADA",
}

QUE_HACE_ESTA_VUELTA = {
    "5.1": ("SE ACATA SIN TOCAR NADA. El acta lee *mismo calibre* como HONDURA y no "
            "como resultado, citando las palabras de `AUDITOR.md` 6.1, y componer con "
            "el tramo 9 en rojo dentro queda adjudicado a favor. No hay trabajo "
            "pendiente en ella: la bateria ya esta compuesta y su rojo publicado."),
    "5.2": ("SE ACATA A FAVOR, Y SU REPARACION SE DECLARA COMO COLA Y NO SE DISFRAZA "
            "DE HECHA. El acta concede el desfase declarado y encarga como cambio de "
            "una linea que el esqueleto y el tallador nombren el acta de la vuelta N y "
            "no la N-1. ESTA VUELTA NO LO EJECUTA: su encargo trae DOS sub-tareas por "
            "el regimen 6.2 y ninguna de las dos es esta. Queda nombrada aqui para que "
            "no se pierda."),
    "5.3": ("SE ACATA SIN TOCAR NADA. Renombrar el caso cuyo nombre llevaba dentro la "
            "cifra caducada queda adjudicado como el remedio y no como una desviacion "
            "del remedio."),
    "5.4": ("SE ACATA SIN TOCAR NADA, Y CON EL RIESGO QUE EL ACTA DEJA ESCRITO. El "
            "esperado computado se concede PORQUE EL CASO HERMANO EXISTE, el de "
            "`LOS_DOS_DE_LA_165`, que no se recompone solo. Si ese hermano se borrara, "
            "el arnes quedaria probando su propio reflejo. Esta vuelta no toca ninguno "
            "de los dos."),
    "5.5": ("SE ACATA SIN TOCAR NADA, Y EL ACTA RESUELVE LA DUDA EN VEZ DE ENCARGARLA. "
            "La lesion exacta del puesto 3.141 ya estaba registrada desde la vuelta "
            "182: pasa las condiciones 1 y 2 y falla la 3, o sea que NO es un "
            "diferenciador movido, y su sede es la `PD.1`. No hace falta encargar "
            "nada."),
    "5.6": ("SE ACATA SIN TOCAR NADA. El arnes que entra a la nomina en su misma vuelta "
            "queda concedido por el acta 176 punto 7.2, reconfirmada por la `5.6` del "
            "acta 184, y la medicion lo respalda: sin el, `arneses_que_faltan()` daba "
            "1."),
    "5.7": ("SE ACATA SIN TOCAR NADA, Y EL ACTA LA CONVIERTE EN REGLA POR EXTENSION. "
            "Cuando el cierre del reporte caiga en rojo, los discutibles, las preguntas "
            "y las caidas propias SE ANEXAN A LA ULTIMA TAREA QUE SI CERRO, y el "
            "reporte lo dice en esa sede. Esta vuelta no necesita aplicarla, porque su "
            "cierre no cae en rojo, pero queda escrita."),
    "6.1": ("`PD.2` CERRADA POR CITA, SIN TOCAR NADA. El calibre de un tramo en rojo lo "
            "resuelve `AUDITOR.md` 6.1 con sus propias palabras: *calibre es hondura*, "
            "y la unica descalificacion que esa seccion nombra es la del vacio. No es "
            "doctrina nueva y no queda trabajo."),
    "6.2": ("`PD.3` CERRADA POR CITA, Y ES LA UNICA ADJUDICACION DEL ACTA QUE MANDA "
            "TOCAR CODIGO. EJECUTADA EN LA TAREA 1.c DE ESTA VUELTA. El rojo de "
            "`cerrar_reporte.py` sobre el reporte de la 184 queda declarado FALSO ROJO: "
            "la guarda nacio contra pedir prestada la bateria terminada de otra vuelta, "
            "y una bateria que RETOMA EN EL TRAMO SIGUIENTE cruza vueltas POR DISENO, "
            "que es lo que la decision del fundador del 5 sep 2026 pide. Por "
            "`AUDITOR.md` 0, cuando una guarda contradice una decision escrita del "
            "fundador, la que se corrige es la guarda. LA REPARACION EXIGE MAS QUE LA "
            "GUARDA VIEJA Y NO MENOS: cuatro condiciones a la vez, y la evidencia se "
            "computa de `git log` y NO se puede pasar por bandera. La prueba vive en "
            "`docs/loop/SALIDA_V185_T1C_MUTACION_BATERIA_CONTINUADA.txt`."),
    "6.3": ("`PD.4` CERRADA POR EXTENSION, SIN TOCAR NADA. Una entrada de la nomina que "
            "nunca ha aparecido en una bateria COMPLETA no esta probada, y el rojo de "
            "su primera bateria completa es un hallazgo SOBRE EL ARNES y no sobre la "
            "bateria. Es exactamente lo que paso con "
            "`vuelta182_tarea2_mutacion_apertura_auditor.py`, y su reparacion va en la "
            "TAREA 1.b de esta vuelta."),
    "6.4": ("`PD.1` SIGUE ABIERTA Y ESTA VUELTA NO LA CIERRA NI LA ENCARGA. Lo que "
            "cambia es que deja de ser una lista sin nombres: sus cinco puestos quedan "
            "escritos en el acta y en esta entrada. El acta dice con todas las letras "
            "que darles cola seria doctrina nueva y eso es del fundador."),
}


def armar_entrada(numero, titulo, claves, pds, titulos, l_aud, l_rep,
                  l_declara, inicio, fin, viejas_adj, viejas_eje, viejas_aud,
                  viejas_aud_prosa, puestos_pd1, salto):
    faltan, bajo, alto = salto
    p = []
    p.append("## R.%d. %s" % (numero, titulo))
    p.append("")
    p.append("(Acta del auditor, vuelta %d, secciones 2, 4, 5, 6, 7, 8 y 9; escrito en"
             % VUELTA_DEL_ACTA)
    p.append("la vuelta %d, TAREA 1.a.)" % VUELTA_QUE_ESCRIBE)
    p.append("")
    p.append("Por adicion, como `R.21` a `R.46`. **Corte de todas las cifras de esta")
    p.append("entrada: 6 sep 2026.** El numero de esta entrada NO esta tecleado: lo computa")
    p.append("`scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS sedes.")
    p.append("La SEDE tampoco se supone: sale de la adjudicacion 6.3 del acta 162, que es")
    p.append("la que citan los `R.30` a `R.46`. Salida:")
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
    p.append("seccion 5), %d pendientes de doctrina (`6.1` a `6.%d`, todos en la seccion"
             % (len(pds), len(pds)))
    p.append("6), %d caida propia del auditor y %d caida de reporte del ejecutor.**"
             % (len(l_aud), len(l_rep)))
    p.append("")
    p.append("**LA SECCION 6 NUMERA SUS PENDIENTES Y POR ESO SE CUENTAN CON EL MISMO")
    p.append("PATRON QUE LA 5, NO CON UNO NUEVO.** El registrador de la 184 contaba UNA")
    p.append("adjudicacion sin numeral con un patron de cabecera de seccion, porque su")
    p.append("acta la escribia asi; el acta 185 numera ``**`6.1` `` a ``**`6.4` `` con la")
    p.append("forma entrecomillada de su seccion 5, asi que `claves_entrecomilladas` se")
    p.append("IMPORTA del registrador de la 184 y se corre con otro prefijo. **No se")
    p.append("escribe un patron nuevo donde el viejo ya muerde**, que es la otra mitad de")
    p.append("la misma doctrina.")
    p.append("")
    p.append("**EL CONTRASTE QUE PRUEBA QUE LOS PATRONES SE MIDEN Y NO SE SUPONEN.** El")
    p.append("patron SIN comillas inversas, el del acta 183, corrido sobre esta acta da")
    p.append("**%d**. Se conserva intacto y su cero se publica: **se anaden patrones, no se"
             % viejas_adj)
    p.append("ensancha el viejo hasta que trague**.")
    p.append("")
    p.append("**LA CAIDA PROPIA DEL AUDITOR SE LLAMA `A.n` Y ES ESPECIE NUEVA, DICHA POR")
    p.append("EL PROPIO ACTA.** Vive en una cabecera `###` (`docs/loop/ACTA_AUDITOR.md:%s`)"
             % (", ".join(str(x) for x in l_aud) or "(ninguna)"))
    p.append("y no en una negrita de lista. Los dos patrones `C.n` de las actas anteriores")
    p.append("se corren igual y dan **%d** (patron de linea) y **%d** (patron de negrita de"
             % (viejas_aud, viejas_aud_prosa))
    p.append("frase). **Un cero que sale de un patron que no muerde no es evidencia de")
    p.append("nada, y por eso va con el patron que si muerde al lado.** La linea del acta")
    p.append("que declara *\"%s\"*: **%s aparicion(es)**, que es lo que"
             % (FRASE_SIN_CAIDA_PROPIA, len(l_declara)))
    p.append("tiene que dar un acta que **si** tuvo una caida propia.")
    p.append("")
    p.append("**LA CAIDA DEL EJECUTOR SE LLAMA `R.n` Y ES DE REPORTE.** El patron de `E.n`,")
    p.append("el que mordio en las actas 182 y 184, corrido sobre esta da **%d**. Las dos"
             % viejas_eje)
    p.append("cifras se publican y ninguna se resuelve copiando.")
    p.append("")
    p.append("**LAS %s ADJUDICACIONES NUMERADAS, CON SU LINEA EN EL ACTA LEIDA HOY.** El"
             % PALABRA_CON_CERO[len(claves)].upper())
    p.append("titulo de cada una es LITERAL del fichero; la glosa que sigue es prosa del")
    p.append("ejecutor y va marcada como tal. **Las siete son A FAVOR.**")
    p.append("")
    for clave, _n in claves:
        ln, tit = titulos[clave]
        p.append("  - **`%s` (`docs/loop/ACTA_AUDITOR.md:%d`, leida hoy). VIA: %s.** Titulo"
                 % (clave, ln, VIA[clave]))
        p.append("    literal del acta: *\"%s\"*" % tit)
        p.append("    **QUE HACE ESTA VUELTA CON ELLA (glosa del ejecutor, no del acta):** %s"
                 % QUE_HACE_ESTA_VUELTA[clave])
    p.append("")
    p.append("**LOS %s PENDIENTES DE DOCTRINA DE LA SECCION 6, CON SU ESTADO LEIDO DEL"
             % PALABRA_CON_CERO[len(pds)].upper())
    p.append("TITULO Y NO TECLEADO.** El estado sale de buscar `%s` o `%s` en el"
             % (MARCA_ABIERTA, MARCA_CERRADA))
    p.append("titulo literal: **%s** y **%s**."
             % (", ".join("%s %s" % (pd, est) for _c, pd, est, _l, _t in pds
                          if est == "CERRADA") or "(ninguno cerrado)",
                ", ".join("%s %s" % (pd, est) for _c, pd, est, _l, _t in pds
                          if est == "ABIERTA") or "(ninguno abierto)"))
    p.append("")
    for clave, pd, estado, ln, tit in pds:
        p.append("  - **`%s`, que nombra `%s`, estado %s (`docs/loop/ACTA_AUDITOR.md:%d`,"
                 % (clave, pd, estado, ln))
        p.append("    leida hoy). VIA: %s.** Titulo literal del acta: *\"%s\"*"
                 % (VIA[clave], tit))
        p.append("    **QUE HACE ESTA VUELTA CON EL (glosa del ejecutor, no del acta):** %s"
                 % QUE_HACE_ESTA_VUELTA[clave])
    p.append("")
    p.append("**LOS CINCO PUESTOS DE LA `PD.1`, LEIDOS DEL ACTA Y NO TECLEADOS.** El")
    p.append("encargo los nombra y aqui NO se copian: salen del parrafo del pendiente que")
    p.append("el propio titulo declara ABIERTO. **Son %d puestos: %s.** Es la novedad de"
             % (len(puestos_pd1),
                ", ".join(str(x) for x in puestos_pd1) or "(ninguno)"))
    p.append("este registro sobre el `R.46`: la `PD.1` deja de ser una lista sin nombres.")
    p.append("")
    p.append("**LA CAIDA DE REPORTE `R.1`, EN LA LINEA %s, Y NO ACUMULA.**"
             % (", ".join(str(x) for x in l_rep) or "(ninguna)"))
    p.append("Es la columna `quien lo sello` de la tabla de los nueve tramos, **tecleada")
    p.append("con un `n <= 4` debajo de una frase del reporte que dice que la tabla sale de")
    p.append("contar sus ficheros *\"y no de recordar nada\"*. **Los valores son correctos")
    p.append("hoy** (el auditor los verifico uno a uno con `git log`), **y lo equivocado es")
    p.append("la frase de procedencia**, que vive en prosa. Por la letra afinada del 27 ago")
    p.append("2026, **NO ACUMULA**, y **la racha de reporte se mantiene en 2**. Pero un")
    p.append("`n <= 4` tecleado **es una frontera que caduca**, asi que el acta encarga la")
    p.append("escalada en codigo y esta vuelta la ejecuta en la **TAREA 1.d**.")
    p.append("")
    p.append("**LA DEUDA DE LA SERIE, QUE SIGUE DOCUMENTADA COMO SALTO Y SIN RELLENAR.**")
    p.append("Se vuelve a medir en esta vuelta en vez de heredarse del `R.46`:")
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
    p.append("el desfase del acta `VUELTA - 1` de la `5.2` **queda encargado y sin")
    p.append("ejecutar**, porque el regimen 6.2 deja esta vuelta en dos sub-tareas; y el")
    p.append("TRAMO 1 de la cola post fusion, el par **2.464**, **no se relee aqui**: el")
    p.append("encargo lo pone a la cabeza de la vuelta 186.")
    return NL.join(p) + NL


def _acta_fabricada(n_adj, n_pd, caidas_aud, caidas_rep, declara_cero=False,
                    puestos=(11, 22, 33)):
    """UN ACTA DE MENTIRA para el caso positivo por mutacion. NO toca el repo.

    Escribe los numerales de las secciones 5 y 6 ENTRE COMILLAS INVERSAS, que es
    la forma del acta 185; la caida propia del auditor como cabecera `###` con
    `A.n`; y la caida del ejecutor como ``**`R.n`.`` al principio de linea. Las
    tres cosas son exactamente las que este fichero existe para cubrir."""
    L = ["# ACTA DEL AUDITOR, VUELTA %d (fabricada)" % VUELTA_DEL_ACTA, ""]
    if declara_cero and caidas_aud == 0:
        L += ["**%s ESTA VUELTA, Y LO DECLARO.** Y su cuerpo."
              % FRASE_SIN_CAIDA_PROPIA, ""]
    L += ["## 2. MI APERTURA DE MENTIRA", ""]
    for k in range(1, caidas_aud + 1):
        L += ["### 2.%d MI CAIDA PROPIA `A.%d`, DE MENTIRA" % (k, k), "",
              "Y su cuerpo.", ""]
    L += ["## 5. LAS ADJUDICACIONES", ""]
    for k in range(1, n_adj + 1):
        L += ["**`5.%d` UN TITULO DE MENTIRA NUMERO %d.** Y su cuerpo." % (k, k), ""]
    L += ["## 6. LOS PENDIENTES DE DOCTRINA", ""]
    for k in range(1, n_pd + 1):
        if k < n_pd:
            L += ["**`6.%d` `PD.%d`, UN PENDIENTE DE MENTIRA: ADJUDICADO.** Y su cuerpo."
                  % (k, k + 1), ""]
        else:
            L += ["**`6.%d` `PD.1` SIGUE ABIERTA, DE MENTIRA.** Los puestos son **%s**,"
                  % (k, ", ".join(str(x) for x in puestos)),
                  "medidos en otro sitio.", ""]
    L += ["## 7. LA CAIDA DE REPORTE", ""]
    for k in range(1, caidas_rep + 1):
        L += ["**`R.%d`. UNA CAIDA DE MENTIRA.** Y su cuerpo." % k, ""]
    return NL.join(L) + NL


def _titulos_de(lineas, ini, fin, prefijo):
    """LOS TITULOS LITERALES DE UN PREFIJO, PARA QUE EL CASO POR MUTACION PUEDA
    CORRER `pendientes_de_doctrina()` SIN TOCAR EL REPO."""
    titulos = {}
    for clave, _n in claves_entrecomilladas(lineas, ini, fin, prefijo):
        pat = re.compile(r"^\s*\*\*`%s` " % re.escape(clave))
        res, err = titulo_de_la_negrita(lineas, ini, fin, pat, clave)
        if err:
            return None, err
        titulos[clave] = res
    return titulos, None


def prueba_de_mutacion():
    """EL CASO POSITIVO POR MUTACION, SOBRE VARIABLE COMPUTADA Y NO SOBRE
    CONSTANTE LITERAL (`EJECUTOR.md` 1, EL CASO ROJO SE PRUEBA POR MUTACION).

    Se fabrica un acta con OTRAS cifras, se corre el contador de verdad sobre
    ella, y se exige que las cifras y el titulo CAMBIEN con ella. Despues se muta
    el valor esperado y se comprueba que el caso CAE: si no cayera, el caso no
    probaria nada. NINGUNA COMPARACION DE AQUI ES ENTRE DOS CONSTANTES."""
    sys.stdout.reconfigure(encoding="utf-8")
    salida = []
    w = salida.append
    w("CASO POSITIVO POR MUTACION de vuelta185_tarea1a_registrar_acta185.py")
    w("EL SUJETO ES UN ACTA FABRICADA, NUNCA LA REAL.")
    w("")
    fallos = 0
    casos = [(7, 4, 1, 1), (1, 1, 0, 0), (12, 3, 3, 2), (4, 2, 1, 0)]
    for n_adj, n_pd, n_aud, n_rep in casos:
        texto = _acta_fabricada(n_adj, n_pd, n_aud, n_rep)
        lineas, rango, err = cuerpo_del_acta(texto)
        if err:
            w("   %r -> %s" % ((n_adj, n_pd, n_aud, n_rep), err))
            fallos += 1
            continue
        ini, fin = rango
        cl = claves_entrecomilladas(lineas, ini, fin, PREFIJO_ADJ)
        pd = claves_entrecomilladas(lineas, ini, fin, PREFIJO_PD)
        aud = cuenta_por_patron(lineas, ini, fin, PAT_CAIDA_AUDITOR_A)
        rep = cuenta_por_patron(lineas, ini, fin, PAT_CAIDA_REPORTE)
        ok = (len(cl) == n_adj and len(pd) == n_pd and len(aud) == n_aud
              and len(rep) == n_rep)
        titulo = titulo_de_la_entrada(len(cl), len(pd), len(aud), len(rep))
        w("   acta fabricada con adj=%d pd=%d aud=%d rep=%d"
          % (n_adj, n_pd, n_aud, n_rep))
        w("      los contadores dicen adj=%d pd=%d aud=%d rep=%d -> %s"
          % (len(cl), len(pd), len(aud), len(rep), "CALZA" if ok else "NO CALZA"))
        w("      titulo computado: %s" % titulo)
        if not ok:
            fallos += 1
    w("")
    w("LA MUTACION DEL VALOR ESPERADO, QUE ES LO QUE PRUEBA QUE EL CASO PUEDE CAER:")
    texto = _acta_fabricada(7, 4, 1, 1)
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
    w("LA SEGUNDA MUTACION: LOS PENDIENTES DE DOCTRINA. Si el contador del prefijo")
    w("6. no contara de verdad, este caso no podria cambiar con el acta.")
    medido_pd = len(claves_entrecomilladas(lineas, ini, fin, PREFIJO_PD))
    for esperado in (4, 5):
        w("   con el esperado %d: %s"
          % (esperado, "PASA" if medido_pd == esperado else "CAE"))
    cae_pd = medido_pd != 5
    w("   medido: %d | EL CASO CAE AL MUTAR EL ESPERADO A 5: %s"
      % (medido_pd, "SI" if cae_pd else "NO"))
    if not cae_pd:
        fallos += 1
    w("")
    w("LA TERCERA MUTACION: EL PATRON SIN COMILLAS, EL DEL ACTA 183. Sobre un acta")
    w("que numera ``**`5.n` `` tiene que dar CERO, que es el motivo de este fichero.")
    con_viejo = len(claves_de_adjudicacion(lineas, ini, fin, PREFIJO_ADJ))
    w("   patron sin comillas sobre acta en forma 185 -> %d adjudicaciones" % con_viejo)
    w("   EL CASO CAE CON EL PATRON VIEJO: %s" % ("SI" if con_viejo == 0 else "NO"))
    if con_viejo != 0:
        fallos += 1
    w("")
    w("LA CUARTA MUTACION: EL PATRON `C.n` DE LAS ACTAS ANTERIORES SOBRE UNA CAIDA")
    w("PROPIA ESCRITA COMO `A.n`. Tiene que dar CERO, y el patron nuevo tiene que")
    w("dar la cifra de verdad. Es la prueba de que `A.n` es especie nueva.")
    aud_nuevo = len(cuenta_por_patron(lineas, ini, fin, PAT_CAIDA_AUDITOR_A))
    aud_viejo = len(cuenta_por_patron(lineas, ini, fin, PAT_CAIDA_AUDITOR_VIEJO))
    w("   patron `A.n` (cabecera ###) -> %d | patron `C.n` (linea) -> %d"
      % (aud_nuevo, aud_viejo))
    ok_aud = (aud_nuevo == 1 and aud_viejo == 0)
    w("   EL NUEVO MUERDE Y EL VIEJO NO: %s" % ("SI" if ok_aud else "NO"))
    if not ok_aud:
        fallos += 1
    w("")
    w("LA QUINTA MUTACION: EL PATRON `E.n` SOBRE UNA CAIDA ESCRITA COMO `R.n`.")
    rep_nuevo = len(cuenta_por_patron(lineas, ini, fin, PAT_CAIDA_REPORTE))
    rep_viejo = len(cuenta_por_patron(lineas, ini, fin, PAT_CAIDA_EJECUTOR_VIEJO))
    w("   patron `R.n` -> %d | patron `E.n` -> %d" % (rep_nuevo, rep_viejo))
    ok_rep = (rep_nuevo == 1 and rep_viejo == 0)
    w("   EL NUEVO MUERDE Y EL VIEJO NO: %s" % ("SI" if ok_rep else "NO"))
    if not ok_rep:
        fallos += 1
    w("")
    w("LA SEXTA MUTACION: LOS PUESTOS DE LA `PD.1`, LEIDOS DEL ACTA. Se fabrica un")
    w("acta con OTROS puestos y se exige que salgan LOS DEL ACTA y no los del")
    w("encargo. Si estuvieran tecleados, este caso no podria cambiar.")
    for inventados in ((11, 22, 33), (7, 8, 9, 10)):
        t2 = _acta_fabricada(7, 4, 1, 1, puestos=inventados)
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
    t3 = _acta_fabricada(7, 4, 1, 1, puestos=reales)
    l3, (i3, f3), _z3 = cuerpo_del_acta(t3)
    tit3, _e3 = _titulos_de(l3, i3, f3, PREFIJO_PD)
    leidos3 = puestos_de_la_pd1(l3, i3, f3, tit3)
    w("   y con los cinco que el encargo nombra -> leidos %s" % leidos3)
    w("   con el esperado MUTADO [1778, 2530, 2540, 3141, 9999]: %s"
      % ("PASA" if leidos3 == [1778, 2530, 2540, 3141, 9999] else "CAE"))
    if leidos3 == [1778, 2530, 2540, 3141, 9999]:
        fallos += 1
    w("")
    w("LA SEPTIMA MUTACION: EL ESTADO DE CADA PENDIENTE, LEIDO DEL TITULO. Un")
    w("titulo que dice SIGUE ABIERTA tiene que salir ABIERTA y los que dicen")
    w("ADJUDICADO tienen que salir CERRADA, y el reparto tiene que cambiar con el")
    w("acta.")
    tit_pd, _e4 = _titulos_de(lineas, ini, fin, PREFIJO_PD)
    estados = [(c, pd, e) for c, pd, e, _l, _t
               in pendientes_de_doctrina(lineas, ini, fin, tit_pd)]
    w("   estados computados: %s" % estados)
    n_cerradas = len([1 for _c, _p, e in estados if e == "CERRADA"])
    n_abiertas = len([1 for _c, _p, e in estados if e == "ABIERTA"])
    ok_est = (n_cerradas == 3 and n_abiertas == 1)
    w("   CERRADAS %d | ABIERTAS %d | esperado 3 y 1 -> %s"
      % (n_cerradas, n_abiertas, "CALZA" if ok_est else "NO CALZA"))
    w("   con el esperado MUTADO (4 cerradas): %s"
      % ("PASA" if n_cerradas == 4 else "CAE"))
    if not ok_est or n_cerradas == 4:
        fallos += 1
    w("")
    w("LA OCTAVA MUTACION: EL SALTO. actas_sin_entrada() es PURA y se importa del")
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
    w("LA NOVENA MUTACION: EL TITULO Y SU CONCORDANCIA, INCLUIDO EL CERO.")
    t0 = titulo_de_la_entrada(7, 4, 1, 1)
    w("   %s" % t0)
    ok_t = ("las siete adjudicaciones numeradas" in t0
            and "los cuatro pendientes de doctrina" in t0
            and "la caida propia del auditor" in t0
            and "la caida de reporte del ejecutor" in t0)
    w("   DICE LAS CUATRO COSAS Y CONCUERDA: %s" % ("SI" if ok_t else "NO"))
    if not ok_t:
        fallos += 1
    t1 = titulo_de_la_entrada(3, 1, 0, 2)
    w("   y con otras cifras, para que se vea que no esta clavada: %s" % t1)
    if ("las tres adjudicaciones" not in t1 or "el pendiente de doctrina" not in t1
            or "las cero caidas propias" not in t1
            or "las dos caidas de reporte" not in t1):
        w("   LA CONCORDANCIA NO SIGUE A LAS CIFRAS: NO")
        fallos += 1
    else:
        w("   LA CONCORDANCIA SIGUE A LAS CIFRAS: SI")
    w("")
    w("CIFRA fallos: %d" % fallos)
    w("VEREDICTO: %s" % ("VERDE" if fallos == 0 else "ROJO"))
    t = NL.join(salida) + NL
    ruta = os.path.join(LOOP, "SALIDA_V%s_T1A_MUTACION_REGISTRO_185.txt"
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

    w("C) LOS PENDIENTES DE DOCTRINA DE LA SECCION 6, CON EL MISMO PATRON")
    claves_pd = claves_entrecomilladas(lineas, inicio, fin, PREFIJO_PD)
    w("   prefijo: %r" % PREFIJO_PD)
    w("   CIFRA pendientes de doctrina hallados: %d" % len(claves_pd))
    for clave, cuantas in claves_pd:
        w("      %s -> %d aparicion(es)" % (clave, cuantas))
    if len(claves) + len(claves_pd) != len(VIA):
        w("   PARADA: el acta trae %d numerales y las glosas cubren %d."
          % (len(claves) + len(claves_pd), len(VIA)))
        print(NL.join(salida))
        return 1
    w("")

    w("D) LAS CAIDAS, POR SUS FAMILIAS, Y LOS PATRONES VIEJOS AL LADO")
    l_aud = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_AUDITOR_A)
    l_aud_v = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_AUDITOR_VIEJO)
    l_aud_p = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_AUDITOR_PROSA_VIEJO)
    l_rep = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_REPORTE)
    l_eje_v = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_EJECUTOR_VIEJO)
    l_declara = lineas_que_declaran_cero_caidas(lineas, inicio, fin)
    w("   CAIDAS PROPIAS DEL AUDITOR (patron `A.n`, cabecera ###): %d, lineas %s"
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
    w("   LINEAS DONDE EL ACTA DECLARA QUE NO TUVO NINGUNA CAIDA PROPIA: %s"
      % (", ".join(str(x) for x in l_declara) or "(ninguna)"))
    if not l_rep:
        w("   PARADA: el patron de caida de reporte no encuentra ninguna, y el acta")
        w("   185 declara una en su seccion 7. No se escribe una entrada asi.")
        print(NL.join(salida))
        return 1
    if not l_aud and not l_declara:
        w("   PARADA: cero caidas propias del auditor Y el acta no lo declara.")
        w("   Un cero de un patron que no muerde no se publica como medicion.")
        print(NL.join(salida))
        return 1
    w("")

    w("E) EL TITULO, CON SUS CUATRO NUMERALES COMPUTADOS")
    titulo = titulo_de_la_entrada(len(claves), len(claves_pd), len(l_aud), len(l_rep))
    w("   %s" % titulo)
    w("")

    w("F) LOS TITULOS LITERALES, LEIDOS DEL ACTA")
    titulos = {}
    for clave, _n in claves + claves_pd:
        pat = re.compile(r"^\s*\*\*`%s` " % re.escape(clave))
        res, err2 = titulo_de_la_negrita(lineas, inicio, fin, pat, clave)
        if err2:
            w("   %s -> %s" % (clave, err2))
            print(NL.join(salida))
            return 1
        titulos[clave] = res
        w("   %s (linea %d): %s" % (clave, res[0], res[1][:130]))
    w("")

    w("G) EL ESTADO DE CADA PENDIENTE, LEIDO DE SU TITULO Y NO TECLEADO")
    pds = pendientes_de_doctrina(lineas, inicio, fin, titulos)
    for clave, pd, estado, ln, _tit in pds:
        w("   %s nombra %s -> %s (linea %d)" % (clave, pd, estado, ln))
    sin_decir = [c for c, _p, e, _l, _t in pds if e == "SIN DECIR"]
    if sin_decir:
        w("   PARADA: %s no dice si cierra o sigue abierto." % ", ".join(sin_decir))
        print(NL.join(salida))
        return 1
    puestos_pd1 = puestos_de_la_pd1(lineas, inicio, fin, titulos)
    w("   LOS PUESTOS DEL PENDIENTE ABIERTO, LEIDOS DEL ACTA: %s"
      % (", ".join(str(x) for x in puestos_pd1) or "(ninguno)"))
    if not puestos_pd1:
        w("   PARADA: el pendiente abierto no nombra ningun puesto y el acta dice")
        w("   que ahora tiene cinco nombres. No se escribe una lista vacia.")
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

    w("I) LA DEUDA DE LA SERIE, REMEDIDA EN ESTA VUELTA Y NO HEREDADA DEL R.46")
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
    w("J) LA IDEMPOTENCIA, COMPROBADA ANTES DE ESCRIBIR")
    w("   la marca %r ya esta en la sede: %s"
      % (marca, "SI" if marca in texto_sede else "NO"))
    w("   la entrada entera ya esta: %s" % ("SI" if ya else "NO"))
    w("")

    entrada = armar_entrada(numero, titulo, claves, pds, titulos, l_aud, l_rep,
                            l_declara, inicio, fin, len(viejas_adj),
                            len(l_eje_v), len(l_aud_v), len(l_aud_p),
                            puestos_pd1, salto)
    w("K) LA ENTRADA ARMADA")
    w("   %d bytes | %d lineas" % (len(entrada.encode("utf-8")), entrada.count(NL)))
    w("")

    if a.simular:
        w("L) MODO --simular: NO SE ESCRIBE NADA EN LA SEDE.")
        w("")
        w("LA ENTRADA, ENTERA:")
        for l in entrada.split(NL):
            w("   | " + l)
    elif ya:
        w("L) NO SE ESCRIBE: la entrada ya esta en la sede, byte a byte.")
    else:
        nuevo = texto_sede.rstrip(NL) + NL + NL + entrada
        io.open(SEDE, "w", encoding="utf-8", newline=NL).write(nuevo)
        w("L) ESCRITA EN docs/PENDIENTES.md")
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
