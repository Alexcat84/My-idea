# -*- coding: utf-8 -*-
r"""_v178_parche_pareja.py . EL PARCHE QUE HACE CAER EN ROJO A
`scripts/loop/cerrar_reporte.py` CUANDO EL REPORTE PUBLICA UNA CIFRA DE BYTES O
UN SHA SIN SU PAREJA (vuelta 178, TAREA 1.e).

ES UN PARCHE, NO CODIGO VIVO: empieza por guion bajo, no lo ve el censo de
arneses y no entra en ninguna nomina. Cada sustitucion lleva su `assert`.
"""
import io
import os

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
R = os.path.join(RAIZ, "scripts", "loop", "cerrar_reporte.py")

t = io.open(R, encoding="utf-8").read().replace(chr(13) + NL, NL)
PARES = []

# ------------------------------------------------------------------ DOCSTRING
PARES.append(("""Y CAE EN ROJO SI AL TERMINAR FALTA CUALQUIERA DE LAS CUATRO PIEZAS:""",
"""LA QUINTA COMPROBACION, QUE NO ES UNA PIEZA SINO UNA CONVENCION (vuelta 178,
TAREA 1.e; adjudicacion del acta 177 punto 7.11). LA CONVENCION DE BYTES SIGUE
SIN FIJAR y es del fundador, no la fija nadie mas; lo que el auditor SI adjudica,
porque no elige entre las dos, es que MIENTRAS NO ESTE FIJADA TODA CIFRA DE
BYTES O SHA SE PUBLIQUE CON LAS DOS, disco y normalizado a LF. La causa esta
medida en la 177: su propio reporte declaraba hacerlo y luego no lo hizo en dos
celdas, un tallador publicado en "5.001 bytes" cuando el disco decia 5.021, y un
sha `7d683eea4700f18b` que era el de LF y no el de disco. LAS DOS CIFRAS ERAN
VERDADERAS Y LAS DOS HUBO QUE IR A BUSCARLAS. Aqui deja de depender de que
alguien se acuerde.

COMO SE MIDE, Y ES MECANICO. Una cifra esta EMPAREJADA si EN SU MISMA LINEA hay
DOS O MAS apariciones de su especie (dos "N bytes", o dos sha), O si la linea
NOMBRA AL MENOS DOS de las marcas de convencion (`disco`, `LF`, `normalizado`,
`cat-file`, `getsize`), que es la forma de decir "las dos convenciones dan esta
misma cifra" sin escribirla dos veces.

QUE QUEDA FUERA, Y SE DICE POR QUE: los bloques de codigo cercados con tres
comillas invertidas. Ahi va PEGADA la salida cruda de un instrumento, que es una
CITA y no una celda publicada: exigirle la pareja seria exigirsela al
instrumento citado, y una cita que se retoca deja de ser una cita. Los sha solo
se buscan en lineas que digan `sha`, para no confundir un hash de commit (que es
identidad y no contenido) con el sha de un fichero.

Y CAE EN ROJO SI AL TERMINAR FALTA CUALQUIERA DE LAS CUATRO PIEZAS:"""))

# ------------------------------------------------------------------ CONSTANTES
PARES.append(("""PATRON_BYTES = re.compile(r"(\\d[\\d.]*)\\s+bytes")""",
'''PATRON_BYTES = re.compile(r"(\\d[\\d.]*)\\s+bytes")

# LA PAREJA DE CIFRAS (vuelta 178, TAREA 1.e). Un sha se busca SOLO en lineas
# que digan `sha`, y con 12 caracteres hexadecimales como minimo, para no
# confundirlo con un hash corto de commit: un commit es identidad, no contenido,
# y la convencion que falta es la del contenido.
PATRON_SHA = re.compile(r"\\b[0-9a-f]{12,64}\\b")
MARCAS_CONVENCION = ("disco", "LF", "normalizado", "cat-file", "getsize")
CERCA = "```"'''))

# ------------------------------------------------------------------ FUNCION
PARES.append(("""def piezas_que_faltan(texto, filas_tallador, lineas_bateria,""",
'''def cifras_sin_pareja(texto):
    """LAS CIFRAS DE BYTES Y LOS SHA QUE EL REPORTE PUBLICA SIN SU PAREJA.

    Devuelve [(numero_de_linea, especie, muestra, linea)], VACIA si todas van
    emparejadas. PURA a proposito, como sus hermanas de este fichero: recibe el
    texto y no lee ni escribe nada, para que su caso positivo por mutacion la
    pueda tumbar caso a caso sin tocar el repo.

    LA REGLA, ESCRITA AQUI PARA QUE NO HAYA QUE DEDUCIRLA DE LA SALIDA: una
    cifra esta emparejada si en su MISMA LINEA hay dos o mas apariciones de su
    especie, o si la linea nombra al menos DOS marcas de convencion. Los bloques
    cercados quedan fuera porque son citas de la salida de un instrumento."""
    fallos = []
    dentro_de_cerca = False
    for n, linea in enumerate(texto.split(NL), 1):
        if linea.lstrip().startswith(CERCA):
            dentro_de_cerca = not dentro_de_cerca
            continue
        if dentro_de_cerca:
            continue
        marcas = sum(1 for m in MARCAS_CONVENCION if m in linea)
        for especie, hits in (("bytes", PATRON_BYTES.findall(linea)),
                              ("sha", PATRON_SHA.findall(linea)
                               if "sha" in linea.lower() else [])):
            if not hits:
                continue
            if len(hits) >= 2 or marcas >= 2:
                continue
            fallos.append((n, especie, hits[0], linea.strip()[:120]))
    return fallos


def piezas_que_faltan(texto, filas_tallador, lineas_bateria,'''))

# ------------------------------------------ LA CABECERA PUBLICA LAS DOS CIFRAS
PARES.append(('''        "cruda vive en `%s` (%d bytes, %d filas de tabla," % (a.tallador,
                                                             len(tallador.encode("utf-8")),
                                                             len(filas)) + NL +''',
'''        "cruda vive en `%s` (%d bytes en disco y %d normalizado a LF, %d filas de"
        % (a.tallador, os.path.getsize(os.path.join(RAIZ, a.tallador.replace("/", os.sep))),
           len(tallador.encode("utf-8")), len(filas)) + NL +
        "tabla," + NL +'''))

# --------------------------------------------- LA SECCION 9 PUBLICA LAS DOS
PARES.append(('''            "Fichero: `%s` (**%d bytes, %d lineas no vacias**, contadas" % (a.bateria, tam,
                                                                           len(lineas_bat)) + NL +''',
'''            "Fichero: `%s` (**%d bytes en disco y %d normalizado a LF**, **%d lineas"
            % (a.bateria, tam, len(bateria.encode("utf-8")), len(lineas_bat)) + NL +
            "no vacias**, contadas" + NL +'''))

PARES.append(('''            "**SUS BYTES, MEDIDOS EN ESTA CORRIDA** con `os.path.getsize` por" + NL +
            "`scripts/loop/cerrar_reporte.py`, no tecleados: **%d bytes**." % max(tam, 0) + NL + NL +''',
'''            "**SUS BYTES, MEDIDOS EN ESTA CORRIDA** con `os.path.getsize` por" + NL +
            "`scripts/loop/cerrar_reporte.py`, no tecleados, y POR LAS DOS" + NL +
            "CONVENCIONES mientras la del fundador no este fijada: **%d bytes en disco"
            % max(tam, 0) + NL +
            "y %d bytes normalizados a LF**." % max(tam_lf, 0) + NL + NL +'''))

# ------------------------------------------------- SE MIDE EL LF DE LA BATERIA
PARES.append(('''    bateria = leer(ruta_bat) if existe and tam > 0 else ""
    lineas_bat = [l for l in bateria.split(NL) if l.strip()]''',
'''    bateria = leer(ruta_bat) if existe and tam > 0 else ""
    tam_lf = len(bateria.encode("utf-8"))
    lineas_bat = [l for l in bateria.split(NL) if l.strip()]'''))

# ------------------------------------------------------- LA QUINTA, AL RELEER
PARES.append(('''    extra = 0
    for etiqueta, cond in (
            ("el cuerpo del cierre esta byte a byte", cuerpo.rstrip(NL) in de_nuevo),
            ("cero guiones largos y cero guiones medios",
             chr(8212) not in de_nuevo and chr(8211) not in de_nuevo)):
        print("   %-34s %s" % (etiqueta, "SI" if cond else "NO"))
        if not cond:
            extra += 1
    print("")''',
'''    extra = 0
    huerfanas = cifras_sin_pareja(de_nuevo)
    for etiqueta, cond in (
            ("el cuerpo del cierre esta byte a byte", cuerpo.rstrip(NL) in de_nuevo),
            ("cero guiones largos y cero guiones medios",
             chr(8212) not in de_nuevo and chr(8211) not in de_nuevo),
            ("toda cifra de bytes y todo sha con su pareja", not huerfanas)):
        print("   %-34s %s" % (etiqueta, "SI" if cond else "NO"))
        if not cond:
            extra += 1
    if huerfanas:
        print("   LAS CIFRAS SIN PAREJA, UNA A UNA (vuelta 178, TAREA 1.e):")
        for n, especie, muestra, linea in huerfanas:
            print("      linea %-5d %-5s %-20s | %s" % (n, especie, muestra, linea))
    print("   CIFRA cifras publicadas sin su pareja: %d" % len(huerfanas))
    print("")'''))

for viejo, nuevo in PARES:
    assert viejo in t, "NO ESTA: " + viejo[:70]
    t = t.replace(viejo, nuevo, 1)

io.open(R, "w", encoding="utf-8", newline=NL).write(t)
print("PARCHES APLICADOS: %d" % len(PARES))
print("cerrar_reporte.py -> %d bytes en disco y %d normalizado a LF, %d saltos de linea"
      % (len(t.encode("utf-8")), len(t.encode("utf-8")), t.count(NL)))
