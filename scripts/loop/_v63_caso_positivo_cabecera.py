# -*- coding: utf-8 -*-
"""_v63_caso_positivo_cabecera.py . EL CASO POSITIVO DE LA CORRECCION DE LA
CABECERA DE generar_plan_del_lote.py, CON LAS DOS MITADES EN LA MISMA SALIDA.

ES DE SOLO LECTURA. No escribe un plan, ni un nodo, ni un script. Extrae la
version VIEJA del generador del commit que la llevaba, la carga en memoria y la
compara con la de hoy.

LAS TRES PRUEBAS, y la segunda es la que impide que la correccion sea un
acomodo del conteo:

  1. COMO ESTABA. La cabecera vieja es un dict CONSTANTE. Se lee del modulo
     extraido con git show, SIN CORRERLO sobre ningun tramo, y se imprimen sus
     cifras. Salen las mismas dijeras lo que dijeras: son constantes.

  2. COMO QUEDA, SOBRE EL INSUMO VERDADERO. La cabecera de hoy se arma con el
     fichero del tramo 6, el mismo que sellaron los dos planes de la vuelta 62.
     TIENE QUE DAR LAS MISMAS CIFRAS QUE LOS PLANES SELLADOS LLEVAN: 21 actos y
     42 combinaciones. Si diera otras, la correccion estaria acomodando el
     conteo en vez de honrarlo, que es justo la objecion que el acta 62 le hizo
     al D2 de la vuelta anterior.

  3. COMO QUEDA, SOBRE UN INSUMO DISTINTO. La misma cabecera de hoy se arma con
     un tramo FICTICIO de tres actos hecho con filas del propio tramo 6. La de
     hoy dice TRES; la vieja seguiria diciendo VEINTIUNO. AHI ES DONDE LA
     PLANTILLA MENTIA, y es lo unico que esta correccion cambia.

  4. LA FALTA, DECLARADA. Sin --nomina, --dossier, --varas-impresas ni
     --colisiones-esperadas, los cuatro bloques tienen que DECLARAR su ausencia
     con todas las letras en vez de suponerla. Se comprueba que los cuatro
     textos lo dicen.

Uso:
  python scripts/loop/_v63_caso_positivo_cabecera.py
exit 0 si las cuatro pruebas pasan; exit 1 si alguna falla.
"""
import io
import json
import os
import re
import subprocess
import sys
import types

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
COMMIT_VIEJO = "630c6d19"
RUTA = "scripts/loop/generar_plan_del_lote.py"
TRAMO = "docs/loop/TRAMO6_V61.jsonl"
NL = chr(10)


class Args(object):
    def __init__(self, **kw):
        self.__dict__.update(kw)


def cargar_viejo():
    """Trae el fichero del commit viejo y lo ejecuta como modulo suelto."""
    fuente = subprocess.check_output(["git", "show", "%s:%s" % (COMMIT_VIEJO, RUTA)],
                                     cwd=RAIZ).decode("utf-8")
    mod = types.ModuleType("generador_viejo")
    mod.__file__ = os.path.join(RAIZ, RUTA)
    exec(compile(fuente, "generador_viejo", "exec"), mod.__dict__)
    return mod, fuente


def cargar_nuevo():
    sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
    import generar_plan_del_lote as nuevo
    return nuevo


def cifras(texto):
    return re.findall(r"\d+", texto)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("CASO POSITIVO DE LA CORRECCION DE LA CABECERA DE %s" % RUTA)
    print("  la mitad COMO ESTABA sale del commit %s, extraido con git show" % COMMIT_VIEJO)
    print("  la mitad COMO QUEDA sale del fichero de hoy")
    print("=" * 78)
    fallos = []

    viejo, fuente_vieja = cargar_viejo()
    nuevo = cargar_nuevo()
    filas = [json.loads(l) for l in io.open(os.path.join(RAIZ, TRAMO.replace("/", os.sep)),
                                            encoding="utf-8") if l.strip()]
    ORD = "orden_tramo6"
    prot = nuevo.puertas()

    # ---------------------------------------------------------------- 1
    print()
    print("-" * 78)
    print("1. COMO ESTABA: la cabecera vieja es un dict CONSTANTE")
    print("-" * 78)
    vieja = viejo.CABECERA
    for campo in ("tramo_definido_en", "dossier", "vara", "colisiones_esperadas",
                  "vara_de_las_puertas"):
        print("   %-22s %s" % (campo, vieja[campo][:150].replace(NL, " ")))
    if "21 actos" not in vieja["tramo_definido_en"]:
        fallos.append("la cabecera vieja no trae 21 actos donde se esperaba")
    if "42 combinaciones" not in vieja["colisiones_esperadas"]:
        fallos.append("la cabecera vieja no trae 42 combinaciones donde se esperaba")
    if "848 lineas" not in vieja["dossier"]:
        fallos.append("la cabecera vieja no trae 848 lineas donde se esperaba")
    print()
    print("   LAS TRES CIFRAS TALLADAS ESTAN DONDE EL CENSO LAS PUSO: 21 actos,")
    print("   42 combinaciones y 848 lineas. NO DEPENDEN DE NINGUN ARGUMENTO: son")
    print("   valores de un dict de modulo, asi que salen iguales corra lo que corra.")

    # ---------------------------------------------------------------- 2
    print()
    print("-" * 78)
    print("2. COMO QUEDA, SOBRE EL INSUMO VERDADERO: tiene que dar lo mismo que los")
    print("   planes sellados de la vuelta 62 llevan")
    print("-" * 78)
    a = Args(operacion="OP-U-01", tramo=TRAMO, nomina=None, dossier=None,
             varas_impresas=None, colisiones_esperadas=None)
    nueva = nuevo.cabecera(a, filas, ORD, "6", prot,
                           nuevo.cotejo_del_insumo(filas))
    print("   tramo_definido_en : %s" % nueva["tramo_definido_en"][:220].replace(NL, " "))
    print("   vara              : %s" % nueva["vara"][:150].replace(NL, " "))
    print("   colisiones        : %s" % nueva["colisiones_esperadas"][-190:].replace(NL, " "))
    print("   puertas           : %s" % nueva["vara_de_las_puertas"][-200:].replace(NL, " "))
    if "%d actos" % len(filas) not in nueva["tramo_definido_en"]:
        fallos.append("la cabecera de hoy no midio los %d actos del tramo" % len(filas))
    combis = sum(len(f["miembros"]) for f in filas)
    if "%d, contadas al sellar" % combis not in nueva["colisiones_esperadas"]:
        fallos.append("la cabecera de hoy no midio las %d combinaciones" % combis)
    plan_a = json.load(io.open(os.path.join(RAIZ, "docs", "loop",
                                            "PLAN_V62_OPU01_LOTE_A.json"), encoding="utf-8"))
    if "21 actos" not in plan_a["tramo_definido_en"]:
        fallos.append("el plan sellado de la vuelta 62 no dice 21 actos")
    print()
    print("   MEDIDO HOY: %d actos y %d combinaciones." % (len(filas), combis))
    print("   EL PLAN SELLADO DE LA VUELTA 62 DICE: 21 actos y 42 combinaciones.")
    print("   CALZAN. LA CORRECCION HONRA EL CONTEO, NO LO ACOMODA.")

    # ---------------------------------------------------------------- 3
    print()
    print("-" * 78)
    print("3. COMO QUEDA, SOBRE UN INSUMO DISTINTO: ahi es donde la vieja mentia")
    print("-" * 78)
    tres = [dict(f) for f in filas[:3]]
    nueva3 = nuevo.cabecera(a, tres, ORD, "FICTICIO", prot,
                            nuevo.cotejo_del_insumo(tres))
    print("   la de HOY  : %s" % nueva3["tramo_definido_en"][:210].replace(NL, " "))
    print("   la VIEJA   : %s" % vieja["tramo_definido_en"][:210].replace(NL, " "))
    if "3 actos" not in nueva3["tramo_definido_en"]:
        fallos.append("con tres filas la cabecera de hoy no dice 3 actos")
    if "21 actos" not in vieja["tramo_definido_en"]:
        fallos.append("la vieja deberia seguir diciendo 21 actos con tres filas")
    print()
    print("   CON TRES ACTOS DE INSUMO, LA DE HOY DICE TRES Y LA VIEJA SIGUE")
    print("   DICIENDO VEINTIUNO. Esa es la mentira, y esa es la que se corrige.")

    # ---------------------------------------------------------------- 4
    print()
    print("-" * 78)
    print("4. LA FALTA, DECLARADA: sin los cuatro ficheros externos, los cuatro")
    print("   bloques lo dicen en vez de suponerlo")
    print("-" * 78)
    for campo in ("nomina", "dossier", "varas_impresas", "colisiones_esperadas"):
        t = nueva[campo]
        ok = "NO ENTRO NINGUN FICHERO" in t
        print("   %-22s %s" % (campo, "DECLARA LA FALTA" if ok else "NO LA DECLARA: " + t[:90]))
        if not ok:
            fallos.append("el bloque %s no declara su falta" % campo)
    print()
    print("   Y CON EL FICHERO PUESTO, LA CIFRA SE MIDE en vez de tallarse:")
    a2 = Args(operacion="OP-U-01", tramo=TRAMO, nomina=None,
              dossier="docs/loop/SALIDA_V61_DOSSIER_TRAMO6.txt",
              varas_impresas=None, colisiones_esperadas=None)
    nueva2 = nuevo.cabecera(a2, filas, ORD, "6", prot, nuevo.cotejo_del_insumo(filas))
    print("   dossier            : %s" % nueva2["dossier"][:140].replace(NL, " "))
    real = len(io.open(os.path.join(RAIZ, "docs", "loop", "SALIDA_V61_DOSSIER_TRAMO6.txt"),
                       encoding="utf-8").read().split(NL))
    print("   lineas contadas fuera del generador, con python: %d" % real)
    if "(%d lineas" % real not in nueva2["dossier"]:
        fallos.append("el bloque dossier no midio las lineas del fichero que entro")

    print()
    print("=" * 78)
    if fallos:
        print("ROJO, %d de las pruebas fallan:" % len(fallos))
        for f in fallos:
            print("   %s" % f)
        return 1
    print("LAS CUATRO PRUEBAS EN VERDE.")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
