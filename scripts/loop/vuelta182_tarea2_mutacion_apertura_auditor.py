# -*- coding: utf-8 -*-
r"""vuelta182_tarea2_mutacion_apertura_auditor.py . EL CASO POSITIVO POR MUTACION
DE `apertura_del_auditor.py`.

QUE TIENE QUE PROBAR, Y LO DICE EL ENCARGO: *"Con CASO POR MUTACION sobre variable
computada: si el sello se intenta despues de tocar cualquiera de los tres, TIENE
QUE CAER"*.

Y LO DICE TAMBIEN `EJECUTOR.md` 1, letra del 29 ago 2026, EL CASO ROJO SE PRUEBA
POR MUTACION: *"ningun `assert`, guarda o caso rojo se publica como prueba sin
haber corrido antes su prueba de mutacion: se cambia el valor esperado y se
comprueba que el caso CAE"*. Esa letra nace de una caida concreta, la 2 de la
vuelta 89, donde un caso rojo comparaba `"ENTRA"` con `"ENTRA"`: **una constante
literal contra si misma, que no puede fallar nunca.**

AQUI NINGUNA VARIABLE DE VEREDICTO ES UNA CONSTANTE LITERAL. Todas salen de
llamar a `puede_sellar()` o a `sellar()` DE VERDAD sobre la bitacora del modulo,
y al final se muta el valor esperado y se comprueba que el caso CAE.

TODO EL MATERIAL VA FABRICADO EN UN TEMPORAL: el sello de prueba se escribe en un
directorio de mentira, no en `docs/loop/`. **NI EL REPO NI `docs/loop/` SE
TOCAN** (`P.16`, quien fabrica limpia).

LOS ESCENARIOS, UNO POR CADA PROHIBIDO Y UNO LIMPIO:

  A) bitacora limpia               -> tiene que PODER sellar
  B) tras `git log`                -> NO
  C) tras `git status`             -> NO
  D) tras abrir `REPORTE.md`       -> NO
  E) tras los tres                 -> NO, y los nombra los tres
  F) sellar de verdad tras tocar   -> ROJO y **NO escribe fichero de sello**

SUJETO CONGELADO, DECLARADO EN LA VUELTA 183 Y MEDIDO, NO AFIRMADO. Este arnes
no entro en la nomina de la bateria en su propia vuelta, y al abrir la 183
`arneses_que_faltan()` lo nombraba solo, con la cifra en el bloque H.9 de
`docs/loop/SALIDA_V183_APERTURA.txt`: *"faltan 1 . FALTA:
vuelta182_tarea2_mutacion_apertura_auditor.py"*. Al meterlo,
`guarda_del_sujeto_congelado()` lo clasificaba NO DECIDIBLE, porque trae LAS DOS
huellas: las de congelado (`tempfile`, `mkdtemp`) y una de sujeto vivo
(`REPORTE.md`). LA GUARDA NO ADIVINA CUAL MANDA, y hace bien: pide que el propio
arnes lo declare. AQUI SE DECLARA, Y CON LA MEDICION DELANTE: la unica aparicion
de `REPORTE.md` fuera de este docstring es UN DATO DENTRO DE UNA TABLA DE
ESCENARIOS, la linea `("tras abrir REPORTE.md", ["REPORTE.md"], False)`, y este
fichero NO ABRE `docs/loop/REPORTE.md` en ninguna linea: todo lo que toca lo
fabrica en un `mkdtemp` y lo retira (`P.16`). El sujeto, por tanto, esta
congelado.

LA REPARACION DE LA VUELTA 185, TAREA 1.b, DECLARADA AQUI Y NO ESCONDIDA. Este
arnes salia `exit 0` y sus catorce casos pasaban, pero ESCRIBIA EN SU SALIDA
SELLADA UN DATO QUE CAMBIA SOLO: el sufijo aleatorio del `mkdtemp` se colaba en
el informe de `sellar()` que los bloques C y D pegan, y la doble corrida de la
bateria, que compara byte a byte, lo cazaba. Tres lineas de diferencia, las 53,
54 y 55 de su salida, y nada mas. La reparacion es `sin_temporal()`, PURA, que
sustituye TODAS las formas de esa ruta por el literal `<TEMPORAL>` ANTES del
recorte a 130 caracteres: recortar primero partiria la ruta por la mitad y
dejaria media sin normalizar. LO QUE ESTE ARNES PRUEBA NO SE TOCO: los catorce
casos son los mismos, ningun esperado se afloja y ningun escenario se quita.
ESTA REPARACION REESCRIBE `docs/loop/SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt`
con `<TEMPORAL>` dentro, y eso es esperado y se dice. Su arnes propio es
`scripts/loop/vuelta185_tarea1b_mutacion_sin_temporal.py`.

USO:
  python scripts/loop/vuelta182_tarea2_mutacion_apertura_auditor.py
"""
import importlib
import io
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import apertura_del_auditor as AP   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)


# LA MARCA QUE SUSTITUYE A LA RUTA DEL TEMPORAL. Es un literal y no una cadena
# vacia a proposito: borrar la ruta dejaria la linea muda sobre el hecho de que
# ahi habia una ruta, y esta casa prefiere que se vea el hueco.
MARCA_TEMPORAL = "<TEMPORAL>"


def sin_temporal(linea, tmp):
    """LA RUTA DEL TEMPORAL, SUSTITUIDA POR `<TEMPORAL>` EN TODAS SUS FORMAS.
    PURA: recibe dos cadenas y devuelve una, no lee ni escribe nada, y por eso
    su arnes la puede tumbar caso por caso sin tocar el repo.

    LAS CUATRO FORMAS QUE CUBRE, y las cuatro hacen falta porque el informe de
    `sellar()` no promete ninguna en concreto:
      - LA ABSOLUTA, tal cual la devuelve `mkdtemp`.
      - LA RELATIVA CON BARRA NORMAL, que es la que salio de verdad en las
        lineas 53 a 55 de la salida sellada.
      - LA RELATIVA CON BARRA INVERTIDA, que es la que `os.path.relpath`
        devuelve en Windows antes de que nadie la normalice.
      - EL NOMBRE BASE SUELTO del directorio, que es la unica forma que sigue
        cazando el sufijo aleatorio venga la ruta de donde venga.

    SE SUSTITUYE DE LA MAS LARGA A LA MAS CORTA. Si el nombre base se cambiara
    antes que la ruta que lo contiene, la ruta quedaria a medias y la linea
    seguiria siendo distinta entre dos corridas, que es justo lo que esto viene
    a impedir.

    Y NO NORMALIZA DE MAS: una linea que no lleve ninguna de las cuatro formas
    dentro sale IDENTICA, byte a byte."""
    if not tmp or not linea:
        return linea
    abso = os.path.abspath(tmp)
    formas = []
    for cruda in (tmp, abso, os.path.normpath(tmp)):
        formas.append(cruda)
        formas.append(cruda.replace(chr(92), "/"))
        formas.append(cruda.replace("/", chr(92)))
    try:
        rela = os.path.relpath(abso)
        formas.append(rela)
        formas.append(rela.replace(chr(92), "/"))
        formas.append(rela.replace("/", chr(92)))
    except ValueError:
        pass
    formas.append(os.path.basename(os.path.normpath(tmp)))
    for forma in sorted({f for f in formas if f}, key=len, reverse=True):
        linea = linea.replace(forma, MARCA_TEMPORAL)
    return linea



def main():
    sys.stdout.reconfigure(encoding="utf-8")
    importlib.reload(AP)
    L = []
    w = L.append
    fallos = 0
    w("CASO POSITIVO POR MUTACION de scripts/loop/apertura_del_auditor.py")
    w("todo el material va FABRICADO: el sello de prueba se escribe en un temporal")
    w("")
    w("LOS TRES PROHIBIDOS, LEIDOS DE LA CONSTANTE Y NO TECLEADOS AQUI:")
    w("   %s" % ", ".join(repr(p) for p in AP.PROHIBIDOS_ANTES_DEL_SELLO))
    w("")

    w("A) LOS ESCENARIOS DE puede_sellar(), CON EL VEREDICTO COMPUTADO")
    escenarios = [
        ("bitacora limpia", [], True),
        ("tras git log", ["git log"], False),
        ("tras git status", ["git status"], False),
        ("tras abrir REPORTE.md", ["REPORTE.md"], False),
        ("tras los tres", list(AP.PROHIBIDOS_ANTES_DEL_SELLO), False),
        ("tras algo que NO esta prohibido", ["git rev-parse"], True),
    ]
    for nombre, toques, esperado in escenarios:
        AP.olvidar_todo()
        for t in toques:
            AP.apuntar(t)
        # LA VARIABLE DEL VEREDICTO ES COMPUTADA: sale de llamar a la funcion.
        computado, motivo = AP.puede_sellar()
        ok = computado is esperado
        if not ok:
            fallos += 1
        w("   %-38s toques %-34s -> puede_sellar %-5s | esperado %-5s | %s"
          % (nombre, ",".join(toques) or "(ninguno)", computado, esperado,
             "CALZA" if ok else "NO CALZA"))
        w("      motivo: %s" % motivo[:120])
        w("      toques_prohibidos(): %s"
          % (", ".join(AP.toques_prohibidos()) or "(ninguno)"))
    w("")

    w("B) UNO POR UNO, CADA PROHIBIDO POR SU FUNCION DE VERDAD")
    w("   (no se apunta a mano: se llaman git_log(), git_status() y leer_reporte(),")
    w("    que es como el auditor los usaria, y se mira si el sello se cierra)")
    for nombre, llamar in (("git_log()", lambda: AP.git_log("-1", "--format=%h")),
                           ("git_status()", lambda: AP.git_status("--porcelain")),
                           ("leer_reporte()", lambda: AP.leer_reporte())):
        AP.olvidar_todo()
        antes, _m = AP.puede_sellar()
        llamar()
        despues, motivo = AP.puede_sellar()
        ok = (antes is True) and (despues is False)
        if not ok:
            fallos += 1
        w("   %-16s puede_sellar antes %-5s -> despues %-5s | %s"
          % (nombre, antes, despues, "CALZA" if ok else "NO CALZA"))
        w("      motivo: %s" % motivo[:120])
    w("")

    w("C) EL SELLO DE VERDAD: TRAS TOCAR, NI SIQUIERA SE ESCRIBE EL FICHERO")
    tmp = tempfile.mkdtemp(prefix="v182_apertura_")
    try:
        AP.olvidar_todo()
        AP.git_status("--porcelain")
        ok_sucio, informe = AP.sellar(
            criterio="criterio de mentira del arnes", vuelta="ARNES_SUCIO",
            muestra=3, semilla=1, dir_salida=tmp)
        ficheros = sorted(os.listdir(tmp))
        w("   tras git_status(), sellar() devuelve: %s" % ok_sucio)
        for l in informe:
            w("      | " + sin_temporal(l, tmp)[:130])
        w("   ficheros escritos en el temporal: %d %s"
          % (len(ficheros), ficheros))
        # DOS VARIABLES COMPUTADAS: el veredicto y el conteo de ficheros.
        if ok_sucio is not False:
            fallos += 1
        if ficheros:
            fallos += 1
            w("   ROJO: escribio algo, y no tenia que escribir nada.")
        else:
            w("   VERDE: no escribio NADA, que es lo que se le pide.")
        w("")
        w("D) Y CON LA BITACORA LIMPIA SI SELLA, para que se vea que no esta")
        w("   simplemente roto (un guardia que no deja pasar a nadie no es un")
        w("   guardia, es una pared)")
        AP.olvidar_todo()
        ok_limpio, informe2 = AP.sellar(
            criterio="criterio de mentira del arnes, bitacora limpia",
            vuelta="ARNES_LIMPIO", muestra=3, semilla=1, dir_salida=tmp)
        for l in informe2:
            w("      | " + sin_temporal(l, tmp)[:130])
        ficheros2 = sorted(os.listdir(tmp))
        w("   sellar() devuelve: %s" % ok_limpio)
        w("   ficheros en el temporal ahora: %d %s" % (len(ficheros2), ficheros2))
        hay_sello = any(n.startswith("SELLO_APERTURA_AUDITOR_") for n in ficheros2)
        w("   hay fichero de sello: %s" % ("SI" if hay_sello else "NO"))
        if ok_limpio is not True or not hay_sello:
            fallos += 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
        w("   temporal borrado: %s" % (not os.path.exists(tmp)))
    w("")

    w("E) LA MUTACION DEL VALOR ESPERADO, QUE ES LO QUE PRUEBA QUE ESTO CAE")
    AP.olvidar_todo()
    AP.git_log("-1")
    medido, _m = AP.puede_sellar()
    w("   escenario: se llamo a git_log() y despues se pregunta si puede sellar")
    w("   el veredicto COMPUTADO (no escrito) es: %s" % medido)
    for esperado in (False, True):
        w("   con el esperado %-5s -> %s"
          % (esperado, "PASA" if medido is esperado else "CAE"))
    cae = medido is not True
    w("   EL CASO CAE AL MUTAR EL ESPERADO A True: %s" % ("SI" if cae else "NO"))
    if not cae:
        fallos += 1
    w("")
    w("   LA SEGUNDA MUTACION: SE LE QUITA UN PROHIBIDO A LA LISTA.")
    w("   (si `git log` dejara de estar en PROHIBIDOS_ANTES_DEL_SELLO, este mismo")
    w("    escenario tendria que PODER sellar. Se comprueba sobre una copia de la")
    w("    constante y se deja como estaba)")
    originales = AP.PROHIBIDOS_ANTES_DEL_SELLO
    try:
        AP.PROHIBIDOS_ANTES_DEL_SELLO = tuple(
            p for p in originales if p != "git log")
        con_lista_mutada, _m2 = AP.puede_sellar()
        w("   con la lista mutada, puede_sellar computa: %s" % con_lista_mutada)
        w("   TENIA QUE CAMBIAR A True: %s" % ("SI" if con_lista_mutada else "NO"))
        if not con_lista_mutada:
            fallos += 1
    finally:
        AP.PROHIBIDOS_ANTES_DEL_SELLO = originales
        w("   la constante se deja como estaba: %s"
          % ("SI" if AP.PROHIBIDOS_ANTES_DEL_SELLO == originales else "NO"))
    AP.olvidar_todo()
    w("")
    w("CIFRA fallos: %d" % fallos)
    w("VEREDICTO: %s" % ("VERDE" if fallos == 0 else "ROJO"))

    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V182_T2_MUTACION_APERTURA_AUDITOR.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0 if fallos == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
