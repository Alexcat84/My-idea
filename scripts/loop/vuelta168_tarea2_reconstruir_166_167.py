# -*- coding: utf-8 -*-
r"""vuelta168_tarea2_reconstruir_166_167.py . TAREA 2 de la vuelta 168.

RECONSTRUYE LO QUE LAS VUELTAS 166 Y 167 ENTREGARON, DE LOS COMMITS Y DE LAS
ACTAS, Y DECLARA COMO NO RECONSTRUIBLE LO QUE NO SE PUEDA SACAR DE AHI.

POR QUE NACE. `docs/loop/REPORTE.md` seguia siendo el de la vuelta 165: las
vueltas 166 y 167 terminaron sin escribir el suyo, dos seguidas, y el acta 167
lo midio en su hallazgo 4.2. Esta es la deuda de dos vueltas, y el encargo de la
168 la manda pagar con una condicion que es la que hace honesto el ejercicio:
**lo que no se pueda reconstruir SE DECLARA COMO NO RECONSTRUIBLE en vez de
rellenarse.**

DE DONDE SALE CADA COSA, Y NO SE MEZCLAN LAS DOS FUENTES:
  - EL CORREDOR de cada vuelta (que commits la componen, que rutas toca cada
    uno, cuantas lineas mueve) sale de `git log` y `git show --numstat`, leidos
    en esta vuelta. Es dato duro.
  - EL VEREDICTO DEL AUDITOR sobre cada vuelta sale del acta de esa vuelta,
    citada por su linea. Es dato duro tambien, pero de otra sede, y va marcado
    como tal.
  - LO QUE UN REPORTE HABRIA TRAIDO Y NINGUNA DE LAS DOS SEDES CONTIENE (los
    DISCUTIBLES MARCADOS, las PREGUNTAS y los PENDIENTES DE DOCTRINA del
    ejecutor) NO SE INVENTA. Se declara NO RECONSTRUIBLE con su motivo, porque
    un discutible marcado despues de conocer el veredicto del auditor ya no es
    un discutible: es una copia.

LAS FRONTERAS DE CADA VUELTA SE LEEN DE GIT Y NO SE TECLEAN: la vuelta N va del
commit del acta N-1 (exclusive) al commit del acta N (inclusive). Los tres
commits de acta se localizan por el patron "ACTA DE LA VUELTA <n> DEL AUDITOR",
el mismo que ya usan `tallar_cabecera_reporte.py` y
`verificar_apertura_sellada.py`. Si alguno falta o esta duplicado, PARA.

USO:
  python scripts/loop/vuelta168_tarea2_reconstruir_166_167.py
  python scripts/loop/vuelta168_tarea2_reconstruir_166_167.py --mutar
"""
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ACTA = os.path.join(RAIZ, "docs", "loop", "ACTA_AUDITOR.md")

# LO QUE UN REPORTE TRAE Y NINGUNA OTRA SEDE GUARDA. Se declara, no se rellena.
NO_RECONSTRUIBLE = [
    ("LOS DISCUTIBLES MARCADOS del ejecutor de cada vuelta",
     "Un discutible se marca ANTES de saber si se acierta (`EJECUTOR.md` 7). Hoy "
     "el acta 167 ya publico su veredicto sobre las dos vueltas, asi que "
     "cualquier lista que se escribiera ahora seria una copia con la respuesta "
     "delante, no un discutible. El acta 167 lo dice de su lado con estas "
     "palabras: NO HAY DISCUTIBLES MARCADOS, PORQUE NO HAY REPORTE."),
    ("LAS PREGUNTAS del ejecutor de cada vuelta",
     "Una pregunta es lo que el ejecutor no pudo medir EN SU VUELTA. Ni los "
     "commits ni las actas guardan las que no llegaron a escribirse, y "
     "fabricarlas hoy seria inventar el estado mental de una sesion cerrada."),
    ("LOS PENDIENTES DE DOCTRINA que las vueltas 166 y 167 hubieran levantado",
     "Solo se conocen los que llegaron a un commit o a un acta. Si alguna de las "
     "dos vueltas levanto uno y no lo escribio, hoy no hay sede de la que "
     "leerlo, y suponerlo seria adivinar."),
    ("EL VEREDICTO DE UNA LINEA del ejecutor de cada vuelta",
     "Es la lectura que el ejecutor hace de su propia vuelta antes de que el "
     "auditor la juzgue. Escribirla hoy, con las dos actas ya publicadas, seria "
     "escribir el veredicto del auditor con otra letra."),
]


def git(args):
    r = subprocess.run(["git"] + args, cwd=RAIZ, capture_output=True)
    return r.returncode, r.stdout.decode("utf-8", errors="replace")


def commit_del_acta(n):
    """EL COMMIT DEL ACTA N, LEIDO DE GIT. Uno solo o PARA."""
    patron = "ACTA DE LA VUELTA %d DEL AUDITOR" % n
    c, log = git(["log", "--format=%H%x09%s", "-400"])
    if c != 0:
        return None, "PARADA: git log fallo."
    hits = [l for l in log.splitlines() if l.split("\t", 1)[-1].startswith(patron)]
    if len(hits) != 1:
        return None, ("PARADA: commits que empiezan por %r: %d (hace falta 1)."
                      % (patron, len(hits)))
    h, asunto = hits[0].split("\t", 1)
    return (h, asunto), None


def corredor(desde, hasta):
    """Los commits de `desde` (exclusive) a `hasta` (inclusive), del mas viejo
    al mas nuevo, cada uno con su asunto, sus rutas y sus lineas movidas."""
    c, log = git(["log", "--reverse", "--format=%H%x09%s", "%s..%s" % (desde, hasta)])
    if c != 0:
        return None, "PARADA: no se pudo leer el corredor %s..%s" % (desde[:8], hasta[:8])
    fuera = []
    for linea in log.splitlines():
        if not linea.strip():
            continue
        h, asunto = linea.split("\t", 1)
        c2, num = git(["show", h, "--numstat", "--format="])
        rutas, mas, menos = [], 0, 0
        for fila in num.splitlines():
            partes = fila.split("\t")
            if len(partes) != 3:
                continue
            a, b, ruta = partes
            rutas.append(ruta)
            if a.isdigit():
                mas += int(a)
            if b.isdigit():
                menos += int(b)
        fuera.append({"hash": h, "asunto": asunto, "rutas": rutas,
                      "mas": mas, "menos": menos})
    return fuera, None


def tareas_del_corredor(commits):
    """LAS TAREAS ENTREGADAS, CONTADAS DE LOS ASUNTOS Y NO TECLEADAS. Un commit
    de tarea abre su asunto con 'TAREA <n>:'. Los bloques de apertura y cierre
    no lo hacen y por eso no cuentan como tarea."""
    tareas = []
    for c in commits:
        m = re.match(r"^TAREA (\d+)([a-z]?):", c["asunto"])
        if m:
            tareas.append((m.group(1) + m.group(2), c))
    return tareas


def cuerpo_del_acta(n):
    """El cuerpo del acta N, acotado por su cabecera y la siguiente."""
    texto = io.open(ACTA, encoding="utf-8").read()
    lineas = texto.split("\n")
    cab = "# ACTA DEL AUDITOR, VUELTA %d" % n
    inicios = [i for i, l in enumerate(lineas, 1) if l.startswith(cab)]
    if len(inicios) != 1:
        return None, "PARADA: la cabecera del acta %d aparece %d veces." % (n, len(inicios))
    inicio = inicios[0]
    sig = [i for i, l in enumerate(lineas, 1)
           if i > inicio and re.match(r"^# ACTA (DE LA VUELTA|DEL AUDITOR)", l)]
    fin = min(sig) - 1 if sig else len(lineas)
    return (lineas, inicio, fin), None


def veredicto_del_acta(lineas, inicio, fin):
    """EL VEREDICTO DE UNA LINEA del auditor, leido de su acta y con su numero
    de linea. Es la unica frase de esa acta que este instrumento cita."""
    for i in range(inicio, fin + 1):
        if "EL VEREDICTO DE UNA LINEA" in lineas[i - 1]:
            acumulado, j, cierre = "", i - 1, -1
            while j < fin:
                trozo = lineas[j].strip()
                if not trozo and acumulado:
                    break
                acumulado = (acumulado + " " + trozo).strip() if acumulado else trozo
                cierre = acumulado.find("**", 2)
                if cierre >= 0:
                    break
                j += 1
            if cierre < 0:
                return None, "PARADA: el veredicto del acta no cierra su negrita."
            return (i, re.sub(r"\s+", " ", acumulado[2:cierre]).strip()), None
    return None, "PARADA: el acta no trae 'EL VEREDICTO DE UNA LINEA'."


def reconstruir(n):
    """La vuelta N entera, reconstruida. Devuelve (dict, error)."""
    par_ant, err = commit_del_acta(n - 1)
    if err:
        return None, err
    par, err = commit_del_acta(n)
    if err:
        return None, err
    commits, err = corredor(par_ant[0], par[0])
    if err:
        return None, err
    tri, err = cuerpo_del_acta(n)
    if err:
        return None, err
    lineas, ini, fin = tri
    ver, err = veredicto_del_acta(lineas, ini, fin)
    if err:
        return None, err
    tareas = tareas_del_corredor(commits)
    rutas = set()
    for c in commits:
        rutas.update(c["rutas"])
    return {
        "vuelta": n,
        "acta_anterior": par_ant,
        "acta": par,
        "commits": commits,
        "tareas": tareas,
        "rutas": sorted(rutas),
        "mas": sum(c["mas"] for c in commits),
        "menos": sum(c["menos"] for c in commits),
        "acta_lineas": (ini, fin),
        "veredicto": ver,
    }, None


def main():
    print("=" * 78)
    print("VUELTA 168, TAREA 2: LAS VUELTAS 166 Y 167, RECONSTRUIDAS DE COMMITS Y ACTAS")
    print("=" * 78)
    print("")
    for n in (166, 167):
        r, err = reconstruir(n)
        if err:
            print(err)
            return 1
        print("=" * 78)
        print("VUELTA %d" % n)
        print("=" * 78)
        print("A) LAS FRONTERAS, LEIDAS DE GIT Y NO TECLEADAS")
        print("   abre tras el acta %d: %s  %s"
              % (n - 1, r["acta_anterior"][0][:8], r["acta_anterior"][1][:60]))
        print("   cierra en el acta %d:  %s  %s"
              % (n, r["acta"][0][:8], r["acta"][1][:60]))
        print("   CIFRA commits del corredor (acta anterior exclusive, acta inclusive): %d"
              % len(r["commits"]))
        print("")
        print("B) LOS COMMITS, UNO POR UNO, DEL MAS VIEJO AL MAS NUEVO")
        for c in r["commits"]:
            print("   %s  +%-6d -%-6d  %d ruta(s)  %s"
                  % (c["hash"][:8], c["mas"], c["menos"], len(c["rutas"]), c["asunto"][:78]))
        print("")
        print("C) LAS TAREAS ENTREGADAS, CONTADAS DE LOS ASUNTOS Y NO TECLEADAS")
        for clave, c in r["tareas"]:
            print("   TAREA %-3s %s  %s" % (clave, c["hash"][:8], c["asunto"][:70]))
        print("   CIFRA tareas con commit propio: %d" % len(r["tareas"]))
        print("")
        print("D) EL VOLUMEN Y LAS RUTAS")
        print("   CIFRA lineas anadidas en la vuelta: %d" % r["mas"])
        print("   CIFRA lineas quitadas en la vuelta: %d" % r["menos"])
        print("   CIFRA rutas distintas tocadas: %d" % len(r["rutas"]))
        print("   CIFRA rutas bajo dataset/: %d"
              % len([x for x in r["rutas"] if x.startswith("dataset/")]))
        print("   CIFRA rutas bajo web/: %d"
              % len([x for x in r["rutas"] if x.startswith("web/")]))
        print("   CIFRA rutas bajo docs/plan/: %d"
              % len([x for x in r["rutas"] if x.startswith("docs/plan/")]))
        print("")
        print("E) EL VEREDICTO DEL AUDITOR, LEIDO DE SU ACTA Y MARCADO COMO SUYO")
        print("   acta %d: docs/loop/ACTA_AUDITOR.md, lineas %d a %d"
              % (n, r["acta_lineas"][0], r["acta_lineas"][1]))
        print("   docs/loop/ACTA_AUDITOR.md:%d" % r["veredicto"][0])
        print("   \"%s\"" % r["veredicto"][1])
        print("")
        print("F) EL REPORTE DE ESA VUELTA, MEDIDO Y NO SUPUESTO")
        c, rep = git(["show", "%s:docs/loop/REPORTE.md" % r["acta"][0]])
        if c == 0 and rep.strip():
            primera = rep.splitlines()[0].strip()
            mm = re.search(r"REPORTE DE LA VUELTA (\d+)", primera)
            dice = int(mm.group(1)) if mm else -1
            print("   primera linea de docs/loop/REPORTE.md en el arbol del acta %d:" % n)
            print("      %s" % primera)
            print("   ESA VUELTA ESCRIBIO SU REPORTE: %s"
                  % ("SI" if dice == n else "NO (el fichero era el de la vuelta %d)" % dice))
        else:
            print("   NO EXISTE docs/loop/REPORTE.md en ese arbol.")
        print("")

    print("=" * 78)
    print("G) LO QUE NO SE PUEDE RECONSTRUIR, DECLARADO EN VEZ DE RELLENADO")
    print("=" * 78)
    for que, porque in NO_RECONSTRUIBLE:
        print("   NO RECONSTRUIBLE: %s" % que)
        print("      motivo: %s" % porque)
    print("   CIFRA cosas declaradas NO RECONSTRUIBLES: %d" % len(NO_RECONSTRUIBLE))
    print("")
    print("VERDE: las dos vueltas quedan reconstruidas de sus dos sedes.")
    return 0


# ---------------------------------------------------------------------------
# CASO POSITIVO POR MUTACION (EJECUTOR.md 1). Los sujetos son corredores
# FABRICADOS EN MEMORIA mas los corredores REALES leidos de git. Cero
# escrituras.
# ---------------------------------------------------------------------------

def prueba_de_mutacion():
    print("=" * 78)
    print("VUELTA 168, TAREA 2: CASO POSITIVO POR MUTACION DEL RECONSTRUCTOR")
    print("=" * 78)
    print("")
    casos = []

    print("A) EL CONTEO DE TAREAS SIGUE A LOS ASUNTOS Y NO A UNA CONSTANTE")
    fabricados = [
        ("seis tareas mas apertura y cierre",
         ["Bloque de apertura"] + ["TAREA %d: algo" % k for k in range(1, 7)]
         + ["Bloque de cierre"], 6),
        ("ninguna tarea, solo apertura",
         ["Bloque de apertura de la vuelta X"], 0),
        ("tres tareas y una con letra",
         ["TAREA 1: a", "TAREA 2: b", "TAREA 3b: c"], 3),
        ("un asunto que NOMBRA una tarea pero no la abre",
         ["ACTA: la TAREA 5 quedo en parada", "TAREA 1: a"], 1),
    ]
    for rotulo, asuntos, esperado in fabricados:
        cs = [{"hash": "0" * 40, "asunto": a, "rutas": [], "mas": 0, "menos": 0}
              for a in asuntos]
        visto = len(tareas_del_corredor(cs))
        print("   %-52s -> %d tarea(s)" % (rotulo[:52], visto))
        casos.append(("A_%s" % rotulo.replace(" ", "_")[:40], visto, esperado))
    print("")

    print("B) LOS CORREDORES REALES, LEIDOS DE GIT HOY")
    r166, err = reconstruir(166)
    if err:
        print("   " + err)
        return 1
    r167, err = reconstruir(167)
    if err:
        print("   " + err)
        return 1
    print("   vuelta 166: %d commits, %d tareas con commit propio"
          % (len(r166["commits"]), len(r166["tareas"])))
    print("   vuelta 167: %d commits, %d tareas con commit propio"
          % (len(r167["commits"]), len(r167["tareas"])))
    # LAS DOS CIFRAS DE COMMITS ESTUVIERON TECLEADAS MAL EN LA PRIMERA CORRIDA DE
    # ESTE ARNES, Y SE DECLARA EN VEZ DE TAPARSE: puse 8 y 5, que son los commits
    # DEL EJECUTOR, y el corredor que este instrumento mide va hasta el acta
    # INCLUSIVE, asi que son 9 y 6. El arnes las cazo antes de que llegaran a
    # ninguna salida sellada. La leccion es la de la casa: la cifra se cuenta del
    # instrumento, no se recuerda de un `git log --oneline -8` truncado.
    casos.append(("B_la_166_tiene_9_commits_acta_incluida", len(r166["commits"]), 9))
    casos.append(("B_y_8_de_ellos_son_del_ejecutor", len(r166["commits"]) - 1, 8))
    casos.append(("B_la_166_entrego_6_tareas", len(r166["tareas"]), 6))
    casos.append(("B_la_167_tiene_6_commits_acta_incluida", len(r167["commits"]), 6))
    casos.append(("B_y_5_de_ellos_son_del_ejecutor", len(r167["commits"]) - 1, 5))
    casos.append(("B_la_167_entrego_4_tareas", len(r167["tareas"]), 4))
    casos.append(("B_la_166_entrego_MAS_tareas_que_la_167",
                  len(r166["tareas"]) > len(r167["tareas"]), True))
    print("")

    print("C) LAS DOS VUELTAS TIENEN CORREDORES DISTINTOS Y NO SE CONFUNDEN")
    casos.append(("C_el_acta_que_cierra_la_166_abre_la_167",
                  r166["acta"][0] == r167["acta_anterior"][0], True))
    casos.append(("C_los_corredores_no_comparten_ningun_commit",
                  len(set(c["hash"] for c in r166["commits"]) &
                      set(c["hash"] for c in r167["commits"])), 0))
    print("   el acta que cierra la 166 (%s) es la que abre la 167: %s"
          % (r166["acta"][0][:8], r166["acta"][0] == r167["acta_anterior"][0]))
    print("")

    print("D) NINGUNA DE LAS DOS ESCRIBIO SU REPORTE, Y SE MIDE EN VEZ DE CREERSE")
    for r, n in ((r166, 166), (r167, 167)):
        c, rep = git(["show", "%s:docs/loop/REPORTE.md" % r["acta"][0]])
        mm = re.search(r"REPORTE DE LA VUELTA (\d+)", rep.splitlines()[0] if rep else "")
        dice = int(mm.group(1)) if mm else -1
        print("   arbol del acta %d: el REPORTE.md dice ser el de la vuelta %d" % (n, dice))
        casos.append(("D_el_reporte_del_arbol_del_acta_%d_es_el_de_la_165" % n, dice, 165))
    print("")

    print("E) LA LISTA DE NO RECONSTRUIBLES NO ESTA VACIA Y CADA UNA TRAE MOTIVO")
    casos.append(("E_hay_no_reconstruibles_declarados", len(NO_RECONSTRUIBLE), 4))
    casos.append(("E_todos_traen_motivo",
                  len([1 for _q, p in NO_RECONSTRUIBLE if len(p) > 40]), 4))
    print("   CIFRA no reconstruibles: %d, todos con motivo escrito" % len(NO_RECONSTRUIBLE))
    print("")

    print("F) PASADA 1, LOS CASOS TAL CUAL")
    fallos = 0
    for nombre, real, esperado in casos:
        ok = (real == esperado)
        print("   %-56s %s   (real=%r esperado=%r)"
              % (nombre[:56], "PASA" if ok else "FALLA", real, esperado))
        if not ok:
            fallos += 1
    print("   CIFRA casos: %d | pasan: %d | fallan: %d"
          % (len(casos), len(casos) - fallos, fallos))
    print("")

    print("G) PASADA 2, SE MUTA EL VALOR ESPERADO Y CADA CASO TIENE QUE CAER")
    caen = 0
    for nombre, real, esperado in casos:
        mutado = (not esperado) if isinstance(esperado, bool) else (
            esperado + 1 if isinstance(esperado, int) else str(esperado) + "_mutado")
        cae = (real != mutado)
        print("   %-56s %s   (esperado mutado=%r)"
              % (nombre[:56], "CAE" if cae else "NO CAE", mutado))
        if cae:
            caen += 1
    print("   CIFRA casos que caen al mutar el esperado: %d de %d" % (caen, len(casos)))
    print("")

    if fallos == 0 and caen == len(casos):
        print("VERDE: los %d casos pasan tal cual y los %d caen al mutar el esperado."
              % (len(casos), len(casos)))
        return 0
    print("ROJO: fallos=%d, casos que no caen=%d" % (fallos, len(casos) - caen))
    return 1


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    if "--mutar" in sys.argv:
        sys.exit(prueba_de_mutacion())
    sys.exit(main())
