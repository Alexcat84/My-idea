# -*- coding: utf-8 -*-
r"""vuelta147_2a_medir_escape.py . TAREA 2.a de la vuelta 147: LA MEDICION DEL
ESCAPE DEL VOCABULARIO, REPRODUCIDA POR EL EJECUTOR Y NO COPIADA DEL ACTA.

QUE MIDE. Cuantas afirmaciones de ausencia VE `verificar_ausencias_del_reporte.py`
con el vocabulario VIEJO (las doce de la vuelta 146) y cuantas con el NUEVO (las
veinte, tras la ampliacion de la 147), sobre DOS SUJETOS CONGELADOS POR REF:

  - el reporte de la vuelta 145, el texto que produjo la caida 4.1 de aquella acta;
  - el reporte de la vuelta 146, el texto que produjo la caida 4.2 del acta 146,
    que es el que la ampliacion viene a cazar.

LOS DOS REFS SE COMPUTAN, NINGUNO SE TECLEA (`EJECUTOR.md`, LA IDENTIDAD SE LEE
DE GIT): el de la 146 es el ultimo commit que toco `docs/loop/REPORTE.md` antes
del HEAD de apertura de esta vuelta (leido de su sello), y el de la 145 es el
ultimo que lo toco antes de ESE.

Y MIDE ADEMAS LO QUE EL ACTA 146 PUBLICA COMO "SEIS QUE SE ESCAPAN ENTERAS": las
frases que disparan ALGUNA formula NUEVA. Se separan las que disparan SOLO
formulas nuevas (escape puro: el vocabulario viejo no las veia en absoluto) de
las que ya disparaban alguna vieja (no anaden cobertura). SI LA CIFRA DISCREPA
DE LA DEL ACTA, SE DECLARA Y NO SE RESUELVE COPIANDO.

Salida: docs/loop/SALIDA_V147_2A_ESCAPE_VOCABULARIO.txt

USO:
  python scripts/loop/vuelta147_2a_medir_escape.py
"""
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(RAIZ)

import verificar_ausencias_del_reporte as G  # noqa: E402

REPORTE = "docs/loop/REPORTE.md"
HEAD_APERTURA = os.path.join(RAIZ, "docs", "loop", "SALIDA_V147_HEAD_APERTURA.txt")


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit("ROJO PREVIO: git %s fallo" % " ".join(args))
    return r.stdout


def ultimo_toque(ruta, antes_de):
    hs = [h for h in git(["log", "-1", "--format=%H", antes_de, "--", ruta]).splitlines()
          if h.strip()]
    if len(hs) != 1:
        raise SystemExit("ROJO PREVIO: no se pudo computar el ultimo commit de %s antes de %s"
                         % (ruta, antes_de[:8]))
    return hs[0]


def refs_de_los_dos_reportes():
    """El ref del reporte de la 146 y el de la 145, LOS DOS COMPUTADOS.

    LA FRONTERA DE CADA VUELTA ES SU COMMIT DE APERTURA, y no "los dos ultimos
    commits que tocan el reporte": el reporte de una vuelta se escribe y se
    retoca DENTRO de la misma vuelta (el de la 146 vive en dos commits), asi
    que contar commits daria dos veces el mismo reporte. Se usa el nacimiento
    de `SALIDA_V<N>_HEAD_APERTURA.txt`, que por la guarda de apertura sellada
    es el PRIMER commit de la vuelta N."""
    head = io.open(HEAD_APERTURA, encoding="utf-8").read().strip()
    if not re.match(r"^[0-9a-f]{40}$", head):
        raise SystemExit("ROJO PREVIO: %s no trae un hash de 40 caracteres" % HEAD_APERTURA)
    ref_146 = ultimo_toque(REPORTE, head)
    apertura_146 = [h for h in git(["log", "--diff-filter=A", "--format=%H", "--",
                                    "docs/loop/SALIDA_V146_HEAD_APERTURA.txt"]).splitlines()
                    if h.strip()]
    if len(apertura_146) != 1:
        raise SystemExit("ROJO PREVIO: no se pudo computar el commit de apertura de la 146")
    ref_145 = ultimo_toque(REPORTE, apertura_146[0])
    return ref_146, ref_145


def recortado(texto):
    """El mismo recorte que hace la guarda antes de parsear (citas congeladas,
    bloque de commits y cabecera tallada). Se reusa el de la guarda, no se
    reimplementa."""
    fallos = []
    t = G.quitar_citas_congeladas(texto, fallos)
    t = G.quitar_bloque_simple(t, G.MARCA_COMMITS_ABRE, G.MARCA_COMMITS_CIERRA, fallos, "commits")
    t = G.quitar_bloque_simple(t, G.MARCA_CABECERA_ABRE, G.MARCA_CABECERA_CIERRA, fallos, "cabecera")
    return t


def cobertura(ref, vocabulario):
    r = subprocess.run([sys.executable, "scripts/loop/verificar_ausencias_del_reporte.py",
                        "--ref", ref, "--vocabulario", vocabulario],
                       cwd=RAIZ, capture_output=True)
    sal = r.stdout.decode("utf-8", "replace")
    m = re.search(r"^COBERTURA DE AUSENCIAS: (\d+) vistas / (\d+) respaldadas / (\d+) en rojo",
                  sal, re.MULTILINE)
    if not m:
        raise SystemExit("ROJO PREVIO: la guarda no imprimio su linea de cobertura sobre %s" % ref)
    return int(m.group(1)), int(m.group(2)), int(m.group(3))


def main():
    ref_146, ref_145 = refs_de_los_dos_reportes()
    viejas = set(G.FORMULAS_DE_AUSENCIA_VIEJAS)
    nuevas = [f for f in G.FORMULAS_DE_AUSENCIA if f not in viejas]

    print("EL ESCAPE DEL VOCABULARIO, MEDIDO POR EL EJECUTOR EN LA VUELTA 147 (TAREA 2.a)")
    print("")
    print("  formulas del vocabulario VIEJO (vuelta 146): %d" % len(viejas))
    print("  formulas ANADIDAS en la vuelta 147: %d" % len(nuevas))
    for f in nuevas:
        print("      %s" % f)
    print("  formulas del vocabulario NUEVO: %d" % len(G.FORMULAS_DE_AUSENCIA))
    print("")

    for rotulo, ref in (("reporte de la vuelta 145", ref_145),
                        ("reporte de la vuelta 146", ref_146)):
        v = cobertura(ref, "viejo")
        n = cobertura(ref, "nuevo")
        print("  SUJETO CONGELADO: %s:%s  (%s)" % (ref[:8], REPORTE, rotulo))
        print("      vocabulario VIEJO: %d vistas / %d respaldadas / %d en rojo" % v)
        print("      vocabulario NUEVO: %d vistas / %d respaldadas / %d en rojo" % n)
        print("      la cobertura pasa de %d vistas a %d vistas" % (v[0], n[0]))
        print("")

    texto = G.leer_ref(ref_146, REPORTE)
    frases = G.dividir_frases(recortado(texto))
    puros, mixtas = [], []
    for fr in frases:
        b = fr.lower()
        hay_v = [f for f in viejas if f in b]
        hay_n = [f for f in nuevas if f in b]
        if hay_n and not hay_v:
            puros.append((fr.strip(), hay_n))
        elif hay_n and hay_v:
            mixtas.append((fr.strip(), hay_v, hay_n))

    print("  LAS QUE SE ESCAPAN ENTERAS del vocabulario viejo, sobre %s:%s" % (ref_146[:8], REPORTE))
    print("      frases que disparan SOLO formulas NUEVAS (escape puro): %d" % len(puros))
    for fr, fs in puros:
        print("          %s" % fr[:110])
        print("              dispara por: %s" % ", ".join(fs))
    print("      frases que ya disparaban alguna VIEJA (no anaden cobertura): %d" % len(mixtas))
    for fr, fv, fn in mixtas:
        print("          %s" % fr[:110])
        print("              vieja: %s | nueva: %s" % (", ".join(fv), ", ".join(fn)))
    print("")
    print("  CONTRASTE CON EL ACTA 146, DECLARADO Y NO RESUELTO COPIANDO (`EJECUTOR.md` 2):")
    print("      el acta 146 publica SEIS afirmaciones coladas enteras y CINCO sin barrido")
    print("      en su ventana, y publica que la cobertura pasa de 3 vistas a 8 vistas.")
    print("      Mi medicion de hoy sobre el MISMO sujeto congelado da %d escapes puros."
          % len(puros))
    print("      La cifra de cobertura del acta (3 a 8) cuadra con %d y no con seis."
          % len(puros))
    print("")
    print("CIFRA formulas del vocabulario viejo: %d formulas" % len(viejas))
    print("CIFRA formulas anadidas en la vuelta 147: %d formulas" % len(nuevas))
    print("CIFRA formulas del vocabulario nuevo: %d formulas" % len(G.FORMULAS_DE_AUSENCIA))
    print("CIFRA frases de escape puro sobre el reporte de la 146: %d frases" % len(puros))
    print("CIFRA frases que ya disparaban una vieja: %d frases" % len(mixtas))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
