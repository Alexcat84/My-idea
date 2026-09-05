# -*- coding: utf-8 -*-
r"""vuelta178_tarea1b_mutacion_hermano.py . EL CASO POSITIVO POR MUTACION DE LA
VARA DEL CENSO, Y EL CASO QUE HOY FALLA CORRIDO CON LAS DOS FUNCIONES.

TAREA 1.b de la vuelta 178. La letra del encargo es exacta y se cita: "un
directorio fabricado con DOS arneses de la MISMA vuelta que la ultima de la
nomina, uno dentro y otro fuera, y la funcion tiene que VER al de fuera. Con la
funcion vieja ese caso CAE; publica las dos corridas, la vieja en rojo y la
nueva en verde."

SUJETO CONGELADO, que es la condicion de entrada en la nomina desde la vuelta
148: TODO lo que este arnes mide vive en un directorio TEMPORAL que el propio
arnes fabrica y retira (`P.16`, quien fabrica limpia), y en una nomina FABRICADA
que se pasa por parametro. Ni `scripts/loop/` ni `VIEJAS` ni el disco del repo
se tocan. La funcion vieja no se re-implementa aqui: se importa de
`scripts/loop/_v178_arneses_que_faltan_viejo_copia.py`, que la lleva congelada.

NINGUN VEREDICTO ES UNA CONSTANTE LITERAL (`EJECUTOR.md` 1, caida 2 de la vuelta
89): los cinco casos salen de correr las dos funciones sobre escenarios
fabricados, y la segunda pasada MUTA EL VALOR ESPERADO de cada uno y exige que
CAIGA. Si una mutacion no hace caer su caso, este arnes sale en ROJO.

QUE PRUEBA, CASO A CASO:

  (1) EL CASO QUE DECIDE TODO. Directorio con `vuelta200_a_mutacion_dentro.py` y
      `vuelta200_b_mutacion_fuera.py`, nomina con SOLO el primero. LA FUNCION
      NUEVA VE al de fuera. Es exactamente lo que le paso a la vuelta 177 con
      sus cuatro arneses propios.
  (2) EL MISMO CASO CON LA FUNCION VIEJA, QUE NO LO VE. Su `>` estricto contra
      la ultima vuelta de la nomina (200) descarta a todo lo de la vuelta 200.
      ESTA ES LA CORRIDA EN ROJO que el encargo pide publicar.
  (3) LA VARA SIGUE PROTEGIENDO A LOS VIEJOS. Con un arnes de la vuelta 50 en el
      mismo directorio y la vara en 100, no se reclama.
  (4) Y CON LA VARA EN 0 SI SE RECLAMA, o sea que lo que lo protege es LA VARA y
      no un azar del filtro.
  (5) LA VARA VIVA DEL FICHERO ES UN ENTERO Y VALE 148, leido de
      `VARA_DEL_CENSO` y no tecleado dos veces.

USO:
  python scripts/loop/vuelta178_tarea1b_mutacion_hermano.py
"""
import io
import os
import shutil
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import verificar_mutaciones_viejas as V   # noqa: E402
import _v178_arneses_que_faltan_viejo_copia as VIEJO   # noqa: E402

NL = chr(10)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    p = print
    p("=" * 78)
    p("CASO POSITIVO POR MUTACION DE LA VARA DEL CENSO (vuelta 178, TAREA 1.b)")
    p("=" * 78)
    p("")

    casos = []
    tmp = tempfile.mkdtemp(prefix="v178_hermano_")
    try:
        for nombre in ("vuelta200_a_mutacion_dentro.py",
                       "vuelta200_b_mutacion_fuera.py",
                       "vuelta050_c_mutacion_muy_vieja.py"):
            io.open(os.path.join(tmp, nombre), "w",
                    encoding="utf-8").write("# de mentira" + NL)
        nomina = [("vuelta200_a_mutacion_dentro.py", False)]

        p("A) EL DIRECTORIO FABRICADO Y LA NOMINA FABRICADA")
        p("   ficheros: %s" % ", ".join(sorted(os.listdir(tmp))))
        p("   nomina:   %s" % ", ".join(n for n, _a in nomina))
        p("   CIFRA arneses que el censo reconoce ahi: %d"
          % len(V.arneses_del_directorio(tmp)))
        p("")

        p("B) LA CORRIDA NUEVA, QUE ES LA QUE TIENE QUE VER AL HERMANO")
        ultima_n, faltan_n = V.arneses_que_faltan(nomina, tmp, vara=100)
        p("   ultima vuelta de la nomina: %s" % ultima_n)
        p("   vara pasada a mano: 100")
        p("   CIFRA que faltan: %d (%s)"
          % (len(faltan_n), ", ".join(faltan_n) or "ninguno"))
        casos.append(("la_nueva_VE_al_hermano_de_la_misma_vuelta",
                      "vuelta200_b_mutacion_fuera.py" in faltan_n, True))
        p("")

        p("C) LA CORRIDA VIEJA SOBRE EL MISMO CASO. ESTA ES LA QUE CAE")
        p("   (funcion congelada en scripts/loop/_v178_arneses_que_faltan_viejo_copia.py)")
        ultima_v, faltan_v = VIEJO.arneses_que_faltan_viejo(nomina, tmp)
        p("   ultima vuelta de la nomina: %s" % ultima_v)
        p("   CIFRA que faltan segun la vieja: %d (%s)"
          % (len(faltan_v), ", ".join(faltan_v) or "ninguno"))
        p("   LA VIEJA VE AL HERMANO: %s"
          % ("SI" if "vuelta200_b_mutacion_fuera.py" in faltan_v else "NO"))
        casos.append(("la_vieja_NO_VE_al_hermano_de_la_misma_vuelta",
                      "vuelta200_b_mutacion_fuera.py" in faltan_v, False))
        p("   ROJO DE LA VIEJA: el censo tiene el fichero delante y la funcion")
        p("   contesta que no falta ninguno. Es la caida de la vuelta 177 entera,")
        p("   reproducida sobre un directorio de mentira y sin tocar el repo.")
        p("")

        p("D) LA VARA PROTEGE A LOS VIEJOS, Y SE COMPRUEBA MOVIENDOLA")
        _u, con_vara_100 = V.arneses_que_faltan(nomina, tmp, vara=100)
        _u, con_vara_0 = V.arneses_que_faltan(nomina, tmp, vara=0)
        p("   con la vara en 100, el de la vuelta 50 se reclama: %s"
          % ("SI" if "vuelta050_c_mutacion_muy_vieja.py" in con_vara_100 else "NO"))
        p("   con la vara en   0, el de la vuelta 50 se reclama: %s"
          % ("SI" if "vuelta050_c_mutacion_muy_vieja.py" in con_vara_0 else "NO"))
        casos.append(("la_vara_en_100_deja_fuera_al_de_la_50",
                      "vuelta050_c_mutacion_muy_vieja.py" in con_vara_100, False))
        casos.append(("la_vara_en_0_si_reclama_al_de_la_50",
                      "vuelta050_c_mutacion_muy_vieja.py" in con_vara_0, True))
        p("")

        p("E) LA VARA VIVA DEL FICHERO, LEIDA Y NO TECLEADA DOS VECES")
        p("   VARA_DEL_CENSO = %r (tipo %s)"
          % (V.VARA_DEL_CENSO, type(V.VARA_DEL_CENSO).__name__))
        casos.append(("la_vara_viva_es_un_entero_y_vale_148",
                      V.VARA_DEL_CENSO, 148))
        p("")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
        p("   P.16: el temporal se retira. Existe todavia: %s" % os.path.exists(tmp))
        p("")

    p("F) PASADA 1, LOS CASOS TAL CUAL")
    fallos = 0
    for nombre, real, esperado in casos:
        ok = (real == esperado)
        p("   %-46s %s   (real=%r esperado=%r)"
          % (nombre, "PASA" if ok else "FALLA", real, esperado))
        if not ok:
            fallos += 1
    p("   CIFRA casos: %d | pasan: %d | fallan: %d"
      % (len(casos), len(casos) - fallos, fallos))
    p("")

    p("G) PASADA 2, SE MUTA EL VALOR ESPERADO Y CADA CASO TIENE QUE CAER")
    caen = 0
    for nombre, real, esperado in casos:
        mutado = (not esperado) if isinstance(esperado, bool) else esperado + 1
        cae = (real != mutado)
        p("   %-46s %s" % (nombre, "CAE" if cae else "NO CAE (ROJO)"))
        if cae:
            caen += 1
    p("   CIFRA casos que CAEN: %d de %d" % (caen, len(casos)))
    p("")

    if fallos or caen != len(casos):
        p("ROJO DE LA MUTACION: la vara del censo no se comporta.")
        p("FIN")
        return 1
    p("VERDE DE LA MUTACION: %d casos, los %d pasan y los %d CAEN al mutarles el "
      "valor esperado. LA FUNCION NUEVA VE al hermano de la misma vuelta que la "
      "ultima de la nomina y LA VIEJA NO LO VE, sobre el mismo directorio "
      "fabricado y en la misma corrida; y la vara sigue protegiendo a los "
      "anteriores, cosa que se prueba MOVIENDOLA y no afirmandola."
      % (len(casos), len(casos), len(casos)))
    p("FIN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
