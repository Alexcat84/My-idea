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
    print("    toca REPORTE.md; su padre es el commit del acta del auditor)")
    print("")

    print("B) EL SUJETO DE ENTONCES: EL REPORTE.md QUE HABIA AL ABRIR ESTA VUELTA")
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

    print("C) LO QUE HABIA ARCHIVADO ENTONCES")
    archivados = sorted(f for f in os.listdir(ARCHIVO) if f.startswith("REPORTE_V"))
    print("   CIFRA ficheros en docs/loop/reportes/: %d" % len(archivados))
    for f in archivados:
        t = io.open(os.path.join(ARCHIVO, f), encoding="utf-8").read().replace(chr(13) + NL, NL)
        print("      %-18s %7d bytes  sha256 %s  %s"
              % (f, len(t.encode("utf-8")), sha(t)[:16], t.split(NL, 1)[0][:40]))
    print("   ¿existe REPORTE_V%d.md?: %s"
          % (VUELTA_ANTERIOR,
             "SI" if ("REPORTE_V%d.md" % VUELTA_ANTERIOR) in archivados else "NO"))
    print("")

    print("D) LA GUARDA CORRIDA CONTRA EL ESCENARIO DE ENTONCES, EN UN TEMPORAL")
    print("   (modo solo comprobacion: ejecutar_archivador=False, CERO escrituras)")
    tmp = tempfile.mkdtemp(prefix="v172_guarda_")
    try:
        rep_tmp = os.path.join(tmp, "REPORTE.md")
        io.open(rep_tmp, "w", encoding="utf-8", newline=NL).write(rep_entonces)
        arc_tmp = os.path.join(tmp, "reportes")
        os.makedirs(arc_tmp)
        for f in archivados:
            shutil.copyfile(os.path.join(ARCHIVO, f), os.path.join(arc_tmp, f))
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

    print("E) LA MISMA GUARDA CONTRA EL ARBOL DE HOY, CON LA 171 YA CERRADA")
    ok_hoy, informe_hoy = PASO0.exigir_archivado(
        VUELTA_ANTERIOR, ejecutar_archivador=False)
    for l in informe_hoy:
        print("   " + l)
    print("   VEREDICTO SOBRE EL ARBOL DE HOY: %s" % ("VERDE" if ok_hoy else "ROJO"))
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
        ("y sigue mordiendo hoy, porque la 171 aun no esta archivada",
         ok_hoy is False),
        ("el reporte de entonces NO estaba en el archivo",
         ("REPORTE_V%d.md" % VUELTA_ANTERIOR) not in archivados),
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
    print("   (d) (el REPORTE.md del arbol no esta guardado byte a byte en el archivo")
    print("   de la 170), que es la que el auditor midio y publico.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
