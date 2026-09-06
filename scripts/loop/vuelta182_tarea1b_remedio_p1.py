# -*- coding: utf-8 -*-
r"""vuelta182_tarea1b_remedio_p1.py . EL REMEDIO DE LA `P.1` DEL ACTA 180:
PRIMERO EL ESPERADO, DESPUES EL NOMBRE, EN ESE ORDEN.

EL ORDEN NO ES ESTILO, ES PARTE DE LA ADJUDICACION, y esta escrito en el acta 180
en `docs/loop/ACTA_AUDITOR.md:62818`, leido hoy: *"El orden importa y es parte de
la adjudicacion: primero el esperado, despues el nombre."* Y da su motivo:
renombrarlo antes de arreglarlo meteria un rojo permanente en la nomina.

QUE ESTA ROTO, MEDIDO Y NO RECORDADO.
`scripts/loop/vuelta172_tarea1c_guarda_que_mordio.py` cae con **exit 1**,
fallando **1 de 6** comprobaciones. La que falla es:

    ("el reporte de entonces NO estaba en el archivo",
     ("REPORTE_V%d.md" % VUELTA_ANTERIOR) not in archivados)

y `archivados` es **el listado de `docs/loop/reportes/` DE HOY**. O sea que la
comprobacion pregunta por el ESTADO DEL REPO DE HOY y no por la CONDUCTA de la
guarda. `REPORTE_V171.md` se archivo en su momento, luego la comprobacion pasa a
ser falsa para siempre, y el arnes queda en rojo permanente sin que nada se haya
roto. **Es exactamente la especie que `prueba_de_la_nomina()` se re-fundo para
matar en la vuelta 178**, con estas palabras suyas: *"el caso viejo exigia que en
el repo de hoy no faltara NINGUNO, y eso era una expectativa sobre el estado del
repo, no sobre la conducta de la funcion"*.

Y HAY UNA SEGUNDA MITAD DE LA MISMA ESPECIE, QUE EL ACTA NO NOMBRA Y QUE APARECE
AL MIRAR EL CODIGO: el escenario "de entonces" del bloque D **se fabrica copiando
`docs/loop/reportes/` DE HOY** al temporal. Un escenario historico construido con
el directorio de hoy no es un escenario historico: envejece con el repo, igual que
la comprobacion. Se arregla con la misma medicina, y se declara aunque nadie la
haya pedido, porque arreglar la mitad visible y dejar la invisible es justo el
verde que llega por donde la guarda no mira.

EL REMEDIO, LAS DOS MITADES:

  (a) EL ESCENARIO DE ENTONCES SE RECONSTRUYE DE GIT, en el commit de apertura de
      la vuelta 172, con `git ls-tree` y `git show`. Deja de depender del arbol de
      hoy.
  (b) LA COMPROBACION PASA A SER SOBRE ESE ESCENARIO RECONSTRUIDO y no sobre el
      directorio de hoy. El listado de hoy se sigue imprimiendo COMO CONTRASTE,
      con su etiqueta, porque una cifra que se deja de mirar es una cifra que
      nadie audita.

Y DESPUES, EL NOMBRE. El fichero pasa a llamarse
`vuelta172_tarea1c_caso_positivo_guarda_que_mordio.py`, que es lo que le hace
entrar en el censo: `PATRON_ARNES` exige que el nombre lleve una de las
`FAMILIAS_DE_ARNES` (`mutacion`, `caso_positivo`, `simular`) y el nombre viejo no
llevaba ninguna. **Que la bateria no lo vea es `banco 9`: un arnes en rojo que
nadie corre es una guarda apagada.**

USO:
  python scripts/loop/vuelta182_tarea1b_remedio_p1.py --simular
  python scripts/loop/vuelta182_tarea1b_remedio_p1.py
"""
import argparse
import io
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

VIEJO = "scripts/loop/vuelta172_tarea1c_guarda_que_mordio.py"
NUEVO = "scripts/loop/vuelta172_tarea1c_caso_positivo_guarda_que_mordio.py"

# ------------------------------------------------------------------ (a) y (b)
V_C = '''    print("C) LO QUE HABIA ARCHIVADO ENTONCES")
    archivados = sorted(f for f in os.listdir(ARCHIVO) if f.startswith("REPORTE_V"))
    print("   CIFRA ficheros en docs/loop/reportes/: %d" % len(archivados))
    for f in archivados:
        t = io.open(os.path.join(ARCHIVO, f), encoding="utf-8").read().replace(chr(13) + NL, NL)
        print("      %-18s %7d bytes  sha256 %s  %s"
              % (f, len(t.encode("utf-8")), sha(t)[:16], t.split(NL, 1)[0][:40]))'''

N_C = '''    print("C) LO QUE HABIA ARCHIVADO ENTONCES, RECONSTRUIDO DE GIT Y NO DEL ARBOL")
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
          % (", ".join(sorted(set(archivados) - set(archivados_entonces))) or "(ninguno)"))'''

V_D = '''        for f in archivados:
            shutil.copyfile(os.path.join(ARCHIVO, f), os.path.join(arc_tmp, f))'''
N_D = '''        # EL ESCENARIO SE LLENA CON LO QUE HABIA ENTONCES, LEIDO DE GIT, y no
        # con lo que hay hoy. REMEDIO DE LA P.1, vuelta 182, mitad (a).
        for f in archivados_entonces:
            io.open(os.path.join(arc_tmp, f), "w", encoding="utf-8",
                    newline=NL).write(texto_entonces[f])'''

V_F = '''        ("el reporte de entonces NO estaba en el archivo",
         ("REPORTE_V%d.md" % VUELTA_ANTERIOR) not in archivados),'''
N_F = '''        # REMEDIO DE LA P.1, vuelta 182, mitad (b). ANTES esta linea decia
        # `("REPORTE_V%d.md" % VUELTA_ANTERIOR) not in archivados`, con
        # `archivados` siendo el listado de HOY: una expectativa sobre el ESTADO
        # DEL REPO y no sobre la CONDUCTA de la guarda, que pasaba a falsa para
        # siempre en cuanto REPORTE_V171.md se archivara, como se archivo. Ahora
        # pregunta por el escenario RECONSTRUIDO DE GIT, que no envejece.
        ("el reporte de entonces NO estaba en el archivo DE ENTONCES",
         ("REPORTE_V%d.md" % VUELTA_ANTERIOR) not in archivados_entonces),'''


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def aplicar(texto):
    """PURA: recibe el texto del arnes y devuelve (nuevo, informe)."""
    informe = []
    for viejo, nuevo, nombre in ((V_C, N_C, "(a) el bloque C se reconstruye de git"),
                                 (V_D, N_D, "(a) el bloque D usa el escenario de entonces"),
                                 (V_F, N_F, "(b) la comprobacion deja de mirar el repo de hoy")):
        if viejo not in texto:
            informe.append("NO SE ENCUENTRA EL TROZO DE %s" % nombre)
            return None, informe
        texto = texto.replace(viejo, nuevo, 1)
        informe.append("APLICADO: %s" % nombre)
    return texto, informe


def correr(ruta):
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run([sys.executable, ruta], cwd=RAIZ, capture_output=True, env=env)
    out = (r.stdout.decode("utf-8", errors="replace")
           + r.stderr.decode("utf-8", errors="replace"))
    return r.returncode, out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    salida = []
    w = salida.append
    w("VUELTA 182, TAREA 1.b: EL REMEDIO DE LA P.1 DEL ACTA 180")
    w("orden: PRIMERO EL ESPERADO, DESPUES EL NOMBRE (acta 180, linea 62818)")
    w("")

    p_viejo = os.path.join(RAIZ, VIEJO.replace("/", os.sep))
    p_nuevo = os.path.join(RAIZ, NUEVO.replace("/", os.sep))
    w("A) EL SUJETO, ANTES DE TOCARLO")
    w("   %s existe: %s" % (VIEJO, "SI" if os.path.exists(p_viejo) else "NO"))
    w("   %s existe: %s" % (NUEVO, "SI" if os.path.exists(p_nuevo) else "NO"))
    if not os.path.exists(p_viejo):
        w("   ROJO: no esta el fichero que hay que remediar.")
        print(NL.join(salida))
        return 1
    w("   disco %d bytes" % os.path.getsize(p_viejo))
    c_antes, o_antes = correr(VIEJO)
    fallan_antes = [l for l in o_antes.split(NL) if "CIFRA comprobaciones" in l]
    w("   CORRIDO ANTES DEL REMEDIO -> EXITCODE %d" % c_antes)
    for l in fallan_antes:
        w("      | " + l.strip())
    for l in o_antes.split(NL):
        if l.strip().endswith(" NO"):
            w("      LA QUE FALLA: " + l.strip())
    w("")

    t = io.open(p_viejo, encoding="utf-8").read().replace(chr(13) + NL, NL)
    nuevo, informe = aplicar(t)
    w("B) EL ESPERADO, ARREGLADO (y esto va PRIMERO)")
    for l in informe:
        w("   " + l)
    if nuevo is None:
        w("   ROJO: el remedio NO se aplica.")
        print(NL.join(salida))
        return 1
    w("   el arnes pasa de %d a %d bytes en LF"
      % (len(t.encode("utf-8")), len(nuevo.encode("utf-8"))))
    w("")

    if a.simular:
        w("MODO --simular: no se escribe ni se renombra nada.")
        t2 = NL.join(salida) + NL
        ruta = os.path.join(LOOP, "SALIDA_V182_T1B_REMEDIO_P1.txt")
        io.open(ruta, "w", encoding="utf-8", newline=NL).write(t2)
        print(t2)
        print("ESCRITO: %s (%d bytes)" % (ruta, len(t2.encode("utf-8"))))
        return 0

    io.open(p_viejo, "w", encoding="utf-8", newline=NL).write(nuevo)
    c_medio, o_medio = correr(VIEJO)
    w("   CORRIDO CON EL ESPERADO ARREGLADO Y EL NOMBRE VIEJO -> EXITCODE %d" % c_medio)
    for l in o_medio.split(NL):
        if "CIFRA comprobaciones" in l or l.strip().startswith(("VERDE", "ROJO")):
            w("      | " + l.strip()[:120])
    if c_medio != 0:
        w("   ROJO: el arnes sigue cayendo. NO SE RENOMBRA, que es justo lo que la")
        w("         adjudicacion 6.6 manda evitar: renombrar antes de arreglar")
        w("         meteria un rojo permanente en la nomina.")
        t2 = NL.join(salida) + NL
        ruta = os.path.join(LOOP, "SALIDA_V182_T1B_REMEDIO_P1.txt")
        io.open(ruta, "w", encoding="utf-8", newline=NL).write(t2)
        print(t2)
        return 1
    w("")

    w("C) Y AHORA EL NOMBRE, PORQUE EL ESPERADO YA ESTA VERDE")
    r = subprocess.run(["git", "mv", VIEJO, NUEVO], cwd=RAIZ, capture_output=True)
    w("   git mv -> exit %d %s"
      % (r.returncode, r.stderr.decode("utf-8", errors="replace").strip()[:120]))
    if r.returncode != 0:
        w("   ROJO: el renombrado fallo.")
        print(NL.join(salida))
        return 1
    w("   %s existe: %s" % (NUEVO, "SI" if os.path.exists(p_nuevo) else "NO"))
    w("   %s existe: %s" % (VIEJO, "SI" if os.path.exists(p_viejo) else "NO"))
    c_desp, o_desp = correr(NUEVO)
    w("   CORRIDO CON EL NOMBRE NUEVO -> EXITCODE %d" % c_desp)
    for l in o_desp.split(NL):
        if "CIFRA comprobaciones" in l or l.strip().startswith(("VERDE", "ROJO")):
            w("      | " + l.strip()[:120])
    w("")

    w("D) EL CENSO, QUE ES EL MOTIVO ENTERO DEL RENOMBRADO")
    sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
    import importlib
    import verificar_mutaciones_viejas as VMV
    importlib.reload(VMV)
    censo = VMV.arneses_del_directorio()
    nomina = [s for s, _x in VMV.VIEJAS]
    w("   FAMILIAS_DE_ARNES: %s" % ", ".join(VMV.FAMILIAS_DE_ARNES))
    w("   PATRON_ARNES casa con el nombre VIEJO: %s"
      % ("SI" if VMV.PATRON_ARNES.match(os.path.basename(VIEJO)) else "NO"))
    w("   PATRON_ARNES casa con el nombre NUEVO: %s"
      % ("SI" if VMV.PATRON_ARNES.match(os.path.basename(NUEVO)) else "NO"))
    w("   CIFRA censo arneses_del_directorio(): %d" % len(censo))
    w("   el nombre NUEVO esta en el censo: %s"
      % ("SI" if os.path.basename(NUEVO) in censo else "NO"))
    w("   el nombre NUEVO esta en la nomina VIEJAS: %s"
      % ("SI" if os.path.basename(NUEVO) in nomina else "NO"))
    w("   (que NO este en la nomina hoy es lo correcto y lo dice el propio fichero")
    w("    de la bateria: un arnes entra en la nomina EN LA VUELTA SIGUIENTE a la")
    w("    que nace. Aqui se declara para que nadie lo lea como un hueco)")
    ultima, faltan = VMV.arneses_que_faltan()
    w("   arneses_que_faltan(): ultima vuelta de la nomina %s, faltan %d"
      % (ultima, len(faltan)))
    for n in faltan:
        w("      FALTA: %s" % n)
    w("")

    t2 = NL.join(salida) + NL
    ruta = os.path.join(LOOP, "SALIDA_V182_T1B_REMEDIO_P1.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t2)
    print(t2)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t2.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
