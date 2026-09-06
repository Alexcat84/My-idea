# -*- coding: utf-8 -*-
r"""vuelta194_tarea2c_mutacion_sede_del_turno.py . EL CASO POSITIVO POR MUTACION
DE LA TAREA 2 DE LA VUELTA 194: **CAE SI UN ARNES DE LA NOMINA MODIFICA O BORRA
`docs/loop/_TURNO_DEL_AUDITOR.json` EN SU SEDE DE VERDAD.**

QUE CAZA, CON LAS PALABRAS DEL ENCARGO Y DEL HALLAZGO `5.1` DEL ACTA 194:
`vuelta192_tarea4_mutacion_cuarta_puerta.py` llamaba a `AP.olvidar_todo()` OCHO
veces contra el modulo REAL sin redirigir `AP.RUTA_DEL_TURNO`, y desde que la
TAREA 4.a de la 193 le anadio a `olvidar_todo()` el `os.remove(RUTA_DEL_TURNO)`
eso pasaba a **BORRAR EL TURNO VIVO DEL AUDITOR**, con exitcode 0 y sin avisar.

**LANZA PROCESOS DE VERDAD, Y ESA ES LA MITAD QUE IMPORTA.** Corriendo todo en un
solo proceso esto NO SE VE: la sede se resuelve al IMPORTAR el modulo, y un arnes
importado desde aqui heredaria la redireccion de otro. Es la misma leccion que la
TAREA 4.e de la 193 dejo escrita: **el agujero vivia en la costura que el arnes
de un solo proceso no cruzaba.**

COMO LO PRUEBA, Y POR QUE PUEDE SALIR EN ROJO DE VERDAD:

  A. **EL CULPABLE FABRICADO.** Se escribe en un temporal un programa de cuatro
     lineas que reproduce el fallo exacto de antes de esta vuelta: importa
     `apertura_del_auditor` y llama a `olvidar_todo()` **sin redirigir nada**. Se
     lanza como PROCESO. **Si el detector no lo caza, este arnes sale ROJO.** Es
     el caso rojo que la letra del 29 ago 2026 exige: no es una constante
     comparada consigo misma, es codigo que de verdad borra el fichero.
  B. **EL ARNES DE LA 192, YA REPARADO**, lanzado como proceso: NO puede tocar la
     sede.
  C. **EL ARNES DE LA 193, YA REPARADO**, lanzado como proceso: NO puede tocar la
     sede, Y ademas tiene que salir VERDE **con el fichero del turno PUESTO**,
     que es justo lo que su caso `H` viejo hacia imposible.
  D. **LOS DOS SEGUIDOS, EN EL ORDEN ALFABETICO EN QUE LA BATERIA LOS CORRE.**
     Los dos verdes y la sede intacta: **el verde de cada uno tiene que ser
     suyo y no prestado del otro.**
  E. **LA GUARDA DURABLE DE LA PIEZA `d`**: `git check-ignore` dice que la sede
     esta cubierta por `.gitignore`, y `git ls-files` dice que no esta en el
     indice. **La comprobacion la hace git y no una lectura del fichero de
     reglas**, porque lo que importa es lo que git hace, no lo que el fichero
     parece decir.

LA SEDE DE VERDAD SE TOCA Y SE DEJA COMO ESTABA, Y SE DICE ENTERO EN VEZ DE
DISIMULARLO. Para probar que nadie la borra hace falta que EXISTA mientras corre
la prueba, asi que: se mide al entrar; si habia una viva se guarda byte a byte en
el temporal; se pone un **centinela FABRICADO de contenido fijo**, que es el que
los hijos pueden borrar; y al terminar se retira el centinela, **se restaura la
viva si la habia y se REMIDE** (existencia, bytes y `sha256`). **El ultimo caso
del arnes es exactamente ese: que la sede quedo como estaba al entrar.**

SALIDA DETERMINISTA A PROPOSITO: no se imprime el nombre del temporal, ni la
salida cruda de los hijos, ni el estado ambiental de la sede. Lo que se publica
son exitcodes, veredictos y el `sha256` del centinela, **que es fijo por
construccion**. Esta salida se sella y se compara byte a byte.

USO:
  python scripts/loop/vuelta194_tarea2c_mutacion_sede_del_turno.py
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
SALIDA = os.path.join(LOOP, "SALIDA_V194_T2C_MUTACION_SEDE_DEL_TURNO.txt")

RUTA_RELATIVA_DEL_TURNO = "docs/loop/_TURNO_DEL_AUDITOR.json"
TURNO_REAL = os.path.join(LOOP, "_TURNO_DEL_AUDITOR.json")

# EL CENTINELA, DE CONTENIDO FIJO PARA QUE SU sha256 NO CAMBIE ENTRE CORRIDAS.
CENTINELA = json.dumps({"bitacora": ["centinela del arnes de la 194"],
                        "sellado": {"hecho": False, "ruta": None,
                                    "vuelta": None},
                        "clases": {"escritas": False, "ruta": None}},
                       ensure_ascii=False, indent=1, sort_keys=True) + NL

# EL CULPABLE FABRICADO: el fallo exacto de antes de esta vuelta, en cuatro
# lineas. NO redirige `AP.RUTA_DEL_TURNO`, asi que `olvidar_todo()` borra la sede.
CULPABLE = ("import os, sys" + NL
            + "sys.path.insert(0, %r)" % SCRIPTS + NL
            + "import apertura_del_auditor as AP" + NL
            + "AP.olvidar_todo()" + NL)

# LOS ARNESES DE LA NOMINA QUE ESTA VUELTA REPARA, EN EL ORDEN ALFABETICO EN QUE
# LA BATERIA LOS CORRE. NO SE TOCA LA NOMINA: esta lista es de este arnes.
ARNESES = [
    "scripts/loop/vuelta192_tarea4_mutacion_cuarta_puerta.py",
    "scripts/loop/vuelta193_tarea4e_mutacion_sello_entre_procesos.py",
]

_CUENTA = {"casos": 0, "pasan": 0}


def medir_sede(ruta=None):
    """(existe, bytes, sha256) DE LA SEDE DE VERDAD DEL TURNO. Semi-pura: solo
    lee la ruta que se le pasa, y la ruta va por parametro para poder medir una
    fabricada. **LAS TRES COSAS A PROPOSITO:** un fichero reescrito con el mismo
    tamano tiene el mismo `existe` y los mismos `bytes`, y solo el `sha256` lo
    delata."""
    ruta = ruta or TURNO_REAL
    if not os.path.isfile(ruta):
        return (False, 0, "")
    datos = io.open(ruta, "rb").read()
    return (True, len(datos), hashlib.sha256(datos).hexdigest())


def poner_centinela():
    """ESCRIBE EL CENTINELA EN LA SEDE DE VERDAD. Devuelve su medicion."""
    io.open(TURNO_REAL, "w", encoding="utf-8", newline=NL).write(CENTINELA)
    return medir_sede()


def toco_la_sede(antes, despues):
    """SI UN PROCESO TOCO LA SEDE. PURA.

    Devuelve (toco, motivo). **Tocar es cualquiera de las tres:** que deje de
    existir, que cambie de tamano o que cambie de `sha256`. Se separa de la
    medicion a proposito para que su caso rojo se pueda correr sobre mediciones
    fabricadas, sin tocar nada."""
    if antes[0] and not despues[0]:
        return True, "LA BORRO"
    if not antes[0] and despues[0]:
        return True, "LA CREO donde no habia"
    if antes[1] != despues[1]:
        return True, "cambio de tamano, de %d a %d bytes" % (antes[1], despues[1])
    if antes[2] != despues[2]:
        return True, "cambio de sha256 con el mismo tamano"
    return False, "no la toco"


def correr_proceso(args):
    """LANZA UN PROCESO DE VERDAD Y DEVUELVE SU EXITCODE Y SU VEREDICTO.

    NO SE DEVUELVE SU SALIDA CRUDA: los hijos imprimen nombres de temporales y
    esta salida se sella y se compara byte a byte. Lo que se publica es el
    exitcode y la linea de veredicto, si la tiene."""
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run(args, cwd=RAIZ, capture_output=True, env=env)
    texto = (r.stdout.decode("utf-8", errors="replace")
             + r.stderr.decode("utf-8", errors="replace"))
    veredicto = ""
    for linea in texto.replace(chr(13), "").split(NL):
        if linea.strip().startswith("VEREDICTO"):
            veredicto = linea.strip()
    return r.returncode, veredicto


def git(args):
    r = subprocess.run(["git"] + list(args), cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace").strip()


def _caso(w, nombre, obtenido, esperado):
    ok = obtenido == esperado
    _CUENTA["casos"] += 1
    _CUENTA["pasan"] += 1 if ok else 0
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
    w("=" * 78)
    w("VUELTA 194, TAREA 2.c: NINGUN ARNES DE LA NOMINA TOCA LA SEDE DEL TURNO")
    w("=" * 78)
    w("")
    w("LO QUE SE PRUEBA Y POR QUE PUEDE CAER: cada arnes se lanza como PROCESO")
    w("NUEVO de verdad. La sede del turno se resuelve al IMPORTAR el modulo, asi")
    w("que un arnes importado desde aqui heredaria la redireccion de otro y el")
    w("agujero no se veria. Es la misma costura que la TAREA 4.e de la 193 cruzo.")
    w("")
    w("LA SEDE SE DEJA COMO ESTABA, Y SE DICE ENTERO: se mide al entrar, la viva")
    w("se guarda byte a byte si la hay, se pone un CENTINELA FABRICADO de")
    w("contenido fijo, y al terminar se retira, se restaura la viva y se REMIDE.")
    w("EL ULTIMO CASO ES EXACTAMENTE ESE.")
    w("")

    sede_al_entrar = medir_sede()
    tmp = tempfile.mkdtemp(prefix="v194_sede_del_turno_")
    respaldo = os.path.join(tmp, "_TURNO_VIVO_RESPALDADO.json")
    if sede_al_entrar[0]:
        shutil.copyfile(TURNO_REAL, respaldo)
    try:
        culpable = os.path.join(tmp, "culpable_fabricado.py")
        io.open(culpable, "w", encoding="utf-8", newline=NL).write(CULPABLE)

        w("A) EL CULPABLE FABRICADO, QUE REPRODUCE EL FALLO DE ANTES DE ESTA VUELTA")
        w("   Cuatro lineas: importa `apertura_del_auditor` y llama a")
        w("   `olvidar_todo()` SIN redirigir `AP.RUTA_DEL_TURNO`. Es el caso ROJO,")
        w("   y no puede salir verde: si el detector no lo caza, este arnes cae.")
        antes = poner_centinela()
        w("   centinela puesto: %d bytes | sha256 %s" % (antes[1], antes[2][:16]))
        ok &= _caso(w, "el centinela esta puesto antes de lanzar al culpable",
                    antes[0], True)
        cod, _ver = correr_proceso([sys.executable, culpable])
        despues = medir_sede()
        toco, motivo = toco_la_sede(antes, despues)
        w("   exitcode del culpable: %d" % cod)
        w("   veredicto del detector: %s" % motivo)
        ok &= _caso(w, "EL CULPABLE TOCA LA SEDE y el detector LO CAZA", toco, True)
        ok &= _caso(w, "y lo que hace es borrarla, que es el fallo de la `5.1`",
                    motivo, "LA BORRO")
        ok &= _caso(w, "y ademas SALE CON EXITCODE 0 mientras la borra: no avisa",
                    cod, 0)
        w("")

        w("B) EL ARNES DE LA 192, YA REPARADO, LANZADO SOLO Y COMO PROCESO")
        antes = poner_centinela()
        cod, ver = correr_proceso([sys.executable, ARNESES[0]])
        despues = medir_sede()
        toco, motivo = toco_la_sede(antes, despues)
        w("   %s" % ARNESES[0])
        w("      exitcode %d | %s" % (cod, ver or "(sin linea de veredicto)"))
        w("      el detector dice: %s" % motivo)
        ok &= _caso(w, "NO toca la sede de verdad", toco, False)
        ok &= _caso(w, "y sale en verde por su cuenta", cod, 0)
        w("")

        w("C) EL ARNES DE LA 193, YA REPARADO, LANZADO SOLO Y CON EL TURNO PUESTO")
        w("   (ESTE ES EL CASO QUE CAIA. Su caso `H` viejo exigia que el fichero")
        w("    NO EXISTIERA, o sea que pedia que no hubiera auditor, y por eso")
        w("    lanzado solo con el turno puesto salia en ROJO con exitcode 1)")
        antes = poner_centinela()
        cod, ver = correr_proceso([sys.executable, ARNESES[1]])
        despues = medir_sede()
        toco, motivo = toco_la_sede(antes, despues)
        w("   %s" % ARNESES[1])
        w("      exitcode %d | %s" % (cod, ver or "(sin linea de veredicto)"))
        w("      el detector dice: %s" % motivo)
        ok &= _caso(w, "NO toca la sede de verdad", toco, False)
        ok &= _caso(w, "y sale en verde CON EL FICHERO DEL TURNO PUESTO", cod, 0)
        w("")

        w("D) LOS DOS SEGUIDOS, EN EL ORDEN ALFABETICO EN QUE LA BATERIA LOS CORRE")
        w("   LO QUE ESTO PRUEBA: que el verde de cada uno es SUYO y no prestado.")
        w("   Antes de esta vuelta el primero borraba el fichero que el segundo")
        w("   exigia ausente, y el orden era lo unico que los ponia de acuerdo.")
        antes = poner_centinela()
        codigos = []
        for arnes in ARNESES:
            c, v = correr_proceso([sys.executable, arnes])
            codigos.append(c)
            w("      %-58s exitcode %d" % (os.path.basename(arnes), c))
        despues = medir_sede()
        toco, motivo = toco_la_sede(antes, despues)
        w("   el detector dice: %s" % motivo)
        ok &= _caso(w, "los DOS salen en verde corridos seguidos", codigos,
                    [0] * len(ARNESES))
        ok &= _caso(w, "y la sede sigue intacta despues de los dos", toco, False)
        w("")

        w("E) LA GUARDA DURABLE: LA SEDE NO SE PUEDE VOLVER A COMMITEAR")
        w("   La comprobacion la hace GIT y no una lectura del fichero de reglas:")
        w("   lo que importa es lo que git hace, no lo que `.gitignore` parece.")
        cod_ig, salida_ig = git(["check-ignore", "-v", "--", RUTA_RELATIVA_DEL_TURNO])
        cod_ls, salida_ls = git(["ls-files", "--", RUTA_RELATIVA_DEL_TURNO])
        w("      git check-ignore -v -> exitcode %d" % cod_ig)
        w("      la regla que lo cubre: %s"
          % (salida_ig.split("\t")[0] if cod_ig == 0 and salida_ig else "(ninguna)"))
        ok &= _caso(w, "git dice que la sede esta IGNORADA", cod_ig, 0)
        ok &= _caso(w, "y que NO esta en el indice", salida_ls.strip(), "")
        w("")

    finally:
        w("F) LA SEDE, DEVUELTA A COMO ESTABA Y REMEDIDA")
        try:
            if os.path.isfile(TURNO_REAL):
                os.remove(TURNO_REAL)
            if os.path.isfile(respaldo):
                shutil.copyfile(respaldo, TURNO_REAL)
        except Exception as e:                           # noqa: BLE001
            w("   NO SE PUDO RESTAURAR: %r" % (e,))
        sede_al_salir = medir_sede()
        ok &= _caso(w, "la sede quedo EXACTAMENTE como estaba al entrar",
                    sede_al_salir, sede_al_entrar)
        shutil.rmtree(tmp, ignore_errors=True)
        ok &= _caso(w, "y el temporal quedo retirado (P.16)", os.path.exists(tmp),
                    False)
        w("")

    w("CIFRA casos: %d | pasan: %d | fallan: %d"
      % (_CUENTA["casos"], _CUENTA["pasan"], _CUENTA["casos"] - _CUENTA["pasan"]))
    w("VEREDICTO: %s" % ("VERDE" if ok else "ROJO"))
    t = NL.join(L) + NL
    io.open(SALIDA, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: docs/loop/SALIDA_V194_T2C_MUTACION_SEDE_DEL_TURNO.txt (%d bytes)"
          % len(t.encode("utf-8")))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
