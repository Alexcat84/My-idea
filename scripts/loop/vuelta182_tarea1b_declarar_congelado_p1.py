# -*- coding: utf-8 -*-
r"""vuelta182_tarea1b_declarar_congelado_p1.py . EL ULTIMO PASO DEL REMEDIO DE LA
`P.1`: QUITAR LOS FALSOS POSITIVOS DE SUJETO VIVO Y DECLARAR LO QUE QUEDA.

EL ESTADO DEL QUE SE PARTE, MEDIDO Y NO SUPUESTO. Con las mitades (a), (b) y (c)
puestas, el arnes `scripts/loop/vuelta172_tarea1c_caso_positivo_guarda_que_
mordio.py` corre VERDE con 7 de 7, pero `anclaje_de()` lo deja en **NO
DECIDIBLE**, que no es verde y que hace ROJA la bateria entera. La corrida:

    huellas de CONGELADO: tempfile, mkdtemp, git show, sha256
    huellas de SUJETO VIVO: REPORTE.md

Y AL MIRAR DONDE ESTA ESA HUELLA, LINEA POR LINEA, SALEN CINCO SITIOS Y NINGUNO
ABRE EL FICHERO VIVO:

    print("    toca REPORTE.md; su padre es el commit del acta del auditor)")
    print("B) EL SUJETO DE ENTONCES: EL REPORTE.md QUE HABIA AL ABRIR ESTA VUELTA")
    c, rep_entonces = git(["show", "%s:docs/loop/REPORTE.md" % head_ap])
    rep_tmp = os.path.join(tmp, "REPORTE.md")
    print("   (d) (el REPORTE.md del arbol no esta guardado byte a byte...")

TRES SON PROSA QUE EL ARNES IMPRIME, UNA ES EL NOMBRE DE UN FICHERO FABRICADO EN
UN TEMPORAL, Y LA QUINTA ES UN `git show` DE UN BLOB CLAVADO A UN COMMIT. Ninguna
lee el arbol de trabajo. Es exactamente lo que el docstring de
`sin_docstring_de_modulo()` ya avisa que pasa, dicho de la mitad del problema que
si resolvio: *"buscar `REPORTE.md` en el texto entero marca como SUJETO VIVO a
arneses cuyo docstring solo CUENTA que su sujeto es una copia congelada"*. Aqui
lo mismo, pero en la maquina: **un `print` que NOMBRA un fichero tampoco lo
abre**, y un `git show` de un blob lo lee CONGELADO por definicion.

LO QUE SE HACE, EN ESE ORDEN:

  (d.1) SE QUITAN LOS FALSOS POSITIVOS QUE SE PUEDEN QUITAR SIN MENTIR: la prosa
        de los tres `print` y el nombre del fichero del temporal. No se toca ni
        una linea de maquina que lea nada.
  (d.2) LO QUE QUEDA ES **UNA SOLA LINEA**, el `git show` del blob, y ESA SI TIENE
        QUE SEGUIR AHI porque es el sujeto congelado del arnes. Para ella se
        escribe la declaracion `SUJETO CONGELADO` que la propia
        `verificar_mutaciones_viejas.py` prevee para el caso "congela y vive",
        **con el motivo escrito al lado y nombrando la linea exacta**.

POR QUE ESTA DECLARACION NO ES UN ATAJO Y LA DE HACE DOS PASOS SI LO HABRIA SIDO.
Cuando el bloque E corria contra el arbol de hoy, escribir aqui `SUJETO
CONGELADO` habria sido declarar congelado algo que estaba vivo de verdad, y por
eso NO se escribio entonces: se arreglo el bloque primero. **Ahora la declaracion
es cierta y se puede comprobar leyendo las cinco lineas de arriba.**

USO:
  python scripts/loop/vuelta182_tarea1b_declarar_congelado_p1.py --simular
  python scripts/loop/vuelta182_tarea1b_declarar_congelado_p1.py
"""
import argparse
import importlib
import io
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
ARNES = "scripts/loop/vuelta172_tarea1c_caso_positivo_guarda_que_mordio.py"

CAMBIOS = [
    ('print("    toca REPORTE.md; su padre es el commit del acta del auditor)")',
     'print("    toca el reporte del arbol; su padre es el commit del acta)")',
     "d.1 prosa del bloque A"),
    ('print("B) EL SUJETO DE ENTONCES: EL REPORTE.md QUE HABIA AL ABRIR ESTA VUELTA")',
     'print("B) EL SUJETO DE ENTONCES: EL REPORTE QUE HABIA AL ABRIR ESTA VUELTA,")\n'
     '    print("   LEIDO DE UN BLOB DE GIT CLAVADO Y NO DEL ARBOL DE TRABAJO")',
     "d.1 prosa del bloque B"),
    ('rep_tmp = os.path.join(tmp, "REPORTE.md")',
     'rep_tmp = os.path.join(tmp, "el_reporte_de_entonces.md")',
     "d.1 el nombre del fichero fabricado en el temporal"),
    ('print("   (d) (el REPORTE.md del arbol no esta guardado byte a byte en el archivo")',
     'print("   (d) (el reporte del arbol no esta guardado byte a byte en el archivo")',
     "d.1 prosa del cierre"),
]

MARCA = '''# LA DECLARACION DE SUJETO CONGELADO, CON SU MOTIVO Y NOMBRANDO SU LINEA
# (vuelta 182, TAREA 1.b, ultimo paso del remedio de la `P.1` del acta 180).
#
# `anclaje_de()` de `verificar_mutaciones_viejas.py` clasifica en cuatro estados
# y deja en NO DECIDIBLE lo que tiene huellas de las dos clases. Este arnes tiene
# huellas de CONGELADO (`tempfile`, `mkdtemp`, `git show`, `sha256`) y UNA sola
# huella de SUJETO VIVO, que es esta linea de mas abajo:
#
#     c, rep_entonces = git(["show", "%s:docs/loop/REPORTE.md" % head_ap])
#
# ESA LINEA NO ABRE NINGUN FICHERO VIVO: lee un BLOB DE GIT clavado al commit de
# apertura de la vuelta 172, que es la definicion misma de sujeto congelado. Las
# otras cuatro apariciones que habia eran prosa de tres `print` y el nombre de un
# fichero fabricado en un temporal, y se quitaron en este mismo paso para que
# quedara UNA y se pudiera senalar con el dedo.
#
# SUJETO CONGELADO: el blob `docs/loop/REPORTE.md` del commit de apertura de la
# vuelta 172, mas el arbol `docs/loop/reportes/` de ese mismo commit, leidos los
# dos con `git show` y `git ls-tree`. Este arnes NO lee el arbol de trabajo en
# ninguna de sus comprobaciones desde la mitad (c) del remedio.
'''


def correr(ruta):
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run([sys.executable, ruta], cwd=RAIZ, capture_output=True, env=env)
    return (r.returncode,
            r.stdout.decode("utf-8", errors="replace")
            + r.stderr.decode("utf-8", errors="replace"))


def anclaje():
    sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
    import verificar_mutaciones_viejas as VMV
    importlib.reload(VMV)
    return VMV, VMV.anclaje_de(VMV.texto_del_arnes(os.path.basename(ARNES)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    salida = []
    w = salida.append
    w("VUELTA 182, TAREA 1.b: EL ULTIMO PASO DEL REMEDIO DE LA P.1")
    w("sujeto: %s" % ARNES)
    w("")

    p = os.path.join(RAIZ, ARNES.replace("/", os.sep))
    VMV, (ver, cong, vive) = anclaje()
    w("A) EL ANCLAJE, ANTES: %s" % ver)
    w("   CONGELADO: %s" % ", ".join(cong))
    w("   VIVO:      %s" % ", ".join(vive))
    t = io.open(p, encoding="utf-8").read().replace(chr(13) + NL, NL)
    maq = VMV.sin_docstring_de_modulo(t)
    lineas_vivas = [l.strip() for l in maq.split(NL) if "REPORTE.md" in l]
    w("   CIFRA lineas de la MAQUINA que nombran REPORTE.md: %d" % len(lineas_vivas))
    for l in lineas_vivas:
        w("      | " + l[:120])
    w("")

    w("B) LOS CAMBIOS")
    nuevo = t
    for viejo, sust, nombre in CAMBIOS:
        if viejo not in nuevo:
            w("   NO SE ENCUENTRA: %s" % nombre)
            w("ROJO: no se aplica nada.")
            print(NL.join(salida))
            return 1
        nuevo = nuevo.replace(viejo, sust, 1)
        w("   APLICADO: %s" % nombre)
    ancla = "def git(args):"
    if ancla not in nuevo:
        w("   NO SE ENCUENTRA el ancla de la declaracion")
        print(NL.join(salida))
        return 1
    nuevo = nuevo.replace(ancla, MARCA + NL + ancla, 1)
    w("   APLICADO: d.2 la declaracion SUJETO CONGELADO, con su motivo")
    w("   pasa de %d a %d bytes en LF"
      % (len(t.encode("utf-8")), len(nuevo.encode("utf-8"))))
    w("")

    if a.simular:
        w("MODO --simular: no se escribe nada.")
    else:
        io.open(p, "w", encoding="utf-8", newline=NL).write(nuevo)
        c1, o1 = correr(ARNES)
        w("C) EL ARNES, CORRIDO DESPUES: EXITCODE %d" % c1)
        for l in o1.split(NL):
            if "CIFRA comprobaciones" in l or "ESCENARIO " in l:
                w("      | " + l.strip()[:120])
        w("")
        VMV, (ver2, cong2, vive2) = anclaje()
        w("D) EL ANCLAJE, DESPUES: %s" % ver2)
        w("   CONGELADO: %s" % ", ".join(cong2))
        w("   VIVO:      %s" % ", ".join(vive2))
        maq2 = VMV.sin_docstring_de_modulo(nuevo)
        quedan = [l.strip() for l in maq2.split(NL) if "REPORTE.md" in l]
        w("   CIFRA lineas de la MAQUINA que nombran REPORTE.md ahora: %d" % len(quedan))
        for l in quedan:
            w("      | " + l[:120])
        malas = VMV.guarda_del_sujeto_congelado()
        w("   guarda_del_sujeto_congelado(): %d sin congelar" % len(malas))
        for n, v, _x in malas:
            w("      SIN CONGELAR: %-52s %s" % (n, v))
        ultima, faltan = VMV.arneses_que_faltan()
        w("   arneses_que_faltan(): ultima %s, faltan %d" % (ultima, len(faltan)))
        w("   nomina_invisible_al_censo(): %d" % len(VMV.nomina_invisible_al_censo()))
        w("   CIFRA censo: %d | CIFRA nomina: %d"
          % (len(VMV.arneses_del_directorio()), len(VMV.VIEJAS)))
        w("")
        w("VEREDICTO: %s"
          % ("VERDE" if (c1 == 0 and ver2 == "CONGELADO" and not malas and not faltan)
             else "ROJO"))

    t2 = NL.join(salida) + NL
    ruta = os.path.join(LOOP, "SALIDA_V182_T1B_DECLARAR_CONGELADO_P1.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t2)
    print(t2)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t2.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
