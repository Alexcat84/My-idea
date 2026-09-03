# -*- coding: utf-8 -*-
"""_v163_parche_bateria.py . El parche de la TAREA 2 sobre
verificar_mutaciones_viejas.py (adjudicacion 6.8 del acta 162), escrito como
fichero para que quede auditable QUE se inserto y DONDE. Idempotente."""
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(RAIZ, "scripts", "loop", "verificar_mutaciones_viejas.py")

ENTRADAS = '''    # --- DE LA VIGESIMOCUARTA EN ADELANTE, ANADIDAS EN LA VUELTA 163 (TAREA 2;
    # ADJUDICACION 6.8 DEL ACTA 162) --------------------------------------
    #
    # POR QUE ENTRAN TODAS DE GOLPE, Y NO ES UN CAPRICHO: LA NOMINA LLEVABA
    # QUINCE VUELTAS CONGELADA. Medido en el acta 162 (seccion 5.1) y
    # recomputado en la vuelta 163 (`docs/loop/SALIDA_V163_T2_CENSO_POST147.txt`):
    # la nomina tenia 23 entradas, su ultima vuelta representada era la 147, y en
    # `scripts/loop/` habia 84 arneses de mutacion de los cuales VEINTIDOS
    # nacieron despues de la 147 y ninguno entro. La regla que lo prohibe estaba
    # escrita aqui mismo desde la vuelta 144 y nadie la miro: "UNA MUTACION ENTRA
    # EN ESTA BATERIA EN LA VUELTA SIGUIENTE A LA QUE NACE, NO MAS TARDE".
    #
    # Y NO ERA TEORICO: CUATRO DABAN ROJO DENTRO DEL AGUJERO. Los cuatro se
    # arreglaron EN LA FUENTE en esta misma vuelta, cada uno con su diagnostico
    # medido y ninguno en verde alegado ni borrado:
    #   - `vuelta148_0d_mutacion_corredor.py`: llevaba roto desde la vuelta 154,
    #     cuando `intrusos_del_corredor` paso de devolver UNA lista a devolver
    #     DOS. Reventaba al desempaquetar.
    #   - `vuelta157_tarea4b_mutacion_tachado.py`: nacio caducado en su propio
    #     commit `5ebac882`, el mismo que tacho las celdas que el arnes exigia
    #     limpias. Reescrito para computar su sujeto y su clase esperada.
    #   - `vuelta160_tarea6b_mutacion_puerta.py`: su contraprueba sacaba la
    #     guarda vieja de `git show HEAD:`, o sea el remedio comparado consigo
    #     mismo desde el commit siguiente al suyo. Anclado a un ref FIJO.
    #   - `vuelta162_tarea1a_mutacion_serie.py`: sus esperados estaban clavados a
    #     un estado que su propio commit cambio. Reescrito a DELTAS.
    #
    # UNA NOTA QUE NO SE CALLA, PORQUE CALLARLA SERIA LO CONTRARIO DEL BANCO 9:
    # `vuelta154_tarea2d_mutacion_guarda.py` SALIO ROJO UNA VEZ y no se ha
    # reproducido. Las dos corridas del lote estan selladas
    # (`SALIDA_V163_T2_CENSO_POST147.txt` con cinco rojos y `..._SEGUNDA.txt` con
    # cuatro) y la medicion del intermitente esta en
    # `docs/loop/SALIDA_V163_T2_FLAKE_154.txt`. Entra igual, y entra con esta
    # nota: INTERMITENTE NO REPRODUCIDO no es lo mismo que sano.
    ("vuelta148_0d_mutacion_corredor.py", False),
    ("vuelta148_1a_mutacion_embebido.py", False),
    ("vuelta148_2a_mutacion_nomina_commiteada.py", False),
    ("vuelta148_2b_mutacion_cifras_conjunto.py", False),
    ("vuelta148_2c_mutacion_vara_parada.py", False),
    ("vuelta148_2d_mutacion_exencion.py", False),
    ("vuelta150_5c_mutacion_ciclo.py", False),
    ("vuelta154_tarea2d_mutacion_guarda.py", False),
    ("vuelta154_tarea6_mutacion_corredor.py", False),
    ("vuelta156_tarea4b_mutacion_tallador.py", False),
    ("vuelta156_tarea5d_mutacion_corredor.py", False),
    ("vuelta157_tarea4b_mutacion_tachado.py", False),
    ("vuelta157_tarea5c_mutacion_ruido.py", False),
    ("vuelta157_tarea6b_mutacion_re_sellado.py", False),
    ("vuelta159_tarea6c_mutacion_exencion.py", False),
    ("vuelta160_tarea6b_mutacion_puerta.py", False),
    ("vuelta160_tarea7c_mutacion_guarda_cita.py", False),
    ("vuelta161_tarea1a_mutacion_alcance.py", False),
    ("vuelta162_tarea1a_mutacion_serie.py", False),
    ("vuelta162_tarea2a_mutacion_puerta.py", False),
    ("vuelta162_tarea2b_mutacion_excepcion.py", False),
    ("vuelta162_tarea3_mutacion_fila.py", False),
    # Y LAS QUE NACEN HOY, EN LA VUELTA 163, por la misma regla aplicada a si
    # misma, que es lo que la vuelta 144 hizo con las suyas: entran el dia que
    # nacen y no se esperan una vuelta mas. Ninguna admite `--sujeto`: todas
    # eligen su sujeto por computo o sobre commits fijos de la historia, y
    # ninguna escribe en `docs/loop/`.
    ("vuelta163_tarea1b_mutacion_relectura.py", False),
    ("vuelta163_tarea1c_mutacion_tramo.py", False),
    ("vuelta163_tarea2_mutacion_nomina.py", False),
    ("vuelta163_tarea4a_mutacion_cobertura.py", False),
    ("vuelta163_tarea4b_mutacion_re_sellado.py", False),
    ("vuelta163_tarea5a_mutacion_contador.py", False),
]
'''

FIN_VIEJAS = '''    ("vuelta147_3d_mutacion_nomina.py", False),
    ("vuelta147_3e_simular_a26.py", False),
]
'''

MIRARSE = '''
# --- LA GUARDA SE MIRA A SI MISMA (vuelta 163, TAREA 2; adjudicacion 6.8 del
#     acta 162) --------------------------------------------------------------
#
# POR QUE NACE, Y LA CAUSA ESTA MEDIDA: EL AGUJERO SE ABRIO POR NO MIRAR. Esta
# bateria corria sus 23 y salia VERDE mientras 22 arneses nacidos despues de la
# vuelta 147 se quedaban fuera, y NADA en este fichero lo notaba. Seis actas
# seguidas publicaron "la bateria de las 23, VERDE" sin cruzar nunca esa nomina
# contra los arneses que nacian (acta 162, seccion 2, caida 2 del auditor). Un
# verde que cuenta 23 de 45 no es un verde: es un verde que no mira.
#
# QUE COMPRUEBA: que NINGUN arnes de mutacion de `scripts/loop/` POSTERIOR a la
# ultima vuelta representada en `VIEJAS` se quede fuera de `VIEJAS`. Si lo hay,
# ROJO CON SU LISTA ENTERA, no con un resumen.
#
# LAS DOS CIFRAS SE COMPUTAN, NINGUNA SE TECLEA: la nomina sale de `VIEJAS` y el
# censo del propio directorio. El dia que se anada un arnes, esta comprobacion lo
# ve sin que nadie edite una lista.
#
# POR QUE "POSTERIOR" Y NO "TODOS": porque la regla que esta guarda lleva escrita
# dentro nace en la vuelta 144 y NO DICE si alcanza a lo anterior. Los 41 arneses
# anteriores a la 148 que estan fuera se MIDEN aparte (vuelta 163, TAREA 5.b,
# `docs/loop/SALIDA_V163_T5B_PREVIOS.txt`) y NO se meten aqui por cuenta propia:
# con esa cifra delante decide quien tiene que decidir. Ensanchar la vara sin
# adjudicacion seria exactamente lo que la congelacion de `P.5.1` prohibe en su
# terreno.
PATRON_ARNES = re.compile(r"^vuelta(\\d+).*mutacion.*\\.py$")


def vuelta_de(nombre):
    m = re.match(r"^vuelta(\\d+)", nombre)
    return int(m.group(1)) if m else None


def arneses_del_directorio(directorio=None):
    """Los arneses de mutacion que existen HOY. PURA salvo por leer el
    directorio, y con `directorio` por parametro para que el caso por mutacion
    pueda apuntarla a uno fabricado sin tocar el repo."""
    base = directorio or LOOP
    return sorted(n for n in os.listdir(base) if PATRON_ARNES.match(n))


def arneses_que_faltan(nomina=None, directorio=None):
    """(ultima_vuelta_de_la_nomina, los_que_faltan). PURA a proposito: recibe la
    nomina y el directorio, para que su caso rojo se pueda probar por mutacion
    sin tocar ni este fichero ni el disco."""
    nombres = [s for s, _admite in (nomina if nomina is not None else VIEJAS)]
    vueltas = [v for v in (vuelta_de(n) for n in nombres) if v is not None]
    if not vueltas:
        return None, []
    ultima = max(vueltas)
    dentro = set(nombres)
    fuera = [n for n in arneses_del_directorio(directorio)
             if n not in dentro and (vuelta_de(n) or 0) > ultima]
    return ultima, sorted(fuera)


def prueba_de_la_nomina():
    """CASO POSITIVO POR MUTACION DE LA MIRADA SOBRE SI MISMA (vuelta 163,
    TAREA 2). Todo sobre un directorio FABRICADO en un temporal y una nomina
    FABRICADA: ni este fichero ni `scripts/loop/` se tocan. P.16, quien fabrica
    limpia.

    NINGUN VEREDICTO ES UNA CONSTANTE LITERAL: los cinco salen de correr
    `arneses_que_faltan` sobre escenarios distintos, y la segunda pasada muta el
    valor esperado de cada uno y exige que CAIGA."""
    print("=" * 78)
    print("PRUEBA DE MUTACION DE LA MIRADA DE LA NOMINA SOBRE SI MISMA")
    print("(vuelta 163, TAREA 2; adjudicacion 6.8 del acta 162)")
    print("=" * 78)
    print("")
    tmp = tempfile.mkdtemp(prefix="v163_nomina_")
    casos = []
    try:
        for nombre in ("vuelta100_tarea1_mutacion_vieja.py",
                       "vuelta110_tarea2_mutacion_dentro.py",
                       "vuelta120_tarea3_mutacion_fuera.py",
                       "vuelta121_tarea4_mutacion_tambien_fuera.py",
                       "vuelta115_tarea9_un_script_cualquiera.py"):
            io.open(os.path.join(tmp, nombre), "w", encoding="utf-8").write("# de mentira" + chr(10))
        nomina = [("vuelta100_tarea1_mutacion_vieja.py", False),
                  ("vuelta110_tarea2_mutacion_dentro.py", False)]

        print("A) EL DIRECTORIO FABRICADO Y LA NOMINA FABRICADA")
        print("   ficheros: %s" % ", ".join(sorted(os.listdir(tmp))))
        print("   nomina:   %s" % ", ".join(n for n, _a in nomina))
        censo = arneses_del_directorio(tmp)
        print("   CIFRA arneses que el censo reconoce: %d (%s)" % (len(censo), ", ".join(censo)))
        casos.append(("el_censo_no_cuenta_lo_que_no_es_arnes", len(censo), 4))
        print("")

        print("B) LA MIRADA, CON DOS FUERA DE LA NOMINA")
        ultima, faltan = arneses_que_faltan(nomina, tmp)
        print("   ultima vuelta de la nomina: %s" % ultima)
        print("   CIFRA que faltan: %d (%s)" % (len(faltan), ", ".join(faltan)))
        casos.append(("la_ultima_vuelta_se_computa_de_la_nomina", ultima, 110))
        casos.append(("y_ve_LOS_DOS_que_faltan", faltan,
                      ["vuelta120_tarea3_mutacion_fuera.py",
                       "vuelta121_tarea4_mutacion_tambien_fuera.py"]))
        print("")

        print("C) SI ENTRAN EN LA NOMINA, DEJA DE FALTAR NADIE")
        completa = nomina + [("vuelta120_tarea3_mutacion_fuera.py", False),
                             ("vuelta121_tarea4_mutacion_tambien_fuera.py", False)]
        _u2, faltan2 = arneses_que_faltan(completa, tmp)
        print("   CIFRA que faltan tras meterlos: %d" % len(faltan2))
        casos.append(("metidos_en_la_nomina_ya_no_faltan", len(faltan2), 0))
        print("")

        print("D) LOS ANTERIORES A LA ULTIMA VUELTA NO SE RECLAMAN, Y SE DICE POR QUE")
        print("   (la regla de esta bateria nace en la vuelta 144 y no dice si")
        print("   alcanza a lo anterior: ensancharla sin adjudicacion seria")
        print("   moverle la vara a nadie)")
        solo_una = [("vuelta120_tarea3_mutacion_fuera.py", False),
                    ("vuelta121_tarea4_mutacion_tambien_fuera.py", False)]
        _u3, faltan3 = arneses_que_faltan(solo_una, tmp)
        print("   con la nomina en la vuelta 121, faltan: %d (%s)"
              % (len(faltan3), ", ".join(faltan3) or "ninguno"))
        casos.append(("los_anteriores_no_se_reclaman", len(faltan3), 0))
        print("")

        print("E) Y SOBRE EL REPO DE VERDAD, HOY")
        ultima_real, faltan_real = arneses_que_faltan()
        print("   ultima vuelta de la nomina real: %s" % ultima_real)
        print("   CIFRA que faltan de verdad: %d (%s)"
              % (len(faltan_real), ", ".join(faltan_real) or "ninguno"))
        casos.append(("en_el_repo_de_hoy_no_falta_ninguno", len(faltan_real), 0))
        print("")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
        print("   P.16: el temporal se retira. Existe todavia: %s" % os.path.exists(tmp))
        print("")

    print("F) PASADA 1, LOS CASOS TAL CUAL")
    fallos = 0
    for nombre, real, esperado in casos:
        ok = (real == esperado)
        print("   %-46s %s   (real=%r esperado=%r)"
              % (nombre, "PASA" if ok else "FALLA", real, esperado))
        if not ok:
            fallos += 1
    print("   CIFRA casos: %d | pasan: %d | fallan: %d"
          % (len(casos), len(casos) - fallos, fallos))
    print("")
    print("G) PASADA 2, SE MUTA EL VALOR ESPERADO Y CADA CASO TIENE QUE CAER")
    caen = 0
    for nombre, real, esperado in casos:
        if isinstance(esperado, list):
            mutado = esperado + ["vuelta999_de_mentira_mutacion.py"]
        else:
            mutado = esperado + 1
        cae = (real != mutado)
        print("   %-46s %s" % (nombre, "CAE" if cae else "NO CAE (ROJO)"))
        if cae:
            caen += 1
    print("   CIFRA casos que CAEN: %d de %d" % (caen, len(casos)))
    print("")
    if fallos or caen != len(casos):
        print("ROJO DE LA MUTACION: la mirada sobre si misma no se comporta.")
        print("FIN")
        return 1
    print("VERDE DE LA MUTACION: %d casos, los %d pasan y los %d CAEN al mutarles el "
          "valor esperado. La mirada VE los que faltan, deja de verlos cuando entran, "
          "no reclama los anteriores a su vara, y sobre el repo de hoy no falta "
          "ninguno." % (len(casos), len(casos), len(casos)))
    print("FIN")
    return 0

'''

LLAMADA_VIEJA = '''    print("=" * 78)
    print("LAS %d MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO." % len(VIEJAS))
'''

LLAMADA_NUEVA = '''    print("=" * 78)
    print("LAS %d MUTACIONES VIEJAS. ANCLA PERDIDA CUENTA COMO ROJO." % len(VIEJAS))
'''

AUTOMIRADA = '''    # LA GUARDA SE MIRA A SI MISMA ANTES DE MEDIR NADA (vuelta 163, TAREA 2).
    # Va PRIMERO a proposito: si la nomina esta incompleta, el resto de esta
    # salida es un verde sobre una parte, y eso es lo que hay que ver arriba y
    # no enterrado al final.
    ultima_de_la_nomina, faltan_en_la_nomina = arneses_que_faltan()
    print("")
    print("  LA NOMINA, MIRADA CONTRA scripts/loop/ (adjudicacion 6.8 del acta 162)")
    print("  CIFRA entradas en la nomina: %d" % len(VIEJAS))
    print("  CIFRA arneses de mutacion en scripts/loop/: %d" % len(arneses_del_directorio()))
    print("  CIFRA ultima vuelta representada en la nomina: %s" % ultima_de_la_nomina)
    print("  CIFRA arneses POSTERIORES a esa vuelta que se quedan FUERA: %d"
          % len(faltan_en_la_nomina))
    for n in faltan_en_la_nomina:
        print("      FUERA DE LA NOMINA: %s" % n)
    if not faltan_en_la_nomina:
        print("      (ninguno)")
    print("")

'''

MODO_MUTACION = '''    ap.add_argument("--mutar-nomina", dest="mutar_nomina", action="store_true",
                    help="vuelta 163, TAREA 2: prueba de mutacion de la mirada de "
                         "la nomina sobre si misma, sobre un directorio fabricado")
'''

VEREDICTO_VIEJO = '''    if perdidas or no_mordio or no_reprod:
        print("")
        print("ROJO: %d con el ancla perdida, %d que no mordieron y %d cuya salida "
              "sellada NO SE REPITE." % (len(perdidas), len(no_mordio), len(no_reprod)))
        print("FIN")
        return 1
    print("")
    print("VERDE: las %d mutaciones viejas corren, muerden, y sus salidas selladas "
          "salen IDENTICAS en dos corridas seguidas." % len(filas))
    print("FIN")
    return 0
'''

VEREDICTO_NUEVO = '''    # LA MIRADA SOBRE SI MISMA CUENTA PARA EL ROJO (adjudicacion 6.8 del acta
    # 162). Se recomputa AQUI, al cierre de la corrida, y no se hereda de la
    # cabecera: el estado al cierre se mide al cierre.
    _ultima, faltan_al_cierre = arneses_que_faltan()
    print("  CIFRA arneses POSTERIORES a la nomina que se quedan FUERA (recomputado "
          "al cierre): %d" % len(faltan_al_cierre))
    for n in faltan_al_cierre:
        print("      FUERA DE LA NOMINA: %s" % n)

    if perdidas or no_mordio or no_reprod or faltan_al_cierre:
        print("")
        if faltan_al_cierre:
            print("ROJO: %d arnes(es) de mutacion nacidos despues de la vuelta %s se "
                  "quedan FUERA de esta nomina, y la regla escrita en este mismo "
                  "fichero dice que una mutacion entra en la vuelta SIGUIENTE a la que "
                  "nace, no mas tarde. La lista entera: %s"
                  % (len(faltan_al_cierre), _ultima, ", ".join(faltan_al_cierre)))
        if perdidas or no_mordio or no_reprod:
            print("ROJO: %d con el ancla perdida, %d que no mordieron y %d cuya salida "
                  "sellada NO SE REPITE." % (len(perdidas), len(no_mordio), len(no_reprod)))
        print("FIN")
        return 1
    print("")
    print("VERDE: las %d mutaciones viejas corren, muerden, sus salidas selladas "
          "salen IDENTICAS en dos corridas seguidas, y NINGUN arnes posterior a la "
          "vuelta %s se queda fuera de la nomina." % (len(filas), _ultima))
    print("FIN")
    return 0
'''


DESPACHO_NOMINA = '''
    if a.mutar_nomina:
        return prueba_de_la_nomina()
'''


def main():
    s = io.open(P, encoding="utf-8").read()
    if "arneses_que_faltan" in s:
        print("YA ESTABA: la mirada sobre si misma ya vive en la bateria.")
        return 0
    for viejo in (FIN_VIEJAS, LLAMADA_VIEJA, VEREDICTO_VIEJO):
        if viejo not in s:
            print("PARADA: no se halla el trozo que hay que sustituir:")
            print(repr(viejo[:90]))
            return 1
    s = s.replace(FIN_VIEJAS, FIN_VIEJAS[:-len("]\n")] + ENTRADAS)
    # el bloque MIRARSE va justo antes de `def correr(`
    ancla = "\ndef correr(script, sujeto=None, base=None):"
    if ancla not in s:
        print("PARADA: no se halla el ancla de `def correr`.")
        return 1
    s = s.replace(ancla, MIRARSE + ancla, 1)
    s = s.replace(LLAMADA_VIEJA, LLAMADA_NUEVA)
    # la automirada va tras la cabecera del rotulo, antes de `sujeto = None`
    ancla2 = "    sujeto = None\n    tmp = None\n"
    if ancla2 not in s:
        print("PARADA: no se halla el ancla del cuerpo de main.")
        return 1
    s = s.replace(ancla2, AUTOMIRADA + ancla2, 1)
    ancla3 = '    ap.add_argument("--mutar-ancla", dest="mutar", action="store_true")\n'
    if ancla3 not in s:
        print("PARADA: no se halla el ancla de los argumentos.")
        return 1
    s = s.replace(ancla3, ancla3 + MODO_MUTACION, 1)
    ancla4 = "    if a.mutar_repro:\n        return prueba_de_reproducibilidad()\n"
    if ancla4 not in s:
        print("PARADA: no se halla el ancla del despacho de modos.")
        return 1
    s = s.replace(ancla4, ancla4 + DESPACHO_NOMINA, 1)
    s = s.replace(VEREDICTO_VIEJO, VEREDICTO_NUEVO)
    if "\nimport re\n" not in s:
        s = s.replace("\nimport shutil\n", "\nimport re\nimport shutil\n", 1)
    io.open(P, "w", encoding="utf-8", newline="\n").write(s)
    print("VERDE: nomina ampliada y mirada sobre si misma insertada.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
