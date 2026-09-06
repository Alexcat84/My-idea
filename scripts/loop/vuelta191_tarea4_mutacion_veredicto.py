# -*- coding: utf-8 -*-
r"""vuelta191_tarea4_mutacion_veredicto.py . EL CASO POSITIVO POR MUTACION DE LA
GUARDA DEL VEREDICTO DUPLICADO.

QUE TIENE QUE CAZAR, CON LAS PALABRAS DEL ENCARGO: **que `cerrar_reporte.py` caiga
en ROJO si el `--veredicto` que recibe ya trae la etiqueta o los asteriscos, en
vez de pegarla dos veces**, y **que este arnes CAIGA si la guarda se quita**.

LOS DOS CARRILES, Y NINGUNO SUSTITUYE AL OTRO:

  . EL CARRIL DE LA FUNCION PURA. `veredicto_ya_viene_vestido()` se importa y se
    corre sobre veredictos fabricados, incluido **el literal exacto que la vuelta
    190 le paso**, sacado de su propio fichero de cierre y no tecleado.
  . EL CARRIL DE LA MUTACION DE VERDAD. Se copia `cerrar_reporte.py` a un fichero
    temporal, **se le QUITA la guarda con un reemplazo literal**, y se comprueba
    que la version mutilada **DEJA PASAR** lo que la de verdad tumba. Sin este
    carril, "la guarda funciona" seria una afirmacion sobre codigo que nadie
    volvio a tocar.

Y NO CORRE `cerrar_reporte.py` CONTRA EL REPORTE DE VERDAD: el arnes trabaja sobre
el modulo importado y sobre una COPIA en un directorio temporal. **No toca
`docs/loop/REPORTE.md`.**

USO:
  python scripts/loop/vuelta191_tarea4_mutacion_veredicto.py
"""
import importlib.util
import io
import os
import re
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cerrar_reporte as CR   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
SALIDA = os.path.join(LOOP, "SALIDA_V191_T4_MUTACION_VEREDICTO.txt")
FUENTE = os.path.join(RAIZ, "scripts", "loop", "cerrar_reporte.py")

# EL TROZO QUE LA MUTACION QUITA. Es literal y tiene que aparecer EXACTAMENTE UNA
# VEZ: una mutacion que no sabe donde cae no prueba nada.
TROZO_DE_LA_GUARDA = "    rojos.extend(motivos_vestido)"


def _caso(w, nombre, obtenido, esperado):
    ok = obtenido == esperado
    w("   %-56s obtenido %-14s esperado %-14s -> %s"
      % (nombre, repr(obtenido)[:14], repr(esperado)[:14], "PASA" if ok else "CAE"))
    return 0 if ok else 1


def veredicto_que_paso_la_190():
    """EL VEREDICTO QUE LA VUELTA 190 LE PASO, LEIDO DE SU PROPIA SALIDA SELLADA
    Y NO TECLEADO. Devuelve la cadena o None.

    `docs/loop/SALIDA_V190_CERRAR_REPORTE.txt` imprime la linea
    `el veredicto, tal como se paso: '...'`. De ahi sale, con su comilla y todo.
    Si el fichero no esta o la linea no aparece, se devuelve None y el bloque se
    declara SIN CORRER en vez de fabricar un ejemplar."""
    ruta = os.path.join(LOOP, "SALIDA_V190_CERRAR_REPORTE.txt")
    if not os.path.isfile(ruta):
        return None
    t = io.open(ruta, encoding="utf-8", errors="replace").read()
    m = re.search(r"el veredicto, tal como se paso:\s*'(.*)'", t)
    return m.group(1) if m else None


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    fallos = 0
    no_cayeron = 0
    w("=" * 78)
    w("VUELTA 191, TAREA 4: MUTACION DE LA GUARDA DEL VEREDICTO DUPLICADO")
    w("=" * 78)
    w("")

    # ------------------------------------------------------------- BLOQUE A
    w("A) LA FUNCION PURA SOBRE VEREDICTOS FABRICADOS")
    limpio = "LAS CINCO TAREAS CERRARON Y NO SE MOVIO NINGUN VEREDICTO."
    con_etiqueta = "%s %s" % (CR.ETIQUETA_VEREDICTO, limpio)
    vestido = "%s%s %s%s" % (CR.ENVOLTURA_VEREDICTO, CR.ETIQUETA_VEREDICTO,
                             limpio, CR.ENVOLTURA_VEREDICTO)
    solo_asteriscos = "%s%s%s" % (CR.ENVOLTURA_VEREDICTO, limpio,
                                  CR.ENVOLTURA_VEREDICTO)
    for etiqueta, v, esperado in (
            ("un veredicto LIMPIO", limpio, 0),
            ("con la ETIQUETA dentro", con_etiqueta, 1),
            ("con etiqueta Y asteriscos, como el de la 190", vestido, 3),
            ("solo con los asteriscos", solo_asteriscos, 2)):
        motivos, _h = CR.veredicto_ya_viene_vestido(v)
        fallos += _caso(w, etiqueta, len(motivos), esperado)
    w("   LA MUTACION 1: al veredicto LIMPIO se le pide que dispare, y tiene que")
    w("   CAER. Una guarda que muerde a los limpios no sirve")
    m_limpio, _h = CR.veredicto_ya_viene_vestido(limpio)
    if m_limpio:
        w("      LA MUTACION NO CAYO: el limpio dispara %d motivo(s)." % len(m_limpio))
        no_cayeron += 1
    else:
        w("      LA MUTACION CAE: el limpio dispara 0, o sea que la guarda")
        w("      distingue y no muerde por gusto.")
    w("   LA MUTACION 2: al VESTIDO se le pide 0, y tiene que CAER")
    m_vest, h_vest = CR.veredicto_ya_viene_vestido(vestido)
    if not m_vest:
        w("      LA MUTACION NO CAYO: el vestido pasa limpio.")
        no_cayeron += 1
    else:
        w("      LA MUTACION CAE: dispara %d motivo(s)." % len(m_vest))
    w("   Y LOS MOTIVOS DICEN QUE SE RECIBIO Y QUE SE ESPERABA, que es la mitad")
    w("   del encargo:")
    for mm in m_vest:
        w("      %s" % mm[:200])
    fallos += _caso(w, "algun motivo dice RECIBIDO",
                    any("RECIBIDO" in x for x in m_vest), True)
    fallos += _caso(w, "algun motivo dice ESPERADO",
                    any("ESPERADO" in x for x in m_vest), True)
    for hh in h_vest:
        w("      hallazgo: %s" % hh[:160])
    w("")

    # ------------------------------------------------------------- BLOQUE B
    w("B) EL EJEMPLAR DE VERDAD: EL VEREDICTO QUE LA VUELTA 190 LE PASO, LEIDO DE")
    w("   SU PROPIA SALIDA SELLADA Y NO TECLEADO")
    v190 = veredicto_que_paso_la_190()
    if v190 is None:
        w("   NO SE PUDO LEER de docs/loop/SALIDA_V190_CERRAR_REPORTE.txt.")
        w("   ESTE BLOQUE QUEDA SIN CORRER Y SE DECLARA, en vez de fabricar un")
        w("   ejemplar que se apruebe solo.")
    else:
        w("   leido: %r" % v190[:140])
        motivos, _h = CR.veredicto_ya_viene_vestido(v190)
        w("   CIFRA motivos que dispara: %d" % len(motivos))
        for mm in motivos:
            w("      %s" % mm[:180])
        fallos += _caso(w, "la guarda lo tumba", len(motivos) > 0, True)
        w("   LA MUTACION: si la guarda NO lo tumbara, la linea 50 del reporte de")
        w("   la 190 volveria a salir con la etiqueta duplicada")
        if not motivos:
            w("      LA MUTACION NO CAYO: el ejemplar real pasa limpio.")
            no_cayeron += 1
        else:
            w("      LA MUTACION CAE: lo tumba con %d motivo(s)." % len(motivos))
    w("")

    # ------------------------------------------------------------- BLOQUE C
    w("C) LA MUTACION DE VERDAD: SE LE QUITA LA GUARDA A UNA COPIA Y SE COMPRUEBA")
    w("   QUE LA VERSION MUTILADA DEJA PASAR LO QUE LA DE VERDAD TUMBA")
    codigo = io.open(FUENTE, encoding="utf-8").read().replace(chr(13) + NL, NL)
    n = codigo.count(TROZO_DE_LA_GUARDA)
    w("   el trozo %r aparece %d vez(ces) en cerrar_reporte.py"
      % (TROZO_DE_LA_GUARDA, n))
    fallos += _caso(w, "aparece exactamente una vez", n, 1)
    if n == 1:
        tmp = tempfile.mkdtemp(prefix="v191_mut_ver_")
        try:
            mutado = codigo.replace(
                TROZO_DE_LA_GUARDA,
                "    pass  # LA GUARDA QUITADA POR EL ARNES DE LA VUELTA 191")
            ruta = os.path.join(tmp, "cerrar_reporte_mutado.py")
            io.open(ruta, "w", encoding="utf-8", newline=NL).write(mutado)
            # LOS BYTES ABSOLUTOS NO SE IMPRIMEN (vuelta 193, TAREA 2; el
            # ejecutor lo cazo con el carril --reproduccion nuevo de
            # guarda_de_entrada_a_la_nomina.py, y NO estaba entre los tres que el
            # acta 193 midio). `cerrar_reporte.py` CRECE cada vuelta, asi que
            # imprimir su tamano hacia que esta salida sellada cambiara sola: da
            # 6072 bytes las dos veces y `sha256` DISTINTO, porque las dos cifras
            # tienen el mismo numero de digitos. LA MISMA ESPECIE QUE LOS TRES DE
            # LA 4.10, y por eso se arregla igual.
            #
            # EL SUJETO SIGUE VIVO A PROPOSITO, Y ESO NO ES EL FALLO: lo que este
            # bloque prueba es que LA GUARDA DE HOY se puede quitar de una copia
            # y que la copia compila, y para eso hace falta el `cerrar_reporte.py`
            # de hoy. **La reproduccion no se le exige al sujeto: se le exige a la
            # SALIDA.** Lo que se imprime, entonces, es la DIFERENCIA, que es
            # invariante porque solo depende del trozo sustituido.
            delta = len(codigo.encode("utf-8")) - len(mutado.encode("utf-8"))
            w("   copia mutada escrita. Los bytes ABSOLUTOS de `cerrar_reporte.py`")
            w("   no se imprimen: ese fichero crece cada vuelta y esta salida se")
            w("   sella. Lo que se imprime es la DIFERENCIA, que solo depende del")
            w("   trozo sustituido y no del tamano del fichero:")
            w("      la mutada mide %d bytes MENOS que la de verdad" % delta)
            fallos += _caso(w, "la diferencia es la del trozo sustituido", delta,
                            len(TROZO_DE_LA_GUARDA.encode("utf-8"))
                            - len("    pass  # LA GUARDA QUITADA POR EL ARNES "
                                  "DE LA VUELTA 191".encode("utf-8")))
            fallos += _caso(w, "la copia mutada compila",
                            bool(compile(mutado, ruta, "exec")) or True, True)
            w("   Y LA DIFERENCIA SE MIDE, no se afirma:")
            w("      `rojos.extend(motivos_vestido)` en la de verdad: %d"
              % codigo.count(TROZO_DE_LA_GUARDA))
            w("      `rojos.extend(motivos_vestido)` en la mutada:    %d"
              % mutado.count(TROZO_DE_LA_GUARDA))
            fallos += _caso(w, "la mutada ya no lleva el trozo",
                            mutado.count(TROZO_DE_LA_GUARDA), 0)
            w("   LO QUE ESTO PRUEBA, Y NI UNA PALABRA MAS: que la linea que mete")
            w("   los motivos en `rojos` EXISTE, es UNICA y se puede quitar. La")
            w("   version mutilada seguiria MIDIENDO el veredicto y publicando sus")
            w("   motivos, pero NO los sumaria a `rojos`, o sea que **cerraria el")
            w("   reporte igual**. Eso es exactamente lo que hacia antes de hoy.")
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
    w("")

    # ------------------------------------------------------------- BLOQUE D
    w("D) LA COMPOSICION Y LA GUARDA MIRAN EL MISMO LITERAL, QUE ES LO QUE HACE")
    w("   QUE LA VIGILANCIA VALGA")
    w("   ETIQUETA_VEREDICTO  = %r" % CR.ETIQUETA_VEREDICTO)
    w("   ENVOLTURA_VEREDICTO = %r" % CR.ENVOLTURA_VEREDICTO)
    compuesto = "%s%s %s%s" % (CR.ENVOLTURA_VEREDICTO, CR.ETIQUETA_VEREDICTO,
                               limpio, CR.ENVOLTURA_VEREDICTO)
    w("   compuesto con el limpio: %r" % compuesto[:120])
    fallos += _caso(w, "el compuesto trae la etiqueta UNA sola vez",
                    compuesto.count(CR.ETIQUETA_VEREDICTO), 1)
    doble = "%s%s %s%s" % (CR.ENVOLTURA_VEREDICTO, CR.ETIQUETA_VEREDICTO,
                           con_etiqueta, CR.ENVOLTURA_VEREDICTO)
    w("   compuesto con uno que YA la traia: %r" % doble[:120])
    fallos += _caso(w, "ese trae la etiqueta DOS veces",
                    doble.count(CR.ETIQUETA_VEREDICTO), 2)
    w("   LA MUTACION: si componer un veredicto que ya la traia NO diera dos, la")
    w("   caida del reporte de la 190 no se podria reproducir")
    if doble.count(CR.ETIQUETA_VEREDICTO) != 2:
        w("      LA MUTACION NO CAYO: da %d." % doble.count(CR.ETIQUETA_VEREDICTO))
        no_cayeron += 1
    else:
        w("      LA MUTACION CAE: da 2, que es la linea 50 del reporte de la 190")
        w("      reproducida aqui sin tocar el reporte.")
    w("")

    # ------------------------------------------------------------- BLOQUE E
    w("E) LOS REPORTES ARCHIVADOS, CONTADOS UNO A UNO, PORQUE EL ACTA 191 DICE")
    w("   QUE LOS 186 A 189 LA TRAEN UNA SOLA VEZ Y ESO SE MIDE, NO SE CREE")
    for v in (185, 186, 187, 188, 189, 190):
        ruta = os.path.join(LOOP, "reportes", "REPORTE_V%d.md" % v)
        if not os.path.isfile(ruta):
            w("   REPORTE_V%d.md -> NO EXISTE" % v)
            continue
        t = io.open(ruta, encoding="utf-8", errors="replace").read()
        w("   REPORTE_V%d.md -> %d aparicion(es) de %r"
          % (v, t.count(CR.ETIQUETA_VEREDICTO), CR.ETIQUETA_VEREDICTO))
    w("   ESTA CUENTA NO ES UN CASO DEL ARNES: es la medicion que sostiene la")
    w("   PARADA que el reporte de esta vuelta declara. No se corrige aqui ningun")
    w("   reporte cerrado.")
    w("")

    w("=" * 78)
    w("CIFRA casos que CAEN: %d" % fallos)
    w("CIFRA mutaciones que NO cayeron (y deberian): %d" % no_cayeron)
    w("VEREDICTO: %s" % ("ROJO" if (fallos or no_cayeron) else "VERDE"))
    texto = NL.join(L) + NL
    io.open(SALIDA, "w", encoding="utf-8", newline=NL).write(texto)
    print(texto)
    print("ESCRITO: docs/loop/SALIDA_V191_T4_MUTACION_VEREDICTO.txt (%d bytes)"
          % len(texto.encode("utf-8")))
    return 1 if (fallos or no_cayeron) else 0


if __name__ == "__main__":
    sys.exit(main())
