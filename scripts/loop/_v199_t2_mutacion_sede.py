# -*- coding: utf-8 -*-
r"""_v199_t2_mutacion_sede.py . LA PRUEBA DE MUTACION DEL CASO ROJO DE LA TAREA 2
DE LA VUELTA 199.

QUE PRUEBA, Y POR QUE HACE FALTA: `EJECUTOR.md` 1, letra del 29 ago 2026, dice que
**ningun caso rojo se publica como prueba sin haber corrido antes su prueba de
mutacion**. El caso rojo de la TAREA 2 es *"la sede del turno no se movio"*, y
para probarlo hay que enseñar que **SIN la redireccion la sede SI se mueve**.

POR QUE ESTE FICHERO EXISTE Y NO ES MAQUINARIA NUEVA: la mutacion es
DESTRUCTIVA por naturaleza (quitar la redireccion BORRA
`docs/loop/_TURNO_DEL_AUDITOR.json`, que es la sede real del turno del auditor y
que **esta en `.gitignore`**, o sea que git no la puede devolver). Correrla dentro
del arnes de la nomina dejaria un arnes que destruye la sede cada vez que la
bateria pasa, que es exactamente lo que la TAREA 2 viene a reparar. Va aparte, con
prefijo `_` para que el censo de arneses no lo cuente, **NO entra en la nomina**
(congelada en 135 por `AUDITOR.md` 6.3) y se corre UNA VEZ.

COMO NO PIERDE LA SEDE, Y ESO SE MIDE, NO SE PROMETE:
  1. lee la sede ENTERA en bytes y la guarda en memoria y en un temporal;
  2. corre la copia MUTADA del arnes (sin la redireccion) en un proceso aparte;
  3. mide su `sha256`, que es el caso rojo mordiendo;
  4. la RESTAURA byte a byte y **REMIDE** que el `sha256` calza con el de entrada.

Y LA VARA ES EL CONTENIDO Y NO LA EXISTENCIA, cosa que esta prueba aprendio EN
ROJO contra si misma: `olvidar_todo()` BORRA el fichero, pero el `apuntar()`
siguiente LO VUELVE A CREAR con la bitacora del arnes dentro. Medir solo la
existencia daba VERDE sobre una sede PISADA, que es el fallar callado del banco 9.
Si el paso 4 no calza, este fichero sale ROJO y lo dice: una restauracion que no
se remide no es una restauracion.

USO:
  python scripts/loop/_v199_t2_mutacion_sede.py
"""
import hashlib
import io
import os
import shutil
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
AQUI = os.path.dirname(os.path.abspath(__file__))
NL = chr(10)
PY = sys.executable
SEDE = os.path.join(LOOP, "_TURNO_DEL_AUDITOR.json")
ARNES = os.path.join(AQUI, "vuelta182_tarea2_mutacion_apertura_auditor.py")

# LAS DOS MUTACIONES, Y VAN DOS PORQUE LA PRIMERA DESCUBRIO LA SEGUNDA CAPA.
#
# `M1` le quita al arnes la REDIRECCION. Se esperaba que borrara la sede, y NO la
# borra: salta la GUARDA que la reparacion de la 199 dejo puesta (*"si la
# redireccion no se aplico, NO se sigue: borraria la sede"*), el arnes sale con
# exitcode 1 y la sede queda entera. **Eso no es un fallo de la mutacion: es una
# segunda capa que no se sabia que estuviera midiendo, y se publica como caso.**
#
# `M2` le quita la REDIRECCION **Y** la GUARDA, que es el arnes tal como estaba
# ANTES de esta vuelta. Ahi si borra la sede, y esa es la mordida que el caso rojo
# de la TAREA 2 necesita enseñar.
#
# Cada `viejo` tiene que aparecer EXACTAMENTE UNA VEZ o esto cae antes de tocar
# nada.
M_REDIRECCION = (
    '    AP.RUTA_DEL_TURNO = os.path.join(carpeta_turno, "_TURNO_DEL_AUDITOR.json")'
    + NL + "    AP.LOOP = carpeta_turno" + NL)
M_GUARDA = (
    "    if AP.RUTA_DEL_TURNO == ruta_turno_real or AP.LOOP == loop_real:" + NL
    + "        fallos += 1" + NL
    + '        w("   ROJO: la redireccion no se aplico. NO se sigue: borraria la sede.")'
    + NL + "        return 1" + NL)


def sha(datos):
    return hashlib.sha256(datos).hexdigest()


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    L, casos, verdes = [], 0, 0
    w = L.append

    def caso(titulo, ok, detalle=""):
        nonlocal casos, verdes
        casos += 1
        if ok:
            verdes += 1
        w("   %-62s %s" % (titulo[:62], "VERDE" if ok else "ROJO"))
        if detalle:
            w("      %s" % detalle)

    w("=" * 78)
    w("VUELTA 199, TAREA 2: LA PRUEBA DE MUTACION DEL CASO ROJO.")
    w("SIN LA REDIRECCION, LA SEDE DEL TURNO QUEDA PISADA. CON ELLA, INTACTA.")
    w("=" * 78)
    w("")

    if not os.path.exists(SEDE):
        w("ROJO: no existe la sede %s. No se puede medir nada." % SEDE)
        w("VEREDICTO: ROJO")
        io.open(os.path.join(LOOP, "SALIDA_V199_T2_MUTACION_SEDE.txt"), "w",
                encoding="utf-8", newline=NL).write(NL.join(L) + NL)
        return 1

    original_sede = io.open(SEDE, "rb").read()
    sha_antes = sha(original_sede)
    w("LA SEDE AL ENTRAR: %d bytes, sha256 %s"
      % (len(original_sede), sha_antes[:16]))
    carpeta = tempfile.mkdtemp(prefix="v199_t2_")
    respaldo = os.path.join(carpeta, "respaldo_TURNO.json")
    io.open(respaldo, "wb").write(original_sede)
    caso("el respaldo se escribe y calza byte a byte con la sede",
         sha(io.open(respaldo, "rb").read()) == sha_antes)

    texto = io.open(ARNES, encoding="utf-8").read()
    ok_conteo = True
    for etiqueta, aguja in (("la redireccion", M_REDIRECCION),
                            ("la guarda de la redireccion", M_GUARDA)):
        veces = texto.count(aguja)
        caso("%s aparece EXACTAMENTE 1 vez en el arnes" % etiqueta, veces == 1,
             "veces contadas: %d" % veces)
        ok_conteo = ok_conteo and veces == 1
    if not ok_conteo:
        w("ROJO: la mutacion no es la que dice ser. NO SE CORRE NADA.")
        shutil.rmtree(carpeta, ignore_errors=True)
        w("VEREDICTO: ROJO")
        io.open(os.path.join(LOOP, "SALIDA_V199_T2_MUTACION_SEDE.txt"), "w",
                encoding="utf-8", newline=NL).write(NL.join(L) + NL)
        return 1

    mutado = os.path.join(AQUI, "_v199_t2_arnes_mutado_TEMPORAL.py")

    def correr_mutacion(etiqueta, texto_mutado):
        io.open(mutado, "w", encoding="utf-8", newline=NL).write(texto_mutado)
        try:
            r = subprocess.run([PY, mutado], cwd=RAIZ, capture_output=True,
                               text=True, encoding="utf-8", errors="replace")
            existe = os.path.exists(SEDE)
            # SE MIDE EL `sha256`, NO SOLO LA EXISTENCIA, Y ESO LO ENSEnO ESTA
            # MISMA PRUEBA EN ROJO: `olvidar_todo()` BORRA el fichero, pero el
            # `apuntar()` siguiente lo VUELVE A CREAR con la bitacora del arnes
            # dentro. Medir solo la existencia daba VERDE sobre una sede
            # PISADA, que es exactamente el fallar callado que el banco 9
            # prohibe. La vara es el contenido.
            actual = (sha(io.open(SEDE, "rb").read()) if existe else "NO EXISTE")
            w("   %s -> exitcode %d | la sede existe: %s | sha256 %s"
              % (etiqueta, r.returncode, existe, actual[:16]))
            return r.returncode, existe, actual
        finally:
            try:
                os.remove(mutado)
            except Exception:                            # noqa: BLE001
                pass

    w("")
    w("M1. SE LE QUITA SOLO LA REDIRECCION.")
    w("   Se esperaba que borrase la sede, y NO la borra: salta la GUARDA que la")
    w("   propia reparacion dejo puesta. Es una segunda capa, y se publica.")
    code1, existe1, sha1 = correr_mutacion(
        "M1", texto.replace(M_REDIRECCION, "    pass" + NL, 1))
    caso("M1: la GUARDA muerde y el arnes NO sigue (exitcode distinto de 0)",
         code1 != 0, "exitcode medido: %d" % code1)
    caso("M1: con la guarda puesta, la sede queda INTACTA byte a byte",
         sha1 == sha_antes, "sha256 tras M1: %s" % sha1[:16])

    w("")
    w("M2. SE LE QUITAN LA REDIRECCION **Y** LA GUARDA, que es el arnes tal como")
    w("   estaba ANTES de esta vuelta. Aqui es donde el caso rojo tiene que morder.")
    texto_m2 = texto.replace(M_REDIRECCION, "    pass" + NL, 1).replace(M_GUARDA, "", 1)
    code2, existe2, sha2 = correr_mutacion("M2", texto_m2)
    caso("M2: SIN redireccion NI guarda, LA SEDE QUEDA PISADA", sha2 != sha_antes,
         "sha256 al entrar %s | sha256 tras M2 %s (existe: %s)"
         % (sha_antes[:16], sha2[:16], existe2))
    caso("la copia mutada se retira del arbol (P.16)", not os.path.exists(mutado))

    w("")
    w("LA RESTAURACION, Y SE REMIDE: una restauracion que no se remide no lo es.")
    io.open(SEDE, "wb").write(original_sede)
    sha_despues = sha(io.open(SEDE, "rb").read())
    w("   sha256 al entrar:    %s" % sha_antes[:16])
    w("   sha256 al restaurar: %s" % sha_despues[:16])
    caso("LA SEDE QUEDA IDENTICA BYTE A BYTE A COMO ENTRO",
         sha_despues == sha_antes)
    shutil.rmtree(carpeta, ignore_errors=True)
    caso("el temporal se retira (P.16)", not os.path.exists(carpeta))

    w("")
    w("=" * 78)
    w("CASOS: %d | VERDES: %d | ROJOS: %d" % (casos, verdes, casos - verdes))
    w("VEREDICTO: %s" % ("VERDE" if verdes == casos else "ROJO"))
    w("=" * 78)
    w("")
    w("LO QUE ESTO SIGNIFICA, DICHO SIN ADORNO: el caso rojo de la TAREA 2 MUERDE.")
    w("Con la redireccion la sede no se mueve. Sin ella, y sin la guarda, el arnes")
    w("la BORRA y luego la REESCRIBE con su propio estado: el fichero sigue ahi y")
    w("su contenido ya no es el del auditor. Las dos cifras salen de medir.")

    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V199_T2_MUTACION_SEDE.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: %s (%d bytes)" % (ruta, len(t.encode("utf-8"))))
    return 0 if verdes == casos else 1


if __name__ == "__main__":
    sys.exit(main())
