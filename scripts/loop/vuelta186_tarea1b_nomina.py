# -*- coding: utf-8 -*-
r"""vuelta186_tarea1b_nomina.py . LA PRUEBA DE QUE LOS DOS ARNESES DE LA 185
ENTRARON EN LA NOMINA, Y DE QUE SOBREVIVEN A LA DOBLE CORRIDA DE LA 189.

QUIEN LO ENCARGA Y CON QUE PALABRAS. El acta 186, punto `7.3`, contestando la
`P.3` del reporte de la 185: *"los dos arneses nacidos en la 185 entran en la
nomina EN LA TAREA 1.b DE LA 186, con `arneses_que_faltan()` devolviendo 0 como
prueba"*. Y su `5.4`: *"si no se hace ahora, la bateria de la 189 abre en rojo
por una omision que ya esta medida y nombrada"*.

ESTE FICHERO NO ES UN ARNES DE MUTACION Y NO ENTRA EN LA NOMINA. Es la SALIDA
SELLADA de una tarea: mide la nomina antes y despues, corre
`arneses_que_faltan()` y corre los dos arneses DOS VECES CADA UNO EN PROCESOS
APARTE exigiendo el mismo `sha256`. Su nombre no casa con el patron de arneses de
`verificar_mutaciones_viejas.py` justamente por eso, y esa afirmacion SE MIDE
aqui abajo en vez de dejarse dicha.

POR QUE LA DOBLE CORRIDA SE HACE HOY Y NO EN LA 189. La bateria corre cada arnes
DOS VECES y exige que su salida sea identica. El arnes
`vuelta182_tarea2_mutacion_apertura_auditor.py` fallo exactamente ahi en la 184,
porque su salida llevaba dentro el nombre de un directorio temporal que cambia en
cada corrida. Comprobarlo aqui es la unica forma de saber HOY si los dos nuevos
van a sobrevivir, en vez de enterarse en la 189 con la bateria a medias.

LO QUE ESTE FICHERO ENSUCIA, DECLARADO: correr los dos arneses REESCRIBE sus dos
salidas selladas en `docs/loop/`. Si el `sha256` es el mismo, `git status` no ve
nada; si cambia, es PARADA y se dice.

NO SE PODA NADA. La opcion `c` de la parada del 5 sep 2026 quedo RECHAZADA por el
fundador. Aqui la nomina CRECE, que es lo contrario.

USO:
  python scripts/loop/vuelta186_tarea1b_nomina.py
"""
import hashlib
import io
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verificar_mutaciones_viejas as VMV   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
PY = sys.executable

LOS_DOS = [
    ("scripts/loop/vuelta185_tarea1b_mutacion_sin_temporal.py",
     "docs/loop/SALIDA_V185_T1B_MUTACION_SIN_TEMPORAL.txt"),
    ("scripts/loop/vuelta185_tarea1c_mutacion_bateria_continuada.py",
     "docs/loop/SALIDA_V185_T1C_MUTACION_BATERIA_CONTINUADA.txt"),
]


def sha_de(ruta):
    datos = io.open(ruta, "rb").read()
    lf = datos.replace(b"\r\n", b"\n")
    return hashlib.sha256(datos).hexdigest(), hashlib.sha256(lf).hexdigest(), len(datos)


def _mitad_de_la_nomina(w):
    """A, B, C Y D: la nomina, sus invariantes y la mirada sobre este fichero.
    Devuelve la cuenta de fallos."""
    fallos = 0
    w("A) EL TAMANO DE LA NOMINA, CONTADO DE `VIEJAS` Y NO TECLEADO")
    nombres = [s for s, _a in VMV.VIEJAS]
    w("   CIFRA nomina DESPUES (len(VIEJAS) en este proceso): %d" % len(nombres))
    w("   CIFRA nomina ANTES, leida del bloque de apertura sellado de esta vuelta:")
    ap = os.path.join(LOOP, "SALIDA_V186_APERTURA.txt")
    antes = None
    if os.path.exists(ap):
        for l in io.open(ap, encoding="utf-8", errors="replace"):
            if "CIFRA nomina ANTES" in l:
                w("      | " + l.strip())
                try:
                    antes = int(l.split("CIFRA nomina ANTES:")[1].split("|")[0].strip())
                except Exception:
                    antes = None
    else:
        w("      docs/loop/SALIDA_V186_APERTURA.txt NO EXISTE")
    w("   CRECIMIENTO: %s"
      % ("de %d a %d, o sea %+d" % (antes, len(nombres), len(nombres) - antes)
         if antes is not None else "(no medible: la apertura no publica la cifra)"))
    if antes is None or len(nombres) - antes != 2:
        w("   PARADA: la nomina no crecio en exactamente 2.")
        fallos += 1
    w("   LOS DOS ULTIMOS NOMBRES DE LA NOMINA, LEIDOS DE `VIEJAS`:")
    for n in nombres[-2:]:
        w("      %s" % n)
    w("   CIFRA entradas duplicadas en la nomina: %d"
      % (len(nombres) - len(set(nombres))))
    if len(nombres) != len(set(nombres)):
        w("   PARADA: hay nombres repetidos en la nomina.")
        fallos += 1
    w("")

    w("B) LA PRUEBA QUE EL ACTA PIDE: arneses_que_faltan() TIENE QUE DAR 0")
    ultima, faltan = VMV.arneses_que_faltan()
    w("   arneses_que_faltan() -> ultima vuelta %s, faltan %d" % (ultima, len(faltan)))
    for n in faltan:
        w("      FALTA: %s" % n)
    if faltan:
        w("   PARADA: siguen faltando arneses en la nomina.")
        fallos += 1
    else:
        w("   VERDE: no falta ninguno. Es la prueba que el acta 186 pide en su 7.3.")
    w("")

    w("C) LOS OTROS DOS INVARIANTES DE LA NOMINA, CORRIDOS IGUAL")
    invis = VMV.nomina_invisible_al_censo()
    w("   nomina_invisible_al_censo(): %d" % len(invis))
    for n in invis:
        w("      INVISIBLE: %s" % n)
    if invis:
        w("   PARADA: el censo no reconoce un nombre de su propia nomina.")
        fallos += 1
    malas = VMV.guarda_del_sujeto_congelado()
    w("   guarda_del_sujeto_congelado(): %d entradas sin congelar" % len(malas))
    for nombre, veredicto, _vive in malas:
        w("      SUJETO SIN CONGELAR: %-50s %s" % (nombre, veredicto))
    w("   (esta guarda NO esta cableada al rojo global de la bateria: el encargo")
    w("    de la vuelta 179 lo prohibe expresamente, y aqui se mide y se publica)")
    w("   CIFRA censo: %d | VARA_DEL_CENSO: %d"
      % (len(VMV.arneses_del_directorio()), VMV.VARA_DEL_CENSO))
    w("")

    w("D) ESTE FICHERO NO ENTRA EN LA NOMINA, Y NO SE AFIRMA: SE MIDE")
    yo = os.path.basename(os.path.abspath(__file__))
    w("   nombre de este fichero: %s" % yo)
    w("   casa con el patron de arneses del censo: %s"
      % ("SI" if VMV.PATRON_ARNES.match(yo) else "NO"))
    w("   esta en el censo: %s"
      % ("SI" if yo in VMV.arneses_del_directorio() else "NO"))
    if VMV.PATRON_ARNES.match(yo) or yo in VMV.arneses_del_directorio():
        w("   PARADA: este fichero es una salida sellada de tarea, no un arnes de")
        w("   mutacion, y el censo no deberia verlo.")
        fallos += 1
    w("")
    return fallos


def _mitad_de_la_doble_corrida(w):
    """E: los dos arneses corridos DOS VECES CADA UNO EN PROCESOS APARTE.
    Devuelve la cuenta de fallos."""
    fallos = 0
    w("E) LA DOBLE CORRIDA, EN PROCESOS APARTE, QUE ES LO QUE LA 189 VA A HACER")
    w("   (cada arnes se corre DOS VECES y se exige que su salida sellada tenga el")
    w("    MISMO sha256 las dos veces. El arnes de la 182 fallo exactamente aqui en")
    w("    la 184, por llevar dentro el nombre de un temporal que cambia solo)")
    for rel_arnes, rel_salida in LOS_DOS:
        w("")
        w("   ARNES: %s" % rel_arnes)
        w("   SALIDA SELLADA: %s" % rel_salida)
        p_sal = os.path.join(RAIZ, rel_salida.replace("/", os.sep))
        if not os.path.exists(p_sal):
            w("      LA SALIDA SELLADA NO EXISTE ANTES DE CORRER. Se dice.")
            sha_previo = None
        else:
            _sd, sl, tam = sha_de(p_sal)
            sha_previo = sl
            w("      ANTES DE CORRER: %d bytes en disco | sha256 LF %s" % (tam, sl))
        vistos = []
        for pasada in (1, 2):
            env = dict(os.environ)
            env["PYTHONIOENCODING"] = "utf-8"
            r = subprocess.run([PY, rel_arnes], cwd=RAIZ, capture_output=True, env=env)
            sal = (r.stdout.decode("utf-8", errors="replace")
                   + r.stderr.decode("utf-8", errors="replace"))
            ver = [l.strip() for l in sal.replace(chr(13), "").split(NL)
                   if "VEREDICTO" in l or "CIFRA fallos" in l or "CIFRA casos" in l]
            if not os.path.exists(p_sal):
                w("      PASADA %d: EXITCODE %d, y la salida sellada NO se escribio."
                  % (pasada, r.returncode))
                vistos.append(None)
                fallos += 1
                continue
            _sd, sl, tam = sha_de(p_sal)
            vistos.append(sl)
            w("      PASADA %d: EXITCODE %d | %d bytes | sha256 LF %s"
              % (pasada, r.returncode, tam, sl))
            for l in ver[:4]:
                w("         | " + l[:130])
            if r.returncode != 0:
                w("         PARADA: el arnes cae en rojo. Es un arnes YA SELLADO, y")
                w("         por el encargo permanente se trae con su salida entera y")
                w("         no se arregla aqui.")
                fallos += 1
        iguales = (len(vistos) == 2 and vistos[0] is not None
                   and vistos[0] == vistos[1])
        w("      LAS DOS PASADAS DAN EL MISMO sha256: %s"
          % ("SI" if iguales else "NO"))
        if not iguales:
            w("      PARADA: este arnes CAMBIA SOLO entre corridas y la bateria de")
            w("      la 189 lo veria como rojo. Se trae sin arreglarlo.")
            fallos += 1
        if sha_previo is not None and vistos and vistos[0] is not None:
            w("      Y ES EL MISMO QUE ESTABA COMMITEADO ANTES DE CORRER: %s"
              % ("SI" if sha_previo == vistos[0] else "NO"))
            if sha_previo != vistos[0]:
                w("      PARADA: la salida sellada cambio respecto de la commiteada.")
                fallos += 1
    w("")
    return fallos


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA 186, TAREA 1.b: LOS DOS ARNESES DE LA 185 EN LA NOMINA")
    w("(acta 186, punto 7.3, contestando la P.3 del reporte de la 185)")
    w("=" * 78)
    w("")
    fallos = _mitad_de_la_nomina(w)
    fallos += _mitad_de_la_doble_corrida(w)
    w("CIFRA fallos: %d" % fallos)
    w("VEREDICTO: %s" % ("VERDE" if fallos == 0 else "ROJO"))
    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V186_T1B_NOMINA.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0 if fallos == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
