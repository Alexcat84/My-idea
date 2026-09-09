# -*- coding: utf-8 -*-
r"""vuelta197_tarea2_mutacion_orden_del_turno.py . EL CASO POSITIVO POR MUTACION
DE LAS TRES PIEZAS QUE LA TAREA 2 DE LA VUELTA 197 ANADE A
`scripts/loop/apertura_del_auditor.py`.

LAS TRES, Y DE DONDE SALE CADA UNA:

  A. `puede_leer_reporte()` Y `leer_reporte()` QUE CAE EN ROJO. Adjudicacion
     `4.5` del acta 197, por extension de `AUDITOR.md` 1.2. **La tabla de
     discrepancias de un reporte ES un destape**, y esta MEDIDO: el reporte de la
     196 publico la clase de archivo de 8 de los 120 puestos que el auditor de la
     197 acababa de sellar. El orden pasa a ser
     `sellar()` -> clasificar -> `--declarar-clases` -> `leer_reporte()`.
     **Un turno SIN sello sigue pudiendo leer el reporte**, y eso se prueba aqui.

  B. `cerrar_turno()`. Hallazgo `5.4` del acta 197: el fichero del turno NO se
     limpia al cerrar, el auditor siguiente lo hereda sucio, y **tiene que
     borrarlo para poder sellar**. Se prueba EN PROCESOS DE VERDAD, porque el
     agujero es entre procesos y en uno solo no se ve.

  C. `guarda_del_marcador()`. Caida `C.A1` del auditor, **TERCERA acta seguida de
     la misma especie** (195, 196 y 197): recontar el marcador con `json` a mano
     en vez de por `AP.marcador()`. El remedio de memoria ya fallo una vez.

SUJETO CONGELADO (declarado en la auditoria integral, 9 sep 2026, al entrar en la
nomina de la bateria): todo lo que este arnes lee lo fabrica en un temporal
(`mkdtemp`, `REPORTE_FABRICADO.md`); la cadena `REPORTE.md` aparece aqui solo
como LITERAL dentro de las bitacoras fabricadas que se comparan, y este arnes
NO abre el REPORTE.md vivo. La guarda de sujeto congelado de la bateria veia las
dos huellas y lo dejaba NO DECIDIBLE; esta declaracion es el remedio que la
propia guarda pide.

EL CASO ROJO TIENE QUE MORDER, Y AQUI SE PRUEBA LAS DOS DIRECCIONES: de cada
pieza se comprueba que **SIN el remedio la guarda deja pasar** y **CON el no**.
`EJECUTOR.md` 1, EL CASO ROJO SE PRUEBA POR MUTACION. **Ningun veredicto es una
constante literal**: todos salen de llamar a la funcion.

TODO SOBRE UN TEMPORAL: `AP.RUTA_DEL_TURNO` se redirige, los sellos y las clases
se fabrican dentro, y el temporal se retira al final (P.16, quien fabrica limpia).
**LA SEDE DE VERDAD DEL TURNO SE MIDE ANTES Y DESPUES Y EL ARNES CAE SI CAMBIA**,
que es la leccion que la TAREA 2.b de la vuelta 194 dejo escrita.

USO:
  python scripts/loop/vuelta197_tarea2_mutacion_orden_del_turno.py
"""
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import apertura_del_auditor as AP   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
SCRIPTS = os.path.join(RAIZ, "scripts", "loop")
NL = chr(10)
SALIDA = os.path.join(LOOP, "SALIDA_V197_T2_MUTACION_ORDEN_DEL_TURNO.txt")

VUELTA = "MUT197"

# EL PROGRAMA QUE CADA PROCESO HIJO CORRE, con el mismo molde que el arnes de la
# vuelta 193: se le pasa el directorio del turno y el paso, y devuelve JSON.
HIJO = r'''
import io, json, os, sys
sys.path.insert(0, %(scripts)r)
os.environ["PYTHONIOENCODING"] = "utf-8"
import apertura_del_auditor as AP
AP.RUTA_DEL_TURNO = os.path.join(%(base)r, "_TURNO_DEL_AUDITOR.json")
AP._cargar_turno()
paso = %(paso)r
res = {"paso": paso, "bitacora_al_entrar": AP.bitacora(),
       "cerrados_al_entrar": sorted(AP.cerrados())}
if paso == "ensuciar":
    AP.apuntar("git log")
    AP.apuntar("git status")
    AP.apuntar("REPORTE.md")
    res["bitacora_al_salir"] = AP.bitacora()
elif paso == "puede_sellar":
    ok, motivo = AP.puede_sellar()
    res["ok"] = ok
    res["motivo"] = motivo
elif paso == "declarar":
    ok, informe = AP.declarar_clases_con_sello(
        os.path.join(%(base)r, "mis_clases.txt"), %(vuelta)r, base=%(base)r)
    res["ok"] = ok
    res["informe"] = informe
elif paso == "leer_reporte":
    try:
        texto = AP.leer_reporte(ruta=os.path.join(%(base)r, "REPORTE_FABRICADO.md"),
                                vuelta=%(vuelta)r, base=%(base)r)
        res["ok"] = True
        res["texto"] = texto.strip()
    except AP.ReporteFueraDeOrden as e:
        res["ok"] = False
        res["motivo"] = str(e)
sys.stdout.write("<<<" + json.dumps(res) + ">>>")
'''


def correr_hijo(base, paso, vuelta=VUELTA):
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


def medir_turno_real(ruta=None):
    """(existe, bytes, sha256) DE LA SEDE DE VERDAD DEL TURNO DEL AUDITOR."""
    ruta = ruta or os.path.join(LOOP, "_TURNO_DEL_AUDITOR.json")
    if not os.path.isfile(ruta):
        return (False, 0, "")
    datos = io.open(ruta, "rb").read()
    return (True, len(datos), hashlib.sha256(datos).hexdigest())


_CUENTA = {"casos": 0, "pasan": 0}


def _caso(w, nombre, obtenido, esperado):
    ok = obtenido == esperado
    _CUENTA["casos"] += 1
    _CUENTA["pasan"] += 1 if ok else 0
    w("   %-64s %s" % (nombre, "VERDE" if ok else "ROJO"))
    if not ok:
        w("      esperado: %r" % (esperado,))
        w("      obtenido: %r" % (obtenido,))
    return ok


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    ok = True
    w("=" * 78)
    w("VUELTA 197, TAREA 2: CASO POSITIVO POR MUTACION DEL ORDEN DEL TURNO")
    w("=" * 78)
    w("")
    turno_antes = medir_turno_real()
    w("0) LA SEDE DE VERDAD DEL TURNO, MEDIDA ANTES DE FABRICAR NADA")
    w("   %s | sha256 %s"
      % ("EXISTE, %d bytes" % turno_antes[1] if turno_antes[0] else "NO EXISTE",
         turno_antes[2][:16] or "(no hay fichero)"))
    w("")

    tmp = tempfile.mkdtemp(prefix="v197_orden_turno_")
    ruta_original = AP.RUTA_DEL_TURNO
    loop_original = AP.LOOP
    try:
        AP.RUTA_DEL_TURNO = os.path.join(tmp, "_TURNO_DEL_AUDITOR.json")
        # EL SANDBOX SE COMPLETA EN LA VUELTA 199, TAREA 1.b, Y SE DECLARA.
        # Este arnes prometia en su docstring *"TODO SOBRE UN TEMPORAL"*, y era
        # verdad a medias: `AP.LOOP` seguia apuntando a `docs/loop/` de verdad.
        # Mientras `puede_leer_reporte()` solo mirara el disco CON `vuelta`, eso
        # no se notaba. Desde que la 199 la hace mirar el disco TAMBIEN SIN
        # `vuelta`, una llamada a secas dentro de este arnes leia los sellos
        # REALES de la sede. Se redirige, y con eso la promesa del docstring pasa
        # a ser cierta.
        AP.LOOP = tmp
        ok &= _caso(w, "AP.RUTA_DEL_TURNO ya NO apunta a la sede de verdad",
                    AP.RUTA_DEL_TURNO == ruta_original, False)
        ok &= _caso(w, "y AP.LOOP tampoco apunta a docs/loop de verdad",
                    AP.LOOP == loop_original, False)
        vacio = os.path.join(tmp, "sin_sellos")
        os.makedirs(vacio)
        io.open(os.path.join(tmp, "mis_clases.txt"), "w", encoding="utf-8",
                newline=NL).write("clases fabricadas por el arnes" + NL)
        io.open(os.path.join(tmp, "REPORTE_FABRICADO.md"), "w", encoding="utf-8",
                newline=NL).write("el reporte fabricado" + NL)
        sello = os.path.join(tmp, "SELLO_APERTURA_AUDITOR_V%s.json" % VUELTA)
        io.open(sello, "w", encoding="utf-8", newline=NL).write(
            json.dumps({"vuelta": VUELTA, "ciega": "fabricada"},
                       ensure_ascii=False, indent=1) + NL)

        # ---------------------------------------------------------------- A
        w("A) `puede_leer_reporte()`: LOS TRES ESTADOS DEL TURNO, UNO POR UNO")
        w("   (la variable del veredicto es COMPUTADA: sale de llamar a la")
        w("    funcion, nunca de una constante escrita al lado)")
        AP.olvidar_todo()
        # EL CASO ORIGINAL DE LA 197, CON SU PREMISA HECHA CIERTA. Decia
        # *"SIN sello: SI puede leer"*, y su premisa era que el turno no tuviera
        # sello. Desde la 199 *sin sello* significa SIN SELLO EN NINGUN SITIO, ni
        # en memoria ni en disco, asi que se mide contra un directorio SIN
        # SELLOS. **Es la mitad que impide que la guarda sea una pared**, y sigue
        # entera: lo que cambia es donde se mira, no lo que se espera.
        ok &= _caso(w, "SIN sello EN NINGUN SITIO: SI puede leer, y no se prohibe",
                    AP.puede_leer_reporte(base=vacio)[0], True)
        # Y EL CASO QUE LA VUELTA 199 HACE NACER, ANADIDO Y NO SUSTITUIDO: sin
        # sello en MEMORIA pero CON el sello EN DISCO, la guarda YA MUERDE. Antes
        # de la 199 esta misma llamada devolvia True, y por ahi se le escapo el
        # sujeto al auditor de la 198.
        ok &= _caso(w, "SIN sello en memoria pero CON sello EN DISCO: ya NO puede",
                    AP.puede_leer_reporte()[0], False)
        ok &= _caso(w, "y sin sello EN DISCO tampoco se prohibe",
                    AP.puede_leer_reporte(vuelta=VUELTA, base=tmp)[0], False)
        w("      OJO: la linea de arriba sale FALSE porque el sello de la vuelta")
        w("      %s SI existe en el temporal. Es el caso siguiente." % VUELTA)
        ok &= _caso(w, "con una vuelta SIN sello en disco, si puede",
                    AP.puede_leer_reporte(vuelta="NO_EXISTE", base=tmp)[0], True)
        AP._SELLADO["hecho"] = True
        AP._SELLADO["ruta"] = sello
        AP._SELLADO["vuelta"] = VUELTA
        ok &= _caso(w, "CON sello y SIN clases: NO puede. ESTE ES EL CASO NUEVO",
                    AP.puede_leer_reporte()[0], False)
        motivo = AP.puede_leer_reporte()[1]
        ok &= _caso(w, "y el motivo nombra la adjudicacion que lo manda",
                    "4.5 del acta 197" in motivo, True)
        cayo = None
        try:
            AP.leer_reporte(ruta=os.path.join(tmp, "REPORTE_FABRICADO.md"))
            cayo = False
        except AP.ReporteFueraDeOrden:
            cayo = True
        ok &= _caso(w, "leer_reporte() LEVANTA ReporteFueraDeOrden", cayo, True)
        ok &= _caso(w, "y el toque queda apuntado igual: el intento se registra",
                    AP.bitacora()[-1], "REPORTE.md")
        AP._CLASES["escritas"] = True
        AP._CLASES["ruta"] = os.path.join(tmp, "mis_clases.txt")
        ok &= _caso(w, "CON sello Y con clases: vuelve a poder",
                    AP.puede_leer_reporte()[0], True)
        ok &= _caso(w, "y leer_reporte() devuelve el texto de verdad",
                    AP.leer_reporte(
                        ruta=os.path.join(tmp, "REPORTE_FABRICADO.md")).strip(),
                    "el reporte fabricado")
        w("   LA MUTACION, Y SE CORRE EN LAS DOS DIRECCIONES: SIN el remedio,")
        w("   `leer_reporte()` era un `io.open` con su `apuntar()` delante y NADA")
        w("   MAS. Se reconstruye ese comportamiento y se mira que deja pasar el")
        w("   estado que ahora se prohibe.")
        AP.olvidar_todo()
        AP._SELLADO["hecho"] = True
        AP._SELLADO["vuelta"] = VUELTA
        sin_remedio = io.open(os.path.join(tmp, "REPORTE_FABRICADO.md"),
                              encoding="utf-8").read().strip()
        ok &= _caso(w, "SIN el remedio, el estado prohibido devuelve el texto",
                    sin_remedio, "el reporte fabricado")
        ok &= _caso(w, "CON el remedio, ese mismo estado NO puede",
                    AP.puede_leer_reporte()[0], False)
        w("")

        # ---------------------------------------------------------------- B
        w("B) `cerrar_turno()`, EN PROCESOS DE VERDAD, QUE ES DONDE VIVE EL")
        w("   HALLAZGO `5.4`. Cada paso es un `subprocess` nuevo: el estado de")
        w("   modulo muere entre ellos por construccion.")
        AP.olvidar_todo()
        p1 = correr_hijo(tmp, "ensuciar")
        ok &= _caso(w, "el turno 1 entra limpio", p1.get("bitacora_al_entrar"), [])
        ok &= _caso(w, "y sale con los TRES prohibidos apuntados",
                    p1.get("bitacora_al_salir"),
                    ["git log", "git status", "REPORTE.md"])
        p2 = correr_hijo(tmp, "puede_sellar")
        ok &= _caso(w, "EL AGUJERO `5.4`: el turno 2 hereda la bitacora sucia",
                    p2.get("bitacora_al_entrar"),
                    ["git log", "git status", "REPORTE.md"])
        ok &= _caso(w, "y NO puede sellar, que es lo que obligaba a borrar",
                    p2.get("ok"), False)
        w("      motivo publicado: %s" % (p2.get("motivo") or "")[:110])
        w("   AHORA SE CIERRA EL TURNO POR SU CARRIL, declarando las clases, Y")
        w("   NO SE BORRA NADA:")
        p3 = correr_hijo(tmp, "declarar")
        ok &= _caso(w, "declarar_clases_con_sello() sale VERDE", p3.get("ok"), True)
        cerro = any("TURNO CERRADO" in l for l in (p3.get("informe") or []))
        ok &= _caso(w, "y su informe dice que el turno queda CERRADO", cerro, True)
        existe = os.path.exists(os.path.join(tmp, "_TURNO_DEL_AUDITOR.json"))
        ok &= _caso(w, "EL FICHERO DEL TURNO SIGUE EXISTIENDO: cerrar no es borrar",
                    existe, True)
        ok &= _caso(w, "y el sello en disco tampoco se toco",
                    os.path.exists(sello), True)
        d = json.load(io.open(os.path.join(tmp, "_TURNO_DEL_AUDITOR.json"),
                              encoding="utf-8"))
        ok &= _caso(w, "el fichero guarda la constancia del cierre",
                    sorted(d.get("cerrados") or {}), [VUELTA])
        ok &= _caso(w, "con la bitacora del turno cerrado DENTRO, como prueba",
                    (d["cerrados"][VUELTA] or {}).get("bitacora"),
                    ["git log", "git status", "REPORTE.md"])
        ok &= _caso(w, "y el bloque vivo marcado como cerrado",
                    (d.get("vivo") or {}).get("abierto"), False)
        p4 = correr_hijo(tmp, "puede_sellar")
        ok &= _caso(w, "EL TURNO NUEVO ENTRA LIMPIO SIN QUE NADIE BORRE NADA",
                    p4.get("bitacora_al_entrar"), [])
        ok &= _caso(w, "y ya PUEDE sellar", p4.get("ok"), True)
        ok &= _caso(w, "y ve la constancia de la vuelta cerrada",
                    p4.get("cerrados_al_entrar"), [VUELTA])
        w("   LA GUARDA QUE NO SE PIERDE AL LIMPIAR: declarar dos veces la MISMA")
        w("   vuelta sigue cayendo, y ahora entre procesos.")
        p5 = correr_hijo(tmp, "declarar")
        ok &= _caso(w, "declarar otra vez la vuelta ya cerrada CAE", p5.get("ok"),
                    False)
        dice_cerrada = any("YA SE CERRO" in l for l in (p5.get("informe") or []))
        ok &= _caso(w, "y el motivo nombra el cierre, no una memoria perdida",
                    dice_cerrada, True)
        w("   LA MUTACION: se le devuelve al fichero el `vivo.abierto` verdadero,")
        w("   que es EXACTAMENTE el estado de antes del remedio, y se mira si el")
        w("   turno nuevo vuelve a heredar la suciedad.")
        d["vivo"] = {"abierto": True}
        d["bitacora"] = ["git log", "git status", "REPORTE.md"]
        io.open(os.path.join(tmp, "_TURNO_DEL_AUDITOR.json"), "w",
                encoding="utf-8", newline=NL).write(
            json.dumps(d, ensure_ascii=False, indent=1) + NL)
        p6 = correr_hijo(tmp, "puede_sellar")
        ok &= _caso(w, "SIN el cierre, el turno nuevo VUELVE a heredar la suciedad",
                    p6.get("bitacora_al_entrar"),
                    ["git log", "git status", "REPORTE.md"])
        ok &= _caso(w, "y VUELVE a no poder sellar. LA MUTACION MUERDE",
                    p6.get("ok"), False)
        w("")

        # ------------------------------------------------------- A, en procesos
        w("B.1) Y EL ORDEN DEL REPORTE TAMBIEN VALE ENTRE PROCESOS, que es la")
        w("     unica forma de que no se esquive arrancando otro")
        os.remove(os.path.join(tmp, "_TURNO_DEL_AUDITOR.json"))
        p7 = correr_hijo(tmp, "leer_reporte")
        ok &= _caso(w, "un proceso nuevo, con el sello EN DISCO y sin clases: CAE",
                    p7.get("ok"), False)
        w("      motivo publicado: %s" % (p7.get("motivo") or "")[:110])
        p8 = correr_hijo(tmp, "declarar")
        ok &= _caso(w, "declara sus clases en otro proceso: VERDE", p8.get("ok"),
                    True)
        p9 = correr_hijo(tmp, "leer_reporte")
        ok &= _caso(w, "y ahora SI, aunque el turno se cerro en medio",
                    p9.get("ok"), True)
        ok &= _caso(w, "y lee el texto de verdad", p9.get("texto"),
                    "el reporte fabricado")
        w("      NOTA MEDIDA: el turno se cerro al declarar, asi que el proceso")
        w("      de `leer_reporte` entra LIMPIO y sin sello en memoria. Puede")
        w("      leer por la primera puerta de la guarda (sin sello no hay sujeto")
        w("      que quemar), no por la tercera. SE DICE EN VEZ DE DISIMULARLO.")
        w("")

        # ---------------------------------------------------------------- C
        w("C) `guarda_del_marcador()`, LA GUARDA DE LA `C.A1`")
        acta_buena = ("| marcador, por `AP.marcador()` | **3388 filas; A 551, "
                      "B 72, C 5, D 2760**; 0 huecos | SI |")
        leido = AP.cifras_del_marcador_del_acta(acta_buena)
        ok &= _caso(w, "lee las filas y el reparto de la forma que usan las actas",
                    leido, {"filas": 3388,
                            "por_clase": {"A": 551, "B": 72, "C": 5, "D": 2760}})
        ok &= _caso(w, "un texto sin cifras de marcador devuelve None",
                    AP.cifras_del_marcador_del_acta("una linea cualquiera"), None)
        ok &= _caso(w, "SIN salida sellada de esa vuelta, la guarda CAE",
                    AP.guarda_del_marcador(acta_buena, VUELTA, base=tmp)[0], False)
        w("      ESE ES EL CASO QUE LA `C.A1` ES: un marcador publicado que nadie")
        w("      saco por `AP.marcador()`. No hay tercera via.")
        archivo = os.path.join(tmp, "veredictos_fabricados.jsonl")
        filas = ([{"puesto_intra": i, "clase": "A"} for i in range(551)]
                 + [{"puesto_intra": 1000 + i, "clase": "B"} for i in range(72)]
                 + [{"puesto_intra": 2000 + i, "clase": "C"} for i in range(5)]
                 + [{"puesto_intra": 3000 + i, "clase": "D"} for i in range(2760)])
        io.open(archivo, "w", encoding="utf-8", newline=NL).write(
            NL.join(json.dumps(f, ensure_ascii=False) for f in filas) + NL)
        destino, medido = AP.sellar_marcador(VUELTA, ruta=archivo, base=tmp)
        ok &= _caso(w, "la salida sellada existe y no mide cero bytes",
                    os.path.exists(destino) and os.path.getsize(destino) > 0, True)
        ok &= _caso(w, "y sus cifras salen de contar el archivo, no de una tabla",
                    (medido["filas"], medido["por_clase"]),
                    (3388, {"A": 551, "B": 72, "C": 5, "D": 2760}))
        ok &= _caso(w, "CON la salida sellada y calzando, la guarda sale VERDE",
                    AP.guarda_del_marcador(acta_buena, VUELTA, base=tmp)[0], True)
        w("   LA MUTACION, UNA POR CIFRA, Y CADA UNA TIENE QUE MORDER:")
        acta_filas = acta_buena.replace("3388 filas", "3389 filas")
        ok &= _caso(w, "un acta que se equivoca en las FILAS: CAE",
                    AP.guarda_del_marcador(acta_filas, VUELTA, base=tmp)[0], False)
        acta_clase = acta_buena.replace("B 72", "B 73")
        ok &= _caso(w, "un acta que se equivoca en UNA CLASE: CAE",
                    AP.guarda_del_marcador(acta_clase, VUELTA, base=tmp)[0], False)
        acta_falta = acta_buena.replace(", C 5", "")
        ok &= _caso(w, "un acta a la que le FALTA una clase: CAE",
                    AP.guarda_del_marcador(acta_falta, VUELTA, base=tmp)[0], False)
        acta_muda = "| marcador | lo reconte a mano y da lo mismo | SI |"
        ok &= _caso(w, "un acta que NO publica cifras: CAE, no pasa por muda",
                    AP.guarda_del_marcador(acta_muda, VUELTA, base=tmp)[0], False)
        ok &= _caso(w, "y la buena SIGUE saliendo verde despues de las cuatro",
                    AP.guarda_del_marcador(acta_buena, VUELTA, base=tmp)[0], True)
        w("")
    finally:
        # EL ORDEN DE ESTAS TRES LINEAS ES UNA CAIDA MIA, DECLARADA Y REMEDIADA.
        # La primera version restauraba `AP.RUTA_DEL_TURNO` ANTES de llamar a
        # `olvidar_todo()`, y `olvidar_todo()` BORRA el fichero del turno: el
        # arnes se llevo por delante la sede de verdad del auditor. Lo cazo el
        # ultimo caso de este mismo arnes, el que mide la sede antes y despues.
        # AHORA SE OLVIDA PRIMERO, con la ruta todavia en el temporal, Y SE
        # RESTAURA DESPUES.
        AP.olvidar_todo()
        AP.RUTA_DEL_TURNO = ruta_original
        AP.LOOP = loop_original
        shutil.rmtree(tmp, ignore_errors=True)
        w("D) EL TEMPORAL SE RETIRA (P.16, quien fabrica limpia)")
        w("   (su nombre NO se imprime: `mkdtemp` lo fabrica aleatorio y esta")
        w("    salida se sella y se compara byte a byte)")
        ok &= _caso(w, "el temporal quedo retirado", os.path.exists(tmp), False)
        ok &= _caso(w, "y AP.RUTA_DEL_TURNO vuelve a su sede",
                    AP.RUTA_DEL_TURNO == ruta_original, True)
        ok &= _caso(w, "y AP.LOOP vuelve a docs/loop de verdad",
                    AP.LOOP == loop_original, True)
        ok &= _caso(w, "el fichero del turno del TEMPORAL si quedo borrado",
                    os.path.exists(os.path.join(tmp, "_TURNO_DEL_AUDITOR.json")),
                    False)
        turno_despues = medir_turno_real()
        w("   LA SEDE DE VERDAD DEL TURNO, MEDIDA ANTES Y DESPUES:")
        w("   al entrar: %s | al salir: %s"
          % ("EXISTE, %d bytes" % turno_antes[1] if turno_antes[0] else "NO EXISTE",
             "EXISTE, %d bytes" % turno_despues[1] if turno_despues[0]
             else "NO EXISTE"))
        ok &= _caso(w, "el turno del auditor DE VERDAD no CAMBIO",
                    turno_despues, turno_antes)
    w("")
    w("=" * 78)
    w("CASOS: %d | VERDES: %d | ROJOS: %d"
      % (_CUENTA["casos"], _CUENTA["pasan"], _CUENTA["casos"] - _CUENTA["pasan"]))
    w("VEREDICTO: %s" % ("VERDE" if ok else "ROJO"))
    w("=" * 78)
    t = NL.join(L) + NL
    # REPRODUCIBLE (auditoria integral, 9 sep 2026): el sufijo aleatorio del
    # temporal de mkdtemp se imprimia en los motivos publicados y la doble
    # corrida de la bateria lo veia como salida que NO SE REPITE. Se sustituye
    # por un rotulo fijo ANTES de sellar; el temporal sigue siendo aleatorio.
    t = re.sub(r"v197_orden_turno_[A-Za-z0-9_]+", "v197_orden_turno_TEMPORAL", t)
    io.open(SALIDA, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (SALIDA, len(t.encode("utf-8"))))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
