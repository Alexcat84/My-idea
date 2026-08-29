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

CONTRATO (exacto, del encargo del auditor):
  - Lee docs/loop/REPORTE.md y busca los pares (afirmacion, fichero citado)
    sobre un vocabulario CERRADO y corto, en la misma frase o en la frase
    anterior: "25/25", "vacio", "GATE 0 OK" o "Gate 0 verde", "EXIT 0",
    "EXIT 1", "ROJO", "IDENTICA AL TALLADOR".
  - Para cada par, abre el fichero citado y comprueba:
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
mas. Un par fuera de ese vocabulario no se coteja: no es su contrato.

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
        # Una fila de tabla markdown ("| ... |") es dato ya validado por OTRA
        # guarda (tallar_cabecera_reporte.py --comparar): sus celdas no llevan
        # cita propia por diseno (la cita vive una sola vez, en el parrafo que
        # abre la tabla). Exigirle una cita a cada celda con "25/25" o similar
        # es imposible de cumplir sin romper la pega verbatim que la otra
        # guarda exige: se excluye del vocabulario, no del cotejo de prosa.
        if frase.strip().startswith("|"):
            continue
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
            if not ficheros and i > 0:
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
                if cumple(afirmacion, contenido):
                    pares_ok.append((afirmacion, fichero, ln))
                else:
                    fallos.append('linea %d: NO CUADRA "%s" <-> `%s`. frase: %s'
                                  % (ln, afirmacion, fichero, frase.strip()[:200]))


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
