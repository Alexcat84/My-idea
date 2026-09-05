# -*- coding: utf-8 -*-
r"""vuelta179_tarea1b_mutacion_citas.py . EL CASO POSITIVO POR MUTACION DE LA
GUARDA DE LA CITA DE ARNES (vuelta 179, TAREA 1.b).

QUE PRUEBA. `cerrar_reporte.citas_de_arnes_que_no_calzan()` y sus dos hermanas
puras, `emparejar_citas()` y `cifra_propia_del_arnes()`. Todas reciben el texto y
UN LECTOR, asi que este arnes NO TOCA EL REPO EN NINGUN CASO: fabrica el reporte
y fabrica los ficheros de salida en un diccionario.

EL CASO QUE LO DECIDE TODO, Y ES EL QUE EL ENCARGO NOMBRA: un reporte fabricado
que publica 16 junto a un fichero fabricado que dice 18 tiene que salir ROJO
NOMBRANDO LAS DOS CIFRAS; el mismo con 18 y 18 tiene que salir VERDE.

LA MUTACION, QUE ES LO QUE HACE QUE ESTO SEA UNA PRUEBA Y NO UNA AFIRMACION
(`EJECUTOR.md` 1, EL CASO ROJO SE PRUEBA POR MUTACION): de cada caso se mueve EL
VALOR ESPERADO y se comprueba que el caso CAE. Un `assert` que compara un literal
consigo mismo no puede fallar nunca, y eso ya costo una caida en la vuelta 89.

USO:
  python scripts/loop/vuelta179_tarea1b_mutacion_citas.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cerrar_reporte as CR   # noqa: E402

NL = chr(10)


def lector(mapa):
    """UN LECTOR FABRICADO. Devuelve None si el nombre no esta en el mapa (el
    fichero no existe) y lo que diga el mapa si esta, incluida la cadena vacia
    (el fichero de cero bytes)."""
    return lambda nombre: mapa.get(nombre)


def rojas(texto, mapa):
    return [c for c in CR.citas_de_arnes_que_no_calzan(texto, lector(mapa))
            if not c[4].startswith("SIN COTEJO")]


def sin_cotejo(texto, mapa):
    return [c for c in CR.citas_de_arnes_que_no_calzan(texto, lector(mapa))
            if c[4].startswith("SIN COTEJO")]


# ---------------------------------------------------------------- LOS SUJETOS
FICH_18 = ("VERDE DE LA MUTACION" + NL +
           "   CIFRA casos: 18 | pasan: 18 | fallan: 0" + NL +
           "   CIFRA casos que CAEN: 18 de 18" + NL)
FICH_16 = ("   CIFRA casos: 16 | pasan: 16 | fallan: 0" + NL +
           "   CIFRA casos que CAEN: 16 de 16" + NL)
FICH_SOLO_CAEN = "   CIFRA casos que CAEN: 7 de 9" + NL
FICH_MUDO = "el arnes corrio y no dice cuantos casos son" + NL

REP_16 = ("# REPORTE DE LA VUELTA 900" + NL + NL +
          "**Su arnes** es `scripts/loop/vuelta900_mutacion.py`" + NL +
          "(`docs/loop/SALIDA_V900_MUTACION.txt`), **16 casos, los 16 pasan y los 16" + NL +
          "CAEN**, y prueba las dos guardas." + NL)
REP_18 = REP_16.replace("16 casos, los 16 pasan y los 16", "18 casos, los 18 pasan y los 18")

# EL PARRAFO DE DOS CIFRAS Y UN SOLO FICHERO, copiado en su forma del sujeto real
# (`REPORTE_V178.md`, lineas 239 a 241): la cifra que va con el fichero es la
# SEGUNDA, y emparejar por parrafo entero acusaria a la primera.
REP_DOS_CIFRAS = ("# REPORTE DE LA VUELTA 900" + NL + NL +
                  "El arnes da **20 casos, los 20 pasan y los 20 CAEN**." + NL +
                  "**Y EL ARNES VIEJO NO SE TOCO:** `vuelta899_mutacion.py`" + NL +
                  "da **28 casos, los 28 pasan y los 28 caen** (`docs/loop/SALIDA_V900_MUTACION.txt`)." + NL)

# LA FORMA QUE NO REPITE LA PALABRA `casos`, copiada de la linea 188 del sujeto
# real, que es la que hizo que la primera version de esta guarda inventara un
# rojo. La cifra que va con el fichero es la 8, no la 5.
REP_SIN_LA_PALABRA = ("# REPORTE DE LA VUELTA 900" + NL + NL +
                      "La prueba de la nomina de la propia bateria" + NL +
                      "pasa de 5 casos a **8, los 8 pasan y los 8 caen**" + NL +
                      "(`docs/loop/SALIDA_V900_MUTACION.txt`), y su caso `E` se re-fundo." + NL)

REP_CERCADO = ("# REPORTE DE LA VUELTA 900" + NL + NL +
               "```" + NL +
               "**16 casos, los 16 pasan y los 16 CAEN** (`docs/loop/SALIDA_V900_MUTACION.txt`)" + NL +
               "```" + NL)

REP_LEJOS = ("# REPORTE DE LA VUELTA 900" + NL + NL +
             "El arnes da **16 casos, los 16 pasan y los 16 CAEN**, y ademas " +
             ("relleno que separa la cifra del fichero mas alla de la ventana. " * 4) +
             "El fichero es `docs/loop/SALIDA_V900_MUTACION.txt`." + NL)

REP_SIN_CIFRA = ("# REPORTE DE LA VUELTA 900" + NL + NL +
                 "La salida cruda vive en `docs/loop/SALIDA_V900_MUTACION.txt` y no se" + NL +
                 "publica aqui ninguna cifra de casos." + NL)

# EL MISMO 16 CONTRA 18, PERO DENTRO DE UNA CORRECCION DECLARADA. La casa OBLIGA
# a escribir la cifra equivocada al lado de su fichero (`EJECUTOR.md` 8, una
# correccion que tapa lo que corrige no se puede auditar), y sin la exencion la
# guarda acusaria al reporte por hacer lo que la doctrina manda. LO DESTAPO LA
# PROPIA GUARDA al cerrar el reporte de la vuelta 179, que es el que la estrena.
REP_CORRECCION = ("# REPORTE DE LA VUELTA 900" + NL + NL +
                  "CORRECCION DECLARADA. La vuelta 899 publico **16 casos** citando" + NL +
                  "`docs/loop/SALIDA_V900_MUTACION.txt`, y ese fichero, contado, dice 18." + NL)

# Y EL MISMO SIN DECIR LAS PALABRAS: tiene que seguir siendo ROJO. Una exencion
# que se coge sin declararla seria un agujero.
REP_CORRECCION_MUDA = REP_CORRECCION.replace("CORRECCION DECLARADA. ", "")

MAPA = {"SALIDA_V900_MUTACION.txt": FICH_18}
MAPA_16 = {"SALIDA_V900_MUTACION.txt": FICH_16}
MAPA_8 = {"SALIDA_V900_MUTACION.txt": "   CIFRA casos: 8 | pasan: 8 | fallan: 0" + NL}
MAPA_28 = {"SALIDA_V900_MUTACION.txt": "   CIFRA casos: 28 | pasan: 28 | fallan: 0" + NL}
MAPA_VACIO = {"SALIDA_V900_MUTACION.txt": ""}
MAPA_MUDO = {"SALIDA_V900_MUTACION.txt": FICH_MUDO}


# ------------------------------------------------------------------ LOS CASOS
# Cada caso es (nombre, funcion_que_mide, valor_esperado). La funcion NO recibe
# el esperado: se mide primero y se compara despues, para que mover el esperado
# tumbe el caso de verdad.
CASOS = [
    ("A_el_caso_que_lo_decide_16_contra_18_es_ROJO",
     lambda: len(rojas(REP_16, MAPA)), 1),
    ("A_y_nombra_LAS_DOS_cifras",
     lambda: (rojas(REP_16, MAPA)[0][2], rojas(REP_16, MAPA)[0][3]), (16, 18)),
    ("A_y_nombra_el_fichero",
     lambda: rojas(REP_16, MAPA)[0][1], "SALIDA_V900_MUTACION.txt"),
    ("A_y_nombra_la_linea_en_que_esta_la_ruta",
     lambda: rojas(REP_16, MAPA)[0][0], 4),
    ("B_el_mismo_con_18_contra_18_es_VERDE",
     lambda: len(rojas(REP_18, MAPA)), 0),
    ("B_y_16_contra_16_tambien_es_VERDE",
     lambda: len(rojas(REP_16, MAPA_16)), 0),
    ("C_el_fichero_que_NO_EXISTE_es_ROJO",
     lambda: len(rojas(REP_16, {})), 1),
    ("C_y_el_motivo_lo_dice",
     lambda: "NO EXISTE" in rojas(REP_16, {})[0][4], True),
    ("D_el_fichero_de_CERO_BYTES_es_ROJO",
     lambda: len(rojas(REP_16, MAPA_VACIO)), 1),
    ("D_y_el_motivo_lo_dice",
     lambda: "CERO BYTES" in rojas(REP_16, MAPA_VACIO)[0][4], True),
    ("L_la_CORRECCION_DECLARADA_no_es_rojo",
     lambda: len(rojas(REP_CORRECCION, MAPA)), 0),
    ("L_pero_SI_se_publica_como_SIN_COTEJO",
     lambda: len(sin_cotejo(REP_CORRECCION, MAPA)), 1),
    ("L_y_nombra_LAS_DOS_cifras_igual",
     lambda: (sin_cotejo(REP_CORRECCION, MAPA)[0][2],
              sin_cotejo(REP_CORRECCION, MAPA)[0][3]), (16, 18)),
    ("L_SIN_DECIR_LAS_PALABRAS_VUELVE_A_SER_ROJO",
     lambda: len(rojas(REP_CORRECCION_MUDA, MAPA)), 1),
    ("E_el_fichero_mudo_NO_es_rojo_sino_SIN_COTEJO",
     lambda: (len(rojas(REP_16, MAPA_MUDO)), len(sin_cotejo(REP_16, MAPA_MUDO))), (0, 1)),
    ("F_dos_cifras_y_un_fichero_se_empareja_con_la_SUYA",
     lambda: len(rojas(REP_DOS_CIFRAS, MAPA_28)), 0),
    ("F_y_si_el_fichero_dijera_20_ese_mismo_parrafo_CAE",
     lambda: len(rojas(REP_DOS_CIFRAS, {"SALIDA_V900_MUTACION.txt":
                                        "   CIFRA casos: 20 | pasan: 20 | fallan: 0" + NL})), 1),
    ("G_la_forma_que_no_repite_la_palabra_casos_se_caza",
     lambda: len(rojas(REP_SIN_LA_PALABRA, MAPA_8)), 0),
    ("G_y_ES_LA_8_LA_QUE_SE_EMPAREJA_Y_NO_LA_5",
     lambda: CR.emparejar_citas(" ".join(REP_SIN_LA_PALABRA.split(NL)[2:5]))[0][0], 8),
    ("H_el_bloque_cercado_queda_fuera",
     lambda: len(CR.citas_de_arnes_que_no_calzan(REP_CERCADO, lector(MAPA))), 0),
    ("I_mas_alla_de_la_ventana_no_se_empareja",
     lambda: len(CR.citas_de_arnes_que_no_calzan(REP_LEJOS, lector(MAPA))), 0),
    ("J_un_fichero_citado_sin_cifra_de_casos_no_se_mira",
     lambda: len(CR.citas_de_arnes_que_no_calzan(REP_SIN_CIFRA, lector(MAPA))), 0),
    ("K_la_cifra_propia_sale_de_CIFRA_casos",
     lambda: CR.cifra_propia_del_arnes(FICH_18)[0], 18),
    ("K_y_de_CIFRA_casos_que_CAEN_sale_el_TOTAL_y_no_los_que_caen",
     lambda: CR.cifra_propia_del_arnes(FICH_SOLO_CAEN)[0], 9),
    ("K_y_de_un_fichero_mudo_sale_None",
     lambda: CR.cifra_propia_del_arnes(FICH_MUDO)[0], None),
]


def main():
    print("=" * 78)
    print("CASO POSITIVO POR MUTACION: LA GUARDA DE LA CITA DE ARNES (179, 1.b)")
    print("=" * 78)
    print("")
    print("NADA SALE DEL REPO: los reportes y los ficheros de salida son fabricados,")
    print("y el lector es un diccionario. La funcion juzgada es PURA.")
    print("")

    print("A) LOS CASOS, CORRIDOS")
    fallan = 0
    for nombre, fn, esperado in CASOS:
        try:
            visto = fn()
        except Exception as e:
            visto = "EXCEPCION %r" % (e,)
        ok = visto == esperado
        if not ok:
            fallan += 1
        print("   %-52s %s  visto=%r esperado=%r"
              % (nombre[:52], "pasa " if ok else "FALLA", visto, esperado))
    print("   CIFRA casos: %d | pasan: %d | fallan: %d"
          % (len(CASOS), len(CASOS) - fallan, fallan))
    print("")

    print("B) LA MUTACION: A CADA CASO SE LE MUEVE EL VALOR ESPERADO Y TIENE QUE CAER")
    caen = 0
    for nombre, fn, esperado in CASOS:
        if isinstance(esperado, bool):
            mutado = not esperado
        elif isinstance(esperado, int):
            mutado = esperado + 1
        elif isinstance(esperado, tuple):
            mutado = tuple(list(esperado)[::-1]) if len(set(esperado)) > 1 else (99, 99)
        elif esperado is None:
            mutado = 0
        else:
            mutado = str(esperado) + "_MUTADO"
        try:
            visto = fn()
        except Exception as e:
            visto = "EXCEPCION %r" % (e,)
        cae = visto != mutado
        if cae:
            caen += 1
        print("   %-52s %s" % (nombre[:52], "CAE" if cae else "NO CAE, Y ESO ES ROJO"))
    print("   CIFRA casos que CAEN: %d de %d" % (caen, len(CASOS)))
    print("")

    if fallan or caen != len(CASOS):
        print("ROJO DE LA MUTACION: %d caso(s) fallan y %d de %d caen."
              % (fallan, caen, len(CASOS)))
        return 1
    print("VERDE DE LA MUTACION: %d casos, los %d pasan y los %d CAEN al mutarles "
          "el valor esperado. La guarda caza el 16 contra 18 nombrando las dos "
          "cifras, deja pasar el 18 contra 18, cae en rojo con el fichero que no "
          "existe y con el de cero bytes, NO inventa un rojo cuando el parrafo "
          "trae dos cifras y un solo fichero, caza la forma que no repite la "
          "palabra casos, no entra en los bloques cercados y no empareja mas alla "
          "de su ventana." % (len(CASOS), len(CASOS), len(CASOS)))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
