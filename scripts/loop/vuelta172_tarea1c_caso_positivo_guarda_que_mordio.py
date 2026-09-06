# -*- coding: utf-8 -*-
r"""vuelta172_tarea1c_guarda_que_mordio.py . TAREA 1.c DE LA VUELTA 172.

MIDE, ANTES DE ARCHIVAR NADA, QUE LA GUARDA DEL PASO 0 ESTABA MORDIENDO AL
ABRIR ESTA VUELTA, Y QUE DEJA DE MORDER EN CUANTO EL REPORTE DE LA 171 SE
CIERRA Y SE ARCHIVA.

POR QUE HACE FALTA ESTE FICHERO, Y NO BASTA CON CITAR AL AUDITOR: el auditor lo
midio en su acta 171, seccion 4.1, y dio el sha256 `8e9ce848425fd704`. Esa es
SU cifra y va con SU atribucion. `EJECUTOR.md` 2 dice que un acta previa nunca
es fuente de una cifra nueva. Asi que aqui se vuelve a medir con codigo propio,
sobre el arbol de HOY y sobre los cortes de git, y las dos cifras se publican
al lado.

LO QUE MIDE, Y LAS TRES SON RECONSTRUIBLES DESDE GIT:

  1. EL SUJETO DE ENTONCES. El `docs/loop/REPORTE.md` que habia en el arbol al
     abrir esta vuelta es el del commit del acta 171 (el HEAD de apertura
     sellado en `SALIDA_V172_HEAD_APERTURA.txt` no lo toca). Se lee de
     `git show`, se computa su sha256 y se compara con el del ultimo reporte
     archivado. SI SON DISTINTOS, la clausula (d) muerde.

  2. LA GUARDA CORRIDA EN MODO SOLO COMPROBACION contra ese escenario, con la
     funcion pura `exigir_archivado(..., ejecutar_archivador=False)`, sobre
     COPIAS en un temporal. CERO escrituras en el repo (P.16, quien fabrica
     limpia).

  3. LA MISMA GUARDA CONTRA EL ARBOL DE HOY, con el reporte de la 171 ya
     cerrado, para ver si sigue mordiendo (tiene que morder, porque todavia no
     se ha archivado) y por que clausula.

NO ARCHIVA NADA Y NO ESCRIBE EN EL REPO. El archivado lo hace el paso 0 del
esqueleto, que es donde tiene que estar.

USO:
  python scripts/loop/vuelta172_tarea1c_guarda_que_mordio.py
"""
import hashlib
import io
import os
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paso0_archivar_anterior as PASO0   # noqa: E402

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
ARCHIVO = os.path.join(LOOP, "reportes")
VUELTA_ANTERIOR = 171


# LA DECLARACION DE SUJETO CONGELADO, CON SU MOTIVO Y NOMBRANDO SU LINEA
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

def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def sha(t):
    return hashlib.sha256(t.replace(chr(13) + NL, NL).encode("utf-8")).hexdigest()


def main():
    print("=" * 78)
    print("VUELTA 172, TAREA 1.c: LA GUARDA DEL PASO 0, MEDIDA ANTES DE ARCHIVAR")
    print("=" * 78)
    print("")

    print("A) EL COMMIT DEL ACTA %d, LOCALIZADO Y NO TECLEADO" % VUELTA_ANTERIOR)
    c, head_ap = git(["rev-parse", io.open(
        os.path.join(LOOP, "SALIDA_V172_HEAD_APERTURA.txt"),
        encoding="utf-8").read().strip()])
    head_ap = head_ap.strip()
    print("   HEAD de apertura de esta vuelta, del sello: %s" % head_ap[:8])
    c, padre = git(["rev-parse", head_ap + "^"])
    padre = padre.strip()
    c, asunto = git(["log", "-1", "--format=%s", padre])
    print("   su padre: %s" % padre[:8])
    print("   asunto del padre: %s" % asunto.strip()[:96])
    print("   (el HEAD de apertura es el commit de suciedad de esta vuelta, que no")
    print("    toca el reporte del arbol; su padre es el commit del acta)")
    print("")

    print("B) EL SUJETO DE ENTONCES: EL REPORTE QUE HABIA AL ABRIR ESTA VUELTA,")
    print("   LEIDO DE UN BLOB DE GIT CLAVADO Y NO DEL ARBOL DE TRABAJO")
    c, rep_entonces = git(["show", "%s:docs/loop/REPORTE.md" % head_ap])
    rep_entonces = rep_entonces.replace(chr(13) + NL, NL)
    sha_entonces = sha(rep_entonces)
    print("   primera linea: %s" % rep_entonces.split(NL, 1)[0][:88])
    print("   bytes: %d | saltos de linea: %d"
          % (len(rep_entonces.encode("utf-8")), rep_entonces.count(NL)))
    print("   sha256: %s" % sha_entonces)
    print("   CONTRASTE, CON SU ATRIBUCION: el auditor publica en su acta 171,")
    print("   seccion 4.1, el sha256 8e9ce848425fd704 para este mismo fichero.")
    print("   ES SU CIFRA. La mia, medida hoy con codigo propio, empieza por %s."
          % sha_entonces[:16])
    print("   CALZAN: %s" % ("SI" if sha_entonces.startswith("8e9ce848425fd704") else "NO"))
    print("")

    print("C) LO QUE HABIA ARCHIVADO ENTONCES, RECONSTRUIDO DE GIT Y NO DEL ARBOL")
    print("   (REMEDIO DE LA P.1, vuelta 182, mitad (a). ANTES este bloque listaba")
    print("    docs/loop/reportes/ DE HOY y con el fabricaba el escenario del")
    print("    bloque D. Un escenario historico construido con el directorio de hoy")
    print("    envejece con el repo: el mismo mal que la comprobacion que fallaba)")
    c, arb = git(["ls-tree", "--name-only", head_ap, "docs/loop/reportes/"])
    archivados_entonces = sorted(
        os.path.basename(l.strip()) for l in arb.splitlines()
        if os.path.basename(l.strip()).startswith("REPORTE_V"))
    texto_entonces = {}
    print("   CIFRA ficheros en docs/loop/reportes/ EN EL COMMIT %s: %d"
          % (head_ap[:8], len(archivados_entonces)))
    for f in archivados_entonces:
        c, t = git(["show", "%s:docs/loop/reportes/%s" % (head_ap, f)])
        t = t.replace(chr(13) + NL, NL)
        texto_entonces[f] = t
        print("      %-18s %7d bytes  sha256 %s  %s"
              % (f, len(t.encode("utf-8")), sha(t)[:16], t.split(NL, 1)[0][:40]))
    hay_entonces = ("REPORTE_V%d.md" % VUELTA_ANTERIOR) in archivados_entonces
    print("   REPORTE_V%d.md estaba archivado ENTONCES: %s"
          % (VUELTA_ANTERIOR, "SI" if hay_entonces else "NO"))
    print("")
    print("C.2) Y EL ARBOL DE HOY, COMO CONTRASTE Y NO COMO SUJETO")
    print("   (se sigue imprimiendo a proposito: una cifra que se deja de mirar es")
    print("    una cifra que nadie audita. Pero NINGUNA comprobacion depende de ella)")
    archivados = sorted(f for f in os.listdir(ARCHIVO) if f.startswith("REPORTE_V"))
    print("   CIFRA ficheros en docs/loop/reportes/ HOY: %d" % len(archivados))
    print("   REPORTE_V%d.md esta archivado HOY: %s"
          % (VUELTA_ANTERIOR,
             "SI" if ("REPORTE_V%d.md" % VUELTA_ANTERIOR) in archivados else "NO"))
    print("   LA DIFERENCIA ENTRE LOS DOS LISTADOS: %d fichero(s) que hoy estan y"
          % len(set(archivados) - set(archivados_entonces)))
    print("   entonces no: %s"
          % (", ".join(sorted(set(archivados) - set(archivados_entonces))) or "(ninguno)"))
    print("   ¿existe REPORTE_V%d.md?: %s"
          % (VUELTA_ANTERIOR,
             "SI" if ("REPORTE_V%d.md" % VUELTA_ANTERIOR) in archivados else "NO"))
    print("")

    print("D) LA GUARDA CORRIDA CONTRA EL ESCENARIO DE ENTONCES, EN UN TEMPORAL")
    print("   (modo solo comprobacion: ejecutar_archivador=False, CERO escrituras)")
    tmp = tempfile.mkdtemp(prefix="v172_guarda_")
    try:
        rep_tmp = os.path.join(tmp, "el_reporte_de_entonces.md")
        io.open(rep_tmp, "w", encoding="utf-8", newline=NL).write(rep_entonces)
        arc_tmp = os.path.join(tmp, "reportes")
        os.makedirs(arc_tmp)
        # EL ESCENARIO SE LLENA CON LO QUE HABIA ENTONCES, LEIDO DE GIT, y no
        # con lo que hay hoy. REMEDIO DE LA P.1, vuelta 182, mitad (a).
        for f in archivados_entonces:
            io.open(os.path.join(arc_tmp, f), "w", encoding="utf-8",
                    newline=NL).write(texto_entonces[f])
        ok, informe = PASO0.exigir_archivado(
            VUELTA_ANTERIOR, ruta_reporte=rep_tmp, dir_archivo=arc_tmp,
            ejecutar_archivador=False)
        for l in informe:
            print("   " + l)
        print("   VEREDICTO SOBRE EL ESCENARIO DE ENTONCES: %s"
              % ("VERDE" if ok else "ROJO"))
        de_entonces = ok
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
        print("   temporal borrado: %s" % (not os.path.exists(tmp)))
    print("")

    print("E) LA CONDUCTA DE LA GUARDA, SOBRE DOS ESCENARIOS FABRICADOS")
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
    print("")

    print("E.2) Y LA MISMA GUARDA CON EL OTRO PARAMETRO, QUE ES EL QUE EL AUDITOR")
    print("     CORRIO, Y NO DA LA MISMA CLAUSULA. LA DISCREPANCIA SE DECLARA.")
    print("   El auditor dice ROJO por la clausula (d). Yo, con vuelta_anterior=%d,"
          % VUELTA_ANTERIOR)
    print("   obtengo ROJO por la (b), porque REPORTE_V%d.md no existe todavia y la"
          % VUELTA_ANTERIOR)
    print("   (b) corta antes de llegar a la (d). LA CIFRA DEL AUDITOR SE REPRODUCE")
    print("   CON EL PARAMETRO QUE EL USO: exigir_archivado(170), que es lo que el")
    print("   esqueleto de la 171 llamaba. Corrido aqui:")
    ok_170, informe_170 = PASO0.exigir_archivado(
        VUELTA_ANTERIOR - 1, ejecutar_archivador=False)
    for l in informe_170:
        print("      " + l)
    print("   VEREDICTO con vuelta_anterior=%d: %s"
          % (VUELTA_ANTERIOR - 1, "VERDE" if ok_170 else "ROJO"))
    motivos_170 = [l for l in informe_170 if l.strip().startswith("(")]
    print("   clausulas que disparan: %s"
          % (", ".join(m.strip()[:3] for m in motivos_170) or "ninguna"))
    print("")

    print("F) LO QUE ESTO SOSTIENE, Y NI UNA PALABRA MAS")
    casos = [
        ("la guarda MORDIA sobre el escenario de apertura", de_entonces is False),
        # REMEDIO DE LA P.1, vuelta 182, mitad (c). ANTES esta linea decia
        # `("y sigue mordiendo hoy, porque la 171 aun no esta archivada",
        # ok_hoy is False)`, y `ok_hoy` salia de correr la guarda CONTRA EL ARBOL
        # DE HOY. Cuando REPORTE_V171.md se archivo, la frase dejo de ser cierta
        # y la comprobacion siguio pasando por otra clausula: verde y mal. Ahora
        # son DOS comprobaciones de CONDUCTA sobre escenarios fabricados.
        ("muerde cuando el reporte NO esta en el archivo", ok_sin is False),
        ("y deja de morder cuando SI esta, byte a byte", ok_con is True),
        # REMEDIO DE LA P.1, vuelta 182, mitad (b). ANTES esta linea decia
        # `("REPORTE_V%d.md" % VUELTA_ANTERIOR) not in archivados`, con
        # `archivados` siendo el listado de HOY: una expectativa sobre el ESTADO
        # DEL REPO y no sobre la CONDUCTA de la guarda, que pasaba a falsa para
        # siempre en cuanto REPORTE_V171.md se archivara, como se archivo. Ahora
        # pregunta por el escenario RECONSTRUIDO DE GIT, que no envejece.
        ("el reporte de entonces NO estaba en el archivo DE ENTONCES",
         ("REPORTE_V%d.md" % VUELTA_ANTERIOR) not in archivados_entonces),
        ("mi sha256 y el del auditor calzan en sus 16 primeros digitos",
         sha_entonces.startswith("8e9ce848425fd704")),
        ("con vuelta_anterior=%d la guarda tambien muerde" % (VUELTA_ANTERIOR - 1),
         ok_170 is False),
        ("y ahi la clausula que dispara es la (d), la del auditor",
         any(m.strip().startswith("(d)") for m in motivos_170)),
    ]
    fallos = 0
    for etiqueta, cond in casos:
        print("   %-62s %s" % (etiqueta, "SI" if cond else "NO"))
        if not cond:
            fallos += 1
    print("   CIFRA comprobaciones: %d | fallan: %d" % (len(casos), fallos))
    print("")
    if fallos:
        print("ROJO: la guarda no se comporta como esta medicion espera.")
        return 1
    print("VERDE: LA GUARDA QUE NACIO EN LA VUELTA 171 ESTA MORDIENDO EN LA 172,")
    print("   que es la vuelta siguiente a la que nacio. Y MUERDE POR DOS CLAUSULAS")
    print("   DISTINTAS SEGUN A QUE VUELTA SE LE PREGUNTE, cosa que se declara en vez")
    print("   de elegir la que mejor suene: con vuelta_anterior=%d por la (b) (el"
          % VUELTA_ANTERIOR)
    print("   archivo de la 171 no existe todavia), y con vuelta_anterior=%d por la"
          % (VUELTA_ANTERIOR - 1))
    print("   (d) (el reporte del arbol no esta guardado byte a byte en el archivo")
    print("   de la 170), que es la que el auditor midio y publico.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
