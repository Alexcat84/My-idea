# -*- coding: utf-8 -*-
"""Vuelta 48, TAREA 1.4: LAS DOS FILAS DE LECTURAS DIRIGIDAS DEL 00_INDICE,
MEDIDAS CON INSTRUMENTO EN VEZ DE MARCADAS `A VERIFICAR`.

La vuelta 47 dejo las dos celdas en `A VERIFICAR` porque ningun instrumento suyo
las contaba, y eso fue correcto: una cifra sin medicion de hoy no se republica.
Este instrumento las cuenta.

QUE ES UNA LECTURA DIRIGIDA HECHA, y el criterio va escrito para poder discutirlo:
una lectura dirigida esta HECHA cuando tiene su PROPIA SECCION con veredicto en
las paginas de lecturas dirigidas del plan, o sea un encabezado markdown que abra
con su numero. Es la forma que la campana uso desde la primera tanda
(docs/plan/LECTURAS_DIRIGIDAS.md) y la que copiaron las paginas por nomina
(docs/plan/LD_*.md). Contar en cambio TODA mencion de un numero contaria las
citas cruzadas, que son muchas.

QUE ES UNA ENCARGADA Y SIN HACER: un numero que aparece nombrado en un sitio
donde CABE UN ENCARGO y NO tiene seccion propia en ninguna de esas paginas. Un
encargo se escribe en el acta, en el prompt, en una parada o en una pagina del
plan; no en la pagina que aun no existe. Por eso el universo se barre ancho y
no solo sobre las paginas de lecturas dirigidas.

CORRECCION DECLARADA SOBRE MI PROPIO INSTRUMENTO, 19 ago 2026 (vuelta 48), y el
motivo se queda escrito porque el siguiente pisara la misma piedra: la primera
version barria docs/ ENTERO, incluidos los SALIDA_*.txt, que son la salida de
los propios instrumentos. Resultado: su seccion 5 imprime la lista de huecos
"LD-12, LD-13, ... LD-27", y la segunda corrida LEIA ESA LISTA como si fueran
numeros nombrados. El universo pasaba de 83 a 99 y las encargadas sin hacer de
2 a 18, SIN QUE NADA HUBIERA CAMBIADO EN EL PLAN. Un instrumento que se lee a
si mismo se da la razon solo. Los SALIDA_*.txt quedan EXCLUIDOS: son medicion,
no encargo. Se vio antes de publicar y no llego a ninguna celda.

SEGUNDA CORRECCION DECLARADA SOBRE MI PROPIO INSTRUMENTO, 19 ago 2026
(vuelta 49, encargada por el auditor en el acta de la vuelta 48, TAREA 1.2), y
EL TEXTO VIEJO DEL CRITERIO SE QUEDA DELANTE, SIN BORRAR, porque una correccion
que tapa lo que corrige no se puede auditar. EL TEXTO VIEJO ERA ESTE, y decia lo
suficiente para la primera piedra pero no para la segunda:

    "QUE ES UNA ENCARGADA Y SIN HACER: un numero que aparece nombrado en un
    sitio donde CABE UN ENCARGO y NO tiene seccion propia en ninguna de esas
    paginas. Un encargo se escribe en el acta, en el prompt, en una parada o en
    una pagina del plan; no en la pagina que aun no existe. Por eso el universo
    se barre ancho y no solo sobre las paginas de lecturas dirigidas."
    "Los SALIDA_*.txt quedan EXCLUIDOS: son medicion, no encargo."

EL MOTIVO DE LA SEGUNDA CORRECCION, medido por el auditor y reproducido aqui: la
primera correccion tapo el agujero por el nombre del fichero (SALIDA_*) y lo dejo
abierto UN NIVEL MAS ARRIBA. Los ficheros NARRATIVOS del bucle (REPORTE.md,
ACTA_AUDITOR.md, PROMPT_SIGUIENTE.md) tambien son mi propia salida: el REPORTE de
la vuelta 48 CITA "LD-12" y "LD-27" al narrar su correccion 1, o sea al contar
que la lista de huecos se leia a si misma. La corrida del 19 ago 2026 antes de
esta correccion daba 4 nombradas sin seccion y 14 huecos por esa unica causa
(docs/loop/SALIDA_V49_CONTAR_LD_ANTES.txt, seccion 4: LD-12 y LD-27, los dos
nombrados SOLO en docs/loop/PROMPT_SIGUIENTE.md y docs/loop/REPORTE.md). Un
instrumento que se lee a si mismo se da la razon solo, y la narracion de una
medicion es medicion, no encargo: un encargo de lectura dirigida se escribe en
una pagina del PLAN, no en el reporte que cuenta lo que ya se midio. Los tres
ficheros narrativos del bucle quedan EXCLUIDOS del universo, con la misma vara y
por el mismo motivo que los SALIDA_*.

De solo lectura. No escribe nada.

Uso: python scripts/loop/vuelta48_contar_ld.py
"""
# ROTULO titulo especie=PROCEDENCIA cita=vuelta:48 fuente=scripts/loop/vuelta48_contar_ld.py prueba="Vuelta 48, TAREA 1.4" corte=2026-08-20 motivo="es la copia de contraste del instrumento de la vuelta 48 y conserva su cabecera a proposito"
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DOCS = os.path.join(RAIZ, "docs")
PLAN = os.path.join(DOCS, "plan")

# Las paginas donde una lectura dirigida se escribe con seccion propia.
PAGINAS = ["LECTURAS_DIRIGIDAS.md"] + sorted(
    f for f in os.listdir(PLAN) if f.startswith("LD_") and f.endswith(".md"))

# Los ficheros NARRATIVOS del bucle: cuentan lo que los instrumentos midieron y
# por eso citan numeros de LD sin encargar nada. Ver la segunda correccion
# declarada del docstring. Rutas relativas a la raiz, con barra unix.
NARRATIVOS_DEL_BUCLE = {
    "docs/loop/REPORTE.md",
    "docs/loop/ACTA_AUDITOR.md",
    "docs/loop/PROMPT_SIGUIENTE.md",
}

RE_ID = re.compile(r"LD-(\d+)")
RE_CAB = re.compile(r"^#+\s*\**\s*`?LD-(\d+)`?")


def sep(t):
    print()
    print("=" * 78)
    print(t)
    print("=" * 78)


def main():
    sys.stdout.reconfigure(encoding="utf-8")

    sep("1. LAS PAGINAS DONDE UNA LECTURA DIRIGIDA SE ESCRIBE")
    hechas = {}
    for nombre in PAGINAS:
        p = os.path.join(PLAN, nombre)
        vistos = []
        for i, l in enumerate(io.open(p, encoding="utf-8"), 1):
            m = RE_CAB.match(l)
            if m:
                n = int(m.group(1))
                vistos.append(n)
                hechas.setdefault(n, []).append("%s:%d" % (nombre, i))
        print("  %-32s secciones con encabezado propio: %3d (ids distintos %3d)"
              % (nombre, len(vistos), len(set(vistos))))
    print()
    print("  LECTURAS DIRIGIDAS HECHAS (ids distintos con seccion propia): %d"
          % len(hechas))
    print("  rango: LD-%02d a LD-%02d" % (min(hechas), max(hechas)))

    sep("2. LOS IDS CON MAS DE UNA SECCION (no cuentan dos veces)")
    dobles = {k: v for k, v in hechas.items() if len(v) > 1}
    print("  ids con seccion repetida: %d" % len(dobles))
    for k in sorted(dobles):
        print("     LD-%02d en %s" % (k, ", ".join(dobles[k])))

    sep("3. EL UNIVERSO: TODO NUMERO NOMBRADO EN docs/ ENTERO")
    universo = {}
    excluidos = []
    excluidos_narrativos = []
    for base, _, ficheros in os.walk(DOCS):
        for f in ficheros:
            if not f.endswith((".md", ".txt", ".json", ".jsonl")):
                continue
            # EXCLUIDOS: la salida de los instrumentos no es un encargo. Ver la
            # correccion declarada del docstring: sin esto, este instrumento se
            # lee a si mismo y se inventa encargos con su propia lista de huecos.
            rel_f = os.path.relpath(os.path.join(base, f), RAIZ).replace("\\", "/")
            # EXCLUIDOS, DOS FAMILIAS Y UN MISMO MOTIVO: ninguna de las dos es un
            # sitio donde quepa un ENCARGO, las dos son salida propia del bucle.
            #  (a) SALIDA_*: la salida cruda de los instrumentos (correccion 1).
            #  (b) LOS NARRATIVOS DEL BUCLE: el reporte, el acta y el prompt, que
            #      NARRAN las mediciones y por eso citan numeros de LD al contar
            #      lo ya medido (correccion 2, vuelta 49). Ver el docstring.
            if f.startswith("SALIDA_"):
                excluidos.append(rel_f)
                continue
            if rel_f in NARRATIVOS_DEL_BUCLE:
                excluidos_narrativos.append(rel_f)
                continue
            p = os.path.join(base, f)
            try:
                t = io.open(p, encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            rel = os.path.relpath(p, RAIZ).replace("\\", "/")
            for n in set(int(x) for x in RE_ID.findall(t)):
                universo.setdefault(n, []).append(rel)
    print("  ficheros EXCLUIDOS por ser salida de instrumento (SALIDA_*): %d"
          % len(excluidos))
    print("  ficheros EXCLUIDOS por ser NARRATIVOS del bucle: %d  ->  %s"
          % (len(excluidos_narrativos),
             ", ".join(sorted(excluidos_narrativos)) or "ninguno"))
    print("  ficheros barridos bajo docs/: numeros distintos hallados = %d"
          % len(universo))
    print("  rango del universo: LD-%02d a LD-%02d" % (min(universo), max(universo)))

    sep("4. LAS ENCARGADAS Y SIN HACER: nombradas y SIN seccion propia")
    sin = sorted(set(universo) - set(hechas))
    print("  numeros nombrados sin seccion propia: %d" % len(sin))
    for n in sin:
        print()
        print("     LD-%02d nombrado en %d fichero(s):" % (n, len(universo[n])))
        for r in sorted(universo[n]):
            print("        %s" % r)

    sep("5. LOS HUECOS DE NUMERACION (ni nombrados ni hechos)")
    huecos = [n for n in range(min(universo), max(universo) + 1)
              if n not in universo]
    print("  huecos en el rango: %d -> %s"
          % (len(huecos), ", ".join("LD-%02d" % n for n in huecos) or "ninguno"))
    print("  NO son encargos pendientes: son numeros que nunca se nombraron.")

    sep("6. LAS DOS CELDAS DEL 00_INDICE, IMPRESAS")
    print("  | lecturas dirigidas **hechas**              | **%d** |" % len(hechas))
    print("  | lecturas dirigidas **encargadas sin hacer** | **%d** |" % len(sin))
    print()
    print("  La cifra vieja de la tabla de la sesion B era 65 hechas y CERO")
    print("  encargadas, con corte 12 ago 2026. La de hoy se publica al lado; si")
    print("  discrepa, se declara la discrepancia y no se resuelve copiando.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
