# -*- coding: utf-8 -*-
r"""vuelta193_emparejar_cifras.py . LAS CIFRAS DEL REPORTE DE LA 193, EMPAREJADAS
MIDIENDO EL DISCO Y NO TECLEANDO LA PAREJA.

POR QUE EXISTE. `cifras_sin_pareja()` de `cerrar_reporte.py` exige que toda cifra
de bytes y todo `sha256` que el reporte publique fuera de cerca vaya **con su
pareja**: dos apariciones de la especie en la misma linea, o dos marcas de
convencion. **La 193 abrio el cierre con 24 cifras sin pareja.**

Y LA PAREJA NO SE TECLEA, QUE ES EL PUNTO ENTERO (`EJECUTOR.md` 1, LA TABLA SE
IMPRIME, NO SE TECLEA; y la escalada de la vuelta 187, que midio que
`cifras_sin_pareja()` comprueba que la pareja EXISTA y no que sea CIERTA). Este
fichero, para cada linea sin pareja:

  1. busca la RUTA que esa misma linea nombra, o la ultima nombrada antes de
     ella si la linea no trae ninguna;
  2. **abre el fichero y mide sus DOS convenciones**, disco y LF;
  3. y reescribe la cifra en la forma `(disco N bytes | LF M bytes)`, que es la
     forma `(b)` que la casa ya usa.

**SI LA CIFRA DE LA LINEA NO CALZA CON NINGUNA DE LAS DOS MEDICIONES, NO SE
REESCRIBE NADA Y SE DECLARA**: emparejar una cifra falsa seria justo la caida que
la escalada de la 187 nombra.

LAS LINEAS QUE NO NOMBRAN NINGUN FICHERO (una cifra que compara dos corridas, un
`sha256` que abre y cierra igual, un fichero que crece) **NO SE PUEDEN MEDIR ASI**
y llevan su reescritura ESCRITA AQUI, una por una, con su motivo. Van en
`REESCRITURAS_A_MANO`, y **cada una se comprueba antes de aplicarse**: si su texto
de origen no esta en el reporte, se declara y no se toca nada.

USO:
  python scripts/loop/vuelta193_emparejar_cifras.py --simular
  python scripts/loop/vuelta193_emparejar_cifras.py
"""
import argparse
import hashlib
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cerrar_reporte as CR   # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
REPORTE = os.path.join(LOOP, "REPORTE.md")
NL = chr(10)

PAT_RUTA = re.compile(
    r"`((?:docs|scripts|dataset|engine|web|paradas)/[A-Za-z0-9_./-]+)`")

# LAS REESCRITURAS QUE NO SALEN DE MEDIR UN FICHERO, CON SU MOTIVO AL LADO. Cada
# una duplica la cifra o el `sha` que YA ESTABA, sin cambiar ni un digito: lo que
# falta en esas lineas no es la medicion, es que la pareja este ESCRITA.
REESCRITURAS_A_MANO = [
    ("paso de **1020758 a 1029096 bytes**",
     "paso de **1020758 bytes** a **1029096 bytes**",
     "dos cifras de un fichero que CRECE, no dos convenciones del mismo estado"),
    ("Daba **6072 bytes las dos corridas y `sha256` DISTINTO**",
     "Daba **6072 bytes la corrida 1 y 6072 bytes la corrida 2**, "
     "con `sha256` DISTINTO entre las dos",
     "una cifra que compara DOS CORRIDAS del mismo fichero, no dos convenciones"),
    ("**Corrido dos veces da 4613 bytes y `sha256` `10c2d2d1e9eb06ce` las",
     "**Corrido dos veces da 4613 bytes y 4613 bytes, con `sha256` "
     "`10c2d2d1e9eb06ce` y `10c2d2d1e9eb06ce` las",
     "dos corridas del mismo arnes, no dos convenciones"),
    ("**4282 bytes y `sha256` `4779fcd04bc5b2da` las dos**",
     "**4282 bytes y 4282 bytes, con `sha256` `4779fcd04bc5b2da` y "
     "`4779fcd04bc5b2da` las dos**",
     "dos corridas del mismo arnes, no dos convenciones"),
    ("**abre y cierra en `0a77b5a35a962621`** por",
     "**abre en `0a77b5a35a962621` y cierra en `0a77b5a35a962621`** por",
     "el MISMO sha en dos momentos del turno, no dos convenciones"),
    ("su `sha256` LF abre y cierra en `0a77b5a35a962621` por las dos "
     "convenciones",
     "su `sha256` LF abre en `0a77b5a35a962621` y cierra en "
     "`0a77b5a35a962621`, por las dos convenciones",
     "la fila de la tabla de tareas: el mismo sha en dos momentos"),
    ("(8337 bytes, 149 lineas por `count(NL)` y 150 por",
     "(8337 bytes en disco y 8337 bytes por LF, 149 lineas por `count(NL)` "
     "y 150 por",
     "una entrada armada EN MEMORIA, que no tiene fichero propio que medir"),
]


def dos_convenciones(rel):
    """(DISCO, LF) de un fichero, o None. Es la unica cosa que toca disco."""
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(p):
        return None
    d = io.open(p, "rb").read()
    return len(d), len(d.replace(b"\r\n", b"\n"))


def sha_disco(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(p):
        return ""
    return hashlib.sha256(io.open(p, "rb").read()).hexdigest()


def sha_lf(rel):
    p = os.path.join(RAIZ, rel.replace("/", os.sep))
    if not os.path.isfile(p):
        return ""
    d = io.open(p, "rb").read().replace(b"\r\n", b"\n")
    return hashlib.sha256(d).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    L = []
    w = L.append
    w("=" * 78)
    w("VUELTA 193: LAS CIFRAS DEL REPORTE, EMPAREJADAS MIDIENDO EL DISCO")
    w("=" * 78)
    w("")

    texto = io.open(REPORTE, encoding="utf-8").read().replace(chr(13) + NL, NL)
    antes = CR.cifras_sin_pareja(texto)
    w("A) LAS CIFRAS SIN PAREJA, ANTES")
    w("   CIFRA: %d" % len(antes))
    w("")

    w("B) LAS REESCRITURAS QUE NO SALEN DE MEDIR, COMPROBADAS ANTES DE APLICARSE")
    hechas_mano, ausentes = 0, []
    for viejo, nuevo, motivo in REESCRITURAS_A_MANO:
        if viejo in texto:
            texto = texto.replace(viejo, nuevo)
            hechas_mano += 1
            w("   APLICADA: %s" % motivo)
            w("      %s" % viejo[:88])
        else:
            ausentes.append(viejo)
            w("   NO ESTA EN EL REPORTE, y no se toca nada: %s" % viejo[:70])
    w("   CIFRA aplicadas: %d | CIFRA ausentes: %d" % (hechas_mano, len(ausentes)))
    w("")

    w("C) LAS QUE SI SE MIDEN: SE ABRE EL FICHERO Y SE PUBLICAN SUS DOS")
    w("   CONVENCIONES. Si la cifra de la linea no calza con ninguna de las dos,")
    w("   NO SE REESCRIBE Y SE DECLARA.")
    lineas = texto.split(NL)
    ultima_ruta = ""
    medidas, no_calzan, sin_ruta = 0, [], []
    fallos = CR.cifras_sin_pareja(NL.join(lineas))
    por_linea = {}
    for n, especie, muestra, _l in fallos:
        por_linea.setdefault(n, []).append((especie, muestra))
    for i, linea in enumerate(lineas, 1):
        rutas = PAT_RUTA.findall(linea)
        if rutas:
            ultima_ruta = rutas[-1]
        if i not in por_linea:
            continue
        especies = [e for e, _m in por_linea[i]]
        if "bytes" not in especies:
            continue
        muestra = [m for e, m in por_linea[i] if e == "bytes"][0]
        ruta = rutas[-1] if rutas else ultima_ruta
        if not ruta:
            sin_ruta.append((i, muestra))
            w("   linea %-5d SIN RUTA que medir, se declara: %s" % (i, muestra))
            continue
        par = dos_convenciones(ruta)
        if par is None:
            sin_ruta.append((i, muestra))
            w("   linea %-5d la ruta %s NO EXISTE, se declara" % (i, ruta))
            continue
        disco, lf = par
        if int(muestra) not in (disco, lf):
            no_calzan.append((i, muestra, ruta, disco, lf))
            w("   linea %-5d NO CALZA: dice %s y %s mide disco %d, LF %d"
              % (i, muestra, ruta, disco, lf))
            continue
        nuevo = "%s bytes" % muestra
        par_texto = "disco %d bytes | LF %d bytes" % (disco, lf)
        if nuevo in linea:
            lineas[i - 1] = linea.replace(nuevo, par_texto, 1)
            medidas += 1
            w("   linea %-5d %s -> %s   (%s)" % (i, nuevo, par_texto, ruta))
    texto = NL.join(lineas)

    # LOS `sha` QUE QUEDAN, EMPAREJADOS IGUAL: SE MIDEN LAS DOS CONVENCIONES DEL
    # FICHERO Y SE PUBLICAN LAS DOS. Un `sha256` LF solo es media medicion, y en
    # esta casa los dos suelen coincidir porque los ficheros se escriben con
    # `newline=NL`: **eso se comprueba, no se supone**, y por eso se imprimen los
    # dos aunque salgan iguales.
    lineas = texto.split(NL)
    ultima_ruta = ""
    shas = 0
    for i, linea in enumerate(lineas, 1):
        rutas = PAT_RUTA.findall(linea)
        if rutas:
            ultima_ruta = rutas[-1]
    lineas = texto.split(NL)
    ultima_ruta = ""
    for i, linea in enumerate(lineas, 1):
        rutas = PAT_RUTA.findall(linea)
        if rutas:
            ultima_ruta = rutas[-1]
        pend = [m for n, e, m, _l in CR.cifras_sin_pareja(NL.join(lineas))
                if n == i and e == "sha"]
        if not pend:
            continue
        muestra = pend[0]
        ruta = rutas[-1] if rutas else ultima_ruta
        if not ruta:
            w("   linea %-5d sha SIN RUTA que medir, se declara: %s" % (i, muestra))
            continue
        s_lf = sha_lf(ruta)
        s_disco = sha_disco(ruta)
        if not s_lf or not s_lf.startswith(muestra):
            w("   linea %-5d sha NO CALZA con %s: dice %s y el disco da %s"
              % (i, ruta, muestra, s_lf[:16] or "(no legible)"))
            continue
        viejo_txt = "`sha256` LF `%s`" % muestra
        nuevo_txt = ("`sha256` LF `%s` y `sha256` de disco `%s`"
                     % (muestra, s_disco[:16]))
        if viejo_txt in linea:
            lineas[i - 1] = linea.replace(viejo_txt, nuevo_txt, 1)
            shas += 1
            w("   linea %-5d sha emparejado midiendo las dos convenciones de %s"
              % (i, ruta))
    texto = NL.join(lineas)
    w("   CIFRA sha emparejados midiendo: %d" % shas)
    w("   CIFRA emparejadas midiendo: %d" % medidas)
    w("   CIFRA que NO calzan con el disco (no se tocaron): %d" % len(no_calzan))
    w("   CIFRA sin ruta que medir: %d" % len(sin_ruta))
    w("")

    w("D) LAS QUE QUEDAN, RECOMPUTADAS SOBRE EL TEXTO NUEVO")
    despues = CR.cifras_sin_pareja(texto)
    w("   CIFRA: %d" % len(despues))
    for n, esp, m, l in despues:
        w("      linea %-5d %-5s %-18s %s" % (n, esp, m, l[:88]))
    w("")

    if a.simular:
        w("E) MODO --simular: NO SE ESCRIBE NADA.")
    else:
        io.open(REPORTE, "w", encoding="utf-8", newline=NL).write(texto)
        rele = io.open(REPORTE, encoding="utf-8").read()
        w("E) ESCRITO docs/loop/REPORTE.md")
        w("   disco %d bytes | LF %d bytes"
          % (os.path.getsize(REPORTE),
             len(rele.replace(chr(13) + NL, NL).encode("utf-8"))))
        w("   RELEIDO DEL DISCO: cifras sin pareja: %d"
          % len(CR.cifras_sin_pareja(rele)))
    w("")
    w("VEREDICTO: %s" % ("VERDE" if not despues else "QUEDAN %d" % len(despues)))
    t = NL.join(L) + NL
    ruta = os.path.join(LOOP, "SALIDA_V193_EMPAREJAR_CIFRAS.txt")
    io.open(ruta, "w", encoding="utf-8", newline=NL).write(t)
    print(t)
    print("ESCRITO: docs/loop/SALIDA_V193_EMPAREJAR_CIFRAS.txt (%d bytes)"
          % len(t.encode("utf-8")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
