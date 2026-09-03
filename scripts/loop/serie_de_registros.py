# -*- coding: utf-8 -*-
r"""serie_de_registros.py . LA SERIE `R.N`, RECOMPUTADA DE SUS DOS SEDES.

Nombre estable y SIN numero de vuelta (como `tallar_cabecera_reporte.py` y
`verificar_apertura_sellada.py`): se invoca cada vez que haya que escribir un
registro nuevo, y no se clona por vuelta.

--- POR QUE NACE (vuelta 162, TAREA 1.a; acta 161, seccion 5.1 y adjudicacion
6.8) ---

LA CAIDA, CON SU NOMBRE. En la vuelta 161 el ejecutor escribio
`## R.29. Registro de las caidas de clase...` en `docs/PENDIENTES.md` declarando
que *"la ultima escrita era `R.28`"*. **`R.29` YA ESTABA ASIGNADA** desde la
vuelta 150 y vive en `docs/plan/CORRECCIONES_A_APLICAR.md:2127`. Y la prueba
estaba en el mismo fichero que se abrio: `docs/PENDIENTES.md:10389` dice, literal,
*"REMISION (vuelta 150, TAREA 1.a): `R.29`, el registro del acta de la vuelta
149, NO esta en esta pagina ... la fuente unica de `R.29` es esa pagina"*.

LAS DOS CAUSAS, LAS DOS DE INSTRUMENTO, leidas en el codigo de
`scripts/loop/vuelta161_tarea1_0_registros.py`:
  (i)  EL ULTIMO NUMERO ESTABA TECLEADO, en la propia cabecera del script
       (*"con la ultima escrita siendo `R.28`"*) y en la constante `MARCA`.
  (ii) SU IDEMPOTENCIA MIRABA UN SOLO FICHERO, `docs/PENDIENTES.md`, cuando la
       serie `R.N` es GLOBAL A LOS DOS, y lo prueba la propia remision.

QUE HACE ESTE INSTRUMENTO. Recompone la serie leyendo LOS DOS ficheros e imprime
la serie ENTERA con su sede fichero por fichero, mas el siguiente numero libre.
EL NUMERO NO SE TECLEA NUNCA MAS: quien vaya a escribir un registro llama a
`siguiente_libre()` y usa lo que devuelve.

LA VARA DEL TITULO, Y SE DICE POR QUE ES ESA. La serie global usa `## R.N.` (DOS
almohadillas y punto detras del numero). En `docs/PENDIENTES.md` viven ademas
unos `### R.N` (TRES almohadillas y sin punto) que son OTRA cosa: una numeracion
LOCAL dentro de la seccion *"VUELTA 119, TAREA 2: LOS REGISTROS DEL ACTA 118"* y
sus hermanas, donde `R.1` y `R.2` aparecen repetidas. Confundirlas seria contar
dos series como una.

USO:
  python scripts/loop/serie_de_registros.py
  python scripts/loop/serie_de_registros.py --sedes ruta1.md ruta2.md
"""
import argparse
import io
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# LAS DOS SEDES DE LA SERIE. Es una lista, no una constante suelta, justo porque
# la caida de la vuelta 161 fue mirar una sola.
SEDES = [
    os.path.join(RAIZ, "docs", "PENDIENTES.md"),
    os.path.join(RAIZ, "docs", "plan", "CORRECCIONES_A_APLICAR.md"),
]

# `## R.<numero>.` al principio de linea. Las TRES almohadillas quedan fuera a
# proposito (ver docstring).
PATRON = re.compile(r"^##\s+R\.(\d+)\.")


def entradas(rutas=None):
    """La serie leida de sus sedes. Devuelve [(numero, ruta_relativa, linea,
    titulo)], ordenada por numero y despues por sede.

    PURA salvo por leer los ficheros que se le pasan: `rutas` es parametro para
    que el caso positivo por mutacion pueda apuntarla a copias de trabajo sin
    tocar el repo."""
    rutas = list(rutas) if rutas else list(SEDES)
    halladas = []
    for ruta in rutas:
        rel = os.path.relpath(ruta, RAIZ).replace("\\", "/")
        texto = io.open(ruta, encoding="utf-8", errors="replace").read()
        for i, linea in enumerate(texto.split("\n"), 1):
            m = PATRON.match(linea)
            if m:
                halladas.append((int(m.group(1)), rel, i, linea.strip()))
    halladas.sort(key=lambda x: (x[0], x[1], x[2]))
    return halladas


def colisiones(halladas):
    """Numeros escritos mas de una vez, cada uno con todas sus sedes."""
    por_numero = {}
    for numero, rel, linea, titulo in halladas:
        por_numero.setdefault(numero, []).append((rel, linea, titulo))
    return {n: v for n, v in sorted(por_numero.items()) if len(v) > 1}


def huecos(halladas):
    """Numeros que faltan entre el minimo y el maximo escritos."""
    nums = sorted(set(n for n, _r, _l, _t in halladas))
    if not nums:
        return []
    return [n for n in range(nums[0], nums[-1] + 1) if n not in nums]


def siguiente_libre(halladas):
    """EL NUMERO QUE NO SE TECLEA. Uno mas que el mayor escrito en CUALQUIERA de
    las sedes. No rellena huecos a proposito: un hueco puede ser un registro
    retirado y reusar su numero rompeia las citas viejas."""
    nums = [n for n, _r, _l, _t in halladas]
    return (max(nums) + 1) if nums else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sedes", nargs="*", default=None)
    a = ap.parse_args()
    rutas = a.sedes if a.sedes else SEDES

    print("=" * 78)
    print("LA SERIE R.N, RECOMPUTADA DE SUS DOS SEDES (vuelta 162, TAREA 1.a)")
    print("=" * 78)
    print("")
    print("A) LAS SEDES QUE SE LEEN, Y SON LAS DOS")
    for ruta in rutas:
        print("   %s" % os.path.relpath(ruta, RAIZ).replace("\\", "/"))
    print("")

    halladas = entradas(rutas)
    print("B) LA SERIE ENTERA, FICHERO POR FICHERO, SIN RESUMIR")
    for numero, rel, linea, titulo in halladas:
        print("   R.%-3d %s:%-6d %s" % (numero, rel, linea, titulo[:96]))
    print("")

    por_sede = {}
    for numero, rel, _l, _t in halladas:
        por_sede.setdefault(rel, []).append(numero)
    print("C) EL REPARTO POR SEDE, CONTADO")
    for rel in sorted(por_sede):
        nums = por_sede[rel]
        print("   CIFRA entradas en %s: %d (%s)"
              % (rel, len(nums), ", ".join("R.%d" % n for n in nums)))
    print("   CIFRA entradas en total: %d" % len(halladas))
    print("")

    cols = colisiones(halladas)
    hue = huecos(halladas)
    print("D) LA SALUD DE LA SERIE")
    print("   CIFRA numeros distintos: %d" % len(set(n for n, _r, _l, _t in halladas)))
    print("   CIFRA colisiones (un numero escrito mas de una vez): %d" % len(cols))
    for numero, sitios in cols.items():
        print("      R.%d escrito %d veces:" % (numero, len(sitios)))
        for rel, linea, titulo in sitios:
            print("         %s:%d  %s" % (rel, linea, titulo[:88]))
    print("   CIFRA huecos: %d (%s)" % (len(hue), ", ".join("R.%d" % n for n in hue) or "ninguno"))
    print("")

    print("E) EL NUMERO QUE NO SE TECLEA")
    print("   CIFRA mayor numero escrito: R.%d" % max(n for n, _r, _l, _t in halladas))
    print("   SIGUIENTE LIBRE: R.%d" % siguiente_libre(halladas))
    print("")
    if cols:
        print("ROJO: la serie tiene %d colision(es). Se declara, no se tapa." % len(cols))
        return 1
    print("VERDE: la serie no tiene colisiones.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
