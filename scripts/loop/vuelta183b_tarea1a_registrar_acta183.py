# -*- coding: utf-8 -*-
r"""vuelta183b_tarea1a_registrar_acta183.py . EL ACTA 183 ENTERA, REGISTRADA EN LA
SERIE `R.N` EN LA FORMA DE LA CASA.

LA MAQUINA NO SE CLONA, SE IMPORTA, y eso lo adjudico la `6.6` del acta 172 como
correcto y obligatorio: `PALABRA` y `titulo_de_la_negrita` se importan de
`scripts/loop/vuelta172_tarea1_registrar_acta171.py`, y `claves_de_adjudicacion`,
`cuenta_por_patron` y `actas_sin_entrada` se importan de los registradores de las
vueltas 182 y 183, que son las sedes que la casa ya vigila. Lo unico propio de
este fichero es EL ACOTE DE SU ACTA, LOS PATRONES QUE SU ACTA NECESITA Y SUS
GLOSAS.

POR QUE HACE FALTA CODIGO PROPIO OTRA VEZ, MEDIDO Y NO SUPUESTO, Y SON TRES COSAS:

  1) LA FAMILIA DE ADJUDICACION CAMBIA DE NUMERO. El acta 182 las numeraba `7.n`
     en su seccion 7 y `5.D.n` en su seccion 5. EL ACTA 183 LAS NUMERA `5.n`, en
     su seccion 5, y su seccion 7 es LA METRICA DE CREDITO. Corrido el prefijo
     `7.` de la vuelta pasada sobre esta acta, da CERO, y esa cifra se publica al
     lado de la buena.

  2) LA CAIDA DEL EJECUTOR NO ESTA DONDE ESTABA. El acta 182 la escribia como
     ``**`E.1`.`` al principio de linea. EL ACTA 183 LA ESCRIBE DENTRO DEL TITULO
     DE SU PRIMERA ADJUDICACION: *"**5.1 LA CAIDA DEL EJECUTOR, `E.1`: LAS CUATRO
     SALIDAS SELLADAS..."*. Los dos patrones viejos cuentan CERO sobre esta acta y
     las dos cifras se publican. Se anade un patron, NO se ensancha el viejo hasta
     que trague.

  3) LAS CAIDAS PROPIAS DEL AUDITOR SON CERO, Y UN CERO SE PUBLICA CON SU
     DECLARACION AL LADO O NO VALE. El registrador de la 183 hacia PARADA si no
     encontraba ninguna, porque el acta 182 traia una. Aqui el cero es LA
     MEDICION CORRECTA, y para que no se confunda con un patron que no muerde, el
     instrumento EXIGE ADEMAS que el acta lo declare con todas las letras
     (*"NINGUNA CAIDA PROPIA ESTA VUELTA"*) y publica la linea donde lo dice. Si
     el patron diera cero Y el acta no lo declarara, eso SI seria PARADA.

LAS CIFRAS DEL TITULO NO SE TECLEAN: se cuentan del acta acotada. Ni el numero de
la entrada: lo devuelve `scripts/loop/serie_de_registros.py` recomputando la serie
de sus DOS sedes.

LO QUE ESTE FICHERO NO HACE: no toca el acta, no toca el reporte, no toca
`docs/plan/`, no corre la bateria y no escribe ningun veredicto. Escribe UNA
entrada en UNA sede, y si la entrada ya esta, NO la duplica y lo dice.

USO:
  python scripts/loop/vuelta183b_tarea1a_registrar_acta183.py
  python scripts/loop/vuelta183b_tarea1a_registrar_acta183.py --simular
  python scripts/loop/vuelta183b_tarea1a_registrar_acta183.py --mutacion
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

VUELTA_DEL_ACTA = 183
VUELTA_QUE_ESCRIBE = 183
SUFIJO_QUE_ESCRIBE = "183"
CABECERA_ACTA = "# ACTA DEL AUDITOR, VUELTA %d" % VUELTA_DEL_ACTA
PREFIJO_ADJ = "5."
PREFIJO_VIEJO = "7."

# EL NUMERAL CERO, QUE `PALABRA` NO TRAE PORQUE NINGUNA ACTA ANTERIOR LO NECESITO.
# Se extiende la tabla importada en vez de reescribirla, y se dice aqui.
PALABRA_CON_CERO = dict(PALABRA)
PALABRA_CON_CERO[0] = "cero"

# LA CAIDA DEL EJECUTOR, EN LA FORMA DEL ACTA 183: dentro del titulo de una
# adjudicacion. Los dos patrones de abajo son los VIEJOS y se conservan para
# publicar su CERO al lado, que es lo que prueba que hacia falta uno nuevo.
PAT_CAIDA_EJECUTOR_EN_TITULO = re.compile(
    r"^\*\*\d+\.\d+ .*CAIDA DEL EJECUTOR, `E\.(\d+)`")
PAT_CAIDA_EJECUTOR_VIEJA = re.compile(r"^\s*(?:-\s+)?\*\*`?E\.(\d+)`?[,.]")
PAT_CAIDA_AUDITOR_VIEJA = re.compile(r"^\s*(?:-\s+)?\*\*`?C\.(\d+)`?[,.]")
PAT_CAIDA_AUDITOR_PROSA = re.compile(r"^\*\*[^*]*CAIDA[^*]*`C\.(\d+)`")
FRASE_SIN_CAIDA_PROPIA = "NINGUNA CAIDA PROPIA"

# LA VIA DE CADA ADJUDICACION, escrita a mano porque es JUICIO del ejecutor sobre
# que hace ESTA vuelta con ella, y el juicio no sale de ningun instrumento. Lo
# que si sale de instrumento es el TITULO literal de cada una y su linea.
VIA = {
    "5.1": "EJECUTADA",
    "5.2": "EJECUTADA",
    "5.3": "SIN TOCAR NADA",
    "5.4": "SIN TOCAR NADA",
    "5.5": "SIN TOCAR NADA",
    "5.6": "EJECUTADA",
    "5.7": "EJECUTADA",
}

QUE_HACE_ESTA_VUELTA = {
    "5.1": ("EJECUTADA EN LA TAREA 1.b DE ESTA VUELTA, QUE ES SU OPERACION DE "
            "CODIGO. La caida se acata entera y no se discute: las cuatro salidas "
            "selladas decian que eran de la vuelta 176 y no lo eran. Lo que pasaba "
            "antes NO SE BORRA: el bloque H.2 del bloque de apertura de esta "
            "continuacion conto TRES lineas con `176` en cada una de las cuatro, "
            "DOCE en total, antes de que nadie tocara el lanzador. Y la reparacion "
            "no es teclear un 183 encima del 176: el numero y el nombre se computan "
            "de `os.path.basename(__file__)`, con un guarda propio que impide que "
            "el lanzador arranque si alguien vuelve a clavar uno."),
    "5.2": ("EJECUTADA EN LA TAREA 1.d DE ESTA VUELTA. El acta adjudica las tres "
            "rutas abreviadas A FAVOR del ejecutor y aun asi encarga escribirlas "
            "enteras, por el motivo que ella misma da: una ruta que hay que "
            "reconstruir mentalmente no se puede cotejar pegandola en un comando. "
            "Se escriben con su carpeta y su prefijo en la celda de prueba de la "
            "TAREA 1 del reporte de la 183."),
    "5.3": ("SE ACATA SIN TOCAR NADA, Y ES UNA CONCESION AL EJECUTOR. La correccion "
            "declarada de la TAREA 1.e de la 183 queda concedida entera, y el acta "
            "dice ademas que el error del encargo era del auditor. No hay trabajo "
            "pendiente en ella."),
    "5.4": ("SE ACATA SIN TOCAR NADA, Y ESTA VUELTA HACE LA MISMA CUENTA OTRA VEZ. "
            "Los dos arneses que entraron a la nomina sin estar encargados quedan "
            "concedidos por la regla del acta 176 punto 7.2. Esta vuelta anade UN "
            "TERCERO por la misma regla y con la misma medicion delante: "
            "`arneses_que_faltan()` daba `ultima 183, faltan 1` con el arnes de la "
            "TAREA 1.b fuera, y la nomina crece de 111 a 112 sin podar nada."),
    "5.5": ("SE ACATA SIN TOCAR NADA. El acta declara que la vuelta cortada NO es "
            "una caida, porque el reporte parcial dice hasta donde se llego. Esta "
            "vuelta es la continuacion que ese mismo reporte parcial reclama."),
    "5.6": ("EJECUTADA EN EL PRIMER COMMIT DE ESTA VUELTA. "
            "`scripts/loop/_v183_tallar_cierre.py` estaba sin seguir por git y NO "
            "se borro: entra a git con el bloque de apertura, porque es el tallador "
            "del cuerpo del cierre que la TAREA 2 va a necesitar."),
    "5.7": ("EJECUTADA, Y ES LA QUE ORDENA ESTA VUELTA ENTERA. La continuacion "
            "escribe SOBRE el reporte de la 183 por anexion, no abre uno nuevo y no "
            "lo archiva. El motivo es aritmetica de dos reglas escritas: "
            "`cerrar_reporte.py` exige la composicion de los nueve tramos, y "
            "`AUDITOR.md` 6.1 manda retomar en el tramo siguiente. Este fichero es "
            "de la continuacion y por eso su nombre lleva `183b`, pero la vuelta "
            "que registra el acta sigue siendo la 183."),
}


def cuerpo_del_acta(texto=None):
    """EL ACTA ACOTADA: (lineas, (inicio, fin), error). El fin es el final del
    fichero porque el acta 183 es la ultima escrita; si algun dia dejara de
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
    todas las letras son la misma cifra y NO son la misma evidencia. Esta funcion
    existe para que la segunda se pueda publicar."""
    return [i for i in range(inicio, fin + 1)
            if FRASE_SIN_CAIDA_PROPIA in lineas[i - 1]]


def titulo_de_la_entrada(n_adj, n_cai_aud, n_cai_eje):
    """El titulo, con sus TRES numerales COMPUTADOS y no tecleados, y con la
    concordancia dentro del computo. El CERO entra por `PALABRA_CON_CERO`, y va
    en plural porque en castellano el cero es plural."""
    def trozo(n, sing, plur):
        if n == 1:
            return "la %s" % sing
        return "las %s %s" % (PALABRA_CON_CERO[n], plur)
    return ("Registro de %s, %s del auditor y %s del ejecutor "
            "del acta de la vuelta %d"
            % (trozo(n_adj, "adjudicacion", "adjudicaciones"),
               trozo(n_cai_aud, "caida propia", "caidas propias"),
               trozo(n_cai_eje, "caida", "caidas"),
               VUELTA_DEL_ACTA))


def armar_entrada(numero, titulo, claves, titulos, l_aud, l_eje, l_declara,
                  inicio, fin, viejas_eje, viejas_aud, cero_prefijo_viejo, salto):
    faltan, bajo, alto = salto
    p = []
    p.append("## R.%d. %s" % (numero, titulo))
    p.append("")
    p.append("(Acta del auditor, vuelta %d, secciones 2, 5, 6 y 7; escrito en la"
             % VUELTA_DEL_ACTA)
    p.append("CONTINUACION de la vuelta %d, TAREA 1.a.)" % VUELTA_QUE_ESCRIBE)
    p.append("")
    p.append("Por adicion, como `R.21` a `R.44`. **Corte de todas las cifras de esta")
    p.append("entrada: 5 sep 2026.** El numero de esta entrada NO esta tecleado: lo computa")
    p.append("`scripts/loop/serie_de_registros.py` recomputando la serie de sus DOS sedes.")
    p.append("La SEDE tampoco se supone: sale de la adjudicacion 6.3 del acta 162, que es")
    p.append("la que citan los `R.30` a `R.44`. Salida:")
    p.append("`docs/loop/SALIDA_V%s_T1A_REGISTRO_R%d.txt`."
             % (SUFIJO_QUE_ESCRIBE, numero))
    p.append("")
    p.append("**ESTA ENTRADA SE ESCRIBE CON LA TAREA 1 EN CURSO Y LA TAREA 2 SIN CORRER,")
    p.append("ASI QUE SUS GLOSAS NO AFIRMAN EN PASADO LO QUE TODAVIA NO HA PASADO.** Es la")
    p.append("forma que la `6.4` del acta 172 adjudico como correcta y que la realidad")
    p.append("probo cuando la vuelta 172 se corto: donde una glosa dice EJECUTADA, la")
    p.append("prueba va nombrada con su fichero de salida; donde dice que va a ejecutarse,")
    p.append("se dice que **todavia no ha corrido** y no se disfraza.")
    p.append("")
    p.append("**Y LOS TRES NUMERALES DEL TITULO TAMPOCO ESTAN TECLEADOS:** se cuentan del")
    p.append("acta acotada (lineas %d a %d) y de ahi sale el numeral en palabra, incluida"
             % (inicio, fin))
    p.append("la concordancia. **%d adjudicaciones (`5.1` a `5.%d`, todas en la seccion 5),"
             % (len(claves), len(claves)))
    p.append("%d caidas propias del auditor y %d caida del ejecutor (`E.n`).**"
             % (len(l_aud), len(l_eje)))
    p.append("")
    p.append("**ESTA ACTA NUMERA SUS ADJUDICACIONES `5.n` Y LA ANTERIOR LAS NUMERABA")
    p.append("`7.n`.** Corrido el prefijo de la vuelta pasada sobre esta acta, da **%d**."
             % cero_prefijo_viejo)
    p.append("Su seccion 7 no es de adjudicaciones: es LA METRICA DE CREDITO. La cifra de")
    p.append("cero se publica al lado de la buena y no se resuelve copiando.")
    p.append("")
    p.append("**Y LA CAIDA DEL EJECUTOR NO ESTA DONDE ESTABA.** El acta 182 la escribia")
    p.append("como ``**`E.1`.`` al principio de linea; **el acta 183 la escribe DENTRO DEL")
    p.append("TITULO de su primera adjudicacion**. El patron viejo, corrido sobre esta")
    p.append("acta, cuenta **%d**. Se anade un patron, no se ensancha el viejo hasta que"
             % viejas_eje)
    p.append("trague.")
    p.append("")
    p.append("**LAS CAIDAS PROPIAS DEL AUDITOR SON CERO, Y EL CERO VA CON SU DECLARACION")
    p.append("AL LADO.** Los dos patrones de caida propia cuentan **%d** sobre esta acta,"
             % viejas_aud)
    p.append("y un cero que sale de un patron que no muerde no es evidencia de nada. Lo que")
    p.append("lo sostiene es que **el acta lo declara con todas las letras**, en la linea")
    p.append("**%s**: *\"NINGUNA CAIDA PROPIA ESTA VUELTA, Y DECLARO EL METODO QUE LA EVITO"
             % (", ".join(str(x) for x in l_declara) or "(ninguna)"))
    p.append("PORQUE ESTUVE A UN PASO DE UNA\"*. **Si el patron diera cero y el acta no lo")
    p.append("declarara, el instrumento haria PARADA en vez de escribir esta entrada.**")
    p.append("")
    p.append("**LAS %s ADJUDICACIONES, CON SU LINEA EN EL ACTA LEIDA HOY.** El titulo de"
             % PALABRA_CON_CERO[len(claves)].upper())
    p.append("cada una es LITERAL del fichero; la glosa que sigue es prosa del ejecutor y")
    p.append("va marcada como tal.")
    p.append("")
    for clave, _n in claves:
        ln, tit = titulos[clave]
        p.append("  - **%s (`docs/loop/ACTA_AUDITOR.md:%d`, leida hoy). VIA: %s.** Titulo"
                 % (clave, ln, VIA[clave]))
        p.append("    literal del acta: *\"%s\"*" % tit)
        p.append("    **QUE HACE ESTA VUELTA CON ELLA (glosa del ejecutor, no del acta):** %s"
                 % QUE_HACE_ESTA_VUELTA[clave])
    p.append("")
    p.append("**LA CAIDA DEL EJECUTOR, EN LA LINEA %s, Y ACUMULA.**"
             % ", ".join(str(x) for x in l_eje))
    p.append("El `E.1` es **CIFRA PUBLICADA EN LA CUARTA SEDE**, que es `scripts/`: las")
    p.append("cuatro salidas selladas de la bateria de la 183 declaraban en sus primeras")
    p.append("lineas que eran de la vuelta 176 y que las lanzo el fichero de la 176, y las")
    p.append("dos cosas eran falsas. **La racha de cifra publicada pasa de 0 a 1, y dos")
    p.append("tandas seguidas serian PARADA.** El acta dice ademas dos cosas que esta")
    p.append("entrada recoge sin adornar: que **el fichero lo escribio la vuelta 182 en su")
    p.append("TAREA 5** y que la caida se registra **contra el rol** y no contra la sesion")
    p.append("de la 183; y que **el hueco de verificacion que la dejo pasar es del propio")
    p.append("auditor**, que dio el fichero por bueno corriendo los dos unicos carriles que")
    p.append("no imprimen esas lineas. **Corregida en la TAREA 1.b de esta continuacion,")
    p.append("en codigo y con caso positivo por mutacion.**")
    p.append("")
    p.append("**LA DEUDA DE LA SERIE, QUE SIGUE DOCUMENTADA COMO SALTO Y SIN RELLENAR.**")
    p.append("Se vuelve a medir en esta vuelta en vez de heredarse del `R.44`:")
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
    p.append("de las cinco `D` con el diferenciador ya presente el dia del veredicto sigue")
    p.append("**registrada y sin resolver**; el instrumento de vigencia de las ocho `A`")
    p.append("rancias por `P.5` **sigue sin cablear**, porque su adjudicacion lo manda a la")
    p.append("primera vuelta de trabajo y esta sigue siendo **vuelta de bateria**; y el")
    p.append("TRAMO 1 de la cola post fusion, el par **2.464**, **no se relee aqui**.")
    return NL.join(p) + NL


def _acta_fabricada(n_adj, caidas_aud, caidas_eje, declara_cero=True):
    """UN ACTA DE MENTIRA para el caso positivo por mutacion. NO toca el repo.

    Escribe la caida del ejecutor EN LA FORMA DEL ACTA 183 (dentro del titulo de
    una adjudicacion) y no en la del acta 182, que es justo la diferencia que
    este fichero existe para cubrir."""
    L = ["# ACTA DEL AUDITOR, VUELTA %d (fabricada)" % VUELTA_DEL_ACTA, ""]
    if declara_cero and caidas_aud == 0:
        L += ["**%s ESTA VUELTA, Y LO DECLARO.** Y su cuerpo."
              % FRASE_SIN_CAIDA_PROPIA, ""]
    for k in range(1, caidas_aud + 1):
        L += ["**MI CAIDA PROPIA, `C.%d`, DE MENTIRA Y EN NEGRITA.** Y su cuerpo." % k, ""]
    L += ["## 5. LAS ADJUDICACIONES", ""]
    for k in range(1, n_adj + 1):
        if k <= caidas_eje:
            L += ["**5.%d LA CAIDA DEL EJECUTOR, `E.%d`: UN TITULO DE MENTIRA.** Y su "
                  "cuerpo." % (k, k), ""]
        else:
            L += ["**5.%d UN TITULO DE MENTIRA NUMERO %d.** Y su cuerpo." % (k, k), ""]
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
    w("CASO POSITIVO POR MUTACION de vuelta183b_tarea1a_registrar_acta183.py")
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
        # LAS TRES VARIABLES SON COMPUTADAS: salen de correr los contadores de
        # verdad sobre el acta fabricada, no de escribirlas aqui.
        cl = claves_de_adjudicacion(lineas, ini, fin, PREFIJO_ADJ)
        aud = cuenta_por_patron(lineas, ini, fin, PAT_CAIDA_AUDITOR_PROSA)
        eje = cuenta_por_patron(lineas, ini, fin, PAT_CAIDA_EJECUTOR_EN_TITULO)
        ok = (len(cl) == n_adj and len(aud) == n_aud and len(eje) == n_eje)
        titulo = titulo_de_la_entrada(len(cl), len(aud), len(eje))
        w("   acta fabricada con adj=%d aud=%d eje=%d" % (n_adj, n_aud, n_eje))
        w("      los contadores dicen adj=%d aud=%d eje=%d -> %s"
          % (len(cl), len(aud), len(eje), "CALZA" if ok else "NO CALZA"))
        w("      titulo computado: %s" % titulo)
        if not ok:
            fallos += 1
    w("")
    w("LA MUTACION DEL VALOR ESPERADO, QUE ES LO QUE PRUEBA QUE EL CASO PUEDE CAER:")
    texto = _acta_fabricada(7, 0, 1)
    lineas, (ini, fin), _e = cuerpo_del_acta(texto)
    medido = len(claves_de_adjudicacion(lineas, ini, fin, PREFIJO_ADJ))
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
    w("LA SEGUNDA MUTACION: EL PATRON DE LA CAIDA DEL EJECUTOR. Con el patron del")
    w("acta 182 el contador tiene que dar CERO sobre un acta que la escribe dentro")
    w("del titulo de una adjudicacion, que es el motivo de este fichero.")
    con_viejo = len(cuenta_por_patron(lineas, ini, fin, PAT_CAIDA_EJECUTOR_VIEJA))
    w("   patron del acta 182 sobre acta en forma 183 -> %d caidas" % con_viejo)
    w("   EL CASO CAE CON EL PATRON VIEJO: %s" % ("SI" if con_viejo == 0 else "NO"))
    if con_viejo != 0:
        fallos += 1
    w("")
    w("LA TERCERA MUTACION: EL PREFIJO DE LA ADJUDICACION. Con el prefijo `7.` el")
    w("contador tiene que dar CERO sobre un acta que numera `5.n`.")
    con_7 = len(claves_de_adjudicacion(lineas, ini, fin, PREFIJO_VIEJO))
    w("   prefijo %r sobre acta de %r -> %d adjudicaciones"
      % (PREFIJO_VIEJO, PREFIJO_ADJ, con_7))
    w("   EL CASO CAE CON EL PREFIJO VIEJO: %s" % ("SI" if con_7 == 0 else "NO"))
    if con_7 != 0:
        fallos += 1
    w("")
    w("LA CUARTA MUTACION: EL CERO DE CAIDAS PROPIAS CON Y SIN SU DECLARACION. Es")
    w("la diferencia entre un cero medido y un cero que nadie sostiene, y el")
    w("instrumento tiene que distinguirlos.")
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
    w("LA QUINTA MUTACION: EL SALTO. actas_sin_entrada() es PURA y se importa del")
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
    w("LA SEXTA MUTACION: EL NUMERAL CERO EN EL TITULO. `PALABRA` no trae el cero")
    w("y la tabla se extiende aqui; el titulo tiene que decirlo y concordar.")
    t0 = titulo_de_la_entrada(7, 0, 1)
    w("   titulo con cero caidas propias: %s" % t0)
    ok_cero = "las cero caidas propias del auditor" in t0 and "la caida del ejecutor" in t0
    w("   DICE EL CERO Y CONCUERDA: %s" % ("SI" if ok_cero else "NO"))
    if not ok_cero:
        fallos += 1
    t1 = titulo_de_la_entrada(7, 2, 1)
    w("   y con dos, para que se vea que la concordancia no esta clavada: %s" % t1)
    if "las dos caidas propias del auditor" not in t1:
        fallos += 1
    w("")
    w("CIFRA fallos: %d" % fallos)
    w("VEREDICTO: %s" % ("VERDE" if fallos == 0 else "ROJO"))
    t = NL.join(salida) + NL
    ruta = os.path.join(LOOP, "SALIDA_V%s_T1A_MUTACION_REGISTRO_183.txt"
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
    w("CONTINUACION DE LA VUELTA %d, TAREA 1.a: EL ACTA %d ENTERA, REGISTRADA"
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

    w("B) LAS ADJUDICACIONES, CONTADAS Y NO TECLEADAS")
    claves = claves_de_adjudicacion(lineas, inicio, fin, PREFIJO_ADJ)
    w("   prefijo de esta acta: %r" % PREFIJO_ADJ)
    w("   CIFRA adjudicaciones halladas: %d" % len(claves))
    for clave, cuantas in claves:
        w("      %s -> %d aparicion(es)" % (clave, cuantas))
    viejas = claves_de_adjudicacion(lineas, inicio, fin, PREFIJO_VIEJO)
    w("   EL CONTRASTE QUE PRUEBA QUE HACIA FALTA CODIGO PROPIO:")
    w("      el prefijo %r de la vuelta pasada -> %d sobre esta acta"
      % (PREFIJO_VIEJO, len(viejas)))
    w("      (su seccion 7 no es de adjudicaciones: es la metrica de credito)")
    dobles = [c for c, n in claves if n != 1]
    if dobles:
        w("   PARADA: hay claves repetidas dentro del acta: %s" % ", ".join(dobles))
        print(NL.join(salida))
        return 1
    if len(claves) != len(VIA):
        w("   PARADA: el acta trae %d adjudicaciones y las glosas cubren %d."
          % (len(claves), len(VIA)))
        w("   No se escribe una entrada con una glosa inventada ni con una de menos.")
        print(NL.join(salida))
        return 1
    w("")

    w("C) LAS CAIDAS, POR SUS FAMILIAS, Y LOS PATRONES VIEJOS AL LADO")
    l_aud = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_AUDITOR_PROSA)
    l_aud_v = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_AUDITOR_VIEJA)
    l_eje = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_EJECUTOR_EN_TITULO)
    l_eje_v = cuenta_por_patron(lineas, inicio, fin, PAT_CAIDA_EJECUTOR_VIEJA)
    l_declara = lineas_que_declaran_cero_caidas(lineas, inicio, fin)
    w("   CAIDAS DEL EJECUTOR (patron del titulo, el del acta 183): %d, en las lineas %s"
      % (len(l_eje), ", ".join(str(x) for x in l_eje) or "(ninguna)"))
    w("   EL PATRON DEL ACTA 182 (`**`E.n`.` al principio de linea): %d" % len(l_eje_v))
    w("   CAIDAS PROPIAS DEL AUDITOR (patron de negrita de frase): %d" % len(l_aud))
    w("   EL PATRON DEL ACTA 181 (`**`C.n`.` al principio de linea): %d" % len(l_aud_v))
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

    w("D) EL TITULO, CON SUS TRES NUMERALES COMPUTADOS")
    titulo = titulo_de_la_entrada(len(claves), len(l_aud), len(l_eje))
    w("   %s" % titulo)
    w("")

    w("E) LOS TITULOS LITERALES DE CADA ADJUDICACION, LEIDOS DEL ACTA")
    titulos = {}
    for clave, _n in claves:
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

    w("G) LA DEUDA DE LA SERIE, REMEDIDA EN ESTA VUELTA Y NO HEREDADA")
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
    w("H) LA IDEMPOTENCIA, COMPROBADA ANTES DE ESCRIBIR")
    w("   la marca %r ya esta en la sede: %s"
      % (marca, "SI" if marca in texto_sede else "NO"))
    w("   la entrada entera ya esta: %s" % ("SI" if ya else "NO"))
    w("")

    entrada = armar_entrada(numero, titulo, claves, titulos, l_aud, l_eje,
                            l_declara, inicio, fin, len(l_eje_v), len(l_aud_v),
                            len(viejas), salto)
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
    ruta = os.path.join(LOOP, "SALIDA_V%s_T1A_REGISTRO_R%d.txt"
                        % (SUFIJO_QUE_ESCRIBE, numero))
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
