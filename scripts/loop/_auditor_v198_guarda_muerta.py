# -*- coding: utf-8 -*-
r"""_auditor_v198_guarda_muerta.py . EL CASO POSITIVO POR MUTACION DE DOS GUARDAS
QUE YA NO MUERDEN, ESCRITO POR EL AUDITOR DE LA VUELTA 198 CONTRA LOS FICHEROS
QUE LE PROTEGEN A EL.

QUE SOSTENGO, Y LO SOSTENGO CON UNA CORRIDA Y NO LEYENDO CODIGO: desde que la
TAREA 2.b de la vuelta 197 dejo `docs/loop/_TURNO_DEL_AUDITOR.json` con
`vivo.abierto: false`, **NINGUN PROCESO VUELVE A ABRIR EL TURNO**, y con eso se
apagan de golpe DOS remedios escritos:

  . el de la **vuelta 193**: que la bitacora sobreviva al proceso, que es lo unico
    que hace que `sellar()` pueda caer en rojo si el turno ya toco `git log`,
    `git status` o `REPORTE.md`;
  . el de la **vuelta 197, TAREA 2.a**: que `leer_reporte()` caiga en rojo con el
    sujeto sellado y las clases sin escribir.

**Y NO ES UNA SOSPECHA MIA: ME PASO A MI EN ESTA VUELTA.** Selle por el CLI, llame
a `AP.leer_reporte()` como `AUDITOR.md` manda, y el modulo me entrego el reporte
entero con las tablas de discrepancias de MI PROPIO SUJETO, sin un solo rojo.

LA CAUSA, EN UNA LINEA DE CODIGO: `_cargar_turno()` lee `vivo.abierto`; si es
`False` llama a `_reiniciar_memoria()` y vuelve, **y ni ahi ni en `sellar()` ni en
`apuntar()` se vuelve a poner en `True`**. La unica linea que lo reabre esta en la
rama del fichero INEXISTENTE. Entonces `_guardar_turno()` reescribe
`vivo.abierto: false`, y **el proceso siguiente vuelve a reiniciar la memoria**:
lo que un proceso apunta, el siguiente lo tira.

Y LA SEGUNDA MITAD, QUE POR SI SOLA YA BASTARIA: `puede_leer_reporte()` solo
consulta `sello_en_disco()` **si se le pasa `vuelta`**, y el orden que `AUDITOR.md`
escribe es `leer_reporte()` A SECAS. Con la memoria reiniciada y sin `vuelta`, la
guarda concluye *"este turno NO ha sellado"* **con el sello de esa vuelta en el
disco, a su lado**.

POR QUE LOS 49 CASOS DE LA 197 SALEN VERDES Y AUN ASI ESTO PASA: aquel arnes
prueba la guarda **con la `vuelta` en la mano** y sobre un turno que **no venia
cerrado**. La sede real la llama **sin `vuelta`** y sobre un turno **que si venia
cerrado**. Es la especie que el banco `9` llama fallar callado: verde en el arnes
y mudo en produccion.

UNA CAIDA MIA QUE ESTE MISMO ARNES CAZO, Y VA ESCRITA PORQUE ES LA MITAD QUE
PRUEBA QUE EL ARNES SIRVE: mi PRIMERA version montaba el escenario llamando a
`cerrar_turno()` y daba por hecho que cerraba. **No cerraba** (sus precondiciones
no se cumplian), asi que el arnes declaraba ROJOS que no median lo que decian.
Esta version **escribe el fichero cerrado a mano**, que es el estado exacto en el
que yo encontre la sede.

COMO SE CORRE:
  python scripts/loop/_auditor_v198_guarda_muerta.py

NO TOCA LA SEDE DE VERDAD: todo corre sobre un fichero de turno TEMPORAL, y al
terminar se mide que `docs/loop/_TURNO_DEL_AUDITOR.json` sigue byte a byte igual
(la leccion de la `C.1` del reporte de la 197, que se llevo la sede por delante).
"""
import hashlib
import io
import json
import os
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
AQUI = os.path.dirname(os.path.abspath(__file__))
NL = chr(10)
PY = sys.executable

HIJO = r'''
# -*- coding: utf-8 -*-
import json, os, sys
sys.path.insert(0, r"%s")
import apertura_del_auditor as AP
AP.RUTA_DEL_TURNO = sys.argv[2]
AP._cargar_turno()
q = sys.argv[1]
if q == "sellar":
    # LO QUE HACE sellar() AL FINAL, sin correr el aislador y sin escribir ningun
    # sello de verdad: apuntar el sello en el estado del turno y guardarlo.
    AP._SELLADO.update({"hecho": True, "ruta": sys.argv[3], "vuelta": sys.argv[4]})
    AP._guardar_turno()
elif q == "tocar":
    AP.apuntar(sys.argv[3])
elif q == "estado":
    print(json.dumps({
        "sellado_en_memoria": bool(AP._SELLADO["hecho"]),
        "bitacora": AP.bitacora(),
        "vivo_abierto": bool(AP._VIVO["abierto"]),
        "puede_leer_sin_vuelta": AP.puede_leer_reporte(),
        "toques_prohibidos": AP.toques_prohibidos(),
    }, ensure_ascii=False))
''' % AQUI


def medir(ruta):
    if not os.path.exists(ruta):
        return "NO EXISTE"
    b = io.open(ruta, "rb").read()
    return "%d bytes, sha256 %s" % (len(b), hashlib.sha256(b).hexdigest()[:16])


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L, casos, verdes = [], 0, 0
    w = L.append
    hijo_py = os.path.join(tempfile.gettempdir(), "_auditor_v198_hijo.py")
    io.open(hijo_py, "w", encoding="utf-8", newline=NL).write(HIJO)

    def correr(turno, *args):
        r = subprocess.run([PY, hijo_py, args[0], turno] + list(args[1:]),
                           capture_output=True, text=True, encoding="utf-8",
                           errors="replace", cwd=RAIZ)
        return (r.stdout or "") + (r.stderr or "")

    def estado(turno):
        return json.loads(correr(turno, "estado").strip().splitlines()[-1])

    def caso(titulo, ok, detalle=""):
        nonlocal casos, verdes
        casos += 1
        if ok:
            verdes += 1
        w("   %-66s %s" % (titulo, "VERDE" if ok else "ROJO"))
        if detalle:
            w("      %s" % detalle)

    def escribir_turno(ruta, abierto):
        io.open(ruta, "w", encoding="utf-8", newline=NL).write(json.dumps({
            "bitacora": [],
            "sellado": {"hecho": False, "ruta": None, "vuelta": None},
            "clases": {"escritas": False, "ruta": None},
            "cerrados": {"197": {"motivo": "cierre de la TAREA 2.b de la 197",
                                 "ruta_clases": "docs/loop/_auditor_v197_mis_clases.txt",
                                 "bitacora": []}},
            "vivo": {"abierto": abierto}}, ensure_ascii=False, indent=1) + NL)

    w("=" * 78)
    w("VUELTA 198, EL AUDITOR CONTRA LAS GUARDAS QUE LE PROTEGEN:")
    w("UN TURNO CERRADO NO SE REABRE, Y CON EL SE APAGAN LOS REMEDIOS DE LA 193")
    w("Y DE LA 197")
    w("=" * 78)
    w("")
    sede = os.path.join(LOOP, "_TURNO_DEL_AUDITOR.json")
    antes = medir(sede)
    w("SEDE DE VERDAD AL ENTRAR: %s" % antes)
    w("")

    carpeta = tempfile.mkdtemp(prefix="v198_")
    tmp = os.path.join(carpeta, "_TURNO.json")

    # ------------------------------------------------------ ESCENARIO 1, CONTROL
    w("-" * 78)
    w("ESCENARIO 1 (CONTROL). TURNO ABIERTO (`vivo.abierto: true`).")
    w("Es como se comportaba la sede ANTES de que la 197 la cerrara.")
    escribir_turno(tmp, True)
    correr(tmp, "sellar", "ruta_de_sello_de_prueba", "198")
    correr(tmp, "tocar", "git log")
    correr(tmp, "tocar", "git status")
    d = estado(tmp)
    caso("el sello sobrevive de un proceso al siguiente", d["sellado_en_memoria"])
    caso("la bitacora ACUMULA entre procesos (remedio de la 193)",
         d["bitacora"] == ["git log", "git status"],
         "bitacora medida: %s" % d["bitacora"])
    caso("`sellar()` tendria con que caer en rojo: ve los prohibidos",
         d["toques_prohibidos"] == ["git log", "git status"],
         "toques prohibidos que ve: %s" % d["toques_prohibidos"])
    caso("`leer_reporte()` SIN vuelta CAE EN ROJO (remedio de la 197)",
         d["puede_leer_sin_vuelta"][0] is False,
         "motivo: %s..." % d["puede_leer_sin_vuelta"][1][:70])

    # ------------------------------------------- ESCENARIO 2, EL DE ESTA VUELTA
    w("")
    w("-" * 78)
    w("ESCENARIO 2 (EL DE VERDAD). TURNO CERRADO (`vivo.abierto: false`), que es")
    w("EXACTAMENTE el estado en que la vuelta 197 dejo la sede y en el que yo la")
    w("encontre al abrir mi turno.")
    escribir_turno(tmp, False)
    correr(tmp, "sellar", "ruta_de_sello_de_prueba", "198")
    tras_sellar = json.load(io.open(tmp, encoding="utf-8"))
    correr(tmp, "tocar", "git log")
    correr(tmp, "tocar", "git status")
    d = estado(tmp)
    w("")
    w("   el fichero JUSTO DESPUES de sellar: sellado=%s, vivo.abierto=%s"
      % (tras_sellar["sellado"]["hecho"], tras_sellar["vivo"]["abierto"]))
    w("   el fichero tras dos toques:         %s" % json.dumps(
        {"sellado": d["sellado_en_memoria"], "bitacora": d["bitacora"],
         "vivo": d["vivo_abierto"]}, ensure_ascii=False))
    w("")
    caso("EL SELLO NO SOBREVIVE: el proceso siguiente lo tira",
         d["sellado_en_memoria"] is False,
         "se guardo `sellado: true` y se lee `sellado: %s`" % d["sellado_en_memoria"])
    caso("LA BITACORA NO ACUMULA: cada proceso empieza limpio",
         d["bitacora"] != ["git log", "git status"],
         "bitacora medida: %s (se apuntaron los dos, en procesos distintos)"
         % d["bitacora"])
    caso("`sellar()` YA NO PUEDE CAER EN ROJO: no ve ningun prohibido",
         d["toques_prohibidos"] == [],
         "toques prohibidos que ve: %s" % d["toques_prohibidos"])
    caso("`leer_reporte()` SIN vuelta DEJA PASAR: LA GUARDA NO MUERDE",
         d["puede_leer_sin_vuelta"][0] is True,
         "motivo que da: %s..." % d["puede_leer_sin_vuelta"][1][:70])
    caso("`vivo.abierto` sigue en false despues de sellar y de dos toques",
         d["vivo_abierto"] is False)

    # ----------------------------------------------------------------- LA SEDE
    w("")
    w("-" * 78)
    despues = medir(sede)
    w("SEDE DE VERDAD AL SALIR:  %s" % despues)
    caso("LA SEDE DE VERDAD NO SE MOVIO (P.16, y la leccion de la `C.1` de la 197)",
         antes == despues)
    try:
        os.remove(tmp)
        os.rmdir(carpeta)
        os.remove(hijo_py)
    except Exception:                                    # noqa: BLE001
        pass

    w("")
    w("=" * 78)
    w("CASOS: %d | VERDES: %d | ROJOS: %d" % (casos, verdes, casos - verdes))
    w("VEREDICTO DEL ARNES: %s" % ("VERDE" if verdes == casos else "ROJO"))
    w("=" * 78)
    w("")
    w("LO QUE MIDE, DICHO SIN ADORNO: las dos guardas estan ENTERAS EN EL CODIGO y")
    w("sus casos de mutacion son verdes, pero sobre un turno CERRADO ninguna de las")
    w("dos muerde. El remedio de la 193 y el de la 197 llevan apagados desde que la")
    w("197 cerro la sede, y el sujeto de MI ciega se quemo por esa via.")
    w("EL VERDE DE ESTE ARNES SIGNIFICA QUE EL AGUJERO ESTA MEDIDO, no que este")
    w("reparado: repararlo es de codigo y va encargado, no lo hace este fichero.")

    t = NL.join(L) + NL
    io.open(os.path.join(LOOP, "SALIDA_V198_GUARDA_MUERTA.txt"), "w",
            encoding="utf-8", newline=NL).write(t)
    print(t)
    return 0 if verdes == casos else 1


if __name__ == "__main__":
    sys.exit(main())
