# -*- coding: utf-8 -*-
"""vuelta159_tarea5_alcance_p16.py . TAREA 5.b DE LA VUELTA 159, EL ALCANCE DEL
CHECK DE P.16, RECOMPUTADO.

POR QUE NACE Y POR QUE SE QUEDA AQUI. El encargo de la vuelta 159 dice, literal:
"EL ALCANCE, MEDIDO POR MI Y RECOMPUTALO TU: once ficheros de scripts/loop/
llevan el patron literal, siete de ellos dentro de la bateria de las 23. SI TU
CUENTA NO DA ONCE, PARAS Y LO DICES."

ESTE INSTRUMENTO SOLO CUENTA. NO TOCA UN SOLO CHECK. Publica la nomina bajo TRES
lecturas distintas de "el patron literal", el cruce con la bateria de las 23, y
el fichero que explica la diferencia con la cifra del acta.

LAS TRES LECTURAS, PORQUE "EL PATRON LITERAL" ADMITE MAS DE UNA Y NO SE ELIGE LA
QUE CONVIENE:
  (A) LA ESTRECHA: el codigo invoca `git status --porcelain` con los DOS
      pathspec que el docstring de la 6.7 nombra, `dataset/` Y `docs/plan/`.
  (B) LA MEDIA: el codigo invoca `git status --porcelain` con un pathspec que
      EMPIEZA por `dataset/`. Es la que este instrumento toma como principal,
      porque la 6.7 describe el defecto por su INSTRUMENTO (git status ve fin de
      linea y suciedad previa) y ese defecto lo tiene cualquier pathspec sobre
      `dataset/`.
  (C) LA ANCHA: el codigo invoca `git status --porcelain` con cualquier
      pathspec o sin ninguno.

LA EXCLUSION QUE SE DECLARA EN VEZ DE CALLARSE, Y ES LA MISMA TRAMPA QUE
`verificar_apertura_sellada.py` lleva escrita desde la vuelta 102: UN BUSCADOR
DE UN PATRON CONTIENE EL PATRON QUE BUSCA. Se descartan POR NOMBRE este fichero
y `vuelta159_tarea1_registrar_adjudicaciones.py`, que es el otro que lo escribe
para buscarlo. Sin esa exclusion la cuenta sale inflada en dos, y la primera
corrida de la TAREA 1 de esta vuelta lo demostro saliendo TRECE.

USO:  python scripts/loop/vuelta159_tarea5_alcance_p16.py

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
"""
import ast
import io
import os
import re
import sys
import tokenize

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "scripts", "loop")
BATERIA = os.path.join(LOOP, "verificar_mutaciones_viejas.py")

ESTRECHA = '"--porcelain", "--", "dataset/", "docs/plan/"'
MEDIA = '"--porcelain", "--", "dataset/'
ANCHA = '"--porcelain"'

BUSCADORES = {
    "vuelta159_tarea5_alcance_p16.py",
    "vuelta159_tarea1_registrar_adjudicaciones.py",
}

# ESPERADO_FICHEROS, EXCLUSION POR CONTENIDO (vuelta 161, TAREA 1.a): linea
#     vieja TACHADA Y LEGIBLE, no borrada. Traia la cifra del acta 158
#     (adjudicacion 6.7), que decia ONCE. La adjudicacion 6.1 del acta 159 la
#     corrigio a DOCE leyendo la fuente del duodecimo
#     (docs/loop/ACTA_AUDITOR.md:52708, leida hoy: "6.1 EL ALCANCE DEL CHECK
#     DE P.16 SON DOCE, NO ONCE, Y EL DUODECIMO ENTRA.").
#     ~~ESPERADO_FICHEROS = 11~~
ESPERADO_FICHEROS = 12
ESPERADO_EN_BATERIA = 7

# La marca que el remedio de la vuelta 160 estampo en cada fichero del
# alcance. Va DENTRO DE UNA CADENA a proposito: asi este fichero cae en la
# clase ESCRIBE_EL_REMEDIO y se excluye SOLO, sin que su nombre aparezca en
# ninguna nomina.
MARCA_DEL_REMEDIO = "REMEDIO DEL CHECK DE P.16 (vuelta 160"


def leer(ruta):
    return io.open(ruta, encoding="utf-8").read()


def con_patron(patron):
    salida = []
    for nombre in sorted(os.listdir(LOOP)):
        # EXCLUSION POR CONTENIDO (vuelta 161, TAREA 1.a). Linea vieja
        # TACHADA Y LEGIBLE, no borrada:
        #     ~~if not nombre.endswith(".py") or nombre in BUSCADORES:~~
        # La nomina BUSCADORES se queda escrita arriba como registro de lo
        # que se hacia; ya no filtra nada. Las tres lecturas cuentan AHORA
        # todo lo que contiene el patron, y quien decide es clasificar().
        if not nombre.endswith(".py"):
            continue
        try:
            if patron in leer(os.path.join(LOOP, nombre)):
                salida.append(nombre)
        except (IOError, UnicodeDecodeError):
            continue
    return salida


def nomina_bateria():
    t = leer(BATERIA)
    return [m[0] for m in re.findall(r'^\s*\("(vuelta[^"]+\.py)",\s*(True|False)\)',
                                     t, re.M)]


def _tokens(texto):
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
    print("=" * 78)
    print("VUELTA 159, TAREA 5.b: EL ALCANCE DEL CHECK DE P.16, RECOMPUTADO")
    print("=" * 78)
    print("")
    # EXCLUSION POR CONTENIDO (vuelta 161, TAREA 1.a). Lineas viejas TACHADAS
    # Y LEGIBLES, no borradas:
    #     ~~print("EXCLUSION DECLARADA: se descartan por nombre los dos buscadores que")~~
    #     ~~print("contienen el patron porque tienen que escribirlo para buscarlo:")~~
    #     ~~for b in sorted(BUSCADORES): print("   %s" % b)~~
    print("EXCLUSION DECLARADA, Y DESDE LA VUELTA 161 ES POR CONTENIDO Y NO POR")
    print("NOMBRE: nadie se descarta por como se llama. Se lee de cada fichero,")
    print("con tokenize, si LLEVA la marca del remedio de la vuelta 160 en un")
    print("COMENTARIO REAL (esta en el alcance) o si la ESCRIBE dentro de una")
    print("constante de cadena (la pone en otros, no la lleva).")
    print("   marca: %s" % MARCA_DEL_REMEDIO)
    print("   la nomina vieja BUSCADORES queda escrita en el fuente como")
    print("   registro de lo que se hacia, y ya no filtra nada.")
    print("")

    bat = nomina_bateria()
    print("A) LA BATERIA, CONTADA DE SU PROPIO FICHERO")
    print("   fuente: scripts/loop/verificar_mutaciones_viejas.py")
    print("   CIFRA mutaciones en la nomina de la bateria: %d" % len(bat))
    print("")

    print("B) LAS TRES LECTURAS DEL PATRON LITERAL")
    resultados = {}
    for nombre, patron in (("A ESTRECHA (dataset/ Y docs/plan/)", ESTRECHA),
                           ("B MEDIA (pathspec que empieza por dataset/)", MEDIA),
                           ("C ANCHA (cualquier git status --porcelain)", ANCHA)):
        f = con_patron(patron)
        resultados[nombre] = f
        en_bat = [x for x in f if x in bat]
        print("   %s" % nombre)
        print("      patron: %s" % patron)
        print("      CIFRA ficheros: %d" % len(f))
        print("      CIFRA de ellos en la bateria de las 23: %d" % len(en_bat))
    print("")

    # EXCLUSION POR CONTENIDO (vuelta 161, TAREA 1.a). Linea vieja TACHADA Y
    # LEGIBLE, no borrada:
    #     ~~principal = resultados["B MEDIA (pathspec que empieza por dataset/)"]~~
    # La lectura B sigue imprimiendose entera arriba como contraste; lo que
    # cambia es quien manda: manda la clasificacion por contenido.
    clases = clasificacion_del_directorio()
    principal = sorted(n for n, (c, _e) in clases.items() if c == "ALCANCE")
    en_bat = [x for x in principal if x in bat]
    fuera_bat = [x for x in principal if x not in bat]
    # ROTULO DE LA SECCION C (vuelta 161, TAREA 1.a). Linea vieja TACHADA Y
    # LEGIBLE, no borrada. Decia "lectura B" cuando la nomina de debajo ya
    # no sale de la lectura B sino de la clasificacion por contenido: la
    # lectura B da 17 y la lista tiene 12.
    #     ~~print("C) LA NOMINA PRINCIPAL (lectura B), UNA A UNA")~~
    print("C) LA NOMINA PRINCIPAL (clase ALCANCE de la seccion E), UNA A UNA")
    for x in principal:
        print("   %-46s %s" % (x, "EN LA BATERIA" if x in bat else "fuera de la bateria"))
    print("")
    # ROTULO DE LA CIFRA DE LA SECCION C (vuelta 161, TAREA 1.a). Linea vieja
    # TACHADA Y LEGIBLE, no borrada. Decia "ficheros con el patron" y contaba
    # la nomina del ALCANCE: chocaba de frente con la seccion E, que publica
    # 17 con ese mismo rotulo. Los que contienen el patron son 17; los del
    # alcance son 12.
    #     ~~print("   CIFRA ficheros con el patron: %d" % len(principal))~~
    print("   CIFRA ficheros en el alcance: %d" % len(principal))
    print("   CIFRA de ellos dentro de la bateria de las 23: %d" % len(en_bat))
    print("   CIFRA de ellos fuera de la bateria: %d" % len(fuera_bat))
    print("")

    print("E) LA CLASIFICACION POR CONTENIDO, FICHERO A FICHERO (vuelta 161)")
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

    print("D) EL COTEJO CONTRA LA CIFRA DEL ACTA 158, ADJUDICACION 6.7")
    print("   (la cifra vigente es la de la adjudicacion 6.1 del ACTA 159,")
    print("    docs/loop/ACTA_AUDITOR.md:52708, que corrige el once del acta 158)")
    print("   CIFRA que el acta declara, ficheros: %d" % ESPERADO_FICHEROS)
    print("   CIFRA que el acta declara, dentro de la bateria: %d" % ESPERADO_EN_BATERIA)
    print("   CIFRA que este computo da, ficheros: %d" % len(principal))
    print("   CIFRA que este computo da, dentro de la bateria: %d" % len(en_bat))
    print("")
    if len(en_bat) == ESPERADO_EN_BATERIA:
        print("   LOS SIETE DE LA BATERIA REPRODUCEN AL DIGITO.")
    if len(principal) != ESPERADO_FICHEROS:
        sobran = len(principal) - ESPERADO_FICHEROS
        print("   LA CIFRA DE FICHEROS NO REPRODUCE: sale %d y el acta dice %d."
              % (len(principal), ESPERADO_FICHEROS))
        candidatos = [x for x in principal if not x.startswith("vuelta1")]
        print("   EL RESIDUO SE PUEDE NOMBRAR, Y ES UNO SOLO: %s" % ", ".join(candidatos))
        print("   Quitandolo, la cuenta da %d, que es exactamente la del acta."
              % (len(principal) - len(candidatos)))
        print("")
        print("   PARADA, POR MANDATO LITERAL DEL ENCARGO (TAREA 5.b): si la cuenta")
        print("   no da once, se para y se dice. NO SE TOCA UN SOLO CHECK. El remedio")
        print("   de la 5.a y el caso positivo de la 5.c NO SE EJECUTAN en esta")
        print("   vuelta, porque su alcance esta en disputa y una guarda que se")
        print("   reescribe con el alcance mal contado es peor que la que se deja.")
        print("FIN")
        return 1

    print("   LA CUENTA REPRODUCE. Se puede aplicar el remedio de la 5.a.")
    print("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
