# -*- coding: utf-8 -*-
r"""_v207_t1d_correcciones.py . TAREA 1.d DE LA VUELTA 207: LAS DOS CAIDAS DE
REPORTE QUE EL ACTA 206 LEVANTO (`E.1` y `E.2`), CORREGIDAS EN EL REPORTE
ARCHIVADO DE LA 206 POR CORRECCION DECLARADA Y CON EL TEXTO VIEJO ENTERO ENCIMA
(`EJECUTOR.md` 8: *"una correccion que tapa lo que corrige no se puede
auditar"*).

COMPUTO DE UNA VUELTA, CON PREFIJO DE GUION BAJO, fuera del censo y fuera de la
nomina (moratoria de `AUDITOR.md` 6.3). NO ESCRIBE NINGUN LECTOR NUEVO: mide con
`hashlib` y `git show`, y coloca por busqueda de literal.

LAS CIFRAS NO SE COPIAN DEL ENCARGO NI DEL ACTA: LAS MIDE ESTE FICHERO. El
encargo lo pide expresamente para la `E.1` (*"Mide los dos tu y publica los dos,
no copies los mios"*).

LA REGLA DE LA `1.e` DEL ENCARGO, QUE ES EL HALLAZGO `7.3` DEL ACTA 206, SE
APLICA AQUI Y ES LA QUE HACE FALTA PARA LA `E.2`: **una salida sellada que una
vuelta posterior vuelve a correr deja de ser evidencia de la vuelta que la
sello**. Por eso el rechazo del tallador de la 205 se lee con
`git show 78ca7176:docs/loop/SALIDA_V205_TALLADOR_RECHAZO.txt` y NUNCA del
fichero de hoy, que la vuelta 206 piso en el commit `a75ff760`.

LAS GUARDAS, Y SON LAS QUE PUEDEN CAER:
  (a) cada ancla tiene que aparecer EXACTAMENTE UNA VEZ en el fichero destino; si
      aparece 0 o mas de 1, este computo CAE EN ROJO y no escribe nada;
  (b) al salir, NI UNA LINEA del texto de entrada puede faltar, en orden, en el
      de salida: la correccion solo puede ANADIR;
  (c) la segunda corrida no escribe nada (idempotencia por el literal de la
      marca).

USO:
  python scripts/loop/_v207_t1d_correcciones.py
  python scripts/loop/_v207_t1d_correcciones.py --escribir
"""
import argparse
import hashlib
import io
import os
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)

DESTINO = os.path.join(LOOP, "reportes", "REPORTE_V206.md")
REL_DESTINO = "docs/loop/reportes/REPORTE_V206.md"
COMMIT_205 = "78ca7176"
COMMIT_206_T1 = "a75ff760"
RUTA_NO_MORDIO = "docs/loop/SALIDA_V206_NO_MORDIO.txt"
RUTA_RECHAZO = "docs/loop/SALIDA_V205_TALLADOR_RECHAZO.txt"

MARCA_E1 = "CORRECCION DECLARADA DE LA VUELTA 207, SOBRE LA `E.1` DEL ACTA 206"
MARCA_E2 = "CORRECCION DECLARADA DE LA VUELTA 207, SOBRE LA `E.2` DEL ACTA 206"

# LAS DOS ANCLAS. Son el ULTIMO renglon del parrafo que se corrige: la
# correccion se pega DESPUES, y el parrafo viejo queda entero encima.
ANCLA_E1 = ("LF, sha256 `cffa5cd0724d0427` en disco y `cffa5cd0724d0427` "
            "normalizado a LF.")
ANCLA_E2 = "ciclo entero hoy, en mi turno, y sus valores quedaron en esos nombres."


def git_bytes(ref_ruta):
    r = subprocess.run(["git", "show", ref_ruta], cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout


def dos_convenciones(datos):
    lf = datos.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return (len(datos), len(lf),
            hashlib.sha256(datos).hexdigest(), hashlib.sha256(lf).hexdigest())


def medir_disco(rel, w, etiqueta):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(p):
        w("   %s: NO EXISTE (ausencia, no cero)" % rel)
        return None
    d, lf, sd, sl = dos_convenciones(io.open(p, "rb").read())
    w("   %s %s: %d bytes en disco y %d normalizado a LF" % (etiqueta, rel, d, lf))
    w("      sha256 disco %s | sha256 LF %s" % (sd[:16], sl[:16]))
    w("      sha256 disco COMPLETO: %s" % sd)
    w("      sha256 LF COMPLETO   : %s" % sl)
    return d, lf, sd, sl


def bloque_e1(med, w):
    d, lf, sd, sl = med
    p = []
    a = p.append
    a("")
    a("> **%s.** El renglon de arriba se queda **entero y sin tocar**, porque una"
      % MARCA_E1)
    a("> correccion que tapa lo que corrige no se puede auditar (`EJECUTOR.md` 8).")
    a("> **LO QUE DICE Y ES FALSO:** que el `sha256` de disco y el normalizado a LF")
    a("> de `%s` son los dos `cffa5cd0724d0427`." % RUTA_NO_MORDIO)
    a("> **LO QUE MIDO YO EN LA VUELTA 207, con `hashlib` sobre el fichero y sobre")
    a("> el mismo fichero con los `CRLF` cambiados por `LF`, y NO copiado de nadie:**")
    a("> **%d** bytes en disco y **%d** normalizado a LF, **sha256 de disco" % (d, lf))
    a("> `%s`** y **sha256 LF `%s`**. **Los dos son distintos**, y"
      % (sd[:16], sl[:16]))
    a("> la propia linea corregida ya lo probaba sin saberlo: **%d** contra **%d**"
      % (d, lf))
    a("> bytes solo puede salir de que el fichero tiene `CRLF`, y entonces los dos")
    a("> `sha256` no pueden coincidir. **La cifra de bytes era correcta; el `sha256`")
    a("> de disco era el de LF escrito dos veces.**")
    a("> **LOS DOS COMPLETOS, PARA QUE SE PUEDAN REHACER:** disco")
    a("> `%s`," % sd)
    a("> LF `%s`." % sl)
    a("> **ESTA CAIDA NO ACUMULA** (`AUDITOR.md` 4, letra afinada del 27 ago 2026,")
    a("> citada por el acta 206 en su `E.1`): vive en prosa de acompanamiento de una")
    a("> linea de evidencia, no en tabla, cabecera ni conclusion. **La conclusion de")
    a("> la seccion 3.0 no se mueve ni un digito.**")
    a("")
    return p


def bloque_e2(sellado, hoy, w):
    sd_bytes, sd_lf, sd_sha, sl_sha, cifras_sello = sellado
    hd, hlf, hsd, hsl, cifras_hoy = hoy
    p = []
    a = p.append
    a("")
    a("> **%s.** El parrafo de arriba se queda **entero y sin tocar**"
      % MARCA_E2)
    a("> (`EJECUTOR.md` 8). **LO QUE SE CORRIGE ES LA PROCEDENCIA, NO EL HECHO.**")
    a("> **LO QUE DICE Y ES FALSO:** que el **19** y el **18** son *lo que dice el")
    a("> rechazo que aquella vuelta dejo sellado*. **No lo son.** Ese `19 / 18` es el")
    a("> contenido que **esta misma vuelta 206** escribio encima de")
    a("> `%s` al volver a correr el tallador, en el" % RUTA_RECHAZO)
    a("> commit `%s`." % COMMIT_206_T1)
    a("> **LO QUE LA VUELTA 205 SELLO DE VERDAD, LEIDO POR MI CON")
    a("> `git show %s:%s`:**" % (COMMIT_205, RUTA_RECHAZO))
    for l in cifras_sello:
        a("> `%s`" % l)
    a("> Ese blob mide **%d** bytes y **%d** normalizado a LF, sha256 LF"
      % (sd_bytes, sd_lf))
    a("> **`%s`**." % sl_sha[:16])
    a("> **Y ESTO ES LO QUE EL MISMO NOMBRE DE FICHERO DICE HOY EN DISCO**, que es")
    a("> de donde salio el `19 / 18`: **%d** bytes en disco y **%d** normalizado a"
      % (hd, hlf))
    a("> LF, sha256 disco **`%s`** y sha256 LF **`%s`**."
      % (hsd[:16], hsl[:16]))
    for l in cifras_hoy:
        a("> `%s`" % l)
    a("> **LA REGLA QUE ESTO DEJA, Y ES EL HALLAZGO `7.3` DEL ACTA 206:** una salida")
    a("> sellada que una vuelta posterior vuelve a correr **deja de ser evidencia de")
    a("> la vuelta que la sello**. La fuente correcta es")
    a("> `git show <commit de aquella vuelta>:<ruta>`, nunca el fichero de hoy.")
    a("> **LA CONCLUSION DEL `D.1` SE SOSTIENE Y NO SE TOCA:** los seis")
    a("> `SALIDA_V205_*_APERTURA.txt` no existian antes de la vuelta 206, y el acta")
    a("> 206 lo verifico aparte midiendo que los seis se anaden **una sola vez en")
    a("> toda la historia de git, y es en `%s`**. Lo que estaba mal era"
      % COMMIT_206_T1)
    a("> de donde se decia que salia la cifra. **ESTA CAIDA NO ACUMULA**, por la")
    a("> misma letra que la `E.1`: prosa de un discutible.")
    a("")
    return p


def insertar(lineas, ancla, bloque, w, etiqueta):
    """PEGA EL BLOQUE JUSTO DESPUES DE LA LINEA DEL ANCLA. Devuelve (lineas, ok).
    CAE EN ROJO si el ancla no aparece exactamente una vez."""
    hits = [i for i, l in enumerate(lineas) if l.strip() == ancla]
    w("   %s: el ancla aparece %d vez(ces)" % (etiqueta, len(hits)))
    if len(hits) != 1:
        w("      ROJO: se necesita exactamente 1. NO SE ESCRIBE NADA.")
        return lineas, False
    i = hits[0]
    w("      ancla en la linea %d: %s" % (i + 1, lineas[i][:78]))
    return lineas[:i + 1] + bloque + lineas[i + 1:], True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--escribir", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA 207, TAREA 1.d: LAS DOS CAIDAS DE REPORTE DEL ACTA 206,")
    w("CORREGIDAS EN EL REPORTE ARCHIVADO DE LA 206 POR CORRECCION DECLARADA")
    w("=" * 78)
    w("")

    w("A) EL SUJETO AL ENTRAR, POR LAS DOS CONVENCIONES")
    med_dest0 = medir_disco(REL_DESTINO, w, "destino")
    if med_dest0 is None:
        w("   ROJO: el reporte archivado de la 206 no existe. NO SE ESCRIBE.")
        print(NL.join(L))
        return 1
    texto0 = io.open(DESTINO, encoding="utf-8").read().replace(chr(13) + NL, NL)
    w("   CIFRA lineas: %d" % len(texto0.split(NL)))
    w("")

    w("B) LA `E.1`. LOS DOS `sha256` DE %s, MEDIDOS POR MI" % RUTA_NO_MORDIO)
    w("   (el encargo lo manda expresamente: no se copian los del auditor)")
    med_e1 = medir_disco(RUTA_NO_MORDIO, w, "medido hoy:")
    if med_e1 is None:
        w("   ROJO: el fichero de la evidencia no esta. NO SE ESCRIBE.")
        print(NL.join(L))
        return 1
    c, blob = git_bytes("%s:%s" % ("d42f73a9", RUTA_NO_MORDIO))
    if c == 0:
        bd, blf, bsd, bsl = dos_convenciones(blob)
        w("   EL MISMO FICHERO EN EL COMMIT DE CIERRE DE LA 206 (d42f73a9), leido")
        w("   con git show: %d bytes | %d LF | sha256 LF %s" % (bd, blf, bsl[:16]))
        w("   (git guarda el blob ya normalizado, y por eso su sha calza con el LF")
        w("    del disco y no con el de disco)")
    w("   LA HISTORIA DEL FICHERO, PARA SABER SI ALGUIEN LO VOLVIO A CORRER")
    r = subprocess.run(["git", "log", "--format=%h %s", "--", RUTA_NO_MORDIO],
                       cwd=RAIZ, capture_output=True)
    for l in r.stdout.decode("utf-8", errors="replace").splitlines():
        w("      %s" % l[:90])
    w("")

    w("C) LA `E.2`. LO QUE LA 205 SELLO, LEIDO DE GIT Y NO DEL FICHERO DE HOY")
    w("   (regla `1.e` del encargo, hallazgo `7.3` del acta 206)")
    c, blob = git_bytes("%s:%s" % (COMMIT_205, RUTA_RECHAZO))
    if c != 0:
        w("   ROJO: git show no pudo leer el blob sellado. NO SE ESCRIBE.")
        print(NL.join(L))
        return 1
    sd_bytes, sd_lf, sd_sha, sl_sha = dos_convenciones(blob)
    texto_sello = blob.decode("utf-8", errors="replace").replace(chr(13) + NL, NL)
    cifras_sello = [l.strip() for l in texto_sello.split(NL)
                    if l.strip().startswith("CIFRA")]
    w("   git show %s:%s -> %d bytes | %d LF | sha256 LF %s"
      % (COMMIT_205, RUTA_RECHAZO, sd_bytes, sd_lf, sl_sha[:16]))
    for l in cifras_sello:
        w("      SELLADO> %s" % l)
    med_hoy = medir_disco(RUTA_RECHAZO, w, "el mismo nombre HOY:")
    if med_hoy is None:
        w("   ROJO: el fichero de hoy no esta. NO SE ESCRIBE.")
        print(NL.join(L))
        return 1
    texto_hoy = io.open(os.path.join(RAIZ, RUTA_RECHAZO.replace("/", os.sep)),
                        encoding="utf-8").read().replace(chr(13) + NL, NL)
    cifras_hoy = [l.strip() for l in texto_hoy.split(NL)
                  if l.strip().startswith("CIFRA")]
    for l in cifras_hoy:
        w("      HOY> %s" % l)
    w("   LA HISTORIA DEL FICHERO, QUE ES LA PRUEBA DE QUE SE VOLVIO A CORRER:")
    r = subprocess.run(["git", "log", "--format=%h %s", "--", RUTA_RECHAZO],
                       cwd=RAIZ, capture_output=True)
    for l in r.stdout.decode("utf-8", errors="replace").splitlines():
        w("      %s" % l[:90])
    w("")

    w("D) LA IDEMPOTENCIA, MIRADA ANTES DE TOCAR NADA")
    ya1 = MARCA_E1 in texto0
    ya2 = MARCA_E2 in texto0
    w("   la correccion de la `E.1` YA ESTA: %s" % ("SI" if ya1 else "NO"))
    w("   la correccion de la `E.2` YA ESTA: %s" % ("SI" if ya2 else "NO"))
    w("")

    w("E) LA COLOCACION, POR ANCLA Y NO POR NUMERO DE LINEA")
    lineas = texto0.split(NL)
    ok = True
    if not ya1:
        lineas, ok1 = insertar(lineas, ANCLA_E1, bloque_e1(med_e1, w), w, "`E.1`")
        ok = ok and ok1
    if not ya2:
        lineas, ok2 = insertar(
            lineas, ANCLA_E2,
            bloque_e2((sd_bytes, sd_lf, sd_sha, sl_sha, cifras_sello),
                      (med_hoy[0], med_hoy[1], med_hoy[2], med_hoy[3], cifras_hoy),
                      w),
            w, "`E.2`")
        ok = ok and ok2
    w("")
    if not ok:
        w("   ROJO: alguna ancla no aparecio exactamente una vez. NO SE ESCRIBE.")
        print(NL.join(L))
        return 1

    nuevo = NL.join(lineas)
    w("F) LA GUARDA DE ADICION PURA, ANTES DE ESCRIBIR")
    viejas = texto0.split(NL)
    nuevas = nuevo.split(NL)
    faltan = 0
    j = 0
    for l in viejas:
        while j < len(nuevas) and nuevas[j] != l:
            j += 1
        if j >= len(nuevas):
            faltan += 1
        else:
            j += 1
    w("   CIFRA lineas del texto de ENTRADA que NO estan, en orden, en el de")
    w("   SALIDA: %d" % faltan)
    w("   (si no es 0, es ROJO y no se escribe)")
    if faltan != 0:
        w("   ROJO. NO SE ESCRIBE NADA.")
        print(NL.join(L))
        return 1
    w("   CIFRA lineas al entrar: %d | al salir: %d | anadidas: %d"
      % (len(viejas), len(nuevas), len(nuevas) - len(viejas)))
    w("")

    if a.escribir and (not ya1 or not ya2):
        io.open(DESTINO, "w", encoding="utf-8", newline=NL).write(nuevo)
        w("G) ESCRITO %s" % REL_DESTINO)
    elif a.escribir:
        w("G) NO SE ESCRIBE: las dos correcciones ya estaban. IDEMPOTENTE.")
    else:
        w("G) MODO MEDICION: no se escribe nada.")
    w("")

    w("H) EL SUJETO AL SALIR, REMEDIDO Y NO HEREDADO")
    med_dest1 = medir_disco(REL_DESTINO, w, "destino")
    w("   CIFRA crecimiento en bytes de disco: %d"
      % (med_dest1[0] - med_dest0[0]))
    w("   CIFRA crecimiento en bytes LF: %d" % (med_dest1[1] - med_dest0[1]))
    w("")
    w("FIN")

    salida = NL.join(L) + NL
    print(salida)
    io.open(os.path.join(LOOP, "SALIDA_V207_T1D_CORRECCIONES.txt"),
            "w", encoding="utf-8", newline=NL).write(salida)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
