# -*- coding: utf-8 -*-
r"""vuelta162_tarea3_mutacion_fila.py . TAREA 3 de la vuelta 162.

CASO POSITIVO POR MUTACION PARA LA COBERTURA DE FILAS DE TABLA
(adjudicacion 6.6 del acta 161), Y COTEJO DE QUE NINGUN VEREDICTO VIEJO SE MUEVE.

LOS SUJETOS SON FIJOS Y CONGELADOS, no el REPORTE.md vivo (banco 9.10): la
copia del reporte de la vuelta 161 y la del de la 160 sacada de
`git show aa6bb622`, las dos commiteadas como
`docs/loop/SUJETO_FIJO_V162_T3_REPORTE_16*.md`. Un sujeto que se mueve no sirve
de vara.

LOS CASOS, DICHOS ANTES DE CORRERLOS:
  1. `el_161_cotejaba_cero_filas_con_la_guarda_vieja`, y por eso hubo que
     repararla.
  2. `el_161_ahora_coteja_sus_filas_de_fase`: la cifra medida, no la esperada de
     memoria.
  3. `el_160_sigue_dando_cinco`: la vara de aceptacion del encargo, con sus
     palabras.
  4. `el_160_no_gana_ni_una_fila_de_tabla`: su cierre vive en prosa, asi que el
     camino nuevo no le toca nada.
  5. `numero_movido_en_una_fila_pone_la_guarda_ROJA`: se muta EN MEMORIA una
     cifra de una fila de fase y la guarda tiene que caer. Es el caso rojo, y
     se prueba por mutacion, no por asercion.
  6. `fila_sin_cita_cae_al_AVISO`: se le quita la cita a esa misma fila y la
     guarda deja de poder cotejarla; entonces TIENE que decirlo en el aviso, con
     su cifra, en vez de callarse.
  7. `los_dos_sujetos_siguen_en_exit_0` con la guarda nueva: ningun veredicto
     viejo se mueve.

USO:  python scripts/loop/vuelta162_tarea3_mutacion_fila.py
"""
import io
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verificar_cifras_del_reporte as G      # noqa: E402
import _v162_cifras_vieja_copia as VIEJA      # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

LOOP = G.LOOP
S161 = os.path.join(LOOP, "SUJETO_FIJO_V162_T3_REPORTE_161.md")
S160 = os.path.join(LOOP, "SUJETO_FIJO_V162_T3_REPORTE_160.md")
FILA_A_MUTAR = "| fase 06 | 16 / 16 / 0 | `docs/loop/SALIDA_V161_T4_FASE_06.txt` |"


def corre(modulo, ruta, con_filas=True):
    """(exitcode_equivalente, n_cierres, n_filas, n_avisos, fallos)."""
    cierres, nomina = [], {}
    if con_filas:
        filas, avisos = [], []
        fallos, cot, ex, tot = modulo.verificar(
            ruta, cierres_out=cierres, nomina_out=nomina,
            filas_out=filas, avisos_out=avisos)
    else:
        filas, avisos = [], []
        fallos, cot, ex, tot = modulo.verificar(
            ruta, cierres_out=cierres, nomina_out=nomina)
    codigo = 1 if (fallos or not cot) else 0
    return codigo, len(cierres), len(filas), len(avisos), fallos


def main():
    print("=" * 78)
    print("CASO POSITIVO POR MUTACION: LA GUARDA DE CIFRAS Y LA FILA DE TABLA")
    print("=" * 78)
    print("")

    print("A) LOS SUJETOS CONGELADOS")
    for r in (S161, S160):
        print("   %s (%d bytes)" % (os.path.basename(r), os.path.getsize(r)))
    print("")

    print("B) LA GUARDA VIEJA, COPIADA ANTES DE TOCAR NADA")
    v161_v = corre(VIEJA, S161, con_filas=False)
    v160_v = corre(VIEJA, S160, con_filas=False)
    print("   161: exit %d, cierres %d, fallos %d" % (v161_v[0], v161_v[1], len(v161_v[4])))
    print("   160: exit %d, cierres %d, fallos %d" % (v160_v[0], v160_v[1], len(v160_v[4])))
    print("")

    print("C) LA GUARDA NUEVA SOBRE LOS MISMOS SUJETOS")
    v161_n = corre(G, S161)
    v160_n = corre(G, S160)
    print("   161: exit %d, cierres %d, filas %d, avisos %d, fallos %d"
          % (v161_n[0], v161_n[1], v161_n[2], v161_n[3], len(v161_n[4])))
    print("   160: exit %d, cierres %d, filas %d, avisos %d, fallos %d"
          % (v160_n[0], v160_n[1], v160_n[2], v160_n[3], len(v160_n[4])))
    print("")

    tmp = tempfile.mkdtemp(prefix="v162_fila_")
    mutado = os.path.join(LOOP, "_v162_mut_reporte161.md")
    texto = io.open(S161, encoding="utf-8").read()
    if texto.count(FILA_A_MUTAR) != 1:
        print("ROJO: la fila que se iba a mutar aparece %d veces." % texto.count(FILA_A_MUTAR))
        return 1

    print("D) LA MUTACION 1: UNA CIFRA MOVIDA EN UNA FILA DE FASE")
    fila_mala = FILA_A_MUTAR.replace("16 / 16 / 0", "16 / 15 / 0")
    print("   antes : %s" % FILA_A_MUTAR)
    print("   ahora : %s" % fila_mala)
    io.open(mutado, "w", encoding="utf-8", newline="\n").write(
        texto.replace(FILA_A_MUTAR, fila_mala, 1))
    mut1 = corre(G, mutado)
    print("   resultado: exit %d, filas cotejadas %d, fallos %d"
          % (mut1[0], mut1[2], len(mut1[4])))
    for f in mut1[4]:
        print("      %s" % f)
    print("")

    print("E) LA MUTACION 2: A ESA MISMA FILA SE LE QUITA LA CITA")
    fila_sin_cita = "| fase 06 | 16 / 16 / 0 | (sin cita) |"
    print("   ahora : %s" % fila_sin_cita)
    io.open(mutado, "w", encoding="utf-8", newline="\n").write(
        texto.replace(FILA_A_MUTAR, fila_sin_cita, 1))
    mut2 = corre(G, mutado)
    print("   resultado: exit %d, filas cotejadas %d, avisos %d, fallos %d"
          % (mut2[0], mut2[2], mut2[3], len(mut2[4])))
    print("")

    os.remove(mutado)
    shutil.rmtree(tmp, ignore_errors=True)

    casos = [
        ("el_161_cotejaba_cero_filas_con_la_guarda_vieja", v161_v[1], 0),
        ("el_161_ahora_coteja_sus_filas_de_fase", v161_n[2], 4),
        ("el_160_sigue_dando_cinco", v160_n[1], 5),
        ("el_160_no_gana_ni_una_fila_de_tabla", v160_n[2], 0),
        ("numero_movido_en_una_fila_pone_la_guarda_ROJA", mut1[0], 1),
        ("y_solo_cae_esa_fila", mut1[2], 3),
        ("fila_sin_cita_cae_al_AVISO", mut2[3], 1),
        ("y_el_aviso_no_tumba_la_guarda", mut2[0], 0),
        ("el_161_sigue_en_exit_0", v161_n[0], 0),
        ("el_160_sigue_en_exit_0", v160_n[0], 0),
        ("el_161_no_cambio_de_veredicto", v161_n[0], v161_v[0]),
        ("el_160_no_cambio_de_veredicto", v160_n[0], v160_v[0]),
        ("el_160_no_cambio_de_cierres", v160_n[1], v160_v[1]),
    ]

    print("F) PASADA 1, LOS CASOS TAL CUAL: todos tienen que PASAR")
    caidos = []
    for nombre, obtenido, esperado in casos:
        ok = obtenido == esperado
        print("   %-52s esperado %-4r obtenido %-4r %s"
              % (nombre, esperado, obtenido, "PASA" if ok else "CAE"))
        if not ok:
            caidos.append(nombre)
    print("")

    print("G) PASADA 2, LA MUTACION DEL VALOR ESPERADO: cada caso TIENE que CAER")
    sobreviven = []
    for nombre, obtenido, esperado in casos:
        mut = esperado + 1
        cae = obtenido != mut
        print("   %-52s esperado MUTADO %-4r obtenido %-4r %s"
              % (nombre, mut, obtenido, "CAE (bien)" if cae else "SOBREVIVE (mal)"))
        if not cae:
            sobreviven.append(nombre)
    print("")

    if caidos:
        print("ROJO: %d caso(s) no pasan: %s" % (len(caidos), caidos))
        return 1
    if sobreviven:
        print("ROJO: %d caso(s) sobreviven a su mutacion: %s" % (len(sobreviven), sobreviven))
        return 1
    print("VERDE: %d casos, los %d pasan y los %d caen al mutarles el valor esperado."
          % (len(casos), len(casos), len(casos)))
    print("Y LOS TRES QUE IMPORTAN, POR SU NOMBRE: el reporte de la 160 SIGUE DANDO 5 y no "
          "gana ni una fila; una cifra movida en una fila de fase PONE LA GUARDA ROJA; y "
          "una fila sin cita CAE AL AVISO en vez de desaparecer en silencio.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
