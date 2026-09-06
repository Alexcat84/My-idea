# -*- coding: utf-8 -*-
r"""vuelta183_tarea1a_registrar_acta182.py . EL ACTA 182 ENTERA, REGISTRADA EN LA
SERIE `R.N` EN LA FORMA DE LA CASA, Y EL SALTO DE OCHO DECLARADO EN LA MISMA
ENTRADA.

LA MAQUINA NO SE CLONA, SE IMPORTA, y eso lo adjudico la `6.6` del acta 172 como
correcto y obligatorio: `PALABRA` y `titulo_de_la_negrita` se importan de
`scripts/loop/vuelta172_tarea1_registrar_acta171.py`, que es la sede que la
bateria ya vigila, y `claves_de_adjudicacion`, `cuenta_por_patron` y
`_acta_fabricada` se importan de `scripts/loop/vuelta182_tarea1a_registrar_acta181.py`,
que es el registrador de la vuelta pasada. Lo unico propio de este fichero es EL
ACOTE DE SU ACTA, LOS PATRONES QUE SU ACTA NECESITA Y SUS GLOSAS.

POR QUE HACE FALTA CODIGO PROPIO OTRA VEZ, MEDIDO Y NO SUPUESTO. El acta 182 tiene
DOS familias de adjudicacion, no una: las `5.D.1` a `5.D.7` de su seccion 5 (que
el acta escribe como ``**`D.1`,``) y las `7.1` a `7.5` de su seccion 7. El
registrador de la 182 solo sabe barrer un prefijo del tipo `**7.n `, asi que
sobre esta acta se dejaria SIETE adjudicaciones fuera.

Y HAY UNA SEGUNDA DIFERENCIA, Y ES LA QUE IMPORTA PARA EL PATRON DE CAIDA. El
acta 181 escribia la caida propia del auditor como ``**`C.1`.`` al principio de
linea. EL ACTA 182 NO: la escribe DENTRO de una frase en negrita, *"**MI CAIDA
PROPIA, `C.1`, Y VA IGUAL AUNQUE EL SELLO AGUANTARA.**"*. **El patron de la 182,
corrido sobre el acta 182, cuenta CERO**, y esa cifra se publica al lado de la
nueva. Se anade un patron, no se ensancha el viejo hasta que trague.

LAS CIFRAS DEL TITULO NO SE TECLEAN: se cuentan del acta acotada. Ni el numero de
la entrada: lo devuelve `scripts/loop/serie_de_registros.py` recomputando la serie
de sus DOS sedes.

LA 1.b VA DENTRO DE ESTA MISMA ENTRADA Y NO EN OCHO ENTRADAS FABRICADAS. La
adjudicacion `7.4` del acta 182 dice, literal, que la deuda **se documenta como
salto, no se inventa**, y encarga **una sola linea de constancia en la serie**.
Aqui esa linea va con sus DOS EXTREMOS (el registro que cubre el acta 172 y el
que cubre la 181) y su CIFRA CONTADA por el instrumento, no tecleada.

LO QUE ESTE FICHERO NO HACE: no toca el acta, no toca el reporte, no toca
`docs/plan/`, no corre la bateria y no escribe ningun veredicto. Escribe UNA
entrada en UNA sede, y si la entrada ya esta, NO la duplica y lo dice.

USO:
  python scripts/loop/vuelta183_tarea1a_registrar_acta182.py
  python scripts/loop/vuelta183_tarea1a_registrar_acta182.py --simular
  python scripts/loop/vuelta183_tarea1a_registrar_acta182.py --mutacion
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

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")
SEDE = os.path.join(RAIZ, "docs", "PENDIENTES.md")
NL = chr(10)

VUELTA_DEL_ACTA = 182
VUELTA_QUE_ESCRIBE = 183
CABECERA_ACTA = "# ACTA DEL AUDITOR, VUELTA %d" % VUELTA_DEL_ACTA
PREFIJO_ADJ = "7."

# LAS ADJUDICACIONES DE LA SECCION 5, que el acta escribe con backticks y coma:
# ``**`D.1`, LA VARA ...``. El acta las llama `5.D.n` en su seccion 10.
PAT_ADJ_D = re.compile(r"^\s*\*\*`?D\.(\d+)`?[,.]")

# LAS DOS FORMAS DE LA CAIDA DEL AUDITOR. La primera es la del acta 181 y se
# conserva para publicar su CERO al lado; la segunda es la que el acta 182 usa de
# verdad, dentro de una frase en negrita.
PAT_CAIDA_AUDITOR_VIEJA = re.compile(r"^\s*(?:-\s+)?\*\*`?C\.(\d+)`?[,.]")
PAT_CAIDA_AUDITOR_PROSA = re.compile(r"^\*\*[^*]*CAIDA[^*]*`C\.(\d+)`")
PAT_CAIDA_EJECUTOR = re.compile(r"^\s*(?:-\s+)?\*\*`?E\.(\d+)`?[,.]")
PAT_CAIDA_VIEJA = re.compile(r"^\s*(?:-\s+)?\*\*`?CAIDA (\d+)`?[,.]")

# LA VIA DE CADA ADJUDICACION, escrita a mano porque es JUICIO del ejecutor sobre
# que hace ESTA vuelta con ella, y el juicio no sale de ningun instrumento. Lo
# que si sale de instrumento es el TITULO literal de cada una y su linea.
VIA = {
    "D.1": "SIN TOCAR NADA",
    "D.2": "SIN TOCAR NADA",
    "D.3": "SIN TOCAR NADA",
    "D.4": "SIN TOCAR NADA",
    "D.5": "SIN TOCAR NADA",
    "D.6": "EJECUTADA",
    "D.7": "SIN TOCAR NADA",
    "7.1": "EJECUTADA",
    "7.2": "SIN TOCAR NADA",
    "7.3": "SIN TOCAR NADA",
    "7.4": "EJECUTADA A MEDIAS, Y LA MITAD QUE FALTA VA DECLARADA",
    "7.5": "SIN TOCAR NADA",
}

QUE_HACE_ESTA_VUELTA = {
    "D.1": ("SE ACATA SIN TOCAR NADA. La vara `abs 3, cobertura 0.45` queda "
            "concedida CON SU LIMITE ESCRITO: vale para nombrar candidatos, no "
            "para cerrar una clase. Esta vuelta es de bateria y no mueve ninguna "
            "clase, asi que el limite no se acerca siquiera."),
    "D.2": ("SE ACATA SIN TOCAR NADA, Y SE HEREDA COMO DEUDA MEDIBLE. Las seis "
            "clausulas de carencia quedan concedidas como deuda y no como defecto: "
            "el dia que alguien ensanche la lista, la cifra de 99 sube. Esta vuelta "
            "no ensancha nada."),
    "D.3": ("SE ACATA SIN TOCAR NADA. El corte por punto y coma queda concedido "
            "porque el orden se declaro y la salida vieja se publico entera. No hay "
            "trabajo pendiente en el."),
    "D.4": ("SE ACATA SIN TOCAR NADA, Y ESTA VUELTA ES LA QUE LA COBRA. El arnes de "
            "la `P.1` entro a la nomina en su misma vuelta, y por eso "
            "`arneses_que_faltan()` abre la 183 en CERO en vez de en uno. La cifra "
            "va medida en el bloque H.9 de la apertura de hoy."),
    "D.5": ("SE ACATA SIN TOCAR NADA. La declaracion de sujeto congelado sobre su "
            "propio arnes quedo concedida porque el auditor la CORRIO, que es la "
            "condicion que el acta pone. Esta vuelta la vuelve a medir sin tocarla: "
            "`guarda_del_sujeto_congelado()` en el bloque H.9 de la apertura."),
    "D.6": ("EJECUTADA EN LA TAREA 2 DE ESTA VUELTA, QUE ES DONDE VIVE. La `D.6` "
            "concede que `--siguiente` cuente una salida de CERO BYTES como NO "
            "hecha, por extension citada del punto 3 de "
            "`paradas/2026-09-05-la-bateria-sin-techo-DECISION.md`. La bateria por "
            "tramos de esta vuelta corre con esa regla puesta."),
    "D.7": ("SE ACATA SIN TOCAR NADA. El TRAMO 1 y unico de la cola post fusion "
            "queda concedido como tramo legitimo. Esta vuelta NO lo relee: es "
            "vuelta de bateria y el 2.464 espera a la primera vuelta de trabajo."),
    "7.1": ("EJECUTADA EN LA TAREA 1.d DE ESTA VUELTA. La adjudicacion dice que la "
            "declaracion del hueco de la seccion 9 tiene que decir CUAL DE LOS DOS "
            "casos es, inexistente o de cero bytes, porque hoy `max(tam, 0)` los "
            "confunde en un mismo cero. Esta vuelta lo separa en el codigo, con su "
            "arnes, y sin tocar las tres piezas que el hueco ya exige."),
    "7.2": ("SE ACATA SIN TOCAR NADA. Es la declaracion de que la vara de la `D.1` "
            "no cierra clases, escrita por el auditor para que no se herede al "
            "reves. Esta vuelta no encola ni desencola ningun par."),
    "7.3": ("SE ACATA SIN TOCAR NADA POR MI PARTE, Y DISPARA LA TAREA 1.e. Las seis "
            "discrepancias de la ciega son del auditor y van a favor del archivo; "
            "lo que llega al ejecutor es la RELECTURA AL DOBLE del tramo, que "
            "`AUDITOR.md` 1.2 manda porque salieron FUERA del marcado."),
    "7.4": ("EJECUTADA A MEDIAS, Y LA MITAD QUE FALTA VA DECLARADA AQUI MISMO. De "
            "las tres partes de la `7.4`: la deuda de ocho registros se documenta "
            "como SALTO en esta misma entrada y NO se rellena, que es lo que la "
            "adjudicacion manda; la `PD.1` de las cinco `D` queda registrada y sin "
            "resolver; y el instrumento de vigencia de las ocho `A` rancias por "
            "`P.5` NO se cablea en esta vuelta, porque la propia adjudicacion lo "
            "manda a la primera vuelta de trabajo y la 183 es de bateria."),
    "7.5": ("SE ACATA SIN TOCAR NADA, Y SE REGISTRA A FAVOR DEL EJECUTOR. El acta "
            "registra la `C.1` del ejecutor a su favor porque la cazo su propio "
            "instrumento y el texto viejo no se borro. No hay trabajo pendiente."),
}


def cuerpo_del_acta(texto=None):
    """EL ACTA ACOTADA: (lineas, (inicio, fin), error). El fin es el final del
    fichero porque el acta 182 es la ultima escrita; si algun dia dejara de
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


def claves_de_la_seccion5(lineas, inicio, fin):
    """LAS ADJUDICACIONES `5.D.n`, CONTADAS DE SU PATRON Y ORDENADAS POR NUMERO.
    Devuelve [(clave, cuantas)] con la clave en la forma corta `D.n`, que es como
    el acta las escribe en su seccion 5.

    PURA: recibe las lineas y no lee nada."""
    vistas = {}
    for i in range(inicio, fin + 1):
        m = PAT_ADJ_D.match(lineas[i - 1])
        if m:
            k = int(m.group(1))
            vistas[k] = vistas.get(k, 0) + 1
    return [("D.%d" % k, vistas[k]) for k in sorted(vistas)]


def titulo_de_la_entrada(n_adj, n_cai_aud, n_cai_eje):
    """El titulo, con sus TRES numerales COMPUTADOS y no tecleados, y con la
    concordancia dentro del computo."""
    def trozo(n, sing, plur):
        return ("%s %s" % ("la" if n == 1 else "las", sing) if n == 1
                else "%s %s %s" % ("las", PALABRA[n], plur))
    return ("Registro de %s, %s del auditor y %s del ejecutor "
            "del acta de la vuelta %d"
            % (trozo(n_adj, "adjudicacion", "adjudicaciones"),
               trozo(n_cai_aud, "caida propia", "caidas propias"),
               trozo(n_cai_eje, "caida", "caidas"),
               VUELTA_DEL_ACTA))


def actas_sin_entrada(halladas, desde, hasta):
    """LAS ACTAS QUE NO TIENEN ENTRADA PROPIA EN LA SERIE, y los DOS EXTREMOS del
    salto. Devuelve (faltan, extremo_bajo, extremo_alto), con cada extremo como
    (numero_de_registro, vuelta_del_acta) o None.

    PURA: recibe la serie ya recomputada. El extremo bajo es el ULTIMO registro
    que cubre un acta ANTERIOR al salto; el alto, el PRIMERO que cubre una
    posterior. Ninguno de los dos se teclea: los dos salen de los titulos."""
    cubre = {}
    for numero, _rel, _linea, titulo in halladas:
        m = re.search(r"acta de la vuelta (\d+)", titulo)
        if m:
            cubre[int(m.group(1))] = numero
    faltan = [v for v in range(desde, hasta + 1) if v not in cubre]
    if not faltan:
        return faltan, None, None
    bajos = [(cubre[v], v) for v in cubre if v < min(faltan)]
    altos = [(cubre[v], v) for v in cubre if v > max(faltan)]
    return (faltan,
            max(bajos) if bajos else None,
            min(altos) if altos else None)


def armar_entrada(numero, titulo, claves_d, claves_7, titulos, l_aud, l_eje,
                  inicio, fin, viejas_aud, viejas_caida, salto):
    faltan, bajo, alto = salto
    p = []
    p.append("## R.%d. %s" % (numero, titulo))
    p.append("")
    p.append("(Acta del auditor, vuelta %d, secciones 2, 5, 6 y 7; escrito en la vuelta %d,"
             % (VUELTA_DEL_ACTA, VUELTA_QUE_ESCRIBE))
    p.append("TAREAS 1.a y 1.b.)")
    p.append("")
    p.append("Por adicion, como `R.21` a `R.43`. **Corte de todas las cifras de esta")
    p.append("entrada: 5 sep 2026.** El numero de esta entrada NO esta tecleado: lo computa")
    p.append("`scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS sedes.")
    p.append("La SEDE tampoco se supone: sale de la adjudicacion 6.3 del acta 162, que es")
    p.append("la que citan los `R.30` a `R.43`. Salida:")
    p.append("`docs/loop/SALIDA_V%d_T1A_REGISTRO_R%d.txt`."
             % (VUELTA_QUE_ESCRIBE, numero))
    p.append("")
    p.append("**ESTA ENTRADA SE ESCRIBE CON LA TAREA 1.a EN CURSO Y LA TAREA 2 SIN CORRER,")
    p.append("ASI QUE SUS GLOSAS NO AFIRMAN EN PASADO LO QUE TODAVIA NO HA PASADO.** Es la")
    p.append("forma que la `6.4` del acta 172 adjudico como correcta y que la realidad")
    p.append("probo cuando la vuelta 172 se corto: donde una glosa dice EJECUTADA, la")
    p.append("prueba va nombrada con su fichero de salida; donde dice que va a ejecutarse,")
    p.append("se dice que **todavia no ha corrido** y no se disfraza.")
    p.append("")
    p.append("**Y LOS TRES NUMERALES DEL TITULO TAMPOCO ESTAN TECLEADOS:** se cuentan del")
    p.append("acta acotada (lineas %d a %d) y de ahi sale el numeral en palabra, incluida"
             % (inicio, fin))
    p.append("la concordancia. **%d adjudicaciones (%d de la seccion 5, `5.D.n`, y %d de la"
             % (len(claves_d) + len(claves_7), len(claves_d), len(claves_7)))
    p.append("seccion 7, `7.n`), %d caida propia del auditor (`C.n`) y %d caidas del"
             % (len(l_aud), len(l_eje)))
    p.append("ejecutor (`E.n`).**")
    p.append("")
    p.append("**ESTA ACTA TIENE DOS FAMILIAS DE ADJUDICACION Y EL REGISTRADOR DE LA 182")
    p.append("SOLO SABIA CONTAR UNA.** Su `claves_de_adjudicacion()` barre un prefijo del")
    p.append("tipo `**7.n `, y las siete de la seccion 5 el acta las escribe como")
    p.append("``**`D.1`,``. **Corrido tal cual, dejaria SIETE adjudicaciones fuera.** Aqui")
    p.append("se anade `claves_de_la_seccion5()`, y la funcion vieja se importa y se corre")
    p.append("igual para las `7.n`: no se reescribe lo que ya funciona.")
    p.append("")
    p.append("**Y EL PATRON DE LA CAIDA DEL AUDITOR CAMBIA OTRA VEZ, Y SE DECLARA EN VEZ DE")
    p.append("FORZARLO.** El acta 181 escribia ``**`C.1`.`` al principio de linea; el acta")
    p.append("182 escribe la suya DENTRO de una frase en negrita, *\"**MI CAIDA PROPIA,")
    p.append("`C.1`, Y VA IGUAL AUNQUE EL SELLO AGUANTARA.**\"*. **El patron de la 182,")
    p.append("corrido sobre el acta 182, cuenta %d**, y el patron todavia mas viejo")
    p.append("(`**CAIDA n.`) cuenta %d." % viejas_caida)
    p[-2] = p[-2] % viejas_aud
    p.append("Las dos cifras se publican al lado de la buena para que se vea que no se")
    p.append("afloja nada: se anade un patron, no se ensancha el viejo hasta que trague.")
    p.append("")
    p.append("**LAS %s ADJUDICACIONES, CON SU LINEA EN EL ACTA LEIDA HOY.** El titulo de"
             % PALABRA[len(claves_d) + len(claves_7)].upper())
    p.append("cada una es LITERAL del fichero; la glosa que sigue es prosa del ejecutor y")
    p.append("va marcada como tal.")
    p.append("")
    for clave, _n in list(claves_d) + list(claves_7):
        ln, tit = titulos[clave]
        etiqueta = ("5.%s" % clave) if clave.startswith("D.") else clave
        p.append("  - **%s (`docs/loop/ACTA_AUDITOR.md:%d`, leida hoy). VIA: %s.** Titulo"
                 % (etiqueta, ln, VIA[clave]))
        p.append("    literal del acta: *\"%s\"*" % tit)
        p.append("    **QUE HACE ESTA VUELTA CON ELLA (glosa del ejecutor, no del acta):** %s"
                 % QUE_HACE_ESTA_VUELTA[clave])
    p.append("")
    p.append("**LA CAIDA PROPIA DEL AUDITOR, EN LA LINEA %d, Y NO ES TRABAJO DEL"
             % l_aud[0])
    p.append("EJECUTOR.** Es la `C.1` de la vuelta 182, y el acta la declara **aunque el")
    p.append("sello aguantara**: el auditor corrio `head -c 900` sobre el archivo de")
    p.append("veredictos con su sujeto ya aislado, midio el solape con sus 30 y le dio")
    p.append("CERO. **Es ademas la primera en cinco actas que NO es la del orden de la")
    p.append("apertura**, y esa racha se corto porque la TAREA 2 de la 182 convirtio el")
    p.append("remedio en codigo. **El acta confiesa ademas una segunda, menor y sin")
    p.append("numero** (un verificador de parejas de bytes que publico 7 discrepancias")
    p.append("falsas y que el propio auditor cazo y reescribio); **su seccion 9 cuenta")
    p.append("UNA**, y esta entrada cuenta lo que el patron encuentra, que es una.")
    p.append("")
    p.append("**LAS DOS CAIDAS DEL EJECUTOR, EN LAS LINEAS %s.**"
             % " y ".join(str(x) for x in l_eje))
    p.append("El `E.1` **ACUMULA**: el veredicto de una linea del reporte de la 182 dice")
    p.append("*\"LAS SEIS CAIDAS QUE COMETI\"* y su seccion 8 lista **siete**, `C.1` a")
    p.append("`C.7`. Vive en la CONCLUSION del reporte, no en prosa de acompanamiento, y")
    p.append("por la letra afinada del 27 ago 2026 cuenta para la racha. **La racha de")
    p.append("reporte llega a DOS, y por eso la escalada de `AUDITOR.md` 1.2 es la TAREA")
    p.append("1.c de esta vuelta.** El `E.2` **NO acumula**: el reporte afirmaba que la")
    p.append("181 cerro y archivo su reporte en su misma vuelta y no hizo ninguna de las")
    p.append("dos cosas, pero la frase vive en el bloque de prosa que abre el reporte.")
    p.append("**Su consecuencia si es de fondo:** de ella depende el disparador del")
    p.append("regimen `6.2`, y con la medicion delante la cuenta de vueltas que cierran su")
    p.append("propio reporte es **UNA**, no dos.")
    p.append("")
    p.append("**LA DEUDA DE LA SERIE, DOCUMENTADA COMO SALTO Y NO RELLENADA (TAREA 1.b).**")
    p.append("La adjudicacion `7.4` del acta 182 lo dice con estas palabras: *\"la deuda se")
    p.append("documenta como salto, no se inventa\"*, y encarga **una sola linea de")
    p.append("constancia**. Esta es:")
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
        p.append("    escribir de memoria ocho registros de ocho actas que nadie ha releido")
        p.append("    en esta vuelta seria justo lo que `AUDITOR.md` 2 prohibe.")
    else:
        p.append("  - **NO HAY SALTO:** todas las actas del tramo medido tienen entrada")
        p.append("    propia en la serie. La constancia se escribe igual, porque una")
        p.append("    comprobacion que solo se publica cuando falla no se puede auditar.")
    p.append("")
    p.append("**LO QUE ESTA ENTRADA NO REGISTRA, DICHO PARA QUE NO SE BUSQUE:** la `PD.1`")
    p.append("de las cinco `D` con el diferenciador ya presente el dia del veredicto queda")
    p.append("**registrada y sin resolver**, que es lo que el acta manda; y el instrumento")
    p.append("de vigencia de las ocho `A` rancias por `P.5` **no se cablea en esta vuelta**,")
    p.append("porque la propia `7.4` lo manda a la primera vuelta de trabajo y la 183 es")
    p.append("**vuelta de bateria**.")
    return NL.join(p) + NL


def _acta_fabricada(n_d, n_7, caidas_aud, caidas_eje):
    """UN ACTA DE MENTIRA para el caso positivo por mutacion. NO toca el repo.

    Escribe la caida del auditor EN LA FORMA DEL ACTA 182 (dentro de una frase en
    negrita) y no en la del acta 181, que es justo la diferencia que este fichero
    existe para cubrir."""
    L = ["# ACTA DEL AUDITOR, VUELTA %d (fabricada)" % VUELTA_DEL_ACTA, ""]
    for k in range(1, caidas_aud + 1):
        L += ["**MI CAIDA PROPIA, `C.%d`, DE MENTIRA Y EN NEGRITA.** Y su cuerpo." % k, ""]
    for k in range(1, caidas_eje + 1):
        L += ["**`E.%d`. UNA CAIDA DEL EJECUTOR DE MENTIRA.**" % k, ""]
    L += ["## 5. LOS DISCUTIBLES MARCADOS", ""]
    for k in range(1, n_d + 1):
        L += ["**`D.%d`, UN TITULO DE MENTIRA NUMERO %d.** Y su cuerpo." % (k, k), ""]
    L += ["## 7. LAS ADJUDICACIONES", ""]
    for k in range(1, n_7 + 1):
        L += ["**7.%d UN TITULO DE MENTIRA NUMERO %d.** Y su cuerpo." % (k, k), ""]
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
    w("CASO POSITIVO POR MUTACION de vuelta183_tarea1a_registrar_acta182.py")
    w("")
    fallos = 0
    casos = [(7, 5, 1, 2), (1, 1, 1, 1), (3, 12, 2, 1), (9, 2, 1, 4)]
    for n_d, n_7, n_aud, n_eje in casos:
        texto = _acta_fabricada(n_d, n_7, n_aud, n_eje)
        lineas, rango, err = cuerpo_del_acta(texto)
        if err:
            w("   %r -> %s" % ((n_d, n_7, n_aud, n_eje), err))
            fallos += 1
            continue
        ini, fin = rango
        # LAS CUATRO VARIABLES SON COMPUTADAS: salen de correr los contadores de
        # verdad sobre el acta fabricada, no de escribirlas aqui.
        cd = claves_de_la_seccion5(lineas, ini, fin)
        c7 = claves_de_adjudicacion(lineas, ini, fin, PREFIJO_ADJ)
        aud = cuenta_por_patron(lineas, ini, fin, PAT_CAIDA_AUDITOR_PROSA)
        eje = cuenta_por_patron(lineas, ini, fin, PAT_CAIDA_EJECUTOR)
        ok = (len(cd) == n_d and len(c7) == n_7 and len(aud) == n_aud
              and len(eje) == n_eje)
        titulo = titulo_de_la_entrada(len(cd) + len(c7), len(aud), len(eje))
        w("   acta fabricada con D=%d 7=%d aud=%d eje=%d" % (n_d, n_7, n_aud, n_eje))
        w("      los contadores dicen D=%d 7=%d aud=%d eje=%d -> %s"
          % (len(cd), len(c7), len(aud), len(eje), "CALZA" if ok else "NO CALZA"))
        w("      titulo computado: %s" % titulo)
        if not ok:
            fallos += 1
    w("")
    w("LA MUTACION DEL VALOR ESPERADO, QUE ES LO QUE PRUEBA QUE EL CASO PUEDE CAER:")
    texto = _acta_fabricada(7, 5, 1, 2)
    lineas, (ini, fin), _e = cuerpo_del_acta(texto)
    medido = len(claves_de_la_seccion5(lineas, ini, fin))
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
    w("LA SEGUNDA MUTACION: EL PATRON DE CAIDA DEL AUDITOR. Con el patron del acta")
    w("181 el contador tiene que dar CERO sobre un acta que la escribe en negrita")
    w("de frase, que es justo el motivo de este fichero.")
    con_viejo = len(cuenta_por_patron(lineas, ini, fin, PAT_CAIDA_AUDITOR_VIEJA))
    w("   patron del acta 181 sobre acta en forma 182 -> %d caidas" % con_viejo)
    w("   EL CASO CAE CON EL PATRON VIEJO: %s" % ("SI" if con_viejo == 0 else "NO"))
    if con_viejo != 0:
        fallos += 1
    w("")
    w("LA TERCERA MUTACION: EL PREFIJO DE LA SECCION 7. Con el prefijo `6.` el")
    w("contador tiene que dar CERO sobre un acta que numera `7.n`.")
    con_6 = len(claves_de_adjudicacion(lineas, ini, fin, "6."))
    w("   prefijo %r sobre acta de %r -> %d adjudicaciones" % ("6.", "7.", con_6))
    w("   EL CASO CAE CON EL PREFIJO VIEJO: %s" % ("SI" if con_6 == 0 else "NO"))
    if con_6 != 0:
        fallos += 1
    w("")
    w("LA CUARTA MUTACION: EL SALTO. actas_sin_entrada() es PURA, asi que se le")
    w("pasa una serie fabricada y se comprueba que el salto y sus DOS extremos")
    w("salen de los titulos y no de ninguna constante.")
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
    faltan2, _b2, _a2 = actas_sin_entrada(serie_falsa, 100, 101)
    w("   y sobre un tramo SIN salto (100 a 101) devuelve: %s" % faltan2)
    if faltan2 != []:
        fallos += 1
    w("")
    w("CIFRA fallos: %d" % fallos)
    w("VEREDICTO: %s" % ("VERDE" if fallos == 0 else "ROJO"))
    t = NL.join(salida) + NL
    ruta = os.path.join(LOOP, "SALIDA_V%d_T1A_MUTACION_REGISTRO.txt" % VUELTA_QUE_ESCRIBE)
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
    w("VUELTA %d, TAREAS 1.a Y 1.b: EL ACTA %d ENTERA, REGISTRADA, Y EL SALTO"
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

    w("B) LAS ADJUDICACIONES, EN SUS DOS FAMILIAS, CONTADAS Y NO TECLEADAS")
    claves_d = claves_de_la_seccion5(lineas, inicio, fin)
    claves_7 = claves_de_adjudicacion(lineas, inicio, fin, PREFIJO_ADJ)
    w("   SECCION 5, patron %r" % PAT_ADJ_D.pattern)
    w("   CIFRA adjudicaciones `5.D.n` halladas: %d" % len(claves_d))
    for clave, cuantas in claves_d:
        w("      %s -> %d aparicion(es)" % (clave, cuantas))
    w("   SECCION 7, prefijo %r" % PREFIJO_ADJ)
    w("   CIFRA adjudicaciones `7.n` halladas: %d" % len(claves_7))
    for clave, cuantas in claves_7:
        w("      %s -> %d aparicion(es)" % (clave, cuantas))
    w("   CIFRA adjudicaciones TOTAL: %d" % (len(claves_d) + len(claves_7)))
    viejas = claves_de_adjudicacion(lineas, inicio, fin, "6.")
    w("   EL CONTRASTE QUE PRUEBA QUE HACIA FALTA CODIGO PROPIO:")
    w("      el registrador de la 172 busca %r clavado -> %d sobre esta acta"
      % ("6.", len(viejas)))
    w("      el registrador de la 182 solo barre un prefijo `**7.n ` -> %d sobre"
      % len(claves_7))
    w("      esta acta, y dejaria las %d de la seccion 5 fuera." % len(claves_d))
    dobles = [c for c, n in list(claves_d) + list(claves_7) if n != 1]
    if dobles:
        w("   PARADA: hay claves repetidas dentro del acta: %s" % ", ".join(dobles))
        print(NL.join(salida))
        return 1
    w("")

    w("C) LAS CAIDAS, POR SUS FAMILIAS, Y LOS PATRONES VIEJOS AL LADO")
    l_aud = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_AUDITOR_PROSA)
    l_aud_v = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_AUDITOR_VIEJA)
    l_eje = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_EJECUTOR)
    l_vie = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_VIEJA)
    w("   CAIDAS DEL AUDITOR (patron de negrita de frase, el del acta 182): %d, "
      "en las lineas %s"
      % (len(l_aud), ", ".join(str(x) for x in l_aud) or "(ninguna)"))
    w("   EL PATRON DEL ACTA 181 (`**`C.n`.` al principio de linea): %d" % len(l_aud_v))
    w("   CAIDAS DEL EJECUTOR (patron E.n): %d, en las lineas %s"
      % (len(l_eje), ", ".join(str(x) for x in l_eje) or "(ninguna)"))
    w("   EL PATRON MAS VIEJO (`**CAIDA n.`), corrido sobre esta acta: %d" % len(l_vie))
    w("   (los dos viejos dan CERO y por eso hay un patron nuevo. Se declara, no")
    w("    se fuerza el viejo para que salga algo)")
    if not l_aud or not l_eje:
        w("   PARADA: falta alguna de las dos familias de caida. No se escribe.")
        print(NL.join(salida))
        return 1
    w("")

    w("D) EL TITULO, CON SUS TRES NUMERALES COMPUTADOS")
    titulo = titulo_de_la_entrada(len(claves_d) + len(claves_7), len(l_aud), len(l_eje))
    w("   %s" % titulo)
    w("")

    w("E) LOS TITULOS LITERALES DE CADA ADJUDICACION, LEIDOS DEL ACTA")
    titulos = {}
    for clave, _n in claves_d:
        pat = re.compile(r"^\s*\*\*`?%s`?[,.]" % re.escape(clave))
        res, err2 = titulo_de_la_negrita(lineas, inicio, fin, pat, clave)
        if err2:
            w("   %s -> %s" % (clave, err2))
            print(NL.join(salida))
            return 1
        titulos[clave] = res
        w("   %s (linea %d): %s" % (clave, res[0], res[1][:130]))
    for clave, _n in claves_7:
        pat = re.compile(r"^\s*\*\*%s " % re.escape(clave))
        res, err2 = titulo_de_la_negrita(lineas, inicio, fin, pat, clave)
        if err2:
            w("   %s -> %s" % (clave, err2))
            print(NL.join(salida))
            return 1
        titulos[clave] = res
        w("   %s (linea %d): %s" % (clave, res[0], res[1][:130]))
    w("")

    w("F) EL NUMERO DE LA ENTRADA, QUE NO SE TECLEA")
    halladas = SERIE.entradas()
    numero = SERIE.siguiente_libre(halladas)
    w("   serie recomputada de sus dos sedes: %d entradas" % len(halladas))
    w("   CIFRA colisiones: %d | CIFRA huecos: %d"
      % (len(SERIE.colisiones(halladas)), len(SERIE.huecos(halladas))))
    w("   SIGUIENTE LIBRE: R.%d" % numero)
    w("")

    w("G) LA DEUDA DE LA SERIE (TAREA 1.b), MEDIDA Y DECLARADA COMO SALTO")
    salto = actas_sin_entrada(halladas, 173, VUELTA_DEL_ACTA - 1)
    faltan, bajo, alto = salto
    w("   tramo mirado: actas 173 a %d" % (VUELTA_DEL_ACTA - 1))
    w("   CIFRA actas SIN entrada propia en la serie: %d" % len(faltan))
    w("   LAS QUE FALTAN: %s" % (", ".join(str(x) for x in faltan) or "(ninguna)"))
    w("   EXTREMO BAJO (ultimo registro que cubre un acta anterior al salto): %s"
      % ("R.%d cubre el acta %d" % bajo if bajo else "(ninguno)"))
    w("   EXTREMO ALTO (primer registro que cubre un acta posterior): %s"
      % ("R.%d cubre el acta %d" % alto if alto else "(ninguno)"))
    w("   (la entrada de esta vuelta cubre el acta %d y NO rellena el salto: la"
      % VUELTA_DEL_ACTA)
    w("    adjudicacion 7.4 manda documentarlo, no inventarlo)")
    w("")

    marca = "## R.%d." % numero
    texto_sede = io.open(SEDE, encoding="utf-8").read().replace(chr(13) + NL, NL)
    ya = ("## R.%d. %s" % (numero, titulo)) in texto_sede
    w("H) LA IDEMPOTENCIA, COMPROBADA ANTES DE ESCRIBIR")
    w("   la marca %r ya esta en la sede: %s"
      % (marca, "SI" if marca in texto_sede else "NO"))
    w("   la entrada entera ya esta: %s" % ("SI" if ya else "NO"))
    w("")

    entrada = armar_entrada(numero, titulo, claves_d, claves_7, titulos, l_aud,
                            l_eje, inicio, fin, len(l_aud_v), len(l_vie), salto)
    w("I) LA ENTRADA ARMADA")
    w("   %d bytes | %d lineas" % (len(entrada.encode("utf-8")), entrada.count(NL)))
    w("")

    if a.simular:
        w("J) MODO --simular: NO SE ESCRIBE NADA EN LA SEDE.")
        w("")
        w("LA ENTRADA, ENTERA:")
        for l in entrada.split(NL):
            w("   | " + l)
    elif ya:
        w("J) NO SE ESCRIBE: la entrada ya esta en la sede, byte a byte.")
    else:
        nuevo = texto_sede.rstrip(NL) + NL + NL + entrada
        io.open(SEDE, "w", encoding="utf-8", newline=NL).write(nuevo)
        w("J) ESCRITA EN docs/PENDIENTES.md")
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
    ruta = os.path.join(LOOP, "SALIDA_V%d_T1A_REGISTRO_R%d.txt"
                        % (VUELTA_QUE_ESCRIBE, numero))
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
