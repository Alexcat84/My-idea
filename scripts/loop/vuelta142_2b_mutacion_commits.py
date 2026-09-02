# -*- coding: utf-8 -*-
r"""vuelta142_2b_mutacion_commits.py . LA PRUEBA DE MUTACION DE LA TAREA 2.b de
la vuelta 142 (acta de la vuelta 141: caida 4.2 de la casa y 4.6 de encargo del
auditor, el `--comparar-commits` anclado al HEAD VIVO).

TRES CASOS, TODOS CORRIENDO EL TALLADOR DE VERDAD COMO SUBPROCESO (se prueba su
EXIT y sus lineas, no una copia de su regla), y ninguno sobre un literal:

  (a) CASO POSITIVO SOBRE SUJETO CONGELADO. `--vuelta 141 --comparar-commits`
      contra el reporte de la vuelta 141 tal como esta en su commit de reporte
      (`9835e37e`, sacado de git a un fichero de trabajo, no del arbol vivo):
      con el ancla nueva tiene que salir **VERDE EXIT 0**. Con el ancla vieja
      (HEAD vivo) salia ROJO, y este mismo script LO REPRODUCE sacando la
      version vieja del tallador de git y corriendola sobre el mismo sujeto:
      el contraste no se afirma, se mide.
  (b) CONTRAPRUEBA NEGATIVA. Sobre una COPIA del mismo reporte se mete un
      commit INVENTADO dentro del bloque delimitado. Tiene que salir ROJO
      NOMBRANDOLO. El hash inventado se COMPUTA a partir del primero real
      (se le cambia el ultimo digito hexadecimal por otro), no se teclea.
  (c) EL SELLO QUE NO CUADRA. Sobre una copia del sello de cierre se escribe
      OTRO hash real de la rama, y el tallador tiene que salir ROJO diciendo
      que el padre del commit que lo lleva no es el sellado. Es la guarda
      nueva que ata el hash escrito al commit que lo carga.

P.16, QUIEN FABRICA LIMPIA: todo lo fabricado (copias de reporte, copia del
sello, tallador viejo) se borra en el `finally`, y el sello REAL se restaura
byte a byte desde git.

USO:
  python scripts/loop/vuelta142_2b_mutacion_commits.py
"""
import io
import os
import re
import shutil
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
LOOP = os.path.join(RAIZ, "docs", "loop")

VUELTA = 141
COMMIT_DEL_REPORTE = "9835e37e"          # el commit que escribe el reporte de la 141
# El acta de la vuelta 141: el ultimo commit ANTES de que la vuelta 142 tocara el
# tallador. Se ancla a un commit FIJO y no a `HEAD` a proposito: el contraste
# tiene que seguir dando lo mismo cuando esta reparacion ya este commiteada, que
# es justamente lo que le faltaba al `--comparar-commits` que aqui se repara.
COMMIT_ANTES_DE_LA_REPARACION = "fd020d71"
TALLADOR = os.path.join(AQUI, "tallar_cabecera_reporte.py")
REL_TALLADOR = "scripts/loop/tallar_cabecera_reporte.py"
REL_REPORTE = "docs/loop/REPORTE.md"
REL_SELLO = "docs/loop/SALIDA_V%d_HEAD_CIERRE.txt" % VUELTA

SUJETO = os.path.join(LOOP, "_prueba_v142_2b_reporte141.md")
SUJETO_MUTADO = os.path.join(LOOP, "_prueba_v142_2b_reporte141_mutado.md")
TALLADOR_VIEJO = os.path.join(AQUI, "_prueba_v142_2b_tallador_viejo.py")
SELLO = os.path.join(RAIZ, REL_SELLO)

MARCA_ABRE = "<!-- COMMITS TALLADOS -->"
MARCA_CIERRA = "<!-- FIN COMMITS TALLADOS -->"
RE_LINEA_COMMIT = re.compile(r"^(\s*)([0-9a-f]{7,40})(\s+)(\S.*?)(\s*)$")


def de_git(ref, rel):
    r = subprocess.run(["git", "show", "%s:%s" % (ref, rel)], cwd=RAIZ, capture_output=True)
    if r.returncode != 0:
        raise SystemExit("ROJO (arnes): no se pudo sacar %s de %s" % (rel, ref))
    return r.stdout.decode("utf-8")


def escribir(ruta, texto):
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


def correr_tallador(script, ruta_reporte):
    r = subprocess.run([sys.executable, script, "--vuelta", str(VUELTA),
                        "--comparar-commits", ruta_reporte],
                       cwd=RAIZ, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def contar_problemas(salida):
    """COMPUTADO de la salida del tallador, no tecleado."""
    m = re.search(r"ROJO, (\d+) cosa\(s\) no cuadran en el bloque de commits", salida)
    return int(m.group(1)) if m else 0


def primer_hash_del_bloque(texto):
    lineas = texto.splitlines()
    dentro = False
    for l in lineas:
        if MARCA_ABRE in l:
            dentro = True
            continue
        if MARCA_CIERRA in l:
            break
        if dentro:
            m = RE_LINEA_COMMIT.match(l)
            if m:
                return m.group(2)
    raise SystemExit("ROJO (arnes): el sujeto no trae ninguna linea de commit en su bloque")


def inventar_hash(real):
    """COMPUTADO del real: se le cambia el ULTIMO digito por otro distinto, para
    que sea un hash con la misma forma y que git no conozca."""
    ultimo = real[-1]
    otro = "0" if ultimo != "0" else "1"
    return real[:-1] + otro


def mutar_bloque(texto, real, inventado):
    """Sustituye SOLO la primera linea de commit del bloque delimitado."""
    lineas = texto.splitlines()
    dentro = False
    for i, l in enumerate(lineas):
        if MARCA_ABRE in l:
            dentro = True
            continue
        if MARCA_CIERRA in l:
            break
        if dentro:
            m = RE_LINEA_COMMIT.match(l)
            if m and m.group(2) == real:
                lineas[i] = "%s%s%s%s%s" % (m.group(1), inventado, m.group(3),
                                            m.group(4), m.group(5))
                return "\n".join(lineas) + "\n", True
    return texto, False


def otro_commit_real_de_la_rama(distinto_de):
    r = subprocess.run(["git", "log", "-20", "--pretty=format:%H"], cwd=RAIZ,
                       capture_output=True, text=True, check=True)
    for h in r.stdout.splitlines():
        if h.strip() and h.strip() != distinto_de:
            return h.strip()
    raise SystemExit("ROJO (arnes): no hay otro commit en la rama para el caso (c)")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    resultados = []
    sello_original = None
    try:
        texto_reporte = de_git(COMMIT_DEL_REPORTE, REL_REPORTE)
        escribir(SUJETO, texto_reporte)
        sello_original = io.open(SELLO, encoding="utf-8").read()
        sellado = sello_original.strip()

        print("=" * 78)
        print("MUTACIONES DE LA TAREA 2.b | vuelta 142")
        print("Sujeto CONGELADO: %s:%s (no el arbol vivo)" % (COMMIT_DEL_REPORTE, REL_REPORTE))
        print("Sello de cierre de la vuelta %d: %s" % (VUELTA, sellado[:8]))
        print("El tallador se corre COMO SUBPROCESO: se prueba su EXIT y sus lineas.")
        print("=" * 78)

        # ---- CONTRASTE MEDIDO: EL TALLADOR VIEJO, SACADO DE GIT -------------
        # No se afirma "antes salia ROJO con 13": se saca la version anterior de
        # git y se corre sobre el MISMO sujeto.
        viejo = de_git(COMMIT_ANTES_DE_LA_REPARACION, REL_TALLADOR)
        escribir(TALLADOR_VIEJO, viejo)
        exit_v, salida_v = correr_tallador(TALLADOR_VIEJO, SUJETO)
        problemas_v = contar_problemas(salida_v)
        print("")
        print("CONTRASTE, el tallador de HEAD (el anclado al HEAD VIVO, antes de esta")
        print("reparacion) sobre el mismo sujeto -> EXIT %d, problemas %d"
              % (exit_v, problemas_v))

        # ---------------- (a) CASO POSITIVO ---------------------------------
        exit_a, salida_a = correr_tallador(TALLADOR, SUJETO)
        ok = (exit_a == 0) and ("BLOQUE DE COMMITS: IDENTICO A GIT" in salida_a)
        resultados.append(("a CASO POSITIVO sobre sujeto congelado: EXIT 0, bloque IDENTICO "
                           "A GIT con el ancla sellada", ok))
        print("")
        print("(a) tallador reparado -> EXIT %d, problemas %d"
              % (exit_a, contar_problemas(salida_a)))
        for l in salida_a.splitlines():
            if l.strip().startswith(("rango cotejado", "commit que LLEVA", "HEAD sellado",
                                     "commits en el bloque", "BLOQUE DE COMMITS")):
                print("      %s" % l.strip())

        # ---------------- (b) CONTRAPRUEBA NEGATIVA -------------------------
        real = primer_hash_del_bloque(texto_reporte)
        inventado = inventar_hash(real)
        mutado, hubo = mutar_bloque(texto_reporte, real, inventado)
        if not hubo:
            raise SystemExit("ROJO (arnes): no se pudo mutar el bloque; sin sujeto no hay caso")
        escribir(SUJETO_MUTADO, mutado)
        exit_b, salida_b = correr_tallador(TALLADOR, SUJETO_MUTADO)
        nombrado = inventado[:8] in salida_b or inventado in salida_b
        ok = (exit_b == 1) and nombrado
        resultados.append(("b COMMIT INVENTADO dentro del bloque: EXIT 1 y ROJO NOMBRANDOLO", ok))
        print("")
        print("(b) hash real %s -> inventado %s (COMPUTADO, ultimo digito cambiado)"
              % (real, inventado))
        print("    -> EXIT %d, problemas %d, nombrado en la salida: %s"
              % (exit_b, contar_problemas(salida_b), nombrado))
        for l in salida_b.splitlines():
            if inventado[:8] in l:
                print("      %s" % l.strip())

        # ---------------- (c) EL SELLO QUE NO CUADRA ------------------------
        impostor = otro_commit_real_de_la_rama(sellado)
        escribir(SELLO, impostor + "\n")
        exit_c, salida_c = correr_tallador(TALLADOR, SUJETO)
        dice_padre = "el sello no se escribio donde dice" in salida_c
        ok = (exit_c == 1) and dice_padre
        resultados.append(("c SELLO CAMBIADO por otro commit real: EXIT 1 diciendo que el "
                           "padre del portador no es el sellado", ok))
        print("")
        print("(c) sello cambiado a %s -> EXIT %d, dice lo del padre: %s"
              % (impostor[:8], exit_c, dice_padre))
        for l in salida_c.splitlines():
            if "ROJO:" in l:
                print("      %s" % l.strip())
    finally:
        # P.16: quien fabrica, limpia; y el sello REAL se restaura de git.
        if sello_original is not None:
            escribir(SELLO, sello_original)
            subprocess.run(["git", "checkout", "--", REL_SELLO], cwd=RAIZ,
                           capture_output=True)
        for p in (SUJETO, SUJETO_MUTADO, TALLADOR_VIEJO):
            if os.path.exists(p):
                os.remove(p)

    print("")
    print("=" * 78)
    verdes = 0
    for nombre, ok in resultados:
        print("  %-5s %s" % ("VERDE" if ok else "ROJO", nombre))
        verdes += 1 if ok else 0
    print("CIFRA de la bateria 2.b: %d comprobaciones" % len(resultados))
    print("CIFRA verdes de la bateria 2.b: %d comprobaciones" % verdes)
    print("=" * 78)
    if verdes != len(resultados):
        print("ROJO: %d de %d casos no se comportan." % (len(resultados) - verdes, len(resultados)))
        return 1
    print("VERDE: los %d casos se comportan." % len(resultados))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
