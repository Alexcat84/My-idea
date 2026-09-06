# -*- coding: utf-8 -*-
r"""dos_convenciones_de_lineas.py . LA PAREJA DE CIFRAS DE LINEAS, Y LA GUARDA
QUE CAE SI UN INSTRUMENTO PUBLICA UNA SOLA POR LA CONVENCION QUE NO CALZA.

NOMBRE ESTABLE Y SIN NUMERO DE VUELTA, como `serie_de_registros.py`,
`aislador_de_ciega.py` y `tallar_cabecera_reporte.py`: lo va a llamar cualquier
vuelta y no se clona.

--- POR QUE NACE (vuelta 191, TAREA 3; hallazgo `5.1` del acta 190) ---

LA CAIDA, CON SU NOMBRE Y SU CIFRA. El reporte de la vuelta 190 publico **"2231
lineas"** de `docs/plan/LECTURAS_DIRIGIDAS.md` donde `wc -l` dice **2230**. **La
cifra no era inventada: la imprimia su instrumento.** Por eso el defecto es del
instrumento y no del que lo leyo, y por eso el remedio va aqui y no en una
advertencia.

LAS DOS CONVENCIONES, DICHAS SIN ADORNO:

  . `len(texto.split(NL))` cuenta los TROZOS que deja el corte. Un fichero que
    termina en salto de linea deja un trozo final VACIO, que **no es una linea**.
    Da UNO DE MAS y **no calza con `wc -l`**.
  . `texto.count(NL)` cuenta los SALTOS. **Calza con `wc -l`**, que es lo que
    cuenta cualquiera que quiera cotejar la cifra desde fuera.
  . `len(texto.splitlines())` tambien calza con `wc -l` cuando el texto termina
    en salto, y **no calza** cuando no termina en salto. Se cuenta aparte y se
    dice, en vez de meterla en el mismo saco.

LA VARA, QUE NO ES NUEVA: ES LA DE LAS DOS CONVENCIONES DE **BYTES** QUE ESTA
CASA YA CONSTRUYO. Una cifra que no se puede cotejar con la herramienta obvia no
sirve de cifra. **O se publica la pareja, o se publica la que calza con `wc -l`
diciendo cual es.** Las dos salidas valen; publicar SOLO la que no calza, no.

QUE OFRECE ESTE FICHERO, Y SON TRES COSAS SEPARADAS:

  1. `lineas(texto)`: la PAREJA `(por_count, por_split)`, PURA.
  2. `frase(texto, ...)`: la frase de la casa, con las dos cifras y con **cual de
     ellas calza con `wc -l` dicho en la propia frase**, PURA.
  3. `veredicto_de_fuente(codigo)` y `censo(directorio)`: LA GUARDA. Miran el
     CODIGO de un instrumento, cuentan sus sitios de conteo por cada convencion y
     devuelven un veredicto. **ROJO significa una cosa sola y comprobable: el
     fichero cuenta lineas por la convencion SPLIT y NO cuenta por ninguna de las
     que calzan.** Ese es el caso que el acta 190 pillo.

LO QUE LA GUARDA NO VE, DICHO PARA QUE NADIE LEA DE MAS. Es un detector de
PATRONES SOBRE EL TEXTO DEL CODIGO, no un analizador del arbol sintactico:

  . NO ve la forma INDIRECTA (`lineas = t.split(NL)` en una linea y `len(lineas)`
    en otra). La cuenta que publica es de la forma DIRECTA, y su alcance va
    escrito en su propia salida.
  . NO decide si la cifra se PUBLICA o solo se usa para iterar; su regla es sobre
    los sitios de CONTEO, que es lo que si se puede contar sin adivinar.
  . Un fichero SIN ningun sitio de conteo sale `NO APLICA` y no cuenta como
    verde: **un cero que sale de una maquina que no muerde no es evidencia.**

SU CASO POSITIVO POR MUTACION: `scripts/loop/vuelta191_tarea3_mutacion_lineas.py`.

USO:
  python scripts/loop/dos_convenciones_de_lineas.py
  python scripts/loop/dos_convenciones_de_lineas.py --directorio scripts/loop
"""
import argparse
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NL = chr(10)

# LOS TRES LITERALES CON QUE ESTA CASA ESCRIBE EL SALTO DE LINEA EN SU CODIGO.
# Van juntos en el patron a proposito: un detector que solo viera `NL` se quedaria
# ciego ante el mismo conteo escrito con `chr(10)`, que es como lo escriben varios
# instrumentos viejos.
_SALTO = r"(?:NL|chr\(10\)|[\"']\\n[\"'])"

# LA CONVENCION QUE **NO** CALZA CON `wc -l`: contar los TROZOS del corte.
PAT_SPLIT = re.compile(r"len\(\s*[^()\n]*?\.split\(\s*" + _SALTO + r"\s*\)\s*\)")
# LA CONVENCION QUE **SI** CALZA: contar los SALTOS.
PAT_COUNT = re.compile(r"\.count\(\s*" + _SALTO + r"\s*\)")
# LA TERCERA, QUE CALZA CUANDO EL TEXTO TERMINA EN SALTO Y NO CUANDO NO.
PAT_SPLITLINES = re.compile(r"len\(\s*[^()\n]*?\.splitlines\(\s*\)\s*\)")
# LA CUARTA, Y ES UNA CORRECCION DECLARADA DE ESTE MISMO DETECTOR EN SU PRIMERA
# CORRIDA (vuelta 191, TAREA 3), SIN BORRAR LO QUE CORRIGE. La primera version
# saco 13 ficheros en ROJO, y al mirarlos uno a uno habia un sitio con `- 1`
# pegado detras: `len(mutado.split(NL)) - 1` es EXACTAMENTE `count(NL)` cuando el
# texto termina en salto, o sea que **si calza**. Marcarlo en rojo era un falso
# positivo, y ese fichero (`vuelta183_tarea1b_mutacion_atribucion.py`) esta
# ADEMAS en la nomina de la bateria, asi que "arreglarlo" habria movido una
# salida sellada que se compara byte a byte. **Se cuenta aparte y CUENTA COMO QUE
# CALZA**, y el sitio corregido NO se cuenta ademas como sitio SPLIT: acusar al
# que ya se corrigio es la misma especie de cifra falsa que este detector caza.
PAT_SPLIT_CORREGIDO = re.compile(
    r"len\(\s*[^()\n]*?\.split\(\s*" + _SALTO + r"\s*\)\s*\)\s*-\s*1\b")

ROJO = "ROJO: cuenta lineas SOLO por la convencion que no calza con wc -l"
VERDE_PAREJA = "VERDE: publica la pareja"
VERDE_CALZA = "VERDE: cuenta solo por una convencion que calza con wc -l"
NO_APLICA = "NO APLICA: no cuenta lineas de ninguna de las tres formas"


def lineas(texto):
    """LA PAREJA `(por_count, por_split)`. PURA.

    `por_count` es `texto.count(NL)` y **es la que calza con `wc -l`**.
    `por_split` es `len(texto.split(NL))` y **es la que da uno de mas** cuando el
    texto termina en salto de linea. Los dos numeros se devuelven siempre: quien
    llame decide cual publica, pero **no puede decir que no tenia el otro**."""
    t = texto.replace(chr(13) + NL, NL)
    return (t.count(NL), len(t.split(NL)))


def frase(texto, nombre=None, pareja=True):
    """LA FRASE DE LA CASA, CON LAS DOS CIFRAS Y CON CUAL CALZA DICHO DENTRO.
    PURA.

    Con `pareja=False` publica SOLO la que calza, **y lo dice**: esa es la otra
    salida que la vara admite. Lo que no admite ninguna de las dos es publicar la
    que no calza a secas."""
    c, s = lineas(texto)
    quien = ("%s: " % nombre) if nombre else ""
    if pareja:
        return ("%s%d lineas por `count(NL)`, que es la que calza con `wc -l`, "
                "y %d por `len(split(NL))`" % (quien, c, s))
    return "%s%d lineas, contadas por `count(NL)`, que es la que calza con `wc -l`" % (
        quien, c)


def sitios_de_conteo(codigo):
    """LOS SITIOS DE CONTEO DE UN FICHERO DE CODIGO, POR CONVENCION. PURA.

    Devuelve `{"split": [(linea, texto)], "count": [...], "splitlines": [...]}`.
    Las lineas de comentario y las de cadena de documentacion NO se excluyen a
    proposito, y se dice por que: un instrumento que trae el patron dentro de su
    propia prosa **tambien lo esta enseñando**, y sacarlo del censo exigiria
    decidir a ojo que es codigo y que no. Lo que se hace en vez de eso es
    publicar el texto de cada sitio, para que se vea de cual se trata."""
    salida = {"split": [], "count": [], "splitlines": [], "split_corregido": []}
    for i, l in enumerate(codigo.replace(chr(13) + NL, NL).split(NL), 1):
        n_corr = len(PAT_SPLIT_CORREGIDO.findall(l))
        n_split = len(PAT_SPLIT.findall(l))
        if n_corr:
            salida["split_corregido"].append((i, l.strip()[:120]))
        # UN SITIO CORREGIDO NO CUENTA ADEMAS COMO SITIO SPLIT: el patron de
        # SPLIT casa DENTRO del de CORREGIDO, y contarlo dos veces seria acusar
        # al que ya se corrigio.
        if n_split > n_corr:
            salida["split"].append((i, l.strip()[:120]))
        for clave, pat in (("count", PAT_COUNT), ("splitlines", PAT_SPLITLINES)):
            if pat.search(l):
                salida[clave].append((i, l.strip()[:120]))
    return salida


def veredicto_de_fuente(codigo):
    """EL VEREDICTO DE UN FICHERO. PURA. Devuelve `(veredicto, sitios)`.

    LA REGLA, ESCRITA ENTERA PARA QUE SE PUEDA MUTAR:
      . tiene sitios SPLIT y NINGUNO de los que calzan  -> ROJO
      . tiene sitios SPLIT y ALGUNO de los que calzan   -> VERDE, publica la pareja
      . no tiene SPLIT pero si alguno de los que calzan -> VERDE, la que calza
      . no tiene ninguno                                -> NO APLICA

    **NO APLICA NO ES VERDE**, y esa distincion es la mitad de la guarda: un
    fichero que no cuenta lineas no ha aprobado nada."""
    s = sitios_de_conteo(codigo)
    calzan = len(s["count"]) + len(s["splitlines"]) + len(s["split_corregido"])
    if s["split"] and not calzan:
        return ROJO, s
    if s["split"] and calzan:
        return VERDE_PAREJA, s
    if calzan:
        return VERDE_CALZA, s
    return NO_APLICA, s


def censo(directorio):
    """EL CENSO DE UN DIRECTORIO, FICHERO A FICHERO. Devuelve
    `[(nombre, veredicto, sitios)]`, ordenado por nombre."""
    salida = []
    for nombre in sorted(os.listdir(directorio)):
        if not nombre.endswith(".py"):
            continue
        ruta = os.path.join(directorio, nombre)
        if not os.path.isfile(ruta):
            continue
        codigo = io.open(ruta, encoding="utf-8", errors="replace").read()
        v, s = veredicto_de_fuente(codigo)
        salida.append((nombre, v, s))
    return salida


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--directorio", default="scripts/loop")
    ap.add_argument("--salida", default=None)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    d = os.path.join(RAIZ, a.directorio.replace("/", os.sep))
    L = []
    w = L.append
    w("=" * 78)
    w("LAS DOS CONVENCIONES DE `lineas`, CENSADAS EN %s" % a.directorio)
    w("=" * 78)
    w("")
    w("LA VARA, ESCRITA ANTES DE CONTAR NADA:")
    w("   `len(texto.split(NL))` cuenta TROZOS y da UNO DE MAS cuando el texto")
    w("   termina en salto. NO calza con `wc -l`.")
    w("   `texto.count(NL)` cuenta SALTOS y SI calza con `wc -l`.")
    w("   `len(texto.splitlines())` calza cuando el texto termina en salto.")
    w("   `len(texto.split(NL)) - 1` es la SPLIT YA CORREGIDA y SI calza: se")
    w("   cuenta aparte y NO se acusa. Es una correccion declarada de este mismo")
    w("   detector en su primera corrida de la vuelta 191, y no se tapa lo que")
    w("   corrige: la primera version saco 13 en ROJO y uno era falso positivo.")
    w("   ROJO es una cosa sola: contar por SPLIT y por ninguna de las que calzan.")
    w("")
    w("LO QUE ESTE DETECTOR NO VE, DICHO ANTES DE PUBLICAR SU CIFRA:")
    w("   no ve la forma INDIRECTA (`x = t.split(NL)` y `len(x)` en otra linea),")
    w("   no decide si la cifra se publica o solo se itera, y no separa el codigo")
    w("   de la prosa. Su cuenta es de SITIOS DE CONTEO DIRECTOS.")
    w("")

    filas = censo(d)
    por_veredicto = {}
    for nombre, v, s in filas:
        por_veredicto.setdefault(v, []).append((nombre, s))

    w("A) EL REPARTO, CONTADO")
    w("   CIFRA ficheros .py mirados: %d" % len(filas))
    for v in (ROJO, VERDE_PAREJA, VERDE_CALZA, NO_APLICA):
        w("   %-64s %d" % (v, len(por_veredicto.get(v, []))))
    w("")

    w("B) LOS FICHEROS EN ROJO, NOMBRADOS UNO A UNO CON SUS SITIOS")
    rojos = por_veredicto.get(ROJO, [])
    if not rojos:
        w("   (ninguno)")
    for nombre, s in rojos:
        w("   %s -> %d sitio(s) SPLIT, 0 que calcen" % (nombre, len(s["split"])))
        for i, t in s["split"]:
            w("      LINEA %-5d %s" % (i, t))
    w("   CIFRA ficheros en ROJO: %d" % len(rojos))
    w("")

    w("C) LOS QUE PUBLICAN LA PAREJA, NOMBRADOS")
    pareja = por_veredicto.get(VERDE_PAREJA, [])
    for nombre, s in pareja:
        w("   %-56s SPLIT %d | COUNT %d | SPLITLINES %d"
          % (nombre, len(s["split"]), len(s["count"]), len(s["splitlines"])))
    w("   CIFRA: %d" % len(pareja))
    w("")

    w("D) LOS QUE CUENTAN SOLO POR UNA CONVENCION QUE CALZA, NOMBRADOS")
    calza = por_veredicto.get(VERDE_CALZA, [])
    for nombre, s in calza:
        w("   %-56s COUNT %d | SPLITLINES %d"
          % (nombre, len(s["count"]), len(s["splitlines"])))
    w("   CIFRA: %d" % len(calza))
    w("")

    w("E) LOS QUE NO CUENTAN LINEAS DE NINGUNA FORMA")
    w("   CIFRA: %d (no se nombran uno a uno: no aportan a la decision, y"
      % len(por_veredicto.get(NO_APLICA, [])))
    w("   NO APLICA no es VERDE)")
    w("")

    w("F) LAS CIFRAS TOTALES DE SITIOS, QUE ES EL TAMANO DEL ASUNTO")
    tot = {"split": 0, "count": 0, "splitlines": 0, "split_corregido": 0}
    for _n, _v, s in filas:
        for k in tot:
            tot[k] += len(s[k])
    for k in ("split", "count", "splitlines", "split_corregido"):
        w("   CIFRA sitios %-11s %d" % (k, tot[k]))
    w("")
    w("VEREDICTO DEL CENSO: %s" % ("ROJO, %d fichero(s)" % len(rojos)
                                   if rojos else "VERDE, ninguno en rojo"))

    texto = NL.join(L) + NL
    if a.salida:
        io.open(os.path.join(RAIZ, a.salida.replace("/", os.sep)), "w",
                encoding="utf-8", newline=NL).write(texto)
        print(texto)
        print("ESCRITO: %s (%d bytes)" % (a.salida, len(texto.encode("utf-8"))))
    else:
        print(texto)
    return 1 if rojos else 0


if __name__ == "__main__":
    sys.exit(main())
