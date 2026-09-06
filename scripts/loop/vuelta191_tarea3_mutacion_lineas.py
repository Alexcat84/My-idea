# -*- coding: utf-8 -*-
r"""vuelta191_tarea3_mutacion_lineas.py . EL CASO POSITIVO POR MUTACION DE LAS DOS
CONVENCIONES DE `lineas`.

QUE TIENE QUE CAZAR, DICHO CON LAS PALABRAS DEL ENCARGO: **que CAIGA si un
instrumento vuelve a publicar una sola cifra de lineas por la convencion que no
calza con `wc -l`.**

NINGUN assert SE PUBLICA COMO PRUEBA SIN HABER CORRIDO ANTES SU PRUEBA DE
MUTACION (`EJECUTOR.md` 1). Cada caso verde va seguido de su gemelo con el
esperado MUTADO, y el arnes exige que el gemelo CAIGA. **Ninguna variable de
veredicto es una constante literal**: todas salen de correr la guarda sobre un
texto fabricado.

Y EL EJEMPLAR NO ES INVENTADO: el bloque `F` corre las dos convenciones sobre
`docs/plan/LECTURAS_DIRIGIDAS.md`, que es el fichero donde el reporte de la 190
publico **2231** donde `wc -l` dice **2230**, y coteja contra `wc -l` de verdad.

USO:
  python scripts/loop/vuelta191_tarea3_mutacion_lineas.py
"""
import io
import os
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dos_convenciones_de_lineas as DC   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
SALIDA = os.path.join(LOOP, "SALIDA_V191_T3_MUTACION_LINEAS.txt")

# LOS CUATRO FUENTES FABRICADOS. Son texto, no ficheros del repo: el arnes no
# toca nada de la casa para probar.
FUENTE_SOLO_SPLIT = (
    "def escribe(texto):" + NL +
    '    print("REPORTE escrito: %d lineas" % len(texto.split(chr(10))))' + NL)
FUENTE_PAREJA = (
    "def escribe(texto):" + NL +
    '    print("REPORTE escrito: %d por count y %d por split"' + NL +
    "          % (texto.count(chr(10)), len(texto.split(chr(10)))))" + NL)
FUENTE_SOLO_COUNT = (
    "def escribe(texto):" + NL +
    '    print("REPORTE escrito: %d lineas por wc -l" % texto.count(chr(10)))' + NL)
FUENTE_MUDO = (
    "def escribe(texto):" + NL +
    '    print("REPORTE escrito: %d bytes" % len(texto.encode("utf-8")))' + NL)
FUENTE_CORREGIDO = (
    "def escribe(texto):" + NL +
    '    print("REPORTE escrito: %d lineas" % (len(texto.split(chr(10))) - 1))' + NL)


def _caso(w, nombre, obtenido, esperado):
    ok = obtenido == esperado
    w("   %-58s obtenido %-30s esperado %-30s -> %s"
      % (nombre, repr(obtenido)[:30], repr(esperado)[:30], "PASA" if ok else "CAE"))
    return 0 if ok else 1


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    fallos = 0
    no_cayeron = 0
    w("=" * 78)
    w("VUELTA 191, TAREA 3: CASO POSITIVO POR MUTACION DE LAS DOS CONVENCIONES")
    w("=" * 78)
    w("")

    # ------------------------------------------------------------- BLOQUE A
    w("A) LA GUARDA SOBRE LOS CINCO FUENTES FABRICADOS")
    for etiqueta, fuente, esperado in (
            ("SOLO SPLIT (el defecto que el acta 190 pillo)", FUENTE_SOLO_SPLIT, DC.ROJO),
            ("LA PAREJA", FUENTE_PAREJA, DC.VERDE_PAREJA),
            ("SOLO COUNT", FUENTE_SOLO_COUNT, DC.VERDE_CALZA),
            ("SPLIT YA CORREGIDA CON -1", FUENTE_CORREGIDO, DC.VERDE_CALZA),
            ("NO CUENTA LINEAS", FUENTE_MUDO, DC.NO_APLICA)):
        v, _s = DC.veredicto_de_fuente(fuente)
        fallos += _caso(w, etiqueta, v, esperado)
    w("   LA MUTACION 1: al fuente SOLO SPLIT se le pide VERDE, y tiene que CAER")
    v_rojo, _ = DC.veredicto_de_fuente(FUENTE_SOLO_SPLIT)
    if v_rojo != DC.ROJO:
        w("      LA MUTACION NO CAYO: el defecto no se ve, sale %r." % v_rojo)
        no_cayeron += 1
    else:
        w("      LA MUTACION CAE: sale ROJO y no VERDE, o sea que la guarda muerde")
        w("      exactamente el caso que el encargo nombra.")
    w("   LA MUTACION 2: `NO APLICA` NO es verde. Un fichero que no cuenta lineas")
    w("   no ha aprobado nada, y confundirlos dejaria pasar cualquier cosa")
    v_mudo, _ = DC.veredicto_de_fuente(FUENTE_MUDO)
    if v_mudo in (DC.VERDE_PAREJA, DC.VERDE_CALZA):
        w("      LA MUTACION NO CAYO: el mudo sale verde, %r." % v_mudo)
        no_cayeron += 1
    else:
        w("      LA MUTACION CAE: el mudo sale %r, que no es verde." % v_mudo)
    w("   LA MUTACION 3: la SPLIT ya corregida con `- 1` NO se acusa. Acusarla")
    w("   seria un falso positivo, y uno de los suyos vive en la nomina")
    v_corr, s_corr = DC.veredicto_de_fuente(FUENTE_CORREGIDO)
    if v_corr == DC.ROJO:
        w("      LA MUTACION NO CAYO: la corregida sale ROJA.")
        no_cayeron += 1
    else:
        w("      LA MUTACION CAE: sale %r, con %d sitio(s) SPLIT y %d corregido(s)."
          % (v_corr, len(s_corr["split"]), len(s_corr["split_corregido"])))
    w("")

    # ------------------------------------------------------------- BLOQUE B
    w("B) LA PAREJA DE CIFRAS, SOBRE TEXTOS FABRICADOS DE LARGO CONOCIDO")
    t_con = "a" + NL + "b" + NL + "c" + NL
    t_sin = "a" + NL + "b" + NL + "c"
    fallos += _caso(w, "texto de 3 lineas QUE TERMINA en salto", DC.lineas(t_con),
                    (3, 4))
    fallos += _caso(w, "texto de 3 lineas QUE NO TERMINA en salto", DC.lineas(t_sin),
                    (2, 3))
    w("   LA MUTACION: si las dos convenciones dieran lo mismo, no habria nada que")
    w("   arreglar y este arnes no probaria nada")
    c1, s1 = DC.lineas(t_con)
    if c1 == s1:
        w("      LA MUTACION NO CAYO: las dos dan %d, o sea que no se distinguen." % c1)
        no_cayeron += 1
    else:
        w("      LA MUTACION CAE: %d contra %d, uno de diferencia, que es la caida"
          % (c1, s1))
        w("      entera del acta 190.")
    w("   Y LA FRASE DE LA CASA NOMBRA A `wc -l` DENTRO, que es el punto:")
    f_par = DC.frase(t_con, nombre="fabricado")
    f_sola = DC.frase(t_con, nombre="fabricado", pareja=False)
    w("      pareja: %s" % f_par)
    w("      sola  : %s" % f_sola)
    fallos += _caso(w, "la frase de la pareja nombra wc -l", "wc -l" in f_par, True)
    fallos += _caso(w, "la frase de la sola nombra wc -l", "wc -l" in f_sola, True)
    w("")

    # ------------------------------------------------------------- BLOQUE C
    w("C) EL CENSO SOBRE UN DIRECTORIO FABRICADO, PARA QUE MUERDA DE VERDAD")
    tmp = tempfile.mkdtemp(prefix="v191_lineas_")
    try:
        io.open(os.path.join(tmp, "sano.py"), "w", encoding="utf-8",
                newline=NL).write(FUENTE_PAREJA)
        io.open(os.path.join(tmp, "mudo.py"), "w", encoding="utf-8",
                newline=NL).write(FUENTE_MUDO)
        filas = DC.censo(tmp)
        rojos = [n for n, v, _s in filas if v == DC.ROJO]
        fallos += _caso(w, "directorio SIN ningun defecto: rojos", len(rojos), 0)
        io.open(os.path.join(tmp, "roto.py"), "w", encoding="utf-8",
                newline=NL).write(FUENTE_SOLO_SPLIT)
        filas = DC.censo(tmp)
        rojos = [n for n, v, _s in filas if v == DC.ROJO]
        fallos += _caso(w, "el mismo directorio CON el defecto metido: rojos",
                        len(rojos), 1)
        fallos += _caso(w, "y lo nombra", rojos, ["roto.py"])
        w("   LA MUTACION: si el censo diera lo mismo con y sin el defecto metido,")
        w("   no estaria mirando nada")
        if len(rojos) == 0:
            w("      LA MUTACION NO CAYO: el defecto metido no cambia el censo.")
            no_cayeron += 1
        else:
            w("      LA MUTACION CAE: 0 rojos antes y %d despues, y con su nombre."
              % len(rojos))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    w("")

    # ------------------------------------------------------------- BLOQUE D
    w("D) EL CENSO SOBRE EL REPO DE VERDAD, QUE ES LO QUE ESTA VUELTA ARREGLO")
    filas = DC.censo(os.path.join(RAIZ, "scripts", "loop"))
    rojos = [n for n, v, _s in filas if v == DC.ROJO]
    w("   CIFRA ficheros .py censados: %d" % len(filas))
    fallos += _caso(w, "ficheros en ROJO en scripts/loop", len(rojos), 0)
    for n in rojos:
        w("      %s" % n)
    reparto = {}
    for _n, v, _s in filas:
        reparto[v] = reparto.get(v, 0) + 1
    for v in (DC.ROJO, DC.VERDE_PAREJA, DC.VERDE_CALZA, DC.NO_APLICA):
        w("   %-64s %d" % (v, reparto.get(v, 0)))
    w("")

    # ------------------------------------------------------------- BLOQUE E
    w("E) LOS INSTRUMENTOS PROPIOS DE ESTA VUELTA, UNO A UNO")
    w("   (una guarda que no se aplica a quien la escribio no es una guarda)")
    mios = [n for n in sorted(os.listdir(os.path.join(RAIZ, "scripts", "loop")))
            if n.startswith("vuelta191_") or n == "dos_convenciones_de_lineas.py"]
    malos = []
    for n in mios:
        codigo = io.open(os.path.join(RAIZ, "scripts", "loop", n),
                         encoding="utf-8", errors="replace").read()
        v, _s = DC.veredicto_de_fuente(codigo)
        w("   %-46s %s" % (n, v))
        if v == DC.ROJO:
            malos.append(n)
    fallos += _caso(w, "instrumentos de la 191 en ROJO", len(malos), 0)
    w("")

    # ------------------------------------------------------------- BLOQUE F
    w("F) EL EJEMPLAR DEL ACTA 190, COTEJADO CONTRA `wc -l` DE VERDAD")
    w("   (el reporte de la 190 publico 2231 lineas de este fichero. NO SE COPIA:")
    w("    se cuentan las dos convenciones y se corre `wc -l`)")
    ruta = os.path.join(RAIZ, "docs", "plan", "LECTURAS_DIRIGIDAS.md")
    if not os.path.isfile(ruta):
        w("   NO EXISTE %s" % ruta)
        fallos += 1
    else:
        texto = io.open(ruta, encoding="utf-8", errors="replace").read()
        c, s = DC.lineas(texto)
        w("   por `count(NL)`      : %d" % c)
        w("   por `len(split(NL))` : %d" % s)
        r = subprocess.run(["wc", "-l", "docs/plan/LECTURAS_DIRIGIDAS.md"],
                           cwd=RAIZ, capture_output=True)
        crudo = (r.stdout.decode("utf-8", errors="replace")
                 + r.stderr.decode("utf-8", errors="replace")).strip()
        w("   `wc -l` dice         : %r (exitcode %d)" % (crudo, r.returncode))
        wcn = None
        for tok in crudo.split():
            if tok.isdigit():
                wcn = int(tok)
                break
        if wcn is None:
            w("   `wc -l` NO ESTA DISPONIBLE AQUI, y eso se DECLARA en vez de")
            w("   fabricar un numero. El cotejo de este bloque queda SIN CORRER.")
        else:
            fallos += _caso(w, "la convencion count CALZA con wc -l", c, wcn)
            w("   LA MUTACION: la convencion split tiene que NO calzar, o el")
            w("   arreglo entero sobraria")
            if s == wcn:
                w("      LA MUTACION NO CAYO: split tambien calza, %d." % s)
                no_cayeron += 1
            else:
                w("      LA MUTACION CAE: split da %d y `wc -l` da %d." % (s, wcn))
    w("")

    w("=" * 78)
    w("CIFRA casos que CAEN: %d" % fallos)
    w("CIFRA mutaciones que NO cayeron (y deberian): %d" % no_cayeron)
    w("VEREDICTO: %s" % ("ROJO" if (fallos or no_cayeron) else "VERDE"))
    texto = NL.join(L) + NL
    io.open(SALIDA, "w", encoding="utf-8", newline=NL).write(texto)
    print(texto)
    print("ESCRITO: %s (%d bytes)"
          % (os.path.relpath(SALIDA, RAIZ).replace(os.sep, "/"),
             len(texto.encode("utf-8"))))
    return 1 if (fallos or no_cayeron) else 0


if __name__ == "__main__":
    sys.exit(main())
