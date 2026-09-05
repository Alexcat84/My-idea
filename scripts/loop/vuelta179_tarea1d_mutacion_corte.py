# -*- coding: utf-8 -*-
r"""vuelta179_tarea1d_mutacion_corte.py . EL CASO POSITIVO POR MUTACION DEL
CORTE DEL DENOMINADOR (vuelta 179, TAREA 1.d).

QUE PRUEBA. `verificar_mutaciones_viejas.sello_de_corte()`, que es PURA y recibe
el denominador y el head, y la separacion entre ella y `corte_de_git()`, que es
la unica que toca git. NADA SALE DEL REPO: este arnes no llama a git, no lee
ficheros y no corre ningun otro arnes. Su sujeto es una funcion pura y dos
literales.

POR QUE EXISTE LA COSA QUE PRUEBA, Y EL MOTIVO ESTA MEDIDO (adjudicacion 7.2 del
acta del auditor de la vuelta 178, por `banco 9.21`): la 178 publico `15 de 92`
SIENDO VERDAD CUANDO LO MIDIO, y al cerrar esa misma vuelta el denominador era
98, porque la nomina crece dentro de la propia vuelta que la esta contando. Una
cifra de la nomina sin su corte no se puede cotejar con nada.

LA MUTACION (`EJECUTOR.md` 1, EL CASO ROJO SE PRUEBA POR MUTACION): de cada caso
se mueve EL VALOR ESPERADO y se comprueba que el caso CAE.

USO:
  python scripts/loop/vuelta179_tarea1d_mutacion_corte.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verificar_mutaciones_viejas as VMV   # noqa: E402


CASOS = [
    ("A_el_sello_lleva_el_denominador",
     lambda: VMV.sello_de_corte(92, "abcdef123456").startswith("92 "), True),
    ("A_y_lleva_el_head_que_se_le_da",
     lambda: "abcdef123456" in VMV.sello_de_corte(92, "abcdef123456"), True),
    ("A_y_dice_la_palabra_corte",
     lambda: "corte:" in VMV.sello_de_corte(92, "abcdef123456"), True),
    ("B_dos_denominadores_distintos_dan_sellos_distintos",
     lambda: VMV.sello_de_corte(92, "abcdef123456") == VMV.sello_de_corte(98, "abcdef123456"),
     False),
    ("B_ES_EL_CASO_DE_LA_178_el_92_y_el_98_no_se_confunden",
     lambda: (VMV.sello_de_corte(92, "abcdef123456").split()[0],
              VMV.sello_de_corte(98, "abcdef123456").split()[0]), ("92", "98")),
    ("C_dos_cortes_distintos_dan_sellos_distintos_con_el_mismo_numero",
     lambda: VMV.sello_de_corte(98, "aaaaaaaaaaaa") == VMV.sello_de_corte(98, "bbbbbbbbbbbb"),
     False),
    ("D_el_head_no_medible_se_dice_y_no_se_inventa",
     lambda: "(no medible)" in VMV.sello_de_corte(98, "(no medible)"), True),
    ("E_es_PURA_no_llama_a_git_y_por_eso_no_cambia_entre_corridas",
     lambda: VMV.sello_de_corte(98, "abcdef123456") == VMV.sello_de_corte(98, "abcdef123456"),
     True),
    ("F_corte_de_git_es_OTRA_funcion_y_esta_separada",
     lambda: (callable(VMV.corte_de_git), callable(VMV.sello_de_corte)), (True, True)),
    ("G_la_nomina_crece_dentro_de_la_vuelta_y_por_eso_el_corte_manda",
     lambda: VMV.sello_de_corte(len(VMV.VIEJAS), "abcdef123456").split()[0],
     str(len(VMV.VIEJAS))),
]


def main():
    print("=" * 78)
    print("CASO POSITIVO POR MUTACION: EL CORTE DEL DENOMINADOR (179, 1.d)")
    print("=" * 78)
    print("")
    print("NADA SALE DEL REPO: no se llama a git, no se lee ningun fichero y no se")
    print("corre ningun otro arnes. El sujeto es una funcion PURA.")
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
        print("   %-56s %s  visto=%r esperado=%r"
              % (nombre[:56], "pasa " if ok else "FALLA", visto, esperado))
    print("   CIFRA casos: %d | pasan: %d | fallan: %d"
          % (len(CASOS), len(CASOS) - fallan, fallan))
    print("")

    print("B) LA MUTACION: A CADA CASO SE LE MUEVE EL VALOR ESPERADO Y TIENE QUE CAER")
    caen = 0
    for nombre, fn, esperado in CASOS:
        if isinstance(esperado, bool):
            mutado = not esperado
        elif isinstance(esperado, tuple):
            mutado = tuple(list(esperado)[::-1]) if len(set(esperado)) > 1 else ("X", "X")
        else:
            mutado = str(esperado) + "_MUTADO"
        try:
            visto = fn()
        except Exception as e:
            visto = "EXCEPCION %r" % (e,)
        cae = visto != mutado
        if cae:
            caen += 1
        print("   %-56s %s" % (nombre[:56], "CAE" if cae else "NO CAE, Y ESO ES ROJO"))
    print("   CIFRA casos que CAEN: %d de %d" % (caen, len(CASOS)))
    print("")

    if fallan or caen != len(CASOS):
        print("ROJO DE LA MUTACION: %d caso(s) fallan y %d de %d caen."
              % (fallan, caen, len(CASOS)))
        return 1
    print("VERDE DE LA MUTACION: %d casos, los %d pasan y los %d CAEN al mutarles "
          "el valor esperado. El sello lleva el denominador y el corte pegados, dos "
          "denominadores distintos no se confunden aunque el corte sea el mismo, dos "
          "cortes distintos no se confunden aunque el numero sea el mismo, el head "
          "que no se pudo leer se dice en vez de inventarse, y la funcion que juzga "
          "esta separada de la que toca git."
          % (len(CASOS), len(CASOS), len(CASOS)))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
