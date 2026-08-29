# -*- coding: utf-8 -*-
"""verificar_citas_del_reporte.py . GUARDA: cada afirmacion del vocabulario
cerrado del reporte tiene que cuadrar con el fichero que cita al lado.

Nace en la vuelta 122 (encargo, TAREA 1.e), remedio del tramo doblado de
reporte (acta de la vuelta 121, seccion 5, ramales (i) y (ii)): una frase del
reporte no puede decir mas, ni distinto, de lo que su propio fichero citado
dice. El ejemplar que la motiva: la TAREA 3.a de la vuelta 121 escribio "git
status --porcelain vacio tras el rojo" citando (abreviado en la prosa)
`SALIDA_V121_OPS03_ROJO_SEGUNDA_PASADA.txt`, cuando ese fichero, leido, trae
tres lineas " M dataset/...json" al final: no esta vacio.

CONTRATO (exacto, tal como corre desde la vuelta 123, encargo 1.e, acta de la
vuelta 122 seccion 4.6):
  - Lee docs/loop/REPORTE.md y parte el texto en frases. Cada LINEA de tabla
    markdown ("| ... |") es su propia frase atomica; el resto es prosa,
    partida por punto seguido de espacio o salto de linea (sin partir un
    punto de miles como "3.853").
  - Busca los pares (afirmacion, fichero citado) sobre un vocabulario CERRADO
    y corto: "25/25", "vacio", "GATE 0 OK" o "Gate 0 verde", "EXIT 0",
    "EXIT 1", "ROJO", "IDENTICA AL TALLADOR". El vocabulario se busca fuera
    de los nombres de fichero citados (un fichero puede traer "ROJO" en su
    propio nombre).
  - LA CITA: si la frase (fila de tabla o prosa) trae su PROPIA cita de
    fichero, se coteja con esa. Si es PROSA y no trae cita propia, mira la
    cita de la frase anterior (lookback de prosa, sin cambios desde la 122).
    Si es FILA DE TABLA y no trae cita propia, NO coteja y NO es rojo (no
    mira a la frase anterior): una tabla puede tener celdas de dato sin cita
    propia porque la cita vive una sola vez, en el parrafo que abre la
    tabla, y forzar el lookback ahi fue el punto ciego que la 122 tapo
    recortando el vocabulario entero de las filas (acta 122, 4.6). Desde la
    123, una fila CON cita propia SI se coteja como cualquier frase.
  - Si una afirmacion en prosa no tiene cita propia ni previa: ROJO
    (sin fichero citado).
  - Para cada par con cita, abre el fichero citado y comprueba:
      "25/25"              -> el fichero contiene "TODOS LOS TESTS PASARON (25/25)"
      "vacio"               -> el fichero NO tiene ninguna linea que empiece
                               por espacio y una letra de estado de git
                               (M, A, D, R) seguida de espacio
      "Gate 0 verde"/"GATE 0 OK" -> el fichero contiene "GATE 0: OK"
      "EXIT 0"              -> el fichero NO contiene "EXIT:1" ni "EXITCODE: 1"
      "EXIT 1" / "ROJO"     -> el fichero SI contiene "EXIT:1" o "EXITCODE: 1"
      "IDENTICA AL TALLADOR" -> el fichero contiene esa cadena literal
  - Si un par no cuadra: ROJO EXIT 1, con la frase, el fichero y la linea.
  - Si el reporte cita un fichero que no existe: ROJO.
  - Si cuadran todos: VERDE EXIT 0 con el recuento de pares cotejados.

La guarda NO interpreta ni corrige nada: solo lee el fichero citado y compara
contra lo que la frase afirma, con el vocabulario cerrado de arriba y nada
mas. Un par fuera de ese vocabulario no se coteja: no es su contrato. Una
fila de tabla SIN cita propia tampoco se coteja: por diseno, no por recorte
silencioso (la exclusion esta escrita aqui, en el REPORTE de la vuelta que la
toca, y probada con un caso positivo, tal como manda el ramal (iii) del
tramo doblado de EJECUTOR.md).

USO:
  python scripts/loop/verificar_citas_del_reporte.py
  python scripts/loop/verificar_citas_del_reporte.py --reporte RUTA

CASO POSITIVO POR MUTACION (vuelta 122, criterio de HECHO de la fase 08: "una
fase esta hecha cuando su verificacion se caeria si el fallo volviera"):
`scripts/loop/vuelta122_tarea1e_mutacion_citas.py` corre esta guarda sobre una
copia MUTADA del REPORTE.md de la vuelta 121 en la que la frase "vacio" cita,
sin abreviar, `SALIDA_V121_OPS03_ROJO_SEGUNDA_PASADA.txt` (que trae tres lineas
" M ..."): tiene que dar ROJO. Sobre el REPORTE.md de esta vuelta (una vez
escrito) tiene que dar VERDE.

CASO POSITIVO DEL PUNTO CIEGO DE FILA DE TABLA (vuelta 123, encargo 1.e, mio):
`scripts/loop/vuelta123_tarea1e_mutacion_fila_tabla.py` corre esta guarda
sobre una copia del REPORTE.md de la vuelta 122 con una fila de tabla nueva
que cita, con cita propia en la misma fila, `SALIDA_V122_TSC_APERTURA.txt`
afirmando "25/25" (ese fichero es el tsc, EXIT=0, y NUNCA contiene la cadena
"TODOS LOS TESTS PASARON (25/25)", que es del motor): tiene que dar ROJO
nombrando el par. Y la mutacion vieja de la 122
(`vuelta122_tarea1e_mutacion_citas.py`) tiene que SEGUIR dando ROJO: si el
arreglo de la fila de tabla rompiera esa mutacion, el arreglo estaria mal.

--- EL ENSANCHE: UN FICHERO CITADO TIENE QUE TRAER MEDICION, NO SOLO CODIGO
DE SALIDA (TAREA 1.i de la vuelta 129, acta de la vuelta 128, seccion "DOS
GUARDAS QUE NO ALCANZAN", ramal (a)) ---

POR QUE NACE. Esta guarda cotejaba el VEREDICTO ("vacio", "ROJO", "EXIT 0")
contra el fichero citado, pero nunca exigia que el fichero trajera una
medicion debajo: `SALIDA_V128_REBASE_ARBOL_IDENTICO.txt` (acta 128, 4.2)
tiene como contenido ENTERO la unica linea `EXITCODE: 0`, sin el comando, sin
los dos refs ni la salida de `git diff`, y el reporte lo citaba como prueba
de "vacio". La afirmacion resulto CIERTA (el auditor la verifico aparte con
sus propios comandos), pero la PRUEBA no era reproducible por nadie desde el
propio fichero: un fichero que no dice mas que su codigo de salida no prueba
nada por si mismo.

QUE COMPRUEBA, DE MAS. Para cada par (afirmacion, fichero) que ya coteja
`cumple()` y que CUADRA, ademas exige que el fichero tenga AL MENOS UNA
linea de contenido ademas de su linea de codigo de salida (`EXITCODE: <n>` o
`EXIT=<n>`, sin mas texto en esa linea). Si el contenido ENTERO del fichero
es esa unica linea, ROJO, nombrando el fichero y la afirmacion ("la palabra
que el reporte le colgo") que lo cita. EXCEPCION DECLARADA, UNA SOLA: los
ficheros cuyo nombre trae el segmento `_TSC_` (`SALIDA_V<vuelta>_TSC_
<LADO>.txt` y sus variantes `_POST`), cuyo formato canonico de esta casa es
EXACTAMENTE la linea `EXIT=<n>` y nada mas (docs/loop/PROMPT_SIGUIENTE.md,
seccion 1.c). Ningun otro nombre esta exento.

CASO POSITIVO REAL, SIN INVENTAR NADA (vuelta 129): esta guarda, corrida
sobre `docs/loop/REPORTE.md` DE LA VUELTA 128 (que sigue en el arbol de
trabajo hasta que la 129 lo sobrescribe), da ROJO nombrando
`SALIDA_V128_REBASE_ARBOL_IDENTICO.txt` con la afirmacion "vacio": ese es su
caso positivo real (`SALIDA_V129_1I_CASO_POSITIVO_REPORTE128.txt`). Sobre el
`REPORTE.md` de la vuelta 129 (una vez escrito) tiene que dar VERDE.
"""
import argparse
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")

VOCABULARIO = [
    "25/25",
    "vacio",
    "GATE 0 OK",
    "Gate 0 verde",
    "EXIT 0",
    "EXIT 1",
    "ROJO",
    "IDENTICA AL TALLADOR",
]

PATRON_FICHERO = re.compile(r"`([A-Za-z0-9_./\\-]+\.(?:txt|py|md|jsonl|json))`")
PATRON_GIT_STATUS_LINEA = re.compile(r"(?m)^ [MADR] ")
RE_SOLO_EXITCODE = re.compile(r"^\s*(EXITCODE:\s*\d+|EXIT=\d+)\s*$")


def es_excepcion_tsc(nombre_fichero):
    """La unica excepcion declarada del ensanche 1.i (vuelta 129): los
    ficheros de tsc, cuyo formato canonico de esta casa es EXACTAMENTE la
    linea `EXIT=<n>` y nada mas."""
    return "_TSC_" in nombre_fichero.upper()


def fichero_es_solo_codigo_de_salida(contenido):
    """True si el contenido ENTERO del fichero (ignorando lineas en blanco)
    es una unica linea con el codigo de salida (`EXITCODE: <n>` o
    `EXIT=<n>`) y nada mas: el caso que el ensanche 1.i de la vuelta 129
    prohibe fuera de la excepcion de tsc."""
    lineas = [l for l in contenido.splitlines() if l.strip() != ""]
    if len(lineas) != 1:
        return False
    return bool(RE_SOLO_EXITCODE.match(lineas[0].strip()))


def dividir_frases(texto):
    """Parte el texto en frases (con su posicion de inicio), por punto seguido
    de espacio o salto de linea. NO parte un punto de miles (tipo 3.853): ese
    punto SIEMPRE trae otro digito pegado despues, asi que el lookahead negativo
    solo (sin lookbehind) ya lo protege, y un lookbehind de digito de mas
    tambien tapaba el punto real de cierre de "25/25." (vuelta 122, hallado al
    probar la guarda sobre su propio reporte)."""
    # Las filas de tabla markdown ("| ... |") son unidades de dato, no prosa:
    # no llevan punto final y, sin este corte, una fila con "25/25" quedaria
    # en la MISMA "frase" que una cita de fichero de una fila vecina (vuelta
    # 122, hallado al probar la guarda sobre su propio reporte). Cada linea de
    # tabla se trata como su propia frase atomica, cortando el bloque de prosa
    # alrededor.
    frases = []
    pos = 0
    lineas = texto.split("\n")
    cursor = 0
    bloque_ini = None
    bloque = []

    def cerrar_bloque():
        if not bloque:
            return
        sub = "\n".join(bloque)
        base = bloque_ini
        p = 0
        for m in re.finditer(r"\.(?!\d)(?:\s+|\n|$)", sub):
            frase = sub[p:m.end()]
            if frase.strip():
                frases.append((base + p, frase))
            p = m.end()
        if p < len(sub) and sub[p:].strip():
            frases.append((base + p, sub[p:]))

    for linea in lineas:
        if linea.strip().startswith("|"):
            cerrar_bloque()
            bloque, bloque_ini = [], None
            if linea.strip():
                frases.append((cursor, linea))
        else:
            if bloque_ini is None:
                bloque_ini = cursor
            bloque.append(linea)
        cursor += len(linea) + 1
    cerrar_bloque()
    frases.sort(key=lambda t: t[0])
    return frases


def linea_de(texto, offset):
    return texto.count("\n", 0, offset) + 1


def ficheros_citados(frase):
    return PATRON_FICHERO.findall(frase)


def cumple(afirmacion, contenido):
    if afirmacion == "25/25":
        return "TODOS LOS TESTS PASARON (25/25)" in contenido
    if afirmacion == "vacio":
        return PATRON_GIT_STATUS_LINEA.search(contenido) is None
    if afirmacion in ("GATE 0 OK", "Gate 0 verde"):
        return "GATE 0: OK" in contenido
    if afirmacion == "EXIT 0":
        return "EXIT:1" not in contenido and "EXITCODE: 1" not in contenido
    if afirmacion in ("EXIT 1", "ROJO"):
        return "EXIT:1" in contenido or "EXITCODE: 1" in contenido
    if afirmacion == "IDENTICA AL TALLADOR":
        return "IDENTICA AL TALLADOR" in contenido
    return False


def cotejar(texto, fallos, pares_ok):
    frases = dividir_frases(texto)
    for i, (offset, frase) in enumerate(frases):
        # Una fila de tabla markdown ("| ... |") vuelve a ser cotejable desde
        # la vuelta 123 (encargo 1.e, acta 122 4.6): si lleva una afirmacion
        # del vocabulario Y una cita de fichero EN LA MISMA FILA, se coteja
        # como cualquier frase. Lo unico que sigue vivo del corte de la 122
        # es que una fila SIN cita propia NO MIRA a la frase anterior (ese
        # lookback era el cruce que motivo el recorte de la 122): simplemente
        # no se coteja y no es rojo, porque una tabla puede tener celdas de
        # dato sin cita (la cita vive en el parrafo que abre la tabla).
        es_fila_tabla = frase.strip().startswith("|")
        # El vocabulario se busca FUERA de los nombres de fichero citados: un
        # fichero como `SALIDA_V121_OPS03_ROJO_SEGUNDA_PASADA.txt` trae la
        # palabra "ROJO" en su propio nombre, y sin este enmascarado el
        # cotejo la tomaba como una AFIRMACION en prosa (vuelta 122, hallado
        # al probar la guarda sobre su propio reporte).
        frase_sin_ficheros = PATRON_FICHERO.sub(lambda m: "`" + " " * len(m.group(1)) + "`", frase)
        for afirmacion in VOCABULARIO:
            if afirmacion not in frase_sin_ficheros:
                continue
            ficheros = ficheros_citados(frase)
            if not ficheros:
                if es_fila_tabla:
                    # fila de tabla sin cita propia: no coteja, no es rojo, y
                    # NO mira a la frase anterior (vuelta 123, 1.e)
                    continue
                if i > 0:
                    ficheros = ficheros_citados(frases[i - 1][1])
            ln = linea_de(texto, offset)
            if not ficheros:
                fallos.append('linea %d: sin fichero citado para "%s": %s'
                              % (ln, afirmacion, frase.strip()[:200]))
                continue
            for fichero in ficheros:
                ruta = os.path.join(LOOP, fichero)
                if not os.path.exists(ruta):
                    ruta = os.path.join(RAIZ, fichero)
                if not os.path.exists(ruta):
                    fallos.append('linea %d: fichero citado no existe: `%s` (afirmacion "%s")'
                                  % (ln, fichero, afirmacion))
                    continue
                contenido = io.open(ruta, encoding="utf-8", errors="replace").read()
                if not cumple(afirmacion, contenido):
                    fallos.append('linea %d: NO CUADRA "%s" <-> `%s`. frase: %s'
                                  % (ln, afirmacion, fichero, frase.strip()[:200]))
                    continue
                # ENSANCHE 1.i (vuelta 129): el fichero citado tiene que
                # traer medicion, no solo su codigo de salida.
                if fichero_es_solo_codigo_de_salida(contenido) and not es_excepcion_tsc(fichero):
                    fallos.append('linea %d: `%s` citado con "%s" pero su contenido ENTERO es '
                                  'la linea de codigo de salida, sin medicion debajo (excepcion '
                                  'solo para ficheros _TSC_)' % (ln, fichero, afirmacion))
                    continue
                pares_ok.append((afirmacion, fichero, ln))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reporte", default=os.path.join(LOOP, "REPORTE.md"))
    args = ap.parse_args()

    if not os.path.exists(args.reporte):
        print("ROJO: no existe %s" % args.reporte)
        sys.exit(1)
    texto = io.open(args.reporte, encoding="utf-8").read()

    fallos = []
    pares_ok = []
    cotejar(texto, fallos, pares_ok)

    if fallos:
        print("ROJO, %d par(es) no cuadran (%s):" % (len(fallos), args.reporte))
        for f in fallos:
            print("  " + f)
        sys.exit(1)

    print("VERDE: %d par(es) cotejados en %s, todos cuadran." % (len(pares_ok), args.reporte))
    for a, fch, ln in pares_ok:
        print('  linea %d: "%s" <-> `%s`' % (ln, a, fch))
    sys.exit(0)


if __name__ == "__main__":
    main()
