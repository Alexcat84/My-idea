# -*- coding: utf-8 -*-
r"""vuelta146_2b_mutacion_ausencias.py . LA PRUEBA DE MUTACION DE LA ESCALADA
(TAREA 2.b y 2.c de la vuelta 146).

QUE PRUEBA, Y SOBRE QUE SUJETO. `verificar_ausencias_del_reporte.py` es la
guarda que hace morder a `EJECUTOR.md` 9 ("una busqueda negativa no se puede
citar"). Una guarda que no muerde no es una guarda (banco 9), y un caso rojo
que no puede fallar no es una prueba (`EJECUTOR.md` 1, caida 2 de la vuelta
89): aqui NINGUN veredicto es un literal comparado consigo mismo, TODOS salen
de leer la salida real del proceso.

EL SUJETO DEL CASO ROJO ES CONGELADO Y ES EL DE VERDAD (CORRECCION 22, y el
patron del discutible 1 de la vuelta 145): `a9b638ba:docs/loop/REPORTE.md`, el
reporte de la vuelta 145 TAL COMO SE COMMITEO. No es un sujeto fabricado para
la ocasion: es el texto que fallo, leido de su commit con `git show`, asi que
este arnes no puede envejecer por el camino por el que envejecieron las tres
mutaciones que la CORRECCION 22 curo. `docs/loop/REPORTE.md` se reescribe cada
vuelta; el blob de `a9b638ba` no.

LOS CUATRO CASOS:

  (A) CASO ROJO, EL QUE MANDA. La guarda sobre el reporte congelado de la 145
      tiene que salir EXIT 1 y tiene que NOMBRAR LA AFIRMACION DE LA 3.c, la
      frase literal "no existe en el repositorio ninguna lista canonica de
      libros". Si saliera verde sobre este sujeto la guarda no sirve, y este
      arnes lo dice en vez de aflojar el vocabulario hasta que pase.

  (B) CASO VERDE. Sin el, (A) solo probaria que el instrumento sabe decir rojo.
      Una ausencia RESPALDADA por un barrido exhaustivo de verdad
      (`docs/loop/SALIDA_V146_2C_BARRIDO_VERDE.txt`, producido por
      `barrer_ausencia.py` con su sello de cinco piezas) tiene que salir EXIT 0.

  (C) LA MUTACION DEL CASO VERDE, que es la que prueba que el SELLO muerde y no
      solo la ausencia de cita. Se toma el MISMO sujeto de (B) y se le cambia
      SOLO la cita: se apunta a un fichero de salida REAL que existe y no es un
      barrido (`SALIDA_V146_MOTOR_APERTURA.txt`). Tiene que salir EXIT 1
      diciendo que ese fichero no trae la marca del barrido. Sin este caso, la
      guarda podria estar aprobando cualquier cita.

  (D) LA CITA CONGELADA NO ES UN INTERRUPTOR (la leccion de la vuelta 135, "una
      exencion que escribe el auditado no es una exencion"). Se fabrica un
      bloque `<!-- CITA CONGELADA a9b638ba:docs/loop/REPORTE.md -->` con una
      frase de ausencia que NO esta en ese blob. Tiene que salir EXIT 1
      nombrando la linea. Y su contraprueba va DENTRO del mismo caso: el mismo
      bloque con una frase que SI esta verbatim en ese blob tiene que salir
      EXIT 0.

QUIEN FABRICA, LIMPIA (P.16): los sujetos de (B), (C) y (D) se escriben en un
temporal y se borran siempre, tambien si el arnes revienta. El sujeto de (A) no
se fabrica: se lee de git.

USO:
  python scripts/loop/vuelta146_2b_mutacion_ausencias.py
"""
import io
import os
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GUARDA = os.path.join(RAIZ, "scripts", "loop", "verificar_ausencias_del_reporte.py")

REF_CONGELADO = "a9b638ba"
RUTA_CONGELADA = "docs/loop/REPORTE.md"
# La frase de la 3.c, la que la caida 4.1 del acta 145 nombra. NO es el
# veredicto de nada: es la AGUJA que se busca en la salida del proceso.
AGUJA_3C = "no existe en el repositorio ninguna lista canonica de libros"
BARRIDO_BUENO = "SALIDA_V146_2C_BARRIDO_VERDE.txt"
NO_BARRIDO = "SALIDA_V146_MOTOR_APERTURA.txt"


def correr(argv):
    r = subprocess.run([sys.executable, GUARDA] + argv, cwd=RAIZ,
                       capture_output=True, text=True)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def escribir_temporal(texto):
    fd, ruta = tempfile.mkstemp(suffix=".md", prefix="v146_2b_")
    os.close(fd)
    with io.open(ruta, "w", encoding="utf-8") as f:
        f.write(texto)
    return ruta


def blob_congelado():
    r = subprocess.run(["git", "show", "%s:%s" % (REF_CONGELADO, RUTA_CONGELADA)],
                       cwd=RAIZ, capture_output=True)
    if r.returncode != 0:
        return None
    return r.stdout.decode("utf-8", "replace")


def frase_real_del_blob(blob):
    """Una linea del blob congelado que DISPARA el vocabulario, elegida POR
    COMPUTO y no tecleada: la primera que contiene la aguja de la 3.c. Es lo
    que hace que la contraprueba de (D) no pueda ser un literal inventado."""
    for linea in blob.split("\n"):
        if AGUJA_3C in linea:
            return linea.strip()
    return None


def main():
    temporales = []
    try:
        resultados = []

        # (A) CASO ROJO SOBRE SUJETO CONGELADO
        cod_a, sal_a = correr(["--ref", REF_CONGELADO, "--reporte", RUTA_CONGELADA])
        nombra_3c = AGUJA_3C in sal_a
        ok_a = (cod_a == 1) and nombra_3c
        print("(A) CASO ROJO, sujeto congelado %s:%s" % (REF_CONGELADO, RUTA_CONGELADA))
        print("    exit %r (se esperaba 1) | nombra la afirmacion de la 3.c: %s"
              % (cod_a, nombra_3c))
        for ln in sal_a.splitlines():
            if AGUJA_3C in ln:
                print("      %s" % ln.strip()[:170])
        print("    VEREDICTO: %s" % ("OK" if ok_a else "ROJO"))
        resultados.append(("A caso rojo sobre el reporte congelado de la 145", ok_a))

        # (B) CASO VERDE
        verde = (u"# SUJETO FABRICADO (B)\n\n"
                 u"Barrido en `%s`: el control A2.6 **no existe** en el codigo.\n" % BARRIDO_BUENO)
        ruta_b = escribir_temporal(verde)
        temporales.append(ruta_b)
        cod_b, sal_b = correr(["--reporte", ruta_b])
        ok_b = (cod_b == 0)
        print("")
        print("(B) CASO VERDE, ausencia respaldada por %s" % BARRIDO_BUENO)
        print("    exit %r (se esperaba 0)" % cod_b)
        for ln in sal_b.splitlines():
            if ln.startswith("VERDE") or ln.startswith("ROJO") or "COBERTURA DE AUSENCIAS:" in ln:
                print("      %s" % ln.strip()[:170])
        print("    VEREDICTO: %s" % ("OK" if ok_b else "ROJO"))
        resultados.append(("B caso verde con barrido sellado detras", ok_b))

        # (C) MUTACION DEL CASO VERDE: se cambia SOLO la cita
        mutado = verde.replace(BARRIDO_BUENO, NO_BARRIDO)
        ruta_c = escribir_temporal(mutado)
        temporales.append(ruta_c)
        cod_c, sal_c = correr(["--reporte", ruta_c])
        nombra_marca = "BARRIDO EXHAUSTIVO" in sal_c and NO_BARRIDO in sal_c
        ok_c = (cod_c == 1) and nombra_marca
        print("")
        print("(C) MUTACION DEL VERDE: la misma frase citando %s, que existe y NO es barrido"
              % NO_BARRIDO)
        print("    exit %r (se esperaba 1) | nombra el fichero y la marca que le falta: %s"
              % (cod_c, nombra_marca))
        for ln in sal_c.splitlines():
            if "AUSENCIA MAL RESPALDADA" in ln:
                print("      %s" % ln.strip()[:200])
        print("    VEREDICTO: %s" % ("OK" if ok_c else "ROJO"))
        resultados.append(("C el sello del barrido muerde, no solo la falta de cita", ok_c))

        # (D) LA CITA CONGELADA NO ES UN INTERRUPTOR
        blob = blob_congelado()
        real = frase_real_del_blob(blob) if blob else None
        if real is None:
            print("")
            print("(D) ROJO PREVIO: no se pudo montar el sujeto (no se leyo el blob congelado)")
            resultados.append(("D la cita congelada se comprueba contra su ref", False))
        else:
            falsa = (u"# SUJETO FABRICADO (D.1), CITA FALSA\n\n"
                     u"<!-- CITA CONGELADA %s:%s -->\n"
                     u"no existe ninguna cosa que este texto se acaba de inventar\n"
                     u"<!-- FIN CITA CONGELADA -->\n" % (REF_CONGELADO, RUTA_CONGELADA))
            ruta_d1 = escribir_temporal(falsa)
            temporales.append(ruta_d1)
            cod_d1, sal_d1 = correr(["--reporte", ruta_d1])
            nombra_cita = "CITA CONGELADA" in sal_d1 and "NO esta en ese blob" in sal_d1

            buena = (u"# SUJETO FABRICADO (D.2), CITA DE VERDAD\n\n"
                     u"<!-- CITA CONGELADA %s:%s -->\n%s\n"
                     u"<!-- FIN CITA CONGELADA -->\n" % (REF_CONGELADO, RUTA_CONGELADA, real))
            ruta_d2 = escribir_temporal(buena)
            temporales.append(ruta_d2)
            cod_d2, sal_d2 = correr(["--reporte", ruta_d2])

            ok_d = (cod_d1 == 1) and nombra_cita and (cod_d2 == 0)
            print("")
            print("(D) LA CITA CONGELADA SE COMPRUEBA CONTRA SU REF")
            print("    D.1 texto inventado dentro del bloque: exit %r (se esperaba 1) | "
                  "lo nombra: %s" % (cod_d1, nombra_cita))
            for ln in sal_d1.splitlines():
                if "CITA CONGELADA" in ln and "NO esta" in ln:
                    print("      %s" % ln.strip()[:200])
            print("    D.2 contraprueba, la linea REAL del blob elegida por computo: "
                  "exit %r (se esperaba 0)" % cod_d2)
            print("      linea usada: %r" % real[:120])
            print("    VEREDICTO: %s" % ("OK" if ok_d else "ROJO"))
            resultados.append(("D la cita congelada se comprueba contra su ref", ok_d))

        print("")
        print("=" * 78)
        buenas = sum(1 for _, ok in resultados if ok)
        for rot, ok in resultados:
            print("  %-62s %s" % (rot, "OK" if ok else "ROJO"))
        print("")
        print("CASOS QUE MUERDEN: %d de %d" % (buenas, len(resultados)))
        return 0 if buenas == len(resultados) else 1
    finally:
        for t in temporales:
            try:
                os.remove(t)
            except OSError:
                pass


if __name__ == "__main__":
    raise SystemExit(main())
