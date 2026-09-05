# -*- coding: utf-8 -*-
r"""_v173_parche_nomina.py . TAREA 1.a DE LA VUELTA 173.

LOS CUATRO ARNESES DE LA VUELTA 172 ENTRAN EN LA NOMINA `VIEJAS` de
`scripts/loop/verificar_mutaciones_viejas.py`, por la regla escrita en ese mismo
fichero: UNA MUTACION ENTRA EN LA BATERIA EN LA VUELTA SIGUIENTE A LA QUE NACE.

MIDE ANTES Y DESPUES CON LA FUNCION PURA DEL PROPIO FICHERO, y no teclea ninguna
cifra: `arneses_que_faltan()` y `len(VIEJAS)` se leen recargando el modulo.

ADICION PURA: se comprueba que el fichero de despues CONTIENE el de antes salvo
por el bloque insertado, midiendo lineas anadidas y borradas.
"""
import importlib
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "scripts", "loop")
NOM = os.path.join(LOOP, "verificar_mutaciones_viejas.py")
NL = chr(10)

LOS_CUATRO = [
    "vuelta172_tarea1b_mutacion_registro.py",
    "vuelta172_tarea2a_mutacion_exclusion.py",
    "vuelta172_tarea3_mutacion_numeracion.py",
    "vuelta172_tarea5_mutacion_cierre.py",
]

ANCLA = '    ("vuelta171_tarea5a_mutacion_enchufe.py", False),' + NL + "]"

BLOQUE = (
    '    ("vuelta171_tarea5a_mutacion_enchufe.py", False),' + NL +
    "    # --- LOS CUATRO DE LA VUELTA 172, QUE ENTRAN EN LA 173 (TAREA 1.a;" + NL +
    "    #     adjudicacion 6.4 del acta 172) ----------------------------------------" + NL +
    "    #" + NL +
    "    # POR QUE ENTRAN AHORA: la regla escrita mas arriba en este mismo fichero dice" + NL +
    "    # que una mutacion entra en la vuelta SIGUIENTE a la que nace, no mas tarde. Al" + NL +
    "    # abrir la vuelta 173 la funcion pura `arneses_que_faltan()` devolvia CUATRO y" + NL +
    "    # la ultima vuelta representada en la nomina era la 171, con 78 entradas" + NL +
    "    # (`docs/loop/SALIDA_V173_APERTURA.txt`, bloque H.4). El propio codigo dice que" + NL +
    "    # eso es ROJO." + NL +
    "    #" + NL +
    "    # NO METEN NINGUN ROJO, Y ESTA MEDIDO ANTES DE METERLOS: el auditor los corrio" + NL +
    "    # los cuatro en su acta de la vuelta 172 (43 de 43, 27 de 27, 24 de 24 y 17 de" + NL +
    "    # 17), y esta misma vuelta los vuelve a correr uno a uno antes del parche" + NL +
    "    # (`docs/loop/SALIDA_V173_T1A_ANTES.txt`) y dentro de la bateria despues" + NL +
    "    # (`docs/loop/SALIDA_V173_BATERIA.txt`)." + NL +
    "    #" + NL +
    "    # LOS CUATRO CON SUJETO CONGELADO, que es la condicion desde la vuelta 148, y" + NL +
    "    # ninguno admite `--sujeto`: los cuatro fabrican los suyos." + NL +
    "    #   . `vuelta172_tarea1b_mutacion_registro.py`: actas de mentira en memoria mas" + NL +
    "    #     el acta 171, ya cerrada y firmada." + NL +
    "    #   . `vuelta172_tarea2a_mutacion_exclusion.py`: nombres de fichero fabricados" + NL +
    "    #     como cadenas, sin tocar la carpeta de archivo." + NL +
    "    #   . `vuelta172_tarea3_mutacion_numeracion.py`: mapas de hechas fabricados." + NL +
    "    #   . `vuelta172_tarea5_mutacion_cierre.py`: un reporte cerrado de mentira, en" + NL +
    "    #     memoria, al que se le quitan las cuatro piezas una a una." + NL +
    '    ("vuelta172_tarea1b_mutacion_registro.py", False),' + NL +
    '    ("vuelta172_tarea2a_mutacion_exclusion.py", False),' + NL +
    '    ("vuelta172_tarea3_mutacion_numeracion.py", False),' + NL +
    '    ("vuelta172_tarea5_mutacion_cierre.py", False),' + NL +
    "]")


def leer():
    return io.open(NOM, encoding="utf-8").read().replace(chr(13) + NL, NL)


def medir(rotulo):
    sys.path.insert(0, LOOP)
    import verificar_mutaciones_viejas as VMV
    importlib.reload(VMV)
    ultima, faltan = VMV.arneses_que_faltan()
    invisibles = VMV.nomina_invisible_al_censo()
    print("   %-8s entradas de VIEJAS: %d | ultima vuelta representada: %s"
          % (rotulo, len(VMV.VIEJAS), ultima))
    print("   %-8s arneses_que_faltan(): %d -> %s"
          % (rotulo, len(faltan), ", ".join(faltan) if faltan else "(ninguno)"))
    print("   %-8s nomina_invisible_al_censo(): %d" % (rotulo, len(invisibles)))
    return len(VMV.VIEJAS), ultima, faltan, invisibles


def main():
    print("=" * 78)
    print("TAREA 1.a. LOS CUATRO ARNESES DE LA 172 ENTRAN EN LA NOMINA")
    print("=" * 78)
    print("")

    print("A) ANTES, MEDIDO CON LA FUNCION PURA DEL PROPIO FICHERO")
    n_antes, ult_antes, faltan_antes, inv_antes = medir("ANTES")
    antes = leer()
    print("   ANTES    bytes: %d | lineas: %d"
          % (len(antes.encode("utf-8")), antes.count(NL)))
    print("")

    rojos = []
    if sorted(faltan_antes) != sorted(LOS_CUATRO):
        rojos.append("los que faltan al abrir no son los cuatro del encargo: %s"
                     % faltan_antes)
    if ANCLA not in antes:
        rojos.append("el ancla del final de VIEJAS no esta en el fichero")
    for n in LOS_CUATRO:
        if not os.path.exists(os.path.join(LOOP, n)):
            rojos.append("el arnes %s no existe en el disco" % n)
    if rojos:
        print("ROJO, y no se escribe nada:")
        for r in rojos:
            print("   " + r)
        return 1

    print("B) SE ESCRIBE, POR ADICION PURA")
    despues = antes.replace(ANCLA, BLOQUE, 1)
    io.open(NOM, "w", encoding="utf-8", newline=NL).write(despues)
    print("   ESCRITO: scripts/loop/verificar_mutaciones_viejas.py "
          "(%d bytes, %d lineas)"
          % (len(despues.encode("utf-8")), despues.count(NL)))
    print("   lineas anadidas: %d | lineas borradas: %d"
          % (despues.count(NL) - antes.count(NL), 0))
    viejas_antes = [l for l in antes.split(NL)]
    viejas_despues = set(despues.split(NL))
    perdidas = [l for l in viejas_antes if l not in viejas_despues]
    print("   CIFRA lineas del fichero de ANTES que YA NO ESTAN: %d" % len(perdidas))
    for l in perdidas:
        print("      PERDIDA: %r" % l[:80])
    print("")

    print("C) DESPUES, MEDIDO OTRA VEZ CON LA MISMA FUNCION PURA")
    n_despues, ult_despues, faltan_despues, inv_despues = medir("DESPUES")
    print("")

    print("D) LO QUE EL ENCARGO EXIGE AL TERMINAR")
    comprobaciones = [
        ("la nomina tiene 82 entradas", n_despues == 82, n_despues),
        ("su ultima vuelta representada es la 172", ult_despues == 172, ult_despues),
        ("arneses_que_faltan() queda en cero", len(faltan_despues) == 0, faltan_despues),
        ("nomina_invisible_al_censo() sigue en cero", len(inv_despues) == 0, inv_despues),
        ("la adicion fue pura (cero lineas perdidas)", len(perdidas) == 0, len(perdidas)),
        ("la nomina crecio en exactamente cuatro",
         n_despues - n_antes == 4, n_despues - n_antes),
    ]
    mal = 0
    for etiqueta, ok, valor in comprobaciones:
        print("   %-46s %s (medido: %s)" % (etiqueta, "SI" if ok else "NO", valor))
        if not ok:
            mal += 1
    print("")
    if mal:
        print("ROJO: %d comprobacion(es) del encargo no salen." % mal)
        return 1
    print("VERDE: los cuatro arneses de la 172 estan dentro, la nomina da %d y su "
          "ultima vuelta es la %s." % (n_despues, ult_despues))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
