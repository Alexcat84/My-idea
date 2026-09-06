# -*- coding: utf-8 -*-
r"""vuelta185_tarea1d_cotejo_quien_sello.py . EL COTEJO QUE ES LA PRUEBA DE LA
ESCALADA (vuelta 185, TAREA 1.d; `AUDITOR.md` 1.2).

QUE PRUEBA, Y NO ES UNA MEJORA SINO LA OPERACION DE CODIGO DE LA ESCALADA. La
caida de reporte `R.1` del acta 185: la novena columna de la tabla de los nueve
tramos, `quien lo sello`, estaba TECLEADA en la linea 128 de
`scripts/loop/_v184_tallar_t2.py` (`quien = "vuelta 183" if n <= 4 else
"**vuelta 184**"`) debajo de una frase del reporte que dice que la tabla sale de
contar sus ficheros *"y no de recordar nada"*. Los valores eran correctos HOY y
caducaban solos.

LA PRUEBA ES QUE LA VERSION COMPUTADA REPRODUCE LA TECLEADA EXACTAMENTE. Las
NUEVE celdas de esa columna se leen de DOS sitios y se cotejan una a una:

  1. LAS TECLEADAS: se leen de `docs/loop/REPORTE.md`, que es donde el reporte de
     la 184 las publico y donde siguen sin tocarse.
  2. LAS COMPUTADAS: se leen de `scripts/loop/_v184_t2_seccion.md`, que es lo que
     el tallador acaba de escribir con `tramos_por_vuelta()`.

ESTE FICHERO NO RE-PEGA NADA EN `docs/loop/REPORTE.md`. El reporte de la 184 se
cierra en la TAREA 2 con el texto que ya tiene; aqui solo se prueba el
instrumento.

USO:
  python scripts/loop/vuelta185_tarea1d_cotejo_quien_sello.py
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
REPORTE = os.path.join(LOOP, "REPORTE.md")
SECCION = os.path.join(RAIZ, "scripts", "loop", "_v184_t2_seccion.md")
TALLADOR = os.path.join(RAIZ, "scripts", "loop", "_v184_tallar_t2.py")
DESTINO = os.path.join(LOOP, "SALIDA_V185_T1D_COTEJO_QUIEN_SELLO.txt")

# LA FILA DE UN TRAMO: empieza por `| **<n>** |` y trae nueve celdas. La novena
# es `quien lo sello`. NO se cuenta por posicion de linea: se busca la fila por
# su primer campo, que es el numero del tramo.
PAT_FILA = re.compile(r"^\|\s*\*\*(\d+)\*\*\s*\|")


def celdas_de(texto):
    """LAS CELDAS `quien lo sello` DE LA TABLA DE LOS NUEVE TRAMOS, LEIDAS DE UN
    TEXTO. Devuelve `{numero_de_tramo: celda}`. PURA.

    LA COLUMNA SE LOCALIZA POR SU CABECERA Y NO POR SU NUMERO DE ORDEN: si algun
    dia la tabla ganara o perdiera una columna, esto seguiria leyendo la que se
    llama `quien lo sello` en vez de la novena que haya."""
    lineas = texto.replace(chr(13) + NL, NL).split(NL)
    idx = None
    salida = {}
    for l in lineas:
        if "quien lo sello" in l and l.strip().startswith("|"):
            campos = [c.strip() for c in l.strip().strip("|").split("|")]
            if "quien lo sello" in campos:
                idx = campos.index("quien lo sello")
            continue
        m = PAT_FILA.match(l.strip())
        if m and idx is not None:
            campos = [c.strip() for c in l.strip().strip("|").split("|")]
            if len(campos) > idx:
                salida[int(m.group(1))] = campos[idx]
    return salida, idx


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    fallos = 0
    w("COTEJO DE LA COLUMNA `quien lo sello`: LA COMPUTADA CONTRA LA TECLEADA")
    w("(vuelta 185, TAREA 1.d, operacion de codigo de la escalada de AUDITOR.md 1.2)")
    w("")

    w("A) LA LINEA TECLEADA YA NO ESTA EN EL INSTRUMENTO, Y SE COMPRUEBA")
    fuente = io.open(TALLADOR, encoding="utf-8").read().replace(chr(13) + NL, NL)
    vieja = 'quien = "vuelta 183" if n <= 4 else "**vuelta 184**"'
    w("   %s -> %d lineas | disco %d bytes"
      % ("scripts/loop/_v184_tallar_t2.py", fuente.count(NL),
         os.path.getsize(TALLADOR)))
    # LA CITA LEGITIMA SE EXIME NOMBRANDOLA, NO ENSANCHANDO EL PATRON HASTA QUE
    # NO MUERDA (doctrina de la `5.3` del acta 185). La linea vieja aparece hoy
    # DENTRO DE UN COMENTARIO del instrumento, porque `EJECUTOR.md` 8 manda que
    # una correccion no tape lo que corrige. Se cuentan las dos cosas POR
    # SEPARADO: la que es CODIGO VIVO tiene que ser CERO; la que es CITA se
    # cuenta, se nombra y se pega.
    como_codigo = [i for i, l in enumerate(fuente.split(NL), 1)
                   if l.strip().startswith('quien = "vuelta 183"')]
    como_cita = [i for i, l in enumerate(fuente.split(NL), 1)
                 if vieja in l and l.strip().startswith("#")]
    w("   CIFRA apariciones de la linea tecleada COMO CODIGO VIVO: %d, lineas %s"
      % (len(como_codigo), como_codigo or "(ninguna)"))
    w("   CIFRA apariciones COMO CITA DENTRO DE UN COMENTARIO: %d, lineas %s"
      % (len(como_cita), como_cita or "(ninguna)"))
    for i in como_cita:
        w("      LINEA %d: %s" % (i, fuente.split(NL)[i - 1].strip()[:140]))
    w("   CIFRA apariciones totales del texto en el fichero: %d" % fuente.count(vieja))
    w("   CIFRA apariciones de 'tramos_por_vuelta': %d"
      % fuente.count("tramos_por_vuelta"))
    w("   CIFRA apariciones de 'from cerrar_reporte import': %d"
      % fuente.count("from cerrar_reporte import"))
    if como_codigo:
        w("   ROJO: la linea tecleada sigue viva como codigo.")
        fallos += 1
    if fuente.count(vieja) != len(como_codigo) + len(como_cita):
        w("   ROJO: hay apariciones que no son ni codigo vivo ni cita, y una")
        w("   aparicion que el instrumento no sabe clasificar no se deja pasar.")
        fallos += 1
    if not fuente.count("from cerrar_reporte import"):
        w("   ROJO: la funcion no se importa, o sea que se copio.")
        fallos += 1
    w("")

    w("B) LAS NUEVE CELDAS, LEIDAS DE SUS DOS SITIOS")
    texto_rep = io.open(REPORTE, encoding="utf-8").read()
    texto_sec = io.open(SECCION, encoding="utf-8").read()
    tecleadas, i_rep = celdas_de(texto_rep)
    computadas, i_sec = celdas_de(texto_sec)
    w("   docs/loop/REPORTE.md        -> disco %d bytes | columna en el indice %s"
      % (os.path.getsize(REPORTE), i_rep))
    w("   scripts/loop/_v184_t2_seccion.md -> disco %d bytes | columna en el indice %s"
      % (os.path.getsize(SECCION), i_sec))
    w("   CIFRA filas de tramo leidas del REPORTE:  %d" % len(tecleadas))
    w("   CIFRA filas de tramo leidas de la SECCION: %d" % len(computadas))
    if len(tecleadas) != 9 or len(computadas) != 9:
        w("   ROJO: no hay nueve filas en los dos sitios. No se cotejan celdas que")
        w("   no existen.")
        fallos += 1
    w("")
    w("   | tramo | TECLEADA (del REPORTE) | COMPUTADA (del tallador) | calza |")
    w("   |---:|---|---|---|")
    n_calzan = 0
    for n in range(1, 10):
        a = tecleadas.get(n, "(ausente)")
        b = computadas.get(n, "(ausente)")
        ok = (a == b) and a != "(ausente)"
        if ok:
            n_calzan += 1
        else:
            fallos += 1
        w("   | %d | %s | %s | %s |" % (n, a, b, "SI" if ok else "NO"))
    w("")
    w("   CIFRA celdas que CALZAN: %d de 9" % n_calzan)
    w("   CIFRA celdas que NO CALZAN: %d" % (9 - n_calzan))
    w("")

    w("C) LA MUTACION DEL ESPERADO, QUE ES LO QUE PRUEBA QUE ESTE COTEJO PUEDE")
    w("   CAER. Se muta UNA celda de la tecleada y se comprueba que el cotejo la")
    w("   caza. No se toca ningun fichero: la mutacion vive en memoria.")
    mutadas = dict(tecleadas)
    if 1 in mutadas:
        mutadas[1] = mutadas[1] + " (mutada)"
    n_calzan_mut = len([1 for n in range(1, 10)
                        if mutadas.get(n) == computadas.get(n)
                        and mutadas.get(n) is not None])
    w("   con la celda del tramo 1 mutada, CALZAN %d de 9" % n_calzan_mut)
    w("   EL COTEJO CAE AL MUTAR UNA CELDA: %s"
      % ("SI" if n_calzan_mut < n_calzan else "NO"))
    if n_calzan_mut >= n_calzan:
        fallos += 1
    w("")
    w("   Y LA SEGUNDA MUTACION: SI LA FRONTERA TECLEADA SIGUIERA VIVA, LA COLUMNA")
    w("   DIRIA `vuelta 183` PARA LOS TRAMOS 1 A 4 PASE LO QUE PASE. La computada")
    w("   se compara con lo que esa frontera diria, para que se vea que HOY")
    w("   coinciden y que la coincidencia es una MEDICION y no una copia.")
    frontera = {n: ("vuelta 183" if n <= 4 else "**vuelta 184**") for n in range(1, 10)}
    iguales = len([1 for n in range(1, 10) if frontera[n] == computadas.get(n)])
    w("   la frontera tecleada y la computada coinciden en %d de 9 celdas HOY"
      % iguales)
    w("   (y esa es toda la gracia: la computada REPRODUCE la tecleada, y desde")
    w("    hoy seguira siendo cierta cuando la bateria de la 189 se corte en otro")
    w("    sitio, cosa que la frontera tecleada no puede prometer)")
    w("")

    w("D) LO QUE ESTE FICHERO NO HACE: no re-pega nada en docs/loop/REPORTE.md.")
    w("   El reporte de la 184 se cierra en la TAREA 2 con el texto que ya tiene.")
    w("")
    w("CIFRA fallos: %d" % fallos)
    w("VEREDICTO: %s" % ("VERDE" if fallos == 0 else "ROJO"))

    t = NL.join(L) + NL
    io.open(DESTINO, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (DESTINO, len(t.encode("utf-8"))))
    return 0 if fallos == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
