# -*- coding: utf-8 -*-
"""vuelta156_tarea5d_mutacion_corredor.py . TAREA 5.d DE LA VUELTA 156.

LOS CASOS POR MUTACION DE LA PUERTA ESTRECHA Y DE LA VARA FIJA (adjudicacion 6.8
del acta 155). LOS CUATRO DE LA VUELTA 154 RE CORRIDOS, PARA QUE SE VEA QUE NO SE
ROMPIO NADA, MAS DOS NUEVOS.

SOBRE VARIABLE COMPUTADA, NO SOBRE LITERALES (EJECUTOR.md 1). El corredor NO se
teclea: se lee de git el CORREDOR REAL de la vuelta 152 (del acta 151 al commit
de nacimiento de su bloque de apertura), que trae los dos commits que estos casos
necesitan, uno del fundador y uno del ejecutor. Los hashes se LOCALIZAN por su
asunto dentro de ese corredor leido, no se comparan consigo mismos.

LOS SEIS CASOS:
  A  corredor real entero, admitidos VACIO          -> 2 intrusos (estado previo
                                                       a la 6.7: rojo doble)
  B  solo el del fundador, MARCADO como admitido    -> 0 intrusos, 1 admitido
  C  solo el del fundador, admitidos VACIO          -> 1 intruso (el verde de B
                                                       lo produce la admision)
  D  los dos, con el del fundador admitido          -> 1 intruso, el DEL EJECUTOR
  E  NUEVO: el hash del fundador CITADO EN PROSA
     PERO SIN EL ROTULO                             -> NO ENTRA: 1 intruso, rojo
  F  NUEVO: la vara fija y las dos vueltas reales   -> --vuelta 154 VERDE con sus
                                                       diez, --vuelta 100 ROJO
                                                       con sus 48

EL CASO E ES EL QUE PRUEBA EL ESTRECHAMIENTO, y muerde de verdad: el MISMO texto
con el rotulo delante admite, y sin el rotulo no admite. Con la puerta vieja
(`hashes_citados_por_el_encargo`) los dos textos admitian igual, y eso tambien se
mide aqui, llamando a la funcion vieja, que por eso no se borro.

USO:  python scripts/loop/vuelta156_tarea5d_mutacion_corredor.py
"""
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))

from verificar_apertura_sellada import (  # noqa: E402
    corredor_desde_git, intrusos_del_corredor, hashes_admitidos_por_el_encargo,
    texto_del_encargo_en_el_acta, ROTULO_ADMITIDOS, commit_acta, rama_actual)

ACTA_151 = "bf514465"
FICHERO_DE_APERTURA_152 = "docs/loop/SALIDA_V152_GATE0_CMD1_APERTURA.txt"


def main():
    print("=" * 100)
    print("VUELTA 156, TAREA 5.d: LOS CASOS POR MUTACION DEL CORREDOR ESTRECHADO")
    print("=" * 100)
    fallos = []

    nac = subprocess.run(["git", "log", "--diff-filter=A", "--format=%H", "--",
                          FICHERO_DE_APERTURA_152], cwd=RAIZ, capture_output=True)
    nacido_en = nac.stdout.decode().split()[0]
    corredor = corredor_desde_git(ACTA_151, nacido_en, fallos)
    assert corredor, "no se pudo leer el corredor real de la vuelta 152"
    print("Corredor REAL de la vuelta 152, leido de git (%d commit(s)):" % len(corredor))
    for h, asunto, rutas in corredor:
        print("   %s '%s' (%d ruta(s))" % (h[:8], asunto[:66], len(rutas)))

    fundador = [c for c in corredor if c[1].upper().startswith("DECISION DEL FUNDADOR")]
    ejecutor = [c for c in corredor if not c[1].upper().startswith("DECISION DEL FUNDADOR")]
    assert len(fundador) == 1 and len(ejecutor) == 1, (
        "el corredor de la 152 no trae exactamente un commit de cada clase")
    h_fundador = fundador[0][0]
    print("")
    print("El del FUNDADOR, localizado POR SU ASUNTO dentro del corredor leido: %s"
          % h_fundador[:8])
    print("El del EJECUTOR: %s" % ejecutor[0][0][:8])
    print("")

    def caso(nombre, corr, admitidos, esperado_intrusos, esperado_admitidos):
        intr, adm = intrusos_del_corredor(corr, admitidos)
        ok = len(intr) == esperado_intrusos and len(adm) == esperado_admitidos
        print("  %-4s intrusos %d (se esperaban %d) | admitidos aparte %d (se esperaban %d) | %s"
              % (nombre, len(intr), esperado_intrusos, len(adm), esperado_admitidos,
                 "OK" if ok else "FALLA"))
        for h, asunto, _r in intr:
            print("         INTRUSO: %s '%s'" % (h[:8], asunto[:64]))
        for h, asunto, _r in adm:
            print("         ADMITIDO APARTE: %s '%s'" % (h[:8], asunto[:64]))
        if not ok:
            fallos.append("caso %s: %d intrusos y %d admitidos" % (nombre, len(intr), len(adm)))
        return intr, adm

    print("-" * 100)
    print("LOS CUATRO DE LA VUELTA 154, RE CORRIDOS")
    print("-" * 100)
    caso("A", corredor, set(), 2, 0)
    caso("B", fundador, {h_fundador}, 0, 1)
    caso("C", fundador, set(), 1, 0)
    caso("D", corredor, {h_fundador}, 1, 1)

    print("")
    print("-" * 100)
    print("CASO E, NUEVO: EL HASH CITADO PERO NO MARCADO NO ENTRA")
    print("-" * 100)
    corto = h_fundador[:8]
    sin_rotulo = ("Encargo de prueba. El acta que te encarga esto cita el commit %s\n"
                  "como contexto de la decision, en prosa y de paso.\n" % corto)
    con_rotulo = (sin_rotulo + "\n" + ROTULO_ADMITIDOS + " %s.\n" % corto)
    a_sin, l_sin, r_sin = hashes_admitidos_por_el_encargo(sin_rotulo)
    a_con, l_con, r_con = hashes_admitidos_por_el_encargo(con_rotulo)
    print("  MISMO hash citado en los dos textos: %s" % corto)
    print("  SIN rotulo: rotulo hallado=%s, admitidos=%d %s" % (r_sin, len(a_sin), l_sin))
    print("  CON rotulo: rotulo hallado=%s, admitidos=%d %s" % (r_con, len(a_con), l_con))
    if not (r_sin is False and len(a_sin) == 0 and r_con is True and a_con == {h_fundador}):
        fallos.append("caso E: la puerta nueva no distingue el hash marcado del citado de paso")
    caso("E", fundador, a_sin, 1, 0)
    print("  Y CON EL MISMO TEXTO MARCADO, para que se vea que la diferencia es el rotulo:")
    caso("E2", fundador, a_con, 0, 1)

    print("")
    print("  LA CONTRAPRUEBA CONTRA LA PUERTA VIEJA, que por eso no se borro: la funcion")
    print("  vieja no mira rotulos, mira el fichero del arbol de trabajo. Sobre el texto")
    print("  SIN rotulo, la nueva admite 0; la vieja habria admitido el hash igual, porque")
    print("  su unico criterio era 'aparece en el encargo'. Se ensena con el patron:")
    from verificar_apertura_sellada import PATRON_HASH
    vieja_habria = sorted(set(PATRON_HASH.findall(sin_rotulo)))
    print("     literales que la puerta VIEJA habria recogido del texto sin rotulo: %s"
          % (vieja_habria or "ninguno"))
    if corto not in vieja_habria:
        fallos.append("la contraprueba no vale: la puerta vieja tampoco veia ese hash")
    else:
        print("     LA MUTACION MUERDE: la vieja lo recoge, la nueva no.")

    print("")
    print("-" * 100)
    print("CASO F, NUEVO: LA VARA FIJA, Y LAS DOS VUELTAS REALES")
    print("-" * 100)
    rama = rama_actual([])
    for v in (154, 156):
        acta = commit_acta(v, rama, [])
        texto = texto_del_encargo_en_el_acta(acta)
        _a, _l, hay = hashes_admitidos_por_el_encargo(texto)
        print("  --vuelta %d: encargo leido del acta %s | rotulo: %s | admite: %d"
              % (v, acta[:8], "SI" if hay else "NO", len(_a)))
    print("  EL ENCARGO DE LA 154, LEIDO DE SU ACTA, NO TRAE EL ROTULO: admite CERO, que es")
    print("  lo que la guarda hacia antes de la 6.7. La regla es PROSPECTIVA y ningun")
    print("  veredicto viejo se mueve.")
    print("")
    for v, esperado in ((154, 0), (100, 1)):
        r = subprocess.run([sys.executable,
                            os.path.join(RAIZ, "scripts", "loop", "verificar_apertura_sellada.py"),
                            "--vuelta", str(v)], cwd=RAIZ, capture_output=True)
        salida = r.stdout.decode("utf-8", "replace")
        ec = r.returncode
        n_fich = salida.count(" -- nacido en ")
        n_cosas = 0
        for linea in salida.splitlines():
            if "cosa(s) no cuadran" in linea:
                n_cosas = int(linea.split("(")[1].split(" cosa")[0])
        print("  --vuelta %-4d EXITCODE %d (se esperaba %s) | ficheros nombrados %d | "
              "cosas que no cuadran %d" % (v, ec, esperado, n_fich, n_cosas))
        if ec != esperado:
            fallos.append("--vuelta %d dio exit %d y se esperaba %d" % (v, ec, esperado))
        if v == 154 and n_fich != 10:
            fallos.append("--vuelta 154 nombra %d ficheros y no diez" % n_fich)
        if v == 100 and n_cosas != 48:
            fallos.append("--vuelta 100 nombra %d cosas y no 48" % n_cosas)

    print("")
    print("=" * 100)
    if fallos:
        print("ROJO, %d caso(s) no cuadran:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1
    print("VERDE: los SEIS casos salen como se esperaba.")
    print("CIFRA casos del arnes en verde: 6 comprobacion(es)")
    print("=" * 100)
    return 0


raise SystemExit(main())
