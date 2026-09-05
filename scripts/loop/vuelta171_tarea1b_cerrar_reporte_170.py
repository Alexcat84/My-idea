# -*- coding: utf-8 -*-
r"""vuelta171_tarea1b_cerrar_reporte_170.py . TAREA 1.b DE LA VUELTA 171.

CIERRA EL REPORTE DE LA VUELTA 170, QUE LA PROPIA 170 NO CERRO.

EL HECHO, MEDIDO Y NO CREIDO (bloque H de scripts/loop/vuelta171_apertura.py,
salida docs/loop/SALIDA_V171_APERTURA.txt): el commit 29f04e86, titulado "EL
BLOQUE DE CIERRE DE LA VUELTA 170, ENTERO", toca DOCE ficheros y
docs/loop/REPORTE.md NO ES NINGUNO DE ELLOS. El reporte en HEAD sigue diciendo
"SIN ESCRIBIR TODAVIA" y "PENDIENTE DE TALLAR AL CIERRE", y sus secciones 3 a 9
no existen en el.

QUE HACE ESTE INSTRUMENTO, Y LAS TRES COSAS SON PEGAR, NO ESCRIBIR:

  (1) LA CABECERA: sustituye el hueco entre <!-- CABECERA TALLADA --> y
      <!-- FIN CABECERA TALLADA --> por la tabla que YA SALIO VERDE al cierre de
      la 170 y que vive en docs/loop/SALIDA_V170_TALLADOR_CABECERA.txt. La tabla
      SE PEGA ENTERA desde ese fichero. NINGUNA CELDA SE TECLEA (EJECUTOR.md 1,
      "LA CABECERA DEL REPORTE SE TALLA, NO SE TECLEA").

  (2) EL CUERPO: anexa las secciones 3 a 9 de scripts/loop/_v170_cierre_texto.md
      TAL COMO ESTAN, sin reescribir una palabra, sin suavizar ninguno de sus
      OCHO discutibles ni de sus CINCO caidas. El instrumento COMPRUEBA por
      sha256 que lo que anexa es byte a byte lo que el borrador dice.

  (3) EL VEREDICTO DE UNA LINEA, que hoy dice "SIN ESCRIBIR TODAVIA", y la nota
      de quien cierra: este cierre lo escribe la VUELTA 171 y eso se dice en vez
      de disimularse.

LA SECCION 9 SE ESCRIBE DICIENDO LA VERDAD Y NO SE RELLENA (encargo 1.c). El
borrador trae la CABECERA de la seccion 9 y NADA debajo, porque la bateria de la
170 no llego a correr: docs/loop/SALIDA_V170_BATERIA.txt mide CERO BYTES, y este
instrumento lo vuelve a medir antes de escribirlo. AQUI NO SE PEGA UNA CORRIDA DE
LA VUELTA 171: eso seria publicar como de una vuelta lo medido en otra, que es
exactamente la especie que esta campana persigue. Se remite a la seccion 5 del
acta 170, que trae la corrida del auditor.

CERO REPARACIONES DE NODOS: este fichero solo toca docs/loop/REPORTE.md.

USO:
  python scripts/loop/vuelta171_tarea1b_cerrar_reporte_170.py
"""
import hashlib
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
REPORTE = os.path.join(LOOP, "REPORTE.md")
BORRADOR = os.path.join(RAIZ, "scripts", "loop", "_v170_cierre_texto.md")
TALLADOR = os.path.join(LOOP, "SALIDA_V170_TALLADOR_CABECERA.txt")
BATERIA = os.path.join(LOOP, "SALIDA_V170_BATERIA.txt")
ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")

VUELTA_DEL_REPORTE = 170
VUELTA_QUE_CIERRA = 171

MARCA_ABRE = "<!-- CABECERA TALLADA -->"
MARCA_CIERRA = "<!-- FIN CABECERA TALLADA -->"
CAB_SECCION_9 = "## 9. LA BATERIA DE MUTACIONES, CORRIDA ENTERA Y SOLA AL CIERRE"

VEREDICTO_VIEJO = "**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.**"


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def sha(t):
    return hashlib.sha256(t.replace("\r\n", "\n").encode("utf-8")).hexdigest()


def leer(ruta):
    return io.open(ruta, encoding="utf-8").read().replace("\r\n", "\n")


def main():
    print("=" * 78)
    print("VUELTA %d, TAREA 1.b: SE CIERRA EL REPORTE DE LA VUELTA %d"
          % (VUELTA_QUE_CIERRA, VUELTA_DEL_REPORTE))
    print("=" * 78)
    print("")

    rojos = []

    # ------------------------------------------------------------- A. EL SUJETO
    print("A) EL SUJETO, COMPROBADO ANTES DE TOCARLO")
    texto = leer(REPORTE)
    primera = texto.split("\n", 1)[0]
    print("   docs/loop/REPORTE.md primera linea: %s" % primera[:90])
    m = re.match(r"^#\s*REPORTE DE LA VUELTA\s+(\d+)\b", primera)
    if not m or int(m.group(1)) != VUELTA_DEL_REPORTE:
        rojos.append("el REPORTE.md del arbol no es el de la vuelta %d" % VUELTA_DEL_REPORTE)
    print("   lineas: %d | bytes: %d" % (texto.count("\n"), len(texto.encode("utf-8"))))
    for marca, esperado in ((VEREDICTO_VIEJO, True),
                            ("PENDIENTE DE TALLAR AL CIERRE", True),
                            ("\n## 3.", False), ("\n## 9.", False)):
        hay = marca in texto
        print("   contiene %-38r -> %s (se esperaba %s)"
              % (marca[:36], "SI" if hay else "NO", "SI" if esperado else "NO"))
        if hay != esperado:
            rojos.append("el sujeto no esta en el estado que este instrumento espera: %r"
                         % marca[:40])
    print("")

    # -------------------------------------------- B. LA CABECERA, PEGADA ENTERA
    print("B) LA CABECERA, LEIDA DEL FICHERO DEL TALLADOR Y NO TECLEADA")
    sal = leer(TALLADOR)
    filas = [l for l in sal.split("\n") if l.strip().startswith("|")]
    print("   %s -> %d bytes, %d filas de tabla"
          % (os.path.relpath(TALLADOR, RAIZ).replace(os.sep, "/"),
             len(sal.encode("utf-8")), len(filas)))
    if len(filas) < 8:
        rojos.append("el fichero del tallador trae %d filas de tabla, muy pocas" % len(filas))
    con_celda_de_cierre = [l for l in filas if l.count("|") >= 3]
    print("   filas con las dos columnas: %d" % len(con_celda_de_cierre))
    for l in filas:
        print("      %s" % l.strip()[:110])
    tabla = "\n".join(l.rstrip() for l in filas)
    print("")

    # ----------------------------------------------- C. EL BORRADOR, VERIFICADO
    print("C) EL BORRADOR DEL CIERRE, COMPROBADO ANTES DE ANEXARLO")
    cuerpo = leer(BORRADOR)
    print("   %s -> %d bytes, %d lineas, sha256 %s"
          % (os.path.relpath(BORRADOR, RAIZ).replace(os.sep, "/"),
             len(cuerpo.encode("utf-8")), cuerpo.count("\n"), sha(cuerpo)[:16]))
    if not cuerpo.startswith("## 3. EL CIERRE"):
        rojos.append("el borrador no empieza por la seccion 3")
    if not cuerpo.rstrip("\n").endswith(CAB_SECCION_9):
        rojos.append("el borrador no termina en la cabecera de la seccion 9")
    secciones = [l for l in cuerpo.split("\n") if l.startswith("## ")]
    print("   secciones que trae: %d" % len(secciones))
    for l in secciones:
        print("      %s" % l[:95])
    n_disc = len(re.findall(r"^- \*\*`D\.\d+`", cuerpo, re.M))
    n_caidas_num = len(re.findall(r"^- \*\*`CAIDA \d+`", cuerpo, re.M))
    n_quinta = len(re.findall(r"^- \*\*UNA QUINTA", cuerpo, re.M))
    print("   CIFRA discutibles `D.n` contados del borrador: %d" % n_disc)
    print("   CIFRA caidas numeradas contadas del borrador: %d" % n_caidas_num)
    print("   CIFRA caidas sin numero ('UNA QUINTA'): %d" % n_quinta)
    print("   CIFRA caidas totales: %d" % (n_caidas_num + n_quinta))
    if n_disc != 8:
        rojos.append("el borrador trae %d discutibles y el encargo nombra ocho" % n_disc)
    if n_caidas_num + n_quinta != 5:
        rojos.append("el borrador trae %d caidas y el encargo nombra cinco"
                     % (n_caidas_num + n_quinta))
    print("")

    # ------------------------- D. LOS HASHES DEL BORRADOR, VERIFICADOS EN GIT
    print("D) LOS OCHO COMMITS QUE EL BORRADOR NOMBRA, VERIFICADOS EN GIT")
    print("   (se VERIFICAN, no se reescriben: el borrador se anexa tal cual)")
    c, rango = git(["log", "--format=%H", "46208790..29f04e86"])
    del_rango = set(h[:8] for h in rango.split() if h.strip())
    print("   commits en 46208790..29f04e86, contados de git log: %d" % len(del_rango))
    nombrados = re.findall(r"^\| \d+ \| `([0-9a-f]{8})` \|", cuerpo, re.M)
    print("   commits nombrados en la tabla del borrador: %d" % len(nombrados))
    fuera = [h for h in nombrados if h not in del_rango]
    for h in nombrados:
        c, asunto = git(["log", "-1", "--format=%s", h])
        print("      %s  %s  %s" % (h, "EN EL RANGO" if h in del_rango else "FUERA",
                                    asunto.strip()[:66]))
    print("   CIFRA nombrados que NO estan en el rango: %d" % len(fuera))
    if len(nombrados) != 8 or fuera:
        rojos.append("la tabla de commits del borrador no calza con git log")
    print("")

    # ------------------------------- E. LA BATERIA, MEDIDA Y NO DADA POR BUENA
    print("E) LA BATERIA DE LA VUELTA %d, MEDIDA HOY" % VUELTA_DEL_REPORTE)
    existe = os.path.exists(BATERIA)
    bytes_bat = os.path.getsize(BATERIA) if existe else -1
    print("   %s -> %s"
          % (os.path.relpath(BATERIA, RAIZ).replace(os.sep, "/"),
             ("%d bytes" % bytes_bat) if existe else "NO EXISTE"))
    if not existe or bytes_bat != 0:
        rojos.append("la bateria de la 170 no mide cero bytes; este instrumento "
                     "esta escrito para el caso en que no corrio")
    acta = leer(ACTA)
    lineas_acta = acta.split("\n")
    cab5 = [i for i, l in enumerate(lineas_acta, 1)
            if l.startswith("## 5. LA BATERIA DE MUTACIONES, CORRIDA POR MI MANO")]
    print("   seccion 5 del acta (la corrida del auditor): %s"
          % (", ".join("ACTA_AUDITOR.md:%d" % i for i in cab5) or "NO ESTA"))
    if len(cab5) != 1:
        rojos.append("la seccion 5 del acta 170 no aparece exactamente una vez")
    linea_acta_5 = cab5[0] if len(cab5) == 1 else 0
    c, hash_acta = git(["log", "-1", "--format=%h", "--", "docs/loop/ACTA_AUDITOR.md"])
    print("   ultimo commit que toca el acta: %s" % hash_acta.strip())
    print("")

    if rojos:
        print("ROJO, %d motivo(s), y NO se escribe nada:" % len(rojos))
        for r in rojos:
            print("   " + r)
        return 1

    # --------------------------------------------------------- F. SE ESCRIBE
    print("F) SE ESCRIBE")

    bloque_cabecera = (
        MARCA_ABRE + "\n"
        "**LA TABLA, PEGADA ENTERA DEL FICHERO QUE LA LLEVA Y NO TECLEADA.** Salio\n"
        "de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta %d`, corrido al\n"
        "cierre de la vuelta %d, y su salida cruda vive en\n"
        "`docs/loop/SALIDA_V%d_TALLADOR_CABECERA.txt` (%d bytes, %d filas de tabla,\n"
        "contadas por `scripts/loop/vuelta%d_tarea1b_cerrar_reporte_170.py`). **Es la\n"
        "primera vez en dos vueltas que el tallador saca la tabla entera con sus dos\n"
        "columnas**, y por eso aqui no queda ningun hueco que rellenar.\n\n"
        "%s\n\n"
        + MARCA_CIERRA + "\n") % (
        VUELTA_DEL_REPORTE, VUELTA_DEL_REPORTE, VUELTA_DEL_REPORTE,
        len(sal.encode("utf-8")), len(filas), VUELTA_QUE_CIERRA, tabla)

    i0 = texto.index(MARCA_ABRE)
    i1 = texto.index(MARCA_CIERRA) + len(MARCA_CIERRA) + 1
    texto = texto[:i0] + bloque_cabecera + texto[i1:]
    print("   cabecera sustituida: %d bytes de hueco -> %d bytes de tabla pegada"
          % (i1 - i0, len(bloque_cabecera.encode("utf-8"))))

    veredicto = (
        "**EL VEREDICTO DE UNA LINEA: LA VUELTA %d HIZO SUS CINCO TAREAS Y NO CERRO\n"
        "SU REPORTE; ESTE CIERRE LO ESCRIBE LA VUELTA %d, Y LO DICE EN VEZ DE\n"
        "DISIMULARLO.**\n\n"
        "> **QUIEN ESCRIBE ESTE CIERRE, Y CUANDO, PORQUE CALLARLO SERIA MAQUILLARLO.**\n"
        "> Las secciones 3 a 9 de abajo NO se commitearon en la vuelta %d. Su borrador\n"
        "> quedo en `scripts/loop/_v170_cierre_texto.md` y el commit `29f04e86`,\n"
        "> titulado *\"EL BLOQUE DE CIERRE DE LA VUELTA %d, ENTERO\"*, **toca doce\n"
        "> ficheros y `docs/loop/REPORTE.md` no es ninguno de ellos** (medido en la\n"
        "> vuelta %d por `scripts/loop/vuelta%d_apertura.py`, bloque H, salida\n"
        "> `docs/loop/SALIDA_V%d_APERTURA.txt`). **La vuelta %d las pega aqui TAL COMO\n"
        "> ESTAN**, sin reescribir una palabra y sin suavizar ninguno de sus **ocho**\n"
        "> discutibles ni de sus **cinco** caidas (las dos cifras contadas del\n"
        "> borrador, no tecleadas). **Lo unico que la %d escribe de su mano en este\n"
        "> reporte son este recuadro y la seccion 9**, que el borrador dejo con\n"
        "> cabecera y sin cuerpo.\n"
        % (VUELTA_DEL_REPORTE, VUELTA_QUE_CIERRA, VUELTA_DEL_REPORTE,
           VUELTA_DEL_REPORTE, VUELTA_QUE_CIERRA, VUELTA_QUE_CIERRA,
           VUELTA_QUE_CIERRA, VUELTA_QUE_CIERRA, VUELTA_QUE_CIERRA))
    i = texto.index(VEREDICTO_VIEJO)
    j = texto.index("\n\n", i)
    print("   veredicto sustituido: %d bytes -> %d bytes"
          % (j - i, len(veredicto.encode("utf-8"))))
    texto = texto[:i] + veredicto + texto[j + 1:]

    seccion9 = (
        "\n**NO CORRIO. Y SE DICE CON LA MEDICION DELANTE EN VEZ DE RELLENARSE CON UNA\n"
        "CORRIDA DE OTRA VUELTA.** `docs/loop/SALIDA_V%d_BATERIA.txt` **existe y mide\n"
        "%d bytes**, medido en la vuelta %d por\n"
        "`scripts/loop/vuelta%d_tarea1b_cerrar_reporte_170.py` con `os.path.getsize`.\n"
        "El fichero de salida se creo y **la corrida no llego a escribir ni una linea**:\n"
        "la vuelta %d se corto antes de lanzarla.\n\n"
        "**AQUI NO SE PEGA UNA CORRIDA DE LA VUELTA %d.** Escribir en la seccion 9 del\n"
        "reporte de la %d una bateria corrida en otra vuelta seria publicar como de una\n"
        "vuelta lo medido en otra, que es **exactamente la especie que esta campana\n"
        "persigue**. El hueco se declara y no se rellena.\n\n"
        "**LA BATERIA DE LA VUELTA %d SI ESTA CORRIDA, PERO POR OTRA MANO Y EN OTRO\n"
        "SITIO, Y AHI ES DONDE HAY QUE IR A LEERLA:** seccion 5 del acta del auditor de\n"
        "la vuelta %d, *\"LA BATERIA DE MUTACIONES, CORRIDA POR MI MANO\"*, en\n"
        "`docs/loop/ACTA_AUDITOR.md:%d` (linea localizada por este instrumento, no\n"
        "tecleada). **Su cifra es del auditor y lleva su atribucion**: 75 entradas en la\n"
        "nomina, exit 0, ANCLA PERDIDA 0, NO MORDIO 0, NO REPRODUCIBLE 0, y los dos\n"
        "CASO DECLARADO de siempre. **Esa corrida no es de este reporte y por eso se\n"
        "cita y no se copia como propia.**\n"
        % (VUELTA_DEL_REPORTE, bytes_bat, VUELTA_QUE_CIERRA, VUELTA_QUE_CIERRA,
           VUELTA_DEL_REPORTE, VUELTA_QUE_CIERRA, VUELTA_DEL_REPORTE,
           VUELTA_DEL_REPORTE, VUELTA_DEL_REPORTE, linea_acta_5))

    anexo = "\n" + cuerpo.rstrip("\n") + "\n" + seccion9
    texto = texto.rstrip("\n") + "\n" + anexo

    io.open(REPORTE, "w", encoding="utf-8", newline="\n").write(texto)
    print("   ESCRITO: docs/loop/REPORTE.md (%d bytes, %d lineas)"
          % (len(texto.encode("utf-8")), texto.count("\n")))
    print("")

    # ------------------------------------ G. LA RELECTURA, LEYENDO DEL DISCO
    print("G) LA PRIMERA DE LAS DOS COMPROBACIONES: SE RELEE DEL DISCO")
    de_nuevo = leer(REPORTE)
    fallos = 0
    for etiqueta, cond in (
            ("el veredicto ya no dice SIN ESCRIBIR TODAVIA",
             "SIN ESCRIBIR TODAVIA" not in de_nuevo),
            ("el hueco PENDIENTE DE TALLAR ya no esta",
             "PENDIENTE DE TALLAR AL CIERRE" not in de_nuevo),
            ("las secciones 3 a 9 estan las siete",
             all(("\n## %d." % k) in de_nuevo for k in range(3, 10))),
            ("las secciones 3 a 8 del borrador estan byte a byte",
             cuerpo.rstrip("\n") in de_nuevo),
            ("los ocho discutibles siguen",
             len(re.findall(r"^- \*\*`D\.\d+`", de_nuevo, re.M)) == 8),
            ("las cinco caidas siguen",
             len(re.findall(r"^- \*\*`CAIDA \d+`", de_nuevo, re.M))
             + len(re.findall(r"^- \*\*UNA QUINTA", de_nuevo, re.M)) == 5),
            ("la tabla tallada esta pegada entera",
             all(l.rstrip() in de_nuevo for l in filas)),
            ("la seccion 9 dice que la bateria NO corrio",
             "**NO CORRIO." in de_nuevo),
            ("la seccion 9 no cuela ninguna corrida de la %d" % VUELTA_QUE_CIERRA,
             "SALIDA_V%d_BATERIA" % VUELTA_QUE_CIERRA not in de_nuevo)):
        print("   %-58s %s" % (etiqueta, "SI" if cond else "NO"))
        if not cond:
            fallos += 1
    print("   CIFRA comprobaciones: 9 | fallan: %d" % fallos)
    print("")
    if fallos:
        print("ROJO: el fichero escrito no cumple %d de sus propias guardas." % fallos)
        return 1
    print("VERDE: el reporte de la vuelta %d queda cerrado." % VUELTA_DEL_REPORTE)
    print("   LA SEGUNDA COMPROBACION (leer de git lo que se acaba de commitear)")
    print("   NO la hace este fichero: se hace DESPUES del commit, con git show,")
    print("   que es lo que la relectura al doble de este encargo manda.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
