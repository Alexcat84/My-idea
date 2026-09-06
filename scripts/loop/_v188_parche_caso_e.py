# -*- coding: utf-8 -*-
"""_v188_parche_caso_e.py . REESCRIBE EL CASO E DE
scripts/loop/vuelta186_tarea2c_mutacion_cierre_tardio.py DENTRO DE SU PROPIO
FICHERO, SIN CLONARLO Y SIN ESCRIBIR UN ARNES NUEVO PARA ESQUIVARLO.

Auxiliar de una sola vuelta: no es guarda, no entra en la nomina y no publica
ninguna cifra. Quien autoriza el cambio: acta 188, punto 7.1.
"""
import io
import os

NL = chr(10)
RUTA = os.path.join("scripts", "loop",
                    "vuelta186_tarea2c_mutacion_cierre_tardio.py")

CABEZA_NUEVA = '''# ---------------------------------------------------------------------------
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
PAT_COLUMNA = re.compile(r"^\\s*(?:[^,()]*,\\s*)?not\\s+tardio\\s*\\)")
PAT_IF = re.compile(r"^\\s*if\\s+not\\s+tardio\\s*:")
PAT_ETIQUETA = re.compile(r'^\\s*\\(\\s*"([^"]+)"\\s*,')
PAT_ASIGNA = re.compile(r"^\\s*(\\w+)\\s*=\\s*(\\w+)\\s*\\(")
VENTANA_ATRAS = 12


def exenciones_del_carril_tardio(fuente):
    """EL INVENTARIO DE GUARDAS EXIMIDAS EN EL CARRIL TARDIO, CON SUS NOMBRES.

    Devuelve [(linea, nombre, forma)]. **PURA**: recibe el texto del fuente y no
    lee ni escribe nada, para que sus tres casos rojos se puedan tumbar sobre
    fuentes fabricados en memoria sin tocar el fichero vivo.

    COMO SE NOMBRA CADA UNA, Y NO SE TECLEA NINGUNA:

      - FORMA `columna`: la exencion vive como la tercera celda de una fila de la
        lista de comprobaciones (`("etiqueta", condicion, not tardio)`). Su nombre
        es LA ETIQUETA de esa fila, buscada hacia atras hasta %d lineas.
      - FORMA `if`: la exencion es un `if not tardio:` que envuelve el `extra +=`.
        Su nombre es EL DE LA FUNCION que produjo lo que ese bloque contaba,
        buscada hacia atras en la asignacion mas cercana.

    UNA EXENCION QUE NO SE PUEDA NOMBRAR SALE COMO `(sin nombre)`, y quien llama
    la trata como ROJO: **una exencion anonima es peor que una que no esta en la
    lista**, porque nadie puede saber que afloja.""" %% VENTANA_ATRAS
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


'''

BLOQUE_NUEVO = '''    w("   Y LA CUARTA PATA, QUE ES LA QUE ESTA VUELTA REESCRIBE (acta 188, 7.1):")
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
         fuente.replace("    print(\\"\\")\\n    if faltan or extra:",
                        "    if not tardio:\\n        extra += 0\\n"
                        "    print(\\"\\")\\n    if faltan or extra:", 1),
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
'''


def main():
    t = io.open(RUTA, encoding="utf-8").read().replace(chr(13) + NL, NL)
    if "LISTA_AUTORIZADA" in t:
        print("YA PARCHEADO: no se toca.")
        return 0

    # 1. imports que el bloque nuevo necesita
    t = t.replace("import io\nimport os\nimport sys\n",
                  "import hashlib\nimport io\nimport os\nimport re\nimport sys\n", 1)

    # 2. la cabeza nueva, justo antes de fabricar()
    ancla = "def fabricar(extra=(), sin_veredicto=False, sin_seccion=None,"
    t = t.replace(ancla, CABEZA_NUEVA + ancla, 1)

    # 3. el bloque viejo del caso E, sustituido entero
    ini = t.index('    w("   Y LAS OTRAS TRES COMPROBACIONES DEL BLOQUE D TAMPOCO SE AFLOJAN: el")')
    fin = t.index('    w("")\n    return fallos, casos, caen\n\n\ndef main():')
    t = t[:ini] + BLOQUE_NUEVO + t[fin:]

    # 4. el docstring del fichero: se anade el caso E nuevo sin borrar el viejo
    t = t.replace(
        "  (E) EL CARRIL TARDIO NO AFLOJA NINGUNA DE LAS CUATRO PIEZAS: sobre un texto al\n"
        "      que le falta cada una de las cuatro, `piezas_que_faltan()` sigue\n"
        "      acusandolas, y ese instrumento NI SIQUIERA TIENE un parametro de carril,\n"
        "      que es la prueba mas fuerte que se puede dar de que el carril no lo toca.",
        "  (E) EL CARRIL TARDIO NO AFLOJA NINGUNA DE LAS CUATRO PIEZAS: sobre un texto al\n"
        "      que le falta cada una de las cuatro, `piezas_que_faltan()` sigue\n"
        "      acusandolas, y ese instrumento NI SIQUIERA TIENE un parametro de carril,\n"
        "      que es la prueba mas fuerte que se puede dar de que el carril no lo toca.\n"
        "      Y DESDE LA VUELTA 188 (acta 188, punto `7.1`) SU CUARTA PATA DEJA DE\n"
        "      CONTAR UN TEXTO: computa el INVENTARIO de guardas eximidas en el carril\n"
        "      tardio, CON SUS NOMBRES, leido del fuente, y lo coteja contra una LISTA\n"
        "      AUTORIZADA Y ESCRITA que vive en este arnes con la vuelta y la decision\n"
        "      que autorizo cada entrada. Cae en rojo en TRES casos y los tres se\n"
        "      prueban: una exencion que no esta en la lista, una de la lista que\n"
        "      desaparece del fuente, y una eximida que NO exige su declaracion.\n"
        "      NO AFLOJA NADA: queda MAS APRETADO que la cuenta vieja, porque una\n"
        "      cuenta de dos no distingue si las dos son las de la lista o si una se\n"
        "      cambio por otra.", 1)

    io.open(RUTA, "w", encoding="utf-8", newline=NL).write(t)
    print("PARCHEADO: %s (%d bytes)" % (RUTA, len(t.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
