# -*- coding: utf-8 -*-
r"""_gen_v206_t2_registros.py . GENERA scripts/loop/_v206_t2_registros.py COMO
CLON DECLARADO DE scripts/loop/_v204_t1_registros.py, COPIANDO TODO LO DEMAS
BYTE A BYTE Y MIDIENDO EL CLON CON difflib.

Fichero de computo con PREFIJO DE GUION BAJO: fuera del censo y fuera de la
nomina (`AUDITOR.md` 6.3, `4.5` del acta 199, `4.6` del acta 203, `4.1` del acta
205). No anade guarda ni lector que se quede vigilando y muere con la vuelta.

LO QUE NO SE CLONA: el COMPUTO del reparto,
`scripts/loop/_v203_reparto_de_actas_viejas.py`, se **IMPORTA** tal cual, igual
que hizo la 204. Por eso no hay cifra de `difflib` del reparto: no hay clon del
reparto que medir.

EL UNICO CAMBIO DE CONDUCTA, Y ES EL QUE EL ENCARGO MANDA: el encargo de la 206
prohibe expresamente contar las preguntas con `REP.preguntas_del_reporte()`,
porque su patron `^##\s+\d+\.\s+PREGUNTAS\b` NO CASA con `## 6. LAS PREGUNTAS` y
el articulo `LAS` le rompe la coincidencia (acta 204 `4.4`, linea 196 de
`_v203_reparto_de_actas_viejas.py`). Ese lector ES CODIGO Y HOY NO SE TOCA: no le
cambio ni un caracter. Lo que hace el clon es CONTAR A MANO en un bloque propio,
`preguntas_a_mano()`, y PISAR con esa cuenta los campos que el reparto dejo, con
la cuenta vieja publicada al lado como contraste.
"""
import difflib
import io
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FUENTE = os.path.join(RAIZ, "scripts", "loop", "_v204_t1_registros.py")
DESTINO = os.path.join(RAIZ, "scripts", "loop", "_v206_t2_registros.py")

DOCSTRING = 'r' + chr(34) * 3 + '''_v206_t2_registros.py . TAREA 2 DE LA VUELTA 206: `R.69` PARA EL ACTA 179 Y
`R.70` PARA EL ACTA 180, LAS DOS ULTIMAS DE LA DEUDA DEL `4.9` DEL ACTA 201.

CLON DECLARADO de `scripts/loop/_v204_t1_registros.py`, generado de el
programaticamente con `scripts/loop/_gen_v206_t2_registros.py`, que imprime
cuantas lineas vienen SIN TOCAR y cuantas son nuevas, contadas con `difflib` y
no a ojo.

EL COMPUTO DEL REPARTO NO SE ESCRIBE POR CUARTA VEZ Y TAMPOCO SE CLONA: se
**IMPORTA** de `scripts/loop/_v203_reparto_de_actas_viejas.py`, el mismo que
usaron la 203 y la 204.

LAS PREGUNTAS SE CUENTAN A MANO Y SE DICE COMO, PORQUE EL ENCARGO LO MANDA. El
lector heredado `REP.preguntas_del_reporte()` casa con
`^##\\s+\\d+\\.\\s+PREGUNTAS\\b` y el articulo `LAS` le rompe la coincidencia, asi
que sobre `## 6. LAS PREGUNTAS` devuelve cero y ademas hace decir a la entrada
que el reporte no titula ninguna seccion de preguntas, que es FALSO. Ese lector
es codigo y hoy NO SE TOCA (acta 204 `4.4`): aqui se cuenta aparte, en
`preguntas_a_mano()`, y **la cuenta vieja se publica al lado como contraste**.

UN CERO DE UN INSTRUMENTO NO ES UN HECHO DEL MUNDO (`EJECUTOR.md` 9): cuando un
patron no halla nada, esta entrada escribe *el patron no encontro nada*, nunca
*no existe*.

EL NUMERO NO SE TECLEA: lo computa `serie_de_registros.siguiente_libre()`
recomputando la serie de sus DOS sedes, y el segundo se computa DESPUES de
escribirse el primero.

USO:
  python scripts/loop/_v206_t2_registros.py
  python scripts/loop/_v206_t2_registros.py --escribir
  python scripts/loop/_v206_t2_registros.py --escribir --salida NOMBRE
''' + chr(34) * 3

# LA FUNCION NUEVA, INSERTADA ENTERA Y DECLARADA COMO NUEVA. No pisa ninguna
# funcion de la fuente: se anade delante de `def main()`.
FUNCION_NUEVA = '''def preguntas_a_mano(m, vuelta, w):
    """LAS PREGUNTAS DEL REPORTE ARCHIVADO, CONTADAS A MANO Y NO CON EL LECTOR
    HEREDADO. Pisa los campos de preguntas que dejo `REP.medir_acta()` y publica
    la cuenta vieja al lado como contraste, sin borrarla.

    COMO CUENTO, DICHO PARA QUE SE PUEDA RECONTAR:

      1. busco TODA seccion `## N. TITULO` cuyo TITULO nombre la palabra
         PREGUNTAS, sin exigir que la palabra vaya pegada al numero, que es lo
         que el patron heredado si exige y por lo que se le escapa `LAS`;
      2. acoto esa seccion hasta la siguiente `## N.`;
      3. saco de ahi las claves `P.n` en LAS DOS FORMAS que los reportes de esta
         campana usan, con comillas inversas y sin ellas, porque el reporte 179
         escribe `**P.1.` y el 180 escribe ``**`P.1`.``;
      4. pego las lineas crudas de las que sale cada clave, para que la cuenta se
         pueda rehacer sin volver a correr nada.

    SI EL PATRON NO HALLA NADA se dice EL PATRON NO ENCONTRO NADA, y la cifra NO
    se publica como un cero del mundo."""
    ruta = os.path.join(LOOP, "reportes", "REPORTE_V%d.md" % vuelta)
    w("   cuento a mano sobre: docs/loop/reportes/REPORTE_V%d.md" % vuelta)
    viejas = list(m.get("del_reporte") or [])
    vieja_seccion = m.get("seccion_preg")
    w("   LA CUENTA VIEJA, DEL LECTOR HEREDADO, PUBLICADA COMO CONTRASTE Y NO")
    w("   BORRADA: %d clave(s) (%s) | %s"
      % (len(viejas), ", ".join(viejas) or "ninguna", vieja_seccion))
    if not os.path.isfile(ruta):
        w("   EL PATRON NO ENCONTRO EL FICHERO, y eso NO dice que no exista el")
        w("   reporte: dice que no esta en esa ruta. La cifra no se publica.")
        return
    lineas = io.open(ruta, encoding="utf-8").read().replace(
        chr(13) + NL, NL).split(NL)
    cabeceras = [(i, l) for i, l in enumerate(lineas, 1)
                 if re.match(r"^##\\s+\\d+\\.", l)]
    conpreg = [(i, l) for i, l in cabeceras if "PREGUNTAS" in l.upper()]
    w("   CIFRA secciones `## N.` en el reporte: %d" % len(cabeceras))
    w("   CIFRA de ellas cuyo TITULO nombra PREGUNTAS: %d" % len(conpreg))
    for i, l in conpreg:
        w("      linea %d | %s" % (i, l.strip()))
    if len(conpreg) != 1:
        w("   EL PATRON NO ENCONTRO EXACTAMENTE UNA. La cifra no se publica por")
        w("   esta via y los campos del reparto se quedan como estaban.")
        return
    a0 = conpreg[0][0]
    sig = [i for i, _l in cabeceras if i > a0]
    b0 = (sig[0] - 1) if sig else len(lineas)
    w("   seccion acotada: lineas %d a %d (%d lineas)" % (a0, b0, b0 - a0 + 1))
    claves = []
    for i in range(a0, b0 + 1):
        linea = lineas[i - 1]
        for mm in re.finditer(r"`(P\\.\\d+)`|\\*\\*(P\\.\\d+)\\.", linea):
            c = mm.group(1) or mm.group(2)
            if c not in claves:
                claves.append(c)
                w("      linea %d clava %s | %s" % (i, c, linea.strip()[:96]))
    w("   CIFRA claves `P.n` contadas a mano en esa seccion: %d (%s)"
      % (len(claves), ", ".join(claves) or "ninguna"))
    if len(claves) != len(viejas):
        w("   LA DISCREPANCIA SE DECLARA Y NO SE RESUELVE COPIANDO: el lector")
        w("   heredado dice %d y mi cuenta a mano dice %d. Las dos quedan escritas."
          % (len(viejas), len(claves)))
    nombradas = list(m.get("nombradas") or [])
    m["del_reporte"] = claves
    m["preguntas"] = [p for p in nombradas if p in claves]
    m["fuera"] = [p for p in nombradas if p not in claves]
    m["preguntas_a_mano"] = claves
    m["preguntas_a_mano_seccion"] = (conpreg[0][1].strip(), a0, b0)
    # EL NUMERAL SIGUE `NO COMPUTABLE` CUANDO NO HAY DE DONDE CONTARLO, Y EL
    # REPARTO MEDIDO VA DEBAJO COMO MEDICION (acta 204 `4.6`, que el encargo de
    # la 206 cita para las entradas DESDE `R.69`). Si el acta no titula ninguna
    # seccion de adjudicaciones, no hay titulo que pueda nombrar una `P.n`, y un
    # cero ahi se leeria como QUE EL ACTA NO CONTESTO NINGUNA PREGUNTA. Eso es
    # justo la caida que el acta 205 le cobro a la 204 sobre `R.67` y `R.68`.
    m["preguntas_numeral"] = len(m["preguntas"]) if nombradas else None
    w("   CIFRA claves `P.n` nombradas en titulos de adjudicaciones: %d"
      % len(nombradas))
    w("   EL NUMERAL DE PREGUNTAS ES: %s"
      % ("NO COMPUTABLE, porque ninguna seccion de esta acta titula las "
         "adjudicaciones y no hay titulo del que sacar una `P.n`"
         if not nombradas else "%d" % len(m["preguntas"])))
    m["hay_seccion_preg"] = True
    m["seccion_preg"] = ("la seccion de preguntas se titula %r, en la linea %d, y "
                         "sus claves las conte A MANO en la vuelta 206 porque el "
                         "lector heredado no la ve"
                         % (conpreg[0][1].strip(), a0))
    m["via_preguntas"] = ("FILTRADAS contra la seccion de PREGUNTAS del reporte "
                          "archivado, CONTADA A MANO en la vuelta 206 y NO con "
                          "`preguntas_del_reporte()`, cuyo patron el articulo "
                          "`LAS` le rompe (acta 204 `4.4`)")
    w("   CIFRA preguntas del numeral, recomputada a mano: %d (%s)"
      % (len(m["preguntas"]), ", ".join(m["preguntas"]) or "ninguna"))


'''

CAMBIOS = [
    ("VUELTA_QUE_ESCRIBE = 204", "VUELTA_QUE_ESCRIBE = 206", 1),
    ("SUJETOS = [177, 178]", "SUJETOS = [179, 180]", 1),
    ('ap.add_argument("--salida", default="T1_REGISTROS")',
     'ap.add_argument("--salida", default="T2_REGISTROS")', 1),
    ('a("(Acta del auditor, vuelta %d; escrito en la vuelta %d, TAREA 1.)"',
     'a("(Acta del auditor, vuelta %d; escrito en la vuelta %d, TAREA 2.)"', 1),
    ('a("Por adicion, como `R.21` a `R.66`. **Corte de todas las cifras de esta")',
     'a("Por adicion, como `R.21` a `R.68`. **Corte de todas las cifras de esta")',
     1),
    ('a("Salida: `docs/loop/SALIDA_V%d_T1_REGISTROS.txt`." % VUELTA_QUE_ESCRIBE)',
     'a("Salida: `docs/loop/SALIDA_V%d_T2_REGISTROS.txt`." % VUELTA_QUE_ESCRIBE)',
     1),
    ('    w("VUELTA %d, TAREA 1: R.67 PARA EL ACTA 177 Y R.68 PARA EL ACTA 178,"',
     '    w("VUELTA %d, TAREA 2: R.69 PARA EL ACTA 179 Y R.70 PARA EL ACTA 180,"',
     1),
    ('    w("LAS DOS SIGUIENTES DE LA DEUDA DEL 4.9 DEL ACTA 201, REMEDIDA AQUI")',
     '    w("LAS DOS ULTIMAS DE LA DEUDA DEL 4.9 DEL ACTA 201, REMEDIDA AQUI")',
     1),
    ('for etiqueta, vuelta in zip(("1.a", "1.b"), SUJETOS):',
     'for etiqueta, vuelta in zip(("2.a", "2.b"), SUJETOS):', 1),
    # EL UNICO CAMBIO DE CONDUCTA: LAS PREGUNTAS SE CUENTAN A MANO.
    ('        m = REP.medir_acta(vuelta, w)' + NL + '        w("")',
     '        m = REP.medir_acta(vuelta, w)' + NL + '        w("")' + NL +
     '        w("C.1) LAS PREGUNTAS, CONTADAS A MANO Y NO CON el lector heredado,")' + NL +
     '        w("     porque el encargo de la 206 lo prohibe expresamente")' + NL +
     '        if m is not None:' + NL +
     '            preguntas_a_mano(m, vuelta, w)' + NL +
     '        w("")', 1),
    # EL NUMERAL DE PREGUNTAS PUEDE SER `NO COMPUTABLE`, COMO SUS CUATRO
    # HERMANOS. Hasta aqui era el unico de los cinco que SIEMPRE salia numero,
    # porque se computaba con `len()` sobre una lista vacia.
    ('    preg = len(m["preguntas"])',
     '    preg = (m["preguntas_numeral"] if "preguntas_numeral" in m'
     + NL + '            else len(m["preguntas"]))', 1),
    # LA FILA DE LA TABLA, Y EL REPARTO MEDIDO DEBAJO COMO MEDICION.
    ('    a("| preguntas contestadas | (no es una seccion: son las `P.n` que los titulos "' + NL +
     '      "de las adjudicaciones nombran) | (no aplica) | (no aplica) | %s | **%d** |"' + NL +
     '      % (", ".join("`%s`" % x for x in m["preguntas"]) or "(ninguna)",' + NL +
     '         len(m["preguntas"])))',
     '    _pn = m.get("preguntas_numeral", len(m["preguntas"]))' + NL +
     '    a("| preguntas contestadas | (no es una seccion: son las `P.n` que los titulos "' + NL +
     '      "de las adjudicaciones nombran) | (no aplica) | (no aplica) | %s | %s |"' + NL +
     '      % (", ".join("`%s`" % x for x in m["preguntas"]) or "(ninguna)",' + NL +
     '         "**no computable**" if _pn is None else "**%d**" % _pn))', 1),
    ('    a("")' + NL +
     '    a("### LAS DOS LECTURAS, PUBLICADAS JUNTAS Y CON LA DISCREPANCIA DECLARADA")',
     '    a("")' + NL +
     '    if m.get("preguntas_a_mano") is not None:' + NL +
     '        _t, _a0, _b0 = m["preguntas_a_mano_seccion"]' + NL +
     '        a("### EL REPARTO MEDIDO DE LAS PREGUNTAS, QUE NO ES EL NUMERAL")' + NL +
     '        a("")' + NL +
     '        a("**ESTO ES UNA MEDICION Y NO UN NUMERAL** (acta 204 `4.6`, que el encargo")' + NL +
     '        a("de la vuelta 206 cita para las entradas desde `R.69`). El numeral de")' + NL +
     '        a("arriba se queda como esta; esto va debajo y no lo sustituye.")' + NL +
     '        a("")' + NL +
     '        a("**COMO SE CONTO, DICHO PARA QUE SE PUEDA RECONTAR SIN CORRER NADA:** en")' + NL +
     '        a("`%s` la seccion de preguntas se titula" % m["ruta_rep"])' + NL +
     '        a("**%s**, en la linea **%d**, y va hasta la **%d**. De ahi salen las claves"' + NL +
     '          % (_t.replace("#", "").strip(), _a0, _b0))' + NL +
     '        a("`P.n` EN LAS DOS FORMAS que esta campana usa, con comillas inversas y sin")' + NL +
     '        a("ellas. **EL LECTOR HEREDADO NO LAS VE**: su patron exige que la palabra")' + NL +
     '        a("PREGUNTAS vaya pegada al numero de seccion y el articulo `LAS` se lo")' + NL +
     '        a("rompe (acta 204 `4.4`, linea 196 de `_v203_reparto_de_actas_viejas.py`),")' + NL +
     '        a("y ese lector ES CODIGO Y NO SE TOCO EN ESTA VUELTA.")' + NL +
     '        a("")' + NL +
     '        a("| lectura | claves `P.n` en la seccion de preguntas del reporte | cuantas |")' + NL +
     '        a("|---|---|---:|")' + NL +
     '        a("| **contada a mano en la vuelta 206** | %s | **%d** |"' + NL +
     '          % (", ".join("`%s`" % x for x in m["preguntas_a_mano"]) or "(ninguna)",' + NL +
     '             len(m["preguntas_a_mano"])))' + NL +
     '        a("| el lector heredado, `REP.preguntas_del_reporte()`, publicado como "' + NL +
     '          "contraste | el patron no encontro nada | 0 |")' + NL +
     '        a("")' + NL +
     '        a("**LA DISCREPANCIA SE DECLARA Y NO SE RESUELVE COPIANDO** (`EJECUTOR.md`")' + NL +
     '        a("2). **EL CERO DEL HEREDADO NO ES UN HECHO DEL MUNDO**: es que su patron")' + NL +
     '        a("no encontro nada (`EJECUTOR.md` 9).")' + NL +
     '        a("")' + NL +
     '    a("### LAS DOS LECTURAS, PUBLICADAS JUNTAS Y CON LA DISCREPANCIA DECLARADA")', 1),
    ("def main():", FUNCION_NUEVA + "def main():", 1),
]

src = io.open(FUENTE, encoding="utf-8").read().replace(chr(13) + NL, NL)
L = src.split(NL)
n_antes = len(L)

assert L[0].startswith("# -*- coding"), L[0][:60]
assert L[1].startswith('r' + chr(34) * 3 + '_v204_t1_registros.py'), L[1][:60]
cierres = [i for i in range(2, len(L)) if L[i] == chr(34) * 3]
assert cierres, "no se encuentra el cierre del docstring"
fin_doc = cierres[0]
doc_viejo = NL.join(L[1:fin_doc + 1])
texto = L[0] + NL + DOCSTRING + NL + NL.join(L[fin_doc + 1:])
print("1) DOCSTRING: %d lineas viejas -> %d lineas nuevas"
      % (doc_viejo.count(NL) + 1, DOCSTRING.count(NL) + 1))

print("2) LOS CAMBIOS PUNTUALES, CADA UNO CON SU CUENTA DE APARICIONES:")
for viejo, nuevo, esperadas in CAMBIOS:
    hay = texto.count(viejo)
    assert hay == esperadas, (viejo[:70], hay, esperadas)
    texto = texto.replace(viejo, nuevo)
    print("   %-3d aparicion(es)  %s" % (hay, viejo.split(NL)[0][:66]))

nuevas = texto.split(NL)
sm = difflib.SequenceMatcher(None, L, nuevas, autojunk=False)
iguales = sum(b.size for b in sm.get_matching_blocks())
print("")
print("EL CLON, MEDIDO Y NO AFIRMADO (difflib.SequenceMatcher):")
print("   CIFRA lineas de la fuente %s: %d" % (os.path.basename(FUENTE), n_antes))
print("   CIFRA lineas del destino %s: %d"
      % (os.path.basename(DESTINO), len(nuevas)))
print("   CIFRA lineas que vienen SIN TOCAR de la fuente: %d" % iguales)
print("   CIFRA lineas nuevas o cambiadas en el destino: %d"
      % (len(nuevas) - iguales))
print("")
print("EL LECTOR HEREDADO DE PREGUNTAS NO SE TOCA, Y SE COMPRUEBA AQUI:")
print("   CIFRA veces que este generador escribe 'def preguntas_del_reporte': %d"
      % texto.count("def preguntas_del_reporte"))
print("   CIFRA veces que el destino llama a REP.preguntas_del_reporte: %d"
      % texto.count("REP.preguntas_del_reporte"))
print("")
print("EL COMPUTO DEL REPARTO NO SE CLONA: SE IMPORTA. Por eso no hay cifra de")
print("   difflib para el, y la linea del import se copia sin tocar:")
for i, l in enumerate(nuevas, 1):
    if "_v203_reparto_de_actas_viejas" in l:
        print("   linea %d | %s" % (i, l.strip()))

io.open(DESTINO, "w", encoding="utf-8", newline=NL).write(texto)
print("")
print("ESCRITO: scripts/loop/_v206_t2_registros.py (%d bytes)"
      % len(texto.encode("utf-8")))
