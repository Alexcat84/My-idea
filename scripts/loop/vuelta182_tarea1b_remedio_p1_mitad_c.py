# -*- coding: utf-8 -*-
r"""vuelta182_tarea1b_remedio_p1_mitad_c.py . LA TERCERA MITAD DEL REMEDIO DE LA
`P.1`, QUE APARECIO AL MEDIR Y NO ESTABA EN EL ENCARGO.

POR QUE EXISTE ESTE FICHERO APARTE Y NO SE METIO EN EL OTRO: porque el otro ya
corrio, ya renombro el arnes y ya dejo su salida sellada en
`docs/loop/SALIDA_V182_T1B_REMEDIO_P1.txt` (2.337 bytes). Meter esto alli seria
reescribir una salida ya publicada. Se escribe aparte y se declara.

QUE SE MIDIO DESPUES DE APLICAR EL REMEDIO, Y NO ES UNA SOSPECHA. Con el arnes ya
remediado y renombrado, se le metio en la nomina `VIEJAS` y
`guarda_del_sujeto_congelado()` lo saco como **NO DECIDIBLE**, que NO es verde y
que hace ROJA la corrida entera de la bateria. La corrida de ese veredicto:

    huellas de CONGELADO: tempfile, mkdtemp, git show, sha256
    huellas de SUJETO VIVO: REPORTE.md

La huella de sujeto vivo es el **bloque E**, que corre
`PASO0.exigir_archivado(171, ejecutar_archivador=False)` **contra el arbol de
HOY**, y la comprobacion de la `F` que lo juzga:

    ("y sigue mordiendo hoy, porque la 171 aun no esta archivada", ok_hoy is False)

**ES LA MISMA ESPECIE QUE EL ACTA 180 ADJUDICO EN SU `6.6`**: una expectativa
sobre el ESTADO DEL REPO y no sobre la CONDUCTA de la guarda. Y ademas HOY YA
PASA POR OTRO MOTIVO QUE EL QUE SU TEXTO DICE: su frase dice *"porque la 171 aun
no esta archivada"*, y `REPORTE_V171.md` **si esta archivada** (la archivo el
paso 0 del esqueleto de esta misma vuelta 182); sigue dando ROJO, pero por la
clausula `(d)`, porque el `REPORTE.md` del arbol es ahora el de la 182. **Una
comprobacion que pasa por un motivo distinto del que declara es verde y mal**, y
eso es `banco 9`.

EL REMEDIO, MITAD (c): EL BLOQUE E DEJA DE PREGUNTARLE AL ARBOL DE HOY Y PASA A
SER CONDUCTA SOBRE DOS ESCENARIOS FABRICADOS EN UN TEMPORAL:

  - ESCENARIO SIN ARCHIVO: el reporte de la 171 NO esta en el archivo. La guarda
    TIENE QUE MORDER.
  - ESCENARIO CON ARCHIVO: el mismo reporte SI esta, byte a byte. La guarda TIENE
    QUE DEJAR DE MORDER.

Eso es lo que el arnes siempre quiso decir, escrito de forma que no envejezca: la
guarda muerde cuando falta el archivo y deja de morder cuando esta. Y de paso
`REPORTE.md` deja de aparecer en la maquina, con lo que el veredicto de anclaje
pasa de `NO DECIDIBLE` a `CONGELADO` **por medicion y no por declaracion**: aqui
no se escribe la marca `SUJETO CONGELADO` para forzarlo. Escribirla habria sido
declarar congelado algo que seguia vivo, que es exactamente lo contrario de lo
que la guarda vigila.

EL BLOQUE E.2 SE CONSERVA ENTERO. Ese si es conducta: corre la guarda con OTRO
parametro para ensenar que muerde por otra clausula, y la discrepancia con el
auditor esta declarada ahi desde la 172. No se toca.

USO:
  python scripts/loop/vuelta182_tarea1b_remedio_p1_mitad_c.py --simular
  python scripts/loop/vuelta182_tarea1b_remedio_p1_mitad_c.py
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

V_E = '''    print("E) LA MISMA GUARDA CONTRA EL ARBOL DE HOY, CON LA 171 YA CERRADA")
    ok_hoy, informe_hoy = PASO0.exigir_archivado(
        VUELTA_ANTERIOR, ejecutar_archivador=False)
    for l in informe_hoy:
        print("   " + l)
    print("   VEREDICTO SOBRE EL ARBOL DE HOY: %s" % ("VERDE" if ok_hoy else "ROJO"))
    print("")'''

N_E = '''    print("E) LA CONDUCTA DE LA GUARDA, SOBRE DOS ESCENARIOS FABRICADOS")
    print("   (REMEDIO DE LA P.1, vuelta 182, mitad (c). ANTES este bloque corria la")
    print("    guarda CONTRA EL ARBOL DE HOY y la F juzgaba su resultado con la")
    print("    frase 'porque la 171 aun no esta archivada'. Esa frase dejo de ser")
    print("    cierta el dia que se archivo REPORTE_V171.md: la comprobacion seguia")
    print("    pasando, pero por la clausula (d) y no por la que decia. Verde y mal.")
    print("    Aqui se pregunta por CONDUCTA: muerde cuando falta y deja de morder")
    print("    cuando esta, sobre material fabricado que no envejece)")
    tmp2 = tempfile.mkdtemp(prefix="v172_conducta_")
    try:
        rep2 = os.path.join(tmp2, "el_reporte_del_escenario.md")
        io.open(rep2, "w", encoding="utf-8", newline=NL).write(rep_entonces)
        sin_arc = os.path.join(tmp2, "sin_archivo")
        con_arc = os.path.join(tmp2, "con_archivo")
        os.makedirs(sin_arc)
        os.makedirs(con_arc)
        io.open(os.path.join(con_arc, "REPORTE_V%d.md" % VUELTA_ANTERIOR), "w",
                encoding="utf-8", newline=NL).write(rep_entonces)
        ok_sin, inf_sin = PASO0.exigir_archivado(
            VUELTA_ANTERIOR, ruta_reporte=rep2, dir_archivo=sin_arc,
            ejecutar_archivador=False)
        ok_con, inf_con = PASO0.exigir_archivado(
            VUELTA_ANTERIOR, ruta_reporte=rep2, dir_archivo=con_arc,
            ejecutar_archivador=False)
        print("   ESCENARIO SIN ARCHIVO -> %s" % ("VERDE" if ok_sin else "ROJO"))
        for l in inf_sin:
            print("      " + l)
        print("   ESCENARIO CON ARCHIVO -> %s" % ("VERDE" if ok_con else "ROJO"))
        for l in inf_con:
            print("      " + l)
    finally:
        shutil.rmtree(tmp2, ignore_errors=True)
        print("   temporal borrado: %s" % (not os.path.exists(tmp2)))
    print("")'''

V_F = '''        ("y sigue mordiendo hoy, porque la 171 aun no esta archivada",
         ok_hoy is False),'''

N_F = '''        # REMEDIO DE LA P.1, vuelta 182, mitad (c). ANTES esta linea decia
        # `("y sigue mordiendo hoy, porque la 171 aun no esta archivada",
        # ok_hoy is False)`, y `ok_hoy` salia de correr la guarda CONTRA EL ARBOL
        # DE HOY. Cuando REPORTE_V171.md se archivo, la frase dejo de ser cierta
        # y la comprobacion siguio pasando por otra clausula: verde y mal. Ahora
        # son DOS comprobaciones de CONDUCTA sobre escenarios fabricados.
        ("muerde cuando el reporte NO esta en el archivo", ok_sin is False),
        ("y deja de morder cuando SI esta, byte a byte", ok_con is True),'''


def correr(ruta):
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run([sys.executable, ruta], cwd=RAIZ, capture_output=True, env=env)
    return (r.returncode,
            r.stdout.decode("utf-8", errors="replace")
            + r.stderr.decode("utf-8", errors="replace"))


def aplicar(texto):
    informe = []
    for viejo, nuevo, nombre in ((V_E, N_E, "(c) el bloque E pasa a ser conducta"),
                                 (V_F, N_F, "(c) la F juzga conducta y no el repo")):
        if viejo not in texto:
            informe.append("NO SE ENCUENTRA EL TROZO DE %s" % nombre)
            return None, informe
        texto = texto.replace(viejo, nuevo, 1)
        informe.append("APLICADO: %s" % nombre)
    return texto, informe


def veredicto_de_anclaje():
    sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
    import verificar_mutaciones_viejas as VMV
    importlib.reload(VMV)
    t = VMV.texto_del_arnes(os.path.basename(ARNES))
    return VMV.anclaje_de(t), VMV


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    salida = []
    w = salida.append
    w("VUELTA 182, TAREA 1.b: LA TERCERA MITAD DEL REMEDIO DE LA P.1")
    w("sujeto: %s" % ARNES)
    w("")

    p = os.path.join(RAIZ, ARNES.replace("/", os.sep))
    if not os.path.exists(p):
        w("ROJO: no esta el arnes. Se esperaba el nombre YA remediado.")
        print(NL.join(salida))
        return 1
    w("A) EL VEREDICTO DE ANCLAJE, ANTES")
    (ver, cong, vive), _V = veredicto_de_anclaje()
    w("   veredicto: %s" % ver)
    w("   huellas de CONGELADO: %s" % ", ".join(cong))
    w("   huellas de SUJETO VIVO: %s" % ", ".join(vive))
    w("   disco %d bytes" % os.path.getsize(p))
    c0, o0 = correr(ARNES)
    w("   CORRIDO ANTES -> EXITCODE %d" % c0)
    for l in o0.split(NL):
        if "CIFRA comprobaciones" in l:
            w("      | " + l.strip())
    w("")

    t = io.open(p, encoding="utf-8").read().replace(chr(13) + NL, NL)
    nuevo, informe = aplicar(t)
    w("B) EL PARCHE")
    for l in informe:
        w("   " + l)
    if nuevo is None:
        w("   ROJO: no se aplica.")
        print(NL.join(salida))
        return 1
    w("   pasa de %d a %d bytes en LF"
      % (len(t.encode("utf-8")), len(nuevo.encode("utf-8"))))
    w("")
    if a.simular:
        w("MODO --simular: no se escribe nada.")
        t2 = NL.join(salida) + NL
        ruta = os.path.join(LOOP, "SALIDA_V182_T1B_REMEDIO_P1_MITAD_C.txt")
        io.open(ruta, "w", encoding="utf-8", newline=NL).write(t2)
        print(t2)
        print("ESCRITO: %s (%d bytes)" % (ruta, len(t2.encode("utf-8"))))
        return 0

    io.open(p, "w", encoding="utf-8", newline=NL).write(nuevo)
    c1, o1 = correr(ARNES)
    w("C) EL ARNES, CORRIDO DESPUES")
    w("   EXITCODE %d" % c1)
    for l in o1.split(NL):
        if ("CIFRA comprobaciones" in l or "ESCENARIO SIN ARCHIVO" in l
                or "ESCENARIO CON ARCHIVO" in l
                or l.strip().startswith(("VERDE:", "ROJO:"))):
            w("      | " + l.strip()[:120])
    w("")

    w("D) EL VEREDICTO DE ANCLAJE, DESPUES, Y MEDIDO Y NO DECLARADO")
    (ver2, cong2, vive2), VMV = veredicto_de_anclaje()
    w("   veredicto: %s" % ver2)
    w("   huellas de CONGELADO: %s" % ", ".join(cong2))
    w("   huellas de SUJETO VIVO: %s" % ", ".join(vive2))
    w("   la marca %r NO se escribio en el arnes: %s"
      % (VMV.MARCA_DECLARA_CONGELADO,
         "CORRECTO" if VMV.MARCA_DECLARA_CONGELADO not in nuevo else "SE ESCRIBIO"))
    malas = VMV.guarda_del_sujeto_congelado()
    w("   guarda_del_sujeto_congelado(): %d sin congelar" % len(malas))
    for n, v, _x in malas:
        w("      SIN CONGELAR: %-52s %s" % (n, v))
    ultima, faltan = VMV.arneses_que_faltan()
    w("   arneses_que_faltan(): ultima %s, faltan %d" % (ultima, len(faltan)))
    for n in faltan:
        w("      FALTA: %s" % n)
    w("   nomina_invisible_al_censo(): %d" % len(VMV.nomina_invisible_al_censo()))
    w("   CIFRA censo: %d | CIFRA nomina: %d"
      % (len(VMV.arneses_del_directorio()), len(VMV.VIEJAS)))
    w("")
    w("VEREDICTO DE ESTA MITAD: %s"
      % ("VERDE" if (c1 == 0 and ver2 == "CONGELADO" and not malas and not faltan)
         else "ROJO"))

    t2 = NL.join(salida) + NL
    ruta = os.path.join(LOOP, "SALIDA_V182_T1B_REMEDIO_P1_MITAD_C.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t2)
    print(t2)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t2.encode("utf-8"))))
    return 0 if c1 == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
