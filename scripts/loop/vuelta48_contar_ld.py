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

TERCERA CORRECCION DECLARADA SOBRE MI PROPIO INSTRUMENTO, 19 ago 2026
(vuelta 50, encargada por el auditor en el acta de la vuelta 49, TAREA 1.2), y
OTRA VEZ EL TEXTO VIEJO DEL CRITERIO SE QUEDA DELANTE, SIN BORRAR. EL TEXTO
VIEJO ERA ESTE, y es el que la segunda correccion dejo escrito:

    "Los tres ficheros narrativos del bucle quedan EXCLUIDOS del universo, con
    la misma vara y por el mismo motivo que los SALIDA_*."
    (con NARRATIVOS_DEL_BUCLE = REPORTE.md, ACTA_AUDITOR.md, PROMPT_SIGUIENTE.md)

EL MOTIVO DE LA TERCERA, medido por el auditor y RE-MEDIDO aqui: la segunda
correccion tapo el agujero al nivel del PAPEL del bucle y lo dejo abierto UN
NIVEL MAS ARRIBA TODAVIA, en los REGISTROS DEL ARNES. El auditor midio 4
nombradas sin seccion porque docs/loop/ultimo_ejecutor.json, que NO esta en git
(.gitignore linea 26) y que el arnes escribe AL TERMINAR cada sesion, guardaba el
resumen de la vuelta 49 y en ese resumen citaba LD-12 y LD-27.

Y HAY UNA RAZON MAS FUERTE QUE LA DEL NIVEL, MEDIDA EN ESTA VUELTA Y QUE SE
ESCRIBE PORQUE ES LA QUE DE VERDAD CONDENA A ESOS FICHEROS: SU CONTENIDO NO ES
REPRODUCIBLE. La corrida del ejecutor de la vuelta 50, hecha ANTES de esta
correccion, dio 2 y no 4 (docs/loop/SALIDA_V50_CONTAR_LD_ANTES.txt), y la causa
es que docs/loop/ultimo_ejecutor.json estaba en CERO BYTES en ese momento: el
arnes lo vacia al abrir la sesion y lo reescribe al cerrarla. O sea que el mismo
instrumento, sobre el mismo repo y el mismo dia, devuelve una cifra distinta
segun EN QUE MINUTO DE LA SESION se corra. Una celda publicada no puede colgar de
eso. Los registros del arnes no son papel del plan ni salida de instrumento: son
estado de la maquina que corre el bucle, y no es un sitio donde quepa un ENCARGO.

CORRECCION DECLARADA 4 (vuelta 172, TAREA 2.a; adjudicacion 6.1 del acta 171).
EL ARCHIVO DE LOS REPORTES ES EL REPORTE. Desde que `archivar_reporte.py` guarda
cada reporte en `docs/loop/reportes/REPORTE_V<N>.md`, ese fichero entraba en el
universo y le metia TODOS los numeros de `LD` que el reporte narraba. Medido en
la vuelta 171: el sha256 de `docs/loop/reportes/REPORTE_V170.md` es identico byte
a byte al blob de `docs/loop/REPORTE.md` en `ca55afd8`, o sea que el instrumento
contaba como encargo un fichero que ya excluye por NARRATIVO DEL BUCLE, solo que
con otro nombre. Entra por PATRON de la carpeta de archivo, no por el nombre de
una vuelta, para que no haya que volver a tocarlo cada tres vueltas. NO es la
guarda general sobre ficheros nuevos bajo `docs/`, que el acta 170 reservo al
fundador.

LA VARA, escrita para poder discutirla: quedan EXCLUIDOS los ficheros
docs/loop/ultimo_*.json (hoy ultimo_ejecutor.json y ultimo_auditor.json, y sus
hermanos si el arnes anade alguno, que es lo que el patron cubre por adelantado).
docs/loop/loop.log ya quedaba fuera por su extension y se dice en vez de darlo
por supuesto: el universo solo barre .md, .txt, .json y .jsonl.

De solo lectura. No escribe nada.

Uso: python scripts/loop/vuelta48_contar_ld.py
"""
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

# LOS REGISTROS DEL ARNES del bucle: estado de la maquina que corre las sesiones,
# fuera de git, vaciado al abrir y reescrito al cerrar cada sesion. Ver la tercera
# correccion declarada del docstring. Es un PATRON y no una lista cerrada, para
# que un hermano nuevo del arnes no vuelva a entrar por la puerta de atras.
RE_ARNES = re.compile(r"^docs/loop/ultimo_[a-z_]+\.json$")

# EL ARCHIVO DE LOS REPORTES (correccion declarada 4, vuelta 172, TAREA 2.a;
# adjudicacion 6.1 del acta 171). `docs/loop/reportes/REPORTE_V<N>.md` NO SE
# PARECE al reporte: ES el reporte, guardado bajo otro nombre por
# `archivar_reporte.py`. Lo probo el sha256 de la vuelta 171, identico byte a
# byte al blob de `docs/loop/REPORTE.md` en `ca55afd8`. Sin esta linea, cada
# vuelta que archiva su reporte le mete al universo todos los numeros de `LD`
# que ese reporte NARRABA, y el instrumento vuelve a leerse a si mismo por la
# puerta de atras, que es la misma caida de las correcciones 1 y 2.
#
# ES UN PATRON Y NO UNA LISTA DE NOMBRES, a proposito: si aqui pusiera
# `REPORTE_V171.md`, dentro de tres vueltas habria que volver a tocar esto y
# nadie se acordaria. El patron cubre la carpeta de archivo entera y SOLO esa.
#
# LO QUE ESTO NO ES: no es la guarda general sobre ficheros nuevos bajo `docs/`
# que el acta 170 reservo al fundador en su seccion 7.3. Esa sigue siendo suya.
RE_ARCHIVO_DEL_REPORTE = re.compile(r"^docs/loop/reportes/REPORTE_V\d+\.md$")


def motivo_de_exclusion(rel):
    """POR QUE UN FICHERO NO ENTRA EN EL UNIVERSO. Devuelve la etiqueta del
    motivo, o None si el fichero SI cuenta.

    PURA A PROPOSITO (vuelta 172, TAREA 2.a): antes este criterio vivia dentro
    del bucle de `main()` y no habia nada que un arnes pudiera llamar, asi que
    no se podia probar por mutacion. Ahora `main()` llama aqui y no hay dos
    copias del criterio.

    `rel` es la ruta relativa a la raiz, con barra unix."""
    nombre = rel.rsplit("/", 1)[-1]
    if nombre.startswith("SALIDA_"):
        return "SALIDA"
    if rel in NARRATIVOS_DEL_BUCLE:
        return "NARRATIVO"
    if RE_ARCHIVO_DEL_REPORTE.match(rel):
        return "NARRATIVO"
    if RE_ARNES.match(rel):
        return "ARNES"
    return None

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
    excluidos_arnes = []
    for base, _, ficheros in os.walk(DOCS):
        for f in ficheros:
            if not f.endswith((".md", ".txt", ".json", ".jsonl")):
                continue
            # EXCLUIDOS: la salida de los instrumentos no es un encargo. Ver la
            # correccion declarada del docstring: sin esto, este instrumento se
            # lee a si mismo y se inventa encargos con su propia lista de huecos.
            rel_f = os.path.relpath(os.path.join(base, f), RAIZ).replace("\\", "/")
            # EXCLUIDOS, TRES FAMILIAS Y UN MISMO MOTIVO: ninguna de las tres es
            # un sitio donde quepa un ENCARGO, las tres son salida propia del
            # bucle o de su arnes.
            #  (a) SALIDA_*: la salida cruda de los instrumentos (correccion 1).
            #  (b) LOS NARRATIVOS DEL BUCLE: el reporte, el acta y el prompt, que
            #      NARRAN las mediciones y por eso citan numeros de LD al contar
            #      lo ya medido (correccion 2, vuelta 49). Ver el docstring.
            #  (c) LOS REGISTROS DEL ARNES (docs/loop/ultimo_*.json): estado de la
            #      maquina, fuera de git, y con contenido NO REPRODUCIBLE dentro
            #      de una misma sesion (correccion 3, vuelta 50). Ver el docstring.
            # UNA SOLA FUENTE DEL CRITERIO: la funcion pura de arriba, que es
            # la que el arnes de mutacion llama (vuelta 172, TAREA 2.a).
            motivo = motivo_de_exclusion(rel_f)
            if motivo == "SALIDA":
                excluidos.append(rel_f)
                continue
            if motivo == "NARRATIVO":
                excluidos_narrativos.append(rel_f)
                continue
            if motivo == "ARNES":
                excluidos_arnes.append(rel_f)
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
    print("  ficheros EXCLUIDOS por ser REGISTROS DEL ARNES: %d  ->  %s"
          % (len(excluidos_arnes),
             ", ".join(sorted(excluidos_arnes)) or "ninguno"))
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
