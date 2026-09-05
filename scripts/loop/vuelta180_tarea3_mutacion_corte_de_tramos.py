# -*- coding: utf-8 -*-
r"""vuelta180_tarea3_mutacion_corte_de_tramos.py . EL CASO POSITIVO POR MUTACION
DEL CORTE DE LA TABLA DE TRAMOS: DOS CORTES DISTINTOS CON LA MISMA CIFRA NO SE
CONFUNDEN, Y LA MISMA CIFRA CON DOS CORTES DISTINTOS TAMPOCO.

TAREA 3 de la vuelta 180. Sujetos: `sello_de_corte()` de
`scripts/loop/verificar_mutaciones_viejas.py`, con su tercer parametro nuevo, y
las funciones puras del barrido `scripts/loop/vuelta180_tarea3_barrido_de_cortes.py`.

SUJETO CONGELADO: este arnes **no toca git, no lee ningun fichero y no corre
ningun otro script**. Su sujeto son tres funciones puras y unos literales
fabricados aqui dentro.

POR QUE EXISTE, Y EL MOTIVO ES UNA MEDICION DEL FUNDADOR (seccion 6 del acta 179).
La 179 publico su tabla de tramos con `6 actos / 29 pares / 8 reales` y
`34 / 44 / 10`, **contada de su fichero y siendo verdad**; el mismo instrumento
corrido despues, dentro de la misma vuelta, dio `14 / 39 / 18` y `26 / 34 / 0`,
tambien verdad. **Las dos son ciertas y sin corte no hay manera de saber cual
mira que.** Este arnes prueba que el sello que se cablo no confunde ese caso.

Y PRUEBA UNA TERCERA CONFUSION QUE EL SELLO VIEJO SI PODIA TENER, y que aparece
justo al cablearlo fuera de la nomina: **DOS CIFRAS DISTINTAS DEL MISMO TAMANO Y
DEL MISMO CORTE**. En la corrida de hoy hay un `18` que son pares reales y un
`18` que son pares con clase escrita. Con la palabra `nomina` clavada, los dos
sellos habrian salido identicos.

LA MUTACION (`EJECUTOR.md` 1, EL CASO ROJO SE PRUEBA POR MUTACION): de cada caso
se mueve EL VALOR ESPERADO y se comprueba que el caso CAE. Ninguna variable de
veredicto es una constante literal: todas salen de llamar a la funcion.

USO:
  python scripts/loop/vuelta180_tarea3_mutacion_corte_de_tramos.py
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import verificar_mutaciones_viejas as VMV   # noqa: E402
import vuelta180_tarea3_barrido_de_cortes as BAR   # noqa: E402

S = VMV.sello_de_corte
A = "aaaaaaaaaaaa"
B = "bbbbbbbbbbbb"
NL = chr(10)

# LAS DOS CIFRAS QUE LA 179 MIDIO Y QUE EL FUNDADOR PUSO UNA AL LADO DE LA OTRA.
# Van como literales A PROPOSITO: son el escenario, no el veredicto.
REALES_ANTES = 8
REALES_DESPUES = 18

CASOS = [
    ("A_el_sello_lleva_la_cifra",
     lambda: S(REALES_DESPUES, A, "pares reales").startswith("18 "), True),
    ("A_y_lleva_el_corte_que_se_le_da",
     lambda: A in S(REALES_DESPUES, A, "pares reales"), True),
    ("A_y_dice_QUE_esta_contando",
     lambda: "pares reales" in S(REALES_DESPUES, A, "pares reales"), True),

    ("B_ES_EL_CASO_DEL_ACTA_179_la_misma_tabla_en_dos_cortes_no_se_confunde",
     lambda: S(REALES_ANTES, A, "pares reales") == S(REALES_DESPUES, B, "pares reales"),
     False),
    ("B_y_las_dos_cifras_se_leen_enteras_cada_una_con_su_corte",
     lambda: (S(REALES_ANTES, A, "pares reales").split()[0],
              S(REALES_DESPUES, B, "pares reales").split()[0]), ("8", "18")),

    ("C_LA_MISMA_CIFRA_CON_DOS_CORTES_DISTINTOS_NO_SE_CONFUNDE",
     lambda: S(REALES_DESPUES, A, "pares reales") == S(REALES_DESPUES, B, "pares reales"),
     False),
    ("C_y_la_diferencia_esta_en_el_corte_y_no_en_el_numero",
     lambda: (S(REALES_DESPUES, A, "pares reales").split()[0]
              == S(REALES_DESPUES, B, "pares reales").split()[0]), True),

    ("D_DOS_COSAS_DISTINTAS_DEL_MISMO_TAMANO_Y_MISMO_CORTE_NO_SE_CONFUNDEN",
     lambda: (S(18, A, "pares reales contados en esta corrida")
              == S(18, A, "pares con clase contados en esta corrida")), False),
    ("D_y_es_lo_que_el_sello_VIEJO_no_podia_distinguir",
     lambda: ("pares reales contados en esta corrida"
              in S(18, A, "pares reales contados en esta corrida")), True),

    ("E_el_valor_por_defecto_conserva_a_los_llamadores_viejos",
     lambda: S(105, A) == S(105, A, "nomina contada en esta corrida"), True),

    ("F_es_PURA_dos_llamadas_iguales_dan_lo_mismo",
     lambda: S(18, A, "pares reales") == S(18, A, "pares reales"), True),

    # ------------------------------------ LAS FUNCIONES PURAS DEL BARRIDO
    ("G_lleva_corte_ve_una_linea_sellada",
     lambda: BAR.lleva_corte("   CIFRA pares reales: " + S(18, A, "pares reales")), True),
    ("G_y_NO_ve_corte_donde_no_lo_hay",
     lambda: BAR.lleva_corte("   CIFRA pares reales: 18"), False),
    ("H_dice_que_no_se_mueve_reconoce_la_frase",
     lambda: BAR.dice_que_no_se_mueve(
         "   CIFRA actos medidos: 40 (NO se mueve dentro de una vuelta)"), True),
    ("H_y_no_la_ve_donde_no_esta",
     lambda: BAR.dice_que_no_se_mueve("   CIFRA actos medidos: 40"), False),
    ("I_lineas_de_cifra_recoge_las_CIFRA_y_las_filas_de_tabla",
     lambda: len(BAR.lineas_de_cifra(
         "prosa cualquiera" + NL
         + "   CIFRA algo: 12" + NL
         + "| una fila | **7** |" + NL
         + "| `un_acto` | **3** |" + NL
         + "|---|---|" + NL)), 2),
]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    p = print
    p("=" * 78)
    p("CASO POSITIVO POR MUTACION DEL CORTE DE LA TABLA DE TRAMOS (vuelta 180, 3)")
    p("=" * 78)
    p("")
    p("EL ESCENARIO, QUE ES LA MEDICION DEL FUNDADOR EN LA SECCION 6 DEL ACTA 179:")
    p("   la 179 publico %d pares reales en los actos ya leidos y el mismo" % REALES_ANTES)
    p("   instrumento dio %d despues, dentro de la misma vuelta." % REALES_DESPUES)
    p("   LAS DOS SON VERDAD. Lo que faltaba era el corte.")
    p("")

    p("A) LOS CASOS, CORRIDOS")
    fallos = 0
    for nombre, fn, esperado in CASOS:
        dado = fn()
        ok = (dado == esperado)
        p("   %-64s %s" % (nombre, "PASA" if ok else "FALLA"))
        if not ok:
            p("      esperado %r y salio %r" % (esperado, dado))
            fallos += 1
    p("   CIFRA casos: %d | fallan: %d" % (len(CASOS), fallos))
    p("")

    p("B) LA MUTACION: A CADA CASO SE LE MUEVE EL VALOR ESPERADO Y TIENE QUE CAER")
    caen = 0
    for nombre, fn, esperado in CASOS:
        if isinstance(esperado, bool):
            mutado = not esperado
        elif isinstance(esperado, tuple):
            mutado = tuple(reversed(esperado))
        elif isinstance(esperado, int):
            mutado = esperado + 1
        else:
            mutado = str(esperado) + "_MUTADO"
        cae = (fn() != mutado)
        p("   %-64s %s" % (nombre, "CAE" if cae else "NO CAE"))
        if cae:
            caen += 1
    p("   CIFRA casos que CAEN: %d de %d" % (caen, len(CASOS)))
    p("")

    p("C) LA MUTACION DE LA GUARDA DEL BARRIDO, QUE ES LA OTRA MITAD")
    p("   Se sustituye BAR.lleva_corte por una version que dice SI siempre, que es")
    p("   la forma en que esta guarda dejaria de mirar sin que nadie lo notara.")
    original = BAR.lleva_corte
    try:
        BAR.lleva_corte = lambda _l: True
        pasaria = BAR.lleva_corte("   CIFRA pares reales: 18")
    finally:
        BAR.lleva_corte = original
    p("      con la guarda tumbada, una linea SIN corte pasaria: %r" % pasaria)
    p("      con la guarda de verdad, la misma linea pasa: %r"
      % BAR.lleva_corte("   CIFRA pares reales: 18"))
    mutacion_muerde = (pasaria is True
                       and BAR.lleva_corte("   CIFRA pares reales: 18") is False)
    p("      LA GUARDA MUERDE Y LA MUTACION LA TUMBA: %s"
      % ("SI" if mutacion_muerde else "NO"))
    p("      la mutacion queda deshecha: %s"
      % ("SI" if BAR.lleva_corte is original else "NO"))
    p("")

    if fallos or caen != len(CASOS) or not mutacion_muerde:
        p("ROJO: %d caso(s) fallan, %d de %d caen al mutar, y la guarda del barrido "
          "muerde: %s" % (fallos, caen, len(CASOS), mutacion_muerde))
        p("FIN")
        return 1
    p("VERDE: %d casos, los %d pasan y los %d CAEN al mutarles el valor esperado. "
      "La misma tabla medida en dos cortes no se confunde, la misma cifra con dos "
      "cortes distintos tampoco, y dos cosas distintas del mismo tamano y del "
      "mismo corte tampoco. Y la guarda del barrido muerde: tumbada, una linea sin "
      "corte pasaria." % (len(CASOS), len(CASOS), caen))
    p("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
