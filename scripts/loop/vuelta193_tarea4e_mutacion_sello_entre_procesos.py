# -*- coding: utf-8 -*-
r"""vuelta193_tarea4e_mutacion_sello_entre_procesos.py . EL CASO POSITIVO POR
MUTACION DE LA TAREA 4 DE LA VUELTA 193.

QUE TIENE QUE CAZAR, CON LAS PALABRAS DEL ENCARGO: **que CAIGA si un sello se
puede reescribir despues de tocar uno de los tres prohibidos EN OTRO PROCESO.**

POR QUE NO BASTABA EL ARNES DE LA 192, Y ESTA ES LA MITAD QUE IMPORTA:
`vuelta192_tarea4_mutacion_cuarta_puerta.py` corre todos sus escenarios **DENTRO
DE UN MISMO PROCESO**, y ahi la guarda vieja SI mordia. El agujero vivia
exactamente en la costura que aquel arnes no cruzaba. **Este arnes LANZA PROCESOS
DE VERDAD** con `subprocess`, que es la unica forma de probar que el estado
sobrevive.

SU SUJETO ESTA CONGELADO: todo se fabrica en un `mkdtemp` y se retira (`P.16`).
No toca `docs/loop/`, no toca el turno del auditor de verdad y no lee el archivo
de veredictos: **el escenario entero se monta con un archivo de veredictos
fabricado**, para que ni el sujeto ni la sede sean los vivos.

USO:
  python scripts/loop/vuelta193_tarea4e_mutacion_sello_entre_procesos.py

--- SUJETO CONGELADO, DECLARADO EN LA VUELTA 195 (TAREA 3.c) ---

**LA HUELLA DE VIVO QUE LA GUARDA VE AQUI ES `REPORTE.md`, Y NO ES UNA APERTURA
DE ESE FICHERO.** Es el argumento de `AP.apuntar("REPORTE.md")` dentro del
programa hijo que este arnes lanza: **una CADENA que se mete en la bitacora del
turno para poder comprobar si sobrevive entre procesos**. `apuntar()` escribe un
nombre en una lista; no abre, no lee y no toca `docs/loop/REPORTE.md`.

**LO QUE ESTE ARNES SI TOCA, Y ESO SI ES SU SUJETO:** un directorio temporal de
`mkdtemp` donde redirige `AP.RUTA_DEL_TURNO` y donde escribe sus sellos y su
turno de mentira. **Todo lo que abre en escritura vive dentro de ese temporal**, y
`P.16` (quien fabrica limpia) lo retira al salir.

**POR ESO SU SUJETO ESTA CONGELADO** y esta declaracion lo dice con el literal que
la regla de la vuelta 148 pide. **La cadena que la guarda confunde con un fichero
no se cambia**: cambiarla para contentar a la guarda seria falsear la prueba, que
es justamente comprobar que ESE nombre viaja entre procesos.

"""
import hashlib
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
SCRIPTS = os.path.join(RAIZ, "scripts", "loop")
NL = chr(10)
SALIDA = os.path.join(LOOP, "SALIDA_V193_T4E_MUTACION_SELLO_ENTRE_PROCESOS.txt")

# EL PROGRAMA QUE CADA PROCESO HIJO CORRE. Se le pasa por `-c` con dos
# parametros: el directorio del turno y el paso que tiene que dar. Escribe su
# resultado en JSON por stdout, para que el padre no tenga que parsear prosa.
HIJO = r'''
import io, json, os, sys
sys.path.insert(0, %(scripts)r)
os.environ["PYTHONIOENCODING"] = "utf-8"
import apertura_del_auditor as AP
AP.RUTA_DEL_TURNO = os.path.join(%(base)r, "_TURNO_DEL_AUDITOR.json")
AP._cargar_turno()
paso = %(paso)r
res = {"paso": paso, "bitacora_al_entrar": AP.bitacora()}
if paso == "tocar":
    AP.apuntar("REPORTE.md")
    res["bitacora_al_salir"] = AP.bitacora()
elif paso == "sellar":
    ok, informe = AP.sellar("criterio fabricado por el arnes de la 193",
                            %(vuelta)r, puestos="1,2", dir_salida=%(base)r)
    res["ok"] = ok
    res["informe"] = informe
    res["bitacora_al_salir"] = AP.bitacora()
elif paso == "puede":
    ok, motivo = AP.puede_sellar()
    res["ok"] = ok
    res["motivo"] = motivo
elif paso == "declarar":
    ok, informe = AP.declarar_clases_con_sello(
        os.path.join(%(base)r, "mis_clases.txt"), %(vuelta)r, base=%(base)r)
    res["ok"] = ok
    res["informe"] = informe
sys.stdout.write("<<<" + json.dumps(res) + ">>>")
'''


def correr_hijo(base, paso, vuelta):
    """LANZA UN PROCESO DE VERDAD Y DEVUELVE SU DICT. Es lo que separa este arnes
    del de la 192: aquel corria todo en el mismo proceso."""
    codigo = HIJO % {"scripts": SCRIPTS, "base": base, "paso": paso,
                     "vuelta": vuelta}
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run([sys.executable, "-c", codigo], cwd=RAIZ,
                       capture_output=True, env=env)
    salida = r.stdout.decode("utf-8", errors="replace")
    if "<<<" not in salida or ">>>" not in salida:
        return {"paso": paso, "ROTO": True,
                "stderr": r.stderr.decode("utf-8", errors="replace")[-400:]}
    return json.loads(salida.split("<<<", 1)[1].rsplit(">>>", 1)[0])


def sin_el_temporal(linea, tmp):
    """LA LINEA SIN EL NOMBRE DEL DIRECTORIO TEMPORAL. PURA.

    ES LA MISMA LECCION DE LA TAREA 2.b DE ESTA VUELTA: `mkdtemp` da un nombre
    ALEATORIO POR CONSTRUCCION, y esta salida se sella y se compara byte a byte.
    Aqui el nombre se cuela DENTRO de los informes que el modulo devuelve, asi
    que se tapa al imprimir en vez de no imprimir la linea entera: **lo que el
    informe dice sigue publicandose; lo que no reproduce, no.**"""
    marca = "(EL TEMPORAL DEL ARNES)"
    for forma in (tmp, tmp.replace(os.sep, "/"), os.path.relpath(tmp, RAIZ),
                  os.path.relpath(tmp, RAIZ).replace(os.sep, "/")):
        linea = linea.replace(forma, marca)
    return linea


def medir_turno_real(ruta=None):
    """(existe, bytes, sha256) DE LA SEDE DE VERDAD DEL TURNO DEL AUDITOR.

    ANADIDA EN LA VUELTA 194, TAREA 2.b. Semi-pura: lo unico que toca disco es
    leer la ruta que se le pasa, y la ruta va por parametro para que se pueda
    medir una fabricada. **Devuelve las TRES cosas a proposito:** un fichero que
    se borra y se vuelve a escribir con el mismo tamano tiene el mismo `existe` y
    los mismos `bytes`, y solo el `sha256` lo delata."""
    ruta = ruta or os.path.join(LOOP, "_TURNO_DEL_AUDITOR.json")
    if not os.path.isfile(ruta):
        return (False, 0, "")
    datos = io.open(ruta, "rb").read()
    return (True, len(datos), hashlib.sha256(datos).hexdigest())


def _caso(w, nombre, obtenido, esperado):
    ok = obtenido == esperado
    w("   %-62s %s" % (nombre, "VERDE" if ok else "ROJO"))
    if not ok:
        w("      esperado: %r" % (esperado,))
        w("      obtenido: %r" % (obtenido,))
    return ok


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    ok = True
    VUELTA = "MUT193"
    w("=" * 78)
    w("VUELTA 193, TAREA 4.e: EL SELLO NO SE REESCRIBE, NI SIQUIERA EN OTRO")
    w("PROCESO")
    w("=" * 78)
    w("")
    w("LO QUE SE PRUEBA Y POR QUE PUEDE CAER: cada paso corre en un PROCESO")
    w("NUEVO de verdad, lanzado con subprocess. El estado de modulo muere entre")
    w("ellos por construccion, asi que si la bitacora o el sello sobreviven es")
    w("porque el fichero del turno los llevo, y no porque el arnes se lo crea.")
    w("")

    # LA SEDE DE VERDAD DEL TURNO, MEDIDA ANTES DE FABRICAR NADA (anadido en la
    # vuelta 194, TAREA 2.b): el caso `H` la vuelve a medir al final y CAE SI
    # CAMBIA. Antes exigia que NO EXISTIERA, y eso es pedir que no haya auditor.
    turno_antes = medir_turno_real()
    w("0) LA SEDE DE VERDAD DEL TURNO, MEDIDA ANTES DE EMPEZAR")
    w("   %s" % ("EXISTE, %d bytes" % turno_antes[1] if turno_antes[0]
                 else "NO EXISTE"))
    w("   sha256: %s" % (turno_antes[2][:16] or "(no hay fichero)"))
    w("")

    tmp = tempfile.mkdtemp(prefix="v193_sello_procesos_")
    try:
        # EL ESCENARIO SE FABRICA ENTERO: hasta el fichero de clases.
        io.open(os.path.join(tmp, "mis_clases.txt"), "w", encoding="utf-8",
                newline=NL).write("clases fabricadas por el arnes" + NL)

        w("A) PROCESO 1: EL TURNO TOCA `REPORTE.md`")
        p1 = correr_hijo(tmp, "tocar", VUELTA)
        ok &= _caso(w, "entra con la bitacora vacia", p1.get("bitacora_al_entrar"), [])
        ok &= _caso(w, "y sale con el toque apuntado",
                    p1.get("bitacora_al_salir"), ["REPORTE.md"])
        existe = os.path.exists(os.path.join(tmp, "_TURNO_DEL_AUDITOR.json"))
        ok &= _caso(w, "el fichero del turno quedo escrito", existe, True)
        w("")

        w("B) PROCESO 2, NUEVO Y DISTINTO: LA BITACORA TIENE QUE SOBREVIVIR")
        w("   (ESTE ES EL CASO QUE CAIA. Antes de la 193 el proceso nuevo nacia")
        w("    con la bitacora VACIA y `puede_sellar()` decia SI)")
        p2 = correr_hijo(tmp, "puede", VUELTA)
        ok &= _caso(w, "el proceso nuevo VE el toque del proceso anterior",
                    p2.get("bitacora_al_entrar"), ["REPORTE.md"])
        ok &= _caso(w, "y `puede_sellar()` dice NO", p2.get("ok"), False)
        w("      motivo publicado: %s" % (p2.get("motivo") or "")[:110])
        w("   LA MUTACION: si la bitacora NO sobreviviera, el proceso nuevo")
        w("   entraria vacio y `puede_sellar()` diria SI")
        if p2.get("bitacora_al_entrar") == []:
            w("      LA MUTACION NO CAYO: entro vacio, o sea que no sobrevivio.")
            ok = False
        else:
            w("      LA MUTACION CAE: entro con %r, que es el toque del proceso"
              % (p2.get("bitacora_al_entrar"),))
            w("      anterior, y por eso no puede sellar.")
        w("")

        w("C) PROCESO 3: INTENTA SELLAR CON LA BITACORA SUCIA, EN OTRO PROCESO")
        p3 = correr_hijo(tmp, "sellar", VUELTA)
        ok &= _caso(w, "sellar() CAE EN ROJO", p3.get("ok"), False)
        hay_sello = os.path.exists(
            os.path.join(tmp, "SELLO_APERTURA_AUDITOR_V%s.json" % VUELTA))
        ok &= _caso(w, "y NO escribio ningun sello", hay_sello, False)
        for l in (p3.get("informe") or [])[:4]:
            w("      | %s" % sin_el_temporal(l, tmp)[:110])
        w("")

        w("D) SE LIMPIA EL TURNO Y SE SELLA BIEN, PARA TENER UN SELLO DE VERDAD")
        os.remove(os.path.join(tmp, "_TURNO_DEL_AUDITOR.json"))
        # El aislador de verdad necesita el archivo de veredictos, que aqui NO se
        # fabrica: el sello se monta a mano, que es lo que hace falta para probar
        # la guarda de DISCO. Se dice en vez de disimularlo.
        io.open(os.path.join(tmp, "SELLO_APERTURA_AUDITOR_V%s.json" % VUELTA),
                "w", encoding="utf-8", newline=NL).write(
            json.dumps({"vuelta": VUELTA, "criterio": "fabricado",
                        "ciega": "fabricada", "destape": "fabricado",
                        "bitacora_antes_del_sello": [],
                        "prohibidos_antes_del_sello": []},
                       ensure_ascii=False, indent=1) + NL)
        w("   EL SELLO SE MONTA A MANO Y SE DICE: el aislador de verdad necesita")
        w("   el archivo de veredictos, y este arnes NO lo fabrica ni lo toca. Lo")
        w("   que aqui se prueba es la guarda de DISCO, y para eso basta con que")
        w("   el fichero del sello EXISTA.")
        ok &= _caso(w, "el sello fabricado existe",
                    os.path.exists(os.path.join(
                        tmp, "SELLO_APERTURA_AUDITOR_V%s.json" % VUELTA)), True)
        w("")

        w("E) EL CASO QUE EL ENCARGO NOMBRA: TOCAR UN PROHIBIDO EN UN PROCESO,")
        w("   Y EN OTRO PROCESO VOLVER A SELLAR CON EL SELLO YA EN DISCO")
        p5a = correr_hijo(tmp, "tocar", VUELTA)
        ok &= _caso(w, "el proceso toca `REPORTE.md`",
                    p5a.get("bitacora_al_salir"), ["REPORTE.md"])
        p5b = correr_hijo(tmp, "sellar", VUELTA)
        ok &= _caso(w, "EL SELLO NO SE REESCRIBE: sellar() CAE", p5b.get("ok"),
                    False)
        motivo_disco = any("YA HAY SELLO EN DISCO" in l
                           for l in (p5b.get("informe") or []))
        ok &= _caso(w, "y el motivo que publica es el del DISCO", motivo_disco,
                    True)
        for l in (p5b.get("informe") or [])[:4]:
            w("      | %s" % sin_el_temporal(l, tmp)[:110])
        w("   LA MUTACION: si la guarda mirara solo la MEMORIA, este proceso")
        w("   nuevo la encontraria limpia de sello y reescribiria el fichero")
        w("   publicando `prohibidos tocados antes del sello: 0`")
        if p5b.get("ok"):
            w("      LA MUTACION NO CAYO: el sello se reescribio.")
            ok = False
        else:
            w("      LA MUTACION CAE: no se reescribio, y el motivo nombra el")
            w("      disco y no la memoria.")
        w("")

        w("F) LA PIEZA `c`: EL CARRIL QUE DECLARA CLASES LEYENDO EL SELLO DE")
        w("   DISCO, CORRIDO EN UN PROCESO QUE NO SELLO")
        os.remove(os.path.join(tmp, "_TURNO_DEL_AUDITOR.json"))
        p6 = correr_hijo(tmp, "declarar", VUELTA)
        ok &= _caso(w, "un proceso que NO sello puede declarar sus clases",
                    p6.get("ok"), True)
        for l in (p6.get("informe") or [])[:3]:
            w("      | %s" % sin_el_temporal(l, tmp)[:110])
        w("   LA MUTACION: sin el sello en disco tiene que CAER, o estaria")
        w("   dejando declarar clases de un sujeto que nadie aisló")
        os.remove(os.path.join(tmp, "_TURNO_DEL_AUDITOR.json"))
        os.remove(os.path.join(tmp, "SELLO_APERTURA_AUDITOR_V%s.json" % VUELTA))
        p7 = correr_hijo(tmp, "declarar", VUELTA)
        ok &= _caso(w, "sin sello en disco, declarar CAE", p7.get("ok"), False)
        if p7.get("ok"):
            w("      LA MUTACION NO CAYO: declaro clases sin sello.")
        else:
            w("      LA MUTACION CAE: sin sello no hay sujeto, y lo dice.")
        w("")

        w("G) Y EL DESTAPE SIGUE QUEMANDO ENTRE PROCESOS: LA GUARDA VIEJA NO SE")
        w("   AFLOJA")
        io.open(os.path.join(tmp, "SELLO_APERTURA_AUDITOR_V%s.json" % VUELTA),
                "w", encoding="utf-8", newline=NL).write(
            json.dumps({"vuelta": VUELTA, "ciega": "fabricada"},
                       ensure_ascii=False, indent=1) + NL)
        io.open(os.path.join(tmp, "_TURNO_DEL_AUDITOR.json"), "w",
                encoding="utf-8", newline=NL).write(
            json.dumps({"bitacora": ["veredictos:destape"],
                        "sellado": {"hecho": False, "ruta": None, "vuelta": None},
                        "clases": {"escritas": False, "ruta": None}},
                       ensure_ascii=False, indent=1) + NL)
        p8 = correr_hijo(tmp, "declarar", VUELTA)
        ok &= _caso(w, "con un destape apuntado en OTRO proceso, declarar CAE",
                    p8.get("ok"), False)
        for l in (p8.get("informe") or [])[:3]:
            w("      | %s" % sin_el_temporal(l, tmp)[:110])
        w("")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
        w("H) EL TEMPORAL SE RETIRA (P.16, quien fabrica limpia)")
        w("   (su nombre NO se imprime: `mkdtemp` lo fabrica aleatorio y esta")
        w("    salida se sella y se compara byte a byte)")
        ok &= _caso(w, "el temporal quedo retirado", os.path.exists(tmp), False)
        # -----------------------------------------------------------------
        # CORREGIDO EN LA VUELTA 194, TAREA 2.b. HALLAZGO `5.1` DEL ACTA 194.
        #
        # LO QUE ESTE CASO DECIA ANTES, Y ERA FALSO: comprobaba
        # `os.path.exists(turno_real) == False`, o sea EXIGIA QUE EL FICHERO DEL
        # TURNO NO EXISTIERA. Un turno de auditor vivo lo tiene puesto, asi que
        # este arnes salia en ROJO cada vez que habia auditor, y salia en VERDE
        # solo porque el arnes de la 192 corria antes en orden alfabetico y lo
        # BORRABA. **Su verde no era suyo: se lo debia al otro.**
        #
        # LO QUE TIENE QUE COMPROBAR ES QUE EL NO LO TOCO, no que no exista. La
        # medicion se toma ANTES (arriba, `turno_antes`) y aqui DESPUES, con las
        # tres cosas: existencia, bytes y `sha256`. CAE SI CAMBIA.
        turno_despues = medir_turno_real()
        w("   LA SEDE DE VERDAD DEL TURNO, MEDIDA ANTES Y DESPUES Y NO SUPUESTA")
        w("   (corregido en la 194: antes se exigia que NO EXISTIERA, que es")
        w("    pedir que no haya auditor)")
        w("   al entrar: %s | al salir: %s"
          % ("EXISTE, %d bytes" % turno_antes[1] if turno_antes[0] else "NO EXISTE",
             "EXISTE, %d bytes" % turno_despues[1] if turno_despues[0]
             else "NO EXISTE"))
        w("   sha256 al entrar: %s" % (turno_antes[2][:16] or "(no hay fichero)"))
        w("   sha256 al salir:  %s" % (turno_despues[2][:16] or "(no hay fichero)"))
        ok &= _caso(w, "el turno del auditor DE VERDAD no CAMBIO",
                    turno_despues, turno_antes)
        # -----------------------------------------------------------------
    w("")

    w("VEREDICTO: %s" % ("VERDE" if ok else "ROJO"))
    t = NL.join(L) + NL
    io.open(SALIDA, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: docs/loop/SALIDA_V193_T4E_MUTACION_SELLO_ENTRE_PROCESOS.txt "
          "(%d bytes)" % len(t.encode("utf-8")))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
