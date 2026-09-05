# -*- coding: utf-8 -*-
r"""vuelta177_tarea1e_mutacion_correcciones_chicas.py . EL CASO POSITIVO POR
MUTACION DE LAS DOS CORRECCIONES CHICAS DE LA TAREA 1.e DE LA VUELTA 177.

DOS SUJETOS, LOS DOS ADJUDICADOS POR EL ACTA 176:

  1. `D.5` (acta 176, punto 7.5). `scripts/loop/vuelta176_bateria_por_tramos.py`
     ESCRIBE SU PROPIA TRANSCRIPCION FUERA DE `docs/loop/` Y LA COPIA DENTRO AL
     TERMINAR, en vez de dejar que acabe donde la meta quien lo llame.
  2. Acta 176, seccion 9 punto 4. `scripts/loop/tallar_cabecera_reporte.py`
     SELLA SU PROPIO RECHAZO en `docs/loop/SALIDA_V<N>_TALLADOR_RECHAZO.txt`,
     con las celdas que no pudo leer y de que lado esta cada una.

POR QUE UNA CORRECCION DE UNA LINEA TAMBIEN LLEVA ARNES, y no es celo: las dos
correcciones son EXACTAMENTE de la especie que esta casa lleva castigando desde
la vuelta 15, la de dar por hecho lo que no se ha medido. Decir "ya escribe
fuera" sin correrlo es la misma frase que "el diff sale vacio".

COMO SE PRUEBA EL `D.5` SIN CORRER LA BATERIA, QUE ES LO IMPORTANTE. Esta vuelta
NO ES DE BATERIA (acta 176, punto 7.8: la proxima es la 181), asi que correr un
tramo de verdad estaria prohibido y ademas mutaria `dataset/`. Lo que se hace es
sustituir `correr_tramo` por un doble que no corre nada y solo imprime, y llamar
a `main()` con `--tramo 1`: ASI SE EJERCITA EL CAMINO REAL DEL CODIGO (el
desdoble, el fichero de fuera, el copiado de dentro y el `finally`) SIN CORRER
UNA SOLA ENTRADA DE LA NOMINA. El doble comprueba, DESDE DENTRO y mientras el
tramo "corre", que el fichero de `docs/loop/` TODAVIA NO EXISTE, que es la
propiedad que la correccion promete y la unica que importa.

Y SE LIMPIA LO QUE ENSUCIA: el fichero que el doble deja en `docs/loop/` se
borra al terminar y se comprueba que se borro. Un arnes que deja basura con
nombre de salida de verdad es peor que no tenerlo.

CERO ESCRITURAS PERMANENTES. El sellado del tallador se prueba con su `LOOP`
apuntado a un directorio temporal.

USO:  python scripts/loop/vuelta177_tarea1e_mutacion_correcciones_chicas.py
"""
import io
import os
import shutil
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import tallar_cabecera_reporte as TALL   # noqa: E402
import vuelta176_bateria_por_tramos as LANZ   # noqa: E402

NL = chr(10)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 177, TAREA 1.e: LAS DOS CORRECCIONES CHICAS, PROBADAS")
    print("=" * 78)
    print("")

    casos = []

    # ------------------------------------------------------------ SUJETO 1
    print("A) SUJETO 1, `D.5`: LA TRANSCRIPCION DEL LANZADOR FUERA DE docs/loop/")
    print("   sujeto: scripts/loop/vuelta176_bateria_por_tramos.py")
    print("")

    print("A.1 LO QUE EL FICHERO DICE DE SI MISMO, LEIDO Y NO RECORDADO")
    texto_lanz = io.open(os.path.join(AQUI, "vuelta176_bateria_por_tramos.py"),
                         encoding="utf-8").read()
    for marca, esperado in (("class Desdoble", True),
                            ("def nombre_transcripcion", True),
                            ("lanzador_en_curso.txt", True)):
        hay = marca in texto_lanz
        print("   contiene %-32s -> %s" % (repr(marca), hay))
        casos.append(("1_el_lanzador_lleva_%s" % marca.split()[-1], hay, esperado))
    print("")

    print("A.2 EL CAMINO REAL, EJERCITADO CON UN DOBLE DE `correr_tramo`")
    print("   (NO se corre ni una entrada de la nomina: esta vuelta no es de")
    print("    bateria y ademas la bateria muta dataset/)")
    nombre = LANZ.nombre_transcripcion(1)
    dentro = os.path.join(LANZ.LOOP, nombre)
    ya_estaba = os.path.exists(dentro)
    print("   docs/loop/%s existia ANTES: %s" % (nombre, ya_estaba))
    casos.append(("1_no_existia_antes", ya_estaba, False))

    visto = {}

    def doble(n, tramos):
        # ESTO CORRE MIENTRAS EL TRAMO "CORRE": es el unico momento en que se
        # puede comprobar la propiedad que la correccion promete.
        visto["existe_dentro_mientras_corre"] = os.path.exists(dentro)
        visto["stdout_es_desdoble"] = isinstance(sys.stdout, LANZ.Desdoble)
        visto["fichero_de_fuera"] = getattr(sys.stdout, "f", None)
        visto["ruta_de_fuera"] = getattr(getattr(sys.stdout, "f", None), "name", "")
        print("   (desde dentro del tramo) esto se esta escribiendo al doble")
        return 0

    real = LANZ.correr_tramo
    argv = sys.argv[:]
    try:
        LANZ.correr_tramo = doble
        sys.argv = ["vuelta176_bateria_por_tramos.py", "--tramo", "1"]
        codigo = LANZ.main()
    finally:
        LANZ.correr_tramo = real
        sys.argv = argv

    print("   codigo que devuelve main(): %s" % codigo)
    casos.append(("1_main_devuelve_lo_del_tramo", codigo, 0))
    print("   MIENTRAS EL TRAMO CORRIA, docs/loop/%s existia: %s"
          % (nombre, visto.get("existe_dentro_mientras_corre")))
    casos.append(("1_NO_existe_dentro_mientras_corre",
                  visto.get("existe_dentro_mientras_corre"), False))
    print("   MIENTRAS EL TRAMO CORRIA, sys.stdout era el Desdoble: %s"
          % visto.get("stdout_es_desdoble"))
    casos.append(("1_stdout_desdoblado_durante_el_tramo",
                  visto.get("stdout_es_desdoble"), True))
    ruta_fuera = visto.get("ruta_de_fuera") or ""
    fuera_de_loop = bool(ruta_fuera) and not os.path.abspath(ruta_fuera).startswith(
        os.path.abspath(LANZ.LOOP) + os.sep)
    print("   la ruta a la que escribia: %s" % ruta_fuera)
    print("   esa ruta esta FUERA de docs/loop/: %s" % fuera_de_loop)
    casos.append(("1_la_ruta_de_trabajo_esta_fuera_de_loop", fuera_de_loop, True))

    existe_despues = os.path.exists(dentro)
    print("   AL TERMINAR, docs/loop/%s existe: %s" % (nombre, existe_despues))
    casos.append(("1_SI_existe_al_terminar", existe_despues, True))
    if existe_despues:
        cont = io.open(dentro, encoding="utf-8", errors="replace").read()
        tiene = "esto se esta escribiendo al doble" in cont
        print("   y trae lo que se imprimio durante el tramo: %s" % tiene)
        casos.append(("1_la_transcripcion_trae_lo_impreso", tiene, True))
        os.remove(dentro)
    print("   LIMPIEZA: docs/loop/%s borrado: %s" % (nombre, not os.path.exists(dentro)))
    casos.append(("1_limpieza_del_arnes", os.path.exists(dentro), False))
    print("")

    # ------------------------------------------------------------ SUJETO 2
    print("B) SUJETO 2: EL TALLADOR SELLA SU PROPIO RECHAZO")
    print("   sujeto: scripts/loop/tallar_cabecera_reporte.py, sellar_rechazo()")
    print("")
    tmp = tempfile.mkdtemp(prefix="v177_tallador_")
    loop_real = TALL.LOOP
    try:
        TALL.LOOP = tmp
        FALLOS = [
            "no existe la salida SALIDA_V800_GATE0_CMD1_APERTURA.txt",
            "sin texto para censo (nodos) APERTURA",
            "sin texto para desfase CIERRE",
            "no existe el sello SALIDA_V800_HEAD_CIERRE.txt",
            "git log de la rama no trae ningun commit del acta",
        ]
        print("B.1 CINCO CELDAS FABRICADAS: 2 de APERTURA, 2 de CIERRE, 1 SIN LADO")
        ruta = TALL.sellar_rechazo(800, FALLOS)
        print("   ruta escrita: %s" % (ruta or "(ninguna)"))
        casos.append(("2_devuelve_una_ruta", ruta is not None, True))
        casos.append(("2_el_fichero_existe", bool(ruta) and os.path.exists(ruta), True))
        nombre_ok = bool(ruta) and os.path.basename(ruta) == "SALIDA_V800_TALLADOR_RECHAZO.txt"
        print("   se llama SALIDA_V800_TALLADOR_RECHAZO.txt: %s" % nombre_ok)
        casos.append(("2_el_nombre_es_el_que_el_acta_pide", nombre_ok, True))

        cont = io.open(ruta, encoding="utf-8").read() if ruta else ""
        print("   CIFRA bytes del sello: %d" % len(cont.encode("utf-8")))
        casos.append(("2_no_mide_cero_bytes", len(cont) > 0, True))

        print("B.2 LAS CIFRAS DEL SELLO, LEIDAS DE SU PROPIO TEXTO")
        for linea, esperado in (("CIFRA celdas que no se pudieron leer: 5", True),
                                ("CIFRA de ellas del lado APERTURA: 2", True),
                                ("CIFRA de ellas del lado CIERRE  : 2", True),
                                ("CIFRA de ellas del lado SIN LADO: 1", True)):
            hay = linea in cont
            print("   %-52s -> %s" % (repr(linea), hay))
            casos.append(("2_sello_dice_%s" % linea.split(":")[0].replace(" ", "_")[:34],
                          hay, esperado))

        print("B.3 LAS CINCO CELDAS ESTAN UNA A UNA, CON SU LADO")
        todas = all(f in cont for f in FALLOS)
        print("   las 5 celdas aparecen en el sello: %s" % todas)
        casos.append(("2_las_celdas_estan_una_a_una", todas, True))
        # LA ETIQUETA VA ACOLCHADA A OCHO, o sea `[CIERRE  ]` y no `[CIERRE]`, y
        # esta linea lo dice porque la primera version de este arnes NO lo decia
        # y fallo aqui: el sello estaba bien y la assertion estaba mal.
        con_lado = all(("[%-8s]" % l) in cont for l in ("APERTURA", "CIERRE", "SIN LADO"))
        print("   los tres lados aparecen etiquetados: %s" % con_lado)
        casos.append(("2_cada_celda_lleva_su_lado", con_lado, True))

        print("B.4 EL SELLO NO REPARTE A OJO LO QUE NO NOMBRA NINGUN LADO")
        print("   (una celda que no dice de que lado es NO se cuenta como apertura")
        print("    ni como cierre: se cuenta aparte, que es lo unico honesto)")
        casos.append(("2_sin_lado_no_se_reparte", "SIN LADO: 1" in cont, True))

        print("B.5 MUTACION: SI LAS CELDAS CAMBIAN, EL SELLO CAMBIA")
        ruta2 = TALL.sellar_rechazo(801, FALLOS[:2])
        cont2 = io.open(ruta2, encoding="utf-8").read()
        print("   con 2 celdas en vez de 5, dice 2: %s"
              % ("CIFRA celdas que no se pudieron leer: 2" in cont2))
        casos.append(("2_con_dos_celdas_dice_dos",
                      "CIFRA celdas que no se pudieron leer: 2" in cont2, True))
        casos.append(("2_los_dos_sellos_no_son_iguales", cont == cont2, False))
    finally:
        TALL.LOOP = loop_real
        shutil.rmtree(tmp, ignore_errors=True)
        print("   el directorio temporal se borro: %s" % (not os.path.exists(tmp)))
        print("   y TALL.LOOP volvio a su sitio: %s" % (TALL.LOOP == loop_real))
    print("")

    print("C) PASADA 1, LOS CASOS TAL CUAL")
    fallos = 0
    for nombre_c, real_v, esperado in casos:
        ok = (real_v == esperado)
        print("   %-54s %s   (real=%r esperado=%r)"
              % (nombre_c, "PASA" if ok else "FALLA", real_v, esperado))
        if not ok:
            fallos += 1
    print("   CIFRA casos: %d | pasan: %d | fallan: %d"
          % (len(casos), len(casos) - fallos, fallos))
    print("")

    print("D) PASADA 2, SE MUTA EL VALOR ESPERADO Y CADA CASO TIENE QUE CAER")
    caen = 0
    for nombre_c, real_v, esperado in casos:
        mutado = (not esperado) if isinstance(esperado, bool) else esperado + 1
        cae = (real_v != mutado)
        print("   %-54s %s   (esperado mutado=%r)"
              % (nombre_c, "CAE" if cae else "NO CAE", mutado))
        if cae:
            caen += 1
    print("   CIFRA casos que caen al mutar el esperado: %d de %d" % (caen, len(casos)))
    print("")

    if fallos == 0 and caen == len(casos):
        print("VERDE: los %d casos pasan tal cual y los %d caen al mutar el esperado."
              % (len(casos), len(casos)))
        return 0
    print("ROJO: fallos=%d, casos que no caen=%d" % (fallos, len(casos) - caen))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
