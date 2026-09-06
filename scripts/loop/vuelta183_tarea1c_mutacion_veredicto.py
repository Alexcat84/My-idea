# -*- coding: utf-8 -*-
r"""vuelta183_tarea1c_mutacion_veredicto.py . EL ARNES DE LA ESCALADA: LOS
NUMERALES DEL VEREDICTO CONTRA LO QUE EL CUERPO PERMITE CONTAR, Y EL HUECO QUE
DICE CUAL DE LOS DOS CASOS ES.

CUBRE LAS DOS OPERACIONES DE CODIGO DE LA VUELTA 183:

  TAREA 1.c, la ESCALADA de `AUDITOR.md` 1.2, que la racha de reporte en DOS
  dispara sin esperar decision nueva del fundador:
  `numerales_del_veredicto_que_no_calzan()`, con sus dos contadores
  (`caidas_propias_del_cuerpo()` y `tareas_de_la_tabla()`) y su lector de
  numerales en cifra y en letra.

  TAREA 1.d, la adjudicacion `7.1` del acta 182: `frase_del_caso_del_hueco()`,
  que separa "el fichero no existe" de "el fichero mide cero" en vez de
  fundirlos en el `max(tam, 0)` que los confundia.

EL CASO POSITIVO ES REAL Y NO FABRICADO, QUE ES LA CONDICION DEL ENCARGO. El
veredicto de una linea de la 182 se lee de `docs/loop/reportes/REPORTE_V182.md`,
su cuerpo tambien, y la guarda TIENE QUE CAER sobre ellos; el mismo veredicto con
la palabra "SIETE" en vez de "SEIS" TIENE QUE PASAR. Ni el veredicto ni el numero
de caidas se teclean aqui: los dos salen del fichero.

Y LA MUTACION SE CORRE DE VERDAD (`EJECUTOR.md` 1, EL CASO ROJO SE PRUEBA POR
MUTACION): cada caso se evalua sobre una VARIABLE COMPUTADA por la funcion de
verdad, y despues se cambia el valor esperado para comprobar que el caso CAE. Un
`assert` que compara una constante literal consigo misma no puede fallar nunca y
no prueba nada.

SUJETO CONGELADO, Y AQUI NO ES UNA FRASE SINO UNA HUELLA. El unico fichero del
repo que este arnes lee es `docs/loop/reportes/REPORTE_V182.md`, que es un
reporte ARCHIVADO: `scripts/loop/archivar_reporte.py` lo escribio byte a byte y
no vuelve a tocarlo nadie. Para no tener que creerselo, el bloque A imprime su
`sha256` cada vez que corre, asi que el dia que ese fichero se mueva la salida lo
dira sola. Todo lo demas lo fabrica en memoria. El instrumento que se prueba,
`scripts/loop/cerrar_reporte.py`, SI se mueve, y eso no es un defecto: es el
sujeto bajo prueba de un arnes de mutacion, no su ancla.

USO:
  python scripts/loop/vuelta183_tarea1c_mutacion_veredicto.py
"""
import hashlib
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cerrar_reporte as CR   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
R182 = os.path.join(LOOP, "reportes", "REPORTE_V182.md")
NL = chr(10)

SALIDA = []


def w(s=""):
    SALIDA.append(s)


def caso(nombre, computado, esperado, esperado_mutado):
    """UN CASO CON SU MUTACION. `computado` sale de correr la funcion de verdad;
    `esperado` es lo que la casa afirma. Se comprueba que PASA con el esperado
    bueno y que CAE con el mutado, que es lo unico que prueba que el caso podia
    fallar."""
    pasa = computado == esperado
    cae = computado != esperado_mutado
    w("   %-52s %-5s %s"
      % (nombre, "PASA" if pasa else "FALLA", "CAE" if cae else "NO CAE"))
    if not pasa:
        w("      computado: %r" % (computado,))
        w("      esperado : %r" % (esperado,))
    return (0 if pasa else 1) + (0 if cae else 1)


def cuerpo_de_reporte_falso(n_caidas, n_tareas, con_seccion8=True, con_tabla=True):
    """UN REPORTE DE MENTIRA con las cifras que se le pidan. NO toca el repo."""
    p = ["# REPORTE DE LA VUELTA 999 (fabricado)", ""]
    if con_tabla:
        p += [CR.MARCA_TABLA_ABRE,
              "| tarea | que encarga | estado | donde vive la prueba |",
              "|---|---|---|---|"]
        for k in range(1, n_tareas + 1):
            p.append("| **TAREA %d** | algo | **CERRADA** | un fichero |" % k)
        p += [CR.MARCA_TABLA_CIERRA, ""]
    p += ["## 7. PENDIENTES DE DOCTRINA", "", "Nada.", ""]
    if con_seccion8:
        p += ["## 8. MIS CAIDAS PROPIAS", ""]
        for k in range(1, n_caidas + 1):
            p += ["**`C.%d`. UNA CAIDA DE MENTIRA.** Su cuerpo." % k, ""]
    p += ["## 9. LA BATERIA", "", "Nada.", ""]
    return NL.join(p) + NL


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    fallos = 0

    w("=" * 78)
    w("ARNES DE LA VUELTA 183, TAREAS 1.c Y 1.d")
    w("=" * 78)
    w("")

    # ------------------------------------------------------------ EL CASO REAL
    w("A) EL CASO REAL, LEIDO DEL REPORTE ARCHIVADO DE LA 182 Y NO TECLEADO")
    if not os.path.exists(R182):
        w("   ROJO: no existe %s. SIN EL NO HAY CASO REAL, y eso se dice en vez"
          % os.path.relpath(R182, RAIZ).replace(os.sep, "/"))
        w("   de fabricar uno que se aprueba solo.")
        fallos += 1
        real = None
    else:
        t182 = io.open(R182, encoding="utf-8").read().replace(chr(13) + NL, NL)
        l182 = t182.split(NL)
        w("   docs/loop/reportes/REPORTE_V182.md -> %d lineas | %d bytes en disco "
          "y %d bytes normalizados a LF"
          % (len(l182), os.path.getsize(R182), len(t182.encode("utf-8"))))
        # EL ANCLA, MEDIDA CADA VEZ QUE ESTO CORRE. Un reporte archivado no se
        # mueve; el dia que se mueva, esta linea lo dira sin que nadie pregunte.
        w("   sha256 del ancla, en disco y normalizado a LF: %s y %s"
          % (hashlib.sha256(io.open(R182, "rb").read()).hexdigest()[:16],
             hashlib.sha256(t182.encode("utf-8")).hexdigest()[:16]))
        lineas_ver = [(i, l) for i, l in enumerate(l182, 1)
                      if "EL VEREDICTO DE UNA LINEA" in l]
        w("   CIFRA lineas que se llaman a si mismas veredicto: %d" % len(lineas_ver))
        if len(lineas_ver) != 1:
            w("   ROJO: se necesita exactamente 1 y hay %d." % len(lineas_ver))
            fallos += 1
            real = None
        else:
            n_ver, linea_ver = lineas_ver[0]
            w("   EL VEREDICTO, EN LA LINEA %d, LEIDO DEL FICHERO:" % n_ver)
            for k in range(0, len(linea_ver), 100):
                w("      | " + linea_ver[k:k + 100])
            # EL VEREDICTO SE PASA COMO EL CIERRE LO RECIBE: sin el envoltorio
            # `**EL VEREDICTO DE UNA LINEA: ... **` que el propio instrumento
            # anade al escribirlo.
            crudo = linea_ver.split("EL VEREDICTO DE UNA LINEA:", 1)[1]
            real = crudo.rstrip("*").strip()
            w("   el veredicto DESENVUELTO, que es como cerrar_reporte.py lo")
            w("   recibe por --veredicto: %d caracteres" % len(real))
    w("")

    if real is not None:
        w("B) LOS CONTADORES SOBRE EL CUERPO REAL, CORRIDOS Y NO RECORDADOS")
        caidas = CR.caidas_propias_del_cuerpo(t182)
        tareas = CR.tareas_de_la_tabla(t182)
        w("   caidas_propias_del_cuerpo() -> %s" % sorted(caidas or []))
        w("   CIFRA caidas propias contadas de la seccion 8: %s"
          % (len(caidas) if caidas is not None else "(sin seccion 8)"))
        w("   tareas_de_la_tabla() -> %s" % tareas)
        w("   LAS CABECERAS `C.n`, CON SU LINEA EN EL FICHERO:")
        for i, l in enumerate(l182, 1):
            if CR.PATRON_CAIDA_PROPIA.match(l):
                w("      linea %-5d %s" % (i, l.strip()[:96]))
        w("")

        w("C) LA GUARDA SOBRE EL CASO REAL: TIENE QUE CAER")
        motivos, cuentas, hallados = CR.numerales_del_veredicto_que_no_calzan(
            real, t182)
        w("   numerales hallados en el veredicto real: %d" % len(hallados))
        for c, v, e in hallados:
            w("      %-10r -> %d %s" % (c, v, e))
        w("   cuentas del cuerpo: %r" % (cuentas,))
        w("   CIFRA motivos: %d" % len(motivos))
        for m in motivos:
            w("      " + m)
        # LA VARIABLE ES COMPUTADA: sale de correr la guarda de verdad sobre el
        # fichero de verdad. Nada de constantes literales aqui.
        fallos += caso("el veredicto real de la 182 CAE", len(motivos) > 0,
                       True, False)
        w("")

        w("D) EL MISMO VEREDICTO CON EL NUMERAL BUENO: TIENE QUE PASAR")
        # LA CORRECCION SE HACE SOBRE EL TEXTO REAL, no se reescribe a mano: se
        # sustituye la palabra del numeral por la que el cuerpo permite contar,
        # y la palabra buena se computa de la cuenta, no se teclea.
        inversa = {v: k for k, v in sorted(CR.PALABRA_A_NUMERO.items())}
        palabra_buena = inversa[len(caidas)]
        w("   la cuenta del cuerpo es %d, o sea %r" % (len(caidas), palabra_buena))
        arreglado = re.sub(r"(?i)\bseis\b", palabra_buena.upper(), real)
        w("   el veredicto arreglado, %d caracteres, difiere del real: %s"
          % (len(arreglado), "SI" if arreglado != real else "NO"))
        motivos2, _c2, _h2 = CR.numerales_del_veredicto_que_no_calzan(
            arreglado, t182)
        w("   CIFRA motivos con el numeral bueno: %d" % len(motivos2))
        for m in motivos2:
            w("      " + m)
        fallos += caso("el veredicto con el numeral bueno PASA", len(motivos2),
                       0, 1)
        w("")

    # ------------------------------------------------ LOS CASOS FABRICADOS
    w("E) LOS CASOS FABRICADOS, PARA TUMBAR LA GUARDA UNO A UNO")
    cuerpo = cuerpo_de_reporte_falso(7, 5)
    for texto_ver, esperado_motivos, nombre in (
            ("LAS CINCO TAREAS CERRARON Y LAS SIETE CAIDAS VAN CON SU NOMBRE", 0,
             "cinco tareas y siete caidas sobre 5 y 7"),
            ("LAS CINCO TAREAS CERRARON Y LAS SEIS CAIDAS VAN CON SU NOMBRE", 1,
             "cinco tareas y SEIS caidas sobre 5 y 7"),
            ("LAS DOS TAREAS CERRARON Y LAS SIETE CAIDAS VAN CON SU NOMBRE", 1,
             "DOS tareas y siete caidas sobre 5 y 7"),
            ("LAS 5 TAREAS CERRARON Y LAS 7 CAIDAS VAN CON SU NOMBRE", 0,
             "los mismos numerales en CIFRA y no en letra"),
            ("LAS 5 TAREAS CERRARON Y LAS 6 CAIDAS VAN CON SU NOMBRE", 1,
             "en cifra, y la de caidas mal"),
            ("EL 2.464 ENTRA A LA COLA Y NO HAY MAS QUE DECIR", 0,
             "un numero que NO va seguido de caidas ni tareas no se cuenta"),
            ("UNA TAREA CERRADA Y SIETE CAIDAS", 1,
             "el singular tambien se lee: UNA TAREA sobre 5"),
            ("CERO CAIDAS Y CINCO TAREAS", 1,
             "CERO tambien se lee, y sobre 7 no calza")):
        motivos, cuentas, hallados = CR.numerales_del_veredicto_que_no_calzan(
            texto_ver, cuerpo)
        fallos += caso(nombre, len(motivos), esperado_motivos,
                       esperado_motivos + 1)
    w("")

    w("F) EL CUERPO QUE NO PERMITE CONTAR: UNA CIFRA SIN FICHERO NO CIERRA")
    sin8 = cuerpo_de_reporte_falso(7, 5, con_seccion8=False)
    m_sin8, c_sin8, _h = CR.numerales_del_veredicto_que_no_calzan(
        "LAS CINCO TAREAS CERRARON Y LAS SIETE CAIDAS VAN CON SU NOMBRE", sin8)
    w("   cuentas sobre un cuerpo SIN seccion 8: %r" % (c_sin8,))
    fallos += caso("sin seccion 8, el numeral de caidas CAE", len(m_sin8), 1, 0)
    sintabla = cuerpo_de_reporte_falso(7, 5, con_tabla=False)
    m_st, c_st, _h = CR.numerales_del_veredicto_que_no_calzan(
        "LAS CINCO TAREAS CERRARON Y LAS SIETE CAIDAS VAN CON SU NOMBRE", sintabla)
    w("   cuentas sobre un cuerpo SIN tabla de tareas: %r" % (c_st,))
    fallos += caso("sin tabla, el numeral de tareas CAE", len(m_st), 1, 0)
    w("   y un veredicto SIN numerales sobre ese mismo cuerpo no inventa rojos:")
    m_mudo, _c, _h = CR.numerales_del_veredicto_que_no_calzan(
        "LA VUELTA CERRO Y NO HAY MAS", sintabla)
    fallos += caso("un veredicto sin numerales no cae", len(m_mudo), 0, 1)
    w("")

    w("G) LOS CONTADORES, TUMBADOS UNO A UNO SOBRE CUERPOS FABRICADOS")
    for n_c, n_t in ((7, 5), (1, 1), (0, 2), (12, 9)):
        cu = cuerpo_de_reporte_falso(n_c, n_t)
        fallos += caso("cuerpo con %d caidas -> el contador dice" % n_c,
                       len(CR.caidas_propias_del_cuerpo(cu)), n_c, n_c + 1)
        fallos += caso("cuerpo con %d tareas -> el contador dice" % n_t,
                       CR.tareas_de_la_tabla(cu), n_t, n_t + 1)
    w("   Y LA CABECERA Y EL SEPARADOR DE LA TABLA NO CUENTAN COMO FILAS: el")
    w("   cuerpo de 2 tareas tiene 4 lineas que empiezan por barra y el contador")
    w("   dice 2.")
    cu2 = cuerpo_de_reporte_falso(0, 2)
    barras = len([l for l in cu2.split(NL) if l.strip().startswith("|")])
    fallos += caso("lineas que empiezan por barra", barras, 4, 2)
    fallos += caso("filas de tarea contadas", CR.tareas_de_la_tabla(cu2), 2, 4)
    w("   Y UNA `C.n` CITADA FUERA DE LA SECCION 8 NO SE CUENTA: se le mete una")
    w("   cita en la seccion 7 y el contador no se mueve.")
    con_cita = cu2.replace("Nada." + NL + NL + "## 8",
                           "**`C.9`. UNA CAIDA AJENA CITADA.**" + NL + NL + "## 8")
    fallos += caso("con una `C.n` ajena en la seccion 7",
                   len(CR.caidas_propias_del_cuerpo(con_cita)), 0, 1)
    w("")

    w("H) TAREA 1.d: LA FRASE DEL HUECO DICE CUAL DE LOS DOS CASOS ES")
    no_existe = CR.frase_del_caso_del_hueco(False, -1, 0)
    cero = CR.frase_del_caso_del_hueco(True, 0, 0)
    con_cuerpo = CR.frase_del_caso_del_hueco(True, 1234, 1230)
    for nombre, frase in (("NO EXISTE", no_existe), ("CERO BYTES", cero),
                          ("CON CUERPO", con_cuerpo)):
        w("   --- %s ---" % nombre)
        for l in frase.split(NL):
            w("      | " + l)
    fallos += caso("la del fichero ausente dice EL FICHERO NO EXISTE",
                   "EL FICHERO NO EXISTE" in no_existe, True, False)
    fallos += caso("la del ausente NO dice que getsize lo midiera",
                   "no llego a correr sobre el" in no_existe, True, False)
    fallos += caso("la del cero dice EXISTE Y MIDE CERO",
                   "EXISTE Y MIDE CERO" in cero, True, False)
    fallos += caso("la del cero dice que el cero es una medicion",
                   "El cero es una" in cero, True, False)
    fallos += caso("las dos son DISTINTAS, que es el defecto que se corrige",
                   no_existe == cero, False, True)
    w("   Y LAS TRES SIGUEN TRAYENDO SUS BYTES, que es la pieza (2) del hueco y")
    w("   esta operacion no afloja ninguna de las tres:")
    for nombre, frase in (("NO EXISTE", no_existe), ("CERO BYTES", cero),
                          ("CON CUERPO", con_cuerpo)):
        hay = CR.PATRON_BYTES.search(frase) is not None
        fallos += caso("la frase %-10s trae una cifra de bytes" % nombre,
                       hay, True, False)
    w("   Y NINGUNA DEJA UNA CIFRA DE BYTES SIN SU PAREJA, que es la quinta")
    w("   comprobacion de este mismo instrumento:")
    for nombre, frase in (("NO EXISTE", no_existe), ("CERO BYTES", cero),
                          ("CON CUERPO", con_cuerpo)):
        huerfanas = CR.cifras_sin_pareja(frase)
        fallos += caso("la frase %-10s sin cifras huerfanas" % nombre,
                       len(huerfanas), 0, 1)
    w("")

    w("I) EL COTEJO CON EL DEFECTO VIEJO, QUE NO SE BORRA SINO QUE SE CUENTA")
    w("   Lo que la vuelta 182 publicaba era `max(tam, 0)` con `tam = -1` cuando")
    w("   el fichero no existia, o sea el MISMO CERO en los dos casos:")
    w("      fichero ausente -> max(-1, 0) = %d" % max(-1, 0))
    w("      fichero de cero -> max( 0, 0) = %d" % max(0, 0))
    fallos += caso("el defecto viejo daba el mismo numero en los dos casos",
                   max(-1, 0) == max(0, 0), True, False)
    w("   y las frases nuevas ya no: son dos textos distintos.")
    w("")

    w("=" * 78)
    w("CIFRA fallos: %d" % fallos)
    w("VEREDICTO: %s" % ("VERDE" if fallos == 0 else "ROJO"))
    w("=" * 78)

    t = NL.join(SALIDA) + NL
    ruta = os.path.join(LOOP, "SALIDA_V183_T1C_MUTACION_VEREDICTO.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0 if fallos == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
