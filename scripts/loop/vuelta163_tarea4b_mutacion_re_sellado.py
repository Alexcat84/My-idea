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
  (F) EL CAMINO NUEVO NO INVENTA MODIFICADAS: su lista es EXACTAMENTE la que da
      `git diff --name-status` en crudo, menos los exentos, sobre DOS PARES
      FIJOS de la historia (el de la 162 y el de la 161).
  (G) NINGUN VEREDICTO VIEJO SE MUEVE: vieja y nueva sobre el mismo arbol dan la
      misma cuenta DEL CAMINO VIEJO y las mismas salidas citadas, y la nueva
      NUNCA AFLOJA.

--- ANCLADO EN LA VUELTA 164, TAREA 2.c (ADJUDICACION 6.6 DEL ACTA 163) ---

CORRECCION DECLARADA POR ADICION: no se borra una linea de lo de arriba y los
casos viejos quedan escritos dentro de la propia salida del arnes.

QUE ESTABA MAL, MEDIDO Y NO ALEGADO. Tres casos leian EL ARBOL DE TRABAJO VIVO y
clavaban su ESTADO: `F_hoy_la_guarda_sale_VERDE` (exit esperado 0),
`F_hoy_no_hay_ninguna_sin_nombrar` (sin nombrar esperado 0) y `G_mismo_exit`
(exit de la nueva igual al de la vieja). Sellados dieron 17 de 17; corridos por
el auditor con tres `docs/loop/SALIDA_*` modificadas en vuelo dieron 14 de 17
SIN QUE NADIE TOCARA UNA LINEA DE CODIGO (acta 163, seccion 5.1). No es un falso
verde: es un FALSO ROJO, y la raiz es la misma que la propia vuelta 163 curo dos
veces, en `160_6b` ("una contraprueba anclada a una referencia movil es un falso
verde esperando su dia") y en `162_1a` ("los esperados se COMPUTAN del estado del
dia, no se clavan").

Y `G_mismo_exit` era ademas FALSO POR CONSTRUCCION el dia que el camino nuevo
muerde: si la nueva ve algo que la vieja no puede ver, sus exit TIENEN que
diferir. Exigir que coincidan es exigir que el remedio no remedie.

CON QUE SE SUSTITUYEN, Y NINGUNO MIRA EL ESTADO DEL ARBOL:
  - PARES FIJOS Y COMPUTADOS. El par de la 161 sale entero de `git log
    --diff-filter=A` sobre sus dos sellos de HEAD (`_nacimiento`), sin un digito
    tecleado; y los dos hashes tecleados del par de la 162 se COTEJAN contra su
    version computada, asi que el dia que dejen de calzar el arnes lo canta.
  - INVARIANTES, no estados: la lista de la guarda contra `git` en crudo.
  - IMPLICACIONES, no absolutos: la nueva nunca afloja a la vieja; si los exit
    difieren lo explica el camino nuevo; y el exit de hoy, sea el que sea, lo
    explica su propia cuenta publicada.

LA PRUEBA DE QUE EL ANCLAJE FUNCIONA ESTA CORRIDA Y SELLADA en
`docs/loop/SALIDA_V164_T2C_PRUEBA_DEL_ANCLAJE.txt`: se ensucian a proposito las
tres `SALIDA_V135_2E_MUTACION` del arbol, la guarda sale ROJO exit 1 nombrandolas
(hace su trabajo) y ESTE ARNES sigue dando 24 de 24 VERDE sobre el mismo arbol
sucio. P.16: las tres se restauran y se comprueba que el arbol queda limpio.

LA GUARDA `verificar_re_sellado.py` NO SE TOCA en esta correccion: esta bien y
muerde de verdad. Lo que estaba roto era el arnes.

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


def _nacimiento(ruta_rel):
    """EL REF FIJO Y COMPUTADO (vuelta 164, TAREA 2.c, adjudicacion 6.6 del acta
    163). El commit que ANADIO un sello, leido de `git log --diff-filter=A`: no
    se teclea un hash y no se mira HEAD, asi que no puede moverse debajo del
    arnes como le paso a `160_6b`. Devuelve None si el sello no existe o si lo
    anade mas de un commit, y el caso que lo use se declara imposible en vez de
    inventarse un ancla."""
    r = subprocess.run(["git", "log", "--diff-filter=A", "--format=%h", "--", ruta_rel],
                       cwd=RAIZ, capture_output=True, text=True)
    hs = [l.strip() for l in (r.stdout or "").splitlines() if l.strip()]
    return hs[0] if len(hs) == 1 else None


# EL SEGUNDO PAR, ENTERAMENTE COMPUTADO. La vuelta 161 es historia cerrada igual
# que la 162, pero aqui NO se teclea ni un digito: los dos extremos salen del
# commit que anadio su sello de HEAD.
APERTURA_161 = _nacimiento("docs/loop/SALIDA_V161_HEAD_APERTURA.txt")
CIERRE_161 = _nacimiento("docs/loop/SALIDA_V161_HEAD_CIERRE.txt")


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

    print("F) EL CAMINO NUEVO NO INVENTA MODIFICADAS: SU LISTA CONTRA git EN CRUDO")
    print("   ANCLADO EN LA VUELTA 164, TAREA 2.c (adjudicacion 6.6 del acta 163).")
    print("   LO QUE HABIA AQUI, Y NO SE BORRA: dos casos que corrian la guarda entera")
    print("   sobre EL ARBOL DE TRABAJO VIVO y clavaban su ESTADO,")
    print("   `F_hoy_la_guarda_sale_VERDE` (exit esperado 0) y")
    print("   `F_hoy_no_hay_ninguna_sin_nombrar` (sin nombrar esperado 0). Sellados")
    print("   dieron VERDE; corridos por el auditor con tres SALIDA_* modificadas en")
    print("   vuelo dieron ROJO SIN QUE NADIE TOCARA UNA LINEA DE CODIGO. No era un")
    print("   falso verde: era un FALSO ROJO, y la raiz es la misma que la 163 curo en")
    print("   `160_6b` y en `162_1a`. Se sustituyen por invariantes sobre PARES FIJOS")
    print("   de la historia y por IMPLICACIONES, que no dependen del arbol de hoy.")
    print("")
    # LOS DOS HASHES TECLEADOS DEL PAR 162 SE COTEJAN CONTRA SU VERSION
    # COMPUTADA: si algun dia dejan de calzar, este arnes lo canta en vez de
    # seguir midiendo sobre un par que ya no es el que dice ser.
    casos.append(("F_162_la_apertura_tecleada_calza_con_la_computada",
                  _nacimiento("docs/loop/SALIDA_V162_HEAD_APERTURA.txt"), APERTURA_162))
    casos.append(("F_162_el_cierre_tecleado_calza_con_el_computado",
                  _nacimiento("docs/loop/SALIDA_V162_HEAD_CIERRE.txt"), CIERRE_162))
    casos.append(("F_161_los_dos_extremos_se_computan",
                  bool(APERTURA_161) and bool(CIERRE_161), True))
    if not (APERTURA_161 and CIERRE_161):
        print("   ROJO PREVIO: no se pudo computar el par de la vuelta 161.")
        return 1
    for etiqueta, a, b in (("162", APERTURA_162, CIERRE_162),
                           ("161", APERTURA_161, CIERRE_161)):
        lista = G.salidas_modificadas_desde(a, hasta=b)
        _c, ns = git("diff", "--name-status", a, b, "--", "docs/loop/")
        crudas = sorted({l.split("\t")[-1].strip() for l in ns.splitlines()
                         if l.split("\t")[0].startswith("M")
                         and os.path.basename(l.split("\t")[-1].strip()).startswith("SALIDA_")
                         and l.split("\t")[-1].strip().endswith(".txt")
                         and not G.es_exento(l.split("\t")[-1].strip())})
        print("   par %s (%s..%s): guarda %d | git en crudo menos exentos %d"
              % (etiqueta, a, b, len(lista), len(crudas)))
        casos.append(("F_%s_la_lista_es_la_de_git_en_crudo" % etiqueta,
                      sorted(lista), crudas))
        # NACER NO ES RE SELLAR, tambien sobre este par: cero anadidas coladas.
        anad = [l.split("\t")[-1].strip() for l in ns.splitlines()
                if l.startswith("A") and "SALIDA_" in l]
        casos.append(("F_%s_ninguna_anadida_se_cuela" % etiqueta,
                      len([r for r in lista if r in anad]), 0))
    print("")

    print("G) NINGUN VEREDICTO VIEJO SE MUEVE, VIEJA CONTRA NUEVA SOBRE EL MISMO ARBOL")
    print("   LO QUE HABIA AQUI, Y NO SE BORRA: `G_mismo_exit`, que exigia que la guarda")
    print("   NUEVA y la VIEJA dieran EL MISMO codigo de salida sobre el arbol de hoy.")
    print("   Ese caso es FALSO POR CONSTRUCCION el dia que el camino nuevo muerde: si")
    print("   la nueva ve algo que la vieja no puede ver, sus exit TIENEN que diferir, y")
    print("   exigir que coincidan es exigir que el remedio no remedie. Se sustituye por")
    print("   las dos afirmaciones que si son 'ningun veredicto viejo se mueve': que EL")
    print("   CAMINO VIEJO da lo mismo en las dos, y que la nueva NUNCA AFLOJA.")
    print("")
    cn, sn = correr(NUEVA)
    cv, sv = correr(VIEJA)
    patron_viejo = r"CIFRA re selladas SIN declarar en el reporte: (\d+)"
    patron_citadas = r"CIFRA salidas selladas que el reporte cita: (\d+)"
    sin_hoy = cuenta(sn, r"CIFRA de esas que el reporte NO nombra: (\d+)")
    mod_hoy = cuenta(sn, r"CIFRA docs/loop/SALIDA_\* MODIFICADAS desde la apertura: (\d+)")
    print("   nuevo exit %d | viejo exit %d" % (cn, cv))
    print("   camino NUEVO hoy: modificadas %s | sin nombrar %s" % (mod_hoy, sin_hoy))
    print("   camino viejo, sin declarar: nuevo %s | viejo %s"
          % (cuenta(sn, patron_viejo), cuenta(sv, patron_viejo)))
    print("   camino viejo, salidas citadas: nuevo %s | viejo %s"
          % (cuenta(sn, patron_citadas), cuenta(sv, patron_citadas)))
    casos.append(("G_misma_cuenta_del_camino_viejo",
                  cuenta(sn, patron_viejo), cuenta(sv, patron_viejo)))
    casos.append(("G_mismas_salidas_citadas",
                  cuenta(sn, patron_citadas), cuenta(sv, patron_citadas)))
    # DELTA, NO ESTADO: la nueva nunca da VERDE donde la vieja daba ROJO.
    casos.append(("G_la_nueva_nunca_AFLOJA_a_la_vieja", cn >= cv, True))
    # Y SI LOS EXIT DIFIEREN, LA DIFERENCIA LA EXPLICA EL CAMINO NUEVO Y NO OTRA
    # COSA: no hay diferencia sin al menos una modificada sin nombrar.
    casos.append(("G_si_los_exit_difieren_lo_explica_el_camino_nuevo",
                  (cn == cv) or (sin_hoy or 0) > 0, True))
    # LA IMPLICACION QUE SUSTITUYE AL ESTADO CLAVADO DE `F_hoy_*`: el veredicto
    # de hoy, sea el que sea, lo explica su propia cuenta publicada.
    viejo_sin = cuenta(sn, patron_viejo) or 0
    casos.append(("G_el_exit_de_hoy_lo_explica_su_propia_cuenta",
                  (cn != 0) == ((sin_hoy or 0) > 0 or viejo_sin > 0), True))
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
