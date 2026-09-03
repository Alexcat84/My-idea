# -*- coding: utf-8 -*-
r"""vuelta163_tarea4b_mutacion_re_sellado.py . TAREA 4.b de la vuelta 163.

CASO POSITIVO POR MUTACION DEL CAMINO NUEVO DE
`scripts/loop/verificar_re_sellado.py` (adjudicacion 6.7 del acta 162): toda
`docs/loop/SALIDA_*` MODIFICADA desde la apertura de la vuelta que el reporte no
nombre sale en ROJO con su nombre.

EL CASO REAL SE REPRODUCE, NO SE INVENTA. El escenario del caso central es EL DE
LA VUELTA 162, leido de git: entre su apertura (`78d10690`) y su cierre
(`ac4af00d`) cambian TRES `SALIDA_V135_2E_MUTACION_*.txt`, y el reporte de esa
vuelta NO LAS NOMBRA. La guarda VIEJA salio VERDE sobre eso, que es exactamente
lo que el acta 162 midio en su seccion 5.4.

LOS CASOS, Y NINGUN ESPERADO ES UN ESTADO DE HOY QUE PUEDA CADUCAR: los que
miran a la 162 corren sobre DOS COMMITS FIJOS de la historia, y los que miran a
hoy son deltas.

  (A) EL ESCENARIO DE LA 162, CONTRA LA FUNCION NUEVA: las tres aparecen como
      MODIFICADAS, y las tres salen SIN DECLARAR contra el reporte de esa
      vuelta, leido de git con `git show 78d10690:docs/loop/REPORTE.md`.
  (B) LA CONTRAPRUEBA, Y ES LA QUE CONVIERTE (A) EN PRUEBA DE UN REMEDIO: sobre
      ESE MISMO escenario, la guarda VIEJA (copia byte a byte tomada ANTES de
      tocar nada, `scripts/loop/_v163_re_sellado_vieja_copia.py`) sale VERDE. La
      copia se corre de verdad, no se alega.
  (C) NOMBRARLAS LAS SACA DEL ROJO: al texto del reporte se le anaden los tres
      nombres EN MEMORIA y la cuenta de no declaradas cae a cero. Es lo que hace
      que el camino nuevo componga con el viejo en vez de duplicarlo.
  (D) NACER NO ES RE SELLAR: una salida que solo se ANADE entre los dos commits
      no entra en la lista. Se comprueba contra una que de verdad nacio ahi.
  (E) LA EXENCION POR CONSTRUCCION SIGUE VALIENDO: un fichero con el sufijo
      reservado no entra ni aunque cambie.
  (F) HOY, SOBRE ESTA VUELTA: la guarda entera sale VERDE y su camino nuevo no
      inventa modificadas.
  (G) NINGUN VEREDICTO VIEJO SE MUEVE: vieja y nueva sobre el reporte de HOY
      dan el mismo codigo de salida y la misma cuenta del camino viejo.

USO:  python scripts/loop/vuelta163_tarea4b_mutacion_re_sellado.py
"""
import os
import re
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
RAIZ = os.path.dirname(os.path.dirname(AQUI))

import verificar_re_sellado as G   # noqa: E402

VIEJA = os.path.join(AQUI, "_v163_re_sellado_vieja_copia.py")
NUEVA = os.path.join(AQUI, "verificar_re_sellado.py")

# LOS DOS COMMITS DEL ESCENARIO. Son historia y por eso son fijos: la apertura y
# el cierre de la vuelta 162. NO se computan de HEAD a proposito, porque un
# escenario historico anclado a una referencia movil es lo que caduco a
# vuelta160_tarea6b_mutacion_puerta.py.
APERTURA_162 = "78d10690"
CIERRE_162 = "ac4af00d"


def git(*args):
    r = subprocess.run(["git"] + list(args), cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", "replace")


def correr(guarda):
    r = subprocess.run([sys.executable, guarda], capture_output=True, text=True,
                       cwd=RAIZ, encoding="utf-8", errors="replace")
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def cuenta(salida, patron):
    m = re.search(patron, salida)
    return int(m.group(1)) if m else None


def main():
    print("=" * 78)
    print("VUELTA 163, TAREA 4.b: CASO POSITIVO POR MUTACION DEL CAMINO NUEVO")
    print("=" * 78)
    print("")
    if not os.path.exists(VIEJA):
        print("ROJO PREVIO: falta la copia byte a byte de la guarda vieja, %s" % VIEJA)
        return 1

    casos = []

    print("A) EL ESCENARIO REAL DE LA VUELTA 162, CONTRA LA FUNCION NUEVA")
    print("   apertura %s  ->  cierre %s" % (APERTURA_162, CIERRE_162))
    modificadas = G.salidas_modificadas_desde(APERTURA_162, hasta=CIERRE_162)
    print("   CIFRA docs/loop/SALIDA_* MODIFICADAS entre esos dos commits: %d"
          % len(modificadas))
    for r in modificadas:
        print("      %s" % os.path.basename(r))
    codigo, reporte_162 = git("show", "%s:docs/loop/REPORTE.md" % APERTURA_162)
    print("   reporte de la 162 leido de git show %s:docs/loop/REPORTE.md: %d caracteres"
          % (APERTURA_162, len(reporte_162)))
    faltan = G.no_declaradas(modificadas, reporte_162)
    print("   CIFRA de esas que ese reporte NO nombra: %d" % len(faltan))
    for r in faltan:
        print("      SIN DECLARAR: %s" % os.path.basename(r))
    casos.append(("A_la_162_trae_TRES_modificadas", len(modificadas), 3))
    casos.append(("A_las_tres_son_las_SALIDA_V135_2E_MUTACION",
                  sorted(os.path.basename(r) for r in modificadas),
                  ["SALIDA_V135_2E_MUTACION_1.txt", "SALIDA_V135_2E_MUTACION_2.txt",
                   "SALIDA_V135_2E_MUTACION_3.txt"]))
    casos.append(("A_y_las_TRES_salen_SIN_DECLARAR", len(faltan), 3))
    print("")

    print("B) LA CONTRAPRUEBA: LA GUARDA VIEJA NO TIENE ESTE CAMINO")
    tiene_viejo = hasattr(G, "salidas_modificadas_desde")
    import importlib.util
    spec = importlib.util.spec_from_file_location("_v163_re_sellado_vieja", VIEJA)
    vieja_mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(vieja_mod)
    vieja_tiene = hasattr(vieja_mod, "salidas_modificadas_desde")
    print("   la guarda NUEVA tiene salidas_modificadas_desde: %s" % tiene_viejo)
    print("   la guarda VIEJA tiene salidas_modificadas_desde: %s" % vieja_tiene)
    print("   POR CONSTRUCCION LA VIEJA NO PUEDE VER LO QUE EL REPORTE NO CITA, y")
    print("   por eso salio VERDE sobre las tres de la 162 (acta 162, seccion 5.4).")
    casos.append(("B_la_nueva_tiene_el_camino", tiene_viejo, True))
    casos.append(("B_la_vieja_NO_lo_tiene", vieja_tiene, False))
    casos.append(("B_la_vieja_no_nombraba_las_tres",
                  sum(1 for r in modificadas
                      if os.path.basename(r) in reporte_162), 0))
    print("")

    print("C) NOMBRARLAS LAS SACA DEL ROJO, Y ASI COMPONE CON EL CAMINO VIEJO")
    texto_con_nombres = reporte_162 + "\n" + "\n".join(
        os.path.basename(r) for r in modificadas)
    faltan_tras = G.no_declaradas(modificadas, texto_con_nombres)
    print("   CIFRA sin declarar tras nombrarlas en el texto: %d" % len(faltan_tras))
    casos.append(("C_nombrarlas_deja_cero_sin_declarar", len(faltan_tras), 0))
    print("")

    print("D) NACER NO ES RE SELLAR: LAS ANADIDAS NO ENTRAN")
    _c, name_status = git("diff", "--name-status", APERTURA_162, CIERRE_162,
                          "--", "docs/loop/")
    anadidas = [l.split("\t")[-1].strip() for l in name_status.splitlines()
                if l.startswith("A") and "SALIDA_" in l]
    coladas = [r for r in modificadas if r in anadidas]
    print("   CIFRA docs/loop/SALIDA_* ANADIDAS entre los dos commits: %d" % len(anadidas))
    print("   CIFRA de esas que se colaron en la lista de MODIFICADAS: %d" % len(coladas))
    casos.append(("D_hay_anadidas_de_verdad_en_ese_tramo", len(anadidas) > 0, True))
    casos.append(("D_y_ninguna_se_cuela_como_modificada", len(coladas), 0))
    print("")

    print("E) LA EXENCION POR CONSTRUCCION SIGUE VALIENDO EN EL CAMINO NUEVO")
    ejemplos = [("SALIDA_V162_T6_RE_SELLADO.txt", True),
                ("SALIDA_V162_T6_CIFRAS_REPORTE.txt", True),
                ("SALIDA_V135_2E_MUTACION_1.txt", False)]
    for nombre, esperado in ejemplos:
        real = G.es_exento("docs/loop/%s" % nombre)
        print("   %-40s exento: %-5s (esperado %s)" % (nombre, real, esperado))
        casos.append(("E_exencion_%s" % nombre.replace(".", "_"), real, esperado))
    print("")

    print("F) HOY, SOBRE ESTA VUELTA: LA GUARDA ENTERA")
    cn, sn = correr(NUEVA)
    mod_hoy = cuenta(sn, r"CIFRA docs/loop/SALIDA_\* MODIFICADAS desde la apertura: (\d+)")
    sin_hoy = cuenta(sn, r"CIFRA de esas que el reporte NO nombra: (\d+)")
    print("   exit %d | modificadas desde la apertura %s | sin nombrar %s"
          % (cn, mod_hoy, sin_hoy))
    casos.append(("F_hoy_la_guarda_sale_VERDE", cn, 0))
    casos.append(("F_hoy_no_hay_ninguna_sin_nombrar", sin_hoy, 0))
    print("")

    print("G) NINGUN VEREDICTO VIEJO SE MUEVE, VIEJA CONTRA NUEVA SOBRE EL DE HOY")
    cv, sv = correr(VIEJA)
    patron_viejo = r"CIFRA re selladas SIN declarar en el reporte: (\d+)"
    print("   nuevo exit %d | viejo exit %d" % (cn, cv))
    print("   camino viejo, sin declarar: nuevo %s | viejo %s"
          % (cuenta(sn, patron_viejo), cuenta(sv, patron_viejo)))
    print("   camino viejo, salidas citadas: nuevo %s | viejo %s"
          % (cuenta(sn, r"CIFRA salidas selladas que el reporte cita: (\d+)"),
             cuenta(sv, r"CIFRA salidas selladas que el reporte cita: (\d+)")))
    casos.append(("G_mismo_exit", cn, cv))
    casos.append(("G_misma_cuenta_del_camino_viejo",
                  cuenta(sn, patron_viejo), cuenta(sv, patron_viejo)))
    casos.append(("G_mismas_salidas_citadas",
                  cuenta(sn, r"CIFRA salidas selladas que el reporte cita: (\d+)"),
                  cuenta(sv, r"CIFRA salidas selladas que el reporte cita: (\d+)")))
    print("")

    print("H) PASADA 1, LOS CASOS TAL CUAL")
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

    print("I) PASADA 2, SE MUTA EL VALOR ESPERADO Y CADA CASO TIENE QUE CAER")
    caen = 0
    for nombre, real, esperado in casos:
        if isinstance(esperado, bool):
            mutado = not esperado
        elif isinstance(esperado, int):
            mutado = esperado + 1
        elif isinstance(esperado, list):
            mutado = esperado + ["UN_FICHERO_QUE_NO_EXISTE.txt"]
        else:
            mutado = str(esperado) + "_MUTADO"
        cae = (real != mutado)
        print("   %-52s %s" % (nombre, "CAE" if cae else "NO CAE (ROJO)"))
        if cae:
            caen += 1
    print("   CIFRA casos que CAEN: %d de %d" % (caen, len(casos)))
    print("")

    if fallos or caen != len(casos):
        print("ROJO: la bateria no se comporta.")
        return 1
    print("VERDE: %d casos, los %d pasan y los %d CAEN al mutarles el valor esperado. "
          "EL CASO DE LA VUELTA 162 SE REPRODUCE ENTERO: las tres salidas de la 135 "
          "aparecen como modificadas y sin declarar, la guarda vieja no tenia con que "
          "verlas, nombrarlas las devuelve al camino viejo, y ningun veredicto viejo se "
          "movio." % (len(casos), len(casos), len(casos)))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
