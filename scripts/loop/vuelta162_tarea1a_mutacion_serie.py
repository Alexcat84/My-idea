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

LO QUE SE MIDE, Y ES VARIABLE COMPUTADA, NO CONSTANTE LITERAL (EJECUTOR.md 1,
29 ago 2026): `siguiente_libre(entradas(...))` sobre las copias. Si el
instrumento fuera ciego al segundo fichero (la caida de la 161), la `R.31` de
mentira no lo moveria y seguiria diciendo `R.30`. LA MUTACION ES LA PRUEBA: el
valor esperado se cambia y el caso TIENE que caer.

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

FALSA = ("\n## R.31. ENTRADA DE MENTIRA, escrita por el caso positivo por mutacion "
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

    print("B) SIN MUTAR: la serie de las copias tiene que dar lo mismo que el repo")
    limpio = S.entradas(copias)
    limpio_siguiente = S.siguiente_libre(limpio)
    limpio_cols = len(S.colisiones(limpio))
    print("   CIFRA entradas: %d" % len(limpio))
    print("   CIFRA colisiones: %d" % limpio_cols)
    print("   SIGUIENTE LIBRE: R.%d" % limpio_siguiente)
    print("")

    print("C) LA MUTACION: se anade una R.31 DE MENTIRA al OTRO fichero, el que la")
    print("   idempotencia caida de la vuelta 161 no miraba")
    print("   fichero mutado: %s" % os.path.basename(correcciones_copia))
    with io.open(correcciones_copia, "a", encoding="utf-8", newline="\n") as fh:
        fh.write(FALSA)
    mutado = S.entradas(copias)
    mutado_siguiente = S.siguiente_libre(mutado)
    vistas = [(n, rel, ln) for n, rel, ln, _t in mutado if n == 31]
    print("   CIFRA entradas tras la mutacion: %d" % len(mutado))
    print("   la R.31 de mentira, VISTA por el instrumento: %s"
          % (vistas if vistas else "NO LA VE"))
    print("   SIGUIENTE LIBRE tras la mutacion: R.%d" % mutado_siguiente)
    print("")

    print("D) LA MUTACION SOLO EN docs/PENDIENTES.md, para probar que la ceguera")
    print("   habria sido de UN fichero y no de los dos")
    solo_pendientes = S.entradas([pendientes_copia])
    print("   SIGUIENTE LIBRE mirando SOLO docs/PENDIENTES.md: R.%d"
          % S.siguiente_libre(solo_pendientes))
    print("   (esa es exactamente la cifra que la vuelta 161 publico, y por eso cayo)")
    print("")

    casos = [
        ("sin_mutar_la_serie_da_30", limpio_siguiente, 30),
        ("sin_mutar_hay_una_colision", limpio_cols, 1),
        ("la_R31_de_mentira_SE_VE", len(vistas), 1),
        ("y_mueve_el_siguiente_libre_a_32", mutado_siguiente, 32),
        ("mirando_solo_PENDIENTES_la_serie_miente", S.siguiente_libre(solo_pendientes), 30),
    ]

    print("E) PASADA 1, LOS CASOS TAL CUAL: todos tienen que PASAR")
    caidos = []
    for nombre, obtenido, esperado in casos:
        ok = obtenido == esperado
        print("   %-42s esperado %-6r obtenido %-6r %s"
              % (nombre, esperado, obtenido, "PASA" if ok else "CAE"))
        if not ok:
            caidos.append(nombre)
    print("")

    print("F) PASADA 2, LA MUTACION DEL VALOR ESPERADO: cada caso TIENE que CAER")
    sobreviven = []
    for nombre, obtenido, esperado in casos:
        mutado_esp = esperado + 1
        cae = obtenido != mutado_esp
        print("   %-42s esperado MUTADO %-6r obtenido %-6r %s"
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
          "R.31 DE MENTIRA EN EL OTRO FICHERO SE VE, y mueve el siguiente libre de R.30 "
          "a R.32. Mirando solo docs/PENDIENTES.md el instrumento habria seguido diciendo "
          "R.30, que es la ceguera exacta de la vuelta 161." % (len(casos), len(casos), len(casos)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
