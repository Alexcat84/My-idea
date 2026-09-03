# -*- coding: utf-8 -*-
r"""vuelta162_tarea1a_mutacion_serie.py . TAREA 1.a de la vuelta 162.

CASO POSITIVO POR MUTACION SOBRE VARIABLE COMPUTADA, para
`scripts/loop/serie_de_registros.py`.

LO QUE EL ENCARGO PIDE CON SUS PALABRAS: *"mete una `R.31` de mentira en el OTRO
fichero y el instrumento tiene que verla"*. EL OTRO fichero es
`docs/plan/CORRECCIONES_A_APLICAR.md`, que es justo el que la idempotencia caida
de la vuelta 161 NO miraba.

COMO SE HACE SIN TOCAR EL REPO: `serie_de_registros.entradas()` recibe las sedes
POR PARAMETRO a proposito. Aqui se copian los dos ficheros a un directorio
temporal, se muta LA COPIA y se apunta el instrumento a las copias. El arbol de
trabajo no se toca, y se comprueba al final que sigue igual.

--- CORRECCION DECLARADA (vuelta 163, TAREA 3; acta 162, seccion 5.2) ---

ESTE ARNES NACIO CADUCADO DENTRO DE SU PROPIO COMMIT. Medido por el auditor y
reproducido hoy: corrido en la vuelta 163 sale ROJO con 4 de 5 casos que no
pasan, y uno de ellos (`la_R31_de_mentira_SE_VE`) ADEMAS SOBREVIVIA a la
mutacion de su valor esperado, o sea que su segunda pasada ya no mordia. Su
salida sellada (`docs/loop/SALIDA_V162_T1A_MUTACION_SERIE.txt`) era HONESTA
cuando corrio, con la serie en 22 entradas y siguiente libre `R.30`.

LO QUE FALLABA ERA LA CONSTRUCCION, NO LA MEDICION: sus valores esperados
estaban CLAVADOS (`30`, `31`, `32`) a un estado que la TAREA 1.b de la vuelta 162
cambio EN EL MISMO COMMIT `e2b2e74f`, donde nacen el arnes y la `R.31` de verdad
juntos. Desde ese dia el `31` de mentira ya no era libre, dejo de mover el
siguiente libre y el caso que contaba "las entradas con el numero 31" contaba
DOS, la de verdad y la de mentira.

LOS ESPERADOS VIEJOS, QUE NO SE BORRAN (EJECUTOR.md 8):
    ("sin_mutar_la_serie_da_30", limpio_siguiente, 30)
    ("sin_mutar_hay_una_colision", limpio_cols, 1)
    ("la_R31_de_mentira_SE_VE", len(vistas), 1)
    ("y_mueve_el_siguiente_libre_a_32", mutado_siguiente, 32)
    ("mirando_solo_PENDIENTES_la_serie_miente", ..., 30)

COMO SE ARREGLA, Y ES LA UNICA FORMA QUE NO VUELVE A ENVEJECER: LOS ESPERADOS SE
COMPUTAN DEL ESTADO DEL DIA Y LO QUE SE PRUEBA ES EL DELTA.

  - EL NUMERO DE LA ENTRADA DE MENTIRA NO SE TECLEA: es `siguiente_libre()` sobre
    las copias sin mutar, o sea el primer numero que hoy esta libre. Asi la
    entrada de mentira SIEMPRE es nueva, valga la serie 22 entradas o 240.
  - LO QUE SE PRUEBA ES EL DELTA, invariante al numero que toque: metida en EL
    OTRO fichero, la entrada de mentira MUEVE el siguiente libre EXACTAMENTE UNO;
    y mirando SOLO `docs/PENDIENTES.md` NO lo mueve NADA. Esa segunda mitad es la
    ceguera exacta de la vuelta 161, y es lo que este arnes existe para cazar.
  - NINGUN ESPERADO ES UN LITERAL DE ESTADO. Los unicos literales que quedan son
    los deltas (`+1`, `0`, `True`), que es lo que la construccion promete.

USO:
  python scripts/loop/vuelta162_tarea1a_mutacion_serie.py
"""
import io
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import serie_de_registros as S   # noqa: E402

# EL TEXTO DE LA ENTRADA DE MENTIRA. Su NUMERO se interpola por computo: un
# numero tecleado aqui es exactamente lo que caduco este arnes.
PLANTILLA_FALSA = (
    "\n## R.%d. ENTRADA DE MENTIRA, escrita por el caso positivo por mutacion "
    "de la vuelta 162 en una COPIA TEMPORAL. Si esto aparece en el repo, algo "
    "salio muy mal.\n")


def sha_del_repo():
    return [(os.path.relpath(r, S.RAIZ).replace("\\", "/"),
             os.path.getsize(r)) for r in S.SEDES]


def main():
    print("=" * 78)
    print("CASO POSITIVO POR MUTACION: LA SERIE R.N SE LEE DE LOS DOS FICHEROS")
    print("=" * 78)
    print("")

    antes_del_repo = sha_del_repo()
    tmp = tempfile.mkdtemp(prefix="v162_serie_")
    copias = []
    for ruta in S.SEDES:
        destino = os.path.join(tmp, os.path.basename(ruta))
        shutil.copyfile(ruta, destino)
        copias.append(destino)
    pendientes_copia, correcciones_copia = copias

    print("A) EL SUJETO: COPIAS TEMPORALES DE LAS DOS SEDES")
    for c in copias:
        print("   %s (%d bytes)" % (os.path.basename(c), os.path.getsize(c)))
    print("")

    print("B) EL ESTADO DE PARTIDA, COMPUTADO HOY Y NO TECLEADO")
    limpio = S.entradas(copias)
    limpio_siguiente = S.siguiente_libre(limpio)
    limpio_cols = len(S.colisiones(limpio))
    solo_pend_antes = S.siguiente_libre(S.entradas([pendientes_copia]))
    vistas_antes = [n for n, _rel, _ln, _t in limpio if n == limpio_siguiente]
    print("   CIFRA entradas: %d" % len(limpio))
    print("   CIFRA colisiones: %d" % limpio_cols)
    print("   SIGUIENTE LIBRE de las DOS sedes: R.%d" % limpio_siguiente)
    print("   SIGUIENTE LIBRE mirando SOLO docs/PENDIENTES.md: R.%d" % solo_pend_antes)
    print("   CIFRA entradas que ya llevan el numero R.%d: %d (tiene que ser 0: es el libre)"
          % (limpio_siguiente, len(vistas_antes)))
    print("")

    print("C) LA MUTACION: se anade una R.%d DE MENTIRA al OTRO fichero, el que la"
          % limpio_siguiente)
    print("   idempotencia caida de la vuelta 161 no miraba. EL NUMERO SALE DE")
    print("   siguiente_libre() Y NO ESTA TECLEADO.")
    print("   fichero mutado: %s" % os.path.basename(correcciones_copia))
    with io.open(correcciones_copia, "a", encoding="utf-8", newline="\n") as fh:
        fh.write(PLANTILLA_FALSA % limpio_siguiente)
    mutado = S.entradas(copias)
    mutado_siguiente = S.siguiente_libre(mutado)
    mutado_cols = len(S.colisiones(mutado))
    vistas = [(n, rel, ln) for n, rel, ln, _t in mutado if n == limpio_siguiente]
    print("   CIFRA entradas tras la mutacion: %d" % len(mutado))
    print("   la R.%d de mentira, VISTA por el instrumento: %s"
          % (limpio_siguiente, vistas if vistas else "NO LA VE"))
    print("   SIGUIENTE LIBRE tras la mutacion: R.%d" % mutado_siguiente)
    print("")

    print("D) LA MISMA MUTACION MIRADA SOLO DESDE docs/PENDIENTES.md, para probar que")
    print("   la ceguera habria sido de UN fichero y no de los dos")
    solo_pend_despues = S.siguiente_libre(S.entradas([pendientes_copia]))
    print("   SIGUIENTE LIBRE mirando SOLO docs/PENDIENTES.md, tras la mutacion: R.%d"
          % solo_pend_despues)
    print("   (mirando un solo fichero la entrada de mentira es INVISIBLE, y esa es")
    print("   exactamente la ceguera con la que cayo la vuelta 161)")
    print("")

    # LOS ESPERADOS SON DELTAS, NO ESTADOS. Ninguno se teclea del estado del dia.
    casos = [
        ("sin_mutar_el_libre_no_esta_ocupado", len(vistas_antes), 0),
        ("la_entrada_de_mentira_SE_VE", len(vistas), 1),
        ("mueve_el_siguiente_libre_EXACTAMENTE_UNO",
         mutado_siguiente - limpio_siguiente, 1),
        ("anade_EXACTAMENTE_UNA_entrada", len(mutado) - len(limpio), 1),
        ("no_crea_colisiones", mutado_cols - limpio_cols, 0),
        ("mirando_solo_PENDIENTES_el_libre_NO_se_mueve",
         solo_pend_despues - solo_pend_antes, 0),
        ("y_por_eso_PENDIENTES_solo_MIENTE_sobre_el_libre",
         mutado_siguiente - solo_pend_despues, 1),
    ]

    print("E) PASADA 1, LOS CASOS TAL CUAL: todos tienen que PASAR")
    print("   (el esperado de cada uno es un DELTA, no un estado)")
    caidos = []
    for nombre, obtenido, esperado in casos:
        ok = obtenido == esperado
        print("   %-48s esperado %-4r obtenido %-4r %s"
              % (nombre, esperado, obtenido, "PASA" if ok else "CAE"))
        if not ok:
            caidos.append(nombre)
    print("")

    print("F) PASADA 2, LA MUTACION DEL VALOR ESPERADO: cada caso TIENE que CAER")
    sobreviven = []
    for nombre, obtenido, esperado in casos:
        mutado_esp = esperado + 1
        cae = obtenido != mutado_esp
        print("   %-48s esperado MUTADO %-4r obtenido %-4r %s"
              % (nombre, mutado_esp, obtenido, "CAE (bien)" if cae else "SOBREVIVE (mal)"))
        if not cae:
            sobreviven.append(nombre)
    print("")

    shutil.rmtree(tmp, ignore_errors=True)
    despues_del_repo = sha_del_repo()
    print("G) EL ARBOL DE TRABAJO NO SE TOCO")
    print("   antes:   %s" % antes_del_repo)
    print("   despues: %s" % despues_del_repo)
    intacto = antes_del_repo == despues_del_repo
    print("   IDENTICO: %s" % ("SI" if intacto else "NO"))
    print("")

    if caidos:
        print("ROJO: %d caso(s) no pasan tal cual: %s" % (len(caidos), caidos))
        return 1
    if sobreviven:
        print("ROJO: %d caso(s) sobreviven a su mutacion: %s" % (len(sobreviven), sobreviven))
        return 1
    if not intacto:
        print("ROJO: el arbol de trabajo cambio de tamano durante la prueba.")
        return 1
    print("VERDE: %d casos, los %d pasan y los %d caen al mutar el valor esperado. LA "
          "ENTRADA DE MENTIRA EN EL OTRO FICHERO SE VE y mueve el siguiente libre "
          "EXACTAMENTE UNO (de R.%d a R.%d); mirando solo docs/PENDIENTES.md el "
          "instrumento se queda en R.%d, que es la ceguera exacta de la vuelta 161. "
          "NINGUN ESPERADO ES UN ESTADO: todos son deltas, y por eso esto no puede "
          "volver a caducar."
          % (len(casos), len(casos), len(casos), limpio_siguiente, mutado_siguiente,
             solo_pend_despues))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
