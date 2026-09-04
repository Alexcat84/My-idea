# -*- coding: utf-8 -*-
r"""vuelta165_tarea2_mutacion_censo.py . CASO POSITIVO POR MUTACION DEL PUNTO
CIEGO DEL CENSO DE ARNESES (TAREA 2 de la vuelta 165; adjudicacion 6.3 del acta
164, sobre su hallazgo 5.1).

POR QUE HACIA FALTA Y NO EXISTIA. El agujero era este: el patron del censo de
`verificar_mutaciones_viejas.py` exigia la palabra `mutacion` en el nombre, y
DOS entradas de su propia nomina no la llevan. `arneses_que_faltan()` produce el
VERDE *"NINGUN arnes posterior se queda fuera de la nomina"*, y ese verde solo
cubria a los que se llamaran `mutacion`. NINGUN caso rojo probaba esa frase.

LO QUE ESTE ARNES TIENE QUE HACER, Y ES LA LETRA DEL ENCARGO: **CAER si alguien
devuelve el patron a su forma vieja.** Por eso no compara el patron consigo
mismo: corre el patron VIEJO y el NUEVO **sobre el mismo sujeto** y mide la
diferencia. Si `PATRON_ARNES` volviera a ser el viejo, los dos darian lo mismo y
los casos B y D caerian.

NINGUN VEREDICTO ES UNA CONSTANTE LITERAL (`EJECUTOR.md` 1, "EL CASO ROJO SE
PRUEBA POR MUTACION"): todos salen de correr las funciones reales del modulo, y
la segunda pasada muta cada valor esperado y exige que el caso CAIGA.

SUJETO: nominas fabricadas como listas de tuplas y directorios fabricados en un
temporal. El unico sujeto vivo es la nomina real de hoy, y de ella solo se mide
que su cifra de invisibles sea CERO, que es la propiedad que el arreglo instala
y que tiene que seguir siendo cierta manana. P.16: quien fabrica, limpia.

USO:  python scripts/loop/vuelta165_tarea2_mutacion_censo.py
"""
import io
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verificar_mutaciones_viejas as B   # noqa: E402


def prueba():
    print("=" * 78)
    print("VUELTA 165, TAREA 2: CASO POSITIVO POR MUTACION DEL PUNTO CIEGO DEL CENSO")
    print("=" * 78)
    print("")
    casos = []

    print("A) EL AGUJERO, MEDIDO SOBRE LA NOMINA REAL DE HOY CON LOS DOS PATRONES")
    invis_viejo = B.nomina_invisible_al_censo(patron=B.PATRON_ARNES_VIEJO)
    invis_nuevo = B.nomina_invisible_al_censo()
    print("   con el patron VIEJO, entradas de la nomina invisibles: %d" % len(invis_viejo))
    for n in invis_viejo:
        print("      %s" % n)
    print("   con el patron NUEVO, entradas de la nomina invisibles: %d" % len(invis_nuevo))
    print("   LAS DOS QUE EL AUDITOR NOMBRO SIGUEN SIENDO LAS MISMAS:")
    esperadas = ["vuelta144_3c_caso_positivo_1190.py", "vuelta147_3e_simular_a26.py"]
    print("      %s" % ", ".join(esperadas))
    casos.append(("A_el_patron_VIEJO_no_ve_dos_de_su_propia_nomina",
                  invis_viejo, esperadas))
    casos.append(("A_el_patron_NUEVO_las_ve_todas", len(invis_nuevo), 0))
    casos.append(("A_y_las_dos_existen_en_disco",
                  sum(1 for n in esperadas
                      if os.path.exists(os.path.join(B.LOOP, n))), 2))
    print("")

    print("B) LA CONSECUENCIA QUE NO ERA COSMETICA: EL VERDE QUE NO MIRA")
    print("   Un directorio fabricado con un arnes POSTERIOR a la nomina cuyo")
    print("   nombre NO lleva la palabra mutacion. El patron viejo dice que no")
    print("   falta ninguno SIN HABERLO MIRADO; el nuevo lo reclama.")
    tmp = tempfile.mkdtemp(prefix="v165_censo_")
    try:
        for nombre in ("vuelta100_tarea1_mutacion_dentro.py",
                       "vuelta200_tarea9_caso_positivo_fuera.py",
                       "vuelta201_tarea9_simular_fuera.py",
                       "vuelta202_tarea9_mutacion_fuera.py",
                       "vuelta203_tarea9_un_script_cualquiera.py"):
            io.open(os.path.join(tmp, nombre), "w", encoding="utf-8").write("# de mentira\n")
        nomina = [("vuelta100_tarea1_mutacion_dentro.py", False)]

        censo_nuevo = B.arneses_del_directorio(tmp)
        print("   ficheros fabricados: %s" % ", ".join(sorted(os.listdir(tmp))))
        print("   CIFRA que el censo NUEVO reconoce: %d (%s)"
              % (len(censo_nuevo), ", ".join(censo_nuevo)))
        casos.append(("B_el_censo_nuevo_ve_las_tres_familias", len(censo_nuevo), 4))
        casos.append(("B_y_no_cuenta_lo_que_no_es_arnes",
                      "vuelta203_tarea9_un_script_cualquiera.py" in censo_nuevo, False))

        _u, faltan_nuevo = B.arneses_que_faltan(nomina, tmp)
        print("   CIFRA que el patron NUEVO reclama: %d (%s)"
              % (len(faltan_nuevo), ", ".join(faltan_nuevo)))
        casos.append(("B_el_patron_NUEVO_reclama_los_tres", len(faltan_nuevo), 3))

        # EL PATRON VIEJO, SOBRE EL MISMO SUJETO. Se mide corriendo la MISMA
        # funcion con el censo restringido al patron viejo: no hay copia de la
        # logica, solo se le cambia el patron debajo y se devuelve enseguida.
        guardado = B.PATRON_ARNES
        try:
            B.PATRON_ARNES = B.PATRON_ARNES_VIEJO
            censo_viejo = B.arneses_del_directorio(tmp)
            _u2, faltan_viejo = B.arneses_que_faltan(nomina, tmp)
        finally:
            B.PATRON_ARNES = guardado
        print("   CIFRA que el censo VIEJO reconoce: %d (%s)"
              % (len(censo_viejo), ", ".join(censo_viejo)))
        print("   CIFRA que el patron VIEJO reclama: %d (%s)"
              % (len(faltan_viejo), ", ".join(faltan_viejo)))
        print("   LOS QUE EL VIEJO DEJABA PASAR SIN MIRAR: %s"
              % ", ".join(sorted(set(faltan_nuevo) - set(faltan_viejo))))
        casos.append(("B_el_patron_VIEJO_solo_reclama_uno", len(faltan_viejo), 1))
        casos.append(("B_y_los_DOS_que_deja_pasar_son_los_de_las_familias_nuevas",
                      sorted(set(faltan_nuevo) - set(faltan_viejo)),
                      ["vuelta200_tarea9_caso_positivo_fuera.py",
                       "vuelta201_tarea9_simular_fuera.py"]))
        casos.append(("B_el_VIEJO_saldria_verde_sobre_lo_que_no_miro",
                      len(faltan_viejo) < len(faltan_nuevo), True))
        print("")

        print("C) EL INVARIANTE NUEVO: UN CENSO QUE NO VE SU NOMINA ES ROJO")
        ciega = [("vuelta300_tarea1_caso_positivo_x.py", False),
                 ("vuelta301_tarea1_familia_quinta.py", False)]
        invis_ciega = B.nomina_invisible_al_censo(ciega)
        print("   nomina fabricada: %s" % ", ".join(n for n, _a in ciega))
        print("   CIFRA invisibles al censo: %d (%s)"
              % (len(invis_ciega), ", ".join(invis_ciega)))
        print("   la que NO se ve es la de la familia QUINTA, que hoy no existe:")
        print("   ese es exactamente el caso que el ensanche del patron NO cubre")
        print("   y que esta comprobacion SI caza.")
        casos.append(("C_una_nomina_con_familia_quinta_da_invisibles",
                      invis_ciega, ["vuelta301_tarea1_familia_quinta.py"]))
        casos.append(("C_una_nomina_de_familias_conocidas_da_cero",
                      len(B.nomina_invisible_al_censo(
                          [("vuelta300_tarea1_caso_positivo_x.py", False),
                           ("vuelta302_tarea1_mutacion_y.py", False),
                           ("vuelta303_tarea1_simular_z.py", False)])), 0))
        print("")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
        print("   P.16: el temporal se retira. Existe todavia: %s" % os.path.exists(tmp))
        print("")

    print("D) LAS DOS FAMILIAS QUE FALTABAN SALEN DE LA NOMINA, NO DE LA IMAGINACION")
    print("   FAMILIAS_DE_ARNES declaradas: %s" % ", ".join(B.FAMILIAS_DE_ARNES))
    nombres = [s for s, _a in B.VIEJAS]
    cubiertas = sorted(set(f for f in B.FAMILIAS_DE_ARNES
                           if any(f in n for n in nombres)))
    print("   familias que la nomina real usa de verdad: %s" % ", ".join(cubiertas))
    casos.append(("D_ninguna_familia_declarada_sobra",
                  sorted(B.FAMILIAS_DE_ARNES), cubiertas))
    casos.append(("D_el_patron_nuevo_ve_mas_que_el_viejo",
                  len(B.arneses_del_directorio()) >
                  len([n for n in os.listdir(B.LOOP)
                       if B.PATRON_ARNES_VIEJO.match(n)]), True))
    print("")

    print("E) PASADA 1, LOS CASOS TAL CUAL")
    fallos = 0
    for nombre, real, esperado in casos:
        ok = (real == esperado)
        print("   %-52s %s   (real=%r esperado=%r)"
              % (nombre, "PASA" if ok else "FALLA", real, esperado))
        if not ok:
            fallos += 1
    print("   CIFRA casos: %d | pasan: %d | fallan: %d"
          % (len(casos), len(casos) - fallos, fallos))
    print("")

    print("F) PASADA 2, SE MUTA EL VALOR ESPERADO Y CADA CASO TIENE QUE CAER")
    caen = 0
    for nombre, real, esperado in casos:
        if isinstance(esperado, bool):
            mutado = not esperado
        elif isinstance(esperado, int):
            mutado = esperado + 1
        elif isinstance(esperado, list):
            mutado = esperado + ["mutado.py"]
        else:
            mutado = str(esperado) + "_mutado"
        cae = (real != mutado)
        print("   %-52s %s   (esperado mutado=%r)"
              % (nombre, "CAE" if cae else "NO CAE", mutado))
        if cae:
            caen += 1
    print("   CIFRA casos que caen al mutar el esperado: %d de %d" % (caen, len(casos)))
    print("")

    if fallos == 0 and caen == len(casos):
        print("VERDE: los %d casos pasan tal cual y los %d caen al mutar el esperado."
              % (len(casos), len(casos)))
        print("Y LO QUE ESTE ARNES GARANTIZA: si alguien devuelve PATRON_ARNES a su")
        print("forma vieja, los casos A_el_patron_NUEVO_las_ve_todas,")
        print("B_el_censo_nuevo_ve_las_tres_familias, B_el_patron_NUEVO_reclama_los_tres,")
        print("B_y_los_DOS_que_deja_pasar y D_el_patron_nuevo_ve_mas_que_el_viejo CAEN.")
        return 0
    print("ROJO: fallos=%d, casos que no caen=%d" % (fallos, len(casos) - caen))
    return 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(prueba())
