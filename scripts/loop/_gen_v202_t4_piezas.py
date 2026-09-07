# -*- coding: utf-8 -*-
r"""_gen_v202_t4_piezas.py . LAS PIEZAS QUE CAMBIAN DEL REGISTRADOR DE LA VUELTA
202 RESPECTO AL DE LA 201.

Fichero de computo con PREFIJO DE GUION BAJO: fuera del censo y fuera de la
nomina. No es un lector ni un arnes: es el molde del que sale
`scripts/loop/_v202_t4_registrar_actas.py`, que se genera de
`scripts/loop/_v201_t1_registrar_actas.py` copiando todo lo demas BYTE A BYTE.
"""
NL = chr(10)

DOCSTRING = r'''r"""_v202_t4_registrar_actas.py . LAS DOS ENTRADAS DE LA SERIE `R.N` DE LA
VUELTA 202: LA DEL ACTA 173 (`R.63`) Y LA DEL ACTA 174 (`R.64`), QUE SON LAS DOS
MAS VIEJAS DE LA DEUDA.

ADJUDICADA POR EL ACTA 201 EN SU `4.9`: la deuda son OCHO actas seguidas, las 173
a las 180, y se pagan DE LA MAS VIEJA A LA MAS NUEVA, DOS POR VUELTA. Esta tarea
va DETRAS del trabajo de plan y nunca delante, porque la moratoria dice que EL
TRABAJO ES EL PLAN HASTA AGOTARLO.

PREFIJO DE GUION BAJO, Y NO ES UN CAPRICHO. La moratoria de maquinaria
(`AUDITOR.md` 6.3) prohibe fabricar arneses, guardas y lectores nuevos, y esta
vuelta NO TIENE NINGUNA EXCEPCION. La adjudicacion `4.5` del acta 199 dice con
sus palabras que un computo de una vuelta que muere con ella, con prefijo de
guion bajo, fuera del censo y fuera de la nomina, y que no vigila a nadie, NO ES
MAQUINARIA. Este fichero es eso, y es CLON DECLARADO de
`scripts/loop/_v201_t1_registrar_actas.py`, generado de el programaticamente con
`scripts/loop/_gen_v202_t4.py`.

Y LO MAS IMPORTANTE: NO ESCRIBE NI UN LECTOR NUEVO. Todos los que usa se
IMPORTAN de los registradores que ya existen, y se dice cual hace cada cosa:

  . `serie_de_registros.siguiente_libre()`     . el numero, que no se teclea
  . `R84.claves_entrecomilladas()`             . las `4.n`, las `5.n` y las `C.An`
  . `R94.caidas_propias_entrecomilladas()`     . las `C.n` del ejecutor
  . `R92.caidas_por_lead_heredado()`           . el contraste heredado, al lado
  . `R92.titulo_de_la_entrada()`               . el titulo con sus cinco numerales
  . `R95.cifras_de_la_fila_de_puestos()`       . la metrica, si su forma calza

LO QUE CAMBIA RESPECTO DEL CLONADO, Y SE DICE ENTERO:

1. LOS DOS SUJETOS SON OTROS: el acta 173 y el acta 174, que son las dos mas
   viejas de la deuda. Se corren en ese orden y cada una computa SU numero con
   `siguiente_libre()` DESPUES de la anterior, que es la unica forma de que el
   segundo numero no se teclee.
2. EL REPORTE DE LA 173 NO EXISTE, y eso NO SE FABRICA. Medido aqui con
   `os.path.isfile` y `os.path.getsize`, y tambien por el bloque `H.2` del sello
   de apertura de esta vuelta. Su numeral de PREGUNTAS CONTESTADAS usa entonces
   LA VARA QUE EL ACTA 201 DEJO ESCRITA EN SU `4.7`: las claves `P.n` NOMBRADAS
   EN LOS TITULOS `4.n` DEL ACTA, y la entrada DECLARA que usa esa vara. El
   reporte de la 174 SI existe, asi que la suya va por el filtro de siempre.
3. LOS CASOS DE LA PRUEBA DE IDEMPOTENCIA cambian de sujeto y de numero, porque
   una prueba que se corre sobre el sujeto de otra vuelta no prueba esta.

USO:
  python scripts/loop/_v202_t4_registrar_actas.py
  python scripts/loop/_v202_t4_registrar_actas.py --escribir
"""'''

CASOS = '''        titulo173 = "## R.63. Registro de algo del acta de la vuelta 173"
        titulo174 = "## R.63. Registro de algo del acta de la vuelta 174"
        casos = [
            ("sede SIN la entrada, numero 63", "## R.62. algo" + NL, 63, 173, False),
            ("sede CON la entrada, numero 63", "## R.63. algo" + NL, 63, 173, True),
            ("sede con R.630, que NO es R.63", "## R.630. algo" + NL, 63, 173, False),
            ("sede con la entrada en mitad", "x" + NL + "## R.63. algo" + NL,
             63, 173, True),
            ("el acta 173 ya registrada con OTRO numero", titulo173 + NL, 64,
             173, True),
            ("el acta 174 NO registrada, numero libre", titulo173 + NL, 64,
             174, False),
            ("el acta 174 ya registrada con OTRO numero", titulo174 + NL, 64,
             174, True),
            ("el acta citada en prosa, NO en titular",
             "hablo del acta de la vuelta 173 por ahi" + NL, 64, 173, False),
        ]'''

GLOSAS = '''GLOSA_173 = [
    "**ESTA ES LA PRIMERA DE LAS OCHO DE LA DEUDA, Y SE PAGA DE LA MAS VIEJA A LA",
    "MAS NUEVA** (adjudicacion `4.9` del acta 201, DOS POR VUELTA). La deuda son las",
    "actas **173 a 180**, y esta vuelta paga la **173** y la **174**. **El trabajo de",
    "plan va delante y esta tarea detras**, que es lo que la moratoria `6.3` manda al",
    "decir que **el trabajo es el plan hasta agotarlo**.",
    "",
    "**EL REPORTE DE LA VUELTA 173 NO SE ARCHIVO NUNCA, Y ESTA ENTRADA DECLARA LA",
    "AUSENCIA EN VEZ DE RELLENARLA:** `docs/loop/reportes/REPORTE_V173.md` **no",
    "existe**, medido en esta vuelta con `os.path.isfile` y `os.path.getsize` desde",
    "`scripts/loop/_v202_t4_registrar_actas.py`, y tambien por el bloque `H.2` del",
    "sello de apertura `docs/loop/SALIDA_V202_APERTURA.txt`, que ademas conto el rango",
    "entero: de la **168** a la **199** faltan **DOS** reportes archivados, la **173** y",
    "la **198**. **NO SE RECONSTRUYE Y NO SE FABRICA.**",
    "",
    "**LA CONSECUENCIA MEDIDA, Y ES LA QUE EXPLICA EL NUMERAL DE PREGUNTAS:** la via",
    "de siempre filtra las claves `P.n` de los titulos `4.n` del acta contra la seccion",
    "de PREGUNTAS del reporte archivado de esa vuelta. **Sin reporte no hay filtro.**",
    "Por eso el numeral de esta entrada usa **la vara que el acta 201 dejo escrita en",
    "su `4.7`**, las claves `P.n` nombradas en los titulos `4.n` del acta, **y lo dice",
    "en vez de publicar un cero** que se leeria como que el acta 173 no contesto",
    "ninguna pregunta. **Declarada asi, no es caida.**",
]

GLOSA_174 = [
    "**ESTA ES LA SEGUNDA DE LAS OCHO DE LA DEUDA** (adjudicacion `4.9` del acta 201).",
    "Con esta entrada quedan **SEIS** actas de la deuda sin entrada propia, las **175 a",
    "180**, y la cifra de la deuda se **REMIDE AL CIERRE** de esta misma corrida en vez",
    "de heredarse.",
    "",
    "**Y AQUI SI HAY REPORTE ARCHIVADO, QUE ES LA DIFERENCIA CON LA ENTRADA DE",
    "ARRIBA:** `docs/loop/reportes/REPORTE_V174.md` **existe**, medido con",
    "`os.path.isfile` y `os.path.getsize` en esta vuelta, asi que el numeral de",
    "preguntas de esta entrada **si va por el filtro de siempre** y no por la vara del",
    "`4.7`. **Las dos vias quedan escritas, una en cada entrada, para que se puedan",
    "comparar.**",
]'''
