# -*- coding: utf-8 -*-
r"""vuelta187_tarea4_mutacion_dos_convenciones.py . EL CASO POSITIVO POR MUTACION
DE LA GUARDA DE LAS DOS CONVENCIONES.

QUE PRUEBA, Y ES LA PRUEBA DE LA ESCALADA. `cerrar_reporte.py` publicaba en su
bloque D la linea `toda cifra de bytes y todo sha con su pareja SI`, y **las
cuatro cifras falsas de la `C.1` del acta 187 pasaron por delante de esa linea
sin encender nada**, porque la guarda vieja comprueba que la pareja EXISTA, no
que sea CIERTA. La guarda nueva **recomputa las DOS convenciones desde el disco**
y cae en ROJO si alguna de las dos publicadas discrepa.

EL ULTIMO CASO ES EL QUE DECIDE: si la guarda no caza las cuatro cifras del
texto real de `git show bb3aaad3:docs/loop/REPORTE.md`, **no sirve**, y este
arnes lo dice en vez de disimularlo.

TODAS LAS FUNCIONES QUE SE PRUEBAN SON PURAS Y SE LES PASA UN MAPA DE MEDICIONES
FABRICADO, salvo el ultimo caso, que usa el lector real porque su sujeto es el
texto real. **Ningun caso escribe en el repo.**

Y EL CASO ROJO SE PRUEBA POR MUTACION (`EJECUTOR.md` 1): cada comprobacion se
corre con su esperado y **despues con el esperado MUTADO**, y se exige que CAIGA.
Ningun `assert` de aqui compara dos constantes literales.

USO:
  python scripts/loop/vuelta187_tarea4_mutacion_dos_convenciones.py

--- SUJETO CONGELADO, DECLARADO EN LA VUELTA 195 (TAREA 3.c) ---

**LA HUELLA DE VIVO QUE LA GUARDA VE AQUI ES `REPORTE.md`, Y NUNCA ES EL FICHERO
DEL ARBOL DE TRABAJO:** todas sus apariciones en la maquina son parte de
`git show bb3aaad3:docs/loop/REPORTE.md`, o sea **el BLOB de un commit fijo**, con
el hash escrito en la constante `COMMIT_DE_LA_C1` de este mismo fichero.

**UN BLOB DE GIT NO SE MUEVE.** Es exactamente la especie de sujeto que
`HUELLAS_DE_CONGELADO` ya reconoce por `git show`, y el arnes la trae. Lo que le
faltaba era la DECLARACION que la regla pide cuando un texto trae huellas de las
dos especies, y va aqui.

**NO SE TOCA `docs/loop/REPORTE.md`** ni en lectura del arbol ni en escritura: la
ruta solo aparece detras de un `git show` con su commit delante.

"""
import io
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cerrar_reporte as CR   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
COMMIT_DE_LA_C1 = "bb3aaad3"
# LAS CUATRO RUTAS DE LA `C.1`. Van en una constante con nombre porque son un
# DATO DEL ACTA 187 y no un juicio de este fichero: el acta las lista en su
# seccion 8 con su tabla de sedes.
LAS_CUATRO_DE_LA_C1 = [
    "docs/loop/SALIDA_V186_COTEJO_DE_CLONES.txt",
    "docs/loop/SALIDA_V186_T2C_CERRAR_REPORTE_184.txt",
    "docs/loop/SALIDA_V186_T2C_ARCHIVAR_184_SIN_FORZAR.txt",
    "docs/loop/SALIDA_V186_T2C_ARCHIVAR_184.txt",
]


def texto_con(parrafo):
    """UN REPORTE DE MENTIRA con un parrafo dentro. NO toca el repo."""
    return NL.join([
        "# REPORTE DE LA VUELTA 999 (fabricado)", "",
        "**EL VEREDICTO DE UNA LINEA: de mentira.**", "",
        "## 3. UN APARTADO CUALQUIERA", "",
        parrafo, "",
    ]) + NL


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("CASO POSITIVO POR MUTACION de la guarda de LAS DOS CONVENCIONES")
    w("(vuelta 187, TAREA 4; operacion de codigo de la escalada de AUDITOR.md 1.2)")
    w("")
    fallos = 0

    w("CASO 1. LAS DOS CONVENCIONES CALZANDO: VERDE.")
    t1 = texto_con("La salida vive en `docs/loop/UNA.txt` (**120 bytes en disco y "
                   "110 bytes normalizados a LF**).")
    med_ok = {"docs/loop/UNA.txt": (120, 110)}
    r1 = CR.convenciones_que_no_calzan(t1, med_ok)
    w("   parejas halladas: %d" % len(CR.parejas_publicadas(t1)))
    w("   CIFRA que no calzan: %d (esperado 0)" % len(r1))
    w("   VEREDICTO: %s" % ("VERDE" if not r1 else "ROJO"))
    w("   con el esperado MUTADO (se exige 1 que no calce): %s"
      % ("PASA" if len(r1) == 1 else "CAE"))
    if r1 or len(r1) == 1:
        fallos += 1
    w("")

    w("CASO 2. LA CIFRA DE LF MUTADA: ROJO, Y TIENE QUE NOMBRAR LF.")
    med_lf = {"docs/loop/UNA.txt": (120, 999)}
    r2 = CR.convenciones_que_no_calzan(t1, med_lf)
    w("   CIFRA que no calzan: %d (esperado 1)" % len(r2))
    for f in r2:
        w("      linea %-4d %-24s %-5s publicada %-6d medida %-6d | %s" % f)
    nombra_lf = len(r2) == 1 and r2[0][2] == "LF"
    w("   NOMBRA LA CONVENCION QUE FALLA, Y ES LF: %s" % ("SI" if nombra_lf else "NO"))
    w("   NOMBRA LA RUTA: %s"
      % ("SI" if r2 and r2[0][1] == "docs/loop/UNA.txt" else "NO"))
    w("   NOMBRA LA PUBLICADA Y LA MEDIDA: %s"
      % ("SI, %d contra %d" % (r2[0][3], r2[0][4]) if r2 else "NO"))
    w("   con el esperado MUTADO (se exige que sea DISCO): %s"
      % ("PASA" if r2 and r2[0][2] == "DISCO" else "CAE"))
    if not nombra_lf or (r2 and r2[0][2] == "DISCO"):
        fallos += 1
    w("")

    w("CASO 3. LA CIFRA DE DISCO MUTADA: ROJO, Y TIENE QUE NOMBRAR DISCO.")
    med_d = {"docs/loop/UNA.txt": (777, 110)}
    r3 = CR.convenciones_que_no_calzan(t1, med_d)
    w("   CIFRA que no calzan: %d (esperado 1)" % len(r3))
    for f in r3:
        w("      linea %-4d %-24s %-5s publicada %-6d medida %-6d | %s" % f)
    nombra_disco = len(r3) == 1 and r3[0][2] == "DISCO"
    w("   NOMBRA LA CONVENCION QUE FALLA, Y ES DISCO: %s"
      % ("SI" if nombra_disco else "NO"))
    w("   con el esperado MUTADO (se exige que sea LF): %s"
      % ("PASA" if r3 and r3[0][2] == "LF" else "CAE"))
    if not nombra_disco or (r3 and r3[0][2] == "LF"):
        fallos += 1
    w("")

    w("CASO 4. UNA RUTA CON CRLF REAL EN DISCO, DONDE LAS DOS CIFRAS SON")
    w("   LEGITIMAMENTE DISTINTAS: VERDE. ES EL CASO QUE IMPIDE QUE LA GUARDA")
    w("   EXIJA QUE LAS DOS SEAN IGUALES, que seria el error facil de escribir")
    w("   aqui y dejaria en rojo a la mitad de los reportes de esta casa.")
    t4 = texto_con("El cotejo esta en `docs/loop/CRLF.txt` (**49804 bytes en disco "
                   "y 49036 bytes normalizados a LF**).")
    med_crlf = {"docs/loop/CRLF.txt": (49804, 49036)}
    r4 = CR.convenciones_que_no_calzan(t4, med_crlf)
    w("   publicadas: disco 49804 y LF 49036, DISTINTAS entre si")
    w("   CIFRA que no calzan: %d (esperado 0)" % len(r4))
    w("   VEREDICTO: %s" % ("VERDE" if not r4 else "ROJO"))
    w("   con el esperado MUTADO (se exige que caiga por ser distintas): %s"
      % ("PASA" if r4 else "CAE"))
    if r4:
        fallos += 1
    w("")

    w("CASO 5. UNA CIFRA PUBLICADA SIN PAREJA: SIGUE SIENDO EL ROJO DE HOY, CON")
    w("   SU TEXTO DE HOY, Y NO EL DE ESTA GUARDA. Las dos son especies distintas")
    w("   y ninguna pisa a la otra.")
    t5 = texto_con("La salida vive en `docs/loop/SOLA.txt` (**333 bytes**).")
    r5_vieja = CR.cifras_sin_pareja(t5)
    r5_nueva = CR.convenciones_que_no_calzan(t5, {"docs/loop/SOLA.txt": (333, 333)})
    w("   cifras_sin_pareja() -> %d (esperado 1, y es SU rojo)" % len(r5_vieja))
    for n, especie, muestra, linea in r5_vieja:
        w("      linea %-4d %-5s %-8s | %s" % (n, especie, muestra, linea[:80]))
    w("   convenciones_que_no_calzan() -> %d (esperado 0: no hay pareja que cotejar)"
      % len(r5_nueva))
    ok5 = (len(r5_vieja) == 1 and len(r5_nueva) == 0)
    w("   CADA GUARDA EN SU SITIO: %s" % ("SI" if ok5 else "NO"))
    w("   con el esperado MUTADO (que la nueva tambien la acuse): %s"
      % ("PASA" if r5_nueva else "CAE"))
    if not ok5 or r5_nueva:
        fallos += 1
    w("")

    w("CASO 5.1. UNA RUTA QUE NO EXISTE EN DISCO: SIGUE SIENDO EL ROJO QUE YA ES")
    w("   (el de vuelta186_rutas_del_reporte.py), Y ESTA GUARDA NO LO DUPLICA.")
    t51 = texto_con("La salida vive en `docs/loop/NO_EXISTE_JAMAS.txt` (**10 bytes "
                    "en disco y 10 bytes normalizados a LF**).")
    r51 = CR.convenciones_que_no_calzan(t51, {"docs/loop/NO_EXISTE_JAMAS.txt": None})
    w("   CIFRA que no calzan: %d (esperado 0: sin medicion no se acusa)" % len(r51))
    w("   y el lector real la mide como: %r"
      % (CR.mediciones_de_las_rutas(t51).get("docs/loop/NO_EXISTE_JAMAS.txt"),))
    w("   con el esperado MUTADO (que esta guarda tambien la acuse): %s"
      % ("PASA" if r51 else "CAE"))
    if r51:
        fallos += 1
    w("")

    w("CASO 6. EL QUE DECIDE: EL TEXTO REAL DE `git show %s:docs/loop/REPORTE.md`."
      % COMMIT_DE_LA_C1)
    w("   SE EXIGE QUE LA GUARDA HABRIA CAZADO LAS CUATRO CIFRAS DE LA `C.1`,")
    w("   NOMBRADAS UNA A UNA. Si no caza el caso que la trajo, no sirve.")
    r = subprocess.run(["git", "show", "%s:docs/loop/REPORTE.md" % COMMIT_DE_LA_C1],
                       cwd=RAIZ, capture_output=True)
    t6 = r.stdout.decode("utf-8", errors="replace")
    if r.returncode != 0 or not t6.strip():
        w("   ROJO: no se pudo leer el texto de %s. Sin sujeto no hay caso."
          % COMMIT_DE_LA_C1)
        fallos += 1
    else:
        w("   el texto mide %d bytes y %d lineas"
          % (len(t6.encode("utf-8")), t6.count(NL)))
        med6 = CR.mediciones_de_las_rutas(t6)
        r6 = CR.convenciones_que_no_calzan(t6, med6)
        w("   CIFRA parejas de convenciones publicadas: %d"
          % len(CR.parejas_publicadas(t6)))
        w("   CIFRA que NO calzan: %d" % len(r6))
        for n, ruta, cual, pub, med, forma in r6:
            w("      linea %-5d %-56s %-5s publicada %-8d medida %-8d | %s"
              % (n, ruta, cual, pub, med, forma))
        cazadas = sorted({ruta for _n, ruta, _c, _p, _m, _f in r6})
        w("   LAS RUTAS CAZADAS, DISTINTAS: %d" % len(cazadas))
        for x in cazadas:
            w("      %s" % x)
        faltan = [x for x in LAS_CUATRO_DE_LA_C1 if x not in cazadas]
        sobran = [x for x in cazadas if x not in LAS_CUATRO_DE_LA_C1]
        w("   DE LAS CUATRO DE LA `C.1`, FALTAN POR CAZAR: %s"
          % (", ".join(faltan) or "(ninguna)"))
        conv_de_las_cuatro = [c for _n, ru, c, _p, _m, _f in r6
                              if ru in LAS_CUATRO_DE_LA_C1]
        w("   LA CONVENCION QUE FALLA EN LAS CUATRO ES LF, Y NO DISCO: %s"
          % ("SI" if conv_de_las_cuatro
             and all(c == "LF" for c in conv_de_las_cuatro) else "NO"))
        w("   CAZA ADEMAS: %s" % (", ".join(sobran) or "(ninguna)"))
        # QUE UNA RUTA DE MAS SEA UN ROJO INVENTADO NO SE SUPONE: SE MIDE.
        # Una ruta que la guarda acusa hoy y que NO estaba en la `C.1` es un
        # rojo LEGITIMO si el fichero HA CAMBIADO desde `bb3aaad3`, porque
        # entonces la cifra que aquel reporte publico ya no es cierta. Solo es
        # INVENTADO si el fichero sigue byte a byte como estaba y aun asi se
        # acusa. La primera version de este caso exigia CERO de mas y salio en
        # ROJO en cuanto otra tarea de esta misma vuelta movio un fichero; su
        # corrida entera vive en
        # `docs/loop/SALIDA_V187_T4_MUTACION_EN_ROJO.txt`.
        inventados = []
        for x in sobran:
            r_old = subprocess.run(
                ["git", "show", "%s:%s" % (COMMIT_DE_LA_C1, x)],
                cwd=RAIZ, capture_output=True)
            viejo_b = r_old.stdout if r_old.returncode == 0 else None
            p_hoy = os.path.join(RAIZ, x.replace("/", os.sep))
            hoy_b = io.open(p_hoy, "rb").read() if os.path.isfile(p_hoy) else None
            cambio = (viejo_b is None or hoy_b is None or viejo_b != hoy_b)
            w("      %s -> en %s %s | hoy %s | HA CAMBIADO: %s"
              % (x, COMMIT_DE_LA_C1,
                 ("%d bytes" % len(viejo_b)) if viejo_b is not None else "NO ESTA",
                 ("%d bytes" % len(hoy_b)) if hoy_b is not None else "NO EXISTE",
                 "SI" if cambio else "NO"))
            if not cambio:
                inventados.append(x)
        w("   CIFRA rutas de mas que serian ROJO INVENTADO (mismo fichero que en")
        w("   %s y aun asi acusado): %d" % (COMMIT_DE_LA_C1, len(inventados)))
        ok6 = (not faltan and not inventados and conv_de_las_cuatro
               and all(c == "LF" for c in conv_de_las_cuatro))
        w("   HABRIA CAZADO LAS CUATRO, POR LF, Y SIN INVENTAR NINGUNA: %s"
          % ("SI" if ok6 else "NO"))
        w("   con el esperado MUTADO (que cazara CERO): %s"
          % ("PASA" if not r6 else "CAE"))
        w("   con el esperado MUTADO (exigir que la convencion sea DISCO): %s"
          % ("PASA" if conv_de_las_cuatro
             and all(c == "DISCO" for c in conv_de_las_cuatro) else "CAE"))
        if not ok6 or not r6:
            fallos += 1
        w("")
        w("   Y LA GUARDA VIEJA SOBRE EL MISMO TEXTO, PARA QUE SE VEA EL HUECO QUE")
        w("   ESTA ESCALADA CIERRA: cifras_sin_pareja() sobre las CUATRO lineas que")
        w("   la `C.1` publico da lo siguiente.")
        lineas6 = t6.replace(chr(13) + NL, NL).split(NL)
        huerf = {n for n, _e, _m, _l in CR.cifras_sin_pareja(t6)}
        for n, ruta, cual, pub, med, forma in r6:
            w("      linea %-5d %-56s | la guarda VIEJA la acusa: %s"
              % (n, ruta, "SI" if n in huerf else "NO"))
        vistas = sorted({n for n, _r, _c, _p, _m, _f in r6})
        acusadas_viejas = len([n for n in vistas if n in huerf])
        w("   CIFRA de esas lineas que la guarda VIEJA acusaba: %d de %d"
          % (acusadas_viejas, len(vistas)))
        w("   (si esa cifra es 0, queda medido que las cuatro pasaron por delante")
        w("    de la linea `con su pareja SI` sin encender nada)")
        del lineas6
    w("")

    w("CIFRA casos: 7")
    w("CIFRA fallos: %d" % fallos)
    w("VEREDICTO: %s" % ("VERDE" if fallos == 0 else "ROJO"))
    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V187_T4_MUTACION_DOS_CONVENCIONES.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0 if fallos == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
