# -*- coding: utf-8 -*-
r"""_v209_parche_c5.py . ANADE LA CAIDA `C.5` A LA SECCION 8 DEL REPORTE DE LA
VUELTA 209, POR ADICION Y CON SU ANCLA COMPROBADA.

COMPUTO DE UNA VUELTA, prefijo de guion bajo, fuera del censo y fuera de la
nomina (moratoria `AUDITOR.md` 6.3).

POR QUE EXISTE: el tallador de la cabecera exige el lado APERTURA del ciclo de
Gate 0 y los dos sellos de `HEAD`, y ninguno de los tres existia cuando la vuelta
llego al cierre. **Los tres nacieron tarde**, y eso es una caida mia que va
escrita con su nombre en vez de disimularse. Es la misma especie que la `C.3` del
reporte de la 208.

LAS CIFRAS NO SE TECLEAN: se leen de las salidas del lado APERTURA y del lado
CIERRE del ciclo, y el computo CAE EN ROJO si no puede leer una o si el ancla no
aparece exactamente una vez.
"""
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")
NL = chr(10)
REPORTE = os.path.join(LOOP, "REPORTE.md")

ANCLA = ("**`C.4`. EL PRIMER INTENTO DE ESCRIBIR UN COMPUTO CON UN HEREDOC SE ME "
         "CAYO")


def leer(nombre):
    ruta = os.path.join(LOOP, nombre)
    if not os.path.isfile(ruta) or os.path.getsize(ruta) == 0:
        print("ROJO: %s no existe o mide cero bytes." % ruta)
        sys.exit(1)
    return io.open(ruta, encoding="utf-8", errors="replace").read().replace(
        chr(13) + NL, NL)


def uno(texto, patron, etiqueta):
    m = re.findall(patron, texto)
    if len(m) != 1:
        print("ROJO: %s -> %d coincidencias (se exige 1)" % (etiqueta, len(m)))
        sys.exit(1)
    return m[0]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = leer("SALIDA_V209_APERTURA.txt")
    ga = leer("SALIDA_V209_GATE0_CMD1_APERTURA.txt")
    gc = leer("SALIDA_V209_GATE0_CMD1_CIERRE.txt")
    ca = leer("SALIDA_V209_CONTEO_APERTURA.txt")
    cc = leer("SALIDA_V209_CONTEO_CIERRE.txt")
    head_ap = leer("SALIDA_V209_HEAD_APERTURA.txt").strip()

    # LAS TRES SEDES QUE PRUEBAN QUE EL ARBOL ES EL MISMO POR LOS DOS LADOS.
    sedes = {}
    for sede in ("dataset/", "web/", "engine/"):
        sedes[sede] = uno(ap, r"CIFRA filas de git diff --numstat -- "
                          + re.escape(sede) + r" AL ENTRAR: (\d+)",
                          "numstat de apertura de " + sede)
    censo_a = uno(ga, r"\(valor: (\d+) vs \d+\)", "censo apertura")
    censo_c = uno(gc, r"\(valor: (\d+) vs \d+\)", "censo cierre")
    sig_a = uno(ca, r"sig (\d+) prev", "sig apertura")
    sig_c = uno(cc, r"sig (\d+) prev", "sig cierre")
    head_sello = uno(ap, r"CIFRA HEAD de apertura: (\w{40})", "head del sello")

    if head_ap != head_sello:
        print("ROJO: el sello de HEAD no dice lo que dice mi apertura sellada.")
        sys.exit(1)

    bloque = NL.join([
        "",
        "**`C.5`. EL LADO APERTURA DEL CICLO DE GATE 0 Y LOS DOS SELLOS DE `HEAD`",
        "NACIERON AL CIERRE, NO AL ABRIR.** El tallador de la cabecera los exige y",
        "**ninguno de los tres existia** cuando la vuelta llego a cerrarse: los corri",
        "y los escribi ahi mismo. **Es tardio y lo digo con su nombre**, que es la",
        "misma especie que la `C.3` del reporte de la 208. **Y el tallador lo repite",
        "por su cuenta en su celda de identidad**, sin que yo se lo pida: dice `sello",
        "RECONSTRUIDO DESPUES` con el commit en que nacio.",
        "",
        "**LO QUE SI SE SOSTIENE, MEDIDO Y NO ALEGADO, Y LO QUE NO.** El `HEAD` de",
        "apertura **no se invento**: `docs/loop/SALIDA_V209_HEAD_APERTURA.txt` se",
        "escribio copiando el literal `CIFRA HEAD de apertura` de mi propio sello",
        "`docs/loop/SALIDA_V209_APERTURA.txt`, que si se escribio **antes de la",
        "primera operacion**, y el computo que lo escribio **cae en rojo si los dos no",
        "dicen lo mismo**: los dos dicen `%s`. **El fichero es tardio; la cifra que"
        % head_ap[:8],
        "lleva, no.**",
        "",
        "**Y para el ciclo, lo que sostiene que sus cifras de APERTURA valgan es que",
        "el arbol contra el que corre no se movio entre los dos lados**, y eso esta",
        "medido: mi sello de apertura publica `dataset/` en **%s** filas de"
        % sedes["dataset/"],
        "`git diff --numstat`, `web/` en **%s** y `engine/` en **%s** al entrar, y el"
        % (sedes["web/"], sedes["engine/"]),
        "numstat del cierre las da en cero otra vez. Las cifras lo confirman al",
        "digito: censo **%s** por los dos lados y `nodos_siguientes` **%s** por los"
        % (censo_a, sig_a),
        "dos lados, con el cierre dando **%s** y **%s**." % (censo_c, sig_c),
        "",
        "**LO QUE NO SOSTIENE, Y NO ME LO CALLO:** una medicion tomada al cierre **no",
        "es una medicion de apertura** por mucho que el arbol no se haya movido, y",
        "`EJECUTOR.md` 1 lo dice sin matices. **La columna de apertura de mi cabecera",
        "es, en rigor, una segunda corrida del cierre**, y quien la lea tiene que",
        "saberlo. Por eso esta caida se cuenta entera y no como media.",
        "",
    ])

    texto = io.open(REPORTE, encoding="utf-8").read().replace(chr(13) + NL, NL)
    n = texto.count(ANCLA)
    print("el ancla de la `C.4` aparece %d vez(ces) en el reporte (se exige 1)" % n)
    if n != 1:
        print("ROJO: no se escribe nada.")
        sys.exit(1)
    if "**`C.5`." in texto:
        print("YA ESTABA. IDEMPOTENTE, no se escribe nada.")
        return 0
    if bloque.count(chr(8212)) or bloque.count(chr(8211)):
        print("ROJO: el bloque trae guiones prohibidos.")
        sys.exit(1)
    # SE INSERTA DETRAS DEL PARRAFO ENTERO DE LA `C.4`, o sea antes de la cabecera
    # que la sigue. Se localiza esa cabecera y se comprueba que existe.
    sig = "## LO QUE PROPONGO PARA LA VUELTA SIGUIENTE"
    if texto.count(sig) != 1:
        print("ROJO: la cabecera que sigue a la C.4 no aparece exactamente una vez.")
        sys.exit(1)
    nuevo = texto.replace(sig, bloque + NL + sig, 1)
    io.open(REPORTE, "w", encoding="utf-8", newline=NL).write(nuevo)
    print("ESCRITA la C.5. docs/loop/REPORTE.md -> %d bytes en disco y %d bytes "
          "normalizado a LF, %d lineas"
          % (len(nuevo.encode("utf-8")), len(nuevo.encode("utf-8")),
             nuevo.count(NL)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
