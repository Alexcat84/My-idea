# -*- coding: utf-8 -*-
"""vuelta161_tarea1a_arreglar_alcance.py . TAREA 1.a DE LA VUELTA 161.

ARREGLA `scripts/loop/vuelta159_tarea5_alcance_p16.py` PARA QUE DEJE DE EXCLUIR
POR NOMBRE. La deuda la midio el auditor en la parada del 3 sep 2026
(`docs/loop/paradas/2026-09-03-credito-vara-movil.md`, seccion de las tres
deudas) y el encargo de esta vuelta la manda entera: el instrumento descarta hoy
los buscadores POR NOMBRE, con una nomina cerrada de dos, y por eso ENVEJECE
SOLO: la vuelta 160 escribio tres ficheros mas que contienen el patron y la
cuenta paso de 12 a 15 con exit 1 sin que nadie anadiera un solo check.

LA MANO NO ESCRIBE, ESCRIBE EL INSTRUMENTO (costumbre de la casa desde la vuelta
160, TAREA 3.a): cada edicion es un par (texto viejo literal, texto nuevo
literal) y este script PARA si el texto viejo no aparece EXACTAMENTE una vez.
LA LINEA VIEJA NO SE BORRA: queda TACHADA Y LEGIBLE en un comentario.

ES IDEMPOTENTE: si la marca ya esta escrita, no vuelve a tocar el fichero.

USO:  python scripts/loop/vuelta161_tarea1a_arreglar_alcance.py
"""
import io
import os
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DESTINO = os.path.join(RAIZ, "scripts", "loop", "vuelta159_tarea5_alcance_p16.py")
MARCA = "EXCLUSION POR CONTENIDO (vuelta 161, TAREA 1.a)"

DOC_NUEVO = '''USO:  python scripts/loop/vuelta159_tarea5_alcance_p16.py

--- EXCLUSION POR CONTENIDO (vuelta 161, TAREA 1.a). CORRECCION DECLARADA POR
ADICION: NADA DE LO ESCRITO ARRIBA SE BORRA ---

EL DEFECTO, MEDIDO Y NO ALEGADO: la exclusion de arriba es POR NOMBRE, con una
nomina cerrada de dos ficheros, y por eso ENVEJECE SOLA. Corrido este
instrumento el 3 sep 2026, sin tocarle una letra, daba QUINCE ficheros y exit 1
(salida `docs/loop/SALIDA_V161_T1A_ALCANCE_ANTES.txt`); los tres de mas son de
la vuelta 160 y NINGUNO anade un check: dos escriben el patron para buscarlo o
para editarlo, y el tercero nacio ya con la huella de contenido como vara. La
cifra publicada, DOCE, era la correcta; lo roto era la exclusion.

LA VARA NUEVA, Y SE LEE DEL CONTENIDO CON `tokenize`, NUNCA DEL NOMBRE: el
remedio de la vuelta 160 (TAREA 3.a) estampo en CADA fichero del alcance un
bloque de comentario que empieza por la marca literal del remedio. De ahi salen
las tres clases, y la distincion es la del que LO LLEVA contra la del que LO
ESCRIBE EN OTROS:

  ALCANCE            la marca aparece en un COMENTARIO REAL (token COMMENT) y NO
                     aparece dentro de ninguna constante de cadena: el fichero
                     LLEVA el remedio, o sea que tenia el check.
  ESCRIBE_EL_REMEDIO la marca aparece dentro de una CONSTANTE DE CADENA: el
                     fichero la escribe en otros. Es el caso literal de
                     `vuelta160_tarea3_remedio_p16.py`, cuyo bloque entero vive
                     dentro de una cadena triple.
  SOLO_CITA          contiene el patron y no trae la marca de ninguna forma: lo
                     guarda para buscarlo, o corre git status por otro motivo.
                     No es un check de P.16.

POR QUE ESTO NO ENVEJECE COMO LA NOMINA DE NOMBRES: se pueden anadir cuantos
buscadores, arneses y editores se quiera; ninguno lleva la marca en comentario y
ninguno mueve la cuenta. Este mismo fichero se excluye SOLO, sin nombrarse,
porque la marca solo vive en el dentro de una cadena.

Y LO QUE ESTA VARA NO VE, DICHO EN VEZ DE CALLADO (banco 9, fallar ruidoso): un
fichero NUEVO que anadiera un check de P.16 con `git status` como vara no
llevaria la marca del remedio y quedaria fuera. Para que eso no pase en
silencio, la seccion E imprime un AVISO con los ficheros que EJECUTAN el patron
(lista literal de argumentos en el arbol de sintaxis) y NO llevan la marca. Hoy
sale uno, `vuelta160_tarea3b_caso_positivo.py`, y esta bien que salga: ejecuta
git status para EVALUAR la condicion vieja de otro fichero, y su propia vara es
la huella de contenido desde que nacio.
"""'''

FUNCIONES_NUEVAS = '''def _tokens(texto):
    """(comentarios, cadenas) del TEXTO, leidos con tokenize. Un fichero que no
    tokeniza devuelve dos listas vacias y cae en SOLO_CITA, que es el lado
    seguro: no se mete en el alcance nada que no se haya podido leer."""
    comentarios, cadenas = [], []
    try:
        for t in tokenize.generate_tokens(io.StringIO(texto).readline):
            if t.type == tokenize.COMMENT:
                comentarios.append(t.string)
            elif t.type == tokenize.STRING:
                cadenas.append(t.string)
    except (tokenize.TokenError, IndentationError, SyntaxError):
        return [], []
    return comentarios, cadenas


def clasificar(texto):
    """PURA, y a proposito: recibe el TEXTO del fichero (no su ruta y no su
    nombre) y devuelve la clase. Es LA VARIABLE COMPUTADA sobre la que corre la
    prueba de mutacion de EJECUTOR.md 1 ("EL CASO ROJO SE PRUEBA POR MUTACION"):
    se le puede dar una copia mutada de un fichero real y ver caer el veredicto
    sin tocar el disco."""
    if MEDIA not in texto:
        return "SIN_PATRON"
    comentarios, cadenas = _tokens(texto)
    en_cadena = any(MARCA_DEL_REMEDIO in c for c in cadenas)
    en_comentario = any(MARCA_DEL_REMEDIO in c for c in comentarios)
    if en_cadena:
        return "ESCRIBE_EL_REMEDIO"
    if en_comentario:
        return "ALCANCE"
    return "SOLO_CITA"


def ejecuta_el_patron(texto):
    """PURA. True si el TEXTO trae una lista o tupla literal de cadenas que es
    una invocacion de git status --porcelain sobre dataset/. Sirve SOLO para el
    aviso de la seccion E: un fichero que ejecuta el patron y no lleva la marca
    es justo el sitio por donde esta vara podria quedarse ciega."""
    try:
        arbol = ast.parse(texto)
    except (SyntaxError, ValueError):
        return False
    for n in ast.walk(arbol):
        if not isinstance(n, (ast.List, ast.Tuple)):
            continue
        vals = [e.value for e in n.elts
                if isinstance(e, ast.Constant) and isinstance(e.value, str)]
        if len(vals) != len(n.elts) or not vals:
            continue
        if ("status" in vals and "--porcelain" in vals
                and any(v.startswith("dataset/") for v in vals)):
            return True
    return False


def clasificacion_del_directorio():
    """{nombre: (clase, ejecuta)} de todo .py de scripts/loop/ que contenga el
    patron. Lee el disco; la decision la toma clasificar(), que es pura."""
    fuera = {}
    for nombre in sorted(os.listdir(LOOP)):
        if not nombre.endswith(".py"):
            continue
        try:
            texto = leer(os.path.join(LOOP, nombre))
        except (IOError, UnicodeDecodeError):
            continue
        clase = clasificar(texto)
        if clase == "SIN_PATRON":
            continue
        fuera[nombre] = (clase, ejecuta_el_patron(texto))
    return fuera


def main():
    print("=" * 78)'''

SECCION_E = '''    print("E) LA CLASIFICACION POR CONTENIDO, FICHERO A FICHERO (vuelta 161)")
    for nombre in sorted(clases):
        clase, ejecuta = clases[nombre]
        print("   %-46s %-18s %s" % (nombre, clase,
                                     "ejecuta el patron" if ejecuta else ""))
    print("")
    print("   CIFRA ficheros que contienen el patron: %d" % len(clases))
    for c in ("ALCANCE", "ESCRIBE_EL_REMEDIO", "SOLO_CITA"):
        print("   CIFRA en la clase %s: %d"
              % (c, len([1 for _n, (k, _e) in clases.items() if k == c])))
    aviso = sorted(n for n, (c, e) in clases.items() if c != "ALCANCE" and e)
    print("   CIFRA que EJECUTAN el patron sin llevar la marca (AVISO): %d"
          % len(aviso))
    for n in aviso:
        print("      AVISO: %s ejecuta git status --porcelain" % n)
        print("             sobre dataset/ y NO lleva la marca del remedio. No entra")
        print("             al alcance, y por aqui es por donde esta vara podria")
        print("             quedarse ciega.")
    print("")

    print("D) EL COTEJO CONTRA LA CIFRA DEL ACTA 158, ADJUDICACION 6.7")'''

EDICIONES = [
    ('USO:  python scripts/loop/vuelta159_tarea5_alcance_p16.py\n"""', DOC_NUEVO),

    ('ESPERADO_FICHEROS = 11\nESPERADO_EN_BATERIA = 7',
     '# ESPERADO_FICHEROS, EXCLUSION POR CONTENIDO (vuelta 161, TAREA 1.a): linea\n'
     '#     vieja TACHADA Y LEGIBLE, no borrada. Traia la cifra del acta 158\n'
     '#     (adjudicacion 6.7), que decia ONCE. La adjudicacion 6.1 del acta 159 la\n'
     '#     corrigio a DOCE leyendo la fuente del duodecimo\n'
     '#     (docs/loop/ACTA_AUDITOR.md:52708, leida hoy: "6.1 EL ALCANCE DEL CHECK\n'
     '#     DE P.16 SON DOCE, NO ONCE, Y EL DUODECIMO ENTRA.").\n'
     '#     ~~ESPERADO_FICHEROS = 11~~\n'
     'ESPERADO_FICHEROS = 12\n'
     'ESPERADO_EN_BATERIA = 7\n'
     '\n'
     '# La marca que el remedio de la vuelta 160 estampo en cada fichero del\n'
     '# alcance. Va DENTRO DE UNA CADENA a proposito: asi este fichero cae en la\n'
     '# clase ESCRIBE_EL_REMEDIO y se excluye SOLO, sin que su nombre aparezca en\n'
     '# ninguna nomina.\n'
     'MARCA_DEL_REMEDIO = "REMEDIO DEL CHECK DE P.16 (vuelta 160"'),

    ('        if not nombre.endswith(".py") or nombre in BUSCADORES:\n'
     '            continue',
     '        # EXCLUSION POR CONTENIDO (vuelta 161, TAREA 1.a). Linea vieja\n'
     '        # TACHADA Y LEGIBLE, no borrada:\n'
     '        #     ~~if not nombre.endswith(".py") or nombre in BUSCADORES:~~\n'
     '        # La nomina BUSCADORES se queda escrita arriba como registro de lo\n'
     '        # que se hacia; ya no filtra nada. Las tres lecturas cuentan AHORA\n'
     '        # todo lo que contiene el patron, y quien decide es clasificar().\n'
     '        if not nombre.endswith(".py"):\n'
     '            continue'),

    ('def main():\n    print("=" * 78)', FUNCIONES_NUEVAS),

    ('    print("EXCLUSION DECLARADA: se descartan por nombre los dos buscadores que")\n'
     '    print("contienen el patron porque tienen que escribirlo para buscarlo:")\n'
     '    for b in sorted(BUSCADORES):\n'
     '        print("   %s" % b)\n'
     '    print("")',
     '    # EXCLUSION POR CONTENIDO (vuelta 161, TAREA 1.a). Lineas viejas TACHADAS\n'
     '    # Y LEGIBLES, no borradas:\n'
     '    #     ~~print("EXCLUSION DECLARADA: se descartan por nombre los dos buscadores que")~~\n'
     '    #     ~~print("contienen el patron porque tienen que escribirlo para buscarlo:")~~\n'
     '    #     ~~for b in sorted(BUSCADORES): print("   %s" % b)~~\n'
     '    print("EXCLUSION DECLARADA, Y DESDE LA VUELTA 161 ES POR CONTENIDO Y NO POR")\n'
     '    print("NOMBRE: nadie se descarta por como se llama. Se lee de cada fichero,")\n'
     '    print("con tokenize, si LLEVA la marca del remedio de la vuelta 160 en un")\n'
     '    print("COMENTARIO REAL (esta en el alcance) o si la ESCRIBE dentro de una")\n'
     '    print("constante de cadena (la pone en otros, no la lleva).")\n'
     '    print("   marca: %s" % MARCA_DEL_REMEDIO)\n'
     '    print("   la nomina vieja BUSCADORES queda escrita en el fuente como")\n'
     '    print("   registro de lo que se hacia, y ya no filtra nada.")\n'
     '    print("")'),

    ('    principal = resultados["B MEDIA (pathspec que empieza por dataset/)"]\n'
     '    en_bat = [x for x in principal if x in bat]',
     '    # EXCLUSION POR CONTENIDO (vuelta 161, TAREA 1.a). Linea vieja TACHADA Y\n'
     '    # LEGIBLE, no borrada:\n'
     '    #     ~~principal = resultados["B MEDIA (pathspec que empieza por dataset/)"]~~\n'
     '    # La lectura B sigue imprimiendose entera arriba como contraste; lo que\n'
     '    # cambia es quien manda: manda la clasificacion por contenido.\n'
     '    clases = clasificacion_del_directorio()\n'
     '    principal = sorted(n for n, (c, _e) in clases.items() if c == "ALCANCE")\n'
     '    en_bat = [x for x in principal if x in bat]'),

    ('    print("D) EL COTEJO CONTRA LA CIFRA DEL ACTA 158, ADJUDICACION 6.7")',
     SECCION_E),

    ('    print("   CIFRA que el acta declara, ficheros: %d" % ESPERADO_FICHEROS)',
     '    print("   (la cifra vigente es la de la adjudicacion 6.1 del ACTA 159,")\n'
     '    print("    docs/loop/ACTA_AUDITOR.md:52708, que corrige el once del acta 158)")\n'
     '    print("   CIFRA que el acta declara, ficheros: %d" % ESPERADO_FICHEROS)'),

    ('import io\nimport os\nimport re\nimport sys',
     'import ast\nimport io\nimport os\nimport re\nimport sys\nimport tokenize'),
]

TACHADAS = [
    "~~ESPERADO_FICHEROS = 11~~",
    '~~if not nombre.endswith(".py") or nombre in BUSCADORES:~~',
    '~~print("EXCLUSION DECLARADA: se descartan por nombre los dos buscadores que")~~',
    '~~principal = resultados["B MEDIA (pathspec que empieza por dataset/)"]~~',
]


def leer(ruta):
    return io.open(ruta, encoding="utf-8").read()


def escribir(ruta, texto):
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(texto)


def main():
    print("=" * 78)
    print("VUELTA 161, TAREA 1.a: EL INSTRUMENTO DEL ALCANCE DEJA DE EXCLUIR POR NOMBRE")
    print("=" * 78)
    print("")
    texto = leer(DESTINO)
    if MARCA in texto:
        print("YA ESTABA: la marca '%s' vive en el fichero. No se toca." % MARCA)
        print("CIFRA ediciones aplicadas: 0")
        print("FIN")
        return 0

    aplicadas = 0
    for viejo, nuevo in EDICIONES:
        n = texto.count(viejo)
        if n != 1:
            print("PARADA: el texto viejo de la edicion %d aparece %d veces (tiene"
                  " que aparecer exactamente UNA). No se escribe nada."
                  % (aplicadas + 1, n))
            print("   texto viejo (primeros 90 caracteres): %r" % viejo[:90])
            print("FIN")
            return 1
        texto = texto.replace(viejo, nuevo, 1)
        aplicadas += 1
        print("   edicion %d aplicada" % aplicadas)

    escribir(DESTINO, texto)
    print("")
    print("CIFRA ediciones aplicadas: %d" % aplicadas)
    print("")
    print("LA ADITIVIDAD SE MIDE, NO SE PROMETE (git diff --numstat del destino):")
    r = subprocess.run(["git", "diff", "--numstat", "--",
                        "scripts/loop/vuelta159_tarea5_alcance_p16.py"],
                       cwd=RAIZ, capture_output=True, text=True)
    print("   %s" % r.stdout.strip())
    borrados = 0
    for linea in r.stdout.strip().split("\n"):
        partes = linea.split("\t")
        if len(partes) >= 2 and partes[1].isdigit():
            borrados = int(partes[1])
    print("   CIFRA borrados en el destino: %d" % borrados)
    print("   (los borrados que hay son las lineas SUSTITUIDAS, y cada una queda")
    print("    TACHADA Y LEGIBLE en el comentario que la reemplaza: se comprueba")
    print("    aqui abajo, una a una, que su texto sigue en el fichero.)")
    nuevo_texto = leer(DESTINO)
    faltan = [t for t in TACHADAS if t not in nuevo_texto]
    print("   CIFRA lineas viejas comprobadas como tachadas y legibles: %d de %d"
          % (len(TACHADAS) - len(faltan), len(TACHADAS)))
    if faltan:
        print("   ROJO: no estan tachadas: %s" % ", ".join(faltan))
        print("FIN")
        return 1
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
