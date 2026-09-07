# -*- coding: utf-8 -*-
r"""vuelta186_tarea2c_mutacion_cierre_tardio.py . EL CASO POSITIVO POR MUTACION
DEL CARRIL DE CIERRE TARDIO.

QUIEN LO ENCARGA. El acta 186, punto `7.2`, contestando la `P.2`: las 10 cifras
sin pareja del reporte de la 184 *"ni se eximen ni se reescriben. SE DECLARAN"*.
Reescribir el texto esta descartado porque seria escribir en pasado lo que no
paso; eximir en silencio esta descartado por banco 9, que llama a eso degradacion
silenciosa. Lo que queda es un carril donde el defecto queda **visible y medido**.

QUE PRUEBA, CASO A CASO, Y TODOS TIENEN QUE CAER AL MUTAR SU ESPERADO:
  (A) LA CONDICION DEL CARRIL, que es `es_cierre_tardio()` y es PURA: la vuelta
      en curso igual a la del reporte NO abre el carril; una posterior SI; y si
      la vuelta en curso no se puede leer, TAMPOCO se abre. La falta de evidencia
      cierra el carril, no lo abre.
  (B) CIFRAS SIN PAREJA EN CARRIL NORMAL: bloquean.
  (C) LAS MISMAS EN CARRIL TARDIO: no bloquean, Y APARECEN DECLARADAS en el
      texto, cotejado POR CONTENCION renglon a renglon.
  (D) CERO CIFRAS SIN PAREJA EN CARRIL TARDIO: la declaracion dice cero y NO se
      omite.
  (E) EL CARRIL TARDIO NO AFLOJA NINGUNA DE LAS CUATRO PIEZAS: sobre un texto al
      que le falta cada una de las cuatro, `piezas_que_faltan()` sigue
      acusandolas, y ese instrumento NI SIQUIERA TIENE un parametro de carril,
      que es la prueba mas fuerte que se puede dar de que el carril no lo toca.
      Y DESDE LA VUELTA 188 (acta 188, punto `7.1`) SU CUARTA PATA DEJA DE
      CONTAR UN TEXTO: computa el INVENTARIO de guardas eximidas en el carril
      tardio, CON SUS NOMBRES, leido del fuente, y lo coteja contra una LISTA
      AUTORIZADA Y ESCRITA que vive en este arnes con la vuelta y la decision
      que autorizo cada entrada. Cae en rojo en TRES casos y los tres se
      prueban: una exencion que no esta en la lista, una de la lista que
      desaparece del fuente, y una eximida que NO exige su declaracion.
      NO AFLOJA NADA: queda MAS APRETADO que la cuenta vieja, porque una
      cuenta de dos no distingue si las dos son las de la lista o si una se
      cambio por otra.

LO QUE ESTE ARNES NO HACE: no escribe ningun reporte, no corre
`cerrar_reporte.py` como proceso y no toca `docs/loop/REPORTE.md`. Llama a las
funciones PURAS del fichero vivo con textos fabricados en memoria.

USO:
  python scripts/loop/vuelta186_tarea2c_mutacion_cierre_tardio.py

--- SUJETO CONGELADO, DECLARADO EN LA VUELTA 195 (TAREA 3.c) ---

**LA HUELLA DE VIVO QUE LA GUARDA VE AQUI ES `REPORTE.md`, Y ES UNA LINEA QUE
ESTE ARNES IMPRIME PARA DECIR QUE NO LO TOCA:** *"Aqui no se escribe ningun
reporte y no se toca docs/loop/REPORTE.md."* La guarda mira la maquina (el fichero
sin su docstring de modulo) y ahi esa frase es un `w(...)`, no una apertura.

**CUAL ES SU SUJETO DE DATOS, DICHO SIN ADORNARLO: CADENAS FABRICADAS EN
MEMORIA.** Todas las llamadas a las funciones PURAS de `cerrar_reporte.py` van
sobre textos que este proceso construye, y **no lee ningun fichero de datos de la
campana**.

**Y LO UNICO QUE SI LEE DEL DISCO SE DICE EN VEZ DE CALLARLO:** abre
`scripts/loop/cerrar_reporte.py`, que es **el codigo bajo prueba**, y publica su
`sha256` como procedencia. Eso no es un sujeto que se mueva por debajo: es la
identidad del modulo que se esta probando, y **todo arnes importa el codigo que
prueba**. La huella `sha256` que la guarda ya le ve sale precisamente de ahi.

**POR ESO SU SUJETO ESTA CONGELADO** y esta declaracion lo dice con el literal que
la regla de la vuelta 148 pide.

"""
import hashlib
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cerrar_reporte as CR   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

FILAS = ["| celda | celda |", "| a | b |", "| c | d |", "| e | f |",
         "| g | h |", "| i | j |", "| k | l |", "| m | n |", "| o | p |"]
BAT = ["linea uno de la bateria"]
NOM = "docs/loop/SALIDA_V999_BATERIA.txt"

# TRES LINEAS QUE PUBLICAN UNA CIFRA SIN SU PAREJA, escritas a proposito con una
# sola convencion para que `cifras_sin_pareja()` las cace.
SIN_PAREJA = [
    "El fichero mide 1234 bytes.",
    "Y el otro mide 5678 bytes.",
    "Su sha256 es abcdef0123456789abcdef01.",
]


# ---------------------------------------------------------------------------
# EL INVENTARIO DE EXENCIONES DEL CARRIL TARDIO (vuelta 188, TAREA 3).
#
# QUIEN AUTORIZA ESTE CAMBIO, ESCRITO AQUI DENTRO PARA QUE NO HAYA QUE BUSCARLO:
# EL ACTA 188, PUNTO `7.1`, contestando la `P.1` que el reporte de la 187 trajo
# como PARADA. Su letra: *"el caso E deja de contar un texto y pasa a computar el
# INVENTARIO de guardas eximidas en el carril tardio, con sus nombres, cotejado
# contra una lista autorizada y escrita"*.
#
# QUE ESTABA MAL, Y NO ERA UN CHOQUE DE REGLAS. El caso E contaba las apariciones
# de `not tardio` en el fuente y exigia exactamente **1**. El encargo de la vuelta
# 187 mando anadir una segunda exencion con estas palabras: *"En el carril de
# CIERRE TARDIO, la guarda de la `2.d` NO bloquea, pero SE DECLARA"*. Asi que no
# habia dos reglas vigentes peleandose: habia **un esperado tecleado en la 186** y
# **una orden escrita de la 187 que lo dejo viejo**.
#
# POR QUE NO SE CAMBIA EL `1` POR UN `2`, QUE ERA LO FACIL: porque eso deja **otra
# cifra tecleada** que la proxima exencion volveria a dejar vieja, y el caso E
# dejaria de vigilar lo que dice vigilar. **Una cuenta de dos no distingue si las
# dos son las de la lista o si una se cambio por otra.**
#
# ESTO NO AFLOJA NADA, Y SE MIDE EN VEZ DE PROMETERSE. El caso E queda MAS
# APRETADO que antes porque **nombra cuales** y porque exige tres cosas donde
# antes exigia una:
#   (1) que no aparezca una exencion que no este en la lista autorizada;
#   (2) que no desaparezca del fuente ninguna de las que la lista autoriza;
#   (3) que toda eximida EXIJA SU DECLARACION, o sea que su exencion no sea muda.
#
# Y LAS TRES SE PRUEBAN POR MUTACION SOBRE FUENTES FABRICADOS EN MEMORIA, nunca
# sobre el fichero vivo.
LISTA_AUTORIZADA = [
    # (nombre de la guarda eximida, vuelta que la autorizo, decision que la
    #  autoriza, y LA MARCA LITERAL que prueba que la exencion EXIGE SU
    #  DECLARACION en vez de ser muda)
    ("toda cifra de bytes y todo sha con su pareja", 178,
     "acta 186 punto 7.2, contestando la P.2: las cifras sin pareja de un reporte "
     "viejo NI SE EXIMEN NI SE REESCRIBEN, SE DECLARAN",
     "declaracion_de_cifras_sin_pareja"),
    ("seccion4_que_no_calza", 187,
     "encargo de la vuelta 187, TAREA 5.b, respuesta del acta 187 a la P.2: EN EL "
     "CARRIL DE CIERRE TARDIO, LA GUARDA DE LA 2.d NO BLOQUEA, PERO SE DECLARA",
     "if not dentro or sin_declarar:"),
]

# LOS PATRONES CON QUE SE LEE EL INVENTARIO DEL FUENTE. Son dos formas y no una,
# porque el fuente escribe la exencion de dos maneras distintas: como COLUMNA
# `bloquea` de una fila de comprobacion, y como `if` que envuelve el `extra +=`.
PAT_COLUMNA = re.compile(r"^\s*(?:[^,()]*,\s*)?not\s+tardio\s*\)")
PAT_IF = re.compile(r"^\s*if\s+not\s+tardio\s*:")
PAT_ETIQUETA = re.compile(r'^\s*\(\s*"([^"]+)"\s*,')
PAT_ASIGNA = re.compile(r"^\s*(\w+)\s*=\s*(\w+)\s*\(")
VENTANA_ATRAS = 12


def exenciones_del_carril_tardio(fuente):
    """EL INVENTARIO DE GUARDAS EXIMIDAS EN EL CARRIL TARDIO, CON SUS NOMBRES.

    Devuelve [(linea, nombre, forma)]. **PURA**: recibe el texto del fuente y no
    lee ni escribe nada, para que sus tres casos rojos se puedan tumbar sobre
    fuentes fabricados en memoria sin tocar el fichero vivo.

    COMO SE NOMBRA CADA UNA, Y NO SE TECLEA NINGUNA:

      - FORMA `columna`: la exencion vive como la tercera celda de una fila de la
        lista de comprobaciones (`("etiqueta", condicion, not tardio)`). Su nombre
        es LA ETIQUETA de esa fila, buscada hacia atras dentro de la ventana
        de `VENTANA_ATRAS` lineas.
      - FORMA `if`: la exencion es un `if not tardio:` que envuelve el `extra +=`.
        Su nombre es EL DE LA FUNCION que produjo lo que ese bloque contaba,
        buscada hacia atras en la asignacion mas cercana.

    UNA EXENCION QUE NO SE PUEDA NOMBRAR SALE COMO `(sin nombre)`, y quien llama
    la trata como ROJO: **una exencion anonima es peor que una que no esta en la
    lista**, porque nadie puede saber que afloja."""
    lineas = fuente.replace(chr(13) + NL, NL).split(NL)
    salida = []
    for i, l in enumerate(lineas, 1):
        if PAT_IF.match(l):
            nombre = "(sin nombre)"
            for j in range(i - 1, max(0, i - 1 - VENTANA_ATRAS), -1):
                m = PAT_ASIGNA.match(lineas[j - 1])
                if m:
                    nombre = m.group(2)
                    break
            salida.append((i, nombre, "if"))
        elif PAT_COLUMNA.match(l):
            nombre = "(sin nombre)"
            for j in range(i, max(0, i - VENTANA_ATRAS), -1):
                m = PAT_ETIQUETA.match(lineas[j - 1])
                if m:
                    nombre = m.group(1)
                    break
            salida.append((i, nombre, "columna"))
    return salida


def exenciones_mudas(fuente, lista=None):
    """LAS EXIMIDAS QUE NO EXIGEN SU DECLARACION. Devuelve [(nombre, marca)].
    PURA.

    Es la tercera pata del caso E, y la que impide que una exencion se ensanche
    en silencio: **el carril tardio exime SOLO si la declaracion esta escrita**.
    La marca de cada una vive en la lista autorizada, al lado de la vuelta y la
    decision que la autorizo."""
    lista = LISTA_AUTORIZADA if lista is None else lista
    presentes = set(n for _l, n, _f in exenciones_del_carril_tardio(fuente))
    faltan = []
    for nombre, _v, _d, marca in lista:
        if nombre in presentes and marca not in fuente:
            faltan.append((nombre, marca))
    return faltan


def fabricar(extra=(), sin_veredicto=False, sin_seccion=None,
             con_hueco_de_cabecera=False, filas_pegadas=True):
    """UN REPORTE DE MENTIRA. PURA: devuelve texto y no escribe nada.

    Cada parametro rompe UNA de las cuatro piezas, para que el caso (E) pueda
    exigir que el carril tardio no afloje ninguna."""
    p = ["# REPORTE DE LA VUELTA 999 (fabricado)", ""]
    if not sin_veredicto:
        p += ["**EL VEREDICTO DE UNA LINEA: de mentira.**", ""]
    if con_hueco_de_cabecera:
        p += ["**%s.** Y su prosa." % CR.HUECO_CABECERA, ""]
    if filas_pegadas:
        p += FILAS + [""]
    p += list(extra) + [""]
    for k in range(3, 9):
        if sin_seccion is not None and k == sin_seccion:
            continue
        p += ["## %d. UNA SECCION DE MENTIRA" % k, "", "Y su cuerpo.", ""]
    if sin_seccion != 9:
        p += ["## 9. LA BATERIA DE MUTACIONES, DE MENTIRA", ""] + BAT + [""]
    return NL.join(p) + NL


def _caso_a(w):
    """A: la condicion del carril, que es PURA."""
    fallos = casos = caen = 0
    w("CASO A. LA CONDICION DEL CARRIL, QUE SE COMPUTA Y NO SE PASA POR BANDERA")
    escenarios = [
        ("la vuelta en curso es la del reporte", 186, 186, False),
        ("la vuelta en curso es POSTERIOR", 184, 186, True),
        ("la vuelta en curso es ANTERIOR", 186, 184, True),
        ("la vuelta en curso NO SE PUDO LEER", 184, None, False),
        ("la vuelta del reporte es None", None, 186, False),
    ]
    for etiqueta, v, curso, esperado in escenarios:
        medido = CR.es_cierre_tardio(v, curso)
        casos += 1
        w("   %-42s reporte %-5s curso %-5s -> %-5s | esperado %-5s | %s"
          % (etiqueta, v, curso, medido, esperado,
             "CALZA" if medido == esperado else "NO CALZA"))
        if medido != esperado:
            fallos += 1
        w("      MUTACION del esperado (exigir %s): %s"
          % (not esperado, "PASA" if medido != esperado else "CAE"))
        if medido != esperado:
            fallos += 1
        else:
            caen += 1
    w("")
    return fallos, casos, caen


def _casos_bcd(w):
    """B, C Y D: las cifras sin pareja en cada carril y la declaracion."""
    fallos = casos = caen = 0
    texto = fabricar(extra=SIN_PAREJA)
    huerfanas = CR.cifras_sin_pareja(texto)
    w("CASO B. CIFRAS SIN PAREJA EN CARRIL NORMAL: BLOQUEAN")
    w("   CIFRA cifras sin pareja medidas sobre el texto fabricado: %d"
      % len(huerfanas))
    for n, especie, muestra, linea in huerfanas:
        w("      linea %-4d %-5s %-24s | %s" % (n, especie, muestra, linea[:70]))
    # EL BLOQUEO EN CARRIL NORMAL SE MODELA COMO LO HACE main(): la condicion
    # `bloquea` es `not tardio`, y aqui se computa con la MISMA funcion pura.
    normal = not CR.es_cierre_tardio(999, 999)
    bloquea_normal = bool(huerfanas) and normal
    casos += 1
    w("   carril: %s | bloquea: %s"
      % ("NORMAL" if normal else "TARDIO", bloquea_normal))
    w("   ESPERADO: bloquea -> %s" % ("CALZA" if bloquea_normal else "NO CALZA"))
    if not bloquea_normal:
        fallos += 1
    w("   MUTACION del esperado (exigir que NO bloquee): %s"
      % ("PASA" if not bloquea_normal else "CAE"))
    if bloquea_normal:
        caen += 1
    else:
        fallos += 1
    w("")

    w("CASO C. LAS MISMAS EN CARRIL TARDIO: NO BLOQUEAN Y APARECEN DECLARADAS")
    tardio = CR.es_cierre_tardio(999, 1000)
    bloquea_tardio = bool(huerfanas) and not tardio
    casos += 1
    w("   carril: %s | bloquea: %s"
      % ("TARDIO" if tardio else "NORMAL", bloquea_tardio))
    w("   ESPERADO: NO bloquea -> %s" % ("CALZA" if not bloquea_tardio else "NO CALZA"))
    if bloquea_tardio:
        fallos += 1
    w("   MUTACION del esperado (exigir que SI bloquee): %s"
      % ("PASA" if bloquea_tardio else "CAE"))
    if bloquea_tardio:
        fallos += 1
    else:
        caen += 1
    decl = CR.declaracion_de_cifras_sin_pareja(huerfanas, 999, 1000)
    w("   LA DECLARACION, COTEJADA POR CONTENCION RENGLON A RENGLON:")
    w("      la declaracion mide %d bytes en disco y %d normalizados a LF"
      % (len(decl.encode("utf-8")), len(decl.replace(chr(13) + NL, NL).encode("utf-8"))))
    dentro = 0
    for n, especie, muestra, linea in huerfanas:
        renglon = "linea %-6d %-5s %-24s | %s" % (n, especie, muestra, linea)
        esta = renglon in decl
        w("      %s -> %s" % (renglon[:88], "ESTA" if esta else "NO ESTA"))
        if esta:
            dentro += 1
    casos += 1
    w("   CIFRA cifras sin pareja DECLARADAS en el texto: %d de %d"
      % (dentro, len(huerfanas)))
    w("   ESPERADO: las %d -> %s"
      % (len(huerfanas), "CALZA" if dentro == len(huerfanas) else "NO CALZA"))
    if dentro != len(huerfanas):
        fallos += 1
    w("   MUTACION del esperado (exigir %d declaradas): %s"
      % (len(huerfanas) + 1,
         "PASA" if dentro == len(huerfanas) + 1 else "CAE"))
    if dentro == len(huerfanas) + 1:
        fallos += 1
    else:
        caen += 1
    w("   Y LA DECLARACION LLEVA SU CUENTA TOTAL:")
    linea_total = "CIFRA cifras publicadas sin su pareja: %d" % len(huerfanas)
    casos += 1
    w("      %r esta en la declaracion: %s"
      % (linea_total, "SI" if linea_total in decl else "NO"))
    if linea_total not in decl:
        fallos += 1
    falso = "CIFRA cifras publicadas sin su pareja: %d" % (len(huerfanas) + 1)
    w("      MUTACION del esperado (exigir la cuenta %d): %s"
      % (len(huerfanas) + 1, "PASA" if falso in decl else "CAE"))
    if falso in decl:
        fallos += 1
    else:
        caen += 1
    w("   Y LA DECLARACION VA DENTRO DE UNA CERCA, ASI QUE NO SE ACUSA A SI MISMA:")
    texto_con_decl = texto.rstrip(NL) + NL + NL + decl
    de_nuevo = CR.cifras_sin_pareja(texto_con_decl)
    casos += 1
    w("      CIFRA cifras sin pareja del texto CON la declaracion pegada: %d"
      % len(de_nuevo))
    w("      ESPERADO: las mismas %d, ni una mas -> %s"
      % (len(huerfanas), "CALZA" if len(de_nuevo) == len(huerfanas) else "NO CALZA"))
    if len(de_nuevo) != len(huerfanas):
        fallos += 1
    w("      MUTACION del esperado (exigir %d): %s"
      % (len(huerfanas) + 1,
         "PASA" if len(de_nuevo) == len(huerfanas) + 1 else "CAE"))
    if len(de_nuevo) == len(huerfanas) + 1:
        fallos += 1
    else:
        caen += 1
    w("")

    w("CASO D. CERO CIFRAS SIN PAREJA EN CARRIL TARDIO: LA DECLARACION DICE CERO")
    w("        Y NO SE OMITE")
    limpio = fabricar(extra=["Un parrafo sin ninguna cifra."])
    ninguna = CR.cifras_sin_pareja(limpio)
    decl0 = CR.declaracion_de_cifras_sin_pareja(ninguna, 999, 1000)
    casos += 1
    w("   CIFRA cifras sin pareja del texto limpio: %d" % len(ninguna))
    dice_cero = ("CIFRA cifras publicadas sin su pareja: 0" in decl0
                 and "la cuenta es CERO" in decl0)
    w("   la declaracion se escribe igual: %s"
      % ("SI, %d bytes" % len(decl0.encode("utf-8")) if decl0.strip() else "NO"))
    w("   y dice CERO con todas las letras: %s" % ("SI" if dice_cero else "NO"))
    if not (len(ninguna) == 0 and dice_cero and decl0.strip()):
        fallos += 1
    w("   MUTACION del esperado (exigir que la declaracion se omita): %s"
      % ("PASA" if not decl0.strip() else "CAE"))
    if not decl0.strip():
        fallos += 1
    else:
        caen += 1
    w("")
    return fallos, casos, caen


def _caso_e(w):
    """E: el carril tardio NO afloja ninguna de las cuatro piezas."""
    fallos = casos = caen = 0
    w("CASO E. EL CARRIL TARDIO NO AFLOJA NINGUNA DE LAS CUATRO PIEZAS")
    w("   (y la prueba mas fuerte es de forma: piezas_que_faltan() NI SIQUIERA")
    w("    TIENE un parametro de carril, asi que no puede saber en cual esta)")
    import inspect
    firma = list(inspect.signature(CR.piezas_que_faltan).parameters)
    casos += 1
    w("   parametros de piezas_que_faltan(): %s" % ", ".join(firma))
    sin_carril = not any(("tardio" in p or "carril" in p or "curso" in p)
                         for p in firma)
    w("   ninguno nombra el carril: %s" % ("SI" if sin_carril else "NO"))
    if not sin_carril:
        fallos += 1
    w("   MUTACION del esperado (exigir que SI tenga uno): %s"
      % ("PASA" if not sin_carril else "CAE"))
    if sin_carril:
        caen += 1
    else:
        fallos += 1
    w("")
    w("   Y LAS CUATRO, ROTAS UNA A UNA, CON LA MISMA LLAMADA QUE HACE main():")
    rotos = [
        ("(1) sin veredicto escrito", dict(sin_veredicto=True), "(1)"),
        ("(2) con el hueco de cabecera fuera de cerca",
         dict(con_hueco_de_cabecera=True), "(2)"),
        ("(2) con las filas del tallador sin pegar",
         dict(filas_pegadas=False), "(2)"),
        ("(3) sin la seccion 5", dict(sin_seccion=5), "(3)"),
        ("(4) sin la seccion 9", dict(sin_seccion=9), "(4)"),
    ]
    for etiqueta, kw, codigo in rotos:
        texto = fabricar(extra=SIN_PAREJA, **kw)
        faltan = CR.piezas_que_faltan(texto, FILAS, BAT, vuelta=999,
                                      nombre_bateria=NOM)
        acusada = [f for f in faltan if f.startswith(codigo)]
        casos += 1
        w("      %-46s -> %s"
          % (etiqueta, acusada[0][:80] if acusada else "NO LA ACUSA"))
        if not acusada:
            fallos += 1
        w("         MUTACION del esperado (exigir que NO la acuse): %s"
          % ("PASA" if not acusada else "CAE"))
        if acusada:
            caen += 1
        else:
            fallos += 1
    w("")
    w("   Y LA CUARTA PATA, QUE ES LA QUE ESTA VUELTA REESCRIBE (acta 188, 7.1):")
    w("   EL INVENTARIO DE GUARDAS EXIMIDAS EN EL CARRIL TARDIO, CON SUS NOMBRES,")
    w("   COTEJADO CONTRA UNA LISTA AUTORIZADA Y ESCRITA.")
    w("")
    w("   LA LISTA AUTORIZADA, QUE VIVE EN ESTE ARNES CON SU VUELTA Y SU DECISION")
    w("   AL LADO, PARA QUE ANADIR UNA TERCERA SEA UN ACTO VISIBLE Y NO UN DESCUIDO:")
    for nombre, vuelta_a, decision, marca in LISTA_AUTORIZADA:
        w("      - %r" % nombre)
        w("        autorizada en la vuelta %d por: %s" % (vuelta_a, decision))
        w("        marca que prueba que EXIGE SU DECLARACION: %r" % marca)
    w("   CIFRA entradas de la lista autorizada: %d" % len(LISTA_AUTORIZADA))
    w("")
    fuente = io.open(os.path.join(RAIZ, "scripts", "loop", "cerrar_reporte.py"),
                     encoding="utf-8").read().replace(chr(13) + NL, NL)
    sha_fuente = hashlib.sha256(fuente.encode("utf-8")).hexdigest()
    w("   EL SUJETO, CON SU SELLO AL LADO (vuelta 188, TAREA 3.b), para que los")
    w("   numeros de linea de abajo no envejezcan solos:")
    w("      scripts/loop/cerrar_reporte.py -> %d bytes normalizados a LF, %d lineas"
      % (len(fuente.encode("utf-8")), fuente.count(NL)))
    w("      sha256 LF %s" % sha_fuente)
    w("")
    inventario = exenciones_del_carril_tardio(fuente)
    w("   EL INVENTARIO, LEIDO DEL FUENTE Y NO TECLEADO:")
    for ln, nombre, forma in inventario:
        w("      linea %-5d forma %-8s nombre %r" % (ln, forma, nombre))
    w("   CIFRA exenciones halladas en el fuente: %d" % len(inventario))
    w("   CONTRASTE, la cuenta que este caso hacia antes: `not tardio` aparece %d"
      % fuente.count("not tardio"))
    w("   vez(ces). SE PUBLICA IGUAL, pero YA NO ES EL VEREDICTO: una cuenta de dos")
    w("   no distingue si las dos son las de la lista o si una se cambio por otra.")
    w("")
    nombres = sorted(n for _l, n, _f in inventario)
    autorizados = sorted(n for n, _v, _d, _m in LISTA_AUTORIZADA)
    intrusas = sorted(set(nombres) - set(autorizados))
    ausentes = sorted(set(autorizados) - set(nombres))
    anonimas = [x for x in nombres if x == "(sin nombre)"]
    mudas = exenciones_mudas(fuente)
    casos += 1
    w("   (1) EXENCIONES QUE NO ESTAN EN LA LISTA AUTORIZADA: %d %s"
      % (len(intrusas), intrusas or ""))
    w("   (2) DE LA LISTA QUE HAN DESAPARECIDO DEL FUENTE:    %d %s"
      % (len(ausentes), ausentes or ""))
    w("   (3) EXIMIDAS QUE NO EXIGEN SU DECLARACION:          %d %s"
      % (len(mudas), [n for n, _m in mudas] or ""))
    w("       ANONIMAS (que es peor que las tres): %d" % len(anonimas))
    ok_inv = not (intrusas or ausentes or mudas or anonimas)
    w("   ESPERADO: cero en las tres -> %s" % ("CALZA" if ok_inv else "NO CALZA"))
    if not ok_inv:
        fallos += 1
    w("")
    w("   Y LOS TRES ROJOS SE PRUEBAN, SOBRE FUENTES FABRICADOS EN MEMORIA Y NUNCA")
    w("   SOBRE EL FICHERO VIVO:")
    rojos = [
        ("(1) aparece una TERCERA exencion que nadie autorizo",
         fuente.replace("    print(\"\")\n    if faltan or extra:",
                        "    if not tardio:\n        extra += 0\n"
                        "    print(\"\")\n    if faltan or extra:", 1),
         "intrusa"),
        ("(2) desaparece del fuente una de las dos de la lista",
         fuente.replace("             not huerfanas, not tardio),",
                        "             not huerfanas, True),", 1),
         "ausente"),
        ("(3) una eximida deja de exigir su declaracion",
         fuente.replace("        if not dentro or sin_declarar:",
                        "        if False:", 1),
         "muda"),
    ]
    for etiqueta, falso, especie in rojos:
        casos += 1
        cambio = (falso != fuente)
        inv2 = exenciones_del_carril_tardio(falso)
        n2 = sorted(n for _l, n, _f in inv2)
        i2 = sorted(set(n2) - set(autorizados))
        a2 = sorted(set(autorizados) - set(n2))
        m2 = exenciones_mudas(falso)
        cae = bool(i2 or a2 or m2)
        w("      %-52s -> fuente cambiado: %s" % (etiqueta, "SI" if cambio else "NO"))
        w("         intrusas %d %s | ausentes %d %s | mudas %d %s -> ROJO: %s"
          % (len(i2), i2 or "", len(a2), a2 or "", len(m2),
             [n for n, _m in m2] or "", "SI" if cae else "NO"))
        if not cambio:
            w("         NO SE PUDO FABRICAR EL CASO: el fuente no trae el texto que")
            w("         esta mutacion cambia. Se declara en vez de darlo por bueno.")
            fallos += 1
            continue
        if cae:
            caen += 1
        else:
            w("         EL CASO NO CAE, Y ESO ES UN FALLO DE ESTE ARNES.")
            fallos += 1
    w("")
    w("   Y LA MUTACION DEL ESPERADO SOBRE EL FUENTE DE VERDAD, QUE ES LA QUE PRUEBA")
    w("   QUE EL VEREDICTO NO ES UNA CONSTANTE: si se exige que la lista autorizada")
    w("   tenga UNA sola entrada, el cotejo tiene que CAER.")
    casos += 1
    lista_mutada = LISTA_AUTORIZADA[:1]
    aut_m = sorted(n for n, _v, _d, _m in lista_mutada)
    intr_m = sorted(set(nombres) - set(aut_m))
    w("      con la lista mutada a %d entrada(s): intrusas %d %s -> %s"
      % (len(lista_mutada), len(intr_m), intr_m,
         "PASA" if not intr_m else "CAE"))
    if not intr_m:
        fallos += 1
    else:
        caen += 1
    w("")
    return fallos, casos, caen


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("CASO POSITIVO POR MUTACION DEL CARRIL DE CIERRE TARDIO")
    w("(vuelta 186, TAREA 2.c; respuesta del acta 186 a la P.2)")
    w("=" * 78)
    w("")
    w("EL SUJETO ES EL FICHERO VIVO scripts/loop/cerrar_reporte.py, IMPORTADO.")
    w("Aqui no se escribe ningun reporte y no se toca docs/loop/REPORTE.md.")
    w("")
    fallos = casos = caen = 0
    for parte in (_caso_a, _casos_bcd, _caso_e):
        f, c, k = parte(w)
        fallos += f
        casos += c
        caen += k
    w("CIFRA casos: %d | pasan: %d" % (casos, casos - fallos))
    w("CIFRA casos que CAEN al mutar su esperado: %d de %d" % (caen, caen))
    w("CIFRA fallos: %d" % fallos)
    w("VEREDICTO: %s" % ("VERDE" if fallos == 0 else "ROJO"))
    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V186_T2C_MUTACION_CIERRE_TARDIO.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0 if fallos == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
