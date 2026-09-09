# -*- coding: utf-8 -*-
r"""vuelta199_tarea1_mutacion_guardas_revividas.py . EL CASO POSITIVO POR MUTACION
DE LAS DOS GUARDAS QUE LA VUELTA 199 VOLVIO A ENCENDER.

DE DONDE SALE, Y NO ES UN ARNES NUEVO INVENTADO: el encargo de la vuelta 199 dice
con esas palabras *"Se parte del ARNES QUE EL AUDITOR DEJO ESCRITO; no se escribe
uno nuevo desde cero"*. La fuente es
`scripts/loop/_auditor_v198_guarda_muerta.py`, de la que se copian el proceso
HIJO, el constructor de escenarios `escribir_turno()` y la medicion de la sede.
**LO QUE CAMBIA SON LOS ESPERADOS**: aquel arnes salia VERDE probando que las
guardas NO mordian; este sale VERDE probando que SI muerden, y ademas corre la
MUTACION que las apaga y comprueba que los mismos casos CAEN.

LAS DOS EXIGENCIAS DEL ENCARGO, QUE NO SE NEGOCIAN PORQUE SON JUSTO POR DONDE SE
ESCAPARON:
  . **PROCESOS DISTINTOS.** Ni un solo caso se decide dentro de la misma corrida.
    Cada paso arranca un `subprocess` propio, que es lo que los 49 casos de la
    197 no hacian y por eso salian verdes sobre un agujero.
  . **SOBRE UN TURNO CERRADO.** El escenario se monta escribiendo a mano el
    fichero del turno con `vivo.abierto: false`, que es el estado EXACTO en el que
    la vuelta 197 dejo la sede y en el que el auditor de la 198 la encontro.

LA MUTACION, Y ES LO QUE HACE QUE ESTO SEA UNA PRUEBA Y NO UNA AFIRMACION
(`EJECUTOR.md` 1, EL CASO ROJO SE PRUEBA POR MUTACION, 29 ago 2026): se copia
`apertura_del_auditor.py` a un temporal, se le QUITAN los remedios por
sustitucion de texto, y se corren LOS MISMOS escenarios contra la copia mutilada.
**Si un caso no cae al quitarle su remedio, ese caso no prueba nada y este arnes
sale ROJO.** Ninguna variable de veredicto es una constante literal: todas salen
de llamar al modulo de verdad en un proceso hijo.

LAS TRES MUTACIONES, UNA POR REMEDIO:
  A) `_cargar_turno()` deja de reabrir el turno consumido  -> muere la `1.a` de carga
  B) `_apuntar_sello()` deja de reabrir el turno           -> muere la `1.a` de sello
  C) `sello_mas_reciente_en_disco()` devuelve vacio        -> muere la `1.b`

Y CADA MUTACION SE MIDE DONDE DE VERDAD SE VE, QUE ES UNA COSA QUE ESTE ARNES
APRENDIO EN ROJO Y VA ESCRITA PORQUE ES LA MITAD QUE LO HACE VALER:

  . LA `B` NO SE VE SOLA. Con la `A` puesta, `_cargar_turno()` ya reabre el turno
    antes de que `_apuntar_sello()` llegue, asi que quitarle a la cola del sello
    su linea NO CAMBIA NADA MEDIBLE. Se mide contra la `A` YA QUITADA: `mut_A`
    (solo A) contra `mut_AB` (A y B). Un remedio que solo se ve cuando el otro
    falta SIGUE SIENDO un remedio, pero decir que se prueba solo seria falso.
  . LA `C` NO SE VE EN EL ESCENARIO LARGO, y por el motivo simetrico: con la `A`
    puesta el sello SOBREVIVE EN MEMORIA, y `puede_leer_reporte()` cae en rojo por
    la memoria antes de llegar a mirar el disco. Se mide en su ESCENARIO PROPIO,
    que es ademas el estado exacto que el auditor de la 198 se encontro: turno
    CERRADO, memoria en blanco, y EL SELLO EN EL DISCO, AL LADO.

Y EL CASO QUE IMPIDE QUE EL REMEDIO SE PASE DE FRENADA, porque un guardia que no
deja pasar a nadie es una pared: un turno CERRADO CON SU CONSTANCIA (la vuelta
esta en `cerrados` con su `ruta_clases`) **tiene que dejar leer el reporte**.

NO TOCA LA SEDE DE VERDAD: todo corre sobre un fichero de turno TEMPORAL y sobre
una carpeta de sellos TEMPORAL, y al terminar se mide que
`docs/loop/_TURNO_DEL_AUDITOR.json` sigue byte a byte igual.

SUJETO CONGELADO, DECLARADO: este arnes fabrica TODO su material con `mkdtemp` y
no lee ningun fichero vivo del repo salvo el modulo que prueba. La unica aparicion
de `REPORTE.md` fuera de este docstring es el nombre del toque que la bitacora
apunta, no una lectura del reporte del arbol.

Y UNA COSA QUE SE DICE EN VEZ DE CALLARSE: **este fichero NO entra en la nomina de
la bateria**, porque `AUDITOR.md` 6.3 la congela en 135 y dice NI CRECE NI SE PODA.
Queda fuera por regla escrita, no por olvido.

COMO SE CORRE:
  python scripts/loop/vuelta199_tarea1_mutacion_guardas_revividas.py
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

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
AQUI = os.path.dirname(os.path.abspath(__file__))
NL = chr(10)
PY = sys.executable
MODULO = os.path.join(AQUI, "apertura_del_auditor.py")

# EL PROCESO HIJO, COPIADO DEL ARNES DEL AUDITOR DE LA 198 Y CON DOS ANADIDOS
# DECLARADOS: el directorio del modulo entra por argumento (para poder importar la
# COPIA MUTADA en vez del original) y `AP.LOOP` se redirige al temporal (para que
# `puede_leer_reporte()` A SECAS mire los sellos del temporal y no los de la sede).
# Redirigir `AP.LOOP` es lo que permite llamarla SIN argumentos, que es como la
# doctrina manda y como el agujero se escapaba.
HIJO = r'''
# -*- coding: utf-8 -*-
import json, os, sys
sys.path.insert(0, sys.argv[1])
import apertura_del_auditor as AP
AP.RUTA_DEL_TURNO = sys.argv[3]
AP.LOOP = sys.argv[4]
AP._cargar_turno()
q = sys.argv[2]
if q == "sellar":
    # LA COLA DE sellar(), LLAMADA AL MODULO Y NO COPIADA AQUI. El arnes del
    # auditor de la 198 copiaba esas lineas en el hijo, y una copia NO SE ENTERA
    # DE LAS MUTACIONES que se le hacen al original: con la copia puesta, la
    # mutacion `B` de este arnes salia ROJA midiendo el hijo y no el modulo. Se
    # llama a `_apuntar_sello()`, que es exactamente lo que `sellar()` corre
    # despues de escribir el sello en disco, sin arrancar el aislador.
    AP._apuntar_sello(sys.argv[5], sys.argv[6])
elif q == "tocar":
    AP.apuntar(sys.argv[5])
elif q == "estado":
    AP.sys = sys
    print(json.dumps({
        "sellado_en_memoria": bool(AP._SELLADO["hecho"]),
        "bitacora": AP.bitacora(),
        "vivo_abierto": bool(AP._VIVO["abierto"]),
        "puede_sellar": AP.puede_sellar(),
        "puede_leer_sin_vuelta": AP.puede_leer_reporte(),
        "toques_prohibidos": AP.toques_prohibidos(),
        "sello_reciente": AP.sello_mas_reciente_en_disco(),
    }, ensure_ascii=False))
'''

# LAS TRES MUTACIONES, POR SUSTITUCION DE TEXTO SOBRE UNA COPIA. Cada par es
# (nombre, viejo, nuevo) y CADA `viejo` TIENE QUE APARECER EXACTAMENTE UNA VEZ:
# si apareciera cero o dos veces, la mutacion no seria la que dice ser y el arnes
# CAE antes de medir nada.
MUTACIONES = [
    ("A. _cargar_turno() deja de reabrir el turno consumido (mata la 1.a de carga)",
     "        # esta rama." + NL + '        _VIVO["abierto"] = True' + NL + "        return False",
     "        # esta rama." + NL + "        return False"),
    ("B. _apuntar_sello() deja de reabrir el turno (mata la 1.a de sello)",
     '    _SELLADO["vuelta"] = str(vuelta)' + NL + '    _VIVO["abierto"] = True' + NL
     + "    _guardar_turno()",
     '    _SELLADO["vuelta"] = str(vuelta)' + NL + "    _guardar_turno()"),
    ("C. sello_mas_reciente_en_disco() devuelve vacio (mata la 1.b)",
     "    carpeta = base or LOOP" + NL,
     '    return "", ""' + NL + "    carpeta = base or LOOP" + NL),
]


def medir(ruta):
    if not os.path.exists(ruta):
        return "NO EXISTE"
    b = io.open(ruta, "rb").read()
    return "%d bytes, sha256 %s" % (len(b), hashlib.sha256(b).hexdigest()[:16])


def escribir_turno(ruta, abierto, cerrados=None):
    """EL CONSTRUCTOR DE ESCENARIOS, COPIADO DEL ARNES DEL AUDITOR DE LA 198.
    Escribe el fichero del turno A MANO, que es como aquel arnes esquivo su propia
    caida: llamar a `cerrar_turno()` NO cerraba (sus precondiciones no se cumplian)
    y los rojos median otra cosa."""
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(json.dumps({
        "bitacora": [],
        "sellado": {"hecho": False, "ruta": None, "vuelta": None},
        "clases": {"escritas": False, "ruta": None},
        "cerrados": cerrados if cerrados is not None else {
            "197": {"motivo": "cierre de la TAREA 2.b de la 197",
                    "ruta_clases": "docs/loop/_auditor_v197_mis_clases.txt",
                    "bitacora": []}},
        "vivo": {"abierto": abierto}}, ensure_ascii=False, indent=1) + NL)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L, casos, verdes = [], 0, 0
    w = L.append

    def caso(titulo, ok, detalle=""):
        nonlocal casos, verdes
        casos += 1
        if ok:
            verdes += 1
        w("   %-64s %s" % (titulo[:64], "VERDE" if ok else "ROJO"))
        if detalle:
            w("      %s" % detalle)

    carpeta = tempfile.mkdtemp(prefix="v199_t1_")
    hijo_py = os.path.join(carpeta, "_hijo.py")
    io.open(hijo_py, "w", encoding="utf-8", newline=NL).write(HIJO)
    sede = os.path.join(LOOP, "_TURNO_DEL_AUDITOR.json")
    antes_sede = medir(sede)

    w("=" * 78)
    w("VUELTA 199, TAREA 1: LAS DOS GUARDAS APAGADAS, VUELTAS A ENCENDER Y")
    w("PROBADAS EN PROCESOS DISTINTOS SOBRE UN TURNO CERRADO.")
    w("Arnes de partida: scripts/loop/_auditor_v198_guarda_muerta.py")
    w("=" * 78)
    w("")
    w("SEDE DE VERDAD AL ENTRAR: %s" % antes_sede)
    w("")

    # ------------------------------------------------ LAS COPIAS DEL MODULO
    original = io.open(MODULO, encoding="utf-8").read()
    dir_sano = os.path.join(carpeta, "sano")
    os.makedirs(dir_sano)
    shutil.copy2(MODULO, os.path.join(dir_sano, "apertura_del_auditor.py"))
    w("-" * 78)
    w("LAS COPIAS DEL MODULO, Y CADA MUTACION COMPROBADA ANTES DE USARLA")
    w("   original: %s" % medir(MODULO))
    dirs_mutados = []
    for nombre, viejo, nuevo in MUTACIONES:
        veces = original.count(viejo)
        caso("la mutacion %s aparece EXACTAMENTE 1 vez en el modulo" % nombre[:2],
             veces == 1, "veces contadas: %d" % veces)
        d = os.path.join(carpeta, "mut_%s" % nombre[:1])
        os.makedirs(d)
        io.open(os.path.join(d, "apertura_del_auditor.py"), "w",
                encoding="utf-8", newline=NL).write(
            original.replace(viejo, nuevo, 1))
        dirs_mutados.append((nombre, d))
        w("   %s -> %s" % (nombre, os.path.basename(d)))
    # LA MUTACION TOTAL: las TRES a la vez, que es el modulo tal como estaba ANTES
    # de esta vuelta. Es la que reproduce el agujero entero que el auditor midio.
    texto_todo = original
    for _n, viejo, nuevo in MUTACIONES:
        texto_todo = texto_todo.replace(viejo, nuevo, 1)
    dir_todo = os.path.join(carpeta, "mut_TODO")
    os.makedirs(dir_todo)
    io.open(os.path.join(dir_todo, "apertura_del_auditor.py"), "w",
            encoding="utf-8", newline=NL).write(texto_todo)
    caso("la mutacion TOTAL cambia el modulo de verdad (no sale identica)",
         texto_todo != original,
         "bytes original %d, bytes mutado %d"
         % (len(original.encode("utf-8")), len(texto_todo.encode("utf-8"))))
    w("")

    def correr(dir_mod, turno, base, *args):
        r = subprocess.run([PY, hijo_py, dir_mod, args[0], turno, base]
                           + list(args[1:]),
                           capture_output=True, text=True, encoding="utf-8",
                           errors="replace", cwd=RAIZ)
        return (r.stdout or "") + (r.stderr or "")

    def estado(dir_mod, turno, base):
        crudo = correr(dir_mod, turno, base, "estado").strip()
        try:
            return json.loads(crudo.splitlines()[-1])
        except Exception:                                # noqa: BLE001
            return {"ROTO": crudo[-400:]}

    def escenario(dir_mod, etiqueta):
        """MONTA EL ESCENARIO ENTERO EN PROCESOS DISTINTOS Y DEVUELVE LO MEDIDO.

        SOBRE UN TURNO CERRADO, y con el sello de la vuelta 199 EN DISCO (en la
        carpeta temporal) pero SIN constancia de cierre para el 199: o sea, el
        estado exacto de un auditor que acaba de sellar y todavia no ha escrito
        sus clases."""
        base = os.path.join(carpeta, "base_%s" % etiqueta)
        if os.path.isdir(base):
            shutil.rmtree(base, ignore_errors=True)
        os.makedirs(base)
        io.open(os.path.join(base, "SELLO_APERTURA_AUDITOR_V199.json"), "w",
                encoding="utf-8", newline=NL).write("{}" + NL)
        turno = os.path.join(carpeta, "turno_%s.json" % etiqueta)
        escribir_turno(turno, False)
        # PROCESO 1: toca `git log`. ES ANTES DEL SELLO A PROPOSITO: la guarda de
        # la vuelta 193 tiene que morder sobre toques ANTERIORES al sello, y esa
        # es la mitad que reabrir-solo-al-sellar no arreglaria.
        correr(dir_mod, turno, base, "tocar", "git log")
        antes_de_sellar = estado(dir_mod, turno, base)
        # PROCESO 2: sella.
        correr(dir_mod, turno, base, "sellar", "ruta_de_sello_de_prueba", "199")
        # PROCESOS 3 y 4: dos toques mas, cada uno en su proceso.
        correr(dir_mod, turno, base, "tocar", "git status")
        correr(dir_mod, turno, base, "tocar", "REPORTE.md")
        return antes_de_sellar, estado(dir_mod, turno, base), base, turno

    # ------------------------------------------------- CON EL REMEDIO PUESTO
    w("-" * 78)
    w("ESCENARIO CON EL REMEDIO PUESTO. TURNO CERRADO, CUATRO PROCESOS DISTINTOS.")
    pre, d, base_sano, turno_sano = escenario(dir_sano, "sano")
    w("   tras el 1.er proceso (toco `git log`, ANTES de sellar):")
    w("      bitacora %s | puede_sellar %s"
      % (pre.get("bitacora"), (pre.get("puede_sellar") or [None])[0]))
    w("   tras los cuatro procesos:")
    w("      %s" % json.dumps({"sellado": d.get("sellado_en_memoria"),
                               "bitacora": d.get("bitacora"),
                               "vivo": d.get("vivo_abierto")},
                              ensure_ascii=False))
    w("")
    esperado_bit = ["git log", "git status", "REPORTE.md"]
    caso("1.a LA BITACORA ACUMULA ENTRE PROCESOS (remedio de la 193)",
         d.get("bitacora") == esperado_bit,
         "bitacora medida: %s" % d.get("bitacora"))
    caso("1.a EL SELLO SOBREVIVE de un proceso al siguiente",
         d.get("sellado_en_memoria") is True)
    caso("1.a `sellar()` PUEDE CAER EN ROJO: ve los prohibidos",
         d.get("toques_prohibidos") == ["git log", "git status", "REPORTE.md"],
         "toques prohibidos que ve: %s" % d.get("toques_prohibidos"))
    caso("1.a UN TOQUE ANTERIOR AL SELLO YA CIERRA `puede_sellar()`",
         (pre.get("puede_sellar") or [None])[0] is False,
         "motivo: %s" % (pre.get("puede_sellar") or [None, ""])[1][:96])
    caso("1.a `vivo.abierto` quedo en TRUE tras sellar",
         d.get("vivo_abierto") is True)
    caso("1.b `leer_reporte()` SIN vuelta CAE EN ROJO",
         (d.get("puede_leer_sin_vuelta") or [None])[0] is False,
         "motivo: %s" % (d.get("puede_leer_sin_vuelta") or [None, ""])[1][:96])
    caso("1.b y el sello que encuentra en disco SIN vuelta es el 199",
         (d.get("sello_reciente") or ["", ""])[1] == "199",
         "sello_mas_reciente_en_disco(): %s" % (d.get("sello_reciente"),))
    w("")

    # ---------------------------------- EL CASO QUE IMPIDE QUE SEA UNA PARED
    w("-" * 78)
    w("EL CASO DE LA PARED: UN TURNO CERRADO **CON SU CONSTANCIA** TIENE QUE")
    w("DEJAR LEER. Un guardia que no deja pasar a nadie no es un guardia.")
    turno_c = os.path.join(carpeta, "turno_constancia.json")
    escribir_turno(turno_c, False, cerrados={
        "199": {"motivo": "clases declaradas por el carril del sello de disco",
                "ruta_clases": "docs/loop/_auditor_v199_mis_clases.txt",
                "bitacora": []}})
    dc = estado(dir_sano, turno_c, base_sano)
    caso("1.b con `cerrados[199]` y su `ruta_clases`, SIN vuelta, DEJA PASAR",
         (dc.get("puede_leer_sin_vuelta") or [None])[0] is True,
         "motivo: %s" % (dc.get("puede_leer_sin_vuelta") or [None, ""])[1][:96])
    w("")
    w("Y SIN NINGUN SELLO EN DISCO NI EN MEMORIA, TAMPOCO ES PARED:")
    base_vacia = os.path.join(carpeta, "base_vacia")
    os.makedirs(base_vacia)
    turno_v = os.path.join(carpeta, "turno_vacio.json")
    escribir_turno(turno_v, False, cerrados={})
    dv = estado(dir_sano, turno_v, base_vacia)
    caso("1.b sin sujeto sellado en ningun sitio, SIN vuelta, DEJA PASAR",
         (dv.get("puede_leer_sin_vuelta") or [None])[0] is True,
         "motivo: %s" % (dv.get("puede_leer_sin_vuelta") or [None, ""])[1][:96])
    w("")

    # ------------------------------------------------------- LA MUTACION
    w("-" * 78)
    w("LA MUTACION: SE LE QUITA CADA REMEDIO Y SE COMPRUEBA QUE SU CASO CAE.")
    w("Si un caso NO cae al quitarle su remedio, ese caso no prueba nada.")
    w("")
    por_letra = dict((n[:1], d) for n, d in dirs_mutados)

    # MUTACION A, EN EL ESCENARIO LARGO: es la que se ve sola y entera.
    pre_a, da, _b, _t = escenario(por_letra["A"], "mut_A")
    w("   MUTACION A (solo A)")
    w("      bitacora: %s | sellado: %s | prohibidos: %s"
      % (da.get("bitacora"), da.get("sellado_en_memoria"),
         da.get("toques_prohibidos")))
    caso("MUTACION A: la bitacora ya NO acumula entre procesos",
         da.get("bitacora") != esperado_bit,
         "bitacora con la mutacion: %s" % da.get("bitacora"))
    caso("MUTACION A: un toque anterior al sello ya NO cierra el sello",
         (pre_a.get("puede_sellar") or [None])[0] is True,
         "puede_sellar con la mutacion: %s"
         % ((pre_a.get("puede_sellar") or [None])[0],))
    w("")

    # MUTACION B, CONTRA LA `A` YA QUITADA, que es donde de verdad se ve.
    dir_ab = os.path.join(carpeta, "mut_AB")
    os.makedirs(dir_ab)
    texto_ab = original
    for _n, viejo, nuevo in MUTACIONES[:2]:
        texto_ab = texto_ab.replace(viejo, nuevo, 1)
    io.open(os.path.join(dir_ab, "apertura_del_auditor.py"), "w",
            encoding="utf-8", newline=NL).write(texto_ab)
    _pre_ab, dab, _b, _t = escenario(dir_ab, "mut_AB")
    w("   MUTACION B, MEDIDA CONTRA LA `A` YA QUITADA (mut_A contra mut_AB)")
    w("      con A quitada y B PUESTA:   sellado %s" % da.get("sellado_en_memoria"))
    w("      con A y B quitadas:         sellado %s" % dab.get("sellado_en_memoria"))
    caso("MUTACION B: con la A fuera, la B PUESTA salva el sello",
         da.get("sellado_en_memoria") is True)
    caso("MUTACION B: con la A fuera, quitar la B TIRA el sello",
         dab.get("sellado_en_memoria") is False,
         "sellado con A y B quitadas: %s" % dab.get("sellado_en_memoria"))
    w("")

    # MUTACION C, EN SU ESCENARIO PROPIO: turno CERRADO, memoria en blanco, y el
    # sello EN DISCO al lado. Es el estado exacto del auditor de la 198.
    w("   MUTACION C, EN SU ESCENARIO PROPIO (el del auditor de la 198):")
    w("      turno CERRADO, memoria en blanco, y el sello V199 EN EL DISCO.")
    base_c = os.path.join(carpeta, "base_solo_disco")
    os.makedirs(base_c)
    io.open(os.path.join(base_c, "SELLO_APERTURA_AUDITOR_V199.json"), "w",
            encoding="utf-8", newline=NL).write("{}" + NL)
    turno_solo = os.path.join(carpeta, "turno_solo_disco.json")
    escribir_turno(turno_solo, False)
    d_sano_c = estado(dir_sano, turno_solo, base_c)
    escribir_turno(turno_solo, False)
    d_mut_c = estado(por_letra["C"], turno_solo, base_c)
    w("      con el remedio:   sellado en memoria %s | puede_leer SIN vuelta %s"
      % (d_sano_c.get("sellado_en_memoria"),
         (d_sano_c.get("puede_leer_sin_vuelta") or [None])[0]))
    w("      con la mutacion:  sellado en memoria %s | puede_leer SIN vuelta %s"
      % (d_mut_c.get("sellado_en_memoria"),
         (d_mut_c.get("puede_leer_sin_vuelta") or [None])[0]))
    caso("1.b EL ESCENARIO ES EL BUENO: la memoria NO tiene sello, solo el disco",
         d_sano_c.get("sellado_en_memoria") is False)
    caso("1.b CON EL REMEDIO, `leer_reporte()` SIN vuelta CAE EN ROJO",
         (d_sano_c.get("puede_leer_sin_vuelta") or [None])[0] is False,
         "motivo: %s" % (d_sano_c.get("puede_leer_sin_vuelta") or [None, ""])[1][:88])
    caso("MUTACION C: sin el remedio, SIN vuelta DEJA PASAR (el agujero de la 198)",
         (d_mut_c.get("puede_leer_sin_vuelta") or [None])[0] is True,
         "motivo con la mutacion: %s"
         % (d_mut_c.get("puede_leer_sin_vuelta") or [None, ""])[1][:88])
    w("")
    w("   Y LA MUTACION TOTAL, que es el modulo TAL COMO ESTABA ANTES DE ESTA")
    w("   VUELTA: tiene que reproducir el agujero ENTERO que el auditor midio.")
    pre_t, dt, _b, _t = escenario(dir_todo, "mut_TODO")
    w("      bitacora: %s | sellado: %s | prohibidos: %s"
      % (dt.get("bitacora"), dt.get("sellado_en_memoria"),
         dt.get("toques_prohibidos")))
    caso("TOTAL: el sello NO sobrevive, como midio la 198",
         dt.get("sellado_en_memoria") is False)
    caso("TOTAL: la bitacora NO acumula, como midio la 198",
         dt.get("bitacora") != esperado_bit,
         "bitacora: %s" % dt.get("bitacora"))
    caso("TOTAL: `sellar()` no ve ningun prohibido, como midio la 198",
         dt.get("toques_prohibidos") == [])
    caso("TOTAL: `leer_reporte()` SIN vuelta DEJA PASAR, como midio la 198",
         (dt.get("puede_leer_sin_vuelta") or [None])[0] is True)
    w("")

    # ----------------------------------------------------------------- LA SEDE
    w("-" * 78)
    despues_sede = medir(sede)
    w("SEDE DE VERDAD AL SALIR:  %s" % despues_sede)
    caso("LA SEDE DE VERDAD NO SE MOVIO (P.16, leccion de la `C.1` de la 197)",
         antes_sede == despues_sede)
    shutil.rmtree(carpeta, ignore_errors=True)
    caso("el temporal se retira (P.16, quien fabrica limpia)",
         not os.path.exists(carpeta))

    w("")
    w("=" * 78)
    w("CASOS: %d | VERDES: %d | ROJOS: %d" % (casos, verdes, casos - verdes))
    w("VEREDICTO DEL ARNES: %s" % ("VERDE" if verdes == casos else "ROJO"))
    w("=" * 78)

    t = NL.join(L) + NL
    # REPRODUCIBLE (auditoria integral, 9 sep 2026): el sufijo aleatorio del
    # temporal de mkdtemp se imprimia en los motivos publicados y la doble
    # corrida de la bateria lo veia como salida que NO SE REPITE. Se sustituye
    # por un rotulo fijo ANTES de sellar; el temporal sigue siendo aleatorio.
    t = re.sub(r"v199_t1_[A-Za-z0-9_]+", "v199_t1_TEMPORAL", t)
    ruta = os.path.join(LOOP, "SALIDA_V199_T1_GUARDAS_REVIVIDAS.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0 if verdes == casos else 1


if __name__ == "__main__":
    sys.exit(main())
