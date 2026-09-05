# -*- coding: utf-8 -*-
r"""_v172_construir_registrador.py . ANDAMIO DE UN SOLO USO DE LA VUELTA 172.

CONSTRUYE `scripts/loop/vuelta172_tarea1_registrar_acta171.py` como CLON
DECLARADO de `vuelta171_tarea1_registrar_acta170.py`, desde el original y en un
solo acto, para que el clon sea REPRODUCIBLE y no una pila de parches a mano.

Cada sustitucion lleva su `assert` de cuantas apariciones espera: si el original
cambia debajo, esto CAE en vez de escribir un clon a medias.

Lo que cambia, y nada mas que esto:
  A. las constantes de vuelta (170 -> 171 como acta leida, 171 -> 172 como
     vuelta que escribe) y los rotulos que las nombran;
  B. las expectativas de la pasada real del arnes de mutacion (el acta 171 trae
     DOCE adjudicaciones y TRES caidas, y el reparto da SIETE y CINCO);
  C. el docstring, la tabla `VIA` y los dos diccionarios de glosa;
  D. el texto de la entrada: `VIA PREVISTA` en vez de `VIA`, el aviso de que la
     entrada se escribe antes que las tareas, y el parrafo del patron.

EL MECANISMO NO SE TOCA: `cuerpo_del_acta`, `claves_de_adjudicacion`,
`titulo_de_la_negrita`, `titulo_de_la_entrada` y `prueba_de_mutacion` se heredan
byte a byte.

USO:  python scripts/loop/_v172_construir_registrador.py
"""
import io
import os
import py_compile
import shutil

NL = chr(10)
BS = chr(92)
CO = chr(34)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "scripts", "loop")
ORIGEN = os.path.join(LOOP, "vuelta171_tarea1_registrar_acta170.py")
DESTINO = os.path.join(LOOP, "vuelta172_tarea1_registrar_acta171.py")

import _v172_parche_glosas as G  # noqa: E402

CAMBIOS = 0


def rep(t, viejo, nuevo, veces=1):
    global CAMBIOS
    n = t.count(viejo)
    assert n == veces, "esperaba %d de %r, hay %d" % (veces, viejo[:70], n)
    CAMBIOS += n
    return t.replace(viejo, nuevo)


DOC = 'r"""vuelta172_tarea1_registrar_acta171.py . TAREA 1.b de la vuelta 172.' + NL + '''
REGISTRA EN LA FORMA DE LA CASA (`R.N`) EL ACTA 171 ENTERA: SUS ADJUDICACIONES
`6.n` Y LAS CAIDAS PROPIAS DEL AUDITOR de su seccion 3. Clon declarado de
`vuelta171_tarea1_registrar_acta170.py`, construido desde el original por
`scripts/loop/_v172_construir_registrador.py` y SIN tocarle el mecanismo.
NINGUNA CIFRA SE TECLEA: el numero de la entrada lo computa
`serie_de_registros.py` recomputando la serie de sus DOS sedes; las
adjudicaciones se barren del acta parando en el primer hueco; las caidas se
cuentan de las negritas `CAIDA n` del cuerpo acotado; y los numerales en palabra
del titulo salen de esos dos conteos.

QUE CAMBIA RESPECTO DEL INSTRUMENTO DE LA VUELTA 171, Y LO QUE IMPORTA ES LO
TERCERO:

  (1) EL CUERPO ACOTADO pasa del acta 170 al acta 171, que es hoy la ULTIMA del
      fichero. Las dos cifras se mueven: el `R.40` registro DOCE adjudicaciones
      y CUATRO caidas; el acta 171 trae DOCE y TRES, y los dos numerales salen
      solos del conteo.

  (2) EL PATRON DE CAIDA NO SE TOCA. El acta 171 escribe sus caidas con la misma
      forma que la 170 (vineta y comillas inversas), asi que el patron adaptado
      en la vuelta 171 casa con las tres sin cambiar una letra. El conteo con el
      patron VIEJO se sigue publicando al lado, y sigue dando cero: adaptar un
      patron una vez y no volver a mirarlo seria la misma caida al reves.

  (3) LAS GLOSAS NO AFIRMAN EN PASADO, Y ESTE ES EL CAMBIO QUE IMPORTA. La
      adjudicacion 6.3 del acta 171 destapo que el `R.40`, escrito en la TAREA
      1.a de la vuelta 171, publicaba "VIA: EJECUTADA" y "EJECUTADA, TAREA 3 de
      esta vuelta ... las 16 filas ganan LD-139 a LD-154" cuando LA TAREA 3 NO
      SE CORRIO. La causa era de orden y esta medida: la entrada se escribe la
      PRIMERA de la vuelta, cuando las demas tareas todavia no han corrido, y
      nadie vuelve a ella. AQUI ESO NO PUEDE VOLVER A PASAR POR LA FORMA DE LA
      FRASE: el campo se llama VIA PREVISTA, todas las glosas hablan de lo que
      esta vuelta VA A HACER, ninguna afirma que ya lo hizo, y la entrada dice
      en su cabecera que se escribio antes que las tareas 2 a 5. LA CONFIRMACION
      MEDIDA SE ANEXA AL CIERRE, por adicion y sin tocar la letra de arriba, con
      `scripts/loop/vuelta172_tarea1b_confirmar_r41.py`.

      NO ES DOCTRINA NUEVA: es EJECUTOR.md 1, "toda afirmacion sobre el estado
      del registro se escribe CON LA MEDICION DEL DIA AL LADO. Si no hay linea
      que citar, la afirmacion no se escribe". Una glosa escrita antes de que la
      tarea corra no tiene linea que citar, asi que no puede escribirse en
      pasado.

USO:  python scripts/loop/vuelta172_tarea1_registrar_acta171.py
      python scripts/loop/vuelta172_tarea1_registrar_acta171.py --mutar
"""'''

VIA = '''VIA = {
    "6.1": "EJECUTADA",
    "6.2": "EJECUTADA",
    "6.3": "EJECUTADA",
    "6.4": "EJECUTADA",
    "6.5": "EJECUTADA",
    "6.6": "EJECUTADA",
    "6.7": "SIN TOCAR NADA",
    "6.8": "SIN TOCAR NADA",
    "6.9": "SIN TOCAR NADA",
    "6.10": "EJECUTADA",
    "6.11": "SIN TOCAR NADA",
    "6.12": "SIN TOCAR NADA",
}'''

PATRON_VIEJO = [
    '        "**Y AQUI HAY UNA ADAPTACION DE PATRON QUE SE DECLARA EN VEZ DE PASAR CALLANDO,BN"',
    '        "PORQUE UN PATRON QUE SE AFLOJA SIN DECIRLO ES UNA GUARDA MENOS.** El acta 169BN"',
    '        "escribia sus caidas como `**CAIDA 1. ...**` al principio de linea; el acta 170BN"',
    '        "las escribe como vineta y con comillas inversas, ``- **`CAIDA 1`. ...**``. ElBN"',
    '        "patron de la vuelta 170, corrido sobre el acta 170, cuenta **%d**; el de estaBN"',
    '        "vuelta, que acepta la vineta y las comillas como OPCIONALES, cuenta **%d**. LasBN"',
    '        "dos cifras se publican al lado y el arnes hermano prueba por mutacion que elBN"',
    '        "patron nuevo casa con **las dos formas** y sigue exigiendo la negrita, elBN"',
    '        "numero y el signo detras: adaptar no es aflojar.BNBN"',
]

PATRON_NUEVO = [
    '        "**Y EL PATRON DE CAIDA NO SE TOCA ESTA VEZ, Y ESO TAMBIEN SE DICE.** El actaBN"',
    '        "170 estreno la forma de vineta con comillas inversas y la vuelta 171 adapto elBN"',
    '        "patron para verla sin dejar de exigir la negrita, el numero y el signo. **ElBN"',
    '        "acta 171 usa esa MISMA forma**, asi que aqui el patron se hereda TAL CUAL, sinBN"',
    '        "ensancharlo ni una letra. Las dos cifras se siguen publicando al lado para queBN"',
    '        "se vea que no se afloja: el patron VIEJO, el de la vuelta 170, corrido sobre elBN"',
    '        "acta 171, cuenta **%d**; el heredado cuenta **%d**. **Un patron que se adaptaBN"',
    '        "una vez y no se vuelve a mirar es la misma caida del reves.**BNBN"',
]

AVISO = [
    '    trozos.append(',
    '        "> **ESTA ENTRADA SE ESCRIBE LA PRIMERA DE LA VUELTA, ANTES DE QUE LAS TAREAS 2BN"',
    '        "> A 5 HAYAN CORRIDO, Y POR ESO NINGUNA DE SUS GLOSAS AFIRMA EN PASADO.** LaBN"',
    '        "> adjudicacion `6.3` del acta 171 destapo que el `R.40` publicaba *~C~VIA:BN"',
    '        "> EJECUTADA~C~* y *~C~EJECUTADA, TAREA 3 de esta vuelta ... las 16 filas ganan `LD-139`BN"',
    '        "> a `LD-154`~C~* **cuando la TAREA 3 no se corrio**. La causa estaba medida y eraBN"',
    '        "> de orden: la entrada se escribe antes que las tareas y **nadie vuelve aBN"',
    '        "> ella**.BN"',
    '        "> BN"',
    '        "> **AQUI ESO NO PUEDE VOLVER A PASAR POR LA FORMA DE LA FRASE.** El campo seBN"',
    '        "> llama **VIA PREVISTA**, cada glosa dice *~C~VA A EJECUTARSE EN LA TAREA n DE ESTABN"',
    '        "> VUELTA, Y AL ESCRIBIR ESTA LINEA TODAVIA NO HA CORRIDO~C~*, y **la confirmacionBN"',
    '        "> MEDIDA se anexa al cierre de la vuelta**, por adicion y sin tocar una letraBN"',
    '        "> de arriba, con `scripts/loop/vuelta172_tarea1b_confirmar_r41.py`. **Si estaBN"',
    '        "> vuelta se corta antes de esa anexion, lo que queda escrito aqui sigue siendoBN"',
    '        "> cierto**, porque solo dice lo que se pensaba hacer.BN"',
    '        "> BN"',
    '        "> **NO ES DOCTRINA NUEVA:** es `EJECUTOR.md` 1, *~C~toda afirmacion sobre elBN"',
    '        "> estado del registro se escribe CON LA MEDICION DEL DIA AL LADO; si no hayBN"',
    '        "> linea que citar, la afirmacion no se escribe~C~*. Una glosa escrita antes deBN"',
    '        "> que la tarea corra no tiene linea que citar.BNBN")',
]


def d(lineas):
    """BN es el escape de salto de linea y ~C~ la comilla doble ESCAPADA, para no
    tener que escribir barras invertidas dentro de este andamio."""
    return NL.join(lineas).replace("BN", BS + "n").replace("~C~", BS + CO) + NL


def main():
    t = io.open(ORIGEN, encoding="utf-8").read().replace(chr(13) + NL, NL)

    # ---------------------------------------------------- A. LAS CONSTANTES
    t = rep(t, 'CABECERA_ACTA = "# ACTA DEL AUDITOR, VUELTA 170"' + NL +
            'VUELTA_DEL_ACTA = 170' + NL + 'VUELTA_QUE_ESCRIBE = 171',
            'CABECERA_ACTA = "# ACTA DEL AUDITOR, VUELTA 171"' + NL +
            'VUELTA_DEL_ACTA = 171' + NL + 'VUELTA_QUE_ESCRIBE = 172')
    t = rep(t, 'FRONTERA_FALSA = "# ACTA DEL AUDITOR, VUELTA 171 (frontera de mentira)"',
            'FRONTERA_FALSA = "# ACTA DEL AUDITOR, VUELTA 172 (frontera de mentira)"')
    t = rep(t, '"""Un acta 170 DE MENTIRA, en memoria.', '"""Un acta 171 DE MENTIRA, en memoria.')
    t = rep(t, 'print("VUELTA 171, TAREA 1.a: CASO POSITIVO POR MUTACION DEL REGISTRADOR DEL ACTA 170")',
            'print("VUELTA 172, TAREA 1.b: CASO POSITIVO POR MUTACION DEL REGISTRADOR DEL ACTA 171")')
    t = rep(t, 'print("VUELTA %d, TAREA 1.a: EL ACTA %d ENTERA, REGISTRADA EN LA FORMA DE LA CASA"',
            'print("VUELTA %d, TAREA 1.b: EL ACTA %d ENTERA, REGISTRADA EN LA FORMA DE LA CASA"')
    t = rep(t, '# `vuelta171_tarea1a_mutacion_registro.py`, que es el que la bateria ve.',
            '# `vuelta172_tarea1b_mutacion_registro.py`, que es el que la bateria ve.')
    # LA LINEA DE CONSOLA QUE NOMBRABA EL ACTA 170 DENTRO DEL INSTRUMENTO QUE LEE
    # LA 171. Se hereda del original y no la caza ningun assert de cifra, porque
    # es prosa de consola. Se corrige aqui para que el clon siguiente no la
    # arrastre. LA SALIDA QUE ESCRIBIO EL R.41 ES ANTERIOR A ESTA CORRECCION Y NO
    # SE TOCA: docs/loop/SALIDA_V172_T1B_REGISTRO_ACTA_171.txt sigue diciendo la
    # frase vieja, que es lo que de verdad se imprimio.
    t = rep(t, '    print("   (la diferencia es la que el docstring predice: el acta 170 escribe")' + NL +
            '    print("    sus caidas como vineta y con comillas inversas)")',
            '    print("   (la diferencia es la que el docstring predice: el acta 171 escribe")' + NL +
            '    print("    sus caidas como vineta y con comillas inversas, igual que la 170,")' + NL +
            '    print("    asi que el patron heredado las ve y el viejo no ve ninguna)")')

    # ------------------------------- B. LAS EXPECTATIVAS DE LA PASADA REAL
    t = rep(t, 'print("   cuerpo del acta 170: lineas %d a %d" % (ri, rf))',
            'print("   cuerpo del acta 171: lineas %d a %d" % (ri, rf))')
    t = rep(t, 'casos.append(("H_el_acta_170_trae_DOCE_adjudicaciones", n_adj, 12))',
            'casos.append(("H_el_acta_171_trae_DOCE_adjudicaciones", n_adj, 12))')
    t = rep(t, 'casos.append(("H_el_acta_170_trae_CUATRO_caidas", n_cai, 4))',
            'casos.append(("H_el_acta_171_trae_TRES_caidas", n_cai, 3))')
    t = rep(t, 'casos.append(("H_y_cero_veces_dentro_del_acta_170",',
            'casos.append(("H_y_cero_veces_dentro_del_acta_171",')
    t = rep(t, 'casos.append(("H_las_dieciseis_negritas_se_leen_sin_error", sin_error, 16))',
            'casos.append(("H_las_quince_negritas_se_leen_sin_error", sin_error, 15))')
    t = rep(t, 'casos.append(("H_el_titulo_que_saldra_dice_doce_y_cuatro",' + NL +
            '                  titulo_de_la_entrada(n_adj, n_cai),' + NL +
            '                  "Registro de las doce adjudicaciones y las cuatro caidas propias "' + NL +
            '                  "del acta de la vuelta 170"))',
            'casos.append(("H_el_titulo_que_saldra_dice_doce_y_tres",' + NL +
            '                  titulo_de_la_entrada(n_adj, n_cai),' + NL +
            '                  "Registro de las doce adjudicaciones y las tres caidas propias "' + NL +
            '                  "del acta de la vuelta 171"))')
    t = rep(t, 'casos.append(("H_el_reparto_real_da_OCHO_ejecutadas", len(ejecutadas), 8))',
            'casos.append(("H_el_reparto_real_da_SIETE_ejecutadas", len(ejecutadas), 7))')
    t = rep(t, 'casos.append(("H_y_CUATRO_sin_tocar_nada", len(sin_tocar), 4))',
            'casos.append(("H_y_CINCO_sin_tocar_nada", len(sin_tocar), 5))')
    t = rep(t, 'casos.append(("G_las_caidas_sin_glosa_se_detectan", len(sin_glosa_c), 2))',
            'casos.append(("G_las_caidas_sin_glosa_se_detectan", len(sin_glosa_c), 3))')

    # ------------------------------------------- C. DOCSTRING, VIA Y GLOSAS
    i = t.index('r"""vuelta171_tarea1_registrar_acta170.py')
    j = t.index('USO:  python scripts/loop/vuelta171_tarea1_registrar_acta170.py')
    j = t.index('"""', j) + 3
    t = t[:i] + DOC + t[j:]
    CAMBIOS_DOC = 1

    i = t.index('VIA = {')
    j = t.index('}', i) + 1
    t = t[:i] + VIA + t[j:]

    i = t.index("QUE_HACE_ESTA_VUELTA = {")
    k = t.index(NL + "def cuerpo_del_acta():")
    t = t[:i] + G.QUE_HACE + NL + G.CAIDAS + t[k:]

    # ----------------------------------------- D. EL TEXTO DE LA ENTRADA
    t = rep(t, '. VIA: %s.** Titulo', '. VIA PREVISTA: %s.** Titulo')
    t = rep(t, '"**EL REPARTO POR VIA, CONTADO Y NO TECLEADO:** %s.',
            '"**EL REPARTO POR VIA PREVISTA, CONTADO Y NO TECLEADO:** %s.')
    t = rep(t, 'print("I) EL REPARTO POR VIA, CONTADO Y NO TECLEADO")',
            'print("I) EL REPARTO POR VIA PREVISTA, CONTADO Y NO TECLEADO")')
    t = rep(t, 'TAREA 1.a.)', 'TAREA 1.b.)')
    t = rep(t, '"Por adicion, como `R.21` a `R.39`. **Corte de todas las cifras de esta entrada:',
            '"Por adicion, como `R.21` a `R.40`. **Corte de todas las cifras de esta entrada:')
    t = rep(t, '"4 sep 2026.**', '"5 sep 2026.**')
    t = rep(t, 'SALIDA_V%d_T1A_REGISTRO_ACTA_%d.txt', 'SALIDA_V%d_T1B_REGISTRO_ACTA_%d.txt')
    t = rep(t, 'concordancia**. **EL `R.39` REGISTRO DOCE Y TRES; ESTE REGISTRA %d Y %d.**',
            'concordancia**. **EL `R.40` REGISTRO DOCE Y CUATRO; ESTE REGISTRA %d Y %d.**')
    t = rep(t, d(PATRON_VIEJO), d(PATRON_NUEVO))
    ancla = '           todas[0], VUELTA_QUE_ESCRIBE, VUELTA_DEL_ACTA))' + NL
    t = rep(t, ancla, ancla + d(AVISO))

    io.open(DESTINO, "w", encoding="utf-8", newline=NL).write(t)
    py_compile.compile(DESTINO, doraise=True)
    print("CONSTRUIDO: %s" % os.path.relpath(DESTINO, RAIZ).replace(os.sep, "/"))
    print("CIFRA sustituciones con assert: %d (mas docstring, VIA y glosas)" % CAMBIOS)
    print("COMPILA: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
