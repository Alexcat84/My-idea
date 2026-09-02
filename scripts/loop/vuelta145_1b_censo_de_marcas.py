# -*- coding: utf-8 -*-
r"""vuelta145_1b_censo_de_marcas.py . INSTRUMENTO PROPIO DEL EJECUTOR,
VUELTA 145, TAREA 1.b (CORRECCION 21) Y MEDICION DE PARTIDA DE LA TAREA 2.a.

QUE MIDE, y lo mide POR SI MISMO, sin copiar ninguna cifra del acta 144:
  (1) CUANTAS VECES aparece cada una de las SEIS marcas (apertura y cierre de
      CABECERA TALLADA, de COMMITS TALLADOS y de COBERTURA DE LA GUARDA) en un
      reporte dado, con la POSICION de cada ocurrencia (linea y offset).
  (2) QUE RECORTA HOY quitar_bloques_cubiertos() de ese reporte y QUE SE QUEDA
      FUERA: por cada uno de sus TRES pares, el tramo que quita (anclado, hoy,
      en la PRIMERA ocurrencia de cada marca por `texto.find`) y el tramo del
      SEGUNDO par, si existe, que NO se quita y por tanto SI se parsea.
  (3) EL VEREDICTO Y LA LINEA DE COBERTURA que la guarda de verdad publica
      sobre ese sujeto, corriendo `verificar_cifras_del_reporte.py` ENTERA
      sobre el (no se reimplementa su maquina: se invoca).
  (4) Con --pegar-cobertura, lo mismo DESPUES de pegar la linea real de
      COBERTURA DENTRO DEL SEGUNDO bloque de marcas, que es justo donde el
      reporte de la 144 anuncia "(pegada abajo tras la segunda corrida)".

EL SUJETO ES UN REF DE GIT, NUNCA EL ARBOL VIVO (patron de
SUJETO_FIJO_V135_2E_REPORTE_134.md, banco 9.10): se pasa <ref>:<ruta> y se lee
con `git show`, de modo que la medicion de hoy se sigue reproduciendo manana
aunque docs/loop/REPORTE.md se reescriba. Un sujeto vivo es lo que puso en rojo
a la bateria VIEJAS en la vuelta 144 (acta 144, 4.8).

USO:
  python scripts/loop/vuelta145_1b_censo_de_marcas.py b7f07648:docs/loop/REPORTE.md
  python scripts/loop/vuelta145_1b_censo_de_marcas.py b7f07648:docs/loop/REPORTE.md --pegar-cobertura
"""
import argparse
import os
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
GUARDA = os.path.join(RAIZ, "scripts", "loop", "verificar_cifras_del_reporte.py")
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))

import verificar_cifras_del_reporte as G

MARCAS = [
    ("CABECERA TALLADA, abre", G.MARCA_CABECERA_ABRE),
    ("CABECERA TALLADA, cierra", G.MARCA_CABECERA_CIERRA),
    ("COMMITS TALLADOS, abre", G.MARCA_COMMITS_ABRE),
    ("COMMITS TALLADOS, cierra", G.MARCA_COMMITS_CIERRA),
    ("COBERTURA DE LA GUARDA, abre", G.MARCA_COBERTURA_ABRE),
    ("COBERTURA DE LA GUARDA, cierra", G.MARCA_COBERTURA_CIERRA),
]

PARES = [
    ("COBERTURA", G.MARCA_COBERTURA_ABRE, G.MARCA_COBERTURA_CIERRA),
    ("COMMITS", G.MARCA_COMMITS_ABRE, G.MARCA_COMMITS_CIERRA),
    ("CABECERA", G.MARCA_CABECERA_ABRE, G.MARCA_CABECERA_CIERRA),
]


def leer(sujeto):
    if ":" in sujeto and not os.path.exists(sujeto):
        r = subprocess.run(["git", "show", sujeto], cwd=RAIZ, capture_output=True)
        if r.returncode != 0:
            raise SystemExit("ROJO: no se pudo leer %s" % sujeto)
        return r.stdout.decode("utf-8")
    with open(sujeto, encoding="utf-8") as f:
        return f.read()


def ocurrencias(texto, marca):
    """Todas las posiciones de `marca`, cada una con su numero de linea."""
    fuera = []
    i = texto.find(marca)
    while i != -1:
        fuera.append((i, texto.count("\n", 0, i) + 1))
        i = texto.find(marca, i + 1)
    return fuera


def correr_la_guarda(texto):
    """LA GUARDA ENTERA sobre este sujeto, escrito a un temporal DENTRO de
    docs/loop/ (la guarda resuelve rutas de SALIDA_V*.txt relativas a esa
    carpeta). Devuelve (exit, linea_de_cobertura, unidades_fuera)."""
    fd, ruta = tempfile.mkstemp(prefix="_v145_sujeto_", suffix=".md", dir=LOOP)
    os.close(fd)
    try:
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(texto)
        r = subprocess.run([sys.executable, GUARDA, "--reporte", ruta],
                           cwd=RAIZ, capture_output=True, text=True)
        cobertura = ""
        fuera = None
        for l in (r.stdout or "").splitlines():
            if l.startswith("COBERTURA:"):
                cobertura = l
                marca = "unidades vistas FUERA del vocabulario: "
                if marca in l:
                    resto = l.split(marca, 1)[1]
                    fuera = int(resto.split(" ", 1)[0])
        return r.returncode, cobertura, fuera
    finally:
        os.remove(ruta)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("sujeto")
    ap.add_argument("--pegar-cobertura", action="store_true")
    a = ap.parse_args()

    texto = leer(a.sujeto)
    print("SUJETO: %s" % a.sujeto)
    print("CARACTERES: %d   LINEAS: %d" % (len(texto), texto.count("\n") + 1))
    print("")
    print("(1) CENSO DE LAS SEIS MARCAS")
    for rotulo, marca in MARCAS:
        occ = ocurrencias(texto, marca)
        print("  %-32s %d vez/veces  %s" % (
            rotulo, len(occ),
            ", ".join("linea %d (offset %d)" % (l, o) for o, l in occ) or "sin ocurrencia"))
    print("")
    print("(2) QUE RECORTA HOY quitar_bloques_cubiertos(), ANCLADO EN LA PRIMERA OCURRENCIA")
    for rotulo, abre, cierra in PARES:
        oa = ocurrencias(texto, abre)
        oc = ocurrencias(texto, cierra)
        if not oa or not oc:
            print("  %-10s sin par de marcas: no recorta nada" % rotulo)
            continue
        i, j = oa[0][0], oc[0][0] + len(cierra)
        print("  %-10s RECORTA lineas %d a %d (%d caracteres)"
              % (rotulo, oa[0][1], oc[0][1], j - i))
        for k in range(1, min(len(oa), len(oc))):
            p, q = oa[k][0], oc[k][0] + len(cierra)
            print("  %-10s QUEDA FUERA el bloque %d.o, lineas %d a %d (%d caracteres): SE PARSEA"
                  % ("", k + 1, oa[k][1], oc[k][1], q - p))
    print("")
    code, cobertura, fuera = correr_la_guarda(texto)
    print("(3) LA GUARDA ENTERA SOBRE ESTE SUJETO: EXIT %d" % code)
    print("  %s" % (cobertura or "(no publico linea de COBERTURA)"))
    print("  unidades fuera del vocabulario: %s" % fuera)

    if a.pegar_cobertura:
        oa = ocurrencias(texto, G.MARCA_COBERTURA_ABRE)
        oc = ocurrencias(texto, G.MARCA_COBERTURA_CIERRA)
        print("")
        if len(oa) < 2 or len(oc) < 2:
            print("(4) NO HAY SEGUNDO BLOQUE DE COBERTURA en este sujeto: nada que pegar dentro")
            return 0
        corte = oc[1][0]
        mutado = texto[:corte] + cobertura + "\n" + texto[corte:]
        code2, cobertura2, fuera2 = correr_la_guarda(mutado)
        print("(4) PEGADA LA LINEA REAL DE COBERTURA DENTRO DEL SEGUNDO BLOQUE (linea %d)"
              % oc[1][1])
        print("  linea pegada: %s" % cobertura)
        print("  la guarda sobre el sujeto mutado: EXIT %d" % code2)
        print("  %s" % (cobertura2 or "(no publico linea de COBERTURA)"))
        print("  unidades fuera del vocabulario: %s -> %s" % (fuera, fuera2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
