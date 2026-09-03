# -*- coding: utf-8 -*-
r"""vuelta163_tarea4a_mutacion_cobertura.py . TAREA 4.a de la vuelta 163.

CASO POSITIVO POR MUTACION DE LA REGLA NUEVA DE
`scripts/loop/verificar_cifras_del_reporte.py` (adjudicacion 6.6 del acta 162):
**LA COBERTURA DE CIERRE NO PUEDE MENGUAR EN SILENCIO.** Si el reporte trae
afirmaciones de cierre y la guarda coteja CERO, es ROJO.

LA ENFERMEDAD QUE SE REPRODUCE, Y NO SE INVENTA (acta 161, seccion 5.2): la
cobertura de cierre cayo de CINCO a CERO porque las cifras se mudaron de la
prosa a una tabla, y la guarda siguio saliendo VERDE diciendo
`afirmaciones de CIERRE cotejadas: 0`.

COMO SE MUTA, Y SOBRE QUE. El sujeto es CONGELADO Y COMMITEADO
(`docs/loop/SUJETO_FIJO_V162_T3_REPORTE_161.md`, banco 9.10): un sujeto que se
mueve no sirve de vara. La mutacion se hace SOBRE UNA COPIA EN UN TEMPORAL, y
consiste en QUITARLE LA CITA a sus filas de fase, que es exactamente lo que
convierte una fila cotejable en una fila que solo se puede avisar. Nada se
teclea: las filas se localizan por computo (las que citan una salida de
`tallar_estado_de_fase.py`) y la cita se sustituye por una que no existe.

LOS CASOS:
  (A) SUJETO INTACTO, GUARDA NUEVA: VERDE, y coteja las CUATRO filas de fase.
      Es la vara de aceptacion del encargo, corregida a CUATRO por la
      adjudicacion 6.1 del acta 162 (el OCHO era una cifra de memoria del
      auditor, y su propia acta lo declara).
  (B) SUJETO DE LA 160 INTACTO, GUARDA NUEVA: VERDE y CINCO, la otra mitad de
      la vara, que mide la prosa en vez de la tabla.
  (C) SUJETO CON LAS CITAS ARRANCADAS, GUARDA NUEVA: **ROJO**, y el fallo dice
      COBERTURA DE CIERRE CERO. Aqui vive el remedio.
  (D) EL MISMO SUJETO MUTADO, GUARDA VIEJA: **VERDE**. Sin esta contraprueba el
      caso (C) no probaria un remedio, solo que hoy funciona. La guarda vieja se
      saca de una COPIA BYTE A BYTE tomada ANTES de tocar nada
      (`scripts/loop/_v163_cifras_vieja_copia.py`), no de `HEAD`, que es la
      trampa que caduco a `vuelta160_tarea6b_mutacion_puerta.py`.
  (E) UN REPORTE SIN NINGUNA AFIRMACION DE CIERRE: la regla NO dispara. Un
      reporte que no habla de cierre no tiene cobertura de cierre que perder, y
      exigirle una seria inventar trabajo.
  (F) NINGUN VEREDICTO VIEJO SE MUEVE: vieja contra nueva sobre los DOS sujetos
      congelados, cotejando codigo de salida y numero de cotejadas.

P.16, QUIEN FABRICA LIMPIA: el temporal se retira siempre.

USO:  python scripts/loop/vuelta163_tarea4a_mutacion_cobertura.py
"""
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "scripts", "loop")
NUEVA = os.path.join(LOOP, "verificar_cifras_del_reporte.py")
VIEJA = os.path.join(LOOP, "_v163_cifras_vieja_copia.py")
SUJETO_161 = os.path.join(RAIZ, "docs", "loop", "SUJETO_FIJO_V162_T3_REPORTE_161.md")
SUJETO_160 = os.path.join(RAIZ, "docs", "loop", "SUJETO_FIJO_V162_T3_REPORTE_160.md")

PATRON_CITA = re.compile(r"`docs/loop/(SALIDA_[A-Za-z0-9_]+\.txt)`")


def correr(guarda, reporte):
    r = subprocess.run([sys.executable, guarda, "--reporte", reporte],
                       capture_output=True, text=True, cwd=RAIZ,
                       encoding="utf-8", errors="replace")
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def filas_cotejadas(salida):
    m = re.search(r"filas de TABLA de cierre cotejadas: (\d+)", salida)
    return int(m.group(1)) if m else None


def cierres_cotejados(salida):
    m = re.search(r"afirmaciones de CIERRE cotejadas contra tallar_estado_de_fase\.py: (\d+)",
                  salida)
    return int(m.group(1)) if m else None


def presentes(salida):
    m = re.search(r"afirmaciones de cierre PRESENTES: (\d+)", salida)
    return int(m.group(1)) if m else None


def arrancar_las_citas(texto):
    """Le quita la cita a TODA fila de tabla que cite una salida existente. Las
    filas se localizan POR COMPUTO, no por su numero de linea: un numero de
    linea tecleado es lo que caduca un arnes."""
    salida, arrancadas = [], 0
    for linea in texto.split("\n"):
        if linea.strip().startswith("|") and PATRON_CITA.search(linea):
            nueva = PATRON_CITA.sub("`docs/loop/UNA_SALIDA_QUE_NO_EXISTE.txt`", linea)
            if nueva != linea:
                arrancadas += 1
            salida.append(nueva)
        else:
            salida.append(linea)
    return "\n".join(salida), arrancadas


def main():
    print("=" * 78)
    print("VUELTA 163, TAREA 4.a: CASO POSITIVO POR MUTACION DE LA COBERTURA DE CIERRE")
    print("=" * 78)
    print("")
    if not os.path.exists(VIEJA):
        print("ROJO PREVIO: falta la copia byte a byte de la guarda vieja, %s" % VIEJA)
        return 1

    tmp = tempfile.mkdtemp(prefix="v163_4a_")
    casos = []
    try:
        print("A) LOS DOS SUJETOS CONGELADOS, CON LA GUARDA NUEVA")
        c161, s161 = correr(NUEVA, SUJETO_161)
        c160, s160 = correr(NUEVA, SUJETO_160)
        print("   sujeto 161: exit %d | filas de tabla cotejadas %s | prosa cotejada %s "
              "| presentes %s" % (c161, filas_cotejadas(s161), cierres_cotejados(s161),
                                  presentes(s161)))
        print("   sujeto 160: exit %d | filas de tabla cotejadas %s | prosa cotejada %s "
              "| presentes %s" % (c160, filas_cotejadas(s160), cierres_cotejados(s160),
                                  presentes(s160)))
        casos.append(("A_161_sigue_VERDE", c161, 0))
        casos.append(("A_161_coteja_CUATRO_filas_de_fase", filas_cotejadas(s161), 4))
        casos.append(("B_160_sigue_VERDE", c160, 0))
        casos.append(("B_160_sigue_dando_CINCO", cierres_cotejados(s160), 5))
        print("")

        print("B) LA MUTACION: al sujeto 161 se le ARRANCAN LAS CITAS de sus filas")
        texto = io.open(SUJETO_161, encoding="utf-8").read()
        mutado, arrancadas = arrancar_las_citas(texto)
        ruta_mutado = os.path.join(tmp, "SUJETO_161_SIN_CITAS.md")
        io.open(ruta_mutado, "w", encoding="utf-8", newline="\n").write(mutado)
        print("   CIFRA filas a las que se les arranco la cita: %d" % arrancadas)
        print("   el sujeto del repo NO se toca: la mutacion vive en %s"
              % os.path.basename(ruta_mutado))
        casos.append(("la_mutacion_arranca_al_menos_una_cita", arrancadas > 0, True))
        print("")

        print("C) EL SUJETO MUTADO CONTRA LA GUARDA NUEVA: TIENE QUE SER ROJO")
        cm, sm = correr(NUEVA, ruta_mutado)
        dice_cero = "COBERTURA DE CIERRE CERO" in sm
        print("   exit %d | presentes %s | filas cotejadas %s | prosa cotejada %s"
              % (cm, presentes(sm), filas_cotejadas(sm), cierres_cotejados(sm)))
        print("   dice COBERTURA DE CIERRE CERO: %s" % dice_cero)
        for l in sm.split("\n"):
            if "COBERTURA DE CIERRE CERO" in l:
                print("      %s" % l.strip()[:190])
        casos.append(("C_el_sujeto_sin_citas_es_ROJO", cm, 1))
        casos.append(("C_y_lo_dice_con_su_nombre", dice_cero, True))
        casos.append(("C_las_afirmaciones_de_cierre_SIGUEN_PRESENTES", presentes(sm), 4))
        casos.append(("C_y_las_cotejadas_son_CERO",
                      (filas_cotejadas(sm) or 0) + (cierres_cotejados(sm) or 0), 0))
        print("")

        print("D) EL MISMO SUJETO MUTADO CONTRA LA GUARDA VIEJA: TIENE QUE SER VERDE")
        cv, sv = correr(VIEJA, ruta_mutado)
        print("   exit %d | filas cotejadas %s | prosa cotejada %s"
              % (cv, filas_cotejadas(sv), cierres_cotejados(sv)))
        print("   LA VIEJA NO VE LA CEGUERA, Y ESO ES LO QUE CONVIERTE AL CASO C EN")
        print("   PRUEBA DE UN REMEDIO Y NO EN UN VERDE QUE NO DICE NADA.")
        casos.append(("D_la_guarda_VIEJA_sobre_lo_mismo_sale_VERDE", cv, 0))
        print("")

        print("E) UN REPORTE SIN NINGUNA AFIRMACION DE CIERRE: LA REGLA NO DISPARA")
        ruta_mudo = os.path.join(tmp, "REPORTE_SIN_CIERRE.md")
        io.open(ruta_mudo, "w", encoding="utf-8", newline="\n").write(
            "# UN REPORTE QUE NO HABLA DE CIERRE\n\n"
            "No dice nada de ninguna fase ni de nada cumplido. Solo esto.\n")
        cmu, smu = correr(NUEVA, ruta_mudo)
        print("   exit %d | presentes %s" % (cmu, presentes(smu)))
        print("   dice COBERTURA DE CIERRE CERO: %s" % ("COBERTURA DE CIERRE CERO" in smu))
        casos.append(("E_sin_afirmaciones_de_cierre_no_hay_presentes", presentes(smu), 0))
        casos.append(("E_y_la_regla_nueva_NO_dispara",
                      "COBERTURA DE CIERRE CERO" in smu, False))
        print("")

        print("F) NINGUN VEREDICTO VIEJO SE MUEVE, COTEJADO VIEJA CONTRA NUEVA")
        for nombre, ruta in (("sujeto 161", SUJETO_161), ("sujeto 160", SUJETO_160)):
            cn, sn = correr(NUEVA, ruta)
            cvv, svv = correr(VIEJA, ruta)
            print("   %-11s nuevo exit %d | viejo exit %d | filas %s vs %s | prosa %s vs %s"
                  % (nombre, cn, cvv, filas_cotejadas(sn), filas_cotejadas(svv),
                     cierres_cotejados(sn), cierres_cotejados(svv)))
            casos.append(("F_%s_mismo_exit" % nombre.replace(" ", "_"), cn, cvv))
            casos.append(("F_%s_mismas_filas" % nombre.replace(" ", "_"),
                          filas_cotejadas(sn), filas_cotejadas(svv)))
            casos.append(("F_%s_misma_prosa" % nombre.replace(" ", "_"),
                          cierres_cotejados(sn), cierres_cotejados(svv)))
        print("")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
        print("   P.16: el temporal se retira. Existe todavia: %s" % os.path.exists(tmp))
        print("")

    print("G) PASADA 1, LOS CASOS TAL CUAL")
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

    print("H) PASADA 2, SE MUTA EL VALOR ESPERADO Y CADA CASO TIENE QUE CAER")
    caen = 0
    for nombre, real, esperado in casos:
        mutado = (not esperado) if isinstance(esperado, bool) else (
            (esperado + 1) if isinstance(esperado, int) else str(esperado) + "_MUTADO")
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
          "LA COBERTURA DE CIERRE YA NO PUEDE CAER A CERO EN SILENCIO, la guarda vieja "
          "sobre la misma mutacion sigue saliendo verde, y ningun veredicto viejo se "
          "movio sobre los dos sujetos congelados." % (len(casos), len(casos), len(casos)))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
