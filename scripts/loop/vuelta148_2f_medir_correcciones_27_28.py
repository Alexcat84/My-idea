# -*- coding: utf-8 -*-
"""vuelta148_2f_medir_correcciones_27_28.py . LA MEDICION DE HOY PARA LAS
CORRECCIONES 27 Y 28 (TAREA 2.6 de la vuelta 148).

POR QUE EXISTE. El acta 147 declara DOS cifras falsas del propio auditor en su
acta 146 (su seccion 4.3): el SEIS de las coladas que son CINCO, y las DOCE
lineas de calibracion que son SIETE. `EJECUTOR.md` 2 dice que una nota vieja o
un acta previa NUNCA son fuente de una cifra nueva: se citan como contraste. Asi
que las dos se RE MIDEN AQUI, con instrumento propio, y si algo discrepa se
declara en vez de resolverse copiando.

CORRECCION 27, LAS COLADAS. El acta 146 publica "SEIS escapes en esta misma
pagina, CINCO de ellos sin barrido en ventana". Se mide el ESCAPE PURO: las
frases que disparan SOLO formulas NUEVAS (las que la vuelta 147 anadio), o sea
las que el vocabulario de DOCE de la vuelta 146 no veia en absoluto. Se mide
sobre DOS sujetos congelados y se publican los dos, porque la palabra "pagina"
del acta admite las dos lecturas y elegir una callando la otra seria elegir la
que conviene:
  (a) `docs/loop/_v146_acta_seccion.md`, la PAGINA DEL ACTA 146, congelada en su
      commit de nacimiento;
  (b) el `docs/loop/REPORTE.md` de la vuelta 146, congelado por ref, que es el
      sujeto que midio la escalada de la vuelta 147.

CORRECCION 28, LAS LINEAS DE CALIBRACION. El acta 146 dice "con doce lineas de
calibracion encima" del umbral. Se cuentan las lineas de comentario CONTIGUAS
que van inmediatamente encima de `UMBRAL_SEMANTICO` en `scripts/intra_dominio.py`,
con sus numeros de linea, sin teclear ninguno.

USO:
  python scripts/loop/vuelta148_2f_medir_correcciones_27_28.py
"""
import io
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
os.chdir(RAIZ)

import verificar_ausencias_del_reporte as G

ACTA_146 = "docs/loop/_v146_acta_seccion.md"
REPORTE = "docs/loop/REPORTE.md"
INTRA = os.path.join(RAIZ, "scripts", "intra_dominio.py")


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    if r.returncode != 0:
        raise SystemExit("ROJO PREVIO: git %s fallo" % " ".join(args))
    return r.stdout.decode("utf-8", "replace")


def ref_de_nacimiento(ruta):
    """El commit que ANADE ese fichero, leido de git y no tecleado."""
    salida = git(["log", "--diff-filter=A", "--pretty=format:%H", "--", ruta]).split()
    if len(salida) != 1:
        raise SystemExit("ROJO PREVIO: %s tiene %d commits que lo anaden" % (ruta, len(salida)))
    return salida[0]


def ref_del_reporte_146():
    """El ultimo commit que toco REPORTE.md ANTES del HEAD de apertura de la
    vuelta 147, que es el reporte de la 146. Computado, no tecleado."""
    head_147 = io.open(os.path.join(RAIZ, "docs", "loop",
                                    "SALIDA_V147_HEAD_APERTURA.txt"),
                       encoding="utf-8").read().strip()
    refs = git(["log", "--pretty=format:%H", head_147, "--", REPORTE]).split()
    if not refs:
        raise SystemExit("ROJO PREVIO: ningun commit toca %s antes de %s" % (REPORTE, head_147))
    return refs[0]


def escape_puro(texto, viejas, nuevas):
    """Las frases que disparan SOLO formulas NUEVAS: las que el vocabulario de
    doce no veia en absoluto."""
    puros, mixtas = [], []
    for fr in G.dividir_frases(texto):
        b = " ".join(fr.lower().split())
        hay_v = [f for f in viejas if f in b]
        hay_n = [f for f in nuevas if f in b]
        if hay_n and not hay_v:
            puros.append((fr, hay_n))
        elif hay_n and hay_v:
            mixtas.append((fr, hay_n, hay_v))
    return puros, mixtas


def main():
    viejas = set(G.FORMULAS_DE_AUSENCIA_VIEJAS)
    nuevas = [f for f in G.FORMULAS_DE_AUSENCIA if f not in viejas]
    print("VOCABULARIO: %d viejas (vuelta 146) + %d anadidas (vuelta 147) = %d activas"
          % (len(viejas), len(nuevas), len(G.FORMULAS_DE_AUSENCIA)))
    print("")

    print("=" * 78)
    print("CORRECCION 27. LAS COLADAS DEL ACTA 146")
    print("=" * 78)
    print("CONTRASTE, y es una cita y no una fuente: el acta 146 publica SEIS escapes en su")
    print("pagina, cinco sin barrido en ventana. El acta 147, en su 4.3.a, se corrige sola y")
    print("dice CINCO. Lo que sigue es MI medicion de hoy.")
    print("")

    sujetos = []
    ref_acta = ref_de_nacimiento(ACTA_146)
    sujetos.append(("(a) la PAGINA DEL ACTA 146", ref_acta, ACTA_146,
                    G.leer_ref(ref_acta, ACTA_146)))
    ref_rep = ref_del_reporte_146()
    sujetos.append(("(b) el REPORTE de la vuelta 146", ref_rep, REPORTE,
                    G.leer_ref(ref_rep, REPORTE)))

    cifras = {}
    for rotulo, ref, ruta, texto in sujetos:
        puros, mixtas = escape_puro(texto, viejas, nuevas)
        cifras[rotulo] = len(puros)
        print("SUJETO CONGELADO %s: %s:%s" % (rotulo, ref[:8], ruta))
        print("   ESCAPE PURO (dispara SOLO formulas nuevas): %d frase(s)" % len(puros))
        for fr, hay_n in puros:
            print("      por %s | %s" % (", ".join(sorted(hay_n)), " ".join(fr.split())[:110]))
        print("   MIXTAS (ya disparaban alguna vieja, no anaden cobertura): %d" % len(mixtas))
        print("")

    print("CIFRA coladas del acta 146 por escape puro sobre la pagina del acta: %d frases"
          % cifras["(a) la PAGINA DEL ACTA 146"])
    print("CIFRA coladas del acta 146 por escape puro sobre el reporte de la 146: %d frases"
          % cifras["(b) el REPORTE de la vuelta 146"])
    print("")

    print("=" * 78)
    print("CORRECCION 28. LAS LINEAS DE CALIBRACION")
    print("=" * 78)
    print("CONTRASTE, y es una cita y no una fuente: el acta 146 dice DOCE lineas de")
    print("calibracion encima del umbral. El acta 147, en su 4.3.b, se corrige sola y dice")
    print("SIETE, de la 61 a la 67. Lo que sigue es MI conteo de hoy sobre el fichero.")
    print("")
    lineas = io.open(INTRA, encoding="utf-8").read().split("\n")
    idx = [i for i, l in enumerate(lineas) if l.startswith("UMBRAL_SEMANTICO")]
    if len(idx) != 1:
        raise SystemExit("ROJO PREVIO: %d lineas UMBRAL_SEMANTICO" % len(idx))
    fin = idx[0]
    ini = fin
    while ini - 1 >= 0 and lineas[ini - 1].lstrip().startswith("#"):
        ini -= 1
    print("scripts/intra_dominio.py, linea %d: %s" % (fin + 1, lineas[fin].strip()))
    print("LAS LINEAS DE COMENTARIO CONTIGUAS INMEDIATAMENTE ENCIMA, una a una:")
    for i in range(ini, fin):
        print("   linea %d: %s" % (i + 1, lineas[i].strip()[:96]))
    n = fin - ini
    print("")
    print("   primera: linea %d | ultima: linea %d" % (ini + 1, fin))
    print("   LA LINEA DE ENCIMA DEL BLOQUE (linea %d), que NO es comentario de calibracion: %s"
          % (ini, lineas[ini - 1].strip()[:70]))
    print("")
    print("CIFRA lineas de calibracion encima del umbral: %d lineas" % n)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
