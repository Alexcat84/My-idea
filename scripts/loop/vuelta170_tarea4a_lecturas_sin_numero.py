# -*- coding: utf-8 -*-
r"""vuelta170_tarea4a_lecturas_sin_numero.py . TAREA 4.a de la vuelta 170.

MIDE LAS LECTURAS DE LA SEGUNDA TANDA QUE NO TIENEN NUMERO `LD`, Y MIDE LA SERIE
`LD` ENTERA, PARA PODER DECIDIR QUE NUMERO LES TOCA. NO ESCRIBE NADA.

POR QUE NACE (adjudicacion 6.9 del acta 169, el `D.8` y el `PD.2` del reporte de
la 169). Gate 0 ya exige que todo par bidireccional entre nodos vivos tenga su
veredicto de lectura REGISTRADO CON CITA, y una lectura que no se puede citar
por su nombre no cumple esa exigencia. Las filas de tabla de la segunda tanda de
`docs/plan/LECTURAS_DIRIGIDAS.md` no se pueden citar. El remedio que el acta
manda es de ADICION PURA: ganan numero `LD` y no pierden una palabra de su
texto, con el siguiente libre COMPUTADO POR INSTRUMENTO.

Y AQUI ESTA LA RAZON DE QUE ESTE FICHERO MIDA Y NO ESCRIBA. El encargo dice, con
estas palabras: *"Si al contarlas el instrumento dice algo distinto de lo que
este encargo supone, PARAS Y LO TRAES."* Lo dice. La serie `LD` NO se parece a
la serie `R.n`:

  - la serie `R.n` tiene CERO huecos, y por eso "el siguiente libre" es
    "el mayor mas uno" sin ambiguedad ninguna;
  - la serie `LD` tiene HUECOS, y uno de ellos es un tramo corrido que empieza
    justo donde acaba la primera tanda y acaba justo donde empieza la tercera.

Con huecos, "el siguiente libre" deja de tener un solo significado, y elegir
entre los dos NO es una lectura del encargo: es una regla nueva. `EJECUTOR.md` 5
dice que no se inventan reglas. Asi que este instrumento MIDE LOS DOS CAMINOS,
los nombra con su cifra, y la vuelta lo trae como PARADA.

QUE MIDE:
  A. Las filas de tabla sin numero de la segunda tanda, una a una, con su par y
     su clase, contadas del fichero y no tecleadas.
  B. La serie `LD` entera, con el instrumento de la casa que ya existe para eso,
     `scripts/loop/vuelta48_contar_ld.py`, corrido HOY.
  C. Los dos candidatos de numeracion, con sus numeros exactos, para que la
     decision se tome mirando las dos cifras y no de memoria.

USO:
  python scripts/loop/vuelta170_tarea4a_lecturas_sin_numero.py
"""
import io
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DOC = os.path.join(RAIZ, "docs", "plan", "LECTURAS_DIRIGIDAS.md")
CONTADOR = os.path.join(RAIZ, "scripts", "loop", "vuelta48_contar_ld.py")
INICIO = "# SEGUNDA TANDA: LA SELECCION DE `OP-L-02`"
FIN = "# TERCERA TANDA:"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 78)
    print("VUELTA 170, TAREA 4.a: LAS LECTURAS DE LA SEGUNDA TANDA SIN NUMERO LD")
    print("=" * 78)
    print("")

    lineas = io.open(DOC, encoding="utf-8").read().split(chr(10))
    ini = [i for i, l in enumerate(lineas, 1) if l.startswith(INICIO)]
    fin = [i for i, l in enumerate(lineas, 1) if l.startswith(FIN)]
    print("A) LA SEGUNDA TANDA, ACOTADA ANTES DE CONTAR NADA")
    print("   docs/plan/LECTURAS_DIRIGIDAS.md: %d lineas" % len(lineas))
    if len(ini) != 1 or not fin:
        print("   ROJO: la cabecera de la segunda tanda aparece %d veces y la de la"
              " tercera %d." % (len(ini), len(fin)))
        return 1
    a = ini[0]
    b = min(f for f in fin if f > a) - 1
    print("   segunda tanda: lineas %d a %d" % (a, b))
    print("")

    print("B) SUS TABLAS DE LECTURA, LOCALIZADAS POR SU CABECERA `| par | clase |`")
    tablas = []
    for i in range(a, b + 1):
        l = lineas[i - 1].strip()
        if re.match(r"^\|\s*par\s*\|\s*clase\s*\|$", l):
            titulo = ""
            for j in range(i - 1, a - 1, -1):
                if lineas[j - 1].startswith("## "):
                    titulo = lineas[j - 1][3:].strip()
                    break
            tablas.append((i, titulo))
    print("   CIFRA tablas de lectura halladas: %d" % len(tablas))
    for n, t in tablas:
        print("      linea %d, bajo '%s'" % (n, t))
    if not tablas:
        print("   ROJO: no hay ninguna tabla de lectura en la segunda tanda.")
        return 1
    print("")

    print("C) LAS FILAS, UNA A UNA, CONTADAS DEL FICHERO")
    filas = []
    for n, titulo in tablas:
        k = n + 2   # la cabecera y la linea de guiones
        while k <= b and lineas[k - 1].strip().startswith("|"):
            celdas = [c.strip() for c in lineas[k - 1].strip().strip("|").split("|")]
            if len(celdas) >= 2 and celdas[0]:
                filas.append((titulo, k, celdas[0], celdas[1]))
            k += 1
    for titulo, k, par, clase in filas:
        lleva = bool(re.search(r"LD-\d+", par))
        print("   %-34s linea %-5d %-3s %s"
              % (titulo[:34], k, clase.replace("*", ""),
                 ("YA LLEVA LD" if lleva else "SIN NUMERO") + "  " + par[:70]))
    sin_numero = [f for f in filas if not re.search(r"LD-\d+", f[2])]
    print("   CIFRA filas de lectura en la segunda tanda: %d" % len(filas))
    print("   CIFRA de ellas SIN numero LD: %d" % len(sin_numero))
    por_tabla = {}
    for titulo, _k, _p, _c in sin_numero:
        por_tabla[titulo] = por_tabla.get(titulo, 0) + 1
    for t in sorted(por_tabla):
        print("      %-40s %d" % (t[:40], por_tabla[t]))
    print("")
    print("   CONTRASTE CON LA PROSA DE LA PROPIA TANDA, Y ES CONTRASTE Y NO FUENTE:")
    dice = [l for l in lineas[a - 1:b] if "SE LEEN DIECISEIS" in l]
    print("      la tanda dice literalmente: %s"
          % (dice[0].strip() if dice else "(no dice ninguna cifra en palabra)"))
    print("      yo cuento %d filas sin numero, %s"
          % (len(sin_numero), "CALZA" if len(sin_numero) == 16 else "NO CALZA"))
    print("")

    print("D) LA SERIE LD ENTERA, CON EL INSTRUMENTO DE LA CASA CORRIDO HOY")
    print("   comando: python scripts/loop/vuelta48_contar_ld.py")
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run([sys.executable, CONTADOR], cwd=RAIZ, capture_output=True, env=env)
    sal = r.stdout.decode("utf-8", errors="replace") + r.stderr.decode("utf-8", errors="replace")
    hechas = re.search(r"ids distintos con seccion propia\):\s*(\d+)", sal)
    rango = re.search(r"rango del universo:\s*LD-(\d+) a LD-(\d+)", sal)
    hue = re.search(r"huecos en el rango:\s*(\d+)\s*->\s*([^\n]*)", sal)
    if not (hechas and rango and hue):
        print("   ROJO: el contador de la casa no imprime lo que este instrumento lee.")
        return 1
    huecos = [int(x.strip()[3:]) for x in hue.group(2).split(",") if x.strip()]
    mayor = int(rango.group(2))
    print("   CIFRA lecturas dirigidas HECHAS (con seccion propia): %s" % hechas.group(1))
    print("   rango del universo: LD-%s a LD-%s" % (rango.group(1), rango.group(2)))
    print("   CIFRA huecos en el rango: %d" % len(huecos))
    corridos = []
    for h in huecos:
        if corridos and h == corridos[-1][-1] + 1:
            corridos[-1].append(h)
        else:
            corridos.append([h])
    print("   CIFRA tramos corridos de huecos: %d" % len(corridos))
    for tramo in corridos:
        print("      LD-%02d a LD-%02d, %d numeros" % (tramo[0], tramo[-1], len(tramo)))
    print("")

    print("E) LOS DOS CAMINOS, MEDIDOS LOS DOS, Y NINGUNO ELEGIDO AQUI")
    n = len(sin_numero)
    print("   CAMINO 1, LA VARA LITERAL DEL ENCARGO (la de serie_de_registros.py,")
    print("   'el siguiente libre' = el mayor mas uno):")
    print("      LD-%d a LD-%d" % (mayor + 1, mayor + n))
    print("      LO QUE TIENE A FAVOR: es la vara que el encargo nombra por su")
    print("      nombre, y no inventa ninguna regla.")
    print("      LO QUE TIENE EN CONTRA: pone lecturas del 11 ago 2026 DESPUES de")
    print("      LD-138, que es de una tanda muy posterior, y deja los 54 huecos")
    print("      donde estan.")
    encaja = [t for t in corridos if len(t) == n]
    print("")
    print("   CAMINO 2, RELLENAR EL TRAMO QUE ENCAJA:")
    if not encaja:
        print("      NO HAY ningun tramo corrido de huecos de exactamente %d"
              " numeros. Este camino no existe." % n)
    for tramo in encaja:
        print("      LD-%02d a LD-%02d, que son EXACTAMENTE %d numeros, los mismos"
              " que filas sin numero." % (tramo[0], tramo[-1], len(tramo)))
        print("      LO QUE TIENE A FAVOR: el tramo empieza donde acaba la primera")
        print("      tanda (LD-11) y acaba donde empieza la tercera (LD-28), o sea")
        print("      que es el sitio cronologico exacto de estas lecturas, y el")
        print("      tamano coincide al numero.")
        print("      LO QUE TIENE EN CONTRA: 'rellenar huecos' NO es lo que")
        print("      serie_de_registros.py hace, y adoptarlo seria REGLA NUEVA.")
    print("")

    print("F) EL VEREDICTO DE ESTE INSTRUMENTO")
    print("   NO SE ESCRIBE NINGUNA NUMERACION. Los dos caminos dan numeros")
    print("   DISTINTOS para las mismas %d lecturas, la diferencia es visible" % n)
    print("   (LD-%d..LD-%d contra LD-%02d..LD-%02d) y elegir entre ellos es"
          % (mayor + 1, mayor + n,
             encaja[0][0] if encaja else 0, encaja[0][-1] if encaja else 0))
    print("   escribir una regla que no existe. EJECUTOR.md 5: no se inventan")
    print("   reglas; y el propio encargo dice PARAS Y LO TRAES si el instrumento")
    print("   dice algo distinto de lo que el supone. Se trae como PARADA.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
