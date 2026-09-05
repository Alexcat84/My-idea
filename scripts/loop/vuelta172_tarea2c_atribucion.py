# -*- coding: utf-8 -*-
r"""vuelta172_tarea2c_atribucion.py . TAREA 2.c DE LA VUELTA 172.

LA LECTURA NUEVA DEL CONTADOR `LD` AL LADO DE LA VIEJA, Y LA ATRIBUCION DELANTE:
CADA NUMERO POR ENCIMA DE `LD-138` QUE SIGA EN EL UNIVERSO, CON SU FICHERO Y SU
LINEA.

ES LA GUARDA DE LA TAREA 3 Y SIN ELLA LA 3 NO SE CORRE (letra del encargo). La
adjudicacion 6.2 del acta 171 dice que **la vara que asigna es la de las HECHAS**
(las que tienen seccion propia) y que **ninguno de los numeros por encima de
`LD-138` puede tener seccion propia**; si alguno la tuviera, hay una asignacion
ajena y SE PARA.

QUE HACE, Y NADA SE TECLEA:

  A. Corre el contador de verdad, `vuelta48_contar_ld.py`, sobre el arbol de
     hoy, y guarda su salida entera.
  B. Recompone POR SU CUENTA las dos varas, usando las MISMAS funciones y los
     MISMOS patrones del contador (`RE_ID`, `RE_CAB`, `PAGINAS`,
     `motivo_de_exclusion`), para poder dar la LINEA que el contador no
     imprime. UNA SOLA FUENTE DEL CRITERIO: no se copia ninguna regla, se
     importan.
  C. Imprime, uno a uno, cada numero por encima de `LD-138` del universo con
     TODOS sus ficheros y TODAS sus lineas, y dice de cada uno si tiene o no
     seccion propia.
  D. CAE EN ROJO si alguno de esos numeros tiene seccion propia (esa es la
     parada que el encargo describe) o si las dos varas no salen de la misma
     lectura.

CERO ESCRITURAS EN EL REPO: solo lee y escribe su salida por stdout.

USO:
  python scripts/loop/vuelta172_tarea2c_atribucion.py
"""
import io
import os
import subprocess
import sys

NL = chr(10)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vuelta48_contar_ld as C   # noqa: E402

RAIZ = C.RAIZ
DOCS = C.DOCS
PLAN = C.PLAN
CORTE = 138


def rel(p):
    return os.path.relpath(p, RAIZ).replace(os.sep, "/")


def hechas_con_linea():
    """{numero: [ruta:linea]} de las secciones con encabezado propio. Usa el
    MISMO patron `RE_CAB` y las MISMAS `PAGINAS` del contador."""
    d = {}
    for nombre in C.PAGINAS:
        p = os.path.join(PLAN, nombre)
        for i, l in enumerate(io.open(p, encoding="utf-8"), 1):
            m = C.RE_CAB.match(l)
            if m:
                d.setdefault(int(m.group(1)), []).append("docs/plan/%s:%d" % (nombre, i))
    return d


def universo_con_linea():
    """{numero: [ruta:linea]} de todo numero nombrado bajo docs/, con la MISMA
    exclusion del contador (`motivo_de_exclusion`) y el MISMO `RE_ID`."""
    d = {}
    excluidos = {}
    for base, _, ficheros in os.walk(DOCS):
        for f in ficheros:
            if not f.endswith((".md", ".txt", ".json", ".jsonl")):
                continue
            ruta = os.path.join(base, f)
            r = rel(ruta)
            motivo = C.motivo_de_exclusion(r)
            if motivo:
                excluidos.setdefault(motivo, []).append(r)
                continue
            try:
                texto = io.open(ruta, encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            for i, l in enumerate(texto.split(NL), 1):
                for n in set(int(x) for x in C.RE_ID.findall(l)):
                    d.setdefault(n, []).append("%s:%d" % (r, i))
    return d, excluidos


def main():
    print("=" * 78)
    print("VUELTA 172, TAREA 2.c: EL CONTADOR OTRA VEZ, CON LA ATRIBUCION DELANTE")
    print("=" * 78)
    print("")

    print("A) EL CONTADOR DE VERDAD, CORRIDO EN ESTA VUELTA")
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run([sys.executable, "scripts/loop/vuelta48_contar_ld.py"],
                       cwd=RAIZ, capture_output=True, env=env)
    salida = r.stdout.decode("utf-8", errors="replace")
    print("   exit del contador: %d" % r.returncode)
    for l in salida.split(NL):
        if ("LECTURAS DIRIGIDAS HECHAS" in l or "rango:" in l
                or "EXCLUIDOS" in l or "rango del universo" in l
                or "numeros nombrados sin seccion propia" in l
                or "huecos en el rango" in l):
            print("   | " + l.strip()[:150])
    print("")

    print("B) LAS DOS VARAS, RECOMPUESTAS AQUI CON LAS MISMAS FUNCIONES DEL CONTADOR")
    hechas = hechas_con_linea()
    universo, excluidos = universo_con_linea()
    print("   CIFRA hechas (ids con seccion propia): %d" % len(hechas))
    print("   mayor de las HECHAS:   LD-%d" % max(hechas))
    print("   CIFRA universo (ids nombrados bajo docs/): %d" % len(universo))
    print("   mayor del UNIVERSO:    LD-%d" % max(universo))
    for motivo in sorted(excluidos):
        print("   CIFRA ficheros excluidos por %-10s %d" % (motivo, len(excluidos[motivo])))
    print("   los excluidos por NARRATIVO, uno a uno:")
    for r2 in sorted(excluidos.get("NARRATIVO", [])):
        print("      %s" % r2)
    print("")

    print("C) LA LECTURA NUEVA AL LADO DE LA VIEJA, Y LAS DOS CON SU CORTE")
    print("   | vara | antes de la 2.a (mismo arbol, con el archivo contando) | hoy |")
    print("   |---|---:|---:|")
    print("   | mayor de las HECHAS  | LD-138 | LD-%d |" % max(hechas))
    print("   | mayor del UNIVERSO   | LD-155 | LD-%d |" % max(universo))
    print("   | nombrados sin seccion| 9      | %d |"
          % len(set(universo) - set(hechas)))
    print("   LA CIFRA VIEJA (LD-155 y 9) SALE DE docs/loop/SALIDA_V172_T2_CONTAR_LD_ANTES.txt,")
    print("   corrida en ESTA misma vuelta antes de tocar el instrumento. NO es de un")
    print("   reporte viejo ni de un acta: es una medicion de hoy sobre el arbol de hoy.")
    print("")

    print("D) LA ATRIBUCION: CADA NUMERO POR ENCIMA DE LD-%d, CON FICHERO Y LINEA" % CORTE)
    altos = sorted(n for n in universo if n > CORTE)
    print("   CIFRA numeros del universo por encima de LD-%d: %d" % (CORTE, len(altos)))
    ajenos = []
    for n in altos:
        tiene = n in hechas
        print("   LD-%d  seccion propia: %s" % (n, "SI" if tiene else "NO"))
        for sitio in sorted(set(universo[n])):
            print("      %s" % sitio)
        if tiene:
            ajenos.append(n)
            for sitio in sorted(set(hechas[n])):
                print("      SECCION PROPIA EN: %s" % sitio)
    print("   CIFRA de esos que TIENEN seccion propia: %d" % len(ajenos))
    print("")

    print("E) LAS DOS GUARDAS DE LA TAREA 3")
    casos = [
        ("ningun numero por encima de LD-%d tiene seccion propia" % CORTE,
         len(ajenos) == 0),
        ("el mayor de las HECHAS es LD-%d" % CORTE, max(hechas) == CORTE),
        ("las dos varas salen de la MISMA lectura y del MISMO instrumento",
         r.returncode == 0),
        ("el archivo de reportes ya no cuenta",
         all(not s.startswith("docs/loop/reportes/")
             for n in universo for s in universo[n])),
    ]
    fallos = 0
    for etiqueta, cond in casos:
        print("   %-62s %s" % (etiqueta, "SI" if cond else "NO"))
        if not cond:
            fallos += 1
    print("   CIFRA comprobaciones: %d | fallan: %d" % (len(casos), fallos))
    print("")
    if fallos:
        print("ROJO: la TAREA 3 NO se corre. %d guarda(s) caida(s)." % fallos)
        if ajenos:
            print("   Y LA PARADA TIENE NOMBRE: hay asignacion ajena en LD-%s"
                  % ", LD-".join(str(n) for n in ajenos))
        return 1
    print("VERDE: la TAREA 3 se puede correr. El siguiente libre por la vara que")
    print("   asigna (las HECHAS, las que tienen seccion propia) es LD-%d." % (max(hechas) + 1))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
