# -*- coding: utf-8 -*-
r"""vuelta187_tarea5a_nomina.py . LA PRUEBA DE QUE LOS CUATRO ARNESES DE LA 186
MAS LOS DOS QUE NACEN HOY ENTRARON EN LA NOMINA, Y DE QUE SOBREVIVEN A LA DOBLE
CORRIDA DE LA 189.

QUIEN LO ENCARGA Y CON QUE PALABRAS. El acta 187, punto `7.3`, contestando la
`P.3` del reporte de la 186: *"entra en la 187 y tambien los que nazcan en la
187, medido con la funcion devolviendo 0 al cerrar"*, y *"la bateria es la 189 y
quedan dos vueltas"*. Es la SEGUNDA vez seguida que una vuelta deja arneses fuera
y se lo dice a la siguiente.

CLON DECLARADO de `scripts/loop/vuelta186_tarea1b_nomina.py`. Cambia la lista
(de dos a seis), el nombre de la salida y las glosas. El cotejo del clon lo hace
`scripts/loop/cotejar_clon_declarado.py` y su salida se pega en el reporte con lo
que salga.

ESTE FICHERO NO ES UN ARNES DE MUTACION Y NO ENTRA EN LA NOMINA. Es la SALIDA
SELLADA de una tarea, y esa afirmacion SE MIDE aqui abajo en vez de dejarse
dicha: su nombre no casa con el patron de arneses de
`verificar_mutaciones_viejas.py`.

POR QUE LA DOBLE CORRIDA SE HACE HOY Y NO EN LA 189. La bateria corre cada arnes
DOS VECES y exige que su salida sea identica. El arnes
`vuelta182_tarea2_mutacion_apertura_auditor.py` fallo exactamente ahi en la 184,
porque su salida llevaba dentro el nombre de un directorio temporal. Comprobarlo
aqui es la unica forma de saber HOY si los seis van a sobrevivir.

LO QUE ESTE FICHERO ENSUCIA, DECLARADO Y MEDIDO EN VEZ DE PROMETIDO. Correr los
seis REESCRIBE sus seis salidas en `docs/loop/`. **Cuatro de ellas son evidencia
SELLADA de la vuelta 186**, y esta vuelta ha modificado `cerrar_reporte.py`, que
es el sujeto de las cuatro: sus salidas pueden moverse **aunque el veredicto siga
en VERDE**, porque publican NUMEROS DE LINEA del fichero que juzgan. Aqui se mide
el `sha256` ANTES y DESPUES de cada una y **se publica lo que salga**, con el
`git diff --numstat` de cada fichero al lado. **Lo que hace PARADA es que una
salida cambie ENTRE LAS DOS CORRIDAS DE HOY**, que es lo que significa "cambia
sola"; que se mueva respecto a la de la 186 tiene causa conocida y se declara.

NO SE PODA NADA. La opcion `c` de la parada del 5 sep 2026 quedo RECHAZADA por el
fundador. Aqui la nomina CRECE, que es lo contrario.

USO:
  python scripts/loop/vuelta187_tarea5a_nomina.py
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

LOS_SEIS = [
    ("scripts/loop/vuelta186_tarea2a_mutacion_pieza4.py",
     "docs/loop/SALIDA_V186_T2A_MUTACION_PIEZA4.txt", "de la 186"),
    ("scripts/loop/vuelta186_tarea2b_mutacion_pieza2_cercas.py",
     "docs/loop/SALIDA_V186_T2B_MUTACION_PIEZA2_CERCAS.txt", "de la 186"),
    ("scripts/loop/vuelta186_tarea2c_mutacion_cierre_tardio.py",
     "docs/loop/SALIDA_V186_T2C_MUTACION_CIERRE_TARDIO.txt", "de la 186"),
    ("scripts/loop/vuelta186_tarea2d_mutacion_seccion4.py",
     "docs/loop/SALIDA_V186_T2D_MUTACION_SECCION4.txt", "de la 186"),
    ("scripts/loop/vuelta187_tarea4_mutacion_dos_convenciones.py",
     "docs/loop/SALIDA_V187_T4_MUTACION_DOS_CONVENCIONES.txt", "NACE HOY"),
    ("scripts/loop/vuelta187_tarea5b_mutacion_seccion4_tardio.py",
     "docs/loop/SALIDA_V187_T5B_MUTACION_SECCION4_TARDIO.txt", "NACE HOY"),
]


def sha_de(ruta):
    """LAS DOS CONVENCIONES Y LOS DOS sha256 DE UN FICHERO, o None si no esta."""
    if not os.path.isfile(ruta):
        return None
    datos = io.open(ruta, "rb").read()
    lf = datos.replace(b"\r\n", b"\n")
    return (hashlib.sha256(datos).hexdigest(), hashlib.sha256(lf).hexdigest(),
            len(datos), len(lf))


def numstat(ruta_rel):
    """LAS FILAS DE `git diff --numstat` DE UNA RUTA, contadas."""
    r = subprocess.run(["git", "diff", "--numstat", "--", ruta_rel],
                       cwd=RAIZ, capture_output=True)
    return [l for l in r.stdout.decode("utf-8", errors="replace").splitlines()
            if l.strip()]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA 187, TAREA 5.a: LA NOMINA, Y LA DOBLE CORRIDA DE LOS SEIS")
    w("=" * 78)
    w("")

    w("A) LA NOMINA Y EL CENSO, RECOMPUTADOS AL CERRAR")
    censo = VMV.arneses_del_directorio()
    nomina = [s for s, _a in VMV.VIEJAS]
    w("   CIFRA censo: %d | CIFRA nomina AHORA: %d | VARA_DEL_CENSO: %d"
      % (len(censo), len(nomina), VMV.VARA_DEL_CENSO))
    ultima, faltan = VMV.arneses_que_faltan()
    w("   arneses_que_faltan(): ultima vuelta %s, FALTAN %d" % (ultima, len(faltan)))
    for n in faltan:
        w("      FALTA: %s" % n)
    invis = VMV.nomina_invisible_al_censo()
    w("   nomina_invisible_al_censo(): %d" % len(invis))
    for n in invis:
        w("      INVISIBLE: %s" % n)
    malas = VMV.guarda_del_sujeto_congelado()
    w("   guarda_del_sujeto_congelado(): %d entradas sin congelar" % len(malas))
    for nombre, veredicto, vive in malas:
        w("      SUJETO SIN CONGELAR: %-46s %s" % (nombre, veredicto))
    w("   LOS SEIS QUE ENTRAN, COMPROBADOS UNO A UNO DENTRO DE LA NOMINA:")
    dentro = set(nomina)
    n_dentro = 0
    for script, _sal, origen in LOS_SEIS:
        base = os.path.basename(script)
        esta = base in dentro
        n_dentro += 1 if esta else 0
        w("      %-52s %-9s en la nomina: %s" % (base, origen, "SI" if esta else "NO"))
    w("   CIFRA de los seis que estan dentro: %d de %d" % (n_dentro, len(LOS_SEIS)))
    w("   Y ESTE FICHERO NO ENTRA EN LA NOMINA, Y SE MIDE EN VEZ DE DECIRSE:")
    yo = os.path.basename(os.path.abspath(__file__))
    w("      %s esta en el censo de arneses: %s" % (yo, "SI" if yo in censo else "NO"))
    w("      %s esta en la nomina: %s" % (yo, "SI" if yo in dentro else "NO"))
    w("")

    w("B) LA DOBLE CORRIDA, EN PROCESOS APARTE, EXIGIENDO EL MISMO sha256")
    w("   (lo que hace PARADA es que una salida cambie ENTRE LAS DOS CORRIDAS DE")
    w("    HOY, que es lo que significa 'cambia sola'. Que se mueva respecto a la")
    w("    salida sellada de la 186 tiene causa conocida, esta vuelta toco")
    w("    cerrar_reporte.py, y se declara con su numstat al lado)")
    paradas = 0
    for script, salida, origen in LOS_SEIS:
        ruta_sal = os.path.join(RAIZ, salida.replace("/", os.sep))
        antes = sha_de(ruta_sal)
        w("   %s (%s)" % (script, origen))
        w("      salida: %s" % salida)
        w("      ANTES de correr: %s"
          % ("no existe" if antes is None
             else "disco %d bytes | LF %d bytes | sha256 LF %s"
                  % (antes[2], antes[3], antes[1])))
        shas = []
        for k in (1, 2):
            r = subprocess.run([PY, script], cwd=RAIZ, capture_output=True)
            s = sha_de(ruta_sal)
            shas.append(s)
            w("      CORRIDA %d: exitcode %d | %s"
              % (k, r.returncode,
                 "LA SALIDA NO EXISTE" if s is None
                 else "disco %d bytes | LF %d bytes | sha256 LF %s"
                      % (s[2], s[3], s[1])))
            if r.returncode != 0:
                w("         ROJO: el arnes no salio en verde. Se trae sin arreglar.")
                paradas += 1
        iguales = shas[0] is not None and shas[0] == shas[1]
        w("      LAS DOS CORRIDAS DAN EL MISMO sha256: %s" % ("SI" if iguales else "NO"))
        if not iguales:
            w("      PARADA: esta salida CAMBIA SOLA. Se trae sin arreglarla.")
            paradas += 1
        movio = (antes is not None and shas[1] is not None and antes[1] != shas[1])
        w("      SE MOVIO RESPECTO A LA SALIDA QUE HABIA: %s" % ("SI" if movio else "no"))
        filas = numstat(salida)
        w("      git diff --numstat -- %s : %d fila(s)" % (salida, len(filas)))
        for f in filas:
            w("         %s" % f)
    w("")
    w("   CIFRA paradas: %d" % paradas)
    w("")

    w("C) EL ESTADO DEL ARBOL DESPUES DE LA DOBLE CORRIDA")
    r = subprocess.run(["git", "diff", "--numstat", "--", "dataset/"],
                       cwd=RAIZ, capture_output=True)
    filas_ds = [l for l in r.stdout.decode("utf-8", errors="replace").splitlines()
                if l.strip()]
    w("   CIFRA filas de `git diff --numstat -- dataset/`: %d" % len(filas_ds))
    for f in filas_ds:
        w("      %s" % f)
    w("")

    ok = (len(faltan) == 0 and not invis and not malas
          and n_dentro == len(LOS_SEIS) and paradas == 0)
    w("VEREDICTO: %s" % ("VERDE" if ok else "ROJO"))
    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V187_T5A_NOMINA.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
