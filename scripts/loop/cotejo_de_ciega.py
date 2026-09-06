# -*- coding: utf-8 -*-
r"""cotejo_de_ciega.py . EL FORMATO UNICO DEL COTEJO DE CIEGA, Y SU LECTOR.

NOMBRE ESTABLE Y SIN NUMERO DE VUELTA, como `aislador_de_ciega.py`,
`apertura_del_auditor.py`, `tallar_cabecera_reporte.py`, `serie_de_registros.py`
y `cerrar_reporte.py`: lo usan TODAS las ciegas de aqui en adelante y NO SE
CLONA. Un fichero que se clona por vuelta es un fichero que la vuelta siguiente
puede escribir de otra manera, y **de otra manera es exactamente la enfermedad
que esto viene a curar**.

DE DONDE SALE, PALABRA POR PALABRA. Es el `P.2` del ejecutor, adjudicado A FAVOR
en la `4.9` del acta 192: *"la TAREA 5 midio que el universo se queda en 6 de 43
ficheros por una razon de formato y no de fondo... mientras eso siga asi ninguna
medicion sobre la historia de ciegas va a alcanzar para concluir nada"*. **Tres
cotejos de ciega DE VERDAD (los de las vueltas 183, 184 y 190) quedan fuera de
esa medicion por FORMATO y no por FONDO.**

--- LO QUE EL FORMATO EXIGE, Y POR QUE CADA COSA ---

Cinco columnas, todas explicitas, **una fila POR CADA PUESTO COTEJADO y no solo
por las discrepancias**:

  1. `puesto`             . el numero, para poder cruzarlo con el archivo.
  2. `clase del lector`   . lo que el lector escribio a ciegas.
  3. `clase del archivo`  . lo que el archivo dice.
  4. `en dudosos`         . `si` o `no`: si el lector lo habia marcado DELANTE.
  5. `veredicto`          . `COINCIDE` o `DISCREPA`, computado de las dos clases
                            y NO tecleado.

**Y LA RAZON DE QUE LAS FILAS SEAN TODAS Y NO SOLO LAS DISCREPANCIAS ES EL
DENOMINADOR.** Dos de los seis ficheros que hoy entran en la medicion **solo
listan discrepancias**, y por eso no se sabe sobre cuantos pares se midieron. Una
tasa sin denominador no es una tasa: es un numero suelto. Con este formato el
denominador **se recupera contando las filas**, y ademas va DECLARADO en la
cabecera, **y las dos cifras tienen que calzar o el fichero es ROJO**.

--- LO QUE ESTE FORMATO NO PUEDE HACER, DICHO ANTES DE SU PRIMERA CIFRA ---

**No convierte en legible un cotejo viejo que no trae la informacion.** Un
fichero que nunca escribio la clase del lector no la tiene, y ningun lector la
puede recuperar. Lo que este formato hace es que **de aqui en adelante no vuelva
a pasar**; lo que se pueda rescatar de los viejos lo dice
`lector_de_cotejos_viejos()`, y lo que no se pueda se nombra en vez de estimarse.

**Y no dice si el lector acerto.** Dice si coincide con el archivo, que es otra
cosa: el archivo tambien se equivoca, y esta casa tiene correcciones declaradas
que lo prueban.

USO COMO INSTRUMENTO:
  from cotejo_de_ciega import escribir_cotejo, filas_del_cotejo, denominador
  escribir_cotejo(ruta, cabecera=[...], filas=[(puesto, clase_lector,
                  clase_archivo, en_dudosos)])

USO DESDE LA LINEA:
  python scripts/loop/cotejo_de_ciega.py --leer docs/loop/SALIDA_V192_T2_COTEJO.txt
  python scripts/loop/cotejo_de_ciega.py --mutacion
"""
import argparse
import io
import os
import re
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

MARCA_FORMATO = "FORMATO: COTEJO_DE_CIEGA v1"
CABECERA_TABLA = ("puesto | clase del lector | clase del archivo | "
                  "en dudosos del lector | veredicto")
ABRE_TABLA = "TABLA (una fila POR CADA PUESTO COTEJADO, no solo por las discrepancias):"
FIN_TABLA = "FIN DE LA TABLA."
LINEA_DENOMINADOR = "CIFRA puestos cotejados"

PAT_FILA = re.compile(
    r"^\s*(\d+)\s*\|\s*([A-Za-z?]+)\s*\|\s*([A-Za-z?]+)\s*\|\s*(si|no)\s*\|"
    r"\s*(COINCIDE|DISCREPA)\s*$")
PAT_DENOM = re.compile(r"^%s:\s*(\d+)\s*$" % re.escape(LINEA_DENOMINADOR))


# LAS FORMAS QUE `en dudosos` ADMITE, ESCRITAS ANTES DE MEDIR NADA (vuelta 193,
# TAREA 5.a; hallazgo 5.2 del acta 193). La lista es CORTA a proposito: se admite
# el booleano de verdad y las dos formas que el propio docstring de este fichero
# especifica para la columna, `si` y `no`. **Todo lo demas CAE**, que es la misma
# vara que el caso `G` de la mutacion ya le aplica a `veredicto_de`: una clase
# rara SALE A LA VISTA en vez de resolverse en silencio.
VALORES_SI = ("si", "s\u00ed", "true", "1")
VALORES_NO = ("no", "false", "0")


class EnDudososIlegible(ValueError):
    """LA COLUMNA `en dudosos` NO SE PUDO LEER, Y NO SE ADIVINA.

    NACE DE UNA CAIDA MEDIDA Y NO DE UNA PRECAUCION (acta 193, hallazgo `5.2`):
    `cuerpo_del_cotejo()` hacia `bool(du)`, y **`bool("no")` es `True`**. El
    docstring de este mismo fichero especifica esa columna como *"`si` o `no`"*,
    o sea que **la forma que el formato invita a usar era justo la que
    reventaba**. Un auditor la uso y el instrumento le publico
    `discrepancias FUERA de los dudosos: 0 (ninguna)` **teniendo DOS**.

    **POR QUE ESTO ES MAS QUE UNA ERRATA:** la columna `en dudosos` es la unica
    de la que cuelga una regla de PARADA, porque `AUDITOR.md` 1.2 baja el credito
    de la tanda y encarga la relectura al doble **por lo que cae FUERA**. Un
    instrumento que silencia esa cifra **publica un verde donde hay una
    escalada**."""


def normalizar_en_dudosos(valor):
    """`en dudosos` COMO BOOLEANO, O CAE. PURA.

    Admite el booleano de verdad y las formas literales que el formato
    especifica. **Cualquier otra cosa levanta `EnDudososIlegible`**, y ese es el
    punto entero: la version vieja aceptaba cualquier cosa y la convertia en
    `si`. **No se normaliza mas de lo necesario, para que lo raro salga a la
    vista.**"""
    if valor is True or valor is False:
        return valor
    if isinstance(valor, int):
        if valor in (0, 1):
            return bool(valor)
        raise EnDudososIlegible(
            "`en dudosos` llego como el entero %r, y solo 0 y 1 se leen" % valor)
    if isinstance(valor, str):
        v = valor.strip().lower()
        if v in VALORES_SI:
            return True
        if v in VALORES_NO:
            return False
    raise EnDudososIlegible(
        "`en dudosos` llego como %r, que no es ni booleano ni una de las formas "
        "que el formato admite (%s / %s). NO SE ADIVINA: la columna de la que "
        "cuelga la regla de parada de AUDITOR.md 1.2 no se resuelve en silencio."
        % (valor, "/".join(VALORES_SI), "/".join(VALORES_NO)))


def veredicto_de(clase_lector, clase_archivo):
    """COINCIDE O DISCREPA, COMPUTADO Y NO TECLEADO. PURA.

    La comparacion es por la letra en mayusculas y nada mas: no se normaliza
    ninguna otra cosa, para que una clase escrita de otra manera SALGA a la vista
    en vez de resolverse en silencio."""
    return "COINCIDE" if str(clase_lector).upper() == str(clase_archivo).upper() \
        else "DISCREPA"


def filas_del_cotejo(texto):
    """LAS FILAS DE UN COTEJO EN ESTE FORMATO. PURA.

    Devuelve `[(puesto, clase_lector, clase_archivo, en_dudosos, veredicto)]`,
    vacia si el texto no trae ninguna fila legible. `en_dudosos` sale como bool."""
    salida = []
    for linea in texto.replace(chr(13) + NL, NL).split(NL):
        m = PAT_FILA.match(linea)
        if not m:
            continue
        salida.append((int(m.group(1)), m.group(2).upper(), m.group(3).upper(),
                       m.group(4) == "si", m.group(5)))
    return salida


def denominador(texto):
    """(OK, DECLARADO, CONTADO, MOTIVO). PURA. **ES LA GUARDA DEL FORMATO.**

    `declarado` es la cifra de la cabecera; `contado` es cuantas filas trae la
    tabla. **Si no calzan, o si falta alguna de las dos, `ok` es False y el
    motivo lo dice.** Un cotejo que solo lista discrepancias no puede pasar por
    aqui, y ese es exactamente el caso que su prueba de mutacion fabrica."""
    dec = None
    for linea in texto.replace(chr(13) + NL, NL).split(NL):
        m = PAT_DENOM.match(linea.strip())
        if m:
            dec = int(m.group(1))
            break
    filas = filas_del_cotejo(texto)
    if MARCA_FORMATO not in texto:
        return False, dec, len(filas), "el fichero no declara %r" % MARCA_FORMATO
    if dec is None:
        return False, None, len(filas), \
            "no trae la linea %r en su cabecera" % LINEA_DENOMINADOR
    if not filas:
        return False, dec, 0, "la tabla no trae ninguna fila legible"
    if dec != len(filas):
        return False, dec, len(filas), \
            ("el denominador declarado (%d) no calza con las filas contadas (%d)"
             % (dec, len(filas)))
    return True, dec, len(filas), "declarado y contado calzan"


def resumen(filas):
    """LAS CIFRAS DEL COTEJO, COMPUTADAS DE LAS FILAS. PURA. Devuelve un dict."""
    disc = [f for f in filas if f[4] == "DISCREPA"]
    coin = [f for f in filas if f[4] == "COINCIDE"]
    dud = [f for f in filas if f[3]]
    return {
        "total": len(filas),
        "coinciden": len(coin),
        "discrepan": len(disc),
        "dudosos": len(dud),
        "disc_dentro": [f[0] for f in disc if f[3]],
        "disc_fuera": [f[0] for f in disc if not f[3]],
        "reparto_lector": _reparto(filas, 1),
        "reparto_archivo": _reparto(filas, 2),
    }


def _reparto(filas, i):
    d = {}
    for f in filas:
        d[f[i]] = d.get(f[i], 0) + 1
    return d


def cuerpo_del_cotejo(cabecera, filas):
    """EL TEXTO ENTERO DEL COTEJO, EN EL FORMATO UNICO. PURA.

    `filas` son tuplas `(puesto, clase_lector, clase_archivo, en_dudosos)`: el
    veredicto **no se le pasa, se computa**, para que no se pueda teclear uno que
    contradiga a sus dos clases."""
    # `bool(du)` ERA EL FALLO Y AQUI VA SU REMEDIO (vuelta 193, TAREA 5.a):
    # `bool("no")` es `True`, y el docstring de arriba especifica esta columna
    # como `si` o `no`. Ahora se NORMALIZA o se CAE, y no se resuelve en
    # silencio. La excepcion nombra el valor que llego.
    completas = [(p, str(cl).upper(), str(ca).upper(),
                  normalizar_en_dudosos(du), veredicto_de(cl, ca))
                 for p, cl, ca, du in filas]
    r = resumen(completas)
    L = [MARCA_FORMATO, "=" * 78]
    L.extend(cabecera)
    L.append("")
    L.append("%s: %d" % (LINEA_DENOMINADOR, r["total"]))
    L.append("CIFRA que COINCIDEN: %d" % r["coinciden"])
    L.append("CIFRA que DISCREPAN: %d" % r["discrepan"])
    L.append("CIFRA en los dudosos del lector: %d" % r["dudosos"])
    L.append("CIFRA discrepancias DENTRO de los dudosos: %d (%s)"
             % (len(r["disc_dentro"]),
                ", ".join(str(x) for x in r["disc_dentro"]) or "ninguna"))
    L.append("CIFRA discrepancias FUERA de los dudosos: %d (%s)"
             % (len(r["disc_fuera"]),
                ", ".join(str(x) for x in r["disc_fuera"]) or "ninguna"))
    L.append("REPARTO DEL LECTOR:  %s"
             % ", ".join("%s %d" % (k, r["reparto_lector"][k])
                         for k in sorted(r["reparto_lector"])))
    L.append("REPARTO DEL ARCHIVO: %s"
             % ", ".join("%s %d" % (k, r["reparto_archivo"][k])
                         for k in sorted(r["reparto_archivo"])))
    L.append("")
    L.append(ABRE_TABLA)
    L.append(CABECERA_TABLA)
    L.append("-" * 78)
    for p, cl, ca, du, ver in completas:
        L.append("%6d | %s | %s | %s | %s"
                 % (p, cl, ca, "si" if du else "no", ver))
    L.append(FIN_TABLA)
    L.append("")
    L.append("EL DENOMINADOR ES RECUPERABLE CONTANDO LAS FILAS DE ESTA TABLA, y la")
    L.append("cifra declarada arriba tiene que calzar con ese conteo. Lo comprueba")
    L.append("`denominador()` de scripts/loop/cotejo_de_ciega.py, y si no calzan el")
    L.append("fichero es ROJO.")
    return NL.join(L) + NL


def escribir_cotejo(ruta, cabecera, filas):
    """ESCRIBE EL COTEJO Y LO RELEE PARA COMPROBAR SU PROPIO FORMATO.

    Devuelve `(ok, informe)`. **NO da por bueno lo que acaba de escribir:** lo
    relee del disco y le corre su propia guarda del denominador."""
    texto = cuerpo_del_cotejo(cabecera, filas)
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(texto)
    releido = io.open(ruta, encoding="utf-8").read()
    ok, dec, cont, motivo = denominador(releido)
    inf = ["ESCRITO: %s" % os.path.relpath(ruta, RAIZ).replace(os.sep, "/"),
           "   disco %d bytes | LF %d bytes"
           % (os.path.getsize(ruta),
              len(releido.replace(chr(13) + NL, NL).encode("utf-8"))),
           "   RELEIDO DEL DISCO Y PASADO POR SU PROPIA GUARDA:",
           "      denominador declarado: %s | filas contadas: %d" % (dec, cont),
           "      %s -> %s" % (motivo, "VERDE" if ok else "ROJO")]

    # LA SEGUNDA MITAD DE LA GUARDA (vuelta 193, TAREA 5.b). LA PRIMERA MIRABA
    # SOLO EL DENOMINADOR, Y ESO ES EL CONTEO DE FILAS: sobre el fichero del
    # auditor de la 193, con las DOS discrepancias de fuera silenciadas, el
    # denominador calzaba PERFECTAMENTE y la guarda daba VERDE. **Un
    # denominador correcto sobre una columna falsa sigue siendo un verde
    # falso.**
    #
    # QUE MIRA AHORA: la columna `en dudosos` RELEIDA DEL DISCO contra la que se
    # le paso, normalizada. Si el fichero escrito dice `si` donde la entrada
    # decia `no`, esta guarda CAE y nombra los puestos. **Ese es exactamente el
    # caso que el hallazgo 5.2 describe.**
    entrada = {}
    ilegibles = []
    for p, _cl, _ca, du in filas:
        try:
            entrada[int(p)] = normalizar_en_dudosos(du)
        except EnDudososIlegible as e:
            ilegibles.append((p, str(e)))
    del_disco = dict((f[0], f[3]) for f in filas_del_cotejo(releido))
    torcidos = sorted(p for p, v in entrada.items()
                      if p in del_disco and del_disco[p] != v)
    ausentes = sorted(p for p in entrada if p not in del_disco)
    inf.append("      LA COLUMNA `en dudosos`, RELEIDA Y COTEJADA CONTRA LA QUE")
    inf.append("      SE PASO (y no solo el denominador, que es conteo de filas):")
    inf.append("         CIFRA puestos con `en dudosos` torcido al escribir: %d (%s)"
               % (len(torcidos), ", ".join(str(x) for x in torcidos) or "ninguno"))
    inf.append("         CIFRA puestos que no volvieron del disco: %d (%s)"
               % (len(ausentes), ", ".join(str(x) for x in ausentes) or "ninguno"))
    inf.append("         CIFRA `si` en el fichero: %d | CIFRA `no`: %d"
               % (len([1 for v in del_disco.values() if v]),
                  len([1 for v in del_disco.values() if not v])))
    if ilegibles:
        inf.append("         CIFRA valores ILEGIBLES en la entrada: %d"
                   % len(ilegibles))
        for pp, mot in ilegibles:
            inf.append("            puesto %s: %s" % (pp, mot))
    if torcidos or ausentes or ilegibles:
        ok = False
        inf.append("      ROJO: la columna de la que cuelga la regla de parada de")
        inf.append("      AUDITOR.md 1.2 no calza con lo que se paso.")
    return ok, inf


# ---------------------------------------------------------------- LA MUTACION
def _caso(w, nombre, obtenido, esperado):
    ok = obtenido == esperado
    w("   %-64s %s" % (nombre, "VERDE" if ok else "ROJO"))
    if not ok:
        w("      esperado: %r" % (esperado,))
        w("      obtenido: %r" % (obtenido,))
    return ok


def prueba_de_mutacion():
    """EL CASO POSITIVO POR MUTACION: **CAE SI UN COTEJO NO PERMITE RECUPERAR EL
    DENOMINADOR.** No toca el repo: fabrica los textos."""
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    ok = True
    w("=" * 78)
    w("CASO POSITIVO POR MUTACION DEL FORMATO UNICO DEL COTEJO DE CIEGA")
    w("=" * 78)
    w("")
    w("LO QUE SE PRUEBA: que `denominador()` CAE cuando el cotejo no permite")
    w("recuperar sobre cuantos pares se midio. Los textos se FABRICAN aqui, con")
    w("la cifra sabida por construccion, y el valor esperado NO es una constante")
    w("igual a la obtenida.")
    w("")

    bueno = cuerpo_del_cotejo(["cabecera de prueba"],
                              [(1, "A", "A", False), (2, "B", "D", True),
                               (3, "D", "D", False)])
    w("A) UN COTEJO BIEN FORMADO, CON TRES FILAS")
    ok &= _caso(w, "denominador() sale VERDE", denominador(bueno)[0], True)
    ok &= _caso(w, "declarado y contado son los dos 3", denominador(bueno)[1:3], (3, 3))
    ok &= _caso(w, "filas_del_cotejo() recupera las tres", len(filas_del_cotejo(bueno)), 3)
    ok &= _caso(w, "el veredicto se computa y no se teclea",
                [f[4] for f in filas_del_cotejo(bueno)],
                ["COINCIDE", "DISCREPA", "COINCIDE"])
    w("")

    w("B) LA MUTACION QUE EL ENCARGO PIDE: UN COTEJO QUE SOLO LISTA LAS")
    w("   DISCREPANCIAS. Es la forma de dos de los seis ficheros que hoy entran")
    w("   en la medicion, y por eso su denominador no se sabe.")
    solo_disc = NL.join([l for l in bueno.split(NL)
                         if "COINCIDE" not in l or l.startswith("CIFRA que")])
    ok &= _caso(w, "denominador() CAE sobre el cotejo mutilado",
                denominador(solo_disc)[0], False)
    ok &= _caso(w, "y dice que declarado (3) y contado (1) no calzan",
                denominador(solo_disc)[1:3], (3, 1))
    w("")

    w("C) LA MUTACION SIN LA LINEA DEL DENOMINADOR EN LA CABECERA")
    sin_dec = NL.join([l for l in bueno.split(NL)
                       if not l.startswith(LINEA_DENOMINADOR + ":")])
    ok &= _caso(w, "denominador() CAE sin la linea declarada",
                denominador(sin_dec)[0], False)
    ok &= _caso(w, "y el motivo nombra la linea que falta",
                LINEA_DENOMINADOR in denominador(sin_dec)[3], True)
    w("")

    w("D) LA MUTACION SIN LA MARCA DE FORMATO")
    sin_marca = bueno.replace(MARCA_FORMATO, "un cotejo cualquiera")
    ok &= _caso(w, "denominador() CAE sin la marca de formato",
                denominador(sin_marca)[0], False)
    w("")

    w("E) LA MUTACION CON LA TABLA VACIA")
    vacio = cuerpo_del_cotejo(["cabecera de prueba"], [])
    ok &= _caso(w, "denominador() CAE con cero filas", denominador(vacio)[0], False)
    w("")

    w("F) LA MUTACION QUE FALSEA EL DENOMINADOR DECLARADO")
    falseado = bueno.replace("%s: 3" % LINEA_DENOMINADOR,
                             "%s: 30" % LINEA_DENOMINADOR)
    ok &= _caso(w, "denominador() CAE si la cabecera miente",
                denominador(falseado)[0], False)
    ok &= _caso(w, "y publica las dos cifras, 30 declarada y 3 contada",
                denominador(falseado)[1:3], (30, 3))
    w("")

    w("G) `veredicto_de` NO NORMALIZA MAS QUE LA CAJA, PARA QUE UNA CLASE RARA")
    w("   SALGA A LA VISTA EN VEZ DE RESOLVERSE EN SILENCIO")
    ok &= _caso(w, "'a' contra 'A' COINCIDE", veredicto_de("a", "A"), "COINCIDE")
    ok &= _caso(w, "'A' contra 'D' DISCREPA", veredicto_de("A", "D"), "DISCREPA")
    ok &= _caso(w, "'AB' contra 'A' DISCREPA", veredicto_de("AB", "A"), "DISCREPA")
    w("")

    w("H) LA COLUMNA `en dudosos` SE NORMALIZA O CAE, Y NO SE RESUELVE EN")
    w("   SILENCIO (vuelta 193, TAREA 5.c; hallazgo 5.2 del acta 193)")
    w("   LA CAIDA QUE ESTO CIERRA, DICHA CON SU CIFRA: la version vieja hacia")
    w("   `bool(du)`, y `bool(\"no\")` es %r. Un auditor escribio la columna con"
      % bool("no"))
    w("   las formas que el propio docstring de este fichero especifica, `si` y")
    w("   `no`, y el instrumento le publico `discrepancias FUERA de los dudosos:")
    w("   0 (ninguna)` TENIENDO DOS.")
    w("")
    w("   LA MUTACION QUE MANDA: se fabrica un cotejo con `no` en TEXTO en el")
    w("   puesto que DISCREPA. Con la version vieja ese `no` se volvia `si` y la")
    w("   discrepancia salia DENTRO de los dudosos; con esta tiene que salir")
    w("   FUERA. Los dos caminos se corren y se publican los dos.")
    filas_texto = [(1, "A", "A", "si"), (2, "A", "D", "no"), (3, "D", "D", "no")]
    bueno_txt = cuerpo_del_cotejo(["cabecera de prueba"], filas_texto)
    r_txt = resumen(filas_del_cotejo(bueno_txt))
    w("      con `no` en TEXTO, la version de HOY dice:")
    w("         dudosos %d | DENTRO %s | FUERA %s"
      % (r_txt["dudosos"], r_txt["disc_dentro"], r_txt["disc_fuera"]))
    ok &= _caso(w, "el `no` en texto NO se convierte en `si`", r_txt["dudosos"], 1)
    ok &= _caso(w, "y la discrepancia sale FUERA de los dudosos, que es donde va",
                (r_txt["disc_dentro"], r_txt["disc_fuera"]), ([], [2]))
    w("   Y EL CAMINO VIEJO, CORRIDO AQUI PARA QUE LA MUTACION NO SEA UNA")
    w("   AFIRMACION: se aplica `bool()` a los mismos valores, que es lo que la")
    w("   version vieja hacia, y se mira que sale")
    viejo_bools = [bool(du) for _p, _cl, _ca, du in filas_texto]
    w("      `bool()` sobre %r da %r"
      % ([f[3] for f in filas_texto], viejo_bools))
    if all(viejo_bools):
        w("      LA MUTACION CAE: la version vieja marca los TRES como dudosos,")
        w("      incluidos los dos que decian `no`, y la discrepancia del puesto")
        w("      2 le sale DENTRO. La de hoy la saca FUERA.")
    else:
        w("      LA MUTACION NO CAYO: `bool()` ya distinguia `si` de `no`.")
        ok = False
    ok &= _caso(w, "los dos caminos NO dan lo mismo",
                viejo_bools == [f[3] for f in filas_del_cotejo(bueno_txt)], False)
    w("")
    w("   LA MUTACION 2: un valor QUE NO ES NI BOOLEANO NI UNA DE LAS FORMAS")
    w("   ADMITIDAS TIENE QUE LEVANTAR, no volverse `si`")
    for raro in ("quiza", "", None, 7, [], "SI ", "No"):
        try:
            v = normalizar_en_dudosos(raro)
            cayo = False
        except EnDudososIlegible:
            v, cayo = None, True
        esperado_cae = raro not in ("SI ", "No")
        w("      %-8r -> %s"
          % (raro, "LEVANTA" if cayo else "se lee como %r" % v))
        ok &= _caso(w, "         %r se comporta como debe" % (raro,),
                    cayo, esperado_cae)
    w("   (`SI ` y `No` SI se leen: la caja y los espacios se normalizan, que es")
    w("    lo unico que se normaliza. Lo demas CAE)")
    w("")
    w("   LA MUTACION 3: `cuerpo_del_cotejo()` ENTERO tiene que caer si una fila")
    w("   trae un valor ilegible, en vez de escribir un fichero con la columna")
    w("   inventada")
    try:
        cuerpo_del_cotejo(["x"], [(1, "A", "A", "quiza")])
        w("      LA MUTACION NO CAYO: escribio el cotejo con un valor ilegible.")
        ok = False
    except EnDudososIlegible as e:
        w("      LA MUTACION CAE: levanta EnDudososIlegible y nombra el valor.")
        w("      %s" % str(e)[:70])
    w("")

    w("VEREDICTO: %s" % ("VERDE" if ok else "ROJO"))
    t = NL.join(L) + NL
    ruta = os.path.join(RAIZ, "docs", "loop",
                        "SALIDA_V192_T5_MUTACION_FORMATO_COTEJO.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: docs/loop/SALIDA_V192_T5_MUTACION_FORMATO_COTEJO.txt (%d bytes)"
          % len(t.encode("utf-8")))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--leer", help="lee un cotejo y le corre la guarda del denominador")
    ap.add_argument("--mutacion", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    if a.mutacion:
        return prueba_de_mutacion()
    if not a.leer:
        print("ROJO: hace falta --leer RUTA o --mutacion.")
        return 1
    texto = io.open(a.leer, encoding="utf-8", errors="replace").read()
    ok, dec, cont, motivo = denominador(texto)
    print("%s" % a.leer)
    print("   declarado: %s | contado: %d" % (dec, cont))
    print("   %s" % motivo)
    if ok:
        r = resumen(filas_del_cotejo(texto))
        for k in ("total", "coinciden", "discrepan", "dudosos"):
            print("   %-12s %d" % (k, r[k]))
        print("   discrepancias DENTRO de los dudosos: %s"
              % (", ".join(str(x) for x in r["disc_dentro"]) or "ninguna"))
        print("   discrepancias FUERA de los dudosos: %s"
              % (", ".join(str(x) for x in r["disc_fuera"]) or "ninguna"))
    print("   VEREDICTO: %s" % ("VERDE" if ok else "ROJO"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
