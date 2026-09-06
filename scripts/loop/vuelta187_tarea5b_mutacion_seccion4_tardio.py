# -*- coding: utf-8 -*-
r"""vuelta187_tarea5b_mutacion_seccion4_tardio.py . EL CASO POSITIVO POR MUTACION
DE LA DECLARACION DEL DEFECTO DE LA SECCION 4 EN EL CARRIL DE CIERRE TARDIO.

QUE PRUEBA, Y ES LA `P.2` CONTESTADA POR EL ACTA 187 (punto 7.2, por extension de
la `7.2` del acta 186: *"ni se eximen ni se reescriben, se declaran"*).

  - En el carril **NORMAL**, una seccion 4 muda **BLOQUEA**, con su texto de hoy.
  - En el carril **TARDIO**, la misma seccion 4 muda **NO bloquea** y **aparece
    DECLARADA en el texto**, cotejada **por contencion** y no por parecido.
  - **El CERO se dice y no se omite**: sin motivos, la declaracion se escribe
    igual y dice cero.
  - Y sobre **los ficheros REALES del 184** se exige **1 motivo** y que **la
    declaracion lo nombre**.

QUE ES LO QUE EL ARNES EXIGE Y LA VISTA NO PUEDE DAR. El acta 187 dice, con esas
palabras, que en el carril normal la guarda *"sigue bloqueando entera, y eso lo
tiene que exigir el arnes"*. Aqui esa exigencia es el CASO A, y va sobre la
COLUMNA `bloquea` real de `main()`, leida del fichero fuente, no sobre una
descripcion de ella.

TODAS LAS FUNCIONES QUE SE PRUEBAN SON PURAS Y RECIBEN TEXTOS FABRICADOS. El
unico caso que toca disco es el ultimo, porque su sujeto son los dos ficheros
reales del 184, y ese caso **no escribe nada**.

Y EL CASO ROJO SE PRUEBA POR MUTACION (`EJECUTOR.md` 1): cada comprobacion se
corre con su esperado y **despues con el esperado MUTADO**, y se exige que CAIGA.

USO:
  python scripts/loop/vuelta187_tarea5b_mutacion_seccion4_tardio.py
"""
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cerrar_reporte as CR   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
REP184 = os.path.join(LOOP, "reportes", "REPORTE_V184.md")
AP184 = os.path.join(LOOP, "SALIDA_V184_APERTURA.txt")


def apertura_fabricada(status, numstat):
    """UNA APERTURA SELLADA DE MENTIRA, con sus dos cifras. NO toca el repo."""
    return NL.join([
        "SELLO DE APERTURA DE LA VUELTA 999, fabricado.", "",
        "=== C. git status --porcelain ENTERO ===",
        "CIFRA lineas de status: %d" % status, "",
        "=== E. DIFF REAL ===",
        "CIFRA filas de `git diff --numstat -- dataset/` AL ENTRAR: %d" % numstat,
        "",
    ]) + NL


def reporte_fabricado(dice_status=None, dice_numstat=None):
    """UN REPORTE DE MENTIRA cuya seccion 4 afirma lo que se le pida, o calla.
    NO toca el repo. `None` en una cifra significa QUE NO LA AFIRMA."""
    # LOS DOS MARCADORES SE IMPORTAN DE LA GUARDA Y NO SE TECLEAN AQUI. La
    # primera version de este arnes los tecleo parafraseados y su CASO C salio
    # en ROJO: el reporte fabricado creia afirmar la cifra de status y la guarda
    # no veia nada, porque `cifras_que_afirma_la_seccion4()` busca el MARCADOR
    # literal `git status --porcelain` y no la frase `CIFRA lineas de status`.
    # La corrida en rojo entera vive en
    # `docs/loop/SALIDA_V187_T5B_MUTACION_SECCION4_TARDIO_EN_ROJO.txt`. **Un
    # arnes que fabrica su sujeto con otras palabras que las que la guarda busca
    # no prueba la guarda: prueba la parafrasis.**
    sec4 = ["## 4. EL ESTADO DEL ARBOL", ""]
    if dice_status is not None:
        sec4.append("El arbol abrio con `%s` en **%d** lineas."
                    % (CR.MARCADOR_STATUS, dice_status))
    if dice_numstat is not None:
        sec4.append("Y `%s` AL ENTRAR en **%d** filas."
                    % (CR.MARCADOR_NUMSTAT, dice_numstat))
    if len(sec4) == 2:
        sec4.append("Aqui no se afirma ninguna cifra del estado del arbol.")
    return NL.join([
        "# REPORTE DE LA VUELTA 999 (fabricado)", "",
        "**EL VEREDICTO DE UNA LINEA: de mentira.**", "",
        "## 3. UN APARTADO", "", "Cuerpo.", "",
    ] + sec4 + ["", "## 5. OTRO APARTADO", "", "Cuerpo.", ""]) + NL


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("CASO POSITIVO POR MUTACION de la declaracion del defecto de la SECCION 4")
    w("en el CARRIL DE CIERRE TARDIO (vuelta 187, TAREA 5.b; `P.2`, acta 187 7.2)")
    w("")
    fallos = 0
    casos = 0

    w("CASO A. EN EL CARRIL NORMAL LA SECCION 4 MUDA BLOQUEA, Y ESO LO EXIGE EL")
    w("   ARNES Y NO LA VISTA: se lee la columna `bloquea` real de main() del")
    w("   fichero fuente, y se cuenta en cual de los dos carriles suma a `extra`.")
    casos += 1
    fuente = io.open(os.path.join(RAIZ, "scripts", "loop", "cerrar_reporte.py"),
                     encoding="utf-8").read().replace(chr(13) + NL, NL)
    n_normal = len(re.findall(r"if not tardio:\s*\n\s*extra \+= len\(motivos_s4\)",
                              fuente))
    w("   apariciones de `if not tardio: extra += len(motivos_s4)`: %d (esperado 1)"
      % n_normal)
    w("   ES DECIR: en el carril NORMAL los motivos de la seccion 4 SUMAN a extra")
    w("   y el cierre CAE; en el TARDIO no suman por si mismos.")
    w("   con el esperado MUTADO (exigir 0): %s" % ("PASA" if n_normal == 0 else "CAE"))
    if n_normal != 1:
        fallos += 1
    w("")

    w("CASO B. LA MISMA SECCION 4 MUDA, EN CARRIL TARDIO: NO BLOQUEA POR SI SOLA,")
    w("   Y APARECE DECLARADA EN EL TEXTO, COTEJADA POR CONTENCION.")
    casos += 1
    rep = reporte_fabricado(dice_status=None, dice_numstat=0)
    ap = apertura_fabricada(status=2, numstat=0)
    motivos = CR.seccion4_que_no_calza(rep, ap, "APERTURA_DE_MENTIRA.txt")
    w("   CIFRA motivos en rojo: %d (esperado 1)" % len(motivos))
    for m in motivos:
        w("      | %s" % m[:150])
    decl = CR.declaracion_de_seccion4(motivos, 184, 187, "REPORTE_DE_MENTIRA.md")
    texto_cerrado = rep.rstrip(NL) + NL + NL + decl
    w("   la declaracion mide %d bytes" % len(decl.encode("utf-8")))
    w("   LA COTEJO POR CONTENCION, MOTIVO A MOTIVO Y NO POR PARECIDO:")
    sin_declarar = [m for m in motivos if m not in texto_cerrado]
    for m in motivos:
        w("      motivo dentro del texto cerrado: %s" % ("SI" if m in texto_cerrado else "NO"))
    w("   CIFRA motivos SIN declarar: %d (esperado 0)" % len(sin_declarar))
    w("   la marca %r esta: %s"
      % (CR.MARCA_TARDIO_S4, "SI" if CR.MARCA_TARDIO_S4 in texto_cerrado else "NO"))
    okb = (len(motivos) == 1 and not sin_declarar
           and CR.MARCA_TARDIO_S4 in texto_cerrado)
    w("   VEREDICTO DEL CASO B: %s" % ("VERDE" if okb else "ROJO"))
    w("   con el esperado MUTADO (exigir 0 motivos): %s"
      % ("PASA" if len(motivos) == 0 else "CAE"))
    w("   con el esperado MUTADO (exigir que el motivo NO este declarado): %s"
      % ("PASA" if sin_declarar else "CAE"))
    if not okb or len(motivos) == 0 or sin_declarar:
        fallos += 1
    w("")

    w("CASO B.1. LA DECLARACION NO SE ACUSA A SI MISMA. Va dentro de una cerca, y")
    w("   las guardas de este fichero no miran dentro de las cercas. Si fuera")
    w("   prosa, la siguiente pasada la contaria como una afirmacion nueva de la")
    w("   seccion 4 y el instrumento se perseguiria la cola.")
    casos += 1
    motivos_2 = CR.seccion4_que_no_calza(texto_cerrado, ap, "APERTURA_DE_MENTIRA.txt")
    w("   motivos ANTES de anexar la declaracion: %d" % len(motivos))
    w("   motivos DESPUES de anexarla:            %d" % len(motivos_2))
    w("   SON LOS MISMOS: %s" % ("SI" if motivos == motivos_2 else "NO"))
    huerf = CR.cifras_sin_pareja(texto_cerrado)
    w("   y cifras_sin_pareja() sobre el texto con la declaracion dentro: %d"
      % len(huerf))
    okb1 = (motivos == motivos_2)
    w("   con el esperado MUTADO (exigir que cambien): %s"
      % ("PASA" if motivos != motivos_2 else "CAE"))
    if not okb1:
        fallos += 1
    w("")

    w("CASO C. CERO MOTIVOS EN CARRIL TARDIO: LA DECLARACION DICE CERO Y NO SE")
    w("   OMITE. Un campo ausente y un cero contado no son lo mismo.")
    casos += 1
    rep_ok = reporte_fabricado(dice_status=2, dice_numstat=0)
    motivos_0 = CR.seccion4_que_no_calza(rep_ok, ap, "APERTURA_DE_MENTIRA.txt")
    decl_0 = CR.declaracion_de_seccion4(motivos_0, 184, 187, "REPORTE_DE_MENTIRA.md")
    w("   CIFRA motivos en rojo: %d (esperado 0)" % len(motivos_0))
    w("   la declaracion se escribe igual: %s"
      % ("SI, %d bytes" % len(decl_0.encode("utf-8")) if decl_0 else "NO"))
    dice_cero = "CIFRA motivos en rojo de la seccion 4: 0" in decl_0
    w("   y DICE CERO con todas las letras: %s" % ("SI" if dice_cero else "NO"))
    w("   la marca %r esta igualmente: %s"
      % (CR.MARCA_TARDIO_S4, "SI" if CR.MARCA_TARDIO_S4 in decl_0 else "NO"))
    okc = (not motivos_0 and dice_cero and CR.MARCA_TARDIO_S4 in decl_0)
    w("   con el esperado MUTADO (exigir que la declaracion se omita): %s"
      % ("PASA" if not decl_0 else "CAE"))
    if not okc or not decl_0:
        fallos += 1
    w("")

    w("CASO D. LOS FICHEROS REALES DEL 184: SE EXIGE 1 MOTIVO Y QUE LA")
    w("   DECLARACION LO NOMBRE. Es el caso que la `P.2` trajo.")
    casos += 1
    if not os.path.exists(REP184) or not os.path.exists(AP184):
        w("   ROJO: falta alguno de los dos ficheros reales.")
        w("      docs/loop/reportes/REPORTE_V184.md existe: %s"
          % os.path.exists(REP184))
        w("      docs/loop/SALIDA_V184_APERTURA.txt existe: %s" % os.path.exists(AP184))
        fallos += 1
    else:
        d_r = io.open(REP184, "rb").read()
        d_a = io.open(AP184, "rb").read()
        w("   docs/loop/reportes/REPORTE_V184.md -> disco %d bytes | LF %d bytes"
          % (len(d_r), len(d_r.replace(b"\r\n", b"\n"))))
        w("   docs/loop/SALIDA_V184_APERTURA.txt -> disco %d bytes | LF %d bytes"
          % (len(d_a), len(d_a.replace(b"\r\n", b"\n"))))
        t_r = d_r.decode("utf-8", errors="replace").replace(chr(13) + NL, NL)
        t_a = d_a.decode("utf-8", errors="replace").replace(chr(13) + NL, NL)
        vara = CR.cifras_de_la_apertura(t_a)
        w("   LO QUE LA APERTURA SELLADA DEL 184 PUBLICA, LEIDO Y NO TECLEADO:")
        w("      CIFRA lineas de status: %s" % vara["status"])
        w("      CIFRA filas de numstat AL ENTRAR: %s" % vara["numstat"])
        m184 = CR.seccion4_que_no_calza(t_r, t_a, "docs/loop/SALIDA_V184_APERTURA.txt")
        w("   CIFRA motivos en rojo: %d (esperado 1)" % len(m184))
        for m in m184:
            w("      | %s" % m)
        d184 = CR.declaracion_de_seccion4(
            m184, 184, 187, "docs/loop/reportes/REPORTE_V184.md")
        nombrados = [m for m in m184 if m in d184]
        w("   CIFRA motivos que la declaracion NOMBRA: %d de %d"
          % (len(nombrados), len(m184)))
        w("   la declaracion dice la cuenta: %s"
          % ("SI" if "CIFRA motivos en rojo de la seccion 4: %d" % len(m184) in d184
             else "NO"))
        w("   y dice que el 184 NO se reabre ni se reescribe: %s"
          % ("SI" if "NO SE REABRE Y NO SE REESCRIBE" in d184 else "NO"))
        okd = (len(m184) == 1 and len(nombrados) == len(m184))
        w("   VEREDICTO DEL CASO D: %s" % ("VERDE" if okd else "ROJO"))
        w("   con el esperado MUTADO (exigir 2 motivos): %s"
          % ("PASA" if len(m184) == 2 else "CAE"))
        w("   con el esperado MUTADO (exigir 0 motivos): %s"
          % ("PASA" if len(m184) == 0 else "CAE"))
        if not okd or len(m184) in (0, 2):
            fallos += 1
    w("")

    w("CASO E. NINGUNA OTRA GUARDA SE AFLOJA POR ESTA TAREA, Y SE CUENTA EN VEZ")
    w("   DE PROMETERSE: la guarda de LAS DOS CONVENCIONES de la TAREA 4 bloquea")
    w("   en LOS DOS carriles, y su columna `bloquea` en main() es `True`.")
    casos += 1
    n_conv = len(re.findall(
        r'"toda pareja de convenciones es CIERTA, no solo completa",\s*\n\s*'
        r'not convenciones_rojas, True\)', fuente))
    w("   apariciones de la comprobacion con `bloquea=True`: %d (esperado 1)" % n_conv)
    w("   con el esperado MUTADO (exigir 0): %s" % ("PASA" if n_conv == 0 else "CAE"))
    if n_conv != 1:
        fallos += 1
    w("")

    w("CASO F. LA EXENCION DEL CARRIL TARDIO NO ES GRATIS: SI LA DECLARACION NO")
    w("   ESTA, VUELVE A SER ROJO. Se prueba sobre el cotejo por contencion, que")
    w("   es lo que main() hace: un texto SIN la declaracion deja motivos sin")
    w("   declarar y eso vuelve a sumar.")
    casos += 1
    sin_decl = rep  # el mismo reporte, pero SIN anexarle la declaracion
    faltantes = [m for m in motivos if m not in sin_decl]
    w("   motivos que NO estan declarados en un texto sin declaracion: %d de %d"
      % (len(faltantes), len(motivos)))
    w("   la marca %r esta: %s"
      % (CR.MARCA_TARDIO_S4, "SI" if CR.MARCA_TARDIO_S4 in sin_decl else "NO"))
    okf = (len(faltantes) == len(motivos) and CR.MARCA_TARDIO_S4 not in sin_decl)
    w("   LA EXENCION NO SE COGE SIN DECLARARLA: %s" % ("SI" if okf else "NO"))
    w("   con el esperado MUTADO (exigir que si este declarada): %s"
      % ("PASA" if not faltantes else "CAE"))
    if not okf or not faltantes:
        fallos += 1
    w("")

    w("CIFRA casos: %d" % casos)
    w("CIFRA fallos: %d" % fallos)
    w("VEREDICTO: %s" % ("VERDE" if fallos == 0 else "ROJO"))
    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V187_T5B_MUTACION_SECCION4_TARDIO.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0 if fallos == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
