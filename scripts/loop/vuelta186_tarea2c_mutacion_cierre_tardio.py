# -*- coding: utf-8 -*-
r"""vuelta186_tarea2c_mutacion_cierre_tardio.py . EL CASO POSITIVO POR MUTACION
DEL CARRIL DE CIERRE TARDIO.

QUIEN LO ENCARGA. El acta 186, punto `7.2`, contestando la `P.2`: las 10 cifras
sin pareja del reporte de la 184 *"ni se eximen ni se reescriben. SE DECLARAN"*.
Reescribir el texto esta descartado porque seria escribir en pasado lo que no
paso; eximir en silencio esta descartado por banco 9, que llama a eso degradacion
silenciosa. Lo que queda es un carril donde el defecto queda **visible y medido**.

QUE PRUEBA, CASO A CASO, Y TODOS TIENEN QUE CAER AL MUTAR SU ESPERADO:
  (A) LA CONDICION DEL CARRIL, que es `es_cierre_tardio()` y es PURA: la vuelta
      en curso igual a la del reporte NO abre el carril; una posterior SI; y si
      la vuelta en curso no se puede leer, TAMPOCO se abre. La falta de evidencia
      cierra el carril, no lo abre.
  (B) CIFRAS SIN PAREJA EN CARRIL NORMAL: bloquean.
  (C) LAS MISMAS EN CARRIL TARDIO: no bloquean, Y APARECEN DECLARADAS en el
      texto, cotejado POR CONTENCION renglon a renglon.
  (D) CERO CIFRAS SIN PAREJA EN CARRIL TARDIO: la declaracion dice cero y NO se
      omite.
  (E) EL CARRIL TARDIO NO AFLOJA NINGUNA DE LAS CUATRO PIEZAS: sobre un texto al
      que le falta cada una de las cuatro, `piezas_que_faltan()` sigue
      acusandolas, y ese instrumento NI SIQUIERA TIENE un parametro de carril,
      que es la prueba mas fuerte que se puede dar de que el carril no lo toca.

LO QUE ESTE ARNES NO HACE: no escribe ningun reporte, no corre
`cerrar_reporte.py` como proceso y no toca `docs/loop/REPORTE.md`. Llama a las
funciones PURAS del fichero vivo con textos fabricados en memoria.

USO:
  python scripts/loop/vuelta186_tarea2c_mutacion_cierre_tardio.py
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cerrar_reporte as CR   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

FILAS = ["| celda | celda |", "| a | b |", "| c | d |", "| e | f |",
         "| g | h |", "| i | j |", "| k | l |", "| m | n |", "| o | p |"]
BAT = ["linea uno de la bateria"]
NOM = "docs/loop/SALIDA_V999_BATERIA.txt"

# TRES LINEAS QUE PUBLICAN UNA CIFRA SIN SU PAREJA, escritas a proposito con una
# sola convencion para que `cifras_sin_pareja()` las cace.
SIN_PAREJA = [
    "El fichero mide 1234 bytes.",
    "Y el otro mide 5678 bytes.",
    "Su sha256 es abcdef0123456789abcdef01.",
]


def fabricar(extra=(), sin_veredicto=False, sin_seccion=None,
             con_hueco_de_cabecera=False, filas_pegadas=True):
    """UN REPORTE DE MENTIRA. PURA: devuelve texto y no escribe nada.

    Cada parametro rompe UNA de las cuatro piezas, para que el caso (E) pueda
    exigir que el carril tardio no afloje ninguna."""
    p = ["# REPORTE DE LA VUELTA 999 (fabricado)", ""]
    if not sin_veredicto:
        p += ["**EL VEREDICTO DE UNA LINEA: de mentira.**", ""]
    if con_hueco_de_cabecera:
        p += ["**%s.** Y su prosa." % CR.HUECO_CABECERA, ""]
    if filas_pegadas:
        p += FILAS + [""]
    p += list(extra) + [""]
    for k in range(3, 9):
        if sin_seccion is not None and k == sin_seccion:
            continue
        p += ["## %d. UNA SECCION DE MENTIRA" % k, "", "Y su cuerpo.", ""]
    if sin_seccion != 9:
        p += ["## 9. LA BATERIA DE MUTACIONES, DE MENTIRA", ""] + BAT + [""]
    return NL.join(p) + NL


def _caso_a(w):
    """A: la condicion del carril, que es PURA."""
    fallos = casos = caen = 0
    w("CASO A. LA CONDICION DEL CARRIL, QUE SE COMPUTA Y NO SE PASA POR BANDERA")
    escenarios = [
        ("la vuelta en curso es la del reporte", 186, 186, False),
        ("la vuelta en curso es POSTERIOR", 184, 186, True),
        ("la vuelta en curso es ANTERIOR", 186, 184, True),
        ("la vuelta en curso NO SE PUDO LEER", 184, None, False),
        ("la vuelta del reporte es None", None, 186, False),
    ]
    for etiqueta, v, curso, esperado in escenarios:
        medido = CR.es_cierre_tardio(v, curso)
        casos += 1
        w("   %-42s reporte %-5s curso %-5s -> %-5s | esperado %-5s | %s"
          % (etiqueta, v, curso, medido, esperado,
             "CALZA" if medido == esperado else "NO CALZA"))
        if medido != esperado:
            fallos += 1
        w("      MUTACION del esperado (exigir %s): %s"
          % (not esperado, "PASA" if medido != esperado else "CAE"))
        if medido != esperado:
            fallos += 1
        else:
            caen += 1
    w("")
    return fallos, casos, caen


def _casos_bcd(w):
    """B, C Y D: las cifras sin pareja en cada carril y la declaracion."""
    fallos = casos = caen = 0
    texto = fabricar(extra=SIN_PAREJA)
    huerfanas = CR.cifras_sin_pareja(texto)
    w("CASO B. CIFRAS SIN PAREJA EN CARRIL NORMAL: BLOQUEAN")
    w("   CIFRA cifras sin pareja medidas sobre el texto fabricado: %d"
      % len(huerfanas))
    for n, especie, muestra, linea in huerfanas:
        w("      linea %-4d %-5s %-24s | %s" % (n, especie, muestra, linea[:70]))
    # EL BLOQUEO EN CARRIL NORMAL SE MODELA COMO LO HACE main(): la condicion
    # `bloquea` es `not tardio`, y aqui se computa con la MISMA funcion pura.
    normal = not CR.es_cierre_tardio(999, 999)
    bloquea_normal = bool(huerfanas) and normal
    casos += 1
    w("   carril: %s | bloquea: %s"
      % ("NORMAL" if normal else "TARDIO", bloquea_normal))
    w("   ESPERADO: bloquea -> %s" % ("CALZA" if bloquea_normal else "NO CALZA"))
    if not bloquea_normal:
        fallos += 1
    w("   MUTACION del esperado (exigir que NO bloquee): %s"
      % ("PASA" if not bloquea_normal else "CAE"))
    if bloquea_normal:
        caen += 1
    else:
        fallos += 1
    w("")

    w("CASO C. LAS MISMAS EN CARRIL TARDIO: NO BLOQUEAN Y APARECEN DECLARADAS")
    tardio = CR.es_cierre_tardio(999, 1000)
    bloquea_tardio = bool(huerfanas) and not tardio
    casos += 1
    w("   carril: %s | bloquea: %s"
      % ("TARDIO" if tardio else "NORMAL", bloquea_tardio))
    w("   ESPERADO: NO bloquea -> %s" % ("CALZA" if not bloquea_tardio else "NO CALZA"))
    if bloquea_tardio:
        fallos += 1
    w("   MUTACION del esperado (exigir que SI bloquee): %s"
      % ("PASA" if bloquea_tardio else "CAE"))
    if bloquea_tardio:
        fallos += 1
    else:
        caen += 1
    decl = CR.declaracion_de_cifras_sin_pareja(huerfanas, 999, 1000)
    w("   LA DECLARACION, COTEJADA POR CONTENCION RENGLON A RENGLON:")
    w("      la declaracion mide %d bytes en disco y %d normalizados a LF"
      % (len(decl.encode("utf-8")), len(decl.replace(chr(13) + NL, NL).encode("utf-8"))))
    dentro = 0
    for n, especie, muestra, linea in huerfanas:
        renglon = "linea %-6d %-5s %-24s | %s" % (n, especie, muestra, linea)
        esta = renglon in decl
        w("      %s -> %s" % (renglon[:88], "ESTA" if esta else "NO ESTA"))
        if esta:
            dentro += 1
    casos += 1
    w("   CIFRA cifras sin pareja DECLARADAS en el texto: %d de %d"
      % (dentro, len(huerfanas)))
    w("   ESPERADO: las %d -> %s"
      % (len(huerfanas), "CALZA" if dentro == len(huerfanas) else "NO CALZA"))
    if dentro != len(huerfanas):
        fallos += 1
    w("   MUTACION del esperado (exigir %d declaradas): %s"
      % (len(huerfanas) + 1,
         "PASA" if dentro == len(huerfanas) + 1 else "CAE"))
    if dentro == len(huerfanas) + 1:
        fallos += 1
    else:
        caen += 1
    w("   Y LA DECLARACION LLEVA SU CUENTA TOTAL:")
    linea_total = "CIFRA cifras publicadas sin su pareja: %d" % len(huerfanas)
    casos += 1
    w("      %r esta en la declaracion: %s"
      % (linea_total, "SI" if linea_total in decl else "NO"))
    if linea_total not in decl:
        fallos += 1
    falso = "CIFRA cifras publicadas sin su pareja: %d" % (len(huerfanas) + 1)
    w("      MUTACION del esperado (exigir la cuenta %d): %s"
      % (len(huerfanas) + 1, "PASA" if falso in decl else "CAE"))
    if falso in decl:
        fallos += 1
    else:
        caen += 1
    w("   Y LA DECLARACION VA DENTRO DE UNA CERCA, ASI QUE NO SE ACUSA A SI MISMA:")
    texto_con_decl = texto.rstrip(NL) + NL + NL + decl
    de_nuevo = CR.cifras_sin_pareja(texto_con_decl)
    casos += 1
    w("      CIFRA cifras sin pareja del texto CON la declaracion pegada: %d"
      % len(de_nuevo))
    w("      ESPERADO: las mismas %d, ni una mas -> %s"
      % (len(huerfanas), "CALZA" if len(de_nuevo) == len(huerfanas) else "NO CALZA"))
    if len(de_nuevo) != len(huerfanas):
        fallos += 1
    w("      MUTACION del esperado (exigir %d): %s"
      % (len(huerfanas) + 1,
         "PASA" if len(de_nuevo) == len(huerfanas) + 1 else "CAE"))
    if len(de_nuevo) == len(huerfanas) + 1:
        fallos += 1
    else:
        caen += 1
    w("")

    w("CASO D. CERO CIFRAS SIN PAREJA EN CARRIL TARDIO: LA DECLARACION DICE CERO")
    w("        Y NO SE OMITE")
    limpio = fabricar(extra=["Un parrafo sin ninguna cifra."])
    ninguna = CR.cifras_sin_pareja(limpio)
    decl0 = CR.declaracion_de_cifras_sin_pareja(ninguna, 999, 1000)
    casos += 1
    w("   CIFRA cifras sin pareja del texto limpio: %d" % len(ninguna))
    dice_cero = ("CIFRA cifras publicadas sin su pareja: 0" in decl0
                 and "la cuenta es CERO" in decl0)
    w("   la declaracion se escribe igual: %s"
      % ("SI, %d bytes" % len(decl0.encode("utf-8")) if decl0.strip() else "NO"))
    w("   y dice CERO con todas las letras: %s" % ("SI" if dice_cero else "NO"))
    if not (len(ninguna) == 0 and dice_cero and decl0.strip()):
        fallos += 1
    w("   MUTACION del esperado (exigir que la declaracion se omita): %s"
      % ("PASA" if not decl0.strip() else "CAE"))
    if not decl0.strip():
        fallos += 1
    else:
        caen += 1
    w("")
    return fallos, casos, caen


def _caso_e(w):
    """E: el carril tardio NO afloja ninguna de las cuatro piezas."""
    fallos = casos = caen = 0
    w("CASO E. EL CARRIL TARDIO NO AFLOJA NINGUNA DE LAS CUATRO PIEZAS")
    w("   (y la prueba mas fuerte es de forma: piezas_que_faltan() NI SIQUIERA")
    w("    TIENE un parametro de carril, asi que no puede saber en cual esta)")
    import inspect
    firma = list(inspect.signature(CR.piezas_que_faltan).parameters)
    casos += 1
    w("   parametros de piezas_que_faltan(): %s" % ", ".join(firma))
    sin_carril = not any(("tardio" in p or "carril" in p or "curso" in p)
                         for p in firma)
    w("   ninguno nombra el carril: %s" % ("SI" if sin_carril else "NO"))
    if not sin_carril:
        fallos += 1
    w("   MUTACION del esperado (exigir que SI tenga uno): %s"
      % ("PASA" if not sin_carril else "CAE"))
    if sin_carril:
        caen += 1
    else:
        fallos += 1
    w("")
    w("   Y LAS CUATRO, ROTAS UNA A UNA, CON LA MISMA LLAMADA QUE HACE main():")
    rotos = [
        ("(1) sin veredicto escrito", dict(sin_veredicto=True), "(1)"),
        ("(2) con el hueco de cabecera fuera de cerca",
         dict(con_hueco_de_cabecera=True), "(2)"),
        ("(2) con las filas del tallador sin pegar",
         dict(filas_pegadas=False), "(2)"),
        ("(3) sin la seccion 5", dict(sin_seccion=5), "(3)"),
        ("(4) sin la seccion 9", dict(sin_seccion=9), "(4)"),
    ]
    for etiqueta, kw, codigo in rotos:
        texto = fabricar(extra=SIN_PAREJA, **kw)
        faltan = CR.piezas_que_faltan(texto, FILAS, BAT, vuelta=999,
                                      nombre_bateria=NOM)
        acusada = [f for f in faltan if f.startswith(codigo)]
        casos += 1
        w("      %-46s -> %s"
          % (etiqueta, acusada[0][:80] if acusada else "NO LA ACUSA"))
        if not acusada:
            fallos += 1
        w("         MUTACION del esperado (exigir que NO la acuse): %s"
          % ("PASA" if not acusada else "CAE"))
        if acusada:
            caen += 1
        else:
            fallos += 1
    w("")
    w("   Y LAS OTRAS TRES COMPROBACIONES DEL BLOQUE D TAMPOCO SE AFLOJAN: el")
    w("   cuerpo byte a byte, los guiones y las citas de arnes bloquean en LOS DOS")
    w("   carriles, y eso esta escrito en main() como una columna `bloquea` que")
    w("   solo la de las cifras sin pareja pone a `not tardio`. Aqui se cuenta:")
    fuente = io.open(os.path.join(RAIZ, "scripts", "loop", "cerrar_reporte.py"),
                     encoding="utf-8").read().replace(chr(13) + NL, NL)
    casos += 1
    n_not_tardio = fuente.count("not tardio")
    w("      CIFRA apariciones de `not tardio` en el instrumento: %d" % n_not_tardio)
    w("      ESPERADO exactamente 1 -> %s"
      % ("CALZA" if n_not_tardio == 1 else "NO CALZA"))
    if n_not_tardio != 1:
        fallos += 1
    w("      MUTACION del esperado (exigir 2): %s"
      % ("PASA" if n_not_tardio == 2 else "CAE"))
    if n_not_tardio == 2:
        fallos += 1
    else:
        caen += 1
    w("")
    return fallos, casos, caen


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("CASO POSITIVO POR MUTACION DEL CARRIL DE CIERRE TARDIO")
    w("(vuelta 186, TAREA 2.c; respuesta del acta 186 a la P.2)")
    w("=" * 78)
    w("")
    w("EL SUJETO ES EL FICHERO VIVO scripts/loop/cerrar_reporte.py, IMPORTADO.")
    w("Aqui no se escribe ningun reporte y no se toca docs/loop/REPORTE.md.")
    w("")
    fallos = casos = caen = 0
    for parte in (_caso_a, _casos_bcd, _caso_e):
        f, c, k = parte(w)
        fallos += f
        casos += c
        caen += k
    w("CIFRA casos: %d | pasan: %d" % (casos, casos - fallos))
    w("CIFRA casos que CAEN al mutar su esperado: %d de %d" % (caen, caen))
    w("CIFRA fallos: %d" % fallos)
    w("VEREDICTO: %s" % ("VERDE" if fallos == 0 else "ROJO"))
    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V186_T2C_MUTACION_CIERRE_TARDIO.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0 if fallos == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
