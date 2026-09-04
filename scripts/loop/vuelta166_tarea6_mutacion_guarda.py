# -*- coding: utf-8 -*-
r"""vuelta166_tarea6_mutacion_guarda.py . CASO POSITIVO POR MUTACION DEL
ESTRECHAMIENTO DE `tallar_cifras_de_antes.py` (TAREA 6 de la vuelta 166,
adjudicacion 5.11 del acta 165), CON NOMBRE DE ARNES para que la bateria lo
vea (invoca cada arnes SIN ARGUMENTOS).

LO QUE EL ENCARGO PIDE, LITERAL: *"SE ESTRECHA EN LA FUENTE, con su caso
positivo por mutacion... el caso tiene que CAER si alguien devuelve el
vocabulario a su forma ancha."* Eso es exactamente lo que se prueba aqui: se
DEVUELVE el vocabulario a su forma ancha (se apaga el filtro de medida y se
apaga la construccion de orden) y se exige que los casos CAIGAN.

NINGUN VEREDICTO ES UNA CONSTANTE LITERAL: los casos salen de correr
`clasificar()` de verdad sobre oraciones reales del reporte de la 165 y del
de la 164, y la segunda pasada devuelve el vocabulario a su forma ancha y
comprueba que la clasificacion CAMBIA.

CERO ESCRITURAS Y CERO FICHEROS NUEVOS. La forma ancha se restaura
sustituyendo los dos patrones EN MEMORIA y devolviendolos al salir; el fichero
fuente no se toca, y al final se comprueba que sigue byte a byte igual.

USO:  python scripts/loop/vuelta166_tarea6_mutacion_guarda.py
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
import tallar_cifras_de_antes as G   # noqa: E402

FUENTE = os.path.join(RAIZ, "scripts", "loop", "tallar_cifras_de_antes.py")
R_164 = os.path.join(RAIZ, "docs", "loop", "_v166_t6", "reporte_164.md")
R_165 = os.path.join(RAIZ, "docs", "loop", "REPORTE.md")

# LA FORMA ANCHA, QUE ES LA QUE HABIA ANTES DE ESTA VUELTA: sin filtro de
# medida (todo pasa) y sin construccion de orden (nada se excluye por ella).
ANCHO_MEDIDA = re.compile(r"")
ANCHO_ORDEN = re.compile(r"(?!x)x")      # no casa nunca


def con_vocabulario_ancho(fn):
    """Devuelve el resultado de fn() con los dos patrones en su forma ancha."""
    m, o = G._RE_MEDIDA, G._RE_ORDEN_CONSTRUCCION
    G._RE_MEDIDA, G._RE_ORDEN_CONSTRUCCION = ANCHO_MEDIDA, ANCHO_ORDEN
    try:
        return fn()
    finally:
        G._RE_MEDIDA, G._RE_ORDEN_CONSTRUCCION = m, o


# LOS SUJETOS, COPIADOS LITERALES DE LOS DOS REPORTES, con lo que cada uno es.
SUJETOS = [
    ("prosa con el verbo ser, sin cifra ni estado",
     "Su caso (D) era literalmente una constante.", "sin_medida"),
    ("orden con infinitivo que la lista vieja no traia",
     "Marco los discutibles antes de saber si acierto.", "excluida"),
    ("orden con infinitivo, segunda forma",
     "Se dice antes de decirlo que no se toca nada.", "excluida"),
    ("cifra de antes de verdad, sin cita: TIENE que ser hallazgo",
     "El censo pasa de ver 92 a ver 122 sobre el mismo arbol.", "hallazgo"),
    ("estado medible de antes, sin cita: TIENE que ser hallazgo",
     "OP-L-01 no se cierra y su estado sigue en LISTA.", "hallazgo"),
    ("cifra de antes CON su cita: tiene que pasar la vara",
     "El marcador era 3.388 (`SALIDA_V166_T4_CENSO_OPERACIONES.txt`).", "ok"),
]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 166, TAREA 6: CASO POSITIVO POR MUTACION DEL ESTRECHAMIENTO")
    print("=" * 78)
    print("")
    antes_fuente = io.open(FUENTE, encoding="utf-8").read()
    casos = []

    print("A) LA FRASE DICE A QUE UNIVERSO SE REFIERE, Y SE COMPRUEBA QUE LO DICE")
    print(G.UNIVERSO)
    for palabra in ("MEDIDA", "antes de", "no se callan"):
        casos.append(("A_el_universo_nombra_%s" % palabra.replace(" ", "_"),
                      palabra in G.UNIVERSO, True))
    print("")

    print("B) CADA SUJETO, CLASIFICADO POR LA FUNCION REAL")
    for nombre, oracion, esperado in SUJETOS:
        v = G.clasificar(oracion)
        tipo = v["tipo"] if v else "no_marcada"
        print("   %-52s -> %-10s (esperado %s)" % (nombre[:52], tipo, esperado))
        casos.append(("B_%s" % nombre[:44].replace(" ", "_"), tipo, esperado))
    print("")

    print("C) LA MUTACION: SE DEVUELVE EL VOCABULARIO A SU FORMA ANCHA")
    print("   se apaga el filtro de MEDIDA y se apaga la CONSTRUCCION de orden,")
    print("   que es exactamente el estado en que la guarda estaba antes de esta")
    print("   vuelta. Los tres primeros sujetos TIENEN QUE CAER a 'hallazgo'.")
    for nombre, oracion, esperado in SUJETOS:
        ancho = con_vocabulario_ancho(lambda o=oracion: G.clasificar(o))
        tipo_a = ancho["tipo"] if ancho else "no_marcada"
        estrecho = G.clasificar(oracion)
        tipo_e = estrecho["tipo"] if estrecho else "no_marcada"
        cambia = tipo_a != tipo_e
        print("   %-52s estrecho=%-10s ancho=%-10s %s"
              % (nombre[:52], tipo_e, tipo_a, "CAE" if cambia else "no cambia"))
        if esperado in ("sin_medida", "excluida"):
            casos.append(("C_con_vocabulario_ancho_%s_cae" % nombre[:38].replace(" ", "_"),
                          tipo_a, "hallazgo"))
        else:
            casos.append(("C_%s_no_depende_del_estrechamiento" % nombre[:38].replace(" ", "_"),
                          tipo_a, tipo_e))
    print("")

    print("D) LOS DOS REPORTES ENTEROS, ESTRECHO CONTRA ANCHO")
    for etiqueta, ruta in (("164", R_164), ("165", R_165)):
        if not os.path.exists(ruta):
            print("   PARADA: no existe %s" % ruta)
            return 1
        e_exc, e_hal, e_ok, e_sin = G.verificar(ruta)
        a_exc, a_hal, a_ok, a_sin = con_vocabulario_ancho(
            lambda r=ruta: G.verificar(r))
        print("   reporte %s: ANCHO %d hallazgos | ESTRECHO %d hallazgos, "
              "%d sin medida, %d exclusiones"
              % (etiqueta, len(a_hal), len(e_hal), len(e_sin), len(e_exc)))
        casos.append(("D_el_reporte_%s_baja_al_estrechar" % etiqueta,
                      len(e_hal) < len(a_hal), True))
        casos.append(("D_el_reporte_%s_no_esconde_nada" % etiqueta,
                      len(e_hal) + len(e_sin) + len(e_ok) + len(e_exc)
                      >= len(a_hal), True))
    print("")

    print("E) LAS DOS GUARDAS HISTORICAS SIGUEN EN PIE, y esto es lo que impide")
    print("   que un estrechamiento se coma la guarda entera: el caso positivo")
    print("   de la vuelta 111 sobre el reporte de la 110 tiene que SEGUIR")
    print("   nombrando el caso O y NO nombrando el caso N.")
    r110 = os.path.join(RAIZ, "docs", "loop", "_v111_mut", "reporte_110.md")
    r110m = os.path.join(RAIZ, "docs", "loop", "_v111_mut",
                         "reporte_110_mut_casoN.md")
    if not (os.path.exists(r110) and os.path.exists(r110m)):
        print("   PARADA: faltan los ficheros historicos de la vuelta 111.")
        return 1
    _e, h110, ok110, _s = G.verificar(r110)
    _e2, h110m, _o2, _s2 = G.verificar(r110m)
    caso_o = [x for x in h110 if "Caso O" in x[1]]
    caso_n_ok = [x for x in ok110 if "Caso N" in x[1]]
    caso_n_hal = [x for x in h110m if "Caso N" in x[1]]
    print("   reporte 110: %d hallazgos | el caso O sale nombrado: %s"
          % (len(h110), bool(caso_o)))
    print("   reporte 110: el caso N pasa la vara con sus 2 citas: %s"
          % bool(caso_n_ok))
    print("   reporte 110 mutado (una cita menos al caso N): el caso N sale "
          "nombrado: %s" % bool(caso_n_hal))
    casos.append(("E_el_caso_O_sigue_nombrado", bool(caso_o), True))
    casos.append(("E_el_caso_N_limpio_sigue_pasando", bool(caso_n_ok), True))
    casos.append(("E_el_caso_N_mutado_sigue_cayendo", bool(caso_n_hal), True))
    casos.append(("E_y_el_mutado_trae_mas_hallazgos_que_el_limpio",
                  len(h110m) > len(h110), True))
    print("")
    print("F) PASADA 1, LOS CASOS TAL CUAL")
    fallos = 0
    for nombre, real, esperado in casos:
        ok = (real == esperado)
        print("   %-58s %s   (real=%r esperado=%r)"
              % (nombre[:58], "PASA" if ok else "FALLA", real, esperado))
        if not ok:
            fallos += 1
    print("   CIFRA casos: %d | pasan: %d | fallan: %d"
          % (len(casos), len(casos) - fallos, fallos))
    print("")

    print("G) PASADA 2, SE MUTA EL VALOR ESPERADO Y CADA CASO TIENE QUE CAER")
    caen = 0
    for nombre, real, esperado in casos:
        if isinstance(esperado, bool):
            mutado = not esperado
        elif isinstance(esperado, int):
            mutado = esperado + 1
        else:
            mutado = str(esperado) + "_mutado"
        cae = (real != mutado)
        print("   %-58s %s   (esperado mutado=%r)"
              % (nombre[:58], "CAE" if cae else "NO CAE", mutado))
        if cae:
            caen += 1
    print("   CIFRA casos que caen al mutar el esperado: %d de %d"
          % (caen, len(casos)))
    print("")

    print("H) Y SE COMPRUEBA QUE ESTA PRUEBA NO TOCO LA FUENTE")
    igual = (io.open(FUENTE, encoding="utf-8").read() == antes_fuente)
    print("   tallar_cifras_de_antes.py sigue byte a byte igual: %s" % igual)
    print("   los dos patrones estan restaurados: %s"
          % (G._RE_MEDIDA is not ANCHO_MEDIDA
             and G._RE_ORDEN_CONSTRUCCION is not ANCHO_ORDEN))
    if not igual:
        print("   ROJO: la prueba de mutacion escribio en la fuente.")
        return 1
    print("")

    if fallos == 0 and caen == len(casos):
        print("VERDE: los %d casos pasan tal cual y los %d caen al mutar el esperado."
              % (len(casos), len(casos)))
        return 0
    print("ROJO: fallos=%d, casos que no caen=%d" % (fallos, len(casos) - caen))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
