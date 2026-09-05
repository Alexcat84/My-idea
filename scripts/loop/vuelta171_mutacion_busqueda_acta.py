# -*- coding: utf-8 -*-
r"""vuelta171_mutacion_busqueda_acta.py . CASO POSITIVO POR MUTACION DE LA
BUSQUEDA DEL COMMIT DEL ACTA (`tallar_cabecera_reporte.py:buscar_acta`),
ESTRENADA EN LA VUELTA 171.

POR QUE EXISTE ESTE FICHERO Y NO SOLO UN FLAG: la bateria
`scripts/loop/verificar_mutaciones_viejas.py` invoca cada arnes SIN ARGUMENTOS.

QUE PRUEBA, Y ES LO QUE MAS FALTA HACIA PROBAR PORQUE LA GUARDA SE AFLOJO:

  (1) QUE LA PASADA ESTRICTA SIGUE MANDANDO. Mientras el titulo este al
      principio, la pasada suelta NI SE CORRE. Esto es lo que garantiza que
      ninguna vuelta vieja cambie de resultado.
  (2) QUE LA PASADA SUELTA SOLO ENTRA CUANDO LA ESTRICTA DA CERO.
  (3) QUE LA EXIGENCIA DE UN SOLO ACIERTO NO SE AFLOJO: dos aciertos sueltos
      siguen siendo dos, y el llamante los rechaza igual que antes.
  (4) QUE CERO SIGUE SIENDO CERO: si el titulo no esta en ningun sitio, no se
      inventa nada.
  (5) EL CASO REAL, LEIDO DE GIT HOY: el commit del acta 170 se encuentra por la
      pasada suelta y NO por la estricta, y el que se encuentra es exactamente
      uno.

SUJETO: filas de `git log` fabricadas EN MEMORIA, mas la lectura real de
`git log` de hoy. CERO escrituras.

SUJETO CONGELADO (condicion de entrada a la bateria desde la vuelta 148): las
filas de mentira son literales de este proceso, y el sujeto real es el commit
`d7b18370`, ya escrito y firmado, cuyo asunto no se reescribe (asi lo declara
el commit `0caca89f`).

NINGUN VEREDICTO ES UNA CONSTANTE LITERAL: cada caso sale de llamar a la funcion
real sobre un sujeto distinto, y la segunda pasada muta el valor esperado y
exige que el caso CAIGA.

USO:  python scripts/loop/vuelta171_mutacion_busqueda_acta.py
"""
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tallar_cabecera_reporte as T   # noqa: E402

RAIZ = T.RAIZ
TITULO = "ACTA DE LA VUELTA 170 DEL AUDITOR"


def patrones(n=170):
    return [re.compile(r"^ACTA DE LA VUELTA %d DEL AUDITOR\b" % n),
            re.compile(r"^ACTA DEL AUDITOR,\s*VUELTA %d\b" % n)]


def prueba_de_mutacion():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 171: CASO POSITIVO POR MUTACION DE LA BUSQUEDA DEL COMMIT DEL ACTA")
    print("=" * 78)
    print("")
    casos = []
    P = patrones()

    print("A) LA PASADA ESTRICTA MANDA, Y LA SUELTA NI SE CORRE")
    filas = [("aaaa1111", "%s: cuerpo" % TITULO),
             ("bbbb2222", "otra cosa que no es un acta"),
             ("cccc3333", "@ %s: el mismo titulo con ruido delante" % TITULO)]
    hall, anclado = T.buscar_acta(filas, P)
    print("   filas: 1 anclada y 1 suelta -> aciertos %d, anclado=%r"
          % (len(hall), anclado))
    print("   el hash elegido: %s" % (hall[0][0] if hall else "(ninguno)"))
    casos.append(("A_la_estricta_gana", anclado, True))
    casos.append(("A_y_devuelve_UNA_sola", len(hall), 1))
    casos.append(("A_y_es_la_anclada_no_la_ruidosa",
                  hall[0][0] if hall else "", "aaaa1111"))
    print("")

    print("B) SIN NINGUNA ANCLADA, ENTRA LA SUELTA")
    filas = [("bbbb2222", "otra cosa"),
             ("cccc3333", "@ %s: con ruido delante @" % TITULO)]
    hall, anclado = T.buscar_acta(filas, P)
    print("   aciertos %d, anclado=%r, hash %s"
          % (len(hall), anclado, hall[0][0] if hall else "(ninguno)"))
    casos.append(("B_la_suelta_entra", anclado, False))
    casos.append(("B_y_encuentra_UNA", len(hall), 1))
    casos.append(("B_y_es_la_ruidosa", hall[0][0] if hall else "", "cccc3333"))
    print("")

    print("C) LA EXIGENCIA DE UN SOLO ACIERTO NO SE AFLOJO")
    filas = [("cccc3333", "@ %s: uno" % TITULO),
             ("dddd4444", "ruido y %s: y dos" % TITULO)]
    hall, anclado = T.buscar_acta(filas, P)
    print("   dos sueltas -> aciertos %d (el llamante lo llama AMBIGUO)" % len(hall))
    casos.append(("C_dos_sueltas_siguen_siendo_dos", len(hall), 2))
    casos.append(("C_y_no_se_elige_ninguna", len(hall) == 1, False))
    print("")

    print("D) CERO SIGUE SIENDO CERO: NO SE INVENTA NINGUN HASH")
    filas = [("eeee5555", "un commit cualquiera"),
             ("ffff6666", "ACTA DE LA VUELTA 169 DEL AUDITOR: la de al lado")]
    hall, anclado = T.buscar_acta(filas, P)
    print("   aciertos %d" % len(hall))
    casos.append(("D_sin_titulo_no_hay_acierto", len(hall), 0))
    print("")

    print("E) LA SEGUNDA FORMA DEL TITULO (vuelta 106) SIGUE CASANDO ANCLADA")
    filas = [("7777aaaa", "ACTA DEL AUDITOR, VUELTA 170 (4 sep 2026, auditor Opus 5)")]
    hall, anclado = T.buscar_acta(filas, P)
    print("   aciertos %d, anclado=%r" % (len(hall), anclado))
    casos.append(("E_la_forma_de_la_106_sigue_anclada", anclado, True))
    casos.append(("E_y_acierta_una", len(hall), 1))
    print("")

    print("F) EL CASO REAL, LEIDO DE GIT HOY Y NO SUPUESTO")
    r = subprocess.run(["git", "log", "--pretty=format:%H\x01%s", "-400"],
                       cwd=RAIZ, capture_output=True, text=True)
    reales = [l.split("\x01", 1) for l in r.stdout.splitlines() if "\x01" in l]
    print("   asuntos leidos de git log: %d" % len(reales))
    solo_anclados = [(h, s) for h, s in reales if any(p.match(s) for p in P)]
    hall, anclado = T.buscar_acta(reales, P)
    print("   los que EMPIEZAN por el titulo: %d" % len(solo_anclados))
    print("   los que buscar_acta encuentra: %d (anclado=%r)" % (len(hall), anclado))
    if hall:
        print("   hash: %s" % hall[0][0][:8])
        print("   asunto: %s" % hall[0][1][:110])
    casos.append(("F_en_git_hoy_NINGUNO_empieza_por_el_titulo", len(solo_anclados), 0))
    casos.append(("F_pero_buscar_acta_encuentra_exactamente_uno", len(hall), 1))
    casos.append(("F_y_lo_encuentra_por_la_pasada_suelta", anclado, False))
    casos.append(("F_y_es_el_commit_d7b18370",
                  hall[0][0][:8] if hall else "", "d7b18370"))
    casos.append(("F_cuyo_asunto_lleva_ruido_delante",
                  hall[0][1].startswith(TITULO) if hall else True, False))
    print("")

    print("G) PASADA 1, LOS CASOS TAL CUAL")
    fallos = 0
    for nombre, real, esperado in casos:
        bien = (real == esperado)
        print("   %-52s %s   (real=%r esperado=%r)"
              % (nombre, "PASA" if bien else "FALLA", real, esperado))
        if not bien:
            fallos += 1
    print("   CIFRA casos: %d | pasan: %d | fallan: %d"
          % (len(casos), len(casos) - fallos, fallos))
    print("")

    print("H) PASADA 2, SE MUTA EL VALOR ESPERADO Y CADA CASO TIENE QUE CAER")
    caen = 0
    for nombre, real, esperado in casos:
        if isinstance(esperado, bool):
            mutado = not esperado
        elif isinstance(esperado, int):
            mutado = esperado + 1
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
        return 0
    print("ROJO: fallos=%d, casos que no caen=%d" % (fallos, len(casos) - caen))
    return 1


if __name__ == "__main__":
    sys.exit(prueba_de_mutacion())
