# -*- coding: utf-8 -*-
r"""vuelta170_tarea1b_medir_tachadas_por_commit.py . TAREA 1.b de la vuelta 170.

MIDE, COMMIT A COMMIT, CUANTAS TACHADAS TIENE LA FILA DE LOS COLAPSOS DE
docs/plan/RECOMPUTO_3388.md, Y NOMBRA EL COMMIT EN QUE ENTRA CADA UNA.

POR QUE NACE. La caida `4.1` del acta 169: el comentario que la TAREA 2 de la
vuelta 169 escribio en `scripts/loop/vuelta166_tarea3_mutacion_retrato.py` dice
que "la vuelta 167 anadio una tachada", y eso es falso. Es una cifra en el texto
de una guarda, o sea la CUARTA SEDE, y por tanto CIFRA PUBLICADA. La correccion
va por el carril del banco `9.10` (frase vieja entera y tachada, correccion
fechada adosada debajo) y tiene que llevar LA TABLA DE COMMITS MEDIDA al lado.

LA TABLA SE MIDE AQUI Y NO SE COPIA DEL ACTA (EJECUTOR.md 2, "EL INSTRUMENTO
MANDA"): el acta del auditor dice 12 en `3ffc2091`, 13 en `33fe1380` y 13 desde
entonces, pero un acta previa NUNCA es fuente de una cifra nueva. Aqui se
recorre `git log --diff-filter=AM` sobre el fichero, se lee el BLOB de cada
commit y se cuenta la cadena con el LOCALIZADOR Y EL CONTADOR DEL PROPIO
INSTRUMENTO del retrato (`localizar_filas` y `anatomia`), no con un `grep`.

QUE IMPRIME:
  (a) la tabla commit a commit, con vuelta, fecha, tachadas y viva;
  (b) EL COMMIT EN QUE ENTRA LA DECIMOTERCERA, computado como el primero de la
      serie cuyo conteo llega a 13;
  (c) LA VUELTA de ese commit, que su asunto NO nombra, computada del invariante
      de la casa (los commits posteriores al `ACTA DE LA VUELTA N` son de la
      vuelta N mas 1) y no supuesta;
  (d) que la vuelta 167 NO movio esa fila. Es una busqueda negativa, asi que se
      publica con el comando que la produce y con el conteo que la sostiene.

TRES FUNCIONES SE EXPORTAN A PROPOSITO (`serie_medida`,
`nacimiento_de_la_tachada`, `vuelta_computada_de`): el arnes del retrato las
IMPORTA para su caso de anclaje de la TAREA 1.c. UNA SOLA FUENTE, sin copia.

CERO ESCRITURAS SOBRE EL REPO: solo lee git y el disco.

USO:
  python scripts/loop/vuelta170_tarea1b_medir_tachadas_por_commit.py
"""
import io
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta166_tarea3_retrato_de_las_a as T   # noqa: E402

RAIZ = T.RAIZ
RUTA = "docs/plan/RECOMPUTO_3388.md"
CLAVE = "colapsos"
LF = chr(10)
CR = chr(13)
TAB = chr(9)


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def vuelta_del_asunto(asunto):
    """La vuelta de un commit LEIDA de su asunto. None si el asunto no la
    nombra, y entonces se dice en vez de suponerla."""
    m = re.search(r"\bVUELTA\s+(\d+)\b", asunto.upper())
    return int(m.group(1)) if m else None


def serie_medida():
    """[(hash, vuelta_del_asunto, fecha, tachadas, viva, asunto)] en orden
    cronologico, contando la cadena del BLOB de cada commit con el localizador y
    el contador del PROPIO instrumento del retrato."""
    c, o = git(["log", "--reverse", "--diff-filter=AM",
                "--format=%H|%ad|%s", "--date=short", "--", RUTA])
    tabla = []
    for fila in [l for l in o.splitlines() if l.strip()]:
        h, fecha, asunto = fila.split("|", 2)
        c2, blob = git(["show", "%s:%s" % (h, RUTA)])
        if c2 != 0:
            continue
        lineas = blob.replace(CR + LF, LF).split(LF)
        halladas, _errores = T.localizar_filas(lineas)
        por_clave = dict((k, t) for k, n, t in halladas)
        if CLAVE not in por_clave:
            continue
        t = por_clave[CLAVE]
        _tach, viva, cuantas = T.anatomia(t)
        tabla.append((h, vuelta_del_asunto(asunto), fecha, cuantas, viva, asunto))
    return tabla


def nacimiento_de_la_tachada(n, tabla=None):
    """EL COMMIT EN QUE ENTRA LA n-ESIMA TACHADA, computado como el PRIMERO de la
    serie cuyo conteo llega a n. Devuelve la fila entera o None.

    Es una ESCALERA y no una consulta suelta: sirve para cualquier n, asi que
    anadir una tachada catorce manana NO mueve el nacimiento de la trece."""
    for fila in (tabla if tabla is not None else serie_medida()):
        if fila[3] >= n:
            return fila
    return None


def vuelta_computada_de(commit):
    """LA VUELTA DE UN COMMIT, COMPUTADA DE LAS ACTAS Y NO SUPUESTA: los commits
    posteriores al del `ACTA DE LA VUELTA N` pertenecen a la vuelta N mas 1.
    Devuelve None si no hay ningun acta anterior o el commit no esta en el log,
    en vez de inventarse una vuelta."""
    c, olog = git(["log", "--format=%H" + TAB + "%s", "-2000"])
    orden = [l.split(TAB, 1) for l in olog.splitlines() if TAB in l]
    hashes = [x[0] for x in orden]
    if commit not in hashes:
        return None
    for _hh, asu in orden[hashes.index(commit) + 1:]:
        m = re.match(r"^ACTA DE LA VUELTA (\d+) DEL AUDITOR", asu)
        if m:
            return int(m.group(1)) + 1
    return None


def tachadas_de_hoy():
    """Las tachadas que la fila tiene HOY en el arbol de trabajo."""
    lineas = io.open(T.DOC, encoding="utf-8").read().split(LF)
    halladas, _err = T.localizar_filas(lineas)
    por_clave = dict((k, t) for k, n, t in halladas)
    return T.anatomia(por_clave[CLAVE])[2]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 170, TAREA 1.b: LAS TACHADAS DE LA FILA DE LOS COLAPSOS,")
    print("MEDIDAS COMMIT A COMMIT CON EL LOCALIZADOR DEL PROPIO INSTRUMENTO")
    print("=" * 78)
    print("")

    print("A) LA SERIE DE COMMITS QUE TOCAN EL FICHERO")
    print("   comando: git log --reverse --diff-filter=AM --format=%H|%ad|%s"
          " --date=short -- " + RUTA)
    tabla = serie_medida()
    print("   CIFRA commits con la fila de los colapsos localizada: %d" % len(tabla))
    if not tabla:
        print("   ROJO: ningun commit trae la fila localizable.")
        return 1
    print("")

    print("B) LA TABLA, CONTADA DEL BLOB DE CADA COMMIT")
    print("   %-10s %-6s %-11s %-9s %-7s %s"
          % ("commit", "vuelta", "fecha", "tachadas", "viva", "asunto"))
    for h0, v0, f0, c0, vi0, a0 in tabla:
        print("   %-10s %-6s %-11s %-9d %-7s %s"
              % (h0[:8], v0 if v0 is not None else "(sin)", f0, c0,
                 vi0 if vi0 else "(sin)", a0[:46]))
    print("")

    print("C) EL COMMIT EN QUE ENTRA LA DECIMOTERCERA TACHADA, COMPUTADO")
    objetivo = 13
    fila = nacimiento_de_la_tachada(objetivo, tabla)
    if fila is None:
        print("   ROJO: ningun commit de la serie llega a %d tachadas." % objetivo)
        return 1
    h, v, fecha, cuantas, viva, asunto = fila
    anteriores = [f for f in tabla if f[3] < objetivo]
    print("   el primer commit cuya fila llega a %d tachadas: %s" % (objetivo, h[:8]))
    print("   su vuelta LEIDA de su asunto: %s"
          % (v if v is not None else "(el asunto no la nombra)"))
    print("   fecha: %s" % fecha)
    print("   asunto: %s" % asunto)
    if anteriores:
        ha, va, fa, ca = anteriores[-1][:4]
        print("   el commit inmediatamente anterior de la serie: %s (vuelta %s), con %d"
              % (ha[:8], va if va is not None else "(sin)", ca))
    print("   CIFRA tachadas en el ultimo commit de la serie: %d" % tabla[-1][3])
    print("")

    print("D) LA VUELTA 167, BUSCADA Y NO SUPUESTA")
    print("   (una busqueda negativa no se puede citar sin el comando que la produce)")
    de_167 = [f for f in tabla if f[1] == 167]
    print("   CIFRA commits de la serie cuyo asunto nombra la VUELTA 167: %d"
          % len(de_167))
    for f in de_167:
        print("      %s  %s" % (f[0][:8], f[5][:70]))
    conteos = sorted(set(f[3] for f in tabla))
    print("   CIFRA valores distintos de tachadas en toda la serie: %d (%s)"
          % (len(conteos), ", ".join(str(x) for x in conteos)))
    saltos = [(tabla[i - 1], tabla[i]) for i in range(1, len(tabla))
              if tabla[i][3] != tabla[i - 1][3]]
    print("   CIFRA puntos en que el conteo CAMBIA: %d" % len(saltos))
    for a, b in saltos:
        print("      %s (%d) -> %s (%d), vuelta %s del asunto, %s computada"
              % (a[0][:8], a[3], b[0][:8], b[3],
                 b[1] if b[1] is not None else "(sin)", vuelta_computada_de(b[0])))
    print("")

    print("E) LA VUELTA DE UN COMMIT CUYO ASUNTO NO LA NOMBRA, COMPUTADA DE LAS ACTAS")
    print("   REGLA, del invariante de la casa y no de una corazonada: los commits")
    print("   posteriores al del ACTA DE LA VUELTA N pertenecen a la vuelta N mas 1.")
    vuelta_computada = vuelta_computada_de(h)
    if vuelta_computada is None:
        print("   no hay acta anterior a %s en la rama, o el commit no esta en el log:"
              " su vuelta NO se computa y se dice." % h[:8])
    else:
        print("   %s pertenece a la VUELTA %d" % (h[:8], vuelta_computada))
    print("   CONTRASTE, y es contraste y no fuente: el acta 169 dice que la")
    print("   decimotercera entro en 33fe1380, que es la vuelta 166.")
    print("   yo computo: %s, %s"
          % (vuelta_computada, "CALZA" if vuelta_computada == 166 else "NO CALZA"))
    print("")

    print("F) LA TABLA PARA PEGAR EN LA CORRECCION")
    primera = tabla[0]
    print("   %s (vuelta %s, %s): %d tachadas, la primera de la serie"
          % (primera[0][:8],
             primera[1] if primera[1] is not None else "(sin)",
             primera[2], primera[3]))
    if anteriores:
        ha, va, fa, ca = anteriores[-1][:4]
        print("   %s (vuelta %s, %s): %d tachadas" % (ha[:8], va, fa, ca))
    print("   %s (vuelta %s, %s): %d tachadas, LA DECIMOTERCERA ENTRA AQUI"
          % (h[:8], vuelta_computada, fecha, cuantas))
    print("   %s (vuelta %s, %s): %d tachadas, ultimo commit que toca el fichero"
          % (tabla[-1][0][:8], vuelta_computada_de(tabla[-1][0]),
             tabla[-1][2], tabla[-1][3]))
    print("   el fichero de HOY en el arbol de trabajo: %d tachadas" % tachadas_de_hoy())
    print("")

    print("G) EL CONTRASTE CON EL ACTA, Y ES CONTRASTE Y NO FUENTE")
    print("   el acta 169 dice: 12 tachadas en 3ffc2091, 13 en 33fe1380,")
    print("   y 13 desde entonces hasta HEAD.")
    dic = dict((f[0][:8], f[3]) for f in tabla)
    for corto, esperado_del_acta in (("3ffc2091", 12), ("33fe1380", 13)):
        medido = dic.get(corto)
        print("   %s -> el acta dice %d, yo mido %s, %s"
              % (corto, esperado_del_acta,
                 medido if medido is not None else "(no esta en la serie)",
                 "CALZA" if medido == esperado_del_acta else "NO CALZA"))
    print("   el ultimo de la serie -> el acta dice 13, yo mido %d, %s"
          % (tabla[-1][3], "CALZA" if tabla[-1][3] == 13 else "NO CALZA"))
    print("")
    print("VERDE: la tabla queda medida. La cifra que se publique sale de aqui.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
