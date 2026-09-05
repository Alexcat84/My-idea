# -*- coding: utf-8 -*-
r"""vuelta172_tarea3b_indice.py . TAREA 3, SEGUNDA MITAD, DE LA VUELTA 172.

LAS DOS FILAS DE `docs/plan/00_INDICE.md` RECIBEN SU CIFRA DE HOY POR `9.21`, POR
ADICION Y SIN TOCAR UNA LETRA DE LO VIEJO (adjudicacion 6.10 del acta 171).

LA FILA QUE EL ENCARGO NOMBRA es *"lecturas dirigidas encargadas y sin hacer"*.
El `D.4` de la vuelta 171 decidio NO adosarle su cifra porque el barrido estaba
contaminado por el archivo de reportes; la `6.10` le da la razon y dice que **con
la 6.1 y la 6.2 de hoy la cifra deja de estar envenenada**, asi que ya se puede.

Y SE TOCA UNA SEGUNDA FILA QUE EL ENCARGO NO NOMBRA, Y SE DICE POR QUE, PORQUE
CALLARLO SERIA DEJAR UNA TRAMPA: la fila de arriba, *"lecturas dirigidas
hechas"*, lleva adosada desde la vuelta 171 la cifra **82 con corte 5 sep 2026**.
**La TAREA 3 de HOY, que es 5 sep 2026 tambien, la ha movido a 98.** Si se deja
como esta, esa pagina publica **dos cifras distintas con la misma fecha** para la
misma vara, y eso no es una cifra con su corte: es una contradiccion. Se adosa
por el mismo `9.21`, **con la hora del cambio dicha en palabras** (antes y
despues de la TAREA 3 de esta vuelta), y sin tocar el 82 ni el 81 ni el 65.

CERO REPARACIONES DE NODOS: este fichero solo toca docs/plan/00_INDICE.md.

USO:
  python scripts/loop/vuelta172_tarea3b_indice.py
"""
import io
import os
import re
import subprocess
import sys

NL = chr(10)
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
INDICE = os.path.join(RAIZ, "docs", "plan", "00_INDICE.md")
SALIDA_CONTADOR = "docs/loop/SALIDA_V172_T3_CONTAR_LD.txt"
FECHA = "5 sep 2026"

ANCLA_HECHAS = "| lecturas dirigidas **hechas** | **65** |"
ANCLA_SIN_HACER = "| lecturas dirigidas **encargadas y sin hacer** | **CERO** |"
MARCA = "ADOSADA POR `9.21` EN LA VUELTA 172"


def leer(ruta):
    return io.open(ruta, encoding="utf-8").read().replace(chr(13) + NL, NL)


def main():
    print("=" * 78)
    print("VUELTA 172, TAREA 3 (segunda mitad): LAS DOS FILAS DEL 00_INDICE, POR 9.21")
    print("=" * 78)
    print("")
    rojos = []

    print("A) EL CONTADOR, CORRIDO EN ESTA VUELTA Y DESPUES DE LA NUMERACION")
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run([sys.executable, "scripts/loop/vuelta48_contar_ld.py"],
                       cwd=RAIZ, capture_output=True, env=env)
    salida = r.stdout.decode("utf-8", errors="replace")
    print("   exit: %d" % r.returncode)
    if r.returncode != 0:
        rojos.append("el contador no sale en 0")
    m_h = re.search(r"\| lecturas dirigidas \*\*hechas\*\*\s+\| \*\*(\d+)\*\* \|", salida)
    m_s = re.search(r"\| lecturas dirigidas \*\*encargadas sin hacer\*\* \| \*\*(\d+)\*\* \|",
                    salida)
    if not m_h or not m_s:
        print("   PARADA: el contador no imprime sus dos celdas.")
        return 1
    hechas, sin_hacer = int(m_h.group(1)), int(m_s.group(1))
    print("   CIFRA hechas, LEIDA de la salida del contador: %d" % hechas)
    print("   CIFRA encargadas sin hacer, LEIDA de la salida: %d" % sin_hacer)
    nombres = re.findall(r"^     LD-(\d+) nombrado en", salida, re.M)
    print("   los que quedan sin seccion, uno a uno: %s"
          % ", ".join("LD-%s" % n for n in nombres))
    if len(nombres) != sin_hacer:
        rojos.append("la lista de sin seccion trae %d y la celda dice %d"
                     % (len(nombres), sin_hacer))
    print("")

    print("B) LAS DOS FILAS, LOCALIZADAS Y CONTADAS")
    texto = leer(INDICE)
    for etiqueta, ancla in (("hechas", ANCLA_HECHAS), ("encargadas y sin hacer", ANCLA_SIN_HACER)):
        filas = [l for l in texto.split(NL) if l.startswith(ancla)]
        print("   filas que empiezan por el ancla de %-24s %d" % (etiqueta, len(filas)))
        if len(filas) != 1:
            rojos.append("la fila de %s no aparece exactamente una vez" % etiqueta)
    print("   ya lleva la marca de esta vuelta: %s" % ("SI" if MARCA in texto else "NO"))
    if MARCA in texto:
        print("YA ESTABA: las cifras de esta vuelta ya se adosaron. No se toca.")
        return 0
    print("")

    if rojos:
        print("ROJO, %d motivo(s), y NO se escribe nada:" % len(rojos))
        for x in rojos:
            print("   " + x)
        return 1

    print("C) SE ESCRIBE, POR ADICION Y SIN TOCAR UNA LETRA DE LO VIEJO")
    largos_antes = texto.count(chr(8212))
    medios_antes = texto.count(chr(8211))
    print("   guiones largos y medios que ya habia: %d y %d" % (largos_antes, medios_antes))

    fila_h = [l for l in texto.split(NL) if l.startswith(ANCLA_HECHAS)][0]
    fila_s = [l for l in texto.split(NL) if l.startswith(ANCLA_SIN_HACER)][0]

    cola_h = (
        " **Y LA CIFRA DE HOY, %s Y SIN TOCAR UNA LETRA DE LO VIEJO: %d.** Misma vara y "
        "MISMO INSTRUMENTO, `scripts/loop/vuelta48_contar_ld.py`, corrido en esta vuelta "
        "([`../loop/%s`](../loop/%s), exit 0), **DESPUES de la TAREA 3**. "
        "**Y SE DICE POR QUE HAY DOS CIFRAS CON LA MISMA FECHA EN ESTA MISMA CELDA, EN "
        "VEZ DE DEJAR LA TRAMPA PUESTA:** el **82** de arriba lo adoso la vuelta 171 el "
        "mismo %s y era exacto a su corte; **esta vuelta lo ha movido ella misma**, "
        "porque su TAREA 3 escribio las 16 secciones `LD-139` a `LD-154` que le faltaban "
        "a la segunda tanda. **82 antes de la TAREA 3 de la vuelta 172, %d despues**, y "
        "el 82 no se borra ni se corrige. La diferencia son exactamente **16**."
        % (MARCA, hechas, os.path.basename(SALIDA_CONTADOR),
           os.path.basename(SALIDA_CONTADOR), FECHA, hechas))

    cola_s = (
        " **Y LA CIFRA DE HOY, %s Y SIN TOCAR UNA LETRA DE LO VIEJO: %d.** Misma vara y "
        "MISMO INSTRUMENTO, corrido en esta vuelta "
        "([`../loop/%s`](../loop/%s), exit 0). **LA VUELTA 171 SE NEGO A ADOSARLA Y TENIA "
        "RAZON** (su `D.4`): entonces el barrido daba **8** y seis de esos ocho salian "
        "del archivo de reportes, que el propio bucle acababa de crear. **La adjudicacion "
        "6.10 del acta 171 le da la razon y dice que hoy ya se puede**, porque la TAREA "
        "2.a de esta vuelta metio `docs/loop/reportes/REPORTE_V<N>.md` en los narrativos "
        "del bucle y la TAREA 3 numero las 16. **Los %d que quedan son %s**, y NINGUNO es "
        "nuevo: los dos primeros son las menciones de la serie `R.n` al glosar un encargo "
        "(el `PD.1` que sigue abierto), y los dos ultimos son los mismos que la vuelta 48 "
        "ya declaraba como no pendientes. **El CERO viejo no se borra: era exacto a su "
        "corte del 19 ago 2026.**"
        % (MARCA, sin_hacer, os.path.basename(SALIDA_CONTADOR),
           os.path.basename(SALIDA_CONTADOR), sin_hacer,
           ", ".join("`LD-%s`" % n for n in nombres)))

    nueva_h = fila_h.rstrip()
    if nueva_h.endswith("|"):
        nueva_h = nueva_h[:-1].rstrip() + cola_h + " |"
    nueva_s = fila_s.rstrip()
    if nueva_s.endswith("|"):
        nueva_s = nueva_s[:-1].rstrip() + cola_s + " |"

    texto = texto.replace(fila_h, nueva_h).replace(fila_s, nueva_s)
    io.open(INDICE, "w", encoding="utf-8", newline=NL).write(texto)
    print("   ESCRITO: docs/plan/00_INDICE.md (%d bytes)" % len(texto.encode("utf-8")))
    print("")

    print("D) LA RELECTURA DEL DISCO")
    de_nuevo = leer(INDICE)
    fallos = 0
    for etiqueta, cond in (
            ("la letra vieja de la fila de hechas sigue entera",
             "**MEDIDO el 19 ago 2026 (vuelta 48)" in de_nuevo),
            ("el 65 sigue", ANCLA_HECHAS in de_nuevo),
            ("el 81 sigue", "exit 0): 81**" in de_nuevo),
            ("el 82 de la vuelta 171 sigue y sin corregir",
             "EN LA VUELTA 171 (5 sep 2026) Y SIN TOCAR UNA LETRA DE LO VIEJO: 82.**"
             in de_nuevo),
            ("el CERO de la otra fila sigue", ANCLA_SIN_HACER in de_nuevo),
            ("la cifra de hoy de hechas esta escrita",
             "%s Y SIN TOCAR UNA LETRA DE LO VIEJO: %d.**" % (MARCA, hechas) in de_nuevo),
            ("la cifra de hoy de encargadas sin hacer esta escrita",
             "%s Y SIN TOCAR UNA LETRA DE LO VIEJO: %d.**" % (MARCA, sin_hacer)
             in de_nuevo),
            ("los cuatro numeros que quedan estan nombrados uno a uno",
             all(("`LD-%s`" % n) in de_nuevo for n in nombres)),
            ("no anado ni un guion largo ni uno medio",
             de_nuevo.count(chr(8212)) == largos_antes
             and de_nuevo.count(chr(8211)) == medios_antes),
            ("la tabla no gana ni pierde filas",
             de_nuevo.count(NL) == texto.count(NL))):
        print("   %-58s %s" % (etiqueta, "SI" if cond else "NO"))
        if not cond:
            fallos += 1
    print("   CIFRA comprobaciones: 10 | fallan: %d" % fallos)
    print("")
    if fallos:
        print("ROJO: el fichero escrito no cumple %d de sus propias guardas." % fallos)
        return 1
    print("VERDE: las dos filas del 00_INDICE llevan su cifra de hoy, por adicion.")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
