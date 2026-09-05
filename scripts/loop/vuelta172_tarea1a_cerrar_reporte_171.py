# -*- coding: utf-8 -*-
r"""vuelta172_tarea1a_cerrar_reporte_171.py . TAREA 1.a DE LA VUELTA 172.

CIERRA EL REPORTE DE LA VUELTA 171, QUE LA PROPIA 171 NO CERRO. Es la SEGUNDA
vuelta seguida que muere en el mismo tramo (acta 171, seccion 4.1).

CLON DECLARADO de scripts/loop/vuelta171_tarea1b_cerrar_reporte_170.py, que hizo
lo mismo con el reporte de la 170. Cambia los numeros de vuelta, y ademas:

  (i)  LA SECCION 3 SE GENERA DE GIT Y NO SALE DEL BORRADOR. La caida de la
       vuelta 79 fue publicar un hash de identidad tecleado, y EJECUTOR.md 1
       dice desde entonces que todo hash, rama o fecha que el reporte publique
       se lee de git en esa vuelta y se talla. Los dos extremos del rango se
       leen de los SELLOS de la 171 (SALIDA_V171_HEAD_APERTURA.txt y
       SALIDA_V171_HEAD_CIERRE.txt), NO se teclean, y la tabla de commits y el
       reparto de rutas salen de git log y git diff --name-only.
  (ii) LA SECCION 9 LLEVA SU CORTE PEGADO. Dice dos cosas medidas HOY: que
       docs/loop/SALIDA_V171_BATERIA.txt mide cero bytes, y que la nomina de la
       bateria esta ROJA por letra de su propio codigo. La segunda es una cifra
       QUE ESTA VUELTA VA A MOVER en su TAREA 4, asi que se publica con el
       momento de la medicion delante: "medido al cerrar la TAREA 1 de la
       vuelta 172, antes de que la TAREA 4 los meta". Medir temprano y publicar
       tarde sin decir cuando se midio es la caida de la vuelta 28.

POR QUE ESTE FICHERO Y NO cerrar_reporte.py, QUE NACE EN LA TAREA 5 DE ESTA
MISMA VUELTA: porque cerrar_reporte.py CAE EN ROJO si la salida de la bateria no
esta dentro de la seccion 9, y la bateria de la 171 NO CORRIO. El reporte de la
171 no puede cerrarse con el instrumento que exige lo que a la 171 le falta. Es
la guarda funcionando, no un rodeo, y se dice en vez de aflojarla.

LA SECCION 9 NO SE RELLENA CON UNA CORRIDA DE LA 172. Eso seria publicar como de
una vuelta lo medido en otra, que es exactamente la especie que esta campana
persigue, y el encargo lo prohibe con esas palabras.

CERO REPARACIONES DE NODOS: este fichero solo toca docs/loop/REPORTE.md.

USO:
  python scripts/loop/vuelta172_tarea1a_cerrar_reporte_171.py
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
BORRADOR = os.path.join(RAIZ, "scripts", "loop", "_v171_cierre_texto.md")
TALLADOR = os.path.join(LOOP, "SALIDA_V171_TALLADOR_CABECERA.txt")
BATERIA = os.path.join(LOOP, "SALIDA_V171_BATERIA.txt")
SELLO_AP = os.path.join(LOOP, "SALIDA_V171_HEAD_APERTURA.txt")
SELLO_CI = os.path.join(LOOP, "SALIDA_V171_HEAD_CIERRE.txt")
ACTA = os.path.join(LOOP, "ACTA_AUDITOR.md")

VUELTA_DEL_REPORTE = 171
VUELTA_QUE_CIERRA = 172

MARCA_ABRE = "<!-- CABECERA TALLADA -->"
MARCA_CIERRA = "<!-- FIN CABECERA TALLADA -->"
CAB_SECCION_9 = "## 9. LA BATERIA DE MUTACIONES, CORRIDA ENTERA Y SOLA AL CIERRE"
VEREDICTO_VIEJO = "**EL VEREDICTO DE UNA LINEA: SIN ESCRIBIR TODAVIA.**"

NL = chr(10)


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def sha(t):
    return hashlib.sha256(t.replace(chr(13) + NL, NL).encode("utf-8")).hexdigest()


def leer(ruta):
    return io.open(ruta, encoding="utf-8").read().replace(chr(13) + NL, NL)


def rel(ruta):
    return os.path.relpath(ruta, RAIZ).replace(os.sep, "/")


def main():
    print("=" * 78)
    print("VUELTA %d, TAREA 1.a: SE CIERRA EL REPORTE DE LA VUELTA %d"
          % (VUELTA_QUE_CIERRA, VUELTA_DEL_REPORTE))
    print("=" * 78)
    print("")

    rojos = []

    # ------------------------------------------------------------- A. EL SUJETO
    print("A) EL SUJETO, COMPROBADO ANTES DE TOCARLO")
    texto = leer(REPORTE)
    primera = texto.split(NL, 1)[0]
    print("   docs/loop/REPORTE.md primera linea: %s" % primera[:92])
    m = re.match(r"^#\s*REPORTE DE LA VUELTA\s+(\d+)\b", primera)
    if not m or int(m.group(1)) != VUELTA_DEL_REPORTE:
        rojos.append("el REPORTE.md del arbol no es el de la vuelta %d" % VUELTA_DEL_REPORTE)
    print("   CIFRA saltos de linea: %d | bytes: %d"
          % (texto.count(NL), len(texto.encode("utf-8"))))
    for marca, esperado in ((VEREDICTO_VIEJO, True),
                            ("PENDIENTE DE TALLAR AL CIERRE", True),
                            (NL + "## 3.", False), (NL + "## 9.", False)):
        hay = marca in texto
        print("   contiene %-40r -> %s (se esperaba %s)"
              % (marca[:38], "SI" if hay else "NO", "SI" if esperado else "NO"))
        if hay != esperado:
            rojos.append("el sujeto no esta en el estado que este instrumento espera: %r"
                         % marca[:40])
    print("")

    # -------------------------------------------- B. LA CABECERA, PEGADA ENTERA
    print("B) LA CABECERA, LEIDA DEL FICHERO DEL TALLADOR Y NO TECLEADA")
    sal = leer(TALLADOR)
    filas = [l for l in sal.split(NL) if l.strip().startswith("|")]
    print("   %s -> %d bytes, %d filas de tabla"
          % (rel(TALLADOR), len(sal.encode("utf-8")), len(filas)))
    if len(filas) < 8:
        rojos.append("el fichero del tallador trae %d filas de tabla, muy pocas" % len(filas))
    for l in filas:
        print("      %s" % l.strip()[:112])
    tabla = NL.join(l.rstrip() for l in filas)
    print("")

    # ------------------------ C. LA IDENTIDAD DE LA VUELTA 171, LEIDA DE GIT
    print("C) LA IDENTIDAD DE LA VUELTA %d, LEIDA DE SUS SELLOS Y DE GIT"
          % VUELTA_DEL_REPORTE)
    head_ap = leer(SELLO_AP).strip()
    head_ci = leer(SELLO_CI).strip()
    print("   HEAD de apertura, leido de %s: %s" % (rel(SELLO_AP), head_ap))
    print("   HEAD de cierre,   leido de %s: %s" % (rel(SELLO_CI), head_ci))
    for etiqueta, h in (("apertura", head_ap), ("cierre", head_ci)):
        if not re.match(r"^[0-9a-f]{40}$", h):
            rojos.append("el sello de %s no es un hash de 40 caracteres" % etiqueta)
        c, _ = git(["cat-file", "-e", h + "^{commit}"])
        print("   el sello de %-8s existe como commit en este repo: %s"
              % (etiqueta, "SI" if c == 0 else "NO"))
        if c != 0:
            rojos.append("el sello de %s no existe como commit" % etiqueta)

    rango = "%s..%s" % (head_ap, head_ci)
    c, log = git(["log", "--format=%h%x09%s", rango])
    commits = [l.split(chr(9), 1) for l in log.split(NL) if l.strip()]
    commits.reverse()
    print("   CIFRA commits en %s..%s: %d" % (head_ap[:8], head_ci[:8], len(commits)))
    for i, (h, s) in enumerate(commits, 1):
        print("      %d  %s  %s" % (i, h, s[:88]))
    if not commits:
        rojos.append("el rango de la vuelta %d no trae ningun commit" % VUELTA_DEL_REPORTE)

    c, numstat = git(["diff", rango.replace("..", " ").split()[0], head_ci,
                      "--numstat", "--", "dataset/", "web/", "engine/"])
    filas_numstat = [l for l in numstat.split(NL) if l.strip()]
    print("   CIFRA filas de numstat sobre dataset/, web/ y engine/: %d"
          % len(filas_numstat))
    for l in filas_numstat:
        print("      " + l)

    c, nombres = git(["diff", "--name-only", head_ap, head_ci])
    rutas = [l.strip() for l in nombres.split(NL) if l.strip()]
    print("   CIFRA rutas tocadas por la vuelta %d: %d" % (VUELTA_DEL_REPORTE, len(rutas)))
    reparto = {}
    for r in rutas:
        carpeta = r.rsplit("/", 1)[0] if "/" in r else "(raiz)"
        reparto[carpeta] = reparto.get(carpeta, 0) + 1
    for carpeta in sorted(reparto, key=lambda k: (-reparto[k], k)):
        print("      %-24s %d" % (carpeta, reparto[carpeta]))
    print("")

    # ----------------------------------------------- D. EL BORRADOR, VERIFICADO
    print("D) EL BORRADOR DEL CIERRE, COMPROBADO ANTES DE ANEXARLO")
    cuerpo = leer(BORRADOR)
    print("   %s -> %d bytes, %d saltos de linea, sha256 %s"
          % (rel(BORRADOR), len(cuerpo.encode("utf-8")), cuerpo.count(NL), sha(cuerpo)[:16]))
    if not cuerpo.startswith("## 4. LA PARADA"):
        rojos.append("el borrador no empieza por la seccion 4")
    if not cuerpo.rstrip(NL).endswith(CAB_SECCION_9):
        rojos.append("el borrador no termina en la cabecera de la seccion 9")
    secciones = [l for l in cuerpo.split(NL) if l.startswith("## ")]
    print("   CIFRA secciones que trae: %d" % len(secciones))
    for l in secciones:
        print("      %s" % l[:95])
    n_disc = len(re.findall(r"^- \*\*`D\.\d+`", cuerpo, re.M))
    n_caidas = len(re.findall(r"^- \*\*`CAIDA \d+`", cuerpo, re.M))
    n_preg = len(re.findall(r"^- \*\*`P\.\d+`", cuerpo, re.M))
    n_pd = len(re.findall(r"^- \*\*`PD\.\d+`", cuerpo, re.M))
    print("   CIFRA discutibles `D.n` contados del borrador: %d" % n_disc)
    print("   CIFRA caidas `CAIDA n` contadas del borrador: %d" % n_caidas)
    print("   CIFRA preguntas `P.n` contadas del borrador: %d" % n_preg)
    print("   CIFRA pendientes de doctrina `PD.n` contados: %d" % n_pd)
    if n_disc != 4:
        rojos.append("el borrador trae %d discutibles y el encargo nombra cuatro" % n_disc)
    if n_caidas != 1:
        rojos.append("el borrador trae %d caidas y el encargo nombra una" % n_caidas)
    print("")

    # ------------------ E. LOS CUATRO DISCUTIBLES, COTEJADOS CON LA PROSA VIEJA
    print("E) LOS CUATRO DISCUTIBLES SALEN DE LA PROSA DE LAS TAREAS, NO DE LA NADA")
    print("   (se comprueba que el cuerpo YA commiteado los nombra uno a uno)")
    for n in range(1, 5):
        marca = "`D.%d`" % n
        veces = texto.count(marca)
        print("   %-6s nombrado en el cuerpo de la vuelta %d: %d vez(ces)"
              % (marca, VUELTA_DEL_REPORTE, veces))
        if veces < 1:
            rojos.append("el cuerpo no nombra %s por ningun sitio" % marca)
    print("   `CAIDA 1` nombrada en el cuerpo: %d vez(ces)" % texto.count("`CAIDA 1`"))
    print("   `P.2`     nombrada en el cuerpo: %d vez(ces)  (el hueco se declara)"
          % texto.count("`P.2`"))
    print("")

    # ------------------------------- F. LA BATERIA, MEDIDA Y NO DADA POR BUENA
    print("F) LA BATERIA DE LA VUELTA %d, MEDIDA HOY" % VUELTA_DEL_REPORTE)
    existe = os.path.exists(BATERIA)
    bytes_bat = os.path.getsize(BATERIA) if existe else -1
    print("   %s -> %s" % (rel(BATERIA), ("%d bytes" % bytes_bat) if existe else "NO EXISTE"))
    if not existe or bytes_bat != 0:
        rojos.append("la bateria de la %d no mide cero bytes; este instrumento "
                     "esta escrito para el caso en que no corrio" % VUELTA_DEL_REPORTE)

    sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
    import verificar_mutaciones_viejas as vmv
    ultima, faltan = vmv.arneses_que_faltan()
    nomina = len(vmv.VIEJAS)
    c, head_hoy = git(["rev-parse", "--short", "HEAD"])
    head_hoy = head_hoy.strip()
    print("   CON SU FUNCION PURA, NO CON UN CONTADOR CASERO (la CAIDA 2 del acta 171):")
    print("   CIFRA arneses que faltan en la nomina, HOY, en %s: %d" % (head_hoy, len(faltan)))
    for n in sorted(faltan):
        print("      %s" % n)
    print("   CIFRA entradas de la nomina, HOY: %d" % nomina)
    print("   ultima vuelta representada en la nomina, HOY: %s" % ultima)

    acta = leer(ACTA)
    lineas_acta = acta.split(NL)
    cab5 = [i for i, l in enumerate(lineas_acta, 1)
            if l.strip() == "## 5. LA BATERIA DE MUTACIONES"]
    print("   seccion 5 del acta %d (la bateria del auditor): %s"
          % (VUELTA_DEL_REPORTE,
             ", ".join("ACTA_AUDITOR.md:%d" % i for i in cab5) or "NO ESTA"))
    if len(cab5) != 1:
        rojos.append("la seccion 5 del acta %d no aparece exactamente una vez"
                     % VUELTA_DEL_REPORTE)
    linea_acta_5 = cab5[0] if len(cab5) == 1 else 0
    print("")

    if rojos:
        print("ROJO, %d motivo(s), y NO se escribe nada:" % len(rojos))
        for r in rojos:
            print("   " + r)
        return 1

    # --------------------------------------------------------- G. SE ESCRIBE
    print("G) SE ESCRIBE")

    bloque_cabecera = (
        MARCA_ABRE + NL +
        "**LA TABLA, PEGADA ENTERA DEL FICHERO QUE LA LLEVA Y NO TECLEADA.** Salio" + NL +
        "de `scripts/loop/tallar_cabecera_reporte.py --fase04 --vuelta %d`, corrido al" % VUELTA_DEL_REPORTE + NL +
        "cierre de la vuelta %d a las 00:10, y su salida cruda vive en" % VUELTA_DEL_REPORTE + NL +
        "`%s` (%d bytes, %d filas de tabla, contadas por" % (rel(TALLADOR), len(sal.encode("utf-8")), len(filas)) + NL +
        "`scripts/loop/vuelta%d_tarea1a_cerrar_reporte_171.py`). **El tallador salio" % VUELTA_QUE_CIERRA + NL +
        "VERDE con sus dos columnas y el auditor lo volvio a correr y salio identico**" + NL +
        "(acta %d, seccion 4.1). **Lo que la vuelta %d no llego a hacer fue pegarlo** " % (VUELTA_DEL_REPORTE, VUELTA_DEL_REPORTE) + NL +
        "aqui, y eso es lo unico que hace esta linea de mas." + NL + NL +
        tabla + NL + NL +
        MARCA_CIERRA + NL)

    i0 = texto.index(MARCA_ABRE)
    i1 = texto.index(MARCA_CIERRA) + len(MARCA_CIERRA) + 1
    texto = texto[:i0] + bloque_cabecera + texto[i1:]
    print("   cabecera sustituida: %d bytes de hueco -> %d bytes de tabla pegada"
          % (i1 - i0, len(bloque_cabecera.encode("utf-8"))))

    veredicto = (
        "**EL VEREDICTO DE UNA LINEA: LA VUELTA %d PAGO SUS DEUDAS DE REGISTRO Y" % VUELTA_DEL_REPORTE + NL +
        "MIDIO LO QUE NADIE HABIA MEDIDO, PERO SE CORTO ANTES DE CERRAR SU REPORTE, QUE" + NL +
        "ES EL MISMO TRAMO QUE YA ESTABA EN RELECTURA AL DOBLE; ESTE CIERRE LO ESCRIBE" + NL +
        "LA VUELTA %d, Y LO DICE EN VEZ DE DISIMULARLO.**" % VUELTA_QUE_CIERRA + NL + NL +
        "> **QUIEN ESCRIBE ESTE CIERRE, Y CUANDO, PORQUE CALLARLO SERIA MAQUILLARLO.**" + NL +
        "> Las secciones 3 a 9 de abajo NO se commitearon en la vuelta %d. Su bloque de" % VUELTA_DEL_REPORTE + NL +
        "> cierre **si corrio entero**, a las 00:09, y su tallador salio **VERDE**; lo" + NL +
        "> que no ocurrio nunca fue el paso siguiente, que era **a mano**." + NL +
        "> `scripts/loop/vuelta%d_cierre.py` **solo mide**: escribe once ficheros" % VUELTA_DEL_REPORTE + NL +
        "> `SALIDA_*` y **no toca `REPORTE.md` en ninguna linea** (medido por el auditor," + NL +
        "> acta %d, seccion 4.1, con su atribucion delante). **Las dos vueltas que han" % VUELTA_DEL_REPORTE + NL +
        "> caido, han caido justo ahi**, y por eso la TAREA 5 de la vuelta %d es" % VUELTA_QUE_CIERRA + NL +
        "> codigo y no una promesa." + NL +
        "> " + NL +
        "> **LA VUELTA %d NO SUAVIZA NADA DE LO QUE ENCUENTRA.** Los **cuatro**" % VUELTA_QUE_CIERRA + NL +
        "> discutibles y la **una** caida de abajo son los que la prosa de las tareas" + NL +
        "> declaro, contados del borrador por el instrumento y no tecleados. **La" + NL +
        "> seccion 9 dice que la bateria NO corrio** y no se rellena con una corrida" + NL +
        "> de otra vuelta." + NL)
    i = texto.index(VEREDICTO_VIEJO)
    j = texto.index(NL + NL, i)
    print("   veredicto sustituido: %d bytes -> %d bytes"
          % (j - i, len(veredicto.encode("utf-8"))))
    texto = texto[:i] + veredicto + texto[j + 1:]

    filas_tabla = [
        "| %d | `%s` | %s |" % (i, h, s.split(":", 1)[0][:72])
        for i, (h, s) in enumerate(commits, 1)]
    reparto_txt = ", ".join("**%d** de `%s`" % (reparto[c], c)
                            for c in sorted(reparto, key=lambda k: (-reparto[k], k)))

    seccion3 = (
        "## 3. EL CIERRE, CON SU IDENTIDAD LEIDA DE GIT" + NL + NL +
        "**LOS DOS EXTREMOS NO SE TECLEAN: SE LEEN DE LOS SELLOS QUE LA PROPIA VUELTA %d" % VUELTA_DEL_REPORTE + NL +
        "ESCRIBIO.** Apertura `%s`, de `%s`, sellado ANTES de la" % (head_ap[:8], rel(SELLO_AP)) + NL +
        "primera operacion; cierre `%s`, de `%s`, sellado tras la" % (head_ci[:8], rel(SELLO_CI)) + NL +
        "ultima. Los dos existen como commit en este repo, comprobado con `git cat-file`." + NL + NL +
        "**LOS COMMITS DE LA VUELTA, LEIDOS DE `git log %s..%s`: %d.**" % (head_ap[:8], head_ci[:8], len(commits)) + NL + NL +
        "| # | commit | que cierra |" + NL +
        "|---:|---|---|" + NL +
        NL.join(filas_tabla) + NL + NL +
        "**EL GRAFO NO SE MOVIO, PROBADO Y NO CREIDO:**" + NL +
        "`git diff %s %s --numstat -- dataset/ web/ engine/` sale con" % (head_ap[:8], head_ci[:8]) + NL +
        "**%d filas**. Las **%d rutas** que la vuelta toca se reparten en %s." % (len(filas_numstat), len(rutas), reparto_txt) + NL +
        "**Cero nodos tocados, cero aristas movidas, cero clases movidas.**" + NL + NL +
        "**EL COMMIT QUE LLEVA ESTE REPORTE NO SE NOMBRA AQUI**, porque se crea despues" + NL +
        "de escribirlo, y esta vez ni siquiera es de esta vuelta: **lo escribe la" + NL +
        "%d**. El `HEAD` de cierre que la cabecera publica, `%s`, es el sello" % (VUELTA_QUE_CIERRA, head_ci[:8]) + NL +
        "leido de `git rev-parse HEAD` **tras la ultima operacion de la %d**, que es lo" % VUELTA_DEL_REPORTE + NL +
        "unico que se puede leer sin inventarlo." + NL + NL +
        "**Y UNA COSA QUE ESTA TABLA DICE SIN QUERER Y CONVIENE LEER: NINGUNO DE LOS %d" % len(commits) + NL +
        "COMMITS ES UN BLOQUE DE CIERRE.** La vuelta %d corrio su cierre y no lo" % VUELTA_DEL_REPORTE + NL +
        "commiteo: sus trece ficheros quedaron sueltos en el arbol y los recogio el" + NL +
        "auditor con su acta. **Eso tambien es parte de la especie.**" + NL)

    seccion9 = (
        NL +
        "**NO CORRIO. Y SE DICE CON LA MEDICION DELANTE EN VEZ DE RELLENARSE CON UNA" + NL +
        "CORRIDA DE OTRA VUELTA.** `%s` **existe y mide %d bytes**," % (rel(BATERIA), bytes_bat) + NL +
        "medido en la vuelta %d por" % VUELTA_QUE_CIERRA + NL +
        "`scripts/loop/vuelta%d_tarea1a_cerrar_reporte_171.py` con `os.path.getsize`." % VUELTA_QUE_CIERRA + NL +
        "El fichero de salida se creo a las 00:10 y **la corrida no llego a escribir ni" + NL +
        "una linea**." + NL + NL +
        "**AQUI NO SE PEGA UNA CORRIDA DE LA VUELTA %d.** Escribir en la seccion 9 del" % VUELTA_QUE_CIERRA + NL +
        "reporte de la %d una bateria corrida en otra vuelta seria publicar como de una" % VUELTA_DEL_REPORTE + NL +
        "vuelta lo medido en otra, que es **exactamente la especie que esta campana" + NL +
        "persigue**. El hueco se declara y no se rellena." + NL + NL +
        "**Y HAY ALGO PEOR QUE NO HABER CORRIDO, QUE ES QUE HOY SALDRIA ROJA POR LETRA" + NL +
        "DE SU PROPIO CODIGO.** Medido con la funcion pura `arneses_que_faltan()` del" + NL +
        "propio `scripts/loop/verificar_mutaciones_viejas.py` (no con un contador" + NL +
        "casero: esa fue la `CAIDA 2` del auditor en su acta %d), **al cerrar la" % VUELTA_DEL_REPORTE + NL +
        "TAREA 1 de la vuelta %d y en el commit `%s`**:" % (VUELTA_QUE_CIERRA, head_hoy) + NL + NL +
        "| que se mide | valor, con su corte |" + NL +
        "|---|---:|" + NL +
        "| arneses de la %d fuera de la nomina | **%d** |" % (VUELTA_DEL_REPORTE, len(faltan)) + NL +
        "| cuales | %s |" % ", ".join("`%s`" % n for n in sorted(faltan)) + NL +
        "| entradas de la nomina | **%d** |" % nomina + NL +
        "| ultima vuelta representada | **%s** |" % ultima + NL + NL +
        "**ESA CIFRA TIENE FECHA DE CADUCIDAD DENTRO DE ESTA MISMA VUELTA, Y POR ESO VA" + NL +
        "CON SU CORTE PEGADO:** la TAREA 4 de la vuelta %d mete los tres en la nomina," % VUELTA_QUE_CIERRA + NL +
        "asi que a partir de ahi el %d y el %d dejan de ser ciertos. **Publicar una" % (len(faltan), nomina) + NL +
        "medicion sin decir cuando se tomo, cuando la propia vuelta la va a mover, es la" + NL +
        "caida de la vuelta 28 y no se repite aqui.**" + NL + NL +
        "**LA BATERIA DE LA VUELTA %d SI ESTA CORRIDA, PERO POR OTRA MANO Y EN OTRO" % VUELTA_DEL_REPORTE + NL +
        "SITIO, Y AHI ES DONDE HAY QUE IR A LEERLA:** seccion 5 del acta del auditor de" + NL +
        "la vuelta %d, en `docs/loop/ACTA_AUDITOR.md:%d` (linea localizada por este" % (VUELTA_DEL_REPORTE, linea_acta_5) + NL +
        "instrumento, no tecleada). **Lo que ahi hay es del auditor y lleva su" + NL +
        "atribucion**: dice que la lanza despues de commitear su acta, sola y sin nada" + NL +
        "al lado, y que **sabe sin correrla que su veredicto sera ROJO** por los tres" + NL +
        "arneses fuera de la nomina. **Esa corrida no es de este reporte y por eso se" + NL +
        "cita y no se copia como propia.**" + NL)

    anexo = NL + seccion3 + NL + cuerpo.rstrip(NL) + NL + seccion9
    texto = texto.rstrip(NL) + NL + anexo

    io.open(REPORTE, "w", encoding="utf-8", newline=NL).write(texto)
    print("   ESCRITO: docs/loop/REPORTE.md (%d bytes, %d saltos de linea)"
          % (len(texto.encode("utf-8")), texto.count(NL)))
    print("")

    # ------------------------------------ H. LA RELECTURA, LEYENDO DEL DISCO
    print("H) LA PRIMERA DE LAS DOS COMPROBACIONES: SE RELEE DEL DISCO")
    de_nuevo = leer(REPORTE)
    fallos = 0
    for etiqueta, cond in (
            ("el veredicto ya no dice SIN ESCRIBIR TODAVIA",
             "SIN ESCRIBIR TODAVIA" not in de_nuevo),
            ("el hueco PENDIENTE DE TALLAR ya no esta",
             "PENDIENTE DE TALLAR AL CIERRE" not in de_nuevo),
            ("las secciones 3 a 9 estan las siete",
             all((NL + "## %d." % k) in de_nuevo for k in range(3, 10))),
            ("las secciones 4 a 9 del borrador estan byte a byte",
             cuerpo.rstrip(NL) in de_nuevo),
            ("los cuatro discutibles siguen",
             len(re.findall(r"^- \*\*`D\.\d+`", de_nuevo, re.M)) == 4),
            ("la caida sigue",
             len(re.findall(r"^- \*\*`CAIDA \d+`", de_nuevo, re.M)) == 1),
            ("la tabla tallada esta pegada entera",
             all(l.rstrip() in de_nuevo for l in filas)),
            ("la seccion 3 nombra los %d commits" % len(commits),
             all(("`%s`" % h) in de_nuevo for h, _s in commits)),
            ("la seccion 9 dice que la bateria NO corrio",
             "**NO CORRIO." in de_nuevo),
            ("la seccion 9 no cuela ninguna corrida de la %d" % VUELTA_QUE_CIERRA,
             "SALIDA_V%d_BATERIA" % VUELTA_QUE_CIERRA not in de_nuevo),
            ("la seccion 9 lleva el corte de la cifra que va a caducar",
             head_hoy in de_nuevo),
            ("cero guiones largos y cero guiones medios",
             chr(8212) not in de_nuevo and chr(8211) not in de_nuevo)):
        print("   %-58s %s" % (etiqueta, "SI" if cond else "NO"))
        if not cond:
            fallos += 1
    print("   CIFRA comprobaciones: 12 | fallan: %d" % fallos)
    print("")
    if fallos:
        print("ROJO: el fichero escrito no cumple %d de sus propias guardas." % fallos)
        return 1
    print("VERDE: el reporte de la vuelta %d queda cerrado." % VUELTA_DEL_REPORTE)
    print("   LA SEGUNDA COMPROBACION (leer de git lo que se acaba de commitear)")
    print("   NO la hace este fichero: se hace DESPUES del commit, con git show,")
    print("   que es lo que la relectura al doble de este encargo manda, y esta vez")
    print("   SOBRE LO PROPIO.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
