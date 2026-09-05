# -*- coding: utf-8 -*-
r"""vuelta179_tarea1c_cuenta_nomina.py . LA CUENTA ENTERA DE LA NOMINA Y DEL
CENSO, CON SU RESTA COMPROBADA Y CON SU CORTE (vuelta 179, TAREA 1.c y 1.d).

POR QUE SE PUBLICA ENTERA Y NO SOLO LA CIFRA QUE INTERESA. Porque una cuenta que
no cierra consigo misma se caza sola si alguien la escribe entera, que es lo que
la 178 hizo en su 1.a y lo que este encargo repite. Aqui van las cuatro y la
resta: censo, nomina, fuera de la nomina, invisibles al censo.

Y CON SU CORTE (adjudicacion 7.2 del acta 178, por `banco 9.21`). El corte no se
teclea en una frase: sale de `verificar_mutaciones_viejas.sello_de_corte()`, que
es donde se genera la cifra, y el head lo lee `corte_de_git()`.

ESTE FICHERO NO ES UN ARNES y no entra en el censo a proposito: su nombre no
lleva ninguna de las familias (`mutacion`, `caso_positivo`, `simular`). SOLO
CUENTA: no corre ningun arnes, no toca la nomina y no escribe nada fuera de su
propia salida.

USO:
  python scripts/loop/vuelta179_tarea1c_cuenta_nomina.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verificar_mutaciones_viejas as VMV   # noqa: E402

# LOS QUE ESTA VUELTA METE EN LA NOMINA, nombrados aqui para que la cuenta de
# abajo no los pueda elegir despues de ver el resultado.
LOS_DE_ESTA_VUELTA = [
    "vuelta150_2d_simular_op_c_05.py",
    "vuelta160_tarea3b_caso_positivo.py",
    "vuelta179_tarea1b_mutacion_citas.py",
    "vuelta179_tarea3_mutacion_triangulos.py",
    "vuelta179_tarea1d_mutacion_corte.py",
]


def main():
    print("=" * 78)
    print("LA CUENTA DE LA NOMINA Y DEL CENSO (vuelta 179, TAREA 1.c)")
    print("=" * 78)
    print("")

    head = VMV.corte_de_git()
    censo = VMV.arneses_del_directorio()
    nomina = [s for s, _a in VMV.VIEJAS]
    invisibles = VMV.nomina_invisible_al_censo()
    fuera = sorted(set(censo) - set(nomina))

    print("A) EL CORTE, LEIDO DE GIT EN ESTA CORRIDA Y NO TECLEADO")
    print("   HEAD: %s" % head)
    print("   LA VARA DEL CENSO, que es la que decide: %d" % VMV.VARA_DEL_CENSO)
    print("   LAS FAMILIAS DEL CENSO: %s" % ", ".join(VMV.FAMILIAS_DE_ARNES))
    print("")

    print("B) LAS CUATRO CIFRAS, CADA UNA CON SU CORTE PEGADO")
    print("| que se cuenta | cuantos |")
    print("|---|---:|")
    print("| arneses que ve el censo | %d |" % len(censo))
    print("| entradas de la nomina | %s |" % VMV.sello_de_corte(len(nomina), head))
    print("| del censo, FUERA de la nomina | %d |" % len(fuera))
    print("| de la nomina, INVISIBLES al censo | %d |" % len(invisibles))
    print("")

    print("C) LA RESTA, COMPROBADA Y NO AFIRMADA")
    print("   censo %d menos nomina %d = %d" % (len(censo), len(nomina), len(censo) - len(nomina)))
    print("   y los que estan fuera de la nomina son %d" % len(fuera))
    calza = (len(censo) - len(nomina)) == len(fuera)
    print("   CALZAN: %s" % ("SI" if calza else "NO"))
    print("   (la resta cierra solo si NINGUNA entrada de la nomina es invisible al")
    print("    censo; hoy las invisibles son %d)" % len(invisibles))
    for n in invisibles:
        print("      INVISIBLE AL CENSO: %s" % n)
    print("")

    print("D) LOS QUE ESTA VUELTA METE, UNO A UNO Y COMPROBADOS")
    faltan_de_disco = []
    fuera_de_nomina = []
    for n in LOS_DE_ESTA_VUELTA:
        en_disco = os.path.exists(os.path.join(VMV.LOOP, n))
        en_nomina = n in nomina
        en_censo = n in censo
        if not en_disco:
            faltan_de_disco.append(n)
        if not en_nomina:
            fuera_de_nomina.append(n)
        print("   %-46s disco: %-3s nomina: %-3s censo: %s"
              % (n, "SI" if en_disco else "NO",
                 "SI" if en_nomina else "NO", "SI" if en_censo else "NO"))
    print("   CIFRA que esta vuelta mete: %d" % len(LOS_DE_ESTA_VUELTA))
    print("   CIFRA de esos que NO estan en disco: %d" % len(faltan_de_disco))
    print("   CIFRA de esos que NO estan en la nomina: %d" % len(fuera_de_nomina))
    print("")

    print("E) LO QUE arneses_que_faltan() DICE HOY, QUE ES LA VARA DEL ROJO DE LA 181")
    ultima, faltan = VMV.arneses_que_faltan()
    print("   ultima vuelta representada en la nomina: %s (INFORMATIVA)" % ultima)
    print("   CIFRA arneses del censo, no anteriores a la vara, FUERA de la nomina: %d"
          % len(faltan))
    for n in faltan:
        print("      FUERA DE LA NOMINA: %s" % n)
    if not faltan:
        print("      (ninguno)")
    print("")

    print("F) EL VEREDICTO")
    rojos = []
    if not calza:
        rojos.append("la resta no cierra: censo %d menos nomina %d no es %d"
                     % (len(censo), len(nomina), len(fuera)))
    if faltan_de_disco:
        rojos.append("hay %d entrada(s) de la nomina que no estan en disco: %s"
                     % (len(faltan_de_disco), ", ".join(faltan_de_disco)))
    if fuera_de_nomina:
        rojos.append("hay %d de los que esta vuelta mete que NO entraron: %s"
                     % (len(fuera_de_nomina), ", ".join(fuera_de_nomina)))
    if faltan:
        rojos.append("arneses_que_faltan() sigue nombrando %d, y ese es el rojo que "
                     "la 181 tendria: %s" % (len(faltan), ", ".join(faltan)))
    if rojos:
        print("   ROJO, %d motivo(s):" % len(rojos))
        for r in rojos:
            print("      " + r)
        print("FIN")
        return 1
    print("   VERDE: la resta cierra, los %d que esta vuelta mete estan en disco y en"
          % len(LOS_DE_ESTA_VUELTA))
    print("   la nomina, y arneses_que_faltan() no nombra a nadie. El rojo que la 178")
    print("   anuncio para la 181 NO llega a existir.")
    print("FIN")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
