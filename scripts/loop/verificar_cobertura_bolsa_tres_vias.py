# -*- coding: utf-8 -*-
r"""verificar_cobertura_bolsa_tres_vias.py . TAREA 2 de la vuelta 108 (encargo
del auditor, acta de la vuelta 107, caida 1.1: "el 74/74 que es 73/74").
Nombre estable, SIN numero de vuelta (como tallar_cabecera_reporte.py y
contar_cierre_efectivo.py): no se clona cada vuelta.

POR QUE NACE. El reporte de la vuelta 107 publico "de las 74 RESUELTA vivas,
74 han pasado por la pregunta de tres vias (74/74)" en un .txt tecleado a
mano (SALIDA_V107_TAREA5_5_CIFRA_FINAL_BOLSA.txt, que no tiene script que lo
produzca: `grep -rn "sin pregunta de tres vias" scripts/` da CERO). La cifra
real, contada por el auditor de las salidas de los barridos, es 73/74: el 46
nunca recibio la pregunta, apartado cada vuelta por la guarda del paso mal
casado (docs/loop/SALIDA_V105_TAREA4_3_RE_BARRIDO.txt lo dice literal:
"SALTAN 1 puesto(s) por (4.1), nota de paso mal casado").

QUE HACE. Cuenta la cobertura DE LAS SALIDAS, no de la memoria: (1) toma las
RESUELTA vivas de HOY llamando a `contar_cierre_efectivo.cifras()` sobre los
cuatro tramos de OP-E-03 (la misma fuente que ya aplica correccion_vNN); (2)
recorre la lista FICHEROS_VEREDICTO declarada abajo (impresa entera en la
salida, para que un fichero olvidado se note) y extrae, de cada uno, los
puestos que SI recibieron un veredicto de la pregunta de tres vias
(OBJETO / SATELITE / NO_OBJETO); (3) cruza las dos listas e imprime cuantas
vivas hay, cuantas tienen pregunta, y la lista NOMINAL de las que no.

DOS FORMATOS DE FICHERO, LOS DOS QUE EXISTEN HOY EN docs/loop/:
  - "bloque": encabezado `--- PUESTO N ---` seguido, en las lineas que le
    siguen (hasta la proxima linea en blanco o el proximo encabezado), de una
    linea `VEREDICTO: PALABRA`. Un puesto SALTADO (guarda del paso mal
    casado, ejemplo el 46 en la vuelta 105) NO trae encabezado `--- PUESTO N
    ---`: no se cuenta, que es lo correcto.
  - "tabla": lineas `N | ... | PALABRA` o `N | ... | PALABRA (explicacion)`,
    con el puesto al principio de la linea seguido de ` | `.
  PALABRA es una de OBJETO, SATELITE, NO_OBJETO.

SIN FICHERO QUE CONTAR, NO HAY TABLA: si `FICHEROS_VEREDICTO` trajera una
ruta que no existe, el instrumento cae en ROJO (exit 1) y no imprime cifra
ninguna, en vez de contar silenciosamente con lo que si encontro.

USO:
  python scripts/loop/verificar_cobertura_bolsa_tres_vias.py

CASO POSITIVO (vuelta 108, ANTES de la TAREA 3): 74 vivas, 73 con pregunta,
1 sin ella, nombra el 46 (docs/loop/SALIDA_V108_TAREA2_3_CASO_POSITIVO.txt).

CASO ROJO POR MUTACION (vuelta 108): copia de
docs/loop/SALIDA_V107_TAREA5_3_TRAMO1_TRES_VIAS.md con la fila del puesto 3
borrada (docs/loop/_v108_mut/SALIDA_V107_TAREA5_3_TRAMO1_TRES_VIAS_MUTADO.md),
puesta EN EL LUGAR del fichero real (no aditiva) al llamar
`puestos_con_pregunta()`: el 3 tiene que aparecer en la lista de los que no
recibieron la pregunta (docs/loop/SALIDA_V108_TAREA2_4_CASO_ROJO_MUTACION.txt).
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOOP = os.path.join(RAIZ, "docs", "loop")
sys.path.insert(0, os.path.join(RAIZ, "scripts", "loop"))
import contar_cierre_efectivo as cce  # noqa: E402

# LA LISTA NO SE TECLEA A MANO SIN QUE SE NOTE (TAREA 2.2): se declara aqui,
# como constante, Y EL INSTRUMENTO LA IMPRIME ENTERA en su salida.
FICHEROS_VEREDICTO = [
    ("SALIDA_V105_TAREA4_3_RE_BARRIDO.txt", "bloque"),
    ("SALIDA_V106_TAREA4_3_TRES_VIAS.txt", "bloque"),
    ("SALIDA_V107_TAREA4_3_TRAMO3_TRES_VIAS.md", "tabla"),
    ("SALIDA_V107_TAREA5_3_TRAMO1_TRES_VIAS.md", "tabla"),
    ("SALIDA_V108_TAREA3_3_TRES_VIAS_46.md", "tabla"),
]

RE_BLOQUE_CABECERA = re.compile(r"^--- PUESTO (\d+) ---")
RE_BLOQUE_VEREDICTO = re.compile(r"VEREDICTO:\s*(OBJETO|SATELITE|NO_OBJETO)\b")
RE_TABLA_FILA = re.compile(r"^(\d+)\s*\|.*\|\s*(OBJETO|SATELITE|NO_OBJETO)\b")


def extraer_bloque(texto):
    puestos = set()
    puesto_actual = None
    for linea in texto.splitlines():
        m = RE_BLOQUE_CABECERA.match(linea)
        if m:
            puesto_actual = int(m.group(1))
            continue
        if linea.strip() == "":
            puesto_actual = None
            continue
        if puesto_actual is not None and RE_BLOQUE_VEREDICTO.search(linea):
            puestos.add(puesto_actual)
            puesto_actual = None
    return puestos


def extraer_tabla(texto):
    puestos = set()
    for linea in texto.splitlines():
        m = RE_TABLA_FILA.match(linea)
        if m:
            puestos.add(int(m.group(1)))
    return puestos


def puestos_con_pregunta(ficheros, fallos):
    todos = set()
    for nombre, formato in ficheros:
        ruta = os.path.join(LOOP, nombre)
        if not os.path.exists(ruta):
            fallos.append("no existe %s (declarado en FICHEROS_VEREDICTO)" % nombre)
            continue
        texto = io.open(ruta, encoding="utf-8").read()
        if formato == "bloque":
            hallados = extraer_bloque(texto)
        elif formato == "tabla":
            hallados = extraer_tabla(texto)
        else:
            fallos.append("%s: formato %r desconocido" % (nombre, formato))
            continue
        todos |= hallados
    return todos


def vivas_de_hoy(fallos):
    d, f = cce.cifras(cce.TRAMOS_OP_E_03_POR_DEFECTO)
    if f:
        fallos.extend(f)
        return None
    todos_puestos = set(range(1, d["n"] + 1))
    return todos_puestos - set(d["sin_dir"])


def main():
    fallos = []
    vivas = vivas_de_hoy(fallos)
    ficheros = list(FICHEROS_VEREDICTO)

    con_pregunta_todos = puestos_con_pregunta(ficheros, fallos)

    if fallos or vivas is None:
        print("ROJO, %d cosa(s) no cuadran, NO SE CUENTA NADA:" % len(fallos))
        for x in fallos:
            print("   %s" % x)
        return 1

    con_pregunta = vivas & con_pregunta_todos
    sin_pregunta = sorted(vivas - con_pregunta_todos)

    print("FICHEROS DE ENTRADA (declarados en FICHEROS_VEREDICTO, %d):" % len(ficheros))
    for nombre, formato in ficheros:
        print("   %s (%s)" % (nombre, formato))
    print()
    print("RESUELTA vivas de hoy (contar_cierre_efectivo.cifras): %d" % len(vivas))
    print("con la pregunta de tres vias: %d" % len(con_pregunta))
    print("SIN la pregunta de tres vias: %d" % len(sin_pregunta))
    if sin_pregunta:
        print("LISTA NOMINAL de las que faltan: %s" % ", ".join(str(p) for p in sin_pregunta))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
