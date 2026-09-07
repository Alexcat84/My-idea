# -*- coding: utf-8 -*-
r"""_gen_v202_t4.py . GENERA scripts/loop/_v202_t4_registrar_actas.py COMO CLON
DECLARADO DEL REGISTRADOR DE LA 201, COPIANDO TODO LO DEMAS BYTE A BYTE.

Fichero de computo con PREFIJO DE GUION BAJO. Cambia SIETE cosas y las imprime
una a una; todo lo demas, incluidas las funciones puras y la prueba de
idempotencia, se copia sin tocar.
"""
import difflib
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _gen_v202_t4_piezas as P   # noqa: E402

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FUENTE = os.path.join(RAIZ, "scripts", "loop", "_v201_t1_registrar_actas.py")
DESTINO = os.path.join(RAIZ, "scripts", "loop", "_v202_t4_registrar_actas.py")

src = io.open(FUENTE, encoding="utf-8").read().replace(chr(13) + NL, NL)
L = src.split(NL)
cambios = []

# 1. EL DOCSTRING: linea 1 es el coding; el docstring va de la 2 al primer cierre.
assert L[0].startswith("# -*- coding"), L[0][:60]
assert L[1].startswith("r" + chr(34) * 3 + "_v201_t1_registrar_actas.py"), L[1][:60]
fin_doc = next(i for i in range(2, len(L)) if L[i] == chr(34) * 3)
texto = L[0] + NL + P.DOCSTRING + NL + NL.join(L[fin_doc + 1:])
cambios.append(("docstring", fin_doc, P.DOCSTRING.count(NL) + 1))

# 2. LA CONSTANTE DE LA VUELTA QUE ESCRIBE.
assert texto.count("VUELTA_QUE_ESCRIBE = 201") == 1
texto = texto.replace("VUELTA_QUE_ESCRIBE = 201", "VUELTA_QUE_ESCRIBE = 202")
cambios.append(("VUELTA_QUE_ESCRIBE", "201", "202"))

# 3. LOS CASOS DE LA PRUEBA DE IDEMPOTENCIA: sujeto y numero nuevos.
i = texto.index("        titulo200 = ")
j = texto.index("        ]" + NL, i) + len("        ]")
cambios.append(("casos de la prueba", len(texto[i:j]), len(P.CASOS)))
texto = texto[:i] + P.CASOS + texto[j:]

# 4. LAS DOS GLOSAS.
i = texto.index("GLOSA_200 = [")
j = texto.index(NL + "]" + NL, texto.index("GLOSA_198 = [")) + len(NL + "]")
cambios.append(("glosas", len(texto[i:j]), len(P.GLOSAS)))
texto = texto[:i] + P.GLOSAS + texto[j:]

# 5. LOS DOS SUJETOS DEL BUCLE.
viejo_bucle = ('    for etiqueta, vuelta, glosa in (("1.a", 200, GLOSA_200),' + NL
               + '                                    ("1.b", 198, GLOSA_198)):')
nuevo_bucle = ('    for etiqueta, vuelta, glosa in (("4.a", 173, GLOSA_173),' + NL
               + '                                    ("4.b", 174, GLOSA_174)):')
assert texto.count(viejo_bucle) == 1
texto = texto.replace(viejo_bucle, nuevo_bucle)
cambios.append(("sujetos del bucle", "200 y 198", "173 y 174"))

# 6. EL NOMBRE DE LA SALIDA Y LAS ETIQUETAS DE TAREA.
for viejo, nuevo, veces in (
        ('SALIDA_V%d_T1_REGISTROS.txt', 'SALIDA_V%d_T4_REGISTROS.txt', 2),
        ('escrito en la vuelta %d, TAREA 1.', 'escrito en la vuelta %d, TAREA 4.', 1),
        ('Por adicion, como `R.21` a `R.60`.', 'Por adicion, como `R.21` a `R.62`.', 1),
        ('LOS DOS REGISTROS DE LA VUELTA %d, TAREA 1: EL ACTA 200 (1.a) Y LA VUELTA',
         'LOS DOS REGISTROS DE LA VUELTA %d, TAREA 4: EL ACTA 173 (4.a) Y EL ACTA',
         1),
        ('w("198 (1.b, POR LA ADJUDICACION 4.7 DEL ACTA 200)")',
         'w("174 (4.b), LAS DOS MAS VIEJAS DE LA DEUDA DE OCHO DEL ACTA 201 4.9")',
         1)):
    n = texto.count(viejo)
    assert n == veces, (viejo, n, veces)
    texto = texto.replace(viejo, nuevo)
    cambios.append((viejo[:44], n, "sustituido"))

# 7. LA COTA DE LA DEUDA QUE SE REMIDE AL CIERRE: el rango sigue siendo 173 a
#    200 y NO se toca, porque la deuda del acta 201 es 173 a 180 y el rango
#    ancho no esconde nada; lo unico que cambia es la frase que lo acompana.
assert texto.count("sin, con = actas_sin_entrada(despues, 173, 200)") == 1

io.open(DESTINO, "w", encoding="utf-8", newline=NL).write(texto)

print("FUENTE : %s (%d bytes, %d lineas)"
      % (os.path.relpath(FUENTE, RAIZ).replace(os.sep, "/"),
         len(src.encode("utf-8")), len(L)))
print("DESTINO: %s (%d bytes, %d lineas)"
      % (os.path.relpath(DESTINO, RAIZ).replace(os.sep, "/"),
         len(texto.encode("utf-8")), len(texto.split(NL))))
print("")
print("LAS PIEZAS QUE CAMBIAN, UNA A UNA:")
for c in cambios:
    print("   %s" % (c,))
print("")
a_l, b_l = src.split(NL), texto.split(NL)
sm = difflib.SequenceMatcher(None, a_l, b_l, autojunk=False)
iguales = sum(bl.size for bl in sm.get_matching_blocks())
print("CIFRA lineas de la fuente: %d | del destino: %d" % (len(a_l), len(b_l)))
print("CIFRA lineas COPIADAS SIN TOCAR, contadas con difflib: %d" % iguales)
print("CIFRA lineas del destino que NO vienen de la fuente: %d"
      % (len(b_l) - iguales))

# ---------------------------------------------------------------------------
# 8, 9 Y 10. LAS TRES PIEZAS QUE LA CONVENCION VIEJA DE LAS ACTAS 173 Y 174
# OBLIGA A CAMBIAR, Y SE DICE POR QUE ANTES DE CAMBIARLAS.
#
# MEDIDO Y NO SUPUESTO: los cinco lectores heredados devuelven CERO sobre estas
# dos actas, y el cero NO ES AUSENCIA, ES CONVENCION. Las actas 173 y 174 son
# ANTERIORES a la 184: escriben sus claves como cabeceras markdown `### 4.1` y
# no como ``**`4.1` ...``, su seccion 4 es LOS HALLAZGOS y no LAS ADJUDICACIONES,
# y sus adjudicaciones viven en la seccion 6 sin clave numerada.
#
# LA VUELTA 201 YA SENTO EL PRECEDENTE Y AQUI SE SIGUE: sobre la entrada de la
# 198 escribio que no publicaba un cero "que se leeria como que el acta 198 no
# contesto ninguna pregunta". Un titulo que diga "las cero adjudicaciones
# numeradas del acta de la vuelta 173" seria exactamente esa lectura falsa.
#
# POR ESO: el titulo heredado SE SIGUE COMPUTANDO Y SE PUBLICA EN LA SALIDA COMO
# CONTRASTE, pero NO SE USA COMO TITULO. Y la frase de los cinco numerales dice
# lo que se midio y con que vara, en vez de pegar cinco ceros.
texto2 = io.open(DESTINO, encoding="utf-8").read().replace(chr(13) + NL, NL)

VIEJO_TITULO = '''    w("C) EL TITULO, CON SUS CINCO NUMERALES COMPUTADOS")
        titulo = titulo_computado(m, w)
        if titulo is None:
            continue'''
NUEVO_TITULO = '''    w("C) EL TITULO. LOS CINCO NUMERALES HEREDADOS SE COMPUTAN Y SE")
        w("   PUBLICAN COMO CONTRASTE, PERO NO SE USAN COMO TITULO, Y EL MOTIVO")
        w("   ESTA MEDIDO: los cinco lectores heredados dan CERO sobre esta acta")
        w("   porque es de la convencion ANTERIOR a la 184. Un titulo que dijera")
        w("   'las cero adjudicaciones numeradas' se leeria como que el acta no")
        w("   adjudico nada, y la vuelta 201 ya rechazo esa lectura falsa en su")
        w("   entrada de la 198.")
        titulo_heredado = titulo_computado(m, w)
        w("   TITULO HEREDADO, PUBLICADO COMO CONTRASTE Y NO USADO:")
        w("      %s" % (titulo_heredado or "(no computable)"))
        titulo = ("Registro del acta de la vuelta %d, con sus cinco numerales NO "
                  "COMPUTABLES POR LOS LECTORES HEREDADOS porque el acta es de la "
                  "convencion anterior a la 184" % m["vuelta"])
        w("   TITULO ESCRITO: %s" % titulo)'''
assert texto2.count(VIEJO_TITULO) == 1, "ancla del titulo"
texto2 = texto2.replace(VIEJO_TITULO, NUEVO_TITULO)

VIEJO_NUM = '''    p.append("**LOS CINCO NUMERALES DEL TITULO NO ESTAN TECLEADOS:** se cuentan del acta")
    p.append("acotada (lineas %d a %d, sobre un fichero de %d bytes en disco y %d "
             "normalizado a LF). **%d adjudicaciones numeradas, %d "
             "hallazgos numerados en la seccion 5, %d preguntas contestadas, "
             "%d caidas propias del auditor y %d caidas del ejecutor.**"
             % (m["ini"], m["fin"], m["bytes_disco"], m["bytes_lf"],
                len(m["adj"]), len(m["hal"]), len(m["preguntas"]),
                len(m["cai_aud"]), len(m["cai_eje"])))'''
NUEVO_NUM = '''    p.append("**LOS CINCO NUMERALES NO SE PUBLICAN COMO REPARTO, Y EL MOTIVO ESTA MEDIDO,")
    p.append("NO SUPUESTO.** El acta acotada va de la linea %d a la %d, sobre un fichero de"
             % (m["ini"], m["fin"]))
    p.append("%d bytes en disco y %d normalizado a LF. Sobre ese cuerpo, los cinco lectores"
             % (m["bytes_disco"], m["bytes_lf"]))
    p.append("heredados devuelven **%d, %d, %d, %d y %d**: `R84.claves_entrecomilladas()`"
             % (len(m["adj"]), len(m["hal"]), len(m["preguntas"]),
                len(m["cai_aud"]), len(m["cai_eje"])))
    p.append("con prefijo `4.`, con prefijo `5.` y con prefijo `C.A`, el numeral de")
    p.append("preguntas, y `R94.caidas_propias_entrecomilladas()`. **ESOS CINCO CEROS SON")
    p.append("DE CONVENCION Y NO DE AUSENCIA**, y por eso **no se publican como el reparto")
    p.append("del acta**: esta acta es **ANTERIOR a la 184** y escribe sus claves como")
    p.append("**cabeceras markdown** `### 4.1`, no como ``**`4.1` ...``; ademas **su seccion")
    p.append("4 es LOS HALLAZGOS y no LAS ADJUDICACIONES**, sus adjudicaciones viven en la")
    p.append("**seccion 6 sin clave numerada**, y sus caidas propias del auditor en la")
    p.append("**seccion 3**. **La vuelta 201 ya rechazo publicar un cero de esta especie**")
    p.append("en su entrada de la 198, con estas palabras: *lo dice en vez de publicar un")
    p.append("cero que se leeria como que el acta no contesto ninguna pregunta*.")
    p.append("")
    p.append("**LO QUE SI SE MIDE Y SE PUBLICA ES LA ESTRUCTURA DEL ACTA**, contada por el")
    p.append("bloque `H.2` del sello de apertura de esta vuelta,")
    p.append("`docs/loop/SALIDA_V%d_APERTURA.txt`, que es un instrumento que YA CORRIO y no"
             % VUELTA_QUE_ESCRIBE)
    p.append("un lector nuevo. **Y LO QUE FALTA SE TRAE COMO PARADA en vez de improvisarse:**")
    p.append("computar el reparto de esta acta pide **o un lector para la convencion vieja**,")
    p.append("que la moratoria `AUDITOR.md` 6.3 prohibe fabricar, **o decidir que seccion del")
    p.append("acta vieja cuenta como cada numeral**, que es **DECIDIR y no medir**")
    p.append("(`AUDITOR.md` 3). **No lo arregla el ejecutor.**")'''
assert texto2.count(VIEJO_NUM) == 1, "ancla de los numerales"
texto2 = texto2.replace(VIEJO_NUM, NUEVO_NUM)

io.open(DESTINO, "w", encoding="utf-8", newline=NL).write(texto2)
print("")
print("PIEZAS 8 Y 9 APLICADAS: el titulo heredado se publica como contraste y no")
print("   se usa; la frase de los cinco numerales declara la convencion en vez de")
print("   pegar cinco ceros.")
b2 = texto2.split(NL)
sm2 = difflib.SequenceMatcher(None, a_l, b2, autojunk=False)
ig2 = sum(bl.size for bl in sm2.get_matching_blocks())
print("CIFRA lineas del destino FINAL: %d | copiadas sin tocar: %d | nuevas: %d"
      % (len(b2), ig2, len(b2) - ig2))
