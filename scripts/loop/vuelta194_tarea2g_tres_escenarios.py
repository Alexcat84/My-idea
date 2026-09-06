# -*- coding: utf-8 -*-
r"""vuelta194_tarea2g_tres_escenarios.py . LOS DOS ARNESES DE LA CUARTA PUERTA
CORRIDOS EN LOS TRES ESCENARIOS DEL FICHERO DEL AUDITOR, PARA PONER LA TABLA
NUEVA AL LADO DE LA SUYA.

ES LA PIEZA `g` DE LA TAREA 2 DE LA VUELTA 194, literal del encargo: *"AL CERRAR,
CORRE LOS DOS ARNESES EN LOS TRES ESCENARIOS DE MI FICHERO (cada uno solo con el
fichero del turno puesto, y los dos seguidos) Y PUBLICA LAS TRES SALIDAS. Si el
verde de alguno sigue dependiendo del orden, PARAS Y LO TRAES."*

LA TABLA DEL AUDITOR, en `docs/loop/_auditor_v194_cuarta_puerta_rota.txt`, que es
lo que esto tiene que desmentir con mediciones y no con prosa:

  | solo el arnes de la 192  | EXISTE | exit 0, verde | BORRADO |
  | solo el arnes de la 193  | EXISTE | exit 1, ROJO  | EXISTE  |
  | los dos, en orden        | EXISTE | 192 verde, 193 verde | BORRADO |

QUE ANADE ESTE FICHERO SOBRE EL ARNES DE LA PIEZA `c`, Y NO ES UNA REPETICION: la
`c` es el CASO POSITIVO POR MUTACION, con su culpable fabricado y su caso rojo
que no puede salir verde. Esto es EL COTEJO CONTRA LA TABLA DEL AUDITOR, escenario
a escenario, y ademas mide **el `sha256` de la salida sellada de cada arnes en
CADA escenario**: si el verde de uno dependiera del orden, su salida cambiaria
entre escenarios y esa es la forma de verlo sin creerse ningun veredicto.

LA SEDE DE VERDAD SE TRATA IGUAL QUE EN LA PIEZA `c`: se mide al entrar, la viva
se respalda byte a byte si la hay, se pone un CENTINELA FABRICADO de contenido
fijo antes de cada escenario, y al terminar se retira, se restaura la viva y se
REMIDE. El ultimo caso es exactamente ese.

SALIDA DETERMINISTA: exitcodes, veredictos, mediciones del centinela y `sha256` de
salidas selladas. Ni nombres de temporales ni estado ambiental.

USO:
  python scripts/loop/vuelta194_tarea2g_tres_escenarios.py
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
NL = chr(10)
SALIDA = os.path.join(LOOP, "SALIDA_V194_T2G_TRES_ESCENARIOS.txt")
TURNO_REAL = os.path.join(LOOP, "_TURNO_DEL_AUDITOR.json")

CENTINELA = json.dumps({"bitacora": ["centinela del arnes de la 194"],
                        "sellado": {"hecho": False, "ruta": None,
                                    "vuelta": None},
                        "clases": {"escritas": False, "ruta": None}},
                       ensure_ascii=False, indent=1, sort_keys=True) + NL

# (arnes, su salida sellada). EN EL ORDEN ALFABETICO EN QUE LA BATERIA LOS CORRE.
ARNESES = [
    ("scripts/loop/vuelta192_tarea4_mutacion_cuarta_puerta.py",
     "docs/loop/SALIDA_V192_T4_MUTACION_CUARTA_PUERTA.txt"),
    ("scripts/loop/vuelta193_tarea4e_mutacion_sello_entre_procesos.py",
     "docs/loop/SALIDA_V193_T4E_MUTACION_SELLO_ENTRE_PROCESOS.txt"),
]

# LO QUE LA TABLA DEL AUDITOR PUBLICA PARA CADA ESCENARIO, ESCRITO AQUI COMO
# CONTRASTE Y NO COMO FUENTE (EJECUTOR.md 2): la cifra de hoy sale de correrlo.
LO_QUE_DECIA_EL_AUDITOR = {
    "solo la 192": ("exit 0, verde", "BORRADO"),
    "solo la 193": ("exit 1, ROJO", "EXISTE"),
    "los dos en orden": ("192 verde, 193 verde", "BORRADO"),
}

_CUENTA = {"casos": 0, "pasan": 0}


def medir(ruta):
    """(existe, bytes, sha256) DE UNA RUTA. Semi-pura: solo lee."""
    if not os.path.isfile(ruta):
        return (False, 0, "")
    datos = io.open(ruta, "rb").read()
    return (True, len(datos), hashlib.sha256(datos).hexdigest())


def poner_centinela():
    io.open(TURNO_REAL, "w", encoding="utf-8", newline=NL).write(CENTINELA)
    return medir(TURNO_REAL)


def correr(arnes):
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run([sys.executable, arnes], cwd=RAIZ, capture_output=True,
                       env=env)
    texto = (r.stdout.decode("utf-8", errors="replace")
             + r.stderr.decode("utf-8", errors="replace"))
    veredicto = ""
    for linea in texto.replace(chr(13), "").split(NL):
        if linea.strip().startswith("VEREDICTO"):
            veredicto = linea.strip()
    return r.returncode, veredicto


def _caso(w, nombre, obtenido, esperado):
    ok = obtenido == esperado
    _CUENTA["casos"] += 1
    _CUENTA["pasan"] += 1 if ok else 0
    w("   %-62s %s" % (nombre, "VERDE" if ok else "ROJO"))
    if not ok:
        w("      esperado: %r" % (esperado,))
        w("      obtenido: %r" % (obtenido,))
    return ok


def escenario(w, etiqueta, cuales):
    """CORRE UN ESCENARIO Y DEVUELVE (ok, filas). Deja la sede medida antes y
    despues, y con el centinela puesto al empezar."""
    ok = True
    antes = poner_centinela()
    w("   fichero del turno ANTES: %s"
      % ("EXISTE, %d bytes, sha256 %s" % (antes[1], antes[2][:16])
         if antes[0] else "NO EXISTE"))
    filas = []
    for i in cuales:
        arnes, sellada = ARNESES[i]
        cod, ver = correr(arnes)
        med = medir(os.path.join(RAIZ, sellada.replace("/", os.sep)))
        filas.append((arnes, cod, ver, med))
        w("   %s" % os.path.basename(arnes))
        w("      exitcode %d | %s" % (cod, ver or "(sin linea de veredicto)"))
        w("      su sellada: %d bytes | sha256 %s" % (med[1], med[2][:16]))
        ok &= _caso(w, "sale con exitcode 0", cod, 0)
    despues = medir(TURNO_REAL)
    w("   fichero del turno DESPUES: %s"
      % ("EXISTE, %d bytes, sha256 %s" % (despues[1], despues[2][:16])
         if despues[0] else "NO EXISTE, o sea BORRADO"))
    ok &= _caso(w, "el fichero del turno sigue EXACTAMENTE como estaba",
                despues, antes)
    viejo_ver, viejo_fichero = LO_QUE_DECIA_EL_AUDITOR[etiqueta]
    w("   LO QUE LA TABLA DEL AUDITOR PUBLICABA PARA ESTE ESCENARIO, COMO")
    w("   CONTRASTE Y NO COMO FUENTE: %r y el fichero %r"
      % (viejo_ver, viejo_fichero))
    return ok, filas


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    ok = True
    w("=" * 78)
    w("VUELTA 194, TAREA 2.g: LOS DOS ARNESES EN LOS TRES ESCENARIOS DEL")
    w("FICHERO DEL AUDITOR")
    w("=" * 78)
    w("")
    w("LA VARA DE ESTE FICHERO, ESCRITA ANTES DE CORRER NADA: un verde que")
    w("depende del orden en que corren dos arneses no prueba nada. Por eso cada")
    w("escenario mide TAMBIEN el sha256 de la salida sellada de cada arnes: si")
    w("el verde de uno fuera prestado, su salida cambiaria entre escenarios.")
    w("")

    sede_al_entrar = medir(TURNO_REAL)
    tmp = tempfile.mkdtemp(prefix="v194_tres_escenarios_")
    respaldo = os.path.join(tmp, "_TURNO_VIVO_RESPALDADO.json")
    if sede_al_entrar[0]:
        shutil.copyfile(TURNO_REAL, respaldo)
    todas = {}
    try:
        w("ESCENARIO 1. SOLO EL ARNES DE LA 192, CON EL FICHERO DEL TURNO PUESTO")
        ok1, f1 = escenario(w, "solo la 192", [0])
        ok &= ok1
        todas["solo la 192"] = f1
        w("")

        w("ESCENARIO 2. SOLO EL ARNES DE LA 193, CON EL FICHERO DEL TURNO PUESTO")
        ok2, f2 = escenario(w, "solo la 193", [1])
        ok &= ok2
        todas["solo la 193"] = f2
        w("")

        w("ESCENARIO 3. LOS DOS SEGUIDOS, EN EL ORDEN ALFABETICO DE LA BATERIA")
        ok3, f3 = escenario(w, "los dos en orden", [0, 1])
        ok &= ok3
        todas["los dos en orden"] = f3
        w("")

        w("EL COTEJO QUE DECIDE: LA SALIDA DE CADA ARNES ES LA MISMA CORRIDO SOLO")
        w("Y CORRIDO EN COMPANIA. Si el verde de uno dependiera del otro, aqui se")
        w("veria, porque la salida sellada llevaria dentro la diferencia.")
        for i, (arnes, sellada) in enumerate(ARNESES):
            etiqueta_sola = "solo la 192" if i == 0 else "solo la 193"
            sha_solo = todas[etiqueta_sola][0][3][2]
            sha_junto = todas["los dos en orden"][i][3][2]
            w("   %s" % os.path.basename(arnes))
            w("      corrido solo:    %s" % (sha_solo[:16] or "(sin sellada)"))
            w("      corrido en orden:%s" % (sha_junto[:16] or "(sin sellada)"))
            ok &= _caso(w, "su salida sellada es la MISMA en los dos escenarios",
                        sha_solo == sha_junto and bool(sha_solo), True)
            cod_solo = todas[etiqueta_sola][0][1]
            cod_junto = todas["los dos en orden"][i][1]
            ok &= _caso(w, "y su exitcode tambien", cod_solo, cod_junto)
        w("")
    finally:
        w("LA SEDE, DEVUELTA A COMO ESTABA Y REMEDIDA")
        try:
            if os.path.isfile(TURNO_REAL):
                os.remove(TURNO_REAL)
            if os.path.isfile(respaldo):
                shutil.copyfile(respaldo, TURNO_REAL)
        except Exception as e:                           # noqa: BLE001
            w("   NO SE PUDO RESTAURAR: %r" % (e,))
        ok &= _caso(w, "la sede quedo EXACTAMENTE como estaba al entrar",
                    medir(TURNO_REAL), sede_al_entrar)
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
    print("ESCRITO: docs/loop/SALIDA_V194_T2G_TRES_ESCENARIOS.txt (%d bytes)"
          % len(t.encode("utf-8")))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
