# -*- coding: utf-8 -*-
r"""vuelta184_tarea1c_mutacion_estimacion.py . CASO POSITIVO POR MUTACION DE LA
ESTIMACION DEL `--plan` CON SU CORTE PEGADO (vuelta 184, TAREA 1.c).

POR QUE NACE, Y NO ES POR GUSTO. Es la ESCALADA que el acta 184 encarga en su
seccion 9 por `AUDITOR.md` 1.2, sobre su caida `E.1`. La racha de caidas de
reporte esta en DOS, y el remedio que el acta 182 encargo esta puesto DONDE
CAERIA LA TERCERA SI CAYERA EN EL VEREDICTO; la de la 184 cayo en OTRA
SUPERFICIE, la estimacion sin corte, y ahi no habia guarda. Esto es esa guarda.

LA CAIDA, CON SU MEDICION. El reporte de la vuelta 183 publico DOS VECES que el
`--plan` *"de hoy"* estimaba entre **36,6 y 47,7 minutos** para la nomina entera,
cuando la nomina de ese dia ya era de **112** y el `--plan` de ese dia decia
**37,0 y 48,2**. La aritmetica dice de donde salio: 111 por 0,33 da 36,6 y 111
por 0,43 da 47,7. **La cifra publicada era la de una nomina de 111**, o sea la de
antes de que esa misma vuelta la subiera a 112 tres parrafos mas arriba.

QUE PRUEBA ESTE ARNES, Y SON TRES COSAS QUE FALLAN POR SEPARADO:

  1) QUE LA LINEA SALE CON SU CORTE. `linea_de_estimacion()` es PURA y su salida
     tiene que llevar, EN LA MISMA LINEA, el tamano de nomina y el `HEAD` sobre
     el que se computo. Una linea sin corte devuelve `None` en
     `corte_de_la_estimacion()` y este arnes la declara ROJA.

  2) QUE EL CORTE NO MIENTE. Una linea que lleva corte pero cuyo corte dice OTRA
     nomina es una averia distinta de no llevarlo, y `corte_calza()` las
     distingue. Las dos son rojo.

  3) QUE EL `--plan` DE VERDAD LO CUMPLE. Las dos mitades de arriba son puras y
     se pueden satisfacer sin que el lanzador las use. Por eso el bloque C corre
     `--plan` en un proceso de verdad, localiza sus lineas de `ESTIMACION` y
     exige que TODAS lleven corte y que ese corte coincida con la nomina que ESA
     MISMA CORRIDA imprime. Si alguien devuelve las dos lineas a su forma vieja,
     este bloque CAE.

NINGUN VEREDICTO ES UNA CONSTANTE LITERAL (`EJECUTOR.md` 1, EL CASO ROJO SE
PRUEBA POR MUTACION): todos salen de correr las funciones reales del modulo o de
leer la salida real del `--plan`, y la segunda pasada muta cada valor esperado y
exige que el caso CAIGA.

SUJETO: la nomina real solo se toca para CONTARLA. No se escribe nada en el repo,
no se corre ningun tramo y no se toca `dataset/`. La unica salida es
`docs/loop/SALIDA_V184_T1C_MUTACION_ESTIMACION.txt`.

USO:  python scripts/loop/vuelta184_tarea1c_mutacion_estimacion.py
"""
import io
import os
import re
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

sys.path.insert(0, AQUI)
import vuelta183_bateria_por_tramos as L   # noqa: E402
import verificar_mutaciones_viejas as B   # noqa: E402

LANZADOR_REL = "scripts/loop/vuelta183_bateria_por_tramos.py"


def prueba():
    sys.stdout.reconfigure(encoding="utf-8")
    salida = []
    w = salida.append
    w("=" * 78)
    w("VUELTA 184, TAREA 1.c: CASO POSITIVO POR MUTACION DE LA ESTIMACION CON SU CORTE")
    w("=" * 78)
    w("")
    casos = []

    w("A) LA FUNCION PURA, TUMBADA SIN CORRER NINGUN PROCESO")
    linea = L.linea_de_estimacion("de la nomina entera", 37.0, 48.2, 112, "abc123def456")
    w("   la linea que produce, entera:")
    w("      | %s" % linea)
    leido = L.corte_de_la_estimacion(linea)
    w("   corte leido de vuelta de esa misma linea: %r" % (leido,))
    casos.append(("A_la_linea_lleva_su_corte_y_se_lee_de_vuelta",
                  leido, ("abc123def456", 112)))
    casos.append(("A_la_linea_dice_las_dos_cifras_de_la_estimacion",
                  ("entre 37.0 y 48.2" in linea), True))

    # EL CASO ROJO, Y SE PRUEBA CORRIENDOLO: una linea SIN corte tiene que dar
    # None. Es la forma VIEJA de la linea, escrita aqui tal cual era.
    vieja = ("  ESTIMACION minutos de la nomina entera: entre %.1f y %.1f"
             % (112 * 0.33, 112 * 0.43))
    w("   LA FORMA VIEJA DE LA LINEA, LA QUE CAUSO LA CAIDA `E.1`, ESCRITA AQUI:")
    w("      | %s" % vieja)
    w("   corte leido de la forma vieja: %r" % (L.corte_de_la_estimacion(vieja),))
    casos.append(("A_la_forma_VIEJA_no_tiene_corte_y_se_detecta",
                  L.corte_de_la_estimacion(vieja), None))
    w("")

    w("B) EL CORTE QUE MIENTE, QUE ES UNA AVERIA DISTINTA DE NO LLEVARLO")
    w("   La misma linea de arriba dice nomina 112. Se le pregunta por 112 y por")
    w("   111, que es justo la cifra vencida que el reporte de la 183 publico.")
    w("   corte_calza(linea, 112) -> %s" % L.corte_calza(linea, 112))
    w("   corte_calza(linea, 111) -> %s" % L.corte_calza(linea, 111))
    w("   corte_calza(forma vieja, 112) -> %s" % L.corte_calza(vieja, 112))
    casos.append(("B_el_corte_bueno_calza", L.corte_calza(linea, 112), True))
    casos.append(("B_un_corte_de_otra_nomina_NO_calza", L.corte_calza(linea, 111), False))
    casos.append(("B_una_linea_sin_corte_NO_calza", L.corte_calza(vieja, 112), False))
    w("")

    w("C) EL --plan DE VERDAD, CORRIDO EN UN PROCESO, Y SUS LINEAS DE ESTIMACION")
    w("   (las dos mitades de arriba son puras y se pueden cumplir sin que el")
    w("    lanzador las use. Este bloque mira la salida REAL)")
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run([sys.executable, LANZADOR_REL, "--plan"],
                       cwd=RAIZ, capture_output=True, env=env)
    texto = (r.stdout.decode("utf-8", errors="replace")
             + r.stderr.decode("utf-8", errors="replace")).replace(chr(13), "")
    w("   EXITCODE de --plan: %d" % r.returncode)
    casos.append(("C_el_plan_sale_verde", r.returncode, 0))

    lineas_plan = texto.split(NL)
    m_nom = [l for l in lineas_plan if "CIFRA entradas de la nomina:" in l]
    nomina_de_la_corrida = (int(re.search(r"(\d+)", m_nom[0]).group(1))
                            if m_nom else -1)
    w("   CIFRA entradas de la nomina que ESA MISMA CORRIDA imprime: %d"
      % nomina_de_la_corrida)
    w("   CIFRA entradas de la nomina contada aqui, en este proceso: %d" % len(B.VIEJAS))
    casos.append(("C_la_nomina_del_plan_es_la_nomina_de_hoy",
                  nomina_de_la_corrida, len(B.VIEJAS)))

    est = [l for l in lineas_plan if "ESTIMACION minutos" in l]
    w("   CIFRA lineas de ESTIMACION halladas en la salida real: %d" % len(est))
    for l in est:
        w("      | %s" % l.rstrip())
    con_corte = [l for l in est if L.corte_de_la_estimacion(l) is not None]
    calzan = [l for l in est if L.corte_calza(l, nomina_de_la_corrida)]
    w("   de esas, LAS QUE LLEVAN CORTE: %d" % len(con_corte))
    w("   de esas, LAS QUE ADEMAS LO LLEVAN BIEN (calza con la nomina de la corrida): %d"
      % len(calzan))
    casos.append(("C_hay_dos_lineas_de_estimacion", len(est), 2))
    casos.append(("C_TODAS_llevan_su_corte", len(con_corte), len(est)))
    casos.append(("C_y_el_corte_de_TODAS_calza_con_la_nomina_de_la_corrida",
                  len(calzan), len(est)))
    heads = sorted(set(L.corte_de_la_estimacion(l)[0] for l in con_corte))
    w("   HEAD que declaran las lineas con corte: %s" % ", ".join(heads))
    casos.append(("C_las_dos_lineas_declaran_UN_SOLO_head", len(heads), 1))
    w("")

    w("D) LA CIFRA VENCIDA DE LA 183, RECONSTRUIDA PARA QUE SE VEA DE DONDE SALIO")
    w("   Con la linea nueva, una nomina de 111 y una de 112 producen DOS TEXTOS")
    w("   DISTINTOS, y el que se copie lleva escrito de cual es. Con la vieja, los")
    w("   dos textos solo se distinguian por un decimal que nadie coteja.")
    n111 = L.linea_de_estimacion("de la nomina entera", 111 * 0.33, 111 * 0.43,
                                 111, "abc123def456")
    n112 = L.linea_de_estimacion("de la nomina entera", 112 * 0.33, 112 * 0.43,
                                 112, "abc123def456")
    w("      | %s" % n111)
    w("      | %s" % n112)
    casos.append(("D_las_dos_lineas_se_distinguen_por_su_corte",
                  L.corte_de_la_estimacion(n111)[1]
                  != L.corte_de_la_estimacion(n112)[1], True))
    casos.append(("D_la_de_111_NO_calza_con_la_nomina_de_hoy",
                  L.corte_calza(n111, len(B.VIEJAS)), False))
    w("")

    w("E) PASADA 1, LOS CASOS TAL CUAL")
    fallos = 0
    for nombre, real, esperado in casos:
        ok = (real == esperado)
        w("   %-56s %s   (real=%r esperado=%r)"
          % (nombre, "PASA" if ok else "FALLA", real, esperado))
        if not ok:
            fallos += 1
    w("   CIFRA casos: %d | pasan: %d | fallan: %d"
      % (len(casos), len(casos) - fallos, fallos))
    w("")

    w("F) PASADA 2, SE MUTA EL VALOR ESPERADO Y CADA CASO TIENE QUE CAER")
    caen = 0
    for nombre, real, esperado in casos:
        if isinstance(esperado, bool):
            mutado = not esperado
        elif isinstance(esperado, int):
            mutado = esperado + 1
        elif esperado is None:
            mutado = ("mutado", 0)
        elif isinstance(esperado, tuple):
            mutado = tuple(list(esperado) + ["mutado"])
        else:
            mutado = str(esperado) + "_mutado"
        cae = (real != mutado)
        w("   %-56s %s   (esperado mutado=%r)"
          % (nombre, "CAE" if cae else "NO CAE", mutado))
        if cae:
            caen += 1
    w("   CIFRA casos que caen al mutar el esperado: %d de %d" % (caen, len(casos)))
    w("")

    veredicto = "VERDE" if (fallos == 0 and caen == len(casos)) else "ROJO"
    if veredicto == "VERDE":
        w("VERDE: los %d casos pasan tal cual y los %d caen al mutar el esperado."
          % (len(casos), len(casos)))
        w("Y LO QUE ESTE ARNES GARANTIZA: si alguien devuelve las dos lineas de")
        w("ESTIMACION del lanzador a su forma sin corte, los casos")
        w("C_TODAS_llevan_su_corte y")
        w("C_y_el_corte_de_TODAS_calza_con_la_nomina_de_la_corrida CAEN.")
    else:
        w("ROJO: fallos=%d, casos que no caen=%d" % (fallos, len(casos) - caen))

    t = NL.join(salida) + NL
    ruta = os.path.join(LOOP, "SALIDA_V184_T1C_MUTACION_ESTIMACION.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0 if veredicto == "VERDE" else 1


if __name__ == "__main__":
    raise SystemExit(prueba())
